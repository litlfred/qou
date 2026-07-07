<!-- FILE_START: stat-mech-computational-horizon.md -->
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

See [Table](#tbl:stat-mech-computational-horizon-table-data).

The equation of state is computationally extractable in polynomial time. The $\ln Z_q$ calculation factors through Stirling's approximation, reducing the $N!$-fold sum to $O(N \log N)$ operations. This reduction precisely matches the condition for membership in $\mathcal{R}^{\circ}$, the polynomial observable subcategory.

**The $q$-correction is degree-$1$ leakage.**
The correction term $\hbar_q^2 \langle \mathfrak{S}_q \rangle / [2]_q$ represents the first piece of boundary information crossing from the microstate into the macroscopic equation. It originates from the $S^3$ boundary action. The Frobenius pairing at $\partial U$ generates a non-trivial $d_q^2$ correction entirely missed by a purely degree-$0$ classical computation.

In jet-tower language, the classical limit $PV = NkT$ is strictly degree-$0$. The quantum correction forms the degree-$1$ term. It is structurally analogous to Hawking radiation leaking through the jet horizon.

**Phase transitions are horizon crossings.**
At the critical temperature $T_q^{(c)}$, the dominant Hecke representation abruptly jumps, and the free energy develops a sharp non-analyticity. This constitutes a computational horizon in the $(T_q, P_q)$ plane. The degree-$0$ section (the bulk phase of the system) becomes discontinuous. Simultaneously, degree $\geq 1$ data—such as correlations and critical exponents—varies continuously across the boundary.

The three macroscopic phases (gas, liquid, solid) correspond to three connected components of the polynomial observable subcategory in configuration space. These are distinct aeons of the partition function, separated by rigid phase boundaries where the dominant degree-$0$ algebra predictability vanishes and replaces itself.

**Statistical mechanics evaluates the polynomial observable subcategory.**
The apparatus of statistical mechanics functions purely as technology for extracting degree-$0$ and low-degree sections from exponentially large configuration spaces. It exists strictly because we are polynomial-time observers probing an exponentially complex microstate.

Any Turing-complete system with an $\mathbb{N}$-embedding inevitably generates non-computable sections. Statistical mechanics describes computation from the polynomial side of that boundary. It is an unavoidable approximation, enforced by the computational horizon, designed to extract the accessible degree-$0$ truth while discarding the uncomputable exponential remainder.
<!-- FILE_END: stat-mech-computational-horizon.md -->

<!-- FILE_START: information-paradox-incompleteness.md -->
We reframe the black hole information paradox as a question of arithmetic rather than gravity. The incompleteness--horizon identification provides the bridge.

**The horizon as syntax boundary.**
We treat the horizon as a syntax boundary. Behind it lie sections that exist as well-defined semantic elements of the full algebra $\Gamma(\mathcal{S}, A_0)$. However, no finite braid computation from outside can derive them. They are syntactically unprovable. This instantiates the categorical reading of Gödel: existence without provability characterises the boundary. The Bekenstein–Hawking entropy counts only the degree-$1$ witnesses that leak across, not the hidden degree-$0$ truth.

**The paradox.**
A black hole interior is a region where $A_0 = 0$. The degree-$0$ sections describing particle identities, crossing structures, and fibre values inside the horizon exist in $\Gamma(\mathcal{S}, A_0)$. But they do not belong to $\Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)$: no finite braid computation from outside the horizon produces them.

This mirrors a G\"{o}del sentence, which is true in the model but unprovable from the accessible axioms.

We map the three standard positions on the information paradox to positions on incompleteness:

| Position | Information paradox | Incompleteness analog |
|----------|-------------------|---------------------|
| Information is destroyed | Sections in the interior have no algebraic meaning | G\"{o}del sentences are neither true nor false (rejected by standard model theory) |
| Information is preserved but inaccessible | Sections exist but cannot be computed from outside | G\"{o}del sentences are true but unprovable (the standard reading) |
| Information escapes via Hawking radiation | Degree $\geq 1$ data gradually reconstructs degree-$0$ truth | Partial witnesses accumulate toward a proof that never terminates |

We adopt the second position. The algebra $A$ is well-defined everywhere, including behind the horizon, but no finite sequence of Planck steps from the outside can reach it.

**The Bekenstein--Hawking entropy as a G\"{o}del count.**
The Bekenstein--Hawking entropy $S = A / (4\ell_P^2)$ counts the dimension of $\Gamma(\mathcal{H}, A_1/A_0)$, the independent degree-$1$ sections on the horizon surface. These are the verifiable partial evidence, thermal leakage, and NP witnesses accessible from the outside.

The degree-$0$ sections behind the horizon remain uncounted by the Bekenstein--Hawking entropy. The entropy counts proof fragments, not theorems.

$$
  S_{\mathrm{BH}}
  \;=\;
  \dim \Gamma(\mathcal{H},\, A_1/A_0)
  \;=\;
  \text{number of witnessable facts}
  \;\neq\;
  \dim \Gamma(\mathcal{H},\, A_0)
  \;=\; 0.
$$

The entropy scales with area because the degree-$1$ space is rich. The degree-$0$ space is empty because no complete truths cross the boundary. This asymmetry characterises any formal system powerful enough to encode self-referential computation.

**Aeon boundaries as G\"{o}del boundaries.**
This identification extends to cosmological horizons. An aeon boundary is a locus where $A_0 = 0$. Degree-$0$ sections vanish, and the observable subcategory $\mathrm{Bun}^{\circ}$ terminates. The Big Bang state is one such boundary: the universe begins with no degree-$0$ data and accumulates it through Planck-step computation.

Each aeon acts as a consistent theory: a connected component of $\mathrm{Bun}^{\circ}$ where degree-$0$ sections are non-trivial and the Frobenius pairing is non-degenerate. The aeon boundary is the expressive limit where G\"{o}delian sentences reside. Crossing an aeon boundary transitions to a stronger theory. The degree $\geq 1$ data from the dying aeon seeds the axioms of the next.

The universe does not resolve its own incompleteness. It iterates past it. Each aeon is a consistent fragment bounded by the limit of finite derivation.
<!-- FILE_END: information-paradox-incompleteness.md -->