---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-006-5-a-fractional-leibniz-rule-and-the-form-of-pt-q
section_title: "A fractional leibniz rule and the form of PT Q"
section_number: 5
pages: 9-14
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.955
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
---
[]{#sec:bilinearHilberttransform label="sec:bilinearHilberttransform"}

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
