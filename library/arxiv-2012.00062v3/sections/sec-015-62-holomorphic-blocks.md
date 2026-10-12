---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-015-62-holomorphic-blocks
section_title: "Holomorphic blocks"
section_number: 6.2
pages: 47-60
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
text_source: latex
latex_prose_ratio: 0.673
latex_coverage_ratio: 0.723
---
\label{sub.41holo}



In this section we give the definition of the holomorphic blocks (and
their descendants) which factorize the state-integral (and its
descendants), and discuss their analytic properties, and their linear
$q$-difference equations.  Note that in this section, as well as in
Section~\ref{sub.41near1}, all the statements are theorems, whose
proofs we provide.

Motivated by the state-integral $Z_{\knot{4}_1}(u;\tau)$ of the
$\knot{4}_1$ knot given in~\eqref{Z41x}, and by the descendant
state-integral $Z_{\knot{4}_1,m,\mu}(0;\tau)$ given
in~\eqref{Z410-desc}, we introduce the descendant state-integral of
the $\knot{4}_1$ knot 
\begin{equation}
  \label{Z41x-desc}
  Z_{\knot{4}_1,m,\mu}(u;\tau) =
  
  \re^{-2 \pi \ri u^2} 
  \int_{\mc{D}} \Phi_\bb(v) \, \Phi_\bb(u+v)
  \, \re^{-\pi \ri (v^2+4uv) + 2\pi(m \bb - \mu \bb^{-1})v} \, \rd v
\end{equation}
for integers $m$ and $\mu$, which agrees with the Andersen-Kashaev
invariant of the $\knot{4}_1$ knot when $m=\mu=0$. Here the contour
$\mc{D}$ was introduced in \eqref{Z410-desc}. It is expressed in terms
of two descendant holomorphic blocks, which we denote by $A_m$ and
$B_m$ instead of $B^{\s_1}_m$ and $B^{\s_2}_m$, in order to simplify
the notation.  For $|q| \neq 1$, $A_m(x;q)$ and $B_m(x;q)$ are given
by
\begin{subequations}
  \begin{align}
    \label{41Am}
    A_m(x;q) &= \th(-q^{\frac{1}{2}}x;q)^{-2}
               x^{2m} J(q^m x^2, x; q)\,, \\
    \label{41Bm}
    B_m(x;q) &= \th(-q^{-\frac{1}{2}}x;q)
               x^m J(q^m x, x^{-1}; q)\,,
  \end{align}
\end{subequations}
where $J(x,y;q^\ve):=J^\ve(x,y;q)$ for $|q|<1$ and $\ve=\pm$ is the
$q$-Hahn Bessel function
\begin{subequations}
\begin{align}
  \label{J41p}
  J^+(x,y;q) & = (qy;q)_\infty \sum_{n=0}^\infty (-1)^n
               \frac{q^{\frac{1}{2}n(n+1)} x^n}{(q;q)_n (qy;q)_n}\,, \\
  \label{J41n}
  J^-(x,y;q) & = \frac{1}{(y;q)_\infty}
               \sum_{n=0}^\infty (-1)^n \frac{q^{\frac{1}{2}n(n+1)}
               x^n y^{-n}}{ (q;q)_n (qy^{-1};q)_n}
               \,.
\end{align}
\end{subequations}

The next theorem expresses the descendant state-integrals bilinearly
in terms of descendant holomorphic blocks.

\begin{theorem}
  \label{thm.41a}
  \rm{(a)} The descendant state-integral can be expressed in terms of
  the descendant holomorphic blocks by 
  \begin{align}
    Z_{\knot{4}_1,m,\mu}(\ub;\tau) 
    =& (-1)^{m+\mu}q^{m/2}\tq^{\mu/2} \Big(
    \re^{-\frac{3\pi\ri}{4} -\frac{\pi\ri}{6}(\tau+\tau^{-1})}
      A_m(x;q) A_{-\mu}(\tx;\tq^{-1}) \\ & +
    \re^{\frac{3\pi\ri}{4}+\frac{\pi\ri}{3}(\tau+\tau^{-1})}
      B_{m}(x;q) B_{-\mu}(\tx;\tq^{-1})\Big) \,.
    \label{41x-desc-fac}
  \end{align}
  \rm{(b)} The functions $A_m(x;q)$, $B_m(x;q)$ are holomorphic
  functions of $|q| \neq 1$ and meromorphic functions of $x \in \BC^*$
  with poles in $x \in q^\BZ$ of order at most $1$.  \newline
  \rm{(c)} Let
  \begin{equation}
    W_m(x;q) = \begin{pmatrix}
      A_{m}(x;q) & B_{m}(x;q)  \\
      A_{m+1}(x;q) & B_{m+1}(x;q) 
    \end{pmatrix} \qquad (|q| \neq 1) \,.
    \label{eq:Wm}
  \end{equation}
  For all integers $m$ and $\mu$, the state-integral
  $Z_{\knot{4}_1,m,\mu}(u;\tau)$ and the matrix-valued function
  \begin{equation}
    W_{m,\mu}(u;\tau) = W_{-\mu}(\tx;\tq^{-1}) \Delta(\tau) 
    W_m(x;q)^T \,,
    \label{W41x-desc}
  \end{equation}
  where
  \begin{equation}
    \label{D41}
    \Delta(\tau) = \begin{pmatrix}
      \re^{-\frac{3\pi\ri}{4}-\frac{\pi\ri}{6}(\tau+\tau^{-1})}&0\\
      0&\re^{\frac{3\pi\ri}{4}+\frac{\pi\ri}{3}(\tau+\tau^{-1})}
    \end{pmatrix} \,,
  \end{equation}
  are holomorphic functions of $\tau \in \BC'$ and entire
  functions of $u \in \BC$. 
\end{theorem}

\begin{proof}
  Part (a) follows by applying the residue theorem to the
  state-integral~\eqref{Z41x-desc}, along the lines of the proof of
  Theorem 1.1 in~\cite{GK:qseries}. A similar result was stated in
  \cite{dimofte-state}.

  Part (b) follows from the fact that when $|q|<1$, the ratio test
  implies that $J^+(x,y;q)$ is an entire function function of
  $(x,y) \in \BC^2$ and $J^-(x,y;q)$ is a meromorphic function of
  $(x,y)$ with poles in $y \in q^{\BZ}$.

  For part (c), one uses parts (a) and (b) to deduce that
  $W_{m,\mu}(u;\tau)$ is holomorphic of $\tau\in \IC'$ and meromorphic in
  $u$ with potential simple poles at $\ri \bb \BZ + \ri \bb^{-1} \BZ$.
  An expansion at these points, done by the method of
  Section~\ref{sub.41near1}, demonstrates that the function is analytic
  at the points $\ri \bb \BZ + \ri \bb^{-1} \BZ$.
