---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-008-19-2-sided-non-degenerate-integrals
section_title: "2-sided non-degenerate integrals"
section_number: 1.9
pages: 26-29
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.972
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
The space of 2-sided integrals $\I(A):=\LI(A)\cap\RI(A)$ in a weak
Hopf algebra $A$ is a possibly zero subalgebra of $A$. The
assumption $\I(A)\neq 0$ is independent of the
assumption $\LI_*(A)\neq\emptyset$ since already Hopf algebras
provide examples \cite{Van Daele} for $\LI_*(A)\neq 0$ and $\I(A)=0$.
In this Subsection we will make the
stronger assumption $\I_*(A):=\LI_*(A)\cap\I(A)\neq\emptyset$ and
study some of the consequences. The main result will be finding a
criterion for a WHA to be a symmetric algebra.
 
At first we observe that if a non-degenerate 2-sided integral
$j$ exists
then the subspace of 2-sided integrals is obtained from $j$ by
the action of the central subalgebra $Z^R=A^R\cap\CA$,
\beq
\I=j\,Z^R\,,\quad\I_*=j\, Z^R_\x\qquad\mbox{for any}\quad
j\in\I_*\ .
\eeq
As a matter of fact if $i\in\I$ then
$i$ is a left integral therefore there exists an $x^R\in\A^R$ such
that $i=jx^R$. Thus for all $y\in A$ we have
$jx^R\PR(y)=jx^Ry=j\PR(x^Ry)$. Since $j$ is separating for the
right $A^R$-action, $x^R\PR(y)=\PR(x^Ry)$. Therefore
\[
x^RS(y)=x^RS(y\c)y\cc S(y\ccc)=S(y\c)x^Ry\cc S(y\ccc)=S(\1\c
y)x^R\1\cc=S(y)x^R
\]
hence $x^R$ is central.
 
Next we recall some facts about "modular automorphisms". Let $A$
be a finite dimensional Frobenius algebra over a field $K$ and let
$f\colon A\to K$
be a non-degenerate functional. Then the {\em modular
automorphism}
of $f$ is defined to be the unique $\theta_f\in\Aut A$ such that
\beq
f(xy)\ =\ f(y\theta_f(x))\ ,\qquad x,y,\in A\ .
\eeq
It is worth to give two other equivalent definitions of $\theta$:
\beq
f\ra x\ =\ \theta_f(x)\la f\ ,\qquad x\in A
\eeq
or simply
\beq
\theta_f\ =\ f_R^{-1}\circ f_L\ .
\eeq
Since any two non-degenerate functionals $f$ and $g$ are related
by $g=x\la f$, with $x\in A_\x$, the equivalence class
$\theta_A:=[\theta_f]$ of $\theta_f$ modulo inner automorphisms is
independent of the choice of $f$. If $A$ is a WHA which is
Frobenius then one may ask the question whether $\theta_A=[S^2]$.
\begin{defi}
A non-degenerate functional $f\colon A\to K$ over a WHA $A$ is
called a q-trace if $\theta_f=S^2$.
\end{defi}
In the term "q-trace" the letter "q" has no individual meaning.
One may as well read it as "skew trace" although we do not denie
that our motivation came from the theory of q-deformed Hopf
algebras.
\begin{lem}                          \label{lem: Sinv&qtr}
In a WHA $A$ let $l$ be a non-degenerate left integral. Then
$S(l)=l$ if and only if its dual left integral $\lambda$ is a
q-trace.
\end{lem}
\Proof $\theta_{\lambda}=S^2$ is equivalent to that the quasibasis
of $\lambda$ satisfies
\beq
l\cc\o S^{-1}(l\c)\ =\ S(l\c)\o l\cc\ .
\eeq
Applying $S$ to the second tensor factor we obtain
$\cop(l)=\cop(S(l))$ which yields $l=S(l)$ by the existence of
a counit. \qed
 
\begin{lem}                         \label{lem: S-inv}
If non-degenerate 2-sided integrals exist then all 2-sided
integrals $i\in\I(A)$ are $S$-invariant, $S(i)=i$.
\end{lem}
\Proof If we can show only that the non-degenerate 2-sided
integrals are $S$-invariant then we are ready since
$j=S(j)\in\I_*$ implies $S(jz^R)=S(z^R)j=z^Rj=jz^R$ for all
$z^R\in Z^R$.
 
So let $j\in\I_*$. Then $S(j)\in\I_*$ thus there exists an
invertible $z\in Z^R$  such that $S(j)=jz$.
Let $\lambda$ be the dual of $j$ as a left integral. Then
for arbitrary $x\in A$ and for $z^L=S^{-1}(z^{-1})$
\beanon
z^LS(x)&=&z^L(\lambda\ra x)\la j=(\lambda\ra x)\la z^Lj=
        (\lambda\ra x)\la S^{-1}(j)\\
S^2(x)z^{-1}&=&j\ra\duS^{-1}(\lambda\ra x)=j_L\circ
\duS^{-1}\circ\lambda_L(x)=\lambda_R^{-1}\circ\lambda_L(x)=\\
&=&\theta_\lambda(x)
\eeanon
Therefore $z^{-1}=\theta_\lambda(\1)=\1$ and $j$ is $S$-invariant.
\qed
 
\begin{thm} The WHA $A$ over $K$ is a symmetric algebra if and
only if it has non-degenerate
2-sided integrals and the square of the antipode is an inner automorphism.
\end{thm}
 
