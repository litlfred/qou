The three-calibration discipline ([`prop:three-calibration-discipline`](#prop:three-calibration-discipline)) designates $m_e$, $m_\mu/m_e$, and $m_\pi$ as the framework's external CODATA/PDG inputs. It maps them bijectively to three cohomological data of the Bring Hodge structure $H^1 = 2W$: the $W$-plane scale, the $W$-plane modulus, and the orthogonal $\mathrm{Vol}(\mathrm{Hopf})=0$ meson class. We unpack the epistemic status of each input. We distinguish what is genuinely calibrated from what is structurally derived from canonical cohomology but recorded as if calibrated. 

The parameter $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$ is the proxy for CAL-2 (the neutron $\beta$-decay width $\mathfrak{D}_\beta$), per the 2026-06-26 decay-width ruling. It is not a fourth calibration. It is not derived as opposed to calibrated. The CAL-2 modulus is overdetermined and pinned most precisely by $m_\mu/m_e$. Reproducing $\mathfrak{Q}_\beta$ from $q_0$ serves as a $0.17\%$ cross-check. The "CAL-3" section below treats it accordingly—as the bar-odd $\sinh$ partner of the meson scale $m_\pi$. CAL-3 proper is the pion decay width $\mathfrak{D}_\pi$ (proxy $m_\pi$).

We do not propose a fourth calibration input, a fit, or a numerological substitution. The forbidden clauses of [`prop:three-calibration-inputs`](#prop:three-calibration-inputs) remain in force. We clarify the status of the three existing CALs without altering the framework's calibration count.

## CAL-1 ($m_e$) — unit choice + cohomological period

CAL-1 plays two distinct roles:

| Role | Type | Status |
|---|---|---|
| Unit of mass (MeV $\leftrightarrow$ natural units) | dimensional convention | **unit choice** (physically arbitrary) |
| Numerical value in natural units $m_e(\text{natural}) = \mathrm{Li}_2(q^{-2}) / \hbar_q^2 \approx 112$ | dimensionless | **cohomologically derived** from $q_0$ (motivic dilog period) |

Per [`rem:calibration-inputs`](#rem:calibration-inputs), "its brane tower is fully computable from $q_0$ alone." The dimensional input the framework requires is the conversion factor $m_e(\text{MeV})/m_e(\text{natural}) \approx 4.57 \times 10^{-3}$ MeV per natural unit. This is a unit choice, not a fundamental constant.

## CAL-2 ($m_\mu/m_e$) — substrate $q_0$ pin

CAL-2 fixes $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$. Per the audit [`-cal-2-cohomological-vs-calibration-critique`](../../../docs/audits/-cal-2-cohomological-vs-calibration-critique.md):

- $\mathrm{Vol}(4_1) = 2\Lambda(\pi/3) \approx 2.0299$ is pure cohomology (Bloch-Wigner motivic period at the primitive 6th root of unity). It uses no CODATA input.
- $\hbar_q = (q-1)/q$ is pure algebra in $q$. It uses no CODATA input.
- $q_0 \approx 1.10998$ itself is the un-derived gap. It is pinned by inverting $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ against the CODATA value $m_\mu/m_e = 206.7682830$.

The framework's claim that $m_\mu = m_e \times \mathrm{Vol}(4_1)/\hbar_q^2$ is structurally tautological. We defined $q_0$ to make this equation hold. The Lean cross-check `figure-8-muon-mass-cross-check.lean:42` states explicitly: "equality by construction."

The muon is the structurally preferred anchor, not merely the tautological one. The muon scale $\mathrm{Vol}(4_1)/\hbar_q^2$ is distinguished by a self-duality. The figure-eight knot $4_1$ is amphichiral, so its coloured Jones polynomial is bar-invariant: $J_N(4_1; q) = J_N(4_1; q^{-1})$. Its Neumann–Zagier complex volume is real: $\mathrm{CS}(4_1) = 0$ ([`prop:self-dual-higgs-real-volume`](../braids-and-knots/self-dual-higgs-real-volume.md)). The muon thus pins $q_0$ through a quantity with zero imaginary (decay) content. In contrast, the physical observations proton pin $m_p/m_e$ runs through $F_{\mathrm{Bor}} = \lvert \mathrm{tr}_M(\beta_{\mathrm{Bor}}) \rvert$. This is the modulus of a many-body binding endomorphism whose bar-odd ($\mathfrak{Q}_\beta$) face is projected out. The muon provides the cleanest, decay-free $q_0$ determination. This provides a structural reason for the canonical convention, independent of its experimental leverage. The residual $\mu$–$p$ tension ($\approx 11.5$ ppb in $q_0$) is the genuine substrate floor. It is not a modulus-projection artefact, because the observable-level bar-odd face is $O(1)$ and is exactly $\mathfrak{Q}_\beta$ (see audit [`2026-07-02-self-dual-anchor-and-mu-p-tension-framing`](../../../docs/audits/2026-07-02-self-dual-anchor-and-mu-p-tension-framing.md)).

The substrate-$q_0$ derivation remains open research.

## CAL-3 ($\mathfrak{D}_\pi$, proxy $m_\pi$) and CAL-2 proxy $\mathfrak{Q}_\beta$

CAL-3 is $\mathfrak{D}_\pi$, the pion decay width. The proxy is the charged-pion mass $m_\pi$, the orthogonal $\mathrm{Vol}(\mathrm{Hopf})=0$ meson scale, completely independent of $(m_e, q_0)$. The parameter $\mathfrak{Q}_\beta$ below is the proxy for CAL-2 ($\mathfrak{D}_\beta$, the bar-odd $\sinh$ partner of $m_\pi$). It is not the third calibration. The modulus is pinned by $m_\mu/m_e$. We assess whether $q_0$ reproduces $\mathfrak{Q}_\beta$ as a cross-check.

The derived $\mathfrak{Q}_\beta$ fixes the hadronic energy scale $\mathfrak{E}_0$ via $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$. Per audit [`-q-beta-net-ansatz-fitting-finding`](../../../docs/audits/-q-beta-net-ansatz-fitting-finding.md):

- The relation $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$ is postulated, not derived from the canonical per-braid mass formula.
- The +0.17% match between the framework-derived $\mathfrak{E}_0^{(N=0)} = m_e/(q_0(q_0-1))$ and CODATA-calibrated $\mathfrak{E}_0^{(\text{cal})} = \mathfrak{Q}_\beta / |\Delta(\mathrm{net})|$ could be a genuine $N=0$ truncation residual or a substrate-specific artefact.
- Higher-order corrections are recast cohomologically as traces over Khovanov-Rozansky strata of the link projection (audit [`-qbeta-n5-cohomological-breakdown`](../../../docs/audits/-qbeta-n5-cohomological-breakdown.md)). The $N=3$ rung $= J_{\mathrm{Hopf}}(q=1) = -2$ already beats the L2 100$\times$ target by ~24%.

## Summary table

| CAL | Pinned quantity | Cohomological derivation candidate | Status |
|---|---|---|---|
| CAL-1 | $m_e$ in MeV | $\mathrm{Li}_2(q^{-2}) / \hbar_q^2$ for the natural-units value | **unit-choice + derived** |
| CAL-2 | $q_0$ via $m_\mu/m_e$ | $\mathrm{Vol}(4_1) = 2\Lambda(\pi/3)$ on the cohomology side; $q_0$ un-derived | **open** |
| CAL-3 | $m_\pi$ | independent of $(m_e,q_0)$ via $\mathrm{Vol}(\mathrm{Hopf})=0$ | **genuine independent input** |
| *(derived)* | $\mathfrak{E}_0$ via $\mathfrak{Q}_\beta$ | Khovanov-Rozansky cohomology strata | **open** |

## Scope exclusions

This analysis:
- Does not propose a fourth calibration input.
- Does not claim $q_0$ has been cohomologically derived.
- Does not override the no-fourth-CAL audit discipline.
- Does not introduce new fitting, ansätze, or numerological inputs.

It is a structural clarification. The framework's cohomological status is more advanced than its calibration status. Closing the gap remains an open research direction.

## Significance

The three-calibration discipline claims the Standard Model's 19 free parameters reduce to 3. We clarify that the framework aims to reduce this number as close to zero as structural completeness allows. Ideally, it leaves only a single dimensional unit choice (the CAL-1 conversion factor), plus a cohomologically-derived $q_0$ and a cohomologically-derived hadronic-sector residual.

