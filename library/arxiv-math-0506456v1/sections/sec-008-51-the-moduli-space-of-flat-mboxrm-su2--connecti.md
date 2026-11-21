---
doc_id: arxiv-math-0506456v1
doc_title: "Asymptotics of the quantum invariants for surgeries on the figure 8 knot"
section_id: sec-008-51-the-moduli-space-of-flat-mboxrm-su2--connecti
section_title: "The moduli space of flat $\mbox{\rm SU}(2)$--connections on $M_{p/q}$"
section_number: 5.1
pages: 30-35
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.976
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
\noindent In the following
$\pi=\pi_{1}\left( S^{3} \sm \nbd (K) \right)$ denotes the knot
group of the figure $8$ knot. We have a presentation
\begin{equation}\label{eq:pi}
\pi = \la \, x,y\, | wx=yw \,\ra,
\end{equation}
where $w=[x^{-1},y]$, and where $\mu=x$ and
$\lambda=yx^{-1}y^{-1}x^{2}y^{-1}x^{-1}y$ are the elements of
$\pi$ corresponding to the meridian and the preferred longitude
of $K$. The $\SL(2,\C)$ representation variety of $\pi$ was
analyzed by Riley \cite{[28]}, \cite{[29]} relevant to our
work. Consider a group $G$ given by a presentation
$$
G = \la \, x,y\, | wx=yw \,\ra,
$$
where
$w=x^{\vep_{1}}y^{\vep_{2}}x^{\vep_{3}}\cdots
y^{\vep_{\alpha-1}}$,
where $\alpha$ is odd and $\vep_{j} = \vep_{\alpha-j} = \pm 1$,
$j=1,2,\ldots,\alpha-1$. Such groups are denoted $2$--bridge
kmot groups by Riley since they generalize the $2$--bridge knot
groups. Following Riley we say that a representation
$\psi : G \to \SL(2,\C)$ is affine when the image of $\psi$
fixes exactly one point in $\C\Pro^{1}$ and not affine when
this image has no fixed points. We note that if $\psi$ is
nonabelian then $\psi$ is affine if and only if $\psi(x)$
and $\psi(y)$ have a common eigenvector, and $\psi$ is not
affine if these two matrices have no common eigenvector.
Let $H$ be some subgroup of $\SL(2,\C)$. Then we will say
that two representations $\psi_{1},\psi_{2} : G \to \SL(2,\C)$
are $H$--equivalent if they are conjugate to each other by a
matrix in $H$, i.e.\ if there exists a matrix $U \in H$ such
that $\psi_{2}(\gamma)=U\psi_{1}(\gamma)U^{-1}$ for all
$\gamma \in G$. In particular, we will say that $\psi_{1}$ and
$\psi_{2}$ are equivalent if they are  $\SL(2,\C)$--equivalent.
For $(t,u) \in \C^{*} \times \C$ we put
\begin{eqnarray*}
C_{0}(t) &=& \left( \begin{array}{cc} t & 1 \\
                0 & 1 \end{array}\right), \hspace{.2in}
D_{0}(t,u) = \left( \begin{array}{cc} t & 0 \\
                         -tu & 1 \end{array}\right), \\
C_{1}(t) &=& \left( \begin{array}{cc} t & 1 \\
                0 & t^{-1} \end{array}\right), \hspace{.2in}
D_{1}(t,u) = \left( \begin{array}{cc} t & 0 \\
                     -u & t^{-1} \end{array}\right), \\
C_{2}(t) &=& \left( \begin{array}{cc} t & t^{-1} \\
                0 & t^{-1} \end{array}\right), \hspace{.2in}
D_{2}(t,u) = \left( \begin{array}{cc} t & 0 \\
                     -tu & t^{-1} \end{array}\right).
