# Compute Infrastructure Audit — 2026-05-08

**Branch:** `claude/compute-infrastructure-audit-1vzRo`
**Skills used:**
[`local/compute-audit`](../../.claude/skills/local/compute-audit.md),
[`local/lean-witness-audit`](../../.claude/skills/local/lean-witness-audit.md),
[`local/witnessed-values`](../../.claude/skills/local/witnessed-values.md),
[`local/proof-status-tracking`](../../.claude/skills/local/proof-status-tracking.md)
**Companion:** [`2026-05-08-compute-audit-workplan.md`](2026-05-08-compute-audit-workplan.md)
(per-pattern P1–P30 workplan — this document is the orthogonal
infrastructure-level view).

This audit covers every compute artifact under
[`folio-assistant/computations/`](../../folio-assistant/computations/)
plus the supporting CI gates, content-block wiring, and witness
schema. The static P-pattern scanner findings are tabulated alongside
new infrastructure-level findings.

## 1. Inventory snapshot

| Artifact | Count | Notes |
|---|---:|---|
| Python scripts (`*.py`) | 245 | Production + audit + infra |
| Witnesses (`*.witness.json`) | 201 | Plus 4 `*.derivation.json` |
| Wired (referenced by content block `computation:` field) | 101 | from `audit-wiring.ts` |
| Audit-only (declares `auditOnly: docs/audits/*.md`) | 100 | |
| Orphan | 0 | ✅ wiring is healthy |
| Largest infra modules | `hecke_core.py` (3173 LOC), `hecke_symbolic.py` (1206), `picard_lefschetz_thimble.py` (1050), `hecke_division.py` (951) | |
| `WitnessBuilder` adopters | 100 | 82 scripts still hand-`json.dump` |
| `WitnessBuilder.wrap_legacy` adopters | 1 (`alpha_em_pslq_uniqueness.py`) | Helper landed `31cbfe3c`; sweep paused on per-file decisions |
| `LaurentQ` callers | 5 (`hecke_laurent_fast`, `markov_peel`, `term6_residues_at_roots`, `habiro_coefficients_extended`, `laurent_q` itself) | P17 sweet spot is A=3 |
| `BlockCache` callers | 1 production (`ocneanu_weights`) + 1 defn (`syt_prefix_cache`) | 21 numerical-q candidates not yet wired |
| `pickle` users (P14) | 1 (`mass_at_3A_proper.py`) | Decision pending: `numpy.savez` vs JSON-of-`str(sympy.Expr)` |
| `lp_dual_solver` direct callers | 4 | Plus `linprog`, `cvxpy` callers — 17 total LP/SDP scripts |

## 2. Findings table — orthogonal axes

Each row is an infrastructure-level finding (different from the per-pattern
P1–P30 cells in the companion workplan). Severity legend: 🔴 blocking, 🟡 warn, 🟢 informational.

