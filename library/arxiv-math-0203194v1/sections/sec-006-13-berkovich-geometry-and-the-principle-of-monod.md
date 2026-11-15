---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-006-13-berkovich-geometry-and-the-principle-of-monod
section_title: "Berkovich geometry and the principle of monodromy"
section_number: 1.3
pages: 17-20
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.856
latex_coverage_ratio: 0.988
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\begin{para}
 Rigid analytic spaces are endowed with a 
 Grothendieck generalized topology, and their
 structure sheaf is a sheaf with respect to this topology. Hence
 it cannot be said to satisfy the principle of
 unique continuation in the strict sense of \defref{dfn-unique-cont}.
 Moreover, there is no non-trivial path in such spaces.  Therefore,
 rigid geometry is not a suitable setting for discussing $p$-adic 
 analytic continuation in an intuitive way.

 In contrast, Berkovich's viewpoint on $p$-adic geometry does 
 not suffer from these drawbacks: Berkovich's
 analytic spaces are genuine locally ringed topological spaces, which 
 are even locally arcwise connected. We refer to
 \cite{spasalc} for a compact technical presentation.
\end{para}

\begin{para}
 The buildings blocks are the same: affinoid algebras $\matheur{A}$
 (called strictly affinoid algebras by Berkovich), \ie topological
 $K$-algebras isomorphic to quotients of rings of restricted power
 series. 
 However, instead of attaching to $\matheur{A}$ its maximal spectrum
 $\mathrm{Spm}(\matheur{A})$ as in rigid geometry, 
 Berkovich analytic geometry deals with the {\it affinoid space}
 $\matheur{M}(\matheur{A})$ of all bounded multiplicative seminorms
 on $\matheur{A}$.

 This ``spectrum'' contains ``more points'' than the maximal spectrum
 $\mathrm{Spm}(\matheur{A})$, namely something 
 like ``generic points'', which ``complete'' $\mathrm{Spm}(\matheur{A})$.
 There is a natural inclusion $\mathrm{Spm}(\matheur{A})\subseteq 
 \matheur{M}(\matheur{A})$ which identifies $\mathrm{Spm}(\matheur{A})$
 with the subspace of all seminorms $|\cdot|$ with
 $\matheur{A}/\Ker |\cdot| =\C_p$.
 This ``completion'', in fact, simplifies the topology; e.g.\ Berkovich
 analytic spaces are locally arcwise connected. 
\end{para}

