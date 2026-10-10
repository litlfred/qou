---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-008-5-invariance-under-the-choice-of-quad
section_title: "Invariance under the choice of quad"
section_number: 5
pages: 19-23
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.918
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further choices)"
---
\label{sec.quad}

The definition of the series $\Phi^\Xi(\hbar)$ requires some choices,
some of which were described and dealt with in the previous
Section~\ref{sec.elementary}. What remains to complete the proof of
Theorem~\ref{thm.1} is the independence of $\Phi^\Xi(\hbar)$
under the choice of a nondegenerate quad, and the independence
under the 2--3 Pachner moves that connect two ideal triangulations.

In this section, we will prove that $\Phi^\Xi(\hbar)$ is independent
of the choice of a nondegenerate quad. Recall that to each pair of opposite
edges of an ideal tetrahedron there is an associated variable
called a shape variable. When defining Neumann--Zagier data (see
Section~\ref{sub.NZ}), we must
choose an edge for each tetrahedron, which associates one of these shapes.
There are three possible choices, which leads to the action on $\BZ/3\BZ$ on
the each column of the Neumann--Zagier data. All in all, for a triangulation
with $N$ tetrahedra, this leads to $3^{N}$ choices on of Neumann--Zagier
data. On the other hand, the definition of the series $\Phi^{\Xi}(\hbar)$
requires a choice of a nondegenerate quad, i.e., one for which $\det(B) \neq 0$
(such quads always exist~\cite[Lem.A.3]{DG}). In this section, we will show
that any of the $3^N$ choices of quad with $\det(B) \neq 0$
lead to the same $\Phi^{\Xi}(\hbar)$ series.

\begin{theorem}
\label{thm.quadinvariance}  
The series $\Phi^{\Xi}(\hbar)$ is independent of the choice of a nondegenerate
quad. 
\end{theorem}

\begin{proof}
Fix two non--degenerate NZ data $\Xi=(A,B,\nu,z,f,f'')$ and 
$\widetilde{\Xi}=(\widetilde{A},\widetilde{B},\widetilde{\nu},\widetilde{z},
\widetilde{f},\widetilde{f}'')$ related by a quad change of the same ideal
triangulation. The nondegeneracy assumption implies that $\det(B) \neq 0$ and 
$\det(\widetilde{B})\neq0$. 

