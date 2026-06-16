> **DEPRECATED on 2026-05-24.** Superseded by [`2026-05-18-1ppb-workplan-v7-100x-experimental.md`](../2026-05-18-1ppb-workplan-v7-100x-experimental.md) (the latest in the 1ppb-workplan chain). Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) §"5-tranche recommendation" T4 for the deprecation rationale.

# 1 ppb work plan — update 2026-05-10

Refreshes the 2026-05-09 plan
([`docs/audits/2026-05-09-mass-table-1ppb-audit.md`](2026-05-09-mass-table-1ppb-audit.md))
in light of two days of substantive progress on `origin/main`.

## What landed (last 48 h, ordered by relevance to 1 ppb)

### PR #623 — `claude/ppb-math-infrastructure-p3oQQ` (28 lean(infra) batches)

The largest single block of 1 ppb-relevant infrastructure to land on
`main`. Headline shipments:

- **`QOU.HeckeAlgebra.JonesMarkovWenzl`** — Wenzl 1988 closed-form
  for $y_\lambda$ at the Lean level (`qInteger`, the principal
  Schur element; integrates the same convention bridge proved in
  `prop:y-lambda-closed-form-wenzl-bridge`).
- **`QOU.HeckeAlgebra.MarkovTrace`** — `axiom JonesMarkovCoefficient`,
  `axiom JonesMarkovCoefficient_sum_eq_one` (Plancherel identity at
  the Lean level), `axiom markovTrace`, plus `axiom heckeMul` for
  the multiplication.
- **`QOU.HeckeAlgebra.{Wedderburn, Common, Hoefsmit, QSubstrate}`** —
  Wedderburn decomposition with PSD scalar smul / addition
  preservation; `axiom q_0` and `q_0_gt_one` typed at Lean level;
  Hoefsmit seminormal axioms with the Hecke quadratic relation;
  Frobenius inner product positivity.
- **`QOU.MathlibExt.{PosSemidefDiagZero, PosSemidefTraceZero,
  SDPEmptyConstraints, SDPRealUniqueness, FrobeniusInnerProduct}`**
  — the missing Mathlib pieces that make SDP-uniqueness theorems
  expressible at the Lean level.
- **`QOU.BraidKnot.{AppliedDeuteronUniqueness,
  AppliedTritiumUniqueness, AppliedHelium3Uniqueness,
  CanonicalKnotIdSDPUniqueness, PerNucleusMassDerivation,
  HopfBindingK, MassFormulaCategorical, PSDFeasibilityProxy,
  R5FullWitness, LightNucleus}`** — applied uniqueness theorems
  for D, T, ³He plus the categorical mass formula and per-nucleus
  derivation framework.

The Lean-side scaffolding is now in place to express **per-nucleus
binding-energy uniqueness theorems** the way the narrative has been
asserting them for months. The actual derivation chains in
`computations/*.py` are not yet wired through the
new uniqueness instances — that wiring is **Phase 1 of this update**.

### PR #622 — `claude/term7-alpha5-derive-investigation` (merged earlier)

Iterative LP-dual at H_3 + spin-involution invariance theorem,
fully verified by Lean. Provides the scaffolding for per-particle
$u^{(\ell)*}(\beta)$ extraction at every level $\ell$.

### PR #614 — `claude/issue-604-binding-k-enumerator`

Binding-K enumerator + sharpened `bindingKUniqueness` proposition.
The `binding_k_solver.py` pipeline is now wired for issue #604
deliverable 3.

### PR #617 — mass-table: derived `m_p` only

Marks `m_n` and `B(⁴He+)` explicitly as **pending** in
`mass-table-best.witness.json`. Wires LP duals through and adds a
50-dps cache. Honest current-state ledger.

### PR #571 — KLR / crystal-language upgrades

