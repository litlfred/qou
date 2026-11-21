---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-009-52-chern--simons-invariants
section_title: "Chern--Simons invariants"
section_number: 5.2
pages: 35-39
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.983
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
\noindent We begin by recalling formulas from \cite{[18]} for
the Chern--Simons invariants of the flat $\SU(2)$--connections
on $M_{p/q}$. The basic tool will be \refthm{thm:KK} below due
to P.\ A.\ Kirk and E.\ P.\ Klassen.

Let $M$ be a closed oriented $3$--manifold with a knot $K$ in
its interior and let $X$ be the complement of a tubular
neighborhood of $K$ in $M$. Moreover, let $\mu$ be a meridian
of $K$ and $\lambda$ a longitude, both in $\partial X$. Let $G$
be $\SU(2)$ or $\SL(2,\C)$. If $\rho : \pi_{1}(X) \to G$ is a
representation, then $\rho$ extends to a $G$--representation of
$\pi_{1}(M)$ if and only if $\rho(\mu)=1$. Now assume that
$\rho_{t} : \pi_{1}(X) \to G$ is a piecewise smooth path of
representations, $t \in I=[0,1]$. Choose a piecewise smooth
path $g : I \to G$ such that
\begin{eqnarray}\label{eq:pathkonjugering}
g_{t} \rho_{t}(\mu) g_{t}^{-1} &=&
\diag \left( e^{2\pi i \alpha(t)},e^{-2\pi i \alpha(t)}
\right), \nonumber \\*
g_{t} \rho_{t}(\lambda) g_{t}^{-1} &=&
\diag \left( e^{2\pi i \beta(t)},e^{-2\pi i \beta(t)} \right)
\end{eqnarray}
for some piecewise smooth curves $\alpha,\beta$. If $G=\SU(2)$
this is always possible by \cite[Lemma 3.1]{[18]}, and in that
case $\alpha$ and $\beta$ are real-valued. If $G=\SL(2,\C)$ the
above is possible if the path $\rho$ avoids the parabolic
representations (i.e.\ upper triangular with $1$s or $-1$s on
the diagonal), cf.\ \cite[Remark p.~354]{[18]}. (See the text
in connection to (\ref{eq:rhoa1}) for the case of the figure
$8$ knot.) In that case the curves $\alpha$ and $\beta$ are
complex-valued. We then have


\begin{theorem}[ {\cite[Theorem 4.2]{[18]}} ]\label{thm:KK}
Assume that $\rho_{0}(\mu)=\rho_{1}(\mu)=1$. Thinking of
$\rho_{0}$ and $\rho_{1}$ as flat $G$--connections on $M$, we
have
$$
\CS(\rho_{1})-\CS(\rho_{0})
= -2\int_{0}^{1} \beta(t)\alpha'(t) \dte t \pmod{\Z},
$$
where $\CS$ is the Chern--Simons functional associated to
$G$.\HS
\end{theorem}


We note that in case $G=\SL(2,\C)$ the Chern--Simons functional
takes values in $\C/\Z$.

