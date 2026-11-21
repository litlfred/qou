---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-023-41-symmetrisation-and-a-residue-formula
section_title: "Symmetrisation and a residue formula"
section_number: 4.1
pages: 45-48
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.915
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
\label{sub.sym}

Elements of the usual Habiro ring $\calH_{\BZ}$ are extremely easy to write down.
For example, the ring $\BZ[q]$ is a subring of $\calH_{\BZ}$. This is not the case
for the Habiro ring of a number field, where $\calO[q]$ is no longer a subring
of $\calH_{\calO[1/\Delta]}$. One can construct
elements of these rings for certain presentations of a number field. In this section
we explain how to get formulas for such elements using combinatorial data. 

Fix a symmetric integer matrix $A$, and consider the following expression
\be
J_A(t,w,q)
\=
\sum_{n\in\BZ^N_{\geq0}}
\frac{(-q^{\frac{1}{2}})^{n^{\Tran}An}q^{\frac{1}{2}\diag(A)\cdot n}w^{An}
t^n}{(qw;q)_n}\,,
\ee
where $t^n=t_1^{n_1}\cdots t_N^{n_N}$ and
$(qw;q)_n=(qw_1;q)_{n_{1}}\cdots(qw_N;q)_{n_{N}}$.

We can expand this sum when $q=\z_m+x$
is near a root of unity $\z_m$ and obtain an element
of $\BZ[\z_m][w^{\pm1},(1-w)^{-1}]\llbracket t\rrbracket\llbracket x \rrbracket$.
In fact, it is not hard to see that 
\be
\label{Jwdef}
J_A(t,w,\z_m+x) \inn \BZ[\z_m][t,w_i^{\pm1},
(1-t_i^{m}P_i(w^{m}))^{-1} \, | \, i\=1,\dots,N]
\llbracket x\rrbracket\,,
\ee
where
\be
\label{ABge}
P_{i}(z)\= (-1)^{A_{ii}} (1-z_i)^{-1} \prod_{j=1}^N z_j^{A_{ij}},\qquad i=1,\dots,N\,.
\ee

We define the collection $\Psi_A(t,q) \= (\Psi_{A,m}(t,x))_{m \geq 1}$ by
\be
\label{psitmdef}
\Psi_{A,m}(t,x)
\=
\Res{w^{m}=z}
t^{-1/m}J_A(t^{1/m},w,\z_m+x)\,\frac{dw}{w}\,,
\ee
where the residue is taken over all $w^{m}=z$ and $z$ satisfies the equations
\be
\label{tpz}
t_i P_i(z)\=1, \qquad i\=1,\dots, N \,. 
\ee

The value at $\z_m$ is given by the manifestly integral formula
\be
\Psi_{A,m}(t,0)
\=
\frac{1}{\delta_A(t) m^N}
\sum_{w^m=z}
\sum_{n\in\BZ^{N}/m\BZ^{N}}
\frac{(-\z^{\frac{1}{2}})^{n^{\Tran}An}\z^{\frac{1}{2}\diag(A)\cdot n}w^{An}
t^n}{(qw;q)_n} 
\ee
with $\delta_A(t)$ as in~\eqref{dt}. 
The next theorem says in particular that this number is the same as the symmetrised
value $\Phitof_A^{\mathrm{sym}}(t,\z_m)=\Phitof_A(t,\z_m)\Phitof_A(t,\z_m^{-1})$, which
therefore is also integral.

\begin{theorem}
\label{thm.sym}
For every positive integer $m$ and $\Phitof_A$ of Theorem~\ref{thm.1} in
Section~\ref{sub.results}, we have
\be
\label{phipsi}
\Psi_A(t,q) \= \Phitof_A(t,q) \Phitof_A(t,q^{-1}) \inn
\BZ[\z_m][\![x]\!][\![t^{1/m}]\!], \qquad q\=\z_m+x \,.
\ee
\end{theorem}

