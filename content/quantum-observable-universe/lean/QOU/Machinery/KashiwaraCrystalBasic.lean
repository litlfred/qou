import Mathlib.Tactic

/-
Copyright (c) 2026 litlfred. All rights reserved.

# Kashiwara crystal basic structure scaffold (2026-06-04)

This file scaffolds the minimal Kashiwara-crystal infrastructure
needed for the residue A composite-operator promotion path D (and
related theorems in `MmuR9V9Closure.lean`).

## What this provides

A type-level scaffold for a Kashiwara crystal graph (`CrystalGraph`)
with:
- Underlying type of vertices
- Decorator: weight, rank labels
- Crystal operators `f_i`, `e_i` as `Option`-valued partial endomorphisms
- Type-classes that downstream theorems can carry

The actual algebraic content (Stembridge crystal axiom, type-A
embedding, Demazure closure) is captured as conditional classes whose
fields state the genuine conditions (crystal reversibility, a crystal
morphism into the abstract standard-`sl_n` target, closure of the
Demazure sub-crystal under lowering) — no longer `True` markers. The
`standardSl2Crystal` (`B(Λ₁)`) instances below inhabit all four classes,
so the scaffold is honest (non-vacuous) infrastructure. Constructing the
*general* instances (the concrete standard-`sl_n` tensor-power crystal and
the Demazure characters) is the open — and currently unscheduled —
infrastructure work; see the route-status note below.

## Route status (2026-07-17): PARKED — honest scaffold, do-not-re-pitch route

This scaffold is honest and non-vacuous, but the motivating route it was
built to serve — a **residue-A KLR/crystal derivation of the `Q_β` `c_k`
precision-ladder coefficients** — is **not** an active direction, and this
file should not be read as an invitation to wire it up:

- The KLR/crystal link-Markov-closure route carries a standing
  **"DO NOT RE-PITCH"** note in `.beans/1ppq-qbeta-queue.json` (AGENTS.md
  §7b skeptical prior + the 2026-05-30 KLR dialog assessment found 0/6
  candidate proofs shorten under a KLR layer).
- Its finite-dimensional form is **falsified**: the 2026-07-11 Gemini audit
  (`docs/audits/2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md`,
  Finding 4) shows the `[3]_q`/Gram-trace "pion" factor does not fall out of
  the finite-dim KLR/Hecke `H₃(q)` Markov trace (raw trace `−4 + i√3 ≠ 0`).
- The live `c_k` direction has moved to the geometric Φ_b state-integral +
  `D(u)` ladder function, which does **not** route through these types.

Accordingly these classes have **no downstream Lean consumers** at present.
The residue-A infra scope doc below remains "scoping only; owner direction
required before any items proceed" — no such go-ahead is on record. Keep the
scaffold (an honest inhabited scaffold is strictly better than the vacuous
`: True` version it replaced); do not resurrect the residue-A crystal route
without first clearing the do-not-re-pitch prior with the owner.

## Cross-refs

