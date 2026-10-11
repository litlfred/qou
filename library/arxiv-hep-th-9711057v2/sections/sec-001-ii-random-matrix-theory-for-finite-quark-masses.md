---
doc_id: arxiv-hep-th-9711057v2
doc_title: "The microscopic spectrum of the QCD Dirac operator with finite quark masses"
section_id: sec-001-ii-random-matrix-theory-for-finite-quark-masses
section_title: "RANDOM-MATRIX THEORY FOR FINITE QUARK MASSES"
section_number: II
pages: 2-6
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
doc_brief: "The microscopic spectrum of the QCD Dirac operator with finite quark masses — 7 sections: INTRODUCTION; RANDOM-MATRIX THEORY FOR FINITE QU; CALCULATION OF OBSERVABLES"
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.994
---
\label{sec2}

In Sec.~\ref{sec21}, we formulate the chiral random-matrix model by
introducing the probability density function and the partition
function in the presence of finite quark masses. In Sec.~\ref{sec22},
we construct the orthogonal polynomials of the model. An alternative
construction is presented in Sec.~\ref{sec23} which is based on a certain
duality between models in different matrix spaces.



\subsection{Formulation of the model}
\label{sec21}

The statistical properties of the random-matrix model for the massive
Dirac operator with $N_f$ flavors and dynamical quark masses $M_f$
($f=1,\ldots,N_f$) which was introduced above are given by the
probability density function
\begin{equation}
P_N^{(N_f)}(W,M) \ = \ \frac{1}{\widetilde{Z}_N^{(N_f)}(M)} \, 
                \prod_{f=1}^{N_f}\det(WW^\dagger+M_f^2)
                \exp(-N\Sigma^2{{\rm tr}\,} WW^\dagger)
\label{pdf}
\end{equation}
with $M=(M_1,\ldots,M_{N_f}$). Here, $W$ is a complex matrix of
dimension $N$.  Apart from a Gaussian, this distribution contains
$N_f$ fermionic determinants. Eventually, we are mainly interested in
the microscopic limit. Hence, it suffices to take into account a
Gaussian in the total distribution (\ref{pdf}) since various authors
\cite{Brez96,Nish96} have given proofs of universality in related
problems.  Note that even for nonzero topological charge $\nu$ it is
sufficient to consider only square matrices $W$ in the calculation
because of the duality between topology and flavor
\cite{Verb93,Verb94a}.  A nonzero $\nu$ is obtained by introducing
$\nu$ additional massless flavors at the end of the calculation.  The
normalization constant
\begin{equation}
\widetilde{Z}_N^{(N_f)}(M) \ = \ 
               \int d[W] \prod_{f=1}^{N_f}\det(WW^\dagger+M_f^2)
                \exp(-N\Sigma^2{{\rm tr}\,} WW^\dagger)
\label{partf}
\end{equation}
depends on the quark masses and plays the role of a partition
function.  Since both of the above expressions depend on the matrices
$W$ only through invariant functions of $WW^\dagger$, they can be
reduced to integrals over radial coordinates. We write $W=U \Lambda
\bar{V}$ with $U\in{\rm U}(N)$, $\bar{V}\in{\rm U}(N)/ {\rm U}^N(1)$,
and $\Lambda={\rm diag}(\lambda_1,\ldots,\lambda_N)$, where the radial
coordinates $\lambda_i$ are restricted to the positive real axis.
Thus, we have $WW^\dagger=U\Lambda^2U^\dagger$ suggesting the
introduction of new variables $x_i=\lambda_i^2$. The measure
transforms as $d[W]=\Delta_N^2(X)d[X]d\mu(U)d\mu(\bar{V})$, where
$X={\rm diag} (x_1,\ldots,x_N)$, $\Delta_N(X)=\prod_{i<j}(x_i-x_j)$ is
the Vandermonde determinant, and $d\mu$ is the Haar measure.  After
integrating over the unitary groups, we obtain
\begin{equation}
\label{eq2.1}
P_N^{(N_f)}(X,M) = \frac{1}{Z_N^{(N_f)}(M)} \, \Delta_N^2(X) \, 
                 \prod_{i=1}^N w^{(N_f)}(x_i,M) 
\end{equation}
for the probability density and 
\begin{equation}
Z_N^{(N_f)}(M) = \int d[X] \, \Delta_N^2(X) \,
                 \prod_{i=1}^N w^{(N_f)}(x_i,M) 
\label{pdpfx}
\end{equation}
for the partition function $Z_N^{(N_f)}(M)$ which differs from
$\widetilde{Z}_N^{(N_f)}(M)$ by the group volumes. The expression
\begin{equation}
w^{(N_f)}(x,M) \ = \ \exp(-N\Sigma^2x) \prod_{f=1}^{N_f}(x+M_f^2) 
\label{weight}
\end{equation}
will be referred to as the weight function.

