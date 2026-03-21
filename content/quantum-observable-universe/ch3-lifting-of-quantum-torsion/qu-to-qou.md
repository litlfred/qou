Let $(\mathcal{C}, A, \omega)$ be a quantum universe over a Noetherian
ring $R$ ([Definition](#def:quantum-universe)); let $q$ denote the substrate parameter.  Assume observability
$\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$
([Definition](#def:quantum-observable-universe)).  Then the brane tower
$\{A_n\}_{n \geq 0}$ constructed via jet prolongation
([Proposition](#prop:jet-prolongation)) satisfies the Yekutieli lifting
condition ([Definition](#def:yekutieli-lifting-condition),
[Proposition](#prop:yekutieli-lifting)), and $(\mathcal{C}, A, \omega)$
is a quantum observable universe with the following structural properties:

1. *Descent terminates.*  The geometric descent tower has finite
   length, bounded by $\mathrm{Krull\;dim}\,
   Z(\mathrm{End}_{\mathcal{C}}(A))$.  Observability ensures each step
   is a strict reduction (the $G_q$-action is faithful, so fixed-point
   reduction strictly decreases dimension).
2. *First obstruction equals the Euler class.*  The Yekutieli
   obstruction $\kappa_0 \in H^2(\mathcal{S}, \mathcal{B})$ equals the
   Euler class of the Reeb bundle.  Under the trace map,
   $\kappa_0 \mapsto \chi(A) = \mathrm{tr}(\mathrm{id}_A) \in R$.
3. *Perpetual obstruction.*  If $\kappa_0$ is non-torsion in
   $H^2(\mathcal{S}, \mathcal{B})$, then $\kappa_n \neq 0$ for all
   $n \geq 0$.  The class $\kappa_0$ and the jet corrections at
   level $n$ live in complementary subgroups of
   $H^2(\mathcal{S}, \mathcal{B})$, so the corrections cannot cancel
   $\kappa_0$.
4. *Branch point formula.*  The geometric descent from
   $\mathbb{P}(V)$ ([Definition](#def:projective-line-object)) to
   points has $B$ branch points with total ramification
   $R_{\mathrm{tot}} = 2d + \lvert\chi(A)\rvert$ (Riemann--Hurwitz),
   where $d$ is the degree of the covering.
5. *Terminal fiber data.*  At each branch point $p$, the QOU
   reduces to fiber data $(A, \omega, q(p))$ with the involution
   $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$
   ([Proposition](#prop:fiber-adjoint-involution)).

---

[Proposition](#prop:yekutieli-lifting) establishes that the constructed
brane tower satisfies the Yekutieli lifting condition.  We prove each
structural property in turn.

*Item (1): Descent terminates.*
The centre $Z(\mathrm{End}_{\mathcal{C}}(A))$ is a finitely generated
commutative $R$-algebra (since $R$ is Noetherian and $\omega$ is faithful),
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
\to 1$ ([Proposition](#prop:yekutieli-lifting)).  In the archimedean
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
algebraic setting, from the etale--analytic comparison.

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
[Proposition](#prop:fiber-adjoint-involution).
