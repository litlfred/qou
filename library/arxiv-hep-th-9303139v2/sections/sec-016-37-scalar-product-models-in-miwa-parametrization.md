---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-016-37-scalar-product-models-in-miwa-parametrization
section_title: "Scalar-product models in Miwa parametrization"
section_number: 3.7
pages: 65-66
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.992
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
We shall now make the first step towards clarification of the interrelation
between the scalar-product and Kontsevich models.
We already know that in the latter
case the important role is played by representation of time-variables in the
form of
\be
T_k = \frac{1}{k} {\rm tr} \Lambda ^{-k},
\label{MiwaT}
\ee
with $n\times n$ matrix $\Lambda $,
which will be further refered to as Miwa parametrization (expressions of
some similar form were first introduced in \cite{Miwa}). Let us now perfrom
such transformation in the case of the scalar-product model.
Let us use eq.(\ref{tbartmeas}) to define the time-dependence of the measure,
only ignore the $\bar t$-variables. Namely, introduce
$d\mu_{h,\bar h} = e^{U(h)} d\hat\nu_{h,\bar h}$ (i.e. $d\hat\nu_{h,\bar h} =
e^{\bar U(\bar h)}d\hat\mu_{h,\bar h}$). Substitute
\be
t_k = \mp\left(\frac{1}{k}{\rm tr}\Lambda ^{-k} + r_k\right)
\ee
and obtain:
\be
\new
\begin{array}{c}
e^{U(h)} = e^{-\hat V(h)} e^{\mp{\rm tr} \sum_{k=1}^{\infty}\frac{1}{k}
\left(\frac{h}{\Lambda }\right)^k} =
e^{-\hat V(h)}\frac{{\rm det}^{\pm 1}(\Lambda -h\cdot I)}{{\rm
det} \Lambda } = \\
= \frac{ e^{-\hat V(h)}}{{\rm det} \Lambda }
\prod_{\gamma =1}^n (\lambda _\gamma-h)^{\pm 1},
\end{array}
\ee
where $\hat V(h) \equiv \pm \sum_k r_kh^k$. Let us choose {\it upper} signs in
these formulas. Then we can  use eqs.(\ref{meas2}) and
(\ref{meas3}) to conclude that in Miwa parametrization
\be
Z_N^{\{d\mu\}} =
\frac{1}{({\rm det} \Lambda )^N} Z_N^{\{d\hat\nu\}}\{ \lambda _\delta\} =
Z_N^{\{d\hat\nu\}}
\frac{{\rm det}_{\gamma\delta}\hat Q_{N+\gamma-1}(\lambda _\delta)}
{\Delta(\lambda )({\rm det} \Lambda )^N},
\nn
\ee
where $d\hat\nu_{h,\bar h} \equiv e^{-\hat V(\bar h)}d\nu_{h,\bar h}$ and
$\hat Q_k$ are the corresponding orthogonal polinomials.
In other words, we reduced the model with potential $U(h)$ to another model
with potential, $-\hat V(h)$, and expressed the difference in terms of
orthogonal polinomials $\hat Q_k$:
\be
\frac{Z_N^{\{d\mu\}}}{Z_N^{\{d\hat\nu\}}} =
\frac{1}{({\rm det} \Lambda )^N}\cdot
\frac{{\rm det}_{\gamma\delta}\hat Q_{N+\gamma-1}
(\lambda _\delta)}{\Delta(\lambda )}.
\label{reduhv}
\ee
If $\hat V(h)$ is adjusted to give rise to some simple orthogonal polinomials,
(i.e. if the new model $Z_N^{\{d\hat\nu\}}$ is easy to solve),
this representation can considerably simplify the original model.

Another interpretation of this formula is that we obtained a GKM-like
representation of the from of (\ref{KIev"N}) for the {\it discrete}
scalar-product model. The only difference is that $\varphi_\gamma^{\{V\}}$ in
(\ref{KIev"N}) are changed for $\hat Q_{\gamma-1}$ in (\ref{reduhv}). This is
an important difference, because $\varphi_\gamma^{\{V\}}$ in GKM are defined
to by integral formulas like (\ref{hatvarphi}),
$\varphi_\gamma^{\{V\}} =\ \langle\langle x^{\gamma -1} \rangle\rangle$
or, alternatively, satisfy the
recursive relations like (\ref{Kasch}). Moreover, generic
$\varphi_\gamma^{\{V\}}$ are infinite formal series in $\lambda^{-1}$, while
$Q_{\gamma-1}$ are orthogonal {\it polinomials}. This discreapancy is one of
important stimuli for further developement of the concept of Generalized
Kontsevich model, as well as for search for convenient integral
representations for orthogonal polinomials.

There is, however, at least one interesting situation when the two formulas
indeed coincide. This is the case of Gaussian potentials $V$ and $\hat V$,
when both $\varphi_\gamma^{\{V\}}$ and
$Q_{\gamma-1}$ are represented by orthogonal Hermite polinomials, which
possess  integral representation, exactly adequate in the context of
GKM. This is the subject of our consideration in the next subsection.