Because of a main result of RMT \cite{Meht91}, all spectral
correlation functions $R_k^{(N_f)}(x_1,\ldots,x_k,M)$ of our model can
readily be written in terms of the polynomials $p_n^{(N_f)}(x,M)$
which are orthogonal with respect to the weight function
$w^{(N_f)}(x,M)$,
\begin{equation}
  \int_0^\infty dx \, w^{(N_f)}(x,M) p_n^{(N_f)}(x,M) p_m^{(N_f)}(x,M)
  \ = \ 
  \frac{Z_{n+1}^{(N_f)}(M)}{(n+1)\,Z_n^{(N_f)}(M)} \, \delta_{nm} \ .
\label{ortho}
\end{equation} 
The correlation functions are given as the determinant
\begin{equation}
R_k^{(N_f)}(x_1,\ldots,x_k,M) \ = \ 
  \det\left[K_N^{(N_f)}(x_i,x_j,M)\right]_{i,j=1,\ldots,k}
\label{corrfct}
\end{equation}
with a kernel given by
\begin{equation}
K_N^{(N_f)}(x,y,M) \ = \ \sqrt{w^{(N_f)}(x,M)w^{(N_f)}(y,M)} \,
                 \sum_{n=0}^{N-1}   
                \frac{(n+1)\,Z_n^{(N_f)}(M)}{Z_{n+1}^{(N_f)}(M)}
                p_n^{(N_f)}(x,M) p_n^{(N_f)}(y,M) \ .
\label{summe}
\end{equation}
With the help of the Christoffel-Darboux formula the kernel
can be expressed as
\begin{eqnarray}
K_N^{(N_f)}(x,y,M) & = & N \, \frac{Z_{N-1}^{(N_f)}}{Z_N^{(N_f)}} \,
                 \sqrt{w^{(N_f)}(x,M)w^{(N_f)}(y,M)} \nonumber\\
  &&\times \frac{p_N^{(N_f)}(x,M)p_{N-1}^{(N_f)}(y,M)
    -p_{N-1}^{(N_f)}(x,M)p_N^{(N_f)}(y,M)}{x-y} \ ,
\label{kernel}
\end{eqnarray}
provided that the coefficient of the power $x^n$ in $p_n^{(N_f)}(x,M)$
is unity.  Eventually, we will take the microscopic limit as discussed
in the Introduction.



\subsection{Construction of orthogonal polynomials}
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



\subsection{A duality of matrix ensembles}
\label{sec23}

In this section, we present an alternative derivation of the
orthogonal polynomials $p_n^{(N_f)}(x,M)$ and of the partition
function $Z_N^{(N_f)}(M)$. It employs a certain kind of duality
between matrix ensembles and is therefore of conceptual interest. On
the practical side, this method advantageously yields all
normalizations, particularly the function $C_n^{(N_f)}(M)$ and the
partition function $Z_n^{(N_f)}(M)$, in a very direct and convenient
way. We consider the integral
\begin{equation}
X_N^{(K)}(a) \ = \int d[W] \, \exp(-\alpha{{\rm tr}\,} WW^\dagger) \,
\prod_{f=1}^K \det\left[
            \begin{array}{cc} -ia_f & W \\ 
                          W^\dagger & -ia_f 
            \end{array} \right]
\label{Xdef}
\end{equation}
depending on $K$ parameters $a_f$ ($f=1,\ldots,K$). For
$\alpha=N\Sigma^2$, $K=N_f$, and $a_f=M_f$, the integral~(\ref{Xdef})
is just the partition function~(\ref{partf}). For $N=n$, $K=N_f+1$,
$a_f=M_f$ ($f=1,\ldots,N_f$), and $a_{N_f+1}^2=-x$, the
integral~(\ref{Xdef}) is, up to the group volumes, equal to
$Z_n^{(N_f)}(M)p_n^{(N_f)}(x,M)$ as defined in Eq.~(\ref{poly}). Thus,
the function $X_N^{(K)}(a)$ yields all desired quantities.  We define
$K$ $2N$-component vectors $\zeta_f$ ($f=1,\ldots,K$) with complex
Grassmannian entries $\zeta_{fi}$ ($i=1,\ldots,2N$) as well as the
$2NK$-component combination $\zeta=(\zeta_1,\ldots,\zeta_K)^T$.  The
determinants in the integrand of Eq.~(\ref{Xdef}) are represented as
the integral
\begin{equation}
\prod_{f=1}^K \det\left[\begin{array}{cc} -ia_f      & W \\ 
                                           W^\dagger & -ia_f 
                        \end{array}\right] \ = \ 
(2\pi)^{2NK} \, \int d[\zeta] \, \exp\left(\zeta^\dagger
  \left(\openone_K\otimes
   \left[\begin{array}{cc} 0         & W \\ 
                           W^\dagger & 0
    \end{array}\right] - ia\otimes \openone_{2N}\right)\zeta\right)
