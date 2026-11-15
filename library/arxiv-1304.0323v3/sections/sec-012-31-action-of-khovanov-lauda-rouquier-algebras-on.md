---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-012-31-action-of-khovanov-lauda-rouquier-algebras-on
section_title: "Action of Khovanov-Lauda-Rouquier algebras on V'0362V"
section_number: 3.1
pages: 27-31
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.925
---
Let $\{V_s\}_{s\in \mathcal{S}}$ be a family of good $\uqpg$-modules
and  let $\lambda_s$ be a dominant extremal weight of $V_s$ and $v_s$
a dominant extremal weight vector in $V_s$ of weight $\lambda_s$.


Let $J$ be an index set and
let $X \colon J \rightarrow \mathbb{T}$ and
$S \colon J \rightarrow \Ss$ be maps,
where $\mathbb{T}=\cor^\times$ is the algebraic torus.
For each $i,j \in J $,
we choose $c_{i,j}(u,v)\in\cor[[u,v]]$ such that
\eq&&\ba{l} \label{cond:cij}
c_{i,j}(u,v)c_{j,i}(v,u)=1,\\
c_{i,i}(u,v)=1.
\ea
\eneq
Set
\begin{equation}
P_{ij}(u,v) =(u-v)^{d_{ij}}c_{i,j}(u,v),\label{def:Pij}
\end{equation}
where $d_{ij}$ denotes the order of the zero of
$d_{V_{S(i)},V_{S(j)}}(z_2 / z_1)$ at $z_2 / z_1 = {X(j) / X(i)}$.

Let $R^{J}$ be the symmetric \KLR\ associated with
\begin{equation}\label{eq:Q_omega}
Q_{ij}(u,v) = \delta(i\not=j)P_{ij}(u,v)P_{ji}(v,u)=\delta(i\not=j) (u-v)^{d_{ij}}(v-u)^{d_{ji}}\end{equation}
for $i,j \in J$.

\Rem \label{rmk:cij} If we consider the non-graded $R^{J}$-module category $R^J\smod$,
the choice of $c_{i,j}$ is not important, and we can choose, for example,
$c_{i,j}(u,v)=1$. Indeed, adding $c_{i,j}(u,v)$
is equivalent to  the change of  generators
$\tau_ke(\nu)\mapsto c_{\nu_k,\nu_{k+1}}(x_x,x_{k+1})\tau_ke(\nu)$.
However, as we shall see later in Theorem~\ref{thm:cij},
we need to choose $c_{i,j}(u,v)$ carefully when we  are concerned with
localizations of the graded $R^{J}$-module category $R^J\gmod$.
\enrem

\begin{remark}
The underlying Cartan matrix $A_J=(a^J_{ij})_{i,j\in J}$ is given by
\begin{equation}\label{eq:quiver}
a^J_{ij}=\begin{cases}
2&\text{if $i=j$,}\\
-d_{ij}-d_{ji}&\text{if $i\not=j$.}\end{cases}
\end{equation}
Consider the quiver $\Gamma_J \seteq (J, \Omega)$ with the set of
vertices $J$ and the set of oriented edges $\Omega$ such that
$$\sharp\set{h \in \Omega}{s(h) = i, t(h)=j } = d_{ij}
\qtext{ for all $i,j\in J$,}$$
where $s(h)$ and $t(h)$ denote the source and the target of an oriented edge $h \in \Omega$.

Theorem~\ref{th:zero} implies that $X(j)/X(i)\in\C[[q^{1/m}]]q^{1/m}$ for some $m>0$
if $d_{ij}>0$.
Hence we obtain
$$\text{if $d_{ij} > 0$, then $d_{ji} =0$.}$$
Thus the quiver $\Gamma_J$ has neither loops nor cycles.
The underlying unoriented graph of $\Gamma_J$ gives a symmetric Cartan datum and the polynomials in \eqref{eq:Q_omega}
are essentially same as
the ones used in \cite{VV09} associated with
 the symmetric Cartan datum of $\Gamma_J$.
\end{remark}

\bigskip
Let
\begin{equation*}
\Oh_{\mathbb{T}^n, X(\nu)} = \cor [[X_1 - X(\nu_1), \ldots, X_n-X(\nu_n)]]
\end{equation*}
 be the completion of
the local ring $\sho_{\mathbb{T}^n, X(\nu)}$
 of $\mathbb{T}^n$ at  $X(\nu)\seteq(X(\nu_1),\ldots,X(\nu_n))$
 and $\bK[\nu]$  the fraction field of $\Oh_{\mathbb{T}^n, X(\nu)}$.

 For $\beta \in \rootl^+$ with $|\beta|=n$,
