---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-006-21-derivation-of-the-equations
section_title: "Derivation of the Equations"
section_number: 2.1
pages: 9-14
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.977
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
\label{subsec:derivation_pde}
A central role in the derivation of our equations is played by the
commutator identity
\begin{equation}
\left\lbrack L,\left(I-K\right)^{-1}\right\rbrack = \left(I-K\right)^{-1}
\left\lbrack L,K\right\rbrack \left(I-K\right)^{-1}
\label{CR_1}
\end{equation}
for any operators $K$ and $L$. Taking $L$ to be $D$ ($=d/dx$) or
$M$ (=multiplication by the independent variable) give two of the three
basic ingredients from which the equations are derived.  The third
is the equally simple fact that if $K$ depends upon a parameter $\alpha$
then
\begin{equation}
{d\over d\alpha} \left(I-K\right)^{-1} = -\left(I-K\right)^{-1}
{dK\over d\alpha} \left(I-K\right)^{-1} \, .
\label{dResolvent_dalpha}
\end{equation}
\par
It will be very useful for us to think of $K$ as acting not on $J$
but on $(-\infty,\infty)$ and to have kernel
\begin{equation}
K(x,y) \chiJ (y)
\label{K_char}
\end{equation}
where $\chiJ$ is the characteristic function of $J$.  We continue
to denote the resolvent kernel of $K$ by $R(x,y)$ but note that
while it is smooth in $x$ it is discontinuous at $y=a_j$.  Thus the
quantity $R(a_j,a_j)$ appearing in (\ref{dlog_tau}) must be
interpreted to mean
\[ \lim_{y\rightarrow a_j \atop y\in J} R(a_j,y); \]
similarly for $p_j$ and $q_j$ in (\ref{qp_defn}) and like quantities
appearing later.  The definitions of $u$ and $v$ must be modified
to read
\begin{equation}
u=\left(A\chiJ,\left(I-K\right)^{-1}A\right),\ \ \
v=\left(A\chiJ,\left(I-K\right)^{-1}A^\prime\right)\, .
\label{uv_defn2}
\end{equation}
Notice that since
\[ \left(I-K\right)^{-1} A = \left(I-K\right)^{-1} A \chiJ \ \ \
{\rm in }\  J
\]
this agrees with the original  definitions of $u$ and $v$
given  by (\ref{uv_defn}).
\par
We can think of $K$ as an operator taking smooth functions to smooth
functions and so the operators $KD$ and $DK$ make sense, the former
having distributional kernel.  The transpose operator $K^t$ takes
distributions to distributions.
\par
With these preliminaries out of the way we begin with the
derivation of the representations of the quantities $R(a_j,a_k)$
in terms of the $q_j$, $p_j$, $u$ and $v$.  We introduce
the notation
\begin{equation}
Q=\left(I-K\right)^{-1} A, \ \ \ P=\left(I-K\right)^{-1} A^\prime \, ,
\label{QP_defn}
\end{equation}
so that $q_j=Q(a_j)$, $p_j=P(a_j)$.  (For the moment we ignore
the dependence of $Q$ and $P$ on the parameter $a=(a_1,\cdots,a_{2m})$;
this will come later.)
\par
The first commutator relation we use is the simple
\[ \left\lbrack M,K \right\rbrack  \doteq \left( A(x) A^\prime(y)
-A^\prime(x) A(y) \right) \chiJ (y) \]
(where $\doteq$ means ``has kernel equal to'').  Hence from (\ref{CR_1})
with $L=M$
\begin{equation}
\left\lbrack M,\left(I-K\right)^{-1}\right\rbrack\doteq
Q(x) \left(I-K^t\right)^{-1} A^\prime \chiJ (y) - P(x) \left(I-K\right)^{-1}
A\chiJ (y)
\label{CR_2}
\end{equation}
(The transpose here arises from the general fact that if $L\doteq U(x) V(y) $,
then $T_1L T_2\doteq T_1 U(x)\>  T_2^t V(y)$.)\ \ If we use the fact
that
\begin{equation}
\left(I-K^t\right)^{-1} A \chiJ = \left(I-K\right)^{-1} A
\ \ \ {\rm on} \ J,
\label{transpose_rela}
\end{equation}
we deduce from (\ref{QP_defn}) and (\ref{CR_2})  that \cite{its90}
\begin{equation}
R(x,y) = {Q(x) P(y) - P(x) Q(y) \over x-y }
 \ \ \ \left(x,y\in J, x\neq y\right).
\label{R_QP}
\end{equation}
In particular, therefore,
\begin{eqnarray}
R(a_j,a_k)={q_j p_k - p_j q_k\over a_j-a_k} \ \ \ (j\neq k),
 \label{R_jk}  \\
