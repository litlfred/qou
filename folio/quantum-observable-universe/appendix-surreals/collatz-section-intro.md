**What this section proves about Collatz, and what it does not.** Nothing here proves the Collatz conjecture, and nothing here is a step toward a proof of it. The section studies a deformation of the Syracuse map to the Laurent ring $\mathbb{Z}[q^{\pm 1}]$, which is the Skein module $\mathcal{S}(q)$ of the Reeb bundle, and it records what can be proved about that deformation. Every claim below has one of four labels: *proved* (with a Lean proof that states the same thing), *provable now* (an argument is written out here and no Lean proof exists yet), *open*, and *out of reach*.

**The map.** Write $[2]_q = q + 1$ and $[3]_q = q^2 + q + 1$. For $P \in \mathbb{Z}[q^{\pm 1}]$,

$$
\mathcal{C}_q(P) =
\begin{cases}
  P / [2]_q & \text{if } P(-1) = 0,\\[4pt]
  \bigl([3]_q P + 1\bigr) / [2]_q & \text{if } P(-1) = -1,
\end{cases}
$$

and $\mathcal{C}_q(P)$ is undefined when $P(-1) \notin \{0, -1\}$. Unlike integer parity, this test can fail, so $\mathcal{C}_q$ is a partial map. An element is *domain-stable* if its whole forward orbit stays inside the domain. Domain-stable elements are scarce. The questions below are about them.

**Proved, with Lean.**

1. *Setting $q = 1$ gives the Syracuse map* ([Syracuse lift](#prop:collatz-syracuse-lift)). Evaluation at $q = 1$ sends an even step to $n \mapsto n/2$ and an odd step to $n \mapsto (3n+1)/2$. The type of each step is the ordinary parity of $P(1)$. So a domain-stable orbit follows exactly the classical parity sequence of the integer $P(1)$.
2. *The periodic orbits are known* ([cycle classification](#prop:collatz-no-cycles)). In $\mathbb{Z}[q^{\pm 1}]$ the only periodic orbits are $\{0\}$, the fixed point $\{-q^{-2}\}$ and the cycle $\{q^{-1},\, 1 + q^{-1}\}$. These are the $q$-lifts of the classical cycles $\{0\}$, $\{-1\}$ and $\{1, 2\}$.
3. *Classical convergence implies $q$-convergence* ([Syracuse lift](#prop:collatz-syracuse-lift)). If the Syracuse orbit of $P(1)$ is eventually periodic, the $q$-orbit of a domain-stable $P$ lands on one of the three cycles in item 2. So the classical statement "no Syracuse orbit diverges" implies the convergence half of the [$q$-Collatz conjecture](#conj:q-collatz). A further consequence: no domain-stable $P$ has $P(1)$ on one of the classical negative cycles, such as $\{-5, -7, -10\}$, because those cycles do not lift.
4. *Bounded support implies convergence* ([bounded window](#prop:collatz-bounded-window)). If the support of a domain-stable orbit stays inside a fixed window of exponents, the orbit reaches one of the three cycles. The proof reduces modulo $2$: the reductions take finitely many values, each one fixes the next step and the next reduction, so the parity sequence is eventually periodic, and item 3's argument closes it.
5. *What a counterexample looks like* ([bounded window](#prop:collatz-bounded-window)). A domain-stable orbit that never reaches a known cycle has support in no fixed window, and the Syracuse orbit of its value at $q = 1$ is unbounded.
6. *The identities behind the map.* $[3]_q = q[2]_q + 1$, $[2]_q^2 - [3]_q = q$, and $[2]_q$, $[3]_q$ are coprime ([interpretation](#rem:q-collatz-interpretation)).

**Provable now (no Lean proof yet).**

7. *The limiting contact average is at most $1$.* The degree goes up by one at an odd step and down by one at an even step, and the lowest exponent never decreases below $\min(\operatorname{ord}_q P_0, 0)$. This shows that along a domain-stable orbit with infinitely many odd steps, the even steps outnumber the odd steps by at most a bounded amount. So the average $[2]_q$-adic valuation after an odd step ([contact boundary](#def:collatz-contact-boundary)) tends to at most $1$. It equals $1$ on the cycle $\{q^{-1}, 1 + q^{-1}\}$. The criterion "converges if and only if $\langle v_{[2]} \rangle \geq 2$" in [contact boundary](#conj:collatz-contact-boundary) is therefore false as stated: the fundamental cycle converges and has $\langle v_{[2]} \rangle = 1$. The threshold $2$ is the classical heuristic count of halvings per tripling, which also counts the halving that $\mathcal{C}_q$ already builds into its odd step.

8. *The mod-$2$ shadow.* Reduction modulo $2$ turns $\mathcal{C}_q$ into a map on $\mathbb{F}_2[q^{\pm 1}]$ that is defined everywhere, because every element there has value $0$ or $1$ at $q = 1$. The argument behind item 4 shows that a domain-stable orbit converges exactly when its mod-$2$ shadow is eventually periodic.

**Open.** Each open problem is discussed in [open problems](#rem:collatz-open-problems): the conjecture itself in the form "no domain-stable Laurent polynomial lifts a divergent Syracuse orbit", which integers lift, the mod-$2$ shadow, and the braid form.

**Out of reach, and not claimed.**

9. *Classical Collatz.* Nothing here implies it. The implication runs the other way, by item 3. The deformation gives classical information only for integers that have a domain-stable lift, and that set is sparse ([open problems](#rem:collatz-open-problems)).
10. *The "margin $q$" picture.* The gap $[2]_q^2 - [3]_q = q$ is correct algebra. The contraction factors $[3]_q/[2]_q^v$ describe values at a real $q$. By item 1, though, the parity sequence of a $q$-orbit is the classical one, so the deformation leaves untouched the combinatorics that makes Collatz hard. The margin does not give a proof route.
11. *The surreal bound and the Kummer obstruction.* The [surreal bound](#rem:collatz-surreal-bound) is an analogy. Its scaling laws are asserted, not derived, and it is not an argument. The Kummer obstruction $\kappa_C$ vanishes at level $2$ because $2 \mid \chi(A)$. This is proved, and it is a divisibility fact that does not bear on convergence.

**Reading order.** The [conjecture](#conj:q-collatz) comes first, then the [valuation](#def:two-q-adic-valuation) and the [contact boundary](#def:collatz-contact-boundary). The proved results follow: [cycle classification](#prop:collatz-no-cycles), [Syracuse lift](#prop:collatz-syracuse-lift) and [bounded window](#prop:collatz-bounded-window). Then come the [open problems](#rem:collatz-open-problems), and the heuristic remarks come last.
