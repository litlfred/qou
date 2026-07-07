<!-- FILE_START: markov-trace-factorization.md -->
**Theorem.**
*Let $\mathcal{N}(Z, N)$ be the Gröbner-Shirshov-reduced nuclear braid word in $H_A(q)$. At each generator $\sigma_i$, let $(a_i, b_i)$ be the transfer-matrix-reduced chain coefficients. Let $z = 1/(q^{1/2} + q^{-1/2})$ be the Markov trace parameter. The Markov trace factors exactly:*

$$
  \mathrm{tr}_{\mathrm{Markov}}\!\bigl(
    \mathcal{N}(Z, N)
  \bigr)
  \;=\;
  \prod_{i=0}^{A-2}
  \bigl(z \cdot a_i + b_i\bigr).
$$

Each factor $\hat{V}_i = z \cdot a_i + b_i$ is a polynomial in $q$. The full trace is a product of polynomials, evaluating the nuclear Skein polynomial.

**The transfer matrix IS the polynomial.**
At each crossing between nucleons $i$ and $j$, the transfer matrix

$$
  T_j = 
  \begin{pmatrix}
    c_j(q - q^{-1}) + d_j & c_j \\
    c_j & d_j
  \end{pmatrix}
$$

carries polynomial entries. The crossing types determine the coefficients:

| Pair type | $c_j$ | $d_j$ | $\det(T_j)$ |
|---|---|---|:---:|
| $\mathfrak{p}$-$\mathfrak{p}$ | $1$ | $0$ | $-1$ |
| $\mathfrak{n}$-$\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ | $-1$ |
| mixed | $1$ | $-\frac{1}{2}(q - q^{-1})$ | $-1 - \frac{1}{4}(q - q^{-1})^2$ |

The product of $k_i$ transfer matrices at generator $\sigma_i$ yields $M_i \in \mathrm{GL}_2(\mathbb{Q}(q))$, whose entries are polynomials of degree bounded by $2k_i$. Then $\hat{V}_i(q) = z \cdot (M_i)_{11} + (M_i)_{21}$ evaluates the Skein polynomial $P_{\mathcal{N}}(q) = \prod_{i=0}^{A-2} \hat{V}_i(q)$ in factored form.

**Asymptotic behaviour.**
For heavy nuclei ($A \gg 1$), the ratio of $L_0^{-}$ and parent traces converges:

$$
  \frac{\mathrm{tr}(L_0^{-})}{\mathrm{tr}(\mathcal{N})}
   \;\longrightarrow\;
  \frac{1}{\hbar_q}
  \;=\;
  \frac{1}{1 - q^{-1}}
   \;\approx\;  10.09.
$$

The sub-leading $O(1/A)$ correction carries the nucleus-specific shell structure and pairing data.
<!-- FILE_END: markov-trace-factorization.md -->

<!-- FILE_START: ks-multiplicativity-via-markov.md -->
Kontsevich and Soibelman prove that the Donaldson-Thomas counting map acts as a monoid homomorphism (disjoint union maps to product) via the motivic Hall algebra. The QOU framework recovers this multiplicativity directly via the Markov trace.

**Two-line proof.** 
A split braid $\beta \sqcup \beta'$ contains no generator linking the two blocks. The right-to-left Markov peel processes the two blocks independently. Hence