R(a_j,a_j)=Q^\prime(a_j) p_j - P^\prime(a_j) q_j \ \ \
\left(^\prime={d\over dx}\right)\, .
\label{R_jj}
\end{eqnarray}
\par
To compute $Q^\prime(x)$ and $P^\prime(x)$ we consider first the
commutator $[D,K]$.  If an operator $L$ has distributional kernel
$L(x,y)$ then
\begin{equation}
\left\lbrack D,L\right\rbrack \doteq \left( {\partial\over\partial x}+
{\partial\over\partial y}\right) L(x,y)\, .
\label{CR_3}
\end{equation}
It is an easy verification, using the equation $A^{\prime\prime}(x)=x A(x)$,
that
\begin{equation}
\left( {\partial\over\partial x}+
{\partial\over\partial y}\right) K(x,y) = - A(x) A(y)
\label{partial_K}
\end{equation}
and so (recall the definition (\ref{K_char}) of the kernel of $K$)
\[
\left\lbrack D,K\right\rbrack \doteq - A(x)A(y)\chiJ (y)
-\sum_k (-1)^k K(x,a_k)\delta(y-a_k)\, .
\]
Hence, applying (\ref{CR_1}) with $L=D$ (and recalling definitions
(\ref{QP_defn})),
\begin{equation}
\left\lbrack D,\left(I-K\right)^{-1}\right\rbrack
=-Q(x) \left(I-K^t\right) A \chiJ (y) - \sum_k(-1)^k R(x,a_k)\rho(a_k,y)
\label{CR_5}
\end{equation}
where
\[ \rho(x,y)=\delta(x-y)+R(x,y)\]
is the distributional kernel of $(I-K)^{-1}$.
\par
We proceed with the computations of $Q^\prime(x)$ and $P^\prime(x)$.
Differentiating the first relation in (\ref{QP_defn}) and
using (\ref{CR_5}) give
\begin{eqnarray*}
Q^\prime&=& D(I-K)^{-1} A = P+\left\lbrack D,\left(I-K\right)^{-1}
\right\rbrack A \\
&=& P - Q\left(\left(I-K^t\right)^{-1}A\chiJ,A\right) -
\sum_k(-1)^k R(\cdot,a_k) q_k \, .
\end{eqnarray*}
Thus (recall (\ref{uv_defn2}))
\begin{equation}
Q^\prime(x)=P(x) - Q(x) u - \sum_k(-1)^k R(x,a_k) q_k\, .
\label{Q_deriv}
\end{equation}
\par
Similarly
\[ P^\prime = (I-K)^{-1} A^{\prime\prime} +
 \left\lbrack D,\left(I-K\right)^{-1}\right\rbrack A^\prime\, . \]
