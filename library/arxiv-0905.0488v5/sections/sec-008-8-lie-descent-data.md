---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES"
section_id: sec-008-8-lie-descent-data
section_title: "Lie Descent Data"
section_number: 8
pages: 36-39
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.982
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES — Let X be a smooth algebraic variety over a ﬁeld K containing the real numbers. We introduce the notion of twisted associative (resp."
---
\label{sec:Lie-desc}

We begin this section by recalling what are $\mrm{L}_{\infty}$ morphisms
between DG Lie algebras,
following \cite[Sections 7-8]{Ye7}; see also \cite{Ko1, Hi2, CKTB}.
We denote by $\cat{DGLie} (\K)$ the category of differential graded Lie algebras
over $\K$, and by $\cat{DGCog}(\K)$ the category of DG unital cocommutative
coalgebras over $\K$. There are functors 
\[ \cat{DGLie}(\K) \xar{\opn{C}} \cat{DGCog}(\K) \xar{\opn{L}}
\cat{DGLie}(\K) , \]
called the {\em bar} and {\em cobar} functors respectively. 
These functors are adjoint to each other, and they have explicit formulas. 
The functor $\opn{C}$ is faithful.
By definition an $\mrm{L}_{\infty}$ morphism 
$\Psi : \g \to \h$ between DG Lie algebras $\g$ and $\h$
is a coalgebra homomorphism $\opn{C}(\Psi) : \opn{C}(\g) \to \opn{C}(\h)$.
In this way we get a new category $\cat{DGLie}_{\infty}(\K)$, with
functors 
\[ \cat{DGLie} (\K) \xar{\opn{inc}} \cat{DGLie}_{\infty}(\K)
\xar{\opn{C}} \cat{DGCog}(\K) , \]
the first faithful and bijective of objects, and the second fully faithful.

The explicit formula for the functor $\opn{C}$ allows an explicit (yet
cumbersome) description of $\mrm{L}_{\infty}$ morphisms. An $\mrm{L}_{\infty}$
morphism $\Psi : \g \to \h$ can be described as a sequence
$\Psi = \{ \Psi_i \}_{i \geq 1}$ of $\K$-multilinear functions
$\Psi_i : \bwedge^i \g \to \mfrak{h}$,
satisfying certain equations (see \cite{Ko1}, 
\cite[Definition 3.7]{Ye1}, \cite[Section 3.7]{CKTB} or \cite[Section 7]{Ye7}).
The homomorphism $\Psi_1 : \g \to \mfrak{h}$ is a homomorphism of DG
$\K$-modules, and it respects the Lie brackets up to the homotopy
$\Psi_2$; and so on. Thus if $\Psi_i = 0$ for all $i \geq 2$, then 
$\Psi_1 : \g \to \mfrak{h}$ is a DG Lie algebra homomorphism.
An $\mrm{L}_{\infty}$ morphism 
$\Psi = \{ \Psi_i \}_{i \geq 1}$ is called a quasi-isomorphism
if $\Psi_1$ is a quasi-isomorphism. 

Take a DG Lie algebra $\g$, and let 
$\til{\g} := (\opn{L} \circ \opn{C})(\g)$.
According to \cite[Proposition 4.4.3(1)]{Hi2} the adjunction homomorphism
$\zeta_{\g} : \til{\g} \to \g$ in $\cat{DGLie}(\K)$ is a 
quasi-isomorphism. Thus if $\g$ is a quasi quantum type DG Lie algebra, then 
so is $\til{\g}$. (Note that even if $\g$ is quantum type, but nonzero, the DG
Lie algebra  $\til{\g}$ is unbounded below.) Thus we have a functor 
\[ \opn{L} \circ \opn{C} : \cat{DGLie}_{\infty}(\K) \to \cat{DGLie}(\K) \]
sending quasi quantum type DG Lie algebras to quasi quantum type DG Lie
algebras. 

Now suppose $(S, \n)$ is another parameter algebra, and
$\nu : R \to S$ is a homomorphism of parameter algebras. 
There are pronilpotent DG Lie algebras $\m \hot \g$ and 
$\n \hot \h$, an
induced $R$-multilinear $\mrm{L}_{\infty}$ morphism
$\nu \hot \Psi : \m \hot \g \to \n \hot \mfrak{h}$.
We know that there is an induced function
\begin{equation}
\opn{MC}(\nu \hot \Psi) : \opn{MC}(\m \hot \g) \to 
\opn{MC}(\n \hot \mfrak{h})
\end{equation}
between MC sets, with explicit formula
\begin{equation} \label{eqn:300}
\opn{MC}(\nu \hot \Psi) (\om) :=
\sum_{i \geq 1} \smfrac{1}{i!} \Psi_{i}(\nu(\om), \ldots, \nu(\om)) .
\end{equation}
The function $\opn{MC}(\nu \hot \Psi)$ is functorial in $\Psi$ and $\nu$.
If $\Psi$ is an $\mrm{L}_{\infty}$ quasi-isomorphism and $\nu$ is an
isomorphism, then we get an induced bijection
\begin{equation} \label{eqn:22}
\ol{\opn{MC}}(\nu \hot \Psi) : \ol{\opn{MC}}(\m \hot \g) \to 
\ol{\opn{MC}}(\n \hot \mfrak{h})  
\end{equation}
on gauge equivalence classes.
See \cite[Theorem 4.2]{Ye7}.

Now let us suppose that $\g$ and $\h$ are of quasi quantum type
(Definition \ref{dfn:220}), so
that their Deligne crossed groupoids exits. If $\Psi : \g \to \h$ is a DG Lie
homomorphism, then there is an induced morphism of crossed groupoids
\begin{equation} \label{eqn:403}
\opn{Del}(\Psi, \nu) : \opn{Del}(\g, R) \to \opn{Del}(\h, S) ,
\end{equation}
and this is functorial in $\Psi$ and $\nu$. Furthermore, if $\Psi$ is a
quasi-isomorphism and $\nu$ is an isomorphism, then $\opn{Del}(\Psi, \nu)$ is a
weak equivalence of crossed groupoids, by \cite[Theorem 0.4]{Ye7}.
However we do not know if this is true when $\Psi$ is  an $\mrm{L}_{\infty}$
morphism; to be precise, we do not know if there is a functor $\opn{Del}(-,R)$
from $\cat{DGLie}_{\infty}(\K)$ to $\cat{CrGrpd}$. 
The best we can do is the next theorem. 

\begin{thm} \label{thm:400}
Let $\Psi : \g \to \h$ be an $\mrm{L}_{\infty}$ morphism between 
quasi quantum type DG Lie algebras, and let 
$\nu : R \to S$ be a homomorphism between parameter algebras.
Consider the first diagram below. It is a diagram in $\cat{DGLie}(\K)$, 
where $\til{\g} := (\opn{L} \circ \opn{C})(\g)$, 
$\til{\h} := (\opn{L} \circ \opn{C})(\h)$, 
$\til{\Psi} := (\opn{L} \circ \opn{C})(\Psi)$,
and $\zeta_{\g}$, $\zeta_{\h}$ are the adjunction morphisms.
Applying $\opn{Del}(-,-)$ to it we obtain the second diagram, which
is in $\cat{CrGrpd}$.
\[
\UseTips \xymatrix @C=6ex @R=4ex {
\til{\g}
\ar[d]_{\zeta_{\g}}
\ar[r]^(0.5){\til{\Psi}}
&
\til{\h}
\ar[d]^{\zeta_{\h}}
\\
\g
&
\h
} 
\hspace{8ex}
\UseTips \xymatrix @C=10ex @R=5ex {
\opn{Del}(\til{\g}, R)
\ar[d]_{\opn{Del}(\zeta_{\g}, \bsym{1}_R)}
\ar[r]^(0.5){\opn{Del}(\til{\Psi}, \nu)}
&
\opn{Del}(\til{\h}, S)
\ar[d]^{\opn{Del}(\zeta_{\h}, \bsym{1}_S)}
\\
\opn{Del}(\g, R)
&
\opn{Del}(\h, S)
}
\]
Then the morphisms $\opn{Del}(\zeta_{\g}, \bsym{1}_R)$ and 
$\opn{Del}(\zeta_{\h}, \bsym{1}_S)$ in $\cat{CrGrpd}$ are weak equivalences.
If $\Psi$ is an  $\mrm{L}_{\infty}$ quasi-isomorphism, 
and if $\nu$ is an isomorphism, then 
$\opn{Del}(\til{\Psi}, \nu)$ is a weak equivalence.
\end{thm}

\begin{proof}
As already noted, the vertical arrows in the first diagram above
are quasi-isomorphisms (this is by \cite[Proposition 4.4.3(1)]{Hi2}).
According to \cite[Theorem 6.13]{Ye7} the morphisms 
$\opn{Del}(\zeta_{\g}, \bsym{1}_R)$ and 
$\opn{Del}(\zeta_{\h}, \bsym{1}_S)$ are weak equivalences. 

If $\Psi$ is an $\mrm{L}_{\infty}$ quasi-isomorphism and $\nu$ is an
isomorphism, then by \cite[Lemma 7.3]{Ye7} the  DG Lie homomorphism
$\til{\Psi} : \til{\g} \to \til{\h}$ is a quasi-isomorphism.
Again using \cite[Theorem 6.13]{Ye7} we conclude that 
$\opn{Del}(\til{\Psi}, \nu)$ is a weak equivalence.
\end{proof}

 A cosimplicial DG Lie algebra, i.e.\ an object of
$\bsym{\Delta}(\cat{DGLie} (\K))$, is  a collection
$\g = \{ \mfrak{g}^{p} \}_{p \in \mbb{N}}$
of DG Lie algebras
$\mfrak{g}^{p} = \bigoplus_{i \in \mbb{Z}} \mfrak{g}^{p, i}$.
For every $\alpha \in \bsym{\Delta}^q_p$
there is a DG Lie algebra homomorphism 
$\g(\alpha) : \mfrak{g}^{p} \to \mfrak{g}^{q}$,
and these homomorphisms satisfy the simplicial relations.
A cosimplicial DG Lie algebra 
$\g = \{ \mfrak{g}^{p} \}_{p \in \mbb{N}}$ is said to be of quasi quantum type
if every $\g^p$ is a  quasi quantum type DG Lie algebra.

A cosimplicial quasi quantum type DG Lie algebra 
$\g = \{ \mfrak{g}^{p} \}_{p \in \mbb{N}}$ and a parameter algebra $R$
give rise to a cosimplicial crossed groupoid 
$\opn{Del}(\g, R) = \bigl\{ \opn{Del}(\g^p, R)  
\bigr\}_{p \in \mbb{N}}$.

\begin{dfn} \label{dfn:Lie-desc.102}
Let $\g$ be a cosimplicial quasi quantum type DG Lie algebra, and let $R$ be a
parameter algebra, all over the field $\K$. 
A {\em Lie descent datum} in $(\g, R)$ is an element of the set 
$\opn{Desc}(\opn{Del}(\g, R))$;
cf.\ Definition \ref{dfn:101}.

Given 
$\bsym{\de}, \bsym{\de}' \in \opn{Desc}(\opn{Del}(\g, R))$,
a {\em gauge transformation} $\bsym{\delta} \to \bsym{\delta}'$ is 
a gauge transformation of combinatorial descent data, as defined in
Definition \ref{dfn:100}.

Passing to gauge equivalence classes we get the set
$\ol{\opn{Desc}}(\opn{Del}(\g, R))$.
\end{dfn}

Let $\g = \{ \mfrak{g}^{p} \}_{p \in \mbb{N}} $ be a cosimplicial quasi quantum
type DG Lie algebra. In a Lie descent datum 
$\bsym{\de} = (\de^0, \de^1, \de^2) \in \opn{Desc}(\opn{Del}(\g, R))$,
the component $\de^0$ belongs to $\opn{MC}(\m \hot \g^0)$.
Thus there is a function 
$\opn{Desc}(\opn{Del}(\g, R)) \to \opn{MC}(\m \hot \g^0)$.
This function respects gauge equivalence, and we get an induced function 
\begin{equation} \label{eqn:Lie-desc.105}
\ol{\opn{Desc}}(\opn{Del}(\g, R)) \to \ol{\opn{MC}}(\m \hot \g^0) .
\end{equation}

Let $\g = \{ \mfrak{g}^{p} \}_{p \in \mbb{N}}$ and 
$\h = \{ \mfrak{h}^{p} \}_{p \in \mbb{N}}$ 
be cosimplicial  quasi quantum type DG Lie algebras. By {\em cosimplicial 
$\mrm{L}_{\infty}$ morphism} 
$\Psi : \g \to \h$ we mean a collection 
$\Psi = \{ \Psi^{p} \}_{p \in \mbb{N}}$
of $\mrm{L}_{\infty}$ morphisms $\Psi^p : \g^p \to \h^p$, 
such that for every $\al : p \to q$ in $\bsym{\Delta}$ we have 
$\Psi^q \circ \g(\al) = \h(\al) \circ \Psi^p$
in $\cat{DGLie}_{\infty}(\K)$.
This gives us a category $\bsym{\Delta}(\cat{DGLie}_{\infty}(\K))$.
We call such $\Psi$ a {\em cosimplicial $\mrm{L}_{\infty}$ quasi-isomorphism} if
each $\Psi^p$ is an $\mrm{L}_{\infty}$ quasi-isomorphism.

\begin{thm}[Equivalence for Lie Descent]  \label{thm:Lie-desc.101}
Let $\Psi : \g \to \h$ be a cosimplicial $\mrm{L}_{\infty}$ morphism between 
cosimplicial quasi quantum type DG Lie algebras, and let 
$\nu : R \to S$ be a homomorphism between parameter algebras. Then there
is a function 
\[ \ol{\opn{Desc}}(\opn{Del})(\Psi, \nu) : 
\ol{\opn{Desc}}(\opn{Del}(\g, R)) \to \ol{\opn{Desc}}(\opn{Del}(\h, S))  \]
with these properties. 

\begin{enumerate}
\rmitem{i} The function $\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu))$
is functorial in $\Psi$ and $\nu$.

