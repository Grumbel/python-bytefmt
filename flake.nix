{
  description = "Python library to format bytes into a human readable format";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    let
      bytefmtWithPythonPackages = (pythonPackages:
          pythonPackages.buildPythonPackage {
            name = "bytefmt";
            src = nixpkgs.lib.cleanSource ./.;
            checkInputs = (with pythonPackages; [
              flake8
              mypy
              pylint
            ]);
            checkPhase = ''
              runHook preCheck
              flake8 bytefmt tests
              # pyright bytefmt tests
              mypy bytefmt tests
              pylint bytefmt tests
              python3 -m unittest discover -v -s tests/
              runHook postCheck
            '';
          }
        );
    in
      {
        lib = {
          inherit bytefmtWithPythonPackages;
        };
      } //
      flake-utils.lib.eachDefaultSystem (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          pythonPackages = pkgs.python3Packages;
        in rec {
          packages = flake-utils.lib.flattenTree rec {
            bytefmt = bytefmtWithPythonPackages pythonPackages;
            default = bytefmt;
          };
        }
      );
}
