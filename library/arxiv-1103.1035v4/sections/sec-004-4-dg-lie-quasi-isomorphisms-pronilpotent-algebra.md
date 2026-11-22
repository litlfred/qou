---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-004-4-dg-lie-quasi-isomorphisms-pronilpotent-algebra
section_title: "DG Lie Quasi-isomorphisms – Pronilpotent Algebras"
section_number: 4
pages: 14-18
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.971
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:dg-quasi-comp}

In this section we extend \cite[Theorem 2.4]{GM} (attributed to Deligne) to the
case of complete noetherian local rings and unbounded DG Lie algebras. 
This is Theorem \ref{thm:2}.

Let $(R, \m)$ be a complete parameter algebra, and let
$\phi : \g \to \h$ be a DG Lie algebra quasi-isomorphism. 
As in Section \ref{sec:facts}, for any $j \in \N$ we write 
$R_j := R / \m^{j+1}$ and $\m_j := \m / \m^{j+1}$. We denote by 
$p_j : R \to R_j$ and $p_{j, i} : R_j \to R_i$ the canonical projections 
(for $j \geq i$).
Let $\n_j := \m^{j} / \m^{j + 1}$, which is an ideal in $R_j$ satisfying \lb
$\m_j \n_j = 0$ and 
\[ \n_j = \opn{Ker}(p_{j, j-1} : R_j \to R_{j - 1}) . \]
Thus $R_{j - 1} \cong R_j / \n_j$.

\begin{lem} \label{lem:6}
\begin{enumerate}
\item Let $\om \in  \opn{MC}(\g, R)$ and
$\chi := \phi(\om) \in \opn{MC}(\h, R)$.
Then the homomorphism of DG Lie algebras
\[ \phi :  (\m \hatotimes \g)_{\om} \to 
(\m \hatotimes \h)_{\chi} \]
is a quasi-isomorphism. 

\item The canonical function 
\[ \opn{MC}(\g, R) \to \lim_{\leftarrow j}\, \opn{MC}(\g, R_j) \]
is bijective.

