Fix a substrate datum: a candidate zeta function $\zeta$, its Chebyshev-type prime-counting function $\psi$, and the Reeb spectrum $\rho$ of the same substrate. The following are equivalent:

1. **Macroscopic stability.** $\psi(X) = X + O(X^{1/2 + \varepsilon})$ for every $\varepsilon > 0$.
2. **Riemann hypothesis.** Every zero of $\zeta$ in the critical strip satisfies $\mathrm{Re}(s) = 1/2$.
3. **Critical-line spectrum.** Every Reeb eigenvalue $\rho(n, i)$, at every deformation level $n$, satisfies $\mathrm{Re}(\rho(n,i)) = 1/2$.

The three conditions are properties of **one** system. This is not a stylistic point: quantifying over them independently makes the statement false, as recorded below.

The equivalence $(1) \Leftrightarrow (2)$ is classical in one direction — von Koch (1901) proved that the Riemann hypothesis implies the optimal Chebyshev error term, and the converse follows from the explicit formula, since a zero with $\mathrm{Re}(\rho) > 1/2$ makes the oscillatory contribution $X^{\rho}/\rho$ violate the bound. It is nonetheless carried here as a hypothesis rather than as an established input. The equivalence $(2) \Leftrightarrow (3)$ is the framework's own claim and is **open**.

The algebraic substrate supplies a conditional framework: $q$-scale stability is proved, and macroscopic stability is what would require the Riemann hypothesis. The obstruction to extending the $q$-scale result is that the classical limit functor $\mathcal{L}$ is not full — the relative phases of the local spectra are lost in the adelic assembly.

## Status

The statement is carried as a single conjecture over one datum and is not established. The one result proved is conditional on it and derives the remaining equivalence $(1) \Leftrightarrow (3)$ by transitivity; it is a derivation from the hypotheses, not a restatement of one.

## Why independent quantification is inconsistent

Quantifying the two equivalences over their arguments **independently** —

$$
  \forall\, \psi\ \forall\, \zeta,\quad
  \mathrm{Stability}(\psi) \iff \mathrm{RH}(\zeta),
  \qquad
  \forall\, \zeta\ \forall\, \rho,\quad
  \mathrm{RH}(\zeta) \iff \mathrm{Persistence}(\rho)
$$

— produces an inconsistent theory for a purely logical reason. Any axiom of the form $\forall a\, \forall b,\ P(a) \iff Q(b)$ forces $P$ to be constant in $a$: fixing $b$ freezes the right-hand side, so all values of $P$ must agree. Yet $\mathrm{RH}(\zeta)$ is not constant in $\zeta$: it holds vacuously at $\zeta \equiv 1$ (which has no zeros) and fails at $\zeta \equiv 0$ (for which every point of the strip is a zero, forcing $1/4 = 1/2$ at $s = 1/4$). Substituting both into either independently quantified biconditional with the second argument held fixed yields a contradiction.

Similarly, weakening condition (3) to the implication "if every level has real part $1/2$, then level $0$ has real part $1/2$" reduces the right-hand side to universal instantiation, a tautology, which again cannot be equivalent to $\mathrm{RH}(\zeta)$ across varying $\zeta$. Constraining the entire family $\rho(n, i)$ in condition (3) over a single bound datum $(\zeta, \psi, \rho)$ avoids both pathologies. Likewise, Weil's explicit formula establishes a duality between the zeros and prime-power coefficients of the *same* $\zeta$; no formulation of it equates $\mathrm{RH}(\zeta)$ to a predicate in which $\zeta$ does not occur.
