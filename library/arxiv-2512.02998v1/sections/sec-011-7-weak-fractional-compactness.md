---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-011-7-weak-fractional-compactness
section_title: "Weak fractional compactness"
section_number: 7
pages: 23-29
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 0.968
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
\label{sec:compactness}
From the introduction we recall  
Definition~\eqref{eq:symmetric-subset} of
the $p$-rotationally symmetric subset $\Sigma_p(\mathcal{K})$ of a given
knot equivalence class $\mathcal{K}$ for $p\in\N\setminus\{1\}$. 
Consider now for given constants
$L\ge 1$ and $R>0$ the subset
\begin{equation}\label{eq:compact-subset}
\mathcal{F}_{p,L,R}(\mathcal{K}):=
\{\eta\in\Sigma_p(\mathcal{K})\!\cap\! W^{\frac32,2}(\R/\Z,\R^3):
|\eta'|\!=\!1\,\textnormal{a.e.},\,\bilip(\eta)\!\ge\!
\textstyle\frac1{L},\,\max\{|\eta(0)|,\lfloor\eta'
\rfloor^2_{\frac12,2}\}\!\le\! R\},
\end{equation}
where $\bilip(\eta)$ denotes the bilipschitz constant defined in
\eqref{eq:def-bilip} in Section~\ref{sec:stability}. Then
we can prove the following compactness result which may be of
independent interest in geometric knot theory.
\begin{theorem}[Weak fractional compactness]
\label{thm:fractional-compactness}
For any tame prime knot equivalence class  $\mathcal{K}$ the set
$\mathcal{F}_{p,L,R}(\mathcal{K})$ is weakly sequentially compact
in $W^{\frac32,2}(\R/\Z,\R^3)$ in the restricted sense that for any sequence
$(\g_n)_n\subset \mathcal{F}_{p,L,R}(\mathcal{K})\cap C^1(\R/\Z,\R^3)$ 
there is a knot
$\g\in\mathcal{F}_{p,L,R}(\mathcal{K})$ and a 
subsequence $\g_{n_k}\rightharpoonup \g$ in $W^{\frac32,2}$ as $k\to\infty$.
\end{theorem}

Strictly speaking, the tameness requirement is superfluous since
$\mathcal{F}_{p,L,R}(\mathcal{K})=\emptyset$ if $\mathcal K$ is wild
as pointed out at the end of the proof of Corollary \ref{cor:fractional-stability}.
The additional smoothness assumption on the sequence $(\g_n)_n$ guarantees 
that sequence members remain tame after the harmonic substitution described
in Section~\ref{sec:harmonic}. This assumption might 
be of purely technical
nature and can possibly be omitted.

For our application 
in search of symmetric minimizing knots for the M\"obius energy
in Section~\ref{sec:symm-critical}, however, a mollification argument
allows us to focus on smooth minimizing sequences satisfying all assumptions
of Theorem~\ref{thm:fractional-compactness} above.

\noindent
{\it Proof of Theorem~\ref{thm:fractional-compactness}.}\,
We proceed in several steps.

{\it Step 1. Subconvergence to a candidate curve $\g$.}\,
Since $|\g_n'|=1$ a.e.\@ on $\R/\Z$ and $|\g_n(t)|\le
|\g_n(t)-\g_n(0)|+R\le 1+R$ for a.e.\@ $t\in\R/\Z$ one finds a constant
$C=C(R)$ independent of $n$ such that
\begin{equation}\label{eq:w3halbe-bound}
\|\g_n\|_{W^{\frac32,2}}\le C\quad\Foa n\in\N.
\end{equation}
The space $W^{\frac32,2}(\R/\Z,\R^3)$ is reflexive so that we may
assume that there is some curve $\g\in W^{\frac32,2}
(\R/\Z,\R^3)$ such that (up to a subsequence)
\begin{equation}\label{eq:weak-subconvergence}
\g_n\rightharpoonup \g \quad\textnormal{as $n\to\infty$.}
\end{equation}
By the Poincar\'e inequality (cf.~\cite[Proposition A.3]{knappmann-etal_2022}) the seminorm $\lfloor\cdot
\rfloor_{\frac12,2}$ is a norm on the subspace $\{f\in 
W^{\frac12,2}(\R/\Z,\R^3):\int_{\R/\Z}f(u)du=0\}$ 
equivalent to $\|\cdot\|_{W^{\frac12,2}}$. Since $
\int_{\R/\Z}\eta'(u)du=0$
for all $\eta\in W^{\frac32,2}(\R/\Z,\R^3)$ we therefore have by 
\eqref{eq:weak-subconvergence},
\begin{equation}\label{eq:uhs-seminorm}
\lfloor\g'\rfloor_{\frac12,2}\le\liminf_{n\to\infty}\lfloor\g_n'
\rfloor_{\frac12,2}\le \sqrt{R}.
\end{equation}
Moreover, due to the compact embeddings $W^{\frac32,2}\hookrightarrow
C^0$ and $W^{\frac32,2}\hookrightarrow
W^{1,1}$ and the theorem of Fischer--Riesz, we find (up to a further
subsequence)
\begin{equation}\label{eq:unif-subconvergence}
\g_n\to\g\quad\textnormal{in $C^0$, \quad and}\quad
\g_n'\to\g'\quad\textnormal{a.e.\@ on $\R/\Z$\quad as $n\to\infty$.}
\end{equation}
This implies $|\g(0)|=\lim_{n\to\infty}|\g_n(0)|\le R$ and
$|\g'|=\lim_{n\to\infty}|\g_n'|=1$ a.e.\@ on $\R/\Z$. The uniform
convergence in \eqref{eq:unif-subconvergence} leads to the bilipschitz
estimate
$$
\textstyle
|\g(u)-\g(v)|=\lim_{n\to\infty}
|\g_n(u)-\g_n(v)|\ge\frac1{L}|u-v|_{\R/\Z}\quad\Foa u,v\in\R/\Z;
$$
hence 
\begin{equation}\label{eq:bilip-gamma}
\textstyle
\bilip(\g)\ge\frac1{L},
\end{equation}
and $\g$ is embedded. 
Also the symmetry relation \eqref{eq:rot-symm} is preserved in the uniform
limit
since
$$
\textstyle
\g(s)=\lim_{n\to\infty}\g_n(s)\overset{\eqref{eq:rot-symm}}{=}
R_{\frac{2\pi}p}\lim_{n\to\infty}\g_n(s-\frac1{p})=
R_{\frac{2\pi}p}\g(s-\frac1{p})\quad\Foa s\in\R/\Z.
$$
So, the only requirement on the limiting knot $\g$ to be checked, 
is that $\g$ represents the prescribed knot equivalence
class, i.e., that $[\g]=\mathcal{K}$. 

