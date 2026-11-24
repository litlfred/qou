/-
# Habiro rigidity of the fibre residue 𝔴_λ — "rigidity ⇒ no fit", as a §3b class

**This file REFRAMES the fibre→observable residue as an algebro-geometric rigidity question; it does
NOT prove Habiro's injectivity theorem and does NOT close the geometric `W_λ` gate** (AGENTS.md
§"Axiomatization is NOT a Proof"). Habiro's theorem is carried as the **class hypothesis**
(`root_injective`), not proved.

Context (audit `2026-07-12-fibre-observable-categorical-not-analytic.md` §5 + §"correct statement of
the residue"): a `z`-Habiro-ring element is **determined by its root-of-unity values** (Habiro's
injectivity miracle: the evaluation map to the product over all roots of unity is injective). The
surviving residue of the de-opaqued gate `bwS0_eq_hecke` (#3677) pins `W_λ(q₀)` to the archimedean
functor `τ_∞` (the `q₀`-evaluation algebra map) applied to a Habiro element `𝔴_λ` whose
**root-of-unity values are the colored-WRT amplitudes** `bwS0Concrete`. By Habiro rigidity `𝔴_λ` —
hence its `q₀` value — is **uniquely determined** by that fibre data: **no fit is possible in
principle**, the answer is forced, not tuned. This is the "rigidity ⇒ no fit" content.

* `HabiroRigidity H RootIndex` — a §3b class over an abstract Habiro-like element type `H` with a
  root-of-unity evaluation `evalRoot : RootIndex → H → ℂ` and an archimedean `q₀`-value
  `evalQ0 : H → ℝ` (the `τ_∞` value). The content field is **`root_injective`**: an element is
  determined by its root-of-unity values (the Habiro injectivity **hypothesis**).
* `q0_value_unique` — the conditional uniqueness theorem **derived** sorry-free from the class:
  two elements with the same root-of-unity values have the same `q₀` value. This is precisely
  "the fibre data forces the observable value; a fit is structurally impossible."
* the instance over `H = ℂ`, `RootIndex = Unit`, `evalRoot _ = id`, `evalQ0 = Complex.re`
  witnesses the **shape** is inhabited by a genuinely-injective evaluation — it is the shape-witness;
  the real Habiro ring `ℤ[q]^` and the actual WRT element `𝔴_λ` are the open objects (owner-gated
  geometric `W_λ` index), not modeled here.

What is **NOT** proved: Habiro's injectivity for the actual `z`-Habiro ring, and the identification
of `𝔴_λ` with the `S³/2I` WRT element. Both remain open; this file states the rigidity as a
hypothesis and derives its "no-fit" consequence.

Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-12-fibre-observable-categorical-not-analytic.md
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot.Keystone

/-- **Habiro rigidity (§3b class).** An abstract Habiro-like element type `H` equipped with a
root-of-unity evaluation `evalRoot ζ : H → ℂ` (value at each root of unity `ζ`, indexed by
`RootIndex`) and an archimedean `q₀`-value `evalQ0 : H → ℝ` (the `τ_∞` evaluation post-fibre-functor).
The content is **`root_injective`**: an element of `H` is **determined by its root-of-unity values**
— Habiro's injectivity miracle, carried here as the class **hypothesis** (not proved). Any instance
supplies this rigidity; the actual `z`-Habiro ring realizing it is the open object. -/
class HabiroRigidity (H : Type*) (RootIndex : Type*) where
  /-- Root-of-unity evaluation: value of a Habiro element at the root of unity indexed by `ζ`. -/
  evalRoot : RootIndex → H → ℂ
  /-- Archimedean `q₀`-value (`τ_∞` evaluation) of a Habiro element. -/
  evalQ0 : H → ℝ
  /-- **Content — Habiro injectivity (hypothesis).** A Habiro element is determined by its
  root-of-unity values: if `a` and `b` agree at every root of unity, then `a = b`. -/
  root_injective : ∀ a b : H, (∀ ζ : RootIndex, evalRoot ζ a = evalRoot ζ b) → a = b

/-- **Rigidity ⇒ no fit — conditional uniqueness, derived sorry-free from the class.** If two Habiro
elements `w w'` have the **same root-of-unity values** (both realize the colored-WRT fibre data
`bwS0Concrete`), then they have the **same archimedean `q₀` value** `τ_∞`. The fibre data forces the
observable value; it cannot be tuned. Fully verified **modulo the class instance** — the instance
for the actual `z`-Habiro ring (Habiro's theorem) is the open input, not proved here. -/
theorem q0_value_unique {H RootIndex : Type*} [HabiroRigidity H RootIndex]
    (w w' : H) (h : ∀ ζ : RootIndex, HabiroRigidity.evalRoot ζ w = HabiroRigidity.evalRoot ζ w') :
    (HabiroRigidity.evalQ0 (RootIndex := RootIndex) w)
      = HabiroRigidity.evalQ0 (RootIndex := RootIndex) w' := by
  have hww : w = w' := HabiroRigidity.root_injective (RootIndex := RootIndex) w w' h
  rw [hww]

/-- **The class is non-vacuous (shape-witness).** `H = ℂ`, one root of unity (`RootIndex = Unit`),
`evalRoot` the identity and `evalQ0 = Re`: the identity evaluation is genuinely injective, so
`root_injective` holds with real content. This witnesses the rigidity shape is inhabited by an
honestly-injective evaluation; it does **not** model the actual `z`-Habiro ring (the open object). -/
instance : HabiroRigidity ℂ Unit where
  evalRoot := fun _ => id
  evalQ0 := Complex.re
  root_injective := by
    intro a b h
    simpa using h ()

end QOU.BraidKnot.Keystone
