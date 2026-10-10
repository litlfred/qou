> **DEPRECATED on 2026-05-24.** Superseded by [`2026-05-18-1ppb-workplan-v7-100x-experimental.md`](../2026-05-18-1ppb-workplan-v7-100x-experimental.md) (the latest in the 1ppb-workplan chain). Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T4 for the deprecation rationale.

# 1 ppb implementation plan — phased, with audit-anchored status

**Date:** 2026-05-12 (integrated 2026-05-15)
**Branch:** `claude/review-1ppb-prs-EC0ay` (originally `copilot/analyze-audit-reports-and-fix-calculations`)
**Author:** Copilot agent (handover doc); integrated + corrected by review agent
**Builds on:** [`2026-05-11-1ppb-gap-narrowing-plan.md`](2026-05-11-1ppb-gap-narrowing-plan.md), [`2026-05-11-model-b-mass-table.md`](2026-05-11-model-b-mass-table.md), [`2026-05-11-three-calibration-discipline-violations.md`](2026-05-11-three-calibration-discipline-violations.md)

> ## ⚠️ 2026-05-15 integration corrections
>
> This document was integrated from PR #644 into the review branch.
> Two parts of the plan **deviate from canonical derivation** and have
> been overridden during integration:
>
> 1. **P1.B "V1 is the natural Hecke choice" is wrong on physics.**
>    V1 sets β\* = β⁻¹ (multiplicative inverse), so τ(β · (β\*)⁻¹) =
>    τ(β · β) = **τ(β²)** — a double-winding quantity, not a chirality
>    measure. V2 is the genuine mirror knot (each crossing's over/under
>    flipped) and IS the physically correct β\* for a Markov-pairing
>    chirality factor `a_K · 𝒞_K`. V1 production-wiring is **not**
>    recommended; the V1 backfill in `term5-aK-audit.witness.json` is
>    retained as an audit artefact only. See
>    [`2026-05-15-three-pr-integration.md`](2026-05-15-three-pr-integration.md)
>    §V1≠mirror for the full argument.
>
> 2. **P1.E ⁴He Model B knot survey is methodologically non-canonical.**
>    Picking ⁴He's canonical hyperbolic knot from a survey of $\{8_{17},
>    10_{123}, 8_{18}, L6a4\}$ does not follow from substrate
>    primitives; ⁴He should be **built compositionally** from simpler
>    isotopes (D⊕D, T⊕p, ³He⊕n) at the Model A 12-strand level, with
>    JSJ decomposition of the closure producing the canonical knot. The
>    survey script `probe_he4_model_b_knot_survey.py` and witness
>    `model-b-he4-knot-survey.witness.json` were **dropped** from this
>    integration. The existing Model B {D, T, ³He} → {$6_2$, $8_{11}$,
>    $L6a4$} assignments require the same re-validation under
>    compositionality.
>
> Status entries below have been left as written by the original
> author; readers should consult the integration audit for the
> canonical reading.

This document is the **execution plan** that the next coding agent
should pick up. The previous-PR planning doc (`2026-05-11-1ppb-gap-
narrowing-plan.md`) gives the *strategy*; this doc gives the
*tasks*, the *current code locations* that need to change, and the
*math sanity-checks* each task must satisfy before merge.

A separate companion document
[`2026-05-12-lean-handover.md`](2026-05-12-lean-handover.md) covers
Phase 4 (Lean closure of conditional results) for the Lean agent.

## 0  Goal & hard floor (recap)

- **Target:** 1 ppb on $\{m_p, m_n, B(D), B(T), B({}^3\mathrm{He}),
  B({}^4\mathrm{He})\}$, then extend to $A \le 40$.
- **Hard floor:** $\sim 780$ ppb from CAL-2 ($q_0$) propagation
  amplified by $|\partial \ln E_0/\partial \ln q_0| = 11.09$.
- **Discipline:** only $\{m_e, q_0, Q_\beta\}$ are calibration anchors.
  Everything else is a prediction.

## 1  Live mass table on this branch (M0 baseline)

Source: `computations/sweeps/paper-six-term-isotope-sweep.witness.json`.
Default mode `tower_mode="li2q"`, proton-calibrated $E_0$ at S9,
Model A T1 from Hoefsmit + Wenzl bridge.