Next consider a knot $K$ in $S^{3}$ and let $X$ be the knot
complement. Let $p/q$ be a rational number and let $N_{p/q}$ be
the closed oriented $3$--manifold obtained by $p/q$ surgery on
$S^{3}$ along $K$. Let $\mu$ and $\lambda$ be classes in
$\pi_{1}(\partial X)$ represented by respectively a meridian
and the preferred longitude of $K$. Choose integers
$c,d \in \Z$ such that $pd-qc=1$. Let $V$ be a tubular
neighborhood of $K$ considered as a subspace of $N_{p/q}$. We
note that $\mu'=p\mu+q\lambda$ and $\lambda'=c\mu+d\lambda$ are
represented by respectively a meridian of $V$ and a longitude
of $V$. Assume that $\rho_t : \pi_{1}(X) \to G$, $t \in I$, is
a piecewise smooth curve of representations from the trivial
representation to a representation, which extends to a
representation of $\pi_{1}(N_{p/q})$, i.e.\ $\rho_1(\mu')=1$.
Assume, moreover, that $\rho_t$ avoids the parabolic
representations in case $G=\SL(2,\C)$, and choose curves
$\alpha,\beta$ as in (\ref{eq:pathkonjugering}) with
$\alpha(0)=\beta(0)=0$. By \refthm{thm:KK} we have
\begin{eqnarray}\label{eq:CSsurgery}
\CS(\rho_1) &=& -2\int_{0}^{1}
(c\alpha(t)+d\beta(t))(p\alpha'(t)+q\beta'(t))\dte t \\*
&=& -2\int_{0}^{1} \beta(t)\alpha'(t)\dte t
    -cp\alpha^{2}(1) - dq\beta^{2}(1) - 2cq\alpha(1)\beta(1)
            \pmod{\Z}.\nonumber
\end{eqnarray}
(We have corrected a sign error in
\cite[Formula (*) p.~361]{[18]}.) We note that this expression
is independent of the choice of $c,d$. The condition
$\rho_1(\mu')=1$ is equivalent to
\begin{equation}\label{eq:p/q1}
p\alpha(1) + q\beta(1) \in \Z.
\end{equation}
Now let $K$ be the figure $8$ knot and let
$\bar{\rho}_{\theta,\vep}$ be a $\SU(2)$--representation of
$\pi_{1}(M_{p/q})$, i.e.\ (\ref{eq:p/q}) is satisfied.
Following \cite{[18]} we determine a formula for
$\CS(\bar{\rho}_{\theta,\vep})$. For later we will here pay
special attention to the branches of the logarithm. By
\refprop{prop:SU(2)} we have
\begin{eqnarray}\label{eq:Lreaima}
\rea\left(L_{-}(\theta)\right) &=&
\rea\left(L_{+}(\theta)\right)
= 2\cos^{2}(4\pi\theta) - \cos(4\pi\theta)-2, \nonumber \\*
\ima\left(L_{\pm}(\theta)\right) &=&
\mp 2\sin(4\pi\theta)\sqrt{\cos^{2}(4\pi\theta)
         - \cos(4\pi\theta) - \frac{3}{4}}
\end{eqnarray}
for all $\theta \in [-1/3,-1/6] \cup [1/6,1/3]$. From these
identities we see that
\begin{equation}\label{eq:Lspecialvalues}
L_{\pm}(1/3) = L_{\pm}(1/6) = -1, \hspace{.2in}
L_{\pm}(1/4) = 1,
\end{equation}
and that $\ima(L_{+})<0$ and $\ima(L_{-})>0$ on $]1/6,1/4[$
with the opposite signs on $]1/4,1/3[$. We conclude that
$L_{+}(\theta)$ and $L_{-}(\theta)$ run through $S^{1}$ both
beginning and ending in $-1$, $L_{+}$ in the anti-clockwise and
$L_{-}$ in the clockwise direction, as $\theta$ runs through
$[1/6,1/3]$. We can therefore use the principal logarithm
$\Log$ to define continuous curves
$\beta_{\pm} : [1/6,1/3] \to \R$ by
\begin{equation}\label{eq:beta}
\beta_{\pm}(\theta) = \frac{1}{2\pi i} \Log(L_{\pm}(\theta))
                      + f_{\pm}(\theta),
\end{equation}
where
\begin{equation}\label{eq:f+}
f_{+}(\theta) = \left\{
\begin{array}{cl} 0,& \theta = \frac{1}{6}, \\
1,& \theta \in ]\frac{1}{6},\frac{1}{3}],\end{array}\right.
\end{equation}
and
\begin{equation}\label{eq:f-}
f_{-}(\theta) = \left\{
\begin{array}{cl} 0,& \theta \in [\frac{1}{6},\frac{1}{3}[, \\
-1,& \theta = \frac{1}{3}.\end{array}\right.
\end{equation}
By (\ref{eq:p/q}) and the definition of $\beta_{\pm}$ the
representation $\bar \rho _{\theta,\vep}$ extends to a
representation of $\pi_1(M_{p/q})$ if and only if
\begin{equation}\label{eq:p/q'}
p\theta+q\beta_{\vep}(\theta) \in \Z
\end{equation}
which is nothing but (\ref{eq:p/q1}) (reparametrized).
We note that $\beta_{\pm}$ are smooth on
$]\frac{1}{6},\frac{1}{3}[$ but not in the end points $1/6$ and
$1/3$. The terms $f_{\pm}$ have been chosen so that
$\beta_{\pm}(1/6)= 1/2$. This is needed for the proof of


\begin{proposition}[ {\cite[p.~362]{[18]}} ]\label{prop:CS1}
Let $\theta \in [1/6,1/3]$ and let $\bar{\rho}_{\theta,\pm}$
be as in \refprop{prop:SU(2)}. If $\bar{\rho}_{\theta,\vep}$
extends to a representation of $\pi_{1}(M_{p/q})$ for a
$\vep \in \{\pm 1\}$ then
$$
\CS(\bar{\rho}_{\theta,\vep}) = -\frac{1}{6} - cp\theta^{2}
- dq\beta_{\vep}^{2}(\theta) - 2cq\theta\beta_{\vep}(\theta)
- 2\int_{1/6}^{\theta}\beta_{\vep}(t)\dte t \pmod{\Z},
$$
where $\beta_{\pm}$ are the curves defined by
(\ref{eq:beta}).\HS
\end{proposition}


Kirk and Klassen prove the above result by explicitly
constructing a piecewise smooth path
$\rho : [0,1] \to \Hom(\pi,\SL(2,\C))$ from the trivial
representation to
$\bar{\rho}_{\frac{1}{6},+} = \bar{\rho}_{\frac{1}{6},-}$ with
piecewise smooth curves $\alpha,\beta:[0,1] \to \C$ as in
(\ref{eq:pathkonjugering}) satisfying $\alpha(1)=\frac{1}{6}$
and $\beta(1)=\frac{1}{2}$. Moreover, they use that
$\int_{0}^{1} \beta(t)\alpha'(t) \dte t=\frac{1}{12}$ and the
fact that $y \mapsto \bar{\rho}_{y,\vep}$,
$[1/6,\theta] \to \Hom(\pi,\SU(2))$ is a path from
$\bar{\rho}_{\frac{1}{6},\vep}$ to $\bar{\rho}_{\theta,\vep}$
with associated functions $\alpha(y)=y$ and
$\beta(y)=\beta_{\vep}(y)$. By the choice of the functions
$f_{\pm}$, these $\alpha$-- and $\beta$--functions are
continuations of the ones used for the path $\rho$ from the
trivial representation to $\bar{\rho}_{\frac{1}{6},\pm}$.

Kirk and Klassen argue that
$\int_{0}^{1} \beta(t)\alpha'(t) \dte t = \frac{1}{12}$ using a
comparison between a computer calculation and the Chern--Simons
invariants of flat $\SU(2)$--connection on the Seifert manifold
$M_{-3}$. By following Kirk and Klassen's argument
\cite[pp.~361--362]{[18]} it is actually not hard to give an
explicit calculation of this integral. Let us give some
details. The path $\rho$ from the trivial connection to
$\bar{\rho}_{\frac{1}{6},\pm}$ consists of three parts, where
$\beta$ is identically zero along the first two parts. We can
therefore concentrate on the third part. Let
$a=(3+\sqrt{5})/2$, and let $\alpha : [0,1] \to \C$ be a
piecewise smooth curve from $\frac{1}{2\pi i} \Log(\sqrt{a})$
to $1/6$. Let $t(s)=e^{4\pi i \alpha(s)}$ and choose a
piecewise smooth solution $u(s)$ to $\phi(t(s),u(s))=0$, where
$\phi$ is given by (\ref{eq:phifunction}). Then
$s \mapsto \rho_{(e^{2\pi i\alpha(s)},u(s))} =: \eta_{s}$
is the third piece of our curve $\rho$ (reparametrized).
Assuming $\alpha(s) \notin \frac{1}{2}\Z$ (so as to avoid the
parabolic representations) we can diagonalize exactly as
demonstrated after \refcor{cor:SL(2,C)} and get
$$
\tilde{\eta}_{s}(\mu) = \diag(T,T^{-1}),\qquad
\tilde{\eta}_{s}(\lambda) =
\diag\left( \lambda_{11}(T,u),\lambda_{11}(T,u)^{-1}\right),
$$
where $T=T(s)=e^{2\pi i\alpha(s)}$, $u=u(s)$, $\lambda_{11}$
is as below \refcor{cor:SL(2,C)}, and where
$\tilde{\eta}_{s}(\gamma) = U^{-1}\eta_{s}(\gamma)U$ for
$\gamma \in \pi$, where
$U=U(s)=\left( \begin{array}{cc}
                1 & -1/(T^{2}-1) \\
                0 & 1
                \end{array}
\right)$.
This shows that $\alpha(s)$ indeed plays the role as the
$\alpha$--curve for our path $\eta_{s}$. The $\beta$--curve
should be a piecewise smooth curve $\beta(s)$ starting at zero
such that
\begin{equation}\label{eq:betany}
e^{2\pi i\beta(s)} = \lambda_{11}(e^{2\pi i\alpha(s)},u(s))
\end{equation}
for $s \in [0,1]$. We note that
$\lambda_{11}(e^{2\pi i\alpha(1)},u(1))=-1$ so we must have
$\beta(1) \in \frac{1}{2} + \Z$. Since $\bar{\rho}_{1/6,\pm}$
extends to a $\SU(2)$--representation of $\pi_{1}(M_{-3})$ we
get from (\ref{eq:CSsurgery}) that
$$
- 2\int_{0}^{1} \beta(s) \alpha'(s) \dte s - \frac{1}{12}
+ \frac{1}{3}\beta(1) \pmod{\Z}
$$
is a Chern--Simons value of a flat $\SU(2)$--connection on
$M_{-3}$, so $\int_{0}^{1} \beta(s) \alpha'(s) \dte s$ is real.

We now only have to choose a nice $\alpha$--curve. Let $\delta$
be a small positive parameter less than $|\alpha(0)| < 1/6$,
and let $\alpha = \alpha_{1} + \alpha_{2} + \alpha_{3}$, where
$\alpha_{1}$ is the line segment $[\alpha(0), -i\delta]$,
$\alpha_{2}$ is the part of the circle with centre zero and
radius $\delta$ running from $-i\delta$ to $\delta$, and
$\alpha_{3} = [\delta,1/6]$. Here the parameter $\delta$ is
introduced to avoid passing through zero (so as to avoid
parabolic representations). With this choice it is not hard to
show that there is a unique continuous solution
$(u(s),\beta(s))$ to $\phi(t(s),u(s))=0$ and (\ref{eq:betany})
with $\beta(0)=0$ and $\beta(1)=\frac{1}{2}$ and to show that
$\int_{0}^{1} \beta(s) \alpha'(s)\dte s = \frac{1}{12}$ for
this solution. (Use that the integral is real and independent
of $\delta$ and calculate its $\delta \ria 0_{+}$ limit).

\refprop{prop:CS1} gives a formula for the Chern--Simons
invariants of the irreducible flat $\SU(2)$--connections on
$M_{p/q}$. Let us also determine the Chern--Simons invariants
of the reducible flat $\SU(2)$--connections on $M_{p/q}$.
Therefore let $\rho_{j/|p|}$ be as in
\refprop{prop:SU(2)abelian}, $p \neq 0$, and let
$\alpha(t)=jt/|p|$ and $\beta(t)=0$, $t \in [0,1]$, and get by
(\ref{eq:CSsurgery}) that
\begin{equation}\label{eq:CSabelianpnot0}
\CS(\rho_{j/|p|}) = -cpj^{2}/p^{2} = -cj^{2}/p \pmod{\Z},
\end{equation}
where $c$ is the inverse of $-q \bmod{p}$.

In case $p=0$ the moduli space of flat reducible
$\SU(2)$--connections on $M_{0}$ can be identified with a
closed interval, cf.\ \refprop{prop:SU(2)abelian}. Since the
Chern--Simons functional is constant on each of the connected
components of the moduli space of flat connections, we conclude
that the Chern--Simons invariant of any of the reducible
$\SU(2)$--connections is equal to the Chern--Simons invariant
of the trivial connection, i.e.\ it is equal to zero. This of
course also follows from Kirk and Klassen's result. In fact,
if $\rho_{\theta}$ denotes the abelian representation from
\refprop{prop:SU(2)abelian}, then we can put
$\alpha(t)=\theta t$ and $\beta(t) =0$, $t \in [0,1]$, and get
by (\ref{eq:CSsurgery}) that
\begin{equation}\label{eq:CSabelianp0}
\CS(\rho_{\theta}) = 0 \pmod{\Z}.
\end{equation}


\newpage
