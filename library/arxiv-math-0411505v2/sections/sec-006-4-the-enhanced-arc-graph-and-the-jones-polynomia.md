---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-006-4-the-enhanced-arc-graph-and-the-jones-polynomia
section_title: "The enhanced arc-graph and the Jones polynomial"
section_number: 4
pages: 7-8
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.974
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sub.enhanced}


In order to express the Jones polynomial as a function of the arc graph, we 
need to enhance the arc-graph as follows.

\begin{definition}
\lbl{def.rotten}
{\rm (a)}
We introduce a {\em linear order} $<_v$ on the set of
edges of $G_K$ terminating at vertex $v$ as follows. Recall that
$v$ corresponds to an arc $a_v$ of $K$. 
If we travel on $a_v$ along the orientation of $K$, we 'see' one by one the 
arcs corresponding to starting vertices of red arcs 
entering $v$: this gives the linear order of red arcs entering $v$. 
Finally there is at most one blue edge entering vertex $v$, and we make it 
less than all the red edges entering $v$. 
\newline
{\rm (b)}
If $f$ is a flow on $G_K$, we define the {\em rotation} and {\em excess}
number of $f$ by:
\begin{equation}
\lbl{eq.rotexc}
\rot(f)=\sum_{e\in E_K} f(e)\rot(e),
\qquad
\exc(f)=\sum_{v \in V_K} \sign(v) f(e^b_v) \sum_{e<_v e^r_v}f(e),
\qquad \d(f)=\exc(f)-\rot(f),  
\end{equation}
where $V_K$ and $E_K$ are the set of vertices and edges of $G_K$, and $\rot(e)$
is defined in Definition \ref{def.jjj}.
\end{definition}

Let $\Sev(G)$ denote the set of all subgraphs $C$ of $G$ such that each 
component
of $C$ is a directed cycle. Note that $\Sev(G)$ may be identified with a 
finite subset of $\F(G)$ since the characteristic function of $C$ is a flow.

The next theorem, due to Lin-Wang, expresses the Jones polynomial of
a knot projection $\K$ in terms of the enhanced arc-graph of $K$. 
For the sake of completeness we include
its proof in Appendix \ref{sec.LW}.

\begin{theorem}
\lbl{thm.arcjones}\cite{LW} 
For every knot projection $\K$ we have:
$$
J(\K, t)= t^{\d(K)} \sum_{c \in \Sev(G_K)} t^{\d(c)} \b(c).
$$
\end{theorem}

We now give a similar formula for the {\em colored Jones function} $J_n$ 
of a knot. 
We will normalize the colored Jones function so that it is the constant
sequence $\{1\}$ for the unknot, and $J_n$ is the quantum group invariant
of knots that corresponds to the $(n+1)$-dimensional irreducible representation
of $\mathfrak{sl}_2$.

Recall the operation of {\em cabling} $\K^{(n)}$ the knot projection 
$\K$ $n$ times.
 Recall that $a_1,\dots, a_{r+1}$ are the arcs of $\K$.
Each $a_l$ is in the cabling replaced by $n^2$ arcs $a^l_{i,j}$, 
$i,j=1,\dots, n$,
with the agreement that the 'long arcs' obtained by cabling arc $a_k$ will be
$a^k_{1j}$, $j=1,\dots, n$ and the 'small arcs' obtained by cabling of crossing
$k$ will be denoted by $a^k_{ij}$ for $i=2,\dots, n$ and $j=1,\dots, n$.
Note that all crossings which replace the original crossing $k$ have the
same sign, equal to the sign of the crossing $k$.
(see figure before Lemma \ref{lem.evenn}). 

We further let $K^{(n)}$ denote the link obtained from $\K^{(n)}$ by deletion
of the $n$ special long arcs $a^{r+1}_{1j}$, $j=1,\dots, n$.

\begin{theorem}
\lbl{thm.arcjonesn}
For every knot $\K$ and every $n \in \BN$, we have
$$
J_n(\K, t)=t^{\d(K, n)} 
\sum_{c \in \Sev(G_{K^{(n)}})}
t^{\d(c)} \b(c) 
$$
where $G_{K^{(n)}}$ is the arc graph of $K^{(n)}$.
\end{theorem}

\begin{proof}
Let $V_n$ denote the $(n+1)$-dimensional irreducible representation of the
quantum group $U_q(\mathfrak{sl}_2)$, and let $v_n$ denote a highest weight 
vector of $V_n$. Then, there is an inclusion $V_n \longto \otimes^n V_1$ that 
maps $v_n$ to a nonzero multiple of $\otimes^n v_1$.  

The result follows since cabling $\K$ corresponds to tensor product of 
representations and since $\w(\K^{(n)})=n^2 \w(\K)$ and $\rot(K^{(n)})=
n\, \rot(K)$. 
\end{proof}


For an integer $m$, we denote by 
$$
(m)_q=\frac{q^m-1}{q-1}
$$ 
the {\em quantum integer} $m$. This defines the 
{\em quantum factorial} and the {\em quantum binomial coefficients} by
$$
(m)_q!=(1)_q (2)_q \dots (m)_q
\qquad
\binom{m}{n}_q=\frac{(m)_q!}{(n)_q!(m-n)_q!}
$$
for natural numbers $m,n$ with $n \leq m$. We also define
$$
\mult_q(f)=\prod_v\binom{f(v)}{f(e_v^b)}_{q^{\sign(v)}}.
$$

\begin{theorem}
\lbl{thm.main}
For every knot projection $\K$ we have:
$$
J_n(\K,t) = t^{\d(K, n)}\sum_{f\in \F(G_K)}\mult_{t}(f)
t^{\d(f)} \prod_{v \in V_K} t^{-\sign(v)nf(e^b_v)} 
\prod_{e \text{red};t(e)=v}\prod_{j=0}^{f(e)-1} (1-t^{-\sign(s(e))
(n- j- \sum_{e'<_v e}f(e))}). 
$$
\end{theorem}



\begin{remark}
\lbl{rem.jo1}
It simply follows that the
contribution of a flow $f$ to the sum in Theorem \ref{thm.main} is non-zero 
only if $f(v)\leq n$ for each vertex $v$. Thus, in the above sum, only 
finitely many terms contribute. As a result, when $n=1$,
Theorems \ref{thm.main} and \ref{thm.arcjones} coincide. 
\end{remark}




\section{Proof of Theorem \ref{thm.nonc}}
\lbl{sec.prpr}

Theorem \ref{thm.main} is used in this section to prove the main 
Theorem \ref{thm.nonc}.
In the rest of the paper we then prove Theorem \ref{thm.main} from 
Theorem \ref{thm.arcjonesn}.
