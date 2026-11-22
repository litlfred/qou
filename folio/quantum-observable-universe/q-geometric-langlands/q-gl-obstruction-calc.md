Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\chi(A) \neq 0$ and obstruction class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ ([quantum characteristic classes](#def:quantum-characteristic-classes)). Assume:

- **(H-HKR)** the Hochschild--Kostant--Rosenberg comparison identifies the space of intrinsic $q$-curvatures $HH^2(\mathcal{U}_q, \mathrm{Ad})$ with $H^2(\mathcal{S}, \mathbb{G}_m)$, by an isomorphism $\Theta$ sending the intrinsic curvature to $\kappa_0$;
- **(H-tr)** the trace $\mathrm{tr} \colon H^2(\mathcal{S}, \mathbb{G}_m) \to \mathbb{Z}$ is an isomorphism, with $\mathrm{tr}(\kappa_0) = \chi(A)$.

Then:

1. The **intrinsic $q$-curvature** $\mathcal{F}_q^{\mathrm{intr}} = \Theta^{-1}(\kappa_0) \in HH^2(\mathcal{U}_q, \mathrm{Ad})$ is non-zero whenever $\kappa_0 \neq 0$.
2. A $q$-connection $\nabla_q$ is $q$-flat ([q-flat connection](#def:q-flat-connection)) when its connection-dependent curvature $\mathcal{F}_q^{\mathrm{conn}}$ vanishes. This condition does not involve $\kappa_0$, so $q$-flat connections can exist when $\kappa_0 \neq 0$; they then carry the intrinsic curvature of item 1. Lifting a $q$-flat connection through the brane tower to level $n$ requires $\kappa_0 \equiv 0 \pmod n$, that is, $\kappa_0 \in n\,H^2(\mathcal{S}, \mathbb{G}_m)$.
3. At Kummer level $n$, the class $\kappa_0 \bmod n \in H^2(\mathcal{S}, \mathbb{G}_m)/n$ vanishes if and only if $n \mid \chi(A)$. Thus $q$-flat $G_q$-connections lift to level $n$ only when $n$ divides $|\chi(A)|$.
4. For $\chi(A) \neq 0$, the condition $\kappa_0 \not\equiv 0 \pmod n$ holds at a density-$1$ set of Kummer levels $n \in \mathbb{Z}_{>0}$; this is the perpetual obstruction. The $q$-local systems exist as objects with intrinsic curvature, but their brane tower lifts are obstructed at cofinitely many levels.

The reduction is taken in $H^2(\mathcal{S}, \mathbb{G}_m)/n$, not in $H^2(\mathcal{S}, \mu_n)$: the Kummer sequence embeds $H^2(\mathcal{S}, \mathbb{G}_m)/n$ in $H^3(\mathcal{S}, \mu_n)$.
