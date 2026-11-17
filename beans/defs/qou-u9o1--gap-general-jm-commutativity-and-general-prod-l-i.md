---
# qou-u9o1
title: 'GAP: general JM commutativity and general prod L_i = Delta^2 (adjacent case is the blocker)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T22:13:51Z
updated_at: 2026-11-17T06:22:00Z
parent: qou-rtxm
---

## Where this stands after PR (HeckeJucysMurphyElements.lean)

The `JucysMurphySpectrum` assumption in `KeystoneJucysMurphyTwist.lean` bundles TWO
independent facts. They are now separated, and only one has a demonstrated route.

### STRUCTURAL half — route demonstrated, not finished

`HeckeGenerators` is the type-A presentation (braid + Hecke relations). Assuming it
is "let A be a Hecke algebra" — a definition, not a world-claim — so it is not the
axiomatization the anti-laundering rule targets.

PROVED from that presentation:

- `jmRaw_closed_two`  L_2 = (q - q^-1) sigma_0 + 1     [Hecke relation]
- `jmRaw_prod_two`    L_1 L_2 = Delta^2 at n=2
- `jmRaw_prod_three`  L_1 L_2 L_3 = Delta^2 at n=3     [BRAID RELATION ONLY]
- `jm_prod_three`     the q-normalized form: q^-3 . Delta^2, and 3 = c([3])
- `sigma_comm_jmRaw_one`  far-commutation of sigma_j past L_2 for j >= 2

The n=3 proof is one braid application on the middle three letters of
`sigma_0 sigma_0 sigma_1 sigma_0 sigma_0 sigma_1`. Worth recording because I nearly
got the CONVENTION wrong: `prod L_i = Delta^2` holds ON THE NOSE only for the
UNNORMALIZED recursion `L_{i+1} = sigma_i L_i sigma_i`. With the q^-1 convention the
product picks up `q^{-n(n-1)/2}` — which is `c([n])`, the same triangular number the
twist arc uses. Do not quote one convention's identity under the other's name.

### OPEN — this bean

1. **General `prod_{i<n} L_i = Delta^2`.** n=2 and n=3 only. The induction step needs
   `L_i` to commute past the newly-introduced generator; n=3 is the first genuine
   instance of that, not a corollary of a finished argument.
2. **General commutativity `L_i L_j = L_j L_i`.** The FAR case is easy
   (`sigma_comm_jmRaw_one` is its first instance). The ADJACENT case is the classical
   hard one and is the actual blocker.

### OPEN — separate, larger, NOT this bean

3. **The SPECTRAL half**: that `L_i` acts on the seminormal basis with eigenvalue
   `q^{2.content}`. Untouched. Needs Young's seminormal form, which the corpus does not
   carry and Mathlib does not have. This is the half that actually discharges
   `JucysMurphySpectrum`, and it is much larger than 1+2.

**Do not read the n=3 result as "prod L_i = Delta^2 is proved."** It is proved at two
values of n. The honest summary is that the structural half now has a demonstrated
proof route in Lean and the spectral half does not exist yet.

Lit is available and is NOT the blocker: `library/hecke-alg`, plus
`arxiv-math-0411647v2` and `arxiv-2607.03827v1`. The mathematics is standard; the gap
is formalization effort.


## 2026-08-24 second pass — the adjacent case is REDUCED, not closed

New file `HeckeJucysMurphyCommutation.lean`, sorry-free, lean-direct exit 0, axioms
clean on all five theorems.

### Proved, general in i (not instances)

    sigma_mul_jm_succ    sigma_i . L_{i+1} = h.L_{i+1} + L_i . sigma_i
    jm_succ_mul_sigma    L_{i+1} . sigma_i = h.L_{i+1} + sigma_i . L_i
    sigma_comm_add       sigma_i commutes with (L_i + L_{i+1})          <-- classical
    sigma_mul_jm_prod    sigma_i (L_i L_{i+1}) = (L_{i+1} L_i) sigma_i
    jmRaw_comm_sigma_far sigma_j L_i = L_i sigma_j  for j > i           <-- general far case

The two exchange relations are each ONE application of the Hecke relation, and they
carry the SAME h.L_{i+1} term — which is why it cancels in the SUM. That is the whole
content of `sigma_comm_add`, the classical "sigma_i commutes with symmetric functions
of the adjacent JM pair".

### Why the adjacent case did NOT fall, recorded so the next attempt does not redo it

Set u := L_i.sigma_i and v := sigma_i.L_i. The exchange relations give

    u = (sigma_i - h) L_{i+1}          v = L_{i+1} (sigma_i - h)

and then L_i L_{i+1} = u^2 while L_{i+1} L_i = v^2. So the goal becomes

    (sigma_i - h) w  =  w (sigma_i - h),   w := L_{i+1} (sigma_i - h) L_{i+1}

i.e. it reduces to ANOTHER commutation of the same shape, not to anything proved.
**The sum is reachable from these relations; the product is not.** Anyone attacking
this again should start from the hook-word form of L_i and the braid relation, not
from the exchange relations — they are exhausted.

`sigma_mul_jm_prod` has an ORDER SWAP on the right and is NOT commutation. It becomes
commutation exactly when L_i, L_{i+1} commute, i.e. it is equivalent to the open
problem, not progress past it. Do not cite it as though sigma_i commutes with the
product.

### A wrong statement the compiler caught

I first stated far-commutation as `i <= j`. That is FALSE: `jmRaw H i` is a word in
sigma_0..sigma_{i-1}, so at j = i the generator is ADJACENT to the outermost letter
and `far` does not apply. The correct hypothesis is `i < j` strictly, and the excluded
boundary j = i is precisely the open adjacent case. Worth recording because the wrong
version looks more general and would have been quoted as covering the adjacent case.

### Status of the general-lambda derivation — UNCHANGED

Still conditional. Two things remain, and neither is closed by this file:

1. adjacent commutativity (above), hence general `prod L_i = Delta^2` (still n=2,3 only);
2. the SPECTRAL half — that L_i acts on the seminormal basis by q^{2.content}.

