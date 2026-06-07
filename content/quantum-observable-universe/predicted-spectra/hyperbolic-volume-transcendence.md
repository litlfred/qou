The [topological mass formula](#prop:topological-mass-formula) assigns mass
$\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$, where $q$ is the
[substrate parameter](#def:substrate-parameter).  Three non-zero
hyperbolic volumes drive the Descartes universe mass spectrum:

| Knot/Link | Volume | QOU identity |
|-----------|--------|-------------|
| Figure-eight $4_1$ | $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx 2.02988$ | Higgs boson |
| Three-twist $5_2$ | $\mathrm{Vol}(5_2) \approx 2.82812$ | Down quark |
| Borromean rings $\mathcal{B}_3$ | $\mathrm{Vol}(\mathcal{B}_3) \approx 7.32772$ | Nucleon |

All torus knots (trefoil, cinquefoil, septafoil) have zero hyperbolic
volume and contribute no bare mass from this channel.

**Conjecture.**
The set $\{\mathrm{Vol}(4_1),\; \mathrm{Vol}(5_2),\;
\mathrm{Vol}(\mathcal{B}_3)\}$ is algebraically independent over
$\mathbb{Q}[q, q^{-1}]$.  That is, there exists no non-zero polynomial
$P \in \mathbb{Q}[q, q^{-1}][x, y, z]$ satisfying

$$
  P\bigl(\mathrm{Vol}(4_1),\; \mathrm{Vol}(5_2),\;
    \mathrm{Vol}(\mathcal{B}_3)\bigr) = 0.
$$

If the conjecture holds, the *physical coefficient ring* of the Descartes
universe is $\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
\mathrm{Vol}(\mathcal{B}_3)]$ --- a polynomial ring in three
transcendentals over the ground ring.  The specialisation map
$\iota \colon \mathbb{Z}[q, q^{-1}] \to \mathbb{R}$ sending
$q \mapsto q_0$ extends to an embedding of this ring into $\mathbb{R}$.
In particular, the three volumes are algebraically independent over
$\mathbb{Q}(q_0)$.

*Remark.* Even the irrationality of a single hyperbolic 3-manifold volume is open.  The Borel--Zagier conjecture concerns only
$\mathbb{Q}$-linear independence of volumes of non-commensurable
manifolds --- a strictly weaker claim that is itself unresolved.
Reid (1991) proved that $4_1$ is the unique arithmetic hyperbolic knot,
commensurable with $\mathrm{PSL}_2(\mathcal{O}_3)$.  The three-twist
$5_2$ is non-arithmetic; the Borromean rings $\mathcal{B}_3$, as a
3-component link, fall outside Reid's classification entirely.  The
three complements are pairwise non-commensurable, so the Borel--Zagier
conjecture would at least yield their $\mathbb{Q}$-linear independence.

**Scope: external open problem, partial categorical approach.**
This conjecture is *not* internal to the framework.  In all three of its
forms

$$
  \text{irrationality}
  \;\Longleftarrow\;
  \mathbb{Q}\text{-linear independence}
  \;\Longleftarrow\;
  \text{algebraic independence}
$$

it is a special case of recognised open problems in transcendental
number theory: [single-volume irrationality](#conj:single-volume-irrationality)
(open --- no hyperbolic 3-manifold volume has ever been proved
irrational), [Borel--Zagier](#conj:borel-zagier-qou-volumes), and, in the
present algebraic-independence form, the Kontsevich--Zagier period
conjecture and Grothendieck's period conjecture (algebraic independence
of periods is governed by the motivic Galois group).  Only the *choice*
of the three knots $4_1, 5_2, \mathcal{B}_3$ is framework-specific; the
hardness is entirely external.

The framework does not close the conjecture --- it offers a *partial,
conditional* categorical approach.  The
[transcendence shadow](#rem:yekutieli-transcendence-shadow) reduces
algebraic independence to non-collapse of the brane tower *plus* a
Nesterenko-type arithmetic control of the quantum dilogarithm at every
tower level; that second ingredient is the external open input, so the
reduction relocates the difficulty rather than removing it.  The Lean
formalisation proves only the *structural* half --- the tower
decomposition, Chern--Simons faithfulness, and the downstream
implications (algebraic independence $\Rightarrow$ Borel--Zagier
$\Rightarrow$ irrationality) --- while the transcendence core is
axiomatised as the Lean class `HyperbolicVolumeIndependence` following
the conditional-class convention (the conjecture's content *is* the class
instance, so downstream results stay rigorous-conditional rather than
asserting an unproved theorem).

The conjecture is retained not because the paper depends on it, but as
the *ideal* statement: the guarantee that the predicted spectrum is no
algebraic coincidence.  As the [formal-chain
remark](#rem:formal-chain-transcendence) records, the mass predictions
and the categorical derivation live entirely over $\mathbb{Z}[q, q^{-1}]$
and are unaffected whether the volumes are transcendental, algebraic, or
rational.  The framework operates only with the *proved* numerical
[distinctness](#prf:knot-volumes-verification) of the three volumes,
which is all the predictions require.
