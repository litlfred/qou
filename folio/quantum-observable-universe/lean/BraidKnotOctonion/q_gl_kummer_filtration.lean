import Mathlib.Data.Real.Basic

/-!
# QOU.QGeometricLanglands.q_gl_kummer_filtration — conjecture carrier (content-bearing, no instance)

**§3b-cond class axiomatisation** for content block
[`conj:q-gl-kummer-filtration`](../../../quantum-observable-universe/q-geometric-langlands/q-gl-kummer-filtration.md):
*Kummer-tower filtration of the moduli of $q$-local systems.*

This is a **conjecture**, and the honest open state is a **content-bearing class
with no instance** (AGENTS.md §3b-tax). `q_gl_kummer_filtration` carries the
conjecture's actual content as the `level1_all` and `lifts_iff_divides` fields.
**No instance is provided anywhere in this file.** Downstream theorems take
`[q_gl_kummer_filtration]` as an explicit hypothesis.

The moduli of $q$-local systems is abstracted as a class parameter; the
two substantive claims encoded are (1) the level-1 sublocus is
everything, and (3) the level-$n$ sublocus lifts through the brane tower
iff $n \mid \chi(A)$.
-/

namespace QOU.QGeometricLanglands

/-- **Kummer-tower filtration of $\mathrm{LocSys}_{\check G_q}(X)$.**

    Conjectural class — see
    [`conj:q-gl-kummer-filtration`](../../../quantum-observable-universe/q-geometric-langlands/q-gl-kummer-filtration.md). -/
class q_gl_kummer_filtration where
  /-- Moduli of $q$-local systems $\mathrm{LocSys}_{\check G_q}(X)$. -/
  LocSys : Type
  /-- Membership in the level-$n$ sublocus
      $\mathrm{LocSys}^{(n)} \subseteq \mathrm{LocSys}$ ($n$-divisible
      $q$-monodromy). -/
  inLevel : ℕ → LocSys → Prop
  /-- Whether the level-$n$ sublocus admits lifts through the brane tower. -/
  liftsThroughTower : ℕ → Prop
  /-- The Euler characteristic $\chi(A)$ governing the lifting obstruction. -/
  chiA : ℤ
  /-- **Conjecture, part 1**: the level-1 sublocus is all $q$-local systems. -/
  level1_all : ∀ L : LocSys, inLevel 1 L
  /-- **Conjecture, part 3**: the level-$n$ sublocus lifts through the
      brane tower iff $n \mid \chi(A)$ (perpetual obstruction otherwise). -/
  lifts_iff_divides : ∀ n : ℕ, 1 ≤ n → (liftsThroughTower n ↔ (n : ℤ) ∣ chiA)

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  An instance would have to supply the class fields above, which
-- is exactly the open conjecture; supplying one asserts it.
--
-- History: this file previously carried
--     axiom q_gl_kummer_filtration_conjecture : q_gl_kummer_filtration
--     noncomputable instance : q_gl_kummer_filtration := q_gl_kummer_filtration_conjecture
-- so every downstream `[q_gl_kummer_filtration]` resolved for free and the assumption was
-- invisible outside `#print axioms`.  (The removed comment also described it
-- as a `sorry` representing the open conjecture — it was an `axiom`, which is
-- strictly stronger: a `sorry` at least shows up as `sorryAx`.)  Removed, not
-- completed.  Downstream results must take `[q_gl_kummer_filtration]` as an explicit
-- hypothesis.

namespace q_gl_kummer_filtration

/-- **The level-1 sublocus always lifts through the brane tower**, since
    $(1 : \mathbb{Z}) \mid \chi(A)$ unconditionally. -/
theorem liftsThroughTower_one [c : q_gl_kummer_filtration] :
    c.liftsThroughTower 1 := by
  rw [c.lifts_iff_divides 1 le_rfl]
  exact one_dvd c.chiA

/-- **Perpetual brane-tower lifting obstruction** when $n \nmid \chi(A)$:
    for any level $n \ge 1$ whose integer cast does not divide $\chi(A)$,
    the level-$n$ sublocus cannot lift through the brane tower. -/
theorem not_liftsThroughTower_of_not_dvd [c : q_gl_kummer_filtration]
    (n : ℕ) (hn : 1 ≤ n) (hndvd : ¬ ((n : ℤ) ∣ c.chiA)) :
    ¬ c.liftsThroughTower n := by
  rw [c.lifts_iff_divides n hn]
  exact hndvd

/-- **Brane-tower descent along divisibility**: if $1 \le m$, $1 \le n$,
    $m \mid n$, and the level-$n$ sublocus lifts through the brane tower,
    then the intermediate level-$m$ sublocus also lifts through the tower. -/
theorem liftsThroughTower_of_dvd_trans [c : q_gl_kummer_filtration]
    (m n : ℕ) (hm : 1 ≤ m) (hn : 1 ≤ n) (hmn : m ∣ n)
    (hlift : c.liftsThroughTower n) :
    c.liftsThroughTower m := by
  rw [c.lifts_iff_divides m hm]
  have hndvd : (n : ℤ) ∣ c.chiA := (c.lifts_iff_divides n hn).mp hlift
  have hmn_int : (m : ℤ) ∣ (n : ℤ) := Int.ofNat_dvd.mpr hmn
  exact dvd_trans hmn_int hndvd

end q_gl_kummer_filtration

end QOU.QGeometricLanglands
