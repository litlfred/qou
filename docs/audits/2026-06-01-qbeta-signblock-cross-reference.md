# Q_β c_3 = −2 vs m_p sign-block template — cross-reference

**Date:** 2026-06-01
**Type:** Light-coordination note (Item 5 of PR #1671)

This audit cross-references the m_p sign-block / Plancherel finding
(PRs #1581 → #1654) with the heavy sibling Q_β Habiro activity
(recent ⁶He−⁶Be mirror, ¹⁰C extension, Φ_8 multiplicity scaling
A−1 in mirror-pair Habiro, Wenzl tower FALSIFIED, mass-table sweep
of 12 atoms).

## Sign-block / Plancherel finding (m_p side)

`(α_em/π) · P_(1,1,1)(H_3) = (α_em/π)/6` closes the proton-mass identity
to 54 ppb (76% of CODATA propagated floor). Hypothesis: EM correction
lives at the 1-dim sign-rep Wedderburn block of H_3 (Fermi-statistics
color antisymmetry).

## Q_β c_3 = −2 (sibling Habiro work)

`c_3 = J_Hopf(q=1) = −(q² + q⁻²)|_{q=1} = −2` is the Hopf-link Jones
evaluation at q=1.

## Algebraic relation found in PR #1654 Item 3

PR #1654 `qbeta_signblock_template_check.py`:
  c_3 = −2 reproduces EXACTLY as:
    - `2 · σ_1(sign)|_{q=1} = 2 · (−1)` (sign-channel × dim H_2)
    - `−(q² + q⁻²)|_{q=1}` (the Jones-Hopf evaluation)

But NOT as a clean Plancherel-weighted sum:
  - `Σ_λ P_λ · σ_1(λ)|_{q=1} = 0` (cancels)
  - `Σ_λ P_λ · σ_1²(λ)|_{q=1} = 1` (NOT −2)

## Interpretation

Both m_p `(α_em/π)/6` and Q_β `c_3 = −2` involve **sign-rep contributions**,
but with **different normalizations**:

| Observable | Form | Normalization |
|---|---|---|
| m_p EM correction | `(α_em/π) · P_(sign)(H_3)` | `P_λ = d²_λ/|S_3|` (Plancherel weight squared) |
| Q_β c_3 | `dim H_2 · σ_1(sign)\|_{q=1}` | `dim H_n` (linear dim) |

This suggests **two different categorical mechanisms**:
- m_p: Plancherel-weighted EM coupling at sign block
- Q_β: dim-scaled Hopf-link Jones at sign channel

The sibling Q_β Habiro work (Φ_8 multiplicity scaling A−1, Wenzl
positivity, mass-table sweep) is pursuing the **Habiro-element
identification** for the per-rung Q_β coefficients — independent
categorical framework from the m_p sign-block hypothesis.

## Cross-coordination note

The two campaigns are **complementary, not competing**:
- m_p sign-block: closed at CODATA floor; opens substrate Fermi
  statistics + Wedderburn EM projection (multi-session)
- Q_β Habiro: closure pending; sibling 12-atom mass-table sweep
  + mirror-pair Φ_8 multiplicity scaling are the production attack

Future agents pursuing Q_β closure should NOT re-derive the m_p
sign-block pattern (PRs #1581-#1654 catalogue all PSLQ NULL +
27 alt-geometries + exotic-basis NULL — see consolidated reference
`docs/audits/2026-06-01-sign-block-plancherel-campaign-canonical-reference.md`).

## Cross-references

- consolidated reference (this PR #1671):
  `docs/audits/2026-06-01-sign-block-plancherel-campaign-canonical-reference.md`
- m_p sign-block hypothesis: merged PR #1645
- Q_β c_3 template check: merged PR #1654 Item 3
- Q_β Habiro sibling sweep: recent main commits (mass-table extractor,
  ¹⁰C, ⁶He−⁶Be, Wenzl tower FALSIFIED)