| Atom | Z, N | A | M_pred (MeV) | M_CODATA (MeV) | err (%) |
|------|-----:|--:|-------------:|---------------:|--------:|
| p    | 1, 0 | 1 |  938.272 (calibrated) | 938.272 | $\sim 10^{-5}$ |
| n    | 0, 1 | 1 |  893.397 | 939.565 | **−4.91** |
| D    | 1, 1 | 2 | 1447.850 | 1876.124 | **−22.83** |
| T    | 1, 2 | 3 | 1910.632 | 2809.432 | **−31.99** |
| ³He  | 2, 1 | 3 | 2194.124 | 2809.413 | **−21.90** |
| ⁴He  | 2, 2 | 4 | 2795.002 | 3728.401 | **−25.03** |

MAE on {n, D, T, ³He, ⁴He} ≈ **21.4 %**. Best closure on ³He under
`brane-legacy` mode is +0.58 % but exhibits the −737 MeV mirror
pathology between T and ³He (`prop:t-3he-mirror-asymmetry`).

## 2  Step-by-step error breakdown of the canonical formula

For each isotope, `paper_six_term_mass()` computes:

| Step | Quantity | Canonical source | Production wiring uses canonical? | Error contribution |
|-----:|----------|------------------|-----------------------------------|--------------------|
| S1 | Braid word $\beta$ for $(Z, N)$ | `atom_canonical_crossings(Z, N)` | ✅ Model A; ⚠️ ⁴He Model B unassigned (P1.E) | T1 can shift ×2–10 |
| S2 | Per-generator $\hat V_i^{\mathrm{full}}$ | `hecke_core.atom_per_generator_volumes` | ⚠️ **NOT Markov-invariant** — basis-dependent | Φ_q amplifies near pole by $\sim 10^5\times$ |
| S3 | T1 $= \|\tau_M(T_w)\|$ at 50 dps | Hoefsmit seminormal × Jones–Markov $y_\lambda$ via Wenzl bridge | ✅ canonical | Negligible |
| S4 | T2 $= -\sum_i \mathrm{Li}_2^q(-\|\hat V_i\|)$ | Symmetric q-dilog (corrected Kashaev limit) | ⚠️ basis-dependent via S2 | **Primary n−p direction error** |
| S5 | T3 $= -z^2\sum_{i<j}\mathrm{Li}_2^q(-\|\hat V_i\hat V_j\|)$ | Same as S4 | ⚠️ same | Same |
| S6 | T4 $= m_e\cdot\sum_{\lambda\vdash 3A}1/\dim_q\lambda$ | `thm:frobenius-codim-universal` | ✅ in main path; ⚠️ stragglers see P1.C | $\sim 1$–2 MeV per A |
| S7 | T5 $a_K$ chirality | `prop:chirality-dual-space-derivation`: $\tau(\beta\beta^{*-1})$ | ⚠️ uses **hand-coded sign table** `chirality_signs_for_isotope` | 2.2 % gap to canonical Markov pairing per `_deprecated/term5_aK_audit.py` |
| S8 | T6 cyclotomic residues | `prop:gb-residue-spectral-sum` Habiro form | ✅ canonical | Negligible |
| S9 | Calibration $E_0 = (M_p^{\mathrm{CODATA}} - T_6^p) / \sum_{1..5}^p$ | None — this is a CAL-3-adjacent leak | ⚠️ **proton-mass-fitted**, not substrate-derived | Linear-in-$E_0$ propagates to all atoms |
| S10 | Assembly $M_{\mathrm{pred}} = E_0\cdot\sum_{1..5} + T_6$ | `paper_six_term_mass` | ✅ structurally; numerical accuracy bounded by S2/S4/S5/S7/S9 | — |

## 3  Phase plan (single source of truth — pick up here)

### Phase 1 — Restore canonical wiring (this PR scope)

