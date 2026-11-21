---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras I: Integral Theory and C*-structure"
section_id: sec-012-113-the-canonical-grouplike-element
section_title: "The canonical grouplike element"
section_number: 1.13
pages: 35-40
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.512
doc_brief: "Weak Hopf Algebras I: Integral Theory and C*-structure — We give an introduction to the theory of weak Hopf algebras proposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
In this Subsection we investigate further properties of the
element $g$ of Proposition \ref{pro: g}. We show that it is always
a product of left and right elements, implying its
grouplikeness immediately, and obtain expressions for the
modular automorphisms of the Haar measures of $A$ and $\duA$.
 
\begin{prop}        \label{pro: gg}
In a $C^*$-WHA $A$ there exists a unique $g\in A$ such that
\begin{description}
\item[i)] $g\geq 0$ and invertible,
\item[ii)] $gxg^{-1}=S^2(x)$ for all $x\in A$,
\item[iii)] $h\cc\o h\c=h\c\o gh\cc g$.
\end{description}
\end{prop}
\Proof {\em Existence}\,: Let $g$ be the (unique) element defined
by the conditions of Proposition \ref{pro: g}. As in the
proof of Lemma \ref{lem: coph} let $\tau$ be the
$S$-invariant trace
with trace vector $\tau_q=\tr_q(g)$ and $\sum x_i\o y_i$ be its
quasibasis. Then
\bea
h\cc\o h\c&=&\sum_i x_i\o S(g^{-1}y_i)=\sum_i S^{-1}(y_i)\o
x_ig=\\
&=&\sum_i S^{-1}(y_ig^{-1})\o gx_ig=\sum_igS^{-1}(y_i)\o gx_ig
=\\
&=&\sum_i S(g^{-1}y_i)\o gx_ig\ =\ h\c\o gh\cc g
\eea
{\em Uniqueness}\,: Let $g$ and $g'$ satisfy {\bf i)}, {\bf ii)},
and {\bf iii)}. Then $g'=gc$ with $c$ central, positive, and
invertible. Furthermore, since {\bf iii)} is equivalent to
\beq
\bra \varphi\psi,\,h\ket\ =\ \bra\psi(g\la\varphi\ra g),\,h\ket\,,
\eeq
non-degeneracy of $h$ implies
\beq
g'\la\varphi\ra g'\ =\ g\la\varphi\ra g\ ,\qquad \varphi\in\duA\ .
\eeq
Therefore $c^2\la\varphi\equiv c\la\varphi\ra c=\varphi$ for all
$\varphi\in\duA$. Thus $c^2=\1$ and, by positivity, $c=\1$.
\qed
 
Notice that property {\bf iii)} of Proposition \ref{pro: gg} is
equivalent to that the modular automorphism of the
Haar functional $\varphi\mapsto\varphi(h)$ is expressible in the
form
\beq
\theta_h(\psi)\ =\ g\la\psi\ra g\ ,\qquad\psi\in\duA\ .
\eeq
\begin{defi}
Let $A$ be a $C^*$-weak Hopf algebra. Then the unique element
$g\in A$ determined either by the conditions of Proposition
\ref{pro: g} or by the conditions of Proposition \ref{pro: gg}
is called the {\em canonical grouplike element} of $A$.
\end{defi}
As one may suspect the canonical grouplike element is grouplike
in the sense of
\begin{defi}                               \label{grouplikeness}
An element $x$ of a WHA $A$ is called {\em grouplike} if
\bea
\cop(x)&=&x\1\c\o x\1\cc\ =\ \1\c x\o\1\cc x\label{grouplike1}\\
S(x)x&=&\1\ .\label{grouplike2}
\eea
\end{defi}
We remark that if (\ref{grouplike1}) holds then condition
(\ref{grouplike2}) is equivalent to the assumption that $x$ is
invertible.
One should emphasize that grouplike elements are not always like
group elements if a $^*$-operation is present. Namely we allow
for $x$ not to be unitary. Thus there can be positive grouplike
elements, for example, in a $C^*$-WHA.
 
If $x$ is
an invertible element factorizable as $x_Lx_R^{-1}$ with $x_L\in
A^L$ and $x_R=S(x_L)=S^{-1}(x_L)$ then $x$ is automatically
grouplike. As a matter of fact
$\cop(x)=x_L\1\c\o x_R^{-1}\1\cc=xx_R\1\c\o x_R^{-1}\1\cc=x\1\c\o
x\1\cc$. Now it follows from the next Lemma that the canonical
grouplike element $g$ is grouplike.
\begin{lem}
In a weak $C^*$-Hopf algebra $A$ the elements $h\ra\hat h$ and
$\hat h\la h$ are positive and invertible. The canonical grouplike
element of $A$ can be factorized as
\bea
g\ =\ g_Lg_R^{-1}\ ,&\qquad&\mbox{where}\label{eq: g=}\\
g_L:=(\hat h\la h)^{1/2}\ ,&\qquad& g_R=(h\ra\hat h)^{1/2}
\eea
\end{lem}
\Proof $\hat h\la h=E^L(h)=E^L(h^*h)\geq 0$
and similarly $h\ra\hat h\geq 0$
by positivity of the conditional expectations (\ref{eq: E^LR}).
Invertibility follows from the existence of the dual left integral
$\chi$ since $(h\ra\hat h)\la\chi=\duS(\hat h)(h\la\chi)=\hat h$
can hold for the non-degenerate $\chi$ and $\hat h$ only if
$h\ra\hat h$ is invertible. Thus $\hat h\la h=S(h\ra\hat h)$
is invertible, too.
 