\end{eqnarray*}
We note that $C_{\nu}(t)$ and $D_{\nu}(t,u)$ are elements of
$\SL(2,\C)$, $\nu=1,2$. If $s$ is a square root of $t$ and
$V(s)=\diag(s,s^{-1})$ then
\begin{equation}\label{eq:konjugering}
V(s)C_{2}(t)V(s)^{-1} = C_{1}(t), \hspace{.2in}
V(s)D_{2}(t,u)V(s)^{-1} = D_{1}(t,u),
\end{equation}
and
\begin{equation}\label{eq:C0C2}
C_{0}(t) = sC_{2}(s), \hspace{.2in} D_{0}(t,u) = sD_{2}(s,u).
\end{equation}
Let $W_{\nu}(t,u)$ denote the matrix obtained by replacing
$x$ and $y$ by respectively $C_{\nu}(t)$ and $D_{\nu}(t,u)$
in the expression for $w$, and let
$$
\phi(t,u) = W_{11} + (1-t)W_{12},
$$
where $W=W(t,u)=W_{0}(t,u)$. We let $\rho_{(t,u)}$ be the
assignment $x \mapsto C_{2}(t)$, $y \mapsto D_{2}(t,u)$. We
have the following $\SL(2,\C)$ version of
\cite[Theorem 1]{[28]}.


\begin{theorem}\label{thm:SL(2,C)}
Let $(s,u) \in \C^{*} \times \C$. None of the assignments
$\rho_{(s,u)}$ extend to an abelian
$\SL(2,\C)$--representation of $G$. The assignment
$\rho_{(s,u)}$ extends to a nonabelian representation
$\rho_{(s,u)} : G \to \SL(2,\C)$ if and only if
\begin{equation}\label{eq:phizero}
\phi(s^{2},u) = 0.
\end{equation}
Conversely, if $\psi : G \to \SL(2,\C)$ is a nonabelian
representation, then there exists a pair
$(s,u) \in \C^{*} \times \C$ satisfying
(\ref{eq:phizero}) such that $\psi$ and $\rho_{(s,u)}$
are equivalent. When $\psi$ is affine this pair is unique,
and when $\psi$ is not affine the pair $(s,u)$ can only be
replaced by $(s^{-1},u)$.
\end{theorem}


\begin{proof}
The theorem follows by results of \cite{[28]}, \cite{[29]}.
The assignment $\rho_{(s,u)}$ extends to a
$\SL(2,\C)$--representation of $G$ if and only if
$W_{2}(s,u)C_{2}(s,u) = D_{2}(s,u)W_{2}(s,u)$.
The matrices $C_{2}(s)$ and $D_{2}(s,u)$ commute if and only
if $s = \pm 1$ and $u=0$, and since $C_{2}(\pm 1)=\pm C_{2}(1)$
is different from $D_{2}(\pm 1,0)=\pm D_{2}(1,0)$ we have that
the assignment $\rho_{(\pm 1,0)}$ does not extend to a
$\SL(2,\C)$--representation of $G$. (We note that if $W=W(1,0)$
then $W_{21}=0$ since the matrices $C_{0}(1), D_{0}(1,0)=I$ and
their inverses are upper triangular. But we also have that
$\phi(1,0)=0$ would imply that $W_{11}=0$ contradicting the
fact that $W$ is invertible. Therefore $\phi(1,0) \neq 0$.)

Let $\sigma=\sum_{j=1}^{\alpha-1} \vep_{j}$. Then
$s^{\sigma}W_{2}(s,u)=W(s^{2},u)$. By (the proof of)
\cite[Theorem 1]{[28]} we have
$W(s^{2},u)C_{0}(s^{2}) = D_{0}(s^{2},u)W(s^{2},u)$
if and only if $\phi(s^{2},u)=0$, so by (\ref{eq:C0C2}) we
find that $\rho_{(s,u)}$ extends to a (necessarily nonabelian)
$\SL(2,\C)$--representation of $G$ if and only if
$\phi(s^{2},u)=0$.

