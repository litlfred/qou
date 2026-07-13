<!-- FILE_START: planck-scale-computation-intro.md -->
Computation at the Planck scale operates via substrate-level transitions. The Toffoli transfer matrix realizes the $q$-deformed AND gate. Linear-program stability analysis determines the operational regime of this gate.

This substrate-level construction lifts to a $q$-deformed Game of Life, supplying a model for quantum-computational universality. The categorical embodiment of this dynamic is the skein Turing machine. It realizes Church–Turing equivalence at the substrate level, establishing the physical falsifiability of the information-theoretic framework.
<!-- FILE_END: planck-scale-computation-intro.md -->

<!-- FILE_START: planck-scale-computation.md -->
Every Planck-time step corresponds to the application of a single transfer matrix on the brane fibre. The product of matrices along the braid word determines the computational cost. The entropy per step equals the operational entropy $\eta_q$ of the substrate. 

We realize universal classical computation through a Toffoli transfer matrix on $\Sigma_3$, yielding an explicit $q$-AND amplitude that vanishes in the classical limit. The binding of this gate remains robust under noise via linear-program stability. Evaluated as a discrete dynamical system, this constitutes a $q$-deformed Game of Life. Because the combinatorics is medium-independent, every Turing machine of $N$ gates encodes identically as a braid with $c = 3N$ crossings. Each Planck step applies exactly one such matrix, with the bandwidth $\mathfrak{B}(q)$ bounding the information-theoretic cost.
<!-- FILE_END: planck-scale-computation.md -->

<!-- FILE_START: toffoli-transfer-matrix.md -->
Let $P_{\mathrm{flip}}(q; k_1, k_2)$ be the target-flip amplitude on a $3$-strand nuclear braid with control types $(k_1, k_2) \in \{0,1\}^2$ and target strand $3$, constructed from the Hecke crossing coefficients. Then:

1. **(Universal factorization.)** Every target-flip amplitude factors as
$$
  P_{\mathrm{flip}}(q; k_1, k_2) = c_{k_1 k_2}(q) \cdot \Phi(q)
$$
where $c_{k_1 k_2}$ is the crossing coefficient of the control–control pair (the non-flipping strands) and $\Phi(q)$ is the **universal core amplitude** independent of the control types:
$$
  \Phi(q) = \frac{(q - 1)(q^{3/2} + q^{1/2} - 1)(q^{3/2} + q + 1)}{2(q + 1)^2}
$$

| Control pair | $c_{k_1 k_2}$ | $d_{k_1 k_2}$ |
|:------------:|:--------------:|:--------------:|
| $\mathfrak{p}\mathfrak{p}$ | $1$ | $0$ |
| mixed | $1$ | $-\frac{q - q^{-1}}{2}$ |
| $\mathfrak{n}\mathfrak{n}$ | $1$ | $-(q - q^{-1})$ |

2. **(Target-flip blindness of the control crossing.)** The generator $\sigma_1$ constitutes the single control–control crossing. Its traced volume $\hat{V}_1 = z(q)\,c + d$ is type-dependent. A target-flip leaves the control crossing unchanged. Consequently, $\Delta_1 = 0$ for every target-flip transition. The entire target-flip amplitude concentrates at generator $\sigma_0$.

3. **(The q-AND.)** The Toffoli gate selects the target strand whose control–control pair has $c = 1$ ($\mathfrak{p}\mathfrak{p}$ crossing). In the exceptional divisor, this choice provides the governor basis with unit prefactor:
$$
  P_{7,6}(q) = 1 \cdot \Phi(q) = \frac{(q-1)(q^{3/2}+q^{1/2}-1)(q^{3/2}+q+1)}{2(q+1)^2}
$$

4. **(Antisymmetry.)** $P_{6,7}(q) = -P_{7,6}(q)$.

5. **(Classical limit.)** All target-flip amplitudes vanish as $q \to 1$ because the core $\Phi(q)$ contains the factor $(q - 1)$.

6. **(Toffoli diagonal.)** The diagonal entry is
$$
  P_{7,7}(q) = \frac{q + q^{1/2} - 1}{q + 1}
$$
This all-proton amplitude vanishes exactly at the golden ratio threshold $q = 1/\varphi^2$.
<!-- FILE_END: toffoli-transfer-matrix.md -->

