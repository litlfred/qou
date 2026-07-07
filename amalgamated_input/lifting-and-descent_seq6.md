<!-- FILE_START: mass-brane-intro.md -->
The direct-limit algebra of the previous section is the arena in which a categorical notion of mass becomes available. This section defines that notion as a Frobenius trace, shows it is well-defined and unique, and connects it to the obstruction class through Euler-characteristic stability.

**Non-commutativity and mass** establishes that mass arises as a non-commutativity invariant of the direct-limit algebra. **Stability of the Euler characteristic** certifies that $\chi(A_n)$ is constant along the tower, the topological invariant on which the mass identity will rest. **Mass (categorical trace)** gives the construction itself, and the paired propositions **Well-definedness of the inertial mass identity** and **Uniqueness of the inertial mass identity** verify that the trace passes through the brane tower and is the unique Frobenius pairing compatible with it. **Homological shell condensation** is the conjectural form of the result we will compute with: BB-stratified $E_\infty^{p,>0}(n) = 0$ at the magic values of $n$.

The next section, *Betti Numbers and Harmonic Basis*, uses the Euler-characteristic stability and the categorical mass to refine the picture by Hodge-theoretic data.
<!-- FILE_END: mass-brane-intro.md -->

<!-- FILE_START: euler-char-stability.md -->
Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe) and let $\{A_n\}_{n \geq 0}$ be its [recursive brane tower](#def:recursive-brane-tower). The categorical Euler characteristic $\chi(A_n) := \mathrm{tr}(\mathrm{id}_{A_n})$ (computed via the rigidity trace of the identity endomorphism in $\mathbf{C}$) is stable under jet prolongation: for each level $n$,

$$
  \chi(A_{n+1}) =  \chi(A_n).
$$

In particular, if the base level satisfies $\chi(A_0) = c \in k$, then $\chi(A_n) = c$ for all $n \geq 0$. In the archimedean realisation, $\chi(A_n) = \chi(\mathcal{S}_n)$ is the topological Euler characteristic of the total space $\mathcal{S}_n$.
<!-- FILE_END: euler-char-stability.md -->

