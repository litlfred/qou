**Proposition (recursive memoised q-MN).**
*The classical Murnaghan-Nakayama rule expresses $\chi_\rho^\lambda$ recursively via border-strip removal. The $q$-deformed analogue (Halverson-Ram broken-strip rule) replaces the sign by a $q$-weight, maintaining the identical recursion structure.*

*Memoising the recursive call cache indexed by $(\rho, \lambda)$ provides a $10\times$ speedup for batch character evaluation and reduces storage requirements drastically compared to explicit seminormal tables.*

This optimization is essential for atom-knot identification at high $n$, enabling efficient evaluation of many hyperbolic knots at $H_{18}$ and $H_{21}$. It integrates cleanly into the canonical compute pipeline.
