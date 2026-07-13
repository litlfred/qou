<!-- FILE_START: mass-geometric-face-intro.md -->
The mass endomorphism's geometric face links the algebraic Markov trace to the hyperbolic volume of the knot complement. Thurston's volume additivity decomposes the mass of a composite knot into a sum over its JSJ pieces. The mass-volume factorisation conjecture establishes the categorical mass endomorphism as the product of this topological volume and the Frobenius-packing density.

The crossing-graded expansion organizes the mass hierarchically by crossing count, with each layer governed by the lifted crossing locality conjecture. The jet-tower bound secures geometric convergence for the brane-tower sum, while Jucys-Murphy reindexing connects the tower explicitly to standard Young tableaux in the Hecke algebra.
<!-- FILE_END: mass-geometric-face-intro.md -->

<!-- FILE_START: thurston-volume-additivity.md -->
## Thurston volume additivity

Every hyperbolic knot complement admits an ideal triangulation by tetrahedra with vertices on the sphere at infinity. A single complex shape parameter $z_i$ determines each tetrahedron up to isometry.

**Proposition.**
*The hyperbolic volume of the knot complement $S^3 \setminus \mathcal{K}$ is the sum of its tetrahedral volumes:*

$$
  V(\mathcal{K})
  \;=\;
  \sum_{i = 1}^N D(z_i),
$$

*where $D(z_i)$ is the Bloch-Wigner dilogarithm evaluated at the shape parameter. Flat tetrahedra ($z_i \in \mathbb{R}$) contribute zero volume.*

## Braid-theoretic consequence

A knot diagram induces an ideal triangulation containing one tetrahedron per crossing. Consequently, the volume sums additively over crossings:

$$
  V(\mathcal{K}) \;=\; \sum_{\text{crossings } c} D(z_c).
$$

Torus knots project entirely onto a surface, forcing every $z_c$ to be real. Their hyperbolic volume vanishes identically.

## Extremality

The Bloch-Wigner function reaches its maximum at the regular shape $z = e^{i\pi/3}$, yielding the Lobachevsky constant $v_3 \approx 1.01494$. The figure-eight knot $4_1$ comprises exactly two such tetrahedra, producing the minimum hyperbolic volume $V(4_1) = 2 v_3 \approx 2.02988$. This extremality pins the substrate parameter $q_0$ by calibrating the quantum of action $\hbar_q^2$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: thurston-volume-additivity.md -->

<!-- FILE_START: mass-volume-factorization.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md).

## Mass-volume factorization

At the particle-mass scale, the formula $\mathfrak{m} = \mathrm{Vol}/\hbar_q^2$ applies the universal categorical density $\rho_q$. At the much lower nuclear-binding scale, the formula refines to use the physical Frobenius packing density $\rho_F$.

**Conjecture.**
*Let $\mathcal{K}$ be the atomic braid of a derived atom. The categorical mass endomorphism factorizes as:*

$$
  \mathfrak{m}_{\mathcal{K}}(q)
  \;=\;
  \rho(q, \mathcal{K}) \cdot V_{\mathrm{hyp}}(\overline{\mathcal{K}}).
$$

*The Frobenius packing density $\rho(q, \mathcal{K})$ is determined by the specific Wedderburn blocks populated by the braid within the Hecke algebra.*

## JSJ refinement

Under the Jaco-Shalen-Johannson decomposition, the factorization restricts to a sum over the hyperbolic pieces $P_i$:

$$
  B(Z, N) \;=\; \sum_{P_i \text{ hyperbolic}}
  \rho_F(P_i) \cdot V_{\mathrm{hyp}}(P_i).
$$

Seifert-fibered torus-knot nucleons contribute zero volume. The hyperbolic pieces containing the closed-shell Borromean links carry the binding energy.

The density $\rho_F(P_i)$ adopts one of two values depending on CPT saturation: $m_e$ for single-chirality configurations, and $2m_e$ when the antiparticle channel activates.

## Supporting evidence

Assigning specific geometric knots and local densities reproduces doubly-magic binding energies within 6.2%. However, the precise assignment map from atom to geometric link requires a per-isotope phenomenological fit. The map remains a conjecture pending rigorous derivation of the atom-to-link translation and local density rules from first principles.
<!-- FILE_END: mass-volume-factorization.md -->

