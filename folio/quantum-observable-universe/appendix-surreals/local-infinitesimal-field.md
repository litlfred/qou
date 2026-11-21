The appendix so far treats the substrate parameter $q = 1 +
\varepsilon$ as a **single global element** of the valuation ring
$\mathcal{O} \subset \mathbf{No}$. This conjecture proposes a
richer structure: $\varepsilon$ is a **sheaf** of infinitesimals
across a scheme $X$, with $q(x) = 1 + \varepsilon(x)$ varying
locally from patch to patch.

## Setup

Let $X$ be the scheme of quantum observable universes (underlying
the categorical substrate of this paper). Following the
points-and-topology framework already in the paper, treat $X$ as a
functor $\mathrm{CRing} \to \mathrm{Set}$.

Evaluate $X$ at the valuation ring
([valuation ring of finite surreals](#rem:valuation-ring-finite-surreals)):

$$
  X(\mathcal{O})
   := \mathrm{Hom}_{\mathrm{CRing}}(\mathcal{O}_X, \mathcal{O}).
$$

An element of $X(\mathcal{O})$ is a "surreal-valued point" — an
assignment of a finite surreal to each coordinate of $X$. The
standard-part map $\mathrm{st} : \mathcal{O} \to \mathbb{R}$
induces

$$
  X(\mathrm{st}) \;:\; X(\mathcal{O}) \twoheadrightarrow X(\mathbb{R}),
$$

sending each surreal-valued point to its classical real shadow
by stripping infinitesimal fluctuations.

## Conjecture

The substrate parameter is not a global constant $q \in \mathbb{R}$
but a **section of the structure sheaf** valued in $\mathcal{O}$:

$$
  \varepsilon \;\in\; \Gamma(X, \mathfrak{m}_X),
$$

where $\mathfrak{m}_X \subset \mathcal{O}_X$ is the sheaf of
infinitesimals on $X(\mathcal{O})$. Writing $\varepsilon(x)$ for
the stalk at a point $x \in X$:

1. **Local variation**: $\varepsilon(x)$ may differ from
 $\varepsilon(y)$ for distinct $x, y \in X$ — the substrate
 parameter *fluctuates* across the scheme.

2. **Standard-part global constant**: $\mathrm{st}(\varepsilon(x)) = 0$
 for all $x$, so the classical substrate is $q_{\mathrm{classical}} = 1$
 everywhere — matching the archimedean limit to a trivial
 constant.

3. **Birthday-uniform at archimedean scale**: the *leading
 surreal coefficient* of $\varepsilon(x)$ (i.e., the coefficient
 of $\omega^{-1}$ in the Conway normal form) *is* globally
 constant, and equals the paper's archimedean substrate deviation
 $q_0 - 1 \approx 0.11$.

Equivalently, $q(x) = 1 + (q_0 - 1) + \delta(x)$ where $\delta(x)$
is a strictly-infinitesimal local fluctuation with zero mean and
birthday-ordered magnitude distribution.

## Significance

1. **Halo structure**: every classical real point of $X$ is
 surrounded by a *halo* (monad) of infinitesimally-fluctuated
 surreal points. Under the functor $X(\mathrm{st})$ all halo
 points collapse to the classical point — but within the halo,
 distinct surreal fluctuations are resolved.

2. **Non-global symmetries**: a symmetry of this paper's QOU
 that is global in the archimedean sense may be broken at the
 infinitesimal scale *locally* (at specific points $x$), without
 affecting the classical image. This is analogous to approximate
 isospin / chiral symmetries in particle physics.

3. **Singularity detection**: a "singularity" of this paper's
 QOU is a point $x_0$ where some quantity diverges. In the
 surreal lift, the divergence has a specific normal-form order
 $\ordw(\cdot)$ — which, by locality, can vary in a neighbourhood
 of $x_0$.

## Relation to existing conjectures

This conjecture refines Hahn-series
substrate: instead of $q$ being a single
Hahn series, it is a *sheaf* of Hahn series. The base $\mathbb{R}$-
shadow agrees with the paper in both cases.

It also specialises [archimedean-stpart](#conj:archimedean-stpart)
to the sheaf-theoretic setting: the archimedean QOU is the
standard-part *sheaf-morphism* of the surreal QOU, not a
single-point morphism.

## Proof strategy

**Mathematical layer (existence of local sheaf structure)**:

1. Show that $\mathcal{O}$ is a valid coefficient ring for the
 scheme $X$: it is a local ring, hence satisfies all standard
 sheaf-construction axioms (easy).

2. Define $\mathfrak{m}_X$ as the kernel sheaf of the structure-
 sheaf morphism $\mathcal{O}_X \to (\mathcal{O}/\mathfrak{m})_X
   = \mathbb{R}_X$. This is the standard construction of an ideal
 sheaf.

3. Verify that global sections of $\mathfrak{m}_X$ exist
 (non-vacuously): the constant section $\varepsilon \mapsto
   \varepsilon$ witnesses this.

4. Characterise which global sections give consistent QOU
 structure — i.e., which $\varepsilon$-valued $q$ deformations
 preserve the rigid monoidal axioms.

**Physical layer (uniqueness of the fluctuation distribution)**:

5. Assume the fluctuation distribution $\delta(x)$ has some
 explicit form (e.g., zero-mean Gaussian on the classical
 spectrum of $X$).

6. Show that the classical observables (particle masses,
 $\mathcal{Q}$-values, spectral gaps) are *unchanged* under
 standard-part — equivalent to the sheaf being $\mathrm{st}$-
 compatible.

7. Show that there are *no* non-trivial fluctuation distributions
 at leading order beyond the global one — equivalent to
 rigidity of this paper QOU.

**Falsification path**: produce two distinct sheaf sections
$\varepsilon_1, \varepsilon_2$ on $X$ both producing the same
archimedean QOU under $X(\mathrm{st})$ but *differing* in some
surreal observable (e.g., the second-order coefficient of a
particle mass). Such non-uniqueness would show that the surreal
lift is strictly richer than the archimedean, and the extra
information is physical.

**Provability assessment**: mathematical layer provable once
the finite-surreal valuation-ring foundations are developed.
Physical layer speculative — depends on interpretation.
