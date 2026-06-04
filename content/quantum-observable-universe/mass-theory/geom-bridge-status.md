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
| 4 | $-12 / (-64) = \tfrac{3}{16} = \kappa$ | **Disproved as structural** — the $-64$ matches only at $h^2$; see below |
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

2. **Link 4 (the $-64$ normalisation) — DISPROVED as structural.**
   The feedback map $\Phi_0$ was hypothesised to divide by a constant
   $-64$ to reach $\kappa = \tfrac{3}{16}$.  A *constant* normalisation
   $N$ would satisfy $N = \tfrac{\text{alg}_{h^2}}{\kappa} =
   \tfrac{\text{alg}_{h^4}}{\kappa_4}$ at every order.  Direct
   computation (`phi0_normalization_disproof.py`) gives
   $$
     \tfrac{\text{alg}_{h^2}}{\kappa} = \tfrac{-12}{3/16} = -64,
     \qquad
     \tfrac{\text{alg}_{h^4}}{\kappa_4} = \tfrac{-6}{-0.7578\ldots}
       = +7.92,
   $$
   which **disagree**.  No constant $N$ exists; the $-64$ matched at
   $h^2$ by coincidence (and four candidate "structural" readings —
   $2^6$, $2^{|\chi|}$, $|Q_8|^2$, $\dim(V)^6$ — all collapse to $64$,
   the degeneracy tell of a numerical accident, not a derivation).
   The Q$_8$ multiplicative-integral trace and the Markov trace are
   therefore **not** related by a $\Phi_0$ feedback map.

What **is** secured by the proved Link 1 is the precise algebraic
object — the integer $-12$, equal to $\dim(V)\cdot\chi(\Sigma_4)$ —
that any categorical bridge must reproduce.  But the boundary
coefficient $\kappa = \tfrac{3}{16}$ is **not** reached from $-12$ by
a constant feedback map (Link 4 disproved above), so the chain does
not close as a simple scalar cascade.  The honest open question is
therefore: **does the fibre functor $\tau$ relate the algebraic
$h$-expansion to the Markov-trace $h$-expansion at all orders** (not
just $h^2$)?  The $h^4$ disagreement shows that whatever $\tau$ is,
it is not multiplication by a constant — it must be an order-mixing
map, or the algebraic and boundary sides measure genuinely different
invariants that happen to share the $h^2$ value.