(2) is the larger and is what actually discharges `JucysMurphySpectrum`. Nothing in
this pass touches it.


## Third pass — adjacent commutativity has a FIRST INSTANCE, via a different route

Added to the same file. All sorry-free, axioms clean.

    jmRaw_hook              L_k = (s_{k-1}...s_1) s_0^2 (s_1...s_{k-1}), k >= 1
    fullTwist3_symm         (s_0 s_1)^3 = (s_1 s_0)^3
    jmRaw_two_mul_one       L_3 L_2 = (s_1 s_0)^3
    jmRaw_comm_adjacent_one L_2 L_3 = L_3 L_2                <-- ADJACENT, i=1

**The route is NOT the one the exchange relations suggest.** It goes through the
HALF-twist: `Delta = s_0 s_1 s_0 = s_1 s_0 s_1` by the braid relation, and both
`(s_0 s_1)^3` and `(s_1 s_0)^3` group into `Delta . Delta`. So L_2 L_3 and L_3 L_2 are
the full twist approached from opposite sides, and the half-twist symmetry identifies
them.

**Why this does NOT generalise, stated so nobody assumes it does.** At i=1 both
products are THE WHOLE full twist of B_3, which is what makes the half-twist argument
close. For i >= 2 the products L_i L_{i+1} are proper sub-words of a larger twist and
the argument has nothing to bite on. So this is one instance, not an induction base
with a visible step.

The hook-word form is now available (`jmRaw_hook`) as the tool for a real attack: it
exhibits L_k as a palindrome around s_0^2 and makes the letter set explicit.

### Still open

1. General adjacent commutativity (i >= 2). Exchange relations exhausted; half-twist
   argument does not extend; hook-word route now available but untried.
2. General `prod L_i = Delta^2` — still n=2,3.
3. The SPECTRAL half, untouched, and still the larger of the two.


## 2026-08-25 — the problem is now ONE-PARAMETER, and the spectral base case is forced

### The reduction (HeckeJucysMurphyReduction.lean)

    jmRaw_commutator_step        [L_i, L_{j+1}] = s_j [L_i, L_j] s_j    for j > i
    jmRaw_comm_of_adjacent       adjacent at i  =>  L_i commutes with every L_j, j >= i
    jmRaw_one_comm_all           L_2 commutes with EVERY L_j            <-- full row
    jmRaw_comm_all_of_all_adjacent   all adjacent => fully commutative

`L_{j+1} = s_j L_j s_j` and L_i slides past both copies of s_j when j > i
(far-commutation, already proved). So a FAR commutator is a CONJUGATE of the one a
step closer — no cancellation, no Hecke relation needed. Iterating down to j = i+1:

    [L_i, L_j] = 0 for all j > i   <=>   [L_i, L_{i+1}] = 0

**The adjacent case is not merely the hard case, it is the ONLY case.** Everything
else is conjugation. This collapses a two-parameter problem to one parameter, and it
upgrades the earlier single instance: with `jmRaw_comm_adjacent_one` fed in, the whole
i=1 ROW is now proved, not one entry.

Caveat that matters: the reduction relates different j at FIXED i. It gives no
purchase on varying i, so it does not touch i >= 2.

### The spectral half, started (StandardTableauSpectral.lean)

    mem_cells_pred_row      Young diagrams are closed upward in a column
    StandardTableau         bijection + row/column increasing conditions
    .sum_content            sum_content_of_equiv still applies to standard ones
    .zero_row / .zero_at_corner   entry 0 sits at (0,0)
    .zero_content           hence its content is 0

**Why a bijection was not enough.** `KeystoneJucysMurphyTwist` models a tableau as a
bare bijection `Fin n = cells l`. That is exactly right for `sum_content_of_equiv`
(reindexing works for ANY bijection) but too weak for the spectral statement, which
holds for STANDARD tableaux only. The seminormal representation is built on those.

**The base case is FORCED, not chosen.** The spectral rule says L_i has eigenvalue
q^{2.content(cell of i)}. At i=0 the recursion gives L_1 = 1, so the rule is only
consistent if entry 0 has content 0. `zero_at_corner` proves entry 0 is at (0,0)
exactly — from standardness plus the partition shape — so content = 0 and q^0 = 1.
That is a consistency check on the assumed rule, discharged rather than assumed.

### Still open

1. adjacent commutativity for i >= 2 — now the ONLY commutativity question;
2. general prod L_i = Delta^2 (still n=2,3);
3. the spectral half at general i — the seminormal representation itself, still absent.

The general-lambda twist remains CONDITIONAL. (3) is still the largest item.


## 2026-08-25 — the adjacent case is ONE word identity; the seminormal build has a first prerequisite

### i >= 2: normal forms (HeckeJucysMurphyAdjacentNormalForm.lean)

With u := sigma_k, v := sigma_{k+1}, N := L_k:

    jmRaw_adjacent_left    L_{k+1} L_{k+2} = (uv) N (uv) N (uv)
    jmRaw_adjacent_right   L_{k+2} L_{k+1} = (uvu) N (uv) N u

TWO rewrites each — one braid (uvu = vuv), one commutation of N past v. The Hecke
relation is not used.

**Why this is progress and not restatement.** Every previous attempt unfolded the
recursion and regenerated a commutator of the same shape (see the exchange-relation
dead end above). Here N appears twice and OPAQUELY. Both sides start with uv, so
after cancelling that unit the question is

    N (uv) N (uv)  =?=  u N (uv) N u

for an arbitrary N commuting with v — one word identity in ONE unknown, no recursion
left. That is the shape a future attack should work on.

Consistency checked at k=0: N=1 collapses the forms to (s0 s1)^3 and
(s0 s1 s0)(s0 s1) s0, exactly the words jmRaw_prod_three / jmRaw_two_mul_one identify
and fullTwist3_symm equates. So jmRaw_comm_adjacent_one is the N=1 specialisation —
the general forms are consistent with the one known case.

### Seminormal build: axial distance (StandardTableauAxialDistance.lean)

