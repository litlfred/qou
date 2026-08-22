#!/usr/bin/env bash
# precision-gates.sh — run the whole NO-FLOAT64 gate family as ONE preflight.
#
# WHY THIS EXISTS
# ---------------
# Every gate below was already written, already strict, and already wired into
# `.github/workflows/witness-staleness.yml`. Three dirty witnesses still reached
# `origin/main` (bean qou-mnrd). The reason is not a missing gate — it is that
# the workflow carrying them is `workflow_dispatch:` only, per the owner's
# 2026-06-30 Actions-billing directive. Nothing runs them on a push, so nothing
# ran them at all.
#
# Turning the trigger back on is an owner decision about money, not an agent
# decision. What IS an agent decision is AGENTS.md §"QA is agent-owned; CI is a
# backup": run the checks that apply to your own change, by hand, before
# committing. This script is that preflight for the precision family, in the
# same idiom as scripts/check-sidecars.sh.
#
# USAGE
#   scripts/precision-gates.sh              # run every gate (~40s)
#   scripts/precision-gates.sh --changed    # no-op unless this change touches
#                                           # a witness or a computations/ script
#   scripts/precision-gates.sh --list       # print the gate list and exit
#
# EXIT CODE
#   0  every blocking gate green
#   1  at least one blocking gate red  (the run does NOT stop at the first
#      failure — a preflight that hides four reds behind one is worse than none)
#
# ADVISORY, NOT BLOCKING
#   `no_free_parameter_certificate.py` is red BY DESIGN on A_omega = 3 and is
#   declared fail-open in the workflow for a documented reason (an open research
#   question, qou-qnnq). It is run and reported here, and never gates.
#
# DO NOT MAKE A RED RUN GREEN BY WIDENING A BASELINE.
#   Each gate says so in its own output. Fix at the producer: carry the value as
#   mpmath.mpf from its source and serialize with _precision.fmt. Adding a file
#   to raw-float64-baseline.json or mpf-import-time-dps-baseline.json, or
#   --rebaseline'ing to go green, defeats the mechanism the gate exists to
#   provide. Baselines drain, never grow.
#
# A GATE OUTSIDE THIS ARRAY IS A GATE NOBODY RUNS. (2026-08-10, bean qou-j6gb)
#   `mpf_import_time_dps_audit.py` was written 2026-08-07, worked from the start,
#   and was in no array — not here, so nothing ran it. Its defect class then
#   landed five more times, each caught instead by a different gate reacting to a
#   downstream symptom. It was added here as a ratchet (baseline 91 files / 185
#   proven-lossy / 103 position-risky) rather than pass/fail, because a gate that
#   is red on arrival gets skipped, which is how a checker goes quiet. When you
#   write a detector, wiring it here is the half that makes it a gate.
set -uo pipefail

ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "not a git repo"; exit 0; }
cd "$ROOT"

