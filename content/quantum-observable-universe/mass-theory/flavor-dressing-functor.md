**Definition.**
*The **flavor dressing functor** is the categorical assignment
of a dressed-mass scale to each quark flavor:*

$$
  \mu \colon \mathbf{Flavor} \longrightarrow \mathbb{R}_{>0},
  \qquad
  q \in \{\mathfrak{u}, \mathfrak{d}, \mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}\}
  \longmapsto
  \mu_q \in \mathbb{R}_{>0}.
$$

*Here $\mathbf{Flavor}$ is the discrete category whose objects are
the six quark flavors and whose only morphisms are identities; the
target $\mathbb{R}_{>0}$ is the positive real line carrying the
canonical commutative-monoid structure under multiplication.*

## Scope of this paper

The current paper formalises the functor on the doublet
$\{\mathfrak{u}, \mathfrak{d}\}$ only. Heavy flavors
$\{\mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}\}$ are
included in the categorical signature for forward compatibility
but their individual $\mu_q$ values are open
(no derivation is committed in this revision).

## Categorical role

The functor is the chapter-level bridge between two layers that
already live in this chapter:

1. **Substrate side** — the splitting $\mu_{\mathfrak{d}} - \mu_{\mathfrak{u}}$
 is determined by the substrate flavor split
 ([`prop:flavor-split-substrate`](../observations/flavor-split-substrate.md))
 modulo the Skein factor of
 [`lem:pair-skein-mass-formula`](../observations/pair-skein-mass-formula.md);
 see [`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md).

2. **Bounds side** — the splitting respects the categorical bound
 coming from the substrate factors
 $\hbar_q$, $h_q$, $[2]_q$; see
 [`thm:flavor-mass-splitting-bound`](flavor-mass-splitting-bound.md).

## Composition with other functors

The flavor dressing functor composes with the
[shell dressing morphism](#def:dressed-particle) at the
hadron / atom level:

```tex
\begin{tikzcd}
  \mathbf{Flavor}
  \arrow[r, "\mu"] \arrow[d, "\Phi"]
  & \mathbb{R}_{>0}
  \\
  \mathbf{Hadron}
  \arrow[r, "m_{\mathrm{bare}}"']
  & \mathbb{R}_{>0}
  \arrow[u, "P_{\mathrm{bare}} \mapsto P_{\mathrm{dressed}}"']
\end{tikzcd}
```

where $\Phi$ is the quark-content functor (e.g. $\Phi(\mathfrak{p})
= \mathfrak{u}\mathfrak{u}\mathfrak{d}$, $\Phi(\mathfrak{n}) =
\mathfrak{u}\mathfrak{d}\mathfrak{d}$) and the right-vertical
arrow lifts a bare hadron mass to its electron-dressed atomic mass.

## Functor versus function

The discrete-category framing makes the dressing assignment
**accordingly** compatible with the chapter's other categorical
constructions (Markov trace, Hoefsmit functor, Wedderburn block
decomposition). In particular, sums over flavors that appear in
hadronic mass formulas (e.g. $\sum_q n_q \cdot \mu_q$ for quark
content $\{n_q\}$) are then natural transformations of functors,
not ad-hoc weighted sums.

## Lean encoding

The Lean side carries the functor as a typeclass
`FlavorDressingFunctor` with field `μ : Flavor → ℝ` and positivity
hypothesis `μ_pos : ∀ q, 0 < μ q`. Instances at specific values of
the substrate parameter (e.g. $q = q_0$) are provided by sibling
files; the canonical instance at $q_0$ uses the derivation in
[`prop:flavor-dressed-mass-from-substrate-split`](flavor-dressed-mass-from-substrate-split.md)
plus a chosen value of the nucleon-mass average $M_N$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
