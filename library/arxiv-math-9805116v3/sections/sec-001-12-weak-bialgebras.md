---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-001-12-weak-bialgebras
section_title: "Weak bialgebras"
section_number: 1.2
pages: 6-9
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.952
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
In a WBA define the maps $\PL,\PR\colon A\to A$ by the formulae
\beq                              \label{Pi}
\PL(x):=\eps(\1\c x)\1\cc\ ,\qquad
\PR(x):=\1\c\eps(x\1\cc)
\eeq
and introduce the notation $A^L:=\PL(A)$, $A^R:=\PR(A)$ for their
images. The analogue objects in the dual bialgebra $\duA$ will be
denoted by $\duPL,\duPR,\duA^L,$ and $\duA^R$, respectively.
 
Substituting $y=\1$ in Axiom (A.6b) one obtains
immediately the identities
\begin{lrarray}
\eps(x\PL(y))=\eps(xy)\eql&
\eps(\PR(x)y)=\eps(xy)\eqr\label{5}\\
\PL\circ\PL=\PL\eql&\PR\circ\PR=\PR\eqr\label{6}
\end{lrarray}
As a first application of the duality principle
take\footnote{In taking the transpose of a statement with
$\PLR$ use the fact that in a WBA\hfill\break
$\bra\varphi,\PL(x)\ket=\bra\du1\c\o\du1\cc,\1\c\o
x\ket\bra\varphi,\1\cc\ket=\bra\duPL(\varphi),x\ket$ and similarly
$\bra\varphi,\PR(x)\ket=\bra\duPR(\varphi),x\ket$.}
the duals of Eqns(\ref{5}a-b),
\[\1\c\o\PL(\1\cc)\ =\ \1\c\o\1\cc\ =\ \PR(\1\c)\o\1\cc\ .\]
Then these are identities in any WBA. It follows that
\beq
\cop(\1)\ \in\ A^R\ \o\ A^L\ .              \label{9}
\eeq
\begin{lem}
The counit defines a non-degenerate bilinear form
$$x^L\in A^L, y^R\in A^R\ \mapsto\ \eps(y^Rx^L)\in K\ .$$
Hence $A^L\cong A^R$ as $K$-spaces.
\end{lem}
\Proof
\beanon
\eps(y^Rx^L)=0\ \forall y^R\in A^R &\Longrightarrow&
x^L=\eps(\1\c x^L)\1\cc=0\\
\eps(y^Rx^L)=0\ \forall x^L\in A^L &\Longrightarrow&
y^R=\1\c\eps(y^R\1\cc)=0
\eeanon
where we used (\ref{9}).\qed
 
Returning to Eqns(\ref{5}a-b) and substituting them into the
definitions (\ref{Pi}) one obtains
\begin{lrarray}
\PL(x\PL(y))=\PL(xy)\eql&
\PR(\PR(x)y)=\PR(xy)\eqr\label{10}
\end{lrarray}
The duals of (2.5a-b),
\begin{lrarray}
\cop(A^L)\subset A\o A^L\eql&
\cop(A^R)\subset A^R\o A\eqr\label{11}
\end{lrarray}
tell us that $A^L$ and $A^R$ are left, respectively right coideals
in the coalgebra $A$. Using Axiom (A.7b) we can obtain explicit
expressions for these coproducts
\beabc
\cop(x^L)&=\eps(\1\c x^L)\1\cc\o\1\ccc=\eps(\1\cp x^L)\1\c\1\ccp
\o\1\cc=&\1\c x^L\o\1\cc\label{12a}\\
\cop(x^R)&=\1\c\o\1\cc\eps(x^R\1\ccc)=\1\c\o\1\cp\1\cc\eps(x^R\1\ccp)
       =&\1\c\o x^R\1\cc\label{12b}
\eeabc
where $x^L$ and $x^R$ are meant to denote arbitrary elements of
$A^L$, resp. $A^R$.
 
\begin{lem}
For all $x\in A$ we have the identities
\beabc
x\c\o\PL(x\cc)&=&\1\c x\o\1\cc\label{13a}\\
\PR(x\c)\o x\cc&=&\1\c\o x\1\cc\label{13b}
\eeabc
\end{lem}
\Proof Using Axiom (A.7b) one obtains
\beanon
x\c\o\eps(\1\c x\cc)\1\cc&=&\1\cp x\c\eps(\1\c\1\ccp x\cc)\o\1\cc
   =\1\c x\c\eps(\1\cc x\cc)\o\1\ccc=\\
   &=&\1\c x\o\1\cc\\
