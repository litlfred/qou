---
# qou-l8az
title: 'Step 1: ExactPairing (X⊗Y) (Yᘁ⊗Xᘁ) — Mathlib Future-work entry, not done'
status: completed
type: task
priority: normal
created_at: 2026-08-26T18:00:27Z
updated_at: 2026-08-26T20:06:55Z
---


## Status 2026-08-26: construction FOUND and verified to elaborate; the snake is NOT proved

### What is settled (real progress, do not redo)

The coevaluation and evaluation formulas are correct and TYPECHECK against the
required signatures:

    coevaluation' := eta_X (X) (X2) tensorcomp X <| eta_Y (Y) (Y2) |> X2 tensorcomp id
    evaluation'   := id tensorcomp Y2 <| eps_X (X) (X2) |> Y tensorcomp eps_Y (Y) (Y2)

i.e. in Lean notation
    coevaluation' := eta_ X X' ⊗≫ X ◁ eta_ Y Y' ▷ X' ⊗≫ 𝟙 _
    evaluation'   := 𝟙 _ ⊗≫ Y' ◁ eps_ X X' ▷ Y ⊗≫ eps_ Y Y'

Both were checked standalone against
    𝟙_C ⟶ (X ⊗ Y) ⊗ (Y' ⊗ X')   and   (Y' ⊗ X') ⊗ (X ⊗ Y) ⟶ 𝟙_C
and elaborate clean. So the DEFINITION is not the open part.

### What is open

Both ExactPairing snake fields. Neither is dischargeable by the autoparam.

