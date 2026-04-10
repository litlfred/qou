Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with $N$ non-interacting particle knots in a region
$U \subset M$.  Let $P_q$, $V_q$, $T_q$ be the quantum
pressure, volume, and temperature of $U$
([quantum pressure](#def:quantum-pressure),
[quantum volume](#def:quantum-volume),
[quantum temperature](#def:quantum-temperature)).
Then the equation of state is

$$
  P_q \, V_q
  \;=\; N \, T_q
  \left(
    1 \;+\; \frac{\hbar_q^2}{[2]_q}
    \,\langle S_q \rangle
  \right),
$$

where $\langle S_q \rangle$ is the thermal expectation of
the categorical action
([categorical action](#def:categorical-action)) and
$[2]_q = q + q^{-1}$ is the quantum $2$-number.

**Derivation.**
The proof proceeds from the partition function, not from
billiard-ball kinematics.

*Step 1: Single-particle partition function.*
A single particle knot $K$ in the $S^3$ fibre at a brane
point $p$ has categorical action $S_q(K)$, the Markov
trace of its Hecke algebra representative.  The
single-particle partition function in a single fibre is

$$
  z_q
  \;=\;
  \sum_{K \,\in\, \mathrm{Conf}_p}
  e^{-\beta_q \, S_q(K)},
$$

where the sum ranges over knot configurations that fit
in the fibre.  The number of available configurations is
proportional to the fibre volume
$\mathrm{Vol}(S^3_q) = 2\pi^2 [2]_q$
([quantum volume](#def:quantum-volume)).

*Step 2: $N$-particle partition function.*
For $N$ non-interacting knots distributed across $|U|$
brane points (the quantum analogue of "ideal gas"):

$$
  Z_q
  \;=\; \frac{1}{N!}
  \left( |U| \cdot z_q \right)^N.
$$

The $1/N!$ arises from the braid group statistics: the knots
are indistinguishable under isotopy, just as Gibbs required
$1/N!$ for classical indistinguishable particles — but here
it is a consequence of the braid group action on
$\mathrm{Conf}(U)$, not an *ad hoc* correction.

*Step 3: Free energy and pressure.*
The quantum free energy is
$F_q = -T_q \ln Z_q$.  Using Stirling and
$V_q = |U| \cdot \mathrm{Vol}(S^3_q)$:

$$
  F_q
  \;=\; -N T_q
  \left(
    \ln\!\frac{V_q}{N \cdot \mathrm{Vol}(S^3_q)}
    \;+\; \ln z_q \;+\; 1
  \right).
$$

Taking $P_q = -(\partial F_q / \partial V_q)|_{T_q}$
with $V_q = |U| \cdot 2\pi^2 [2]_q$:

$$
  P_q \, V_q \;=\; N \, T_q.
$$

This is the **leading-order** quantum ideal gas law.

*Step 4: $q$-anomaly correction.*
The leading order assumes that $z_q$ is independent of
$V_q$ — i.e., that the single-fibre partition function does
not depend on how many fibres are available.  But the
$q$-anomaly from $d_q^2 \neq 0$ introduces a boundary
correction: each time a knot configuration
$K$ approaches $\partial U$, the Frobenius pairing
contributes a boundary pressure term
$P_q^{(\mathrm{boundary})} \propto \hbar_q^2 / V_q$
([quantum pressure](#def:quantum-pressure)).

The corrected equation of state is

$$
  P_q \, V_q
  \;=\; N \, T_q
  \left(
    1 \;+\;
    \frac{\hbar_q^2}{[2]_q}
    \,\langle S_q \rangle
  \right),
$$

where the correction term
$\hbar_q^2 \,\langle S_q \rangle / [2]_q$ is the ratio of
the $q$-anomaly energy to the fibre volume.

**Noether invariant.**
The quantum ideal gas law is the equation of state
associated to the **scale symmetry** of the partition
function.  In the $q$-deformed Noether dictionary
([Noether theorem](#rem:noether-theorem-callout)),
the conserved quantity under simultaneous rescaling of
$V_q$ and $\beta_q$ is the quantum free energy $F_q$
itself.  The identity $P_q V_q = N T_q (1 + \cdots)$ is
the Ward identity of this scale symmetry — the analogue
of the classical Euler relation
$E = TS - PV + \mu N$.

Explicitly, define the **thermodynamic Noether current**

$$
  \mathcal{J}_q^{\mathrm{thermo}}
  \;:=\;
  V_q \,\frac{\partial}{\partial V_q}
  \;+\;
  \beta_q \,\frac{\partial}{\partial \beta_q}.
$$

Then $\mathcal{J}_q^{\mathrm{thermo}}(\ln Z_q) = 0$
at the equation-of-state surface, and the quantum ideal
gas law is the content of this vanishing.

**Classical limit.**
As $q \to 1$: $T_q = \hbar_q \to 0$, but
$N T_q = N \hbar_q$ remains finite when rewritten in
physical units via $k_B$.  The correction vanishes as
$\hbar_q^2 \to 0$, and we recover $PV = Nk_BT$.

**Comparison with the classical derivation.**

| Classical | QOU |
|-----------|-----|
| Point particles in a box | Knot configurations in $S^3$ fibres |
| Elastic wall collisions | Frobenius pairing at $\partial U$ |
| Passive boundary | Active boundary with $q$-anomaly $\propto \hbar_q^2$ |
| Temperature by fiat ($\frac{3}{2}k_BT = \langle E_{\mathrm{kin}}\rangle$) | Temperature = Reeb tick rate $\hbar_q$ |
| $1/N!$ (Gibbs *ad hoc*) | $1/N!$ from braid group indistinguishability |
| No phase transitions | Phase transitions from $S^3$ boundary action |
