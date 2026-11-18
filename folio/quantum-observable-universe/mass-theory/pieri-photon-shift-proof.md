**Proof.**
For a partition $\mu \vdash m + 1$, write $\rho_\mu$ for its seminormal representation, a matrix on the standard Young tableaux of shape $\mu$. Group these tableaux by the cell that holds the largest entry $m + 1$. That cell is always a removable corner $c$ of $\mu$, and the tableaux with $m + 1$ at $c$ correspond one-to-one to the standard tableaux of $\mu \setminus c$.

*Part 1.* $\rho_\mu(a\beta_m) = \rho_\mu(a)\,\rho_\mu(\beta_m)$, and the second factor is zero for $\mu \neq \lambda$.

*Part 2.* Since $\rho_\mu(\gamma\beta_m) = \rho_\mu(\gamma)\,\rho_\mu(\beta_m)$, it suffices to show $\rho_\mu(\beta_m) = 0$ whenever $\mu$ is not $\lambda$ plus a box.

- The image of $H_m(q)$ does not mix the groups. Its generators $\sigma_1, \dots, \sigma_{m-1}$ leave the position of the entry $m + 1$ fixed, so every $\rho_\mu(x)$ with $x \in H_m(q)$ has zero entries between tableaux in different groups.
- On the group of a corner $c$, $\rho_\mu(x)$ is exactly $\rho_{\mu \setminus c}(x)$. This is the branching rule for the seminormal representations: it holds on generators by inspecting the seminormal matrix entries, and it extends to all of $H_m(q)$ because restriction to a group is multiplicative on group-preserving matrices.

If $\mu$ is not $\lambda$ plus a box, then $\mu \setminus c \neq \lambda$ for every corner $c$. So every diagonal group of $\rho_\mu(\beta_m)$ is $\rho_{\mu \setminus c}(\beta_m) = 0$, every off-diagonal group is zero by the first point, and $\rho_\mu(\beta_m) = 0$. $\blacksquare$

**Scope.**
This is a containment of supports, not an equality. Which of the partitions $\lambda + \square$ actually occur, and with what coefficients, depends on $\gamma$; none is computed here.

**Relation to the volume vanishing.** The [degree-one volume lemma](#lem:degree-one-braid-trivial-volume) says every braid word in the support of a degree-one element has volume $0$. The Pieri shift is the representation-theoretic counterpart: it tracks how such an element moves the Wedderburn support, independent of the archimedean volume.