> **Status as of 2026-05-12 commit `abd1cd5` + this session:**
>
> | Task  | Status      | Notes |
> |-------|-------------|-------|
> | P1.A  | ✅ done     | `e0_mode={substrate, proton-fit}` on `run_sweep_for_mode`; default is `substrate`. |
> | P1.B  | ⚠️ partial  | `term5_aK_audit.py` moved out of `_deprecated/`; `--atoms` CLI added; **proton-only** witness emitted (audit confirms historical 2.2% gap, V1=+1.022, V2=V4=+1.147, V3=+2.424). Backfill of {n, D, T, ³He} blocked by sandbox time budget (>12 min/atom). Production wiring of V1–V4 winner not yet done — owner input needed on which mirror convention is canonical. |
> | P1.C  | ✅ done     | T4 straggler in `mass_formula_6term_mpfr_50dps.py` now delegates to per-3A canonical. |
> | P1.D  | ✅ done     | `tower_mode="per-partition-k"` wired; covers {D, T, ³He}, raises on {p, n, ⁴He}. |
> | P1.E  | ❌ reverted | Both candidate Model B knots for ⁴He moved error in the wrong direction; assignment remains genuinely upstream-blocked. |
> | P2.A  | ✅ done     | `tower_mode="habiro"` wired; covers {p, n, D}, raises on {T, ³He, ⁴He}. |
> | P2.B  | ✅ done     | `tower_mode="combined"` (M1 router) wired: per-atom routing {p, n, D}→habiro, {T, ³He}→per-partition-k, ⁴He+→li2q. Audit-trail fix in this session: combined rows now record `tower_mode="combined"` AND `sub_tower_mode=<actual>`, so the witness is unambiguous to a downstream auditor. |
> | P3    | ⏸ deferred | Closed-form $\Delta_{\mathrm{coupling}}$ — new math; separate PR. |
> | P4    | ⏸ deferred | Lean closure — see `2026-05-12-lean-handover.md`. |
>
> **M1 mass table (substrate $E_0$, no calibration leak):** see
> [`2026-05-12-m1-mass-table.md`](2026-05-12-m1-mass-table.md). Headline:
> the substrate-$E_0$ default makes every mode honestly report a ~98%
> shortfall on absolute mass — confirming the closure gap is structural
> ($\Delta_{\mathrm{coupling}}$ + ⁴He Model B), not plumbing. Combined
> mode under `e0_mode="proton-fit"` is structurally invalid (E_0 can
> only be fit to one sub-mode at a time); use `substrate` E_0 with
> combined.

Each task below is independently mergeable. Numbered tasks are the
implementation units; bullets are the math/code sanity checks the
agent must satisfy.

#### P1.A — Substrate $E_0$ as a non-fitted reporting mode

**Math:** $E_0^{\mathrm{subst}} = m_e / (q_0(q_0 - 1)) \approx 4.186$
MeV per `prop:beta-decay-energy-scale`, derived from CAL-1 + CAL-2
only (no CAL-3 leak). Already implemented in
`derived_masses.e_0_full_mev()`.

**Code:** Add a new boolean parameter `use_substrate_E0=False` (or
a new mode label) to `run_sweep_for_mode()` in
`computations/sweeps/paper_six_term_isotope_sweep.py`. When
true, use `e_0_full_mev()` instead of the proton-fit calibration at
line 564. Emit a parallel set of rows in the witness JSON under
`all_modes[<mode>].rows_substrate_E0`.

**Sanity check:** the proton row will no longer be exact; its err%
becomes the **honest** structural-gap signal at A=1. Anything close
to 0 % means we accidentally calibrated.

#### P1.B — Replace hand-coded chirality table with Markov pairing

**Math:** Per `prop:chirality-dual-space-derivation`, the canonical
chirality factor is
$$
  a_K \cdot \mathcal{C}_K \;=\; \tau(\beta \cdot \beta^{*-1})
$$
where $\beta^{*-1}$ is the Hecke inverse of the mirror braid. The
production sweep uses a hand-coded sign table
`chirality_signs_for_isotope` (line 540 of
`paper_six_term_isotope_sweep.py`):
```python
"D":   [+1],
"T":   [+1, -1],
"3He": [+1, -1],
"4He": [+1, -1, +1, -1],
```
This is heuristic, not derived from $\beta$. The audit
`_deprecated/term5_aK_audit.py` already implements the canonical
Markov pairing across four mirror-convention variants V1–V4.

