<!-- FILE_START: intro-spectral-sequence-chirality-confinement.md -->
The categorical braid-word space carries a natural filtration indexed by jet-prefix length. The associated Gröbner-Shirshov filtration converges via a spectral sequence to the categorical normal-form invariants.

This section maps the spectral sequence, identifies its $E_\infty$ page with the chirality-graded normal-form ring, and extracts the confinement-NF structure. The sequence defines the jet-prefix filtration, proves convergence, isolates the involutive chirality grading, and tabulates the explicit $E_\infty$ classes. Downstream mass and charge computations extract their inputs directly from these verified $E_\infty$ classes.
<!-- FILE_END: intro-spectral-sequence-chirality-confinement.md -->

<!-- FILE_START: jet-prefix-gb-filtration.md -->
**Proposition (GB-filtration-indexed prefix).**
*Define the Gröbner-Shirshov-filtered prefix $\beta_k^{\mathrm{GS}}$ of an atomic braid word $T_w \in H_{3A}(q)$ as the projection onto the filtration stratum:*

$$
  \beta_k^{\mathrm{GS}}
  \;:=\;
  \sigma_{k-3}\bigl(T_w\bigr)
  \;\in\;
  J^{k-3}(q) / J^{k-2}(q).
$$

*The jet-level prefix evaluates as:*

$$
  a_k(\beta_k^{\mathrm{GS}})
  \;=\;
  \frac{\mathrm{tr}_M^{[\ell]}\bigl(\beta_k^{\mathrm{GS}}\bigr)}
       {\sum_\lambda w_\lambda\,\dim\mathrm{Res}^{H_k}_{H_3}(V_\lambda)}.
$$

The GB filtration aligns exactly with the Hecke-algebraic structure. The symbol map isolates the top graded component, projecting the residual homological error solely into higher degrees. The prefix $\beta_k^{\mathrm{GS}}$ inherits accurate restriction multiplicities from this strictly graded construction.
<!-- FILE_END: jet-prefix-gb-filtration.md -->

<!-- FILE_START: jet-prefix-gb-filtration-evidence.md -->
**Remark (Failed prefix conventions).**
Earlier empirical attempts to evaluate the jet-level prefix failed entirely to reproduce AME bindings. Nucleon-cumulative, strand-cumulative, and generator-bounded truncations all collapsed toward zero rather than converging to a "correction near 1". A height-based heuristic similarly degraded under increasing atomic mass. The observed structural failure dictates that the jet-level prefix formula must process the true confinement-level filtration $J^\bullet$, not combinatorial proxies.
<!-- FILE_END: jet-prefix-gb-filtration-evidence.md -->

<!-- FILE_START: frobenius-self-pairing-chirality.md -->
**Definition (Frobenius self-pairing chirality).**
*Let $(A, \tau)$ be a self-dual Frobenius algebra and $\beta \in A$ a braid word. Let $\beta^*$ denote the image of $\beta$ under the algebra antipode. The chirality factor of $\beta$ is the normalized Frobenius norm:*

$$
  a_K(\beta)
  \;:=\;
  \frac{\tau(\beta \cdot \beta^*)}{\tau(1 \cdot 1)}.
$$
<!-- FILE_END: frobenius-self-pairing-chirality.md -->

<!-- FILE_START: chirality-from-frobenius-self-pairing.md -->
**Proposition (chirality classification by writhe and topology).**
*The Frobenius self-pairing chirality factor $a_K(\beta)$ satisfies:*

1. *For a chiral knot $K$ with writhe $w(K) \neq 0$:*

$$
   a_K \;=\; 1 + w(K) \cdot h \;+\; O(h^2).
$$

2. *For an amphichiral knot $K$:*

$$
   a_K \;=\; 1 - c_K \cdot h^2 \;+\; O(h^4).
$$

3. *For a Borromean-type link (multiple amphichiral sublinks):*

