---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-008-the-space-of-star-products-on-the-poincaré-orbit
section_title: "The space of star products on the Poincaré orbit M:=SO(1,1)R2/R"
section_number: null
pages: 11-13
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.994
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
It is proven in \cite{Bi07} that every Poincar\'e invariant star product on $\MM$ is realized as
a formal  asymptotic expansion in powers of $\hbar$ of an oscillatory integral expression in terms of the geometrical quantities defined above:
\begin{equation*}
u\,\star_{\hbar,{\cal P}} \,v\,(x_0)\;=\;\frac{1}{\hbar^2}\,\int_{\MM\times \MM}\,\sqrt{\mbox{\rm Jac}_{\Phi}(x_0,x_1,x_2)}\,e^{\frac{i}{\hbar}\,S^{(\MM)}_{\mbox{\rm can}}(x_0,x_1,x_2)}\,\frac{{\cal P}(a_0-a_1){\cal  P}(a_2-a_0)}{{\cal  P}(a_1-a_2)}\,u(x_1)\,v(x_2)\,{\rm d}x_1\,{\rm d}x_2\;;
\end{equation*}
where ${\rm d}x$ denotes the Liouville symplectic measure on $M$ and where $\cal P$ is an essentially arbitrary nowhere vanishing complex-valued one variable function possibly depending smoothly in the real deformation
parameter $\hbar$. The function $\cal P$
therefore being the only degree of freedom (see \cite{Bi07} for details).

\noindent We now briefly recall how the above result is obtained. The key point relies in the fact that the global Darboux coordinate system $(a,\ell)$ on $\SS$ enjoys a property of compatibility with 
the hyperbolic action of $G:=SL_2(\R)$ on $\DD=\SS$. 

\noindent In the case $\LL$ is a Lie group with Lie algebra $\mathfrak{l}$ that acts on a symplectic manifold $(M,\omega)$ in a Hamiltonian manner, a 
(not necessarily $\LL$-invariant) star product $\star$ on $(M,\omega)$  is called {\sl $\mathfrak{l}$-covariant}
if, denoting by
\begin{equation}
\lambda:\mathfrak{l}\longrightarrow C^\infty(M): X\mapsto \lambda_X
\end{equation}
the associated (dual) moment mapping, the following equalities hold:
\begin{equation}
\frac{i}{\hbar}\,[\,\lambda_X\,,\,\lambda_Y\,]_\star\;:=\;\frac{i}{\hbar}\,(\lambda_X\star\lambda_Y-\lambda_Y\star\lambda_X)\;=\;\{\,\lambda_X\,,\,\lambda_Y\,\}\;=\;\lambda_{[X,Y]}
\end{equation}
for all $X,Y\in\mathfrak{l}$. 

\noindent In this situation, one has a representation of $\mathfrak{l}$ on $C^\infty(M)[[\hbar]]$
by derivations of the star product $\star$:
\begin{eqnarray}
\rho_\hbar:\mathfrak{l}&\longrightarrow&\mathfrak{Der}(\star)\\
\rho_\hbar(X)\,u&:=&\frac{i}{\hbar}\,[\,\lambda_X\,,\,u\,]_\star\;.
\end{eqnarray}

\vspace{2mm}

\noindent It turns out that in coordinates $(a,\ell)$ the Moyal product (\ref{asympt}) is $\mathfrak{sl}_2(\R)$-covariant
with respect to the hyperbolic action of $G:=SL_2(\R)$ on the hyperbolic plane $\DD=\SS$ \cite{Bithese}. Precisely, presenting the Lie algebra $\gg:=\mathfrak{sl}_2(\R)$ as generated over $\R$ by $H, E$ and $F$ satisfying:
\begin{equation}
 [H,E] = 2E \quad,\quad [H,F] = -2F \quad,\quad [E,F] = H,\label{HEF}
 \end{equation}
the moment map associated with the action of $G$ on $\DD=G/K=\SS$ reads:
\begin{equation}\label{moments}
\lambda_H=\sqrt{k}\,\ell\,;\,\lambda_E=\frac{\sqrt{k}}{2}e^{-2a}\,;\,\lambda_F=-\frac{\sqrt{k}}{2}e^{2a}(1+\ell^2)\;.
\end{equation}
The associated fundamental vector fields are given by:
\begin{equation}\label{fundamental}
 H^\star = -\partial_a; \, E^\star = -e^{-2a}\partial_\ell;  \,
 F^\star= e^{2a}(\ell \partial_a - (k+\ell^2) \partial_\ell)\;.
 \end{equation}
