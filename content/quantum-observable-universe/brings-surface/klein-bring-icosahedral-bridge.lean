import Mathlib.Tactic

/-!
# QOU.KleinBringBridge — the Klein icosahedral–quintic / Bring-radical bridge

Formalises [`conj:klein-bring-icosahedral-bridge`](klein-bring-icosahedral-bridge.md):
a faithful icosahedral `A₅`-action on the categorical base `ℙ(V)` (archimedean
realisation `τ(ℙ(V)) ≅ ℙ¹(ℂ)`) whose order-5 generator is the corpus `ζ₅`
pentad, realising Klein's solution of the Bring–Jerrard quintic, with quotient
`ℙ(V)/A₅ ≅ S²(2,3,5)` = the keystone Seifert base of `S³/2I`.

Layers (AGENTS.md §3b / §3b-tax), all the arithmetic/group facts sorry-free:

* **arithmetic skeleton** — spherical `(2,3,5)`, order `60`, orbit obstruction;
* **refutation of the naive assembly** — `dihedral_two_cycle_sq`: the corpus's
  canonical order-2/order-3 force generators (`def:su2-generators`,
  `βαβ⁻¹ = α⁻¹`) give `(βα)² = 1`, the `(2,3,2)` trefoil — NOT `(2,3,5)`;
* **construction of the surviving core** — `icosahedral_235_realizable`: explicit
  even permutations realise the `(2,3,5)` relation (`c₂c₃` a 5-cycle), the
  positive complement; the explicit Klein generators `S = ζ₅` pentad, `T`
  (icosahedral 2-fold) live in `keystone_klein_icosahedral_construction.py`;
* the **residual primary conjecture** `KleinBringIcosahedralBridge` — now the
  *sole* open content is the orbifold identification `ℙ(V)/⟨c₂,c₃⟩ ≅ KB` (the
  keystone Seifert base `S²(2,3,5)`); content-bearing, no instance. `-- Ref: [klein1888]`.

Base ring (§7c): `ℕ`/`ℚ` arithmetic + abstract group/`Perm` data — no
archimedean construct, no `ℝ`. Authored in a sandbox without a Lean toolchain;
group lemmas + the construction cross-checked in Python;
**not yet `lean`-direct verified** (`validation: not_checked`).
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

/-- `A₅`-orbit sizes on `ℙ(V) = S²` are `60/{1,2,3,5} = {60,30,20,12}`; no orbit
has size `6`, so the ED's six branch points `{ζ₅ᵏ, ∞}` are not `A₅`-invariant. -/
theorem no_orbit_of_size_six :
    ∀ k ∈ ({1, 2, 3, 5} : Finset ℕ), icoOrder / k ≠ 6 := by decide

/-! ## Refutation of the naive assembly (the trefoil generators are dihedral) -/

/-- **The canonical force generators are `(2,3,2)`-dihedral, not `(2,3,5)`.**
The `def:su2-generators` relation `βαβ⁻¹ = α⁻¹` with `β² = 1` gives `βαβ = α⁻¹`,
forcing `(βα)² = (βαβ)·α = α⁻¹·α = 1`. So `βα` has order dividing `2` — never the
order `5` an icosahedral `(2,3,5)` relation demands; `⟨α, β⟩` is the trefoil
`S₃ ≅ D₃`. -/
theorem dihedral_two_cycle_sq {G : Type*} [Group G] (α β : G)
    (h : β * α * β = α⁻¹) : (β * α) * (β * α) = 1 := by
  have hassoc : (β * α) * (β * α) = (β * α * β) * α := by group
  rw [hassoc, h]; group

/-- Corollary: a `(2,3,2)`-dihedral pair collapses the would-be order-5 product
to `βα` itself (`(βα)⁵ = βα`), so it cannot satisfy the icosahedral relation
unless `βα = 1`. -/
theorem dihedral_not_order_five {G : Type*} [Group G] (α β : G)
    (h : β * α * β = α⁻¹) :
    (β * α) * ((β * α) * ((β * α) * ((β * α) * (β * α)))) = β * α := by
  have h2 : (β * α) * (β * α) = 1 := dihedral_two_cycle_sq α β h
  calc
    (β * α) * ((β * α) * ((β * α) * ((β * α) * (β * α))))
        = (β * α) * (((β * α) * (β * α)) * ((β * α) * (β * α))) := by group
    _ = (β * α) * (1 * 1) := by rw [h2]
    _ = β * α := by group