Transfer-matrix and jet-prefix GB filtration are now expressed in
crystal-graph language; closes the convention chasm between the
KLR program (this branch's Phase 8) and the existing GB filtration.

### PR #618 + #567 — Hecke NF shift implementation

Path A multi-nucleon **CLOSED**: deuteron `shift_NF = 40` verified
rigorously; cached `y_λ` + `chi` auto-cache + per-term pole. Cross-
confirms the Path A proton cite in mass-table.

## Where the gap stands now (2026-05-10)

| Isotope | $\Delta\mathfrak{m}$ vs CODATA | Pre-2026-05-09 | Now | Drop |
|---------|-------------------------------:|---------------:|----:|-----:|
| ¹H ($\mathfrak{p}$) full chain | 544k ppb | 544k ppb | 544k ppb | 0 |
| ¹H lift-only (audit) | 14 ppb | 14 ppb | 14 ppb | 0 |
| ²H (D) binding | +1.09% | +1.09% | +1.09% | 0 |
| ³H (T) binding | −0.156% | −0.156% | −0.156% | 0 |
| ³He binding | −2.97% | −2.97% | −2.97% | 0 |
| ⁴He binding | +5.87% | +5.87% | +5.87% | 0 |
| ⁸Be binding | — | — | +10.34% | new |
| ¹²C binding | — | — | +5.41% | new |
| ¹⁶O binding | — | — | +5.30% | new |
| ²⁰Ne binding | — | — | +8.34% | new |
| ²⁴Mg binding | — | — | +9.02% | new |
| ⁴⁰Ca binding | — | — | +19.51% | new |

Numerical errors did not move; the substrate work added Lean
*infrastructure* and *uniqueness theorems*, not new derivations.
Heavy-nucleus rows are now exposed (α-cluster expansion); they
inherit the ⁴He floor and the c_αα coupling fit, so each tier of
A growth amplifies the per-nucleon error.

### Open siblings (status as of 2026-05-10 04:00 UTC)

| PR  | Branch | Scope | Overlap with PR #621 |
|-----|--------|-------|----------------------|
| #621 (this) | `claude/upgrade-klr-algebras-OdYFc` | Phase 1.8 braid encoding deep-dive + KLR Phase 8 + Wenzl-bridge fix + uniqueness theorem | — |
| #628 | `claude/sdp-axiom-class-bridge` | `SDPSlaterUniqueness` class — §3b conditional kernel-uniqueness | adjacent: same conditional-class pattern as my `wenzl_bridge_unique_categorical` |
| #625 | `claude/kite-tail-reconciliation` | $A^\lambda_{\mu\nu}(I)$ structural rank theorem + per-interface extract + Lean | adjacent: cites the same Wenzl-bridge $y_\lambda$ |
| #626 | `claude/lp-dual-followup-1-2-3` | PR #622 review fixes + scaling-conjecture research | adjacent: builds on iterative LP-dual |
| #629 | `claude/pr600-option-e-crystal-weight` | Option E (Kashiwara $c_\lambda$) **breaks** Hopf-antipode invariance under canonical $\Delta_I$ words | **negative finding** — relevant to crystal-graph KLR program |
| #630 | `claude/fix-habiro-interpolate-disagreement` | habiro_coefficients_interpolate fix to canonical $y_\lambda$ | **DIRECT DUPLICATE** of PR #621 commit `a82197577`; #630 is smaller and likely merges first |

## Updated work plan

### Phase 0 — Land PR #621 (DONE — merged)

PR #621 merged 2026-05-10 as `d6bab3065`. Net-new contributions on
main:

- Wenzl-bridge factor-of-2 fix (canonical $y_\lambda$ in
  `habiro_coefficients_interpolate.py`)
- §3b-cond uniqueness-of-convention-shift theorem
  (`wenzl_bridge_unique_definitional`,
  `wenzl_bridge_unique_categorical`, no `sorry`)
- T1: n=6 + n=7 Frobenius co-Casimir codimension theorems
- Phase 1.8 braid-encoding deep-dive audit
- Updated 1 ppb workplan (this document)

PR #630 (parallel duplicate of the factor-of-2 fix) closed as
redundant.

### Session progress note (2026-05-10)

Phase 1 + Phase 2 partial delivery on PR #631
(`claude/wire-applied-uniqueness-mass-table`):

- **Phase 1 delivered**: `applied_uniqueness_mass_table.py` consumes
  canonical `|tr_M(β_K, q_0)|` from `derivation_chain.TR_M_AT_Q0`
  and applies the categorical mass formula from
  `QOU.BraidKnot.MassFormulaCategorical`. Reports
  `applied-uniqueness-mass-table.witness.json` with err_ppb vs
  CODATA / AME baselines. Predictions sit at $-2.5 \times 10^8$
  to $-3.5 \times 10^8$ ppb with the placeholder $m_{e,\text{Hecke}}$;
  Phase 2's substitution will tighten by ~5 orders of magnitude.
- **Phase 1.2 / 1.3 (T, ³He)**: blocked on `chi-tritium-h9` partial
  cache (2/30 partitions) and missing `chi-helium3-h9` cache.
  Workplan-Phase-8 graded-Hecke-energy infrastructure (per-grade
  truncation + resumable cache) would unblock.
- **Phase 2 diagnostic**: `phase2_proton_m_e_hecke_diagnostic.py`
  surveys three approaches (full 6-term, categorical-ratio,
  placeholder-anomaly) and finds NONE close. Recommends T1+T4
  Path A partial chain as an interim, with T2 as the highest-
  priority follow-up audit (likely contaminated by the same
  legacy-weight bug as PR #621/#630).
- **Phase 5 (n=8 Frobenius co-Casimir)** — DELIVERED: convention
  pinned (quantum hook-length formula
  $\dim_q(\lambda) = [n]_q! / \prod_x [h_x]_q$), `heckeH8DimQ`,
  22 simp lemmas, `Fin_sum_univ_twentytwo`, and
  `hecke_n8_frobenius_codim` integrated into
  `frobenius-codim-universal.lean`. Conjugate-symmetric ordering
  matches the n=6 / n=7 pattern (idx i ↔ idx (21-i)); 10 conjugate
  pairs + 2 self-conjugates ((4,2,1,1) at idx 10, (3,3,2) at idx 11).
  Closure unblocks ⁴He's H_{12} block. Generator script
  `phase5_n8_dim_q_table.py` + table `phase5-n8-dim-q-table.json`
  committed for downstream extension to n=9 (triton/³He at H_9)
  and n=12 (⁴He). Paper-side documentation in
  [`frobenius-codim-universal.md §"Explicit Lean closures by partition count $n$"`](../../content/quantum-observable-universe/braids-and-knots/frobenius-codim-universal.md).

- **Phase 8 (graded Hecke energy infrastructure)** — DELIVERED:
  new content block
  [`prop:graded-hecke-energy-truncation-bound`](../../content/quantum-observable-universe/braids-and-knots/graded-hecke-energy-truncation-bound.md)
  proves $P_K(q)$ has at most $\ell(K, q_0) + 1$ nonzero grades
  conditional on the GS-filtration descent
  (CLAUDE.md §3b-cond conditional class). Companion script
  `graded_hecke_energy_probe.py` stratifies the canonical
  Wenzl-bridge $|\mathrm{tr}_M(\beta_K, q_0)|$ per partition by
  content-sum grade and reports cumulative convergence. Empirical
  results at $q_0$:

  | atom | $p(3A)$ | grades | $\ell_{\text{eff}}$ (1e-12) | $\ell_{\text{eff}}$ (1e-3) |
  |------|--------:|-------:|----------------------------:|---------------------------:|
  | proton | 3 | 3 | 3 | 1 |
  | neutron | 3 | 3 | 3 | 1 |
  | deuteron | 11 | 9 | 15 (max grade) | 6 |

  Loose-tolerance speedups confirm the truncation bound. The
  proposition + probe together provide the structural unblocker
  for Phase 1.2 / 1.3: cache stratified by content-sum grade
  (instead of partition index) makes the slow T / ³He chi
  computation resumable and truncatable.

If PR #630 merges first, rebase #621 on top and drop the redundant
`a82197577` commit; the audit doc + uniqueness theorem additions
remain net-new contributions.

### Phase 1 — Wire the new lean(infra) into derivation scripts (HIGH ROI)

Target: turn `AppliedDeuteronUniqueness`, `AppliedTritiumUniqueness`,
`AppliedHelium3Uniqueness`, `CanonicalKnotIdSDPUniqueness` from
free-standing Lean blocks into **actual gates on the derivation
scripts**. Currently `mass-table-best.witness.json` re-emits the
same +1.09% / −0.156% / −2.97% / +5.87% rows because the prediction
formulas (`m_e · Vol(K)`, `2·m_e · Vol(K)`, `A · 8G`) are still the
hyp-census heuristic, not the SDP-uniqueness derivation.

Subtasks:

1. Translate `AppliedDeuteronUniqueness` from Lean type-level
   guarantee into a Python callable that emits a unique
   $\mathfrak{m}_D$ per Wedderburn-block decomposition + LP dual,
   refusing to fall back on `m_e · Vol(6_2)`.
2. Same for T (`AppliedTritiumUniqueness` → 8_11 chain).
3. Same for ³He (`AppliedHelium3Uniqueness` → L6a4 chain).
4. Reroute `mass-table-best.witness.json` to consume these new
   derived predictions; preserve the legacy hyp-census rows under
   `comparison_legacy:` for visibility.

**Expected drop**: D / T / ³He errors should fall by ~1–2 orders
of magnitude (from 1–3% to 0.01–0.1%) once the predictions come
from the SDP-derived chain rather than fitted volumes.

**Files**:
- `computations/applied_{deuteron,tritium,helium3}_derivation.py` (new)
- `computations/atomic_braid_mass_table.py` (consumer; consume new derivations)

### Phase 2 — Proton 544k ppb root-cause closure

Audit ([`docs/audits/2026-05-09-proton-m_e-anomaly.md`](2026-05-09-proton-m_e-anomaly.md))
identified `M_HECKE_PIPELINE_AT_Q0` literals as the bug source: the
ratio sits at $(m_p - m_e)/m_e$ + ~470 ppb, not $m_p / m_e$. PR
#621 marked them DEPRECATED but did not replace them.

Subtasks:

1. Derive `m_p_Hecke` and `m_e_Hecke` symbolically from the Path A
   50-dps pipeline (#618's `shift_NF = 40` deuteron-cross-confirmed
   construction, applied to $A = 1$ atoms).
2. Replace the placeholder literals in `derivation_chain.py` with
   calls to the new derivation; emit a `proton-m_e-derivation.witness.json`
   that pins both numerator and denominator to the witness chain.
3. Verify $(m_p - m_e)/m_e + (m_e/m_e) = m_p/m_e$ does not require
   an algebraic +1; the natural derivation should produce the right
   ratio without that adjustment.
4. Audit downstream: every consumer of `M_HECKE_PIPELINE_AT_Q0`
   (currently only `proton_m_e_anomaly_audit.py` after PR #621's
   DEPRECATED note) gets rewired or marked audit-only.

**Expected drop**: $m_p$ from 937.7615 → 938.27 MeV (within Path
A precision floor, ~10 ppb). Resolves the 544k ppb structurally.

**Files**:
- `computations/derive_m_p_hecke_path_a.py` (new)
- `computations/derive_m_e_hecke_path_a.py` (new)
- `computations/derivation_chain.py` (consumer)

### Phase 3 — Triton (smallest absolute error, easiest first win)

T binding sits at -1556k ppb, the closest to 1 ppb of any A ≥ 2
isotope. The Path A pipeline is already verified for the deuteron
(#618 `shift_NF = 40`), so extending to T is mechanical:

1. Compute `shift_NF` for T at H_9 via the Path A construction.
2. Wire `chi-tritium-h9.witness.json` (cached chi values) into the
   binding-energy formula `B(T) = E(T_w_T, q_0) - E(T_w_p, q_0) -
   2·E(T_w_n, q_0)`.
3. Use Wenzl-bridge $y_\lambda$ at $n = 9$ (PR #621 fix; partitions
   of 9 already covered in `y-lambda-wenzl-bridge-symbolic-witness.json`).
4. Cross-check with `iterative_lp_dual_h9_tritium.py` (analogue of
   PR #621's H_6 deuteron iterative LP-dual at H_9).

**Expected drop**: T binding from -1556k ppb → ~10 ppb (Path A
precision floor at A=3).

### Phase 4 — ³He sign-asymmetry resolution

³He at -2.97% vs D at +1.09% pattern is a cross-knot interference
signature. Phase 1's `AppliedHelium3Uniqueness` wiring should
resolve the sign automatically once the L_6a4 chain runs through
the SDP rather than the volume-fit. If the residual is still > 100
ppb after Phase 1:

1. Apply the iterative LP-dual at H_9 with σ↔σ⁻¹-aware character
   chain (the proton's σ_1^7 σ_2^4 word does not extend cleanly to
   the ³He braid via the same character-table reduction; needs the
   neutron-side chain from `delta_n2_lp_dual_extraction.py` deferred
   note).
2. Verify the Hopf-antipode invariance with the Wenzl-bridge $y_\lambda$
   word (PR #629 found Option E violates this; need to confirm
   canonical $y_\lambda$ does not).

### Phase 5 — ⁴He (n=8 Frobenius co-Casimir closure)

PR #621 closed n=6 and n=7 Frobenius co-Casimir codimension. ⁴He's
H_{12} block needs n=8 explicit closure following the same
`Fin.sum_univ_*` pattern (lines 217 of
`frobenius-codim-universal.lean`).

1. Mechanical extension: 22 partitions of 8, `Fin 22` enumeration,
   `rfl + simp + ring`.
2. Once n=8 closes, ⁴He's `frobeniusCoCasimirTraceFallback` is
   replaced by the explicit Lean theorem.
3. The current +5.87% ⁴He error has two components:
   (a) the fallback path's tautological return,
   (b) the `A · 8G` magic rule (where `8G` is the ³He volume scaled by 1.063).
   Both go away once Phase 1 + n=8 closure lands.

**Expected drop**: ⁴He from +5.87% → < 0.1%.

### Phase 6 — Heavy-nucleus α-cluster derivation

A ≥ 8 isotopes (⁸Be, ¹²C, ¹⁶O, ²⁰Ne, ²⁴Mg, ⁴⁰Ca) currently use
`B = n_α · B(⁴He) + n_pairs · c_αα` with `c_αα = 2.43 MeV` fitted.
The 5–20% error compounds with A. Need:

1. Derive `c_αα` from `HopfBindingK` (PR #623 batch 3) — coupling
   constant from the Hopf algebra of the 4He cluster.
2. Apply n=12, n=16, n=20 Frobenius co-Casimir closures (analogue
   of Phase 5).
3. Verify the α-cluster expansion is exact at the SDP level, not a
   fit.

### Phase 7 — Structural CODATA floor (long-game)

The 22 ppb m_μ/m_e calibration floor on q_0 (per `q_parameter.py:21-25`)
remains the structural blocker for sub-22 ppb predictions on any
chain that reads q_0. Without a non-CODATA derivation of q_0, 1 ppb
on derived predictions is **structurally impossible** below this
floor.

This is research-grade; deferred until Phases 1–5 close the
~10⁴–10⁵ ppb gaps.

### Phase 8 — KLR Phase 8 propositions (defer)

PR #621 dropped the KLR Phase 8 propositions in favour of upstream
duplicates that landed in main during the branch's lifetime
(`conj:crystal-graph-realization`,
`conj:cemetery-group-emergence`,
`conj:confinement-grading-correspondence`). The KLR research
program continues but is now off the 1 ppb critical path.

## Critical path (next sprint)

```
Phase 0 (PR #621 land) ──┐
                         ▼
                    Phase 1 ──→ Phase 3 (T)  ──→ Phase 5 (⁴He) ──→ Phase 6 (heavy)
                         │           │
                         │           ▼
                         │      Phase 4 (³He)
                         ▼
                    Phase 2 (proton 544k ppb)
```

Phase 1 (wire lean(infra) into scripts) is the single highest-ROI
task on the queue. It both closes #623's Lean→compute gap AND
enables Phase 3/4/5 by making `mass-table-best.witness.json`
consume the new uniqueness-derived predictions instead of the fit.

## Reuse — leverage what landed

- `QOU.HeckeAlgebra.JonesMarkovWenzl.qInteger` (Lean) ← my
  `wenzl_bridge_unique_categorical` (PR #621) builds on the same
  convention bridge; cite directly.
- `QOU.BraidKnot.AppliedDeuteronUniqueness` (Lean) — the formal
  uniqueness theorem; Phase 1 just needs the Python-side wrapper.
- `binding_k_solver.py` (PR #614) — the H_{3·A} SDP solver Phase 1
  needs.
- `wedderburn_jones_markov.y_lambda_at` (PR #572 + sibling #630) —
  the canonical numerical y_λ implementation; should replace
  PR #621's `y_lambda_wenzl_bridge_numeric` import once #630
  merges (functionally equivalent, but consolidating to one
  canonical entry point reduces audit surface).
- Hoefsmit caches `chi-{atom}-h{n}.witness.json` (PR #618) — already
  cover D, T, ³He, ⁴He at H_3·A; Phase 1 reads them directly.

## Verification at each phase

1. After Phase 1: `mass-table-best.witness.json` regenerates with
   D / T / ³He errors < 0.1%; legacy `comparison_legacy:` rows
   preserved for diff.
2. After Phase 2: `proton-mass-50dps.derivation.json` reports
   `m_p_predicted ≈ 938.272 MeV ± 10 ppb`; `proton-m_e-anomaly-audit`
   becomes a closed audit (no longer flags 544k ppb).
3. After Phase 3: `tritium-binding-1ppb.witness.json` (new)
   reports `B(T) = 8.4818 ± 10 ppb`.
4. After Phase 4: `helium3-binding-1ppb.witness.json` reports
   `B(³He) = 7.7180 ± 10 ppb`.
5. After Phase 5: `helium4-binding-1ppb.witness.json` reports
   `B(⁴He) = 28.296 ± 10 ppb`; n=8 Lean theorem builds.
6. After Phase 6: `mass-table-ppb.witness.json` heavy rows drop
   from 5–20% to < 1%.
7. Phase 7 (CODATA floor) gates the final 22 → 1 ppb push.
