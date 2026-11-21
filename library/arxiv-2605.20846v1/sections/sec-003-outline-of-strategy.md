---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-003-outline-of-strategy
section_title: "Outline of Strategy"
section_number: null
pages: 22-26
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.997
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec:outlineofstrat}
\begin{defn} \label{defn:3d Morse Datum}
Let $M$ be a compact oriented connected 3 manifold with boundary $X_-$ and $X_+$ of codimension $1$. A \textit{prime Morse datum} is a pair $f:M\to \mathbb{R}$ and an ordered tuple $b=(b_0<b_1<\dots <b_m) \in \mathbb{R}^{m+1}$ such that 
\begin{enumerate}
\item $X_- = f^{-1}(b_0)$ and $X_+ = f^{-1}(b_m)$ are the sets of minimum resp maximum of $f$.

\item $b_i$ are regular values of $f$ such that any connected component $C \subset f^{-1}(b_{i-1}, b_i)$ is diffeomorphic to $D^3$, $S^2 \times I$, $S^3 \setminus \operatorname{int}(\sqcup^3 D^3)$, or $p\setminus \operatorname{int}(D^3 \sqcup D^3)$ where $p$ is an oriented irreducible 3-manifold.
\end{enumerate}
$C$ is called an \textit{elementary bordism} if $C$ is diffeomorphic to $D^3$ or $S^3 \setminus \operatorname{int}(\sqcup^3 D^3)$. $C$ is called a \textit{prime bordism} if $C$ is diffeomorphic to $p\setminus \operatorname{int}(D^3 \sqcup D^3)$ for $p\not \cong S^2\times S^1$ oriented irreducible. $C$ is \textit{cylindrical} if $C$ is diffeomorphic to $S^2\times I$. Note elementary bordisms admit Morse datum with only one critical point (the standard Morse function), while a cylindrical one admits datum with no critical point. Any Morse datum on a prime bordism must necessarily have more than one critical point.

We frequently suppress $b$ when discussing the prime Morse datum $f,b$ if it is clear from context which prime decomposition it induces.
\end{defn}

\begin{defn} \label{defn:Prime decomposition}
The \textit{prime decomposition} of a bordism $M$ compact oriented connected 3 manifold with boundary $X_-, X_+$ is a decomposition  \[
M = M_1 \cup_{X_1} M_2 \cup_{X_2} \dots \cup_{X_{m-1}} M_m
.\]
such that $M_i$ is diffeomorphic to a disjoint union of $D^3$, $S^2 \times I$, $S^3 \setminus \operatorname{int}(\sqcup^3 D^3)$, or $p\setminus \operatorname{int}(D^3 \sqcup D^3)$ for $p\not \cong S^2 \times S^1$ oriented irreducible. Additionally we require that $M_1 \cap \partial M = X_+$ and $M_m \cap \partial M = X_-$. 
\end{defn}

\begin{defn} \label{defn:Prime composition}
(Prime composition) of a morphism $[M]$ in $\operatorname{Cob}(3)_{S^2} $ is a collection of morphisms $[M_1], [M_2], \dots , [M_m]$ such that 
\begin{enumerate}
\item each$[M_i]$ is a tensor product of $1$, $tr$, $id$, $m$, $m^\vee$, and $[p\setminus \operatorname{int}(D^3 \sqcup D^3)]$ for $p$ oriented irreducible $3$-manifold.
\item the collection composes to $[M] = [M_1]\circ [M_2] \dots \circ [M_m]$. 
\end{enumerate}
\end{defn}

\begin{claim}
\begin{enumerate}
\item Any prime Morse datum $f, b$ on $M$ induces a prime decomposition of $M$. each factor is $M_{m-i+1}= f^{-1}(b_{i-1},b_i)$.
\item Any prime decomposition of a bordism $M$ induces a prime composition of $[M]$ such that $M_i \in [M_i]$.
\item Any prime decomposition of $M$ comes from some prime Morse datum -- once fixed some ``standard'' Morse functions for each $M_i$, and glue them together into a Morse function on $M$.
\item Any prime composition of a morphism comes from a prime decomposition of a representative.
\end{enumerate}
\end{claim}













\textbf{General strategies on showing a certain relation is true} 
Suppose we have two composition sequences, say one sequence composes to $\left[ M \right] $ and the other to $\left[ M' \right] $, and we want to show that they are equal. There are two strategies: one at the level of prime decompositions, one at the level of Morse data. 

At the level of prime decompositions, one can show that two chosen representatives $M, M'$ of $[M]$ and $[M']$ have prime decompositions inducing the corresponding compositions, and that $M$ and $M'$ are diffeomorphic. This is convenient when it is easy to argue that $M\cong M'$. One can alternatively show that that the same manifold has two prime decompositions, but it is harder-- this amounts to explicitly identifying the gluing surfaces on a fixed manifold $M$.

