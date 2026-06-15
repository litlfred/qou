The quantum ideal gas law
([ideal gas law](#prop:quantum-ideal-gas-law))

$$
  P_q \, V_q
  \;=\; N \, T_q
  \left(
    1 + \frac{\hbar_q^2}{[2]_q}\,\langle \mathfrak{S}_q \rangle
  \right)
$$

is a **degree-$0$ section** of an exponentially complex
partition function.  The partition function
$Z_q = (|U| \cdot z_q)^N / N!$ sums over all $N!$ braid
permutations of $N$ knot configurations across $|U|$ fibres.
But the equation of state collapses this exponential sum to
a single polynomial relation among three observables
$(P_q, V_q, T_q)$ --- via $F_q = -T_q \ln Z_q$ and the
Stirling approximation.

This is the Markov trace of statistical mechanics.  Just as
the Markov trace collapses $3^c$ resolution paths to a Skein
polynomial
([Skein Turing machine](#rem:skein-turing-machine)), the
free energy collapses $N!$ microstate configurations to an
equation of state.

**$PV = NkT$ is in the polynomial horizon.**

The full dictionary:

See [Table](#tbl:stat-mech-computational-horizon-table-data).

The equation of state is extractable in polynomial time: the
$\ln Z_q$ computation factors through Stirling's approximation,
which converts the $N!$-fold sum to $O(N \log N)$ operations.
This is precisely the condition for membership in
$\mathcal{R}^{\circ}$ --- the polynomial observable subcategory
([computational horizon](#def:computational-horizon)).

**The $q$-correction is degree-$1$ leakage.**

The correction term $\hbar_q^2 \langle \mathfrak{S}_q \rangle / [2]_q$
is the first piece of boundary information that crosses from
the microstate into the macroscopic equation.  It arises from
the $S^3$ boundary action --- the Frobenius pairing at
$\partial U$ contributes a non-trivial $d_q^2$ correction that
a purely degree-$0$ computation (the classical ideal gas) would
miss.

In the jet-tower language: the classical limit $PV = NkT$ is
purely degree-$0$.  The quantum correction is the degree-$1$
term --- analogous to Hawking radiation leaking through the
jet horizon ([Hawking radiation](#rem:hawking-radiation)).

**Phase transitions are horizon crossings.**

At the critical temperature $T_q^{(c)}$
([phase transitions](#prop:phase-transition-boundary)), the
dominant Hecke representation jumps and the free energy
develops a non-analyticity.  This is a **computational horizon
in the $(T_q, P_q)$ plane**: the degree-$0$ section (which
phase the system is in) becomes discontinuous, while
degree $\geq 1$ data (correlations, critical exponents) varies
continuously across the boundary.

The three phases (gas, liquid, solid) are three connected
components of the polynomial observable subcategory in
configuration space --- three "aeons" of the partition
function, separated by phase boundaries where the degree-$0$
algebra (the dominant representation) vanishes and is replaced.

**Statistical mechanics is the theory of the polynomial
observable subcategory.**

The entire apparatus of statistical mechanics --- partition
functions, free energies, entropy, equations of state --- is
the technology for extracting degree-$0$ and low-degree
sections from exponentially large configuration spaces.  It
exists because we are polynomial-time observers
confronting an exponentially complex microstate.

By the incompleteness proposition
([incompleteness implies horizon](#prop:incompleteness-implies-horizon)),
any Turing-complete system with $\mathbb{N}$-embedding
necessarily has non-computable sections.  Statistical
mechanics is what computation looks like from the polynomial
side of that boundary: an approximation, forced by the
computational horizon, that extracts the accessible
degree-$0$ truth and discards the exponential remainder.
