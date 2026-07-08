<!-- FILE_START: vertex-factorisation-feynman-intro.md -->
The preceding sub-section developed the vertex-factorisation machinery. This sub-section identifies the same factorisation within the Feynman framework. We establish the Feynman eigenbasis decomposition, the trace collapse, the Feynman-Markov identification, the Feynman-QOU dictionary, and the classical limit. These two sub-sections together unify the vertex-algebra and Feynman views of the exceptional-divisor structure.

This output yields the Feynman eigenbasis decomposition with explicit categorical-trace evaluations. The subsequent sub-section consumes this trace collapse as its substrate-level input for the Kashaev volume bridge.
<!-- FILE_END: vertex-factorisation-feynman-intro.md -->

<!-- FILE_START: feynman-eigenbasis-decomposition.md -->
*Let $V$ be the fundamental representation of $\mathrm{SU}_q(2)$ with $q$ not a root of unity. Let $\beta \in B_n$ act on $V^{\otimes n}$ via the braid group representation $\rho_n \colon B_n \to \mathrm{Aut}(V^{\otimes n})$. Then*

$$
  V^{\otimes n}
  \cong
  \bigoplus_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  V_\lambda \otimes S_\lambda,
$$

*where $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin $j = (\lambda_1 - \lambda_2)/2$ and $S_\lambda$ is the irreducible $H_n(R, q)$-module. The braid $\beta$ acts on each $S_\lambda$ via the quotient map $B_n \to H_n(R, q)$. The number of summands is $\lfloor n/2 \rfloor + 1$, which is finite for every $n$.*
<!-- FILE_END: feynman-eigenbasis-decomposition.md -->

<!-- FILE_START: feynman-trace-collapse.md -->
*Suppose $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ admits the complete eigenbasis of ([eigenbasis decomposition](#lem:feynman-eigenbasis-decomposition)). Then the Feynman path integral*

$$
  \langle\psi_f|\psi_i\rangle
  =
  \int \mathcal{D}\phi\,e^{iS[\phi]/\hbar}
$$

*collapses to a finite weighted sum over the irreducible summands $V_\lambda \otimes S_\lambda$. No regularisation is needed because $V^{\otimes n}$ has finitely many irreducible summands due to the semisimplicity of $H_n(R, q)$ at non-root-of-unity $q$.*
<!-- FILE_END: feynman-trace-collapse.md -->

<!-- FILE_START: feynman-markov-identification.md -->
*Let $\beta \in B_n$ act on $V^{\otimes n}$ via $\rho_n$. The transition amplitude on the eigenbasis is the Markov-weighted sum of partial traces:*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  :=
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr).
$$

*This equals the Jones--Markov trace $\mathrm{tr}_M\bigl(\rho(\beta)\bigr)$ on $H_n(R, q)$, where the Markov weights are $w_\lambda = \dim_q(V_\lambda) \cdot \dim(S_\lambda) / \dim_q(V^{\otimes n})$.*
<!-- FILE_END: feynman-markov-identification.md -->

<!-- FILE_START: feynman-categorical-trace.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\mathbf{C} = \mathbf{Rep}(\mathrm{SU}_q(2))$, $V$ the fundamental representation, and $q$ not a root of unity. Let $\varrho \colon \mathbf{1} \to A$ be a closed cycle with braid representative $\beta \in B_n$.

**Proposition.**
*The Feynman transition amplitude evaluated on the knot-type eigenbasis equals the Jones--Markov trace of the braid representation in the Hecke algebra:*

$$
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  =
  \sum_{\substack{\lambda \vdash n \\ \ell(\lambda) \leq 2}}
  w_\lambda \cdot \mathrm{tr}_{S_\lambda}\bigl(\rho_n(\beta)\bigr)
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr),
$$

*where the sum spans partitions $\lambda \vdash n$ with at most two parts. The Markov weights $w_\lambda$ satisfy the Markov property $\mathrm{tr}_M(x \sigma_n^{\pm 1}) = z^{\pm 1}\mathrm{tr}_M(x)$ and evaluate to $w_\lambda = \dim_q(V_\lambda) \cdot \dim(S_\lambda) / \dim_q(V^{\otimes n})$, with $\dim_q(V_\lambda) = [2j+1]_q$.*

*The transition amplitude is a finite sum over $\lfloor n/2 \rfloor + 1$ terms. Its absolute value equals the categorical mass at a single brane level:*

$$
  \mathfrak{m}(\varrho)\big|_{\text{single level}}
  =
  \mathrm{tr}_M\bigl(\rho(\beta)\bigr)
  =
  \bigl|
  \langle\psi_f|\psi_i\rangle_{\mathrm{eigenbasis}}
  \bigr|.
$$
<!-- FILE_END: feynman-categorical-trace.md -->

<!-- FILE_START: feynman-qou-dictionary.md -->
The correspondence between the Feynman path integral formalism and the QOU categorical trace is strict.

