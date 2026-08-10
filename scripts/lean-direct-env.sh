# Source this to verify a single QOU .lean with restored oleans (no lake build).
#   source scripts/lean-direct-env.sh && lean <file>   # exit 0 = checks, sorry-free
#
# LEAN_PATH entries are ABSOLUTE, deliberately.  They used to come from
# `find .lake ...` — relative — which works only while `lean` is invoked from the
# repo root.  `scripts/lean-axiom-guard.py` writes its probe to a TEMP FILE and
# runs `lean` there, so every relative entry missed and the guard failed with a
# thoroughly misleading
#
#     error: unknown module prefix 'QOU'
#     No directory 'QOU' or file 'QOU.olean' in the search path entries: ...
#
# while `QOU.olean` was sitting in a listed directory the whole time.  Rooting the
# find at the script's own repo (not at `$PWD`, which is the caller's) fixes every
# consumer at once.  Measured 2026-08-10.
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
_root=$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")/.." && pwd)
_lp=$(find "$_root/.lake" -type d -path '*/build/lib/lean' 2>/dev/null | tr '\n' ':')
_qou=$(find "$_root/content/quantum-observable-universe/lean" -type d -path '*/build/lib/lean' 2>/dev/null | tr '\n' ':')
export LEAN_PATH="${_lp}${_qou}"
unset _root _lp _qou
