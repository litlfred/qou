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
The symbol $\wedge_q$ denotes the Hecke-algebra q-AND amplitude $\Phi(q) = (q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1) / 2(q+1)^2$. Each $\mathrm{Toff}_q$ executes in three Planck steps.

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

4. **Reversibility and energy conservation.** Each $\mathrm{Toff}_q$ is unitary:
$$
  \mathrm{Toff}_q^\dagger  \mathrm{Toff}_q
   = 
  \mathbb{I}.
$$
Consequently, $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is unitary. Classical dissipation is replaced by $q$-energy conservation. The $q$-energy $\mathfrak{E}_q = \langle \Psi | \hat{H}_{\mathrm{q\text{-}GoL}} | \Psi \rangle$ is conserved along the automaton orbit, where $\hat{H}_{\mathrm{q\text{-}GoL}} = i\hbar_q \ln \mathcal{U}_{\mathrm{q\text{-}GoL}}/t_P$ generates the unitary flow.

5. **Information bandwidth budget.** One generation advances in $3 |\mathcal{L}|$ Planck steps. The substrate bandwidth $\mathfrak{B}(q) = q \eta_q / (q - 1)^2$ bounds the generation rate:
$$
  \text{gens / sec}
   \leq 
  \frac{\mathfrak{B}(q)}{3  |\mathcal{L}|}
   = 
  \frac{q \eta_q}{3  (q - 1)^2  |\mathcal{L}|}.
$$

**Stability condition.** The evolution is well-defined only when the Toffoli diagonal $P_{7,7}(q)$ and the q-AND amplitude $\Phi(q)$ are strictly positive. This requires the physical regime $q > 1$. The physical substrate value $q_0 \approx 1.110$ lies safely inside the stable regime.