\rmitem{ii}  If $\Psi$ is a morphism in $\cat{DGLie}(\K)$ then 
$\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu) = 
\ol{\opn{Desc}}(\opn{Del}^{}(\Psi, \nu))$,
where  
$\opn{Del}^{}(\Psi, \nu)$ is corresponding the morphism in
$\bsym{\Delta}(\cat{CrGrpd})$.

\rmitem{iii} The diagram 
\[ \UseTips \xymatrix @C=18ex @R=5ex {
\ol{\opn{Desc}}(\opn{Del}(\g, R))
\ar[d]
\ar[r]^(0.5){\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)}
&
\ol{\opn{Desc}}(\opn{Del}(\h, S))
\ar[d]
\\
\ol{\opn{MC}}(\m \hot \g^0)
\ar[r]^(0.5){\ol{\opn{MC}}(\nu \hot \Psi)}
&
\ol{\opn{MC}}(\n \hot \h^0)
} \]
with vertical arrows \tup{(\ref{eqn:Lie-desc.105})}, commutative. 

\rmitem{iv} If $\Psi$ is a cosimplicial $\mrm{L}_{\infty}$ quasi-isomorphism, 
and if $\nu$ is an isomorphism, then 
$\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)$ is bijective.  
\end{enumerate}
\end{thm}

