## Proof

The Lean proof in [`t-beta-markov-collapse-general-lift.lean`](t-beta-markov-collapse-general-lift.lean) follows the same Lagrangian / completing-the-square argument as the substrate-model version, lifted to the general algebra:

1. **Algebra identity** (`completing_the_square_general`): for any $X \in A$, $S \in R$,
   $$\tau(X \cdot X) = \tau\!\big((X - S \cdot 1)(X - S \cdot 1)\big) + 2 S \cdot \tau(X) - S^2.$$
   Mechanical expansion using centrality of $S \cdot 1_A$ (`Algebra.commutes`) plus $R$-linearity of $\tau$.
2. **Constraint substitution** ($\tau(X) = S$, $\tau(1) = 1$):
   $$\tau(X \cdot X) = \tau\!\big((X - S \cdot 1)^2\big) + S^2.$$
3. **PSD bound** (`PSDTrace.psd`): $\tau\!\big((X - S \cdot 1)^2\big) \ge 0 \Rightarrow \tau(X \cdot X) \ge S^2$.
4. **Equality case** (`markov_frobenius_min_norm_uniqueness`, using `NonDegTrace.nondeg`): $\tau\!\big((X - S \cdot 1)^2\big) = 0 \Leftrightarrow X - S \cdot 1 = 0$.
