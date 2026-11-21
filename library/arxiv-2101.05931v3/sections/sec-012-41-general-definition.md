---
doc_id: arxiv-2101.05931v3
doc_title: "CATEGORICAL BRAID GROUP ACTIONS"
section_id: sec-012-41-general-definition
section_title: "General definition"
section_number: 4.1
pages: 10-11
source_pdf: 2101.05931v3.pdf
source_sha256: 41eaa81b97ede8e9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.93
doc_brief: "CATEGORICAL BRAID GROUP ACTIONS — Let g be a semisimple simply-laced Lie algebra of ﬁnite type."
---
\label{sec:pervdef}
Let $\cT$ be a triangulated category with shift functor $[1]:\cT \rightarrow \cT$. In the cases of most interest to us, $\cT$ is a subcategory of a derived category, in which case $[1]$ is the homological shift functor.
Suppose $\cT$ has a t-structure $t=(\cT^{\leq0},\cT^{\geq0})$, with heart $\cT^\heartsuit=\cT^{\leq0} \cap \cT^{\geq0}$ \cite{BBD}.  Recall that a triangulated functor $F:\cT \to \cS$ between triangulated categories with $t$-structure is \textbf{$t$-exact} if $F(\cT^{\leq0})\subseteq \cS^{\leq0}$ and $F(\cT^{\geq0})\subseteq \cS^{\geq0}$.  We let $F[p]: \cT \to \cS$ denote the pre-composition of $F$ with the $p$-shift $[p]$.


Now let $\cS \subset \cT$ be a thick triangulated subcategory, and consider the quotient functor $Q:\cT \to \cT/\cS$.  Following \cite{CRperv}, we say that $t$ is \textbf{compatible} with $\cS$ if $t_{\cT/\cS}=(Q(\cT^{\leq0}),Q(\cT^{\geq0}))$ is a t-structure on $\cT/\cS$.  By \cite[Lemmas 3.3 \& 3.9]{CRperv}, if $t$ is compatible with $\cS$ then $(\cT/\cS)^\heartsuit=\cT^\heartsuit/\cT^\heartsuit\cap \cS$, and  $t_\cS=(\cS\cap\cT^{\leq0},\cS\cap\cT^{\geq0})$ is a t-structure on $\cS$ such that $\cS^\heartsuit=\cT^\heartsuit\cap \cS$.

Now suppose that $\cT,\cT'$ are two triangulated categories with t-structures $t,t'$.  Suppose further that we have filtrations by thick triangulated subcategories:
\begin{align*}
0 \subset \cT_0 \subset \cT_1\subset \cdots\subset \cT_r=\cT ,\quad 0 \subset \cT_0' \subset \cT_1'\subset \cdots\subset \cT_r'=\cT', 
\end{align*}
such that for every $i$, $t$ is compatible with $\cT_i$ and $t'$ is compatible with $\cT'_i$. By \cite[Lemma 3.11]{CRperv}, $t_{\cT_i}$ is also compatible with $\cT_{i-1}$, and hence $\cT_i/\cT_{i-1}$ inherits a natural t-structure.  Let $p: \{0,\hdots,r\} \rightarrow \ZZ$.  The data $(\cT_\bullet, \cT'_\bullet, p)$ is termed a \textbf{perversity triple}.  

Although Chuang and Rouquier didn't formulate perverse equivalences for graded categories, it is straightforward to extend their definitions to this setting.

\begin{Definition}\label{def:PE}
A graded equivalence of graded triangulated categories $\sF:\cT\to\cT'$ is a \textbf{(graded) perverse equivalence} with respect to $(\cT_\bullet, \cT'_\bullet, p)$ if for every $i$, 
\begin{enumerate}
\item $\sF(\cT_i)= \cT_i'$, and
\item the induced equivalence $\sF[-p(i)]:\cT_i/\cT_{i-1}\to \cT_i'/\cT_{i-1}'$ is t-exact.
\end{enumerate}
\end{Definition}
For brevity, we say $\sF$ is \textbf{perverse} if it is a graded perverse equivalence with respect to some perversity datum.  Since we will be working exclusively in the graded setting, a perverse equivalence for us will always mean a graded perverse equivalence.    

A perverse equivalence $\sF:\cT\to\cT'$  induces a bijection $\varphi_\sF:\Irr(\cT^\heartsuit) \to \Irr(\cT^{\prime\heartsuit})$.  Indeed, by (2) $\sF[-p(i)]$ induces a bijection $\Irr(\cT_i^\heartsuit)\setminus \Irr(\cT_{i-1}^\heartsuit) \to \Irr(\cT_i^{\prime\heartsuit})\setminus \Irr(\cT_{i-1}^{\prime\heartsuit})$, and these yield $\varphi_\sF$.


