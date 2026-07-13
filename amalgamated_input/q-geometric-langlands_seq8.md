<!-- FILE_START: intro-orphan-reconnect.md -->
We integrate four auxiliary components into the Langlands narrative: the cyclotomic $L$-value decomposition, the mirror 3d-3d correspondence, the modular $S$-transform exchanging the substrate parameter with its dual, and the quantum Langlands dual anchoring the spectral-automorphic interchange. The mutant-Jones and Bloch-group relations bridge the substrate geometry to the cyclotomic $L$-value decomposition.
<!-- FILE_END: intro-orphan-reconnect.md -->

<!-- FILE_START: cyclotomic-l-value-decomposition.md -->
The cyclotomic $\mathrm{Cl}_n$ values established as a basis for the depth-$n$ content over $\mathbb{Q}(\zeta_K)$ are $\mathbb{Q}$-linearly equivalent to Dirichlet $L$-values $L(\chi, n)$ for primitive Dirichlet characters $\chi$ mod $K$ with $\chi(-1) = (-1)^n$.

For prime $K \geq 3$ and integer $n \geq 1$ with parity matching the character class:

$$
  L(\chi, n) \;=\; \frac{G(\chi)}{K^n}\, \sum_{a = 1}^{K - 1} \overline{\chi(a)} \cdot \mathrm{Cl}_n(2\pi a/K),
$$

where $G(\chi) = \sum_{a = 1}^{K - 1} \chi(a) \zeta_K^a$ is the Gauss sum. Inverting via character orthogonality yields:

$$
  \mathrm{Cl}_n(2\pi a/K)
  \;=\;
  \frac{1}{\varphi(K)}\, \sum_\chi G(\overline{\chi}) \chi(a) \cdot \frac{K^n}{G(\chi)}\, L(\chi, n).
$$

Each $\mathrm{Cl}_n(2\pi a/K)$ is a $\mathbb{Q}(\zeta_K)$-linear combination of $L(\chi, n)$ values, and vice versa.

At $N = 4$ and $n = 3$, this recovers a Catalan-like depth-3 $L$-value:

$$
  \beta(3) \;=\; L(\chi_4, 3) \;=\; \mathrm{Im}\,\mathrm{Li}_3(i) \;=\; \frac{\pi^3}{32},
$$

where $\chi_4$ is the non-trivial Dirichlet character mod 4 ($\chi_4(1) = 1, \chi_4(3) = -1$) and $\beta$ is the Dirichlet beta function. The $N=5$ cyclotomic depth-3 content yields a single generator $\mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5) \approx 0.95572$, corresponding to the two odd Dirichlet characters $\chi_5$, $\chi_5^3$ mod 5.

The graded-Mikusiński depth-$n$ cyclotomic content coincides with the Dirichlet $L$-value content at integer $n$, up to $\mathbb{Q}(\zeta_K)$-linear combinations. Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$ depth $n$ becomes the Beilinson conjecture on $L$-values of Dirichlet characters.
<!-- FILE_END: cyclotomic-l-value-decomposition.md -->

<!-- FILE_START: mirror-3d-3d-correspondence.md -->
The Dimofte–Gaiotto–Gukov 3d–3d correspondence maps a hyperbolic 3-manifold $M^3$ to a 3d $\mathcal{N}{=}2$ gauge theory $T[M^3]$. The partition function $Z_{T[M^3]}(q)$ on a squashed 3-sphere $S^3_b$ equals the state-integral invariant of $M^3$ constructed from the quantum dilogarithm $\Phi_q$. Applied to the Borromean rings complement $\mathbf{S}^3 \setminus \mathcal{B}_3$, the 3d–3d theory $T[\mathbf{S}^3 \setminus \mathcal{B}_3]$ yields a partition function whose $h^4$ coefficient matches the framework's Markov-trace coefficient $h^4 = -3/4$.

This 3d–3d correspondence provides a gauge-theory realisation for every hyperbolic 3-manifold mass formula.

| Framework side | 3d gauge theory side |
|----------------|----------------------|
| $\mathcal{B}_3$ (Borromean rings complement) | $T[\mathcal{B}_3]$ — a 3d $\mathcal{N}{=}2$ theory |
| $m_p = m_e \cdot \mathrm{VolDensity}(\mathcal{B}_3, q_0)$ | partition function $Z_{T[\mathcal{B}_3]}(q_0)$ on $S^3_b$ |
| $h^4 = -3/4$ Markov-trace coefficient | 4-loop perturbative contribution to $Z_{T[\mathcal{B}_3]}$ |

