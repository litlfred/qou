---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-017-64-estimation-of-the-critical-value
section_title: "Estimation of the critical value"
section_number: 6.4
pages: 46-52
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.873
---
In this section, we prove the Lemma [\[lemma-volumeestimate\]](#lemma-volumeestimate){reference-type="ref" reference="lemma-volumeestimate"} which gives the estimation of the critical value $\zeta_{\mathbb{R}}(p,q)$. Recall that $\zeta_{\mathbb{R}}(p,q)$ is given by $$\begin{aligned}
        \zeta_{\mathbb{R}}(p,q)=\text{Re} \hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0), 
\end{aligned}$$ where $(\theta_1^0,\theta_2^0,\theta_3^0)$ is the unique solution of the equations $$\begin{aligned}
 \label{formula-Vtheta1}
\hat{V}_{\theta_1}=\pi\sqrt{-1}(q\theta_1-2\theta_1-1)+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})=0, 
\end{aligned}$$ $$\begin{aligned}
 \label{formula-Vtheta2}
\hat{V}_{\theta_2}&=-2\pi\sqrt{-1}-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})+\log(1-e^{2\pi\sqrt{-1}\theta_2})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})=0,    
\end{aligned}$$ $$\begin{aligned}
 \label{formula-Vtheta3}
&\hat{V}_{\theta_3}=\pi\sqrt{-1}((4p+2)\theta_3-(2p+3))-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})=0.
\end{aligned}$$

Putting $\gamma_1=\frac{1}{p}, \gamma_2=\frac{1}{q}$, we regard $(\theta_1^0,\theta_2^0,\theta_3^0)$ as a function of $\gamma_1,\gamma_2$, and the denote it by $(\theta_1(\gamma_1,\gamma_2),\theta_2(\gamma_1,\gamma_2),\theta_3(\gamma_1,\gamma_2))$, then by expanding the above equations ([\[formula-Vtheta1\]](#formula-Vtheta1){reference-type="ref" reference="formula-Vtheta1"}), ([\[formula-Vtheta2\]](#formula-Vtheta2){reference-type="ref" reference="formula-Vtheta2"}) and ([\[formula-Vtheta3\]](#formula-Vtheta3){reference-type="ref" reference="formula-Vtheta3"}), we obtain $$\begin{aligned}
 \label{formula-thetaTaylor}
    \theta_1(\gamma_1,\gamma_2)&=\gamma_2-2(1+\sqrt{-1})\gamma_2^2+8\sqrt{-1}\gamma_2^3-\frac{\sqrt{-1}}{4}\pi^2\gamma_1^2\gamma_2^2-(1-\sqrt{-1})\pi^2\gamma_1^2\gamma_2^3+\cdots\\\nonumber
    \theta_2(\gamma_1,\gamma_2)&=\frac{\log(1-2\sqrt{-1})}{2\pi\sqrt{-1}}+1+\frac{1+2\sqrt{-1}}{40}\pi\gamma_1^2+\frac{-2+\sqrt{-1}}{5}\pi\gamma_2^2+\frac{-3+4\sqrt{-1}}{100}\pi^3\gamma_1^2\gamma_2^2+\cdots\\\nonumber
    \theta_3(\gamma_1,\gamma_2)&=\frac{1}{2}+\frac{1}{2}\gamma_1+\frac{1-\sqrt{-1}}{8}\gamma_1^2-\frac{\sqrt{-1}}{16}\gamma_1^3-\frac{\sqrt{-1}}{8}\pi^2\gamma_1^2\gamma_2^2+\cdots
\end{aligned}$$

Now, we put $$\begin{aligned}
    \hat{V}(\gamma_1,\gamma_2)&=\hat{V}(p,q,\theta_1(\gamma_1,\gamma_2),\theta_2(\gamma_1,\gamma_2),\theta_3(\gamma_1,\gamma_2))\\\nonumber
    &=\pi\sqrt{-1}\left(\frac{3}{2\gamma_2}+\frac{\theta_1^2}{2\gamma_2}-\theta_1^2-\theta_1+\left(\frac{2}{\gamma_1}+1\right)\theta_3^2-\left(\frac{2}{\gamma_1}+3\right)\theta_3-2\theta_2\right)\\\nonumber
&+\frac{1}{2\pi\sqrt{-1}}\left(\frac{\pi^2}{6}+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})\right.\\\nonumber
&\left.-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right),
\end{aligned}$$

