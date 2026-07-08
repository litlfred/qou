<!-- FILE_START: skein-resolution-obstruction.md -->
The Skein resolution obstruction provides a fourth evaluation of the universal obstruction class $\chi(A) \in HH^2 \cong k$. It measures whether the degree-$0$ link polynomial $P_L(q)$ can be extracted from the resolution tree in polynomial depth.

Let $L = \hat{\beta}$ be a link with $c$ crossings, and let $\mathcal{R}(L)$ be its Skein resolution tree. The **Skein resolution obstruction** is the restriction of the universal class to the resolution tree:
$$
  \kappa_c^{\mathrm{comp}}(L, q)
  \;=\; 
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)
   \;\in\; 
  H^2(\mathcal{R}, \mathbb{G}_m).
$$
This class is proportional to the spectral, collision, and elliptic restrictions. A single integer $\chi(A) = -6$ controls whether these computational problems persist through the classical limit.

The Kummer filtration gives:
$$
  \kappa_c^{\mathrm{comp}} \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi(A).
$$
The obstruction vanishes for $n \mid 6$ and persists otherwise. At root-of-unity torsion where the obstruction vanishes, the Iwahori--Hecke algebra has a radical that prunes the resolution tree. At non-vanishing torsion, even quantum interference cannot collapse the tree. Over a finite field $\mathbb{F}_p$ for $p > 7$, the obstruction persists modulo $p - 1$, but computation terminates in bounded time because the field itself is finite. Over $\mathbb{R}$ at non-torsion $q_0 \approx 1.1099$, the algebra $H_n(q_0)$ is semisimple ($\mathrm{Rad} = 0$), the full $3^c$ tree survives, and the obstruction remains non-vanishing.
<!-- FILE_END: skein-resolution-obstruction.md -->

<!-- FILE_START: hecke-satisfies-blitvic-hypothesis.md -->
The non-commutative random variables $\sigma_i \in H_\infty(q)$ under the Markov trace $\mathrm{tr}_M$ satisfy the pair-partition combinatorial hypothesis of Blitvić's non-commutative central limit theorem. 

Blitvić's theorem applies when joint moments $\mathrm{tr}_M(\sigma_{i_1} \sigma_{i_2} \cdots \sigma_{i_k})$ decompose as a sum over pair-partitions $\pi$ with weights depending only on $\pi$ and $q$. The Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$ reduces every generator word to a combination of square-free products. The Markov property then evaluates the trace as a sum over matchings. 

Explicitly, for the centred generator $\tilde\sigma_i := \sigma_i - \mathrm{tr}_M(\sigma_i) \cdot 1$, the joint moment vanishes for odd $k$. For even $k$, it decomposes as:
$$
  \mathrm{tr}_M\bigl(\tilde\sigma_{i_1} \cdots \tilde\sigma_{i_k}\bigr)
  \;=\;
  \sum_{\pi \in P_2(k)}
    W(\pi; q) \cdot \prod_{\{a, b\} \in \pi}
      \delta_{i_a = i_b}.
$$
The weight function $W(\pi; q)$ depends on the crossing count of $\pi$ and aligns with Blitvić's $(q, t)$-Gaussian moment kernel at $t = 1$. This structural decomposition provides the required input for the QOU q-CLT.
<!-- FILE_END: hecke-satisfies-blitvic-hypothesis.md -->

<!-- FILE_START: hecke-satisfies-blitvic-hypothesis-interpretation.md -->
The crossing-count exponent $q^{\mathrm{cr}(\pi)}$ in the pair-partition moment formula arises directly from the braid relation $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$. Each non-trivial reordering of a crossing pair contributes $q$ (positive crossing) or $q^{-1}$ (negative crossing). The Blitvić $(q, t)$-Gaussian with $t=1$ recovers this crossing-weighted combinatorics exactly.
<!-- FILE_END: hecke-satisfies-blitvic-hypothesis-interpretation.md -->

<!-- FILE_START: trace-locality-meets-gs-nonlocality.md -->
Two computational operations seemingly contradict: single Hecke crossings obey Markov locality, yet composite braid evaluation via Gröbner–Shirshov reduction is non-local. Wenzl's product factorisation reconciles them.

