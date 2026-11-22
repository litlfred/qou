---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-013-72-sortings-and-the-jones-polynomial
section_title: "Sortings and the Jones polynomial"
section_number: 7.2
pages: 13-14
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.79
latex_coverage_ratio: 0.99
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
\lbl{sub.CJones}

Here we define admissible sortings and give a formula for the colored
Jones function in terms of them.


\begin{definition}
\lbl{def.AConf}
Fix a flow $f$ of $G_K$ and a natural number $n$. Let 
$P=(C,v)$ be an n-sorting of $f$. We say that $P$ is {\em admissible} if
\begin{itemize}
\item
For every two edges $e,e' \in F_r$ such that $v_e=v_{e'}$ and 
$e$ ends in vertex $i$ and $e'$ ends in vertex $j$ and $j \geq i$,
there exists an $l$, $i \leq l < j$ such that $e \not\in C_l$.
\end{itemize}
We denote by $\AC_n(f)$ the set of all admissible n-sortings of $f$,
and by $\Sev_n(G_K, f)$ the set of all lifts of $f$ to admissible subgraphs 
of $G_K^{(n)}$.
\end{definition}

The next lemma explains the notion of admissible sortings.

\begin{lemma}
\lbl{lem.ACconf}
There is a bijection $\Phi$ from $\AC_n(f)$ to $\Sev_n(G_K, f)$
such that $\b(\Phi(P))= b(P)$.
Moreover, if $P\in \AC_n(f)$  and $\pi$ is the projection to  $G_K$ 
then for each $e\in E_K$, the fixed total order on $F(e)$ agrees 
with the total order $(\pi^{-1}(e), \prec)$ introduced in Definition 
\ref{def.orderf}.
\end{lemma}

\begin{proof}
Let $P=(C,v)$, $C=(C_1,\dots, C_{r})$, and $P\in \AC_n(f)$.
In order to define
$\Phi(P)$ we will define the image $\Phi(P,e)$ for each $e\in F$.

First we  determine the ends of  the lifts of the red edges
as follows: if $e\in F_r$ then we let $t(\Phi(P,e))= a^{t(e)}_{v(e)+1}$.

Next we determine the blue edges of $\Phi(P)$ as follows:
if $1\leq i \leq r$ then we let 
$$
\{s(\Phi(P,e))\, |\,\, e\in F(e^b_i)\}= \{a^i_{v_e+1}\, | \,\, e\in C_i\}.
$$
This determines the beginnings of the  blue edges,
and hence also the ends of the blue edges.

 It remains to specify the beginnings of the lifts of the red edges. 
Since $P$ is admissible, observe that for each $1\leq i\leq r$, 
there are exactly $f(e^r_i)$ vertices $a^i_j$ of indegree $1$ in current
$\Phi(P)$. Hence it remains to make each of them starting vertex of exactly
one edge $\Phi(P,e)$, $e\in F(e^i_r)$. This
is uniquely determined by the 'moreover' part of the Lemma. 
This finishes the definition of $\Phi$. The equality for the weights 
follows easily, and the moreover part of the Lemma directly from the 
definition of $\Phi$. To finish the proof we find the inverse to $\Phi$.

Let $c\in \Sev_n(G_K, f)$. We construct $\Phi^{-1}(c)=(C(c), v(c))$ as follows:
 Let $e$ be an edge of $G_K$. There is an order preserving bijection between 
the 
fixed total ordering $(F(e),<)$ and  $(\pi^{-1}(e), \prec)$. If $e'$ is an 
edge 
of $c$ then we let $e'_F$ be the corresponding edge of $F$.

