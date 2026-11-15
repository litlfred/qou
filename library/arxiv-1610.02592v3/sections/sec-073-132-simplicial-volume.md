---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-073-132-simplicial-volume
section_title: "Simplicial volume"
section_number: 13.2
pages: 418-425
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.997
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
Gromov has introduced a topological invariant on closed manifolds of any dimension called the \emph{simplicial volume}. This nice invariant can be used, among other things, to prove Mostow's rigidity theorem.\index{simplicial volume}


\subsection{Definition}
Gromov has introduced a measure of ``volume'' of a closed manifold $M$ which makes use only of the homology of $M$. Quite surprisingly, this notion of volume coincides (up to a factor) with the Riemannian one when $M$ is hyperbolic. 

Consider a topological space $X$ and its homology with ring $\matR$. We define the \emph{norm} of a cycle $\alpha = \lambda_1\alpha_1+\ldots +\lambda_h\alpha_h$ as follows:
$$|\alpha| = |\lambda_1|+\ldots +|\lambda_h|.$$

\begin{defn} The \emph{norm} of a class $a \in H_k(X,\matR)$ is the infimum of the norms of its elements: 
$$|a| = \inf \big\{|\alpha| \ \big|\ \alpha \in Z_k(X,\matR), [\alpha] = a \big\}.$$
\end{defn}

Recall that a \emph{seminorm} on a real vector space $V$ is a map $|\cdot|\colon V \to \matR_{\geqslant 0}$ such that
\begin{itemize}
\item $|\lambda v| = |\lambda||v|$ for any scalar $\lambda\in \matR$ and vector $v\in V$,
\item $|v+w| \leqslant |v|+|w|$ for any pair of vectors $v,w \in V$.
\end{itemize}
A \emph{norm} is a seminorm where $|v|=0$ implies $v=0$. The following is immediate.
\begin{prop} The norm $|\cdot |$ induces a seminorm on $H_k(X,\matR)$.
\end{prop}

Although it is only a seminorm, the function $|\cdot|$ is called a norm for simplicity. Let now $M$ be an oriented closed connected manifold: we know that $H_n(M,\matZ)\isom \matZ$ and the orientation of $M$ determines a \emph{fundamental class} $[M] \in H_n(M,\matZ)$ that generates the group. Moreover $H_n(M,\matR)\isom \matR$ and there is a natural inclusion\index{fundamental class}  
$$\matZ \isom H_n(M,\matZ) \hookrightarrow H_n(M,\matR) \isom \matR$$
hence the fundamental class $[M]$ is also an element of $H_n(M,\matR)$ and has a norm. 
\begin{defn} The \emph{simplicial volume} $\|M\|\in\matR_{\geqslant 0}$ of a closed oriented connected $M$ is the norm of its fundamental class:
$$\|M\| = |[M]|$$
\end{defn}
Since $|[M]| = |-[M]|$ the simplicial volume actually does not depend on the orientation. 
When $M$ is non-orientable we set $\|M\| = \big\|\tilde M\big\|/2$ where $\tilde M$ is the orientable double cover of $M$. The definition of $\|M\|$ is relatively simple but has various non-obvious consequences.


\subsection{Properties}
A continuous map $f\colon M \to N$ between closed oriented $n$-manifolds induces a homomorphism $f_*\colon H_n(M,\matZ) \to H_n(N,\matZ)$, and recall that the \emph{degree} of $f$ is the integer $\deg f$ such that
$$f_*([M]) = \deg f \cdot [N].$$

\begin{prop} \label{grado:prop}
Let $f\colon M\to N$ be a continuous map between closed oriented manifolds. The following inequality holds:
$$\|M\| \geqslant |\deg f| \cdot \|N\|.$$
\end{prop}
\begin{proof}
Every description of $[M]$ as a cycle $\lambda_1\alpha_1+\ldots +\lambda_h\alpha_h$ induces a description of $f_*([M]) = \deg f[N]$ as a cycle $\lambda_1f\circ\alpha_1+\ldots +\lambda_hf\circ\alpha_h$ with the same norm (or less, if there is some cancelation). 
\end{proof}

