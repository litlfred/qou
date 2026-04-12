Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\chi(A) \neq 0$ and Yekutieli class
$\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$
([quantum characteristic classes](#def:quantum-characteristic-classes)).

1. The **intrinsic $q$-curvature** of any $q$-flat connection
   $\nabla_q$ on a $G_q$-bundle over $X$ is

   $$
     \mathcal{F}_q^{\mathrm{intr}}
     = 
     \mathrm{HKR}^{-1}(\kappa_0)
      \in 
     HH^2(\mathcal{U}_q, \mathrm{Ad}),
   $$

   where $\mathrm{HKR}$ is the Hochschild--Kostant--Rosenberg
   comparison
   ([Kummer filtration](#rem:kummer-filtration-obstruction)).
   This curvature is non-zero whenever $\kappa_0 \neq 0$:
   $q$-flat connections carry intrinsic curvature from $d_q^2 \neq 0$.

2. The $q$-connection $\nabla_q$ is $q$-flat
   ([q-flat connection](#def:q-flat-connection)) — meaning its
   connection-dependent curvature
   $\mathcal{F}_q^{\mathrm{conn}} = 0$ — regardless of whether
   $\kappa_0$ vanishes.  However, $q$-flat connections that
   **lift through the brane tower** require $\kappa_0 \bmod n = 0$
   at the target level.

3. At Kummer level $n$, the obstruction $\kappa_0 \bmod n$
   vanishes if and only if $n \mid \chi(A)$.  Consequently,
   $q$-flat $G_q$-connections that lift to level $n$ of the
   brane tower exist only when $n$ divides $|\chi(A)|$.

4. For $\chi(A) \neq 0$, the set of Kummer levels $n$ at which
   $\kappa_0 \bmod n \neq 0$ has density $1$ in
   $\mathbb{Z}_{>0}$: the obstruction **persists perpetually**.
   The $q$-local systems exist (as objects with intrinsic
   curvature), but their brane tower lifts are obstructed at
   cofinitely many levels.
