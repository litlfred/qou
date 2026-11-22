---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-010-111-first-consequences-of-the-c-structure
section_title: "First consequences of the $C^*$-structure"
section_number: 1.11
pages: 31-33
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.987
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
\begin{defi}
We define a $^*$-WHA as a WHA $(A,\1,\cop,\eps,S)$ over the
complex
numbers $\C$ together with an antilinear involution $^*$ such that
\begin{description}
\item[i)]\ $(A,\ ^*)$  is a $^*$-algebra,
\item[ii)]\ $\cop$ is a $^*$-algebra map, i.e.
      $(x^*)\c\o(x^*)\cc=(x\c)^*\o(x\cc)^*$ for all $x\in A$.
\end{description}
\end{defi}
By uniqueness of the unit, counit, and the antipode (see Lemma
\ref{lem: uniq S}) we have the following additional relations in a
$^*$-WHA.
\beq   \label{eq: 66}
\1^*=\1,\quad\eps(x^*)=\overline{\eps(x)},\quad
S(x^*)^*=S^{-1}(x).
\eeq
Now it is easy to check that the projections $\PL$ and $\PR$
satisfy
\beq
\PL(x)^*=\PL(S(x)^*),\qquad \PR(x)^*=\PR(S(x)^*)
\eeq
therefore $A^L$ and $A^R$ are $^*$-subalgebras of $A$.
As an elementary exercise we obtain selfduality of the $^*$-WHA:
\begin{scho}
Let $A$ be a $^*$-WHA and define a star operation on its dual as
follows
\beq
\bra\varphi^*,x\ket\ =:\ \overline{\bra\varphi, S(x)^*\ket}\ .
\eeq
Then $\duA$ with this star operation becomes a $^*$-WHA.
\end{scho}
 
For a $^*$-WHA $A$ the canonical isomorphisms $\kappa_A^L\colon
A^L\to\duA^R$ and $\kappa_A^R\colon A^R\to\duA^L$ of Lemma
\ref{kappa} become $^*$-algebra isomorphisms.
 
We omit the discussion of further properties of $^*$-WHAs and turn
to the most important case of $C^*$-WHAs.
\begin{defi}
A $^*$-WHA $A$ possessing a faithful $^*$-representation is called
a $C^*$-weak Hopf algebra, or $C^*$-WHA for short.
\end{defi}
Being a finite dimensional $C^*$-algebra any $C^*$-WHA can be
uniquely characterized, as an algebra, by the dimensions
$n_r\in\N$ of its blocks where $r$ is running over the finite set
$\Sec A$ of equivalence classes of irreducible representations
(i.e. the sectors) of $A$.
\beq
A\ \cong\ \bigoplus_{r\in\Sec A}\ M_{n_r}\ ,\qquad
M_{n_r}=\mbox{Mat}(n_r,\C)\ .
\eeq
$A^L$ and $A^R$ are unital $^*$-subalgebras therefore they are
$C^*$-algebras as well and we have natural numbers $n_a$,
$a\in\Sec A^L$ and $n_b$, $b\in\Sec A^R$ characterizing the type
of $A^L$ and $A^R$, respectively.
\beq
A^c\ \cong\ \bigoplus_{a\in\Sec A^c}\ M_{n_a}\ ,\qquad c=L, R\ .
\eeq
The antiisomorphism $S\colon A^L\to A^R$ establishes a bijection
$a\mapsto\bar a$ of the blocks of $A^L$ to the blocks of $A^R$
such that $n_{\bar a}=n_a$. (We consider $\Sec A^L$, $\Sec A^R$,
and $\Sec A$ as disjoint sets which allows to use one function
$n$.)
 
The following elementary but important Proposition will be the
basic ingredient in proving both the existence of Haar measures
and rigidity of the representation category of $C^*$-WHAs.
\begin{prop}                             \label{pro: g}
Let $A$ be a finite dimensional $C^*$-algebra and $S\colon A\to
A^{op}$ an algebra isomorphism such that $(\,^*\,\circ
S)^2=\id_A$. Then there exists $g\in A_\x$ such that
\begin{description}
\item[i)]$\ g\geq\ 0$
\item[ii)]$\ gxg^{-1}\ =\ S^2(x),\ \ x\in A$
\item[iii)]$\ \tr_r(g)\ =\ \tr_r(g^{-1}),\ \ r\in\Sec A$
\item[iv)]$\ S(g)\ =\ g^{-1}$
\end{description}
where $\tr_r$ denotes trace in the irreducible representation
$D_r$.
An element $g\in A$ satisfying only the first three properties is
already unique.
\end{prop}
\Proof The restriction $S|_{{\rm \scriptstyle Center}\,A}$ is an
algebra automorphism
therefore acts on the minimal central idempotents $e_r$ as
$S(e_r)=e_{\bar r}$ where $r\mapsto \bar r$ is a permutation of
$\Sec A$. Since $e_r^*=e_r$ and $^*\circ S$ is an involution,
$r\mapsto\bar r$ is an involution.
 
Choose matrix units $\{e_r^{\alpha\beta}\}$ for the $C^*$-algebra
$A$ and define the antiautomorphism $S_0\colon A\to A$ by
$S_0(e_r^{\alpha\beta}):=e_{\bar r}^{\beta\alpha}$. Then
$S_0^2=\id_A$ and $^*\circ S_0=S_0\circ\,^*$. Since $S\circ S_0$
is an automorphism of $A$ that acts as the identity on the centre,
there exists $C\in A$ invertible such that $S=\Ad_C\circ S_0$..
It follows that
\beq
^*\circ S(x)=C^{-1*}S_0(x^*)C^*,\quad
(^*\circ S)^2(x)=C^{-1*}S_0(C^{-1})xS_0(C)C^*=x,
\eeq
therefore $S_0(C)C^*$ is central and so is its adjoint
$K:=CS_0(C^*)=S(C^*)C$.
\beq
S^2(x)=CS_0(CS_0(x)C^{-1})C^{-1}=CS_0(C^{-1})xS_0(C)C^{-1},\quad
x\in A
\eeq
hence $T:=CS_0(C^{-1})=CC^*[S_0(C)C^*]^{-1}=CC^*K^{-1*}$
implements $S^2$ and its polar decomposition takes the form
\beq
T=ug'\,,\qquad u=K^{-1*}(K^*K)^{1/2}\,,\quad g'=C(K^*K)^{-1/2}C^*
\ .
\eeq
Using centrality of the unitary part and the computations
$S(T)=S(C)S^2(C^{-1})=$\break $S(C)TC^{-1}T^{-1}=T^{-1}$ and
$S(K)=S_0(K)=C^*S_0(C)=S_0(C)C^*=K^*$ we obtain that $g'$
is positive invertible, implements $S^2$, and satisfies
$S(g')=g'^{-1}$.
These latter three properties, however, do not fix $g$ completely.
If $c$ is positive, central, and satisfies $S(c)=c^{-1}$ then
$g=g'c$ will also satisfy the above three properties. Now defining
\beq
g:=g'c\quad\mbox{where}\quad c=\sum_r\ e_r\left(
{\tr_r(g'^{-1})\over \tr_r(g')}\right)^{1/2}
\eeq
it is easy to verify that $g$ obeys (i--iv)
of the Proposition. If $f\in A$ satisfies only (i),
(ii), and (iii) then $f=gc$
where $c$ is positive invertible, central, and
satisfies $D_r(c)=D_r(c)^{-1}$ for all irrep $D_r$. Hence $c=\1$,
proving uniqueness of $g$. \qed
