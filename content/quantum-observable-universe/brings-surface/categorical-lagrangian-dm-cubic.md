**Conjecture (open; conditional structural chain).** Let $F$ be the $q$-Lagrangian fibration of the Bring hyperkähler cone, with $q$-period matrix $\tau_{ij}$ and period-map differential $\partial_k \tau_{ij}$. The **Donagi--Markman cubic condition** — a family of abelian varieties admits a Lagrangian (algebraically completely integrable Hamiltonian system) structure iff there is a field of totally-symmetric cubics $c_{ijk} \in \mathrm{Sym}^3 T^*B$ with $\partial_k \tau_{ij} = c_{ijk}$ — applied to $F$ yields a $q$-cubic $c$ on the base whose leading self-contraction is the binding kernel $C_1$:

$$
  c_{ddd} = \kappa \neq 0,
  \qquad
  \kappa = \mathrm{recurrenceKernelLead},
$$

the nonzero top-shift weight of the proved depth-$2$ kernel $[n+2]_q\, b_{n+2} = b_{n+1} + b_n$. If this identity is *derived* (not fitted), it gives $C_1$ an **independent geometric origin** and de-tautologizes the QDM-3 symbol identity.

## Motivation and scope

The QDM-3 result `symbol D_q = recurrenceKernelLead κ` is an honest **tautological re-encoding**: the recurrence operator $D_q$ is *defined from* the $C_1$ recurrence and $\mathrm{recurrenceKernelLead}$ is *defined as* its leading term, so the symbol match holds by construction. It does **not** supply a geometric origin for $C_1$. The route conjectured here builds the cubic / period datum *independently* from the Bring hyperkähler geometry (via the Donagi--Markman cubic condition) and only *then* matches it to the kernel — the match being the genuine open wall.

The load-bearing geometric structure is the holomorphic-symplectic $2$-form $\Omega_{\mathbb{C}}$, **not** the tetraplectic $4$-form: on the real-$4$-dimensional Bring cone the $4$-form degenerates to a volume form ($m = 1$) and carries no fibration data. Its existence is signalled by the $3$-Sasakian boundary and the Reeb quaternionic twist $[M_i, M_j] = 2 M_k$. The on-shell categorical-Lagrangian wavefront $\mathcal{D}_\nabla \psi = 0$ is Lagrangian with respect to $\Omega_{\mathbb{C}}$.

## The structural chain

The chain is formalized (formalize-first, generic base ring) in `QOU.Brings.CategoricalLagrangianDMCubic` as content-bearing conjecture carriers:

1. **$q$-Donagi--Markman cubic condition** (primary conjecture, no instance): there is a totally-symmetric cubic $c$ with $\partial_k \tau_{ij} = c_{ijk}$ — the non-automatic total symmetry equivalent to the fibration being Lagrangian.
2. **Bring holomorphic-symplectic $2$-form** (primary conjecture, no instance): $\Omega_{\mathbb{C}}$ is non-degenerate and the wavefront $\mathcal{D}_\nabla \psi = 0$ is Lagrangian (isotropic and half-dimensional).
3. **DM cubic of the Bring fibration** (conditional theorem, proved sorry-free modulo 1 and 2): the cubic condition applied to $F$ yields a $q$-cubic that reproduces the period differential and is fully $S_3$-symmetric, with the wavefront isotropic for $\Omega_{\mathbb{C}}$.
4. **$q$-cubic $=$ binding kernel $C_1$** (dependent target conjecture, no instance): the open identity $c_{ddd} = \kappa \neq 0$. This is the keystone step; it is not proved.

This block **scaffolds** the route — it narrows the search by stating each claim honestly — and does **not** close the keystone. The identity $c = C_1$ must be *derived*, never fitted.
