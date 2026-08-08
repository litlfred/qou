# C1 ∞-side: `deg_q(cₙ) = n²` PROVED for all `n` (was a spot-check to `n ≤ 9`)

**Date:** 2026-08-08 · **Axis:** Q_β odd channel / C1 ∞-Stokes (W2, bean
`qou-xufp`; D-ladder front `qou-dri7`) · **Tier:** elementary proof + exact
check. No fit, nothing wired, no tier change.

Upgrades one line of
[`2026-08-01-c1-inf-formal-solution-qgevrey.md`](2026-08-01-c1-inf-formal-solution-qgevrey.md),
which records `deg_q(cₙ) = n²` as *"verified symbolically for `n ≤ 9`"*.

**Why it matters that this was only spot-checked.** That degree law is the
entire evidence for the q-Gevrey slope-½ conclusion — that the C1 formal
solution at `∞` is divergent and therefore *must* be q-Borel/Laplace summed
(sector-dependent, theta-family kernel). The whole ∞-Stokes programme is
downstream of it. Per the formalize-first discipline, an invariant that
prunes or directs a search should be **proved** before the search runs; a
9-point sample supporting an all-`n` claim is exactly the shape that
discipline exists to catch. It is provable in one induction.

## Statement

With `L1 = (q²x−1)σ² − (q−1)σ − (q−1)` and the ansatz `f(x) = Σ_{n≥0} cₙ x^{−n}`,
the exact coefficient recurrence is

```
c_{m+1} = c_m · f_m ,    f_m := 1 + (q−1)q^m + (q−1)q^{2m} ,    c_0 = 1 .
```

**Theorem.** `deg_q(cₙ) = n²` for every `n ≥ 0`; and `lc(cₙ) = 2` for every
`n ≥ 1` (with `lc(c_0) = 1`).

## Proof

Expand `f_m = 1 − q^m − q^{2m} + q^{m+1} + q^{2m+1}`.

- **`m ≥ 1`.** The exponents `m, 2m, m+1, 2m+1` are pairwise distinct and
  `2m+1` is strictly the largest, so nothing can cancel the top term:
  `deg f_m = 2m+1`, `lc(f_m) = 1`.
- **`m = 0`.** The two `(q−1)` terms **collide**: `f_0 = 1 + 2(q−1) = 2q − 1`.
  Its degree is `1 = 2·0+1`, matching the general formula, but its leading
  coefficient is `2`, not `1`.

`ℤ[q]` is an integral domain, so degrees add and leading coefficients multiply
across a product. Hence

```
deg cₙ = Σ_{m=0}^{n−1} (2m+1) = n²           and     lc(cₙ) = 2·1⋯1 = 2  (n ≥ 1).
```
∎

The `q^{n²}` growth is therefore established for all `n`, and with it the
irregular slope-½ / q-Gevrey divergence — no longer contingent on a sample.

## Check

[`c1_inf_degree_law_proof_probe.py`](../../computations/qbeta/c1_inf_degree_law_proof_probe.py)
→ [`c1-inf-degree-law-proof-probe.witness.json`](../../computations/qbeta/c1-inf-degree-law-proof-probe.witness.json).
Exact integer polynomial arithmetic over `ℤ[q]` (no floats, no CAS
dependency), re-deriving the coefficients independently to **`n = 30`** —
3× the previously recorded window.

| claim | window | result |
|---|---|---|
| `deg_q(cₙ) = n²` | `n ≤ 30` | holds |
| `lc(cₙ) = 2`, `n ≥ 1` | `n ≤ 30` | holds |
| `deg f_m = 2m+1` | `m < 30` | holds |

This is a *check of a proved statement*, not the evidence for it.

## Correction to the prior record

The 08-01 audit does not mention the leading coefficient. It is **2**, not 1,
for all `n ≥ 1`, and the reason is the degenerate `m = 0` case where
`(q−1)q^m` and `(q−1)q^{2m}` are the same term. Small, but it is the sort of
constant that later gets absorbed into a normalization and then hunted for; it
is recorded here so nobody re-derives it.

## Scope — what this does NOT do

- **It does not compute a Stokes multiplier.** Those remain the residual of
  W2 / the ∞-side of the C1 module, exactly as the 08-01 audit states. This
  strengthens the *premise* of the q-Borel route, not its conclusion.
- ~~It is not Lean-formalized.~~ **It is now Lean-proved, sorry-free** —
  see §Lean below.
