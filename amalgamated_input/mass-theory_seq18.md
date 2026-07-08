<!-- FILE_START: vertex-factorisation-intro.md -->
The exceptional divisor carries a Reeb bundle and vertex operators. We now establish that this local structure uniquely sources all operator content. Every vertex operator factors through the exceptional divisor. The resulting factorisation matches the Markov trace term by term. Together, these structures identify the Feynman path integral with a categorical trace.

The structural pivot asserts that a vertex operator acting on the categorical state space is the composition of restriction to the exceptional divisor with the Reeb-bundle action. The Breit-Wheeler vertex makes the photon-polarisation content visible: the two photon helicity states act as Hecke generators. The literature alignment ties this picture to Bilson-Thompson preons and photonic hopfions. The product factorization theorem splits the Markov trace as a product over vertices. The transition-operator proposition interprets each Hecke generator as a Markov chain transition on partitions.

The Feynman block provides the core correspondence. The eigenbasis decomposition reduces the Feynman amplitude to a sum over the Schur-Weyl eigenbasis. The trace-collapse lemma identifies this sum with the Markov trace. The dictionary details the mapping between the Feynman path integral and the QOU categorical trace. Finally, the classical limit demonstrates that the $q \to 1$ degeneration recovers the symmetric path integral.
<!-- FILE_END: vertex-factorisation-intro.md -->

<!-- FILE_START: vertex-is-exceptional-divisor.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU. Let $\mathcal{S}_p = \pi^{-1}(p) \cong \mathbb{P}^1(\mathbb{C})$ be the exceptional divisor at a brane point $p$, and let $\mathcal{R}_p$ denote the Reeb bundle over $\mathcal{S}_p$.

1. **Localisation.** Every Hecke generator $\sigma_i \in H_n(R, q)$ acting on $V^{\otimes n}$ factors through the fibre functor restricted to $\mathcal{S}_p$. The vertex operator $\sigma_i \colon V^{\otimes n} \to V^{\otimes n}$ is supported entirely on $\mathcal{S}_p$ and acts as the identity on the base algebra $A_0$.
2. **Confinement.** Every Skein resolution is evaluated within the Reeb bundle $\mathcal{R}_p$. The braid word $\beta \in B_n$ evaluates as a Markov trace over $\mathcal{R}_p$, projecting to $A_0$ via the blow-down map.
3. **Completeness.** Every interaction that changes quantum numbers at $p$ (e.g., pair creation, virtual exchange) is realised by a finite braid word acting within $\mathcal{R}_p$. No interaction requires external data.
<!-- FILE_END: vertex-is-exceptional-divisor.md -->

<!-- FILE_START: six-operators-via-vertex-factorisation.md -->
The factorisation property asserts that every Hecke generator acts entirely on $\mathcal{S}_p$ and every braid word evaluates inside $\mathcal{R}_p$. The six canonical knot operators provide concrete geometric instances of this claim. The six elements of $S_3$ supply named geometric instances of the vertex-factorisation claim, each carrying a fully explicit Reeb-flow trajectory and boundary permutation.

