---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-018-65-two-dimensional-saddle-point-method
section_title: "Two-dimensional saddle point method"
section_number: 6.5
pages: 52-55
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 0.884
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
[]{#Appendix-twodimsaddle label="Appendix-twodimsaddle"}

We consider the potential function $$\begin{aligned}
&\hat{V}(p,q;\theta_1,\theta_2,\theta_3;m_1,m_2,m_3)\\\nonumber
&=\pi\sqrt{-1}\left(\frac{3q}{2}+\left(\frac{q}{2}-1\right)\theta_1^2-(2m_1+1)\theta_1-(2m_2+2)\theta_2+(2p+1)\theta_3^2-(2p+3+2m_3)\theta_3\right)\\\nonumber
&+\frac{1}{2\pi\sqrt{-1}}\left(\frac{\pi^2}{6}+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-
\theta_3)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})\right.\\\nonumber
&\left.-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right).
\end{aligned}$$

### The case $\theta_3=c_3$

Fixing $\theta_3=c_3$, then $$\begin{aligned}
\hat{V}_{\theta_1}=\pi\sqrt{-1}(-2m_1-1+q\theta_1-2\theta_1)+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})    
\end{aligned}$$ $$\begin{aligned}
\hat{V}_{\theta_2}&=-(2m_2+2)\pi\sqrt{-1}+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}\theta_2})-\log(1-e^{2\pi\sqrt{-1}(\theta_2+c_3)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-c_3)})    
\end{aligned}$$

Let $z_1=e^{2\pi\sqrt{-1}\theta_1}$, $z_2=e^{2\pi\sqrt{-1}t}$, $C_3=e^{2\pi\sqrt{-1}c_3}$, then from the critical point equations $$\begin{aligned}
\hat{V}_{\theta_1}=0, \ \hat{V}_{\theta_2}=0,    
\end{aligned}$$ we obtain $$\begin{aligned}
&z_2=\frac{z_1+z_1^{\frac{q}{2}}}{1+z_1^{\frac{q}{2}+1}}, \\
&z_2^2-(z_1+\frac{1}{z_1})z_2+z_1+\frac{1}{z_1}-C_3-\frac{1}{C_3}+1=0. 
\end{aligned}$$ It follows that $$\begin{aligned}
 \label{equation-z1}
&z_1^{q+4}-(C_3+C_3^{-1})z_1^{q+3}+z_1^{q+2}-z_1^{\frac{q}{2}+4}+2z_1^{\frac{q}{2}+3}\\\nonumber
&-2(C_3+C_3^{-1}-1)z_1^{\frac{q}{2}+2}+2z_1^{\frac{q}{2}+1}-z_1^{\frac{q}{2}}+z_1^2-(C_3+C_3^{-1})z_1+1=0.    
\end{aligned}$$

