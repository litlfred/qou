<!-- FILE_START: lagrange-q-kinematics-intro.md -->
The previous section read kinematic data off a single crossing. We now diagonalise the cyclic symmetry that ties crossings together. The relevant cyclic group is $C_5 \subset S_5$ acting on the five branch points of the base surface. The diagonalisation provides the discrete Fourier transform — the Lagrange resolvents. Once $C_5$ is diagonal, the categorical analogues of momentum, angular momentum, and energy emerge as the natural eigencoordinates.

Proposition: Discrete Fourier transform diagonalises $C_5$ on the base surface identifies the Lagrange resolvents $w_0, \dots, w_4$ as the simultaneous eigenvectors of the $C_5$-action on the coordinate ring of $\mathcal{X}_5$. Remark: Lagrange resolvents and spectral form specifies the explicit weight assignments.

With the spectral coordinates established, Definition: $q$-Momentum from the braid writhe defines the eigenvalue of the writhe operator on the first resolvent. Definition: $q$-Angular momentum from the $\mathrm{SU}_q(2)$ Casimir extracts the Casimir of the quantum group along the same eigenline. Definition: $q$-Deformed Energy then merges the two. Remark: Jones polynomial connection, building block values, and nuclear $q$-angular momentum reads the resulting $q$-angular momentum from the building-block knots and matches it with the Jones polynomial evaluation.

The section closes with Remark: Noether's theorem in the $q$-deformed setting. This packages the conservation laws and anomaly terms for the resolvent symmetries in the format required by the rest of the chapter. The next section, **Exceptional Divisor and Vertex Operators**, uses the resolvent decomposition as the eigenstructure on which the vertex operators act.
<!-- FILE_END: lagrange-q-kinematics-intro.md -->