If $\psi : G \to \SL(2,\C)$ is an arbitrary nonabelian
representation it follows by \cite[Lemma 7]{[29]} and
(\ref{eq:konjugering}) that there exists a pair
$(s,u) \in \C^{*} \times \C$ (necessarily satisfying
(\ref{eq:phizero})) such that $\psi$ and $\rho_{(s,u)}$
are equivalent. By the above any such pair is different from
$(\pm 1,0)$ and by \cite[Lemma 8]{[29]} and
(\ref{eq:konjugering}) we then get the final statement of
the theorem.
\end{proof}


If $(s,u) \in \C^{*} \times \C$ with $\phi(s^{2},u)=0$ then
$\rho_{(s,u)}$ is affine if and only if $C_{2}(s)$ and
$D_{2}(s,u)$ have a common eigenvector. But this happens
exactly when $u=0$ or $u=(s-s^{-1})^{2}$.

Let us now restrict to the case where $G$ is the figure $8$
knot group $\pi$. Then
\begin{equation}\label{eq:phifunction}
\phi(t,u)=u^{2}+\left(3-(t+t^{-1})\right)(u+1)
\end{equation}
so in particular $\phi(s^{2},0)=3-s^{2}-s^{-2}=0$ if and only
if $s^{4}-3s^{2}+1=0$ i.e.\ if and only if
$s=\mu_{1}\sqrt{(3+\mu_{2}\sqrt{5})/2}$ for some
$\mu_{1},\mu_{2} \in \{ \pm 1 \}$. If
$u=(s-s^{-1})^{2}=s^{2}+s^{-2}-2$ then
$\phi(s^{2},u) = u^{2} + (3-u-2)(u+1) = u^{2} + 1 - u^{2} = 1$,
so we conclude that $\rho_{(s,u)}$ is affine if and only if
$u=0$ and $s^{4}-3s^{2}+1=0$. Let
$$
\mN = \Hom(\pi,\SL(2,\C))/\SL(2,\C)
$$
be the space of conjugacy classes of
$\SL(2,\C)$--representations of $\pi$ and let $\mN_{\nab}$ be
the subset consisting of classes represented by nonabelian
$\SL(2,\C)$--representations. Moreover, let
\begin{equation}\label{eq:Ntilde}
\tilde{\mN} = \{\, (s,u) \in
        \C^{*} \times \C \, | \, \phi(s^{2},u)=0 \,\},
\end{equation}
and let $\Phi : \tilde{\mN} \to \mN$ be the map which maps
$(s,u)$ to the class represented by $\rho_{(s,u)}$. We have
shown


\begin{corollary}\label{cor:SL(2,C)}
The image of $\Phi$ is $\mN_{\nab}$. If we let
$$
\tilde{\mN}_{0} = \{ \,(\mu_{1}\sqrt{(3+\mu_{2}\sqrt{5})/2},0)
         \,|\,\mu_{1},\mu_{2} \in \{\pm 1\}\,\}
$$
then $\Phi|_{\tilde{\mN}_{0}} : \tilde{\mN}_{0} \to \mN$ is
injective and $\Phi^{-1}(\Phi(s,u))=\{(s,u),(s^{-1},u)\}$
for any $(s,u) \in \tilde{\mN} \sm \tilde{\mN}_{0}$.\HS
\end{corollary}


Recall that $M_{p/q}$ denotes the closed oriented $3$--manifold
obtained by surgery on $S^{3}$ along the figure $8$ knot with
rational surgery coefficient $p/q$. The representation
$\rho_{(s,u)}$, $(s,u) \in \tilde{\mN}$, extends to a
$\SL(2,\C)$--representation of $\pi_{1}(M_{p/q})$ if and only
if
$$
\rho_{(s,u)}(\mu)^{p}\rho_{(s,u)}(\lambda)^{q} = 1.
$$
To analyze this criterion it is an advantage to diagonalize
$\rho_{(s,u)}(\lambda)$. Assume in the following that
$(s,u) \in \tilde{\mN}$. By a rather long but completely
elementary and straightforward calculation we find that
$$
\rho_{(s,u)}(\lambda) = \left(
  \begin{array}{cc} \lambda_{11}(s,u) & \lambda_{12}(s,u) \\
            0 & \lambda_{11}(s^{-1},u) \end{array} \right),
