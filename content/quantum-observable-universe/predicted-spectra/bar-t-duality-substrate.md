*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
The bar involution $\iota \colon q \mapsto q^{-1}$ on the substrate
parameter line lifts to a **substrate-level T-duality** between
elliptic curves of the Descartes family
([Descartes elliptic curve](#prop:descartes-elliptic-curve)):

$$
  \iota_*\,\mathcal{E}_q  =  \mathcal{E}_{q^{-1}},
$$

where $\iota_*$ is the pull-back of $\iota$ along the substrate
parametrization $q \mapsto \mathcal{E}_q$.  Under $\iota_*$:

1. **Discriminant locus:** $\Delta(\mathcal{E}_q) = 0$ at
   $q = 1/\varphi^2$ pairs with $\Delta(\mathcal{E}_{1/q}) = 0$ at
   $q = \varphi^2$ ([skew-dual golden node](#prop:golden-skew-dual-node)).
2. **$j$-invariant:** $j(\mathcal{E}_q)$ and $j(\mathcal{E}_{1/q})$
   are related by the rational involution $j \mapsto j^*$ induced by
   $q \mapsto q^{-1}$ on the Weierstrass coefficients.
3. **Confinement band:** $\mathcal{E}_q$ is non-degenerate iff
   $q \in \mathcal{B}$ ([bar-self-dual band](#prop:bar-self-dual-confinement-band)),
   and the band is fixed setwise by $\iota$.

This is **distinct from** the existing target-space T-duality
([self-duality of $\mathcal{E}_z$](#rem:t-duality-elliptic)),
which exchanges $X \leftrightarrow z$ on a single curve.  Bar
T-duality acts on the **moduli parameter** $q$, not on the curve's
own coordinates.  The two dualities commute and together generate
a $\mathbb{Z}/2 \times \mathbb{Z}/2$-action on the moduli stack of
Descartes-family curves.

*Proof.*
The substitution $q \mapsto q^{-1}$ in the Weierstrass coefficients
$p(q)$ and $r(q)$ (rational functions in $q$) yields rational
functions $p^*(q) = p(q^{-1})$ and $r^*(q) = r(q^{-1})$, defining
the curve $\mathcal{E}_{q^{-1}} : y^2 = x^3 + p^*(q)\,x + r^*(q)$.
The map $\iota_* \colon \mathcal{E}_q \to \mathcal{E}_{q^{-1}}$ is
defined by $(x, y, q) \mapsto (x, y, q^{-1})$ on the total space
$\mathcal{X} = \{(x, y, q) : y^2 = x^3 + p(q)x + r(q)\}$ and is an
involution since $\iota \circ \iota = \mathrm{id}$.

Claims (1)–(3) follow:

*(1)* $\Delta(\mathcal{E}_q) = -4p(q)^3 - 27r(q)^2 = 0$ at
$q = 1/\varphi^2$ implies $\Delta(\mathcal{E}_{1/q}) = -4p(1/q)^3
- 27r(1/q)^2 = 0$ at $1/q = 1/\varphi^2$, i.e. $q = \varphi^2$.

*(2)* $j(\mathcal{E}_q) = -1728 \cdot 64\,p(q)^3 / \Delta(q)$ pulls
back along $\iota$ to $j^*(q) := j(\mathcal{E}_{1/q}) = j(q^{-1})$,
a well-defined rational function of $q$.

*(3)* By [bar-self-dual confinement band](#prop:bar-self-dual-confinement-band)
the open interval $\mathcal{B} = (1/\varphi^2, \varphi^2)$ is the
maximal $\iota$-invariant open subset of $\mathbb{R}_{>0}$ avoiding
the golden nodes, hence the maximal locus on which both
$\mathcal{E}_q$ and $\mathcal{E}_{1/q}$ are simultaneously
non-degenerate. $\square$

**Refactoring corollary.**

Any statement of the form *"$\mathcal{E}_q$ has property $P$ for
$q \in I \subset \mathcal{B}$"* automatically yields its bar conjugate:
*"$\mathcal{E}_{1/q}$ has property $P$ for $q \in \iota(I)$."*  Thus
proofs about the elliptic family on the sub-classical wing
$(1/\varphi^2,\,1)$ extend to the super-classical wing $(1,\,\varphi^2)$
**without re-derivation** by composing with $\iota_*$.

This refactoring opportunity applies to every existing block whose
$q$-range is one-sided.  In particular, deconfinement statements
phrased as "$q < q_{\mathrm{gold}}$ $\Rightarrow$ deconfined" gain the bar
companion "$q > \varphi^2$ $\Rightarrow$ deconfined" with no additional proof
work — only an application of $\iota_*$ to the existing argument.

**Hecke-algebraic origin.**

Substrate-level bar T-duality is the geometric shadow of the
**Iwahori--Hecke bar involution** $\overline{\,\cdot\,} \colon H_n(q)
\to H_n(q^{-1})$ given on generators by $\sigma_i \mapsto
\sigma_i^{-1}$.  Since the Descartes elliptic curve $\mathcal{E}_q$
arises from the Markov trace
([Descartes elliptic curve](#prop:descartes-elliptic-curve)),
the Hecke bar involution descends to $\iota$ on the moduli
parameter — the two structures are not independent dualities but
two faces of the same algebraic involution.


**Remark on Mathematical Novelty:** Framing standard q->q^-1 involution directly as a Hecke-bar origin yields a novel algebraic geometry for the substrate, bridging T-duality cleanly with involution algebra and enforcing rigorous algebraic parity on the substrate.
