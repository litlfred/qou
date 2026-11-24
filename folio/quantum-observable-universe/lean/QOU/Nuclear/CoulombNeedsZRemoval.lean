import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# On nucleon blocks, the neutral exchange is Coulomb exactly when the `Z` part is removed

`NeutralExchangeSplit.neutralExchange_split` writes the unbroken neutral exchange
`g²·T₃T₃' + g'²·(Y/2)(Y'/2)` as a photon part `e²·QQ'` plus a `Z` part
`g_Z²·(T₃ − s²Q)(T₃' − s²Q')`. This file asks what is left when only a fraction `λ` of the
`Z` part survives (in the Standard Model `λ` is a Yukawa factor set by the `Z` mass and the
distance; nothing here fixes it):

    E_λ(T, T') = e²·Q Q' + λ·g_Z²·(T − s²Q)(T' − s²Q'),     Q = T + 1/2 (three-quark block, Y = 1).

On the four nucleon pairs (`T = ±1/2`) a Coulomb shape `c + κ·Q_A Q_B` means `pn = np = nn = c`
and `pp = c + κ`.

* `pn_eq_nn_iff_Z_removed`: if `g² ≠ 0` and `g² + g'² ≠ 0`, then `E_λ(p, n) = E_λ(n, n)` holds
  **iff `λ = 0`**. So no choice of mixing angle makes the `Z` part Coulomb-shaped; only its
  removal does.
* `coulombShape_iff_Z_removed`: the full statement, with `κ = e²` when `λ = 0`.
* `photon_coupling_eq_zero_iff`: `e² = 0` iff `g'² = 0` (given `g² ≠ 0`). Without the
  hypercharge coupling there is no Coulomb term at all.

So, at the level of charge factors, Coulomb between nucleon blocks needs two independent
inputs: the hypercharge coupling with its mixing angle `s² = g'²/(g² + g'²)`, and a mechanism
that removes the `Z` part (`λ = 0`). The identity holds over any field and fixes neither.
-/

namespace QOU.QBeta.CoulombNeedsZRemoval

variable {K : Type*} [Field K]

/-- Electric charge of a three-quark block (`Y = 1`) with isospin `T`. -/
def q (T : K) : K := T + 1 / 2

/-- Neutral exchange between two three-quark blocks with a surviving fraction `lam` of the
`Z` part: `e²·QQ' + lam·g_Z²·(T − s²Q)(T' − s²Q')`. -/
def exch (g2 gp2 lam T T' : K) : K :=
  (g2 * gp2 / (g2 + gp2)) * q T * q T' +
    lam * (g2 + gp2) * (T - gp2 / (g2 + gp2) * q T) * (T' - gp2 / (g2 + gp2) * q T')

/-- The neutron block (`T = −1/2`) has charge zero. -/
theorem q_neutron (h2 : (2 : K) ≠ 0) : q (-1 / 2 : K) = 0 := by
  unfold q; field_simp; ring

/-- The proton block (`T = 1/2`) has charge one. -/
theorem q_proton (h2 : (2 : K) ≠ 0) : q (1 / 2 : K) = 1 := by
  unfold q; field_simp; ring

/-- `pn` and `np` agree for every `lam`: the exchange is symmetric in the two blocks. -/
theorem pn_eq_np (g2 gp2 lam : K) :
    exch g2 gp2 lam (1 / 2) (-1 / 2) = exch g2 gp2 lam (-1 / 2) (1 / 2) := by
  unfold exch; ring

/-- `pn − nn = −lam·g²/2` (for `g² + g'² ≠ 0`). -/
theorem pn_sub_nn (g2 gp2 lam : K) (hs : g2 + gp2 ≠ 0) (h2 : (2 : K) ≠ 0) :
    exch g2 gp2 lam (1 / 2) (-1 / 2) - exch g2 gp2 lam (-1 / 2) (-1 / 2) = -(lam * g2 / 2) := by
  unfold exch q
  field_simp
  ring

/-- **The `Z` part is never Coulomb-shaped on nucleons.** With `g² ≠ 0`, the neutron–neutron
and proton–neutron values agree iff the surviving fraction of the `Z` part is zero. -/
theorem pn_eq_nn_iff_Z_removed (g2 gp2 lam : K) (hs : g2 + gp2 ≠ 0) (hg : g2 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    exch g2 gp2 lam (1 / 2) (-1 / 2) = exch g2 gp2 lam (-1 / 2) (-1 / 2) ↔ lam = 0 := by
  rw [← sub_eq_zero, pn_sub_nn g2 gp2 lam hs h2, neg_eq_zero, div_eq_zero_iff,
    mul_eq_zero]
  constructor
  · rintro ((h | h) | h)
    · exact h
    · exact absurd h hg
    · exact absurd h h2
  · intro h; exact Or.inl (Or.inl h)

/-- Coulomb shape on the four nucleon pairs: `pn = np = nn = c` and `pp = c + κ`. -/
def CoulombShape (E : K → K → K) (c κ : K) : Prop :=
  E (1 / 2) (1 / 2) = c + κ ∧ E (1 / 2) (-1 / 2) = c ∧ E (-1 / 2) (1 / 2) = c ∧
    E (-1 / 2) (-1 / 2) = c

/-- **Coulomb on nucleons iff the `Z` part is removed.** For `g² ≠ 0`, `g² + g'² ≠ 0`, the
exchange has a Coulomb shape for some `c, κ` iff `lam = 0`; then `c = 0` and `κ = e²`. -/
theorem coulombShape_iff_Z_removed (g2 gp2 lam : K) (hs : g2 + gp2 ≠ 0) (hg : g2 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    (∃ c κ, CoulombShape (exch g2 gp2 lam) c κ) ↔ lam = 0 := by
  constructor
  · rintro ⟨c, κ, -, hpn, -, hnn⟩
    exact (pn_eq_nn_iff_Z_removed g2 gp2 lam hs hg h2).1 (hpn.trans hnn.symm)
  · rintro rfl
    refine ⟨0, g2 * gp2 / (g2 + gp2), ?_, ?_, ?_, ?_⟩ <;>
      · unfold exch; simp only [q_proton h2, q_neutron h2]; ring

/-- With the `Z` part removed, the remaining coefficient is the photon coupling `e²`. -/
theorem coulomb_kappa_eq_e2 (g2 gp2 : K) (h2 : (2 : K) ≠ 0) :
    CoulombShape (exch g2 gp2 0) 0 (g2 * gp2 / (g2 + gp2)) := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    · unfold exch; simp only [q_proton h2, q_neutron h2]; ring

/-- **No hypercharge coupling, no Coulomb term.** For `g² ≠ 0` and `g² + g'² ≠ 0`, the photon
coupling `e² = g²g'²/(g² + g'²)` vanishes iff `g'² = 0`. -/
theorem photon_coupling_eq_zero_iff (g2 gp2 : K) (hs : g2 + gp2 ≠ 0) (hg : g2 ≠ 0) :
    g2 * gp2 / (g2 + gp2) = 0 ↔ gp2 = 0 := by
  rw [div_eq_zero_iff, mul_eq_zero]
  constructor
  · rintro ((h | h) | h)
    · exact absurd h hg
    · exact h
    · exact absurd h hs
  · intro h; exact Or.inl (Or.inr h)

end QOU.QBeta.CoulombNeedsZRemoval
