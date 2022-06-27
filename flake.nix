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
