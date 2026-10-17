---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-019-66-one-dimensional-saddle-point-method
section_title: "One-dimensional saddle point method"
section_number: 6.6
pages: 55-61
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.826
latex_coverage_ratio: 0.822
doc_brief: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST KNOT — This is the"
---
[]{#appendix-onedim label="appendix-onedim"} Consider the function, $$\begin{aligned}
 \hat{V}(\theta_1,\theta_2,\theta_3;m_1,m_2,m_3)=\hat{V}(\theta_1,\theta_2,\theta_3)-2\pi\sqrt{-1}m_1\theta_1-2\pi\sqrt{-1}m_2\theta_2-2\pi\sqrt{-1}m_3\theta_3.         
\end{aligned}$$

Let $\theta_1=c_1$, $\theta_3=c_3$ with $(c_1,c_3)\in [0,\frac{1}{4}]\times [\frac{1}{2},\frac{3}{4}]$ then $$\begin{aligned}
    &\hat{V}_{\theta_2}(c_1,\theta_2,c_3;m_1,m_2,m_3)\\\nonumber
    &=-2\pi\sqrt{-1}(m_2+1)-\log(1-e^{2\pi\sqrt{-1}(\theta_2-c_3)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2+c_3)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2+c_1)})+\log(1-e^{2\pi\sqrt{-1}\theta_2})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-c_1)}).    
\end{aligned}$$

From the critical point equation $$\begin{aligned}
 \label{equation-criticalequ-onedim0}
    V_{\theta_2}(c_1,\theta_2,c_3,m_1,m_2,m_3)=0,
\end{aligned}$$ we obtain $$\begin{aligned}
(1-xC_3)(1-\frac{x}{C_3})=(1-x)(1-xC_1)(1-\frac{x}{C_1}),   
\end{aligned}$$ where we set $C_1=e^{2\pi\sqrt{-1}c_1}$ and $C_3=e^{2\pi\sqrt{-1}c_3}$. Hence, we obtain $$\begin{aligned}
 \label{equation-criticalequ-onedim}
 x^2-(C_1+\frac{1}{C_1})x+(C_1+\frac{1}{C_1})-(C_3+\frac{1}{C_3})+1=0.   
\end{aligned}$$ It follows that $$\begin{aligned}
x=\cos(2\pi c_1)\pm 2\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}.    
\end{aligned}$$

We set $$\begin{aligned}
T_2(c_1,c_3)=\frac{\log(\cos(2\pi c_1)-2\sqrt{\sin^4(\pi c_1)- \sin^2(\pi c_3)})}{2\pi\sqrt{-1}}+1,   
\end{aligned}$$ then $$\begin{aligned}
 \label{equation-eT2}
    e^{2\pi\sqrt{-1}T_{2}(c_1,c_3)}=\cos(2\pi c_1)-  2\sqrt{\sin^4(\pi c_1)- \sin^2(\pi c_3)}
\end{aligned}$$ is a solution to the equation ([\[equation-criticalequ-onedim\]](#equation-criticalequ-onedim){reference-type="ref" reference="equation-criticalequ-onedim"}), moreover, $\theta_2(c_1,c_2)=T_2(c_1,c_3)$ is the unique solution to critical point equation ([\[equation-criticalequ-onedim0\]](#equation-criticalequ-onedim0){reference-type="ref" reference="equation-criticalequ-onedim0"}) with $\text{Re}(\theta_2(c_1,c_2))\in (\frac{1}{2},1)$.

From the equation ([\[equation-eT2\]](#equation-eT2){reference-type="ref" reference="equation-eT2"}), we obtain $$\begin{aligned}
    &e^{2\pi\sqrt{-1}T_2(c_1,c_3)}2\pi\sqrt{-1}\frac{dT_2(c_1,c_3)}{dc_1}\\\nonumber
    &=-2\pi\sin(2\pi c_1)-\frac{4\pi \sin^3(\pi c_3)\cos(\pi c_3)}{\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}}\\\nonumber
    &=-2\pi\sin(2\pi c_1)\left(1+\frac{\sin^2(\pi c_1)}{\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}}\right)
\end{aligned}$$ and $$\begin{aligned}
  e^{2\pi\sqrt{-1}T_2(c_1,c_3)}2\pi\sqrt{-1}\frac{dT_2(c_1,c_3)}{dc_3}=\frac{\pi\sin(2\pi c_3)}{\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}}.
\end{aligned}$$

Hence $$\begin{aligned}
    \frac{dT_2(c_1,c_3)}{dc_1}=\frac{2\sqrt{-1}\sin(\pi c_1)\left(\cos(\pi c_1)+\frac{\sin^2(\pi c_1)}{\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}}\right)}{\cos(2\pi c_1)-2\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}},