The seminormal action of sigma_i has the axial distance between the cells of i and
i+1 in a DENOMINATOR, so the representation is not even well-posed until that
distance is known nonzero.

    mem_cells_of_le_col   diagrams are closed leftward in a row
    diag_gap              entry(r+1,c+1) >= entry(r,c) + 2
    not_consecutive_diag  i and i+1 are never at (r,c) and (r+1,c+1)
    cellContent_diag_step content(r+1,c+1) = content(r,c)

**The "two" is the whole point.** A one-step chain gives only `<`, which would still
permit consecutive entries on a diagonal. The gain of two comes from the INTERMEDIATE
cell (r,c+1) — a cell whenever (r+1,c+1) is, since rows are weakly decreasing — whose
entry is strictly between. Combined with cellContent_diag_step, this is exactly
"axial distance 0 cannot occur between consecutive entries", i.e. the d=1 case, and
the case the denominators actually hit.

### Still open

1. the word identity above — adjacent commutativity at k >= 1;
2. general prod L_i = Delta^2 (n=2,3 only);
3. the seminormal representation itself: the d >= 2 diagonal case, the action of
   sigma_i, and the L_i eigenvalue q^{2.content}. Still the largest item.

JucysMurphySpectrum is untouched; the general-lambda twist stays CONDITIONAL.


## CORRECTION to the entry above — "arbitrary N" is REFUTED

I wrote that the reduced identity is a question "for an arbitrary N commuting with v".
**That is false, and I am correcting it within the hour.**

If it held for any such N, JM commutativity would follow from almost nothing — which
should have been the tell for a theorem this hard.

Measured: take N = v, which certainly commutes with v. In the 2-dim irrep of H_3(q)
at q = 2, exact `fractions.Fraction` arithmetic, the two normal forms DIFFER — both
in the uncancelled and the cancelled shape.

    computations/hecke/jm_adjacent_generic_N_counterexample.py

So adjacent commutativity genuinely needs L_k's STRUCTURE, not merely its commutation
with v. **An attack assuming only the latter cannot work** — which is worth more to a
future attempt than the wrong generalisation was.

### The control caught my own harness bug, and that is the transferable lesson

The first version of the script reported `N = 1` FALSE — a case Lean PROVES. The
script was comparing the UNCANCELLED left form against the CANCELLED right form.
Without the N = 1 control I would have "refuted" the k=0 case that is already a
theorem, and drawn the opposite conclusion with equal confidence.

**Any probe testing a claimed identity must include a case whose answer is already
known.** A probe with no control measures itself.


## Next lead — what L_k has that the counterexample lacks (HYPOTHESIS, UNTESTED)

The refutation says "commutes with v" is insufficient. So what is the extra
structure? Two candidates, neither tested — recording them as leads, NOT findings:

1. **Palindromicity.** `jmRaw_hook` gives `L_k = (s_{k-1}..s_1) s_0^2 (s_1..s_{k-1})` —
   a palindrome around `s_0^2`. The counterexample `N = v` is a single letter, trivially
   palindromic, so palindromicity ALONE is probably not enough either. But `L_k` is a
   palindrome whose CENTRE is a square, which `v` is not.

2. **The recursion.** `L_k = s_{k-1} L_{k-1} s_{k-1}`, so an induction on k is available:
   at step k the unknown N is itself `w M w` with `w = s_{k-1}`, `M = L_{k-1}`, where
   `w` and `u = s_k` are ADJACENT (braid applies) and `w` and `v = s_{k+1}` are FAR
   (commute). That gives two more relations the counterexample cannot use, and is the
   route I would try first.

**How to test cheaply.** The 2-dim irrep of H_3 can only reach k = 0 — it has two
generators, so there is no room for the k = 1 adjacent pair. Testing k = 1 needs H_4
(3-dim standard irrep, or the 24-element regular representation built from the Hecke
multiplication table). Whoever does it: **keep a control case whose answer is known**,
per the harness bug recorded above.

Do not record either candidate as established without that measurement.


## Both leads above are REFUTED — measured in H_4, same session

`computations/hecke/jm_adjacent_h4_structure_probe.py`. Regular representation of
H_4(q) (24-dim, FAITHFUL — an irrep can hide nothing here), exact Fractions at q=2,
k=1 so u=s_1, v=s_2 and the true JM element is L_1 = s_0^2.

**CONTROL passes**: N = s_0^2, the real JM element, gives True — adjacent
commutativity at k=1 is a theorem and the harness reproduces it.

    True :  1,  s_0^2 (JM),  s_2^2,  s_0 s_2
    False:  s_0,  s_2,  s_1,  s_1^2,  (s_0 s_2)^2,  s_0^3,  s_0^4

### What died

* **Lead 1, "palindrome with a square centre"** — `s_1^2` is exactly that and FAILS.
* **"is a square"** — `(s_0 s_2)^2` and `s_0^4` are squares and FAIL.
* **"commutes with v"** — `s_0` and `s_2` both commute with v and both FAIL. This is an
  INDEPENDENT confirmation of the earlier H_3 2-dim-irrep refutation, by a different
  computation in a different algebra.

Lead 2 (the recursion) is untouched by this — it is a statement about how to run an
induction, not a property of N testable this way. It remains the only surviving route.

### NOT claimed

The True set {1, s_0^2, s_2^2, s_0 s_2} is small and suggestive. **Twelve points at one
q in one algebra is not a characterisation**, and fitting one would be the numerology
this repo forbids. Widen q and n before proposing anything.

### The harness bug recurred — third time, same class

An earlier version built the LEFT form uncancelled and the RIGHT form cancelled, and
reported False for every case INCLUDING the theorem. That is now twice in this session
(the H_3 script did the same). Both times the known-answer control was the only thing
that caught it. **A probe testing a claimed identity without a control case measures
itself.**


## Widened q and n — the k=1 pattern was an ARTIFACT, and the flip is now PROVED

