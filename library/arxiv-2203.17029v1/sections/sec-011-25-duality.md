---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q -HOLONOMIC MODULES"
section_id: sec-011-25-duality
section_title: "Duality"
section_number: 2.5
pages: 20-23
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.968
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
\label{sub.duality}















In this section we review some elementary facts about duality of $q$-holonomic modules.
Recall that we can write the linear $q$-difference equation
\be
\label{af}
a_r(t,q) f(q^r t, q) + a_{r-1}(t,q) f(q^{r-1}t,q) + \dots + a_0(t,q) f(t,q) =0 
\ee
for a function $f(t,q)$ in matrix form $\s X = A X$ where
$X=X_f=(f, \s f, \dots, \s^{r-1} f)^t$ is a column vector and
$A=\comp(-a_0/a_r, \dots, -a_{r-1}/a_r)$ is the companion matrix where
{\small
\be
\label{comp}


\comp(c_0,c_1,\dots,c_{r-1}) =
\begin{pmatrix}
0 & 1 & 0 & \dots & 0\\
0 & 0 & 1 & \dots & 0\\
: & : & : & \dots & :\\
0 & 0 & 0 & \dots & 1\\
c_0 & c_1 & c_2 & \dots
& c_{r-1} 
\end{pmatrix} \,.
\ee
}
We will also write~\eqref{af} in operator form $L f=0$ where
$L=\sum_{j=0}^r a_j \s^{r-j} \in \calW$ and denote by $M_f=\calW f$ the corresponding
module over the $q$-Weyl algebra $\calW$. The module $M_f$ has two duals.
The first one is defined by
\be
\label{Mdual1}
M_{f}^{\wedge}=M_{f^{\wedge}}, \qquad f^{\wedge}(t,q)=f(t,q^{-1}) 
\ee
which in matrix form is given by
\be
\label{Awedge}
\s X_{f^{\wedge}} = A^{\wedge} X_{f^{\wedge}}, \qquad
A^{\wedge}(t,q) = A(qt,q^{-1})^{-1} \,.
\ee
Indeed, we have
\begin{equation*}
a_r(t,q^{-1}) f^{\wedge}(q^{-r} t, q) + a_{r-1}(t,q^{-1})
f^{\wedge}(q^{-r+1}t,q) + \dots + a_0(t,q^{-1}) f^{\wedge}(t,q) =0 
\end{equation*}
and inverting $a_{r}$, we obtain that
\begin{equation*}
f^{\wedge}(qt,q)
=
-\frac{ a_{r}(qt,q^{-1})}{ a_{0}(qt,q^{-1})}f^{\wedge}(q^{1-r}t,q)
- \frac{ a_{r-1}(qt,q^{-1})}{ a_{0}(qt,q^{-1})}f^{\wedge}(t,q)
-\dots
-\frac{ a_{1}(qt,q^{-1})}{ a_{0}(qt,q^{-1})}f^{\wedge}(t,q)
\end{equation*}
which implies~\eqref{Awedge}. The second dual module is defined by
\be
\label{Mdual2}
M_{f}^{\vee}
=
\mathrm{Hom}_{\BQ(q)[t^{\pm 1}]}(M_{f},\BQ(q)[t^{\pm 1}]) 
\ee
with a basis $f^{\vee}_{i}$ for $i=0,\dots r-1$ such that for $j=0,\dots,r-1$ we have
$f^{\vee}_{i}(\sigma^{j}f)=\delta_{i,j}$. We claim that in matrix form, this
dual module is given by
\be
\label{Avee}
\s X_{f^{\vee}} = A^{\vee} X_{f^{\vee}}, \qquad
A^{\vee}(t,q) = (A(t,q)^{-1})^t \,.
\ee
Indeed, using the basis $f^{\vee}$, we can define an action of $\calW$ on
$M_{f}^{\vee}$ via conjugation with $\sigma$. By definition, the action satisfies
$\sigma(\lambda(v)) = (\sigma\cdot\lambda)(\sigma v)$ for $\lambda\in M_{f}^{\vee}$
and $v\in M_{f}$. In particular we have
$\sigma\cdot f_{i}^{\vee} = \sigma f_{i}^{\vee}\sigma^{-1}$. 
Notice that for $i,j=0,\dots,r-1$
\begin{equation*}
\begin{aligned}
(\sigma\cdot f_{i}^{\vee})(\sigma^{j}f)
&=
(\sigma f_{i}^{\vee})(\sigma^{j-1}f)
=
(\sigma f_{i}^{\vee})\left(\sum_{k=0}^{r-1}(A(q^{-1}t,q)^{-1})_{jk}\sigma^{k}f\right)
\\ &=
\sigma\left(\sum_{k=0}^{r-1}(A(q^{-1}t,q)^{-1})_{jk}\delta_{ik}\right)

