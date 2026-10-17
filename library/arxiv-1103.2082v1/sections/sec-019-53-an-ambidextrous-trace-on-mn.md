---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-019-53-an-ambidextrous-trace-on-mn
section_title: "An Ambidextrous Trace on Mn"
section_number: 5.3
pages: 10-14
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.608
latex_coverage_ratio: 0.988
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
\label{SS:Mnambi}  Suppose $t\in F$ and $n>0$.   By Corollary~\ref{Mbasis}, to define a linear functional on $\End_{\uRep(S_t)}(M_n)$ it suffices to give the values of the linear functional on $s_n$ and $s_nx_ns_n$.  Let $\mt_n$ be the following linear map:
$$\begin{array}{rcl}
\mt_n:\End_{\uRep(S_t)}(M_n)&\to& F\\
s_n & \mapsto & 1\\
s_nx_ns_n&\mapsto&1\\
\end{array}$$ 
Notice that $\mt_1$ is the ambidextrous trace on $M_1=L(\Box)$ in $\uRep(S_0)$ studied in section \ref{0trace}.    
In this section we will show that $\mt_n$ is an ambidextrous trace on $M_n$ in $\uRep(S_t)$ for all $t\in F$, $n>0$.  To do so, we must examine the endomorphism ring $\End_{\uRep(S_t)}(M_n\otimes M_n)=(s_n\otimes s_n)FP_{2n}(t)(s_n\otimes s_n)$.  

For the remainder of this section assume $n>0$.
Given a partition diagram $\pi\in P_{2n}$, write $\pi_L$ (resp. $\pi_R$) for the partition diagram in $P_n$ obtained by restricting the partition $\pi$ to the vertices $\{1, 1',\ldots, n, n'\}$ (resp. $\{n+1, (n+1)',\ldots, 2n, (2n)'\}$).  
For example, 
$$\includegraphics{trace9.pdf}.$$  
Finally, let $\Theta_1, \Theta_2: P_{2n}\to \End_{\uRep(S_t)}(M_n)$ be the maps given by 
$$\includegraphics{trace10.pdf}.$$ The following lemma is the first of three lemmas concerning $\Theta_1$ and $\Theta_2$ which will be used to show that $\mt_n$ is an ambidextrous trace.


\begin{lemma}\label{Thzero}  Suppose $\pi\in P_{2n}$ is a partition diagram such that $\pi_L\not\in S_n\sqcup S_n^-$ or $\pi_R\not\in S_n\sqcup S_n^-$.  Then $\Theta_1(\pi)=0=\Theta_2(\pi)$.
\end{lemma}

\begin{proof} If $\pi_L\not\in S_n\sqcup S_n^-$ then (arguing as in the proof of Proposition~\ref{snprop}) there exists a transposition $\tau\in S_n$ with $\pi(\tau\otimes\id_n)=\pi$ or $(\tau\otimes\id_n)\pi=\pi$.  Thus $$\includegraphics{trace11.pdf}$$ In either case, by Proposition~\ref{snprop}(1), $\Theta_1(\pi)=-\Theta_1(\pi)$ and hence $\Theta_1(\pi)=0$ as the characteristic of $F$ is not 2.  Moreover, $$\includegraphics{trace12.pdf}$$ Using Proposition~\ref{snprop}(1) again, we have $\Theta_2(\pi)=-\Theta_2(\pi)$ so that $\Theta_2(\pi)=0$.  The proof when $\pi_R\not\in S_n\sqcup S_n^-$ is similar.
\end{proof}

Now for the second lemma on $\Theta_1$ and $\Theta_2$.  In this lemma, the symbol $\geq$ refers to the partial order on partition diagrams found in \cite[Section 2.1]{CO1}.

\begin{lemma}\label{lemmaSTP} Suppose $\pi\in P_{2n}$ is such that $\pi_L, \pi_R\in S_n\sqcup S_n^-$.  If $\pi_L$ (resp. $\pi_R$) is in $S_n^-$ then there exists a partition diagram $\pi'\in P_{2n}$ with $\pi'_L$ (resp. $\pi'_R$) in $S_n$ such that $\pi'_R\geq\pi_R$ (resp. $\pi'_L\geq\pi_L$) and $\mt_n(\Theta_i(\pi'))=\mt_n(\Theta_i(\pi))$ for $i=1,2$.
\end{lemma}

