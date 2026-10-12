[Yekutieli lifting](#prop:yekutieli-lifting) establishes that the constructed
brane tower satisfies the Quantum lifting condition.  We prove each
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
The first obstruction $\kappa_0 \in H^2(\mathcal{S}, \mathcal{B})$
is the connecting-homomorphism image of $[A_0]$ under the central extension
$1 \to \mathcal{B} \to \mathfrak{G}_1 \to \mathfrak{G}_0 \to 1$.  In the
archimedean realisation, this identifies with the Euler class $e$ of the
Reeb $\mathrm{U}(1)$-bundle via the Gysin sequence; the trace map sends
$\kappa_0$ to $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$.

*Item (3): Perpetual obstruction.*
The class $\kappa_0$ lies in the image of
$H^2(\mathcal{S}, \underline{R}) \to H^2(\mathcal{S}, \mathcal{B})$
(constant/topological), while jet corrections at level $n$ lie in the
image of $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}}) \to H^2(\mathcal{S}, \mathcal{B})$
(analytic/algebraic).  When $\kappa_0$ is non-torsion, these images are
complementary, so corrections cannot cancel $\kappa_0$.

*Scope of items (2) and (3).* Both depend on the band $\mathcal{B}$, which this proof does not fix.

- **Item (2).** The identification requires an obstruction group in which the Euler class can be non-zero. The Euler class of the Reeb $\mathrm{U}(1)$-bundle is its first Chern class. That is the image under $c_1$ of a class in $H^1(\mathcal{S}, \mathcal{O}^{\times})$, landing in $H^2(\mathcal{S}, \mathbb{Z})$. For the archimedean band $\mathcal{B} = \mathcal{O}^{\times}$ on a closed surface, $H^2(\mathcal{S}, \mathcal{O}^{\times}) \cong H^3(\mathcal{S}, \mathbb{Z}) = 0$. There $\kappa_0 = 0$, while $e = \chi = -6$ on Bring's surface, so item (2) does not hold for that band.
- **Item (3).** It is conditional on $\kappa_0$ being non-torsion. For $\mathcal{B} = \mathcal{O}^{\times}$ on a surface the hypothesis is never met, and item (3) is vacuous there. The complementary-subgroup step above is stated, not derived.

Both items are coherent only for a band whose $H^2$ contains the integral Euler class, such as $\mathbb{Z}$. Constructing the central extension that the jet tower actually lifts through, and deriving $\kappa_0$ from it, is open.

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