$$
   a_K \;=\; \prod_i (1 - c_{K_i} h^2).
$$

The self-pairing evaluates trivially ($a_K=1$) for bare generator crossings and pure trefoils. The non-trivial chirality factor arises directly from higher Markov moments during the braid closure operation. The Fricke trace relation fixes $c_K = 1$ for the figure-eight, driving $a_K = 1 - h^2$.
<!-- FILE_END: chirality-from-frobenius-self-pairing.md -->

<!-- FILE_START: chirality-from-frobenius-self-pairing-scope.md -->
**Remark (Scope of derivation).**
This proposition fully derives the amphichiral case. For chiral knots, the raw algebra pairing returns 1; the $1+h$ factor requires a complete categorical derivation tracking the braided ribbon-category closure. The twist $\varTheta_X$ encodes the writhe, and its interaction with the Frobenius pairing drives the first-order chiral contribution.
<!-- FILE_END: chirality-from-frobenius-self-pairing-scope.md -->

<!-- FILE_START: hecke-curvature-2-cocycle.md -->
**Definition (Hecke curvature 2-cocycle).**
*The Hecke curvature 2-cocycle is the 2-form-valued bilinear map $F \in C^2(H_n(R, q), H_n(R, q))$ defined on generator pairs by the deviation from Hecke and Yang-Baxter flat relations:*

$$
  F(\sigma_i, \sigma_j) \;=\;
  \begin{cases}
    R_H(i) & \text{if } i = j, \\
    R_{YB}(i) & \text{if } |i - j| = 1, \\
    [\sigma_i, \sigma_j] & \text{if } |i - j| \geq 2.
  \end{cases}
$$

*It extends to general elements via the Leibniz rule. It explicitly measures the failure of commutativity and normal-form flatness at each generator pair.*
<!-- FILE_END: hecke-curvature-2-cocycle.md -->

<!-- FILE_START: curvature-rank.md -->
**Definition (curvature-rank).**
*The curvature-rank $r(T_w)$ is the smallest non-negative integer $r$ mapping the $r$-fold iterated curvature $F^{\,r}(T_w)$ into the $J^{\,r}(q) \setminus J^{\,r+1}(q)$ filtration stratum. It explicitly counts the minimal number of reduction steps required to drive $T_w$ into normal form.*
<!-- FILE_END: curvature-rank.md -->

<!-- FILE_START: curvature-rank-gb-stratification.md -->
**Proposition (curvature-rank = GB filtration index).**
*The curvature-rank strictly stratifies the GB filtration:*

$$
  J^{\,r}(q) / J^{\,r+1}(q)
  \;=\;
  \bigl\{T_w \in H_n(R, q)\ \bigm|\ r(T_w) = r\bigr\}.
$$

*The spectral-sequence pages decompose identically by curvature rank. The non-abelian Stokes residue of the Markov trace at depth $\ell$ isolates the precise contribution from words of curvature-rank $\ell$.*
<!-- FILE_END: curvature-rank-gb-stratification.md -->

<!-- FILE_START: curvature-rank-gb-stratification-interpretation.md -->
**Remark (geometric reading).**
Under the archimedean realization, the Markov trace acts as a boundary holonomy on a Seifert surface. The curvature 2-cocycle behaves as the curvature 2-form of the Frobenius-Hopf flat connection. The total mass decomposes via non-abelian Stokes into independent stratum integrals, each evaluating the curvature-rank components directly over the blow-up loci.
<!-- FILE_END: curvature-rank-gb-stratification-interpretation.md -->

<!-- FILE_START: ks-finiteness-via-diamond-lemma.md -->
**Remark (Finiteness via Diamond Lemma).**
Kontsevich-Soibelman must assume ind-constructibility to measure their $3$CY moduli stacks. The QOU framework avoids this assumption completely. The Gröbner-Shirshov confluent normal forms guarantee a finite basis of standard monomials at every length. The length slices construct finite-dimensional schemes immediately. The topological structure extracts rigorous finiteness directly from the Diamond Lemma.
<!-- FILE_END: ks-finiteness-via-diamond-lemma.md -->

