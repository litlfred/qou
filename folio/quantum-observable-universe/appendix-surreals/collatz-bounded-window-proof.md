*Item 1.* Put $f_j = q^{N_0} P_j \in \mathbb{Z}[q]$. Multiplying the step relations by $q^{N_0}$ gives

$$
(q + 1) f_{j+1} = f_j \quad\text{(even step)}, \qquad (q + 1) f_{j+1} = [3]_q f_j + q^{N_0} \quad\text{(odd step)}.
$$

Let $\bar f_j \in \mathbb{F}_2[q]$ be the reduction modulo $2$. There are three facts.

- *The reduction fixes the step type.* Evaluate the reduced relation at $q = 1$, where $q + 1 = 0$ and $[3]_q = 1$ in $\mathbb{F}_2$. An even step gives $\bar f_j(1) = 0$, and an odd step gives $\bar f_j(1) = 1$.
- *The reduction fixes the next reduction.* If $\bar f_i = \bar f_j$, the two steps have the same type. Then $(q+1)\bar f_{i+1} = (q+1)\bar f_{j+1}$, and $q + 1 \neq 0$ in the domain $\mathbb{F}_2[q]$, so $\bar f_{i+1} = \bar f_{j+1}$.
- *There are finitely many reductions.* Each $\bar f_j$ is a polynomial over $\mathbb{F}_2$ of degree at most $m$, so there are at most $2^{m+1}$ of them.

By pigeonhole, $\bar f_a = \bar f_c$ for some $a < c$. By the second fact and induction, $\bar f_{a+k} = \bar f_{c+k}$ for all $k$. By the first fact, steps $a + k$ and $c + k$ have the same type. So the parity sequence repeats with period $c - a$ from $a$ on. Item 2 of the [Syracuse lift](#prop:collatz-syracuse-lift) gives $P_c = P_a$. The [cycle classification](#prop:collatz-no-cycles) then lists the cycle through $P_a$.

*Item 2.* The first half is item 1. For the second, item 3 of the [Syracuse lift](#prop:collatz-syracuse-lift) shows that an eventually periodic Syracuse orbit of $P_0(1)$ would bring the $q$-orbit onto a known cycle. $\square$

No real value of $q$ and no bound on the coefficients is used. The coefficients may grow; only their parities matter.
