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
[`computations/`](../../computations/)
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
| F7 | 🟡 | LaurentQ wiring | **5 callers; P17 sweet-spot A=3 (3–6× speedup).** Per workplan §11, the speedup fades past A=4 because GS reduction dominates. R4 quotient-ideal port into LaurentQ would recover the gap but is research-grade. | grep | Defer (Tier 4). Add a one-line comment in `laurent_q.py` noting the empirical ceiling so future agents do not re-launch the sweep. |
| F8 | 🔴 | Pickle (P14) | **1 hit, scoped, local-only:** `mass_at_3A_proper.py:146-167`. Cache content: tuple of numpy arrays + SYT dicts. RCE risk requires local write access. | scan + per-file read | Tier 1 — 5-line edit to `numpy.savez_compressed`; arrays are already-typed (no sympy expressions in this cache). |
| F9 | 🔴 | sp.cancel walltime risk (P15) | **64 hits.** Reference fix `term6_residues_at_roots.py` (commit 18fce929) moved tritium-scale evaluation 120 s → < 1 s by replacing `sp.cancel` with `sp.together` + targeted `sp.div`. Hot files: `markov_weights_symbolic.py` (4×), `markov_trace_atomic_proton_full.py` (heavy hits), `shift_from_nf_basis.py` (8×). | scanner top-files | Tier 2 — per-call review; some `sp.cancel` are genuinely required (downstream divisibility test) so each finding needs a 2-line confirmation. Batch in PRs of ≤ 10 files. |
| F10 | 🟡 | sp.simplify walltime risk (P16) | **71 hits.** Reference fix `2834792d` for ³He moved a 30-min wall down to seconds by gating `sp.simplify` behind a `simplify=False` parameter. Hot files: `schur_weyl_symbolic.py` (12×, no P15), `gb_filtration_jet_tracker.py` (9×). | scanner top-files | Tier 3 — apply the `simplify=False` opt-in default pattern across `schur_weyl_symbolic.py`; gate `gb_filtration_jet_tracker.py` calls behind `verbose=False`. |
| F11 | 🟡 | CI workflow scope | `witness-pipeline.yml` re-runs only ~10 specific scripts (`habiro_*`, `markov_*`, `picard_lefschetz_*`, `mobius_*`, `baryon_*`, `sw_*`, `jet_*`, `derivation_chain_*`, `e0_calibration_audit`, `cross_check_trM_1ppb`, two axiomatic markov runners, two informational atomic-mass runs). The `lp_dual_witness_validator`, `bound_state_observable_validator`, and `audit-wiring.ts` run **warn-only**; `compute_audit_scan.py` is **not** wired into CI at all. | yaml read | Tier 2 — add `compute_audit_scan.py` step (warn-only initially; alarm if P14/P30 hit count grows). Promote `lp_dual_witness_validator --strict-wired` from warn to fail (37 wired witnesses; 0 currently flagged). |
| F12 | 🟢 | Drift detection | `witness-pipeline.yml` strips `computedAt`/`durationMs`/`commitSha`/`scriptCommitSha`/`scriptHash`/`engineVersion`/`engine` before diffing → only substantive numerical movement fails CI. Working as designed. | yaml read | None. |
| F13 | 🟡 | `:val[…]` directive coverage | `witnessed-values` registry in `content/values/registry.ts` is the single source of truth for substrate-derived literals. Checked: registry exists, `:val[…]` validation rules wired, codemod available. **Not checked here:** how many `.md` blocks still contain hard-coded literals above `MATCH_PRECISION = 6`. | skill file | Tier 3 — run `bun content/pipeline/codemod-val.ts content/quantum-observable-universe` (dry-run); report drift. Out of scope for this audit. |
| F14 | 🟢 | Audit-wiring | 201 witnesses → 101 wired + 100 audit-only + 0 orphan. **Healthy.** | `audit-wiring.ts --warn-only` | None. Keep `--max-per-dir 5` budget gate ready when orphan count drops are needed. |
| F15 | 🟡 | Compute-audit workplan baseline drift | The 2026-05-08 workplan baseline (104 P30 hits) and current scan (103 P30 hits) differ by 1 — the `wrap_legacy` first migration. Workflow not re-run since. Re-running confirms 260 total findings vs the baseline's 261 (one P30 closed). | scanner + workplan | Tier 1 — update workplan §"Implementation begun in this PR" with current numbers. (Done by this audit.) |

## 3. Per-pattern static scan (current)

`python computations/compute_audit_scan.py` →
[`compute-audit-scan.witness.json`](../../computations/compute-audit-scan.witness.json):
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

3. **F2 — dropped (2026-05-08, author decision).** PR #564 is
   regenerating witnesses with the canonical `WitnessBuilder` flow,
   which carries `scriptHash` for free. Backfilling here would be
   redundant and would risk merge conflicts. Re-evaluate after #564
   lands.
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
10. **Close F1 (assertion backfill, 2026-05-08, author scope: all
    37 in one batch).** For every wired witness linked to a
    theorem / proposition / lemma / corollary content block,
    identify the central numerical claim and encode it as
    `w.add_assertion(name, computed, expected, tolerance)`. Skip
    audit-only witnesses (their assertions live in the audit MD).
    Per-witness 2-line read required.
