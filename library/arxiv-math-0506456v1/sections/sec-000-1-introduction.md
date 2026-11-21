---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-10
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.962
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
\noindent In this paper we investigate the large level
asymptotics of the Reshetikhin--Turaev invariants of the
$3$--manifolds obtained by doing surgery on the figure $8$
knot with an arbitrary rational surgery coefficient. Let $X$
be a closed oriented $3$--manifold and let $\tau_r(X)$ be the
RT--invariant of $X$ associated to $\frsl_{2}(\C)$ at level
$r$, some integer $\geq 2$. The investigations of this paper
are motivated by the following conjecture.


\begin{conjecture}[Asymptotic expansion conjecture
(AEC)]\label{conj:AEC}
There exist constants (depending on X) $d_j \in \Q$ and
$b_j \in \C$ for $j=0,1, \ldots, n$ and $a_j^l \in  \C$ for
$j=0,1, \ldots, n$,\, $l=1,2,\ldots$ such that the asymptotic
expansion of $\tau_{r}(X)$ in the limit $r \ria \infty$ is
given by
\[\tau_r(X) \sim \sum_{j=0}^n e^{2\pi i r q_j} r^{d_j}
b_j \left( 1 + \sum_{l=1}^\infty a_j^l r^{-l}\right), \]
where $q_0 = 0, q_1, \ldots, q_n$ are the finitely many
different values of the Chern--Simons functional on the space
of flat $\SU(2)$--connections on $X$.
\end{conjecture}


Here {\bf $\sim$} means {\bf asymptotic expansion} in the
Poincar\'{e} sense, which means the following: Let
\[d = \max\{d_0,\ldots,d_n\}.\]
Then, for any non-negative integer $L$, there is a $c_L \in \R$
such that
\[\left| \tau_r(X) - \sum_{j=0}^n e^{2\pi i r q_j} r^{d_j}
b_j \left( 1 + \sum_{l=0}^L a_j^l
r^{-l}\right) \right| \leq c_L r^{d-L-1}\]
for all levels $r$. Of course such a condition only puts
limits on the large $r$ behaviour of $\tau_{r}(X)$.