`computations/hecke/jm_adjacent_widen_q_and_n.py`. Regular reps of H_4 and H_5
(faithful), exact Fractions, q in {2, 3, 5/2}, (n,k) in {(4,1), (5,2)}.

**CONTROL passes at k=2 as well** — N = L_2 = s_1 s_0 s_0 s_1 gives True. Adjacent
commutativity is now numerically verified at k=1 AND k=2; Lean has only the k=0 shape,
so k=2 is a genuinely new checked case.

1. **q-INDEPENDENT.** Identical at all three q. Structural, not arithmetic.
2. **k-DEPENDENT — this kills the k=1 "True set".**

       N = s_0     : FALSE at k=1,  TRUE at k=2
       N = s_0 s_j : TRUE  at k=1,  FALSE at k=2

   The set {1, s_0^2, s_2^2, s_0 s_2} recorded last turn is an ARTIFACT of k=1. It was
   explicitly not claimed as a characterisation; that restraint was correct.

3. **The flip has a PROVED explanation** — `jmRaw_adjacent_of_comm`, sorry-free:
   if N commutes with BOTH u = s_k and v = s_{k+1}, both normal forms collapse to
   N^2 (uvu)^2 and the identity follows from `braid_cube_eq` ((uv)^3 = (uvu)(uv)u,
   both sides being (uvu)^2). At k=2, s_0 commutes with s_2 and s_3; at k=1 it does
   not commute with s_1. Exactly the flip.

### The limit of that lemma, measured not guessed

**Sufficient, NOT necessary**: at k=2, N = s_3^2 satisfies the identity while NOT
commuting with u = s_2 (adjacent). And it does **not** apply to the case that matters —
`N = L_k` never commutes with `s_k`, because the hook word ends in `s_{k-1}`, which is
adjacent to `s_k`. That is precisely why the real case is hard, and why this lemma
explains the easy rows without touching the hard one.


## Lead 2 (the recursion) is REFUTED in its naive form — all recorded leads now dead

`computations/hecke/jm_adjacent_induction_step_probe.py`. H_5 regular rep (faithful),
exact Fractions, q=2, k=2 — so u=s_2, v=s_3, w=s_1, which is exactly the recursion's
geometry (w adjacent to u, far from v).

The obvious inductive step, given `L_k = w L_{k-1} w`, is

    "the identity holds for N"  =>  "it holds for w N w"

**It is FALSE:**

    N = 1      works;  wNw = s_1^2        works
    N = s_0    works;  wNw = s_1 s_0 s_1  FAILS
    N = s_0^2  works;  wNw = s_1 s_0^2 s_1 works   (= L_2, the CONTROL)
    N = s_3^2  works;  wNw = s_1 s_3^2 s_1 FAILS

So "satisfies the identity" is not preserved by N |-> wNw. **An induction whose
hypothesis is just the conclusion cannot work; the invariant must be strengthened.**

### Status of all leads

| lead | status |
|---|---|
| commutes with v | REFUTED (twice, two algebras) |
| palindrome, square centre | REFUTED (s_1^2) |
| is a square | REFUTED ((s_0s_2)^2, s_0^4) |
| commutes with BOTH u and v | PROVED SUFFICIENT, measured NOT necessary, and provably inapplicable to L_k |
| the recursion / induction on k | REFUTED in its naive form (this probe) |

Every lead recorded in this bean has now been tested. None survives as stated.

### NOT claimed

The step succeeded exactly for N = 1 = L_0 and N = s_0^2 = L_1 — both genuine JM
elements — and failed for the two non-JM inputs. That hints the invariant is "N is a
JM element" rather than "N satisfies the identity". **That is TWO points.** It is a
direction, not evidence; do not fit a characterisation to it. Widen first.

### Honest overall position

Adjacent commutativity at k >= 2 is verified numerically (k=1, k=2, three values of q)
but every proof route this session proposed has been measured and failed. The problem
is well-posed and well-isolated — one word identity, one unknown — and genuinely open.


## FOUND THE CLASSICAL PROOF — and my objects are NOT Mathas's JM elements

Source: `library/hecke-alg` (Mathas, *Iwahori-Hecke Algebras and Schur Algebras of the
Symmetric Group*), **Proposition 3.24**, p.30 of the PDF. The ingested `sections/*.md`
OCR is unusable (one char per line); `pypdf` extraction plus a de-mangling pass makes
it readable. **`pypdf` had to be pip-installed — it is not in the image.**

### Mathas's definition is ADDITIVE, mine is MULTIPLICATIVE

    Mathas:  L_k = q^-1 T_(k-1,k) + q^-2 T_(k-2,k) + ... + q^(1-k) T_(1,k),   L_1 = 0
             recursion:  L_k = q^-1 ( T_k + T_k L_{k-1} T_k )        <-- note the EXTRA +T_k
    Mine:    jmRaw(k+1) = sigma_k . jmRaw(k) . sigma_k,               jmRaw 0 = 1

**These are different elements.** Mine is the multiplicative analogue. They are affinely
related — at the first index, exactly:

    jmRaw 1 = T_1^2 = (q - q^-1) T_1 + 1,   Mathas L_2 = q^-1 T_1
    =>  jmRaw 1 = 1 + q(q - q^-1) L_2

(exact algebra from the Hecke relation, not a fit). If that affine form persists, the
two generate the same commutative subalgebra and commutativity transfers — consistent
with my numerics, which found my jmRaw DO commute at k=1 and k=2.

### Prop 3.24 in full — and what I had already re-derived

    (i)   T_i and L_k commute if i != k-1, k         <-- = my jmRaw_comm_sigma_far
    (ii)  T_i L_{i+1} = (q-1) L_{i+1} + 1 + L_i T_i
          T_i L_i     = T_i L_{i+1} - 1 - (q-1) L_{i+1}
                                                     <-- = my two exchange relations,
                                                         independently derived
    (iii) T_i commutes with  L_i L_{i+1}  AND  L_i + L_{i+1}
    (iv)  L_i and L_k commute

