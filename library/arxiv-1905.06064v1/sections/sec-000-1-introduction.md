---
doc_id: arxiv-1905.06064v1
doc_title: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 1905.06064v1.pdf
source_sha256: 3ffe25c8ee62779d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.982
doc_brief: "ON O’HARA KNOT ENERGIES I: REGULARITY FOR CRITICAL KNOTS — We develop a regularity theory for extremal knots of scale invariant knot ener- gies deﬁned by J. O’hara in 1991."
---
For $\alpha p \geq 4$, $p \geq 2$, the O'hara knot energies\footnote{In this paper we divert from the usual notation of the literature by writing $\frac{p}{2}$ instead of $p$ for the simple reason that the case $p=2$ (in the knot literature: $p=1$) corresponds to the Hilbert-space case of an $L^2$-energy.} $\mathcal{O}^{\alpha,p}$ named after their inventor J.~O'hara \cite{OH91,OH92} are defined for closed Lipschitz curves $\sol: \R/\Z \to \R^3$ from the circle $\R/\Z$ into the three-dimensional space $\R^3$ by
\begin{equation}\label{eq:oharaenergiesnew}
 \mathcal{O}^{\alpha,p}(\sol)= \int_{\R/\Z} \int_{\R/\Z} \brac{\frac{1}{|\sol(x) - \sol(y)|^\alpha} - \frac 1 {\mathcal{D}_\sol(x,y)^\alpha }}^{\frac{p}{2}} |\sol'(x)|\, |\sol'(y) |\ dx\ dy.
\end{equation}
Here, $\mathcal{D}_\sol(x,y)$ denotes the intrinsic distance between $\sol(x)$ and $\sol(y)$ along the curve $\sol$. 


A striking property of an O'hara knot energy is its self-repulsive effect which is in contrast to other geometric energies like e.g. Bernoulli's bending energy. Namely, curves with self-intersections have infinite energy. 


The original definition of the O'hara knot energies in \cite{OH91,OH92} was motivated by the idea of calculating the potential energy of electric charge equidistributed on the given curve. He adapted ideas in the work of Fukuhara \cite{Fukuhara1988} who attempted to use energies to find especially nice representatives of a given knot class.  The subject has found applications in other parts of mathematics and the sciences. Knot energies can help to model repulsive forces of fibres, whenever self-interaction of strands should be avoided. In fact, there is some indication that DNA molecules seek to attain a minimum state of a suitable energy~\cite{Moffatt1996}. There have been several attempts to employ self-avoiding energies for mathematical models in microbiology, see e.g. \cite{Banavar2003}  and references therein for links to polymer science and protein science. Moreover, attraction phenomena may be modeled by a corresponding positive gradient flow \cite{Reiter2009}. Self-repulsive terms can also be used to penalize self-penetration of physical objects, e.g. in elasticity theory \cite{K18}.

From the analytical point of view, one important driving force in this field is the hope that knot energies might lead to a very natural proof of the Smale conjecture. In one of its many equivalent forms this conjecture states that the space of circles is a deformation retract of all Jordan curves. This conjecture was proven by Hatcher \cite{Hatcher1983}. If it could be shown that, in the unknot class, circles are the only critical knots of one of the O'hara energies this could be used to construct a deformation retract proving Smale's conjecture in a straightforward way.

Of course, the central analytic questions for a variational energy are the questions of existence of minimizers, their regularity, and - if possible - even a list or classification of all minimizers. There are two different regimes, analytically: if $\alpha p > 4$ the energy is sensitive to scaling $\sol \mapsto \lambda \sol$, i.e. the size of the knot. Fixing the length of the curve (to ensure existence of minimizers) one finds that the energy is \emph{sub}-critical, e.g. in the sense that sequences of knots with bounded energy (up to a subsequence) converge in the ambient isotopy class. 

For $\alpha p = 4$ the energy $\mathcal{O}^{\alpha,p}$ is invariant under scalings $\sol \mapsto \lambda \sol$. In this case the energy $\mathcal{O}^{\alpha,p}$ measures only the physical shape and does not take into account the size of the knot $\sol$. This is the critical (and thus analytically most challenging) case, e.g. in the sense that sequences of knots with bounded energy may exhibit bubbling phenomena.

Let us also remark that in the (generally in this paper excluded) case $\alpha p < 4$ the energy is not repulsive any more, i.e. self-intersections are permissible.

In this work we will concentrate on the critical case where $\alpha p = 4$. We draw our motivation from the results known in the special case $\alpha = 2$ and $p = 2$, in which the O'hara energy $\mathcal{O}^{2,2}$ is called M\"obius energy. Namely, the following was shown in the groundbreaking work by Freedman, He, and Wang \cite{Freedman1994}.

