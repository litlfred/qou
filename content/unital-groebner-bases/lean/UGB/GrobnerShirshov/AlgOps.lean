import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.NormalForms
import Mathlib.Data.Finset.Image

/-!
# Generic admissible orders

The arithmetic on `AlgElement G k` (`single`, `add`, `smul`, `sub`,
`leftMulGen`, `ofTerms`, `contextMul`, …) now lives in `Elem.lean`, which
`Basic.lean` imports: stating a reduction step needs subtraction and
two-sided multiplication by a monomial, so those operations have to be
available *before* the reduction relations, not after them. Nothing was
renamed and everything is still in the `UGB.GrobnerShirshov` namespace, so
`import UGB.GrobnerShirshov.AlgOps` continues to bring all of it into scope.

What remains here is the order-theoretic half: shortlex well-foundedness and
the generic deg-lex `AdmissibleOrder` construction for any generator type
with an injective rank function.
-/


namespace UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Ring k] [DecidableEq G]

/-! ## §8  Generic Deg-Lex Order Construction -/

/-- **Shortlex well-foundedness** (Mathlib v4.24.0 gap). Pure `List.Lex` is *not*
    well-founded on unbounded-length lists (e.g. `[1] ≻ [0,1] ≻ [0,0,1] ≻ …`); the
    length-first refinement — "shorter word, or equal length and lexicographically
    smaller" — restores well-foundedness for any well-founded base relation `r`.
    This is the generic replacement for `NormalForms.lexEncoding`, whose fixed-base
    encoding into `ℕ` only works for the finite generator set `SU2Gen`; an arbitrary
    injective `rank : G → ℕ` has unbounded image, so no order-embedding of the
    length-`n` lex order (order type `ω^n`) into `ℕ` (order type `ω`) exists — the
    accessibility must be proved directly. -/
theorem shortLex_wellFounded {α : Type*} {r : α → α → Prop} (hr : WellFounded r) :
    WellFounded (fun a b : List α =>
      a.length < b.length ∨ (a.length = b.length ∧ List.Lex r a b)) := by
  constructor
  intro a0
  suffices key : ∀ n : ℕ, ∀ a : List α, a.length ≤ n →
      Acc (fun a b : List α => a.length < b.length ∨
        (a.length = b.length ∧ List.Lex r a b)) a by
    exact key a0.length a0 le_rfl
  intro n
  induction n with
  | zero =>
    intro a ha
    cases a with
    | nil =>
      refine Acc.intro [] (fun b hb => ?_)
      rcases hb with hlt | ⟨_, hlex⟩
      · exact absurd hlt (Nat.not_lt_zero _)
      · cases hlex
    | cons h t =>
      simp only [List.length_cons] at ha
      exact absurd ha (Nat.not_succ_le_zero _)
  | succ n IHn =>
    -- `acc_cons`: if the head `g` is `r`-accessible and the tail has length `≤ n`,
    -- then `g :: gs` is shortlex-accessible.  Double accessibility induction:
    -- outer on `Acc r g` (handles a strictly smaller head, `List.Lex.rel`), inner
    -- on `Acc SL gs` (handles an equal head and shortlex-smaller tail, `.cons`).
    have acc_cons : ∀ g : α, Acc r g → ∀ gs : List α, gs.length ≤ n →
        Acc (fun a b : List α => a.length < b.length ∨
          (a.length = b.length ∧ List.Lex r a b)) (g :: gs) := by
      intro g hg
      induction hg with
      | intro g _ IHg =>
        suffices H : ∀ gs : List α,
            Acc (fun a b : List α => a.length < b.length ∨
              (a.length = b.length ∧ List.Lex r a b)) gs → gs.length ≤ n →
            Acc (fun a b : List α => a.length < b.length ∨
              (a.length = b.length ∧ List.Lex r a b)) (g :: gs) by
          intro gs hgs
          exact H gs (IHn gs hgs) hgs
        intro gs accgs
        induction accgs with
        | intro gs _ IHgs =>
          intro hgs
          refine Acc.intro _ (fun b hb => ?_)
          cases b with
          | nil => exact IHn [] (Nat.zero_le n)
          | cons h hs =>
            rcases hb with hlen | ⟨hlen_eq, hlex⟩
            · apply IHn
              simp only [List.length_cons] at hlen ⊢
              omega
            · simp only [List.length_cons] at hlen_eq
              have hhs : hs.length = gs.length := by omega
              cases hlex with
              | rel hr' => exact IHg h hr' hs (by omega)
              | cons hlx => exact IHgs hs (Or.inr ⟨hhs, hlx⟩) (by omega)
    intro a ha
    cases a with
    | nil =>
      refine Acc.intro [] (fun b hb => ?_)
      rcases hb with hlt | ⟨_, hlex⟩
      · exact absurd hlt (Nat.not_lt_zero _)
      · cases hlex
    | cons g gs =>
      simp only [List.length_cons] at ha
      exact acc_cons g (hr.apply g) gs (by omega)

