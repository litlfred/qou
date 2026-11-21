**Conjecture.** Fix a substrate datum: a candidate zeta function $\zeta$, its Chebyshev-type prime-counting function $\psi$, and the Reeb spectrum $\rho$ of the same substrate. The following are equivalent:

1. **Macroscopic stability.** $\psi(X) = X + O(X^{1/2 + \varepsilon})$ for every $\varepsilon > 0$.
2. **Riemann hypothesis.** Every zero of $\zeta$ in the critical strip satisfies $\mathrm{Re}(s) = 1/2$.
3. **Critical-line spectrum.** Every Reeb eigenvalue $\rho(n, i)$, at every deformation level $n$, satisfies $\mathrm{Re}(\rho(n,i)) = 1/2$.

The three conditions are properties of **one** system. This is not a stylistic point: quantifying over them independently makes the statement false, as recorded below.

The equivalence $(1) \Leftrightarrow (2)$ is classical in one direction — von Koch (1901) proved that the Riemann hypothesis implies the optimal Chebyshev error term, and the converse follows from the explicit formula, since a zero with $\mathrm{Re}(\rho) > 1/2$ makes the oscillatory contribution $X^{\rho}/\rho$ violate the bound. It is nonetheless carried here as a hypothesis rather than as an established input. The equivalence $(2) \Leftrightarrow (3)$ is the framework's own claim and is **open**.

The algebraic substrate supplies a conditional framework: $q$-scale stability is proved, and macroscopic stability is what would require the Riemann hypothesis. The obstruction to extending the $q$-scale result is that the classical limit functor $\mathcal{L}$ is not full — the relative phases of the local spectra are lost in the adelic assembly.

## Status

The statement is carried as a single conjecture over one datum and is not established. The one result proved is conditional on it and derives the remaining equivalence $(1) \Leftrightarrow (3)$ by transitivity; it is a derivation from the hypotheses, not a restatement of one.

## Two inconsistent formulations withdrawn

An earlier version of this statement asserted the two equivalences as axioms, each quantified over its two arguments **independently**:

$$
  \forall\, \psi\ \forall\, \zeta,\quad
  \mathrm{Stability}(\psi) \iff \mathrm{RH}(\zeta),
  \qquad
  \forall\, \zeta\ \forall\, \rho,\quad
  \mathrm{RH}(\zeta) \iff \mathrm{Persistence}(\rho).
$$

Both are inconsistent, and for the same reason. A statement of the form $\forall a\, \forall b,\ P(a) \iff Q(b)$ forces $P$ to be constant in $a$: fix any $b$ and the right-hand side no longer varies, so all values of $P$ agree. But $\mathrm{RH}$ is not constant in $\zeta$. It holds vacuously at $\zeta \equiv 1$, which is never zero, and fails at $\zeta \equiv 0$, for which every point of the strip is a zero and $s = 1/4$ would have to satisfy $1/4 = 1/2$. Substituting both into either axiom, with the other argument held fixed, yields a contradiction.

A second and independent route was available for the second axiom. The proposition it called *spectral persistence* read "if every level is $1/2$ then level $0$ is $1/2$", which is instantiation and is provable outright, so the axiom equated $\mathrm{RH}(\zeta)$ with a tautology for every $\zeta$. The replacement condition (3) constrains the whole family instead, and has content.

Nothing downstream inherited the inconsistency.

The withdrawn axioms were attributed to von Koch and to Weil. The von Koch attribution is accurate for the direction it names and is retained as such above. The Weil attribution was not: the explicit formula is a duality between zeros and prime powers, and no formulation of it makes the Riemann hypothesis equivalent to a proposition in which $\zeta$ does not occur. It is withdrawn.