\begin{cor}
If $M$ and $N$ are closed orientable and homotopically equivalent $n$-manifolds then $\|M\|=\|N\|$.
\end{cor}
\begin{proof}
A homotopic equivalence consists of two maps $f\colon M\to N$ and $g\colon N \to M$ whose compositions are both homotopic to the identity. In particular both $f$ and $g$ have degree $\pm 1$.
\end{proof}

\begin{cor}
If $M$ admits a continuous self-map $f\colon M \to M$ of degree at least two then $\|M\| = 0$.
\end{cor}
\begin{cor}
Every sphere $S^n$ has norm zero. More generally we have $\|M\times S^n\|=0$ for every closed $M$ and any $n\geqslant 1$.
\end{cor}
\begin{proof}
A sphere $S^n$ admits self-maps of degree $\geqslant 2$, and hence also the product $M\times S^n$ does.
\end{proof}
Among the genus-$g$ surfaces $S_g$, we deduce that the sphere and the torus have simplicial volume zero. We will see soon that every surface of genus $g\geqslant 2$ has positive simplicial volume. When the continuous map is a covering the inequality from Proposition \ref{grado:prop} is promoted to an equality.

\begin{prop}
If $f\colon M \to N$ is a degree-$d$ covering we have 
$$\|M\| = d \cdot \|N \|.$$
\end{prop}
\begin{proof} 
The reason for this equality is that cycles can be lifted and projected through the covering. More precisely, we already know that $\|M\|\geqslant d\cdot \|N\|$. Conversely, let $\alpha = \lambda_1\alpha_1+\ldots +\lambda_h\alpha_h$ represent $[N]$; each $\alpha_i$ is a map $\Delta_n\to N$. Since $\Delta_n$ is simply connected, the map $\alpha_i$ lfts to $d$ distinct maps $\alpha_i^1,\ldots, \alpha_i^d\colon \Delta_n\to N$. The chain $\tilde\alpha = \sum_{ij} \lambda_i\alpha_i^j$ is a cycle in $M$ and $f_*(\tilde \alpha) = d\alpha$. Hence $\|M\|\leqslant d\cdot \|N\|$.
\end{proof}

We also note the following fact.

\begin{prop}
If $M$ is triangulated with $k$ simplices, then $\|M\| \leqslant k$.
\end{prop}
\begin{proof}
Up to taking a double cover we may suppose that $M$ is oriented. The closed $n$-manifold $M$ is triangulated into some simplices $\Delta_1, \ldots, \Delta_k$, and
we fix an orientation-preserving parametrisation $s_i\colon \Delta \to \Delta_i$ of each.
We would like to say that $s_1+\ldots + s_k$ is a fundamental cycle, however this singular chain is not necessarily a cycle because the restriction to adjacent faces coincide only up to the symmetries $S_{n+1}$ of $\Delta$. 

We can fix this problem easily by averaging each $s_i$ on all its permutations, that is we substitute each $s_i$ with $\frac{1}{(n+1)!}\sum_{\sigma \in S_{n+1}} (-1)^{{\rm sgn}(\sigma)} s_i \circ \sigma$. Now $s=s_1+\ldots + s_k$ is a fundamental cycle and $|s| = k$.
\end{proof}


\subsection{Seifert manifolds}
We can now calculate the simplicial volume of Seifert manifolds.

\begin{prop}
If $M$ is a closed Seifert 3-manifold then $\|M\|=0$.
\end{prop}
\begin{proof}
Every Seifert manifold is finitely covered by a product $S \times S^1$ (if $e=0$) or by a bundle $\big(S,(1,1)\big)$ with Euler number 1 (if $e\neq 0$). In the first case we are done since $\|S\times S^1\|=0$. 

