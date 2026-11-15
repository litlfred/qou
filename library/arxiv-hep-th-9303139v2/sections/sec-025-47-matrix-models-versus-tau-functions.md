---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-025-47-matrix-models-versus-tau-functions
section_title: "Matrix models versus $\tau$-functions."
section_number: 4.7
pages: 99-104
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.969
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
We are now prepared to return to our main subject and discuss integrability
properties of eigenvalue matrix models. The claim is that partition functions
of all these models, when considered as functions of time-variables
(parametrizing the shapes of  potentials) are in fact $\tau$-functions of
(perhaps, multicomponent) Toda-lattice and/or KP type. (Interesting
non-eigenvalue models are believed to be related to integrable systems of more
general type, not restricted to level $k=1$ Kac-Moody algebras.)

Partition functions are, however, not generic Toda or KP $\tau$-functions:
first, they usually belong to some reduced hierarchies, second, the relevent
operators $G$ (points of Grassmannian) are restricted to stay in peculiar
domains of the universal module space, specified by "string equations". String
equation is in fact nothing but the set of Ward-identities (Virasoro or
$W$-constraints in the examples under investigation), which are now
interpreted as equations on $G$. The very possibility of such interpretation
is highly non-trivial and reflects some deep relation between the constraints
and integrable structure. In the case of Virasoro constraints this is not a
puzzle, because Virasoro algebra is a symmetry (covariance) of the hierarchy,
the situation with other constraints is less clear (see the footnote at
section 4.3). In fact, when applied to a $\tau$-function of appropriately
reduced hierarchy, the infinitely many constraints usually become dependent
and it is enough to impose only the lowest Virasoro constraint $L_{-1}\tau =
0$
(or ${\cal L}_{-p}\tau = 0$, where $p$ is the degree of reduction), in order
to recover the entire set \cite{FKN}. It is this lowest constraint (or rather
its $t_1$-derivative, $\frac{\partial}{\partial t_1}(L_{-1}\tau) = 0$) that
traditionally carries the name of "string equation". It is often much simpler
to deduce than the entire set of identites, what is important in
practical applications (especially because determinant formulas, which imply
integrability, can  be also simpler to find in some situations than
the Ward identities).

