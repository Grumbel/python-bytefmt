{
  description = "Python library to format bytes into a human readable format";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-22.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = flake-utils.lib.flattenTree {
          bytefmt = pkgs.python3Packages.buildPythonPackage {
            name = "bytefmt";
            src = nixpkgs.lib.cleanSource ./.;
          };
        };
        defaultPackage = packages.bytefmt;
      });
}
