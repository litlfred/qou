import Mathlib.Data.Nat.Basic
import Mathlib.Tactic.NormNum
import QOU.Machinery.KashiwaraCrystalBasic

/-!
# QOU.BraidsAndKnots.TypeBFoldingCpt — the D22 conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:type-b-folding-cpt`](type-b-folding-cpt.md): *D22 Type-B folding*.

**No instance is provided** — the honest open state for a conjecture (AGENTS.md §3b).

## 2026-09-05 — this carrier used to assert nothing

It read, in full:

```lean
class TypeBFoldingCpt where
  holds : Prop
```

A field typed `: Prop` has the *universe* of propositions as its type, so an instance
supplies a proposition rather than a proof of one: `⟨True⟩` discharges the class, and every
`[TypeBFoldingCpt]`-conditional theorem was conditional on nothing.

**Prior work, credited.** The defect class is bean `qou-tsnp`'s — *"GAP: 12 conjecture
carriers axiomatised as `holds : Prop` assert nothing"* — which lists this carrier among
its twelve, with the corpus-wide census at
[`docs/audits/2026-08-23-free-prop-field-census.md`](../../../docs/audits/2026-08-23-free-prop-field-census.md)
(PR #5562) and a re-runnable detector at
[`scripts/free-prop-field-audit.py`](../../../scripts/free-prop-field-audit.py). What is new
here is the **repair**, in that bean's prescribed shape. D9 (`IsospinFromCanonicalBowtie`,
#6671), D10 (`SpinFromSo3Fiber`, #6683) and the parity carrier (`PFromBraidMirror`, #6728)
were closed the same way; a fresh library-twin check was run first, per the D11 lesson
(#6711), and came back empty — no `TypeBFolding*` declaration exists anywhere under
`lean/QOU/`, so the content repair is the right move here rather than a mis-ref fix.

**A dead pointer was dropped.** The old header directed the reader to
`../lean/QOU/BraidsAndKnots/TypeBFoldingCPT.lean` "(file pending)". That file does not
exist and never did; the ref resolves to this sibling.

## What is encoded

The block makes four claims. Two are stated here, in caller-parameter form.

**1. The Cartan-datum fold.** The `𝔰𝔩ₙ` simple roots `α₁, …, α_{n-1}` (the `A_{n-1}`
diagram) are folded by the involution `ι : αᵢ ↔ α_{n-i}` — the diagram reversal. `fold` is
the caller's label map and `fold_reverses` pins it to the block's own `i ↦ n - i` on the
label range.

**2. Matter and antimatter as the fixed/moved split.** The block's physical content, in
one sentence: *"Stable matter = fixed points of the folded crystal; antimatter = the
`ι`-orbit complement."* `foldAct` is the induced `ℤ/2` on the crystal vertices,
`stable`/`anti` the two predicates, and `stable_iff_fixed` / `anti_iff_moved` say exactly
that. These are **not** derivable from field 1 — `typeBFoldingCpt_refutable_on_matter`
below exhibits a caller satisfying every other field and failing this one, so the leg
carries independent content.

**2a. `foldAct` is the lift of the fold (added 2026-11-20, bean `qou-dx7g`).** The
crystal is now an explicit `QOU.Machinery.CrystalGraph` `G`, every label `i ∈ [1, n-1]` must
act on it (`labels_act`), and `foldAct` must intertwine the Kashiwara operators with the
label fold, `foldAct ∘ fᵢ = f_{ι(i)} ∘ foldAct` (and likewise for `eᵢ`). Before this,
`foldAct` was an arbitrary involution of an arbitrary type, unrelated to `fold`, and
`foldAct = id`, `stable = True`, `anti = False` satisfied every field for every `n` — so the
matter/antimatter split asserted nothing about any crystal.
`typeBFoldingCpt_refutable_on_crystal` shows that inhabitant now fails on `B(Λ₁)` of `𝔰𝔩₃`.

`G`, `n`, `fold`, `foldAct`, `stable` and `anti` are all supplied by the **caller**, per
the design rule recorded in `QOU/AlgebraicSubstrate/ConditionalClasses.lean` after its own
retraction — an `∃` over a quantity the statement is itself free to choose cannot be
false, whereas a `∀` over a quantity the caller supplies can. So the class is refutable,
and that is discharged in two theorems below rather than asserted in prose. (The rule is
paraphrased rather than quoted: its original wording is second-person and trips
`voice-scholarly-default`, which the two sibling repairs quote verbatim behind stale
sidecar entries.)

## What is DERIVED rather than axiomatised

Four consequences follow from the fields and are proved, not assumed:

* `typeBFold_label_involutive` — the label map really is a `ℤ/2`. Not a field: `i ↦ n - i`
  is self-inverse on `[1, n-1]`, so assuming it would have been assuming arithmetic.
* `typeBFold_label_fixed_iff_even_strands` — a simple root is `ι`-fixed exactly when
  `n = 2i`; hence `typeBFold_label_free_of_odd_strands`, the fold is fixed-point-free on
  labels for odd `n`. This is the label-level shadow of the block's matter/antimatter split.
* `typeBFold_orbit_complete_invariant` + `typeBFold_orbit_representative_range` — the
  `ι`-orbits on the `n-1` simple roots are classified by `min i (n - i) ∈ [1, n/2]`. That
  orbit count **is** the rank of the folded datum, so this is the arithmetic behind the
  block's own `B_{n/2}`, discharged rather than restated.
* `typeBFold_no_global_chirality_grading` — **the interesting one.** If any stable matter
  exists, the folded crystal admits no globally `foldAct`-odd chirality grading. This is
  the corpus's own proved obstruction, re-derived from this carrier's fields: compare
  `QOU.StandardModel.Chirality.stable_matter_and_global_chirality_incompatible` in
  [`lean/QOU/StandardModel/TypeBFoldingChiralityObstruction.lean`](../lean/QOU/StandardModel/TypeBFoldingChiralityObstruction.lean),
  which proves the same dilemma for a bare involution and reads it *against* this block.
  Reproducing it here is the check that the repaired carrier is strong enough to imply a
  known non-trivial result about itself — and it fixes the sign of the relationship: this
  file does **not** contradict that obstruction, it entails it.

  Read together with that file's scope note, the honest reading stays scope-(a): what is
  excluded is the identification of *this* fold involution with the chirality involution,
  not Type-B folding's other roles.

## What is NOT encoded, and why

**3. Bar-invariance of the GS normal forms.** The block says the folded crystal is a
symmetric crystal *"whose GS normal forms are bar-involution invariant by construction"*.
That leg **already has a carrier**: `QOU.BraidKnot.SymmetricCrystalPairProduction` (block
`conj:symmetric-crystal-pair-production`) carries `barInvolution`, `bar_involutive` and
`bar_invariant` over `[CrystalGraphRealization R q]`, and states the same Type-B folding
premise. Restating it here would put two competing statements of one claim in the corpus —
the duplicate-carrier failure the D11 library-twin check exists to prevent — so it is
named and left where it lives.

**4. The `CPT = C ⊗ P ⊗ T` tensor decomposition.** The block gives it as three rows (C from
colour-sheet flavour conjugation, P from Type-B Cartan folding, T from Markov-trace
cyclicity). Stating it needs `C`, `P` and `T` as maps on one common type, whose carriers
are three separate blocks. #6728 left the identical composition unstated for
`conj:p-from-braid-mirror` and named the same missing object; **what must grow first is a
common braid-word / crystal type carrying `C`, `P` and `T` simultaneously**, so the
composite identity can be written at all.

**Consistency with #6728, which must not be broken.** That PR fixed the vocabulary: the
bar-involution sends `σᵢ ↦ σᵢ⁻¹` **and** `q ↦ q⁻¹` and is `P·C·T` composed, while `P`
alone is `σᵢ^ε ↦ σᵢ^{-ε}` with `q` held **fixed**. Nothing here restates bar. D22's claim
is narrower and orthogonal: that in the folded realisation the *role of* `P` is played by
the Cartan-fold `ℤ/2` rather than by explicit braid-mirror manipulation. Stating that
identification needs `P` and `foldAct` on one type — the same missing object as above — so
it too is named and left.

**Also not encoded: that the folded datum is of type `B` specifically.** The corpus has no
Cartan-datum or root-system type; `Machinery/KashiwaraCrystalBasic.lean` carries
`CrystalGraph`, `TypeACrystal` and `DemazureSubcrystal`, but nothing that could distinguish
`B_{n/2}` from `C_{n/2}` or from a bare folded datum of rank `n/2`. What is stated is the
`ℤ/2` and its orbit count (the *rank*); the type label would be invention. Per `qou-tsnp`'s
guard, that is named rather than faked: **a root-system / Cartan-matrix type must grow
first.**

**Also not claimed:** that any such `fold`, `foldAct` or crystal exists on the corpus's
Hecke types. No instance is provided; the carrier says what the folding must satisfy, not
that something does.

## Base ring

Deliberately generic — there is no ring here at all. Labels are `ℕ`, the crystal is an
abstract `CrystalGraph` (vertex type arbitrary), and the chirality grading is `Bool`-valued. Nothing
archimedean is needed to say what the fold does, so per §7c this stays over type variables
rather than specialising to `ℝ`. Bar-involution and crystal combinatorics are algebraic.

-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/type-b-folding-cpt.ts
-/

namespace QOU.BraidsAndKnots

/-! ### Unconditional arithmetic of the diagram reversal

These are facts about `i ↦ n - i` on the `A_{n-1}` label range `[1, n-1]`, independent of
the conjecture; the class-conditional statements below are their transports along
`fold_reverses`. -/

/-- The label range `[1, n-1]` is closed under the diagram reversal `i ↦ n - i`. -/
theorem typeBFold_label_mem_range {n i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    1 ≤ n - i ∧ n - i ≤ n - 1 := by omega

/-- **Orbit representatives.** `min i (n - i)` is constant on `ι`-orbits and lands in
`[1, n/2]` — the label set of the folded datum. -/
theorem typeBFold_orbit_representative_range {n i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    1 ≤ min i (n - i) ∧ min i (n - i) ≤ n / 2 := by omega

/-- **`min i (n - i)` is a complete invariant of the `ι`-orbits**: two simple roots share a
representative exactly when they are equal or swapped by the reversal.

With `typeBFold_orbit_representative_range`, this says the `ι`-orbits on the `n-1` simple
roots of `A_{n-1}` are indexed by `[1, n/2]` — i.e. the folded datum has rank `n/2`, which
is the arithmetic content of the block's `B_{n/2}`. -/
theorem typeBFold_orbit_complete_invariant {n i j : ℕ}
    (hi : 1 ≤ i) (hi' : i ≤ n - 1) (hj : 1 ≤ j) (hj' : j ≤ n - 1) :
    min i (n - i) = min j (n - j) ↔ (j = i ∨ j = n - i) := by omega

/-! ### The carrier -/

/-- **CONJECTURE (D22).** Type-B Cartan folding realises CPT via symmetric-crystal `ℤ/2`
fixed points.

The `𝔰𝔩ₙ` Cartan datum folds under `ι : αᵢ ↔ α_{n-i}`; the induced `ℤ/2` on the folded
Kashiwara crystal splits its vertices into stable matter (the fixed points) and antimatter
(the orbit complement).

`n` is the strand count, `fold` the label map, `V` the crystal vertex type, `foldAct` the
induced involution, and `stable`/`anti` the two predicates. All are supplied by the
**caller**, so the class is false for data that does not behave this way — see
`typeBFoldingCpt_refutable` (the label leg) and `typeBFoldingCpt_refutable_on_matter` (the
physical leg, which fails independently).

Deliberately **not** stated here: the bar-invariance of GS normal forms (carried by
`QOU.BraidKnot.SymmetricCrystalPairProduction`), the `CPT = C ⊗ P ⊗ T` decomposition, and
the identification of the folded datum as type `B` rather than merely rank-`n/2`. See the
module docstring for what must grow first in each case.

**No instance is provided.** Downstream results consume this as
`[TypeBFoldingCpt n fold foldAct stable anti]` and are genuinely conditional on it.

-- Ref: [kashiwara1991] Kashiwara, "On crystal bases of the q-analogue of universal enveloping algebras," Duke Math. J. 63 (1991)
-- Ref: [lecouvey2007] Lecouvey, "Combinatorics of crystal graphs for the root systems of types A_n, B_n, C_n, D_n and G_2," MSJ Memoirs 17 (2007)
-- Ref: [leitner2026] conj:type-b-folding-cpt -/
class TypeBFoldingCpt (G : QOU.Machinery.CrystalGraph) (n : ℕ) (fold : ℕ → ℕ)
    (foldAct : G.V → G.V) (stable anti : G.V → Prop) : Prop where
  /-- The fold is the **diagram reversal** `αᵢ ↔ α_{n-i}` on the `A_{n-1}` simple-root
  labels — the block's own `ι`. -/
  fold_reverses : ∀ i, 1 ≤ i → i ≤ n - 1 → fold i = n - i
  /-- **Every simple root acts on the crystal.**  Each label `i ∈ [1, n-1]` has at least
  one `fᵢ`-arrow, so the crystal is a genuine rank-`(n-1)` crystal and not the trivial one
  (on which every operator is `none` and any vertex map would intertwine). -/
  labels_act : ∀ i, 1 ≤ i → i ≤ n - 1 → ∃ v w, G.f i v = some w
  /-- **`foldAct` is the lift of the label fold to the crystal**: it intertwines the
  lowering operators, `foldAct ∘ fᵢ = f_{ι(i)} ∘ foldAct`.  (Added 2026-11-20, bean
  `qou-dx7g`: before this field `foldAct` was an arbitrary involution unrelated to `fold`,
  so `foldAct = id` with `stable = True`, `anti = False` inhabited the class.) -/
  foldAct_f : ∀ i, 1 ≤ i → i ≤ n - 1 → ∀ v, (G.f i v).map foldAct = G.f (fold i) (foldAct v)
  /-- Same for the raising operators. -/
  foldAct_e : ∀ i, 1 ≤ i → i ≤ n - 1 → ∀ v, (G.e i v).map foldAct = G.e (fold i) (foldAct v)
  /-- The fold **induces a `ℤ/2` on the crystal**. This is a genuine assumption: that the
  label-level reversal lifts to an involution of crystal vertices at all is part of what
  "the folded crystal is a symmetric crystal" asserts. -/
  foldAct_involutive : ∀ v, foldAct (foldAct v) = v
  /-- **Stable matter = fixed points of the folded crystal.** -/
  stable_iff_fixed : ∀ v, stable v ↔ foldAct v = v
  /-- **Antimatter = the `ι`-orbit complement** — the vertices the fold moves. -/
  anti_iff_moved : ∀ v, anti v ↔ foldAct v ≠ v

/-! ### Consequences

Each is derived from the fields above; none is a restatement of one. -/

/-- **The label fold is an involution** — derived from `fold_reverses` plus the closure of
the label range, not assumed. -/
theorem typeBFold_label_involutive {G : QOU.Machinery.CrystalGraph} {n : ℕ} {fold : ℕ → ℕ} {foldAct : G.V → G.V}
    {stable anti : G.V → Prop} [h : TypeBFoldingCpt G n fold foldAct stable anti]
    {i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    fold (fold i) = i := by
  obtain ⟨k, k'⟩ := typeBFold_label_mem_range hi hi'
  rw [h.fold_reverses i hi hi', h.fold_reverses (n - i) k k']
  omega

/-- **A simple root is `ι`-fixed exactly when `n = 2i`** — so a fixed label exists only for
an even strand count, and then only at `i = n/2`. The label-level shadow of the block's
matter/antimatter split. -/
theorem typeBFold_label_fixed_iff_even_strands {G : QOU.Machinery.CrystalGraph} {n : ℕ} {fold : ℕ → ℕ}
    {foldAct : G.V → G.V} {stable anti : G.V → Prop}
    [h : TypeBFoldingCpt G n fold foldAct stable anti]
    {i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    fold i = i ↔ n = 2 * i := by
  rw [h.fold_reverses i hi hi']
  omega

/-- **For an odd strand count the fold is fixed-point-free on labels.** The odd-`n` case of
the previous; recorded because it is the label-level analogue of the chirality obstruction
below — an odd `n` leaves no `ι`-fixed simple root to carry stable matter.

Proved directly from `fold_reverses` rather than by rewriting with the theorem above: the
latter's `V`, `foldAct`, `stable` and `anti` are implicit and undetermined by the label
arguments, so the instance search would be stuck on metavariables. -/
theorem typeBFold_label_free_of_odd_strands {G : QOU.Machinery.CrystalGraph} {n : ℕ} {fold : ℕ → ℕ}
    {foldAct : G.V → G.V} {stable anti : G.V → Prop}
    [h : TypeBFoldingCpt G n fold foldAct stable anti]
    (hodd : ¬ 2 ∣ n) {i : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) :
    fold i ≠ i := by
  intro hfix
  rw [h.fold_reverses i hi hi'] at hfix
  exact hodd ⟨i, by omega⟩

/-- **Orbit equality in terms of the carrier's own `fold`.** The transport of
`typeBFold_orbit_complete_invariant` along `fold_reverses`: two simple roots lie in the
same `ι`-orbit exactly when one is the other's fold image. -/
theorem typeBFold_orbit_eq_iff {G : QOU.Machinery.CrystalGraph} {n : ℕ} {fold : ℕ → ℕ} {foldAct : G.V → G.V}
    {stable anti : G.V → Prop} [h : TypeBFoldingCpt G n fold foldAct stable anti]
    {i j : ℕ} (hi : 1 ≤ i) (hi' : i ≤ n - 1) (hj : 1 ≤ j) (hj' : j ≤ n - 1) :
    min i (fold i) = min j (fold j) ↔ (j = i ∨ j = fold i) := by
  rw [h.fold_reverses i hi hi', h.fold_reverses j hj hj']
  exact typeBFold_orbit_complete_invariant hi hi' hj hj'

/-- **Matter and antimatter partition the crystal** — the block's word "complement", made
precise. Derived from the two predicate fields; neither alone gives it. -/
theorem typeBFold_stable_iff_not_anti {G : QOU.Machinery.CrystalGraph} {n : ℕ} {fold : ℕ → ℕ} {foldAct : G.V → G.V}
    {stable anti : G.V → Prop} [h : TypeBFoldingCpt G n fold foldAct stable anti] (v : G.V) :
    stable v ↔ ¬ anti v := by
  rw [h.stable_iff_fixed v, h.anti_iff_moved v]
  simp

/-- **If stable matter exists, the folded crystal carries no globally odd chirality
grading.**

If `stable v` then `foldAct v = v`, so any `chir` with `chir (foldAct w) = !chir w` for all
`w` gives `chir v = !chir v`, which is false.

This is the corpus's own obstruction, re-derived from this carrier's fields: compare
`QOU.StandardModel.Chirality.stable_matter_and_global_chirality_incompatible`, which proves
the same dilemma for a bare involution and reads it against this very block. So the
repaired carrier is strong enough to entail a known non-trivial result about itself —
and it agrees with, rather than contradicts, the existing scope-(a) finding that this
fold involution cannot itself be the chirality involution. -/
theorem typeBFold_no_global_chirality_grading {G : QOU.Machinery.CrystalGraph} {n : ℕ} {fold : ℕ → ℕ}
    {foldAct : G.V → G.V} {stable anti : G.V → Prop}
    [h : TypeBFoldingCpt G n fold foldAct stable anti]
    {v : G.V} (hv : stable v) :
    ¬ ∃ chir : G.V → Bool, ∀ w, chir (foldAct w) = ! chir w := by
  rintro ⟨chir, hodd⟩
  have hfix : foldAct v = v := (h.stable_iff_fixed v).mp hv
  have hv' := hodd v
  rw [hfix] at hv'
  simp at hv'

/-! ### Refutability

The property the `holds : Prop` carrier lacked. Three witnesses, because the class has
independent legs and a single witness would only show one of them has content.

`symBoolCrystal` is a two-vertex crystal in which *every* label `i` acts by the same arrow
`false ↦ true`; it is `ι`-symmetric by construction, so the identity intertwines `fᵢ` with
`f_{ι(i)}`, and it is the cheapest crystal on which the label and matter legs can be tested
separately. `string3Crystal` is the standard `𝔰𝔩₃` crystal `B(Λ₁)` with labels `1, 2`
(`0 →f₁→ 1 →f₂→ 2`); on it the crystal leg has teeth. -/

/-- A two-vertex crystal on which every label acts by `false ↦ true`. -/
def symBoolCrystal : QOU.Machinery.CrystalGraph where
  V := Bool
  f := fun _ v => if v = false then some true else none
  e := fun _ v => if v = true then some false else none

/-- The standard `𝔰𝔩₃` crystal `B(Λ₁)`, labels `1, 2`: `0 →f₁→ 1 →f₂→ 2`. -/
abbrev string3Crystal : QOU.Machinery.CrystalGraph where
  V := Fin 3
  f := fun i v =>
    if i = 1 ∧ v = 0 then some 1 else if i = 2 ∧ v = 1 then some 2 else none
  e := fun i v =>
    if i = 1 ∧ v = 1 then some 0 else if i = 2 ∧ v = 2 then some 1 else none

/-- **The label leg is refutable**: the identity label map is not the diagram reversal at
`n = 4`, so it fails `fold_reverses` at `i = 1`. -/
theorem typeBFoldingCpt_refutable :
    ¬ TypeBFoldingCpt symBoolCrystal 4 id id (fun _ => True) (fun _ => True) := by
  intro hc
  have h := hc.fold_reverses 1 (by norm_num) (by norm_num)
  simp at h

/-- **The matter leg is refutable independently**: the *correct* reversal `i ↦ 4 - i`, an
identity crystal action that genuinely intertwines (every label acts alike on
`symBoolCrystal`), and still a failure, because an action that moves nothing has an empty
orbit complement — so `anti_iff_moved` carries content the other fields do not supply. -/
theorem typeBFoldingCpt_refutable_on_matter :
    ¬ TypeBFoldingCpt symBoolCrystal 4 (fun i => 4 - i) id (fun _ => True) (fun _ => True) := by
  intro hc
  exact ((hc.anti_iff_moved true).mp trivial) rfl

/-- **The crystal leg is refutable — the old trivial inhabitant is gone.**  Before
2026-11-20, `foldAct = id`, `stable = True`, `anti = False` satisfied the class for every
`n`.  On the genuine `𝔰𝔩₃` crystal `B(Λ₁)` the identity does not intertwine `f₁` with
`f_{ι(1)} = f₂` (`f₁ 0 = 1` but `f₂ 0` is undefined), so it is not a lift of the fold. -/
theorem typeBFoldingCpt_refutable_on_crystal :
    ¬ TypeBFoldingCpt string3Crystal 3 (fun i => 3 - i) id (fun _ => True) (fun _ => False) := by
  intro hc
  have h := hc.foldAct_f 1 (by norm_num) (by norm_num) 0
  simp at h

end QOU.BraidsAndKnots