\begin{proof}
The series $\Psi_A(t,q)$ and $\Phitof_A(t,q) \Phitof_A(t,q^{-1})$ are the specialisations
to $\mu=\nu=0$ of two families indexed by two integer vectors $\mu,\nu\in\BZ^{N}$ 
\be
\label{2Phi}
\begin{aligned}
\Phitof_{A,\mu,\nu}(t,q) & \= \Phitof_A(q^{m\mu}t,q) \Phitof_A(q^{-m\nu}t,q^{-1})\,,
\\
\Psi_{A,\mu,\nu}(t,q) & \= \Res{w^{m}=z}
q^{\nu}w^{\mu+\nu}t_1^{-1/m}\cdots t_N^{-1/m}J_A(q^{\mu}t^{1/m},w,\z_m+x)\,
\frac{dw}{w}\,.
\end{aligned}
\ee
Both families satisfy the same system of $q$-difference equations. In the
one-dimensional case (i.e. $N=1$), for $q=\z_m+x$ we have
\be
\label{eq:two.qdiffs}
\begin{aligned}
\Phitof_{A,\mu,\nu}(t,q)-\Phitof_{A,\mu+1,\nu}(t,q)
&\=
(-1)^{A}q^{A}t^{1/m}\Phitof_{A,\mu+A,\nu}(t,q)\,,\\
\Phitof_{A,\mu,\nu}(t,q)-\Phitof_{A,\mu,\nu+1}(t,q)
&\=
(-1)^{A}q^{-A}t^{1/m}\Phitof_{A,\mu,\nu+A}(t,q)\,,\\
\Phitof_{A,\mu,\nu}(q^mt,q)
&\=
\Phitof_{A,\mu+1,\nu-1}(t,q)\,.
\end{aligned}
\ee
To see that $\Psi_{A,\mu,\nu}(t,q)$ also satisfies these equations note
that
\be
\begin{aligned}
J_A(t,w,q)-wJ_A(qt,w,q)










&\=
-(1-w) +(-1)^Aq^{A}tw^{A} J_A(q^{A}t,w,q)\,,\\
(1-qw)J_A(t,w,q)










&\=
-(1-qw) +(-1)^{A}q^{-A}tq^{A}(qw)^{A}J_A(t,qw,q)\,.
\end{aligned}
\ee
Therefore after taking the residues with a change of variables in the RHS of the
second equation $qw\mapsto w$ we find that $\Psi_{A,\mu,\nu}(t,q)$ satisfies the
equations~\eqref{eq:two.qdiffs}. In both cases the solutions can be taken of the form
\be
\sum_{k=0}^{\infty} a_{\mu,\nu,k}(q)\,t^{k/m} \inn\BZ[\z_m][\![x]\!][\![t^{1/m}]\!]\,.
\ee
The $q$-difference equations imply that for
\be
\begin{aligned}
a_{\mu,\nu,k}-a_{\mu+1,\nu,k}
&\=
(-1)^{A}q^{A}a_{\mu+A,\nu,k-1}\,,\\
a_{\mu,\nu,k}-a_{\mu,\nu+1,k}
&\=
(-1)^{A}q^{-A}a_{\mu,\nu+A,k-1}\,,\\
q^ka_{\mu,\nu,k}
&\=
a_{\mu+1,\nu-1,k}\,,
\end{aligned}
\ee
where we set $a_{\mu,\nu,k}=0$ for $k<0$. This completely determines all $a_{\mu,\nu,k}$
from the value of~$a_{0,0,0}$. Notice that $\Phitof_{A,m}(0,q)\Phitof_{A,m}(0,q^{-1})=1$.
To see that $\Psi_{A,\mu,\nu}(0,q)$ also equals $1$, notice that only the coefficient
of $x^{0}$ contributes to the coefficient of $t^{0}$, because the residues of the
factors $(1-t_i^{m}P_i(w^{m}))^{-\ell}$ contribute at least one factor of $t$ when
$\ell>0$. Therefore an explicit computation leads to $\Psi_{A,m}(0,x)=1$.
\end{proof}

To get elements of the Habiro ring of a number field, we specialise to 
$t=1$ and assume that the equations~\eqref{tpz} define a reduced
zero-dimensional scheme over $\BQ$. Fix a solution $z$ of these equations
and denote the corresponding collection of power series by $\Psi_{A,\mu,\nu,z}(q)$.
A solution $z$ generates a number field $\BK$.
Combining Theorem~\ref{thm.1} of Section~\ref{sub.results}, Theorem~\ref{thm.sym}
and Theorem~\ref{thm.2} of Section~\ref{sub.results}, we obtain that
$\Psi_{A,\mu,\nu,z}(q) \in \calH_{R}$.

