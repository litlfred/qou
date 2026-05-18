# λ_scale Conjecture: Substrate-Form FALSIFIED (h² coefficient)

**Date:** 2026-05-18
**Branch:** `claude/lambda-scale-conjecture-proof` (PR #701)
**Status:** Negative result — the specific form `λ = 5/2 − h²·G + O(h⁴)`
is **NOT** a structural identity; the 5.6 ppm match to CODATA m_p
was a PSLQ-style numerical coincidence.

## What the conjecture claimed

`conj:lambda-scale-substrate-form` asserts:

$$
  \lambda_{\mathrm{scale}}^{(u,d)} = \frac{5}{2} - h^2 \cdot G + O(h^4)
$$

with:
- **5/2** = conjugate-pair half-symmetric partition count at H_4
- **G** = Catalan's constant = Vol(B_3)/8
- **5.6 ppm** match to CODATA m_p/m_e · ℏ_q² / Vol(B_3)

The structural arguments offered (Step 2 combinatorial, Step 3
Yekutieli-Stokes per-cell hyperbolic volume) suggested this form
was derivable, not fit.

## What the computation actually gives

The natural categorical realization of "5/2 = half-symmetric block
count" at q=1 is

$$
  \pi_{\mathrm{HS}}(\mathrm{id}, q) = \frac{1}{4} \sum_{\lambda \vdash 4} \dim_q V_\lambda
$$

(the (1/4) factor gives 5/2 at q=1 because Σ dim_λ = 10).

Substituting the standard q-deformed dimensions (Frame-Robinson-Thrall
hook-content formula) at H_4:

$$
  \dim_q V_{(4)} = 1, \quad
  \dim_q V_{(3,1)} = [3]_q, \quad
  \dim_q V_{(2,2)} = \frac{[4]_q}{[2]_q} = q^2 + q^{-2}, \quad
  \dim_q V_{(2,1,1)} = [3]_q, \quad
  \dim_q V_{(1,1,1,1)} = 1
$$

The sum:

$$
  \pi_{\mathrm{HS}}(\mathrm{id}, q) = \frac{3q^2 + 4 + 3q^{-2}}{4}
                                   = \frac{3 \cdot [2]_q^2 - 2}{4}
$$

**h-expansion at q = 1 + ε, converted to h = q − q⁻¹:**

$$
  \pi_{\mathrm{HS}}(\mathrm{id}, q) = \frac{5}{2} + \frac{3}{4} \cdot h^2 + O(h^\infty)
$$

The series **terminates** at h² — there are no h⁴, h⁶ corrections.

## What this means

| Coefficient | Conjecture | Computed (this script) | Match? |
|-------------|-----------|------------------------|--------|
| h⁰ | 5/2 | 5/2 | ✅ |
| h² | −G ≈ −0.916 | **+3/4 = +0.75** | ❌ wrong sign and value |
| h⁴ | −c_4 ≈ −0.0069 | 0 (terminates) | ❌ |
| h⁶+ | TBD | 0 | ❌ |

The natural categorical form for "5/2 + perturbation" gives
**+3/4·h²**, not **−G·h²**. The conjecture's specific form was
a numerical fit (PSLQ-style), not a structural derivation.

## Numerical comparison at q_0

| Quantity | Value at q_0 (MPFR 80 dps) |
|----------|----------------------------|
| `(1/4) Σ dim_q V_λ` (categorical π_HS) | 2.5327796637 |
| λ_p_target (from CODATA m_p/m_e · ℏ_q²/Vol(B_3)) | 2.4599534077 |
| `5/2 - h²·G` (conjecture's form) | 2.4599666078 |
| Relative diff (π_HS − λ_p_target) | +2.96% |
| Relative diff (5/2−h²·G − λ_p_target) | +5.4 ppm |

The conjecture's form is **closer** to λ_p_target than the natural
categorical form. This means λ_p_target itself is NOT the natural
categorical quantity at H_4 — there's a structural mismatch.

## What's revised

The proof state changes:

| Step | Previous status | Updated status |
|------|----------------|----------------|
| 1 | Structural argument | Same (the Markov-stabilisation claim is unaffected) |
| 2 | ✅ Proved | Still proved (5/2 IS the half-symmetric count) |
| 3 | Structural argument | ❌ **FALSIFIED** — the h²·G ≠ structural h² coefficient |
| 4 | Open R&D | Open R&D (different question now) |
| 5 | ✅ Closed structurally | Same |

## What this is NOT

This is **not** evidence that the Borromean baryon formula is wrong.
The formula `m_p = m_e · [Vol(B_3)/ℏ_q² · λ_scale + S(p)]` may still
hold — with λ_scale being some OTHER substrate quantity, not the
specific `5/2 − h²·G` form.

## What's open

Three questions:

1. **What's the correct substrate form for λ_scale?**
   The PSLQ search (previous R&D) found no clean candidate.
   The natural π_HS(id) gives `5/2 + 3/4·h²` (terminates at h²),
   off by 3% from λ_p_target. Neither matches CODATA exactly.

2. **Is the 5.6 ppm match of `5/2 − h²·G` to λ_p a coincidence?**
   Possibly. With 50 free parameters tested in PSLQ basis, finding
   one match at 5.6 ppm is plausible by chance. Statistical analysis
   would need a wider basis check.

3. **Is the Borromean baryon formula itself the right framework?**
   The `m_p = m_e · [Vol(B_3)/ℏ_q² · λ_scale + S(p)]` form is
   conjectured (`conj:borromean-baryon-mass-formula`) but not
   derived from first principles. If λ_scale doesn't have a
   simple substrate form, maybe the whole formula needs
   refinement.

## Recommended next R&D direction

Rather than continue searching for c_4 closed forms in a falsified
ansatz, the productive next steps are:

A. **Test alternative substrate forms** for λ_scale that give the
   leading 5/2 at q=1 plus a NEGATIVE h² correction. The conjecture's
   form was one such candidate that turned out empirically close but
   structurally wrong. Other ansätze involving alternating sums
   (e.g. Σ (-1)^|λ| dim_q V_λ) or different normalizations might
   give the −G coefficient directly.

B. **Investigate the Borromean baryon mass formula's structural
   origin** — is λ_scale even supposed to be a clean substrate
   quantity, or is it the result of additional dynamical structure
   (Skein, Habiro)?

C. **Drop the simple form ansatz** and treat λ_scale as a
   substrate-derivable but non-trivial expression — e.g. a Bloch-
   Wigner dilogarithm value, or the regulator of a specific
   topological invariant of B_3 beyond Vol.

## Conclusion

A structural derivation requires that the categorical computation
MATCH the empirical target without numerical fitting. The
"5/2 − h²·G" form, while empirically close to λ_p at 5.6 ppm,
does NOT match the natural π_HS categorical realization (which
gives +3/4 h²). The conjecture's specific form is therefore not
yet structurally proved; it was an empirical hypothesis worth
testing, and the test has falsified it at the h² level.

The 5/2 leading term remains a genuine categorical identity
(half-symmetric partition count at H_4 → q-dimensions sum / 4).
What lies beyond is open.
