---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-016-62-graded-cases
section_title: "Graded cases"
section_number: 6.2
pages: 41-45
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.904
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipotent quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
Let $\rootl$ be a free abelian group equipped with a symmetric bilinear form
\eqn
( \ , \ ) : \rootl \times \rootl \to \Z \quad \text{such that} \
 (\beta,\beta) \in 2\Z \ \text{for all} \ \beta \in \rootl.
\eneqn
We consider  a $\coro$-linear abelian monoidal category $\shc$ satisfying
\eqref{cond:monoidal category} and the following conditions:
\eq
&&\hs{-2ex}\left\{\parbox{67ex}{
\bnum
\item We have a direct sum decomposition
  $\shc = \soplus_{\beta \in \rootl} \shc_\beta $ such that
 the tensor product $\otimes$
   sends  $\shc_\beta \times \shc_\gamma$ to $\shc_{\beta + \gamma}$
   for every  $\beta, \gamma \in \rootl$.

 \item There exists an object $Q  \in \shc_0$ satisfying
\bna
\item there is an isomorphism
$$R_{Q}(X) : Q \tensor X \isoto X \tensor Q$$
functorial in $X \in \shc$ such that
$$\xymatrix@C=7ex{
Q\tensor X\tensor Y\ar[r]_-{R_Q(X)}\ar@/^3ex/[rr]^{R_Q(X\tensor Y)}
&X\tensor Q\tensor Y\ar[r]_-{R_Q(Y)}
&X\tensor Y\tensor Q}$$
 commutes for any $X,Y\in \shc$,
\item the functor $X \mapsto Q \tensor X$ is an  equivalence of categories.
\end{enumerate}
\item for any $M$, $N\in\shc$, we have
$\Hom_\shc(M,Q^{\tens n}\tens N)=0$ except finitely many integers $n$.
\end{enumerate}
}\right.\label{cond:quantum monoidal category}
\eneq

We denote by $q$ the auto-equivalence $Q \otimes \scbul$ of $\shc$,
and call it the {\em grading shift functor}.

In such a case the Grothendieck group $K(\shc)$ is a $\rtl$-graded
$\Z[q^{\pm1}]$-algebra: $K(\shc)=\soplus_{\beta\in\rtl}K(\shc)_\beta$ where
$K(\shc)_\beta=K(\shc_\beta)$. Moreover, we have
$$K(\shc)=\soplus_{S}\Z[q^{\pm1}][S],$$
where $S$ ranges over  equivalence classes of
simple modules. Here, two simple modules $S$ and $S'$ are equivalent
if $q^nS\simeq S'$ for some $n\in\Z$.

\medskip
For $M\in\shc_{\beta}$, we sometimes write
$\beta=\wt(M)$ and call it the {\em weight} of $M$.
Similarly, for $x\in \Q(q^{1/2})\tens_{\Z[q^{\pm1}]}K(\shc_\beta)$,
we write $\beta=\wt(x)$ and call it the {\em weight} of $x$.

\begin{definition} \label{def:quantum monoidal seed}
We call a quadruple $\seed = (\{M_i\}_{i\in\K}, L,\widetilde B, D)$
a \emph{quantum monoidal seed  in $\shc$}
 if it satisfies the following conditions{\rm:}
\bnum
\item $\widetilde B = (b_{ij})_{i\in\K,\,j\in\Kex}$ is an  integer-valued $\K\times\Kex$-matrix
whose principal part is skew-symmetric,
\item $L=(\lambda_{ij})_{i,j\in\K}$ is an integer-valued skew-symmetric $\K\times\K$-matrix,
\item $D=\{d_i\}_{i\in\K}$ is a family of elements in $\rootl$,
\item $\{M_i\}_{i\in\K}$ is a family of simple objects such that $M_i \in \shc_{d_i}$ for any $i\in\K$,
\item $M_i \otimes M_j \simeq q^{\lambda_{ij}} M_j \otimes M_i$ for all $ i, j \in\K$,
\item $M_{i_1} \otimes \cdots \otimes M_{i_t}$ is simple for any
sequence  $(i_1,\ldots,i_t)$ in $\K$,
\item The pair  $(L,\widetilde B)$  is  compatible in the sense of \eqref{eq:compatible} with $d=2$,
\item $\lambda_{ij} - (d_i,d_j) \in 2\Z$ for all $i,j \in\K$,
\item $\displaystyle\sum_{i\in\K}b_{ik}d_i =0$ for all $k\in\Kex$.
\end{enumerate}
\end{definition}


Let  $\seed =(\{M_i\}_{i\in\K}, L,\widetilde B, D)$
be a  quantum monoidal seed.
For any $X\in\shc_\beta$ and $Y\in\shc_\gamma$ such that $X\otimes Y\simeq
q^{c}Y \otimes X$ and $c+(\beta,\gamma)\in2\Z$, we set
\eqn&&\tL(X,Y)=\frac{1}{2}\bl-c+(\beta,\gamma)\br\in\Z\eneqn
and
\eqn X\nconv Y\seteq q^{\tL(X,Y)}X\tens Y\simeq
q^{\tL(Y,X)}Y\tens X.\label{eq:balpro}\eneqn
Then $X\nconv Y\simeq Y\nconv X$.
For any sequence $(i_1,\ldots, i_\ell)$ in $\K$,
we define
$$\sodot_{s=1}^{\ell} M_{i_s}\seteq
(\cdots((M_{i_1}\nconv M_{i_2})\nconv M_{i_3})\cdots)\nconv M_{i_\ell}.$$
Then we have
\eqn
\sodot_{s=1}^{\ell} M_{i_s} =
q^{\frac{1}{2}\sum_{1\le u<v \le \ell}(-\lambda_{i_u i_v}  +(d_{i_u},d_{i_v}) ) } M_{i_1} \tensor \cdots \tensor M_{i_\ell}.
\eneqn
For any $w\in\sym_\ell$, we have
\eqn
&&\sodot_{s=1}^{\ell} M_{ i_{w(s)}}\simeq
\sodot_{s=1}^{\ell} M_{i_s}\eneqn
Hence for any subset $A$ of $\K$ and any set of non-negative integers
$\{m_a\}_{a\in A}$, we can define
$\sodot_{a\in A}M_a^{\snconv m_a}$.

For $(a_i)_{i\in\K}\in\Z_{\ge0}^\K$ and $(b_i)_{i\in\K}\in\Z_{\ge0}^\K$,
we have
$$\bl\sodot_{i\in \K}M_i^{\snconv a_i}\br\nconv
\bl\sodot_{i\in\K}M_i^{\snconv b_i}\br\simeq\sodot_{i\in \K}M_i^{\snconv (a_i+b_i)}.$$

\medskip
Let $\seed=(\{M_i\}_{i\in\K}, L,\widetilde B, D)$ be  a quantum monoidal seed.
When the $L$-commuting family $\{[M_i]\}_{i\in\K}$
of elements of $\Z[q^{\pm1/2}]\tens_{\Z[q^{\pm1}]}K(\shc)$
is algebraically independent,
we shall define a quantum seed
$[\seed]$ in $\Z[q^{\pm1/2}]\tens_{\Z[q^{\pm1}]}K(\shc)$
by
\eqn&&[\seed]=(\{q^{-(d_i,d_i)/4}[M_i]\}_{i\in\K}, L,\widetilde B).
\eneqn

Set
\eqn&&X_i:=q^{-(d_i,d_i)/4}[M_i].\label{eq:XM}
\eneqn
Then for any $\mathbf a=(a_i)_{i\in\K}\in\Z_{\ge0}^\K$, we have
$$X^{\mathbf a}=q^{-(\mu,\mu)/4}[\sodot_{i\in \K}M_i^{\snconv a_i}],$$
where $\mu=\wt(\sodot_{i\in \K}M_i^{\snconv a_i})=\wt(X^{\mathbf a})=\sum_{i\in \K}a_id_i$.

\medskip
For a given $k\in\Kex$, we define the \emph{mutation $\mu_k(D) \in \rootl^\K$ of $D$ in direction $k$ with respect to $\widetilde B$} by
\eqn
\mu_k(D)_i =d_i \ (i \neq k), \quad \mu_k(D)_k=-d_k+\sum_{b_{ik} >0}   b_{ik} d_i.
\eneqn
Note that
\eqn
\mu_k(\mu_k(D))=D.
\eneqn

Note also  that
$(\mu_k(L),\mu_k(\tB),\mu_k(D))$ satisfies conditions (viii) and (ix)
in Definition~\ref{def:quantum monoidal seed} for any $k\in\Kex$.

\medskip

We have the following
\Lemma\label{lem:decat} Set $X'_k=\mu_k(X)_k$, the mutation of $X_k$
as in \eqref{eq:quantum mutation}.
Set $\zeta=\wt(X'_k)=-d_k+\sum_{b_{ik}>0}b_{ik}d_i$.
Then we have
\eqn
&&\hs{-20ex}\ba{l}q^{m_k}[M_k] q^{(\zeta,\zeta)/4}X'_k=
q [\sodot_{b_{ik} >0} M_i^{\snconv b_{ik}}]+
[\sodot_{b_{ik} <0} M_i^{\snconv (-b_{ik})}],\\[2.5ex]
q^{m'_k} q^{(\zeta,\zeta)/4}X'_k[M_k]= [\sodot_{b_{ik} >0} M_i^{\snconv b_{ik}}]+
q[\sodot_{b_{ik} <0} M_i^{\snconv (-b_{ik})}],\ea
\eneqn
where
\eq
&&\hs{-10ex}\left\{\ba{l}
m_k=\dfrac{1}{2}(d_k,\zeta) +\dfrac{1}{2} \displaystyle
\sum_{b_{ik} < 0}\la_{ki}  b_{ik},
\\[1ex]
m'_k=\dfrac{1}{2}(d_k,\zeta) +\dfrac{1}{2} \displaystyle
\sum_{b_{ik} > 0} \la_{ki}b_{ik}.
\ea\right.\label{eq:mm'}
\eneq
\enlemma
\Proof
By \eqref{eq:XaXb}, we have
\eqn
X_k X^{\bf a} = q^{\frac{1}{2} \sum_{i \in \K} a_i \la_{ki}}  X^{{{\bf e}_k} +\bf a}
\quad \text{for ${\bf a}=(a_i)_{i\in\K} \in \Z^\K$ and
$({\bf e}_k)_i = \delta_{ik}$  ($i \in \K$).}
\eneqn
Let $\mathbf{a}'$ and ${\bf a}''$ be as in \eqref{eq:aa}. Because
\eqn
\sum_{i \in \K} a_i' \la_{ki} - \sum_{i \in \K} a_i'' \la_{ki}
= \sum_{b_{ik} >0} b_{ik} \la_{ki} - \sum_{b_{ik} <0} (-b_{ik}) \la_{ki}
= \sum_{i \in \K} b_{ik} \la_{ki} = 2,
\eneqn
 we have
\eqn
X_k X'_k = X_k(X^{{\bf a}'}  +   X^{{\bf a}''})
=q^{\frac{1}{2} \sum_i a_i'' \la_{ki} } (qX^{{\bf e_k}+{\bf a}'} + X^{{\bf e_k}+{\bf a}''}).
\eneqn
Note that
$
\wt(X^{{\bf e_k}+{\bf a}'}) =\wt(X^{{\bf e_k}+{\bf a}''})= d_k +\zeta.
$
It follows that
\eqn
m_k&=&-\dfrac{1}{4}((d_k,d_k)+(\zeta,\zeta))-\dfrac{1}{2} \sum_{i \in J} a_i'' \la_{ki} + \dfrac{1}{4}(\zeta+d_k,\zeta+d_k) \\
&=&\dfrac{1}{2} (d_k, \zeta) +\dfrac{1}{2} \sum_{b_{ik} <0} b_{ik} \la_{ki}.
\eneqn

One can calculate $m_k'$ in a similar way.
\QED

\begin{definition} \label{def:monoidal mutation}
We say that a quantum monoidal seed
$\seed =(\{M_i\}_{i\in\K}, L,\widetilde B, D)$
 \emph{admits a mutation in direction $k\in\Kex$} if
there exists  a simple object  $M_k' \in \shc_{\mu_k(D)_k}$
such that
\bni
  \item
there exist exact sequences in $\shc$
\eq
&&0 \to q \sodot_{b_{ik} >0} M_i^{\snconv b_{ik}} \to q^{m_k} M_k \tensor M_k' \to
 \sodot_{b_{ik} <0} M_i^{\snconv (-b_{ik})} \to 0,
\label{eq:ses graded mutation1} \\
 &&0 \to q \sodot_{b_{ik} <0} M_i^{\snconv(-b_{ik})} \to q^{m_k'} M_k' \tensor M_k \to
  \sodot_{b_{ik} >0} M_i^{\snconv b_{ik}} \to 0, \label{eq:ses graded mutation2}
\eneq
where $m_k$ and $m'_k$ are as in \eqref{eq:mm'}.
\item 
$\mu_k(\seed)\seteq\bl\{M_i\}_{i\neq k}\sqcup\{M_k'\},\mu_k(L),
\mu_k(\widetilde B), \mu_k(D)\br$ is
a quantum monoidal seed in $\shc$.
\end{enumerate}
We call $\mu_k(\seed)$ the {\em mutation} of $\seed$ in direction $k$.
\end{definition}

By Lemma~\ref{lem:decat}, the following lemma is obvious.
\Lemma
Let $\seed =(\{M_i\}_{i\in\K}, L,\widetilde B, D)$ be
 a quantum monoidal seed  which admits a mutation in direction $k\in\Kex$.
Then we have
$$[\mu_k(\seed)]=\mu_k([\seed]).$$
\enlemma

\begin{definition}
Assume that a $\coro$-linear abelian monoidal category
$\shc$ satisfies  \eqref{cond:monoidal category}
and \eqref{cond:quantum monoidal category}.
The category $\shc$ is called a
\em{monoidal categorification of a quantum cluster algebra $A$
over $\Z[q^{\pm1/2}]$}
if
\bnum
\item the Grothendieck ring $\Z[q^{\pm1/2}]\tens_{\Z[q^{\pm1}]} K(\shc)$ is isomorphic to $A$,
\item there exists a quantum monoidal seed
$\seed =(\{M_i\}_{i\in\K}, L,\widetilde B, D)$ in $\shc$ such that
$[\seed]\seteq(\{q^{-(d_i,d_i)/4}[M_i]\}_{i\in\K}, L, \widetilde B)$
 is a quantum seed of $A$,
\item $\seed$ admits successive mutations in all the directions.
\end{enumerate}
\end{definition}
Note that if $\shc$ is a monoidal categorification of a quantum cluster algebra
$A$, then any quantum seed in $A$ obtained by  a sequence of mutations from the initial quantum seed
is of the form
$(\{q^{-(d_i,d_i)/4}[M_i]\}_{i\in\K}, L, \widetilde B)$  for some quantum monoidal seed
$(\{M_i\}_{i\in\K}, L,\widetilde B, D)$.
 In particular, all the quantum cluster monomials in $A$ are the
classes of real simple objects in $\shc$ up to a power of $q^{1/2}$.
