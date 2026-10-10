#!/usr/bin/env bash
# lean-blocks-lake-probe — story LEANNODES L1 (bean qou-hs14): can Lake build
# the content-block Lean siblings where they sit?
#
#   R1  Does Lake accept kebab-case globs / module names (the chapter and
#       block directories are kebab-case: braids-and-knots/jones-at-q0.lean)?
#   R2  May a [[lean_lib]] srcDir point OUTSIDE the package (srcDir = "..")?
#   FB  The fallback: a generated shadow tree of identifier-safe symlinks.
#
# Builds a throwaway package in a temp dir with no Mathlib, so it needs only a
# Lean toolchain matching ./lean-toolchain on PATH (`lake`). It touches nothing
# in the repository. Exit 0 always; the verdicts are printed.
#
#   bash scripts/lean-blocks-lake-probe.sh
set -u
command -v lake >/dev/null || { echo "UNKNOWN: no lake on PATH (need $(cat "$(dirname "$0")/../lean-toolchain"))"; exit 0; }
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/paper/lean/QOU" "$T/paper/braids-and-knots" "$T/paper/mass-theory"
cd "$T/paper"
printf 'import QOU.Base\n' > lean/QOU.lean
printf 'namespace QOU\ndef two : Nat := 2\nend QOU\n' > lean/QOU/Base.lean
printf 'import QOU.Base\nnamespace QOU.Probe\ntheorem two_eq : QOU.two = 2 := rfl\nend QOU.Probe\n' > braids-and-knots/jones-at-q0.lean
printf 'namespace QOU.Probe2\ntheorem t : 1 + 1 = 2 := rfl\nend QOU.Probe2\n' > mass-theory/rho-k-h3a-refinement.lean
cp "$(dirname "$0")/../lean-toolchain" lean/lean-toolchain 2>/dev/null || true
lakefile() { # srcDir, globs
  cat > lean/lakefile.toml <<TOML
name = "qou"
defaultTargets = ["QOU"]
[[lean_lib]]
name = "QOU"
srcDir = "."
globs = ["QOU", "QOU.+"]
[[lean_lib]]
name = "QOUBlocks"
srcDir = "$1"
globs = $2
TOML
}
try() { (cd lean && rm -rf .lake && lake build QOUBlocks >"$T/out.txt" 2>&1) && echo PASS || echo "FAIL ($(grep -m1 -i error "$T/out.txt"))"; }

lakefile ".." '["braids-and-knots.+", "mass-theory.+"]'
echo "R1  kebab-case globs, srcDir \"..\":          $(try)"
lakefile ".." '["«braids-and-knots».+", "«mass-theory».+"]'
echo "R1' guillemet-quoted kebab globs:              $(try)"
mkdir -p BraidsAndKnots MassTheory
cp braids-and-knots/jones-at-q0.lean BraidsAndKnots/JonesProbe.lean
cp mass-theory/rho-k-h3a-refinement.lean MassTheory/RhoProbe.lean
lakefile ".." '["BraidsAndKnots.+", "MassTheory.+"]'
echo "R2  srcDir \"..\" with identifier-safe names:   $(try)"
rm -rf BraidsAndKnots MassTheory
mkdir -p lean/blocks-shadow/BraidsAndKnots lean/blocks-shadow/MassTheory
ln -s ../../../braids-and-knots/jones-at-q0.lean lean/blocks-shadow/BraidsAndKnots/JonesAtQ0.lean
ln -s ../../../mass-theory/rho-k-h3a-refinement.lean lean/blocks-shadow/MassTheory/RhoKH3aRefinement.lean
lakefile "blocks-shadow" '["BraidsAndKnots.+", "MassTheory.+"]'
echo "FB  symlink shadow tree:                       $(try)"
printf 'theorem extra : 2 + 2 = 4 := rfl\n' >> mass-theory/rho-k-h3a-refinement.lean
(cd lean && lake build QOUBlocks 2>&1 | grep -q "Built MassTheory.RhoKH3aRefinement") && echo "FB  edit to the real file rebuilds through link: PASS" || echo "FB  edit rebuild: FAIL"
