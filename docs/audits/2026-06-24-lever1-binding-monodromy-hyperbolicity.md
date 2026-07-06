# Lever-1: the binding monodromy `B` is HYPERBOLIC — not a compact-SU(2) trefoil holonomy

**Date:** 2026-06-24
**Probe:** [`computations/substrate/lever1_binding_monodromy_hyperbolicity.py`](../../computations/substrate/lever1_binding_monodromy_hyperbolicity.py)
**Witness:** [`computations/substrate/lever1-binding-monodromy-hyperbolicity.witness.json`](../../computations/substrate/lever1-binding-monodromy-hyperbolicity.witness.json) (8/8)
**Status:** structural (b)-exclusion + corpus synthesis (directions A + B of the lever-1 frontier). No fit; not owner-gated (pure trace arithmetic). Follows [`2026-06-24-lever1-trB-geometric-target.md`](2026-06-24-lever1-trB-geometric-target.md).

## What this resolves

The lever-1 frontier reduces to one number, `τ = tr B`, where `B` is the rank-2 prolongation
matrix of the binding generating function (`R = x² − τx + 1`, `det B = 1` proved —
`prop:sl2-prolongation-recurrence`, Lean `sl2_prolongation_recurrence`). The
[`2026-06-24` target audit](2026-06-24-lever1-trB-geometric-target.md) left a fork: **(a)** `W`
is a distinct Bring-specific rank-2 factor, or **(b)** the rule values are not the geometric
periods (`a_D ≠ lw`). This probe sharpens **(a)** with a structural exclusion and a corpus
synthesis that the target audit did not cross-reference — the **2026-06-06 M-workplan**.

## The corpus already pins the rank-2 object (M-workplan, 2026-06-06)

[`docs/workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md`](../workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md)
establishes (corpus-backed by `prop:mi-sw-abelianisation`, `prop:prolonged-periods-fixed-depth`,
`prop:sl2-prolongation-recurrence`, Lean `sl2-prolongation-recurrence.lean`):

- `H^{1,0}(Bring)` is the **irreducible** 4-dim `S₅` rep `W` (Riera–Rodríguez 1992) — matching
  the 2026-06-24 Sage character result (A₅-irreducible standard rep).
- `H¹(Bring) = W ⊕ conj W = W ⊗ ℂ²`: `W` enters with **multiplicity 2**.
- `M` (Gauss–Manin) is `S₅`-equivariant ⇒ by Schur `M = id_W ⊗ B`, `B` a **2×2** matrix on the
  **Hodge multiplicity space `ℂ²`**, `det B = 1` (polarisation, `B ∈ Sp(2) = SL₂`).

So the rank-2 object is the `S₅`-Hodge **multiplicity space**, not a sub-space of forms — the
clean reading of "`H¹(Bring) = 2W`". The 2026-06-24 target audit's "`W` must be a CM/isogeny
factor of `Jac(Bring)`" is **compatible** (the Riera–Rodríguez isotypic factor *is* that rank-2
Hodge structure) but under-cited this established resolution.

## The decisive structural exclusion (b): `B` is hyperbolic, the trefoil holonomy is compact

The color elliptic curve `E_z` ([`brings-surface/color-elliptic.md`](../../content/quantum-observable-universe/brings-surface/color-elliptic.md))
is the natural rank-2 candidate for that Hodge structure: it is the elliptic fibre of Bring's
surface, and **its monodromy around the singular fibres recovers the trefoil holonomy
generators** `H₁ = σ₁, H₂ = σ₂` ([`holonomy-trefoil.md`](../../content/quantum-observable-universe/braids-and-knots/holonomy-trefoil.md)),
a `B₃ → SU(2)` representation with `(H₁H₂)³ = id`.

But (probe, 50 dps, `q₀ ≈ 1.10998`):

| quantity | value | class |
|---|---|---|
| `τ_binding = (a_D⁽²⁾+a_D⁽⁴⁾)/a_D⁽³⁾ = 3(3q⁴+8q²+3)/(4q(q+1)²)` | **2.6423863** | `> 2` |
| `tr(H₁H₂)` (compact SU(2), `(H₁H₂)³=id`, 3-cycle) | **−1** | `|·| ≤ 2` |

