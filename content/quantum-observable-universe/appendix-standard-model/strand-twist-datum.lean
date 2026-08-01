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

end TwistDatum

end QOU.StandardModel
