---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-006-admissible-functions-on-symplectic-symmetric-sur
section_title: "Admissible functions on symplectic symmetric surfaces"
section_number: null
pages: 8-11
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.985
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
In \cite{WeinsteinTr}, Alan Weinstein conjectures the relevance of a certain three-point function, here denoted
$S_W$, as the essential constituent of the phase of an oscillatory kernel defining an invariant star product
on the hyperbolic plane $\DD$ or more generally on any (reasonable) symplectic symmetric space $\co=G/K$. Essentially, when three points $x,y$ and $z$ in $\co$ are close enough to one another, Weinstein
function $S_W=S_W(x,y,z)$ is defined as the symplectic area of the geodesic (defined by the Loos connection) triangle
in $\co$ admitting points $x,y,z$ as mid-points of its geodesic edges.

 
\begin{figure}[h] 
   \centering
   \includegraphics[scale=1]{Picture1.pdf} 
   \caption{Contraction of the Kaehler orbit into a non-metric hyperbolic cylinder.}
   \label{Figure 1}
\end{figure}



\noindent Additionally to its invariance under the symmetries, the three-point function $S_W$ (when defined)
has been shown in \cite{PierreStrict} to satisfy  the following so-called admissibility condition (\ref{ADM}). 

\noindent A three-point function
$S\in C^\infty(\co\times\co\times\co,\R)$ is called {\sl admissible} if it is invariant under the diagonal action of the symmetries on $\co\times\co\times\co$, is totally skewsymmetric, and if it satisfies the following property:
\begin{equation}\label{ADM}
S(x,y,z)=-S(x,s_{x}y,z)\;.
\end{equation}
As it will appear, the above condition is in fact the crucial one regarding star-products. 

\noindent In the case of a symplectic symmetric surface, every such (regular) admissible function turns out to 
coincide with an odd function of a {\sl canonical} admissible function. The latter function denoted hereafter $S_{\mbox{\rm can}}$ is defined in terms of the co-adjoint orbit realization of the symplectic symmetric surface
at hand. We now explain how to define it. 

\noindent Locally, every geodesic line
starting at the base point $o:=K$ and ending at $x$ can be realized as the (parametrized) orbit of $o$ by a one-parameter 
subgroup $\exp(tX)$ of $G$ with $X\in\pp$ ( see e.g. \cite{helgason} ). An invariant totally skewsymmetric smooth function $S\in C^\infty(\co^3)$ will be called {\sl regular admissible } if $S(o,x,y)=S(o,x,\exp(tX).y)$,
for all $t\in\R$ and $y\in\co$. Observe that regular admissibility implies admissibility as a consequence of the
following classical identity:
\begin{equation}
\exp(X)\;=\;s_{\mbox{\rm Exp}_o(\frac{1}{2}X)}\,\circ\, s_o\qquad(X\in\pp)
\end{equation}
where $\mbox{\rm Exp}_o$ denotes the exponential mapping at point $o$ with respect to the 
canonical connection.
The inclusion $\pp\subset\gg$ induces a linear projection  $\Pi:\gg^\star\to\pp^\star$. The dual space
$\pp^\star$ naturally carries a (constant) symplectic 2-form here denoted again by $\Omega$. Identifying 
points with vectors in $\pp^\star$, given two points $\xi$ and $\eta$, the quantity $\Omega(\xi,\eta)$
therefore represents the flat symplectic area of the (flat) Euclidean triangle in $\pp^\star$ admitting
points $0,\xi$ and $\eta$ as vertices. By transversality, the restriction  of the projection $\Pi$ to 
the co-adjoint orbit $\co\subset\gg^\star$ is locally (around $o$) a diffeomorphism.  Denoting by $\frac{x}{2}$ the unique point in a small neighbourhood of $o$ such that $s_{\frac{x}{2}}o=x$,
the following formula:
\begin{equation*}
S_{\mbox{\rm can}}(x,y,z)\;:=\;\Omega(\,\Pi(s_{\frac{x}{2}}(y))\,,\,\Pi(s_{\frac{x}{2}}(z))\,)
\end{equation*}
defines a (local) regular admissible function on $\co$. In the case where the surface $\co$ is of group type, the function $S_{\mbox{can}}$ is globally defined and smooth. 
Moreover every regular admissible function is an odd function of $S_{\mbox{can}}$. 

\begin{figure}[h] 
   \centering
   \includegraphics[scale=1]{Picture2.pdf} 
   \caption{The canonical three-point phase obtained from projecting the orbit.}
   \label{Figure 2}
\end{figure}
\noindent The proof essentially relies in the fact that the $\Pi$-projected $\exp(tX)$-orbits in $\co$ exactly
coincide with {\sl straight lines} in $\pp^\star$. Indeed, 
we first observe that the 
diffeomorphism $\Pi$ establishes a bijection between the 
$\exp(tX)$-orbits ($X\in\pp$) in $\co$ and the straight lines
in $\pp^\star$. Indeed, for $x\in\co$ and $X\in\pp$, one has $<\mbox{\rm Ad}^\star(\exp(tX))x-x,X>=0$, where 
$\mbox{\rm Ad}^\star$ denotes the co-adjoint action. Which means
that the $x$-translated  $\exp(tX)$-orbit of $x$ lies in the plane in $\gg^\star$ orthodual to $X\in\pp$.
This plane is generated by the kernel $\kk^\star$ of the projection $\Pi:\gg^\star\to\pp^\star$ and 
an element $X^\perp$ of $\pp^\star$ orthodual to $X$. In particular, it projects onto the line 
directed by $X^\perp$.
\noindent Now consider the two-point function $\kappa(x,y):=S(o,x,y)$ on $M$ induced by the data of an 
admissible function $S$ on $M$. This function corresponds to a two-point function $\kappa^0$ on $\pp^\star$
via the diffeomorphism $\Pi$. By admissibility and the above observation, one has
$\kappa^0(\xi,\eta)=\kappa^0(\xi,\eta+t\xi)$ for all $t\in\R$. Which is precisely the property of admissibility
for a two-point function with respect to the flat structure on $\pp^\star$. The rest then follows from Proposition 3.3 in \cite{PierreStrict}.

