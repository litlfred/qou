---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-007-18-non-degenerate-integrals
section_title: "Non-degenerate integrals"
section_number: 1.8
pages: 22-26
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.963
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Until now we have not been able to decide whether the WHM Theorem
of Subsection 3.2 implies the existence of non-degenerate
integrals, as it does in case of Hopf algebras. In the present
subsection we will show that the existence of non-degenerate
integrals in the WHA $\duA$ is equivalent to the existence of
non-degenerate functionals on $A$, i.e. that $A$ is a Frobenius
algebra. As a byproduct we obtain that the class of Frobenius WHAs
is selfdual.
 
The space $\RI$ of right integrals can be viewed as a $K$-module,
as a left $A^L$-module $_{A^L}\RI$ by left multiplication, and as
a left $A$-module $_A\RI$ since it is a left ideal of $A$. From
the latter point of view $_A\RI$ is the dual of the trivial right
$A$-module, $_A\RI\cong\Hom(\duA^L_A,A_A)$, by a twisted version
of Lemma \ref{lem:embedtrivi}. As a $K$-module $\RI$ has $\duLI$
as its $K$-dual,
$\duLI\cong\Hom(_K\RI,\,_KK)$ the isomorphism being given by the
restriction of the canonical pairing (see Corollary \ref{coro:
WHM}). The
next Lemma shows that $\duLI$ is also the $A^L$-dual of $\RI$ with
right $A^L$-module structure precisely the one needed in Example
\ref{ex:rWHM}, i.e. $\lambda\cdot x^L=S(x^L)\la\lambda$.
\begin{lem}
The $A^L$-valued bilinear form
\beq
(\ ,\ )_{A^L}\ \colon\ \RI\x\duLI\ \to\ A^L\ ,\qquad
(r,\lambda)_{A^L}=\lambda\la r
\eeq
provides an isomorphism of right $A^L$-modules
\beq
(\duLI)^{A^L}\ \to\ \Hom(_{A^L}\RI,\,_{A^L}A^L)\ ,\qquad
\lambda\mapsto\ (r\mapsto(r,\lambda)_{A^L})\ ,
\eeq
i.e. $(\duLI)^{A^L}$ is the $A^L$-dual of $_{A^L}\RI$.
\end{lem}
\Proof At first verify the following properties of the
$A^L$-valued bilinear form.
\beabc
(x^L\cdot r,\lambda)_{A^L}&=&x^L(r,\lambda)_{A^L}\\
(r,\lambda\cdot x^L)_{A^L}&=&(r,\lambda)_{A^L}\,x^L\\
(r,\lambda)_{A^L}=0\ \forall r\in\RI&\Rightarrow&\lambda=0
\eeabc
The first two are simple WHA identities. The third one follows
from the relation $\eps((r,\lambda)_{A^L})=\bra\lambda,r\ket$
and from non-degeneracy of the canonical pairing $\bra\ ,\ \ket$
on $\duLI\x\RI$ (Corollary \ref{coro: WHM}). Now properties (a)
and (b) tell
us that $\lambda\mapsto (.,\lambda)_{A^L}$ is indeed the required
$A^L$-module map and (c) ensures that it is injective. In order to
show that it is surjective it is sufficient to find finite sets of
elements $\{r_a\}$ in $\RI$ and $\{\lambda^a\}$ in $\duLI$ such
that
\beq             \label{fgp}
\sum_a (r,\lambda^a)_{A^L}\ r_a\ =\ r\qquad \forall r\in\RI\ .
\eeq
For if such elements exist then any
$f\in\Hom(_{A^L}\RI,\,_{A^L}A^L)$ can be written as $f=\sum_a
\lambda^a\cdot f(r_a)$. As a matter of fact
\[
f(r)=f(\sum_a (r,\lambda^a)_{A^L}\cdot r_a)=\sum_a
(r,\lambda^a)_{A^L}\ f(r_a)=(r,\sum_a\lambda^a\cdot f(r_a))_{A^L}
\]
for all $r\in\RI$. Now we claim that a pair of dual bases $\{r_a\}$ of
$\RI$ and $\{\lambda^a\}$ of $\duLI$, in the sense of $K$-duality,
i.e. $\bra\lambda^a,r_b\ket=\delta_{ab}$, also satisfies
(\ref{fgp}). As a matter of fact for $\lambda\in\duLI$ we have
\beanon
&&\bra\lambda,\sum_a (\lambda^a\la r)r_a\ket=\eps(\sum_a
(\lambda^a\la r)(\lambda\la r_a))=\sum_a\bra\lambda^a,r(\lambda\la
r_a)\ket=\\
&=&\sum_a\bra\lambda^a, r(S(r_a)\ra \duS^{-1}(\lambda))\ket=
\sum_a\bra\lambda^a\c,r\ket\,\bra\duS^{-1}(\lambda)\lambda^a\cc,
S(r_a)\ket=\\
&=&\sum_a\bra\lambda\lambda^a\c,r\ket\,\bra\lambda^a\cc,S(r_a)\ket=
\bra\lambda\left[\sum_a S(r_a)\la\lambda^a\right],\,r\ket
=\bra\lambda,r\ket
\eeanon
where in the last equality (\ref{eq:r-lambda}) has been used.\qed
 
