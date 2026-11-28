*Item 1.* Set $f_j = q^{N_0} P_j \in \mathbb{Z}[q]$, so $(q + 1) f_{j+1} = f_j$ on an even step and $(q + 1) f_{j+1} = (q^2 + q + 1) f_j + q^{N_0}$ on an odd step, and write $\bar{f}_j \in \mathbb{F}_2[q]$ for the reduction modulo $2$:

- Evaluating modulo $2$ at $q = 1$ (where $q + 1 = 0$ and $q^2 + q + 1 = 1$ in $\mathbb{F}_2$) gives $\bar{f}_j(1) = 0$ on an even step and $\bar{f}_j(1) = 1$ on an odd step, so $\bar{f}_j$ determines the step type.
- Whenever $\bar{f}_i = \bar{f}_j$, steps $i$ and $j$ share the same type, so $(q + 1)\bar{f}_{i+1} = (q + 1)\bar{f}_{j+1}$ in the integral domain $\mathbb{F}_2[q]$; cancelling $q + 1 \neq 0$ yields $\bar{f}_{i+1} = \bar{f}_{j+1}$.
- Since $\deg \bar{f}_j \le m$, there are at most $2^{m+1}$ polynomials in $\mathbb{F}_2[q]$ of degree at most $m$.

By the pigeonhole principle, $\bar{f}_a = \bar{f}_c$ for some $a < c$, so $\bar{f}_{a+k} = \bar{f}_{c+k}$ and the step types repeat with period $c - a$ for all $k \ge 0$. Item 2 of [Syracuse projection](#prop:q-syracuse-lift) gives $P_c = P_a$, and [periodic-orbit classification](#prop:balanced-holonomy-exclusion) restricts $P_a$ to the three listed cycles.

*Item 2* is the contrapositive of Item 1 combined with Item 3 of [Syracuse projection](#prop:q-syracuse-lift). $\square$
