#!/usr/bin/env bash
# staleness-gates.sh — unified witness-staleness gate family.
#
# WHY THIS EXISTS
# ---------------
# Two independent stale-audit instances hit during one rebase (PR #4929):
#   - main's L1 green: onepb-status-dashboard.witness.json predated a
#     precision-limit finding and was not invalidated.
#   - charm-* audit counts: chapter audit aggregates drifted during rebase
#     without any checker flagging it.
#
# The general failure mode: an audit whose own witness isn't regenerated when
# its inputs change reports yesterday's answer with today's authority.
#
# precision-gates.sh covers the PRECISION family (float64, mpf, q₀ values).
# This script covers the STALENESS family:
#   - scriptHash drift (producer code changed, witness not regenerated)
#   - upstream dependency drift (an input witness changed, consumer not re-run)
#   - q₀ constant drift (q₀ repinned, witness carries the old value)
#   - dependency coverage (witnesses with no upstream_witness_hashes declared)
#
# USAGE
#   scripts/staleness-gates.sh              # run every gate
#   scripts/staleness-gates.sh --changed    # skip if no witness/script touched
#   scripts/staleness-gates.sh --list       # print the gate list and exit
#
# EXIT CODE
#   0  every blocking gate green
#   1  at least one blocking gate red
#   2  preflight failed (missing modules, can't evaluate)
#
# DO NOT SUPPRESS A RED BY EDITING THE WITNESS.
#   Fix at the producer: re-run the script that generates the witness.
#   A stale witness that is manually updated to look fresh is worse than
#   a stale witness that says it's stale.
set -uo pipefail

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 0; }
cd "$ROOT"

# Shared changed-file collection. ONE definition, so the fifth gate script
# cannot repeat the defect the first four shared (bean qou-pt9b).
. "$ROOT/scripts/lib/changed-files.sh"

# name|script|args|blocking?
# Notes:
#   - witness_dependency_drift.py --strict gates on BOTH upstream + self staleness.
#     Use --self-strict for self-only, --no-self for upstream-only.
#   - witness_constant_staleness.py checks q₀ value drift (complements the
#     precision-gates q0-anchor check, which validates the anchor FORMULA;
#     this validates the q₀ VALUE embedded in witness outputs).
#   - witness_dependency_coverage_audit.py flags witnesses that don't declare
#     upstream_witness_hashes — the root cause of the "silent stale" class.
GATES=(
  "scriptHash + upstream drift|computations/witness_dependency_drift.py|--strict|yes"
  "q0 constant staleness|computations/substrate/witness_constant_staleness.py|--strict|yes"
  "dependency coverage|computations/audits/witness_dependency_coverage_audit.py|--strict|no"
  # BLOCKING, and green on arrival. Bean qou-cdj8.
  #
  # The vendored qou-mass mirror is the same failure this file exists for, one
  # package over: a copy whose source moved and was never regenerated, reporting
  # yesterday's answer with today's authority. It belongs in the STALENESS
  # family, not the precision one -- nothing about it is float64.
  #
  # It had no runner at all. AGENTS.md calls `--check` "the gate", and a grep of
  # every .sh and .yml found nothing invoking it, which is why the mirror went
  # red again four days after the ratchet was built (bean qou-wpp2) and why two
  # separate agents independently re-measured the same drift. Fourth instance of
  # the qou-j6gb pattern this repo keeps hitting: the checker exists, works,
  # ships --check, and is in no array.
  #
  # Blocking from the start rather than advisory, because it is GREEN on arrival
  # -- the objection in precision-gates.sh (a gate red on arrival gets skipped)
  # does not apply here. Coverage as of 2026-08-22: 42 modules, 18 cone
  # witnesses, 122 package-data witnesses, 0 uncovered.
  "qou-mass vendor mirror|scripts/sync-qou-mass-vendor.py|--check|yes"
)

if [ "${1:-}" = "--list" ]; then
  printf '%-28s %-58s %s\n' "GATE" "SCRIPT" "BLOCKING"
  for g in "${GATES[@]}"; do
    IFS='|' read -r name script _args blocking <<<"$g"
    printf '%-28s %-58s %s\n' "$name" "$script" "$blocking"
  done
  exit 0