RULED OUT (each run, each fails):
  cat_disch (the class's own autoparam), simp, monoidal, aesop_cat,
  simp [monoidalComp], simp only [monoidalComp] + simp,
  + [whisker_exchange], + [<- whisker_exchange] (rw and simp forms), 6 variants.

### Diagnosis

monoidal handles associators and unitors ONLY. The missing step is the
INTERCHANGE law: the two snakes are NESTED (X2 from the dual pairs with X from
eta_X; Y2 pairs with Y), and moving eta_Y past eps_X on disjoint strands is
whisker_exchange, which monoidal does not apply and which simp does not place
correctly on its own.

So this needs a HAND-WRITTEN calc in Mathlib's own idiom -- the shape used by
exactPairingCongrLeft (Rigid/Basic.lean ~line 388) and
coevaluation_evaluation_braided' (Rigid/Braided.lean): normalise with monoidal
into ⊗≫ form until a literal `A ◁ g ≫ f ▷ B` pattern is exposed, rw
[whisker_exchange], monoidal again, repeat.

### Attempted intermediate that does NOT work

    Y' ◁ (X' ◁ eta_X ⊗≫ eps_X ▷ X') ⊗≫ (Y' ◁ eta_Y ⊗≫ eps_Y ▷ Y') ▷ X'

The decomposition is mathematically right -- it is the two component snakes,
each in coevaluation_evaluation'' form -- but `monoidal` cannot bridge the outer
composite to it, for the interchange reason above. An earlier version with
`▷ 𝟙_ C` appended failed differently, on MonoidalCoherence synthesis, because
its endpoints were wrong (𝟙_C instead of Y' ⊗ X').

### Honest cost estimate

This is a genuine string-diagram coherence proof of the kind Mathlib left on its
Future-work list. Comparable proofs in Rigid/Braided.lean run 20-30 lines of calc
with a Yang-Baxter/Whitney step. NOT the sixty-lines-of-mate-algebra shape that
closed rtqd and the drinfeldIso naturality -- I predicted in PR #5848 that this
one would be different, and so far it is.

### METHOD ERROR to avoid repeating

My first tactic battery reported "field 1 PASSED" on cat_disch. It had not. The
battery's success test keyed on WHICH FIELD the error message named, which tests
nothing -- an error naming field 2 is equally consistent with field 1 failing
first. Verified properly by putting `sorry` in field 2 and cat_disch in field 1:
field 1 fails. A pass/fail harness whose success condition is not the thing being
tested is worse than no harness.



## Update: 5 more routes ruled out; the goal is now GROUNDED (printed, not guessed)

Additionally ruled out, after expanding the whiskering with
whiskerLeft_comp / comp_whiskerRight first (so the individual eta/eps are
exposed rather than buried under `(A) <| (f >> g)`):
  + simp [whisker_exchange], + simp [<- whisker_exchange], + monoidal,
  and two mixed simp-set variants. Eleven automated placements total now fail.

### The precise obstruction, from the PRINTED goal

The composite fires in the order  eta_X, eta_Y, eps_X, eps_Y.

Neither snake is CONTIGUOUS in that order. The X-snake needs eta_X adjacent to
eps_X; eta_Y sits between them. So:
  - `monoidal` can never reach the two-snakes intermediate, because reordering
    eta_Y past eps_X is the INTERCHANGE law, not coherence. That is why my first
    calc step failed every time -- the intermediate was correct mathematics and
    unreachable by the tactic I kept aiming at it.
  - `simp [whisker_exchange]` does not place the exchange either: it needs to
    fire at one specific subterm, and simp either does not match it or loops
    over the symmetric rewrite.

### What would actually work (not attempted -- out of budget this pass)

Transcribe the idiom of `coevaluation_evaluation_braided'` (Rigid/Braided.lean)
line by line rather than guessing calc shapes. Its distinguishing features,
which none of my attempts had:
  - `𝟙 X ⊗≫ ... ⊗≫ 𝟙 X` padding at BOTH ends of every calc term
  - explicit parenthesisation of the interesting middle
  - `congr 3` to isolate that middle before rewriting
  - `repeat rw [<- assoc]` / `iterate n rw [...]` to drive the rewrite to the
    right position
Estimate: 20-30 lines of calc, an hour or more, genuine chance of success but
no guarantee. This is the same genre as the proof being transcribed.

### On literature

NOT the blocker. The statement is textbook and the diagram is unambiguous --
X2 pairs with the X from eta_X, Y2 with the Y from eta_Y, nested. No paper will
supply the Lean bookkeeping, which is the entire difficulty. If any external
source helps it is another FORMALISATION (a Lean or Coq library that already has
rigid-monoidal tensor duals), not a mathematics paper.



## BREAKTHROUGH on the calc shape (2026-08-26, later pass)

**Step 1 of the Mathlib-idiom calc WORKS.** This is what every earlier attempt
lacked, and it is durable -- do not rediscover it:

    calc _ = 𝟙 _ ⊗≫ (Y2 ⊗ X2) ◁ eta_ X X2
            ⊗≫ ((Y2 ⊗ X2) ◁ (X ◁ eta_ Y Y2 ▷ X2) ⊗≫ (Y2 ◁ eps_ X X2 ▷ Y) ▷ (Y2 ⊗ X2))
            ⊗≫ eps_ Y Y2 ▷ (Y2 ⊗ X2) ⊗≫ 𝟙 _ := by monoidal

`monoidal` closes that step, exit 0. So the outer coherence is SOLVED and the
whole problem is now localised to the parenthesised middle.

The features that made it work, absent from my earlier attempts:
  - `𝟙 _ ⊗≫ ... ⊗≫ 𝟙 _` padding at BOTH ends
  - the interesting part explicitly parenthesised as one ⊗≫ group
  - whiskerings written in the compound form the goal actually has
These are exactly the idiom of coevaluation_evaluation_braided'.

## What middle' should be (derived, not yet type-checked)

Doing eps_X FIRST and then eta_Y, the strands say:
  eps_X consumes X2 (from the dual) and X (from eta_X), leaving eta_X's X2.
  eta_Y must then create Y ⊗ Y2 BETWEEN Y2 and X2.
So the exchanged middle should be, up to bracketing:

    (Y2 ◁ eps_ X X2 ▷ X2) ⊗≫ (Y2 ◁ eta_ Y Y2 ▷ X2)

## Still failing

5 more routes, now from the padded base: rw/simp with whisker_exchange given
EXPLICIT arguments `(Y2 ◁ eps_ X X2) (eta_ Y Y2)` in both directions, and
simp with both snake ''-forms. The explicit args do not match the actual
subterm shape -- the terms carry compound whiskerings, so the bare
`W ◁ g ≫ f ▷ Z` pattern is not literally present.

Total ruled out: ~23 automated placements across 5 batteries.

## Next concrete step

Write middle' out explicitly as the second calc step's target and let the
ELABORATOR check the endpoints -- a small goal with fast feedback -- rather
than guessing whole-proof tactics. Then prove middle = middle' on its own.



## REDUCED TO ONE LEMMA — skeleton verified, exchange open (2026-08-26, final pass)

Steps 1, 3 and 4 of the calc are PROVED. The whole tensor-dual snake now rests
on a single interchange step. Verified end to end with only that step sorry'd:
`lean` exit 0, one `declaration uses 'sorry'` warning and nothing else.

### The working skeleton — copy this, do not re-derive it

    calc _ = 𝟙 _ ⊗≫ (Y2 ⊗ X2) ◁ eta_ X X2
            ⊗≫ ((Y2 ⊗ X2) ◁ (X ◁ eta_ Y Y2 |> X2) ⊗≫ (Y2 ◁ eps_ X X2 |> Y) |> (Y2 ⊗ X2))
            ⊗≫ eps_ Y Y2 |> (Y2 ⊗ X2) ⊗≫ 𝟙 _ := by monoidal          -- PROVED
      _ = 𝟙 _ ⊗≫ (Y2 ⊗ X2) ◁ eta_ X X2
            ⊗≫ (Y2 ◁ eps_ X X2 |> X2 ⊗≫ Y2 ◁ eta_ Y Y2 |> X2)
            ⊗≫ eps_ Y Y2 |> (Y2 ⊗ X2) ⊗≫ 𝟙 _ := by
            sorry                                                      -- THE ONLY GAP
      _ = 𝟙 _ ⊗≫ Y2 ◁ (X2 ◁ eta_ X X2 ⊗≫ eps_ X X2 |> X2)
            ⊗≫ (Y2 ◁ eta_ Y Y2 ⊗≫ eps_ Y Y2 |> Y2) |> X2 ⊗≫ 𝟙 _ := by monoidal   -- PROVED
      _ = _ := by
            rw [ExactPairing.coevaluation_evaluation'',
                ExactPairing.coevaluation_evaluation'']
            monoidal                                                   -- PROVED

(`|>` above is the whiskerRight triangle; `◁` is whiskerLeft. Written this way
because the real glyph does not survive every tool path.)

### What the one gap is

Exactly the INTERCHANGE: move `eta_Y` before `eps_X`. They act on disjoint
strands -- eps_X consumes X2 (from the dual) and X (from eta_X); eta_Y creates
Y ⊗ Y2 -- so it is true, and it is `whisker_exchange` morally. Both sides
TYPE-CHECK (four bracketings of the exchanged middle were checked and all four
elaborate), so the statement is right; only the placement is missing.

### Ruled out for this ONE step (all run, all fail)

congr 1 / congr 2 / congr 3; simp only [monoidalComp] then rw whisker_exchange
in both directions; congr 1 followed by either; simp [monoidalComp,
whisker_exchange]; monoidal; whisker_exchange with EXPLICIT arguments
(Y2 ◁ eps_ X X2) (eta_ Y Y2) in both directions; and the tensorHom
formulation -- simp/rw with tensorHom_def and tensorHom_def' in four
combinations, which is the natural spelling of interchange and the most
promising of the lot.

Roughly 35 automated placements across 8 batteries now excluded.

### The next thing to try (not attempted)

Two more calc steps INSIDE step 2, regrouping each side until a literal
`W ◁ g ≫ f |> Z` appears with no compound whiskering around it -- that bare
pattern is what whisker_exchange matches and what the compound forms hide.
This is the same move that made step 1 work; it was not applied to step 2.

### Standing note

No Lean committed. A sorry in the repo would assert this is one lemma away --
which is now TRUE and precisely located, but the strict discipline is that the
repo carries no sorry, and a bean carries the skeleton instead.



## CLOSED 2026-08-26 — both snakes PROVED, Mathlib Future-work entry 1 supplied

QOU/MathlibExt/RigidTensorDual.lean: tensorExactPairing, sorry-free, axioms
clean. Also hasRightDualTensor and tensorRightDualIso (`(X tensor Y)dual iso
Ydual tensor Xdual`), so qou-9m7v (step 2) is closed in the same file.

### What finally worked

The move that unlocked step 1 of the calc, applied AGAIN inside the exchange
step -- which is precisely what my earlier passes never did:

  regroup until a BARE `W <| g >> f |> Z` appears with NO compound whiskering
  around it. That bare shape is what whisker_exchange matches; the compound
  forms hide it.

Snake 1 needed one extra regrouping to expose it; snake 2 needed the mirrored
form and `whisker_exchange` in the same direction (the composite runs
f-then-g there rather than g-then-f, so the rewrite lands on the other side).

Full proofs are in the file. ~35 automated placements had been ruled out first;
none of them would ever have worked, because the pattern was not present to
match until the regrouping exposed it.

### Non-vacuity

Mutation: declaring the pairing against the WRONG dual order (X' tensor Y'
instead of Y' tensor X') fails to compile. So the order-reversal is load-bearing
and this is not an accident of coherence.
