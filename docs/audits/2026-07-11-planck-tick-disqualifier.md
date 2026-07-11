# The Planck-tick disqualifier — the per-operation time is Compton, not Planck

**Date:** 2026-07-11
**Branch:** `claude/meridian-exceptional-divisor-znxqcn`
**Scope:** (a) scope-limited — records why identifying the QOU
computational tick with the Planck time is unsupported, so it is not
re-proposed. Not a structural exclusion of any ingredient.

## Question

Following "the meridian is at the exceptional divisor": one meridian
turn = one $R$-matrix application = one knot operation = a (hyperbolic)
rotation. Is that turn's *duration* the Planck time — i.e. is one
computation one Planck time?

## Finding

**No.** The natural per-operation tick is the electron Compton time,
$\sim 22$ orders of magnitude longer than the Planck time. This is not a
normalization bug in the definition of $t_P$; it is the standard
gravitational hierarchy.

| Quantity | Value | Source |
|---|---|---|
| Planck time $t_P = \sqrt{\hbar G/c^5}$ | $5.391\times10^{-44}$ s | CODATA |
| Electron Compton time $t_C = \hbar/(m_e c^2)$ | $1.288\times10^{-21}$ s | CODATA |
| $t_C/t_P = m_{\text{Planck}}/m_e$ | $2.389\times10^{22}$ (22.38 orders) | CODATA |
| $\alpha_G/\alpha_{EM}$ (grav. weakness, 2 electrons) | $2.4\times10^{-43}$ | CODATA |

Verified in `computations/` by the standard-constant check reproduced in
this branch's chat; all figures are textbook and owe nothing to QOU.

## Why it is not derivable in QOU

1. **A rotation is dimensionless.** The meridian holonomy is
   multiplication by $q$; one turn is a boost of rapidity $\ln q_0
   \approx 0.104$ (`QOU.Knot.CuspShapeBarParity.holonomy_hyperbola`,
   `barEven_mul`). Converting a rotation to a duration divides by an
   energy, $t = \hbar/E$.

2. **The substrate energy scale is $m_e$ (CAL-1).** So $t = \hbar/(m_e
   c^2) = t_C$. Nothing in the knot combinatorics supplies the
   $10^{22}$ factor to reach $t_P$ (Borromean has 6 crossings, not
   $10^{22}$; $\log_{q_0}(t_C/t_P) = 495$, not a clean knot number).

3. **Planck time needs $G$.** Pinning the tick at $m_{\text{Planck}}$
   introduces Newton's constant, an input outside the three-calibration
   weak sector $(m_e, \mathfrak{D}_\beta, \mathfrak{D}_\pi)$. That is a
   **fourth calibration** and a **substrate-scale derivation
   (Subgoal-2)**, which the coordination ledger declined (2026-05-08)
   and which this note does not reopen.

## Scope discipline

This is a **(a) scope-limited negative** per AGENTS.md "Before declaring
'refuted' / 'ruled out'": the Planck-tick identification, *as a
free-standing scaling assumption*, is unsupported and would smuggle a
CAL-4 (gravity). It is **not** a structural exclusion — the framework is
simply *silent* on the 22-order gap to gravity by construction (it is
calibrated on the weak sector), and this silence is consistent, not a
defect. If a future categorical origin for $G$ is derived (owner
reversal required for Subgoal-2), the question reopens.

## Formalization

- `content/quantum-observable-universe/lean/QOU/Knot/CuspShapeBarParity.lean`
  — the cusp bar-parity split ($\mathrm{barEven}(\omega)=1$,
  $\mathrm{barOdd}(\omega)^2=-3$) and the boost/rapidity structure
  (`holonomy_hyperbola`, `barEven_mul`, `barOdd_mul`), sorry-free,
  generic `[Field R]`.
- Content blocks: `prop:cusp-shape-bar-parity`,
  `prop:meridian-holonomy-boost`, `rem:meridian-exceptional-divisor-note`
  (braids-and-knots chapter).