\begin{theorem}[Freedman-He-Wang]\label{th:FHW}${}$
\begin{enumerate}
\item Minimizers of the M\"obius energy $\mathcal{O}^{2,2}$ exist within any prime knot class.
\item Any local minimizer of $\mathcal{O}^{2,2}$ is of class $C^{1,1}$ when parametrized by arclength.
\end{enumerate}
\end{theorem}
Here, a knot class is the ambient isotopy class of an embedded curve. A knot is called a \emph{prime knot} if it cannot be decomposed into two non-trivial knots. Otherwise it is called a \emph{composite knot}, cf. \cite{BZH}.
Kusner and Sullivan conjectured that there are no minimizers in composite knot classes, supporting their intuition with numerical experiments \cite{Kusner1998}. It is an interesting fact  that the existence in prime knot classes corresponds to what is known for minimizing harmonic maps \cite{SU81} where minimizers exist in generators of the homotopy group and may not exist in other elements of the homotopy group.

The main result of this work is the following regularity theorem extending Freedman, He, Wang's result to the case $\alpha p = 4$. The question of existence will be treated in the forthcoming paper \cite{BRS22}.
\begin{mtheorem}\label{th:regularity}
If $\alpha p = 4$, $p\geq 2$, then any critical knot $\sol$ of $\mathcal{O}^{\alpha,p}$ parametrized by constant speed is of class $C^{1,\sigma}$ for some $\sigma > 0$. In particular this holds for local minimizers.
\end{mtheorem}

Before we explain the main ideas behind the proof of Theorem~\ref{th:regularity} let us gather further facts about O'hara energies.

