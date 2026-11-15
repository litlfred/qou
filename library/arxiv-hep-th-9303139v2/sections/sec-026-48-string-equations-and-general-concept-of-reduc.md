---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-026-48-string-equations-and-general-concept-of-reduc
section_title: "String equations and general concept of reduction"
section_number: 4.8
pages: 104-110
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.976
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
The role of string equation is to fix the point $G$ in the universal module
space (UMS), associated with the particular matrix model, so that partition
function, considered as a function of time variables, will appear as  the
corresponding $\tau$-function of a fixed shape. In this sense the idea behind
the string equation is exatly the same as reduction of integrable hierarchies.
The difference is that {\it linear} reductions, as defined in the section 4.5
above, are not enough to fix $G$ unambiguously: they just specify certain
subsets in the Grassmannian, which are still infinite-dimensional. The reason,
why  these are usually linear reductions that are considered in the
conventional theory of integrable hierarchies, is that they are associated
with the simplest possible - Kac-Moody - subalgebras in the entire
$GL(\infty)$. String equations, even their simplest examples, are usually
fragments of more complicated - Virasoro and $W$-algebras, and are in fact
considerably more restrictive. Moreover, string equation is usually a
{\it distinguished} fragment,
because it usually belongs to the Virasoro component
of Ward identities, and Virasoro is still a {\it Lie} subalgebra in
$GL(\infty)$. This is what makes the problem of string equations very similar
to the "classical" one with linear reduction.

More specifically, in order to include string equations (and in fact the
entire set of Virasoro - but not $W$ - constraints) into consideration of
reduction it is enough to allow the coefficients in (\ref{redtotau1})
to depend on $t$
and $\bar t$, without changing the order of time-derivatives. Of course, there
are no obvious reasons to think that {\it any} point $G$ in the UMS can be
selected by imposing this kind of linear-derivative constraints on
$\tau$-function, - and further investigation can require essential
generalization of such restricted notion of string equation. However, some of
the eigenvalue matrix models are already known to possess string equations
of such simple type, associated with Virasoro subalgebras of $GL(\infty)$.
We do not go into details of the general theory - it is far not completed yet,
- but instead present several examples of how string equations arise in
particular matrix models. These examples can illustrate also the
simplifications arising when only  string equations and not the entire sets of
Ward identities need be derived. In particular, it is clear that in cases when
$\tau$ is represented as ${\rm Det}_{ij} {\cal H}_{ij}$, a linear differential
equation imposed on ${\cal H}_{ij}$ will give rise to a similar equation on
$\tau$ itself. Most of known string equations can be derived with the help of
this technical idea. They are usually associated with invariance of integrals
under {\it constant} shifts of integration variables $\delta h =\ const$ in
scalar-product and other discrete models, and with the action of operator
${\rm tr} \frac{\partial}{\partial L_{tr}}$ in GKM. For somewhat more involved
ideas, associated with string equations see \cite{GMoo}.

{\it Scalar-product models}. String equation can be easily deduced for very
specific type of measures $d\hat\mu_{h,\bar h}$. Since integral
\be
{\cal H}_{ij} = \int h^i\bar h^j e^{U(h)+\bar U(\bar h)}
d\mu_{h,\bar h}
\ee
is invariant under the shift of integration variable $\delta h =\ const$,
\be
\int h^i\bar h^j e^{U(h)+\bar U(\bar h)}
d\hat\mu_{h,\bar h} \left[ ih^{-1} + \frac{\partial U(h)}{\partial h} +
\frac{\partial}{\partial h} \log (d\hat\mu_{h,\bar h}) \right] = 0,
\ee
or
\be
i{\cal H}_{i-1,j} + \sum_{k>0} kt_k\frac{\partial}{\partial t_{k-1}}
{\cal H}_{ij} +
\left[ S\left(\frac{\partial}{\partial t},\frac{\partial}{\partial \bar t}
\right)\right]_{ij} = 0.
\ee
String equation arises straightforwardly, when operator $S$ is linear. This is
true, if $\log (d\hat\mu_{h,\bar h}) \sim hf(\hat h)$  with any function
$f(h)$. If the measure $d\hat\mu_{h,\bar h}$ is also required to be symmetric
in $h$ and $\bar h$,  we obtain conventional 2-matrix model as the only
example:
\be
d\hat\mu_{h,\bar h} = e^{ch\bar h}dhd\bar h.
\ee
Equation for ${\cal H}_{ij}$ is:
\be
\phantom.\left(\sum_{k>0} kt_k\frac{\partial}{\partial t_{k-1}} +
c\frac{\partial}{\partial \bar t_1}\right) {\cal H}_{ij} =
- i{\cal H}_{i-1,j}.
\label{hfor2mamo}
\ee
Its implication for $\hat \tau_N$ is:
\be
\left(\sum_{k>0} kt_k\frac{\partial}{\partial t_{k-1}} +
c\frac{\partial}{\partial \bar t_1}\right) \hat\tau_N = 0,
\label{sefor2mamo}
\ee
since the r.h.s. of (\ref{hfor2mamo}) does not contribute to determinant (the
entries in the i-th row are proportional to those in the $i-1$-th row).