# name|script|args|self-test?|blocking?
GATES=(
  "q0-anchor flip|computations/audits/q0_anchor_consistency_audit.py|--strict|no|yes"
  "mpf(<float>) source|computations/mpf_float_source_audit.py|--strict|yes|yes"
  "import-time dps ratchet|computations/mpf_import_time_dps_audit.py|--strict|yes|yes"
  "never-raises-dps ratchet|computations/never_raises_dps_audit.py|--strict|yes|yes"
  "float64-padding ratchet|computations/witness_float64_padding_audit.py|--strict|yes|yes"
  "mp.dps no-op|computations/mpf_context_dps_audit.py|--strict|yes|yes"
  "module-const precision|computations/module_const_precision_audit.py|--strict|yes|yes"
  "raw-float64 ratchet|computations/witness_raw_float64_audit.py|--strict|yes|yes"
  # Paired with the ratchet above and deliberately independent of it: the
  # ratchet counts raw floats, so a GUTTED witness scores zero and reads as a
  # perfect drain. This one asks the orthogonal question — did the witness lose
  # content? — by diffing shape against HEAD. Bean qou-h4xk; measured twice on
  # rho-k-co-casimir-extended, where a partial write showed 4 -> 0 raw floats
  # with durationMs 2,552,837 -> 519. Neither gate subsumes the other.
  "witness shape guard|computations/witness_shape_guard.py||yes|yes"
  "q0-value drift ratchet|computations/q0_value_drift_audit.py|--strict|no|yes"
  # BLOCKING, and green on arrival because the 111-witness backlog is
  # baselined. The mirror of `witness_hollowness_audit` (which catches
  # `allPassed: true` with `assertions: []` — green with nothing behind it):
  # this catches a witness committed with its failure RECORDED INSIDE IT.
  #
  # A recorded-but-unread failure is strictly worse than no check, because the
  # check's existence is what stops anyone looking. Motivating case, bean
  # qou-4e5k: `tr-m-algebraic-q.witness.json` carried
  # `symbolic_delta_matches_li2q computed=1.338e-06 tol=1e-12 passed=false`
  # from 2026-08-09 — naming a real δ defect numerically — and was
  # rediscovered twelve days later by hand-measuring a deuteron trace.
  #
  # Baselined at 111 witnesses / 137 assertions rather than run red, because
  # this file's own comments (see the provenance entry below) record that a
  # gate red on arrival gets skipped, which is how a checker goes quiet.
  # Counts shrink, never grow. Drain triage is bean qou-ad4t; the category to
  # identify first is the probe that records an EXPECTED negative, since every
  # such witness teaches readers that red is normal.
  #
  # ADVISORY ON ARRIVAL, AND THIS IS THE FLIP-TO-BLOCKING NOTE.
  # ----------------------------------------------------------
  # FLIP TO BLOCKING WHEN THE NEW-OFFENDER COUNT REACHES 0 — i.e. when a plain
  # run reports no witness outside the baseline. Same terms as the
  # audits-tree entry above, and the same precedent this file set for its
  # red-on-arrival provenance gate.
  #
  # It was authored BLOCKING and green at 111. Between authoring and merge,
  # `main` gained a 112th (`computations/probes/qbeta-habiro-residual.witness.json`,
  # `Q_A_witness_matches_live_single_wrap computed=29.959 expected=0.0
  # tolerance=1.0`, landed by ae571e445d). Shipping it blocking would therefore
  # have made THIS SCRIPT exit 1 on `main` for every other agent — over a
  # witness that has nothing to do with the branch introducing the gate.
  #
  # That is the failure this gate exists to prevent, arriving one level up: a
  # preflight that is red for reasons you did not cause is a preflight you
  # learn to skip. Advisory keeps the signal and costs nobody a red run.
  #
  # The two shortcuts were BOTH refused, and neither should be taken later:
  #   * do NOT add the offender to the baseline — the ratchet drains and never
  #     grows (AGENTS.md), and a baseline that absorbs each new arrival is not
  #     a ratchet;
  #   * do NOT "fix" qbeta-habiro-residual to clear this — it is a 30x
  #     residual, not a tolerance nudge, and it belongs to the live qbeta
  #     proton re-pin arc (#5386). Editing it steps on a sibling mid-flight.
  # Drain owners: bean qou-6ort (the dps defect) and the qbeta re-pin arc.
  "witness failed-assertion ratchet|computations/witness_failed_assertion_audit.py|--strict|yes|no"
  # Blocking, and GREEN as of the commit that added it (0 candidates across
  # 273 numpy-importing files) — which is exactly when a gate is safe to make
  # blocking, because it can then only ever fire on a NEW regression.
  # Guards the mpmath/float64 boundary: an mpf reaching a numpy array demotes
  # it to dtype=object, silently leaving BLAS. Measured at ~4000x on
  # chi_numpy, invisible to compute_audit_scan, and misdiagnosed as slow
  # hardware for six hours. Bean qou-5qwb.
  "numpy/mpmath dtype leak|computations/numpy_mpmath_dtype_leak_audit.py||yes|yes"
  # ADVISORY, and it was never wired in at all until now (bean qou-d8gq).
  # This audit already names, in prose, the exact shape that cost 642x in
  # syt_prefix_cache -- "`BlockCache(float(Q0), float(HA_VAL))` seeds a cache
  # with doubles" -- and nothing ever ran it, so nobody read it. Advisory
  # rather than blocking because three of its five tiers are explicitly
  # circumstantial ("lists of places to look", per its own docstring), and a
  # gate that fails on a high-recall list gets muted rather than fixed.
  "f64-into-mpmath (advisory)|computations/f64_into_mpmath_audit.py||yes|no"
  # BLOCKING as of 2026-08-19, and green on arrival. Bean qou-irzg.
  #
  # It ran ADVISORY because the ratchet had no MEMORY for this tree, not
  # because the tree was dirty: the baseline's 1572 entries are all
  # computations/ paths, so every witness under docs/audits/scripts/ was
  # reported NEW on every run, forever. A ratchet with no memory is red on
  # arrival, and a gate that is red on arrival gets skipped — the rule this
  # file states at the top.
  #
  # That is the `_output_name` defect (qou-pgdw) one step removed. The OUTPUT
  # name was scoped to the scan root when that was fixed; the BASELINE was left
  # global. `_baseline_path` now derives it the same way, so this tree has its
  # own drains-only baseline and the corpus one is untouched — establishing
  # coverage where there was none, which is a different act from silencing a
  # regression in a tree that already has it.
  #
  # Why it was worth flipping rather than waiting for the drain: the count grew
  # 5 -> 6 while it was advisory (wlambda_normalisation_census). Advisory
  # REPORTS a gap; it does not HOLD one. Verified before flipping — green at
  # exit 0, exit 1 naming a planted dirty witness, green again once removed.
  #
  # WIDENED to all of docs/audits on 2026-08-21, superseding the
  # docs/audits/scripts root. The scripts subtree was the smaller half by an
  # order of magnitude: 6 files / 26 fields against 32 files / 1,275 fields for
  # the tree containing it. Gating the subtree alone left the bulk of the
  # audits tree in the same ungated state the flip was meant to end.
  #
  # The 26 fields the old baseline tolerated are now 0 — all six producers were
  # fixed at source (max_loss_digits, c_ratios, Z_at_q0, sum_classical), so the
  # wider baseline records those files at nothing and the subtree's floor is
  # preserved exactly: new dirt there is still NEW, still blocking. The
  # subtree baseline is deleted rather than kept beside this one, because two
  # baselines over nested roots is two things to keep true.
  #
  # The 32 files / 1,275 fields now recorded are a TOLERATED backlog belonging
  # to the arcs that own those probes, not to this one. The ratchet holds the
  # line; it does not drain it. 32 of those fields are LP-dual carve-outs in a
  # single witness and are excused by name, not by baseline.
  # ADVISORY, baseline 28 — the leak BETWEEN the two layers above. The
  # padding ratchet works on values and is blind once a float64 is multiplied
  # by anything exact (measured: fmt(mpf(f64)) caught, fmt(exact*mpf(f64)) not);
  # the mpf(<float>) gate works on construction sites and is blind because this
  # defect involves no mpf() call at all. Motivating case: pre-fix
  # h6_deuteron_free_word_chi_lambda_probe.py published a 50-digit q0 beside a
  # payload good to ~1e-15, with both gates green throughout. Advisory rather
  # than blocking because the inference is high-recall (a stale `-> float`
  # annotation already produced one measured false positive, since fixed);
  # flip to blocking once the 28 rows carry agent verdicts. Bean qou-gqt5.
  "mixed mpf/f64 -> serializer|computations/mpf_mixed_arithmetic_audit.py|--strict|yes|yes"
  "audits-tree raw-float64|computations/witness_raw_float64_audit.py|--scan-root docs/audits --strict|no|yes"
  # ADVISORY, and it starts red on purpose — same terms as the audits-tree
  # entry above. `witness_provenance_audit.py` was written, works (27/27
  # self-test), ships --strict/--list, and was in NO array, so nothing ran it.
  # That is the second instance of the qou-j6gb pattern this file already
  # warns about at the top; wiring it here is the half that makes it a gate.
  #
  # It asks the question no other gate asks: does a witness's `scriptFile`
  # actually WRITE that witness? `scriptFile` is treated everywhere as "the
  # producer" — run_pipeline regenerates through it — and nothing checked it.
  # Confirms the class by finding the bug #5170 fixed BY HAND: a producer
  # whose output path had drifted from the witness naming it.
  #
  # Red on arrival at 7: 2 NOT_A_PRODUCER (psl27-irrep-verification,
  # sigma-all-evaluator — both named scripts contain "witness" zero times, so
  # they provably cannot write them) and 5 SCRIPT_MISSING, of which at least 2
  # are false positives naming legitimate non-Python producers (a .lean and
  # joint_tower_sdp.rs). It ran advisory rather than blocking because a gate
  # that is red on arrival gets skipped, which is how a checker goes quiet.
  #
  # BLOCKING as of 2026-08-16 — the stated flip condition is met, all seven
  # drained (bean qou-w9s3, then qou-zdz5):
  #   - .lean/.rs false-positive class handled: a non-Python producer found in
  #     the tree now scores UNCONFIRMED, not SCRIPT_MISSING. 5 -> 3.
  #   - the 3 real SCRIPT_MISSING reconstructed. Two producers existed on
  #     branches that never merged (one an exact scriptHash match); the third
  #     was never committed at all and rebuilt from its recorded values, which
  #     it reproduces to every digit. 3 -> 0.
  #   - both NOT_A_PRODUCER wired to emit the witness naming them
  #     (psl27 in #5179, sigma-all here). 2 -> 0.
  # --strict exits 0 and the self-test is 27/27. UNCONFIRMED (31) is not a
  # failure class: it means the audit cannot statically prove the write, which
  # is the honest verdict for a non-Python producer or a dynamic output path.
  "witness scriptFile provenance|computations/witness_provenance_audit.py|--strict|yes|yes"
  "no-free-parameter cert|computations/no_free_parameter_certificate.py|--strict|yes|no"
)

