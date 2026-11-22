---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-016-52-holomorphic-blocks
section_title: "Holomorphic blocks"
section_number: 5.2
pages: 27-32
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.957
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
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
