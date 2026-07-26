import Mathlib.Algebra.Lie.Rank
import Mathlib.Algebra.Lie.Classical
import Mathlib.Tactic

/-!
# Atomicity — the Lie-algebra-rank route to the upper bound (`qou-atsd`, T3-lie)

The atomicity upper bound needs `rank G ≤ 1` for the Tannaka dual `G` — the piece
the elementary matrix route (`AtomicityFromSelfDuality.lean`) could not close,
because algebraic-**group** rank is not in Mathlib. But `rank G = rank Lie(G)`, and
Mathlib **does** have Lie-algebra rank (`LieAlgebra.rank`) together with the
specific-element upper bound

  `rank R L ≤ (ad R L x).charpoly.natTrailingDegree`   (`rank_le_natTrailingDegree_charpoly_ad`).

So the residual reframes to a **Mathlib-reachable** statement: for `Lie(SL₂) = 𝔰𝔩₂`
with the regular diagonal `h = diag(1,−1)`, `ad h` has characteristic polynomial
`X³ − 4X` (eigenvalues `0, 2, −2` on the basis `h, e, f`), whose trailing degree is
`1` — giving `rank 𝔰𝔩₂ ≤ 1`, the atomicity upper bound.

This file lands the **frame** (`rank_le_one_of_ad_charpoly_trailing`): the general
reduction from a trailing-degree-≤1 witness to `rank ≤ 1`. The concrete `𝔰𝔩₂`
charpoly computation `natTrailingDegree (charpoly (ad h)) = 1` — the genuine
remaining core — is bean `qou-atsd-t3-lie`.

-- Ref: [manuscript] conj:binding-manybody-eq-jet-filtration (atomicity); def:tannaka-dual
-/

namespace QOU.Atomicity

open LieAlgebra

/-- **Lie-rank route to the atomicity upper bound (frame).** If a Lie algebra `L`
    over `R` carries an element `x` whose `ad`-characteristic polynomial has
    trailing degree `≤ 1`, then `rank R L ≤ 1`. Immediate from Mathlib's
    specific-element rank bound `rank_le_natTrailingDegree_charpoly_ad`.

    This is the closeable reframing of the atomicity residual: with `rank G =
    rank Lie(G)` it replaces the (Mathlib-absent) algebraic-group root count by a
    Lie-algebra charpoly computation. Applied to `𝔰𝔩₂` and the regular diagonal
    `h` (whose `ad h` charpoly is `X³ − 4X`, trailing degree 1) it yields
    `rank 𝔰𝔩₂ ≤ 1` — the atomicity upper bound. The concrete `𝔰𝔩₂` computation is
    the remaining core (bean `qou-atsd-t3-lie`); no instance is fabricated here. -/
theorem rank_le_one_of_ad_charpoly_trailing
    {R L : Type*} [CommRing R] [Nontrivial R] [LieRing L] [LieAlgebra R L]
    [Module.Finite R L] [Module.Free R L] (x : L)
    (hx : (ad R L x).charpoly.natTrailingDegree ≤ 1) :
    rank R L ≤ 1 :=
  (rank_le_natTrailingDegree_charpoly_ad R x).trans hx

end QOU.Atomicity
