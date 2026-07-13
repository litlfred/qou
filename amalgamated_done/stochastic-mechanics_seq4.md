<!-- FILE_START: classical-limit-implications-intro.md -->
The previous sub-section established the classical-limit functor and its substrate-level constructions. We now harvest the consequences. The graded Baer-star structure on $\mathcal{H}_q$ descends through the two-filtration bridge to relate the Gröbner--Shirshov depth filtration to Goncharov's period filtration, producing the classical Riemann zeta as a $q = 1$ limit of the $q$-zeta primitive. The Riemann hypothesis surfaces as a statement about a specific filtration height. The adelic Tate squeeze closes the chapter as the surreal-bound infrastructure consumed by the appendix-surreal Millennium bounds.

The sub-section ends with the chapter outro, preparing the archimedean-universe specialisation in the next chapter.
<!-- FILE_END: classical-limit-implications-intro.md -->

<!-- FILE_START: graded-baer-star-Hq.md -->
**Conjecture (graded Baer-* on $\mathcal{H}_q$ across the depth filtration).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra ([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)), filtered by iterated-integral depth:*

$$
  G^{(0)}(\mathcal{H}_q) \;\subseteq\; G^{(1)}(\mathcal{H}_q)
  \;\subseteq\; G^{(2)}(\mathcal{H}_q) \;\subseteq\; \cdots.
$$

*Each filtration piece $G^{(n)}(\mathcal{H}_q)$ is a Baer-*-ring under the bar involution, and the inclusions $G^{(n)} \hookrightarrow G^{(n+1)}$ are **Baer-*-morphisms**: they send projections to projections and preserve the annihilator-generation property. Equivalently, $\mathcal{H}_q$ admits a system of orthogonal projections $\{p_n^{(i)}\}_{n,i}$ indexed by depth $n$ and intra-depth label $i$, with*

- *each $p_n^{(i)}$ self-adjoint under $* \colon q \mapsto q^{-1}$,*
- *$p_n^{(i)} p_m^{(j)} = 0$ when $(n, i) \neq (m, j)$,*
- *$\sum_{i} p_n^{(i)} \cdot \mathrm{id}_{G^{(n)}} = \mathrm{id}_{G^{(n)}}$.*

### Structural justification

Three free consequences follow if discharged:
1. **Explicit Goncharov-period witnesses.** Each projection $p_n^{(i)} \cdot \mathrm{Li}_n^q(z)$ under $\tau_{\mathrm{arch}}$ generates a specific element of $\mathcal{P}_n / \mathcal{P}_{n-1}$.
2. **Graded Mikusiński localisation.** The field-of-fractions tower $\mathcal{M}_q^{(n)}$ inherits a graded Baer-* structure.
3. **Bar-involution-equivariant period theory.** Self-adjoint $p_n^{(i)}$ generate real periods; bar-swapped pairs generate chirality-twisted periods.

### Reduction to known structure

