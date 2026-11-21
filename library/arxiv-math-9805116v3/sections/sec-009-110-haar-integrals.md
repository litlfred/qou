---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-009-110-haar-integrals
section_title: "Haar integrals"
section_number: 1.10
pages: 29-31
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.991
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
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
