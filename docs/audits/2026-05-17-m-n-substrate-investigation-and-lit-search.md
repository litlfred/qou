# m_n substrate derivation investigation + PL integration-limit lit search

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**Owner asks**:
- "fix m_n difference formula... can we use m_p like approach?"
- "we need to derive the thimble... where are they determined in the lit in other problems? anything like ours?"
- "work on m_n"
- "also lit search"

## Part 1 — Literature search on PL integration-limit derivation

### Standard PL integration practice

Reviewed sources (Cristoforetti, Feldbrugge–Turok, Witten, Bachelor thesis
Zorbach, Acquiring-the-Lefschetz-thimbles MNRAS 2024):

**Standard PL does NOT use finite real-axis cutoffs.** The textbook
procedure is:

1. Identify saddle points of the action S(z) in ℂ.
2. For each saddle, compute the steepest-descent thimble — extending
   to infinity along the direction of decreasing Re(S).
3. Decompose the original integration contour as a sum
   `γ = Σ n_σ · 𝒥_σ` where `n_σ` are intersection numbers of the
   anti-thimbles 𝒦_σ with γ.
4. Integrate ALONG each thimble TO INFINITY (the integrand is
   guaranteed to decay along the thimble direction).
5. Sum the contributions weighted by intersection numbers.