$$
where
$$
\lambda_{11}(s,u) =
-1 + s^{-2} - 2s^{2} + s^{4} + u(s^{-2}-s^{2})
$$
and $\lambda_{12}(s,u) = 2u(1-u)$ if $s^{2}=1$ and
$$
\lambda_{12}(s,u) = \frac{\lambda_{11}(s,u)
              - \lambda_{11}(s^{-1},u)}{s^{2}-1}
$$
for $s^{2} \neq 1$. We note that
$\lambda_{11}(s^{-1},u) = \lambda_{11}(s,u)^{-1}$.

In general, if
$A = \left(\begin{array}{cc} \alpha & \beta \\
       0 & \alpha^{-1} \end{array}\right) \in \SL(2,\C)$,
then $A$ can be diagonalized if and only if $A$ is not
parabolic, i.e.\ if and only if $\tr(A) \neq \pm 2$ or
equivalently if and only if $\alpha \neq \pm 1$ (except, of
course, if $\beta=0$). If $\alpha \neq \pm 1$ then $(1,0)$ is
an eigenvector with eigenvalue $\alpha$ and
$(-\beta/(\alpha-\alpha^{-1}),1)$ is an eigenvector with
eigenvalue $\alpha^{-1}$. If $s^{2}=1$ then
$\lambda_{11}(s,u)=-1$ and $\lambda_{12}(s,u)=\pm i2\sqrt{3}$.
If $s^{2} \neq 1$ then $\lambda_{11}(s,u) = \pm 1$ if and only
if $\lambda_{12}(s,u)=0$. Therefore $\rho_{(s,u)}(\lambda)$ is
diagonalizable (or diagonal) if and only if $s^{2} \neq 1$. In
case $s^{2} \neq 1$ and $\lambda_{12}(s,u) \neq 0$ we have
$$
\frac{\lambda_{12}(s,u)}{\lambda_{11}(s,u)
         -\lambda_{11}(s,u)^{-1}}
= \frac{1}{s^{2}-1} = \frac{s^{-1}}{s-s^{-1}}.
$$
We conclude that if $s^{2} \neq 1$, then $\C^{2}$ has a basis
consisting of a set of common eigenvectors for the matrices
$\rho_{(s,u)}(\mu)$ and $\rho_{(s,u)}(\lambda)$, namely
$u_{1}=(1,0)$ and $u_{2}=(-1/(s^{2}-1),1)$. If we let
$\tilde{\rho}_{(s,u)} : \pi \to \SL(2,\C)$ be the
representation
$\tilde{\rho}_{(s,u)}(\gamma)=U^{-1}\rho_{(s,u)}(\gamma)U$,
where $U \in \SL(2,\C)$ with $j$th column $u_{j}$, we
therefore have
\begin{equation}\label{eq:rhoa1}
\tilde{\rho}_{(s,u)}(x) = \diag\left(s,s^{-1}\right), \qquad
\tilde{\rho}_{(s,u)}(\lambda) =
   \diag\left(\lambda_{11}(s,u),\lambda_{11}(s,u)^{-1}\right).
\end{equation}
In particular, $\rho_{(s,u)} : \pi \to \SL(2,\C)$,
$s^{2} \neq 1$, extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if
\begin{equation}\label{eq:rhosurgery}
s^{-p} = \lambda_{11}(s,u)^{q}.
\end{equation}
Recall here that $\rho_{(s,u)}$ and $\rho_{(s^{-1},u)}$
are equivalent for $(s,u) \in \tilde{\mN} \sm \tilde{\mN}_{0}$,
cf.\ \refcor{cor:SL(2,C)}. But as noted above
$\lambda_{11}(s^{-1},u) = \lambda_{11}(s,u)^{-1}$ in accordance
with (\ref{eq:rhosurgery}). For $(s,u) \in \tilde{\mN}_{0}$
we have $\lambda_{11}(s,u)=1$ and $|s| \neq 1$, so
$\rho_{(s,u)}$ extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if $p=0$.

