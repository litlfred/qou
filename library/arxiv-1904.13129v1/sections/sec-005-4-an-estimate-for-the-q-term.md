---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-005-4-an-estimate-for-the-q-term
section_title: "An estimate for the Q term"
section_number: 4
pages: 7-9
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.865
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
---
[]{#sec:maintermQ label="sec:maintermQ"}

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
