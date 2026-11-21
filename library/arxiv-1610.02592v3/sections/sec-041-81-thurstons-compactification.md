---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-041-81-thurstons-compactification
section_title: "Thurston's compactification"
section_number: 8.1
pages: 227-231
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.996
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
Let $S_g$ be a surface of genus $g\geqslant 2$.
Recall that $\Teich(S_g)$ is the Teichm\"uller space of $S_g$ and $\calS = \calS(S_g)$ is the set of all non-trivial simple closed curves in $S_g$, considered up to isotopy and orientation reversal: all the closed curves considered in this chapter are \emph{unoriented}. 

Although $\Teich(S_g)$ and $\calS$ are very different in nature, we want to compactify both spaces by embedding them in a single bigger space. The model that we have in mind, and that we would like to extend to higher genus surfaces, is the flat torus picture that was painted in Section \ref{length:torus:subsection}. 

We briefly summarise it. The Teichm\"uller space $\Teich(T)$ of the torus $T$ is $\matH^2$ and it compactifies to $\overline {\matH^2}$; the mapping class group $\MCG(T)$ acts on $\overline {\matH^2}$ as a discrete group of isometries; as such, the non-trivial elements of $\MCG(T)$ are divided into three classes (hyperbolic, parabolic, elliptic); the simple closed curves form a dense countable set of rational points in $\partial \matH^2 = \matR\cup \{\infty\}$.

We now may wonder whether there is an analogous identification between $\Teich(S_g)$ and $\matH^{6g-6}$ that transforms $\Teich(S_g)$ into a discrete subgroup of $\Iso(\matH^n)$. This is unfortunately not the case, and the compactification of $\Teich(S_g)$ must be constructed from scratch via different methods: we compactify $\Teich(S_g)$ by embedding it in a bigger infinite-dimensional space.


\subsection{Projective immersion} \label{projective:immersion:subsection}
In Chapter  \ref{Teichmuller:chapter} we have used the length functions to construct an embedding
$$i\colon \Teich(S_g) \hookrightarrow \matR^\calS.$$
We know that $\Teich(S_g)$ is homeomorphic to an open ball of dimension $6g-6$, and we want to compactify it in a geometrically meaningful way. A first tentative could be to take its closure in $\matR^\calS$, but this does not work:

\begin{prop}
The subspace $i(\Teich(S_g))$ is closed in $\matR^\calS$.
\end{prop}
\begin{proof}
The inclusion is proper, hence closed by Proposition \ref{propria:chiusa:prop}.
\end{proof}

We are apparently stuck, so we turn back to our model, hyperbolic space, to get some inspiration. We recall that $\matH^n$ is properly embedded in the lorentzian $\matR^{n+1}$ as a hyperboloid $I^n$. To compactify $\matH^n$, we may consider its image $K^n$ in $\matRP^n$ (the Klein model) and take the closure $\overline{K^n}$ there.