\1\c\eps(x\c\1\cc)\o x\cc&=&\1\c\o\eps(x\c\1\cp\1\cc)x\cc\1\ccp
   =\1\c\o\eps(x\c\1\cc)x\cc\1\ccc=\\
   &=&\1\c\o x\1\cc
\eeanon
\qed
 
As a consequence we obtain the dual statements
\begin{lrarray}
x\PL(y)=\eps(x\c y)x\cc\eql&
\PR(x)y=y\c\eps(x y\cc)\ .\eqr\label{14}
\end{lrarray}
 
\begin{prop}
Let $A$ be a WBA. Then $A^L$ and $A^R$ are subalgebras of $A$
containing $\1$ and
\beq                       \label{LR=RL}
x^Ly^R\ =\ y^Rx^L\qquad\mbox{for all }x^L\in A^L\ \mbox{and }
           y^R\in A^R\ .
\eeq
\end{prop}
\Proof Eqns(\ref{13a}-b) imply the relations
\beabc
\1\c\1\cp\o\1\cc\o\1\ccp&=&\1\c\o\PL(\1\cc)\o\1\ccc\label{15a}\\
\1\c\o\1\cp\o\1\cc\1\ccp&=&\1\c\o\PR(\1\cc)\o\1\ccc\label{15b}
\eeabc
Now either Axiom (A.7a) or (A.7b) show that on the RHS of
(\ref{15a}) the first tensor factor belongs to $A^R$ and on the
RHS of (\ref{15b}) the last factor belongs to $A^L$. This is
sufficient for $A^R$, respectively $A^L$ to be closed under
multiplication. Hence they are algebras. Obviously $\1\in A^L\cap
A^R$ since $\PL(\1)=\1=\PR(\1)$. In order to see commutativity of
left and right elements just compare Axioms (A.7a) and (A.7b).
\qed
 
As the duals of the statements that $A^L$ and $A^R$ are
subalgebras we obtain that $\Ker\PL$ and $\Ker\PR$ are coideals of
the coalgebra $A$, i.e.
\bea
\cop(\Ker\sqcap^C)&\subset& A\o\Ker\sqcap^C\ +\ \Ker\sqcap^C\o A\
,\\
\eps(\Ker\sqcap^C)&=&0\ ,\qquad\qquad C=L,R\ .\nonumber
\eea
On the other hand, being the annihilator of the left coideal
$\duA^L$, $\Ker\PL$ is a left ideal of the algebra $A$ and
similarly, $\Ker\PR$ is a right ideal.
\begin{lem}
Consider $A^L$ and $A$ as left $A^L$-modules by left
multiplication. Then $\PL\colon$ $A\to A^L$ is a left $A^L$-module
map. Analogously, $\PR\colon A\to A^R$ is a right $A^R$-module
map. That is to say
\beabc
\PL(\PL(x)y)&=&\PL(x)\PL(y)\label{17a}\\
\PR(x\PR(y))&=&\PR(x)\PR(y)\label{17b}
\eeabc
hold true for all $x,y\in A$.
\end{lem}
\Proof At first use the definition of $\PLR$, then
Eqn(\ref{5}a-b), and finally Eqn(\ref{12a}-b):
\beanon
\PL(\PL(x)y)&=\eps(\1\c\PL(x)y)\1\cc=\eps(\1\c\PL(x)\PL(y))\1\cc
             =&\PL(x)\PL(y)\\
\PR(x\PR(y))&=\1\c\eps(x\PR(y)\1\cc)=\1\c\eps(\PR(x)\PR(y)\1\cc)
             =&\PR(x)\PR(y)
\eeanon
\qed
 
Our next assertion about WBA-s establishes a canonical
isomorphism between the left (right) subalgebra of $A$ and the
right (left) subalgebra of $\duA$. Since the existence of a common
non-trivial subalgebra of $A$ and $\duA$ for Hopf algebras is by
far not typical, this result is the first hint towards the
fundamental role $A^L$ and $A^R$ will play in the theory of WHAs.
 