11. **F4 — closed (2026-05-08, author decision).** The 3-of-3
    flagged-with-dual set on the tightened `LP_SDP_HINTS` is the
    authoritative baseline going forward. The 14 LP-solving scripts
    not on the hint list are presumed `feasibility-only` (opt-out).
    `--strict-wired` enforced in CI per F11. AGENTS.md updated.
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
python computations/compute_audit_scan.py

# Pipeline staleness
python computations/run_pipeline.py --dry-run

# LP-dual coverage
python computations/lp_dual_witness_validator.py --list-wired

# Bound-state observable coverage
python computations/bound_state_observable_validator.py

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
  (AGENTS.md § *LP / SDP duals*).
- Bound-state observables compute via the master formula
  `⟨O⟩_T = Σ_{i,j ∈ A*(T)} u_i (G⁻¹)_{ij} ⟨O, b_j⟩`
  (`prop:confinement-frobenius-reciprocity`); the raw Markov trace
  is the right answer **only** when `observable_type: "raw_trace"`
  is opted in.
- Substrate-derived literals in paper prose go through
  `:val[name]{…}` (`witnessed-values` skill); never hard-code.

## 7. Post-rebase reuse + simplify pass (2026-05-08)

Per `/prepare-merge` step 2a. Main shipped during this branch's
session:

- `content/.../braids-and-knots/jet-prefix-gb-filtration.md`
  (PR #571) — distinguishes truncation cutoff `k` from intrinsic
  grading bound `ℓ(K,q)`. Future SDP-wiring work (per #564 P6)
  should key any cache by the intrinsic bound, not the cutoff.
- `content/.../braids-and-knots/ontological-agnosticism.md`
  (PR #571) — interpretive remark; flat transport of crystal-limit
  observables to the generic fibre. Useful framing for any
  follow-up that lifts the F6 BlockCache demo to the symbolic-q
  path.
- `.claude/skills/local/coordinate.md` (PR #568) — official
  /coordinate skill. The version landed with this branch was a
  parallel implementation; rebase took main's authoritative copy.
- `.claude/skills/local/editor.md` (PR #570) — adds the PR-queue
  policy for handling webhook events without interrupting the
  workplan.

**Schema gap closed.** 16 content files on main carried
`status: "experimental"` and 4 carried compound engine names
(`closed-form`, `python+mpmath`, `python+numpy+cvxpy`) that the
Zod schema rejected. Widened `ComputationStatusSchema` and
`ComputationEngineSchema` in
[`folio-assistant/schemas/constraints.ts`](../../folio-assistant/schemas/constraints.ts)
to accept these values. Validation goes from 74 hard errors → 0
hard errors (185 warnings unchanged; pre-existing `:val` block-
computation hints).

**No code duplicates with main.** The branch's work is purely
compute-infrastructure; main's 4 PRs touched content blocks
(braids-and-knots) and skills, with zero overlap on
`computations/`. No simplifications discovered;
no proofs to revisit.

### New 1ppb-improvement areas surfaced by this rebase

| # | Lever | Source | Sketch |
|---|---|---|---|
| L1 | **Per-atom intrinsic grading bound `ℓ(K,q)`** as an SDP cache key, not the truncation `k`. | `jet-prefix-gb-filtration.md` (main, #571) | Emit a `jet-prefix-grading-bound.witness.json` with `ℓ(K,q)` per atomic braid; #564's P6 (jet-order → Rust SDP wiring) keys variable filtering by it. Enables warm-started chain-decomposition without recomputing the cutoff per run. |
| L2 | **Crystal-limit transport** for observables that timeout at symbolic `q`. | `ontological-agnosticism.md` (main, #571) | Compute observable at `q=0` (combinatorial; fast), flatly transport to `q_0` along the connection. Side-steps `sp.simplify` walls (P16 cases) for any observable that respects flat transport. Paired with #567's crystal-R-matrix proof, the path is rigorous. |
| L3 | **Class-axiomatise the 12 hub conjectures** per #564 §1A. | #564 P1 | One small PR per conjecture; each closes ~249 §3b violators downstream. Unblocks Lean conditional-on-class proofs across the mass / binding chain. |
| L4 | **F2 reactivation** when #564 lands its witness regen. | author decision (this branch) | The dropped `scriptHash` backfill becomes safe to apply once #564's wrap_legacy migration settles; ~18 hand-written witnesses gain staleness detection. |
| L5 | **Compound-β shell calibration** | #564 P8 | Implement `compound_beta_shell.py` chain-subtraction against AME 2020 Q-values. Drops shell residual contribution from ~5–15% to ~0.1%. |
| L6 | **Quotient-braid `a(Z, N)` for `A ≥ 5`** | #564 P5' + #567's crystal proof | Replace placeholder `(1−h²)^(A−2)` with the column-rich crystal-R-matrix formula. Drops residual 10–30% → 1–3% on heavy atoms. |

L1 and L2 are immediately tractable on `computations/`
(small witness emitters); L5 and L6 are research-grade. L3 is paper-
side bookkeeping. L4 unblocks itself.