set
\begin{align*}
&\bP_{ \beta } \seteq \soplus_{\nu \in J^{ \beta }} \cor [x_1, \ldots, x_n] e(\nu)\subset R^J( \beta ), \\
&\bPh_{ \beta }\seteq\soplus_{\nu\in J^{ \beta }}\Oh_{\mathbb{T}^n, X(\nu)}e(\nu), \\
&\bK[ \beta ] \seteq \soplus_{\nu \in J^{ \beta }} \bK[\nu]e(\nu).\end{align*}

Then we have
\begin{equation*}
\bP_{ \beta }\hookrightarrow\bPh_{ \beta }\hookrightarrow\bK[ \beta ]
\end{equation*}
as $\cor$-algebras, where the first arrow is given by
\begin{equation*}
x_k e(\nu) \mapsto X(\nu_k)^{-1}\bl X_k -X(\nu_k)\br e(\nu).
\end{equation*}
Note that
\begin{equation*}
\cor [X_1^{\pm1}, \ldots, X_n^{\pm1}] \subset \Oh_{\mathbb{T}^n, X(\nu)}
\qtext{and}\quad \Oh_{\mathbb{T}^n, X(\nu)}\simeq\cor[[x_1,\ldots,x_n]]
\qtext{for all} \ \nu \in J^{ \beta }.
\end{equation*}
Let
\begin{align*}
\cor [\sym_n] \seteq \bigoplus_{w \in \sym_n} \cor r_w
\end{align*}
be the group algebra of $\sym_n$;
i.e., the $\cor$-algebra with the multiplication
$r_{w}r_{w'}=r_{ww'}$ for $w,w'\in \sym_n$.
We denote $r_{s_i}$ by $r_i$ for $i=1,\ldots, n-1$.

The symmetric group $\sym_n$ acts on $\bP_{ \beta }$, $\bPh_{ \beta }$, $\bK[ \beta ]$
from the left and we have
\begin{equation*}
\bP_{ \beta }\otimes {\cor[\sym_n]} \hookrightarrow \bPh_{ \beta }\otimes {\cor[\sym_n]} \hookrightarrow \bK[ \beta ]\otimes {\cor[\sym_n]}
\end{equation*}
as algebras. Here the algebra structure on $\bK[ \beta ]\otimes {\cor[\sym_n]}$ is given by
\begin{align} \label{eq:rel of Khat S_n}
r_w f =w(f) r_w & \quad \text{for $f \in \bK[ \beta ]$, $w \in \sym_n$.}
\end{align}
Then $\bK[ \beta ]$
may be regarded as a right $\bK[ \beta ] \otimes {\cor[\sym_n]}$-module
by
$$a (f\otimes r_w)=w^{-1}(af) \quad (a,f\in \bK[ \beta ], \ w\in
\sym_n).$$




 Define $\tau_a\in\bK[ \beta ]\otimes {\cor[\sym_n]}$ by
\begin{equation*}
e(\nu) \tau_a = \begin{cases}
e(\nu)  P_{\nu_a, \nu_{a+1}}(x_{a}, x_{a+1})r_a & \text{if $\nu_a \neq \nu_{a+1}$,} \\
e(\nu) (r_a -1)(x_a -x_{a+1})^{-1} & \text{if $\nu_a = \nu_{a+1}$.}
\end{cases}
\end{equation*}
Then the subalgebra of $\bK[ \beta ]\otimes {\cor[\sym_n]}$
generated by \eqn &&e(\nu) \ (\nu \in J^{ \beta }),\quad x_a \ (1
\leq a \leq n), \quad \tau_a  \ (1 \leq a \leq n-1) \eneqn is
isomorphic to the \KLR\ $R^J({ \beta })$ at ${ \beta }$ associated
with $Q_{ij}(u,v) = \delta(i\not=j)P_{ij}(u,v) P_{ji}(v,u)$
(\cite[Proposition 3.12]{R08}, \cite[Theorem 2.5]{KL09}).

\bigskip
For each $\nu =(\nu_1,\ldots, \nu_n) \in J^{ \beta }$, we set
$$
V_\nu =( V_{S(\nu_1)})_\aff \otimes \cdots
\otimes (V_{S(\nu_n)})_\aff$$
which is a $\bl\cor[X_1^{\pm1},\ldots, X_n^{\pm1}]\otimes\uqpg \br$-module,
where $X_k=z_{V_{S(\nu_k)}}$.
 We   define