= (A(t,q)^{-1})_{ji}
= \left(\sum_{k=0}^{r-1}(A(t,q)^{-t})_{ik}f^{\vee}_{k}\right)(\sigma^{j}f)
\end{aligned}
\end{equation*}
which implies~\eqref{Avee}.

Recall that if two modules with companion matrices $A$ and $B$ are isomorphic,
there exists a change of basis $P$ such that
\be
B
=
(\s P) A P^{-1} \,.
\ee
Then taking
\be
\begin{tiny}
\begin{aligned}
  P^{\vee}(t,q)
  =
  \begin{pmatrix}
    1 & 0 & 0 & \dots & 0\\
    a_{1}/a_0 & 1 & 0 & \dots & 0\\
    a_{2}/a_0 & \s(a_{1}/a_0) & 1 & \dots & 0\\
    : & : & : & \dots & :\\
    a_{r-1}/a_0 & \s(a_{r-2}/a_0) & \s(a_{r-3}/a_0) & \dots & 1\\
  \end{pmatrix}, \qquad
  P^{\wedge}(t,q)
  =
  \begin{pmatrix}
    0 & 0 & \dots & 0 & 1\\
    0 & 0 & \dots & 1 & 0\\
    : & : & \dots & : & :\\
    0 & 1 & \dots & 0 & 0\\
    1 & 0 & \dots & 0 & 0\\
  \end{pmatrix}
\end{aligned}
\end{tiny}
\ee
we find that
\be
\begin{aligned}
  (\s P^{\vee})^{-1}A^{\vee}P^{\vee}
  &=\comp(-a_r/a_0,\s(a_{r-1}/a_0), \dots, \s^{r}(a_{1}/a_0))\\
  (\s P^{\vee})^{-1}A^{\vee}P^{\vee}
  &=\comp\left(-\frac{a_r(qt,q^{-1})}{a_0(qt,q^{-1})},
    \frac{a_{r-1}(qt,q^{-1})}{a_0(qt,q^{-1})}, \dots,
    \frac{a_{1}(qt,q^{-1})}{a_0(qt,q^{-1})}\right)\,.
\end{aligned}
\ee

We now remark an elementary relation between fundamental solutions of
inhomogeneous linear $q$-difference equations and their corresponding
homogeneous ones. Consider the inhomogeneous equation
\be
 a_{0}(t,q)f(t,q)+\dots+ a_{r-1}(t,q)f(q^{r-1}t,q)+f(q^{r}t,q)=c_{0}(q).
\ee
We can write it either in the form $\s X_{f^{(in)}} = A^{(in)} X_{f^{(in)}}$
with 
{\tiny
  \begin{equation*}
   X_{f^{(in)}}
=
\begin{pmatrix}
1\\
f \\
:\\
\s^{r-1} f
\end{pmatrix},
\qquad
A^{(in)}
=
\begin{pmatrix}
1 & 0 & 0 & 0 & \dots & 0\\
0 & 0 & 1 & 0 & \dots & 0\\
0 & 0 & 0 & 1 & \dots & 0\\
: & : & : & : & \dots & :\\
0 & 0 & 0 & 0 & \dots & 1\\
c_{0} & - a_{0} & - a_{1} & - a_{2} & \dots & - a_{r-1}
\end{pmatrix}
\end{equation*}
}

\noindent
or in the form $\s X = A X$ with
{\small
$$
X_f=(f, \s f, \dots \s^r f)^t, \qquad 
A=\comp(- a_{0} , \s a_{0}- a_{1} , \s a_{1}- a_{2} , \dots ,
\s a_{r-2}- a_{r-1} , \s a_{r-1}-1) \,.
$$
}





















The two equations are related by 
$X_f = P X_{f^{(in)}}, \,\,\, A=\s P A^{(in)} P^{-1}$
where
$$
P=\comp(c_{0} , - a_{0} , - a_{1} , - a_{2} , \dots , - a_{r-1}) \,.
$$













We end this subsection by discussing the duality
\be
M^{\vee} \cong M^{\wedge}
\ee
which follows from (but is not equivalent to) the existence of matrices
$P^{\vee},P^{\wedge} \in GL_r(\BQ(t,q))$ such that
\be
\s P^{\wedge} A^{\wedge} (P^{\wedge})^{-1}
=
\s P^{\vee} A^{\vee} (P^{\vee})^{-1}
\ee
is a companion matrix. For the $q$-holonomic modules that come from Chern-Simons
theory, the duality $M \mapsto M^{\wedge}$ corresponds to orientation-reversal of
the ambient 3-manifold. On the other hand, the factorisation of the Andersen--Kashaev
state integrals into elements of $M$ and $M^{\wedge}$ suggests that in those
examples, we have $M^{\wedge}\cong M^{\vee}$. The following proposition
confirms this for the case of the $4_1$ knot. 

