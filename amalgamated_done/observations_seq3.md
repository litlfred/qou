<!-- FILE_START: substrate-from-leptons-intro.md -->
We calibrate the substrate parameter $q$ using lepton masses alone. The $q$-deformed Skein relation encodes the deformation of the standard Skein identity. **Knot volume verification (SnapPy)** independently checks hyperbolic volumes. A classification of building-block knots provides Jones polynomials and volumes required for mass formulas. This outputs the calibrated value $q_0 \approx 1.1097$. The subsequent section applies this to the full hadron spectrum.
<!-- FILE_END: substrate-from-leptons-intro.md -->

<!-- FILE_START: epistemic-status-of-calibrations.md -->
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
<!-- FILE_END: epistemic-status-of-calibrations.md -->

<!-- FILE_START: skein-mass-relation.md -->
The mass functional $\mathcal{M}(\mathfrak{H})$ obeys the quantum Skein relation:

$$
q \mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\mathcal{M}(L_0).
$$

Evaluating the lepton mass ratio $m_{\mu}/m_{e}$ determines the local substrate parameter $q$:

$$
\frac{m_{\mu}}{m_{e}} \;\stackrel{\text{LO}}{=}\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
  \approx \frac{:val[Vol_4_1]{precision=6}}{(1 - q^{-1})^2},
\qquad 206.7683 \implies q \approx 1.10998.
$$
<!-- FILE_END: skein-mass-relation.md -->

<!-- FILE_START: knot-volumes-verification.md -->
We independently verify hyperbolic volumes using SnapPy 3.3.

**Verified assertions**:

See [Table 1](#tbl:knot-volumes-verification-table1-data).

**Derived quantities**:

See [Table 2](#tbl:knot-volumes-verification-table2-data).
<!-- FILE_END: knot-volumes-verification.md -->

<!-- FILE_START: building-block-knots.md -->
Every particle is built from knots and links embeddable on Bring's surface. We catalog the building blocks.

## Visual convention

- **Solid** (filled ●) = particle
- **Outlined** (hollow ○) = antiparticle
- **Dashed** (⊙) = neutral antiparticle

The mirror operation $\sigma$ reverses all crossings. For chiral knots, it produces a distinct knot. For amphichiral knots, it returns the same knot.

## Table 1: Fundamental knots

See [Table 1](#tbl:building-block-knots-table1-data).

Torus knots have $\mathrm{Vol} = 0$. Their mass arises entirely from crossing energy at $q \neq 1$.

## Table 2: Derived knots

See [Table 2](#tbl:building-block-knots-table2-data).

The figure-eight knot $4_1$ is amphichiral. Its volume $\mathrm{Vol}(4_1) = 2.0299$ drives the mass mechanism ([cohomological embedding](#prop:cohomological-embedding)).

## Table 3: Links

See [Table 3](#tbl:building-block-knots-table3-data).

## Table 4: Antiparticle completion

See [Table 4](#tbl:building-block-knots-table4-data).

## Mass from knot energy

The mass of a knot $K$ is:

$$
  \mathfrak{m}(K) =  \frac{\mathrm{Vol}(K)}{\hbar_q^2}
  +  \sum_{\text{crossings}} \mathfrak{E}_{\times}(q)
$$

- **Torus knots** ($\mathrm{Vol} = 0$): Mass comes from crossing energy. The trefoil yields $m_{e} = 3 \cdot \mathfrak{E}_{\times}(q) \cdot \mu_0$.
- **Hyperbolic knots** ($\mathrm{Vol} > 0$): Mass combines volume and crossing terms. The figure-eight volume determines $m_\mu / m_e = \mathrm{Vol}(4_1) / \hbar_q^2$, fixing $q_0$.
- **Links**: Linking numbers contribute inter-component crossing energy.

## Jones polynomial at $q = q_0$

See [Table 5](#tbl:building-block-knots-table5-data).

At $q = q_0$, the polynomial encodes the $q$-deformation of the knot's categorical action.

## Table 5: Categorical action at $q = q_0$

The categorical action $\mathfrak{S}_q(K) = \mathrm{tr}_\tau(\rho(\mathcal{B}_K))$ decomposes into a hyperbolic volume term and a crossing energy term. 

**Fundamental constants from $q$:**

See [Table 6](#tbl:building-block-knots-table6-data).

**Categorical action per building block:**

See [Table 7](#tbl:building-block-knots-table7-data).

The neutron--proton mass difference $\delta_{\mathrm{Skein}} = \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) \approx 1.293$ MeV arises from the pair Skein asymmetry between $\mathfrak{d}\mathfrak{d}$ and $\mathfrak{u}\mathfrak{u}$ crossings.

**Key consequence for beta decay.** The electron's categorical action $\mathfrak{S}_q(e)$, the neutrino's $\mathfrak{S}_q(\nu) = 0$, and the nuclear actions $\mathfrak{S}_q(\mathcal{N})$ depend solely on $q$. The $Q$-value $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$ requires no external constants.
<!-- FILE_END: building-block-knots.md -->