\vspace{3mm}

\noindent It is remarkable that in the case of Poincar\'e orbit $\MM$ the equation $s_xs_ys_zt=t$ admits a 
unique solution $t$ for all data of three points $x,y$ and $z$ in $\MM$. Moreover, the `double triangle' mapping\footnote{
Within A. Weinstein terminology.}:
\begin{equation*}
\Phi: \MM\times  \MM\times  \MM\to  \MM\times  \MM\times  \MM:(x,y,z)\mapsto(t,s_zt,s_ys_zt)
\end{equation*}
is a global diffeomorphism whose jacobian determinant equals
\begin{equation*}
\mbox{\rm Jac}_{\Phi}(x_{0},x_1,x_2)\;=\;16\,\cosh(2(a_0-a_1))\,\cosh(2(a_1-a_2))\,\cosh(2(a_2-a_0))\;.
\end{equation*}
\begin{figure}[h] 
   \centering
   \includegraphics[scale=1]{Picture3.pdf} 
   \caption{The double geoedesic triangle.}
   \label{Figure 3}
\end{figure}

This is a straightforward computation based on the following formulas for the symmetries:
\begin{equation}\label{symPpl}
s^{\MM}_{(a,\ell)}(a',\ell')\,=\,(\,2a-a'\,,\,2\cosh(2(a-a'))\ell\,-\,\ell'\,)\;,
\end{equation}
as well as for the mid-point map:
\begin{equation}\label{midPpl}
m: \MM\times  \MM\to  \MM:(x,y)\mapsto m(x,y)=\left(\;\frac{1}{2}(a_x+a_y)\;,\;\frac{1}{2}(\ell_x+\ell_y)\sech(a_x-a_y)\;\right)\;,
\end{equation}
defined by the relation
\begin{eqnarray*}
s^{\MM}_{m(x,y)}x=y\;.
\end{eqnarray*}
One has 
\begin{equation*}
\Phi^{-1}(x,y,z)=(m(x,y),m(y,z),m(z,x))\;;
\end{equation*}
and a computation yields
\begin{equation*}
\mbox{\rm Jac}_{\Phi^{-1}}(x_0,x_1,x_2)=\frac{1}{16}\sech(a_0-a_1)\sech(a_1-a_2)\sech(a_2-a_0).
\end{equation*}
One then obtains the announced formula by using the relation: 
$\mbox{\rm Jac}_{\Phi}=(\Phi^\star\mbox{\rm Jac}_{\Phi^{-1}})^{-1}$.

\noindent At last, the canonical admissible three-point function, in this particular situation of $\MM$, exactly coincides
with Weinstein's function:
\begin{equation*}
S^{( \MM)}_{\mbox{\rm can}}\;=\;\mbox{ \rm Symplectic Area of } \Phi\;=\;S^{( \MM)}_W\;.
\end{equation*}
In coordinates, one has 
\begin{equation*}
S^{( \MM)}_{\mbox{\rm can}}(x_0,x_1,x_2)\;=\;\sinh(2(a_0-a_1))\,\ell_2+\,\sinh(2(a_2-a_0))\,\ell_1+\,\sinh(2(a_1-a_2))\,\ell_0\;.
\end{equation*}

\vspace{3mm}

\noindent In the hyperbolic plane case, however, the situation is not as nice. Indeed, a bit of reflection leads to the fact that Weinstein's
function is not well-defined for every triple of points $x,y$ and $z$ in $\DD$. In particular, since by construction $S^{(\DD)}_{\mbox{\rm can}}$ is smooth it must differ from $S^{(\DD)}_W$. Nevertheless, as proven above,
they should locally be odd functions of each other. Precisely, one has the relation:
\begin{equation*}
S^{(\DD)}_W\;=\;\pi-2\arccos(S^{(\DD)}_{\mbox{\rm can}})\;.
\end{equation*}
We set 
\begin{equation}\label{fW}
f_W(t)\;:=\; \pi-2\arccos(t)\;.
\end{equation}
In terms of the Kaehler potential $\zeta$ of the hyperbolic plane realized as the Poincar\'e unit disc, one has 
\begin{equation*}
S^{(\DD)}_{\mbox{can}}(0,z,w)\;=\;4\,\zeta(z)\,\zeta(w)\,\mbox{\rm Im}(z\overline{w})\,.
\end{equation*}
In coordinates, one has
\begin{equation}
S^{(\DD)}_{\mbox{can}}(0,x_0,x_1)=\ell_1 \sinh 2 a_0 -\ell_0\sinh 2 a_1 + \frac{\ell_0
\ell_1}{2}(\ell_0 e^{2 a_0} -\ell_1e^{2 a_1})\;.
\end{equation}
\noindent As we will see in the sequel, the 3-point kernel defining the associative  deformation product in the case of the hyperbolic plane turns out to be expressed as a special function (of one real variable) of the function $S_{\mbox{\rm can}}$ only (no approximation). While in the solvable contracted case, the latter coincides (up to a co-boundary) with the phase of the quantization kernel. This canonical function therefore appears as a unifying notion for  both contracted and un-contracted situations.
