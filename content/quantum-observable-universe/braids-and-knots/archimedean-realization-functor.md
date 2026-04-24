**Definition.**
*The **archimedean realization functor** of the QOU substrate is
the composite*

$$
  \mathcal{R}_{\mathrm{top}}
  \;:\;
  \widehat{\mathcal{M}}
  \;\xrightarrow{\;\;\chi_{\mathrm{top}}\;\;}\;
  \widehat{\mathcal{M}} \otimes_{K_0(\mathrm{Var})} \mathbb{Z}
  \;\xrightarrow{\;\;\pi_\infty\;\;}\;
  \mathbb{R}
$$

*sending the motivic class $[X]$ to its topological Euler
characteristic $\chi_{\mathrm{top}}(X)$ followed by the
**archimedean projection** $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$
of the [adelic substrate](#def:adelic-substrate). The composite
$\mathcal{R}_{\mathrm{top}}$ is the topological realization of the
motivic measure: it maps motives to real-valued physical observables.*

**The two halves.**

1. **Realization of motives.** A motivic integral
   $\int_{\mathcal{L}(X)} d\mu \in \widehat{\mathcal{M}}$
   ([motivic mass measure](#def:motivic-mass-measure))
   is a class in the Grothendieck ring of varieties — a *geometric
   shape*, not a number. The topological realization
   $\chi_{\mathrm{top}}$ sends $[X]$ to $\chi(X) \in \mathbb{Z}$
   (Euler characteristic), or more refinedly to a Hodge-theoretic
   invariant such as a hyperbolic volume when $X$ has a hyperbolic
   structure on its smooth part.

2. **Adelic projection.** A laboratory measurement is an evaluation
   of an adelic observable at the archimedean place $\infty$:
   $\pi_\infty \colon \mathbb{A} \to \mathbb{R}$ discards the
   non-archimedean coordinates $\mathbb{Q}_p$ and keeps only the
   real component. Stability of the underlying state depends on
   the full adelic ring; the *measured value* depends only on
   $\pi_\infty$.

The physical observable extracted from a state with motivic
description $[X]$ is therefore

$$
  \mathrm{Obs}_{\mathbb{R}}(X)
  \;=\;
  \mathcal{R}_{\mathrm{top}}\!\left(
    \int_{\mathcal{L}(X)} d\mu
  \right)
  \;\in\;\mathbb{R}.
$$

**Compatibility with the spatial realization.** The
[spatial realization functor](#def:spatial-realization-functor)
$\tau \colon \mathbf{C} \to \mathrm{Sh}(M)$ realizes the categorical
substrate as smooth geometry over a manifold $M$.
$\mathcal{R}_{\mathrm{top}}$ is its measure-theoretic counterpart:
where $\tau$ realizes objects (algebras, sheaves, connections),
$\mathcal{R}_{\mathrm{top}}$ realizes their motivic *volumes*.
The two are compatible — $\mathcal{R}_{\mathrm{top}}$ factors
through $\tau$ on the part of $\widehat{\mathcal{M}}$ supported by
the spatial realization — but $\mathcal{R}_{\mathrm{top}}$ extends
to motives that have no smooth realization (e.g. the exceptional
divisors of singular blow-ups in
[motivic mass measure](#def:motivic-mass-measure)).

**Synthesis.** The QOU framework computes macroscopic observables
from discrete quantum data along a single chain:

$$
  \begin{array}{c}
   \text{local }q\text{-data at each prime }p
   \;\xrightarrow{\;\text{adelic stitch}\;}\;
   \mathbb{A}\text{-valued global state}
   \\[0.5ex]
   \;\xrightarrow{\;\int_{\mathcal{L}(X)} d\mu\;}\;
   \text{motivic class in }\widehat{\mathcal{M}}
   \\[0.5ex]
   \;\xrightarrow{\;\mathcal{R}_{\mathrm{top}} = \pi_\infty \circ \chi_{\mathrm{top}}\;}\;
   \mathrm{Obs}_\mathbb{R}\in\mathbb{R}.
  \end{array}
$$

No continuous differential equations are integrated; no Lebesgue
measure on a smooth manifold is assumed. Discrete categorical data
on the [arc space](#def:arc-space) of the substrate is assembled
adelically, integrated motivically, and projected archimedeanly
into the laboratory continuum. The Kashaev limit of the
[algebraic quantum volume](#def:algebraic-quantum-volume) is the
canonical instance of $\mathcal{R}_{\mathrm{top}}$ in action; see
[Kashaev limit as archimedean realization](#rem:kashaev-as-archimedean-realization).