A direct check shows that if $s^{2}=1$ then $\rho_{(s,u)}$
does not extend to a representation of $\pi_{1}(M_{p/q})$ for
any rational number $p/q$. In fact, if $s = \pm 1$, then
$$
\rho_{(s,u)}(\mu)^{p} = (\pm 1)^{|p|}
  \left(\begin{array}{cc} 1 & p \\ 0 & 1 \end{array}\right)
$$
and
$$
\rho_{(s,u)}(\lambda)^{q} =
       \left(-\left(\begin{array}{cc} 1 & \vep i2\sqrt{3} \\
            0 & 1 \end{array}\right)\right)^{q}
= (-1)^{|q|}\left(\begin{array}{cc} 1 & \vep i2q\sqrt{3} \\
          0 & 1 \end{array}\right)
$$
for a $\vep \in \{-1,1\}$. On the other hand, since
$\lambda_{11}(s,u) = -1$, we have that (\ref{eq:rhosurgery})
is satisfied if $s=1$ and $q$ is even or $s=-1$ and both $p$
and $q$ are odd. For the following we note that if $s^{2}=1$
then $u^{2} + u + 1 = \phi(1,u) = 0$ so $u$ is not real.

We are mostly interested in the $\SU(2)$--representations of
$\pi$. Let in the following $\mM_{\nab}$ be the set of
conjugacy classes of nonabelian $\SU(2)$--representations of
$\pi$.


\begin{proposition}\label{prop:SU(2)}
Let $(s,u) \in \tilde{\mN}$. The representation
$\rho_{(s,u)} : \pi \to \SL(2,\C)$ is $\SL(2,\C)$--equivalent
to a representation  $\pi \to \SU(2)$ if and only if $|s|=1$
and $u$ is real. If we write $s=e^{2\pi i\theta}$,
$\theta \in ]-1/2,1/2]$, then $u \in \{ u_{\pm} \}$, where
$u_{\pm} = u_{\pm}(\theta)$ are the two solutions to
$\phi(e^{4\pi i\theta},u) = 0$, i.e.\
$$
u_{\pm}(\theta) = \cos(4\pi\theta)-\frac{3}{2}
\pm \sqrt{\cos^{2}(4\pi\theta)-\cos(4\pi\theta)-\frac{3}{4}}.
$$
Since $u$ is real we have
$\theta \in [-1/3,-1/6] \cup [1/6,1/3]$.
The representation $\rho_{(e^{2\pi i \theta},u_{\vep})}$,
$\theta \in [-1/3,-1/6] \cup [1/6,1/3]$ and
$\vep \in \{\pm \}$, is $\SL(2,\C)$--equivalent to a
$\SU(2)$--representation $\bar{\rho}_{\theta,\vep}$ which
satisfies
$$
\bar{\rho}_{\theta,\vep}(\mu) = \diag\left(e^{2\pi i \theta},
         e^{-2\pi i\theta}\right),\hspace{.2in}
\bar{\rho}_{\theta,\vep}(\lambda) =
\diag(L_{\vep},L_{\vep}^{-1}),
$$
where $\mu$ and $\lambda$ are the elements of $\pi$
corresponding to the meridian and the preferred longitude of
$K$, and
$$
L_{\pm} = L_{\pm}(\theta) =
   \lambda_{11}\left(e^{2\pi i\theta},u_{\pm}\right)
= - 1 + e^{-4\pi i\theta} - 2e^{4\pi i\theta}
+ e^{8\pi i \theta}
+ u_{\pm}\left(e^{-4\pi i\theta} - e^{4\pi i\theta}\right).
$$
We note that $\bar{\rho}_{-\theta,\vep}$ and
$\bar{\rho}_{\theta,\vep}$ are $\SU(2)$--equivalent. In
particular, the space $\mM_{\nab}$ can be parametrized by the
two arcs
$(e^{2\pi i\theta},u_{+}(\theta))$, $\theta \in [1/6,1/3]$, and
$(e^{2\pi i\theta},u_{-}(\theta))$, $\theta \in [1/6,1/3]$.
These two arcs only coincide at the endpoints, so
topologically $\mM_{\nab}$ is a circle.
\end{proposition}


