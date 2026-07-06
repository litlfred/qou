Any $q$-deformation of Geometric Langlands must reduce to the
classical Beilinson–Drinfeld equivalence $\mathbb{L}_{\mathrm{BD}}$ at
$q = 1$; this consistency check the $q$-correspondence passes, and it
does so through three compatible limits of its defining data
(differential, Hecke, and dual-group).  Accordingly, as $q \to 1$ in
the $\mathbb{G}_m$-family, the $q$-Geometric Langlands correspondence
recovers the classical Geometric Langlands equivalence:

$$
  \lim_{q \to 1} \mathbb{L}_q =  \mathbb{L}_{\mathrm{BD}}
  \colon \mathcal{D}\text{-}\mathrm{mod}(\mathrm{Bun}_G(X))
  \xrightarrow{ \sim }
  \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}}(X)).
$$

The degeneration proceeds through three compatible limits:

1. **Differential limit**: $d_q \to d$ and $d_q^2 \to 0$
   ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)),
   so $q$-flat connections become flat connections and $q$-local
   systems become classical local systems.

2. **Hecke limit**: the Hecke relation
   $(T-q)(T+q^{-1}) = 0$ degenerates to $(T-1)(T+1) = 0$, recovering
   the symmetric group action.  The $q$-Hecke operators become
   classical Hecke correspondences.

3. **Dual group limit**: $\check{G}_q = G_{q^{-1}}^\vee \to
   G^\vee = \check{G}$ as the quantum deformation is removed.