\end{proof}

Note that the summand of $J^+$ (a proper $q$-hypergeometric function)
equals to that of $J^-$ after replacing $q$ by $q^{-1}$. This implies
that $J^\pm$ have a common annihilating ideal $\calI_J$ with respect
to $x,y$ which can be computed (rigorously, along with a provided
certificate) using the creative telescoping method of
Zeilberger~\cite{PWZ} implemented in the \texttt{HolonomicFunctions}
package of Koutschan~\cite{Koutschan,Koutschan:holofunctions}.  Below,
we will abbreviate this package by~\texttt{HF}.

\begin{lemma}  
  \label{lem.annJ}
  The annihilating ideal of $\calI_J$ of $J^\pm$ is given by
  \begin{equation}
    \label{annJ}
    \calI_J = \langle
    (-x + y) + x S_y - y S_x, \,\, 1 + (-1 - x + q y) S_y + x S_y^2
    \rangle
  \end{equation}
  where $S_x$ and $S_y$ are the shifts $x$ to $qx$ and $y$ to $qy$.
\end{lemma}

The next theorem concerns the properties of the linear $q$-difference
equations satisfied by the descendant holomorphic blocks.

\begin{theorem}
  \label{thm.41b}
  \rm{(a)} The pair $A_m(x;q)$ and $B_m(x;q)$ are $q$-holonomic
  functions in the variables $(m,x)$ with a common annihilating ideal
  \begin{equation}
    \label{ann41}
    \calI_{\knot{4}_1} = \langle q^m x^2 + (-q^m + q^{1 + 2 m} x^2) S_m + x^3
    S_x,  \, 
    (1-x^{-1}S_m)(1-x^{-2}S_m) + q^{1+m} S_m \rangle
  \end{equation}
  where $S_m$ is the shift of $m$ to $m+1$ and $S_x$ is the shift of
  $x$ to $q x$.  $\calI_{\knot{4}_1}$ has rank 2 and the two functions form
  a basis of solutions of the corresponding system of linear equations.
  \newline
  \rm{(b)} As functions of an integer $m$, $A_m(x;q)$ and
  $B_m(x;q)$ form a basis of solutions of the linear $q$-difference
  equation $\Bhat_{\knot{4}_1}(S_m,x,q^m,q) f_m(x;q) = 0$ for $|q| \neq 1$
  where 
  \begin{equation}
    \label{rec41m}
    \Bhat_{\knot{4}_1}(S_m,x,q^m,q) =  (1-x^{-1}S_m)(1-x^{-2}S_m) + q^{1+m} S_m \,.
  \end{equation}
  \rm{(c)} The Wronskian $W_m(x;q)$ of~\eqref{rec41m},
  defined in ~\eqref{eq:Wm}, satisfies
  \begin{equation}
    \label{W410}
    \det(W_m(x;q)) = x^{3m+3} 
    \qquad
    (m \in \BZ) \,.
  \end{equation}
  \rm{(d)} The Wronskian satisfies the orthogonality relation
  \begin{equation}
    \label{WW41b}
    W_{-1}(x;q) \,
    \begin{pmatrix}
      1 & 0 \\
      0 & -1
    \end{pmatrix}
    \,  W_{-1}(x;q^{-1})^T =
    \begin{pmatrix}
      x^{-2}+x^{-1}-1 & 1\\
      1 & 0
    \end{pmatrix} \,.
  \end{equation}
  It follows that for all integers $m$ and $\ell$ 
  
  
  \begin{equation}
    \label{WW41}
    
    
    W_m(x;q) \,
    \begin{pmatrix}
      1 & 0 \\
      0 & -1
    \end{pmatrix} \, W_\ell(x;q^{-1})^T \in \GL(2,\BZ[q^\pm, x^\pm])
  \end{equation}
  \rm{(e)} As functions of $x$, $A_m(x;q)$ and $B_m(x;q)$ form a basis
  of a linear $q$-difference equation
  $\hat A_{\knot{4}_1} (S_x,x,q^m,q) f_m(x;q) =0$
where 
  \begin{equation}
    \label{rec41x}
    \hat A_{\knot{4}_1} (S_x,x,q^m,q) = \sum_{j=0}^2 C_j(x,q^m,q) S_x^j \,,
  \end{equation}
  $S_x$ is the operator that shifts $x$ to $qx$ and
  \begin{subequations}
    \begin{align}
      \label{rec41x0}
      C_0 =
      &q^{2 + 3 m} x^2 (-1 + q^{3 + m} x^2) \\
      \label{rec41x1}
      C_1 =
      & -q^m (-1 + q^{2 + m} x^2) (1 - q x - q^{1 + m} x^2 - q^{3 + m} x^2 - 
        q^{3 + m} x^3 + q^{4 + 2 m} x^4) \\ 
      \label{rec41x2}
      C_2 =
      & q^2 x^2 (-1 + q^{1 + m} x^2) \,.
    \end{align}
  \end{subequations}
  \rm{(f)} The Wronskian of~\eqref{rec41x}
  \begin{equation}
    \label{W41x}
    \calW_m(x;q) = \begin{pmatrix}
      A_{m}(x;q) & B_{m}(x;q)  \\
      A_{m}(qx;q) & B_{m}(qx;q) 
    \end{pmatrix}, \qquad (|q| \neq 1)
  \end{equation}
  satisfies
  \begin{equation}
    \label{detW41x}
    \det(\calW_m(x;q)) = q^m x^{3m}(1-q^{m+1} x^2) \qquad (m \in \BZ) \,.
  \end{equation}
\end{theorem}

