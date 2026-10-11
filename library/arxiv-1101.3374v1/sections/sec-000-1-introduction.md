---
doc_id: arxiv-1101.3374v1
doc_title: "PONTRYAGIN INVARIANTS AND INTEGRAL FORMULAS FOR MILNOR’S TRIPLE LINKING NUMBER"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-20
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
doc_brief: "PONTRYAGIN INVARIANTS AND INTEGRAL FORMULAS FOR MILNOR’S TRIPLE LINKING NUMBER — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
text_source: latex
latex_prose_ratio: 0.652
latex_coverage_ratio: 1.0
---
\label{sec:intro}

\begin{wrapfigure}[10]{l}{35mm}
  \begin{center}
  \includegraphics[height=100pt]{cremona7.jpg}
  \put(-88,-12){\small\bf Borromean Rings}

  \end{center}
\label{fig:borromean}
\end{wrapfigure}
Three-component links in the $3$-sphere $S^3$ were classified up to {\itb link homotopy} -- a deformation during which each component may cross itself but distinct components must remain disjoint -- by John Milnor in his senior thesis, published in 1954.   A complete set of invariants is given by the pairwise linking numbers $p$, $q$ and $r$ of the components, and by the residue class $\mu$ of one further integer modulo the greatest common divisor of $p$, $q$ and $r$, the {\itb triple linking number} of the title.   For example, the Borromean rings shown here have $p=q=r=0$ and $\mu=\pm1$, where the sign depends on the ordering and orientation of the components.


\vskip .1in

To each such link $L$ we will associate a geometrically natural characteristic map $g_L$ from the $3$-torus $\tor = S^1\times S^1\times S^1$ to the $2$-sphere $S^2$ in such a way that link homotopies of $L$ become homotopies of $g_L$.  The definition of $g_L$ will be given below.   The assignment $L\mapsto g_L$ then defines a function 
\begin{comment}
\begin{equation}\label{eqn:g}
g:\call_3\  \longrightarrow \ [T^3,S^2]
\tag{$*$}
\end{equation}
\end{comment}
$$
g:\call_3 \longrightarrow [T^3,S^2]
$$
from the set $\call_3$ of link homotopy classes of three-component links in $S^3$ to the set $[T^3,S^2]$ of homotopy classes of maps $T^3\to S^2$, and it will be seen below that $g$ is injective.  

\begin{comment}  This perspective on link homotopy will be discussed further in the ``Background and Motivation" section at the end of the Introduction.
\end{comment}

Maps from $\tor$ to $S^2$  were classified up to homotopy by Lev Pontryagin in 1941.   A complete set of invariants is given by the degrees $p$, $q$ and $r$ of the restrictions to the $2$-dimensional coordinate subtori, and by the residue class $\nu$ of one further integer modulo {\it twice} the greatest common divisor of $p$, $q$ and $r$, the {\itb Pontryagin invariant} of the map.  

This invariant is an analogue of the Hopf invariant for maps from $S^3$ to $S^2$, and is an absolute version of the relative invariant originally defined by Pontryagin for {\it pairs} of maps from a $3$-complex to $S^2$ that agree on the $2$-skeleton of the domain.  

Our first main result, \thmref{A} below, equates Milnor's and Pontryagin's invariants $p$, $q$ and $r$ for $L$ and $g_L$, and asserts that 
$$
2\mu(L) \ = \ \nu(g_L).
$$
As a consequence, the function $g:\call_3\  \longrightarrow \ [T^3,S^2]$ above is one-to-one, with image the set of maps of even $\nu$-invariant.   

In the special case when $p=q=r=0$, we derive an explicit and geometrically natural integral formula for the triple linking number, reminiscent of Gauss' classical integral formula for the pairwise linking number.  This formula and variations of it are presented in \thmref{B} below.

In the rest of this introduction, we provide the definition of the characteristic map, give careful statements of Theorems \ref{thm:A} and \ref{thm:B}, and then discuss some motivation for our work coming from the homotopy theory of configuration spaces and from fluid dynamics and plasma physics. 

   

\part{The characteristic map of a three-component link in the $3$-sphere}


Let $x$, $y$ and $z$ be three distinct points on the unit $3$-sphere $S^3$ in $\br^4$.  They cannot lie on a straight line in $\br^4$,  so must span a $2$-plane there.  Translate this plane to pass through the origin, and then orient it so that the vectors $x-z$ and $y-z$ form a positive basis.  The result is an element $G(x,y,z)$ of the Grassmann manifold $\gras$ of all oriented 2-planes through the origin in $4$-space.  This procedure defines the {\itb Grassmann map} 
$$
G: \conf \ \longrightarrow \ \gras
$$
pictured in \figref{gras}, where 
$$
\conf\ \subset \ S^3 \times S^3 \times S^3
$$ 
is the configuration space of ordered triples of distinct points in $S^3$.  The map $G$ is equivariant with respect to the diagonal $SO(4)$ action on $S^3 \times S^3 \times S^3$ and the usual $SO(4)$ action on $\gras$.


\begin{figure}[h!]
\includegraphics[height=120pt]{FigGR.pdf}
\put(-70,27){\small $G(x,y,z)$}
\put(-135,95){\small $x$}
\put(-107,86){\small $y$}
\put(-85,80){\small $z$}
\put(-125,15){$S^3$}
\put(-190,23){$\br^4$}
\caption{The Grassmann map $(x,y,z)\mapsto G(x,y,z)$}
\label{fig:gras}
\end{figure}


The Grassmann manifold $\gras$ is diffeomorphic to the product $S^2\times S^2$ of two 2-spheres, as explained in \secref{characteristic} below.  Let $\pi_+$ and $ \pi_- : \gras\to S^2$ denote the projections to the two factors.  One of these will be used in the definition of the characteristic map, but the choice of which one will be seen to be immaterial.  

Now let $L$ be a link in $S^3$ with three parametrized components
$$
X \ = \ \{x(s) \st s \in S^1\} \ , \ Y \ = \ \{y(t) \st t \in S^1 \} \ \ \text{and}\ \  Z \ = \ \{z(u) \st u \in S^1 \}
$$
as indicated schematically in \figref{graslink}.  Here and throughout, we view the parametrizing circle $S^1$ as the quotient $\br/2\pi\bz$, and assume implicitly that the parametrizing functions $x=x(s)$, $y=y(t)$ and $z=z(u)$ are smooth with nowhere vanishing derivatives. 


\begin{figure}[h!]
\includegraphics[height=120pt]{FigLink.pdf}
\put(-112,75){\small $X$}
\put(-40,25){\small $Y$}
\put(-19,60){\small $Z$}
\put(-75,8){$S^3$}
\caption{The link $L$ in $S^3$}
\label{fig:graslink}
\end{figure}


We define the {\itb characteristic map} $g_L:T^3 \to S^2$ in terms of the Grassmann map $G:\conf\to\gras$ and the projection $\pi_+:\gras\to S^2$ by the formula
$$
g_L(s,t,u) \ = \ \pi_+(G(x(s),y(t), z(u)).
$$
In other words $g_L$ is the composition $\pi_+Ge_L$ where $e_L:\tor\to\gras$ is the embedding that parametrizes the link, given by $e_L(s,t,u) \ = \ (x(s),y(t),z(u))$.   We regard $g_L$ as a natural generalization of the Gauss map $T^2\to S^2$ associated with a two-component link in $\br^3$. 

It is clear that the homotopy class of $g_L$ is unchanged under reparametrization of $L$, or more generally under any link homotopy of $L$.  Furthermore, $g_L$  is ``symmetric" in that  it transforms under any permutation of the components of $L$ by precomposing with the corresponding permutation automorphism of $\tor$ multiplied by the sign of the permutation.

\begin{comment}
In \secref{characteristic} we give an explicit formula for $g_L$ as the unit normalization of a vector field on $\tor$ whose components are quadratic polynomials in the components of $x(s)$, $y(t)$ and $z(u)$.   Then in \secref{asymmetric} we set up for the proof of \thmref{A} by describing an alternative asymmetric form $h_L$ of the characteristic map, homotopic to $g_L$, and introducing a special class of ``generic" links whose associated Pontryagin invariants $\nu(h_L)$ are easily computed.
\end{comment}




\part{Statement of results}



The first of our two main results gives an explicit correspondence between the Milnor link homotopy invariants of a three-component ordered, oriented link in the $3$-sphere and the Pontryagin homotopy invariants of its characteristic map. 


\begin{theorem}\label{thm:A}
\textbf{\boldmath Let $L$ be a $3$-component link in $S^3$.  Then the pairwise linking numbers $p$, $q$ and $r$ of $L$ are equal to the degrees of its characteristic map $g_L:T^3\to S^2$ on the two-dimensional coordinate subtori of $\tor$, while twice Milnor's $\mu$-invariant for $L$ is equal to \mbox{Pontryagin's} $\nu$-invariant for $g_L$ modulo $2\gcd(p,q,r)$.}
\end{theorem}


