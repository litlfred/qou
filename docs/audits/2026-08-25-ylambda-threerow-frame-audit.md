# The ≥3-row stratum is a structural zero under convention D — which consumers still reason about it

**Date:** 2026-08-25 · **Bean:** `qou-4dq1` (sweep), instance-level `qou-58w3`, `qou-prjo`
**Tool:** [`computations/audits/ylambda_threerow_frame_audit.py`](../../computations/audits/ylambda_threerow_frame_audit.py)

## The fact this rests on — established, not re-derived

Under the canonical trace convention **D** (`z = q³/(q²+1)`, owner ruling 2026-08-15)
the Wenzl level relation collapses to `Q^r = Q²`, i.e. **`r = 2`**.
`schur_principal_mpmath` is then the SU(2) two-row specialisation `s_λ(1, Q)`, so
`y_λ = 0` for every partition with three or more rows.

Both halves are Lean-proved sorry-free on `main` — `wenzlLevel_conventionD` and
`schurPrincipal_eq_zero_iff` (all `n`, all `r`) — and
[`two_row_support_recount.py`](../../computations/deltalambda/two_row_support_recount.py)
measures what the truncation removes. Nothing here re-derives them.

Measured at the proton pin, 40 dps:

| n | partitions | ℓ(λ) ≥ 3 | max\|y_λ\| on that stratum | noise floor | structural zero | genuinely negative y_λ |
|---|---|---|---|---|---|---|
| 6 | 11 | 7 | 1.387e-42 | 1.153e-33 | yes | 0 |
| 9 | 30 | 25 | 3.343e-43 | 2.212e-34 | yes | 0 |
| 12 | 77 | 70 | 6.555e-44 | 3.966e-35 | yes | 0 |

`Q^r = 1.5179532498183459375 = Q²`, `r = 2.0`.

## Why a sweep

Code written before the 2026-08-09 ruling can carry a premise the ruling
falsifies, and it does **not** fail loudly when it does. Three failure shapes,
all observed:

1. **Round-off reported as a measurement.** A filter on `y < 0` picks up the
   ~1e-42 residue in the zeroed entries.
   [`mu3_door_budget_probe`](../../computations/deltalambda/mu3_door_budget_probe.py)
   printed *"the negative-weight blocks supply ~1/7617139225999999870250124307207290880000
   of what the door needs"* from a `Σ|y_neg|` of `1.04e-42` (fixed, PR #4673).
2. **A sum or ratio over an empty set.** Any quantity of the form
   `(something over ℓ ≥ 3) / (something else over ℓ ≥ 3)` is noise ÷ noise.
3. **A C-frame narrative running over D-frame arithmetic.** The prose describes
   `r = 2.5995` while the code returns `r = 2`, and the two never meet.

## Confirmed instance: `threerow_qcross_trend_probe.py`

This is shape (3) in its strongest form, and it prints a false arithmetic claim.

The probe's docstring, its `_D_wenzl`, its `U_STAR`, and its line-223 symbolic
identity all describe **convention C**:

```
Q^r = u³/D(u),  D(u) = −u⁶−u⁴+u³+u²+1,  u* = 1.13068544546204…,  r(q₀) = 2.5995
```

The code calls `_wenzl_constants`, which on `main` returns **convention D**.
Measured side by side at q₀:

```
Q^r from the corpus (LIVE)              1.517953249818345896   = Q²  ⇒ r = 2.0
Q^r = u³/D(u)  (the probe's own text)   1.720251751213844854        ⇒ r = 2.5995
```

The consequences are visible in its own output:

- `level r(0.98q*) = 2.0 (real);  r(1.45) = 2.0  ← COMPLEX ⇒ OFF-BRANCH` — it
  prints `2.0` and labels it complex. Under D, `Q^r = Q²` is entire; there is no
  pole, so `q*` does not exist and the "real-level branch" is all of `q > 0`.
- The level-integer ladder `q_k (r(q_k) = k)` prints `r = 2.0` at **every** rung
  from `q_2` to `q_10`.
- `⇒ q₀ ∈ (q_2, q_3);  r(q₀)=2.0 ∉ ℤ` — **`2.0 ∉ ℤ` is false.** Under C,
  `r = 2.5995 ∉ ℤ` was the real and interesting claim; under D it inverts.
