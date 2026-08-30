Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$ and Planck time $t_P(q) = 1/\hbar_q$. Let $\mathcal{L} \subset M$ be a discrete sublattice of brane points $\{p_i\}$. Each site carries a qubit $|\psi_i\rangle \in \mathcal{S}_{p_i}$. The **$q$-Game of Life** ($q$-GoL) is the discrete-time unitary cellular automaton
$$
  \mathcal{U}_{\mathrm{q\text{-}GoL}}
    \colon  \mathcal{H}_{\mathcal{L}}
    \to  \mathcal{H}_{\mathcal{L}},
  \qquad
  |\Psi(t{+}1)\rangle
   = 
  \mathcal{U}_{\mathrm{q\text{-}GoL}}
  |\Psi(t)\rangle.
$$
The operator $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is constructed entirely from $q$-deformed Toffoli gates acting on Reeb bundle fibres of neighbour sites. The construction requires five properties:

1. **Building block.** The transition operator is the $q$-AND gate:
$$
  \mathrm{Toff}_q
  \colon  |c_1, c_2, t\rangle
  \longmapsto
  |c_1, c_2,  t \oplus_q (c_1 \wedge_q c_2)\rangle.
$$
The symbol $\wedge_q$ denotes the Hecke-algebra q-AND amplitude $\Phi(q) = (q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1) / \bigl(2(q+1)^2\bigr)$. Each $\mathrm{Toff}_q$ executes in three Planck steps.

2. **Superposition.** Cell states admit superpositions $|\psi_i\rangle = \alpha_i|0\rangle + \beta_i|1\rangle$ via Hadamard rotations $H \in \mathrm{End}(\mathcal{S}_{p_i})$. The set $\{\mathrm{Toff}_q, H\}$ is universal for quantum computation.

3. **Conway's rules as Toffoli circuits.** Survival ($k = 2, 3$) and birth ($k = 3$) at site $i$ with neighbourhood $N(i)$ are enacted by the composite operator
$$
  \mathcal{U}_i^{\mathrm{rule}}
   = 
  \prod_{\{j_1, j_2\} \subset N(i)}
  \mathrm{Toff}_q
  \!\left(
    |\psi_{j_1}\rangle,  |\psi_{j_2}\rangle;  |\psi_i\rangle
  \right).
$$
Ancilla qubits encode the neighbour sum. A ripple-carry adder of $O(|N(i)|)$ Toffoli gates computes the binary count $k$.

4. **Reversibility.** Each $\mathrm{Toff}_q$ is invertible, with
$$
  \sigma_i^{-1}
   = 
  \sigma_i - (q - q^{-1})\cdot \mathbb{1},
$$
so $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is invertible and the automaton is reversible. It is **not** unitary away from the classical limit: the eigenvalues of $\sigma_i$ are $q$ and $-q^{-1}$, of modulus $\neq 1$ for $q \neq 1$, so no inner product makes $\mathrm{Toff}_q$ unitary, and the Markov trace form is degenerate under the production trace convention. Reversibility in the sense a reversible cellular automaton requires — invertibility of the tick — therefore holds for every $q > 0$, being a property of the quadratic relation alone and independent of the amplitude signs discussed below; unitarity holds only at $q = 1$.

5. **Information bandwidth budget.** One generation advances in $3 |\mathcal{L}|$ Planck steps. The substrate bandwidth $\mathfrak{B}(q) = q \eta_q / (q - 1)^2$ bounds the generation rate:
$$
  \text{gens / sec}
   \leq 
  \frac{\mathfrak{B}(q)}{3  |\mathcal{L}|}
   = 
  \frac{q \eta_q}{3  (q - 1)^2  |\mathcal{L}|}.
$$

**Stability condition.** The evolution is well-defined only when the Toffoli diagonal $P_{7,7}(q)$ and the q-AND amplitude $\Phi(q)$ are strictly positive. In the canonical convention $z_D = q^3/(q^2+1)$ the two amplitudes are

$$
  P_{7,7}^{D}(q) \,=\, \frac{q^{3}\bigl(q^{4}+1\bigr)}{\bigl(q^{2}+1\bigr)^{2}},
  \qquad
  \Phi^{D}(q) \,=\, -\,\frac{(q-1)(q+1)\bigl(q^{6}+q^{4}+2q^{2}+1\bigr)}{2q\bigl(q^{2}+1\bigr)^{2}},
$$

the first having no positive root and the second carrying its sign entirely in the factor $(q-1)$, the sextic having no positive real root. The region on which both are strictly positive is therefore $0 < q < 1$, and the substrate value $q_0 \approx 1.110$ lies outside it: there $\Phi^{D}(q_0) \approx -0.1438$. The regime $q > 1$ previously named here, and the golden-ratio threshold $q_\star = 1/\varphi^{2}$ from which it was read off, are both artifacts of the excised convention $C$ (see [Toffoli LP-stability](#prop:toffoli-lp-stability) and [Toffoli q-AND](#rem:toffoli-q-and)).

Whether strict positivity is the condition a reversible automaton actually requires is a separate question, and it is open. The universality argument of [Toffoli q-AND](#rem:toffoli-q-and) turns on $\Phi \neq 0$ rather than $\Phi > 0$, and the two conditions give opposite verdicts at the substrate: non-vanishing holds for every $q \neq 1$, strict positivity only below $1$. Which one governs is not settled here.