\begin{proof} Suppose $\pi_L\in S_n^-$ so that $\pi_L=\sigma_i$ for some $\sigma\in S_n$ and $i\in\{1,\ldots, n\}$.  Let $\pi'\in P_{2n}$ be the partition diagram obtained from $\pi$ by adding an edge between the vertices labelled $i$ and $\sigma(i)'$.  Then $\pi'\geq \pi$ which implies   $\pi'_R\geq \pi_R$.  Also, $\pi'_L=\sigma\in S_n$.  Moreover, given $\tau\in S_n$, the connected components of the graph \begin{equation}\label{tdp}\includegraphics{trace14.pdf}\end{equation} are all cycles.  Hence, as the graph of \begin{equation}\label{td}\includegraphics{trace15.pdf}\end{equation} is obtained from (\ref{tdp}) by deleting one edge, the partitions of $\{1, 1',\ldots, n, n'\}$ corresponding to the 
connected components of (\ref{tdp}) and (\ref{td}) are equal.  Therefore, $$\includegraphics{trace16.pdf}$$ for every $\tau\in S_n$.  Hence $$\includegraphics{trace17.pdf}$$ which implies $\Theta_2(\pi')=\Theta_2(\pi)$.  

Now, fix $\rho\in S_n$ and let $\mu_\rho, \mu_\rho'\in P_n$, $\ell(\rho), \ell(\rho)'\in\Z_{\geq0}$ be such that $$\includegraphics{trace18.pdf}.$$  Notice that $\ell(\rho)$ (resp. $\ell(\rho)'$) is the number of connected components of the partition diagram $\pi(\id_n\otimes \rho)$ (resp. $\pi'(\id_n\otimes \rho)$) which only contain vertices labelled by integers greater than $n$.  The connected components of $\pi$ and $\pi'$ (and hence of  $\pi(\id_n\otimes \rho)$ and $\pi'(\id_n\otimes \rho)$) which only contain vertices labelled by integers greater than $n$ are identical.  Hence $\ell(\rho)=\ell(\rho)'$.  Also, it is easy to see that $\mu_\rho\geq\pi_L$.  Thus, as $\pi_L\in S_n^-$, there are three cases:  (i) $\mu_\rho=\pi_L$, (ii) $\mu_\rho=\pi'_L$, (iii) $\mu_\rho\not\in S_n\sqcup S_n^-$.  Next, we show that $\mt_n(s_n\mu_\rho s_n)=\mt_n(s_n\mu'_\rho s_n)$ in each of the three cases above:

\noindent (i) If $\mu_\rho=\pi_L=\sigma_i$ then it is easy to see that $\mu'_\rho=\pi'_L=\sigma$.  Hence, by Proposition~\ref{snprop}(1)\&(3) and the definition of $\mt_n$, $\mt_n(s_n\mu_\rho s_n)=\sgn(\sigma)=\mt_n(s_n\mu'_\rho s_n)$.

\noindent (ii) If $\mu_\rho=\pi'_L$ then $\mu'_\rho=\pi_L'$ too.  Hence $\mt_n(s_n\mu_\rho s_n)=\mt_n(s_n\mu'_\rho s_n)$.

\noindent (iii) If $\mu_\rho\not\in S_n\sqcup S_n^-$ then $\mu'_\rho\not\in S_n\sqcup S_n^-$ too.  Therefore, by Proposition~\ref{snprop}(2), $\mt_n(s_n\mu_\rho s_n)=0=\mt_n(s_n\mu'_\rho s_n)$.

