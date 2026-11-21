---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-009-sl2r--triplets-of-derivations-and-an-unexpected
section_title: "sl2(R)- triplets of derivations and an unexpected Lorentzian structure"
section_number: null
pages: 13-13
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.984
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
\noindent Let us now consider {\sl any} Poincar\'e invariant formal star $\star$ product on the contracted plane $\MM$. Denote
by $\Der(\star)$ its algebra of derivations. Note that from formal equivalence with Moyal, every derivation is interior.
Consider in $\Der(\star)$ any element $D$ with the property that $D,H^\star$ and $E^\star$ form an $\mathfrak{sl}_2(\R)$-triplet of $\star$-derivations. The crucial point which the entirety of the present paper relies on resides now in the following totally unexpected fact:

\vspace{3mm}

\noindent {\sl Intertwining the derivation $D$ by the partial Fourier transform yields a second order hyperbolic differential operator $\Box\,:=\,\cf\,\circ\,D\,\circ\,\cf^{-1}$ whose principal symbol defines a Lorentzian metric which does not depend on any particular  choice made (of $\star$, $\mathfrak{sl}_2(\R)$-triplet derivation algebra and $D$)}.

\vspace{3mm}

\noindent The latter Lorentzian metric is therefore a new object that is canonically associated with the hyperbolic
plane, its canonical contraction and their quantization.

\vspace{3mm}

\noindent To prove the above assertion we first observe that the above covariance property implies that
the operator 
\begin{equation}\label{DERIV}
D_0\;:=\;T\circ\rho_\hbar(F)\circ T^{-1}
\end{equation}L
is a derivation of $\star:=T(\star^0)$. Now the particular choice of 
\begin{equation}
\cp(\zeta)\;\equiv1
\end{equation}
yields the following 
expression for $\Box:=\cf\,\circ\,D_0\,\circ\,\cf^{-1}$ that appears to be a second order differential operator:
\begin{eqnarray}\label{box1}
 \Box_{(a,\zeta)} = i e^{2a} \left[   \frac{\hbar^2}4\,\zeta\,
\partial_a^2 + \zeta\, (1+\hbar^2\, \zeta^2) \partial_\zeta^2 + (1+\hbar ^2
\, \zeta^2) \partial_a \partial_\zeta + \hbar^2 \,\zeta\, \partial_a  +  (2 + 3 \hbar^2 \, \zeta^2)
\partial_\zeta - \zeta\,(k-\hbar^2) \right] \;.\label{Box0}
\end{eqnarray}
Note the occurrence of the Lorentzian metric on $\tilde{\SS}$:
\begin{equation}
[g^{ij}]\;:=\;e^{2a}(1+\hbar ^2
\, \zeta^2) \,\left(
\begin{array}{cc}
 \frac{\hbar^2}4\,\frac{\zeta}{(1+\hbar ^2
\, \zeta^2) } & 1\\
1 & \zeta
\end{array}
\right)\;.
\end{equation}
Now, consider an arbitrary Poincar\'e invariant star product $\star$ on $\MM$. Note  that, denoting by $\ss$ the Lie algebra of $\SS$, the above Moyal-covariance property yields a $\ss$-quantum moment for $\star $ i.e. a linear map $\mathfrak{sl}_2(\R)\to C^\infty(\MM)[[\hbar]];X\mapsto\Lambda_X$ such that $\frac{1}{2\hbar}[\Lambda_X,\Lambda_Y]_\star=\Lambda_{[X,Y]}$ and $V^\star=\frac{1}{2\hbar}[\,\Lambda_V\,,\,.\,]$
for all $V\in\ss$. Fix $D_0$ in $\Der(\star)$ with the same property as $D$ and set $D=:D_0+D_1:=:D_0+[\lambda_1\,,\,.\,]$
with $\lambda_1\in C^\infty(\MM)[\hbar^{-1},\hbar]]$ (one knows from the equivalence with Moyal that $\Der(\star)$ is interior). The triplet condition yields the following conditions: $[E^\star,D_1]=0$ and $[H^\star,D_1]=-2D_1$.
The implies $\frac{1}{2\hbar}[\Lambda_E,\lambda_1]=E^\star.\lambda_1=c_E$ and $H^\star.\lambda_1=-2\lambda_1+c_H$ where $c_E$ and $c_H$ are formal constants. From the expressions (\ref{fundamental}),
one gets $\lambda_1=-c_Ee^{2a}\ell+const.$ i.e. $D=D_0+c_\hbar\,[e^{2a}\ell\,,\,.\,]_\star$ where $c_\hbar\in\C[\hbar^{-1},\hbar]]$. We now argue that the operator 
$\cf D_1\cf^{-1}:=\cf \circ c_\hbar\,[e^{2a}\ell\,,\,.\,]_\star\circ\cf^{-1}$ is differential and at most first order.
Indeed, starting with $D_0:=T^{-1}\rho_\hbar(F)T$ where $\star=T(\star^0)$, one observes by looking a the expression (\ref{moments}) of the classical moment that $D$ exactly corresponds to $\lambda_F$ affected by a 
translation in $\ell)$: $(a,\ell)\mapsto(a,\ell +c)$\footnote{Note that this symplectic transformation leaves Moyal' star product invariant.} (and a re-definition of $k$). From expression (\ref{lambdaF}), one 
deduces that $TD_1T^{-1}$ is a linear combination of $\cos(\hbar\partial_\ell)$,  
and $\ell\sin(\hbar\partial_\ell)$. The latter correspond under the $T$ equivalence to multiplication and 
vector fields operators. To complete the argument, we end by observing (see \cite{Bi07}) that one passes from one 
Poincar\'e invariant star product $\star'$ to $\star$ by an equivalence of the form $\cf^{-1}\circ\cm_{Q}\circ\cf$ where 
$\cm_Q$ denotes the multiplication operator by a one variable (formal) function $Q=Q(\xi)$ independent of $s$.
The latter has the effect of a simple gauge transformation affecting $\Box$ only by lower order terms.