{\it Step 2. Controlling the local distortion of the limiting  knot $\g$.}\,
Combining \eqref{eq:seminorm-bilip2} in Corollary \ref{cor:seminorm-bilip} 
with the absolute
continuity of the double integral defining the seminorm
 $\lfloor\g'\rfloor_{\frac12,2}\le$ $\sqrt{R}$ yields a number $\rho_\g\in
 (0,\frac14)$ such that for $d_\g(s,t)\equiv d_\g(\g(s),\g(t))=|s-t|_{\R/\Z}$
 \begin{equation}\label{eq:dist-limit}
\textstyle
\sup\big\{\frac{d_\g(s,t)}{|\g(s)-\g(t)|}:s,t\in\R/\Z,\,0<|s-t|_{\R/\Z}=
|s-t|\le 2\rho_\g\big\}<g_3.
\end{equation}
For parameters $s,t\in\R/\Z$ with $d_\g(s,t)>2\rho_\g$, on the
other hand, we infer from \eqref{eq:bilip-gamma}
\[ 2\rho_\g<d_\g(s,t)=|s-t|_{\R/\Z}\le L|\g(s)-\g(t)|. \]
This together
with \eqref{eq:dist-limit} leads to 
\begin{equation}\label{eq:local-distortion-limit}
\textstyle
\delta(\g,r_\g)<g_3\quad\textnormal{at scale
$r_\g:=\frac{\rho_\g}L.$}
\end{equation}
Suppose we had $\delta(\g_m,r_{\g_m})<g_3$ for  some $m\in\N$ at some
scale $r_{\g_m}>0$, then we could conclude the knot equivalence $
\mathcal{K}=[\g_m]=[\g]$ from Corollary \ref{cor:equiv-knots},
if, in addition, $\|\g_m-\g\|_{L^\infty}<\frac14\min\{r_\g,r_{\g_m}\}$.
But as indicated in Section~\ref{sec:strategy} of the introduction
this might be too much to hope for because of possible 
concentrations in the seminorms $\lfloor \g_m'\rfloor_{\frac12,2}$
as $m\to\infty$. Therefore, we are going to carefully
cut out possible
concentrations of the curves $\g_n$,
 replace these subarcs by straight segments
to obtain modified curves $\tilde{\g}_n$, and use
the estimates of Section~\ref{sec:harmonic} to finally
find a sequence member $\tilde{\g}_m$ sufficiently 
$L^\infty$-close to $\g$, so that Corollary \ref{cor:equiv-knots}
indeed implies
$[\g]=[\tilde{\g}_m]=[\g_m]=\mathcal{K}$. 
The details are presented in the remaining steps. This is 
where the assumptions $\g_n\in C^1(\R/\Z,\R^3)$ and $\mathcal{K} $
prime come into play.

{\it Step 3. Localizing concentrations via weak convergence of measures.}\,
Fix
\begin{equation}\label{eq:fix-theta}
\textstyle
\theta\equiv \theta_4:=\big(\frac1{6\cdot 128L}\big)^8<\theta_3<\theta_2<
\theta_1<\frac1{20},
\end{equation}
such that we have Lemmas \ref{lem:quant-embed}, 
\ref{lem:difference-quotients}, \ref{lem:harmonic-substitution},
\ref{lem:compare-intrinsic}, and \ref{lem:bilip-control-harmonic}
of Section~\ref{sec:harmonic} at our disposal. In addition, set
\begin{equation}\label{eq:epsilon-choice}

