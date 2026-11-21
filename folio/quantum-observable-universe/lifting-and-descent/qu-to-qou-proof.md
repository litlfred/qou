[Yekutieli lifting](#prop:yekutieli-lifting) establishes that the constructed
brane tower satisfies the Quantum lifting condition.  One proves each
structural property in turn.

*Item (1): :refterm[Descent]{#descent} terminates.*
The centre $Z(\mathrm{End}_{\mathbf{C}}(A))$ is a finitely generated
commutative $R$-algebra (since $R$ is Noetherian and $\tau$ is faithful),
hence has finite Krull dimension $d_0$.  Observability forces the
$G_q$-action on $A$ to be faithful: any $G_q$-invariant element of
$\mathrm{Ad}(A)$ would give a non-zero element of
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$.  Each :refterm[descent]{#descent} step strictly
reduces the Krull dimension of the centre, so after at most $d_0$ steps
the base becomes a discrete (Artinian) scheme.

*Item (2): $\kappa_0$ equals the Euler class.*
On a manifold the sheaf $\underline{\mathbb{R}}$ of smooth real functions is fine, so $H^k(\mathcal{S}, \underline{\mathbb{R}}) = 0$ for $k \geq 1$. Every $\underline{\mathbb{R}}$-torsor is therefore trivial. The connecting map of $1 \to \underline{\mathbb{Z}} \to \underline{\mathbb{R}} \to \underline{\mathrm{U}(1)} \to 1$ is an isomorphism $\delta \colon H^1(\mathcal{S}, \underline{\mathrm{U}(1)}) \to H^2(\mathcal{S}, \mathbb{Z})$, and it sends the class of $\xi$ to $c_1(\xi)$. So $\xi$ lifts along $\underline{\mathbb{R}} \to \underline{\mathrm{U}(1)}$ exactly when $c_1(\xi) = 0$, and the obstruction is $\kappa_0 = c_1(\xi)$. For an oriented circle bundle, $c_1 = e$. When $\xi$ is the unit tangent bundle, $e(\xi)[\mathcal{S}] = \chi(\mathcal{S})$ by Poincaré--Hopf. This is the torsor instance of the lifting theorem for central extensions of gerbes (Yekutieli 2010, Example "torsors" and Theorem 4.17). On Bring's surface, $\kappa_0 = -6$.

*Item (3): Kummer persistence.*
Taking $n$-th powers is a surjection of sheaves $\underline{\mathrm{U}(1)} \to \underline{\mathrm{U}(1)}$, since $n$-th roots exist locally. Its kernel is the constant sheaf $\mu_n$. The long exact sequence contains
$$
  H^1(\mathcal{S}, \underline{\mathrm{U}(1)})
   \xrightarrow{\;n\;}
  H^1(\mathcal{S}, \underline{\mathrm{U}(1)})
   \longrightarrow
  H^2(\mathcal{S}, \mu_n)
   \longrightarrow
  H^2(\mathcal{S}, \underline{\mathrm{U}(1)}).
$$
By item (2), $H^1(\mathcal{S}, \underline{\mathrm{U}(1)}) \cong H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z}$. Similarly $H^2(\mathcal{S}, \underline{\mathrm{U}(1)}) \cong H^3(\mathcal{S}, \mathbb{Z}) = 0$ for a surface. So $H^2(\mathcal{S}, \mu_n) \cong \mathbb{Z}/n$. The obstruction to an $n$-th root of $\xi$ is the image of $c_1(\xi) = \chi(\mathcal{S})$, namely $\chi(\mathcal{S}) \bmod n$. It vanishes exactly when $n \mid \chi(\mathcal{S})$. For $\chi(\mathcal{S}) \neq 0$ that happens for finitely many $n$. On Bring's surface those are $n \in \{1, 2, 3, 6\}$; the case $n = 2$ is a spin structure.

*Retracted claim.* Earlier versions of this theorem asserted a *perpetual obstruction*: $\kappa_n \neq 0$ at every level of the jet-prolongation tower, because $\kappa_0$ and the jet corrections were said to live in complementary subgroups of $H^2(\mathcal{S}, \mathcal{B})$. That claim does not hold on a closed surface such as Bring's.
- The corrections lie in the image of $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) = 0$.
- $H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z}$ has no non-trivial complement.
- The archimedean band $\mathcal{O}^{\times}$ has $H^2(\mathcal{S}, \mathcal{O}^{\times}) = 0$.

The persistence statement that does hold is item (3), in the Kummer tower rather than the jet tower. In the jet tower, the holomorphic extension classes of the tangent bundle are non-zero at every level except $n = 3$; see the [remark on jet-tower splitting](#rem:jet-tower-splitting-bring).

*Item (4): Riemann--Hurwitz.*
The branched covering $\pi \colon S \to \mathbb{P}(V)$ of degree $d$ has
total ramification $R_{\mathrm{tot}} = 2d + \lvert\chi(A)\rvert$ by
Riemann--Hurwitz: $\chi(S) = d \cdot \chi(\mathbb{P}(V)) - R_{\mathrm{tot}}$
with $\chi(\mathbb{P}(V)) = 2$.

*Item (5): Terminal fiber data.*
At a branch point $p$, the Krull dimension of the centre is $0$, so the
base is a point.  The QOU data reduces to the fiber: the Frobenius--Hopf
algebra $A$ at parameter $q(p)$, with the involution
$\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ of
[fibre adjoint involution](#prop:fiber-adjoint-involution).  $\square$

*Item (6): Lifting criterion.*
This is proved for a central extension of presheaves of groups that is exact and central on every section group, and a cocycle with a local lift on overlaps. The obstruction is a 2-cocycle. Its class does not depend on the local lift, and it is compatible with refinement of the cover.