**(iii) is exactly where I stalled.** I proved the SUM case (`sigma_comm_add`) but for
the PRODUCT could only get `sigma_i (L_i L_{i+1}) = (L_{i+1} L_i) sigma_i` — with an
ORDER SWAP. Mathas asserts the product commutes outright, no swap, and (iv) follows
from (iii).

Mathas's proof note: *"the proofs of all of these statements follow easily using the
relations"* — he writes out only (i).

### The actionable redirection

The five refuted leads were all attempts to force commutativity of the MULTIPLICATIVE
objects directly. The classical route instead:

1. define the ADDITIVE L_k (sum of transpositions, L_1 = 0);
2. prove 3.24(i)-(iii) for those — (ii) is already in hand, transcribed;
3. get (iv) from (iii);
4. transfer to `jmRaw` via the affine relation.

That is a concrete plan with a citation, replacing "no candidate I would defend".

### NOT claimed

The affine relation is verified only at the first index. Whether
`jmRaw k = 1 + c_k L_{k+1}` holds generally is UNTESTED — check before relying on step 4.
Also: 3.25 states any symmetric polynomial in the L's is CENTRAL, which is a stronger
and possibly easier handle than (iv) directly.


## The additive family is BUILT — the sum half improves, the product half does NOT

`HeckeAdditiveJucysMurphy.lean`, sorry-free, exit 0, axioms clean on all five.

Built in THIS corpus's convention (sigma^2 = (q - q^-1)sigma + 1), NOT by transcribing
Mathas's coefficients — he works with T^2 = (q-1)T + q, so his constants are not ours.
Recursion form, with the normalisation `d` left FREE:

    A_0 = 0,   A_{k+1} = sigma_k A_k sigma_k + d . sigma_k

    addJM_sigma_left    sigma_k A_{k+1} = h.A_{k+1} + A_k sigma_k + d
    addJM_sigma_right   A_{k+1} sigma_k = h.A_{k+1} + sigma_k A_k + d
    addJM_sigma_comm_add   sigma_k commutes with A_k + A_{k+1}, FOR EVERY d
    addJM_sigma_prod_swap  sigma_k (A_k A_{k+1}) = (A_{k+1} A_k) sigma_k

### The gain

The two exchange relations differ ONLY by swapping `A_k sigma_k` and `sigma_k A_k`, so
those terms cancel in the SUM. Mathas 3.24(iii)'s sum half therefore holds with **no
constraint on d at all** — strictly cleaner than the multiplicative `sigma_comm_add`,
which needed the specific recursion.

### The obstruction SURVIVES the convention change — this is the real finding

3.24(iii) also asserts T_i commutes with the PRODUCT L_i L_{i+1}, and (iv) follows from
it. From the recursion alone one gets only the SWAPPED form, which is commutation
exactly when A_k, A_{k+1} already commute. **So (iii)-product and (iv) are entangled,
and the recursion does not separate them — in either convention.**

I had hoped the additive convention would rescue the product half. **It does not.** That
was the point of building it, and the negative is worth more than the hope was: it means
the remaining gap is NOT a convention artifact.

### Consequence for the next attempt

Mathas's "follows easily using the relations" must lean on the explicit
sum-of-transpositions expansion of L_k, which an ABSTRACT presentation does not provide
— `HeckeGenerators` has generators and relations, no transposition elements T_(i,k).
So the next step is not another convention or another invariant: it is either

  (a) add transposition elements T_(i,k) and the expansion to the presentation, or
  (b) work in a concrete model (regular representation) where they exist.

Do not try a sixth "what property of N" lead. That family is exhausted, and this file
shows why: the obstruction is structural, not conventional.


## ANSWER to "is Mathas wrong, or is there a better reference?"

**Mathas is NOT wrong.** My swapped identity is CONSISTENT with 3.24(iii) given (iv) —
the defect is provability ORDER, not correctness. Using (iii) to get (iv) is circular
for us because our derivation of (iii) already needs (iv).

**But there IS a better route, and it is in the same book at 3.25 rather than 3.24:
Jucys's CENTRALITY argument.**

    S_m := A_1 + ... + A_m ;   A_m = S_m - S_{m-1}

For i < m, every generator occurring in A_i is one that BOTH S_m and S_{m-1} commute
with, hence A_m commutes with A_i. **The product statement is never used.**

### Measured (jm_partial_sum_centrality_probe.py; H_5 regular rep, exact Fractions)

q in {2,3}, d in {1/2, 1/3, 1} — including d = 1, NOT Mathas's normalisation:

    S_m commutes with sigma_j for EVERY j != m

    m=1: Y n Y Y    m=2: Y Y n Y    m=3: Y Y Y n    m=4: Y Y Y Y

and the exception is explained exactly:

    sigma_j commutes with the INDIVIDUAL A_i except for i in {j, j+1}   (= 3.24(i))

At j = m the summation cutoff SPLITS the pair (A_m, A_{m+1}) — and that pair is exactly
what `addJM_sigma_comm_add` already handles. Every other term commutes individually.

### What it buys, and what it does not

BUYS: a NON-CIRCULAR route, d-independent, that never touches the product half. This is
the route to formalise.

DOES NOT BUY: it still needs 3.24(i) **in full**, and the `i >= j+2` half is NOT
provable from the recursion by induction — at i = j+2 the recursion introduces
sigma_{j+1}, adjacent to sigma_j, and commutation holds only by cancellation. Mathas
proves that case from the explicit transposition form ("T_{k+1} commutes with T_(j,k)").

**So the conclusion of `HeckeAdditiveJucysMurphy` is reinforced, not overturned**: the
missing ingredient is the sum-of-transpositions expansion. What changed is that we now
know WHICH argument to run once we have it — Jucys's centrality, not Mathas's 3.24(iii).

### Restating (a)/(b), which an earlier note referenced without defining

(a) add transposition elements T_(i,k) and their expansion to the `HeckeGenerators`
    presentation;
(b) drop the abstract presentation and work in a concrete model (regular representation)
    where those elements already exist.

(a) is now clearly preferable: the centrality route needs only the expansion, and gives
a general-n Lean proof. (b) would only ever verify fixed n.