At last, the representation of $\gg$ by derivations of $\star^0_\hbar$ admits the expression:
\begin{eqnarray}
\rho_{\hbar } (H) &=& -\partial_a \\
\rho_{\hbar }(E) &=& -\frac{e^{-2a}}{ \hbar } \sin ( \hbar \partial_\ell) \\
\rho_{\hbar }(F) &=&
 e^{2a}\left(\frac{\hbar  }4\sin ( \hbar \partial_\ell)\partial_a^2+
  \ell\cos ( \hbar \partial_\ell)\partial_a-(k+\ell^2)\frac{\sin ( \hbar \partial_\ell)}\hbar
\right)\;.\label{lambdaF} 
\end{eqnarray}
We now consider the partial Fourier transform in the $\ell$-variable
\begin{equation}
{\cal F}(\varphi)(a,\zeta) = \int_{-\infty}^\infty e^{-i \zeta \ell} \varphi(a, \ell) {\rm d}\ell \quad,
\end{equation}
and denote by $\tilde{\SS}:=\{(a,\zeta)\}$ the space where the Fourier transformed $\cf(g)$ is defined on.
\noindent Defining the following one-parameter family of diffeomorphisms of $\tilde{\SS}$:
\begin{equation}
\phi_\hbar  (a,\zeta) = \left(a,\frac{\sinh (\hbar\, \zeta)}{\hbar}\right) \quad ,
\end{equation}
and denoting by $\tilde{\cs}$ (resp. $\cs$) the space of Schwartz test functions $\cs(\tilde{\SS})$
(resp. $\cs({\SS})$) on $\tilde{\SS}=\{(a,\zeta)\}$ (resp. on $\cs(\SS)$ of $\SS=\{(a,\ell)\}$), one observes the following inclusions:
\begin{equation}
\phi_\hbar^\star\,\tilde{\cs}\,\subset\,\tilde{\cs}\;\mbox{\rm and }\,\tilde{\cs}\,\subset\,(\phi_\hbar^{-1})^\star\tilde{\cs}\,\subset\,\tilde{\cs}'\;.
\end{equation}
Therefore, every data of (reasonable) one parameter smooth family of invertible functions $\cp_\hbar=\cp_\hbar(b)$ yields an operator on the Schwartz space 
$\cs(\SS)$ of $\SS=\{(a,\ell)\}$:
\begin{equation}
T^{-1}:\cs(\SS)\longrightarrow\cs(\SS)
\end{equation}
defined as 
\begin{equation}\label{OpT}
T^{-1} \varphi(a_0,\ell_0)= \frac{1}{2\,\pi } \int \, e^{i\zeta \ell_0}\, \PP_\hbar(
\zeta)\, e^{\frac{-i}{\hbar}\ell \sinh(\hbar \zeta )} \, \varphi(a_0,\ell) \, {\rm d}\ell\,
{\rm d}\zeta\;.
\end{equation}
More generally, denoting by $\cm_f$ the pointwise multiplication operator by $f$, the  operator:
\begin{equation}
T:\cs(\SS)\longrightarrow\cs'(\SS)
\end{equation}
defined as
\begin{equation}
T\;:=\;\cf^{-1}\,\circ\,(\phi_\hbar^{-1})^\star\,\circ\cm_{\frac{1}{\cp}}\,\circ\cf
\end{equation}
is a left-inverse of $T^{-1}$.
Intertwining Moyal-Weyl's product by $T$ yields the above  product as $\star_{\hbar,{\cal P}} =T(\star^0_\hbar)$. Observe that the latter closes on the range space $\ce_\hbar:=T\cs$
yielding a (non-formal) one parameter family of associative  function algebras: $(\ce_\hbar,\star_{\hbar,{\cal P}} )$. Asymptotic expansions of these non-formal products produce
genuine Poincar\'e-invariant formal star products on $\MM$ \cite{BBM}.

\vspace{2mm}

\noindent For generic $\cal P$ the above oscillatory integral product defines, for all real {\sl value} of $\hbar$, an associative product law on some function space (as opposed to formal power series space) on $\MM$. The most remarkable case being probably the one where $\cal P$ is pure phase. In the latter case, the above
product formula extends (when $\hbar\neq0$) to the space $L^2(\MM)$ of square integrable functions as a Poincar\'e invariant Hilbert associative algebra. The star product there appears to be {\sl strongly closed}: for all
$u$ and $v$ in $L^2(\MM)$, $u\,\star_{\hbar,{\cal P}} \,v$ belongs to $L^1(\MM)$, and one has:
\begin{equation*}
\int_\MM u\,\star_{\hbar,{\cal P}} \,v\;=\;\int_\MM u\,v\;.
\end{equation*}

\vspace{3mm}

\noindent The contracted situation is therefore, to some extent, relatively well understood.