> "Integration along these thimbles is computationally efficient and
> insensitive to numerical cutoffs"  
> — [MNRAS 2024 on wave-optics lensing Lefschetz thimbles](https://academic.oup.com/mnras/article/534/2/1143/7756437)

### What QOU's `picard_lefschetz_thimble.py` actually does

The script integrates `∫_{-a}^{+a}` along the **real axis** (not along
a thimble), then picks `a` as the value that minimises `|m_p_pred −
M_P_MEV|` from a list of 6 candidates.

**This is a non-standard heuristic**, not the textbook PL procedure.
Per the lit:

- Standard PL would integrate along the thimble 𝒥_σ from z_c to
  infinity (no finite cutoff).
- The "limit" in standard PL is `t → ∞` along the steepest-descent
  parameter, not a real-axis interval bound.

### What the lit DOES say about finite-interval crossings

The closest analog in the literature: when reducing a real-line
integral to a sum-over-thimbles, the **intersection numbers**
`n_σ = ⟨𝒦_σ, γ⟩` (anti-thimble crossings with γ) determine WHICH
thimbles contribute, NOT a finite interval bound.

> "Flow lines help define the optimal generalized integration contour
> for an interval on the original integration axis, with the location
> of the interval determined by where the real axis crosses the
> steepest **ascending** contour"  
> — [Picard-Lefschetz overview](https://p-lpi.github.io/)

So the **anti-thimble** (steepest-ASCENT) real-axis crossing
determines the natural interval. I tested this on the QOU color-tube
cubic in [`derive_a_thimble_intersection.py`](../../computations/derive_a_thimble_intersection.py):

| direction | from z_c | real-axis crossing |
|---|---|---|
| Descent (J⁺, J⁻) | 0.106 ± 0.937i | **z = 3.86** (over-predicts m_p by 100%) |
| Ascent (K⁺, K⁻) | 0.106 ± 0.937i | **does not cross within \|z\|≤4** |

So:
- The descent thimble crosses at 3.86 → over-predicts.
- The ascent anti-thimble (which the lit says SHOULD determine the
  interval) doesn't cross the real axis for this cubic — likely
  heads to infinity along a Stokes ray.

**Conclusion**: there is NO categorical derivation of the empirical
`a = (4-q)/(4q+3) = 0.388` from standard PL thimble geometry. The
"agreement" at 6 ppm is a back-solved fit, not a substrate prediction
per literature standards.

### Comparable problems in the lit

| Problem | Integration prescription |
|---|---|
| **Feynman path integral** (Cristoforetti et al.) | Integrate along thimble to infinity; uses asymptotic decay |
| **Diffraction integrals in wave-optics lensing** (MNRAS 2024) | Multi-thimble decomposition; integrate each to infinity |
| **Chern-Simons analytic continuation** (Witten 2010) | Half-thimbles, no finite cutoff |
| **Resurgent analysis** (Costin, Écalle) | Borel transform + median resummation along thimbles |
| **QOU's `picard_lefschetz_thimble.py`** | **Finite real-axis interval `[-a, a]`, `a` post-hoc fit** ← NON-STANDARD |

The QOU script's prescription is **idiosyncratic** — no direct analog
in the published PL literature. To bring it into alignment with
standard PL, the integration would need to be **along the thimble
from z_c to infinity**, not on the real axis with a finite cutoff.

## Part 2 — m_n substrate derivation investigation

### Current m_n status

The only "substrate-derived" m_n in compute infra is
[`m_n_difference_formula.py`](../../computations/m_n_difference_formula.py), which:

```
Δm = ((q+q⁻¹)/(q^{1/2}+q^{-1/2})) · (μ_d − μ_u)
m_n = m_p + Δm
```

with `(μ_d − μ_u)` **fit to CODATA Δm = 1.293 MeV**. The script's
own description: *"Both paths are 1-parameter calibrations"*. So m_n
is NOT substrate-derived; it's a 1-parameter fit anchored to CODATA
mass difference.

### Why the Picard-Lefschetz analog doesn't directly work for m_n

The color-tube cubic `F(z, c) = c³ + (4z+1)c² + (6z²+3z+1)c +
(4z³+3z²+2z+1)` encodes the **BARYON's 3-color structure**
(3 color sheets via the cubic's roots). It does NOT encode the
**quark-flavor content** (uud vs udd).

So:
- Proton (uud) and neutron (udd) share the SAME color-tube cubic
- The 9 simultaneous-3-root prescriptions tested in
  `picard_lefschetz_thimble.py` are all baryon-agnostic
- None of them naturally give a m_n ≠ m_p (at the cubic level)

To distinguish proton from neutron, the framework needs an
**additional categorical input** beyond the color-tube cubic:

1. **Quark-flavor structure**: a separate cubic / variety for
   u vs d flavors, encoding the chirality difference.
2. **Markov-trace structure**: |tr_M(β_p)| vs |tr_M(β_n)|
   differ (1.0653 vs 0.9232 per `atomic-mass-gb-nf.md` line 60).
   This DOES distinguish p from n.
3. **The Δm formula** in `m_n_difference_formula.py`: uses
   (μ_d − μ_u) as a categorical scalar. If `(μ_d − μ_u)` can be
   derived from substrate (rather than fit), m_n becomes a real
   prediction.

### Tested prescriptions in picard_lefschetz_thimble.py — none give m_n

The script's 9 simultaneous-3-root prescriptions all integrate
**baryon-symmetric** combinations of (c_1, c_2, c_3) and (dc_k/dz).
None of them encode a flavor preference. Numerically (at the z₀
integration limit):

| prescription | ratio | m_pred |
|---|---:|---:|
| ∏ dc_k/dz | 2.401 | 930.43 (proton) |
| Σ dc_k/dz | 3.898 | far from m_n |
| Σ(c_k+z) | 1.091 | far |
| ∏(c_k+z) | 23.55 | far |
| ... | ... | ... |

Required ratio for m_n: `2.401 × (939.565/938.272) = 2.404`. Only
∏ dc_k/dz gives anything near this — but the relevant variation
(0.1%) is below the prescription-choice spread (which is orders
of magnitude).

### Substrate-derivation paths for m_n (none implemented; research)

1. **Categorical (μ_d − μ_u) from V_(2,1) Hoefsmit**.
   The d_1, d_2 entries of the Hoefsmit V_(2,1) matrix differ
   in sign and magnitude:
   - d_1 = q³/(q²+1) ≈ 0.613 at q_0
   - d_2 = −q⁻¹/(q²+1) ≈ −0.404 at q_0
   These encode chirality. A natural identification might be:
   - μ_u → d_1 contribution (positive eigenvalue, "right-handed")
   - μ_d → d_2 contribution (negative eigenvalue, "left-handed")
   But the magnitudes don't directly give Δm ≈ 1.293 MeV; would
   need a calibration prefactor. **Research item.**

2. **Δm via Markov-trace ratio**:
   m_n / m_p (CODATA) = 1.001378. Could this ratio be derived from
   substrate as |tr_M(β_n)|·something / |tr_M(β_p)|·something?
   Per atomic-mass-gb-nf.md, |tr_M(p)|=1.0653 and |tr_M(n)|=0.9232,
   giving ratio 1.154 — too far from 1.001 to be the answer directly.

3. **Picard-Lefschetz with flavor-extended cubic**:
   Replace the 3-color cubic with a 6-flavor-color cubic (3 colors
   × 2 flavors). The roots would encode both quark species. Research.

4. **Use the existing m_p PL chain + Wenzl 1988 multiplicativity**:
   If m_p is derived from `Vol(𝔅₃)/ℏ_q² · A_p · m_e`, and m_n
   could be derived from `Vol(𝔅₃)/ℏ_q² · A_n · m_e` with A_n
   computed from a NEUTRON-specific simulator-of-prescriptions
   (different choice of dc_k/dz combination based on udd content),
   m_n would be substrate-derived. **Research item.**

### Honest m_n status

| chain | m_n_pred (MeV) | residual | substrate-only? |
|---|---:|---:|---|
| `m_n_difference_formula.py` | 939.5654 | <1 ppb (by fit) | **NO** — 1-parameter fit to CODATA Δm |
| Picard-Lefschetz analog | — | — | **NOT IMPLEMENTED** (cubic doesn't distinguish u/d) |
| brane-tower (this PR) | 8.10 cat = 4.14 MeV | 99.6 % | NO closure |

**Conclusion**: substrate m_n is NOT done. The only "1 ppb m_n" in
compute is a calibration. To get real substrate m_n requires
research-level work on (μ_d − μ_u) categorical derivation OR
extension of the Picard-Lefschetz prescription to flavor-distinguishing.

## Cross-link to previous audits

- [`docs/audits/2026-05-17-substrate-m-p-m-n-compute-audit.md`](2026-05-17-substrate-m-p-m-n-compute-audit.md)
  — initial finding that m_p_pred = 938.267 MeV via PL is back-fit
- [`docs/audits/2026-05-17-rho-vs-rho-K-paper-discrepancy.md`](2026-05-17-rho-vs-rho-K-paper-discrepancy.md)
  — ρ_K open problem requires substrate m_p AND m_n

## Recommendation

For PR #663 (this branch):

1. **Stop calling Picard-Lefschetz m_p "substrate-derived"** — it
   is "substrate + best-fit integration limit". Honest framing:
   substrate-only PL m_p closes at **0.84 %** (using z_0 or ℏ_q
   as categorical limits) — still 1180× better than brane-tower's
   99.4 % but not 6 ppm.

2. **m_n stays calibration-pending**. The 1-parameter fit in
   `m_n_difference_formula.py` is the only finite-residual m_n
   value; it should be tagged `m_n_via_1param_fit` not
   `m_n_substrate_derived`.

3. **Research items queued**:
   - (μ_d − μ_u) categorical derivation from Hoefsmit V_(2,1)
   - Picard-Lefschetz prescription extension to flavor
   - Standard-PL refactor of `picard_lefschetz_thimble.py`
     (integrate ALONG thimbles to infinity, not finite real-axis)
   - Bring QOU's PL prescription into alignment with the
     published literature (Feldbrugge–Turok, Cristoforetti, etc.)

## Sources

- [Picard-Lefschetz Path Integrals overview](https://p-lpi.github.io/)
- [Applied Picard–Lefschetz Theory (AMS Surveys 97)](https://www.ams.org/books/surv/097/surv097-endmatter.pdf)
- [Toward Picard-Lefschetz Theory of Path Integrals, Complex Saddles and Resurgence (arXiv 1510.03435)](https://arxiv.org/abs/1510.03435)
- [Acquiring the Lefschetz thimbles: efficient evaluation of the diffraction integral for lensing in wave optics (MNRAS 2024)](https://academic.oup.com/mnras/article/534/2/1143/7756437)
- [Picard–Lefschetz integrator (Feldbrugge–Turok)](https://jfeldbrugge.github.io/Picard_Lefschetz_Integrator/)
- [Hamilton dynamics for the Lefschetz thimble integration (arXiv 1507.07351)](https://ar5iv.labs.arxiv.org/html/1507.07351)
- [A Picard-Lefschetz Approach to the Path Integral (Colorado College seminar)](https://www.coloradocollege.edu/academics/dept/physics/_documents/seminar/posters_19_20/Kate.pdf)
- [Stable Evaluation of Lefschetz Thimble Intersection Numbers (2025)](https://www.researchgate.net/publication/396330615_Stable_Evaluation_of_Lefschetz_Thimble_Intersection_Numbers_Towards_Real-Time_Path_Integrals)