**Code:** (a) Move `term5_aK_audit.py` out of `_deprecated/` (or
stand up a new production-grade `term5_aK_canonical.py`); (b) emit
`term5-aK-audit.witness.json` with rows for {p, n, D, T, ³He, ⁴He};
(c) in `paper_six_term_mass()`, replace the
`chirality_signs_for_isotope` lookup with a witness-driven $a_K$.

**Status (2026-05-12, this PR):**
- (a) ✅ Done — script lives at `computations/audits/term5_aK_audit.py`.
- (b) ✅ V1 backfill done for {p, n, D, T, ³He}; V2–V4 done for {p, n}
  only. ⁴He still blocked on P1.E (no canonical Model B braid). Witness:
  `computations/audits/term5-aK-audit.witness.json`. Run with
  `--merge-prior` for incremental backfills; use `--variants V1` to skip
  the slow symbolic mirror conventions (V2 alone takes >34 min for
  deuteron in this implementation — unbounded for A=3).
- (c) ⏳ Blocked on owner choice of canonical mirror convention (V1 is
  the natural Hecke choice; V2/V3/V4 are alternative "mirror knot"
  conventions whose physical meaning differs).

**V1 audit results (Δ vs heuristic closed-form):**

| Atom    | closed-form $a_K$ | V1 ($\tau(\beta\beta^{-1})$) | Δ_V1 |
|---------|------------------:|-----------------------------:|------:|
| proton  | 1.000000          | 1.021972                     | 0.0220 |
| neutron | 1.000000          | 1.021972                     | 0.0220 |
| D       | 1.209060          | 1.055840                     | 0.1532 |
| T       | 1.209060          | 1.079039                     | 0.1300 |
| ³He     | 1.209060          | 1.079039                     | 0.1300 |

V1(T) = V1(³He) is an emergent symmetry — flag for narrative
reconciliation (heuristic gives the same closed-form for these two by
construction; canonical Markov pairing also agrees).

**Sanity check:** 2.2 % delta vs heuristic on the proton (per PR #520
audit). At A≥2 the delta jumps to 13–15 % — production wiring of V1
will shift the multi-nucleon mass predictions by O(15 %) on T5.

**Calibration discipline note:** $\tau(\beta\beta^{*-1})$ is a Markov
trace — Markov-invariant by construction, no calibration anchor used.

#### P1.C — Migrate T4 stragglers to per-3A formula

**Math:** Per `thm:frobenius-codim-universal`,
$$
  T_4 \;=\; m_e \cdot \sum_{\lambda \vdash 3A} \frac{1}{\dim_q \lambda}
$$
with the sum over **partitions of 3A** (since the isotope braid
lives in $H_{3A}(q)$). The legacy heuristic
$T_4^{\mathrm{legacy}}(A) = A \cdot m_e \cdot (2 + 1/[2]_q)$ is the
$H_3(q)$-character formula multiplied by A — it overcounts the
trace because it ignores the partitions of 3A that are not just
trivial reductions of partitions of 3.

**Audit results from this branch:**

| File | Status | Action |
|------|:------:|--------|
| `paper_six_term_isotope_sweep.py:285` | ✅ correct (per-3A) | none |
| `unified_low_isotope_predictor.py:99` | ✅ correct (per-3A from witness; line-15 docstring stale) | update docstring only |
| `mass_formula_6term_mpfr_50dps.py:223` | ✅ **migrated 2026-05-12** — `term_4_frobenius_mp(A)` now delegates to `paper_six_term_isotope_sweep.term4_frobenius_codim(A)` with explicit "HARD BREAK" docstring (lines 229-237). Returns single mpf; legacy 2-tuple shape removed by design. | none |
| `d_from_scratch.py:31, 149, 156` | ✅ **migrated 2026-05-12** — uses `term4_frobenius_codim(A)` with explicit "P1.C HARD BREAK" comment (lines 157-162) | none |
| `path_b_habiro_mass_probe.py:145` | ✅ correct (per-3A) | none |
| `compound_binding_via_differences.py:123, 127, 131` | ✅ reads `term4_frobenius_codim` from upstream witness | none |