## The transposition expansion is IN — and it needed no new axioms

`HeckeTranspositionExpansion.lean`, sorry-free, exit 0, axioms clean.

The missing ingredient identified two passes ago is supplied:

    transp H i (k+1) = sigma_k * transp H i k * sigma_k,   transp H k (k+1) = sigma_k
    addJM_eq_transp_sum :  A_k = d . SUM_{i<k} T_(i,k)

### Why this is a definition, not an axiomatisation

The tempting move was to add transposition elements to `HeckeGenerators` as new FIELDS with
defining relations — that would be an axiomatisation, exactly what the anti-laundering
rule targets. **It is unnecessary.** In a braid presentation the transposition element is a
CONJUGATE of a generator,

    T_(i,k) = sigma_{k-1} ... sigma_{i+1} . sigma_i . sigma_{i+1} ... sigma_{k-1}

which recursively is `T_(i,k+1) = sigma_k T_(i,k) sigma_k`. Built from what is already
there; nothing assumed. This is the difference between (a) done right and (a) done as a
laundering step.

### Coefficients are UNIFORM here, geometric in Mathas

With this corpus's recursion `A_{k+1} = sigma_k A_k sigma_k + d.sigma_k` the `d` sits on
the new term only, so every transposition carries the same `d`. Mathas puts `q^-1` OUTSIDE
both terms and gets geometric coefficients `q^-1, q^-2, ...`. **Different families** — the
expansion proved here is for the one this corpus actually uses, not a transcription.

Cross-checked numerically (H_5, exact Fractions): recursion == d.sum(transp) at k = 1..4.

### What it unlocks

Conjugating a transposition by sigma_j PERMUTES its index pair, so sigma_j fixes the sum
`SUM_{i<k} T_(i,k)` whenever j and j+1 both miss k — that is 3.24(i), which feeds partial-sum
centrality, which telescopes to commutativity. The route is now unblocked at its one
blocking step.

### NOT proved here

The conjugation-permutation law itself, hence not 3.24(i), not centrality, not
commutativity. This file supplies the object and its expansion only. JucysMurphySpectrum is
untouched; the general-lambda twist stays conditional.


## The PAIR-SWAP law is PROVED — 3.24(i)'s mechanism is in Lean

`sigma_comm_transp_pair` in `HeckeTranspositionExpansion.lean`, sorry-free, axioms clean:

    for i > j+1 :   sigma_j (T_(j,i) + T_(j+1,i)) = (T_(j,i) + T_(j+1,i)) sigma_j

### Why this is the right lemma

With the expansion `A_k = d . SUM_{l<k} T_(l,k)` in hand, "does sigma_j commute with A_k?"
becomes "does sigma_j fix that sum?". For i > j+1 exactly TWO terms can be disturbed —
l = j and l = j+1 — because i itself is out of sigma_j's reach. So the whole question
reduces to whether that PAIR is preserved.

Measured first (`jm_transposition_pair_swap_probe.py`, H_6 faithful, exact Fractions,
q in {2,3}): the pair commutes in EVERY case, each term ALONE never does. A genuine pair
phenomenon — which is exactly why a term-by-term approach fails and the sum is essential.

### The proof needs BOTH relations

Base case i = j+2, with u = sigma_j, v = sigma_{j+1}: one braid move reduces the claim to

    v u v^2 + u v  =  v^2 u v + v u

and only the HECKE relation v^2 = hv + 1 turns both sides into h.vuv + uv + vu. **Braid
alone does not close it.** The step i -> i+1 is pure far-commutation (sigma_j commutes with
sigma_i since i > j+1), with both transpositions gaining the same outer conjugation.

### Chain status

    expansion A_k = d.SUM T_(l,k)          DONE  (addJM_eq_transp_sum)
    pair-swap law                          DONE  (sigma_comm_transp_pair)
    3.24(i): sigma_j commutes with A_k     NEXT  -- split the sum into the pair + the rest
    partial-sum centrality                 then
    telescoping => commutativity           then

The next step is now bookkeeping over a Finset: terms with l outside {j, j+1} commute
individually by far-commutation, and the two exceptional terms are handled by the lemma just
proved. No new mathematical ingredient is needed for it.


## Both halves of 3.24(i)'s mechanism are now PROVED

Added to `HeckeTranspositionExpansion.lean` (8 declarations total, all sorry-free, axioms clean):

    sigma_comm_transp_far       sigma_m commutes with T_(l,i) when m > i
    sigma_comm_transp_base      sigma_j commutes with T_(l,j+2) for l < j   <- the hard case
    sigma_comm_transp_disjoint  sigma_j commutes with T_(l,i) for l < j, i > j+1

Measured first (H_6, exact Fractions): 24 disjoint pairs, all commuting, none failing.
Worth measuring because it is NOT letter-wise obvious — for l < j < j+1 < i the word for
T_(l,i) CONTAINS both sigma_j and sigma_{j+1}.

### The only hard case is i = j+2, and it has a two-line proof

Everything above i = j+2 is a plain induction: each step conjugates by sigma_{i-1} with
i-1 > j+1, which sigma_j commutes past by far-commutation. The base case does the work.

With u = sigma_j, v = sigma_{j+1}, X = T_(l,j) — and X commutes with v because every letter
of X has index <= j-1:

    u . vuXuv = (uvu) X uv = (vuv) X uv = vuX (vuv) = vuX (uvu) = vuXuv . u

**Two braid moves, nothing else.** Note the contrast with the pair-swap law, which genuinely
needed the HECKE relation: here braid alone suffices. The two halves of 3.24(i) have
different proof ingredients.

### Chain status

    expansion A_k = d.SUM T_(l,k)             DONE  addJM_eq_transp_sum
    pair-swap  (l in {j,j+1})                 DONE  sigma_comm_transp_pair       [braid+HECKE]
    disjoint   (l outside {j,j+1})            DONE  sigma_comm_transp_disjoint   [braid only]
    3.24(i): sigma_j commutes with A_k        NEXT  -- assemble: split the Finset sum
    partial-sum centrality                    then
    telescoping => commutativity              then