At the level of Morse data, one can start with two Morse functions (or rather, prime Morse data) $f_0 ,f_1 :M\to \mathbb{R}$ on the same manifold, and show that $f_0, f_1$ indeed induce the appropriate Morse decompositions. This process necessarily factors through the alternative method at the level of prime decomposition, but is strictly easier, as it gives explicitly the gluing surfaces which are regular surfaces of the Morse data. Note that if we want a non-trivial relation, $f_0, f_1$ must induce non-isomorphic /diffeomorphic prime decompositions, thus inducing different prime compositions. 

\textbf{The classification of relations take the opposite approach.} To classify all possible relations between generating bordisms is to show that for any two prime compositions of the same bordism class $\left[ M \right] $, one can always turn one composition into the other using a set of known relations. This means that there exists a sequence of prime compositions $(C_i) $ such that $C_{i-1}$ and $C_i$ are the same everywhere except for one instance of a known relation. Since the two compositions result in the same bordism class, we may choose the same representative $M$. Hence at the level of prime decompositions, one needs to show that there exists a sequence $(D_i)$ of prime decompositions of $M$ inducing the composition sequence $(C_i)$ such that $D_i$, $D_{i-1}$ are the same except for one application of a known decomposition diffeomorphism. At the level of Morse data, we need a sequence of Morse datum $(f_i, b_i)$ which induce the prime decompositions $(D_i)$

Let's review what this means in $\operatorname{Cob}(2) $. Let $M$ be a compact oriented bordism and $f_0 ,f_1:M \to \mathbb{R}$ prime data which induce compositions $C_0, C_1$. To show that commutative Frobenius relations are sufficient, one must show that there exists a sequence $(f_0, \dots , f_i, \dots , f_1)$ such that $f_{i-1}$ and  $f_i$ induces decompositions that are identical except related by a diffeomorphism of a certain kind, which in turn induces compositions that are identical except related by a commutative Frobenius relation. By noticing that Cerf theory provides a path from $f_0 $ to $f_1 $ which is excellent Morse for all but finitely many singularities, and that the types of singularities can be shown to induce commutative Frobenius relations, one chooses a path and let the sequence of Morse functions be chosen, one for each excellent Morse segment, along which with suitable choices of $b_i$ the decomposition is unique up to diffeomorphism. One summarizes by saying ``the singularities along the Cerf path exhibit the relations necessary to equate composition $C_0 $ to $C_1 $.''

The situation in $\operatorname{Cob}(3)_{S^2} $ is markedly different due to the additional prime morphisms, especially at the level of Morse data. First, external prime relations, such as legs and waist relations, are induced by Morse functions connected by a Cerf path with multiple singularities. Second, there is no longer a bijection between non-trivial singularities and commutative Frobenius relations. For example, the 0-1 birth death does not induce any relations among commutative Frobenius generators.

To show that commutative Frobenius relations between the $C=\left\{ 1, m \right\} $ and $F= \left\{ tr, m^\vee \right\} $ generators are true, we use the local form of a birth-death singularity to deduce the straight forward decompositions, hence compositions; we analyse the topological constraints on the exchanges of critical values and deduce the corresponding decompositions, which induce the compositions. To show that these relations are sufficient among CF generators, we prove in proposition \ref{prop:keyprop} and proposition \ref{prop:keypropCF} that any two Morse data inducing CF-generated compositions are connected by a path whose singularities split the path into segments, each of which is related to its neighbours by inducing a specific relation among the decompositions. To do so, we invoke the equivalence between the types of singularities and the induced decomposition relations, and show that only specific types of singularities are present on this path. This culminates in corollary \ref{cor:CFonlycommFrob}, which states that there are no more relations between CF generators. 

Then we have to deal with the prime bordisms, which have no counterparts in $\operatorname{Cob}( 2)$. There are some obvious composition relations coming from prime decompositions, which can be induced by Morse data closely related to each other. One such example is \textit{prime commutativity} introduced in \ref{primecommutativity}, which says $p^{\times \times}_1 \circ p^{\times \times}_2 = p^{\times \times}_2 \circ p^{\times \times}_1  $. If $(f,b=0)$ is a prime Morse datum inducing a prime decomposition inducing the composition on the left hand side, then ``flipping the picture upside down,'' post-composing with the map $\mathbb{R}\to \mathbb{R}$ sending $x \mapsto -x$ and keeping $b=0$ fixed will induce the composition on the right hand side. See figure \ref{fig:primecommutativity}.

