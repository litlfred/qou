---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-072-131-volume-of-tetrahedra
section_title: "Volume of tetrahedra"
section_number: 13.1
pages: 413-418
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.983
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
\label{volume:tetrahedra:section}
The volume of an ideal hyperbolic tetrahedron is a simple (but integral) formula that involves the \emph{Lobachevsky function}: we now prove this formula here. As a consequence we show that the regular ideal tetrahedron is the hyperbolic tetrahedron with maximal volume.


\subsection{The Lobachevsky function}
The \emph{Lobachevsky function} is\index{Lobachevsky function}
$$\Lambda(\theta) = -\int_0^\theta \log |2\sin t| dt.$$
The function $\log |2\sin t|$ is $-\infty$ on $\pi\matZ$ but is integrable, hence $\Lambda$ is well-defined and continuous on $\matR$. Its first derivatives are
$$\Lambda'(\theta) = -\log |2\sin \theta |, \qquad \Lambda''(\theta) = -\cot \theta.$$
The function $\Lambda$ has derivative $+\infty$ on $\pi\matZ$ and is an odd function, because its derivative is even. 

\begin{prop} \label{Loba:prop}
The function $\Lambda$ is $\pi$-periodic. We have $\Lambda (0) = \Lambda \left(\frac \pi 2 \right) = \Lambda (\pi) = 0$. The function $\Lambda$ is strictly positive on $\left(0,\frac \pi 2 \right)$, strictly negative on $\left(\frac \pi 2, \pi\right)$, and has absolute maximum and minimum at $\frac \pi 6 $ and $\frac 56 \pi$.
For all $m\in \matN$ the following holds:
$$\Lambda(m\theta) = m \sum_{k=0}^{m-1} \Lambda\left(\theta + \frac{k\pi}m\right).$$
\end{prop}
\begin{proof}
We prove the equality for $m=2$:
\begin{align*}
\frac{\Lambda(2\theta)}2 & = -\frac 12\int_0^{2\theta} \log |2\sin t|dt = - \int_0^\theta \log |2\sin 2t| dt \\
 & = - \int_0^\theta \log |2\sin t| dt - \int_0^\theta \log \left|2\sin \left(t+\frac \pi 2 \right) \right| dt \\
 & = \Lambda(\theta) - \int_{\frac \pi 2}^{\frac \pi 2 + \theta} \log |2 \sin t| dt \\
  & = \Lambda(\theta) + \Lambda\left(\theta + \frac \pi 2 \right) - \Lambda \left(\frac \pi 2 \right).
\end{align*}
By setting $\theta = \frac \pi 2$ we get $\Lambda(\pi)=0$. Since the derivative $\Lambda'$ is $\pi$-periodic and $\Lambda(\pi)=0$, also $\Lambda$ is $\pi$-periodic. Since $\Lambda$ is $\pi$-periodic and odd, we have $\Lambda \left(\frac \pi 2 \right) = 0$. We have also proved the formula for $m=2$.

To prove the formula for generic $m$ we use a generalisation of the duplication formula for the sinus. From the equality
$$z^m - 1 = \prod_{k=0}^{m-1} \left(z-e^{-\frac {2\pi ik}m}\right)$$
we deduce
$$2\sin(mt) = \prod_{k=0}^{m-1} 2\sin \left(t+\frac{k\pi}m\right)$$
and hence
\begin{align*}
\frac{\Lambda(m\theta)}m & = -\frac 1m \int_0^{m\theta} \log | 2\sin t| dt = - \int_0^\theta \log | 2 \sin (mt)| dt  \\
 & = - \sum_{k=0}^{m-1} \int_0^\theta \log \left|2 \sin \left( t + \frac {k \pi}m \right) \right| dt \\
 & = - \sum_{k=0}^{m-1} \left( \int_0^{\theta + \frac{k\pi}m} \log |2 \sin t| dt - \int_0^{\frac {k\pi}m} \log | 2\sin t | dt \right) \\
 & = - \sum_{k=0}^{m-1} \Lambda \left(\theta + \frac{k\pi}m \right) + C(m)
 \end{align*}
where $C(m)$ is a constant independent of $\theta$. By integrating both sides we get 
$$\frac 1m \int_0^\pi \Lambda(m\theta) = -\sum_{k=0}^{m-1}\int_0^\pi \Lambda\left(\theta + \frac{k\pi}m \right) + C(m)\pi.$$
Since $\Lambda$ is odd and $\pi$-periodic, we have
$$\int_0^\pi \Lambda (m\theta) = 0$$
for any integer $m$. Hence $C(m)=0$ and the formula is proved. Finally we note that $\Lambda''(\theta) = -\cot \theta $ is strictly negative in $(0,\frac \pi 2)$ and strictly positive in $(\frac \pi 2, \pi)$, hence $\Lambda$ is strictly positive in $(0, \frac \pi 2)$ and strictly negative in $(\frac \pi 2, \pi)$.
\end{proof}


