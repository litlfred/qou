---
doc_id: arxiv-math-9805116v3
doc_title: "arXiv:math/9805116v3 [math.QA] 8 Jun 1999"
section_id: sec-008-110-haar-integrals
section_title: "Haar integrals"
section_number: 1.10
pages: 29-33
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.99
---
Since finite dimensional weak Hopf algebras do not go beyond the
"compact" and "discrete" case, the following very conservative
definition of Haar measure will suffice.
\begin{defi}  \label{def: Haar}
An element $h$ of a WHA $A$ is called a Haar integral in $A$ or
Haar measure on $\duA$ if $h$ is a normalized 2-sided integral,
i.e. $h\in \I(A)$ and $\PL(h)=\PR(h)=\1$.
\end{defi}
Obviously, if Haar integral exists then it is a unique
$S$-invariant idempotent.
As a matter of fact let $h$ and $h'$ be Haar integrals. Then
$h'=\PL(h)h'=hh'=h\PR(h')=h$. In particular $h^2=h$.
$S$-invariance follows from uniqueness since $S(h)$ is a always a
Haar integral if $h$ is.
 
In finding criteria for the existence of Haar measure in $A$ an
important role will be played by a special element $\chi\in\duA$
the definition of which was inspired by similar computations in
Hopf algebra theory \cite{Van Daele}:
\beq     \label{eq: khi}
\chi\ :=\ \sum_i\ \beta^i\ra S^{-2}(b_i)\ \equiv\ \hat L'(\du1)\,,
\eeq
where $\{b_i\}$ and $\{\beta^i\}$ are dual bases of $A$ and
$\duA$, respectively, and $\hat L'\colon\duA\to\duA$ is given by
$\hat L'(\psi):=\sum_i \beta^i\psi\ra S^{-2}(b_i)$ .  Note that
$\hat L'$ is the "cop" version of the dual analogue $\hat L$
of the projection (\ref{eq: L}) onto the space of left integrals.
Hence $\chi$ is a left integral in $(\duA)_{cop}$ and therefore in
$\duA$.
 
As we will see below if $\chi$ is non-degenerate and a q-trace then
its dual left integral will automatically be the Haar measure.
In order to see that it is a q-trace let $\Tr_A$ be the standard
trace on $\End_K A$ and introduce the notation $Q_-(x)y:=yx$.
Then for $x\in A$ we have
\beanon
\chi(x)&=&\sum_i\bra\beta^i,S^{-2}(b_i)x\ket=\Tr_A\ Q_-(x)\circ
S^{-2}\\
\chi(xy)&=&\Tr_A\ Q_-(y)\circ Q_-(x)\circ S^{-2}=
\Tr_A\ Q_-(y)\circ S^{-2}\circ Q_-(S^2(x))=\\
&=&\chi(y S^2(x)).
\eeanon
The next Lemma will be crucial in deciding whether $\chi$ is
non-degenerate.
\begin{lem}                             \label{lem: khi}
Let $l$ be a left integral in a WHA $A$ and let $\chi\in\duA$ be
the q-trace left integral defined in Eq(\ref{eq: khi}). Then
\beq                              \label{eq: l->khi}
l\la\chi\ =\ \duS^2(\du1\ra l)\ .
\eeq
\end{lem}
\Proof  Using the q-trace property of $\chi$ and then (\ref{piba})
\beanon
l\la\chi
&=&\sum_i\beta^i\ra S^{-2}(b_il)=(\du1\ra\1\c)\ra S^{-2}(\1\cc
l)=\\
&=&\bra\du1\c,S^{-1}(\1\cc)\1\c\ket\du1\cc\ra S^{-2}(l)=\du1\ra
S^{-2}(l)=\duS^{2}(\du1\ra l)
\eeanon
\qed
\begin{prop}
Let $A$ be a weak Hopf algebra over a field $K$ and let $\chi$ be
given by (\ref{eq: khi}).
\begin{description}
\item[i)] The Haar integral $h\in A$ exists if and only if $\chi$
is non-degenerate, in which case $(h,\chi)$ is a dual pair of left
integrals. In particular Haar integrals are non-degenerate.
\item[ii)] A left integral $l\in\IL $ is a Haar integral if
and only if $\PR(l)\ =\1$.
\end{description}
\end{prop}
The characterization of Haar measures under (ii) is so simple that
it
could be well used as a definition of Haar measure. Notice that in
that case the formal difference between the notions of normalized
left integral and Haar measure  were so tiny (change $\PL$ for
$\PR$) that it would smear out the big conceptual difference:
The existence of normalized left integrals is equivalent to
semisimplicity while the existence of Haar measures is much
stronger.
 
\Proof {\bf ii)} Assume $l\in\IL$ satisfies $\PR(l)=\1$. Then by
Lemma
\ref{lem: khi} $l\la\chi=\du1$. Therefore the duality Theorem
(Thm \ref{thm: dualint}) implies that $(l,\chi)$ is a dual pair of
non-degenerate left integrals. Since $\chi$ is a q-trace, Lemma
\ref{lem: Sinv&qtr} shows that $l$ is an $S$ invariant
non-degenerate left integral. Furthermore
$\PL(l)=\PL(S(l))=S\circ\PR(l)=\1$. Thus $l$ is a Haar integral.
Now assume $h$ is a Haar integral. Then obviously $h$ is a left
integral satisfying $\PR(h)=\1$.
 
