**Independence of neighborhood.**
*Stability is a **fixed-$q$** property. It does not require the ILP to be feasible on a neighborhood of $q$. An atom may be stable at $q_0$ and unstable at $q_0 + \epsilon$ without contradiction. Stability tracks ILP-feasibility pointwise.*

**Connection to LP-feasibility.**
*The continuous LP relaxation ($x \in \mathbb{R}_{\geq 0}^N$, $\mathrm{G}(q) x \geq 0$) is always feasible, since the trivial identity normal form $T_e = e_{(k)}$ has $y_{(k)} = 0$. The ILP version is strictly stronger. The proton derivation in [mass-endomorphism-tower](#prop:mass-endomorphism-tower) shows that the $9$-crossing element $\mathcal{B}_3 \times \Delta_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ violates Frobenius positivity (it is LP-infeasible at integer values). An ILP search adjoining $\{\sigma_0, \sigma_1, L_+, L_-\}$ finds the unique integer solution $\sigma_0 \to \sigma_0$ ($2$ gluon crossings) that restores stability.*

**Confined operators only.**
*We solve the ILP within the confinement filtration ([confinement level](#def:confinement-level)) at $q$. We only consider primitives $e_\lambda$ in $J^{\ell(K, q)}(q)$, since operators above the atom's confinement level are unavailable without further phase transitions.*

**Scope of the stability condition.** For a [stable atom](#def:stable-atom), the Frobenius positivity constraint $(\mathrm{G}x)_\gamma \geq 0$ holds for every primitive constraint $\gamma$ at the coefficient vector of $T_w$ itself. The condition is evaluated at the vector $x(K, q)$ fixed by the decomposition of $T_w$, not at an arbitrary vector. The existential form $\exists\, x \in \mathbb{Z}_{\geq 0}^N$ with $\mathrm{G}(q)\,x \geq 0$ holds for every atom, since $x = 0$ satisfies it, and therefore does not distinguish stable from unstable atoms.