\begin{theorem}
\label{thm.desc}
For all $\mu, \nu \in \BZ^N$, we have $\Psi_{A,\mu,\nu,z}(q) \in \calH_R$.
\end{theorem}

Some cases of the above theorem were first proven in the thesis of Ferdinand Wagner.
Here is a concrete example for the cubic field of discriminant $-23$.



\begin{example}
\label{ex.23}
Consider the sum
\be
J(t,w,q)
\=
\sum_{k=0}^{\infty}
(-1)^{k}\frac{q^{3k(k+1)/2}w^{3k}t^k}{(qw;q)_{k}} \,.
\ee
Expanding $J(t,w,1+x)$ as a power series in $x$ and observing that each coefficient
is a sum of derivatives of geometric series in $t$, we find that
\be
\begin{small}
\begin{aligned}
J(t,w,1+x)
&\=
\frac{-1 + w}{-tw^3+w-1}
+\frac{3tw^3 - 5tw^4 + 2tw^5}{(-tw^3+w-1)^3}x \\
&+\frac{1}{(-tw^3+w-1)^5} \Big( 3tw^3 - 9tw^4 + 10tw^5 + (-21t^2 - 5t)w^6
+ (50t^2 + t)w^7 \\ &\qquad\qquad - 39t^2w^8 + (3t^3 + 10t^2)w^9
- 4t^3w^{10} + t^3w^{11} \Big) x^2
+O(x^3)
\end{aligned}
\end{small}
\ee
and
\be
\begin{aligned}
\Psi_{1}(t,x)
&\=
\frac{2tz^2 + 3tz - 9t}{27t-4}
+\frac{x^2}{(27t-4)^4}\big((-4374t^4 - 2106t^3 + 3t^2)z^2\\
&\qquad+ (-2187t^4 - 2997t^3 - 129t^2 + 2t)z
+ (2916t^3 + 1404t^2 - 2t)\big)
+\mathrm{O}(x^3) \,,
\end{aligned}
\ee
where $z$ satisfies the equation
\be
1-z\=-t z^3 \,.
\ee
Specialising to $t=1$ we find the expansion 
\be
\Psi_{1}(x)
\=
\frac{2z^2 + 3z - 9}{23}
+
\frac{-6477z^2 - 5311z + 4318}{23^4}x^2
+O(x^3)
\ee
of the element of the Habiro ring $R=\BZ[z,\tfrac{1}{23}]$, where $z^3-z+1=0$
generates the cubic field of discriminant $-23$.
Using
\be
  \delta\=-2t-\frac{t}{1-z}\=-tz^2 - tz + (-3t + 1)
\ee
one can compare these equations to equation~\eqref{fsymvals3} and
equation~\eqref{eq:ex.fsym.admis1}.


\end{example}



The next remark is for knot-theorists.

\begin{remark}
\label{rem.knots}
Use the matrices
\be
\label{3knots}
A_{4_1} \= \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix},
\qquad
A_{5_2} \= \begin{pmatrix} 2 & 1 & 1 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix},
\qquad
A_{(-2,3,7)} \=
\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 1 & 2 & 4 \end{pmatrix}
\ee
in Theorem~\ref{thm.2} of Section~\ref{sub.results} to compute the asymptotic
series $\Phitof^{(K)}(h)$ of the three simplest hyperbolic knots (for the $(-2,3,7)$
pretzel knot, the matrix was given in~\cite[Rem.A.5]{GZ:qseries}). To get the
asymptotic series of~\cite{DG} for any knot, one can use a triangulation of it
from \texttt{SnapPy}, choose quad types with Neumann--Zagier matrices
$(\mathbf A|\mathbf B)$ satisfying that $\mathbf B^{-1} \mathbf A$ is integral
(if this is possible) and apply Theorem~\ref{thm.2} of Section~\ref{sub.results}
with $A=\mathrm{I}- \mathbf B^{-1} \mathbf A$. 
\end{remark}