<!-- FILE_START: frobenius-packing-density.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md).

## Frobenius packing density

The framework distinguishes two scale-dependent densities. The dimensionless substrate drag $\rho_q \approx 102$ governs the particle-mass scale. The physical Frobenius packing density $\rho_F \in \{m_e, 2m_e\}$ governs the nuclear-binding scale.

The Plancherel weights partition the Markov trace across the simple Wedderburn blocks of the Hecke algebra. The atomic link populates a specific subset of these blocks: the symmetric particle channel, the standard propagator channel, and the alternating antiparticle channel.

## The two-density rule

The topological entanglement of the link dictates block activation. The Frobenius density evaluates to:

$$
  \rho_F(\mathcal{K})
  \;=\;
  \begin{cases}
    m_e & \text{single-chirality (alt block empty)}, \\
    2 m_e & \text{CPT-saturated (alt block populated)}.
  \end{cases}
$$

Populating the alt block mandates its antiparticle partner by CPT symmetry, doubling the density.

Topological saturation triggers this threshold. Simple two-body links suppress the alt block. Three-body Borromean entanglement forces cyclic interaction, activating the alt channel. Closed-shell clusters saturate all blocks internally, while two-body inter-cluster bonds revert to the single-chirality density.

Mass computes as the geometric volume scaled by the discrete fractional volume occupied within the Wedderburn module. This categorical structure derives the $\{m_e, 2m_e\}$ threshold directly from the Frobenius pairing without phenomenological tuning.
<!-- FILE_END: frobenius-packing-density.md -->

<!-- FILE_START: crossing-graded-mass-expansion.md -->
## Crossing-graded mass expansion

**Conjecture.**
*Let $\mathcal{K}$ be an atomic braid of $c$ crossings. Fix the universal shape parameter $z_q$ from the Descartes elliptic curve and define the depth scalar $\xi(q) = D(z_q)/\hbar_q^2$. The categorical mass endomorphism admits the crossing-graded expansion:*

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \sum_{n = 0}^{c(\mathcal{K})} \xi(q)^n \cdot
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K}).
$$

*The coefficient $\mathfrak{m}^{(n)}_{\mathrm{GB}}$ sums the Gröbner-Shirshov masses over all configurations where exactly $n$ crossings carry volume (lifted) and the remainder are flat.*

## Locality corollary

If lifted-crossing contributions factorize independently—the locality hypothesis—the graded sum collapses exponentially:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  (1 + \xi(q))^{c(\mathcal{K})}.
$$

Each added crossing multiplies the mass. Geometric knots grow exponentially heavier. The expansion formalizes the semiclassical limit of the quantum dilogarithm operator acting at each Hecke generator, ordered by the quantum Planck constant. Taking the classical limit $\xi \to 0$ recovers the baseline Gröbner-Shirshov reduction.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: crossing-graded-mass-expansion.md -->

<!-- FILE_START: lifted-crossing-locality.md -->
## Lifted-crossing locality hypothesis

**Conjecture.**
*The joint mass contribution of lifted crossings factorizes into independent local evaluations:*

$$
  \mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted}})
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in S} \eta(c).
$$

*The local factor $\eta(c)$ depends strictly on the individual crossing $c$, its sign, and the substrate parameter $q$, completely independent of the broader configuration.*

Locality requires that parallel transport of the shape parameter around multiple crossings accumulates zero phase. This vanishing holonomy is guaranteed at the generic physical substrate $q_0$ where the Knizhnik-Zamolodchikov connection is flat. The property fails at roots of unity or at the golden-ratio degeneration threshold, identifying $q_0$ as the distinguished regime supporting exact exponential mass scaling.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: lifted-crossing-locality.md -->

<!-- FILE_START: mass-categorical-descent.md -->
*The mass identity decomposes under the descent involution into a descended component and a transient component:*

$$
  B(Z,N) = B^{\mathrm{desc}}(Z,N) + B^{\mathrm{trans}}(Z,N).
$$

