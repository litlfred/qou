---
# qou-v2om
title: 'EPIC: close the low-isotope binding defect — five fronts, formalize-first'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-26T03:37:39Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-10v9
---

Owner picked "try all 5, prioritize what is formalized and provable first"
(2026-08-26). Five fronts dispatched in parallel, ordered by formalizability.

## The reframing that produced the fronts

**The low-isotope defect is NOT one defect.** Against the complete-graph
pairwise MAXIMUM `B_allpairs` (`K_A`):

    3H 0.945    4He 1.647    6Li 0.743    7Li 0.639     (B_AME / B_allpairs)

Too strong at A=2 and A=6,7; too weak at A=4. A scale error is monotone; this
is not. Corroborated by the plateau comparison (4He +10.5%, 6Li/9Be -25%) --
the alpha-cluster signature.

**And the residual changes sign:** `R(2H) = -0.61`, every other isotope
positive. This morning's Faddeev-Niemi sum-of-squares argument proved a
non-negative functional cannot equal a sign-changing target, and that
generalises beyond FN to ANY correction non-negative for all A. **So no
positive additive term can fix 4He while 2H overshoots by 27%.** F1 is
therefore logically prior to F2/F3/F4, not merely cheapest.

## The five, in dispatch order (formalize-first)

| bean | front | why this rank |
|---|---|---|
| `qou-39bx` | F1 deuteron overshoot | primary task is a LEAN STATEMENT (is `B_sym(2H)` parameter-free?), and it gates the others |
| `qou-09e0` | F5 indexing | pure Lean/algebra; target just narrowed to "a second central element in `F_1`" |
| `qou-o37w` | F4 derive `R(q,x)` | formalize-first by construction -- a derived target exists in `BindingEigenfunctionTwoTier` |
| `qou-hh9q` | F2 the n=3 term | semi-formal: is n=3 FORCED by the two derived anchors? 3 points, 2 anchors, 1 unknown |
| `qou-52x7` | F3 cluster substructure | least formal, highest fit hazard -- dispatched WITH a mandatory pre-registration step |

## Guards carried into the briefs

- F3 must commit a pre-registration (criteria + scheme count) BEFORE computing,
  on the FN template that worked today.
- F4 is warned that the `[n]_q^2` 6.9% near-miss is a TRAP, and that a tuned
  recursion is the banned seventh Delta_lambda ansatz.
- F2 is warned that fitting n=3 to A=3 data is circular -- the question is
  whether n=3 is FORCED, not whether a working value exists.
- F5 is warned that a win supplies the INDEX, not the magnitude (which is a
  Seiberg-Witten period), and must get the quantifier right: "no filtration
  DEFINABLE FROM THE GS DATA", not "no filtration" -- one exists trivially.
- F1 is told that if `L_pn` provably cannot hit the deuteron without moving the
  CAL-2-locked alpha, that is a scope-(b) exclusion of the whole `B_sym`
  construction.

## Already closed this session, do not re-attack

- Single global topological charge functionals (FN, scope-(b), sign + shape).
- All three `J^bullet` readings (`qou-wjbd`, PR #5812).



## Reorganisation 2026-10-04

Now the epic for P1.BIND under PROGRAM: L2 at 1 ppQ (mass and binding accuracy).

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

- **Round 87 (`https://github.com/litlfred/qou/pull/8401`, head `e8b8112ae090b9f21e8140c9696e25d7da0297c6`)**: Formalized theorem + 80-dps witness (`status: in-progress`).
