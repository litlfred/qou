Let $\beta \in B_n$ be a braid with closure
$\widehat{\beta} = K \subset S^3$ and let
$\{\sigma_0, \dots, \sigma_{n-2}\}$ enumerate its crossings (one
per Hecke generator instance). For each subset
$S \subseteq \{0, \dots, n-2\}$, the **Φ$_q$-piece $K_S \subseteq S^3$**
is the link obtained from $\widehat{\beta}$ by replacing each crossing
$\sigma_i$ with $i \notin S$ by its $L_0$-smoothing (Kauffman skein
resolution [Kauffman bracket](#thm:jones-markov-trace)) while leaving
the crossings $\{\sigma_i : i \in S\}$ intact.

Concretely: let $\beta_S \in B_n$ denote the braid obtained from
$\beta$ by deleting (i.e., replacing by the identity strand) every
$\sigma_i$ with $i \notin S$ and keeping every $\sigma_i$ with $i \in S$.
Then

$$
  K_S \;:=\; \widehat{\beta_S}
  \;\subseteq\; S^3.
$$

The Φ$_q$ tower
([mass endomorphism tower](#prop:mass-endomorphism-tower))
indexes its summands by the *non-empty* subsets with
$\lvert S \rvert \leq 2$ — singletons and pairs — but the
construction above is well-defined for *every* $S$, including
$S = \emptyset$ (the trivial unlink) and $S = \{0, \dots, n-2\}$
(the original closure $K$). The full family $\{K_S\}_{S \subseteq
\{0,\dots,n-2\}}$ is what enjoys the structural properties below;
the truncation $\lvert S \rvert \leq 2$ is a property of the tower,
not of the Φ$_q$-piece itself.

The construction satisfies three structural properties:

1. **Functoriality.** $K_\emptyset$ is the trivial $n$-component
   unlink (no crossings remain); $K_{\{0,\dots,n-2\}} = K$ is the
   original closure.

2. **Subset compatibility.** For $S \subseteq T$ the link $K_S$ is
   obtained from $K_T$ by smoothing every crossing in $T \setminus S$,
   i.e., $K_S = (K_T)_S$.

3. **Categorical interpretation.** The same family $\{K_S\}_S$ is
   the geometric shadow of the Wedderburn-block stratification of the
   transient mass element
   ([categorical mass as Markov trace](#prop:categorical-mass-markov)):
   the spectral coordinate $\prod_{i \in S} \hat{V}_i$ on the algebraic
   side localises geometrically to the link $K_S$.

The piece $K_S$ is the geometric carrier of the per-$S$ summand
$\Phi_q\bigl(\bigl\lvert\prod_{i \in S} \hat{V}_i^{\mathrm{full}}\bigr\rvert\bigr)$
of the Φ$_q$ tower
([mass endomorphism tower](#prop:mass-endomorphism-tower)).
The empty piece $K_\emptyset$ is the descended (level-zero) carrier;
all other $K_S$ with $1 \leq \lvert S \rvert \leq 2$ are the transient
carriers.

The hyperbolic volume $\mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S)$
of the piece is well-defined whenever the complement is hyperbolic;
when it is not (e.g., when $K_S$ is an unknot or torus link), the
piece contributes zero hyperbolic volume by convention. The Φ$_q$-piece
is the unit on which the archimedean realisation
([archimedean realization functor](#def:archimedean-realization-functor))
acts when restricted to the per-block summands of the tower.