\begin{proof}
  Since $A_m(x;q)$ and $B_m(x;q)$ are given in terms of $q$-proper
  hypergeometric multisums, it follows from the fundamental theorem of
  Zeilberger~\cite{Zeil:holo,WZ,PWZ} (see also~\cite{GL:survey}) that
  they are $q$-holonomic functions in both variables $m$ and $x$.
  Part (a) follows from an application of the \texttt{HF} package of
  Koutschan~\cite{Koutschan, Koutschan:holofunctions}.

  Part (b) follows from the \texttt{HF} package. The
  fact that they are a basis follows from (c).

  For part (c), Equation~\eqref{rec41m} implies that the determinant of
  the Wronskian satisfies the first order
  equation $\det(W_{m+1}(x;q))=x^3\det(W_{m}(x;q))$
  (see~\cite[Lem.4.7]{GK:74}). It follows that
  $\det(W_m(x;q))=x^{3m}\det(W_0(x;q))$ with initial condition a
  function of $x$ given by Swarttouw~\cite{MR2714507} 
  \begin{equation}
    \label{W4100}
    \det(W_0(x;q)) = x^3 
    \qquad
    (|q| \neq 1) \,.
  \end{equation}
  We recall the details of the proof which will be useful in the case
  of the $\knot{5}_2$ knot.  When $|q|<1$, the $q$-Hahn Bessel function
  $J(x,y;q)$ satisfies the recursion relation
  \begin{equation}
    y J(qx,y;q) - (1+y-x)J(x,y;q) + J(q^{-1}x,y;q) = 0.
    \label{eq:J-rec1}
  \end{equation}
  This follows from~\cite{MR2714507}, and can also be proved
  using the \texttt{HF} package. It then follows that
  \begin{equation}
    \cJ_{\nu,1}(z;q) := J(z,q^\nu;q), \quad
    \cJ_{\nu,2}(z;q) := z^{-\nu}J(q^{-\nu}z,q^{-\nu};q)
  \end{equation}
  are two independent solutions to
  \begin{equation}
    q^\nu \cJ(qz;q) - (1+q^\nu-x)\cJ(z;q) + \cJ(q^{-1}z;q) = 0.
  \end{equation}
  The corresponding Wronskian
  \begin{equation}
    \cW_\nu(z;q) =
    \begin{pmatrix}
      \cJ_{\nu,1}(z;q) & \cJ_{\nu,2}(z;q)\\
      \cJ_{\nu,1}(qz;q) & \cJ_{\nu,2}(qz;q)
    \end{pmatrix}
  \end{equation}
  satisfies the recursion relation (see~\cite[Lem.4.7]{GK:74})
  \begin{equation}
    \det\cW_\nu(z;q) = q^{-\nu} \det\cW_\nu(q^{-1}z;q)
  \end{equation}
  which implies that the determinant of $U(z;q) = z^\nu \cW_\nu(z;q)$ is
  an elliptic function
  \begin{equation}
    \det U(qz;q) = \det U(z;q).
  \end{equation}
  It can be computed by the following limit
  \begin{align}
    \det U(z;q) =
    &\lim_{k\rightarrow \infty} \det U(q^k z;q) = \lim_{z\rightarrow 0}
      \det U(z;q)\nn  =
    &\lim_{z\rightarrow 0} \Big(
      q^{-\nu}J(z,q^\nu;q)J(q^{1-\nu}z,q^{-\nu};q) -
      J(q^{-\nu}z,q^{-\nu};q)J(qz,q^\nu;q)
      \Big) \nn =
    &(q^{-\nu}-1)(q^{1+\nu};q)_\infty(q^{1-\nu};q)_\infty,
  \end{align}
  where in the last step we just used the $q$-expansion definition of
  the $q$-Hahn Bessel function.  We thus have
  \begin{equation}
    \label{zcw}
    z^\nu \det \cW_\nu(z;q) = -(q q^\nu;q)_\infty(q^{-\nu};q)_\infty.
  \end{equation}
  Using the substitution
  \begin{equation}
    z\mapsto x^2,\quad z^\nu \mapsto x
  \end{equation}
  in the above equation and cancelling with the
  $\theta$-prefactors of $A_m(x;q)$ and $B_m(x;q)$ we
  obtain Equation~\eqref{W4100} for $|q|<1$.
  The case of $|q|>1$ can be obtained by analytic continuation on both
  sides of \eqref{W4100}.

  For part (d), Equation~\eqref{rec41m} implies that
  \begin{equation}
    W_{m+1}(x;q) =
    \begin{pmatrix}
      0&1\\-x^3&x^2+x-q^{1+m}x^3
    \end{pmatrix} W_m(x;q) \,.
    \label{eq:W41rec}
  \end{equation}
  Hence, Equation~\eqref{WW41} follows from~\eqref{WW41b}. The
  latter is a direct consequence of the analytic continuation formula
  \begin{equation}
    J(x,y;q) = \theta(-q^{1/2}y;q)J(y^{-1}x,y^{-1};q^{-1})
  \end{equation}
  which one easily sees by comparing \eqref{J41p} and \eqref{J41n}.

  Part (e) follows from the \texttt{HF} package. The
  fact that they are a basis follows from (f).

  For part (f), since $A_m(x;q)$ (as well as $B_m(x;q)$) are
  annihilated by the first generator of~\eqref{ann41}, it follows that
  \begin{equation}
    q^m x^2 A_m(x;q) -q^m (1 - q^{1 + m} x^2) A_{m+1}(x;q)
    + x^3 A_m(qx;q) =0 \,.
  \end{equation}
  After solving for the above for $A_m(qx;q)$ (and same for
  $B_m(qx;q)$) and substituting into the Wronskian~\eqref{W41x}, it
  follows that the two Wronskians are related by
  \begin{equation}
    \label{W41xm}
    \calW_m(x;q) =
    \begin{pmatrix} 1 & 0 \\ -q^m x^{-1} & q^m x^{-3}(1-q^{1+m} x^2)
    \end{pmatrix}
    W_m(x;q) \,.
  \end{equation}
  After taking determinants, it follows that
  \begin{equation}
    \det(\calW_m(x;q)) = q^m x^{-3} (1 - q^{1 + m} x^2)\det(W_m(x;q))
    \label{detW41xm}
  \end{equation}
  This, together with~\eqref{W410} concludes the proof of~\eqref{detW41x}.
\end{proof}