Please note the subtle notational distinction between 
$\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)$ and \lb
$\ol{\opn{Desc}}(\opn{Del}^{}(\Psi, \nu))$.
In general (except in the situation of property (ii)) there is no morphism of
cosimplicial crossed groupoids $\opn{Del}^{}(\Psi, \nu)$, and thus the function 
$\ol{\opn{Desc}}(\opn{Del}^{}(\Psi, \nu))$ is not defined; only the function 
$\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)$ on equivalence classes of descent data
is defined. 

\begin{proof}
Applying the functor $\ol{\opn{Desc}}$ to the second diagram in Theorem 
\ref{thm:400}  we get a diagram (the solid arrows) 
\begin{equation} \label{eqn:405}
\UseTips \xymatrix @C=18ex @R=7ex {
\ol{\opn{Desc}}(\opn{Del}(\til{\g}, R))
\ar[d]
\ar[r]^(0.5){\ol{\opn{Desc}}(\opn{Del}(\til{\Psi}, \nu))}
&
\ol{\opn{Desc}}(\opn{Del}(\til{\h}, S))
\ar[d]
\\
\ol{\opn{Desc}}(\opn{Del}(\g, R))
\ar@{-->}[r]^(0.5){\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)}
&
\ol{\opn{Desc}}(\opn{Del}(\h, S))
} 
\end{equation}
in $\cat{Set}$.
Theorem \ref{thm:100} tells us that the vertical arrows here are bijections.
Hence there is a unique function 
$\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)$ making
this diagram commutative. 
The functoriality of $\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)$
in $\Psi$ is because $\opn{L} \circ \opn{C}$ is a functor; and the
functoriality in $\nu$ is trivial.