Since $A^{\prime\prime}(x)=xA(x)$ this is equal to
\[ M\left(I-K\right)^{-1} A - \left\lbrack M,\left(I-K\right)^{-1}\right
\rbrack A +\left\lbrack D,\left(I-K\right)^{-1}\right\rbrack A^\prime\, . \]
We now use formula (\ref{CR_2}) and (\ref{CR_5}) to deduce that
\begin{equation}
P^\prime(x)=x Q(x) - 2 Q(x) v + P(x) u - \sum_k (-1)^k R(x,a_k) p_k \, .
\label{P_deriv}
\end{equation}
Setting $x=a_j$ in ({\ref{Q_deriv}) and (\ref{P_deriv}) and using
(\ref{R_jj}) give
\[ R(a_j,a_j)=p_j^2-a_j q_j^2 +2 q_j^2 v - 2 p_j q_j u
+\sum_k (-1)^k R(a_j,a_k) (q_j p_k - p_j q_k)\, .
\]
In view of (\ref{R_jk}) this is precisely equation (\ref{airy_7}).
\par
Most of the work is already done and we can derive the equations
(\ref{airy_1})--(\ref{airy_6}) very quickly.  First, we have the
easy fact
\[ {\partial\over\partial a_k} K\doteq (-1)^k K(x,a_k)\delta(y-a_k) \]
and so by (\ref{dResolvent_dalpha})
\begin{equation}
{\partial\over \partial a_k} \left(I-K\right)^{-1} \doteq
(-1)^k R(x,a_k) \rho(y-a_k) \, .
\label{dR2}
\end{equation}
At this point we must keep in mind that $Q$ and $P$ are functions
of $a$ as well, and so we denote them now by $Q(x,a)$ and
$P(x,a)$, respectively.  We deduce immediately from (\ref{dR2})
and the definitions (\ref{QP_defn}) that
\begin{equation}
{\partial\over\partial a_k} Q(x,a) = (-1)^k R(x,a_k) q_k, \ \ \
{\partial\over\partial a_k} P(x,a) = (-1)^k R(x,a_k) p_k\, .
\label{dQP}
\end{equation}
Since $q_j=Q(a_j,a)$ and $p_j=P(a_j,a)$ this gives
\[ {\partial q_j\over \partial a_k}= (-1)^k R(a_j,a_k) q_k ,\ \ \
{\partial p_j\over \partial a_k}= (-1)^k R(a_j,a_k) p_k \ \ \ (j\neq k).\]
In view of (\ref{R_jk}) these are equations (\ref{airy_1}) and
(\ref{airy_2}).  Moreover
\[ {\partial q_j\over \partial a_j}=\left( {\partial\over \partial x}+
{\partial\over \partial a_j}\right)Q(x,a)\biggr\vert_{x=a_j}\ ,
\ \ \ \
 {\partial p_j\over \partial a_j}=\left( {\partial\over \partial x}+
{\partial\over \partial a_j}\right)P(x,a)\biggr\vert_{x=a_j} \]
and (\ref{dQP}), (\ref{Q_deriv}) and (\ref{P_deriv}) give
\begin{eqnarray*}
{\partial q_j\over \partial a_j}&=& p_j - q_j u -
 \sum_{k\neq j} (-1)^k R(a_j,a_k)
q_k\, ,  \\
{\partial p_j\over \partial a_j}&=& a_jq_j-2q_j v +p_j u - \sum_{k\neq j}
(-1)^k R(a_j,a_k) p_k \, .
\end{eqnarray*}
In view of (\ref{R_jk}) again, these are equations (\ref{airy_3})
and (\ref{airy_4}).
\par
Finally, using the definition of $u$ in (\ref{uv_defn2}), the fact
\[ {\partial\over \partial a_j}\chiJ (y)=(-1)^j\delta(y-a_j)\, ,\]
and (\ref{dR2}) we find that
\[ {\partial u\over \partial a_j}=(-1)^j A(a_j) q_j +
(-1)^j \left(A\chiJ,R(\cdot,a_j)\right) q_j\, .\]
But
\[\left(A\chiJ,R(\cdot,a_j)\right) = \int_J R(x,a_j) A(x)\, dx
=\int_J R(a_j,x) A(x)\, dx \]
since $R(x,y)=R(y,x)$ for $x,y\in J$.  Since $R(y,x)=0$ for
$x\not\in J$ the last integral equals
\[ \int_{-\infty}^\infty R(a_j,x) A(x)\, dx = A(a_j) - q_j\, . \]
Thus
\[ {\partial u\over \partial a_j}= (-1)^j q_j^2\, ,\]
which is (\ref{airy_5}).  Equation (\ref{airy_6}) is derived
analogously.
\par
We end this section with two relations between $u$, $v$, the $q_j$
and the $p_j$ which in fact can be used to represent $u$ and $v$
directly in terms of the $q_j$ and $p_j$.  These relations are
\begin{eqnarray}
2v - u^2 &= &\sum_j (-1)^j q_j^2\, , \label{uv_1}\\
u&=& -\sum_j\left(p_j^2-a_j q_j^2-2p_jq_j u +2q_j^2 v\right) \, .
\label{uv_2}
\end{eqnarray}
\par
To obtain the first of these observe that (\ref{airy_1}) and
(\ref{airy_3}) imply
\begin{equation}
\left(\sum_k{\partial\over\partial a_k}\right) q_j = p_j-q_j u
\label{uv_3}
\end{equation}
while from (\ref{airy_5}) and (\ref{airy_6})
\[
{\partial\over\partial a_j}\left(2v-u^2\right)=
2(-1)^j q_j\left(p_j-q_j u\right)\, .
\]
Hence if we multiply both sides of (\ref{uv_3}) by $2(-1)^j q_j$
and sum over $j$ we obtain
\[
\left(\sum_k {\partial\over\partial a_k}\right) \left(
\sum_j (-1)^j q_j^2\right) = \left(\sum_k {\partial\over\partial a_k}\right)
\left(2v-u^2\right)\, .
 \]
It follows that the two sides of (\ref{uv_1}) differ by a function
of $(a_1,\cdots,a_{2m})$ which is invariant under translation by
any vector $(s,\cdots,s)$.  Since, clearly, both sides tend to zero
as all $a_i\rightarrow\infty$, their difference must be identically
zero.
\par
To deduce (\ref{uv_2}) we add
(\ref{CR_5}) and (\ref{dR2}) to obtain
\[ \left( {\partial\over\partial x}+{\partial\over\partial y}+
\sum_k {\partial\over\partial a_k}\right) R(x,y) = -Q(x) Q(y)
\ \ \ (x,y\in J).\]
(Observe that the kernel of $[D,(I-K)^{-1}]$ is
$(\partial/\partial x + \partial/\partial y ) R(x,y)$.)\ \
Hence
\[ \left(\sum_k {\partial\over\partial a_k}\right) R(a_j,a_j)
= -q_j^2=-(-1)^j {\partial u\over\partial a_j}\, , \]
the last by (\ref{airy_5}).  Multiplying by $(-1)^j$ and summing
over $j$ gives
\[ \left(\sum_k {\partial\over\partial a_k}\right)
\left(\sum_j(-1)^j R(a_j,a_j)\right) = -\left(\sum_k {\partial\over
\partial a_k}\right) u\, .\]
{}From this we deduce, by an argument similar to the one at the
end of the last paragraph, that
\begin{equation}
\sum_j(-1)^j R(a_j,a_j) = -u\, .
\label{uv_5}
\end{equation}
If we substitute formula (\ref{airy_7}) into this we see that the
resulting double sum vanishes and we are left with (\ref{uv_2}).
