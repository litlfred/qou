---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-002-21-fractional-sobolev-spaces
section_title: "Fractional Sobolev spaces"
section_number: 2.1
pages: 3-4
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.868
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
---
[]{#sec:fractionalsobolevspaces label="sec:fractionalsobolevspaces"}

We denote by $|\cdot |$ the Euclidean norm on $\mathbb{C}^n$ for any integer $n\geq 1$. In this article we work with closed curves on the periodic domain $\mathbb{R}/ \mathbb{Z}$ so that a curve $f: \mathbb{R}\rightarrow \mathbb{R}^n$ is periodic with unit periodicity.

We know that for any $f\in L^2(\mathbb{R}/ \mathbb{Z}, \mathbb{C}^n)$ the Fourier series of $f$ in $x\in \mathbb{R}/ \mathbb{Z}$ is given by $\sum_{k\in\mathbb{Z}} \widehat{f}(k) e^{2\pi i k x},$ where the $k$-th Fourier coefficient of $f$ are given by $$\begin{aligned}
\widehat{f}(k) = \int_0^1 f(x) e^{-2\pi i k x} \mathrm{d} x .
\end{aligned}$$

The *fractional Sobolev space* of order $s\geq 0$ (i.e. the Bessel potential space of order $s \geq 0$) is defined as $$\begin{aligned}
H^s(\mathbb{R}/ \mathbb{Z}, \mathbb{C}^n) := \{f\in L^2 (\mathbb{R}/ \mathbb{Z}, \mathbb{C}^n) \ | \ \| f \|_{H^s}:= \| f \|_{H^s(\mathbb{R}/ \mathbb{Z},\mathbb{C}^n)} := \sqrt{(f,f)_{H^s}} < \infty  \},
\end{aligned}$$ equipped with the scalar product $$\begin{aligned}
(f,g)_{H^s} := (f,g)_{H^s(\mathbb{R}/ \mathbb{Z},\mathbb{C}^n)} := \sum_{k\in\mathbb{Z}} (1+k^2)^s \langle \widehat{f}(k), \widehat{g}(k) \rangle_{\mathbb{C}^n}.
\end{aligned}$$

Furthermore, we will need the embeddings $H^s(\mathbb{R}/ \mathbb{Z},\mathbb{C}^n)\subseteq H^t(\mathbb{R}/ \mathbb{Z},\mathbb{C}^n)$ for any $0 \leq t<s$ (cf. [@DNPV12 Prop. 2.1, Corol. 2.3]) as well as $H^s(\mathbb{R}/ \mathbb{Z},\mathbb{C}^n) \subseteq C(\mathbb{R}/ \mathbb{Z},\mathbb{C}^n)$ for any $s> \frac{1}{2}$ (cf. [@DNPV12 Theor. 8.2]), from which we can deduce that the Fourier series of any $f\in H^s(\mathbb{R}/ \mathbb{Z},\mathbb{C})$ with $s> \frac{1}{2}$ converges absolutely and uniformly to $f$. In fact the space $H^m$, for any integer $m\geq 0$, coincides with the classical Sobolev space and the norms $\|\cdot\|_{H^m}$ and $\|f\|_{W^m}:= (\sum_{\nu=0}^{m} \|\partial^\nu f\|^2_{L^2})^{\frac{1}{2}}$ are equivalent (cf. [@R09 Lem. 1.2] or [@AF03 7.62]). Furthermore, let us also mention the Banach algebra property of $H^m$ for any integer $m\geq 1$, i.e. there exists a positive constant $C_m$ such that $$\begin{aligned}
\label{prop:Banachalgebra}
    \|fg\|_{H^m} \leq C_m \|f\|_{H^m} \|g\|_{H^m}
    
\end{aligned}$$ for all $f,g \in H^m(\mathbb{R}/ \mathbb{Z},\mathbb{R})$ (cf. [@AF03 Theor. 4.39]).