**`τ_binding = 2.642 > 2` ⇒ `B` is hyperbolic in `SL₂(ℝ)`.** A compact-SU(2) element has all
traces in `[−2, 2]` in the 2-dim representation. Therefore **`B` cannot be a compact
trefoil-holonomy generator** — *(b)-exclusion, invariant cited: the `SL₂(ℝ)` trace dichotomy /
the `|tr| ≤ 2` bound on the 2-dim rep of compact SU(2).*

**Scope (strict (a)/(b)).** This excludes only the **compact evaluation** — it does **not**
exclude the color `E_z` as the rank-2 `W`. The curve is fine; its monodromy is simply evaluated
in the **non-compact** regime at the substrate `q₀ > 1`. `B` is the non-compact
`SU_q(2) → E_q(2)` hyperbolic continuation, with `τ = 2cosh θ_binding`,
`θ_binding = 0.78145` (`λ = e^{θ} = 2.18465`).

## Independent convergence: binding ↔ keystone both require the non-compact arena

The keystone reached the **non-compact** `SU_q(2) → E_q(2)` Hahn–Exton q-Bessel arena from the
`W_λ` / modular-category side (`q₀ > 1` is the growth regime, not a root of unity —
[`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md), 2026-06-22). This probe reaches the
**same** non-compact arena independently from the **binding** (lever-1) side: the binding
monodromy is hyperbolic, structurally excluded from the compact SU(2) holonomy. Two independent
routes — generation (`W_λ`) and binding (`tr B`) — converge on the non-compact arena.

## Refinement of the target audit's torus refutation

The substrate torus is **also** hyperbolic (`τ_torus = 2cosh 2η₀ = 2.04371 > 2`,
`θ_torus = 2η₀ = 0.20868` exactly). So `binding ≠ torus` is a **rapidity** mismatch
(`θ_b/θ_t = 3.7447`), **not** a compact-vs-non-compact one. Both substrate monodromies are
hyperbolic; the binding rapidity `θ_binding` is a genuinely separate, larger value
(`k = θ_b/η₀ = 7.4894`, non-integer ⇒ `τ ≠ q₀^k + q₀^{−k}` for integer `k`, confirming the
target audit's `k ≈ 7.49`).

## Corpus-hygiene flag

The M-workplan references three scripts — `bring_picard_fuchs_kernel.py`, `sl2_tau_solver.py`,
`s5_bring_hodge_depth.py` — that are **not present** in the current tree (only the Lean
`sl2-prolongation-recurrence.lean` and the `prop:` blocks exist). The structural claims are
corpus-backed by the Lean + props; the numerical scripts were never committed (or were dropped).
Flagging for re-creation if the explicit `B` computation is pursued.

## Net + next step (tractable, NOT genus-4, NOT owner-gated)

- **Resolved (B):** the rank-2 `W` is the `S₅`-Hodge multiplicity space `= H¹` of the color
  elliptic `E_z` (Riera–Rodríguez isotypic factor of `Jac(Bring) ~ ` `W`-isotypic) — a rank-2
  *elliptic* object, **not** a fresh genus-4 computation.
- **Sharpened (A):** `τ = tr B` is the **non-compact hyperbolic** rapidity of the color `E_z`
  Picard–Fuchs / Gauss–Manin monodromy at `q₀`, `θ_binding = 0.78145`. The decisive in-session
  test for a future session: compute the color `E_z` (genus-1) Picard–Fuchs monodromy trace and
  check it equals `2.6424`. This is a rank-2 elliptic period problem (tractable without Sage's
  genus-4 `RiemannSurface`), and the explicit hyperbolic `B` is the keystone's q-family `M`
  restricted to the color elliptic factor.
- **Honest scope:** **NOT a keystone closure.** The geometric meaning of the rapidity
  `θ_binding = 0.78145` (vs the torus `2η₀`) is open; the color-`E_z`-monodromy `= τ_binding`
  identity is a well-motivated **hypothesis** (both are rank-2, both carry the trefoil/braid
  monodromy, both Bring-derived), **not** proved here. No fit; nothing wired; no tier change.
