---
doc_id: arxiv-1101.3374v1
doc_title: "Pontryagin invariants and integral formulas for Milnor's triple linking number"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-9
source_pdf: 1101.3374v1.pdf
source_sha256: 01d76c1d259c1d51
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.996
doc_brief: "Pontryagin invariants and integral formulas for Milnor's triple linking number — To each three-component link in the 3-sphere, we associate a geometrically natural characteristic map from the 3-torus"
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
