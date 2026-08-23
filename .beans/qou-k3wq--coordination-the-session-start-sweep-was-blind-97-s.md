---
# qou-k3wq
title: 'Coordination: the session-start sweep was blind to sibling branches — 97 active in 24h, 31 in this campaign''s scope, and four working my exact defect shape'
status: todo
type: task
created_at: 2026-08-23T14:50:00Z
updated_at: 2026-08-23T14:50:00Z
---

Consequence of `qou-i5jy` finding #6. `scripts/session-start-coord-sweep.sh` read
`refs/remotes/origin/claude/*` while fetching only `main`, so in these ephemeral
containers it reported **no sibling section at all**. Fixed there; this bean
records what the fix immediately revealed, so the cost of the blindness is
legible and nobody re-derives it.

**97 sibling branches updated in the last 24 h.** Triaged all 97, none dropped:
**31 IN-SCOPE**, 28 ADJACENT, 38 UNRELATED (96 distinct commits — two refs share
a tip).

## 1. My audit-coverage commits do NOT collide — checked file by file

Zero siblings touch any of `scripts/guard_check.py`,
`scripts/session-start-coord-sweep.sh`, `computations/q0_value_drift_audit.py`,
`computations/extraction_wall_gate.py`,
`computations/audits/producer_importability_audit.py`,
`computations/witness_failed_assertion_audit.py`, or
`computations/classify_production_reach.py`. (21 siblings touch
`computations/audits/` broadly, never these files.)

## 2. FOUR siblings are working this exact defect shape, independently

This matters more than the non-collision. `qou-i5jy`'s thesis is being
implemented in parallel on surfaces I did not touch:

- **`changed-files-helper-2026-08-22`** (`qou-pt9b`) —
  *"lib(qou-pt9b): **a skip is not a pass** — say what was compared, and how
  much"*, rewiring four **shell** gates (`precision-gates.sh`,
  `staleness-gates.sh`, `check-sidecars.sh`, `lean-verify-changed.sh`) onto one
  changed-files helper. Verbatim this bean's thesis, on the shell side.
- **`codata-gate-cost-2026-08-22`** (`qou-s2gm`, `qou-p8lx`) — *"precision-gates.sh
  changed silently passes"*, *"main is red on staleness-gates.sh, 3 gates
  invisible"*, and *"docs(qou-p8lx): **main is RED on this script — say so, before
  someone reads it as theirs**"*. That last move is the one I independently made
  for the failed-assertion gate in `qou-i5jy` #3, the same day.
- **`ratchet-selftest-tautology-fix-2026-08-23`** (`qou-1brv`) — *"the ratchet
  self-test could not fail — one shared predicate"*.
- **`wrap-legacy-computation-clobber-2026-08-21`** — *"the register could report
  **AT RISK 0 without examining anything**"*.

**Read these before extending `qou-i5jy` further.** Four independent
rediscoveries of one shape in three days is itself the finding: it is systemic,
not a handful of sloppy scripts. It also means the marginal value of a fifth
sweep is low and the value of a shared helper is high — `qou-pt9b` has already
built one for the shell gates.

## 3. Beans of mine that siblings have already advanced or overtaken

- **`qou-khac` — likely OVERTAKEN.** `q0-anchor-comparison-vocabulary-2026-08-21`
  carries *"probe: **three different values are all called \"the muon q0\"** — and
  it blocks the stamp above"*, plus a `muon_pin_three_values_probe.py`. khac's ask
  was two values; they measured three and built the probe. A third branch
  (`ratchet-selftest-nonwriting`) states it again: *"the corpus hardcodes SEVERAL
  mutually inconsistent muon-q0 pins, not one"*. **Do not re-derive khac — verify
  against theirs and close or narrow it.**
- **`qou-cds1` — four siblings editing the bean file** itself
  (`cds1-ladder-d-rederivation`, `q0-witness-staleness-drain`,
  `qbeta-ladder-convention-d`, `nok3-resolve`), three more citing it. Correctly
  left unclaimed here; the deferral in `qou-a613` was the right call.
- **`qou-pvem` / `qou-cdh3` — counts disagree with a sibling census.**
  `hecke-core-mpf-scoping-2026-08-23` (`qou-z11r`) classified **58** convention-C
  witnesses; pvem measured 25 and cdh3 14. pvem was already scrapped on
  re-measurement. **Reconcile against the 58 before acting on either.**

## 4. Campaign-material change landing underneath this branch

**`muon-anchor-codata-2022-2026-08-22`** — *"muon anchor → CODATA 2022 (owner
ruling): derive it, stop the self-certification"*. One commit, but it rewrites
`computations/substrate/q_parameter.py` and regenerates the anchor witness (442
lines). Every q₀-pin conclusion on this branch is stated against the *current*
muon pin; if that ruling lands, the `ideal_muon` layer moves. `qou-fd0e`'s open
question (148 witnesses in a class that cannot be STALE) should be answered
**after** it lands, not before.

## 5. Semantic collisions to expect on merge

- `computations/q0-value-drift-audit.witness.json` regenerated on **14** siblings;
  `computations/audits/q0-anchor-consistency-audit.witness.json` on **16**. I edit
  both producers (`q0_value_drift_audit.py --layer-check`,
  `q0_anchor_consistency_audit.py --payload-check`), so any semantic change
  invalidates those regenerations. Merge order matters; the witnesses must be
  regenerated after, not merged.
- `scripts/convention-c-witness-audit.py` — `mu-lambda-heat-kernel-2026-08-12` /
  `sorry-reapply-2026-08-22` (same tip `2b7f5fd8d9`) adds *"a third convention-C
  test — sqrt(q) in a weight expression"* (+134 lines) and edits `.beans/qou-7hfy`.
  Buried mid-history under a tip subject of *"Remove python scripts"* — it will
  not be found by reading branch tips.
- `q0-direct-reader-fixes-2026-08-22` runs the same campaign under another name:
  *"fix(324i): the convention-C detector could not see 'mpf(1)' — actionable
  1 → 31"* and *"fix(qou-dkm2): load_q_50dps defaults to proton, with an explicit
  anchor= for the ideal layer"*. Highest topical duplication risk.

## Method, so this can be re-audited

Enumerated with `git for-each-ref … refs/remotes/origin/claude` filtered to
`committerdate ≥ now − 86400`, **after** widening the clone's fetch refspec —
which is the whole point: the default `+refs/heads/main:refs/remotes/origin/main`
makes this list empty and the emptiness invisible. Buckets assigned on commit
subjects and changed paths only. 97 = 31 + 28 + 38 + **0 unevaluated**.