**Sanity check after migration:** at A = 4, legacy gives
$4 \cdot m_e \cdot (2 + 1/[2]_q) \approx 4 \cdot 0.511 \cdot 2.474 \approx 5.06$
MeV. Per-3A (sum over partitions of 12) gives $\approx 1.05$ MeV. Ratio $\sim 5\times$ inflation
on the brane-tower scale.

#### P1.D — Per-partition $k_\lambda$ cherry-pick from #639

**Math:** PR #639 demonstrates that uniform truncation $k$ across all
Wedderburn blocks of $H_n(q_0)$ is dominated by ONE specific
partition per atom (D: $[2,2,1,1]$, T: $[6,3]$, ³He: $[5,4]$). The
canonical refinement is
$$
  T_2(\beta) \;=\; \sum_\lambda \tilde w_\lambda \cdot
    \sum_{k=0}^{k_\lambda} \frac{|\hat V_\lambda|^k}{(q;q)_k}
$$
with **per-partition** truncation depths $k_\lambda$ chosen by the
substrate confinement bound rather than a uniform $k$.

**Code:** Cherry-pick `per-partition-k-lambda-rule.{md,ts,lean}`
from PR #639 once it merges. Integrate into
`paper_six_term_mass()` as a new `tower_mode="per-partition-k"`.

**Status:** ✅ **LANDED on this branch.** Content blocks
`per-partition-k-lambda-rule.{md,ts}` are present under
`content/quantum-observable-universe/braids-and-knots/`. The
`paper_six_term_isotope_sweep.py:546` branch implements
`tower_mode="per-partition-k"` and is wired into `tower_mode="combined"`
for {T, ³He}. Witness:
`computations/probe-phiq-per-partition-klambda.witness.json`.
(Note: PR #639 itself shipped the Q_β spectral bridge content, not the
per-partition-k machinery; the per-partition-k pieces landed via a
separate path. Cross-reference label retained for historical traceability.)

#### P1.E — ⁴He Model B canonical hyperbolic knot assignment

**Math:** Model B encodes a nucleus as a **single canonical
hyperbolic knot** in the minimum-strand braid group, vs Model A's
$3A$-strand quark braid. For {D, T, ³He} the assignments are
$6_2$, $8_{11}$, $L6a4$ (Borromean) respectively. ⁴He is open.

**Candidates** (from `_T1_ATOM_NAME_B` mapping in
`paper_six_term_isotope_sweep.py:144` and the Model B audit doc):
- $L6a4$ Borromean (already used for ³He — risks degenerate
  assignment)
- $8_{18}$ — 4-bridge symmetric knot, has 4-fold symmetry matching
  ⁴He's $\alpha$-particle structure
- Brunnian 4-component link (matches the "Borromean²" sign
  pattern $[+1,-1,+1,-1]$ already in the chirality table)

**Verification metric:** $\tau_M$ at $q_0$ should match AME within
an order of magnitude. From the M0 table, ⁴He AME binding is
28.30 MeV; current Model A gives a 25 % under-prediction of total
mass, so the canonical Model B knot's $\tau_M$ should be in the
range $[0.05, 0.5]$ at $q_0$ to be plausible.

**Status:** **Survey witness landed (2026-05-12); final knot
selection still needs owner input.**

- ✅ **Survey witness**:
  `computations/model-b-he4-knot-survey.witness.json`
  via `probe_he4_model_b_knot_survey.py`. Computes $\tau_M(\beta)$
  at $q_0$ in both Plancherel and Wenzl-Schur conventions for
  $\{L6a4,\ 8_{17},\ 8_{18},\ 10_{123}\}$ in $B_3$; ranks against
  AME$(^4\mathrm{He}) = 28.30$ MeV with the plausibility window
  $\tau_M \in [0.05, 0.5]$.
- ⏳ **Owner decision pending**: pick the canonical knot from the
  ranking below.

**Survey results (Wenzl-Schur convention at $q_0$):**