In particular case of {\it 1-matrix model} $\ c=0$, and we recognize the lowest
Virasoro constraint $L_{-1}\hat\tau_N = 0$.
Traditionally the name of string equation is
given not to $L_{-1}$-constraint itself, but to its $t_1$-derivative:
$\frac{\partial}{\partial t_1}(L_{-1}\hat\tau_N) = 0$.
For 2-matrix model
(\ref{sefor2mamo}) is the lowest ($m=1,\ n=0$) component of the Ward
identities $\left(\tilde W_{n-m}^{(m+1)}(t) - (-)^{m+n}c^{n+1}
\tilde W_{m-n}^{(n+1)}(\bar t)\right)\hat\tau_N = 0$.
Of course, there is also a similar equation with
$t \leftrightarrow \bar t$.

{\it Multicomponent (conformal) models}. The crucial feature of these models
is that intermatrix interaction, when rewritten in terms of eigenvalues,
usually contains only differences $\ h_i^{(\balpha)} - h_j^{(\bbeta)}\ $. Thus
there is usually covariance under {\it simultaneous} shift of all eigenvalues
$\ \delta h_i^{(\balpha)} = const\ $ by a {\it same} constant.
This gives rise to a string equation of the form
\be
\left( \sum_{\balpha} L_{-1}^{(\balpha)} \right) \tau_{\bf N} = 0.
\ee
See \cite{comamo} for details.

{\it Generalized Kontsevich Model}.

