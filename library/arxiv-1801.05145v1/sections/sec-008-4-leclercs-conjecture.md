---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-008-4-leclercs-conjecture
section_title: "Leclerc's conjecture"
section_number: 4
pages: 31-35
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.935
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
{\em In this section, $R$ is assumed to be a symmetric KLR algebra
over a base field $\cor$.}


\subsection{Leclerc's conjecture}

  The following theorem is a part of Leclerc's conjecture stated in the introduction.
\Th\label{th:leclerc}
Let $M$ and $N$ be simple modules.
We assume that $M$ is real.
Then we have
the equalities in the Grothendieck group $K(R\gmod)${\rm:}
\bnum
\item
$[M\conv N]=[M\hconv N]+\sum_{k}[S_k]$\\[.5ex]
with simple modules $S_k$ such that $\La(M,S_k)<\La(M,M\hconv N)=\La(M,N)$,
\item
$[M\conv N]=[ M\sconv N]+\sum_{k}[S_k]$\\[.5ex]
with simple modules $S_k$ such that $\La(S_k,M)<\La( M\sconv N,M)=\La(N,M)$,
\item
$[N\conv M]=[N\hconv M]+\sum_{k}[S_k]$\\[.5ex]
with simple modules $S_k$ such that $\La(S_k,M)<\La(N\hconv M,M)=\La(N,M)$,
\item
$[N\conv M]=[ N\sconv M]+\sum_{k}[S_k]$\\[.5ex]
with simple modules $S_k$ such that $\La(M,S_k)<\La(M, N \sconv M )=\La(M,N)$.
\ee
In particular, $M\hconv N$ as well as $ M \sconv N $ appears only once
in the Jordan-H\"older series of $M\conv N$ in $R\smod$.
\enth

The following result is an immediate consequence of this theorem.
\Cor\label{cor:compest}
Let $M$ and $N$ be simple modules.
We assume that one of them is real.
Assume that $M$ and $N$ do not commute,
Then we have
the equality in the Grothendieck group $K(R\gmod)$
$$[M\conv N]=[M\hconv N]+[ M\sconv N ]+\sum_{k}[S_k]$$
with simple modules $S_k$.
Moreover we have
\bnum
\item
If $M$ is real, then we have
$\La(M,  M\sconv N)<\La(M,N)$, $\La(M\hconv N,M)<\La(N,M)$ and
$\La(M, S_k)<\La(M,N)$, $\La(S_k,M)<\La(N,M)$.
\item
If $N$ is real, then we have
$\La(N, M\hconv N)<\La(N,M)$, $\La( M \sconv N, N)<\La( M,N)$ and
$\La(N, S_k)<\La(N,M)$, $\La(S_k,N)<\La(M,N)$.
\ee
\encor

\medskip

\Proof[Proof of Theorem~\ref{th:leclerc}]
We shall prove only (i).
The other statements are proved similarly.



$$M\conv N=K_0\supset K_1\supset \cdots\supset K_\ell\supset K_{\ell+1}=0.$$
Then we have
$K_0/K_1\simeq M\hconv N$.
Let us consider the
renormalized R-matrix
$\Rm_{M_z,M\circ N}=(M\conv\Rm_{M_z,N})\circ(\Rm_{M_z,M}\conv N)$
$$\xymatrix@C=10ex{
M_z\conv M\conv N\ar[r]^{\Rm_{M_z,M}\circ N}
&M\conv M_z\conv N\ar[r]^{M\circ\Rm_{M_z,N}}&M\conv N\conv M_z.}
$$
Then $\Rm_{M_z,M\circ N}$ sends $M_z\conv K_k$ to $K_k\conv M_z$ for any $k$.
Hence evaluating the above diagram at $z=0$, we obtain
$$\xymatrix@C=10ex{
M\conv M\conv N\ar[r]^{M\circ\rmat{M,N}}
&M\conv N\conv M\\
\wb{M\conv K_1}\ar[r]\ar@{^{(}->}[u] &\wb{K_1\conv M\,.}\ar@{^{(}->}[u]}
$$
Since $\Im(\rmat{M,N}\cl M\conv N\to N\conv M)\simeq (M\conv N)/K_1$,
we have
$\rmat{M,N}(K_1)=0$.
Hence, $\Rm_{M_z,M\circ N}$ sends $M_z\conv K_1$ to
$(K_1\conv M_z)\cap z\bl (M\conv N)\conv M_z\br
=z(K_1\conv M_z)$.
Thus $z^{-1}\Rm_{M_z,M\circ N}\vert_{M_z\circ K_1}$ is well defined.
Then it sends
$M_z\conv K_k$ to $K_k\conv M_z$ for $k\ge1$.
Thus we obtain an R-matrix
$$z^{-1}\Rm_{M_z, M\circ N}\vert_{M_z\circ(K_k/K_{k+1})}\cl
M_z\conv (K_k/K_{k+1})\to (K_k/K_{k+1})\conv M_z
\quad\text{for $1\le k\le \ell$.}$$
Hence we have
$$\Rm_{M_z, K_k/K_{k+1}}=z^{-s_k}z^{-1}\Rm_{M_z, M\circ N}\vert_{M_z\circ(K_k/K_{k+1})}$$
for some $s_k\in \Z_{\ge0}$.
Since the homogeneous degree of $\Rm_{M_z,M\circ N}$
is $\La(M,M\circ N)=\La(M,N)$, we obtain
$$\La(M,K_k/K_{k+1})=\La(M,N)-2(1+s_k)<\La(M,N).$$
\QED


Recall that the isomorphism classes of self-dual simple modules in $R \gmod$ are  parameterized by the crystal basis $B(\infty)$
(\cite{LV11}).
The following theorem is an application of the above theorem.

\Th \label{thm:divisible}
Let $\phi$ be an element of the Grothendieck group $K(R\gmod)$
given by
\eqn
\phi = \sum_{b \in B(\infty)} a_b [L_b],
\eneqn
where $L_b$ is the self-dual simple module corresponding to $b \in B(\infty)$ and $a_b \in \Z[q^{\pm1}]$.

Let $A$ be a real simple module in $R\gmod$.
Assume that we have an equality
\eqn
\phi [A] = q^l [A] \phi
\eneqn
in $K(R\gmod)$ for some $l \in \Z$.
Then $A$ commutes with $L_b$ and
\eqn
l= \La(A,L_b)
\eneqn
for  every $b \in B(\infty)$ such that $a_b \neq 0$.


\enth
\Proof
Note that we have
\eqn
\phi [A] = \sum_b a_b [L_b \conv A]
= \sum_b a_b ([L_b \hconv A] + \sum_k [S_{b,k}]) \quad \text{and} \\
q^l [A] \phi = q^l \sum_b a_b [A \conv L_b ]
= q^l \sum_b a_b (q^{\La(L_b,A)}[L_b \hconv A] + \sum_k [S^{b,k}]),
\eneqn
for some simple modules $S_{b,k}$ and $S^{b,k}$ satisfying
\eqn
\La(S_{b,k},A) < \La(L_b,A) \quad \text{and} \quad\La(S^{b,k},A) < \La(L_b,A)
\eneqn
by Theorem \ref{th:leclerc}.

We may assume that $\set{ b\in B(\infty)}{a_b \neq 0}\not=\emptyset$. Set
\eqn
t\seteq\displaystyle\max \set{ \La(L_b,A)}{ a_b \neq 0}.
\eneqn
By taking the classes of self-dual simple modules $S$ with $\La(S,A)=t$
in the expansions of $\phi [A]$ and $q^l [A] \phi$, we obtain
\eqn
\sum_{\La(L_b,A)=t} a_b [L_b \hconv A ]
=\sum_{\La(L_b,A)=t} q^l a_b q^{\La(L_b,A)} [L_b \hconv A ].
\eneqn
In particular, we have
$t=-l$.

Set
\eqn
t'\seteq\displaystyle\max \set{ \La(A,L_b)}{a_b \neq 0}.
\eneqn
Then, by a similar argument we have
$t'=l$.

It follows that

\eqn
0= t+t' \ge  \La(L_b,A) + \La(A,L_b)\ge0
\eneqn
for every $b$ such that $a_b \neq 0$. Hence $A$ and $L_b$ commute.

Since
\eqn \sum a_b ~ q^{\La(A,L_b)} [A\conv L_b]
 =\sum a_b [L_b \conv A]
=\phi [A]=q^l [A] \phi
 =q^l \sum a_b [A\conv L_b],
\eneqn
we have
\eqn
l=\La(A,L_b)
\eneqn
for any $b$ such that $a_b \neq 0$, as desired.
\QED

\Cor \label{cor:qcomm_module}
Let $M$ and $N$ be simple modules. Assume that one of them is real.
If $[M]$ and $[N]$ q-commute \ro i.e., $[M][N]=q^n[N][M]$ for some $n\in\Z$\rf, then
$M$ and $N$ commute. In particular, $M\conv N$ is simple.
\encor
The following corollary is an immediate consequence of the corollary above
and Theorem~\ref{thm:categorification 2}.
\Cor \label{cor:qcomm}
Assume that the generalized Cartan matrix $A$ is symmetric
and  that $b_1, b_2\in B(\infty)$ satisfy the conditions{\rm:}
\bni
\item one of  $G^\up(b_1)^2$ and $G^\up(b_2)^2$ is a member of the upper global basis
up to a power of $q$,
\item
$G^\up(b_1)$ and $G^\up(b_2)$ q-commute.
\ee
Then their product $G^\up(b_1)G^\up(b_2)$ is a member of the upper global basis
of $\Um$ up to a power of $q$.
\encor

\medskip
