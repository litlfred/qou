The three-calibration discipline
([`prop:three-calibration-discipline`](#prop:three-calibration-discipline))
names $m_e$, $m_\mu/m_e$, $m_\pi$ as the framework's external CODATA/PDG
inputs and maps them bijectively to three cohomological data of the
Bring Hodge structure $H^1 = 2W$ ($W$-plane scale, $W$-plane modulus,
and the orthogonal $\mathrm{Vol}(\mathrm{Hopf})=0$ meson class). This
remark unpacks the *epistemic status* of each input — distinguishing
what is genuinely calibrated from what is structurally derived from
canonical cohomology but recorded *as if* calibrated. ($Q_\beta$ is
**derived** from CAL-1 + CAL-2, not a calibration; the §"CAL-3"
section below treats it as the *derived* hadronic observable, the
bar-odd $\sinh$ partner of the meson scale $m_\pi$.)

The remark **does not** propose a 4th calibration input, a fit, or
a numerological substitution. The forbidden clauses of
[`prop:three-calibration-inputs`](#prop:three-calibration-inputs)
§"What is forbidden" remain in force. It clarifies the *status* of
the three existing CALs without changing how many CALs the framework
admits.

## CAL-1 ($m_e$) — unit choice + cohomological period

CAL-1 plays two distinct roles:

| Role | Type | Status |
|---|---|---|
| Unit of mass (MeV $\leftrightarrow$ natural units) | dimensional convention | **unit choice** (could be GeV, eV; physically arbitrary) |
| Numerical value in natural units $m_e(\text{natural}) = \mathrm{Li}_2(q^{-2}) / \hbar_q^2 \approx 112$ | dimensionless | **cohomologically derived** from $q_0$ (motivic dilog period) |

Per [`rem:calibration-inputs`](#rem:calibration-inputs) §"second
input": *"its brane tower is fully computable from $q_0$ alone."*
The dimensional input the framework genuinely needs is the
conversion factor $m_e(\text{MeV})/m_e(\text{natural}) \approx 4.57
\times 10^{-3}$ MeV per natural unit — a unit choice, not a
fundamental constant.

## CAL-2 ($m_\mu/m_e$) — substrate $q_0$ pin (self-referential)

CAL-2 fixes $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$.
Per the audit
[`-cal-2-cohomological-vs-calibration-critique`](../../../docs/audits/-cal-2-cohomological-vs-calibration-critique.md):

- $\mathrm{Vol}(4_1) = 2\Lambda(\pi/3) \approx 2.0299$ is **pure
  cohomology** (Bloch-Wigner motivic period at the primitive 6th
  root of unity). No CODATA input.
- $\hbar_q = (q-1)/q$ is **pure algebra** in $q$. No CODATA input.
- $q_0 \approx 1.10998$ itself is the **un-derived gap**. Currently
  pinned by inverting $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
  against CODATA $m_\mu/m_e = 206.7682830$.

The framework's existing line *"Muon mass: $m_\mu = m_e \times
\mathrm{Vol}(4_1)/\hbar_q^2$ (first prediction, by construction
matches calibration input)"*
([`rem:calibration-inputs`](#rem:calibration-inputs)) is
**structurally tautological**: $q_0$ was defined to make this
equation hold, so it holds. The Lean cross-check
`figure-8-muon-mass-cross-check.lean:42` says explicitly *"equality
by construction."*

The substrate-$q_0$ derivation was declined as out-of-scope on
 (coordination ledger) and **re-opened on** in
response to the same owner question that produced this remark. The
research-grade workplan tracks candidate derivation paths
(spectral collapse, K-theoretic period, Bring $\chi = -6$
fixed-point, categorical endomorphism fixed-point).

## CAL-3 ($m_\pi$) and the derived $Q_\beta$ — conditional net-ansatz

**CAL-3 is $m_\pi$** (the charged-pion mass — the orthogonal
$\mathrm{Vol}(\mathrm{Hopf})=0$ meson scale, genuinely independent of
$(m_e, q_0)$). $Q_\beta$ below is the **derived** hadronic observable
(bar-odd $\sinh$ partner of $m_\pi$), **not** the third calibration;
its derivation status is what this section assesses.

The derived $Q_\beta$ fixes the hadronic energy scale $\mathfrak{E}_0$ via
$Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$. Per sibling
 and audit
[`-q-beta-net-ansatz-fitting-finding`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md):

- The relation $Q_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$
  is **postulated**, not derived from the canonical per-braid mass
  formula.
- The +0.17% match between framework-derived
  $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1))$ and CODATA-calibrated
  $\mathfrak{E}_0^{(\text{cal})} = Q_\beta / |\Delta(\mathrm{net})|$
  could be either a genuine $N=0$ truncation residual or a
  substrate-specific artefact — the framework currently has no
  discriminator.
- Higher-order corrections are being recast cohomologically as
  traces over **Khovanov-Rozansky strata** of the link projection
  (audit
  [`-qbeta-n5-cohomological-breakdown`](../../../docs/audits/-qbeta-n5-cohomological-breakdown.md)),
  with the $N=3$ rung $= J_{\mathrm{Hopf}}(q=1) = -2$ already
  beating the L2 100$\times$ target by ~24%.

## Summary table

| CAL | Pinned quantity | Cohomological derivation candidate | Status |
|---|---|---|---|
| CAL-1 | $m_e$ in MeV | $\mathrm{Li}_2(q^{-2}) / \hbar_q^2$ for the natural-units value | **unit-choice + derived**; the unit choice itself is real |
| CAL-2 | $q_0$ via $m_\mu/m_e$ (phys-obs: $m_p/m_e$) | $\mathrm{Vol}(4_1) = 2\Lambda(\pi/3)$ on the cohomology side; $q_0$ un-derived | **open** (re-opened, weeks-of-research workplan) |
| CAL-3 | $m_\pi$ (meson scale; orthogonal class) | independent of $(m_e,q_0)$ via $\mathrm{Vol}(\mathrm{Hopf})=0$ | **genuine independent input** |
| *(derived)* | $\mathfrak{E}_0$ via $Q_\beta$ | Khovanov-Rozansky cohomology strata of the link projection | **open** (derivation status of $Q_\beta$, not a CAL) |

## What this remark does NOT do

- Does **not** propose a 4th calibration input.
- Does **not** propose to replace CAL-1, CAL-2, or CAL-3 with empirical fits.
- Does **not** claim $q_0$ has been cohomologically derived.
- Does **not** override the no-fourth-CAL audit discipline.
- Does **not** introduce new fitting, ansätze, or numerological inputs.

It is a structural clarification: the framework's *cohomological*
status is more advanced than the *calibration* status, and the gap
between them is a recognised open research direction.

## Why this matters

The 3-CAL discipline is rhetorically powerful: it claims the
Standard Model's 19 free parameters reduce to 3. The accounting
above clarifies that **the framework's aim is to reduce 3 to as
close to 0 as the structural completeness allows**, ideally
leaving only a single dimensional unit choice (the CAL-1 conversion
factor) plus cohomologically-derived $q_0$ and cohomologically-
derived hadronic-sector residual. This is the *direction*, not a
redefinition of the discipline.

## See also

- [`rem:calibration-inputs`](#rem:calibration-inputs) — canonical 3-CAL remark with formulas
- [`prop:three-calibration-inputs`](#prop:three-calibration-inputs) — proposition form with Wedderburn alignment
- [`prop:three-calibration-discipline`](#prop:three-calibration-discipline) — the proposition this remark interprets
- [`prop:three-parameters-wedderburn`](#prop:three-parameters-wedderburn) — categorical 3-parameter count
- Audit
  [`-cal-2-cohomological-vs-calibration-critique`](../../../docs/audits/-cal-2-cohomological-vs-calibration-critique.md)
- Audit
  [`-q-beta-net-ansatz-fitting-finding`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md) (sibling)
- Audit
  [`-qbeta-n5-cohomological-breakdown`](../../../docs/audits/-qbeta-n5-cohomological-breakdown.md)