<!-- FILE_START: toffoli-transfer-matrix-interpretation.md -->
**Explicit values at the local substrate parameter $q = q_0$:**

| Controls | $c_{k_1 k_2}$ | $P_{\mathrm{flip}}$ | Ratio |
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
The polynomial $P_{7,6}(q)$ defines the **q-AND**: the $q$-deformed AND gate realized by braiding. In the classical Toffoli gate (CCNOT), the target bit flips if and only if both control bits are $1$. The $3$-strand nuclear braid replaces this Boolean AND with a topological amplitude. Two control particles must braid around the target to flip its phase. All other phase-flip pathways destructively interfere to zero.

**Three Planck steps.**
The $3$-strand Toffoli braid contains $\binom{3}{2} = 3$ crossings. A single crossing is not a complete topological operation; one must close the full braid loop. The complete Toffoli gate therefore executes in exactly **$3$ Planck steps**, allocating one step per crossing.

| Epoch | $q$ | $t_P(q)$ | Toffoli ($3$ steps) | $P_{7,6}$ |
|-------|:---:|:---------:|:-------------------:|:---------:|
| Big Bang | $\to \infty$ | $\to 1$ | $3$ units | $\to \infty$ |
| Physical | $q_0$ | $10.11$ | $30.3$ units | $+0.050$ |
| Classical | $\to 1$ | $\to \infty$ | $\infty$ | $0$ |

At the Big Bang, each Planck step equals one unit of time. The Toffoli gate executes in the shortest possible time. Near the classical limit, the Planck step diverges and the gate freezes. Braiding ceases to operate, and the q-AND amplitude vanishes as $(q - 1) \to 0$.

**Factor anatomy.**
The three factors of $P_{7,6}(q)$ dictate its physical consequences. The factor $(q - 1)$ measures the departure from classicality; the q-AND magnitude is proportional to the quantum deformation. The factor $(q^{3/2} + q^{1/2} - 1)$ is a cubic in $q^{1/2}$ with a real zero at $q \approx 0.466$. Below this threshold, the q-AND changes sign, imparting a phase reversal to the target. Finally, the factor $(q^{3/2} + q + 1)$ remains strictly positive for all $q > 0$, providing a non-zero baseline amplitude.

**Antisymmetry.**
The identity $P_{6,7}(q) = -P_{7,6}(q)$ ensures the forward and reverse Toffoli transitions possess equal magnitude but opposite sign. Creating a proton from a neutron and annihilating one are related by a sign. This matches the asymmetry of the beta decay matrix $\Delta_\beta$.

**Universality.**
The Toffoli gate is universal for reversible classical computation. Any irreversible Turing machine can be simulated by a reversible one, relying entirely on Toffoli gates, with at most polynomial overhead in time and space. When combined with a single-qubit gate outside the Clifford group, the Toffoli gate achieves quantum computational universality. The existence of a non-zero $P_{7,6}(q)$ in the Iwahori--Hecke algebra guarantees that the substrate's braiding dynamics, operating in discrete Planck steps, is computationally universal.
<!-- FILE_END: toffoli-q-and.md -->

<!-- FILE_START: toffoli-lp-stability.md -->
Let $T_q \in H_3(q)$ be the $q$-Toffoli element, realized as the $3$-strand braid word with traced volume matrix $M(q)$. Let $G = (\mathrm{tr}_M(b_i \cdot b_j))_{i,j}$ be the Gram matrix of the normal-form basis. Express the $q$-Toffoli in normal-form coordinates as $T_q = \sum_{i=1}^{6} t_i(q) \, b_i$. Then:

1. **(Stability region.)** The $q$-Toffoli element is LP-stable on the physical regime $q > 1$. All Hecke amplitudes carry the correct sign, rendering the confinement LP feasible. Three operator zeros in $(0, \infty)$ delimit sub-physical behavior:
$$
  q_\star \,=\, 1/\varphi^2 \,=\, (3 - \sqrt{5})/2 \,\approx\, 0.3820,
  \qquad
  q_\Phi \,\approx\, 0.4656,
  \qquad
  q \,=\, 1,
$$
where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio.