{\bf i)} The "only if" part follows from the proof of (ii). Assume
$\chi$ is non-degenerate and let $h$ be its dual left integral.
Then by Lemma \ref{lem: Sinv&qtr} $h$ is 2-sided and by Lemma
\ref{lem: khi} it is normalized. \qed
 
However simple, the criteria of the above Proposition are very
difficult
to verify in concrete situations. So it is worth looking for other
criteria even if they are not applicable in full generality.
 
\begin{thm}         \label{thm: Haar}
Let $A$ be a WHA over an algebraically closed field $K$. Then a
necessary and sufficient condition for the existence of Haar
measure $h\in A$ is that  $A$ is semisimple and there exists a $g\in A_\x$
such that $gxg^{-1}=S^2(x)$ for $x\in A$
and $\tr\,D_r(g^{-1})\neq 0$ for all irreducible representation
$D_r$ of $A$\,.
\end{thm}
The assumption on $K$ is used only to ensure that $A$ is split
semisimple, $A=\oplus_r M_{n_r}(K)$, once knowing that it is
semisimple. In particular there will be a $K$-basis
$\{e_r^{\alpha\beta}\}$ for $A$ obeying matrix unit relations.
 
\Proof {\em Sufficiency}\,: Let $\tau\colon A\to K$ be the trace
with trace vector $\tau_r=\tr D_r(g^{-1})$. Then $\tau$ is
non-degenerate and has as quasibasis the element
\[
\sum_i x_i\o y_i\ :=\ \sum_r\ {1\over
\tau_r}\sum_{\alpha,\beta=1}^{n_r}\,e_r^{\alpha\beta}\o
e_r^{\beta\alpha}\ .
\]
Notice that $\sum_i x_ig^{-1}y_i=\1$. Now we
define $\chi':=g\la\tau$ and claim that $\chi'$ coincides with the
$\chi$ of Eq(\ref{eq: khi}). As a matter of fact
\beanon
\chi'(x)&=&\tau(gx)=\sum_i\tau(x_ig^{-1}y_igx)=\sum\tau(x_i
S^{-2}(y_i)x)=\\
&=&\sum_i\bra\beta_i,S^{-2}(b_i)x\ket=\chi(x)
\eeanon
where we used the fact that the dual of the basis $b_i=y_i$ is
$\beta_i=\tau\ra x_i$. Since $\chi'$ was non-degenerate by
construction, we conclude that {\em the} $\chi$ of Eq(\ref{eq:
khi}) is non-degenerate and therefore its dual left integral $l$
has $\PR(l)=\1$ by Eq(\ref{eq: l->khi}). Therefore $l$ is a Haar
measure.
 
{\em Necessity}\,: If $h\in A$ is a Haar measure then $A$ is
semisimple
by Theorem \ref{thm: semi}. Therefore $A$ is a symmetric algebra
and $\theta_A=\id$. This means that $\theta_\psi$ is inner for all
non-degenerate functional $\psi$. In particular $\theta_\chi=S^2$
is inner where $\chi$ is the dual left integral of $h$. Choose a
$g\in A_{\x}$ implementing $S^2$ and construct the non-degenerate
trace $\tau:=g^{-1}\la\chi$.
\[
\tau(x)=\chi(xg^{-1})=\Tr_A\ Q_-(xg^{-1})\circ S^{-2}=
\Tr_A\ Q_+(g^{-1})\circ Q_-(x)
\]
where $Q_+(x)y:=xy$ is left multiplication on $A$. Choosing a
matrix unit basis to evaluate the trace we obtain
\[
\tau(x)=\sum_r\ \tr D_r(g^{-1})\ \tr D_r(x)
\]
and by non-degeneracy of $\tau$ all components $\tr D_r(g^{-1})$
of the trace vector are non-vanishing. \qed
 
 
 
 
\sec{$C^*$-Weak Hopf Algebras}
 
In this Section we introduce the $C^*$-structure in WHAs
which is inevitable if WHAs are to be used as symmetries of
inclusions of von Neumann algebras, in particular in quantum field
theory. Utilizing the results of Sections 2 and 3 we establish the
existence of two canonical elements in any $C^*$-WHA, the Haar
measure $h$ and the canonical grouplike element $g$. While the
Haar measure is well known for $C^*$-Hopf algebras, the
canonical grouplike element cannot be recognized in finite
dimensional Hopf
algebras because it is always equal to $\1$. This is related to
involutivity of the antipode in finite dimensional $C^*$-Hopf
algebras \cite{W}. The very fact that $C^*$-WHAs can have
non-involutive antipodes provides the sufficient flexibility
for the emergence of non-integer dimensions.
 
 
 

\subsection{First consequences of the $C^*$-structure}
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
