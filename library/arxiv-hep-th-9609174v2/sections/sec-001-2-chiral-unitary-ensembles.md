---
doc_id: arxiv-hep-th-9609174v2
doc_title: "arXiv:hep-th/9609174v2 23 Sep 1996"
section_id: sec-001-2-chiral-unitary-ensembles
section_title: "Chiral unitary ensembles"
section_number: 2
pages: 4-5
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.974
doc_brief: "arXiv:hep-th/9609174v2 23 Sep 1996 — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom matrices in the microscopic limit."
---
In this section we consider the chiral unitary ensemble:
\begin{equation}
Z=\int \d M \, {\rm det}^{N_f} M\, \exp 
\left\{ -\frac{N}{2} {\rm tr}\, V(M^2) \right\},\ \ \ 
V(M^2)=\sum_{k\geq 1} \frac{g_k}{k}M^{2k},\ \ \ N_f=0,1,\cdots
\label{partition} 
\end{equation}
where $M$ stands for an $(N+N')\times (N+N')$ block hermitian matrix
whose non-zero components are $N\times N'$ complex matrices
on the off-diagonals,
\begin{equation}
M=
\left(
\begin{array}{cc}
0&W^\dagger\\
W&0
\end{array}\right)
\end{equation}
and $\d M$ the Haar measure of $W$.
We take  $N\leq N'$ without loss of generality.
An ensemble is called chiral unitary because of 
the invariance under the transformation
\begin{equation}
W\mapsto V^\dagger\,W\,U ~,~~ \ \ 
U \in {\rm U}(N) ~,~~ V \in {\rm U}(N').
\label{chi-inv}
\end{equation}
This model has the same global symmetries as
a Euclidean four-dimensional ${\rm SU}(N_c\! \geq \! 3)$ gauge theory
coupled to $N_f$ massless fermions in the fundamental representation.
The topological charge $\nu$ of the vacuum is identified with
$|\nu|=N'-N$ (which is kept fixed) and 
the volume of space-time is $V_4=N+N'$ (which is sent to infinity 
afterwards).
Specifically, due to the ``${\rm U}(1)_{\rm A}$ symmetry''
\begin{equation}
\{ M, \gamma_5\}=0,\ \ 
\gamma_5=
{
\left(
\begin{array}{cc}
1_N&0\\
0&-1_{N'}
\end{array}\right)},
\end{equation}
all ($2N$) non-zero eigenvalues $M$ 
occurs in pairs with opposite signs.

\vspace{12pt}\noindent
The partition function (\ref{partition}) is expressible in terms of
the component matrices
as well as of the eigenvalues after integration 
over the angular coordinates
$(U,V)\in{\rm U}(N)\times {\rm U}(N')/{\rm U}(1)^N$ \cite{Mor},
\begin{eqnarray}
Z&=&\int 
\d W\,
{\rm det}^{N_f}\left(W^\dagger W\right)\,
\e^{-N{\rm tr} V(W^\dagger W) }
\nonumber \\
&\propto&
\int_{-\infty}^\infty \prod_{i=1}^N 
\left( \d z^2_i\, z^{2\alpha}_i\,\e^{-N V(z_i^2) }\right)
\left|\det_{ij} z^{2(i-1)}_j \right|^2\cr &=&
\int_0^\infty \prod_{i=1}^N \left( \d\lambda_i\,\lambda^{\alpha}_i\, 
\e^{-N V(\lambda_i) }\right)
\left|\det_{ij} \lambda^{i-1}_j \right|^2 ~, \label{chUE1} 
\end{eqnarray}
where we have set $\alpha=N_f+|\nu|$ and suppressed an irrelevant
constant of the angular integration.
The above expression can be interpreted as a positive definite
$N\times N$ hermitian matrix model in $H=W^\dagger W$ whose 
eigenvalues are $\lambda_1,\cdots,\lambda_N\geq 0$.
Therefore the problem is reduced to finding 
a set of orthogonal polynomials 
$P_n^{(\alpha)}(\lambda)$
over the semi-infinite interval $[0,\infty)$ with the shown
weight function,
\begin{equation}
\int_0^\infty \d\lambda\, \lambda^\alpha\,\e^{-N V(\lambda) }
 P_n^{(\alpha)}(\lambda)\,P_m^{(\alpha)}(\lambda)=
 h^{(\alpha)}_n\, \delta_{nm} .
\label{orthochUE}
\end{equation}
The definition of the orthogonality relation (\ref{orthochUE})
shows that
the problem is well-defined for arbitrary real $\alpha > -1$. 
Here we shall only deal with $\alpha$ to be a nonnegative integer,
which is motivated physically from the above.

\vspace{12pt}\noindent
In the orthogonal polynomial method,
the polynomials $P^{(\alpha)}_n(\lambda)$
are usually normalized to be monic,
\begin{equation}
P_n^{(\alpha)}(\lambda) = \lambda^n + \cdots ~,
\end{equation}
so that the Vandermonde determinant $\det_{ij} \lambda^{i-1}_j$
can be substituted by $\det_{ij} P_{i-1}^{(\alpha)}(\lambda_j)$ 
in the integrand.
However, for the present purposes 
we will employ a different normalization
by demanding $P_n^{(\alpha)}(0) = 1$:
\begin{equation}
P_n^{(\alpha)}(\lambda) = 1+ \cdots + p^{(\alpha)}_n \lambda^n.
\label{normal}
\end{equation}
This is because we shall seek a smooth limiting
behavior near $\lambda = 0$ as $n$ gets as large as
$N$ (which is taken to infinity),
and $N^2 \lambda$ is kept fixed at the same time 
(the microscopic limit). 
We thus start by the assumption that
$P_n^{(\alpha)}(0) \neq 0$, 
and normalize the polynomials accordingly.\footnote{
We avoid a proliferation of new symbols by employing the same
$P^{(\alpha)}_n(\lambda)$ and $h^{(\alpha)}_n$
in both conventions.}
As we shall see shortly, 
this assumption is equivalent to having the origin 
included in the support of the spectral density.