This manifests mirror symmetry: the framework's mass formula corresponds to a quantum field theory partition function on a curved spacetime. Both compute the same hyperbolic invariant.
<!-- FILE_END: mirror-3d-3d-correspondence.md -->

<!-- FILE_START: modular-s-transform-q-q-tilde.md -->
Writing the Hecke parameter as $q = e^{2\pi i \tau}$ for a complex parameter $\tau \in \mathbb{H}$ in the upper half-plane, the modular $S$-transform $\tau \mapsto -1/\tau$ induces the analytic continuation:

$$
  q  \;\longmapsto\;  \tilde q \;:=\; \exp\!\bigl(2\pi i / \tau\bigr).
$$

The substrate enters this picture through its bar image $q_0^{-1}$, not through $q_0$. Modular convergence requires $\operatorname{Im}\tau > 0$. Because $q_0 \approx 1.11 > 1$, the value $q_0 = e^{2\pi i\tau_0}$ has $\operatorname{Im}\tau_0 < 0$. Only $q_0^{-1} \approx 0.901 < 1$ lands in $\mathbb{H}$. The modular sector is intrinsically bar-symmetric.

The $S$-transform provides a structural duality. The parameter $q$ admits a bar-symmetric real parameterisation ($q \in \mathbb{R}_{>0}$) and a modular parameterisation ($q = e^{2\pi i \tau}$). The analytic continuation of every Hecke quantity to the modular parameter is well-defined. The $S$-transform $\tau \mapsto -1/\tau$ provides a categorical duality complementing the bar involution.

This realizes the Kashaev Volume Conjecture asymptotics. Writing the bar image $q_0^{-1} = e^{2\pi i \tau_0}$ with $\tau_0 \approx +0.0166\,i$, the $S$-transform sends $\tau_0 \mapsto -1/\tau_0 \approx +60.2\,i$. This large positive imaginary part forces the nome $\tilde q \to 0$, realizing the root-of-unity TQFT limit. This grants an explicit categorical handle on the small-$q_0$ $\leftrightarrow$ root-of-unity duality.
<!-- FILE_END: modular-s-transform-q-q-tilde.md -->

<!-- FILE_START: mutant-jones-bloch-group-intro.md -->
We develop mutant Jones falsifiability and Bloch group closure, tracing the construction from the existing knot-indexed convolutions onward.
<!-- FILE_END: mutant-jones-bloch-group-intro.md -->

<!-- FILE_START: quantum-langlands-dual.md -->
The Iwahori–Hecke algebra $H_n(q)$ admits a quantum Langlands dual $H_n(q^{-1})$ obtained by inverting the deformation parameter. Under Cartan-folding, this duality satisfies:

1. It is distinct from the bar involution $\bar q = q^{-1}$. Langlands duality acts on the Hecke algebra structure at fixed generators, whereas the bar involution acts on the generator action at fixed root data.
2. It coincides with the reverse-limit $q \to \infty$ for non-classical specialisations.
3. For non-simply-laced types, it yields a genuinely distinct dual algebra.

For Type $A_{n-1}$, the Langlands dual is self-dual at the algebra level. The parameter inversion $q \to q^{-1}$ produces a non-trivial $\mathbb{Z}/2$ duality. The $H_n(q)$ algebra possesses a natural Langlands-dual perspective at $q^{-1}$ that connects to the reverse-limit at $q \to \infty$ and to Type-B folding for non-simply-laced extensions. It supplies a categorical origin for the symmetric/antisymmetric mass-tower decomposition, equating matter with Langlands-dual antimatter.
<!-- FILE_END: quantum-langlands-dual.md -->

<!-- FILE_START: outro-q-geometric-langlands.md -->
This closes the main argument of the chapter. The $q$-geometric Langlands correspondence packages the substrate arithmetic—Tannaka–Krein duality on the Hopf side, Weil-bound stability on the spectral side, and the geometric Riemann hypothesis exposition—into a single functorial statement. The substrate parameter $q$ controls both the categorical structure of $\mathbf{C}$ and the spectral distribution of its associated $L$-functions.
<!-- FILE_END: outro-q-geometric-langlands.md -->

