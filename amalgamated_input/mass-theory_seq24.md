<!-- FILE_START: intro-mutant-jones-bloch-group.md -->
The Jones polynomial fails to distinguish mutant knots, notably the Conway and Kinoshita-Terasaka pair. However, the substrate-level Hecke framework tracks refined invariants beyond the closure trace. This section applies the mutant pair as a critical falsifiability test. We identify the Bloch-group closure as the exact categorical mechanism resolving mutant ambiguity.

The sequence maps the bi-filtration grid that categorically separates mutants, tests the substrate invariant against the canonical mutant pair, and connects this separation directly to the Bloch-group quotient. This yields the strongest falsifiability target in the chapter: a precise geometric divergence where the standard polynomial evaluates identically.
<!-- FILE_END: intro-mutant-jones-bloch-group.md -->

<!-- FILE_START: knot-indexed-convolution-grid.md -->
*Each operational non-tensor product linking two morphisms in the QOU occupies a specific $(n, K)$ stratum in the bi-filtration grid $\mathcal{H}_q^{(n, K)}$.*

### The grid structure

Most knot-indexed operations operate algebraically at depth $n=0$ without polylogarithms. They shift the knot-index axis strictly through structural translation. The archimedean image emerges at higher depths only post-realization via $\tau_{\mathrm{arch}}$.

The bi-filtration cleanly separates input shape (depth-0 knot index) from output transcendence depth (post-realization polylogarithm). The interface coupling $\bowtie_K$ exemplifies this as a strict depth-0 convolution in the Hecke algebra, manipulating elements algebraically without generating higher-order transcendental terms.

This grid systematizes existing convolutions, predicts compositions between depths, and identifies open falsifiability targets like high-$n$ chiral entries.
<!-- FILE_END: knot-indexed-convolution-grid.md -->

<!-- FILE_START: conway-kt-vol-injectivity-test.md -->
**Remark (Conway-Kinoshita-Terasaka mutant pair).**

The transcendental accounting framework predicts that identical Jones polynomials imply identical hyperbolic volumes. The Conway and Kinoshita-Terasaka mutant knots share exactly the same Jones polynomial and the same hyperbolic volume, satisfying this prediction. 

Mutation preserves the colored Jones polynomials and the hyperbolic volume universally (Ruberman's theorem). The prediction therefore holds trivially for mutants. 

For rigorous falsifiability, the Vol-injectivity hypothesis requires a non-mutant knot pair sharing identical Jones polynomials but exhibiting distinct hyperbolic volumes. No such pairs are currently known within the Bring-embeddable class. Discovering one would strictly falsify the $J^{(2)}$ Vol-injectivity claim, though the higher-color asymptotic Volume Conjecture mechanism would remain mathematically consistent.
<!-- FILE_END: conway-kt-vol-injectivity-test.md -->

<!-- FILE_START: jones-faithfulness-crossing-8.md -->
**Remark (Bring-embeddable Jones-faithfulness).**

The Hoste-Thistlethwaite-Weeks enumeration proved that distinct prime knots up to 10 crossings possess unique Jones polynomials. The Conway-KT mutant pair breaks this uniqueness precisely at 11 crossings. 

Since both the Conway and KT knots are Bring-embeddable (genus 3), Jones-faithfulness strictly fails for Bring-embeddable knots at crossing 11. However, Ruberman's theorem forces their volumes to match, maintaining the Vol-injectivity prediction. The open challenge remains locating non-mutant Jones-coincident pairs above 11 crossings to construct a definitive falsification target.
<!-- FILE_END: jones-faithfulness-crossing-8.md -->

<!-- FILE_START: wedderburn-as-noncomm-fourier.md -->
**Statement.**
*The character expansion driving the three-invariant mass formula operates identically to the inverse non-commutative Fourier transform on the semisimple Hecke algebra $H_n(q)$.*

The Wedderburn-Artin decomposition maps the Markov trace into a spectral expansion over partitions. The trace reassembles class functions directly from these non-commutative Fourier coefficients.

This proposition asserts no new physics. It clarifies the underlying mechanism: the mass formula evaluates specific physical channels by selecting isolated partitions from the non-commutative spectrum. The identification governs the Pieri-shift dynamics of the Hecke photon and the spectral distribution of the archimedean remainder.
<!-- FILE_END: wedderburn-as-noncomm-fourier.md -->

<!-- FILE_START: degree-one-braid-trivial-volume.md -->
**Statement.**
*Let $\gamma$ be a degree-one braid element. Under the archimedean realization functor, the volume image vanishes identically:*

$$
  \tau_{\mathrm{arch}}\!\bigl(\operatorname{tr}_M(\gamma)\bigr)
  \;=\; 0.
$$
<!-- FILE_END: degree-one-braid-trivial-volume.md -->

<!-- FILE_START: pieri-photon-shift.md -->
**Statement.**
*Let $\gamma$ be a degree-one element, and let $\beta_m$ be supported purely on the $\lambda$-block. The support of the product $\gamma \cdot \beta_m$ expands strictly to partitions adjacent to $\lambda$ in the Young lattice:*

$$
  \mathrm{supp}\bigl(\gamma \cdot \beta_m\bigr)
  \;\subseteq\;
  \{\lambda\} \;\cup\;
  \{\lambda + \square\} \;\cup\;
  \{\lambda - \square\}.
$$
<!-- FILE_END: pieri-photon-shift.md -->

<!-- FILE_START: pieri-photon-shift-interpretation.md -->
**Remark (spectral shift).**
Under the non-commutative Fourier transform, the degree-one element acts as a discrete finite-difference operator. It shifts the Young-diagram support up or down by exactly one box, analogous to a single-step translation on the commutative frequency lattice.
<!-- FILE_END: pieri-photon-shift-interpretation.md -->

<!-- FILE_START: phi-q-tower-jsj-bridge.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

**Conjecture ($\Phi_q$-JSJ archimedean bridge).**
*Under the archimedean realization, each summand of the dilogarithm tower evaluates precisely to the hyperbolic volume of the corresponding $\Phi_q$-piece, weighted by the substrate density:*

$$
  \tau_{\mathrm{arch}}\!\bigl(z^{\lvert S\rvert} \cdot \Phi_q(\|V_S\|_F)\bigr)
  \;=\;
  \rho_q \cdot
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S).
$$