\begin{para}
 {\itshape Berkovich's affinoids.\ }
 Let us be a little more precise about the definition of 
 {\it affinoid spaces} in Berkovich geometry.
 Let $\matheur{A}$ be an affinoid algebra over a complete subfield $K$ of 
 $\C_p$.

 \begin{enumerate}
  \item A point of $\matheur{M}(\matheur{A})$ is a bounded multiplicative
	seminorm on $\matheur{A}$.
  \item The topology of $\matheur{M}(\matheur{A})$ is the weakest one so
	that the mapping
	$\matheur{M}(\matheur{A})\ni\chi\mapsto\chi(f)\in \R_{\ge 0}$
	is continuous for any $f\in\matheur{A}$.
  \item The sheaf of rings $\OO_{\matheur{M}(\matheur{A})}$ is defined by 
	$\Gamma(U,\OO_{\matheur{M}(\matheur{A})})=\varprojlim\matheur{A}_V$, 
	where $V$ runs over finite unions $\bigcup V_i$ of affinoid
	domains contained in $U$, and
	$\matheur{A}_V= \Ker\bigl(\prod_i\matheur{A}_{V_i}
	\rightrightarrows
	\prod_{ij}\matheur{A}_{V_i\cap V_j}\bigr)$, $\matheur{A}_{V_i}$
	being the affinoid algebra attached to the affinoid domain $V_i$.
 \end{enumerate}

 The value of a ``function'' $f\in \matheur{A}$ at a point $\chi\in 
 \matheur{M}(\matheur{A})$ is its image in the field
 $\matheur{A}/\Ker\chi$. This field inherits the absolute value induced by 
 the seminorm $\chi$, and its completion is
 denoted by $\mathscr{H}(\chi)$.\index{000H@$\mathscr{H}(\;)$}
\end{para}

\begin{exa}\label{exa-berkovich-space}
Let $K\{t\}$ denote the ring of restricted power series in one
variable.
Let us assume, for simplicity, that $K$ is algebraically closed.
In rigid geometry, the maximal spectrum $\mathrm{Spm}(K\{t\})$ is
just the closed disk $\matheur{D}(0,1^{+})$ in $K$ of radius $1$ in the usual sense.
In $\matheur{M}(K\{t\})$, the following four kinds of points occur:
\begin{enumerate}
 \renewcommand{\labelenumi}{(\arabic{enumi})}
 \item classical points (\ie those coming from $\mathrm{Spm}(K\{t\})$):
       $x\in\matheur{D}(0,1^{+})$, $\chi_x(f)=|f(x)|_K$ for $f\in K\{t\}$,
 \item  generic points of disks: $\chi=\eta_{x,r}$ for $0<r\leq 1$ with 
       $r\in |K^{\times}|$, 
       $\chi(f)=|f|_{\matheur{D}(x,r^{+})}$ (the sup-norm), 
 \item the same, for $r\not\in |K^{\times}|$,
 \item generic points of infinite decreasing families
       $\{\matheur{D}_{\alpha}\}$
       of closed disks with radius $\leq 1$: 
       $\chi(f)=\mathrm{inf}|f|_{\matheur{D}_{\alpha}}$.
\end{enumerate}

\vspace{2ex}
\begin{figure}[h]
 \setlength{\unitlength}{1pt}
 \begin{picture}(150,60)(0,0)
  
  
  \put(25,10){\line(1,1){35}}
  \put(95,10){\line(-1,1){35}}
  \put(25,9){\makebox(0,0)[c]{$\bp$}}
  \put(95,9){\makebox(0,0)[c]{$\bp$}}
  \put(60,44){\makebox(0,0)[c]{$\bp$}}
  \put(45,29){\makebox(0,0)[c]{$\bp$}}
  \put(55,58){\makebox(0,0)[l]{$\eta_{x,|x-y|}$}}
  \put(17,0){$x$}
  \put(96,0){$y$}
  \put(20,35){$\matheur{\eta}_{x,r}$}
  
 \end{picture}
 \caption{Generic points and paths on a Berkovich space.}
 \label{pic1}
\end{figure}
\vspace{1ex}

Therefore, two arbitrary distinct points in $\matheur{M}(K\{t\})$ can be 
connected by a unique path.
For example, two points of type (1), $x$ and $y$, are connected by a
path consisting of points of type (2) and (3) associated to the disks
$\matheur{D}(x,r^{+})$ and $\matheur{D}(y,r^{+})$ for $0<r\leq |x-y|$.
The complement of a point of type (1) or (4) is connected.
The affine line $\mathbb{A}^1$ is the union of the affinoid spaces
associated to the algebras of power series convergent in 
$\matheur{D}(0,r^{+})$, and the projective line $\mathbb{P}^1$ is the
Alexandroff compactification of $\mathbb{A}^1$.
\end{exa}

\begin{rem}
 Adding generic points to rigid spaces 
 to come up with Berkovich spaces simplifies the topology in contrast to 
 what happens in algebraic geometry, when
 generic points are added to varieties to produce schemes.
 Actually Berkovich's generic points are closed, unlike Grothendieck's
 ones.
\end{rem}

\begin{para}\label{para:strict-analytic}
 The construction of (strictly) analytic $K$-spaces by gluing affinoid
 spaces together is a little delicate (one is not gluing open
 subspaces); we refer to \cite{ecfnas}.  These spaces are \emph{locally 
 compact, locally countable at infinity, and locally arcwise connected.} 

 There is a fully faithful functor between Berkovich's Hausdorff 
 (strictly) analytic $K$-spaces and rigid analytic varieties: at the
 level of underlying sets, this functor sends a space $S$ to the subset of
 ``classical points'', \ie points $s$ for which $[\mathscr{H}(s):K]<\infty$.

 This functor establishes \emph{an equivalence of categories 
 between the category of paracompact (strictly)
 analytic $K$-spaces and quasi-separated rigid spaces over $K$ having 
 an admissible affinoid covering of finite type}.

 This equivalence respects the notion of dimension
 (topological dimension in the case of Berkovich analytic spaces), as
 well as the standard properties of local rings such as: reduced,
 normal, smooth..., and the properties: finite, \'etale...  of
 morphisms. Also, a paracompact analytic space is connected (in the
 usual sense) if and only if the corresponding rigid space does not
 admit an admissible covering by two disjoint non-empty open subsets.

 
 Furthermore, there is a canonical functor ``analytification''
 \begin{equation*}
  \left\{
  \begin{matrix}
   \text{separated schemes}\\
   \text{locally of finite type}\\
   \text{over $K$}
  \end{matrix}
  \right\}
  \rightarrow
  \left\{
  \begin{matrix}
   \text{paracompact (strictly)}\\
   \text{analytic $K$-spaces}
  \end{matrix}
  \right\}
 \end{equation*}
 \noindent
 and a canonical functor ``generic fiber''
 \begin{equation*}
  \left\{
  \begin{matrix}
   \text{separated formal schemes locally}\\
   \text{finitely presented over $\mathcal{O}_K$}
  \end{matrix}
  \right\}
  \rightarrow
  \left\{
  \begin{matrix}
   \text{paracompact (strictly)}\\
   \text{analytic $K$-spaces}
  \end{matrix}
  \right\}.
 \end{equation*}
\end{para}

\begin{para}\label{para:p-adic-manifold}
 {\itshape $p$-adic manifolds.} We shall be mainly 
 concerned with paracompact (strictly) $K$-analytic spaces $S$ which
 satisfy the following assumption:
 \begin{quote}
  any $s\in S$ has a neighborhood $U(s)$ which is isomorphic 
  to an affinoid subdomain of some space
  $V_s$ which admits locally an \'etale morphism to the affine space 
  $\mathbb{A}^{\dim S}$.
 \end{quote}
 For convenience, we shall call such a space $S$ a {\it
 $K$-manifold}\index{Kmanifold@$K$-manifold}, and simply 
 a {\it $p$-adic manifold}\index{padicmanifold@$p$-adic manifold} if $K=\C_p$.

 \noindent It is an important result of V. Berkovich \cite{spasalc}
 that \emph{$p$-adic manifolds are locally contractible}.  Therefore
 they have universal coverings. 
\end{para}

\begin{pro}  
 The structure sheaf of any $p$-adic 
 manifold $S$ satisfies the principle of unique
 continuation, and (equivalently) the principle of monodromy.
\end{pro}
\begin{proof} 
 Since the principle of unique continuation is local, we may replace $S$
 by the neighborhood $U(s)$ of any 
 point $s$ given in advance. Thus we may assume that $S$ 
 itself is affinoid: $S=\matheur{M}(\matheur{A})$,
 and connected, and we have to show that the homomorphism 
 $\iota_s:\;\matheur{A}\rightarrow \matheur{A}_s\simeq
 \underset{s\in V}{\liminj}\matheur{A}_V$ is injective ($V$ runs over
 the affinoid neighborhoods of $s$).  This follows from the
 fact that the homomorphism of completion at 
 $s : \matheur{A}\rightarrow  \widehat{\matheur{A}}_s =
 \underset{n}{\limproj}\matheur{A}/\mathcal{I}_s^n\;$ is injective and factors
 through $\iota_s$.
\end{proof}  

In the case of curves (\ie $p$-adic manifolds of dimension $1$),
analytic continuation is particularly intuitive, because there is a basis
of open subsets $\mathcal{U}$ with finite boundary such that two arbitrary
points in $\mathcal{U}$ are connected by a unique geometric path lying in
$\mathcal{U}$.
