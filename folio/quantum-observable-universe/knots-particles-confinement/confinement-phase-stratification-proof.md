*Proof.*
*Claim (1)—Openness.*
*Slater-strict feasibility of an SDP is preserved under small perturbations of the defining data (Boyd–Vandenberghe Lemma 5.4.1). If $\Phi_0 \succ 0$ is strictly feasible at $q_0$, then for every $q$ in a neighbourhood of $q_0$, the same $\Phi_0$ remains strictly feasible due to the continuity of the SDP constraint matrices in $q$. Hence, $\Omega(P)$ is a union of open neighbourhoods and is therefore open.*

*Claim (2)—Stratification.*
*The complement $\mathcal{G} \setminus \Omega(P)$ is defined by the vanishing of a finite product of principal-minor determinants of the Gram matrix $\mathrm{G}(q)$. Each determinant is a polynomial in $q$ with finitely many real zeros in $\mathcal{G}$. The union of these zero sets forms a real-algebraic stratification. Generic strata have codimension 1 (single-minor vanishing), while lower strata appear at simultaneous vanishings.*

*Claim (3)—Local constancy.*
*On each component $\Omega_\alpha$, the active support $\mathcal{S}^*(P, q)$ is determined by the sign pattern of the complementary-slackness dual variables $u_\lambda^*(q)$. By the continuity of the SDP optimiser in $q$ (generic uniqueness from Slater strictness, [Boyd–Vandenberghe §5.5.3](https://doi.org/10.1017/CBO9780511804441)) and the integer-valuedness of $|\mathcal{S}^*|$, the set $\mathcal{S}^*(P, q)$ cannot change within $\Omega_\alpha$. Any change requires some $u_\lambda^*$ to pass through zero, which precisely defines the phase-boundary condition. Continuity of $\sigma_F$ follows directly from the continuity of the SDP optimal value under Slater regularity.*

*Claim (4)—Scope.*
*The proofs of [coarsest-level Markov sufficiency](#prop:level-sufficiency) (Markov-inclusion + active-support preservation) and [shell-closure stability](#prop:shell-closure-stability) (SDP-relaxation monotonicity + multi-block tightness) both assume the active support is well-defined and locally constant (i.e., $q \in \Omega_\alpha$). If any of the three properties in Claim (3) fails on $\partial\Omega(P)$, it invalidates the corresponding proof. Therefore, the scope is strictly confined to the open stratum.*

*Claim (5)—Phase transitions.*
*A boundary crossing at $q_0$ represents either a Slater-loss event (primal strict PSD feasibility breaks $\to$ deconfinement) or an active-support transition (some $u_\lambda^*$ passes through zero $\to$ regime switch with $\mu$-jump). Both correspond precisely to the discrete-regime-switch phenomenology documented in [parity regime selection](#thm:parity-regime-selection) and the [deconfinement golden threshold](#rem:deconfinement-golden-threshold). $\square$*

**Corollary (phase-scoped applicability).**
*The scope of any theorem, proposition, or definition in the confinement framework referencing [confined particle definition](#def:confined-particle), [confinement category](#def:confinement-category), [confinement semidefinite program](#prop:confinement-sdp), [coarsest-level Markov sufficiency](#prop:level-sufficiency), electron-shell attachment, [dressed particle definition](#def:dressed-particle), or [shell-closure stability](#prop:shell-closure-stability) is implicitly restricted to "for all $q \in \Omega_\alpha(P)$, some fixed confinement phase of $P$". Statements that must hold across phase boundaries (e.g., phase-transition signatures, critical exponents, scaling laws) require explicit boundary analysis; within-phase theorems do not cover them.*