The next point is to observe that the three elements $\hat h\la
h$,
$h\ra\hat h$, and $g$ commute with each other. For $g$ and any one
of the others this follows from the fact that $\hat h\la h$ and
$h\ra\hat h$ are invariant under $S^2$. For the commutativity of
the remaining two notice that one of them belongs to $A^L$ the
other to $A^R$. Now compare the following expressions:
\bea
\hat h&=&(h\ra\hat h)\la\chi\ =\ (h\ra\hat h)g\la\tau\ ,\\
\hat h&=&\duS^{-1}(\hat h)=\tau\ra g^{-1}(\hat h\la h)=g^{-1}(\hat
h\la h)\la\tau\ .
\eea
By non-degeneracy of $\tau$ we obtain
\beanon
(\hat h\la h)g^{-1}&=&(h\ra\hat h)g\\
(\hat h\la h)(h\ra\hat h)^{-1}&=&g^2
\eeanon
and taking the (positive) square root the Lemma is proven. \qed
 
\begin{lem}
The left--right components of the canonical grouplike element $g$
of $A$ and $\hat g$ of $\duA$ obey the following identities.
\bea
\hat g_L=\du1\ra g_L=\du1\ra g_R&\qquad&
g_L=\1\ra\hat g_L=\1\ra\hat g_R\\
\hat g_R=g_R\la\du1=g_L\la\du1&\qquad&
g_R=\hat g_R\la\1=\hat g_L\la\1\\
S(g_L)\ =\ g_R\ =\ S^{-1}(g_L)&\qquad&
\duS(\hat g_L)\ =\ \hat g_R\ =\ \duS^{-1}(\hat g_L)
\eea
\end{lem}
\Proof
Since $g_L\in A^L$ and $g_R\in A^R$, they commute and both of them
are invariant under $S^2=\Ad_g$. So are the $C^*$-algebras
generated by each of them, pointwise. Hence
$S(g_L^{1/2})^*=S^{-1}(g_L^{1/2})=S(g_L^{1/2})$ therefore
$S(g_L)=S(g_L^{1/2})^2\geq 0$. On the other hand
$S(g_L)^2=S(g_L^2)=g_R^2$, therefore $S(g_L)$ is the positive
square root of $g_R^2$, i.e. $S(g_L)=g_R$.
 
Next we want to show that $\du1\ra(\hat h\la
h)=h\la\hat h$. Since both hand sides belong to $\duA^L$, the
identity
\beanon
\bra\du1\ra(\hat h\la h),\,x^R\ket&=&\eps((\hat h\la h)S(x^R))=
\eps(\hat h\la hS(x^R))=\\
&=&\bra\hat h\ra h,\,S(x^R)\ket=\bra h\la\hat h,\,x^R\ket\ ,
\eeanon
valid for $x^R\in A^R$, suffices. Therefore $\du1\ra g_L^2=\hat
g_L^2$, or $\du1\ra g_R^2=\hat g_L^2$. Now use the fact that
$A^R\ni x^R\mapsto (\du1\ra x^R)\in\duA^L$ is a $^*$-algebra
isomorphism. Hence passing to the square roots we obtain $\1\ra
g_R=\hat g_L$. All the remaining identities are simple
consequences of this. \qed
 
 
\begin{prop}
Let $A$ be a $C^*$-WHA with dual $\duA$ and let $h\in A$, $\hat
h\in\duA$ be the corresponding Haar measures. Then
\begin{description}
\item[i)]
the modular automorphism of the Haar functional $\hat h$ is
implemented by $g_Lg_R$, i.e. for all $x\in A$ we
have $\theta_{\hat h}(x)=g_Lg_R\,x\,g_R^{-1}g_L^{-1}$;
\item[ii)]
the dual left integral of $h$ can be expressed as $\chi=\hat h\hat
g_R^{-2}$;
\item[iii)]
the $S$-invariant trace functional $\tau=g^{-1}\la\chi$ and
the Haar functional $\hat h$ are related by
\bea
\tau&=&\hat g_L^{-1}\hat h\hat g_R^{-1}\\
\hat h&=&g_Lg_R\la\tau
\eea
\end{description}
\end{prop}
\Proof {\bf i)}: Using identities like $\hat g_L\la
x=g_Rx,\dots$etc, which follow from Scholium \ref{sch: arrow}, one
can easily verify $\hat g\la x\ra \hat g=g_Lg_Rxg_R^{-1}g_L^{-1}$,
for $x\in A$.
 
