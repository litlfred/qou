---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-016-the--operad-l
section_title: "The -operad L"
section_number: null
pages: 78-90
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.965
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:infoperad}
We now shift gears to the $(\infty,1)$-categorical setting. In this exploratory section, we aim to define an $\infty$-operad $\mathbb{L}^\otimes $ and conjecture it as equivalent to the connected part of the $\infty$-endomorphism operad $\operatorname{End}_{\Omega^2 \text{Bord}_3^{fr}}^\otimes (S^2) $. There is also an oriented version of the proposal. 

We will do this in steps: first we will briefly review the constructions of the $\infty$-little $n$-cube operad $\mathbb{E}_n^\otimes $, then we will define the $\infty$-operad $\mathbb{L}^\otimes $ and $\operatorname{End}_{\Omega^2 \text{Bord}_3}^\otimes (S^2) $, and lastly we will give two precise conjectures which state that there exists a map of $\infty$-operads which is an equivalence.

\begin{mycom}
When we say $\mathcal{C}$ is an $\infty$-category we mean either $\mathcal{C}$ is a complete Segal space or a quasi-category. Although it is usually clear from context which model we are referring, we will default to using quasi-categories unless specified otherwise.

Many influential work on the bordism categories were done in the model of ($n$-fold) complete Segal spaces such as\cite{lurie_classification_2008, Calaque_2019, scheimbauer2014factorization}, while $\infty$-operads were explored by \cite{LurieHigherAlgebra} in the model of quasi-categories. 

Both complete Segal spaces and quasi categories are valid models of $(\infty,1)$-categories, due to the fact that the homotopy theory of complete Segal spaces is the same as the homotopy theory of Quasi-categories, hence one loses nothing by choosing a model. In fact, one may move from one model to the other via \cite{joyal2007quasi} style constructions, such as theorem \ref{thm:JoyalTierney} in the appendix.
\end{mycom}

The following category will show up repeatedly in the section

\begin{defn} \label{defn:Fin*}
($\mathcal{F}in_*$) Let $\langle n \rangle = \left\{ *, 1, \dots ,n \right\} $. The Segal category of finite pointed set $\mathcal{F}in_*$ is defined to have 
\begin{enumerate}
\item objects are $\langle n \rangle $ for each $n\geq 1$.
\item a morphism $\alpha : \langle m \rangle \to \langle n \rangle  $ is a map such that  $\alpha (*)=*$.
\end{enumerate}

A morphism $\alpha : \langle m \rangle \to \langle n \rangle $ is \textit{inert} if for each $i \in 1, \dots ,n$, the inverse $\alpha ^{-1}(i)$ has only one element; it is \textit{active} if $\alpha ^{-1}(*) = \left\{ * \right\} $.
\end{defn} 

Recall that an $\infty$-operad as defined in \cite{lurie2017higheralgebra} is a morphism of $\infty$-categories \[
p: \mathcal{O}^\otimes \to N(\mathcal{F}in_*)
.\]
such that every inert morphism has $p$-coCartesian lifts, the inert morphisms $\rho ^i \langle n \rangle \to \langle 1 \rangle $ sending $i$ to $1$ and everything else to $*$ induce ``projection maps,'' and there is equivalence of $\infty$-categories $\mathcal{O}^\otimes _{\langle n \rangle } \to \mathcal{O}^n$ where $\mathcal{O}^\otimes _{\langle n \rangle } \equiv p ^{-1}(\langle n \rangle )$, $\mathcal{O} \equiv \mathcal{O}^{\otimes }_{\langle 1 \rangle }$. A precise definition is recorded in \ref{defn:infoperad}.





First let's recall the standard construction of the $\infty$-little k-cube operad $\mathbb{E}_k^ \otimes $. 

Let $\Box^k = (-1,1)^k $ be the $k$-dimensional open cube. We say an embedding $f: \Box^k \to \Box^k$ is rectilinear if it is given by \[
f(x_1 , \dots ,x_k) = (a_1 x_1 +b_1 , \dots , a_k x_k+b_k)
.\]
for some constants $a_i>0$ and $b_i$. For any finite set $S$, we say an open embedding $\Box^k \times S \to \Box^k$ is rectilinear if it is rectilinear on each connected component. Denote all such rectilinear embeddings as $\operatorname{Rect}(\Box^k \times S, \Box^k)$ and equip it with the subspace topology of $\mathbb{R}^{2k \mid S \mid }$. Note that the images of the $|S|$-many $\Box^k$ are disjoint by definition.

