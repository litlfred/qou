---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-003-13-the-case-of-the-41-knot
section_title: "The case of the 41 knot"
section_number: 1.3
pages: 4-5
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.771
latex_coverage_ratio: 0.915
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integrals of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topology can be written"
---
\lbl{sub.41}

We now specialize Corollary \ref{cor.1} to the invariant of the 
$4_1$ and $5_2$ knots is given by \cite{KLV,AK} 
$$
\calI_{1,2}=\calI_{4_1} \qquad \calI_{2,3}=\calI_{5_2} \,.
$$
In this section, let 
\begin{equation}
\lbl{eq.Fqx}
F(q,x)=F_{1,2}(q,x)= \sum_{n=0}^\infty 
(-1)^n \frac{q^{\frac{1}{2} n(n+1)}}{(q)_n^2} x^n \,.
\end{equation}

\begin{corollary}
\lbl{cor.41}
\rm{(a)} We have:
\begin{equation}
\lbl{eq.prop1}
\calI_{4_1}(b) = -\frac{i}{2} \left(\frac{q}{\tq}\right)^{\frac{1}{24}}
\left( b \, G(q) g(\tq) - b^{-1} G(\tq) g(q) \right)
\end{equation}
where
\begin{subequations}
\begin{align}
\lbl{eq.g}
g(q) &= \sum_{n=0}^\infty (-1)^n \frac{q^{\frac{1}{2} n(n+1)}}{(q)_n^2}
\\
\lbl{eq.G}
G(q) &=\sum_{m=0}^\infty \left(1 + 2m -4 
\sum_{s=1}^\infty \frac{q^{s(m+1)}}{1-q^s} \right) 
(-1)^m \frac{q^{\frac{1}{2} m(m+1)}}{(q)_m^2}
\end{align}
\end{subequations}
\rm{(b)} The series $g(q)$ and $G(q)$ are given in terms of $F(q,x)$
by:
\begin{subequations}
\begin{align}
\lbl{eq.gF}
g(q) &= \la F \ra \\
\lbl{eq.GF}
G(q) &= \la (2 + 2 \d -4 \d_1)F \ra


\end{align}
\end{subequations}
\rm{(c)} $F$ satisfies the linear $q$-difference equation
\begin{equation}
\lbl{eq.Frec}
F(q,q^{-1}x)+F(q,qx)=(2-x) F(q,x)
\end{equation}
\end{corollary}

The series $g(q)$ that appears in Theorem \ref{cor.41} was known to
the first author and Zagier to be closely related to the $4_1$ knot. 
For a detailed discussion of experimental facts below, see \cite{GZ2}.
Empirically, it appears that
\begin{itemize}
\item
the pair $(g(q),G(q))$ is related to the 3D index of the $4_1$ knot, 
\item
the radial asymptotics of the pair $(g(q),G(q))$ are related to
the asymptotics of the Kashaev invariant of the $4_1$ knot, 
\item
the above observations for $4_1$ also hold for the case of $5_2$ knot
discussed below.
\end{itemize}
Recall that the index of an ideal triangulation was introduced in 
\cite{DGG1,DGG2}, necessary and sufficient conditions for its
convergence was established in \cite{Ga:index} and its topological invariance
was proven in \cite{GHRS}. For a detailed discussion of the above
experimental facts, see \cite{GZ2}.



\subsection{The case of the $5_2$ knot}
\lbl{sub.52}

