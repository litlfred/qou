The three-calibration discipline ([`prop:three-calibration-discipline`](#prop:three-calibration-discipline)) uses $m_e$, $m_\mu/m_e$, and $m_\pi$ as CODATA/PDG inputs. It maps them bijectively to three cohomological data of the Bring Hodge structure $H^1 = 2W$: the $W$-plane scale, the $W$-plane modulus, and the orthogonal $\mathrm{Vol}(\mathrm{Hopf})=0$ meson class. We clarify the epistemic status of each input.

The parameter $\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$ proxies CAL-2 (the neutron $\beta$-decay width $\mathfrak{D}_\beta$). It is not a fourth calibration. The CAL-2 modulus is most precisely pinned by $m_\mu/m_e$. Reproducing $\mathfrak{Q}_\beta$ from $q_0$ provides a $0.17\%$ cross-check. We treat it as the bar-odd $\sinh$ partner of the meson scale $m_\pi$. CAL-3 is the pion decay width $\mathfrak{D}_\pi$ (proxy $m_\pi$).

We introduce no fourth calibration or numerological substitution. The clauses of [`prop:three-calibration-inputs`](#prop:three-calibration-inputs) remain in force.

## CAL-1 ($m_e$) — unit choice + cohomological period

CAL-1 has two roles:

| Role | Type | Status |
|---|---|---|
| Unit of mass (MeV $\leftrightarrow$ natural units) | dimensional convention | **unit choice** |
| Numerical value $m_e(\text{natural}) = \mathrm{Li}_2(q^{-2}) / \hbar_q^2 \approx 112$ | dimensionless | **cohomologically derived** |

The framework requires the conversion factor $m_e(\text{MeV})/m_e(\text{natural}) \approx 4.57 \times 10^{-3}$ MeV. This is a unit choice, not a fundamental constant.

## CAL-2 ($m_\mu/m_e$) — substrate $q_0$ pin

CAL-2 fixes $q_0$ via $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$.

- $\mathrm{Vol}(4_1) = 2\Lambda(\pi/3) \approx 2.0299$ is pure cohomology (no CODATA input).
- $\hbar_q = (q-1)/q$ is pure algebra (no CODATA input).
- $q_0 \approx 1.10998$ is pinned by matching $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$ to the CODATA value $206.7682830$.

The relation $m_\mu = m_e \times \mathrm{Vol}(4_1)/\hbar_q^2$ is structurally tautological. We defined $q_0$ to enforce it. The muon is the structurally preferred anchor due to a self-duality: the figure-eight knot $4_1$ is amphichiral, and its Neumann–Zagier complex volume is real ([`prop:self-dual-higgs-real-volume`](../braids-and-knots/self-dual-higgs-real-volume.md)). It pins $q_0$ through a quantity with zero imaginary (decay) content. In contrast, the proton pins $m_p/m_e$ through a modulus of a many-body binding endomorphism. The muon provides the cleanest $q_0$ determination. The residual $\mu$–$p$ tension ($\approx 11.5$ ppb in $q_0$) is the genuine substrate floor.

## CAL-3 ($\mathfrak{D}_\pi$, proxy $m_\pi$) and CAL-2 proxy $\mathfrak{Q}_\beta$

CAL-3 is the pion decay width $\mathfrak{D}_\pi$ (proxy $m_\pi$). This is independent of $(m_e, q_0)$. The parameter $\mathfrak{Q}_\beta$ proxies CAL-2.

The derived $\mathfrak{Q}_\beta$ fixes the hadronic scale $\mathfrak{E}_0$ via $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$.

- We postulate $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})| \cdot \mathfrak{E}_0$.
- The +0.17% match between derived $\mathfrak{E}_0^{(N=0)}$ and calibrated $\mathfrak{E}_0^{(\text{cal})}$ is either a truncation residual or a substrate artefact.
- Higher-order corrections correspond to traces over Khovanov-Rozansky strata.

## Summary table

| CAL | Pinned quantity | Cohomological derivation candidate | Status |
|---|---|---|---|
| CAL-1 | $m_e$ | $\mathrm{Li}_2(q^{-2}) / \hbar_q^2$ | **unit-choice + derived** |
| CAL-2 | $q_0$ via $m_\mu/m_e$ | $\mathrm{Vol}(4_1) = 2\Lambda(\pi/3)$ | **open** |
| CAL-3 | $m_\pi$ | independent of $(m_e,q_0)$ | **genuine input** |
| *(derived)* | $\mathfrak{E}_0$ via $\mathfrak{Q}_\beta$ | Khovanov-Rozansky strata | **open** |

## Scope exclusions

This analysis:
- Proposes no fourth calibration.
- Does not claim $q_0$ is cohomologically derived.
- Retains the no-fourth-CAL discipline.
- Introduces no fitting inputs.

It structuralizes the framework's calibrations.

## Significance

The framework aims to reduce the Standard Model's 19 free parameters to a single unit choice, a cohomologically-derived $q_0$, and a derived hadronic residual.