\end{aligned}$$ and $$\begin{aligned}
    \frac{dT_2(c_1,c_3)}{dc_3}=\frac{-\sqrt{-1}\sin(\pi c_3)\cos(\pi c_3)}{\cos(2\pi c_1)\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_2)}-2\sin^4(\pi c_3)+2\sin^2(\pi c_3)}.
\end{aligned}$$

It follows that $$\begin{aligned}
  \label{formula-dReVdc1}
\frac{d \text{Re}\hat{V}}{dc_1}&=\text{Re}\left(\frac{\partial \hat{V}}{\partial \theta_1}\frac{dc_1}{dc_1}+\frac{\partial \hat{V}}{\partial \theta_2}\frac{dT_2(c_1,c_3)}{dc_1}+\frac{\partial \hat{V}}{\partial \theta_3}\frac{dc_3}{dc_1} \right) \\\nonumber
&=\text{Re}\left(\frac{\partial \hat{V}}{\partial \theta_1}\right)\\\nonumber
&=\text{Re}(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)+c_1)}))-\text{Re}(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)-c_1)}))\\\nonumber
&=\log\left(\frac{2\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}-\sin(2\pi c_1)}{2\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}+\sin(2\pi c_1)}\right)
\end{aligned}$$ By the following Lemma [\[lemma-c1c3\]](#lemma-c1c3){reference-type="ref" reference="lemma-c1c3"}.

::: lemma
[]{#lemma-c1c3 label="lemma-c1c3"} For $(c_1,c_3)\in [0,\frac{1}{4}]\times [\frac{1}{2},\frac{3}{4}]$, we have $$\begin{aligned}
 \text{Re}\left(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)+c_1)})\right)=\log\left(2\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}-\sin(2\pi c_1)\right)    
 
\end{aligned}$$ and $$\begin{aligned}
 \text{Re}\left(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)-c_1)})\right)=\log\left(2\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}+\sin(2\pi c_1)\right)   
 
\end{aligned}$$
:::

::: proof
*Proof.* Since $\sin^4(\pi c_1)-\sin^2(\pi c_3)\leq 0$ by $(c_1,c_3)\in [0,\frac{1}{4}]\times [\frac{1}{2},\frac{3}{4}]$. By a straightforward computation, $$\begin{aligned}
&\text{Re}\left(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)+c_1)})\right) \\\nonumber
&=\text{Re}\left(\log\left(1-\left(\cos(2\pi c_1)-2\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}\right)e^{2\pi\sqrt{-1}c_1}\right)\right)\\\nonumber
&=\text{Re}\left(\log\left(1-\left(\cos(2\pi c_1)-2\sqrt{-1}\sqrt{\sin^2(\pi c_2)-\sin^4(\pi c_1)}\right)\left(\cos(2\pi c_1)+\sqrt{-1}\sin(2\pi c_1)\right)\right)\right)\\\nonumber
&=\text{Re}\left(\log\left(1-\cos^2(2\pi c_1)-2\sin(2\pi c_1)\sqrt{\sin^2(\pi c_2)-\sin^4(\pi c_2)}\right.\right. \\\nonumber
&\left.\left. -\sqrt{-1}\left(\sin(2\pi c_1)\cos(2\pi c_1)-2\cos(2\pi c_1)\sqrt{\sin^2(\pi c_2)-\sin^4(\pi c_2)}\right)\right)\right)\\\nonumber
&=\frac{1}{2}\log\left(\left(1-\cos^2(2\pi c_1)-2\sin(2\pi c_1)\sqrt{\sin^2(\pi c_2)-\sin^4(\pi c_2)}\right)^2\right. \\\nonumber
&\left. +\left(\sin(2\pi c_1)\cos(2\pi c_1)-2\cos(2\pi c_1)\sqrt{\sin^2(\pi c_2)-\sin^4(\pi c_2)}\right)^2\right)\\\nonumber
&=\frac{1}{2}\log\left(\sin^2(2\pi c_1)-4\sin(2\pi c_1)\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}+4(\sin^2(\pi c_3)-\sin^4(\pi c_1))\right)\\\nonumber
&=\log\left(2\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}-\sin(2\pi c_1)\right).
\end{aligned}$$

