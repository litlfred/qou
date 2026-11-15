---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-008-8-l-quasi-isomorphisms-between-pronilpotent-alge
section_title: "L Quasi-isomorphisms between Pronilpotent Algebras"
section_number: 8
pages: 26-31
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.98
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:L-infty-cplt}

Let $(R, \m)$ be a parameter $\K$-algebra, and let
$\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ morphism between DG Lie algebras. 
Then $\Phi$ extends uniquely to an $R$-multilinear $\mrm{L}_{\infty}$ morphism 
\[ \Phi_{R} : R \hot \g \to R \hot \h , \]
whose $i$-th Taylor coefficient
\[ \partial^i \Phi_{R} :
\underset{i}{\underbrace{(R \hot \g) \times \cdots \times 
(R \hot \g)}} \to R \hot \h \]
is the $R$-multilinear homogeneous extension of 
$\partial^i \Phi$. See \cite[Section 3]{Ye2} for more details. 

\begin{dfn} \label{dfn:6}
Let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ morphism, and let 
$(R, \m)$ be a parameter algebra. For an element 
$\om \in \m \hot \g^1$ we define
\[ \opn{MC}(\Phi, R)(\om) := 
\sum_{i \geq 1} \, \smfrac{1}{i!} (\partial^i \Phi_{R})
(\underset{i}{\underbrace{\om, \ldots, \om}}) \in \m \hot \h^1 . \]
\end{dfn}

Note that the sum above converges in the $\m$-adic topology of 
$\m \hot \h^1$, since 
\[ (\partial^i \Phi_{R})(\om, \ldots, \om)
\in \m^i \hot \h^1 = \m^{i-1} \cdot (\m \hot \h^1) . \]

\begin{prop} \label{prop:4}
Let 
$\om \in \opn{MC}(\g, R) = \opn{MC}(\m \hot \g)$.
Then the element
$\opn{MC}(\Phi, R)(\om)$ belongs to $\opn{MC}(\h, R)$.
Thus we get a function 
\[ \opn{MC}(\Phi, R) : \opn{MC}(\g, R) \to \opn{MC}(\h, R) . \]
\end{prop}

\begin{proof}
Let $R_j := R / \m^{j+1}$, and let $p_j : R \to R_j$ be the projection.
According to \cite[Theorem 3.21]{Ye2}, which refers to the artinian case, we
have
\[ \opn{MC}(\Phi, R_j)(p_j(\om)) \in \opn{MC}(\h , R_j) \]
for every $j$. And by Lemma \ref{lem:6}(2) we know that 
\[ \opn{MC}(\h, R) \cong 
\lim_{\leftarrow j}\, \opn{MC}(\h, R_j) . \]
\end{proof}

Let $\Om_{\K[t]} = \K[t] \oplus \Om^1_{\K[t]}$ be the algebra of polynomial
differential forms
in the variable $t$ (relative to $\K$). This is a commutative DG
algebra. For $\la \in \K$ there is a DG algebra homomorphism
$\sg_{\la} : \Om_{\K[t]} \to \K$, namely $t \mapsto \la$.
There is an induced homomorphism of DG Lie algebras 
\begin{equation} \label{eqn:2}
\sg_{\la}  :  \m \hatotimes \Om_{\K[t]} \hatotimes \g \to 
\m \hatotimes \g ,
\end{equation}
and an induced function
\begin{equation} \label{eqn:61}
\ol{\opn{MC}}(\sg_{\la}) : 
\ol{\opn{MC}} ( \m \hatotimes \Om_{\K[t]} \hatotimes \g) 
\to \ol{\opn{MC}}(\m \hatotimes \g) 
\end{equation}

We shall often think of elements of $\Om_{\K[t]}$ as 
``functions of $t$'', as in Section \ref{sec:facts}. Given elements
$f(t) \in \Om_{\K[t]}$ and $\la \in \K$,
we shall use the substitution notation  
$f(\la) := \sg_{\la} (f(t)) \in \K$.

\begin{lem} \label{lem:16}
Here $\lambda = 0, 1$. 
\begin{enumerate}
\item The homomorphisms $\sg_0, \sg_1$ in formula \tup{(\ref{eqn:2})}
are quasi-iso\-morphisms.

\item The functions $\ol{\opn{MC}}(\sg_0)$ and $\ol{\opn{MC}}(\sg_1)$
in formula \tup{(\ref{eqn:61})} are bijections.

\item The bijections 
$\ol{\opn{MC}}(\sg_0)$ and $\ol{\opn{MC}}(\sg_1)$ are equal.
\end{enumerate} 
\end{lem}

\begin{proof}
(1) This is because the homomorphisms $\sg_i : \Om_{\K[t]} \to \K$ are
homotopy equivalences (of complexes of $\K$-modules).