As $\rho$ was an arbitrary element of $S_n$, we have  $$\mt_n(\Theta_1(\pi))=\sum_{\rho\in S_n}\sgn(\rho)t^{\ell(\rho)}\mt_n(s_n\mu_\rho s_n)=\sum_{\rho\in S_n}\sgn(\rho)t^{\ell(\rho)'}\mt_n(s_n\mu'_\rho s_n)=\mt_n(\Theta_1(\pi')).$$
The statement of the lemma with $\pi_L\in S_n^-$ follows.  The proof when $\pi_R\in S_n^-$ is similar.
\end{proof}  

Before proving the third and final lemma on $\Theta_1$ and $\Theta_2$ we need to introduce a bit more notation.  
Suppose $\pi\in P_{2n}$ is such that $\pi_L, \pi_R\in S_n$.  Let $I=I_\pi\subset\{1,\ldots, n\}$ denote the set of all $i\in\{1,\ldots, n\}$ which correspond to vertices in $\pi$ whose parts are of size two.  Now let $\pi_{L-R}=\sigma_I$ where $\sigma\in S_n$ is any permutation with $\sigma(i)=j$ whenever the top vertices labelled by $i$ and $n+j$ are in the same part of $\pi$.  For example, 
$$\includegraphics{trace19.pdf}.$$
The following proposition concerning $\pi_{L-R}$ will be used in the proof of the final lemma on $\Theta_1$ and $\Theta_2$.

\begin{proposition}\label{piprop} Suppose $\pi\in P_{2n}$ is such that $\pi_L, \pi_R\in S_n$.  If $\pi'\in P_{2n}$ has $\pi'_L=\pi_L$, $\pi'_R=\pi_R$, and $\pi'_{L-R}=\pi_{L-R}$, then $\pi'=\pi$.
\end{proposition}

\begin{proof} Since $\pi_L, \pi_R\in S_n$, each part of $\pi$ is of one of the following three types:  (i) $\{i, j'\}$ with $1\leq i, j\leq n$; (ii) $\{i, j'\}$ with $n<i, j\leq 2n$; (iii) $\{i, j', k, l'\}$ with $1\leq i, j\leq n$ and $n<k, l\leq 2n$.  Hence $\pi$ is completely determined by $\pi_L, \pi_R$, and $\pi_{L-R}$.
\end{proof}

\begin{lemma}\label{lemmaSn} If $\pi\in P_{2n}$ is such that $\pi_L, \pi_R\in S_n$, then $\Theta_1(\pi)=\Theta_2(\pi)$.
\end{lemma}

\begin{proof} Write $I=I_\pi$ as above and let $\sigma\in S_n$ be any permutation with $\pi_{L-R}=\sigma_I$.  Let $\mu, \mu'\in P_{2n}$ be the following partition diagrams
$$\includegraphics{trace13.pdf}.$$ 
It is easy to check that $\mu_L=\pi_R=\mu'_L$, $\mu_R=\pi_L=\mu'_R$, and $\mu_{L-R}=(\sigma^{-1})_{J}=\mu'_{L-R}$ where $J=\{\sigma(i)~|~i\in I\}$.  Hence, by Proposition~\ref{piprop}, $\mu=\mu'$.  Also, by Proposition~\ref{snprop}(1), $\Theta_1(\pi)=\Theta_1(\mu)$. Therefore $\Theta_1(\pi)=\Theta_1(\mu)=\Theta_1(\mu')=\Theta_2(\pi)$.
\end{proof}

Now we prove the main result of this section.

\begin{theorem}\label{amb} $\mt_n$ is a nonzero ambidextrous trace on $M_n$ in $\uRep(S_t)$ for all $t\in F$, $n>0$.
\end{theorem}

\begin{proof} We are required to show $\mt_n(\Theta_1(\pi))=\mt_n(\Theta_2(\pi))$ for all $\pi\in P_{2n}$.  If either $\pi_L$ or $\pi_R$ is not in $S_n\sqcup S_n^-$ then the result follows from Lemma~\ref{Thzero}.  Hence we can assume $\pi_L, \pi_R\in S_n\sqcup S_n^-$.  If $\pi_L\in S_n^-$ then by Lemma~\ref{lemmaSTP} there exists $\pi'\in P_{2n}$ with $\pi'_L\in S_n$ and $\mt_n(\Theta_i(\pi'))=\mt_n(\Theta_i(\pi))$ for $i=1, 2$.  If $\pi'_R\not\in S_n\sqcup S_n^-$ then by Lemma~\ref{Thzero} we have $\mt_n(\Theta_i(\pi))=\mt_n(\Theta_i(\pi'))=0$ for $i=1, 2$; hence we can assume $\pi'_R\in S_n\sqcup S_n^-$.  If $\pi'_R\in S_n^-$ then by Lemma~\ref{lemmaSTP} there exists $\pi''\in P_{2n}$ with $\pi''_R\in S_n$, $\pi''_L\geq \pi'_L$, and $\mt_n(\Theta_i(\pi''))=\mt_n(\Theta_i(\pi'))$ for $i=1, 2$.  If $\pi''_L\not\in S_n\sqcup S_n^-$ then by Lemma~\ref{Thzero} we have $\mt_n(\Theta_i(\pi))=\mt_n(\Theta_i(\pi''))=0$ for $i=1, 2$; hence we can assume $\pi''_L\in S_n\sqcup S_n^-$.  Also, since $\pi''_L\geq \pi'_L$ and $\pi'_L\in S_n$ it follows that $\pi''_L\not\in S_n^-$.  Thus, we can assume $\pi''_L\in S_n$.  In this case, by Lemma~\ref{lemmaSn}, $\mt_n(\Theta_1(\pi))=\mt_n(\Theta_1(\pi''))=\mt_n(\Theta_2(\pi''))=\mt_n(\Theta_2(\pi)).$
\end{proof}

\begin{corollary}\label{C:nonzerotrace} If $t\in\Z_{\geq 0}$ then there exists a nonzero trace on the ideal of negligible objects in $\uRep(S_t)$.
\end{corollary}

\begin{proof} This follows from Theorem~\ref{T:ambitrace} and Theorem \ref{amb} that there is a nonzero trace on $\ideal_{M_{n}}$. By Corollary~\ref{Mneg} we have that $M_{n}$ is an object in $\ideal = \ideal (\mN )$ and, hence, $\ideal_{M_{n}} \subseteq \ideal$.  By Lemma~\ref{L:ideals} we have $J(\ideal_{M_{n}})$ is not the zero ideal and $J(\ideal_{M_{n}}) \subseteq J(\ideal)$.  By the classification of tensor ideals in $\uRep(S_t)$, $\mN$ is the unique proper tensor ideal of $\uRep(S_t)$.  Thus $J(\ideal_{M_{n}}) = J(\ideal)$ and by Lemma~\ref{L:ideals} $\ideal_{M_{n}}=\ideal$.  This proves the trace function is in fact defined on the entire ideal of negligible objects in $\uRep(S_t)$.
\end{proof}
\begin{remark}\label{R:SemisimpleCase}  When $t \notin \Z_{\geq 0}$ then $\uRep (S_{t})$ is a semisimple category \cite[Th\'eor\`eme 2.18]{Del07}.  Consequently, there are no proper ideals in $\uRep (S_{t})$ and the categorical trace is the only nontrivial trace. 
\end{remark}



\section{A Graded Variation on Deligne's Category}\label{S:quantumdouble} In this section we briefly examine a graded version of Deligne's category and show that it can be used to recover the writhe of a knot -- a well-known invariant of framed knots.



\subsection{}\label{SS:gradedvariant}   

Fix $t,q \in F $ with $q \neq 0$.  We then let $\gruRep_{0}(S_{t})=\gruRep_{0}(S_{t})_{q}$ be the category defined as follows.  The objects are all pairs $[a,b]$ for all $a,b \in \Z_{\geq 0}$.  We put a $\Z$-grading on the objects of the category by setting the degree of $[a,b]$ to be $a-b$.   

The morphisms are given by 
\[
\Hom_{\gruRep_{0}(S_{t})}\left([a,b],[c,d] \right) = \begin{cases}  FP_{a+b,c+d} , &\text{when $a-b=c-d$}; \\
0, &\text{else}.
\end{cases}
\]  The composition of morphisms is given by the same vertical concatenation of diagrams rule as in the definition of Deligne's category $\uRep_{0}(S_{t})$.  By definition the morphisms preserve the $\Z$-grading.


Define the tensor product on $\gruRep_{0}(S_{t})$ by 
\[
[a,b] \otimes [c,d] = [a+c, b+d]
\] and on morphisms by horizontal concatenation of diagrams just as in Deligne's category $\uRep_{0}(S_{t})$.   The associativity constraint is given by the identity.  

The unit object is then $\unit = [0,0]$ and the unit constraints $[0,0] \otimes [a,b] \to [a,b]$ and $[a,b] \otimes [0,0] \to [a,b]$ are given by the identity.

The dual of the object $[a,b]$ is given by
\[
[a,b]^{*}=[b,a].
\]  The evaluation morphism $\ev : [a,b]^{*} \otimes [a,b] \to \unit$ is given by a diagram in $FP_{2a+2b,0}$ which gives the evaluation morphism $[a+b]^{*} \otimes [a+b] \to \unit$ in $\uRep_{0}(S_{t})$.  Similarly, the coevaluation morphism $\coev : \unit  \to [a,b] \otimes [a,b]^{*}$ is given by the coevaluation in $\uRep_{0}(S_{t})$.

Let $\beta_{n,m}: [n] \otimes [m] \to [m] \otimes [n]$ be the diagram in $FP_{m+n, m+n}$ which gives the braiding in $\uRep_{0}(S_{t})$.  The braiding on $\gruRep_{0}(S_{t})$,
\[
c_{[a,b],[c,d]}: [a,b] \otimes [c,d] \to [c,d] \otimes [a,b],
\] is then given by 
\[
c_{[a,b],[c,d]} = q^{(a-b)(c-d)}\beta_{a+b,c+d}.
\]  The fact that this gives a braiding on the category follows from the calculation which shows that the $\beta$'s define a braiding in $\uRep_{0}(S_{t})$ along with the fact that morphisms in $\gruRep_{0}(S_{t})$ are grading preserving.  Also note that this braiding is usually \emph{not} symmetric.

Finally, the twist morphisms $\theta_{[a,b]} : [a,b] \to [a,b]$ are given by 
\[
\theta_{[a,b]}= q^{(a-b)^{2}}\Id_{a+b},
\] where $\Id_{a+b}$ is the identity in $FP_{a+b}$.  

A direct verification of the axioms shows that the above tensor product, unit, duality, braiding, and twists make $\gruRep_{0}(S_{t})$ into a ribbon category.  

Write $\gruRep (S_{t})$ for the Karoubian envelope of the additive envelope of $\gruRep_{0}(S_{t})$.  
The ribbon category structure on  $\gruRep_{0}(S_{t})$ defines a ribbon category structure on $\gruRep (S_{t})$ just as it does going from $\uRep_{0}(S_{t})$ to $\uRep (S_{t})$.  We also note that using the definition of the additive and Karoubian envelopes we see that the category $\gruRep (S_{t})$ inherits a $\Z$-grading and all morphisms are grading preserving. 

We have the following ``degrading'' functor between the graded and ungraded versions of Deligne's category.


\begin{proposition}\label{P:RelatingCats} Let $q \in  F \backslash \{0 \}$.
 Then there is a faithful functor 
\[
\F: \gruRep(S_{t})_{q} \to \uRep(S_{t}).
\] 


This functor is induced by the functor
\[
\F_{0}: \gruRep_{0}(S_{t})_{q} \to \uRep_{0}(S_{t})
\] given by setting
\[
\F_{0}([a,b])=[a+b]
\]
for all $a,b \in \Z_{\geq 0}$.  On morphisms, $\F_{0}$ is the identity; that is, for 
\[
f \in \Hom_{\gruRep_{0}(S_{t})}([a,b], [c,d]) \subseteq FP_{a+b,c+d},
\]
we set 
\[
\F_{0}(f) = f: [a+b] \to [c+d].
\] 

\end{proposition}

\begin{proof} The construction of the additive and Karoubian envelopes shows that $\F_{0}$ induces a functor $\F:\gruRep(S_{t})_{q} \to \uRep(S_{t})$. The statement about injectivity on morphisms follows from the fact that $\F_{0}$ is injective on morphisms and the construction of $\F$.


\end{proof}

\begin{remark}\label{R:degrading}  It is straightforward to verify that $\F$ is a tensor functor (i.e.\ $\F(X \otimes Y) = \F(X) \otimes \F(Y)$ for all objects $X$ and $Y$, $\F(\unit ) = \unit$, and preserves the associativity and unit constraints) and that it preserves duals (i.e.\ $\F(X^{*})=\F(X)^{*}$ for all objects $X$ and preserves the evaluation and coevaluation morphisms).  If $V,W$ are homogeneous objects in $\gruRep(S_{t})_{q}$ with $V$ of degree $r \in \Z$ and $W$ of degree $s \in \Z$, then 
\[
\F(c_{V,W}) = q^{r  s} c_{\F(V), \F(W)},
\] where $c_{\F(V), \F(W)}$ is the braiding in the category $\uRep(S_{t})$.  Similarly,
\[
\F(\theta_{V}) = q^{r^{2}}\theta_{\F(V)},
\] where $\theta_{\F(V)}$ is the twist in the category $\uRep(S_{t})$.

Thus the functor $\F$ preserves braidings and twists if and only if $q=1$ but, as we will soon see, it is close enough for our purposes.
\end{remark}


\begin{theorem}\label{T:gradedambis}  Let $V$ be an object of $\gruRep(S_{t})_{q}$ such that $\F(V)$ admits an ambidextrous trace 
\[
\mt_{\F(V)}: \End_{\uRep(S_{t})}(\F(V)) \to F .
\]  Then the map 
\[
\mt: \End_{\gruRep(S_{t})_{q}}(V) \to F 
\] given by $g \mapsto \mt_{\F(V)}(\F(g))$ defines an ambidextrous trace on $V$.
\end{theorem}

\begin{proof} Since both $\F$ and $\mt_{\F(V)}$ are linear, the map $\mt$ is linear and so without loss of generality we may assume $V$ is homogenous of degree $d \in \Z$.  Let $h \in \End_{\gruRep(S_{t})_{q}}(V \otimes V)$ and consider the morphism $\Tr_{R}(h): V \to V$.  Since $\F$ is a tensor functor, preserves evaluation and coevaluation, and takes the braiding and twist to a $q$ multiple of the braiding and twist, it follows that $\F(\Tr_{R}(h))$ is a $q$-multiple of $\Tr_{R}(\F(h))$.  A calculation using Remark~\ref{R:degrading} shows that in fact $\F(\Tr_{R}(h))=\Tr_{R}(\F(h))$. Similarly, $\F(\Tr_{L}(h))=\Tr_{L}(\F(h))$.  From this it is immediate that $\mt$ defines an ambidextrous trace.
\end{proof}

\begin{remark}\label{R:gradedambis}  Fix a nonnegative integer $n$ and fix $a,b \in \Z_{\geq 0}$ such that $a+b = n$.  Let $s_{n} \in FP_{n,n}$ be as in Equation \ref{E:sndef}.  Then $M_{a,b}:=([a,b], s_{n})$ is an object of $\gruRep(S_{t})_{q}$ and $\F(M_{a,b})=M_{n}$, the object of $\uRep(S_{t})$ defined in Section~\ref{SS:Mndef} and shown to admit an ambidextrous trace in Section~\ref{SS:Mnambi}.  By the previous theorem, the object $M_{a,b}$ in  $\gruRep(S_{t})_{q}$ admits an ambidextrous trace.  In particular, say we fix $a,b$ so that $a-b \neq 0$ and fix $q \in F$ not a root of unity\footnote{Otherwise we obtain the writhe modulo the order of $q$.}.  Then  $M_{a,b}$ is homogeneous of degree $a-b$ and it is not difficult to see that if $K$ is an oriented framed knot, then the invariant obtained by labeling $K$ by $M_{a,b}$ is the function 
\[
K \mapsto q^{(a-b)^{2}\omega},
\] where $\omega \in \Z$ is the \emph{writhe} of $K$.  


\end{remark}














\renewcommand{\bibname}{\textsc{references}} 
\bibliographystyle{amsalpha}	

	\addcontentsline{toc}{chapter}{\bibname}