In the second, if $S=S^2$ then $\big(S^2,(1,1)\big)=S^3$ and $\|S^3\|=0$, so we suppose $\chi(S)\leqslant 0$. There is a universal $K>0$ such that $\big(S,(1,1)\big)$ triangulates with at most $K|\chi (S)|+K$ tetrahedra (exercise) and therefore $\big\|\big(S,(1,1)\big)\big\| \leqslant K|\chi(S)|+K$. Exercise \ref{e:construct:ex} shows that for every $e>0$ there is a degree-$e$ covering $\tilde S \to S$ and two degree-$e$ coverings
$$\big(\tilde S, (1,1)\big) \longrightarrow \big(\tilde S, (1,e)\big) \longrightarrow \big(S,(1,1)\big)$$
which compose to a degree-$e^2$ covering 
$\big(\tilde S, (1,1)\big) \to \big(S,(1,1)\big)$. Therefore
$$\big\|\big(S, (1,1) \big) \big\| = \frac{\big\|\big(\tilde S, (1,1) \big) \big\|}{e^2} \leqslant \frac{K|\chi(\tilde S)| + K}{e^2} \leqslant \frac{Ke|\chi(S)| + K}{e^2} \to 0$$
as $e \to \infty$.
\end{proof}



\subsection{Simplicial and hyperbolic volume}
In the next pages we will prove the following theorem. Let $v_3$ be the volume of the regular ideal tetrahedron in $\matH^3$.

\begin{teo} \label{Gromov:teo}
Let $M$ be a closed hyperbolic $3$-manifold. We have 
$$\Vol(M) = v_3\|M\|.$$
\end{teo}
The theorem furnishes in particular some examples of manifolds with positive simplicial volume and shows that $\Vol(M)$ is a topological invariant of $M$, thus generalising the Gauss-Bonnet theorem to dimension $n=3$. Mostow rigidity will then strengthen this result in dimension $n = 3$, showing that the hyperbolic metric itself (not only its volume) is a topological invariant.

Both quantities $\Vol(M)$ and $\|M\|$ are multiplied by $d$ if we substitute $M$ with a degree-$d$ covering. In particular, up to substituting $M$ with its orientable double cover we can suppose that $M$ is orientable. 


\subsection{Cycle straightening}
The \emph{straight singular $k$-simplex} with vertices $v_0,\ldots, v_{k} \in \matH^n$ is the map
\begin{align*}
\alpha\colon \quad \ \Delta_k & \longrightarrow \matH^n \\
(t_0,\ldots, t_{k}) & \longmapsto t_0v_0 + \ldots + t_{k}v_{k}
\end{align*}
defined using convex combinations, see Section \ref{convex:subsection}. If the $k+1$ vertices are not contained in a $(k-1)$-plane the singular $k$-simplex is \emph{non-degenerate} and its image is a hyperbolic $k$-simplex.

The \emph{straightening} $\alpha^\st$ of a singular simplex $\alpha\colon \Delta_k \to \matH^n$ is the straight singular simplex with the same vertices of $\alpha$. The straightening $\alpha^\st$ of a singular simplex $\alpha\colon\Delta_k\to M$ in a hyperbolic manifold $M=\matH^n/_\Gamma$ is defined by lifting the singular simplex in $\matH^n$, straightening it, and projecting it back to $M$ by composition with the covering map.
Different lifts produce the same straightening in $M$ because they are related by isometries of $\matH^n$. 

The straightening extends by linearity to a homomorphism
$$\st\colon C_k(M,R) \to C_k(M,R)$$
which commutes with $\partial$ and hence induces a homomorphism in homology
$$\st_*\colon H_k(M,R) \to H_k(M,R).$$
\begin{prop} The map $\st_*$ is the identity.
\end{prop}
\begin{proof}
We may define a homotopy between a singular simplex $\sigma$ and its straightening $\sigma^{\rm st}$ using the convex combination
$$\sigma^t(x) =t\sigma(x) + (1-t)\sigma^{\rm st}(x).$$
This defines a chain homotopy between $\st_*$ and $\id$ via the same technique used to prove that homotopic maps induce the same maps in homology.
\end{proof}

The \emph{abstract volume} of a straightened singular $n$-simplex $\alpha\colon\Delta_n \to M$ is the volume of its lift in $\matH^n$ and may also be calculated as
$$\left|\int_\alpha \omega\right|$$
where $\omega$ is the volume form on $M$ pulled back along $\alpha$. 
If $\alpha$ is non-degenerate, we say that its \emph{sign} is \emph{positive} if $\alpha$ is orientation-preserving and \emph{negative} otherwise: equivalently, it is the sign of $\int_\alpha\omega$.

