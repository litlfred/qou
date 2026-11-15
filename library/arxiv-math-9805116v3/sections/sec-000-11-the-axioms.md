---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-000-11-the-axioms
section_title: "The axioms"
section_number: 1.1
pages: 4-6
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.994
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
\begin{defi}
A {\em weak bialgebra} (WBA) is a quintuple
$(A,\mu,u,\cop,\eps)$ satisfying Axioms 1, 2, and 3 below.
If $(A,\mu,u,\cop,\eps,S)$ satisfies Axioms 1, 2, 3, and 4 below
it is called a {\em weak Hopf algebra} (WHA).
\end{defi}
\begin{description}
\item [\bf Axiom 1.] $A$ is a finite dimensional associative
algebra over a field $K$ with multiplication
$\mu\colon A\o A\to A$ and unit $u\colon K\to A$. I.e. $\mu$ and
$u$ are $K$-linear and satisfy
\begin{description}
\item[\sf Associativity:] $\quad\mu\circ(\mu\o\id)=
                           \mu\circ(\id\o\mu)\quad$\hfill$(A.1)$
\item[\sf Unit property:] $\quad\mu\circ(u\o\id)=\id=
                           \mu\circ(\id\o u)\quad$\hfill$(A.2)$
\end{description}
(Later on we will suppress $\mu$ and $u$, just write $xy$ for
$\mu(x,y)$ and use the {\em unit element} $\1:=u(1)$ instead of
$u$.)
\item[\bf Axiom 2.] $A$ is a
coalgebra over $K$ with {\em comultiplication}
$\cop\colon A\to A\o A$ and {\em counit}
$\eps\colon A\to K$. I.e. $\cop$ and $\eps$ are $K$-linear and
satisfy
\begin{description}
\item[\sf Coassociativity:]
$\qquad(\Delta\o\id)\circ\Delta\ =\ (\id\o\Delta)\circ\Delta$
\hfill$(A.3)$
\item[\sf Counit property:]
$\qquad(\varepsilon\o\id)\circ\Delta\ =\ \id\
           =\ (\id\o\varepsilon)\circ\Delta$ \hfill$(A.4)$
\end{description}
\item[\bf Axiom 3.] For compatibility of the algebra and coalgebra
structures we assume
\begin{description}
\item[\sf Multiplicativity of the coproduct:] For all $x,y\in A$
 
\smallskip
$\Delta(xy)\ =\ \Delta(x)\Delta(y)$\hfill $(A.5)$
 
\smallskip
\item[\sf Weak multiplicativity of the counit:] For all $x,y,z\in
A$
 
\smallskip
$\eps(xyz)=\eps(xy\c)\eps(y\cc z)$\hfill$(A.6a)$
 
$\eps(xyz)=\eps(xy\cc)\eps(y\c z)$\hfill$(A.6b)$
 
\smallskip
\item[\sf Weak comultiplicativity of the unit:]\hfill
 
\smallskip
$\cop^2(\1)=(\cop(\1)\o\1)(\1\o\cop(1))$\hfill$(A.7a)$
 
$\cop^2(\1)=(\1\o\cop(1))(\cop(\1)\o\1)$\hfill$(A.7b)$
 
\smallskip
\end{description}
\item[Axiom 4.] There exists a $K$-linear map $S\colon A\to A$,
called the {\em antipode}, satisfying the following
\begin{description}
\item[\sf Antipode axioms:] For all $x\in A$
 
\smallskip
$x\c S(x\cc)=\eps(\1\c x)\1\cc$\hfill$(A.8a)$
 
$S(x\c)x\cc=\1\c\eps(x\1\cc)$\hfill$(A.8b)$
 
$S(x\c)x\cc S(x\ccc)=S(x)$\hfill$(A.9)$
 
\smallskip
\end{description}
\end{description}
In eqs. (A.6-9) we used a standard suffix notation for (iterated) coproducts,
omitting as usual summation indices and a summation symbol.
 