$$
  \mathrm{tr}_M(\beta \sqcup \beta')
  \;=\;
  \mathrm{tr}_M(\beta)\,\mathrm{tr}_M(\beta'),
$$

making $\mathrm{tr}_M$ a monoid homomorphism from the disjoint-union monoid of links to $\mathbb{Z}[q^{\pm 1/2}]$.

This applies strictly to the disjoint-union monoidal structure, not the internal product. It avoids the wall-crossing archimedean apparatus entirely.
<!-- FILE_END: ks-multiplicativity-via-markov.md -->

<!-- FILE_START: markov-trace-ratio-exact.md -->
**Proposition (normalization-independence of Markov-trace ratios).**
*For braids $\beta_1, \beta_2 \in B_n$ with $\operatorname{tr}_M(\beta_2) \neq 0$, and for the Jones normalisation factor $C(n, q) = (-q^{1/2} - q^{-1/2})^{n-1}$:*

$$
  \frac{J_{K_1}(q)}{J_{K_2}(q)}
  \;=\;
  \frac{C(n, q) \cdot \operatorname{tr}_M(\beta_1)}{C(n, q) \cdot \operatorname{tr}_M(\beta_2)}
  \;=\;
  \frac{\operatorname{tr}_M(\beta_1)}{\operatorname{tr}_M(\beta_2)}.
$$

*The Gram matrix $G_{ij} = \operatorname{tr}_M(b_i \cdot b_j)$, the LP cost vectors $t_k = \operatorname{tr}_M(b_k)$, and the shadow prices $y^*$ from the operator-selection LP are exact up to a global scalar that cancels in every ratio and optimality condition.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued physical observables at $q_0$.
<!-- FILE_END: markov-trace-ratio-exact.md -->

<!-- FILE_START: vassiliev-filtration-mass-tower.md -->
The Markov trace $\operatorname{tr}_M(\beta)(q)$ expands about $q = 1$ in the Hecke deformation parameter $h = q - q^{-1}$:

$$
  \operatorname{tr}_M(\beta)(q)
  \;=\;
  c_0(\beta)
  \;+\;
  c_1(\beta) \cdot h
  \;+\;
  c_2(\beta) \cdot h^2
  \;+\;
  \cdots
$$

Each coefficient $c_k(\beta)$ is a Vassiliev invariant of type $k$. The graded decomposition by type establishes a canonical filtration by complexity. The leading term $c_0$ is the classical Markov trace. The type-2 term $c_2 \cdot h^2$ introduces the first mass-discriminating framing correction. Higher-order terms supply precision refinements, converging rapidly due to the suppression factor $|h|^k \approx (0.209)^k$ at $q_0 \approx 1.110$.

For the LP/SDP operator-selection framework, the Vassiliev filtration provides a canonical cost-vector basis at each type: $t_k^{(\mathrm{type}\,m)} = c_m(b_k)$. This decomposes the mass-formula optimisation into a graded hierarchy of independent linear programs.
<!-- FILE_END: vassiliev-filtration-mass-tower.md -->

<!-- FILE_START: hecke-quandle.md -->
A quandle encodes the three Reidemeister moves algebraically via idempotency, right-invertibility, and self-distributivity. The Hecke algebra's quadratic relation $\sigma_i^2 = h \sigma_i + 1$ defines the natural Hecke quandle $Q_H(q)$:

$$
  a \triangleright_H b
  \;:=\;
  h \cdot b + \sigma_i^{-1} a \sigma_i.
$$

The knot quandle constitutes a complete invariant of oriented prime knots, distinguishing structures that the HOMFLYPT polynomial conflates.

The mass formula employs averaged crossings $I = \sigma - (h/2) \cdot 1$ whose coefficient depends on the quark flavour. This parameterised quandle rule varies over the $\mathrm{SU}(3)$ flavour representation. The quandle coloring number counts the physically distinct baryonic states within a topological class. The Markov trace operates as a quandle cocycle invariant, conferring a representation-theoretic interpretation upon the Gram matrix.
<!-- FILE_END: hecke-quandle.md -->

<!-- FILE_START: knot-operator-bring-action.md -->
The six Gröbner-Shirshov normal-form basis elements of $H_3(q)$ act on the Bring surface $\Sigma_4$ via the Hecke representation. The three quark strands of a baryon thread through the color-tube cubic on $\Sigma_4$, with the three roots representing quark positions.

Each basis operator $b_k \in H_3(q)$ permutes and $q$-deforms these roots. At $q_0 \neq 1$, crossings shift the root positions along the color-tube fibre by a factor of $q$ or $q^{-1}$.

The six basis operators generate the discrete subgroup $S_3 \subset \mathrm{SO}(3)$, embedded as the symmetry group of the equilateral triangle cross-section. The continuous $\mathrm{SO}(3)/S_3$ rotations remain excluded from the pipeline. Restricting to $S_3$ isolates the discrete crossing transformations.

On the Bring surface, the Gram inverse $G^{-1}$ functions as the metric inverse between the knot-operator basis and the Frobenius dual basis. The LP/SDP operator selection minimises the action functional over the moduli space of braid embeddings on $\Sigma_4$.
<!-- FILE_END: knot-operator-bring-action.md -->

<!-- FILE_START: phi-q-resums-trace-series.md -->
The closed-form quantum dilogarithm

$$
  \Phi_q(z) \;=\; \prod_{k \geq 1}(1 - q^{-k} z)^{-1}
$$

appears to introduce a non-trace transcendental species into the six-term mass formula. It does not. The $\Phi_q$ resummation strictly factors through Markov traces of the identical per-generator subwords used by the baseline term.

Using the expansion $\Phi_q(z) = \exp\!\bigl[\sum_{k \geq 1} z^k / (k(1 - q^k))\bigr]$, each evaluation unpacks into a series of Plancherel-weighted Markov traces. The transient summands represent the Kähler differentials of $\mathrm{tr}_M$ in the substrate parameter $q$. The entire tower generates from symbolic differentiation of the descended trace.

The $\Phi_q$ resummation provides exact computational convenience, yet the underlying algebraic engine remains the canonical Jones-Markov trace applied to atomic braids and their derivatives.
<!-- FILE_END: phi-q-resums-trace-series.md -->

<!-- FILE_START: markov-axiom-recursive-ascent.md -->
**Definition (Markov-axiom recursive ascent).**
*Given a braid $\beta \in B_n$ with Hecke representative $T_w \in H_n(q)$ in Gröbner-Shirshov normal form, the recursive ascent algorithm evaluates the canonical Jones-Markov trace $\mathrm{tr}_M^{(n)}(T_w)$ by:*

1. *Eliminating inverse generators via $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$.*
2. *Peeling the top generator to yield $\mathrm{tr}_M^{(n)}(T_w) = z \cdot \mathrm{tr}_M^{(n-1)}(T_{w'})$.*
3. *Branching on the Hecke quadratic $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$.*
4. *Recursing on $T_{w'}$ until reaching the base case $\mathrm{tr}_M^{(1)}(\mathbf{1}) = 1$.*

The recursive ascent path boundedly evaluates the trace without materialising unwieldy symbolic matrix representations. The production implementation completes the $^4\mathrm{He}$ mass derivation end-to-end in ~60 seconds.
<!-- FILE_END: markov-axiom-recursive-ascent.md -->

<!-- FILE_START: per-braid-mass-tower.md -->
**Proposition (per-braid mass tower — full jet-level form).**
*Let $W \in B_{3A}$ be the atomic braid of a nucleus $(Z, N)$. The mass functional decomposes as*

$$
  \mathfrak{m}(W)
  \;=\;
  \bigl|\mathrm{tr}_M(W)\bigr|
  \;+\;
  \sum_{n=0}^{N}
    \left(
      \sum_{\xi \in \mathcal{S}^{(n)}_1}
        \Phi_q\!\bigl(|\mathrm{tr}_M(\xi)|\bigr)
      \;+\;
      z^{2}\sum_{(\xi,\xi') \in \mathcal{S}^{(n)}_2}
        \Phi_q\!\bigl(|\mathrm{tr}_M(\xi\,\xi')|\bigr)
    \right).
$$

*The descended term enters exclusively at level 0. The sum integrates transient singlet and pair corrections over all higher jet levels.*
<!-- FILE_END: per-braid-mass-tower.md -->