- **Nothing is wired and nothing is fitted.** The recurrence is exact and
  parameter-free; there is no free constant anywhere in the above.

## Lean

[`QOU/QBeta/C1InfDegreeLaw.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/C1InfDegreeLaw.lean)
— **sorry-free**, over `Polynomial ℤ` (§7c: pure algebra over a domain; no
ordering, no `Real.*`, the archimedean wall is not crossed).

| declaration | statement |
|---|---|
| `cFactor m` | `1 + (X−1)Xᵐ + (X−1)X^{2m}` |
| `cCoeff n` | `∏_{m<n} cFactor m` |
| `cCoeff_succ` | `c_{n+1} = cₙ · f_n` — the audit's recurrence |
| `cFactor_ne_zero` | each factor is nonzero |
| `cFactor_natDegree` | `natDegree (f_m) = 2m+1`, **including** `m = 0` |
| `cCoeff_ne_zero` | `cₙ ≠ 0` (product of nonzeros in a domain) |
| **`cCoeff_natDegree`** | **`natDegree (cₙ) = n²`** |

Verified with `lean`-direct (`LEAN_PATH` against the restored oleans, **exit
0**) rather than `lake build`, per the repo's verify recipe. Axiom audit:

```
'QOU.QBeta.cCoeff_natDegree' depends on axioms: [propext, Classical.choice, Quot.sound]
```

— the three standard Mathlib axioms, **no `sorryAx`**; likewise for the other
three declarations. Zero `sorry` / `admit` / `native_decide` in the file.

### The prior Lean file proves the *other* half — and the audit over-claimed it

`QOU/Mass/C1FormalSolutionGrowth.lean` (2026-08-01, sorry-free) already exists.
It defines

```lean
def c1FormalDeg (n : ℕ) : ℕ := ∑ m ∈ range n, (2 * m + 1)
theorem c1FormalDeg_eq_sq (n : ℕ) : c1FormalDeg n = n ^ 2
```

and imports **no `Polynomial` at all** (only `BigOperators` + `Tactic.Ring`).
`c1FormalDeg` is *defined* to be the sum, so `c1FormalDeg_eq_sq` is the pure-`ℕ`
identity `Σ_{m<n}(2m+1) = n²`. That is true and correctly proved — but on its own
it says nothing about the coefficients `cₙ`: nothing in that module mentions the
recurrence, the factor `f_m`, or `natDegree`. The name asserts "the C1
formal-solution degree"; the content is a fact about natural numbers.

So the 08-01 audit's summary — *"the ∞ formal solution is now explicit and its
divergence **proved** (`deg = n²`)"* — over-states what that file establishes.
The divergence claim needs the *polynomial* degree, which is the
no-cancellation step, and that was the missing half.

**This is not a criticism of that file**, which is honest about what it states;
it is a correction to the audit line that cites it as proving the divergence.
`cCoeff_natDegree_eq_c1FormalDeg` now closes the gap by proving the genuine
`natDegree` equals `c1FormalDeg`, which is what earns that definition its name.

(Method note: my own corpus-grep for this work searched Borel/D-ladder terms and
missed this file. It surfaced only when reading the 08-01 audit's "What landed"
list — a reminder that the grep is necessary, not sufficient.)

**Where the mathematical content actually sits, in the Lean.** The two
disequalities `2m ≠ m` and `2m+1 ≠ m` are discharged from `m > 0` and are
exactly the no-cancellation fact; they are what the `m = 0` branch cannot
supply, which is why that case is split off and closed separately on
`f₀ = 2X − 1`. Additivity of `natDegree` is `natDegree_mul` applied with both
non-vanishing hypotheses — i.e. the domain structure of `ℤ[X]` is used, not
assumed away. A file proving only `Σ_{m<n}(2m+1) = n²` would have been pure
`Nat` arithmetic asserting nothing about polynomials; that is the easy half and
is deliberately not what is formalized here.

## Coordination

The D-ladder / q-Borel front is **owned** — `qou-dri7` (W9, in-progress) and
`qou-b00b` (F1, in-progress). This is a deliberately small, disjoint
contribution to the shared premise rather than a parallel attack on the
Stokes multipliers themselves; it should not collide with either. The live
odd-channel route remains q-Borel / Écalle acceleration of the D-ladder per
[`2026-07-17-1ppq-path-reassessment.md`](2026-07-17-1ppq-path-reassessment.md),
and the Fantini–Wheeler summability structure
([`2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`](2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md))
is the literature anchor for the resummation side.
