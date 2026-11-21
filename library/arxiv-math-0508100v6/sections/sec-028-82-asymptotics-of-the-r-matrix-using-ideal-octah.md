---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-028-82-asymptotics-of-the-r-matrix-using-ideal-octah
section_title: "Asymptotics of the R-matrix using ideal octahedra"
section_number: 8.2
pages: 19-21
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.953
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.assRv8}

Since the entries of the $R$-matrix are given by ratios of five quantum
factorials (see Equations \eqref{eq.R+-}), Proposition \ref{lem.1}
gives a formula for the asymptotic behavior of the entries of the
$R$-matrix when evaluated at $e^{2 \pi i/n}$.
This is the content of the next proposition.



\begin{proposition}
\lbl{prop.R+limit}
{\rm (a)}
Suppose that $\a,\b,\k$ are real numbers that satisfy the inequalities
\begin{equation}
\lbl{eq.abk}
\a,\b,\k \in [0,1] \qquad
0 \leq \b+\k \leq 1, \qquad 0 \leq \a-\k \leq 1.
\end{equation}
Then the following limit exists
\begin{equation}
\lbl{eq.r+}
r_+(\a,\b,\k) :=
\lim_{n\to \infty}
\frac{1}{n} \, \log |\ev_n(R_+(n; \lfloor n\a \rfloor,
\lfloor n\b \rfloor,\lfloor n\k \rfloor ))|,
\end{equation}
and is equal to
\begin{equation}
\lbl{eq.r+equal}
r_+(\a,\b,\k)= [-\La(\pi(\b+\k)) +
\La(\pi\b)+\La(\pi\k)-\La(\pi\a)+\La(\pi(\a-\k))]/\pi.
\end{equation}
{\rm (b)} $r_+(\a,\b,\k)$ equals to $1/(2\pi)$ times the volume
of an ideal octahedron with vertices
\begin{equation}
\lbl{eq.vert8}
(0,1,\infty,z_{\kappa},(z_{\b}z_{\kappa}-1)/(z_{\b}-1),z_{\a}) \in
(\BC\setminus\{0,1\})^6
\end{equation}
where
$(z_{\a},z_{\b},z_{\kappa})=(e^{2 \pi i \a},e^{2 \pi i \b}, e^{2 \pi i \kappa})$.
\newline
{\rm (c)} Suppose that $\a,\b,\k$ are real numbers that satisfy:
\begin{equation*}
 \a,\b,\k \in [0,1] \qquad 0 \leq \a+\k \leq 1, \qquad 0
\leq \b-\k \leq 1.
\end{equation*}
Then the following limit exists
$$
r_-(\a,\b,\k) := \lim_{n\to \infty}
\frac{1}{n}\, \log |\ev_n(R_-(n; \lfloor n\a \rfloor,
\lfloor n\b \rfloor,\lfloor n\k \rfloor ))|.
$$
and is equal to
\begin{equation}
\lbl{62}
r_-(\a,\b,\k) = r_+(\b,\a,\k).
\end{equation}
\end{proposition}


\begin{proof}
(a) Observe that
$$
|\ev_n(\{j\})| = |\ev_n(\{n-j\})|= 2 \sin (j \pi/n), \quad
\text{and } |\ev_n(\{n-1\}!)| =  \prod_{j=1}^{n-1} 2\sin (j\pi/n)
=n.
$$

From these, we have that

\begin{equation}
\lbl{61}
|\ev_n(\{j\}!)| = \frac{n}{|\ev_n(\{n-1-j\}!)|}. 
\end{equation}

Using \eqref{eq.R+-} and then \eqref{61}, we have

\begin{equation}\begin{aligned}
 |\ev_n(R_+(n;a,b,k ))|
&= \frac{|\ev_n(\{b+k\}!)|\, |\ev_n(\{n-1+k-a\}!)|  }{ |\ev_n(\{b\}!)|\,
 |\ev_n(\{k\}!)|\,
 |\ev_n(\{n-1-a\}!)|}\\
&=\frac{|\ev_n(\{b+k\}!)| \,|\ev_n(\{a\}!)|  }{ |\ev_n(\{b\}!)|\,
|\ev_n(\{k\}!)|\,
 |\ev_n(\{a-k\}!)|}
 \end{aligned}
 \label{90}
 \end{equation}