| Rank | Knot | crossings | vol | $\lvert\tau_M\rvert$ | $T_1 = m_e \lvert\tau_M\rvert$ (MeV) | in window |
|-----:|------|----------:|----:|---------------------:|-------------------------------------:|:---------:|
| 1 | $8_{17}$ (high-vol amphichiral) |  8 | 10.986 | 0.186 | 0.0949 | ✓ |
| 2 | $10_{123}$ (T(5,2)-like)        | 10 | 17.086 | 0.221 | 0.1130 | ✓ |
| 3 | $8_{18}$ (4-bridge symmetric)   |  8 | 12.351 | 0.109 | 0.0558 | ✓ |
| 4 | $L6a4$ (Borromean, ³He twin)    |  6 |  8.000 | 0.998 | 0.5102 | ✗ |

**Reading of the survey:**

- The ³He-twin $L6a4$ assignment is empirically excluded — its
  $\lvert\tau_M\rvert$ at $q_0$ is $\approx 1.0$, an order of
  magnitude above the plausibility window. The "degenerate
  assignment" concern in the candidate list is borne out
  numerically.
- All three of $\{8_{17},\ 8_{18},\ 10_{123}\}$ pass the
  plausibility window. The plan's primary structural candidate
  ($8_{18}$, 4-fold symmetric) sits at the lower edge; $8_{17}$
  and $10_{123}$ are closer to the geometric mean of the window
  ($\approx 0.158$) and would shift $T_1(^4\mathrm{He})$ by
  $\approx 2$x.
- The Brunnian 4-component link enumerated in the candidate list
  is **not yet surveyed** — no canonical braid word in hand;
  surveying it requires either extending the Hoefsmit cache to
  $H_4$ or sourcing a $B_3$ closure of an equivalent knot.

**Owner decision needed:** select the canonical $^4\mathrm{He}$
Model B knot from the surveyed candidates (or commission a
4-strand follow-up survey for the Brunnian link). The survey
itself is Markov-invariant and does not encode non-trace
constraints (symmetry group, bridge index, chirality compatibility
with the $[+1,-1,+1,-1]$ sign pattern).

### Phase 2 — Surviving brane-tower closure path

#### P2.A — Wire `tower_mode="habiro"` (Path 3)

**Math:** Per `prop:full-pole-structure-mass-trace`,
$$
  \tau_M(T_w; q) \;=\; \sum_m a_m(T_w) \cdot (q; q)_m,
  \qquad a_m \in \mathbb{Z}[q^{\pm1}]
$$
collapses Terms 1, 2, 3, 6 into a single Markov-invariant sum. Each
$a_m$ is in $\mathbb{Z}[q^{\pm1}]$ hence Markov-invariant by
inheritance. This is Path 3 of the closure paths in
`knot-mass-formula-unified.md` lines 80–101.

**Existing implementation:** `path_b_habiro_mass_probe.py` does the
end-to-end computation and emits `path-b-habiro-mass-probe.witness.json`
with predictions:
- p: 932.68 MeV (vs AME 938.78 atomic) — $\sim 0.65$% error
- n: 934.28 MeV (vs AME 939.57) — $\sim 0.56$% error
- D: 1876.12 MeV (calibrated to deuteron)

**⚠️ HONESTY CAVEAT — calibration leak in current Path B:** Line 227 of
`path_b_habiro_mass_probe.py` does `alpha_M = B_D_observed / tr_M_D`,
i.e. it **fits a single prefactor $\alpha_M$ to the deuteron binding
energy**. This is a CAL-3-adjacent calibration; not strictly within
the 3-anchor discipline. The branch hint claim of "sub-1 % closure on
{p, n, D, T, ³He}" should be read as "sub-1 % under deuteron-prefactor
calibration", not as substrate-only.

**Code:** (a) Add `tower_mode="habiro"` to `paper_six_term_mass()`
in `paper_six_term_isotope_sweep.py`. The mode reads
$\tau_M^{\mathrm{Habiro}}$ from `path-b-habiro-mass-probe.witness.json`
(or recomputes from `habiro-coefficients-atomic.witness.json` directly).
(b) Set $T_2 = T_3 = 0$ in this mode (the Habiro sum already
encompasses them). (c) Use the Habiro-derived $\tau_M$ as $T_1$.