*Summing over all subsets perfectly reconstructs the continuous JSJ piecewise sum.*

This conjecture aligns the algebraic discrete evaluation with the geometric continuous evaluation. The dilogarithm pipeline and the hyperbolic-volume pipeline compute the identical archimedean target through entirely different convergence regimes. It formalizes the quantum Bloch group regulator mapping the algebraic strata directly onto the JSJ decomposition.
<!-- FILE_END: phi-q-tower-jsj-bridge.md -->

<!-- FILE_START: dilogarithm-archimedean-limit.md -->
**Conjecture (Archimedean limit).**
*Under the joint Faddeev scaling $q \to 1$, $n \to \infty$, the rescaled logarithm of the $q$-Pochhammer partial product converges strictly to the classical dilogarithm:*

$$
  \lim_{\substack{q \to 1 \\ n \to \infty \\ n |1-q| \to \infty}}
  (1 - q) \cdot \log \Phi_n(x; q)
  \;=\;
  \mathrm{Li}_2(x).
$$

The elementary uniform convergence for $x \in (0, 1)$ holds strictly on the sub-unity limit. The substantive open content concerns the substrate continuation extending past the branch cut, demanding exact cancellation among algebraic poles before evaluating the principal branch.

This conjecture supplies the required algebraic half of the overarching Kashaev volume conjecture, pairing with the Bloch-Wigner geometric half to construct the complete continuous volume.
<!-- FILE_END: dilogarithm-archimedean-limit.md -->