if [ "${1:-}" = "--list" ]; then
  printf '%-26s %-52s %s\n' "GATE" "SCRIPT" "BLOCKING"
  for g in "${GATES[@]}"; do
    IFS='|' read -r name script _args _st blocking <<<"$g"
    printf '%-26s %-52s %s\n' "$name" "$script" "$blocking"
  done
  exit 0
fi

if [ "${1:-}" = "--changed" ]; then
  # Cheap short-circuit. The ratchets are corpus-wide, not per-file, so there is
  # nothing to scope down — but if this change cannot have moved any of them,
  # skip the ~40s entirely.
  relevant=$( { git diff --name-only HEAD 2>/dev/null
                git diff --cached --name-only 2>/dev/null
                git ls-files --others --exclude-standard 2>/dev/null; } \
              | sort -u | grep -E '(\.witness\.json$|^computations/.*\.py$)' || true)
  if [ -z "$relevant" ]; then
    echo "precision-gates: no witness or computations/ script touched — skipped."
    exit 0
  fi
  echo "precision-gates: $(printf '%s\n' "$relevant" | wc -l) relevant file(s) changed — running."
  echo
fi

# ---------------------------------------------------------------------------
# Preflight: an unimportable dependency is NOT a red gate.
#
# Every gate runs `python3 <script>`, and a missing module makes that exit
# non-zero. The loop below cannot tell that apart from a detector that genuinely
# fired, so it lands in the same RED list.
#
# Measured, 2026-08-09, on a tree with `mpmath` absent:
#
#   RED: q0-anchor flip  mpf(<float>) source (self-test)
#        float64-padding ratchet (self-test)  raw-float64 ratchet
#        q0-value drift ratchet
#
# Five blocking failures. Four of them vanished the moment `mpmath` was
# installed — q0-anchor flip went green with 573 Q0_OK — and only raw-float64
# was real (and inherited from main). An agent following prepare-merge §4b would
# have treated four phantoms as merge blockers, or "fixed" them at a producer
# that was never wrong.
#
# The self-test mechanism exists on exactly this principle: "a detector that
# cannot be shown to fire is a no-op." The same applies in the other direction —
# a gate that reports failure without examining anything is not a gate either.
# So: check the imports up front, and exit 2 with a different message, so
# "cannot evaluate" can never be read as "found a defect".
missing=$(python3 - <<'PREFLIGHT_PY'
import importlib.util
# Third-party modules the gate scripts import. Extend when a gate gains a dep.
need = ["mpmath"]
print(" ".join(m for m in need if importlib.util.find_spec(m) is None))
PREFLIGHT_PY
)
if [ -n "$missing" ]; then
  echo "PREFLIGHT FAILED — the precision gates could not be evaluated."
  echo "  missing Python module(s): $missing"
  echo
  echo "  This is NOT a gate failure. Nothing was examined, so nothing is known"
  echo "  about the tree's precision hygiene. Do not report it as red, and do"
  echo "  not go looking for a producer to fix."
  echo
  echo "    pip install $missing"
  exit 2
