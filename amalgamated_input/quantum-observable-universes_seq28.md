<!-- FILE_START: dq-squared-elaboration-intro.md -->
The categorical $d_q^2$ obstruction was computed in
the earlier core development; we now specialise it to a
concrete manifold $M$ and explore the parallel failure of the
Jacobi identity for the $q$-deformed Lie bracket.
Proposition: Archimedean $d_q^2$, with its proof, computes
$d_q^2 \alpha = q^{-1}(1 - q^{-1})\,d\varTheta \wedge
\mathcal{L}_\xi \alpha$ on $\Omega^k(M)$ and identifies the
weight curvature $\omega_V$ with the symplectic form
$d\varTheta$ on $H$. Proposition: Jacobiator of the $q$-Lie bracket, with its proof, computes $\mathrm{Jac}_q(U,V,W) =
-q^{-1}(1-q^{-1}) \sum_{\mathrm{cyc}} d\varTheta(V,W)
\mathcal{L}_\xi U$ on horizontal vector fields and concludes
that $[\cdot,\cdot]_q$ is a Leibniz (not Lie) algebra for
$q \neq 1$ — the same prefactor as $d_q^2$, driven by the same
Levi form. Remark: Classical recovery at $q = 1$ records that
all four deformed operators of the chapter ($d_q$,
$[\cdot,\cdot]_q$, $A_q$, $\xi_q$) follow the uniform
interpolation pattern $q^{-1}(\text{classical}) + (1 -
q^{-1})(\text{Reeb correction})$ and reduce to their classical
counterparts in the limit. The next section, **Physical
elaborations**, takes the same operators and reads off physical
phenomena (torsion leaves, the spinor sign rule, the linearised
Schrödinger equation).

_(draft.)_
<!-- FILE_END: dq-squared-elaboration-intro.md -->

<!-- FILE_START: dq-squared.md -->
The archimedean specialisation of the categorical $d_q^2$ formula
([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)) yields,
for the $q$-deformed exterior derivative
([$q$-exterior derivative](#ex:q-ext-deriv)) acting on
$\Omega^k(M)$:

$$
  d_q^2\alpha
  =  q^{-1}(1 - q^{-1})d\varTheta \wedge \mathcal{L}_\xi\alpha.
$$

```tex
\begin{equation}\label{eq:dq-squared-archimedean-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(M) \ar[r, "d_q"] \ar[rr, bend left=25, "d_q^2"]
  & \Omega^{k+1}(M) \ar[r, "d_q"]
  & \Omega^{k+2}(M)
\end{tikzcd}
\qquad\text{($d_q^2 \neq 0$ for $q \neq 1$)}
\end{equation}
```

Here the categorical curvature $\omega_V$ of the weight projection
specialises to $d\varTheta$ (the symplectic form on $H$) via the
([categorical--geometric correspondence](#prop:categorical-archimedean-bridge)),
and $[\xi, \alpha]$ becomes $\mathcal{L}_\xi\alpha$.

In particular, $d_q^2 = 0$ if and only if $q = 1$ (classical case) or
$\alpha$ lies in the kernel of $\mathcal{L}_\xi$ (Reeb-invariant forms).
On horizontal $\mathcal{L}_\xi$-invariant forms, $d_q$ *does*
define a cochain complex.

Though the proof utilises standard simplification over the obstruction product, framing the failure of the cochain complex condition geometrically—as proportional to the symplectic form and Reeb-invariant flow—constitutes a novel physical translation for the Quantum Observable Universe.
<!-- FILE_END: dq-squared.md -->

<!-- FILE_START: q-jacobiator.md -->
The archimedean specialisation of the categorical $q$-Lie bracket
([categorical $q$-Lie bracket](#def:categorical-q-lie-bracket)) to
the $q$-deformed Lie bracket ([$q$-Lie bracket](#ex:q-lie-bracket))
violates the Jacobi identity when $q \neq 1$.

Let $U, V, W \in \Gamma(H)$ be horizontal vector fields (i.e.
$\varTheta(U) = \varTheta(V) = \varTheta(W) = 0$). The *Jacobiator*

$$
  \mathrm{Jac}_q(U,V,W)
   :=  [[U,V]_q, W]_q + [[V,W]_q, U]_q + [[W,U]_q, V]_q
$$

is given by

$$
  \mathrm{Jac}_q(U,V,W)
  =  -q^{-1}(1-q^{-1})\!\sum_{\mathrm{cyc}}
        d\varTheta(V,W)\mathcal{L}_\xi U,
$$

where the sum is over cyclic permutations of $(U,V,W)$. In particular,
$\mathrm{Jac}_q = 0$ if and only if $q = 1$ (classical Jacobi identity)
or $d\varTheta|_{H \times H} = 0$ (integrable horizontal distribution).
Since $d\varTheta|_{H \times H}$ is the Levi form $L_\varTheta$, which is
non-degenerate by hypothesis, $[\cdot,\cdot]_q$ violates the Jacobi
identity for all $q \neq 1$. Thus $(\mathfrak{X}(M), [\cdot,\cdot]_q)$
is a *Leibniz algebra* (or a pre-Lie algebra), not a Lie algebra.

```tex
\begin{equation}\label{eq:q-jacobiator-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  {[\cdot,\cdot]_q} \ar[r, "\mathrm{Jac}_q"]
    \ar[d, "q{=}1"']
  & q^{-1}(1{-}q^{-1})d\varTheta \wedge \mathcal{L}_\xi \\
  {[\cdot,\cdot]} \ar[r, "\mathrm{Jac}"']
  & 0
\end{tikzcd}
\qquad\text{(Jacobiator)}
\end{equation}
```

The coefficient $q^{-1}(1-q^{-1})$ matches the $d_q^2$ obstruction
([archimedean $d_q^2$](#prop:dq-squared)), confirming that both
failures — of nilpotence and of the Jacobi identity — are driven by
the same geometric source: the non-degeneracy of the contact structure.
<!-- FILE_END: q-jacobiator.md -->

<!-- FILE_START: classical-recovery.md -->
All four $q$-deformed operators interpolate between the classical ($q = 1$)
and deformed ($q > 1$) regimes via the uniform pattern
$q^{-1} \cdot (\text{classical}) + (1 - q^{-1}) \cdot (\text{Reeb correction})$.
At $q = 1$ each recovers its classical counterpart:
$d_q = d$ ([$q$-exterior derivative](#ex:q-ext-deriv)),
$[\cdot,\cdot]_q = [\cdot,\cdot]$
([$q$-Lie bracket](#ex:q-lie-bracket)),
$A_q = A$ ([$q$-connection](#ex:q-connection)), and
$\xi_q = \xi$ ([$q$-Reeb vector field](#ex:q-reeb-vector-field)).
The connection $A_q$ interpolates between the full instanton connection and
its Reeb component $\iota_\xi A\varTheta$.
<!-- FILE_END: classical-recovery.md -->