\Proof Let $A$ be a symmetric WHA, and $\tau\in {\hat A}$ be a
non-degenerate trace. Then there exists a unique $i\in A$ such that
$i\la \tau =\du1 =\tau\ra i$. We claim that $i$ is a 2-sided
integral. As a matter of fact
\beanon xi\la \tau &=&x\la\du1\ =\ \PL(x)\la\du1\ =\
\PL(x)i\la \tau  \\
\tau \ra ix&=&\du1\ra x\ =\ \du1\ra\PR(x)\ =\
\tau \ra i\PR(x)
\eeanon
so by non-degeneracy of $\tau$, $i\in\I$. This integral $i$ is also
non-degenerate: For any $x^R\in A^R$ one has $ix^R\la \tau =
i\la\tau\ra x^R={\hat \1} \ra x^R$,
hence $i$ is separating for ${\cal I}^L_{A^R}$ so non-degenerate by
Scholium \ref{ndeg}.
 
The innerness of $S^2$ in a symmetric algebra follows if we can
construct a non-degenerate functional on $A$ the modular automorphism
of which is $S^2$. By Lemma \ref{lem: S-inv} $i$ is $S$-invariant so
by Lemma \ref{lem: Sinv&qtr} $\chi$, the dual left integral to
$i$, is such a non-degenerate q-trace.
 
Conversely, let $S^2=\Ad_g$ with some $g\in A_\x$ and $i\in\I_*$.
Denoting the dual left integral of $i$ by $\chi$ again, $g^{-1}\la
\chi$ is a non-degenerate trace.
\qed
 
We close this Subsection with a result arising from assuming the
existence of non-degenerate 2-sided integrals in both $A$ and
$\duA$. Although the arising structure is reminiscent to that of
the "distinguished grouplike element" in Hopf algebra theory it is
not a generalization of that.
\begin{prop}
Let $A$ be a WHA and assume that both $\I_*(A)$ and $\I_*(\duA)$
are non-empty. Then $S^4$ is inner and the square of $\theta_A$ is
the identity in $\Out A$. Moreover and more explicitely, for $\hat
h\in\I_*(\duA)$ there exist invertible elements $a_L\in A^L$ and
$\alpha_L\in\duA^L$ such that, with the notations $a_R=S(a_L)$ and
$\alpha_R=\duS(\alpha_L)$, we have
\bea
\Ad_{a_La_R^{-1}}&=&S^4\label{eq: S^4}\\
\Ad_{a_La_R}&=&\theta_{\hat h}^2\label{eq: theta^2}\\
a_La_R^{-1}\la \psi\ra a_La_R^{-1}&=&\alpha_L\alpha_R\psi
\alpha_R^{-1}\alpha_L^{-1}\,,\quad\psi\in\duA\
\label{eq: a-alfa}
. \eea
\end{prop}
\Proof Choose $h\in \I_*(A)$ and $\hat h\in\I_*(\duA)$ and let
$\lambda$ be the dual of $h$ and $l$ be that of $\hat h$, as left
integrals. Define
\beq
a_L=\hat h\la h\ ,\qquad \alpha_L=h\la\hat h\ .
\eeq
Then
\beq
\du1\ra a_L=\bra\du1\c\hat h,h\ket\du1\cc=\bra\hat h\c,h\ket
\hat h\cc\duS(\hat h\ccc)=\duPL(\hat h\ra h)=\duS(\hat h\ra h)
=\alpha_L
\eeq
and introducing $a_R$ and $\alpha_R$ as above
\beq
la_L=l\ra \alpha_R=l\ra(\hat h\ra h)=h(l\ra\hat h)=h(\duS^2(\hat
h)\la l)=h
\eeq
where q-trace property of $l$ and $\duS$-invariance of $\hat h$
have been used. Similarly,
\bea
\alpha_R\la l&=\ h\ =&la_R\\
a_R\la\lambda&=\ \hat h\ =&\lambda\alpha_R\\
\lambda\ra a_R&=\ \hat h\ =&\lambda\alpha_L .
\eea
Non-degeneracy of $\hat h$ and $h$ now imply invertibility of
$a_L$, $a_R$, $\alpha_L$, and $\alpha_R$. Hence Eq(\ref{eq: a-alfa})
readily follows.
 
We can now compute the modular automorphism of $\hat h$
using the information $\theta_\lambda=S^2$.
\beq
\hat h\ra x=a_R\la\lambda\ra x=
a_R\theta_\lambda(x)\la\lambda\quad\Rightarrow\quad
\theta_{\hat h}=\Ad_{a_R}\circ S^2
\eeq
Computing $\duS(\hat h\ra x)$ in two different ways
\beanon
\duS(\hat h\ra x)&=&S^{-1}(x)\la\hat h=\hat h\ra\theta_{\hat
h}^{-1}(S^{-1}(x))\\
&=&\duS(\theta_{\hat h}(x)\la \hat h)=\hat h\ra
S^{-1}(\theta_{\hat h}(x))
\eeanon
yields
\beq
S^{-1}\circ\theta_{\hat h}=\theta_{\hat h}^{-1}\circ S^{-1}
\eeq
and finally
\beq
\Ad_{a_L}\circ S^{-2}\ =\ \theta_{\hat h}\ =\ \Ad_{a_R}\circ S^2
\eeq
from which (\ref{eq: S^4}) and (\ref{eq: theta^2}) follow
immediately. \qed
