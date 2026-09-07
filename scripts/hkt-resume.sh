#!/usr/bin/env bash
# hkt-resume.sh — resume the hadron knot table safely after a container reset.
#
# The table (bean qou-uiut) outlives its container: the box suspends every
# 10-15 minutes and kills the run. Two artifacts carry it across:
#
#   .work/hkt-uiut-ckpt.json   completed atoms. TRACKED IN GIT deliberately --
#                              it was untracked once and a reset cost 16 atoms,
#                              about 9.5 hours of compute. 23KB.
#   .work/kernel-memo/         partial work WITHIN an unfinished atom.
#                              gitignored (37MB, derived) and rebuilt from
#                              scratch after a reset -- which is why a fresh
#                              container is slow, not wrong.
#
# THE CHECK THAT MATTERS is neither of those. If `pyhecke_native` lacks
# `lp_accumulator_step_traces_mpfr`, `hecke_core_legacy.py:1367` falls back to
# `_build_ysn_matrices`, which VIOLATES the braid relation -- not a
# representation of H_n(q), so its products are not Markov traces of braids.
#
# That fallback is SILENT IN THE NUMBERS. On 2026-09-07 it produced proton,
# neutron and protium byte-identical to a known-good run
# (0.629328 / 0.475134 / 1.146338) and diverged only on compounds, 17.3% at
# deuterium. A run left going writes a checkpoint and a witness that look
# entirely normal. So this script REFUSES TO START without the symbol, rather
# than trusting whoever runs it to remember.
#
# Usage:  scripts/hkt-resume.sh [--commit]
#           --commit   also `git add -f` + commit the checkpoint if it advanced
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CKPT="$ROOT/.work/hkt-uiut-ckpt.json"
MEMO="$ROOT/.work/kernel-memo"
LOG="${HKT_LOG:-$ROOT/.work/hkt-run.log}"

commit_checkpoint() {
  # Deliberately callable on BOTH paths. The first version put this after the
  # "already running" early exit, so `--commit` was skipped exactly when the
  # run was healthy -- the checkpoint went uncommitted for as long as nothing
  # went wrong, which is the opposite of what it is for. Found by using it.
  [ "${1:-}" = "--commit" ] || return 0
  [ -f "$CKPT" ] || return 0
  if git -C "$ROOT" diff --quiet -- "$CKPT" 2>/dev/null && \
     git -C "$ROOT" ls-files --error-unmatch "$CKPT" >/dev/null 2>&1; then
    echo "[hkt] checkpoint unchanged — nothing to commit"
    return 0
  fi
  n=$(python3 -c "import json,sys; print(len(json.load(open(sys.argv[1]))['atoms']))" "$CKPT")
  git -C "$ROOT" add -f "$CKPT"
  git -C "$ROOT" commit -q -m "chore(qou-uiut): checkpoint ${n}/19" && \
    echo "[hkt] committed checkpoint at ${n}/19"
}

if pgrep -x python3 >/dev/null 2>&1 && \
   ps -eo cmd --no-headers | grep -q "^python3 computations/hadron_knot_table.py"; then
  echo "[hkt] already running — not starting a second producer in one checkout."
  commit_checkpoint "${1:-}"
  exit 0
fi

echo "[hkt] gate: pyhecke_native.lp_accumulator_step_traces_mpfr"
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
  echo "[hkt] REFUSING TO START. Without the LP kernel this run produces numbers" >&2
  echo "      that are NOT the framework's (braid relation violated) while looking" >&2
  echo "      entirely normal on A=1. Fix: scripts/build-pyhecke-native.sh" >&2
  exit 1
}

if [ -f "$CKPT" ]; then
  python3 -c "import json,sys; print('[hkt] checkpoint:', len(json.load(open(sys.argv[1]))['atoms']), 'of 19')" "$CKPT"
else
  echo "[hkt] no checkpoint — starting from zero"
fi
echo "[hkt] memo entries: $(find "$MEMO" -type f 2>/dev/null | wc -l)"

mkdir -p "$ROOT/.work"
cd "$ROOT" || exit 1
nohup env QOU_HKT_CHECKPOINT="$CKPT" QOU_KERNEL_MEMO="$MEMO" \
      python3 computations/hadron_knot_table.py > "$LOG" 2>&1 < /dev/null &
disown
echo "[hkt] started; log $LOG"

# The gate above proves the symbol is importable HERE. This proves the RUN is
# using it -- a different question, and the cheaper one to get wrong.
sleep 20
if grep -q "WARNING: pyhecke_native" "$LOG" 2>/dev/null; then
  echo "[hkt] FALLBACK WARNING IN THE RUNNING PROCESS — killing it." >&2
  pkill -f "^python3 computations/hadron_knot_table.py"
  exit 1
fi
echo "[hkt] no fallback warning in the started run"

commit_checkpoint "${1:-}"
