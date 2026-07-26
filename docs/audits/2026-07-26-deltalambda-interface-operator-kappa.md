# Δ_λ frustration weight κ: derive it, or wall it — the deuteron refutes `edges − κ·triangles`

**Date:** 2026-07-26 · **Branch:** `claude/deltalambda-interface-operator-kappa-2026-07-26`
· **PR:** #4320 · **Axis:** Δ_λ binding closure (GAP-A-3/A-4) · **Tier:**
structural (0-parameter simplex decomposition) + Lean-proved refutation ·
**Discipline:** STRICT anti-fit (no κ solved from AME; κ=2.385 labelled a FIT;
nothing wired).

## Task

Upgrade the #4316 additive-term result — `M(A) = s·(edges − κ·triangles)`, sign
derived / magnitude a proven fit — to a **derivation** by pinning the frustration
weight κ from 0–1 **derived** parameters: Route A the interface operator ρ_F
(PROBE-2, A=3-vs-A=4 weight ratio), Route B the s5-so3 fibre-action W_λ (WRT level
selection). A κ read from derived ρ_F/W_λ is a derivation; a κ tuned to land the
residual ratio −0.1738 is a fit.

## Scout + infra check

| Item | Finding |
|---|---|
| `pyhecke_native` (Rust core) | **AVAILABLE** — `import pyhecke_native` OK; full API (`tr_m_atomic_mpfr`, `chi_lambdas_via_gp`, `lr_coefficient`, `operator_selection_lp`, …). The historical "ρ_F Rust-gated" note (audit 2026-06-23) is **lifted** for the compute layer. |
| Interface operator ρ_F | audit `2026-06-23-interface-operator-derivation-and-4body-assembly.md`: the **multiplicative** interface `(1−∏f)` saturates → ratio 2.70→2.89, 4.4× short of 12.72. The Mayer decomposition `B(A)=C(A,2)b₂+C(A,3)b₃+C(A,4)b₄` gives **b₃/b₂=0.64, b₄/b₂=4.16** (4-body dominant, [1⁴] SU(4) supermultiplet). ρ_F 3-body Ursell cluster (`cluster-operator-vs-mayer-b3`): \|b₃\|≈1.5 MeV magnitude-matches, **sign-opposed**. |
| s5-so3 W_λ (Route B) | ledger `s5-so3-keystone.md`: W_λ is the **infinite-variable full-Hecke principal-specialization** / colored Σ(2,3,5) WRT q-series; no finite arena, WRT infra **not reachable** here for a per-A frustration weight. Route B **gated**. |
| Corpus-grep for prior κ | No prior derivation of the frustration weight. (`κ₅` = Ohtsuki/Q_β asymptotics; `κ_FW` = Coulomb isovector — both unrelated.) Genuinely open. |

## The derivation attack — and its result

The #4316 fit pinned (s, t) on the two points A=3, 4 alone. **The graded ladder
supplies a third, fully-derived point at the deuteron:**

- `ρ_grad(A) = [A]_q!/[2]_q!` ⇒ `ρ_grad(2) = [2]!/[2]! = 1` (derived).
- `ρ_strong(2) = B(²H)/B(²H) = 1` — the deuteron is the *reference* of the
  `ρ_strong` ratios; its self-ratio is 1 **by construction**.
- ⇒ **`M(2) = ρ_strong(2) − ρ_grad(2) = 0`** — derived, AME-independent.

### (R) The `edges − κ·triangles` model is refuted at the deuteron

The model `M(A) = s·C(A,2) − t·C(A,3)` evaluated at A=2 gives
`M(2) = s·C(2,2) − t·C(2,3) = s·1 − t·0 = s`. The sign window requires `s > 0`,
so the model predicts `M(2) = s > 0`, **contradicting the derived `M(2) = 0`.**
No `s > 0` instance reproduces the deuteron. The A=3,4-only fit that produced
κ = 2.385 silently dropped the third (derived, zero) point. **κ = t/s is
structurally ill-posed** — its denominator `s` is pinned to 0; there is no
2-body/edge component to divide by.

