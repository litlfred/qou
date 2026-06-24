#!/bin/zsh
export PATH="$HOME/.elan/bin:$PATH"
ROOT="/Users/litlfred/space_cats/qou"
LP=$(find "$ROOT/.lake/packages" -maxdepth 5 -type d -path '*/.lake/build/lib/lean' | tr '\n' ':')
LP="$LP$ROOT/.lake/build/lib/lean:$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean"
export LEAN_PATH="$LP"
echo "LEAN_PATH is $LEAN_PATH"
echo "Running lean..."
ELAN_NO_OVERRIDE_NOTICE=1 lean "$ROOT/content/quantum-observable-universe/lean/QOU/HyperellipticQuintic/zeta5_residue_monodromy.lean"
