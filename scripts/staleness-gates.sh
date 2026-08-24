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
  # BLOCKING, and RED ON ARRIVAL -- 3 of 8. Owner-chosen 2026-08-24 (blocking
  # was picked over advisory and over deferring), bean qou-wee5.
  #
  # A LAYER STRADDLE is a witness whose value mixes the ideal (muon) and
  # experimental (proton) layers inside one computed quantity. This gate runs
  # each inline-q0 producer twice -- QOU_Q0_ANCHOR=physical, then =ideal -- and
  # fails if any NON-STAMP field moves. A producer with a q of its own should
  # move nothing but its stamp; if its numbers move, a second q reached them.
  #
  # COST. This is the only gate here that EXECUTES producers rather than
  # scanning files: 8 producers x 2 runs. The other four are static. Budget for
  # it accordingly, and use --timeout to bound a hung producer (an exceeded run
  # reports TIMEOUT = UNTESTED, never "clean").
  #
  # STATE: GREEN. clean=8, STRADDLE=0, measured on main 2026-08-24 (#5646).
  #
  # It ARRIVED red -- STRADDLE=3, per_generator_V_hat_general (24 fields),
  # xi_ell_phi_q_probe (36), t6_tau_h5_embedding_probe (15) -- and was drained
  # the same day rather than allowlisted. All three shared one carrier: the
  # Plancherel weights in `per_generator_V_hat_general`, built from
  # `hecke_characters.qfac` / `dim_q`, NEITHER OF WHICH TAKES A q. Both used the
  # module-level `q_int`, closing over the shim's Q -- so the weights read the
  # ENTRY POINT, which is how two probes that derive q0 inline from the muon
  # ratio, and reference the manifest nowhere, still moved under an anchor flip.
  #
  # No allowlist was seeded, deliberately, and that is why there is nothing to
  # unwind now: seeding a 3-entry allowlist would have been the "make it green
  # by widening a baseline" move AGENTS.md forbids, applied to the very defect
  # being gated. The gate went green because the defect went away.
  #
  # NOT the same as "the class is closed". `qfac`/`dim_q` still have 135
  # defaulted call sites across ~70 files (dim_q 78 of 119, qfac 57 of 59),
  # every one of them still reading the entry point. Nothing straddles today
  # only because the producers that combined two layers all funnelled through
  # that one function. Bean qou-wee5.
  # The 3 drain via qou-wee5.
  #
  # WHAT IT CANNOT DO. Only --candidates (inline closed-form q0) is sound.
  # --literal reports MOVES, not STRADDLE: its selector cannot tell a computed
  # second anchor from a documented one, a selftest constant, or a deliberate
  # comparison leg. Do not wire --literal here. And a producer whose q reaches
  # ONLY stamps is vetoed as STAMP-ONLY, not counted (bean qou-bdkx).
  "anchor-flip layer straddle|computations/audits/anchor_flip_straddle_audit.py|--candidates --timeout 300|yes"
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
# A full run on `main` exits 1. Re-measured 2026-08-23; the set SHRANK, and the
# correction matters more than the count:
#
#   scriptHash + upstream drift   RED   dominated by sha256_mismatch against
#                                       q-pinning-50-digit.witness.json
#   q0 constant staleness         RED   6 witnesses in the muon basin
#   anchor-flip layer straddle    green clean=8 / STRADDLE=0. Added 2026-08-24
#                                       red on arrival (3 of 8) by choice, and
#                                       drained the same day in #5646 -- one
#                                       shared carrier, no allowlist to unwind
#   qou-mass vendor mirror        green as of this commit, and it has now gone
#                                       red TWICE from two unrelated causes:
#
#     2026-08-22, TRANSIENT: the qou-ishr float64 drain (945b2edf2f,
#     e005856e18) rewrote source witnesses, drifting the mirror; that arc's own
#     follow-ups re-synced it (09571f1b3f, c1c8f34bfa). Nothing to fix.
#
#     2026-08-23, STANDING: `char_fast` moved to computations/substrate/ and
#     then gained a q-pinning guard in 6a8d41bf89; the mirror stayed 8 days
#     stale against it, so the packaged `qou-mass` shipped a char_fast WITHOUT
#     that guard. Re-synced here with `--apply`. This one was real.
#
#     2026-08-23, STANDING (third red, and the first one a human never saw):
#     two files, both drifted because the arc that moved their SOURCE never ran
#     `--apply`.
#
#       ame-2020-binding-energies.witness.json          src 03c25e8dbf 08-19
#                                                       mirror synced 08-23
#                                                       -> FOUR DAYS standing
#       data/m-p-borromean-verification-50dps.witness   src f0ef496482 08-23
#                                                       mirror synced 08-23
#
#     Neither self-corrected, so both are STANDING by the test above, not
#     transient. Re-synced with `--apply` in e563c491d9.
#
#     THE INSTRUCTIVE PART IS NOT THE DRIFT. This gate DID fire -- the agent
#     that caused it ran this script, saw `RED: ... qou-mass vendor mirror` in
#     its own output, read past it, rediscovered the same drift by hand an hour
#     later, and then wrote in a merged PR body that `--check` "is simply not
#     wired into precision-gates.sh or staleness-gates.sh". It is wired, at the
#     array entry 20 lines above, blocking, and had been for a day.
#
#     So the qou-j6gb pattern this file was built to close ("the checker
#     exists, works, ships --check, and is in no array") has a successor mode:
#     the checker exists, works, IS in the array, fires -- and the reader
#     skims the summary line. A gate that is not read is not a gate. If you are
#     an agent running this script, the RED list at the end is the deliverable,
#     not the exit code.
#
#   The two look identical from a single `--check`. Only the git history
#   separates them, which is why the rule below is re-measure, not re-run.
#
# THE LESSON, because it cost a bean an over-claim: A RED MEASURED ONCE ON MAIN
# MAY BE MID-ARC, NOT PERSISTENT. A sibling that lands a source change in one
# commit and its derived artifact in the next is red in between, and a snapshot
# taken there reads exactly like a standing backlog. Re-measure before treating
# any red here as work.
#
# Check a clean worktree before spending time on the two that remain:
#
#   git worktree add --detach /tmp/mainwt origin/main
#   (cd /tmp/mainwt && bash scripts/staleness-gates.sh)
#
# AND THE TWO REMAINING ARE NOT ONE BACKLOG EITHER. Of the 6 witnesses the q0
# gate flags, measured 2026-08-23: 2 declare `q0Anchor: muon` AND carry a muon
# q0 -- self-consistent, valid as recorded, and part of the GATED bulk
# migration (bean qou-1c4y, needs scoped sign-off; do not drain them here). The
# other 4 are a different defect entirely -- their declared anchor CONTRADICTS
# their payload:
#
#   lever1-color-eq-intrinsic-tau-rapidity   declares proton, carries muon
#   lever1-color-eq-lambda-sw-rapidity       declares proton, carries muon
#   z2bn-tau-derivation-probe                declares `independent`
#                                            ("reads no substrate value") and
#                                            records .q0 = 1.10997859555733...
#   knot-volumes                             declares no anchor at all
#
# Those 4 are actionable WITHOUT the gated migration, because fixing them means
# reconciling a declaration with a payload, not re-pinning the corpus. Which
# side is wrong is per-witness and needs the producer read. Bean qou-bdkx.
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
  considered=$(changed_files)
  relevant=$(printf '%s\n' "$considered" \
             | grep -E '(\.witness\.json$|^computations/.*\.py$)' || true)
  # A SKIP IS NOT A PASS (#5495, requested by the sibling on #5453). "0 files
  # considered" and "N considered, none relevant" were the same sentence, and
  # they are not the same fact: the first means this gate examined NOTHING.
  # The scope line says what was compared, so a caller can tell a genuine skip
  # from the merge-base half having been dropped.
  if [ -z "$relevant" ]; then
    echo "staleness-gates: 0 relevant of $(printf '%s\n' "$considered" | grep -c .) changed file(s) — skipped."
    echo "  scope: $(changed_files_scope)"
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
