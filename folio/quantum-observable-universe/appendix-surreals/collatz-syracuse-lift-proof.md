*Item 1.* Apply $\mathrm{ev}_1$ to the step relations. An even step $[2]_q P_{j+1} = P_j$ becomes $2\,\mathrm{ev}_1(P_{j+1}) = \mathrm{ev}_1(P_j)$, so $\mathrm{ev}_1(P_j)$ is even and $\mathrm{ev}_1(P_{j+1})$ is its half. An odd step $[2]_q P_{j+1} = [3]_q P_j + 1$ becomes $2\,\mathrm{ev}_1(P_{j+1}) = 3\,\mathrm{ev}_1(P_j) + 1$, so $\mathrm{ev}_1(P_j)$ is odd and $\mathrm{ev}_1(P_{j+1}) = T(\mathrm{ev}_1(P_j))$.

*Item 2.* Put $D_j = P_{N+K+j} - P_{N+j}$. Steps $N+K+j$ and $N+j$ have the same type, and subtracting the two step relations removes the $+1$:

$$
[2]_q\, D_{j+1} = c_j\, D_j, \qquad c_j \in \{1, [3]_q\}.
$$

By induction, $[2]_q^{\,n} D_n = \bigl(\prod_{j<n} c_j\bigr) D_0$ for every $n$. By Bézout, $[3]_q - q[2]_q = 1$, so each $c_j$ is coprime to $[2]_q$, and so is their product. Hence $[2]_q^{\,n} \mid D_0$ for every $n$. A nonzero Laurent polynomial cannot be divisible by every power of $[2]_q$: multiply by a power of $q$ to make it a polynomial $f \neq 0$. Since $q + 1$ is coprime to $q$, $(q+1)^n \mid f$, and $n \le \deg f$. So $D_0 = 0$.

*Item 3.* If $T^{N+K}(n_0) = T^N(n_0)$ for $n_0 = P_0(1)$, then $\mathrm{ev}_1(P_{j+K}) = \mathrm{ev}_1(P_j)$ for all $j \geq N$, by item 1 and induction. By item 1 again, the step types repeat with period $K$ from $N$ on. Item 2 gives $P_{N+K} = P_N$, so $P_N$ lies on a periodic orbit of $\mathcal{C}_q$. The [cycle classification](#prop:collatz-no-cycles) lists those orbits.

*Item 4* is item 3 applied to every orbit. $\square$

Nothing in the argument uses a real value of $q$ or a positivity hypothesis.