In the terminology of \cite{WBA} $(A,\mu,u,\Delta,\varepsilon)$ is called
a {\em weak bialgebra} if it satisfies the Axioms (A.1-5). There a weak
bialgebra is called {\em monoidal} if it satisfies (A.6) and it is called
{\em comonoidal} if it satisfies (A.7). As has been explored in detail in
\cite{WBA}, these (co)monoidality axioms are precisely designed to render
the category of $A$-modules (the category of $A$-comodules, respectively)
monoidal.
 
The {\em dual} of a weak bialgebra (weak Hopf algebra) $A$ is the
dual space $\duA:=\Hom_K(A,K)$ equipped with structure maps
$\hat\mu,\hat u,\ducop,\dueps\ (,\duS)$ defined by transposing
the structure maps of $A$ by means of the canonical pairing $\bra\
,\ \ket\colon\duA\times A\to K$ :
\beanon
\bra\varphi\psi,x\ket&:=&\bra\varphi\o\psi,\cop(x)\ket\\
\bra\du1,x\ket&:=&\eps(x)\\
\bra\ducop(\varphi),x\o y\ket&:=&\bra\varphi,xy\ket\\
\dueps(\varphi)&:=&\bra\varphi,\1\ket\\
\bra\duS(\varphi),x\ket&:=&\bra\varphi,S(x)\ket
\eeanon
where $\varphi,\psi\in\duA$ and $x,y\in A$.
 
Let $f$ and $g$ be maps from the $m$-fold tensor product $A^{\o
m}$ to the $n$-fold tensor product $A^{\o n}$ such that they are
composites of tensor products of the structure maps
$\mu,u,\cop,\eps,S$ and of the twist maps $\tau_{ij}$
interchanging the $i$-th and the $j$-th $A$ factors. Then the
equality $f=g$ is called an {\em $A$-statement}. Similarly one
defines the {\em $\duA$-statements}. Now every $A$-statement $Q\
::\ f=g$ determines an equivalent $\duA$-statement $Q^T\ ::\
f^T=g^T$ obtained by reversing the order of composition and
replacing $\mu$ with $\ducop$, $u$ with $\dueps$, $\cop$ with
$\hat\mu$, $\eps$ with $\hat u$, and $S$ with $\duS$. The
statement $Q^T$ is called the {\em transpose} of $Q$.If we now
substitute $\mu,u,\cop,\eps,S$, respectively in place of
$\hat\mu,\hat u,\ducop,\dueps,\duS$ in the statement $Q^T$ we
obtain a new $A$-statement $Q^\sim\ ::\ f^\sim=g^\sim$
which is not equivalent to $Q$ in general. This $Q^\sim$ will
be called the {\em dual} of $Q$. For example one can easily verify
that the WBA axioms satisfy $(A.1)^\sim=(A.3)$, $(A.2)^\sim
=(A.4)$, $(A.5)^\sim=(A.5)$, $(A.6a)^\sim=(A.7a)$, and
$(A.6b)^\sim=(A.7b)$. Thus the weak bialgebra
axioms form a selfdual set of statements. This implies that the
dual of a WBA is a WBA, too. The same holds for weak Hopf
algebras, since each one of the antipode axioms is a selfdual
statement. As a consequence of selfduality if $Q$ is a true
statement in a WBA or in a WHA then $Q^\sim$ is also true there. This
principle extends also to statements involving both $A$ and $\duA$
structure maps and canonical pairing(s).
 
As has been proven in \cite{WBA},
the above selfdual set of WHA axioms are equivalent
to the non-selfdual set of axioms given in \cite{Sz}.
In this work we will gradually reproduce all
axioms of \cite{Sz} as a consequence of the present ones.
 
For a weak Hopf algebra $(A,\1,\cop,\eps,S)$ the following
conditions are equivalent
\begin{itemize}
\item $A$ is a Hopf algebra;
\item $\cop(\1)=\1\o\1$\ ;
\item $\eps(xy)=\eps(x)\eps(y)$\ ;
\item $S(x\c)x\cc=\1\eps(x)$\ ;
\item $x\c S(x\cc)=\1\eps(x)$\ .
\end{itemize}
The proof of these assertions are either trivial or will become
trivial after acquainting the weak Hopf calculus developed in the
next subsections, see also \cite{WBA}.
