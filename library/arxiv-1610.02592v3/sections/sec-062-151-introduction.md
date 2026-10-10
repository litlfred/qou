---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-062-151-introduction
section_title: "Introduction"
section_number: 15.1
pages: 451-458
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.829
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
It sometimes happens in three-dimensional topology, that a topological or geometric property of a manifold is preserved under Dehn fillings, with only few exceptions.
For instance, the Dehn filling of a Seifert manifold is again a Seifert manifold, with only one exception (a fibre-parallel Dehn filling gives a connected sum of Seifert manifolds, see Corollary~\ref{DF:Seifert:cor}).

The most striking appearance of this phenomenon is the Hyperbolic Dehn filling Theorem, proved by Thurston at the end of the 1970s. This theorem says roughly that ``most'' Dehn fillings of a cusped hyperbolic manifold are still hyperbolic.

\subsection{Generalised Dehn filling parameters} \label{generalised:subsection}
In all this chapter, we consider a compact oriented three-manifold $N$ with $\partial N = T_1 \sqcup \ldots \sqcup T_c$ consisting of tori, and we fix generators $m_i,l_i$ for every $\pi_1(T_i)$. 

Let a \emph{generalised Dehn filling parameter} $s=(s_1,\ldots, s_c)$ be a sequence where each $s_i$ is either the symbol $\infty$ or a rationally related pair of real numbers $(p,q) = (kp',kq') = k(p',q')$ where $k>0$ is real and $(p',q')$ are coprime integers. We think at $s_i$ as lying in the two-sphere $S^2 = \matR^2 \cup \{\infty\}$.

A generalised Dehn filling parameter $s$ determines a Dehn filling $N^{\rm fill}$ of $N$ as follows:
for every $i$, if $s_i=k(p',q')$ we fill $T_i$ by killing the slope $p'm_i + q'l_i$, while if $s_i=\infty$ we do nothing. The result is a new compact manifold, that may be closed (if there are no $\infty$ in $s$) or be bounded by some tori. We also mark the cores of the filled solid tori with the label $\alpha_i = \frac{2\pi} k>0$. 

\subsection{The Hyperbolic Dehn filling Theorem}
This chapter is mainly devoted to the proof of the following theorem. 

\begin{teo} \label{DF:teo} \label{hyperbolic:Dehn:filling:teo}
Let $M = \interior N$ be a complete orientable finite-volume cusped hyperbolic three-manifold. There is a neighbourhood $U$ of $(\infty,\ldots,\infty)$ in $S^2\times \ldots \times S^2$ such that for every generalised Dehn filling parameter $s \in U$ the interior $M^{\rm fill}$ of the manifold $N^{\rm fill}$ obtained by Dehn filling $N$ along $s$ admits a finite-volume complete hyperbolic structure with cone angles. 

The cores of the filling solid tori are closed geodesics with cone angles $\alpha_i$. The singular locus of $M^{\rm fill}$ consists of the core geodesics with $\alpha_i \neq 2\pi$.
\end{teo}

If $s\in U$ is an ordinary (not extended) Dehn filling parameter (see Section \ref{DF:parameters:subsection}), that is if $s_i$ is either $\infty$ or a coprime pair $(p,q)$ for all $i$, then $\alpha_i = 2\pi$ and $N^{\rm fill}$ is a hyperbolic manifold without cone angles: this is of course the case of most interest. 

\begin{cor}
Let $M = \interior N$ be a complete orientable finite-volume hyperbolic three-manifold. For every $i=1,\ldots, c$ there is a finite set $S_i$ of slopes in $T_i$ such that for every Dehn filling parameter $s$ with $s_i \not \in S_i$ for all $i$, the filled manifold $M^{\rm fill} = \interior{N^{\rm fill}}$ is hyperbolic.
\end{cor}

When $M$ has one cusp, the corollary may be stated simply as follows.

\begin{cor}
If $M$ is a complete orientable finite-volume hyperbolic three-manifold with one cusp, all but finitely many Dehn fillings $M^{\rm fill}$ are hyperbolic.
\end{cor}

