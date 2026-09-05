/-
# The Wedderburn embedding, with no hypothesis left

`QOU/HeckeAlgebra/WedderburnConstruction.lean` (bean `qou-usol`) built the
block-diagonal assembly and was careful to isolate the one thing it could not
supply: the Robinson–Schensted–Knuth dimension identity `Σ_λ (f^λ)² = n!`,
carried as the explicit hypothesis `RSKDimIdentity n` on the map into
`Fin (heckeDim n)`. Its docstring said the identity "is available only
conditionally", citing `scripts/lean-axiom-guard.py`'s warning that the corpus's
`OVTopAssembly.sum_numSYT_sq_eq_factorial` reached `clean` "by moving its
obligation into a class binder".

**That cited the wrong declaration.** The corpus carries a second, independent
route — `QOU/Mathlib/SchenstedRSKBurnside.lean:56`:

    theorem rskBurnsideHolds (n : ℕ) : RSKBurnsideHolds n

universally quantified, proved from `Schensted.rskEquiv` over a ~48-module
in-repo Schensted development. Measured 2026-09-05 (bean `qou-yos9`), after
building that cone (46 ok, 2 up-to-date, 0 errors):

    'QOU.Mathlib.rskBurnsideHolds'        [propext, Classical.choice, Quot.sound]
    'QOU.Mathlib.card_pairs_eq_sum'       [propext, Classical.choice, Quot.sound]
    'QOU.Mathlib.Schensted.rskEquiv'      [propext, Classical.choice, Quot.sound]

No `sorryAx`, no class binder. And the two statements are *definitionally* the
same — `seminormalDim = QOU.Mathlib.dimSYT` (`Hoefsmit.lean`) and
`heckeDim n = n.factorial` (`Common.lean`), both by definition — so
`rskDimIdentity` below is the Schensted theorem applied, nothing more.

The result is that the embedding is now **unconditional and injective, with no
axiom and no hypothesis at all**. That is the end of the line this arc opened
with `opaque wedderburnEmbed`: axiom (`qou-qb7p`) → construction with one named
hypothesis (`qou-usol`) → opaque deleted (`qou-kp2z`) → hypothesis discharged
(here).

## On the name

This deliberately does **not** reclaim the name `wedderburnEmbed`.
`computations/qbeta/qbeta_wedderburn_bridge_probe.py` guards that no reference
to the retired opaque survives, and a new declaration sharing its name would
trip that guard on good news. Keeping the guard sharp is worth more than
reclaiming a name, so the total map is `wedderburnEmbedTotal`.

## What this does *not* do

It does not touch the shape objection. `wedderburnEmbedTotal` has the same type
as before — blocks in, one matrix out — so the `(2,1)` clause of
`unified-iterative-correction-proof.md` is exactly as open as
`QOU/HeckeAlgebra/WedderburnTrace.lean` leaves it. Discharging a hypothesis
changed what the map *rests on*, not what it *does*.
-/
import QOU.HeckeAlgebra.WedderburnConstruction
import QOU.Mathlib.SchenstedRSKBurnside

namespace QOU.HeckeAlgebra.Wedderburn

open QOU.HeckeAlgebra QOU.HeckeAlgebra.Hoefsmit

/-- **The RSK dimension identity, discharged.** `RSKDimIdentity n` unfolds to
`QOU.Mathlib.RSKBurnsideHolds n`, which `rskBurnsideHolds` proves for every `n`. -/
theorem rskDimIdentity (n : ℕ) : RSKDimIdentity n :=
  QOU.Mathlib.rskBurnsideHolds n

/-- **The Wedderburn embedding with no hypothesis.** -/
noncomputable def wedderburnEmbedTotal {n : ℕ} (x : WedderburnDecomposition n) :
    Matrix (Fin (heckeDim n)) (Fin (heckeDim n)) ℝ :=
  wedderburnEmbedOf (rskDimIdentity n) x

/-- It agrees with the conditional form, for any proof of the identity —
proof irrelevance, recorded so a caller holding its own `RSKDimIdentity` term
need not wonder whether the two maps differ. -/
theorem wedderburnEmbedTotal_eq {n : ℕ} (h : RSKDimIdentity n)
    (x : WedderburnDecomposition n) :
    wedderburnEmbedTotal x = wedderburnEmbedOf h x := by
  unfold wedderburnEmbedTotal
  congr 1

/-- **Injective, unconditionally.** Positivity of `seminormalDim` is discharged
here rather than passed in — `seminormalDim_pos'` proves it outright, so nothing
is left for a caller to supply. -/
theorem wedderburnEmbedTotal_injective {n : ℕ} :
    Function.Injective (wedderburnEmbedTotal (n := n)) :=
  wedderburnEmbedOf_injective (rskDimIdentity n) (fun lam => seminormalDim_pos' lam)

end QOU.HeckeAlgebra.Wedderburn
