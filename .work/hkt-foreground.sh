#!/usr/bin/env bash
# hkt-foreground.sh — run the table IN THE FOREGROUND of whatever launched it.
#
# The point is the lifecycle, not the compute. `scripts/hkt-resume.sh` launches
# with `nohup ... & disown`, and bean qou-6cm9 records that setsid/nohup jobs
# DIE at session boundaries while the harness's own run_in_background survives.
# Measured here 2026-09-13: nohup'd runs were killed by the SessionStart:resume
# boundaries at 11:38, 12:25 and 12:54, and the nohup'd supervisor died with
# them. So this script does NOT background anything; it is meant to BE the
# harness task, which then owns the process group.
#
# qou-6cm9's open question is exactly this: "survives a 31-min idle gap is
# measured; survives a RESUME is not." Running the table this way answers it,
# either way, on the next resume.
#
# It keeps hkt-resume.sh's two safety properties, which are not optional:
#   1. the LP-kernel gate -- without `lp_accumulator_step_traces_mpfr` the run
#      violates the braid relation and is wrong in a way that looks entirely
#      normal on A=1 and diverges only at compounds;
#   2. the single-producer guard.
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CKPT="$ROOT/.work/hkt-uiut-ckpt.json"
MEMO="$ROOT/.work/kernel-memo"
LOG="$ROOT/.work/hkt-run.log"
cd "$ROOT" || exit 1

if ps -eo cmd --no-headers 2>/dev/null \
     | grep -q '^python3 computations/hadron_knot_table.py'; then
  echo "[hkt-fg] already running — refusing to start a second producer."
  exit 0
fi

echo "[hkt-fg] gate: pyhecke_native.lp_accumulator_step_traces_mpfr"
python3 - <<'PY' || {
import sys
try:
    import pyhecke_native as pn
except Exception as e:                                   # noqa: BLE001
    print(f"  pyhecke_native will not import: {type(e).__name__}: {e}")
    sys.exit(1)
if not hasattr(pn, "lp_accumulator_step_traces_mpfr"):
    print("  LP kernel MISSING")
    sys.exit(1)
print("  LP kernel present")
PY
  echo "[hkt-fg] REFUSING TO START — without the LP kernel the numbers are not" >&2
  echo "         the framework's, and A=1 still looks normal." >&2
  exit 1
}

if [ -f "$CKPT" ]; then
  python3 -c "import json,sys; print('[hkt-fg] checkpoint:', len(json.load(open(sys.argv[1]))['atoms']), 'of 19')" "$CKPT"
else
  echo "[hkt-fg] no checkpoint — starting from zero"
fi
echo "[hkt-fg] memo entries: $(find "$MEMO" -type f 2>/dev/null | wc -l)"
echo "[hkt-fg] starting in the FOREGROUND; log also at $LOG"

exec env QOU_HKT_CHECKPOINT="$CKPT" QOU_KERNEL_MEMO="$MEMO" \
     python3 -u computations/hadron_knot_table.py 2>&1 | tee -a "$LOG"
