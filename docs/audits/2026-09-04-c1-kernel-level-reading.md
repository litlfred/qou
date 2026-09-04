# The C1 kernel is a recurrence on the residue tower, level by level — and #6582 / #6610 read it on the wrong axis

**Date:** 2026-09-04 · **Bean:** `qou-col1` · corrects `qou-33hb` (#6582) and `qou-w0tx` (#6610); builds on `qou-60ew` (#6498), `qou-4g01` (#6474)
**Lean:** `QOU.Mass.C1KernelLevelReading` (sorry-free; `Field K`, `q` not a root of unity where stated)
**Probe:** [`c1_kernel_level_reading_probe.py`](../../computations/probes/c1_kernel_level_reading_probe.py) (exact sympy, symbolic `q` and symbolic weights)

## The correction, stated plainly

**What I asserted** (#6582, #6610, their audit docs, their scope paragraphs on
`conj:qdifference-kernel-prolongation-symbol`, their PR bodies, beans `qou-33hb` and
`qou-w0tx`, the docstrings of `C1KernelAsShiftSum` and `C1KernelDictionaryParity`):
that the kernel `L_K = (q²x − 1)σ² − (q−1)σ − (q−1)` can be read as a shift operator on
the `t`-exponent `e` of a single jet, in one of two "dictionaries" — `σ` = unit
`t`-shift with `x = q^e`, or `σ` = `t`-shift by 2 on the double cover — and that the
question "which dictionary" was wall W2.

**What is actually true.** The conjecture's own text sets `x = q^m` with `m` the **body
order**, and `prop:sw-period-residue-sum` identifies body order with **jet degree**
(`prop:binding-genfun-qdifference`: `G(x;q) = Σ_n B_n x^n` in body order). So `σ` is the
step from one jet level to the next, and `L_K` is the second-order recurrence

    [n+2]_q r_{n+2} = r_{n+1} + r_n

on the **level-indexed residues** `r_n = (Dⁿ X)(−2)` of the prolongation tower — the
periods of the prolonged differential. `D : Jⁿ → Jⁿ⁺¹` is first-order in the level, so
`L_K` is never `D` itself. The `t`-exponent readings are the special case where level
and exponent lock: for a constant-weight pure shift-1 tower `r_n = cⁿ a_{n−2}`
(`shiftOne_const_residueSeq`).

**What survives.** Every theorem in the two earlier modules is correct mathematics
about the `t`-operators it names. What does not survive is the interpretive layer:
*"if the conjecture holds, `D_q` has a non-derivative component"* (#6582) is
re-derived below on the correct axis; *"the `(−1)^m` twist is not produced by `D_q`'s
own iteration"* and *"W2 is not settled by the residual"* (#6610) are withdrawn as
statements about `D_q` — they are statements about two `t`-operators the conjecture
does not name. The "which dictionary" question is not a question the conjecture asks.

**How it was caught.** Reading the conjecture block's statement for its index
convention *before* choosing the next tranche, which I had not done for the previous
two. The corpus-grep checklist would not have caught it — the prior work used my
words. The claim-shape rule ("resolve the symbols to their declarations and check the
arity") would have: `x = q^m` names the body order in the block's first display.

## What is proved on the correct axis

| statement | Lean | content |
|---|---|---|
| rank two | `c1RecFrom_ext` | a C1 sequence from level `n₀` is fixed by its values at `n₀`, `n₀+1` (`q` not a root of unity) — the conjecture's own "two base cases" (2026-08-26 scope note) |
| level 0 | `residueSeq_zero_of_powerSeries` | `r_0 = 0` for **every** operator on a power-series seed; the involution carrier has `b_0 = b_1 = 1`, `b_2 = 2/(q+1)`, so the tower never *equals* the carrier at level 0 — the recurrence is demanded from a level on, or the indices are offset |
| level 1 | `twoOp_residueSeq_one` | `r_1 = c₂(−2) · a₀` — the branch value read through the shift-2 weight at the residue slot |
| derivative-like | `derivativeLike_twoOp_c1Rec_zero` | `c₂(−2) = 0` ⇒ `r_0 = r_1 = 0` ⇒ a C1 residue tower from level 0 is identically zero. **This is #6582's conclusion on the level axis**, invariant named: the first two residues of a derivative-like tower vanish and C1 is homogeneous of order 2 |
| transfer | `twoOp_c1RecFrom_two_iff` | for a derivative-only two-term tower with `κ = c₁(−2)c₂(−1) ≠ 0`: C1 from level 2 on the residues **⇔** `[m+4]_q s_{m+2} = s_{m+1} + s_m` on the `t¹`-coefficients `s_m = (Dᵐ X)(1)` (via #6498's `r_{m+2} = κ s_m`) |
| locking | `shiftOne_const_residueSeq` | `r_n = cⁿ a_{n−2}` — the sense in which the `t`-shift reading was a special case |

## What the probe measured (exact, symbolic)

For the Jackson + q-d/dz tower (`c₁(e) = [e+1]_q`, `c₂(e) = [e+2]_q`):

| convention | `κ = [−1]_q [1]_q` | constraint at level `m` reads | rank of `m = 0..3` | mentions `a₀`? |
|---|---|---|---|---|
| balanced | `−1` | `a_{m+3} … a_{2m+5}` | 4 | **no** |
| geometric | `−1/q` | `a_{m+3} … a_{2m+5}` | 4 | **no** |

So on the level axis the symbol identification becomes a concrete, computable
constraint: C1 from level 2 is an infinite triangular system on the seed, one new top
coefficient per level, and **the branch value `a₀` never enters** — a derivative-only
tower cannot see it (the same blindness #6582 noted for the level-2 residue, now as a
statement about the whole tower). One probe defect corrected before commit: a
finite-sum `q`-integer `Σ_{i<m} q^i` is `0` at negative `m` and silently killed
`c₁(−2) = [−1]_q`, reporting `κ = 0` for the geometric convention; the closed form
`(q^m − 1)/(q − 1)` gives `−1/q`.

## Contamination list (all re-scoped in this PR or noted here)

- `docs/audits/2026-09-04-derivative-only-dq-vs-c1-kernel.md` and
  `docs/audits/2026-09-04-c1-kernel-cannot-carry-door-v-residual.md` — dated records;
  left as written, superseded by this document (same policy as the `4.66e6` and
  `963.6×` drains).
- The two scope paragraphs on `conj:qdifference-kernel-prolongation-symbol` — **rewritten**
  here into one paragraph on the level reading plus one paragraph recording the two
  `t`-operator results as what they are.
- PR bodies #6582, #6610 — merged records; this PR's body cites the correction.
- Beans `qou-33hb`, `qou-w0tx` — correction appended.
- Docstrings of `C1KernelAsShiftSum.lean` and `C1KernelDictionaryParity.lean` — carry
  the `t`-shift framing; the theorems are unaffected. Not edited in this PR (a
  docstring-only change to a merged library module); noted so the next reader knows.

## Honest scope

- Nothing here constructs `D_q` or decides the conjecture. The transfer theorem turns
  "symbol = C1" into a constraint on `(c₁, c₂, X)`; solving it is the open work.
- The exclusion of the derivative-like class is scope-(b) **only for C1 demanded from
  level 0**. From level 2 on, a derivative-only tower is *not* excluded — it is
  constrained, by the shifted recurrence on its `t¹`-coefficients.
- Whether the physical index is "C1 from level 2" (deuteron + three-body base cases,
  per the conjecture's scope note) or an offset of the level is not settled by the
  corpus text I read; the Lean is stated for a general `n₀`.

## Reproduce

```bash
PYTHONPATH=computations python3 -u computations/probes/c1_kernel_level_reading_probe.py
```
