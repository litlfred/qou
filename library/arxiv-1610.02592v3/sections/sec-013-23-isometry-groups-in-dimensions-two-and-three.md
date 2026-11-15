---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-013-23-isometry-groups-in-dimensions-two-and-three
section_title: "Isometry groups in dimensions two and three"
section_number: 2.3
pages: 72-76
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.99
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{isometry:2:3:section}
With the hyperboloid model the isometry group $\Iso(\matH^n)$ is the matrix group $O^+(n,1)$. We now see that in dimensions $n=2$ and $3$ the group $\Iso^+(\matH^n)$ is also isomorphic to some familiar groups of $2\times 2$ matrices. 

We start with a concise tour on M\"obius transformations. 
\index{M\"obius transformation and anti-transformation}


\subsection{M\"obius transformations}
Let the \emph{Riemann sphere} be $S=\matC \cup \{\infty\}$, homeomorphic to $S^2$. Consider the group
$$ \PSLC = \SLC/_{\pm I} = \GLC/_{\{ \lambda I\}} = \PGLC $$
of all $2\times 2$ invertible complex matrices considered up to scalar multiplication. The group $\PSLC$ acts on $S$ as follows: a matrix $\matr abcd \in \PSLC$ determines the \emph{M\"obius transformation} 
$$z \mapsto \frac{az+b}{cz+d}$$
which is an orientation-preserving self-diffeomorphism of $S$, and in fact also a  biolomorphism.

\begin{ex} \label{Mobius:freely:ex}
M\"obius transformations act freely and transitively on triples of distinct points in $S$.
\end{ex}

A matrix $ \matr abcd\in \PSLC$ also determines a \emph{M\"obius anti-transformation}
$$z \mapsto \frac{a\bar z+b}{c\bar z+d}$$
which is an orientation-reversing self-diffeomorphism of $S$. The composition of two anti-transformations is a M\"obius transformation. Transformations and anti-transformations together form a group $\Conf(S)$ which contains the M\"obius transformations as an index-two subgroup.

\begin{prop}
Circle inversions and line reflections are both M\"obius anti-transformations and generate $\Conf(S)$.
\end{prop}
\begin{proof}
By conjugating with translations $z\mapsto z+b$ and complex dilations $z \mapsto az$ every circle inversion transforms into the inversion along the unit circle $z\mapsto \frac{1}{\bar z}$, and every line reflection transforms into $z\mapsto \bar z$.

By composing line reflections we get all translations and rotations, and by composing circle inversions we get all dilations. With these operations and the inversion $z\mapsto \frac 1 {\bar z}$ one can easily act transitively on triples of points. They generate $\Conf(S)$ by Exercise \ref{Mobius:freely:ex}.
\end{proof}


\subsection{M\"obius transformations of $H^2$}
We consider the half-plane $H^2\subset \matC$ as $H^2 = \{z\ |\ \Im z >0\}$ and denote by $\Conf(H^2)$ the subgroup of $\Conf(S)$ consisting of all maps that preserve $H^2$.

\begin{rem}
By standard results in complex analysis, the two groups $\Conf(S)$ and $\Conf(H^2)$ contain precisely all the conformal diffeomorphisms of $S$ and $H^2$, whence their names. We will not use this fact here.
\end{rem}

\begin{prop}
The maps in $\Conf(H^2)$ are of the form
$$z \mapsto \frac{az+b}{cz+d} \qquad {\rm and}
\qquad z \mapsto \frac{a\bar z+b}{c\bar z+d}$$
with $a,b,c,d \in \matR$ and having $ad-bc$ equal to $1$ and $-1$, respectively. 
\end{prop}
\begin{proof}
The transformations listed have real coefficients and hence preserve the line $\matR\cup \infty$ and permute the two half-planes in $\matC\setminus \matR$. The sign condition on $ad-bc = \pm 1$ ensures precisely that $i$ is sent to some point in $H^2$ and hence $H^2$ is preserved.

On the other hand, a transformation that preserves $H^2$ must preserve $\partial H^2 = \matR\cup \infty$ and it is easy to see that since the images of $0,1,\infty$ are real all the coefficients $a,b,c,d$ can be taken in $\matR$.
\end{proof}

The M\"obius transformations in $\Conf(H^2)$ form a subgroup of index two which is naturally isomorphic to
$$\PSLR = \SLR/_{\pm I}.$$

An ordered triple of distinct points in $\matR\cup \infty$ is \emph{positive} if they are oriented counterclockwise, like $0,1, \infty$.

\begin{ex} \label{triple:ex}
The group $\PSLR$ acts freely and transitively on positive triples of points in $\matR\cup \infty$. 
\end{ex}

Let $C\subset \matC$ be a circle or line orthogonal to $\matR$. The inversion or reflection along $C$ preserves $H^2$ and is hence an element of $\Conf(H^2)$.

\begin{prop} \label{H2:generate}
Inversions along circles and reflections along lines orthogonal to $\matR$ generate $\Conf(H^2)$.
\end{prop}
\begin{proof}
Composing reflections we obtain all horizontal translations $z \mapsto z+b$ with $b\in\matR$, composing inversions we obtain all dilations $z \mapsto \lambda z$ with $\lambda \in \matR^*$. These maps together with the inversion $z \mapsto \frac {1}{\bar z}$ act transitively on positive triples of points in $\matR\cup \infty$.
\end{proof}

\begin{ex}
The inversion sending $H^2$ to $D^2$ is 
\begin{equation*} \label{anti:eq}
z \mapsto \frac{\bar z+i}{i\bar z+1}.
\end{equation*}
\end{ex}


\subsection{Isometries of $H^2$}
After this short detour on M\"obius transformations, we turn back to our hyperbolic spaces. We can characterise the isometry group of $H^2$. 
\begin{prop} \label{H2:prop}
We have $\Iso(H^2) = \Conf(H^2)$.
\end{prop}
\begin{proof}
Both groups are generated by inversions along circles and reflections along lines orthogonal to $\partial H^2 = \matR$ by Propositions \ref{generate:Hn:prop} and \ref{H2:generate}.
\end{proof}

In particular we have
$$\Iso^+(H^2) = \PSLR.$$
We will henceforth identify these two groups.
The trace of an element in $\PSLR$ is well-defined up to sign and carries some relevant information:
\begin{prop} \label{PSLR:prop}
A non-trivial isometry $A\in \PSLR$ is elliptic, parabolic, hyperbolic $\Longleftrightarrow$ respectively $|\tr A|<2$, $|\tr A|=2$, $|\tr A|>2$.
\end{prop}
\begin{proof}
Take $A=\big(\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\big)$ with $\det A = ad-bc = 1$. The M\"obius transformation $z\mapsto \frac {az+b}{cz+d}$ has a fixed point $z\in\matC$ if and only if
$$\frac{az+b}{cz+d} = z \Longleftrightarrow cz^2+(d-a)z-b = 0.$$
We find
$$\Delta = (d-a)^2 +4bc = (d+a)^2 - 4 = \tr^2 A - 4.$$
There is a fixed point in $H^2$ if and only if $\Delta <0$; if $\Delta > 0$ we find two fixed points in $\matR\cup\{\infty\}$ and if $\Delta = 0$ only one.
\end{proof}


\subsection{Isometries of $H^3$}
We have proved that $\Iso^+(H^2) = \PSLR$. Quite surprisingly, the isometry group $\Iso^+(H^3)$ is also isomorphic to a group of $2\times 2$ matrices! To prove this, we make the following identifications:
$$\matR^3 = \matC \times \matR = \{(z,t)\ |\ z\in\matC, t\in\matR\}$$
hence $H^3 = \{(z,t)\ |\ t >0\}$.
We also write $\matC$ for $\matC \times \{0\}$. The boundary trace of an isometry of $H^3$ is a homeomorphism of the Riemann sphere
$$\partial H^3 = \matC \cup\{\infty\} = S.$$
\begin{prop} \label{H3:prop}
The boundary trace induces an identification
$$\Iso(H^3) = \Conf(S).$$
\end{prop}
\begin{proof}
The group $\Iso(H^3)$ is generated by inversions along spheres and reflections along planes orthogonal to $\partial H^3$. Their traces are inversions along circles and reflections along lines in $S$. These generate $\Conf(S)$.
\end{proof}
In particular we have
$$ \Iso^+(H^3) = \PSLC.$$
We will also henceforth identify these two groups. As above, the trace of an element in $\PSLC$ is well-defined up to sign and carries some information:
\begin{prop}
A non-trivial isometry $A\in \PSLC$ is elliptic, parabolic, hyperbolic if and only if respectively $\tr A\in (-2,2)$, $\tr A=\pm 2$, $\tr A\in\matC \setminus [-2,2]$.
\end{prop}
\begin{proof}
Every non-trivial matrix $A\in\SLC$ is conjugate to one of:
$$\pm\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \quad 
\begin{pmatrix} \lambda & 0 \\ 0 & \lambda^{-1} \end{pmatrix} $$
for some $\lambda \in \matC^*$, and these represent the following isometries:
$$(z,t) \longmapsto (z + 1,t), \quad (z,t) \longmapsto (\lambda^2 z, |\lambda|^2 t).$$
In the first case $\tr A = \pm 2$ and $A$ is parabolic with fixed point $\infty$, in the second case $A$ has a fixed point in $H^3$ if and only if $|\lambda|=1$, \emph{i.e.}~$\tr A = \lambda + \lambda^{-1}\in (-2,2)$, the fixed point being $(0,1)$. If $|\lambda|\neq 1$ there are two fixed points $0$ and $\infty$ at infinity and hence $A$ is hyperbolic.
\end{proof}

Summing up, we have
$$\Iso^+(H^2) = \PSLR, \qquad \Iso^+(H^3) = \PSLC.$$
The group $\PSLR$ acts directly on $H^2$, while $\PSLC$ acts on the boundary sphere of $H^3$.