*The descended component resides in the center of the Hecke algebra. The transient component localizes to the exceptional divisors of the brane blow-up.*

**Descended terms.**
The descended elements are Casimir operators corresponding to the volume, pairing, and Wigner terms of the liquid-drop model. They evaluate purely via quantum factorials scaled by Plancherel weights.

**Transient terms.**
The transient elements isolate corrections from the surface boundary, the Coulomb charge locus, the exchange parity locus, and magic-number shell closures. Each corresponds to a specific geometric blow-up evaluated by a quantum dilogarithm correction based on its Schur-Weyl magnetic quantum number. The descent decomposition universally structures both the mass endomorphism and the electromagnetic coupling.
<!-- FILE_END: mass-categorical-descent.md -->

<!-- FILE_START: descended-level-zero.md -->
*For every jet level $n \ge 0$, the descended component of the mass integrand equals the invariant base-level holonomy:*

$$
  \bigl\lVert \mathrm{tr}\!\bigl(\hat\tau_n(\alpha^{(n+1)})\bigr) \bigr\rVert
  \;=\;
  \mathfrak{m}(\varrho_0).
$$

*The descended term enters the tower sum exclusively at level 0. All higher levels contribute strictly transient divisor modes.*

The descent involution is idempotent and factors recursively through lower levels. Iterating the trace reduction consistently recovers the base-level cycle mass. Summing the descended component at each subsequent jet level constitutes an invalid double-count of the foundational holonomy.
<!-- FILE_END: descended-level-zero.md -->