After reordering the tetrahedra (which does not change the $\Phi^\Xi(\hbar)$
series, as follows from Section~\ref{sec.elementary}), we can assume
that $\widetilde{\Xi}$ is obtained by applying a change in quad that fixes
the first $N_0$ shapes $z^{(0)}$, replaces the next $N_1$ shapes $z^{(1)}$
by $z'^{(1)}$ and replaces the next $N_2$ shapes $z^{(2)}$ by $z'^{(2)}$. (Recall
that $z'=1/(1-z)$ and $z''=1-1/z$).

\medskip

This partitions the shapes $z=(z^{(0)},z^{(1)},z^{(2)})$ into three sets of 
size $N_0,N_1,N_2$ and the matrices $A$ and $B$ into three block matrices
$A_i$ and $B_i$ of size $N \times N_i$ for $i=0,1,2$
\bea
A &\= (A_0\,|\,A_1\,|\,A_2)\,,\qquad
B &\= (B_0\,|\,B_1\,|\,B_2)\,,\qquad
\eea
and similarly for the flattening $f=(f^{(0)},f^{(1)},f^{(2)})$ and
$f''=(f''^{(0)},f''^{(1)},f''^{(2)})$. After the quad moves, the corresponding
matrices and vectors are given by
\bea
\tilde A &\= (A_0\,|-B_1\,|-A_2+B_2)\,,\quad
& &\tilde B & &\!\!\!=\; (B_0\,|\,A_1-B_1\,|-A_2)\,,\\
\tilde \nu &\= \nu - B_1  1 - A_2 1\,,\quad
& &\tilde z & &\!\!\!=\; 
(z^{(0)},z'^{(1)},z''^{(2)})\,,\\
\tilde f &\= (f^{(0)},1-f^{(1)}-f''^{(1)},f''^{(2)})\,,\quad
& &\tilde f'' & &\!\!\!=\; 
(f''^{(0)},f^{(2)},1-f^{(2)}-f''^{(2)})\,.
\eea
We also partition the vector of formal Gaussian integration variables
$x=(x^{(0)},x^{(1)},x^{(2)})$, as well as the symmetric matrix $Q:=B^{-1}A$
\be
Q\=
\begin{pmatrix}
Q_{00} & Q_{01} & Q_{02}\\
Q_{01}^t & Q_{11} & Q_{12}\\
Q_{02}^t & Q_{12}^t & Q_{22}\\
\end{pmatrix}\,.
\ee
With the above notation, we have
\be
\Phi^{\Xi}(\hbar) \= \langle I_0 \rangle_{x,\Lambda_0}
\ee
where
\[
I_0 \= \exp\Big(\frac\hbar8 f^t B^{-1} A f
-\frac{\hsqrt}2 x^t(B^{-1}\nu-1)\Big)
\prod_{j=1}^N \psi_{\hbar}(x_j,z_j)
\]
and
\begin{equation*}
\Lambda_0\=\diag(z')-Q \,.
\end{equation*}

Applying the first quad move as in Theorem~\ref{thm.fourier} to the $\psi_\hbar$
with arguments of $z^{(1)}$ and the second quad move as in its
Corollary~\ref{cor.fourier} to the $\psi_\hbar$ with arguments $z^{(2)}$, we obtain
that
\be
\Phi^{\Xi}(\hbar) \= \langle I_1 \rangle_{(x,y,w), \Lambda_1}
\ee
where
\begin{align*}
I_1 &\= 
\exp\Big(\frac\hbar8 f^t B^{-1} A f-\frac{\hsqrt}2{x^{(0)}}^t(B^{-1}\nu-1)^{(0)}
-
\frac{N_1\hbar}{24}
- \frac \hsqrt 2 {x^{(1)}}^t(B^{-1}\nu-1)^{(1)}\\
&\qquad\qquad\quad+ \sum_{j=1}^{N_1}
\Big(y_j+\frac{x_j^{(1)}z_j^{(1)}}{1-z_j^{(1)}}\Big)
\frac\hsqrt2
+
\frac{N_2\hbar}{24}
- \frac \hsqrt 2 {x^{(2)}}^t(B^{-1}\nu-1)^{(2)}
-\sum_{j=1}^{N_2}x_j^{(2)} \frac\hsqrt2\Big)\\
&\times\prod_{j=1}^{N_0} \psi_{\hbar}(x_j^{(0)},z_j^{(0)})
\prod_{j=1}^{N_1}\psi_{\hbar}\Big(y_j+\frac{x_j^{(1)}z_j^{(1)}}{1-z_j^{(1)}},
\frac1{1-z_j^{(1)}}\Big)
\prod_{j=1}^{N_2}
\psi_{\hbar}\Big(w_j - \frac{x_j^{(2)}}{1-z_j^{(2)}},1-{z_j^{(2)}}^{-1}\Big),
\end{align*}
$y$ and $w$ are vectors of size $N_1$ and $N_2$, respectively, and  
\[
\Lambda_1 \= 
\begin{pmatrix}
\Lambda & 0 & 0 \\
0 & \diag(z''^{(1)}) & 0 \\
0 & 0 & \diag(z^{(2)})-I
\end{pmatrix} \,.
\]
Making the change of variables
$y_j \mapsto y_j - \frac{x_j^{(1)}z_j^{(1)}}{1-z_j^{(1)}}$
and $w_j \mapsto w_j + \frac{x_j^{(2)}}{1-z_j^{(2)}}$ and using Lemma~\ref{lem.ff1}
we obtain that
\be
\Phi^{\Xi}(\hbar) \= \langle I_2 \rangle_{(x,y,w), \Lambda_2}
\ee
where
\begin{align*}
I_2 &\= \exp\Big(\frac\hbar8 f^t B^{-1} A f
-\frac{\hsqrt}2{x^{(0)}}^t(B^{-1}\nu-1)^{(0)}
-
\frac{N_1\hbar}{24}
- \frac \hsqrt 2 {x^{(1)}}^t(B^{-1}\nu-1)^{(1)}\\
&\qquad\qquad\quad+ y^{t}1\frac\hsqrt2
+
\frac{N_2\hbar}{24}
- \frac \hsqrt 2 {x^{(2)}}^t(B^{-1}\nu)^{(2)}
\Big)\\
&\qquad\qquad\times\prod_{j=1}^{N_0} \psi_{\hbar}(x_j^{(0)},z_j^{(0)})
\prod_{j=1}^{N_1}\psi_{\hbar}\Big(y_j,\frac1{1-z_j^{(1)}}\Big)
\prod_{j=1}^{N_2}
\psi_{\hbar}\big(w_j,1-{z_j^{(2)}}^{-1}\big)
\end{align*}
and
\[
\Lambda_2 \=
\left(\!\!
\def\arraystretch{1.25}
\begin{array}{ccc|cc}
\diag(z'^{(0)}) - Q_{00}
& -Q_{01} & -Q_{02} & 0 & 0\\
-Q_{01}^t & I-Q_{11} & -Q_{12} & I & 0\\
-Q_{02}^t & -Q_{12}^t & -Q_{22} & 0 & -I\\
\hline
0 & I & 0 & \diag(z''^{(1)})& 0 \\
0 & 0 & -I & 0 & \diag(z^{(2)})-I
\end{array}
\!\!\right) \,.
\]
Note that $x^{(1)}$ and $x^{(2)}$ do not appear in the arguments of $\psi_\hbar$.
Moreover, since $BQ=A$, we see that
\be\label{eq.BBt}
B
\begin{pmatrix}
I & Q_{01} & Q_{02}\\
0 & Q_{11}-I & Q_{12}\\
0 & Q_{12}^{t} & Q_{22}
\end{pmatrix}
\begin{pmatrix}
I & 0 & 0\\
0 & I & 0\\
0 & 0 & -I
\end{pmatrix}
\=
(B_0\,|\,A_1-B_1\,|-A_2)
\=
\widetilde{B}\,,
\ee
which implies that
\be
\det
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}\neq0\,,
\quad\text{and}\quad
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}^{-1}
\=
\begin{pmatrix}
0 & I & 0\\
0 & 0 & -I\\
\end{pmatrix}
\widetilde{B}^{-1}B
\begin{pmatrix}
0 & 0\\
I & 0\\
0 & I
\end{pmatrix}\,.
\ee
Therefore, we can apply Fubini's Theorem (Lemma~\ref{lem.ff1}) with the
integration variables $x^{(1)},x^{(2)}$,





















and use Lemma~\ref{lem.quad.inv} and
the equality $Qf+f''=B^{-1}\nu$
to obtain that 
\be
\label{eq.qpf}
\Phi^{\Xi}(\hbar) \= e^{c\hbar}\langle I_3 \rangle_{\widetilde{x}, \Lambda_3}\,.
\ee
where $\widetilde{x}=(x^{(0)},y,w)$, $c\in\frac{1}{24}\BZ$
\begin{equation*}
I_3 \= \exp\Big(\frac\hbar8 \widetilde{f}^t \widetilde{B}^{-1}\widetilde{A}
\widetilde{f}
-\frac{\hsqrt}2 \widetilde{x}^t(\widetilde{B}^{-1}\widetilde{\nu}-1)\Big)
\prod_{j=1}^N \psi_{\hbar}(\widetilde{x}_j,\widetilde{z}_j)
\end{equation*}
and
\begin{equation*}
\Lambda_3\=\diag(\widetilde{z}')-\widetilde{B}^{-1}\widetilde{A}\,.
\end{equation*}
The right hand side of Equation~\eqref{eq.qpf} is exactly equal to
$e^{c\hbar}\Phi^{\widetilde{\Xi}}(\hbar)$, completing the proof of
Theorem~\ref{thm.quadinvariance}.
\end{proof}

\begin{lemma}
\label{lem.quad.inv}
With the notation as in the proof of Theorem~\ref{thm.quadinvariance}, we have
the following identities
\begin{align}
\label{eq.ABtildeq}
\widetilde{B}^{-1}\widetilde{A}
&\=
\begin{pmatrix}
Q_{00} & 0 & 0\\
0 & 0 & 0 \\
0 & 0 & -I
\end{pmatrix}
+
\begin{pmatrix}
Q_{01} & Q_{02}\\
-I & 0 \\
0 & I
\end{pmatrix}
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}^{-1}
\begin{pmatrix}
Q_{01}^t & -I & 0 \\
Q_{02}^t & 0 & I
\end{pmatrix},\\
\widetilde{B}^{-1}\widetilde{\nu}-1
&\=
\begin{pmatrix}
I & 0 & 0\\
0 & 0 & 0\\
0 & 0 & 0
\end{pmatrix}(B^{-1}\nu-1)
-\begin{pmatrix}0\\ 1 \\ 0\end{pmatrix}\notag\\
&\qquad+\begin{pmatrix}
-Q_{01} & -Q_{02}\\
I & 0 \\
0 & -I
\end{pmatrix}
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}^{-1}\left(\begin{pmatrix}0 & I & 0\\0 & 0 & I \end{pmatrix}B^{-1}\nu
-\begin{pmatrix}1 \\ 0\end{pmatrix}\right)\label{eq.Bvtildeq}
\end{align}
and for some $d\in\BZ$
\be\label{eq.fftildeq}
\begin{aligned}
&\widetilde{f}\widetilde{B}^{-1}\widetilde{\nu}
\=
f^tB^{-1}\nu+d\\
&-\Big((B^{-1}\nu)^t\begin{pmatrix}
0 & 0\\
I & 0\\
0 & I
\end{pmatrix}
-\begin{pmatrix}1 & 0\end{pmatrix}
\Big)
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}^{-1}
\left(\begin{pmatrix}0 & I & 0\\0 & 0 & I \end{pmatrix}B^{-1}\nu
-\begin{pmatrix}1 \\ 0\end{pmatrix}\right).
\end{aligned}
\ee
\end{lemma}