Given an arbitrary complex function $f(r)$ defined on the
positive integers a little simple argument shows that there
at most exists one list of numbers $n \in \{0,1,\ldots\}$,
$q_0,q_1,\ldots,q_n \in \R \cap [0,1[$, $d_j \in \Q$
and $b_j \in \C$ for $j=0,1,\ldots, n$
and $a_j^l \in  \C$ for $j=0,1, \ldots, n$,\,
$l=1,2,\ldots$ such that $q_0 < q_1 < \ldots < q_n$,
$b_j \neq 0$ for $j>0$ and such
that the large $r$ asymptotic expansion of $f(r)$ is given by
\[f(r) \sim \sum_{j=0}^n e^{2\pi i r q_j} r^{d_j}
b_j \left( 1 + \sum_{l=1}^\infty a_j^l r^{-l}\right). \]
This implies that if the function $r \mapsto \tau_r(X)$ has an
asymptotic expansion of the form stated in \refconj{conj:AEC}
then the $q_j$'s, $d_j$'s, $b_j$'s and the $a_j^l$'s are all
uniquely determined by the set of invariants
$\{ \tau_r(X) \}_{r \geq 2}$, hence they are also topological
invariants of $X$. As stated above the AEC already includes the
claim that the $q_j$'s are the Chern--Simons invariants. There
are also conjectured topological formulae for the $d_j$'s, and
$b_j$'s (see e.g.\ \cite{[2]} and the references given there).

In general, there should be expressions for each of the
$a_j^l$'s in terms of sums over Feynman diagrams of certain
contributions determined by the Feynman rules of the
Chern--Simons theory. This has not yet been worked out in
general, except in the case of an acyclic flat connection and
the case of a smooth non-degenerate component of the moduli
space of flat connections by Axelrod and Singer,
cf.\ \cite{[4]}, \cite{[5]}, \cite{[3]}.

The AEC, \refconj{conj:AEC}, however offers in a sense a
converse point of view, where one seeks to derive the final
output of perturbation theory after all cancellations have
been made (i.e.\ collect all terms with the same Chern--Simons
value). This seems actually rather reasonable in this case,
since the exact invariant is known explicitly.

The AEC was proved by Andersen in \cite{[1]} in the case of
mapping tori of finite order
diffeomorphisms of orientable surfaces of genus at least two
using the gauge-theoretic approach to the quantum invariants.
Later on the AEC was proved by Hansen in \cite{[9]} for all
Seifert manifolds with orientable base by supplementing the
work of Rozansky \cite{[31]} with the required analytic
estimates. In \cite{[10]} the AEC is futher proved for the
Seifert manifolds with nonorientable base of even genus.

Using the approach of Reshetikhin and Turaev to the quantum
invariants, the AEC has not yet been proved for any hyperbolic
$3$--manifold. It is therefore particular interesting to
consider surgeries on the figure $8$ knot. Let $M_{p/q}$ be
the manifold obtained by (rational) Dehn surgery on the
figure $8$ knot with surgery coefficient $p/q$. Then $M_{p/q}$
has a hyperbolic structure if and only if $|p|>4$ or $|q|>1$,
see e.g.\ \cite[Theorem 10.5.10]{[25]} or \cite{[33]}.
(It is well-known that for $|q|=1$ and $|p| \in \{1,2,3\}$
$M_{p/q}$ is a Seifert manifold, and $M_{\pm 4}$ are obtained
by gluing together the complement of the trefoil knot and the
non-trivial $I$--bundle over the Klein bottle, see e.g.\
\cite[p.~95]{[15]}. The manifold $M_0$ is a mapping torus of
a torus, see Appendix C.) We use here the convention of Rolfsen
for surgery coefficients, cf.\ \cite[Chap.~9]{[30]}. In
particular Dehn surgery on a knot $K$ in $S^{3}$ with surgery
coefficient $f \in \Z$ is equal to the boundary of the compact
$4$--manifold obtained by attaching a $2$--handle to the
$4$--ball using the knot $K$ with framing $f$, see
\cite[p.~261]{[30]}. As usual $M_{p/q}$ is given the
orientation induced by the standard right-handed orientation
of $S^{3}$.

The advantage of working with surgeries on the figure $8$ knot
$K$ is that the (normalized) colored Jones polynomial
$J_K'(\lambda)$ is known explicitly. In fact
\[J'_K(\lambda) =  \sum_{m=0}^{\lambda-1} \xi^{-m\lambda}
\prod_{l=1}^{m}(1-\xi^{\lambda-l}) (1-\xi^{\lambda+l}), \]
where $\xi=\exp(2\pi i/r)$ (and the product is $1$ for $m=0$).
The colors $\lambda$ are here dimensions of irreducible
representations of the quantum group associated to
$\frsl_{2}(\C)$ and the root of unity $\xi$, so
$\lambda =1,2,\ldots,r$. By the above expression for
$J_{K}'(\lambda)$ we have an explicit formula for the quantum
invariant $\tau_r(M_{p/q})$ (see formula (\ref{eq:inv2})).
Although this formula is completely explicit, it is not clear
from it what the leading order large $r$ asymptotics of
$\tau_r(M_{p/q})$ is. In order to study this asymptotics, we
observe (generalizing from Kashaev's work) that the product
in the expression for the colored Jones polynomial can be
expressed in terms of a quotient of two evaluations of
Faddeev's quantum dilogarithm $S_\gamma$ ($\gamma = \pi/r$):
\begin{equation}\label{ncJones}
J'_K(\lambda) =  \sum_{m=0}^{\lambda-1}
\frac{\xi^{-m\lambda}}{(1-\xi^{\lambda})}
\frac{S_{\gamma}(-\pi+2\gamma(\lambda - m) -\gamma)}
{S_{\gamma}(-\pi+2\gamma(\lambda + m) +\gamma)}.
\end{equation}
This follows directly from the functional equation
$$
(1+e^{\I \zeta})S_{\gamma}(\zeta+\gamma) =
S_{\gamma}(\zeta-\gamma)
$$
which Faddeev's $S_\gamma$ satisfies. Recall that for
$\rea(\zeta) < \pi +\gamma$ we have the expression
\[S_{\gamma}(\zeta) = \exp \left( \frac{1}{4} \int_{C_{R}}
\frac{e^{\zeta z}}{\sinh(\pi z)\sinh(\gamma z)z} \dte z\right),
\]
which together with the functional equation determines
$S_\gamma$ as a meromorphic function on $\C$. For the so-called
top color, i.e.\ $\lambda=r$, we obtain the sligthly simpler
expression
$$
J'_K(r) =  r\sum_{m=0}^{r-1}
\frac{S_{\gamma}(\pi - (2m+1)\gamma)}
{S_{\gamma}(-\pi + (2m+1)\gamma)}.
$$
Then we simply use the residue formula to convert this
expression into a contour integral
$$
J_K'(r) =  \int_{C_r} \tan(\pi r x) \tilde{g}_{r}(x) \dte x,
$$
where $C_r$ is contained in the strip
$\{ z \in \C \mid 0 < \rea(z) < 1 \}$ and encloses
$(m + \frac12)/r$ for $m=0, \ldots, r-1$, and $\tilde{g}_{r}$
is a holomorphic function in this strip expressed in terms of
the above quotient of $S_\gamma$ functions (see formula
(\ref{eq:contourfigure8})).

Similarly we get for the quantum invariant with the use of
(\ref{ncJones}) and the residue theorem, now a double contour
integral, since the quantum invariant also involves a sum over
colors:
\begin{equation}\label{qidci}
\tau_r(M_{p/q}) = \int_{C_r\times C_r} \cot(\pi r x)
\tan(\pi r y) \tilde{f}_{p,q,r}(x,y) \dte x \dte y,
\end{equation}
where $\tilde{f}_{p,q,r}$ is holomorphic on the double strip
$\{ z \in \C \mid 0 < \rea(z) < 1 \}^{2}$ and given by some
expression involving quotients of evaluations of
$S_\gamma$ functions, and where we furthermore require of
$C_r$ that it also encloses $k/r$ for $k=1, \ldots, r-1$.

From this it is clear that we need to understand the small
$\gamma$ asymptotics of $S_\gamma$. We have that
\[S_\gamma(\zeta) = \exp\left( \frac{1}{2\I \gamma}
\Li _{2} (-e^{\I \zeta} ) + I_\gamma(\zeta)\right),\]
where $\Li_{2}$ is Euler's dilogarithm function, and where we
have certain analytic estimates on $I_\gamma(\zeta)$ (see
\reflem{lem:Sapproximation}).

Let us first explain how we use this to give a proof of the
volume conjecture of Murakami and Murakami \cite{[24]} for
the figure $8$ knot, namely that
$$
\lim_{r \ria \infty} \frac{2\pi\Log(J_{K}'(r))}{r} =
\Vol(K),
$$
where the right-hand side is the hyperbolic volume of the
figure $8$ knot, i.e.\ the hyperbolic volume of the complement
$S^{3} \sm K$. The basic idea in analyzing the above contour
integral expression for $J_K'(r)$ is the following. In the
upper half plane we approximate $\tan$ by $\I$ and by $-\I$ in
the lower half plane. Further we approximate $S_\gamma$ by the
above expression involving only the dilogarithm. In Appendix B
we prove the required estimates which allows us to do these
approximations and we end up with the following formula for the
leading order large $r$ asymptotics
\begin{equation}\label{eq:Asymf8'}
J'_K(r) \sim r^{2}  \int_\epsilon^{1-\epsilon}
e^{r\Phi(x)} \dte x,
\end{equation}
where $\epsilon <1/(4r)$ is a small positive parameter and
\[\Phi(x)= \frac{1}{2\pi\I}
\left( \Li_{2}(e^{-2\pi\I x}) - \Li_{2}(e^{2\pi\I x})\right).\]
Now we simply analyze the integral on the right-hand side of
(\ref{eq:Asymf8'}) by the saddle point method. This consists of
finding the stationary points of $\Phi$ and also the
directions of steepest descent, see e.g.\ \cite{[6]}.
(In this paper we use critical point and stationary point
interchangeably to mean a point in which the derivative is
zero.) This analysis leads to two interesting results. Firstly,
the search for stationary points leads to the hyperbolicity
equation for the complement of the figure $8$ knot in the
$3$--sphere. Recall that this complement can be decomposed into
two ideal hyperbolic tetrahedra each parametrized by
a certain complex number. This decomposition then defines a
hyperbolic structure on the complement exactly when the two
parameters are equal and satisfy the hyperbolicity equation.

Secondly, we find that the value of the phase function in the
relevant stationary point (there is only one such point in
this case) is equal to the hyperbolic volume of the knot
complement (divided by $2\pi$), hence the leading asymptotics
of $J_{K}'(r)$ is determined by this volume.

These phenomena were first observed by Kashaev \cite{[14]} and
have been conjectured by Thurston \cite{[32]} and Yokota
\cite{[35]} to be generally true for hyperbolic knots
(see \refrem{rem:hyperbolicity}).

Ultimately our asymptotic analysis leads to the following


\begin{theorem}
The leading order large $r$ asymptotics of the colored Jones
polynomial evaluated at the top color is given by
$$
J_{K}'(r) \sim 3^{-1/4} r^{3/2}
\exp\left(\frac{r}{2\pi}\Vol(K)\right).
$$
\end{theorem}


As a corollary we obtain the volume conjecture for the figure
$8$ knot. We note that none of the proofs so far given in the
literature for the volume conjecture for the figure $8$ knot
have been able to see the finer details of the asymptotic
behaviour, namely the polynomial part $3^{-1/4}r^{3/2}$.

After completion of this paper we have been informed that
D.\ Zagier has computed the full asymptotic expansion of
$J_{K}'(r)$ by using the Euler--Maclaurin summation formula,
however his techniques seem not applicable to the calculation
of the large $r$ asymptotics of $\tau_r(M_{p/q})$.

Let us now return to the study of the large $r$ asymptotics of
the quantum invariant $\tau_{r}(M_{p/q})$. We expect that an
analysis of the expression (\ref{qidci}) paralleling our
analysis of $J'_K(r)$ should be applicable. I.e.\ $\tan$ and
$\cot$ should be approximated by $\pm \I$ depending on the
signs of $\ima(y)$ and $\ima(x)$ and $\tilde{f}_{p,q,r}(x,y)$
by an appropriate expression involving the dilogarithm for some
deformation of the relevant part of $C_r\times C_r$. We have
partial analytic results supporting this.

To be more specific we propose the following analog of
(\ref{eq:Asymf8'}) for the quantum invariant. Let $d$ be the
inverse of $p \bmod{q}$ and let $(a,b)\in \{0,1\}^2$ and
$n \in \Z$. Define
$$
\Phi_{n}(x,y) = -\frac{dn^{2}}{q} - \frac{p}{4q} x^{2}
  + \frac{n}{q}x-xy + \frac{1}{4\pi^{2}}
  \left( \Li_{2}(e^{2\pi i(x+y)}) - \Li_{2}(e^{2\pi i (x-y)})
\right),
$$
and
\begin{equation}\label{Phi}
\Phi_{n}^{a,b}(x,y) = a(x+y) + b(x-y) + \Phi_{n}(x,y).
\end{equation}
Finally, let
\begin{equation}\label{eq:SUcriticalpoint}
\mS = \{ (x,y) \in \R \times \C \; | \; e^{2\pi iy} \in
]-\infty,0[ \;\}.
\end{equation}
Thus $\mS$ is the union of infinitely many planes,
namely the ones characterized by $x \in \R$ and
$\rea(y) \in \frac{1}{2} + \Z$.


\begin{conjecture}\label{conj:MC}
There exist surfaces
$\tilde{\Sigma}_{a,b}^{\mu,\nu,n} \subset \C^2$
for $(a,b) \in \{0,1\}^2$, $n \in \Z / |q|\Z$ and
$(\mu,\nu) \in \{\pm 1\}^2$ such that the leading order large
$r$ asymptotics of the quantum invariant is given by
\begin{eqnarray}\label{eq:asympqiI}
\bar{\tau}_{r}(M_{p/q}) &\sim& C r \qsum \sum_{(a,b) \in
\{0,1\}^{2}} \sum_{(\mu,\nu) \in \{ \pm 1 \}^{2}} \mu\nu \\ &&
\times \int_{\tilde{\Sigma}_{a,b}^{\mu,\nu,n}} \tilde{g}_n(x)
e^{2\pi ir\Phi_{n}^{a,b}(x,y)} \dte x \dte y,
\end{eqnarray}
where $C$ is a constant only depending on $p$ and $q$ and
$\tilde{g}_n$ is some simple $r$--independent function of
$x \in \C$. If $p/q \neq 0$ the surfaces
$\tilde{\Sigma}_{a,b}^{\mu,\nu,n} \subset \C^2$ can be chosen
such that any critical point of $\Phi_{n}^{a,b}$ belonging to
$\tilde{\Sigma}_{a,b}^{\mu,\nu,n}$ also belongs to the set
$\mS$.
\end{conjecture}


Please see \refconj{conj:mainconj} for the more detailed
version of this conjecture, including the precise formula for
$\tilde{g}_n$. (We have here for sign-reasons switched to the
complex conjugate invariant
$\bar{\tau}_{r}(M_{p/q})=\overline{\tau_{r}(M_{p/q})}
=\tau_{r}(M_{-p/q})$.) In case $p/q=0$ our results show that
we have to include critical points not belonging to $\mS$ in
our surfaces $\tilde{\Sigma}_{a,b}^{\mu,\nu,n}$, see 
Appendix C.

We now proceed by making an asymptotic analysis of the
right-hand side of (\ref{eq:asympqiI}) using the saddle point
method like in our analysis of (\ref{eq:Asymf8'}). Thus we
need to analyze integrals of the form
\begin{eqnarray}\label{eq:Int}
I_{a,b}^{\mu,\nu,n} = \int_{\tilde{\Sigma}_{a,b}^{\mu,\nu,n}}
\tilde{g}_n(x) e^{2\pi ir\Phi_{n}^{a,b}(x,y)} \dte x \dte y.
\end{eqnarray}
Again we have to determine the stationary points of
$\Phi_{n}^{a,b}$ and the values of $\Phi_{n}^{a,b}$ in the
relevant stationary points. The main idea behind the saddle
point method is to deform $\tilde{\Sigma}_{a,b}^{\mu,\nu,n}$ 
so that it contains certain stationary points of 
$\Phi_{n}^{a,b}$ satisfying that the leading order large $r$ 
asymptotics of $I_{a,b}^{\mu,\nu,n}$ is given by integrating 
the integrant of the integral (\ref{eq:Int}) over small 
neighborhoods of these stationary points.

If we let $v = e^{\pi i x}$ and $w = e^{2\pi i y}$, then by
exponentiating the two equations for $(x,y)$ being a
stationary point of $\Phi_{n}^{a,b}$ (see
\refthm{thm:main'} below) we obtain the equations
\begin{eqnarray}\label{eq:stationary'}
v^{-p} &=& \left(\frac{w-v^{2}}{1-v^{2}w}\right)^{q},
\nonumber \\*
v^2w &=& (1-v^{2}w)(w-v^{2}),
\end{eqnarray}
which are independent of the integer parameters $a,b,n$. To
link the asymptotics to the flat connections (as proposed by
the AEC) we then have to relate the relevant stationary points
of the phase functions $\Phi_{n}^{a,b}$ to the classical
$\SU(2)$ Chern--Simons theory on the manifolds $M_{p/q}$.
Fortunately, this Chern--Simons theory has been given a
detailed description by Kirk and Klassen \cite{[18]} using the
work of Riley \cite{[28]}, \cite{[29]} on the $\SL(2,\C)$
representation variety of the knot group of the figure $8$
knot. According to Riley the conjugacy classes of the
nonabelian elements of this variety can be represented
by a certain set of representations $\rho$ parametrized by
$\rho=\rho_{(s,u)}$, where $(s,u) \in \C^{*} \times \C$
satisfies a certain polynomial equation. (To be precise
$\rho_{(s_1,u_1)}$ and $\rho_{(s_2,u_2)}$ are conjugate if and
only if $u_2=u_1 \neq 0$ and $s_2 \in \{ s_1,s_1^{-1} \}$ or
$u_2=u_1=0$ and $s_2=s_1 \in A$, where $A$ is a certain subset
of $\C^{*}$ consisting of $4$ points.)

We show that $\rho_{(s,u)}$ defines a
$\SL(2,\C)$--representation of $\pi_{1}(M_{p/q})$ if and only
if $(v,w)=(s,u+1)$ is a solution to (\ref{eq:stationary'}) and
$v^{2} \neq 1$. By a result of Riley it is known that this
representation is conjugate to a $\SU(2)$--representation if
and only if $(s,u) \in S^{1} \times \R$. We relate the results
of Kirk and Klassen \cite{[18]} on the Chern--Simons invariants
of flat $\SU(2)$--connections on the manifolds $M_{p/q}$ to the
asymptotic analysis of the quantum invariants
$\bar{\tau}_{r}(M_{p/q})$ via a detailed analysis of the
relevant critical values of the phase functions $\Phi_n^{a,b}$.
Ultimately we arrive at


\begin{theorem}\label{thm:main'}
The map
$$
(x,y) \mapsto [\rho_{(e^{\pi ix},e^{2\pi i y} -1)}]
$$
gives a surjection from the set of critical points $(x,y)$ of
the functions $\Phi_{n}^{a,b}$ with $x \notin \Z$ onto the
set of conjugacy classes of nonabelian
$\SL(2,\C)$--representations of $\pi_{1}(M_{p/q})$. Moreover,
$(x,y) \in \C^{2}$ is a critical point of $\Phi_{n}^{a,b}$ if
and only if
\begin{eqnarray}\label{eq:stationary''}
2a + \frac{n}{q} &=& y + \left( \frac{p}{2q} + 1 \right)x
     + \frac{i}{\pi}\Log\left( 1 - e^{2\pi i (x+y)} \right),
\nonumber \\*
2b + \frac{n}{q} &=& y + \left( \frac{p}{2q} - 1 \right)x
     - \frac{i}{\pi}\Log\left( 1 - e^{2\pi i (x-y)} \right).
\end{eqnarray}
Futhermore, if $(x,y)$ is a critical point of $\Phi_{n}^{a,b}$
then $\rho_{(e^{\pi ix},e^{2\pi i y} -1)}$ is equivalent to
a $\SU(2)$--representation $\bar{\rho}$ of $\pi_{1}(M_{p/q})$
if and only if $(x,y) \in \mS$ (see
(\ref{eq:SUcriticalpoint})), and in that case
$$
\CS(\bar{\rho}) = \Phi_{n}^{a,b}(x,y) \pmod{\Z},
$$
where $\CS$ is the Chern--Simons functional on the space of
flat $\SU(2)$--connections on $M_{p/q}$.
\end{theorem}


Continuing our asymptotic analysis of the integral
(\ref{eq:Int}) we point out that not all critical points have
to give contributions to the asymptotics. The simplest case
arise when all the relevant critical points are non-degenerate.
Following \refconj{conj:MC} we claim that the only
critical points giving a contribution to the leading order
large $r$ asymptotics of $\tau_r(M_{p/q})$ are (some of) the
ones belonging to the set $\mS$ in (\ref{eq:SUcriticalpoint}).
In \refprop{prop:Nondeg} in Sec.~4 we prove that all these
critical points are non-degenerate in case $|p/q| < \sqrt{20}$.
In case $|p/q| > \sqrt{20}$ we have the following partial
result:
The surjection described in the first part of
\refthm{thm:main'} restricts to a surjection $\phi$ from the
set of critical points belonging to $\mS$ onto the moduli space
$\mM_{p/q}'$ of flat irreducible $\SU(2)$--connections on
$M_{p/q}$. If $p/q > \sqrt{20}$ we prove that all the
critical points belonging to $\mS \sm \mC_0$ are
non-degenerate, where $\mC_0$ is a certain set of critical
points. To be more precise the set $\mC_0$ is either empty or
it is equal to the preimage of $\phi$ of one point if $p$ is
odd and of two points if $p$ is even. We expect that the
argument equation following from the first of the equations
(\ref{eq:stationary'}) together with the last statement in
\refprop{prop:Nondeg} should establish that $\mC_0$ is empty.

From \refconj{conj:MC} we see that the only
relevant phase functions $\Phi_n^{a,b}$ are the ones with
$a,b \in \{0,1\}$. This, however, does not imply that only a
proper subset of the conjugacy classes of
$\SL(2,\C)$--representations of $\pi_1(M_{p/q})$ are in play.
In fact, by using (\ref{eq:stationary''}), we see that
if $(x,y)$ is a critical point of $\Phi_n^{a,b}$ then
$(x+2k,y+2l)$ is a critical point of
$\Phi_{n+pk}^{a+l+k,b+l-k}$ for any $k,l \in \Z$. Moreover,
the critical points $(x,y)$ and $(x+2k,y+2l)$ correspond to
the same conjugacy class of representations by the surjection
in \refthm{thm:main'}. In particular all points of the
moduli space of flat irreducible $\SU(2)$--connections on
$M_{p/q}$ could potentially give a contribution to the
asymptotics of $\bar{\tau}_r(M_{p/q})$.

One is only likely to succeed in using the saddle point method
to calculate the large $r$ asymptotics of an integral of the
form (\ref{eq:Int}) in case one can deform the surface
$\tilde{\Sigma}_{a,b}^{\mu,\nu,n}$ so that it only contains 
critical point of a certain nice kind. Here we will only 
consider the case of non-degenerate critical points. Therefore,
assume that $(x,y)$ is a non-degenerate critical point of 
$\Phi_n^{a,b}$ belonging to $\tilde{\Sigma}_{a,b}^{\mu,\nu,n}$.
Then to be able to calculate that critical point's contribution
to the large $r$ asymptotics of the integral in (\ref{eq:Int}) 
we assume that $(x,y)$ is positive definite, meaning that the 
imaginary part of a certain ``twisted'' Hessian of 
$\Phi_n^{a,b}$ in $(x,y)$ is positive definite, see 
\refdefi{defi:posdefinite} for the precise definition. 
Ultimatively we arive at the following result.


\begin{theorem}\label{thm:MT}
Assume that $p/q \neq 0$. IF \refconj{conj:MC} is true and if
all the critical points of the phase functions $\Phi_n^{a,b}$
belonging to $\mS$ are non-degenerate and positive definite,
then the leading order large $r$ asymptotics of the quantum
invariant $\bar{\tau}_{r}(M_{p/q})$ is given by
\begin{eqnarray}\label{eq:asympqi}
\bar{\tau}_{r}(M_{p/q}) &\sim&
\frac{\sign(q)}{4\sqrt{|q|}} e^{\frac{3\pi i}{4}\sign(pq)}
\sum_{\bar \rho\in {\mathcal M}'_{p/q}}
e^{2\pi i r CS(\bar \rho)} b_{\bar \rho},
\end{eqnarray}
where $\mM_{p/q}'$ is the moduli space of flat irreducible
$\SU(2)$--connections on $M_{p/q}$. For each
$\bar \rho \in {\mathcal M}'_{p/q}$ there are
$(a,b) \in \{0,1\}^2$, $n \in \Z$ and a stationary point
$(x,y) \in \mS$ for the function $\Phi_n^{a,b}$ given by
(\ref{Phi}), i.e.\ $(x,y)$ solves the equations
(\ref{eq:stationary''}), such that $\bar \rho$ is equivalent to
$\rho_{(e^{\pi ix}, e^{2\pi iy}-1)}$. Moreover
\[CS(\bar\rho) = \Phi_n^{a,b}(x,y) \pmod{\Z},\]
and
\[b_{\bar \rho} = m_{\bar \rho}
e^{\frac{\pi i\sigma_{\bar \rho}}{2}}
\sin\left( \frac{\pi}q(x-2nd)\right)
\left| 1-4\cos(2\pi x)) +
\frac{p}{2q}\sinh(2\pi \ima(y))\right|^{-\frac12}, \]
where $m_{\bar \rho}$ and $\sigma_{\bar \rho}$ are some
integers.
\end{theorem}


The positive integers $m_{\bar \rho}$ arrise from the following
two situations. First of all it can happen that two or more
critical points of the relevant stationary phase functions
correspond to the same irreducible flat $\SU(2)$--connection on
$M_{p/q}$. Secondly, the same stationary point for the same 
phase function $\Phi_n^{a,b}$ can belong to two or more of the 
surfaces $\tilde{\Sigma}_{a,b}^{\mu,\nu,n}$. In fact, we expect
that there is a one to one correspondence between the moduli 
space $\mM_{p/q}'$ of flat irreducible $\SU(2)$--connections on
$M_{p/q}$ and the set of stationary points contributing to the
leading large $r$ asymptotics of $\bar{\tau}_r(M_{p/q})$.
Moreover, we expect that a contributing stationary point for a
relevant phase function $\Phi_n^{a,b}$ belongs to (a 
deformation) of $\Sigma_{a,b}^{\mu,\nu,n}$ for all 
$(\mu,\nu) \in \{\pm 1\}^2$ thus causing $m_{\bar \rho}=4$ for 
all $\bar \rho \in \mM_{p/q}'$, see \refrem{rem:Remark4}. The 
above result, \refthm{thm:MT}, coincides with the one found by 
the second author in \cite{[10]} for the cases 
$|p/q| \in \{1,2,3\}$ with $m_{\bar \rho}=4$ for all
$\bar \rho$.

The invariant $\tau_{r}(M_{0})$ and its full asymptotic
expansion have been calculated by Jeffrey \cite{[13]}. We show
(see Appendix C) that Jeffrey's result is in agreement with the
AEC. In this case the reducible flat $\SU(2)$--connections
contribute to the leading asymptotics. We find that the part of
the leading order large $r$ asymptotics of $\tau_{r}(M_{0})$
associated to the irreducible flat $\SU(2)$--connections on
$M_0$ is given by the right hand side of (\ref{eq:asympqi})
with all $m_{\bar \rho}=4$.



\nonumsection{Acknowledgements}



\noindent The first author thanks the Department of Mathematics
and the Mathematical Sciences Research Institute, University
of California, Berkeley for their hospitality during several
visits, where part of this work was undertaken. The second
author thanks the Universit\'{e} Louis Pasteur, Strasbourg,
the University of Edinburgh, and the Max--Planck--Institut
f\"{u}r Mathematik, Bonn for their hospitality during this work.
He was supported by the European Commission, the Danish
Natural Science Research Council and the Max--Planck--Institut
f\"{u}r Mathematik, Bonn.