\noindent {\bf Conventions.}  (1) In this paper, links in $S^3$ are always {\it ordered} (the components are taken in a specific order) and {\it oriented} (each component is oriented).  

\noindent (2) The two-dimensional coordinate subtori of $T^3$ are oriented to have positive intersection with the remaining circle factors.

\vskip.05in

The key idea of the proof centers on the ``delta move", a higher order variant of a crossing change.  Applied to a three-component link $L$ in the $3$-sphere, we show easily that this move increases Milnor's $\mu$-invariant by $1$, and then the bulk of the proof is devoted to showing that it increases Pontryagin's $\nu$-invariant by $2$.



The background material for the proof is contained in Sections \ref{sec:milnor} and \ref{sec:pontryagin} of the paper.  In particular, in \secref{milnor} we discuss how to compute Milnor's $\mu$-invariant, describe the delta move, and prove that it increases the $\mu$-invariant by $1$.  In \secref{pontryagin}, we discuss Pontryagin's homotopy classification of maps from a 3-manifold  to the 2-sphere in terms of framed bordism of framed links, define the ``Pontryagin link'' of such a map to be the inverse image of any regular value, and then show how to convert the relative $\nu$-invariant to an absolute one when the manifold is the $3$-torus.  This section concludes with a simple procedure for computing the absolute $\nu$-invariant of any map of the 3-torus to the 2-sphere from a diagram of its Pontryagin link. 

The proof of \thmref{A} will occupy us in Sections \ref{sec:characteristic}--\ref{sec:A}, and is organized as follows.  

In \secref{characteristic}, we derive an explicit formula for the characteristic map $g_L$ needed for the proof of \thmref{B}, but not for that of \thmref{A}.  We then describe an alternative asymmetric form $h_L$ of the characteristic map that is more convenient for the proof of \thmref{A}, and that, just as for $g_L$, depends {\it a priori} on the choice of a projection to the $2$-sphere.  We show that the two characteristic maps are homotopic to one another, and that, up to homotopy, neither in fact depends on the choice of projection.   We note a close relation between $h_L$ and the classical Gauss maps of two-component links in $3$-space, and use this, together with the symmetry of $g_L$, to prove the first statement in \thmref{A}.  

In \secref{Aprep}, we set up for the proof of the rest of \thmref{A} by describing the standard open-book structure on $S^3$ with disk pages, use a link homotopy to move a given link $L$ into ``generic position'' with respect to it, and then show how to explicitly visualize the Pontryagin link of the corresponding asymmetric characteristic map $h_L$.  Finally, we use the results of \secref{pontryagin} to develop a method for computing $\nu(h_L) = \nu(g_L)$. 

In \secref{A}, we complete the proof of \thmref{A} by induction, using the methods developed in Sections \ref{sec:milnor} and \ref{sec:pontryagin} to first confirm the ``base case'', and then using the methods of \secref{Aprep} to carry out the inductive step, showing that the delta move increases Pontryagin's $\nu$-invariant by 2.