- Its headline object `G_n(q) = Σ_{ℓ(λ)≥3} y_λ Δ_λ` is identically zero, so the
  "is `q_cross(n)` a structured sequence in `n`?" question has no content. The
  measured crossing list is **identical for every n from 3 to 23** —
  `1.000007 1.000032 1.000178 1.000188 1.001887 1.009783 1.092527 1.103019 1.107539 1.222267` —
  with one spurious extra root at n = 11 and n = 18. Its own summary line reads
  `first-crossing sequence: [(3, 1.000007), (4, 1.000007), …, (23, 1.000007)]`,
  i.e. twenty-one identical entries, followed by `MONOTONE INCREASING? False`.
  An n-dependent object does not produce an n-independent answer; a
  bisect-on-sign-change over round-off does.
- **The probe says so itself in section 2.** Its character-dressed object prints

  ```
  D    n= 6  F(q₀)=+0.00000e+00  crossings=3  1.000042 1.148084 1.225963
  T    n= 9  F(q₀)=+0.00000e+00  crossings=3  1.000042 1.148084 1.225963
  3He  n= 9  F(q₀)=+0.00000e+00  crossings=3  1.000042 1.148084 1.225963
  ```

  `F(q₀)` is **exactly zero** at the substrate anchor for all three isotopes, and
  the three "crossings" are again identical across isotopes and across `n`. The
  ⁴He leg was killed after 52 s of a 1308 s ETA; it was printing
  `f=+0.0000e+00` too.

**Scope, stated:** this is a scope-(a) finding about *this probe*. It does not
refute the general-`r` mathematics the probe describes — the `Q^r = u³/D(u)`
family is a legitimate object — it says the probe is *not computing it*, because
its arithmetic is pinned to `r = 2` while its narrative is pinned to `r = 2.5995`.
Either the narrative is corrected to D (and the object becomes trivial), or the
arithmetic is explicitly re-pinned to the general-`r` family and the probe declares
itself an off-canon comparison. It cannot stay as it is.

## Triage: 158 consumers, 27 flagged

The tool has two layers because a source-only detector cannot decide this.

**Layer 1 — source triage.** High recall, explicitly *not* a verdict. Its own top
hit is a **false positive by construction**: `mu3_door_budget_probe` scores 28 on
negative-weight vocabulary precisely because it now *documents* the trap and
carries the fix. A file that discusses the defect scores like a file that has it.
(The audit also flagged *itself* on the first run, for quoting `2.5995` and
`1.7202` in its own docstring; it now excludes its own path, and says why.)

Tags: `HARD-CODES C's LEVEL` is the strongest single signal;
`declares a C-vs-D comparison` means reasoning about the annihilated stratum is
**correct by design** (both tags together are expected — see
`binding_sum_C_vs_D_per_isotope_probe`); `has a noise floor` is not a clearance
but rules out the `mu3_door_budget` error.

**Layer 2 — numeric confirmation.** `--measure` evaluates the stratum directly.
A value cannot be stale, mislabelled, or re-spelled and still be nonzero. This is
the layer that decides.

`--selftest` fails unless the known instance is detected *and* the stratum
measures as a structural zero, so a future narrowing cannot quietly report a clean
tree.

## A trap the selftest caught, in the audit itself

The first version tested `sum|y| == 0`. It **failed**, reporting `1.27e-42`.

The vanishing is a polynomial identity, but in finite precision it is *reached by
cancellation*, so the computed stratum sits near 1e-42 rather than at a clean
zero — and the value depends on how `q` is spelled: `mpf("1.1099785827513808")`
gives exactly `0.0` where the full-precision `Q_MP` gives `1.27e-42`. Both are the
same structural zero. **An equality test answers a question about the arithmetic,
not about the mathematics.** Compare against a noise floor tied to the working
precision — which is exactly the fix `mu3_door_budget_probe` needed, arriving one
layer up in the tool written to find it.

## Three states, not one — measured on the top candidates

Working down the triage separates the class into three states. The distinction
matters, because only the third is a live corpus defect.

### (1) Code reasons about the stratum; the record is already honest