In this section, let
$$
F(q,x)=F_{2,3}(q,x)=\sum_{m=0}^\infty t_m(q) x^m, 
\qquad 
\ti F(q,\ti x)=F_{1,3}(q,\ti x)=\sum_{m=0}^\infty T_m(q) \ti x^m
$$
where
$$
t_m(q)=
\frac{q^{m(m+1)}}{(q)^3_m}, \qquad
T_n(q)=(-1)^n
\frac{q^{\frac{1}{2}n(n+1)}}{(q)^3_n} = t_n(q^{-1}) \,.
$$
Let
{\small
\begin{align*}
R_{m,n}(q,\tq) &= -\frac{b^2}{2} \left(
1 + 4 m + 4 m^2   - 6 E^{(m)}_1(q) - 12 m  E^{(m)}_1(q) + 9 E^{(m)2}_1(q) - 3 
E^{(m)}_2(q) \right)
\\
& - \frac{1}{2 \pi i} +  \frac{1}{2}
\left(1 + 2 m - 3 E^{(m)}_1(q)\right)\left(1 + 2 n -6 E^{(n)}_1(\tq)\right) 
\\
& + \frac{b^{-2}}{2} \left( - n - n^2 -6 E^{(0)}_2(\tq) + 3 E^{(n)}_1(\tq) 
+6 n E^{(n)}_1(\tq) - 9 E^{(n)2}_1(\tq) + 3 E^{(n)}_2(\tq) \right) \,,
\end{align*}
}
where $E^{(m)}_l(q)$ are defined in Equation \eqref{eq.Elm}.
For $k=1,\dots,4$ let
\begin{equation}
\lbl{eq.gG52}
g_k(q)=\sum_{m=0}^\infty p_k(m) t_m(q), \qquad 
G_k(\tq)=\sum_{n=0}^\infty P_k(n) T_n(\tq) \,,
\end{equation}
where
{\small
\begin{subequations}
\begin{align}
\lbl{eq.g1}
p_{1,m}(q) &=
1 + 4 m + 4 m^2  -6 E^{(m)}_1(q) - 12 m E^{(m)}_1(q)
+ 9 E^{(m)2}_1(q) - 3 E^{(m)}_2(q) 
\\
\lbl{eq.gg2}
p_{2,m}(q) &= 1 + 2 m - 3 E^{(m)}_1(q)
\\
\lbl{eq.g3}
p_{3,m}(q) &= 1 
\end{align}
\end{subequations}
}
and
{\small
\begin{subequations}
\begin{align}
\lbl{eq.G1}
P_{1,m}(q) &= 1
\\
\lbl{eq.G2}
P_{2,m}(q) &= 1 + 2 n -6 E^{(n)}_1(\tq)
\\
\lbl{eq.G3}
P_{3,m}(q) &= - n - n^2 -6 E^{(0)}_2(\tq) + 3 E^{(n)}_1(\tq) 
+6 n E^{(n)}_1(\tq) - 9 E^{(n)2}_1(\tq) + 3 E^{(n)}_2(\tq) \,.
\end{align}
\end{subequations}
}

\begin{corollary}
\lbl{cor.52}
\rm{(a)} We have:
\begin{align}
\lbl{eq.52}
\calI_{2,3}(q)& = 
-e^{\frac{3 \pi i}{4}} 
\left(\frac{q}{\tq}\right)^{\frac{1}{8}} 
\sum_{m,n=0}^\infty  R_{m,n}(q,\tq) t_m(q) T_n(\tq) \\ \notag
& = -e^{\frac{3 \pi i}{4}} 
\left(\frac{q}{\tq}\right)^{\frac{1}{8}} 
\left(
-\frac{b^2}{2} g_1(q) G_1(\tq) -\frac{1}{2 \pi i}
g_3(q) G_1(\tq) +\frac{1}{2} g_2(q) G_2(\tq) 
+ \frac{b^{-2}}{2} g_3(q) G_3(\tq) \right)
\end{align}

\begin{subequations}
\rm{(b)} $F$ and $\ti F$ satisfy the linear $q$-difference equations
\begin{equation*}
\lbl{eq.F52rec}
F(q,q^3x) - (3 - q^2 x) F(q,q^2x) + 3 F(q,qx) - F(q,x) =0 
\end{equation*}
\begin{equation*}
\lbl{eq.tF52rec}
\ti F(q,q^3x) - 3 \ti F(q,q^2x) + (3 - q^2 x)  \ti F(q,qx) - \ti F(q,x) =0 \,.
\end{equation*}
\end{subequations}
\end{corollary}


\begin{remark}
\lbl{eq.41.52}
A computation gives that $P(A,B)=P(B-A,B)$ for $(A,B)=(1,2)$ and 
$(A,B)=(2,3)$ corresponding to the invariants of the $4_1$ and $5_2$ knots.
In all other cases that we tried, we found that $P(A,B)$ is not equal
to $P(B-A,B)$.
\end{remark}
