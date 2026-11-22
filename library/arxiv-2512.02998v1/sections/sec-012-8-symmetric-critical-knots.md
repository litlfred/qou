---
doc_id: arxiv-2512.02998v1
doc_title: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy"
section_id: sec-012-8-symmetric-critical-knots
section_title: "Symmetric critical knots"
section_number: 8
pages: 29-31
source_pdf: 2512.02998v1.pdf
source_sha256: 146ff93cd70baad4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.954
doc_brief: "Stability of knot equivalence at low regularity, and symmetric critical knots for the M\'obius energy — We present sufficient criteria for the equivalence of tame knots at low regularity."
---
\label{sec:symm-critical}
In this section we are going to use our weak compactness result, Theorem
\ref{thm:fractional-compactness}, to prove the existence of rotationally
symmetric critical knots for the M\"obius energy.

{\it Proof of Theorem~\ref{thm:symm-crit-prime}.}\,
Since $\Sigma_p(\mathcal{K})$ contains a knot with finite M\"obius energy,
the knot equivalence class $\mathcal{K}$ is tame according to
\cite[Theorem~4.1]{freedman-etal_1994}, 
the infimum of the energy is finite, and there is a minimizing sequence
$(\g_m)_m\subset\Sigma_p(\mathcal{K})$ with 
$$
\emob(\g_m)\to\inf_{\Sigma_p(\mathcal{K})}\emob(\cdot)<\infty\quad
\As m\to\infty.
$$
Due to parameter invariance of $\emob$ and because
rescaling to unit length and subsequent
reparametrization to arclength preserves the knot equivalence class,
and also the $p$-rotational symmetry 
\eqref{eq:rot-symm} according to 
\cite[Lemma 4.6]{gilsbach-vdm_2018}\footnote{see
 version 2 in \cite[Lemma 4.6]{gilsbach-vdm_2017} for the corrected proof.},
we may assume without loss
of generality that $|\g_m'|=1$  a.e.\@ on $\R/\Z$ for all $m$. In order
to apply Theorem~\ref{thm:fractional-compactness} we use convolutions
$\g_{m,\epsilon_m}\in C^\infty(\R/\Z,\R^3)$, $\epsilon_m\to 0 $ as 
$m\to\infty$, 
their
rescalings $\hat{\g}_{m,\epsilon_m}:=(\mathcal{L}(\g_{m,\epsilon_m}))^{-1}
\g_{m,\epsilon_m}$, and reparametrize $\hat{\g}_{m,\epsilon_m}$ to 
arclength to obtain $\G_m\in C^\infty(\R/\Z,\R^3)$ with $|\G_m'|=1$
a.e.\@ on $\R/\Z$ for all $m\in\N$, such that
$$
\emob(\G_m)\le\emob(\g_m)+\frac1{m}\quad\Foa m\in\N,
$$
which is possible due to
\cite[Theorems 1.1, 1.3 \& 1.4]{blatt_2019b}. Especially 
\cite[Theorem~1.3]{blatt_2019b} in combination with Corollary 
\ref{cor:fractional-stability}
of the present paper allows us to assume that $[\G_m]=[\g_m]=
\mathcal{K}$ for all $m\in\N$.
As before, this mollification,
 rescaling, and
 subsequent reparametrization to arclength preserves the 
 $p$-rotational
 symmetry defined in \eqref{eq:rot-symm},
 so that $\G_m\in\Sigma_p(\mathcal{K})$ for  all $m\in\N$.

 This new $\emob$-minimizing sequence $(\G_m)_m$ has
 equibounded M\"obius energy, which yields a uniform bound on the 
 seminorms $\lfloor \G_m'\rfloor_{\frac12,2}$ according to
  \cite[Theorem~1.1]{blatt_2012a}
 or \cite[Theorem~3.2(i)]{gilsbach-vdm_2018}, as well as a uniform bilipschitz constant
 $L$ depending only on the uniform energy bound; see 
 \cite[Theorem~2.3]{ohara_1992a}.
 So, for each $m\in\N$, the curve $\G_m$ is contained in the class
 $\mathcal{F}_{R,L,p}$ as defined in 
 \eqref{eq:compact-subset}
 for $R:=\sup_{m\in\N}\lfloor \G_m'\rfloor^2_{\frac12,2}$,
 where we assumed (by translational invariance of $\emob$) that 
 $\G_m(0)=0\in\R^3$ for all $m\in\N$.

Consequently, Theorem~\ref{thm:fractional-compactness} implies the existence
of a limiting arclength parametrized knot $\G\in\mathcal{F}_{R,L,p}$ such that
a subsequence (still denoted by $\G_m$) converges weakly in 
$W^{\frac32,2}$ and uniformly to $\G$ as $m\to\infty$.
The 
lower semicontinuity of $\emob$ (see \cite[Lemma 4.2]{freedman-etal_1994})
implies
\begin{equation}\label{eq:inf-emob}
\inf_{\Sigma_p(\mathcal{K})}\emob(\cdot)
\le\emob(\G)\le\liminf_{m\to\infty}\emob(\G_m)=\inf_{\Sigma_p(\mathcal{K})}
\emob(\cdot);
\end{equation}
hence $\G$ is the desired symmetric minimizing prime knot.

