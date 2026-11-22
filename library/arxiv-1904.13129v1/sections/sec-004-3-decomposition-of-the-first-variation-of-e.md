---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-004-3-decomposition-of-the-first-variation-of-e
section_title: "Decomposition of the first variation of E"
section_number: 3
pages: 6-7
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.974
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
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