then $$\begin{aligned}
\frac{\partial \hat{V}(\gamma_1,\gamma_2)}{\partial\gamma_1}&=V_{\theta_1}\frac{d\theta_1}{d\gamma_1}+V_{\theta_2}\frac{d\theta_2}{d\gamma_1}+V_\frac{d\theta_3}{d\gamma_1}+\frac{2\pi\sqrt{-1}}{\gamma_1^2}(\theta_3-\theta_3^2)\\\nonumber
&=\frac{2\pi\sqrt{-1}}{\gamma_1^2}(\theta_3-\theta_3^2)\\\nonumber
&=\frac{\pi\sqrt{-1}}{2}\frac{1}{\gamma_1^2}-\frac{\pi\sqrt{-1}}{2}-\frac{1+\sqrt{-1}}{4}\pi \gamma_1-\frac{\pi^3}{4}\gamma_1\gamma_2^2-\frac{3}{16}\pi\gamma_1^2+\cdots    
\end{aligned}$$ $$\begin{aligned}
    \frac{\partial \hat{V}(\gamma_1,\gamma_2)}{\partial \gamma_2}&=V_{\theta_1}\frac{d\theta_1}{d\gamma_2}+V_{\theta_2}\frac{d\theta_2}{d\gamma_2}+V_{\theta_3}\frac{d\theta_3}{d\gamma_2}-\frac{\pi\sqrt{-1}}{2\gamma_2^2}(3-\theta_1^2)\\\nonumber
&=-\frac{\pi\sqrt{-1}}{2\gamma_2^2}(3-\theta_1^2)\\\nonumber
&=-\frac{3\pi\sqrt{-1}}{2}\frac{1}{\gamma_2^2}-\frac{\pi\sqrt{-1}}{2}+(-2+2\sqrt{-1})\pi\gamma_2+12\pi\gamma_2^2+
\cdots  
\end{aligned}$$

We obtain $$\begin{aligned}
2\pi \hat{V}(\gamma_1,\gamma_2)&=v_8-\sqrt{-1}\pi^2\frac{1}{\gamma_1}-3\sqrt{-1}\pi^2\frac{1}{\gamma_2}-\pi^2\sqrt{-1}\gamma_2\\\nonumber
&+(-2+2\sqrt{-1})\pi^2\gamma_2^2-\sqrt{-1}\pi^2\gamma_1-\frac{1+\sqrt{-1}}{4}\pi^2\gamma_1^2+\cdots,    
\end{aligned}$$ and $$\begin{aligned}
2\pi\text{Re}\hat{V}(\gamma_1,\gamma_2)=v_8-\frac{1}{4}\pi^2\gamma_1^2-2\pi^2\gamma_2^2-\frac{1}{8}\pi^2\gamma_1^3+8\pi^2\gamma_2^3+\cdots, 
\end{aligned}$$ where $v_8$ denotes the hyperbolic volume of the regular octahedron in $\mathbb{H}^3$.

Note that, when $\gamma_2=0$, we obtain $$\begin{aligned}
2\pi \text{Re}\hat{V}(\gamma_1,0)=v_8-\frac{1}{4}\pi^2\gamma_1^2-\frac{1}{8}\pi^2\gamma_1^3+\cdots
\end{aligned}$$ which is just the formula (6.100) in ([@CZ23-1]).

In conclusion, we have the following estimations for the critical value

::: theorem
$$\begin{aligned}
        &2\pi\hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber
        &=v_8-\left(\sqrt{-1}\pi^2\frac{1}{\gamma_1}+3\sqrt{-1}\pi^2\frac{1}{\gamma_2}\right)-(\sqrt{-1}\pi^2\gamma_1+\sqrt{-1}\pi^2\gamma_2)\\\nonumber
        &-\left(\left(\frac{1}{4}+\frac{\sqrt{-1}}{4}\right)\pi^2\gamma_1^2+2(1-\sqrt{-1})\pi^2\gamma_2^2\right)+\left(-\frac{1}{8}\pi^2\gamma_1^3+8\pi^2\gamma_2^3\right)+\cdots
    
