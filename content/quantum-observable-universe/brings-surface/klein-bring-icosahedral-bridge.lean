import Mathlib.Tactic

/-!
# QOU.KleinBringBridge — the Klein icosahedral–quintic / Bring-radical bridge

Formalises [`conj:klein-bring-icosahedral-bridge`](klein-bring-icosahedral-bridge.md):
the proposed identification of the Bring exceptional divisor
(`ED ≅ ℙ¹(ℂ)`, the `ζ₅`-pentagon base) with the icosahedral `ℙ¹(ℂ)` of Klein's
solution of the Bring–Jerrard quintic, via the three force-symmetry orders
`{2,3,5}` = the icosahedral `(2,3,5)` triangle generators.

Two layers (AGENTS.md §3b / §3b-tax):

* a **proved arithmetic skeleton** — the spherical `(2,3,5)` fact, the
  icosahedral order `60`, and the orbit obstruction (no orbit of size `6`) —
  sorry-free, `decide`/`norm_num`; and
* the **primary conjecture** `KleinBringIcosahedralBridge` — a content-bearing
  class with **no instance** (the open QOU-wiring claim). `-- Ref: [klein1888]`.

Base ring (AGENTS.md §7c): the skeleton is `ℕ`/`ℚ` arithmetic and abstract
group data — no archimedean construct, so no `ℝ`.

Authored in a sandbox without a Lean toolchain; **not yet `lean`-direct
verified** (validation: not_checked in the manifest).
-/

namespace QOU.KleinBringBridge

/-! ## Proved arithmetic skeleton (classical, no fit) -/

/-- The `(2,3,5)` triangle is **spherical**: `1/2 + 1/3 + 1/5 = 31/30 > 1`.
Hence its orientation-preserving triangle group is finite — the icosahedral
group `A₅`. -/
theorem triangle_235_spherical : (1 : ℚ) / 2 + 1 / 3 + 1 / 5 > 1 := by norm_num

/-- Order of the icosahedral group `A₅`. -/
def icoOrder : ℕ := 60

theorem icoOrder_two   : icoOrder = 2 * 30 := by norm_num [icoOrder]
theorem icoOrder_three : icoOrder = 3 * 20 := by norm_num [icoOrder]
theorem icoOrder_five  : icoOrder = 5 * 12 := by norm_num [icoOrder]

/-- A point-stabiliser of an `SO(3)` action on `S² = ℙ¹(ℂ)` is cyclic; the
cyclic-subgroup orders of `A₅` are exactly its element orders `{1,2,3,5}`. By
orbit–stabiliser the orbit sizes are `60/{1,2,3,5} = {60,30,20,12}` — the
classical generic/edge/face/vertex orbits. **No orbit has size `6`**, and a
finite `A₅`-invariant set is a union of orbits whose minimum size is `12 > 6`,
so the ED's six branch points `{ζ₅ᵏ, ∞}` are **not** `A₅`-invariant (they are
the `C₅`-pentagon). -/
theorem no_orbit_of_size_six :
    ∀ k ∈ ({1, 2, 3, 5} : Finset ℕ), icoOrder / k ≠ 6 := by decide

/-! ## The primary conjecture (open QOU wiring) -/

/-- **Klein icosahedral–quintic / Bring-radical bridge** (PRIMARY conjecture,
AGENTS.md §3b-tax — content-bearing class, no instance = the open state).

`G` is the abstract symmetry group (conjecturally the icosahedral `A₅`) acting
on the ED sphere `S` via `act`; `c2, c3, c5 : G` are the three corpus
force-symmetry operations:

* `c2` — the electromagnetic Möbius involution `z ↦ 1/z` (order `2`);
* `c3` — the colour/trefoil triality (order `3`);
* `c5` — the weak `ζ₅`-Bring pentad (order `5`).

The fields encode the QOU-wiring content: the three operations have the
icosahedral orders, satisfy the `(2,3,5)` triangle relation `c5 = c2 * c3`
(so `(c2 c3)^5 = 1`), and act **faithfully** on the ED. The deep classical
inputs — Klein's icosahedral solution of the Bring–Jerrard quintic and the
identification `ED/A₅ ≅ S²(2,3,5)` (the keystone Seifert base) — are carried as
the conjectural hypothesis; no instance is constructed.

-- Ref: [klein1888] https://archive.org/details/lecturesonikosa00kleigoog
-- Ref: [bring1786] (Bring–Jerrard reduction of the quintic) -/
class KleinBringIcosahedralBridge
    (G : Type*) [Monoid G] (S : Type*) (act : G → S → S)
    (c2 c3 c5 : G) : Prop where
  /-- the electromagnetic involution has order exactly `2`. -/
  order_c2 : c2 ^ 2 = 1 ∧ c2 ≠ 1
  /-- the colour/trefoil triality has order exactly `3`. -/
  order_c3 : c3 ^ 3 = 1 ∧ c3 ≠ 1
  /-- the weak/`ζ₅` pentad has order exactly `5`. -/
  order_c5 : c5 ^ 5 = 1 ∧ c5 ≠ 1
  /-- the `(2,3,5)` triangle relation: the product of the order-`2` and
      order-`3` generators is the order-`5` pentad — the defining relation of
      the icosahedral triangle group, so `(c2 * c3) ^ 5 = 1`. -/
  triangle_relation : c2 * c3 = c5
  /-- the symmetry group acts faithfully on the ED sphere `S` (distinct group
      elements act distinctly) — the icosahedral `A₅` acts effectively on
      `ℙ¹(ℂ)`. -/
  faithful : ∀ g h : G, (∀ s : S, act g s = act h s) → g = h

end QOU.KleinBringBridge
