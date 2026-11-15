import Mathlib.Data.Nat.Basic


/-!
# QOU.Archimedean.generation_completeness — All embeddable knots are reachable

Every knot with Seifert genus g(K) ≤ 4 is reachable from the generator
set 𝒢 by a finite sequence of Skein crossing changes.  The generation
scheme applied to 𝒢 produces every knot type that admits a localized
knot structure in the Descartes universe.

LaTeX label: `thm:generation-completeness`

## What the Lean states — and what carries the content

History (bean `qou-0avp` → `qou-08zf`, 2026-09-03;
`docs/audits/2026-08-30-generation-completeness-is-vacuous.md`).  Until
this revision `isReachable K := ∃ r : ℕ, r ≤ K.unknottingNumber` — inhabited
by `r = 0` for **every** `K`, so the "theorem" constrained no knot, its genus
hypothesis was dead code, and its corollary restated its own hypothesis.

Now reachability is an actual reachability relation over an actual move
set.  A `GenerationScheme` carries a generator predicate, a distinguished
unknot in the generator set, a one-step crossing-change relation, the
Seifert genus and the unknotting number — and, as its one content field,
the **defining property of the unknotting number** (Kauffman): every knot
type is obtained from the unknot by `u(K)` crossing changes.  The theorem
composes that field with `unknot ∈ 𝒢`.  It does **not** construct knots:
the geometric content is the modelling assumption `unknotting_realised`,
stated explicitly rather than hidden in a trivially-inhabited predicate.

The genus bound `g(K) ≤ 4` is the *scope* of the spectrum (which knots the
theorem is about), not an input to reachability — reachability holds for
every knot type, and `reachable_of_unknotting` says so without the
hypothesis.  The corollary asserting particle-spectrum completeness
(`V_phys = colim V^⊗n`) has no formal carrier for `V_phys` and is not
stated; it was previously `⟨h, trivially-true⟩`.

## References

- [leitner2026] §5/generation-completeness
- [kauffman1991] https://doi.org/10.1142/1116
-/

namespace QOU.Archimedean

/-- The genus bound for the Bring's surface. -/
def genusBound : ℕ := 4

/-- `ReachableIn r n a b`: `b` is obtained from `a` by **exactly `n`** steps
    of the one-step relation `r`. -/
inductive ReachableIn {K : Type*} (r : K → K → Prop) : ℕ → K → K → Prop
  | refl (a : K) : ReachableIn r 0 a a
  | step {n : ℕ} {a b c : K} (hab : ReachableIn r n a b) (hbc : r b c) :
      ReachableIn r (n + 1) a c

/-- Zero steps reach exactly the starting point (sanity: the step count is
    meaningful). -/
theorem ReachableIn.eq_of_zero {K : Type*} {r : K → K → Prop} {a b : K}
    (h : ReachableIn r 0 a b) : a = b := by
  cases h
  rfl

/-- **A generation scheme** over a type `K` of knot types: the generator
    set `𝒢`, the unknot `T_{1,0} ∈ 𝒢`, the one-step Skein crossing-change
    relation, the two invariants the theorem mentions, and the defining
    property of the unknotting number. -/
structure GenerationScheme (K : Type*) where
  /-- Membership in the generator set `𝒢`. -/
  isGenerator : K → Prop
  /-- The unknot `T_{1,0}`. -/
  unknot : K
  /-- `T_{1,0} ∈ 𝒢`. -/
  unknot_generator : isGenerator unknot
  /-- One Skein crossing change. -/
  crossingChange : K → K → Prop
  /-- Seifert genus. -/
  seifertGenus : K → ℕ
  /-- Unknotting number. -/
  unknottingNumber : K → ℕ
  /-- **The defining property of the unknotting number** (Kauffman): every
      knot type is obtained from the unknot by exactly `u(K)` crossing
      changes.  This is the field that carries the geometric content; the
      theorem below does not re-derive it. -/
  -- Ref: [kauffman1991] Kauffman, "Knots and Physics," World Scientific 1991
  unknotting_realised : ∀ k, ReachableIn crossingChange (unknottingNumber k) unknot k

variable {K : Type*} (S : GenerationScheme K)

/-- A knot type is embeddable if its Seifert genus is within the bound. -/
def isEmbeddable (k : K) : Prop := S.seifertGenus k ≤ genusBound

/-- A knot type is **reachable from `𝒢`** if some generator reaches it by a
    finite sequence of Skein crossing changes. -/
def Reachable (k : K) : Prop :=
  ∃ (g : K) (n : ℕ), S.isGenerator g ∧ ReachableIn S.crossingChange n g k

/-- Every knot type is reachable from `𝒢`: the unknot is a generator and the
    unknotting number realises `k` from it.  This is the theorem's real
    content, without the scope hypothesis. -/
theorem reachable_of_unknotting (k : K) : Reachable S k :=
  ⟨S.unknot, S.unknottingNumber k, S.unknot_generator, S.unknotting_realised k⟩

/-- **Generation completeness** (Theorem):

    Let `K` be any knot type with Seifert genus `g(K) ≤ 4`.  Then `K` is
    reachable from the generator set `𝒢` by a finite sequence of Skein
    crossing changes.

    The genus hypothesis is the scope of the spectrum and is not consumed
    by the proof (see the module docstring); the content is
    `reachable_of_unknotting`, i.e. `GenerationScheme.unknotting_realised`
    composed with `unknot_generator`. -/
-- Ref: [kauffman1991] Kauffman, "Knots and Physics," World Scientific 1991
-- Ref: [leitner2026] §5/generation-completeness
theorem generation_completeness (k : K) (_h_embed : isEmbeddable S k) :
    Reachable S k :=
  reachable_of_unknotting S k

end QOU.Archimedean