\end{aligned}$$ where $\gamma_1=\frac{1}{p}, \gamma_2=\frac{1}{q}$. $$\begin{aligned}
  &2\pi \text{Re} \hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber
  &=v_8-\left(\frac{1}{4}\pi^2\gamma_1^2+2\pi^2\gamma_2^2\right)+\left(-\frac{1}{8}\pi^2\gamma_1^3+8\pi^2\gamma_2^3\right)\\\nonumber
  &+\left(\left(-\frac{1}{32}\pi^2-\frac{1}{192}\pi^4\right)\gamma_1^4-\frac{1}{4}\pi^4\gamma_1^2\gamma_2^2+(-16\pi^2+\frac{1}{3}\pi^4)\gamma_2^4\right)+\cdots
  
\end{aligned}$$ In particular, by Theorem [\[theorem-critical=volume\]](#theorem-critical=volume){reference-type="ref" reference="theorem-critical=volume"}, we have $$\begin{aligned}
   &Vol\left(S^3\setminus \mathcal{K}_p\right)\\\nonumber
   &=2\pi \text{Re}\hat{V}(p,\infty,\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber
   &=v_8-\frac{1}{4}\pi^2\gamma_1^2-\frac{1}{8}\pi^2\gamma_1^3+\left(\frac{1}{32}\pi^2+\frac{1}{192}\pi^4\right)\gamma_1^4+\cdots
\end{aligned}$$ and $$\begin{aligned}
      &2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)\\\nonumber
      &=2\pi \text{Re}\hat{V}\left(\infty,q,\theta_1,\theta_2,\theta_3\right)\\\nonumber
      &=v_8-2\pi^2\gamma_2^2+8\pi^2\gamma_2^3+(-16\pi^2+\frac{1}{3}\pi^4)\gamma_2^4+\cdots
  
\end{aligned}$$
:::

So we have $$\begin{aligned}
&2\pi \text{Re}\hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber &=Vol\left(S^3\setminus \mathcal{K}_p\right)-2\pi^2\gamma_2^2+8\pi^2\gamma_2^3-\frac{1}{4}\pi^4\gamma_1^2\gamma_2^2+\cdots  
\end{aligned}$$ or $$\begin{aligned}
&2\pi \text{Re}\hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber &=2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\frac{1}{4}\pi^2\gamma_1^2-\frac{1}{8}\pi^2\gamma_1^3+\left(-\frac{1}{32}\pi^2-\frac{1}{192}\pi^4\right)\gamma_1^4+\cdots  
\end{aligned}$$ By Theorem [\[theorem-critical=volume\]](#theorem-critical=volume){reference-type="ref" reference="theorem-critical=volume"}, we have $$\begin{aligned}
&Vol\left(M_{p,q}\right)\\\nonumber
&=2\pi \text{Re}\hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber
  &=v_8-\left(\frac{1}{4}\pi^2\gamma_1^2+2\pi^2\gamma_2^2\right)+\left(-\frac{1}{8}\pi^2\gamma_1^3+8\pi^2\gamma_2^3\right)\\\nonumber
  &+\left(\left(-\frac{1}{32}\pi^2-\frac{1}{192}\pi^4\right)\gamma_1^4-\frac{1}{4}\pi^4\gamma_1^2\gamma_2^2+(-16\pi^2+\frac{1}{3}\pi^4)\gamma_2^4\right)+\cdots\\\nonumber
  &=2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\frac{1}{4}\pi^2\gamma_1^2-\frac{1}{8}\pi^2\gamma_1^3-\left(\frac{1}{32}\pi^2+\frac{1}{192}\pi^4\right)\gamma_1^4-\frac{1}{4}\pi^4\gamma_1^2\gamma_2^4+\cdots
\end{aligned}$$

From the above expansion formula, in principal, we can obtain that

::: theorem
[]{#theorem-inprincipal1 label="theorem-inprincipal1"} $$\begin{aligned}
Vol\left(M_{p,q}\right)>2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\frac{49}{64}\pi^2\frac{1}{p^2}.    
\end{aligned}$$
:::

Fixing $\theta_3=c_3$, we have $$\begin{aligned}
&\hat{V}_{\theta_1}(p,q,\theta_1,\theta_2,c_3;0,0,m_3)\\\nonumber
&=\pi\sqrt{-1}(-1+(q-2)\theta_1)+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})    
\end{aligned}$$ and $$\begin{aligned}
&\hat{V}_{\theta_2}(p,q,\theta_1,\theta_2,c_3;0,0,m_3)\\\nonumber
&=-2\pi\sqrt{-1}+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}\theta_2})-\log(1-e^{2\pi\sqrt{-1}(\theta_2+c_2)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-c_2)}).    
\end{aligned}$$

