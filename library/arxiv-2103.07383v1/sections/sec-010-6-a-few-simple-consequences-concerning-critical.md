---
doc_id: arxiv-2103.07383v1
doc_title: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case"
section_id: sec-010-6-a-few-simple-consequences-concerning-critical
section_title: "A few simple consequences concerning critical knots"
section_number: 6
pages: 23-25
source_pdf: 2103.07383v1.pdf
source_sha256: 9dca35ea16490ad8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.993
doc_brief: "On the Analyticity of Critical Points of the Generalized Integral Menger Curvature in the Hilbert Case — We prove the analyticity of smooth critical points for generalized integral Menger cur- vature"
---
\label{sec:Consequences}

The main result of the paper states that critical points of the generalized integral Menger curvature $\Mpz$ are not only smooth, which was known before, cf. \cite[Theorem\,4]{BlattReiter:2015:Menger}, but also analytic. Recalling and employing special properties for analytic functions, we hence decude a few simple corollaries for critical knots of $\Mpz$ and some other knot energies.

The following statements hold for any functional $\EL: C^0(\R/\Z,\R^3) \rightarrow (0,\infty]$ whose (arc-length parametrized) critical points with respect to fixed length are analytic. As a consequence, the results also apply to the generalized integral Menger curvature $\Mpz$ and some of O'Hara's knot energies, cf. \cite{BlattVorderobermeier:2019:CriticalMoebius,Vorderobermeier:2019:CriticalOHara}.

Central to these consequences is a real version of the identity theorem. It is a well-known result for analytic functions which easily carries over to the periodic case:
\begin{proposition}
\label{propositionRealIdentityTheorem}
    If two analytic functions on $\R/\Z$ are identical at infinitely many distinct points, they are identical everywhere.
\end{proposition}
\begin{proof}
    Let $\gamma,\eta : \R/\Z \to \R^3$ be analytic and without loss of generality $t_1<t_2< \ldots \in [0,1)$ such that $\gamma(t_i)=\eta(t_i)$ for all $i \in \N$.
    Define $g,h: (-1,2) \to \R^3$ as the restrictions of $\gamma$ and $\eta$ to $(-1,2)$ which are clearly also analytic.
    As $t_i \in [0,1]$ for all $i \in \N$, we have a subsequence converging to $t_0 \in [0,1]\subseteq(-1,2)$, so by \cite[Corollary~1.2.7]{KrantzParks:2002:Aprimerofrealanalyticfunctions}, $g=h$ and thus $\gamma = \eta$.
\end{proof}

\begin{lemma}
    \label{lemma:zerosAnalyticFunctions}
    Let $\gamma \colon \R/\Z \to \R^3$ and $F: \R^3 \to \R$ both be analytic. Then, $F\circ \gamma$  either has finitely many roots or is uniformly zero.
\end{lemma}
\begin{proof}
    $F \circ \gamma \colon \R/\Z \to \R$ is analytic as a composition of analytic functions (see e.g. \cite[Proposition~2.2.8]{KrantzParks:2002:Aprimerofrealanalyticfunctions}).
    Using the zero function in \thref{propositionRealIdentityTheorem}, $F\circ \gamma$ either is uniformly zero or has only finitely many roots.
\end{proof}

\begin{proposition}
	\label{corollary:UnknotEllipsoidHyperplane}
	Let $\gamma \in C^1(\R/\Z,\R^3)$ be a simple curve parametrized by arc-length which is a critical point of $\EL$.
	Then, it is the unknot or it has only finitely many intersections with any hyperplane or sphere	in $\R^3$.
	In particular, $\gamma$ cannot have straight segments.