The second formula in Lemma [\[lemma-c1c3\]](#lemma-c1c3){reference-type="ref" reference="lemma-c1c3"} can be computed similarly. ◻
:::

$$\begin{aligned}
 \label{formula-dReVdc3}
\frac{d\text{Re}\hat{V}}{dc_3}&=\text{Re}\left(\frac{\partial \hat{V}}{\partial \theta_3}\right)\\\nonumber
&=\text{Re}\left(-\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)+c_3)})+\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)-c_3)})\right)\\\nonumber
&=\frac{1}{2}\log\left(\frac{\cos^2(\pi c_1)+\cos(\pi c_2)\sqrt{1-\frac{\sin^4(\pi c_1)}{\sin^2(\pi c_2)}}}{\cos^2(\pi c_1)-\cos(\pi c_2)\sqrt{1-\frac{\sin^4(\pi c_1)}{\sin^2(\pi c_2)}}}\right)
\end{aligned}$$ where in the last $=$ we have used the Lemma [\[lemma-c1c3-2\]](#lemma-c1c3-2){reference-type="ref" reference="lemma-c1c3-2"}.

::: lemma
[]{#lemma-c1c3-2 label="lemma-c1c3-2"} For $(c_1,c_3)\in [0,\frac{1}{4}]\times [\frac{1}{2},\frac{3}{4}]$, we have $$\begin{aligned}
 &\text{Re}\left(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)+c_3)})\right)\\\nonumber
 &=\frac{1}{2}\log\left(8\sin^2(\pi c_3)\cos^2(\pi c_1)-8\sin^2(\pi c_3)\cos(\pi c_3)\sqrt{1-\frac{\sin^4(\pi c_1)}{\sin^2(\pi c_2)}}\right)    
 
\end{aligned}$$ and $$\begin{aligned}
 &\text{Re}\left(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)-c_3)})\right)\\\nonumber
 &=\frac{1}{2}\log\left(8\sin^2(\pi c_3)\cos^2(\pi c_1)+8\sin^2(\pi c_3)\cos(\pi c_3)\sqrt{1-\frac{\sin^4(\pi c_1)}{\sin^2(\pi c_2)}}\right)    
 
\end{aligned}$$
:::