\begin{align}
\ba{ll}
\hV_\nu&\seteq \Oh_{\mathbb{T}^n, X(\nu)}\otimes _{\cor[X_1^{\pm1},\ldots,X_n^{\pm1}]}
V_\nu,\\[1ex]
\bV[ \beta ]&\seteq \soplus\nolimits_{\nu \in J^{ \beta }}
\hV_\nu e(\nu),\\[1ex]
\bVK[ \beta ]&\seteq \bK[ \beta ]\tens_{\bPh_{ \beta }}\bV[{ \beta
}] \simeq\soplus\nolimits_{\nu\in J^\beta}\bK[\nu]\tens
\nolimits_{\Oh_{\mathbb{T}^n, X(\nu)}} \hV_\nu.\ea
\label{eq:Vhat}
\end{align}
For each $\nu \in J^{ \beta }$ and $a=1,\ldots, n-1$, there exists a $\uqpg$-module homomorphism
\begin{equation*}
R^{\nu}_{a, a+1} \colon \cor(X_1,\ldots,X_n) \otimes_{\cor[X_1^{\pm1}, \ldots X_n^{\pm1}]}
V_\nu \rightarrow
\cor(X_1,\ldots,X_n) \otimes_{\cor[X_1^{\pm1}, \ldots X_n^{\pm1}]} V_{s_a(\nu)}
\end{equation*}
which is given by
\begin{equation*}
 v_1 \otimes \cdots \otimes v_a \otimes v_{a+1} \otimes \cdots \otimes v_n
\mapsto v_1 \otimes \cdots \otimes \Rnorm_{V_{S(\nu_a)},V_{S(\nu_{a+1})}}(v_a \otimes v_{a+1}) \otimes \cdots \otimes v_n
\end{equation*}
for $v_k \in (V_{S(\nu_k)})_\aff$ $(1 \leq k \leq n)$.
It follows that
\begin{align}
&R^{\nu}_{a, a+1} \circ X_k = X_{s_a(k)} \circ R^{\nu}_{a, a+1} && \text{from \eqref{eq:r-matrix commute with z},} \nonumber\\
&R^{s_a(\nu)}_{a, a+1} \circ R^{\nu}_{a, a+1} = 1_{V_{\nu}}&& \text{from \eqref{eq:r^2=1},} \nonumber \\
&R^{s_{a+1}s_a(\nu)}_{a, a+1} \circ R^{s_a (\nu)}_{a+1, a+2} \circ R^{\nu}_{a, a+1} =
R^{s_a s_{a+1}(\nu)}_{a+1, a+2} \circ R^{s_{a+1}(\nu)}_{a, a+1} \circ R^{\nu}_{a+1, a+2}
&& \text{from \eqref{eq:r_YB}.} \ \nonumber
\end{align}
Set $d_{\nu_a,\nu_{a+1}}(u)=d_{V_{S(\nu_a)}, V_{S(\nu_{a+1})}} (u)$. Then,
we have
\begin{equation}
 R^{\nu}_{a, a+1}\circ d_{\nu_a,\nu_{a+1}}(X_{a+1}/X_a)
\colon V_{\nu} \rightarrow V_{s_a(\nu)}.\label{eq:regR}
\end{equation}

The algebra $\bK[ \beta ] \otimes {\cor[\sym_n]}$ acts on $\bVK[{ \beta }]$ from the right, where

\begin{align*}
e(\nu) r_a \col \; &\widehat{\mathbb K}_\nu \otimes_{\cor[X_1^{\pm1}, \ldots X_n^{\pm1}]} V_\nu \\
&\rightarrow \widehat{\mathbb K}_{s_a(\nu)} \otimes_{\cor(X_1,\ldots,X_n)} \big( \cor(X_1,\ldots,X_n) \otimes_{\cor[X_1^{\pm1}, \ldots X_n^{\pm1}]} V_{s_a(\nu)}\big)
\end{align*}
is given by
\begin{equation*}
(f \otimes v) e(\nu) r_a = s_a(f) e(s_a(\nu)) \otimes R^{\nu}_{a, a+1}(v)
\end{equation*}
for $f \in \widehat{\mathbb K}_{\nu}$, $v \in \cor(X_1,\ldots,X_n) \otimes_{\cor[X_1^{\pm1}, \ldots, X_n^{\pm1}]} V_\nu$.
The subalgebra $\widehat{\mathbb{K}}_{ \beta }$ acts by the multiplication.
The relation
\eqref{eq:rel of Khat S_n} follows from the properties of normalized R-matrices and hence we have a well-defined right action of the algebra $\widehat{\mathbb{K}}_{ \beta } \otimes {\cor[\sym_n]}$ on
$\bVK[{ \beta }]$.
Since the normalized R-matrices are $\uqpg$-module homomorphisms,
$\bVK[{ \beta }]$ has a structure of
 $(\uqpg,\widehat{\mathbb{K}}_{ \beta } \otimes {\cor[\sym_n]})$-bimodule.