\medskip \noindent
(2) This is by item (1) and Theorem \ref{thm:2}.

\medskip \noindent
(3) Note that the inclusion
\[ \phi : \m \hot \g \to \m \hatotimes \Om_{\K[t]} \hatotimes \g \]
is also a quasi-isomorphism, and that 
$\sg_0 \circ \phi = \sg_1 \circ \phi$ is the identity automorphism of 
$\m \hot \g$. Hence 
\[ \ol{\opn{MC}}(\sg_0) \circ \ol{\opn{MC}}(\phi) = 
\ol{\opn{MC}}(\sg_1) \circ \ol{\opn{MC}}(\phi) , \]
and canceling the bijection $\ol{\opn{MC}}(\phi)$ we obtain our result.
\end{proof}

\begin{lem} \label{lem:17}
Let $\om_0, \om_1 \in \opn{MC}(\m \hatotimes \g)$. The following two
conditions are equivalent:
\begin{enumerate}
\rmitem{i} There exists an element 
$g \in \opn{exp}(\m \hatotimes \g^0)$ such that 
\[ \opn{Af}(g)(\om_0) = \om_1 . \]
\rmitem{ii} There exists an element 
\[ \om(t) \in 
\opn{MC}( \m \hatotimes \Om_{\K[t]} \hatotimes \g) \]
such that 
$\om(0) = \om_0$ and $\om(1) = \om_1$. 
\end{enumerate}
\end{lem}

\begin{proof}
(i) $\Rightarrow$ (ii): Consider the elements $\ga := \log(g) \in \m \hot
\g^0$, 
\[ g(t) := \exp(t \ga) \in \exp(\m \hot (\Om_{\K[t]} \ot \g)^0) \]
and 
\[ \om(t) :=  \opn{Af}(g(t))(\om_0) \in 
\opn{MC}(\m \hot \Om_{\K[t]} \hot \g) . \]
Then 
\[ \om(0) = \opn{Af}(g(0))(\om_0) = \opn{Af}(1)(\om_0) = \om_0 \]
and
\[ \om(1) = \opn{Af}(g(1))(\om_0) =
\opn{Af}(g)(\om_0) = \om_1 . \]

\medskip \noindent
(ii) $\Rightarrow$ (i): Let us write $[\om_i]$ for the classes in 
$\ol{\opn{MC}}(\m \hatotimes \g)$.
We know that 
\[ \ol{\opn{MC}}(\sg_i)([\om(t)]) = [\om_i] \]
for $i = 0, 1$. By Lemma \ref{lem:16}(3) we know that 
$\ol{\opn{MC}}(\sg_0) = \ol{\opn{MC}}(\sg_1)$.
Therefore $[\om_0] = [\om_1]$; and by definition this says that 
$\opn{Af}(g)(\om_0) = \om_1$ for some $g$. 
\end{proof}

\begin{prop} \label{prop:5}
Let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ morphism.
The function 
\[ \opn{MC}(\Phi, R) : \opn{MC}(\g, R) \to \opn{MC}(\h, R) \]
respects gauge equivalences. Therefore there is an induced function 
\[ \ol{\opn{MC}}(\Phi, R) : \ol{\opn{MC}}(\g, R) \to 
\ol{\opn{MC}}(\h, R) . \]
\end{prop}

\begin{proof}
Let $A:= R \hot \Om_{\K[t]}$, which is a commutative DG algebra. There
are induced homomorphisms $\sg_i : A \to R$.
And there is an induced $A$-multilinear $\mrm{L}_{\infty}$ morphism 
\[ \Phi_{A} : \m \hot \Om_{\K[t]} \hot \g \to 
\m \hot \Om_{\K[t]} \hot \h  \]
(cf.\ \cite[Section 3]{Ye2}).
Let us write 
$\opn{MC}(\g, A) := \opn{MC}(\m \hot \Om_{\K[t]} \hot \g)$ etc.
There is a function $\opn{MC}(\Phi, A)$ whose formula is like in Definition
\ref{dfn:6}. Since the $\mrm{L}_{\infty}$ morphisms $\Phi_R$ and
$\Phi_A$ are induced from $\Phi$,
the diagram of functions 
\[ \UseTips \xymatrix @C=11ex @R=6ex {
\opn{MC}(\g, A) 
\ar[r]^{\opn{MC}(\Phi, A)}
\ar[d]_{\opn{MC}(\sg_i, R)}
&
\opn{MC}(\h, A) 
\ar[d]^{\opn{MC}(\sg_i, R)}
\\
\opn{MC}(\g, R) 
\ar[r]^{\opn{MC}(\Phi, R)}
&
\opn{MC}(\h, R) 
} \]
is commutative, for $i = 0, 1$.
Now suppose $\om_0, \om_1 \in \opn{MC}(\g, R)$ are gauge equivalent. By Lemma
\ref{lem:17} there is an element $\om(t) \in \opn{MC}(\g, A)$ such that 
$\om(i) = \om_i$. Define
$\chi_i := \opn{MC}(\Phi, R)(\om_i)$ and 
$\chi(t) := \opn{MC}(\Phi, A)(\om(t))$. 
Because the diagram above is commutative, we have
$\chi(i) = \chi_i$. Using Lemma \ref{lem:17} again we conclude that 
$\chi_0$ and $\chi_1$ are gauge equivalent.
\end{proof}