Both ingredients for the assembly now exist. The next step splits `SUM_{l<i} T_(l,i)` into
the two exceptional terms plus the rest, applying one lemma to each part. It is Finset
bookkeeping over a proved case analysis — no new mathematics.


## 3.24(i) AND Jucys's centrality are both PROVED

`HeckeTranspositionExpansion.lean` is now 15 declarations, all sorry-free, axioms clean.

    sigma_comm_transp_below     sigma_j commutes with T_(l,i) for l > j+1     [braid]
    sigma_comm_addJM            3.24(i) for i > j+1                          <-- ASSEMBLED
    sigma_comm_addJM_small      3.24(i) for i < j                            [braid]
    partialSum                  S_m = SUM_{i<=m} A_i
    sigma_comm_partialSum       j < m
    sigma_comm_partialSum_above j > m
    sigma_comm_partialSum_ne    **sigma_j commutes with S_m for every j != m**

### 3.24(i)'s assembly, and why the SUM was essential

Splitting `SUM_{l<i} T_(l,i)` on l:

    l < j          sigma_comm_transp_disjoint   braid
    l in {j,j+1}   sigma_comm_transp_pair       braid + HECKE   <-- AS A PAIR
    l > j+1        sigma_comm_transp_below      braid

The middle row cannot be done term by term — **neither T_(j,i) nor T_(j+1,i) commutes with
sigma_j alone** (measured, H_6). Only their sum does. So the expansion into a SUM was a
necessary ingredient, not a convenience: this is precisely where a term-by-term approach
had to fail, and it explains in retrospect why all five earlier "property of N" leads died.

### Centrality, and why the exception is at j = m exactly

Split `range(m+1)` the same way. For j < m the pair {j, j+1} is INSIDE the sum, so
`addJM_sigma_comm_add` covers it and every other index commutes alone. For j > m every index
is below j. At j = m the cutoff SPLITS the pair — which is exactly the measured exception,
now explained rather than observed.

### Chain status

    expansion                      DONE
    pair-swap / disjoint / below   DONE
    3.24(i)                        DONE  sigma_comm_addJM (+ _small)
    partial-sum centrality         DONE  sigma_comm_partialSum_ne
    telescoping => commutativity   NEXT

### What telescoping still needs

`A_m = S_m - S_{m-1}`, and for i < m both S_m and S_{m-1} must commute with A_i. Centrality
gives commutation with GENERATORS; lifting that to commutation with A_i needs "commutes with
every letter => commutes with the word", an induction over `transp`. Every letter of A_i has
index <= i-1 <= m-2, so it misses both m and m-1 and the hypotheses are available. That is
the one remaining step, and it is structural bookkeeping, not new mathematics.


## 2026-08-25 — COMMUTATIVITY IS PROVED. The blocker named in this bean's title is gone.

`QOU.BraidKnot.Hecke.jmRaw_comm` : `L_i L_k = L_k L_i`, all `i, k`, unconditionally.
Sorry-free, `#print axioms` clean. The adjacent case `[L_k, L_{k+1}] = 0` — the
"blocker" in the title, which five direct attacks on `jmRaw` failed to reach — falls
out with the rest. It was never adjacent-specific; it was a symptom of attacking the
wrong family.

### The chain, all landed on `claude/jm-adjacent-normal-forms-2026-08-25`

    transposition expansion  A_k = d * sum_{l<k} T_(l,k)       addJM_eq_transp_sum
    pair-swap law            sigma_j fixes T_(j,i)+T_(j+1,i)   sigma_comm_transp_pair
    disjoint / below / far   term-by-term commutation          three lemmas
    Mathas 3.24(i)           sigma_j commutes with A_i         sigma_comm_addJM
    Jucys centrality         sigma_j commutes with S_m, j!=m   sigma_comm_partialSum_ne
    word lifting             letters -> whole word             comm_addJM_of_comm_sigma
    telescoping              A_i A_{m+1} = A_{m+1} A_i         addJM_comm_of_le
    additive commutativity   all i,k, EVERY d                  addJM_comm
    identification           L_k = 1 + A_k at d = q - q^-1     jmRaw_eq_one_add_addJM
    MULTIPLICATIVE           L_i L_k = L_k L_i                 jmRaw_comm

### The two things worth remembering

**The identification was not planned, and it is the payoff for leaving `d` free.**
`sigma_k (1 + A_k) sigma_k = h*sigma_k + 1 + sigma_k A_k sigma_k` by the Hecke
relation, which is `1 + A_{k+1}` exactly when `d = h = q - q^-1`. The value is FORCED
by the recursion. Had `d` been pinned to Mathas's `q^-1` at the outset this would not
have been visible.

**The middle case of 3.24(i) cannot be done term-by-term.** Neither `T_(j,i)` nor
`T_(j+1,i)` commutes with `sigma_j` alone — only their SUM does (measured, then
proved). That retrospectively explains why all five earlier "find the right property
of N" leads died: there is no such property, because the phenomenon is not a property
of a single element.

### Independent confirmation

`computations/hecke/jm_commutativity_confirmation_probe.py` — faithful regular rep of
H_4/H_5, exact Fractions, q in {2,3,5/2}. All three identities True. Both controls
fire: the L's are NOT central (so the True is not a broken comparison), and the
identification FAILS at d = 1 (so the probe can see d).

### What is still open — this bean stays open for it

1. **`prod L_i = Delta^2` for general n.** Only n = 2, 3 are proved. The needed
   braid identity is `delta_{n+1}^{n+1} = delta_n^n * L_{n+1}` with
   `delta_n = sigma_0 ... sigma_{n-2}`; commutativity does NOT supply it (it makes the
   product order-independent, which is a different statement).
2. **The spectral half of `JucysMurphySpectrum`** — the seminormal representation
   itself. This is the larger remaining item and the one that would actually discharge
   the general-lambda twist. The general-lambda twist REMAINS CONDITIONAL.


