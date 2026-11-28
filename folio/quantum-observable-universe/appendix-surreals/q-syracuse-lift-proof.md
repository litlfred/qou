*Item 1.* Applying $\mathrm{ev}_1$ to $[2]_q P_{j+1} = P_j$ gives $2\,\mathrm{ev}_1(P_{j+1}) = \mathrm{ev}_1(P_j)$, so $\mathrm{ev}_1(P_j)$ is even and $\mathrm{ev}_1(P_{j+1}) = \mathrm{ev}_1(P_j)/2$. Applying $\mathrm{ev}_1$ to $[2]_q P_{j+1} = [3]_q P_j + 1$ gives $2\,\mathrm{ev}_1(P_{j+1}) = 3\,\mathrm{ev}_1(P_j) + 1$, so $\mathrm{ev}_1(P_j)$ is odd and $\mathrm{ev}_1(P_{j+1}) = T(\mathrm{ev}_1(P_j))$.

*Item 2.* Set $D_j = P_{N+K+j} - P_{N+j}$. Because steps $N + K + j$ and $N + j$ have identical type, subtracting the two step equations cancels the $+1$ term:

$$
[2]_q\, D_{j+1} = c_j\, D_j, \qquad c_j \in \{1, [3]_q\}.
$$

Induction yields $[2]_q^n D_n = \bigl(\prod_{j < n} c_j\bigr) D_0$ for all $n \ge 0$. Since $[3]_q - q[2]_q = 1$, every $c_j$ is coprime to $[2]_q$, so $[2]_q^n \mid D_0$ for every $n \ge 0$. Multiplying $D_0$ by a power of $q$ to obtain a polynomial $f \in \mathbb{Z}[q]$ with $(q + 1)^n \mid f$ for every $n$ forces $f = 0$ (otherwise $n \le \deg f$), hence $D_0 = 0$ and $P_{N+K} = P_N$.

*Item 3.* If $T^{N+K}(n_0) = T^N(n_0)$ for $n_0 = P_0(1)$ and $K \ge 1$, Item 1 gives $\mathrm{ev}_1(P_{j+K}) = \mathrm{ev}_1(P_j)$ for all $j \ge N$, so the step types repeat with period $K$ from $N$ onward. Item 2 then gives $P_{N+K} = P_N$, placing $P_N$ on one of the three periodic orbits of [periodic-orbit classification](#prop:balanced-holonomy-exclusion). $\square$
