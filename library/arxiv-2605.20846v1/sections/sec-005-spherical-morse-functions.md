---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-005-spherical-morse-functions
section_title: "Spherical Morse Functions"
section_number: null
pages: 32-38
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.972
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:Cob2Cob3Iso}
Before we proceed to show that the commutative Frobenius relations are sufficient among CF generators, it is necessary to examine their Morse theory. We will prove in this section that there is an isomorphism between the categories $\operatorname{Cob}( 3)_{S^2,CF} $ and $\operatorname{Cob}( 2)$ in theorem \ref{thm:Cob2Cob3CFIso}. Furthermore we show that $G_1 $ and $G_2 $ are both minimal in proposition \ref{prop:G1G2minimal}.

\begin{prop} \label{prop:sphericalnoirreducible}
Let $M$ be a closed oriented 3-manifold, and $f:M\to \mathbb{R}$ a Morse function such that for every regular value $r\in \mathbb{R}$, $f^{-1}(r) \cong \sqcup S^2$. Namely, $f$ is a spherical Morse function-- a Morse function whose regular surfaces are disjoint unions of $S^2$. Then 
\begin{enumerate}
\item $\pi_1(M)$ is free, and
\item $M$ is diffeomorphic to either $S^3$ or $\#^r \left( S^2\times S^1 \right) $ with $r\geq 1$ the rank of $\pi_1(M)$.
\end{enumerate}
\end{prop}

\begin{proof}
Let $R_f$ be the Reeb graph of $f:M\to \mathbb{R}$. Recall that for a Morse function $f$ on a compact manifold $M$, the Reeb graph $R_f$ is a finite graph such that
\begin{itemize}
\item the vertices of $R_f$ are the critical level components
\item the edges of $R_f$ are copies of intervals of regular values 
\end{itemize}

Let $q: M \to M/\sim=R_f$ be the quotient map. Then the Morse function factors through $q$:

