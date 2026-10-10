---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-003-symplectic-symmetric-spaces
section_title: "Symplectic symmetric spaces"
section_number: null
pages: 4-7
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
text_source: latex
latex_prose_ratio: 0.628
latex_coverage_ratio: 0.928
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
\label{Symsymspa}
\subsection{Definitions and elementary properties}\label{DefandProp}
Everything in this subsection is entirely standard and can be found e.g. in \cite{Bithese} and references therein.
A {\sl symplectic symmetric space} is a triple $(M,\omega,s)$ where $M$ is a connected smooth manifold
endowed with a non-degenerate two-form $\omega$ and where 
\begin{equation*}
s:M\times M\to M:(x,y)\mapsto s(x,y)=:s_xy
\end{equation*}
is a smooth map such that for all point $x$ in $M$, the partial map:
$s_x:M\to M$ is an involutive  diffeomorphism 
of $M$ (i.e. $s_x^2=\mbox{\rm id}_M$) which preserves the two-form $\omega$ (i.e. $s_x^\star\omega=\omega$)
and which admits $x$ as an isolated fixed point. On furthermore requires the following property:
\begin{equation*}
s_xs_ys_x\;=\;s_{s_xy}
\end{equation*}
to hold for any pair of points $(x,y)$ in $M\times M$.
In this situation, the space $M$ is endowed with a preferred affine connection. Indeed, 
for every triple of tangent vector fields $X,Y$ and $Z$ on $M$,
the following formula:
\begin{equation*}
\omega_x(\,\nabla_XY\,,\,Z\,)\;:=\;\frac12 X_x.\omega(\,Y\,+\,s_{x\star}Y\,,\,Z)
\end{equation*}
defines\footnote{See \cite{Bithese} and appendix \ref{AppenB} for an explicit computation in the case of generic coadjoint orbits of the Poincar\'e (1,1) group.} a torsion-free affine connection $\nabla$ on $M$ that enjoys the properties of being preserved by every 
{\sl symmetry} $s_x$ as well as being compatible with $\omega$ in the sense that:
\begin{equation*}
\nabla\omega=0\;.
\end{equation*}
This last fact implies in particular that $\omega$ is closed, turning it into a {\sl symplectic} form on $M$.

\vspace{2mm}

\noindent An important class of symplectic symmetric spaces is constituted by the non-compact {\sl Hermitean 
symmetric spaces}. Such a space is a coset space $M=G/K$ of a non-compact simple Lie group $G$ by
a maximal compact subgroup $K$ that admits a non-discrete center $Z(K)$. The first example
being the hyperbolic plane $\DD:=\mbox{SL}_2(\R)/\mbox{SO}(2)$.  The compactness of $K$ implies
in particular that a Hermitean symmetric space admits a $G$-invariant Riemannian metric for which
the connection $\nabla$ is the Levi-Civita connection. 

\noindent However, in general a symplectic symmetric space
needs not to be Riemannian, even not pseudo-Riemannian, in the sense that there is in general {\sl no} metric tensor $g$ on $M$ such that $\nabla g=0$. In this sense a symplectic symmetric space is a purely 
symplectic object. In the problem we are concerned with in the present work, such a ``non-metric"
symplectic symmetric space will play a central role.

\vspace{2mm}

\noindent Two symplectic symmetric spaces $(M_i,s^{(i)},\omega^{(i)})$ $(i=1,2)$ are said {\sl isomorphic}
is there exists a diffeomorphism $\varphi:M_1\to M_2$ that is symplectic i.e. such that $\varphi^\star\omega^{(2)}=\omega^{(1)}$ and that intertwines the symmetries: $\varphi s^{(1)}_x\varphi^{-1}=s^{(2)}_{\varphi(x)}$ for all $x$ in $M^{(1)}$. Given a symplectic symmetric space $(M,\omega,s)$,
its {\sl automorphism  group} $\mbox{\rm Aut}(M,\omega,s)$ therefore turns out to be the intersection of the diffeomorphism group
of affine transformation of $(M,\nabla)$ with the symplectic group of $(M,\omega)$:
\begin{equation}
\mbox{\rm Aut}(M,\omega,s)\;=\;\mbox{\rm Aff}(\nabla)\,\cap\,\mbox{\rm Symp}(\omega)\;.
\end{equation}
The latter group is therefore a (finite dimensional) Lie group of transformations of $M$. One 
then  shows that since it contains the symmetries $\{s_x\}_{x\in M}$ its action on $M$ is transitive,
turning $(M,\omega)$ into a {\sl homogeneous symplectic space}. In particular, every symplectic 
symmetric space is a coset space.

\vspace{2mm}

\noindent Up to isomorphism, the list of homogeneous spaces underlying simply connected 2-dimensional symplectic symmetric spaces is the following:
\begin{enumerate}
\item$\mbox{\rm the flat plane}: \R^2$
\item$\mbox{\rm the hyperbolic plane}: \DD\;:=\;SL_2(\R)/SO(2)$
\item$\mbox{\rm the universal covering space of the anti-de Sitter surface}: \widetilde{\mbox{\rm AdS}_2}:=\widetilde{SL_2(\R)/SO(1,1)}$
\item$\mbox{\rm the sphere}: S^2:=SO(3)/SO(2)$
\item$\mbox{the universal covering space of the Galileo coset}: \widetilde{SO(2)\times\R^2}/\R$
\item$\mbox{the Poincar\'e coset}: \MM:=SO(1,1)\times\R^2/\R$.
\end{enumerate}
Items 5 and 6 provide the first examples of non-metric symplectic symmetric spaces.

\noindent A old classical result independently due to Kirilov and Kostant \cite{Kos,Kir} asserts that every simply connected homogeneous symplectic
space is isomorphic to the universal covering space of a co-adjoint orbit of some Lie group. In our situation
of symplectic symmetric spaces this can be easily visualized. Indeed, fixing a base point $o\in M$ the conjugation
\begin{equation}
\tilde{\sigma}:\mbox{\rm Aut}(M,\omega,s)\to\mbox{\rm Aut}(M,\omega,s):g\mapsto\tilde{\sigma}(g):=s_ogs_o
\end{equation}
defines an involutive automorphism of the group $\mbox{\rm Aut}(M,\omega,s)$. Its differential at the unit
element therefore yields an involutive automorphism at the Lie algebra level:
\begin{equation}
\sigma:=\tilde{\sigma}_{\star e}:\mathfrak{aut}(M,\omega,s)\to\mathfrak{aut}(M,\omega,s)
\end{equation}
where $\mathfrak{aut}(M,\omega,s)$ denotes the Lie algebra of the automorphism group.
The latter Lie algebra therefore decomposes into a direct sum of ($\pm 1$)-eigenspaces for $\sigma$:
\begin{equation}
\mathfrak{aut}(M,\omega,s)\;=\;\kk\oplus\pp\;.
\end{equation}
Note that the differential at $e$ of the coset projection: $\pi:\mbox{\rm Aut}(M,\omega,s)\to M$
when restricted to the ($-1$)-eigensubspace $\pp$ provides a linear isomorphism with the tangent space at $o$:
\begin{equation}
\pi_{\star e}|_\pp:\pp\tilde{\longrightarrow}T_o(M)\;.
\end{equation}
The pull back of the symplectic structure at $o$ therefore defines a symplectic bilinear two-form on $\pp$:
\begin{equation}
\Omega\;:=\;(\pi_{\star e}|_\pp)^\star\,\omega_o\;.
\end{equation}
When extended by zero to the entire $\mathfrak{aut}(M,\omega,s)$ the element $\Omega$ is easily seen
to be a {\sl Chevalley 2-cocycle} in the sense that:
\begin{equation}
\Omega([X,Y],Z)+\Omega([Z,X],Y)+\Omega([Y,Z],X)=0\;.
\end{equation}
The 2-cocycle $\Omega$ needs in general not to be exact at the level of the automorphism algebra $\mathfrak{aut}(M,\omega,s)$. That is there does not always exist a linear form $\xi_o$
on $\mathfrak{aut}(M,\omega,s)$ such that 
\begin{equation}\label{XI}
\Omega(X,Y)\;=\;\xi_o[X,Y]\;.
\end{equation}
Note nevertheless that the only 2-dimensional non-exact case corresponds
to the flat plane $\R^2$. 

\noindent We now adopt the notation
\begin{equation}
G\;:=\mbox{\rm Aut}(M,\omega,s)\;;\quad\gg\;:=\;\mathfrak{aut}(M,\omega,s)\;.
\end{equation}
Denoting by $K$ the stabilizer subgroup of $G$ of the base point $o$, one gets the $G$-equivariant identification
\begin{equation}
G/K\longrightarrow M: gK\mapsto go\;,
\end{equation}
where the symmetry map reads
\begin{equation}
s_{gK}(g'K)\;=\;g\tilde{\sigma}(g^{-1}g')\,K\;.
\end{equation}
It turns out that the 2-cocycle $\Omega$ is exact if and only if the action of $G$ on $(M,\omega)$
is {\sl Hamiltonian} in the sense that, endowing $C^\infty(M)$ with the Lie algebra structure defined
by the Poisson bracket associated to the symplectic structure $\omega$, 
there exists a Lie algebra map
\begin{equation}
\lambda: \gg\longrightarrow C^\infty(M):X\mapsto\lambda_X
\end{equation}
that satisfies the following property:
\begin{equation}
\{\lambda_X,f\}(x)\;=\;\frac{d}{dt}|_{t=0}f(\exp(-t X)x)\;=:\;X^\star_x.f
\end{equation}
for all function $f\in C^\infty(M)$.
Note that the map $\lambda$ is then necessarily {\sl $G$-equivariant} in the sense that
\begin{equation}
\lambda_{\mbox{Ad}(g)X}(x)\;=\;\lambda_X(gx)
\end{equation}
for all $g\in G$, $X\in\gg$ and $x\in M$.

\noindent When Hamiltonian, one may choose:
\begin{equation}
\xi_o(X)\;:=\lambda_X(o)\;.
\end{equation}
In that case, denoting by $\co$ the co-adjoint orbit of the element $\xi_o\in\gg^\star$,
the {\sl moment mapping}:
\begin{equation}
J: M\longrightarrow\co\subset\gg^\star:x\mapsto[J(x):\gg\to\R:X\mapsto\lambda_X(x)]
\end{equation}
realizes a $G$-equivariant covering from $M$ onto the co-adjoint orbit $\co$. Note that the co-adjoint orbit
$\co$ is itself endowed with a canonical symplectic structure $\omega^\co$ defined at the level
of the fundamental vector fields for the co-adjoint action by
\begin{equation}
\omega^\co_\xi(X^\star,Y^\star)\;:=\;\xi[X,Y]\qquad(\xi\in\co)\;.
\end{equation}
With respect to the latter structure the moment map $J:M\to\co$ is symplectic. 

\vspace{2mm}

\noindent When non-exact, a passage to a central extension of  $\gg$ yields an entirely
similar situation. Indeed, the transvection group (generated by all the $s_x \circ s_y$ and forming a normal subgroup of Aut$(M)$ ) does not act in a strongly Hamiltonian manner on $M$.
However, one may consider the (non-split) central extension $0\to\R Z\to\tilde{\gg}:=\gg\oplus\R Z\to\gg\to0$ defined by $[X,Y]^{\sim}:=[X,Y]\oplus\Omega(X,Y)Z$, mimicking the passage from $\R^{2n}$ to the Heisenberg algebra in the flat situation. In this new set-up, $M$ may now be realized as a coadjoint orbit of the extended group and the above results remain valid under essentially the same form \cite{Bithese}.

\vspace{2mm}

\noindent To close this subsection, we observe that when the co-adjoint orbit $\co$ is simply connected
the moment mapping $J:M\to \co$ is then necessarily a global $G$-equivariant symplectomorphism. This turns out to be the case in items 1, 2, 4 and 6 in the above list of 2-dimensional spaces.

\subsection{Group type symplectic symmetric surfaces, curvature contractions}
A symplectic symmetric space $(M,\omega,s)$ is said to be {\sl of group type} if there exists in its
automorphism group $G$ a Lie subgroup $\SS$ that acts on $M$ in a simply transitive manner i.e.
in a way that for all $x$ in $M$ there is one and only one element $g$ in $\SS$ with $x=go$. In that
case, one has a $\SS$-equivariant diffeomorphism:
\begin{equation}
\SS\to M:g\mapsto go\;.
\end{equation}
The symplectic structure $\omega$ on $M$ then pulls back to the group manifold $\SS$ as a left-invariant
symplectic structure $\omega^\SS$. Also, the symmetry at $o$ corresponds to a symplectic involution
\begin{equation}
\Psi^M:\SS\to\SS
\end{equation}
that encodes at the level of $\SS$ the  whole structure of symmetric space of $(M,s)$:
the symmetry at a point $g\in\SS$ is given by:
\begin{equation}
s^M_g(g')\;:=\;g.\Psi^M(g^{-1}.g')\;.
\end{equation}
A quick look at the above list in the 2-dimensional case leads us to the observation that

\vspace{2mm}

\noindent{\sl up to isomorphism, there are two and only two non-flat symplectic symmetric affine geometries
that are of group type: the hyperbolic plane $\DD$ and the Poincar\'e orbit $\MM$}.

\vspace{2mm}

\noindent The corresponding automorphism subgroups are in fact both isomorphic to the 2-dimensional affine group $\SS$
that we realize as $\SS:=\{(a,\ell)\}$ with the group law:
\begin{equation}\label{ANmult}
(a,\ell).(a',\ell')\;:=\;(\,a\,+\,a'\,,\,e^{-2a'}\ell\,+\,\ell'\,)\;.
\end{equation}
The unit element is then $e=(0,0)$ and the inverse map is given by $(a,\ell)^{-1}=(-a,-e^{2a}\ell)$.

\noindent Within this setting (see appendix \ref{AppenB}), the affine structures are encoded by the maps :
\begin{equation}\label{PSIM}
\Psi^\MM(a,\ell)\;:=\;(\,-a\,,\,-\ell\,)\;;
\end{equation}
and 
\begin{equation}\label{PSID}
\Psi^\DD(a,\ell)\;:=\;\left(\,-a-\frac{1}{2}\log(1+\ell^2)\,,\,-\ell\,\right)\;.
\end{equation}

\noindent Regarding the symplectic structures, one observes that the constant 2-form ${\rm d}a\wedge{\rm d}\ell$
is invariant under the left-action. Therefore, for every $k\in\R^+_0$, the symplectic structure
\begin{equation}
\omega^{(k)}\;:=\;\sqrt{k}\,{\rm d}a\wedge{\rm d}\ell
\end{equation}
induces the following symplectic symmetric surfaces: $(\SS,s^\DD,\omega^{(k)})$ and $(\SS, s^\MM,\omega^{(k)})$.
The first one is isomorphic to the hyperbolic plane $\DD$ with curvature $\frac{-1}{k}$. In the second one,
the parameter $k$ is indifferent in the sense that for all $k$, one has the isomorphism: $(\SS, s^\MM,\omega^{(k)})\simeq(\SS, s^\MM,\omega^{(1)})$. 

\subsection{Admissible functions on symplectic symmetric surfaces}
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