We now concentrate on the dimension $n=3$ where we know that a tetrahedron has maximum volume $v_3$ if and only if it is both regular and ideal: a straight simplex is compact and hence its abstract volume is strictly smaller than $v_3$. 
We can now easily prove one inequality. 

\begin{prop} \label{Gromov:1:prop}
Let $M$ be a closed hyperbolic $3$-manifold. We have
$$\Vol(M) \leqslant v_3 \|M\|.$$
\end{prop}
\begin{proof}
As we said above, we can suppose that $M$ is orientable. Take a cycle $\alpha = \lambda_1\alpha_1+\ldots+\lambda_k\alpha_k$ that represents $[M]$. We can suppose it is straightened, because the straightening preserves both the coefficients and the homology class. Let $\omega$ be the volume form on $M$. We get 
$$\Vol (M) = \int_M \omega = \int_\alpha \omega = \lambda_1 \int_{\alpha_1}\omega + \ldots + \lambda_k \int_{\alpha_k}\omega.$$
The quantity $\big|\int_{\alpha_i}\omega\big|$ is the abstract volume of $\alpha_i$. Hence $\big|\int_{\alpha_i}\omega\big|<v_3$ and
$$\Vol(M) < \big(|\lambda_1|+ \ldots +|\lambda_k|\big)v_3.$$
This holds for all $\alpha$, hence $\Vol(M) \leqslant v_3 \|M\|$.
\end{proof}

The proof of the converse inequality is less immediate.


\subsection{Efficient cycles} \label{efficienti:subsection}
Let $M=\matH^3/_\Gamma$ be a closed oriented hyperbolic 3-manifold. 
An \emph{$\varepsilon$-efficient cycle} for $M$ is a straightened cycle
$$\alpha = \lambda_1\alpha_1 + \ldots + \lambda_k\alpha_k$$
representing $[M]$ where the abstract volume of $\alpha_i$ if bigger than $v_3-\varepsilon$ and the sign of $\alpha_i$ is coherent with the sign of $\lambda_i$, for all $i$.

We will construct an $\varepsilon$-efficient cycle for every $\varepsilon >0$. This will conclude the proof of Theorem \ref{Gromov:teo} in virtue of the following:

\begin{lemma}
If for every $\varepsilon>0$ the manifold $M$ admits an $\varepsilon$-efficient cycle, then we have $\Vol(M) \geqslant v_3 \|M\|$.
\end{lemma}
\begin{proof}
Let $\alpha = \lambda_1\alpha_1 + \ldots \lambda_k\alpha_k$ be an $\varepsilon$-efficient cycle and $\omega$ be the volume form on $M$. Coherence of signs gives $\lambda_i\int_{\alpha_i}\omega>0$ for all $i$.
We get
\begin{align*}
\Vol(M) & = \int_M \omega = \int_\alpha \omega = \lambda_1 \int_{\alpha_1} \omega + \ldots + \lambda_k \int_{\alpha_k} \omega  \\
& \geqslant \big(|\lambda_1| + \ldots + |\lambda_k|\big) \cdot (v_3 - \varepsilon).
\end{align*}
Therefore $\Vol(M) \geqslant \|M\| \cdot (v_3 - \varepsilon)$ for all $\varepsilon > 0$.
\end{proof}

It remains to construct $\varepsilon$-efficient cycles.

\begin{ex} \label{volume:continuo:ex}
If $\Delta^i$ is a sequence of tetrahedra in $\matH^3$ whose vertices tend to the vertices of a regular ideal tetrahedron in $\partial\matH^3$, then
$$\Vol(\Delta^i)\to v_3.$$
\end{ex}

For any $t>0$, let $\Delta(t)$ be a regular tetrahedron obtained as in Section \ref{platonici:subsection} as follows.
Pick a point $x\in \matH^3$ and a regular tetrahedron in the Euclidean tangent space $T_x\matH^3$, centred at the origin with vertices at distance $t$ from it, project the vertices in $\matH^3$ via the exponential map, and pick their convex hull.

