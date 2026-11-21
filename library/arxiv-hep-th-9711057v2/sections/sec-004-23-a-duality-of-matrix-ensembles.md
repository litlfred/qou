---
doc_id: arxiv-hep-th-9711057v2
doc_title: "arXiv:hep-th/9711057v2 30 Apr 1998"
section_id: sec-004-23-a-duality-of-matrix-ensembles
section_title: "A duality of matrix ensembles"
section_number: 2.3
pages: 5-6
source_pdf: 9711057v2.pdf
source_sha256: acf5cdd7fe848f43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.989
doc_brief: "arXiv:hep-th/9711057v2 30 Apr 1998 — 11 sections: Front matter; Introduction; Random-matrix theory for finite qu"
---
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
