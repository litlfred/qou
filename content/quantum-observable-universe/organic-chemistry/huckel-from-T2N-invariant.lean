/-!
# QOU.Organic.HuckelFromT2NInvariant — Hückel 4n+2 from T(2,N)

Conjectural axiomatisation: the predicate "T(2,N) is aromatic by
component-count and Alexander-weight parity" coincides with
N ≡ 2 (mod 4), i.e. the Hückel 4n+2 rule.

The Lean class encodes the conjecture; the equivalence with
N ≡ 2 (mod 4) is proved as a downstream theorem conditional on
the class instance.

## References

- [manuscript] Ch. 10, Conjecture `conj:huckel-from-T2N-invariant`
- [manuscript] Ch. 10, Lemma `lem:T2N-components`
- [manuscript] Ch. 10, Lemma `lem:alexander-T2N-closed-form`
-/

namespace QOU.Organic

/-- The topological aromaticity predicate: N is even and N/2 is odd. -/
def topologicallyAromatic (N : ℕ) : Prop :=
  N % 2 = 0 ∧ (N / 2) % 2 = 1

/-- Conjectural class: a witness that the topological rule
    coincides with the Hückel 4n+2 rule for all N in a given range. -/
class HuckelFromT2NInvariant where
  agrees : ∀ N : ℕ, 2 ≤ N → N ≤ 14 →
    (topologicallyAromatic N ↔ N % 4 = 2)

/-- Sanity check: benzene (N = 6) is topologically aromatic. -/
-- Ref: [manuscript] Ch. 10, Conjecture conj:huckel-from-T2N-invariant
theorem benzene_topologically_aromatic : topologicallyAromatic 6 := by
  unfold topologicallyAromatic
  exact ⟨by decide, by decide⟩

/-- Sanity check: cyclobutadiene (N = 4) is NOT topologically aromatic
    (correctly: anti-aromatic). -/
-- Ref: [manuscript] Ch. 10, Conjecture conj:huckel-from-T2N-invariant
theorem cyclobutadiene_not_topologically_aromatic :
    ¬ topologicallyAromatic 4 := by
  unfold topologicallyAromatic
  intro ⟨_, h⟩
  exact absurd h (by decide)

/-- Sanity check: trefoil ring (N = 3) is NOT topologically aromatic
    (correctly: not even, fails component condition). -/
-- Ref: [manuscript] Ch. 10, Conjecture conj:huckel-from-T2N-invariant
theorem trefoil_not_topologically_aromatic :
    ¬ topologicallyAromatic 3 := by
  unfold topologicallyAromatic
  intro ⟨h, _⟩
  exact absurd h (by decide)

end QOU.Organic