A \emph{$t$-simplex} is a tetrahedron isometric to $\Delta(t)$ equipped with an ordering of its vertices: the ordering allows us to consider it as a straightened singular simplex. Let $S(t)$ be the set of all $t$-simplices in $\matH^3$.

\begin{ex} The group $\Iso(\matH^3)$ acts on $S(t)$ freely and transitively.
\end{ex}

Recall from Corollary \ref{unimodular:cor} that $\Iso(\matH^3)$ is unimodular:
the Haar measure on $\Iso(\matH^3)$ induces an $\Iso(\matH^3)$-invariant measure on $S(t)$. 

Let $M=\matH^3/_\Gamma$ be a closed hyperbolic 3-manifold and $\pi\colon\matH^3 \to M$ the covering projection. Fix a base point $x_0 \in \matH^3$ and consider its orbit $O=\Gamma x_0$. Consider the set
$$\Sigma = \Gamma^{4}/_\Gamma$$
of the $4$-uples $(g_0,g_1,g_2, g_3)$ considered up to the diagonal action of $\Gamma$:
$$g \cdot (g_0,g_1,g_2, g_3) = (g g_0,gg_1, gg_2, g g_3).$$
An element $\sigma = (g_0,g_1,g_2, g_3) \in \Sigma$ determines a singular simplex $\tilde\sigma$ in $\matH^3$ with vertices $g_0(x_0), g_1(x_0), g_2(x_0), g_3(x_0)\in O$ only up to translations by $g\in\Gamma$, hence it gives a well-defined singular simplex in $M$, which we still denote by $\sigma$. We now introduce the chain
$$\alpha(t) = \sum_{\sigma \in \Sigma} \lambda_\sigma(t) \cdot \sigma$$
for some appropriate real coefficients $\lambda_\sigma(t)$ that we now define. The base point $x_0$ determines the Dirichlet tessellation of $\matH^3$ into domains $D(g(x_0))$, $g\in\Gamma$. For $\sigma = (g_0,g_1,g_2, g_3)$ we let $S^+_\sigma(t)\subset S(t)$ be the set of all positive $t$-simplices whose $i$-th vertex lies in $D(g_i(x_0))$ for all $i$. The number $\lambda^+_\sigma(t)$ is the measure of $S^+_\sigma(t)$. We define analogously $\lambda^-_\sigma(t)$ and set
$$\lambda_\sigma(t) = \lambda^+_\sigma(t) - \lambda^-_\sigma(t).$$

\begin{lemma} \label{ciclo:lemma}
The chain $\alpha(t)$ has finitely many addenda and is a cycle. If $t$ is sufficiently big the cycle $\alpha(t)$ represents a positive multiple of $[M]$ in the group $H_3(M,\matR)$.
\end{lemma}
\begin{proof}
We prove that the sum is finite. Let $d, T$ be the diameters of $D(x_0)$ and of a $t$-simplex. 
We write $\sigma = (\id,g_1,g_2,g_3)$ for all $\sigma \in \Sigma$: that is, all simplices have their first vertex at $x_0$. 
If $\lambda_\sigma(t)\neq 0$ then $d(g_ix_0, x_0) < 2d+T$ for all $i$: therefore $\alpha(t)$ has finitely many addenda (because $O$ is discrete).

We prove that $\alpha(t)$ is a cycle. The boundary $\partial \alpha(t)$ is a linear combination of straight $2$-simplices with vertices in $(g_0x_0, g_1x_0, g_2x_0)$ as $g_0, g_1$, and $g_2$ vary. The coefficient of one such $2$-simplex is
$$\sum_{g\in\Gamma} \big(- \lambda_{(g,g_0,g_1,g_2)}(t) + \lambda_{(g_0,g,g_1,g_2)}(t)
- \lambda_{(g_0,g_1,g,g_2)}(t) + \lambda_{(g_0,g_1,g_2,g)}(t)\big).$$
We prove that each addendum summed along $g\in \Gamma$ is zero; for simplicity we consider the last addendum and get
$$\sum_{g\in\Gamma} \lambda_{(g_0, g_1, g_{2}, g)}(t) = \sum_{g\in\Gamma} \lambda_{(g_0, g_1, g_{2}, g)}(t)^+ - \sum_{g\in\Gamma} \lambda_{(g_0, g_1, g_{2}, g)}(t)^-.$$
The first addendum measures the positive $t$-simplices whose first $3$ vertices lie in $D(g_0(x_0)), \ldots, D(g_2(x_0))$, the second measures the negative $t$-simplices with the same requirement. These two subsets have the same volume in $S(t)$ because they are related by the involution $r\colon S(t) \to S(t)$ that mirrors a simplex with respect to its first facet. 

