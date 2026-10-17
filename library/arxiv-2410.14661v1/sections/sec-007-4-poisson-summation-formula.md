---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-007-4-poisson-summation-formula
section_title: "Poisson summation formula"
section_number: 4
pages: 15-20
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.914
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
[]{#Section-Poissonsummation label="Section-Poissonsummation"} By Proposition [\[Prop-RTN\]](#Prop-RTN){reference-type="ref" reference="Prop-RTN"}, we have $$\begin{aligned}
   g_{N}(a,k,l)=\sin\left(\frac{(a+\frac{1}{2})\pi}{N+\frac{1}{2}}\right)\sin\left(\frac{2\pi(l+\frac{1}{2})}{N+\frac{1}{2}}\right)e^{(N+\frac{1}{2})\hat{V}_N\left(\frac{a+\frac{1}{2}}{N+\frac{1}{2}},\frac{k+\frac{1}{2}}{N+\frac{1}{2}},\frac{l+\frac{1}{2}}{N+\frac{1}{2}}\right)}
\end{aligned}$$ We consider the real part of the potential function $$\begin{aligned}
&v(\theta_1,\theta_2,\theta_3)\\\nonumber
&=\text{Re}\hat{V}(\theta_1,\theta_2,\theta_3)\\\nonumber
&= \text{Re}\left(\frac{1}{2\pi\sqrt{-1}}\left(\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})\right.\right.\\\nonumber
&\left.\left.-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right)   \right)\\\nonumber
&=\Lambda(\theta_2+\theta_3)+\Lambda(\theta_2-\theta_3)-\Lambda(\theta_2+\theta_1)-\Lambda(\theta_2)-\Lambda(\theta_2-\theta_1)
\end{aligned}$$ where $D$ is given by the following domain $$\begin{aligned}
D'=\{(\theta_1,\theta_2,\theta_3)\in \mathbb{R}^3|-1 \leq \theta_1\leq 1, 0\leq \theta_3\leq \theta_2\leq 1-\theta_1 \}    
\end{aligned}$$