\subsection{Volumes of ideal tetrahedra}
An ideal tetrahedron in $\matH^3$ is the convex hull of four non-planar ideal points. Quite surprisingly, every ideal tetrahedron has some non-trivial symmetries.\index{ideal tetrahedron} 

\begin{figure}
\begin{center}
\includegraphics[width = 4.5 cm] {\iftoggle{BW}{tetraedro4-BW}{tetraedro4}} 
\nota{Every pair of opposite edges in an ideal tetrahedron has an axis orthogonal to both which is a symmetry axis for the tetrahedron.}
\label{tetraedro4:fig}
\end{center}
\end{figure}

\begin{prop} \label{symmetries:ideal:tetrahedron:prop}
For any pair of opposite edges in an ideal tetrahedron $\Delta$ there is a unique line $r$ orthogonal to both as in Figure \ref{tetraedro4:fig} and $\Delta$ is symmetric with respect to a $\pi$-rotation around $r$.
\end{prop}
\begin{proof}
The opposite edges $e$ ed $e'$ are ultraparallel lines in $\matH^3$ and hence have a common perpendicular $r$. A $\pi$-rotation around $r$ inverts both $e$ and $e'$ but preserve the 4 ideal vertices of $\Delta$, hence $\Delta$ itself. 
\end{proof}


\begin{figure}
\begin{center}
\includegraphics[width = 10 cm] {\iftoggle{BW}{Loba-BW}{Loba}} 
\nota{The dihedral angles $\alpha, \beta, \gamma$ of an ideal tetrahedron. Opposite edges have the same angle and $\alpha+\beta+\gamma = \pi$ (left). To calculate the volume we use the half-space model, send a vertex to $\infty$, and divide the tetrahedron in six sub-tetrahedra (right).}
\label{Loba:fig}
\end{center}
\end{figure}

As a consequence, two opposite edges in $\Delta$ have coinciding dihedral angles as in Figure \ref{Loba:fig}-(left). Moreover, we have $\alpha + \beta + \gamma = \pi$ because a small horosphere based at a vertex intersects $\Delta$ into a Euclidean triangle with inner angles $\alpha, \beta$, and $\gamma$.
The regular ideal tetrahedron has of course equal angles $\alpha = \beta = \gamma = \frac \pi 3$.

\begin{teo} Let $\Delta$ be an ideal tetrahedron with dihedral angles $\alpha$, $\beta$ and $\gamma$. We have
$$\Vol(\Delta) = \Lambda(\alpha) + \Lambda(\beta) + \Lambda(\gamma).$$
\end{teo}
\begin{proof}
We represent $\Delta$ in the half-space model $H^3$ with one vertex $v_0$ at infinity and three vertices $v_1,v_2,v_3$ in $\matC$. Let $C$ be the circle containing $v_1$, $v_2$, and $v_3$: up to composing with elements in $\PSLC$ we can suppose that $C=S^1$. The Euclidean triangle $T\subset\matC$ with vertices $v_1$, $v_2$, and $v_3$ has interior angles $\alpha$, $\beta$, and $\gamma$. 

We first consider the case $0\in T$, that is $\alpha, \beta, \gamma \leqslant \frac \pi 2$. 
We decompose $T$ into six triangles as in Figure \ref{Loba:fig}: the tetrahedron $\Delta$ decomposes accordingly into six tetrahedra lying above them, and we prove that the one $\Delta_\alpha$ lying above the \iftoggle{BW}{light grey}{yellow} triangle has volume $\frac{\Lambda(\alpha)}2$. 
This proves the theorem.