fi

# Witnesses that are dirty BEFORE the run are the agent's own work; witnesses
# that the run itself dirties are audits whose committed output is stale. The
# two are different findings and are reported separately.
before=$(git status --porcelain 2>/dev/null | sort)

blocking_failed=()
advisory_failed=()

for g in "${GATES[@]}"; do
  IFS='|' read -r name script args selftest blocking <<<"$g"
  printf '\n\033[1m▸ %s\033[0m  (%s)\n' "$name" "$script"
  if [ ! -f "$script" ]; then
    echo "  MISSING: $script — the gate list is out of date with the tree."
    blocking_failed+=("$name (script missing)")
    continue
  fi
  if [ "$selftest" = "yes" ]; then
    if ! python3 "$script" --self-test >/dev/null 2>&1; then
      echo "  SELF-TEST FAILED — a detector that cannot be shown to fire is a no-op."
      blocking_failed+=("$name (self-test)")
      continue
    fi
  fi
  out=$(python3 "$script" $args 2>&1); rc=$?
  printf '%s\n' "$out" | sed 's/^/  /' | head -18
  if [ $rc -ne 0 ]; then
    if [ "$blocking" = "yes" ]; then
      blocking_failed+=("$name")
    else
      advisory_failed+=("$name")
    fi
  fi