\begin{proof}
We will show that boths sides of Equation~\eqref{eq.ABtildeq} and
Equation~\eqref{eq.Bvtildeq} are equal after multiplying by the invertible
matrix $\widetilde{B}$. Denote
\be
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}^{-1}
\=
\begin{pmatrix}
\Gamma_{11} & \Gamma_{12}\\
\Gamma_{12}^{t} & \Gamma_{22}
\end{pmatrix}\,,
\ee
and note that
\be\label{eq.qlq}
\begin{tiny}
\begin{aligned}
&
\widetilde{B}
\begin{pmatrix}
-Q_{01} & -Q_{02}\\
I & 0 \\
0 & -I
\end{pmatrix}
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}^{-1}
\=
\widetilde{B}
\begin{pmatrix}
  -Q_{01}\Gamma_{11}-Q_{02}\Gamma_{12}^t
  &-Q_{01}\Gamma_{12}-Q_{02}\Gamma_{22}\\
  \Gamma_{11} & \Gamma_{12}\\
  -\Gamma_{12}^{t} &-\Gamma_{22}
\end{pmatrix}\\
&\=
(
-B_{0}Q_{01}\Gamma_{11}-B_0Q_{02}\Gamma_{12}^t+(A_1-B_1)\Gamma_{11}+A_2\Gamma_{12}^{t}
\;|\;-B_0Q_{01}\Gamma_{12}-B_0Q_{02}\Gamma_{22}+(A_1-B_1)\Gamma_{12}+A_2\Gamma_{22}
)
\\
&\=
(
(B_1(Q_{11}-I)+B_2Q_{12}^t)\Gamma_{11}+(B_1Q_{12}+B_2Q_{22})\Gamma_{12}^t
\;|\;(B_1(Q_{11}-I)+B_2Q_{12}^t)\Gamma_{12}+(B_1Q_{12}+B_2Q_{22})\Gamma_{22}
)
\\
&\=
(
B_1\;|\;B_2
)\,.
\end{aligned}
\end{tiny}
\ee
Therefore, since
\be
\widetilde{B}
\begin{pmatrix}
Q_{00} & 0 & 0\\
0 & 0 & 0 \\
0 & 0 & -I
\end{pmatrix}
\=(B_0Q_{00}\;|\;0\;|-A_2)\,,
\ee
we see that multiplying the right hand side of
Equations~\eqref{eq.ABtildeq} on the left by $\widetilde{B}$ we have
\be
  (B_0Q_{00}+B_1Q_{01}^t+B_{2}Q_{02}^t\;|-B_1\;|-A_2+B_2)
  \=\widetilde{A}\,,
