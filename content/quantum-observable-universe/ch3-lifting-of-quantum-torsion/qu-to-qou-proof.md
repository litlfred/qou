
[Yekutieli lifting](#prop:yekutieli-lifting) establishes that the constructed
brane tower satisfies the Yekutieli lifting condition.  We prove each
structural property in turn.

*Item (1): Descent terminates.*
The centre $Z(\mathrm{End}_{\mathcal{C}}(A))$ is a finitely generated
commutative $R$-algebra (since $R$ is Noetherian and $\tau$ is faithful),
hence has finite Krull dimension $d_0$.  Observability forces the $G_q$-action
on $A$ to be faithful: any $G_q$-invariant element of $\mathrm{Ad}(A)$ would
give a non-zero element of $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A))$,
contradicting the observability condition.  Each descent step (fixed-point
reduction under $G_q$) therefore strictly reduces the Krull dimension of the
centre.  After at most $d_0$ steps, the Krull dimension reaches $0$, and the
base is a discrete (Artinian) scheme.

*Item (2): $\kappa_0$ equals the Euler class.*
The first Yekutieli obstruction $\kappa_0 \in H^2(\mathcal{S}, \mathcal{B})$
is the connecting homomorphism image of the bundle class $[A_0]$ under the
central extension $1 \to \mathcal{B} \to \mathfrak{G}_1 \to \mathfrak{G}_0
\to 1$ ([Yekutieli lifting](#prop:yekutieli-lifting)).  In the archimedean
realisation, this identifies with the Euler class $e$ of the Reeb
$\mathrm{U}(1)$-bundle via the Gysin sequence.  The trace map sends
$\kappa_0$ to $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$.

*Item (3): Perpetual obstruction.*
The class $\kappa_0$ lies in the image of $H^2(\mathcal{S}, \underline{R})
\to H^2(\mathcal{S}, \mathcal{B})$ (constant/topological classes), while jet
corrections at level $n$ lie in the image of $H^2(\mathcal{S},
\mathcal{O}_{\mathcal{S}}) \to H^2(\mathcal{S}, \mathcal{B})$ (analytic/algebraic
classes).  When $\kappa_0$ is non-torsion, these images are complementary
subgroups, so the corrections cannot cancel $\kappa_0$.  In the archimedean
realisation, the splitting follows from the exponential sequence; in the
algebraic setting, from the étale--analytic comparison.

*Item (4): Riemann--Hurwitz.*
The branched covering $\pi \colon S \to \mathbb{P}(V)$ of degree $d$ has
total ramification $R_{\mathrm{tot}} = 2d + \lvert\chi(A)\rvert$ by
Riemann--Hurwitz: $\chi(S) = d \cdot \chi(\mathbb{P}(V)) - R_{\mathrm{tot}}$
with $\chi(\mathbb{P}(V)) = 2$.

*Item (5): Terminal fiber data.*
At a branch point $p$, the Krull dimension of the centre is $0$, so the base
is a point.  The QOU data reduces to the fiber: the Frobenius--Hopf
algebra $A$ at parameter $q(p)$, with the involution
$\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ of
[fibre adjoint involution](#prop:fiber-adjoint-involution).