`mu3_frechet_perblock_probe` still filters on negative weights, but its committed
witness reads `n_negative_weight = 0`, `n_negative_y_lambda_at_9 = 0`. It has been
regenerated under D and answers 0. The code is dead weight; nothing is being
mis-stated. **No action beyond tidying.**

### (2) Stale convention-C record; the producer would now return zero

`threerow-sign-crossing.witness.json` on `main` records

```
D    F_at_qlo = 8.0529125227220376e-5   F_at_q0 = -0.19496635114594539
     sign_crossed = True   crossing_q_values = ['1.0536500613326059']
T    F_at_q0 = -2.3181589081699395      sign_crossed = False
3He  F_at_q0 = -2.8064582609621747      sign_crossed = False
```

Order-unity magnitudes — so this is a **C-era number**, not a sign taken of noise.
Re-run on `main` today:

```
D    n= 6  F(q_lo)=+0.00000e+00  F(q₀)=+0.00000e+00  sign +0→+0  no crossing
T    n= 9  F(q_lo)=+0.00000e+00  F(q₀)=+0.00000e+00  sign +0→+0  no crossing
3He  n= 9  F(q_lo)=+0.00000e+00  F(q₀)=+0.00000e+00  sign +0→+0  no crossing
VERDICT: sign crossing on (1,q₀] in the ≥3-row object — NO
```

**The verdict inverts**: the committed record says the deuteron ≥3-row object
crosses sign at `q = 1.0537`; the live producer says the object is identically
zero and there is no crossing. Nothing on `main` marks the committed number as
C-frame. `threerow-4he-completion.witness.json` has the same shape
(`sign_qlo = 1`, `sign_q0 = -1`, plus `sign_change_brackets` at 1.19–1.25 and
1.33–1.44).

Two things worth noting about the re-run. Its character-free leg still reports
`CROSS @ q=[1.0001396…, 1.0002147…, 1.0052872…, 1.0082994…]` while simultaneously
printing `G(q_lo) = G(q₀) = +0.00000e+00` — sign flips located in round-off,
the `mu3_door_budget` shape again — and those crossing lists are **identical for
n = 6 and n = 9**. And its three assertions **all pass**, because they check
internal consistency rather than whether the object is nonzero. A naive
regeneration would therefore land a green witness with vacuous content.

### (3) Stale record *and* the producer now refutes it — the live defect

`ylambda-sign-content-threshold.witness.json`. Committed on `main`:

```
rule_holds_all_partitions   computed 1  expected 1  passed TRUE
no_threshold_degeneracy     computed 1  expected 1  passed TRUE
by_n: n_negative_y = 0, 0, 1, 1, 3, 4, 8, 10   (n = 2 … 9)
```

That `10` at n = 9 is exactly the convention-C count. Re-run on `main` today:

```
rule_holds_all_partitions   computed 0  expected 1  passed FALSE
no_threshold_degeneracy     computed 0  expected 1  passed FALSE
RESULT: FAILED — see mismatches above. The rule as stated is wrong.
```

and every mismatch reads `predicted=1 measured=-1 y=0.0` — the "measured sign" is
being taken of a value that is exactly zero.

**So `main` currently carries a green assertion for a claim its own producer
refutes.** The probe's thesis — *sign(y_λ) is a content-threshold parity* — is a
statement about a sign structure that convention D removed: under D, 25 of the 30
partitions of 9 have `y_λ = 0` and none is negative.

This one is not merely stale bookkeeping. A passing assertion is what the QA
pipeline reads as evidence.

## Layer 3 — provenance dating, and the trap in it

There is a third, cheap discriminator that needs no compute and is orthogonal to
both the source scan and the re-run: **when was the committed number produced?**

**The trap: the ruling date is not the code date.** The convention-D ruling is
**2026-08-09**. `_wenzl_constants` actually switched C → D in **`e54ffbca0a`,
2026-08-14T22:04:12Z** — five days later. A witness stamped 2026-08-12 post-dates
the ruling and is **still convention C**. Dating against the ruling mis-classifies
everything in that window.

Dating the flagged producers' witnesses against the commit:

