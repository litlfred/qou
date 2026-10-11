---
doc_id: arxiv-math-9805116v3
doc_title: "arXiv:math/9805116v3 [math.QA] 8 Jun 1999"
section_id: sec-002-13-weak-hopf-algebras
section_title: "Weak Hopf algebras"
section_number: 1.3
pages: 9-14
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.985
latex_coverage_ratio: 0.994
---
In this Subsection we
will show how the existence of an antipode relates $\PL$, $A^L$
with $\PR$, $A^R$ and derive the expected properties
of $S$ that have been axioms in earlier formulations.
The two most important results will be invertibility of the
antipode and separability of the algebras $A^L$ and $A^R$.
Let us start with the question of uniqueness of the antipode.
\begin{lem} \label{lem: uniq S}
The unit, the counit, and the antipode, if exist, are unique. I.e.
if \break
$(A,\mu,u,\cop,\eps,S)$ and $(A,\mu,u',\cop,\eps',S')$ are both
weak Hopf algebras then $u'=u$, $\eps'=\eps$,\break and $S'=S$.
\end{lem}
\Proof The uniqueness of the unit and the counit are obvious.
Therefore $\PL$ and $\PR$ are common in these two WHA-s. In order
to prove $S'=S$ introduce the convolution product
\beq
(f\diamond g)(x)\ :=\ f(x\c)g(x\cc)\ ,\qquad x\in A
\eeq
on functions $f,g\in\Hom_K(A,A)$. This is an associative operation
in terms of which the antipode axioms take the form
\[\id\diamond S=\PL,\qquad S\diamond\id\diamond S=S,\qquad
  S\diamond\id=\PR\ .\]
Now $S'$ satisfies the same equations with the same $\PL,\PR$,
therefore
\[
S'=S'\diamond\id\diamond S'=S'\diamond\PL=S'\diamond\id\diamond S
  =\PR\diamond S=S\diamond\id\diamond S=S\ .\]
\qed
 
As a preparation for the Theorem below notice that the
definitions (\ref{Pi}) have counterparts involving the antipode:
\begin{lrarray}
\PL(x)=\eps(S(x)\1\c)\1\cc\eql &
\PR(x)=\1\c\eps(\1\cc S(x))\eqr\label{18}
\end{lrarray}
As a matter of fact
\beanon
\PL(x)&=&\eps(\1\c\PL(x))\1\cc=\eps(\PL(x)\1\c)\1\cc=
       \eps(x\c S(x\cc)\1\c)\1\cc=\\
      &=&\eps(\PR(x\c)S(x\cc)\1\c)\1\cc=\eps(S(x\c)x\cc S(x\ccc)
        \1\c)\1\cc=\\
      &=&\eps(S(x)\1\c)\1\cc
\eeanon
where in the subsequent equations (\ref{Pi}), (\ref{LR=RL}),
(A.8a), (\ref{5}b), (A.8b), and finally (A.9) have been used.
Eqn(2.23b) can be proven analogously. As the duals of
(2.23a-b) we have automatically the identities
\begin{lrarray}
\PL(x)=S(\1\c)\eps(\1\cc x)\eql&
\PR(x)=\eps(x\1\c)S(\1\cc).\eqr \label{19}
\end{lrarray}
\begin{lem}
In a WHA $A$ the following identities hold:
\beabc
\PL\circ S\ =&\PL\circ\PR&=\ S\circ\PR\label{20a}\\
\PR\circ S\ =&\PR\circ\PL&=\ S\circ\PL\label{20b}
\eeabc
\end{lem}
\Proof It is sufficient to prove the first equalities in
(\ref{20a}) and (\ref{20b}) because the second ones then follow by
duality.
\beanon
\PL\circ S(x)&=&\eps(\1\c S(x))\1\cc=\eps(\1\c S(x\c)x\cc
               S(x\ccc))\1\cc=\\
             &=&\eps(\1\c S(x\c)\PL(x\cc))\1\cc=\eps(\1\c S(x\c)
               x\cc)\1\cc\\
             &=&\PL\circ\PR(x).
\eeanon
In a similar way one can verify $\PR\circ S=\PR\circ\PL$.\qed
 
The above Lemma implies that $S(A^R)\subset A^L$ and
$S(A^L)\subset A^R$. On the other hand Eqns(2.24a-b) say that
$A^L\subset S(A^R)$ and $A^R\subset S(A^L)$. Therefore the
antipode maps $A^L$ onto $A^R$ bijectively and maps $A^R$ onto
$A^L$ bijectively.
 
\begin{thm}   \label{thm: S}
Let $A$ be a WHA. Then the antipode is antimultiplicative and anti
comultiplicative,
\bea
S(xy)&=&S(y)S(x)\qquad\qquad x,y\in A\ ,\label{21}\\
S(x)\c\o S(x)\cc&=&S(x\cc)\o S(x\c)\qquad\qquad x\in A\
                                                   ,\label{22}
\eea
and the restrictions $S|_{A^L}$ and $S|_{A^R}$ are bijections such
that
\beq
S(A^L)\ =\ A^R\ ,\qquad\qquad S(A^R)\ =\ A^L\ .      \label{23}
\eeq
The unit and the counit are $S$-invariant,
\begin{lrarray}
S(\1)\ =\ \1\ ,\eql&
\eps\circ S\ =\ \eps\ .\eqr\label{24}
\end{lrarray}
Furthermore $S\colon A\to A$ is invertible.
\end{thm}
\Proof We have already shown (\ref{23}). (\ref{22}) is the dual of
(\ref{21}) and (2.29a) is the dual of (2.29b).
\beanon
S(xy)&=&S(x\c y\c)x\cc y\cc S(x\ccc y\ccc)=S(x\c y\c)
                   \PL(x\cc\PL(y\cc))=\\
&=&S(x\c y\c)x\cc\PL(y\cc)S(x\ccc)=\PR(\PR(x\c)
                    y\c)S(y\cc)S(x\cc)=\\
&=&S(y\c)\PR(x\c)y\cc S(y\ccc)S(x\ccc)=S(y\c)y\cc S(y\ccc)
                    S(x\c)x\cc S(x\ccc)=\\
&=&S(y)S(x)\ .
\eeanon
Next we prove (2.29b).
\beanon
\eps(S(x))&=&\eps(S(x\c)x\cc S(x\ccc))=\eps(S(x\c)\PL(x\cc))=
            \eps(S(x\c)x\cc)=\eps(\PR(x))=\\
          &=&\eps(x)\ .
\eeanon
In order to prove invertibility of $S$ notice that the descending
chain $A\supset S(A)\supset S^2(A)\supset\dots$ of WHAs all
contain $\1$ by (2.29a). This implies the existence
of $n\in\N$ such that
\[
\1\ \in\ S^{n+1}(A)\ =\ S^n(A)\ \subset\ S^{n-1}(A)\ .
\]
We want to show that this implies $S^n(A)=S^{n-1}(A)$.
Replacing $A$ by $S^{n-1}(A)$ it is
therefore enough to prove invertibility of $S$
under the additional assumption $S^2(A)=S(A)$, implying
\[
\Ker S\ \cap\ S(A)\ =\ 0\ .
\]
In this case let $\bar S:=S|_{S(A)}$, then $\bar S\colon S(A)\to
S(A)$ is bijective and
\[
P_S\ :=\ {\bar S}^{-1}\circ S\ \colon\ A\to S(A)
\]
is a multiplicative idempotent satisfying
\[
P_S(xS(y))\ =\ P_S(x)S(y)\,,\qquad x,y\in A\ .
\]
By (\ref{23}) $A^{L,R}\subset S(A)$.
Now taking into account the identity $x=x_{(1)}
S(x_{(2)})x_{(3)}$,
which follows directly from axioms (A.8a) and (A.4), then
using also $P_S(\1)=\1$ we have
\beanon
P_S(x)&=&P_S( x_{(1)} S(x_{(2)})x_{(3)})=P_S(x_{(1)})
S(x_{(2)})x_{(3)}= P_S(x_{(1)} S(x_{(2)}))x_{(3)}=\\
&=&P_S(\1)x_{(1)} S(x_{(2)})x_{(3)}=x,
\eeanon
so $\Ker P_S=\Ker S=0$.\qed
 
We are now able to derive (versions of) the original antipode
axioms of \cite{BSz,Sz}:
\beabc
x\c\o x\cc S(x\ccc)&=&\1\c x\o\1\cc\\
S(x\c)x\cc\o x\ccc&=&\1\c\o x\1\cc  \label{eq: 2.29b}\\
x\c\o S(x\cc)x\ccc&=&x\1\c\o S(\1\cc)\\
x\c S(x\cc)\o x\ccc&=&S(\1\c)\o\1\cc x
\eeabc
The first two are just rewritings of the bialgebra identities
(\ref{13a}-b). The second two are more delicate.
\beanon
x\c\o S(x\cc)x\ccc&=&x\c\o\eps(x\cc\1\c)S(\1\cc)
                   =x\c\1\cp\o\eps(x\cc\1\ccp\1\c)S(\1\cc)=\\
                  &=&x\c\1\c\eps(x\cc\1\cc)\o S(\1\ccc)
                   =x\1\c\o S(\1\cc)\\
x\c S(x\cc)\o x\ccc&=&S(\1\c)\eps(\1\cc x\c)\o x\cc
                    =S(\1\c)\eps(\1\cc\1\cp x\c)\o \1\ccp x\cc=\\
                   &=&S(\1\c)\o\eps(\1\cc x\c)\1\ccc x\cc
                    =S(\1\c)\o\1\cc x
\eeanon
The following Proposition also holds, if $A$ is just a WBA, see
\cite{WBA}.
 
\begin{prop} \label{pro:sepa}
Let $A$ be a WHA over $K$. Then $A^L$ and $A^R$ are separable
$K$-algebras, in particular, they are semisimple.
\end{prop}
\Proof Recall that an algebra $A$ is separable if and
only if there exists a $q\in A\o A$ such that $(x\o\1)q=q(\1\o x)$
holds for all $x\in A$ and furthermore $\mu(q)=\1$, where $\mu$
denotes the multiplication map of $A$ \cite{Pierce} . Such a $q$ will be
called
a {\em separable idempotent}\footnote{In fact $q$ is an idempotent
only if considered as an element of $A\o A^{op}$.}. So, our proof
will consist of showing that $q^L=S(\1\c)\o\1\cc\in A^L\o
A^L$ and $q^R=\1\c\o S(\1\cc)\in A^R\o A^R$ are separable
idempotents of $A^L$ and $A^R$, respectively. In fact we will
prove the somewhat more general identities
\beabc \label{separ}
x\c y^R\o x\cc&=&x\c\o x\cc S(y^R)\\
x\c\o y^L x\cc&=&S(y^L)x\c\o x\cc
\eeabc
valid for all $x\in A$ and $y^L\in A^L$, $y^R\in A^R$.
Pairing the LHS of (\ref{separ}) with $\varphi\o\psi$, we obtain
\beanon
\bra\varphi\o\psi,LHS\ket&=&\bra\varphi(y^R\la\du1),x\c\ket
\bra\psi,x\cc\ket=\bra\varphi,x\c\ket\bra(S(y^R)\la\du1)\psi,x\cc\ket=\\
&=&\bra\varphi\o\psi,RHS\ket\ .
\eeanon
The proof of (2.31b) is simply the mirror image of the
above argument. \qed
 
 
 

\subsection{The "trivial" representation}
 
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