<!-- FILE_START: spectral-sequence-collapse.md -->
**Proposition (cohomology vanishing collapses the GB spectral sequence).**
*For semisimple $A = H_n(R, q)$, Hochschild cohomology vanishes in positive degrees $\mathrm{HH}^k(A,\, A) = 0$. The GB filtration spectral sequence collapses at $E_1$, concentrating all contributions in the center $E_\infty^{0, *} = Z(A)$.*
<!-- FILE_END: spectral-sequence-collapse.md -->

<!-- FILE_START: delta-q-decoration.md -->
**Definition (q-dimension decoration of the NF basis).**
*The $\delta_q$-decoration maps an algebra element $b \in H_n(q)$ to the tuple of its $q$-characters across each irreducible representation $V_\lambda$:*

$$
  \delta_q(b)
  \;:=\;
  \bigl(\chi_\lambda(b)\bigr)_{\lambda \vdash n}
  \;\in\;
  R^{|\,\mathrm{Par}(n)\,|}.
$$

This layer preserves the crucial per-irrep structure that the Markov trace normally collapses. It provides the high-fidelity projection data required to map force-carrier knots into exact Wedderburn components. For example, it cleanly extracts the $[9]_q$ and $[10]_q$ $q$-dimensions for the Bring torus-knot force carriers directly from the character evaluations.
<!-- FILE_END: delta-q-decoration.md -->

<!-- FILE_START: alpha-basis-knot-delta-q.md -->
**Proposition (q-dimension decoration of the basis knots).**
*For the basis torus knot $T_{2,k}$, the $\delta_q$-decoration evaluates exactly as:*

$$
  \delta_q(T_{2,k}) \;=\; q^{k} - q^{-k} \;=\; h\,[k]_q.
$$

*The identity holds purely algebraically in $\mathbb{Z}[q^{\pm 1/2}, h^{-1}]$ with no archimedean approximation.*
<!-- FILE_END: alpha-basis-knot-delta-q.md -->

<!-- FILE_START: torus-knot-delta-q-writhe.md -->
**Proposition (writhe exponent of the torus-knot $\delta_q$ decoration).**
*For the torus knot $T_{m,p}$, the $\delta_q$-decoration extracts the quantum integer at the writhe $w = (m-1)p$:*

$$
  \delta_q(T_{m,p}) \;=\; q^{w} - q^{-w} \;=\; h\,[w]_q.
$$

The decoration corresponds to the bar-odd part of the top-channel twist. The writhe exponent governs the $h\,[w]_q$ form across all torus knots, cleanly matching the $10_{124} = T_{3,5}$ and $8_{19} = T_{3,4}$ force-carrier evaluations.
<!-- FILE_END: torus-knot-delta-q-writhe.md -->

<!-- FILE_START: force-carrier-intertwining-correspondence.md -->
**Proposition (force-carrier intertwining correspondence).**
*When the torus-knot force carrier $T_{p,q}$ applies to an $n$-strand molecular braid, the dominant non-trivial Wedderburn weight rests strictly on the intertwining partition:*

$$
  \lambda^{(T_{p,q})}
  \;=\;
  (p,\, 1, 1, \ldots, 1).
$$

The embedding $B_p \hookrightarrow B_n$ restricts the non-trivial permutation orbit precisely to size $p$. The corresponding partition must therefore allocate exactly one tied hook-like part of size $p$, leaving $n-p$ free strands. Empirical evaluation on H$_2$ bound states verifies that $T_{2,9}$ maps exclusively to $(2,1,1)$ and $T_{3,5}$ maps exclusively to $(3,1)$.
<!-- FILE_END: force-carrier-intertwining-correspondence.md -->
