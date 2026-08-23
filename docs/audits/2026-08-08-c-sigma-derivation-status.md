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
asymptotic expansion of the Kashaev invariant of `5_2` (`library/ki52/ki52.pdf`,
Theorem 1.1) is a **rigorous theorem**, and its 1-loop constant satisfies

```
|ω| = 0.65620337047140662        (all 10 digits Ohtsuki prints)
k·|τ_DG(5_2)|^{−1/2} = 0.65620337051419987
```

on a **cubic** trace field (discriminant −23), so not a quadratic coincidence.
→ addendum in `docs/audits/2026-08-08-per-cusp-factor-dissolves.md`

## THE ONE ASSUMPTION BEING CARRIED — read this before citing the upgrade

> **AMENDED 2026-08-08 — it is not one assumption, it is two, and only the
> second is actually assumed.** Full argument in
> `docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md`.
>
> * **The exponent `−1/2` is NOT assumed.** For any pair of manifolds
>   `k_i = k_j` and `p_ij = −1/2` are algebraically the same statement, so the
>   `k_c`-constancy checks in this very document were exponent measurements all
>   along. The 17-digit `k_1 = k_2` agreement *is* `p = −1/2` to 17 digits. A
>   free four-point fit — 4 points, 2 parameters, 2 residual degrees of freedom,
>   so a test that can actually fail — returns `p = −0.4983` and `k = 0.70699`
>   against the predicted `2^{−1/2}`.
> * **What IS assumed is that `c_σ` depends on `τ` ALONE.** A law
>   `c_σ = k·|τ|^p·f(M)` with `f` weakly varying fits the four points equally
>   well, and nothing in the corpus excludes it. That is the load-bearing part.
>
> **AMENDED AGAIN, same day — the FORM is in the literature; the CONSTANT is
> not.** `library/arxiv-0903.2472v1/0903.2472v1.pdf` (Dimofte–Gukov–Lenells–Zagier) was sitting
> downloaded and cited nowhere in the repository. Read. Its eq (2.3) is
>
> ```
> S₁^(ρ) = ½ log( T(M; E_ρ) / 2 )      ⇒   one-loop factor = 2^{−1/2}·T^{1/2}
> ```
>
> * **`k = 2^{−1/2}` IS still calibrated.** An earlier version of this amendment
>   said it "is the `/2` inside their logarithm" and that it was never a fit.
>   Retracted. DGLZ carry a `/2` in (2.3), a `+log 2` in (4.5) between `S₁` and
>   the colored-Jones coefficient `s₁`, and a `log π` shift against
>   Gukov–Murakami — and fix their integration constants against colored-Jones
>   asymptotics. The corpus measures `c_σ` from that same asymptotic, so it
>   matches `s₁`, under which the relation is `T = 4/|τ_DG|` rather than
>   `1/|τ_DG|`. A factor of 4 from a convention choice; the constant cannot be
>   lifted.
>   **Superseded later the same day, for links only.** "Cannot be lifted *from
>   DGLZ*" remains true and is the whole of what was shown here. But `k` does not
>   have to come from DGLZ: van der Veen's colored-Jones asymptotic for the
>   Whitehead chains gives `c_σ = 2^{1/2−n}(n²+m²)^{−1/4}` outright
>   (`n = c+d`, `m = 4a−c+d`), reproducing `k = 2^{−1/2}` with no calibration and
>   no convention to reconcile. So on the **link** side `k` is derived, and the
>   `4_1` calibration is corroborated rather than required; on the **knot** side
>   this entry stands unchanged, since van der Veen's family contains no knots.
>   See `2026-08-08-vdv-constant-closed-form-and-the-open-bridge.md`.
> * **What IS invariant is the exponent** — no multiplicative constant changes
>   `−1/2` — so the FORM transfers and the prefactor does not. The `T^{+1/2}` vs
>   `|τ|^{−1/2}` sign is likewise a choice of variable, verified to 1.3e−10 on
>   `5_2` and 6.2e−21 on `L5a1`. Read correctly that agreement says **one
>   constant serves both cusp numbers**, which is this corpus's own empirical
>   result — DGLZ assert nothing about cusp-independence, and Ray–Singer torsion
>   on a cusped manifold needs a basis of `H¹` whose rank is the cusp number.
> * That also dissolves the Ohtsuki–Takata discrepancy noted a moment ago — DGLZ
>   carry `+1/2` in the torsion too.
> * Eq (2.3) is stated for a **general** 3-manifold `M` with a flat `G_C` bundle,
>   with **no** restriction to knots, two-bridge knots or cusp number. So the
>   "`c_σ` depends on `τ` alone" part above is a cited result — for the FORM. The
>   NORMALISATION at `c ≥ 2` is a separate, still-open question, and it is the
>   one with a track record here (the retracted `2^{(c−1)/2}`, and L6a4's
>   unexplained 0.35%).
> * `jones_1loop_c0_calibration_fig8.py`'s `exp(2c₀) = 1/(2|τ_DG|)` coincides
>   with eq (2.3) under one convention reading and differs by the eq (4.5)
>   `log 2` under the other — a structural echo, not provenance for the constant.
>
> **What is actually left is RIGOUR.** Eq (2.3) is a one-loop saddle-point /
> Feynman-diagram derivation (Witten 1989, Bar-Natan–Witten 1991,
> Gukov–Murakami 2006), not a theorem. And the gap is not link-shaped: the
> formula already covers links, and the missing proof is missing for `4_1` too.
> Wherever this document says "no theorem covers the link case", read it as a
> statement about proof status, not about the formula's reach.
>
> Machine-checked:
> `computations/probes/one_loop_dglz_prefactor_identification_probe.py`.
>
> The text below stands as written; read it with all of the above in mind.

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