\label{fermint}
\end{equation}
with $a={\rm diag}(a_1,\ldots,a_K)$. In this form, the Gaussian
average over the matrices $W$ can easily be performed. We arrive at a
four-fermion interaction which is then decoupled by a
Hubbard-Stratonovitch transformation. In Ref.~\cite{Guhr97a}, a
very similar route was taken. In this study, however, a problem
involving fermionic and bosonic determinants was solved which led to
the introduction of supervectors of commuting and anticommuting
variables. In the present case, the vectors $\zeta_f$ have only
anticommuting entries. Fortunately, this difference has little
influence on the structure of the results. Instead of the
supermatrices which were used in Ref.~\cite{Guhr97a} for the
Hubbard-Stratonovitch transformation, we have to employ ordinary
matrices here. We arrive at
\begin{equation}
X_N^{(K)}(a) \ = \ \left(\frac{\alpha}{\pi}\right)^{K^2}
                   \, \int d[\sigma]
  \exp\left(-\alpha{{\rm tr}\,}(\sigma-a)(\sigma^\dagger-a)\right)
                   \, {\rm det}^N\sigma\sigma^\dagger \:,
\label{dualmod}
\end{equation}
where $\sigma$ is an ordinary complex $K\times K$ matrix without
further symmetries. Thus, we have mapped the original model of
Sec.~\ref{sec21} in the form~(\ref{Xdef}) in the space of the $N\times
N$ matrices $W$ onto a dual model in the space of the $K\times K$
matrices $\sigma$. This is highly convenient because, eventually, we
wish to take the limit $N\to\infty$.  Remarkably, these dual models
differ with respect to rotation invariance. The model of
Sec.~\ref{sec21} is invariant under rotations in the sense that the
integrand of the partition functions in Eqs.~(\ref{partf})
and~(\ref{pdpfx}) depends only on the radial coordinates of the
matrices $W$, i.e., on the variables $x_i$.  This is not true for the
model~(\ref{dualmod}). The presence of the matrices $a$ breaks this
kind of rotation invariance. In Refs.~\cite{Guhr96b} and
\cite{Guhr97a}, a procedure was developed to deal with models
precisely of this kind. We introduce radial coordinates by
$\sigma=us\bar{v}$ with $u\in {\rm U}(K)$, $\bar{v}\in {\rm U}(K)/
{\rm U}^K(1)$, and $s={\rm diag}(s_1,\ldots,s_K)$. Again, the radial
coordinates $s_f$ are restricted to the positive real axis. The
measure transforms as
$d[\sigma]=\Delta_K^2(s^2)\prod_{f=1}^Ks_fd[s]d\mu(u)d\mu(\bar{v})$.
The integral over the unitary groups is now nontrivial. The solution
can be found in Ref.~\cite{Guhr96b},
\begin{equation}
\left(\frac{\alpha}{\pi}\right)^{K^2} \, 
          \int d\mu(u) \int d\mu(\bar{v}) 
          \exp\left(-\alpha{{\rm tr}\,}(us\bar{v}-a)
                   (\bar{v}^\dagger su^\dagger-a)\right) \ = \
           \frac{1}{K!}
           \frac{\det\left[\gamma(s_f,a_{f^\prime})
                      \right]_{f,f^\prime=1,\ldots,K}}
                {\Delta_K(s^2)\Delta_K(a^2)} \ .
\label{groupint}
\end{equation}
The entries of the determinant are given by
\begin{equation}
\gamma(s_f,a_{f^\prime}) \ = \ 2\alpha \, 
         \exp\left(-\alpha(s_f^2+a_{f^\prime}^2)\right) \,
                        I_0(2\alpha s_f a_{f^\prime}) \ ,
\label{diffkern}
\end{equation}
where $I_0$ is the modified Bessel function of the first kind and
zeroth order.  Collecting everything, we obtain
\begin{equation}
X_N^{(K)}(a) \ = \ \frac{1}{K!} \, \frac{1}{\Delta_K(a^2)} 
       \prod_{f=1}^K \int_0^\infty ds_f \, s_f^{2N+1} \, \Delta_K(s^2)
  \det\left[\gamma(s_f,a_{f^\prime})\right]_{f,f^\prime=1,\ldots,K}\:.
\label{integral}
\end{equation}
This integral can be solved in a straightforward way. We write
$\Delta_K(s^2)=\det[s_f^{2(f^\prime-1)}]_{f,f^\prime=1,\ldots,K}$
and integrate this determinant row by row. Using the representation
\begin{equation}
2\alpha \int_0^\infty dw \, w^{2n+2m+1} \,
       \exp\left(-\alpha(z^2+w^2)\right) I_0(2\alpha wz) \ = \
\frac{(n+m)!}{\alpha^{n+m}} \, L_{n+m}^{(0)}(-\alpha z^2)
\label{intrepres}
\end{equation}
for the Laguerre polynomials, we find 
\begin{equation}
X_N^{(K)}(a) \ = \ \frac{1}{\Delta_K(a^2)} 
 \prod_{f=0}^{K-1} \frac{(N+f)!}{\alpha^{N+f}}
 \det\left[L_{N+f-1}^{(0)}(-\alpha
 a_{f'}^2)\right]_{f,f^\prime=1,\ldots,K} \ .
\label{chefformel}
\end{equation}
This result immediately yields the orthogonal polynomials
$p_n^{(N_f)}(x,M)$ and the partition function $Z_N^{(N_f)}(M)$.
