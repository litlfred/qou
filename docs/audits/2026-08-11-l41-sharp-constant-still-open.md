# L4-1 is NOT ingredient-complete — correcting my own over-claim

**Date**: 2026-08-11 · **Beans**: qou-ph2s (closed), qou-shrp (new) ·
**Epic**: qou-u1b5 (vdV Lemma 4) · **Evidence**:
[`computations/logsine_smooth_defect_constant.py`](../../computations/logsine_smooth_defect_constant.py)
+ witness.

## The over-claim

PR #5003 (L4-1c(ii)) landed `smooth_defect_squeeze` sorry-free —

    h·(φ_ext(n) − log 2)  ≤  Σ_{i<n} ∫_{cell_i} (φ(x_{i+1}) − φ(u)) du  ≤  0

— and described L4-1's ingredient list as **complete**, on the strength of
"no derivative estimate anywhere". The bound is correct and the sorry-free
claim stands. **The completeness claim does not.**

## Why it is wrong

Van der Veen's Lemma 3 is

    S̃_N ~ exp( (4N/π)·Λ(π/4) − ½·log 2N ),

and that explicit `−½·log 2N` is the `N^{−1/2}` prefactor that feeds
Lemma 4's `N^{(c+d+3)/2}`. It is not decoration: it is the polynomial order
of the whole asymptotic. Obtaining it requires the **limit** of the scaled
smooth defect, and an antitone squeeze gives only two-sided *bounds*.

Measured directly at `r = 1/2` (so `x_n = π/2`):

| N | scaled defect `D(N)` | proved interval | `½·(φ(x_n) − log 2)` | `\|D − ½·\|` |
|---|---|---|---|---|
| 200 | −0.22662468 | `[−0.451583, 0]` | −0.22579135 | 8.3e-4 |
| 800 | −0.22599969 | `[−0.451583, 0]` | −0.22579135 | 2.1e-4 |
| 3200 | −0.22584344 | `[−0.451583, 0]` | −0.22579135 | 5.2e-5 |

`D(N)` converges to the **midpoint** of the proved interval. The interval
has fixed width `0.4516` and does not narrow with `N` — it cannot, since
neither envelope depends on `N` except through `x_n`. So the squeeze
brackets the truth with a permanent **factor-2 gap** and cannot yield the
`½`.

## What this means for the epic

* `qou-ph2s` is genuinely **done** as scoped (the two-sided bound), and its
  finding — that the *sign* suffices for the bound, so no Lipschitz bound
  across the removable singularity is needed *for that* — remains correct.
* L4-1's **sharp statement** still needs the Riemann-defect refinement:
  `Σ_j ∫_cell (φ(x_j) − φ(u)) du = (h/2)·(φ(nh) − φ(0)) + O(h²)`, which is a
  mean-value / `φ'`-based argument. That is new bean **`qou-shrp`**.
* So the derivative work I called "avoidable" is avoidable for the *bound*
  and **required** for the *constant*. Both statements are true; PR #5003
  conflated them.

## Calibration note

This is the third estimate on this front to move, and the first to move in
the *pessimistic* direction: Euler–Maclaurin (called necessary, wasn't), the
Lipschitz bound (called necessary, wasn't *for the bound*), and now the
sharp constant (called done, isn't). The pattern is not "everything is
easier than scoped" — it is that **the scoping was tracking the wrong
quantity**: bounds versus limits. Downstream estimates in the epic (L4-2,
L4-5, L4-6) should be re-read with that distinction explicit, since Lemma 2a
likewise states an *asymptotic with error term*, not a bound.
