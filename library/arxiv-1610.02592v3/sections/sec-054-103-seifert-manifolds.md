---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-054-103-seifert-manifolds
section_title: "Seifert manifolds"
section_number: 10.3
pages: 321-339
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.945
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We now enlarge the class of circle bundles over surfaces by admitting some kind of singular fibres. We introduce the \emph{Seifert fibrations}, whose total spaces are called \emph{Seifert manifolds}. These manifolds were introduced by Herbert Seifert in 1933 and fit perfectly in the much more recent geometrisation perspective: in the next chapter we will introduce the eight three-dimensional geometries, and prove that six of them are realised precisely by the Seifert manifolds.


\subsection{Definition}
We define the Seifert manifolds as Dehn fillings of trivial bundles over surfaces with boundary. Here are the details.

Let $M$ be the (unique) oriented bundle $S\timforsetil S^1$ over a compact connected (possibly non-orientable) surface $S$ with boundary. We denote by $S$ the zero-section.

Let $T_1,\ldots, T_k$ be the boundary tori of $M$. On each $T_i$ we choose an orientation for the meridian $m_i=T_i\cap \partial S$ and for the fibre $l_i$ of the bundle so that the basis $(m_i,l_i)$ for $H_1(T_i,\matZ)$ be positively oriented.
 
A $(p_i,q_i)$-Dehn filling on $T_i$ kills the slope $p_im_i + q_il_i$. We say that the Dehn filling is \emph{fibre-parallel} if $p_i=0$, \emph{i.e.}~if it kills a fibre.

\begin{defn}
A \emph{Seifert manifold} is any 3-manifold $N$ obtained from $M$ by Dehn filling some $h\leqslant k$ boundary tori in a non-fibre-parallel way, that is with $p_i\neq 0$ for all $i$.\index{Seifert manifold} 
\end{defn}

The Seifert manifold is closed if $h=k$, and has $k-h$ boundary tori otherwise. It is not important to know which $h$ tori are filled, in virtue of the following.

\begin{prop}
Every permutation of the boundary tori is realised by a self-diffeomorphism of $M$ that preserves the pairs $\pm (m_i,l_i)$.
\end{prop}
\begin{proof}
Every permutation of the boundary circles of $S$ is realised by a self-diffeomorphism of $S$, that extends orientation-preservingly to the orientable $I$-bundle and its double $M$.
\end{proof}

The pair $(p_i,q_i)$ is determined up to sign, so we can always suppose $p_i>0$ and we fully encode the Seifert manifold $N$ using the following notation: 
\begin{equation} \label{Seifert:notation:eqn}
N = \big(\hat S, (p_1,q_1), \ldots, (p_h, q_h)\big)
\end{equation}
where $\hat S$ is $S$ with $h$ boundary components capped. The reason for using $\hat S$ instead of $S$ is that $N$ has a particular fibration onto $\hat S$, as we will soon see. Before constructing this fibration we list some simple examples that should hopefully help the reader to familiarise with the notation (\ref{Seifert:notation:eqn}), that will be used extensively in the whole chapter.

\begin{example}
The Seifert manifold $\big(S_g,(1,e)\big)$ is the circle bundle over the orientable genus-$g$ surface $S_g$ with Euler number $e$, by construction. In particular $\big(S_g,(1,0)\big) = S_g \times S^1$.
\end{example}

\begin{example}
The Seifert manifold $\big( S^2, (p,q) \big)$ is diffeomorphic to the lens space $L(q,p)$.
\end{example}

The following facts follow from Exercise \ref{fill:T:ex}.

\begin{ex} \label{solid:ex}
The Seifert manifold $\big(D^2, (p,q)\big)$ is a solid torus.
\end{ex}

In the following exercise, it should be clear that the resulting manifold is a lens space (by Exercise \ref{fill:T:ex}) and the hard part is to check carefully that the proposed lens space parameters are correct.
\begin{ex} \label{two:lens:ex}
The Seifert manifold $\big(S^2, (p_1,q_1), (p_2, q_2)\big)$ is the lens space $L (p_1q_2 + q_1p_2, rq_2 + sp_2)$
where $r,s$ are such that $p_1s-q_1r=\pm 1$. In particular, this Seifert manifold is $S^3$ when $p_1q_2+q_1p_2 = \pm 1$.
\end{ex}


\subsection{Seifert fibrations}
As we anticipated, a Seifert manifold $N$ as in (\ref{Seifert:notation:eqn}) possesses some kind of singular fibration over the filled surface $\hat S$. We clarify this point here by defining the notion of \emph{Seifert fibration}. 

Let $(p,q)$ be two coprime integers with $p>0$. A \emph{standard fibered solid torus} with coefficients $(p,q)$ is the solid torus\index{solid torus!standard fibered solid torus} 
$$D \times [0,1]/_\psi$$
where $\psi\colon D \times 0 \to D \times 1$ is a rotation of angle $2\pi \frac qp$. The fibration into vertical segments $\{{\rm pt}\} \times [0,1]$ extends to a fibration into circles of the solid torus. The central fibre obtained by identifying the endpoints of $0 \times [0,1]$ is the core of the solid torus, and every non-central fibre winds $p$ times around the core of $M$: see Figure \ref{Seifert_fibration:fig}.

\begin{figure}
\begin{center}
\includegraphics[width = 2.5 cm] {\iftoggle{BW}{Seifert_fibration-BW}{Seifert_fibration}}
\nota{A standard fibered solid torus. We identify the top and bottom discs by a $2\pi \frac qp$ rotation, for some $q$ coprime with $p$. Here $p=5$. Every non-central fibre (\iftoggle{BW}{light grey}{green}) winds $p$ times along the central fibre (\iftoggle{BW}{dark grey}{red}).}
\label{Seifert_fibration:fig}
\end{center}
\end{figure}

The positive number $p$ is the \emph{multiplicity} of the central fibre. If $p=1$ the fibered solid torus is diffeomorphic to the usual product fibration $D\times S^1$ and the central fibre is \emph{regular}. If $p>1$ the central fibre is \emph{singular}.

\begin{defn}
A \emph{Seifert fibration} is a partition of a compact oriented 3-manifold $N$ with (possibly empty) boundary into circles, such that every circle has a fibered neighbourhood diffeomorphic to a standard fibered solid torus.\index{Seifert fibration}
\end{defn}

Let $S$ be the topological space obtained from $N$ by quotienting circles to points.

\begin{prop}
The space $S$ is a compact connected surface with (possibly empty) boundary.
\end{prop}
\begin{proof}
Every standard fibered solid torus quotients to a disc: a sector $z= \rho e^{i\theta}$ with $0\leqslant \rho \leqslant 1$ and $0\leqslant \theta \leqslant \frac{2\pi}p$ with two edges $\theta=0$ and $\theta = \frac{2\pi}p$ identified by a rotation. This disc actually looks like a ``cone'', and this motivates the following discussion.
\end{proof}

