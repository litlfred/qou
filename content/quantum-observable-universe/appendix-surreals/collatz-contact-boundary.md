**Proposition (conditional on [`conj:q-collatz`](#conj:q-collatz); "$[2]_q$-contact boundary").**

Let $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2, \xi_q)$ be the Reeb bundle ([Reeb bundle](#def:reeb-bundle)) with $U(1)$ fiber parametrized by $q = e^{i\varTheta}$ for $\varTheta \in [0, 2\pi)$. The $q$-Collatz orbit of $P \in \mathcal{S}(q)_{>0}$ converges if and only if its orbit contact average ([Collatz contact boundary](#def:collatz-contact-boundary)) attains the threshold $\langle v_{[2]} \rangle(P) \geq 2$. Equivalently, the $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz)) reduces to the uniform contact condition:

$$
  \boxed{
  \bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle
   \geq  2
  \quad\text{for all } P \in \mathcal{S}(q)_{>0}.
  }
$$

### Proof

The algebraic bounds $[2]_q < [3]_q < [2]_q^2$ imply the sharp contact threshold $v^*(q)$ strictly bounds $1 < v^*(q) < 2$. The orbit therefore converges whenever each tripling is followed by at least two halvings on average, requiring exactly $\langle v_{[2]} \rangle(P) \geq 2$.

Two halvings multiply by $[2]_q^{-2}$. One tripling multiplies by $[3]_q / [2]_q$. The net factor for one tripling and two halvings is:

$$
  \frac{[3]_q}{[2]_q} \cdot \frac{1}{[2]_q^2}
  = 
  \frac{[3]_q}{[2]_q^3}.
$$

This factor is strictly contractive because $[3]_q < [2]_q^2 < [2]_q^3$. The contraction ratio is:

$$
  \frac{[3]_q}{[2]_q^3}
  = 
  \frac{[2]_q^2 - q}{[2]_q^3}
  = 
  \frac{1}{[2]_q} - \frac{q}{[2]_q^3}.
$$

The orbit shrinks by slightly more than $1/[2]_q$ per cycle. The margin between two halvings and the exact threshold is:

$$
  [2]_q^2 - [3]_q =  q.
$$

Since the substrate parameter $q$ is positive, the per-cycle factor is strictly contractive. The threshold $\langle v_{[2]} \rangle \geq 2$ guarantees convergence.

The sharp theoretical threshold is $v^* = \log [3]_q / \log [2]_q$. Because $v^* < 2$ holds algebraically, the integer condition $\langle v_{[2]} \rangle \geq 2$ suffices and bypasses transcendental evaluations.

At $q = 1$, the exact probability $\Pr(v_2(3n+1) = k) = 2^{-k}$ yields $\mathbb{E}[v_2] = 2$. The classical Collatz average of two halvings per tripling sits precisely on this integer threshold. $\qquad\blacksquare$