We now come to Conjecture~\ref{conj.ann} concerning a refinement of
the $\Ahat$-polynomial.  
Combining Theorems~\ref{thm.41a} and~\ref{thm.41b} we obtain explicit
linear $q$-difference equations for the descendant integrals with respect
to the $u$ and the $m$ variables. To simplify our presentation
keeping an eye on Equation~\eqref{41x-desc-fac}, let us define
a normalized version of the descendant state-integral by
\begin{equation}
  \label{Z41r}
  z_{\knot{4}_1,m,\mu}(u;\tau) =
  (-1)^{m+\mu}q^{-m/2}\tq^{-\mu/2}
  Z_{\knot{4}_1,m,\mu}(u;\tau) \,.
\end{equation}

\begin{theorem}
  \label{thm.41c}\rm
  $z_{\knot{4}_1,m,k}(\ub;\tau)$ is a $q$-holonomic function of $(m,u)$
  with annihilator ideal $\calI_{\knot{4}_1}$ given in~\eqref{ann41}.
  As a function of $u$ (resp., $m$) it is annihilated by the operators
  $\Ahat_{\knot{4}_1}(S_x,x,q^m,q)$ and
  $\Bhat_{\knot{4}_1}(S_m,x,q^m,q)$ (given respectively
  by~\eqref{rec41x} and~\eqref{rec41m}), whose classical limit is
   \begin{equation}
   \begin{aligned}
     &  \Ahat_{\knot{4}_1}(S_x,x,q^m,1)\\
     & = (-1 + q^{m} x^2) (x^2 S_x^2 -q^m (1 - x -2 q^{m} x^2 - q^{m}
     x^3 + q^{2 m} x^4) S_x + q^{3 m} x^2)
 \end{aligned}
  \end{equation}
  and
  
  \begin{equation}
    \Bhat_{\knot{4}_1}(S_m,x,q^m,1) = (1-x^{-1}S_m)(1-x^{-2}S_m) + q^m S_m.
  \end{equation}
 
  $\Ahat_{\knot{4}_1}(S_x,x,1,1)$ is the $A$-polynomial of the knot,
  $\Ahat_{\knot{4}_1}(S_x,x,1,q)$ is the (homogeneous part) of the
  $\Ahat$-polynomial of the knot and $\Bhat_{\knot{4}_1}(x^2y,x,1,1)$
  is the defining equation of the curve~\eqref{41critb}.
\end{theorem}

Note that although the two equations~\eqref{rec41m} and~\eqref{rec41x}
look quite different, they come from the common annihilating
ideal~\eqref{ann41} of rank $2$.  This explains their common order,
assuming that the ideal is generic. The annihilating ideal is easier
to describe than the $S_m$-free element~\eqref{rec41x} of it. In fact,
the first generator of $\calI_{\knot{4}_1}$ expresses $S_x$ as a
polynomial in $S_m$, and eliminating $S_m$, one obtains
equation~\eqref{rec41x} from~\eqref{rec41m}.  The characteristic
variety of $\calI_{\knot{4}_1}$ is a complex is a 2-dimensional
complex surface in $(\BC^*)^4$ and its intersection with a complex
3-torus contains two special curves, namely the $A$-polynomial and the
$B$-polynomial of the $\knot{4}_1$ knot.


\subsection{Taylor series expansion at $u=0$}
\label{sub.41near1}

The descendant state-integral is a meromophic function of $u$ which is
analytic at $u=0$ and factorizes in terms of descendant holomorphic
blocks~\eqref{41x-desc-fac}. In this section we compute the Taylor
series of the holomorphic blocks and of the state-integral at $u=0$
and show how the factorization of the descendant state-integral
\eqref{41x-desc-fac} reproduces~\eqref{410-desc-fac}.

We begin with some general comments valid for descendant holomorphic
blocks and state-integrals.  Since the descendant holomorphic blocks
are products of theta functions times $q$-hypergeometric sums, we need
to compute the Taylor expansion of each piece. For Taylor expansion of
the $q$-hypergeometric sums, we
\begin{subequations}
\begin{align}
  &\phi_n(u):=\frac{(q^{1+n}\re^u;q)_\infty}{(q^{1+n};q)_\infty}
    =\exp\left(-\sum_{l=1}^\infty \frac{1}{l!}E_l^{(n)}(q) u^l \right)
    \label{eq:phin}\\
  &\wt{\phi}_n(u):=\frac{(\tq;\tq)_\infty}{(\tq\re^u;\tq)_\infty}
    \frac{(\tq^{-1};\tq^{-1})_n}{(\tq^{-1}\re^u;\tq^{-1})_n}
    =\exp\left(\sum_{l=1}^\infty
    \frac{1}{l!}\wt{E}_l^{(n)}(\tq) u^l\right)
    \label{eq:tphin}
  \end{align}
\end{subequations}
from~\cite[Prop.2.2]{GK:qseries}, where
\begin{equation}
\label{En}
E_l^{(n)}(q)=\sum_{s=1}^\infty \frac{s^{l-1} q^{s(n+1)}}{1-q^s} 
\end{equation}
and
\begin{align}
  \wt{E}_l^{(n)}(\tq) =
  \begin{cases}
    -n+E_l^{(n)}(\tq) \quad &l=1\\
    E_l^{(n)}(\tq)\quad &l>1\;\text{odd}\\
    2E_l^{(0)}(\tq) - E_l^{(n)}(\tq)\quad &l>1\;\text{even} \,.
  \end{cases} 