Let $\Psi : C \to D$ be the morphism in $\cat{DGCog}(\K)$ gotten by applying
the functor $\opn{C}_{\infty}$ to the $\opn{L}_{\infty}$ morphism 
$\Phi : \g  \to \h$. And let 
$\til{\Psi} : \til{C} \to \til{D}$ be the morphism gotten by applying
the functor $\opn{C} \circ \opn{L}$ to $\Psi : C \to D$. 
Since $\th_-$ is a natural transformation, we get a
commutative diagram 
\begin{equation} \label{eqn:62}
\UseTips \xymatrix @C=7ex @R=5ex {
C
\ar[r]^{\Psi}
\ar[d]_{\th_C}
&
D
\ar[d]^{\th_D}
\\
\til{C}
\ar[r]^{\til{\Psi}}
&
\til{D}
} 
\end{equation}
in $\cat{DGCog}(\K)$.
There is a corresponding commutative diagram 
\begin{equation} \label{eqn:63}
\UseTips \xymatrix @C=7ex @R=5ex {
\g
\ar[r]^{\Phi}
\ar[d]_{\th_{\g}}
&
\h
\ar[d]^{\th_{\h}}
\\
\til{\g}
\ar[r]^{\til{\Phi}}
&
\til{\h}
} 
\end{equation}
in $\cat{DGLie}_{\infty}(\K)$. Namely 
$\til{\g} = (\opn{L} \circ \opn{C})(\g)$,
$\til{\h} = (\opn{L} \circ \opn{C})(\h)$, 
and the full faithful functor $\opn{C}_{\infty}$ sends the 
diagram (\ref{eqn:63}) to the diagram (\ref{eqn:62}).
Note that by the proof of Lemma \ref{lem:20}, the Taylor coefficients
$\pa^j \th_C$ are nonzero for all $j$; so the corresponding morphism 
$\th_{\g} : \g \to \til{\g}$ in $\cat{DGLie}_{\infty}(\K)$ is not a DG Lie
algebra homomorphism. The same for $\th_{\h}$.

\begin{lem} \label{lem:18}
The diagram of functions
\begin{equation} \label{eqn:65}
\UseTips \xymatrix @C=11ex @R=6ex {
\opn{MC}(\g, R)
\ar[r]^{\opn{MC}(\Phi, R)}
\ar[d]_{\opn{MC}(\th_{\g}, R)}
&
\opn{MC}(\h, R)
\ar[d]^{\opn{MC}(\th_{\h}, R)}
\\
\opn{MC}(\til{\g}, R)
\ar[r]^{\opn{MC}(\til{\Phi}, R)}
&
\opn{MC}(\til{\h}, R)
} 
\end{equation}
is commutative.
\end{lem}

\begin{proof}
Because of Lemma \ref{lem:6}(2) we can assume that $R$ is artinian.
Consider the commutative diagram of DG coalgebras over $R$
\begin{equation} \label{eqn:67}
\UseTips \xymatrix @C=11ex @R=6ex {
R \ot C
\ar[r]^{\Psi_R}
\ar[d]_{\th_{C, R}}
&
R \ot D
\ar[d]^{\th_{D, R}}
\\
R \ot \til{C}
\ar[r]^{\til{\Psi}_R}
&
R \ot \til{D}
} 
\end{equation}
induced from (\ref{eqn:62}) by tensoring with $R$. 

Take any $\om \in \m \ot \g^1 \subset R \ot C$, and define 
\[ e := \exp(\om) = \sum_{i \geq 0} \, \smfrac{1}{i!} \om^i \in R \ot C . \]
According to \cite[Lemma 3.18]{Ye2} we have
\[ \begin{aligned}
& \bigl( \opn{MC}(\th_{\h}, R) \circ \opn{MC}(\Phi, R) \bigr)(\om) =
\log \bigl( (\th_{D, R} \circ \Psi_R)(e) \bigr) = \\
& \qquad \log \bigl( (\til{\Psi}_R \circ \th_{C, R})(e) \bigr) =
\bigl( \opn{MC}(\til{\Phi}, R) \circ \opn{MC}(\th_{\g}, R) \bigr)(\om) . 
\end{aligned} \]
This proves commutativity of the diagram.
\end{proof}