\secref{A'} contains a sketch of a more algebraic proof of this theorem using the group of link homotopy classes of three-component string links and the fundamental groups of spaces of maps of the 2-torus to the $2$-sphere. More details for this alternative proof can be found in our announcement \cite{DGKMSV}, which is otherwise an abridged version of some of the material in the current paper.



In Sections~\ref{sec:B} and~\ref{sec:B'}, we investigate the special case when the pairwise linking numbers $p$, $q$ and $r$ of $L$ are all zero, and so the $\mu$ and $\nu$-invariants are ordinary integers.  In this case we will use J.\,H.\,C.~Whitehead's integral formula for the Hopf invariant, adapted to maps of the $3\text{-torus}$ to the $2$-sphere, together with a formula for the fundamental solution of the scalar Laplacian on the $3$-torus as a Fourier series in three variables, to provide an explicit integral formula for $\nu(g_L)$, and hence for $\mu(L)$ in light of \thmref{A}.  See \thmref{B}, stated below.
 
This formula will be presented in three versions: first as an integral involving differential forms on the {$3\text{-torus}$, second as the same integral expressed in terms of vector fields, and finally as an infinite sum involving Fourier coefficients. 

To state these formulas, we need some definitions.   Let $\omega$ denote the Euclidean area $2$-form on $S^2$, normalized to have total area $1$.  Then $\omega$ pulls back under the characteristic map $g_L$ to a closed $2$-form $\omega_L$ on $\tor$, which can be converted to a divergence-free vector field $\vec_L$ on $\tor$ via the usual formula 
$$
\omega_L(\vc{\textup{\bf a}}\, ,\vc{\textup{\bf b}}) \ = \ (\vc{\textup{\bf a}}\times\vc{\textup{\bf b}})\dtw\vec_L.
$$  
We call  $\omega_L$  the {\itb characteristic $2$-form} of  $L$,  and  $\vec_L$  its {\itb characteristic vector field}.  When $p$, $q$ and $r$ are all zero, $\omega_L$ is exact and $\vec_L$ is in the image of curl.  In \secref{B} we give explicit formulas for  $\omega_L$  and  $\vec_L$,  and in \secref{B'}  for the fundamental solution $\varphi$ of the scalar Laplacian on $\tor$, which appear in the integral formulas for $\mu(L)$. 



For the third version of our formula for the Milnor invariant, we need to express the characteristic $2$-form and vector field in terms of Fourier series on the $3$-torus.  To that end, view $T^3$ as the quotient $(\br/2\pi\bz)^3$ and write $\x=(s,t,u)\in\br^3$ for a general point there.  Using the complex form of Fourier series, express
$$
\omega_L \ = \ \sum_{\n\in\bz^3}\left(c^s_{\n} \, dt\wedge du+c^t_{\n} \, du\wedge ds+c^u_{\n} \, ds\wedge dt\right)e^{i\n\dte\x}.
$$
Using vector notation \,$\c_{\n} = (c^s_{\n},c^t_{\n},c^u_{\n})$\ , \ $d\x \ = \ (ds, dt, du)$\ , \ $\partial_\x = (\partial/\partial s,\partial/\partial t, \partial/\partial u)$ \,and\, $\star d\x \ = \ (dt\wedge du, du\wedge ds, ds\wedge dt)$\,, the formulas for $\omega_L$ and $\vec_L$ become
$$
\omega_L\ =\ \sum_{\n\,\in\,\bz^3}\c_{\n}\, e^{i\n\dte\x}\dtw\star\!d\x \qquad\text{and }\qquad \vec_L \ = \ \sum_{\n\,\in\,\bz^3}\c_{\n}\, e^{i\n\dte\x}\dtw \partial_\x.
$$
As a consequence of the assumption that the pairwise linking numbers of $L$ vanish, the coefficient $\c_{\zero}$ is the zero vector, which will imply that $\omega_L$ is exact, or equivalently that $\vec_L$ is in the image of curl.


\begin{theorem}\label{thm:B}
\textbf{\boldmath If the pairwise linking numbers of a three-component link $L$ in $S^3$ are all zero, then Milnor's $\mu$-invariant of $L$ is given by each of the following equivalent formulas
$$
\begin{aligned}
\mu(L) \ &= \  1/2\, \int_{T^3} \delta(\varphi*\omega_L) \wedge \omega_L \ & \qquad (1) \\
\ &= \ 1/2\, \int_{\tor\times\tor} \vec_L(\x) \times \vec_L(\y) \dtew \nabla_{\!\y}\, \varphi(\x - \y)\ d\x\, d\y \ & \qquad (2) \\
\ & = \  8\pi^3 \sum_{\n\ne\zero} \textstyle \a_\n\times \b_\n\dtew \n/\|\n\|^2\ . & \qquad (3)
\end{aligned}
$$
where $\varphi$ is the fundamental solution of the scalar Laplacian on the $3$-torus, $\omega_L$ and $\vec_L$ are the characteristic form and vector field of $L$, and $\a_\n$ and $\b_\n$ are the real and imaginary parts of the Fourier coefficients $\c_\n$ of $\omega_L$ and $\vec_L$.}
\end{theorem}



\noindent {\bf Explanation of the notation.} In (1), $\delta$ is the exterior co-derivative and $\ph*\omega_L$ is the convolution of $\ph$ with $\omega_L$, discussed in detail in Sections~\ref{sec:B} and~\ref{sec:B'}. 

In (2), the difference $\x-\y$ is taken in the abelian group structure on $\tor$, the expression $\nabla_{\!\y}\, \varphi(\x - \y)$ indicates the gradient with respect to $\y$ while $\x$ is held fixed, and $d\x$ and $d\y$ are volume elements on $\tor$.  This formula is just the vector field version of (1) in which the integral hidden in the convolution is expressed openly; we will see below that it represents the ``helicity" of the vector field $\vec_L$ on $\tor$.  

Observe that the integrands in (1) and (2) are invariant under the group $SO(4)$ of orientation-preserving rigid motions of $S^3$, attesting to the naturality of the formulas. 




\part{Background and Motivation} 




{\bf Configuration spaces.} \ To study the linking of simple closed curves in a $3$-manifold $\man$ from the perspective of homotopy theory, it is convenient to ignore the knotting of individual components and focus on the relation of {\itb link homotopy}.  For some background on this notion, see Milnor \cite{Milnor54, Milnor57} and, for example, Massey~\cite{Massey68}, Casson~\cite{Casson75}, Turaev~\cite{Turaev76}, Porter~\cite{Porter}, Fenn~\cite{Fenn83}, Orr~\cite{Orr}, Cochran~\cite{Cochran}, and Habegger and Lin~\cite{HabeggerLin}.


Configuration spaces come into the picture as follows.  Let $L$ be an ordered, oriented link in $\man$ with $n$ components $X,Y,\dots$ parametrized by $x=x(s),y=y(t), \dots$ for $s,t,\dots$ in $S^1$.  Then consider the {\itb evaluation map} 
$$
e_L : T^n \ \longrightarrow \ \confn\ , \qquad (s, t, \dots)\longmapsto (x, y, \dots)
$$
from the $n$-torus $T^n = S^1\times\cdots\times S^1$ to the configuration space $\confn$ of ordered $n\text{-tuples}$ of distinct points in $\man$.  Since link homotopies of $L$ become homotopies of $e_L$, the assignment $L\mapsto e_L$ induces a map from the set $\call_n(\man)$ of link homotopy classes of $n$-component links in $\man$ to the set $[T^n,\confn]$ of homotopy classes of maps from $T^n$ to $\confn$,
$$
e : \call_n(\man) \ \longrightarrow \ [T^n,\confn].
$$
We can think of the map $e$ as defining a representation from the world of link homotopy to the world of homotopy, and the basic question  is whether or not this representation is faithful, that is, one-to-one.

For two-component links in $\br^3$, the representation $e$ is faithful.  The set $\call_2(\br^3)$ is in one-to-one correspondence with the integers via the classical linking number, while the set $[T^2,\conftr]$ is also in one-to-one correspondence with the integers via the Brouwer degree, since $\conftr$ deformation retracts to $S^2$.  The correspondence $e$ is bijective since the linking number of a two-component link equals the degree of its ``Gauss map"
$$
T^2 \ \longrightarrow \ S^2\quad , \quad (s,t)\,\longmapsto\, \frac{y-x}{\|y-x\|}.
$$

\break
The profit is the famous integral formula of Gauss~\cite{Gauss},
$$
\begin{aligned}
\lk(X,Y) \ &= \ \frac1{4\pi} \,\int_{T^2} \frac{dx}{ds}  \times \frac{dy}{dt} \dtw  \frac{x-y}{\,|x-y|^3} \ \,ds \, dt \\
\ &= \ \int_{T^2} \frac{dx}{ds}  \times   \frac{dy}{dt}  \dtw  \nabla_{\!y}\,\varphi(y\!-\!x) \ ds \, dt,
\end{aligned}
$$
where $\varphi(x) = 1/4\pi\|x\|$ is the fundamental solution of the scalar Laplacian in $\br^3$.  The integrand is natural, in the sense that it is invariant under the group of orientation-preserving rigid motions of $\br^3$, acting on the link.  

By contrast, for two-component links in $S^3$ the representation $e$ is not faithful.  The configuration space $\confts$ has the homotopy type of $S^3$, and hence all maps of $T^2$ to $\confts$ are homotopically trivial.  In particular, the analogue of Gauss's linking integral in $S^3$, with an integrand which is geometrically natural in the above sense, cannot be obtained by this route.   Nevertheless, such an integral formula was found by DeTurck and Gluck \cite{DeTurckGluck} using an alternative route via electrodynamics on the $3$-sphere, and independently by Kuperberg~\cite{Kuperberg} via the calculus of double forms.

For higher-dimensional two-component links, the same dichotomy holds. 
In $\br^n$, Scott \cite{Scott} and Massey and Rolfsen \cite{MasseyRolfsen} showed that link homotopy classes of links whose components are copies of $S^k$ and $S^{n-k-1}$ are in bijective correspondence with homotopy classes of maps from $S^k\times S^{n-k-1}$ to the configuration space $\conftrn\simeq S^{n-1}$, and consequently with $\pi_{n-1}(S^{n-1}) \cong\bz$.  Finding a geometric linking integral is straightforward, as the Gauss linking integral and its proof easily generalize to this setting.  Shifting the scene to $S^n$ does not change the link homotopy story, but all maps from $S^k\times S^{n-k-1}$ to the configuration space $\conftsn\simeq S^n$ are homotopically trivial.  Geometrically natural linking integrals still exist in this situation, as demonstrated by DeTurck and Gluck \cite{DeTurckGluckb} and Shonkwiler and Vela-Vick \cite{SVV}, but finding them requires new techniques. 


For $n$-component {\itb homotopy Brunnian} links in $\br^3$ -- meaning links that become trivial up to link homotopy when any single component is removed -- and analogous links in higher dimensions, Koschorke \cite{Koschorke} showed that the representation $e$ is again faithful.  This provided the first proof (up to sign) of our \thmref{A} for the case when the pairwise linking numbers are zero.

The content of the present paper is that, for arbitrary three-component links $L$ in $S^3$, the representation $e$ is faithful, and that we are led thereby to a natural integral for Milnor's triple linking number when the pairwise linking numbers vanish.  The relevant configuration space $\conf$ is easily seen to deformation retract to  $S^3 \times S^2$, where the $S^3$ coordinate records one of the three points in each triple (see \secref{characteristic}).  It follows that the evaluation map $e_L:\tor\to\conf$ is homotopic to a map of $\tor$ into an $S^2$ fiber, and this turns out to be, up to homotopy, our characteristic map $g_L$.

\thmref{A} asserts, among other things, that $L$ and $L'$ are link homotopic if and only if $g_L$ and $g_{L'}$ are homotopic, and hence that
$$
e:\call_3(S^3)\longrightarrow[T^3,\conf]
$$
is faithful.  Furthermore, it was observed above that if $h\in\so(4)$ is an orientation preserving isometry of $S^3$, then $e_{h(L)} = h\cdot e_L$ where $\cdot$ is the diagonal action, and so the integrands in the formulas for Milnor's triple linking number $\mu(L)$ in \thmref{B} are invariant under the action of $\so(4)$.


We emphasize that our Theorems \ref{thm:A} and \ref{thm:B} are set specifically in $S^3$, and that so far we have been unable to find corresponding results in Euclidean space $\br^3$ which are equivariant (for \thmref{A}) and invariant (for \thmref{B}) under the noncompact group of orientation-preserving rigid motions of $\br^3$.   



{\bf Fluid mechanics and plasma physics.} \ The {\itb helicity} of a vector field $V$ defined on a bounded domain $\Omega$ in $\br^3$ is given by the formula
$$
\begin{aligned}
\text{Hel}(V) \ &= \ \frac{1}{4\pi}\, \int_{\Omega\times\Omega} \!\!\!\!\!V(x) \times V(y) \dtw \frac{x-y}{\,|x-y|^3} \  \,dx \, dy \\
 \ &= \ \int_{\Omega\times\Omega} \!\!\!\!\!V(x) \times V(y) \dtw \nabla_{\!y}\,\varphi(x\!-\!y) \ dx \, dy.
\end{aligned}
$$
where, as above, $\varphi$ is the fundamental solution of the scalar Laplacian in $\br^3$, and $dx$ and $dy$ are volume elements.

Woltjer~\cite{Woltjer} introduced this notion during his study of the magnetic field in the Crab Nebula, and showed that the helicity of a magnetic field remains constant as the field evolves according to the equations of ideal magnetohydrodynamics, and that it provides a lower bound for the field energy during such evolution.  The term ``helicity'' was coined by Moffatt~\cite{Moffatt}, who also derived the above formula from Woltjer's original expression.  

There is no mistaking the analogy with Gauss's linking integral, and no surprise that helicity is a measure of the extent to which the orbits of $V$ wrap and coil around one another.  Since its introduction, helicity has played an important role in astrophysics and solar physics, and in plasma physics here on earth.  

Looking back at \thmref{B}, we see that the integral in our formula for Milnor's $\mu\textup{-invariant}$ of a three-component link $L$ in the 3-sphere expresses the helicity of the associated vector field $\vec_L$ on the 3-torus.


Our study was motivated by a problem proposed by Arnol$'$d and Khesin~\cite{ArnoldKhesin98} regarding the search for ``higher helicities'' for divergence-free vector fields.  In their own words:

\vspace{.05in}
\begin{indentation}{2.6em}{2.6em}
\small\itb
\noindent The dream is to define such a hierarchy of invariants for generic vector fields such that, whereas all the invariants of order $\leq k$ have zero value for a given field and there exists a nonzero invariant of order $k+1$, this nonzero invariant provides a lower bound for the field energy.
\end{indentation}
\vspace{.05in}

Since the helicity integral above is analogous to the Gauss linking integral, the general hope is that higher helicities will be analogous to higher order linking invariants.  But the anti-symmetry of Milnor's triple linking number appears to be an impediment to naively generalizing it to a second order helicity for vector fields, and suggests that attention be directed to yet higher order link homotopy and concordance invariants.  

The formulation in Theorems~\ref{thm:A} and~\ref{thm:B} has led to partial results that address the case of vector fields on invariant domains such as flux tubes modeled on the Borromean rings; see Komendarczyk~\cite{Komendarczyk, Komendarczyk10}.


\break

{\bf Other integral formulas.} Previous integral formulas for Milnor's triple linking number and attempts to define a higher order helicity can be found in the work of Massey~\cite{Massey58, Massey68}, Monastyrsky and Retakh~\cite{MonastyrskyRetakh}, Berger~\cite{Berger90, Berger91}, Guadagnini, Martellini and Mintchev~\cite{GMM}, Evans and Berger~\cite{EvansBerger92}, Akhmetiev and Ruzmaiken~\cite{Akhmetiev94, Akhmetiev95}, Arnol$'$d and Khesin~\cite{ArnoldKhesin98}, Laurence and Stredulinsky \cite{Laurence}, Leal~\cite{Leal02}, Hornig and Mayer \cite{Hornig}, Rivi\`ere~\cite{Riviere}, Khesin~\cite{Khesin}, Bodecker and Hornig~\cite{Bodecker04}, Auckly and Kapitanski~\cite{AucklyKapitanski}, Akhmetiev~\cite{Akhmetiev05}, and Leal and Pineda~\cite{LealPineda08}.

The principal sources for these formulas are Massey triple products in cohomology, quantum field theory in general, and Chern--Simons theory in particular.  A common feature of these integral formulas is that choices must be made to fix the domain of integration and the value of the integrand. 


\smallskip





\noindent{\bf Acknowledgements.}  We are grateful to Fred Cohen and Jim Stasheff for their substantial input and help during the preparation of this paper, and to Toshitake Kohno, whose 2002 paper provided one of the inspirations for this work.  Komendarczyk and Shonkwiler also acknowledge support from DARPA grant \#FA9550-08-1-0386, and Vela-Vick from an NSF postdoctoral fellowship.

The Borromean rings shown on the first page are from a panel in the carved walnut doors of the Church of San Sigismondo in Cremona, Italy.  The photograph is courtesy of Peter Cromwell.  








 




\vskip-.15in
\vskip-.15in


\section{The Milnor $\mu$-invariant} 
\label{sec:milnor}

Let $L$ be a three-component link in either $\br^3$ or $S^3$, with oriented components $X$, $Y$ and $Z$, and pairwise linking numbers $p$, $q$ and $r$.  Milnor's original definition of the triple linking number $\mu(L)$, typically denoted $\bar\mu_{123}(L)$, was algebraic.  The formulation in his PhD thesis \cite{Milnor57} is expressed in terms of the lower central series of the link group $G$, the fundamental group of the complement of $L$, as follows.

Choose based meridians for the link components $X$, $Y$ and $Z$, and let $x$, $y$ and $z$ denote the corresponding elements of $G$.  In general, these three elements do not generate $G$, but they do generate the quotient of $G$ by the third term $[[G,G],G]$ in its lower central series.  In this quotient group, the longitude of $Z$ can be written as a word $w$ in $x$, $y$ and $z$ and their inverses.  Assign an integer $m_{xy}(w)$ to this word that counts with signs the number of times that $x$ appears before $y$ in $w$, allowing intervening letters.  More precisely, each appearance of $x\cdotsclose y$ or $x^{-1}\cdotsclose y^{-1}$ contributes $+1$ to $m_{xy}(w)$, while $x\cdotsclose y^{-1}$ or $x^{-1}\cdotsclose y$ contributes $-1$.  Then $\mu(L)$ is the element of $\bz_{\gcd(p,q,r)}$ defined by
$$
\mu(L) \ = \ m_{xy}(w)\ \ \textup{mod}\gcd(p,q,r).
$$

There is a geometric reformulation of this definition, found by Mellor and Melvin \cite{MellorMelvin}, that is more convenient for our purposes:  choose Seifert surfaces $F_X$, $F_Y$ and $F_Z$ for the components of $L$, and move these into general position.   Starting at any point on $X$, record its intersection with the Seifert surfaces for $Y$ and $Z$ by a word $w_X$ in $y$ and $z$.  For example a $y$ or $y^{-1}$ in $w_X$ indicates a positive or negative intersection point of $X$ with $F_Y$.  Set $m_X = m_{yz}(w_X)$, where the right hand side is computed as in the last paragraph, and similarly set $m_Y = m_{zx}(w_Y)$ and $m_Z = m_{xy}(w_Z)$.  Finally, let $t$ be the signed count of the number of triple points of intersection of the three Seifert surfaces.  Then 
$$
\mu(L) \ =  \ m_X+m_Y+m_Z - t \ \ \textup{mod}\gcd(p,q,r).
$$
It follows from this formula that $\mu(L)$ is invariant under even permutations of the components of $L$, but changes sign under odd permutations.  This is a well known property of Milnor's triple linking number.

We give two sample calculations of the triple linking number, using this geometric formulation, that will feature in our inductive proof of \thmref{A} in \secref{A}.

\begin{example} \label{ex:Lpqr}
Let $L_{pqr}$ be the link shown in \figref{Lpqr}, with components $X$, $Y$ and $Z$ and with pairwise linking numbers $p$, $q$ and $r$.   Choose the Seifert surfaces $F_X$, $F_Y$ and $F_Z$ to be the obvious disks, essentially lying in the page, bounded by $X$, $Y$ and $Z$.  


\begin{figure}[h!]
\includegraphics[height=150pt]{FigLpqr.pdf}
\put(-80,25){$X$}
\put(-30,90){$Y$}
\put(-125,90){$Z$}
\put(-58,62){\small$r$}
\put(-96,64){\small$q$}
\put(-78,95){\small$p$}
\caption{The base link $L_{pqr}$ for  $p=5$, $q=3$, $r=-2$}
\label{fig:Lpqr}
\end{figure}


Starting at appropriate points on the link components, we can read off the words 
$$
w_X = y^rz^q \ , \ \ w_Y = z^px^r \quad\textup{and}\quad w_Z = x^qy^p.
$$
Thus $m_X = qr$, $m_Y = rp$ and $m_Z = pq$.   Furthermore, it is clear that there are no triple points of intersection of the three disks.  Therefore
$$
\mu(L_{pqr}) \ = \ qr+rp+pq-0 \ = \ 0 \ \in \ \bz_{\gcd(p,q,r)}.
$$  
The links $L_{pqr}$ will serve as the {\itb base links} for our proof of \thmref{A}.
\end{example} 

\begin{example}\label{ex:delta} 
Consider the {\itb delta move} shown in \figref{delta}, transforming the link $L$ on the left to the link $\what L$ on the right.  


\begin{figure}[h!]
\includegraphics[height=100pt]{FigD.pdf}
\put(-228,95){$X$}
\put(-28,99){$\what X$}
\put(-230,-5){$Y$}
\put(-22,-5){$\what Y$}
\put(-315,45){$Z$}
\put(-113,46){$\what Z$}


\caption{The delta move $L\to \what L$}
\label{fig:delta}
\end{figure}


This move takes place within a $3$-ball, outside of which the link is left fixed.  It does not alter the pairwise linking numbers of $L$, and may be thought of as a higher order variant of a crossing change.

The delta move was introduced by Matveev \cite{Matveev}.  It was shown by Murakami and Nakanishi \cite{MurakamiNakanishi} that a suitable sequence of such moves can transform any link into any other link with the same number of components and the same pairwise linking numbers.  In particular, the base link $L_{pqr}$ above can be transformed into any other three-component link with pairwise linking numbers $p$, $q$ and $r$ by a sequence of delta moves.  The inductive step of our proof of \thmref{A} will be based on this observation, and so we determine right now the effect of the delta move on the $\mu$-invariant.   

If the three arcs involved in the delta move {\it do not} come from three distinct components of the link $L$, then the change can be achieved by a link homotopy, and hence neither Milnor's $\mu$-invariant nor Pontryagin's $\nu$-invariant for $g_L$ will change.  

But if the arcs {\it do} come from three distinct components of $L$ as shown in the figure, then $\mu$ increases by $1$, that is 
$
\mu(\what L) = \mu(L) + 1.
$
This can be seen as follows, using the geometric formula for the $\mu$-invariant.

In \figref{seifert}, we display on the left fragments of the Seifert surfaces $F_X$, $F_Y$ and $F_Z$ before the delta move, while on the right, after the delta move, each old surface is enlarged a bit to provide new surfaces $F_{\what X}$, $F_{\what Y}$ and $F_{\what Z}$. 
 

\begin{figure}[h!]
\includegraphics[height=120pt]{FigS.pdf}
\put(-300,90){$F_X$}
\put(-185,90){$F_Y$}
\put(-275,-5){$F_Z$}
\put(-125,90){$F_{\what  X}$}
\put(-10,90){$F_{\what  Y}$}
\put(-30,-3){$F_{\what  Z}$}
\caption{A negative triple point appears}
\label{fig:seifert}
\end{figure}


On the left, the three surface fragments are disjoint, while on the right, after their enlargement, they are not.  Where these surfaces now come together, we have an additional isolated triple point, and since the normals to the surfaces at this point form a left-handed frame, this triple point gets a minus sign.  Thus $t$ drops by $1$.   We also see that after the delta move, the curve $\what Z$ has two extra intersections with $F_{\what Y}$, the first positive and the second negative, and no extra intersections with $F_{\what X}$.  Since these new intersection points are adjacent along the curve, and of opposite signs,  it follows that the new count $m_{\what Z} =  m_{xy}(w_{\what Z})$ is equal to the old one $m_Z$.  Similarly $m_{\what X} = m_X$ and $m_{\what Y} = m_Y$.   Hence $\mu =  m_X + m_Y + m_Z  - t$  increases by 1,  as claimed. 
 
The heart of the proof of \thmref{A} will be to show that application of the delta move increases Pontryagin's $\nu$-invariant by $2$. 

\end{example}

 






\section{The Pontryagin $\nu$-invariant} 
\label{sec:pontryagin}

Heinz Hopf proved in 1931 that homotopy classes of maps from the $3$-sphere to the $2$-sphere are in one-to-one correspondence with the integers via his now famous Hopf invariant.  Pontryagin \cite{Pontryagin41} generalized this to give the homotopy classification for maps from an arbitrary finite $3$-complex to the $2$-sphere.  It is convenient for our purposes to restrict to smooth maps from $3$-manifolds to the $2$-sphere,  and to use Poincar\'e duality to take Pontryagin's result, originally presented via cohomology, and reformulate it in homological terms.

 

\part{Definition and properties}


Fix a closed oriented smooth $3$-manifold $\man$.  The homotopy classification of maps $f: \man\to S^2$  can be expressed using two differential topological invariants.  

The primary invariant
$$
\lambda(f) \ \in \ H_1(\man) \qquad\text{(with integral coefficients understood)}
$$
records the homology class of the preimage link $\bl = f^{-1}(*)$
of any regular value $\pt$ of $f$ (oriented as explained below), or equivalently the Poincar\'e dual of the pull-back $f^*(\omega)$ of the orientation class $\omega\in H^2(S^2)$.  It is easily shown that two maps have the same primary invariant if and only if they induce the same map on homology.     

The secondary invariant 
$$
\nu(f_0,f_1) \ \in \ \bz_{2d(\lambda)}
$$ 
compares two maps $f_0$ and $f_1$ with the same primary invariant $\lambda$.  Here $d(\lambda)$ is the divisibility of $\lambda$ as an element of the free abelian group $H_1(\man)/$torsion.  Thus $d(\lambda) = 0$ if $\lambda$ is of finite order, and otherwise $d(\lambda)$ is the largest positive integer $d$ for which $\lambda = d\kappa$ for some $\kappa\in H_1(\man)$.   

For example, if $\man$ is the $3$-torus $\tor$, then 
$
\lambda(f) = (p,q,r) \in H_1(\tor) \cong \bz^3
$
where $p$, $q$ and $r$ are the degrees of $f$ restricted to the coordinate $2$-tori, and the divisibility $d(p,q,r)$ is the greatest common divisor of $p$, $q$ and $r$. 

In the next few paragraphs, we discuss these invariants $\lambda$ and $\nu$ in more detail, and provide a natural way, in the special case that $\man$ is the $3$-torus, to transform $\nu$ from a relative invariant into an absolute one, meaning a function of a single map.

First recall that a {\it framing} of a smooth link in $M$ is a homotopy class of trivializations of the normal bundle of the link. It can be represented by an orthonormal triple $(\u,\vv,\t)$ of vector fields along the link with respect to some Riemannian metric on $M$, where $\t$ is tangent to the link.  We can use this to orient the link by $\t$ by insisting that the triple give the orientation on $M$.  Conversely, if the link is already oriented by $\t$, then the framing can be specified by a single unit normal vector field $\u$, as $\vv$ is then determined by the condition that $(\u,\vv,\t)$ be an orthonormal frame giving the orientation on $M$.  In pictures, therefore, we often indicate a framing on an oriented link by simply drawing a thin parallel push-off of the link, recording the tips of the vectors in $\u$.

Now given a map $f:\man\to S^2$ with regular value $*$, the link $\bl = f^{-1}(*)\subset \man$ inherits a framing by pulling back an oriented basis for the tangent space to $S^2$ at $*$, and acquires an orientation from this framing, as above.   Equipped with this framing and orientation, $\bl$ will be called the {\itb Pontryagin link} of $f$ at $\pt$.  

Note that any framed oriented link $\bl$ in $\man$ arises as the Pontryagin link of some map from $M$ to $S^2$.  In particular, the {\itb Pontryagin--Thom construction} produces such a map, given by wrapping each normal disk fiber of a tubular neighborhood of $\bl$ around the $2$-sphere by the exponential map, using the framing to identify the fiber with the disk of radius $\pi$ in the tangent space to $S^2$ at $*$, and sending everything outside the neighborhood to the antipode of $*$.  This construction provides a one-to-one correspondence 
$$
[M,S^2] \ \longleftrightarrow \ \Omega_1^{\text{fr}}(\man)
$$
where $[M,S^2]$ is the set of homotopy classes of maps $\man\to S^2$, and $\Omega_1^{\text{fr}}(\man)$ is the set of framed bordism classes of framed oriented links in $\man$  (see e.g.\ Chapter 7 in Milnor \cite{Milnor65}).  

Now we return to our discussion of the invariants associated with maps $f:\man\to S^2$.  

An easy argument shows that the primary invariant $\lambda(f)$, the homology class of the oriented link $f^{-1}(*)$, is independent of the choice of regular value $*$, and that $\lambda(f)$ is invariant under homotopies of $f$.  Indeed, the preimages $\bl_0$ and $\bl_1$ of any regular values for any pair of maps homotopic to $f$ are bordant in $\man\times[0,1]$ (see Milnor \cite{Milnor65} for a proof).  It follows that $\bl_0$ and $\bl_1$ are homologous in $\man$.  Conversely, homologous links in $\man$ are bordant in $\man\times[0,1]$ by a standard argument going back to Thom \cite{Thom}.   

\begin{comment} 
This follows from transversality and the fact that $H^2(X)=[X,CP^2]$ for $X=\man$ or $\man\times[0,1]$
\end{comment} 

This shows that the partition of $[\man,S^2]$ into subsets $[\man,S^2]_\lambda$ according to their primary invariants $\lambda\in H_1(\man)$ corresponds to the partition of $\Omega_1^{\text{fr}}\man$ into {\it unframed} bordism classes.  


The secondary invariant associated with a pair of bordant framed links measures the obstruction to extending the framings on the links across any bordism between them.    More precisely, given $f_0$ and $f_1$ in $[\man,S^2]_\lambda$ with Pontryagin links $\bl_0$ and $\bl_1$, and an oriented surface 
$\bF \subset \man\times[0,1]$ with $\partial\bF  =  \bl_1\times1 - \bl_0\times0$,  the framings on $\bl_0$ and  $\bl_1$ combine to give a normal framing of $\bF$ along its boundary.  The obstruction to extending this framing across $\bF$ is measured by its relative Euler class $e(\bF)$ in $H^2(\bF,\partial\bF;\pi_1SO(2)) = \bz$,
which in homological terms is the intersection number of $\bF$ with a generic perturbation of itself that is directed by the given framings along $\partial\bF$.   This class depends on the choice of the regular values of $f_0$ and $f_1$ used to define the Pontryagin links, and on the choice of the bordism $\bF$ between the links.  But the residue class of $e(\bF)$ mod $2d(\lambda)$ does not depend on these choices; see Gompf~\cite{Gompf} and Cencelj, Repov{\v s} and Skopenkov~\cite{Cencelj} for details, and also see Auckly and Kapitanksi~\cite{AucklyKapitanski}.  
This residue class 
$$
\nu(f_0,f_1)  \ = \ e(\bF) \textup{ mod }2d(\lambda) \ \in \ \bz_{2d(\lambda)}
$$
will be referred to as the {\itb relative Pontryagin $\nu$-invariant} of $f_0$ and $f_1$. 


\part{Converting the relative Pontryagin $\nu$-invariant into an absolute invariant}


The task of converting $\nu$ into an {\it absolute} invariant, that is, changing it from a function of two variables to a function of one variable, requires the choice of a {\itb base map} $f_\lambda$ in each subset $[\man,S^2]_{\lambda}$ of homotopy classes of maps with primary invariant $\lambda$.  One can then define the {\itb\boldmath absolute Pontryagin $\nu$-invariant} by
$$
\nu(f) \ = \ \nu(f,f_\lambda)
$$
for any $f\in[\man,S^2]_\lambda$.  Whether such choices can be made in a topologically meaningful way depends on the manifold $\man$. 
 
For example, Pontryagin \cite[page 356]{Pontryagin41} explicitly cautioned against trying to make this choice when $\man=S^1\times S^2$.  In this case there are, up to homotopy, exactly two maps to $S^2$ with primary invariant $1\in H_1(S^1\times S^2) = \bz$, meaning degree $1$ on the cross-sectional $2$-spheres in $S^1\times S^2$.  One of these is the projection $f_0(\theta,x)  =  x$ to the $S^2$ factor,  and the other is the twist map $f_1(\theta,x)  =  \rot_\theta(x)$ that rotates the $S^2$ factor once while traversing the $S^1$ factor; here $\rot_\theta$  indicates rotation of  $S^2$ through an angle $\theta$ about its polar axis.  Note that the double twist $f_2(\theta,x)  =  \rot_{2\theta}(x)$ is homotopic to $f_0$.   

What Pontryagin observed is that $f_0$ and $f_1$ differ by an automorphism of $S^1\times S^2$, and so there is no natural way to choose which one should serve as the base map for the homology class $[S^1\times S^2,S^2]_1$.  More precisely, the automorphism $h$ given by $h(\theta,x)  =  (\theta,\rot_\theta(x))$ satisfies $f_0h=f_1$, while $f_1h=f_2$, which is homotopic to $f_0$.  Thus the maps $f_0$ and $f_1$ have equal topological status, and so neither is more basic than the other.

A key feature of this example is the existence of a homotopically nontrivial automorphism of $S^1\times S^2$ that induces the identity on homology.  In general, if a $3$-manifold $\man$ supports such an automorphism $h$, then $\lambda(fh) = \lambda(f)$ for any map $f:\man\to S^2$.   Hence the existence of $h$ provides a potential obstruction to the natural choice of base maps in $[\man,S^2]_\lambda$ for all $\lambda$.  The $3$-torus has no such automorphisms, due to the fact that its higher homotopy groups vanish.   

For each triple of integers $p$, $q$  and $r$,  we now show how to pick out a specific map $f_{pqr}:\tor\to S^2$ having these preassigned cross-sectional degrees, which can serve in a topologically meaningful way as the base map for the set $[\tor,S^2]_{(p,q,r)}$ of all such maps.   

We will describe $f_{pqr}$ by specifying its Pontryagin link $\bl_{pqr}$, as follows.  Choose three pairwise disjoint circles $\calc_s$, $\calc_t$ and $\calc_u$ that are cosets of the coordinate circle subgroups 
$$
S^1_s = S^1 \times 0 \times 0 \ , \ S^1_t = 0 \times S^1 \times 0 \ \text{ and } \ S^1_u = 0 \times 0 \times S^1
$$
of the $3$-torus (where as usual $S^1=\br/2\pi\bz$) with disjoint tubular neighborhoods $\caln_s$, $\caln_t$ and $\caln_u$.  Equip these circles with their {\itb coordinate framings} induced from the Lie framing $(\partial_s,\partial_t,\partial_u)$ of the tangent bundle of $\tor$, that is, $(\partial_t,\partial_u)$ for $\calc_s $, $(\partial_u,\partial_s)$ for $\calc_t$ and $(\partial_s,\partial_t)$ for $\calc_u$.  Then construct $\bl_{pqr}$ from $p$ parallel copies of $\calc_s$ in $\caln_s$ (meaning $p$ distinct cosets of $S^1_s$ lying in $\caln_s$), $q$ copies of $\calc_t$ in $\caln_t$ and $r$ copies of $\calc_u$ in $\caln_u$, all with their coordinate framings, as indicated in \figref{basemaps}.  Thus $f_{pqr}$ wraps the disk fibers of the tubes $\caln_s$, $\caln_t$ and $\caln_u$ around $S^2$ by maps of degree $p$, $q$ and $r$, and is constant elsewhere.


\begin{figure}[h!]
\includegraphics[height=120pt]{FigBaseMaps.pdf}
\put(-128,-2){\small$s$}
\put(-76,122){\small$u$}
\put(1,39){\small$t$}
\put(-110,40){\small$p$}
\put(-90,66){\small$q$}
\put(-50,25){\small$r$}
\caption{Pontryagin link $\bl_{pqr}$ for the base map $f_{pqr}$}
\label{fig:basemaps}
\end{figure}


Here and below, the $3$-torus is pictured as the cube $[0,2\pi]^3$ in $stu$-space with opposite faces identified.  The axes correspond to the coordinate circles $S^1_s$, $S^1_t$ and $S^1_u$, and the coordinate framings are the ``blackboard" framings, i.e.\ those given by parallel push-offs in the projection shown.  The link $\bl_{5\,3\,-2}$ is shown in the figure.  Note that by construction $\bl_{000}$ is empty, so $f_{000}$ is constant.   




\part{Computing the absolute Pontryagin $\nu$-invariant}


Our goal is to give a simple procedure for computing the Pontryagin $\nu$-invariant  of a map $f:\tor\to S^2$ from a ``toral diagram" of its Pontryagin link $\bl$.  


By definition, a {\itb toral diagram} of $\bl$ consists of 
\vspace{.02in}
\begin{indentation}{.05em}{1em}
\begin{enumerate}
\item a classical oriented link diagram $\cald$ in the $2$-torus $\torh$ with {\itb crossings} $\calc$, 
\smallskip
\item a finite set of signed points in $T^2$, the {\itb marked points}, partitioned into
the {\itb isolated} ones $\calm \subset T^2-\cald$, and the {\itb internal} ones $\caln\subset\cald-\calc$, \label{markedpoints} and
\smallskip
\item  integer {\itb framings} for each component of $\cald$ and each point in $\calm$.
\end{enumerate}  
\end{indentation}
\vspace{.02in}

For example, the link $\bl_{pqr}$ above is duplicated in \figref{diagrams}(a) with its toral diagram beneath it, and another example is given in \figref{diagrams}(b).        


\begin{figure}[h!]
\includegraphics[height=175pt]{FigDiagrams.pdf}
\put(-100,24){\tiny$3$}
\put(-39,12){\tiny$2$}
\put(-300,-20){(a) The link $\bl_{pqr}$ and its diagram}
\put(-100,-20){(b) Another example}
\caption{Toral diagrams of framed links in $\tor$}
\label{fig:diagrams}
\end{figure}



It is understood that $\bl$ should project to $\cald\cup\calm$ under the projection $\tor\to\torh$ sending $(s,t,u)$ to $(s,t)$, and so points in $\calm$ correspond to vertical components $\pt\times\pt\times S^1$ in $\bl$, oriented up or down according to the signs.  The points in $\caln$ correspond to transverse intersections of $\bl$ with the {\itb horizontal $2$-torus} \,$\torh\times0$ -- shaded in the figures -- where the sign $+1$ or $-1$ indicates whether the curve points up or down near the intersection. 

To explain the crossings $\calc$, view $\tor$ as the cube $[0,2\pi]^3$ in $stu$-space with opposite faces identified, as before, and $\torh$ as the square $[0,2\pi]^2$ in the $st$-plane with opposite sides identified.  Above $\cald-\caln$, the link $\bl$ resides in $\torh\times(0,2\pi)$.  At a crossing, the over-crossing strand is the one with the larger vertical $u$-coordinate in the cube.

Finally, the framings specify a push-off of $\bl$ by comparison with the blackboard framing of $\cald\cup\calm$ in $\torh$.  These ``blackboard" framings are obtained by pushing $\cald\cup\calm$ off itself in the direction of a normal vector field in $\torh$, and then lifting these push-offs to a collection of framing curves for the components of $\bl$ that we call their {\it $0$-framings}.  For vertical circles, these are just the coordinate framings.  Now the $n$-framing on any given component of $\bl$ is the one obtained from the $0$-framing by adding $n$ full twists, right or left handed according as $n$ is positive or negative.  
  


In these figures we typically indicate the framing on the link in $\tor$ by a thin push-off, and use the convention that the unlabeled components of the diagram have framing zero, that is, the blackboard framing.  We also denote the positive marked points in the diagram with solid dots, and the negative ones with hollow dots.

We have allowed isolated marked points in the definition above so that projections of links such as $\bl_{pqr}$ will qualify as toral diagrams, and to facilitate our later work.  Note, however, that a generic isotopy of $\bl$ will eliminate the set $\calm$ of isolated marked points, converting an $n$-framed isolated marked point -- corresponding to a vertical circle in $\bl$ -- into a small $(n\pm1)$-framed circle with one internal marked point -- corresponding to a spiral perturbation of the vertical circle.   More precisely, using the notation above of solid dots for positive marked points and hollow dots for negative ones, we have


$$
\includegraphics[height=25pt]{FigIso.pdf}
\put(-250,11){$=$}
\put(-205,11){$=$}
\put(-261,3){\small$n$}
\put(-235,-5){\small$n-1$}
\put(-190,-5){\small$n+1$}
\put(-135,10){and}
\put(-85,10){$=$}
\put(-40,10){$=$}
\put(-93,2){\small$n$}
\put(-66,-6){\small$n+1$}
\put(-24,-6){\small$n-1$}




$$
as is readily verified by a suitable picture in the $3$-torus.
 

Now suppose we are given a toral diagram of a Pontryagin link $\bl$ for a map $f:\tor\to S^2$.  We say that the diagram {\itb represents} $f$, and seek to compute $\nu(f)$ from it.

First observe that the primary invariant  
$$
\lambda(f) \ = \ (p,q,r) \label{primary}
$$
is easily read from the diagram.  Indeed $p$ and $q$ (which are the degrees of the projections of $\bl$ to the horizontal circle factors $S^1_s$ and $S^1_t$) are just the intersection numbers of $\cald$ with $S^1_t$ and $-S^1_s$, and $r$ (the degree of the projection of $\bl$ to the vertical circle $S^1_u$\,, or equivalently the intersection number of $\bl$ with the horizontal $2$-torus) is the sum of the signs of all the marked points.  We call $p$ and $q$ the {\itb horizontal winding numbers} of the diagram, and $r$ its {\itb vertical winding number}.   For what follows, we will also need to consider the vertical winding of the individual components of $\bl$.  Each such component $\bl_i$ projects either to some subset $\cald_i$ of $\cald$, or to a point $\calm_i$ in $\calm$ (if $\bl_i$ is vertical).  In either case, we call this projected image the ``$i^\text{th}$ component" of the diagram, and write $r_i$ for the sum of all the marked points that lie on it.  Clearly $r_i$ is just the vertical winding number of $\bl_i$, and $\sum r_i = r$, the total vertical winding number of the diagram. 

To compute $\nu(f)$, we will transform $\bl$ by a sequence of framed bordisms into $\bl_{pqr}$ with some extra twists in the framing.  The number of twists is by definition $\nu(f)$; counting these twists ultimately yields the simple formula for $\nu(f)$ that will be given in \propref{pontryagin}.   

To cleanly state this formula, we assume from the outset that our diagram has no crossings.  There is no loss of generality in doing so since the crossings can be eliminated by {\itb saddle bordisms} of $\bl$, as illustrated in \figref{crossing} (viewing $\bl$ from the top, looking down on a crossing in the horizontal torus) which of course do not change $\nu(f)$.   Furthermore, we will see that the Pontryagin link of a ``generic link" (to be defined in \secref{Aprep}), has a toral diagram without crossings.


\begin{figure}[h!]
\includegraphics[height=70pt]{FigCrossing1.pdf}
\put(-193,28){$\sim$}
\put(-201,17){\tiny bordism}
\put(-87,28){$=$}
\caption{Using saddles to eliminate crossings}
\label{fig:crossing}
\end{figure}


Each such saddle bordism is achieved by adding a $1$-handle, as indicated on the left side of \figref{bordism}, and drawn in full, suppressing one dimension in $\tor$, on the right side.


\begin{figure}[h!]
\includegraphics[height=80pt]{FigBordism.pdf}
\caption{The saddle bordism}
\label{fig:bordism}
\end{figure}


The effect of the saddle bordism on the diagram is easy to describe.  If it is used to eliminate a self-crossing of an $n_i$-framed component $\cald_i$ (meaning $\cald_i$ is the projection of a component $\bl_i$ of $\bl$) then $\cald_i$ splits into two components whose framings must add up to $n_i\pm1$, depending on the sign of the crossing.  Beyond this condition, the framings on the new components can be chosen arbitrarily since twists in the original framing can be shifted along $\bl_i$ at will.  If the saddle bordism is used to eliminate a crossing between distinct components $\cald_i$ and $\cald_j$ of $\cald$ with framings $n_i$ and $n_j$, then the result is a single component with framing $n_i+n_j\pm1$.     

Once we have a toral diagram {\sl without crossings} representing $f$, the extra data needed to compute $\nu(f)$ is the list of {\itb vertical winding numbers} $r_i$ of its components together with one additional integer $n=\sum n_i$, the sum of all the component framings $n_i$, which we call the {\itb total framing} and place as a label next to the diagram. 

To state the formula efficiently, we will use one more list of numbers that is easily read from the diagram.    First pick a basepoint $*$ in $\torh$ away from $\cald\cup\calm$, and then for each $i$, choose an arc $\gamma_i$ that runs from the $i^\text{th}$ component of $\cald\cup\calm$ to $*$.   Now define the {\itb depth} \label{depth} of the $i^\text{th}$ component to be 
$$
d_i \ = \ 2\,\gamma_i\,\dt\,\cald \mod{2\gcd(p,q,r)}

\,,
$$
that is, twice the intersection number in $\torh$ of the arc $\gamma_i$ with the union $\cald$ of the closed curves in the diagram.  This intersection number must be properly interpreted for components of $\cald$.  In this case the initial point of $\gamma_i$ lies on $\cald$, contributing $\pm\frac12$ to the intersection number, and thus $\pm1$ to $d_i$.  It follows that $d_i$ is always an odd integer for components of $\cald$, and an even integer for components of $\calm$, meaning isolated marked points.  An example is shown in \figref{depth}.


\begin{figure}[h!]
\includegraphics[height=120pt]{FigDepth.pdf}
\put(-107,87){\small$\cald_i$}
\put(-100,68){\small$\gamma_i$}
\put(-26,31){\small$\calm_j$}
\put(-20,57){\small$\gamma_j$}
\put(-195,60){$d_i = 2\cdot2\frac12 = 5$}
\put(8,47){$d_j = 2\cdot-1 = -2$}
\caption{Depths of components in the diagram}
\label{fig:depth}
\end{figure}


Of course the depth $d_i$ depends on the choice of arc $\gamma_i$, but only modulo $2\gcd(p,q)$, and so it is certainly well defined modulo $2\gcd(p,q,r)$.  Furthermore, in the formula for $\nu(f)$ below, the depths appear only as coefficients in the sum $\sum d_ir_i$.  It is readily seen that this sum changes by a multiple of $\sum 2r_i = 2r$ when moving the basepoint $*$, and so it is well defined modulo $2\gcd(p,q,r)$, independent of the choices of $*$ and of the arcs $\gamma_i$. 

We can now state the main result of this section.    


\begin{proposition}
\label{prop:pontryagin}
\textbf{\boldmath Let $f:\tor\to S^2$ be a smooth map whose Pontryagin link $\bl$ is represented by a toral diagram in $\torh$ without crossings, with horizontal winding numbers $p$ and $q$, vertical winding number $r$, and total framing $n$.  Then the primary and secondary Pontryagin invariants of $f$ are given by
$$
\begin{aligned}
\lambda(f) \ &= \ (p,q,r) \quad\text{and} \\
\nu(f) \ &= \ n + pq + \textstyle\sum d_ir_i \mod{2\gcd(p,q,r)}
\end{aligned}
$$
where $r_i$ and $d_i$ are the vertical winding numbers and depths $($with respect to any chosen basepoint$)$ of the components of the diagram.}
\end{proposition}


\begin{proof}
The formula for $\lambda(f)$ was derived on page \pageref{primary}, and the formula for $\nu(f)$ is, as explained above, at least well defined modulo $2\gcd(p,q,r)$, independent of the choice of basepoint.  So it remains to verify that this is the correct formula for $\nu(f)$. 

First observe that, in the absence of crossings, the integers $r_i$ are all that are needed to recover the link $\bl$ up to {\sl isotopy}.  In particular, each nonvertical component of $\bl$ can be taken to wind monotonically around the last circle factor of $\tor$. Furthermore, equipped with the total framing $n$, we can recover the framed link $\bl$ up to {\sl framed bordism}.  To see this, note that a pair of saddle bordisms can be used as shown in \figref{framing} to transfer a twist in the framing from any component of $\bl$ to any other, and so we can distribute the framings in any desired way among the components.


\begin{figure}[h!]
\includegraphics[height=80pt]{FigFraming.pdf}
\put(-183,32){$\sim$}
\put(-117,32){$=$}
\put(-55,32){$\sim$}
\caption{Using saddles to transfer twists}
\label{fig:framing}
\end{figure}


We now propose to transform $\bl$ by a sequence of framed bordisms into $\bl_{pqr}$ with some extra twists in the framing.  These correspond to homotopies of $f$ and so do not change the Pontryagin invariant $\nu(f)$.  We will carry this out on a diagrammatic level, transforming our given toral diagram, with total framing $n$, to the diagram for $\bl_{pqr}$ shown in \figref{diagrams}(a) with some total framing, which by definition will equal $\nu(f)$.  So we must simply keep track of the change in the total framing as we proceed.  

We first use saddle bordisms to replace the vertical winding of each non-vertical component $\bl_i$ by $|r_i|$ zero-framed vertical components, at the cost of adding $r_i$ to the total framing.  The new vertical circles are ``adjacent" to $\cald_i$ -- meaning displaced slightly to the {\it right} of it in the projection -- and oriented up or down according to the sign of $r_i$.  

This is illustrated in \figref{winding}.  The net effect on the diagram is to reduce all the vertical winding numbers to zero on the components of $\cald$ (i.e.\ to eliminate the internal marked points $\caln$), to add $\sum|r_j|$ isolated marked points, and to add $\sum r_j$ to the total framing of the diagram, where the sums are only over the non-vertical components of $\bl$.


\begin{figure}[h!]
\includegraphics[height=150pt]{FigWinding.pdf}
\put(-102,100){$\sim$}
\put(-134,5){\small$n$}
\put(-4,5){\small $n+1$}
\caption{Using saddles to replace vertical winding by vertical circles}
\label{fig:winding}
\end{figure}


Since our target is the base link $\bl_{pqr}$ (with extra twists), the vertical circles must be gathered together.  This is the purpose of our base point $*$, which will serve as a gathering spot, and the arcs $\gamma_i$, which will serve as the paths in $\torh$ along which to move the vertical circles which at the moment are adjacent to the $\bl_i$.   At each intersection of $\gamma_i$ with a component of $\cald$, these vertical circles must cross the corresponding strand of $\bl$.   This crossing can be accomplished by a pair of saddle bordisms as indicated in \figref{gathering}, adding $\pm2$ to the diagram framing.   On the diagrammatic level, this can viewed as a two step process, running the bordism shown in \figref{winding} backwards and then forwards, in order to move an isolated marked point across a component of $\cald$, as shown at the bottom of the figure. 


\begin{figure}[h!]
\includegraphics[height=150pt]{FigGathering.pdf}
\put(-240,100){$\sim$}
\put(-110,100){$\sim$}
\put(-275,5){\small$n-1$}
\put(-134,5){\small$n$}
\put(0,5){\small $n+1$}
\caption{Using saddles to gather the vertical circles}
\label{fig:gathering}
\end{figure}


Now it is easy to check that the act of removing the vertical winding of the nonvertical components of $\bl$, and then gathering all the resulting vertical circles (including the original ones corresponding to $\calm$) will add $\sum d_ir_i$ to the total framing of the diagram.  Visually, this process can be thought of as a ``migration" to the base point of all the marked points in the diagram. 

Next use disk bordisms to remove the null homotopic components of $\cald$ (arranging for them to be $0$-framed by storing their twists elsewhere, as explained above) and similarly use annular bordisms to remove any pair of curves that are parallel but oppositely oriented.  The diagram now consists of a $(p,q)$ torus link in $\torh$ (meaning $c$ parallel copies of the $(p',q')$ torus knot, where $p=cp'$ and $q=cq'$ with $p'$ and $q'$ relatively prime) together with $r$ isolated marked points near $*$.  The total framing, which was originally equal to $n$, has changed to $n+\sum d_ir_i$.  

Finally we transform the $(p,q)$ torus link by using saddle bordisms (reversing the process described above for removing crossings) into $p$ copies of $S^1_s$ and $q$ copies of $S^1_t$, grouped as in $\bl_{pqr}$, at the cost of adding $pq$ to the total framing.   Thus we have arrived at $\bl_{pqr}$, having changed the total framing from $n$ to $n+pq + \sum d_ir_i.$  This verifies the stated formula for $\nu(f)$, and completes the proof of \propref{pontryagin}.
\end{proof}


The following application will arise in the proof of \thmref{A} in \secref{A}.

\begin{example}\label{ex:basecase} 

If $f$ is represented by the $\pm(pq+r)$-framed $(p,q)$ torus link in $\torh$, with one component $K$ of vertical winding number $r$, and the rest of vertical winding number zero, then $\lambda(f)  = (p,q,r)$, and choosing a base point adjacent to $K$,
$$
\nu(f) \ = \ (pq+r) + pq + (1\cdot r + 0 + 0) \ = \ 2(pq+r) \ = \ 0 \ \in \bz_{2\gcd(p,q,r)}.
$$
\end{example}
