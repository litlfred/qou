The two hypotheses of the
[archimedean functor uniqueness theorem](#prop:archimedean-functor-uniqueness)
are its only unproved inputs; both are well-established results in the
literature (on the dilogarithm, the Bloch group and the Suslin map) and
enter as cited inputs.

## Pre-archimedean / archimedean separation

The QOU substrate is pre-archimedean: every block in the
[motivic substrate](#def:motivic-substrate) and the
[algebraic quantum volume](#def:algebraic-quantum-volume) lives
in $R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$, a ring of
Laurent polynomials with no real-analytic transcendentals. QOU
observables — masses, binding energies, the fine-structure
constant — are real numbers, and the only exit from $R$ to
$\mathbb{R}$ is the archimedean realization functor
$\tau_{\text{arch}}$.

Two structural questions are settled simultaneously by Bloch-Suslin
pentagon-uniqueness. (i) *Uniqueness of the exit*: any real-valued
continuous functional on $B(\mathbb{C})$ respecting the 5-term
pentagon identity is forced to coincide with $D$ up to a single
overall scalar; therefore the archimedean image of a substrate
motivic class is canonical. (ii) *Provenance of $\pi$*: any
transcendental constant in a QOU observable is the
$\tau_{\text{arch}}$-image of substrate pentagon data via $D$ (or
its multivariate generalisations), and is therefore not an external
import. The additive Bring zero-mode candidate
[Additive Bring zero-mode form $1/\alpha_{EM} = q\cdot[9]_q\cdot[10]_q + 2g/(4\pi(g-1))$ (conditional)](#prop:em-coupling-bring-zero-mode)
illustrates the second point: the $2/(3\pi) = 2g/(4\pi(g-1))$
correction at $g = 4$ is the archimedean shadow of pentagon
data on Bring's surface, not a $\pi$-import outside $R$.

The algebraic / archimedean dichotomy establishes a clean separation between categorical structure and continuum measurement. The mass formula evaluates a closed cycle on the Frobenius-Hopf substrate. The non-degenerate Frobenius pairing $\int_A \circ \mu$ identifies $A \cong A^\vee$, making the substrate algebra self-dual. This self-duality drives the descent involution $\hat{\tau}_n$ on the endomorphism algebra, which splits the categorical mass endomorphism into a descended baseline component and a transient component localized at the exceptional divisors of the brane tower.

Within this purely algebraic substrate, the mass evaluation yields the algebraic quantum volume:

$$
  \mathrm{Vol}_q(\beta) \;=\; \prod_{i=0}^{A-2}\hat{V}_i(q),
  \qquad \hat{V}_i(q) \in \mathbb{Z}[q^{\pm 1/2}],
$$

a finite product of Laurent polynomials living strictly in $\mathbb{Z}[q^{\pm 1/2}]$. This domain is categorical and discrete: devoid of $\pi$, $\zeta(3)$, or real-analytic transcendentals.

Transcendental numbers enter the framework exclusively at the boundary of observation. The functor $\tau_{\text{arch}}$ projects categorical data into physical spacetime by taking the absolute logarithm of the algebraic quantum volume. This functor converts the discrete Hecke algebra states into continuous observables.

To satisfy the Descartes condition $\chi = -6$, the physical state space restricts to Bring's surface, a genus-$4$ curve with maximal $S_5$ automorphism. The observable particle spectrum consists entirely of knots that embed within this genus-$4$ handlebody. After applying $\tau_{\text{arch}}$, the Kashaev volume conjecture identifies the limit of the algebraic state sum with the classical hyperbolic volume of these specific knot complements. In this limit, the quantum dilogarithm $\Phi_q(z_i)$ evaluated at each exceptional divisor degenerates into the Bloch-Wigner dilogarithm $D(z_i)$. The Bloch-Wigner dilogarithm is uniquely characterized as the function satisfying the 5-term pentagon identity, providing the exact geometric measure of the ideal tetrahedra that triangulate the knot complement.

## Corollaries

**(a) Resolves the pre-archimedean concern in
[Additive Bring zero-mode form $1/\alpha_{EM} = q\cdot[9]_q\cdot[10]_q + 2g/(4\pi(g-1))$ (conditional)](#prop:em-coupling-bring-zero-mode).**
The $\pi$ in the additive correction $2/(3\pi) = 2g/(4\pi(g-1))$
at $g=4$ is the unique archimedean shadow of pentagon-coherent
substrate data on Bring's surface. The substrate's pentagon
coherence forces the archimedean image to involve $D$ (and hence
$\pi$ via $D$'s functional equation); no other transcendental
shape is admissible. The additive correction is therefore *not*
outside $R$ — it is the canonical $\tau_{\text{arch}}$-image of
$R$-internal pentagon data.

**(b) Forecloses arbitrary $\pi$-imports.** Any candidate closed
form for a QOU observable that includes a transcendental constant
not derivable from $D$ (or its multivariate generalisations
$D_n$) is excluded. This is a falsifiability constraint: the
multiplicative gluon-octet form (a PSLQ-empirical candidate, which
[Additive Bring zero-mode form $1/\alpha_{EM} = q\cdot[9]_q\cdot[10]_q + 2g/(4\pi(g-1))$ (conditional)](#prop:em-coupling-bring-zero-mode) replaces)
required arbitrary integer ratios $45 \cdot [3]_q \cdot
(1+\delta_{CS}+8q\delta_{CS}^2)$ that would have to come from a
non-pentagon source, is ruled out *structurally* in addition to
the existing PSLQ ruling.

**(c) Pins the figure-8 knot example.** The figure-8 knot $4_1$
embeds smoothly into Bring's surface as the amphichiral mass
mechanism. On the pre-archimedean side it has a rigorous
motivic / algebraic representation via its Hecke normal form in
$\mathbb{Z}[q^{\pm 1/2}]$. Once $\tau_{\text{arch}}$ maps this
motivic state into the observable continuum, its hyperbolic volume
realizes as the transcendental
$\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx {{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}$. The
motivic side guarantees exact algebraic relationships governing
particle interactions; $\tau_{\text{arch}}$ supplies the
transcendental continuum required for geometric measurement. See
[figure-8 archimedean illustration](#rem:figure-8-archimedean-illustration).

## Open problems

1. **K-theoretic identification.** Make the Bloch-group factoring
   of the QOU mass-formula state sum precise: which class in
   $K_3^{\text{ind}}(\mathbb{C})$ does an $A$-strand braid $\beta$
   represent? Conjecturally, the class is read off from the
   Yekutieli triple data; making this rigorous requires identifying
   the $J^2$-jet of the cosimplicial structure with a Bloch-group
   1-cocycle.
2. **Multivariate Bloch-Suslin.** For mass-tower contributions
   spanning multiple exceptional divisors, the relevant invariant
   is the higher Bloch group $B_n(\mathbb{C})$ with the
   $n$-variable polylogarithm $D_n$. Pentagon-uniqueness for
   $D_n$ at $n \geq 3$ is open in the literature (Goncharov 1995
   conjectures); the QOU framework can take it as input where
   needed.
3. **Suslin's theorem as a cited input.** The result of
   \cite{suslin1991} is used as a cited input and is not proved
   here.

## Witness

No canonical witness is appropriate for a uniqueness claim. The
relevant cross-check is that any new closed form for a QOU
observable proposed in this repository must be expressible as a
$\tau_{\text{arch}}$-image of a pentagon-coherent
$R$-internal class, or equivalently, must factor through $D$ (or
$D_n$) in its archimedean expansion. The
[`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
candidate satisfies this; the gluon-octet PSLQ candidate does not.
