import QOU.Machinery.KashiwaraCrystalBasic

/-!
# `CompositeKashiwaraResidueA` is already inhabited, and is weak

`CompositeKashiwaraResidueA` is **not** uninhabited: the source file itself
declares `instance : CompositeKashiwaraResidueA.{0, 0} standardSl2Crystal`.
It should be removed from the "uninhabited class" debt list.

**What is proved here (sorry-free).** `compositeKashiwaraResidueA_iff`: for
every crystal graph `G`,

  `CompositeKashiwaraResidueA G ↔ StembridgeCrystal G ∧ ∃ v, ∀ i, G.e i v = none`.

So the class says only "the operators are mutually inverse partial maps, and
some vertex is annihilated by every raising operator". The `has_type_A` field
is always satisfiable (embed `G` into itself, at any `n`), and `has_demazure`
is satisfiable at `level = 0` by any highest-weight singleton. Neither field
carries type-A or Demazure content.

**What is not proved.** Any genuine type-A (tensor-power of the standard
`sl_n` crystal) or Demazure statement: the class does not encode one. Making
it do so (e.g. fixing the target of `TypeACrystal` to the actual `B(Λ₁)^{⊗N}`
of `sl_n`, and requiring `level ≥ 1` with a nontrivial Weyl word) is a refactor
of the source classes and needs owner approval.

-- Ref: [leitner2026] QOU.Machinery.KashiwaraCrystalBasic; [kashiwara1995]
-- M. Kashiwara, On crystal bases, CMS Conf. Proc. 16 (1995), §7 (crystal
-- axioms); [stembridge2003] J. Stembridge, A local characterization of
-- simply-laced crystals, Trans. AMS 355 (2003).
-/

namespace QOU.Machinery.Instances

open QOU.Machinery

universe u

/-- Every crystal embeds into itself, at any rank label `n`. -/
def typeA_self (G : CrystalGraph.{u}) (n : ℕ) : TypeACrystal.{u, u} G n where
  target := G
  embed :=
    { toFun := id
      map_f := fun _ _ => by simp
      map_e := fun _ _ => by simp }
  embed_injective := Function.injective_id

/-- Any highest-weight vertex gives a level-`0` Demazure sub-crystal. -/
def demazure_zero (G : CrystalGraph.{u}) (v : G.V) (hv : ∀ i, G.e i v = none) :
    DemazureSubcrystal.{u} G 0 where
  member := fun w => w = v
  highest := v
  highest_mem := rfl
  highest_isHighest := hv
  demazure_closure := fun _ hi => absurd hi (Nat.not_lt_zero _)

/-- **Characterisation**: the composite class is reversibility plus the
existence of a highest-weight vertex. -/
theorem compositeKashiwaraResidueA_iff (G : CrystalGraph.{u}) :
    CompositeKashiwaraResidueA.{u, u} G ↔
      StembridgeCrystal G ∧ ∃ v : G.V, ∀ i, G.e i v = none := by
  constructor
  · intro h
    obtain ⟨_, ⟨D⟩⟩ := h.has_demazure
    exact ⟨h.is_stembridge, D.highest, D.highest_isHighest⟩
  · rintro ⟨hS, v, hv⟩
    exact ⟨hS, ⟨0, ⟨typeA_self G 0⟩⟩, ⟨0, ⟨demazure_zero G v hv⟩⟩⟩

end QOU.Machinery.Instances