To appreciate the power of these theorems, consider for instance a hyperbolic link $L\subset S^3$ (recall that $L\subset S^3$ is hyperbolic if $S^3\setminus L$ admits a finite-volume complete hyperbolic metric). By the hyperbolic Dehn filling theorem, there is a finite subset $S\subset \matQ$ such that every surgery on $L$ with coefficients in $\matQ\setminus S$ produces a closed hyperbolic manifold.

\subsection{Examples} We describe a couple of clarifying examples. We know that the figure eight knot $K\subset S^3$ is hyperbolic: by the Dehn filling Theorem, there is an open neighbourhood $U \subset S^2$ of $\infty$ such that every Dehn surgery on $K$ with parameter $s\in U$ produces a hyperbolic cone manifold. 

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{figure8_U-BW}{figure8_U}} 
\nota{Hyperbolic Dehn fillings on the figure-eight knot complement.}
\label{figure8_U:fig}
\end{center}
\end{figure}

We will prove in the next section that the subset $U$ shown in Figure \ref{figure8_U:fig} fulfils this requirement. The only coprime pairs $(p,q)$ that are not contained in $U$ are those with $\frac pq$ equal to one of the following
\begin{equation} \label{K:list:eqn}
-4,-3,-2,-1,0,1,2,3,4,\infty.
\end{equation}
Every other surgery on $K$ yields a closed hyperbolic three-manifold. For instance, the manifold Vol2 from Table \ref{closed:census:table} can be obtained with $\frac pq = \pm 5$ (there is a symmetry of $K$ sending $\frac pq$ to $-\frac pq$).

On the other hand, a $\frac pq$ surgery from the list (\ref{K:list:eqn}) does not produce a hyperbolic manifold: see Table \ref{non:hyp:table}, taken from Martelli -- Petronio \cite{MP}.

\begin{table}
\begin{center}
\begin{tabular}{c||c}
$\frac pq$ & manifold \phantom{\Big|}\!\! \\
\hline
\hline
$0$ & $T_{\matr 31{-1}0}$ \phantom{\Big|}\!\!  \\
$\pm 1$ & $\big(S^2, (2,1), (3,1), (7,-6)\big)$  \phantom{\Big|}\!\! \\
$\pm 2$ & $\big(S^2, (2,1), (4,1), (5,-4)\big)$  \phantom{\Big|}\!\! \\
$\pm 3$ & $\big(S^2, (3,1), (3,1), (4,-3)\big)$  \phantom{\Big|}\!\! \\
$\pm 4$ & $\big(D,(2,1), (2,1)\big) \bigcup_{\matr 0110} \big(D, (2,1), (3,1)\big) $\phantom{\Big|}\!\!
\end{tabular}
\vspace{.2 cm}
\nota{The non-hyperbolic Dehn surgeries of the figure-eight knot. We get a torus bundle with Anosov monodromy and hence of $\Sol$ geometry, three Seifert manifolds of $\widetilde {\SL_2}$ geometry, and a graph manifold that splits into two Seifert manifolds via a map that interchanges the fibres and the boundary sections of the two portions (the map is here denoted by a matrix in the section-fibre basis).}
\label{non:hyp:table}
\end{center}
\end{table}

More generally, a parameter $k(p,q) \in U$ produces a hyperbolic closed manifold with a core geodesic of cone angle $\frac{2\pi}k$, which may be interpreted as an orbifold when $k\in \matN$. In particular, if $(p,q) = (1,0)$ the closed manifold is just $S^3$, because an $\infty$-surgery on a knot in $S^3$ gives $S^3$ back. Therefore by looking at Figure \ref{figure8_U:fig} we discover that for every $k\geqslant 5$ there is a hyperbolic structure on $S^3$ with cone angle $\frac{2\pi}k$ on the figure-eight knot $K$. 

We now consider a link with two components.
The \emph{Whitehead link} $L$ shown in Figure \ref{sequence:fig} is hyperbolic: it is hard to determine an explicit open set $U\subset S^2\times S^2$ in this case, but a careful computer-aided analysis carried with SnapPy \cite{Sna} shows the following, see \cite{MP}.

