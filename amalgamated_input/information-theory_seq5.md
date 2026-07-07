<!-- FILE_START: planck-scale-computation-intro.md -->
This section develops computation at Planck time lengths. We analyze substrate-level Planck-scale computation, the Toffoli transfer matrix, and the $q$-deformed AND gate. We then use linear-program stability analysis to pin the Toffoli gate's operational regime.

We lift this substrate-level construction into a $q$-deformed game of life. We identify the substrate computation as a model of quantum-computational universality. We conclude with the skein Turing machine. This machine provides the categorical embodiment of substrate-level Church–Turing equivalence, establishing the falsifiability of the information-theoretic framework.
<!-- FILE_END: planck-scale-computation-intro.md -->

<!-- FILE_START: planck-scale-computation.md -->
We frame every Planck-time step as the application of a single transfer matrix on the brane fibre. The product of the matrices encountered along the braid word determines the total cost of a finite computation. The per-step entropy is the operational entropy $\eta_q$ of the substrate.

The technical components construct this computational model:

- [Toffoli transfer matrix](#prop:toffoli-transfer-matrix): We realize the universal classical gate as a $2 \times 2$ matrix on $\Sigma_3$.
- [Toffoli $q$-AND amplitudes](#rem:toffoli-q-and): We provide the explicit amplitude formula and its $q \to 1$ limit.
- [Toffoli LP stability](#prop:toffoli-lp-stability): We demonstrate the robustness of the gate's binding under noise.
- [$q$-Game of Life](#prop:q-game-of-life): We work through a discrete dynamical system on the substrate.
- [Substrate computation](#rem:substrate-computation): We explain why the combinatorics is medium-independent.
- [Quantum computational universality](#conj:quantum-computational-universality) and [Skein Turing machine](#rem:skein-turing-machine): We present the closure argument, showing every Turing machine of $N$ gates encodes as a braid with $c = 3N$ crossings.

Each Planck step applies one of these matrices. The bandwidth $\mathfrak{B}(q)$ bounds the information-theoretic cost ([information speed of light](#def:information-speed-of-light)).
<!-- FILE_END: planck-scale-computation.md -->

<!-- FILE_START: toffoli-transfer-matrix.md -->
**Proposition.**
*Let $P_{\mathrm{flip}}(q; k_1, k_2)$ be the target-flip amplitude on a $3$-strand nuclear braid with control types $(k_1, k_2) \in \{0,1\}^2$ and target strand $3$. It is constructed from the Hecke crossing coefficients ([transfer matrix product](#prop:skein-polynomial-transfer-matrix)). Then:*

1. **(Universal factorization.)** *Every target-flip amplitude factors as:*

$$
  P_{\mathrm{flip}}(q; k_1, k_2) = c_{k_1 k_2}(q) \cdot \Phi(q)
$$

*Here, $c_{k_1 k_2}$ is the crossing coefficient of the **control–control pair** (the two strands that do not flip). The term $\Phi(q)$ is a **universal core amplitude** independent of the control types:*

$$
  \Phi(q) = \frac{(q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1)}{2(q + 1)^2}
$$

| Control pair | $c_{k_1 k_2}$ | $d_{k_1 k_2}$ |
|:------------:|:--------------:|:--------------:|
| $\mathfrak{p}\mathfrak{p}$ | $1$ | $0$ |
| mixed | $1$ | $-\frac{q - q^{-1}}{2}$ |
| $\mathfrak{n}\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ |

2. **(Target-flip blindness of the control crossing.)** *Generator $\sigma_1$ is the single control–control crossing. Its traced volume $\hat{V}_1 = z(q)\,c + d$ is type-dependent ($z$ for $\mathfrak{p}\mathfrak{p}$, $z - \tfrac{q - q^{-1}}{2}$ for mixed, $z - (q - q^{-1})$ for $\mathfrak{n}\mathfrak{n}$). A target-flip leaves the control crossing unchanged. Therefore, $\Delta_1 = 0$ for every target-flip transition. The entire target-flip amplitude is concentrated at generator $\sigma_0$ (whose chain has $2$ crossings).*

3. **(The q-AND = governor choice.)** *The Toffoli gate selects the target strand whose control–control pair has $c = 1$ ($\mathfrak{p}\mathfrak{p}$ crossing). Among the $S_3$ orbit of target choices in the exceptional divisor, this forms the **governor basis**: the choice with unit prefactor.*

$$
  P_{7,6}(q) = 1 \cdot \Phi(q) = \frac{(q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1)}{2(q+1)^2}
$$

4. **(Antisymmetry.)** *$P_{6,7}(q) = -P_{7,6}(q)$.*

5. **(Classical limit.)** *All target-flip amplitudes vanish as $q \to 1$. The core $\Phi(q)$ carries the factor $(q - 1)$.*

6. **(Toffoli diagonal.)**

$$
  P_{7,7}(q) = \frac{q + q^{1/2} - 1}{q + 1}
$$

*This entry vanishes at $q = 1/\varphi^2$ ([golden ratio degeneration](#rem:golden-ratio-degeneration)). The all-proton diagonal amplitude has a zero at the golden ratio threshold.*
<!-- FILE_END: toffoli-transfer-matrix.md -->

<!-- FILE_START: toffoli-transfer-matrix-interpretation.md -->
**Explicit values at $q = q_0$
([local substrate $q$](#prop:local-substrate-q)):**

| Controls | $c_{k_1 k_2}$ | $P_{\mathrm{flip}}$ | $P_{7,6}$ ratio |
|:--------:|:-----------:|:-------------------:|:---:|
| $\mathfrak{p}\mathfrak{p}$ | $1$ | $+0.0495$ | $1\times$ |
| mixed | $1$ | $+0.0495$ | $1\times$ |
| $\mathfrak{n}\mathfrak{n}$ | $1$ | $+0.0495$ | $1\times$ |

| Entry | Symbolic | Numerical |
|:-----:|----------|:---------:|
| $P_{6,6}$ | $\frac{q^4 + q^{7/2} + 2q^{3/2} + q^{1/2} - 1}{2(q+1)^2}$ | $0.6010$ |
| $P_{7,6}$ | $\Phi(q)$ (q-AND) | $+0.0495$ |
| $P_{6,7}$ | $-\Phi(q)$ | $-0.0495$ |
| $P_{7,7}$ | $\frac{q + q^{1/2} - 1}{q + 1}$ | $0.5515$ |
<!-- FILE_END: toffoli-transfer-matrix-interpretation.md -->

<!-- FILE_START: toffoli-q-and.md -->
The polynomial $P_{7,6}(q)$ is the **q-AND**: the $q$-deformed AND gate realised by braiding. In the classical Toffoli gate (CCNOT), the target bit flips iff both control bits are $1$. The $3$-strand nuclear braid replaces the Boolean AND with a topological amplitude. Two control particles must braid around the target to flip its phase. All other phase-flip pathways destructively interfere to zero ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).

**Three Planck steps.**
The $3$-strand Toffoli braid contains $\binom{3}{2} = 3$ crossings. A single crossing is not a complete topological operation. One must close the full braid loop. The complete Toffoli gate therefore executes in exactly **$3$ Planck steps** ([discrete Planck step](#rem:discrete-planck-step)), allocating one step per crossing.

| Epoch | $q$ | $t_P(q)$ | Toffoli ($3$ steps) | $P_{7,6}$ |
|-------|:---:|:---------:|:-------------------:|:---------:|
| Big Bang | $\to \infty$ | $\to 1$ | $3$ units | $\to \infty$ |
| Physical | $q_0$ | $10.11$ | $30.3$ units | $+0.050$ |
| Classical | $\to 1$ | $\to \infty$ | $\infty$ | $0$ |

At the Big Bang, each Planck step is one unit of time. The Toffoli gate executes in the shortest possible time. Near the classical limit, the Planck step diverges and the gate freezes. Braiding ceases to operate. The q-AND amplitude itself vanishes as $(q - 1) \to 0$.

**Factor anatomy.**
The three factors of $P_{7,6}(q)$ each dictate a physical consequence:

1. $(q - 1)$: **departure from classicality**. The q-AND exists only away from the classical limit. Its magnitude is proportional to the quantum deformation.
2. $(q^{3/2} + q^{1/2} - 1)$: a cubic (in $q^{1/2}$) with a real zero at $q \approx 0.466$. Below this threshold, the q-AND changes sign. The target acquires a phase reversal rather than a simple flip.
3. $(q^{3/2} + q + 1)$: strictly positive for all $q > 0$. This factor carries no zeros and provides the baseline amplitude.

**Antisymmetry.**
The identity $P_{6,7}(q) = -P_{7,6}(q)$ implies the forward and reverse Toffoli transitions have equal magnitude but opposite sign. Creating a proton from a neutron (target $0 \to 1$) and annihilating one ($1 \to 0$) are related by a sign. This matches the asymmetry of the beta decay matrix $\Delta_\beta = T_{\mathrm{mix}} - T_{nn} = T_{pp} - T_{\mathrm{mix}}$.

**Universality.**
The Toffoli gate is universal for reversible classical computation \cite{toffoli1980}. Any Boolean circuit can be simulated by a circuit of Toffoli gates with ancilla bits. Bennett \cite{bennett1973} showed that any irreversible Turing machine can be simulated by a reversible one (hence by Toffoli gates alone) with at most polynomial overhead in time and space. Combined with a single-qubit gate outside the Clifford group (e.g. the Hadamard gate), the Toffoli gate achieves universality for quantum computation \cite{fredkin1982}. The existence of a non-zero $P_{7,6}(q)$ in the Iwahori--Hecke algebra confirms that the substrate's braiding dynamics, evaluated at discrete Planck steps, is computationally universal.
<!-- FILE_END: toffoli-q-and.md -->

<!-- FILE_START: toffoli-lp-stability.md -->
**Proposition.**
*Let $T_q \in H_3(q)$ be the $q$-Toffoli element. It is realised as the $3$-strand braid word whose traced volume matrix is $M(q)$ ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)). Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix of the normal-form basis ([Gram matrix](#prop:frobenius-gram-matrix)). Write the $q$-Toffoli in NF coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$. Then:*

1. **(Stability region.)** *The $q$-Toffoli element is LP-stable ([LP-dual stability](#prop:lp-dual-stability)) on the **physical regime** $q > 1$. All Hecke amplitudes have the correct sign. The confinement LP ([confinement as LP](#prop:confinement-lp)) is feasible. Three operator zeros in $(0, \infty)$ delimit sub-physical behaviour:*

$$
  q_\star \,=\, 1/\varphi^2 \,=\, (3 - \sqrt{5})/2 \,\approx\, 0.3820,
  \qquad
  q_\Phi \,\approx\, 0.4656,
  \qquad
  q \,=\, 1,
$$

   *where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio.*

2. **(Three operator thresholds.)** *Each zero corresponds to a vanishing Hecke amplitude:*

See [Table 1](#tbl:toffoli-lp-stability-table1-data).

   *At $q_\star$, the diagonal amplitude $P_{7,7}$ vanishes. At $q_\Phi$, the q-AND amplitude $\Phi$ reverses sign. At $q = 1$, the q-AND vanishes. The classical reversible Toffoli has trivial amplitude here.*

3. **(Dual shadow prices.)** *For $q > 1$, the LP dual has bounded shadow prices $y_i^*(q)$ satisfying:*

$$
  |y_i^*(q)| \leq \kappa(\mathrm{G}(q)) \cdot \|t(q)\|,
$$

   *where $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$ is the Gram condition number. At the physical substrate value $q_0 \approx 1.110$, $\kappa(G(q_0)) \approx 3.03$ (verified in the witness file). All shadow prices remain bounded in Skein units.*

4. **(Physical-substrate stability.)** *At $q_0 \approx 1.110$:*

$$
  P_{7,7}(q_0) \,\approx\, 0.5514,
  \qquad
  \Phi(q_0) \,\approx\, 0.0495.
$$

   *Both are strictly positive. The $q$-Toffoli is LP-stable at the physical substrate value. The set $\{q$-Toffoli$, H\}$ generates universal reversible computation on the Reeb bundles ([q-GoL](#prop:q-game-of-life)).*

**Substrate stability table** (verified numerically by `toffoli-lp-stability.witness.json`):

See [Table 2](#tbl:toffoli-lp-stability-table2-data).
<!-- FILE_END: toffoli-lp-stability.md -->

<!-- FILE_START: q-game-of-life.md -->
**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$ and Planck time $t_P(q) = 1/\hbar_q$. Let $\mathcal{L} \subset M$ be a discrete sublattice of brane points $\{p_i\}$. Each site carries a qubit $|\psi_i\rangle \in \mathcal{S}_{p_i}$ ([state bundle fibre convention](#def:reeb-bundle)). The **$q$-Game of Life** ($q$-GoL) is the discrete-time unitary cellular automaton*

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

*The operator $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is constructed entirely from $q$-deformed Toffoli gates acting on Reeb bundle fibres of neighbour sites \cite{pena2022}. The construction requires five properties:*

1. **Building block.** *The transition operator is the $q$-AND gate:*

$$
  \mathrm{Toff}_q
  \colon  |c_1, c_2, t\rangle
  \longmapsto
  |c_1, c_2,  t \oplus_q (c_1 \wedge_q c_2)\rangle.
$$

 *The symbol $\wedge_q$ denotes the Hecke-algebra q-AND amplitude $\Phi(q) = (q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1) / 2(q+1)^2$ ([q-AND](#rem:toffoli-q-and)). Each $\mathrm{Toff}_q$ executes in three Planck steps.*

2. **Superposition.** *Cell states admit "maybe-alive" superpositions $|\psi_i\rangle = \alpha_i|0\rangle + \beta_i|1\rangle$ via Hadamard rotations $H \in \mathrm{End}(\mathcal{S}_{p_i})$. The set $\{\mathrm{Toff}_q, H\}$ is universal for quantum computation.*

3. **Conway's rules as Toffoli circuits.** *Survival ($k = 2, 3$) and birth ($k = 3$) at site $i$ with neighbourhood $N(i)$ are enacted by the composite operator*

$$
  \mathcal{U}_i^{\mathrm{rule}}
   = 
  \prod_{\{j_1, j_2\} \subset N(i)}
  \mathrm{Toff}_q
  \!\left(
    |\psi_{j_1}\rangle,  |\psi_{j_2}\rangle;  |\psi_i\rangle
  \right).
$$

 *Ancilla qubits encode the neighbour sum. A ripple-carry adder of $O(|N(i)|)$ Toffoli gates on $\lceil \log_2 |N(i)| \rceil$ ancilla strands computes the binary count $k$.*

4. **Reversibility and energy conservation.** *Each $\mathrm{Toff}_q$ is self-inverse:*

$$
  \mathrm{Toff}_q^\dagger  \mathrm{Toff}_q
   = 
  \mathbb{I}.
$$

 *Consequently, $\mathcal{U}_{\mathrm{q\text{-}GoL}}$ is unitary. Classical dissipation is replaced by $q$-energy conservation. The $q$-energy $\mathfrak{E}_q = \langle \Psi | \hat{H}_{\mathrm{q\text{-}GoL}} | \Psi \rangle$ is conserved along the automaton orbit, where $\hat{H}_{\mathrm{q\text{-}GoL}} = i\hbar_q \ln \mathcal{U}_{\mathrm{q\text{-}GoL}}/t_P$ generates the unitary flow.*

5. **Information bandwidth budget.** *One generation advances in $3 |\mathcal{L}|$ Planck steps. The substrate bandwidth $\mathfrak{B}(q) = q \eta_q / (q - 1)^2$ bounds the generation rate:*

$$
  \text{gens / sec}
   \leq 
  \frac{\mathfrak{B}(q)}{3  |\mathcal{L}|}
   = 
  \frac{q \eta_q}{3  (q - 1)^2  |\mathcal{L}|}.
$$

**Stability condition.**
*The evolution is well-defined only when the Toffoli diagonal $P_{7,7}(q)$ and the q-AND amplitude $\Phi(q)$ are strictly positive. This requires the physical regime*

$$
  q  >  1.
$$

*Three operator zeros in $(0, 1]$ bound the sub-physical behaviour: $q_\star = 1/\varphi^2 \approx 0.382$ (golden-ratio zero of $P_{7,7}$), $q_\Phi \approx 0.466$ (cubic root of $\Phi$), and $q = 1$ (classical limit, where $\Phi$ vanishes). The physical substrate value $q_0 \approx 1.110$ lies safely inside the stable regime.*
<!-- FILE_END: q-game-of-life.md -->

<!-- FILE_START: q-game-of-life-interpretation.md -->
**Remark (Relation to Peña et al. and 't Hooft).**
Peña et al. \cite{pena2022} construct a reversible quantum Game of Life using Toffoli-based adder circuits. This paper subsumes their construction. Their Toffoli gate is the classical limit $q \to 1$ of the $q$-Toffoli. Their unitary tick maps to $3$ Planck steps. We identify the $q$-deformed amplitude $\Phi(q)$ as the physical AND amplitude and establish the golden-ratio threshold $q = 1/\varphi^2$ bounding stability.

This construction realises 't Hooft's proposal \cite{thooft2016} that quantum mechanics emerges from a deterministic Planck-scale cellular automaton. The QOU supplies the geometric mechanism. The ontological states are Reeb bundle fibres $\mathcal{S}_p$. The automaton tick is the Planck step $t_P(q)$. The $q$-deformation replaces ad hoc information loss with categorical coarse-graining via the Markov trace.
<!-- FILE_END: q-game-of-life-interpretation.md -->

<!-- FILE_START: substrate-computation.md -->
Discrete time at the Planck scale ([discrete Planck step](#rem:discrete-planck-step)) replaces analysis with combinatorics. The iteration $f_q(z) = z^2 + c(q)$ acts on a finite set. The Toffoli braid $P_{7,6}(q)$ ([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)) is a rational function of the substrate parameter $q$. Its numerator contains the factor $(q - 1)$.

This forces three structural facts:

* The q-AND amplitude is non-zero for all $q \neq 1$.
* The combinatorial skeleton of reversible computation persists at every substrate scale.
* As the universe cools from the Big Bang ($q \to \infty$) to our epoch ($q = q_0$, [local substrate $q$](#prop:local-substrate-q)), the amplitude decreases but never vanishes.

Computers can be built from stones, vacuum tubes, or silicon. The medium does not matter. The combinatorics depends only on the substrate parameter. The Hecke crossing coefficients at $q = q_0$ satisfy the same algebraic relations as at $q = 10^{60}$. The transfer matrices still multiply. The destructive interference isolating the q-AND remains exact. A computation performed with pebbles and one performed with photons inhabit the same Iwahori--Hecke algebra $H_n(q)$ at the same $q$.

**Consistency under :refterm[descent]{#descent}.**
Planck-scale combinatorics must align with local continuous physics. The rationality of $P_{7,6}(q)$ in $q^{1/2}$ guarantees this. The amplitude is a ratio of polynomials with integer coefficients. It remains valid over any field where $q \neq 1$. The polynomial that governs a $3$-strand braid at the Big Bang governs it in the laboratory. The passage from discrete to approximately continuous physics does not break logic gates. It only reduces the amplitude $P_{7,6}$ and stretches the Planck step $t_P(q) = q/(q-1)$.

At $q = q_0$ ([local substrate $q$](#prop:local-substrate-q)):

$$
  P_{7,6}(q_0) = +0.0495, \qquad
  t_P(q_0) \approx 10.11
$$

The gate is slow and quiet, but it operates. This operation is not contingent. It is a direct algebraic consequence of $q \neq 1$.

**Relation to 't Hooft's CA interpretation.**
The thesis that quantum mechanics emerges from a deterministic Planck-scale cellular automaton \cite{thooft2016} aligns structurally with this framework. Both models treat discrete combinatorics at the Planck scale as the ontological primitive. Both view macroscopic quantum superposition as an artifact of coarse-graining. The QOU substrate replaces 't Hooft's information-loss mechanism with algebraic coarse-graining via the Markov trace on $H_n(q)$. This makes the passage from cellular automata to quantum mechanics functorial rather than statistical.
<!-- FILE_END: substrate-computation.md -->

<!-- FILE_START: quantum-computational-universality.md -->
**Conjecture.**
*Let $\beta$ be a braid on $n$ strands with $c = 3N$ crossings,
encoding a reversible computation of $N$ Toffoli gates
([Toffoli transfer matrix](#prop:toffoli-transfer-matrix)).
Let $P_L(q)$ be the Skein polynomial of the braid closure
$\hat{\beta}$, with $\deg P_L \leq c^2 - 1$
([transfer matrix product](#prop:skein-polynomial-transfer-matrix)).*

*Then:*

1. **(Quadratic level.)** *There exists a root of unity
 $q_k = e^{2\pi i/(k+2)}$ with $k \geq 3$ and*

 $k + 2  \leq  c^2 - 1$

 *such that $P_L(q_k) \neq 0$ — the Skein polynomial does
 not degenerate at $q_k$. The level $k$ grows
 **quadratically** in the crossing number: a computation
 with $c$ crossings lives accordingly at level $k \sim c^2$.
 This is the degree of $P_L$: the minimal $k$ for which
 evaluation at $q_k$ retains all information of the
 computation without reduction modulo the cyclotomic
 ideal $(q^{k+2} - 1)$.*

2. **(Quantum universality.)** *At $q_k$ with $k \geq 3$, the
 braiding representation $\rho_{q_k} \colon B_n \to \mathrm{End}(V^{\otimes n})$ is dense in $\mathrm{SU}(2^n)$
 \cite{freedman2003}. Every quantum circuit on $n$ qubits
 with $N$ gates can be approximated to precision $\epsilon$
 by a braid $\beta$ with $c = O(N \cdot \mathrm{polylog}(1/\epsilon))$ crossings.*

3. **(:refterm[Descent]{#descent} projects quantum to classical.)** *The :refterm[descent]{#descent}
 involution $\hat{\tau}$
 ([:refterm[descent]{#descent} involution](#def:descent-involution)) decomposes
 the endomorphism algebra at the root-of-unity level into*

 $$
     \mathrm{End}(V^{\otimes n})
     = 
     \mathcal{A}^{\mathrm{desc}}  \oplus  \mathcal{A}^{\mathrm{trans}}
   $$

 *([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)).
 The descended subalgebra $\mathcal{A}^{\mathrm{desc}} = \mathrm{im}\hat{\tau}$ is the classical shadow — the
 Toffoli computation at real $q$. The transient complement
 $\mathcal{A}^{\mathrm{trans}} = \ker\hat{\tau}$ carries
 the quantum parallelism: exponentially many Skein
 resolution paths that destructively interfere upon
 observation.*

 *The projection $\hat{\tau}$ is observation: it collapses
 the quantum computation at $q_k$ to the classical
 computation at real $q$, with the transient modes erased.*

4. **(Information content.)** *The information content of the
 computation is the crossing number $c$ of the braid
 closure — the minimum jet order at which the computation
 first becomes resolvable
 ([jet–Planck steps](#rem:jet-planck-steps)). The Skein
 polynomial encodes up to $c^2 - 1$ independent
 coefficients (the full quantum state); the factored form
 $P_L(q) = \prod_i \hat{V}_i(q)$ compresses this to
 $O(c)$ factors (the observable output).*

*The flow from real $q$ to the root of unity $q_k$ is the
**lifting** of a classical computation to its quantum
completion
([complex substrate](#rem:complex-substrate-interpretation)):
$q$ leaves the real axis, traverses the complex plane, and
arrives at a point on the unit circle where the full density
of $\mathrm{SU}(2^n)$ becomes available. The :refterm[descent]{#descent}
involution projects back. The round-trip*

$$
  q_{\mathrm{real}}
  \xrightarrow{ \text{lift}}
  q_k = e^{2\pi i/(k+2)}
  \xrightarrow{\hat{\tau}}
  q_{\mathrm{real}}
$$

*is the quantum computation: the lift explores the full
Hilbert space; the :refterm[descent]{#descent} collapses it to the observable.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: quantum-computational-universality.md -->

<!-- FILE_START: skein-turing-machine.md -->
A Turing machine computation of $N$ gates encodes as a braid
$\beta$ on $n$ strands with $c = 3N$ crossings — three per
Toffoli gate
([q-AND](#rem:toffoli-q-and)).  Closing the braid gives a
link $L = \hat{\beta}$ whose Skein polynomial $P_L(q)$ is
the **output** of the computation
([transfer matrix product](#prop:skein-polynomial-transfer-matrix)).

**The Skein decomposition is the discrete path integral.**

At each crossing of $L$, the Skein relation resolves the
link into three branches:

$$
  q  L_+ -  q^{-1} L_- =  s  L_0
$$

where $s = q^{1/2} - q^{-1/2}$.  Each resolution replaces
one crossing with one of three outcomes: positive ($L_+$),
negative ($L_-$), or smoothed ($L_0$).  Iterating over all
$c$ crossings produces a **resolution tree** with $3^c$
leaves — one per discrete history of the computation.

This is the **path integral at Planck resolution**:

| Path integral                | Skein decomposition                                             |
| ---------------------------- | --------------------------------------------------------------- |
| History                      | Resolution path through the tree                                |
| Action weight $e^{iS/\hbar}$ | Skein weight $q^{\pm 1}$ or $s$ per crossing                    |
| Partition function $Z$       | Skein polynomial $P_L(q) = \sum_{\text{paths}}(\text{weights})$ |
| Path integral measure        | Markov trace $\mathrm{tr}_M$                                    |
| Planck time step             | One crossing resolution                                         |

Each resolution is one Planck step
([discrete Planck step](#rem:discrete-planck-step)).  Each
path through the tree is one discrete history of the
universe at the resolution of one crossing.  The Skein
polynomial is the sum over all $3^c$ histories, weighted by
their crossing signs — the partition function of the
computation.

**Information before and after the trace.**

Before the Markov trace, the braid word $\beta \in H_n(q)$
retains the full fine structure: which generators, in which
order, with which crossing types.  This is $O(N \log n)$
bits — the gate addresses of the computation.

After the trace, the Skein polynomial $P_L(q)$ has degree
$\leq c^2 - 1$ but is computed in factored form:

$$
  P_L(q) = \prod_{i=0}^{n-2} \hat{V}_i(q)
$$

This compression from $3^c$ paths to $O(c)$ factors is the
**selective erasure** of internal wiring: which resolution
path was taken — which history the universe followed — is
lost.  What survives is the topological invariant: the
computation's output.

The Markov trace is observation.  It collapses $3^c$ quantum
paths to one polynomial.

**The backward flow.**

Start from a section $E \in \Gamma(M, \mathcal{S})$ — the
output state of the computation.  Resolve each crossing via
the Skein relation, one gate at a time, flowing backward
through the jet tower
([jet–Planck steps](#rem:jet-planck-steps)):

* After $1$ resolution: the last gate is undone.
* After $3N$ resolutions: complete unwinding —
  arrival at the Big Bang initial conditions
  $\mathcal{S}_0 = \sum_i (p_i, H_i)$
  ([bundle initial conditions](#def:bundle-initial-conditions)).

By :refterm[descent]{#descent}
([:refterm[descent]{#descent} involution](#def:descent-involution)), all
branches of the resolution tree flow back to
$\mathcal{S}_0$.  The initial conditions **are** the
program.  The braid **is** the computation.  The Skein
polynomial **is** the output.

**Quantum computations.**

A section $E$ that factors through a finite braid word is
**computable**: it is reachable from $\mathcal{S}_0$ by a
finite number of Toffoli gates, each executing in $3$ Planck
steps.  The set of all such $E$ is the computable fragment
of the QOU — the sections that can be written as finite
products of transfer matrices.

Sections that do not factor through any finite braid require
infinite crossing number — infinite jet order — and are
**never resolvable**.  They are the non-computable bundles:
states of the universe that no finite sequence of logic
gates, however long, can produce from the Big Bang.

The distinction between computable and non-computable $E$ is
not a choice — it is a topological property of the section,
determined by whether its Skein polynomial has finite degree.
<!-- FILE_END: skein-turing-machine.md -->

<!-- FILE_START: reeb-turing-completeness.md -->
The QOU asserts that universal computation is native to the substrate. This claim, articulated by [`conj:quantum-computational-universality`](#conj:quantum-computational-universality) and the [Skein–Turing correspondence](#rem:skein-turing-machine), admits a sharp geometric analogue. Cardona, Miranda, Peralta-Salas, and Presas \cite{cardona2021} prove a corresponding result for steady Euler flows.

**The classical result.**
Let $(M^3, g)$ be a closed Riemannian 3-manifold. Let $X$ be a divergence-free vector field on $M$ satisfying the steady Euler equation

$$
  \nabla_X X = -\nabla p, \qquad \mathrm{div}_g(X) = 0.
$$

By a theorem of Sullivan–Etnyre–Ghrist, a conformal change of metric $g \mapsto \tilde g$ maps any non-vanishing steady Euler field to the Reeb vector field $R_\alpha$ of a contact form $\alpha$ on $M$, up to rescaling. Cardona–Miranda–Peralta-Salas–Presas show that this Reeb field can be chosen to be strongly Turing complete. They construct a Reeb field whose first-return map on a Poincaré section simulates an arbitrary Turing machine. Consequently, determining whether a trajectory reaches a given open set is strictly undecidable.

**Translation to the QOU.**
The QOU's [categorical Reeb derivation](#def:categorical-reeb-derivation) $\xi_q \colon A \to A$ generates a flow on the state bundle $\mathcal{S}$. Its horizontal projection precisely yields the Reeb vector field of the contact form $\varTheta$ ([Cartan magic formula relation](#def:categorical-reeb-derivation)). This is exactly the dynamical object that achieves universal computation in the classical setting. Three structural identifications follow.

First, Reeb flow acts as the internal clock. The [discrete Planck step](#rem:discrete-planck-step) and the [Reeb iterations per Planck](#prop:reeb-operations-per-planck) cast the Reeb derivation as the universe's clock. Cardona et al. show this identical dynamical object can encode any computable function. The clock that drives the universe is simultaneously a universal computer.

Second, the first-return map serves as a Toffoli action. The classical construction places a Turing machine's tape on a horizontal disk in $M$, using the Reeb first-return map to update the head's state. In the QOU, the analogue is the [Toffoli transfer matrix](#prop:toffoli-transfer-matrix) acting on the [observable MTC](#def:observable-mtc). The horizontal distribution $\ker(\varTheta)$ carries the tape, and one Reeb period implements exactly one Toffoli gate.

Third, undecidability guarantees an observational horizon. The undecidable trajectory problem of \cite{cardona2021} (extended to stationary Beltrami fields in \cite{cardona2023}) represents the geometric face of the [computational horizon](#def:computational-horizon). No finite observer can predict whether a given Reeb orbit reaches a given open set. Correspondingly, no finite QOU observer can resolve every section of $\mathcal{S}$.

**Consequences for the QOU.**
The categorical Reeb derivation is occasionally dismissed as an axiomatised formalism rather than a geometric flow. The Cardona–Miranda–Peralta-Salas–Presas construction collapses this gap. The Reeb-on-contact structure posited algebraically by the QOU is classically proven to support Turing-complete dynamics in dimension three. Universal computation is not a late emergent property of the quantum substrate; it is native to every contact 3-manifold possessing a sufficiently rich periodic-orbit structure. The QOU inherits this property by construction.

Tao's programme on hydrodynamic universality \cite{tao2019} parallels this result. Any sufficiently expressive ODE system embeds in steady Euler flow on some manifold. The QOU's Reeb derivation constitutes one such embedding. The [Skein–Turing machine](#rem:skein-turing-machine), encoding a Turing machine as a braid whose Skein polynomial yields the output, is simply the discrete Hecke-algebra shadow of this geometric construction.

**Location of the conjectural part.**
Cardona–Miranda–Peralta-Salas–Presas establish universality at one fixed metric. The QOU extends this claim: universality survives the [q-deformation](#def:quantum-observable-universe) of the ambient differential geometry. We conjecture that the continuous family of substrate parameters $q \in (1, \infty)$ supports a continuous family of universal Reeb flows, where discrete roots-of-unity specialisations recover the [FKLW universal quantum computer](#conj:quantum-computational-universality). Thus, [`conj:quantum-computational-universality`](#conj:quantum-computational-universality) remains conjectural, while the classical $q = 1$ limit stands as a theorem.
<!-- FILE_END: reeb-turing-completeness.md -->