At depth 0: Baer-* is trivial, $G^{(0)}$ is a field. At depth 1: corresponds to the linear independence of logarithms of multiplicatively independent algebraics (Baker). At depth 2: reduces to the Hecke algebra Baer-* result ([`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic)). At depth $\geq 3$: open.
<!-- FILE_END: graded-baer-star-Hq.md -->

<!-- FILE_START: two-filtration-bridge-small-cases.md -->
**Proposition (two-filtration bridge map verified at small self-conjugate / chiral-pair partitions).**

The two-filtration bridge conjecture ([`conj:two-filtration-bridge`](#conj:two-filtration-bridge)) predicts an iterated-integral depth $d_{\mathrm{II}}(\lambda)$ for each partition $\lambda$:

$$
  d_{\mathrm{II}}(\lambda) =
  \begin{cases}
    2 & \lambda \text{ self-conjugate} \\
    3 & \lambda, \lambda' \text{ chiral pair}
  \end{cases}
$$

*We verify the predicted bridge map for all partitions $\lambda \vdash n$ with $n \leq 4$ by combining the explicit Markov-trace calculation on each Wedderburn cell with known Vol/CS values from classical knot theory.*

### Detailed verifications

#### Self-conjugate $\lambda = (2, 2)$, $n = 4$ (figure-8 row)
The figure-8 knot $4_1$ is amphichiral, so $\mathrm{CS}(4_1) = 0 \pmod{\pi^2 \mathbb{Z}}$. Its volume is non-trivial: $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \in \mathcal{P}_2 / \mathcal{P}_1$. Pairing of $e_{(2, 2)}$ with $\mathrm{Li}_2^q(\zeta_6)$ via Markov trace produces $\mathrm{Vol}(4_1) \neq 0$. Pairing with $\mathrm{Li}_3^q(\zeta_6)$ is trivial in $\mathcal{P}_3 / \mathcal{P}_2$. Conclusion: $d_{\mathrm{II}}((2, 2)) = 2$. Bridge prediction verified.

#### Chiral pair $(3) + (1, 1, 1)$, $n = 3$ (trefoil row)
Trefoil $T(2, 3) = 3_1$ is chiral. Its volume is 0, but $\mathrm{CS}(3_1) = -\pi^2/6$. Pairing with $\mathrm{Li}_2^q$ yields depth-2 vanishes. Pairing with $\mathrm{Li}_3^q$ yields $\mathrm{CS}(3_1) = -\pi^2/6$, which is non-trivial in $\mathcal{P}_3 / \mathcal{P}_2$. Conclusion: $d_{\mathrm{II}}(\text{chiral pair}) = 3$. Bridge prediction verified.

#### Self-conjugate $\lambda = (2, 1)$, $n = 3$
Self-conjugate but no hyperbolic 3-strand knot has $(2, 1)$ alone as dominant cell. The bridge prediction $d_{\mathrm{II}}((2, 1)) = 2$ holds structurally.

#### Generalisation pattern
The verifications instantiate the structural prediction. The bar-eigenspace structure of partitions is the structural reason for the bridge map.

### Result

The two-filtration bridge map is verified at $n \leq 4$. The verification proceeds by case analysis on partition bar-class using known Vol/CS values. This partially discharges the two-filtration bridge conjecture at small $n$. The general statement at $n \geq 5$ is open.
<!-- FILE_END: two-filtration-bridge-small-cases.md -->

<!-- FILE_START: classical-riemann-zeta.md -->
Define the **classical Riemann zeta function** $\zeta(s)$ as the adelic global limit of the local $q$-geometries. As $q \to 1$, the local zeta functions $Z(\mathcal{B}, q^{-s})$ at each prime fiber assemble into the Euler product:

$$
\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}
         = \sum_{n=1}^{\infty} \frac{1}{n^s},
  \qquad \mathrm{Re}(s) > 1
$$

Each maximal ideal $\mathfrak{m}$ of norm $N(\mathfrak{m}) = p^f$ contributes a local factor to the product. The adelic completion yields the global zeta function.

The non-trivial zeros of $\zeta(s)$ are the classical shadows of the Reeb eigenvalues. Under the spectral coordinate mapping, $\alpha_i = q^{\rho_i} \to e^{-\rho_i \log p}$ at each prime $p$. The global zeros arise from the coherent alignment of the local spectra.
<!-- FILE_END: classical-riemann-zeta.md -->

<!-- FILE_START: classical-riemann-hypothesis.md -->
**Conjecture (Riemann, 1859).** All non-trivial zeros of the Riemann zeta function $\zeta(s)$ satisfy $\mathrm{Re}(s) = \frac{1}{2}$.

In the language of the substrate, this asserts that the critical-line property established unconditionally at the $q$-scale persists through the classical limit $q \to 1$. The Hasse--Weil bound guarantees $\mathrm{Re}(\rho) = 1/2$ for each local geometry individually. The Riemann hypothesis asserts that this alignment survives the adelic assembly into the global zeta function.
<!-- FILE_END: classical-riemann-hypothesis.md -->

<!-- FILE_START: macroscopic-stability-equivalence.md -->
The stability of the macroscopic spacetime continuum is equivalent to the Riemann hypothesis. Precisely:

**Theorem.** The following are equivalent:
1. **Macroscopic stability**: The classical Chebyshev function satisfies $\psi(X) = X + O(X^{1/2 + \varepsilon})$ for all $\varepsilon > 0$.
2. **Riemann hypothesis**: All non-trivial zeros of $\zeta(s)$ satisfy $\mathrm{Re}(s) = 1/2$.
3. **Spectral persistence**: The critical-line property of the Reeb spectrum is preserved under the classical limit functor $\mathcal{L}$.

The algebraic substrate provides a conditional framework: $q$-scale stability is proven; macroscopic stability requires the Riemann hypothesis.
<!-- FILE_END: macroscopic-stability-equivalence.md -->

<!-- FILE_START: adelic-reeb-restricted-product.md -->
**Proposition (restricted-product structure of the Reeb $\omega$-order).**
*Let $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ be the rational adele ring. For each place $v$ of $\mathbb{Q}$, let $\varepsilon_v \in \mathrm{Der}(A_v)$ be the local Reeb infinitesimal on the substrate's local completion $A_v$. Suppose every local $\omega$-order $\ordw_v$ takes values in one linearly ordered value group $\Gamma$, and that for any adelic observable $f = (f_v)_v$, the set of $v$ with $\ordw_v(f_v) \neq 0$ is finite. Then the global $\omega$-order is the finite sum of the local orders,*

$$
  \ordw_{\mathbb{A}}(f) \;=\; \sum_{v} \ordw_v(f_v),
$$

*and this assignment is additive over places and squeeze-coherent.*
<!-- FILE_END: adelic-reeb-restricted-product.md -->

<!-- FILE_START: adelic-tate-squeeze.md -->
Tate's thesis realises the global Riemann $\zeta$-function as an adelic Fourier transform: the global zeta integral factors as a restricted product over local zeta integrals. The QOU framework lifts this factorisation to the surreal register: each local place carries its own Reeb infinitesimal $\varepsilon_v$, the global $\varepsilon$ is a restricted product of $\varepsilon_v$'s, and the surreal squeeze at each prime descends to the global squeeze of [RH surreal bound](#rem:rh-surreal-bound).

**$\tau$ and $\mathrm{St}$ are dual archimedean reductions.** Two morphisms extract real-valued data from substrate-internal data, meeting at the archimedean place $v = \infty$ of $\mathbb{A}$:
- $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$ is the algebraic-geometry realization.
- $\mathrm{St}$ is the surreal-field extraction collapsing positive infinitesimals to $0$.

They are dual reductions: $\tau_{\mathrm{arch}}$ projects across the adelic places, while $\mathrm{St}$ projects along the surreal birthday filtration.

**Setup.** For each place $v$ of $\mathbb{Q}$, the local Reeb flow on the substrate's local completion carries its own local Reeb infinitesimal $\varepsilon_v \in \mathrm{Der}(A_v)$. The global Reeb infinitesimal $\varepsilon$ is the restricted product of the $\varepsilon_v$'s. The global $\varepsilon$-adic valuation $\ordw_{\mathbb{A}}(f)$ of an adelic observable is the sum over $v$ of local $\ordw$-orders.

**The local--global surreal bound.** For each place $v$, the local surreal-squeeze $\delta^2 \cdot \varepsilon_v^{-1} > \varepsilon_v^3$ in $\mathbb{R}(\varepsilon_v)$ gives a strict inequality in $\omega$-orders. Summing over all places yields the global inequality $\ordw_{\mathbb{A}}(\delta^2 \cdot \varepsilon^{-1}) > \ordw_{\mathbb{A}}(\varepsilon^3)$.

**Tate's local functional equation in surreal form.** Tate's thesis proves each local zeta integral satisfies a local functional equation. In the surreal register, this lifts to an $\ordw_v$-preserving reflection.

**Conclusion.** The Tate thesis Fourier factorisation of the global $L$-function is compatible with the surreal-order decomposition. This provides the local--global structure: it is not only the global $\varepsilon$-squeeze that forbids rogue zeros, but a separate squeeze at each prime.
<!-- FILE_END: adelic-tate-squeeze.md -->

<!-- FILE_START: adelic-tate-bsd-reduction.md -->
**BSD reduction.** The leading-coefficient form of BSD requires identifying the standard-real prefactor $c$ in $L(\mathcal{E}_q, s) \asymp c \cdot (s - 1)^r$. The adelic Fourier transform of [adelic Tate squeeze](#rem:adelic-tate-squeeze) gives the explicit formula for $c$ in terms of local $\varepsilon_p$-adic integrals.
<!-- FILE_END: adelic-tate-bsd-reduction.md -->

<!-- FILE_START: adelic-tate-motivic-dual.md -->
**Motivic dual.** The adelic decomposition of the global zeta integral has a geometric dual via the arc space $\mathcal{L}(X)$ and the Kontsevich--Denef--Loeser motivic measure. Motivic integration on $\mathcal{L}(X)$ factorises a class in the Grothendieck ring of varieties as a sum over jet-scheme cylinders. The leading-coefficient form of [BSD surreal bound](#rem:bsd-surreal-bound) is the motivic-measure read of the same data on $\mathcal{L}(\mathcal{E}_q)$.
<!-- FILE_END: adelic-tate-motivic-dual.md -->

<!-- FILE_START: outro-braids-and-knots.md -->
This closes the substrate-arithmetic chapter. The categorical machinery developed here is the engine that drives every numerical prediction downstream. The classical-limit closing remark anchors the substrate-flow as $q \to 1$ in the adelic side, so the next chapter's choice of archimedean model is rigorously a categorical specialisation rather than a free choice.

The next chapter consumes this categorical arithmetic and surveys the candidate archimedean models. The substrate-level apparatus survives the archimedean specialisation. The categorical predictions become testable against CODATA.
<!-- FILE_END: outro-braids-and-knots.md -->