\begin{defn} \label{defn:Ek}
Let $^t \mathbb{E}_k^{\otimes }$ be the topological category defined as follows 
\begin{enumerate}
\item The objects are $\langle n \rangle $, the same as those of $\mathcal{F}in_*$ 
\item An arrow $f:\langle m \rangle \to \langle n \rangle $ consists of the following data:
\begin{enumerate}
\item a morphism $\alpha : \langle m \rangle \to \langle n \rangle $ in $\mathcal{F}in_*$.
\item for each $1\leq j\leq n$, a rectilinear embedding in \[
\operatorname{Rect}(\Box^k \times \alpha ^{-1}(j), \Box^k)
.\]
\end{enumerate}
\item The topology on the mapping spaces $\operatorname{Map}_{^t \mathbb{E}_3^\otimes }(\langle m \rangle , \langle n \rangle )$ is induced by the presentation \[
\operatorname{Map}_{^t \mathbb{E}_3^\otimes }(\langle m \rangle , \langle n \rangle ) = \coprod_{\alpha : \langle m \rangle \to \langle n \rangle } \prod_{1\leq j\leq n} \operatorname{Rect}(\Box^k \times \alpha ^{-1}(j), \Box^k)
.\]
\item The composition \[
\operatorname{Map}_{^t \mathbb{E}_3^\otimes }(\langle n \rangle , \langle n' \rangle ) \times \operatorname{Map}_{^t \mathbb{E}_3^\otimes }(\langle n' \rangle , \langle n'' \rangle ) \to \operatorname{Map}_{^t \mathbb{E}_3^\otimes }(\langle n \rangle , \langle n'' \rangle )
.\]
sends $\alpha : \langle n \rangle , \langle n' \rangle , \beta : \langle n' \rangle \to \langle n'' \rangle $ to $\beta \circ \alpha : \langle n \rangle \to \langle n'' \rangle $, and the rectilinear embeddings \[
f_j : \Box^k \times \alpha ^{-1}(j) \to \Box^k ,\quad f'_{j'}: \Box^k \times \beta ^{-1}(j') \to \Box^k
.\]
are sent to \[
f'_{j'} \circ (\coprod_{j \in \alpha ^{-1}(\beta ^{-1}(j'))} f_j) : \Box^k \times (\beta \circ \alpha ) ^{-1} (j') \to \Box^k
.\]
\end{enumerate}

We call $^t \mathbb{E}_k^{\otimes }$ the topological little $k$-cube operad.

Define the $\infty$-category $\mathbb{E}_k^\otimes $ as the topological nerve of $^t \mathbb{E}_k^\otimes $.
\end{defn}

\begin{prop}
$\mathbb{E}_k^\otimes $ is an $\infty$-operad.
\end{prop}










\begin{defn}
We call $\mathbb{E}_k^\otimes $ the $\infty$-little $k$-cube operad. 
\end{defn}

\begin{rmk}
There are many variations to definition \ref{defn:Ek} by replacing the spaces $\operatorname{Rect}(\Box^k \times \alpha ^{-1}(j), \Box^k)$ by some other ones. There are two important variants:
\begin{enumerate}
\item One may replace $\Box^k$ with $D^k$, and define a rectilinear embedding  $D^k \to D^k$ as one which extends to $\mathbb{R}^k \to \mathbb{R}^k$ as $v \mapsto \lambda v + v_0 $ for some $\lambda > 0$ and $v_0 \in \mathbb{R}^k$. That is, a uniform radial scaling and a translation. The resulting topological category is referred to as the ``little $k$-disk operad'' and its topological nerve is once again an $\infty$-operad, rightfully called the ``$\infty$-little $k$-disk operad.'' 

By \cite{may1997operads} and \cite{Lambrechts_Volić_2014}, for any finite set $S$ there is a canonical homotopy equivalence between $\operatorname{Rect}(\Box^k \times S, \Box^k)$, $\operatorname{Rect}(D^k \times S, D^k)$ and $\operatorname{Conf}_{|S|}(\mathbb{R}^k)$ the configuration space of $|S|$-many distinct points in $\mathbb{R}^k$. Hence the topological little $k$-cube operad is homotopy equivalent to the topological little $k$-disk operad. Passing through the homotopy coherent nerve gives an equivalence between the $\infty$-little $k$-cube operad and the $\infty$-little $k$-disk operad. 

\item One may replace $\Box^k$ with $D^k$, and define a ``projective isometry'' $f: D^k \to D^k$ as one which extends to $\mathbb{R}^k \to \mathbb{R}^k$ as $v \mapsto \lambda Rv + v_0 $ for some $R\in SO(k)$, $\lambda > 0$ and $v_0 \in \mathbb{R}^k$. That is, a rotation followed by a uniform radial scaling, then a translation. The resulting topological category $^t \mathbb{E}_{SO(k)}^\otimes $ is referred to as the ``framed little $k$-disk operad'' and its topological nerve $\mathbb{E}_{SO(k)}^\otimes $ is once again an $\infty$-operad, rightfully called the ``$\infty$-framed little $k$-disk operad.''

This operad (both the topological and the $\infty$-version) is not equivalent to the ordinary little $k$-disk/cube operad for $k\geq 2$. Heuristically speaking, the $SO(k)$ rotational information assigned to the embedded disks is the classifying space $BSO(k)$. When $k\geq 2$ this space is no longer contractible, hence the homotopy theory of projective isometries is different from the homotopy theory of rectilinear embeddings.

\item Similar to variation 2, one may further allow $R \in O(k)$ to include orientation reversal. The resulting topological category is denoted $^t \mathbb{E}_{O(k)}^{\otimes }$ and the topological nerve $\mathbb{E}^\otimes _{O(k)}$ is an $\infty$-operad.
\end{enumerate}
\end{rmk}

\begin{eg}
It is widely understood that $S^{k-1}$ is an $\mathbb{E}_k^\otimes $-algebra object in $\operatorname{Bord}_k^{fr}$. Precisely, this means that there is a map of $\infty$-operads \[
\mathbb{E}_k^{\otimes } \to \Omega^{k-1} \operatorname{Bord}_k^{fr, \otimes }
.\]
sending $\langle 1 \rangle $ to the object $S^2$. 

Additionally, $S^{k-1}$ is understood to be an $\mathbb{E}_{SO(k)}^\otimes $-algebra object in $\Omega^{k-1}\operatorname{Bord}_k^{SO(k), \otimes }$, and an $\mathbb{E}_{O(k)}^{\otimes}$-algebra object in $\Omega^{k-1}\operatorname{Bord}_k^{O(k), \otimes }$. \footnote{Note the infamous trap in naming conventions: associated to the \textit{framed} little $k$-disk operad is $S^{k-1}$ as an \textit{oriented} manifold.} Though, at the time of this writing, we are not aware of a thorough treatment in existing literature.
\end{eg}


Recall \cite{hatcher2008diffeomorphism}'s construction of the space of connect sum configurations:
\begin{notations}
Let $G$ be a graph and $v$ be a vertex. Let $HE(v) = DE(v) \cup E(v)$ be the set of half edges of $v$, written as a union of unpaired half edges $DE(v)$ and the paired half edges $E(v)$. We say $v$ has valency $|E(v)|$ and deficiency $|DE(v)|$.
\end{notations}

\begin{defn} \label{defn:C(M)}
($C(M)$) Let $M= P_1 \# \dots \#P_m \#(S^2\times S^1)^g$ be a closed oriented 3-manifold, where $P_i$ are oriented irreducible 3-manifolds. Let $G$ be a finite connected graph with $m$ of its vertices labelled $1, \dots , m$ and such that all unlabelled vertices have valence $\geq 3$ and the fundamental group is free of rank $g$. Let
\[
C_G(M) = \left\{ (r_e, l_e, D^3_e \hookrightarrow P_i, D_e^3 \hookrightarrow S^3_v ) \right\}
\]
over all edges $e$ and all unlabelled vertices $v$ of $G$, where $r_e>0, l_e>0 $ and embeddings $D^3_e \hookrightarrow P_i$ and $D^3_e \hookrightarrow S^3_v$, the latter being an isometry on its boundary. Let $\overline{C_G}(M)$ be the same as $C_G(M)$ except now allow $l_e$ to go to $0$. Let $G/e$ denote the graph by contracting the edge $e$. Then define \[
C(M) = \coprod_{G} \overline{C_G}(M) / \sim
.\]
where a configuration with $l_e=0$ is identified with the same one after contracting the edge $e$.
\end{defn}

The space $C(M)$ is best thought of as all the possible ways to ``build '' $M$ from $P_i$ factors. To incorporate spherical boundaries, we need to introduce unpaired half edges corresponding to $S^2$ boundaries, one of which is distinguished and corresponds to the outgoing boundary.

\begin{defn} \label{defn:C(M)par}
($C^{\partial, n}_{SO}(M)$) Let $M= P_1 \# \dots \#P_m \#(S^2\times S^1)^g$ be a closed oriented 3-manifold, where $P_i$ are oriented irreducible 3-manifolds. Let $G$ be a finite connected graph with $m$ of its vertices labelled $1, \dots , m$ and such that all unlabelled vertices have valence $\geq 3$ and the fundamental group is free of rank $g$, and such that it has $n+1$-many unpaired half edges, one of which is distinguished. Let
\[
C_{SO,G}^{\partial ,n}(M) = \left\{ (r_e, l_e, D^3_e \hookrightarrow P_i, D^3 \hookrightarrow S^3_v, D^3_\epsilon \hookrightarrow P_i, D^3_\epsilon \hookrightarrow S^3_v ) \right\}
\]
over all edges $e$ and all unpaired half edges $\epsilon$ and all unlabelled vertices $v$ of $G$, where $r_e>0, l_e>0 $ and embeddings $D^3_e \hookrightarrow P_i$ and $D^3_e \hookrightarrow S^3_v$, the latter being an isometry on its boundary. The half-edge embeddings $D^3_\epsilon \hookrightarrow P_i, D^3_\epsilon \hookrightarrow S^3_v $ are orientation-preserving and have disjoint images. Let $\overline{C_{SO,G}^{\partial ,n}}(M)$ be the same as $C_{SO,G}^{\partial ,n}(M)$ except now allow $l_e$ to go to $0$. Let $G/e$ denote the graph by contracting the edge $e$. Then define \[
C_{SO}^{\partial ,n}(M) = \coprod_{G} \overline{C_{SO}^{\partial ,n}}(M) / \sim
.\]
\end{defn}

The space $C^{\partial ,n}_{SO} (M)$ is $C(M)$ but now one remembers incoming and outgoing spherical boundary data. This is the oriented version-- all the irreducible factors are oriented, and all edge embeddings $D^3_e \hookrightarrow S^3_v, D^3_e \hookrightarrow P_i$ oriented, and the boundary embeddings $D^3_\epsilon \hookrightarrow S^3_v, D^3_\epsilon \hookrightarrow P_i$ (those corresponding to half edges) are also oriented. 

\noindent \textbf{Variation}
There exists an obvious variation, one where we upgrade the orientation to the more restrictive framed setting. Call the space $C^{\partial ,n}_{fr}(M)$, where $M$ is now a framed closed $3$-manifold, and the $P_i$ factors are also framed. All embeddings are framing-preserving embeddings. \footnote{We will be intentionally vague about this, since this is only a sketch definition.} 

\begin{rmk}
The definition for the configuration space of the un-oriented case is less straightforward, so we won't attempt to present it here. However, we can make some suggestions. Call this configuration space $C^{\partial ,n}_{O}(M)$, where $M= P_1 \# \dots \# P_m \#(S^2\times S^1)^g \# (S^2 \overset{\sim}{\times}S^1)^{g'}$. In the unoriented case there exists a reducible prime $S^2 \widetilde{\times} S^1$ which is a $S^2$ bundle over $S^1$, defined as \[
S^2 \widetilde{\times} S^1 = S^2 \times [0,1] / (x,0) \sim (r(x),1)
.\]
where $r:S^2 \to S^2$ is the antipodal map, in particular orientation reversing.\footnote{Unlike $S^2\times S^1$ where the identification can be made as $(x,0)\sim (x,1)$.} Hence we need the underlying graphs to have fundamental groups free of rank $g+g'$.

We would need the attaching tubes $D^3_e \times I_{e}$ as well as the orientation-reversing version of these tubes, defined as \[
\left( D^3_e \times I_e  \right) \coprod D^3 / (x,1) \sim r(x)
.\]
where $r:D^3 \times D^3$ is again the antipodal map.
\end{rmk}

Setting aside the issue of the unoriented configuration space, we define an operad which captures the information in the oriented configuration space:

\begin{defn} \label{defn:tL}
($^t \mathbb{L}^\otimes $) is a topological category defined as follows
\begin{enumerate}
\item The objects are $\langle n \rangle $, the same as $\mathcal{F}in_*$.
\item A morphism from $\langle m \rangle $ to $\langle n \rangle $ consists of the following data:
\begin{enumerate}
\item a morphism $\alpha : \langle m \rangle \to \langle n \rangle $ in $\mathcal{F}in_*$
\item for every $j = 1, \dots , n$, a non-negative integer $g_j \geq 0$ and an element $h_j \in \operatorname{BDiff}(\coprod_{i \in I_j} P_i)$, where $P_i$ are framed irreducible 3-manifolds.
\item for every $j=1, \dots ,n$, a framed connect sum configuration $f_j \in C^{\partial , \mid \alpha ^{-1}(j) \mid } _{fr}(M)$ where $M=\left( \#_{i\in I_j} P_i \right) \# (S^2\times S^1)^{g_j}$.
\end{enumerate}
\item Composition is given by
\begin{enumerate}
\item send $\alpha : \langle m \rangle \to \langle n \rangle $ and $\beta : \langle n \rangle \to \langle n' \rangle $ to the composition $\beta \circ \alpha : \langle m \rangle \to \langle n' \rangle $.
\item If $g_j\geq 0$, $h_j \in \operatorname{BDiff}(\coprod_{i \in I_j}P_i)$ for $j = 1, \dots , n'$ and $g_k\geq 0$, $h_k \in \operatorname{BDiff}(\coprod_{i \in I_k}P_{i})$ for $k = 1, \dots , n''$ are the data to be composed, their composition is given by $\overline{g}_k = g_k + \sum_{j \in \alpha ^{-1}(k)}^{ } g_j $ and $\overline{h}_k  $ is the image of $(h_j, h_k)_{j\in \alpha ^{-1}(k)}$ under the natural map \[
\left( \prod_{j \in \alpha ^{-1}(k)} \operatorname{BDiff}\left(\coprod_{i \in I_j} P_i \right) \right)  \times \operatorname{BDiff}\left(\coprod_{i \in I_k} P_i \right) \to \operatorname{BDiff}(\coprod_{i \in \cup_{j \in \alpha ^{-1}(k)} I_j \cup I_k}P_i ) 
.\]
\item If $f_j $ for $j = 1, \dots , n'$ and $f_k$ for $k=1, \dots , n''$ are the framed connect sum configurations over the graphs $G_j$ and $G_k$ respectively, their composition $\overline{f}_k$ is a configuration over the graph $\overline{G}_k$ obtained by connecting the incoming half-edges of $G_k$ with the outgoing half-edges of $\left\{ G_j, j\in \alpha ^{-1}(k) \right\}$. The configuration $\overline{f}_k$ itself is the union of the configurations $\left\{ f_j \right\}_{j\in \alpha ^{-1}(k)}$ and $f_k$.
\end{enumerate}
\end{enumerate}
\end{defn}

\begin{rmk}
The natural map in item 3.b requires some explaining. There is a natural map \[
\operatorname{BDiff}(X ) \times \operatorname{BDiff}(Y ) \to \operatorname{BDiff}(X \coprod Y ) 
.\]
which is induced by the natural map $\operatorname{Diff}(X ) \times \operatorname{Diff}(Y ) \to \operatorname{Diff}(X\coprod Y ) $. If $X$ is not diffeomorphic to $Y$, the target is just $\operatorname{Diff}(X ) \times \operatorname{Diff}(Y ) $ and this map is the identity. If $X$ is diffeomorphic to $Y$, however, the target now must include the diffeomorphism swapping the two, which is a separate path component from the identity component.

In our model of $\operatorname{BDiff}(X) = \operatorname{Emb}(X, \mathbb{R}^\infty) / \operatorname{Diff}(X ) $, we can give a geometric construction. Fix two embeddings \[
i_0, i_1 : \mathbb{R}^\infty \to \mathbb{R}^\infty
.\]
with disjoint images. Then send $[e_X] \in \operatorname{BDiff}(X ) = \operatorname{Emb}(X, \mathbb{R}^\infty) / \operatorname{Diff}(X ) $ and $[e_Y] \in \operatorname{BDiff}(Y )= \operatorname{Emb}(Y, \mathbb{R}^\infty) / \operatorname{Diff}(Y )  $ to the class of embedding $X \coprod Y \to \mathbb{R}^\infty$ given by \[
x \mapsto i_0 (e_X(x)) ,\quad y \mapsto i_1 (e_Y(y))
.\]
This is well defined because precomposing $e_X$ and $e_Y$ by diffeomorphisms corresponds to precomposing the union embedding by an element of $\operatorname{Diff}(X\coprod Y) $.
\end{rmk}

\textbf{Variation} Define $^t \mathbb{L}^\otimes _{SO}$ similarly, except now 2.b the $P_i$ are oriented irreducible 3-manifolds, and 2.c the configuration $f_j \in C^{\partial , \mid \alpha ^{-1}(j) \mid } _{SO}(M)$ is an oriented connect sum configuration.

\begin{defn} \label{defn:L}
Denote by $\mathbb{L}^\otimes $ the topological nerve of $^t \mathbb{L}^\otimes $, and by $\mathbb{L}^\otimes _{SO}$ the topological nerve of $^t \mathbb{L}^\otimes _{SO}$.
\end{defn}

\begin{prop}
The $\infty$-categories $\mathbb{L}^\otimes $ and $\mathbb{L}^\otimes _{SO}$ are $\infty$-operads.
\end{prop}

\begin{proof}
We show that $\operatorname{Sing}(^t \mathbb{L}^\otimes )$ is canonically isomorphic to the simplicial category $\mathcal{O}^\otimes $, constructed via \cite[Notation 2.1.1.22]{lurie2017higheralgebra}, of a fibrant simplicial coloured operad $\mathcal{O}$. Therefore $\mathbb{L}^\otimes = N(\operatorname{Sing}(^t \mathbb{L}^\otimes )) = N(\mathcal{O}^\otimes ) = N^\otimes (\mathcal{O})$ is the operadic nerve of $\mathcal{O}$, which by \cite[Proposition 2.1.1.27]{lurie2017higheralgebra} is an $\infty$-operad.

Let $\mathcal{O}$ be the simplicial coloured operad with a single object $D^3$, with  \[
\operatorname{Mul}_{\mathcal{O}}(\left\{ D^3 \right\} _{i\in I}, D^3) = \operatorname{Sing}(\operatorname{Map}_{^t \mathbb{L}^\otimes } (\langle n \rangle , \langle 1 \rangle )^a)
\]
where $a: \langle n \rangle \to \langle 1 \rangle $ is the unique active map, sending $*$ to $*$ and everything else to $1$, and $\text{Map}_{^t \mathbb{L}^\otimes }(\langle n \rangle , \langle 1 \rangle )^a$ is the subspace of morphisms with data $a$ as the map in $\mathcal{F}in_*$.



The singular complex of any topological space is Kan. So $\mathcal{O}$ is a fibrant simplicial one-coloured operad. By construction, there is a canonical isomorphism between $\operatorname{Sing}(^t \mathbb{L}^\otimes )$ and $\mathcal{O}^\otimes $. Hence $\mathbb{L}^\otimes $ is an $\infty$-operad.

The proof for the oriented version is analogous.
\end{proof}

The $\infty$-operad $\mathbb{L}^\otimes $ has a few notable sub-operads, induced by sub-categories of $^t \mathbb{L}^\otimes $. Same goes for the oriented version $\mathbb{L}_{SO}^\otimes $. We shall introduce them below and show that one of them is equivalent to $\mathbb{E}_3^{\otimes }$.

\begin{defn}
($^t \mathbb{L}^{*, \otimes }$) Consider the subcategory $^t \mathbb{L}^{*, \otimes }$ of the topological category $^t \mathbb{L}^{\otimes }$ defined by 
\begin{enumerate}
\item The objects are $\langle n \rangle $, the same as before and as those of $\mathcal{F}in_*$.
\item A morphism from $\langle m \rangle $ to $\langle n \rangle $ consists of the following data:
\begin{enumerate}
\item a morphism $\alpha : \langle m \rangle \to \langle n \rangle  $ in $\mathcal{F}in_*$.
\item for every $j=1, \dots ,n$, a framed connect sum configuration $f_j \in C^\partial _{fr, G}(S^3) \subset C^\partial _{fr}(S^3)$, where $G$ is the graph with a single vertex $v$ and $d\geq 1$ unpaired half-edges.
\end{enumerate}
\item The composition is the same as those of $^t \mathbb{L}^\otimes $.
\end{enumerate}
\end{defn}

\begin{rmk}
This is a subcategory of $^t \mathbb{L}^\otimes $ because we have chosen all $g_j$ to be $0$, and all $h_j \in \operatorname{BDiff}(\emptyset ) $ to be the unique point.\footnotemark{} Then $M$ ,which is supposed to appear in the configuration $C^\partial _{fr}(M)$, is now the unit under connect sum, which is $S^3$. 

\footnotetext{There is a unique function  $f: \emptyset \to \emptyset$ which is vacuously smooth and vacuously its own inverse. Hence $\operatorname{Diff}(\emptyset  ) = \left\{ f \right\}  $. Recall that our model for the classifying spaces is $\operatorname{BDiff}(M) \cong \operatorname{Emb}(M, \mathbb{R}^\infty) / \operatorname{Diff}(M ) $. There is only one map from the empty set to any (possibly empty) set: $e: \emptyset \to S$, which is vacuously a smooth embedding when $S = \mathbb{R}^\infty$. Hence $\operatorname{BDiff}((\emptyset) ) \cong * $ the one-point space in our model. } 
\end{rmk}

\begin{defn}
Let $\mathbb{L}^{*, \otimes }$ be the topological nerve of $^t \mathbb{L}^{*, \otimes }$. It is an $\infty$-operad. Moreover, it is an $\infty$-sub-operad of $\mathbb{L}^\otimes $.
\end{defn}

\begin{prop}
There is a canonical isomorphism between $^t \mathbb{L}^{*, \otimes }$ and $^t \mathbb{E}_3^\otimes $. 
\end{prop}

\begin{proof}
The two topological categories have the same objects. So we only need to show that they agree on morphisms. Fix a $j = 1, \dots , n$. A framed connect sum configuration $f_j \in C^{\partial }_{fr, G}(S^3)$ where $G$ is the single vertex $v$ graph with $d\geq 1$ unpaired half edges is a tuple \[
f_j = (D^3_\epsilon \hookrightarrow S^3)_{\epsilon \in DE(v)}
.\]
where the embeddings are rectilinear and whose images are disjoint. Here $ DE(v)$ is the set of half-edges at the only vertex $v$. We may delete the interior of the image of the rectilinear embedding $D^3_{\epsilon^!} \hookrightarrow S^ 3$ corresponding to the one distinguished half-edge $\epsilon^! \in DE(v)$. After which we are left with a collection of rectilinear disjoint embeddings \[
D^3_\epsilon \hookrightarrow (S^3 \setminus \operatorname{int}(im(D^3_{\epsilon^!})) )\cong D^3 ,\quad  \epsilon \in DE(v) - \epsilon^!
.\]
We may identify this with the morphisms of $^t\mathbb{E}_3^\otimes $\[
\operatorname{Rect}(D^3 \times \alpha ^{-1}(j), D^3)
.\]
where $d = |\alpha ^{-1}(j)| +1$.
\end{proof}


\begin{cor}
There is a canonical isomorphism of $\infty$-operads between $\mathbb{L}^{*, \otimes }$ and $\mathbb{E}_3^\otimes $. Moreover, $\mathbb{E}_3^\otimes $ is an $\infty$-sub-operad of $\mathbb{L}^\otimes $.
\end{cor}

Another sub-operad of interest is the ``spike ball'' operad, defined below.

\begin{defn}
(Spike Ball Operad) The ``spike ball'' operad $^t \mathbb{L}^{\bigstar, \otimes }$ is the subcategory of the topological category $^t \mathbb{L}^\otimes $ defined by 
\begin{enumerate}
\item The objects are $\langle n \rangle $, the same as before and as those of $\mathcal{F}in_*$.
\item A morphism from $\langle m \rangle $ to $\langle n \rangle $ consists of the following data:	
\begin{enumerate}
\item a morphism $\alpha : \langle m \rangle \to \langle n \rangle $ in $\mathcal{F}in_*$.
\item for every $j = 1, \dots , n$, an element $h_j \in \operatorname{BDiff}(\coprod_{i \in I_j} P_i ) $, where $P_i$ are framed irreducible $3$-manifolds.
\item for every $j=1, \dots , n$, a framed connect sum configuration $f_j \in C^{\partial , \mid \alpha ^{-1}(j) \mid }_{fr, G}(M) \subset C^{\partial, \mid \alpha ^{-1}(j) \mid } _{fr}(M)$, where $M = \#_{i \in I_j} P_i $, and $G$ is a graph with an unlabelled vertex $v$ and $\mid \alpha ^{-1}(j) \mid $ unpaired half edges at $v$, and connected to $v$ are $I_j$-labelled vertices. So $G$ is the star graph with one central vertex $v$ and $|I_j|$-many leaves, where $v$ also has $\mid \alpha ^{-1}(j) \mid $ unpaired half-edges.
\end{enumerate}
\item The composition is the same as those of  $^t \mathbb{L}^\otimes $.
\end{enumerate}

An example of the type of star graph $G$ can be found in figure \ref{fig:spikeball}-(a). 
Let $\mathbb{L}^{\bigstar, \otimes }$ be the topological nerve of $^t \mathbb{L}^{\bigstar, \otimes }$. It is an $\infty$-category and moreover an $\infty$-operad. Call it the ``$\infty$-spike-ball operad.''
\end{defn}

\begin{figure}[ht]
    \centering
    \incfig{spikeball}
    \caption[Spike ball operad example]{(a) An example of the star graph $G$ in the spike ball operad. In this particular case, $G$ has $\mid \alpha ^{-1}(j) \mid + 1 =3$ half edges, and $I_j=\left\{ 1,2 \right\} $ labelled vertices. (b) illustrate the particular bordism $[M] \in \operatorname{BDiff}( M) $represented by $G$ and the connect sum configuration $f$. The two dashed spheres are considered incoming, and the distinguished half edge is the big sphere, considered outgoing.}
    \label{fig:spikeball}
\end{figure}

\begin{rmk}
This is a subcategory of $^t \mathbb{L}^\otimes $ because we have chosen all $g_j$ to be $0$. Also note that $^t \mathbb{L}^{*, \otimes }$ is a subcategory of $^t \mathbb{L}^{\bigstar, \otimes }$, where for any $j = 1, \dots , n$, $I_j = \emptyset$ so there are no irreducible factors in $\operatorname{BDiff}(\coprod_{i \in I_j}P_i) $.
\end{rmk}

\begin{cor}
$\mathbb{E}_3^\otimes $ is an $\infty$-sub-operad of $\mathbb{L}^{\bigstar, \otimes }$.
\end{cor}


Lastly, we need to define the $\infty$-endomorphism operad of $S^2$. This is most easily done using complete Segal spaces as there is previous work by Calaque and Scheimbauer. 

\begin{defn} 
Let $V$ be a finite dimensional real vector space. Define $\left( P\Omega^{n-1}Bord_n^V \right)_k$ to be the set of tuples \[
(M, t_0, \dots , t_k)
.\]
such that
\begin{enumerate}
\item $t_0 \leq t_1 \leq \dots \leq t_k$ an ordered tuple of $k+1$ real numbers.
\item $M$ is a closed $n$-dimensional submanifold of $V \times \mathbb{R}$ and the composition $\pi :M \hookrightarrow V\times \mathbb{R} \twoheadrightarrow \mathbb{R}$ is proper.
\item For each $0\leq i\leq k$, and each $x\in \pi ^{-1}(t_i)$, the map $\pi $ is submersive at $x$.
\end{enumerate}
Viewing $\left( P\Omega ^{n-1}Bord_n^V \right)_k$ as a subspace of \[
\operatorname{Sub}(V\times \mathbb{R})\times \mathbb{R}^{k+1} ,\quad \operatorname{Sub}(V\times \mathbb{R}) = \coprod_{[M]} \operatorname{Emb}(M, V\times \mathbb{R}) / \operatorname{Diff}(M)
.\]
we equip it with the subspace topology.

Note that $\left( P\Omega^{n-1}Bord_n^V \right)_\bullet$ is a simplicial space. The simplicial face maps are given by forgetting a $t$, and the simplicial degeneracy maps are given by duplicating a $t$.
\end{defn}

Let $P\Omega^{n-1}Bord_n = \varinjlim_{V \subseteq \mathbb{R}^\infty} P\Omega^{n-1}Bord_n^V$. At the $k$-th level, we may think of it to consist of tuples \[
(M, t_0, \dots ,t_k)
.\]
where $M$ is now a closed $n$-dimensional submanifold of $\mathbb{R}^\infty$ (technically $\mathbb{R}^\infty \times \mathbb{R}$).

\begin{claim}
$P\Omega^{n-1}Bord_n$ is a Segal space.
\end{claim}

\begin{defn} 
We define the $(\infty,1)$ category of $n-1$ manifolds and bordisms as the completion of the Segal space $P\Omega^{n-1}Bord_n$. Loosely speaking this category consists of the following data:
\begin{itemize}
\item The objects are closed $n-1$ manifolds, corresponding to the $n-1$ dimensional preimage $\pi ^{-1}(t_0)\subset M$ where $M$ is an $n$-manifold.
\item The 1-morphisms are compact bordisms, corresponding to the $n$-dimensional preimage $\pi ^{-1}([t_0 ,t_1 ])\subset  M$.
\item The 2-morphisms are diffeomorphisms between bordisms.
\item The 3-morphisms are isotopes of diffeomorphisms
\item  $\dots $
\end{itemize}
\end{defn}

\textbf{Variations} By demanding the manifolds of $P\Omega^{n-1}\operatorname{Bord}_n$ be framed or oriented, we obtain the standard framed or oriented variations of $\Omega^{n-1}\operatorname{Bord}_n$, denoted as $\Omega^{n-1}\operatorname{Bord}_n^{fr}$  or $\Omega^{n-1}\operatorname{Bord}_n^{SO}$.

\begin{mycom}
There are a few versions of $PBord^V$ floating in the literature. They differ mostly on condition 3. The original sketch was proposed by \cite{lurie_classification_2008}, which was later corrected by \cite{Calaque_2019} . Our definition most closely resembles that of \cite{jordan2016topological}, which was adapted from \cite{Calaque_2019}.
\end{mycom}

\begin{rmk}
If $\mathcal{C}$ is a symmetric monoidal $(\infty,n)$-category with unit $\mathbf{1}$, then $\Omega \mathcal{C} = \operatorname{End}_{\mathcal{C}}(\mathbf{1})= \operatorname{Hom}_{\mathcal{C}}(\mathbf{1}, \mathbf{1}) $ is a symmetric monoidal $(\infty,n-1)$-category. As the notation suggests, $\Omega^{k-1} Bord_k$ has an alternative construction as the $k-1$ looping of the $(\infty,k)$-category $Bord_k$. In fact, this construction is more precise than the one we presented above-- see \cite{Calaque_2019} if our presentation is insufficient.
\end{rmk}

\begin{rmk}
The $(\infty,1)$-category $\Omega^{n-1}Bord_n$ inherits a symmetric monoidal structure from $Bord_n$. We shall be intentionally vague about what we mean by ``symmetric monoidal structure.'' Beyond the heuristics of disjoint union, a precise definition can be found in [Scheimbauer]. The symmetric monoidal category $\Omega^{n-1}Bord_n$ determines 
\footnote{More precisely, one extracts a quasi-category via [Joyal Tierney]. This quasi-category is the $\infty$-category which is symmetric monoidal in the sense of Lurie HA, and it is the underlying $\infty$-category of the $\infty$-operad $\Omega^{n-1}Bord_n^\otimes$.} 
an $\infty$-operad $p: \Omega^{n-1}Bord_n^\otimes \to N(\mathcal{F}in_*)$. Roughly speaking, the fibre of $p$ over $\langle m \rangle $ consists of $m$-tuples of $n-1$ dimensional closed manifolds, and a morphism over $\alpha : \langle m \rangle \to \langle m' \rangle $ is a bordism. 
\end{rmk}

\begin{defn} \label{defn:Endomorphism operad}
(Endomorphism operad) Given $p: \mathcal{C}^\otimes \to N(\mathcal{F}in_*)$ be an $\infty$-operad, and let $X \in \mathcal{C}$ be an object. By definition there is an equivalence $\mathcal{C}^\otimes _{\langle n \rangle } \cong \mathcal{C}^n$ induced by the inert maps $\rho^i : \langle n \rangle \to \langle 1 \rangle $. Let $X^n$ denote the object of $\mathcal{C}^\otimes_{\langle n \rangle }$ corresponding to the $n$-tuple $(X, \dots , X) \in \mathcal{C}^n$. The $\infty$-endomorphism operad of $X$ is defined as the full $\infty$-suboperad \[
\operatorname{End}_{\mathcal{C}}^\otimes (X) \subseteq \mathcal{C}^\otimes 
.\]
spanned by the objects $X^n$ in each fiber $\mathcal{C}^\otimes_{\langle n \rangle }$.
\end{defn}

\begin{notations}
Let $\operatorname{Mul}_{\mathcal{C}}(\left\{ X \right\}_{1\leq i\leq n},Y)$ denote the union of the components of $\operatorname{Map}_{\mathcal{C}^\otimes }(X^n,X)$ over the unique (active) map $\langle n \rangle \to \langle 1 \rangle $ sending $*$ to $*$ and everything else to $1$.
\end{notations}

Heuristically, the $\infty$-endomorphism operad of $X$ is the one-coloured $\infty$-operad whose multimorphisms are given by those of $\mathcal{C}$: \[
\operatorname{Map}_{\operatorname{End}_{\mathcal{C}}^\otimes (X) }(X^n, X) = \operatorname{Mul}_{\mathcal{C}}(\{X, \dots , X\}, X)
.\]

\begin{defn} 
Let $\Omega^{n-1}Bord_n$ be the symmetric monoidal $\infty$-category of $n$-dimensional bordisms. The $\infty$-endomorphism operad of $S^{n-1}$ is $\operatorname{End}_{\Omega^{n-1}Bord_n}^{\otimes }(S^{n-1}) $. The connected $\infty$-endomorphism operad of $S^{n-1}$ is the sub-operad
\[
\operatorname{End}_{\Omega^{n-1}Bord_n}^{\otimes , conn}(S^{n-1}) \hookrightarrow  \operatorname{End}_{\Omega^{n-1}Bord_n}^{\otimes }(S^{n-1})
\]
consisting of connected bordisms.

Similarly, we define the framed $\infty$-endomorphism operad $\operatorname{End}_{\Omega^{n-1}Bord_n^{fr}}^{\otimes }(S^{n-1}) $, its connected sub-operad $\operatorname{End}_{\Omega^{n-1}Bord_n^{fr}}^{\otimes, conn }(S^{n-1}) $ and the oriented $\infty$-endomorphism operad $\operatorname{End}_{\Omega^{n-1}Bord_n^{SO}}^{\otimes }(S^{n-1}) $, along with its connected sub-operad $\operatorname{End}_{\Omega^{n-1}Bord_n^{SO}}^{\otimes, conn }(S^{n-1}) $.
\end{defn}

















\begin{conj} \label{conj:LisEndfr}
There is a map of $\infty$-operads $f: \mathbb{L}^\otimes \to \operatorname{End}_{\Omega^2 \operatorname{Bord}_3^{fr}}^\otimes (S^2) $, whose image is $\operatorname{End}_{\Omega^2 \operatorname{Bord}_3^{fr}}^{\otimes , conn}(S^2)$. Furthermore, $f$ is an equivalence of $\infty$-operads $\mathbb{L}^\otimes \overset{\sim}{\to} \operatorname{End}_{\Omega^2 \operatorname{Bord}_3^{fr}}^{\otimes , conn}(S^2)$.
\end{conj}

\begin{conj} \label{conj:LisEndSO}
There is a map of $\infty$-operads $f_{SO}: \mathbb{L}_{SO}^\otimes \to \operatorname{End}_{\Omega^2 \operatorname{Bord}_3^{SO}}^\otimes (S^2) $, whose image is $\operatorname{End}_{\Omega^2 \operatorname{Bord}_3^{SO}}^{\otimes , conn}(S^2)$. Furthermore, $f_{SO}$ is an equivalence of $\infty$-operads $\mathbb{L}_{SO}^\otimes \overset{\sim}{\to} \operatorname{End}_{\Omega^2 \operatorname{Bord}_3^{SO}}^{\otimes , conn}(S^2)$.
\end{conj}

\begin{rmk}
The reason behind the proposal is this: by Hatcher's unfinished draft \cite{hatcher2008diffeomorphism}, which was proven by \cite{boyd2026primedecompositionfibresequence}, for every oriented 3 manifold $M$ whose irreducible factors are $P_1 , \dots , P_m$, with possibly finitely many irreducible prime factors $S^2 \times S^1$, then there exists a homotopy fibre sequence \[
C(M) \to \operatorname{BDiff}(M ) \to \operatorname{BDiff}(\coprod_{1\leq i\leq m}P_i ) 
.\]
where $C(M)$ is the space of connect sum configurations, and the second map is roughly the splitting of $M \hookrightarrow \mathbb{R}^\infty$ along splitting spheres, resulting in a collection of irreducible factors with $D^3$ removed and embedded in $\mathbb{R}^\infty$. We then cap the missing balls, which give the boundary-less irreducible factors $\coprod_{i} P_i \hookrightarrow \mathbb{R}^\infty$.

