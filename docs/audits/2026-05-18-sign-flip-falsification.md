# Sign-Flip Hypothesis Falsification (Structural)

**Date:** 2026-05-18
**Branch:** `claude/lambda-scale-conjecture-proof` (PR #701)
**Status:** Stronger negative result — the natural Wedderburn-sum family is **completely excluded** as a source of `λ_scale = 5/2 − h²·G`.

## The hypothesis tested

After the original conjecture `λ_scale = 5/2 − h²·G` was falsified
(Family A gave `5/2 + 3h²/4`, opposite sign), a natural question:
**could a sign-flipped variant of the Wedderburn sum give the
negative h² coefficient?**

Specifically, can we find signs ε_λ ∈ {±1} such that

$$
  \lambda_\varepsilon(q) := \frac{1}{4} \sum_{\lambda \vdash 4}
                            \varepsilon_\lambda \cdot \dim_q V_\lambda
$$

equals `5/2 − h²·G` to leading orders?

## Exhaustive search result

At H_4 there are 2⁵ = 32 sign assignments. Computed each
symbolically; only the **all-positive** assignment gives the
required leading 5/2 at q=1:

| Sign combo (ordered by λ shape) | Leading at q=1 | h² coefficient |
|---------------------------------|----------------|----------------|
| **+++++** | **5/2** ✓ | **+3/4** |
| All other 31 combos | ≠ 5/2 | — |

**Reason:** the q=1 dimensions are {1, 3, 2, 3, 1} summing to 10.
Only the all-positive combination achieves 10; any single negative
flip changes the sum by 2 or 6 or 4 — none preserves 10.

Since the only viable sign assignment is +++++, the h² coefficient
is forced to be the **sum** of h² coefficients from the three
non-trivial dim_q expansions:

- dim_q V_(3,1) = 3 + h² (contributes +1)
- dim_q V_(2,2) = 2 + h² (contributes +1)
- dim_q V_(2,1,1) = 3 + h² (contributes +1)
- dim_q V_(4) = 1 (no h-term)
- dim_q V_(1,1,1,1) = 1 (no h-term)

Total h² in sum: 3. After /4: **+3/4**.

**No sign-flip can produce negative h² coefficient** while
preserving the leading 5/2.

## What this rules out

The natural Wedderburn-block family:

$$
  \mathcal{F}_{\text{WB}} = \left\{ \frac{1}{4} \sum_\lambda \varepsilon_\lambda \cdot \dim_q V_\lambda
                                    : \varepsilon_\lambda \in \{\pm 1\} \right\}
$$

is **completely excluded** as a source of `λ_scale = 5/2 − h²·G + O(h⁴)`.

The empirical form must come from a DIFFERENT categorical
construction:

1. **Non-Wedderburn-sum**: a quantity that isn't `Σ ε_λ dim_q V_λ`,
   e.g. a trace of a specific NON-identity braid, or a non-linear
   combination of dim_q values.

2. **Higher Hecke level** (H_5, H_6, ...): perhaps the proton isn't
   actually at H_4 in the relevant sense, and the half-symmetric
   count 5/2 is a numerical coincidence at this specific level.

3. **Geometric (Yekutieli-Stokes) contribution**: a TOPOLOGICAL
   invariant that adds a NEGATIVE h² correction on top of the
   +3h²/4 from the algebraic Wedderburn sum, ending with net
   coefficient -G.

4. **The form is genuinely transcendental/dilogarithmic**: not a
   polynomial in h at all, but involves Bloch-Wigner, Clausen, or
   similar functions whose h-expansion has the right coefficients
   by accident.

## Implications for the conjecture

| Status | Result |
|--------|--------|
| Family A: `5/2 + 3h²/4` | ✅ PROVED (sympy + Lean) |
| Family B: `5/2 − h²·G` | ❌ Empirical only (5.4 ppm), structurally unfounded |
| Sign-flip family | ❌ **EXCLUDED structurally** |
| Wedderburn-block family overall | ❌ **EXCLUDED** as λ_scale source |

The original conjecture's specific form was based on a
PSLQ-style numerical hit, not a categorical construction. The
empirical 5.4 ppm match to CODATA m_p remains a tantalising
near-miss, but it's no longer supported by the natural categorical
candidate.

## Open R&D directions

Now that the sign-flip family is excluded:

1. **Search the geometric family**: λ_scale = π_alg + π_geom where
   π_geom involves Vol(B_3)/8 = G in a structurally meaningful way.

2. **Test transcendental ansätze**: dilogarithm and Clausen values
   at specific arguments. Vol(4_1) = 2·Cl_2(π/3); maybe λ_scale
   involves a similar identity.

3. **Check the Borromean baryon formula's foundations**: if no
   substrate form gives `5/2 − h²·G` exactly, perhaps the Borromean
   formula itself needs refinement.

4. **Stop chasing the specific 5.4 ppm match**: if it's a numerical
   coincidence, the right next step is to find a categorical λ_scale
   that gives close-to-CODATA but with a derivable form, rather
   than insisting on the original conjecture's exact form.
