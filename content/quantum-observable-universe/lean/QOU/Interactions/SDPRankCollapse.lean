/-!
# QOU.Interactions.SDPRankCollapse — magic-shell rank-1 conjecture

The nuclear-confinement SDP at strand count `n` and substrate `q`
has optimal primal `T*(n, q)` (PSD matrix) and dual `u*(n, q)`
(shadow-price vector indexed by Wedderburn blocks). The conjecture
below asserts a **q-independent** structural-optimum predicate
that holds exactly on the magic ladder.

LaTeX label: `conj:sdp-rank-collapse-magic-shell`

## References

- [mathas1999] https://doi.org/10.1090/ulect/015
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [hoefsmit1974] — Hoefsmit, Representations of Hecke algebras
- [manuscript] particle-interactions / sdp-rank-collapse-magic-shell
-/

import QOU.LiftingDescent.HomologicalCondensation

namespace QOU.Interactions.SDPRankCollapse

open QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  SDP optimum surrogate -/

/-- Surrogate for `rank(T*(n, q)) = 1`. The actual SDP solver is
    not formalised here; we expose a `Prop`-valued predicate that
    captures "the SDP optimum at strand count `n` and substrate `q`
    is rank-1 with self-conjugate-block support." Concrete instances
    in future modules will tie this to a real linear-algebra rank
    computation. -/
opaque IsRankOneAtMagicShell (n : ℕ) (q : ℝ) : Prop

/-! ## §2  The rank-collapse conjecture -/

/-- **Conjecture (Proposition 5).**

    For generic `q > 1` (i.e., excluding a measure-zero set of
    root-of-unity-like specializations), the rank-1-at-magic-shell
    predicate `IsRankOneAtMagicShell n q` holds **iff** `n` lies on
    the magic ladder `{2, 8, 20, 28, 50, 82, 126}`.

    This is the q-independent partition-structural selection rule
    for the magic ladder, mediated by the SDP optimum's interaction
    with LR-fusion stability of self-conjugate Hecke modules. -/
-- Ref: [manuscript] conj:sdp-rank-collapse-magic-shell
class MagicShellRankConjecture where
  /-- Genericity: `q` is in the open interval `(1, ∞)` and not in
      a measure-zero set of accidental specializations. We expose
      the genericity condition as a typeclass field so the conjecture
      stays well-formed even for non-generic `q`. -/
  IsGeneric : ℝ → Prop
  /-- The defining iff. -/
  rank_one_iff_magic :
    ∀ (q : ℝ), IsGeneric q →
      ∀ (n : ℕ), IsRankOneAtMagicShell n q ↔ n ∈ magicLadder

/-- Re-export forward direction: at magic `n` and generic `q`, the
    SDP optimum is rank-1 with self-conjugate-block support. -/
-- Ref: [manuscript] conj:sdp-rank-collapse-magic-shell
theorem rank_one_at_magic
    [C : MagicShellRankConjecture]
    {n : ℕ} {q : ℝ}
    (hq : C.IsGeneric q) (hn : n ∈ magicLadder) :
    IsRankOneAtMagicShell n q :=
  (C.rank_one_iff_magic q hq n).mpr hn

/-- Re-export reverse direction: if the SDP optimum is rank-1 at
    `n` and generic `q`, then `n` lies on the magic ladder. -/
-- Ref: [manuscript] conj:sdp-rank-collapse-magic-shell
theorem magic_of_rank_one
    [C : MagicShellRankConjecture]
    {n : ℕ} {q : ℝ}
    (hq : C.IsGeneric q) (hr : IsRankOneAtMagicShell n q) :
    n ∈ magicLadder :=
  (C.rank_one_iff_magic q hq n).mp hr

end QOU.Interactions.SDPRankCollapse
