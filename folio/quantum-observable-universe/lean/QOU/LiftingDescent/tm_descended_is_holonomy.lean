import Mathlib.Tactic

/-!
# QOU.LiftingDescent.tm_descended_is_holonomy

**Lemma** ([`lem:topological-mass-holonomy`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-holonomy.md)).

*Under the topological blow-up decomposition
`Σ = Σ₀ ∪ ⋃_{i=1}^N D_i`, where `Σ₀` is a disc spanning the unknot core
`ϱ₀` and each `D_i` is the exceptional disc at the `i`-th blow-up, the
descended term equals the unknot-core holonomy:*

    MI∫_Σ τ̂ₙ(α) = Hol_{∇A}(ϱ₀; 𝔊).

## Structure (hypotheses vs. derivation)

Everything is a **parameter**; nothing is a named constant.  The
multiplicative integral takes values in an arbitrary (not necessarily
commutative) monoid `G` — the structure group in which holonomies live —
so the blow-up product is an *ordered* `List.prod`.  Surfaces and
integrands are arbitrary types, and the multiplicative integral is an
arbitrary map `MI : Form → Surf → G`.

The descended term is modelled as what the proof block says it is: a
level-`n` section `β` pulled back along the blow-down,
`τ̂ₙ(α) = pullback β` (the ascent embedding `ℓₙ`).  The hypotheses are
the standard properties of the multiplicative integral the proof uses,
each strictly more primitive than the conclusion:

1. `hfact` — multiplicativity over the blow-up decomposition (Yekutieli):
   `MI∫_Σ = MI∫_{Σ₀} · Π_i MI∫_{D_i}` (ordered product).
2. `hnat` — naturality under the blow-down on the exceptional discs:
   `MI∫_{D_i} (pullback β) = MI∫_{blowdown D_i} β`.
3. `hcollapse` — each exceptional disc collapses to a point under the
   blow-down: `blowdown D_i = pt`.
4. `hpt` — the multiplicative integral over a degenerate (point) surface
   is the identity.
5. `hstokes` — non-abelian Stokes on the spanning disc:
   `MI∫_{Σ₀} (pullback β) = Hol_{∇A}(ϱ₀; 𝔊)`.

**Derived**: (2)+(3)+(4) give that every exceptional-disc contribution is
`1` (`descended_exceptional_disc_trivial`, formerly an assumed class
field); (1) then collapses the ordered product and (5) closes.

An earlier revision modelled the five quantities as `opaque` reals and
assumed disc triviality directly as a `Prop`-class field; one earlier
still *defined* `descendedMIdisc := 1`, collapsing the lemma to `rfl`.
Bean `tmvac`.
-/

namespace QOU.LiftingDescent

variable {G Surf Form : Type*} [Monoid G]

/-- **Exceptional discs contribute trivially (derived).**  A pulled-back
(descended) integrand has trivial multiplicative integral over every
exceptional disc: naturality moves the integral to the blow-down image,
which is a point, where the multiplicative integral is the identity. -/
theorem descended_exceptional_disc_trivial
    (MI : Form → Surf → G) (pullback : Form → Form) (blowdown : Surf → Surf)
    (pt : Surf) (D : ℕ → Surf) (β : Form)
    (hnat : ∀ i, MI (pullback β) (D i) = MI β (blowdown (D i)))
    (hcollapse : ∀ i, blowdown (D i) = pt)
    (hpt : ∀ ω, MI ω pt = 1) :
    ∀ i, MI (pullback β) (D i) = 1 := by
  intro i
  rw [hnat, hcollapse, hpt]

/-- **Descended term = unknot-core holonomy**
    ([`lem:topological-mass-holonomy`]).

`MI∫_Σ τ̂ₙ(α) = Hol_{∇A}(ϱ₀; 𝔊)` with `τ̂ₙ(α) = pullback β`.  *Derived*
(not assumed): factorise over the blow-up decomposition, show each
exceptional-disc factor is trivial from naturality and collapse, collapse
the ordered product, then apply Stokes on the spanning disc. -/
theorem tm_descended_is_holonomy
    (MI : Form → Surf → G) (pullback : Form → Form) (blowdown : Surf → Surf)
    (pt Sig Sig0 : Surf) (D : ℕ → Surf) (N : ℕ) (β : Form) (hol : G)
    (hfact : MI (pullback β) Sig
      = MI (pullback β) Sig0 * ((List.range N).map fun i => MI (pullback β) (D i)).prod)
    (hnat : ∀ i, MI (pullback β) (D i) = MI β (blowdown (D i)))
    (hcollapse : ∀ i, blowdown (D i) = pt)
    (hpt : ∀ ω, MI ω pt = 1)
    (hstokes : MI (pullback β) Sig0 = hol) :
    MI (pullback β) Sig = hol := by
  have htriv := descended_exceptional_disc_trivial MI pullback blowdown pt D β
    hnat hcollapse hpt
  have hprod : ((List.range N).map fun i => MI (pullback β) (D i)).prod = 1 := by
    simp [htriv]
  rw [hfact, hprod, mul_one, hstokes]

end QOU.LiftingDescent
