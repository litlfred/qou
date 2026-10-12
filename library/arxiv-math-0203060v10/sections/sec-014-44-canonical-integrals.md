---
doc_id: arxiv-math-0203060v10
doc_title: "ON FUSION CATEGORIES"
section_id: sec-014-44-canonical-integrals
section_title: "Canonical integrals"
section_number: 4.4
pages: 16-18
source_pdf: 0203060v10.pdf
source_sha256: 2ccb480f4bd4a970
doc_brief: "ON FUSION CATEGORIES — Using a variety of methods developed in the literature (in pa rtic- ular, the theory of weak Hopf algebras), we prove a number of g eneral results about fusion categories in"
text_source: latex
latex_prose_ratio: 0.653
latex_coverage_ratio: 0.909
---
Using the squared antipode, one can construct integrals 
on a weak Hopf algebra $A$ called the {\em canonical integrals}. 
Namely, we have the following proposition, a particular case of which 
was proved in \cite{BNSz}. 

\begin{proposition}
\label{chi}
Let $A$ be a finite-dimensional weak Hopf algebra
and let $\{q_i\}$ be primitive central idempotents in $A_t$.
Then $\chi_i(h) := \Tr(L_h\circ S^2|_{AS(q_i)})$, where $L_h \in \End_k(A)$
is given by $L_h(x)=hx,\,h, x\in A$, defines a left integral in $A^*$
such that 
\begin{eqnarray}
\label{chi1}
\chi_i(q_j) &=& \Tr(S^2|_{q_jAS(q_i)})  \qquad \mbox{and } \\
\label{q-trace}
\chi_i(gh) &=& \chi(h S^2(g)),
\end{eqnarray} 
for all $g,h\in A$.
\end{proposition}

\begin{proof}
The identities \eqref{chi1} and \eqref{q-trace} follow immediately 
from the definition of $\chi$, since $A$ is regular and 
$S^2\circ L_g = L_{S^2(g)}\circ S^2$ for all $g\in A$.

Next, for all $\phi\in A^*$ we define $R_\phi \in \End_k(A)$
by $R_\phi(x) = x\actr \phi,\, x\in A^*$. 
Then $R_\phi(xS(q_i)) = R_\phi(x)S(q_i)$ so that $AS(q_i)$ is
$R_\phi$-invariant. A direct computation shows
that  $L_{(h \actr \phi)} = R_{\phi\1}\circ L_h \circ R_{S^{-1}(\phi\2)}$
for all $h\in A,\, \phi\in A^*$,
and hence,
\begin{eqnarray*}
(\phi \otimes \chi_i)(\Delta(h))
&=& \Tr(L_{(h \actr \phi)}\circ S^2|_{AS(q_i)}) \\
&=& \Tr( R_{\phi\1}\circ L_h \circ R_{S^{-1}(\phi\2)}\circ S^2|_{AS(q_i)}) \\
&=& \Tr( R_{\eps_t(\phi)}\circ  L_h \circ S^2|_{AS(q_i)}),
\end{eqnarray*}
therefore, $  (\id \otimes \chi_i)\Delta(h) =  
(\eps_t \otimes \chi)\Delta(h)$ for all $h\in A$, i.e., $\chi_i$
is a left integral in $A^*$.
\end{proof}



\subsection{Sufficient conditions for semisimplicity}

The next proposition is a refinement of \cite[Proposition 6.4]{N}
and is analogous to the Larson-Radford theorem \cite{LR1} for usual
Hopf algebras which says that if $A$ is a finite dimensional Hopf algebra
with $\Tr(S^2|_A)\neq 0$ then $A$ is semisimple and cosemisimple.