### (S) The exact 0-parameter simplex decomposition — residual is pure ≥3-body

Over the derived coordination-graph basis `C(A,k)` (edges, triangles, tetrahedra),
the three points A=2,3,4 pin `M(A) = μ₂·C(A,2) + μ₃·C(A,3) + μ₄·C(A,4)` with **no
free parameter** (unit-lower-triangular counts matrix, det = 1). At the canonical
q₀:

| coeff | body-order | value |
|---|---|---|
| μ₂ | edge (2-body) | **0** (forced by the deuteron) |
| μ₃ | triangle (3-body) | **+0.4708** |
| μ₄ | tetrahedron (4-body) | **−4.591** (dominant; drives the A=4 sign flip) |

`μ₄/μ₃ = −9.75`. The residual is a **pure ≥3-body object** — no edge component, a
positive 3-body triangle, and a large negative 4-body tetrahedron that dominates.
This is the **same tetrahedron dominance** as the derived ρ_F full-binding Mayer
`b₄/b₂ = 4.16` (⁴He α-cluster / closed [1⁴] SU(4) supermultiplet).

## Verdict — WALL for κ + redirect (scope (a))

**κ is NOT derived; it is the wrong structural object.** The specific
`edges − κ·triangles` parametrisation, with an edge term and `s > 0`, is *refuted*
at the deuteron (M(2)=0 forces s=0). This is a clean structural negative, scope
(a) (scope-limited): it does **not** exclude a many-body closure — μ₃>0 and μ₄<0
are legitimate derived triangle + tetrahedron contributions; it excludes only the
edge-carrying `s>0` frustration parametrisation.

**The residual is *derived* to be pure ≥3-body (μ₂=0).** The remaining derivation
target is **μ₄** — the 4-body/tetrahedron α-cluster residual — reachable via the
ρ_F cluster integrals (`pyhecke_native` present) but requiring the **residual
(graded-subtracted) cluster-integral compute**: an identified, **infra-scoped**
next step, not a κ fit. The μ₃ handle is the sign-opposed 3-body Ursell cluster
(`cluster-operator-vs-mayer-b3`), which needs its sign/normalisation pinned.

### Derivation-vs-fit ledger (STRICT)

- **κ = 2.385**: a **FIT** (A=3,4-only; refuted once the derived A=2 point is
  included). Labelled, never wired.
- **μ₂ = 0**: the **derived, AME-independent** fact (deuteron self-reference) —
  the load-bearing result. μ₃, μ₄ are the same AME residuals re-expressed in the
  derived simplex basis (targets, not derived magnitudes).
- Route B (W_λ) is **infra-gated** (WRT / full-Hecke principal specialization not
  reachable). Route A (ρ_F for μ₄) is **infra-reachable but not yet run** (residual
  cluster-integral compute).
- "No seventh fit-based ansatz" + PROBE-4 KL-prune stand. Nothing wired.

## Artifacts

- Probe: [`computations/deltalambda/deltalambda_kappa_interface_residual_simplex_probe.py`](../../computations/deltalambda/deltalambda_kappa_interface_residual_simplex_probe.py)
  · witness `deltalambda-kappa-interface-residual-simplex.witness.json`
- Lean (sorry-free, lean-direct EXIT 0): [`content/quantum-observable-universe/lean/QOU/MassTheory/AdditiveResidualSimplex.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/AdditiveResidualSimplex.lean)
  — `model_refuted_at_deuteron`, `deuteron_forces_edge_weight_zero`,
  `residual_edge_coeff_zero`, `simplex_solve_exists`, `simplex_solve_unique`.

## Cross-refs

- #4316 [`QOU.MassTheory.AdditiveSignChangingTerm`](../../content/quantum-observable-universe/lean/QOU/MassTheory/AdditiveSignChangingTerm.lean) — the sign/window + anti-fit certificate this sharpens.
- [`docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`](2026-06-23-interface-operator-derivation-and-4body-assembly.md) — ρ_F / Mayer b₄/b₂=4.16.
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ / PROBE-2 ledger.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — Route B W_λ (gated).
