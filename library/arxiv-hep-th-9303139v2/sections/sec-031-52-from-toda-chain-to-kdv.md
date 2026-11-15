---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-031-52-from-toda-chain-to-kdv
section_title: "From Toda-chain to KdV"
section_number: 5.2
pages: 124-126
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
We begin with the simplest existing example: continuum limit, in which the
lowest  equation of the "Volterra hierarchy",
\be
\frac{\partial R_n}{\partial t} = - R_n(R_{n+1}-R_{n-1}),
\label{lowVolt}
\ee
turns into the lowest KdV equation:
\be
\frac{\partial r}{\partial T_3} = - \frac{1}{3}r''' - 2rr'.
\label{lowKdV}
\ee
Volterra hierarchy is a reduction of Toda-chain hierarchy, with
$R_n = e^{\phi_n-\phi_{n-1}}$, arising when all the odd-times $t_{2k+1} = 0$
and all $\phi_n$ are supposed to be independent of them. Therefore this
hierarchy is clearly related to the discrete 1-matrix model. We"ll turn to the
study of 1-matrix model in the next subsection, but here we just address the
transformation from (\ref{lowVolt}) to (\ref{lowKdV}) \cite{Nov},\cite{GMMMO}.

The basic idea of taking continuum limit is to change discrete "zero-time" $n$
for {\it continuum} variable $x$ (to be after all substituted by $T_1$ of the
continuous hierarchy). In other words, the idea is to consider a subset of
functions $R_n$, which satisfy Volterra equation and depend on $n$ very
smoothly, so that they can actually be substituted by a smooth function
$R(x)$. This is a very natural thing to do, of course, when one is interested
in the large-$n$ limit of the equation. Namely, one substitutes
(\ref{lowVolt}) by
\be
\frac{\partial R(x)}{\partial t} = - R(x)(R(x+\epsilon)-R(x-\epsilon)),
\label{lowVoltcon}
\ee
and take the limit $\epsilon \rightarrow 0$, which, after rescaling
$x \rightarrow \epsilon x$, gives rise to "Bateman equation",
\be
\frac{\partial R(x)}{\partial t} = - R(x)R'(x).
\label{Bateq}
\ee
This is a very interesting equation (see \cite{Fair} for description of the
amusements of the related theory, which is in fact intimately related to the
theory of jets). However, it is much simpler that KdV equation (for example,
it is {\it completely} integrable in the most trivial sense of the word:
entire set of solutions, satisfying {\it any} boundary conditions can be
immediately written down, see \cite{Fair}). KdV equation can be considered as
a sort of "quantization" of (\ref{Bateq}) (unfortunately this very interesting
subject did not yet attract enough attention and is not studied well enough).

Remarkably, Bateman equation is not the {\it only} possible limit of Volterra
equation: a fine tuning procedure ("double-scaling limit") exist, which can
provide less trivial - KdV - equation \cite{Nov}. Indeed, imagine, that in
continuum limit $R_n$ tends to a constant $R_0$, and the function $r(x)$
arises only as scaling approximation to this constant:
$R(x) = R_0(1 + \epsilon ^sr(x))$. Then the leading term at the r.h.s. of
(\ref{Bateq}) is $\epsilon RR'(x) =
-2\epsilon^s r(x) (1 + {\cal O}(\epsilon^2,\epsilon^s))$,
and instead of (\ref{Bateq}) we would get:
\be
\frac{\partial r}{\partial t} = - 2\epsilon R_0 r'(x) ((1 + {\cal
O}(\epsilon^2,\epsilon^s)).
\nn
\ee
This equation is even simpler that (\ref{Bateq}) - it is just linear, but in
fact it is too simple to preserve its form: by a simple change of
variables\footnote{
This change of variables is implied by the relation:
\be
\frac{\partial}{\partial t} + 2\epsilon^sR_0 \frac{\partial}{\partial x} =
\left( \frac{\partial \tilde t}{\partial t} +
2\epsilon^sR_0 \frac{\partial \tilde t}{\partial x}\right)
\frac{\partial}{\partial \tilde t} +
\left( \frac{\partial \tilde x}{\partial t} +
2\epsilon^sR_0 \frac{\partial \tilde x}{\partial x}\right)
\frac{\partial}{\partial \tilde x} =
\frac{\partial}{\partial \tilde t}.
\ee
}
\be
\tilde x = x - 2\epsilon R_0 t, \\
\tilde t = \epsilon^3 R_0 t
\label{chavacont}
\ee
it can be transformed into
\be
\frac{\partial r}{\partial \tilde t} = \epsilon^{-2} {\cal
O}(\epsilon^2,\epsilon^s),
\nn
\ee
and terms at the r.h.s. also deserves beeing taken into account.
Then we get:
\be
\frac{\partial r(x)}{\partial t} = -2\epsilon R_0 \left(1 + \epsilon^sr(x))
(r'(x) + \frac{1}{6}\epsilon^2r'''(x) + {\cal O}(\epsilon^4)\right) = \nn \\
= -2\epsilon R_0 \left( r'(x) + \frac{1}{6}\epsilon^2r'''(x)
+ \epsilon^s rr'(x) + \epsilon^2{\cal O}(\epsilon^2, \epsilon^s)\right)
\nn
\ee
and, after the change of variables (\ref{chavacont}),
\be
\frac{\partial r(\tilde x)}{\partial \tilde t} = - \frac{1}{3} r'''(\tilde x)
- 2\epsilon^{s-2}rr'(\tilde x) + {\cal O}(\epsilon^2, \epsilon^s).
\nn
\ee
It is now clear, that the choice $s=2$  is distinguished (a critical point)
and at this point we get:
\be
\frac{\partial r}{\partial T_3} =
-\frac{1}{3}\frac{\partial^3r}{\partial T_1^3} -
2r\frac{\partial r}{\partial T_1},
\ee
where new notation $T_1$ and $T_3$ is introduced for $\tilde x$ and $\tilde t$
respectively. This is already the KdV equation (\ref{lowKdV}), and our
conclusion is:

While the naive continuum limit of Volterra equation is just a
simple Bateman equation, the scaling limit can be fine tuned so that KdV
equation arises instead. The crucial ingredient of this adjustement is the
change of time-variables $\{t\} \longrightarrow \{T\}$, which involves
singular parameter $\epsilon$. The procedure can be easily generalized to the
entire Volterra hierarchy, and fine tuning allows to get the entire KdV
hierarchy in the limit of $\epsilon \rightarrow 0$. Usually transformation to
the "Kazakov variables" $\{T\}$ (they are a little different from those
originally introduced by V.Kazakov in \cite{Kmamo})
from $\{t\}$ is some linear {\it triangular} transformation.

An important detail is that this procedure
requires restriction to only {\it even} time-variables $t_{2m},\ m\geq 0$.
(If odd times are also involved, a {\it pair} of KdV hierarchies arises in the
continuum limit - this is not a "minimal" case.) Thus "irreducible"
realization of continuum limit requires {\it reduction} of original hierarchy.
This can be also seen from the fact that the lowest KdV equation arises from
the lowest Volterra equation, which is related to the {\it second} eqaution of
Toda-chain hierarchy.

Unfortunately this simple piece of theory (continuum limits in terms of
hierarchies) has never been worked out in full details (for the entire
Toda-lattice hierarchy, its multicomponent generalizations and their
reductions). As we already mentioned, this theory will involve the general
relation between homogeneous and principal representations of the (level
$k=1$) Kac-Moody algebras.