\begin{thm} \label{thm:3}
Let $\g$ and $\h$ be DG Lie algebras, 
let $\Phi : \g \to \h$ be an $\mrm{L}_{\infty}$ quasi-isomorphism, and
let $R$ be a parameter algebra, all over the field $\K$. 
Then the function 
\[ \ol{\opn{MC}}(\Phi, R) : \ol{\opn{MC}}(\g, R) \to 
\ol{\opn{MC}}(\h, R) \]
\tup{(}see Proposition \tup{\ref{prop:5})} is bijective. 
\end{thm}

The idea for the proof was suggested to us by Van den Bergh.

\begin{proof}
By Lemma \ref{lem:21} the DG Lie algebra homomorphism 
$\til{\Psi} : \til{\g} \to \til{\h}$ is a quasi-isomorphism.
Therefore by Theorem \ref{thm:2} the function 
\[  \ol{\opn{MC}}(\til{\Phi}, R) : \ol{\opn{MC}}(\til{\g}, R) \to 
\ol{\opn{MC}}(\til{\h}, R) \]
is bijective.

Next, by \cite[Proposition 4.4.3(1)]{Hi2} the DG Lie algebra homomorphism
$\zeta_{\g} : \til{\g} \to \g$ is a  quasi-isomorphism.
Again using Theorem \ref{thm:2} we conclude that the function 
\[  \ol{\opn{MC}}(\zeta_{\g}, R) : \ol{\opn{MC}}(\til{\g}, R) \to 
\ol{\opn{MC}}(\g, R) \]
is bijective. On the other hand, by Lemma \ref{lem:20}, with the arguments in
the proof of Lemma \ref{lem:18}, we see that 
\[ \opn{MC}(\zeta_{\g}, R) \circ \opn{MC}(\th_{\g}, R) = 
\bsym{1}_{\opn{MC}(\g, R)} . \]
Therefore 
\[ \ol{\opn{MC}}(\zeta_{\g}, R) \circ \ol{\opn{MC}}(\th_{\g}, R) = 
\bsym{1}_{\ol{\opn{MC}}(\g, R)} . \]
Because $\ol{\opn{MC}}(\zeta_{\g}, R)$ is a bijection, the same is true for the
function $\ol{\opn{MC}}(\th_{\g}, R)$. 
The same line of reasoning says that 
$\ol{\opn{MC}}(\th_{\h}, R)$ is bijective. 

Finally consider the commutative diagram of functions
\[ \UseTips \xymatrix @C=11ex @R=6ex {
\ol{\opn{MC}}(\g, R)
\ar[r]^{\ol{\opn{MC}}(\Phi, R)}
\ar[d]_{\ol{\opn{MC}}(\th_{\g}, R)}
&
\ol{\opn{MC}}(\h, R)
\ar[d]^{\ol{\opn{MC}}(\th_{\h}, R)}
\\
\ol{\opn{MC}}(\til{\g}, R)
\ar[r]^{\ol{\opn{MC}}(\til{\Phi}, R)}
&
\ol{\opn{MC}}(\til{\h}, R)
} \]
induced from (\ref{eqn:65}). 
We know that three of the arrows are bijective; so the fourth arrow, namely 
$\ol{\opn{MC}}(\Phi, R)$, is also bijective.
\end{proof}

\begin{rem} \label{rem:1}
Lemma 3.5 in our earlier paper \cite{Ye1} says that the canonical function 
\[ \ol{\opn{MC}}(\g, R) \to \lim_{\leftarrow j} \,
\ol{\opn{MC}}(\g, R / \m^j) \]
is bijective. The proof of this Lemma
(which is actually omitted from the paper) is incorrect. Moreover, we
suspect that statement itself is false. The hidden assumption was that 
the gauge group $\opn{G}(\g, R)$ acts on the set $\opn{MC}(\g, R)$
with {\em closed} orbits. 

This lemma is used to deduce \cite[Corollary 3.10]{Ye1} (incorrectly) 
from the nilpotent case. The correction is to replace 
\cite[Corollary 3.10]{Ye1} with Theorem \ref{thm:3} above.
The same correction pertains also to \cite[formula (12.2)]{Ye4}.
\end{rem}

\begin{rem}
This is a good place to correct a typographical error (repeated several
times) in \cite[Section 3]{Ye2}. In Lemmas 3.14 and 3.18 of op.\ cit., instead
of ``$\m \g [1]$'' the correct expression should be ``$\m \g^1$'' or
``$(\m \g [1])^0$''.

Let us also mention that a ``colocal coalgebra homomorphism'', in the sense of 
\cite[Definition 3.3]{Ye2}, is the same as a ``unital coalgebra homomorphism''.
\end{rem}