\begin{proposition}
\label{prop.M41duals}
The $q$-difference module $M$ associated to Equation~\eqref{41x1} satisfies
\be
  M
  \cong
  M^{\wedge}
  \cong
  M^{\vee} \,.
  \ee
The fundamental matrices satisfy
\be
\begin{aligned}
  U(t,\lambda,q)
  &=
  P^{\wedge}(t,q)
  U^{\wedge}(t,\lambda,q)
  =
  P^{\vee}(t,q)
  U^{\vee}(t,\lambda,q)
  \begin{pmatrix}
    0 & -1\\
    1 & 0
  \end{pmatrix}\,,\\
  V(t,q)
  &=
  P^{\wedge}(t,q)
  V^{\wedge}(t,q)
  =
  P^{\vee}(t,q)
  V^{\vee}(t,q)
  \begin{pmatrix}
    0 & -1\\
    1 & 0
  \end{pmatrix}
\end{aligned}
\ee
with
\be
\label{Pvw}
P^{\wedge}(t,q)
  =
  \begin{pmatrix}
1 & 0\\
2q^{-1}-t^{-1}q^{-1} & -q^{-2}
  \end{pmatrix}
  ,\quad
  P^{\vee}(t,q)
  =
  \begin{pmatrix}
0 & -q^{-1}t^{-2}\\
q^{-1}t^{-2} & 0
  \end{pmatrix} 
\ee
and cocycle $\Om$ of $M$ satisfies
  \be
  \label{quadrel}
  \Om = (P^{\wedge}|_{\kappa}\gamma) \Om^{\wedge}(P^{\wedge})^{-1}
  = (P^{\vee}|_{\kappa}\gamma) \Om^{\vee} (P^{\vee})^{-1} \,.
  \ee
\end{proposition}

Equation~\eqref{quadrel} was called ``quadratic relations'' in Section 3.3 and
equations (68)-(70) of~\cite{GZ:kashaev}. An example of a self-dual module is the
generalised $q$-hypergeometric equation (see Equation~\eqref{heine.selfdual.Ueq}
below). 

\begin{proof}
With $A$, given in Equation~\eqref{comp.mat.41.x1}, and the gauge transformations
~\eqref{Pvw}, we have
\be
A(t,q)
=
P^{\wedge}(qt,q)A^{\wedge}(t,q)P^{\wedge}(t,q)^{-1}
=
P^{\vee}(qt,q)A^{\vee}(t,q)P^{\vee}(t,q)^{-1}.
\ee
\end{proof}
The extra symmetry with $M \cong M^{\wedge}$ comes from the fact the $4_{1}$ knot
is amphichiral. However, this symmetry does not persist to the
module associated to the inhomogeneous equation. This can again be seen from
the state integrals introduced in \cite{GGMW:trivial} whose integrand lacks
the symmetry the Andersen-Kashaev state integrals have.

\begin{proposition}
\label{41inhom.not.sd}
The $q$-difference module $M^{\vee}$ associated to Equation~\eqref{41x1inhom}
is not isomorphic to $M^{\wedge}$. 
\end{proposition}

\begin{proof}
The companion matrices of $M$ and $M^{\wedge}$ are given by
\be
  A^{\wedge}(t,q)
  =
  \begin{pmatrix}
1 & 0 & 0\\
q^{-1}t^{-1} & 2q^{-1}-t^{-1}q^{-1} & -q^{-2}\\
0 & 1 & 0
  \end{pmatrix},
  \quad
  A^{\vee}(t,q)
  =
  \begin{pmatrix}
1 & t^{-1} & 0\\
0 & 2q-t^{-1} & 1\\
0 & -q^{2} & 0
  \end{pmatrix} \,.
\ee
If there was an isomorphism there would exist $P(t,q) \in \GL_3(\BQ(t,q))$
such that
\be
  P(qt,q)A^{\vee}(t,q)=A^{\wedge}(t,q)P(t,q) \,.
\ee
It follows that   
\be
\label{P1111}
  P_{1,1}(qt,q)=P_{1,1}(t,q), \qquad
  P_{1,2}(qt,q)=P_{1,3}(t,q),
\ee
which then implies
\be
  tP_{1,2}(t,q)+(1-2tq)P_{1,2}(qt,q)+q^2tP_{1,2}(q^2t,q)=P_{1,1}(qt,q).
\ee
Since $P_{1,1}\in\BQ(t,q)$ satisfies~\eqref{P1111}, it is independent of $t$,
i.e., $P_{1,1}(t,q)=P_{1,1}(q)$. Therefore, $P_{1,2}$ would be a $P_{1,1}(q)$
multiple of a $\BQ(t,q)$-valued solution to Equation~\eqref{41x1inhom}. The
only such solution is zero, thus $P_{1,1}=P_{1,2}=0$ which, together with~\eqref{P1111}
gives also $P_{1,3}=0$, which violates the fact that $P$ is invertible.
\end{proof}