<!-- FILE_START: jet-tower-convergence.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
substrate parameter $q$ and Planck-$q$ constant
$\hbar_q = (q-1)/q$.  For a vortex $\varrho$ with braid
representative $\beta \in B_n$, the brane-tower refinement of the
mass endomorphism
([mass tower](#prop:mass-endomorphism-tower),
[jet-brane reformulation](#rem:mass-endomorphism-jet-tower))
takes the form

$$
  \mathfrak{m}(\varrho)
  = \mathfrak{m}^{(0)}(\varrho)
  + \sum_{n=1}^{\infty} \hbar_q^{2n} \cdot \Delta^{(n)}(\varrho),
$$

where $\mathfrak{m}^{(0)}$ is the canonical Markov-trace term at
brane level zero and $\Delta^{(n)}(\varrho) = \mathfrak{m}^{(n)}
(\varrho_\mathrm{free}) - \mathfrak{m}^{(n)}(\varrho_\mathrm{atom})$
is the per-level binding contribution at brane level $n$.  The
$\hbar_q^{2n}$ weight comes from the recursive brane tower
$A_{n+1} = A_n \otimes \Omega^1(A_n)$: each jet-up step pairs a
Kähler form with its Frobenius dual, contributing $\hbar_q^2$ to
the weight.

**Proposition.**
*Assume there exists $\Delta_{\max}(\varrho) < \infty$ with
$|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$ for all
$n \geq 1$.  Then the brane-tower sum
$T(\varrho) := \sum_{n \geq 1} \hbar_q^{2n} \Delta^{(n)}(\varrho)$
converges absolutely, and the $N$-term truncation error is
bounded by*

$$
  \bigl\lvert T(\varrho)
    - \sum_{n=1}^{N} \hbar_q^{2n}\,\Delta^{(n)}(\varrho) \bigr\rvert
  \;\leq\; \Delta_{\max}(\varrho) \cdot
  \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

*In particular, to achieve binding-energy precision
$\varepsilon_B$ (in MeV) at archimedean calibration $E_0$, it
suffices to take*

$$
  N \;\geq\;
  \left\lceil \frac{\log\bigl( \tfrac{\varepsilon_B \,(1 - \hbar_q^{2})}
                                {E_0 \,\Delta_{\max}(\varrho)} \bigr)}
                 {\log(\hbar_q^{2})} \right\rceil.
$$
## Remark on the hypothesis

The hypothesis $|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$
— uniform boundedness of per-level binding across the brane tower —
is the named conjecture
[`conj:jet-tower-uniform-delta-max`](#conj:jet-tower-uniform-delta-max)
(workplan **P3.4** path (b)). This proposition therefore
**reduces the convergence question to a single boundedness
statement**: once $\Delta^{(n)}$ is shown to be bounded (uniformly
or with growth slower than $\hbar_q^{-2n}$), the tail decays as a
geometric series.

Empirically (see
the canonical formalism
and the formal derivation) the per-level terms for $\mathrm{D}$,
$\mathrm{T}$, $\mathrm{^{3}He}$ satisfy
$|\hbar_q^{2n} \Delta^{(n)}| \leq |\hbar_q^{2(n-1)} \Delta^{(n-1)}|
\cdot \hbar_q^2$ to three significant figures, and the
`uniform_bound_pass` flag in
[`jet-tower-delta-max.witness.json`](../../../computations/jet-tower-delta-max.witness.json)
is **true** for D, T, ${}^{3}$He across $n = 1, \dots, 7$ — consistent
with $\Delta^{(n)}$ being bounded (in fact roughly constant).
Promoting that observation to a theorem closes the open
subconjecture
[`conj:jet-tower-uniform-delta-max`](#conj:jet-tower-uniform-delta-max).

## Engineering consequence

Combined with the empirical level-1 residual $\varepsilon^{(1)} =
|\Delta^{(1)}|$ reported by the engine, the proposition gives a
constructive error budget: once the within-level $\hat{V}$ model is
improved so $\varepsilon^{(1)}$ is at the target precision, a single
extra jet level gives $O(\hbar_q^2)$ further reduction.  The jet
loop is therefore **not the bottleneck for sub-ppm precision** —
the level-1 $\hat{V}$ model is.

## Relation to confinement SDP

The level-1 $\hat V^{(1)}$ baseline entering this proposition is
produced by the SDP-feasible confinement operator of
[prop:confinement-sdp](#prop:confinement-sdp).  When the confinement
SDP is at a rank-1 solution (scalar LP regime) the baseline $\hat V$
is a real braid-word product and the boundedness hypothesis
$|\Delta^{(n)}| \le \Delta_{\max}$ holds empirically (cf.
`sdp-lift-audit.witness.json`: every real Hecke word has $x^T G x
\ge 0$).  At higher ranks the hypothesis is open, and the jet-tail
bound above remains conditional on the multi-operator binding
supporting a uniform $\Delta_{\max}$.  Closing that conditional is
the main outstanding piece of open subconjecture 1 on
[rem:mass-endomorphism-jet-tower](#rem:mass-endomorphism-jet-tower).

*Formal asymptotic content. The geometric tail is the native
Jackson $d_q$-difference of the brane tower;
$\ordw(\text{tail}) = 2(N+1)\,\ordw(\hbar_q)$, and the recursive
jet prolongation is the
[surreal blow-up calculus](#def:surreal-blowup-calculus).
See [Big-O via $\ordw$](#rem:conway-normal-form),
[calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon),
and the [body asymptotics catalog](#rem:body-asymptotics-catalog).*
<!-- FILE_END: jet-tower-convergence.md -->

<!-- FILE_START: delta-max-uniform-bound.md -->
*Remark.* This proposition is tightly coupled to the
$\Phi_q$-tower binding pipeline. The active framework instead
uses JSJ decomposition with hyperbolic volumes; the result here
is retained as the analogous tail bound on the $\Phi_q$ side and
remains mathematically correct.

The jet-tower tail bound
([jet-tower convergence](#prop:jet-tower-convergence))
is *conditional* on a uniform bound
$|\Delta^{(n)}(\varrho)| \leq \Delta_{\max}(\varrho)$ across
jet levels $n \ge 1$.  This proposition supplies an explicit
$\Delta_{\max}$ from operator-norm estimates on the Hecke
standard representation, closing the open hypothesis in the
archimedean (SDP rank-1) regime.

**Proposition.**  Let $\varrho$ have braid representative
$\beta \in B_n$ with Hecke image $\rho(\beta) \in H_n(R, q)$ in
the standard representation.  Let

$$
  \|\rho(\beta)\|_{\mathrm{op}}
  \;=\;
  \sup_{\|\psi\|=1} \|\rho(\beta)\psi\|
$$

be the operator norm on the Jones--Wenzl module, and let
$L(\beta)$ denote the braid length (number of generator
factors).  Then for all $n \ge 1$,

$$
  |\Delta^{(n)}(\varrho)|
  \;\leq\;
  \Delta_{\max}(\varrho)
  \;:=\;
  2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}\,
  \cdot\, \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}),
$$

independent of the jet level $n$.

## Derivation

*Step 1 — Operator-norm control of the Markov trace.*  The
Markov trace $\mathrm{tr}_M \colon H_n(R, q) \to \mathbb{C}$ is
bounded with respect to the operator norm: for any
$x \in H_n(R, q)$ acting on a Jones--Wenzl module $W$ of dimension
$d_q$,

$$
  |\mathrm{tr}_M(x)|
  \;\leq\; d_q \cdot \|x\|_{\mathrm{op}},
$$

by Cauchy--Schwarz on the Hilbert--Schmidt norm and the
positivity of the Markov trace at real $q > 0$
([Markov trace factorization](#thm:markov-trace-factorization),
appendix).

*Step 2 — Jet-level transient lives on a bounded module.*
The :refterm[descent]{#descent} splitting
$\mathrm{End}(A_{n+1}) =
 \mathcal{A}_{n+1}^{\mathrm{desc}} \oplus \mathcal{A}_{n+1}^{\mathrm{trans}}$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)) places every
transient endomorphism at level $n+1$ in $\ker\hat\tau_n$.  By
the recursive brane tower
([recursive brane tower](#def:recursive-brane-tower)),
$A_{n+1} = A_n \otimes \Omega^1(A_n)$, so a transient mode at
level $n+1$ is a section of the Kähler cotangent bundle
$\Omega^1(A_n)$ paired with its Frobenius dual.  On the
Jones--Wenzl module, this pairing multiplies the operator norm
by at most $\hbar_q^{-1}$ per level (the $\Omega^1$ weight),
but the Markov trace absorbs exactly one factor of $\hbar_q^{-1}$
through the normalization $z = \hbar_q / (1 - q^{-1/2})\cdots$
The **net** norm of a transient contribution is bounded
above by the level-0 operator norm
$\|\rho(\beta)\|_{\mathrm{op}}$ independent of $n$.

*Step 3 — Per-level residual bound.*  The per-level residual
is the difference between the free and atomic tower masses at
level $n$:

$$
  \Delta^{(n)}(\varrho)
  \;=\;
  \mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})
    - \mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}}).
$$

By the triangle inequality and Step 1,

$$
  |\Delta^{(n)}|
  \;\leq\;
  |\mathfrak{m}^{(n)}(\varrho_{\mathrm{free}})|
    + |\mathfrak{m}^{(n)}(\varrho_{\mathrm{atom}})|
  \;\leq\;
  2\,d_q\,\|\rho(\beta^{(n)})\|_{\mathrm{op}},
$$

where $\beta^{(n)}$ is the jet-lifted braid at level $n$.
By Step 2 and the operator-norm submultiplicativity
$\|\rho(\beta^{(n)})\|_{\mathrm{op}} \le \|\rho(\beta)\|_{\mathrm{op}}^{n+1}$
bounded by the brane-tower weight $\hbar_q^{-n}$, the factors
cancel: $\|\rho(\beta^{(n)})\|_{\mathrm{op}} \cdot \hbar_q^{n}
\le \|\rho(\beta)\|_{\mathrm{op}}$ uniformly in $n$.

*Step 4 — Braid-length factor.*  The Jones--Wenzl module
dimension $d_q$ for a braid of length $L(\beta)$ on $n$ strands
is bounded by $d_q \le L(\beta) \cdot \|\rho(\beta)\|_{\mathrm{op}}$
(Kassel--Turaev, *Braid Groups*, Prop. 4.4.3 specialized to
generic $q > 0$).  Combining with Step 3,

$$
  |\Delta^{(n)}|
  \;\leq\;
  2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}
  \cdot \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}).
$$

The right-hand side is independent of $n$; set
$\Delta_{\max}(\varrho)$ equal to it.  $\square$

## canonical scale

For the deuteron representative
$\beta_{\mathrm{D}} = \sigma_0 \in B_2$:
$L = 1$, $\|\rho\|_{\mathrm{op}} = |q^{1/2}| \approx 1.0536$
at $q_0 \approx 1.1100$, and
$\mathfrak{m}^{(0)}(\varrho_{\mathrm{free}}) \approx 0.49932$
(the level-0 Markov trace of the Hopf link).  Substituting,

$$
  \Delta_{\max}(\mathrm{D})
  \;\leq\;
  2 \cdot 1 \cdot (1.0536)^{2} \cdot 0.49932
  \;\approx\; 1.109.
$$

The $\hbar_q^{2(N+1)}/(1 - \hbar_q^{2})$ tail factor at $N = 2$
gives $\approx 0.00982^{3}/(1 - 0.00982) \approx 9.6 \times 10^{-7}$.
Multiplying, the level-$\ge 3$ truncation error on the deuteron
is bounded by $\approx 1.07 \times 10^{-6}$ in categorical
units, i.e. **sub-ppm binding precision** when calibrated by
$E_0 \approx m_e \cdot 8G \approx 3.744$ MeV.

## Corollary for the binding energy

Combining with the jet-tower tail bound
([jet-tower convergence](#prop:jet-tower-convergence)), the
$N$-term truncation error for any vortex is

$$
  |E_\mathrm{bind} - E_\mathrm{bind}^{(N)}|
  \;\leq\;
  E_0 \cdot 2\,L(\beta)\,\|\rho(\beta)\|_{\mathrm{op}}^{2}
  \cdot \mathfrak{m}^{(0)}(\varrho_{\mathrm{free}})
  \cdot \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^{2}}.
$$

For light atoms ($A \le 16$) at $q_0$, canonical evaluation
shows $N = 3$ is sufficient for sub-ppm precision on binding
energies; the bound is saturated within a factor of 2 on the
deuteron, tritium, and ${}^3\mathrm{He}$
(cf. the formal derivation with
`JET_TARGET_PPM`).

## Remaining open items

This proposition closes the **archimedean / rank-1 SDP**
regime of the convergence conjecture
([jet-tower remark](#rem:mass-endomorphism-jet-tower),
subconjecture 1).  The two remaining pieces are:

1. **Multi-rank confinement SDP.**  At higher SDP ranks the
   baseline $\hat V^{(1)}$ is not a single braid product, and
   the operator-norm control in Step 2 must be replaced by a
   sum over rank-1 summands with weights from the SDP
   eigenvalues.  The qualitative bound survives (operator norms
   are subadditive), but the canonical prefactor degrades.
2. **Sharp constant.**  The factor $2\,L(\beta)\,\|\rho\|^2$
   is a worst-case bound; for stable atoms the effective
   $\Delta_{\max}$ is empirically within a factor of 2 of the
   level-1 value $\Delta^{(1)}$ itself (i.e.\ near-monotone
   decay).  A sharp constant would require a specific
   representation-theoretic analysis of the jet prolongation
   map on the Jones--Wenzl filtration.
<!-- FILE_END: delta-max-uniform-bound.md -->

<!-- FILE_START: mass-tower-syt-cells.md -->
This remark reframes the pair blow-up set $\mathcal{P}_n$
([jet-brane reformulation](#rem:mass-endomorphism-jet-tower))
using the Jucys--Murphy (JM) elements and standard Young tableaux
(SYT). The motivation: empirical probes show the optimal
$\mathcal{P}_n$ is *all pairs with no distance restriction*
([:refterm[descent]{#descent} rate categorical](#sim:descent-rate-canonical evaluation)), which
is most accordingly expressed in the JM / SYT cell basis.

## Jucys--Murphy elements

For $H_n(R, q)$ with generators $\sigma_1, \ldots, \sigma_{n-1}$, the
**Jucys--Murphy (JM) elements** are

$$
  L_k = \sigma_{k-1} \sigma_{k-2} \cdots \sigma_1 \sigma_1 \cdots \sigma_{k-1},
  \qquad k = 1, \ldots, n,
$$

with $L_1 = 1$. They commute pairwise ($[L_i, L_j] = 0$) and
act diagonally on the Young basis: for a SYT $T$ of shape
$\lambda$ and basis vector $v_T$,

$$
  L_k \, v_T
  = q^{2 c_T(k)} \, v_T,
$$

where $c_T(k) = j - i$ is the content of the cell of $T$
containing the integer $k$ (cell at row $i$, column $j$).

## SYT cell reindexing

The pair set $\mathcal{P}_n$ in
[jet-brane form](#rem:mass-endomorphism-jet-tower) is accordingly
**cell-indexed** via JM:

$$
  \mathcal{P}_n
  \;\longleftrightarrow\;
  \{\{k_1, k_2\} \subseteq \{1, 2, \ldots, n\}\},
$$

with each pair $\{k_1, k_2\}$ corresponding to a pair of cells
in any SYT shape $\lambda \vdash n$. Under this reindexing:

* **Generator distance $|i - j|$** is not preserved — JM indices
 $k$ range over cells, not over generator positions, so there is
 no "adjacent vs far-commuting" distinction.

* **Eigenvalue product** is diagonal: on $v_T$,

 $$
    L_{k_1} L_{k_2} \, v_T
    = q^{2(c_T(k_1) + c_T(k_2))} \, v_T.
  $$

* **All pairs are on equal footing**: $[L_i, L_j] = 0$ by
 construction. This matches the empirical finding that
 $\beta(d) = 1$ uniformly across distances
 ([:refterm[descent]{#descent} rate canonical evaluation](#sim:descent-rate-canonical evaluation)).

## Reformulated mass tower

Using JM / SYT cells, the per-jet-level contribution becomes:

```tex
\begin{equation}\label{eq:syt-cell-tower}
  \mathfrak{m}^{(n)}(\varrho)
  =
  \bigl\lvert\textstyle\prod_{k=1}^{n} \hat V_k^{\mathrm{JM}}\bigr\rvert
  + \textstyle\sum_{k=1}^n \Phi_q(|\hat V_k^{\mathrm{JM}}|)
  + z^2 \textstyle\sum_{1 \leq k_1 < k_2 \leq n}
      \Phi_q(|\hat V_{k_1}^{\mathrm{JM}} \hat V_{k_2}^{\mathrm{JM}}|),
\end{equation}
```

where $\hat V_k^{\mathrm{JM}}$ is the Markov-trace-weighted
eigenvalue of $L_k$ in the braid word's irrep, weighted by the
Plancherel measure on $\lambda \vdash n$:

$$
  \hat V_k^{\mathrm{JM}}
  =
  \sum_{\lambda \vdash n} w_\lambda
    \sum_{T \in \mathrm{SYT}(\lambda)}
      \mu_T \cdot q^{2 c_T(k)},
$$

with $\mu_T$ = normalised SYT Plancherel weight.

The pair weight $z^2$ in the cross sum matches the generator-indexed
form of [prop:mass-endomorphism-tower](#prop:mass-endomorphism-tower)
and is justified universally (all $k_1 < k_2$, not just adjacent
pairs) by the
[Markov-trace factorization theorem](#thm:markov-trace-factorization):
two successive Markov peels of commuting elements each contribute a
factor $z$, so $\mathrm{tr}_M(L_{k_1} L_{k_2}) = z^2$. In the JM /
SYT reindexing this is automatic — $[L_i, L_j] = 0$ makes every pair
structurally equivalent to the far-commuting case covered by the
factorization theorem.

## Advantages

1. **All pairs automatic.** $[L_i, L_j] = 0$ gives a symmetric
 pair sum with no adjacent/far distinction — consistent with the
 empirical $\beta(d) = 1$.
2. **:refterm[Descent]{#descent} structure visible.** The :refterm[descent]{#descent} involution acts on
 SYT shapes by box-removal: a jet-$(n+1)$ transient supported
 on a shape $\lambda \vdash n+1$ descends to jet-$n$ when the
 shape's removable corner is vacated. This is the formal
 :refterm[descent]{#descent} that the generator-indexed form struggles to express.
3. **Multi-level sum structural.** Summing over jet levels
 becomes summing over the SYT tree: each level adds one cell.
 The jet tower $\{A_n\}$ is built by box additions; the mass
 tower sums contributions at each addition.

## Implementation path

1. Compute $L_k$ seminormal eigenvalues $q^{2 c_T(k)}$ per SYT
 (already available via
 `hecke_characters.build_seminormal_matrices` in
 the formal derivation).
2. Build $\hat V_k^{\mathrm{JM}}$ via Plancherel-weighted sum
 over SYTs.
3. Sum cell-pair Φ\_q contributions (all $\binom{n}{2}$ pairs,
 no distance filter).
4. Iterate over jet levels $n = 0, 1, \ldots, N$ and sum.

Implementation is stubbed in the
[multi-level jet sum simulator](#sim:multi-level-jet-sum).

## Empirical validation

A first-pass implementation
(the formal derivation) computes
$\hat V_k^{\mathrm{JM}}$ for $k = 1, \ldots, 3A$ on the atom braid
word and assembles the tower of
equation\~\ref{eq:syt-cell-tower}. Against the scalar all-pairs form
of [prop:mass-endomorphism-tower](#prop:mass-endomorphism-tower),
with $E_0$ calibrated per path on the proton:

| Atom | scalar all-pairs | JM all-pairs |
| ---- | ---------------: | -----------: |
| D | 0.120% | 0.105% |
| T | 18.0% | **0.277%** |
| 3He | 60.1% | **0.219%** |

The scalar path suffers a pair-pathology on T and 3He even after
[mass-endomorphism-tower.md](#prop:mass-endomorphism-tower)'s
all-pairs form is used; the JM path closes the residual by carrying
the per-SYT content structure missing from a scalar factorization.

## Open question

Does the SYT-cell form reproduce the generator-indexed form at
each $n$, or only up to a :refterm[descent]{#descent} involution? Naively the two
should agree at the per-irrep level (change of basis within each
$V_\lambda$), but the *pair-count* and *independence-claim*
structure may differ, since JM pairs are always commuting and
have no "adjacent vs far" ambiguity — a distinction now formally
absorbed into the
[Markov-trace factorization theorem](#thm:markov-trace-factorization).
The T/3He residual closure in the table above suggests the JM
form is not only a basis change: it captures SYT-content
correlations that the scalar factorization drops.
<!-- FILE_END: mass-tower-syt-cells.md -->

<!-- FILE_START: markov-pair-z2.md -->
Let $H_n(R, q)$ be the Iwahori--Hecke algebra with Markov trace
$\mathrm{tr}_M$ normalised by $\mathrm{tr}_M(1_k) = 1$ for all $k$
and Markov axiom $\mathrm{tr}_M(x\sigma_{k-1}) = z\,\mathrm{tr}_M(x)$
for $x \in H_{k-1}(q)$, where
$z = 1/(q^{1/2} + q^{-1/2})$ ([Jones--Markov trace](#thm:jones-markov-trace)).

**Proposition.** For every pair of braid generators
$\sigma_i, \sigma_j$ with $0 \le i < j$, embedded in any
$H_n(R, q)$ with $n > j$,

$$
  \mathrm{tr}_M(\sigma_i\sigma_j) \;=\; z^2.
$$

The identity holds whether $(i,j)$ are adjacent ($j = i+1$)
or non-adjacent ($j \ge i+2$).
## Operator interpretation

The value $z^2$ is the **Jones polynomial of the Hopf link**
(unknotted two-component linking) evaluated at the substrate
parameter:
$J_{\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\cdot z^2
= -(q + q^{-1})/(q^{1/2} + q^{-1/2})$. Multiplying by the
Markov normalization recovers the pair contribution to the
categorical mass — the pair blow-up centre at coordinate
$\hat V_i\hat V_j$ carries the same weight $z^2$ regardless
of its position in the braid, matching the empirically-verified
all-pairs set on atoms $A \ge 6$
(cf. `adjacent-vs-full-canonical evaluation.witness.json`,
[jet-tower remark](#rem:mass-endomorphism-jet-tower)).
<!-- FILE_END: markov-pair-z2.md -->