\begin{teo}
A surgery on the Whitehead link with coefficients $(\frac pq, \frac rs)$ produces a closed hyperbolic manifold, unless one of the following holds:
\begin{itemize}
\item $\frac pq$ or $\frac rs$ belongs to the set $\{0, 1, 2, 3, 4, \infty\}$,
\item up to permutation the pair $\big( \frac pq, \frac rs \big)$ belongs to the set
$$\left\{ (-4,-1), (-3,-1), (-2,-2), (-2,-1), \left(\tfrac 32, 5\right), \left(\tfrac 43, 5\right) \left(\tfrac 52, \tfrac 72\right) \right\}.$$
\end{itemize}
\end{teo}
The proposition is symmetric in the two coefficients because the link itself has a symmetry that interchanges the two components. All the Dehn filling parameters listed in the theorem indeed produce non-hyperbolic manifolds. For instance, if $\frac pq\in \{1,2,3\}$ we get a Seifert manifold fibering over the disc with two singular fibres, see \cite{MP}.

We first prove Theorem \ref{hyperbolic:Dehn:filling:teo} for the figure-eight knot, where the combinatorics is so simple that everything can be verified by hand.
We will then prove the theorem in general in Section \ref{solution:space:section} using more sophisticated tools.

\subsection{The figure-eight knot example} \label{figure:8:example:subsection}

\begin{figure}
\begin{center}
\includegraphics[width = 11 cm] {\iftoggle{BW}{triangulation_figure8_2-BW}{triangulation_figure8_2}} 
\nota{We truncate the tetrahedra and flatten their boundary. We assign a modulus $z$ and $w$ to them. The edge numbered $i=1,2,3$ has modulus $z_i$ (on the left tetrahedron) or $w_i$ (on the right tetrahedron).}
\label{triangulation_figure8_2:fig}
\end{center}
\end{figure}

\begin{figure}
\begin{center}
\includegraphics[width = 9 cm] {\iftoggle{BW}{triangulation_figure8_3-BW}{triangulation_figure8_3}} 
\nota{The triangulated boundary is a torus obtained by identifying the opposite edges of this parallelogram. The triangulation $\calT$ has two edges, that we colour in \iftoggle{BW}{grey}{red} and white. Their endpoints are shown here.}
\label{triangulation_figure8_3:fig}
\end{center}
\end{figure}

We now discuss in detail the standard example: the figure-eight knot complement, one of the very few cases where the consistency and completeness equations can be solved by hand. This part will not be needed in the proof of Theorem \ref{hyperbolic:Dehn:filling:teo}, so the reader may wish to skip it and go directly to Section \ref{sketch:filling:subsection}.

Let $\calT$ be the triangulation with two tetrahedra shown in Figure \ref{triangulation_figure8:fig}. The truncated version is in Figure \ref{triangulation_figure8_2:fig}. We assign the complex variable $z$ and $w$ to the left and right tetrahedron, respectively. We set
$$z_1 = z, \quad z_2 = \frac{1}{1-z}, \quad z_3 = \frac {z-1}{z}$$
and define $w_1,w_2,w_3$ similarly. Recall that
\begin{equation} \label{m1:eq}
z_1z_2z_3 = w_1w_2w_3 = -1.
\end{equation}
The modulus of an edge in Figure \ref{triangulation_figure8_2:fig} labeled with $i\in \{1,2,3\}$ is $z_i$ or $w_i$ depending on the tetrahedron. With some patience one sees that the boundary triangulated surface is a torus $T$ as in Figure \ref{triangulation_figure8_3:fig}. The triangulation $\calT$ has two edges shown in Figure \ref{triangulation_figure8:fig}, each yielding a consistency equation. Figure \ref{triangulation_figure8_3:fig} shows that the consistency equations are
$$z_2^2z_3w_2^2w_3 = 1, \quad z_1^2z_3w_1^2w_3=1.$$
Using (\ref{m1:eq}) we see that the equations are both equivalent to 
$$z_2w_2 = z_1w_1,$$ 
that is
\begin{equation} \label{c:eqn}
z(1-z)w(1-w) = 1.
\end{equation}
We now look at the boundary torus $T$. Let $m$ and $l$ be the generators of $\pi_1(T)$ shown in Figure \ref{triangulation_figure8_3:fig}. We have
\begin{equation} \label{ml:eqn}
\mu(m) = - z_1z_3w_1 = w(1-z), \quad \mu(l) = z_2^2z_3^2w_1^4w_2^2w_3^2 = \frac{z^2}{w^2}.
\end{equation}
The completeness equations are
\begin{equation} \label{c2:eqn}
w(1-z) = 1,\quad z^2 = w^2.
\end{equation}

