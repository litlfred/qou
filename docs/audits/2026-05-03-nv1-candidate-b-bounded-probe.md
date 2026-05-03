# NV-1 candidate (b) — bounded probe

**Date.** 2026-05-03
**Target.** $N_v = 1{,}445{,}519$
**Conjecture under probe.**
[`conj:nv-as-bring-period-rank`](2026-05-02-nv-frob-filter-conjectures.md)
(candidate (b) of the NV-1 trio).

## Scope

This is a STRICT bounded probe — closed-form arithmetic only, no DP
arrays of size $> 10^4$.  It is **not** a closure of candidate (b).
The full Bring-period-lattice computation (Riemann period
integration on $y^2 = x^5 - 1$) is research-grade open work and is
not addressed here.

The probe is meant to be sharply diagnostic: if $N_v$ is prime, then
any "rank decomposition" by representation dimensions of $S_5$ (or
$S_5 \times \mathbb{Z}/2$) cannot use the trivial dim-1 generator
multiple times *without arithmetic gymnastics*; conversely if the
prime can be written as $4a + 5b + 6c$ with **small** non-negative
$(a, b, c)$, the candidate stays plausible.

## Step 1 — primality

Using `sympy.isprime` and `sympy.factorint`:

| Field | Value |
|-------|-------|
| `N_v` | $1{,}445{,}519$ |
| `isprime(N_v)` | `True` |
| `factorint(N_v)` | `{1445519: 1}` |
| `N_v mod 4` | $3$ |
| `N_v mod 5` | $4$ |
| `N_v mod 6` | $5$ |

So $N_v$ is **prime**.  This is sharply diagnostic: any rank
decomposition into $S_5$ irrep dimensions either (i) leans heavily
on the dim-1 trivial reps, or (ii) requires fine-tuned multiplicities
in the $\{4, 5, 6\}$ dims.

## Step 2 — minimum-coin decompositions (pending)

Pending step 2.

## Step 3 — verdict

**Partial-probe (step 1 only).**

## Handoff

Full Bring-period-lattice machinery on $y^2 = x^5 - 1$ remains
research-grade open work.  See `docs/audits/conjecture-cones.md`
and the candidate-(b) entry of the
[NV-1 conjectures memo](2026-05-02-nv-frob-filter-conjectures.md).