| # | Severity | Axis | Finding | Evidence | Action |
|---|---|---|---|---|---|
| F1 | 🟡 | Witness completeness | **145/201 witnesses have empty `assertions: []`.** They store outputs but no structured pass/fail checks. CI's drift detector catches numerical movement, but no per-witness `allPassed` gate exists for these. | `python3 -c …` enumeration | Tier 3 — backfill key assertions on the 37-block wired set first. |
| F2 | 🟡 | Witness schema | **106/201 witnesses lack `scriptHash`.** 88 are legitimately `auditOnly` hand-curated reference values; ~18 are computational outputs that bypassed `WitnessBuilder` (P30). | `for f in *.witness.json: scriptHash check` | Tier 2 — apply `wrap_legacy` to the 18 computational outputs. |
| F3 | 🟡 | Pipeline staleness | **`run_pipeline.py --dry-run` reports 144 stale scripts** (78 missing witness + 20 changed-script + 46 dependency-stale). Indicates the witness regeneration pipeline hasn't been driven through after recent infra-module touches. | `run_pipeline.py --dry-run` tail | Tier 2 — single overnight `run_pipeline.py --jobs 4` run after baselining a clean main; commit only stable diffs. |
| F4 | 🟢 | LP/SDP dual coverage | **17 scripts call an LP/SDP solver (`scipy.linprog`, `cvxpy`, or `lp_dual_solver`); only 3 are `LP_SDP_HINTS`-flagged**, all 3 of which include the required dual fields (`y0_star`, `y_star`, `active_set`, `primal_obj`, `dual_obj`, `duality_gap`). 14 LP-solving scripts emit witnesses whose name/description does **not** match the hint patterns. They may be solving feasibility / certificate-only problems (legitimate), or they may be primal-only operator-selection solves (regression risk). | `lp_dual_witness_validator.py --list-wired`; grep | Tier 3 — review the 14 unflagged LP scripts; tag each as `feasibility-only` (opt-out) or migrate to `lp_dual_solver`. |
| F5 | 🟡 | Bound-state observables | **`bound_state_observable_validator.py` reports 2/3 flagged witnesses missing G⁻¹ / LP active-set fields**: `gt-matrix-pslq-probe.witness.json` (axial coupling), `t35-weak-vertex.witness.json` (form factor). Tickets AXIAL-G_A-002 + TRIAGE-001..003 are still open from `2026-05-06-frobenius-pairing-compute-audit.md`. | validator output | Tier 2 — close two tickets per `prop:confinement-frobenius-reciprocity` master formula. |
| F6 | 🟡 | BlockCache wiring | **Only `ocneanu_weights.py` uses `BlockCache` in production.** Scanner identifies 21 numerical-q Hoefsmit callers that could benefit. Per workplan §8 table: 12 confirmed-numerical, 5 mixed/review, 4 symbolic (leave as-is). Expected speedup: 5–20× per call on n ≥ 8. | `compute_audit_scan.py` P21 hits | Tier 3 — wire the 12 numerical callers; add `mpmath` BlockCache variant for the 2 mpfr callers (`probe_atom_shell_self_duality_mpfr`, `tr_m_wenzl_bridge_mpfr`). |
| F7 | 🟡 | LaurentQ wiring | **5 callers; P17 sweet-spot A=3 (3–6× speedup).** Per workplan §11, the speedup fades past A=4 because GS reduction dominates. R4 quotient-ideal port into LaurentQ would recover the gap but is research-grade. | grep | Defer (Tier 6). Add a one-line comment in `laurent_q.py` noting the empirical ceiling so future agents do not re-launch the sweep. |
| F8 | 🟡 | Pickle (P14) | **1 hit, scoped, local-only:** `mass_at_3A_proper.py:146-167`. Cache content: tuple of numpy arrays + SYT dicts. RCE risk requires local write access. | scan + per-file read | Tier 1 — 5-line edit to `numpy.savez`; arrays are already-typed (no sympy expressions in this cache). |
| F9 | 🔴 | sp.cancel walltime risk (P15) | **64 hits.** Reference fix `term6_residues_at_roots.py` (commit 18fce929) moved tritium-scale evaluation 120 s → < 1 s by replacing `sp.cancel` with `sp.together` + targeted `sp.div`. Hot files: `markov_weights_symbolic.py` (4×), `markov_trace_atomic_proton_full.py` (heavy hits), `shift_from_nf_basis.py` (8×). | scanner top-files | Tier 2 — per-call review; some `sp.cancel` are genuinely required (downstream divisibility test) so each finding needs a 2-line confirmation. Batch in PRs of ≤ 10 files. |
| F10 | 🟡 | sp.simplify walltime risk (P16) | **71 hits.** Reference fix `2834792d` for ³He moved a 30-min wall down to seconds by gating `sp.simplify` behind a `simplify=False` parameter. Hot files: `schur_weyl_symbolic.py` (12×, no P15), `gb_filtration_jet_tracker.py` (9×). | scanner top-files | Tier 3 — apply the `simplify=False` opt-in default pattern across `schur_weyl_symbolic.py`; gate `gb_filtration_jet_tracker.py` calls behind `verbose=False`. |
| F11 | 🟡 | CI workflow scope | `witness-pipeline.yml` re-runs only ~10 specific scripts (`habiro_*`, `markov_*`, `picard_lefschetz_*`, `mobius_*`, `baryon_*`, `sw_*`, `jet_*`, `derivation_chain_*`, `e0_calibration_audit`, `cross_check_trM_1ppb`, two axiomatic markov runners, two informational atomic-mass runs). The `lp_dual_witness_validator`, `bound_state_observable_validator`, and `audit-wiring.ts` run **warn-only**; `compute_audit_scan.py` is **not** wired into CI at all. | yaml read | Tier 2 — add `compute_audit_scan.py` step (warn-only initially; alarm if P14/P30 hit count grows). Promote `lp_dual_witness_validator --strict-wired` from warn to fail (37 wired witnesses; 0 currently flagged). |
| F12 | 🟢 | Drift detection | `witness-pipeline.yml` strips `computedAt`/`durationMs`/`commitSha`/`scriptCommitSha`/`scriptHash`/`engineVersion`/`engine` before diffing → only substantive numerical movement fails CI. Working as designed. | yaml read | None. |
| F13 | 🟡 | `:val[…]` directive coverage | `witnessed-values` registry in `content/values/registry.ts` is the single source of truth for substrate-derived literals. Checked: registry exists, `:val[…]` validation rules wired, codemod available. **Not checked here:** how many `.md` blocks still contain hard-coded literals above `MATCH_PRECISION = 6`. | skill file | Tier 3 — run `bun content/pipeline/codemod-val.ts content/quantum-observable-universe` (dry-run); report drift. Out of scope for this audit. |
| F14 | 🟢 | Audit-wiring | 201 witnesses → 101 wired + 100 audit-only + 0 orphan. **Healthy.** | `audit-wiring.ts --warn-only` | None. Keep `--max-per-dir 5` budget gate ready when orphan count drops are needed. |
| F15 | 🟡 | Compute-audit workplan baseline drift | The 2026-05-08 workplan baseline (104 P30 hits) and current scan (103 P30 hits) differ by 1 — the `wrap_legacy` first migration. Workflow not re-run since. Re-running confirms 260 total findings vs the baseline's 261 (one P30 closed). | scanner + workplan | Tier 1 — update workplan §"Implementation begun in this PR" with current numbers. (Done by this audit.) |