\[\begin{tikzcd}
M & {M/\sim=R_f} & {\mathbb{R}}
\arrow["q", from=1-1, to=1-2]
\arrow["f"', curve={height=20pt}, from=1-1, to=1-3]
\arrow["{\exists \tilde{f}}", dashed, from=1-2, to=1-3]
\end{tikzcd}\]

Between consecutive critical values $a<b$, standard Morse theory shows that $f^{-1}((a,b)) \cong f^{-1}(t) \times (a,b)$ for any regular value $t\in (a,b)$.  Since our regular surfaces are disjoint unions of  $S^2$, we have by definition \[
q^{-1}(e) \cong  S^2 \times (a,b) 
.\]
for any edge $e$ which corresponds to the regular interval $(a,b)$. See figure \ref{fig:egreeb} for an example.

\begin{figure}[ht]
    \centering
    \incfig{egreeb}
    \caption[A Reeb graph example]{An example of a Reeb graph $R_f$ associated to a Morse function $f$. Here $f:S^2 \times S^1 \to \mathbb{R}$ is the Morse function described in \ref{rmk:S2xS1redundant}, which is the projection onto the $S^1$ factor and then taking the height function.}
    \label{fig:egreeb}
\end{figure}




At a vertex $v$, the local Morse model in 3 dimensions shows the preimage of a small neighbourhood of $v$ is obtained from a union of $3$-balls by attaching a single $k$-handle, for $k\in \left\{ 0, \dots ,3 \right\} $. Since the regular level sets just above $v$ and just below are union of spheres, the only allowed local changes are: 
\begin{itemize}
\item Birth/death of a spherical component (when $v$ corresponds to an index $0$ or $3$ critical point)
\item Merge/split of spherical component(s) that never creates a torus (when $v$ corresponds to an index $1$ or $2$ critical point).
\end{itemize}

In particular, the preimage of a small vertex neighbourhood is simply connected. Indeed, a union of $3$-balls with $1/2$-handle attached along does not create $\pi _1$. The preimage of an open edge is $S^2\times (a,b)$, which is also simply connected.

\textbf{Claim} $\pi_1 (M)$ is a free group.

Cover $M$ by preimages $\left\{ U_v \right\} $ of vertex neighbourhoods and $\left\{ U_e \right\} $ of open edge neighbourhoods in $R_f$. Then each $U_v, U_e$ is simply connected.

By Seifert-van Kampen, $\pi_1 (M) = \pi_1(\text{the nerve of this cover})$. But the nerve of this cover is canonically $R_f$. So \[
\pi_1(M) \cong \pi_1 (R_f) \cong <e-v+1 \text{ many generators}>
.\]
Most importantly, we learn that $\pi_1 (M)$ is a free group.

By prime decomposition, any closed oriented $3$-manifold $M$ splits uniquely as a connected sum of prime summands, and $\pi_1 (M)=$ free product of $\pi_1 (\text{prime summands})$. In particular, if $\pi_1 (M)$ is free of rank $r$, then \[
M \cong \# ^r (S^2\times S^1) \# N
.\]
where $N$ is simply connected. By the Poincare conjecture, $N \cong S^3$.
\end{proof}

\begin{cor}
Let $M$ be a closed oriented prime $3$-manifold, and $f:M \to \mathbb{R}$ a spherical Morse function. Then $M$ is diffeomorphic to either $S^3$ or $S^2 \times S^1$.
\end{cor}









\begin{rmk}
The spirit of the proposition and the corollary is: no matter how hard one tries, one cannot glue CF generators into a prime 3-manifold, except for $S^3$ and $S^2\times S^1$.
\end{rmk}

\begin{cor} \label{cor:hominCF}
Every connected bordism $[M]$ in $\operatorname{Cob}(3)_{S^2, CF}$ has a representative $M$ which is diffeomorphic to either $S^3$ with the interior of a finite number of disjoint $D^3$ removed, or to $\#^r S^2 \times S^1$ with the interior of a finite number of disjoint $D^3$ removed.
\end{cor}

\begin{proof}
First cap off the incoming and outgoing boundaries of $M$, resulting in a closed oriented 3-manifold $\widehat{M}$. By definition, $CF$ generates morphisms in $\operatorname{Cob}(3)_{S^2, CF}$, so the standard spherical Morse functions on the $CF$ generators induces a spherical Morse function on $\widehat{M}$, $f : \widehat{M} \to \mathbb{R}$. Then by proposition \ref{prop:sphericalnoirreducible}, $\widehat{M} \cong S^3$ or $\widehat{M} \cong \#^r \left( S^2 \times S^1 \right) $. Hence $M \cong S^3 \setminus \left( \operatorname{int}(\sqcup D^3) \right) $ or $M \cong \#^r \left( S^2 \times S^1 \right)  \setminus \left( \operatorname{int}(\sqcup D^3) \right) $.
\end{proof}

\begin{defn} \label{defn:Sillyfunctor}
Define the \textit{silly functor} $S$ as the  map \[
S: \operatorname{Cob}( 2) \to \operatorname{Cob}( 3)_{S^2, CF}
.\]
sending
\begin{enumerate}
\item A disjoint union $\sqcup^n S^1$ to a disjoint union $\sqcup^n S^2.$
\item The unit morphism $1: \emptyset \to S^1$ to $1: \emptyset \to S^2$.
\item The trace morphism $tr: S^1 \to \emptyset $ to $tr: S^2 \to \emptyset$.
\item The multiplication $m: S^1 \sqcup S^1 \to S^1$ to $m: S^2 \sqcup S^2 \to S^2$.
\item The comultiplication $m^\vee: S^1\to S^1 \sqcup S^1$ to $m^\vee: S^2 \to S^2 \sqcup S^2$.
\item The genus $g$ bordism $[\Sigma_g \setminus int( \sqcup^{n_{inc}+n_{out}}D^2)]: \sqcup^{n_{inc}}S^1 \to \sqcup^{n_{out}}S^1$ to the bordism $ [\#^g(S^2 \times S^1) \setminus int( \sqcup^{n_{inc}+n_{out}}D^3)]: \sqcup^{n_{inc}}S^2 \to \sqcup^{n_{out}}S^2$.
\end{enumerate}
Theorem \ref{thm:Cob2Cob3CFIso} shows that the silly functor is an isomorphism.
\end{defn}

\begin{thm} \label{thm:Cob2Cob3CFIso}
$S: \operatorname{Cob}(2) \to \operatorname{Cob}(3)_{S^2,CF} $ is an isomorphism.
\end{thm}

\begin{proof}






By \cite{steinebrunner2026surfacecategorytropicalcurves}, $\pi_0: \operatorname{Cob}(2) \to Csp(\mathbb{Z}_{\geq 0},1)$ is an equivalence of symmetric monoidal labelled cospan categories. Slightly abusing the notations, our strategy is to construct another equivalence $\pi_0: \operatorname{Cob}(3)_{S^2, CF} \to Csp(M,[S^2 \times S^1])  $ of symmetric monoidal labelled cospan categories, where $Csp(\mathcal{M}, [S^2 \times S^1])$ is canonically isomorphic to $Csp(\mathbb{Z}_{\geq 0},1)$. Let its inverse be $F: Csp(\mathcal{M}, [S^2 \times S^1]) \to \operatorname{Cob}(3)_{S^2, CF}$. Then we show that the composite \[
\operatorname{Cob}(2) \overset{\pi_0}{\to } Csp(\mathbb{Z}_{\geq 0},1) \overset{\sim}{\to} Csp(\mathcal{M}, [S^2 \times S^1]) \overset{F}{\to } \operatorname{Cob}(3)_{S^2, CF}
.\]
is the desired functor $S: \operatorname{Cob}(2) \to \operatorname{Cob}(3)_{S^2, CF}$.

First, recall the definition of the cospan category of finite sets $Csp$. The category $Csp$ has objects finite sets and morphisms $A \to B$ is an isomorphism class of cospans $[A \to X \leftarrow B]$, where two cospans are isomorphic if there is a bijection $X \cong X'$ that is compatible with the maps from $A$ and from $B$. Disjoint union equips $Csp$ with a symmetric monoidal structure, with the empty set as the monoidal identity. If $(A, +)$ is an abelian monoid and $\alpha  \in A$, then we can define the category $Csp(A,\alpha )$ with finite sets as objects, and an arrow $A\to B$ is an equivalent class of cospans and labels

\[\begin{tikzcd}
	& A & \\
	& X \\
	A && B
	\arrow["l"', from=2-2, to=1-2]
	\arrow[from=3-1, to=2-2]
	\arrow[from=3-3, to=2-2]
\end{tikzcd}\]
The composition law of $Csp(A,\alpha )$ is rigged for the equivalence $ \pi_0:\operatorname{Cob}( 2)\to Csp(\mathbb{Z}_{\geq 0},1) $ to hold. The element $1=\alpha $ is the element that controls how much genus it increases when closing a loop via a composition. For details we refer the reader to \cite{steinebrunner2026surfacecategorytropicalcurves}.

Let $\left( \mathcal{M} = \left\{ [\#^r S^2 \times S^1] \mid r=0,1,\dots  \right\} , \# \right) $ be the abelian monoid under connect sum, whose elements are diffeomorphism classes of connect sums $[\#^r S^2 \times S^1]$. Note that $\mathcal{M}$ is canonically isomorphic to the abelian monoid $(\mathbb{Z}_{\geq 0}, +)$. Therefore there is canonical isomorphism \[
Csp(\mathbb{Z}_{\geq 0},1) \overset{\sim}{\to} Csp(\mathcal{M}, [S^2 \times S^1]) 
.\]
sending a label $l: S \to \mathbb{Z}_{\geq 0}$ to the label $l': S \to \mathbb{Z}_{\geq 0} \overset{\sim}{\to} \mathcal{M}$.

The functor $\pi_0: \operatorname{Cob}(3)_{S^2, CF} \to Csp(\mathcal{M},[S^2 \times S^1])  $ is defined as follows:
\begin{enumerate}
\item An object $\coprod_n S^2$ of $\operatorname{Cob}(3)_{S^2, CF} $ is mapped to $\pi_0 (\coprod_n S^2)$, the set of $n$ elements.
\item A bordism $W: M \to N$ is mapped to the cospan

\[\begin{tikzcd}
& {\pi_0(W)} & \\
{\pi_0(M)} && {\pi_0(N)}
\arrow[from=2-1, to=1-2]
\arrow[from=2-3, to=1-2]
\end{tikzcd}\]
and the label $l: \pi_0 (W) \to \mathcal{M}$ sends a connected component $W' : M' \to N'$ to the diffeomorphism class of the closed manifold \[
\widehat{W'} \cong \left( \sqcup_{|\pi_0 (M')|} D^3 \right) \cup W' \cup \left( \sqcup_{|\pi_0 (N')|} D^3 \right) 
.\]
where the unions are taken at the gluing boundaries. Note that $\widehat{W}$ is indeed diffeomorphic to a connect sum of $S^2 \times S^1$ by corollary \ref{cor:hominCF}.

