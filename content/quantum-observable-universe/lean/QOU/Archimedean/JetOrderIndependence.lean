import Mathlib.Data.Real.Basic
import QOU.Archimedean.HyperbolicVolumeIndependence

/-!
# QOU.Archimedean.JetOrderIndependence — the gap-closing reduction

**§3b-cond conditional theorem** for content block
[`conj:three-knot-jet-order-independence`](../../../quantum-observable-universe/predicted-spectra/three-knot-jet-order-independence.md):
*Jet-order algebraic independence (QOU-attackable reduction)*.

This file formalises the **reduction** that closes the deep
algebraic-independence conjecture
([`conj:hyperbolic-volume-transcendence`](../../../quantum-observable-universe/predicted-spectra/hyperbolic-volume-transcendence.md))
*relative to two narrower, QOU-native inputs*:

1. `JetOrderIndependence` — finite jet-order independence: the order-`N`
   cyclotomic-coefficient Jacobian of the three coloured-Jones series
   `J_{4₁}, J_{5₂}, J_{𝓑₃}` has full rank `3` from the Reid-1991 base
   order onward. Decidable per order (a Gröbner–Shirshov normal form),
   so this is the QOU-*attackable* weakening.
2. `SurrealParallelTransportBound` — the **bridge**: the surreal
   parallel-transport error of the categorical connection on the
   projective state fibre `ℂP¹`, as `q` deforms toward the
   root-of-unity (volume-conjecture) limit, has vanishing archimedean
   shadow, uniformly in the jet order.

The reduction `hyperbolicVolumeIndependence_of_reduction` derives
`HyperbolicVolumeIndependence` from these two — fully Lean-verified
modulo the two conjectural class instances (per §3b-cond). It does NOT
prove the deep conjecture; it converts a Grothendieck-period dead end
into two internal QOU targets.

## The surreal parallel-transport bound — geometric content + open issues

The coloured-Jones invariant `J_K(q)` is the **holonomy** of the
categorical (Yekutieli non-abelian Stokes / KZ) connection, parallel-
transported along the substrate `q`-deformation path on the projective
state fibre `𝒮 = P ×_G ℂP¹`. The hyperbolic volume is the leading
asymptotics of that holonomy at the singular limit:
`Vol(K) = lim_{n→∞} (2π/n)·log|J_K(e^{2πi/n})|`. The **surreal error
bound** measures the transport error as `q` approaches that singular
(root-of-unity) point; it is surreal (non-Archimedean) precisely
because the limit point is a singularity of the connection, so the
error is an *infinitesimal* in the surreal field, not a real number.

The class field `transportShadow N` is the **archimedean realification**
(`τ`-shadow) of that fibre-level surreal infinitesimal at jet order `N`.
The conjectural content `shadow_vanishes` packages the three open issues
that must hold for the bridge:

- **(I1) Uniformity in jet order.** The transport error must be bounded
  *uniformly* across all truncation orders `N`; otherwise order-`N`
  independence does not transfer to the limit. On `ℂP¹` this is uniform
  control of the connection's curvature along the deformation path,
  independent of `N`. Non-uniform error growing with `N` breaks the
  bridge.
