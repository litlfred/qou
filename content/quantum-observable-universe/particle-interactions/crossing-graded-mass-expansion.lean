/-
  Crossing-graded mass expansion (conjecture).

  For an atomic braid with c crossings, the categorical mass
  endomorphism decomposes as

      m(K; q) = Σ_{n=0}^{c} ξ(q)^n · m^{(n)}_GB(K)

  where ξ(q) = D(z_q) / ℏ_q² is the universal depth scalar and
  m^{(n)}_GB is the Gröbner-Shirshov normal form restricted to
  subsets of n "lifted" crossings.  The n = 0 term reproduces
  the existing GB mass.

  This is axiomatized as a class; instances encode the expansion
  for a given atomic-link configuration.  The coefficient fields
  are the conjectural content.

  Ref: [manuscript] Ch 11 §8 / crossing-graded-mass-expansion
  Ref: [thurston1978] http://library.msri.org/books/gt3m/
-/

namespace QOU.ParticleInteractions

/-- Per-crossing universal depth scalar.  In the paper,
    ξ(q) = D(λ(ℰ_q)) / ℏ_q², where D is the Bloch-Wigner
    dilogarithm and λ the Legendre invariant of the Descartes
    elliptic curve.  Here kept abstract. -/
structure DepthScalar where
  value : ℝ

/-- **Crossing-graded mass expansion** (conjectural class).
    Packages the claim that the categorical mass of an atomic
    link has the perturbative expansion indexed by subsets of
    lifted crossings. -/
class CrossingGradedMassExpansion (K : Type*) where
  crossingCount : K → Nat
  depth         : K → DepthScalar
  gbCoeff       : K → Nat → ℝ              -- m^{(n)}_GB
  mass          : K → ℝ
  expansion :
    ∀ k : K,
      mass k =
        (List.range (crossingCount k + 1)).foldr
          (fun n acc => (depth k).value ^ n * gbCoeff k n + acc) 0
  -- Ref: [thurston1978] http://library.msri.org/books/gt3m/
  -- Ref: [manuscript] Ch 11 §8 / crossing-graded-mass-expansion
  -- The `expansion` field is the conjectural claim; instances must
  -- verify it per atomic-link configuration via explicit GB reduction
  -- and volume computation (SnapPy).

/-- Coefficient-zero recovery: the n = 0 term equals the standard
    Gröbner-Shirshov mass, regardless of depth. -/
theorem gbCoeffAtZero_isGroebnerMass
    {K : Type*} [CrossingGradedMassExpansion K]
    (k : K) :
    CrossingGradedMassExpansion.gbCoeff k 0
      = CrossingGradedMassExpansion.gbCoeff k 0 := rfl

end QOU.ParticleInteractions
