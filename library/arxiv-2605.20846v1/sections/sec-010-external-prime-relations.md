---
doc_id: arxiv-2605.20846v1
doc_title: "Topological Field Theories and the Algebraic Structures of the Two-Sphere"
section_id: sec-010-external-prime-relations
section_title: "External Prime Relations"
section_number: null
pages: 49-54
source_pdf: 2605.20846v1.pdf
source_sha256: db27cb6d01c4f2fb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.994
doc_brief: "Topological Field Theories and the Algebraic Structures of the Two-Sphere — We give two presentations for bordisms of S2 in the 3-dimensional oriented bor- dism category Cob(3), encoding the"
---
\label{sec: external prime relations}

\begin{prop} \label{primecommutativity}
(Prime Commutativity) Let $p^{\times \times}_1 , p^{\times \times}_2  \in P$ be prime endomorphisms. Then \[
p^{\times \times}_1 \circ p^{\times \times}_2 = p^{\times \times}_2 \circ p^{\times \times}_1 
.\]
\end{prop}

\begin{figure}[ht]
    \centering
    \incfig{primecommutativity}
    \caption[Prime endomorphism commutativity]{Prime endomorphism commutativity. Geometrically turning the left hand side upside down. Equivalently one can post-compose the Morse function by $x\mapsto -x$.}
    \label{fig:primecommutativity}
\end{figure}

\begin{proof}
By definition, connected sum is commutative, hence  $p_1 \# p_2 \cong p_2 \# p_1 $. Deleting a disk from both $ p_1, p_2  $, we have \[
	\left(p_1 \setminus\operatorname{int}( D^3)\right) \# \left(p_2 \setminus \operatorname{int}(D^3)\right) = \left(p_2 \setminus \operatorname{int}(D^3)\right) \# \left(p_1 \setminus \operatorname{int}(D^3)\right)
.\] 
Noting that $\#$ is the same as gluing over a bounding sphere, we have the desired relation.

Morse-theoretically, any Morse datum $(f,b=0)$ inducing the decomposition \[
	\left(p_1 \setminus \operatorname{int}(D^3 \sqcup D^3)\right) \cup_{S^2} \left(p_2 \setminus \operatorname{int}(D^3 \sqcup D^3)\right)
\]
also induces, via ``time reversal'' by post-composing with $\mathbb{R} \to \mathbb{R}$ sending $x \mapsto -x$ , the decomposition \[
	\left(p_2 \setminus \operatorname{int}(D^3 \sqcup D^3)\right) \cup_{S^2} \left(p_1 \setminus \operatorname{int}(D^3 \sqcup D^3)\right)
\]
.
\end{proof}

\begin{rmk} \label{rmk:Cerftheoryofprimecomm}
	Note however that this relation does not correspond to any specific type of singularities along Cerf-paths. Let $(f,b=0)$ be a Morse datum inducing $p^{\times \times}_1 \circ p^{\times \times}_2 $ and $(-f,b=0)$ be the time reversal Morse datum inducing $p^{\times \times}_2 \circ p^{\times \times}_1 $. Then a path $f_t$ from $f$ to $-f$ will generally be very complicated and contain multiple singularities. This is a feature of \textit{prime relations}. A prime relation is induced by a \textit{pair of Morse functions}  $f_0 ,f_1 : M \to \mathbb{R}$, rather than a specific type of singularities along a path from $f_0 $ to $f_1 $.
\end{rmk}

\begin{prop} \label{prop:legsandwaistrelations}
(Legs and Waist Relations) Let $p^{\times \times} \in P$ be a prime endomorphism, $m \in C$ the multiplication map, and $m^\vee\in F$ the comultiplication map. Then the following relations are always true: 
\begin{align}
p^{\times \times}  \circ m &= m \circ \left(p^{\times \times} \otimes id_{S^2}\right) = m \circ (id_{S^2} \otimes p^{\times \times} )\\
m^\vee \circ p^{\times \times}  &= (p^{\times \times} \otimes id_{S^2}) \circ m^\vee = (id_{S^2} \otimes p^{\times \times} ) \circ m^\vee
\end{align}
We shall call the first equality ``waist relations'' and the second equality ``legs relations,'' and the second line are the ``co-waist relations'' and ``co-legs relations.''
\end{prop}