In order to formulate the statement we introduce the Sweedler
arrow notation
\beq                                            \label{Sw arrow}
x\la\varphi:=\varphi\c\bra\varphi\cc,x\ket\ ,\qquad
  \varphi\ra x:=\bra\varphi\c,x\ket\varphi\cc\ .
\eeq
Since $A$ is the dual WBA of $\duA$, the Sweedler arrows
$\varphi\la x$ and $x\ra\varphi$ are also defined.
\begin{lem} \label{kappa}
The map $\kappa_A^L\colon x^L\mapsto (x^L\la\du1)$ is an algebra
isomorphism from $A^L$ onto $\duA^R$.
The map $\kappa_A^R\colon x^R\mapsto(\du1\ra x^R)$ is an algebra
isomorphism from $A^R$ onto $\duA^L$. Furthermore, the restriction
of the canonical pairing to $\duA^L\x A^L$, $\duA^R\x A^R$,
$\duA^L\x A^R$, or to $\duA^R\x A^L$ is non-degenerate.
\end{lem}
\Proof Using Eqns(\ref{15a}-b) and the defining properties
$\bra\varphi\ra x,y\ket=\bra\varphi,xy\ket$,\dots etc. of the
Sweedler arrows one can easily verify that
\bea
(x^L\la\du1)(y^L\la\du1)&=&\du1\c\du1\cp\bra\du1\cc,x^L\ket
                           \bra\du1\ccp,y^L\ket=
              \du1\c\bra\du1\cc,x^L\ket\bra\du1\ccc,y^L\ket=\nn
              &=&x^Ly^L\la\du1\\
(\du1\ra x^R)(\du1\ra y^R)&=&\bra\du1\c,x^R\ket\bra\du1\cp,y^L\ket
                             \du1\cc\du1\ccp=
              \bra\du1\c,x^R\ket\bra\du1\cc,y^R\ket\du1\ccc\nn
              &=&\du1\ra x^Ry^R\\
(\du1\ra x^R)\la \1&=&\1\c\bra\du1\ra x^R,\1\cc\ket=
                     \1\c\eps(x^R\1\cc)=x^R\\
\1\ra(x^L\la\du1)&=&\bra\1\c,x^L\la\du1\ket\1\cc=
                     \eps(\1\c x^L)\1\cc=x^L
\eea
Thus $\kappa_A^L$ ($\kappa_A^R$) is an algebra map with inverse
$\kappa_{\duA}^R$ ($\kappa_{\duA}^L$). As for the non-degeneracy
\beanon
\bra\varphi^R,x^L\ket=0\ \forall\varphi^R&\Longrightarrow&
     x^L=\bra\du1,x^L\1\c)\1\cc=\bra\1\c\la\du1,x^L\ket\1\cc=0\\
\bra\varphi^L,x^L\ket=0\ \forall\varphi^L&\Longrightarrow&
     x^L=\bra\du1,\1\c x^L\ket\1\cc=\bra\du1\ra\1\c,x^L\ket\1\cc=0
\eeanon
and the transpose of these prove the claim. \qed
 
 
If $\{b_i\}$ is a $K$-basis of $A$ and $\{\beta^i\}\subset\duA$ is
its dual basis, $\langle\beta^i,b_j\rangle=\delta_{ij}$, then
\beabc
\sum_i\PL(b_i)\o\beta^i&=&\sum_ib_i\o\duPL(\beta^i)\ =\
\1\ra\du1\c\o\du1\cc \label{piba}\\
\sum_i\PR(b_i)\o\beta^i&=&\sum_i b_i\o\duPR(\beta^i)\ =\
\1\c\o\1\cc\la\du1 \label{pibb}
\eeabc
This can be easily seen by pairing both hand sides of any of these
equations with $\varphi\o x$ and apply the definitions (\ref{Pi}).
 
The four arrow identities of the next Scholium will be
frequently used in later computations.
\begin{scho} \label{sch: arrow}
Let $A$ be a WBA. Then for all $\varphi\in\duA$, $x^L\in A^L$, and
$x^R\in A^R$
\beabc \label{44-45}
x^L\la\varphi&=&(x^L\la\du1)\varphi\\
\varphi\ra x^R&=&\varphi(\du1\ra x^R)\ .
\eeabc
\beabc \label{46-47}
\varphi\ra x^L&=&(\du1\ra x^L)\varphi\\
x^R\la\varphi&=&\varphi(x^R\la\du1)\ .
\eeabc
\end{scho}
