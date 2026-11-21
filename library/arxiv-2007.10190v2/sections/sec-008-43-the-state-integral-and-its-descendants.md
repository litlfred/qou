---
doc_id: arxiv-2007.10190v2
doc_title: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS"
section_id: sec-008-43-the-state-integral-and-its-descendants
section_title: "The state integral and its descendants"
section_number: 4.3
pages: 9-11
source_pdf: 2007.10190v2.pdf
source_sha256: 37bcbd3a343bb21a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.93
doc_brief: "THE RESURGENT STRUCTURE OF QUANTUM KNOT INVARIANTS — The asymptotic expansion of quantum knot invariants in complex Chern-Simons theory gives rise to factorially divergent formal power series."
---
\label{sub.state}

In this section we recall the definition of state integrals and some
of their basic properties. State integrals are multidimensional
integrals whose integrand is a product of Faddeev's quantum
dilogarithm function $\Phi_{\bb}$ (whose definition we will not need
and may be found in~\cite{Faddeev,FK-QDL}) times an exponential of a
quadratic and linear form. Here
$\tau=\bb^2 \in \BC':=\BC\setminus(-\infty,0]$, thus even if the
integrand contains no free variables, a state integral is always a
holomorphic function of $\tau$.

State integrals have two key properties:
\begin{itemize}
\item[(a)] they define holomorphic functions in the complex cut plane
  $\BC'$.
\item[(b)] they can be expressed bilinearly in the upper and in the
  lower half-plane in terms of products of $q$-series and
  $\tq$-series.
\end{itemize}
For a detailed discussion of state integrals and numerous example, see
for instance~\cite{Beem} and also~\cite{AK} and~\cite{GK:qseries}.

In this section we introduce a descendant version of the one
dimensional state integrals of~\cite{GK:qseries} that satisfies the
above properties. In this section we will use the notation
from~\cite{GK:qseries}.  Consider the state integral

\begin{equation}
\label{eq.statelm}
  \calI_{A,B,\lambda,\mu}(\bb) =
    \int_{\BR+\ri\epsilon} \Phi_{\bb}(x)^B \re^{-A\pi\ri x^2 +
      2\pi(\lambda \bb - \mu \bb^{-1})x}\rd x,\qquad
     (\lambda,\mu\in \BZ)
   \end{equation}
   
   where $A$ and $B$ are integers and $B > A > 0$. Under these
  assumptions, it follows that the integrand is exponentially decaying
  at infinity and the integral is absolutely convergent and defines
  a holomorphic
  function of $\tau = \bb^2 \in \BC'$.
  Below, we will use the notation
  $\phi(w,\delta_\bullet)$, $\tilde{\phi}(w,\tilde{\delta}_\bullet)$
  and 
  \begin{equation}
    \vev{F(q,x)} = F(q,1)
  \end{equation}
  from~\cite{GK:qseries}.
  
  \begin{theorem}
    \label{thm.state}
    Fix integers $A$ and $B$ with $B > A > 0$ and integers $\lambda$ and
    $\mu$. For all $\tau$ with $\Im(\tau)>0$, we have:
\begin{equation}
\label{thm1}
    \calI_{A,B,\lambda,\mu}(\bb) =
    (-1)^{\lambda-\mu} q^{\frac{\lambda}{2}}\tq^{\frac{\mu}{2}}
    \left(\frac{\tq}{q}\right)^{\frac{B-3A}{24}}
    \re^{\pi\ri\frac{B+2(A+1)}{4}}
    \vev{P_{A,B,\lambda,\mu}
      \left(F_{A,B,\lambda}(q,x)\wt{F}_{A,B,\mu}(\tq,\tx)\right)}
  \end{equation}