The map $N \to S$ is in fact what we call a Seifert fibration. The surface $S$ may have boundary and may be non-orientable, and its interior has a natural orbifold structure: if the preimage of $x\in S$ is a fibre of order $p$, we see $x$ as a cone point of order $p$, see Section \ref{orbifold:surface:subsection}. If $N$ has boundary, then $S$ also has, and we say that $S$ itself is an orbifold for simplicity although we actually mean only its interior. Morally, we should consider the fibration $N\to S$ as a circle bundle over the orbifold $S$.

A Seifert fibration without singular fibres is just an ordinary circle bundle. 
We now show that Seifert manifolds and Seifert fibrations are more or less the same thing. 

\begin{prop} 
The Seifert manifold
\begin{equation*} 
N = \big(S, (p_1,q_1), \ldots, (p_h, q_h)\big)
\end{equation*}
has a Seifert fibration $N \to S$ over the orbifold 
$$(S, p_1,\ldots, p_h).$$
Every Seifert fibration arises in this way.
\end{prop}
\begin{proof}
The Seifert manifold $N$ is obtained by filling $h$ components of a bundle $M=S'\timforsetil S^1$. The bundle $M \to S'$ extends to a Seifert fibration $N \to S$ where the orbifold $S$ is obtained from $S'$ by attaching $h$ discs with cone points $p_1,\ldots, p_h$.

More precisely, we fill each boundary torus $T_i$ of $M$ with a solid torus having meridian $\mu_i= p_im_i + q_il_i$. We fix a longitude $\lambda_i= r_im_i + s_il_i$ for this solid torus by choosing $r_i,s_i$ with $p_is_i-q_ir_i=1$. We get $l_i = p_i\lambda_i - r_i\mu_i$. By hypothesis the Dehn filling is not fibre-parallel, hence $p_i\neq 0$ and the fibration $M\to S'$ extends to a standard fibration of the solid torus with coefficients $(p_i,-r_i)$.

Every Seifert fibration $N\to S$ arises in this way: if we remove the singular fibres (or a regular one, if there are not) we get an ordinary circle bundle over a surface with boundary, which is trivial. Therefore $N$ is a Dehn filling of this trivial bundle, hence a Seifert manifold.
\end{proof}

We have seen that the notation
\begin{equation} \label{notation:eqn}
N = \big(S, (p_1,q_1), \ldots, (p_h, q_h)\big)
\end{equation}
defines a Seifert fibration $N \to S$ and a Seifert manifold $N$.

\begin{example} \label{bad:example}
If the orbifold $S$ is a disc with at most one singular point then $N$ is a standard fibered solid torus. If $S$ is $S^2$ with at most $2$ singular points then $N$ is a lens space: see Exercises \ref{solid:ex} and \ref{two:lens:ex}.
\end{example}


\subsection{Classification of Seifert fibrations}
We say that two Seifert fibrations $\pi_1\colon N_1\to S$, $\pi_2\colon N_2 \to S$ are \emph{isomorphic} if there is a diffeomorphism $\psi\colon N_1 \to N_2$ such that $\pi_1 = \pi_2\circ \psi$. Two different notations as in (\ref{notation:eqn}) may describe isomorphic fibrations, but this phenomenon is completely understood.

\begin{prop} \label{S:moves:prop}
Two notations as in (\ref{notation:eqn}) describe two orientation-preservingly isomorphic Seifert fibrations if and only if they are related by a finite sequence of the following moves and their inverses:
\begin{align}
(p_i,q_i), (p_{i+1},q_{i+1}) & \longmapsto (p_i, q_i+p_i), (p_{i+1},q_{i+1}-p_{i+1}), \label{Seifert:1:eqn} \\
(p_1,q_1), \ldots, (p_h, q_h) & \longmapsto (p_1,q_1), \ldots, (p_h, q_h), (1,0), \label{Seifert:2:eqn} \\
(p_i,q_i) & \longmapsto (p_i,q_i+p_i) \quad {\rm if}\ \partial N \neq\emptyset, \label{Seifert:3:eqn}
\end{align}
and permutations of the pairs $(p_i,q_i)$'s.
\end{prop}
\begin{proof}
Recall that $N$ is a Dehn filling of $M=S'\timforsetil S^1$. Move (\ref{Seifert:1:eqn}) is the result of twisting $M$ along a fibered annulus $A$ connecting the tori $T_i$ and $T_{i+1}$ in $\partial M$: this self-diffeomorphism of $M$ acts on $T_i$ and $T_{i+1}$ like two opposite Dehn twists and extends to an isomorphism of the two fibrations. In (\ref{Seifert:3:eqn}) we twist along an annulus connecting $T_i$ and $\partial N$. The move (\ref{Seifert:2:eqn}) corresponds to drilling a nonsingular fibered torus and refilling it back.

We now prove that these moves suffice to connect two isomorphic Seifert fibrations. 
Suppose that two distinct notations as in (\ref{notation:eqn}) describe isomorphic fibrations. 
We use the moves (\ref{Seifert:1:eqn}), (\ref{Seifert:2:eqn}), and (\ref{Seifert:3:eqn}) to eliminate the parameters $p_i=1$ as much as possible from both notations. If there are no singular fibres, we end up with a single parameter $(1,e)$ if $S$ is closed, and no parameters at all if $\partial S \neq \emptyset$. We conclude by Corollary \ref{unique:e:cor}. 

If the fibration has at least one singular fibre, we can eliminate all $p_i=1$ and the $(p_i,q_i)$ correspond to singular fibres. An isomorphism of Seifert fibrations sends singular fibres to singular fibres and hence induces an isomorphism of their complement $S'\timforsetil S^1$. The parameters $(p_i,q_i)$ are determined by the choice of a section in $S'\timforsetil S^1$. Different sections are related by Dehn twist along annuli and hence the parameters are related by the moves (\ref{Seifert:1:eqn}) and (\ref{Seifert:3:eqn}).
\end{proof}

Proposition \ref{S:moves:prop} classifies all the Seifert fibrations up to isomorphism. A classification of Seifert manifolds up to \emph{diffeomorphism} would also be desirable, but it is much harder to obtain because a three-manifold may admit many non-isomorphic Seifert fibrations. For instance, 
Exercise \ref{two:lens:ex} shows that the lens spaces may fibre in many different ways; a manifold as familiar as $S^3$ fibres over the orbifold $(S^2, p_1, p_2)$ if $p_1$ and $p_2$ are coprime and hence has infinitely many non-isomorphic fibrations. It is a stimulating exercise to try to visualise these Seifert fibrations of $S^3$.

We now start a long journey in Seifert manifolds theory, whose ultimate goal is to classify them completely up to diffeomorphism. We will see at the end that the only Seifert manifolds admitting non-isomorphic fibrations are the ``smallest'' ones, like $S^3$, the lens spaces, and few more that will be classified using some \emph{ad hoc} argument.

