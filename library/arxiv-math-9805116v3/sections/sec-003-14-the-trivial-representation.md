---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-003-14-the-trivial-representation
section_title: "The 'trivial' representation"
section_number: 1.4
pages: 12-14
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.991
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Since the counit of a WHA is in general not an algebra map, weak
Hopf algebras may be lacking of any 1-dimensional representation.
Nevertheless the axioms ensure that any WHA $A$ has a
distinguished representation providing a unit object for the
(relaxed) monoidal category of left $A$-modules. We shall discuss
this category in detail in \cite{BNSzII}. Now we concentrate
only on the properties of this representation. We remark that the
trivial representation exists already in WBA's \cite{WBA} and
therefore the use of the antipode in this subsection is not
obligatory.
 
Since the algebras $A^{L/R}$ occur on the right hand side of
Axioms (A.8a-b) where in ordinary Hopf algebras the trivial
representation stands, one expects that the "trivial
representation" of WHAs must be a non-trivial representation
acting on either one of the algebras $A^{L/R}$ or $\duA^{L/R}$.
 
\begin{lem}                     \label{lem: trivials}
The following left $A$-modules are isomorphic.
$$\begin{array}{rccl}
_A\duA^R\ ::\ &\mbox{the vector space }\duA^R&\mbox{with action }&
               x\cdot\varphi^R:=x\la\varphi^R\\
_A\duA^L\ ::\ &\mbox{the vector space }\duA^L&\mbox{with action }&
               x\cdot\varphi^L:=\varphi^L\ra S(x)\\
_AA^L\ ::\ &\mbox{the vector space }A^L&\mbox{with action }&
               x\cdot y^L:=\PL(xy^L)\\
_AA^R\ ::\ &\mbox{the vector space }A^R&\mbox{with action }&
               x\cdot y^R:=\PR(y^RS(x))
\end{array}$$
\end{lem}
\Proof $\duS\colon\duA^L\to \duA^R$ is an isomorphism of vector
spaces and $\duS(\varphi\ra S(x))=x\la\duS(\varphi)$ is a general
WHA identity. This proves the isomorphism of the first two
$A$-modules. Similarly, $S\colon A^L\to A^R$ is an isomorphism
of vector spaces and $S(\PL(xy))=\PR(S(y)S(x))$ is a WHA identity.
This proves the isomorphism of the last two $A$-modules.
 
In order to show the isomorphism of $_A\duA^R$ with $_AA^L$
consider the bijection $B\colon\duA^R\to A^L$,
$B(\varphi^R):=\1\ra\varphi^R$. Then
\beanon
B(x\la\varphi^R)&=&\1\ra(x\la\varphi^R)=\bra\1\c
x,\varphi^R\ket\1\cc=\\
&=&\bra\1\c(x\ra\varphi^R),\du1\ket\1\cc=\PL(x\ra\varphi^R)=
   \PL(x(\1\ra\varphi^R))=\\
&=&\PL(xB(\varphi^R))
\eeanon
hence $B$ is a left $A$-module map. Here, in the last-but-one
equality we have used one of the four arrow identities
of Scholium \ref{sch: arrow}.\qed
\begin{defi}                         \label{def: triv}
By the trivial representation of the WHA $A$ we mean the cyclic
left $A$-module $\V:=\,_A\duA^R$ with $A$-action $\triv\colon A\to
\End_K \duA^R$, $\triv(x)\varphi:=x\la\varphi$.
\end{defi}
The third and fourth $A$-modules of the above Lemma
demonstrate that the restriction of the trivial representation to
$A^L$ ($A^R$) is equivalent to its left regular representation,
hence faithful. This is one of the instances where $A^{L/R}$
appears in the role of a ground "field".
 
Later we will need the following strengthening of Lemma
\ref{kappa}.
\begin{lem}  \label{Z}
Let $A$ be a WHA and introduce the notation $Z^L:=A^L\cap\Center
A$, $Z^R:=A^R\cap\Center A$, and $Z:=A^L\cap A^R$. Then the
isomorphism (of algebras) $\kappa_A^L\colon A^L\to\duA^R$
restricts to an isomorphism $Z^L\to\duZ$ and the isomorphism
$\kappa_A^R\colon A^R\to\duA^L$ restricts to the isomorphism
$Z^R\to\duZ$. Therefore
\beanon
Z^L\la\du1\ =&\duZ&=\ \du1\ra Z^R\\
Z\la\du1=\duZ^R\,,&\ \ &\duZ^L=\du1\ra Z\ .
\eeanon
The two isomorphisms have a common restriction to the {\em
hypercenter} $\Hypercenter A:=Z^L\cap Z^R$ and yields an
isomorphism $\Hypercenter A\to\Hypercenter \duA$.
\end{lem}
\Proof Notice that for $c\in\Center A$ $\du1\ra c=c\la\du1$.
Therefore $x^L\in Z^L\Rightarrow x^L\la\du1=\du1\ra x^L\in \duZ$.
This proves $\kappa_A^L(Z^L)\subset\duZ$.
 