Proposition \ref{lem.1} concludes the proof of (a).
(b) was pointed out to us by D. Thurston. Although this fact is not used
in the proof of Proposition \ref{prop.R} nor in the proof of Theorem
\ref{thm.4}, it is an interesting geometric fact. To prove it, recall that
the boundary of 3-dimensional hyperbolic space is $\BC \cup\{\infty\}$.
Let $T_z$ denote the {\em regular ideal tetrahedron} of shape
$z \in \BC-\{0,1\}$. $T_z$ is isometric to the ideal tetrahedron with
ordered vertices
at $0,1,\infty$ and $z$ in the boundary of 3-dimensional hyperbolic space.
For $z \in \BC\setminus\{0,1\}$, the ideal octahedron $T_z$ is isometric
to $T_{1/(1-z)}$ and $T_{z/(z-1)}$ by an orientation-preserving isometry,
and isometric to $T_{1/z}$, $T_{(1-z)/z}$ and $T_{(z-1)/z}$ by an orientation-reversing
isometry. Thus, when $z  \in \BC\setminus\{0,1\}$, we have:
\begin{equation}
\lbl{eq.Tzorbit}
\vol(T_z)=\vol(T_{1/(1-z)})=\vol(T_{z/(z-1)})=-\vol(T_{1/z})=-\vol(T_{(1-z)/z})=
-\vol(T_{(z-1)/z})
\end{equation}
The shape of the ideal tetrahedron
with distinct ordered vertices $(z_0,z_1,z_2,z_3)$ in $\BC\cup\{\infty\}$
is given by the {\em cross-ratio}
\begin{equation}
\lbl{eq.CR}
[z_0:z_1:z_2:z_3]=\frac{(z_0-z_3)(z_1-z_2)}{(z_0-z_2)(z_1-z_3)}
\end{equation}
following the convention of \cite[Eqn.1.4]{DZ}.
If $(\a_1,\a_2,\a_3)$ denote the three dihedral angles of $T_z$ at opposite pairs
of edges, then the volume $\vol(T_z)$ is given by \cite[Thm.10.4.10]{Ra}
$$
\vol(T_z)=\La(\a_1)+\La(\a_2)+\La(\a_3)
$$
If the shape parameter $z=e^{i \th}$ is a complex number of magnitude $1$,
then the dihedral angles of $T_z$ coincide with the angles
of an isosceles triangle with angles $(\th,(\pi-\th)/2,(\pi-\th)/2)$.
In that case, we have
$$
\vol(T_{e^{i \th}})=\La\left(\th\right)+
\La\left(\frac{\pi-\th}{2}\right)+\La\left(\frac{\pi-\th}{2}\right).
$$
The following symmetries of the Lobachevsky function
\cite[Thm.10.4.3,10.4.4]{Ra}
$$
\La(-\th)=-\La(\th), \qquad \frac{1}{2} \La(2\th)=\La(\th)
+\La\left(\th+\frac{\pi}{2}\right)
$$
imply that
\begin{equation}
\lbl{eq.Tzth}
\vol(T_{e^{i \th}})=2 \La\left(\frac{\th}{2}\right).
\end{equation}
Now, we return to the proof of part (b). Fix $\a,\b,\kappa$ as in
\eqref{eq.abk} and consider the complex numbers of magnitude $1$:
$$
(z_{\a},z_{\b},z_{\kappa})=(e^{2 \pi i \a},e^{2 \pi i \b}, e^{2 \pi i \kappa})
$$
Consider five ideal tetrahedra with shapes
\begin{equation}
\lbl{eq.5shapes}
(z_{\b}z_{\kappa})^{-1}, \quad z_{\b}, \quad z_{\kappa}, \quad
z_{\a}^{-1}, \quad z_{\a}z_{\kappa}^{-1}
\end{equation}
Equations \eqref{eq.r+equal} and \eqref{eq.Tzth} implies that the sum of
their volumes is given by $2 \pi \, r_+(\a,\b,\kappa)$. Now consider the
ideal octahedron with vertices
$$
(A,B,C,D,E,F)=(0,1,\infty,z_{\kappa},(z_{\b}z_{\kappa}-1)/(z_{\b}-1),z_{\a})
$$
drawn as follows:
$$
\psdraw{octahedron}{1in}
$$
It can be triangulated into five ideal tetrahedra
$ABDE$, $BDCE$, $ABCD$, $ABCF$ and $ACDF$ with ordered vertices and
with shape parameters
$$
\left\{1 - \frac{1}{z_{\b} z_{\kappa}}, \frac{z_{\b}}{z_{\b}-1}, \frac{z_{\kappa}}{z_{\kappa}-1}, \frac{z_{\a}}{z_{\a}-1},
\frac{z_{\a}}{z_{\kappa}} \right\}
$$

computed according to Equation \eqref{eq.CR}. Adding up the volumes
of these tetrahedra, with proper orientations concludes the proof of (b).
(c) is analogous to (a). We thank the referee for correcting the vertices
of the octahedron in an earlier version of this paper.
\end{proof}
