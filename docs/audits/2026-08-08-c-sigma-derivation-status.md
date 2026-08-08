# `c_σ = 2^{−3/4}`: IDENTIFICATION → DERIVATION, and exactly what is being assumed

**Date:** 2026-08-08 · **Beans:** `qou-pn5j` (closed by this), `qou-fl4t`
**Authorized by:** the user, after the evidence below was recorded and the status
change deliberately left open for review.

## The claim being upgraded

```
c_σ(L5a1) = 2^{−3/4}
```

the sub-leading (1-loop) constant in the Whitehead link's volume-conjecture
asymptotic. Its **numerical value** was never in question — `whitehead_c_sigma_hiprec.py`
pins it to ~20 digits with pure mpmath, van der Veen's exact colored Jones and
Neville extrapolation, touching no SnapPy and no determinant. What was in
question was whether it is *derived* from geometry or merely *identified* as a
closed form matching a measured number.

## Why it was demoted, and why each objection is now answered

`qou-pn5j` was reopened on 2026-08-07 by PR #4691 with two objections. Both are
answered, and it matters that they are answered separately.

**Objection 1 — the geometric quantity was not well defined.**
`whitehead_c_sigma_torsion.py` computed a determinant that is *not a topological
invariant*: retriangulating gives 8 distinct values for `5_2`, 17 for `6_2`.
Calibrating on `4_1` could not detect it — 2 tetrahedra, no room to move under
Pachner moves.

*Answered.* `computations/one_loop_torsion.py` computes the Dimofte–Garoufalidis
1-loop invariant at any cusp number, verified triangulation-invariant on **13
manifolds × 25 randomised triangulations**, with controls (`is_isometric_to`,
geometric solutions only). `|τ_DG(L5a1)| = √2`.
→ `docs/audits/2026-08-07-one-loop-multicusp-derivation.md`

**Objection 2 — the per-cusp factor was fitted against its own ambiguity.**
`c_σ = 2^{(c−1)/2}|τ_old|^{−1/2}` introduced a free `c`-dependent factor of
exactly the size of the ambiguity it was fitted through.

*Answered — the factor does not exist.* Against the corrected invariant,
`k_c := c_σ·|τ_DG|^{1/2}` is the **same constant `2^{−1/2}` at `c = 1` and
`c = 2`, to 17 digits**. A per-cusp factor requires `k_2/k_1 = √2`; measured,
`0.999999999999999995`. So there is no free parameter left to fit.
→ `docs/audits/2026-08-08-per-cusp-factor-dissolves.md`

## The derivation, as a chain with no adjustable quantity

1. `|τ_DG(4_1)| = √3/2` — DG's own worked figure-eight example (eq. 3.2),
   reproduced at rel `0.0`. **Given, not fitted.**
2. `c_σ(4_1) = 3^{−1/4}` — measured from colored Jones, 17 digits,
   `whitehead_c_sigma_fig8_calib.py`. **Measured, independent of any geometry.**
3. `k := c_σ(4_1)·|τ_DG(4_1)|^{1/2} = 2^{−1/2}`. **One number, read off `4_1`.**
4. `|τ_DG(L5a1)| = √2` — computed from the geometry, triangulation-invariant,
   validated per cusp against SnapPy's cusp shapes to ~1e−59.
5. `c_σ(L5a1) = k·|τ_DG(L5a1)|^{−1/2} = 2^{−1/2}·2^{−1/4} = 2^{−3/4}`.

Step 5 is a **prediction with nothing adjustable**, and it matches the 20-digit
measured value to ~17 digits.

### Independent confirmation of step 3 on a second manifold

`k` is calibrated on `4_1` alone, which was the chain's thinnest point. Ohtsuki's
asymptotic expansion of the Kashaev invariant of `5_2` (`uploads/ki52.pdf`,
Theorem 1.1) is a **rigorous theorem**, and its 1-loop constant satisfies

```
|ω| = 0.65620337047140662        (all 10 digits Ohtsuki prints)
k·|τ_DG(5_2)|^{−1/2} = 0.65620337051419987
```

on a **cubic** trace field (discriminant −23), so not a quadratic coincidence.
→ addendum in `docs/audits/2026-08-08-per-cusp-factor-dissolves.md`

## THE ONE ASSUMPTION BEING CARRIED — read this before citing the upgrade

The chain assumes the **1-loop prefactor form**

```
c_σ ∝ |τ|^{−1/2}
```

i.e. that the sub-leading constant in the volume-conjecture asymptotic is the
inverse square root of the adjoint torsion, up to a universal constant. This is
the standard GGMW/Ohtsuki saddle-point form and the corpus has used it
throughout, but **it is validated here, not proved**:

* validated on `4_1` to 17 digits (`whitehead_c_sigma_fig8_calib.py`, whose own
  witness calls it "template validated");
* validated on `5_2` to 10 digits against Ohtsuki's theorem;
* consistent on `L6a4` at 0.35%, with that tower's normalization caveat.

So the honest statement of the upgraded claim is:

> **`c_σ = 2^{−3/4}` is DERIVED from the triangulation-invariant DG 1-loop
> invariant of `L5a1` together with a single `c = 1` calibration, assuming the
> 1-loop prefactor form `c_σ ∝ |τ|^{−1/2}`.**

Do not cite it as derived *without* that clause. The `c = 1` leg is now
theorem-backed on both sides for two-bridge knots (Garoufalidis–Yoon prove
1-loop = adjoint torsion; `4_1` and `5_2` are two-bridge), but `L5a1` is a
2-cusped **link**, and no such theorem covers it.

## What remains open

* **The prefactor form itself**, above. Proving it for links is the real
  remaining gap, and it is a research problem, not a computation.
* **The overall constant at `c ≥ 2`** is pinned only *through* the prefactor
  form. Invariance and the change-of-curve law cannot see it (they are blind to
  a factor depending only on `c`); the Jones side can, and does, but only under
  that assumption.
* **`c = 3`** remains supporting-only: `k_3/k_1 = 1.0035`, with an unresolved
  normalization+cusp offset flagged in its own witness and `p = 1.4993` against
  the exact `3/2`.

## What is retracted, and stays retracted

`|τ(L5a1)| = 2^{5/2}`, `|τ(L6a4)| = 2^6 = 64`, the per-cusp factor
`2^{(c−1)/2}`, and the `exp(2c₀) = 2^{c−1}/|det J|` "unified law" — all
properties of a non-invariant determinant on particular default triangulations.
Their replacements are `√2`, `8`, no factor, and `exp(2c₀) = 1/(2|τ_DG|)`.
