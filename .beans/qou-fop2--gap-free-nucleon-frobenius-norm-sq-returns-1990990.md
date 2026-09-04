---
# qou-fop2
title: 'GAP: free_nucleon_frobenius_norm_sq returns 1.99/0.99/0.87 for D/T/He3, not the documented identity limit 1'
status: todo
type: task
created_at: 2026-09-04T21:15:22Z
updated_at: 2026-09-04T21:15:22Z
---


Split out of `qou-8w8v` (the rescaling-discard fix), which asked what this
function actually returns and got an answer that does not belong in a scaling
bean.

## Measured

    D    1.988392799
    T    0.991042245
    He3  0.869097004

`computations/hecke_core_legacy.free_nucleon_frobenius_norm_sq`'s docstring
says the intended value is the identity limit

    ||W_free||^2 = sum_lambda w_lambda = 1   (Wedderburn trace identity)

It is not 1, the three atoms do not agree with each other, and D is off by
essentially a factor of two.

## Not the rescaling bug

`max_ln = 0` for all three on the default Rust path, so the `exp(-2*max_ln)`
scaling `qou-8w8v` fixed was inert here — these numbers are identical before
and after that fix. This is a distinct defect.

## What is actually wrong

The function computes

    sum_lambda w_lambda * (chi_lambda(W_free) / d_lambda)^2

which collapses to `sum_lambda w_lambda = 1` only when
`chi_lambda(W_free)/d_lambda = 1` for every lambda — that is, only when
W_free is the IDENTITY braid. It is not. "Free" removes the INTER-nucleon
crossings and keeps the INTRA-nucleon ones, so each nucleon still contributes
a non-trivial 3-strand braid and its character is not its dimension.

The docstring already contains the honest version of this:

    TODO: proper tensor-product decomposition via H_3(q)^{⊗A} restriction.
    For now: ||W_free||^2 ≈ Σ_λ w_λ · 1 = 1 (Wedderburn trace identity).

So the gap is known and written down — but the code does not implement the
"for now" approximation either. It implements neither the tensor-product
decomposition nor the constant 1; it returns a third thing, and callers get
that third thing while the docstring describes the first two.

## Why it stayed hidden

T at 0.991 and He3 at 0.869 both look like plausible numbers near the claimed
1 and survive a casual glance. Only D at 1.988 makes it unmissable. This is
the same failure mode `qou-8w8v` warned about for the scaled return: when the
intended answer is exactly 1, a wrong value still looks like an answer.

## Scope

1. Decide which of the two documented intentions is wanted: the honest
   H_3(q)^{⊗A} restriction, or the constant-1 approximation stated plainly as
   an approximation.
2. If the decomposition: implement the branching-rule combination the
   docstring's TODO describes, and check `||W_free||^2` against it per atom.
3. If the approximation: return 1 explicitly and say so, rather than returning
   a character sum that is neither.
4. Either way, find the consumers first — the value feeds the Frobenius
   pairing route, so changing it moves published numbers. Identify which
   witnesses before touching it.

Do NOT "fix" this by adjusting a tolerance or by normalising the result to 1;
the discrepancy is the information.