This proposition follows from \cite[Proposition 4]{[28]}, see
also \cite[Proposition 5.4]{[18]}. For a more geometric
argument determining the topological type of $\mM_{\nab}$,
see \cite{[19]}.

For $\theta \in [-1/3,-1/6] \cup [1/6,1/3]$ and
$\vep \in \{\pm\}$, the representation
$\bar{\rho}_{\theta,\vep}$ extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if
$$
\bar{\rho}_{\theta,\vep}(\mu)^{p}
\bar{\rho}_{\theta,\vep}(\lambda)^{q} = 1,
$$
i.e.\ if and only if
\begin{equation}\label{eq:p/q}
e^{-2\pi ip\theta} = L_{\vep}(\theta)^{q}.
\end{equation}
From this (use e.g.\ (\ref{eq:Lreaima})) we see that


\begin{corollary}
Let $p/q \in \Q$ be arbitrary. The moduli space of irreducible
flat $\SU(2)$--connections on $M_{p/q}$ is a finite set.\HS
\end{corollary}


Let us end this section by finding the abelian
$\SU(2)$--representations of $\pi_{1}(M_{p/q})$ (up to
equivalence). Therefore, let $\theta \in ]-1/2,1/2]$
and let $\rho_{\theta}$ be the assignment
$$
\rho_{\theta}(\mu) =
\diag (e^{2\pi i \theta},e^{-2\pi i \theta}).
$$
By (\ref{eq:pi}) this assignment extends to an abelian
$\SU(2)$--representation of $\pi$ for any
$\theta \in ]-1/2,1/2]$ by letting
$\rho_{\theta}(y) = \rho_{\theta}(x)$. Moreover, any abelian
$\SU(2)$--representation of $\pi$ is $\SU(2)$--equivalent to
$\rho_{\theta}$ for some $\theta \in ]-1/2,1/2]$. For any
$\theta \in ]-1/2,1/2]$ we have $\rho_{\theta}(\lambda)=1$, and
$\rho_{\theta}$ extends to a representation of
$\pi_{1}(M_{p/q})$ if and only if $\rho_{\theta}(\mu)^{p} = 1$,
i.e.\ if and only if $p\theta \in \Z$. If
$A = \left(\begin{array}{cc} 0 & -1 \\
1 & 0 \end{array} \right)$
then $A\rho_{\theta}(\mu)A^{-1} = \rho_{-\theta}(\mu)$ so we
can assume that $\theta \in [0,1/2]$. Note, moreover, that two
matrices $\diag (e^{i \phi},e^{-i \phi})$ and
$\diag (e^{i \psi},e^{-i \psi})$, $\phi,\psi \in ]-\pi,\pi]$,
are conjugate in $\SU(2)$ if and only if $\phi=\psi$ or
$\phi =-\psi$. We conclude


\begin{proposition}\label{prop:SU(2)abelian}
For $p \neq 0$ the set of conjugacy classes of abelian
$\SU(2)$--represen-tations of $\pi_{1}(M_{p/q})$ is given by
$$
\left\{ \; [\rho_{j/|p|}] \; \left| \; j=0,1,\ldots,
    \left[\frac{|p|}{2}\right] \; \right. \right\},
$$
where $[|p|/2]$ is the integer part of $|p|/2$. For $p=0$
the set of conjugacy classes of abelian $\SU(2)$--representations
of $\pi_{1}(M_{p/q})$ is given by
$$
\left\{ \; [\rho_{\theta}] \; \left| \; \theta \in
           [0,\frac{1}{2}] \; \right. \right\},
$$
so topologically this set is a closed interval.\HS
\end{proposition}