<!-- FILE_START: phi-q-wkb-greens-function.md -->
**Conjecture (WKB Green's function).**
*Under joint Faddeev scaling, the partial product admits a stationary-phase expansion where the sub-leading term represents the half-log-determinant of the categorical Dirac operator:*

$$
  S_1(x_0)
  \;=\;
  -\tfrac{1}{2} \log \det\!\bigl(\mathfrak{D}_\nabla\big|_{x_0}\bigr).
$$

*The archimedean realization of this one-loop fluctuation factor equals the hyperbolic Green's function at the corresponding cusp.*
<!-- FILE_END: phi-q-wkb-greens-function.md -->

<!-- FILE_START: algebraic-geometric-dilog-equivalence.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

**Conjecture (Algebraic-geometric dilogarithm equivalence).**
*The categorical Markov trace of the nonabelian multiplicative integral
over a lifted transient crossing
([mass identity](#def:mass-identity))
evaluates algebraically to a rational function in $\mathbb{Z}[q^{1/2},
q^{-1/2}, x]$ governed by the $q$-Pochhammer partial product
$\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
([q-Pochhammer partial product](#def:q-pochhammer-partial-product)).
Under the Archimedean realization $\tau_{\mathrm{arch}}$
([archimedean realization functor](#def:archimedean-realization-functor)):*

1. *(**Pole-to-cusp bijection.**) The roots
   $\{x = q^{-k} : k = 0, \dots, n-1\}$ of the denominator
   $(x; q)_n$ are in bijection with the ideal vertices of a hyperbolic
   tetrahedron triangulating the $\Phi_q$-piece $K_S$ of the lifted
   transient crossing
   ([Φ$_q$-piece](#def:phi-q-piece)).*

2. *(**Asymptotic Bloch–Wigner.**) The asymptotic of the partial
   product under Faddeev's scaling
   ([Archimedean limit](#conj:dilogarithm-archimedean-limit))
   recovers the Bloch–Wigner dilogarithm $D(z)$ at the matched shape
   parameter, so*

$$
  \tau_{\mathrm{arch}}\!\bigl(\Phi_n(x; q_0)\bigr)
  \;\xrightarrow[n \to \infty]{}\;
  D(z(x))
  \;=\;
  \mathrm{Vol}_{\mathrm{hyp}}\bigl(\Delta_{z(x)}\bigr),
$$

   *where $z(x)$ is the shape parameter of the ideal tetrahedron
   $\Delta_{z(x)}$ that triangulates $K_S$.*

3. *(**Mass formula.**) The $\tau_{\mathrm{arch}}$-image of the
   transient mass element is*

$$
  \tau_{\mathrm{arch}}\!\bigl(\mathfrak{m}^{\mathrm{trans}}(\varrho)\bigr)
  \;=\;
  \rho_q \cdot
  \!\!\sum_{S \subseteq \{0,\dots,n-2\}}\!\!
  D\bigl(z(\lvert V_S\rvert)\bigr)
  \;=\;
  \rho_q \cdot
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K),
$$

   *recovering the JSJ piecewise sum used in the canonical binding-
   energy pipeline (cf.
   [Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)).*

## Relation to the structural form of Kashaev

The conjecture is the **QOU-native, partial-product** form of the
Kashaev–Murakami–Murakami theorem
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)).
Kashaev–MM pass through the colored Jones polynomial at roots of
unity; the present conjecture passes through the **explicit shared
denominator**:

| Side | Object | Pole / singularity |
|------|--------|--------------------|
| Algebraic ($R$) | $\Phi_n(x; q_0)$ | zero of $(1 - x q^k)$ at $x = q^{-k}$ |
| Archimedean ($\mathbb{C}$) | $\mathrm{Li}_2$ | logarithmic singularity at $t = 1$ |
| Geometric ($\mathbf{Hyp}_3$) | ideal tetrahedron $\Delta_z$ | cusp at vertex $v_k$ |

The bijection between the rows is the content of
([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).
Under that bijection, the algebraic state sum and the hyperbolic
volume are not two competing engines: they are the same regulator
$\Phi_n(x; q_0) \mapsto D(z(x))$ evaluated through two convergence
schemes.

## Conjectural standing (AGENTS.md §3b)

This block is downstream of
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)) and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)), so it is
necessarily a **conjecture** — propagation of conjectural backing
forbids promotion to `proposition`/`theorem`.

A Lean instance of the equivalence is provided as a typeclass
`QOU.QPochhammer.algebraic_geometric_equivalence` parametrised by an
`[ArchimedeanLimit]` instance and a `[Kashaev.VolumeConjecture]`
instance; downstream theorems then verify formally, modulo those two
class instances. This matches the conjectural-class pattern used for
[Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge).

## Witness

The algebraic-geometric matching of poles to cusps for the simplest
non-trivial case (the trefoil, $n = 3$) is recorded in
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json).
The witness reports the algebraic denominator zeros, the SnapPy-
solved cusp shape parameters obtained by feeding those zeros as
Newton–Raphson seeds, and the residual after one Newton step.
<!-- FILE_END: algebraic-geometric-dilog-equivalence.md -->

<!-- FILE_START: shared-denominator-cusp-holonomy.md -->
**Conjecture (Shared-denominator cusp holonomy).**
*Let $T_w \in H_n(R, q)$ be a Hecke normal-form word at GB-depth
$k_\star(T_w) = n$, let $\Phi_n(x; q) = \prod_{k=0}^{n-1}(1 - x q^k)^{-1}$
be its $q$-Pochhammer partial product
([definition](#def:q-pochhammer-partial-product)),
and let $K_S$ be the $\Phi_q$-piece of the lifted braid
([Φ$_q$-piece](#def:phi-q-piece)). Then the roots of the
denominator polynomial*

$$
  (x; q)_n
  \;=\;
  \prod_{k=0}^{n-1}\bigl(1 - x q^k\bigr)
  \;\in\;
  \mathbb{Z}[q, x]
$$

*enforce the **cusp completeness conditions** of the Thurston
gluing equations on the ideal-tetrahedron triangulation of
$S^3 \setminus K_S$:*

$$
  (x; q_0)_n \;=\; 0
  \quad\Longleftrightarrow\quad
  \mathrm{Hol}_{\mu_k}(z_k) = 1
  \;\;\text{and}\;\;
  \mathrm{Hol}_{\lambda_k}(z_k) = 1
  \;\;\text{for some cusp}\;k,
$$

*where $z_k$ is the shape parameter of the ideal tetrahedron at
cusp $k$ and $\mu_k, \lambda_k$ are its meridian and longitude.*

## Algebraic poles as geometric addresses

The conjecture says the **algebraic denominator zeros are the
addresses of the geometric cusps**: a zero in the algebraic state
sum at $x = q_0^{-k}$ corresponds to the geometric requirement that
parallel transport around the meridian and longitude of the $k$-th
ideal-tetrahedron cusp yields a holonomy of exactly $1$. Algebraic
divergence and geometric completeness are the same event, viewed
from opposite sides of the Archimedean fibre functor $\tau$.

| Algebraic side ($R$) | Archimedean side ($\mathbb{C}$) | Geometric side ($\mathbf{Hyp}_3$) |
|---|---|---|
| zero of $(1 - x q_0^k)$ | logarithmic singularity of $\mathrm{Li}_2$ | meridian + longitude holonomy = $1$ |
| pole of $\Phi_n$ | branch point of $\log$ | complete cusp of $\Delta_{z_k}$ |
| algebraic Markov-trace divergence | $\tau_{\mathrm{arch}}$-evaluation diverges | shape parameter $z_k$ on Thurston variety |
| GB-depth $k_\star = n$ | thimble dimension $n$ | $n$ ideal tetrahedra in JSJ piece |

The bijection across rows is the **shared denominator**: the same
polynomial $(x; q_0)_n$ controls the algebraic singularities, the
classical $\mathrm{Li}_2$ branch structure, and the Thurston cusp
equations.

## Proof sketch (modulo the upstream conjectures)

Assume
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)).

1. **Algebraic side** ([q-Pochhammer partial product §interpretation](#def:q-pochhammer-partial-product)).
   The denominator $(x; q)_n$ has $n$ simple zeros at $x = q^{-k}$
   for $k = 0, \dots, n-1$. Each is a simple pole of $\Phi_n(x; q)$.

2. **Archimedean side** ([Archimedean limit](#conj:dilogarithm-archimedean-limit)).
   Under Faddeev's scaling, $(1 - q) \log \Phi_n(x; q) \to
   \mathrm{Li}_2(x)$. The poles of $\Phi_n$ map to the logarithmic
   branch point of $\mathrm{Li}_2$ at $t = 1$ in the integrand
   $-\log(1 - t)/t$.

3. **Geometric side** (Thurston [`thurston1978`], Neumann–Zagier
   [`neumann-zagier1985`]). For an ideal-tetrahedron triangulation of
   a hyperbolic 3-manifold, the **cusp completeness conditions** are
   $\mathrm{Hol}_\mu = \mathrm{Hol}_\lambda = 1$ on the meridian and
   longitude; equivalently, the Neumann–Zagier potential
   $\Phi_{\mathrm{NZ}}(z)$ has a critical point at $z = z_k$ matching
   the corresponding shape parameter.

4. **Bridge.** Under the
   [algebraic-geometric equivalence](#conj:algebraic-geometric-dilog-equivalence)'s
   pole-to-cusp bijection, the algebraic root $x = q_0^{-k}$ matches
   cusp $k$, and Step 2 identifies the singularity of the algebraic
   $\Phi_n$ with the singularity of $\mathrm{Li}_2$ at $z_k$ — which
   by Step 3 is the cusp-completeness condition. $\square$

## Implication for the Newton–Raphson solver

The conjecture has a **direct computational consequence**: the zeros
$\{q_0^{-k}\}$ of the algebraic denominator are the **exact initial
seed values** for the Newton–Raphson solver of the Thurston gluing
equations on the active JSJ piece. The pipeline is:

1. The algebraic engine computes $\Phi_n(x; q_0)$ as a rational
   function.
2. Extract the $n$ roots of its denominator $(x; q_0)_n$:
   $\{q_0^{-k} : k = 0, \dots, n-1\}$.
3. Pass the roots across the WASM boundary to the SnapPy kernel.
4. Use the roots not as a universal constant but as the **initial
   guesses** for the Newton–Raphson solver.

By Steps 1–4 of the proof sketch above, the algebraic seeds sit
**near** the cusp-completeness solution of the Thurston gluing
equations — only the gluing residuals from the active transient
crossings differ from zero. The solver converges in $O(1)$ Newton
steps per cusp (empirically $\approx 10$ steps to machine precision
across depths $n = 1, \dots, 3$, see witness below), instead of the
$O(\log\epsilon^{-1})$ steps needed when starting from a generic
universal $z_q$. The Newton step also avoids local-minimum traps,
because the algebraic poles are **isolated** in the cusp variety.

The witness
[q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json)
drives Newton–Raphson on the color-tube discriminant $\Delta(z) = 0$
from each algebraic seed (perturbed by $0.1i$ to enter $\mathbb{C}$).
At depths $n = 1, 2, 3$, all seeds converge to a complex critical
point with residual $\lesssim 10^{-13}$ in 9–11 iterations,
empirically supporting the $O(1)$ claim.

## Relation to existing PL/JSJ infrastructure

This conjecture is the **shared-denominator** statement that the
existing
([Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge)) already
asserts implicitly: the JSJ piecewise sum
$\sum_S \mathrm{Vol}(K_S)$ is computed from the algebraic
$\sum_S \Phi_q(\lvert V_S\rvert)$ at exactly the cusps prescribed by
the algebraic denominators. Phrased motivically, the algebraic class
$[\Phi_n(x; q_0)] \in \mathfrak{B}(q)$ in the
([quantum Bloch group](#def:quantum-bloch-group))
regulates archimedeanly to the volume of the matched JSJ piece, with
the regulator's domain of definition pinned by the shared-denominator
locus.

## Discussion

Stated conditional on
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence))
and
([Archimedean limit](#conj:dilogarithm-archimedean-limit)). The Lean
formulation
`QOU.QPochhammer.shared_denominator_cusp_holonomy` is therefore a
class instance, not a closed theorem.

### Empirical scope of the seeding pipeline

Two computational witnesses bracket the conjecture's strong form:

- **Color-tube cubic** (succeeds):
  [q-pochhammer-seed.witness.json](../../../computations/q-pochhammer-seed.witness.json)
  drives Newton–Raphson on $\Delta(z) = 0$ from the algebraic seeds
  $q_0^{-k} + 0.1i$. At depths $n \leq 3$, Newton converges to
  machine-precision residual ($\lesssim 10^{-13}$) in 9–11 iterations,
  empirically supporting the $O(1)$-steps-per-cusp prediction.

- **SnapPy Thurston gluing system** (bounds the strong form):
  [snappy-cusp-seeding.witness.json](../../../computations/snappy-cusp-seeding.witness.json)
  measures the distance between the bare algebraic seeds and SnapPy's
  tetrahedral shape parameters for $\mathtt{m004}$, $\mathtt{m003}$,
  and the Borromean rings $\mathtt{L6a4}$. The bare seeds sit at
  distance $\sim 0.4$–$0.9$ from SnapPy's $z_k$, so the pole-to-cusp
  bijection cannot be a literal canonical identity
  $q_0^{-k} = z_k$. The conjecture must be interpreted as a bijection
  of **labels** (algebraic-pole index $\leftrightarrow$ cusp index)
  with the actual shape parameter being a non-trivial function
  $\tau_{\mathrm{arch}}(q_0^{-k})$ of the algebraic seed; the shape
  of that function is the subject of further work.

The two witnesses together support the conjecture's *structural*
content (algebraic poles label cusps) while bounding its *canonical*
form (the bare $q_0^{-k}$ are not literally the cusp shapes).
<!-- FILE_END: shared-denominator-cusp-holonomy.md -->

<!-- FILE_START: quantum-bloch-group.md -->
The classical Bloch group $\mathcal{B}(\mathbb{C})$ is
defined by the five-term relation of the dilogarithm
$\mathrm{Li}_2$.  The **quantum Bloch group**
$\mathfrak{B}(q)(R)$ replaces this with the **pentagon
identity** of the quantum dilogarithm $\Phi_q$:

$$
  \Phi_q(u)\,\Phi_q(v)
  \;=\;
  \Phi_q(v)\,\Phi_q(uv)\,\Phi_q(u)
  \qquad \text{where } uv = qvu
$$

This identity is the **Yang–Baxter equation in
exponential form**.  The connection to our framework:

1. The braid group $B_n$ is generated by the Yang–Baxter
   equation $\sigma_i\sigma_{i+1}\sigma_i =
   \sigma_{i+1}\sigma_i\sigma_{i+1}$.

2. The Hecke relation $\sigma_i^2 = H_A\sigma_i + 1$ is
   the **linearisation** of the quantum pentagon identity.

3. The traced volumes $\hat{V}_i(q)$ satisfy the Hecke
   relation because they are matrix elements of
   $\rho(\sigma_i)$ in the standard representation.

4. The algebraic quantum volume
   $\mathrm{Vol}_q = \prod \hat{V}_i$ therefore satisfies
   the pentagon identity (multiplicatively), and its
   logarithm $\Phi_1 = \tfrac{1}{2}\sum \ln(\hat{V}_i \cdot \overline{\hat{V}_i})$ satisfies the
   five-term relation (additively).

This explains **why** $\Phi_1$ is a quantum dilogarithm:
the traced volumes are exponentials of quantum dilogarithm
values, and their product lives in the quantum Bloch group.
The regulator map $\mathfrak{B}(q) \to \mathbb{R}$ sends
the algebraic volume to the hyperbolic volume, recovering
$\mathrm{Vol}(S^3 \setminus K)$ from the algebraic data.

The **Kashaev invariant** is the state sum version:
$\langle K \rangle = \sum_j \prod_{\text{tetrahedra}}
\Phi_q(x_j)^{\pm 1}$, living in the Habiro ring.  For the
Borromean rings, this gives $\langle \mathcal{B}_3 \rangle$
whose archimedean evaluation yields $8G$.

## Pre-archimedean side: $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$

The quantum Bloch group $\mathfrak{B}(q)$ has a natural
**pre-archimedean refinement** over the Habiro ring
$\widehat{\mathbb{Z}[q]}$ (Habiro 2002), without passing through
the complex numbers:

| Side | Bloch group | Regulator $\Phi_1$ | Where |
|------|-------------|---------------------|-------|
| **Pre-archimedean** | $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$ | $\tfrac{1}{2}\sum \ln(\hat{V}_i \cdot \overline{\hat{V}_i})$ | Habiro ring; bar = $q \leftrightarrow q^{-1}$ |
| **Archimedean** ($\tau_{\mathrm{arch}}$ at real $q_0$, real $\hat{V}_i$) | $\mathcal{B}(\mathbb{C})$ | $\sum \ln\lvert\hat{V}_i\rvert$ | Borel regulator $r_1: K_1(\mathbb{C}) \to \mathbb{R}$ |

The bar-involution form $\tfrac{1}{2}\ln(V \cdot \overline{V})$ at
the pre-archimedean level is what the framework uses for $\rho_K$'s
single-generator piece (`[prop:rho-k-graded-expansion`](rho-k-graded-expansion.md)).
At the archimedean specialization with real $q_0$ and real $\hat{V}_i$,
this reduces to the classical Borel regulator $\sum \ln\lvert\hat{V}_i\rvert$ —
the form that appears in
[`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md)
under the Beilinson regulator $r_2: K_3(\mathbb{C}) \to \mathbb{R}$.

This makes the QOU framework's K-theoretic content categorically
explicit: $\rho_K$ is a graded regulator on $\mathfrak{B}(\widehat{\mathbb{Z}[q]})$
whose archimedean evaluation at $q_0 \in \mathbb{R}_{>1}$ recovers the
classical hyperbolic K_3 regulator. The pre-archimedean form respects
the Hecke bar-involution; the archimedean form respects the standard
$\mathbb{R}$-valued K-theory.

This refines the discussion in
[`conj:borromean-bloch-group-element`](borromean-bloch-group-element.md):
the framework's working object is the **pre-archimedean
$\mathfrak{B}(\widehat{\mathbb{Z}[q]})$**, and the Beilinson regulator
$r_2$ is the archimedean realization of the graded $\rho_K$.
<!-- FILE_END: quantum-bloch-group.md -->

<!-- FILE_START: degree-two-baryon-weight.md -->
*The coefficient of $\Phi_2$ in the Wedderburn mass formula is*

$$
  \beta_2 = -2[3]_q
          = -2 \cdot \frac{q^3 - q^{-3}}{q - q^{-1}}
          \approx -6.087
$$

*where $[3]_q$ is the quantum 3-integer.*
<!-- FILE_END: degree-two-baryon-weight.md -->

<!-- FILE_START: borromean-bloch-group-element.md -->
**Conjecture (D16 K-theoretic / Bloch-group closure).**
*The Borromean rings complement $\mathbf{S}^3 \setminus \mathcal{B}_3$
defines a non-trivial element $[\mathcal{B}_3] \in K_3(\mathbb{C})$
(equivalently, an element of the Bloch group $B(\mathbb{C})$) whose
**Beilinson regulator $r_2: K_3(\mathbb{C}) \to \mathbb{R}$ evaluates
to** $\mathrm{Vol}(\mathcal{B}_3) = 8G$.  The Markov-trace coefficient
$h^4 = -3/4$ of $\mathrm{tr}_M(\mathcal{B}_3, q)$ has a K-theoretic
shadow as the next-order regulator term: $r_2[\mathcal{B}_3] \cdot
(h^4\text{-coefficient}) = (8G)(-3/4) = -6G$.*

## The K-theoretic structure

The Bloch group $B(F)$ of a field $F$ is generated by symbols
$[z]$ for $z \in F \setminus \{0, 1\}$ modulo the **5-term
relation**

$$
  [x] + [y] + [1 - xy] + \bigl[\tfrac{1 - x}{1 - xy}\bigr] + \bigl[\tfrac{1 - y}{1 - xy}\bigr]
  \;=\;
  0,
$$

which IS the Bloch-Wigner / Rogers Pentagon identity for the
dilogarithm.  Bloch–Suslin showed $B(\mathbb{C}) \otimes \mathbb{Q}
\cong K_3^{\text{ind}}(\mathbb{C}) \otimes \mathbb{Q}$.

The **Beilinson regulator** $r_2: B(\mathbb{C}) \to \mathbb{R}$ is
given by the Bloch-Wigner dilogarithm:

$$
  r_2([z]) \;=\; D(z)
  \;=\;
  \mathrm{Im}\,\mathrm{Li}_2(z) + \log|z| \cdot \arg(1 - z).
$$

For an ideal tetrahedron with cross-ratio $z$, the hyperbolic volume
is $\Lambda(\theta) = D(e^{i\theta})/2 = \mathrm{Im}\,\mathrm{Li}_2(e^{i\theta})$
— the **Lobachevsky function**.  So hyperbolic volume IS a regulator
evaluation, per
[`rem:vol-as-motivic-period`](#rem:vol-as-motivic-period).

## The Borromean Bloch-group element

Per
[`def:quantum-bloch-group`](#def:quantum-bloch-group) and the
classical Bloch-Suslin construction:

- The Borromean complement decomposes into 8 ideal octahedra, each
  with cross-ratio $\zeta = e^{i\pi/3}$ (the regular ideal
  octahedron, $\theta = \pi/3$).
- Each octahedron contributes Bloch-group element $8 \cdot
  [\zeta]_2 + \ldots$ via the Lobachevsky decomposition.
- The total Bloch-group element is

$$
  [\mathcal{B}_3]_{B(\mathbb{C})}
  \;=\;
  8 \cdot [e^{i\pi/3}]
  \;\in\;
  B(\mathbb{C}),
$$

with regulator $r_2[\mathcal{B}_3] = 8 \cdot \Lambda(\pi/3) =
8G$ (Catalan's constant; see
[`prop:binding-scale-catalan`](#prop:binding-scale-catalan)).

## The conjectural content — $h^4$ as the next-order regulator term

The Beilinson regulator extends to higher orders via the formal
$q$-expansion of $\Phi_q$ around $q = 1$ (the archimedean limit per
[`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)):

$$
  \log \Phi_q(z)
  \;=\;
  \frac{1}{q - 1}
  \bigl(
    \mathrm{Li}_2(z) + h \cdot R_1(z) + h^2 \cdot R_2(z) + \cdots
  \bigr),
$$

where $R_k(z)$ are higher-Bloch regulators.  The conjecture is:

$$
  \frac{r_2^{(2)}[\mathcal{B}_3]}{r_2[\mathcal{B}_3]}
  \;=\;
  h^4 \text{ coefficient of } \mathrm{tr}_M(\mathcal{B}_3, q)
  \;=\;
  -\frac{3}{4},
$$

where $r_2^{(2)}$ is the order-$h^2$ correction to the leading
$r_2$ regulator.  Equivalently: $r_2^{(2)}[\mathcal{B}_3] = -6G$.

## Significance

Per
[`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
§3 (Cluster C of the duality tracker), four candidate routes for
deriving $h^4 = -3/4$ categorically:

1. **Direct Borromean Markov trace** — already done
2. **Pachner-Pentagon state-sum** —
   [`conj:pachner-pentagon-borromean`](pachner-pentagon-borromean.md) (D15, sibling)
3. **K-theoretic / Bloch group regulator** (this conjecture, D16)
4. **DIM-master Pentagon** — research-grade

Closing D16 ties $h^4$ to the K-theoretic structure of $K_3(\mathbb{C})$
— the deepest connection to motivic / arithmetic structure.  It
also closes the loop:

- $r_2$ at order $h^0$ = $8G$ (the bare hyperbolic volume = production
  $\mathrm{Vol}(\mathcal{B}_3)$ in the canonical formalism),
- $r_2^{(2)}$ at order $h^4$ = $-6G$ (the Markov-trace coefficient),
- $r_2^{(k)}$ at higher orders — the full Markov-trace closed form.

## Diagnostics

Per [`.claude/skills/local/canonical-watcher.md`](../../../.claude/skills/local/canonical-watcher.md) §Slot J:

- **GB filtration level**: N/A — the Bloch group lives at the
  decategorified level (image of $K_3(\mathbb{C})$ in $\mathbb{R}$);
  no Coxeter length attaches naturally.
- **Jet order**: $h^4$ (the load-bearing claim is at the next-order
  regulator level beyond the $h^0$ volume).
- **Bar-symmetry status**: bar-symmetric.  The Beilinson regulator
  $r_2[z] = \mathrm{Im}\,\mathrm{Li}_2(z) + \ldots$ is bar-symmetric
  under $q \mapsto q^{-1}$ because $\mathrm{Li}_2^q$ is bar-symmetric
  (per [`bar-involution.md`](bar-involution.md) Table 2 — Rogers
  q-dilog is bar-symmetric, Faddeev's $\Phi_q$ alone is bar-anti-
  symmetric).

## Lean axiomatisation (sketch)

```lean
class BorromeanBlochGroupElement
    (M : Type*) [BrCategory M] [QuantumDilogarithm M] where
  /-- The Bloch-group element of the Borromean complement. -/
  borromean_bloch_class : BlochGroup (Complex)
  /-- It equals 8 · [e^(iπ/3)]. -/
  borromean_bloch_eq_eight_xi :
    borromean_bloch_class = 8 • bloch_symbol (Complex.exp (Complex.I * π / 3))
  /-- The Beilinson regulator of the class equals 8G. -/
  regulator_eq_eight_G : r_2 borromean_bloch_class = 8 * catalan_G
  /-- The order-h² regulator correction equals -6G. -/
  regulator_h2_correction : r_2_h2_correction borromean_bloch_class = -6 * catalan_G
  /-- Equivalently, the h^4 Markov-trace coefficient = -3/4. -/
  borromean_h4_coefficient_from_regulator :
    markov_trace_h4_coefficient borromean_complement = -3/4
```

## Open R&D

1. **Compute prototype**: at $q = q_0$, canonical evaluate both
   sides of the conjectural identity
   $r_2^{(2)}[\mathcal{B}_3] = -6G$.  The left side requires
   extending the Bloch-Wigner regulator to order $h^2$ via the
   $\Phi_q$ formal expansion; the right side is already in
   [`borromean-markov-trace-closed-form.md`](#prop:borromean-markov-trace-closed-form).
2. **D16 to closed** requires the Lean class instance + the
   `borromean_h4_coefficient_from_regulator` proof (which would
   import a Bloch-Suslin lemma from Mathlib once available; per
   `lean_loogle` search, $K_3$ formalisation is currently partial in
   Mathlib).
3. **Cross-validate against D15**: the Pachner-Pentagon state-sum
   and the K-theoretic regulator should both give $h^4 = -3/4$ —
   a triple cross-validation of the topological coefficient.

## Cross-references

- [`docs/duality-tracker.md`](../../docs/duality-tracker.md) §1 D16
  + §2 Cluster C (Pentagon validation D15-D18)
- [`docs/audits/-pentagon-identity-broad-context.md`](../../docs/audits/-pentagon-identity-broad-context.md)
  — Pentagon literatures + 4 candidate routes for $h^4 = -3/4$
- Sibling Cluster C item:
  [`conj:pachner-pentagon-borromean`](pachner-pentagon-borromean.md) (D15)
- The quantum Bloch group:
  [`def:quantum-bloch-group`](#def:quantum-bloch-group)
- The motivic-period framing:
  [`rem:vol-as-motivic-period`](#rem:vol-as-motivic-period)
- The volume = regulator identity:
  [`prop:vol-through-tau`](#prop:vol-through-tau),
  [`prop:binding-scale-catalan`](#prop:binding-scale-catalan)
- The archimedean dilog limit:
  [`conj:dilogarithm-archimedean-limit`](#conj:dilogarithm-archimedean-limit)
- The Kashaev volume conjecture (upstream):
  [`conj:kashaev-volume-conjecture`](kashaev-volume-conjecture.md)
<!-- FILE_END: borromean-bloch-group-element.md -->