\end{proposition}
\begin{proof}
	First of all, let us consider any hyperplane with normal vector $n\in\R^3$ and position vector $x_0\in\R^3$, described by the equation $F(x)=0$, where  $F:\R^3\rightarrow\R$, $F(x)= \langle n,x-x_0\rangle$. Furthermore, let $\gamma:\R/\Z\rightarrow \R^3$ be a critical point of $\EL$ that is simple and parametrized by arc-length. We then observe that both $F$ and $\gamma$ are analytic, which is why we can apply \thref{lemma:zerosAnalyticFunctions} and observe that the curve $\gamma$ either intersects the hyperplane finitely many times or is entirely contained therein. In the latter case we obtain the unknot, which is the only simple planar knot, cf. \cite[p.~5]{CrowellFox:1977:Introductiontoknottheory} or \cite[Chapter~VI,~18.]{Newman:1951:ElementsOfTopology}.
    If $\gamma$ contains a straight segment, this segment is in particular contained in two distinct hyperplanes.
    Thus, the whole curve has to be contained in both hyperplanes and therefore has to be a straight line which is impossible for a closed $C^1$-curve of finite length.
	
	We then turn our focus to any sphere with center $x_0\in\R^3$ and radius $r>0$, described by the equation $F(x) =0$, where $F:\R^3 \rightarrow \R$, $F(x) = |x-x_0|^2 -r^2$.
    Therefore, similarly to the hyperplane, \thref{lemma:zerosAnalyticFunctions} gives us that any critical analytic knot $\gamma$  of $\EL$ either intersects the sphere finitely many times or is entirely contained therein. 

	In the second case, we would intuitively expect to obtain the unknot by applying a stereographic projection from the sphere to the plane and then argue as above. To make this rigorous, we need to construct an ambient isotopy, cf. \cite[Chapter~8.1]{Hirsch:1976:DifferentialTopology}, to avoid any kind of self-intersection or pull-tight phenomena during the projection process. 
	To simplify the upcoming computations, we assume that the sphere is the unit sphere centered in the origin and that the knot $\gamma$ on the sphere does not intersect the north pole of the sphere. We omit the proof that translations and dilations of the sphere do not change the knot type of the spherical knot and remark that stereographic projections can be done from any other point on the sphere as well. The existence of such point on the sphere, which the knot $\gamma$ does not intersect, is ensured due to the fact that $\gamma$ is rectifiable. Furthermore, note that since the curve $\gamma$ is continuous, there exists an $r>0$ such that $\gamma$ does not intersect a ball around the north pole with radius $r$.
	
	We begin with constructing a $C^1$-isotopy from $\gamma$ to the stereographic projection of $\gamma$ from the north pole onto the plane $z=0$ denoted by $\tilde \gamma$. Note that $\tilde \gamma$ is indeed a $C^1$-embedding: As $\gamma\in C^\omega(\R/\Z,\R^3)$ is a diffeomorphism onto its image and the stereographic projection $P:\mathbb S^2\setminus{(0,0,1)} \rightarrow \R^2$ given by $P(x,y,z)= (\frac{x}{1-z},\frac{y}{1-z})$ with inverse function $P^{-1}(u,v) = \tfrac{1}{u^2+v^2 +1}(2u,2v,u^2+v^2 -1)$ is a diffeomorphism from the sphere without the north pole to the plane $z=0$, also $\tilde \gamma \in C^1(\R/\Z,\R^3)$ is diffeomorphic onto its image. We then define the map $h:\R/\Z \times [0,1]\rightarrow \R^3$ by
	\[
		h_t(w):=(1-t)\gamma(w) + t \tilde \gamma (w),
	\]
    which is continuously differentiable in time and space.
    
    To see that $h$ is a $C^1$-isotopy (cf.\ \cite[Section~8.1]{Hirsch:1976:DifferentialTopology}), we construct a continuously differentiable left-inverse of each $h_t$ and thus show that $h_t$ is a $C^1$-embedding.
    First note that by the nature of stereographic projection, $h_t(w)$ lies on the unique straight line passing through both the north pole $N$ and $\gamma(w)$.
    Since $\gamma$ lies on the sphere and does not contain $N$, this line does not contain any other points of $\gamma$ or $h(\tilde w,[0,1])$ for any $\tilde w \ne w$.
    This means that for any $x \in h_t(\R/\Z)$, we may obtain $w=h_t^{-1}(x)$ as $\gamma^{-1}(y)$, where $y=\lambda N + (1-\lambda)x$ with $\abs{y}=1$.
    Solving for $\lambda \in \R$ yields either $\lambda=0$, which we may safely ignore since it corresponds to $y$ being the north pole, or $\lambda=\frac {\abs{x}^2-1} {\abs{x-N}^2}$.
    As $x$ has to stay away from the north pole, we found a $C^1$ right-inverse of $h_t$ and so, $h$ is a $C^1$-embedding.
    
    Obviously, also 
	\[
		h(\cdot,0) = \gamma \quad \textnormal{and} \quad h(\cdot,1) = \tilde \gamma
	\]
	hold. Now by \cite[Section~8.1,~Exercise~4]{Hirsch:1976:DifferentialTopology} or \cite[Theorem~1.2]{Blatt:2009:NoteOnIsotopies}, we can extend the $C^1$-isotopy between $\gamma$ and $\tilde \gamma$ to an ambient isotopy of $\R^3$ and therefore obtain that the knot type is preserved throughout the stereographic projection.
\end{proof}

As a direct consequence of \thref{lemma:zerosAnalyticFunctions} and  \thref{corollary:UnknotEllipsoidHyperplane}, we obtain the following. 
\begin{corollary}
	Let $\gamma \in C^1(\R/\Z,\R^3)$ be a simple curve parametrized by arc-length which is a critical point of $\EL$ and let $F:\R^3 \rightarrow \R$ be an analytic map that describes an implicit surface $F(x,y,z)=0$.
	Then, the curve $\gamma$ either is entirely contained in the implicit surface $F(x,y,z)=0$ or has only finitely many intersections with it. In particular, if the given surface is ambient isotopic to a sphere or a hyperplane, the curve $\gamma$ is the unknot or has finitely many intersections with the surface.
\end{corollary}

\begin{corollary}
    Let $\gamma,\eta$ be critical points of $\EL$ which are parametrized by arc-length.
    As soon as
    \[
        \gamma(t)=A\eta(t) + x_0
    \]
    for fixed $A\in \R^{3\times 3}$, $x_0 \in \R^3$, and infinitely many distinct $t \in [0,1)$, we have $\gamma = A \eta + x_0$.
\end{corollary}
\begin{proof}
    Note that by assumption, $\gamma$ and $\eta$ are analytic.
    Then, the statement follows from the fact that $A\eta + x_0$ is analytic as well and applying \thref{propositionRealIdentityTheorem}.
\end{proof}
    



\section{Acknowledgements}

Daniel Steenebrügge acknowledges support by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – project number 320021702/GRK2326 –  \emph{Energy, Entropy, and Dissipative Dynamics (EDDy)} and Nicole Vorderobermeier by the Austrian Science Fund (FWF), Grant P29487. Funding from RWTH Aachen University for Nicole Vorderobermeier's research visit is also gratefully acknowledged.

In addition, the authors would like to sincerely thank Simon Blatt for his constant support and indispensable discussions throughout the development of this research paper, Heiko von der Mosel for his generous support and hospitality as well as fruitful discussions, from which Section \thref{sec:Consequences} emerged, and Philipp Reiter for having a sympathetic ear for the authors and giving important hints to deal with some filthy estimates in Section \thref{subsec:FractionalLeibnizRule}.