\end{align}
For the Taylor series of the theta functions, we use the well-known
identity that expresses them in terms of quasi-modular forms (see,
eg.~\cite[Sec.8, Eqn(76)]{Za:quasimod}, or alternatively observe that
the theta functions that appear in the bilinear expressions of the
holomorphic blocks are exponentials of quadratic and linear forms in
$u$; see for instance~\eqref{ebx2}--\eqref{ebx3}.  Yet alternatively
(and this is the method that we will use below), when $r$ and $s$ are
nonzero integers with $r$ odd and positive, we can use the identity
\begin{equation}
  \label{thrs}
  \th(-q^{\frac{r}{2}} x^s;q)
  =(-1)^{\frac{r+1}{2}}q^{\frac{r^2-1}{8}}x^{-\frac{s(r+1)}{2}}(1-x^s)
  \phi_0(su)\phi_0(-su)  
  
\end{equation}
whereas when $r$ is odd and negative, we can use the $q$-difference
equation~\eqref{recth} to bring it to the cass of $r$ odd and positive.

One last comment is that the descendant holomorphic blocks are in
general meromorphic functions of $u$. However, their bilinear
combination that appears in the descendant state-integrals is regular
at $u=0$.

We now give the details of the Taylor series expansion of
$Z_{\knot{4}_1,m,\mu}(u;\tau)$ and of the descendant holomorphic
blocks for the $\knot{4}_1$ knot.
Using the definition of $J(x,y;q)$ and~\eqref{eq:phin}--\eqref{eq:tphin},
we find
\begin{align}
  A_m(\re^u;q)
  
  &= (1-\re^{-u})^{-2}(q;q)_\infty^{-3}\phi_0(u)^{-2}\phi_0(-u)^{-2}
  \sum_{n=0}^\infty \frac{q^{nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \phi_n(u) \re^{(2n+2m)u} \nn
  &= u^{-2}(q;q)_\infty^{-3}
    \left(\alpha^{(m)}_0(q)+u\alpha^{(m)}_1(q)+\cO(u^2)\right)
\label{eq:A-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\alpha^{(m)}_0(q) = G_m^0(q),\label{eq:a0-41}\\
  &\alpha^{(m)}_1(q) =
    \sum_{n=0}^\infty \frac{q^{nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    (1+2n+2m-E_1^{(n)}(q)),\label{eq:a1-41}
\end{align}
\end{subequations}
and
\begin{align}
  B_m(\re^u;q)
  
  &= (1-\re^u)(q;q)_\infty^3\phi_0(u)\phi_0(-u)
    \sum_{n=0}^\infty \frac{q^{nm}}
    {(q;q)_n(q^{-1};q^{-1})_n}
    \phi_n(-u) \re^{(n+m)u} \nn
  &= -u(q;q)_\infty^3
    \left(\beta^{(m)}_0(q)+u\beta^{(m)}_1(q)+\cO(u^2)\right)
    \label{eq:B-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\beta^{(m)}_0(q) = G_m^0(q),\label{eq:b0-41}\\
  &\beta^{(m)}_1(q) =
    \sum_{n=0}^\infty \frac{q^{nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \left(\frac{1}{2}+n+m+E_1^{(n)}(q)\right).\label{eq:b1-41}
\end{align}
\end{subequations}
We notice that
\begin{equation}
  \beta^{(m)}_1(q) -\alpha^{(m)}_1(q) =
  
  -\frac{1}{2} G_m^1(q).
\end{equation}
Similarly, using the definition of $J(x,y;q^{-1})$, we find
\begin{align}
  A_m(\re^u;q^{-1})
  &=

    (1-\re^u)(q;q)_\infty^3\phi_0(u)^2\phi_0(-u)^2
    \sum_{n=0}^\infty\frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \wt{\phi}_n(u)\re^{(2n+2m)u} \nn
  &=
    -u(q;q)_\infty^3\left(\wt{\alpha}^{(m)}_0(q)+u
    \wt{\alpha}^{(m)}_1(q) + \cO(u^2)\right)
    \label{eq:tA-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\wt{\alpha}^{(m)}_0(q) = G_{-m}^0(q),\label{eq:ta0-41}\\
  &\wt{\alpha}^{(m)}_1(q) = \sum_{n=0}^\infty
    \frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \left(\frac{1}{2}+n+2m+E_1^{(n)}(q)\right),\label{eq:ta1-41}
\end{align}
\end{subequations}
and
\begin{align}
  B_m(\re^u;q^{-1})
  &=

  \frac{\phi_0(u)^{-1}\phi_0(-u)^{-1}}{(1-\re^{-u})^2(q;q)_\infty^3}
    \sum_{n=0}^\infty\frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    \wt{\phi}_n(-u)\re^{(n+m)u} \nn
  &=
  u^{-2}(q;q)_\infty^{-3}\left(\wt{\beta}^{(m)}_0(q)+u
    \wt{\beta}^{(m)}_1(q) + \cO(u^2)\right)
    \label{eq:tB-uexp-41}
\end{align}
where
\begin{subequations}
\begin{align}
  &\wt{\beta}^{(m)}_0(q) = G_{-m}^0(q),\label{eq:tb0-41}\\
  &\wt{\beta}^{(m)}_1(q) = \sum_{n=0}^\infty
    \frac{q^{-nm}}{(q;q)_n(q^{-1};q^{-1})_n}
    (1+2n+m-E_1^{(n)}(q)).\label{eq:tb1-41}
\end{align}
\end{subequations}
We also notice
\begin{equation}
  \wt{\beta}_1^{(m)}(q) - \wt{\alpha}_1^{(m)}(q) =
  \frac{1}{2} G_{-m}^1(q).
\end{equation}
Applying these results to the right hand side of \eqref{41x-desc-fac},
we find the $O(1/u)$ contributions from~\eqref{eq:tA-uexp-41}
and~\eqref{eq:tB-uexp-41} cancel, and the $O(u^0)$ contributions
reproduce exactly~\eqref{410-desc-fac}. Notice that the $\sqrt{\tau}$
terms that appear in~\eqref{410-desc-fac} come from expanding in terms
of $2\pi\bb\,u$ and $2\pi\bb^{-1}\,u$ in~\eqref{41x-desc-fac}.
    
As an application of the above computations, we obtain proof of a
simplified formula for the $q$-series $G^1(q)$ from~\eqref{Gm0} which
was found experimentally in~\cite{GZ:qseries}.

\begin{proposition}
  \label{prop.G}
  For $|q|<1$, we have:
  \begin{equation}
  \label{GGformula}
  G^1(q) = \sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2}}{(q;q)_n^2}
  (6n+1) \,.
  \end{equation}
\end{proposition}

\begin{proof}
  We first show that the definition \eqref{Gm0} can equally be written
  as
  \begin{equation}
    G^1(q) = \sum_{n=0}^\infty (-1)^n \frac{q^{n(n+1)/2}}{(q;q)_n^2}
    \left(1+2n-4E_1^{(n)}(q)\right).\label{eq:G1-im}
  \end{equation}
  By definition
  \begin{equation}
    E_1^{(n)}(q) = \sum_{s=1}^\infty \frac{q^{s(n+1)}}{1-q^s},
  \end{equation}
  they satisfy the recursion relation
  \begin{equation}
    E_1^{(n)}(q) - E_1^{(n-1)}(q) = -\frac{q^n}{1-q^n},
  \end{equation}
  and therefore
  \begin{equation}
    E_1^{(n)}(q) = E_1^{(0)}(q) -\sum_{j=1}^n\frac{q^j}{1-q^j}.
  \end{equation}
  Using the identification $E_1(q) = 1-4E_1^{(0)}(q)$, one can then
  easily show that \eqref{eq:G1-im} is the same
  as \eqref{Gm0}.

  \eqref{GGformula} follows from \eqref{eq:G1-im} thanks to the
  non-trivial identity
  \begin{equation}
    \sum_{n=0}^\infty \frac{n+E_1^{(n)}(q)}{(q;q)_n(q^{-1};q^{-1})_n}
    = 0,\quad |q|<1,
    \label{eq:E1n-id}
  \end{equation}
  which now we prove.
  The crucial fact we use is that when $|q|<1$, $J(x,y;q)$ is
  symmetric between $x$ and $y$ (see a proof in \cite{Beem}).
  Let us consider the following expansion in small $u$
  \begin{align}
    J(\re^{-u},\re^u;q) =
    &\sum_{n=0}^\infty (q^{1+n}\re^u;q)_\infty\frac{\re^{-nu}}{(q^{-1};q^{-1})_n} =
    (q;q)_\infty\sum_{n=0}^\infty \frac{\phi_n(u)\re^{-nu}}{(q;q)_n(q^{-1};q^{-1})_n}\nn =
    &(q;q)_\infty\sum_{n=0}^\infty \frac{1-(n+E_1^{(n)}(q))u}{(q;q)_n(q^{-1};q^{-1})_n} +
    O(u^2). 
  \end{align}
  Since $J(\re^{-u},\re^u;q) = J(\re^{u},\re^{-u};q)$, the coefficient
  of $u$ (and in fact, of any odd power of $u$) in the expansion above
  vanishes, which leads to \eqref{eq:E1n-id}.
\end{proof}

As a second application, we demonstrate that Theorem~\ref{thm.410},
especially the identities \eqref{det41}, \eqref{WWT41}, as well as the
recursion relation \eqref{41qdiff}, can be proved by taking the $u=0$
limit of the analogue identities in Theorem~\ref{thm.41b}.

Using the expansion formulas of holomorphic blocks \eqref{eq:A-uexp-41},
\eqref{eq:B-uexp-41}, \eqref{eq:tA-uexp-41}, \eqref{eq:tB-uexp-41},
the Wronskians can be expanded as
\begin{align}
  W_m(\re^u;q) =
  &\begin{pmatrix}
    G_m^0(q)+u\alpha_1^{(m)}(q)&G_m^0(q)+u\beta_1^{(m)}(q)\\
    G_{m+1}^0(q)+u\alpha_1^{(m+1)}(q)&G_{m+1}^0(q)+u\beta_1^{(m+1)}(q)
  \end{pmatrix}
  \begin{pmatrix}
    u^{-2}(q;q)_\infty^{-3}&0\\
    0&-u(q;q)_\infty^3
  \end{pmatrix},
  \label{eq:Wp-uexp-41}\\
  W_m(\re^u;q^{-1}) =
  &\begin{pmatrix}
    G_{-m}^0(q)+u\wt{\alpha}_1^{(m)}(q)
    &G_{-m}^0(q)+u\wt{\beta}_1^{(m)}(q)\\
    G_{-m-1}^0(q)+u\wt{\alpha}_1^{(m+1)}(q)
    &G_{-m-1}^0(q)+u\wt{\beta}_1^{(m+1)}(q)
  \end{pmatrix}
  \begin{pmatrix}
    -u(q;q)_\infty^{3}&0\\
    0&u^{-2}(q;q)_\infty^{-3}
  \end{pmatrix}
  \label{eq:Wn-uexp-41}
\end{align}
Taking the determinant of \eqref{eq:Wp-uexp-41}, we find
\begin{equation}
  \det W_m(\re^u;q) = \frac{1}{2} \det W_m(q) + O(u)
\end{equation}
which together with the $u$-expansion of the right hand side of
\eqref{W410} leads to the determinant identity \eqref{det41}.
Furthermore, by substituting \eqref{eq:Wp-uexp-41},
\eqref{eq:Wn-uexp-41} into the Wronskian relation \eqref{WW41b}, the
latter also reduces in the leading order to the determinant identity
\eqref{det41}.  On the other hand, the Wronskian relation
\eqref{WWT41b} is equivalent to
\begin{equation}
  W_m(q) = 2
  \begin{pmatrix}
    0&-1\\1&0
  \end{pmatrix}\left(W_m(q)^{-1}\right)^T
  \begin{pmatrix}
    0&1\\-1&0
  \end{pmatrix}
\end{equation}
which can be proved directly by expressing the inverse matrix on the
right hand side by minors and determinant, using the explicit value of
the determinant given by the identity \eqref{det41}.

Finally, from the expression \eqref{eq:a0-41},\eqref{eq:b0-41} of the
leading order coefficients $\alpha_0^{(m)}(q)$, $\beta_0^{(m)}(q)$ of
$A_m(\re^u;q)$, $B_m(\re^u;q)$ in the expansion of $u$, one concludes
that the recursion relation \eqref{41qdiff} should be the $u=0$ limit
of the recursion relation \eqref{rec41m} in $m$, and one can easily
check it is indeed the case.


\subsection{Stokes matrices near $u=0$}
\label{sub.41stokes}

In this section we conjecture a formula for the Stokes matrices of the
asymptotic series $\varphi(x;\tau)$.  When we turn on the non-vanising
deformation parameter $u$, the resurgent structure discussed in
Section~\ref{sub.41x=1} undergoes significant changes.  Compared to
Figure~\ref{fig:sings-u0-41} there are many more singular points in
the Borel plane whose positions depend on $u$ in addition to $\tau$,
and the Stokes matrices also become $u$-dependent.  However, if we
focus on the case when $u$ is not far away from zero, equivalent to
$x$ not far away from 1, the resurgent data is holomorphic in $u$ and
reduces to those in Section~\ref{sub.41x=1} in the $u=0$ limit.  For
instance, each singular point in Figure~\ref{fig:sings-u0-41} splits
to a cluster of neighoring singular points separated with distance
$\log x$ as shown in Figure~\ref{fig:sings-m-41}. In particular, each
singular point $\iota_{i,j}$ on the real axis splits to a cluster of
three, in accord with the off-diagonal entries $\pm 3$ in
\eqref{eq:S0u041}, and if we choose real $x$, the split singularities
still lie on the real axis.  As in Section~\ref{sub.41x=1}, we label
the four regions separating singularities on real axis and all the
others by $I,II,III,IV$ (see Figure~\ref{fig:secs-m-41}).  In each of
the four regions, we have the following the results.

\begin{figure}
\leavevmode
\begin{center}
\includegraphics[height=7cm]{fig8_borelplane_s1m}\hspace{4ex}
\includegraphics[height=7cm]{fig8_borelplane_s2m}
\end{center}
\caption{The singularities in the Borel plane for the series
  $\varphi_{\sigma_{j}} (x;\tau)$ with $j=1,2$ of knot $\knot{4}_1$
  where $x$ is close to 1. The shortest vertical spacing between
  singularities is $2\pi\ri$, and the horizontal spacing between
  neighboring singularities in each cluster is $\log x$.}
\label{fig:sings-m-41}
\end{figure}

\begin{figure}
\leavevmode
\begin{center}
\includegraphics[height=7cm]{fig8_regions_m}
\end{center}
\caption{Four different sectors in the $\tau$-plane for $\Phi(u;\tau)$
  of knot $\knot{4}_1$ with $u$ close to zero.}
\label{fig:secs-m-41}
\end{figure} 

\begin{conjecture}
  \label{conj.41M}
  The asymptotic series and the holomorphic blocks are related
  by~\eqref{abrelx} with the diagonal matrix $\Delta(\tau)$ as
  in~\eqref{D41}, where matrices $M_R(x;q)$ are given in terms of the
  matrices $W_{-1}(x;q)$ as follows 
\begin{subequations}
\begin{align}
  M_{I}(x;q) =
  &\begin{pmatrix}
    1&0\\0&-1
  \end{pmatrix} W_{-1}(x;q)^T
            \begin{pmatrix}
              0&1\\-x^{-1}&1
            \end{pmatrix}, & |q|<1\,,
  \label{eq:M1-41}\\
  M_{II}(x;q) =
  &W_{-1}(x^{-1};q)^T
    \begin{pmatrix}
      -x^{-1}&0\\-x^{-1}&1
    \end{pmatrix}, & |q|<1\,,
  \label{eq:M2-41}\\
  M_{III}(x;q) =
  &W_{-1}(x^{-1};q)^T
    \begin{pmatrix}
      -x^{-1}&0\\1+x&1
    \end{pmatrix}, & |q|>1\,,
  \label{eq:M3-41}\\
  M_{IV}(x;q) =
  &\begin{pmatrix}
    1&0\\0&-1
  \end{pmatrix} W_{-1}(x;q)^T
            \begin{pmatrix}
              0&1\\-x^{-1}&-x^{-1}-x^{-2}
            \end{pmatrix}, & |q|>1\,.
                            \label{eq:M4-41}
\end{align}
\end{subequations}
\end{conjecture} 
The above conjecture completely determines the resurgent structure of
$\Phi(\tau)$. Indeed, it implies that the Stokes matrices, defined in 
Equations~\eqref{4G} and~\eqref{SG}, are explicitly given by:

\begin{subequations}
\begin{align}
    \ms{S}^+(x;q) =
    &\begin{pmatrix}
      0&-1\\
      x^{-1}&-1-x
    \end{pmatrix}
              \cdot W_{-1}(x^{-1};q^{-1})\cdot W_{-1}(x;q)^T\cdot
              \begin{pmatrix}
                0&x\\
                -1&-1-x^{-1}
              \end{pmatrix} ,\quad |q|<1\,,
  \label{eq:Sp-41}\\
  
  
  
  
  
  
    \ms{S}^-(x;q)=
    &\begin{pmatrix}
      x&x\\
      0&-1
    \end{pmatrix}
              \cdot W_{-1}(x;q)\cdot W_{-1}(x^{-1};q^{-1})^T\cdot
              \begin{pmatrix}
                x^{-1}&0\\
                x^{-1}&-1
              \end{pmatrix},\quad |q|<1\,.
                                \label{eq:Sn-41}
\end{align}
\end{subequations}
We remark that since $s(\Phi_\s)(x;\tau)$ for $\s=1,2$ transform under
the reflection $\pi: x\mapsto x^{-1}$ uniformly by \eqref{eq:-xPhi} (see
the comment below), the Stokes matrices should be invariant under
$\pi$, and we have checked that \eqref{eq:Sp-41},\eqref{eq:Sn-41}
indeed satisfy this consistency condition.

In the $q\mapsto 0$ limit,
\begin{equation}
  \ms{S}^+(x;0) =
  \begin{pmatrix}
    1&x^{-1}+1+x\\0&1
  \end{pmatrix},\quad
  \ms{S}^-(x;0) =
  \begin{pmatrix}
    1&0\\-x^{-1}-1-x&1
  \end{pmatrix}
  \label{eq:S0x41}
\end{equation}
A curious corollary of our computation is that the matrices of
integers \eqref{eq:S0u041} from~\cite{gh-res,GZ:kashaev} which relates
the asymptotics of the coefficients of $\varphi(\tau)$ to the
coefficients themselves, spreads out to the matrices \eqref{eq:S0x41}
with entries in $\IZ[x^{\pm 1}]$.

Using the unique factorization Lemma~\ref{lem.fac} and the Stokes
matrix $\sf{S}$ from above, we can compute the Stokes constants and
the corresponding matrix $\calS$ of Equation~\eqref{calS} to arbitrary
order in $q$, and we find that
\begin{align}
  \mc{S}^+_{\s_1,\s_1}(x;q) =
  &\ms{S}^+(x;q)_{1,1}-1\nn=
  &(-2 - x^{-2} - 2x^{-1} - 2 x - x^2)q
    +(-3 - x^{-2} - 2x^{-1} - 2 x - x^2)q^2+\cO(q^3),\\
  \mc{S}^+_{\s_1,\s_2}(x;q) =

  &\ms{S}^+(x;q)_{1,2}/\ms{S}^+(x;q)_{1,1}
  -(\mc{S}^{(1,0)}_{\s_1,\s_2}x+\mc{S}^{(0,0)}_{\s_1,\s_2}
  +\mc{S}^{(-1,0)}_{\s_1,\s_2}x^{-1})\nn=
  &(3 + x^{-2} + 2x^{-1} + 2 x + x^2)q\nn
  &+(17 + x^{-4} + 4x^{-3} + 9x^{-2} + 15x^{-1} + 15 x + 9 x^2 + 4 x^3 + x^4)
  q^2+\cO(q^3),\\
  \mc{S}^+_{\s_2,\s_1}(x;q) =
  &\ms{S}^+(x;q)_{2,1}/\ms{S}^+(x;q)_{1,1}\nn=
  &(-3 - x^{-2} - 2x^{-1} - 2 x - x^2)q\nn
  &+(-17 - x^{-4} - 4x^{-3} - 9x^{-2} - 15 x^{-1} - 15 x - 9 x^2 - 4 x^3 - x^4)
  q^2+\cO(q^3),\\
  \mc{S}^+_{\s_2,\s_2}(x;q) =
  &\ms{S}^+(x;q)_{2,2} -1-
    \ms{S}^+(x;q)_{1,2}\ms{S}^+(x;q)_{2,1}/\ms{S}^+(x;q)_{1,1}\nn=
  &(2 + x^{-2} + 2x^{-1} + 2 x + x^2) q \nn
  &+ (17 + x^{-4} + 4x^{-3} + 9x^{-2} + 14x^{-1} + 14 x + 9 x^2 + 4 x^3 + x^4)
  q^2+\cO(q^3).
\end{align}
They enjoy the symmetry
\begin{equation}
  \mc{S}^{+}_{\s_1,\s_2}(x;q) =
  -\mc{S}^{+}_{\s_2,\s_1}(x;q)\,,
\end{equation}
and experimentally, it appears that the entries of the matrix
$\mc{S}^+(x;q) = (\mc{S}^+_{\s_i,\s_j}(x;q))$ (except the upper-left
one) are (up to a sign) in $\BN[x^{\pm 1}][[q]]$. 
Similarly we can extract the Stokes constants
$\mc{S}^{(\ell,-k)}_{\s_i,\s_j}$ associated to the singularities in
the lower half plane, and assemble into $q^{-1}$-series
$\mc{S}^{-}_{\s_i,\s_j}(x;q^{-1})$.  We find they are related to
$\mc{S}^+_{\s_i,\s_j}(x;q)$ by
\begin{gather}
  \mc{S}^{-}_{\s_i,\s_j}(x;q) = -\mc{S}^{+}_{\s_j,\s_i}(x;q),\;\;i\neq j\,
  \nn
  \mc{S}^{-}_{\s_1,\s_1}(x;q) = \mc{S}^{+}_{\s_2,\s_2}(x;q),\;\;
  \mc{S}^{-}_{\s_2,\s_2}(x;q) = \mc{S}^{+}_{\s_1,\s_1}(x;q)\,.
\end{gather}

Let us now verify Conjecture~\ref{conj.S3D}.
From \eqref{eq:Sp-41} we find that indeed
\begin{equation}
  \ms{S}^+(x;q) \stackrel{\cdot}{=} W_{-1}(x^{-1};q^{-1})\cdot W_{-1}(x;q)^T.
\end{equation}
Using the recursion relation \eqref{eq:W41rec} and the relation
between two Wronskians \eqref{W41xm}, we further find 
\begin{equation}
  \ms{S}^+(x;q) \stackrel{\cdot\cdot}{=} \cW_{0}(x^{-1};q^{-1})\cdot
  \cW_{0}(x;q)^T.
  \label{eq:SW41}
\end{equation}
If we use the uniform notation for all holomorphic blocks
\begin{equation}
  (B_{K}^\alpha(x;q))_{\alpha=1,2} = (A_0(x;q),B_0(x;q)),
\end{equation}
the right hand side of \eqref{eq:SW41} reads 
\begin{equation}
  \cW_{0}(x^{-1};q^{-1})\cdot \cW_{0}(x;q)^T =
  \left(
    \sum_{\alpha}B^{\alpha}_{\knot{4}_1}(q^jx;q)
    B^{\alpha}_{\knot{4}_1}(q^{-i}x^{-1};q^{-1})
  \right)_{i,j=0,1}.
  \label{eq:WW41}
\end{equation}
which is precisely the right hand side of \eqref{eq:SInd} in
Conjecture~\ref{conj.S3D} following \eqref{eq:IndB}.\footnote{Note
  that because the form of the state integral in \cite{Beem} is
  slightly different from that in \cite{AK}, which we adopt, our
  convention for holomorphic blocks is also different from
  \cite{Beem}.  As a result, the entries of $\eqref{eq:WW41}$ equate
  the DGG indices computed in \cite{Beem} up to a prefactor
  \begin{equation}
    \left(\cW_{0}(x^{-1};q^{-1})\cdot \cW_{0}(x;q)^T\right)_{i+1,j+1} =
    (-q^{1/2})^{j-i}\text{Ind}_{\knot{4}_1}^{\text{rot}}
    (j-i,q^{\frac{j+i}{2}}x;q),\quad i,j=0,1.
  \end{equation}
  If we take this into account, Conjecture~\ref{conj.S3D} should be
  modified slightly by stating the accompanying matrices on the left
  and on the right are in $GL(2,\IZ(x,q^{1/2}))$.}
In addition, the forms of the accompanying matrices on the left and on the
right are such that the $(1,1)$ entry of $\ms{S}^+(x;q)$ equates
exactly the DGG index with no magnetic flux.
By explicit calculation,

\begin{equation}
\label{S11v}
\begin{aligned}
  \ms{S}^+(x;q)_{1,1}& =
  J(x, x^{-1};q) J(x, x^{-1}; q^{-1}) + J(x^{-2}, x^{-1};q) J(x^2, x; q^{-1}) \\
  &=1 -(2x^{-2}+ x^{-1}+2+x + 2x^2)q - (x^{-2}+2x^{-1} +3+ 2x + 
  x^2) q^2 + O(q^3),
  \end{aligned}
\end{equation}

which is the $\text{Ind}^{\text{rot}}_{\knot{4}_1}(0,x;q)$ given in
\cite{Beem}.