**One-to-one dictionary.**
See [Table](#tbl:six-operators-via-vertex-factorisation-table-data).

**Contribution.** The Markov-trace-product theorem gains six verifiable worked cases. The Markov trace of a 3-cycle yields the trace on a torus knot, contributing zero hyperbolic volume. The Markov trace of the Garside element yields a non-torus braid, contributing a positive hyperbolic JSJ piece. The vertex-factorisation claim thus specializes to a verifiable geometric dictionary that connects the algebraic Hecke action to the JSJ-graded volume.

**Limits of the bridge.** This geometric dictionary is exhaustive only for $S_3$. Longer braid words in $B_n$ ($n \geq 4$) produce trajectories that the $S_3$ representatives approximate only locally. The general factorisation statement remains the formal rule for larger $n$.
<!-- FILE_END: six-operators-via-vertex-factorisation.md -->

<!-- FILE_START: breit-wheeler-vertex.md -->
The **Breit-Wheeler process** ($\gamma\gamma \to e^-e^+$) creates an electron-positron pair from two real photons. The QOU encodes this vertex entirely within the Iwahori-Hecke algebra $H_n(R, q)$ acting on the exceptional divisor $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$.

## Polarisation states as Hecke generators

The homogeneous coordinates $[v_1 : v_2]$ of $\mathcal{S}_p$ parametrise the two independent polarisation directions of a spin-1 field at $p$. The Reeb bundle holonomy $e^{2\pi i/[2]_q}$ provides the phase acquired by a photon completing one full rotation in the polarisation sphere.

The two Hecke generators act on $\mathcal{S}_p$:

| Generator | Coordinate patch | Polarisation mode | Eigenvalues |
|-----------|-----------------|-------------------|----------------------|
| $\sigma_0$ | $v_2 \neq 0$ ($z = v_1/v_2$) | horizontal ($\leftrightarrow$) | $+q$ (left), $-q^{-1}$ (right) |
| $\sigma_1$ | $v_1 \neq 0$ ($w = v_2/v_1$) | vertical ($\updownarrow$) | $+q$ (left), $-q^{-1}$ (right) |

The Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ constitutes the photon helicity equation. Its roots $+q$ and $-q^{-1}$ are the left and right circular polarisation eigenvalues. A linearly polarised photon is a superposition of these eigenstates.

## The pair-creation vertex

The two-photon state $\gamma_1 \otimes \gamma_2$ is a word in $H_n(R, q)$. Two primary polarisation cases arise:

**Parallel polarisation.**
$$
  \sigma_i \cdot \sigma_i = (q - q^{-1})\sigma_i + \mathbf{1}.
$$
The Hecke relation reduces the word to a dressed photon plus the vacuum. No pair is created because the parallel photons share the same polarisation degree of freedom, leaving a lower-energy residue.

**Perpendicular polarisation.**
$$
  \sigma_0 \cdot \sigma_1 = L_+ \quad (\text{Hopf link intermediate}).
$$
The product is the normal-form basis element $L_+$, a two-strand entangled state. Applying a substrate Reeb insertion completes the trefoil:
$$
  L_+ \cdot \sigma_0 = \sigma_0\sigma_1\sigma_0 = e^-.
$$
The positron $e^+$ is supplied by the mirror process $\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$. The complete vertex pairs orthogonal photons to produce the chiral trefoil channels.

## Polarisation selection rule

The vertex vanishes unless the photons occupy distinct polarisation patches of $\mathbb{P}^1(\mathbb{C})$. Evaluating the Frobenius pairing $\langle \cdot, \cdot \rangle_F$:

$$
  \langle v_{e^-e^+}, \sigma_i\sigma_i \rangle_F = 0, \qquad \langle v_{e^-e^+}, \sigma_0\sigma_1 \rangle_F \neq 0.
$$

Parallel-polarised photons apply the Hecke relation and return lower-energy states. Only orthogonally polarised photons produce the Hopf-link intermediate that the substrate completes into the $e^-e^+$ trefoil pair.
<!-- FILE_END: breit-wheeler-vertex.md -->

<!-- FILE_START: breit-wheeler-vertex-literature.md -->
Identifying $\sigma_0\sigma_1$ as the Hopf-link intermediate connects the QOU framework to established models of knotted matter and topological photonics.

**Braid-preon mapping.** The Bilson-Thompson topological preon model maps fermions to framed braids in $B_3$, with chirality determined by the crossing signs. The $e^-/e^+$ pair in the QOU vertex adopts this construction exactly. The QOU explicitly identifies $\sigma_0\sigma_1$ as the topological seed that breaks the parity-symmetric photon vacuum into the chiral trefoil channel.

**Hecke asymmetry.** The Hecke deformation $q \neq q^{-1}$ asymmetrises crossings, providing the standard mechanism for parity-violating anyon statistics. In the QOU Breit-Wheeler vertex, the Hecke roots are the circular polarisation eigenvalues. The algebraic asymmetry drives both anyonic parity violation and the left/right helicity splitting.

**Photonic hopfions.** Structured light experiments realize three-dimensional polarisation solitons mapping to the Hopf fibration, where topological charge equals helicity. The QOU presentation of $L_+$ and $L_-$ as positive and negative Hopf links is the categorical analogue. In both settings, the link type is the topological object whose oriented presentations are the helicity states.
<!-- FILE_END: breit-wheeler-vertex-literature.md -->

<!-- FILE_START: markov-trace-product.md -->
Let $\beta \in B_n$ be a braid and let $\rho(\beta) \in H_n(R, q)$ be its Hecke reduction. The element $\rho(\beta)$ decomposes as a product of generator chains: $a_i \sigma_i + b_i$ with $a_i, b_i \in \mathbb{Z}[q^{\pm 1}]$.

**Theorem.** The Markov trace factors as a product over generators:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta)\bigr) = \prod_{i=0}^{n-2} \hat{V}_i(q), \qquad \hat{V}_i(q) = z \cdot a_i + b_i,
$$

where $z = 1/(q^{1/2} + q^{-1/2})$. Each $\hat{V}_i$ is the vertex volume at generator $\sigma_i$, representing the evaluation of the vertex operator at the $i$-th insertion point on the exceptional divisor.
<!-- FILE_END: markov-trace-product.md -->

