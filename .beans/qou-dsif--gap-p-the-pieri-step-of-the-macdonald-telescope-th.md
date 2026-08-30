---
# qou-dsif
title: 'GAP: (P), the Pieri step of the Macdonald telescope — the induction over addable corners'
status: in-progress
type: task
priority: high
created_at: 2026-08-27T05:35:38Z
updated_at: 2026-08-30T03:42:33Z
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