## 3. Per-pattern static scan (current)

`python folio-assistant/computations/compute_audit_scan.py` →
[`compute-audit-scan.witness.json`](../../folio-assistant/computations/compute-audit-scan.witness.json):
**245 files, 260 findings**.

| Pattern | Hits | Δ since 2026-05-08 baseline | Group |
|---|---:|---:|---|
| P14 (pickle) | 1 | 0 | Correctness/security |
| P15 (`sp.cancel` full-rational) | 64 | 0 | Performance |
| P16 (`sp.simplify` before `evalf`) | 71 | 0 | Performance |
| P21 (Hoefsmit without `BlockCache`) | 21 | 0 | Performance |
| P30 (witness without `WitnessBuilder`) | 103 | −1 | Schema |

The remaining 25 P-patterns (P1–P13, P17–P20, P22–P29) are not
mechanically scannable. P1 (trace-cyclic conjugation) was audited in
`borromean-axial-coupling`; P17–P20 are reviewed per file; P25
(det-pair law) is wired in `det_pair_law.py` but downstream
deployment is opportunistic.

## 4. Workplan to address findings

Items are ordered by **(blast radius / unblock-other-work)**, not by
P-pattern. Each item names the finding it closes. **No item is
attempted in this PR** — this PR only delivers the audit document so
the user can triage.

### Tier 1 — Self-contained, mechanical, no semantic decisions

1. **Close F8 (P14 pickle).** Migrate `mass_at_3A_proper.py:146-167`
   from `pickle.dump` to `numpy.savez_compressed` (cache content is
   numpy arrays + plain dict, so JSON-of-sympy-Expr is overkill).
   5-line edit; numerical-equivalence check at q₀ trivial.
2. **Close F15 (workplan drift).** Already done by this audit
   document.

### Tier 2 — Batched mechanical sweeps with per-file 2-line read

3. **Close F2 (`scriptHash` backfill).** Apply
   `WitnessBuilder.wrap_legacy` to the ~18 computational-output
   witnesses that lack `scriptHash`. Hand-curated `auditOnly`
   witnesses are kept as-is. Batch in PRs of ≤ 10 files; cross-check
   bit-stability of original keys per `wrap_legacy` invariant.
4. **Close F3 (pipeline staleness).** Single supervised
   `run_pipeline.py --jobs 4` run on a clean main; review the
   resulting witness diff with `witness-pipeline.yml` drift filter;
   commit substantive numerical movements separately from pure
   metadata refresh. Block size: estimate 4–8 h walltime (some
   Hoefsmit-heavy scripts at A≥5 are slow).