In order to derive string equation one should act on partition function
$Z_V\{T_k = \frac{1}{k}{\rm tr}\Lambda^{-k}\} =
{\cal C}_V^{-1} {\cal F}_V\{L = V'(\Lambda)\}$ with operator ${\rm
tr}\frac{\partial}{\partial L_{tr}} = {\rm tr}\frac{1}{V''(\Lambda)}
\frac{\partial}{\partial \Lambda_{tr}}$. We can rewrite the result of this
action in terms of time-derivatives,
\be
{\rm tr}\frac{\partial}{\partial L_{tr}} \log Z_V\{T\} =
-\sum_{k>0} \left({\rm tr}\frac{1}{V''(\Lambda)\Lambda^{k+1}}\right)
\frac{\partial}{\partial T_k}\log Z_V\{T\}.
\ee
Alternatively we can use the fact that $\ \displaystyle{
{\rm tr}\frac{\partial}{\partial L_{tr}} = \sum_\gamma
\frac{1}{V''(\lambda_\gamma)}\frac{\partial}{\partial\lambda_\gamma}}\ $,
$l = V'(\lambda)$, and
explicit expression for $Z_V$ in terms of eigenvalues (Miwa coordinates),
\be
\new
\begin{array}{c}
Z_V \sim e^{{\rm tr}V(\Lambda) - {\rm tr}\Lambda V'(\Lambda)}
\sqrt{\prod_\gamma V''(\lambda_\gamma)}\
\frac{{\rm det}\ \hat \varphi_\gamma(\lambda_\delta)}{\Delta(\lambda)} \sim \\
{\sim} \frac{{\rm det}\
\varphi_\gamma(\lambda_\delta)}{\Delta(\lambda)},
\end{array}
\label{detformzv}
\ee
to get:
\be
\new
\begin{array}{c}
\left({\rm tr}\frac{\partial}{\partial L_{tr}}\right) \log Z_V\{T\} =   \\
= \frac{1}{2} {\rm
tr}\frac{V'''(\Lambda)}{(V''(\lambda))^2}
+ \frac{1}{2}\sum_{\gamma > \delta} \frac{V''(\lambda_\gamma) -
V''(\lambda_\delta)}{\lambda_\gamma - \lambda_\delta} \cdot
\frac{1}{V''(\lambda_\gamma)V''(\lambda_\delta)} -  \\
- {\rm tr} \Lambda  + \sum_\beta
\frac{\partial}{\partial l_\beta}
\log{\rm det}_{\gamma\delta} \hat \varphi_\gamma(l_\delta).
\end{array}
\ee
Comparison of these two expressions gives:
\be
\new
\begin{array}{c}
\frac{{\cal L}_{-1}^{(V)} Z_V}{Z_V} \equiv
\frac{1}{Z_V}\left[ \sum_{k>0} \left({\rm
tr}\frac{1}{V''(\Lambda)\Lambda^{k+1}}\right)
\frac{\partial}{\partial T_k} +  \right. \\ \left. +
\frac{1}{2}\sum_{\gamma > \delta} \frac{V''(\lambda_\gamma) -
V''(\lambda_\delta)}{\lambda_\gamma - \lambda_\delta} \cdot
\frac{1}{V''(\lambda_\gamma)V''(\lambda_\delta)} - \frac{\partial}{\partial
T_1}\right] Z_V = \\
= - \frac{\partial}{\partial T_1}\log Z_V + {\rm tr} \Lambda -
\sum_\beta
\frac{\partial}{\partial l_\beta}
\log{\rm det}_{\gamma\delta} \hat \varphi_\gamma(l_\delta).
\end{array}
\label{steqend}
\ee
One can show that the r.h.s. is equal to zero, and thus the string
equation arises in the form
\be
{\cal L}_{-1}^{(V)} Z_V = 0.
\ee
If potential is monomial, $V_p = \frac{X^{p+1}}{p+1}$, then
$r_k = -\frac{p}{p+1}\delta_{k,p+1}$ and
\be
\new
\begin{array}{c}
{\cal L}_{-1}^{V_p} \rightarrow {\cal L}_{-p} \equiv \\
\equiv
\frac{1}{p} \left[ \sum_{k>0} (k+p)(T_{k+p} + r_{k+p})\frac{\partial}{\partial
T_k} + \frac{1}{2} \sum_{k=1}^{p-1} k(p-k)T_kT_{p-k}\right].
\end{array}
\label{asa}
\ee

The technical idea behind the proof \cite{GKM} is to represent
\be
\frac{\partial}{\partial T_1}\log Z_V = {\rm Res}
\frac{Z_V\{T_k + \frac{1}{k\lambda^k}\}d\lambda}{Z_V\{T_k\}},
\ee
and make use of the second determinant representation in (\ref{detformzv})
both in the denominator and the numerator:
\be


\frac{\partial}{\partial T_1}\log Z_V =
{\rm Res}\frac{d\lambda}{\prod_{\gamma=1}^n(\lambda - \lambda_\gamma)}
\cdot\frac{ {\rm det}\left( \begin{array}{cc}
\varphi_\delta(\lambda_\gamma) & \varphi_{n+1}(\lambda_\gamma) \\
\varphi_\delta(\lambda) & \varphi_{n+1}(\lambda)
\end{array}\right)}
{{\rm det}\ \varphi_\delta(\lambda_\gamma)}.

\label{as0}
\ee
Now we recall that
\be
\varphi_\gamma(\lambda) \sim \lambda^{\gamma -1} \left( 1
+ {\cal O}(\lambda^{-1})\right).
\label{as1}
\ee
At some moment we shall need even more:  in fact
\be
&\varphi_\gamma(\lambda) \sim \lambda^{\gamma -1} \left( 1
+ {\cal O}(\lambda^{-2})\right), \ \ {\rm i.e.} \nn \\
&\varphi_\gamma(\lambda) = \lambda^{\gamma -1} + c_\gamma\lambda^{\gamma-2} +
\ldots, \ \ {\rm and}\ \ c_\gamma = 0 \ \ {\rm for\ any} \ \gamma.
\label{as2}
\ee
This is a rather delicate property of GKM, it follows from two facts:
first, $\displaystyle{\varphi_1 = 1 + {\cal O}\left(\frac{V''''}{(V'')^2},
\frac{(V''')^2}{(V'')^3}\right)}$, thus $c_1 = 0$, and
second, Kac-Scwarz operator ${\cal A}$, defined in eq.(\ref{gkmKasch}) below,
does not have contributions with zero-th power of $\lambda$, thus $c_{\gamma
+1} = c_\gamma$. (For example, if $V(x) = \frac{x^2}{2} + ax$,
$\varphi_\gamma(x) = \frac{1}{\sqrt{2\pi}} \int x^{\gamma -1}
e^{-\frac{1}{2}(x-\lambda)^2}dx = \lambda^{\gamma-1} + 0\cdot \lambda^{\gamma
-2} + \ldots$: the dangerous terms with $a$ simply do not show up in the
expression for $\varphi_\gamma$.)

After this comment we can come back to evaluation of (\ref{as0}).
The product in denominator, which arised from the Van-der-Monde determinant,
is already proportional to $\lambda^n$:
$\prod_{\gamma =1}^n(\lambda - \lambda_\gamma) = \lambda^n\left(1 + {\cal
O}(\lambda^{-1})\right)$.
Because of this and the asymptotic formulas (\ref{as1}), it is clear that
if determinant in the numerator of (\ref{as0}) is rewritten as linear
combination of $n\times n$ determinants with the coefficients
$\varphi_\gamma(\lambda)$ from the last row, only items
with $\gamma \geq n$ can contribute. There are two such items: $\gamma = n$
and $\gamma = n+1$. In the expansion of $(n+1)\times (n+1)$ determinant
$\varphi_{n+1}(\lambda) $ is multiplied by ${\rm det}\
\varphi_{\gamma}(\lambda_\delta)$, which exactly cancels with determinant in
denominator, and the relevant contribution is
\be
{\rm Res}\ \frac{\varphi_{n+1}(\lambda)d\lambda}{\prod_{\gamma
=1}^n(\lambda - \lambda_\gamma)} = c_{n+1} + \sum_\gamma \lambda_\gamma =
\nn \\ = c_{n+1} + {\rm tr}\Lambda.
\ee
The item with $\varphi_n(\lambda)$ is
\be
\frac{{\rm det} \left(\varphi_1(\lambda_\gamma) \ldots
\varphi_{n-1}(\lambda_\gamma)\ \varphi_{n+1}(\lambda_\gamma)\right)}
{{\rm det} \left(\varphi_1(\lambda_\gamma) \ldots
\varphi_{n-1}(\lambda_\gamma)\ \varphi_{n}(\lambda_\gamma)\right)}
{\rm Res}\ \frac{\varphi_n(\lambda)d\lambda}{\prod_{\gamma
=1}^n(\lambda - \lambda_\gamma)}.
\label{detratvpn1}
\ee
The remaining residue is just unity. Determinant in the numerator differs from
the one in denominator by substitution of the colomn with entries
$\varphi_{n}(\lambda_\gamma)$ for that with $\varphi_{n+1}(\lambda_\gamma)$.

At last we can return to eq.(\ref{steqend}) and recall that
$\frac{\partial}{\partial l}\hat\varphi_\gamma(l) = \varphi_{\gamma +1}(l)$,
thus
\be
\new
\begin{array}{c}
\sum_\beta \frac{\partial}{\partial l_\beta} \log{\rm
det}_{\gamma\delta}\hat\varphi_\delta(l_\gamma) = \\
\frac{{\rm det} \left(\hat\varphi_1(l_\gamma) \ldots
\hat\varphi_{n-1}(l_\gamma)\ \hat\varphi_{n+1}(l_\gamma)\right)}
{{\rm det} \left(\hat\varphi_1(l_\gamma) \ldots
\hat\varphi_{n-1}(l_\gamma)\ \hat\varphi_{n}(l_\gamma)\right)},
\end{array}
\label{detvarphil}
\ee
what is just the same as (\ref{detratvpn1}), since $\hat\varphi_\delta$
differ from $\varphi_\delta$ by $\delta$-independent factor of
$e^{V(\lambda)-\lambda V'(\lambda)}\sqrt{V''(\lambda)}$. Thus we conclude that
the r.h.s. of (ref{steqend}) is equal to $-c_{n+1}$, which actually vanishes,
as was explained several lines above.

Two things deserve paying attention in this derivation. First, it was
absolutely crucial that we had $\frac{\partial}{\partial T_1}\log Z_V$ at the
r.h.s. of (\ref{steqend}) to make it vanishing, and therefore
$\frac{\partial}{\partial T_1}$ immedeately appears in the expression for the
${\cal L}_{-1}^{(V)}$ operator at the l.h.s. (this is the origin of
$r_k$-corrections in (\ref{asa}). Second, the result is both simple and
natural, but the proof is full of technical details and looks somewhat
artificial. It becomes even more involved, when the general formula
(\ref{tkderiv})
for $T_k$-derivatives of $Z_V$ with $1\leq k\leq p$ \cite{Krich} is derived,
which plays an important role in the theory of GKM and its applications to the
theory of quantum gravity. The proof of the string equation is just a
particular case of that formula, since using integral representation of
$\hat\varphi(l)$ one can represent the r.h.s. of (\ref{detvarphil}) as
$\frac{1}{Z_V}\langle {\rm tr} X \rangle$, where $\langle \ \ \rangle$ now
stand for the average, defined by Kontsevich integral. Thus
\be
{\cal L}_{-1}^{(V)} Z_V \stackrel{(\ref{steqend})}{=}
-\frac{\partial}{\partial T_1}Z_V + \langle {\rm tr}\Lambda - {\rm tr}X
\rangle \stackrel{(\ref{tkderiv})}{=} 0.
\ee
