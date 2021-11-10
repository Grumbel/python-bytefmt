{
  description = "Python library to format bytes into a human readable format";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    nix.inputs.nixpkgs.follows = "nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nix, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in rec {
        packages = {
          bytefmt = pkgs.python3Packages.buildPythonPackage rec {
            name = "bytefmt";
            src = self;
          };
        };
        defaultPackage = packages.bytefmt;
      });
}