## 2026-08-25 (later) — `prod L_i = Delta^2` PROVED for every n. Item 1 above is closed.

`QOU.BraidKnot.Hecke.jmProd_eq_delta_pow` : `L_0 L_1 ... L_n = (delta n)^(n+1)`, the full
twist of `B_{n+1}`. Sorry-free, `#print axioms` clean.
`HeckeFullTwistProduct.lean`, ~230 lines.

**From the braid relations ALONE.** The Hecke relation is not used anywhere in that file,
and neither is `jmRaw_comm` — commutativity makes the product order-independent, which is
a DIFFERENT statement and does not give the identification.

### The engine

    delta k  = sigma_0 ... sigma_{k-1}            ascending run
    run b k  = sigma_{b+k-1} ... sigma_b          descending run, bottom b
    L_k      = run 0 k * delta k                  jmRaw_eq_run_mul_delta

    (delta m * sigma_m)^(k+1) = (delta m)^(k+1) * run b (k+1)   for m = b+k
                                                                 delta_pow_run

At `b = 0` this is `(delta (n+1))^(n+1) = (delta n)^(n+1) * run 0 (n+1)`; multiplying on
the right by `delta (n+1)` turns the RHS into `(delta n)^(n+1) * L_{n+1}` and the LHS into
`(delta (n+1))^(n+2)`, which IS the induction step.

**The free bottom index `b` is load-bearing.** The step consumes the inductive hypothesis
at `b+1`, not at `b`. A version stated only at `b = 0` does not close.

**Exactly one braid move in the whole file** (`core_braid_push`): everything else is
far-commutation bookkeeping. That is why the n=2/n=3 hand proofs looked like "one braid
move on a six-letter word" — they were the base and first step of this induction.

### Independent confirmation

`computations/hecke/jm_full_twist_product_probe.py` — faithful regular rep, H_3..H_6,
exact Fractions, q in {2,3,5/2}. All three identities True; controls fire (the exponent is
tight, the twist is not the identity). **The probe caught a transcription error of mine on
its first run**: I wrote the step's left exponent as `m+1` when it is `m`. The delta index
goes up while the exponent does not, and that asymmetry is the content of the step.

### What remains — this bean stays open for it

**The spectral half of `JucysMurphySpectrum`** — the seminormal representation itself.
That is now the ONLY remaining item, and it is the one that would discharge the
general-lambda twist, which REMAINS CONDITIONAL. Both structural halves the user's arc
named (commutativity, `prod L_i = Delta^2`) are done; the spectral half is not, and is
larger than either.


## 2026-08-25 (third) — the spectral half, narrowed. NOT closed.

`HeckeSeminormalWeight.lean` moves `JucysMurphySpectrum`'s assumption from the COMPOSITE
to the CONSTITUENTS.

That class asserts `fullTwistScalar = prod_i q^(2*content(e i))` — a statement about the
twist. The literature does not prove that; it proves each `L_k` acts by `q^(2*content)`,
and the product statement follows only via `prod L_i = Delta^2`. That step is now proved
for every n, so:

    IsJMWeight                     ASSUMED   L_k . v = c_k . v, PER ELEMENT
    jmProd_smul_of_weight          derived
    fullTwist_smul_of_weight       derived   Delta^2 . v = (prod c_k) . v
    fullTwist_smul_eq_theta_sq     derived   c_k = q^(2c)  =>  Delta^2 . v = theta^2 . v
    twist_scalar_eq_theta_sq       derived   and the scalar is UNIQUE, given v != 0

The last is the bridge: `JucysMurphySpectrum`'s field asserts exactly that equation and it
is now a consequence.

**Non-vacuity, with a falsifiability check.** `scalarGenerators` (the 1-dim rep
`sigma_i -> q`) + `rowTableau` gives `scalar_isJMWeight`: `v = 1` IS a JM weight vector with
the content eigenvalues. Feeding it to the general theorem returns `q^(n(n-1))` — which
`theta_single_row_sq` gets from the two Hecke roots with NO JM input. Two routes, same
answer.

### THIS DOES NOT CLOSE THE BEAN

It does **not** prove the seminormal form. The eigenvalue hypothesis is still assumed for
`dim V_lambda > 1`; the exhibited instance is ONE-DIMENSIONAL and shows only that the
hypothesis is satisfiable. **The general-lambda twist REMAINS CONDITIONAL.**

What is left is the genuine remaining item: construct the seminormal representation — the
standard-tableau basis with `L_k` diagonal — and prove the eigenvalues are the contents.
That is a Wenzl/Hoefsmit-scale construction, larger than everything in this bean so far.


## 2026-08-25 — MERGED as 0916b28b55. This bean's two titled items are DONE.

`jmRaw_comm` (commutativity, all i,k) and `jmProd_eq_delta_pow` (`prod L_i = Delta^2`,
all n) are both on main, sorry-free. Closing this bean; the successor items are:

- **`qou-t1kv`** — `HeckeGenerators` is H_∞, so no finite-dimensional rep can instantiate
  it and `IsJMWeight` cannot be discharged at `dim > 1`. Structural, not mathematical;
  a bounded-index class variant fixes it and lets the corpus's existing `stdRep3`
  (2-dim (2,1)-rep of H_3, relations already proved) close the gap at n = 3.
- **`sv8b`** (HIGH, pre-existing) — the classical seminormal base vector, brick 5 of the
  Okounkov–Vershik tower. The general-lambda twist stays CONDITIONAL until that side lands.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-17 — Jucys–Murphy Full-Twist Triangular Content Scaling (`QOU.Foundations.CalibrationJMGibbsBarPoincare`, PR #8223)
- Formalized `jm_normalized_product_scaling` and `jm_inductive_full_twist_step` in `folio/quantum-observable-universe/lean/QOU/Foundations/CalibrationJMGibbsBarPoincare.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `71263060fde5e0d5c09fecd66cf05ada5b6cd208` | PR: `https://github.com/litlfred/qou/pull/8223`
- Kept at `status: in-progress` per merge-manager protocol.