- Audit (scope, owner-gated): [`docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../../../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md)
- Do-not-re-pitch note: `.beans/1ppq-qbeta-queue.json`
- KLR finite-dim falsification: `docs/audits/2026-07-11-gemini-session-c3-overclaim-continuum-and-lean-audit.md` (Finding 4)
- `MmuR9V9Closure.lean` Theorem 5 deep claim (cinquefoil framing) — does not reference these types
- `QBetaCategoricalPrecisionLadder.lean` — the actual residue-A `c_k` ladder; **axiomatises** `c_k` for `k ≥ 4` directly and does **not** consume these crystal classes (intended-but-never-wired downstream)
-/

namespace QOU.Machinery

/-! ## Basic Kashiwara crystal graph -/

/-- **Kashiwara crystal graph** structure: a type `V` of vertices,
with partial endomorphisms `f i : V → Option V` and `e i : V → Option V`
indexed by simple-root labels `i : ℕ`. -/
structure CrystalGraph where
  /-- The vertex set. -/
  V : Type*
  /-- Lowering operator `f i v` (Option-valued for partiality). -/
  f : ℕ → V → Option V
  /-- Raising operator `e i v` (Option-valued for partiality). -/
  e : ℕ → V → Option V

/-! ## Trivial / one-vertex crystal -/

/-- The **trivial crystal**: one vertex `unit`, both operators return `none`. -/
def trivialCrystal : CrystalGraph where
  V := Unit
  f _ _ := none
  e _ _ := none

/-- The trivial crystal has exactly one vertex (by `Unit` being a singleton). -/
theorem trivialCrystal_unique_vertex (v : trivialCrystal.V) :
    v = () := rfl

/-! ## The standard `sl₂` crystal `B(Λ₁)`

A genuine (non-trivial) crystal, used below to inhabit
`StembridgeCrystal` with a real reversible pair of operators. -/

/-- The **standard `sl₂` crystal** `B(Λ₁)`: two vertices — `false` = highest
weight, `true` = lowest weight — joined by the single `f₀`-arrow
`false ↦ true` (and its `e₀`-inverse `true ↦ false`). All other operators
are `none`. -/
def standardSl2Crystal : CrystalGraph where
  V := Bool
  f := fun i v => if i = 0 ∧ v = false then some true else none
  e := fun i v => if i = 0 ∧ v = true then some false else none

/-! ## Crystal morphisms -/

/-- A **morphism of crystal graphs**: a vertex map `toFun` commuting with
both the lowering (`f`) and raising (`e`) operators.  Bundling the two
morphism laws as separate fields keeps downstream rewriting smooth. -/
structure CrystalHom (G G' : CrystalGraph) where
  /-- The underlying vertex map. -/
  toFun : G.V → G'.V
  /-- `toFun` commutes with lowering: `f i` then map = map then `f i`. -/
  map_f : ∀ (i : ℕ) (v : G.V), (G.f i v).map toFun = G'.f i (toFun v)
  /-- `toFun` commutes with raising: `e i` then map = map then `e i`. -/
  map_e : ∀ (i : ℕ) (v : G.V), (G.e i v).map toFun = G'.e i (toFun v)

/-! ## Conditional classes for the Stembridge axioms + type-A specialisation -/

/-- Conditional class carrying the foundational crystal axiom.
NEAR-MATCH tier.  The reversibility field is inhabitable by a genuine
crystal — see the `standardSl2Crystal` instance below; the full
Stembridge S1–S8 instance still requires upstream Mathlib crystal-graph
machinery.

The single field encodes the Kashiwara **reversibility** law, *not* the
full Stembridge S1–S8 (whose additional string-length / interplay
conditions would further constrain an instance) — hence the field is
named `reversibility` rather than `stembridge_axioms`. -/
class StembridgeCrystal (G : CrystalGraph) : Prop where
  /-- The foundational Kashiwara crystal axiom presupposed by the full
      Stembridge S1–S8: for every simple-root label `i`, the raising and
      lowering operators `e i`, `f i` are mutually inverse partial maps —
      `f i v = some w ↔ e i w = some v`.  (No longer `True`.) -/
  reversibility :
    ∀ (i : ℕ) (v w : G.V), G.f i v = some w ↔ G.e i w = some v

/-- **`B(Λ₁)` is a genuine `StembridgeCrystal`** — a concrete,
non-trivial inhabitant of the reversibility axiom (unlike
`trivialCrystal`, whose operators are all `none`).  The `f₀ : false ↦ true`
arrow and its `e₀`-inverse are mutually reversible; every other operator
is `none` on both sides. -/
instance : StembridgeCrystal standardSl2Crystal where
  reversibility := by
    intro i v w
    by_cases hi : i = 0
    · subst hi
      cases v <;> cases w <;> simp [standardSl2Crystal]
    · simp [standardSl2Crystal, hi]

/-- Conditional class for type-A specialisation: the crystal `G` embeds
into a tensor-power crystal of the standard `sl_n` representation.  The
target crystal is abstract (the concrete standard-`sl_n` tensor-power
construction is substantial and not in Mathlib); the class carries it as
a datum, `embed` as a genuine crystal morphism (`CrystalHom`, so the two
morphism laws are separate fields), and `embed_injective` making it a
true *embedding*. -/
class TypeACrystal (G : CrystalGraph) (n : ℕ) where
  /-- The target crystal — a tensor power of the standard `sl_n` crystal
      (abstract datum). -/
  target : CrystalGraph
  /-- The embedding as a crystal morphism (commutes with `f` and `e`).
      (Was the `True` field `sl_n_embedding`.) -/
  embed : CrystalHom G target
  /-- The embedding is injective — a genuine embedding, not just a
      morphism. -/
  embed_injective : Function.Injective embed.toFun

/-- Conditional class for Demazure module identification: a Demazure
sub-crystal at level `level` corresponds to a Weyl-group word.  The
sub-crystal is carried as a predicate `member` with a distinguished
highest-weight generator (`highest`, pinned by `highest_isHighest` as an
actual highest-weight vertex — annihilated by every raising operator);
`demazure_closure` states the defining Demazure property (closed under the
first `level` lowering operators — the Weyl-word support). -/
class DemazureSubcrystal (G : CrystalGraph) (level : ℕ) where
  /-- Membership predicate cutting out the Demazure sub-crystal. -/
  member : G.V → Prop
  /-- The distinguished highest-weight vertex generating the sub-crystal. -/
  highest : G.V
  /-- The generator lies in the sub-crystal. -/
  highest_mem : member highest
  /-- `highest` really is highest-weight: every raising operator
      annihilates it (`e i highest = none`). -/
  highest_isHighest : ∀ (i : ℕ), G.e i highest = none
  /-- **Demazure closure** (was `True`): the sub-crystal is closed under
      lowering by the first `level` simple roots — exactly the operators
      in the support of the length-`level` Weyl word. -/
  demazure_closure :
    ∀ (i : ℕ), i < level → ∀ (v w : G.V),
      member v → G.f i v = some w → member w

/-! ## The standard `sl₂` crystal inhabits every base Kashiwara class

Concrete instances for `standardSl2Crystal` (`B(Λ₁)`), showing all three
base conditional-class types are inhabitable by a real crystal — not just
`StembridgeCrystal` (above). -/

/-- **`B(Λ₁)` is a genuine `TypeACrystal`** at `n = 2`: it embeds into the
standard `sl₂` crystal (itself) by the identity, which is a crystal
morphism (commutes with `f`/`e`) and is injective. -/
instance instSl2TypeACrystal : TypeACrystal standardSl2Crystal 2 where
  target := standardSl2Crystal
  embed :=
    { toFun := id
      map_f := fun _ _ => by simp
      map_e := fun _ _ => by simp }
  embed_injective := Function.injective_id

/-- **`B(Λ₁)`'s level-1 Demazure sub-crystal — which happens to be everything.**

`sl₂` has one simple root, so `W = {e, s₀}` and `B(Λ₁)` has exactly two Demazure
sub-crystals: `B_e(Λ₁) = {u_Λ}` at length 0, and
`B_{s₀}(Λ₁) = {u_Λ, f₀ u_Λ}` at length 1 — and the second is the *whole*
two-vertex crystal.  So `member := fun _ => True` is the **correct value** here,
not a shortcut: the level-1 sub-crystal of `B(Λ₁)` really is all of it.

**What that costs, and why it was flagged** (2026-08-24, bean `qou-uno5`).  This
docstring used to call the witness *"a genuine `DemazureSubcrystal` … closed
under lowering"*, which reads as though closure had been checked.  It has not:
with `member ≡ True` both the hypothesis and the conclusion of
`demazure_closure` are trivially inhabited, so the field closes by `trivial` —
exactly the strength it had when it was literally `True`, before someone
strengthened it into the real closure condition.  The strengthening bought
nothing *while this was the only inhabitant*.  It is not any more:
`sl3DemazureLevelOne` below is a **proper** sub-crystal whose closure has to be
verified, and `sl3LevelOne_not_closed_at_level_two` proves the field can fail.

`highest_isHighest` is the one field this witness does exercise — `e i false =
none` for every `i` is checked, not assumed.

Still a global `instance`, and correctly so: `DemazureSubcrystal
standardSl2Crystal 1` is a fact about a concrete two-vertex crystal, not a
conjecture, so resolution supplying it is sound.  Read it as "the whole crystal
at the longest Weyl word", never as evidence about Demazure closure in general. -/
instance instSl2DemazureSubcrystal : DemazureSubcrystal standardSl2Crystal 1 where
  member := fun _ => True
  highest := false
  highest_mem := trivial
  highest_isHighest := fun _ => by simp [standardSl2Crystal]
  demazure_closure := fun _ _ _ _ _ _ => trivial

/-! ## A rank where the Demazure condition has teeth

The two-vertex `sl₂` crystal cannot separate a proper Demazure sub-crystal from
the whole crystal at `level = 1`: with one simple root, the length-1 Weyl word
already sweeps everything.  Three vertices and two simple roots can, so the
closure field is tested here rather than left untested (bean `qou-uno5`). -/

/-- The **standard `sl₃` crystal** `B(Λ₁)`: three vertices in a string
`0 -f₀→ 1 -f₁→ 2`, with the matching `e`-inverses.  Vertex `0` is the
highest-weight vector; there are two simple roots, labelled `0` and `1`.

An `abbrev` rather than a `def` (unlike `standardSl2Crystal`) so that
`standardSl3Crystal.V` reduces to `Fin 3` at *reducible* transparency and
instance search finds `OfNat` / `DecidableEq` / `Fintype` on the vertices — which
is what lets the closure obligations below be discharged by `decide`.  The `sl₂`
crystal needs none of this: its vertices are `Bool`, whose two literals are
constructors rather than numerals. -/
abbrev standardSl3Crystal : CrystalGraph where
  V := Fin 3
  f := fun i v =>
    if i = 0 ∧ v = 0 then some 1
    else if i = 1 ∧ v = 1 then some 2
    else none
  e := fun i v =>
    if i = 0 ∧ v = 1 then some 0
    else if i = 1 ∧ v = 2 then some 1
    else none

/-- **A PROPER Demazure sub-crystal**: `B_{s₀}(Λ₁) = {0, 1}` inside the
three-vertex `sl₃` crystal, at `level = 1`.

Unlike `instSl2DemazureSubcrystal`, `demazure_closure` here is a real obligation:
the membership predicate excludes the vertex `2`, so the proof has to check that
no `f₀`-arrow leaves `{0, 1}` — none does, because the only arrow out of `1` is
`f₁`, which `level = 1` does not range over.

Deliberately a `def` and not an `instance`: nothing should acquire this witness
by resolution. -/
def sl3DemazureLevelOne : DemazureSubcrystal standardSl3Crystal 1 where
  member := fun v => v ≠ 2
  highest := 0
  highest_mem := by decide
  highest_isHighest := fun i => by
    simp only [standardSl3Crystal]
    split <;> simp_all
  demazure_closure := by
    intro i hi v w hv hf
    have hi0 : i = 0 := Nat.lt_one_iff.mp hi
    subst hi0
    revert hv hf
    revert v w
    decide

/-- **The sub-crystal really is proper (PROVED)**: the lowest vertex `2` is not a
member, so this witness is not the whole crystal in disguise. -/
theorem sl3DemazureLevelOne_proper :
    ¬ sl3DemazureLevelOne.member 2 :=
  fun h => h rfl

/-- **`demazure_closure` is a falsifiable condition (PROVED).**  The very same
membership predicate `{0, 1}` fails the closure requirement at `level = 2`,
because `f₁` carries `1` to `2`, which is outside it.  So the strengthened field
is not `True` in disguise: it holds at level 1 and fails at level 2 for one fixed
predicate — which is what `member ≡ True` could never show. -/
theorem sl3LevelOne_not_closed_at_level_two :
    ¬ (∀ (i : ℕ), i < 2 → ∀ (v w : standardSl3Crystal.V),
        sl3DemazureLevelOne.member v →
        standardSl3Crystal.f i v = some w →
        sl3DemazureLevelOne.member w) := by
  intro h
  have hmem : sl3DemazureLevelOne.member 1 := by
    show (1 : Fin 3) ≠ 2
    decide
  have harr : standardSl3Crystal.f 1 1 = some 2 := by decide
  exact h 1 (by norm_num) 1 2 hmem harr rfl

/-- **…and it constrains the predicate at a fixed level, too (PROVED).**  The
singleton `{0}` — which *is* the level-0 Demazure sub-crystal `B_e(Λ₁)` — is not
closed at `level = 1`, because `f₀` carries `0` to `1`.  Together with
`sl3DemazureLevelOne` this pins the field down from both sides: at a fixed level
it selects which subsets are Demazure sub-crystals, and for a fixed subset it
selects which levels. -/
theorem sl3_singleton_not_closed_at_level_one :
    ¬ (∀ (i : ℕ), i < 1 → ∀ (v w : standardSl3Crystal.V),
        v = 0 → standardSl3Crystal.f i v = some w → w = 0) := by
  intro h
  have harr : standardSl3Crystal.f 0 0 = some 1 := by decide
  have hbad : (1 : Fin 3) = 0 := h 0 (by norm_num) 0 1 rfl harr
  exact absurd hbad (by decide)

/-! ## Conditional theorem: residue-A composite identification

If a crystal `G` carries all three classes above, then the crystal
operator `f_1^2` acting on the trefoil-image vertex would produce the
empirical c_2 = -1 Taylor coefficient (this is the proven content of
`QBetaCategoricalPrecisionLadder.lean`). The composite operator
`f_1^2 · q-Pochhammer-evaluation` is the path D candidate. -/

/-- Conditional class combining the three classes above for the
composite identification of residue A. -/
class CompositeKashiwaraResidueA (G : CrystalGraph) : Prop where
  /-- Stembridge axioms hold. -/
  is_stembridge : StembridgeCrystal G
  /-- Type-A specialisation at some n (data class, so wrapped in `Nonempty`
      to sit inside the existential). -/
  has_type_A : ∃ n, Nonempty (TypeACrystal G n)
  /-- Demazure sub-crystal correspondence at some level (`Nonempty` for the
      same reason). -/
  has_demazure : ∃ level, Nonempty (DemazureSubcrystal G level)

/-! ## The standard `sl₂` crystal inhabits the full composite class

Assembling the three base instances above (`StembridgeCrystal`,
`TypeACrystal` at `n = 2`, `DemazureSubcrystal` at `level = 1`) shows the
composite residue-A class is inhabitable by a real crystal — not just a
conditional scaffold. -/

/-- **`B(Λ₁)` inhabits `CompositeKashiwaraResidueA`**: it is a Stembridge
crystal, carries a type-A embedding (`n = 2`) and a Demazure sub-crystal
(`level = 1`).  The explicit `.{0,0}` universe annotation pins the two
universe metavariables introduced by the universe-carrying `TypeACrystal`/
`DemazureSubcrystal` target fields (§7d — `standardSl2Crystal.V = Bool`
and each abstract `target.V` live in `Type 0`), so the three base instances
unify at a single rigid universe. -/
instance : CompositeKashiwaraResidueA.{0, 0} standardSl2Crystal where
  is_stembridge := inferInstance
  has_type_A := ⟨2, ⟨instSl2TypeACrystal⟩⟩
  has_demazure := ⟨1, ⟨instSl2DemazureSubcrystal⟩⟩

end QOU.Machinery