In order to give a complete description of some sort of (matrix) models
from the point of view of integrability theory
it is enough to specify the hierarchy, to which it belongs (if partition
function is interpreted as $\tau$-function,
\be
Z_{\rm model}\{t\} = \tau \{t \mid G_{\rm model}\}
\ee
and the string equation which serves to fix operator $G$ - the point in the
universal module space.\footnote{
As we argued in the Introduction and in section 2.1, the word "matrix" can be
probably omited if generic Lagrangians are considered in other models of
quantum field theory. Also the universal module space (where moduli are - of
bundles over {\it spectral} Riemann surfaces)  can (and should) be
treated as a "space of theories". It is one of the great puzzles (and
beauties) of string theory, that Riemann surfaces appear both in the
world-sheet and spectral "dimensions". See \cite{GLM} for more discussion on
this issue.} After that it becomes an internal (yet unsolved) problem of
integrability theory to explain, what is so special about the set of points
$\{G_{\rm model}\}$ in this space. (We shall touch this problem in the next
subsection, devoted to Kac-Schwarz operators.) Alternatively, if there is
nothing special, it is an (unsolved) problem of matrix model theory to find
models, associated with {\it any} points $G$ in the universal module space (or
explain what is an obstacle, if any).

We proceed now to description of particular matrix models from this point of
view. As everywhere in these notes we consider only the most important classes
of scalar-product, conformal (multicomponent) and Generalized Kontsevich
models (GKM). All other examples (like models of complex, orthogonal, unitary
etc matrices) can be included into consideration with more or less effort
(see \cite{MMMM} and \cite{Bowick} for the cases of complex and unitary models
respectively), but they do not add much for the general theory that we are now
considering. String equations will be discussed in the next subsection.

{\it Scalar-product models}. These were exhaustively discussed in sections
3.5-3.7. We remind that all conventional multimatrix models (with inter-matrix
interaction of the form $\exp ({\rm Tr} H^{(\alpha)}H^{(\alpha+1)})$ belong to
this class. The crucial formulas are:
\be
Z_N &= {\rm Det}_N {\cal H}_{ij}^f = {\rm Det}_{0 \leq i,j \leq N-1}
{\cal H}_{ij}^f = \nn \\
&= {\rm Det}_{-N \leq i,j < 0}{\cal H}_{i+N,j+N}^f; \nn \\
{\cal H}_{ij}^f &= \frac{\partial^2}{\partial t_i\partial \bar t_j}
{\cal H}^f = \left(\frac{\partial}{\partial t_1}\right)^i
\left(\frac{\partial}{\partial \bar t_1}\right)^j {\cal H}^f.
\label{scapro1}
\ee
Here
\be
{\cal H}_{ij}^f = \langle h^i \mid \bar h^j\rangle =
\int d\hat\mu_{h,\bar h}e^{U(h)+\bar U(\bar h)} h^i\bar h^j.
\ee
Further,
\be
e^{U(h)} = e^{\sum_{k\geq 0} t_kh^k} = \sum_l h^lP_l(t); \nn \\
e^{\bar U(\bar h)} = e^{\sum_{k\geq 0}\bar t_k\bar h^k} =
\sum_m \bar h^mP_m(\bar t)
\ee
and thus
\be
{\cal H}_{ij}^f &= \sum_{l,m} \langle\langle h^{i+l}\mid \bar h^{j+m}\rangle
\rangle P_l(t)P_m(\bar t) =
\sum_{l,m} T_{lm}^f P_{l-i}(t)P_{m-j}(\bar t), \nn \\
T_{lm}^f &= \langle\langle h^{l}\mid \bar h^{m}\rangle\rangle,
\ee
where the
scalar product $\langle\langle \ \mid \ \rangle\rangle$ is w.r.to the measure
$d\hat\mu_{h,\bar h}$ (while $\langle \ \mid\ \rangle$ is w.r.to
$d\mu_{h,\bar h} = e^{U(h)+\bar U(\bar h)} d\hat\mu_{h,\bar h}$).

One would immediately recognize in these formulas
representation (\ref{todatau}) of Toda-lattice $\tau$-function,
be there no additional restriction that determinant in (\ref{scapro1}) is over
finite-dimensional $N\times N$ matrix (indices are constrained: $i,j\geq -N$).
This can be automatically taken into account if we require that
\be
T_{lm}^f = \infty \ \ {\rm for\ all}\ l,m<0,
\ee
and identify $Z_N$ as a  $\tau$-function $\tau^f$ of {\it forced}
Toda-lattice hierarchy (thus the supescript $f$ carried by ${\cal H}$ and $T$).
We conclude that partition functions of any scalar-product model is a
$\tau^f$-function of forced Toda-lattice hierarchy.

Let us now consider them as KP $\tau$-functions. This means that the $\bar
t$-dependence is simply ignored. However, $N$ will be preserved
explicitly as a parameter, labeling KP $\tau$-function.
After Miwa transformation $t_k = -\frac{1}{k}\sum_\gamma\lambda_\gamma^{-k} -
r_k$, described in section 3.7, we get:
\be
Z_N = \hat Z_N \frac{{\rm det}_{\gamma\delta}\hat
Q_{N+\gamma-1}(\lambda_\delta)}{\Delta(\lambda)},
\ee
where $\hat Q$ are orthogonal polinomials w.r.to the measure $d\hat\nu_{h,\bar
h} = e^{-\sum_k r_kh^k}d\hat\mu_{h,\bar h}$.
We conclude that in the framework of KP hierarchy the scalar-product models
are distinguished by the fact, that the corresponding
$\varphi_\gamma(\lambda)$ in (\ref{KPdetmain}) are {\it
polinomials} rather than infinite series in powers of $\lambda^{-1}$.


{\it 1-Matrix model}. This is particular example of scalar product model with
a {\it local} measure $d\mu_{h,\bar h} = e^{U(h)+\bar U(\bar h)}\delta(h-\bar
h)dhd\bar h$. In this case
\be
{\cal H}^f_{ij} = \langle h^i \mid \bar h^j \rangle =
\langle h^{i+j} \rangle = \frac{\partial}{\partial t_{i+j}}{\cal H}^f =
\left(\frac{\partial}{\partial t_1}\right)^{i+j}{\cal H}^f.
\ee
Thus in this case we deal with the (forced) Toda-chain reduction of
Toda-lattice hierarchy. In the end of this section 4 we use orthogonal
polinomials to present a detailed description of 1-matrix models  as
a Toda-chain $\tau$-function.

This model can be alternatively defined as Gaussian Kontsevich model: see
section 3.8. The fact that partition function is a $\tau$-function follows
then from the general statement for GKM, see below. The fact that it is
{\it forced} $\tau$-function is related to the property $c_{-N} = 0$,
mentioned at the end of s.3.8 (and proved in s.3.9). Also reduction to
Toda-chain hierarchy can be observed directly
in terms of GKM: see ref.\cite{Toda} for more details.


{\it Multicomponent (conformal) matrix models}. These are related to
multicomponent hierarchies, with $\tau$-functions representable as correlators
in multi-fermion systems. An example of determinant formula which substitutes
(\ref{todatau}) in the 2-component case, is given at the end of section 3.5,
where it is derived from consideration of the relevant matrix model
\cite{comamo}. For
derivation of the same determinant formula in the theory of $\tau$-functions
see ref.\cite{HOS}. Generic theory of multicomponent hierarchies is now making
its first steps and we do not review it in these notes. See \cite{Kavdl} for
the group-theory approach to the problem.


{\it Generalized Kontsevich model}. Determinant formulas for this case are
derived in Section 3.3. The most important expression is
\be
Z_V\{N,T\} = \frac{1}{({\rm det}\Lambda)^N}\frac{{\rm
det}_{\gamma\delta}\varphi_{\gamma+N}(\lambda_\delta)}{\Delta(\lambda)},
\label{gkmdet}
\ee
where
\be
\varphi_\gamma(\lambda) &= \frac{1}{\sqrt{2\pi}} e^{-\lambda V'(\lambda) +
V(\lambda)} \sqrt{V''(\lambda)} \int x^{\gamma-1}e^{-V(x) + V'(\lambda)x}dx =
\nn \\
&= \lambda^{\gamma-1}(1 + {\cal O}(\lambda^{-1}));
\label{gkmdet1}
\ee
and
\be
\varphi_\gamma(\lambda) = {\cal A}\varphi_{\gamma-1}(\lambda) =
{\cal A}^{\gamma-1}\Phi(\lambda).
\label{gkmKasch}
\ee
For $N=0$ this is just the representation, peculiar for KP $\tau$-function in
Miwa parametrization $T_k = \frac{1}{k}{\rm tr}\Lambda^{-k}$,
see eq.(\ref{KPdetmain}) above. Thus
\be
Z_V\{T\} = \tau^{KP}\{T \mid G_V\},
\ee
where it is operator $G$ (the point in Grassmannian) which depends on the
shape of potential $V(X)$. We also remind that the only way in which $Z$
depends on the size of the
matrix $n$ is through the {\it domain of variation} of the time variables $T$.
If (\ref{gkmdet}) is extended to full Toda-lattice $\tau$-function, by
introduction of negative times, we get \cite{Toda}:
\be
\new
\begin{array}{c}
Z_V\{T,N,\bar T\} =  \frac{{\cal C}_V^{-1}(\Lambda)}{({\rm det}\Lambda)^N}
e^{-\sum_{k>0}\bar T_k{\rm tr}\Lambda^{-k}} \times  \\
\times\int_{n\times n} dX ({\rm det}X)^N\exp\left( - {\rm tr}V(X) + {\rm
tr}\Lambda X +
\sum_{k>0} \bar T_k {\rm tr}X^{-k} \right)
\end{array}
\ee
When {\it this} extended partition function is considered as KP
$\tau$-function, we have instead of (\ref{gkmdet}):
\be
Z_V\{T,N,\bar T\} = \frac{1}{({\rm det}\Lambda)^N}\frac{{\rm
det}_{\gamma\delta}\varphi_{\gamma+N}^{\{\hat V\}}
(\lambda_\delta)}{\Delta(\lambda)},
\label{gkmdet2}
\ee
and relevant $\varphi$-functions are
\be
\varphi_{\gamma+N}^{\{\hat V\}}(\lambda)
&= \frac{1}{\sqrt{2\pi}} e^{-\lambda V'(\lambda) +
\hat V(\lambda)} \sqrt{V''(\lambda)} \int x^{\gamma-1}
e^{-\hat V(x) + V'(\lambda)x}dx =
\nn \\
&= \lambda^{N+\gamma-1}(1 + {\cal O}(\lambda^{-1})),
\ee
with
\be
\hat V(x) &\equiv V(x) - N\log x - \sum_{k>0}\bar T_kx^{-k}, \nn \\
V(x) &= \hat V_+(x)
\ee
(where $\hat V_+(x)$ is the positive-power fragment of Laurent series $\hat
V(x)$).
Functions $\varphi_\gamma(\lambda)$ in (\ref{gkmdet1}) are just equal to
$\displaystyle{
\left.\varphi_\gamma^{\{\hat V\}}(\lambda)\right|_{\bar T = 0}}$.