First let $e'$ be a red edge of $c$. We let $v(c)_{e'_F}= j$ where 
$t(e')=a^i_{j+1}$.
Hence $v(c)$ encodes the ends of the red edges of $c$.

Next we  define a predecessor $p(e)$ for each edge $e$ of $c$. 
If $e$ red then $p(e)=e$. If $e$ blue then $p(e)$ is the red edge of $c$ 
which terminates in the starting vertex of the longest blue path of $c$ 
whose last edge is $e$. Note that $p(e)$ always exists and is unique
since $c$ is admissible.

Finally for $1\leq i \leq r$ let $C_i=\{p(e)_F; e$ edge of $c$ that 
terminates in 
some $a^i_j$ that is a starting vertex of a blue edge of $c \}$.
This finishes the construction of $\Phi^{-1}$. 
\end{proof}

\begin{theorem}
\lbl{thm.sic5}
We have:
$$
J_n(K)(t) = t^{\d(K,n)}
\sum_{f\in \F(G_K)}
t^{\d(f)}\sum_{P\in \AC_n(f)}t^{\exc(P)}b(P) ,
$$
where $\exc(P)=\exc(\Phi(P))-\exc(f)$. 
\end{theorem}


\begin{proof}
We have:
\begin{eqnarray*}
J_n(K)(t) &=& 
t^{\d(K,n)} \sum_{c \in \Sev_n(G_K)} t^{\d(c)} \b(c) \\
&=&
t^{\d(K,n)} \sum_{f\in \F(G_K)}t^{\d(f)}
\sum_{c \in \Sev_n(G_K,f)}   t^{\exc(c)-\exc(f)}\b(c) \\
&=&
t^{\d(K,n)}
\sum_{f\in \F(G_K)}t^{\d(f)} \sum_{P\in \AC_n(f)}t^{\exc(P)}b(P)
\end{eqnarray*}
\end{proof}



\subsection{Proof of Theorem \ref{thm.main}}
\lbl{sub.proof}

\begin{definition}
\lbl{def.prd}
Let $e\in F_r$. We define set $P(f,e)$ as follows:
if $e\in F(e'), e_1\in F(e'_1)$ then $e_1\in P(f,e)$ if $t(e')= t(e'_1)= v$
and $e'_1<_v e'$, or $e'= e'_1$ and $e_1< e$ in our fixed total order of 
$F(e)$.
\end{definition}

\begin{definition}
\lbl{def.okk}
Let $e \in F_r$. We define
\begin{itemize}
\item
$\defect_1(C,v,e)= |\{e'\in P(f,e): v_{e'}< v_{e} \}|$,
\item
$\defect_2(C,v,e)= |\{e'\in C_{d(e)}: v_{e'}< v_{e} \}|$,
where $d(e)$ is the biggest index such that $d(e)\geq t(e)$
and $e\not\in C_{d(e)}$.
\end{itemize}
Recall that $t(e)$ denotes the terminal vertex of $e$.
\end{definition}



\begin{proposition}
\lbl{prop.gk2}
Let $P= (C,v)$ be an n-sorting of $f$. Then
$$
\exc(P)=\sum_{e\in F_r}\d_1(e)+\d_2(e),
$$
where 
$$
\d_1(e)=\begin{cases}
|P(f,e)|-\defect_1(C,v,e) & \text{ if $e$ starts in a $+$ vertex}
\\
-\defect_1(C,v,e) & \text{ if $e$ starts in a $-$ vertex},
\end{cases}
$$
$$
\d_2(e)= 
\begin{cases}
|C_{d(e)}|- \defect_2(C,v,e) &\text{ if } \quad \sign(d(e))=+ \\
- \defect_2(C,v,e) & \text{ if} \quad \sign(d(e))=-.
\end{cases}
$$
\end{proposition}
\begin{proof}
Let $e\in F_r$ and first assume $\sign(s(e))= +$. Then 
$$
\d_1(e)= |P(f,e)|- \defect_1(C,v,e)= 
|\{e': e'\in P(f,e)\cap F_r, v_{e}< v_{e'} \}|+ 
|\{e' \in C_{t(e)-1}: v_{e}< v_{e'} \}|.
$$
This equals, by definition \ref{def.XY} of function $X$ and by definition of 
bijection $\Phi$ in 
lemma \ref{lem.ACconf},  
$$
\sign(s(\Phi(e)))\sum_{e'\in F}X(\Phi(e), \Phi(e')).
$$
We proceed analogously if $\sign(s(e))= -$. Hence
$$
\sum_{e\in F_r}\d_1(e)= \sum_{e\in F_r}\sign(s(\Phi(e)))
\sum_{e'\in F}X(\Phi(e), \Phi(e')).
$$
Next we denote, for $e\in F_r$, by $D(e))$ the red edge of $\Phi(P)$ that 
starts at vertex
$a^{d(e)}_{v(e)+1}$.
Note that $D$ is a bijection between $F_r$ and the set of the red edges of 
$\Phi(P)$. 