\item For any $\om, \om' \in \opn{MC}(\g, R)$ the canonical function 
\[ \opn{G}^{\mrm{r}}(\g, R)(\om, \om') \to \lim_{\leftarrow j}\, 
\opn{G}^{\mrm{r}} ( \g, R_j) \bigl( p_j(\om), p_j(\om') \bigr) \]
is surjective.
\end{enumerate}
\end{lem}

Of course items (2-3) refer also to $\h$.

\begin{proof}
(1) We forget the Lie brackets. Let $M$ be the mapping cone of the homomorphism
of complexes of $R$-modules
\[ \phi :  (\m \hatotimes \g)_{\om} \to (\m \hatotimes \h)_{\chi} . \]
So 
\[ M = (\m \hatotimes \g)_{\om}[1] \oplus (\m \hatotimes \h)_{\chi} , \]
with a suitable differential. 
For any $j \geq 0$ let $\om_j := p_j(\om)$ and $\chi_j := p_j(\chi)$.
We have an inverse system of homomorphisms of complexes
\[ \phi_j :  (\m_j \hatotimes \g)_{\om_j} \to 
(\m_j \hatotimes \h)_{\chi_j} , \]
and we denote by $M_j$ the mapping cone of $\phi_j$.  
Then each $p_j : M \to M_j$ is surjective, and 
$M \cong \lim_{\leftarrow j}\, M_j$.
According to Lemma \ref{lem:5}(1) the complexes $M_j$ are acyclic. 
Therefore, using the Mittag-Leffler argument, the complex $M$ is also acyclic.

\medskip \noindent
(2) This is because $\m \hatotimes \g^1$ is $\m$-adically complete, and 
$\opn{MC}(\g, R)$ is a closed subset in it (w.r.t.\ the $\m$-adic metric).

\medskip \noindent
(3) Write $\om'_j := p_j(\om')$. 
Suppose we are given a sequence $\{ g_j \}_{j \in \N}$ of elements
\[ g_j \in \opn{G}^{\mrm{r}} ( \g, R_j)(\om_j, \om'_j ) \]
such that $p_{j, j-1}(g_j) = g_{j-1}$.
We are going to find a sequence $\{ \til{g}_j \}_{j \in \N}$ of elements
\[ \til{g}_j \in \opn{G} ( \g, R_j)(\om_j, \om'_j ) \]
such that $p_{j, j-1}(\til{g}_j) = \til{g}_{j-1}$
and $\eta_1(\til{g}_j) = g_j$ for all $j$.
Since the group $\opn{G}(\g, R)$ is 
complete w.r.t.\ its $\m$-adic filtration, the limit
\[ \til{g} := \lim_{\leftarrow j}\, \til{g}_j \in \opn{G}(\g, R) \]
exists; and by continuity 
$\til{g} \in \opn{G}(\g, R)(\om, \om')$.
Then the element
\[ g := \eta_1(\til{g}) \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om') \]
satisfies $p_j(g) = g_j$ for all $j$.

Here is the recursive construction of the sequence 
$\{ \til{g}_j \}_{j \in \N}$.
For $j = 0$ we take $\til{g}_0 := 1$. Now assume that $j \geq 1$ and we have a 
sequence $(\til{g}_0, \ldots, \til{g}_{j-1})$ as required.
Choose any element 
$\til{g}'_j \in \opn{G}(\g, R_j)(\om_j, \om'_j)$
such that $\eta_1(\til{g}'_j) = g_j$. 
Then 
\[ \eta_1(p_{j, j-1}(\til{g}'_j)) = p_{j, j-1}(\eta_1(\til{g}'_j)) = 
p_{j, j-1}(g_j) = g_{j-1} = \eta_1(\til{g}_{j-1}) . \]
There is some $\bar{a} \in N^{\mrm{r}}(\g, R_{j-1})_{\om_{j-1}}$
such that 
$\bar{a} \cdot p_{j, j-1}(\til{g}'_j) = \til{g}_{j-1}$.
Choose any $a \in N^{\mrm{r}}(\g, R_j)_{\om_j}$
lifting $\bar{a}$. Then 
$\til{g}_j := a \cdot \til{g}'_j$ will satisfy 
$p_{j, j-1}(\til{g}_j) = \til{g}_{j-1}$ and
$\eta_1(\til{g}_j) = g_j$.
\end{proof}

Here is the main result of this section. We denote the identity automorphism of
$R$ by $\bsym{1}_R$.

\begin{thm} \label{thm:2}
Let $(R, \m)$ be a parameter algebra over $\K$, and let $\phi : \g \to \h$ be a
DG Lie algebra quasi-isomorphism over $\K$. Then the function 
\[ \ol{\opn{MC}}(\bsym{1}_R \otimes \phi) : \ol{\opn{MC}}(\m \hatotimes \g) \to
\ol{\opn{MC}}(\m \hatotimes \h)  \]
is bijective. Moreover, the morphism of groupoids
\[ \mbf{Del}^{\mrm{r}}(\phi, R) : \mbf{Del}^{\mrm{r}}(\g, R) 
\to \mbf{Del}^{\mrm{r}}(\h, R)  \]
is an equivalence. 
\end{thm}

Observe that there are no finiteness nor boundedness conditions on $\g$ and
$\h$. 

\begin{proof}
We will prove these assertions:
\begin{enumerate}
\rmitem{a} The function $\ol{\opn{MC}}(\bsym{1}_R \otimes \phi)$
is surjective.

\rmitem{b}  The function $\ol{\opn{MC}}(\bsym{1}_R \otimes \phi)$
is injective.

\rmitem{c} For any 
$\om \in \opn{MC}(\g, R)$ the group homomorphism 
\[ \opn{G}^{\mrm{r}}(\phi, R) : \opn{G}^{\mrm{r}}(\g, R)(\om, \om) \to 
\opn{G}^{\mrm{r}}(\h, R) \bigl( \phi(\om), \phi(\om) \bigr) \]
is bijective. 
\end{enumerate}

Assertions (a-b) say that the function
$\ol{\opn{MC}}(\bsym{1}_R \otimes \phi)$
is bijective. Then assertion (c) implies that the function 
\[ \phi :  \opn{G}^{\mrm{r}}(\g, R)(\om, \om') \to 
\opn{G}^{\mrm{r}}(\h, R)(\phi(\om), \phi(\om')) \]
is bijective for every $\om, \om' \in \opn{MC}(\g, R)$.
Hence $\mbf{Del}^{\mrm{r}}(\phi, R)$ is an equivalence.

\medskip \noindent
Proof of (a). Here it is more convenient to work with the groupoids
$\mbf{Del}(-, -)$. 
Suppose we are given $\chi \in \opn{MC}(\h, R)$. We will find 
elements $\om \in \opn{MC}(\g, R)$ and 
$h \in \opn{G}(\h, R)(\phi(\om), \chi)$. 

Define $\chi_j := p_j(\chi) \in \opn{MC}(\h, R_j)$.
We are going to find a sequence $\{ \om_j \}_{j \in \N}$ of elements
$\om_j \in \opn{MC}(\g, R_j)$, and a sequence $\{ h_j \}_{j \in \N}$ of
elements
\[ h_j \in  \opn{G}(\h, R_j)(\phi(\om_j), \chi_j) , \]
such that $p_{j, j-1}(\om_j) = \om_{j-1}$ and 
$p_{j, j-1}(h_j) = h_{j-1}$ for all $j$.
This is done by induction on $j$.
For $j = 0$ we take $\om_0 := 0$ and $h_0 := 1 = \exp(0)$. 
Now consider $j \geq 1$. Assume that we have found sequences 
$(\om_0, \ldots, \om_{j-1})$ and 
$(h_0, \ldots, h_{j-1})$ satisfying the required conditions. 
By Lemma \ref{lem:1}, applied to the artinian local ring $R_j$,
and the elements $\chi_j, \om_{j-1}$ and $h_{j-1}$, 
there exist elements $\om_j$ and $h_j$ as required. 

Now the $R$-module $\m \hatotimes \g^1$ is $\m$-adically complete, 
and the set $\opn{MC}(\g, R)$ is closed inside 
$\m \hatotimes \g^1$ (with respect to the $\m$-adic metric). 
Hence the limit 
$\om := \lim_{\leftarrow j}\, \om_j$
belongs to $\opn{MC}(\g, R)$. 
The gauge group $\opn{G}(\h, R)$ is complete, since it is pronilpotent 
(with respect to its $\m$-adic filtration).
We get an element 
\[ h := \lim_{\leftarrow j}\, h_j \in \opn{G}(\h, R) . \]
By continuity we see that 
$\opn{Af}(h)(\phi(\om)) = \chi$.

\medskip \noindent
Proof of (b). Here we prefer to work with the groupoids
$\mbf{Del}^{\mrm{r}}(-,-)$.
Take $\om, \om' \in \opn{MC}(\g, R)$, and define 
$\chi := \phi(\om)$ and $\chi' := \phi(\om')$. 
Suppose we are given 
$h \in \opn{G}^{\mrm{r}}(\h, R)(\chi, \chi')$;
we will find 
$g \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om')$. 
(We do not care whether $\phi(g) = h$ or not.)

Define 
$\om_j := p_j(\om)$,
$\om'_j := p_j(\om')$,
$\chi_j := p_j(\chi)$,
$\chi'_j := p_j(\chi')$
and 
$h_j := p_j(h)$. 
We will find a sequence $\{ g_j \}_{j \in \N}$ of elements 
$g_j \in  \opn{G}^{\mrm{r}}(\g, R_j)(\om_j, \om'_j)$
such that 
$\phi(g_j) = h_j$
and 
$p_{j, j-1}(g_j) = g_{j-1}$.
Then, by Lemma \ref{lem:6}(3) there is an element 
$g \in \opn{G}^{\mrm{r}}(\g, R)(\om, \om')$
such that $p_j(g) = g_j$ for every $j$. 

We construct the sequence $\{ g_j \}_{j \in \N}$ by induction on $j$. For
$j = 0$ we take $g_0 := 1$. 
Now let $j \geq 1$, and suppose that we have a sequence 
$(g_0, \ldots, g_{j-1})$ as required. According to Lemma \ref{lem:2}, applied
to the artinian local ring $R_j$, there exists an element 
$g_j \in \opn{G}^{\mrm{r}}(\g, R_j)(\om_j, \om'_j)$
such that $p_{j, j-1}(g_j) = g_{j-1}$ and $\phi(g_j) = h_j$.

\medskip \noindent
Proof of (c). This is the complete version of the proof of Lemma \ref{lem:5}(2).
By Lemma \ref{lem:6}(1) the function 
$\mrm{H}^0(\phi_{R, \om})$ is bijective. The claim now follows from Proposition 
\ref{prop:2}.
\end{proof}

\begin{rem}
Assume $\g$ is abelian (i.e.\ the Lie bracket is zero), so that 
$\m \hot \g$ is just a complex of $R$-modules, and 
\[ \ol{\opn{MC}}(\g, R) = \mrm{H}^1 (\m \hot \g) . \]
In this case the Deligne groupoid $\mbf{Del}(\g, R)$ is the truncation 
\[ \cdots \to 0 \to \m \hot \g^0 \to 
\opn{Ker} \bigl( \d : \m \hot \g^{1} \to \m \hot \g^2 \bigr)
\to 0 \to \cdots , \]
whereas as the reduced Deligne groupoid $\mbf{Del}^{\mrm{r}}(\g, R)$
is the truncation
\[ \cdots \to 0 \to 
\opn{Im} \bigl( \d : \m \hot \g^{-1} \to \m \hot \g^0 \bigr)
\to 
\opn{Ker} \bigl( \d : \m \hot \g^{1} \to \m \hot \g^2 \bigr)
\to 0 \to \cdots , \]
both concentrated in the degree range $[0, 1]$.
Let $\h$ be another abelian DG Lie algebra. 
It is clear that a quasi-isomorphism of complexes $\phi : \g \to \h$ will
induce a quasi-isomorphism 
\[ \mbf{Del}^{\mrm{r}}(\phi, R) : 
\mbf{Del}^{\mrm{r}}(\g, R) \to \mbf{Del}^{\mrm{r}}(\h, R) . \]
This is a special case of Theorem \ref{thm:2}.
\end{rem}

\begin{rem} \label{rem:11}
Presumably Theorem \ref{thm:2} can be extended to the following more general
situation: $\g$ and $\h$ are $R$-linear DG Lie algebras, such that all the
$R$-modules $\g^i$ and $\h^i$ are $\m$-adically complete, and the graded Lie
algebras $\opn{gr}_{\m} (\g)$ and $\opn{gr}_{\m} (\h)$ are abelian. 
We are given an $R$-linear DG Lie algebra homomorphism 
$\phi : \g \to \h$ such that 
\[ \opn{gr}_{\m}(\phi) : \opn{gr}_{\m} (\g) \to \opn{gr}_{\m} (\h) \]
is a quasi-isomorphism. Then 
\[ \ol{\opn{MC}}(\phi) : \ol{\opn{MC}}(\g) \to \ol{\opn{MC}}(\h) \]
is bijective. Cf.\ \cite[Theorem 2.1]{Ge} for the corresponding nilpotent case.
\end{rem}
