# `UGB.GrobnerShirshov.NormalForms.lexLt_wf` is false as stated — pure lex is not well-founded

**Date:** 2026-06-25
**Status:** finding / flag (no UGB edit made — cross-paper structural change, surfaced for owner).
**File:** [`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/NormalForms.lean`](https://github.com/litlfred/qou/blob/claude/exciting-lamport-p3b7bz/content/unital-groebner-bases/lean/UGB/GrobnerShirshov/NormalForms.lean)
**(b) structural exclusion** (per AGENTS.md "Before declaring refuted/ruled out"): backed by an
explicit infinite descending chain — a proved invariant, not a failed numerical probe.

## The claim

```lean
def lexLt : Monomial SU2Gen → Monomial SU2Gen → Prop
  | [], []            => False
  | [], (_ :: _)      => True            -- [] < any nonempty word
  | (_ :: _), []      => False
  | (a :: as), (b :: bs) =>
    a.rank < b.rank ∨ (a.rank = b.rank ∧ lexLt as bs)

theorem lexLt_wf : WellFounded lexLt :=          -- NormalForms.lean:281
  Subrelation.wf (fun {a b} h => lexLt_implies_listLex a b h) (sorry)   -- ← the sorry
```

The `sorry` is asked to supply `WellFounded (List.Lex rankRel)`. The TODO comment reads
*"replace sorry with correct Lean 4.24 API name for List.Lex WF."* **No such lemma exists,
because the statement is false.**

## Why it is false (the counterexample)

`lexLt` is the **pure** lexicographic order with `[] < (_ :: _)` (the empty word is the
minimum). On words of unbounded length over an alphabet with ≥ 2 distinct ranks it admits an
infinite descending chain. With `g0.rank = 0`, `g1.rank = 1` (the `SU2Gen` ranks are
`E_- < K⁻¹ < K < E_+`, i.e. `0,1,2,3`):

```
[g1]  >  [g0, g1]  >  [g0, g0, g1]  >  [g0, g0, g0, g1]  >  …
```

Each step is `lexLt xₖ₊₁ xₖ`: prepending `g0` (rank 0) before a common suffix, the first
differing letter is `0 < 1`, so the longer word is strictly *smaller*. This descends forever
⇒ `lexLt` is **not** well-founded. (Equivalently: `List.Lex rankRel` itself is not
well-founded — `[1] > [0,1] > [0,0,1] > …` — which is why `exact?` finds no
`WellFounded r → WellFounded (List.Lex r)` lemma in Mathlib: it would be unsound.)

This is the textbook reason Gröbner–Shirshov computations use an **admissible** (well-founded)
order — degree-first — rather than pure lex.

## Impact: contained (the orphan is unused)

`lexLt_wf` is referenced in exactly two places, neither a proof term:

1. its own definition (`NormalForms.lean:281`);
2. a comment in `AlgOps.lean:286` (*"itself currently sorrys at `lexLt_wf` for the same reason"*).

The well-founded order the package actually relies on is **`degLexLt`** (degree-first, then lex
among equal-length words), whose `degLexLt_wf` is **proved sorry-free** via
`InvImage.wf … (Nat.lt_wfRel.wf.prod_lex Nat.lt_wfRel.wf)` on `(length, lexEncoding)`
(`NormalForms.lean:287–297`); the `WellFoundedRelation` instance uses `degLexLt_wf`
(`:349`). So no live proof rests on the false `lexLt_wf`.

The narrower true fact (pure lex restricted to **equal-length** words *is* well-founded) is
already captured inside `degLexLt_wf` via the `Prod.Lex` on `(length, encoding)`.

## Recommended disposition (owner call — UGB is a separate paper)

One of:

- **Delete `lexLt_wf`** — it is unused and false; removing it costs nothing and the sorry count
  drops by one honestly. The `lexLt` *definition* stays (it is the legitimate tiebreaker used by
  `degLexLt`); only the false standalone WF theorem goes.
- **Restate honestly** — replace it with `lexLt_not_wf : ¬ WellFounded lexLt` (provable by the
  chain above) plus a pointer to `degLexLt_wf` as the admissible order. This turns a latent
  false-sorry into a true, documented negative.

Either way, update the `AlgOps.lean:286` comment, which currently implies `lexLt_wf` is a
fillable gap "for the same reason" as a genuine termination sorry — it is not; it is unfillable.

No edit is made here: the change lives in the `ugb` package (a different paper) and removing a
declared theorem is a structural change. Surfaced for the owner per AGENTS.md
("surface contradictions rather than proceeding").

## Method

Static read of `NormalForms.lean`; Mathlib `exact?` on
`WellFounded r → WellFounded (List.Lex r)` (no hit — the lemma is unsound); hand-verified
infinite descending chain; `grep lexLt_wf` across `content/unital-groebner-bases` (2 hits, both
non-proof).