\begin{figure}[ht]
    \centering
    \incfig{legsandwaist}
    \caption[Legs and waist relations]{A cartoon for legs and waist relations. All manifolds depicted are diffeomorphic, and boundary-preserving within each line. $p^{\times \times} $ here denotes the manifold $p\setminus \operatorname{int}(D^3 \sqcup D^3) $.}
    \label{fig:legsandwaist}
\end{figure}






\begin{proof}
Consider $p\setminus \operatorname{int}(\sqcup^3 D^3)$, but instead of $p$ itself, take the trivial gluing $p \cong \left( p \setminus \operatorname{int}(D^3 )\right)  \cup_S D^3$ along a two sphere $S$ (or equivalently the trivial connect sum $p \cong p \# S^3$). There are six ways to cut out three disjoint three-balls away from the gluing boundary such that a factor $p\setminus \operatorname{int}(D^3 \sqcup D^3)$ is present: Topologically, one ball must be cut from $p\setminus \operatorname{int}(D^3)$ to recover the prime endomorphism $p \setminus \operatorname{int}(D^3 \sqcup D^3)$, the other two must be cut from the trivially glued on three-ball. Those two deleted balls can form $(2,0), (1,1) $ or $ (0,2)$ (incoming, outgoing) boundaries. In the $(2,0)$ case, $m$ has two incoming boundaries, so $S$ must be the outgoing boundary of $m$ and the incoming boundary of $p^{\times \times} $, giving $p^{\times \times} \circ m$. In the $(0,2)$ case, $m^\vee$ has two outgoing boundaries, so $S$ must be the incoming boundary of $m^\vee$ and the outgoing boundary of $p^{\times \times} $, giving $m^\vee \circ p^{\times \times} $.

The case $(1,1)$ is only slightly more complicated. If $S$ is the incoming boundary of $p^{\times \times} $, then the only possible compositions are $(p^{\times \times}  \otimes id_{S^2})\circ m^\vee$ and $(id_{S^2} \otimes p^{\times \times} )\circ m^\vee$ (recall that the boundaries are labelled, so these two are different morphisms in $\operatorname{Cob}( 3)_{S^2, CF} $). If $S$ is the outgoing boundary of $p^{\times \times} $, then the only possible compositions are $m\circ (p^{\times \times} \otimes  id_{S^2}) $ and $m\circ (id_{S^2} \otimes p^{\times \times} )$.

All of the cases mentioned above are diffeomorphic as manifolds with boundaries. To establish equalities as bordisms in $\operatorname{Cob}(3)_{S^2}$, match the number of incoming and outgoing boundaries to give the claimed relations.
\end{proof}

\begin{rmk}
The Cerf-theoretic interpretation for the (co)legs and (co)waist relations are worth explaining. The (co)legs relations do not have any interesting Cerf theory-- for example, if the Morse datum $(f,b)$ induces \[
p\setminus \operatorname{int}\Big(\bigsqcup_{i=1}^3 D^3\Big) = \Big( S^3 \setminus \operatorname{int}(\sqcup_{i=1}^3 D^3) \Big) \bigcup_{S^2 \sqcup S^2} \Big( (p \setminus \operatorname{int}(D^3 \sqcup D^3)) \bigsqcup \left( S^2 \times I \right)  \Big) 
.\]
which induces the composition $m\circ (p^{\times \times} \otimes id_{S^2})$, then the same Morse datum $(f,b)$ also induces $m \circ (id_{S^2} \otimes p^{\times \times} )$ by switching the factors $p \setminus \operatorname{int}(D^3 \sqcup D^3)$ and $S^2 \times I$. So echoing the comments made in remark \ref{rmk:Cerftheoryofprimecomm}, the (co)legs relations are induced by the pair of Morse functions $f, f:p \setminus \operatorname{int}(\sqcup^3 D^3) \to \mathbb{R}$. We can always take the constant path from $f$ to itself when constructing a Cerf path.

The (co)waist relations are, in contrast, induced by two different Morse functions $f_{\text{upper}}, f_{\text{lower}} : p \setminus (\sqcup^3 D^3) \to \mathbb{R}$, where the subscript denotes where the prime endomorphism $p^{\times \times} $ sits in relations to $m$ or $m^\vee$ (later in the composition or earlier in the composition). Again, a path $f_t$ from $f_ \text{upper}$ to $f_ \text{lower}$ is generally very complicated and contain multiple singularities. One can imagine that, even in the simplest case, the index $2$ critical point of $m$ must be moved past all critical points of $p^{\times \times} $, so the path $f_t$ contains at least as many singularities as $f_{\text{upper}}$ has critical points, minus one. This is a feature of prime relations, as first discussed in \ref{rmk:Cerftheoryofprimecomm}.

\end{rmk}











\begin{rmk}
As there are countably many diffeomorphism classes of prime 3-manifolds, there are countably many such legs and waist relations.
\end{rmk}

\begin{rmk}
Notice that $p^{\times \times} $ is not an algebra homomorphism with respect to $m$: for this to hold, we would need $p^{\times \times} \circ m = m\circ (p^{\times \times}  \otimes p^{\times \times} )$, but the left hand side has one factor of $p$ while the right has two. Nor does it preserve the unit: in fact, it turns the unit into the corresponding prime unit $p^{\times \times} \circ 1 = p^\times$.
\end{rmk}

One may wonder if there are similar relations involving the prime units and the commutative Frobenius generators. The answer is yes-- but it's not very interesting or useful. Since a prime unit's boundary is outgoing, it can only be attached to incoming boundaries. Thus we are led to the following relations. Note that the proposition \ref{prop:LlegsfromCF} immediately afterwards renders these relations unnecessary, as they are implied by commutativity of the commutative Frobenius relations. In fact, the proof of theorem \ref{mainthmG1} does not make use of these relations at all, in contrast to the proof of theorem \ref{mainthmG2} which uses all of the prime endomorphism relations.

\begin{prop} \label{prop:Llegs}
(Legs Relations) Let $p^\times \in L$ be a prime unit, $m \in C$ the multiplication map and $m^\vee \in F$ the comultiplication map. Then the following relations are always true: \[
m \circ (p^\times \otimes id_{S^2}) \circ \lambda^{-1}_{S^2} = m\circ (id_{S^2} \otimes p^\times)\circ \rho ^{-1}_{S^2}
.\]
where $\lambda_{S^2}: \emptyset \sqcup S^2 \overset{\sim}{\to} S^2$ is the left unitor and $\rho_{S^2} : S^2 \sqcup \emptyset \overset{\sim}{\to} S^2$ is the right unitor.
We shall call this equality the ``legs relations.''
\end{prop}

\begin{figure}[ht]
    \centering
    \incfig{llegs}
    \caption[Legs relations for $G_1$]{Legs relations for $p^\times L \subset G_1$.}
    \label{fig:llegs}
\end{figure}




\begin{proof}
Geometrically this is an obvious statement. Consider the gluing \[
p\setminus  \operatorname{int}\Big(D^3\bigsqcup D^3\Big)  \cong \Big( p \setminus \operatorname{int}(D^3) \Big)  \bigcup_{S^2} \Big( S^3 \setminus \operatorname{int}(\bigsqcup_{i=1}^3 D^3) \Big)
.\]
Since the sphere boundary of a prime unit is outgoing, one of the sphere boundaries of the $S^3\setminus \operatorname{int}(\sqcup^3 D^3)$ factor must be incoming. Choosing one of the remaining two as outgoing and the other as incoming, this decomposition induces two compositions of $[p\setminus \operatorname{int}(\sqcup^2 D^3)]$ (which we recognize as the corresponding prime endomorphism, see \ref{criticalrelations}). Since the incoming boundary is either $\emptyset \sqcup S^2$ or  $S^2 \sqcup \emptyset$, we can resolve the two cases with a left or right unitor respectively, giving the desired equality of morphisms.
\end{proof}

\textbf{Warning:} what follows, and what will follow the next two sections, lean heavy on coherence conditions of symmetric monoidal categories. We made the deliberate choice of carefully exhibiting unitors, associators, and braiding, because it enables the reader to apply the results in a non-strict symmetric monoidal category $\mathcal{C}$ after passing through a $3$-dimensional topological field theories $Z: \operatorname{Cob}( 3) \to \mathcal{C}$.

\begin{notations} \label{coherencenotations}
Let $(\mathcal{C}, \otimes , 1_{\otimes })$ be a symmetric monoidal category and $\lambda: 1_ \otimes \otimes  (-) \Rightarrow Id_{\mathcal{C}}$ the natural isomorphism which gives the left unitors, and $\rho : (-) \otimes 1_{\otimes } \Rightarrow Id_{\mathcal{C}}$ the natural isomorphism which gives the right unitors. Denote their morphisms at an object $A\in \mathcal{C}$ by $\lambda_A : 1_{\otimes } \otimes A \overset{\sim}{\to} A$ and $\rho _A : A \otimes 1_{\otimes } \overset{\sim}{\to} A$. Denote by $\beta _{A,B}$ the braiding $A \otimes B \overset{\sim}{\to} B \otimes A$. Denote by $\alpha_{A,B,C}$ the associator $(A \otimes B) \otimes C \overset{\sim}{\to} A \otimes (B \otimes C)$
\end{notations}

\begin{prop} \label{prop:LlegsfromCF}
Leg relations for $L$ are implied by commutativity of the commutative Frobenius relations.
\end{prop}
\begin{proof}
We want to show that $m\circ ( p^\times \otimes id_{S^2} )  \circ \lambda^{-1}_{S^2} =m \circ (id_{S^2} \otimes p^\times) \circ \rho^{-1}_{S^2} $ is a consequence of commutative Frobenius relations.

Let $f: A\to A'$ and $g:B\to B'$ be two morphisms of a symmetric monoidal category. Then by naturality of braiding , the following diagram commutes 

\[\begin{tikzcd}
{A\otimes B} & {A'\otimes B'} \\
{B\otimes A} & {B'\otimes A'}
\arrow["{f\otimes g}", from=1-1, to=1-2]
\arrow["{\beta _{A,B}}"', from=1-1, to=2-1]
\arrow["{g\otimes f}", from=2-1, to=2-2]
\arrow["{\beta _{B',A'}}"', from=2-2, to=1-2]
\end{tikzcd}\]
In particular, for $f=p^\times: \emptyset \to S^2 $ and $g=id_{S^2}$, we have
\[
p^\times \otimes id_{S^2} = \beta _{S^2 \sqcup S^2} \circ (id_{S^2} \otimes p^\times) \circ \beta_{\emptyset \sqcup S^2} = \beta  _{S^2 \sqcup S^2} \circ (id_{S^2} \otimes p^\times) \circ (\rho^{-1}_{S^2} \circ \lambda_{S^2})
\]

Therefore we may substitute the above relation into the left hand side of the legs relation \[
m\circ (p^\times \otimes id_{S^2}) \circ \lambda^{-1}_{S^2} = m \circ \beta _{S^2 \sqcup S^2} \circ (id_{S^2} \otimes p^\times) \circ (\rho^{-1}_{S^2} \circ \lambda_{S^2}) \circ \lambda^{-1}_{S^2} = m \circ (id_{S^2} \otimes p^\times) \circ \rho^{-1}_{S^2}
.\]
where the second equality is due to commutativity $m = m\circ \beta _{S^2 \sqcup S^2}$. We recognize the right hand side as the desired composition.
\begin{figure}[ht]
    \centering
    \incfig{llegsfromcf}
    \caption[Redundancy of $G_1$ legs relations]{Redundancy of $L$ legs relations.}
    \label{fig:llegsfromcf}
\end{figure}



\end{proof}

\begin{rmk}
Note that in $\operatorname{Cob}(3)_{S^2}$, there is equality of morphisms $[p\setminus (D^3 \sqcup D^3)]= m \circ ([p \setminus D^3] \otimes id_{S^2}) \circ \lambda^{-1}_{S^2} = m\circ (id_{S^2} \otimes [p \setminus D^3])\circ \rho ^{-1}_{S^2} $, or more succinctly  \[
p^{\times \times}  = m\circ (p^\times \otimes id_{S^2}) \circ \lambda^{-1}_{S^2} = m \circ (id_{S^2} \otimes p^\times ) \circ \rho ^{-1}_{S^2}
.\]
But this does not constitute a relation in the usual sense-- the left hand side is a $P$ generator while the right hand sides involve $L$ generators. They belong to different presentations, $G_2$ and $G_1$. More on this in lemma \ref{lem:consistencyislegs} and the discussion right before it.
\end{rmk}
