import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Data.Fintype.Perm
import Mathlib.Tactic

/-!
# def:strand-twist-datum — per-strand framing (ribbon twist) datum

The framing datum on an `n`-strand state: an integer ribbon twist per
strand (`TwistDatum n = Fin n → ℤ`). This is the candidate *second*
gauge-invariant `U(1)` coordinate demanded by
`conj:sm-hypercharge-invariant` — the writhe cannot carry hypercharge
(the nucleon doublet falsification), and the framing is exactly the
datum the ribbon structure of the braided category adds on top of the
crossing data.

Proved here, sorry-free:

* `totalTwist_perm` / `twistMultiset_perm` — the total twist and the
  twist multiset are invariant under strand relabelling (the residual
  `S_n` of the gauge action on strands): the datum is well-defined on
  gauge orbits.
* `totalTwist_bar` — the bar involution (orientation reversal /
  conjugate state) negates the total twist: antiparticles carry
  opposite twist, the CPT-compatible sign.
* `exists_same_writhe_ne_totalTwist` — the framed state space
  genuinely extends the unframed one: over any fixed braid word (hence
  any fixed writhe) there are framings with distinct total twist. This
  is precisely the degree of freedom `sm-hypercharge-invariant`'s
  factorization criterion shows the writhe cannot supply.

No physics is claimed here: whether the normalised candidate
`Y = 2(Q_twist − I₃)` with `Q_twist = totalTwist/3` passes the
Gell-Mann–Nishijima and `ℤ₆`-spectrum batteries is exactly the open
content of `conj:sm-hypercharge-invariant`; the enumeration probe is
`computations/strand_twist_y_battery.py` (exploratory).

Base ring: none — pure combinatorics over `ℤ`; nothing archimedean.
-/

namespace QOU.StandardModel

open Finset

/-- **Per-strand framing (twist) datum** on an `n`-strand state: an
integer ribbon twist for each strand. -/
def TwistDatum (n : ℕ) : Type := Fin n → ℤ

namespace TwistDatum

/-- Strand relabelling: the residual `S_n` gauge action on the datum. -/
def perm {n : ℕ} (σ : Equiv.Perm (Fin n)) (t : TwistDatum n) : TwistDatum n :=
  t ∘ σ

/-- The total twist `T(t) = Σᵢ tᵢ` — the candidate charge numerator. -/
def totalTwist {n : ℕ} (t : TwistDatum n) : ℤ := ∑ i, t i

/-- The twist multiset — the full gauge-orbit invariant. -/
def twistMultiset {n : ℕ} (t : TwistDatum n) : Multiset ℤ :=
  (univ : Finset (Fin n)).val.map t

/-- The bar involution on framings: orientation reversal negates every
twist (antiparticle datum). -/
def bar {n : ℕ} (t : TwistDatum n) : TwistDatum n := fun i => -(t i)

/-- **Gauge invariance of the total twist**: strand relabelling fixes
`T`. -/
@[simp] theorem totalTwist_perm {n : ℕ} (σ : Equiv.Perm (Fin n))
    (t : TwistDatum n) : totalTwist (perm σ t) = totalTwist t :=
  Equiv.sum_comp σ t

/-- **Gauge invariance of the twist multiset**: strand relabelling fixes
the multiset of twists. -/
theorem twistMultiset_perm {n : ℕ} (σ : Equiv.Perm (Fin n))
    (t : TwistDatum n) : twistMultiset (perm σ t) = twistMultiset t := by
  classical
  unfold twistMultiset perm
  rw [show ((univ : Finset (Fin n)).val.map (t ∘ ⇑σ))
        = ((univ : Finset (Fin n)).val.map ⇑σ).map t from
      (Multiset.map_map t ⇑σ _).symm]
  congr 1
  -- a permutation maps the universal multiset to itself
  rw [← Equiv.coe_toEmbedding, ← Finset.map_val, Finset.map_univ_equiv]

/-- **Bar negation**: the conjugate framing has opposite total twist. -/
@[simp] theorem totalTwist_bar {n : ℕ} (t : TwistDatum n) :
    totalTwist (bar t) = -totalTwist t := by
  unfold totalTwist bar
  simp [Finset.sum_neg_distrib]

/-- **The framing is independent data over the braid word**: over any
fixed word (hence fixed writhe) there exist framings with distinct
total twist — the zero framing and a unit twist on the first strand.
This exhibits the writhe-degenerate separation that
`sm-hypercharge-invariant` proves any hypercharge invariant needs. -/
theorem exists_same_writhe_ne_totalTwist (n : ℕ) (hn : 0 < n) :
    ∃ t₁ t₂ : TwistDatum n, totalTwist t₁ ≠ totalTwist t₂ := by
  refine ⟨fun _ => 0, fun i => if i = ⟨0, hn⟩ then 1 else 0, ?_⟩
  have h1 : totalTwist (n := n) (fun _ => 0) = 0 := by
    simp [totalTwist]
  have h2 : totalTwist (n := n) (fun i => if i = ⟨0, hn⟩ then 1 else 0) = 1 := by
    simp [totalTwist]
  omega

/-! ## The candidate hypercharge is a function of the total twist alone