5. **Close F5 (bound-state observable backfill).** Two tickets:
   `gt-matrix-pslq-probe` and `t35-weak-vertex`. Implement the
   master formula `⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i (G⁻¹)_{ij} ⟨O, b_j⟩`
   per `prop:confinement-frobenius-reciprocity`; or set
   `observable_type: "raw_trace"` if the raw Markov trace is the
   correct answer (escalate to user for the call).
6. **Close F11 (promote validators in CI).** Add
   `compute_audit_scan.py` step to `witness-pipeline.yml`
   (warn-only). Promote `lp_dual_witness_validator --strict-wired`
   from warn to fail (currently 0 wired failures, so it's safe).

### Tier 3 — Targeted speedup opportunities (verify before landing)

7. **Close F9 (P15 sweep).** Replace `sp.cancel` with `sp.together` +
   targeted `sp.div` where the GCD is unused downstream. 64 hits;
   batch in PRs of ≤ 10 files. **Required:** per-file 2-line read
   to confirm the GCD is unused; per-PR benchmark table at q₀ with
   `Δ < 1e-15` cross-check.
8. **Close F10 (P16 sweep).** Apply `simplify=False` opt-in default
   to `schur_weyl_symbolic.py` (12× P16). Gate
   `gb_filtration_jet_tracker.py` `simplify` calls behind
   `verbose=False`. Reference: `2834792d` (³He, 30 min → seconds).
9. **Close F6 (BlockCache wiring).** Wire 12 confirmed-numerical
   Hoefsmit callers per `2026-05-08-compute-audit-workplan.md` §8
   table. Add an `mpmath` BlockCache variant for the 2 mpfr
   callers. Expected: 5–20× per call on n ≥ 8.
10. **Close F1 (assertion backfill).** Pick the 37 witnesses linked
    to provable-kind content blocks (theorem/proposition/lemma/
    corollary); for each, identify the central numerical claim and
    encode it as `w.add_assertion(...)` with a tolerance. Skip
    audit-only witnesses (their assertions live in the audit MD).
11. **Close F4 (LP coverage gap review).** Read the 14 LP-solving
    scripts whose witnesses are not LP_SDP_HINTS-flagged; tag each
    `feasibility-only` (opt-out) or migrate to `lp_dual_solver` and
    extend `LP_SDP_HINTS`.
12. **Close F13 (`:val[…]` codemod sweep).** Run codemod dry-run on
    the QOU paper; report drift; apply with `--write` after user
    review.

### Tier 4 — Defer (research-grade or low-leverage)

13. **F7 (LaurentQ A≥5).** R4 quotient-ideal port is research-grade.
    Defer. Add a one-line comment in `laurent_q.py` documenting the
    empirical A=4 ceiling.

## 5. Re-running this audit

```bash
# Static P-pattern scan
python folio-assistant/computations/compute_audit_scan.py

# Pipeline staleness
python folio-assistant/computations/run_pipeline.py --dry-run

# LP-dual coverage
python folio-assistant/computations/lp_dual_witness_validator.py --list-wired

# Bound-state observable coverage
python folio-assistant/computations/bound_state_observable_validator.py

# Wiring (orphan / audit / wired)
bun run scripts/audit-wiring.ts --warn-only
```

## 6. Conventions reinforced

- Every speedup PR cites a P-pattern (P1–P30), a prior successful
  fix, includes a per-atom benchmark table in the witness JSON +
  commit message, and cross-checks numerical equivalence at q₀
  with `Δ < 1e-15` (or `Δ < 1e-12` for numerical-only paths) (P28).
- Never remove the slow path; keep it as `use_fast=False` opt-out
  for symbolic-output callers (e69d0acf).
- LP/SDP solves emit BOTH primal and dual variables. Route through
  `lp_dual_solver.py`; never re-implement the primal-only solve
  (CLAUDE.md § *LP / SDP duals*).
- Bound-state observables compute via the master formula
  `⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i (G⁻¹)_{ij} ⟨O, b_j⟩`
  (`prop:confinement-frobenius-reciprocity`); the raw Markov trace
  is the right answer **only** when `observable_type: "raw_trace"`
  is opted in.
- Substrate-derived literals in paper prose go through
  `:val[name]{…}` (`witnessed-values` skill); never hard-code.