Notice that Eqn(\ref{fgp}) means that $_{A^L}\RI$ is finitely
generated projective\footnote{Although this is clear from the
fact that $A^L$ is semisimple, constructing the concrete bases
$\lambda^a,\ r_a$ was not in vain since it will help to compute
the commutant in (\ref{eq: EndIR}).}.
Therefore by a general result (see e.g. \cite{Curtis-Reiner new})
\beq
\duLI\amalgo{A^L}\RI\ \cong\ \End\,_{A^L}\RI\ .
\eeq
On the other hand the isomorphism $\alpha$ of the WHM Theorem, if
restricted to $\duLI\amalgo{A^L}\RI$, yields an isomorphism onto
$\duA^L$. Thus we have the composition
\beq
{\cal E}\colon\ \
A^L\longrightarrow\duA^L\stackrel{\alpha^{-1}}{\longrightarrow}
\duLI\amalgo{A^L}\RI\longrightarrow\End\,_{A^L}\RI
\eeq
of isomorphisms. Evaluating it explicitely we obtain
\bea            \label{eq: EndIR}
r\cdot{\cal
E}(x^L)&=&r\cdot\left(\sum_{ij}S^2(b_i)\la(\beta^i\beta^j(\du1\ra
x^L))\ \o\ b_j\right)=r\cdot\left(\sum_j\hat L(\beta^j(\du1\ra
x^L))\o b_j\right)=\nn
&=&r\cdot(\sum_a\lambda^a\o S(x^L)r_a)=\sum_a (r,\lambda^a)_{A^L}
S(x^L)r_a=\nn
&=&S(x^L) r\quad \forall r\in\RI,\ x^L\in A^L\ .
\eea
This proves our next
\begin{prop}
The left modules $_{A^L}\RI$ and $_{A^R}\RI$ are faithful and the
endomorphism algebra of $_{A^L}\RI$ consists of left
multiplications with elements of $A^R$. Therefore
\beq
\End\,_{A^L}\RI\ \cong\ A^L\ ,\qquad\mbox{ as algebras.}
\eeq
\end{prop}
 
