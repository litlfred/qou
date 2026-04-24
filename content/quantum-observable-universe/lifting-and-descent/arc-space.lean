-- Ref: [denef-loeser2001] Denef, Loeser, Geometry on Arc Spaces of Algebraic Varieties.
--   European Congress of Mathematics, Vol. I (Barcelona, 2000), 327-348.
-- Arc space L(X) of a variety X, identified with the recursive brane tower.

namespace QOU.LiftingDescent

/-- The **n-th jet scheme** L_n(X) of a variety X.

    L_n(X) represents the functor R ↦ Hom(Spec R[t]/(t^{n+1}), X).
    In QOU it is identified with the n-th level of the recursive
    brane tower S_n: a section v of S_n is an R-point of L_n(X). -/
structure JetScheme (X : Type*) (n : Nat) where
  /-- Underlying scheme of the n-th jet space. -/
  Carrier : Type*
  /-- The truncation map L_{n+1}(X) → L_n(X). -/
  truncation : Carrier → Carrier

/-- The **arc space** L(X) of a variety X.

    L(X) = lim_{←n} L_n(X) is the inverse limit of the jet schemes.
    In QOU it equals the inverse limit of the recursive brane tower
    S_∞ := lim_n S_n, and carries the formal data needed for
    motivic integration even when the underlying X is singular. -/
structure ArcSpace (X : Type*) where
  /-- The carrier of the arc space (inverse limit of jet schemes). -/
  Carrier : Type*
  /-- Projection to each finite jet level. -/
  projection : (n : Nat) → Carrier → (JetScheme X n).Carrier
  /-- Compatibility: projection at n+1 followed by truncation = projection at n. -/
  compatible : ∀ n a, (JetScheme X n).truncation
                        ((JetScheme X (n+1)).truncation
                          ((projection (n+1) a)) ) =
                      (JetScheme X n).truncation (projection n a)

end QOU.LiftingDescent
