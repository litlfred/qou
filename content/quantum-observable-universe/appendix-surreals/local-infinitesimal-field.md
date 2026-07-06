The appendix previously treated the substrate parameter $q = 1 + \varepsilon$ as a single global element of the valuation ring $\mathcal{O} \subset \mathbf{No}$. This conjecture introduces a richer structure. We treat $\varepsilon$ as a sheaf of infinitesimals across a scheme $X$, with $q(x) = 1 + \varepsilon(x)$ varying locally.

## Setup

Let $X$ be the scheme of quantum observable universes. We treat $X$ as a functor $\mathrm{CRing} \to \mathrm{Set}$.

We evaluate $X$ at the valuation ring ([valuation ring of finite surreals](#rem:valuation-ring-finite-surreals)):

$$
  X(\mathcal{O})
   := \mathrm{Hom}_{\mathrm{CRing}}(\mathcal{O}_X, \mathcal{O}).
$$

An element of $X(\mathcal{O})$ is a surreal-valued point. It assigns a finite surreal to each coordinate of $X$. The standard-part functor $\mathrm{st} : \mathcal{O} \to \mathbb{R}$ induces:

$$
  X(\mathrm{st}) \;:\; X(\mathcal{O}) \twoheadrightarrow X(\mathbb{R}).
$$

This maps each surreal-valued point to its classical real shadow by stripping infinitesimal fluctuations.

## Conjecture

The substrate parameter acts as a section of the structure sheaf valued in $\mathcal{O}$:

$$
  \varepsilon \;\in\; \Gamma(X, \mathfrak{m}_X),
$$

where $\mathfrak{m}_X \subset \mathcal{O}_X$ is the sheaf of infinitesimals on $X(\mathcal{O})$. We write $\varepsilon(x)$ for the stalk at a point $x \in X$:

1. **Local variation**: $\varepsilon(x)$ may differ from $\varepsilon(y)$ for distinct $x, y \in X$. The substrate parameter fluctuates across the scheme.
2. **Standard-part global constant**: $\mathrm{st}(\varepsilon(x)) = 0$ for all $x$. The classical substrate is $q_{\mathrm{classical}} = 1$ everywhere. We match the archimedean limit to a trivial constant.
3. **Birthday-uniform at archimedean scale**: The leading surreal coefficient of $\varepsilon(x)$ is globally constant. It equals the archimedean substrate deviation $q_0 - 1 \approx 0.11$.

We express this as $q(x) = 1 + (q_0 - 1) + \delta(x)$, where $\delta(x)$ is a strictly-infinitesimal local fluctuation with zero mean and birthday-ordered magnitude distribution.

## Significance

1. **Halo structure**: Every classical real point of $X$ possesses a halo of infinitesimally-fluctuated surreal points. The functor $X(\mathrm{st})$ collapses all halo points to the classical point. Within the halo, distinct surreal fluctuations resolve.
2. **Non-global symmetries**: An archimedean global symmetry may break locally at the infinitesimal scale without altering the classical image. This echoes approximate isospin or chiral symmetries in particle physics.
3. **Singularity detection**: We define a singularity as a point $x_0$ where some quantity diverges. The divergence carries a specific normal-form order $\ordw(\cdot)$ that varies locally near $x_0$.

## Relation to existing conjectures

We refine the Hahn-series substrate. Instead of a single Hahn series, $q$ becomes a sheaf of Hahn series. The base $\mathbb{R}$-shadow remains unchanged.

We specialize [archimedean-stpart](#conj:archimedean-stpart) to the sheaf-theoretic setting. The archimedean QOU acts as the standard-part sheaf-morphism of the surreal QOU.

## Proof strategy

**Mathematical layer (existence of local sheaf structure)**:

1. We establish $\mathcal{O}$ as a valid coefficient ring for the scheme $X$. It is a local ring and satisfies standard sheaf-construction axioms.
2. We define $\mathfrak{m}_X$ as the kernel sheaf of the structure-sheaf morphism $\mathcal{O}_X \to (\mathcal{O}/\mathfrak{m})_X = \mathbb{R}_X$.
3. We verify global sections of $\mathfrak{m}_X$ exist via the constant section $\varepsilon \mapsto \varepsilon$.
4. We characterize which global sections preserve the rigid monoidal QOU axioms up to $\varepsilon$-relaxations ([infinitesimal-frobenius](#conj:infinitesimal-frobenius)).

**Physical layer (uniqueness of the fluctuation distribution)**:

5. We assume the fluctuation distribution $\delta(x)$ possesses an explicit form (e.g., zero-mean Gaussian).
6. We show classical observables remain unchanged under standard-part.
7. We show no non-trivial fluctuation distributions exist at leading order beyond the global one. This establishes rigidity.

**Falsification path**: Produce two distinct sheaf sections $\varepsilon_1, \varepsilon_2$ on $X$ that yield the same archimedean QOU under $X(\mathrm{st})$ but differ in a surreal observable.

**Provability assessment**: The mathematical layer is provable once `QOU.AppendixSurreals.ValuationRing` is developed. The physical layer remains speculative.