Let $c_3=\frac{1}{2}+\tilde{c}_3$, we solve the critical point equations $$\begin{aligned}
\left\{ \begin{aligned}
         &\hat{V}_{\theta_1}(p,q,\theta_1,\theta_2,\frac{1}{2}+\tilde{c}_3;0,0,m_3)=0 \\
         &\hat{V}_{\theta_2}(p,q,\theta_1,\theta_2,\frac{1}{2}+\tilde{c}_3;0,0,m_3)=0
                          \end{aligned} \right.
\end{aligned}$$

As a function of $\gamma_2=\frac{1}{q},\tilde{c}_3$, the solutions $\theta_1,\theta_2$ of the above critical point equation have the following expansions $$\begin{aligned}
\theta_1&=\gamma_2-2(1+\sqrt{-1})\gamma_2^2+8\sqrt{-1}\gamma_2^3+(16-16\sqrt{-1}+\frac{2\sqrt{-1}}{3}\pi^2)\gamma_2^4+\cdots \\\nonumber
&+\left(-\sqrt{-1}\pi^2\gamma_2^2+(-4+4\sqrt{-1})\pi^2\gamma_2^3+(24\pi^2-\frac{\sqrt{-1}}{3}\pi^4)\gamma_2^4\right.\\\nonumber
&\left.+(-(64+64\sqrt{-1})\pi^2+\frac{8\sqrt{-1}}{3}\pi^4)\gamma_2^5+\cdots\right) \tilde{c}_3^2+\cdots
\end{aligned}$$ and $$\begin{aligned}
\theta_2&=\frac{\log(1-2\sqrt{-1})}{2\pi\sqrt{-1}}+1+(-\frac{2}{5}+\frac{\sqrt{-1}}{5})\pi\gamma_2^2+(\frac{12}{5}+\frac{4\sqrt{-1}}{5})\pi\gamma_2^3+\cdots\\\nonumber
&+\left((\frac{1}{10}+\frac{\sqrt{-1}}{5})+(-\frac{3}{25}+\frac{4\sqrt{-1}}{25})\pi^3\gamma_2^2+(\frac{38}{25}+\frac{16\sqrt{-1}}{25})\pi^3\gamma_2^3+\cdots\right)\tilde{c}_3^2+\cdots
\end{aligned}$$

Then we obtain $$\begin{aligned}
&2\pi \hat{V}(p,q,\theta_1,\theta_2,\frac{1}{2}+\tilde{c}_3;0,0,m_3)\\\nonumber
&=v_8+\frac{3\sqrt{-1}}{\gamma_2}\pi^2+2\pi^2\sqrt{-1}(-2m_3(\frac{1}{2}+\tilde{c}_2))-\sqrt{-1}\pi^2\gamma_2+(-2+2\sqrt{-1})\pi^2\gamma_2^2+8\pi^2\gamma_2^3+\cdots\\\nonumber
&+\left((-1-\sqrt{-1})\pi^2+4\sqrt{-1}p\pi^2-\pi^4\gamma_2^2+(4+4\sqrt{-1})\pi^4\gamma_2^3+\cdots \right)\tilde{c}_3^2+\cdots
\end{aligned}$$

In particular, when $c_3=\frac{1}{2}$, $$\begin{aligned}
 &2\pi \hat{V}(p,q,\theta_1(\gamma_2,\frac{1}{2}),\theta_2(\gamma_2,\frac{1}{2}),c_3=\frac{1}{2};0,0,m_3)\\\nonumber
 &=v_8+\frac{3\sqrt{-1}}{\gamma_2}\pi^2+2\pi^2\sqrt{-1}(-2m_3(\frac{1}{2}+\tilde{c}_3))-\sqrt{-1}\pi^2\gamma_2+(-2+2\sqrt{-1})\pi^2\gamma_2^2+8\pi^2\gamma_2^3+\cdots
\end{aligned}$$ and $$\begin{aligned}
&2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)\\\nonumber
&=2\pi \text{Re}\hat{V}(p,q,\theta_1,\theta_2,c_2=\frac{1}{2};0,0,m_3)\\\nonumber
&=v_8-2\pi^2\gamma_2^3+8\pi^2\gamma_2^3-(16\pi^2-\frac{1}{3}\pi^4)\gamma_2^4+\cdots
\end{aligned}$$

