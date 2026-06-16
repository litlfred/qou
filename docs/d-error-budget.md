# Deuterium — error budget for the +1.09% residual

*Investigation of where the 10.9 million ppb residual in
`B(D) = m_e · Vol(6_2)` originates. Formally justifiable
observations only; empirical coincidences are flagged as such
and not proposed as fixes.*

## Problem statement

Zero-parameter Kashaev prediction, per
`def:algebraic-quantum-volume-specialization` route 2:

$$
  B_{\text{pred}}(D) = m_e \cdot \operatorname{Vol}_{\text{hyp}}(6_2)
$$

Compared to AME2020:

| quantity | value |
|----------|-------|
| $B_{\text{AME}}(D)$ | 2.22456612 MeV |
| $B_{\text{pred}}(D)$ | 2.2488207948647346286 MeV |
| residual | +0.02425467 MeV |
| relative | +1.0903% = +10,903,104 ppb |

Target per `docs/path-to-1ppb-05-hints.md`: D within 0.1% of 2.225 MeV
(i.e. 1,000,000 ppb). Current: 10.9× above target. **Target for 1 ppb
run:** residual < CODATA bound ≈ 1 ppb.

## Precision of inputs (NOT the source of the gap)

| input | value | precision | ppb contribution |
|-------|-------|-----------|------------------|
| $m_e$ (CODATA 2018) | 0.51099895000 MeV | ±1.5 × 10⁻¹⁰ | ≤ 1 ppb |
| Vol(6_2) (SnapPy HP) | 4.40083251612304610144… | 50-digit verified | effectively 0 |
| $B_{\text{AME}}(D)$ | 2.22456612 MeV | ± few × 10⁻⁷ MeV | ~100 ppb |
| q₀ (from VOL_FIG8 / μ_e) | 1.10997859555418… | CODATA-bounded, ~1.22 × 10⁻⁹ | ≤ 1 ppb |

**Conclusion: the 10.9 Mppb residual is NOT from input precision.**
The gap is in the **formula** `B = m_e · Vol(6_2)` itself being an
approximation at O(10⁻²).

## Candidate loci of the formula-level gap

### A. Knot assignment

6_2 was picked by `jsj_verification.py` census search as the knot
whose Vol is closest to $B_{\text{AME}}/m_e = 4.35328$. The nearest
catalog knots:

| knot | Vol | err vs target |
|------|-----:|--------------:|
| 6_2  | 4.40083 | +1.09% |
| 8_20 | 4.12490 | −5.25% |
| 7_3  | 4.59213 | +5.48% |
| 6²_2 | 4.05977 | −6.74% |

The nearest catalog knot is 6_2 at +1.09%. If deuterium's true
atom-knot is NOT in the ≤8-crossing census, the 1.09% could be
entirely knot-choice; if it IS 6_2, the 1.09% is a formula
correction. **Phase 3 open question** — cannot be decided without a
derivation of the atom-knot from the substrate.

### B. Locality-adjacent pentagon defect

Per `docs/path-to-1ppb-05-hints.md` (three-conjecture summary) and
`docs/path-to-1ppb-04-plan.md` Phase 2:

> **locality, adjacent**: O($\hbar_q^2$) ≈ 1% error from pentagon
> defects — the frontier

$\hbar_q^2 = 0.009817\ldots \approx 0.98\%$. D's residual is 1.09%.
In the right ballpark but not numerically identical.

### C. Density factor ρ ≠ m_e exactly

The hints doc is explicit: *"The density is NOT a free knob — it's
determined by the piece's topology via n_chir(P)."* For D, the hint
table states ρ = m_e (bond-type). A derivation of ρ from
$n_{\text{chir}}$ for D has not been written out. Any $O(10^{-2})$
correction to ρ would fully account for the residual without
invoking (B).

## Empirical observation (DOES NOT prove correction)

Computing the multiplicative gap factor directly:

