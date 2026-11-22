---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-023-45-toda-lattice-tau-function-and-linear-reductio
section_title: "Toda-lattice $\tau$-function and linear reductions of Toda hierarchy"
section_number: 4.5
pages: 87-92
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.964
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
In the previous subsection we derived a formula
\be
\tau_N\{t,\bar t\mid G\} = \left.{\rm Det}\right._{i,j<0} {\cal H}_{i+N,j+N}
\label{todatau}
\ee
for the basic correlator, which defines
"Toda-lattice $\tau$-function". For obvious reasons $\bar t$ are often refered
to as negative-times. $\tau$-function
can be normalized by dividing over the same
quantity for all time-variables vanishing, but this is not always convenient.
Eq.(\ref{todatau}) has generalizations - when similar
matrix elements in a multifermion system is considered - this leads to
"multicomponent Toda" (or AKNS) $\tau$-functions. Generalizations to
arbitrary conformal models should be considered as well. It has also particular
"reductions", of which the most important are: KP (Kadomtsev-Petviashvili),
forced (semi-infinite) and Toda-chain $\tau$-functions.
This is the subject to be discussed in this subsection.

Idea of linear reduction is that the form of operator $G$, or, what is
the same, of
the matrix $T_{lm} $ in eq.(\ref{HversTlm}), can be adjusted in such a way,
that $\tau_N\{t,\bar t\mid G\}$ becomes independent of some variables, i.e.
equation(s)
\be
\left(\sum_k \alpha\frac{\partial}{\partial t_k} +
 \sum_k \bar\alpha\frac{\partial}{\partial \bar t_k} +
\sum_k \beta_k D_N(k) + \gamma \right) \tau_N\{t,\bar t\mid G\} = 0
\label{redtotau1}
\ee
can be solved as equations for $G$ for all the values of $t,\bar t$ and $N$ at
once. (In (\ref{redtotau1}) $D_N(k)f_N \equiv f_{N+k} - f_N$.)
In this case the system of integrable equations (hierarchy), arising from
Hirota equation for $\tau$, gets reduced and one usually speaks about "reduced
hierarchy". Usually equation (\ref{redtotau1}) is imposed directly on matrix
${\cal H}_{ij}$, of course than (\ref{redtotau1}) is just a corollary.

We shall refer to the situation when (\ref{redtotau1}) is fulfilled for {\it
any} $t, \bar t, N$  as to "strong reduction". It is often reasonable to
consider also "weak reductions", when (\ref{redtotau1}) is satisfied on
particular infinite-dimensional hyperplanes in the space of time-variables.
Weak reduction is usually a property of entire $\tau$-function as well, but
not expressible in the from of a local linear equation, satisfied identicall
for {\it all} values of $t, \bar t, N$.
Now we proceed to concrete examples:

{\it Toda-chain hierarchy}. This is a {\it strong} reduction. The
corresponding constraint (\ref{redtotau1}) is just
\be
\frac{\partial {\cal H}_{ij}}{\partial t_k} = \frac{\partial {\cal
H}_{ij}}{\partial \bar t_k},
\ee
or, because of (\ref{todaeqforH}), ${\cal H}_{i+k,j} = {\cal H}_{i,j+k}$.
It has an obvious solution:
\be
{\cal H}_{i,j} = \hat{\cal H}_{i+j},
\ee
i.e. ${\cal H}_{ij}$ is expressed in terms of a one-index quantity $\hat{\cal
H}_i$. It is, however, not enough to say, what are restrictions on ${\cal
H}_{ij}$ - they should be fulfiled for all $t$ and $ \bar t$ at once, i.e.
should be resolvable as equations for $T_{lm}$. In the case under
consideration this is simple: $T_{lm}$ should be such that
\be
T_{lm} = \hat T_{l+m}.
\ee
Indeed, then
\be
&{\cal H}_{ij} = \sum_{l,m} T_{lm} P_{l-i}(t) P_{m-j}(\bar t) =
\sum_{l,m} \hat T_{l+m} P_{l-i}(t)P_{m-j}(\bar t) = \nn \\
&= \sum_{n\geq 0} \hat T_{n+i+j} \left(\sum_{k=0}^n P_k(t)P_{n-k}(\bar
t)\right),
\nn
\ee
and
\be
\hat{\cal H}_i = \sum_{n\geq 0} \hat T_{n+i} \left(\sum_{k=0}^n
P_k(t)P_{n-k}(\bar t)\right).
\label{todachainH}
\ee

