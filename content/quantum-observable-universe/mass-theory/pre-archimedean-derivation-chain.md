This section is a self-contained survey of how the framework derives a
mass.  The aim is to follow a single
thread — from the categorical action of a quantum observable universe to a
number in MeV — and to name, at each step, the algorithm that makes the
step computable.  Every quantity along the way lives in the field
$\mathbb{Q}(q)$ of rational functions in the substrate parameter $q$; no
analytic limit, no fitting, and no empirical nuclear-physics constant
enters until the Archimedean realization functor is applied at the very
end.

The calibration is fixed once, by three weak-sector inputs
([rem:calibration-inputs](#rem:calibration-inputs)): the electron mass
$m_e$ sets the unit; the neutron $\beta$-decay width $\mathfrak{D}_\beta$
fixes the substrate parameter $q_0$; and the pion decay width
$\mathfrak{D}_\pi$ fixes the orthogonal meson scale.  Their most precisely
measured proxies — $m_e$, the lepton ratio $m_\mu/m_e$ (with the $Q$-value
$\mathfrak{Q}_\beta = \hbar/\mathfrak{D}_\beta$), and the pion mass $m_\pi$
— are the numbers we read from experiment.

See [Table 1](#tbl:pre-archimedean-derivation-chain-table1-data).

Everything else — every nucleon mass, every binding energy, every
$\beta$-decay $Q$-value — is a prediction obtained by evaluating an
algebraic invariant at $q_0$.  We organise the survey as eleven steps.
Steps 1–8 build the algebraic object (the Markov trace of a knot, computed
inside an Iwahori–Hecke algebra); steps 9–11 evaluate it as a mass, a
binding energy, and a decay width.

***

## The shape of the derivation

Two ideas carry the whole construction.

The first is that a **particle is a knot** and its **mass is a trace**.  A
hadron $\mathfrak{H}$ is presented by a braid $\beta$; closing the braid
gives a knot or link $K$; the categorical observable attached to $K$ is the
Markov trace $\mathrm{tr}_M$ of the braid in an Iwahori–Hecke algebra
$H_n(q)$.  Mass, binding, and decay are all read off this one invariant.

The second is that the algebra is **finite and computable**.  The
embeddability of knots in the genus-four state space caps the operator
content; the Iwahori–Hecke algebra is semisimple at generic $q$, so it
splits as a direct sum of matrix blocks indexed by partitions; and a
Gröbner–Shirshov normal form turns every braid word into a canonical
representative.  These three facts mean the trace is not an integral over a
continuum but a finite sum of $q$-rational numbers, evaluated symbolically.

We keep two registers of notation throughout.  Categorical objects are
bold ($\mathbf{C}$ for the category) or calligraphic ($\mathcal{B}_K$ for a
canonical braid word, $\mathcal{S}$ for the state bundle); physical
observables are fraktur ($\mathfrak{m}$ for mass, $\mathfrak{E}$ for
energy, $\mathfrak{Q}_\beta$ for the $\beta$-decay $Q$-value,
$\mathfrak{V}$ for the complex volume that packages binding and decay
together).

***

## Step 1 — The categorical action

Let $\mathcal{U} = (\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum
observable universe
([def:quantum-observable-universe](#def:quantum-observable-universe)): a
braided category $\mathbf{C}$, a twist endomorphism $\varTheta$, the internal
gauge group $G$, and the state bundle $\mathcal{S}$ that carries the physical
states.  The
:refterm[braided monoidal category]{#braided-monoidal-category} $\mathbf{C}$
has strands for objects and braid generators $\sigma_i$ for morphisms; the
braiding $c_{X,Y}\colon X \otimes Y \to Y \otimes X$ satisfies the
Yang–Baxter equation by the axioms of a
:refterm[braided monoidal category]{#braided-monoidal-category}.

Acting on the state bundle $\mathcal{S}$ through the fibre functor $\tau$ —
which sends an object to its underlying vector space, written $V$ for the
fundamental object — the category gives a representation of the braid group
on $n$ strands,

$$
  \rho_n \colon B_n \;\longrightarrow\; \mathrm{Aut}_\mathbf{C}(V^{\otimes n}),
$$

in which the generator $\sigma_i$ acts on strands $i$ and $i+1$ through the
$R$-matrix $R_{i,i+1}$
([prop:braid-action-tensor](#prop:braid-action-tensor)).  This categorical
action is the starting point; every later step is a consequence of the
structure of $\rho_n$.

***

## Step 2 — From holonomy to the Hecke relation

Yekutieli's multiplicative integration on surfaces provides the bridge from
the categorical action to an algebra we can compute in.  The $R$-matrix is
the parallel transport across a crossing; the Yang–Baxter relation is the
flatness of that transport.  Yekutieli's non-abelian Stokes theorem equates
the holonomy around the boundary of a 2-cell $\Sigma$ with the
surface-ordered product of the curvature over $\Sigma$,

$$
  \mathrm{Hol}(\partial\Sigma)
  \;=\; \overrightarrow{\textstyle\prod}\!\int_{\Sigma} F ,
$$

and the curvature 2-form on $V^{\otimes n}$ is exactly the Hecke quadratic
operator

$$
  F_{i,i+1} \;=\; R_{i,i+1}^2 - (q-q^{-1})\,R_{i,i+1} - 1 .
$$

Flatness $F_{i,i+1} = 0$ is therefore the Hecke relation

$$
  \sigma_i^2 \;=\; (q - q^{-1})\,\sigma_i + 1 ,
$$

forced by the $R$-matrix eigenvalues $q$ and $-q^{-1}$
([prop:hecke-spectral-sequence](#prop:hecke-spectral-sequence)).  The
quadratic relation is not an extra axiom; it is the curvature of the
substrate.  The dictionary between the 2-categorical datum and its
finite-slice avatar in $H_{n_0}(q)$ is recorded in
[Table 2](#tbl:pre-archimedean-derivation-chain-table2-data).

Writing $h = q - q^{-1}$ and $\eta = \ln q$, the eigenvalue $q$ splits as
$\cosh\eta + \sinh\eta$ and $q^{-1}$ as $\cosh\eta - \sinh\eta$
([prop:crossing-energy-decomposition](#prop:crossing-energy-decomposition)):
the symmetric $\cosh\eta$ part is the curvature-free transport, the
antisymmetric $\sinh\eta$ part is the curvature defect.  This split
returns at every later step — it is the difference between the strong
channel and the Coulomb channel, between binding and decay.

***

## Step 3 — Knots, braids, and the unique trace

Every oriented knot or link is the closure $\hat\beta$ of some braid
$\beta \in B_n$ (Alexander's theorem), and two closures give the same knot
exactly when the braids differ by conjugation (Markov move I) or by
stabilisation $\beta \mapsto \beta\sigma_n^{\pm1}$ (Markov move II).  Jones
proved that there is a **unique** trace
$\mathrm{tr}_M\colon \bigcup_n H_n(q) \to R$ invariant under both moves
([thm:jones-markov-trace](#thm:jones-markov-trace)).  This single fact ties
the topology to the algebra without ambiguity:

$$
  J_K(q) \;=\; \mathrm{tr}_M(T_w), \qquad
  T_w \in H_{n_0}(q)\ \text{the canonical braid closure of }K,
$$

where $J_K(q)$ is the Jones polynomial.  The mass invariant of a particle is
this trace evaluated at the substrate parameter.

***

## Step 4 — Why exactly six operators

The genus-four state space — Bring's surface $\Sigma_4$, with automorphism
group $S_5$ and Euler characteristic $\chi(\Sigma_4) = -6$ — fixes the
particle content.  The Descartes condition $\chi(A) = -6$ on the
Frobenius–Hopf algebra $A$ singles out the Hecke algebra $H_3(q)$, whose
dimension is exactly $6$.  Its six basis elements,

$$
  \{\,1,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ \gamma\,\},
$$

in Gröbner–Shirshov normal form
([prop:spectral-sequence-h3-explicit](#prop:spectral-sequence-h3-explicit)),
are the six independent crossing operators on $\Sigma_4$.  The
$x_5$-Bring weight identification
([prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification))
makes this concrete: the $\mathbb{Z}_5$ automorphism of the Bring curve acts
on the partitions $\lambda \vdash 3$ through a Prym decomposition, selecting
exactly the Wedderburn summands that label the nucleon mass formula.  There
is no seventh operator, and no free choice at this stage.

***

## Step 5 — Splitting the algebra into blocks

At generic $q$ the Iwahori–Hecke algebra is semisimple, and the Wedderburn
theorem splits it into matrix blocks indexed by Young diagrams:

$$
  H_n(q) \;\cong\; \bigoplus_{\lambda \,\vdash\, n}
    M_{d_\lambda}\!\bigl(\mathbb{Q}(q)\bigr),
  \qquad
  d_\lambda \;=\; \frac{n!}{\prod_{x\in\lambda} h_x},
$$

with $d_\lambda$ the number of standard Young tableaux of shape $\lambda$
(the hook-length formula); the quantum dimensions $\dim_q(\lambda)$ are its
$q$-analogue, given by the $q$-hook-length formula.  This block decomposition
is what makes the trace a finite sum.  Two algorithms supply its ingredients
explicitly:

- **Hoefsmit's seminormal representations** give the matrices of each
  generator $\sigma_i$ inside each block $\lambda$ in closed form, so the
  character $\chi_\lambda(\beta)$ of any braid word is a finite matrix
  product evaluated symbolically.
- **Wenzl's branching rule** supplies the unique central weights
  $y_\lambda(q)$ — one scalar per block — that assemble the per-block
  characters into the Markov trace,

$$
  \mathrm{tr}_M(\beta) \;=\; \sum_{\lambda \,\vdash\, n}
    y_\lambda(q)\,\chi_\lambda(\beta).
$$

The weights are not fitted: they are forced, since the linear system
$\sum_\lambda \chi_\lambda(w_\mu)\,y_\lambda = z^{\,n-\ell(\mu)}$ — with $z$
the Markov parameter set by the stabilisation move and $\ell(\mu)$ the Coxeter
word length (Step 7) — is invertible at generic $q$ by Schur–Weyl–Hecke
duality
([prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure)).
For a composite of several nucleons the trace multiplies block by block,
through Wenzl's disjoint-product property, so a multi-atom invariant is
built from single-nucleon pieces.

***

## Step 6 — The Frobenius integral and chirality

The Markov trace is the Frobenius integral $\int_A$ on the symmetric
Frobenius algebra structure of $H_n(q)$
([def:frobenius-hopf-substrate](#def:frobenius-hopf-substrate)), and the
Frobenius pairing $\langle a, b\rangle_F = \int_A(a\cdot b)$ is the inner
product on the algebra.  The Nakayama automorphism satisfies
$\Psi = S^2 = \mathrm{id}_A$ — the algebra is symmetric, since
$S(\sigma_i) = \sigma_i^{-1}$ — so the categorical mass of a hadron is the
absolute trace of its canonical braid,

$$
  \mathfrak{m}(\mathfrak{H})
  \;=\; \Bigl|\int_A \rho(\mathcal{B}_\mathfrak{H})\Bigr|
  \;=\; \bigl|\mathrm{tr}_M(T_w)\bigr|.
$$

The same self-pairing produces the chirality factor: a chiral knot of
writhe $w(K)$ carries a ribbon twist

$$
  a_K \;=\; 1 + w(K)\,h + O(h^2), \qquad h = q - q^{-1},
$$

from the Kauffman framing formula applied to the twist endomorphism
$\varTheta$ on irreducibles
([prop:chirality-writhe-ribbon-derivation](#prop:chirality-writhe-ribbon-derivation)).
On each block the boundary holonomy has eigenvalues $e^{\pm i\theta_\lambda}$
with $q$-Reeb phase $\theta_\lambda = \arccos(\chi_\lambda/d_\lambda)$
([prop:unit-modulus-eigenvalue](#prop:unit-modulus-eigenvalue)); the scalar
trace sums these phases away, which matters for binding (Step 9).

***

## Step 7 — Normal forms and the finite-slice guarantee

The Gröbner–Shirshov basis for $H_{n_0}(q)$ is the engine that makes the
trace mechanically computable
([prop:gb-spectral-sequence](#prop:gb-spectral-sequence)).  It rewrites
every braid word to a unique reduced representative, and grades the algebra
by Coxeter length,

$$
  F_k H_{n_0}(q) \;=\; \bigl\{\text{span of reduced words of length} \leq k\bigr\}.
$$

The associated graded forms a spectral sequence whose differentials encode
exactly the braid relations ($d_1$) and the Hecke quadratic relation
($d_2$); there are no further relations, so the sequence **collapses at
$E_2$**
([prop:spectral-sequence-collapse](#prop:spectral-sequence-collapse)) and
its limit recovers the Wedderburn decomposition
([prop:e-infinity-page-identifications](#prop:e-infinity-page-identifications)).
The consequence for computation is that a finite slice suffices: at
every finite grade the surviving classes already account for all of
$\mathrm{tr}_M(T_w)$, so no infinite tower of corrections contributes to the
mass invariant.

The block structure also tells us which algorithm to reach for.  Folding
the Cartan datum to Type B yields a symmetric crystal whose normal forms are
bar-invariant under $q \mapsto q^{-1}$ — the structural home of
matter–antimatter pairing, obtained without hand-written sign rules.
Decategorifying the same crystal to the Kazhdan–Lusztig basis of $S_n$
recovers ordinary statistics in the classical limit, and Demazure
subcrystals model the unstable resonances.  These crystal-basis techniques
are the combinatorial shortcuts behind the symbolic trace; they replace
ad-hoc bookkeeping with constructions whose algebraic guarantees are known
in advance.

***

## Step 8 — Jet order and the classical limit

The order in which the Gröbner–Shirshov reductions are applied is the jet
order — the temporal slice-traversal order of Yekutieli's picture, recorded
as (word, grade, jet-position) triples.  The jet tower converges to the
classical limit as $q \to 1$
([conj:jet-convergence-classical-limit](#conj:jet-convergence-classical-limit)),
confirming that the finite-slice computation is algebraically consistent
with the semiclassical approximation.

***

## Step 9 — Evaluating the trace as a mass

Up to here every quantity is a rational function of $q$.  The Archimedean
realization functor $\Phi_\mathrm{arch}$
([def:archimedean-realization-functor](#def:archimedean-realization-functor))
is the single point where the substrate becomes a real number: it evaluates
the invariant at $q = q_0$ and attaches the dimensional unit $m_e$.

The energy scale $\mathfrak{E}_0$ follows from the calibration.  From the
electron mass and $q_0$ alone,

$$
  \mathfrak{E}_0
  \;=\; \frac{m_e}{q_0(q_0 - 1)}
  \;=\; m_e\,c_q^2\,\hbar_q
  \;\approx\; 4.19\ \mathrm{MeV},
$$

and the same scale read from the $\beta$-decay $Q$-value through the
symbolic normal-form difference, $\mathfrak{E}_0 = \mathfrak{Q}_\beta /
|h(h-2)/2|$, agrees to within the brane-tower correction
([prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation)); here
$c_q = 1/(q-1)$ and $\hbar_q = 1 - q^{-1}$.  The categorical mass identity is
then

$$
  \boxed{\;
    \mathfrak{m}(\mathfrak{H})
    \;=\;
    m_e \cdot \varrho \cdot
    \bigl[\,|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) +
         \mathrm{tr}_M(C_{\dim_q})\,\bigr]\big|_{q = q_0}
  \;}
$$

where $\varrho \in \mathbb{Z}_{>0}$ is the multiplicity of the Wedderburn
solution selected in Step 10, $\mathrm{tower}(T_w)$ is the brane-tower
correction
([conj:brane-tower-z-habiro](#conj:brane-tower-z-habiro)), and
$\mathrm{tr}_M(C_{\dim_q})$ is the Frobenius co-Casimir trace
([thm:frobenius-codim-universal](#thm:frobenius-codim-universal)).  For the
absolute nucleon mass the canonical realization is the muon-anchored Hecke
energy, $\mathfrak{m}_{\mathfrak{p}} = 2\,(m_\mu F_\mathrm{Bor} - 6\,m_e)$
with $m_\mu = m_e\,\mathrm{Vol}(4_1)/\hbar_q^2$ (the figure-eight knot
volume) and $F_\mathrm{Bor}$ the dimensionless Borromean Hecke factor: the
single dimensionful factor $1/\hbar_q^2$ enters only through the muon anchor.

The trace identity has a **geometric face**.  Because the Markov trace grows
like the exponential of a hyperbolic volume — $\mathrm{tr}_M \sim
\exp(\mathrm{Vol})$, the volume conjecture in its $q$-deformed form — the same
mass is read directly off the knot's hyperbolic geometry.  For a hyperbolic
knot $K$ the mass is a volume times a density,

$$
  \mathfrak{m}(K) \;=\; m_e \cdot \mathrm{Vol}(K) \cdot \varrho(K) \,/\, \hbar_q^2,
$$

the electron scale times the hyperbolic volume $\mathrm{Vol}(K)$ times the
per-knot density $\varrho(K)$ — the same multiplicity $\varrho$ of the box
above, now read off the knot
([*$q$-Hyperbolic Geometry*](#chap:climax-volume-mass)).  The two faces — the
trace $|\mathrm{tr}_M(T_w)|$ and the volume–density product
$\mathrm{Vol}(K)\,\varrho(K)/\hbar_q^2$ — are the same quantity, exchanged by
the archimedean functor: the trace is its algebraic computation, the
volume–density product its geometric reading.  For the absolute nucleon mass
the muon-anchored form above stays canonical — applying $1/\hbar_q^2$ to the
Borromean volume directly mis-scales by a few percent — so the
volume–density product gives the per-knot *shape*, not the route to the
nucleon's absolute value.

The two parts of the trace carry the two physical observables of a nucleus
at once, packaged as a single **complex volume** $\mathfrak{V}$: its real
part is the binding energy, $\mathrm{Re}\,\mathfrak{V} =
\mathfrak{E}_\mathrm{bind}$, and its imaginary part is the $\beta$-decay
$Q$-value, $\mathrm{Im}\,\mathfrak{V} = \mathfrak{Q}_\beta$ — the
bar-even and bar-odd halves of the one geometric quantity, in the same
$\cosh$/$\sinh$ split that the crossing eigenvalues showed in Step 2.

***

## Step 10 — Selecting the canonical knot

Which braid $T_w$ represents a given confined particle is decided by a
**semidefinite program** over the Frobenius Gram matrix
([prop:confinement-sdp](#prop:confinement-sdp),
[prop:atom-knot-mass-derivation](#prop:atom-knot-mass-derivation)).  The
program minimises the Frobenius residual

$$
  \min_{T_w} \;\bigl\|
    \mathrm{tr}_M(T_w)\cdot\mathfrak{E}_0 - B_\mathrm{target}
  \bigr\|^2
  \quad\text{subject to}\quad
  T_w \in H_{n_0}(q_0)^{\text{GB-NF}}, \;\; \|T_w\| \leq \Delta_{\max},
$$

over Gröbner–Shirshov normal forms.  Its **dual** is the load-bearing
object: the shadow prices on the Frobenius positivity constraints identify
which Wedderburn blocks the bound state saturates, so the dual variables
are themselves the binding-energy structure rather than a by-product of the
solve.  The diagonal projection of the matrix program is the integer linear
program of the rank-one case, and strong duality makes the selected
operator unique.  The first-principles knot identification for the lightest
nuclei is an open problem
([conj:canonical-knot-id-sdp](#conj:canonical-knot-id-sdp)); the
identification for heavier nuclei extends through the recursive atom-knot
atlas.

***

## Step 11 — Decay widths and binding from the same trace

Once $\mathfrak{E}_0$ is fixed, $\beta$-decay is a difference of traces.  A
single quark-flavour crossing change $\mathfrak{d} \to \mathfrak{u}$ takes a
parent braid $T_w^\mathfrak{H}$ to a daughter $T_w^{\mathfrak{H}'}$, and the
$Q$-value is

$$
  \mathfrak{Q}_{\beta^-}(\mathfrak{H} \to \mathfrak{H}')
  \;=\;
  \bigl[\,\mathrm{net}(T_w^\mathfrak{H}) - \mathrm{net}(T_w^{\mathfrak{H}'})\,\bigr]
  \times \mathfrak{E}_0.
$$

The symbolic normal-form computation gives the free-neutron value with no
further calibration
([prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)):

$$
  \Delta(\mathrm{net})
  \;=\; \mathrm{net}(\mathfrak{n}) - \mathrm{net}(\mathfrak{p})
  \;=\; \tfrac{h(h-2)}{2}
  \;\approx\; -0.188,
$$

the bar-odd $\sinh$ partner of the bar-even meson scale.  The unweighted
$\mathrm{net}$ sum and the Markov-trace weighted mass tower are distinct
combinations of the same characters, so the relation
$\mathfrak{Q}_\beta = |\Delta(\mathrm{net})|\,\mathfrak{E}_0$ is a
cross-check on the calibration rather than a second derivation of the mass;
it reproduces the measured $Q$-value to better than one percent.  Every
other $Q$-value in the decay chain is a genuine prediction once
$\mathfrak{E}_0$ is fixed.

The same trace difference, evaluated on a free pair against a bound atom,
gives the binding energy.  At full $\mathrm{tr}_M$ level the per-$Z$ step
closes in one line.  The exact interface factor is
$\mathrm{tr}_M(\mathcal{B}_K)/\mathrm{tr}_M(\mathcal{B}_K^{\mathrm{vac}}) =
z^{p_+(K)}(z-h)^{p_-(K)}$, where $p_+(K)$ and $p_-(K)$ count the positive and
negative inter-nucleon interfaces
([prop:interface-knot-markov-z](#prop:interface-knot-markov-z)); combined
with the vacuum factor from Wenzl multiplicativity it gives

$$
  \frac{\mathrm{tr}_M(\mathcal{B}_K^{Z+1, N})}{\mathrm{tr}_M(\mathcal{B}_K^{Z, N})}
  \;=\; z(q)\cdot\mathrm{tr}_M^3(\mathcal{B}_\mathfrak{p}, q),
$$

with no residual
([prop:constit-factor-tau-M-proton-identity](#prop:constit-factor-tau-M-proton-identity)).
The deuteron binding follows from the single-bond trace difference; the
absolute binding of heavier nuclei is carried by the per-block $q$-Reeb
phases that the scalar trace suppresses, and assembling those phases into a
many-body sum over inter-nucleon bonds is the active frontier of the
construction.

***

## Summary

```tex
\begin{align*}
\text{categorical action } \rho_n
  &\xrightarrow{\ \text{Yekutieli}\ } H_{n_0}(q),\quad \sigma_i^2 = (q-q^{-1})\sigma_i + 1 \\
  &\xrightarrow{\ \text{SDP} + \text{GB-NF}\ } T_w \in H_{n_0}(q_0) \\
  &\xrightarrow{\ \text{Wedderburn}\ } \bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q)) \\
  &\xrightarrow{\ \text{Hoefsmit} + \text{Wenzl}\ } \mathrm{tr}_M(T_w) = \sum_\lambda y_\lambda\,\chi_\lambda(T_w) \\
  &\xrightarrow{\ \Phi_\mathrm{arch}\,\times\, m_e\ } \mathfrak{m}(\mathfrak{H}) \quad \text{in MeV.}
\end{align*}
```

Each arrow is algebraic, living in $\mathbb{Q}(q)$ until the Archimedean
functor; the eleven steps together carry three measured proxies into the
full spectrum of nuclear masses, binding energies, and decay widths.