The set $\Sec A^L$ of equivalence classes of simple left
$A^L$-modules will be called the {\em sectors} of $A^L$. For $a\in
\Sec A^L$ let $V_a$ be a simple module from the class $a$ and let
$\D_a=\End V_a$ be the corresponding division algebra. Then by the
Wedderburn structure theorem $A^L\cong\oplus_a M_{n_a}(\D_a)$. Let
$m_a$ denote the multiplicity of $V_a$ in the semisimple module
$_{A^L}\RI$. Then $\End\,_{A^L}\RI\cong\oplus_a M_{m_a}(\D_a)$
which is, by the Proposition, isomorphic to $A^L$. This is
possible only if there is a permutation
\beq
\tilde{\empty}\ \colon\ \Sec A^L\to\Sec A^L\,,\quad \mbox{such
that}\ n_{\tilde a}=m_a\ \mbox{and}\ \D_{\tilde a}=\D_a\ .
\eeq
This means that $\RI$, as an $A^L$-$\End\,_{A^L}\RI$ bimodule, can
be identified with a direct sum of matrices,
\beq
_{A^L}\RI\ \cong\ \oplus_a\ \Mat(n_a\x m_a,\, \D_a)\ .
\eeq
This allows us to compute its $K$-dimension and apply the
Cauchy-Schwarz inequality to obtain the bound
\beq
\dim_K\RI\ =\ \sum_a(\dim_K \D_a)\,n_am_a\ \leq\ \sum_a(\dim_K
\D_a)\, n_a^2 \ =\ \dim_K A^L\ .
\eeq
Equality holds here iff $m_a=n_a$, $a\in\Sec A^L$, i.e. iff
$_{A^L}\RI\cong \,_{A^L}A^L$. Now we are ready to prove the
following
\begin{thm}
Let $A$ be a WHA over the field $K$. Then the following conditions
are equivalent.
\begin{description}
\item[i)] $A$ is a Frobenius algebra;
\item[ii)] $\dim_K\,\RI\ =\ \dim_K\,A^L$;
\item[iii)] Non-degenerate integrals exist in $A$;
\item[iv)] $\duA$ is a Frobenius algebra.
\end{description}
\end{thm}
\Proof {\bf (i)$\Rightarrow$(ii)} If $_AA\cong\,_A\duA$ then their
invariants $\I(_AA)=\LI$ and $\I(_A\duA)=\duA^L$, respectively
(see Scholium 3.5), are isomorphic as $K$-spaces.
{\bf (ii)$\Rightarrow$(iii)} As we have seen above the $K$-space
isomorphism of $\RI$ and $A^L$ implies that $_{A^L}\RI$ is
isomorphic to the left regular module $_{A^L}A^L$. Since the
latter is cyclic, there exists a cyclic vector $r\in\,_{A^L}\RI$.
Thus $l:=S(r)$ is cyclic in $(\LI)^{\duA^L}$.  As a matter of
fact $\LI=S(\RI)=S(A^Lr)=lA^R=\duS(\duA^L)\la l$. Now
interchanging the roles of $A$ and $\duA$ in the WHM Theorem
\[
A=\alpha(\LI\amalgo{\duA^L}\duA)=\duS(\duA)\la\LI=\duS(\duA)\la
(\duS(\duA^L)\la l)=\duA\la l\ ,
\]
hence $l$ is a non-degenerate left integral in $A$. {\bf
(iii)$\Rightarrow$(iv)} is obvious since $l$ is a non-degenerate
functional on $\duA$. {\bf (iv)$\Rightarrow$(i)} Repeat the
arguments above from {\bf (i)} to {\bf (iv)} with $A$
replaced by $\duA$. \qed
 
Weak Hopf algebras satisfying any one of the conditions of the
above Theorem will be called {\em Frobenius WHAs}.
Note that since semisimple algebras are Frobenius, in a semisimple WHA there
exist both normalized and non-degenerate integrals, although there
may be no integral sharing both properties.
\footnote{As an example consider $M_2(\Z_2)$, the semisimple algebra
of two by two matrices
over the field of mod2 residue classes. Fix a set of matrix units
$\{e_{ij}\}$ and introduce the coproduct $\cop(e_{ij})\colon
 = e_{ij} \o e_{ij}$. Then we have two  normalized left integrals
$l_j = \sum_i e_{ij}$
for $j=1,2$ neither of which is non-degenerate. The only non-degenerate
left integral is  $l=l_1+l_2$ for which however $\PL(l)=0$. }
 
 
As an immediate consequence of the above considerations we have
\begin{scho} \label{ndeg} The following properties for $l\in
\LI$ ($r\in\RI$) are equivalent:
\begin{description}
\item[i)] $l$ ($r$) is non-degenerate;
\item[ii)] $l$ is separating for ${\cal I}^L_{A^{L,R}}$
            ($r$ is separating for $_{A^{L,R}}{\cal I}^R$ );
\item[iii)] $l$ is cyclic for ${\cal I}^L_{A^{L,R}}$
             ($r$ is cyclic for $_{A^{L,R}}{\cal I}^R$).
\end{description}
\end{scho}
 