{\it Volterra hierarchy}. Toda-chain $\tau$-function can be further {\it
weakly}
reduced to satisfy the identity
\be
\left.\frac{\partial \tau_{2N}}{\partial t_{2k+1}}\right|
_{\{t_{2l+1}=0\}}  = 0, \ \ \ {\rm for\ all}\ k,
\label{volterrared}
\ee
i.e. $\tau_{2N}$ is requested to be even function of all odd-times $t_{2l+1}$
(this is an example of "global characterization" of the weak reduction).
Note that (\ref{volterrared}) is imposed only on {\it Toda-chain}
$\tau$-function with {\it even} values of zero-time. Then (\ref{volterrared})
will hold whenever $\hat{\cal H}_i$ in (\ref{todachainH}) are even (odd)
functions of $t_{\rm odd}$ for even (odd) values of $i$. Since Shur
polinomials $P_k(t)$ are even (odd) functions of odd-times for even (odd) $k$,
it is enough that the sum in (\ref{todachainH}) goes over even (odd) $n$
when $i$ is even (odd). In other words, the restriction on $T_{lm}$ is that
\be
T_{lm} = \hat T_{l+m}, \ \ \ {\rm and} \ \ \ \hat T_{2k+1} = 0 \ \ {\rm for\
all}\ k.
\ee


{\it Forced hierarchies}. This is another important example of strong
reduction. It also provides an example of {\it singular}
$\tau$-functions,
arising when $G = \exp \left(\sum A_{mn}\psi_m\tilde\psi_n\right)$
blows up and normal ordered operators should be used to define
regularized
$\tau$-functions. Forced hierarchy appears when $G$ can be
represented in the form \cite{KMMOZ}  $G = G_0P_+$, where
projection operator $P_+$ is such that
\be
P_+ \mid N \rangle = \mid N \rangle \ \ {\rm for}\ N\geq N_0,
\nn \\
P_+ \mid N \rangle = 0 \ \ {\rm for}\ N < N_0.
\label{Pplus}
\ee
Explicit expression for this operator is\footnote{
Normal ordering sign $\ : \ \ :\ $ means that all operators
$\tilde\psi$ stand to the {\it left} of all operators $\psi$.
The product at the r.h.s. obviously implies both the property
(\ref{Pplus}) and projection property $P_+^2 = P_+$.
}
\be
P_+ = \ :\exp \left( - \sum_{l<N_0} \tilde\psi_l\psi_l\right): \ =
\prod_{l<N_0} (1 - \tilde\psi_l\psi_l) =
\prod_{l < N_0} \psi_l\tilde\psi_l.
\nn
\ee
Because of (\ref{Pplus}), $P_+\mid -\infty \rangle = )$, and
the identity $G\mid -\infty \rangle = \mid -\infty \rangle$,
which was essentially used in the derivation in (4.27), can be
satisfied only if $G_0$ is singular and $T_{lm} = \infty$.
In order to avoid this problem one usually introduces in the
vicinity of such
singular points in the universal module space a sort of normalized
(forced) $\tau$-function $\tau_N^f \equiv \frac{\tau_N}{\tau_{N_0}}$.
One can check that now $T^f_{lm} = \infty$ for all $l,m < N_0$, and
$\tau^f$ can be represented as determinant of a final-dimensional
matrix \cite{UT},\cite{KMMOZ}:
\be
&\tau_N^f = {\rm Det}_{N_0\leq i,j < N} {\cal H}^f_{ij}\ \ \ {\rm for}\ \
N>N_0;
\nn \\
&\tau_{N_0}^f = 1; \nn \\
&\tau_{N}^f = 0\ \ \ {\rm for }\ \ N < N_0.
\ee
For $N>N_0$ we have now determinant of a {\it finite}-dimensional
$(N-N_0)\times (N-N_0)$ matrix.






The choice of $N_0$ is not really essential, therefore it is better to put
$N_0 = 0$ in order to
simplify formulas, phraising  and relation with the discrete matrix models
($N_0$ is easily restored if everywhere $N$ is substituted by $N-N_0$).
For forced hierarchies one can also represent $\hat\tau$ as
\be
\tau_N^f = {\rm Det}_{0\leq i,j < N}
\partial_1^i\bar\partial_1^j {\cal H}^f,
\ee
where ${\cal H}^f = {\cal H}^f_{00}$ and $\partial_1 = \frac{\partial}{\partial
t_1}$, $\bar \partial_1 = \frac{\partial}{\partial \bar t_1}$. For
{\it forced Toda-chain} hierarchy this turns into even simpler expression:
\be
\tau_N^f = {\rm Det}_{0\leq i,j < N} \partial_1^{i+j}\hat{\cal H}^f,
\ee
while for the {\it forced Volterra} case we get a product of two Toda-chain
$\tau$-functions with twice as small value of $N$ \cite{Bowick}:
\be
\tau_{2N}^f &= \left({\rm Det}_{0\leq i,j < N} \partial_2^{i+j}\hat{\cal
H}^f\right) \cdot
       \left( {\rm Det}_{0\leq i,j < N} \partial_2^{i+j} (\partial_2
\hat{\cal H}^f)\right) = \nn \\
&= \tau_N^f[\hat{\cal H}^f]\cdot \tau_N^f[\partial_2\hat{\cal H}^f].
\ee

