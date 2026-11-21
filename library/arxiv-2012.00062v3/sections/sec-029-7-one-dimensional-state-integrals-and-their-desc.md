---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-029-7-one-dimensional-state-integrals-and-their-desc
section_title: "One-dimensional state-integrals and their descendants"
section_number: 7
pages: 62-65
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.915
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sec.onedim}

In a sense, the results of our paper are not about the asymptotics and
resurgence of complex Chern--Simons theory, but rather involve power
series and $q$-difference equations that arise from $K_2$-Lagrangians
(clearly advocated in Kontsevich's talks~\cite{kontsevich-talk}), or
from symplectic matrices (advocated in~\cite[Sec.7]{GZ:kashaev}). The
connection with complex Chern--Simons theory comes via ideal
triangulations of a 3-manifold with torus boundary components, a
concept introduced by Thurston for the study of complete hyperbolic
structures and their deformations~\cite{Thurston}.  The gluing
equations of such triangulations are encoded by matrices which are the
upper half of a symplectic matrix (see Neumann-Zagier~\cite{NZ}). The
upper half of these symplectic matrices define state-integrals, as well 
as the asymptotic series $\Phi(x;\tau)$ (this was the approach
taken in~\cite{DG}) and the 3D-index (see~\cite{DGG1}).

In this section we discuss briefly general one-dimensional
state-integrals and their descendants, and their asymptotic series. We
will not aim for maximum generality, but instead consider the
one-dimensional state-integral
\begin{equation}
  \label{I1d}
  Z_{A,r}(u,t;\tau)
  =\int_{\BR+\ri 0}
  \left(\prod_{j=1}^r\Phi_\bb(v+u_j)\right)
  \re^{-A\pi\ri v^2 + 2\pi\ri v t} \rd v \,,
\end{equation}
where $u=(u_1,\dots,u_r) \in \BC^r$ with $|\Im u_j| < |\Im c_\bb|$
(this ensures that all poles of the integrand are above the real
axis), $t \in \BC$ and $A$ and $r$ integers with $r>A>0$. (This
ensures that the integrand decays exponentially at infinity, hence the
integral is absolutely convergent.) We have already encountered two
special cases in Equations~\eqref{Z41x-desc} and~\eqref{Z52x-desc}:
\begin{align}
  \label{I4152a}
  \knot{4}_1:
  & \,\, (A,r)=(1,2), \,\, (u_1,u_2) = (u,0), \,\, w = -2u, \\
  \label{I4152b} \knot{5}_2:
  & \,\, (A,r)=(2,3), \,\, (u_1,u_2,u_3) = (0,u,-u),
    \,\, w = 0 \,.
\end{align}
We are interested in the descendants of $Z$ defined by
\begin{equation}
  \label{I1dd}
  z_{A,r,m,\mu}(u,t;\tau) = (-1)^{m+\mu} \,
  q^{-\frac{1}{2}m} \, \tq^{-\frac{1}{2}\mu} \,
  Z_{A,r}(u,t - m \ri \bb + \mu \ri \bb^{-1};\tau)
\end{equation}
for integers $m$ and $\mu$, where the extra factor was inserted to
simplify the formulas below.

We will express the factorization of the state-integral~\eqref{I1dd}
in terms of the auxiliary function
\begin{equation}
  \label{Gar}
  G_{A,r}(y,z;q)
  =\frac{1}{(q;q)_\infty} \sum_{n=0}^\infty
  (-1)^{An} q^{\frac{A}{2}n(n+1)} z^n \prod_{j=1}^{r}(q^{1+n}y_j;q)_\infty 
\end{equation}
for $y=(y_1,\dots,y_r)$ and its specialization 
\begin{equation}
  \label{bmxw}
  b^{(k)}_{m}(x,w;q)
  
  = \frac{1}{x_k^{m}}
  G_{A,r}\left(\frac{1}{x_k} x, x_k^{-A} w^{-1} q^{m};q \right)
  q\end{equation}
for $x=(x_1,\dots,x_r)$ 
and its renormalization 
\begin{equation}
  \label{Bmxw}
  B^{(k)}_{m}(x,w;q) =
  \th(-q^{-1/2}x_k;q)^{-A+1}\th(-q^{-1/2}x_k w;q)^{-1}\th(w;q)
  b^{(k)}_{m}(x,w;q)
\end{equation}
for $k=1,\dots,r$.

\begin{theorem}
  \label{thm.Zfac}
  \rm{(a)} The descendant state-integral can be expressed in terms of
  the descendant holomorphic blocks by
\begin{equation}
  \label{Z-fac}
  z_{A,r,m,\mu}(u,t;\tau) 
  =
  B_{-\mu}(\tx,\tw;\tq^{-1})^T \Delta(\tau) B_m(x,w;q),
  \qquad (m, \mu \in \BZ)
\end{equation}
where 
\begin{equation}
  x_j = \re^{2\pi \bb u_j},\quad \tx_j =
  \re^{2\pi \bb^{-1}u_j},\quad
  w = \re^{2\pi\bb t},\quad \tw = \re^{2\pi\bb^{-1}t} \,.
\end{equation}
and 
\begin{equation}
\label{Dr}
\Delta(\tau) =


\re^{-\frac{\ri\pi}{4}+\frac{(A-2)\ri\pi}{12}(\tau+\tau^{-1})}\md{1}
\end{equation}
and $B_m(x,w;q)=(B^{(1)}_m(x,w;q), \dots, B^{(r)}_m(x,w;q))^T$. 
Consider the matrix $W_m(x,w;q)$ defined by
\begin{equation}
  \label{Wrm}
  W_m(x,w;q) =
  \begin{pmatrix}
    B^{(1)}_{m}(x,w;q) & \ldots & B^{(r)}_{m}(x,w;q) \\
    \vdots & & \vdots \\
    B^{(1)}_{m+r-1}(x,w;q) & \ldots & B^{(r)}_{m+r-1}(x,w;q)
  \end{pmatrix}
\end{equation}
\rm{(b)} The entries of $W_m(x,w;q)$ are holomorphic
functions of $|q| \neq 1$ and meromorphic functions of $(x,w) \in
(\BC^*)^r \times \BC^*$
with poles in $x_j \in q^\BZ$ (for $j=1,\dots,r$) and
$w \in q^\BZ$ of order at most $r$. 
  \newline
  \rm{(c)} The columns of $W_m(x,w;q)$ are a basis of solutions of the
  linear $q$-difference equation $\Bhat(S_m,q^m,x,w,q) f_m(x;q)=0$ for
  $|q| \neq 1$ and $m \in \BZ$ where 
    \begin{equation}
  \label{bkm}
  \Bhat(S_m,q^m,x,w,q) = \prod_{k=1}^r(1-x_i S_m) - (-q)^A w^{-1} q^{m} S_m^A \,.
  \end{equation}
  In particular, $m \mapsto z_{A,r,m,\mu}(u,t;\tau)$ is annihilated by
  the operator $\Bhat(S_m,q^m,x,w,q)$.
\end{theorem}

\begin{proof}
  For part (a), summing up all the residues of the integrand
  of~\eqref{I1d} in the upper half-plane as in~\cite{GK:qseries}, we
  find that 
\begin{align}
  \label{eq:Ira-fac}
  z_{A,r,m,\mu}(u,t;\tau)
  &=
    \re^{-\frac{\pi\ri}{12} +\frac{1}{3}\pi\ri c_\bb^2+2\pi\ri c_\bb t}
    \sum_{k=1}^r \re^{-A\pi\ri(u_k-c_\bb)^2-2\pi\ri u_k t} 
    b^{(k)}_{m}(x,w;q) b^{(k)}_{\mu}(\tx,\tw;\tq^{-1}) \\
    \label{eq:Ira-fac2}
  &=
    \re^{-\frac{\pi\ri}{12}+\frac{1}{3}\pi\ri c_\bb^2+\frac{\pi\ri}{12}(A-1)(\tau+\tau^{-1})}
    \sum_{k=1}^r B^{(k)}_{m}(x,w;q) B^{(k)}_{\mu}(\tx,\tw;\tq^{-1})
  \end{align}
  The last equation follows from~\eqref{ebx2} (which takes care of
  $\re^{-A \pi \ri (u_k-c_\bb)^2}$) and~\eqref{ebx3} (which takes
  care of the $t$-terms under the assumption that $u_k t = \rho_k u$
  and $t = \rho u$ for integers $\rho$ and $\rho_k$) 

  For part (b), note that $G_{A,r}(y,z;q)$ is symmetric with respect
  to permutation of the coordinates of $y$ and that the specialization
  to $y_r=1$ is given by
\begin{equation}
\label{Garr}
 G_{A,r}(y,z;q)|_{y_r=1} 
    = \sum_{n=0}^\infty
    (-1)^{An} \frac{q^{\frac{A}{2}n(n+1)}}{(q;q)_n} z^n
    \prod_{j=1}^{r-1}(q^{1+n}y_j;q)_\infty, \qquad (|q| \neq 1)\,.
\end{equation}
It follows that $G_{A,r}(y,z;q)|_{y_r=1}$ is holomorphic for $(y,z) \in
\BC^{r-1} \times \{1\} \times \BC$ when $|q|<1$ and meromorphic in
$(y,z) \in (\BC^*)^{r-1} \times \{1\} \times \BC^*$ with
poles in $y_j \in q^\BN$ for $j=1,\dots,r$. Since $b^{(k)}_m(x,w;q)$
are expressed in terms of a specialization of $G_{A,r}(y,z;q)|_{y_r=1}$,
part (b) follows. 

  Part (c) follows from Equation~\eqref{bmxw} and the fact (proven
  by a standard creative telescoping argument) that the function
  $z \mapsto G_{A,r}(y,z;q)$ is annihilated by the operator
  \begin{equation}
  \label{Gzrec}
  \prod_{k=1}^r (1-y_k L_z) - (-q)^A z L_z^A 
  \end{equation}
  where $L_z$ shifts $z$ to $q z$.
\end{proof}




\bibliographystyle{hamsalpha}