A multimorphism in any of the above $\infty$-endomorphism operads is a bordism from copies of  $S^2$ to a single outgoing $S^2$. Such a bordism is an element $(M, t_0 ,t_1 )$ of \[
\operatorname{BDiff}(M ) \times \mathbb{R}^2 \cong \operatorname{Emb}(M, \mathbb{R}^\infty) / \operatorname{Diff}(M ) \times \mathbb{R}^2
.\]

Hence in order to model the multimorphisms by an operad, we need the operad to essentially have $\operatorname{BDiff}(M ) $ built in, as well as ways to specify its boundaries. The space of connect sum configurations $C(M)$ in the homotopy fibration, over a base point, is our intended carrier of this information. To specify the boundaries, we modified he space of connect sum configurations to include embeddings $B^3 \hookrightarrow S^3, P_i$ corresponding to newly introduced half edges. Hence the operad $\mathbb{L}^\otimes $ and the oriented cousin $\mathbb{L}_{SO}^\otimes $ has exactly enough information to start from a collection of irreducible 3-manifolds $\coprod_i P_i \hookrightarrow \mathbb{R}^\infty$ and form a connect sum through a connect sum configuration $f \in C_{fr}^\partial (M)$ or $C_{SO}^\partial (M)$. The configuration $f$ also specifies where along the bounding 3-balls are, so one could remove their interior.
\end{rmk}