Even though this relation has very simple geometric interpretations, the singularity types of a path between their Morse functions may be very complicated. Therefore we conclude that prime relations such as prime commutativity are \textit{not} classified by singularity types-- rather, they are collections of singularities along Cerf paths. This makes the classification at the Cerf-theoretic level challenging, but we are able to circumvent it through geometric arguments.

After a brief digression regarding (the lack of) \textit{internal relations}, we prove that \textit{legs and waist relations} \ref{prop:legsandwaistrelations} exist by proving that the prime decompositions, which induces the compositions under consideration, are decompositions of diffeomorphic manifolds. At the level of Morse data, the legs relations are trivial, but the story for the waist relations is similar to that of prime commutativity-- paths between the pairs of Morse functions, which induce the waist relations, will have multiple singularities where the function fails to be excellent Morse. Therefore two Morse data inducing a waist relation is connected by a path with more than one singularity.

The proof that commutative Frobenius relations, prime relations, and legs and waist relations together are sufficient can also be viewed at both the level of prime decompositions and at the level of Morse data. At the level of prime decompositions, one first show that there are ``standard'' form prime decompositions which allows one to isolate the prime morphisms Then we show that the parts generated by CF generators can be brought from one decomposition to the other using proposition \ref{prop:keypropCF}. We may hold the Morse functions over the prime part constant, and glue with the corresponding path to get the total path.





We first outline the strategy for this section. Since both $G_1 $ and $G_2 $ share $C$ and $F$ generators, we first prove that these generators satisfy the usual commutative Frobenius relations like their counterparts in $\operatorname{Cob}(2) $, and most importantly that these relations are necessary and sufficient among morphisms generated by $C$ and $F$. 

More precisely, this means that the graph with $\left\{ \sqcup^n S^2 \right\}\cong \mathbb{Z}_{\geq 0}$ vertices and $C\cup F$ (and tensor products) as directed edges, together with commutative Frobenius relations form a presentation \ref{defn:Generators and Relations} of a subcategory of $\operatorname{Cob}(3)_{S^2}$. This category is denoted $\operatorname{Cob}(3)_{S^2, CF}$ and defined as

\begin{defn} \label{defn:Cob(3)_S^2,CF}
($\operatorname{Cob}(3)_{S^2,CF} $) Let $C=\left\{ m,1 \right\} , F=\left\{ m^\vee, tr \right\} $ be defined as in \ref{notations:CF}. Consider the subcategory of $\operatorname{Cob}(3)_{S^2}$ whose morphisms are those which admit a composition in terms of $C\cup F$ generators and their tensor products. Call this category $\operatorname{Cob}(3)_{S^2,CF} $.
\end{defn}

Next, we show that $P$ generators in $G_2 $ satisfy \textit{prime commutativity} in . The more interesting question is whether the commutative Frobenius generators interact with the new prime generators in some non-trivial way. We first address that there are no ``internal'' commutative Frobenius relations inside a prime generator, and then we show that there are only a handful of ``external'' relations each for $P$ and just one for $L$. These external relations are called ``co/legs and co/waist relations'' for $P$ and ``legs relations'' for $L$. Theorem \ref{mainthmG2} shows that $G_2 $, with commutative Frobenius relations, prime commutativity, co/legs and co/waist relations, form a presentation of $\operatorname{Cob}(3)_{S^2}$. In particular, these relations are sufficient. On the other hand, theorem \ref{mainthmG1} shows that $G_1 $, with commutative Frobenius relations alone, form a presentation of $\operatorname{Cob}(3)_{S^2} $. 

The fact that commutative Frobenius relations alone are sufficient for the $G_1 $ presentation raises the question of whether the same could happen to $G_2 $. This turns out to be mostly the case, except for the co/legs relations. We present a series of propositions which shows that prime commutativity and co/waist relations are implied by the co/legs relations and commutative Frobenius relations, culminating in theorem \ref{thm:trueG2thm}, which shows that $G_2 $, with commutative Frobenius relations and legs relations, form a presentation of $\operatorname{Cob}(3)_{S^2}$. In particular, these relations are necessary.

From a higher perspective, what we aim to achieve in this section is to develop the Cerf theory of 3 manifolds equipped with a notion of ``good'' Morse function, but instead of achieving this goal through the more common Jet-stratification analysis/algebraic approach, we exploit the isomorphism \ref{thm:Cob2Cob3CFIso} between $\operatorname{Cob}(2) $ and $\operatorname{Cob}(3)_{S^2} $ and prove purely geometrically that the relations outlined in the previous paragraphs \textit{are} the Cerf theory we promised.