where the operator $P_{A,B,\lambda,\mu}$ is given by
\begin{equation}
  \label{Plm}
    P_{A,B,\lambda,\mu} = \Res_{w=0}
    \left(
      \re^{\frac{w^2}{4\pi\ri}+w\left(\bb(\delta+1/2+\lambda/A)
          +\bb^{-1}(\tilde{\delta}+1/2-\mu/A)\right)}
    \right)^A
    \left(\frac{\phi(\bb w,\delta_\bullet)
        \tilde{\phi}(\bb^{-1}w,\tilde{\delta}_\bullet)}
      {\bb(1-\re^{\bb^{-1}w})}\right)^B .
  \end{equation}
  \end{theorem}
  In particular, the right hand side of Equation~\eqref{thm1} is a
  bilinear combination of $q$ and $\tq$-series extend to the cut plane
  $\BC'$. A similar formula can be given when $\tau$ is in the lower
  half-plane, and what is more, the state integral satisfies the
  symmetry
  $\calI_{A,B,\lambda,\mu}(\bb) = \calI_{A,B,\lambda,\mu}(\bb^{-1})$
  which is a consequence of the symmetry
  $\Phi_{\bb^{-1}}(x)=\Phi_{\bb}(x)$ of the quantum dilogarithm.
  
  \begin{proof}
  We follow the derivation in \cite{GK:qseries} closely.
  The idea is to sum up residues at all singularities in the upper
  half-plane.  The factor $\Phi_{\bb}(x)$ has poles at
  \begin{equation}
    x_{m,n} = \ri\bb(m+1/2) + \ri\bb^{-1}(n+1/2),\quad m,n\in
    \BN \,.
  \end{equation}
  We notice that
  \begin{equation}
    \re^{2\pi(\lambda\bb - \mu\bb^{-1})(x+x_{m,n})} =
    \re^{w(\lambda\bb - \mu\bb^{-1})}
    q^{\lambda(m+1/2)}\tq^{\mu(n+1/2)}(-1)^{\lambda-\mu} 
  \end{equation}
  where we have made the change of variables $w = 2\pi x$ and used the
  notation
  \begin{equation}
    q = \re^{2\pi\ri \bb^2},\quad \tq = \re^{-2\pi\ri \bb^{-2}}.
  \end{equation}
  Now by modifying Eqn.(27) of~\cite{GK:qseries}, we find
  \begin{multline}
    \calI_{A,B,\lambda,\mu}(\bb) =
    (-1)^{\lambda-\mu} q^{\frac{\lambda}{2}}\tq^{\frac{\mu}{2}}
    \left(\frac{\tq}{q}\right)^{\frac{B-3A}{24}}
    \re^{\pi\ri\frac{B+2(A+1)}{4}} \times \\
    \sum_{m,n=0}^\infty \left(\Res_{w = 0}F_{A,B,m,n,\lambda,\mu}(w)\right)
    \frac{q^{\lambda m}t_m(q)^A}{(q;q)_m^B}
    \frac{\tq^{\mu n}\tilde{t}_n(\tq)^A}{(\tq^{-1};\tq^{-1})_n^B} \,,
  \end{multline}
  where
  \begin{equation}
    F_{A,B,m,n,\lambda,\mu}(w) =
    \left(e^{\frac{w^2}{4\pi\ri}+w\left(\bb(m+1/2
          +\lambda/A)+\bb^{-1}(n+1/2-\mu/A)\right)}
    \right)^A
    \left(\frac{\phi_m(\bb w)\tilde{\phi}_n(\bb^{-1}w)}
      {\bb(1-e^{\bb^{-1}w})}\right)^B \,.
  \end{equation}
  Using the operator formalism in \cite{GK:qseries}, this concludes
  the proof of Equation~\eqref{thm1}.
\end{proof}

  The reader may find in~\cite{GK:qseries} the expressions of the operators
  $\phi(w,\delta_\bullet)$, $\tilde{\phi}(w,\tilde{\delta}_\bullet)$.
  Note that $e_l(\tq)$ in the paper are simply $E_l^{(0)}(\tq)$.
  In addition,
  \begin{align}
    &F_{A,B,\lambda}(q,x) = \sum_{n=0}^\infty (-1)^{A n}
      \frac{q^{A\frac{n(n+1)}{2}+n\lambda}}{(q;q)_n^B} x^n,\\
    &\wt{F}_{A,B,\mu}(\tq,\tx) = \sum_{n=0}^\infty (-1)^{(B-A) n}
      \frac{\tq^{(B-A)\frac{n(n+1)}{2}+n\mu}}{(\tq;\tq)_n^B} \tx^n.
  \end{align}
  They can be related by
  \begin{equation}
    F_{A,B,\lambda}(q^{-1},x) = \wt{F}_{A,B,-\lambda}(q,x).
  \end{equation}

  \begin{example}
\label{ex.41s}
In this example we illustrate theorem~\ref{thm.state} with the
state integral $\calI_{1,2,\lambda,\mu}(\bb)$ associated to the $4_1$
knot~\cite{AK}. As we will see, this reproduces the $q$-series
$G^0_m(q)$ and $G^1_m(q)$ of~\eqref{gm} and~\eqref{Gm}.

Using
  \begin{equation}
    F_\lambda(q,x) = F_{1,2,\lambda}(q,x) = \wt{F}_{1,2,\lambda}(q,x)
    = \sum_{n=0}^\infty (-1)^n \frac{q^{\frac{n(n+1)}{2}+n\lambda}}{(q;q)_n^2}x^n.
  \end{equation}
  we find that 
  \begin{equation}
    P_{1,2,\lambda,\mu} =
    \frac{\bb}{2}(1+2\delta - 4\delta_1+2\lambda)
    -\frac{\bb^{-1}}{2}(1+2\tilde{\delta} - 4\tilde{\delta}_1 + 2\mu).
  \end{equation}
  It then follows that ($\tau = \bb^2$)
  \begin{equation}
  \label{desc-41}
    \calI_{1,2,\lambda,\mu}(\bb)
    =
    (-1)^{\lambda-\mu+1}\ri q^{\frac{\lambda}{2}}\tq^{\frac{\mu}{2}}
    \left(\frac{q}{\tq}\right)^{\frac{1}{24}}
    \left(\frac{\tau^{1/2}}{2}G^1_\lambda(q)G^0_\mu(\tq) -
      \frac{\tau^{-1/2}}{2}G^0_\lambda(q)G^1_\mu(\tq)\right),
  \end{equation}
  
  where we have used that
  
  \be
  \vev{F_{\lambda}(q,x)}=G^0_\lambda(q) , \qquad
  \vev{(1+2\lambda+2\delta-4\delta_1)F_\lambda(q,x)}=G^1_\lambda(q). 
    \end{equation}
    
\end{example}
In appendix~\ref{sec.A52}, we give the details for the state integral
$\calI_{2,3,\lambda,\mu}(\bb)$ of the $5_2$ knot.
