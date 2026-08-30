---
# qou-dsif
title: 'GAP: (P), the Pieri step of the Macdonald telescope — the induction over addable corners'
status: completed
type: task
priority: high
created_at: 2026-08-27T05:35:38Z
updated_at: 2026-08-30T07:29:12Z
---

Successor to `qou-6a7w`, which is completed (PR #5857 merged `6f4d0d2a3a`).
Live on PR #5871.

## The goal

`QOU.MathlibExt.MacdonaldTelescope.PieriStep Q X lam`, i.e.

    Σ_{μ ∈ addableCorners λ}  s_μ(Q,X)  =  ((1 − X)/(1 − Q)) · s_λ(Q,X)

for general `λ`. Everything it needs to be *stated* exists; the induction is
what is missing.

## What is already in Lean (all on main or #5871, all sorry-free)

- `hookLength_addBoxRow_of_ne_corner` — the per-cell update rule, every cell
  but the new box. The corner is excluded because its hook is `1` only under
  weak decrease, which the bare `List ℕ` carrier does not carry.
- `schurElement_eq_prod` — `schurElement` as a product over rows, not a fold.
  Nothing cell-by-cell can be said about a fold.
- All three row-factor cases: `_row_below` (equal), `_same_row`
  (`List.range_succ` split), `_row_above` (+ `_short`) via product surgery at
  one interior index (`Finset.mul_prod_erase`), stated division-free.
- `nLambda_addBoxRow` (`n(λ)+r`) and `nLambda_addBoxNewRow` (`n(λ)+ℓ(λ)`).
- `addBoxNewRow` and its kit, plus `addBoxRow_at_length` recording that
  `addBoxRow` is a no-op out of range.
- `addableCorners` with four `decide` checks, including the negative `(2,2)`.
- `pieriStep_one` and `pieriStep_two_one` — (P) proved at two shapes and shown
  to be instances of the general proposition.

## What is measured, and where

`computations/y_lambda_pieri_step_probe.py` (exact sympy, no floats, no
witness) establishes three things, each of which I had previously asserted
wrongly from memory:

1. (P) holds with `X` FREE at eight shapes, up to `(3,2,1)`.
2. The per-shape ratio has a closed form and needs no collapse:
   `s_{λ+□(r)}/s_λ = Q^r · (1 − X·Q^{λ_r−r})/(1 − Q^{h_μ(r,λ_r)}) ·
   ∏_{h ∈ arm ∪ leg} (1−Q^h)/(1−Q^{h+1})`.
3. **The shift product does NOT collapse** — `(Q²+Q+1)/((Q+1)³(Q²+1))` at
   `(3,2,1), r=1`. Genuine rational function. What telescopes is the SUM over
   corners, never the summand. Do not go looking for a hook-walk collapse in
   the summand; there isn't one, and I wasted a turn claiming there was.

## What the induction actually has to do

Sum the per-shape ratio over the corners and get `(1−X)/(1−Q)`. Every summand
is a different rational function; the cancellation is across them. Note the
denominators `1 − Q^h` may vanish, so the division-free discipline used
throughout should carry into the sum rather than being dropped for
convenience.

Open question worth settling first, cheaply, in the probe: is there a partial-
fraction identity over the corners that makes the sum term-by-term, or does it
genuinely need all corners at once? Measure before formalising — that is what
the three corrections above cost.


### THE REDUCTION — measured 2026-08-27, PR #5871

The open question this bean posed ("is there a partial-fraction identity that
makes the sum term-by-term, or does it need all corners at once?") is answered,
and better than expected. Exact sympy, eleven shapes up to `(4,3,1,1)`.

**(P) splits into TWO identities in `Q` alone.** The ratio is linear in `X`, and
structurally so: one box adds one cell, hence exactly one numerator factor
`(1 − X·Q^c)`; everything else is hook lengths, which carry no `X`. So
`R_r = K_r·(1 − X·Q^{c_r})` with `K_r` X-free, and matching coefficients gives

    (P1)  Σ_r K_r            = 1/(1 − Q)
    (P2)  Σ_r K_r · Q^{c_r}  = 1/(1 − Q)

equivalently `Σ_r K_r·(1 − Q^{c_r}) = 0`.

**The new box's hook is always 1**, at every addable corner including the new
bottom row. Substituting that clears the only denominator outside the product,
and both identities become:

    (P1)   Σ_r  Q^{r}     · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1
    (P2)   Σ_r  Q^{λ_r}   · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1

Same product, two weightings — the **row index** and the **row length**, both
`0` for the new bottom row — each summing to exactly `1`.

**AIM THE LEAN PROOF AT THESE, not at (P).** One variable, no outer
denominator, right-hand side a literal `1`. (P) then follows by X-linearity,
which is itself a short argument: the ratio has one X-bearing factor.

Note the two are NOT obviously the same identity, and I have not tested whether
one implies the other (e.g. by conjugation `λ ↦ λ'`, which negates contents, or
by `Q ↦ 1/Q`). That is the next cheap measurement, and it would halve the work
again if it lands. Measure it; do not assume it.

Still true and still worth not re-deriving: the shift product itself does NOT
collapse — `(Q²+Q+1)/((Q+1)³(Q²+1))` at `(3,2,1), r=1`. The cancellation is
across the sum, never inside a summand.


### AND (P2) IS (P1) AT THE CONJUGATE — the step is ONE identity

The "next cheap measurement" above landed. Transposing sends the corner in row
`r` at `(r, λ_r)` to the corner in row `λ_r` at `(λ_r, r)`, so **row index** and
**row length** swap; hook lengths are transposition-invariant
(`h_λ(i,j) = h_{λ'}(j,i)`), so the product is unchanged. Hence
`(P2)[λ] = (P1)[λ']`.

**THE WHOLE PIERI STEP IS NOW ONE IDENTITY IN ONE VARIABLE:**

    Σ_r  Q^{r} · ∏_{h ∈ arm ∪ leg(r)} (1 − Q^h)/(1 − Q^{h+1})  =  1

(P2) follows by conjugation; (P) follows from the two by X-linearity. No outer
denominator, right-hand side a literal `1`.

**PROVE THIS. Do not attack (P) directly.**

Evidence caveat, and the probe enforces it: the self-conjugate shapes
`(1)`, `(2,1)`, `(2,2)`, `(3,2,1)`, `(3,3,2)` satisfy fact 7 **trivially**
(`λ' = λ`) and are not evidence. `main()` labels each shape and reports the
informative count — currently 6 of 11. Run it; do not quote a count.

### What a Lean attack now needs

1. `Partition.conjugate` already exists in `QPartitionCombinatorics`. Needed:
   that it is an involution on the shapes in play, that it bijects addable
   corners with addable corners, and that it preserves hook lengths
   transposed. That is the conjugation half.
2. The X-linearity half: `schurElement` at `μ = λ + □` has exactly one more
   content factor than at `λ`. Should be short from `schurElement_eq_prod`
   plus the row-factor cases already proved.
3. The one identity itself. Still open, still the hard part — but now a
   single-variable statement about a sum of products of `(1−Q^h)/(1−Q^{h+1})`
   over the corners, equal to `1`.

Nothing above is proved in Lean yet. All of it is measured exact-symbolically.


### MEASURED NEGATIVE — partial sums in row order do NOT telescope

Tested on `(2,1)`, `(3,1)`, `(3,2,1)`, `(4,2,1)`: form the tail sums
`S_{≥k} = Σ_{corners in rows ≥ k} Q^r · P_r` and look for structure. There is
none. `S_{≥0} = 1` as it must, but every proper tail is an ugly rational
function with no pattern — e.g. at `(4,2,1)`,

    S_{≥2} = Q²·(Q¹¹ + 3Q¹⁰ + 5Q⁹ + 8Q⁸ + 10Q⁷ + 11Q⁶ + 11Q⁵ + 9Q⁴ + 7Q³
              + 5Q² + 2Q + 1) / ((Q+1)(Q²+1)(Q⁴+Q³+Q²+Q+1)(Q⁶+…+1))

and the denominators are not the natural product denominators either. **The
cancellation is global across all corners, not sequential.** Consistent with
the earlier finding that no summand collapses on its own.

**Scope (a), not (b):** this rules out *partial sums in row order* as a route,
measured on four shapes. It is not a proved exclusion of every sequential or
recursive structure — I have no invariant forbidding those, and did not look
for one. Do not upgrade this to "no induction exists".

What it does say: do not spend time looking for a telescoping in row order, and
do not expect a two-term recursion in the number of rows to fall out. A route
that works will have to move all corners at once — inclusion–exclusion over the
corner's hook, in the shape of the Greene–Nijenhuis–Wilf hook-walk argument,
is the obvious candidate and is a research-scale build in Lean, not a brick.


### (P) AND (F) ARE ONE STATEMENT — and the corpus already had q=1 (2026-08-27)

PR #5876. Audit: `docs/audits/2026-08-27-pieri-and-branching-are-one-statement.md`.

**Framing correction.** #5857 §4 and #5871 both said the telescope follows from
**two** elementary statements, (P) and (F). It does not. (F) is the `q → 1`
shadow of (P): each factor `(1−Q^h)/(1−Q^{h+1}) → h/(h+1)`, the update rule
gives `∏_{c∈μ} h_μ = ∏_{c∈λ} h_λ · ∏ (h+1)/h`, and FRT turns that into
`f_μ/f_λ = (n+1)·∏ h/(h+1)`. So the `q=1` identity holds **iff** (F) does.
Verified by two independent routes on eleven shapes.

**Corpus find — I built alongside existing work.** The topic grep I ran only
after the reductions landed turns up:

- `numStandardYoungTableaux_mul_hookLengthProduct` — **FRT, sorry-free**,
  `QOU/Mathlib/HookLengthFormula.lean:171`
- `QOU/Mathlib/QHookProduct.lean` — a q-hook product on **Mathlib's
  `YoungDiagram`** with the `q=1` specialisation proved, **sorry-free
  throughout**

The Pieri tower here is a **parallel development on a bare `List ℕ`**. `sp09`
(completed) already sizes the bridge: ~40 lines per-cell hook agreement,
~120–150 for the SYT-count encoding bridge. **Not done, and not recommended
now** — recorded so the choice is deliberate. **Any further Pieri work must
check `QOU/Mathlib/` first.**

### Revised sizing — this is not a brick

Only the **q-deformation** is open; the `q=1` case is reachable from corpus
material plus the update rule already proved. But `sp09` records that (F) — the
`q=1` case — was believed to need Greene–Nijenhuis–Wilf or
Novelli–Pak–Stoyanovskii, and is "multi-week, a plausible Mathlib contribution
in its own right". **The q-deformation is at least that hard.** Treat this as a
multi-week build needing owner sign-off on scope, not a next brick.

### Hazard for the cyclotomic route

Count poles and zeros **per root of unity**, not per exponent. At `(4,2,1) r=0`
the pole exponents are `{3,5,7}` and zeros `{1,4,6}`: the `(1−Q³)` pole dies
against the `(1−Q⁶)` zero, both vanishing at a primitive cube root. Exponent
matching reports a spurious pole.


## 2026-08-30 — the node-level identity is PROVED, and my sizing was wrong

PR #6098. `QOU.Mathlib.sum_prod_qratio_corner`, sorry-free, axiom-clean, generic `[Field F]`:

    Sum_{i in s} (prod_{j != i} (Q v_i - v_j)/(v_i - v_j)) * (Q-1)/(Q v_i - v_b) = 1   (v_b = 1)

That is (P1) after the coordinate change `b_i = q^{beta_i}`. It mentions no partition.

### Three corrections to what this bean said on 2026-08-27

1. **"Multi-week" was wrong, and wrong in an instructive direction.** I reasoned that
   the q=1 case needs GNW/NPS and the q-deformation is "at least that hard". The
   q-dependence lives entirely in the coefficients c_1..c_{|s|-1} of
   `prod_{j != b}(Q X - v_j)`, and the Lagrange vanishing annihilates all of them; only
   the Q-free c_0 survives. The q-statement is NO HARDER than its q=1 shadow.
2. **GNW is already proved in this corpus** (`SYTHookGNW.gnwHookIdentity`, sorry-free),
   so the premise of the estimate was false as well as the inference.
3. **The Lagrange keystone existed and I nearly rebuilt it.**
   `QOU/Mathlib/LagrangeCoeffSum.lean` landed on main while this branch sat idle three
   days: sorry-free, generic-field, carrying `sum_eval_div_prod_eq_coeff` plus two
   siblings of this very identity. Found only by re-running the corpus grep after the
   gap. The proof here is that file's divX residue argument.

### The substrate question is settled by measurement

Option C (`QOU/MathlibExt/QPartitionCombinatorics.lean`, my own tower) is ruled out
STRUCTURALLY, not by preference: `abbrev Partition := List N` carries no
weakly-decreasing invariant (`grep -c Sorted` = 0 across all three of my files), so the
beta-numbers need not be distinct and the Lagrange step is false as stated on that type.
Separately `qou-j7ln` (completed) proved my hook-update rule on YoungDiagram, cleaner
("one `if`, not two cases"). That tower is superseded.

Option B (YoungDiagram) is the partition layer: q-hook product, addable corners, FRT,
hook-under-addCell, all sorry-free. Option A (the sorted-list layer) is the beta home.

### What remains — one bridge, which the corpus names itself

`sum_eq_bracket_mul_of_qratio_scaling`'s docstring calls out its own open input: the
q-analogue of Frame-Robinson-Thrall. Measured today over 13 shapes x 3 paddings,
k-independent, sign-free and power-free:

    prod_{c in lam} (1 - q^h(c)) = prod_i (q;q)_{beta_i} / prod_{j<l} (1 - q^{beta_j - beta_l})

Classical shadow `prodHooks_mul_betaProdGap` already proved on the list layer, so this is
a q-deformation of an existing proof. NOT giving a schedule: the last one I gave was
wrong by a large factor and I am not replacing it with a confident number the other way.

Probe: `computations/pieri_corner_node_identity_probe.py` (6 facts, exact sympy).
Audit: `docs/audits/2026-08-30-pieri-corner-identity-and-the-substrate-question.md`.


## 2026-08-30 (later) — RETRACTION: the q-FRT bridge was never open

My entry above named the q-analogue of Frame-Robinson-Thrall as the one open piece. **It is proved,
sorry-free, on main, and was before I wrote that.** Chain:

  SYTHookFormulaBetaMonoid.rowHookProdF_mul_betaGapProdF   per-row FRT, ANY commutative monoid,
                                                           arbitrary f : N -> M
  SYTHookFormulaBetaProdMonoid.prodHooksF_mul_betaGapProdF whole-diagram assembly, same generality
  SYTBetaGapVandermonde.prodHooksF_one_sub_pow_pair        the q-case, f n = 1 - Q^n

Machine-checked: prodHooksF_one_sub_pow_pair is [propext, Classical.choice, Quot.sound], and all
five files in that chain have ZERO sorry tokens.

### Why I got it wrong, and the pattern

I trusted `LagrangeCoeffSum`'s docstring, which names the q-FRT identity as its own open input and
points at bean qou-j7ln. That docstring is stale -- qou-j7ln is completed and the identity landed
after it was written. AGENTS.md's rule that a source file's `## Status` note is not authoritative
applies to docstrings verbatim; I suspended it for a file whose Lean I had just read closely. Same
failure mode as trusting a sibling's bean, one artifact type over.

THREE TIMES this session the corpus already held what I was about to build: sum_eval_div_prod_eq_coeff,
the hook-update rule (qou-j7ln), and the whole q-FRT chain. Common cause: my grep ran on TOPIC words
(Pieri, telescope, Macdonald) while these files are named for their METHOD (SYTBetaGapVandermonde,
LagrangeCoeffSum). None surfaces on a topic grep; all three surface on the SHAPE of the statement.

### Landed this turn

`QOU/Mathlib/QHookVandermonde.lean` (sorry-free, generic [CommRing R]): converts the pair-product
form to a genuine Vandermonde in x_i = Q^{beta_i}, via the termwise
    x_i - x_j = (-x_j)(1 - Q^{beta_i - beta_j})     (beta_j <= beta_i)
The monomial/sign correction is left as the product prod_{i<j}(-x_j), NOT evaluated to
(-1)^C(k,2) Q^{sum_j j beta_j}: the evaluated form is where sign errors live and no consumer needs
it, since it cancels on both sides of any ratio. Also corrects the stale LagrangeCoeffSum docstring
and the two artifacts of mine that repeated the false claim.

### What is actually left

WIRING, not identity-proving: discharge the `hw` hypothesis of sum_eq_one_of_corner_ratio_scaling
by feeding it the box-addition ratio, which is a quotient of two instances of
prodHooksF_one_sub_pow_vandermonde. No schedule -- my last two estimates on this front were both
wrong, in opposite directions.

### Literature

Not needed and not available. The library (544 docs) has no Macdonald and no symmetric-functions
text; `hdr` (Hecke algebras) has Schur elements but no hook products. Irrelevant anyway: a citation
does not discharge a Lean goal, and the identity is proved in-corpus over a generality no textbook
states (arbitrary f over a commutative monoid). Lit would only serve paper attribution, and would
need ingesting first.


## 2026-08-30 (later still) — CLOSED. The goal is proved, by the other route.

`QOU.MathlibExt.MacdonaldTelescopeGeneralX.telescope_generalX` is the goal of this bean:

    sum_{|nu|=n} f^nu * schurElement Q X0 nu.rowLens  =  ((1 - X0)/(1 - Q))^n

for ARBITRARY X0, over Q > 1 not a root of unity. VERIFIED axiom-clean this turn:
[propext, Classical.choice, Quot.sound], no sorryAx.

It does NOT go through the Pieri step. It goes through the polynomial-identity route: both
sides are eval X of polynomials of degree <= n; they agree at every X = Q^r by the proved
principal specialisation; {Q^r} is infinite for Q > 1; Polynomial.eq_of_infinite_eval_eq.

The Pieri route is proved too, and separately:
  SchurWeyl.sum_schurPrincipal_addCellOrSelf  : sum_a s_{mu + box at a} = [r]_Q * s_mu
  SchurWeyl.sum_wenzlWeight_addCellOrSelf     : sum_a w_{mu + box at a} = w_mu
both axiom-clean, both assembled from sum_eq_bracket_mul_of_qratio_scaling with
schurPrincipal_addCell_eq as the `hw` I twice named as the open remainder.

## Why "sorry-free" was not enough, and the fix that made the check possible

telescope_generalX had ZERO sorry tokens and was NOT VERIFIABLE. Its import cone was RED on
main: QOU/Mass/QIntegerBarParity.lean:53 does `open QOU.Mass.QHookDimension (qIntPoly)` and
that namespace HAS NEVER EXISTED -- QHookDimension.lean declares `QOU.Mass` only. Measured
across history: the file was red on the day it landed (PR #5745), and QHookDimension has
since dropped its own `def qIntPoly` as well, breaking QIntegerCanonical:117 the same way.

One error blocked SIX modules: QIntegerCanonical, QPartitionCombinatorics, WenzlSchurElement,
WenzlSchurElementBridge, WenzlJonesMarkovNormalisation, MacdonaldTelescopeGeneralX. Both
consumers now point at QOU.Mass.QHookDimensionBalanced.qIntPoly -- the identical geometric
`sum_{i<n} q^i`, in a file both already imported. Cone: 104 modules, ok, 0 error, 0 blocked.

`grep -c sorry` is a screen; the proof term is the verdict. Here the screen said 0 and the
verdict could not be taken at all.

## Six duplications in one session

sum_eval_div_prod_eq_coeff; the hook-update rule (qou-j7ln); the whole q-FRT chain;
betaR_addCell (same name I chose, in QRatioBetaFactors); schurPrincipal_addCell_eq (the `hw`);
and finally the telescope itself. My grep ran on TOPIC words -- Pieri, telescope, Macdonald --
while these files are named for their METHOD: SYTBetaGapVandermonde, LagrangeCoeffSum,
QRatioBetaFactors, VandermondeUpdateRatio, BranchingGenericity. Not one surfaces on a topic
grep. Grep the SHAPE of the statement, and grep it BEFORE writing, not after compiling.

## What my two PRs are worth now

#6098's sum_prod_qratio_corner and #6108's QHookVandermonde are a PARALLEL route, not the
critical path. They are new statements (nothing else sums the corner q-ratio to 1, and nothing
else converts the pair product to a genuine Vandermonde), and AGENTS.md explicitly permits
measured research overlap. But they do not close anything this bean needed, and the bean's
goal was met before they were written.


## 2026-08-30 — CORRECTION to my own entry above, and the measured answer

**I claimed the `QOU.Mass.QHookDimension` namespace "has never existed" and that
QIntegerBarParity "was red on the day it landed". BOTH WRONG.** At fed69b1c4d the file
declared

    namespace QOU.Mass
    namespace QHookDimension

so the namespace existed, NESTED. I grepped only `namespace QOU.Mass.QHookDimension` --
the fully-qualified spelling -- got 0, and read that as absence. One spelling of a
two-spelling construct: the detector blind spot this corpus has a taxonomy for. The file
broke at 1646b5d6d3, which removed both the nested namespace and the def. A sibling
(5479e2141a9) got this right while I was working and fixed the first consumer; my branch
now carries only the second (QIntegerCanonical:117) and defers to theirs on the first.

## The measurement: 179

Whole-corpus lean-direct on origin/main bf08fd156f9, keep-going so `error` and `blocked`
separate:

    up-to-date 1718    ok 379    blocked 210    error 1

ONE error -- QOU.MathlibExt.QIntegerCanonical -- and ALL 210 blocked modules trace to it.
Single point of failure. Of those 210, **179 carry zero sorry tokens**: they read as
sorry-free on main while `#print axioms` cannot run on any declaration in them. 31 carry
a sorry and are honestly marked.

The 179 include QOU.Torsion, QOU.ArchimedeanMassFormula, QOU.AlgebraicSubstrate, the whole
QOU.Archimedean.PauliWitness family (20 isotope witnesses), and
MacdonaldTelescopeGeneralX -- which carries telescope_generalX, this bean's goal, verified
axiom-clean only after the cone was unblocked.

**`grep -c sorry` is a screen; the proof term is the verdict.** A blocked cone makes the
verdict unavailable while leaving the screen green, and nothing in the repo currently
distinguishes the two: lean-axiom-guard covers only its registry, and the sorry-count
audits read files, not proof terms. That gap is a candidate bean, not a continuation of
this one.