It remains to be verified that $\G$ is critical for the M\"obius energy on its full domain, because then $\G\in C^\omega(\R/\Z,\R^3)$ due to
\cite[Corollary 1.3]{blatt-vorderobermeier_2019}.
For that notice first that we can proceed exactly as
in the proof of Corollary \ref{cor:fractional-stability}
to find a scale $r_\G>0$ for
the arclength parametrized $W^{\frac32,2}$-knot $\G$, such that
$\delta(\G,r_\G)< g_3$.
We symmetrize any variational vector $h\in C^\infty(\R/\Z,\R^3)$ according to
\begin{equation}\label{eq:symmetrize}
\textstyle
h_\textnormal{sym}(u):=\sum_{k=1}^p\Rot_{-\frac{2\pi k}p}\circ h(u+\frac{k}p)
\quad\Fo u\in\R/\Z,
\end{equation}
to obtain by virtue of Corollary \ref{cor:lipschitz-stability}
a number $\epsilon_{\G,h}>0$ such that the perturbed curves
$\Upsilon_\epsilon:=\G+\epsilon h_\textnormal{sym}$ are immersed knots
equivalent to $\G$ for all $|\epsilon|\le\epsilon_{\G,h}.$
Regarding $p$-rotational symmetry we compute (using \eqref{eq:rot-symm} for
$\G$)
\begin{align*}
\textstyle
&\Rot_{\frac{2\pi}p}\circ\Upsilon_\epsilon(u-\frac1{p})
\textstyle
=\Rot_{\frac{2\pi}p}\circ\G(u-\frac1p)+\epsilon\Rot_{\frac{2\pi}p}\circ
h_\textnormal{sym}(u-\frac1p)\\
&\textstyle\overset{\eqref{eq:rot-symm}}{=}
\G(u)+\epsilon\sum_{k=1}^p\Rot_{-\frac{2\pi}p(k-1)}\circ
h(u+\frac{k-1}p)
= \G(u)+\epsilon\sum_{k=1}^{p-1}\Rot_{-\frac{2\pi k}p}
\circ h(u+\frac{k}p)+\epsilon h(u)\\
&=\G(u)+\epsilon\sum_{k=1}^p
\Rot_{-\frac{2\pi k}p}\circ h(u+\frac{k}p)
 = \G(u)+\epsilon h_\textnormal{sym}(u)=\Upsilon_\epsilon (u)\quad\Foa
u\in\R/\Z,\,|\epsilon|\le\epsilon_{\G,h}.
\end{align*}
Hence $\Upsilon_\epsilon\in\Sigma_p(\mathcal{K})$ and \eqref{eq:inf-emob}
implies
$$
\emob(\G)\le

\emob(\Upsilon_\epsilon)=
\emob(\G+\epsilon h_\textnormal{sym})\quad\Foa |\epsilon|\le\epsilon_{\G,h}.
$$
Therefore, taking the first variation $\delta\emob(\G,\cdot)$, which is linear in 
its second entry,
\begin{equation}\label{eq:variation}
\textstyle
0=\delta\emob(\G,h_\textnormal{sym})=\sum_{k=1}^p\delta\emob\big(\G,
\Rot_{-\frac{2\pi k}p}\circ h (\cdot +\frac{k}p)\big).
\end{equation}
Furthermore, from the symmetry \eqref{eq:rot-symm}
of $\G$ and the invariance of $\emob$ under
rotations and reparametrizations one deduces 
for every $k\in\{1,\ldots,p\}$
\begin{align*}
\textstyle
\emob\big(&\textstyle\G(\cdot)+\epsilon\Rot_{-\frac{2\pi k}p}\circ h(\cdot+\frac{k}p)\big)
\overset{\eqref{eq:rot-symm}}{=}
\textstyle
\emob\big(\Rot_{-\frac{2\pi k}p}\circ\G(\cdot +\frac{k}p)
+\epsilon\Rot_{-\frac{2\pi k}p}\circ h(\cdot+\frac{k}p)\big)\\
& \textstyle
=\emob\big(\Rot_{-\frac{2\pi k}p}\circ [\G(\cdot +\frac{k}p)+\epsilon
h(\cdot+\frac{k}p)]\big)=
\emob\big(\G(\cdot +\frac{k}p)+\epsilon
h(\cdot+\frac{k}p)\big)=\emob(\G+\epsilon h),
\end{align*}
which implies 
$$
\textstyle
\delta\emob\big(\G,\Rot_{-\frac{2\pi k}p}\circ h(\cdot +
\frac{k}p)\big)
\!=\!\frac{d}{d\epsilon} |_{\epsilon=0}
\emob\big(\G+\epsilon\Rot_{-\frac{2\pi k}p}\circ h(\cdot +\frac{k}p)
\big)\!=\!
\frac{d}{d\epsilon} |_{\epsilon=0}
\emob(\G+\epsilon h)\!=\!\delta\emob(\G,h)
$$
for all $k=1,\ldots,p$.
Therefore, by \eqref{eq:variation},
$$
\textstyle
0=\sum_{k=1}^p\delta\emob\big(\G,\Rot_{-\frac{2\pi k}p}\circ h(
\cdot +\frac{k}p)\big)=p\delta\emob(\G,h),
$$
which leads to the desired criticality, since by continuity of the first variation
we may approximate an arbitrary variational vector field $h\in W^{\frac32,2}(
\R/\Z,\R^3)$ by smooth vector fields, for which the first variation
has just been shown to vanish.

In the specific case of torus knot classes $\mathcal{K}=\mathcal{T}(a,b)$
for co-prime integers $a,b\in\Z\setminus\{0,\pm 1\}$ we can proceed
exactly as in the proof of \cite[Theorem~1.2]{gilsbach-vdm_2018}
to show that there
are at least two different $\emob$-critical torus knots
$\G_1,\G_2$ in $\mathcal{T}(a,b)$ for each 
co-prime integers $a,b\in\Z\setminus\{0,\pm 1\}$. The only prerequisite
for that proof is the existence of symmetric energy
minimizers for different
rotational symmetries, which can be  obtained as above for $\emob$ on 
the symmetric subsets
$\Sigma_{p_i}(\mathcal{T}(a,b))$, $i=1,2$, for $p_1=a$ and $p_2=b$.
\hfill $\Box$
