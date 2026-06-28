import Mathlib.Tactic

/-!
# QOU.KleinBringBridge — the Klein icosahedral–quintic / Bring-radical bridge

Formalises [`conj:klein-bring-icosahedral-bridge`](klein-bring-icosahedral-bridge.md):
a faithful icosahedral `A₅`-action on the categorical base `ℙ(V)` (archimedean
realisation `τ(ℙ(V)) ≅ ℙ¹(ℂ)`) realising Klein's solution of the
Bring–Jerrard quintic, with quotient `ℙ(V)/A₅ ≅ S²(2,3,5)` = the keystone
Seifert base of `S³/2I`.

Three layers (AGENTS.md §3b / §3b-tax):

* a **proved arithmetic skeleton** — spherical `(2,3,5)`, icosahedral order `60`,
  orbit obstruction;
* a **proved refutation of the naive assembly** — `dihedral_two_cycle_sq`: the
  corpus's canonical order-2/order-3 force generators (`def:su2-generators`,
  `βαβ⁻¹ = α⁻¹`) satisfy `(βα)² = 1`, the `(2,3,2)` dihedral relation, so they
  generate the trefoil `S₃`, **not** the icosahedral `(2,3,5)`; and
* the **sharpened primary conjecture** `KleinBringIcosahedralBridge` — a
  content-bearing class with **no instance** requiring an order-5 product
  `(c₂ c₃)^5 = 1` (icosahedral-angle generators, *distinct* from the trefoil
  pair the refutation excludes). `-- Ref: [klein1888]`.

Base ring (§7c): `ℕ`/`ℚ` arithmetic + abstract group data — no archimedean
construct, no `ℝ`. Authored in a sandbox without a Lean toolchain;
**not yet `lean`-direct verified** (manifest `validation: not_checked`).
-/

namespace QOU.KleinBringBridge

/-! ## Proved arithmetic skeleton (classical, no fit) -/

/-- The `(2,3,5)` triangle is **spherical**: `1/2 + 1/3 + 1/5 = 31/30 > 1`,
so its orientation-preserving triangle group is finite — the icosahedral `A₅`. -/
theorem triangle_235_spherical : (1 : ℚ) / 2 + 1 / 3 + 1 / 5 > 1 := by norm_num

/-- Order of the icosahedral group `A₅`. -/
def icoOrder : ℕ := 60

theorem icoOrder_two   : icoOrder = 2 * 30 := by norm_num [icoOrder]
theorem icoOrder_three : icoOrder = 3 * 20 := by norm_num [icoOrder]
theorem icoOrder_five  : icoOrder = 5 * 12 := by norm_num [icoOrder]

/-- `A₅`-orbit sizes on `ℙ(V) = S²` are `60/{1,2,3,5} = {60,30,20,12}` (cyclic
point-stabilisers). **No orbit has size `6`** and the minimum is `12`, so the
ED's six branch points `{ζ₅ᵏ, ∞}` are not `A₅`-invariant (they are the
`C₅`-pentagon). -/
theorem no_orbit_of_size_six :
    ∀ k ∈ ({1, 2, 3, 5} : Finset ℕ), icoOrder / k ≠ 6 := by decide

/-! ## Proved refutation of the naive assembly (the trefoil generators are dihedral) -/

/-- **The canonical force generators are `(2,3,2)`-dihedral, not `(2,3,5)`.**
In any group, the dihedral relation `β α β = α⁻¹` (the `def:su2-generators`
relation `βαβ⁻¹ = α⁻¹` with `β² = 1`, so `β⁻¹ = β`) forces the product `βα` to
square to the identity:
`(βα)² = (βαβ)·α = α⁻¹·α = 1`.
Hence `βα` has order dividing `2` — it can **never** have the order `5` an
icosahedral `(2,3,5)` triangle relation demands. The corpus's order-3 colour
`α = exp((2π/3)e₃)` and order-2 EM `β = exp(πe₁)` therefore generate the trefoil
`S₃ ≅ D₃`, refuting the naive "reuse the trefoil generators" assembly of the
bridge (scope-limited). -/
theorem dihedral_two_cycle_sq {G : Type*} [Group G] (α β : G)
    (h : β * α * β = α⁻¹) : (β * α) * (β * α) = 1 := by
  have hassoc : (β * α) * (β * α) = (β * α * β) * α := by group
  rw [hassoc, h]
  group

/-- Corollary: a `(2,3,2)`-dihedral pair cannot satisfy the icosahedral order-5
product relation `(βα)·(βα)·(βα)·(βα)·(βα) = 1` unless `βα = 1` (the degenerate
case). Since `(βα)² = 1`, the fifth power collapses to `βα`. -/
theorem dihedral_not_order_five {G : Type*} [Group G] (α β : G)
    (h : β * α * β = α⁻¹) :
    (β * α) * ((β * α) * ((β * α) * ((β * α) * (β * α)))) = β * α := by
  have h2 : (β * α) * (β * α) = 1 := dihedral_two_cycle_sq α β h
  calc
    (β * α) * ((β * α) * ((β * α) * ((β * α) * (β * α))))
        = (β * α) * (((β * α) * (β * α)) * ((β * α) * (β * α))) := by group
    _ = (β * α) * (1 * 1) := by rw [h2]
    _ = β * α := by group

/-! ## The sharpened primary conjecture (open QOU wiring) -/

/-- **Klein icosahedral–quintic / Bring-radical bridge** (PRIMARY conjecture,
§3b-tax — content-bearing class, no instance = open state).

`G` is the conjectural icosahedral `A₅` acting on the categorical base
`P := ℙ(V)` via `act`; `c2, c3 : G` are an **order-2 / order-3 pair at the
icosahedral angle** — *distinct* from the corpus trefoil generators, which
`dihedral_two_cycle_sq` proves cannot satisfy the field `triangle_relation`
below. The decisive open hypothesis is `triangle_relation`: their product has
order exactly `5` (the `(2,3,5)` icosahedral relation). The deep classical
inputs — Klein's icosahedral solution of the Bring–Jerrard quintic and the
identification `ℙ(V)/A₅ ≅ S²(2,3,5)` (keystone Seifert base) — are carried as
the conjectural hypothesis; no instance is constructed.

-- Ref: [klein1888] https://archive.org/details/lecturesonikosa00kleigoog
-- Ref: [bring1786] (Bring–Jerrard reduction of the quintic) -/
class KleinBringIcosahedralBridge
    (G : Type*) [Monoid G] (P : Type*) (act : G → P → P)
    (c2 c3 : G) : Prop where
  /-- the order-2 generator (icosahedral 2-fold, distinct from the EM trefoil β). -/
  order_c2 : c2 ^ 2 = 1 ∧ c2 ≠ 1
  /-- the order-3 generator (icosahedral 3-fold, distinct from the colour trefoil α). -/
  order_c3 : c3 ^ 3 = 1 ∧ c3 ≠ 1
  /-- **the decisive icosahedral relation**: the product `c2 c3` has order
      exactly `5` (`(2,3,5)`). This is what the corpus trefoil pair provably
      fails (`dihedral_two_cycle_sq`: there `(βα)² = 1`). -/
  triangle_relation : (c2 * c3) ^ 5 = 1 ∧ (c2 * c3) ≠ 1 ∧ (c2 * c3) ^ 2 ≠ 1
  /-- the icosahedral group acts faithfully on the base `P = ℙ(V)`. -/
  faithful : ∀ g h : G, (∀ p : P, act g p = act h p) → g = h

end QOU.KleinBringBridge
