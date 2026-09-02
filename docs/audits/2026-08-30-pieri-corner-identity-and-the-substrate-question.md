# The Pieri corner identity is proved — and "which substrate" was the wrong question to ask blind

**Date:** 2026-08-30 · **PR:** [#6098](https://github.com/litlfred/qou/pull/6098) · **Bean:** `qou-dsif`

## Why this document exists

On 2026-08-27 I asked the author to choose a "substrate" before I would start the
remaining Pieri identity, and sized that identity as multi-week. The author's reply
was that the question was not answerable as posed — I had not said what a substrate
was, nor what the options were, nor what turned on the choice.

That was correct, and the fix was not better phrasing. Once the options were actually
measured, **two of the three collapsed on structural grounds and the largest layer of
the work turned out not to have a substrate at all.** The question was unanswerable
because it was premature: the measurement that would have collapsed it had not been
done. This is the case AGENTS.md's question-writing rule names — *"when you cannot
make an option legible without a paragraph of background, that is a signal the
question is premature."*

## What "substrate" meant

The Pieri step (P) of the Macdonald hook telescope reduces to one identity
(`y_lambda_pieri_step_probe.py`, fact 6):

```
(P1)   Sum_r  Q^r * prod_{h in arm u leg(r)} (1 - Q^h)/(1 - Q^{h+1})  =  1
```

summed over the rows of a partition `lam` that admit a new box. To state that in Lean
you must first fix **how a partition is represented** — the type carrying `lam`, its
hook lengths, and its addable corners. That representation is what I was calling the
substrate. Three existed in the corpus, and I was proposing to build on the one I had
written myself.

## The three options, measured

| | representation | what it carries | verdict |
|---|---|---|---|
| **A** | `QOU.BraidKnot.IdentityI` / `QOU.Mathlib.SYTEnum` — `l : List ℕ`, `Sorted (· ≥ ·)`, `∀ a ∈ l, 0 < a` | `prodHooks`, `corners`, `removeCorner`, β-numbers, `prodHooks_mul_betaProdGap`, the whole `SYTBetaLagrange` engine, GNW `gnwHookIdentity` proved | the β home; **no q-hook product**, and only *removable* corners |
| **B** | Mathlib `YoungDiagram` | `qHookLengthProduct` (`QHookProduct.lean`), `addableRows` / `addCell` / `card_addableCells` (`YoungDiagramAddable.lean`, sorry-free), FRT proved (`HookLengthFormula.lean`), hook-update under `addCell` (`QOU/SchurWeyl/HookLengthAddCell.lean`, sorry-free) | **the answer for the partition layer** |
| **C** | `QOU/MathlibExt/QPartitionCombinatorics.lean` — `abbrev Partition := List ℕ` | my own `hookLength`, `addBoxRow`, `addBoxNewRow`, `addableCorners`, `nLambda`, the hook-update rule | **ruled out structurally** |

### C is ruled out by a fact, not a preference

`abbrev Partition := List ℕ` carries **no weakly-decreasing invariant**. Measured:
`grep -c Sorted` returns **0** across all three of my files (`QPartitionCombinatorics`,
`WenzlSchurElement`, `MacdonaldTelescope`).

That is fatal for this particular proof, not merely untidy. The proof runs through
β-numbers `β_i = λ_i + (k−1−i)`, and every step needs the `β_i` **distinct** — the
Lagrange weight `∏_{j≠i}(β_i − β_j)` is in a denominator. On a type where `λ` need not
decrease, `β` need not be strictly decreasing, the nodes need not be distinct, and the
identity is *false as stated*. Adding the invariant means rebuilding the type, at which
point it is A or B anyway.

Independently, bean `qou-j7ln` (completed, PR #5645) proved my hook-update rule on
`YoungDiagram`, and proved it **better**: "the hook grows by `1` on exactly the union of
`s`'s row and column, and those meet only at `s`, which is not in `ν` — one `if`, not
two cases." My version is a two-case split on the same fact. That tower is superseded.

### The largest layer has no substrate at all

Changing coordinates from hooks to nodes — set `b_i = q^{β_i}` — turns (P1) into

```
Sum_{i in s} (prod_{j != i} (Q*b_i - b_j)/(b_i - b_j)) * (Q - 1)/(Q*b_i - b_r)  =  1
```

which mentions no partition. It is a statement about a `Finset ι` and a `v : ι → F`
over a field. **That is where the mathematical content is, and it is substrate-free.**
Writing it first was not a choice between A, B and C; it was simply the right first
brick, and it would have been the right first brick under any answer to the question I
asked.

## What is proved

`QOU.Mathlib.sum_prod_qratio_corner` — sorry-free, axiom-clean (`propext`,
`Classical.choice`, `Quot.sound`; no `sorryAx`), generic `[Field F]`, in
`QOU/Mathlib/LagrangeCornerNodeSum.lean`.

It is the third member of the `LagrangeCoeffSum` family: `sum_prod_qratio` weights each
node by `1` and sums to `[|s|]_Q`; `sum_prod_qratio_weighted` uses the seminormal weight
`Q·v_i/(Q·v_i − v_b)` and sums to `Q^{|s|}/(Q−1)`; this one uses the constant-numerator
weight `(Q−1)/(Q·v_i − v_b)` and sums to `1`. The proof is that file's `divX` residue
argument.

### `v b = 1` is load-bearing

Measured, not assumed (`pieri_corner_node_identity_probe.py`, fact 6). With free nodes
and no node at `1`, the `k = 2` sum is

```
(b0*q^2 - b0*q + b1*q^2 - b1*q - q^2 + 1)/(b0*b1*q^2 - b0*q - b1*q + 1)
```

— a genuine rational function. The node at `1` is the β-number of the **padded empty
row**, i.e. the addable corner that starts a new bottom row. So the identity is
specifically about shapes permitted to grow a row, and that corner cannot be dropped
from the sum as a degenerate case.

## The sizing was wrong, and here is why

I recorded (P1) on 2026-08-27 as multi-week, reasoning that the `q = 1` case needs
Greene–Nijenhuis–Wilf or Novelli–Pak–Stoyanovskii and that the q-deformation is "at
least that hard." Both halves were wrong.

**The q-dependence annihilates.** Rewrite the summand as `h(v_i)/(v_i · ∏_{j≠i}(v_i − v_j))`
with `h(X) = ∏_{j≠b}(Q·X − v_j)`. Every bit of the `Q`-dependence sits in the
coefficients `c_1 … c_{|s|−1}` of `h`, and the Lagrange vanishing kills all of them.
Only `c_0`, which is `Q`-free, survives — which is why the right-hand side is a bare `1`
for every `Q`. **The q-deformed statement is no harder than its `q = 1` shadow**, not
harder. My estimate inverted the actual difficulty gradient.

**GNW was already proved, and so was the keystone.** `SYTHookGNW.gnwHookIdentity` is
sorry-free on main, and `QOU/Mathlib/LagrangeCoeffSum.lean` — which landed while this
branch sat idle for three days — carries `sum_eval_div_prod_eq_coeff`, generic-field,
the exact Lagrange keystone I had budgeted time to build from scratch. I found it only
by running the corpus grep a second time after the three-day gap. Had I skipped that,
I would have rebuilt a sorry-free file that already existed.

## What remains — RETRACTED AND REPLACED 2026-08-30

**This section was wrong when it was merged, in the direction it warns about elsewhere in this
document.** It said the q-analogue of Frame–Robinson–Thrall was the open input, and that its
classical shadow being proved made it "a q-deformation of an existing proof rather than a new one."

The q-deformation is **already proved, sorry-free, on `main`**, and was before I wrote that:

| | |
|---|---|
| `SYTHookFormulaBetaMonoid.rowHookProdF_mul_betaGapProdF` | the per-row FRT identity in **any commutative monoid**, over an arbitrary `f : ℕ → M` |
| `SYTHookFormulaBetaProdMonoid.prodHooksF_mul_betaGapProdF` | the whole-diagram assembly, same generality |
| `SYTBetaGapVandermonde.prodHooksF_one_sub_pow_pair` | the q-case, `f n = 1 − Qⁿ`, in pair-product form |

Machine-checked here: `prodHooksF_one_sub_pow_pair` depends on
`[propext, Classical.choice, Quot.sound]` — no `sorryAx` — and every file in that chain
(`SYTHookFormulaBeta`, `…Monoid`, `…Prod`, `…ProdMonoid`, `SYTBetaGapVandermonde`) has **zero**
sorry tokens.

**Why I got it wrong.** I took `LagrangeCoeffSum`'s own docstring at face value — it names the
q-FRT identity as its remaining gap and points at bean `qou-j7ln`. That docstring is stale: the
bean is `completed`, and the identity landed after the docstring was written. This corpus's rule
that a source file's status note is not authoritative applies to docstrings verbatim, and I
suspended it for a file whose Lean I had just read carefully — the same failure mode as trusting a
sibling's bean, recorded in AGENTS.md, one artifact type over.

**Three times in one session** the corpus already held what I was about to build: the Lagrange
keystone (`sum_eval_div_prod_eq_coeff`), the hook-update rule (`qou-j7ln`), and now the whole
q-FRT chain. The common cause is that my corpus grep ran on **topic** words — "Pieri",
"telescope", "Macdonald" — while these files are named for their **method**
(`SYTBetaGapVandermonde`, `LagrangeCoeffSum`). None of the three would surface on a topic grep;
all three surface immediately on the *shape* of the statement. Grep the shape.

### What is actually left

`prodHooksF_one_sub_pow_pair` gives the identity in `(1 − Q^{β_i − β_j})` form. The node-sum
consumers want it against a genuine Vandermonde in `x_i = Q^{β_i}`. That conversion is this PR:
`QOU/Mathlib/QHookVandermonde.lean`, sorry-free, generic `[CommRing R]`, one termwise identity

    x_i − x_j  =  (−x_j)·(1 − Q^{β_i − β_j})        (β_j ≤ β_i)

whose only input is that `β` is strictly decreasing on a weakly-decreasing shape. The
monomial-and-sign correction is left as the product `∏_{i<j}(−x_j)` rather than evaluated to
`(−1)^{\binom k 2} Q^{\sum_j j·β_j}`: the evaluated form is where sign errors live, and no
consumer needs it, since the same factor appears on both sides of every ratio of two such products.

After that the remaining work is **wiring, not identity-proving**: discharging the `hw` hypothesis
of `sum_eq_one_of_corner_ratio_scaling` by feeding it the box-addition ratio, which is the quotient
of two instances of the theorem above. I am not putting a schedule on it — my last two estimates on
this front were both wrong, in opposite directions.

## Verification

CI is `workflow_dispatch`-only and Copilot does not enqueue (`qou-gwe9`), so per
AGENTS.md the agent verification is the gate.

- `scripts/lean-direct-cone.sh -B QOU.Mathlib.LagrangeCornerNodeSum` → exit 0,
  `ok=2 err=0`. Lean-direct rather than `lake build`: this tree has a restored olean
  cache (6990 oleans, **0** traces), which `lake build` would evict (`qou-r13s`).
- `#print axioms QOU.Mathlib.sum_prod_qratio_corner` → `[propext, Classical.choice, Quot.sound]`.
- `computations/pieri_corner_node_identity_probe.py` → `all exact: True`, exit 0.