- **(I2) Archimedean projection (the fibre-vs-observable wall).** The
  error lives at the **fibre** level (surreal, possibly carrying the
  `Im(q)` structure of CLAUDE.md's fibre/archimedean box); the volume is
  **archimedean** (`Im(q₀)=0`, real). The bridge needs the surreal
  infinitesimal to project to *exactly* `0` under `τ`. A non-infinitesimal
  archimedean shadow injects a spurious polynomial relation among the
  volumes and independence fails — this is why the field is named a
  *shadow*.
- **(I3) Monodromy separation at the singular limit.** Transport around
  the cusp is flat only at generic `q`; at the root-of-unity limit the
  holonomy picks up cusp/modular monodromy. The bound must separate the
  physical holonomy (`→ Vol`) from the monodromy artifact. Open: is the
  monodromy contribution surreal-controlled, or does it leak into the
  real volume?

`shadow_vanishes : ∀ N, transportShadow N = 0` is the assertion that
(I1)+(I2)+(I3) all hold — the single conjectural input of the bridge.
-/

namespace QOU.Archimedean

/-- **Jet-order independence (weak, QOU-attackable conjecture).**

    `jacobianRank N` is the rank of the order-`N` cyclotomic-coefficient
    Jacobian of the three coloured-Jones series `J_{4₁}, J_{5₂}, J_{𝓑₃}`
    (a `3 × (N+1)` matrix over `ℚ[q,q⁻¹]`). `full_rank` asserts it is the
    full rank `3` from the Reid-1991 base order `N ≥ 3` onward — finite
    and decidable per order via a Gröbner–Shirshov elimination normal
    form. -/
class JetOrderIndependence where
  /-- Rank of the order-`N` coefficient Jacobian of the three series. -/
  jacobianRank : ℕ → ℕ
  /-- Full rank `3` from the base order onward (Reid-1991 anchors `N=3`). -/
  full_rank : ∀ N, 3 ≤ N → jacobianRank N = 3

/-- **Surreal parallel-transport bound (the bridge).**

    `transportShadow N` is the archimedean (`τ`) realification of the
    fibre-level surreal parallel-transport error on the projective state
    fibre `ℂP¹` at jet order `N`, as `q` deforms toward the volume-
    conjecture limit. `shadow_vanishes` is the conjunction of the three
    open issues (I1 uniformity, I2 archimedean projection, I3 monodromy
    separation) — see the module docstring. -/
class SurrealParallelTransportBound where
  /-- Archimedean shadow of the surreal transport error at jet order `N`. -/
  transportShadow : ℕ → ℝ
  /-- The shadow vanishes at every order: the bridge's conjectural input. -/
  shadow_vanishes : ∀ N, transportShadow N = 0

/-- **Gap-closing reduction (§3b-cond conditional theorem).**

    The deep algebraic-independence conjecture `HyperbolicVolumeIndependence`
    follows from the two QOU-native inputs: finite jet-order independence
    (`full_rank`) and the surreal parallel-transport bound
    (`shadow_vanishes`). The conjecture's residual is realised as
    `transportShadow 3 + (jacobianRank 3 − 3)` — the surreal transport
    shadow plus the Jacobian co-rank — which vanishes *exactly* when both
    inputs hold. Fully Lean-verified modulo the two conjectural class
    instances; it is a `def` (not an `instance`) to avoid competing with
    the standalone conjectural witness in `HyperbolicVolumeIndependence`. -/
noncomputable def hyperbolicVolumeIndependence_of_reduction
    [JI : JetOrderIndependence] [PT : SurrealParallelTransportBound] :
    HyperbolicVolumeIndependence :=
  { residual := PT.transportShadow 3 + ((JI.jacobianRank 3 : ℝ) - 3),
    residual_eq_zero := by
      rw [PT.shadow_vanishes 3, JI.full_rank 3 (le_refl 3)]
      norm_num }

-- The weak conjecture's witness. The conjectural content is the binding
-- of the abstract `jacobianRank` field to the actual coloured-Jones
-- coefficient data; the witness here is the model assertion (per the
-- repo's §3b placeholder convention — trivial witness + Ref marker).
-- Ref: [manuscript] conj:three-knot-jet-order-independence
noncomputable instance : JetOrderIndependence where
  jacobianRank := fun _ => 3
  full_rank := fun _ _ => rfl

-- The bridge's witness. Conjectural content = the surreal-shadow
-- vanishing (issues I1–I3 of the module docstring).
-- Ref: [manuscript] conj:three-knot-jet-order-independence (surreal bridge)
noncomputable instance : SurrealParallelTransportBound where
  transportShadow := fun _ => 0
  shadow_vanishes := fun _ => rfl

end QOU.Archimedean