\begin{theorem}
The subspace $\bV[{ \beta }]$ of \/  $\bVK[{ \beta }]$ is stable under
the  right action of the subalgebra $R^J({ \beta })$ of\/ $\widehat{\mathbb{K}}_{ \beta } \otimes {\cor[\sym_n]}$.
In particular, $\bV[{ \beta }]$ has a structure of
$(\uqpg, R^J({ \beta }))$-bimodule.
\begin{proof}
It is obvious that $\bV[{ \beta }]$
is stable under the actions of $e(\nu)$ $(\nu \in J^{ \beta })$ and
$x_a$ $(1 \leq a \leq n)$.
Thus it is enough to show that $\bV[{ \beta }]$ is stable under $e(\nu) \tau_a$ $(\nu \in J^{ \beta }, \ 1 \leq a < n)$.

Assume $\nu_a \neq \nu_{a+1}$. Then we have
\eqn
&&e(\nu) P_{\nu_a,\nu_{a+1}}(x_{a},x_{a+1})\\
&&\hs{1ex}=e(\nu) d_{\nu_a,\nu_{a+1}}(X_{a+1}/X_a)
\dfrac{ (X(\nu_{a})^{-1}X_a-X(\nu_{a+1})^{-1}X_{a+1})^{d_{\nu_a, \nu_{a+1}}}
c_{\nu_a,\nu_{a+1}}(x_{a},x_{a+1})} {d_{\nu_a,\nu_{a+1}}(X_{a+1}/X_a)} \nonumber.
\eneqn
Since $d_{\nu_a, \nu_{a+1}}$ is the multiplicity of the zero of the polynomial
$d_{\nu_a,\nu_{a+1}}(X_{a+1}/X_a)$ at $X_{a+1}/X_a=X(\nu_{a+1}) / X(\nu_{a})$,
we have
$$\dfrac{ (X(\nu_{a})^{-1}X_a-X(\nu_{a+1})^{-1}X_{a+1})^{d_{\nu_a, \nu_{a+1}}}
c_{\nu_a,\nu_{a+1}}(x_{a},x_{a+1})} {d_{\nu_a,\nu_{a+1}}(X_{a+1}/X_a)} \in
 \Oh_{\mathbb{T}^n, X(\nu)}.$$
It follows that
$$\hV_\nu e(\nu) P_{\nu_a,\nu_{a+1}}(x_a,x_{a+1})
\subset\hV_\nu e(\nu)d_{\nu_a,\nu_{a+1}}(X_{a+1}/ X_{a}).$$
Hence
\eqn
&&\hV_\nu e(\nu)\tau_a
=\hV_\nu e(\nu)P_{\nu_a,\nu_{a+1} }(x_{a}, x_{a+1})r_a
\subset \hV_\nu e(\nu) d_{\nu_a,\nu_{a+1}}(X_{a+1} / X_{a})r_a,
\eneqn
and it is contained in $\hV_{s_a(\nu)} e(s_a(\nu))$ by \eqref{eq:regR}.

\smallskip

Assume $\nu_a=\nu_{a+1}$.
Then $\Rnorm_{V_{S(\nu_a)},V_{S(\nu_a)}}$ does not have a pole at
$X_a=X_{a+1}$ by Theorem~\ref{th:zero}.
Since $(V_{S(\nu_a)})_x\otimes (V_{S(\nu_{a})})_x$ is irreducible for any $x\in\cor^\times$, we obtain
$\Rnorm_{V_{S(\nu_a)},V_{S(\nu_a)}}\vert_{X_a=X_{a+1}}=\id$.

Therefore, we have
\begin{align*}
\hV_\nu e(\nu) \tau_a
&=\hV_\nu e(\nu) (r_a -1)(x_a -x_{a+1})^{-1} \\
&=\hV_\nu e(\nu) X(\nu_a) (r_a -1) (X_a -X_{a+1})^{-1}
\subset \hV_\nu e(\nu),
\end{align*}
as desired.
\end{proof}
\end{theorem}