\item Composition is well defined because the definition of $Csp(M, [S^2 \times S^1])$ is rigged specifically to do so.
\end{enumerate}

$\pi_0 $ is obviously compatible with the symmetric monoidal structure on both sides, so it's a symmetric monoidal functor. We want to show that this is an equivalence. Recall that a functor $F: \mathcal{C} \to \mathcal{D}$ of labelled cospan categories is an equivalence of categories if and only if it satisfies 

\begin{enumerate}
\item For any connected object $M_D \in \mathcal{D}$, there exists a connected object $M_C \in \mathcal{C}$ such that $F(M_C) \cong M_D$.
\item for all $M,N \in \mathcal{C}$, $F$ induces a bijection \[
\operatorname{Hom}_{\mathcal{C}}^{conn}(M,N) \cong \operatorname{Hom}_{\mathcal{D}}^{conn}(F(M),F(N)) 
.\]
\end{enumerate}

For the functor $\pi_0 : \operatorname{Cob}(3)_{S^2, CF} \to Csp(\mathcal{M}, [S^2\times S^1])$ we have defined bove, condition 1 is trivial. Hence we need to check that $\pi_0 $ induces a bijection \[
\operatorname{Hom}_{\operatorname{Cob}(3)_{S^2, CF}}^{conn}( \sqcup^{n_{inc}} S^2, \sqcup^{n_{out}} S^2) \cong \operatorname{Hom}_{Csp(\mathcal{M}, [S^2\times S^1])}^{conn}(\pi_0(\sqcup^{n_{inc}} S^2), \pi_0(\sqcup^{n_{out}} S^2))  
.\]
The left hand side is the set of diffeomorphism class of connected bordisms $[W]$ with spherical boundaries. The right hand side are all connected cospans $\pi_0(\sqcup^{n_{inc}} S^2) \to X \leftarrow \pi_0(\sqcup^{n_{out}} S^2)$ with label $l: X \to \mathcal{M}$. By definition, a cospan  $A \to X \leftarrow B$ of finite sets is connected if $X$ is a set with one elements. Hence a connected morphism belonging to the right hand side is an element $l(*) \in \mathcal{M}$. Therefore the right hand side is simply isomorphic to $\mathcal{M}$.