The tetrahedron $\Delta_\alpha$ is the intersection of four half-spaces: three vertical ones bounded by the hyperplanes $y=0$, $x=\cos\alpha$, and $y=x\tan\alpha$, and one bounded by the half-sphere $z^2 = x^2+y^2$. Therefore
\begin{align*}
\Vol(\Delta_\alpha) & = \int_0^{\cos\alpha} dx \int_0^{x\tan \alpha} dy \int_{\sqrt{1-x^2-y^2}}^\infty \frac 1{z^3} dz \\
& = \int_0^{\cos\alpha} dx \int_0^{x\tan \alpha} dy \left[- \frac 1{2z^2} \right]_{\sqrt{1-x^2-y^2}}^\infty \\
& = \frac 12 \int_0^{\cos \alpha}dx \int_0^{x\tan\alpha}\frac 1{1-x^2-y^2}dy. 
\end{align*}
To solve this integral we use the relation 
$$\frac 1{1-x^2-y^2} = \frac 1{2\sqrt{1-x^2}} \left(\frac 1{\sqrt{1-x^2}-y} + \frac 1{\sqrt{1-x^2}+y}\right)$$
and hence $\Vol(\Delta_\alpha)$ equals
\begin{align*}
& \frac 14\int_0^{\cos\alpha} \!\!\!\!\!\! \frac {dx}{\sqrt{1-x^2}} 
\left(\left[-\log(\sqrt{1-x^2}-y)\right]_0^{x\tan \alpha} \!\!\!\!\! + \left[\log(\sqrt{1-x^2}+y)\right]_0^{x\tan\alpha}\right) \\
= & \frac 14 \int_0^{\cos\alpha} \!\!\!\!\! \frac{dx}{\sqrt{1-x^2}}
 \left(-\log(\sqrt{1-x^2}-x\tan\alpha)+\log(\sqrt{1-x^2}+x\tan\alpha)\right).
 \end{align*}
By writing $x=\cos t$ and hence $dx = -\sin t \, dt$ we obtain
\begin{align*} 
\Vol(\Delta_\alpha)  & = \frac 14 \int_{\frac\pi 2}^\alpha \frac{-\sin t}{\sin t} 
\left(-\log \frac{\sin t\cos\alpha - \cos t\sin \alpha}{\sin t \cos\alpha + \cos t \sin \alpha} \right) dt \\
 & = - \frac 14 \int_{\frac \pi 2}^\alpha \log \frac{\sin(t+\alpha)}{\sin(t-\alpha)}dt
 = - \frac 14 \int_{\frac \pi 2}^\alpha \log \frac{|2\sin(t+\alpha)|}{|2\sin(t-\alpha)|}dt \\
 & = \frac 14 \int_{2\alpha}^{\frac \pi 2+\alpha} \log | 2\sin t|dt - \frac 14 \int_0^{\frac \pi 2-\alpha} \log |2\sin t|dt \\
& = \frac 14\left(-\Lambda\left(\frac \pi 2 + \alpha \right) + \Lambda(2\alpha) + \Lambda\left(\frac \pi 2 - \alpha\right) \right) \\
& = \frac 14 \left(-\Lambda \left(\frac \pi 2 + \alpha \right) +2 \Lambda(\alpha) +2\Lambda\left(\frac \pi 2 + \alpha\right) - \Lambda\left(\frac \pi 2 + \alpha\right) \right) = \frac 12 \Lambda(\alpha)
\end{align*}
using Proposition \ref{Loba:prop}.

If $0\not \in T$ the triangle $T$ may be decomposed analogously into triangles, some of which contribute negatively to the volume, and we obtain the same formula.
\end{proof}

\begin{cor} \label{v3:cor}
The regular ideal tetrahedron is the hyperbolic tetrahedron of maximum volume.
\end{cor}
\begin{proof}
It is easy to prove that every hyperbolic tetrahedron is contained in an ideal tetrahedron: hence we may consider only ideal tetrahedra. Consider the triangle $T = \{0\leqslant \alpha, \beta, \alpha+\beta \leqslant \pi\}$ and 
\begin{align*}
f \colon \quad \ \ T & \longrightarrow  \matR \\ 
(\alpha, \beta) & \longmapsto \Lambda(\alpha) + \Lambda(\beta) + \Lambda(\pi-\alpha-\beta).
\end{align*}
The continuous function $f$ is null on $\partial T$ and strictly positive on the interior of $T$ because it measures the volume of the ideal tetrahedron of dihedral angles $\alpha, \beta, \gamma = \pi-\alpha-\beta$. Hence $f$ has at least a maximum on some interior point $(\alpha,\beta)$. The gradient 
$$
\nabla f = \begin{pmatrix}
\Lambda'(\alpha) - \Lambda'(\pi - \alpha-\beta) \\ \Lambda'(\beta) - \Lambda'(\pi-\alpha-\beta) 
\end{pmatrix}
 =
\begin{pmatrix}
-\log |2\sin \alpha| + \log |2\sin (\pi-\alpha-\beta)| \\ 
-\log |2\sin \beta| + \log |2\sin (\pi-\alpha-\beta) |
\end{pmatrix}
$$
must vanish there, and this holds if and only if $\sin\alpha = \sin (\pi-\alpha-\beta) = \sin \beta$, \emph{i.e.}~if and only if the tetrahedron has all dihedral angles equal to $\frac \pi 3$.
\end{proof}
