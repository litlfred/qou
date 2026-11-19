The [topological mass formula](#prop:topological-mass-formula) assigns mass
$\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$. Here $q$ denotes the
[substrate parameter](#def:substrate-parameter). Three non-zero
hyperbolic volumes drive the Descartes universe mass spectrum:

| Knot/Link | Volume | QOU identity |
|-----------|--------|-------------|
| Figure-eight $4_1$ | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx 2.02988$ | Higgs boson |
| Three-twist $5_2$ | $\mathrm{Vol}(5_2) \approx 2.82812$ | Down quark |
| Borromean rings $\mathcal{B}_3$ | $\mathrm{Vol}(\mathcal{B}_3) \approx 7.32772$ | Nucleon |

All torus knots (trefoil, cinquefoil, septafoil) possess zero hyperbolic
volume. They contribute no topological mass from this channel.

**Conjecture.**
The set $\{\mathrm{Vol}(4_1),\; \mathrm{Vol}(5_2),\;
\mathrm{Vol}(\mathcal{B}_3)\}$ is algebraically independent over
$\mathbb{Q}[q, q^{-1}]$. There exists no non-zero polynomial
$P \in \mathbb{Q}[q, q^{-1}][x, y, z]$ satisfying

$$
  P\bigl(\mathrm{Vol}(4_1),\; \mathrm{Vol}(5_2),\;
    \mathrm{Vol}(\mathcal{B}_3)\bigr) = 0.
$$

If the conjecture holds, the physical coefficient ring of the Descartes
universe forms $\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
\mathrm{Vol}(\mathcal{B}_3)]$. This defines a polynomial ring in three
transcendentals over the ground ring. The specialisation map
$\iota \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{R}$ sending
$q \mapsto q_0$ extends to an embedding of this ring into $\mathbb{R}$.
The three volumes remain algebraically independent over
$\mathbb{Q}(q_0)$.

*Remark.* The irrationality of a single hyperbolic 3-manifold volume remains an open problem. The Borel--Zagier conjecture concerns only
$\mathbb{Q}$-linear independence of volumes of non-commensurable
manifolds. This presents a strictly weaker, yet unresolved, claim.
Reid (1991) established $4_1$ as the unique arithmetic hyperbolic knot,
commensurable with $\mathrm{PSL}_2(\mathcal{O}_3)$. The three-twist
$5_2$ is non-arithmetic. The Borromean rings $\mathcal{B}_3$, as a
3-component link, fall outside Reid's classification. The
three complements are pairwise non-commensurable. The Borel--Zagier
conjecture would thus guarantee their $\mathbb{Q}$-linear independence.

**Scope: external open problem, partial categorical approach.**
This conjecture remains external to the framework. Its three forms

$$
  \text{irrationality}
  \;\Longleftarrow\;
  \mathbb{Q}\text{-linear independence}
  \;\Longleftarrow\;
  \text{algebraic independence}
$$

represent recognised open problems in transcendental
number theory. These include [single-volume irrationality](#conj:single-volume-irrationality)
(no hyperbolic 3-manifold volume is known to be irrational), [Borel--Zagier](#conj:borel-zagier-qou-volumes), and the Kontsevich--Zagier and Grothendieck period conjectures. The framework specifies only the choice of the three knots $4_1, 5_2, \mathcal{B}_3$. The mathematical hardness is entirely external.

The framework approaches the conjecture via two complementary, partial reductions. The deeper statement remains open. The sharper reduction is the
[jet-order reduction](#conj:three-knot-jet-order-independence). It
replaces Grothendieck-period machinery with a finite
per-order Gröbner--Shirshov independence computation. The skein engine
executes this computation natively. This pairs with a single QOU-native surreal bridge lemma. This reduction converts an external problem into an incremental
research target natively structured on the framework's jet-order filtration. The second reduction is the [transcendence shadow](#rem:yekutieli-transcendence-shadow). It
reduces algebraic independence to the non-collapse of the brane tower
and Nesterenko-type arithmetic control of the quantum dilogarithm.
Both paths relocate the difficulty. The structural half — the tower
decomposition, Chern--Simons faithfulness, and the downstream
implications (algebraic independence $\Rightarrow$ Borel--Zagier
$\Rightarrow$ irrationality) — holds unconditionally, while the transcendence core isolates as a single explicit hypothesis on which the downstream consequences depend.

The conjecture serves as an ideal statement. It guarantees the predicted spectrum arises from no
algebraic coincidence. As the [formal-chain
remark](#rem:formal-chain-transcendence) records, the mass predictions
and the categorical derivation live entirely over $\mathbb{Z}[q, q^{-1}]$. They function independently of whether the volumes are transcendental, algebraic, or
rational. The framework operates strictly on the proved numerical
[distinctness](#prf:knot-volumes-verification) of the three volumes. This distinctness suffices for all mass predictions.