$$
  R := \frac{B_{\text{AME}}}{B_{\text{pred}}}
     = \frac{2.22456612}{2.2488207948647\ldots}
     = 0.98921449\ldots
$$

$$
  1 - R = 0.01078551\ldots
$$

Compared to dimensionless $q_0$-combinations (mpmath 50-digit):

| expression | value | match to $1-R$? |
|-----------|------:|-----------------|
| $\hbar_q^2$ | 0.00981719 | off by 9% |
| $(q_0 - 1)^2$ | 0.01209535 | off by 12% |
| $H_A^2 / 2$ | 0.02185311 | off factor 2 |
| $q_0 \cdot \hbar_q^2 = (q_0-1)^2 / q_0$ | **0.01089687** | matches $1-R$ to **1.03% relative** |

And the implied correction $1/(1 + q_0 \hbar_q^2)$ applied to
$B_{\text{pred}}$ collapses the residual to **+6,167 ppb** (three
orders better).

**This is not a formal derivation.** It is a numerical coincidence
at the level of matching the first 3 significant figures. The
residual after the "correction" is still **6 ppm**, consistent with a
higher-order term that the simple factor does not capture.

Three reasons to withhold this as a "fix":

1. No derivation: neither `def:algebraic-quantum-volume-specialization`
   nor the 5-part handover writes $1/(1 + q_0 \hbar_q^2)$ as an
   explicit factor in the mass formula.
2. Works for D only: applied to T, ${}^3\mathrm{He}$, ${}^4\mathrm{He}$ it makes residuals
   **worse** (changes sign of the error or increases magnitude).
3. The conjectured pentagon-defect scale is $O(\hbar_q^2)$, not
   $O(q_0 \hbar_q^2)$. The factor-of-$q_0$ mismatch is unexplained.

## What would make this a 1-ppb result

Per `path-to-1ppb-05-hints.md § When claiming 1 ppb`:

- [ ] **Zero free parameters** — ρ and α derived, not fit.
  Currently: ρ_F = m_e is asserted from the "bond" rule but not
  derived from $n_{\text{chir}}(D\text{-piece})$.
- [x] **mpmath ≥ 20 digits** for arithmetic.
- [x] **SnapPy `.high_precision().volume()`** used.
- [ ] **Cross-check with ≥ 2 atoms** — D alone is insufficient.
- [ ] **Residual < CODATA bound** (~1.22 × 10⁻⁹). Current: 10.9 Mppb.
- [ ] **Published witness** with full precision.

The single residual that needs explaining is the 10.9 Mppb gap.
Whether it's (A) knot choice, (B) pentagon defect, or (C) density
correction — or more than one — is the concrete question for the
next session.

## Suggested next concrete probe

Compute $B(D)$ under the three mutually-exclusive hypotheses at
full precision and compare:

1. **Fix the knot, correct the formula.** Require 6_2 is correct;
   derive the correction factor from pentagon defect / Wedderburn
   subleading. If the derivation lands on $1/(1 + q_0\hbar_q^2)$ or
   similar, it validates the observation in §Empirical above.
2. **Fix the formula, search for the knot.** Require $B = m_e \cdot \operatorname{Vol}$;
   search beyond the 8-crossing census for a hyperbolic knot with
   Vol = 4.35328 (to 50 digits). If found, the issue is knot-assignment.
3. **Correct the density.** Derive ρ_F from $n_{\text{chir}}$ explicitly;
   see if it shifts m_e by ~1%.

The current session does not have the formal derivation tools to
pick among these. Writing this doc captures where the leverage is.

## Pointers

- Formula source: `content/quantum-observable-universe/braids-and-knots/algebraic-quantum-volume-specialization.md`
- Knot assignment: `computations/jsj_verification.py`
- Zero-parameter table: `computations/mass_table_ppb.py`
- Session hints: `docs/path-to-1ppb-05-hints.md`
- Pentagon defect plan: `docs/path-to-1ppb-04-plan.md` § Phase 2