Under this identification, $\pi_0$ induces the map \[
\operatorname{Hom}_{\operatorname{Cob}(3)_{S^2, CF}}^{conn}( \sqcup^{n_{inc}} S^2, \sqcup^{n_{out}} S^2) \to  \left\{ [\#^r \left( S^2 \times S^1 \right) ] \mid r=0, 1, \dots  \right\} 
.\]
sending $[W]$ to $[\widehat{W}]$.

We will construct an inverse. Let $V \cong \#^r \left( S^2 \times S^1 \right) $. Choose an orientation-preserving embedding \[
\iota: \left( \sqcup^{n_{inc}} D^3 \right) \sqcup \left( \sqcup^{n_{out}} D^3  \right)  \hookrightarrow V
.\]
Then $V \cong \widehat{W_{\iota}}$, where $W_\iota = V \setminus im(\iota)^\circ$. For any other such embedding $\iota'$, there exists a diffeomorphism $\psi: V \to V$ with $\iota ' = \psi \circ \iota$, and such that $\psi|_{W_\iota} : W_\iota \to W_{\iota'}$ is a boundary and orientation preserving diffeomorphism.\cite[Ch8 Thm 3.2]{hirsch_differential_1976}. Therefore the map \[
[V] \mapsto [W_{\iota}]
.\]
is independent on the choice of $\iota$. It is clearly the inverse to the assignment $[W] \mapsto [\widehat{W}]$.

Hence we have shown that the map \[
\operatorname{Hom}_{\operatorname{Cob}(3)_{S^2, CF}}^{conn}( \sqcup^{n_{inc}} S^2, \sqcup^{n_{out}} S^2) \to  \left\{ [\#^r \left( S^2 \times S^1 \right) ] \mid r=0, 1, \dots  \right\} 
.\]
is a bijection. Therefore \[
\operatorname{Hom}_{\operatorname{Cob}(3)_{S^2, CF}}^{conn}( \sqcup^{n_{inc}} S^2, \sqcup^{n_{out}} S^2) \cong \operatorname{Hom}_{Csp(\mathcal{M}, [S^2\times S^1])}^{conn}(\pi_0(\sqcup^{n_{inc}} S^2), \pi_0(\sqcup^{n_{out}} S^2))  
.\]
is also a bijection, and $\pi_0 : \operatorname{Cob}(3)_{S^2, CF} \to Csp(\mathcal{M}, [S^2\times S^1])$ is an equivalence of labelled cospan categories, in particular an equivalence of categories.

We can construct a functor $F: Csp(\mathcal{M}, [S^2 \times S^1]) \to \operatorname{Cob}(3)_{S^2, CF}$ as the (quasi-)inverse to $\pi_0 $ in the following way:
\begin{enumerate}
\item $F$ sends an order $n$ finite set to $\sqcup^n S^2$. In particular, $F$ sends the empty set to the empty manifold.
\item For a labelled cospan $f: A \to X \leftarrow B :g $ with label $l: X \to \mathcal{M}$,  its image under $F$ is the bordism $W: \sqcup^{|A|}S^2 \to \sqcup^{|B|} S^2$ with $|X|$-many connected component, such that over the element $x\in X$, the corresponding component denoted $W_x$ is diffeomorphic to \[
	W_x \cong l(x) \setminus \Big( \underset{b\in g^{-1}(x)}{\coprod_{a \in f^{-1}(x)}} D^3 \Big) 
.\]
\end{enumerate}

Combining all the relevant functors together, we see that the composition \[
S: \operatorname{Cob}(2) \overset{\pi_0}{\to } Csp(\mathbb{Z}_{\geq 0},1) \overset{\sim}{\to} Csp(\mathcal{M}, [S^2 \times S^1]) \overset{F}{\to } \operatorname{Cob}(3)_{S^2, CF}
.\]
sends
\begin{enumerate}
\item A disjoint union $\sqcup^n S^1$ to a disjoint union $\sqcup^n S^2.$
\item The unit morphism $1: \emptyset \to S^1$ to $1: \emptyset \to S^2$.
\item The trace morphism $tr: S^1 \to \emptyset $ to $tr: S^2 \to \emptyset$.
\item The multiplication $m: S^1 \sqcup S^1 \to S^1$ to $m: S^2 \sqcup S^2 \to S^2$.
\item The comultiplication $m^\vee: S^1\to S^1 \sqcup S^1$ to $m^\vee: S^2 \to S^2 \sqcup S^2$.
\item The genus $g$ bordism $[\Sigma_g \setminus int( \sqcup^{n_{inc}+n_{out}}D^2)]: \sqcup^{n_{inc}}S^1 \to \sqcup^{n_{out}}S^1$ to the bordism $ [\#^g(S^2 \times S^1) \setminus int( \sqcup^{n_{inc}+n_{out}}D^3)]: \sqcup^{n_{inc}}S^2 \to \sqcup^{n_{out}}S^2$.
\end{enumerate}

\end{proof}





\begin{proof}
	(Alternative) An alternative and easier proof is the following: Let $S: \operatorname{Cob}(2)\to \operatorname{Cob}(3)_{S^2, CF}$ be given by 
\begin{enumerate}
\item $S$ sends  $\amalg^n S^1$ to  $\amalg^n S^2$.
\item $S$ sends the unique genus $g$ bordism $\amalg^{n_{inc}}S^1 \to \amalg^{n_{out}} S^1 $ to the unique bordism $[W]: \amalg^{n_{inc}}S^2 \to \amalg^{n_{out}}S^2$ where $\widehat{W} \cong \#^g (S^2 \times S^1)$. 
\end{enumerate}
Then $S(1)=1$, $S(tr)=tr$, $S(m)=m$, and $S(m^\vee) = m^\vee$. By the classification of morphisms in $\operatorname{Cob}( 3)_{S^2,CF} $ in corollary \ref{cor:hominCF}, $S$ induces a bijection \[
\operatorname{Hom}_{\operatorname{Cob}(2)}\Big(\coprod^{n_{inc}}S^1, \coprod^{n_{out}}S^1\Big) \to \operatorname{Hom}_{\operatorname{Cob}(3)_{S^2, CF}}\Big(\coprod^{n_{inc}}S^2, \coprod^{n_{out}}S^2\Big) 
.\]
sending the unique genus $g$ bordism to the unique bordism with $g$-many $S^2 \times S^1$ factors.
\end{proof}




\begin{prop} \label{prop:G1G2minimal}
Both $G_1 $ and $G_2 $ are minimal.
\end{prop}

\begin{proof}
Let $P$ be an oriented irreducible 3-manifold. Consider $[P] = tr \circ [P\setminus \operatorname{int}(D^3)] = tr \circ [P\setminus \operatorname{int}(D^3 \sqcup D^3)] \circ 1$. By proposition \ref{cor:hominCF}, if $[P \setminus \operatorname{int}(D^3)]$ or $[P\setminus \operatorname{int}(D^3 \sqcup D^3) ]$ were generated by commutative Frobenius generators, then $P$ is either $S^3$ or $S^2\times S^1$, which contradicts the premise. Uniqueness of prime decomposition shows that a fixed prime unit cannot be generated by other prime units, hence all prime units are necessary. Theorem \ref{thm:Cob2Cob3CFIso} shows that the commutative Frobenius generators are necessary. Hence $G_1 $ is minimal. The same argument shows that $G_2 $ is also minimal.
\end{proof}