In a Frobenius
WHA $A$ the group of invertible elements $A^R_\x$ of $A^R$ acts on
the set $\LI_*(A)$ of non-degenerate left integrals transitively
and freely. Similar statement holds for the non-degenerate right
integrals $\RI_*$,
\beq
\LI_*=l\,A^R_\x\ ,\qquad \RI_*=A^L_\x\,r
\eeq
for any $l\in\LI_*$ and $r\in\RI_*$. Similar relation for the dual
integrals shows that there are one-to-one correspondences between
non-degenerate integrals of $A$ and of $\duA$. The Theorem below
selects a distinguished "natural" one-to-one correspondence.
\begin{thm}                 \label{thm: dualint}
Let $A$ be a WHA and $l\in\IL$ be a left integral. If there
exists a $\lambda\in\duA$ such that $\lambda\la l=\1$ then
it is unique, it is a left integral in
$\duA$, and both $l$ and $\lambda$ are
non-degenerate. Moreover $l\la\lambda=\du1$. Such a pair
$(\l,\lambda)$ will be called a dual pair of left integrals.
 
Similarly, elements $r\in\RI_*$ and $\lambda\in\duLI_*$ are in
one-to-one correspondence by either one of the equivalent
relations $\lambda\la r=\1$ or $\lambda\ra r=\du1$.
\end{thm}
 
\Proof
By Lemma \ref{scho: IL}.d) if $l$ is a left integral such
that $\lambda\la l=\1$ then\footnote{Here
we use the standard notations $f_L,f_R\colon
A\to\duA$ defined by $f_L(x):=f\ra x$ and $f_R(x):=x\la f$ for
any $f\in\duA$.}
$l_R\circ\lambda_L=S$. Since $S$ is
invertible, both $l_R$ and $\lambda_L$ are invertible, i.e. $l$
and $\lambda$ are non-degenerate and $\lambda$ is unique. To show
that $\lambda\in\duIL$
\[
\varphi\lambda\la l\ =\ \varphi\la\1\ =\ \duPL(\varphi)\lambda\la
l\ ,\quad \varphi\in\duA
\]
suffices since $l_R$ is a bijection. It remains to show that
$l\la\lambda=\du1$ which eventually justifies the term "dual" left
integral. For $l\in\IL$ and $\lambda\in\duA$ we have
\beanon
\lambda\la l=\1&\Leftrightarrow&
xl\c\bra\lambda,l\cc\ket=x\ \ x\in A\\
&\Leftrightarrow&
\bra\lambda,xl\cc\ket S^{-1}(l\c)=x\ \ x\in A\\
&\Rightarrow&
\bra l\la\lambda,x\ket=\eps(x)\ \ x\in A\\
&\Leftrightarrow&
l\la\lambda=\du1
\eeanon
 
The duality between $\duLI$ and $\RI$ follows from the above
duality between $\duLI$ and $\LI$ by passing from $A$ to $A^{op}$.
The other two twisted versions of the Theorem are not spelled out
explicitely. They can also be obtained by applying the antipode
to the above relations. \qed
 
 
Recall that the {\em quasibasis} of a non-degenerate functional
$f$ on $A$ is an element $\sum_i a_i\o b_i\in A\o A$ such that
(cf. \cite{Watatani})
\beq
\sum_i f(xa_i)b_i=x=\sum_i a_i f(b_i x)\,,\quad x\in A\ .
\eeq
(If $K$ is a field then this just means that $\{b_i\}$ is a
$K$-basis of $A$ and $\{a_i\}$ is its dual basis w.r.t. $f$.)
In other words $\sum_i a_i\o b_i$ is simply the expression $\sum_i
f_R^{-1}(\beta^i)\o b_i$ of the inverse of $f_R\colon A \to \duA$
as an element of $A\o A$.
The index of $f$ is then defined by $\Ind f:=\sum_i a_ib_i$ which
belongs to $\Center A$.
Now let $(l,\lambda)$ be a dual pair of left integrals.
Then the quasibasis of $\lambda$ is $l\cc\o S^{-1}(l\c)$ and
\beq
\Ind\lambda=S^{-1}\circ\PL(l)\ \in Z^R\ .
\eeq
In particular a non-degenerate left integral $l$ is normalized if
and only if its dual has index $\1$.
