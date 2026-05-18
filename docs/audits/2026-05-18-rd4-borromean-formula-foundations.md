# R&D 4: Borromean Baryon Mass Formula — Foundational Refinement

**Date:** 2026-05-18
**Branch:** `claude/lambda-scale-conjecture-proof` (PR #701)
**Status:** Foundational analysis — proposes the Borromean baryon mass formula itself needs revision given the cumulative falsification of `λ_scale = 5/2 − h²·G`.

## Recap of cumulative findings

| R&D direction | Result |
|---------------|--------|
| Family A: `(1/4) Σ_λ dim_q V_λ` at H_4 | ✅ Proved `5/2 + (3/4)·h²` (closed form) |
| Sign-flip variants (32 combos) | ❌ All preserved leading-5/2 give +3h²/4 |
| R&D 1: Geometric Σ_geom = (5/3)·h² | Close to empirical (5e-4) but not exact |
| R&D 2: Transcendentals (Cl_2, BW, π, ln 2, ζ(3)) | No clean match |
| R&D 3: Hecke levels H_2..H_7 | All natural sums give POSITIVE h² |

**The empirical `λ_scale = 5/2 − h²·G` form is not derivable from any
tested natural categorical construction.** The 5.4 ppm match to
CODATA m_p remains a numerical near-coincidence, not a structural
identity.

## The conjecture under scrutiny

[`conj:borromean-baryon-mass-formula`](../../content/quantum-observable-universe/braids-and-knots/borromean-baryon-mass-formula.md)
asserts:

$$
  \mathfrak{m}(B) = m_e \cdot \biggl[\frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2} \cdot \lambda_{\mathrm{scale}} + S(B)\biggr]
$$

with Status #1 ("Vol-form mass formula") explicitly labelled
conjectural and Status #2 ("derivation of λ_scale") open.

## Foundational questions

### Q1: Is `Vol(B_3)/ℏ_q²` the right normalisation?

**For the muon (CAL-2 anchor):** `m_μ/m_e = Vol(4_1)/ℏ_q²` exactly
(zero ppm). This is a structural identity, not a fit.

**For the proton:** the analogous form `m_p/m_e = Vol(B_3)/ℏ_q²` gives
**746.42**, not 1836.15. So the Borromean Vol is **off by a factor of
~2.46**, which is what λ_scale is meant to fix.

Why should the proton's Vol-normalisation factor differ from the
muon's? The muon's λ-equivalent is **1 exactly**. The proton's is
**2.46**, a non-trivial multiplicative correction. If both leptons
and baryons follow `m/m_e = Vol(K)/ℏ_q²`, what is K_proton such that
Vol(K_p) = 2.46 · Vol(B_3) ≈ 18.03?

### Q2: Is the additive S(B) Skein term the right correction structure?

`rem:delta-skein-substrate-identity` shows that ΔS(n−p) = (Q_β +
m_e)/m_e ≈ 2.531 is derivable from substrate (CAL-1, CAL-2,
Vol(B_3)) at ~1000 ppm. So the Skein S(B) per baryon orientation
is structurally accessible.

But S(p) itself is set to 0 by convention. If the conjecture's
`λ_scale = 5/2 − h²·G` is falsified, then maybe **S(p) is NOT zero**
and the residual carries all the structural content.

### Q3: Should λ_scale and S(B) be unified?

The split between "Vol-form" (containing λ_scale) and "Skein
correction" (containing S(B)) is conventional. The empirical
m_p, m_n values are determined by their SUM:

$$
  \text{const}_p = \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2} \cdot \lambda_p + S(p)
$$

There are infinitely many (λ_p, S(p)) decompositions giving the
same observed const_p. The split is meaningful only if BOTH pieces
have independent structural origins. If λ_scale doesn't have a
clean form, maybe the WHOLE const_p is better described as a single
substrate-derived quantity.

## Proposed alternative formula

If the Borromean Vol-form is just a numerical anchor (not structurally
forced), an alternative ansatz is:

$$
  m_p = m_e \cdot \mathrm{Vol}(K_p) / \hbar_q^2
$$

with **no λ_scale, no Skein correction** — just the "right" knot K_p
whose hyperbolic volume directly gives m_p/m_e.

**What K_p would need:** Vol(K_p) = 1836.15 · ℏ_q² ≈ 18.03.

### Candidate K_p constructions

1. **Connect sum 9 × 4_1**: Vol(9·4_1) = 9·Vol(4_1) ≈ 18.27.
   Off by ~1.3% — not 1 ppm.

2. **A specific 9-component hyperbolic link**: Vol(L) = 18.03 for some
   specific 9-component link complement.

3. **Bring's curve / Borromean stacking**: Vol(stacked B_3) at some
   specific stacking depth.

4. **Some non-hyperbolic knot complement** under a different
   q-deformed Vol convention.

These are concrete topological R&D items; none has been computed.

## What this audit recommends

Given the cumulative falsification of the `5/2 − h²·G` form:

**Option A**: Keep the Borromean baryon formula as a conjectural
phenomenology, document that λ_scale is empirically 2.46 (matches
CODATA to 5.4 ppm via the specific `5/2 − h²·G` form) but lacks
structural derivation, and treat it as a CAL-anchored value alongside
CAL-1/2/3 (introducing CAL-4 for baryons).

**Option B**: Drop the `Vol(B_3) + λ_scale + S(B)` framework and
search for a single-knot ansatz `m/m_e = Vol(K)/ℏ_q²` for baryon-
specific K (computing Vol of various candidate 3-manifolds).

**Option C**: Accept that the baryon mass formula is intrinsically
NOT a clean function of Vol(B_3) and substrate q, and that the
empirical match (5.4 ppm) requires a more sophisticated categorical
construction beyond what the current paper provides.

## Status

R&D 4 surfaces the foundational issue but does not resolve it. The
Borromean baryon mass formula's structural status needs paper-level
discussion. This audit is for the author's consideration, not an
immediate code change.

## What this PR delivers

- Family A `(1/4) Σ dim_q V_λ = 5/2 + (3/4)·h²` PROVED (sympy + Lean)
- Sign-flip family STRUCTURALLY FALSIFIED at H_4
- Hecke-level scan (H_2..H_7) confirms positive h² always
- Three transcendental/PSLQ searches with no integer relation
- Foundational R&D 4 audit recommending paper-level revision

The structural λ_scale derivation goal cannot be reached with the
methods explored; foundational paper-level work is the appropriate
next escalation.