We show that for sufficiently big $t$ the cycle is a positive multiple of $[M]$. Let $t$ be sufficiently big so that two vertices in a $t$-simplex have distance 
bigger than $2d$. This condition implies that if there is a positive $t$-simplex with vertices in $D(g_0(x_0)), \ldots, D(g_3(x_0))$, then any straight simplex with vertices in $D(g_0(x_0)), \ldots, D(g_3(x_0))$ is positive. 
Therefore in the expression
$$\alpha(t) = \sum_{\sigma \in \Sigma} \lambda_\sigma(t) \cdot \sigma$$
the signs of $\lambda_\sigma(t)$ and $\sigma$ are coherent and
$$\int_{\alpha(t)} \omega = \sum_{\sigma\in \Sigma} \lambda_\sigma(t) \cdot \int_{\sigma}\omega > 0.$$
Therefore $\alpha(t)$ is a positive multiple of $[M]$.
\end{proof}

For sufficiently big $t$ we have $\alpha(t) = k_t[M]$ in homology for some $k_t>0$. The rescaled $\bar\alpha(t) = \alpha(t)/k_t$ hence represents $[M]$.
We have found our $\varepsilon$-efficient cycles. 

\begin{lemma} \label{efficiente:lemma}
For any $\varepsilon>0$ there is a $t_0>0$ such that $\bar\alpha(t)$ is $\varepsilon$-efficient for all $t>t_0$.
\end{lemma}
\begin{proof}
Let $d$ be the diameter of the Dirichlet domain $D(x_0)$. Let a \emph{quasi $t$-simplex} be a simplex whose vertices are at distance $<d$ from those of a $t$-simplex. By construction $\bar\alpha(t)$ is a linear combination of quasi $t$-simplices.

We now show that for any $\varepsilon>0$ there is a $t_0>0$ such that for all $t>t_0$ every quasi $t$-simplex has volume bigger than $v_3-\varepsilon$. By contradiction, let $\Delta^t$ be a sequence of quasi $t$-simplices of volume smaller than $v_3-\varepsilon$ with $t\to\infty$. The vertices of $\Delta^t$ are $d$-closed to a $t$-simplex $\Delta_*^t$, and we move the pair $\Delta^t, \Delta^t_*$ isometrically so that the $t$-simplices $\Delta_*^t$ have the same barycenter. Now both the vertices of $\Delta^t$ and $\Delta^t_*$ tend to the vertices of an ideal regular tetrahedron and Exercise \ref{volume:continuo:ex} gives a contradiction.
\end{proof}

The previous lemmas together prove the second half of Theorem \ref{Gromov:teo}.
\begin{cor}
Let $M$ be a closed hyperbolic $3$-manifold. We have
$$\Vol(M) \geqslant v_3 \|M\|.$$
\end{cor}

Theorem \ref{Gromov:teo} has some non-trivial consequences.

\begin{cor} \label{degree:d:cor}
Let  $M, N$ be two closed orientable hyperbolic $3$-manifolds. If there is a map $f\colon M\to N$ of degree $d$ then $\Vol(M)\geqslant |d| \cdot \Vol(N)$.
\end{cor}

\begin{cor} \label{stesso:volume:cor}
Two homotopically equivalent and closed hyperbolic 3-manifolds have the same volume.
\end{cor}

\begin{rem}
If we are able to prove that the regular ideal simplex has the maximum volume $v_n$ among hyperbolic $n$-simplices in $\matH^n$, then the whole proof extends as is from $\matH^3$ to $\matH^n$ and shows that $\Vol(M) = v_n \cdot |M|$ for any closed hyperbolic $n$-manifold $M$. This is obviously true when $n=2$, and we get $v_2 = \pi$. 
\end{rem}
