---
doc_id: arxiv-hep-th-9711057v2
doc_title: "arXiv:hep-th/9711057v2 30 Apr 1998"
section_id: sec-003-22-construction-of-orthogonal-polynomials
section_title: "Construction of orthogonal polynomials"
section_number: 2.2
pages: 4-5
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9711057v2 30 Apr 1998 — 11 sections: Front matter; Introduction; Random-matrix theory for finite qu"
---
\label{sec22}

The polynomials $p_n^{(N_f)}(x,M)$ can be constructed by applying a
standard formula~\cite{Bate51} in the theory of orthogonal
polynomials. In our case, it reads
\begin{equation}
p_n^{(N_f)}(x,M) \ = \ \frac{1}{Z_n^{(N_f)}(M)} 
                     \int d[X] \Delta_n^2(X) 
                    \prod_{i=1}^n w^{(N_f)} (x_i,M) (x-x_i) \ .
\label{poly}
\end{equation}
This is an integral over $n$ variables $x_i$ ($i=1,\ldots,n$). We
notice that $n$ replaces the dimension $N$ of the matrices $W$ in the
partition function $Z_n^{(N_f)}(M)$ and in the Vandermonde determinant
$\Delta_n(X)$. Moreover, by construction, the coefficient in front
of $x^n$ is unity.

Fortunately, there is a further result, the Christoffel
formula~\cite{Bate51}, which allows us to immediately write down the
polynomials explicitly: The weight function $w^{(N_f)}(x,M)$ is a
product of the weight function $w^{(0)}(x)$ and a polynomial whose
zeros are the negative squared quark masses $-M_f^2$ and which is
nonnegative on the real axis.  Therefore, the polynomials
$p_n^{(N_f)}(x,M)$ can be written in terms of the polynomials which
are orthogonal with respect to the weight
$w^{(0)}(x)=\exp(-N\Sigma^2x)$.  These are precisely the Laguerre
polynomials $L_n^{(0)}(N\Sigma^2x)$.  The application of the
Christoffel formula then yields
\begin{eqnarray}
  p_n^{(N_f)}(x,M) &=& \frac{1}{C_n^{(N_f)}(M)} \,
  \frac{1}{\prod_{f=1}^{N_f}(x+M_f^2)} \,
  \frac{(n+N_f)!}{(N\Sigma^2)^{n+N_f}} \nonumber\\
& & \qquad \times\left| \begin{array}{llcl}
  L_n^{(0)}(N\Sigma^2x) & L_{n+1}^{(0)}(N\Sigma^2x) & \cdots &
                               L_{n+N_f}^{(0)}(N\Sigma^2x) \\ 
  L_n^{(0)}(-N\Sigma^2M_1^2) & L_{n+1}^{(0)}(-N\Sigma^2M_1^2) & \cdots &
                               L_{n+N_f}^{(0)}(-N\Sigma^2M_1^2) \\ 
     \qquad\vdots & \qquad\vdots & & \qquad\vdots \\ 
  L_n^{(0)}(-N\Sigma^2M_{N_f}^2) & L_{n+1}^{(0)}(-N\Sigma^2M_{N_f}^2)
   & \cdots &  L_{n+N_f}^{(0)}(-N\Sigma^2M_{N_f}^2) 
           \end{array}\right|  
\label{polcf}
\end{eqnarray} 
with a function $C_n^{(N_f)}(M)$ yet to be determined.  In
Sec.~\ref{sec23}, we will present a very direct and highly convenient
computation of the polynomials (\ref{polcf}) including all
normalization factors.  Here we proceed as follows: Since the
polynomial $p_n^{(N_f)}(x,M)$ has to be invariant under permutations
of the masses $M_f$ and must have a finite limit when all quark masses
are degenerate, a reasonable guess for the normalization function is
\begin{eqnarray}
C_n^{(N_f)}(M) \ = \ \det\left[L_{n+f-1}^{(0)}
        (-N\Sigma^2M_{f^\prime}^2)\right]_{f,f^\prime=1,\ldots,N_f}\:,
\label{polnorm}
\end{eqnarray} 
see Sec.~\ref{sec23} below, in particular Eq.~(\ref{chefformel}).
With this ansatz, the partition function $Z_n^{(N_f)}(M)$ is obtained
by studying the case of $N_f+1$ flavors. On the one hand,
Eqs.~(\ref{pdpfx}) and (\ref{poly}) yield
$p_n^{(N_f)}(-M_{N_f+1}^2,M)=-Z_n^{(N_f+1)}(M,M_{N_f+1})/Z_n^{(N_f)}(M)$,
which, on the other hand, has to be equal to the right-hand side of
Eq.~(\ref{polcf}) for $x=-M_{N_f+1}^2$. Thus, we arrive at the
recursion relation
\begin{equation}
\frac{Z_n^{(N_f+1)}(M,M_{N_f+1})}{C_n^{(N_f+1)}(M,M_{N_f+1})} 
\ = \ \frac{Z_n^{(N_f)}(M)}{C_n^{(N_f)}(M)} 
       \, \frac{(n+N_f)!}{(N\Sigma^2)^{n+N_f}} \,
          \frac{1}{\prod_{f=1}^{N_f}(M_f^2-M_{N_f+1}^2)} 
\label{recurs}
\end{equation} 
which implies
\begin{equation}
Z_n^{(N_f)}(M) \ = \ \prod_{f=1}^{N_f} \frac{(n+f-1)!}
{(N\Sigma^2)^{n+f-1}}\,\frac{C_n^{(N_f)}(M)}{\Delta_{N_f}(-M^2)}\:.
\label{parterg}
\end{equation} 
The correctness of these results can be verified using the
orthogonality relation~(\ref{ortho}).  In the microscopic limit, the
partition function agrees with the result obtained in
Ref.~\cite{Jack96c}, see Sec.~\ref{sec3}, Eq.~(\ref{CNfm}).  (Note
that in Ref.~\cite{Jack96c}, the result is expressed in terms of
derivatives of modified Bessel functions.  Using the recurrence
relations for Bessel functions \cite{Grad65} and the properties of the
determinant, one can show that the results are identical.)