{\bf ii)}: The identity $\hat h\la h=g_L^2=\1\ra\hat g_R^2$
implies $\1=\hat h\la h\ra\hat g_R^{-2}=\hat h\la hg_L^{-2}$,
hence $hg_L^{-2}=hg_R^{-2}$ is the dual left integral of
$\hat h$. By duality, $\hat h\hat g_R^{-2}$ is the dual left
integral $\chi$ of $h$.
 
{\bf iii)}: $\tau=g^{-1}\la\hat h\hat g_R^{-2}=\hat g_R^{-1}(\hat
h\hat g_R^{-2})\hat g_R=\hat g_L^{-1}\hat h\hat g_R^{-1}$ and
$\tau=g^{-1}\la(g_R^{-2}\la\hat h)=g_L^{-1}g_R^{-1}\la\hat
h$ completes the proof. \qed
 
Cyclicity and separability of the vector $h$ in the right
$A^{L,R}$-module $\LI$ (cf. Scholium \ref{ndeg}) allows us to
introduce $\duA^R$-valued "Radon-Nikodym derivatives" of left
integrals $l$ with respect to the Haar measure. At first note that
$l=\PL(h)l=hl=h\PR(l)=hS^{-1}(\PR(l))$ therefore using Scholium
\ref{sch: arrow} we have
\beq
\bra
\varphi,\,l\ket=\bra\varphi\rho_R,\,h\ket=\bra\rho_L\varphi,\,h\ket
\eeq
where $\rho_R=\PR(l)\la\du1$ and
$\rho_L=S^{-1}(\PR(l))\la\du1=\duS^2(\rho_R)$.
 
\begin{prop}
The bijections $\IL\to\duA^R$ provided by the
left and right Radon-Nikodym derivatives $l\mapsto\rho_L$ and
$l\mapsto\rho_R$, respectively, obey the following properties.
\begin{description}
\item[i)] $l$ is non-degenerate iff $\rho_{R,L}$ is invertible.
\item[ii)] If $l$ is non-degenerate then $l$ is normalized iff
$l^2=l$.
\item[iii)] $l$ is of positive type, i.e.
$\bra\varphi^*\varphi,l\ket\geq 0$ for all $\varphi\in\duA$, iff
$\PR(l)\geq 0$ iff $\rho_R\in\hat g_R^{1/2}\duA^R_+
\hat g_R^{-1/2}$ where $\duA^R_+$ is the cone of positive elements
in $\duA^R$. In this case $\rho_L=\rho_R^*$ and there
exists a $\xi\in\duA$ such that
$\bra\varphi,\,l\ket=\bra\xi^*\varphi\xi,\,h\ket$
for $\varphi\in\duA$.
\item[iv)] Let $\lambda$ be the dual left integral of $l$. Then
the Radon-Nikodym derivatives of $\lambda$ and $l$ are related by
$\PR(l)(\duPR(\lambda)\la\1)=g_R^{-2}$.
\end{description}
\end{prop}
\Proof {\bf i)} follows from cyclicity of $h$ in $\LI_{A^R}$.
{\bf ii)}: $l^2=l$ implies $(\PL(l)-\1)l=0$ and acting with
$\lambda\la$, where $\lambda$ is the dual left integral of $l$,
one obtains $\PL(l)=\1$. The converse implication is trivial.
{\bf iii)}: As in the proof of Theorem \ref{thm: C^* Haar} $l$ is
of positive type iff $S(l\c)\o l\cc$ belongs to the positive cone
(\ref{Pcone}). If it does then $\PR(l)=S(l\c)l\cc\geq 0$. Now
assume $\PR(l)\geq 0$. Then introducing $\xi=\PR(l)^{1/2}\la\du1$
we have
$\PR(l)^{1/2}=\xi\la\1$,
$S^{-1}(\PR(l)^{1/2})=S(\xi\la\1)^*=(\1\ra \duS^{-1}(\xi))^*=
\1\ra\xi^*$ therefore $l=hS^{-1}(\PR(l)^{1/2})\PR(l)^{1/2}=\xi\la
h\ra\xi^*$ proving that $l$ is of positive type. It remained to
reformulate positivity of $\PR(l)$ in terms of $\rho_R$.
Use the fact that the antimultiplicative map
$x^R\mapsto(x^R\la\du1)$ from $A^R$ to $\duA^R$ sends
the $^*$-operation into a new involution,
$x^{R*}\la\du1=(S^{-1}(x^R)\la\du1)^*=(S^{-2}(x^R)\la\du1)^*=
(g_Rx^Rg_R^{-1}\la\du1)^*=\hat g_R(x^R\la\du1)^*\hat g_R^{-1}$.
Therefore the equality $\PR(l)=x^{R*}x^R$ for some $x^R\in A^R$ is
equivalent to the equality $\rho_R=(x^R\la\du1)(x^{R*}\la\du1)=
\hat g_R^{1/2}\eta\eta^*\hat g_R^{-1/2}$ with $\eta=\hat
g_R^{-1/2}(x^R\la\du1)\hat g_R^{1/2}\in\duA^R$.
{\bf iv)} follows by an elementary calculus starting from the
identity $\1=\lambda\la l=\hat h\duPR(\lambda)\la
hS^{-1}(\PR(l))$. \qed
