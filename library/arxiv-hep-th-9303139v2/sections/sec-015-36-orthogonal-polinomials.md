---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-015-36-orthogonal-polinomials
section_title: "Orthogonal polinomials"
section_number: 3.6
pages: 59-65
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.971
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Formalism of orthogonal polinomials was intensively used at the early days of
the theory of matrix models. It is applicable to scalar-product
eigenvalue models
and allows to further transform (diagonalize) the remaining determinants into
products. In variance with both reduction from
original $N^2$-fold matrix integrals to the eigenvalue problem, which (when
possible) reflects a physical phenomenon - decoupling of angular
(unitary-matrix) degrees of freedom (associated with $d$-dimensional gauge
bosons), - and with occurence of determinant formulas which reflects
integrability of the model,  orthogonal polinomials appear more as a technical
device. Essentially orthogonal polinomials are
necessary if wants to explicitly separate dependence on the the size $N$ of
the matrix in the matrix integral ("zero-time") from dependencies on all other
time-variables and to explicitly construct variables, which satisfy Toda-like
equations. However, modern description of integrable hierarchies in terms of
$\tau$-functions does not require explicit separation of the
zero-time and treats it more or less on the equal fooring with all other
variables, thus making the use of orthogonal polinomials unnecessary. Still
this technique remains in the arsenal of the matrix model theory\footnote{
Of course, one can also use this link just with the aim to put the
rich and beautifull mathematical theory of orthogonal polinomials into the
general context of string theory. Among interesting problems here is the
matrix-model description of $q$-orthogonal polinomials.
} and we now
briefly explain what it is about. At the end of this section two simple
applications will be also described: one to evaluation of the volume of the
unitary group, another - to direct proof of equivalence of the ordinary
1-matrix model and the Gaussian Kontsevich model. Both these examples make use
of explicitly known orthogonal Hermite polinomials and in this sense are not
quite representative: usually orthogonal polinomials are $not$ known
explicitly. Some applications of such "abstract" theory of orthogonal
polinomials to the study of matrix models will be mentioned in the following
sections.

In the context of the theory of scalar-product matrix models orthogonal
polinomials naturally arise when one notes that after
partition functions appears in a simple determinantal form of
eq.(\ref{dimamodet}),
any linear change of basises $h^i \rightarrow Q_i(h) = \sum_kA_{ik}h_k,
\ \bar h^j \rightarrow \bar Q_j(\bar h) = \sum_l B_{jl}\bar h^l$ can be easily
performed and
$Z \longrightarrow Z\cdot {\rm det} A\cdot {\rm det} B$. In particular, if $A$
and $B$
are triangular with units at diagonals, their determinants are just unities
and $Z$ does not change at all. This freedom is, however, enough, to
diagonalize the scalar product and choose polinomials $Q_i$ and $\bar Q_j$ so
that
\be
\langle Q_i(h) \mid \bar Q_j(\bar h) \rangle = e^{\phi_i}\delta_{ij}.
\label{orthopol}
\ee
$Q_i$ and $\bar Q_j$ defined in this way up to normalization are called
orthogonal polinomials. (Note that $\bar Q$ does not need to be a {\it
complex} conjugate of $Q$: "bar" does not mean complex conjugation.)
Because of above restriction on the form of matrices
$A$ and $B$ these polinomials are normalized so that
\be
Q_i(h) = h^i + \ldots;\ \ \ \bar Q_j(\bar h) = \bar h^j + \ldots
\nn
\ee
i.e. the leading power enters with the $unit$ coefficient. From
(\ref{dimamodet}) and (\ref{orthopol}) it follows that
\be
Z_N = \prod_{i=1}^N e^{\phi_{i-1}}.
\label{ZNprod}
\ee
This formula is essentially the main outcome of orthogonal polinomials theory
fro matrix models: it provides complete separation of the $N$-dependence of
$Z$ (on the size of the matrix) from that on all other parameters
(which specify the shape of
potential, i.e. the measure $d\mu_{h,\bar h}$), this information is encoded in
a rather complicated fashion in $\phi_i$.
As was already mentioned, any feature of matrix model can be examined already
at the level of eq.(\ref{dimamodet}), which does not refer to orthogonal
polinomials and thus they are not really relevant for the subject.

