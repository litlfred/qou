---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-004-15-integrals-in-weak-hopf-algebras
section_title: "Integrals in weak Hopf algebras"
section_number: 1.5
pages: 14-16
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 0.989
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
The following definition provides the weak Hopf generalization of
the well known notion of integrals in a Hopf algebra \cite{Sweedler}.
 
\begin{defi} \label{def: integral}
A left (right) integral in a weak Hopf algebra $A$ is an
element $l\in A$ {\rm (}$r\in A${\rm )} satisfying
\beq                                                 \label{l (r)}
xl\ =\ \PL(x)l\qquad \left(\ rx\ =\ r\PR(x)\ \right)
\eeq
for all $x\in A$. The space of left (right) integrals in $A$ is
denoted by $\IL$ $(\IR)$. Elements of $\I:=\IL\cap\IR$ are called
two-sided integrals.
A left or right integral in $A$ is called non-degenerate if it
defines a non-degenerate functional on $\duA$. $l\in \IL$ is
called normalized if $\PL(l)=\1$, $r\in \IR$ is called
normalized if $\PR(r)=\1$.
\end{defi}
 
Some equivalent formulations of left (right) integrals are
gathered in the next
\begin{lem}     \label{scho: IL}
Let $A$ be a weak Hopf algebra. Then
the following statements for an element $l\in A$ are equivalent:
\begin{description}
\item[a)] $l\in \IL$
\item[b)] $l\c\o x l\cc=S(x)l\c\o l\cc$ for all $x\in A$
\item[c)] $l\la\duA\subset \duA^L$
\item[d)] $(\varphi\ra x)\la l=S(x)(\varphi\la l)$ for all
$\varphi\in\duA$ and $x\in A$
\item[e)] $(\mbox{\rm Ker}\PL)l=0$
\item[f)] $S(l)\in\IR$
\end{description}
\end{lem}
\Proof {\bf a) $\Rightarrow$ b)}: Using (\ref{eq: 2.29b}) and
(\ref{12a}) we have $l\c\o xl\cc=[S(x\c)\o\1]\cop(x\cc l)=$
$[S(x\c)x\cc S(x\ccc)\o\1]\cop(l)=S(x)l\c\o l\cc$.
{\bf b) $\Rightarrow$ a)}: $xl=x\c l\c\eps(x\cc l\cc)=$\break
$x\c S(x\cc)l\c \eps(l\cc)=\PL(x)l$.
{\bf a) $\Leftrightarrow$ c)}: For an $l\in A$ the equation
$\langle l\la\varphi,x\rangle=\langle\duPL(l\la\varphi),x\rangle$
is clearly equivalent to the equation
$\langle\varphi,xl\rangle=\langle\varphi,\PL(x)l\rangle$.
{\bf b) $\Leftrightarrow$ d)}: By pairing the 2nd tensor factor of
{\bf b)} with an arbitrary $\varphi\in\duA$.
{\bf a) $\Rightarrow$ e)}: is obvious.
{\bf e) $\Rightarrow$ a)}: $xl=[x-\PL(x)]l+\PL(x)l=\PL(x)l$.
{\bf f) $\Leftrightarrow$ a)}: This follows by applying $S$ to
(\ref{l (r)}). \qed
 
 
Definition \ref{def: integral} as well as Lemma \ref{scho:
IL} provide rather technical
characterizations of integrals. The next argument sheds some light
on their real nature. Consider the left $A$-module map $\eps_R$
from the left
regular $A$-module to the trivial $A$-module given by acting
with the trivial representation on the cyclic vector $\du1$:
\bea      \label{eq: vartheta}
\eps_R\ \colon&_AA& \to\ _A\duA^R\nn
&x& \mapsto\ (x\la\du1)\ .
\eea
The existence of this (non-zero) map shows that
$\Hom(_AA,\,_A\duA^R)$ is non-zero. However,
there is in general no guarantee that $\Hom(_A\duA^R,\,_AA)$
is non-zero. Left integrals are precisely the objects that label
the possible homomorphisms of the latter type.
\begin{lem}                           \label{lem:embedtrivi}
Left integrals $l$ in $A$ are in one-to-one correspondence with
left $A$-module homomorphisms $f\colon \,_A\duA^R\to \,_AA$. The
correspondence is given by $f\mapsto f(\du1)\in\LI$. What is more
the above map provides an isomorphism
$\LI_A\cong\Hom(\,_A\duA^R,\,_AA)$ of right $A$-modules. In other
words $\LI_A$ is isomorphic to the $A$-dual of the trivial left
$A$-module.
\end{lem}
\Proof If $f\in\Hom(\,_A\duA^R,\,_AA)$ then
$xf(\du1)=f(x\la\du1)=f(\PL(x)\la\du1)=\PL(x)f(\du1)$, hence
$f(\du1)\in\LI$. This is obviously a right $A$-module map. It is
invertible since for $l\in\LI$ the map $f_l\colon\duA^R\to A$,
$f_l(\varphi^R):=(\1\ra\varphi^R)l$ is a left $A$-module map
and satisfies $f_l(\du1)=l$. \qed
 