Although the construction of $\varphi_\sF$ depends on a choice of perversity triple, the resulting bijection does not when $\cT^\heartsuit,\cT^{\prime\heartsuit}$ have finitely many simple objects.  This follows from the following lemma.
 

\begin{Lemma}[\cite{LosCacti}, Lemma 2.4]\label{lem:LosLem}
 Suppose that $\cT^\heartsuit,\cT^{\prime\heartsuit}$ have finitely many simple objects, and for $i=1,2$ let $\sF_i:\cT \to \cT'$ be a  perverse equivalence with respect to the perversity datum $(\cT_{i,\bullet}, \cT'_{i,\bullet}, p_i)$.  If the induced maps $[\sF_1],[\sF_2]:[\cT]_\ZZ \to [\cT']_\ZZ$ coincide then $\varphi_{\sF_1}=\varphi_{\sF_2}$.
 \end{Lemma}
 
 \begin{Corollary}
 Suppose that $\cT^\heartsuit,\cT^{\prime\heartsuit}$ have finitely many simple objects, and  $\sF:\cT \to \cT'$ is perverse.  Then $\varphi_\sF$ is independent of the choice of perversity triple.
 \end{Corollary}
 
 \begin{proof}
Suppose $\sF$ is a graded perverse equivalence with respect to two choices of perversity triples $(\cT_{i,\bullet}, \cT'_{i,\bullet}, p_i)$, $i=1,2$.  Now apply the lemma.
 \end{proof}
 
 The proofs of the following lemmas are straightforward.
 
 \begin{Lemma}\label{lem:pervshift}
 Suppose $\sF:\cT \rightarrow \cT'$ is perverse.  Then for any $\ell\in\ZZ$, $\sF[\ell]$ is also perverse and $\varphi_{\sF[\ell]}=\varphi_\sF$.
 \end{Lemma}
 
 \begin{Lemma}\label{lem:pervcomp}
 Suppose $\sF:\cT \rightarrow \cT'$ is a  perverse equivalence with respect to $(\cT_\bullet, \cT'_\bullet, p)$, and $\sG:\cT' \rightarrow \cT''$ is a  perverse equivalence with respect to $(\cT'_\bullet, \cT''_\bullet, q)$.  Then $\sG\circ \sF$ is a  perverse equivalence with respect to $(\cT_\bullet, \cT''_\bullet, p+q)$, and $\varphi_{\sG\circ \sF}=\varphi_\sG\circ\varphi_\sF$.
 \end{Lemma}
 
\begin{Lemma}\label{lem:quot}
Let $\cT,\cT'$ be triangulated with t-structures $t,t'$, and let $\cS\subset \cT, \cS'\subset \cT'$ be thick triangulated subcategories such that $t$ is compatible with $\cS$ and $t'$ is compatible with $\cS'$.  Suppose further that $\sF:\cT\to\cT'$ is a perverse equivalence with respect to $(\cT_\bullet, \cT'_\bullet, p)$, and $\sF(\cS)=\cS'$.  

Define $\cS_i=\cS\cap \cT_i, \cS_i'=\cS'\cap \cT_i'$ and  $(\cT/\cS)_i=Q(\cT_i), (\cT'/\cS')_i=Q'(\cT_i')$.  Let 
$\sG:\cS\to\cS'$ and $\sH:\cT/\cS \to \cT'/\cS'$ be the induced equivalences.  Then:
\begin{enumerate}
\item $\sG$ is a perverse equivalence with respect to $(\cS_\bullet, \cS'_\bullet,p)$, and $\varphi_{\sG}=\varphi_{\sF}|_{\Irr{\cS^\heartsuit}}$.
\item $\sH$ is a perverse equivalence with respect to $((\cT/\cS)_\bullet,(\cT'/\cS')_\bullet,p)$, and
$
\varphi_{\sH}=\varphi_{\sF}|_{\Irr{\cT^\heartsuit} \setminus \Irr{\cS^\heartsuit}}.
$
\end{enumerate}
\end{Lemma}

\begin{Lemma}[\cite{LosCacti}, Lemma 2.4]\label{lem:texactperv}
Suppose $\sF:\cT \rightarrow \cT'$ is perverse, and $\sG$ (respectively $\sG'$) is an autoequivalence of $\cT$ (respectively $\cT'$) which is t-exact up to shift.  Then $\sG'\circ \sF \circ \sG$ is perverse, and $\varphi_{\sG'\circ \sF \circ \sG}=\varphi_{\sG'}\circ\varphi_{\sF}\circ\varphi_{\sG'}$.  
\end{Lemma}

Note that in \cite[Lemma 2.4]{LosCacti}  is stated for functors which are t-exact.  Our formulation for functors which are t-exact up to shift follows by Lemma \ref{lem:pervshift}.
