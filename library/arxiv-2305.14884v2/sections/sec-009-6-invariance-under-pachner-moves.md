---
doc_id: arxiv-2305.14884v2
doc_title: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS"
section_id: sec-009-6-invariance-under-pachner-moves
section_title: "Invariance under Pachner moves"
section_number: 6
pages: 23-25
source_pdf: 2305.14884v2.pdf
source_sha256: ebc8e64d901c9e4f
doc_brief: "PERTURBATIVE INVARIANTS OF CUSPED HYPERBOLIC 3-MANIFOLDS — We prove that a formal power series associated to an ideally triangu lated cusped hyperbolic 3-manifold (together with some further choices)"
text_source: latex
latex_prose_ratio: 0.763
latex_coverage_ratio: 1.0
---
\label{sec.pachner}

In this section, we will prove that $\Phi^{\Xi}$ is invariant under 2--3 Pachner
moves. There are several versions of the 2--3 move (and of the corresponding
pentagon identity in Teichm\"uller TQFT~\cite{Kashaev:beta}) and the
one we choose in the next theorem is slightly different from the one
in~\cite[Sec.3.6]{DG} and can be related by
composing with quad moves.

The 2--3 move involves two triangulations $\calT$ and $\widetilde\calT$ with $N+2$
and $N+3$ tetrahedra, respectively, shown in Figure~\ref{fig.23move}.

\begin{figure}[htpb!]
\begin{center}  

\begin{tikzpicture}[scale=0.6,baseline=-3]
\filldraw (2,3.5) circle (2pt);
\filldraw (0,0) circle (2pt);
\filldraw (4,1) circle (2pt);
\filldraw (0.5,2) circle (2pt);
\draw (0,0) -- (2,3.5);
\draw (0,0) -- (4,1);
\draw (0,0) -- (0.5,2);
\draw (4,1) -- (2,3.5);
\draw (0.5,2) -- (2,3.5);
\draw[dashed] (0.5,2) -- (4,1);

\filldraw (0,0-2) circle (2pt);
\filldraw (4,1-2) circle (2pt);
\filldraw (0.5,2-2) circle (2pt);
\filldraw (2,-2.5-2) circle (2pt);
\draw (0,0-2) -- (2,-2.5-2);
\draw (0,0-2) -- (4,1-2);
\draw (0,0-2) -- (0.5,2-2);
\draw (4,1-2) -- (2,-2.5-2);
\draw[dashed] (0.5,2-2) -- (2,-2.5-2);
\draw (0.5,2-2) -- (4,1-2);

\draw[thick,->] (4,0) -- (5.5,0);

\filldraw (6+2,3.5-1) circle (2pt);
\filldraw (6+0,0-1) circle (2pt);
\filldraw (6+0.5,2-1) circle (2pt);
\filldraw (6+2,-2.5-1) circle (2pt);
\draw (6+0,0-1) -- (6+2,3.5-1);
\draw (6+0,0-1) -- (6+0.5,2-1);
\draw (6+0.5,2-1) -- (6+2,3.5-1);
\draw (6+0.5,2-1) -- (6+2,3.5-1);
\draw (6+0,0-1) -- (6+2,-2.5-1);
\draw[dashed] (6+0.5,2-1) -- (6+2,-2.5-1);
\draw (6+2,3.5-1) -- (6+2,-2.5-1);

\filldraw (8+2,3.5-1) circle (2pt);
\filldraw (8+4,1-1) circle (2pt);
\filldraw (8+0.5,2-1) circle (2pt);
\filldraw (8+2,-2.5-1) circle (2pt);
\draw (8+4,1-1) -- (8+2,3.5-1);
\draw (8+0.5,2-1) -- (8+2,3.5-1);
\draw[dashed] (8+0.5,2-1) -- (8+4,1-1);
\draw (8+0.5,2-1) -- (8+2,3.5-1);
\draw (8+4,1-1) -- (8+2,-2.5-1);
\draw (8+0.5,2-1) -- (8+2,-2.5-1);
\draw (8+2,3.5-1) -- (8+2,-2.5-1);

\filldraw (11.75+2,3.5-1) circle (2pt);
\filldraw (11.75+0,0-1) circle (2pt);
\filldraw (11.75+4,1-1) circle (2pt);
\filldraw (11.75+2,-2.5-1) circle (2pt);
\draw (11.75+0,0-1) -- (11.75+2,3.5-1);
\draw (11.75+0,0-1) -- (11.75+4,1-1);
\draw (11.75+4,1-1) -- (11.75+2,3.5-1);
\draw (11.75+0,0-1) -- (11.75+2,-2.5-1);
\draw (11.75+4,1-1) -- (11.75+2,-2.5-1);
\draw[dashed] (11.75+2,3.5-1) -- (11.75+2,-2.5-1);

\filldraw[white] (1.5,2.2) circle (10pt);
\filldraw[white] (3,2.2) circle (10pt);
\filldraw[white] (2.5,0.75) circle (10pt);
\filldraw[white] (1.75,-1.5) circle (10pt);
\filldraw[white] (3,-2.5) circle (10pt);
\filldraw[white] (0.75,-3) circle (10pt);
\filldraw[white] (8,-0.5) circle (10pt);
\filldraw[white] (7.25,1) circle (10pt);
\filldraw[white] (7,-2) circle (10pt);
\filldraw[white] (15,-1.5) circle (10pt);
\filldraw[white] (13,-2.5) circle (10pt);
\filldraw[white] (13,-0.75) circle (10pt);
\filldraw[white] (9.25,-1) circle (10pt);
\filldraw[white] (10,0) circle (10pt);
\filldraw[white] (9.25,1.75) circle (10pt);

\node at (1.5,2.2) {$z_1$};
\node at (3,2.2) {$z_1'$};
\node at (2.5,0.75) {$z_1''$};
\node at (1.75,-1.5) {$z_2$};
\node at (3,-2.5) {$z_2'$};
\node at (0.75,-3) {$z_2''$};
\node at (7.25,1) {$\widetilde{z}_0$};
\node at (8,-0.5) {$\widetilde{z}_0'$};
\node at (7,-2) {$\widetilde{z}_0''$};
\node at (15,-1.5) {$\widetilde{z}_1$};
\node at (13,-2.5) {$\widetilde{z}_1'$};
\node at (13,-0.75) {$\widetilde{z}_1''$};
\node at (9.25,-1) {$\widetilde{z}_2$};
\node at (10,0) {$\widetilde{z}_2''$};
\node at (9.25,1.75) {$\widetilde{z}_2'$};

\end{tikzpicture}
\caption{The 2--3 Pachner move.}
\label{fig.23move}
\end{center}
\end{figure}

\noindent
Using $z_0=z_1+z_2-z_1z_2$ from Equation~\eqref{5z} used in
Theorem~\ref{thm.pentagon}, it follows that the shapes $z$ of $\calT$ and
$\widetilde z$ of $\widetilde\calT$ are related by
\bea
\label{z23}
z\=(z_1,z_2,z^{*}) \mapsto \widetilde z
\= &\big(
\widetilde{z}_0,\; \widetilde{z}_1,\; \widetilde{z}_2,\;\widetilde{z}^{*}
\big)\\
\=&\big(
z_0,\; z_1z_0^{-1},\; z_2z_0^{-1},\;z^{*}
\big)\,.
\eea
Similarly to~\cite[Eq. (3.20) and (3.21)]{DG}, these shapes satisfy the relations
\bea
\label{eq.23sr}
\widetilde{z}_0'&\=z_1'z_2'\,,\quad
& \widetilde{z}_1''&\=z_1''z_2\,,\quad
& \widetilde{z}_2''&\=z_1z_2''\,,\\
z_1&\=\widetilde{z}_0\widetilde{z}_1\,,\quad
& z_1'&\=\widetilde{z}_1'\widetilde{z}_2\,,\quad
& z_1''&\=\widetilde{z}_0''\widetilde{z}_2'\,,\\
z_2&\=\widetilde{z}_0\widetilde{z}_2\,,\quad
& z_2'&\=\widetilde{z}_1\widetilde{z}_2'\,,\quad
& z_2''&\=\widetilde{z}_0''\widetilde{z}_1'\,.
\eea
If we write the Neumann--Zagier matrices of $\calT$ in the form
\be
\label{AB2}
A \= (a_1\,|\,a_2\,|\,a_*)\,,\qquad B=\; (b_1\,|\,b_2\,|\,b_*)\,,
\ee
where $a_1$, $a_2$ are the first two columns of $A$ and $a_*$ is the block
$(N+2)\times N$ matrix of the remaining $N$ columns of $A$, and likewise for $B$,
then using Equations~\eqref{eq.23sr}
the corresponding Neumann--Zagier matrices of $\widetilde\calT$ are given by
\be
\label{AB3}
\widetilde A \= \begin{pmatrix}
 -1 & 0 & 0 & 0 \\
 -b_1-b_2+a_1+a_2 & a_1-b_2 & a_2-b_1 & a_*
 \end{pmatrix}, \qquad 
\widetilde B \= \begin{pmatrix}
 -1 & 1 & 1 & 0\\
 0 & b_1 & b_2 & b_*
\end{pmatrix}
\ee
and the corresponding vector $\widetilde\nu=(1,\nu)$. Analogously to the shapes,
we will fix flattenings
$(\widetilde{f}_0,\widetilde{f}_1,\widetilde{f}_2,\widetilde{f}^{*})$ and
$(\widetilde{f}_0'',\widetilde{f}_1'',\widetilde{f}_2'',\widetilde{f}''^{*})$ for
$(\widetilde{A}\,|\,\widetilde{B})$ and
$(f_1,f_2,f^{*})=(\widetilde{f}_0+\widetilde{f}_1,\widetilde{f}_0
+\widetilde{f}_2,f^{*})$ and $(f''_1,f''_2,f''^{*})=
(\widetilde{f}_0''+\widetilde{f}_2', \widetilde{f}_0''+\widetilde{f}_1',f''^{*})$
for $(A\,|\,B)$. The data of the flattenings then satisfy the additive versions
of Equations~\eqref{eq.23sr}.

\begin{theorem}
\label{thm.23}
The series $\Phi^{\Xi}(\hbar)$ is invariant under 2--3 Pachner moves.
\end{theorem}

The proof involves an application of the pentagon identity for $\psi_{\hbar}$
of Theorem~\ref{thm.pentagon}. 

For two triangulations $\calT$ and $\widetilde\calT$ with $N+2$ and $N+3$
tetrahedra and NZ matrices $(\calA \,|\,\calB)$, respectively, related by a Pachner
2--3 move. To define the corresponding series $\Phi^{\Xi}(\hbar)$ and
$\Phi^{\widetilde\Xi}(\hbar)$, we need to possibly change quads on $\calT$ and
$\widetilde\calT$ so that both $\calB$ and $\widetilde\calB$ are invertible. By a
quad move $q$, we can replace $(\calA \,|\,\calB)$ by $(\mathbf{A} \,|\,\mathbf{B})$
where $\det(\mathbf{B}) \neq 0$. Recalling that quad moves act on tetrahedra and
actions on different tetrahedra commute, we can write the move $q=q_2 \times q_N$
as a product of quad moves $q_2$ on the first 2 tetrahedra times moves $q_N$ on
the remaining $N$ tetrahedra of $\calT$. Let $(A \,|\,B)$ denote the result of
applying the move $1 \times q_N$ on the $N+2$ tetrahedra of $\calT$. 

Since the $(N+2)\times(N+2)$ matrix $\mathbf{B}$ has full rank and $B$ and
$\mathbf{B}$ have the same last $N$ columns, it follows that $B$ has nullity
$0$, $1$ or $2$. 

Now on $\widetilde\calT$, we can apply the identity move on the first three
tetrahedra and the $q_N$ moves on the remaining $N$ tetrahedra, which transforms
the NZ matrices $(\widetilde{\calA} \,|\, \widetilde{\calB})$
to $(\widetilde A \,|\,\widetilde B)$, and further apply the $q_2$ moves on
the second and third tetrahedra to obtain the NZ matrices
$(\widetilde{\mathbf{A}} \,|\,\widetilde{\mathbf{B}})$. By looking at how the
matrix $B$ transforms under a 2--3 move (see Equation~\eqref{AB3}), it follows
that $\widetilde{\mathbf{B}}$ has the same rank as $\mathbf{B}$, and hence
$\det(\widetilde{\mathbf{B}}) \neq 0$.

The above discussion can be summarized in the following commutative diagram.

\be
\begin{tikzcd}
(\mathcal{A}\;|\;\mathcal{B})
\arrow[rrr,"2 \to 3"]\arrow[rd,"1 \times q_N"]\arrow[dd,"q_2 \times q_N"] &  &
& (\widetilde{\mathcal{A}}\;|\;\widetilde{\mathcal{B}})
\arrow[dl,"\!\!\!\!1 \times 1 \times q_N"]\arrow[dd,"1 \times q_2 \times q_N"]\\
& (A\;|\;B)\arrow[r,"2 \to 3"]\arrow[dl,"q_2 \times 1"]
& (\widetilde{A}\;|\;\widetilde{B})\arrow[dr,"1 \times q_2 \times 1"] & \\
(\mathbf{A}\;|\;\mathbf{B}) &   &
& (\widetilde{\mathbf{A}}\;|\;\widetilde{\mathbf{B}})
\end{tikzcd}
\ee
where $\det(\mathbf{B}) \neq 0$ and $\det(\widetilde{\mathbf{B}}) \neq 0$.
Now $\Phi^\Xi(\hbar)$ and $\Phi^{\widetilde\Xi}(\hbar)$ can be defined using 
the nondegenerate NZ data with matrices $(\mathbf{A} \,|\,\mathbf{B})$ and 
$(\widetilde{\mathbf{A}} \,|\,\widetilde{\mathbf{B}})$, respectively. 
We will show that the two $\hbar$-series are equal using a diagram
\be
\label{2Phi}
\begin{tikzcd}
\Phi^\Xi(\hbar)\arrow[rr,"\otimes^i \text{Fourier}"] & & \bullet
\arrow[rr,"\text{Pentagon}"] & & \bullet
\arrow[rr,"\otimes^i \text{Fourier}^{-1}"] & & \bullet
\arrow[rr,"2i-\text{Fubini}"] & & \Phi^{\widetilde\Xi}(\hbar)
\end{tikzcd}
\ee
where $i=0,1,2$ denotes the nullity of $B$. We will treat each case in a separate
section. With this discussion the Theorem~\ref{thm.23} follows from
Propositions~\ref{prop.case0},~\ref{prop.case1}, and~\ref{prop.case2}.
Before proceeding with the proof, we will set some
notation. Similarly to the proof of the quad invariance, denote
$\mbfQ=\mathbf{B}^{-1}\mathbf{A}$

\bea
\label{eq:BinvA_def}
\mathbf Q \=
\def\arraystretch{1.15}
\left(\!\!
\begin{array}{cc|c}
\mathbf Q_{11} & \mathbf Q_{12} & \mathbf Q_1^*\\
\mathbf Q_{12} & \mathbf Q_{22} & \mathbf Q_2^*\\
\hline
\mathbf {Q_1^*}^t & \mathbf {Q_2^*}^t & \mathbf Q^*\\
\end{array}\!\!\right),










\eea
where $\mbfQ_{ij}$ are matrices of size $1\times 1$, $\mbfQ_{j}^{*}$
are matrices of size $1\times N$ and $\mbfQ^{*}$ is a matrix of size
$N\times N$.


\subsection{\texorpdfstring{The case of $B$ with full rank}{The case of B with full rank}}
\label{sub.case0}

In this section, we prove Theorem~\ref{thm.pentagon} under the assumption that
the matrix $B$ has full rank. In this case, Equation~\eqref{2Phi} simplifies
to the following one
\be
\label{2Phi.0}
\begin{tikzcd}
\Phi^\Xi(\hbar)\arrow[rr,"\text{Pentagon}"] & & \Phi^{\widetilde\Xi}(\hbar)
\end{tikzcd}
\ee
since we do not need to apply Fourier transform, nor Fubini's theorem.

\begin{proposition}
\label{prop.case0}
If $B$ has full rank, then $\Phi^{\Xi}(\hbar)$ is invariant under the 2--3
Pachner move given in Equation~\eqref{AB3}.
\end{proposition}

\begin{proof}
To begin with, noting that in this case $A=\mathbf{A}$ and $B=\mathbf{B}$, we have:
\be
\Phi^{\Xi}(\hbar) \= \langle I_0 \rangle_{x,\Lambda}
\ee
where
\[
I_0 \= \exp\Big(\frac\hbar8 f^t B^{-1} A f
-\frac{\hsqrt}2 x^t(B^{-1}\nu-1)\Big)
\prod_{j=1}^{N+2} \psi_{\hbar}(x_j,z_j)
\]
and
\[
\Lambda_0\=\diag(z')-\mbfQ 
\]
and $x=(x_1,x_2,x^*)$ are the integration variables. Applying the pentagon
identity of Theorem~\ref{thm.pentagon}, to the $\psi_{\hbar}$ with arguments
$x_1,x_2$ and introducing a new integration variable $x_0$, we obtain that
\be
\Phi^{\Xi}(\hbar) \= \langle I_1 \rangle_{(x_0,x),\Lambda_1}
\ee
where
\[
\begin{small}
\begin{aligned}
I_1 &\= \exp\Big(\!-\frac{\hbar}{24}+\frac\hbar8 f^t B^{-1} A f
-\frac{\hsqrt}2 x^t(B^{-1}\nu-1)\Big)\,
\psi_\hbar\Big(-x_0 -x_2
+\frac{x_1z_2+x_2z_1}{z_0},
z_1z_0^{-1}\Big)\\
&\!\!\times
\psi_\hbar\Big(x_0+x_1+x_2
-\frac{x_1z_2+x_2z_1}{z_0},
z_0\Big)
\,\psi_\hbar\Big(-x_0-x_1
+\frac{x_1z_2+x_2z_1}{z_0},
z_2z_0^{-1}\Big)
\prod_{j=1}^N \psi_{\hbar}(x_j^{*},z_j^{*})
\end{aligned}
\end{small}
\]
and 
\[
\Lambda_1 \= 
\begin{pmatrix}
 \frac{({z_1}+{z_2}-z_1z_2)^2}{({z_1}-1) {z_1} ({z_2}-1){z_2}}&
 0 \\
 0 & \Lambda
\end{pmatrix} \,.
\]
Making a change of variables $x_0\mapsto x_0+x_1(-1+z_2z_0^{-1})+x_2(-1+z_1z_0^{-1})$
using Lemma~\ref{lem.ff1}, we obtain that
\bea
\Phi^{\Xi}(\hbar) \= \langle I_2 \rangle_{(x_0,x),\Lambda_2},
\eea
where
\[
\begin{aligned}
I_2 &\= 
\exp\Big(-\frac{\hbar}{24}+\frac\hbar8 f^t B^{-1} A f
-\frac{\hsqrt}2 x^t(B^{-1}\nu-1)\Big)\,
\psi_\hbar(-x_0 +x_1,z_1z_0^{-1})\\
&\qquad\times\psi_\hbar(x_0,z_0)\,
\psi_\hbar(-x_0+x_2,z_2z_0^{-1})\,
\prod_{j=1}^N \psi_{\hbar}(x_j^{*},z_j^{*})
\end{aligned}
\]
and 
\[
\def\arraystretch{1.5}
\Lambda_2 \= 
\left(\!\!
\begin{array}{ccc|c}
 \frac{({z_1}+{z_2}-z_1z_2)^2}{({z_1}-1) {z_1} ({z_2}-1){z_2}}&
 \frac{{z_1+z_2-z_1z_2}}{z_2({z_1}-1)} &
 \frac{{z_1}+{z_2}-z_1z_2}{{z_1} ({z_2}-1)}&
 0 \\
\frac{{z_1+z_2-z_1z_2}}{z_2({z_1}-1)}&
-{\mbfQ_{11}}{-}\frac{{z_1+z_2-z_1z_2}}{z_2({z_1}-1)} &
 1-{\mbfQ_{12}} &
 -{\mbfQ_{1}^*} \\
 \frac{{z_1}+{z_2}-z_1z_2}{{z_1} ({z_2}-1)}&
 1-{\mbfQ_{12}} &
 -\mbfQ_{22}{-}\frac{{z_1+z_2-z_1z_2}}{z_1({z_2}-1)} &
 -{\mbfQ_{2}^*} \\
 \hline
 0 &
 -{\mbfQ_{1}^*}^t &
 -{\mbfQ_{2}^*}^t &
 {\diag({z^*}')}-{\mbfQ^*} \\
\end{array}
\!\!\right).
\]
Making a change of variables $x_1\mapsto x_1+x_0$ and $x_2\mapsto x_2+x_0$
using Lemma~\ref{lem.ff1}, and denoting $\widetilde{x}=(x_0,x)$,
$\widetilde{z}=(z_0,z_1z_0^{-1},z_2z_0^{-1},z^{*})$ we obtain that
\bea
\Phi^{\Xi}(\hbar) \= e^{c\hbar}\langle I_3 \rangle_{\widetilde{x},\Lambda_3},
\eea
where
\[
I_3 \= 
\exp\Big(\frac\hbar8 \widetilde{f}^t \widetilde{B}^{-1} \widetilde{A} \widetilde{f}
-\frac{\hsqrt}2 \widetilde{x}^t(\widetilde{B}^{-1}\widetilde{\nu}-1)\Big)
\prod_{j=1}^{N+3} \psi_{\hbar}(\widetilde{x}_j,\widetilde{z}_j)
\]
and
\[
\Lambda_3



















\=\diag(\tilde z') - \tilde B^{-1}\tilde A\,.
\]
\end{proof}

The next lemma identifies vectors and matrices of the two triangulations
$\calT$ and $\widetilde\calT$.

\begin{lemma}
\label{lem.23.c0}
With the notation used in the proof of the previous Proposition~\ref{prop.case0},
\begin{align}\label{eq.c1bia}
\widetilde B^{-1}\widetilde A &\= \left(\!\!
\def\arraystretch{1.25}
\begin{array}{ccc|c}
 {\mbfQ_{11}}+2 {\mbfQ_{12}}+{\mbfQ_{22}}-1 &
 {\mbfQ_{11}}+{\mbfQ_{12}}-1 & {\mbfQ_{12}}+{\mbfQ_{22}}-1 &
 {\mbfQ_{1}^*}+{\mbfQ_{2}^*} \\
 {\mbfQ_{11}}+{\mbfQ_{12}}-1 & {\mbfQ_{11}} & {\mbfQ_{12}}-1 & {\mbfQ_{1}^*} \\
 {\mbfQ_{12}}+{\mbfQ_{22}}-1 & {\mbfQ_{12}}-1 &
 {\mbfQ_{22}} & {\mbfQ_{2}^*} \\
 \hline
 {\mbfQ_{1}^*}^t+{\mbfQ_{2}^*}^t &
 {\mbfQ_{1}^*}^t & {\mbfQ_{2}^*}^t & {\mbfQ^*} \\
\end{array}
\!\!\right)\\
\widetilde B^{-1}\widetilde{\nu}
&\=
\begin{pmatrix}
(B^{-1}\nu)_1+(B^{-1}\nu)_2-1\\
B^{-1}\nu
\end{pmatrix}\label{eq.c1biv}\\
\widetilde{f}^{t}\widetilde{B}^{-1}\widetilde{\nu}
&\=f^{t}B^{-1}\nu-\widetilde{f}_{0}\label{eq.c1ff}
\end{align}
\end{lemma}

\begin{proof}






We will show that both sides of Equations~\eqref{eq.c1bia} and
Equations~\eqref{eq.c1biv} are equal after multiplying by the invertible
matrix $\widetilde{B}$. For Equation~\eqref{eq.c1bia}, we have
\bea[]
&\left(\!\!\begin{array}{ccc|c}
 -1 & 1 & 1 & 0\\
 0 & b_1 & b_2 & b_{*}
 \end{array}\!\!\right)
\left(\!\!
\def\arraystretch{1.25}
\begin{array}{ccc|c}
 {\mbfQ_{11}}+2 {\mbfQ_{12}}+{\mbfQ_{22}}-1 &
 {\mbfQ_{11}}+{\mbfQ_{12}}-1 & {\mbfQ_{12}}+{\mbfQ_{22}}-1 &
 {\mbfQ_{1}^*}+{\mbfQ_{2}^*} \\
 {\mbfQ_{11}}+{\mbfQ_{12}}-1 & {\mbfQ_{11}} &
 {\mbfQ_{12}}-1 & {\mbfQ_{1}^*} \\
 {\mbfQ_{12}}+{\mbfQ_{22}}-1 & {\mbfQ_{12}}-1 &
 {\mbfQ_{22}} & {\mbfQ_{2}^*} \\
 \hline
 {\mbfQ_{1}^*}^t+{\mbfQ_{2}^*}^t &
 {\mbfQ_{1}^*}^t & {\mbfQ_{2}^*}^t & {\mbfQ^*} \\
\end{array}
\!\!\right)\\
&\=\left(\!\!
\begin{array}{ccc|c}
-1 & 0 & 0 & {0}\\
\substack{b_1(-1+\mbfQ_{11}+\mbfQ_{12})+b_*{\mbfQ_1^*}^t\\
+b_2(-1+\mbfQ_{12}+\mbfQ_{22})+b_*{\mbfQ_2^*}^t}&
\substack{b_1\mbfQ_{11}+b_*{\mbfQ_1^*}^t\\+b_2(-1+\mbfQ_{12})} &
\substack{b_2\mbfQ_{22}+b_*{\mbfQ_2^*}^t\\+b_1(-1+\mbfQ_{12})} &
b_1\mbfQ_1^*+b_2\mbfQ_2^*+b_*\mbfQ_*
\end{array}
\!\!\right)\\
&\= \widetilde A.
\eea
For Equation~\eqref{eq.c1biv}, we have
\be
\begin{pmatrix}
 -1 & 1 & 1 & 0\\
 0 & b_1 & b_2 & b_{*}
\end{pmatrix}
\begin{pmatrix}
(B^{-1}\nu)_1+(B^{-1}\nu)_2-1\\
B^{-1}\nu
\end{pmatrix}
\=
\begin{pmatrix}
1\\
\nu
\end{pmatrix}.
\ee
Finally, for Equation~\eqref{eq.c1ff},
\be
\begin{aligned}
\widetilde{f}^{t}\widetilde{B}^{-1}\nu
&\=
\widetilde{f}^{t}
\begin{pmatrix}
(B^{-1}\nu)_1+(B^{-1}\nu)_2-1\\
B^{-1}\nu
\end{pmatrix}\\
&\=(\widetilde{f}_0+\widetilde{f}_1)(B^{-1}\nu)_1+(\widetilde{f}_0
+\widetilde{f}_2)(B^{-1}\nu)_2+f^{*}(B^{-1}\nu)_1-\widetilde{f}_{0}\,,
\end{aligned}
\ee
and we recall we choose $f_i=\widetilde{f}_0+\widetilde{f}_i$ for $i=1,2$.
\end{proof}


\subsection{\texorpdfstring{The case of $B$ with nullity one}{The case of B with nullity one}}
\label{sub.case1}

In this section, we prove Theorem~\ref{thm.pentagon} under the assumption that
the matrix $B$ has nullity 1. In this case, starting from the series
$\Phi^{\Xi}(\hbar)$, there are three intermediate formulas (shown as bullets)
in Equation~\eqref{2Phi} that eventually identify the result with 
$\Phi^{\widetilde\Xi}(\hbar)$. The intermediate formulas involve a Fourier
transform (adding one integration variable), a pentagon (adding a second
variable), an inverse Fourier transform (adding a third), and an application of
Fubini's theorem that removes two integration variables. The detailed computation
is given in the next proposition. 

\begin{proposition}
\label{prop.case1}
If $B$ has rank $N+1$ then $\Phi^{\Xi}(\hbar)$ is invariant under the 2--3
Pachner move given in Equation~\eqref{2Phi}.
\end{proposition}

\begin{proof}
Following the discussion above we can assume that
$\operatorname{rank}(b_1\,|\,b_2\,|\,b_*) = \operatorname{rank}(b_2\,|\,b_*) = N+1$.
Then by \cite[Lem.A.3]{DG}, the matrix $(a_1\,|\,b_2\,|\,b_*)$ has full rank and
we can apply a quad move to the first columns of $(A\,|\,B)$ to obtain
\bea
\mathbf A \= 
(-b_1 \,|\, a_2 \,|\, a_*)\,,\qquad
\mathbf B \= (a_1-b_1 \,|\, b_2 \,|\, b_*)\,,\qquad
\boldsymbol{\nu}
\=
\nu-b_1\,,
\eea
where $\mathbf B$ has full rank. The proof will use the following sequence
of intermediate matrices
\be
\label{manyAB}
\begin{small}
\begin{tikzpicture}[baseline=(current  bounding  box.center)]
\node[right] at (0,0) {$(\mathbf A\,|\, \mathbf B\,|\,\boldsymbol{\nu}) \,=
\left(\!\!\begin{array}{c|c|c|c|c|c|c}
-b_1 & a_2 & a_* & a_1-b_1 & b_2 & b_* & \nu-b_1
\end{array}\!\!\right)$};

\node[right] at (1,-0.9) {$q_1^{-1}\times 1$};
\draw[->,thick] (1,-0.5)--(1,-1.5);

\node[right] at (0,-2) {$(A\,|\,B\,|\,\nu) \,= \left(\!\!\begin{array}{c|c|c|c|c|c|c}
a_1 & a_2 & a_* & b_1 & b_2 & b_* &\nu
\end{array}\!\!\right)$};

\node[right] at (1,-2.9) {$2\to 3$};
\draw[->,thick] (1,-2.5)--(1,-3.5);

\node[right] at (0,-4.25) {$(\widetilde A\,|\,\widetilde B\,|\,\widetilde{\nu}) \,=
\left(\!\!\begin{array}{c|c|c|c|c|c|c|c|c}
-1 & 0 & 0 & 0 & -1 & 1 & 1 & 0 & 1\\
a_1+a_2-b_1-b_2 & a_1-b_2 & a_2-b_1 & a_*&
0 & b_1 & b_2 & b_* & \nu
\end{array}\!\!\right)$};

\node[right] at (1,-5.4) {$1\times q_1\times 1$};
\draw[->,thick] (1,-5)--(1,-6);

\node[right] at (0,-6.75) {$(\widetilde {\mathbf A}\,|\,\widetilde
{\mathbf B}\,|\,\widetilde{\boldsymbol{\nu}})
\,= 
\left(\!\!\begin{array}{c|c|c|c|c|c|c|c|c}
-1 & -1 & 0 & 0 & -1 & -1 & 1 & 0 & 0\\
a_1+a_2-b_1-b_2 & -b_1 & a_2-b_1 & a_*&
0 & a_1-b_1-b_2 & b_2 & b_* & \nu-b_1
\end{array}\!\!\right)$};

\end{tikzpicture}
\end{small}
\ee


























where $\mathbf B$ and $\widetilde {\mathbf B}$ are invertible.
With $x=(x_1,x_2,x^*)$ and $z=(z_1,z_2,z^*)$ vectors of size $N+2$,
$\Phi^{\Xi}(\hbar)$ is defined by 
\be
\Phi^{\Xi}(\hbar) \= \langle I_0 \rangle_{(x_1,x_2,x^*), \mathbf \Lambda_0}
\ee
where with $\mathbf f = (f_1',f_2,f^*)$
\begin{align*}
I_0 &\=\exp\Big(\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)\Big)\,
\psi_{\hbar}\Big( x_1,\frac 1 {1-z_1}\Big)\,
\psi_{\hbar}(x_2,z_2)\,
\prod_{j=1}^{N} \psi_{\hbar}( x^*_j, z^*_j)
\end{align*}
and 
\[
\mathbf \Lambda_0\=\diag(z_1'',z_2',{z^*}')-\mathbf Q \,.
\]












We apply Corollary \ref{cor.fourier} to the $\psi_\hbar$ with argument $ x_1$
and introduce a new variable $w_1$ to obtain
\be
\Phi^{\Xi}(\hbar) \= \langle I_1
\rangle_{(w_1, x_1, x_2,x^*),\mathbf \Lambda_1}
\ee
where
\begin{align*}
I_1 &\= \exp\Big(\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-x_1\frac {\hsqrt}{2}\Big)\\
&\qquad\times\psi_{\hbar}\Big(w_1- x_1(1-z_1^{-1}) ,z_1\Big)\,
\psi_{\hbar}(x_2,z_2)
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_1 \=
\begin{pmatrix}
\frac {z_1} {1-z_1} & 0\\
0 & \mathbf \Lambda
\end{pmatrix}.
\]
We substitute $w_1 \mapsto w_1+ x_1(1-z_1^{-1})$ and obtain, from
Lemma~\ref{lem.ff1}, that
\be
\Phi^{\Xi}(\hbar) \=
\langle I_2 \rangle_{(w_1, x_1, x_2,x^*),\mathbf \Lambda_2}
\ee
where
\begin{align*}
I_2 &\=\exp\Big(\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-x_1\frac \hsqrt2\Big)\,
\psi_{\hbar}(w_1,z_1)\,
\psi_{\hbar}(x_2,z_2)
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and with $\mathbf Q_{11} = 0$ from Lemma \ref{lem.23.c1}
\[
\mathbf \Lambda_2 \= 
\left(\!\!
\def\arraystretch{1.15}
\begin{array}{ccc|c}
 \frac{z_1}{1-{z_1}} & -1 & 0 & 0 \\
 -1 & 0 & -{\mathbf Q_{12}} & -{\mathbf Q_1^*} \\
 0 & -{\mathbf Q_{12}} & \frac{1}{1-{z_2}}-{\mathbf Q_{22}} & -{\mathbf Q_2^*} \\
 \hline
 0 & -{\mathbf Q_1^*}^t & -{\mathbf Q_2^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
We apply the pentagon identity of Theorem \ref{thm.pentagon} to the $\psi_h$
with arguments $w_1$ and $x_1$ and obtain, with the new integration variable $x_0$,
that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_3 \rangle_{(x_0,w_1, x_1, x_2,x^*),
\mathbf \Lambda_3}
\eea
where
\begin{align*}
I_3 &\= \exp\Big(\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-x_1 \frac {\hsqrt}{2}\Big)\,
\psi_\hbar\Big(-x_0-x_2+\frac{w_1z_2+x_2z_1}{z_0},z_1z_0^{-1}\Big)\\
&\psi_\hbar\Big(x_0+w_1+x_2-\frac{w_1z_2+x_2z_1}{z_0},z_0\Big)\,
\psi_\hbar\Big(-x_0-w_1+\frac{w_1z_2+x_2z_1}{z_0},z_2z_0^{-1}\Big)
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_3 \= 
\left(\!\!
\def\arraystretch{1.15}
\begin{array}{cccc|c}
 \frac{({z_1}+{z_2}-z_1z_2)^2}{({z_1}-1) {z_1} ({z_2}-1)
 {z_2}} & 0 & 0 & 0 & 0 \\
 0 & \frac{z_1}{1-{z_1}} & -1 & 0 & 0 \\
 0 & -1 & 0 & -{\mathbf Q_{12}} & -{\mathbf Q_{1}^*} \\
 0 & 0 & -{\mathbf Q_{12}} &
 \frac{1}{1-{z_2}}-{\mathbf Q_{22}} & -{\mathbf Q_{2}^*} \\
 \hline
 0 & 0 & -{\mathbf Q_{1}^*}^t &
 -{\mathbf Q_{2}^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
We use Lemma \ref{lem.ff1} to change the variables
$x_0\mapsto x_0 -w_1-x_2+\frac{w_1z_2+x_2z_1}{z_0}$ and obtain
that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_4 \rangle_{(x_0,w_1,x_1, x_2,x^*),
\mathbf \Lambda_4}
\eea
where
\begin{align*}
I_4 &\= \exp\Big(\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-x_1 \frac {\hsqrt}{2}\Big)\\
&\qquad\times\psi_\hbar(-x_0+w_1,z_1z_0^{-1})\,
\psi_\hbar(x_0,z_0)\,
\psi_\hbar(-x_0+x_2,z_2z_0^{-1})
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_4 \= 
\left(\!\!
\def\arraystretch{1.15}
\begin{array}{cccc|c}
\frac{({z_1}+{z_2}-z_1z_2)^2}{({z_1}-1) {z_1} ({z_2}-1) {z_2}} &
\frac{{z_1}+{z_2}-z_1z_2}{({z_1}-1) {z_2}} & 0 &
\frac{{z_1}+{z_2}-z_1z_2}{{z_1} ({z_2}-1)} & 0 \\
\frac{{z_1}+{z_2}-z_1z_2}{({z_1}-1) {z_2}} &
\frac{{z_1}}{{z_2}(1-{z_1})} & -1 & 1 & 0 \\
 0 & -1 & 0 & -{\mathbf Q_{12}} & -{\mathbf Q_{1}^*} \\
\frac{{z_1}+{z_2}-z_1z_2}{{z_1} ({z_2}-1)}  & 1 & -{\mathbf Q_{12}} &
-\mathbf Q_{22}-\frac{z_1+z_2-z_1z_2}{z_1(z_2-1)} & -{\mathbf Q_{2}^*} \\
\hline
 0 & 0 & -{Q_{1}^*}^t & -{\mathbf Q_{2}^*}^t & {z^*}'-{\mathbf Q_{}^*} \\
\end{array}
\!\!\right).
\]
We substitute $w_1\mapsto w_1+x_0$ and $x_2\mapsto x_2+x_0$ to obtain, with
Lemma \ref{lem.ff1}, that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_5 \rangle_{(x_0,w_1,x_1, x_2,x^*),
\mathbf \Lambda_5}
\eea
where
\begin{align*}
I_5 &\= \exp\Big(\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-\frac{\hsqrt}2 x_0(\mathbf B^{-1}\boldsymbol{\nu}_2-1)
-x_1 \frac {\hsqrt}{2}\Big)\\
&\qquad\times\psi_\hbar(w_1,z_1z_0^{-1})\,
\psi_\hbar(x_0,z_0)\,
\psi_\hbar(x_2,z_2z_0^{-1})
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_5 \= 
\left(\!\!
\def\arraystretch{1.15}
\begin{array}{cccc|c}
 -{\mathbf Q_{22}}+\frac{1}{({z_1}-1) ({z_2}-1)} &
 0 & -1-{\mathbf Q_{12}} & 1-{\mathbf Q_{22}} & -{\mathbf Q_{2}^*} \\
 0 & \frac{{z_1}}{{z_2}(1-{z_1})}& -1 & 1 & 0 \\
 -1-{\mathbf Q_{12}} & -1 & 0 & -{\mathbf Q_{12}} & -{\mathbf Q_{1}^*} \\
 1-{\mathbf Q_{22}} & 1 & -{\mathbf Q_{12}} &
-\mathbf Q_{22}+\frac{z_1+z_2-z_1z_2}{z_1(z_2-1)}& -{\mathbf Q_{2}^*} \\
\hline
-{\mathbf Q_{2}^*}^t & 0 & -{\mathbf Q_{1}^*}^t & -{\mathbf Q_{2}^*}^t &
{z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
By applying the first quad move from Theorem \ref{thm.fourier} to
$\psi_\hbar(w_1,z_1z_0^{-1})$ we obtain, with a new integration variable $y_1$, that
\bea
\Phi^{\Xi}(\hbar) \=
e^{-\frac \hbar {24}}\langle I_6 \rangle_{(y_1,x_0,w_1, x_1, x_2,x^*),
\mathbf \Lambda_6}
\eea
where
\begin{align*}
I_6 &\=\exp\Big(-\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)
\\ & \quad
-\frac{\hsqrt}2 x_0((\mathbf B^{-1}\boldsymbol{\nu})_2-1)
-x_1 \frac {\hsqrt}{2}
+\Big(y_1+\frac{w_1z_1z_0^{-1}}{1-z_1z_0^{-1}}\Big)\frac{\hsqrt}{2}\Big)\\
&\qquad\times
\psi_\hbar\Big(y_1+\frac{w_1z_1z_0^{-1}}{1-z_1z_0^{-1}},\frac1{1-z_1z_0^{-1}}\Big)\,
\psi_\hbar(x_0,z_0)\,
\psi_\hbar(x_2,z_2z_0^{-1})
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\begin{small}
\[
\mathbf \Lambda_6 \=
\left(\!\!
\def\arraystretch{1.15}
\begin{array}{ccccc|c}
\frac{(z_1-1)z_2}{z_1} & 0& 0& 0& 0& 0\\
 0&-{\mathbf Q_{22}}+\frac{1}{({z_1}-1) ({z_2}-1)} &
 0 & -1-{\mathbf Q_{12}} & 1-{\mathbf Q_{22}} & -{\mathbf Q_{2}^*} \\
 0&0 & \frac{{z_1}}{{z_2}(1-{z_1})}& -1 & 1 & 0 \\
 0&-1-{\mathbf Q_{12}} & -1 & 0 & -{\mathbf Q_{12}} & -{\mathbf Q_{1}^*} \\
 0&1-{\mathbf Q_{22}} & 1 & -{\mathbf Q_{12}} &
-\mathbf Q_{22}+\frac{z_1+z_2-z_1z_2}{z_1(z_2-1)}& -{\mathbf Q_{2}^*} \\
\hline
0&-{\mathbf Q_{2}^*}^t & 0 & -{\mathbf Q_{1}^*}^t &
-{\mathbf Q_{2}^*}^t & {z^*}'-{\mathbf Q^*} 
\end{array}
\!\!\right).
\]
\end{small}
We change variables $y_1\mapsto y_1-w_1\frac{z_1z_0^{-1}}{1-z_1z_0^{-1}}$ using
Lemma \ref{lem.ff1} and obtain that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_7 \rangle_{(y_1,x_0,w_1, x_1, x_2,x^*),
\mathbf \Lambda_7}
\eea
where
\begin{align*}
I_7 &\=\exp\Big(-\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-\frac{\hsqrt}2 x_0((\mathbf B^{-1}\boldsymbol{\nu})_2-1)
-x_1 \frac {\hsqrt}{2}
+y_1\frac{\hsqrt}{2}\Big)\\
& \qquad\times
\psi_\hbar\Big(y_1,\frac1{1-z_1z_0^{-1}}\Big)\,
\psi_\hbar(x_0,z_0)\,
\psi_\hbar(x_2,z_2z_0^{-1})
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_7 \= 
\left(\!\!
\def\arraystretch{1.15}
\begin{array}{ccccc|c}
\frac{(z_1-1)z_2}{z_1} & 0& 1& 0& 0& 0\\
 0&-{\mathbf Q_{22}}+\frac{1}{({z_1}-1) ({z_2}-1)} &
 0 & -1-{\mathbf Q_{12}} & 1-{\mathbf Q_{22}} & -{\mathbf Q_{2}^*} \\
 1&0 & 0& -1 & 1 & 0 \\
 0&-1-{\mathbf Q_{12}} & -1 & 0 & -{\mathbf Q_{12}} & -{\mathbf Q_{1}^*} \\
 0&1-{\mathbf Q_{22}} & 1 & -{\mathbf Q_{12}} &
-\mathbf Q_{22}+\frac{z_1+z_2-z_1z_2}{z_1(z_2-1)}& -{\mathbf Q_{2}^*} \\
\hline
0&-{\mathbf Q_{2}^*}^t & 0 & -{\mathbf Q_{1}^*}^t &
-{\mathbf Q_{2}^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
Therefore, we can apply Fubini's Theorem (Lemma~\ref{lem.ff1}) with the
integration variables $w_1,x_1$,
to obtain that





























\bea
\Phi^{\Xi}(\hbar) \=
\langle I_8 \rangle_{(y_1,x_0, x_2,x^*),
\mathbf \Lambda_8}
\eea
where 
\begin{align*}
I_8 &\= \exp\Big(-\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2(
x_0 ((\mathbf B^{-1}\boldsymbol{\nu})_2-1)
+y_1((\mathbf B^{-1}\boldsymbol{\nu})_1-1)
\\ & \qquad\qquad +x_2 ((\mathbf B^{-1}\boldsymbol{\nu})_2
+(\mathbf B^{-1}\boldsymbol{\nu})_1-1)
+x^*((\mathbf B^{-1}\boldsymbol{\nu})^*-1)
)\Big)\\
& \qquad 
\times
\psi_\hbar\Big(y_1,\frac1{1-z_1z_0^{-1}}\Big)\,
\psi_\hbar(x_0,z_0)\,
\psi_\hbar(x_2,z_2z_0^{-1})
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_8 \=
\left(\!\!
\begin{array}{ccc|c}
\frac{({z_1}-1) {z_2}}{{z_1}} & -{\mathbf Q_{12}}-1 &
-{\mathbf Q_{12}} & -{Q_{1}^*} \\
-{\mathbf Q_{12}}-1 & \frac{1}{({z_1}-1) ({z_2}-1)}-{\mathbf Q_{22}} &
-{\mathbf Q_{12}}-{\mathbf Q_{22}} & -{\mathbf Q_{2}^*}
\\
-{\mathbf Q_{12}} & -{\mathbf Q_{12}}-{\mathbf Q_{22}} & 
-2 {\mathbf Q_{12}}-\mathbf Q_{22} + \frac{z_1+z_2-z_1z_2}{z_1(1-z_2)}
& -{\mathbf Q_{1}^*}-{\mathbf Q_{2}^*} \\
\hline
-{\mathbf Q_{1}^*}^t & -{\mathbf Q_{2}^*}^t &
-{\mathbf Q_{1}^*}^t-{\mathbf Q_{2}^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right) \,.
\]
Using Lemma \ref{lem.23.c1} we obtain, with respect to the integration
variables $\tilde x = (x_0,y_1,x_2,x^*)$ and some $c\in\frac{1}{24}\BZ$, that
\bea
\Phi^{\Xi}(\hbar) \=e^{c\hbar}
\langle I_9 \rangle_{\tilde x, \mathbf \Lambda_9}
\eea
where
\[
I_9 \= \exp\Big(\frac\hbar8 \widetilde{\mathbf f}^t \widetilde{\mathbf B}^{-1}
\widetilde{\mathbf A} \widetilde{\mathbf f}
-\frac{\hsqrt}2 \tilde x^t(\widetilde {\mathbf B}^{-1}
\widetilde{\boldsymbol{\nu}}-1)\Big)\,
\prod_{j=0}^{N+2} \psi_{\hbar}( \widetilde{x}_j^*, \widetilde{z}_j^*)
\]
and with $\widetilde {\mathbf A}$, $ \widetilde {\mathbf B}$ as in 
\eqref{manyAB}
\[
\mathbf \Lambda_9 \=
\diag(\widetilde{z}_0',
\widetilde{z}_1'',
\widetilde{z}_2',
\widetilde{z}^*{}')
- {\widetilde {\mathbf B}}^{-1}\widetilde {\mathbf A}.
\]








\end{proof}

\begin{lemma}
\label{lem.23.c1}
With the notation used in the previous proof of Proposition~\ref{prop.case1}
we have\\ $\mbfQ_{11}=0$ and the following equalities:
\begin{align}
\label{eq.c2.bia}
\widetilde {\mathbf B}^{-1} \widetilde {\mathbf A} &\=
\left(\!\!\begin{array}{ccc|c}
\mathbf Q_{22} & \mathbf Q_{12} + 1&
\mathbf Q_{12} + \mathbf Q_{22}& \mathbf Q_2^*\\
\mathbf Q_{12} + 1& 0&
\mathbf Q_{12}& \mathbf Q_1^*\\
\mathbf Q_{12} +\mathbf Q_{22}& \mathbf Q_{12}&
2\mathbf Q_{12} +\mathbf  Q_{22}& \mathbf Q_1^* + \mathbf Q_2^*\\
\hline
{\mathbf Q_2^*}^t& {\mathbf Q_1^*}^t&
{\mathbf Q_1^*}^t + {\mathbf Q_2^*}^t& \mathbf Q^*
\end{array}
\!\!\right),
\\\label{eq.c2.binu}
\widetilde {\mathbf B}^{-1}\widetilde{\boldsymbol{\nu}}
&\= \left(\!\!
\begin{array}{c}
(\mathbf B^{-1}\boldsymbol{\nu})_2\\
(\mathbf B^{-1}\boldsymbol{\nu})_1\\
(\mathbf B^{-1}\boldsymbol{\nu})_1 + (\mathbf B^{-1}\boldsymbol{\nu})_2\\
(\mathbf B^{-1}\boldsymbol{\nu})^*
\end{array}\!\!\right),
\\\label{eq.c3.ff}
\widetilde{\mathbf{f}}^{t}\widetilde {\mathbf B}^{-1}\widetilde{\boldsymbol{\nu}}
&\= \mathbf{f}^{t}\mathbf{B}^{-1}\boldsymbol{\nu}\,.
\end{align}
\end{lemma}

\begin{proof}
Similarly to the proof of Lemma \ref{lem.23.c0} we will proof Equations
\eqref{eq.c2.bia} and \eqref{eq.c2.binu} by showing that both sides are equal
after multiplying by the invertible matrix $\widetilde {\mathbf B}$.
Using $\mathbf Q=\mathbf B^{-1} \mathbf A$ and the fact that
$(a_1\,|\,b_2\,|\,b_*)$ are linearly independent we conclude $\mbfQ_{11}=0$.
For \eqref{eq.c2.bia} we compute

\bea[]
&\begin{pmatrix}
-1 & -1 & 1 & 0 \\
0 & a_1-b_1-b_2 & b_2 & b_*
\end{pmatrix}
\left(\!\!\begin{array}{ccc|c}
\mathbf Q_{22} &\mathbf  Q_{12} + 1&
\mathbf Q_{12} + \mathbf Q_{22}& \mathbf Q_2^*\\
\mathbf Q_{12} + 1& 0& \mathbf Q_{12}& \mathbf Q_1^*\\
\mathbf Q_{12} + \mathbf Q_{22}& \mathbf Q_{12}&
2\mathbf Q_{12} + \mathbf Q_{22}& \mathbf Q_1^* + \mathbf Q_2^*\\
\hline
{\mathbf Q_2^*}^t& {\mathbf Q_1^*}^t&
{\mathbf Q_1^*}^t + {\mathbf Q_2^*}^t& \mathbf Q^*
\end{array}\!\!\right)\\
\=&\begin{pmatrix}
-1 & -1 & 0 & 0\\
\substack{(a_1-b_1)\mathbf Q_{12}\\
 +b_2\mathbf Q_{22}+b_*{\mathbf Q_2^*}^t}&
\substack{b_2\mathbf Q_{12}+b_*{\mathbf Q_1^*}^t}&
\substack{b_2\mathbf Q_{12}+b_*{\mathbf Q_1^*}^t+\\
(a_1-b_1)\mathbf Q_{12}+b_2\mathbf Q_{22}+b_*{\mathbf Q_1^*}^t}&
\substack{(a_1-b_1-b_2)\mathbf Q_1^*\\
+b_2(\mathbf Q_1^*+\mathbf Q_2^*)+b_*\mathbf Q^*}
\end{pmatrix}\\




\= &\widetilde {\mathbf A}
\eea
For \eqref{eq.c2.binu} we have
\bea[]
&\begin{pmatrix}
-1 & -1 & 1 & 0 \\
0 & a_1-b_1-b_2 & b_2 & b_*
\end{pmatrix}
\left(\!\!
\begin{array}{c}
(\mathbf B^{-1}\boldsymbol{\nu})_2\\
(\mathbf B^{-1}\boldsymbol{\nu})_1\\
(\mathbf B^{-1}\boldsymbol{\nu})_1 + (\mathbf B^{-1}\boldsymbol{\nu})_2\\
(\mathbf B^{-1}\boldsymbol{\nu})^*
\end{array}\!\!\right)\\
&\= 
\left(\!\!\begin{array}{c}
0\\ \boldsymbol{\nu}
\end{array}\!\!\right)
\eea
For Equation~\eqref{eq.c3.ff}, we have
\be
\begin{aligned}
&\widetilde{\mathbf{f}}^{t}
\left(\!\!
\begin{array}{c}
(\mathbf B^{-1}\boldsymbol{\nu})_2\\
(\mathbf B^{-1}\boldsymbol{\nu})_1\\
(\mathbf B^{-1}\boldsymbol{\nu})_1 + (\mathbf B^{-1}\boldsymbol{\nu})_2\\
(\mathbf B^{-1}\boldsymbol{\nu})^*
\end{array}\!\!\right)\\








&\=
(\widetilde{f}_1'+\widetilde{f}_2)(\mathbf B^{-1}\boldsymbol{\nu})_1
+
(\widetilde{f}_0-\widetilde{f}_2)(\mathbf B^{-1}\boldsymbol{\nu})_2
+
\widetilde{f}^{*}(\mathbf B^{-1}\boldsymbol{\nu})^*\,.
\end{aligned}
\ee
Then, using the analogous relations between the flattening as given in
Equation~\eqref{eq.23sr} for the shapes, we have
$\widetilde{f}_1'+\widetilde{f}_2=f_1'=\mathbf{f}_1$ and
$\widetilde{f}_0-\widetilde{f}_2=f_2=\mathbf{f}_2$.
\end{proof}


\subsection{\texorpdfstring{The case of $B$ with nullity two}{The case of B with nullity two}}
\label{sub.case2}

In this section, we prove Theorem~\ref{thm.pentagon} under the assumption
that the matrix $B$ has nullity 2. Similarly to the proof of
Proposition~\ref{prop.case1}, we use three intermediate formulas in
Equation~\eqref{2Phi}. They involve two Fourier transforms (adding two
variables), a pentagon (adding a third variable), two inverse Fourier
transforms (adding two variables) and an applications of Fubini's Theorem
(removing four integration variables). The details are given in the following
proposition.

\begin{proposition}
\label{prop.case2}
If $B$ has rank $N$ then $\Phi^{\Xi}(\hbar)$ is invariant under the 2--3
Pachner move given in Equation~\eqref{2Phi}.
\end{proposition}

\begin{proof}

Following the discussion above, we can assume that
$\operatorname{rank}(b_1\,|\,b_2\,|\,b_*) = \operatorname{rank}(\,b_*) = N$.
Then by \cite[Lem.A.3]{DG}, the matrix $(a_1-b_1\,|\,a_2-b_2\,|\,b_*)$ has full rank
and we can apply a quad move to the first columns of $(A\,|\,B)$ to obtain
\bea
\mathbf A \= 
(-b_1 \,|\, -b_2 \,|\, a_*),\qquad
\mathbf B \= (a_1-b_1 \,|\, a_2-b_2 \,|\, b_*)
\eea
where $\mathbf B$ has full rank. The proof will use the following sequence
of intermediate matrices
\be
\label{manyAB.c2}
\begin{small}
\begin{tikzpicture}[baseline=(current  bounding  box.center)]
\node[right] at (0,0) {$(\mathbf A\,|\, \mathbf B\,|\,\boldsymbol{\nu}) \,=
\left(\!\!\begin{array}{c|c|c|c|c|c|c}
-b_1 & -b_2 & a_* & a_1-b_1 & a_2-b_2 & b_* & \nu-b_1-b_2
\end{array}\!\!\right)$};

\node[right] at (1,-0.9) {$q_2^{-1}\times 1$};
\draw[->,thick] (1,-0.5)--(1,-1.5);

\node[right] at (0,-2) {$(A\,|\,B\,|\,\nu) \,= \left(\!\!\begin{array}{c|c|c|c|c|c|c}
a_1 & a_2 & a_* & b_1 & b_2 & b_* &\nu
\end{array}\!\!\right)$};

\node[right] at (1,-2.9) {$2\to 3$};
\draw[->,thick] (1,-2.5)--(1,-3.5);

\node[right] at (0,-4.25) {$(\widetilde A\,|\,\widetilde B\,|\,\widetilde{\nu}) \,=
\left(\!\!\begin{array}{c|c|c|c|c|c|c|c|c}
-1 & 0 & 0 & 0 & -1 & 1 & 1 & 0 & 1\\
a_1+a_2-b_1-b_2 & a_1-b_2 & a_2-b_1 & a_*&
0 & b_1 & b_2 & b_* & \nu
\end{array}\!\!\right)$};

\node[right] at (1,-5.4) {$1\times q_2\times 1$};
\draw[->,thick] (1,-5)--(1,-6);

\node[right] at (0,-6.75) {$(\widetilde {\mathbf A}\,|\,\widetilde
{\mathbf B}\,|\,\widetilde{\boldsymbol{\nu}})=$};

\node[right] at (0.25,-7.75)
{$\left(\!\!\begin{array}{c|c|c|c|c|c|c|c|c}
-1 & -1 & -1 & 0 & -1 & -1 & -1 & 0 & -1\\
a_1+a_2-b_1-b_2 & -b_1 & -b_2 & a_*&
0 & a_1-b_1-b_2 & a_2-b_1-b_2 & b_* & \nu - b_1-b_2
\end{array}\!\!\right)$};
\end{tikzpicture}
\end{small}
\ee

\noindent
where $\mathbf B$ and $\widetilde {\mathbf B}$ are invertible.
With $x=(x_1,x_2,x^*)$ and $z=(z_1,z_2,z^*)$ vectors of size $N+2$,
$\Phi^\Xi(\hbar)$ is defined by
\bea
\Phi^{\Xi}(\hbar) \= \langle I_0 \rangle_{(x_1,x_2,x^*), \mathbf \Lambda_0}
\eea
where with $\mathbf f = (f_1',f_2',f^*)$ 
\begin{align*}
I_0 &\= \exp\Big(
\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)\Big)\\
&\qquad\times\psi_{\hbar}\Big( x_1,\frac 1 {1-z_1}\Big)\,
\psi_{\hbar}\Big(x_2,\frac 1 {1-z_2}\Big)\,
\prod_{j=1}^{N} \psi_{\hbar}( x^*_j, z^*_j)
\end{align*}
and
\[
\mathbf \Lambda_0 \= \diag(1-z_1^{-1}, 1-z_2^{-1}, {z^*}') - \mbfQ\,.
\]












By applying Corollary \ref{cor.fourier} to both $\psi_\hbar(x_1,\frac1{1-z_1})$
and $\psi_\hbar(x_1,\frac1{1-z_1})$ we obtain with new integration
variables $w_1$ and $w_2$ that
\bea
\Phi^{\Xi}(\hbar) \= \langle I_1
\rangle_{(w_1,w_2, x_1, x_2,x^*),\mathbf \Lambda_1}
\eea
where
\begin{align*}
I_1 &\= \exp\Big(\frac{\hbar}{12}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-(x_1+x_2)\frac {\hsqrt}{2}\Big)\\
&\qquad\times\psi_{\hbar}\Big(w_1- x_1(1-z_1^{-1}) ,z_1\Big)\,
\psi_{\hbar}\Big(w_2- x_2(1-z_2^{-1}) ,z_1\Big)\,
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_1 \= 
\begin{pmatrix}
\frac{z_2}{1-z_2} & 0 & 0\\
0 & \frac{z_1}{1-z_1} & 0\\
0 & 0 & \mathbf\Lambda
\end{pmatrix}
\]
The substitutions $w_1 \mapsto w_1+ x_1(1-z_1^{-1})$ and
$w_2 \mapsto w_2+ x_2(1-z_2^{-1})$ imply according to Lemma \ref{lem.ff1} that
\be
\Phi^{\Xi}(\hbar) \=
\langle I_2 \rangle_{(w_1,w_2,x_1, x_2,x^*),\mathbf \Lambda_2}
\ee
where
\begin{align*}
I_2 &\=\exp\Big(\frac{\hbar}{12}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-(x_1+x_2)\frac \hsqrt2\Big)\\
&\qquad\times\psi_{\hbar}(w_1,z_1)\,
\psi_{\hbar}(w_2,z_2)\,
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and with $\mathbf Q_{11} = \mbfQ_{12} = \mbfQ_{22} = 0$ from Lemma \ref{lem.23.c2}
\[
\mathbf \Lambda_2 \= 
\left(\!\!
\begin{array}{cccc|c}
 \frac{z_1}{1-{z_1}} & 0 & -1 & 0 & 0 \\
 0 & \frac{z_2}{1-{z_2}} & 0 & -1 & 0\\
 -1 & 0 & 0 &0 & -{\mathbf Q_1^*} \\
 0 & -1 & 0 & 0 & -{\mathbf Q_2^*} \\
 \hline
 0 & 0 &-{\mathbf Q_1^*}^t & -{\mathbf Q_2^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
We apply the pentagon identity of Theorem \ref{thm.pentagon} to the $\psi_h$
with arguments $w_1$ and $w_1$ and obtain with the new integration variable $x_0$
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_3 \rangle_{(x_0,w_1,w_2, x_1, x_2,x^*),
\mathbf \Lambda_3}
\eea
where
\begin{align*}
I_3 &\=\exp\Big(\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-(x_1+x_2) \frac {\hsqrt}{2}\Big)\\
&\qquad\times
\psi_\hbar\Big(-x_0-w_2+\frac{w_1z_2+w_2z_1}{z_0},z_1z_0^{-1}\Big)\,
\psi_\hbar\Big(x_0+w_1+w_2-\frac{w_1z_2+w_2z_1}{z_0},z_0\Big)\\
&\qquad\times
\psi_\hbar\Big(-x_0-w_1+\frac{w_1z_2+w_2z_1}{z_0},z_2z_0^{-1}\Big)\,
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_3 \= 
\left(\!\!
\begin{array}{ccccc|c}
 \frac{({z_1}+{z_2}-z_1z_2)^2}{({z_1}-1) {z_1} ({z_2}-1){z_2}}&
 0 & 0 & 0 & 0 & 0 \\
 0 & \frac{z_1}{1-{z_1}} & 0 & -1 & 0 & 0 \\
 0 & 0 & \frac{z_2}{1-{z_2}} & 0 & -1 & 0\\
 0 & -1 & 0 & 0 &0 & -{\mathbf Q_1^*} \\
 0 & 0 & -1 & 0 & 0 & -{\mathbf Q_2^*} \\
 \hline
 0 & 0 & 0 &-{\mathbf Q_1^*}^t & -{\mathbf Q_2^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
With change of variables $x_0 \mapsto x_0-w_1-w_2+\frac{w_1z_2+w_2z_1}{z_0}$
Lemma \ref{lem.ff1} gives that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_4 \rangle_{(x_0,w_1,w_2, x_1, x_2,x^*),
\mathbf \Lambda_4}
\eea
where
\begin{align*}
I_4 &\= \exp\Big(\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-(x_1+x_2) \frac {\hsqrt}{2}\Big)\\
&\qquad\times\psi_\hbar(-x_0+w_1,z_1z_0^{-1})\,
\psi_\hbar(x_0,z_0)\,
\psi_\hbar(-x_0+w_2,z_2z_0^{-1})\,
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_4 \= 
\left(\!\!
\begin{array}{ccccc|c}
 \frac{({z_1}+{z_2}-z_1z_2)^2}{({z_1}-1) {z_1} ({z_2}-1){z_2}}&
 \frac{{z_1}+{z_2}-z_1z_2}{({z_1}-1) {z_2}} &
 \frac{{z_1}+{z_2}-z_1z_2}{({z_2}-1) {z_1}} & 0 & 0 & 0 \\
 \frac{{z_1}+{z_2}-z_1z_2}{({z_1}-1) {z_2}} &
 \frac{z_1}{1-{z_1}} & 1 & -1 & 0 & 0 \\
 \frac{{z_1}+{z_2}-z_1z_2}{({z_2}-1) {z_1}} &
 1 & \frac{z_2}{1-{z_2}} & 0 & -1 & 0\\
 0 & -1 & 0 & 0 &0 & -{\mathbf Q_1^*} \\
 0 & 0 & -1 & 0 & 0 & -{\mathbf Q_2^*} \\
 \hline
 0 & 0 & 0 &-{\mathbf Q_1^*}^t & -{\mathbf Q_2^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
We substitute $w_1\mapsto w_1+x_0$ and $w_2\mapsto w_2+x_0$ to obtain with
Lemma \ref{lem.ff1} that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_5 \rangle_{(x_0,w_1,w_2,x_1, x_2,x^*),
\mathbf \Lambda_5}
\eea
where
\begin{align*}
I_5 &\= \exp\Big(\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-(x_1+x_2) \frac {\hsqrt}{2}\Big)\\
&\qquad\times\psi_\hbar(w_1,z_1z_0^{-1})\,
\psi_\hbar(x_0,z_0)\,
\psi_\hbar(w_2,z_2z_0^{-1})\,
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_5 \=
\left(\!\!
\begin{array}{ccccc|c}
 \frac{{z_1}+{z_2}-z_1z_2}{({z_1}-1) ({z_2}-1)}&
 0 & 0& -1 & -1 & 0 \\
 0& \frac{z_1}{(1-{z_1})z_2} & 1 & -1 & 0 & 0 \\
 0& 1 & \frac{z_2}{(1-{z_2})z_1} & 0 & -1 & 0 \\
 -1 & -1 & 0 & 0 &0 & -{\mathbf Q_1^*} \\
 -1 & 0 & -1 & 0 & 0 & -{\mathbf Q_2^*} \\
 \hline
 0 & 0 & 0 &-{\mathbf Q_1^*}^t & -{\mathbf Q_2^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
By applying the first quad move from Theorem \ref{thm.fourier} to both
$\psi_\hbar(w_1,z_1z_0^{-1})$ and $\psi_\hbar(w_2,z_2z_0^{-1})$
 we obtain with new integration variables $y_1$ and $y_2$ that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_6 \rangle_{(y_1,y_2,x_0,w_1,w_2, x_1, x_2,x^*),
\mathbf \Lambda_6}
\eea
where
\begin{align*}
I_6 &\= \exp\Big(-\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-(x_1+x_2) \frac {\hsqrt}{2}\\
&\qquad\qquad+
\Big(y_1+\frac{w_1z_1z_0^{-1}}{1-z_1z_0^{-1}}\Big)\frac{\hsqrt}{2}
+\Big(y_2+\frac{w_2z_2z_0^{-1}}{1-z_2z_0^{-1}}\Big)\frac{\hsqrt}{2}\Big)
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)\\
&\qquad\times
\psi_\hbar\Big(y_1+\frac{w_1z_1z_0^{-1}}{1-z_1z_0^{-1}},
\frac 1 {1-z_1z_0^{-1}}\Big)\,
\psi_\hbar\Big(y_2+\frac{w_2z_2z_0^{-1}}{1-z_2z_0^{-1}},
\frac 1 {1-z_2z_0^{-1}}\Big)\,
\psi_\hbar(x_0,z_0)
\end{align*}
and
\[
\mathbf \Lambda_6 \=
\left(\!\!
\begin{array}{ccccccc|c}
 \frac{(z_1-1)z_2}{z_1} & 0 & 0 &0 &0 &0 &0 &0 \\
 0 & \frac{(z_2-1)z_1}{z_2} & 0 & 0 &0 &0 &0 &0\\
 0 & 0 & \frac{{z_1}+{z_2}-z_1z_2}{({z_1}-1) ({z_2}-1)}&
 0 & 0& -1 & -1 & 0 \\
 0 & 0& 0& \frac{z_1}{(1-{z_1})z_2} & 1 & -1 & 0 & 0 \\
 0&0&0& 1 & \frac{z_2}{(1-{z_2})z_1} & 0 & -1 & 0 \\
 0&0&-1 & -1 & 0 & 0 &0 & -{\mathbf Q_1^*} \\
 0&0&-1 & 0 & -1 & 0 & 0 & -{\mathbf Q_2^*} \\
 \hline
 0&0&0 & 0 & 0 &
 -{\mathbf Q_1^*}^t & -{\mathbf Q_2^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]
We change variables $y_1\mapsto y_1-w_1\frac{z_1z_0^{-1}}{1-z_1z_0^{-1}}$
and $y_2\mapsto y_2-w_2\frac{z_2z_0^{-1}}{1-z_2z_0^{-1}}$ using
Lemma \ref{lem.ff1} to obtain that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_7 \rangle_{(y_1,y_2,x_0,w_1,w_2, x_1, x_2,x^*),
\mathbf \Lambda_7}
\eea
where
\begin{align*}
I_7 &\= \exp\Big(-\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
-\frac{\hsqrt}2 x^t
(\mathbf B^{-1}\boldsymbol{\nu}-1)
-(x_1+x_2) \frac {\hsqrt}{2}
+(y_1+y_2)\frac{\hsqrt}{2}\Big)\\
&\qquad\times\psi_\hbar\Big(y_1,
\frac 1 {1-z_1z_0^{-1}}\Big)\,
\psi_\hbar\Big(y_2,
\frac 1 {1-z_2z_0^{-1}}\Big)\,
\psi_\hbar(x_0,z_0)\,
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_7 \=
\left(\!\!
\begin{array}{ccccccc|c}
 \frac{(z_1-1)z_2}{z_1} & 0 & 0 &1 &0 &0 &0 &0 \\
 0 & \frac{(z_2-1)z_1}{z_2} & 0 & 0 &1 &0 &0 &0\\
 0 & 0 & \frac{{z_1}+{z_2}-z_1z_2}{({z_1}-1) ({z_2}-1)}&
 0 & 0& -1 & -1 & 0 \\
 1 & 0& 0& 0 & 1 & -1 & 0 & 0 \\
 0&1&0& 1 & 0 & 0 & -1 & 0 \\
 0&0&-1 & -1 & 0 & 0 &0 & -{\mathbf Q_1^*} \\
 0&0&-1 & 0 & -1 & 0 & 0 & -{\mathbf Q_2^*} \\
 \hline
 0&0&0 & 0 & 0 &
 -{\mathbf Q_1^*}^t & -{\mathbf Q_2^*}^t & {z^*}'-{\mathbf Q^*} \\
\end{array}
\!\!\right).
\]





























































































Therefore, we can apply Fubini's Theorem (Lemma~\ref{lem.ff1}) with the
integration variables $w_1,w_2,x_1,x_2$,
to obtain that
\bea
\Phi^{\Xi}(\hbar) \=
\langle I_8 \rangle_{(y_1,y_2,x_0,x^*),
\mathbf \Lambda_8}
\eea
where
\begin{align*}
I_8 &\= \exp\Big(-\frac{\hbar}{4}(\mathbf B^{-1}\boldsymbol{\nu})_1
(\mathbf B^{-1}\boldsymbol{\nu})_2-\frac{\hbar}{24}
+\frac\hbar8 \mathbf f^t \mathbf B^{-1} \mathbf A \mathbf f
+\frac{\hsqrt}2\big(
x_0\left((\mathbf B^{-1}\boldsymbol{\nu})_1
 +(\mathbf B^{-1}\boldsymbol{\nu})_2\right)\big)\\
&\qquad\qquad\quad
-\frac{\hsqrt}2y_1\left((\mathbf B^{-1}\boldsymbol{\nu})_1-1\right)
-\frac{\hsqrt}2y_2\left((\mathbf B^{-1}\boldsymbol{\nu})_2-1\right)\\
&\qquad\qquad\quad
-\frac{\hsqrt}2{x^*}^t\left((\mathbf B^{-1}\boldsymbol{\nu})^*-
 (\mathbf B^{-1}\boldsymbol{\nu})_2\mbfQ_1^*
 -(\mathbf B^{-1}\boldsymbol{\nu})_1\mbfQ_2^*-1\right)\Big)\\
&\qquad\times\psi_\hbar\Big(y_1,
\frac 1 {1-z_1z_0^{-1}}\Big)\,
\psi_\hbar\Big(y_2,
\frac 1 {1-z_2z_0^{-1}}\Big)\,
\psi_\hbar(x_0,z_0)\,
\prod_{j=1}^{N} \psi_{\hbar}( x_j^*, z_j^*)
\end{align*}
and
\[
\mathbf \Lambda_8 \=
\left(\!\!
\begin{array}{ccc|c}
 \frac{({z_1}-1) {z_2}}{{z_1}} & 0 & -1 & -{\mbfQ_1^*} \\
 0 & \frac{({z_2}-1){z_1} }{{z_2}} & -1 & -{\mbfQ_2^*} \\
 -1 & -1 & \frac{{z_1}+{z_2}-z_2z_2}{({z_1}-1) ({z_2}-1)}+2 &
   {\mbfQ_1^*}+{\mbfQ_2^*} \\
   \hline
 -{\mbfQ_1^*}^t & -{\mbfQ_2^*}^t & {\mbfQ_1^*}^t+{\mbfQ_2^*}^t &
-{\mbfQ^*}+ {\mbfQ_1^*} {\mbfQ_2^*} + {\mbfQ_2^*} {\mbfQ_1^*}
\end{array}
\!\!\right).
\]
Using Lemma~\ref{lem.23.c2}, we obtain with respect to the integration variables
$\tilde x = (x_0,y_1,y_2,x^*)$ and some $c\in\frac 1 {24}\Z$ that
\bea
\Phi^{\Xi}(\hbar) \=
e^{c\hbar}\langle I_9 \rangle_{\tilde x, \mathbf \Lambda_9}
\eea
where with $\widetilde{\mathbf A}, \widetilde{\mathbf B}$ and
$\widetilde{\boldsymbol{\nu}}$ as in Equation~\eqref{manyAB.c2} and
\bea
I_9 \= \exp\Big(\frac\hbar8 \widetilde{\mathbf f}^t \widetilde{\mathbf B}^{-1}
\widetilde{\mathbf A} \widetilde{\mathbf f}
-\frac{\hsqrt}2 \tilde x^t(\widetilde {\mathbf B}^{-1}
\widetilde{\boldsymbol{\nu}}-1)\Big)\,
\prod_{j=0}^{N+2} \psi_{\hbar}( \widetilde{x}_j^*, \widetilde{z}_j^*)
\eea
and
\bea
\mathbf \Lambda_9





&\=\diag(\widetilde z_0',\,\widetilde z_1'',\,
\widetilde z_2'',\,\widetilde{z}^*{}')
- {\widetilde {\mathbf B}}^{-1}\widetilde {\mathbf A}.\\
\eea








\end{proof}

\begin{lemma}
\label{lem.23.c2}
With the notation used in the proof of the previous Proposition~\ref{prop.case2}
we have $\mbfQ_{11} = \mbfQ_{12} =\mbfQ_{22} = 0$ and
the following equalities: 
\begin{align}
\label{eq.c3.bia}
 \widetilde {\mathbf B}^{-1} \widetilde {\mathbf A} &\=
 \left(\!\!\begin{array}{ccc|c}
-1 & 1 & 1 & -\mbfQ_1^*-\mbfQ_2^*\\
1 & 0 & 0 & \mbfQ_1^*\\
1 & 0 & 0 & \mbfQ_2^*\\
\hline
-{\mbfQ_1^*}^t-{\mbfQ_2^*}^t & {\mbfQ_1^*}^t& {\mbfQ_2^*}^t &
\mbfQ^*-{\mbfQ_1^*}^t{\mbfQ_2^*}-{\mbfQ_2^*}^t{\mbfQ_1^*}
 \end{array}\!\!\right),\\\label{eq.c3.binu}
 \widetilde {\mathbf B}^{-1} \widetilde {\boldsymbol{\nu}} &\=
 \left(\!\!\begin{array}{c}
 -({\mathbf B}^{-1}\boldsymbol{\nu})_1
 -({\mathbf B}^{-1}\boldsymbol{\nu})_2+1\\
 ({\mathbf B}^{-1}\boldsymbol{\nu})_1\\
 {(\mathbf B}^{-1}\boldsymbol{\nu})_2\\
 ({\mathbf B}^{-1}\boldsymbol{\nu})^*
 -({\mathbf B}^{-1}\boldsymbol{\nu})_1\mbfQ_2^*
 -({\mathbf B}^{-1}\boldsymbol{\nu})_2\mbfQ_1^*
 \end{array}\!\!\right),\\\label{eq.c3.ff2}
\widetilde{\mathbf{f}}^{t}\widetilde {\mathbf B}^{-1}\widetilde{\boldsymbol{\nu}}
&\= \mathbf{f}^{t}\mathbf{B}^{-1}\boldsymbol{\nu}+\widetilde{f}_0-2
({\mathbf B}^{-1}\boldsymbol{\nu})_1({\mathbf B}^{-1}\boldsymbol{\nu})_2\,.
\end{align}
\end{lemma}

\begin{proof}
The relation $\mathbf B^{-1} \mathbf A = \mathbf Q$ and the fact that the
columns of $(a_1\,|\,a_2\,|\,b_*)$ are linearly independent imply
that $\mbfQ_{11} = \mbfQ_{12} =\mbfQ_{22} = 0$. We will prove
Equation~\eqref{eq.c3.bia} by showing the identity after multiplying by the
invertible matrix $\widetilde{\mathbf B}$.
For \eqref{eq.c3.bia} we compute
\bea[]
&\left(\!\!\begin{array}{ccc|c}
 -1 & -1 & -1 & 0\\
 0 & a_1-b_1-b_2 & a_2-b_1-b_2 & b_*
\end{array}\!\!\right)
 \left(\!\!\begin{array}{ccc|c}
-1 & 1 & 1 & -\mbfQ_1^*-\mbfQ_2^*\\
1 & 0 & 0 & \mbfQ_1^*\\
1 & 0 & 0 & \mbfQ_2^*\\
\hline
-{\mbfQ_1^*}^t-{\mbfQ_2^*}^t & {\mbfQ_1^*}^t& {\mbfQ_2^*}^t &
\mbfQ^*-{\mbfQ_1^*}^t{\mbfQ_2^*}-{\mbfQ_2^*}^t{\mbfQ_1^*}
 \end{array}\!\!\right)\\
&\=\left(\!\!
\begin{array}{ccc|c}
-1 & -1 & -1 & {0}\\
\hline
 \substack{a_1+a_2-2b_1-2b_2\\-b_*{\mbfQ_1^*}^t-b_*{\mbfQ_2^*}^t}&
{b_*{\mbfQ_1^*}^t} &
{b_*{\mbfQ_2^*}^t} &
\substack{(a_1-b_1){\mbfQ_1^*}^t + (a_2-b_2){\mbfQ_2^*}^t\\
- b_2{\mbfQ_1^*}^t - b_1{\mbfQ_2^*}^t
+b_*{\mbfQ^*}-b_*{\mbfQ_1^*}^t{\mbfQ_2^*} - b_*{\mbfQ_2^*}^t{\mbfQ_1^*}}
\end{array}
\!\!\right)\\
&\= \widetilde{\mathbf{A}}.
\eea
For Equation~\eqref{eq.c3.binu}, we compute
\bea[]
&\left(\!\!\begin{array}{ccc|c}
-1& -1& -1& 0\\
0 & a_1-b_1-b_2 & a_2-b_1-b_2 & b_*
\end{array}\!\!\right) \left(\!\!\begin{array}{c}
 -( {\mathbf B}^{-1}\boldsymbol{\nu})_1
 -( {\mathbf B}^{-1}\boldsymbol{\nu})_2+1\\
 ( {\mathbf B}^{-1}\boldsymbol{\nu})_1\\
 ( {\mathbf B}^{-1}\boldsymbol{\nu})_2\\
 ( {\mathbf B}^{-1}\boldsymbol{\nu})^{*}
 -( {\mathbf B}^{-1}\boldsymbol{\nu})_1\mbfQ_2^*
 -( {\mathbf B}^{-1}\boldsymbol{\nu})_2\mbfQ_1^*
 \end{array}\!\!\right)\\
 &\=\left(\!\!\begin{array}{c}
 -1\\ \boldsymbol\nu
 \end{array}\!\!\right)\,.



\eea
For Equation~\eqref{eq.c3.ff2}, we note that for $i=1,2$ we have
\be
\widetilde{\mathbf{f}}^{*}{}^t\mbfQ_i^*
\=
(\widetilde {\mathbf B}^{-1}\widetilde{\boldsymbol{\nu}})_i
-\widetilde{\mathbf{f}}_0-\widetilde{\mathbf{f}}_i''
\ee
and so
\be
\begin{small}
\begin{aligned}
\widetilde{\mathbf{f}}^{t}\widetilde {\mathbf B}^{-1}\widetilde{\boldsymbol{\nu}}
\=
\widetilde{f}_0+
(\widetilde{f}_1'+\widetilde{f}_2)({\mathbf B}^{-1}\boldsymbol{\nu})_1
+(\widetilde{f}_1+\widetilde{f}_2')({\mathbf B}^{-1}\boldsymbol{\nu})_2
+\widetilde{f}^{*}{}^t({\mathbf B}^{-1}\boldsymbol{\nu})^{*}
-2({\mathbf B}^{-1}\boldsymbol{\nu})_1({\mathbf B}^{-1}\boldsymbol{\nu})_2
\end{aligned}
\end{small}
\ee
Then, using the analogous relations between the flattening as given in
Equation~\eqref{eq.23sr} for the shapes, we have
$\widetilde{f}_1'+\widetilde{f}_2=f_1'=\mathbf{f}_1$ and
$\widetilde{f}_1+\widetilde{f}_2'=f_2'=\mathbf{f}_2$.
\end{proof}





\section{\texorpdfstring{The series of the simplest hyperbolic $4_1$ knot}{The series of the simplest hyperbolic 4\_1 knot}}
\label{sec.41}

In this section, we discuss an effective computation of the power series
$\Phi^{\Xi}(\hbar)$ for the simplest hyperbolic knot, namely the $4_1$ knot.
This example was studied extensively in~\cite{DG}. From~\cite[Ex. 2.6]{DG},
we obtain that the NZ datum $\Xi_{4_1}$ is given by
\be
A\=
\begin{pmatrix}
2 & 2\\
1 & 1
\end{pmatrix},\quad
B\=
\begin{pmatrix}
1 & 1\\
1 & 0
\end{pmatrix},\quad
\nu\=
\begin{pmatrix}
2\\
1
\end{pmatrix},\quad
f\=
\begin{pmatrix}
0\\
1
\end{pmatrix},\quad
f''\=
\begin{pmatrix}
0\\
0
\end{pmatrix},\quad
\ee
and $z_1=z_2=\z_6=e^{2\pi i/6}$. Therefore, we have
\be
\Phi^{\Xi_{4_1}}(\hbar) \= e^{\frac{\hbar}{8}}
\langle
\psi_{\hb}(x_1,\z_6)\psi_{\hb}(x_2,\z_6)\rangle_{(x_1,x_2),
\Lambda_0}\,,
\ee
where
\be
\Lambda_0
\=
\begin{pmatrix}
\z_6-1 & -1\\
-1 & \z_6-1
\end{pmatrix}\,.
\ee
This is a two dimensional formal Gaussian integral which can be simplified. 
Using $\z_6=1/(1-\z_6)=1-\z_6^{-1}$ and applying a change of coordinates
$x_1\mapsto x_1-\z_6x_2$, we find that
\be
\Phi^{\Xi_{4_1}}(\hbar) \= e^{\frac{\hbar}{8}}
\langle
\psi_{\hb}(x_1-\z_6x_2,\z_6)\psi_{\hb}(x_2,\z_6)\rangle_{(x_1,x_2),
\Lambda_1}\,,
\ee
where
\be
\Lambda_1
\=
\begin{pmatrix}
\z_6-1 & 0\\
0 & 2\z_6-1
\end{pmatrix}\,.
\ee
We can apply Fubini's theorem~\cite[Prop.2.13]{AarhusII} and
Corollary~\ref{cor.fourier} to perform the integral over $x_1$. After
renaming the variable $x_2$ by $x$, we express $\Phi^{\Xi_{4_1}}(\hbar)$ by a
one-dimensional formal Gaussian integral
\be
\label{eq.phi41.1d}
\Phi^{\Xi_{4_1}}(\hbar) \= e^{\frac{\hbar}{6}}
\Big\langle
\exp\Big(\frac{x}{2}\hbar^{\frac{1}{2}}\Big)\psi_{\hb}(x,\z_6)^2\Big\rangle_{x,
2\z_6-1}\,.
\ee
Using the definition of $\psi_\hbar$ from Equation~\eqref{psih} and expanding
to $O(\hbar^{5/2})$, we obtain that
\be
\begin{small}
\begin{aligned}
&\exp\Big(\frac{x}{2}\hbar^{\frac{1}{2}}\Big)\psi_{\hb}(x,\z_6)^2\\
&\=
1
+\bigg(\frac{1}{3}x^3 + \Big(\z_6 - \frac{1}{2}\Big)x\bigg)\hbar^{1/2}
+\bigg(\frac{1}{18}x^6 + \Big(\frac{1}{2}\z_6 - \frac{1}{4}\Big)x^4
- \frac{7}{8}x^2 + \Big(-\frac{1}{6}\z_6 + \frac{1}{6}\Big)\bigg)\hbar\\
&\qquad+ \bigg(\frac{1}{162}x^9 + \Big(\frac{1}{9}\z_6 - \frac{1}{18}\Big)x^7
- \frac{1}{2}x^5 + \Big(-\frac{73}{72}\z_6 + \frac{77}{144}\Big)x^3
+ \Big(\frac{1}{12}\z_6 + \frac{1}{4}\Big)x\bigg)\hbar^{3/2}\\
&\qquad+ \bigg(\frac{1}{1944}x^{12} + \Big(\frac{5}{324}\z_6
- \frac{5}{648}\Big)x^{10} - \frac{37}{288}x^8 + \Big(-\frac{1337}{2160}\z_6
+ \frac{1357}{4320}\Big)x^6\\
&\qquad+ \Big(\frac{1}{24}\z_6 + \frac{1027}{1152}\Big)x^4
+ \Big(\frac{23}{48}\z_6 - \frac{5}{16}\Big)x^2
- \frac{1}{72}\z_6\bigg)\hbar^{2}+O(\hbar^{5/2})\,.
\end{aligned}
\end{small}
\ee
Noting that $2\z_6-1=\sqrt{-3}$, we can then evaluate Equation~\eqref{eq.phi41.1d}
with Equation~\eqref{formalG1} to obtain that
\be
e^{-\frac{\hbar}{4}}\Phi^{\Xi_{4_1}}(\hbar) \=
1 + \frac{11}{72\sqrt{-3}}\hbar + \frac{697}{2(72\sqrt{-3})^2}\hbar^{2}+O(\hbar^{4})\,.
\ee
This is in agreement with computations in~\cite{DG,DGLZ,GZ:kashaev}.
The one-dimensional formal Gaussian integral~\eqref{eq.phi41.1d} gives an effective
computation of the series $\Phi^{\Xi_{4_1}}(\hbar)$.




Indeed, using a \texttt{pari-gp} program one can compute one
hundred coefficients in a few seconds and two hundred coefficients in a few minutes,
the first few of them are given by
\be
\begin{tiny}
\begin{aligned}
&e^{-\frac{\hbar}{4}}\Phi^{\Xi_{4_1}}(\hbar)\\
&=\;
1
- \frac{11}{216}\sqrt{-3}\,\hbar - \frac{697}{31104}\hbar^2
+ \frac{724351}{100776960}\sqrt{-3}\,\hbar^3
+ \frac{278392949}{29023764480}\hbar^4
- \frac{244284791741}{43883931893760}\sqrt{-3}\,\hbar^5\\
&\qquad- \frac{1140363907117019}{94789292890521600}\hbar^6
+ \frac{212114205337147471}{20474487264352665600}\sqrt{-3}\,\hbar^7
+ \frac{367362844229968131557}{11793304664267135385600}\hbar^8\\
&\qquad- \frac{44921192873529779078383921}{1260940134703442115428352000}\sqrt{-3}\,
\hbar^9
- \frac{3174342130562495575602143407}{23109593741473993679123251200}\hbar^{10}
+O(\hbar^{11})\,.
\end{aligned}
\end{tiny}
\ee
Similar to the case of the $4_1$, one can obtain one-dimensional formal Gaussian
integrals for the next two simplest hyperbolic knots, the $5_2$ and the
$(-2,3,7)$-pretzel knot, whose details we omit.



\newpage

\addcontentsline{toc}{section}{Acknowledgements}
\noindent \textbf{Acknowledgements.} The authors wish to thank Don Zagier for enlightening conversations.
The work of M.S. and C.W. has been supported by the Max-Planck-Gesellschaft.
C.W. wishes to thank the Southern University of Science and Technology's
International Center for Mathematics in
Shenzhen for their hospitality where the paper was completed.
