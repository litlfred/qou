# Post-refactor verification + pre-archimedean Bloch group note (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/post-refactor-verification-2026-06-01)
**Status:** Verification + structural addition.
**Triggered by:** user 2026-06-01 "1 y 2 y 3 y 4 y" — items 2 + 3.

## TL;DR

**Item 2 (production refactor verification):** at single-nucleon V̂
(both proton and neutron, both positive), the signed-`v` vs `|v|`
refactor in `Phi_q` is **no-op (0% difference)**. At negative V̂
(e.g., Δtr_M = −0.142), the difference is 92.5% per term as
PR #1641 predicted. **Production m_p / m_n / m_atom calculations
are unaffected at the canonical single-nucleon level.**

**Item 3 (pre-archimedean Bloch group):** added a section to
`quantum-bloch-group.md` making the pre-archimedean Habiro Bloch
group $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$ explicit alongside the
archimedean $\mathcal{B}(\mathbb{C})$.

## Item 2 — production refactor verification

Numerical check at q_proton (q = 1.10998):

| Input V̂ | sign | `Phi_q(v)` | `Phi_q(|v|)` | diff |
|---|---|---|---|---|
| +1.07 (proton sub-braid trace) | positive | 9.95×10⁶ | 9.95×10⁶ | **0.0000%** |
| +0.92 (neutron sub-braid trace) | positive | 1.33×10⁵ | 1.33×10⁵ | **0.0000%** |
| −0.142 (Δtr_M, binding-context) | negative | 0.2865 | 3.8092 | **−92.48%** |

**Conclusion:** the PR #1643 production refactor (`Phi_q(abs(v))` →
`Phi_q(v)` in 13 scripts) does NOT change `m_p`, `m_n`, or `m_atom`
calculations at the single-nucleon level. Sub-braid V̂ values for
the canonical proton/neutron braids are all positive at q_0.

Where the refactor MATTERS:
- Δtr_M (binding context) — but Q_β / binding uses `Li_2^q`, not `Phi_q`
- Deeper-level jet pairs `V̂_i · V̂_j` where the product CAN be negative
  if a sign flip occurs (typically rare at q_proton with the canonical
  T_w choices, per Wenzl positivity for SDP-selected T_w)

**No production witness regen catastrophe.** The refactor is a
discipline alignment (categorical signed v matches paper); the
numerical impact at production scope is negligible.

## Item 3 — Pre-archimedean Bloch group addition

The framework already discusses:
- Classical Bloch group $\mathcal{B}(\mathbb{C})$ (`borromean-bloch-group-element.md`) — Beilinson regulator `r_2: K_3(ℂ) → ℝ`, archimedean
- Quantum Bloch group $\mathfrak{B}(q)(R)$ (`quantum-bloch-group.md`) — pentagon identity of $\Phi_q$

But the explicit **Habiro Bloch group $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$**
— the genuine pre-archimedean side — wasn't stated. The user's
discussion in this session highlighted that the pre-archimedean
structure exists and matters.

### Added to `quantum-bloch-group.md`

A new section "Pre-archimedean side: $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$"
making the parallel explicit:

| Side | Bloch group | Regulator $\Phi_1$ |
|------|-------------|---------------------|
| Pre-archimedean | $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$ | $\tfrac{1}{2}\sum \ln(\hat{V}_i \cdot \overline{\hat{V}_i})$ |
| Archimedean ($\tau_{\mathrm{arch}}$ at real $q_0$) | $\mathcal{B}(\mathbb{C})$ | $\sum \ln\lvert\hat{V}_i\rvert$ |

The bar-involution form (PR #1643 refactor) is the pre-archimedean
$r_1$ Borel regulator; the standard `ln|V̂|` is its archimedean
specialization.

This refines `conj:borromean-bloch-group-element`: the framework's
**working object** is $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$; the
Beilinson regulator $r_2$ is the **archimedean realization** of the
graded $\rho_K$.

## Items 1 and 4 (executed elsewhere this session)

- **Item 1 — merge #1641**: DONE. Sister diagnostic PR merged
  (sha 6827b6f6a) after rebase resolving witness drift.
- **Item 4 — sibling PR triage**:
  - #1642 (ζ_8 Wenzl → Q_β Habiro) — **merged as NEGATIVE finding**
    ("multi-track findings: Wenzl→Q_β NEGATIVE + ⁷Li/⁷Be mirror").
    The ζ_8 Habiro route is REFUTED; my work on bar-involution
    discipline (PR #1643) is orthogonal and remains useful.
  - #1636, #1622, #1640 — not yet merged. Out of immediate scope.

## Cross-refs

- PR #1641 (merged 6827b6f6a) — Φ_q signed-vs-|...| 92% sensitivity
- PR #1643 (merged e59cd800b) — paper `|...|` audit + refactor +
  KLR/Wenzl positivity audit
- PR #1642 (merged 4a0bdad71) — Wenzl → Q_β NEGATIVE finding
- `prop:rho-k-graded-expansion`, `conj:borromean-bloch-group-element`,
  `quantum-bloch-group.md` (this PR adds pre-archimedean section)
- `conj:wenzl-positivity-implies-substrate-positivity`
- AGENTS.md §7c — base ring discipline (analogous)