The identification of $\LI$ with $\Hom(\,_A\duA^R,\,_AA)$ yields
an $A$-valued bilinear form $_A\duA^R\x\LI_A\to A$ given by
evaluation, $(\varphi^R,l)\mapsto f_l(\varphi^R)$.
Replacing $_A\duA^R$ with $_AA^L$ using the isomorphism of Lemma
\ref{lem: trivials} we obtain that this bilinear form is nothing
but multiplication in $A$
\beq                       \label{eq: AL IL}
_AA^L\ \x\ \LI_A\ \to\ _AA_A\ ,\qquad (x^L, l)\ \mapsto x^L \, l
\eeq
and it is an $A$-$A$ bimodule map. We claim that (\ref{eq: AL IL})
is a non-degenerate bilinear form. From one side, $x^Ll=0\
\forall x^L\in A^L\ \Rightarrow\ l=0$, this is trivial. From the
other side we will be able to prove this after having established
that WHAs are quasi-Frobenius algebras in Thm. \ref{th:q-Frob}. As
a matter of fact by Theorem 61.2 of \cite{Curtis-Reiner} the left
annihilator of the right annihilator of the left ideal $\Ker\PL$
is $\Ker\PL$ itself. Now by Lemma \ref{scho: IL}.e) the right
annihilator of $\Ker\PL$ is just $\LI$. Thus $x^Ll=0\ \forall
l\in\LI\ \Rightarrow\ x^L=0$ follows.
 
Now we turn to an other characterization of left integrals
that is related to conditional expectations.
Notice at first that if $\lambda\in \duIL$ then
the map $E_{\lambda}\colon x\mapsto \lambda\la x$ is an
$A^L$-$A^L$-bimodule map from $A$ into $A^L$ commuting with the
right $\hat A$-action on $A$. In fact, all such
maps arise from a left integral, as the following Lemma shows.
\begin{lem}
The left integrals $\lambda\in\duIL$ are in one-to-one
correspondence with right $\duA$-module maps
$E\in\Hom(A_{\duA},A^L_{\duA})$ via
\beanon
\lambda&\mapsto& E_{\lambda}\\
E&\mapsto&\eps\circ E\ .
\eeanon
\end{lem}
\Proof If $\lambda$ is a left integral then $E_{\lambda}$ is a
right $\duA$-module map and maps into $A^L$ by Lemma
\ref{scho: IL}.c).
 
Now let $E\in\Hom(A_{\duA},A^L_{\duA})$. Then
\[
E(x)=\eps(\1\c E(x))\1\cc=\eps\circ E(S^{-1}(\1\c)x)\1\cc
\]
where we used the fact that a right $\duA$-module map is an
$A^L$-$A^L$-bimodule map by (2.20b) and (2.21a).
Hence
\[
E(x)=\eps\circ E(x\ccc)x\c S(x\cc)=\PL(\lambda\la x)
\]
where $\lambda:=\eps\circ E$. It remained to show that $\lambda$
is a left integral.
\[
\bra\varphi\lambda,x\ket=\eps(E(x\ra\varphi))=\eps(E(x)\ra\varphi)
=\bra\duPL(\varphi)\lambda,x\ket
\]
which proves the claim.\qed
 
The characterization of left integrals $\lambda$ as "conditional
expectations" $E_{\lambda}$ provides a link to the theory of
inclusions and "Jones extensions" \cite{NSzW}.
 
The properties of the normalized and the non-degenerate
left integrals will be discussed in later Subsections. Here we
only remark that $\lambda$ is non-degenerate iff $E_{\lambda}$ is
non-degenerate and $\lambda$ is normalized iff $E_{\lambda}$ is
unital.
 
There are two twisting operations $A\mapsto A^{op}$ and $A\mapsto
A_{cop}$ that produce WHAs from WHAs. In the first one the
multiplication $\mu$ is replaced with opposite multiplication
$\mu^{op}(x,y)=\mu(y,x)$ while in the second the coproduct is
replaced by $\Delta^{op}(x)=x\cc\o x\c$. In both cases the
antipode is replaced by $S^{-1}$. The left and right
subalgebras$/$integrals and the dual WHAs of the resulting four
twisted
versions of a WHA $A$ are related to those of $A$ as follows.
 
\[\begin{array}{|l|ccccccc|} \hline
& \PL & \PR & A^L & A^R & \LI & \RI &\duA\\ \hline
A=A(\mu,\cop,S)
&\PL&\PR&A^L&A^R&\LI&\RI&\duA\\
A^{op}=A(\mu^{op},\cop,S^{-1}) &S^{-1}\circ\PR&
S^{-1}\circ\PL&A^L & A^R & \RI & \LI&\duA_{cop}\\
A_{cop}=A(\mu,\cop^{op},S^{-1})
&S^{-1}\circ\PL&S^{-1}\circ\PR&A^R&A^L&\LI&\RI&\duA^{op}\\
A^{op}_{cop}=A(\mu^{op},\cop^{op},S)
&\PR&\PL&A^R&A^L&\RI&\LI&\duA^{op}_{cop}\\ \hline
\end{array}\]
As an application of the table we give here the twisted versions
of the identity of Lemma \ref{scho: IL}.d):
\beabc
(\varphi\ra x)\la l& =& S(x) (\varphi\la l)\\
(x\la\varphi)\la r&=&(\varphi\la r) S^{-1}(x)\\
l\ra(\varphi\ra x)&=& S^{-1}(x)(l\ra\varphi)\\
r\ra(x\la\varphi)&=&(r\ra\varphi) S(x)
\eeabc
for all $x\in A$, $\varphi\in \duA$, $l\in \LI$, and $r\in \RI$.