We can, however, reverse the problem and ask, what can matrix models provide
$for$ the theory of orthogonal polinomials.\footnote{Of course, we can hardly
get anything $new$ for that theory, but the purpose is to see, which features
are immediate consequences of the "physically-inspired" approach. As usually
this can help to somehow organize the existing knowledge in appropriate
system. This is, however, not our goal in these notes: only a very simple
example will be mentioned, which will be also of use in our futher
considerations.}
The first question to ask in the theory of orthogonal polinomials is:

Given the measure $d\mu_{h,\bar h}$, what are the corresponding orthogonal
polinomials?

Usually the answer to this type of questions is not at all straightforward.
Its complexity, however, depends on what one agrees to accept as a suitable
answer. Of particular interest for our purposes below would be integral
representations. It would be very helpfull to have just an integral
transformation, converting the set of orthogonal polinomials for given
$d\mu_{h,\bar h}$ into some standard set, like $Q_i^{(0)} = x^i$.
Unfortunately,
such transformation is rarely available, though there are important examples:
classical orthogonal polinomials and their $q$-analogues (expressed through
the ($q$-)hypergeometric functions, which usually possess integral
representation of a simple form, see \cite{movi} for an introductory review of
such integral formulas, which are in fact well known in CFT).
The simplest example of this kind, which will be used below is the set of
Hermite polinomials:
\be
{\rm He}_k(h) = \frac{1}{\sqrt{2\pi}} e^{\frac{h^2}{2}}
\int (ix)^ke^{-\frac{x^2}{2}-ixh} dx
= (h-\frac{d}{dh})^k\cdot 1 = \nn \\
= e^{\frac{h^2}{2}}(-\frac{d}{dh})^k e^{-\frac{h^2}{2}} =
\frac{1}{2^k}e^{\frac{h^2}{4}}(h - 2\frac{d}{dh})^ke^{-\frac{h^2}{4}} =
h^k + \ldots,
\label{hepo}
\ee
orthogonal with the $local$ measure $d\mu_h = e^{-\frac{h^2}{2}}$.

For generic measure the answer of this type does not exist in any universal
form. However, matrix models still provide a somewhat peculiar integral
representation for $any$ measure, with the number of integrations depending on
the number of polinomial.
In order to obtain this expression, let us consider a slight generalization of
formula (\ref{meas1})
\be
Z_N\{\lambda _\gamma\} \equiv
\frac{1}{N!} \prod_{k=1}^N \int d\mu_{h_k,\bar h_k}
\Delta(h)\Delta(\bar h)\prod_{k,\gamma} (\lambda _\gamma - h_k).
\label{meas2}
\ee
Then
$\Delta(h)\prod_{k,\gamma} (\lambda _\gamma - h_k) =
\Delta(h,\lambda )/\Delta(\lambda )$,
and $\lambda _\gamma$ can be just considered as $h_{N+\gamma}$,
which are $not$ integrated over in (\ref{meas2}). Then it is clear that
\be
\Delta(h,\lambda ) = {\rm Det} \left(
\begin{array}{cl}        Q_{i-1}(h_k)  & Q_{N+\gamma-1}(h_k)  \\
                     Q_{i-1}(\lambda _\delta)
& Q_{N+\gamma-1} (\lambda _\delta)
\end{array}
\right)
\ee
while $\Delta(\bar h) = {\rm Det}_{jk} \bar Q_{j-1}(\bar h_k)$. Since all the
$Q_{N+\gamma-1}(h_k)$ are orthogonal to all $\bar Q_{j-1}(\bar h_k)$
(because $N+\gamma-1 \neq j-1$), we obtain:
\be
Z_N\{\lambda _\delta\} =
\frac{{\rm det}_{\gamma\delta}Q_{N+\gamma-1}(\lambda _\delta)}
{\Delta(\lambda )} Z_N.
\label{meas3}
\ee
In particular,
\be
Q_N(\lambda ) = \frac{Z_N\{\lambda \}}{Z_N},
\ee
where both the numerator and denominator can be represented by $N\times
N$-matrix integrals.

