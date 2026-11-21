---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-006-31-homogeneous-degrees-of-r-matrices
section_title: "Homogeneous degrees of R-matrices"
section_number: 3.1
pages: 20-22
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.873
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
\Def
For non-zero $M,N \in R \gmod$, we denote by $\Lambda(M,N)$ the homogeneous degree of the R-matrix
$\rmat{M,N}$.
\edf

Hence
\eqn
&&\Rm_{M_z,N}:M_z \conv N \to   q^{-\Lambda(M,N)} N \conv M_z \quad \text{and}\\
&&\rmat{M,N}:M\conv N \to q^{-\Lambda(M,N)} N \conv M
\eneqn
are morphisms in $R\gMod$ and in $R \gmod$, respectively.



\Lemma \label{lem:tLa even}
 For non-zero $R$-modules $M$ and $N$, we have
\eqn
\Lambda(M,N) \equiv \bl\wt(M),\wt(N)\br \mod 2.
\eneqn
\enlemma
\Proof
Set $\beta\seteq-\wt(M)$ and $\gamma\seteq-\wt(N)$.
By \cite[(1.3.3)]{K^3}, the homogeneous degree of  $R_{M_z,N}$ is $-(\beta,\gamma)+2\inp{\beta,\gamma}$, where
$\inp{{\scbul,\scbul}}$ is the symmetric bilinear form on $\rootl$ given by
$\inp{\al_i,\al_j}=\delta_{ij}$.
Hence  $\Rm_{M_z,N}=z^{-s}R_{M_z,N}$  has degree $-(\beta,\gamma)+2\inp{\beta,\gamma}-2s$.
\QED

\Def
For non-zero $R$-modules $M$ and $N$, we set
\eqn
\tL(M,N) \seteq \frac{1}{2}\bl\Lambda(M,N) +(\wt(M), \wt(N))\br  \in \Z .
\eneqn
\edf





\Lemma\label{lem:selfdual}
Let $M$ and $N$ be self-dual simple modules.
If one of them is real, then
\eqn
q^{\tL(M,N)} M \hconv N
\eneqn
is a self-dual simple module.
\enlemma
\Proof
Set $\beta=\wt(M)$ and $\gamma=\wt(N)$.
Set $M \hconv N = q^c L$ for some self-dual simple module $L$ and some $c \in \Z$.
Then we have
\eqn
M \conv N \epito q^c L \monoto q^{-\Lambda(M,N)} N \conv M,
\eneqn
since $M \hconv N=\Im \rmat{M,N}$.
Taking dual, we obtain
\eqn
q^{\Lambda(M,N)+(\beta,\gamma)} M \conv N \epito q^{-c} L \monoto q^{(\beta,\gamma)} N \conv M.
\eneqn
In particular, $q^{-c-\Lambda(M,N)-(\beta,\gamma)} L $ is a simple quotient of $M\conv N$.
Hence we have $c=-c-\Lambda(M,N)-(\beta,\gamma)$, which implies $c= -\tL(M,N)$.
\QED

\Lemma \label{lem:composition}
\bni
 \item  Let $M_k$ be non-zero modules $( k=1,2,3)$, and let $\vphi_1: L \to  M_1\conv M_2$ and
$\vphi_2:  M_2 \conv M_3 \to L'$ be non-zero homomorphisms.  Assume further that $M_2$ is a simple module.
Then the composition
\eqn
L \conv M_3 \To[\vphi_1 \circ M_3] M_1 \conv M_2 \conv M_3 \To[M_1 \circ \vphi_2] M_1 \conv L'
\eneqn
does not vanish.
\item Let $M$ be a simple module and let $N_1, N_2$ be non-zero modules.
Then the composition
\eqn
M \conv N_1 \conv N_2 \To[\rmat{M,N_1} \circ N_2]
N_1  \conv M \conv N_2 \To[N_1 \circ \; \rmat{M,N_2}]
N_1 \conv N_2 \conv M
\eneqn
coincides with $\rmat{M,N_1 \circ N_2}$,
 and the composition
\eqn
N_1 \conv N_2 \conv M \To[N_1\circ\; \rmat{N_2,M}]
N_1  \conv M \conv N_2 \To[\rmat{N_1,M} \circ N_2]
 M \conv N_1 \conv N_2
\eneqn
coincides with $\rmat{N_1 \circ N_2,M}$.

In particular, we have
\eqn
\Lambda(M, N_1\conv N_2) = \Lambda(M,N_1)+\Lambda(M,N_2)
\eneqn
and
\eqn
\Lambda(N_1\conv N_2,M) = \Lambda(N_1,M)+\Lambda(N_2,M).
\eneqn
\end{enumerate}
\enlemma
\Proof
 (i)  Assume  that the composition vanishes. Then we have $\im \vphi_1 \conv M_3 \subset M_1 \conv \Ker \vphi_2$.
By Lemma \ref{lem:simplicity},
 there is a submodule $N$ of $M_2$
such that $\im \vphi_1  \subset M_1 \conv N$ and $N \conv M_3 \subset \Ker \vphi_2$.
The first inclusion implies that $N\neq 0$  since $\vphi_1$ is non-zero,  and the second  implies  $N\neq M_2$ since $\vphi_2$ is non-zero.
It contradicts  the simplicity of  $M_2$.

(ii) It is  enough to show that the compositions
$(N_1 \conv \rmat{M,N_2}) \circ (\rmat{M,N_1} \conv N_2)$ and
$ (\rmat{N_1,M} \conv N_2) \circ (N_1 \conv \rmat{N_2,M})$
 do not vanish, but these immediately follow from (i).
\QED