\begin{ex}
The number of non-isomorphic Seifert fibrations over a fixed orbifold $S$ is finite $\Longleftrightarrow$ $\partial S \neq \emptyset$.
\end{ex}


\subsection{Euler number}
We now extend the notion of Euler number from ordinary to Seifert fibrations.
We define the \emph{Euler number} of the fibration (\ref{notation:eqn}) to be the rational number\index{Euler number}
$$e(N) = \sum_{i=1}^h \frac{q_i}{p_i}.$$
The Euler number is only defined modulo $\matZ$ when $N$ has boundary. The good definition follows from Proposition \ref{S:moves:prop} (the moves do not affect $e$, except (\ref{Seifert:3:eqn}) that modifies $e$ into $e+1$ and applies only when $N$ has boundary) and is coherent with the circle bundle case. The Euler number depends on the fibration and not only on $N$, but we write $e(N)$ anyway for simplicity. Proposition \ref{S:moves:prop} easily implies the following.

\begin{cor} \label{classification:Seifert:cor}
Two Seifert fibrations
$$\big(S, (p_1,q_1), \ldots, (p_h, q_h)\big), \quad \big(S', (p_1',q_1'), \ldots, (p_{h'}', q_{h'}')\big)$$
with $p_i, p_i'\geqslant 2$ are orientation-preservingly isomorphic if and only if $S=S'$, $h=h'$, $e=e'$, and up to reordering $p_i=p_i'$ and $q_i \equiv q_i'$ (mod $p_i$) for all $i$.
\end{cor}
The numbers $e$ and $e'$ indicate the Euler numbers of the two fibrations, and recall that they are only defined modulo $\matZ$ when $\partial S \neq \emptyset$.

\begin{rem} \label{reverse:rem}
The move
$$\big(S,(p_1,q_1), \ldots, (p_h,q_h)\big) \longmapsto \big(S,(p_1,-q_1), \ldots, (p_h,-q_h)\big) $$
corresponds to a change of orientation for the three-manifold and transforms $e$ into $-e$.
\end{rem}



\subsection{Homology} \label{Seifert:homology:sphere:subsection}
We now characterise the Seifert manifolds that have finite homology groups, and in particular the homology spheres.

\begin{prop} \label{Seifert:homology:prop}
The homology group $H_1(M, \matZ)$ of 
$$M=\big(S,(p_1,q_1), \ldots, (p_h,q_h)\big)$$
is finite $\Longleftrightarrow$ one of the following holds:
\begin{itemize}
\item $S=S^2$ and $e\neq 0$, and we get $|H_1(M,\matZ)| = |e|p_1\cdots p_h$;
\item $S=\matRP^2$, and we get $|H_1(M,\matZ)| = 4p_1\cdots p_h$.
\end{itemize}
\end{prop}
\begin{proof}
If $M$ is not closed then $H_1(M,\matZ)$ is infinite because $H_1(\partial M,\matZ)$ is. If $S\neq S^2, \matRP^2$ then $H_1(S)$ is infinite. It is easy to check that the fibration $M\to S$ induces a surjection $H_1(M)\to H_1(S)$ and hence $H_1(M)$ is also infinite.

Suppose $S=S^2$. The manifold $M$ is a $(p_i,q_i)$-Dehn filling of $S_{0,h}\times S^1$ where $S_{0,h}$ is the sphere with $h$ holes. The homology of $S_{0,h}\times S^1$ is generated by $m_1,\ldots,m_h,l$ with the relation $m_1+\ldots + m_h=0$. The $i$-th Dehn filling adds the relation $p_im_i + q_il_i=0$. The relations form a square $(h+1)$-matrix
$$
\begin{pmatrix}
1 & p_1 & 0 & \cdots & 0 \\
1 & 0 & p_2 & \ddots & \vdots \\
\vdots & \vdots & \ddots & \ddots & 0 \\
\phantom{\Big|} \! 1 & 0 & 0 & \cdots & p_h \\
0 & q_1 & q_2 & \cdots & q_h
\end{pmatrix}
\sim
\begin{pmatrix}
1 & p_1 & 0 & \cdots & 0 \\
1 & 0 & p_2 & \ddots & \vdots \\
\vdots & \vdots & \ddots & \ddots & 0 \\
\phantom{\Big|} \! 1 & 0 & 0 & \cdots & p_h \\
-e & 0 & 0 & \cdots & 0
\end{pmatrix}.
$$
We have used Gauss moves to simplify the last row. The determinant of this matrix is $\pm ep_1\cdots p_h$. The order $|H_1(M,\matZ)|$ is the absolute value of the determinant if it is non-zero, and is infinite if it is zero.

Suppose $S=\matRP^2$ and let $S^{\rm no}_{1,h}$ be $\matRP^2$ with $h$ holes. The homology of $S^{\rm no}_{1,h} \timtil S^1$ is generated by $a,m_1,\ldots, m_h, l$, where $a$ is an orientation-reversing curve in $S^{\rm no}_{1,h}$, with the relations $2a+m_1+\ldots +m_h=0$ and $2l=0$. The relations now form a square $(h+2)$-matrix with determinant
$$
\det \begin{pmatrix}
2 & 0 & 0 & \ldots & 0 \\
1 & 0 & p_1 & \ddots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\phantom{\Big|} \! 1 & 0 & 0 & \cdots & p_h \\
0 & 2& q_1 & \cdots & q_h
\end{pmatrix}
= \pm 2 \det
\begin{pmatrix}
2 & 0 & \cdots & 0 \\
1 & p_1 & \ddots & \vdots \\
\vdots & \vdots & \ddots & \vdots \\
1 & 0 & \cdots & p_h
\end{pmatrix} = \pm 4 p_1\cdots p_h.
$$
The proof is complete.
\end{proof}

We deduce an elegant description of all the Seifert homology spheres.

\begin{cor} \label{sigma:cor}
For every set $p_1, \ldots, p_h$ of pairwise coprime integers $p_i\geqslant 2$ there is a unique homology sphere $\Sigma(p_1,\ldots, p_h)$ Seifert-fibering over $(S^2,p_1,\ldots,p_h)$. Every homology sphere Seifert manifold arises in this way.
\end{cor}
\begin{proof}
By the previous proposition a Seifert manifold 
$$M=\big(S,(p_1,q_1), \ldots, (p_h,q_h)\big)$$
is a homology sphere if and only if $S=S^2$ and $|ep_1\cdots p_h|=1$. We have
$$ep_1\cdots p_h = \sum_{i=1}^h \frac{q_i}{p_i}p_1\cdots p_h = \sum_{i=1}^h q_ip_1\cdots \widehat {p_i}\cdots p_h = \sum_{i=1}^h q_ip_i'$$
where we set $p_i' = p_1\cdots \widehat {p_i}\cdots p_h$. The integers $p_1,\ldots, p_h$ are \emph{pairwise} coprime if and only if $p_1',\ldots, p_h'$ are \emph{globally} coprime (no prime number divides all of them). The equation $\sum_{i=1}q_ip_i' = 1$ is satisfied by some $q_1,\ldots, q_h$ $\Longleftrightarrow$ they are globally coprime. Different solutions $q_i$ are related by moves as in Proposition \ref{S:moves:prop} (exercise) and produce the same Seifert fibration.
\end{proof}

