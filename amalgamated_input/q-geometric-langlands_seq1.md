<!-- FILE_START: q-local-systems-intro.md -->
We establish the automorphic-side geometry upon which the $q$-Hecke correspondences will act. We define $q$-local systems on a brane curve $X$ and the $q$-flat connections that supply their $q$-holonomy residues. Two interpretive remarks track the quantum deformation. Remark: From monodromy to $q$-monodromy casts the $q$-monodromy condition as a $\mathbb{G}_m$-family of holonomies degenerating to the classical case at $q = 1$. Remark: The $d_q^2 \neq 0$ obstruction as curvature interprets the failure of $d_q^2 = 0$ as the curvature class obstructing exact $q$-flatness. This fixes the moduli of $q$-local systems and their flat sections.

_(draft.)_
<!-- FILE_END: q-local-systems-intro.md -->

<!-- FILE_START: q-local-system.md -->
We define local systems on a brane curve to incorporate the perpetual curvature of a quantum observable universe. Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$, and let $X$ be the brane curve. The parameter $q$ selects a fibre in the $\mathbb{G}_m$-family of deformations ([substrate parameter](#def:substrate-parameter)).

A **$q$-local system** on $X$ with structure group $G_q$ is a functor

$$
  \mathcal{L}_q \colon \Pi_1(X) \longrightarrow \mathbf{Rep}(G_q)
$$

from the fundamental groupoid $\Pi_1(X)$ to the category of finite-dimensional representations of the quantum group $G_q$. This functor must satisfy the **$q$-monodromy condition**: for every contractible loop $\varrho \colon \mathbf{1} \to \mathbf{1}$ in $\Pi_1(X)$, the monodromy obeys

$$
  \mathcal{L}_q(\varrho) = \mathrm{id} + (q - 1)\Omega_q(\varrho),
$$

where $\Omega_q(\varrho) \in \mathrm{End}(\tau(\mathcal{L}_q))$ is the **$q$-holonomy residue** determined by the $q$-connection ([q-flat connection](#def:q-flat-connection)).

The $q$-monodromy condition captures the local geometry of the $\mathbb{G}_m$-family. At $q = 1$, the residue vanishes and $\mathcal{L}_1$ becomes a classical flat bundle. For $q \neq 1$, the non-vanishing curvature $d_q^2 \neq 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)) obstructs trivial monodromy. The Kummer reduction of the obstruction class $\kappa_0$ at level $n$ ([Kummer filtration](#rem:kummer-filtration-obstruction)) controls lifting through the brane tower. A $q$-local system $\mathcal{L}_q$ lifts from level $n$ to $n+1$ if and only if $\kappa_0 \bmod n = 0$, which is equivalent to $n \mid \chi(A)$.

We denote the moduli stack of $q$-local systems on $X$ by $\mathrm{LocSys}_{G_q}(X)$.
<!-- FILE_END: q-local-system.md -->

<!-- FILE_START: q-local-system-remark.md -->
Classical local systems on $X$ correspond to representations of $\pi_1(X)$ because the connection satisfies $d^2 = 0$. In a quantum observable universe, the $q$-deformed exterior derivative satisfies $d_q^2 \neq 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)). This perpetual curvature obstructs naive flatness. We therefore replace flatness with the $q$-monodromy condition. For contractible loops, parallel transport deviates from the identity by a residue proportional to $(q-1)$. This deviation vanishes in the classical limit $q \to 1$.

The Kummer filtration measures this obstruction at finite levels. An obstruction class $\kappa_0 = e(\xi) \in H^2(\mathcal{S}, \mathbb{G}_m)$ vanishes modulo $n$ precisely when $n \mid \chi(A)$ ([Kummer filtration](#rem:kummer-filtration-obstruction)). At these levels, the $q$-monodromy is $n$-divisible. This determines a sublocus of $\mathrm{LocSys}_{G_q}(X)$ with enhanced lifting properties through the brane tower. When $n \nmid \chi(A)$, the obstruction forces a non-trivial $q$-holonomy residue on every $q$-local system.

This behavior parallels the Hecke algebra. The Hecke relation $(T - q)(T + q^{-1}) = 0$ deforms the symmetric group relation $(T-1)(T+1) = 0$. Just as braiding eigenvalues split from $\pm 1$ to $q$ and $-q^{-1}$, the monodromy of contractible loops splits from trivial to $q$-parametrised.
<!-- FILE_END: q-local-system-remark.md -->

<!-- FILE_START: q-flat-connection.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe and let $\mathcal{V}$ be a $G_q$-equivariant object in $\mathbf{C}$ over the brane curve $X$. We define a **$q$-flat connection** on $\mathcal{V}$ as a $q$-connection $\nabla_q \colon \mathcal{V} \to \Omega^1_q \otimes \mathcal{V}$ ([categorical $q$-connection](#def:categorical-q-connection)) whose total curvature $\nabla_q^2$ equals the intrinsic $q$-curvature dictated by $d_q^2$:

$$
  \nabla_q^2 = (q - 1)\mathcal{F}_q^{\mathrm{intr}},
$$

where $\mathcal{F}_q^{\mathrm{intr}} \in \mathrm{End}(\mathcal{V}) \otimes \Omega^2_q$ is the **intrinsic $q$-curvature**. This is the image of the obstruction class $\kappa_0$ under the HKR map ([Kummer filtration](#rem:kummer-filtration-obstruction)):

$$
  \mathcal{F}_q^{\mathrm{intr}}
  = 
  \mathrm{HKR}^{-1}(\kappa_0)
   \in 
  HH^2(\mathcal{U}_q, \mathrm{Ad}).
$$

In general, a $q$-connection possesses the total curvature

$$
  \nabla_q^2 = (q - 1)\mathcal{F}_q^{\mathrm{intr}}
  + \mathcal{F}_q^{\mathrm{conn}},
$$

where $\mathcal{F}_q^{\mathrm{conn}}$ is the **connection-dependent curvature** contributed by the connection form itself. A $q$-connection is **$q$-flat** when $\mathcal{F}_q^{\mathrm{conn}} = 0$: all curvature is intrinsic, arising solely from the $d_q^2 \neq 0$ obstruction ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)).

A $q$-flat connection is not flat in the classical sense ($\nabla_q^2 \neq 0$ generally), but carries the minimal possible curvature compatible with the $q$-deformation. When $\kappa_0 \neq 0$ (the perpetual obstruction), $q$-flat connections exist but maintain non-zero total curvature $(q-1)\mathcal{F}_q^{\mathrm{intr}}$.

The category of $q$-flat connections on $X$ with structure group $G_q$ is equivalent to the category of $q$-local systems $\mathrm{LocSys}_{G_q}(X)$ ([q-local system](#def:q-local-system)).
<!-- FILE_END: q-flat-connection.md -->

<!-- FILE_START: q-flat-connection-remark.md -->
**The classical flatness condition and its $q$-deformation.**
The condition $\nabla^2 = 0$ provides the geometric incarnation of $d^2 = 0$. In our framework, $d_q^2 \neq 0$ introduces a canonical obstruction to flatness proportional to $(q-1)$. The $q$-flatness equation $\nabla_q^2 = (q-1)\mathcal{F}_q$ absorbs this obstruction: a $q$-flat connection is not flat, but carries the minimal curvature compatible with the $q$-deformation.

**The HKR identification.**
The Hochschild--Kostant--Rosenberg comparison ([Kummer filtration](#rem:kummer-filtration-obstruction)) identifies the $q$-curvature $\mathcal{F}_q$ with the obstruction class $\kappa_0 = e(\xi)$ in $H^2(\mathcal{S}, \mathbb{G}_m)$. The deformation-theoretic obstruction (Hochschild $HH^2$) and the gerbe-theoretic obstruction (gerbe-theoretic $H^2$) represent two views of the same class. The Kummer filtration on the target pulls back to a filtration on $HH^2$ measuring the $n$-divisibility of the $q$-curvature.

**The perpetual obstruction and Hecke commutativity.**
From the Hecke perspective, the $q$-curvature $\mathcal{F}_q$ serves as the categorical shadow of the non-commutativity of Hecke operators at different places. Classically, Hecke operators at distinct points commute, but the $q$-deformation introduces $(q-1)$-proportional commutators. The perpetual obstruction ([Kummer filtration](#rem:kummer-filtration-obstruction)) ensures this non-commutativity persists at cofinitely many Kummer levels.
<!-- FILE_END: q-flat-connection-remark.md -->