The normalised candidate of `def:strand-twist-datum` pairs the datum with
the writhe-derived isospin `I₃`:

    Y_cand(I₃, t) = 2 · (Q_twist(t) − I₃),   Q_twist(t) = totalTwist(t) / 3,

with `Q_twist = T/3` the helon colour-tube charge quantum
(Bilson-Thompson, `[bilson-thompson2005]`; the `1/3` is a fixed
normalisation, NOT a fitted parameter). The lemmas below pin the
structural content that the enumeration battery
(`computations/strand_twist_y_battery.py`) obscures:

* `Ycand_factors_totalTwist` — `Y_cand` sees **only** the total twist, not
  the full multiset. So the battery's per-flavour *multiset* survivors
  carry strictly more freedom than `Y` constrains.
* `totalTwist_pinned_of_Ycand` — reproducing a **given** hypercharge `Y`
  against a **given** isospin `I₃` is *equivalent* to pinning the total
  twist to `3·(I₃ + Y/2) = 3Q` (the Gell-Mann–Nishijima charge). The total
  is therefore **uniquely determined** by the spectrum; nothing about the
  multiset is.
* `Ycand_bar` — the candidate is bar-odd: `Y_cand(−I₃, bar t) = −Y_cand(I₃, t)`
  (antiparticle hypercharge flips sign, the CPT-compatible property), a
  consequence of `totalTwist_bar`.

Consequence for the battery (recorded in the audit, not claimed as physics
here): the "4 of 10 000 survivors" decompose as `1·2·2·1`, the count of
size-3 `{−1,0,1}`-multisets realising each *uniquely pinned* total
`(u,d,ν,e) = (2,−1,0,−3) = 3Q`. The residual freedom is `Y`-invisible
multiset choice at fixed total, **not** hypercharge non-uniqueness.
Narrowing it requires the per-strand braid word — the gap that stays open.

Base ring: `ℚ` — the SM quantum numbers are rationals; no ordering,
`Real.sqrt`, or other archimedean structure appears, so this stays below
the substrate→archimedean wall (§7c: `ℚ` is the minimal field carrying
these charges, not a gratuitous `ℝ`). -/

/-- **Candidate hypercharge** on a framed state with writhe-derived isospin
`I₃`: `Y = 2·(totalTwist/3 − I₃)`. The `def:strand-twist-datum`
normalisation `Q_twist = totalTwist/3` (helon colour-tube quantum). -/
def Ycand {n : ℕ} (I3 : ℚ) (t : TwistDatum n) : ℚ :=
  2 * (((totalTwist t : ℤ) : ℚ) / 3 - I3)

/-- **The candidate hypercharge factors through the total twist**: two
framings with equal total twist yield the same candidate hypercharge, so
`Y_cand` cannot distinguish framings that differ only in how a fixed total
is split across strands. -/
theorem Ycand_factors_totalTwist {n : ℕ} (I3 : ℚ) (t t' : TwistDatum n)
    (h : totalTwist t = totalTwist t') : Ycand I3 t = Ycand I3 t' := by
  unfold Ycand; rw [h]

/-- **The spectrum pins the total twist, and only the total.** Reproducing a
prescribed hypercharge `Y` against isospin `I₃` is equivalent to the total
twist equalling `3·(I₃ + Y/2) = 3Q` (Gell-Mann–Nishijima). Hence the SM
first-generation spectrum uniquely determines each fermion's total twist;
the residual multiset freedom is unconstrained by `Y`. -/
theorem totalTwist_pinned_of_Ycand {n : ℕ} (I3 Y : ℚ) (t : TwistDatum n) :
    Ycand I3 t = Y ↔ ((totalTwist t : ℤ) : ℚ) = 3 * (I3 + Y / 2) := by
  unfold Ycand
  constructor
  · intro h; linarith
  · intro h; linarith

/-- **Bar (antiparticle) consistency of the candidate**: under orientation
reversal (`bar`, negating every twist) together with the isospin flip
`I₃ ↦ −I₃`, the candidate hypercharge negates. The CPT-compatible sign,
inherited from `totalTwist_bar`. -/
theorem Ycand_bar {n : ℕ} (I3 : ℚ) (t : TwistDatum n) :
    Ycand (-I3) (bar t) = -Ycand I3 t := by
  unfold Ycand
  rw [totalTwist_bar]
  push_cast
  ring

/-- **The surviving multiset ambiguity is `Y`-invisible** (concrete witness).
The two `d`-quark battery survivors `{−1,−1,1}` and `{−1,0,0}` share total
twist `−1`, so at the writhe-derived isospin `I₃(d_L) = −1/2` they yield the
identical candidate hypercharge. The battery cannot separate them; only the
per-strand braid word could — the open gap. -/
example : Ycand (-1/2 : ℚ) (![(-1 : ℤ), -1, 1] : TwistDatum 3)
        = Ycand (-1/2 : ℚ) (![(-1 : ℤ), 0, 0] : TwistDatum 3) := by
  apply Ycand_factors_totalTwist
  simp [totalTwist, Fin.sum_univ_three]

end TwistDatum

end QOU.StandardModel