\begin{eg}
Recall that $\mathbb{L}^\otimes $ has an $\infty$-suboperad $\mathbb{L}^{\bigstar, \otimes }$, the ``spike-ball'' $\infty$-operad. Consider a subset of morphism of $\langle 1 \rangle \to \langle 1 \rangle $ given by the following data
\begin{enumerate}
\item the morphism $\alpha : \langle 1 \rangle \to \langle 1 \rangle $ is the identity in $\mathcal{F}in_*$.
\item an element $h \in \operatorname{BDiff}(P )  $ where $P$ is any fixed framed irreducible 3-manifold.
\item A configuration $f \in C^{\partial, 1}_{fr, G}(P)$, where $G$ is the graph with a single unlabelled vertex $v$ connected via the edge $e$ to a single labelled vertex $p$, where there are two additional unpaired half edges $\left\{ \epsilon_1 , \epsilon_2  \right\} $ at the unlabelled vertex $v$: figure \ref{fig:simplespikeball}

\begin{figure}[ht]
    \centering
    \incfig{simplespikeball}
    \caption[A simple spike ball example]{A simple spike ball example. (a) gives the graph $G$. (b) provides a visualization for the bordism represented by $G$ and a connect sum configuration $f$.}
    \label{fig:simplespikeball}
\end{figure}
\end{enumerate}

