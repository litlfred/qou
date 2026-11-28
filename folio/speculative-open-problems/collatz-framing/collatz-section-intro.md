**What this chapter proves about Collatz, and what it does not.** Nothing in the Quantum Observable Universe monograph \cite{leitner2026} or in this chapter proves the classical Collatz conjecture \cite{collatz1937,lagarias2010}, and nothing here constitutes a step toward proving it. The underlying algebraic system is a partial affine $[2]_q$-division map $\mathcal{C}_q$ on the Laurent ring $\mathbb{Z}[q^{\pm 1}]$: for $[2]_q = q + 1$ and $[3]_q = q^2 + q + 1$,

$$
\mathcal{C}_q(P) =
\begin{cases}
  P / [2]_q & \text{if } P(-1) = 0,\\[4pt]
  \bigl([3]_q P + 1\bigr) / [2]_q & \text{if } P(-1) = -1,
\end{cases}
$$

undefined when $P(-1) \notin \{0, -1\}$. An element whose entire forward orbit stays in the domain is called *domain-stable*.

**Proved Laurent-ring algebra (retained in the main monograph).**

1. *Specialisation at $q = 1$ recovers the Syracuse map.* Evaluating $P \mapsto P(1)$ sends an even step to $n \mapsto n/2$ and an odd step to $n \mapsto (3n + 1)/2$, matching the classical parity of $P(1)$ at every step.
2. *Complete cycle classification in $\mathbb{Z}[q^{\pm 1}]$.* The only periodic orbits of $\mathcal{C}_q$ in $\mathbb{Z}[q^{\pm 1}]$ are $\{0\}$, the odd fixed point $\{-q^{-2}\}$, and the fundamental $2$-cycle $\{q^{-1}, 1 + q^{-1}\}$ (lifting $\{0\}$, $\{-1\}$, and $\{1, 2\}$).
3. *Classical convergence implies $q$-convergence on lifts.* If the Syracuse orbit of $P(1)$ is eventually periodic, any domain-stable lift $P$ reaches one of the three cycles above; consequently, classical no-divergence implies $q$-Collatz convergence, not the reverse, and non-trivial negative integer cycles (if any existed, or classical $3n - 1$ counterparts such as $\{-5, -7, -10\}$) admit no domain-stable lift.
4. *Bounded exponent window implies convergence.* Any domain-stable orbit whose support stays within a fixed degree window $q^{-N_0}\mathbb{Z}[q]_{\le m}$ has finitely many $\mathbb{F}_2[q]$ reductions, forcing an eventually periodic parity word and hence convergence to one of the three cycles; any counterexample must therefore have unbounded exponent support and lift an unbounded Syracuse orbit.

**Withdrawn over-claims and open boundaries (recorded below).**

- *Contact-average threshold $\langle v_{[2]} \rangle \ge 2$ fails.* Because $\mathcal{C}_q$ already divides by $[2]_q$ inside its odd step, the fundamental cycle $\{q^{-1}, 1 + q^{-1}\}$ has $\langle v_{[2]} \rangle = 1 < 2$, and a degree count forces $\limsup \langle v_{[2]} \rangle \le 1$ on every domain-stable orbit with infinitely many odd steps.
- *Odd-step output need not be $q$-even.* Differentiating $[2]_q R = [3]_q P + 1$ at $q = -1$ gives $R(-1) = 1 + P'(-1)$, as witnessed by the odd fixed point $-q^{-2} \mapsto -q^{-2}$.
- *Heuristic contractions and surreal monomials.* Real-valued Lyapunov expressions $\log_q |P(q)|$ are undefined on general Laurent polynomials, leave the classical parity sequence unchanged, and in the surreal register assert unproved contact-volume scalings whose conclusion is withdrawn.
