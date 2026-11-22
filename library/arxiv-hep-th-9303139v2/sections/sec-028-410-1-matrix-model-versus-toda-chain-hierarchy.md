---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-028-410-1-matrix-model-versus-toda-chain-hierarchy
section_title: "1-Matrix model versus Toda-chain hierarchy"
section_number: 4.10
pages: 118-121
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.958
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
At the end of this section we use an explicit example of dicrete 1-matrix
model \cite{GMMMO} to illustrate, how a more familiar Lax description of
integrable hierarchies arises from determinant formulas. This example will be
also usefull in Section 5.3 below, when one of the ways to take double-scaling
continuum limit of the 1-matrix model will be discussed.
Lax representation appears usually after some coordinate system is chosen
in the Grassmannian. In the example which we are now considering this
system is introduced by the use of orthogonal polinomials.

We already know from section 3.6, that partition function of 1-matrix model
(which is a {\it one}-component model) is given by
\be
Z_N = \ {\rm Det}_{0 < i,j \leq N} \langle h^i\mid h^j\rangle\  =
\prod_{i=0}^{N-1} e^{\phi_i} = Z_1 \prod_{i=1}^{N-1} R_i^{N-i},
\ee
where the last two representations are in terms of the norms of orthogonal
polinomials
\be
\langle Q_n \mid Q_m \rangle = e^{\phi_n}\delta_{nm}
\label{orthocond}
\ee
 and parameter of the
3-term relation
\be
\new
\begin{array}{c}
hQ_n(h) = Q_{n+1}(h) + c_nQ_n(h) + R_nQ_{n-1}(h), \\
Z_1 = e^{\phi_0} = \langle 1 \mid 1 \rangle , \ \ \ \ R_n =
e^{\phi_n-\phi_{n-1}}.
\end{array}
\nn
\ee
Of course all the information is contained in the determinant formula together
with the rule, which defines time-dependence of
${\cal H}_{ij}^f = \langle h^i\mid h^j\rangle  = \hat{\cal H}_{i+j}^f$:
\be
\new
\begin{array}{c}
\frac{\partial {\cal H}_{ij}^f}{\partial t_k} =
 {\cal H}_{i+k,j}^f = {\cal H}_{i,j+k}^f ,\ \ {\rm or} \\
\frac{\partial \hat{\cal H}_i^f}{\partial t_k} =
 \hat{\cal H}_{i+k}^f.
\end{array}
\ee
(The possibility to express everything in terms of ${\cal H}_i^f$ with a single
matrix index $i$ is the feature of Toda-chain reduction of generic
Toda-lattice hierarchy.)

However, in order to reveal the standard Lax representation we need to go into
somewhat more involved considerations. Namely, we consider representation of
two operators in the basis of orthogonal polinomials. First,
\be
h^k Q_n(h) = \sum_{m=0}^{n+k}
\frac{\langle n \mid h^k \mid m \rangle}{\langle m \mid m \rangle}
Q_m(h) =
\sum_{m=0}^{n+k} \gamma_{nm}^{(k)}Q_m(h)
\ee
(here the simplified notation is introduced for
$\langle n \mid f(h) \mid m \rangle \equiv
\langle Q_n \mid f(h) \mid Q_m \rangle$ and
$\displaystyle{\gamma_{nm}^{(k)} \equiv
\frac{\langle n \mid h^k \mid m \rangle}{\langle m \mid m \rangle}}$.)
Second,
\be
\new
\begin{array}{c}
\frac{\partial Q_n(h)}{\partial t_k} =
-\sum_{m=0}^{n-1}
\frac{\langle n \mid h^k \mid m \rangle}{\langle m \mid m \rangle}
Q_m(h) =
-\sum_{m=0}^{n-1}\gamma_{nm}^{(k)}Q_m(h), \\
\frac{\partial \phi_n}{\partial t_k} =
\frac{\langle n \mid h^k \mid n \rangle}{\langle n \mid n \rangle}
= \gamma_{nn}^{(k)}.
\end{array}
\ee
(These last relations arise from differentiation of orthogonality condition
(\ref{orthocond}):
\be
\new
\begin{array}{c}
e^{\phi_n}\frac{\partial \phi_n}{\partial t_k}\delta_{nm} =
\frac{\partial \langle Q_n \mid Q_m \rangle}{\partial t_k} =
\nn \\
= \langle \frac{\partial Q_n}{\partial t_k} \mid Q_m \rangle +
\langle Q_n \mid \frac{\partial Q_m}{\partial t_k} \rangle +
\langle Q_n\mid h^k \mid Q_m \rangle
\end{array}
\ee
by looking at the cases of $m<n$ and $m=n$ respectively.)

