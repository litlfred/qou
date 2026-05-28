The three-calibration discipline
([`prop:three-calibration-discipline`](#prop:three-calibration-discipline))
names three independent physical measurements as the framework's
external inputs: $m_\mathfrak{e}$ (electron mass), $\mathfrak{D}_\beta$
(neutron $\beta$-decay width), and $\mathfrak{D}_\pi$ (pion decay
width).  These correspond to jet orders $h^0$, $h^2$, $h^3$ of the
$h$-expansion and to distinct cohomological degrees.  This remark
unpacks the *epistemic status* of each — distinguishing what is
genuinely calibrated from what is structurally derived.

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

## CAL-2 ($\mathfrak{D}_\beta$) — substrate $q_0$ pin

CAL-2 is the neutron $\beta$-decay width
$\mathfrak{D}_\beta = \hbar / \tau_n$, which determines
$Q_\beta = m_n - m_p - m_\mathfrak{e}$ and thereby fixes $q_0$
via the substrate identity.  Equivalently,
$m_\mu/m_\mathfrak{e} = \mathrm{Vol}(4_1)/\hbar_q^2$.
Per the audit
[`2026-05-25-cal-2-cohomological-vs-calibration-critique`](../../../docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md):

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
2026-05-08 (coordination ledger) and **re-opened on 2026-05-25** in
response to the same owner question that produced this remark. The
research-grade workplan tracks candidate derivation paths
(spectral collapse, K-theoretic period, Bring $\chi = -6$
fixed-point, categorical endomorphism fixed-point).

## CAL-3 ($\mathfrak{D}_\pi$) — meson mass scale

CAL-3 is the pion decay width
$\mathfrak{D}_\pi = \hbar / \tau_\pi$, which determines the
pion mass $m_\pi$ and thereby the meson mass scale.  This is
genuinely independent of $(m_\mathfrak{e}, q_0)$: the Hopf link
complement has $\mathrm{Vol} = 0$ (no hyperbolic invariant to
set the meson scale from the substrate).  See
[`prop:meson-scale-independence`](../../particle-interactions/meson-scale-independence.md). Per sibling
the prior work and audit
[`2026-05-24-q-beta-net-ansatz-fitting-finding`](../../../docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md):

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
  [`2026-05-18-qbeta-n5-cohomological-breakdown`](../../../docs/audits/2026-05-18-qbeta-n5-cohomological-breakdown.md)),
  with the $N=3$ rung $= J_{\mathrm{Hopf}}(q=1) = -2$ already
  beating the L2 100$\times$ target by ~24%.

## Summary table

| CAL | Observable | Measurement | Jet order | Status |
|---|---|---|---|---|
| CAL-1 | $m_\mathfrak{e}$ | electron mass (Penning trap) | $h^0$ | **unit-choice + derived** |
| CAL-2 | $\mathfrak{D}_\beta$ | neutron $\beta$-decay width ($\tau_n$) | $h^2$ | **open** (re-opened 2026-05-25) |
| CAL-3 | $\mathfrak{D}_\pi$ | pion decay width ($\tau_\pi$) | $h^3$ | **independent** (SDP-validated) |

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
  [`2026-05-25-cal-2-cohomological-vs-calibration-critique`](../../../docs/audits/2026-05-25-cal-2-cohomological-vs-calibration-critique.md)
- Audit
  [`2026-05-24-q-beta-net-ansatz-fitting-finding`](../../../docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md) (sibling)
- Audit
  [`2026-05-18-qbeta-n5-cohomological-breakdown`](../../../docs/audits/2026-05-18-qbeta-n5-cohomological-breakdown.md)
