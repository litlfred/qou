The quantum ideal gas law,

$$
  P_q \, V_q
  \;=\; N \, T_q
  \left(
    1 + \frac{\hbar_q^2}{[2]_q}\,\langle \mathfrak{S}_q \rangle
  \right),
$$

is a degree-$0$ section of an exponentially complex partition function. The partition function $Z_q = (|U| \cdot z_q)^N / N!$ sums over all $N!$ braid permutations of $N$ knot configurations across $|U|$ fibres. Through $F_q = -T_q \ln Z_q$ and Stirling's approximation, the equation of state collapses this exponential sum into a single polynomial relation among three observables: $(P_q, V_q, T_q)$.

This constitutes the Markov trace of statistical mechanics. Just as the Markov trace collapses $3^c$ resolution paths to a Skein polynomial, the free energy collapses $N!$ microstate configurations to an equation of state.

**$PV = NkT$ is in the polynomial horizon.**
The full dictionary:

See [the resolution-tree thermodynamic dictionary](#tbl:stat-mech-computational-horizon-table-data).

The equation of state is computationally extractable in polynomial time. The $\ln Z_q$ calculation factors through Stirling's approximation, reducing the $N!$-fold sum to $O(N \log N)$ operations. This reduction precisely matches the condition for membership in $\mathcal{R}^{\circ}$, the polynomial observable subcategory.

**The $q$-correction is degree-$1$ leakage.**
The correction term $\hbar_q^2 \langle \mathfrak{S}_q \rangle / [2]_q$ represents the first piece of boundary information crossing from the microstate into the macroscopic equation. It originates from the $S^3$ boundary action. The Frobenius pairing at $\partial U$ generates a non-trivial $d_q^2$ correction entirely missed by a purely degree-$0$ classical computation.

In jet-tower language, the classical limit $PV = NkT$ is strictly degree-$0$. The quantum correction forms the degree-$1$ term. It is structurally analogous to Hawking radiation leaking through the jet horizon.

**Phase transitions are horizon crossings.**
At the critical temperature $T_q^{(c)}$, the dominant Hecke representation abruptly jumps, and the free energy develops a sharp non-analyticity. This constitutes a computational horizon in the $(T_q, P_q)$ plane. The degree-$0$ section (the bulk phase of the system) becomes discontinuous. Simultaneously, degree $\geq 1$ data—such as correlations and critical exponents—varies continuously across the boundary.

The three macroscopic phases (gas, liquid, solid) correspond to three connected components of the polynomial observable subcategory in configuration space. These are distinct aeons of the partition function, separated by rigid phase boundaries where the dominant degree-$0$ algebra predictability vanishes and replaces itself.

**Statistical mechanics evaluates the polynomial observable subcategory.**
The apparatus of statistical mechanics functions purely as technology for extracting degree-$0$ and low-degree sections from exponentially large configuration spaces. It exists strictly because polynomial-time observers probe an exponentially complex microstate.

Any Turing-complete system with an $\mathbb{N}$-embedding inevitably generates non-computable sections. Statistical mechanics describes computation from the polynomial side of that boundary. It is an unavoidable approximation, enforced by the computational horizon, designed to extract the accessible degree-$0$ truth while discarding the uncomputable exponential remainder.