{}From these relations one immediately derives the Lax-like formula:
\be
\frac{\partial \gamma_{nm}^{(k)}}{\partial t_q} =
- \sum_{l=m-k}^{n-1} \gamma_{nl}^{(q)}\gamma_{lm}^{(k)} +
\sum_{l=m+1}^{n+k} \gamma_{nl}^{(k)}\gamma_{lm}^{(q)}
\label{laxrep1mamo}
\ee
or, in a matrix form,
\be
\frac{\partial \gamma^{(k)}}{\partial t_q}
= [ R\gamma^{(q)}, \gamma^{(k)}],
\ee
where
\be
R\gamma_{mn}^{(k)} \equiv \left\{
\begin{array}{c}
-\gamma_{mn}^{(k)} \ \ {\rm if} \ m>n, \\
\gamma_{mn}^{(k)} \ \ {\rm if} \ m<n
\end{array}
\right.
\ee
(We remind that usually $R$-matrix acts on a function
$f(h) = \sum_{n = -\infty}^{+\infty}f_nh^n$ according to the rule:
$Rf(h) = \sum_{n\geq l}f_nh^n - \sum_{n<l}f_nh^n$ with some "level" $l$.)
These $\gamma^{(k)}$ are not symmetric matrices, but one can also rewrite all
the formulas above in terms of symmetric ones:
\be
{\cal L}_{mn}^{(k)} \equiv e^{\frac{1}{2}(\phi_n - \phi_m)}\gamma_{mn}^{(k)}
= \frac{\langle m \mid h^k \mid n \rangle}{\sqrt{\langle m \mid m \rangle
\langle n \mid n \rangle}}
\ee

{}From eqs.(\ref{laxrep1mamo}) one can easily deduce Toda-equations for
$\phi_n$:
\be
\new
\begin{array}{c}
\frac{\partial^2\phi_n}
{\partial t_k\partial t_l} = \frac{\partial}{\partial t_k}
\frac{\langle n \mid h^l \mid n \rangle}{\langle n \mid n \rangle}
=  \\
= \left( \sum_{m>n} - \sum_{m<n}\right)
\frac{\langle n \mid h^k \mid m \rangle \langle m \mid h^l \mid n \rangle}
{\langle m \mid m \rangle\langle n \mid n \rangle},
\end{array}
\ee
where the r.h.s. can be expressed in terms of $R_m = e^{\phi_m - \phi_{m-1}}$.
In particular,
\be
\frac{\partial^2\phi_n}{\partial t_1\partial t_1} =
R_{n+1} - R_n = e^{\phi_{n+1} - \phi_n} - e^{\phi_n - \phi_{n-1}}.
\ee

Let  us also mention that in this formalism the Ward identities (Virasoro
constraints) follow essentially from the relation
\be
\left( \frac{\partial}{\partial h}\right)^\dagger =
- \frac{\partial}{\partial h} -
\sum_{k>0} kt_k h^{k-1},
\ee
where Hermitean conjugation is w.r.to the scalar product $\langle\ \mid\
\rangle$. For example, this relation implies, that
\be
\langle Q_n \mid \frac{\partial Q_n}{\partial h} \rangle =
- \langle \frac{\partial Q_n}{\partial h} \mid Q_n \rangle
- \sum_{k>0} kt_k \langle Q_n \mid h^{k-1} \mid Q_n \rangle.
\ee
Now we note that $\frac{\partial Q_n}{\partial h}$ is a polinomial of
degree $n-1$, thus
${\langle Q_n \mid \frac{\partial Q_n}{\partial
h} \rangle = 0}$. (In fact $$\displaystyle{
\frac{\partial Q_n}{\partial h} = -\sum_{k>0} kt_k
\left(\sum_{m=0}^{n-1} \gamma_{nm}^{(k-1)}Q_m \right) =
-\sum_{k>0} kt_k \frac{\partial Q_n}{\partial t_{k-1}}}.)$$
Also we recall that $\langle Q_n \mid h^{k-1} \mid Q_n \rangle =
\langle Q_n \mid Q_n \rangle \frac{\partial \phi_n}{\partial t_{k-1}}$,
and obtain:
\be
\sum_{k>0} kt_k\frac{\partial \phi_n}{\partial t_{k-1}} = 0
\ee
for any $n$. This should be supplemented by relation
$\frac{\partial \phi_n}{\partial t_0} = \phi_n$. In order to get the lowest
Virasoro constraint (string equation), $L_{-1}Z_N = 0$ or $L_{-1}\log Z_N = 0$
it is enough just to sum over $n$ from $0$ to $N-1$.

For more details about 1-matrix model, Toda-chain hierarchy and application of
the formalism of orthogonal polinomials in this context see \cite{GMMMO}.

\












\bigskip
