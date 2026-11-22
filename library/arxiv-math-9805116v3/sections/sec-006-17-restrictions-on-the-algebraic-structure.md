---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-006-17-restrictions-on-the-algebraic-structure
section_title: "Restrictions on the algebraic structure"
section_number: 1.7
pages: 21-22
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.986
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
The existence of a weak Hopf structure on the $K$-algebra $A$
involves certain restrictions on the algebra $A$, just like in
case of Hopf algebras. In this subsection we show that any WHA
$A$ is quasi-Frobenius, i.e. self-injective. The notions of
semisimple and separable algebras coincide within the class of
WHAs. Moreover, we prove an analogue of Maschke's Theorem which
claims that $A$ is semisimple if and only if it has normalized
left integrals.
 
\begin{thm}     \label{th:q-Frob}
Every weak Hopf algebra over a field $K$ is a
quasi-Frobenius algebra.
\end{thm}
\Proof By Theorem 61.2 of \cite{Curtis-Reiner} it is sufficient
to prove that the left regular $A$-module $_AA$ is injective. By
the Nagao--Nakayama theorem injectivity of a left $A$-module is
equivalent to that it is a direct sum of $K$-duals of principal
indecomposable right $A$-modules.
Since $\duA^A$ is the $K$-dual of $_AA$, we need to
show that $\duA^A$ is a direct sum of principal
indecomposable right $A$-modules, i.e. that $\duA^A$ is
projective.
This in turn is a consequence of the Fundamental Theorem of WHM-s.
 
As a matter of fact we have the right $A$-module isomorphisms
\beq        \label{eq:q-Frob}
\duA^A\ \cong\ \duIL\amalgo{A^L}A_A\ \cong P(\duIL\amalgo{K}A_A)
\eeq
the first of which is the consequence of the Fundamental Theorem
of the right WHM $_{\duA}\duA^A$, the second of which is a rather
simple property of the amalgamated tensor product with
respect to the separable algebra $A^L$. In order to explain the
projection $P$ here we make a digression.
\begin{lem}
Define the map $P\colon \duIL\amalgo{K}A\to\duIL\amalgo{K}A$ by
\beq
P(\lambda\o x)\ :=\ S^2(\1\c)\la\lambda\o\1\cc x\ .
\eeq
Then $P\circ P=P$ and $\Ker P$ coincides with $\Ker\pi$ of the
canonical projection $\pi$ from the free right $A$ module
$\duIL\amalgo{K}A_A$ onto $\duIL\amalgo{A^L}A_A$. Therefore
\beq
P(\duIL\amalgo{K}A_A)\stackrel{\pi|_{{\scriptscriptstyle Im}
P}}{\longrightarrow} \duIL\amalgo{A^L}A_A
\eeq
is an isomorphism of right $A$-modules.
\end{lem}
\Proof The kernel of the canonical projection is
\beq
\Ker\pi\ =\ \mbox{Span}_K\{(\lambda\o x^Ly)-(S(x^L)\la\lambda\o
x)\ |\ \lambda\o y\in\duIL\o A,\ x^L\in A^L\ \}
\eeq
If $\sum_i(\lambda_i\o x_i)\in\Ker\pi$ then obviously $\sum_i
S^2(\1\c)\la\lambda_i\o\1\cc x_i=0$, therefore $\Ker\pi\subset\Ker
P$. Now assume $\sum\lambda_i\o x_i\in\Ker P$. Then
\beanon
\sum_i\lambda_i\o x_i&=&\sum_i\lambda_i\o S(\1\c)\1\cc x_i=\\
&&\sum_i[\lambda_i\o S(\1\c)(\1\cc
x_i)-S^2(\1\c)\la\lambda_i\o\1\cc x_i]\ \in\ \Ker\pi
\eeanon
This proves $\Ker\pi=\Ker P$. That $P$ is a projection and a right
$A$-module map is trivial to verify. Therefore $\pi|_{{\rm
\scriptstyle Im} P}$ is an $A$-module isomorphism.\qed
 
{\it Back to the Proof of Theorem \ref{th:q-Frob}}\,: In virtue of
the above Lemma the amalgamated tensor product
$\duIL\amalgo{A^L}A_A$ is the direct summand of a free $A$-module,
hence projective. By Equation \ref{eq:q-Frob} this is isomorphic
to $\duA^A$. This proves projectivity of $\duA^A$, hence
injectivity of $_AA$.\qed
 
\bigskip\noindent
The equivalence of (c) and (d) of the next Theorem
provides a weak Hopf version of Maschke's Theorem known for Hopf
algebras as well \cite{LS}. Below we denote
$\eps_R(x):=x\la\du1$.
 
\begin{thm}       \label{thm: semi}
The following conditions on a WHA $A$ over $K$ are equivalent:
\begin{description}
\item[a)] $A$ is semisimple.
\item[b)] In the category of left $A$-modules the following exact
sequence is split
$$
0\longrightarrow\Ker\eps_R\longrightarrow\,
_AA\stackrel{\eps_R}{\longrightarrow}\, _A\duA^R\longrightarrow 0
$$
\item[c)] There exists a normalized left integral $l\in A$.
\item[d)] $A$ is a separable $K$-algebra.
\end{description}
\end{thm}
\Proof
(a$\Rightarrow$c):
If $A$ is semisimple, then $\Ker\PL\equiv\Ker\eps_R$ being a
a left ideal there exists $p=p^2\in A$ such that $\Ker\PL=Ap$,
whence $l=\1-p$ is a normalized left integral by Lemma
\ref{scho: IL}.e.
 
(b$\Leftrightarrow$c): Let $F\in\Hom(_A\duA^R,\,_AA)$ be such that
$\eps_R\circ F=\id$. Then $xF(\du1)=F(x\la\du1)=\PL(x)F(\du1)$,
for $x\in A$, therefore $F(\du1)\in\IL$. Moreover,
$\du1=\eps_R(F(\du1))=F(\du1)\la\du1$ implying
$\PL(F(\du1))=\1$.
Conversely, if $l\in\LI$ is a normalized left integral then
$F\in\Hom(_A\duA^R,{_AA})$ given by $F(\eps_R(x)):=xl$ satisfies
$\eps_R\circ F=\id$.
 
(c$\Rightarrow$d): Let $l$ be a normalized left integral. Then
$q=l\c\o S(l\cc)$ is a separating idempotent for $A$. As a matter
of fact $\mu(q)=\1$ follows from the normalization $\PL(l)=\1$
while $(x\o\1)q=q(\1\o x)$ is precisely the left integral property
of Lemma \ref{scho: IL}.b.
 
 
(d$\Rightarrow$a):
This is a standard result \cite{Pierce}.
 \qed
