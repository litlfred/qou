Three constructs bear the name "Markov":
1. **Markov trace:** The algebraic functional $\mathrm{tr}_M$ on the Hecke algebra that feeds the mass formula.
2. **Markov chain:** The stochastic random walk on braid words induced by Hecke transition probabilities, which provides error bounds.
3. **Markov moves:** The topological operations of conjugation and stabilisation that generate link equivalence.
Context clarifies usage, but when precision is needed, $\mathrm{tr}_M$ denotes the algebraic functional, "Markov chain" the stochastic process, and "Markov move" the topological equivalence.

## The trace does not require a closure; the topological reading does

A distinction the three senses above leave implicit, and which is load-bearing.

$\mathrm{tr}_M$ is defined on **all** of $H_n(q)$ by cyclicity together with the Markov property $\mathrm{tr}_M(x\sigma_n) = z\,\mathrm{tr}_M(x)$. It is a linear functional on an algebra, and it evaluates on **any** Hecke element — no braid, no closure, and no topology are needed for the number to exist.

What the closure supplies is the **interpretation**. By Markov's theorem two braids have the same closure exactly when they are related by conjugation and stabilisation; because $\mathrm{tr}_M$ is invariant under both (modulo the writhe prefactor of [the stabilisation remark](#rem:jones-markov-trace-stabilisation)), it descends to a **link invariant** on closures. That descent is what licenses reading $\mathrm{tr}_M(\rho(\beta))$ as a property of the link $K_\beta$.

**Consequently, for $W \in H_n(q)$ that is not in the image of $\rho : B_n \to H_n(q)$, $\mathrm{tr}_M(W)$ is a well-defined number with no link behind it.** Such a $W$ decomposes as a weighted sum of braid images, so $\mathrm{tr}_M(W)$ is a weighted sum of link invariants — not the invariant of any one link. Any construction that reads a *topological* quantity off $\mathrm{tr}_M(W)$ (a volume, a crossing number, a genus) must first establish that $W$ **is** a braid image; linearity of $\mathrm{tr}_M$ does not transport such quantities, because they are not linear.

The consequence matters in practice: an element whose letters are of the form $c\,\sigma_g + d\,\mathbf{1}$ rather than braid generators has a well-defined Markov trace, but no hyperbolic volume can be read off it.