/-! ## Construction of the surviving core: the `(2,3,5)` relation IS realizable -/

open Equiv in
/-- **The icosahedral `(2,3,5)` relation is realizable in `A₅`** — the positive
complement to `dihedral_two_cycle_sq`. The explicit even permutations
`c₂ = (1 2)(3 4)` (order 2) and `c₃ = (0 2 4)` (order 3) have product
`c₂ c₃ = (0 1 2 3 4)` of order **exactly 5**. So order-2/order-3 generators at
the icosahedral angle exist (unlike the perpendicular trefoil pair). Klein's
explicit realization on `ℙ(V)` with `c₂ c₃ =` the `ζ₅` pentad is verified in
`scripts/keystone_klein_icosahedral_construction.py`. -/
theorem icosahedral_235_realizable :
    ∃ c2 c3 : Equiv.Perm (Fin 5),
      (c2 ^ 2 = 1 ∧ c2 ≠ 1) ∧ (c3 ^ 3 = 1 ∧ c3 ≠ 1) ∧
      ((c2 * c3) ^ 5 = 1 ∧ c2 * c3 ≠ 1 ∧ (c2 * c3) ^ 2 ≠ 1) :=
  ⟨swap (1 : Fin 5) 2 * swap 3 4, swap (0 : Fin 5) 2 * swap 2 4,
    by decide, by decide, by decide⟩

/-! ## The residual primary conjecture (sole open content: the keystone-base quotient) -/

/-- **Klein icosahedral–quintic / Bring-radical bridge** (PRIMARY conjecture,
§3b-tax). The group-theoretic core is now *discharged* (`icosahedral_235_realizable`
+ the Klein witness): an order-2/order-3 pair with `c₂c₃` the `ζ₅` pentad exists
and generates a faithful `A₅`. This class isolates the **sole residual open
content** — the orbifold identification `ℙ(V)/⟨c₂,c₃⟩ ≅ KB`, where `KB` is the
keystone Seifert base `S²(2,3,5)` of `S³/2I`. The map `proj : P → KB` realising
the quotient is the open geometric object (no instance is constructed).

* `act` — the `A₅`-action on the base `P = ℙ(V)`;
* `c2, c3` — the icosahedral-angle generators (orders 2, 3; `c₂c₃` order 5);
* `proj` — the conjectural quotient map onto the keystone base `KB`.

-- Ref: [klein1888] https://archive.org/details/lecturesonikosa00kleigoog
-- Ref: [bring1786] (Bring–Jerrard reduction of the quintic) -/
class KleinBringIcosahedralBridge
    (G : Type*) [Monoid G] (P : Type*) (act : G → P → P) (c2 c3 : G)
    (KB : Type*) (proj : P → KB) : Prop where
  /-- order-2 icosahedral generator (distinct from the refuted EM trefoil `β`). -/
  order_c2 : c2 ^ 2 = 1 ∧ c2 ≠ 1
  /-- order-3 icosahedral generator (distinct from the colour trefoil `α`). -/
  order_c3 : c3 ^ 3 = 1 ∧ c3 ≠ 1
  /-- the icosahedral `(2,3,5)` relation: `c₂c₃` (the `ζ₅` pentad) has order
      exactly `5` — realizable (`icosahedral_235_realizable`), unlike the trefoil. -/
  triangle_relation : (c2 * c3) ^ 5 = 1 ∧ c2 * c3 ≠ 1 ∧ (c2 * c3) ^ 2 ≠ 1
  /-- `A₅` acts faithfully on `P = ℙ(V)`. -/
  faithful : ∀ g h : G, (∀ p : P, act g p = act h p) → g = h
  /-- **open content (i):** `proj` is constant on `⟨c₂,c₃⟩`-orbits — it descends
      to the orbit space. -/
  proj_orbit_constant : ∀ (g : G) (p : P), proj (act g p) = proj p
  /-- **open content (ii):** `proj` realises the quotient isomorphism
      `ℙ(V)/A₅ ≅ KB` — distinct orbits map to distinct points of the keystone
      base (so `proj` is injective on the orbit space). Exhibiting such a `proj`
      onto the keystone Seifert base `S²(2,3,5)` is the open geometric problem. -/
  proj_separates_orbits : ∀ p p' : P, proj p = proj p' → ∃ g : G, act g p = p'

end QOU.KleinBringBridge