| computedAt | convention | allPassed | witness |
|---|---|---|---|
| 2026-08-08T21:52:44 | **C** | true | `mu3-abs-choice-robustness` |
| 2026-08-08T21:52:48 | **C** | true | `ylambda-sign-content-threshold` |
| 2026-08-09T16:30:28 | **C** | true | `threerow-sign-crossing` |
| 2026-08-09T17:23:01 | **C** | true | `threerow-4he-completion` |
| 2026-08-09T18:11:26 | **C** | true | `threerow-qcross-trend` |
| 2026-08-15T00:37:38 | D | true | `probe-1b-li6-orthogonality` |
| 2026-08-15T12:54:12 | D | true | `gap10-tjon-correlation` |
| 2026-08-24T12:09:19 | D | **false** | `mu3-frechet-perblock` |
| 2026-08-24T14:28:59 | D | true | `threerow-crossing-a-dependence` |
| 2026-08-24T14:56:24 | D | true | `delta-lambda-closure-tl-support` |
| 2026-08-25T09:46:33 | D | true | `mu3-door-budget` |

**Five committed convention-C records, every one carrying `allPassed: true`.**

This corroborates the classification independently of any re-run, and it turned up
a fifth instance the source scan had ranked low: **`mu3-abs-choice-robustness`**.
Its committed `c3_MeV = -1.7687752752067383763` (T) and `-1.4054244334325435014`
(³He) are *exactly* the convention-C values PR #4673 measured at its pre-rebase
merge-base and could no longer reproduce on `main` — where the same quantity is
`-1.3723` / `-1.0338`. Two independent branches, same numbers, same conclusion.