Suppose $z_1(q,c_3)$ is a solution of the equation ([\[equation-z1\]](#equation-z1){reference-type="ref" reference="equation-z1"}), set $$\begin{aligned}
\theta_1(q,c_3)=\frac{\log(z_1(q,C_3))}{2\pi\sqrt{-1}}+\mathbb{Z}, \\\nonumber
\theta_2(q,c_3)=\frac{\log(z_2(q,C_3))}{2\pi\sqrt{-1}}+\mathbb{Z}, 
\end{aligned}$$ then $(\theta_1(q,c_3),\theta_2(q,c_3))$ satisfies the critical point equations up to an argument.

Moreover, by using the method in [@CZ23-1], we can show that the critical point equations $$\begin{aligned}
    \left\{ \begin{aligned}
         & \hat{V}_{\theta_1}(\theta_1,\theta_2,c_3)=0,  &  \  \\
         &   \hat{V}_{\theta_2}(\theta_1,\theta_2,c_3)=0.
                          \end{aligned}\right.
\end{aligned}$$ has a unique solution denoted by $(\theta_1(c_3),\theta_3(c_3))$.

::: proposition
[]{#prop-twocritical label="prop-twocritical"} For $\frac{1}{2}+\frac{1}{8p}<c_3=\frac{1}{2}+\tilde{c}_3<\frac{3}{4}$, we have $$\begin{aligned}
2\pi \text{Re}\hat{V}(p,q;\theta_1(c_3),\theta_2(c_3),c_3)<2\pi\text{Re}\hat{V}(p,q;\theta_1^0,\theta_2^0,\theta_3^0)-\epsilon  
\end{aligned}$$ for some $\epsilon>0$.
:::

::: proof
*Proof.* For $\frac{1}{2}+\frac{1}{8p}<c_3=\frac{1}{2}+\tilde{c}_3<\frac{3}{4}$, by Theorems [\[theorem-inprincipal1\]](#theorem-inprincipal1){reference-type="ref" reference="theorem-inprincipal1"} and [\[theorem-inprincipal2\]](#theorem-inprincipal2){reference-type="ref" reference="theorem-inprincipal2"}, we have

$$\begin{aligned}
   &2\pi \text{Re}\hat{V}(p,q;\theta_1(q,c_3),\theta_2(q,c_3),c_3)\\\nonumber
   &\leq 2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\pi^2 \tilde{c}_3^2\\\nonumber
  &<2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\frac{49}{64}\pi^2\gamma_1^2\\\nonumber
  &<Vol\left(M_{p,q}\right)=2\pi \text{Re}\hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0).
\end{aligned}$$ ◻
:::

Let $\theta_3=c_3$ and $D_0(c_3)=\{\theta_3=c_3\}\cap D_0$, we need to estimate the following integral used in Theorem [\[theorem-m_1\]](#theorem-m_1){reference-type="ref" reference="theorem-m_1"},

$$\begin{aligned}
    \int_{D_0(c_3)}\sin(\pi \theta_1)\sin(2\pi c_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,c_3;0,0,m_3)}d\theta_1d\theta_2.
\end{aligned}$$

::: theorem
[]{#theorem-usedinm1 label="theorem-usedinm1"} For $\frac{1}{2}+\frac{1}{8p}<c_3=\frac{1}{2}+\tilde{c}_3<\frac{3}{4}$, we have $$\begin{aligned}
    \int_{D_0(c_3)}\sin(\pi \theta_1)\sin(2\pi c_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,c_3;0,0,m_3)}d\theta_1d\theta_2=O(e^{(N+\frac{1}{2})(\zeta_{\mathbb{R}}(p,q)-\epsilon)})
\end{aligned}$$ for $\epsilon>0$.
:::

::: proof
*Proof.* On the region $D_0(c_3)$, we can check the saddle point method condition for two-dimensional integral following the procedure in [@CZ23-1], we omit the details here. Then, together with Proposition [\[prop-twocritical\]](#prop-twocritical){reference-type="ref" reference="prop-twocritical"}, we prove the Theorem. ◻
:::

### The case $\theta_1=c_1$

In this case, let $\theta_1=c_1$ and $D_0(c_1)=\{\theta_1=c_1\}\cap D_0$, we need to estimate the following integral in Theorem [\[theorem-m3\]](#theorem-m3){reference-type="ref" reference="theorem-m3"},

$$\begin{aligned}
    \int_{D_0(c_1)}\sin(\pi c_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\hat{V}_N(c_1,\theta_2,\theta_3;0,0,m_3)}d\theta_2d\theta_3.
\end{aligned}$$

Similarly to previous subsection, we have

::: theorem
[]{#theorem-usedinm3 label="theorem-usedinm3"} For $\frac{2}{q}<c_1<\frac{1}{4}$, we have $$\begin{aligned}
     \int_{D_0(c_1)}\sin(\pi c_1)\sin(2\pi \theta_3)e^{(N+\frac{1}{2})\hat{V}_N(c_1,\theta_2,\theta_3;0,0,m_3)}d\theta_2d\theta_3=O(e^{(N+\frac{1}{2})(\zeta_{\mathbb{R}}(p,q)-\epsilon)})
\end{aligned}$$ for $\epsilon>0$.
:::

::: lemma
[]{#Lemma-inequ label="Lemma-inequ"} When $c_3=\frac{1}{2}+\tilde{c}_3\geq \frac{1}{2}+\frac{7}{8p}$, we have $$\begin{aligned}
   &2\pi\text{Re}\hat{V}(p,q;m_1,0,m_3,c_1,T_2(c_1,\frac{1}{2}+\tilde{c}_3),\frac{1}{2}+\tilde{c}_3)\\\nonumber
   &<2\pi \text{Re}\hat{V}(p,q,m_1,0,0,c_1,\theta_2(c_1),\theta_3(c_1)).    
  
\end{aligned}$$
:::

::: proof
*Proof.* First, we have the estimates, $$\begin{aligned}
&2\pi \text{Re}\hat{V}(p,q,m_1,0,m_3,c_1,T_2(c_1,\frac{1}{2}+\tilde{c}_3),\frac{1}{2}+c_3)\\\nonumber
&=v_8-2\pi^2c_1^2-\pi^2\tilde{c}_3^2+\frac{1}{3}\pi^{4}c_{1}^{4}-\pi
^{4}c_{1}^{2}\tilde{c}_{3}^{2}-\frac{1}{12}\pi^{4}\tilde{c}_{3}^{4}+...\\\nonumber
&=v_{8}-2\pi^{2}c_{1}^{2}+\frac{1}{3}\pi^{4}c_{1}^{4}+...\\\nonumber
&-\pi^{2}\tilde{c}_{3}^{2}-\pi^{4}c_{1}^{2}\tilde{c}_{3}^{2}-\frac{1}{12}\pi^{4}\tilde{c}_{3}^{4}+...\\\nonumber
&=2\pi\text{Re}\hat{V}(p,q,m_1,0,m_3,c_{1},T_{2}(c_{1}
,\frac{1}{2}),\frac{1}{2})-\pi^{2}\tilde{c}_{3}^{2}-\pi^{4}c_{1}^{2}\tilde{c}_{3}
^{2}-\frac{1}{12}\pi^{4}\tilde{c}_{3}^{4}+...
\end{aligned}$$ On the other hand, $$\begin{aligned}
 \label{formula-inprincipal}
 &2\pi\text{Re}\hat{V}(p,q,m_{1},0,0,c_{1},\theta_2(\gamma_{1}
,c_{1}),\theta_3(\gamma_{1},c_{1})) \\\nonumber
&=v_{8}-\frac{1}{4}\pi^{2}\gamma_{1}^{2}-\frac{1}{8}\pi^{2}\gamma_{1}
^{3}-(\frac{1}{32}\pi^{2}+\frac{1}{192}\pi^{4})\gamma_{1}^{4}+\\\nonumber &+(-2\pi^{2}-\frac{1}{4}\pi^{4}\gamma_{1}^{2}-\frac{1}{8}\pi^{4}\gamma_{1}
^{3}-\frac{5}{192}\pi^{6}\gamma_{1}^{4}+...)c_{1}^{2}\\\nonumber&+(\frac{1}{3}\pi
^{4}-\frac{1}{24}\pi^{6}\gamma_{1}^{2}-\frac{1}{48}\pi^{6}\gamma_{1}
^{3}+(\frac{3}{64}\pi^{6}-\frac{23}{1152}\pi^{8})\gamma_{1}^{4}+...)c_{1}
^{4}+...\\\nonumber
&=v_{8}-2\pi^{2}c_{1}^{2}+\frac{1}{3}\pi^{4}c_{1}^{4}+...\\\nonumber
&-\frac{1}{4}\pi^{2}\gamma_{1}^{2}-\frac{1}{8}\pi^{2}\gamma_{1}^{3}-(\frac
{1}{32}\pi^{2}+\frac{1}{192}\pi^{4})\gamma_{1}^{4}+(-\frac{1}{4}\pi^{4}\gamma_{1}^{2}-\frac{1}{8}\pi^{4}\gamma_{1}^{3}-\frac
{5}{192}\pi^{6}\gamma_{1}^{4}+...)c_{1}^{2}\\\nonumber
&+(-\frac{1}{24}\pi^{6}\gamma
_{1}^{2}-\frac{1}{48}\pi^{6}\gamma_{1}^{3}+(\frac{3}{64}\pi^{6}-\frac
{23}{1152}\pi^{8})\gamma_{1}^{4}+...)c_{1}^{4}+...\\\nonumber
&=2\pi\text{Re}\hat{V}(\infty,q,m_{1},0,0,c_{1},\theta_2(\gamma
_{1}=0,c_{1}),\theta_3(\gamma_{1}=0,c_{1}))-\frac{1}{4}\pi^{2}\gamma_{1}^{2}-\frac
{1}{8}\pi^{2}\gamma_{1}^{3}-(\frac{1}{32}\pi^{2}+\frac{1}{192}\pi^{4}
)\gamma_{1}^{4}\\\nonumber &+(-\frac{1}{4}\pi^{4}\gamma_{1}^{2}-\frac{1}{8}\pi^{4}\gamma_{1}^{3}-\frac
{5}{192}\pi^{6}\gamma_{1}^{4}+...)c_{1}^{2}+(-\frac{1}{24}\pi^{6}\gamma
_{1}^{2}-\frac{1}{48}\pi^{6}\gamma_{1}^{3}+(\frac{3}{64}\pi^{6}-\frac
{23}{1152}\pi^{8})\gamma_{1}^{4}+...)c_{1}^{4}+...\\\nonumber
&=2\pi\operatorname{Re}\widehat{V}(p,q,m_{1},0,m_3,c_{1},T_{2}(c_{1}
,\frac{1}{2}),\frac{1}{2})-\frac{1}{4}\pi^{2}\gamma_{1}^{2}-\frac{1}{8}
\pi^{2}\gamma_{1}^{3}-(\frac{1}{32}\pi^{2}+\frac{1}{192}\pi^{4})\gamma_{1}
^{4}\\\nonumber
&+(-\frac{1}{4}\pi^{4}\gamma_{1}^{2}-\frac{1}{8}\pi^{4}\gamma_{1}^{3}-\frac
{5}{192}\pi^{6}\gamma_{1}^{4}+...)c_{1}^{2}+(-\frac{1}{24}\pi^{6}\gamma
_{1}^{2}-\frac{1}{48}\pi^{6}\gamma_{1}^{3}+(\frac{3}{64}\pi^{6}-\frac
{23}{1152}\pi^{8})\gamma_{1}^{4}+...)c_{1}^{4}+...
\end{aligned}$$ Thus finally we have $$\begin{aligned}
    &2\pi \text{Re}\hat{V}(p,q,m_1,0,m_3,c_1,T_2(c_1,\frac{1}{2}+\tilde{c}_3),\frac{1}{2}+c_3)\\\nonumber
    &=2\pi\text{Re}\hat{V}(p,q,m_{1},0,m_3,c_{1},T_{2}(c_{1}
,\frac{1}{2}),\frac{1}{2})-\pi^{2}\tilde{c}_{3}^{2}-\pi^{4}c_{1}^{2}\tilde{c}_{3}
^{2}-\frac{1}{12}\pi^{4}\tilde{c}_{3}^{4}+...\\\nonumber
&<2\pi\text{Re}\hat{V}(p,q,m_{1},0,m_3,c_{1},T_{2}(c_{1}
,\frac{1}{2}),\frac{1}{2})-\pi^{2}\tilde{c}_{3}^{2}\\\nonumber
&<2\pi\text{Re}
\hat{V}(p,q,m_{1},0,m_3,c_{1},T_{2}(c_{1},\frac{1}{2}),\frac{1}
{2})-\frac{49}{64}\pi^{2}\gamma_{1}^{2}.
\end{aligned}$$ In principal, by formula ([\[formula-inprincipal\]](#formula-inprincipal){reference-type="ref" reference="formula-inprincipal"}), we can prove the Lemma. ◻
:::
