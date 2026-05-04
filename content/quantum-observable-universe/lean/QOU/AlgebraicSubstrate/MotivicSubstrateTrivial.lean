import QOU.AlgebraicSubstrate.MotivicSubstrate

/-!
# Trivial witness for `MotivicSubstrate`

A minimal `MotivicSubstrate ℤ ℤ trivialTarget` instance, where every
realisation target is just `ℤ` and every field is the obvious choice.
The instance witnesses **inhabitability** of the class — guarding
against accidental over-constraint — but is **not** the QOU substrate
at `q₀`.

The principal open item (GAP 6a in the
[2026-05-02 forward-derivation audit](../../../../../docs/audits/2026-05-02-forward-derivation-pre-archimedean.md))
is to produce a concrete `MotivicSubstrate` for the QOU motivic
substrate over `ℚ(q₀)`.  See
[2026-05-04 GAP 6a + 18a scoping](../../../../../docs/audits/2026-05-04-gap-6a-18a-scoping.md)
for the precise outstanding mathematical work.

Ref: [tate1967]
LaTeX label: scoping for `def:motivic-substrate`
-/

namespace QOU.AlgebraicSubstrate

/-- Constant-`ℤ` realisation target at every place. -/
def trivialTarget : Place → Type := fun _ => ℤ

instance instCommRingTrivialTarget : ∀ v, CommRing (trivialTarget v) :=
  fun _ => inferInstanceAs (CommRing ℤ)

/-- Trivial witness: every field is the obvious choice over `ℤ`.

    `lefschetz := 1` is conceptually wrong (the Lefschetz motive is
    `[𝔸¹]`, not `[Spec ℤ]`), but algebraically valid: `1` is a unit
    in `ℤ`, satisfying `lefschetz_invertible`.  Real instances must
    pick the actual class of `𝔸¹` in `K₀(Var_k)`. -/
-- Ref: [tate1967]
instance trivialMotivicSubstrate :
    MotivicSubstrate ℤ ℤ trivialTarget where
  lefschetz := 1
  inclusion := RingHom.id ℤ
  lefschetz_invertible := by
    show IsUnit ((RingHom.id ℤ) 1)
    simp
  realize := fun _ => RingHom.id ℤ
  archimedean_nontrivial := inferInstanceAs (Nontrivial ℤ)
  nonarchimedean_nontrivial :=
    ⟨⟨2, Nat.prime_two⟩, inferInstanceAs (Nontrivial ℤ)⟩

end QOU.AlgebraicSubstrate
