<!-- FILE_START: intro-mutant-jones-bloch-group.md -->
The Jones polynomial fails to distinguish mutant knots, notably the Conway and Kinoshita-Terasaka pair. However, the substrate-level Hecke framework tracks refined invariants beyond the closure trace. This section applies the mutant pair as a critical falsifiability test. We identify the Bloch-group closure as the exact categorical mechanism resolving mutant ambiguity.

The sequence maps the bi-filtration grid that categorically separates mutants, tests the substrate invariant against the canonical mutant pair, and connects this separation directly to the Bloch-group quotient. This yields the strongest falsifiability target in the chapter: a precise geometric divergence where the standard polynomial evaluates identically.
<!-- FILE_END: intro-mutant-jones-bloch-group.md -->

<!-- FILE_START: knot-indexed-convolution-grid.md -->
**Proposition (knot-indexed convolutions).**
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