\varepsilon:=\frac23-\frac6{\pi^2}>0
\end{equation}
and define the Radon measures\footnote{suitably extended to
an outer measure; see, e.g., \cite[pp. 13,14]{teschl_2025}.}
\begin{equation}\label{eq:def-radon}
\textstyle
\mu_n(A):=\iint_A\frac{|\g_n'(u)-\g_n'(v)|^2}{|u-v|^2}\,dudv
\quad
\text{for Lebesgue measurable}
A\subset\R/\Z\times\R/\Z,\,\,n\in\N.
\end{equation}
By means of the assumed uniform bound $\lfloor\g_n'\rfloor_{\frac12,2}\le
\sqrt R$ 
we find $\sup_{n\in\N}\mu_n(\R/\Z\times\R/\Z)\le R <\infty$,
so that there is a Radon measure $\mu$ on $\R/\Z\times\R/\Z$ such that
(up to a subsequence)
\begin{equation}\label{eq:weak-convergence}
\mu_n\rightharpoonup\mu\quad\As n\to\infty,
\end{equation}
cf.\@ \cite[Theorem~1.41]{evans-gariepy_2015}. (Note that the limiting
measure $\mu$ might be different from $\lfloor\g'\rfloor_{\frac12,2,\cdot}^{2}$.)
Since the mapping $r\mapsto\mu(B_r(x)\times B_r(y))$ is non-negative and 
non-decreasing for fixed parameters $x,y\in\R/\Z$, its limit
\begin{equation}\label{eq:limit-balls}
\textnormal{$\lim_{r\downarrow 0}\mu(B_r(x)\times B_r(y))$ exists and is 
non-negative,}
\end{equation}
so that we can consider the set
\begin{equation}\label{eq:W-eps}
W_\varepsilon:=\big\{ (x,y)\in\R/\Z\times\R/\Z:\lim_{r\downarrow 0}\mu\big(B_r(x)
\times B_r(y)\big)>\varepsilon\big\}.
\end{equation}
We claim that concentrations take place only on the diagonal, i.e.,
\begin{equation}\label{eq:diagonal}
W_\varepsilon=\bigcup_{x\in V_\varepsilon} \{x\}\times\{x\},
\end{equation}
where $V_\varepsilon:=\{x\in\R/\Z:\lim_{r\downarrow 0}\mu(B_r(x)\times B_r(x))>
\varepsilon\}$.
Indeed, for arbitrary fixed $n\in\N$, distinct parameters
$x,y\in\R/\Z$, and $0<r<\frac14 |x-y|_{\R/\Z},$ one has
$|u-v|\ge |x-y|-2r >\frac12 |x-y|_{\R/\Z}$ for all $u\in B_r(x)$,
$v\in B_r(y)$, so that (with $|\g_n'|=1$ a.e.)
\begin{equation}\label{eq:diagonal-proof}
\mu_n\big(B_r(x)\times B_r(y)\big) < \frac4{|x-y|_{\R/\Z}^2}\cdot 4(2r)^2,
\end{equation}
and therefore, by the characterization of weak convergence
of measures \cite[Theorem~1.40]{evans-gariepy_2015},
$$
\textstyle
\mu\big(B_r(x)\times B_r(y)\big)\le\liminf_{n\to\infty}
\mu_n\big(B_r(x)\times B_r(y)\big)\overset{\eqref{eq:diagonal-proof}}{\le}
\frac{64}{|x-y|^2_{\R/\Z}}\cdot r^2\to 0\quad\As r\to 0.
$$
Hence $(x,y)\not\in W_\varepsilon$, which proves our claim 
\eqref{eq:diagonal}.

We also claim that $W_\varepsilon$ contains only finitely many elements,
that is,
\begin{equation}\label{eq:finitely-many}
\textstyle
\sharp W_\varepsilon =\sharp V_\varepsilon\le\lceil \frac{R}\varepsilon
\rceil,
\end{equation}
where $\lceil a\rceil$ denotes the smallest integer greater or equal to $a$.
For that take $j$ parameters $x_1,\ldots, x_j\in V_\varepsilon$ and
choose radii $r_1,\ldots,r_j>0$ such that
$\mu(B_{r_k}(x_k)\times B_{r_k}(x_k))>\varepsilon$ and
$B_{r_i}(x_i)\cap B_{r_l}(x_l)=\emptyset $ for all $i,k,l\in
\{1,\ldots,j\}$ with $i\not= l$.
Then
$$
\textstyle
\varepsilon\cdot j< \sum_{k=1}^j
\mu\big(B_{r_k}(x_k)\times B_{r_k}(x_k)\big)\le
\mu(\R/\Z\times \R/\Z)\le \liminf_{n\to\infty}\mu_n\big(\R/\Z\times
\R/\Z\big)\le R,
$$
which establishes \eqref{eq:finitely-many}.

Our last claim in this step says that the measure $\mu$ is uniformly
small on small sets off $W_\varepsilon$. More precisely,
\begin{equation}\label{eq:unif-small-mu}
\textnormal{There exists $\rho_\mu>0$, such that
$\mu\big((B_{\rho_\mu}(z)\times B_{\rho_\mu}(z))\setminus W_\varepsilon\big)
\le 2\varepsilon$\,\, for all $z\in\R/\Z.$}
\end{equation}
To prove this define the restricted measures 
(cf.\@ \cite[Definition 1.2]{evans-gariepy_2015}) 
$\bar{\mu}:=\mu\measurerestr [(\R/\Z\times\R/\Z)\setminus
W_\varepsilon ]$ satisfying
\begin{equation}\label{eq:restricted-measure}
\bar{\mu}(A)=\mu\big([(\R/\Z\times\R/\Z)\setminus W_\varepsilon ]\cap A\big)
=\mu\big(A\setminus W_\varepsilon)\quad
\text{for Lebesgue measurable }
A\subset\R/\Z\times\R/\Z,
\end{equation}
and assume for contradiction, that for every $k\in\N$ there is
a parameter $z_k\in\R/\Z$ such that $\bar{\mu}\big(B_\frac1k (z_k)
\times B_\frac1k (z_k)\big)>2\varepsilon.$ We may assume that $z_k\to
z_0\in\R/\Z$ as $k\to\infty$, so that for every $r>0$ there is an 
index $k_0\in\N$ such that 
$|z_k-z_0|<\frac{r}2$ for all $k\ge k_0$, which implies for all 
$k\ge\max\{k_0,\frac2{r}\}$
$$
|u-z_0|\le |u-z_k|+|z_k-z_0|<\frac1{k}+\frac{r}2\le r\quad\Foa
u\in B_\frac1k (z_k).
$$
Consequently,
\begin{equation}\label{eq:widerspruch-mubar}
\textstyle
\bar{\mu}\big( B_r(z_0)\times B_r(z_0)   \big)
\ge\bar{\mu}\big( B_\frac1k (z_k)\times B_\frac1k (z_k)  \big)
>2\varepsilon\quad\Foa r>0,\,k\ge\max\{k_0,\frac2{r}\}.
\end{equation}
{\it Case 1.}\,
If $z_0\not\in V_\varepsilon$ then by definition of $W_\varepsilon,$
by \eqref{eq:diagonal}, \eqref{eq:restricted-measure}, and
\eqref{eq:widerspruch-mubar},
$$
\varepsilon\ge\lim_{r\downarrow 0}\mu\big(B_r(z_0)\times B_r(z_0) \big)
\overset{\eqref{eq:restricted-measure}}{\ge}
\lim_{r\downarrow 0}\bar{\mu}\big(B_r(z_0)\times B_r(z_0)\big)
\overset{\eqref{eq:widerspruch-mubar}}{\ge}2\varepsilon,
$$
contradiction.

{\it Case 2.}\,
If $z_0\in V_\varepsilon$, then write $\{z_0\}\times\{z_0\}=
\bigcap_{r>0}(B_r(z_0)\times B_r(z_0))$ to obtain by virtue
of \eqref{eq:diagonal}, \eqref{eq:restricted-measure}, 
\cite[Theorem~1.2(iv)]{evans-gariepy_2015}, and \eqref{eq:widerspruch-mubar},
\begin{align*}
0 & =
\mu(\emptyset)\overset{\eqref{eq:diagonal}}{=}
\mu\big((\{z_0\}\times\{z_0\})\setminus W_\varepsilon\big)
\overset{\eqref{eq:restricted-measure}}{=}\textstyle
\bar{\mu}\big(\bigcap_{r>0}(B_r(z_0)\times B_r(z_0)\big)\\
&
 = \lim_{r\downarrow 0}\bar{\mu}\big(B_r(z_0)\times B_r(z_0)\big)
\overset{\eqref{eq:widerspruch-mubar}}{\ge} 2\varepsilon,
\end{align*}
again a contradiction. This completes the proof of our claim
\eqref{eq:unif-small-mu}.

{\it Step 4. Identifying a suitable approximating knot $\g_{n_0}$.}\,
For any fixed parameter $x\in\R/\Z$ we estimate the measure $\mu$ on annuli
$A_{r,\theta}(x)=B_r(x)\setminus B_{\theta r}(x)$ as
\begin{align*}
0 & \le \mu\big( \overline{A_{r,\theta}(x)}\times
\overline{A_{r,\theta}(x)}\big)\le
\mu\big((B_{2r}(x)\setminus B_{\theta r}(x))\times
(B_{2r}(x)\setminus B_{\theta r}(x))\big)\\
& = \mu\big( B_{2r}(x)\times B_{2r}(x) \big)-
\mu\big( B_{\theta r}(x)\times B_{\theta r}(x)\big)
\to 0\quad\As r\to 0
\end{align*}
by virtue of \eqref{eq:limit-balls}. Thus, there is a radius $r_x>0$
such that
\begin{equation}\label{eq:small-annuli-measure}
\mu\big( \overline{A_{r,\theta}(x)}\times
\overline{A_{r,\theta}(x)} \big) <\textstyle\frac{\theta}2\quad\Foa
r\in (0,r_x],
\end{equation}
where $\theta$ is given in \eqref{eq:fix-theta}.
In particular, for the finitely many parameters in
$V_\varepsilon=\{x_1,\ldots,x_N\}$, $N\le\lceil\frac{R}\varepsilon
\rceil$ we find radii $r_l:=r_{x_l}>0$ such that
\begin{equation}\label{eq:small-annuli-measure-xl}
\mu\big( \overline{A_{r,\theta}(x_l)}\times
\overline{A_{r,\theta}(x_l)} \big) 
<\textstyle\frac{\theta}2\quad\Foa
r\in (0,r_l],\,\,l=1,\ldots,N.
\end{equation}
Now set
\begin{equation}\label{eq:final-radius}
\bar{r}:=
\textstyle
\min\big\{\rho_\mu,r_1,\ldots,r_N,r_\g,\frac1{4p},\frac14\min\{|x_i-x_k|:
i\not=k,i,k\in\{1,\ldots,N\}\,\big\} >0,
\end{equation}
where $\rho_\mu>0$ is the radius such that \eqref{eq:unif-small-mu}
holds, and $r_\g>0$ is the scale at which $\g$ satisfies the
distortion estimate \eqref{eq:local-distortion-limit}, and $p\in\N\setminus
\{1\}$ determines the prescribed rotational symmetry defined in \eqref{eq:rot-symm}.
Inequality \eqref{eq:small-annuli-measure-xl} implies in particular that
\begin{equation}\label{eq:small-annuli-measure-xl-unif}
\mu\big( \overline{A_{r,\theta}(x_l)}\times
\overline{A_{r,\theta}(x_l)} \big)
<\textstyle\frac{\theta}2\quad\Foa
r\in (0,\bar{r}],\,\,l=1,\ldots,N.
\end{equation}
For the fixed radius $r:
=\bar{r}$ we use the weak convergence \eqref{eq:weak-convergence} to find for each $l\in\{1,\ldots,N\}$ some index $n_l\in\N$ such
that by \cite[Theorem~1.40]{evans-gariepy_2015}
$\mu_n(\overline{A_{\bar{r},\theta}(x_l)}\times
\overline{A_{\bar{r},\theta}(x_l)})<\theta$ for all $n\ge n_l$, so that
\begin{equation}\label{eq:unif-small-measures-annuli-indices}
\mu_n\big(\overline{A_{\bar{r},\theta}(x_l)}\times
\overline{A_{\bar{r},\theta}(x_l)})
<\theta\quad\Foa l=1,\ldots,N,\,n\ge n_*,
\end{equation}
where $n_*:=\max\{n_l:l=1,\ldots,N\}$.
By means of the uniform convergence in \eqref{eq:unif-subconvergence}
we may choose $n_{**}\in\N,$ $n_{**}\ge n_*$ such that
\begin{equation}\label{eq:linfty-close-approx}
\|\g_n-\g\|_{L^\infty}\le\textstyle \frac1{128}\cdot\frac{\bar{r}}L
\quad\Foa n\ge n_{**}.
\end{equation}
Now choose finitely many parameters $y_1,\ldots,y_K\in \R/\Z\setminus
B_{\bar{r}}(V_\varepsilon)$, such that
\begin{equation}\label{eq:covering-complement-Veps}
\R/\Z\setminus \overline{B_{\frac34 \bar{r}}(V_\epsilon)}
\subset\bigcup_{k=1}^K B_{\frac14 \bar{r}}(y_k).
\end{equation}
In particular, from $y_1,\ldots,y_K\notin B_{\bar{r}}(V_\varepsilon)$ we infer that
\begin{equation}\label{eq:covering-intersect}
B_{\frac58 \bar{r}}(V_\epsilon)\cap\bigcup_{k=1}^K B_{\frac38 \bar{r}}(y_k)
=\emptyset.
\end{equation}
Then use the weak convergence \eqref{eq:weak-convergence} again to
find an index $n_0\ge n_{**}$ such that in view of \eqref{eq:unif-small-mu}
\begin{equation}\label{eq:max-mu-n0}
\max_{k=1,\ldots,K}\textstyle
\mu_{n_0}\big(\overline{B_{\frac12 \bar{r}}(y_k)}\times
\overline{B_{\frac12 \bar{r}}(y_k)}\big)\le 3\varepsilon,
\end{equation}
which is possible, since by \cite[Theorem~1.40]{evans-gariepy_2015} and
by our choice of $\bar{r}$ in \eqref{eq:final-radius} and of the
parameters $y_1,\ldots,y_K\in\R/\Z\setminus B_{\bar{r}}(V_\varepsilon)$,
\begin{align*}

&\limsup_{n\to\infty}\mu_n\big(\overline{B_{\frac12 \bar{r}}(y_k)}
\times
\overline{B_{\frac12 \bar{r}}(y_k)}\big)
\overset{\eqref{eq:weak-convergence}}{\le}
\mu\big(\overline{B_{\frac12 \bar{r}}(y_k)}
\times
\overline{B_{\frac12 \bar{r}}(y_k)}\big)\le
\mu\big(B_{\frac34 \bar{r}}(y_k)
\times B_{\frac34 \bar{r}}(y_k)\big)\\
& = \mu\big(B_{\frac34 \bar{r}}(y_k)
\times B_{\frac34 \bar{r}}(y_k)\setminus W_\varepsilon\big)
\overset{\eqref{eq:final-radius}}{\le}
\mu\big((B_{\rho_\mu}(y_k)
\times
B_{\rho_\mu}(y_k))\setminus W_\varepsilon\big)
\overset{\eqref{eq:unif-small-mu}}{\le}
2\varepsilon\Foa k=1,\ldots,K.
\end{align*}
Summarizing \eqref{eq:unif-small-measures-annuli-indices},
\eqref{eq:linfty-close-approx}, and \eqref{eq:max-mu-n0},
we arrive at
\begin{equation}\label{eq:summary-n0}
\textstyle
\begin{cases}
\mu_{n_0}\big(\overline{A_{\bar{r},\theta}(x_l)}\times
\overline{A_{\bar{r},\theta}(x_l)}\big)<\theta & \Foa l=1,\ldots,N,\\
\mu_{n_0}\big(B_{\frac{\bar{r}}2}(y_k)\times
B_{\frac{\bar{r}}2}(y_k)\big)\le 3\varepsilon &\Foa k=1,\ldots,K,\\
\|\g_{n_0}-\g\|_{L^\infty} \le \frac1{128}\cdot\frac{\bar{r}}L.
\end{cases}
\end{equation}

{\it Step 5. Cutting out concentrations of $\g_{n_0}$ and harmonic 
substitution.}\,
Now we modify the knot
$\g_{n_0}$ in each ball $B_{\bar{r}}(x_i)\subset\R/\Z$, $x_i\in
V_\varepsilon,$ $i=1,\ldots,N,$ where $\bar{r}$ is defined in 
\eqref{eq:final-radius}. We do that as in \eqref{eq:modified-curve}
by choosing suitable truncation points $x_\pm^i\in G_\pm^i:=
G_\pm(x_i,\theta,\bar{r})$, where the sets $G_\pm^i$ are defined
as in \eqref{eq:G-set} for $x:=x_i$, $r:=\bar{r}$, and
$\theta:=\theta_4<\theta_3=(64L)^{-8}$ (see  \eqref{eq:fix-theta}),
to obtain the modified curve
\begin{equation}\label{eq:gamma-n0-modified}
\tilde{\gamma}_{n_0}(z):=\begin{cases}
\gamma_{n_0}(x_-^i)+\frac{z-x_-^i}{x_+^i-x_-^i}\big(\gamma_{n_0}(x_+^i)
-\gamma_{n_0}(x_-^i)\big) & \Fo
z\in [x_-^i,x_+^i], i=1\ldots,N,\\
\gamma_{n_0}(z) & \Fo z\in\R/\Z\setminus\bigcup_{i=1}^N[x_-^i,x_+^i].
\end{cases}
\end{equation}
If $V_\varepsilon=\emptyset$ then simply set $\tilde{\gamma}_{n_0}:=
\gamma_{n_0}$. We infer from $\bilip(\g_{n_0})\ge\frac1{L}$ 
(since $\g_{n_0}\in\mathcal{F}_{p,L,R}(\mathcal{K})$)
and
\eqref{eq:bilip-tilde-eta} in
Lemma \ref{lem:bilip-control-harmonic} for $\eta:=\g_{n_0}$,
that there is a constant $\tilde{L}\in [L,2L]$ such that
\begin{equation}\label{eq:bilip-tildegamma}
\textstyle
|\tilde{\g}_{n_0}(y)-\tilde{\g}_{n_0}(z)|\ge
\frac1{\tilde{L}}d_{\tilde{\g}_{n_0}}(y,z)
\quad\Foa y,z\in\R/\Z.
\end{equation}
Thus, $\tilde{\g}_{n_0}$ is embedded. Since $\g_{n_0}$ is assumed to be
of class $C^1(\R/\Z,\R^3)$, and we substituted the subarcs 
$\g_{n_0}([x_-^i,x_+^i])$ by straight segments with small
angels 
$\ANG\big(\g_{n_0}'(x_\pm^i),\frac{\g_{n_0}(x_+^i)-\g_{n_0}(x_-^i)}{
x_+^i-x_-^i}\big)$ for $i=1,\ldots,N$, we can modify the
arguments given by Crowell and Fox
in \cite[Appendix~I]{crowell-fox_1977} to show that 
the modified curve $\tilde{\g}_{n_0}$ is still tame\footnote{although 
$\tilde{\g}_{n_0}$ is in general not in $W^{\frac32,2}(\R/\Z,\R^3)$ 
anymore because of the harmonic substitution; 
cf.\@ Footnote~\ref{foot:harmonic-substitution}.}.
Let us briefly sketch their arguments and indicate the necessary
modifications, the details are then left to the reader.

For a given arclength parametrized $C^1$-knot $\eta$ and any angle
$\alpha\in (0,\alpha_0(\eta)]$, where the threshold angle $\alpha_0(\eta)$
depends on the modulus of continuity of the unit tangent $\eta'$,
Crowell and Fox construct a necklace of double cones (see
\cite[Figure 62]{crowell-fox_1977}) with apex angle $\alpha$,
such that the finitely many apices of these double cones form a closed
polygon $P$ inscribed in $\eta$, and such that $\eta$ intersects every
circular cross-section of each double cone exactly once
and is contained in that necklace. The inscribed
polygon $P$ does the same, which leads them to define a homeomorphism
of $\R^3$ which equals the identity outside the double cones, by
mapping within each cross-section the unique curve point of $\eta$ linearly
to the respective unique point on $P$ in that same cross-section;
see \cite[Figure 64]{crowell-fox_1977}. This way they show that $\eta$
and $P$ are equivalent to conclude that any such $C^1$-curve $\eta$
is tame. In our situation we proceed in the same way\footnote{Here it is important to let 
$m=\bilip\eta=\tilde L$ (not just $L$) 
in~\cite[Eq.~(6), p.~149]{crowell-fox_1977}.} 
with $\tilde{\eta}:=
\tilde{\g}_{n_0}|_{\R/\Z\setminus\bigcup_{i=1}^N [x_-^i,x_+^i]}$
obtaining $N$ open polygonal lines with endpoints $\tilde{\g}_{n_0}(x_\pm^i)$,
$i=1,\ldots,N$, forming the axes of $N$ disjoint necklaces each consisting
of mutually disjoint double cones (by choosing a suitably small 
apex angle $\alpha$ and sufficiently small distances between
neighboring apices). Taking the union of these $N$ polygonal lines with the
$N$ straight segments $\tilde{\g}_{n_0}([x_-^i,x_+^i]), $ $i=1,\ldots,N$,
defines a closed polygon $P$ inscribed in $\tilde{\g}_{n_0}$ (coinciding
with $\tilde{\g}_{n_0}$ in its straight segments). 
We will now show that for any
 $\alpha\in (0,\frac{\pi}4)$ one has
\begin{equation}\label{eq:small-beta-angle}
\beta:=\max_{i=1,\ldots,N}\textstyle
\max\big\{\ANG\big(\g_{n_0}'(x_-^i),\frac{\g_{n_0}(x_+^i)-\g_{n_0}(x_-^i)}{
x_+^i-x_-^i}\big),
\ANG\big(\frac{\g_{n_0}(x_+^i)-\g_{n_0}(x_-^i)}{
x_+^i-x_-^i},\g_{n_0}'(x_+^i)\big)
\big\} < \pi -2\alpha,
\end{equation}
to prevent intersections of any segment $\tilde{\g}_{n_0}([x_-^i,x_+^i])$
with their neighboring double cones. 
Indeed, \eqref{eq:small-beta-angle} is guaranteed by inequality
\eqref{eq:difference-quotients} of Lemma \ref{lem:difference-quotients},
which implies for $\nu_i:=\nu_{B_{\bar{r}}(x_i)}\in\S^{n-1}$ defined
as in \eqref{eq:bmo3},
\begin{align*}
\cos\ANG\big(\g_{n_0}'(x_\pm^i),\nu_i\big)& =
\textstyle
\langle\g_{n_0}'(x_\pm^i),\nu_i
\rangle_{\R^3}=\lim_{s\to 0}\big\langle 
\frac{\g_{n_0}(x_\pm^i+s)-\g_{n_0}(x_\pm^i)}{s},\nu_i\big\rangle_{\R^3}
\overset{\eqref{eq:difference-quotients}}{\ge}
1-2\theta^\frac14,
\end{align*}
and also
\begin{align*}
\textstyle
\cos\ANG\big(\frac{\g_{n_0}(x_+^i)-\g_{n_0}(x_-^i)}{
|\g_{n_0}(x_+^i)-\g_{n_0}(x_-^i)|},\nu_i\big)& =
\big\langle
\frac{\g_{n_0}(x_+^i)-\g_{n_0}(x_-^i)}{x_+^i-x_-^i},\nu_i
\big\rangle_{\R^3}\cdot\frac{x_+^i-x_-^i}{|\g_{n_0}(x_+^i)-\g_{n_0}(x_-^i)|}
\overset{\eqref{eq:difference-quotients}}{\ge}
1-2\theta^\frac14.
\end{align*}
With $\theta<\theta_3\le 64^{-8}$ we find $1-2\theta^\frac14\ge 1-\frac1{128}
>\frac{\sqrt{3}}2,$ so that $\beta
<\frac{\pi}3,$
which implies \eqref{eq:small-beta-angle}.
In order to show that no segment $\tilde{\g}_{n_0}([x_-^i,x_+^i])$
interferes with other parts of the curve, we argue as in~\cite[(I.6), p.~150]{crowell-fox_1977}.

Notice that if $V_\varepsilon\not=\emptyset$ with  some point
$\xi_1\in V_{\varepsilon},$ then by symmetry of $\g_{n_0}$ also the 
points $\xi_j:=\xi_1+\frac{j-1}p\in\R/\Z$ for $j=2,\ldots,p$, are contained
in $V_\varepsilon$, 
so that $\sharp V_\varepsilon\ge 2$.

We are now going to employ the harmonic substitution.
If we replace a part of a curve by a straight line, we may face both global and local effects.
A global effect means that a strand of $\g|_{\R/\Z\setminus B_{\bar r}(x_i)}$ might interfere
with the substitution.
This means that there are some $\xi\in[x_i^-,x_i^+]$, $z\in \R/\Z\setminus B_{\bar r}(x_i)$
such that $\g_{n_0}(z)$ lies on the closed
segment with endpoints $\g_{n_0}(\xi)$ and 
$\tilde\g_{n_0}(\xi)$. 
(We can disregard points in $[x_i-\bar r,x_i^-]$ and $[x_i^+,x_i+\bar r]$ due to small local distortion.)
But in this case we find
\[ \textstyle \frac{3\bar r}{8L}\le \frac1Ld_{\g_{n_0}}(z,\xi)\le |\g_{n_0}(z)-\g_{n_0}(\xi)|
\le |\tilde\g_{n_0}(\xi)-\g_{n_0}(\xi)| \le \|\tilde\g_{n_0}-\g_{n_0}\| \le 6\theta^{1/8}\bar r \]
which implies $1\le\frac83L\cdot6\theta^{1/8}=\frac1{48}$, a contradiction.
It remains to consider local effects.
So,
if any of the subarcs $\g_{n_0}([x_-^i,x_+^i])$ (trivially extended to
infinity) were non-trivially knotted, then by symmetry of $\g_{n_0}$
there are at least two such non-trivially knotted subarcs, which implies
that $\g_{n_0}$ is a composite knot, contradicting our assumption.
Consequently, the subarcs $\g_{n_0}([x_-^i,x_+^i])$ are topologically
trivial for $i=1,\ldots,N$, and these subarcs were replaced by the
topologically trivial straight segments $\tilde{\g}_{n_0}(
[x_-^i,x_+^i])$, which implies that $\g_{n_0}$ is equivalent to
$\tilde{\g}_{n_0}$, i.e., $[\g_{n_0}]=[\tilde{\g}_{n_0}]$.

{\it Step 6. The final local distortion estimate for
the modified curve $\tilde{\g}_{n_0}$.}\,
For any $\xi\in\R/\Z$ one either has $\xi\in\overline{B_{\frac34 \bar{r}}(
V_\varepsilon)}$, in which case there exists $i\in\{1,\ldots,N\}$ 
with $x_i\in V_\varepsilon$, such that
\begin{equation}\label{eq:xi-contain1}
B_{\frac18\bar{r}}(\xi)\subset 
B_{\bar{r}}(x_i),
\end{equation}
or, by the covering \eqref{eq:covering-complement-Veps}, there exists
$k\in\{1,\ldots,K\}$ such that $\xi\in B_{\frac14 \bar{r}}(y_k)$, so that
\begin{equation}\label{eq:xi-contain2}
B_{\frac18\bar{r}}(\xi)\subset B_{\frac38 \bar{r}}(y_k).
\end{equation}
If \eqref{eq:xi-contain1} holds true then $B_{\frac18\bar{r}}(\xi)$
is either contained in the interval $[x_i-\bar{r},x_+^i]$ or in
$[x_-^i,x_i+\bar{r}]$ so that we may apply \eqref{eq:linfty-dist-theta}
of Lemma \ref{lem:harmonic-substitution} to the curve $\eta:=
\g_{n_0}$, to the parameters $x_1,\ldots,x_N\in V_\varepsilon$,
the radius $r:=\bar{r}$, and $\theta=\theta_4\in (0,\theta_2)$ (see
\eqref{eq:fix-theta}), to obtain




\begin{equation}\label{eq:distortion-tildegamma1}
\sup_{y,z\in B_{\frac18 \bar{r}}(\xi)\atop y\not= z}\textstyle
\frac{d_{\tilde{\g}_{n_0}}(y,z)}{|\tilde{\g}_{n_0}(y)-
\tilde{\g}_{n_0}(z)|}< 1+4\theta^\frac14<\frac{\pi}3<\frac{\pi}{\sqrt{8}}
<g_3=\frac{\sqrt{32}}{\sqrt{27}}\cdot
\frac{\pi}{\sqrt{8}}.
\end{equation}
If, on the other hand, \eqref{eq:xi-contain2} is true, then we know
from \eqref{eq:covering-intersect} and our construction of 
$\tilde{\g}_{n_0}$,  which implies in particular that $\tilde{\g}_{n_0}=
\g_{n_0}$ on $\R/\Z\setminus B_{\frac58 \bar{r}}(V_\varepsilon)$,
that
\begin{equation}\label{eq:coincidence-gamma-tildegamma}
\tilde{\g}_{n_0}=\g_{n_0}\quad\ON B_{\frac38 \bar{r}}(y_k).
\end{equation}
By means of \eqref{eq:summary-n0} we infer
\begin{equation}\label{eq:small-mu-n0-measure}
\lfloor\g_{n_0}'\rfloor^2_{\frac12,2,B_{\frac38 \bar{r}}(y_k)}=
\mu_{n_0}\big(B_{\frac38 \bar{r}}(y_k)\times B_{\frac38 \bar{r}}(y_k)\big)
\le 3\varepsilon,
\end{equation}
which we combine with \eqref{eq:seminorm-bilip2} in Corollary
\ref{cor:seminorm-bilip} for $\g:=\g_{n_0}$ to conclude
\begin{align}
\label{eq:distortion-tildegamma2}
\sup_{y,z\in B_{\frac18 \bar{r}}(\xi)\atop y\not= z}
\textstyle
\frac{d_{\tilde{\g}_{n_0}}(y,z)}{|\tilde{\g}_{n_0}(y)-
\tilde{\g}_{n_0}(z)|}&
\overset{\eqref{eq:xi-contain2},\eqref{eq:coincidence-gamma-tildegamma}}{\le}
\sup_{y,z\in B_{\frac38 \bar{r}}(y_k)\atop y\not= z}
\textstyle
\frac{d_{\g_{n_0}}(y,z)}{|\g_{n_0}(y)-\g_{n_0}(z)|}
\overset{\eqref{eq:seminorm-bilip2},\eqref{eq:small-mu-n0-measure}}{\le}
\frac1{\sqrt{1-\frac32 \varepsilon}}
\overset{\eqref{eq:epsilon-choice}}{=}\frac{\pi}3<\frac{\pi}{\sqrt{8}}<g_3,
\end{align}
by our choice of $\varepsilon$ in \eqref{eq:epsilon-choice}.
In view of \eqref{eq:distortion-tildegamma1} and
\eqref{eq:distortion-tildegamma2} we have shown that, by continuity of
$\tilde{\g}_{n_0}$,
\begin{equation}\label{eq:distortion-tildegamma}
\sup_{y,z\in\R/\Z\atop 0<d_{\tilde{\g}_{n_0}}(y,z)\le\frac14\bar{r}}
\textstyle
\frac{d_{\tilde{\g}_{n_0}}(y,z)}{|\tilde{\g}_{n_0}(y)-
\tilde{\g}_{n_0}(z)|}\le\frac{\pi}3< g_3.
\end{equation}
According to \eqref{eq:bilip-tildegamma}  we have for two parameters
$y,z\in\R/\Z$ with intrinsic distance $d_{\tilde{\gamma}_{n_0}}(y,z)
>\frac14\bar{r}$ the estimate
$$
\textstyle
\frac14\bar{r}<d_{\tilde{\gamma}_{n_0}}(y,z)\le\tilde{L}
|\tilde{\g}_{n_0}(y)-
\tilde{\g}_{n_0}(z)|\le 2L|\tilde{\g}_{n_0}(y)-
\tilde{\g}_{n_0}(z)|.
$$
Therefore, \eqref{eq:distortion-tildegamma} implies for the local
distortion of $\tilde{\g}_{n_0}$
\begin{equation}
\textstyle\delta(\tilde{\g}_{n_0},r_{\tilde{\g}_{n_0}})\le\frac{\pi}3<\frac{\pi}{\sqrt{8}}<g_3
\end{equation}
at scale $r_{\tilde{\g}_{n_0}}:=\frac1{16L}\bar{r}.$ In order to apply
Corollary \ref{cor:equiv-knots} to $\g_1:=\g$ and $\g_2:=\tilde{\g}_{n_0}$ 
it suffices to verify by means of \eqref{eq:summary-n0} and 
\eqref{eq:linfty-dist-theta} in Lemma \ref{lem:harmonic-substitution}
for $\eta:=\g_{n_0}$
\begin{eqnarray*}
\|\g-\tilde{\g}_{n_0}\|_{L^\infty}&\le &\|\g-\g_{n_0}\|_{L^\infty}+
\|\g_{n_0}-\tilde{\g}_{n_0}\|_{L^\infty}\\
&\overset{\eqref{eq:summary-n0},\eqref{eq:linfty-dist-theta}}{<}&
\textstyle
\frac1{128L}\bar{r}+6\theta^\frac18\bar{r}
\overset{\eqref{eq:fix-theta}}{=}\frac1{64L}\bar{r}\le\frac14\min\{
r_\g,r_{\tilde{\g}_{n_0}}\}.
\end{eqnarray*}
Therefore, we deduce $\mathcal{K}=
[\g_{n_0}]=[\g]$ by Corollary \ref{cor:equiv-knots}. \hfill $\Box$