The configuration $f$ is equal to the following data \[
(r_e, l_e, D^3_e \hookrightarrow S^3_v, D^3_e \hookrightarrow P, D^3_{\epsilon_1 }\hookrightarrow S^3_v, D^3_{\epsilon_2 } \hookrightarrow S^3_v)
.\]
where all the embeddings in $S^3_v$ are rectilinear and have disjoint images. We may delete the interior of the image of one of the half-edges, say $D^3_{\epsilon_2 }$, so what remains of $S^3_v$ is diffeomorphic to a ball $D^3$. Then the configuration $f$ contains the following data \[
(r_e, l_e, D^3_e \hookrightarrow D^3, D^3_e \hookrightarrow P, D^3_{\epsilon_1 }\hookrightarrow D^3 )
.\]

Note that there exists a map \[
\operatorname{Conf}_2(D^3) \times \operatorname{BDiff}(P) \to \mathbb{L}^{\bigstar, \otimes }
.\]
Sending a configuration of $2$ points in $D^3$ to the centre of the embeddings $D^3_e, D^3_{\epsilon_1 } \hookrightarrow D^3$ and an element $h \in \operatorname{BDiff}(P ) $ to the chosen element as part of the data of $\langle 1 \rangle \to \langle 1 \rangle $. Taking the inclusion into the operad $\mathbb{L}^{\otimes }$, passing through the endomorphism operad, and finally through a TFT $Z$, we get a map \[
\operatorname{Conf}_2(D^3) \times \operatorname{BDiff}(P) \to \mathbb{L}^{\bigstar, \otimes } \hookrightarrow \mathbb{L}^\otimes \to \operatorname{End}_{\Omega \operatorname{Bord}_3^{fr}}^\otimes (S^2) \to \operatorname{End}_{\mathcal{C}}^\otimes (Z(S^2))
.\]
whose image is over the $1$-ary operations. Therefore there is a map \[
\operatorname{Conf}_2(D^3) \times \operatorname{BDiff}(P) \to \operatorname{Map}_{\mathcal{C}}(Z(S^2), Z(S^2))
.\]
for any TFT $Z: \Omega^2\operatorname{Bord}_3^{fr} \to \mathcal{C}$ and for any framed irreducible 3-manifold $P$.
\end{eg}