<!-- FILE_START: lagrange-resolvents.md -->
Let $\zeta=e^{2\pi i/n}$. The discrete Fourier transform on $C_n$ ([Lagrange resolvent transform](#prop:lagrange-resolvent-transform)) diagonalises the cyclic action: $\sigma(w_k) = \zeta^{-k} w_k$. Any $C_n$-invariant polynomial constraint on the coordinates $x_j$ transforms to constraints on $C_n$-equivariant combinations of the Fourier modes $w_k$.

For $n = 5$ ([Bring's surface](#def:brings-surface)), the three power-sum equations become:

```tex
\begin{align}
  w_0 &= 0
    &&\text{(linear projection),}
    \label{eq:resolvent-linear}\\[4pt]
  w_1w_4+w_2w_3 &= 0
    &&\text{(Hermitian quadric),}
    \label{eq:resolvent-quadric}\\[4pt]
  w_1^2w_3+w_4^2w_2+w_2^2w_1+w_3^2w_4 &= 0
    &&\text{(symmetric cubic).}
    \label{eq:resolvent-cubic}
\end{align}
```

The quadric pairs conjugate modes ($w_k$ with $w_{5-k}$). The cubic pairs squared modes in the skip-one pattern. These are the $C_5$-equivariant invariants $h_2$ and $h_3$ ([aggregate color quantities](#rem:aggregate-color-quantities)).
<!-- FILE_END: lagrange-resolvents.md -->

<!-- FILE_START: q-momentum.md -->
The **$q$-momentum** of a particle is the writhe of its braid representative, weighted by the Hecke deformation parameter.

**Definition.**
Let $\beta \in B_n$ be a braid representative of a particle knot $K = \hat{\beta}$ (braid closure), with generators $\sigma_{i_1}^{\epsilon_1} \cdots \sigma_{i_k}^{\epsilon_k}$ where $\epsilon_j = \pm 1$. The **$q$-momentum** is:

$$
  p_q(\beta) =  \sum_{j=1}^{k} [\epsilon_j]_q
  =  \sum_{j=1}^{k} \frac{q^{\epsilon_j} - q^{-\epsilon_j}}{q - q^{-1}}
  =  \sum_{j=1}^{k} \epsilon_j = w(\beta)
$$

where $[\epsilon]_q = (q^{\epsilon} - q^{-\epsilon})/(q - q^{-1})$ is the $q$-integer, defined for $q \neq \pm 1$ (so that $q - q^{-1} \neq 0$). On that domain, $[+1]_q = 1$ and $[-1]_q = -1$ *exactly*. Each crossing contributes precisely its sign, and the $q$-momentum coincides with the classical writhe $w(\beta)$ for all such $q$ — not only in the limit $q \to 1$ (where the removable $0/0$ singularity of $[\pm 1]_q$ takes the same values $\pm 1$). The $q$-deformation operates trivially at single crossings; it would distinguish multi-strand contributions $|\epsilon| \geq 2$, but these do not occur in a braid word.

**Equivalently**, the $q$-momentum is the trace of the braid in the fundamental representation of $H_n(R, q)$:

$$
  p_q(\beta) =  \mathrm{tr}_{\mathrm{fund}}(\rho(\beta))
$$

where $\rho: B_n \to H_n(R, q)$ is the Hecke representation.

**Building block values.**

| Knot | Braid word | Writhe $w$ | $p_q(q_0)$ |
|------|-----------|:----------:|:-------------:|
| $0_1$ (unknot) | $e$ | $0$ | $0$ |
| $3_1$ (trefoil) | $\sigma_1^3$ | $+3$ | $+3$ |
| $3_1^{\sigma}$ | $\sigma_1^{-3}$ | $-3$ | $-3$ |
| $4_1$ (figure-eight) | $\sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$ | $0$ | $0$ |
| $5_1$ (cinquefoil) | $\sigma_1^5$ | $+5$ | $+5$ |
<!-- FILE_END: q-momentum.md -->

<!-- FILE_START: q-momentum-properties.md -->
**Proposition.**
*The [$q$-momentum](#def:q-momentum) $p_q$ satisfies:*

1. **Additivity under concatenation**: $p_q(\beta_1 \beta_2) = p_q(\beta_1) + p_q(\beta_2)$ (because the trace is linear on the Iwahori--Hecke algebra).
2. **Invariance under Markov I**: $p_q$ is conjugation-invariant (the cyclic property of the trace).
3. **Shift under Markov II**: stabilization $\beta \mapsto \beta \sigma_n^{\pm 1}$ shifts $p_q$ by $\pm [1]_q$. This is the $q$-analogue of adding one unit of momentum.
4. **Parity**: Under the mirror $\sigma: \beta \mapsto \beta^{\sigma}$ (reverse all crossings), $p_q(\beta^{\sigma}) = -p_{q^{-1}}(\beta)$. Parity violation at $q \neq 1$ means $p_q(\beta^{\sigma}) \neq -p_q(\beta)$.
<!-- FILE_END: q-momentum-properties.md -->

<!-- FILE_START: q-angular-momentum.md -->
The **$q$-angular momentum** of a particle is the $\mathrm{SU}_q(2)$ Casimir eigenvalue of its knot representation.

**Definition.**
Let $K = \hat{\beta}$ be a knot/link with braid representative $\beta \in B_n$. The **$q$-angular momentum** is the eigenvalue of the $q$-Casimir element $C_q$ (cf. [def:q-casimir](#def:q-casimir)) on the spin-$j$ irreducible of $\mathrm{SU}_q(2)$:

$$
  J_q^2(K) =  [j]_q  [j+1]_q
  =  \frac{q^j - q^{-j}}{q - q^{-1}} \cdot
        \frac{q^{j+1} - q^{-(j+1)}}{q - q^{-1}}
$$

where $j$ is the spin quantum number that the Jones--Wenzl projector $p_n$ acting on the $n$-strand braid determines: $j = n/2$ for the highest-weight component.

At $q = 1$: $J_q^2 \to j(j+1)$, the standard Casimir.

**The $q$-deformed angular momentum operators.**

The generators $J_+, J_-, J_z$ of $\mathrm{SU}_q(2)$ satisfy:

$$
  [J_z, J_{\pm}] = \pm J_{\pm}, \qquad
  [J_+, J_-] = [2 J_z]_q
  =  \frac{q^{2J_z} - q^{-2J_z}}{q - q^{-1}}
$$

This diverges from the classical $[J_+, J_-] = 2J_z$ by substituting $2J_z$ with its $q$-number $[2J_z]_q$. The asymmetry at $q \neq 1$ connects directly to parity violation ([parity violation](#prop:parity-violation-skein)). The raising and lowering operators do not relate by a simple conjugation.


**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs—real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. The generic categorical/$q$-deformation identities it relies upon remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-angular-momentum.md -->

<!-- FILE_START: q-angular-momentum-interpretation.md -->
**Connection to the Jones polynomial.**

The Jones polynomial $J_K(q)$ of a knot $K$ is the quantum trace over the spin-$\tfrac{1}{2}$ representation:

$$
  J_K(q) =  \mathrm{tr}_{V_{1/2}}(\rho(\beta))
$$

The colored Jones polynomial $J_K^{(j)}(q)$ uses the spin-$j$ representation. The **recursion** between colored Jones polynomials encodes the $q$-angular momentum:

$$
  J_K^{(j+1/2)}(q) =  [2j+1]_q \cdot J_K^{(j)}(q)
  +  \text{(lower-order terms)}
$$

**Building block values.**

| Knot | $n$ (strands) | $j$ | $J_q^2$ at the substrate parameter $q$ | Classical $j(j+1)$ |
|------|:---:|:---:|:---:|:---:|
| $0_1$ (unknot) | $1$ | $0$ | $0$ | $0$ |
| $3_1$ (trefoil) | $2$ | $\frac{1}{2}$ | $[1/2]_q [3/2]_q = 0.818$ | $0.75$ |
| $4_1$ (figure-eight) | $2$ | $\frac{1}{2}$ | $0.818$ | $0.75$ |
| $5_1$ (cinquefoil) | $2$ | $\frac{1}{2}$ | $0.818$ | $0.75$ |
| $\mathcal{B}_3$ (Borromean) | $3$ | $\frac{1}{2}$ | $0.818$ | $0.75$ |

All single-component knots in $B_2$ carry spin $j = \tfrac{1}{2}$. The nuclear spin depends on coupling: $A$ nucleons (each $j = 1/2$) couple to total $J$ via $q$-Clebsch--Gordan coefficients. The parity of $A$ (modulo 2) determines the $J$ parity ([nuclear spin parity](#prop:nuclear-spin-parity)).

**Nuclear $q$-angular momentum.**

For a nucleus $\mathcal{N}(Z, N)$ with $A = Z + N$:

$$
  J_q^2(\mathcal{N}) =  [J]_q  [J+1]_q
$$

Here $J$ is the ground-state spin fixed by the nuclear link's embedding in the Temperley--Lieb algebra $TL_A(\delta)$ with $\delta = -(q^{1/2} + q^{-1/2})$.
<!-- FILE_END: q-angular-momentum-interpretation.md -->

<!-- FILE_START: q-energy.md -->
The **$q$-energy** of a particle knot $K$ sums three terms derived from the categorical triple $(\mathbf{C}, A, \tau)$ and the substrate parameter $q$.

**Definition.**
Let $K = \hat{\beta}$ be a particle knot with braid representative $\beta \in B_n$. The **$q$-energy** is:

$$
  \mathfrak{E}_q(K) \;=\; \underbrace{J_q^2(K) \cdot \hbar_q}_{\text{rotational}}
  \;+\;
  \underbrace{p_q(\beta)^2 \cdot \hbar_q / (2\,[n]_q)}_{\text{translational}}
  \;+\;
  \underbrace{\mathfrak{S}_q(K)}_{\text{action (rest mass)}}
$$

where:

- $J_q^2(K) = [j]_q [j+1]_q$ is the $q$-angular momentum ([q-angular momentum](#def:q-angular-momentum)),
- $p_q(\beta)$ is the $q$-momentum (writhe) ([q-momentum](#def:q-momentum)),
- $\mathfrak{S}_q(K) = \mathrm{tr}_\tau(\rho(\beta))$ is the categorical action — the Markov trace of the braid in the Hecke algebra $H_n(R, q)$,
- $\hbar_q = 1 - q^{-1}$ is the quantum Planck constant,
- $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-number.

**At rest** ($p_q = 0$, $J_q = 0$):

$$
  \mathfrak{E}_q(K)\big|_{\text{rest}} \;=\; \mathfrak{S}_q(K) \;=\; \mathfrak{m}(K) c^2
$$

This recovers the topological mass formula.
<!-- FILE_END: q-energy.md -->

<!-- FILE_START: q-energy-terms-and-limits.md -->
**Remark (the three energy terms, limits, and crossing-energy relation).**

This remark unpacks the three terms of the [$q$-energy](#def:q-energy) $\mathfrak{E}_q(K)$, its classical and deep-quantum limits, and its relation to the crossing energy.

**The three terms.**

1. **Rotational term** $J_q^2 \cdot \hbar_q$: The $q$-deformed rotational energy. For a spin-$\frac{1}{2}$ particle at the substrate parameter $q$, this yields $[1/2]_q [3/2]_q \cdot \hbar_q \approx 0.818 \times 0.0991 = 0.0811$. This vanishes at $q = 1$ (where $\hbar_q \to 0$).
2. **Translational term** $p_q^2 \cdot \hbar_q / (2[n]_q)$: The $q$-deformed kinetic energy from the writhe. The denominator $[n]_q$ provides the $q$-deformed "number of strands" (inertia).
3. **Action term** $\mathfrak{S}_q(K)$: The categorical action $\mathfrak{S}_q = \mathrm{tr}(\mathscr{L}_q)$ evaluated on the knot. This constitutes the **rest mass energy** — the categorical action (Markov trace of the braid representation):

$$
  \mathfrak{S}_q(K) = \mathrm{tr}_M(\rho(\beta))
$$

At a single brane level, this equals $|\mathrm{tr}_M(\rho(\beta))|$ ([categorical mass as Markov trace](#prop:categorical-mass-markov)). The full mass including the brane tower evaluates to $\mathrm{Vol}(K)/\hbar_q^2$ for hyperbolic knots ([topological mass formula](#prop:topological-mass-formula)). For torus knots (including the trefoil / electron), the single-level action is nonzero but the hyperbolic volume vanishes. The mass then arises from the quantum dilogarithm contributions across the tower ([mass endomorphism conjecture](#conj:mass-endomorphism)).

The action term dominates: for hadrons, $\mathfrak{S}_q \sim 10^3$ MeV, while the rotational and translational terms sit at $O(\hbar_q) \sim 0.1$.

**Limits.**

| Limit | $\mathfrak{E}_q$ |
|-------|-------|
| $q = 1$ (classical) | $j(j+1) \cdot 0 + w^2 \cdot 0 + \mathfrak{S}_1 = \mathfrak{S}_1$ |
| $q \to \infty$ (deep-quantum) | $J_q^2 \to q^{2j+1}, \; p_q \to w \cdot q, \; \mathfrak{S}_q \to \infty$ |
| Rest frame | $\mathfrak{S}_q(K)$ (mass) |

**Relation to crossing energy.**

Each crossing in the braid word contributes energy $\mathfrak{E}_\times(q) = \frac{1}{2}(q - q^{-1}) = 0.1045$ (in units of the mass scale $\mu_0$). The total action is:

$$
  \mathfrak{S}_q(K) \;=\; \sum_{j=1}^{k} \mathfrak{E}_\times^{(\epsilon_j)}(q)
$$

where $\epsilon_j = \pm 1$ represents the crossing sign. For a positive crossing: $\mathfrak{E}_\times^{(+)} = q$. For a negative crossing: $\mathfrak{E}_\times^{(-)} = q^{-1}$. The asymmetry $q \neq q^{-1}$ at the substrate parameter $q$ forces positive crossings to carry more energy than negative ones. This is the energy signature of parity violation.
<!-- FILE_END: q-energy-terms-and-limits.md -->

<!-- FILE_START: noether-theorem-callout.md -->
The three $q$-deformed kinematic quantities—$q$-momentum ([q-momentum](#def:q-momentum)), $q$-angular momentum ([q-angular momentum](#def:q-angular-momentum)), and $q$-energy ([q-energy](#def:q-energy))—form a **$q$-deformed Noether dictionary**. Each arises from a symmetry of the categorical action $\mathfrak{S}_q$ ([categorical action](#def:categorical-action)) through the variational equations ([variational equations](#prop:variational-equations)), extending Noether's theorem directly.

| Symmetry | Generator | Conserved quantity ($q = 1$) | $q$-Deformed quantity | Source |
|----------|-----------|-------|---------|--------|
| Time translation | Reeb flow $\xi_R$ | Energy $E$ | $\mathfrak{E}_q(K)$ | Categorical action $\mathfrak{S}_q$ |
| Spatial translation | Braid stabilisation | Momentum $p$ | $p_q(\beta)$ (writhe) | Markov II shift |
| Rotation | $\mathrm{SU}(2)$ action | Angular momentum $J^2$ | $J_q^2 = [j]_q[j+1]_q$ | $\mathrm{SU}_q(2)$ Casimir |
| Gauge | Quantum gauge group $G_q$ | Charge | Coulomb charge $Q(K)$ | Tannaka–Krein reconstruction |

**Classical limit.** At $q = 1$, the $q$-deformations collapse: $\hbar_q \to 0$, $[n]_q \to n$, and each $q$-quantity reduces to its classical counterpart. Noether's theorem holds exactly, and the variational equations yield the standard Einstein, Yang–Mills, and Dirac equations.

**$q$-Anomaly.** At $q \neq 1$, the correspondence **deforms** rather than breaks. The key mechanism is $d_q^2 \neq 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)): the $q$-differential does not square to zero. The classical chain of "symmetry $\Rightarrow$ closed current $\Rightarrow$ conserved charge" acquires a correction term at each step.

1. **Energy** is not naively conserved in transitions. The $Q$-value of a nuclear decay differs from the sum of product kinetic energies by a $q$-anomaly $\delta_q \propto \hbar_q^2$ ([q-value transition](#def:Q-value-transition)). A shift in the effective substrate parameter absorbs the "missing" energy. The conserved quantity is the **full categorical action** evaluated at the shifted $q$.
2. **Momentum** acquires an anomalous correction $\delta p_q \propto \hbar_q$ from the non-commutativity of the Iwahori--Hecke algebra.
3. **Angular momentum** remains exactly conserved (the $\mathrm{SU}_q(2)$ Casimir commutes with the coproduct), but its eigenvalues are $q$-deformed: $[j]_q[j+1]_q \neq j(j+1)$.

Noether's theorem **survives the $q$-deformation**, but the conserved quantities become categorical. They live in the Hecke algebra $H_n(R, q)$, not in classical phase space. The archimedean (numerical) values obtained via the fibre functor $\tau$ carry $q$-corrections, which manifest as measurable anomalies in precision experiments.
<!-- FILE_END: noether-theorem-callout.md -->
