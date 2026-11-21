import Mathlib.Data.Multiset.Bind
import Mathlib.Data.Multiset.Filter
import Mathlib.Data.Fintype.Basic
import Mathlib.Logic.Relation
import Mathlib.Data.Fin.Basic
import Mathlib.Logic.Embedding.Basic

/-!
# Oriented link diagram codes and Reidemeister moves

A combinatorial model of oriented link diagrams, meant as the diagram layer of the PL-knot plan
(issue #8902, stage 4) and as the target of braid closure.

A `Code E` over an edge type `E` is a finite multiset of oriented crossings and a finite multiset of
joins. A crossing records its under strand `uin → uout`, its over strand `oin → oout` and a sign.
A join `(a, b)` says that edge `a` continues as edge `b` with no crossing in between. Joins let braid
closure and the local moves be written without renumbering edges; `contract` removes them.

The moves:

* `embed`: relabel the edges along an injection (this also adds unused edges);
* `contract`: remove a join `(a, b)` with `a ≠ b` by identifying `b` with `a`;
* `r1`: a join becomes a kink (four kinds: sign, and whether the strand passes under or over first);
* `r2par` / `r2anti`: two joins become a bigon, with the strands parallel or antiparallel;
* `r3`: the braid-like positive triangle move, read off `σ₁σ₂σ₁ = σ₂σ₁σ₂`.

`ReidemeisterEquiv` is the equivalence relation they generate on bundled codes.

**What this layer does not do.** A code records no planar structure, so it also describes virtual
diagrams; no planarity predicate is imposed here. The move set is the one braid closure needs
(see `braidClosure`); whether it generates all oriented Reidemeister moves on planar codes is
not claimed here. Polyak's minimal generating sets are the reference for that comparison.

-- Ref: [polyak2010] Polyak, "Minimal generating sets of Reidemeister moves",
--   Quantum Topol. 1 (2010) 399–411
-- Ref: [kassel-turaev2008] Kassel–Turaev, "Braid Groups", GTM 247, Ch. 2–3 (closure, Markov)
-/

namespace QOU.MathlibExt.PL.Diagram

universe u

/-- An oriented crossing. The under strand runs `uin → uout`, the over strand runs
`oin → oout`, and `pos` is the sign. -/
structure Crossing (E : Type u) where
  uin : E
  uout : E
  oin : E
  oout : E
  pos : Bool

namespace Crossing

variable {E F G : Type u}

/-- Relabel the edges of a crossing. -/
def map (f : E → F) (x : Crossing E) : Crossing F :=
  ⟨f x.uin, f x.uout, f x.oin, f x.oout, x.pos⟩

@[simp] theorem map_id (x : Crossing E) : x.map id = x := rfl

theorem map_map (f : E → F) (g : F → G) (x : Crossing E) :
    (x.map f).map g = x.map (g ∘ f) := rfl

/-- `e` is one of the four edges at the crossing. -/
def Mentions (x : Crossing E) (e : E) : Prop :=
  x.uin = e ∨ x.uout = e ∨ x.oin = e ∨ x.oout = e

end Crossing

/-- An oriented link diagram code over the edge type `E`. -/
structure Code (E : Type u) where
  xs : Multiset (Crossing E)
  js : Multiset (E × E)

namespace Code

variable {E F G : Type u}

/-- Relabel the edges of a code. -/
def map (f : E → F) (D : Code E) : Code F :=
  ⟨D.xs.map (Crossing.map f), D.js.map (Prod.map f f)⟩

@[simp] theorem map_id (D : Code E) : D.map id = D := by
  cases D; simp [map]

theorem map_map (f : E → F) (g : F → G) (D : Code E) :
    (D.map f).map g = D.map (g ∘ f) := by
  cases D; simp [map, Multiset.map_map, Function.comp_def, Crossing.map_map, Prod.map]

instance : Add (Code E) := ⟨fun D D' => ⟨D.xs + D'.xs, D.js + D'.js⟩⟩

@[simp] theorem add_xs (D D' : Code E) : (D + D').xs = D.xs + D'.xs := rfl
@[simp] theorem add_js (D D' : Code E) : (D + D').js = D.js + D'.js := rfl

/-- The code with the given crossings and no joins. -/
def ofXs (xs : Multiset (Crossing E)) : Code E := ⟨xs, 0⟩

/-- The code with the given joins and no crossings. -/
def ofJs (js : Multiset (E × E)) : Code E := ⟨0, js⟩

/-- `e` occurs somewhere in the code. -/
def Occurs (D : Code E) (e : E) : Prop :=
  (∃ x ∈ D.xs, x.Mentions e) ∨ (∃ j ∈ D.js, j.1 = e ∨ j.2 = e)

open Classical in
/-- Each edge has exactly one head and one tail: it leaves exactly one crossing or join and enters
exactly one. This is what makes a code describe a closed oriented 1-manifold. -/
def WellFormed (D : Code E) : Prop :=
  ∀ e : E, Occurs D e →
    (D.xs.countP (fun x => x.uout = e ∨ x.oout = e) + D.js.countP (fun j => j.1 = e) = 1) ∧
    (D.xs.countP (fun x => x.uin = e ∨ x.oin = e) + D.js.countP (fun j => j.2 = e) = 1)

end Code

/-- A code bundled with its edge type. -/
def Bundled : Type (u + 1) := Σ E : Type u, Code E

variable {E : Type u}

/-- The four kinks of Reidemeister I on a join `a → b`, with loop edge `ℓ`. -/
def kink (a b ℓ : E) (underFirst s : Bool) : Crossing E :=
  if underFirst then ⟨a, ℓ, ℓ, b, s⟩ else ⟨ℓ, b, a, ℓ, s⟩

/-- The parallel bigon of Reidemeister II: the strand `a → b` passes over `c → d` twice,
through the new edges `e₁` (over) and `f₁` (under), with opposite signs. -/
def bigonPar (a b c d e₁ f₁ : E) (s : Bool) : Multiset (Crossing E) :=
  {⟨c, f₁, a, e₁, s⟩, ⟨f₁, d, e₁, b, !s⟩}

/-- The antiparallel bigon of Reidemeister II. -/
def bigonAnti (a b c d e₁ f₁ : E) (s : Bool) : Multiset (Crossing E) :=
  {⟨f₁, d, a, e₁, s⟩, ⟨c, f₁, e₁, b, !s⟩}

/-- The left side of the braid-like Reidemeister III move, the closure pattern of `σ₁σ₂σ₁`:
strand `A` (`a₀ → a₁ → a₂`) is over both others, `C` (`c₀ → c₁ → c₂`) under both. -/
def triL (a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ : E) : Multiset (Crossing E) :=
  {⟨b₀, b₁, a₀, a₁, true⟩, ⟨c₀, c₁, a₁, a₂, true⟩, ⟨c₁, c₂, b₁, b₂, true⟩}

/-- The right side of the braid-like Reidemeister III move, the closure pattern of `σ₂σ₁σ₂`. -/
def triR (a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ : E) : Multiset (Crossing E) :=
  {⟨c₀, c₁, b₀, b₁, true⟩, ⟨c₁, c₂, a₀, a₁, true⟩, ⟨b₁, b₂, a₁, a₂, true⟩}

/-- One elementary move between bundled codes, in the forward direction. `ReidemeisterEquiv` takes
the symmetric, transitive closure. In each local move the new internal edges are required to be
fresh, i.e. not to occur in the rest `R` of the code and to be distinct from the boundary edges. -/
inductive Move : Bundled.{u} → Bundled.{u} → Prop
  | embed {E F : Type u} (f : E ↪ F) (D : Code E) : Move ⟨E, D⟩ ⟨F, D.map f⟩
  | contract {E : Type u} [DecidableEq E] (R : Code E) (a b : E) (hab : a ≠ b) :
      Move ⟨E, R + Code.ofJs {(a, b)}⟩ ⟨E, R.map (Function.update id b a)⟩
  | r1 {E : Type u} (R : Code E) (a b ℓ : E) (u s : Bool)
      (hℓ : ¬ R.Occurs ℓ) (ha : ℓ ≠ a) (hb : ℓ ≠ b) :
      Move ⟨E, R + Code.ofJs {(a, b)}⟩ ⟨E, R + Code.ofXs {kink a b ℓ u s}⟩
  | r2par {E : Type u} (R : Code E) (a b c d e₁ f₁ : E) (s : Bool)
      (he : ¬ R.Occurs e₁) (hf : ¬ R.Occurs f₁) (hef : e₁ ≠ f₁)
      (hbd : ∀ x ∈ ({a, b, c, d} : Set E), x ≠ e₁ ∧ x ≠ f₁) :
      Move ⟨E, R + Code.ofJs {(a, b), (c, d)}⟩ ⟨E, R + Code.ofXs (bigonPar a b c d e₁ f₁ s)⟩
  | r2anti {E : Type u} (R : Code E) (a b c d e₁ f₁ : E) (s : Bool)
      (he : ¬ R.Occurs e₁) (hf : ¬ R.Occurs f₁) (hef : e₁ ≠ f₁)
      (hbd : ∀ x ∈ ({a, b, c, d} : Set E), x ≠ e₁ ∧ x ≠ f₁) :
      Move ⟨E, R + Code.ofJs {(a, b), (c, d)}⟩ ⟨E, R + Code.ofXs (bigonAnti a b c d e₁ f₁ s)⟩
  | r3 {E : Type u} (R : Code E) (a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂ : E)
      (hint : ∀ x ∈ ({a₁, b₁, c₁} : Set E), ¬ R.Occurs x) :
      Move ⟨E, R + Code.ofXs (triL a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂)⟩
        ⟨E, R + Code.ofXs (triR a₀ a₁ a₂ b₀ b₁ b₂ c₀ c₁ c₂)⟩

/-- Reidemeister equivalence of bundled codes. -/
def ReidemeisterEquiv : Bundled.{u} → Bundled.{u} → Prop := Relation.EqvGen Move

theorem reidemeisterEquiv_equivalence : Equivalence (ReidemeisterEquiv.{u}) :=
  Relation.EqvGen.is_equivalence _

theorem ReidemeisterEquiv.refl (D : Bundled.{u}) : ReidemeisterEquiv D D :=
  Relation.EqvGen.refl _

theorem ReidemeisterEquiv.symm {D D' : Bundled.{u}} (h : ReidemeisterEquiv D D') :
    ReidemeisterEquiv D' D := Relation.EqvGen.symm _ _ h

theorem ReidemeisterEquiv.trans {D D' D'' : Bundled.{u}} (h : ReidemeisterEquiv D D')
    (h' : ReidemeisterEquiv D' D'') : ReidemeisterEquiv D D'' :=
  Relation.EqvGen.trans _ _ _ h h'

theorem ReidemeisterEquiv.of_move {D D' : Bundled.{u}} (h : Move D D') :
    ReidemeisterEquiv D D' := Relation.EqvGen.rel _ _ h

/-- Relabelling along an equivalence of edge types is a Reidemeister equivalence. -/
theorem ReidemeisterEquiv.of_equiv {E F : Type u} (e : E ≃ F) (D : Code E) :
    ReidemeisterEquiv ⟨E, D⟩ ⟨F, D.map e⟩ :=
  .of_move (Move.embed e.toEmbedding D)

/-! ### Braid closure -/

/-- The crossing that the letter `(i, b)` of a braid word on `m + 1` strands contributes at level
`k`. Edge `(k, p)` is the segment at position `p` just above level `k`. The positive letter `σᵢ`
takes the strand at position `i` over the strand at `i + 1`; `σᵢ⁻¹` takes the right one over. -/
def letterCrossing {L m : ℕ} (k : Fin L) (i : Fin m) (b : Bool) :
    Crossing (Fin (L + 1) × Fin (m + 1)) :=
  let up : Fin (L + 1) := k.castSucc
  let dn : Fin (L + 1) := k.succ
  if b then ⟨(up, i.succ), (dn, i.castSucc), (up, i.castSucc), (dn, i.succ), true⟩
  else ⟨(up, i.castSucc), (dn, i.succ), (up, i.succ), (dn, i.castSucc), false⟩

/-- The pass-through joins at level `k`: every position not touched by the letter `(i, _)`. -/
def letterJoins {L m : ℕ} (k : Fin L) (i : Fin m) :
    Multiset ((Fin (L + 1) × Fin (m + 1)) × (Fin (L + 1) × Fin (m + 1))) :=
  ((Finset.univ.filter fun p : Fin (m + 1) => p ≠ i.castSucc ∧ p ≠ i.succ).val).map
    fun p => ((k.castSucc, p), (k.succ, p))

/-- The closure of a braid word `w` on `m + 1` strands: the letter at level `k` gives a crossing
and pass-through joins, and the bottom of every position is joined back to its top. -/
def braidClosure {m : ℕ} (w : List (Fin m × Bool)) : Code (Fin (w.length + 1) × Fin (m + 1)) where
  xs := (Finset.univ.val : Multiset (Fin w.length)).map fun k =>
    letterCrossing k (w.get k).1 (w.get k).2
  js := (Finset.univ.val : Multiset (Fin w.length)).bind (fun k => letterJoins k (w.get k).1) +
    (Finset.univ.val : Multiset (Fin (m + 1))).map fun p => ((Fin.last _, p), (0, p))

end QOU.MathlibExt.PL.Diagram
