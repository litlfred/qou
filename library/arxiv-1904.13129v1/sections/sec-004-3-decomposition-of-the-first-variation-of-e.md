---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-004-3-decomposition-of-the-first-variation-of-e
section_title: "Decomposition of the first variation of E"
section_number: 3
pages: 6-14
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.97
---
[]{#section:decomposition label="section:decomposition"}

Results concerning the differentiability of O'Hara's knot energies go back to the paper [@FHW94] where the Gâteaux differentiability and the $L^2$-gradient of the Möbius energy $\mathcal{E}^{2}$ was derived. Subsequently, a linearized version for the gradient of the Möbius energy was given by He [@H00 Lem. 2.2] in the context of the heat flow. An application of He's linearization trick to a range of O'Hara's knot energies $\mathcal{E}^\alpha$, for $2 \leq \alpha <3$, was given by Reiter [@R12 Chap. 2].

In the following we will use the linearization trick of He and Reiter to decompose the first variation of the energies $\mathcal{E}^\alpha$, for $2 < \alpha < 3$, into a highest order quasilinear part $Q^\alpha$ and two remaining $R_1^\alpha$, $R_2^\alpha$ parts of lower order (as it was done in [@BR13] and [@B18 Theor. 2.3]). A similar decomposition of the first variation proved apt for the analyticity proof of critical points of the Möbius energy that was given in [@BV19].

Let $\gamma \in C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ be a simple closed arc-length parametrized curve and $x\in\mathbb{R}/ \mathbb{Z}$. We recall that the orthogonal projection $P^\perp_{\dot{\gamma}(x)} : \mathbb{R}^n \rightarrow \mathbb{R}^n$ at the point $\gamma(x)$ onto the normal space of the curve $\gamma$ is given by $$\begin{aligned}
  (P^\perp_{\dot{\gamma}}v)(x) = P^\perp_{ \dot{\gamma}(x)}(v) = v-\langle v,\dot{\gamma}(x) \rangle_{\mathbb{R}^n} \dot{\gamma}(x)
\end{aligned}$$ for any $v\in \mathbb{R}^n$. Furthermore, the tangential projection $P^T_{\dot{\gamma}} : \mathbb{R}^n \rightarrow \mathbb{R}^n$ at the point $\gamma(x)$ onto the tangent space of the curve $\gamma$ is given by $$\begin{aligned}
(P^T_{\dot{\gamma}}v)(x) = P^T_{\dot{\gamma}(x)} (v) = \langle v, \dot{\gamma}(x) \rangle_{\mathbb{R}^n} \dot{\gamma}(x)
\end{aligned}$$ for any $v\in \mathbb{R}^n$. We remark also that the curvature vector of the curve $\gamma$ is denoted by $\kappa$ i.e. $\kappa = (\frac{d}{ds})^2 \gamma$ where $\frac{d}{ds}$ is the derivative with respect to the arc-length. We recall the following:

::: thm
[]{#thm:1stvar label="thm:1stvar"} The first variation of $\mathcal{E}^{\alpha}$, for $2 < \alpha < 3$, at a simple regular curve $\gamma \in C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ in direction $h \in H^2 (\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ can be expressed as $$\begin{aligned}
    \delta \mathcal{E}^\alpha(\gamma, h) = \int_{0}^{1} \langle (H^\alpha\gamma)(x), h(x) \rangle_{\mathbb{R}^n} |\dot{\gamma}(x)|  \mathrm{d} x,
    
\end{aligned}$$ where $$\begin{aligned}
    &(H^\alpha \gamma)(x) := \lim_{\epsilon \downarrow 0} \int_{|w| \in [\epsilon, \frac{1}{2}]} P^\perp_{\dot{\gamma}(x)} \{ 2\alpha \frac{\gamma(x+w)-\gamma(x)}{|\gamma(x+w)-\gamma(x)|^{2+\alpha}} \\
    &\hspace{5em}  -(\alpha -2) \frac{\kappa(x)}{\mathcal{D}(\gamma(x+w),\gamma(x))^{\alpha}} -2 \frac{\kappa(x)}{|\gamma(x+w)-\gamma(x)|^{\alpha}} \} |\dot{\gamma}(x+w)| \mathrm{d} w.
    
\end{aligned}$$
:::

Due to the the fact that $P^\perp_{\dot{\gamma}(x)}(\dot{\gamma}(x)) = 0$, $\langle \dot{\gamma}(x),\ddot{\gamma}(x) \rangle_{\mathbb{R}^n} = 0$, the curve $\gamma$ is parametrized by arc-length and the orthogonal projection $P^\perp_{\dot{\gamma}(x)}$ is linear, one can easily rewrite $H^{\alpha} \gamma$ as $$\begin{aligned}
\label{formula:H}
(H^\alpha\gamma) (x) = (P^\perp_{\dot{\gamma}}\widetilde{H}^\alpha \gamma) (x) = P^\perp_{\dot{\gamma}(x)} ((\widetilde{H}^\alpha \gamma) (x)) ,
\end{aligned}$$ where $$\begin{aligned}
(\widetilde{H}^{\alpha} \gamma) (x) := \lim_{\varepsilon \downarrow 0} & \int_{|w| \in [\varepsilon,\frac{1}{2}]} \{ 2\alpha \frac{\gamma(x+w)-\gamma(x)-w\dot{\gamma}(x)}{|\gamma(x+w)-\gamma(x)|^{2+\alpha}} \\
& -(\alpha -2) \frac{\ddot{\gamma}(x)}{ \mathcal{D}(\gamma(x+w),\gamma(x))^{\alpha}}  -2 \frac{\ddot{\gamma}(x)}{ |\gamma(x+w)-\gamma(x)|^{\alpha}} \}  \mathrm{d} w .
\end{aligned}$$

Now we want to apply the strategy of He and Reiter indicated as in the above. We decompose $\widetilde{H}^\alpha \gamma$ pointwise for all $x\in \mathbb{R}/ \mathbb{Z}$ into three functionals by $$\begin{aligned}
\label{formula:Htilde}
\widetilde{H}^\alpha\gamma = \alpha Q^\alpha\gamma + 2\alpha R_1^\alpha \gamma - 2 R_2^\alpha \gamma  ,
\end{aligned}$$ where $$\begin{aligned}
    Q^\alpha\gamma (x) 
    &= \lim_{\varepsilon \downarrow 0}Q^{\alpha,\varepsilon}\gamma(x) \\    
    R_1^\alpha \gamma (x) &= \lim_{\varepsilon \downarrow 0}R_1^{\alpha,\varepsilon}\gamma(x) \\
    R_2^\alpha \gamma (x) &= \lim_{\varepsilon \downarrow 0}R_2^{\alpha,\varepsilon}\gamma(x) 
\end{aligned}$$ are given, for any $0<\varepsilon\leq \frac 12$, by $$\begin{aligned}
(Q^{\alpha,\varepsilon}\gamma)(x) &= \int_{|w| \in [\varepsilon, \frac{1}{2}]} \left(2 \frac{\gamma(x+w)-\gamma(x)-w\dot{\gamma}(x)}{w^2} - \ddot{\gamma}(x) \right) \frac{\mathrm{d} w}{|w|^\alpha}, \\
(R_1^{\alpha,\varepsilon} \gamma)(x) &= \int_{|w| \in [\varepsilon, \frac{1}{2}]} (\gamma(x+w)-\gamma(x)-w\dot{\gamma}(x)) \left(\frac{1}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} - \frac{1}{ |w|^{\alpha +2}}\right)\mathrm{d} w, \\
(R_2^{\alpha,\varepsilon} \gamma)(x) &= \int_{|w| \in [\varepsilon, \frac{1}{2}]} \ddot{\gamma}(x)\left(\frac{1}{|\gamma(x+w)-\gamma(x)|^{\alpha}} - \frac{1}{ |w|^{\alpha }}\right)\mathrm{d} w
\end{aligned}$$ Blatt and Reiter [@BR13] have already used this partitioning for studying the regularity of stationary points of O'Hara's energies $\mathcal{E}^{\alpha}$, $2<\alpha <3$, and furthermore, Blatt (cf. [@B18 Theor. 2.3]) used it in the study of the gradient flow for the same range of O'Hara's knot energies.

In the next section we will see that $Q^\alpha$ contains the highest order part of the first variation of $\mathcal{E}^\alpha$. Thereafter the challenge will be to attain sufficient estimates of the tangential part of $Q^\alpha$, whereas $R_1^\alpha$ and $R_2^\alpha$ are of lower order and easier to get under control.

An estimate for the $Q^\alpha$ term[]{#sec:maintermQ label="sec:maintermQ"}

Let the quantities $$\begin{aligned}
q_k^{(\alpha)} := \begin{cases}
\frac{4\pi}{|k|^{\alpha +1}} \int_0^\pi \frac{(k\tau)^2 - 2 + 2\cos(k\tau)}{\tau^{2+\alpha}} \mathrm{d}\tau & \quad k\neq 0, \\
0 & \quad k = 0
\end{cases}
\end{aligned}$$ and set $$\begin{aligned}
    \lambda_k^{(\alpha)} := \int_0^{k\pi} \frac{\sin (\tau)}{\tau^{\alpha - 1}} \mathrm{d} \tau.
\end{aligned}$$ We remark that the $\lambda_k$ are well-defined for all $k\in\mathbb{Z}$ and $\lambda_\infty^{(\alpha)}  := \lim_{k\rightarrow \infty} \lambda_k^{(\alpha)} < \infty$ (cf. [@R12 Lem. 2.4]). We deduce from [@R12 Prop. 2.3], by switching from the weak formulation of the Euler-Lagrange equation to the strong one, the following:

::: thm
[]{#thm:QFourier label="thm:QFourier"} For every curve $\gamma \in C^\infty(\mathbb{R}/ \mathbb{Z}, \mathbb{R}^n)$ the term $Q^\alpha \gamma$ is a $C^\infty$-function and its Fourier coefficients, for all $k\in \mathbb{Z}$, are given by $$\begin{aligned}
\label{eq:fouriercoeffQ}
    \widehat{Q^{\alpha} \gamma}(k) = -q_k^{(\alpha)} |k|^{\alpha +1} \hat{\gamma} (k) 
    .
\end{aligned}$$ The constants $q_k^{(\alpha)}$ are bounded and satisfy $$0 \leq q_k^{(\alpha)} = \frac{8\pi \lambda_k^{(\alpha)}}{\alpha (\alpha + 1 )(\alpha -1)} + O(\tfrac{1}{k^{1-\alpha}})$$ as $k \rightarrow \infty$.
:::

::: proof
*Proof.* By Taylor's expansion up to third order we obtain $$\begin{aligned}
Q^\alpha \gamma (x) & = \lim_{\varepsilon\downarrow 0} 2  \int_{|w| \in [\varepsilon, \frac{1}{2}]} \frac{w }{|w|^\alpha}   \int_0^1 (1-t)^2 \dddot{\gamma}(x+tw) \mathrm{d}t \mathrm{d} w \nonumber \\
& = \lim_{\varepsilon\downarrow 0} 2  \int_{|w| \in [\varepsilon, \frac{1}{2}]} \frac{w }{|w|^\alpha}   \int_0^1 (1-t)^2 \left(\dddot{\gamma}(x+tw) - \dddot{\gamma}(x)\right) \mathrm{d}t  \mathrm{d} w , \label{eq:Qcont}
\end{aligned}$$ from which directly follows that $Q^\alpha$ maps $C^{3,\beta}$ to $L^\infty$ for any $0 < \beta \leq 1$. From the linearity of $Q^\alpha$ we get $\partial^l Q^\alpha \gamma (x) = Q^\alpha\partial^l \gamma(x)$, so $Q^\alpha$ maps $C^{l+3,\beta}$ to $C^{l-1,1}$ for all integers $l\geq 1$, which demonstrates the first part of the Theorem's statement.

Now we define the bilinear functional $$\begin{aligned}
\widetilde Q^\alpha (\gamma,\eta) := \lim_{\varepsilon  \downarrow 0 } \int_{\mathbb R / \mathbb Z} \int_{|w| \in [\varepsilon, \frac 1 2]} \Big( \frac {\langle \gamma(x+w)-\gamma(x),\eta(x+w)-\eta(x)\rangle_{\mathbb{R}^n} }{w^2}- \langle \dot \gamma (x) , \dot \eta (x) \rangle_{\mathbb{R}^n} \Big) \frac{\mathrm{d}w \mathrm{d}x}{|w|^\alpha} .
\end{aligned}$$ for any $\gamma,\eta \in H^{\frac{\alpha+1}{2}}(\mathbb R / \mathbb Z, \mathbb R ^n)$. Applying continuous and discrete integration by parts, gives $$\begin{aligned}
\widetilde Q^\alpha (\gamma,\eta) & = \lim_{\varepsilon  \downarrow 0 } \int_{\mathbb R / \mathbb Z} \int_{|w| \in [\varepsilon, \frac 1 2]} \left( -2 \frac {\langle \gamma(x+w)-\gamma(x),\eta(x)\rangle_{\mathbb{R}^n} }{w^2} - \langle \dot \gamma(x) , \dot \eta(x) \rangle_{\mathbb{R}^n} \right) \frac{\mathrm{d}w \mathrm{d}x}{|w|^\alpha}  \nonumber \\
& = -\lim_{\varepsilon \downarrow 0} \int_{\mathbb R / \mathbb Z} \langle Q^{\alpha,\varepsilon} \gamma(x), \eta(x) \rangle_{\mathbb{R}^n} \mathrm{d}x 
= - \int_{\mathbb R / \mathbb Z} \langle Q^\alpha \gamma(x) ,\eta(x) \rangle_{\mathbb{R}^n} \mathrm{d}x   \label{formula:Qtildecalc}
\end{aligned}$$ because $Q^{\alpha,\varepsilon} \gamma$ converges to $Q^\alpha \gamma$ in $L^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ as $\epsilon\downarrow 0$ by [\[eq:Qcont\]](#eq:Qcont){reference-type="eqref" reference="eq:Qcont"}. Furthermore, by [@R12 Prop. 2.3], we have that $$\begin{aligned}
 \widetilde Q^\alpha(\gamma,\eta) = \sum_{k \in \mathbb Z} q_k^{(\alpha)} |k|^{\alpha+1} \hat{\gamma} (k) \hat {\eta}(k)
\end{aligned}$$ and by Plancherel's identity we get $$\begin{aligned}
  \int_{\mathbb R / \mathbb Z} \langle Q^\alpha\gamma ,\eta \rangle dx  = \sum_{k \in \mathbb Z} \widehat{Q^\alpha \gamma}(k) \widehat{\eta}(k).
\end{aligned}$$ So by comparing the Fourier coefficients in [\[formula:Qtildecalc\]](#formula:Qtildecalc){reference-type="eqref" reference="formula:Qtildecalc"} we have $\widehat{Q^\alpha f}(k) = -q_k^{(\alpha)}|k|^{\alpha +1} \hat{\gamma} (k)$ for all $k\in \mathbb{Z}.$ The properties of the coefficients $q_k^{(\alpha)}$ directly follow from the proof of [@R12 Prop. 2.3]. ◻
:::

By Theorem [\[thm:QFourier\]](#thm:QFourier){reference-type="ref" reference="thm:QFourier"} we obtain the following essential corollary.

::: cor
[]{#kor:Ql label="kor:Ql"} There exists a positive constant $\widetilde{C}$ such that for all curves $\gamma \in C^\infty(\mathbb{R}/ \mathbb{Z}, \mathbb{R}^n)$ and integers $l\geq 0$ $$\begin{aligned}
    \|\partial^{l+3}\gamma \|_{H^{m+\alpha-2}} \leq \widetilde{C} \|\partial^{l} Q^{\alpha}\gamma\|_{H^m}
    
\end{aligned}$$ holds for any real numbers $m\geq 0$ and $2 < \alpha < 3$.
:::

::: proof
*Proof.* By considering Theorem [\[thm:QFourier\]](#thm:QFourier){reference-type="ref" reference="thm:QFourier"}, in particular the form of the Fourier coefficients [\[eq:fouriercoeffQ\]](#eq:fouriercoeffQ){reference-type="eqref" reference="eq:fouriercoeffQ"}, the definition of the fractional Sobolev-norm, elementary properties of Fourier coefficients and the simple estimate $(1+k^2)^{\alpha -2} \leq (2|k|)^{2(\alpha -2)}$ for any $k\in \mathbb{Z}\setminus 0$, we get $$\begin{aligned}
    \|\partial^{l}Q^\alpha\gamma \|_{H^m}^2 &= \sum_{k\in \mathbb{Z}} (1+|k|^2)^m|\widehat{\partial^{l}Q^\alpha \gamma}(k)|^2 \\
    &= \sum_{k\in \mathbb{Z}} (1+|k|^2)^m (2\pi| k|)^{2l} |\widehat{Q^\alpha \gamma}(k)|^2 \\
    &= \sum_{k\in \mathbb{Z}} (1+|k|^2)^m (2\pi| k|)^{2l} (q_k^{(\alpha)})^2 |k|^{2(\alpha +1)} |\hat{\gamma} (k)|^2\\
    &\geq \inf_{k\in\mathbb{Z}\setminus 0} \{(q_k^{(\alpha)})^2 (2\pi)^{-6} 2^{2-\alpha} \} \sum_{k \in \mathbb{Z}} (1+|k|^2)^{m+\alpha-2} (2\pi| k|)^{2(l+3)}   |\hat{\gamma} (k)|^2 \\
    &= \widetilde{C}^{-2} \sum_{k \in \mathbb{Z}} (1+|k|^2)^{m+\alpha-2} |\widehat{\partial^{(l+3)}\gamma} (k)|^2 \\
    &= \widetilde{C}^{-2}   \|\partial^{(l+3)}\gamma \|_{H^{m+\alpha-2}}^2,
    
\end{aligned}$$ where $\widetilde{C}:= \inf_{k\in\mathbb{Z}\setminus{0}} \{(q_k^{(\alpha)})^2 (2\pi)^{-6} 2^{2-\alpha}\}^{-\frac{1}{2}}$ is a positive constant. ◻
:::

A fractional leibniz rule and the form of $P^T_{\dot{\gamma}} Q^\alpha\gamma$ []{#sec:bilinearHilberttransform label="sec:bilinearHilberttransform"}

Let $\gamma \in C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ be a closed simple curve parametrized by arc-length. Recall that in the decomposed first variation of O'Hara's range of energies $\mathcal{E}^\alpha$, for $2 < \alpha < 3$, there appears the orthogonal projection of the main part $Q^\alpha \gamma$, which is given by $P^\perp_{\dot{\gamma}} Q^\alpha\gamma =  Q^\alpha\gamma - P^T_{\dot{\gamma}} Q^\alpha\gamma$. Since we have worked out an estimate for $Q^\alpha \gamma$ in the previous section, it remains to study $P^T_{\dot{\gamma}} Q^\alpha\gamma$, i.e. the tangential part of $Q^\alpha\gamma$.

In this section we will see that a type of fractional derivative of a product of two functions can help to estimate the tangential part of $Q^\alpha\gamma$. We interpret the resulting estimate as a *fractional Leibniz rule*.

In order to avoid problems coming from the singularities of the integrand, we will work with the truncated functional $Q^{\alpha,\varepsilon}$ for $0 < \varepsilon \leq \frac 12$. By using Taylor's approximation up to second order with remainder term in integral from and $\left< \dot{\gamma}(x), \ddot{\gamma}(x) \right> = 0$ for all $x\in \mathbb{R}/ \mathbb{Z}$ together with the bilinearity of the scalar product and $\alpha > 2$, we can write $$\begin{aligned}
\label{formula:PTQepsilon}
& \langle Q^{\alpha,\varepsilon}\gamma(x), \dot{\gamma}(x) \rangle_{\mathbb{R}^n} \nonumber\\
& = \int_{|w|\in [\varepsilon, \frac{1}{2}]} \left< 2 \frac{\gamma(x+w)-\gamma(x)-w\dot{\gamma}(x)}{w^2} - \ddot{\gamma}(x) , \dot{\gamma}(x) \right>_{\mathbb{R}^n}  \frac{\mathrm{d}w}{|w|^\alpha} \nonumber\\
& = 2  \int_{|w|\in [\varepsilon, \frac{1}{2}]} \int_0^1 (1-t) \left< \ddot{\gamma}(x+tw) , \dot{\gamma}(x) \right>_{\mathbb{R}^n}  \mathrm{d}t \frac{\mathrm{d}w}{|w|^{\alpha}} \nonumber\\
& = 2  \int_{|w|\in [\varepsilon, \frac{1}{2}]} \int_0^1 (1-t)  \left<\ddot{\gamma}(x+tw), \frac{\dot{\gamma}(x) - \dot{\gamma}(x+tw)}{w}\right>_{\mathbb{R}^n}  \mathrm{d}t \frac{\mathrm{d}w}{w|w|^{\alpha-2}}  \nonumber\\
& = 2 \int_{|w|\in [\varepsilon, \frac{1}{2}]} \int_0^1  \int_0^1 (1-t) (-t) \frac{\left<\ddot{\gamma}(x+tw), \ddot{\gamma}(x+stw)\right>_{\mathbb{R}^n}}{w}  \mathrm{d}s \mathrm{d}t \frac{\mathrm{d}w}{|w|^{\alpha-2}}.
\end{aligned}$$ With $\varepsilon\downarrow 0$ we also get $$\begin{aligned}
&(P^T_{\dot{\gamma}} Q\gamma)(x) \nonumber\\
& = 4 \lim_{\varepsilon \downarrow 0} \int_{|w|\in [\varepsilon, \frac{1}{2}]} \iint_{[0,1 ]^2} (1-t) (-t) \frac{\left<\ddot{\gamma}(x+tw), \ddot{\gamma}(x+stw)\right>_{\mathbb{R}^n}}{w|w|^{\alpha-2}} \dot{\gamma}(x) \mathrm{d}s \mathrm{d}t \mathrm{d}w. \label{formula:compTQ}
\end{aligned}$$ The last terms of [\[formula:PTQepsilon\]](#formula:PTQepsilon){reference-type="eqref" reference="formula:PTQepsilon"} and [\[formula:compTQ\]](#formula:compTQ){reference-type="eqref" reference="formula:compTQ"} motivate us to introduce the following:

::: defn
Let $s_1,s_2 \in [0,1]$, $0 < \varepsilon \leq \frac{1}{2}$ and $\beta \in (0,1)$. Then the bilinear singular integral $H_{s_1,s_2,\beta}: C^1 (\mathbb{R}/ \mathbb{Z},\mathbb{R}) \times C^1 (\mathbb{R}/ \mathbb{Z},\mathbb{R}) \rightarrow L^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R})$ is given by $$\begin{aligned}
\label{defn:Hs1s2}
    H_{s_1,s_2,\beta}(f,g) (x) := \lim_{\varepsilon \downarrow 0} \int_{|w| \in [\varepsilon, \frac 12]} \frac{f(x+s_1w)  g(x+s_2w)}{w |w|^\beta} \mathrm{d}w 
    
\end{aligned}$$ for all $x\in \mathbb{R}/ \mathbb{Z}$ and, its truncated version $H_{s_1,s_2,\beta}^\varepsilon: C^1 (\mathbb{R}/ \mathbb{Z},\mathbb{R}) \times C^1 (\mathbb{R}/ \mathbb{Z},\mathbb{R}) \rightarrow L^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R})$ is given by $$\begin{aligned}
\label{defn:Hs1s2eps}
        & H_{s_1,s_2,\beta}^\varepsilon(f,g) (x) := \int_{|w| \in [\varepsilon, \frac 12]} \frac{f(x+s_1w)  g(x+s_2w)}{w |w|^\beta} \mathrm{d}w
    
\end{aligned}$$ for all $x\in\mathbb{R}/ \mathbb{Z}$.
:::

If $\beta$ was allowed to vanish, the previous definition would yield the bilinear Hilbert transform. Since we have the factor $|w|^\beta$ for $\beta \in (0,1)$ in the denominator in the definition of the bilinear singular integral [\[defn:Hs1s2\]](#defn:Hs1s2){reference-type="eqref" reference="defn:Hs1s2"}, the formula is reminiscent of a fractional derivative.

::: lem
[]{#lem:Hs1s2cont label="lem:Hs1s2cont"} For every $s_1,s_2 \in [0,1]$, $0 < \varepsilon \leq \frac 12$ and $\beta \in (0,1)$ the transforms $H_{s_1,s_2,\beta}$ and $H_{s_1,s_2,\beta}^\varepsilon$ are well-defined, continuous and bilinear from $C^1 (\mathbb{R}/ \mathbb{Z},\mathbb{R})\times C^1 (\mathbb{R}/ \mathbb{Z},\mathbb{R})$ to $L^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R})$. Furthermore, the truncated bilinear integral $H_{s_1,s_2,\beta}^\varepsilon$ is also continuous from $C (\mathbb{R}/ \mathbb{Z},\mathbb{R})\times C (\mathbb{R}/ \mathbb{Z},\mathbb{R})$ to $L^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R})$.
:::

::: proof
*Proof.* It is easy to see by the linearity of the integral in [\[defn:Hs1s2\]](#defn:Hs1s2){reference-type="eqref" reference="defn:Hs1s2"} that $H_{s_1,s_2,\beta}$ is indeed linear in both components. The function $H_{s_1,s_2,\beta}$ is also well-defined for every $f,g \in C^1 (\mathbb{R}/ \mathbb{Z},\mathbb{R})$, which we can see by adding a zero to the definition of the bilinear singular integral [\[defn:Hs1s2\]](#defn:Hs1s2){reference-type="eqref" reference="defn:Hs1s2"} as $$\begin{aligned}
    H_{s_1,s_2,\beta}(f,g)(x)= \lim_{\varepsilon \downarrow 0} \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{f(x+s_1w)  g(x+s_2w)}{w|w|^\beta} - \frac{f(x)  g(x)}{w|w|^\beta}  \mathrm{d}w,
    
\end{aligned}$$ by inserting a second zero and by the Lipschitz-continuity of continuously differentiable functions on a compact set such that $$\begin{aligned}
\label{lem:Hs1s2}
    & \left|H_{s_1,s_2,\beta}(f,g)(x)\right| \nonumber\\
    & \leq \lim_{\varepsilon \downarrow 0} \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{|f(x+s_1w)  g(x+s_2w) - f(x)g(x+s_2w) +f(x)g(x+s_2w) -f(x)  g(x)|}{|w|^{1+\beta}}  \mathrm{d}w \nonumber\\
    & \leq \lim_{\varepsilon \downarrow 0} \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{|f(x+s_1w) - f(x)| | g(x+s_2w)| +  |f(x)| |g(x+s_2w)- g(x)|}{|w|^{1+\beta}}  \mathrm{d}w \nonumber\\
    & \leq \lim_{\varepsilon \downarrow 0} \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{\|f'\|_\infty s_1|w| \|g\|_\infty +  \|f\|_\infty \|g'\|_\infty s_2 |w|}{|w|^{1+\beta}}  \mathrm{d}w \nonumber\\
    & \leq C (s_1,s_2,\beta)  \|f\|_{C^1} \|g\|_{C^1}  < \infty
    
\end{aligned}$$ for some positive finite constant $C(s_1,s_2,\beta)$. Hence we can deduce from [\[lem:Hs1s2\]](#lem:Hs1s2){reference-type="eqref" reference="lem:Hs1s2"} that $H_{s_1,s_2,\beta}$ is continuous. We get the same properties for $H_{s_1,s_2,\beta}^\varepsilon$ for any $0<\varepsilon\leq \frac 12$ by transfering the previous arguments. Additionally, since we cut off the singularity in the definition of $H_{s_1,s_2,\beta}^\varepsilon$, the continuity of $H_{s_1,s_2,\beta}^\varepsilon$ from $C (\mathbb{R}/ \mathbb{Z},\mathbb{R})\times C (\mathbb{R}/ \mathbb{Z},\mathbb{R})$ to $L^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R})$ follows by the following elementary estimates $$\begin{aligned}
     \left|H_{s_1,s_2,\beta}^\varepsilon(f,g)(x)\right| & = \left| \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{f(x+s_1w)  g(x+s_2w)}{w|w|^\beta} - \frac{f(x)  g(x)}{w|w|^\beta}  \mathrm{d}w \right| \\
    & \leq \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{|f(x+s_1w)| | g(x+s_2w)| +  |f(x)| |g(x)|}{|w|^{1+\beta }}  \mathrm{d}w \\
    & \leq  \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{\|f\|_\infty \|g\|_\infty +  \|f\|_\infty \|g\|_\infty }{|w|^{1+\beta}}  \mathrm{d}w \\
    & \leq C (\beta, \varepsilon)  \|f\|_{L^\infty} \|g\|_{L^\infty}  < \infty
    
\end{aligned}$$ for all $x\in [0,1]$ and some constant $0 < C(\beta, \varepsilon) < \infty$. ◻
:::

We next estimate the truncated bilinear integral [\[defn:Hs1s2eps\]](#defn:Hs1s2eps){reference-type="eqref" reference="defn:Hs1s2eps"} that leads to a new kind of fractional Leibniz rule.

::: thm
[]{#thm:BilinearHT label="thm:BilinearHT"} Let $m> \frac{1}{2}$, $0 < \varepsilon \leq \frac{1}{2}$, $s_1,s_2 \in [0,1]$ and $\beta \in (0,1)$. Then there exists a positive constant $C_H = C_H(m, \beta) < \infty$ independent of $\varepsilon$ such that $$\begin{aligned}
\label{formula:BilinearHT}
    \|H_{s_1,s_2,\beta}^\varepsilon(f,g)\|_{H^m} \leq C_H \|f\|_{H^{m+ \beta}} \|g\|_{H^{m+ \beta }}
    
\end{aligned}$$ for all $f,g \in  C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$.
:::

For the proof we will identify, for any $p \in [1,\infty)$, the sequence space $\ell^p$ by $$\begin{aligned}
\ell^p := \{x = (x_k)_{k\in\mathbb{Z}} \in \mathbb{C}^\mathbb{Z}\ | \ \|x\|_{\ell^p}:= (\textstyle \sum_{k\in\mathbb{Z}} |x_k|^p)^{\frac{1}{p}} < \infty \}
\end{aligned}$$ and use the following lemmata.

::: lem
[]{#lem:Young label="lem:Young"} Let $p,q,r \geq 1$ such that $\frac{1}{p} + \frac{1}{q}=\frac{1}{r}+1$. For sequences $x\in \ell^p$ and $y\in  \ell^q$ the convolution $(x*y)(k):= \sum_{n\in \mathbb{Z}} x(n) y(k-n)$ is such that $x*y \in \ell^r$ and $$\begin{aligned}
    \|x*y\|_{\ell^r} \leq \|x\|_{\ell^p} \|y\|_{\ell^q} .
    
\end{aligned}$$
:::

::: lem
[]{#lem:Sobolev label="lem:Sobolev"} Let $f\in H^m(\mathbb{R}/ \mathbb{Z}, \mathbb{R}^n)$ for $m> \frac{1}{2}$. Then $\hat{f}:= (\hat{f}(k))_{k\in\mathbb{Z}} \in \ell^1$ and there exists a positive constant $C_0 < \infty$ such that $$\begin{aligned}
    \|\hat{f}\|_{\ell^1} \leq C_0 \|f\|_{H^m}.
    
\end{aligned}$$
:::

::: proof
*Proof of Theorem [\[thm:BilinearHT\]](#thm:BilinearHT){reference-type="ref" reference="thm:BilinearHT"}.* Let $f,g \in  C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R})\subseteq H^m(\mathbb{R}/ \mathbb{Z},\mathbb{R})$. Because of $m > \frac{1}{2}$ and [@DNPV12 Theor. 8.2], the partial sums of the Fourier series, i.e. $p_n (x) := \sum_{k=-n}^{n} \hat{f}(k) e^{-2\pi i k x}$ and $q_n (x):=\sum_{k=-n}^{n} \hat{g}(k) e^{-2\pi i k x}$ for any $n\in\mathbb{N}_0$ and $x\in \mathbb{R}/ \mathbb{Z}$, converge uniformly to the functions $f$ and $g$, that means $$\begin{aligned}
\label{formula:apprfg}
    \begin{split}
    \|f-p_n \|_\infty  \rightarrow 0 \textnormal{ and } \|g-q_n \|_\infty \rightarrow 0 \textnormal{ as } n\rightarrow \infty.
    \end{split}     
    
\end{aligned}$$ Note that since $f,g \in  C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R})$, also $p_n, q_n \in C^\infty (\mathbb{R}/ \mathbb{Z}, \mathbb{R})$ holds.

Our approach is to firstly prove the estimate [\[formula:BilinearHT\]](#formula:BilinearHT){reference-type="eqref" reference="formula:BilinearHT"} for the approximating functions $p_n$ and $q_n$ and secondly derive the actual statement of Theorem [\[thm:BilinearHT\]](#thm:BilinearHT){reference-type="ref" reference="thm:BilinearHT"} by passing to the limit $n\rightarrow \infty$. We start by interchanging the integrals two times due to $\varepsilon > 0$ and taking account of the fact that the Fourier coefficients of a product of two functions are the convolution of their Fourier coefficients, to gain $$\begin{aligned}
\label{formula:pnqnepsilonI}
    & \widehat{H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)}(k) \nonumber\\
     & = \int_0^1 \int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{p_n(x+s_1w)  q_n(x+s_2w)}{w|w|^\beta} e^{-2\pi i k x} \mathrm{d}w \mathrm{d}x  \nonumber\\
    & = \int_{|w|\in [\varepsilon, \frac{1}{2}]} \int_0^1  p_n(x+s_1w)  q_n(x+s_2w) e^{-2\pi i k x}  \mathrm{d}x \frac{\mathrm{d}w }{w|w|^\beta} \nonumber \\
    & = \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \sum_{l\in\mathbb{Z}} \widehat{p_n}(l) e^{2\pi ils_1 w} \widehat{q_n}(k-l) e^{2\pi i(k-l)s_2 w} \frac{\mathrm{d}w }{w|w|^\beta} \nonumber \\ 
    & = 
    \begin{cases}
    0       & \quad \text{if } |k| > 2n \\
    \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \sum_{l=-n}^{n} e^{2\pi i(ls_1+ (k-l)s_2) w} \widehat{f}(l) \widehat{g}(k-l) \frac{\mathrm{d}w }{w|w|^\beta}  & \quad \text{if } |k| \leq 2n
    \end{cases} 
    .
\end{aligned}$$ Now we focus on the non-trivial Fourier coeffients of $H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)$, that means on the indices $|k|\leq 2n$. By defining $\phi_{l,k} := 2\pi (ls_1 +(k-l)s_2) \in \mathbb{R}$, substitution and interchanging integral and sum, we get $$\begin{aligned}
\label{formula:pnqnepsilonII}
    & \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \sum_{l=-n}^{n} e^{iw\phi_{l,k} } \widehat{f}(l) \widehat{g}(k-l) \frac{\mathrm{d}w }{w|w|^\beta} \nonumber\\ 
    &\qquad \qquad= \int_\varepsilon^{\frac{1}{2}}  \sum_{l=-n}^{n} \frac{e^{i w\phi_{l,k}} - e^{-i w \phi_{l,k}}}{w|w|^\beta} \widehat{f}(l) \widehat{g}(k-l) \mathrm{d}w \nonumber\\
    &\qquad\qquad = \int_\varepsilon^{\frac{1}{2}}  \sum_{l=-n}^{n}\frac{2i \sin (w \phi_{l,k})}{w^{1+\beta}} \widehat{f}(l) \widehat{g}(k-l) \mathrm{d}w \nonumber\\
    &\qquad\qquad =  \sum_{l=-n}^{n} \widehat{f}(l) \widehat{g}(k-l) 2i \int_\varepsilon^{\frac{1}{2}} \frac{ \sin (w \phi_{l,k})}{w^{1+\beta}}  \mathrm{d}w \nonumber\\
    &\qquad\qquad = \sum_{l=-n}^{n} \widehat{f}(l) \widehat{g}(k-l) 2i \phi_{l,k}^\beta \int_{\phi_{l,k}\varepsilon}^{\frac{\phi_{l,k}}{2}} \frac{ \sin (\widetilde{w})}{\widetilde{w}^{1+\beta}}  \mathrm{d}\widetilde{w} \nonumber\\
    &\qquad\qquad = \sum_{l=-n}^{n} \widehat{f}(l) \widehat{g}(k-l) 2i \phi_{l,k}^\beta (\textnormal{Si}_\beta\left(\tfrac{\phi_{l,k}}{2}\right) - \textnormal{Si}_\beta(\phi_{l,k}\varepsilon)),
    
\end{aligned}$$ where $\textnormal{Si}_\beta (x) := \int_0^x \frac{\sin (t)}{t^{1+\beta}}dt$. Hence we can deduce from the previous computations in [\[formula:pnqnepsilonI\]](#formula:pnqnepsilonI){reference-type="eqref" reference="formula:pnqnepsilonI"} and [\[formula:pnqnepsilonII\]](#formula:pnqnepsilonII){reference-type="eqref" reference="formula:pnqnepsilonII"} $$\begin{aligned}
\label{formula:Hfouriercoeffpnqn}
    \left|\widehat{H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)}(k) \right| 
    & \leq \sum_{l=-n}^{n} |\widehat{f}(l)| | \widehat{g}(k-l)| 2 |\phi_{l,k}|^\beta \left(\left|\textnormal{Si}_\beta\left(\frac{\phi_{l,k}}{2}\right) \right| + \left| \textnormal{Si}_\beta(\phi_{l,k}\varepsilon) \right| \right) \nonumber\\
    & \leq \tilde{M} \sum_{l=-n}^{n} |\widehat{f}(l)| | \widehat{g}(k-l)| |\phi_{l,k}|^\beta, 
    
\end{aligned}$$ where $\tilde{M} := 4 \sup_{\phi \in [0,\infty [} \textnormal{Si}_\beta (\phi) <\infty$ due to [@R12 Lem. 2.4]. By [\[formula:Hfouriercoeffpnqn\]](#formula:Hfouriercoeffpnqn){reference-type="eqref" reference="formula:Hfouriercoeffpnqn"} and $$\begin{aligned}
    |\phi_{k,l}|^\beta = |2\pi (ls_1 +(k-l)s_2)|^\beta \leq 2 \pi  |l|^{\beta} |k-l|^{\beta} \leq 2\pi (l^2 +1)^{\frac{\beta}{2}} ((k-l)^2+1)^{\frac{\beta}{2}},
    
\end{aligned}$$ we conclude $$\begin{aligned}
\label{formula:Hfouriercoeffpnqnfinal}
        \left|\widehat{H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)}(k) \right| \leq & \tilde{M} \sum_{l=-n}^{n} |\widehat{f}(l)| | \widehat{g}(k-l)| |\phi_{l,k}|^\beta  \nonumber\\
        \leq & M \sum_{l=-n}^{n} (l^2 +1)^{\frac{\beta}{2}}  |\widehat{f}(l)| ((k-l)^2+1)^{\frac{\beta}{2}} | \widehat{g}(k-l)| \nonumber\\
        = & M \sum_{l=-n}^{n} (l^2 +1)^{\frac{\beta}{2}}  |\widehat{p_n}(l)| ((k-l)^2+1)^{\frac{\beta}{2}} | \widehat{q_n}(k-l)|,
    
\end{aligned}$$ where $M:= 2\pi \tilde{M}$. In addition, we obtain by [\[formula:Hfouriercoeffpnqnfinal\]](#formula:Hfouriercoeffpnqnfinal){reference-type="eqref" reference="formula:Hfouriercoeffpnqnfinal"} and the elementary estimates $$\begin{aligned}
        (k^2+1)^{\frac{m}{2}} \leq 2^m \left((l^2+1)^{\frac{m}{2}} + ((k-l)^2+1)^{\frac{m}{2}} \right),
    
\end{aligned}$$ which are an immediate consequence of $|k| \leq 2 \max\{|l|, |k-l|\}$, that $$\begin{aligned}
\label{formula:Hs1s2decompose} 
&   \left|(k^2 + 1)^{\frac{m}{2}}\widehat{H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)}(k) \right|  \nonumber \\
     &\qquad \leq  MC(m) \sum_{l\in\mathbb{Z}} (l^2 + 1)^{\frac{m+\beta}{2}} \left|\widehat{p_n}(l)\right|  ((k-l)^2+1)^{\frac{\beta}{2}} \left| \widehat{q_n}(k-l) \right| \nonumber \\
    &\qquad\qquad     + MC(m) \sum_{l\in\mathbb{Z}}  (l^2 +1)^{\frac{\beta}{2}}  \left|\widehat{p_n}(l)\right| ((k-l)^2 + 1)^{\frac{m+\beta}{2}} \left| \widehat{q_n}(k-l) \right|,
    
\end{aligned}$$ where the positive constant $C(m) < \infty$ only depends on the parameter $m$. This leads us to the idea to set the following series component-wise for all $k\in\mathbb{Z}$ and any $\lambda >0$ $$\begin{aligned}
    p_n^\lambda(k) &:= (k^2 + 1)^{\frac{m+\lambda}{2}} \left|\widehat{p_n}(k)\right| \textnormal{ and } \\
    q_n^\lambda(k) &:= (k^2 + 1)^{\frac{m+\lambda}{2}} \left|\widehat{q_n}(k)\right|
    
\end{aligned}$$ such that we can rewrite [\[formula:Hs1s2decompose\]](#formula:Hs1s2decompose){reference-type="eqref" reference="formula:Hs1s2decompose"} as $$\begin{aligned}
    \left|(k^2 + 1)^{\frac{m}{2}}\widehat{H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)}(k) \right| \leq MC(m) \left( (p_n^\beta*q_n^0) (k) +  (p_n^0*q_n^\beta ) (k)\right).
    
\end{aligned}$$ Finally, we obtain the desired estimate [\[formula:BilinearHT\]](#formula:BilinearHT){reference-type="eqref" reference="formula:BilinearHT"} for $p_n$ and $q_n$ by applying Lemma [\[lem:Young\]](#lem:Young){reference-type="ref" reference="lem:Young"}, Lemma [\[lem:Sobolev\]](#lem:Sobolev){reference-type="ref" reference="lem:Sobolev"}, and Sobolev's embedding theorem to estimate $$\begin{aligned}
\label{formula:mainestimatepnqn}
    \|H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)\|_{H^m} & = \|( (k^2 + 1)^{\frac{m}{2}}\widehat{H_{s_1,s_2}^\varepsilon(p_n,q_n)}(k))_{k\in\mathbb{Z}} \|_{\ell^2} \nonumber\\
    & \leq MC(m) \left( \| ((p_n^\beta*q_n^0) (k))_{k\in\mathbb{Z}} \|_{\ell^2}  + \|((p_n^0*q_n^\beta ) (k))_{k\in\mathbb{Z}} \|_{\ell^2} \right) \nonumber\\
    & \leq MC(m) \left(\|p_n^\beta\|_{\ell^2} \|q_n^0\|_{\ell^1} +  \|p_n^0\|_{\ell^1} \|q_n^\beta\|_{\ell^2} \right) \nonumber\\
    & \leq MC(m)C_0 \left(\|p_n\|_{H^{m+\beta}} \|q_n\|_{H^m} + \|p_n\|_{H^m} \|q_n\|_{H^{m+\beta}}\right) \nonumber\\
    & = C_H \|p_n\|_{H^{m+\beta}} \|q_n\|_{H^{m+\beta}} 
    ,
\end{aligned}$$ where $C_H:= 2MC(m)C_0$ is a constant only depending on $m$ and $\beta$.

Finally, we get the statement [\[formula:BilinearHT\]](#formula:BilinearHT){reference-type="eqref" reference="formula:BilinearHT"} for $f$ and $g$ by passing to the limit $n\rightarrow \infty$. In particular, by using [\[formula:mainestimatepnqn\]](#formula:mainestimatepnqn){reference-type="eqref" reference="formula:mainestimatepnqn"}, we find for any integer $n\geq 0$ that $$\begin{aligned}
    \|H_{s_1,s_2,\beta }^\varepsilon(p_{n},q_{n})\|_{H^m} & \leq C_H \|p_{n}\|_{H^{m+\beta}} \|q_{n}\|_{H^{m+\beta}} \nonumber\\
    &  \leq C_H \|f\|_{H^{m+\beta}} \|g\|_{H^{m+\beta}}  \label{formula:Hfg}
    
\end{aligned}$$ By uniform convergence and by Lemma [\[lem:Hs1s2cont\]](#lem:Hs1s2cont){reference-type="ref" reference="lem:Hs1s2cont"} we find that $$\begin{aligned}
    & \|H_{s_1,s_2,\beta}^\varepsilon(f,g) - H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)\|_\infty \\
    &\quad \leq \|H_{s_1,s_2,\beta}^\varepsilon(f,g) - H_{s_1,s_2,\beta}^\varepsilon(p_n,g)\|_\infty + \|H_{s_1,s_2,\beta}^\varepsilon(p_n,g) - H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)\|_\infty \\
    &\quad = \|H_{s_1,s_2,\beta}^\varepsilon(f-p_n,g)\|_\infty + \|H_{s_1,s_2,\beta}^\varepsilon(p_n,g-q_n)\|_\infty \\
    &\quad \leq C(\beta,\varepsilon) 
    \|f-p_n\|_\infty
    \|g\|_\infty + C(\beta, \varepsilon) \|p_n\|_\infty 
    \|g-q_n\|_\infty \\
    &\quad \to 0
    
\end{aligned}$$ as $n\to \infty$, since $\|f-p_n\|_\infty \to 0$ and $\|g-q_n\|_\infty \to 0$ as $n\to \infty$ by our assumption [\[formula:apprfg\]](#formula:apprfg){reference-type="eqref" reference="formula:apprfg"}. Moreover, by the uniqueness of the Fourier coefficients of $H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n) \in H^m (\mathbb{R}/ \mathbb{Z},\mathbb{R}) \subseteq L^2(\mathbb{R}/ \mathbb{Z},\mathbb{R})$ we have, for all $k\in\mathbb{Z}$, that $$\begin{aligned}
    \left|\widehat{H_{s_1,s_2,\beta}^\varepsilon(f,g)}(k)- \widehat{H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)}(k)\right| 
    \to 0 
    
\end{aligned}$$ as $n\to \infty$. Thus for all positive integers $N \geq 1$ we find that $$\begin{aligned}
    &\Big| \Big( \sum_{|k|\leq N} (1+|k|^2)^m|\widehat{H_{s_1,s_2,\beta}^\varepsilon(p_n,q_n)}(k)|^2 \Big)^{\frac{1}{2}} 
    \\  &\hspace{3cm} 
    - \Big( \sum_{|k|\leq N} (1+|k|^2)^m|\widehat{H_{s_1,s_2,\beta}^\varepsilon(f,g)}(k)|^2 \Big)^{\frac{1}{2}} \Big| 
    \to 0
    
\end{aligned}$$ as $n\to\infty$. Then by [\[formula:Hfg\]](#formula:Hfg){reference-type="eqref" reference="formula:Hfg"} we conclude that $$\begin{aligned}
    \Big( \sum_{|k|\leq N} (1+|k|^2)^m|\widehat{H_{s_1,s_2,\beta}^\varepsilon(f,g)}(k)|^2 \Big)^{\frac{1}{2}} \leq C_H \|f\|_{H^{m+\beta}} \|g\|_{H^{m+\beta}} 
    
\end{aligned}$$ which implies the desired estimate [\[formula:BilinearHT\]](#formula:BilinearHT){reference-type="eqref" reference="formula:BilinearHT"} for $f$ and $g$. ◻
:::