Inverse "main question" of the theory of orthogonal polinomials is:

Given a set of polinomials
\be
Q_i(h) = h_i + \ldots,\nn \\
\bar Q_j(\bar h) = \bar h_j + \ldots,
\nn
\ee
 what is the measure
$d\mu_{h,\bar h}$ w.r.to which they form an orthogonal system?

We shall not discuss the complete answer to this question and consider only
the case of the {\it local} measure, when $\bar Q_i = Q_i$.
Then usually the answer does not exist at all: not {\it every} system of
polinomials is orthogonal w.r.to some local measure. It is easy to find the
necessary (and in fact sufficient) condition. As was mentioned above, the
local measure is distinguished by the property that multiplication by (any
function of) $h$ is Hermitean operator:
\be
\langle hf(h)\mid g(\bar h)\rangle =
\langle f(h) \mid \bar h g(\bar h)\rangle, \ \ {\rm if} \
d\mu_{h,\bar h} \sim \delta(h-\bar h).
\ee
This property implies, that the coefficients $c_{ij}$ in the recurrent
relation
\be
hQ_i(h) = Q_{i+1}(h) + \sum_{j=0}^i c_{ij}Q_j(h)
\ee
are almost all vanishing. Indeed: for $j<i$
\be
\new
\begin{array}{c}
c_{ij} = \frac{\langle hQ_i(h) \mid Q_j(\bar h)\rangle}{\langle Q_j(h) \mid
Q_j(\bar h)\rangle} =
\frac{\langle Q_i(h) \mid \bar hQ_j(\bar h)\rangle}{\langle Q_j(h) \mid
Q_j(\bar h)\rangle} =
 \\ =
\delta_{i,j+1}\frac{\langle Q_i(h) \mid Q_i(\bar h)\rangle}{\langle Q_j(h)
\mid Q_j(\bar h)\rangle} =

\delta_{j,i-1} e^{\phi_i -\phi_{i-1}}.
\end{array}
\ee
In other words, polinomials, orthogonal w.r.to a local measure are obliged to
satisfy the "3-term recurrent relation":
\be
hQ_i(h) = Q_{i+1}(h) + C_iQ_i(h) + R_iQ_{i-1}(h)
\label{3termrel}
\ee
(the coefficient in front of $Q_{i+1}$ can be of course changed by the change
of normalization). Parameter $C_i$ vanishes if the measure is even (symmetric
under the change $h \rightarrow -h$), then polinomials are split into two
orthogonal subsets: even and odd in $h$. Partition function (\ref{ZNprod})
of the $one$-component model can be expressed through parameters
$R_i =  e^{\phi_i -\phi_{i-1}}$ of the 3-term relation:
\be
Z_N = Z_1 \prod_{i=1}^{N-1} R_i^{N-i},
\ee
thus defining a one-component matrix model (i.e. particular shape of
potential), associated with any system of orthogonal polinomials.

Our "inverse main question" in the case of the local measure should be now
formulated as follows: Given a set of orthogonal polinomials $Q_i(h) = h^i
+\ldots$ {\it which satisfy the 3-term relation} (\ref{3termrel}), what is
the measure $d\mu_h$?

