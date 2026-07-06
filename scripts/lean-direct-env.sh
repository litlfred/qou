# Source this to verify a single QOU .lean with restored oleans (no lake build).
#   source scripts/lean-direct-env.sh && lean <file>   # exit 0 = checks, sorry-free
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
_lp=$(find .lake -type d -path '*/build/lib/lean' 2>/dev/null | tr '\n' ':')
_qou=$(find content/quantum-observable-universe/lean -type d -path '*/build/lib/lean' 2>/dev/null | tr '\n' ':')
export LEAN_PATH="${_lp}${_qou}"