We try to mimic this construction, by considering the infinite-dimensional projective space $\matP(\matR^\calS)$ with the projection 
$$\pi\colon \matR^\calS\setminus \{0\} \longrightarrow \matP(\matR^\calS).$$
We first need to check that $\Teich(S_g)$ embeds there.
\begin{prop}
The composition
$$\pi\circ i \colon \Teich(S_g) \longrightarrow \matP(\matR^\calS)$$
is injective.
\end{prop}
\begin{proof}
Suppose by contradiction that there are two distinct points $m, m' \in \Teich(S_g)$ with $\pi(i(m)) = \pi(i(m'))$; this implies that there is a constant $k>1$ such that $\ell^\gamma(m) = k\cdot\ell^\gamma(m')$ for all $\gamma\in\calS$. That sounds very unlikely, and we now prove that it easily leads to a contradiction.

Let $\gamma_1, \gamma_2 \in \calS$ be two curves with $i(\gamma_1,\gamma_2)=1$. We take $x_0 = \gamma_1 \cap \gamma_2$ as a basepoint for $\pi_1(S_g, x_0)$ and note that the elements $\gamma_2*\gamma_1$ and $\gamma_2*\gamma_1^{-1}$ are represented by two more non-trivial simple closed curves in $S_g$. It is easily checked that the formula
$$\tr(A)\cdot \tr(B) = \tr(AB) + \tr(A^{-1}B)$$
holds for any $A,B \in \SLR$. Proposition \ref{trace:prop} implies that
$$2\cosh \left(\frac{L(\gamma_1)}2 \right) \cdot \cosh\left(\frac{L(\gamma_2)}2 \right) = 
\cosh\left(\frac{L(\gamma_2*\gamma_1)}2 \right) + \cosh\left(\frac{L(\gamma_2*\gamma_1^{-1})}2 \right).$$
We have obtained a relation between the lengths of $\gamma_1, \gamma_2$, $\gamma_2* \gamma_1$, and $\gamma_2*\gamma_1^{-1}$ that holds for any hyperbolic metric on $S_g$. It may be rewritten as: 
$$ \cosh\left(\tfrac{L(\gamma_1) + L(\gamma_2)}2 \right) + \cosh\left(\tfrac{L(\gamma_1) - L(\gamma_2)}2 \right) = \cosh\left(\tfrac{L(\gamma_2*\gamma_1)}2 \right) + \cosh\left(\tfrac{L(\gamma_2*\gamma_1^{-1})}2 \right).
$$
By contradiction every $m'$-length is $k$ times a $m$-length: this equation is hence valid after multiplying every argument by $k$. It is easy to check that 
$$\cosh a + \cosh b = \cosh c + \cosh d, \quad \cosh ka + \cosh kb = \cosh kc + \cosh kd$$ 
if and only if $\{a,b\} = \{c,d\}$. This leads to a contradiction: the number $L(\gamma_1)+L(\gamma_2)$ is strictly bigger than $L(\gamma_2*\gamma_1)$ or $L(\gamma_2*\gamma_1^{-1})$, since $\gamma_2*\gamma_1$ and $\gamma_2*\gamma_1^{-1}$ have a non-geodesic representative of length $L(\gamma_1)+L(\gamma_2)$.
\end{proof}

We have embedded $\Teich(S_g)$ in $\matP(\matR^\calS)$, and we now turn to the set $\calS$.


\subsection{Thurston's compactification}
We now embed $\calS$ in $\matP(\matR^\calS)$. A simple closed curve $\gamma \in \calS$ defines a functional $i(\gamma) \in \matR^\calS$ by setting:
$$i(\gamma)(\eta) = i(\gamma, \eta).$$
We have constructed a map $i\colon \calS \to \matR^\calS$.
\begin{prop}
The composition
$$\pi \circ i\colon\calS \longrightarrow \matP(\matR^\calS)$$
is injective.
\end{prop}
\begin{proof}
Let $\gamma_1, \gamma_2\in \calS$ be distinct. There is always a curve $\eta\in\calS$ with $i(\gamma_1,\eta)\neq 0$ and $i(\gamma_2,\eta)=0$. (If $i(\gamma_1,\gamma_2)>0$, simply take $\eta=\gamma_2$. Otherwise, it is an easy exercise.)
\end{proof}

We will now tacitly consider both $\Teich(S_g)$ and $\calS$ as subsets of $\matR^\calS$.
\begin{prop}
The subsets $\Teich(S_g)$ and $\calS$ are disjoint in $\matP(\matR^\calS)$.
\end{prop}
\begin{proof}
For each $\gamma\in\calS$ we have $i(\gamma,\gamma)=0$, while every curve has positive length on any hyperbolic metric.
\end{proof}

We can now state Thurston's compactification theorem.\index{Thurston's compactification theorem} 

\begin{teo} \label{compattificazione:teo}
The closure $\overline{\Teich(S_g)}$ of $\Teich(S_g)$ in $\matP(\matR^\calS)$ is homeomorphic to the closed disc $D^{6g-6}$. Its interior is $\Teich(S_g)$ and its boundary sphere contains $\calS$ as a dense subset.
\end{teo}
In particular, the closure of $\calS$ is homeomorphic to a sphere $S^{6g-7}$. 
The proof of Theorem \ref{compattificazione:teo} occupies most of this chapter and will be completed in Section \ref{MCG:conclusion:subsection}. We will introduce in the process various new geometric objects that play an important role in the topology of manifolds in dimension two and three: \emph{geodesic currents}, \emph{laminations}, and \emph{train tracks}.

For the moment we content ourselves with checking that this projective embedding strategy works at least on the much simpler flat torus case.


\subsection{The torus}
The Teichm\"uller space of the torus $T$ is described in Section \ref{length:torus:subsection} and needs no further comment; nevertheless, we prove here that the projective embedding strategy works for $T$, just as a sanity check before approaching the more complicated higher genus surfaces.

\begin{prop} \label{T:compactification:prop}
The space $\Teich(T)$ embeds in $\matP(\matR^\calS)$ and its closure there is homeomorphic to a closed disc $D^2$. The interior of this disc is $\Teich(T)$ and its boundary contains $\calS$ as a dense subset.
\end{prop}
\begin{proof}
Everything can be written explicitly by identifying $\Teich(T)$ with the half-plane $H^2$ and $\calS$ with the set $\matQ\cup \{\infty\} \subset \partial H^2$. Exercise \ref{i:torus:ex} and Proposition \ref{lunghezza:toro:prop} give
\begin{align*}
i\left(\frac pq, \frac rs \right) & = \left|\det \begin{pmatrix} p & r \\ q & s \end{pmatrix}\right| = |ps-qr| = |s|\cdot \left|p-q\frac rs \right|, \\ 
\ell^{\frac pq}(z) & = \frac {|p+qz|}{\sqrt{\Im z}}.
\end{align*}
Therefore the images of $\frac rs\in\calS$ and $z\in H^2 = \Teich(T)$ in $\matP(\matR^\calS)$ are respectively the functionals
\begin{align*}
\frac pq & \longmapsto \left|p - q\frac rs\right| \ {\rm if\ } s \neq 0 {\rm \ and \ } |q|\ {\rm if } \ s=0, \\
\frac pq & \longmapsto \left|p+qz\right|.
\end{align*}
We could remove the constants $|s|$ and $\sqrt{\Im z}$ because we are considering functionals in $\matP(\matR^\calS)$ rather than in $\matR^\calS$. 
We define for all $z \in  \overline{H^2}$ the functional
\begin{align*}
f_z & \colon \frac pq \longmapsto |p+qz| \quad {\rm if\ } z\neq \infty,\\
f_\infty & \colon \frac pq \longmapsto |q|.
\end{align*}
and we get a continuous immersion $z \mapsto f_z$ of $\overline{H^2}$ into $\matP(\matR^\calS)$. The immersion is closed because it sends a compact space to a Hausdorff space, hence it is a homeomorphism onto its image. The image is the closure of $\Teich(T)$ and its boundary contains $\calS$ as a dense set.
\end{proof}
