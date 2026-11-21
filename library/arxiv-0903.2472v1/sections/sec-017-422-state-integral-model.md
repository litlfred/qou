---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-017-422-state-integral-model
section_title: "State integral model"
section_number: 4.2.2
pages: 55-61
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.523
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
[]{#sec:figeightsum label="sec:figeightsum"}

The state integral model [\[statesumdef\]](#statesumdef){reference-type="eqref" reference="statesumdef"} for the figure-eight knot complement gives: $$Z^{(\alpha)} (M; \hbar, u) = \frac{1}{\sqrt{2 \pi \hbar}} \int_{C_{\alpha}} dp
\frac{\Phi_{\hbar} (p + i\pi +\hbar)}{\Phi_{\hbar}(-p-2u-i\pi-\hbar) }
e^{-\frac{2}{\hbar}u(u+p) -u}\;.
\label{base_Hik_41}$$ There are two tetrahedra ($N=2$) in the standard triangulation of $M$, and so two quantum dilogarithms in the integral. There is a single integration variable $p$, and we can identify $g_1(p,u) = p$,  $g_2(p,u) = -p-2u$, and $f(p,2u,\hbar) = -4u(u+p)$.

Plots of $|e^{\Upsilon(\hbar,p,u)}|$ and its logarithm at $u=0$ and $\hbar = \frac{i}{3}$. []{#fig:Lambda0 label="fig:Lambda0"}

It will be convenient here to actually change variables $p\mapsto p-u-i\pi-\hbar$, removing the $(i\pi+\hbar)$ terms in the quantum dilogarithms, and obtaining the somewhat more symmetric expression $$\begin{aligned}
Z^{(\alpha)} (M; \hbar, u)
&= \frac{1}{\sqrt{2 \pi \hbar}}
e^{\frac{2\pi iu}{\hbar}+u}\int_{C_{\alpha}} dp \frac{\Phi_{\hbar}(p-u)}{\Phi_{\hbar}(-p-u)} e^{-\frac{2pu}{\hbar}}
\label{Hik41} \\
&= \frac{1}{\sqrt{2 \pi \hbar}}e^{\frac{2\pi iu}{\hbar}+u}\int_{C_{\alpha}} dp\, e^{\Upsilon(\hbar,p,u)}\;.
\end{aligned}$$

We define $e^{\Upsilon(\hbar,p,u)} = \frac{\Phi_{\hbar}(p-u)}{\Phi_{\hbar}(-p-u)}e^{-\frac{2pu}{\hbar}}$ . Figures [\[fig:Lambda0\]](#fig:Lambda0){reference-type="ref" reference="fig:Lambda0"} and [\[fig:Lambda12\]](#fig:Lambda12){reference-type="ref" reference="fig:Lambda12"} show plots of $|e^{\Upsilon(\hbar,p,u)}|$ and $\log|e^{\Upsilon(\hbar,p,u)}| = {\rm Re}\,\,\Upsilon(\hbar,p,u)$ at $\hbar = i/3$ and two values of $u$. The half-lines of poles and zeroes of the two quantum dilogarithms combine into similar singularities for $\Upsilon(\hbar,p,u)$, as is depicted in Figure [\[fig:MinefieldY\]](#fig:MinefieldY){reference-type="ref" reference="fig:MinefieldY"}; note the splitting of these poles and zeroes by an amount $2u$.

Plots of $|e^{\Upsilon(\hbar,p,u)}|$ and its logarithm at $u=\frac{1}{2}i$ and $\hbar = \frac{i}{3}$. []{#fig:Lambda12 label="fig:Lambda12"}

After our change of variables, the "potential" function $V(p,u)$ as in [\[Hik_gen_V\]](#Hik_gen_V){reference-type="eqref" reference="Hik_gen_V"} is now seen to be $$V(p,u) = \frac{1}{2}\left[\text{Li}_2(-e^{p-u})-\text{Li}_2(-e^{-p-u})-4p u + 4\pi i u\right]\,.
\label{Hik41V}$$

Instead of looking directly at $\frac{\partial}{\partial p} V=0$ to find its critical points, we consider the simpler equation $$r(x,m) = e^{2\frac{\partial}{\partial p}V} = \frac{x}{m^2(m+x)(1+mx)} = 1\,,$$ in terms of $x=e^p$ and $m=e^u$. This clearly has two branches of solutions, which both lift to true critical points of $V$, given by $$p^{({\rm geom},{\rm conj})}(u) = \log\left[\frac{1-m^2-m^4\mp m^2\Delta(m)}{2m^3}\right]\,,
\label{HikpGC}$$ with $\Delta(m)$ defined in [\[def_Delta\]](#def_Delta){reference-type="eqref" reference="def_Delta"}. The lift is unique if (say) $\hbar \in i\,{\mathbb{R}}_{>0}$. We claim that these

Poles, zeroes, and critical points of $e^{\Upsilon(\hbar,p,u)}$ for $u=\frac{1}{2}i$ and $\hbar = \frac{3}{4}e^{i\pi/6}$.\
[]{#fig:MinefieldY label="fig:MinefieldY"}

correspond to the geometric and conjugate branches of the A-polynomial, which can be verified by calculating

[^1]

$s(x,m) = \exp\big( \frac{\partial}{\partial u} V(p,u) \big) = \big[\frac{m+x}{x^3+mx^4}\big]^{1/2}$, and checking indeed that $s(x^{({\rm geom}, {\rm conj})}(m),m) = l_{{\rm geom}, {\rm conj}}(m)$.

The two critical points of $\Lambda_{\hbar}$ which correspond to the critical points of $V$ (as $\hbar \to 0$) are indicated in Figures [\[fig:Lambda0\]](#fig:Lambda0){reference-type="ref" reference="fig:Lambda0"} and [\[fig:Lambda12\]](#fig:Lambda12){reference-type="ref" reference="fig:Lambda12"}. As mentioned at the end of Section [\[sec:statesumdef\]](#sec:statesumdef){reference-type="ref" reference="sec:statesumdef"}, at any fixed $\hbar \neq 0$ there exist many other critical points of $\Lambda_{\hbar}$ that can be seen between consecutive pairs of poles and zeroes in Figures [\[fig:Lambda0\]](#fig:Lambda0){reference-type="ref" reference="fig:Lambda0"} and [\[fig:Lambda12\]](#fig:Lambda12){reference-type="ref" reference="fig:Lambda12"}; however, these other critical points become trapped in half-line singularities as $\hbar\rightarrow0$, and their saddle point approximations are not well-defined.

We now calculate the perturbative invariants $S_n^{({\rm geom})}(u)$ and $S_n^{({\rm conj})}(u)$ by doing a full saddle point approximation of the integral [\[Hik41\]](#Hik41){reference-type="eqref" reference="Hik41"} on (dummy) contours passing through the two critical points. We begin by formally expanding $\Upsilon (\hbar,p,u) = \log \Lambda_{\hbar} (p,u)$ as a series in both $\hbar$ and $p$ around some fixed point $p_0$: $$\Upsilon(\hbar, p_0+p,u) = \sum_{j=0}^\infty \sum_{k=-1}^\infty\Upsilon_{j,k}(p_0,u)\,p^j\hbar^k\,.$$ Our potential $V(p,u)$ is identified with $\Upsilon_{0,-1}(p,u)+2\pi iu$, and critical points of $V$ are defined by $\Upsilon_{1,-1}(p,u) = \frac{\partial}{\partial p} V(p,u) = 0$. Let us also define

$$b(p,u) := -2\Upsilon_{2,-1}(p,u) = -\frac{\partial^2}{\partial p^2}V(p,u)\,.$$

Then at a critical point $p_0 = p^{(\alpha)}(u)$, the integral [\[Hik41\]](#Hik41){reference-type="eqref" reference="Hik41"} becomes

[^2] $$Z^{(\alpha)} (M; \hbar, u) = \frac{e^{u+\frac{1}{\hbar}V^{(\alpha)}(u)}}{\sqrt{2 \pi \hbar}}
\int_{C_{\alpha}} dp\, e^{-\frac{b^{(\alpha)}(u)}{2\hbar}p^2} \exp\left[\frac{1}{\hbar}
\sum_{j=3}^\infty \Upsilon_{j,-1}^{(\alpha)}(u)\,p^j
+ \sum_{j=0}^\infty\sum_{k=1}^\infty \Upsilon_{j,k}^{(\alpha)}(u)\,p^j \hbar^k \right],
\label{saddle_integral}$$ where $V^{(\alpha)}(u) = V(p^{(\alpha)}(u),u)$, $b^{(\alpha)}(u) = b(p^{(\alpha)}(u),u)$, and $\Upsilon_{j,k}^{(\alpha)}(u)=\Upsilon_{j,k}(p^{(\alpha)}(u),u)$ are implicitly functions of $u$ alone.

We can expand the exponential in [\[saddle_integral\]](#saddle_integral){reference-type="eqref" reference="saddle_integral"}, integrate each term using $$\int dp\, e^{-\frac{b}{2\hbar}p^2}p^{n} = \left\{
\begin{array}{ll}
 (n-1)!!\left(\frac{\hbar}{b}\right)^{n/2}\sqrt{\frac{2\pi \hbar}{b}} & \;\mbox{$n$ even} \\
 0 & \; \mbox{$n$ odd}
\end{array}
\right.,
\label{gauss_integral}$$ and re-exponentiate the answer to get a final result. The integrals in [\[gauss_integral\]](#gauss_integral){reference-type="eqref" reference="gauss_integral"} are accurate up to corrections of order ${\cal O}(e^{-{\rm const}/\hbar})$, which depend on a specific choice of contour and are ignored. Following this process, we obtain $$\begin{aligned}
Z^{(\alpha)} (M; \hbar, u)
& = \frac{1}{\sqrt{2 \pi \hbar}} \sqrt{\frac{2\pi \hbar}{b^{(\alpha)}}}
e^{u+\frac{1}{\hbar} V^{(\alpha)}(u)}e^{S_2^{(\alpha)}\hbar+S_3^{(\alpha)}\hbar^2+\ldots} \\
& = \exp\left[\frac{1}{\hbar}V^{(\alpha)}(u)
- \frac{1}{2} \log b^{(\alpha)} + u + S_2^{(\alpha)}\hbar + S_3^{(\alpha)}\hbar^2 + \ldots \right]\,,
\label{final_lambda_int}
\end{aligned}$$ where the coefficients $S_n$ can be straightforwardly computed in terms of $b$ and the $\Upsilon$'s. For example, $S_2^{(\alpha)} = \frac{15}{2(b^{(\alpha)})^3}\Upsilon_{3,-1}^{(\alpha)}+\frac{3}{(b^{(\alpha)})^2}\Upsilon_{4,-1}^{(\alpha)}+\Upsilon_{0,1}^{(\alpha)}$ and $S_3^{(\alpha)} = \frac{3465}{8(b^{(\alpha)})^6}(\Upsilon_{3,-1}^{(\alpha)})^4 +$ (sixteen other terms). In addition, we clearly have

$$\begin{aligned}
 S_0^{(\alpha)}(u) &= V^{(\alpha)}(u)\,, \\
 \delta^{(\alpha)} &= 0\,, \\
 S_1^{(\alpha)}(u) &= -\frac{1}{2}\log\frac{b^{(\alpha)}}{m^2}\,. \label{S1calc}
\end{aligned}$$

To actually evaluate the coefficients $\Upsilon_{i,j}(p,u)$, we refer back to the expansion [\[qdl_exp\]](#qdl_exp){reference-type="eqref" reference="qdl_exp"} of the quantum dilogarithm in Section [\[sec:statesumdef\]](#sec:statesumdef){reference-type="ref" reference="sec:statesumdef"}. We find $$\begin{aligned}
\Upsilon_{j,k}(p,u) &=\frac{B_{k+1}(1/2)\,2^k}{(k+1)! j!}
\left[\text{Li}_{1-j-k} (-e^{p-u})-(-1)^j \text{Li}_{1-j-k} (-e^{-p-u})\right]
\label{jklambda}
\end{aligned}$$ when $j\geq 2 \;\mbox{or}\; k \geq 0$, and that all $\Upsilon_{j,2k}$ vanish.

Therefore: to calculate the expansion coefficients $S_n^{(\alpha)} (u)$ around a given critical point, we substitute $p^{(\alpha)}(u)$ from [\[HikpGC\]](#HikpGC){reference-type="eqref" reference="HikpGC"} into equations [\[Hik41V\]](#Hik41V){reference-type="eqref" reference="Hik41V"} and [\[jklambda\]](#jklambda){reference-type="eqref" reference="jklambda"} to obtain $V^{(\alpha)}$, $b^{(\alpha)}$, and $\Upsilon_{j,k}^{(\alpha)}$; then we substitute these functions into expressions for the $S_n$ and simplify. At the geometric critical point $p^{({\rm geom})}(u)$, we obtain $$\begin{aligned}
V^{({\rm geom})}(u) &= \frac{1}{2}\left[\text{Li}_2(-e^{p^{(\rm geom)}(u)-u})-\text{Li}_2(-e^{-p^{(\rm geom)}(u)-u})-4p^{(\rm geom)}(u)\, u + 4\pi i u\right]\,,\\
b^{({\rm geom})}(u) &= \frac{im^2}{2} \Delta(m)\,,
\end{aligned}$$ and it is easy to check with a little algebra that all the expansion coefficients $S_n^{({\rm geom})}(u)$ reproduce exactly

[^3]

what we found in the previous subsection by quantizing the moduli space of flat connections. (This has been verified to eight-loop order.)

Similarly, at the conjugate critical point $p^{({\rm conj})}(u)$, we have $$V^{({\rm conj})} (u) = -V^{({\rm geom})} (u)\,, \qquad
b^{({\rm conj})} (u) = -\frac{im^2}{2}\Delta(m)\,,$$ and more generally $S_n^{(\rm conj)}=(-1)^{n-1}S_n^{(\rm geom)}$. It is not hard to actually prove this relation between the geomtric and conjugate critical points to all orders by inspecting the symmetries of $e^{\Upsilon(\hbar,p,u)}$. Thus, we find complete agreement with the results of Section [\[sec:figeightquant\]](#sec:figeightquant){reference-type="ref" reference="sec:figeightquant"}.

We would like to thank D. Auroux, N. Dunfield, S. Garoufalidis, K. Hikami, T. Mrowka, W. Neumann, E. Witten, and C. Zickert for useful discussions and correspondence. Research of SG is supported in part by NSF Grant PHY-0757647 and in part by the Alfred P. Sloan Foundation. JL acknowledges support from a Marie Curie Intra-European Fellowship. TD acknowledges support from a National Defense Science and Engineering Graduate Fellowship. Opinions and conclusions expressed here are those of the authors and do not necessarily reflect the views of funding agencies.

[^1]: Here $s(x,m)$ is the square root of a rational function rather than a rational function itself due to our redefined variables. Using [\[base_Hik_41\]](#base_Hik_41){reference-type="eqref" reference="base_Hik_41"} directly, we would have gotten a pure rational expression.

[^2]: This expression assumes that $\Upsilon_{j,k}=0$ when $k$ is even, a fact that shall be explained momentarily.

[^3]: There appears to be a small "correction" of $\frac{1}{2}\log(-1) = \log(\pm i)$ in $S_1^{(\rm geom)}$, comparing [\[S1calc\]](#S1calc){reference-type="eqref" reference="S1calc"} with the value in Table [\[tab:figeightgeom\]](#tab:figeightgeom){reference-type="ref" reference="tab:figeightgeom"}. This merely multiplies the partition function by $i$ and can be attributed to the orientation of the stationary-phase contour passing through the geometric critical point. We also allow the usual modulo $2\pi i u$ ambiguity in matching $S_0$.