fi

# 🛑 THIS SCRIPT IS RED ON `main` — MEASURED, NOT INHERITED FROM YOUR BRANCH.
#
# A full run on a pristine origin/main worktree (2026-08-22) exits 1 on three
# gates: `scriptHash + upstream drift`, `q0 constant staleness`, and `qou-mass
# vendor mirror`. If you see those three, they are almost certainly not yours —
# check a clean worktree before spending time on them:
#
#   git worktree add --detach /tmp/mainwt origin/main
#   (cd /tmp/mainwt && bash scripts/staleness-gates.sh)
#
# WHY NOBODY KNEW. Until 2026-08-22 the `--changed` predicate below read the
# working tree only, so it printed "nothing touched — skipped" for any change
# that had been COMMITTED, which is most of them. The gate has been red for an
# unknown length of time with nothing reporting it. Tracked as bean qou-p8lx.
#
# This is the failure this file's sibling (precision-gates.sh) warns about at
# its top — "a gate that is red on arrival gets skipped, which is how a checker
# goes quiet" — reached by a different route: not red-on-arrival, but
# never-actually-run. Do NOT respond by narrowing the predicate again, and do
# NOT baseline the offenders. Drain them at the producers.

if [ "${1:-}" = "--changed" ]; then
  # THE MERGE-BASE DIFF IS NOT OPTIONAL -- third instance of the qou-s2gm
  # defect-1 shape, after precision-gates.sh and check-sidecars.sh. All three
  # working-tree sources see only UNCOMMITTED work, so once a change is
  # committed the set goes empty, this prints "nothing touched -- skipped" and
  # exits 0, and that is indistinguishable from a real pass. AGENTS.md tells
  # every agent to commit early and often, so verifying after committing is
  # the natural order.
  #
  # On `main` the merge-base IS HEAD, so this adds nothing on a clean checkout.
  relevant=$(changed_files \
             | grep -E '(\.witness\.json$|^computations/.*\.py$)' || true)
  if [ -z "$relevant" ]; then
    echo "staleness-gates: no witness or computations/ script touched — skipped."
    exit 0
  fi
fi

# Preflight: check Python dependencies.
missing=$(python3 - <<'PREFLIGHT_PY'
import importlib.util
need = []  # no third-party deps for the staleness family
print(" ".join(m for m in need if importlib.util.find_spec(m) is None))
PREFLIGHT_PY
)
if [ -n "$missing" ]; then
  echo "PREFLIGHT FAILED — the staleness gates could not be evaluated."
  echo "  missing Python module(s): $missing"
  exit 2
fi

blocking_failed=()
advisory_failed=()

for g in "${GATES[@]}"; do
  IFS='|' read -r name script args blocking <<<"$g"
  printf '\n\033[1m▸ %s\033[0m  (%s)\n' "$name" "$script"
  if [ ! -f "$script" ]; then
    echo "  MISSING: $script — the gate list is out of date with the tree."
    if [ "$blocking" = "yes" ]; then
      blocking_failed+=("$name (script missing)")
    else
      advisory_failed+=("$name (script missing)")
    fi
    continue
  fi
  out=$(python3 "$script" $args 2>&1); rc=$?
  printf '%s\n' "$out" | sed 's/^/  /' | head -25
  if [ $rc -ne 0 ]; then
    if [ "$blocking" = "yes" ]; then
      blocking_failed+=("$name")
    else
      advisory_failed+=("$name")
    fi
  fi
done

echo
echo "======================================================================"
if [ ${#advisory_failed[@]} -gt 0 ]; then
  echo "ADVISORY (not gating): ${advisory_failed[*]}"
fi
if [ ${#blocking_failed[@]} -gt 0 ]; then
  echo "RED: ${blocking_failed[*]}"
  echo
  echo "Fix AT THE PRODUCER. Re-run the script that generates the stale witness."
  echo "Do not hand-edit a witness to make this green."
  exit 1
fi
echo "All staleness gates green."
