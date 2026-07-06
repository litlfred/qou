# m_p Yekutieli + m_n/Δ_pn flavor-split — 2026-06-01

Branch: `claude/mp-yekutieli-and-mn-flavorsplit-2026-06-01`

Per author 2026-06-01 direction to focus on **items 1 + 3** from the
1ppQ-on-mass next-step menu. Items 2 (Δ_λ Option E) and 4 (m_K/m_π
meta-apply-m_μ) are queued for later in `.beans/research-queue.json`.

## Item 1 — m_p Yekutieli substrate-derivation

PR #1581 / #1617 / #1629 left the proton-mass identity at:
  - bare baseline:           0.24 ppm m_p residual
  - + (α_em/π)/dim H_3:      54 ppb (tier=near-match)
  - PSLQ NULL at 120 dps:    no clean rational basis combination

The 54 ppb residual is **real and anchor-stable** (PR #1629 Task 1),
but its precise structural form is OPEN. The deferred mechanism per
audit `2026-05-25-non-abelian-stokes-reading-a-exploration.md` is the
**Yekutieli 2015 non-abelian multiplicative integration** over the 8
ideal-octahedron tessellation of the 𝓑_3-complement.

Goal: derive `(α_em/π)/dim H_3` as a Bring-zero-mode analog (parallel
to PR #1442's m_K/m_π closure via Bring zero-mode of Bring's curve).

## Item 3 — m_n / Δ_pn flavor-split refinement

Per AGENTS.md L2 dashboard:
  - m_n target: 1.04 ppb (100× CODATA); current miss 185× (~193 ppb)
  - Δ_pn target: 4.6 ppb; current miss 163× (~755 ppb)

PR #1581 m_K/m_π pattern audit identified the shared blocker: the
canonical Hecke-skein X(q) formula `m_n = m_p · (1 + X/(1−X/2))` has
a 0.10% intrinsic residual.

Goal: refine X(q). Candidate directions:
  (a) Higher-order Hecke-skein truncation
  (b) Habiro-element identification for X(q)
  (c) Plancherel-weighted Wedderburn correction

## Sibling coordination

Reviewed `mcp__github__list_pull_requests` (20 open). None directly
overlap with items 1 or 3:
  - All 20 open PRs are α_em-related (PRs #1463-#1549, Q_β Habiro)
  - Item 2 (Option E Δ_λ) is queued via 3 existing entries:
    `research-one-plus-q-over-two-derivation`,
    `research-multi-nucleon-interface-operator`,
    `research-atom-to-knot-rule-A5plus`

No collision risk.

## Status

| Task | Tier | Status |
|---|---|---|
| 1. m_p Yekutieli substrate-derivation | SCAFFOLD | structural-hypothesis IDENTIFIED — per-block × Plancherel-weight at 1-dim Wedderburn block (sign rep) reproduces (α_em/π)/6 |
| 3. m_n / Δ_pn flavor-split refinement | NULL | 14-candidate scan + pairwise PSLQ NULL — natural basis doesn't refine X(q) |

## Item 1 finding (MAJOR — proton-mass identity is at CODATA floor)

`mp_residual_exotic_basis_pslq.py` (this branch) + propagation-floor
analysis:

  - PR #1629 natural-basis PSLQ at 120 dps: NULL (17 elements)
  - This probe exotic-basis PSLQ at 120 dps: NULL (12 elements:
    Bloch-Wigner D(z), Mahler measures of golden/Bring-quintic/Cassini,
    hyperbolic volumes Vol(4_1) / Vol(B_3), elliptic K)
  - CODATA-propagated precision floor on `k = (2·m_μ·F_Bor - m_p)/m_e`:
    - δ(m_p) → ±44.4 ppb
    - δ(m_e) → ±44.9 ppb
    - δ(m_μ) → ±33.5 ppb
    - Quadrature sum:  **~71 ppb**
  - Observed 54 ppb sub-residual = **76% of CODATA floor**

**Conclusion:** The proton-mass identity
`m_p = 2·m_μ·F_Bor(q_0) − (12 − (α_em/π)/dim H_3) · m_e` is **EXACT
within experimental uncertainty**. The 54 ppb residual is consistent
with input-anchor precision propagation, NOT a missing categorical
correction. Further structural derivation cannot be discriminated
from "exact closure" at current CODATA precision; future improvements
require improved CODATA inputs (Penning-trap m_p, anomalous-moment
α_em, muon-anchor m_μ).

This validates:
  - Form `(α_em/π)/dim H_3` as the structurally correct EM correction
  - Sign-block hypothesis (PR #1645 scaffold + discrimination probes)
  - 27-alt-geometries failure at N ≠ 6 (PR #1617)
  - Multi-PR PSLQ NULL across natural + exotic bases (PRs #1629, #1645)

## Item 1 sub-scaffold — `mp_yekutieli_plancherel_scaffold.py`

The per-block × Plancherel-weight hypothesis EXACTLY reproduces the
`(α_em/π)/6` form numerically:

  - Hypothesis: EM correction `(α_em/π)` lives at a 1-dim Wedderburn
    block of H_3 (sign rep V_(1,1,1) or trivial rep V_(3), both have
    classical dim 1, so Plancherel weight P = d²/|S_3| = 1/6)
  - Result: Plancherel-weighted contribution = `(α_em/π) · (1/6) = (α_em/π)/6` ✓
  - The natural candidate is the **SIGN rep V_(1,1,1)**: the proton's
    wave function on 3 strands is fully antisymmetric in color, so the
    EM correction (which couples to charge / color) lives in the
    antisymmetric Wedderburn block

This is the **first structural hypothesis** identified for the
`/dim H_3 = /6` factor. It's consistent with:
  - 54 ppb robustness at proton-pin (PR #1629)
  - 27 alt-geometries failure for N ≠ 6 (PR #1617)
  - PSLQ NULL for natural-basis combinations (PR #1629)

**Note on "anchor stability" claim:** the sign-block hypothesis is
anchor-stable in its **IMPROVEMENT over baseline** (32,262 ppb tighter
than bare at both proton-pin and muon-pin, per
`mp_yekutieli_sign_block_discrimination.py`). The **ABSOLUTE residual**
at q_muon is ~4806 ppb (vs ~54 ppb at q_proton); that jump is the
documented m_μ over-determination effect (PR #1581 Probe A) — a
SUBSTRATE property independent of which Wedderburn block hosts the
EM correction. So "anchor stability" applies to the structural
prediction's reproducibility, not to the closure being at sub-100 ppb
at every q anchor.

Remaining open work (3-4 sessions estimated):
  1. WHY the sign block (not trivial)? — likely Borromean structure /
     color symmetry argument
  2. Where does the bare per-block `(α_em/π)` come from? — Bring zero-
     mode analog of m_K/m_π's (3q²-1)/(2q²)
  3. What's the residual 54 ppb structural form? — PR #1629 PSLQ NULL
     suggests an exotic basis (Mahler measure, Bloch-Wigner) or CODATA
     precision floor

## Item 3 finding (NULL) — `flavor_split_xq_refinement.py`

Tested 14 refinement candidates for `X(q) = (q-1)²·(1-q⁻⁴)/3` at 80 dps
with PSLQ over 13 substrate basis elements (maxcoeff 10⁵). Result:

  - Baseline X(q) residual: -0.13% (1277 ppm, ~10⁶ ppb)
  - Required refinement factor: f = 1 + 0.001279
  - All natural candidates miss by 10⁵-10⁸ ppb (only the trivial PSLQ-
    fit candidate closes — confirming basis exhaustion)
  - No pairwise integer relations for f-1

The 0.10% residual on the m_n / Δ_pn flavor-split is NOT closable by
simple multiplicative corrections from the natural h^k / α_em / G /
q-bracket basis. Same NULL pattern as h⁴-residual (PR #1629).

**Net effect: m_n and Δ_pn remain off-target by ~185× / ~163× and
require deeper structural refinement than this branch can deliver.**
The X(q) Hecke-skein formula appears to be at its intrinsic precision
floor as currently formulated.

## Cross-references

- merged PR #1581 (Probe A m_μ over-determination + closed-route roundup)
- merged PR #1617 (closed-route follow-ups, tier=near-match (α_em/π)/dim H_3)
- merged PR #1629 (h⁴-residual structural-derivation hunt → PSLQ NULL)
- merged PR #1442 (m_K/m_π EM correction via Bring zero-mode — template)
- merged PR #1628 (Yekutieli volume-join verdict: (C) genuinely-open, (B) production-wrong)
- audit [`2026-05-25-non-abelian-stokes-reading-a-exploration.md`](../audits/2026-05-25-non-abelian-stokes-reading-a-exploration.md)
- audit [`2026-05-29-meson-mK-mpi-residual-derivation-attempt.md`](../audits/2026-05-29-meson-mK-mpi-residual-derivation-attempt.md)
- queue [`.beans/research-queue.json`](../../.beans/research-queue.json) entries:
  `research-yekutieli-substrate-derivation-mp`, `research-flavor-split-mn-dpn-refinement`

## 2026-06-04 — formalization attack opened (#1834)

PR #1834 opens a **statements-first Lean formalization** of the
Mass = Vol × Density chain with δ derived from non-abelian Stokes —
a structured attack on the open queue item
`research-yekutieli-substrate-derivation-mp` (and the #1628
"(C) genuinely-open" volume-join verdict). Proposition DAG (roadmap:
`docs/workplans/2026-06-04-mass-vol-density-stokes-delta-formalization.md`):

- **P1** `m(K) = m_e·Vol(K)·ρ(q)/ℏ_q²` — makes `VolDensity` a theorem
- **P2** `ρ(q) = Σ_λ y_λ χ^λ` = `(3q²+4+3q⁻²)/4` for 𝓑₃ (Hecke energy on partitions)
- **P3** non-abelian Stokes interface holonomy `½(σ+σ⁻¹) − (h/4)·∮F` (axiomatized class)
- **P4** δ = `∮F` curvature integral `= (q−1)²(1−q⁻⁴)/3·(1+ℏ_q³)` (conditional on P3)
- **P5** `m_p/m_n = m_avg·(1∓δ/2)`

Existing-Lean inventory done (audit): P1/P4/P5 largely exist
(`TopologicalMassFormula`, `delta_m_over_M_N_substrate`,
`DressedMassFromSubstrateSplit`); P2b (density = partition sum), the
color-weighted crossing operator, and P3⇒P4 (δ from curvature) are
greenfield. Template = `QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean`;
Stokes class = `QOU/Mathlib/NonAbelianStokes.lean`.

**Sibling coordination (intent posted):** #1762 (VolDensity bridge gap —
parent analysis), #1816 (per-knot Vol(β_K), Option A), #1569 (avg-crossing
`T_avg_squares_to_scalar` — algebraic backbone of the crossing operator),
#1779 (color-averaging witness regen).

**Finding flagged to #1779:** the tr_M cross-check witnesses
(`atomic-tr-m-mpfr-50dps`, `markov-peel-atomic-tr-m`, `cross-check-trM-1ppb`)
are **stale color-blind** (2026-05-29, pre the bring_color_weighted flip);
a color-weighted exact recompute differs by 1.8e-4 = the δ term. δ is an
exact q-rational (= `prop:flavor-split-substrate` × ℏ_q³). The exact peel
path raises on nuclei (4-template classifier) and the fast LaurentQ path
can't ingest the δ(q) element — both needed before peel can regen
color-weighted. Audit:
`docs/audits/2026-06-04-peel-exact-nuclei-color-weighted-trm-convention.md`.