2. **(Three operator thresholds.)** Each zero corresponds to a vanishing Hecke amplitude:
See [Table 1](#tbl:toffoli-lp-stability-table1-data).
At $q_\star$, the diagonal amplitude $P_{7,7}$ vanishes. At $q_\Phi$, the q-AND amplitude $\Phi$ reverses sign. At $q = 1$, the q-AND vanishes. The classical reversible Toffoli has trivial amplitude here.

3. **(Dual shadow prices.)** For $q > 1$, the LP dual admits bounded shadow prices $y_i^*(q)$ satisfying:
$$
  |y_i^*(q)| \leq \kappa(\mathrm{G}(q)) \cdot \|t(q)\|,
$$
where $\kappa(\mathrm{G}(q)) = \lambda_{\max}(G)/|\lambda_{\min}(G)|$ is the Gram condition number. At the physical substrate value $q_0 \approx 1.110$, $\kappa(G(q_0)) \approx 3.03$. All shadow prices remain bounded in Skein units.

4. **(Physical-substrate stability.)** At $q_0 \approx 1.110$:
$$
  P_{7,7}(q_0) \,\approx\, 0.5514,
  \qquad
  \Phi(q_0) \,\approx\, 0.0495.
$$
Both are strictly positive. The $q$-Toffoli is LP-stable at the physical substrate value. The set $\{q\text{-Toffoli}, H\}$ generates universal reversible computation on the Reeb bundles.

**Substrate stability table:**
See [Table 2](#tbl:toffoli-lp-stability-table2-data).
<!-- FILE_END: toffoli-lp-stability.md -->

<!-- FILE_START: q-game-of-life.md -->
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

4. **Reversibility and energy conservation.** Each $\mathrm{Toff}_q$ is self-inverse:
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
<!-- FILE_END: q-game-of-life.md -->

<!-- FILE_START: q-game-of-life-interpretation.md -->
**Remark (Relation to Peña et al. and 't Hooft).**
Peña et al. construct a reversible quantum Game of Life using Toffoli-based adder circuits. This paper subsumes their construction. Their Toffoli gate is the classical limit $q \to 1$ of the $q$-Toffoli. Their unitary tick maps to $3$ Planck steps. We identify the $q$-deformed amplitude $\Phi(q)$ as the physical AND amplitude and establish the golden-ratio threshold $q = 1/\varphi^2$ bounding stability.

This construction realizes 't Hooft's proposal that quantum mechanics emerges from a deterministic Planck-scale cellular automaton. The QOU supplies the geometric mechanism. The ontological states are Reeb bundle fibres $\mathcal{S}_p$. The automaton tick is the Planck step $t_P(q)$. The $q$-deformation replaces ad hoc information loss with categorical coarse-graining via the Markov trace.
<!-- FILE_END: q-game-of-life-interpretation.md -->

<!-- FILE_START: substrate-computation.md -->
Discrete time at the Planck scale replaces analysis with combinatorics. The Toffoli braid $P_{7,6}(q)$ forms a rational function of the substrate parameter $q$, carrying the numerator factor $(q - 1)$. 

This imposes three structural facts:
1. The q-AND amplitude is non-zero for all $q \neq 1$.
2. The combinatorial skeleton of reversible computation persists at every substrate scale.
3. As the universe cools from the Big Bang ($q \to \infty$) to the local epoch ($q = q_0$), the amplitude decreases but never vanishes.

The medium of computation does not alter its logic. The combinatorics depends only on the substrate parameter. The Hecke crossing coefficients at $q = q_0$ satisfy the exact algebraic relations as at $q = 10^{60}$. The transfer matrices still multiply. The destructive interference isolating the q-AND remains exact. Computations executed by pebbles or photons inhabit the same Iwahori--Hecke algebra $H_n(q)$ at identical $q$.

**Consistency under descent.**
Planck-scale combinatorics aligns tightly with local continuous physics. The rationality of $P_{7,6}(q)$ in $q^{1/2}$ guarantees this. The amplitude remains valid over any field where $q \neq 1$. The polynomial governing a $3$-strand braid at the Big Bang also governs it in the laboratory. The passage from discrete to continuous physics does not break logic gates; it merely attenuates the amplitude $P_{7,6}$ and dilates the Planck step $t_P(q) = q/(q-1)$.

At $q = q_0$, we have $P_{7,6}(q_0) = +0.0495$ and $t_P(q_0) \approx 10.11$. The gate operates slowly and quietly, but its operation is a direct algebraic consequence of $q \neq 1$.

**Relation to 't Hooft's CA interpretation.**
The thesis that quantum mechanics emerges from a deterministic Planck-scale cellular automaton aligns structurally with this framework. Both models posit discrete combinatorics at the Planck scale as the ontological primitive. Both attribute macroscopic quantum superposition to coarse-graining. The QOU substrate formally substitutes 't Hooft's information loss with algebraic coarse-graining via the Markov trace on $H_n(q)$, rendering the emergence of quantum mechanics functorial rather than statistical.
<!-- FILE_END: substrate-computation.md -->

<!-- FILE_START: quantum-computational-universality.md -->
**Conjecture.** Let $\beta$ be a braid on $n$ strands with $c = 3N$ crossings, encoding a reversible computation of $N$ Toffoli gates. Let $P_L(q)$ be the Skein polynomial of the braid closure $\hat{\beta}$, with $\deg P_L \leq c^2 - 1$. Then:

1. **(Quadratic level.)** There exists a root of unity $q_k = e^{2\pi i/(k+2)}$ with $k \geq 3$ and $k + 2 \leq c^2 - 1$ such that $P_L(q_k) \neq 0$. The minimal level $k$ grows quadratically with the crossing number: $k \sim c^2$. Evaluation at $q_k$ preserves all information of the computation without reduction modulo the cyclotomic ideal.
2. **(Quantum universality.)** At $q_k$ with $k \geq 3$, the braiding representation $\rho_{q_k} \colon B_n \to \mathrm{End}(V^{\otimes n})$ is dense in $\mathrm{SU}(2^n)$. Every quantum circuit on $n$ qubits with $N$ gates can be approximated to precision $\epsilon$ by a braid $\beta$ with $c = O(N \cdot \mathrm{polylog}(1/\epsilon))$ crossings.
3. **(Descent projects quantum to classical.)** The descent involution $\hat{\tau}$ decomposes the endomorphism algebra at the root-of-unity level into
$$
  \mathrm{End}(V^{\otimes n}) = \mathcal{A}^{\mathrm{desc}} \oplus \mathcal{A}^{\mathrm{trans}}.
$$
The descended subalgebra $\mathcal{A}^{\mathrm{desc}}$ constitutes the classical shadow: the Toffoli computation at real $q$. The transient complement $\mathcal{A}^{\mathrm{trans}}$ carries the quantum parallelism: exponentially many Skein resolution paths that destructively interfere upon observation. The projection $\hat{\tau}$ represents observation. It collapses the quantum computation to the classical computation at real $q$.
4. **(Information content.)** The information content of the computation is the crossing number $c$. The Skein polynomial encodes up to $c^2 - 1$ independent coefficients representing the full quantum state. The factored form $P_L(q) = \prod_i \hat{V}_i(q)$ compresses this to $O(c)$ observable factors.

The flow from real $q$ to the root of unity $q_k$ signifies the lifting of a classical computation to its quantum completion. The parameter $q$ leaves the real axis, transverses the complex plane, and arrives on the unit circle where $\mathrm{SU}(2^n)$ density applies. The descent involution projects back. The round-trip
$$
  q_{\mathrm{real}} \xrightarrow{\text{lift}} q_k = e^{2\pi i/(k+2)} \xrightarrow{\hat{\tau}} q_{\mathrm{real}}
$$
forms the quantum computation. The lift explores the Hilbert space; the descent collapses it to the observable.

**Archimedean specialisation (§7c).**
This block sits on the archimedean side of the substrate wall. It invokes real-analytic structures and numerical evaluation at the physical parameter $q_0$. Categorical identities drawn here remain valid over an abstract coefficient ring, but their archimedean realization is strictly specialized.
<!-- FILE_END: quantum-computational-universality.md -->

<!-- FILE_START: skein-turing-machine.md -->
A Turing machine computation of $N$ gates encodes as a braid $\beta$ on $n$ strands with $c = 3N$ crossings. Closing the braid yields a link $L = \hat{\beta}$. The Skein polynomial $P_L(q)$ forms the output of the computation.

**The Skein decomposition is the discrete path integral.**
At each crossing of $L$, the Skein relation resolves the link into three branches:
$$
  q L_+ - q^{-1} L_- = s L_0
$$
where $s = q^{1/2} - q^{-1/2}$. Each resolution replaces one crossing with a positive ($L_+$), negative ($L_-$), or smoothed ($L_0$) outcome. Iterating over all $c$ crossings constructs a resolution tree with $3^c$ leaves, each representing one discrete history. 

This constitutes the path integral at Planck resolution. Each resolution is exactly one Planck step. Each tree path is one discrete history. The Skein polynomial sums over all $3^c$ histories, weighted by their crossing signs, yielding the partition function of the computation.

| Path integral | Skein decomposition |
| ------------- | ------------------- |
| History | Resolution path through the tree |
| Action weight $e^{iS/\hbar}$ | Skein weight $q^{\pm 1}$ or $s$ per crossing |
| Partition function $Z$ | Skein polynomial $P_L(q) = \sum_{\text{paths}}(\text{weights})$ |
| Path integral measure | Markov trace $\mathrm{tr}_M$ |
| Planck time step | One crossing resolution |

**Information before and after the trace.**
Before the Markov trace, the braid word $\beta \in H_n(q)$ retains the full gate address fine structure: $O(N \log n)$ bits of exact generator wiring.

After the trace, the Skein polynomial $P_L(q)$ compresses from $3^c$ paths to $O(c)$ factors via $P_L(q) = \prod_{i=0}^{n-2} \hat{V}_i(q)$. This is the selective erasure of internal wiring. The discrete history the universe followed is irreversibly lost. What survives is the topological invariant: the computation's output. The Markov trace acts as observation, collapsing $3^c$ quantum paths into one polynomial.

**The backward flow.**
Starting from the output state $E \in \Gamma(M, \mathcal{S})$, we resolve each crossing backward through the jet tower. After $3N$ resolutions, we unwind completely to the Big Bang initial conditions $\mathcal{S}_0$. By descent, all branches flow back to $\mathcal{S}_0$. The initial conditions are the program; the braid is the computation; the Skein polynomial is the output.

**Quantum computations.**
A section $E$ that factors through a finite braid word is computable: it is reachable from $\mathcal{S}_0$ by a finite sequence of Toffoli gates. These sections form the computable fragment of the QOU. Sections requiring infinite crossing number are non-computable. They correspond to states of the universe unattainable from the Big Bang by any finite logic sequence. This distinction represents a topological property encoded by the finite degree of the Skein polynomial.
<!-- FILE_END: skein-turing-machine.md -->

<!-- FILE_START: reeb-turing-completeness.md -->
The QOU asserts that universal computation is native to the substrate. Cardona, Miranda, Peralta-Salas, and Presas prove a corresponding classical result for steady Euler flows on closed Riemannian 3-manifolds.

**The classical result.**
A conformal change of metric maps any non-vanishing steady Euler field to the Reeb vector field $R_\alpha$ of a contact form. Cardona et al. construct a Reeb field whose first-return map simulates an arbitrary Turing machine, rendering its long-term trajectory problem strictly undecidable.

**Translation to the QOU.**
The categorical Reeb derivation $\xi_q$ generates a flow whose horizontal projection yields exactly this contact Reeb vector field. This flow guarantees universal computation via three structural identifications. 

First, Reeb flow acts as the internal clock. The clock driving the universe is simultaneously a universal computer.
Second, the first-return map functions as a Toffoli action. The horizontal distribution carries the computational tape, and one Reeb period implements exactly one Toffoli gate.
Third, undecidability establishes an observational horizon. No finite QOU observer can predict arbitrary orbits or resolve every section of $\mathcal{S}$.

**Consequences for the QOU.**
The Reeb derivation is a rigorous geometric flow. Universal computation is native to every contact 3-manifold possessing sufficient periodic-orbit structure. The QOU inherits this inherently. Tao's hydrodynamic universality program mirrors this conclusion.

**Location of the conjectural part.**
The Cardona et al. result establishes universality at a fixed classical metric. The QOU extends this geometrically: universality survives the $q$-deformation of the ambient space. We conjecture that the continuous parameter family $q \in (1, \infty)$ supports a continuous family of universal Reeb flows, with discrete roots-of-unity specializations recovering the universal quantum computer. Thus, while the $q=1$ limit stands as a classical theorem, its $q$-deformed lift to arbitrary substrate parameters remains conjectural.
<!-- FILE_END: reeb-turing-completeness.md -->

