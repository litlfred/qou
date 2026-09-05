# The sector trace decays where the irrep column does not — and the irrep failure diverges

> ## 🛑 CORRECTION, same day, before this document was ever quoted: **A=5 refutes the sector claim**
>
> Part 2 below reports the sector ratio `|tr_{W_k}|/C(n,k)` decaying at A=3 and A=4 where the irrep
> column does not, and calls it *"the arc's first constructive direction"*. **A=5, which was running
> when that was written and is named as pending in "What is NOT established", has now risen:**
>
> ```
> A=5 sector, ρ_true:   k=1  2.950204   k=2  0.220441   k=3  0.05628525   k=4  0.06646242  ← rise ×1.181
> ```
>
> So the tally is **A=2 ✗, A=3 ✓, A=4 ✓, A=5 ✗** — **2 of 4, failing at the largest size measured**,
> which is the direction that matters. That is not the "holds for A ≥ 3" shape Part 2 anticipated; it
> is two isolated successes with failures on both sides of them.
>
> **What this does and does not touch.** Part 1 (the irrep failure diverging, margin 1.65 → 0.272 →
> 0.0503) is a separate measurement and **stands**. The **control** stands and is still the reason
> the A=3/A=4 successes are not nothing: plain `tr(ρ)` rises at A=3 and A=4 where `ρΩ₂^P` decays, so
> whatever is happening at those two sizes is about the curvature. But *"the sector is the object to
> bound"* is **not supported**, and I should not have called it a direction on three sizes when the
> fourth was still running — the caution I pre-registered against exactly this is quoted below and I
> wrote it, then partly ignored it in the framing.
>
> A=5's remaining shapes (k=5,6,7) are still computing and can only add rises, not remove this one.

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` (rescoped) · **Scope:** (a) scope-limited — A = 2…5 at
one q₀, complete ≤2-row column. Nothing wired, no witness, no fit. **One negative sharpened into a
divergence, and the arc's first constructive direction.**

> ## 🛑 SECOND CORRECTION, same day: **A=6 refutes Part 1's RATE claim** (the failure itself stands)
>
> Part 1 below reports the `k=3→4` trace ratio growing ~4.6× per A step and concludes the route
> *"fails at a rate, not by a recoverable margin."* **A=6 has now landed and the ratio drops:**
>
> ```
> |tr₄|/|tr₃| :  1.23869  →  5.36793  →  26.4306  →  19.2541      growth ×4.334, ×4.924, ×0.728
> ceiling     :  2.04371  →  1.46067  →   1.32961  →   1.27913
> margin      :  1.6499   →  0.27211  →   0.050306 →   0.066434    ← improves at A=6
> ```
>
> **What survives:** the step **fails at A=4, 5 and 6** — three of the four sizes, passing only at
> A=3 — and by a wide margin (0.272, 0.050, 0.066 against a required 1). The failure is robust.
>
> **What does not:** "growing at a rate", and with it "fails at a rate". The margin *improves* from
> A=5 to A=6. The correct statement is **"fails at every A ≥ 4 tested, by a large margin, and not
> monotonically worsening."**
>
> **This is the third three-point trend refuted by its fourth point in one session** — after the
> A=2/A=3 margin table (#6822) and the sector reframing (correction above). The probe's own closing
> line said *"NOT an asymptotic claim: 3 sizes. Read it as a rate to test, not a limit."* That
> caveat was correct and the test came back negative; the failure was in my prose framing, which
> promoted it to a rate anyway. The ceiling half of the argument is unaffected — it is forced by
> `[n−2k+1]_q/[n−2k−1]_q → q²` and is not an empirical trend.

## Part 1 — the irrep failure is a divergence, not a near miss

The ≤2-row column's monotonicity breaks are not scattered across `k`. Read across sizes, the **same
step `k=3→4`** fails at A=3, 4 and 5; A=2's column is simply too short to contain it. That is a
**fixed-`k`** feature, invisible to a per-A verdict, so it is worth measuring as one thing.

y-weighted monotonicity at a step is exactly `|tr_{k+1}|/|tr_k| < y_k/y_{k+1} =
[n−2k+1]_q/[n−2k−1]_q` (`|c_λ| = y_λ·|tr_λ|` carries no `dim`, so the raw trace ratio is the right
quantity — using `|tr|/dim` here cost a correction in #6822). At `k=3→4`:

| A | n | `\|tr₄\|/\|tr₃\|` | ceiling | margin | verdict |
|---|---|---|---|---|---|
| 3 | 9 | 1.23869 | 2.04371 | 1.6499 | falls ✓ |
| 4 | 12 | 5.36793 | 1.46067 | 0.27211 | **rises ✗** |
| 5 | 15 | **26.4306** | 1.32961 | **0.050306** | **rises ✗** |

**Trace-ratio growth per A step: ×4.334, then ×4.924** — near-constant, ~×4.6.

The two sides move apart from both ends. The ceiling is capped at `[3]_q ≈ 3.0437` at *any* `k`, and
at **fixed** `k` it is forced downward toward `q² = 1.23205` as `n` grows — protection that cannot be
raised and additionally erodes. Against that, a trace ratio growing ~4.6× per step. The margin
collapses **1.65 → 0.272 → 0.0503**.

So the y-weighting route does not fail by a margin a sharper analysis might recover. It fails at a
rate.

## Part 2 — but the irrep traces are DIFFERENCES, and the sector decays

The corpus already named the obstruction; the bean records:

> *"a decay BOUND for two-rows must respect the difference structure — a per-sector triangle
> inequality does not decay in k."*

By `U_q(sl₂)` Schur–Weyl, `W_k = ⊕_{j≤k} S^{(n−j,j)}`, so

```
tr_{W_k} = Σ_{j≤k} tr_{(n−j,j)}        and        tr_{(n−k,k)} = tr_{W_k} − tr_{W_{k−1}}
```

A difference of two decaying sequences need not decay. So the question was asked from the other
side: **does the sector trace itself decay, per sector dimension `C(n,k)`?**

| A | irrep column, ρ_true | **sector `\|tr_{W_k}\|/C(n,k)`, ρ_true** | sector, ρ_bare | **CONTROL: sector, plain ρ** |
|---|---|---|---|---|
| 2 | 1 rise ✗ | **1 rise ✗** (into k=3, ×1.231) | decays ✓ | 1 rise ✗ (into k=3, ×1.194) |
| 3 | 1 rise ✗ | **decays ✓** | decays ✓ | **1 rise ✗** (into k=3, ×1.415) |
| 4 | **2 rises ✗** | **decays ✓** | decays ✓ | **2 rises ✗** (into k=3 and k=6) |

**The control is the column that makes this worth anything.** `tr_{W_k}(ρ)` with **no `Ω₂`** does
*not* decay — it rises at A=3 and A=4 exactly where the `Ω₂` version decays. So sector decay is
**not** a generic property of the weight filtration `W_k`, which would have made the whole reframing
deflationary; it appears when the curvature is inserted. That was the obvious deflationary reading
and it is now excluded by measurement rather than by argument.

**At A=3 and A=4 the sector decays where the irrep column does not** — and A=4 is the decisive case,
since that is where the irrep column fails twice and where the y-weighted mass fails too. The A=4
sector column, ρ_true:

```
k:              1         2         3         4         5         6
|tr_W|/C:   2.5826    0.3197    0.1176    0.1040   0.06225   0.04539
```

Signs are load-bearing here and nowhere else in this arc: the partial sum needs the **signed**
`tr_{(n−j,j)}`, which alternate for the true element (A=4: `− + − − + +`) while the bare element's are
essentially one sign. The reframing cannot be tested from `|tr|` data.

## The Temperley–Lieb framing is NOT new — I checked before writing it up

The ≤2-row restriction has a name: `H_n(q)` acting on `(ℂ²)^⊗n` factors through Temperley–Lieb, so
convention D's row cap *is* the TL quotient, and the sector traces are TL sector traces. I was about
to record that as a structural reframing. **The corpus already holds it**, and the corpus-grep is
what stopped me:

- [`2026-08-10-convention-d-ylambda-root-and-derivation.md:152`](2026-08-10-convention-d-ylambda-root-and-derivation.md)
  states the **`H_n/rad = TL_n` identification** directly, and scopes it honestly: it is
  **measured** (`qou-8iru`, n = 2…7, residual `1.34e-51`) **rather than proved for general `n`**.
- The Lean pinning of `z_D` lives in `QOU/QBeta/TemperleyLiebTower.lean`, section
  `ConventionPinning`.

So the TL connection is prior work, not a finding of this document, and anything built on it
inherits that "measured, not proved for general `n`" scope.

**What my measurement does add is an independent confirmation of the corpus's `y_λ` formula.** That
audit gives `y_λ = [n−2k+1]_q / [2]_q^n` under convention D. The `[2]_q^n` cancels in a ratio of
adjacent shapes, predicting exactly

```
y_k / y_{k+1}  =  [n−2k+1]_q / [n−2k−1]_q
```

which is what the ≤2-row column probe measures against the actual cached weights and confirms to
**1e-50** at A = 2, 3, 4, 5. That is a check of the corpus formula against independently-served
`y_λ` values, not a restatement of it — the failure mode the same audit warns about two sections
earlier (*"Verify a closed form against a quantity derived independently of it, never against your
own restatement"*).

## What this changes

**The arc's non-monotonicity looks like a difference artifact, not a failure of decay.** The natural
object carrying the decay is the **sector** trace; the irrep trace is its first difference, and
first differences of decaying sequences are not required to decay. That is a constructive direction —
the first in this arc after a run of negatives — and it is not a new mechanism I invented: it is the
one the corpus had already flagged, tested from the other end.

## Part 3 — the two surviving facts are ONE phenomenon

With the sector reframing refuted (correction at the top), what is left is Part 1's divergence and
the concentration fact. **They are the same thing measured two ways.**

Concentration is eroding and accelerating — `k=1` share of `Σ|c_λ|`, ρ_true: **77.882 → 73.499 →
59.437 %**. Asking *which* `k` takes it (`magnus_concentration_erosion_probe.py`):

| step | biggest share gainer | points | share of what `k=1` lost |
|---|---|---|---|
| A=2→3 | **k=4** (arrives this A) | +3.33 | **75.99 %** |
| A=3→4 | **k=4** | +15.59 | **110.89 %** |

`k=4` is the gainer at **both** steps, and its `|c₄|/|c₁|` runs **0.0453 → 0.3184**. So the erosion of
concentration is not a separate phenomenon from the `k=3→4` divergence of Part 1 — it is that
divergence seen through the mass rather than through the ratio. (Over 100 % at the second step
because `k=4` also took from `k=2` and `k=3`, which both fell.)

**A defect in my own metric, caught by reading its output.** The first version reported the A=2→3
gainer as `k=2` (+1.779). That was wrong in a structural way: the column grows by one shape every
two `A`, and `k=4` **does not exist at A=2**, so it had no previous share and the Δ column left it
blank — the "biggest gainer" comparison ranged over the overlap only and was therefore **blind to an
arriving term**, which is precisely the term that matters. Treating an absent previous share as `0`
rather than as undefined moves the A=2→3 answer from `k=2` to `k=4` and makes the two steps agree.
A metric that cannot see a new column entry is not a weaker metric; it is one that reports the wrong
`k`.

## What is NOT established, and one caution I registered before running

- **A labelling inconsistency between my own two probes, caught and fixed.** The column probe reports
  a rise by its **destination** `k`; the sector probe reported the **source**, so the same event read
  as "k=2" in one output and "k=3" in the other. Both now say `into k=<destination>`. Any earlier
  quotation of an A=2 sector rise "at k=2" means **into k=3**.
- **A=2 fails**, so the honest statement is *"decays for A ≥ 3"*. **A property that only starts
  holding at the third size is the shape of a small-size artifact**, and I wrote that into the
  probe's docstring *before* running it rather than after seeing the result. Two things weigh
  against dismissing it that way: A=2 is the smallest size, its column has only three entries, and
  its single rise is mild (×1.231) against A=4's irrep rises of ×3.0 and ×7.6. But that is an
  argument, not evidence.
- **A=5 is running** and is not in this document. It is the size that would make the sector claim
  3-of-4 rather than 2-of-3.
- **Nothing is bounded.** A monotone sequence is not a bound, and no tail estimate is attempted.
- **Why the sector decays is unexplained.** I have no argument for it — only the measurement.
- **The divergence in Part 1 is three sizes.** A rate read off three points is a rate to test, not a
  limit; this session has already been caught treating two agreeing sizes as a mechanism.
- **Part 1 and Part 2 are consistent, not redundant.** Part 1 says the *irrep* route diverges; Part 2
  says the irrep was the wrong object. If Part 2 holds up, Part 1 stops being the interesting fact
  about the column and becomes a statement about differencing.