\begin{proposition}
\label{semisimplicity condition}
Let $A$ be a finite dimensional weak Hopf algebra. If for every
primitive idempotent $p$ in $A_t \cap Z(A)$ there exist 
idempotents $q_p,\, q_p'$ in $pA_t$ such that 
\begin{equation}
\label{Tr S2 neq 0}
\Tr(S^2|_{q_pAS(q_p')}) \neq 0,
\end{equation}
then $A$ is semisimple.
\end{proposition}

\begin{proof}
Let $\ell$ and $\lambda$ be a dual pair of non-degenerate left integrals
in $A$ and $A^*$ respectively. Then $(\ell\2 \actl \lambda) \otimes
q_p S^{-1}(\ell\1) S(q_p')$ is the dual bases tensor for $q_p A S(q_p')$,
cf.\ \cite{N}. Therefore,
\begin{eqnarray*}
0 &\neq& \Tr(S^2|_{q_pAS(q_p')}) \\
&=& \la \ell\2 \actl \lambda,\, q_p S(\ell\1)S(q_p') \ra \\
&=& \la \lambda,\, q_p \eps_s(q_p' \ell) \ra.
\end{eqnarray*}  
Therefore, $y_p:=\eps_s(q_p'\ell) \neq 0$. Next, we compute
\begin{eqnarray*}
y_p \ell
&=& S(\ell\1) S(q_p')\ell\2 \ell \\
&=& S(\ell\1) S(q_p') \eps_t(\ell\2) \ell \\
&=& S(\ell\1) \eps_t(\ell\2) S(q_p') \ell = S(\ell) y_p.
\end{eqnarray*}
Let $\xi_p$ be an element in $A^*_t$ 
(here and below we write $A^*_t:=(A^*)_t$, $A^*_s:=(A^*)_s$)
such that 
$\xi_p\actl 1 =y_p$. Then from the previous computation we have
\begin{equation}
y_p \ell = (\alpha \actl \ell) y_p,
\end{equation}
where $\alpha$ is a distinguished group-like element of $A^*$.
Arguing as in \cite[Proposition 6.4]{N} one gets
\begin{equation}
\xi_p = S(\xi_p) \alpha,
\end{equation}
whence $\alpha$ is trivial, i.e., $\alpha\in A^*_{\rm min}$.
This means that one can choose $\ell$ in such a way that $\alpha =\epsilon$,
i.e., $\ell = S(\ell)$. Hence, $y_p\in A_s \cap Z(A)$ is a non-zero multiple
of $p$. We conclude that $y :=\eps_s(\ell) =\sum_p\, y_p$ is an invertible
central element of $A$. Hence, $\ell' = y^{-1}\ell$ is a normalized
right integral in $A$. By Maschke's theorem, $A$ is semisimple.
\end{proof}

Let $q$ qnd $q'$ be idempotents in $A_t$, and let
$\rho = \epsilon \actr q$ and  $\rho' = \epsilon \actr q'$.
Then $\rho$ and $\rho'$ are idempotents in $A_t ^*$.

\begin{lemma}
\label{identify} 
The space $\rho A^* S(\rho')$ may be
identified, in an $S^2$-invariant way,
with the dual space  of $qAS(q')$.  
\end{lemma}

\begin{proof}
It is easy to check that for all $h\in A$ and $\phi\in A^*$
one has $\la \phi,\, qhS(q') \ra = \la \rho \phi S(\rho'),\, h\ra$,
whence the statement follows.
\end{proof}


The next three corollaries refine \cite[Corollaries 6.5 - 6.7]{N}.

\begin{corollary}
\label{dual semisimplicity condition}
Let $A$ be a finite dimensional weak Hopf algebra. If for every
primitive idempotent $\pi$ in $A^*_t \cap A^*_s$ there exist 
idempotents $\rho_\pi,\, \rho_\pi'$ in $\pi A^*_t$ such that 
\begin{equation}
\label{Tr S2 neq 0 dual}
\Tr(S^2|_{\rho_\pi A^* S(\rho_\pi')}) \neq 0,
\end{equation}
then $A$ is semisimple. 
\end{corollary}

\begin{proof}
This immediately follows from Proposition~\ref{semisimplicity condition}
and Lemma~\ref{identify}, since the latter
implies $\Tr(S^2|_{\rho_\pi A^* S(\rho_\pi')}) = \Tr(S^2|_{q_pAS(q_p')})$.
\end{proof}

\begin{corollary}
\label{Tr S2 connected}
Let $A$ be a connected finite dimensional weak Hopf algebra.
If there exist idempotents $q,\, q'$ in $A_t$
such that $\Tr(S^2|_{qAS(q')})\neq 0$ then $A$ is semisimple.
\end{corollary}

\begin{corollary}
\label{Tr S2 biconnected}
Let $A$ be a biconnected finite dimensional weak Hopf algebra.
If there exist idempotents $q,\, q'$ in $A_t$
such that $\Tr(S^2|_{qAS(q')})\neq 0$ then $A$ and $A^*$
are semisimple.
\end{corollary}

\end{section}



\begin{section}{$\Tr(S^2)$ and the global dimension}


\subsection{Proof of Theorem \ref{traceofS2}}

Let $A$ be a connected 
semisimple weak Hopf algebra. Then
$\mathcal{C} = \Rep(A)$ is a fusion category. 
In particular, $V^{**}$ is isomorphic to $V$ for any simple 
object $V$, which means that $S^2$ is an inner 
automorphism of $A$ (this is also proved in [BNSz, 3.22]).
So let $g\in A$ be such that
$S^2(x) = gxg^{-1}$ for all $x\in A$. Then $g|_V : V \to V^{**} : v \mapsto 
g\cdot v$ is an isomorphism of representations.

The calculation of $\Tr_V(g)$ and $\Tr_V((g^{-1})^*)$ yields
\begin{eqnarray}
\label{Tr no 1}
\Tr_V(g){\rm Id}_{A_t} &=& \Tr(S(g)1\1|_{V^*})1\2,\\ 
\label{Tr no 2}
\Tr_{V^*}((g^{-1})^*){\rm Id}_{A_t}&=&\Tr(g^{-1}1\1|_{V})1\2.
\end{eqnarray}

\begin{remark} We note an important distinction between the quantum trace in 
an object $V$ of a morphism $V\to V^{**}$, which is denoted 
by $\Tr_V$, and the usual trace of a linear operator in the vector space $V$, 
which is denoted just by $\Tr$. \end{remark}

Let $\{q_i\}$ be primitive idempotents in $Z(A_t)$
and for every $i$ let $n_i^2 = \dim_k(q_iA_t)$ (i.e.,
$n_i$ is the dimension of the irreducible representation
of $A_t$ corresponding to $q_i$).
Multiplying equations \eqref{Tr no 1} and \eqref{Tr no 2}
on the right by $q_j$ and $q_i$ respectively, 
applying $\Tr|_{A_t}$, 
and using that for a regular weak Hopf algebra
$\Tr(z|_{A_t}) = \epsilon(z)$ for all $z\in A_t$ \cite{N},
we get 
\begin{equation*}
\Tr_V(g)n_j^2=\Tr(g|_{q_jV}),\quad \Tr_{V^*}((g^{-1})^*)n_i^2=\Tr(g^{-1}|_{S(q_i)V}),
\end{equation*}
and hence,
\begin{equation}
\Tr(g|_{q_jV})\Tr(g^{-1}|_{S(q_i)V})=|V|^2n_i^2n_j^2.
\end{equation} 
Taking the sum over all isomorphism classes of simple $V$, we obtain : 
\begin{equation}
\label{TrS2 vs global dimension refined}
\Tr(S^2|_{q_jAS(q_i)}) = \dim(\Rep(A)) n_i^2 n_j^2.
\end{equation}
This proves the first statement of the theorem. The second one follows from 
Theorem \ref{posi}. Theorem \ref{traceofS2}  is proved. 


\subsection{Proof of Theorem \ref{dualcat}}

Let $\mC$ be a fusion category, and let 
$\mM$ be an indecomposable module category over $\mC$. 
Let us show that $\mC^*_{\mM}$ is semisimple. 

Choose a semisimple algebra $R$ with blocks labeled by simple objects 
of $\mM$. Let $F$ be the fiber functor 
$F:\mC\to R-\text{bimod}$ associated with $\mM,R$ as explained in Section 2. 
Let $A=\End_k(F)$ be the corresponding weak Hopf algebra. 
Consider the weak Hopf algebra $A^{*cop}$. The representation category of 
$A^{*cop}$ is $\mC^*_{\mM}$. Thus, $A^{*cop}$ is connected 
(as $\mM$ is indecomposable). So, $A$ is biconnected. Also, 
by Theorem \ref{traceofS2}, we have 
$\Tr(S^2|_{q_jAS(q_i)})=\dim(\mC)n_i^2n_j^2\ne 0$. 
Thus, by Corollary \ref{Tr S2 biconnected}, $A^{*cop}$, and hence 
$\mC^*_{\mM}$ is semisimple. The equality 
$\dim(\mC)=\dim(\mC^*_{\mM})$ follows from 
Theorem \ref{traceofS2} and Lemma \ref{identify}
(noting that the block sizes corresponding to the idempotents
$q$ and $\epsilon\actr q$ are the same). Theorem \ref{dualcat} is proved.
