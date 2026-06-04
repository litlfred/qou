**Remark (logical status — what is proved, what is open).**

The identity
[`prop:crossed-module-euler-characteristic`](#prop:crossed-module-euler-characteristic)
sits at the algebraic end of a three-layer chain that the
$\mathrm{Geom}$ functional
([`conj:geom-universality`](#conj:geom-universality)) is conjectured
to traverse:

$$
  \underbrace{\dim(V)\cdot\chi(\Sigma_4) = -12}_{\text{algebraic } (Q_8)}
  \;\xrightarrow{\;\times\,\tfrac{2G}{3}\;}\;
  \underbrace{-8G = \mathrm{Vol}(\mathcal{B}_3)}_{\text{geometric}}
  \;\xrightarrow{\;\Phi_0\,:\,\div(-64)\;}\;
  \underbrace{\tfrac{3}{16} = \kappa}_{\text{boundary (Markov trace)}}
$$

This remark records the **exact status of each link**, so the chain
is never over-claimed as a single proved result.

| Link | Statement | Status |
|------|-----------|--------|
| 1 | $\operatorname{tr}(h^2\text{ curvature}) = \dim(V)\cdot\chi(\Sigma_4) = -12$ | **Proved** (`native_decide`; [`prop:crossed-module-euler-characteristic`](#prop:crossed-module-euler-characteristic)) |
| 2 | $\tfrac{2G}{3} = \mathrm{Vol}(\mathcal{B}_3)/(\dim(V)\cdot|\chi|) = \tfrac{8G}{12}$ | **Proved** (arithmetic identity) |
| 3 | $\mathrm{Vol}(\mathcal{B}_3) = 8G$ | **Proved** (Adams 1985, ideal-octahedral tessellation) |
| 4 | $-12 / (-64) = \tfrac{3}{16} = \kappa$ | **Arithmetic holds**, but $-64$ is currently *match-defined*, not derived |
| 5 | $\tau$ carries the algebraic $-12$ to the geometric $-8G$ categorically | **Conjectural** — the single open categorical link |

**The two genuinely open points.**

1. **Link 5 (Neumann–Zagier / Yekutieli realisation).**  Whether
   the fibre functor $\tau$ actually realises the bridge factor
   $\tfrac{2G}{3}$ — i.e. whether the algebraic Euler-characteristic
   count and the hyperbolic volume are the *same* invariant viewed
   through $\tau$ — is the content of the
   $\mathrm{Geom}$-universality programme.  It is not settled by the
   finite $Q_8$ computation, which only establishes the algebraic
   endpoint $-12$.

2. **Link 4 (the $-64$ normalisation).**  The feedback map
   $\Phi_0$ divides by $-64 = 2^6$ to reach the Markov-trace
   coefficient $\kappa = \tfrac{3}{16}$.  At present $-64$ is
   *chosen* to make the arithmetic close; a derivation of $-64$
   from the crossed-module structure (e.g. as $|Q_8| \times 8$, or
   $2^{\dim V} \times 2^{\dim V}$) would upgrade Link 4 from
   "match-defined" to "derived".

What **is** secured by the proved Link 1 is the precise algebraic
object — $\dim(V)\cdot\chi(\Sigma_4)$ — that any categorical bridge
must reproduce.  This narrows the open question from "find the
mechanism" to "show $\tau$ realises a known target", which is the
productive form of the remaining problem.