As every complete orthogonal system of functions, orthogonal polinomials
satisfy the completeness relation:
\be
\sum_{i=0}^{\infty} e^{-\phi_i} \bar Q_i(\bar h)Q_i(h) =
\delta^{\{d\mu\}}(\bar h,h),
\ee
where $\delta$-function, associated with the measure $d\mu_{h,\bar h}$ is
defined so that
\be
\int\int f(h)\delta^{\{d\mu\}}(\bar h,h') d\mu_{h,\bar h} = f(h')
\ee
for any function $f(h)$.
Since for the {\it local} measure $d\mu_h = e^{U(h)}dh$ the $\delta$-function
is just $\delta^{\{d\mu\}}(\bar h,h) = e^{-U(h)}\delta(\bar h - h)$,
as an answer to our question we can take a representation of $U(h)$
in terms of the corresponding orthogonal polinomials:
\be
e^{-U(h)}\delta(\bar h - h) = \sum_{k=0}^{\infty} \frac{Q_k(\bar h)Q_k(h)}
{\langle Q_k \mid Q_k\rangle}.
\label{orthopoltomeas}
\ee
As usually this relation should be understood as analytical continuation.
The squared norms $\mid\mid Q_k \mid\mid^2$ in denominator are expressed
through the coefficients $R_i$ of the 3-term relation up to an overall
constant: $\mid\mid Q_k \mid\mid^2 = \prod_{i=1}^k R_i\mid\mid Q_0 \mid\mid^2$.

For example, in the case of Hermite polinomials (\ref{hepo}) we have:
\be
{\rm He}_{k+1}(h) = (h - \frac{d}{dh}){\rm He}_k(h) =
h{\rm He}_k(h) - \frac{d}{dh}{\rm He}_k(h) =
\nn \\
= h{\rm He}_k(h) - k{\rm He}_{k-1}(h)
\ee
(the last equality holds because $\frac{d}{dh}$ and $h-\frac{d}{dh}$ play the
role of annihilation and creation operators respectively). This means that the
3-term relation is satisfied with $R_k = k$ and thus
$\mid \mid {\rm He}_k\mid\mid^2 = \mid \mid {\rm He}_0\mid\mid^2 k!$
We shall use the normalization condition
$\mid \mid He_0\mid\mid^2 = \sqrt{2\pi}$. Then for $e^{-U(h)}$ we get:
\be
\new
\begin{array}{c}
e^{-U(h)}\delta(\bar h-h) =  \\
\sum_{k=0}^{\infty} \frac{{\rm He}_k(\bar h){\rm He}_k(h)}
{\mid\mid He_k\mid\mid^2} =
\frac{1}{\sqrt{2\pi}}\sum_{k=0}^{\infty}\frac{1}{k!}
(h-\frac{d}{dh})^k(\bar h-\frac{d}{d\bar h})^k \cdot 1 =
 \\
=  \frac{1}{\sqrt{2\pi}} e^{\frac{h^2}{2}+\frac{\bar h^2}{2}}
  \sum_{k=0}^{\infty}\frac{1}{k!}(\frac{d^2}{dhd\bar h})^k
  e^{-\frac{h^2}{2}-\frac{\bar h^2}{2}}

= \frac{1}{\sqrt{2\pi}} e^{\frac{h^2}{2}+\frac{\bar h^2}{2}}
  e^{\frac{d^2}{dhd\bar h}} e^{-\frac{h^2}{2}-\frac{\bar h^2}{2}}
=  \\
= \frac{1}{\sqrt{2\pi}} {\rm Im} \int\int \frac{d\alpha d\bar\alpha}{2\pi}
e^{-\alpha\bar\alpha} e^{\frac{h^2}{2}+\frac{\bar h^2}{2}}
e^{\alpha\frac{d}{dh}+\bar\alpha\frac{d}{d\bar h}}
 e^{-\frac{h^2}{2}-\frac{\bar h^2}{2}} =
 \\ =
\frac{1}{\sqrt{2\pi}} {\rm Im} \int\int \frac{d\alpha d\bar\alpha}{2\pi}
e^{-\frac{1}{2}(\alpha +\bar\alpha)^2}
e^{-\frac{1}{2}(\alpha +\bar\alpha)(h + \bar h)}
e^{-\frac{1}{2}(\alpha -\bar\alpha)(h - \bar h)} =
\nn \\ = e^{\frac{h^2}{2}}\delta(h-\bar h).
\end{array}
\ee
