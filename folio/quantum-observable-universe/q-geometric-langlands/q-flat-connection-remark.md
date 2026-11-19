A $q$-flat connection carries the *minimal possible curvature* compatible with the $q$-deformation: curvature arising solely from the perpetual $d_q^2$ obstruction rather than from any connection form. It is *not* flat in the classical sense ($\nabla_q^2 \neq 0$ in general). When $\kappa_0 \neq 0$ (the perpetual obstruction), $q$-flat connections exist but have non-zero total curvature $(q-1)\mathcal{F}_q^{\mathrm{intr}}$.

The condition $\nabla^2 = 0$ provides the geometric incarnation of $d^2 = 0$. The $q$-flatness equation $\nabla_q^2 = (q-1)\mathcal{F}_q^{\mathrm{intr}}$ absorbs the canonical obstruction to flatness. The Hochschild--Kostant--Rosenberg comparison ([Kummer filtration](#rem:kummer-filtration-obstruction)) identifies the $q$-curvature $\mathcal{F}_q^{\mathrm{intr}}$ with the gerbe-theoretic obstruction class $\kappa_0 = e(\xi)$ in $H^2(\mathcal{S}, \mathbb{G}_m)$. The Kummer filtration pulls back to a filtration on $HH^2$ that measures the $n$-divisibility of the $q$-curvature.

**The HKR identification.**
The Hochschild--Kostant--Rosenberg comparison
([Kummer filtration](#rem:kummer-filtration-obstruction))
identifies the $q$-curvature $\mathcal{F}_q$ with the obstruction
class $\kappa_0 = e(\xi)$ in
$H^2(\mathcal{S}, \mathbb{G}_m)$.  The deformation-theoretic
obstruction $HH^2$ and the gerbe class in
$H^2(\mathcal{S}, \mathbb{G}_m)$ are two views of the same class.
The Kummer filtration on the target pulls back to a filtration on
$HH^2$ measuring $n$-divisibility of the $q$-curvature.

**The perpetual obstruction and Hecke commutativity.**
From the Hecke perspective, the $q$-curvature $\mathcal{F}_q$
is the categorical shadow of the non-commutativity of Hecke
operators at different places: classically Hecke operators at
distinct points commute, but the $q$-deformation introduces
$(q-1)$-proportional commutators.  The perpetual obstruction
([Kummer filtration](#rem:kummer-filtration-obstruction))
ensures this non-commutativity persists at cofinitely many
Kummer levels.

**Classical limit, curvature decomposition and $q$-local systems.**
In the classical limit $q \to 1$, the prefactor $(q - 1)$
vanishes, so the intrinsic term drops out and $q$-flatness reduces to
ordinary flatness ($\nabla_q^2 = 0$); the residual curvature is present
only when $q \neq 1$.

In general, a $q$-connection has total curvature

$$
  \nabla_q^2 = (q - 1)\mathcal{F}_q^{\mathrm{intr}}
  + \mathcal{F}_q^{\mathrm{conn}},
$$

where $\mathcal{F}_q^{\mathrm{conn}}$ is the
*connection-dependent curvature* — the contribution from the
connection form itself.  A $q$-connection is $q$-flat when
$\mathcal{F}_q^{\mathrm{conn}} = 0$: all curvature is intrinsic,
arising solely from the $d_q^2 \neq 0$ obstruction
([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)).

The category of $q$-flat connections on $X$ with structure group
$G_q$ is equivalent to the category of $q$-local systems
$\mathrm{LocSys}_{G_q}(X)$
([q-local system](#def:q-local-system)).
