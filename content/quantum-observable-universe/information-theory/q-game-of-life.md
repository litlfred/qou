**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with substrate parameter $q$ and Planck time $t_P(q) = 1/\hbar_q$.
Let $\mathcal{L} \subset M$ be a discrete sublattice of brane
points $\{p_i\}$ with each site carrying a qubit
$|\psi_i\rangle \in \mathcal{S}_{p_i}$ in the state bundle
([state bundle fibre convention](#def:reeb-bundle)). The
**$q$-Game of Life** ($q$-GoL) is the discrete-time unitary
cellular automaton*

$$
  \mathcal{U}_{\mathrm{q\text{-}GoL}}
    \colon  \mathcal{H}_{\mathcal{L}}
    \to  \mathcal{H}_{\mathcal{L}},
  \qquad
  |\Psi(t{+}1)\rangle
   = 
  \mathcal{U}_{\mathrm{q\text{-}GoL}}
  |\Psi(t)\rangle,
$$

*constructed entirely from $q$-deformed Toffoli gates
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix),
[q-AND](#rem:toffoli-q-and)) acting on the Reeb bundle fibres
of neighbour sites \cite{pena2022}. Specifically:*

1. **(Building block.)** *The non-linear transition operator is
 the $q$-AND*

$$
  \mathrm{Toff}_q
  \colon  |c_1, c_2, t\rangle
  \longmapsto
  |c_1, c_2,  t \oplus_q (c_1 \wedge_q c_2)\rangle,
$$

 *where $\wedge_q$ is the Hecke-algebra q-AND amplitude
 $\Phi(q) = (q - 1)(q^{3/2} + q^{1/2} - 1)
   (q^{3/2} + q + 1) / 2(q+1)^2$
 ([q-AND](#rem:toffoli-q-and)). Each $\mathrm{Toff}_q$
 executes in **$3$ Planck steps**
 ([Planck step](#rem:discrete-planck-step)).*

2. **(Superposition.)** *Cell states are prepared in
 "maybe-alive" superpositions $|\psi_i\rangle = \alpha_i|0\rangle + \beta_i|1\rangle$
 via Hadamard rotations $H \in \mathrm{End}(\mathcal{S}_{p_i})$.
 Hadamard generates a single-qubit gate outside the Clifford
 group, so $\{\mathrm{Toff}_q, H\}$ is universal for quantum
 computation ([universality](#prop:toffoli-transfer-matrix)).*

3. **(Conway's rules as Toffoli circuits.)** *Survival
 ($k = 2, 3$) and birth ($k = 3$) at site $i$ with
 neighbourhood $N(i)$ are realised by the composite operator*

$$
  \mathcal{U}_i^{\mathrm{rule}}
   = 
  \prod_{\{j_1, j_2\} \subset N(i)}
  \mathrm{Toff}_q
  \!\left(
    |\psi_{j_1}\rangle,  |\psi_{j_2}\rangle;  |\psi_i\rangle
  \right)
$$

 *composed via ancilla qubits to encode the neighbour sum.
 The binary count $k \in \{2, 3\}$ is computed via a
 ripple-carry adder of $O(|N(i)|)$ Toffoli gates acting on
 $\lceil \log_2 |N(i)| \rceil$ ancilla strands.*

4. **(Reversibility and energy conservation.)**
 *Each $\mathrm{Toff}_q$ is its own inverse:*

$$
  \mathrm{Toff}_q^\dagger  \mathrm{Toff}_q
   = 
  \mathbb{I},
$$

 *so $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is unitary. The
 classical dissipation of Conway's GoL is replaced by
 $q$-energy conservation
 ([quantum temperature](#def:quantum-temperature),
 [mass-energy equivalence](#thm:mass-energy-equivalence)):
 the $q$-energy* $\mathfrak{E}_q = \langle \Psi | \hat{H}_{\mathrm{q\text{-}GoL}} | \Psi \rangle$
 *is conserved along the automaton orbit, where
 $\hat{H}_{\mathrm{q\text{-}GoL}} = i\hbar_q \ln \mathcal{U}_{\mathrm{q\text{-}GoL}}/t_P$
 is the generator of the $q$-GoL unitary flow.*

5. **(Information bandwidth budget.)**
 *One $q$-GoL generation advances in $3 \cdot |\mathcal{L}|$
 Planck steps (one Toffoli per triple, three Planck steps
 each). The substrate bandwidth
 $\mathfrak{B}(q) = q \eta_q / (q - 1)^2$
 ([bandwidth](#def:information-speed-of-light)) bounds the
 number of generations per unit time:*

$$
  \text{gens / sec}
   \leq 
  \frac{\mathfrak{B}(q)}{3  |\mathcal{L}|}
   = 
  \frac{q \eta_q}{3  (q - 1)^2  |\mathcal{L}|}.
$$

**Stability condition.**
*The $q$-GoL evolution is well-defined — both the Toffoli
diagonal $P_{7,7}(q)$ and the q-AND amplitude $\Phi(q)$ are
strictly positive — on the physical regime*

$$
  q  >  1,
$$

*with three operator zeros in $(0, 1]$ that bound the
sub-physical behaviour: $q_\star = 1/\varphi^2 \approx 0.382$
(golden-ratio zero of $P_{7,7}$), $q_\Phi \approx 0.466$ (cubic
root of $\Phi$), and $q = 1$ (classical limit, $\Phi$ by definition
vanishes). See [Toffoli LP-stability](#prop:toffoli-lp-stability)
for the full table. The physical substrate value $q_0 \approx 1.110$
is safely inside the stable regime $q > 1$.*

**Remark (reference to Peña et al. and 't Hooft).**
Peña et al. \cite{pena2022} formalise $q$-GoL as a reversible
quantum circuit acting on a 2D lattice of qubits, with
neighbour counts implemented by Toffoli-based adder circuits.
The QOU framework subsumes this construction: their "Toffoli
gate" is the classical limit $q \to 1$ of our $q$-Toffoli, and
their "unitary tick" is $3$ Planck steps at substrate
parameter $q$. The QOU contribution is to identify the
$q$-deformed amplitude $\Phi(q)$ as the physical AND
amplitude, and to locate the golden-ratio threshold
$q = 1/\varphi^2$ as the boundary of the stability region.

The underlying philosophical motivation — that quantum mechanics
emerges from a deterministic Planck-scale cellular automaton via
information loss and coarse-graining — is developed systematically
in 't Hooft \cite{thooft2016}. The $q$-GoL construction
is the QOU realisation of that programme: the ontological CA
states are the Reeb bundle fibres $\mathcal{S}_p$, the CA tick
is the Planck step $t_P(q)$, and the $q$-deformation replaces
the information-loss mechanism with a categorical coarse-graining
via the Markov trace.