\begin{ex}
The only solution to (\ref{c:eqn}) and (\ref{c2:eqn}) is $z=w= e^{\frac{\pi i}3}$.
\end{ex}

We have confirmed that the figure-eight complement $M$ has a complete hyperbolic structure obtained by representing both tetrahedra with ideal regular hyperbolic tetrahedra. We now investigate the non-complete solutions of the consistency equations.

The two ideal tetrahedra have moduli $w$ and $z$ and the consistency equations reduce to one equation (\ref{c:eqn}) which we rewrite as
$$z^2 - z +\frac{1}{w(1-w)} = 0.$$
The solutions are
$$ z = \frac{1 \pm \sqrt{1-\frac 4{w(1-w)}}}{2}.$$
We are only interested in solutions with $\Im z, \Im w>0$. For every $w$ with $\Im w>0$ there is a unique solution $z$ with $\Im z >0$, except when $\Delta \in \matR_{\geqslant 0}$.

\begin{ex} 
We have $\Delta = 1-\frac 4{w(1-w)}\in\matR_{\geqslant 0}$ if and only if $w$ belongs to the half-line $s = \big\{\frac 12 + yi {\rm\ with\  } y\geqslant \frac{\sqrt{15}}2\big\}$, see Figure \ref{figure8_R:fig}-(left).
\end{ex}

\begin{figure}
\begin{center}
\includegraphics[width = 12.5 cm] {\iftoggle{BW}{figure8_R-BW}{figure8_R}} 
\nota{Every $w\in R$ determines a hyperbolic structure for $M$ (left). The Dehn filling generalised invariants $d$ map $R$ onto a neighbourhood of $\infty$ (right).}
\label{figure8_R:fig}
\end{center}
\end{figure}

We define the open region 
$$R =  \{w\in \matC\ |\ \Im w >0 \} \setminus s.$$
Every $w\in R$ determines a hyperbolic structure for $M$. The complete structure is obtained at $w_0=\frac 12 + \frac {\sqrt 3}2$, see Figure \ref{figure8_R:fig}-(left). 

The manifold $M$ is a knot complement and hence the boundary torus $T$ is equipped with its natural meridian/longitude basis $m',l'$, see Section \ref{canonical:longitudes:subsection}. Using SnapPea we find out that
$$m'=m, \qquad l'=l+2m.$$
From (\ref{ml:eqn}) we get
\begin{equation} \label{mlp:eqn}
 \tilde\mu(m') = w(1-z), \quad \tilde\mu(l') = \frac{z^2}{w^2} w^2(1-z)^2 = z^2(1-z)^2. 
\end{equation}
We fix $m',l'$ as generators for $\pi_1(T)$. We defined in Section \ref{generalized:DF:subsection} the generalised Dehn surgery invariant $(p,q) = d(w)$ for every non-complete solution $w\in R \setminus \{w_0\}$. This gives a continuous map
$$d \colon R \longrightarrow S^2$$
that sends $w_0$ to $\infty$.
\begin{prop}
The image $d(R)$ contains the coloured region shown in Figure \ref{figure8_R:fig}-(right).
\end{prop}
\begin{proof}
The domain $R$ is an open disc and its abstract closure $\bar R$ is homeomorphic to the closed disc. We show that $d$ extends to a continuous map $\bar R \to S^2$ which sends $\partial R$ to the almost-rectangle shown in Figure \ref{figure8_R:fig}. 