Now let $\sign(d(e))=+$. Then $\d_2(e)$ equals the number of $e'\in C_{d(e)}$ 
such that
$v_e< v_{e'}$. This equals $\sign(d(e))\sum_{e'\in F}Y(D(e), \Phi(e'))$.
Again the case $\sign(d(e))= -$ is analogous.

Hence we get 
$$
\sum_{e\in F_r}\d_2(e)= \sum_{e\in F_r}\sign(d(e))\sum_{e'\in F}Y(D(e), 
\Phi(e')).
$$
This finishes the proof by lemma \ref{lem.exc2}.

\end{proof}




\begin{proof}(of Theorem \ref{thm.main})

We use Theorem \ref{thm.sic5}, Lemma \ref{lem.ACconf} and 
Proposition \ref{prop.gk2}:

$$
J_n(K)(t) = t^{\d(K,n)}
\sum_{f\in \F(G_K)}
t^{\d(f)}\sum_{P\in \AC(f,n)}t^{\exc(P)}b(P)=
$$
$$
t^{\d(K,n)}\sum_{f\in \F(G_K)}t^{\d(f)}
t^{n(f^-_b-f^+_b)}(1-t)^{f^-_r}(1-t^{-1})^{f^+_r}
$$
$$
 \prod_{e\in F^+_r} t^{-(n-1-|P(f,e)|)}
\prod_{e\in F_r, \sign(d(e))=+}t^{|C_{d(e)}|}
\sum_{(C,v) \in \AC(f,n)}\prod_{e\in F_r} t^{v_e-\defect_1(C,v,e)-
\defect_2(C,v,e)}.
$$
























Let us recall that
$$
\mult(f)_{q}= \prod_{v=1}^{r-2}\binom{f(v)}{f(e^b_v)}_{q^{\sign(v)}}.
$$

At this point, we will use Appendix \ref{sec.count}. By Theorem 
\ref{thm.sorstr} and 
Theorem \ref{thm.str10} we get 
$$
J_n(K)(t) = t^{\d(K,n)}
\sum_{f\in \F(G_K)}t^{\d(f)}
t^{n(f^-_b-f^+_b)}(1-t)^{f^-_r}(1-t^{-1})^{f^+_r}  t^{-(n-1)f^+_r} 
$$
$$
\prod_{e\in F^+_r} t^{|P(f,e)|}\prod_{e\in F_r, \sign(d(e))=+}t^{|C_{d(e)}|}
 \prod_{v=1}^{r}\binom{f(v)}{f(e^b_v)}_{t^{-1}} 
\prod_{e\in F_r}(n-|P(f,e)|)_t =
$$
$$
t^{\d(K,n)}\sum_{f\in \F(G_K)}t^{\d(f)}\prod_{v=1}^{r}
\binom{f(v)}{f(e^b_v)}_{t^{-1}}
\prod_{v:\sign(v)=+}t^{f(e^r_v)f(e^b_v)}
$$
$$
t^{n(f^-_b-f^+_b)}(1-t)^{f^-_r}(1-t^{-1})^{f^+_r}  t^{-(n-1)f^+_r}
\prod_{e\in F^+_r} t^{|P(f,e)|}
\prod_{e\in F_r}(n-|P(f,e)|)_t  =
$$
$$
t^{\d(K,n)}\sum_{f\in \F(G_K)}\mult_{t}(f)t^{\d(f)}t^{n(f^-_b-f^+_b)} 
(1-t)^{f^-_r}(1-t^{-1})^{f^+_r} 
\prod_{e\in F_r}(n-|P(f,e)|)_{t^{-\sign(s(e))}}=
$$
$$
t^{\d(K,n)}\sum_{f\in \F(G_K)}\mult_{t}(f)
t^{\d(f)} \prod_{v \in V_K} t^{-\sign(v)nf(e^b_v)}
\prod_{e \text{red};t(e)=v}\prod_{j=0}^{f(e)-1} 
(1-t^{-\sign(s(e))(n- j- \sum_{e'<_v e}f(e))}).  
$$
















This finishes the proof.
\end{proof}