For instance, the homology spheres $\Sigma(p_1)$ and $\Sigma(p_1,p_2)$ are just $S^3$ by Example \ref{bad:example}. The simplest homology sphere with three singular fibres is $\Sigma(2,3,5)$. This manifold is called the \emph{Poincar\'e homology sphere} and we will soon see that its fundamental group has order 120.\index{Poincar\'e homology sphere} All the other Seifert homology spheres have infinite fundamental group: this is related to the fact that $\sum \frac 1{p_i}>1$ for all choices of $(p_1,\ldots, p_h)$ with $h\geqslant 3$ except $(2,3,5)$, as we will soon see. A Seifert homology sphere of type $\Sigma(p_1,p_2,p_3)$ is called a \emph{Brieskorn homology sphere}\index{Brieskorn homology sphere}.


\subsection{Coverings} 
We now start to investigate the coverings of Seifert fibered spaces. Our main goal will be to subdivide the Seifert manifolds into nine classes: this will be done in Section \ref{commensurability:Seifert:subsection}.

Like ordinary fibrations, Seifert fibrations behave well with respect to coverings.
Let $M \to S$ be a Seifert fibration and $\tilde M \to M$ a covering. The foliation into circles of $M$ lifts to a foliation into circles or lines in $\tilde M$, with some quotient space $\tilde S$. 

\begin{prop} \label{Seifert:lifts:prop}
The quotient $\tilde S$ is an orbifold covering of $S$. 
\begin{itemize}
\item If $\tilde M$ foliates in circles then $\tilde M \to \tilde S$ is a Seifert fibration, 
\item If $\tilde M$ foliates in lines then $\tilde M \to \tilde S$ is a line bundle.
\end{itemize}
In the second case $\tilde S$ has no singular points.
\end{prop}
\begin{proof}
This holds on all coverings of a standard fibered solid torus and hence holds everywhere.
\end{proof}

We now concentrate ourselves on the finite-degree case.


\subsection{Finite-degree coverings}
We define a \emph{finite-degree covering} of a Seifert fibration $M\to S$ to be a commutative diagram
$$
\xymatrix{ 
\tilde M\ar[r] \ar[d] & M \ar[d] \\
\tilde S\ar[r] & S
}
$$
where $\tilde M \to \tilde S$ is a Seifert fibration, $\tilde M \to M$ is a finite-degree covering, and $\tilde S \to S$ is an orbifold covering. Proposition \ref{Seifert:lifts:prop} implies the following.

\begin{cor}
Let $M\to S$ be a Seifert fibration. Every finite-degree covering $\tilde M \to M$ induces a finite-degree covering of Seifert fibrations:
$$
\xymatrix{ 
\tilde M\ar[r] \ar@{.>}[d] & M \ar[d] \\
\tilde S\ar@{.>}[r] & S
}
$$
\end{cor}
The dotted arrows indicate the maps that are induced. The degree $d$ of such a covering $\tilde M \to M$ splits into two parts: 
\begin{itemize}
\item the \emph{horizontal} degree $d_{\rm h}$ is the degree of the covering $\tilde S \to S$, 
\item the \emph{vertical} degree $d_{\rm v}$ is the degree with which a regular fibre of $\tilde M$ covers a regular fibre of $M$. 
\end{itemize}
The vertical degree is well-defined since regular fibres in $\tilde M$ form a connected set. The pre-image of a regular fibre in $M$ consists of $d_{\rm h}$ regular fibres in $\tilde M$, each fibering with degree $d_{\rm v}$. Therefore
$$d = d_{\rm h} \cdot d_{\rm v}.$$
A covering $\tilde M \to M$ is \emph{horizontal} or \emph{vertical} if respectively
$d_{\rm v} = 1$ or $d_{\rm h} = 1$.

\begin{prop}[Pull-back] \label{horizontal:prop}
Let $M\to S$ be a Seifert fibration. Every finite-degree orbifold covering $\tilde S \to S$ is induced by a unique horizontal covering of Seifert fibrations:
$$
\xymatrix{ 
\tilde M\ar@{.>}[r] \ar@{.>}[d] & M \ar[d] \\
\tilde S\ar[r] & S
}
$$
\end{prop}
\begin{proof}
Like for ordinary bundles, there is a unique way to define $\tilde M$ by pulling back the Seifert fibration on fibered solid tori.
\end{proof}

Recall that an orbifold is \emph{very good} when it is finitely covered by a surface. Every locally orientable 2-orbifold is very good except the bad orbifolds $S^2(p_1)$ and $S^2(p_1,p_2)$ with $p_1\neq p_2$, see Theorem \ref{O:geometrisation:teo} and Corollary \ref{very:good:surface:cor}.

\begin{cor} \label{good:bundle:cor}
If $S$ is good, every Seifert fibration $M\to S$ is finitely covered by a circle bundle over a surface.
\end{cor}
\begin{proof}
Pull-back the fibration along the surface cover $\tilde S \to S$.
\end{proof}

\begin{prop} \label{hv:prop}
Every finite-degree covering between Seifert fibrations is a composition of one vertical and one horizontal covering. 
\end{prop}
\begin{proof}
Let $p\colon \tilde M\to M$ be a covering of Seifert fibrations, with base spaces $\tilde S \to S$. If we pull-back $M$ to $\tilde S$ we get a horizontal covering $p_{\rm h}\colon M_{\rm h} \to M$. There is a natural vertical $p_{\rm v}\colon \tilde M \to M_{\rm h}$ such that $p = p_{\rm h} \circ p_{\rm v}$.
\end{proof}


\subsection{Circle bundle coverings}
The Euler number of the fibration and the Euler characteristic of the base orbifold behave well with coverings.

\begin{prop} \label{e:prop}
Let $p\colon \tilde M \to M$ be a finite covering of closed Seifert fibrations with base orbifolds $\tilde S$ and $S$, with degrees $(d_{\rm h}, d_{\rm v})$. We have
\begin{align*}
\chi(\tilde S) & = d_{\rm h} \cdot \chi (S), \\
e(\tilde M ) & = \frac{d_{\rm h}}{d_{\rm v}} \cdot e(M).
\end{align*}
\end{prop}
\begin{proof}
The first equality holds for every orbifold covering $\tilde S \to S$.
Concerning the second one, by Proposition \ref{hv:prop} we may suppose $p$ is either vertical or horizontal. Write
$$M = \big(S, (p_1,q_1), \ldots (p_h, q_h)\big)$$
and recall that $M$ is obtained from a circle bundle $N$ by $(p_i,q_i)$-filling the boundary torus $T_i$ for all $i=1,\ldots, h$. Set $\tilde T_i = p^{-1}(T_i)$ and $\tilde N = p^{-1}(N)$.

If $p$ is vertical, we fix a section of $\tilde  N$ and note that it projects to a section of $N$: these sections induce meridians on $\tilde T_i$ and $T_i$. Here $\tilde T_i$ is a single torus and $\tilde T_i \to T_i$ wraps the fibre with degree $d=d_{\rm v}$. Since the covering extends to the filled solid tori, we have $d|q_i$ and $\tilde T_i$ is filled with parameters $(p_i,q_i/d)$. Therefore $e(\tilde M) = e(M)/d$.

If $p$ is horizontal, we fix a section of $N$, and its counterimage is a section of $\tilde N$: these sections induce meridians on $T_i$ and $\tilde T_i$.
Now $\tilde T_i$ consists of some tori $\tilde T_i = \tilde T_{i,1} \sqcup \ldots \sqcup \tilde T_{i,k_i}$ and $\tilde T_{i,j} \to T_i$ wraps the meridians with some degree $d_{i,j}$. The total sum of these local degrees is $d_{i,1}+\ldots +d_{i,k_i}=d = d_{\rm h}$. Similarly as above we have $d_{i,j}|p_i$ and the filling solid torus at $\tilde T_{i,j}$ has parameters $(p_i/d_{i,j},q_i)$. Therefore 
$$e(\tilde M) = \sum_{i=1}^h \sum_{j=1}^{k_i} \frac{d_{i,j}q_i}{p_i} = \sum_{i=1}^h d\cdot \frac{q_i}{p_i} = d \cdot e(M).$$
This concludes the proof.
\end{proof}

An important consequence is that the signs of $\chi(S)$ and $e(M)$ are invariant under finite coverings. 


\subsection{Commensurability classes} \label{commensurability:Seifert:subsection}
We now would like to subdivide the Seifert manifolds into few classes, and to this purpose we introduce a general equivalence relation between manifolds.

\begin{defn}
Two manifolds $M$ and  $N$ are \emph{commensurable} if there is a manifold that covers both $M$ and $N$ with finite degrees.\index{commensurability of manifolds}
\end{defn}

\begin{prop}
Commensurability is an equivalence relation.
\end{prop}
\begin{proof}
If $M$ is commensurable with $N_1$ and $N_2$, it has finite-sheeted coverings $M_1, M_2$ that cover $N_1$ and $N_2$ corresponding to finite-index subgroups $\Gamma_1, \Gamma_2 < \pi_1(M)$. The subgroup $\Gamma = \Gamma_1\cap \Gamma_2$ has also finite index and determines a manifold that covers both $N_1$ and $N_2$.
\end{proof}

\begin{ex}
There are three commensurable classes of closed surfaces, determined by their Euler characteristic being positive, null, or negative.
\end{ex}

We now classify the commensurability classes of Seifert manifolds. The \emph{3-torus} is of course $T\times S^1 = S^1\times S^1\times S^1$.\index{3-torus}

\begin{prop} \label{cover:Seifert:prop}
A closed Seifert fibration $M\to S$ has:
\begin{itemize}
\item $\chi(S)>0$ and $e=0$ $\Longleftrightarrow M$ is covered by $S^2\times S^1$,
\item $\chi(S)>0$ and $e\neq 0$ $\Longleftrightarrow M$ is covered by $S^3$,
\item $\chi(S)=0$ and $e=0$ $\Longleftrightarrow M$ is covered by the 3-torus,
\item $\chi(S)=0$ and $e\neq 0$ $\Longleftrightarrow M$ is covered by a twisted bundle over $T$,
\item $\chi(S)<0$ and $e=0$ $\Longleftrightarrow M$ is covered by $S_g \times S^1$ for some $g>1$,
\item $\chi(S)<0$ and $e\neq 0$ $\Longleftrightarrow M$ is covered by a twisted bundle over $S_g$ for some $g>1$.
\end{itemize}
\end{prop}
\begin{proof}
If $S$ is a bad orbifold, then $S=S^2(p)$ or $S^2(p_1,p_2)$ with $p_1\neq p_2$ and hence we get $e\neq 0$ and $\chi(S)>0$. The manifold $M$ is a lens space by Example \ref{bad:example} and is hence covered by $S^3$.

If $S$ is good, the fibration $M\to S$ is covered by a circle bundle $\tilde M\to \tilde S$ over an orientable closed surface $\tilde S$ by Corollary \ref{good:bundle:cor}. By Proposition \ref{e:prop} the numbers $\chi(\tilde S)$ and $e(\tilde M)$ have the same signs of $\chi(S)$ and $e(M)$. Therefore $\tilde S = S^2, T$, or $S_g$ with $g> 1$, depending on whether $\chi(S)$ is positive, null, or negative. 
Exercise \ref{circle:bundle:ex} says that the circle bundle $\tilde M \to \tilde S$ is trivial $\Longleftrightarrow e(\tilde M) =0 \Longleftrightarrow e(M) =0$. Note that a non-trivial bundle over $S^2$ is a lens space $L(e,1)$ with $e\neq 0$ and is hence covered by $S^3$.

We have proved that $M$ is covered (according to the signs of $\chi$ and $e$) by a manifold belonging to one of the six types: $S^3$, $S^2\times S^1$, the 3-torus, a twisted bundle over $T$, $S_g\times S^1$, and a twisted bundle over $S_g$. It remains to prove that $M$ cannot be covered by two manifolds $M_1, M_2$ belonging to two different types: this holds because manifolds of distinct types are not commensurable. To prove that, note that the finite cover of a manifold of one of the six types is a manifold of the same type, and Corollary \ref{distinct:bundle:cor} implies that a manifold cannot belong to two different types. If two manifolds of distinct types were commensurable they would be covered by a manifold belonging to both types, yielding a contradiction.
\end{proof}


\begin{table}
\begin{center}
\begin{tabular}{c||ccc}
        & \phantom{\Big|} $\chi>0$ & $\chi = 0$ & $\chi<0$ \\
 \hline \hline
 $e=0$ & \phantom{\Big|} $S^2\times S^1$ & $S^1\times S^1\times S^1$ & $S_2 \times S^1$ \\
 $e\neq 0$ & \phantom{\big|} $S^3$ & $\big(T,(1,1)\big)$ & $\big(S_2,(1,1)\big)$ \\
 $\partial M\neq \emptyset$ & \phantom{\Big|} $D\times S^1$ & $T \times [0,1]$ & $P \times S^1$
\end{tabular}
\vspace{.2 cm}
\nota{There are 9 commensurability classes of Seifert manifolds: 6 closed and 3 with boundary. Every Seifert manifold $M$ is commensurable with one (and only one) of these 9 manifolds. The commensurability class of $M$ is easily detected by looking at its invariants $\chi$ and $e$ (the latter only in the closed case). The surfaces $T,S_2,D,P$ are the torus, the genus-2 surface, the disc, and the pair-of-pants. Note that $S^3 = \big(S^2,(1,1)\big)$.}
\label{commensurability:table}
\end{center}
\end{table}

We can now easily classify all closed Seifert manifolds up to commensurability. To conclude we just need to solve the following exercise.

\begin{ex} \label{e:construct:ex}
Pick $S=S_g$ and $e>0$. Construct:
\begin{itemize}
\item a degree-$e$ vertical covering $\big(S,(1,1)\big)\to \big(S,(1,e)\big)$,
\item a degree-$e$ horizontal covering $\big(\tilde S,(1,e)\big) \to \big(S,(1,1)\big)$ if $g\geqslant 1$.
\end{itemize}
\end{ex}
\begin{proof}[Hint] If $g\geqslant 1$ then $S$ has covers of any degree $e$. To construct them, pick surjective homomorphisms $\pi_1(S)\to H_1(S) \to \matZ/_{e\matZ}$.
\end{proof}

\begin{cor}
There are six commensurability classes of closed Seifert manifolds, depending on $\chi$ and $e$ as shown in Table \ref{commensurability:table}.
\end{cor}
\begin{proof}
By the previous exercise the non-trivial (or trivial) bundles over closed surfaces with $\chi < 0$ (or $\chi =0$, $\chi >0$) are all commensurable.
\end{proof}

\begin{cor}
A closed Seifert fibration $M\to S$ has $e=0$ $\Longleftrightarrow$ it is finitely covered by a trivial circle bundle.
\end{cor}

We recall that a Seifert manifold $M$ may have non-isomorphic Seifert fibrations $M\to S$ and $M\to S'$, and the invariants $\chi, \chi'$ and $e, e'$ of the two fibrations are not necessarily equal; however $\chi$ is positive, null, or negative if and only if $\chi'$ is, and $e$ vanishes if and only if $e'$ does (in the closed case). This holds because the commensurability class of $M$ does not depend on its fibration. For instance, Exercise \ref{two:lens:ex} shows that a lens space $M=L(p,q)$ with $p>0$ has many fibrations, but each with $\chi>0$ and $e\neq 0$.

We now consider the boundary case, which is simpler because circle bundles over orientable surfaces with boundary are always trivial. Let $A$ denote the annulus and $S_{g,b}$ be the surface of genus $g$ with $b$ open discs removed.

\begin{prop}
A Seifert fibration $M\to S$ with boundary has
\begin{itemize}
\item $\chi(S)>0 \Longleftrightarrow M = D\times S^1$,
\item $\chi(S)=0 \Longleftrightarrow M$ is covered by $A \times S^1 = T\times [0,1]$,
\item $\chi(S)<0 \Longleftrightarrow M$ is covered by $S_{g,b} \times S^1$ for some $g+b>2$.
\end{itemize}
\end{prop}
\begin{proof}
Every Seifert manifold with boundary is covered by a circle bundle over an orientable surface, and such a bundle is trivial here. If $\chi>0$ the base surface is a disc with at most one cone point and hence $M$ is a standard fibered solid torus. 
\end{proof}

\begin{cor} There are three commensurability classes of Seifert manifolds with boundary, depending on $\chi$ as shown in Table \ref{commensurability:table}.
\end{cor}
\begin{proof}
The surfaces $S_{g,b}$ with $g+b>2$ are commensurable (exercise).
\end{proof}

We now characterise some commensurability classes by looking at the fundamental groups.

\begin{table}
\begin{center}
\begin{tabular}{c||ccc}
        & \phantom{\Big|} $\chi>0$ & $\chi = 0$ & $\chi<0$ \\
 \hline \hline
 $e=0$ & \phantom{\Big|} $\matZ$ & $\matZ^3$ & \\
 $e\neq 0$ & \phantom{\big|} $\{e\}$ & &  \\
 $\partial M\neq \emptyset$ & \phantom{\Big|} $\matZ$ & $\matZ^2$ &
\end{tabular}
\vspace{.2 cm}
\nota{There are five Seifert manifolds $M$ with $\pi_1(M) = \matZ^h$ and they belong to distinct commensurability classes. The fundamental group $\pi_1(N)$ of every other manifold $N$ in these five classes is virtually abelian: it contains $\matZ^h$ as a finite-index subgroup.}
\label{abelian:group:table}
\end{center}
\end{table}


\subsection{Virtually abelian fundamental groups} \label{virtually:abelian:subsection}
A group $G$ is \emph{virtually abelian of rank $h$} if it contains $\matZ^h$ as a finite-index subgroup. 

This is a finite-index-independent property: if $G'<G$ has finite index, the group $G'$ is virtually abelian of rank $h$ if and only if $G$ is. Therefore a manifold $M$ has a virtually abelian fundamental group of rank $h$ $\Longleftrightarrow$ every manifold $N$ commensurable with $M$ also has $\Longleftrightarrow$ there is a manifold $N$ in the commensurability class with $\pi_1(N)=\matZ^h$.

\begin{prop} \label{virtually:abelian:prop}
There are five commensurability classes of Seifert manifolds with virtually abelian fundamental groups, shown in Table \ref{abelian:group:table}.
\end{prop}
\begin{proof}
These five classes contain $S^2\times S^1$, $S^1\times S^1\times S^1$, $S^3$, $D\times S^1$, and $A\times S^1$. The remaining four classes do not contain manifolds with abelian fundamental group: every manifold in these classes is covered by some $S \times S^1$ with $\chi(S)<0$ or $\big(S_g, (1,e)\big)$ with $g\geqslant 1$ and $e\geqslant 1$ (use Exercise \ref{e:construct:ex}). The fundamental group of such manifolds is not $\matZ^h$: the former because $\pi_1(S)$ is not abelian, and the latter because its abelianization contains torsion, see Exercise \ref{bundle:ex}.
\end{proof}

It could be reasonable to expect these five commensurability classes to contain manifolds of some simpler topological nature, which are easier to study and classify. We will see however in Section \ref{Seifert:finite:subsection} that the Seifert manifolds covered by $S^3$ are quite interesting and their topological classification is certainly not immediate: we already experienced that for lens spaces in Theorem \ref{Lpq:teo}, whose classification is quite involved. The other four classes are indeed of a simpler nature: we now prove that each contains finitely many manifolds, and we classify them completely.


\subsection{Finite commensurability classes} \label{finite:classes:prop}
We now completely identify the commensurability classes of Seifert manifolds that contain only finitely many manifolds.

We start by considering manifolds $M$ with boundary. We have already seen that the class $\chi>0$ contains only the solid torus. The class $\chi=0$ also contains few manifolds:

\begin{prop} \label{diffeo:fiberings:prop}
Every Seifert fibration with boundary and $\chi = 0$ is isomorphic to one of the following:
$$ A \times S^1, \qquad S \timtil S^1, \qquad \big(D, (2,1), (2,-1) \big).$$
The Seifert manifold is correspondingly diffeomorphic to the interval bundles
$ T \times I$, $K \timtil I$, and $K \timtil I$ again. Here $A$, $S$, and $K$ are the annulus, the M\"obius strip, and the Klein bottle.
\end{prop}
\begin{proof}
The orbifolds with boundary and $\chi=0$ are $A$, $S$, and $(D,2,2)$.
Every Seifert fibration over $(D,2,2)$ is isomorphic to $\big(D,(2,2n+1),(2,2m+1)\big)$ and does not depend on $n,m\in \matZ$ by Proposition \ref{S:moves:prop}. Hence there is only one Seifert fibration over the orbifold $(D,2,2)$, which we write as $\big(D,(2,1),(2,-1)\big)$ only for aesthetic reasons (to get $e=0$).

\begin{figure}
\begin{center}
\includegraphics[width = 12 cm] {\iftoggle{BW}{two_fibrations-BW}{two_fibrations}}
\nota{Draw the orientable line bundle over the Klein bottle as $S^1\times [-1,1]\times [-1,1]/_\psi$ where $\psi$ identifies the lower and upper (\iftoggle{BW}{light grey}{yellow}) annuli $S^1\times [-1,1]\times \{\pm 1\}$ by gluing $(e^{i\theta},t)$ to $(e^{-i\theta},-t)$. The Klein bottle is drawn in \iftoggle{BW}{grey}{green} (left). 
This manifold has two fibrations: a horizontal one with fibres $S^1\times x \times y$ and base surface the \iftoggle{BW}{grey}{green} M\"obius strip (centre), and a vertical one with fibres $x\times y \times [-1,1]$ and base surface the \iftoggle{BW}{grey}{green} disc with two cone points of order two (the \iftoggle{BW}{grey}{green} annulus becomes a disc after identifying the points $(e^{i\theta}, 0)$ and $(e^{-i\theta}, 0)$). The two singular fibres of order two lie above $(\pm 1,0)$ and are drawn in \iftoggle{BW}{grey}{red} (right).}
\label{two_fibrations:fig}
\end{center}
\end{figure}

We get three manifolds and we now prove that they are all diffeomorphic to some interval bundle. The diffeomorphism $A\times S^1 \isom T\times I$ is obvious. Draw $K\timtil I$ as $S^1\times [-1,1]\times [-1,1]/_\psi$ as in Figure \ref{two_fibrations:fig}. The manifold has two fibrations: a horizontal one by circles $S^1\times x\times y$, and a vertical one by segments $x\times y \times [-1,1]$. The horizontal one gives $S\timtil S^1$ and the vertical one closes to a Seifert fibration over the disc with two singular fibres of order two, and hence is $(D,(2,1),(2,-1))$.
\end{proof}

\begin{cor}
Every Seifert manifold with boundary and $\chi\geqslant 0$ is diffeomorphic to $D\times S^1$, $T\times I$, or $K\timtil I$.
\end{cor}

We now turn to closed Seifert manifolds. We have seen that $K\timtil I$ fibres in two non-isomorphic ways, and this has some consequences.

\begin{cor} \label{Seifert:diffeo:cor}
The following diffeomorphisms hold:
\begin{align*}
\big(S^2,(2,1),(2,-1),(p,q)\big) & \isom \big(\matRP^2, (q,p)\big), \\
\big(S^2,(2,1),(2,1),(2,-1),(2,-1)\big) & \isom K\timtil S^1.
\end{align*}
\end{cor}
\begin{proof}
Both equalities follow from $\big(D, (2,1), (2,-1)\big) \isom S\timtil S^1$. In the first we look at Figure \ref{two_fibrations:fig} to check that a $(p,q)$ curve in $\big(D,(2,1),(2,-1)\big)$ becomes a $(q,p)$ curve in $S\timtil S^1$.
The second equality is obtained by doubling the line bundle $K\timtil I$.
\end{proof}

We want to classify the closed Seifert manifolds with $\chi\geqslant 0$ and $e=0$. We start with the case $\chi >0$.

\begin{prop} \label{rp:prop}
Every closed Seifert fibration with $\chi>0$ and $e=0$ is isomorphic to one of the following: 
$$S^2 \times S^1, \qquad \matRP^2 \timtil S^1, \qquad \big(S^2, (p,q), (p,-q)\big).$$
The manifolds of the last type are all diffeomorphic to $S^2\times S^1$.
\end{prop}
\begin{proof}
If the base surface $S$ is a sphere with $\leqslant 2$ singular fibres, we use Exercise \ref{two:lens:ex}. Otherwise $S$ is one of the following orbifolds (see Table \ref{orbifold:elliptic:table}):
$$(S^2,2,2,p), \quad (S^2,2,3,3), \quad (S^2,2,3,4), \quad (S^2,2,3,5), \quad \matRP^2, \quad (\matRP^2, p) $$
with $p\geqslant 2$. In all cases except $\matRP^2$, we get $e\neq 0$ for any choice of Dehn filling parameters: for instance 
$$e\big(S^2,(2,q_1),(2,q_2),(p,q_3)\big) = \frac{q_1+q_2}2 + \frac{q_3}p \neq 0.$$ 
The other cases are analogous.
\end{proof}

The manifold $\matRP^2 \timtil S^1$ is not diffeomorphic to $S^2\times S^1$, because they have non-isomorphic fundamental groups. Moreover, $\matRP^2 \timtil S^1$ is not prime:

\begin{ex} The two manifolds $\matRP^2\timtil S^1$ and $\matRP^3\#\matRP^3$ are diffeomorphic.
\end{ex}

\begin{table}
\begin{center}
\begin{tabular}{c||c}
\phantom{\Big|} $M$ & $H_1(M,\matZ)$ \\
\hline \hline
\phantom{\Big|} $ T \times S^1$ & $\matZ^3$ \\ 
\phantom{\big|} $ K \timtil S^1$ & $\matZ \times \matZ/_{2\matZ} \times \matZ/_{2\matZ}$ \\
\phantom{\Big|} $ \big(S^2, (2,1), (2,1), (2,-1), (2,-1) \big) $ & $\matZ \times \matZ/_{2\matZ} \times \matZ/_{2\matZ}$ \\
\phantom{\big|} $ \big(S^2, (3,1), (3,1), (3,-2) \big) $ & $\matZ \times \matZ/_{3\matZ} $ \\
\phantom{\Big|} $ \big(S^2, (2,1), (4,-1), (4,-1) \big) $ & $\matZ \times \matZ/_{2\matZ} $ \\
\phantom{\big|} $ \big(S^2, (2,1), (3,1), (6,-5) \big) $ & $\matZ$ \\
\phantom{\Big|} $ \big(\matRP^2, (2,1), (2,-1)\big) $ & $\matZ/_{4\matZ} \times \matZ/_{4\matZ}$
\end{tabular}
\vspace{.2 cm}
\nota{The seven closed Seifert fibrations with $\chi=0$ and $e=0$. Two of these manifolds are actually diffeomorphic, so we get six closed Seifert manifolds up to diffeomorphism, distinguished by their homology.}
\label{seven:table}
\end{center}
\end{table}

We will soon see that $\matRP^2 \timtil S^1$ is the unique non-prime Seifert manifold. We now turn to the $\chi=0$ case.

\begin{prop} \label{chi:zero:prop}
Every closed Seifert fibration with $\chi = 0$ and $e=0$ is isomorphic to one of the seven listed in Table \ref{seven:table}. These seven manifolds are all pairwise non-diffeomorphic, except
$$\big(S^2,(2,1),(2,1),(2,-1),(2,-1)\big) \isom K\timtil S^1.$$
\end{prop}
\begin{proof}
The closed orbifolds with $\chi =0$ are 
$$T,\ K,\ (\matRP^2, 2,2),\ (S^2, 2,2,2,2),\ (S^2,2,3,6),\ (S^2,3,3,3),\ (S^2,2,4,4).$$ 
It is easy to show that by imposing $e=0$ we get the fibrations listed.
The homology calculation is an easy exercise and luckily distinguishes all the manifolds except (of course) the two diffeomorphic ones (see Corollary \ref{Seifert:diffeo:cor}).
\end{proof}

\begin{table}
\begin{center}
\begin{tabular}{c||ccc}
       & \phantom{\Big|} $\chi>0$ & $\chi = 0$ & $\chi<0$ \\
 \hline \hline
 $e=0$ & \phantom{\Big|} $2$ & $6$ & $\infty$ \\
 $e\neq 0$ & \phantom{\big|} $\infty$ & $\infty$ & $\infty$ \\
 $\partial M \neq \emptyset$  & \phantom{\Big|} $1$ & $2$ & $\infty$
\end{tabular}
\vspace{.2 cm}
\nota{The number of Seifert manifolds in each commensurability class.}
\label{finite:table}
\end{center}
\end{table}

Summing up, there are four commensurability classes containing finitely many manifolds, and their number is shown in Table \ref{finite:table}.


\subsection{Universal cover}
We now determine the universal cover of all the closed Seifert manifolds. Nothing strange happens: we either get $S^3$, $S^2\times \matR$, or $\matR^3$.

\begin{table}
\begin{center}
\begin{tabular}{c||ccc}
       & \phantom{\Big|} $\chi>0$ & $\chi = 0$ & $\chi<0$ \\
 \hline \hline
 $e=0$ & \phantom{\Big|} $S^2 \times \matR$ & $\matR^3$ & $\matR^3$ \\
 $e\neq 0$ & \phantom{\big|} $S^3$ & $\matR^3$ & $\matR^3$
\end{tabular}
\vspace{.2 cm}
\nota{The universal cover of a closed Seifert manifold depends on its invariants $e$ and $\chi$.}
\label{universal:table}
\end{center}
\end{table}

\begin{prop} \label{universal:Seifert:prop}
The universal cover of a closed Seifert manifold is shown in Table \ref{universal:table}.
\end{prop}
\begin{proof}
The universal cover of a circle bundle over a surface $S$ with $\chi(S)\leqslant 0$
is a line bundle over the universal cover $\matR^2$ of $S$. The line bundle is trivial since $\matR^2$ is contractible and we get $\matR^2\times \matR = \matR^3$.
\end{proof}

\begin{cor}
Every Seifert manifold $M$ is either irreducible or covered by $S^2\times \matR$. In the latter case $M$ is diffeomorphic to $S^2\times S^1$ or $\matRP^2\timtil S^1$.
\end{cor}
\begin{proof}
If the universal cover is $S^3$ or $\matR^3$, it is irreducible and hence also $M$ is. When $M$ has boundary, we apply the proof of Proposition \ref{universal:Seifert:prop} to the interior of $M$ and find that its universal cover is $\matR^3$.
\end{proof}

Therefore every Seifert manifold is prime except $\matRP^2 \timtil S^1 = \matRP^3 \# \matRP^3$.


\subsection{Fibre-Parallel Dehn filling}
We have investigated various topological properties of Seifert manifolds, and we are now curious: what happens if we perform a forbidden fibre-parallel Dehn filling? We start by looking at the basic block $P\times S^1$, where $P$ is a pair-of-pants.

\begin{prop}
A fibre-parallel Dehn filling on $P\times S^1$ produces the connected sum of two solid tori; the fibres of $P\times S^1$ become the meridians of the solid tori.
\end{prop}
\begin{proof}
Let $\gamma \subset \partial P$ be the component whose torus $\gamma \times S^1$ is filled. Pick an essential arc $\alpha$ in $P$ with both endpoints in $\gamma$: the fibered annulus $A = \alpha \times S^1$ closes up to a two-sphere $S$ in the Dehn filling. 

The sphere $S$ separates the filled manifold into two portions, each diffeomorphic to $T\times [0,1]$ with a two-handle attached along a non-trivial curve: this is a holed solid torus. Every fibre now bounds a disc there.
\end{proof}

We now turn to arbitrary bundles.

\begin{ex}
Let $S$ be a compact surface with $b\geqslant 1$ boundary components.
The fibre-parallel Dehn filling of $S \timtil S^1$ is diffeomorphic to the connected sum of $b-1$ solid tori and $-\chi(S)+2-b$ copies of $S^2\times S^1$.
\end{ex}

We now deduce a more general fact: a fibre-parallel Dehn filling of a Seifert manifold is a connected sum of lens spaces and solid tori.

\begin{cor} \label{fiber:parallel:cor}
The fiber-parallel Dehn filling of
$$\big(S, (p_1,q_1), \ldots, (p_h, q_h)\big)$$
is diffeomorphic to the connected sum
$$L(p_1,q_1) \# \ldots \# L(p_h,q_h) \#_k (S^2 \times S^1) \#_{b-1} (D^2 \times S^1)$$
where $S$ has $b$ boundary components and $k=-\chi(S) +2-b$.
\end{cor}
If $S$ is orientable then $k$ is twice the genus of $S$. 

\begin{cor} \label{DF:Seifert:cor}
Every Dehn filling of a Seifert manifold is a connected sum of Seifert manifolds.
\end{cor}

If we have a Seifert manifold $M$ with many boundary components and we Dehn fill some of them, we are guaranteed to produce a new Seifert manifold, unless one of the Dehn filling kills a fiber-parallel slope: in that case the manifold ``degenerates'' to a connected sum of lens spaces and solid tori. This is an interesting phenomenon to keep in mind, because it will reproduce in Chapter \ref{Hyperbolic:Dehn:chapter} in the hyperbolic world: we will show that by Dehn filling a cusped hyperbolic three-manifold we always get a new hyperbolic manifold if we avoid a finite number of ``exceptional slopes'' on every boundary torus; if some of the exceptional slopes is employed, the manifold is possibly not hyperbolic, and it typically ``degenerates'' and breaks into simpler pieces.