If $z\in Z$ then $(z\la\du1)\varphi=z\la\varphi$
by (\ref{44-45}) and $z\la\varphi=\varphi(z\la\du1)$ by
(2.21b). Hence $z\la\du1$ is central. This proves
$\kappa_A^L(Z)\subset\duZ^R$.
 
Since $(\kappa_A^L)^{-1}=\kappa_{\duA}^R$, the analogue inclusions
$\kappa_A^R(Z^R)\subset \duZ$ and $\kappa_A^R(Z)\subset \duZ^L$
complete the proof.\qed
 
The unusual feature of the trivial representation of WHA-s is that
it can be decomposable. But this can occur only if the left and
right
subalgebras of the dual have non-trivial intersection as the next
Proposition claims.
 
\begin{prop} \label{prop: End trivi}
Let $A$ be a WHA, let $(\V,\triv)$ be its trivial
representation as in Definition \ref{def: triv}. Then
\beq
\End\V\ =\ \triv(Z^L)\ =\ \triv(Z^R)\ ,
\eeq
where $\End\V$ denotes the algebra of $A$-module endomorphisms
of $\V$.
\end{prop}
\Proof Let $T\in\End\V$ then $T(x\la\du1)=x\la T(\du1)$, for $x\in
A$, in particular
\beanon
T(x^L\la\du1)&=& x^L\la T(\du1)\ =\ (x^L\la\du1)T(\du1)\\
T(x^L\la\du1)&=& T(S^{-1}(x^L)\la\du1)=S^{-1}(x^L)\la T(\du1)\ =\
               T(\du1)(x^L\la\du1)
\eeanon
where we have made use of Eqns (\ref{44-45}) and (2.21b).
Since by Lemma \ref{kappa} $A^L\la\du1=\duA^R$,
$\zeta:=T(\du1)\in\Center\duA^R$ and $T(\varphi^R)=\varphi\zeta$.
Thus $x\la\zeta=T(x\la\du1)=(x\la\du1)\zeta$ holds for all $x\in
A$. It follows that
$$
\bra\duPL(\zeta),x\ket=\bra\zeta,\1\ra(x\la\du1)\ket=
\bra(x\la\du1)\zeta,\1\ket=\bra x\la\zeta,\1\ket=\bra\zeta,x\ket\
, $$
i.e. $\zeta\in\duA^L\cap\duA^R\equiv \duZ$. Now by Lemma \ref{Z}
there exists a $z^L\in Z^L$ such that $\zeta=z^L\la\du1$. We can
conclude that
$$
T(\varphi^R)=\zeta\varphi^R=(z^L\la\du1)\varphi^R=z^L\la\varphi^R=
             \triv(z^L)\varphi^R\ ,
$$
i.e. $T=\triv(z^L)$. This proves $\End\V\subset\triv(Z^L)$.
The opposite inclusion is trivial since $\triv(Z^L)\subset
\Center(\triv(A))$. This finishes the proof of
$\End\V=\triv(Z^L)$.
 
Showing the other statement $\End\V=\triv(Z^R)$ one proceeds as
above but chooses a $z^R\in Z^R$ such that $\zeta=\du1\ra z^R$.
Then
\beanon
T(\varphi^R)&=&\varphi^R(\du1\ra z^R)=\varphi^R(z^R\la\du1)=
             z^R\la\varphi^R=\\
            &=&\triv(z^R)\varphi^R
\eeanon
completes the proof.\qed
 
Notice that the above Proposition does not imply that the trivial
$A$-module is semisimple. It does imply, however, that $\V$ has a
decomposition $\V\cong\oplus_{\nu}\,V_\nu$ into indecomposable
$A$-modules in which the indecomposables are disjoint, i.e.
$\Hom(V_\mu,V_\nu)=0$ for all $\mu\neq\nu$.
 
\begin{defi}
If $Z^L=K\1$, or equivalently, if the trivial representation is
indecomposable then the WHA is called {\em pure}.
\end{defi}
The name "pure" comes from the $C^*$-setting when the trivial
representation arises from the positive linear functional $\eps$
by the GNS construction. Thus $A$ is pure iff $\eps$ is pure.
 
Nota bene pureness is not a selfdual notion, duals of pure WHA-s
may not be pure. Clearly, $A$ is pure iff $Z^L\cong Z^R$ is
trivial but $\duA$ is pure iff $Z$ is trivial.
 
 
 
 
\sec{Weak Hopf Modules and Integral Theory}
 
As in Hopf algebras so in weak Hopf algebras the integrals play
a decisive role in the structure analysis of these algebras.
Using integrals we can formulate conditions for the algebra to be
Frobenius, symmetric, or semisimple, and study questions related
to innerness of $S^2$ or $S^4$. Furthermore we will be able to
characterize those WHAs that have Haar measures. In deriving the
basic properties of integrals the weak generalization of the
the Fundamental Theorem of Hopf modules is very useful. Unfortunately,
it seems to be less powerful than in Hopf algebra theory
(cf. \cite{Montgomery}) where
it implies the existence of non-degenerate integrals. It is an
open problem yet whether all WHAs are Frobenius algebras. We can
prove, however, that all of them are quasi-Frobenius algebras.
