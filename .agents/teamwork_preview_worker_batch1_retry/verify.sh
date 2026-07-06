#!/bin/bash
set -e
export PATH="$HOME/.elan/bin:$PATH"
ROOT="/Users/litlfred/space_cats/qou"
TGZ=$(mktemp)
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)
BR="lake-cache/qou-$SLUG"
echo "Fetching cache from branch $BR..."
git fetch --depth=1 origin "$BR"
git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort | while read -r p; do git show "FETCH_HEAD:$p"; done > "$TGZ"
tar xzf "$TGZ" -C "$ROOT"
echo "Restored .lake oleans successfully."

LP=$(find "$ROOT/.lake/packages" -maxdepth 5 -type d -path '*/.lake/build/lib/lean' | tr '\n' ':')
LP="$LP$ROOT/.lake/build/lib/lean:$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean"
export LEAN_PATH="$LP"
echo "Compiling zeta5_residue_monodromy.lean..."
ELAN_NO_OVERRIDE_NOTICE=1 lean "$ROOT/content/quantum-observable-universe/lean/QOU/HyperellipticQuintic/zeta5_residue_monodromy.lean"
echo "Compilation check passed!"
