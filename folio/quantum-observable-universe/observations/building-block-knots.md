Every particle is built from knots and links embeddable on Bring's surface. The building blocks are catalogued here.

## Visual convention

- **Solid** (filled ●) = particle
- **Outlined** (hollow ○) = antiparticle
- **Dashed** (⊙) = neutral antiparticle

The mirror operation $\sigma$ reverses all crossings. For chiral knots, it produces a distinct knot. For amphichiral knots, it returns the same knot.

## Table 1: Fundamental knots

Throughout Tables 1, 3, and 5, $J(q)$ denotes the unknot-normalized Jones polynomial determined by $J(0_1) = 1$ and the skein relation $q^{-1} J(L_+) - q J(L_-) = (q^{1/2} - q^{-1/2}) J(L_0)$ (specializing the two-variable HOMFLY polynomial at $v = q$, $z = q^{1/2} - q^{-1/2}$).

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

Evaluating the exact polynomials $J(q)$ of Tables 1--3 at the proton-anchored substrate parameter $q_0 \approx 1.10997858$ yields the numerical values in Table 5, encoding the $q$-deformation of each knot's categorical action.

## Table 5: Categorical action at $q = q_0$

The categorical action $\mathfrak{S}_q(K) = \mathrm{tr}_\tau(\rho(\mathcal{B}_K))$ decomposes into a hyperbolic volume term and a crossing energy term. 

**Fundamental constants from $q$:**

See [Table 6](#tbl:building-block-knots-table6-data).

**Categorical action per building block:**

See [Table 7](#tbl:building-block-knots-table7-data).

The neutron--proton mass difference $\delta_{\mathrm{Skein}} = \mathcal{S}_{\mathfrak{d}\mathfrak{d}}(q) - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) \approx 1.293$ MeV arises from the pair Skein asymmetry between $\mathfrak{d}\mathfrak{d}$ and $\mathfrak{u}\mathfrak{u}$ crossings.

**Key consequence for beta decay.** The electron's categorical action $\mathfrak{S}_q(e)$, the neutrino's $\mathfrak{S}_q(\nu) = 0$, and the nuclear actions $\mathfrak{S}_q(\mathcal{N})$ depend solely on $q$. The $Q$-value $Q = \mathfrak{S}_q(\mathrm{par}) - \mathfrak{S}_q(\mathrm{dau}) - \mathfrak{S}_q(e)$ requires no external constants.