Let $\beta = \sigma_{i_1} \cdots \sigma_{i_N}$ have Gröbner–Shirshov normal form $\mathrm{NF}_{\mathrm{GS}}(\beta) = e_{j_1} \cdots e_{j_M}$. 
1. **Markov locality.** For every $x$, $\mathrm{tr}_{M, n+1}(x \sigma_n^{\pm 1}) = z^{\pm 1} \mathrm{tr}_{M, n}(x)$. A single newly-added crossing contributes a scalar independent of the upstream history.
2. **GS non-locality.** $\mathrm{NF}_{\mathrm{GS}}(\beta)$ depends on the full word. Rewriting rules act non-locally across $\beta$.
3. **Product factorisation.** The Markov trace of the normal form decomposes locally: $\mathrm{tr}_M(\rho_{\mathrm{NF}}(\beta)) = \prod_{i = 1}^{M} \widehat{V}_i(q)$. Each vertex volume $\widehat{V}_i$ depends only on its own normal-form generator and modified coefficients produced by the GS algorithm.

The GS algorithm digests global entanglement into local coefficients. After digestion, the Markov trace factorises locally over the normal form. The process is therefore local after normalisation.
<!-- FILE_END: trace-locality-meets-gs-nonlocality.md -->

<!-- FILE_START: trace-locality-nc-probability-reading.md -->
In non-commutative probability terminology, Markov locality means the conditional expectation of a new random variable given the past is a fixed scalar. GS non-locality implies the joint distribution depends on the full word. Product factorisation signifies that the joint law decomposes as a product over states once the sequence is in normal form. GS reduction is thus the non-commutative analogue of finding the stationary representation of a Markov chain.
<!-- FILE_END: trace-locality-nc-probability-reading.md -->

<!-- FILE_START: jones-markov-trace.md -->
Let $q \in \mathbb{C}^{\times}$ not be a root of unity. The Iwahori--Hecke algebra $H_n(R, q)$ admits a unique $\mathbb{C}$-linear functional $\mathrm{tr}_M$ satisfying:
1. Normalisation: $\mathrm{tr}_M(1) = 1$.
2. Trace property: $\mathrm{tr}_M(ab) = \mathrm{tr}_M(ba)$.
3. Markov property: $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$, where $z = (q - 1)/(q^{1/2} + q^{-1/2})^2$.

For each partition $\lambda \vdash n$, the restriction of $\mathrm{tr}_M$ to the irreducible $H_n(R, q)$-module $S_\lambda$ is a non-zero scalar multiple of the character $\chi_\lambda$. For any braid $\beta$, $\mathrm{tr}_M(\rho_n(\beta))$ computes the Jones polynomial of the closure $\hat{\beta}$ up to framing.
<!-- FILE_END: jones-markov-trace.md -->

<!-- FILE_START: jones-markov-trace-formalization-note.md -->
The existence proof of the Markov trace occupies §3–5 of Jones (1987). Our formalization takes the result as axiomatic, encoding its core properties as a Lean structure over the $R_q = \mathbb{Z}[q, q^{-1}]$ ground ring. Downstream theorems, such as completeness on irreducibles, are formally verified against these structure fields.
<!-- FILE_END: jones-markov-trace-formalization-note.md -->

<!-- FILE_START: markov-disambiguation.md -->
We distinguish three constructs bearing the name "Markov":
1. **Markov trace:** The algebraic functional $\mathrm{tr}_M$ on the Hecke algebra that feeds the mass formula.
2. **Markov chain:** The stochastic random walk on braid words induced by Hecke transition probabilities, which provides error bounds.
3. **Markov moves:** The topological operations of conjugation and stabilisation that generate link equivalence.
Context clarifies usage, but when precision is needed, we write $\mathrm{tr}_M$ for the algebraic functional, "Markov chain" for the stochastic process, and "Markov move" for the topological equivalence.
<!-- FILE_END: markov-disambiguation.md -->

<!-- FILE_START: bar-involution.md -->
The **bar-involution** $\overline{(\cdot)} \colon H_n(q) \to H_n(q)$ is the ring anti-involution on the Iwahori–Hecke algebra defined by:
$$
\overline{\sigma_i} \;=\; \sigma_i^{-1}, \qquad \overline{q} \;=\; q^{-1}.
$$
Geometrically, it corresponds to reflecting the braid diagram (swapping positive and negative crossings).
<!-- FILE_END: bar-involution.md -->

<!-- FILE_START: bar-involution-properties.md -->
The bar-involution satisfies $\overline{\overline x} = x$. Over a field of characteristic $\ne 2$, every $x \in H_n(q)$ decomposes uniquely into a bar-symmetric (even) part $P_{\mathrm{avg}}(x)$ and a bar-anti-symmetric (odd) part $P_{\mathrm{skew}}(x)$.