::: proof
*Proof.* Since $\sin^4(\pi c_1)-\sin^2(\pi c_3)\leq 0$ by $(c_1,c_3)\in [0,\frac{1}{4}]\times [\frac{1}{2},\frac{3}{4}]$, By a straightforward computation, $$\begin{aligned}
&\text{Re}\left(\log(1-e^{2\pi\sqrt{-1}(T_2(c_1,c_3)+c_3)})\right) \\\nonumber
&=\text{Re}\left(\log\left(1-\left(\cos(2\pi c_1)-2\sqrt{\sin^4(\pi c_1)-\sin^2(\pi c_3)}\right)e^{2\pi\sqrt{-1}c_3}\right)\right)\\\nonumber
&=\text{Re}\left(\log\left(1-\left(\cos(2\pi c_1)-2\sqrt{-1}\sqrt{\sin^2(\pi c_2)-\sin^4(\pi c_1)}\right)\left(\cos(2\pi c_3)+\sqrt{-1}\sin(2\pi c_3)\right)\right)\right)\\\nonumber
&=\text{Re}\left(\log\left(1-\cos(2\pi c_1)\cos(2\pi c_3)-2\sin(2\pi c_3)\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}\right.\right. \\\nonumber
&\left.\left. -\sqrt{-1}\left(\sin(2\pi c_3)\cos(2\pi c_1)-2\cos(2\pi c_3)\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}\right)\right)\right)\\\nonumber
&=\frac{1}{2}\log\left(\left(1-\cos(2\pi c_1)\cos(2\pi c_3)-2\sin(2\pi c_3)\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}\right)^2\right. \\\nonumber
&\left. +\left(\sin(2\pi c_3)\cos(2\pi c_1)-2\cos(2\pi c_3)\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}\right)^2\right)\\\nonumber
&=\frac{1}{2}\log\left(4(\cos(2\pi c_1)+1)\sin^2(\pi c_1)-4\sin(2\pi c_3)\sqrt{\sin^2(\pi c_3)-\sin^4(\pi c_1)}\right)\\\nonumber
&=\frac{1}{2}\log\left(8\sin^2(\pi c_3)\cos^2(\pi c_1)-8\sin^2(\pi c_3)\cos(\pi c_3)\sqrt{1-\frac{\sin^4(\pi c_1)}{\sin^2(\pi c_2)}}\right).
\end{aligned}$$ The formula ([\[lemma-c1c3-2\]](#lemma-c1c3-2){reference-type="ref" reference="lemma-c1c3-2"}) can be computed similarly. ◻
:::

::: proposition
[]{#prop-Rec1c3decrease label="prop-Rec1c3decrease"} $$\begin{aligned}
   \text{Re}\hat{V}(c_1,T_2(c_1,c_3),c_3)\leq   \text{Re}\hat{V}(c_1,T_2(c_1,c_{30}),c_{30})   
\end{aligned}$$ for $c_{30}\leq c_3$ $$\begin{aligned}
   \text{Re}\hat{V}(c_1,T_2(c_1,c_3),c_3)\leq   \text{Re}\hat{V}(c_{10},T_2(c_{10},c_{3}),c_{3})   
\end{aligned}$$ for $c_{10}\leq c_{1}$.
:::

::: proof
*Proof.* By formulas ([\[formula-dReVdc1\]](#formula-dReVdc1){reference-type="ref" reference="formula-dReVdc1"}) and ([\[formula-dReVdc3\]](#formula-dReVdc3){reference-type="ref" reference="formula-dReVdc3"}), we have $$\begin{aligned}
\frac{d\text{Re}\hat{V}}{dc_1}<0,  \ \text{and} \ \frac{d\text{Re}\hat{V}}{dc_3}<0.
\end{aligned}$$ ◻
:::

::: proposition
[]{#prop-hessian-onedim label="prop-hessian-onedim"} When $\theta_2$ satisfies the conditions, $\frac{1}{2}<\theta_2<1$, $0<c_1<\frac{1}{4}$, $\frac{1}{2}<c_3<\frac{3}{4}$ and $\theta_2+c_1<1$. then $$\begin{aligned}
f_{X_2X_2}>0.     
\end{aligned}$$
:::

::: proof
*Proof.* Recall that $$\begin{aligned}
f(\theta_1,X_1,\theta_2,X_2,\theta_3,X_3)=\text{Re} \hat{V},    
\end{aligned}$$ then $$\begin{aligned}
f_{X_2X_2}=-\text{Im}\left(\sqrt{-1}\hat{V}_{\theta_2\theta_2}\right)=2\pi (a+b+c+d+e)    
\end{aligned}$$ where $$\begin{aligned}
a&=-\text{Im}\frac{1}{1-z_2/z_1}=-\frac{\sin(2\pi(\theta_2-\theta_1))}{e^{2\pi(X_2-X_1)}+e^{-2\pi(X_2-X_1)}-2\cos(2\pi(\theta_2-\theta_1))} \\\nonumber
b&=-\text{Im}\frac{1}{1-z_2}=-\frac{\sin(2\pi \theta_2)}{e^{2\pi X_2}+e^{-2\pi X_2}-2\cos(2\pi \theta_2)}  \\\nonumber
c&=-\text{Im}\frac{1}{1-z_1z_2}=-\frac{\sin(2\pi( \theta_2+\theta_1))}{e^{2\pi (X_2+X_1)}+e^{-2\pi (X_2+X_1)}-2\cos(2\pi (\theta_2+\theta_1))} \\\nonumber
d&=\text{Im}\frac{1}{1-z_2z_3}=\frac{\sin(2\pi (\theta_2+\theta_3))}{e^{2\pi (X_2+X_3)}+e^{-2\pi (X_2+X_3)}-2\cos(2\pi (\theta_2+\theta_3))}\\\nonumber
e&=\text{Im}\frac{1}{1-z_2/z_3}=\frac{\sin(2\pi (\theta_2-\theta_3))}{e^{2\pi (X_2-X_3)}+e^{-2\pi (X_2-X_3)}-2\cos(2\pi (\theta_2-\theta_3))} 
\end{aligned}$$

we have $$\begin{aligned}
&(d+e)|_{\theta_3=c_3,X_3=0}\\\nonumber
&=\frac{\sin(2\pi(\theta_2+c_3))}{e^{2\pi X_2}-2\cos(2\pi(\theta_2+c_3))+e^{-2\pi X_2}}+\frac{\sin(2\pi(\theta_2-c_3))}{e^{2\pi X_2}-2\cos(2\pi(\theta_2-c_3))+e^{-2\pi X_2}}\\\nonumber
&=2\sin(2\pi \theta_2)\frac{\cos(2\pi c_3)(e^{2\pi X_2}+e^{-2\pi X_2})-2\cos(2\pi \theta_2)}{(e^{2\pi X}-2\cos(2\pi(\theta_2+c_3))+e^{-2\pi X_2})(e^{2\pi X}-2\cos(2\pi(\theta_2-c_3))+e^{-2\pi X_2})}
\end{aligned}$$

For $\frac{1}{2}<c_3<\theta_2<1$, we have $$\begin{aligned}
  \cos(2\pi c_3)(e^{2\pi X_2}+e^{-2\pi X_2})-2\cos(2\pi\theta_2)\leq 2\cos(2\pi c_3)-2\cos(2\pi \theta_2)<0  
\end{aligned}$$ and for $\frac{1}{2}<\theta_2<1$, $\sin(2\pi\theta_2)<0.$ so we have $(d+e)|_{\theta_3=c_3,X_3=0}>0$.

As to $a+c$, $$\begin{aligned}
    &(a+c)|_{\theta_1=c_1,X_1=0}\\\nonumber
    &=-\frac{\sin(2\pi(\theta_2-c_1))}{e^{2\pi X_2}-2\cos(2\pi(\theta_2-c_1))+e^{-2\pi X_2}}-\frac{\sin(2\pi(\theta_2+c_1))}{e^{2\pi X_2}-2\cos(2\pi(\theta_2+c_1))+e^{-2\pi X_2}}\\\nonumber
    &=-2\sin(2\pi \theta_2)\frac{\cos(2\pi c_1)(e^{2\pi X_2}+e^{-2\pi X_2})-2\cos(2\pi\theta_2)}{(e^{2\pi X_2}-2\cos(2\pi(\theta_2+c_1))+e^{-2\pi X_2})(e^{2\pi X_2}-2\cos(2\pi(\theta_2-c_1))+e^{-2\pi X_2})}
\end{aligned}$$

For $0\leq c_1\leq \frac{1}{4}$ and $\theta_2+c_1<1$, we have $$\begin{aligned}
 \cos(2\pi c_1)(e^{2\pi X_2}+e^{-2\pi X_2})-2\cos(2\pi \theta_2)\geq 2\cos(2\pi c_1)-2\cos(2\pi \theta_2)>0   
\end{aligned}$$ and $\sin(2\pi \theta_2)<0$ for $\frac{1}{2}<\theta_2<1$, so we have $(a+c)|_{\theta_1=c_1,X_1=0}>0$. Hence $$\begin{aligned}
 f_{X_2X_2}(c_1,0,\theta_2,X_2,c_3,0)>0   
\end{aligned}$$ when $\frac{1}{2}<\theta_2<1$, $0<c_1<\frac{1}{4}$, $\frac{1}{2}<c_3<\frac{3}{4}$ and $\theta_2+c_1<1$. ◻
:::

::: proposition
[]{#prop-finfty-onedim label="prop-finfty-onedim"} Given $(c_1,c_3)\in [0,\frac{1}{4}]\times [\frac{1}{2},\frac{3}{4}]$, for $\frac{1}{2}<\theta_2<1$, we have $$\begin{aligned}
f(c_1,0,\theta_2,X_2,c_3,0) \rightarrow  +\infty \ \text{as} \ X_2^2\rightarrow \infty.     
\end{aligned}$$
:::

::: proof
*Proof.* Based on Lemma [\[lemma-Li2\]](#lemma-Li2){reference-type="ref" reference="lemma-Li2"}, given $(c_1,c_3)\in [0,\frac{1}{4}]\times [\frac{1}{2},\frac{3}{4}]$, we introduce the following function for the $\theta_2\in (\frac{1}{2},1)$, $$\label{eq:2}
F(X_2)=\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2\geq 0) \\
         &\left(\theta_2+c_3-\frac{3}{2}\right)X_2 & \ (\text{if} \ X_2<0)
                          \end{aligned} \right.$$ $$+\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2\geq 0) \\
         &\left(\theta_2-c_3-\frac{1}{2}\right)X_2 & \ (\text{if} \ X_2<0)
                          \end{aligned} \right.$$ $$-\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2\geq 0) \\
         &\left(\theta_2-\frac{1}{2}\right)X_2 & \ (\text{if} \ X_2<0)
                          \end{aligned} \right.$$ $$-\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2\geq 0) \\
         &\left(\theta_2+c_1-\frac{1}{2}\right)X_2 & \ (\text{if} \ X_2<0)
                          \end{aligned} \right.$$ $$-\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2\geq 0) \\
         &\left(\theta_2-c_1-\frac{1}{2}\right)X_2 & \ (\text{if} \ X_2<0)
                          \end{aligned} \right.$$

$$+X_2$$ i.e. $$\label{eq:2}
F(X_2)=\left\{ \begin{aligned}
         &X_2  &  \ (\text{if} \ X_2\geq 0) \\
         &\left(\frac{1}{2}-\theta_2\right)X_2 & \ (\text{if} \ X_2<0)
                          \end{aligned} \right.$$

It follows that, when $X_2^2\rightarrow \infty$, $F(X_2)\rightarrow +\infty$. ◻
:::