See [Table](#tbl:feynman-qou-dictionary-table-data).

**Three finite computations of the path integral.**
The categorical trace admits three independent evaluation methods, each producing the same finite answer without regularisation:

1. **Multiplicative integral** (analytic):
   $\mathfrak{m} = \lVert\mathrm{MI}\int_\Sigma(\nabla_A q, L \wedge F^+)\rVert$.
   The surface $\Sigma$ is the disc swept by the photon threading the hadron braid. The multiplicative integral accumulates the connection along this surface.

2. **Ribbon trace** (algebraic):
   $\mathfrak{m} = \lVert\mathrm{tr}_{\mathrm{ribbon}}(\rho(\beta))\rVert \cdot (q-1)^2$.
   The Reshetikhin--Turaev invariant evaluated in the ribbon category gives the crossing energy. The factor $(q-1)^2 = c_q^{-2}$ converts to mass.

3. **Gröbner--Shirshov reduction** (computational):
   $\mathfrak{m} = (q-1)^2 \sum |c_w| \cdot |q - q^{-1}|$.
   Each Hecke step $\sigma_i^2 \to (q - q^{-1})\sigma_i + 1$ contributes a discrete term. Yang--Baxter moves are free. Confluence ensures path independence (gauge invariance).

**Photon threading as insertion of a complete set of states.**
The Feynman propagator inserts a complete set of intermediate states. The QOU analogue is photon threading. The photon strand $\gamma$ passes through the hadron braid $\beta_{\mathfrak{H}}$, encountering each crossing sequentially. Each crossing contributes a Hecke step (eigenvalue insertion). The braid crossings act as intermediate states. The Hecke relation provides the eigenvalue decomposition at each insertion.
<!-- FILE_END: feynman-qou-dictionary.md -->

<!-- FILE_START: feynman-classical-limit.md -->
**Proposition (conditional on [`conj:classical-limit-stpart`](#conj:classical-limit-stpart) — classical limit).**
*In the $q \to 1$ limit of the categorical trace, the following degenerations occur:*

1. **(Hecke $\to$ symmetric group.)**
   *The Hecke relation $(T - q)(T + q^{-1}) = 0$ becomes $T^2 = 1$. The Iwahori--Hecke algebra $H_n(R, q)$ degenerates to the group algebra $k[S_n]$.*

2. **(Markov trace $\to$ flat character trace.)**
   *The Jones--Markov trace parameter $z \to 0$. The Markov trace $\mathrm{tr}_M$ on $H_n(R, q)$ degenerates to the augmentation map $\varepsilon \colon k[S_n] \to k$ sending every group element to $1$.*

3. **(Categorical action $\to$ classical action.)**
   *The categorical action $\mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta)) \to \mathfrak{S}_1(\beta)$, the character of the permutation $\pi(\beta) \in S_n$. The $q$-energy reduces to the classical action because the rotational and translational terms vanish with $\hbar_q = 1 - q^{-1} \to 0$.*

4. **(Eigenbasis collapse.)**
   *The Jones polynomial evaluates to $J_K(1) = 1$ for every knot $K$. The Markov trace ceases to distinguish knot types. The eigenspace decomposition $V^{\otimes n} \cong \bigoplus_\lambda V_\lambda \otimes S_\lambda$ persists, but the $S_\lambda$ become Specht modules of $S_n$, forming the standard angular momentum eigenbasis. The quantum dimensions $[2j+1]_q$ become ordinary dimensions $2j+1$.*

5. **(Braiding $\to$ symmetric.)**
   *The braiding $c_{V,V}$ satisfies $c_{V,V}^2 = \mathrm{id}$, making the monoidal category symmetric. The non-trivial knot structure collapses, reducing all braid closures to the unknot.*

*The finite categorical trace degenerates to the standard discrete trace over the finite-dimensional angular momentum eigenbasis of the symmetric group.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: feynman-classical-limit.md -->

<!-- FILE_START: feynman-classical-limit-interpretation.md -->
The classical limit reveals how the QOU categorical trace degenerates to the standard quantum-mechanical formalism.

**The Hecke degeneration.**
At $q = 1$, the minimal polynomial of the braiding drops from a quadratic with distinct roots $q \neq -q^{-1}$ to a quadratic with roots $\pm 1$. The eigenspaces $S^2 V$ and $\Lambda^2 V$ merge into the $+1$ and $-1$ eigenspaces of the symmetric group transposition. The Hecke algebra $H_n(R, q)$ becomes $k[S_n]$.

**Loss of knot discrimination.**
The Jones polynomial satisfies $J_K(1) = 1$ for every knot $K$. The Markov trace becomes constant. All knots become topologically trivial under the symmetric quotient $B_n \twoheadrightarrow S_n$. The irreducible $H_n(R, q)$-modules $S_\lambda$ become Specht modules of $S_n$. This yields the standard angular momentum eigenbasis $|j, m\rangle$ for the $\mathrm{SU}(2)$-coupling of $n$ spin-$\frac{1}{2}$ particles.

**Vanishing of quantum corrections.**
At $q = 1$, the quantum Planck constant $\hbar_q \to 0$ and the speed of light $c_q \to \infty$. The $q$-energy reduces to the classical action. The topological mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ diverges as $\hbar_q \to 0$ for hyperbolic knots with $\mathrm{Vol}(K) > 0$. The classical limit assigns infinite mass to knotted configurations, consistent with the classical expectation that only unknotted particles have finite mass.

**The finite sum persists.**
The decomposition $V^{\otimes n} = \bigoplus_\lambda V_\lambda \otimes S_\lambda$ remains valid at $q = 1$ with the same number of summands. The trace formula is a finite sum over $\lfloor n/2 \rfloor + 1$ terms. This constitutes the standard trace over the Clebsch--Gordan decomposition of $(\mathbb{C}^2)^{\otimes n}$. The divergences of the continuum Feynman integral arise from the $n \to \infty$ passage without the Hecke relation that organizes the tower into a convergent topological invariant at $q \neq 1$.
<!-- FILE_END: feynman-classical-limit-interpretation.md -->