Let $$\begin{aligned}
D=\{(\theta_1,\theta_2,\theta_3)\in D'| \frac{1}{2}<\theta_2<1\},    
\end{aligned}$$ we have

::: lemma
There exists $\epsilon>0$, such that the following domain $$\begin{aligned}
   \text{Re}\hat{V}(\theta_1,\theta_2,\theta_3)>0.324-\epsilon   
\end{aligned}$$ is included in the region $D$.
:::

::: proof
*Proof.* We only need to show that when $0\leq \theta_2\leq \frac{1}{2}$, we have $$\begin{aligned}
 \label{formula-ReV<}
   \text{Re}\hat{V}(\theta_1,\theta_2,\theta_3)\leq 0.324-\epsilon. 
\end{aligned}$$ Clearly, when $\theta_2=0, \frac{1}{2}$, $\text{Re}\hat{V}(\theta_1,\theta_2,\theta_3)=0\leq 0.324-\epsilon$ holds.

For a fixed $0<\theta_2< \frac{1}{2}$, we consider the function $$\begin{aligned}
 f(\theta_1,\theta_2)=2\Lambda(\theta_2)-\Lambda(\theta_2+\theta_1)-\Lambda(\theta_2-\theta_1).   
\end{aligned}$$ Then $$\begin{aligned}
\text{Re}\hat{V}(\theta_1,\theta_2,\theta_3)=\Lambda(\theta_2+\theta_3)+\Lambda(\theta_2-\theta_3)-3\Lambda(\theta_2)+f(\theta_1,\theta_2).
\end{aligned}$$

Clearly, $$\begin{aligned}
f_{\theta_1}(\theta_1,\theta_2)=\log \left|\frac{\sin(\pi(\theta_2+\theta_1)) }{\sin(\pi(\theta_2-\theta_1))}\right|.     
\end{aligned}$$ since $0<\theta_2<\frac{1}{2}$ and $\theta_2+\theta_1<1$, we obtain that $f_{\theta_1}(\theta_1,\theta_2)=0$ has a unique solution $\theta_1=\frac{1}{2}$. Moreover, when $\theta_1\in [0,\frac{1}{2}]$, we have $f_{\theta_1}(\theta_1,\theta_2)\geq 0$ and when $\theta_1\in [\frac{1}{2},1-\theta_2]$, we have $f_{\theta_1}(\theta_1,\theta_2)\leq 0$. Hence, for $0\leq \theta_2\leq \frac{1}{2}$ and $0\leq \theta_1\leq 1-\theta_2$, we have $$\begin{aligned}
   f(\theta_1,\theta_2)\leq f\left(\frac{1}{2},\theta_2\right)=2\Lambda(\theta_2).  
\end{aligned}$$

Suppose formula ([\[formula-ReV\<\]](#formula-ReV<){reference-type="ref" reference="formula-ReV<"}) does not holds, then $$\begin{aligned}
\text{Re}\hat{V}(\theta_1,\theta_2,\theta_3)=\Lambda(\theta_2+\theta_3)+\Lambda(\theta_2-\theta_3)-3\Lambda(\theta_2)+f(\theta_1,\theta_2)\geq 0.324-\epsilon  
\end{aligned}$$ So we obtain $$\begin{aligned}
-3\Lambda(\theta_2)&\geq 0.324-\epsilon-f(\theta_1,\theta_2)-2\Lambda\left(\frac{1}{6}\right)\\\nonumber
&\geq 0.324-\epsilon-2\Lambda(\theta_2)-2\Lambda\left(\frac{1}{6}\right). 
\end{aligned}$$ It implies that $$\begin{aligned}
   -\Lambda(\theta_2)\geq 0.324-\epsilon-0.3230659473> 0,  
\end{aligned}$$ which is impossible, since $-\Lambda(\theta_2)\leq 0$ when $\theta_2\in [0,\frac{1}{2}]$. ◻
:::

Furthermore, as in [@CZ23-1], we introduce the domain $$\begin{aligned}
D_0=&\left\{ (\theta_1,\theta_2,\theta_3)\in D|0.02 \leq \theta_2-\theta_3\leq 0.7, 1.02 \leq \theta_2+\theta_3\leq 1.7, \right. \\\nonumber & \left. 0.2 \leq \theta_3\leq 0.8,0.5\leq \theta_2\leq 0.909\right\}\cap D'
\end{aligned}$$ for this case.

Note that the region $D_0$ lies in the tetrahedron $FEBC$ which is symmetry with respect to the plane EFH and the $\theta_2\theta_3$-plane. Note that, we only illustrated the upper half of this region in Figure [1](#figure-D0){reference-type="ref" reference="figure-D0"}.

<figure id="figure-D0">
<p><span class="math display">$$\begin{aligned}
\raisebox{-15pt}{
\includegraphics[width=300 pt]{D0.pdf}}.
\end{aligned}$$</span></p>
<figcaption>The region <span class="math inline"><em>D</em><sub>0</sub></span> lies in the tetrahedron FEBC</figcaption>
</figure>

Then we have

::: lemma
[]{#lemma-regionD'0 label="lemma-regionD'0"} The following domain $$\begin{aligned}
 \label{formula-domain}
        \left\{(\theta_1,\theta_3,\theta_3)\in D| v(\theta_1,\theta_2,\theta_3)> \frac{3.56337}{2\pi }\right\}
    
\end{aligned}$$ is included in the region $D_0$.
:::

::: proof
*Proof.* By using formulas ([\[formula-vtheta1\]](#formula-vtheta1){reference-type="ref" reference="formula-vtheta1"}) and ([\[formula-vtheta2\]](#formula-vtheta2){reference-type="ref" reference="formula-vtheta2"}), and together with Lemma 4.1 in [@CZ23-1]. ◻
:::

By Corollary [\[corollary-zetaR\]](#corollary-zetaR){reference-type="ref" reference="corollary-zetaR"}, for $p,q$ satisfies the condition ([\[formula-pqconditions\]](#formula-pqconditions){reference-type="ref" reference="formula-pqconditions"}), we have $\zeta_{\mathbb{R}}(p,q)\geq \frac{3.56337}{2\pi }$. Hence

::: proposition
[]{#prop-gkl label="prop-gkl"} For $(p,q)\in S$ and $(\frac{a+\frac{1}{2}}{N+\frac{1}{2}},\frac{k+\frac{1}{2}}{N+\frac{1}{2}},\frac{l+\frac{1}{2}}{N+\frac{1}{2}})\in D\setminus D_0$, we have $$\begin{aligned}
    |g_{N}(k,l)|<O\left(e^{(N+\frac{1}{2})\left(\zeta_{\mathbb{R}}(p,q)-\epsilon\right)}\right)
\end{aligned}$$ for some sufficiently small $\epsilon>0$.
:::

For a sufficiently small $\varepsilon$, we take a smooth bump function $\psi$ on $\mathbb{R}^3$ such that $\psi(\theta_1,\theta_2,\theta_3)=1$ on $(\theta_1,\theta_2,\theta_3)\in D_{\varepsilon}$, $0<\psi(\theta_1,\theta_2,\theta_3)<1$ on $(\theta_1,\theta_2,\theta_3)\in D_0\setminus D_{\varepsilon}$, $\psi(\theta_1,\theta_2,\theta_3)=0$ for $(\theta_1,\theta_2,\theta_3)\notin D_0$. Let $$\begin{aligned}
    h_N(a,k,l)=\psi\left(\frac{2a+1}{2N+1},\frac{2k+1}{2N+1},\frac{2l+1}{2N+1}\right)g_N(a,k,l).
\end{aligned}$$

Then by Proposition [\[prop-gkl\]](#prop-gkl){reference-type="ref" reference="prop-gkl"}, for $(p,q)$ satisfies ([\[formula-pqconditions\]](#formula-pqconditions){reference-type="ref" reference="formula-pqconditions"}) we obtain $$\begin{aligned}
  \label{formula-JN}
    RT_r(M)=\sum_{(a,k,l)\in \mathbb{Z}^3}h_N(a,k,l)+O\left(e^{(N+\frac{1}{2})\left(\zeta_{\mathbb{R}}(p,q)-\epsilon\right)}\right).
\end{aligned}$$ Recall the Poisson summation formula [@SS03] in 3-dimensional case which states that for any function $h$ in the Schwartz space on $\mathbb{R}^2$, we have $$\begin{aligned}
 \label{formula-Poisson}
    \sum_{(a,k,l)\in \mathbb{Z}^3}h(a,k,l)=\sum_{(m_1,m_2,m_3)\in \mathbb{Z}^3}\hat{h}(m_1,m_2,m_3)
\end{aligned}$$ where $$\begin{aligned}
    \hat{h}(m_1,m_2,m_3)=\int_{\mathbb{R}^3}h(\theta_1,\theta_2,\theta_3)e^{-2\pi \sqrt{-1}m_1 \theta_1-2\pi \sqrt{-1}m_2 \theta_2-2\pi\sqrt{-1}m_3 \theta_3}d\theta_1d\theta_2d\theta_3.
\end{aligned}$$

Note that $h_N$ is $C^{\infty}$-smooth and equals zero outside $D_0$, it is in the Schwartz space on $\mathbb{R}^3$. The Poisson summation formula ([\[formula-Poisson\]](#formula-Poisson){reference-type="ref" reference="formula-Poisson"}) holds for $h_N$.

By using change of variables $\theta_1=\frac{a+\frac{1}{2}}{N+\frac{1}{2}}, \theta_2=\frac{k+\frac{1}{2}}{N+\frac{1}{2}}, \theta_3=\frac{l+\frac{1}{2}}{N+\frac{1}{2}}$, we compute the Fourier coefficient $\hat{h}_{N}(m_1,m_2,m_3)$ as follows $$\begin{aligned}
    &\int_{\mathbb{R}^3}h_N(a,k,l)e^{-2\pi \sqrt{-1}m_1 a-2\pi \sqrt{-1}m_2 k-2\pi\sqrt{-1}m_3 l}dadkdl\\\nonumber
    &=(-1)^{m_1+m_2+m_3}\left(N+\frac{1}{2}\right)^3\\\nonumber
    &\cdot\int_{\mathbb{R}^3}h_N\left((N+\frac{1}{2})\theta_1-\frac{1}{2},(N+\frac{1}{2})\theta_2-\frac{1}{2},(N+\frac{1}{2})\theta_3-\frac{1}{2}\right)e^{-2\pi \sqrt{-1}\sum_{i=1}^3\frac{(2N+1)m_i(\theta_1+\theta_2+\theta_3)}{2}}d\theta_1d\theta_2d\theta_3\\\nonumber
    &=(-1)^{m_1+m_2+m_3}\left(N+\frac{1}{2}\right)^3\kappa_r'\\\nonumber
    &\cdot\int_{D_0}\sin(\pi \theta_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\left(V_N\left(\theta_1,\theta_2,\theta_3\right)-2\pi\sqrt{-1}m_1\theta_1-2\pi\sqrt{-1}m_2\theta_2-2\pi\sqrt{-1}m_3 \theta_3\right)}d\theta_1d\theta_2d\theta_3,
\end{aligned}$$ Therefore, applying the Poisson summation formula ([\[formula-Poisson\]](#formula-Poisson){reference-type="ref" reference="formula-Poisson"}) to ([\[formula-JN\]](#formula-JN){reference-type="ref" reference="formula-JN"}), we obtain

::: proposition
[]{#prop-fouriercoeff label="prop-fouriercoeff"} For $(p,q)\in S$ , the Reshetinkhin-Turaev invariant $RT_r(M)$ is given by $$\begin{aligned}
 \label{formula-fouriercoeff}
     RT_r(M)=\sum_{(m_1,m_2,m_3)\in \mathbb{Z}^3}\hat{h}_N(m_1,m_2,m_3)+O\left(e^{(N+\frac{1}{2})\left(\zeta_{\mathbb{R}}(p,q)-\epsilon\right)}\right),
\end{aligned}$$ where $$\begin{aligned}
      \hat{h}_N(m_1,m_2,m_3)=&(-1)^{m_1+m_2+m_3}\left(N+\frac{1}{2}\right)^{\frac{5}{2}}\kappa_r' \\\nonumber
      &\cdot\int_{D_0}\sin(\pi \theta_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\hat{V}_N\left(\theta_1,\theta_2,\theta_3;m_1,m_2,m_3\right)}dsdtdu
\end{aligned}$$ with $$\begin{aligned}
&\hat{V}_N\left(\theta_1,\theta_2,\theta_3;m_1,m_2,m_3\right)\\\nonumber
&=\hat{V}_N\left(\theta_1,\theta_2,\theta_3\right)-2\pi\sqrt{-1}m_1\theta_1-2\pi\sqrt{-1}m_2\theta_2-2\pi\sqrt{-1}m_3 \theta_3,
\end{aligned}$$ and $\hat{V}_{N}(\theta_1,\theta_2,\theta_3)$ is given by formula ([\[formula-VN\]](#formula-VN){reference-type="ref" reference="formula-VN"}).
:::

::: lemma
The following identity holds $$\begin{aligned}
 \label{formula-potientalsym}
          &\hat{V}_{N}(\theta_1,\theta_2,1-\theta_3;m_1,m_2,m_3)
          &=\hat{V}_{N}(\theta_1,\theta_2,\theta_3;m_1,m_2,-m_3-2)-2\pi \sqrt{-1}(m_3+1). 
    
\end{aligned}$$
:::

::: proof
*Proof.* Since we have the following identity $$\begin{aligned}
        &\pi\sqrt{-1}\left((2p+1)(1-\theta_3)^2-(2p+2m_3+3)(1-\theta_3)\right)\\\nonumber
        &=\pi\sqrt{-1}\left((2p+1)\theta_3^2-(2p+2(-m_3-2)+3)\theta_3)\right)\\\nonumber
        &-2\pi \sqrt{-1}(m_3+1).
    
\end{aligned}$$ which immediately gives the formula ([\[formula-potientalsym\]](#formula-potientalsym){reference-type="ref" reference="formula-potientalsym"}). ◻
:::

::: proposition
[]{#prop-hmn label="prop-hmn"} For any $m_1,m_2,m_3\in \mathbb{Z}$, we have $$\begin{aligned}
        \hat{h}_{N}(m_1,m_2,-m_3-2)=(-1)^{m_3}\hat{h}_{N}(m_1,m_2,m_3).
    
\end{aligned}$$
:::

::: proof
*Proof.* Since $$\begin{aligned}
      &\sin(\pi \theta_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\hat{V}_N\left(\theta_1,\theta_2,1-\theta_3;m_1,m_2,m_3\right)} \\\nonumber
      &=\sin(\pi \theta_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\left(\hat{V}_{N}\left(\theta_1,\theta_2,\theta_3;m_1,m_2,-m_3-2\right)-2\pi\sqrt{-1}(m_3+1)\right)}\\\nonumber
      &=\sin(\pi \theta_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\hat{V}_N\left(\theta_1,\theta_2,\theta_3;m_1,m_2,-m_3-2\right)}(-1)^{m_3+1},
    
\end{aligned}$$ since the region $D_0$ is symmetric with respect to the plane $\theta_3=\frac{1}{2}$.

Then we have $$\begin{aligned}
    &\int_{D_0}\sin(\pi s)\sin(2\pi u)e^{(N+\frac{1}{2})\hat{V}_N\left(\theta_1,\theta_2,\theta_3;m_1,m_2,-m_3-2\right)}d\theta_1d\theta_2d\theta_3\\\nonumber
    &=(-1)^{m_3+1}\int_{D_0}\sin (\pi \theta_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\hat{V}_N\left(\theta_1,\theta_2,1-\theta_3;m_1,m_2,m_3\right)}d\theta_1d\theta_2d\theta_3\\\nonumber
    &=(-1)^{m_3}\int_{D_0}\sin(\pi s)\sin(2\pi \tilde{u})\exp^{(N+\frac{1}{2})\hat{V}_N\left(\theta_1,\theta_2,\tilde{\theta}_3;m_1,m_2,m_3\right)}d\theta_1 d\theta_2 d\tilde{\theta}_3,
\end{aligned}$$ where in the third "=\", we have let $\tilde{\theta}_3=1-\theta_3$. It follows that $$\begin{aligned}
        \hat{h}_{N}(m_1,m_2,-m_3-2)=(-1)^{m_3}\hat{h}_{N}(m_1,m_2,m_3).
    
\end{aligned}$$ ◻
:::

::: corollary
We have $$\begin{aligned}
 \label{formula-bigcancel}
        \hat{h}_{N}(m_1,m_2,-1)=0,
    
\end{aligned}$$ and $$\begin{aligned}
    \hat{h}_{N}(m_1,m_2,-2)=\hat{h}_{N}(m_1,m_2,0).    
    
\end{aligned}$$
:::

Note that $$\begin{aligned}
 \label{formula-hatV}
  \hat{V}_{N}(-\theta_1,\theta_2,\theta_3,m_1,m_2,m_3)=\hat{V}_N(\theta_1,\theta_2,\theta_3,-m_1-1,m_2,m_3).  
\end{aligned}$$

Since the region $D_0$ is symmetry with respect to the plane $\theta_1=0$. We have $$\begin{aligned}
&\int_{D_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3,m_1,m_2,m_3)}d\theta_1d\theta_2d\theta_3\\\nonumber
&=-\int_{D_0}\sin(\pi\tilde{\theta}_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(-\tilde{\theta}_1,\theta_2,\theta_3,m_1,m_2,m_3)}d\tilde{\theta}_1d\theta_2d\theta_3\\\nonumber
&=-\int_{D_0}\sin(\pi\theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3,-m_1-1,m_2,m_3)}d\theta_1d\theta_2d\theta_3.
\end{aligned}$$

Hence, we have $$\begin{aligned}
\hat{h}_N(m_1,m_2,m_3)= \hat{h}_N(-m_1-1,m_2,m_3).   
\end{aligned}$$

So we obtain $$\begin{aligned}
 \label{formula-RTN}
   RT_r(M)&=2\sum_{m_1\geq 0}\sum_{m_2\in \mathbb{Z}}\sum_{m_3\in \mathbb{Z}}\hat{h}_{N}(m_1,m_2,m_3)+O(e^{(N+\frac{1}{2})(\zeta_\mathbb{R}(p,q))-\epsilon})\\\nonumber
   &=4\sum_{m_1\geq 0}\sum_{m_2\in \mathbb{Z}}\sum_{m_3\geq 0}\hat{h}_{N}(m_1,m_2,m_3)+O(e^{(N+\frac{1}{2})(\zeta_\mathbb{R}(p,q))-\epsilon}),
\end{aligned}$$ where in the second "=\" we have used the Proposition [\[prop-hmn\]](#prop-hmn){reference-type="ref" reference="prop-hmn"}. Note that $$\begin{aligned}
 \label{formula-heN}
 \hat{h}_N(m_1,m_2,m_3)&=(-1)^{m_1+m_2+m_3}\kappa''_r\\\nonumber
 &\cdot\int_{D_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3,m_1,m_2,m_3)}d\theta_1d\theta_2d\theta_3,   
\end{aligned}$$ where $$\begin{aligned}
  \kappa''_r= \left(N+\frac{1}{2}\right)^\frac{5}{2}\kappa'_r=\left(N+\frac{1}{2}\right)^\frac{3}{2}e^{\sigma_{p,q}\left(\frac{3}{2N+1}+\frac{N+1}{2}\right)\pi\sqrt{-1}}. 
\end{aligned}$$