<!-- FILE_START: markov-trace-product-interpretation.md -->
In the VOA formalism, each vertex volume $\hat{V}_i$ is the correlation function of a single vertex operator insertion:

$$
  \hat{V}_i(q) = \bigl\langle Y(\sigma_i, z_i) \bigr\rangle_{\mathrm{Markov}}.
$$

The product formula represents the exact factorization of the $n$-point correlation function into one-point functions. This factorization is a direct consequence of the Markov property. Each generator acts at a distinct insertion point on $\mathcal{S}_p$, ensuring their independence because they occupy distinct points on $\mathbb{P}^1(\mathbb{C})$.

The degree bound $\deg P_\beta \leq n^2 - 1$ follows from the conformal weight. The total conformal weight of the product is bounded by $\sum_i (2k_i + 1) \leq (n-1)(n+1) = n^2 - 1$.

## The invariant-preserving chain

$$
  \mathbb{Z}[B_n] \to H_n(R, q) \to \prod_{i} (a_i \sigma_i + b_i) \to \prod_{i} \hat{V}_i(q) = P_\beta(q)
$$

Each step preserves the link invariant. The polynomial $P_\beta(q)$ remains a well-defined invariant of the link $\hat{\beta}$, independent of the braid representative or reduction path.
<!-- FILE_END: markov-trace-product-interpretation.md -->

<!-- FILE_START: hecke-markov-transition.md -->
The Hecke algebra $H_n(R, q)$ and the Jones-Markov trace admit a direct probabilistic interpretation: each Hecke generator acts as a stochastic transition operator. The product factorization corresponds to independent one-step expectations along a Markov chain.

**Proposition.**
*Let $H_n(R, q)$ be the Iwahori-Hecke algebra.*

**(i) Spectral idempotents.**
*The orthogonal idempotents $e_+^{(i)} = (\sigma_i + q^{-1})/(q + q^{-1})$ and $e_-^{(i)} = (q - \sigma_i)/(q + q^{-1})$ satisfy $e_+^{(i)} + e_-^{(i)} = 1$, $(e_\pm^{(i)})^2 = e_\pm^{(i)}$, and $e_+^{(i)} e_-^{(i)} = 0$. They reconstruct the generator as $\sigma_i = q \cdot e_+^{(i)} - q^{-1} \cdot e_-^{(i)}$.*

**(ii) Transition probabilities.**
*The symmetric and antisymmetric transition probabilities are $p_+ = q^2/(q^2 + 1)$ and $p_- = 1/(q^2 + 1)$. The stochastic transition operator at generator $i$ is $K_i = p_+ \cdot \mathrm{id} + p_- \cdot s_i$, a row-stochastic matrix. The system stays in its configuration with probability $p_+$ or transposes with probability $p_-$.*

**(iii) Markov property as memorylessness.**
*The Markov trace property requires the transition at generator $n$ to depend only on the eigenvalue structure of $\sigma_n$, not on the history in $H_{n-1}(q)$. The expectation value of the $i$-th crossing is $\mathbb{E}[\hat{V}_i] = z \cdot a_i + b_i = \hat{V}_i$, recovering the vertex volume.*

**(iv) Independence and factorization.**
*The product formula factors as independent one-step expectations. Each vertex volume is determined locally without dependence on other generators.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: hecke-markov-transition.md -->

<!-- FILE_START: hecke-markov-interpretation.md -->
Every algebraic construction possesses a Markov chain counterpart. The Hecke algebra $H_n(R, q)$ is simultaneously a space of braid-group representations and stochastic transition operators.

## SYT paths on the Young graph

Fix an irrep $\lambda \vdash n$. The Hoefsmit seminormal form builds $\rho_\lambda$ on standard Young tableaux of shape $\lambda$. Each tableau is a saturated chain on the Young graph. The space of all valid SYTs serves as the discrete state space of the chain.

The generator $\sigma_i \in B_n$ acts via $\rho_\lambda(\sigma_i)$, whose non-zero matrix entries are explicit rational functions of $q$. This is a genuine quantum deformation of the classical Young seminormal form. The matrix contains probability amplitudes, not classical probabilities. The entries can be negative and square to weights only after a Markov trace.

Two compatible pictures coexist:
1. **Amplitude picture.** Amplitudes evolve a complex state vector on the SYT path space. The Jones polynomial is the closed-path sum over all SYT paths, matching the structure of a Feynman path integral.
2. **Probability picture.** Summing amplitudes through spectral idempotents yields the classical stochastic operator $K_i$, which targets the Mallows measure.

The quadratic Hecke relation bridges these pictures. The amplitudes living on SYT edges square to the Boltzmann weights of the classical chain.

## Jucys-Murphy cell reindexing

