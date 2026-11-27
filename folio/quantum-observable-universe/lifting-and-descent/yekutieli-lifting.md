Let $(\mathbf{C}, A, \tau)$ be a [quantum observable universe](#def:quantum-observable-universe). Let $\{A_n\}_{n \geq 0}$ be the [recursive brane tower](#def:recursive-brane-tower). The [jet prolongation](#prop:jet-prolongation) produces central extensions of gerbes:
$$
  1  \longrightarrow  \mathcal{B}
   \longrightarrow  \mathfrak{G}_{n+1}
   \longrightarrow  \mathfrak{G}_n
   \longrightarrow  1.
$$
These extensions satisfy the [Quantum lifting condition](#def:yekutieli-lifting-condition). In the archimedean realisation, $\mathcal{B} = \mathcal{O}_M^{\times}$. The lift of the Frobenius--Hopf object from level $n$ to level $n{+}1$ exists if and only if the [quantum characteristic class](#def:quantum-characteristic-classes) obstruction $\kappa_n \in H^2(M, \mathcal{B})$ vanishes.

When $M$ is a closed surface (for example Bring's surface), this archimedean band carries no obstruction. The exponential sequence gives $H^2(M, \mathcal{O}_M^{\times}) \cong H^3(M, \mathbb{Z}) = 0$, since $H^2(M, \mathcal{O}_M) = 0$ in both the holomorphic and the smooth setting. So every $\kappa_n$ vanishes there. A non-vanishing obstruction on a surface requires a different band, such as $\mathbb{Z}$ or $\mathbb{Z}/2$.

**Formalisation status.** The group-level case is proved, not assumed. *Proposition (Lean: `QOU.YekutieliLifting.lift_iff`).* For a tower of central group extensions $1 \to A_n \to E_n \to G_n \to 1$ and homomorphisms $\varphi_n \colon H_n \to G_n$, $\varphi_n$ lifts to $E_n$ if and only if its obstruction class $\kappa(\varphi_n) \in H^2(H_n, A_n)$ vanishes. *Proof.* This is the class-form criterion of the [Quantum lifting condition](#def:yekutieli-lifting-condition) at level $n$: the obstruction cocycle is a coboundary exactly when a lift exists. $\square$ *Proposition (Lean: `QOU.YekutieliLifting.perpetual_obstruction`, `no_lift_of_persistent`).* If $\kappa_0 \neq 0$ and $\kappa_n \neq 0$ implies $\kappa_{n+1} \neq 0$ for every $n$, then $\kappa_n \neq 0$ for every $n$, and no level lifts. *Proof.* Induction on $n$, then the criterion above. $\square$ Persistence is a hypothesis here, not a property of the tower. The gerbe-level statement over a site (Steps 1 to 3 of the proof below) is not yet formalised.