Therefore, we get $$\begin{aligned}
 &2\pi\text{Re}\hat{V}(p,q,\theta_1,\theta_2,c_3=\frac{1}{2}+\tilde{c}_3;0,0,m_3)\\\nonumber
 &=2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)+\left(-\pi^2-\pi^4\gamma_2^2+4\pi^4\gamma_2^3-\frac{1}{6}\pi^6\gamma_2^4+\frac{4}{3}\pi^6\gamma_2^5+\cdots \right)\tilde{c}_3^2+\cdots   
\end{aligned}$$

In principal, we have the following estimation

::: theorem
[]{#theorem-inprincipal2 label="theorem-inprincipal2"} $$\begin{aligned}
2\pi \text{Re}\hat{V}(p,q; \theta_1,\theta_2,c_3=\frac{1}{2}+\tilde{c}_3;0,0,m_3)<2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\pi^2 \tilde{c}_3^2.    
\end{aligned}$$
:::

From the formula $$\begin{aligned}
&2\pi \text{Re}\hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber &=Vol\left(S^3\setminus \mathcal{K}_p\right)-2\pi^2\gamma_2^2+8\pi^2\gamma_a^3-\frac{1}{4}\pi^4\gamma_1^2\gamma_2^2+\cdots,   
\end{aligned}$$ in principal, we can prove that

::: theorem
[]{#theorem-inprincipal3 label="theorem-inprincipal3"} $$\begin{aligned}
Vol\left(M_{p,q}\right)>Vol\left(S^3\setminus \mathcal{K}_p\right)-6\pi^2\gamma_2^2.    
\end{aligned}$$
:::

Fixing $\theta_1=c_1$, we have $$\begin{aligned}
&\hat{V}_{\theta_2}(p,q,c_1,\theta_2,\theta_3;m_1,0,0)\\\nonumber
&=-2\pi\sqrt{-1}+\log(1-e^{2\pi\sqrt{-1}(\theta_2-c_1)})+\log(1-e^{2\pi\sqrt{-1}\theta_2})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2+c_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}),   
\end{aligned}$$ and $$\begin{aligned}
&\hat{V}_{\theta_3}(p,q,c_1,\theta_2,\theta_3;m_1,0,0)\\\nonumber
&=\pi\sqrt{-1}(-(2p+3)+(4p+2)\theta_3)-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3}).   
\end{aligned}$$ Consider the critical point equations $$\begin{aligned}
 \left\{ \begin{aligned}
         & \hat{V}_{\theta_2}(p,q,c_1,\theta_2,\theta_3;m_1,0,0)&=0, \\
         &\hat{V}_{\theta_3}(p,q,c_1,\theta_2,\theta_3;m_1,0,0)&=0.
                          \end{aligned} \right.
\end{aligned}$$

As a function of $\gamma_1=\frac{1}{p},\tilde{c}_1$, the solutions $\theta_2,\theta_3$ of the above critical point equations have the following expansions $$\begin{aligned}
\theta_2&=\frac{\log(1-2\sqrt{-1})}{2\pi\sqrt{-1}}+1+\frac{1+2\sqrt{-1}}{40}\pi \gamma_1^2+\frac{3+\sqrt{-1}}{80}\pi\gamma_1^3+\cdots\\\nonumber
&+\left(\frac{-2+\sqrt{-1}}{5}\pi+\frac{-3+4\sqrt{-1}}{100}\pi^3\gamma_1^2+\frac{12+9\sqrt{-1}}{400}\pi^3\gamma_1^3+\cdots \right)\tilde{c}_1^2+\cdots
\end{aligned}$$ $$\begin{aligned}
 \theta_3&=\frac{1}{2}+\frac{1}{2}\gamma_1+\frac{1-\sqrt{-1}}{8}\gamma_1^2-\frac{\sqrt{-1}}{16}\gamma_1^3-(\frac{1+\sqrt{-1}}{64}+\frac{\sqrt{-1}}{192}\pi^2)\gamma_1^4+\cdots \\\nonumber
 &+\left(-\frac{\sqrt{-1}}{8}\pi^2\gamma_1^2-\frac{1+\sqrt{-1}}{16}\pi^2\gamma_1^3-(\frac{3}{64}\pi^2+\frac{5\sqrt{-1}}{192}\pi^4)\gamma_1^4+\cdots \right)\tilde{c}_1^2+\cdots
\end{aligned}$$

Then we have $$\begin{aligned}
  &2\pi \hat{V}(p,q,c_1=\tilde{c}_1,\theta_1,\theta_2;m_1,0,0)\\\nonumber
  &=v_8-\frac{\sqrt{-1}\pi^2}{\gamma_1}+3q\sqrt{-1}\pi^2-\sqrt{-1}\pi^2\gamma_1-\frac{1+\sqrt{-1}}{4}\pi^2\gamma_1^{2}-\frac{1}{8}\pi^2\gamma_1^3+\cdots \\\nonumber
  &-(1+2m_1)2\sqrt{-1}\pi^2\tilde{c}_1+\left((-2+(2+q)\sqrt{-1})\pi^2-\frac{1}{4}\pi^4\gamma_1^2+\frac{-1+\sqrt{-1}}{8}\pi^4\gamma_1^3+\cdots\right)\tilde{c}_1^2+\cdots
\end{aligned}$$

In particular, $c_1=\tilde{c}_1=0$, we have $$\begin{aligned}
&2\pi \hat{V}(p,q,c_1=\tilde{c}_1,\theta_1,\theta_2;m_1,0,0)\\\nonumber
&=v_8-\frac{\sqrt{-1}\pi^2}{\gamma_1}-\sqrt{-1}\pi^2\gamma_1-\frac{1+\sqrt{-1}}{4}\pi^2\gamma_1^2-\frac{1}{8}\pi^2\gamma_1^3+\cdots. 
\end{aligned}$$ It follows that $$\begin{aligned}
&2\pi\text{Re}\hat{V}(p,q,c_1=\tilde{c}_1,\theta_2,\theta_3;m_1,0,0)\\\nonumber
&=Vol(S^3\setminus \mathcal{K}_p)+(-2\pi^2-\frac{1}{4}\pi^4\gamma_1^2-\frac{1}{8}\pi^4\gamma_1^3-\frac{5}{192}\pi^6\gamma_1^4+\cdots)\tilde{c}_1^2+\\\nonumber
&+(\frac{1}{3}\pi^4-\frac{1}{24}\pi^6\gamma_1^2-\frac{1}{48}\pi^6\gamma_1^3+\cdots )\tilde{c}_1^4+\cdots. 
\end{aligned}$$

In principal, we have

::: theorem
[]{#theorem-inprincipal4 label="theorem-inprincipal4"} $$\begin{aligned}
2\pi \text{Re}\hat{V}(p,q; c_1,\theta_2,\theta_3;m_1,0,0)<Vol\left(S^3\setminus \mathcal{K}_p\right)-\frac{3}{2}\pi^2 c_1^2.    
\end{aligned}$$ for $c_1<\frac{1}{4}.$
:::