**Coverage gap:** `habiro-coefficients-atomic.witness.json` currently
contains **only {p, n, D}**. Extending to {T, ³He, ⁴He} requires
running `habiro_coefficients_atomic.py` for those isotopes — a
separate compute step (likely several hours per atom on a single
core because the symbolic Habiro expansion at $n=9, 12$ is heavy).

**Sanity check:** the Habiro evaluation should agree with the
witness-recorded `tr_M_at_q0` to $10^{-6}$ relative (the existing
`agree` flag in `evaluate_habiro_sum` enforces this).

#### P2.B — Combined per-partition $k_\lambda$ + Habiro sweep

**Status:** Blocked on P1.D (which is blocked on PR #639 merge). The
combined run produces the M1 mass table.

### Phase 3 — Structural closure of $\Delta_{\mathrm{shell}}$

**Status:** **DEFERRED to dedicated PR(s).** New math, not plumbing.
The next agent should pick up `2026-05-11-1ppb-gap-narrowing-plan.md`
§Path A directly: propose closed-form $f$ in `DeltaCouplingClosedForm`
(candidates: $\log(1/t)$, $1/t-1$, $\log\Phi_q^{(\infty)}(t)$, KLR
canonical-basis dim count). Anchor: $\Delta_{\mathrm{coupling}}(2,2)
= +13.20$ MeV (extracted, not calibrated).

### Phase 4 — Lean closure

**Status:** **DELEGATED to Lean agent.** See companion handover
document [`2026-05-12-lean-handover.md`](2026-05-12-lean-handover.md).

## 4  Anti-patterns (per AGENTS.md three-cal discipline)

- ❌ **Calibrate** $\Delta_{\mathrm{shell}}$ or $\Delta_{\mathrm{coupling}}$ to AME — this is fitting, not predicting.
- ❌ **Add** ad-hoc per-atom corrections that don't trace to substrate data.
- ❌ **Tune** $n_\star$ or $k_\lambda$ per atom without structural justification.
- ❌ **Hide** the $\alpha_M$ deuteron calibration in Path B — flag every
  use as a Tier-2 calibration leak per
  `2026-05-11-three-calibration-discipline-violations.md`.

## 5  Milestone re-statement (M0 → M5 ladder)

| Milestone | Target residual | Phase that gets us there |
|-----------|---------------:|--------------------------|
| **M0** (now)  | $\sim 22\%$ MAE | post-#638 calibrated sweep |
| **M1** | $\sim 1\%$ on ⁴He | Phase 1 + P2.A (Path 3 Habiro) |
| **M2** | $\sim 0.1\%$ on light | + P3.A (closed-form $f$ for $\Delta_{\mathrm{coupling}}$) |
| **M3** | $\sim 100$ ppm | + P3.A on multiple atoms |
| **M4** | $\sim 10$ ppb | + P3.B (crystal-bases optimisation, A ≥ 5) |
| **M5** (1 ppb) | $\sim 1$ ppb | + Phase 4 Lean closure + N=4 truncation per #639's $c(K)$ ceiling |
| **Hard floor** | $\sim 780$ ppb | CAL-2 propagation; cannot improve without sharper $q_0$ |

## 6  Handover summary for next agent

**Pick up here:**

1. Check PR #639 merge state. If merged, rebase this branch and do
   P1.D cherry-pick first (highest leverage among Phase 1).
2. Implement P1.A (substrate $E_0$ mode) — purely mechanical.
3. Implement P2.A (`tower_mode="habiro"`) — purely mechanical given
   the existing `path-b-habiro-mass-probe.witness.json`.
4. Migrate P1.C straggler in `mass_formula_6term_mpfr_50dps.py:223`.
5. P1.B (Markov-pairing chirality) is a $\sim$1-day task; the
   `_deprecated/term5_aK_audit.py` already has the math.
6. P1.E (⁴He Model B knot) needs owner input — produce the
   candidate-survey witness and ask.

**Do NOT touch:**
- The proton-fitted `run_sweep_for_mode` calibration without adding
  the substrate-$E_0$ alternative side-by-side (P1.A). Removing the
  calibrated mode breaks all downstream witnesses.
- Any T4 implementation in scripts not listed in P1.C above without
  re-grepping; new consumers may have appeared.
