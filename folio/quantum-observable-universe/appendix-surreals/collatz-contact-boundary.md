**Status: false as stated; kept as a record.** The fundamental cycle $\{q^{-1}, 1 + q^{-1}\}$ converges trivially and has $\langle v_{[2]} \rangle = 1 < 2$, so "converges only if $\langle v_{[2]} \rangle \geq 2$" fails. The threshold $2$ counts the halving that $\mathcal{C}_q$ already performs inside its odd step ([contact boundary](#def:collatz-contact-boundary)). With that halving removed the threshold would be $1$, and every domain-stable orbit with infinitely many odd steps has limit at most $1$ ([section introduction](#sec:collatz-intro), item 7). So the limiting contact average cannot carry the conjecture in either convention. The argument below is the heuristic count at a real $q > 0$. The Lean file it cites proves facts about $\chi(A)$ and the real inequalities $[2]_q < [3]_q < [2]_q^2$, not convergence.

**Within a QOU with $2 \mid \chi(A)$; conditional on [The $q$-Collatz conjecture: Skein-module crossing resolution](#conj:q-collatz).**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with aether parameter $q$ whose Frobenius–Hopf object satisfies $2 \mid \chi(A)$ — for instance the Descartes universe, $\chi_{\mathrm{eu}}(M_0) = -6$ — and let $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2, \xi_q)$ be its Reeb bundle ([Reeb bundle](#def:reeb-bundle)) with $U(1)$ fiber parametrized by $q = e^{i\varTheta}$. The parity $2 \mid \chi(A)$ is what makes the $[2]_q$-divisor Kummer-removable below; $\chi_{\mathrm{eu}}(M_0) = -6$ is a property of the Descartes universe, not of a general QOU. The $q$-Collatz orbit of $P \in \mathcal{S}(q)_{>0}$ converges if and only if its orbit contact average ([Collatz contact boundary](#def:collatz-contact-boundary)) attains the threshold $\langle v_{[2]} \rangle(P) \geq 2$. Equivalently, the $q$-Collatz conjecture is the contact condition

$$
\bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle \geq 2 \quad\text{for all } P \in \mathcal{S}(q)_{>0}.
$$

**Proof.**
Since $1 < v^*(q) < 2$ (as $[2]_q < [3]_q < [2]_q^2$), the orbit converges whenever each tripling is followed by at least two halvings on average, i.e., $\langle v_{[2]} \rangle(P) \geq 2$.

Two halvings multiply by $[2]_q^{-2}$; one tripling multiplies by $[3]_q / [2]_q$. The net factor per cycle is

$$
\frac{[3]_q}{[2]_q} \cdot \frac{1}{[2]_q^2} = \frac{[3]_q}{[2]_q^3}.
$$

This is contractive because $[3]_q < [2]_q^2 < [2]_q^3$. The contraction ratio is

$$
\frac{[3]_q}{[2]_q^3} = \frac{[2]_q^2 - q}{[2]_q^3} = \frac{1}{[2]_q} - \frac{q}{[2]_q^3}.
$$

The orbit shrinks by slightly more than $1/[2]_q$ per cycle. The margin between two halvings and the minimum needed is

$$
[2]_q^2 - [3]_q = q.
$$

Since $q$ is positive, the per-cycle factor is strictly contractive and the threshold $\langle v_{[2]} \rangle \geq 2$ is sufficient for convergence.

The sharp threshold is $v^* = \log [3]_q / \log [2]_q$. Since $v^* < 2$ is proved algebraically, the integer condition $\langle v_{[2]} \rangle \geq 2$ avoids transcendental quantities.

At $q = 1$, the average $2$-adic valuation of $3n+1$ for odd $n$ is exactly $2$ (from $\Pr(v_2(3n+1) = k) = 2^{-k}$). This provides exactly two halvings per tripling, meeting the threshold.
