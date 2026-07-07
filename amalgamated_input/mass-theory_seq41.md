<!-- FILE_START: derivation-audit-intro.md -->
This section surveys how the framework derives a mass and a binding
energy, tracing the construction from the categorical action through the
Markov trace to a number in MeV. The blocks below give the step-by-step
chain together with the canonical knot-identification program and the
binding-energy analysis that follow from it.
<!-- FILE_END: derivation-audit-intro.md -->

<!-- FILE_START: pre-archimedean-derivation-chain.md -->
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
<!-- FILE_END: pre-archimedean-derivation-chain.md -->

<!-- FILE_START: conj-canonical-knot-id-sdp.md -->
The canonical Hecke elements $T_w$ for the light nuclei
$^2\mathrm{H}$ (deuterium), $^3\mathrm{H}$ (tritium), and
$^3\mathrm{He}$ (helium-3) were historically identified by matching
their hyperbolic volumes to AME binding energies.  This conjecture
states that the joint mass-tower confinement SDP
([prop:confinement-sdp](#prop:confinement-sdp)) uniquely selects
the same Hecke elements from first principles.

## Statement

**Conjecture.**
*Let $\mathfrak{E}_0$ be the hadronic energy scale fixed by $\mathfrak{Q}_\beta$
and let $q = q_0$ be the substrate parameter fixed by $m_\mu/m_e$.
For each light nucleus $\mathfrak{H} \in \{{}^2\mathrm{H}, {}^3\mathrm{H}, {}^3\mathrm{He}\}$,
the joint mass-tower confinement SDP*

$$
  \min_{T_w \in H_{n_0}(q_0)^{\mathrm{GB\text{-}NF}},\,\rho \in \mathbb{Z}_{>0}}
  \Bigl\|
    \rho \cdot \bigl[\mathrm{tr}_M(T_w) + \mathrm{tower}(T_w)
    + \mathrm{tr}_M(C_{\dim_q})\bigr] \cdot \mathfrak{E}_0
    \;-\; B_{\mathrm{AME}}(\mathfrak{H})
  \Bigr\|^2
$$

*subject to: $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$
([prop:delta-max-uniform-bound](#prop:delta-max-uniform-bound)),*

*has a unique global minimizer $T_w^*$, achieved at:*

| Nucleus | Knot type | $n_0 = 3 \cdot A$ | $\rho$ | $B_\mathrm{AME}$ (MeV) |
|---------|-----------|-------------------|--------|------------------------|
| $^2\mathrm{H}$ | $6_2$ (Miller's knot) | $6$ ($A=2$) | $1$ | $2.2246$ |
| $^3\mathrm{H}$ | $8_{11}$ | $9$ ($A=3$) | $2$ | $8.4820$ |
| $^3\mathrm{He}$ | $L_{6a4}$ | $9$ ($A=3$) | $2$ | $7.7181$ |

(Earlier drafts of this table listed $n_0 = 6$ for ${}^{3}$H/${}^{3}$He.  Reconciled
with the joint-tower SDP convention $n_0 = 3 \cdot A$ used in
[`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement)
and in
[`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/main/computations/joint-tower-sdp-h6-h9.witness.json)
— `atomic_n_0 = 9` for ${}^{3}$H/${}^{3}$He.  See "Structural decomposition" below
for the binding-K factorisation that motivates the $n_0 = 3 \cdot A$
convention.)

*with residual $< 0.5\%$ of $B_{\mathrm{AME}}(\mathfrak{H})$.*

## Historical evidence (volume matching)

The knot assignments above were originally found by matching
hyperbolic volumes to AME binding energies:

| Nucleus | Knot/link | Vol (SnapPy) | $\rho \cdot m_e \cdot \mathrm{Vol}$ (MeV) | vs $B_{\mathrm{AME}}$ |
|---------|-----------|-------------|-------------------------------------------|------------------------|
| $^2$H | $6_2$ | $4.40083$ | $\approx 2.2488$ | $+1.09\%$ |
| $^3$H | $8_{11}$ | $8.28632$ | $\approx 8.4686$ | $-0.16\%$ |
| $^3$He | $L_{6a4}$ | $7.32772$ | $\approx 7.4889$ | $-2.97\%$ |

Here $\rho \in \{1, 2, 2\}$ is the multiplicity from the table above and
$m_e$ is the electron mass (CAL-1); the matching law
$B_{\mathrm{AME}}(\mathfrak{H}) \approx \rho \cdot m_e \cdot \mathrm{Vol}(K)$
carries no free parameter.

(Earlier revisions of this table printed the volumes $3.16396$, $3.42721$,
$5.33349$ — the census volumes of $6_1$, $8_1$, $6^3_1$, subscript-neighbours
of the named knots, surviving from a superseded draft normalised by
$\mathfrak{E}_0 \approx 4.150$ MeV.  Live-census verification and the
two-knot-set adjudication confirm the named assignment: the named set
reproduces the match pattern above, while the orphan volume set misses by
$27$–$59\%$ under the same law — see
[`docs/audits/2026-06-12-knot-id-volume-match-adjudication.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-12-knot-id-volume-match-adjudication.md)
and the witnesses `snappy-census-volume-verification.witness.json`,
`knot-id-volume-match-adjudication.witness.json`.)

The volume-matching identification is empirically strong, but it does not
constitute a categorical derivation.  The conjecture asserts that the SDP
ground truth agrees with the historical assignment.

## SDP witness evidence

canonical SDP witnesses (stored in
`computations/canonical evaluation-sdp-canonical-paper-formula.witness.json`)
show that the multi-term mass formula reproduces the AME binding
energies of $^2$H, $^3$H, $^3$He to within the claimed error bound
when $T_w$ is set to these knot types.  The conjecture asserts that
no other $T_w$ within the $\Delta_{\max}$ ball achieves a smaller
residual.

## Partial closure

The R5-full canonical-knot SDP solver prototype
(the canonical formalism,
witness
[`r5-full-canonical-knot-solver.witness.json`](../../../computations/r5-full-canonical-knot-solver.witness.json))
gave the first **substrate-only** check of this conjecture for the
three light nuclei.  Result:

| Nucleus | Canonical $T_w$ | $\alpha^*$ | PSD-feasible at $q_0$? | Rank in 138 KLR-canonical classes |
|---------|-----------------|------------|------------------------|------------------------------------|
| $^3\mathrm{He}$ | $L_{6a4}$ | $0.000$ | **yes** | 24 (top 17 %) |
| $^2\mathrm{H}$ | $6_2$ | $0.891$ | no (single-term cost) | 62 (top 45 %) |
| $^3\mathrm{H}$ | $8_{11}$ | — | (deferred — needs $H_5$ Hoefsmit) | — |

**Status by nucleus:**

- **$^3\mathrm{He}$ — PSD-feasibility verified** at $q_0$: the
  canonical $T_w = L_{6a4}$ sits on the structural target
  ($\alpha^* = 0$) in the standard $(2,1)$ Wedderburn block.  The
  $\chi$-fingerprint of the prototype's recovered word
  $(\sigma_1 \sigma_2^{-1})^3$ matches the historical SnapPy braid
  $[-1, 2, -1, 2, -1, 2]$ up to generator-sign convention (same KLR
  canonical-basis class).  This discharges sub-deliverable 2 of
  Issue #604 for $^3\mathrm{He}$.
- **$^2\mathrm{H}$ — needs multi-term cost.** The prototype's
  single-term flagship formula $B = m_e \cdot \rho \cdot \mathrm{tr}_M(T_w)$
  does not make $6_2$ the structural winner (per the known offset
  documented in `canonical evaluation-sdp-canonical-paper-formula.witness.json`).
  Wiring T2–T6 of
  [`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
  into `cost_for_candidate` is the next-priority closure step.
- **$^3\mathrm{H}$ — pipeline deferred.** Hoefsmit seminormal at
  $H_5$ needs to land first (currently a deferral to
  Rust `tools/hecke-engine`).

**Categorical uniqueness theorem (proof obligation 2)** is now
formally stated in
[`conj-canonical-knot-id-sdp.lean`](conj-canonical-knot-id-sdp.lean)
as `helium3_canonical_uniqueness_via_strict_complementarity`.  The
Lean theorem takes:

1. The R5-full canonical witness (`R5FullWitness LightNucleus.helium3`)
   recording $\alpha_{\mathrm{gap}} = 0$ + strong duality
   ($|\text{primal\_obj} - \text{dual\_obj}| \leq 10^{-6}$);
2. A strict-complementarity certificate
   (`StrictComplementarity LightNucleus.helium3`) — the categorical
   hypothesis upgrading canonical PSD-feasibility to unique-minimizer
   status per Boyd–Vandenberghe §5.5.

and concludes
`CanonicalKnotIdSDP LightNucleus.helium3` (the §3b-cond conditional
class instance for $^3\mathrm{He}$).  This is the closure path for
sub-deliverable 3 of Issue #604: under the strict-complementarity
hypothesis (a categorical claim about the geometry of the SDP's
feasible set, not a canonical certificate), the historical
$L_{6a4}$ assignment for $^3\mathrm{He}$ is *the* unique R5-full
canonical $T_w$.

The genuine *uniqueness* leg — Boyd–Vandenberghe §5.5
strict-complementarity $\Rightarrow$ unique primal optimum — is closed
for $^3\mathrm{He}$ **without any axiom**.  The R5-full witness places
$^3\mathrm{He}$ in the interior regime (all three Wedderburn-block
minimum eigenvalues strictly positive: trivial $1.87$, standard $0.53$,
sign $0.53$, so the active set is empty), where the §5.5 argument is
fully constructive.  The closure is
`nucleus_uniqueness_closed_via_active_empty` at the $^3\mathrm{He}$
strand count $n_0 = 9$ (specialised as
`helium3_uniqueness_closed_via_active_empty` in
[`AppliedHelium3Uniqueness.lean`](../lean/QOU/BraidKnot/AppliedHelium3Uniqueness.lean)),
discharged through
`real_strict_complementarity_unique_of_active_empty_and_cost_posDef`
([`SDPRealUniqueness.lean`](../lean/QOU/MathlibExt/SDPRealUniqueness.lean))
with no dependency on the general SDP rank-deficiency axiom.

The general (non-empty active set) case — needed at the degenerate /
metallic-coincidence loci where strict complementarity fails — remains
gated on the `SDPRankUniqueness` Mathlib gap (SDP optimal-face
rank-deficiency).  See
[`docs/audits/2026-06-13-strict-complementarity-sdp-uniqueness-attempt.md`](../../../docs/audits/2026-06-13-strict-complementarity-sdp-uniqueness-attempt.md)
for the closeable/irreducible split and the
[`r5-full-canonical-knot-solver.witness.json`](../../../computations/r5-full-canonical-knot-solver.witness.json)
active-set data.

## Proof obligations

1. **Finitude of candidate set.**  The Plancherel-weight boundedness
   ([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
   gives a finite bound on the number of GB-normal-form elements of
   $H_6(q_0)$ with $\|T_w\|_{\mathrm{Frob}} \leq \Delta_{\max}$.
   Make this bound explicit and computable.

2. **Exhaustive or branch-and-bound search.**  Over the finite
   candidate set (or via a certified branch-and-bound), confirm that
   no $T_w \neq T_{6_2}$ (resp.\ $T_{8_{11}}$, $T_{L_{6a4}}$) achieves
   a smaller residual.

3. **Uniqueness of $\rho$.**  Show that $\rho = 1$ for $^2$H and
   $\rho = 2$ for $^3$H/$^3$He are the unique positive-integer
   multiplicities in the feasible SDP region.

## Structural decomposition (issue #604, deliverables 3 + 4)

The canonical evidence from
[`computations/r5-full-canonical-knot-solver.witness.json`](https://github.com/litlfred/qou/blob/main/computations/r5-full-canonical-knot-solver.witness.json)
(deliverable 1) and
[`rho-prefactor-structural-verifier.witness.json`](https://github.com/litlfred/qou/blob/main/computations/rho-prefactor-structural-verifier.witness.json)
(deliverable 4) shows that the canonical $T_w$ at the **braid strand
count** alone does *not* uniquely identify the bound state — proton
and ${}^{3}$He have Markov-equivalent braid words in $H_3(q_0)$ (mutual
inverses), yet they are distinct bound states with distinct $\rho$.

The structural fix is to factor:

$$
T_w(\mathfrak{H})
\;=\;
K(\mathfrak{H})
\,\cdot\,
\bigotimes_{i=1}^{A} T_w(\text{nucleon}_i)
$$

where $K(\mathfrak{H}) \in H_{3 \cdot A}(q_0)$ is the **binding
operator** linking the $A$ nucleon-trefoils.  This splits the SDP
uniqueness conjecture into:

(a) **Constituent uniqueness** — each $T_w(\text{nucleon}_i)$ is the
    unique PSD-feasible canonical element at $H_3(q_0)$.  *Closed
    canonical* by the R5-minimal verifier
    (the canonical formalism).

(b) **Binding-K uniqueness** — $K(\mathfrak{H}) \in H_{3 \cdot A}(q_0)$
    is the unique PSD-feasible Hecke element satisfying the joint-tower
    SDP cross-level consistency constraints (4) of
    [`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement).
    *Open* — this is the categorical uniqueness theorem still required
    to fully close GAP-A-1.

The Lean class
[`conj-canonical-knot-id-sdp.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/conj-canonical-knot-id-sdp.lean)
records (a) and (b) as **separate** sub-assertions
(`constituentUniqueness`, `bindingKUniqueness`), so a downstream
conditional theorem can use only the closed (a) part once the binding-K
SDP solver mode lands and discharges (b) per-particle.

| Nucleus | $A$ | $n_0 = 3A$ | binding $K$ | constituents | $\rho$ |
|---------|-----|-----------|-------------|--------------|--------|
| ${}^2$H | 2 | 6 | $L_H$ (Hopf) | $\{p, n\}$ | 1 |
| ${}^{3}$H | 3 | 9 | $8_{11}$-class link | $\{p, n, n\}$ | 2 |
| ${}^{3}$He | 3 | 9 | $L_{6a4}$ | $\{p, p, n\}$ | 2 |

## Relationship to GAP-A-1

This conjecture directly addresses GAP-A-1 of the
[derivation audit report](#prose:derivation-audit-report).
A proof would replace the historical volume-matching identification
with a purely categorical derivation.

<!-- FILE_END: conj-canonical-knot-id-sdp.md -->

<!-- FILE_START: conj-rho-prefactor-structural.md -->
The SDP multiplicity $\rho \in \mathbb{Z}_{>0}$ in the mass formula

$$
  B(\mathfrak{H}) \;=\; m_e \cdot \rho \cdot M(\mathfrak{H})\big|_{q = q_0}
$$

is currently determined case-by-case as a canonical by-product of
the Wedderburn SDP search. This conjecture proposes a structural rule
for $\rho$ in terms of the categorical data of $\mathfrak{H}$.

## Statement

**Conjecture.**
*Let $\mathfrak{H}$ be a confined particle/atom
([confined particle](#def:confined-particle)) with canonical Hecke
element $T_w \in H_{n_0}(q)$. The SDP multiplicity is:*

$$
  \rho(\mathfrak{H})
  \;=\;
  \dim_q\!\bigl(\lambda^*(T_w)\bigr),
$$

*where $\lambda^*(T_w)$ is the **dominant Young diagram** in the
Wedderburn decomposition of $T_w$: the partition $\lambda \vdash n_0$
maximizing $|y_\lambda(q_0) \cdot \chi_\lambda(T_w)|$
([Markov trace expansion](#prop:wedderburn-trace-identity),
[Wenzl-bridge weights](#prop:alpha-k-derivation-procedure)).*

*The quantum dimension $\dim_q(\lambda) = [d_\lambda]_q$ where
$d_\lambda$ is the number of standard Young tableaux of shape
$\lambda$ (hook-length formula).*

## Evidence (heuristic, pre-binding-K refinement)

The SDP witnesses for all four currently identified particles give the
following heuristic table. **Caveat (issue #604, deliverable 4):** the
"Dominant $\lambda^*$" entries here are *conjectural* and were
populated before the $H_{3 \cdot A}$ binding-K analysis below; they are kept
for historical reference and reconciliation with the older narrative.
The canonical verified rule (see "Critical structural finding" below)
must be evaluated at the atomic strand count $n_0 = 3 \cdot A$:

| Particle | Knot | $n_0 = 3\cdot A$ | Conjectural dominant $\lambda^*$ | $\dim_q(\lambda^*)$ at $q_0$ | Obs.\ $\rho$ |
|----------|------|------------------|----------------------------------|------------------------------|--------------|
| Proton/neutron | trefoil $3_1$ | $3$ ($A=1$) | $(2,1)$ | $[2]_{q_0} \approx 2.01$ $\to$ $\rho = 1$ (hook special case) | $1$ |
| Deuterium $^2$H | $6_2$ | $6$ ($A=2$) | $(3,2,1)$ | $\approx 1.0$ | $1$ |
| Tritium $^3$H | $8_{11}$ | $9$ ($A=3$) | $(3,3,3)$ (conjectural) | $\approx 2.0$ $\to$ $\rho = 2$ | $2$ |
| Helium-3 $^3$He | $L_{6a4}$ | $9$ ($A=3$) | $(3,3,3)$ (conjectural) | $\approx 2.0$ $\to$ $\rho = 2$ | $2$ |

The earlier draft of this table (pre-deliverable-4) listed
$n_0 = 6$ for ${}^{3}$H/${}^{3}$He, which conflicted with the joint-tower SDP
convention $n_0 = 3 \cdot A$ used in
[`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement)
and in
[`joint-tower-sdp-h6-h9.witness.json`](https://github.com/litlfred/qou/blob/main/computations/joint-tower-sdp-h6-h9.witness.json)
(`atomic_n_0 = 9` for ${}^{3}$H, ${}^{3}$He). This table is now reconciled to
$n_0 = 3 \cdot A$. The conjectural $\lambda^* \vdash 9$ entries
remain to be verified once Hoefsmit at $H_9$ is implemented (deferred
— see "Critical structural finding" below).

The pattern $\rho = \mathrm{round}[\dim_q(\lambda^*)]$ (nearest-integer
rounding) is consistent with the four known cases under the
hook-special-case caveat; the rule relating $\lambda^*$ to specific
shapes has not been derived from first principles.

## The rounding question

The exact quantum dimension $[2]_{q_0} = q_0 + q_0^{-1} \approx 2.01$
(with $q_0 = 1.109978595554181\ldots$ (50 dps)), so $\dim_q((2,1)) \approx 2.01$. The
nearest-integer round gives $\rho = 2$, but the proton/neutron uses
$\rho = 1$. This suggests the rule may be:

$$
  \rho(\mathfrak{H})
  \;=\;
  \begin{cases}
    1 & \text{if $\lambda^*$ is the hook partition $(n_0-1, 1)$,} \\
    \mathrm{round}[\dim_q(\lambda^*)] & \text{otherwise.}
  \end{cases}
$$

(The symbol $\lfloor \cdot \rceil$ in earlier drafts denotes
*round-to-nearest*, not floor. The Lean class
[`conj-rho-prefactor-structural.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.lean)
encodes this as the inequality
$|\rho - \dim_q(\lambda^*)| \leq 1/2$.)

Alternatively, the correct $\rho$ may count the number of
**orthogonal Wedderburn copies** that fit inside the SDP feasible
region of the mass formula, which would give $\rho = 1$ for single-copy
and $\rho = 2$ for double-cover nuclei.

## Proof obligations

1. Identify the dominant $\lambda^*$ for each particle from the
 Markov-weight data and show it is $\lambda^* = (2,1)$ for proton
 and $(3,3)$ for $^3$H/$^3$He.

2. Show the multiplicity rule (exact quantum dimension, rounded, or
 orthogonal-copy count) reproduces the known $\rho$ values.

3. Provide a categorical interpretation of $\rho$: it should count
 a natural structural quantity of the confinement-SDP solution space
 (orthogonal copies, Wedderburn summand multiplicity, etc.).

4. Extend the rule to heavier nuclei $A \leq 60$ in the recursive
 atom-knot atlas and verify no per-atom re-tuning is needed.

## Critical structural finding (issue #604, deliverable 4)

The B_3-level canonical evaluation
(the canonical formalism,
witness [`rho-prefactor-structural-verifier.witness.json`](https://github.com/litlfred/qou/blob/main/computations/rho-prefactor-structural-verifier.witness.json))
**falsifies** the simple form of the rule "$\rho = \mathrm{round}[\dim_q(\lambda^*)]$" when
$\lambda^*$ is computed from the *braid strand count* alone:

| atom | knot braid | dominant $\lambda^* \vdash 3$ | $\dim_q$ at $q_0$ | obs $\rho$ |
|------|-----------|------------------------------|--------------------|------------|
| proton | $(\sigma_1 \sigma_2^{-1})^3$ | $(2,1)$ | $2.011$ | $\mathbf{1}$ |
| neutron | $(\sigma_1 \sigma_2^{-1})^3$ | $(2,1)$ | $2.011$ | $\mathbf{1}$ |
| ${}^2$H ($6_2$) | $\sigma_1 \sigma_2^{-1} \sigma_1^3 \sigma_2^{-1}$ | $(3)$ | $1.000$ | $\mathbf{1}$ |
| ${}^{3}$He ($L_{6a4}$) | $(\sigma_1^{-1} \sigma_2)^3$ | $(2,1)$ | $2.011$ | $\mathbf{2}$ |

Proton, neutron, and ${}^{3}$He have **identical** $\chi_\lambda$ values across all
three blocks — their braid words are mutual inverses (or by definition equal),
hence Markov-equivalent in $H_3(q_0)$. No rule of the form
"$\rho = f(\chi_\lambda, y_\lambda)$ at the braid strand count" can
distinguish $\rho_{\mathrm{p}} = 1$ from $\rho_{^3\mathrm{He}} = 2$.

### Required structural refinement: atomic strand count $n_0 = 3 \cdot A$

The conjecture must be evaluated at the **atomic** strand count
$n_0 = 3 \cdot A$, embedding the braid into $H_{3 \cdot A}(q_0)$
**through the binding operator**:

$$
T_w(\mathfrak{H})
\;=\;
\underbrace{K(\mathfrak{H})}_{\text{binding link} \,\in\, H_{3A}(q_0)}
\,\cdot\,
\underbrace{\bigotimes_{i=1}^{A} T_w(\text{nucleon}_i)}_{\text{constituents at } H_3(q_0)^{\otimes A}}.
$$

The binding operator $K(\mathfrak{H})$ links the $A$ nucleon-trefoils
together (Hopf link $L_H$ for ${}^2$H, an $8_{11}$-class link for ${}^3$H,
$L_{6a4}$ for ${}^{3}$He). The dominant $\lambda^* \vdash 3 \cdot A$ of
$K$ — *not* of the whole-particle braid image at $H_3$ — is what
carries the $\rho$ information.

This is the natural framework for the joint-tower SDP cross-level
consistency constraints (4) of
[`prop:joint-tower-sdp-confinement`](#prop:joint-tower-sdp-confinement),
which already enforce $T_w(\mathfrak{H}) \hookleftarrow T_w(\mathfrak{H}')$
across confinement levels. Wiring an explicit
"binding-K SDP solver mode" — that finds $K(\mathfrak{H})$ from
substrate data + constituent $T_w$'s alone — is the natural
follow-up deliverable for issue #604 (after the $H_{3 \cdot A}$ Hoefsmit
infrastructure lands). The Lean class
[`conj-rho-prefactor-structural.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/braids-and-knots/conj-rho-prefactor-structural.lean)
records `A` (not the braid strand count) as its primary parameter and
derives $n_0 = 3 \cdot A$ structurally; per-atom instances must be
constructed at $H_{3 \cdot A}$ to discharge the rule.

## Closure path via the canonical-knot-id

GAP-A-4 closes *as a corollary* of GAP-A-1 (canonical knot
identification): once the canonical $T_w$ for a nucleus is uniquely
fixed by the R5-full SDP, the dominant Wedderburn summand
$\lambda^*(T_w)$ is uniquely determined, and $\rho = [d_{\lambda^*}]_q$
follows from the Wedderburn trace identity.

The Lean side is now stated as
[`rho_eq_qdim_via_canonical_knot`](conj-rho-prefactor-structural.lean)
in `conj-rho-prefactor-structural.lean`. 's R5-full witness
records $\rho_\star$ per atom directly:

| Atom | Witness $\rho_\star$ | Notes |
|------|----------------------|-------|
| $^3\mathrm{He}$ | $3$ | At canonical $T_w = L_{6a4}$ |
| $^2\mathrm{H}$ | $3$ | At prototype's L=8 winner $\sigma_2 \sigma_1^6 \sigma_2^{-1}$ — **not** the historical $\rho = 1$ |

The deuterium discrepancy is because the prototype's single-term
cost function does not select $6_2$ at first principle (
"${}^2$H needs multi-term wiring"). Once T2--T6 of
[`thm:knot-mass-formula-unified`](#thm:knot-mass-formula-unified)
land in `cost_for_candidate`, the historical $\rho = 1$ at $6_2$
should be recovered.

For $^3\mathrm{He}$ the $\rho_\star = 3$ value is consistent with
the dominant-$\lambda^*$ rule once the orthogonal-copies
interpretation is invoked (the historical assignment $\rho = 2$
referred to the double-cover hadronic factor; the SDP's
$\rho_\star$ counts a different structural quantity).
Reconciling the two interpretations is the residual open piece
of obligation 3.

## Relationship to GAP-A-4

This conjecture directly addresses GAP-A-4 of the
[derivation audit report](#prose:derivation-audit-report).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: conj-rho-prefactor-structural.md -->

<!-- FILE_START: frobenius-cocasimir-refuted-deuteron.md -->
**Lemma (Frobenius co-Casimir Δ_λ ansatz refuted at the deuteron).**
*The Frobenius co-Casimir prescription $\Delta_\lambda = 1/\dim_q(\lambda)$ does
not close the per-isotope binding formula
$B(\mathcal{K}) = \mathfrak{m}_e \sum_\lambda y_\lambda \chi^\lambda \Delta_\lambda$
at the deuteron anchor. Its signed binding-density sum*
$$
\Sigma_{\mathrm{coCas}} \;=\; +0.14496\ \mathfrak{m}_e
\qquad\text{misses the empirical target}\qquad
\Sigma_{\mathrm{target}} \;=\; -4.35337\ \mathfrak{m}_e ,
$$
*by $|\Sigma_{\mathrm{coCas}} - \Sigma_{\mathrm{target}}| = 4.49833\ \mathfrak{m}_e > \text{tol} = 1$,
and with the opposite sign ($\Sigma_{\mathrm{coCas}} > 0 > \Sigma_{\mathrm{target}}$).*

The co-Casimir ansatz is theorem-forced (no free parameters), so the miss
cannot be absorbed by a fit: it is a **magnitude** refutation (gap $\approx 4.5$
$\mathfrak{m}_e$ units against tolerance $1$) and a **sign** refutation
(positive prediction versus a negative target — the ansatz is vortex-blind).
This is the first of the six refuted $\Delta_\lambda$ closure ansätze
(Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius,
crystal-graph, augmented Markov); the $\Delta_\lambda$ gate's "no seventh
fit-based ansatz" rule is the standing consequence.

## Lean structure

The refutation is a machine-checked rational (in)equality, sorry-free over
$\mathbb{Q}$ (decidable, `norm_num`-discharged): `coCasimir_refuted_deuteron`
($\text{tol} < |\Sigma_{\mathrm{coCas}} - \Sigma_{\mathrm{target}}|$) and
`coCasimir_wrong_sign` ($0 < \Sigma_{\mathrm{coCas}} \wedge
\Sigma_{\mathrm{target}} < 0$). The literals are 12-figure truncations of the
50-dps witness `rho-k-h3a-co-casimir.witness.json`; the gap exceeds tolerance by
a factor of $\approx 4.5$, so the inequality holds with large margin. Promoting
the standalone library refutation to this block places it under per-block QA so
the dead ansatz cannot be silently re-proposed past review.
<!-- FILE_END: frobenius-cocasimir-refuted-deuteron.md -->