\subsection{Known results for O'hara energies}
For $\alpha p \geq 4$, $p \geq 2$, circles are the global minimizers of all O'hara energies among curves of fixed length \cite{Abrams2003}. Regarding minimizers in a given knot class: for the scaling-dependent case $\alpha p > 4$, O'hara \cite{OH91,OH92} proved the existence of minimizers in any knot class. His argument relies on the fact that for $\alpha p > 4$ the knot energies are coercive on the space of embedded $C^{1, \beta}$ curves and lower semi-continuous with respect to $C^1$ convergence. This can nowadays be derived from the classification of curves of finite energy in \cite{Blatt12}: curves with a uniform bound on $\mathcal O^{\alpha,p}$ are uniformly bounded in the fractional Sobolev space $W^{1+\frac{\alpha}{2}-\frac{1}{p},p}$ which continuously embeds into $C^{1+\beta}$ for $\beta = \frac \alpha 2 -  \frac 2 p >0$, if $\alpha p > 4$. Observe that this embedding fails if $\alpha p = 4$.

Adapting arguments of O'hara and Freedman, He, and Wang, the existence of symmetric but non-minimizing critical points was proven in  \cite{Gv18,BGRv19} for both, the non scale-invariant case $\alpha p > 4$ and the M\"obius energy $(\alpha,p) = (2,2)$ (in that case only in prime knot classes). This extends previous work of Kim and Kusner on torus knots \cite{Kim1993} and of Cantarella, Fu, Mastin, Royal on symmetric critical knots for the rope-length \cite{Cantarella2014}.

For $\alpha > 2$, $p=2$ it was proven in \cite{BR12} that critical knots are $C^\infty$; analyticity of solutions was shown in \cite{V19}. Furthermore, $C^\infty$-smoothness of critical knots of the M\"obius energy $\mathcal{O}^{2,2}$ is due to He \cite{He00}, under a $C^{1,1}$ initial regularity assumption, and under only finite energy assumption this was obtained in \cite{BRS16}. Analyticity in this case was shown in \cite{BV19}. 

In a series of papers Ishizeki and Nagasawa \cite{IshizekiNagasawa, IshizekiNagasawaII,Ishizeki16, IshizekiNagasawaIII} showed and analyzed various decomposition results for the M\"obius energy and more generally O'hara energies, see also~\cite{N18}.


\subsection{Main ideas behind Theorem~\ref{th:regularity}}
A first na\"ive attempt of proving Theorem~\ref{th:regularity} would be to try to extend the geometric arguments in \cite{Freedman1994}. This attempt is thwarted, however, because their proof crucially exploits the M\"obius invariance of the energy $\mathcal{O}^{2,2}$. But this means that there is no hope of extending these arguments: indeed in Section~\ref{s:distortion} we present strong numerical evidence for the following conjecture.

\begin{conjecture}\label{conj}
The energy $\mathcal{O}^{\alpha,p}$ is M\"obius invariant if and only if $(\alpha,p) = (2,2)$.
\end{conjecture}

The underlying strategy behind the proof of Theorem~\ref{th:regularity} is thus completely different from \cite{Freedman1994}. We relate critical knots of $\mathcal{O}^{\alpha,p}$ to harmonic maps. To achieve this we define a new energy $\mathcal{E}^{\alpha,p}$ in \eqref{eq:E}  with the following property: if a constant-speed parametrized knot $\sol$ is a critical knot of $\mathcal{O}^{\alpha,p}$, then the unit 
tangent  $\solu:= \frac {\sol'}{|\sol'|}$  is a critical map of the energy
$
 \mathcal{E}^{\alpha,p} 
$
restricted to maps into the unit sphere $\S^2$, $\solv: \mathbb R / \mathbb Z \rightarrow \mathbb S^2$, cf. Theorem~\ref{th:eregularity}. 

The energy $\mathcal{E}^{\alpha,p}$ has a nonlinear, nonlocal Lagrangian; and $\mathcal{E}^{\alpha,p}$ is comparable to a $W^{\frac{1}{p},p}(\R/\Z)$-seminorm, where $W^{\frac{1}{p},p}$ denotes the fractional Sobolev space. Critical maps of the $W^{\frac{1}{p},p}$-seminorm are called $W^{\frac{1}{p},p}$-harmonic maps. As a consequence, the described reformulation allows us to interpret critical knots $\sol$ of $\mathcal{O}^{\alpha,p}$-energies as (essentially) fractional harmonic-type maps $\solu$ into the sphere $\S^2$.

Fractional harmonic maps have been studied first by Da Lio and Rivi\`{e}re \cite{DR1dSphere,DR1dMan} in the form of $W^{\frac{1}{2},2}$-harmonic maps. These maps are in turn generalizations of classical harmonic maps, as treated e.g. on two-dimensional domains by H\'elein \cite{Helein-1990}. This theory was extended to $W^{1/p,p}$-harmonic maps into spheres by the third-named author in \cite{SchikorraCPDE14}, see also \cite{MS18}. We will further extend this theory to the case of $\mathcal{E}^{\alpha,p}$-harmonic maps into spheres, see Theorem~\ref{th:eregularity}.  In view of our identification of critical knots $\sol$ for the O'hara energy $\mathcal{O}^{\alpha,p}$ with a critical map $\solu=\frac{\sol'}{|\sol'|}$ with respect to the energy $\mathcal{E}^{\alpha,p}$ we obtain Theorem~\ref{th:regularity}.

Let us remark, that the strategy of interpreting $\sol'$ as a solution to a fractional harmonic-type map equation has already been proven successful in \cite{BRS16} for the case of the M\"obius energy $(\alpha,p) = (2,2)$ -- i.e. the Hilbert-space case. 



















\begin{remark}
A minor technical adaptation of the arguments in this article leads  to the corresponding statement of Theorem~\ref{th:regularity} for so-called open knots, $\sol: \R \to \R^3$, which are critical points of the energy
\begin{equation}\label{eq:oharaenergiesnewo}
 \mathcal{O}^{\alpha,p}_o(\sol)= \int_{\R} \int_{\R} \brac{\frac{1}{|\sol(x) - \sol(y)|^\alpha} - \frac 1 {\mathcal{D}_\sol(x,y)^\alpha }}^{\frac{p}{2}} |\sol'(x)|\, |\sol'(y) |\ dx\ dy.
\end{equation}
\end{remark}


\subsection{Notation}
We will use fairly standard notation: $\iv$ will denote intervals in $\R$. 
In estimates we write $a \aleq b$ if $a \leq C\, b$ for some multiplicative constant $C$. We write $a \ageq b$ if $b\aleq a$, and $a \aeq b$ if $a \aleq b$ and $b \aleq a$.

We work with two types of critical points of energy functionals, which for the convenience of the reader we label differently: we will denote as \emph{critical knots} the critical (i.e. stationary) points $\sol: \R / \Z \to \R^3$ of the O'hara energy $\mathcal{O}^{\alpha,p}$. As \emph{critical maps} we will denote the critical points $\solu: \R / \Z \to \S^2$ of the (yet to be defined) energy functional $\mathcal{E}^{\alpha,p}$.



\subsection{Acknowledgments.}

Financial support is acknowledged as follows
\begin{itemize}
\item FWF Austrian Science Fund, grant no P 29487-N32 (SB)
\item German Research Foundation (DFG) through grant no.~RE-3930/1-1 (PR)
\item German Research Foundation (DFG) through grant no.~SCHI-1257/3-1 (AS)
\item Simons foundation through grant no.~579261 (AS)
\item Daimler and Benz foundation, grant no 32-11/16 (AS) 
\end{itemize}
Part of this work was carried out while A.S. was a Heisenberg fellow.