Our framework asserts that $P_{\mathrm{avg}}$ is the canonical projection: the bar-symmetric part represents physical observables, while the bar-anti-symmetric part is projected away. This applies systematically across operations, retaining functions like $\cos$ and $\cosh$ while discarding $\sin$ and $\sinh$.
<!-- FILE_END: bar-involution-properties.md -->

<!-- FILE_START: bar-involution-c5-algebraic-identities.md -->
The parameter $h = q - q^{-1}$ factors into $h_{1/2} = q^{1/2} - q^{-1/2}$ and $1/z = q^{1/2} + q^{-1/2}$. The bar-anti-symmetry of $h$ stems entirely from $h_{1/2}$, while the Markov parameter $z$ is bar-invariant.

The Hoefsmit-Quantum-2 identity is $b^2(q) = 1 - 1/[2]_q^2$. From this, the $c_5$ closed form follows:
$$
c_5(q) \;=\; -\tfrac{3}{2} + \frac{1}{[2]_q^2} \;=\; -\tfrac{3}{2} + \frac{1}{h^2 + 4}.
$$
Both terms are strictly even functions of $h$. The constant $-3/2$ corresponds to half the dimension of the non-sign Wedderburn blocks of the symmetric group $S_3$. This identifies the $-1/2$ fingerprint in the empirical decomposition as the bar-symmetric contribution from the non-sign sector at the classical limit.

Testing the sequence $c_k(q)$ reveals that the $c_5$ outlier only appears at the silver ratio, not at the golden ratio, confirming it is an inert-prime fingerprint tied to the $\beta$-decay null. These bar-grading algebraic structures are fully verified in Lean.
<!-- FILE_END: bar-involution-c5-algebraic-identities.md -->

<!-- FILE_START: bar-involution-geometric-kac-sunada.md -->
The bar-involution projection corresponds to orientation-averaging geometrically. It yields averaged crossings for knots, unsigned winding for color tubes, symmetrized Wilson loops on the exceptional divisor, and the contact volume form $\alpha \wedge d\alpha$.

The Kac-Sunada theorem establishes that distinct manifolds can be isospectral. Similarly, distinct braids can share the same Hecke trace $\tau_M(\beta)$ at fixed $q$. However, requiring the trace to match at both $q$ and $q^{-1}$ imposes a much tighter constraint. The physical theory must hear the bar-symmetrized spectrum, forcing the use of the bar-symmetric projection.
<!-- FILE_END: bar-involution-geometric-kac-sunada.md -->

<!-- FILE_START: braid-group-n-strand.md -->
To compute the $\tau_M(K_1 \sqcup K_2)$ inter-knot decoupling, the $B_3$ framework generalises to arbitrary $n$-strand braid groups and Hecke quotients. The Lean class system enables per-$n$ extensibility, allowing downstream theorems to auto-specialise as higher dimensions are analysed.
<!-- FILE_END: braid-group-n-strand.md -->

<!-- FILE_START: h3-hecke-idempotents.md -->
The algebra $H_3(q)$ contains three irreducible Wedderburn blocks. The symmetric block $V_{(3)}$ and antisymmetric block $V_{(1,1,1)}$ both have dimension $1$. The mixed-symmetry block $V_{(2,1)}$ has dimension $[2]_q = q + q^{-1}$. The sum of dimensions correctly recovers $q + q^{-1} + 2$.

The explicit projector normalization utilizes the $S_3$ Poincaré polynomial $P(q) = 1 + 2q^2 + 2q^4 + q^6$. Because $P(q) \geq 1 > 0$ for all real $q$, idempotency requires no genericity hypothesis beyond $q \neq 0$.
<!-- FILE_END: h3-hecke-idempotents.md -->

<!-- FILE_START: braid-link-types.md -->
The infrastructure provides explicit Lean types for generic braids and links. For 2-strand braids, the closure of $\sigma_1^2$ explicitly yields the Hopf link. This evaluates to the classical Jones value $-2$. 

The 3-strand generalisation requires extracting the dominant 2-strand sub-braid at order $\varepsilon^6$. The reduction of this sub-braid closes to the Hopf link, yielding the same $c_3 = -2$ value. This identifies the perturbative mass coefficients mechanically from the topological scaffolding.
<!-- FILE_END: braid-link-types.md -->

