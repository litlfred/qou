<!-- FILE_START: q-local-systems-intro.md -->
We establish the automorphic-side geometry upon which the $q$-Hecke correspondences act. We define $q$-local systems on a brane curve $X$ and the $q$-flat connections that supply their $q$-holonomy residues.
<!-- FILE_END: q-local-systems-intro.md -->

<!-- FILE_START: q-local-system.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ ([substrate parameter](#def:substrate-parameter)), and let $X$ be a brane curve. A **$q$-local system** on $X$ with structure group $G_q$ is a functor

$$
  \mathcal{L}_q \colon \Pi_1(X) \longrightarrow \mathbf{Rep}(G_q)
$$

from the fundamental groupoid $\Pi_1(X)$ to the category of finite-dimensional representations of $G_q$. This functor must satisfy the **$q$-monodromy condition**: for every contractible loop $\varrho \colon \mathbf{1} \to \mathbf{1}$ in $\Pi_1(X)$, the monodromy obeys

$$
  \mathcal{L}_q(\varrho) = \mathrm{id} + (q - 1)\Omega_q(\varrho),
$$

where $\Omega_q(\varrho) \in \mathrm{End}(\tau(\mathcal{L}_q))$ is the **$q$-holonomy residue** determined by the underlying $q$-connection ([q-flat connection](#def:q-flat-connection)).

The $q$-monodromy condition reflects the local geometry of the $\mathbb{G}_m$-family. At $q = 1$, the residue vanishes and $\mathcal{L}_1$ reduces to a classical flat bundle. For $q \neq 1$, the non-vanishing curvature $d_q^2 \neq 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)) obstructs trivial monodromy. The Kummer reduction of the obstruction class $\kappa_0$ at level $n$ ([Kummer filtration](#rem:kummer-filtration-obstruction)) controls lifting through the brane tower. A $q$-local system $\mathcal{L}_q$ lifts from level $n$ to $n+1$ if and only if $\kappa_0 \equiv 0 \pmod n$, which occurs precisely when $n \mid \chi(A)$. We denote the moduli stack of $q$-local systems on $X$ by $\mathrm{LocSys}_{G_q}(X)$.
<!-- FILE_END: q-local-system.md -->

<!-- FILE_START: q-local-system-remark.md -->
Classical local systems correspond to representations of $\pi_1(X)$ because their connections satisfy $d^2 = 0$. In a quantum observable universe, the perpetual curvature $d_q^2 \neq 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)) obstructs naive flatness. The $q$-monodromy condition absorbs this obstruction. For contractible loops, parallel transport deviates from the identity by a residue proportional to $(q-1)$. 

The Kummer filtration measures this deviation at finite levels. An obstruction class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ vanishes modulo $n$ precisely when $n \mid \chi(A)$ ([Kummer filtration](#rem:kummer-filtration-obstruction)). At these levels, the $q$-monodromy becomes $n$-divisible, determining a sublocus of $\mathrm{LocSys}_{G_q}(X)$ with enhanced lifting properties through the brane tower. When $n \nmid \chi(A)$, the obstruction forces a non-trivial $q$-holonomy residue on every $q$-local system. This behavior mirrors the Hecke relation $(T - q)(T + q^{-1}) = 0$, where the symmetric group relation $(T-1)(T+1) = 0$ deforms to split braiding eigenvalues from $\pm 1$ to $q$ and $-q^{-1}$.
<!-- FILE_END: q-local-system-remark.md -->

<!-- FILE_START: q-flat-connection.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe and let $\mathcal{V}$ be a $G_q$-equivariant object in $\mathbf{C}$ over the brane curve $X$. A **$q$-flat connection** on $\mathcal{V}$ is a $q$-connection $\nabla_q \colon \mathcal{V} \to \Omega^1_q \otimes \mathcal{V}$ ([categorical $q$-connection](#def:categorical-q-connection)) whose total curvature equals the intrinsic $q$-curvature dictated by $d_q^2$:

$$
  \nabla_q^2 = (q - 1)\mathcal{F}_q^{\mathrm{intr}}.
$$

Here, $\mathcal{F}_q^{\mathrm{intr}} \in \mathrm{End}(\mathcal{V}) \otimes \Omega^2_q$ is the **intrinsic $q$-curvature**, defined as the image of the obstruction class $\kappa_0$ under the Hochschild--Kostant--Rosenberg map ([Kummer filtration](#rem:kummer-filtration-obstruction)):

$$
  \mathcal{F}_q^{\mathrm{intr}}
  = 
  \mathrm{HKR}^{-1}(\kappa_0)
   \in 
  HH^2(\mathcal{U}_q, \mathrm{Ad}).
$$

In general, a $q$-connection has total curvature $\nabla_q^2 = (q - 1)\mathcal{F}_q^{\mathrm{intr}} + \mathcal{F}_q^{\mathrm{conn}}$, where $\mathcal{F}_q^{\mathrm{conn}}$ is the connection-dependent curvature. A connection is $q$-flat when $\mathcal{F}_q^{\mathrm{conn}} = 0$. In this state, all curvature is intrinsic and arises solely from the $d_q^2 \neq 0$ obstruction ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)). A $q$-flat connection minimizes curvature rather than vanishing it. The category of $q$-flat connections on $X$ with structure group $G_q$ is equivalent to the category of $q$-local systems $\mathrm{LocSys}_{G_q}(X)$ ([q-local system](#def:q-local-system)).
<!-- FILE_END: q-flat-connection.md -->

<!-- FILE_START: q-flat-connection-remark.md -->
The condition $\nabla^2 = 0$ provides the geometric incarnation of $d^2 = 0$. The $q$-flatness equation $\nabla_q^2 = (q-1)\mathcal{F}_q^{\mathrm{intr}}$ absorbs the canonical obstruction to flatness. The Hochschild--Kostant--Rosenberg comparison ([Kummer filtration](#rem:kummer-filtration-obstruction)) identifies the $q$-curvature $\mathcal{F}_q^{\mathrm{intr}}$ with the gerbe-theoretic obstruction class $\kappa_0 = e(\xi)$ in $H^2(\mathcal{S}, \mathbb{G}_m)$. The Kummer filtration pulls back to a filtration on $HH^2$ that measures the $n$-divisibility of the $q$-curvature.

From the Hecke perspective, the $q$-curvature $\mathcal{F}_q^{\mathrm{intr}}$ is the categorical shadow of Hecke operators failing to commute at different places. Classically, Hecke operators at distinct points commute. The $q$-deformation introduces commutators proportional to $(q-1)$. The perpetual obstruction ensures this non-commutativity persists at cofinitely many Kummer levels.
<!-- FILE_END: q-flat-connection-remark.md -->
