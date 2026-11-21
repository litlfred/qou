---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-015-41-berry-esseen-estimates
section_title: "Berry-Esseen estimates"
section_number: 4.1
pages: 26-29
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 0.908
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
As explained above, we start by establishing some Berry-Esseen estimates in the setting of mod-$\phi$ convergence.

\begin{proposition}[Berry-Esseen expansion]\label{prop:berryesseen}
We place ourselves under the assumptions of Definition \ref{def:modphi}, with $\phi$ non-lattice infinitely divisible law, and the strip $\mathcal{S}_{(c,d)}$ that contains $0$. Denote 
$$g(y)=\frac{1}{\sqrt{2\pi}}\,\E^{-y^{2}/2}$$
the density of a standard Gaussian variable, and $F_{n}(x)=\proba[X_{n}\leq t_{n}\eta'(0)+\sqrt{t_{n}\eta''(0)}\,x]$. One has
$$F_{n}(x)=\int_{-\infty}^{x} \left(1+\frac{\psi'(0)}{\sqrt{t_n\eta''(0)}}\,y+\frac{\eta'''(0)}{6\sqrt{t_{n}(\eta''(0))^{3}}}\,(y^{3}-3y)\right)g(y)\,dy+o\!\left(\frac{1}{\sqrt{t_n}}\right)$$
with the $o(\cdot)$ uniform on $\R$.
\end{proposition}
\medskip

\begin{proof}
We use the same arguments as in the proof of \cite[Theorem XVI.4.1]{Fel71}, but adapted to the assumptions of Definition \ref{def:modphi}. Given an integrable function $f$, or more generally a distribution, its Fourier transform is $f^{*}(\zeta)=\int_{\R}\E^{\I \zeta x}\,f(x)\,dx.$
Consider a probability law $F(x)=\int_{-\infty}^{x}f(y)\,dy$ with vanishing expectation $(f^{*})'(0)=0$; and $G(x)=\int_{-\infty}^{x}g(y)\,dy$ a $m$-Lipschitz function with $g^{*}$ continuously differentiable and
$$(g^{*})'(0)=0 \qquad;\qquad \lim_{y \to -\infty}G(y)=0\qquad ;\qquad\lim_{y \to +\infty}G(y)=1.$$ 
Then Feller's Lemma \cite[Lemma XVI.3.2]{Fel71} states that, for any $x\in \R$ and any $T>0$,
$$|F(x)-G(x)|\leq \frac{1}{\pi} \int_{-T}^{T} \left|\frac{f^{*}(\zeta)-g^{*}(\zeta)}{\zeta}\right|\, d\zeta +\frac{24m}{\pi T}.$$
Notice that this is true even when $f$ is a distribution. Define the auxiliary variables
$$Y_{n}=\frac{X_{n}-t_{n}\eta'(0)}{\sqrt{t_{n}\eta''(0)}}$$
We shall apply Feller's Lemma to the functions
\begin{align*}
    F_{n}(x)&=\text{cumulative distribution function of } 
    Y_n;\\
G_{n}(x)&=\int_{-\infty}^{x}\left(1+\frac{\psi'(0)}{\sqrt{t_{n}\eta''(0)}}\,y+\frac{\eta'''(0)}{6\sqrt{t_{n}(\eta''(0))^{3}}}\,(y^{3}-3y)\right)g(y)\,dy.
\end{align*}
Note that each $G_n$ is clearly a Lipschitz function (with a uniform Lipschitz constant, \emph{i.e.} that does not depend on $n$). Besides, by Lemma \ref{lem:gaussintegral}, \eqref{item:gaussfourier}, the Fourier transform corresponding to the distribution function $G_n$ is, setting $z=\I\, \zeta$,
\begin{equation}\label{eq:gnstar}
    g_n^*(\zeta)= \E^{\frac{z^{2}}{2}}\,\left(1+\frac{\psi'(0)\,z}{\sqrt{t_{n}\eta''(0)}}+\frac{\eta'''(0)\,z^{3}}{6\sqrt{t_{n}(\eta''(0))^{3}}}\right).
\end{equation}
Consider now $f_{n}^{*}(\zeta)$:
if $z=\I\, \zeta$, then
\begin{align*}
    f_{n}^{*}(\zeta) &= \esper \left[\E^{z\left(\frac{X_{n}-t_{n}\eta'(0)}{\sqrt{t_{n}\eta''(0)}}\right)}\right]=\exp\left(-z\sqrt{\frac{t_{n}}{\eta''(0)}}\,\eta'(0)\right)\times \varphi_{n}\left(\frac{z}{\sqrt{t_{n}\eta''(0)}}\right)\\
&=\exp\left(t_{n}\left(\eta\left(\frac{z}{\sqrt{t_{n}\eta''(0)}}\right)-\eta'(0)\,\frac{z}{\sqrt{t_{n}\eta''(0)}}\right)\right)\times \psi_{n}\!\left(\frac{z}{\sqrt{t_{n}\eta''(0)}}\right)
\end{align*}
But
\[ \psi_{n}\!\left(\frac{z}{\sqrt{t_{n}\eta''(0)}}\right) = \left(1+\frac{\psi'_n(0)\,z}{\sqrt{t_{n}\eta''(0)}}+o\!\left(\frac{z}{\sqrt{t_{n}}}\right)\right) = \left(1+\frac{\psi'(0)\,z}{\sqrt{t_{n}\eta''(0)}}+o\!\left(\frac{z}{\sqrt{t_{n}}}\right)\right)\]
where the $o$ is uniform in $n$ because of the local uniform convergence of the analytic functions $\psi_n$ to $\psi$ (and hence, of $\psi'_n$ and $\psi''_n$ to $\psi'$ and $\psi$). Thus
\begin{align}
    f_{n}^{*}(\zeta)&=\exp\left(\frac{z^{2}}{2}+\frac{\eta'''(0)\,z^{3}}{6\sqrt{t_{n}(\eta''(0))^{3}}}+|z|^{2}\,o\!\left(\frac{z}{\sqrt{t_{n}}}\right)\right)\times \left(1+\frac{\psi'(0)\,z}{\sqrt{t_{n}\eta''(0)}}+o\!\left(\frac{z}{\sqrt{t_{n}}}\right)\right)\nonumber\\
&=\E^{\frac{z^{2}}{2}}\,\left(1+\frac{\psi'(0)\,z}{\sqrt{t_{n}\eta''(0)}}+\frac{\eta'''(0)\,z^{3}}{6\sqrt{t_{n}(\eta''(0))^{3}}}+(1+|z|^{2})\,o\!\left(\frac{z}{\sqrt{t_{n}}}\right)\right).\label{eq:asymptoticsfouriertransforms}
\end{align}
Beware that in the previous expansions, the $o(\cdot)$ is 
$$o\!\left(\frac{z}{\sqrt{t_{n}}}\right)=\frac{|z|}{\sqrt{t_{n}}}\,\eps\!\left(\frac{z}{\sqrt{t_{n}}}\right)\quad \text{with } \lim_{t \to 0}\eps(t)=0.$$ 
In particular, $z$ might still go to infinity in this situation. To make everything clear we will continue to use the notation $\eps(t)$ in the following. Fix $0<\delta<\Delta$ and take $T=\Delta\sqrt{t_{n}}$.  Comparing~\eqref{eq:gnstar} and \eqref{eq:asymptoticsfouriertransforms} and using Feller's lemma, we get:
\begin{align}
|F_{n}(x)-G_{n}(x)|&\leq\frac{1}{\pi}\int_{-\Delta\sqrt{t_{n}}}^{\Delta\sqrt{t_{n}}} \left|\frac{f_{n}^{*}(\zeta)-g_{n}^{*}(\zeta)}{\zeta}\right|d\zeta + \frac{24m}{\Delta\pi\sqrt{t_{n}}}\nonumber\\
&\leq \frac{1}{\pi\sqrt{t_{n}}}\int_{-\delta\sqrt{t_{n}}}^{\delta\sqrt{t_{n}}} \E^{-\frac{\zeta^{2}}{2}}\,(1+|\zeta|^{2})\,\, \eps\!\left(\frac{\zeta}{\sqrt{t_{n}}}\right)\,d\zeta+\frac{24m}{\Delta\pi\sqrt{t_{n}}}\nonumber\\
&\quad+\frac{1}{\pi\delta\sqrt{t_{n}}}\int_{[-\Delta\sqrt{t_{n}},\Delta\sqrt{t_{n}}]\setminus[-\delta\sqrt{t_{n}},\delta\sqrt{t_{n}}]}\left|f_{n}^{*}(\zeta)-g_{n}^{*}(\zeta)\right|d\zeta.
\label{ineq:FmoinsG}
\end{align}
In the right-hand side, the first part is of the form $\frac{\eps'(\delta)}{\sqrt{t_{n}}}$ when 
$\lim_{\delta \to 0} \eps'(\delta)=0$,
while the second part is smaller than $\frac{M}{\Delta\sqrt{t_{n}}}$ for some constant $M$.\bigskip

Let us show that the last integral goes to zero faster than any power of $t_{n}$. Indeed, for $|\zeta| \in [\delta\sqrt{t_{n}},\Delta\sqrt{t_{n}}]$,
$$|f_{n}^*(\zeta)|=\left|\varphi_{n}\left(\frac{\I \zeta}{\sqrt{t_{n}\eta''(0)}}\right)\right|\leq
 \left|\psi_n \!\left(\frac{\I \zeta}{\sqrt{t_{n}\eta''(0)}}\right) \right|
\times
 \left| \exp \!\left(t_n\, \eta\! \left(\frac{\I \zeta}{\sqrt{t_{n}\eta''(0)}}\right) \right) \right| 
 $$
The first part is bounded by a constant $K(\Delta)$ because of the uniform convergence of $\psi_n$ towards $\psi$ on the complex segment $[-\I\Delta/\sqrt{\eta''(0)},\I\Delta/\sqrt{\eta''(0)}]$. The second part can be bounded by
\[\left(\max_{\frac{\delta}{\sqrt{\eta''(0)}} \leq |u| \leq \frac{\Delta}{\sqrt{\eta''(0)}}} |\exp(\eta(\I u))|\right)^{\!t_{n}},\]
but the maximum is a constant $q_{\delta,\Delta}$ strictly smaller than 1, because $\eta$ is not lattice distributed. This implies that in the domain 
$[-\Delta\sqrt{t_{n}},\Delta\sqrt{t_{n}}]\setminus[-\delta\sqrt{t_{n}},\delta\sqrt{t_{n}}]$,
one has the bound
\[|f_{n}^*(\zeta)| \le K(\Delta) (q_{\delta,\Delta})^{t_n}.\]
The explicit expression~\eqref{eq:gnstar} shows that the same kind of bound holds for $|g_{n}^*(\zeta)|$. We shall use the notation $\widetilde{K}(\Delta)$ and $\widetilde{q}_{\delta,\Delta}$ for constants valid for both $|f_{n}^*(\zeta)|$ and $|g_{n}^*(\zeta)|$. Thus the third summand in the bound~\eqref{ineq:FmoinsG} is bounded by 
$$\frac{4 \Delta}{\pi \delta}\, \widetilde{K}(\Delta) \,(\widetilde{q}_{\delta,\frac{1}{\delta}})^{t_{n}}.$$
Fix $\eps>0$, then $\delta$ such that $\eps(\delta)<\eps$ and $M\delta<\eps$. Take $\Delta=\frac{1}{\delta}$; we get
$$|F_{n}(x)-G_{n}(x)| \leq \frac{2\eps}{\sqrt{t_{n}}}+\frac{4}{\pi\delta^2}\,\widetilde{K}(\delta^{-1})\,(\widetilde{q}_{\delta,\Delta})^{t_{n}} \leq \frac{3\eps}{\sqrt{t_{n}}}$$
for $t_{n}$ large enough. This completes the proof of the proposition.
\end{proof}
\medskip

\begin{remark}
Proposition \ref{prop:berryesseen} gives an approximation for the Kolmogorov distance between the law $\mu_n$ and the normal law. Indeed, assume to simplify that the reference law $\phi$ is the Gaussian law. Then, $\eta''(0)=1$ and $\eta'''(0)=0$, and one computes
\begin{align*}
d_\text{Kol}(\mu_n,\,\mathcal{N}_{\R}(0,1))&=\frac{1}{\sqrt{t_n}}\,\sup_{x \in \R} \left|\int_{-\infty}^x\psi'(0)\,y\,g(y)\,dy\right|+o\!\left(\frac{1}{\sqrt{t_n}}\right) \\
&= \frac{|\psi'(0)|}{\sqrt{2\pi t_n}}+o\!\left(\frac{1}{\sqrt{t_n}}\right).
\end{align*}
This makes explicit the bound given by Theorem 1 in \cite{Hwa98}.
If $\psi'(0) \ne 0$ ({\em e.g.}, as in Lemma \ref{lem:exponchange}), we get an equivalent of the Kolmogorov distance. However, if $\psi'(0)=0$, then the estimate $d_{\mathrm{Kol}}=o(1/\sqrt{t_n})$ may not be optimal. Indeed, in the case of a scaled sum of i.i.d.~random variables, $t_n=n^{1/3}$ and one obtains the bound 
$$d_{\mathrm{Kol}}\left(\frac{1}{\sqrt{n}}\sum_{i=1}^n Y_i,\,\mathcal{N}_{\R}(0,1)\right)=o\!\left(\frac{1}{n^{1/6}}\right),$$
which is not as good as the classical Berry-Esseen estimate $O(\frac{1}{n^{1/2}})$. There is a way to modify the arguments in order to get such optimal estimates, by controlling  the zone of mod-convergence. We refer to \cite{FMN14}, where such "optimal" computations of Kolmogorov distances is performed.
\end{remark}
\bigskip