\ee
which completes the proof of Equation~\eqref{eq.ABtildeq}.
Similarly, since
\be
\widetilde{B}
\begin{pmatrix}
I & 0 & 0\\
0 & 0 & 0\\
0 & 0 & 0
\end{pmatrix}(B^{-1}\nu-1)
-\widetilde{B}\begin{pmatrix}0\\ 1 \\ 0\end{pmatrix}
\=
B_0(B^{-1}\nu)^{(0)}-B_01
-A_11+B_11
\ee
we see that multiplying the right hand side of
Equations~\eqref{eq.Bvtildeq} on the left by $\widetilde{B}$ we have
\be
  B_0(B^{-1}\nu)^{(0)}-B_01
  -A_11+B_11
  +B_1(B^{-1}\nu)^{(1)}-B_11
  +B_2(B^{-1}\nu)^{(2)}
  \=\widetilde{\nu}-\widetilde{B}1\,,
\ee
which completes the proof of Equation~\eqref{eq.Bvtildeq}.
For Equation~\eqref{eq.fftildeq}, we will compute the three terms that appear there.
Firstly, use Equation~\eqref{eq.Bvtildeq} to obtain that
\be
\begin{pmatrix}
0 & I & 0\\
0 & 0 & -I
\end{pmatrix}
(\widetilde{B}^{-1}\widetilde{\nu}-1)
\=
-\begin{pmatrix}
1\\0
\end{pmatrix}
+
\begin{pmatrix}
Q_{11}-I & Q_{12}\\
Q_{12}^{t} & Q_{22}
\end{pmatrix}^{-1}\left(\begin{pmatrix}0 & I & 0\\0 & 0 & I \end{pmatrix}B^{-1}\nu
-\begin{pmatrix}1 \\ 0\end{pmatrix}\right),
\ee
to obtain that
\be\label{eq.lem.qinter}
\begin{aligned}
&\left((B^{-1}\nu)^t\begin{pmatrix}
0 & 0\\
I & 0\\
0 & I
\end{pmatrix}
-\begin{pmatrix}1 & 0\end{pmatrix}
\right)
\left(
\begin{pmatrix}
0 & I & 0\\
0 & 0 & -I
\end{pmatrix}
(\widetilde{B}^{-1}\widetilde{\nu}-1)+\begin{pmatrix}1 \\ 0\end{pmatrix}
\right)\\
&\=
({(B^{-1}\nu)^{(1)}}^t-1)
(\widetilde{B}^{-1}\widetilde{\nu})^{(1)}
-{(B^{-1}\nu)^{(2)}}^t
(\widetilde{B}^{-1}\widetilde{\nu})^{(2)}+{(B^{-1}\nu)^{(2)}}^t1\,.
\end{aligned}
\ee
Secondly, expanding out
\be
\begin{aligned}
\widetilde{f}^t\widetilde{B}^{-1}\widetilde{\nu}
&\=
f^{(0)}(\widetilde{B}^{-1}\widetilde{\nu})^{(0)}
+(1-f^{(1)}-f''^{(1)})(\widetilde{B}^{-1}\widetilde{\nu})^{(1)}
+f''^{(2)}(\widetilde{B}^{-1}\widetilde{\nu})^{(2)}\\
&\=
f^{(0)}(\widetilde{B}^{-1}\widetilde{\nu})^{(0)}\\
&\qquad+(1-f^{(1)}-{(B^{-1}\nu)^{(1)}}^t+f^{(0)}Q_{01}+f^{(1)}Q_{11}+f^{(2)}Q_{12}^t)
(\widetilde{B}^{-1}\widetilde{\nu})^{(1)}\\
&\qquad+({(B^{-1}\nu)^{(2)}}^t-f^{(0)}Q_{02}-f^{(1)}Q_{12}-f^{(2)}Q_{22})
(\widetilde{B}^{-1}\widetilde{\nu})^{(2)}\,.
\end{aligned}
\ee
Finally, using Equation~\eqref{eq.BBt} we obtain that
\be
\begin{aligned}
f^tB^{-1}\nu
-f^{(1)}1
+f''^{(2)}1
&\=
f^tB^{-1}\nu
-f^{(1)}1
-f^{t}Q(0,0,1)^t
+{(B^{-1}\nu)^{(2)}}^t1\\
&\=f^tB^{-1}\widetilde{\nu}+{(B^{-1}\nu)^{(2)}}^t1\\
&\=
f^{(0)}(\widetilde{B}^{-1}\widetilde{\nu})^{(0)}\\
&\qquad+(f^{(0)}Q_{01}+f^{(1)}(Q_{11}-I)+f^{(2)}Q_{12}^t)
(\widetilde{B}^{-1}\widetilde{\nu})^{(1)}\\
&\qquad-(f^{(0)}Q_{02}+f^{(1)}Q_{12}+f^{(2)}Q_{22})
(\widetilde{B}^{-1}\widetilde{\nu})^{(2)}
+{(B^{-1}\nu)^{(2)}}^t1\,.
\end{aligned}
\ee
\end{proof}
