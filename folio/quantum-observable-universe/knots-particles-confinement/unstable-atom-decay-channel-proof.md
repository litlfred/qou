**Scope of the LP-relaxation argument.** The proof below was formulated for an existential form of [stability](#def:stable-atom) requiring *some* non-negative integer vector $x \in \mathbb{Z}_{\geq 0}^N$ to satisfy $\mathrm{G}(q)\,x \geq 0$ (which is trivially satisfied by $x = 0$). Under the universal formulation of [stability](#def:stable-atom) applied to the fixed normal-form coefficient vector $x(K, q)$ of $T_w$, the violated constraint is read directly as $\arg\min_\gamma (\mathrm{G}(q)\,x(K, q))_\gamma$ whenever $x(K, q) \in \mathbb{Z}_{\geq 0}^N$; the extension to signed normal-form coefficient vectors and its generic uniqueness remain open.

*Proof.*
*Since $K$ is unstable, the ILP $\{x \in \mathbb{Z}_{\geq 0}^N : \mathrm{G}(q) x \geq 0\}$ has no solution within the confinement filtration $J^{\ell(K, q)}(q)$.*

*Run the LP relaxation $\{x \in \mathbb{R}_{\geq 0}^N : \mathrm{G}(q) x \geq 0\}$. This is always feasible. The trivial $x = 0$ vector satisfies $G \cdot 0 = 0 \geq 0$, and the relaxation is the convex hull of integer solutions. Pick the unique optimal vertex $x^*_{LP} \in \mathbb{R}_{\geq 0}^N$ closest to an integer point.*

*The **violated constraint** is:*

$$
  \gamma^*(K, q)
  \;:=\;
  \arg\min_\gamma\;
    (\mathrm{G}(q)\, \lceil x^*_{LP} \rceil)_\gamma,
$$

*which is the constraint with the smallest (most negative) Frobenius positivity value at the rounded integer point. By LP duality ([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)), this corresponds to a unique partition $\lambda^*(K, q)$. This is the operator $e_{\lambda^*}$ that fails to satisfy positivity.*

*Uniqueness: if two distinct partitions $\lambda_1, \lambda_2$ both achieve the minimum at the same integer point, they have identical shadow prices at $q$. That is, $|y_{\lambda_1}(q)| = |y_{\lambda_2}(q)|$. These lie on the **boundary variety** ([local shadow ordering](#def:local-shadow-ordering)) of measure zero. Generically (off the boundary variety), $\lambda^*$ is unique.* $\square$

**Connection to phase boundary.**
*An atom that is stable at $q_1$ and unstable at $q_2$ necessarily crosses a $q^* \in [q_1, q_2]$ where $E(\lambda^*, q^*) = |y_{\lambda^*}(q^*)| = 0$. The LP boundary for the violated constraint vanishes. Crossing $q^*$ flips ILP feasibility.*