If $\Psi$ is in $\cat{DGLie}(\K)$ then we can add the arrow 
$\opn{Del}^{}(\Psi, \nu)$ into the second diagram in Theorem 
\ref{thm:400}, making it commutative. This proves property (ii). 

Since the solid arrows in the diagram (\ref{eqn:405}) 
respect the function (\ref{eqn:Lie-desc.105}), so does the remaining arrow.
This implies property (iii). 

Finally, if $\Psi$ happens to be an $\mrm{L}_{\infty}$
quasi-isomorphism, and $\nu$ is an isomorphism, then according to 
Theorem \ref{thm:400} the morphism of crossed groupoids
$\opn{Del}(\til{\Psi}, \nu)$ is also a weak equivalence.
Hence the functions
$\ol{\opn{Desc}}(\opn{Del}(\til{\g}, R))$
and 
$\ol{\opn{Desc}}(\opn{Del})(\Psi, \nu)$ are bijective.
\end{proof}

\begin{rem}
If we assume that the parameter algebras in question are all artinian, then in
Theorems \ref{thm:400} and \ref{thm:Lie-desc.101} we can
drop the condition that the DG Lie algebras are quasi quantum type. See
\cite[Theorem 6.13]{Ye7}. 
\end{rem}

\begin{rem} \label{rem:Lie-desc.101}
Here is a brief comparison to other work on these matters. 
A special case of Theorem \ref{thm:Lie-desc.101} is 
\cite[Proposition 3.3.1]{BGNT1}, which only deals with cosimplicial DG Lie
quasi-isomorphisms between quantum type DG Lie algebras, and only with artinian
parameter algebras. The methods used in \cite{BGNT1} do not seem to be adequate
for obtaining the result we need. 