The invariants $d(w) = (p,q)$ are such that
\begin{equation} \label{pq:eqn}
w^p(1-z)^{p+2q}z^{2q} = e^{2\pi i}.
\end{equation}

The region $R$ has two involutions (determined in fact by isometries of $M$):
\begin{itemize}
\item the involution $\tau(w) = z = \frac{1 \pm \sqrt{1-\frac 4{w(1-w)}}}{2}$. This involution sends $\mu(m)$ to $\mu(m)^{-1} = \mu(m^{-1})$, hence $d(\tau(w)) = -d(w)$;
\item the involution $\sigma(w) = \overline{1-w}$: using (\ref{mlp:eqn}) we get $d(\sigma(w)) = \overline{d(w)}$.
\end{itemize}
Now we note that when $w$ tends to a point in the line $l_+ = [1, +\infty]$ then $z$ tends to a point in $l_- = [-\infty,0]$. Therefore the argument of $w,z,1-z$
tends respectively to $0, \pi, 0$. Equation (\ref{pq:eqn}) implies that $q \to 1$.

If $w\to 1$ then $z \to -\infty$ and (\ref{pq:eqn}) implies that $p+2q+2q=p+4q\to 0$, so $(p,q)\to (-4,1)$. If $w\to +\infty$ then $z \to 0$ and equation $z(1-z)w(1-w)=1$ implies that $|z||w|^2\to 1$; here (\ref{pq:eqn}) gives $|w|^{p-4q}\to 1$, hence $p-4q\to 0$, so $(p,q)\to (4,1)$. We have proved that $d$ maps $[1,+\infty]$ onto the segment 
$$\overline{(-4,+1), (+4,+1)}.$$
Using the involution $\tau$ we deduce that $d$ maps $[-\infty, 0]$ onto the segment
$$\overline{(+4,-1),(-4,-1)}.$$
When $w$ is near the right side of the half-line $s$, the number $z$ tends to the segment $(0,\frac 12]$. Therefore the arguments of $z$ and $1-z$ tend to $0$ and (\ref{pq:eqn}) implies that the argument of $w^p$ tends to $2\pi$. When $w\in s$ the argument of $w$ is at least $\arctan \sqrt{15} = 1.31811607\ldots $ and hence $p$ is at most $\frac{2\pi}{\arctan \sqrt{15}} = 4.374\ldots < 5$. This implies that we can connect $(4,1)$ and $(4,-1)$ while staying inside the image of $d$ with a curve as in Figure \ref{figure8_R:fig}.
\end{proof}

\subsection{A road map} \label{sketch:filling:subsection}
The rest of this chapter is mostly devoted to the proof of Theorem \ref{hyperbolic:Dehn:filling:teo}. Here is our plan: we first study the combinatorial properties of an arbitrary ideal triangulation $\calT$ for $M$, and we prove that the solutions to the consistency equations form a complex manifold $\Def(M,\calT)$ of (complex) dimension $c$ equal to the number of cusps of $M$. The manifold $\Def(M,\calT)$ is nicely parametrized by the holonomies on any $c$ fixed curves at different cusps. 

The manifold $\Def(M,\calT)$ is often empty, but since $M$ is hyperbolic we expect that there should be some ideal triangulation $\calT$ for which $\Def(M,\calT)$ is not empty and contains a solution $z$ that also satisfies the completeness equations (we are unfortunately not able to prove this in general, and this will be a technical issue). The generalised Dehn filling invariants defined in Section \ref{generalized:DF:subsection} furnish a local diffeomorphism $d\colon \Def(M,\calT) \to S^2 \times \ldots \times S^2$ that sends $z$ to $(\infty,\ldots,\infty)$. In particular this map is open and its image covers a neighbourhood $U$ of $(\infty,\ldots, \infty)$. We conclude thanks to the discussion of Section \ref{generalized:DF:subsection}. 

We start by defining and exploring the solution space $\Def(M,\calT)$.
