---
doc_id: arxiv-0806.4741v1
doc_title: "The deformation quantizations of the hyperbolic plane"
section_id: sec-004-definitions-and-elementary-properties
section_title: "Definitions and elementary properties"
section_number: null
pages: 4-7
source_pdf: 0806.4741v1.pdf
source_sha256: 5e7ad85a99fb3552
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.981
doc_brief: "The deformation quantizations of the hyperbolic plane — We describe the space of (all) invariant deformation quantizations on the hyperbolic plane D as solutions of the evolution of a second order"
---
\label{DefandProp}
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