That probe's thesis is *"is the μ₃ door verdict an artifact of `abs()`?"*, answered
`verdict_robust_to_abs: true` off `n_negative_raw_chi = 8`. Under D the |χ|-vs-signed
choice contributes **exactly zero** (#4673, measured), so the verdict would become
*trivially* true rather than measured — a different claim wearing the same word.

**Coverage caveat:** layer 3 matches witnesses to producers by filename stem, and
only 11 of the 27 flagged producers had a match. Absence from this table is not
evidence of cleanliness.

## Not done

Of the 27 flagged, **4 are now confirmed** (`threerow_qcross_trend_probe`,
`threerow-sign-crossing`, `threerow-4he-completion`,
`ylambda-sign-content-threshold`), **1 is clear** (`mu3_frechet_perblock_probe`,
state 1), and the remaining 22 are **candidates, not findings**.

None of the four was repaired here. Repair is a judgement about what each probe
was *for*, and in two cases (state 2) it is a choice between re-running — which
lands a green witness with vacuous content — and retiring the probe. That is the
author's call, not a mechanical drain.

Two further candidates share the `≥3-row` framing and the D accessor, and were
checked at source but not run: `threerow_crossing_a_dependence_probe` and
`threerow_sign_crossing_decomp`. `delta_lambda_closure_tl_support_probe` reads
`y_lambda_su_n` rather than the `schur_principal_mpmath` accessor and needs a
separate read.

Known instance already beaned by a sibling and not re-declared here:
`qou-58w3` (`he4-two-row-dominance` pins a convention-C 866/1000 that D makes
exactly 1).

---

## The arity question from #5744 — answered: the blocks stay, only the weight goes

A sibling working the Frobenius co-Casimir term of the unified mass formula
(#5744, bean `qou-bn8e`) asked whether "the ≥3-row stratum is a structural zero
under D" means the block is **absent from `Â`** or **present with zero weight**,
because `thm:frobenius-codim-universal` gives

```
τ(C_dim_q) = Σ_{λ ∈ Â} 1 / dim_q(λ)
```

and the two readings move Term 3 differently. The sibling was right that the
distinction matters and right not to guess it.

**It is the second reading. Every ≥3-row block is present in `Â` with a nonzero
quantum dimension; only the weight the trace assigns it is zero. `τ(C_dim_q)` is
unaffected, and Term 3 does not move.**

### Why — the two symbols name different objects

The vanishing theorem is about `wenzlWeight`, and the co-Casimir reads `dim_q`.
They are separate functions and neither is defined in terms of the other:

| | |
|---|---|
| `wenzlWeight r Q μ` | `schurPrincipal r Q μ / [r]_Q^{|μ|}` — the **weight** `y_λ` |
| `dim_q(λ)` | `[n]_q! / ∏_x [h_x]_q` — the **quantum dimension** |

`wenzlWeight_eq_zero_iff` concludes `wenzlWeight r Q μ = 0 ↔ r < μ.colLen 0`. It
quantifies over *all* `YoungDiagram`s and removes nothing from any index set — it
is a statement about the value of a weight function, not about the membership of
a block. The co-Casimir never reads that function.

### The vanishing is not a truncation, and that is the load-bearing part

It is tempting to read `y_λ = 0` as Wenzl's root-of-unity truncation, in which
the ≥(r+1)-row blocks really do leave the semisimple quotient. That is **not**
what is happening at the substrate pin. `wenzlWeight_eq_zero_iff` carries the
hypothesis `hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1` — `Q` is explicitly **generic, not a
root of unity**. The vanishing is the elementary fact that a Schur polynomial in
`r` variables is identically zero when `ℓ(λ) > r`; `schurPrincipal r Q μ =
s_μ(1, Q, …, Q^{r−1})` has only `r` variables.

So at `q₀` no block is truncated away. `H_n(q)` is semisimple, every `λ ⊢ n` is a
block of it, and each has a perfectly good nonzero `dim_q`. The docstring's
remark that the vanishing "is the reason the level-`r` trace factors through the
quotient by the ≥(r+1)-row blocks" is about a *quotient one may construct*; the
co-Casimir as the corpus applies it is applied to `H_n(q)` itself.

### Measured at the proton pin, n = 6, 40 dps, mpf end to end

| λ | rows | `y_λ` | `dim_q(λ)` |
|---|---|---|---|
| (6) | 1 | 0.115324224902 | 1.0 |
| (5,1) | 2 | 0.0789529624759 | 5.22044127533 |
| (4,2) | 2 | 0.046032434692 | 9.66904824567 |
| (4,1,1) | 3 | **0.0** | 10.6690482457 |
| (3,3) | 2 | 0.015123810098 | 5.44860697034 |
| (3,2,1) | 3 | **0.0** | 17.3446732767 |
| (3,1,1,1) | 4 | **0.0** | 10.6690482457 |
| (2,2,2) | 3 | **0.0** | 5.44860697034 |
| (2,2,1,1) | 4 | **0.0** | 9.66904824567 |
| (2,1,1,1,1) | 5 | **0.0** | 5.22044127533 |
| (1⁶) | 6 | **0.0** | 1.0 |

Seven of eleven blocks carry `y_λ = 0`. The **minimum** `dim_q` across those
seven is `1.0`; none is zero. `Σ_λ 1/dim_q` over all eleven is
`3.20213400122175`, against `1.47851063354769` over the ≤2-row blocks alone —
the two readings differ by more than a factor of two, which is why the sibling
was right to ask rather than assume.

### The corpus settles it independently, and this is the strongest evidence

`frobenius-codim-universal.lean` states its own worked specialisation in the
header: *"n = 3: tr_M(C_dim_q) = 2 + 1/[2]_q"*. The partitions of 3 are `(3)`,
`(2,1)` and `(1,1,1)` — and `(1,1,1)` has **three rows**. Measured:

```
(3)       rows=1  dim_q=1.0             y_λ=0.505404226504
(2,1)     rows=2  dim_q=2.01089686671   y_λ=0.247297886748
(1,1,1)   rows=3  dim_q=1.0             y_λ=0.0

2 + 1/[2]_q                            = 2.497290545604915556
Σ over ALL 3 blocks (incl. 3-row 1,1,1) = 2.497290545604915556   ✓
Σ over ≤2-row blocks only               = 1.497290545604915556   ✗
```

The three-row block `(1,1,1)` contributes a full `1/dim_q = 1` to the corpus's
own stated value while contributing zero weight. Had the ≥3-row blocks been
absent from `Â`, the corpus's `n = 3` specialisation would read `1 + 1/[2]_q`.
It does not.

### The co-Casimir could not have been applied under the other reading anyway

`SemisimpleFrobeniusAlgebra`, the class `thm:frobenius-codim-universal` is stated
over, carries `dim_q_ne_zero : ∀ μ, dim_q μ ≠ 0` as a **hypothesis**. Under the
first reading — blocks retained with vanishing quantum dimension — that
hypothesis fails and `1/dim_q(λ)` is undefined, so the sum would not merely
change value, it would not exist. Measured above: the hypothesis holds at every
block of `n = 3` and `n = 6`.

### Scope

This answers the arity question and nothing more. It says the co-Casimir's index
set and value are untouched by the D-frame stratum collapse; it makes no claim
about any *other* consumer of `y_λ`, which is what the rest of this audit is
about. The sibling's own invariance result is unaffected under either reading, as
they stated.

Reproduce: `dim_q` by the `q`-hook-length formula and `wenzlWeight` by the
bialternant in `r = 2` variables, both at `mpf(Q_50_DIGIT_STR)`, `mp.dps = 40`.

---

## State 3 resolved 2026-08-25 — the rule is C-only for a reason sharper than the numbers

`ylambda-sign-content-threshold` (bean `qou-ulxr`) is drained. The bean offered two
dispositions — retire, or restate the rule for the two-row stratum. **The second was
measured before choosing, and it does not exist.** Two independent reasons, either
sufficient alone.

### 1. Under D the threshold lands exactly ON the content lattice

This is the reason the audit did not have, and it is logically *prior* to the
`y_λ = 0` argument: it says the parity is undefined on `ℓ(λ) ≥ 3` before one asks what
`y_λ` is there.

Convention D pins the Wenzl level at `r = 2`, so `Q^r = Q²` and

```
c* = −log_Q(Q^r) = −2   EXACTLY
```

`−2` is an **attainable content** — row 3, column 1 of every diagram with `ℓ(λ) ≥ 3`.
There the test factor is `Q²·Q^{−2} = 1` exactly, so the cell is neither above nor below
the threshold. Measured margins:

| n | min \|Q^r·Q^c − 1\| | witness λ | `hnd` |
|---|---|---|---|
| 2 | 0.232052 | — | holds |
| 3 | **0.0** | (1,1,1) | UNSAT |
| 6 | **0.0** | (4,1,1) | UNSAT |
| 9 | **0.0** | (7,1,1) | UNSAT |
| 12 | **0.0** | (10,1,1) | UNSAT |

Zero, not small. That is exactly `hnd : ∀ x ∈ cells, QR * val x ≠ 1`, the hypothesis of
`QOU.MassTheory.YLambdaSignThreshold.wenzl_sign` — whose own docstring says that without
it *"the parity is genuinely undefined, not merely hard to prove."* The Lean anticipated
this failure mode precisely.

Under C, `c* ≈ −2.5995` sits strictly between two lattice points, `hnd` holds everywhere,
and the rule is well-posed. **The convention moved the threshold onto the lattice.** No
numerical drift is involved, which is why dating the record against the code switch (layer
3 above) was necessary but not sufficient to explain it.

### 2. Where it stays well-posed, it is vacuous

D forces `y_λ = 0` for `ℓ(λ) ≥ 3`, leaving the two-row stratum. A cell at row `i`, column
`j` has content `j − i`, so for `ℓ(λ) ≤ 2` the minimum content is `−1`, while a
below-threshold cell needs `c ≤ −3`. Unreachable **by construction, for every n** —
measured 0 deep cells on the surviving stratum at every `n = 2..12`, every surviving block
positive (distinct signs `{1}` at n = 6, 9, 12). At n = 12, 58 of the 70 annihilated
blocks have `P(λ) > 0` and none of the 7 survivors does: the rule's whole discriminating
power required `ℓ(λ) ≥ 4`, exactly the annihilated stratum.

### Disposition

The probe is now a **retirement record**, not deleted — the numbers were right for the
convention they were taken in. It asserts the four facts true under D
(`threshold_is_on_content_lattice`, `hnd_fails_on_three_row_stratum`,
`no_deep_cells_on_surviving_stratum`, `surviving_stratum_sign_is_constant`) and keeps the
C-frame measurement in `convention_c_record`, labelled not-live.

**The Lean is untouched and is not refuted.** `wenzl_sign` is generic in `Q` and `QR`,
sorry-free and correct; under D its premise is unsatisfiable on that stratum.
Conditional-proved is not premise-established. Two docstring scope corrections were made
with no proof change: the file's `c* ≈ −2.5995` / `margin 8.0e-2` figures are C-frame (D
gives `−2` and `0.0`), and `shallow_of_no_deep_cells`'s *"every `ℓ(λ) ≤ 3` block carries a
positive weight"* reads `ℓ(λ) ≤ 2` under D — those `ℓ = 3` blocks are zero, and fail `hnd`
regardless.

Scope-(a), about this rule under this convention. No claim that a two-row sign rule is
impossible; only that *this* threshold parity has no content there, the sign being constant.

PR #5780.

### Still open from this audit

`qou-qdtk` (`threerow_qcross_trend_probe` — D arithmetic under a C narrative) and the two
state-2 records (`threerow-sign-crossing`, `threerow-4he-completion`), whose re-run
assertions all pass because they check internal consistency rather than whether the object
is nonzero. A naive regeneration there still lands a green witness with vacuous content.

---

## State 2 resolved 2026-08-25 — the defect was a layer below what this audit recorded

`threerow-sign-crossing` and `threerow-4he-completion` are drained (PR #5794). This
audit flagged them as records *"whose re-run assertions all pass, because they check
internal consistency rather than whether the object is nonzero"*. The assertions do
all pass. **That diagnosis was not right, and the truth is worse.**

### `add_assertion(name, X, X)` — a check that compares a value to itself

`threerow_sign_crossing_probe` carried, under a comment calling them *"the headline
falsifiable fact"*:

```python
w.add_assertion("D_sign_qlo", iso_rows["D"]["sign_qlo"], iso_rows["D"]["sign_qlo"])
w.add_assertion("D_sign_q0",  iso_rows["D"]["sign_q0"],  iso_rows["D"]["sign_q0"])
```

`computed` and `expected` are the **same expression**. The assertion is `x == x`:
tautologically true, unable to fail, and rendering as `"passed": true` — which the QA
pipeline reads as evidence. It is not checking internal consistency; it is not
checking anything.

| assertion | committed (C) | re-run (D) |
|---|---|---|
| `D_sign_qlo` | `1/1 True` | `0/0 True` |
| `D_sign_q0` | `-1/-1 True` | `0/0 True` |

The deuteron object went from `F(q₀) = -0.19496…` to identically zero and the asserted
sign inverted `±1 → 0`. Both passed, both times. `threerow_4he_completion_probe` had
the identical pair (`F(q₀) = -5.9468…` → 0).

This is the compute-side twin of the Lean rule AGENTS.md already states under §"No
trivial trues, no tautologies, no laundering" — *"Tautological conclusions are banned:
`X = X` … any proposition that is provable without using any hypothesis about the
mathematical objects in question."* Nothing was checking for it on the compute side.

### The fix

A sign is a **measurement** and now lives in `add_data`. In its place a real
assertion — `three_row_object_is_structural_zero`, `max|F| < 1e-30`, with the
tolerance chosen once and justified rather than fitted: the C-era values were O(1)
(`|F(q₀)|` 0.19 … 5.9) and f64 χ noise on an O(1) product is ~1e-16, so any threshold
below 1e-16 cannot be met by a genuinely non-vanishing object. Measured: `7.50e-49`
(D), `3.788e-48` (T), `3.788e-48` (³He). **On the committed C data that assertion
fails**, which is what makes it a check.

### Corpus scale

[`computations/audits/self_fulfilling_assertion_audit.py`](../../computations/audits/self_fulfilling_assertion_audit.py)
(AST-level, `--selftest` included) over 3199 files and 3532 `add_assertion` calls:
**13 MEASURED** (both slots derived from the computation — the dangerous class) and
**17 LITERAL** (same constant twice; documentary flags). Fixing these two leaves 9,
recorded in bean `qou-ploj`.

Several of the 9 are load-bearing and overlap work already in flight:
`mu3_abs_choice_robustness` is the **fifth C-frame instance** identified by layer 3
above; `mu3_door_budget` and `mu3_frechet_perblock` are in the μ₃-door cone;
`threerow_crossing_a_dependence` is UNIT-2, which `qou-qdtk` shows is receiving a
C-frame correction about crossings above a `q*` that does not exist under D; and
`threerow_isospin_parity` is `qou-iav7`. Read `qou-ploj`, `qou-iav7` and `qou-qdtk`
together rather than fixing file-by-file.

### Lesson for this audit's own method

Layers 1–3 key on **convention provenance** — how a value was spelled, when it was
computed, whether it still reproduces. None of them can see an assertion that is
structurally incapable of failing, because such an assertion is *green in every
convention*. It took re-running a probe and reading the two arguments side by side.
A fourth layer keyed on assertion **shape** rather than value is what the audit tool
above now provides.


---

# Arc status, re-measured 2026-08-29

Re-ran all three layers against `main` (1525 commits on from this audit's branch
point). **The C-frame backlog this audit opened is closed.**

## Layer 3 — zero C-frame records remain

| computedAt | convention | allPassed | witness |
|---|---|---|---|
| 2026-08-25T18:53:21 | D | true | `ylambda-sign-content-threshold` |
| 2026-08-25T19:46:06 | D | true | `threerow-sign-crossing` |
| 2026-08-25T20:03:36 | D | true | `threerow-4he-completion` |
| 2026-08-25T21:17:47 | D | **false** | `mu3-abs-choice-robustness` |
| 2026-08-25T21:17:48 | D | **false** | `mu3-frechet-perblock` |

All five that were convention-C on 2026-08-25 have been regenerated post-switch.
Two now report `allPassed: false`, which is the honest state rather than a
regression — a probe whose object D annihilates *should* fail its own gate.
Three further D-era witnesses have since appeared on the same axis
(`markov-weight-support-conjugation`, `qbeta-d-frame-trace-baseline`,
`molien-jones-markov-general-n`), so 13 witnesses now match, none pre-switch.

## Both confirmed instances retired

- `qou-ulxr` — closed with a **better diagnosis than this audit had**. The prior
  reason is not `y_λ = 0 ⇒ sign(0)`: under D the threshold lands *exactly on the
  content lattice* (`r = 2 ⇒ Q^r = Q² ⇒ c* = −2`, an attainable content), so
  `wenzl_sign`'s `hnd` hypothesis fails and the parity is **undefined**, not
  merely zero. Measured margin `0.0` at every n = 3..12. The rule is also vacuous
  where it stays well-posed (0 deep cells, n = 2..12). Producer rewritten as a
  retirement record keeping the C measurement in `convention_c_record`; Lean
  untouched and not refuted.
- `qou-qdtk` — retired in `6ebae05c45`, same shape.

## A sibling found a sixth instance

`qou-iav7`: `threerow_isospin_parity_probe` carries the same C/D straddle and
**emits no witness at all**, so layers 2 and 3 are both blind to it — only the
source scan can see that one. In progress on another branch; not touched here.

## What this audit got wrong about itself

**The `--selftest` was anchored to a live file, and the fix broke it.**

It required `threerow_qcross_trend_probe.py` to be detected *and* to read as
hard-coding C's level. That file was retired in `6ebae05c45` — exactly what this
audit asked for — and the selftest then began failing on a clean tree, reporting
a regression that was the fix landing.

That is the worst possible direction for a check to fail in: **it cries regression
at success**, which trains a reader to ignore it. A selftest anchored to a mutable
instance goes stale the moment the instance is repaired.

Re-anchored on **per-pattern minimal probe strings** — the detector is now tested
against strings it cannot lose, and the corpus is left to the report. Layer 3's
count is explicitly a report, never a required value: zero C-frame records is the
goal state, not a failure.

**The first attempt at that fix did not work, and the negative control is what
caught it.** It used one combined fixture containing a variable named
`three_row` — which matches `ROWS`' `three[_-]?row` alternative — so sabotaging
`ROWS`' `len(x) >= 3` branch left the selftest **green**. Per-branch probes
replaced it, and two negative controls now confirm the check bites: breaking
`ROWS/len` alone fails it, and breaking `C_LEVEL`'s constant branch alone fails
it. Without those controls this selftest would have been decoration.
