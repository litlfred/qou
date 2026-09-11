# A=4 measured: the 2nd-order Magnus pairing stays POSITIVE at the alpha particle

Bean `qou-za3q`. Producer `computations/deltalambda/he4_magnus_omega2_sign_sparse_probe.py`,
witness `computations/deltalambda/he4-magnus-omega2-sign.witness.json`.

## The number

```
P_total(A=4) = 34.1260272853576529271380692762741452981457684651471317452205
P_total_sign = +1
P_control (rho = I, must vanish) = 0.0      control_tr_M_Omega2_vanishes = True
per-partition split = 33+ / 42-             partitions = 77/77
sign_flip_vs_A3 = False
```

## The sign-vs-A map, corrected

| A | nucleus | P | sign |
|---|---|---|---|
| 2 | deuteron | — | **−1** |
| 3 | triton | +2.4701927 | **+1** |
| 4 | ⁴He | +34.126027 | **+1** |

**There is exactly one sign change in A = 2, 3, 4, and it sits between the
deuteron and the triton — not at the alpha particle.** The doubly-magic A=4
point is unremarkable for this observable.

This is the *opposite* of the question the probe was written to ask. Its
docstring asserted "A=3: P<0 — NO flip vs A=2" and framed A=4 as "does P
continue the negative run?". There was no negative run to continue: A=3 is
positive, confirmed by the committed triton witness and by a fresh 30/30 re-run
(`sign_flip_vs_A2 = True`). Bean `qou-rfhj`.

## The stale premise had propagated into the generated verdict

Worth recording because it is not a comment — it is the machine-written
conclusion that lands in the witness and gets quoted downstream. Both verdict
branches hardcoded the premise:

```python
f"NO MOVE — P(A=4) has the SAME sign as A=2 and A=3 (all {run_desc[P_sign]}; {pat}). "
```

which emitted, against its own printed data `A2=-1 A3=+1 A4=+1`:

> "P(A=4) has the SAME sign as A=2 and A=3 (all positive; A2=-1 A3=+1 A4=+1) …
> the 'flips positive at A≥3' reading fails not just at the triton but at ⁴He too"

Three errors in one sentence: A=2 does not have the same sign; they are not all
positive (the string says so while printing `A2=-1` beside it); and A=3 and A=4
both being positive *confirms* "flips positive at A≥3" rather than failing it.
The comparison **logic** was correct throughout (`flip = P_sign != a3_sign`) —
only the prose asserted an unchecked claim about A=2. Now derived from the
measured signs.

## A second field that reported an absence as a zero

`germ_hecke_check_worst_residual` accumulates over partitions **computed this
run**. On a full resume from checkpoint nothing is computed, so it emitted
`0.0` — indistinguishable from a perfect residual, and in fact a
not-measured. The full 77-partition run measured `7.23215374040307e-91`.

It now emits `null` with a companion `germ_hecke_check_partitions_measured`,
and the `correctness_gate` note says "per-block residual NOT measured this run …
this is an absence, not a zero". The independent gates still run and still pass
on a resume (`gate 1 PASS Δσ=0.0 Δgerm=1.31e-141`; `gate2 PASS` — the sparse
method reproduces the committed triton datum to <1e-30).

## Scope — what this is NOT

- **scope-(a), a dimensionless SIGN datum.** Not a MeV: the Δ_λ magnitude gate
  is open and untouched by this.
- **Not a physical binding-sign assertion.** Mapping the sign of this pairing to
  "binding" needs the sign convention (`qou-v7ro` / #6077), cited here, not
  re-derived.
- **Per-partition sign-indefinite** (33+/42−): the total is a weighted sum of
  mixed-sign terms, not a term-wise positive object.

## What it cost, and why it nearly didn't finish

77 partitions, max dim 7700, 28661 s (8.0 h) of wall clock on 3 workers.

The run was killed **four times** by session boundaries. It survived because the
checkpoint banks per completed partition; the two earlier attempts that did not
survive were launched with `setsid nohup`, which does not outlive a boundary here
(`qou-6cm9`). The single dim-7700 partition took ~3 h on one worker and was
unbankable until it completed — the concrete form of that bean's corollary, and
the thing that was expected to make A=4 unreachable. It landed.