Forced $\tau^f_N$ can be {\it always} represented in the form of a
scalar-product matrix model. Indeed,
\be
{\cal H}_{ij} = \sum T_{lm}P_{l-i}(t)P_{m-j}(\bar t) =
\oint\oint e^{U(h)+\bar U(\bar h)} h^i\bar h^j T(h,\bar h) dhd\bar h,
\ee
where $T(h,\bar h) \equiv \sum_{lm} T_{lm} h^{-l-1}\bar h^{-m-1}$, and
$e^{U(h)} = e^{\sum_{k>0}t_kh^k} = \sum_{l\geq 0} h^lP_l(t)$.
Then, since ${\rm Det}_{0\leq i,j < N}h^i = \Delta_N(h)$ - this is where it
is essential that the hierarchy is forced -
\be
{\rm Det}_{0\leq i,j < N} {\cal H}_{ij} = \prod_i
\oint\oint e^{U(h_i)+\bar U(\bar h_i)}
T(h_i,\bar h_i)dh_id\bar h_i
\cdot \Delta_N(h)\Delta_N(\bar h),
\ee
i.e. we obtain a scalar-product model with
\be
d\mu_{h,\bar h} = e^{U(h)+\bar U(\bar h)}T(h,\bar h) dhd\bar h.
\ee
Inverse is also true: partition function of every scalar-product model is
forced Toda-lattice $\tau$-function - see section 4.7 for more details.

{\it KP hierarchy}.  In this case we just ignore the  dependence of
$\tau$-function on times $\bar t$. Every Toda-lattice $\tau$-function can be
considered also as KP $\tau$-function: just operator $G^{KP} \equiv Ge^{\bar
H}$ (a point of Grassmannian) becomes $\bar t$-dependent. Usually
$N$-dependence is also eliminated - this can be considered as a little more
sophisticated change of $G$. When $N$ is fixed, extra changes of
field-variables are allowed, including transformation from Ramond to
Neveu-Schwarz sector etc. Often KP hierarchy is from the very beginning
formulated in terms of Neveu-Schwarz (antiperiodic) fermionic fields
(associated with  principal
representations of Kac-Moody algebras), i.e. expansions in the first line of
(\ref{notfermcor}) are in semi-integer powers of $z$:
$\psi_{NS}( z) = \sum_{n\in Z}\psi_n z^{n-\frac{1}{2}} d z^{1/2}$.

Given a KP $\tau$-function one can usually construct a Toda-lattice one with
the {\it same} G, by introducing in appropriate way dependencies on $\bar t$
and $N$. For this purpose $\tau^{KP}$ should be represented in the form of
(\ref{todatau}):
\be
\tau^{KP}\{t\mid G\} = {\rm Det}_{i,j<0} {\cal H}_{ij}^{KP},
\label{addkptau1}
\ee
where ${\cal H}_{ij}^{KP} = \sum_l T_{lj} P_{l-i}(t)$. Since $T_{lm} $ is a
function of $G$ only, it does not change when we built up a Toda-lattice
$\tau$-function:
\be
&\tau_N\{t,\bar t\mid G\} = {\rm Det}_{i,j<0} {\cal H}_{i+N,j+N}; \nn \\
&{\cal H}_{ij} = \sum_{l,m}T_{lm} P_{l-i}(t)P_{m-j}(\bar t) =
\sum_m {\cal H}_{im}^{KP} P_{m-j}(\bar t).
\ee
Then
\be
\tau^{KP}\{ t\mid G\} = \tau_0\{t,0\mid G\}.
\ee
If we go in the opposite direction, when Toda-lattice $\tau$-function is
considered as KP $\tau$-function,
\be
\tau_0\{t,\bar t\mid G\} = \tau^{KP}\{t \mid \tilde G(\bar t)\}; \nn \\
\tilde {\cal H}^{KP}_{ij} = \sum_m {\cal H}_{im}P_{m-j}(\bar t)\ \
{\rm and} \nn \\
\tilde T_{lj}\{\tilde G(\bar t)\} = \sum_m T_{lm}\{G\}P_{m-j}(\bar t).
\label{addkptau2}
\ee

KP reduction in its turn has many further weak reductions (KdV and  Boussinesq
being the simplest examples). We shall mention them again in section 4.9
below, after Miwa transformation of representation (\ref{todatau}) will
be considered in the next subsection.