/-- Construct a deg-lex `AdmissibleOrder` for any generator type `G`
    equipped with an injective rank function `rank : G → ℕ`.

    This generalises `degLexOrder` from NormalForms.lean (which is
    specific to `SU2Gen`).  The proofs are identical in structure:
    - Well-foundedness: from `List.Lex.wellFounded` via rank
    - Trichotomy: case split on length, then on lex
    - Compatibility: length preserved by concatenation

    We delegate to the existing NormalForms infrastructure by mapping
    generators to `SU2Gen` (or more precisely, to `ℕ` via rank) and
    using `List.Lex.wellFounded` directly. -/
noncomputable def mkDegLexOrder {G : Type u} [DecidableEq G]
    (rank : G → ℕ) (rank_inj : Function.Injective rank) :
    AdmissibleOrder G where
  lt := fun a b =>
    a.length < b.length ∨
    (a.length = b.length ∧ List.Lex (fun x y => rank x < rank y) a b)
  trichotomy := by
    intro a b
    by_cases h1 : a.length < b.length
    · left; left; exact h1
    · by_cases h2 : b.length < a.length
      · right; right; left; exact h2
      · have heq : a.length = b.length := by omega
        -- Same length: compare lexicographically
        have : ∀ (x y : List G), x.length = y.length →
            List.Lex (fun a b => rank a < rank b) x y ∨
            x = y ∨
            List.Lex (fun a b => rank a < rank b) y x := by
          intro x
          induction x with
          | nil => intro y hy; cases y with
            | nil => right; left; rfl
            | cons _ _ => simp at hy
          | cons g gs ih => intro y hy; cases y with
            | nil => simp at hy
            | cons h hs =>
              simp [List.length_cons] at hy
              by_cases hr1 : rank g < rank h
              · left; exact List.Lex.rel hr1
              · by_cases hr2 : rank h < rank g
                · right; right; exact List.Lex.rel hr2
                · have hge : rank g = rank h := by omega
                  have hgh : g = h := rank_inj hge
                  subst hgh
                  rcases ih hs hy with hlx | heq | hrx
                  · left; exact List.Lex.cons hlx
                  · right; left; rw [heq]
                  · right; right; exact List.Lex.cons hrx
        rcases this a b heq with hlx | heq' | hrx
        · left; right; exact ⟨heq, hlx⟩
        · right; left; exact heq'
        · right; right; right; exact ⟨heq.symm, hrx⟩
  wf :=
    -- Shortlex well-foundedness (`shortLex_wellFounded`) with base relation
    -- `rank · < rank ·` = `InvImage (·<·) rank`, well-founded because `Nat.lt`
    -- is and `InvImage` preserves well-foundedness.  Pure lex is NOT
    -- well-founded (see NormalForms.lean's note where `lexLt_wf` was removed);
    -- the length-first refinement is what restores it — proved sorry-free above.
    -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
    shortLex_wellFounded (InvImage.wf rank Nat.lt_wfRel.wf)
  left_compat := by
    intro a b c h
    rcases h with hlen | ⟨heq, hlex⟩
    · left; simp; omega
    · right; refine ⟨?_, ?_⟩
      · simp; omega
      · -- c ++ a lex< c ++ b when a lex< b (same length)
        induction c with
        | nil => simpa
        | cons x xs ih =>
          simp only [List.cons_append]
          exact List.Lex.cons ih
  right_compat := by
    intro a b d h
    rcases h with hlen | ⟨heq, hlex⟩
    · left; simp; omega
    · right; refine ⟨by simp; omega, ?_⟩
      -- a ++ d lex< b ++ d when a lex< b (same length).
      -- Ref: [bergman1978] https://doi.org/10.1016/0001-8708(78)90010-5
      -- Induction on a (generalising b): the lex difference is in the
      -- prefix, so appending a common suffix preserves it.
      induction a generalizing b with
      | nil =>
        cases b with
        | nil => cases hlex
        | cons _ _ => simp at heq
      | cons x xs ih =>
        cases b with
        | nil => simp at heq
        | cons y ys =>
          simp only [List.cons_append]
          cases hlex with
          | cons h =>
            have heq' : xs.length = ys.length := by
              simp [List.length_cons] at heq; exact heq
            exact List.Lex.cons (ih ys heq' h)
          | rel h => exact List.Lex.rel h

end UGB.GrobnerShirshov