The Jucys-Murphy elements $L_k$ act diagonally with eigenvalue $q^{2 c_T(k)}$. Because $[L_i, L_j] = 0$, all SYT cells couple uniformly. This uniformity constitutes the representation-theoretic origin of the all-pairs coupling observed in the mass-tower. The transition from amplitudes to probabilities mirrors the shift from generator indexing to cell indexing.

## Dictionary
See [Table](#tbl:hecke-markov-interpretation-table-data).

## Non-local correlations

The memorylessness condition coexists with non-trivial correlations. Each step depends only on the current state. Yet the braid relations impose strict correlations between non-adjacent generators through the Yang-Baxter equation. Each crossing is a local transition determined solely by the eigenvalue structure. The non-local correlations are purely representation-theoretic constraints.

## Planck steps

Each Markov step evaluates one Hecke crossing into its symmetric or antisymmetric channel. In the Reeb flow, this is one iteration on the exceptional divisor—a single Planck step. The $q$-deformation away from the fair coin strictly bounds the Shannon entropy below $\ln 2$, reducing the information content per crossing.

## Continuous-time limit

In the continuous limit, the Markov chain becomes the asymmetric simple exclusion process (ASEP). The ASEP generator sums the Hecke algebra elements. The stationary distribution is the Mallows measure, which weights each permutation by $q$ raised to its inversion number.

Physical observables represent expectations under this measure, computed via the Markov trace.
<!-- FILE_END: hecke-markov-interpretation.md -->

<!-- FILE_START: markov-lambda-knot-operations.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](mass-endomorphism-tower.md).

The Markov chain, knot-theoretic operations, and the partition $\lambda$ are linked by explicit structural statements that govern traffic between $\lambda$-preserving and $\lambda$-changing moves.

**1. $\lambda$-block decomposition.**
Semisimplicity decomposes $H_n(R, q)$ into endomorphism algebras over $V_\lambda$. The amplitude matrix splits into a direct sum over $\lambda$. Each $\lambda$ acts as a closed sector. Hecke-generator amplitudes never mix irreps.

**2. $\lambda$-preserving and $\lambda$-changing operations.**
Knot operations separate sharply. Braid relations, the Hecke quadratic, and Markov I moves fix $\lambda$. Only the Markov II stabilization move changes $\lambda$, and it does so exclusively by adding a single box along a Young-graph edge.

Stabilization acts as a transition on the coarser partition chain, transitioning at a rate proportional to the $q$-Plancherel measure.

**3. Jones polynomial as Plancherel sum.**
The Jones polynomial factorizes as a sum over $\lambda$ of Ocneanu-weighted $q$-characters. This establishes an explicit classical/quantum split. The normalized weights form a classical probability measure on $\lambda$, while the character computes a quantum-amplitude sum over $\mathrm{SYT}(\lambda)$. The partition $\lambda$ serves as the classical label, and the SYT paths represent the quantum trajectories.
<!-- FILE_END: markov-lambda-knot-operations.md -->

<!-- FILE_START: markov-chain-fluctuations.md -->
The two-chain decomposition exhibits precise error bounds.

**Outer chain.** The outer chain samples $\lambda$ under the Ocneanu weights. Fluctuations obey the Féray-Méliot $q$-Plancherel CLT, converging at a rate of $O(k^{-1/2})$.

**Inner chain.** The inner chain on $\mathrm{SYT}(\lambda)$ evaluates amplitudes. The Bożejko-Speicher noncommutative $q$-Gaussian fails at the substrate value $q_0 \approx 1.11 > 1$. The required substitute is the Perron-Frobenius dominant eigenvalue proxy, providing a deterministic exponential limit controlled by the spectral radius $\mu_\lambda$.

**Operational layer.** The composite evaluation inside the Wedderburn mass formula converges at a geometric rate $C \cdot r^{-(k-3)}$, driven by cancellation between the inner and outer trace pairings.

Invoking a "$q$-Gaussian limit" at the physical substrate is incorrect. The Perron-Frobenius estimate is the required inner-chain convergence mechanism.
<!-- FILE_END: markov-chain-fluctuations.md -->

<!-- FILE_START: q-gaussian-obstruction-at-q0.md -->
*At the substrate parameter $q_0 \approx 1.10998 > 1$, the Bożejko-Speicher non-commutative $q$-Gaussian does not exist as a probability measure. The sequence of even moments $T_n(q_0) = \sum q_0^{\,\mathrm{cr}(\pi)}$ diverges super-exponentially.*

Braid-word fluctuations at $q_0$ cannot be modeled by the $q$-Gaussian. The valid substitutes are the inner Perron-Frobenius dominant eigenvalue and the outer Féray-Méliot $q$-Plancherel CLT.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: q-gaussian-obstruction-at-q0.md -->