Getzler wrote two papers \cite{Ge1, Ge2} on higher Deligne groupoids. 
Suppose $\g$ is quantum type DG Lie algebra, and $R$ is an artinian parameter
algebra. In the first paper Getzler discusses the Deligne $2$-groupoid
$\opn{Del}(\g, R)$, which is denoted there by $\mcal{C}(\m \ot \g)$.  In the
second paper he introduced a simplicial set $\ga_{\bdot}(\m \ot \g)$.
A main result of \cite{Ge2} is that  an $\mrm{L}_{\infty}$ quasi-isomorphism 
$\g \to \h$ induces a homotopy equivalence 
$\ga_{\bdot}(\m \ot \g) \to \ga_{\bdot}(\m \ot \h)$.
Getzler says that the simplicial set $\ga_{\bdot}(\g \ot \m)$ ``generalizes the
Deligne $2$-groupoid'', but this is not proved, nor even explained.
For some time we had hoped to rely on Getzler's results for a quick proof of 
Theorem \ref{thm:Lie-desc.101} (at least for artinian parameter algebras), but
we could not find a satisfactory way to fill the gap mentioned above.
This is why we eventually had to come up with  Theorem \ref{thm:400}. 

Theorem \ref{thm:Lie-desc.101} (for artinian $R$ and $S$) is similar to 
\cite[Theorem 3.5]{CH}. But \cite[Theorem 3.5]{CH} is not actually proved in
that paper (there appear to be holes in the arguments, cf.\ Remark
\ref{rem:cosim.106}). Another possible difficulty is that in \cite{CH} the
authors rely on the unproved part of Getzler's work that we mentioned above. 

Here is a very recent development. The new paper \cite{BGNT3} appears to fill
the gap in \cite{Ge2}
mentioned above. According to \cite[Remark 1.1]{BGNT3}, their work implies that
the simplicial set $\ga_{\bdot}(\m \ot \g)$ equals the $2$-nerve of the 
Deligne crossed groupoid $\opn{Del}(\g, R)$~!
\end{rem}