done

after=$(git status --porcelain 2>/dev/null | sort)
# Restrict to what the audits can actually write. A bare before/after diff
# misattributes any concurrent edit to the run — it flagged a bean file that was
# being appended to in another shell on its first outing.
newly_dirty=$(comm -13 <(printf '%s\n' "$before") <(printf '%s\n' "$after") \
              | grep -E 'computations/.*\.witness\.json$' || true)

echo
echo "======================================================================"
if [ -n "$newly_dirty" ]; then
  echo "STALE COMMITTED AUDIT WITNESSES — the run regenerated these:"
  printf '%s\n' "$newly_dirty" | sed 's/^/  /'
  echo "  Each is an audit's own output whose committed copy no longer matches"
  echo "  the tree. If only computedAt/commitSha/durationMs/scriptHash moved it"
  echo "  is drift — revert it. If a COUNT moved, the committed witness was"
  echo "  stale: commit the regenerated one and say which count changed."
  echo
fi
if [ ${#advisory_failed[@]} -gt 0 ]; then
  echo "ADVISORY (not gating): ${advisory_failed[*]}"
fi
if [ ${#blocking_failed[@]} -gt 0 ]; then
  echo "RED: ${blocking_failed[*]}"
  echo
  echo "Fix AT THE PRODUCER. Do not add a file to a baseline, do not"
  echo "--rebaseline, and do not hand-edit a number, to make this green."
  exit 1
fi
echo "All blocking precision gates green."
