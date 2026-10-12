---
doc_id: arxiv-2410.14661v1
doc_title: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eigh"
section_id: sec-009-51-preparations
section_title: "Preparations"
section_number: 5.1
pages: 20-41
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
doc_brief: "On the asymptotic expansion of various quantum invariants III: the Reshetikhin-Turaev invariants of closed hyperbolic 3-manifolds obtained by integral surgery along the figure-eight knot — This is"
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 0.903
---
Recall the functions $$\begin{aligned}
 \label{formula-PotentialV}
   &\hat{V}_N(\theta_1,\theta_2,\theta_3)\\\nonumber
   &=\pi\sqrt{-1}\left(\left(\frac{q}{2}-1\right)\theta_1^2-\theta_1+(2p+1)\theta_3^2-(2p+3)\theta_3-2\theta_2+\frac{3}{2}q-\frac{1}{12}\right.\\\nonumber
   &\left.+\frac{2\theta_2}{N+\frac{1}{2}}+\frac{p-2q+\frac{7}{4}}{N+\frac{1}{2}}-\frac{3(p+q)+2}{6(N+\frac{1}{2})^2}\right)\\\nonumber
    &+\frac{1}{N+\frac{1}{2}}\left(\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})\right.\\\nonumber
    &\left.-\varphi_N(\theta_2+\theta_1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)\right)
\end{aligned}$$ and $$\begin{aligned}
\hat{V}(\theta_1,\theta_2,\theta_3)&=\pi\sqrt{-1}\left(\frac{3q}{2}+(\frac{q}{2}-1)\theta_1^2-\theta_1+(2p+1)\theta_3^2-(2p+3)\theta_3-2\theta_2\right)\\\nonumber
&+\frac{1}{2\pi\sqrt{-1}}\left(\frac{\pi^2}{6}+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}))\right.\\\nonumber
&\left.-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right).
\end{aligned}$$

::: proposition
[]{#prop-VNexpansion label="prop-VNexpansion"} For any $L>0$, in the region $$\begin{aligned}
\{(\theta_1,\theta_2,\theta_3)\in \mathbb{C}^3|(\text{Re}(\theta_1),\text{Re}(\theta_2),\text{Re}(\theta_3))\in D_{0}, |\text{Im}(\theta_1)|<L, |\text{Im} \theta_2|<L, |\text{Im} \theta_3|<L\},    
\end{aligned}$$ we have $$\begin{aligned}
 \label{formula-VNexpansion}
    &\hat{V}_{N}(\theta_1,\theta_2,\theta_3)=\hat{V}(\theta_1,\theta_2,\theta_3)+\frac{1}{N+\frac{1}{2}}\left(\pi\sqrt{-1}\left(2\theta_2+(p-2q+\frac{7}{4})\right)\right.\\\nonumber
    &\left.-\frac{1}{2}\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})-\frac{1}{2}\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})\right)+\frac{1}{(N+\frac{1}{2})^2}w_{N}(\theta_1,\theta_2,\theta_3),
\end{aligned}$$ with $|w_{N}(\theta_1,\theta_2,\theta_3)|$ bounded from above by a constant independent of $N$.
:::

::: proof
*Proof.* By using Taylor expansion, together with Lemma [\[lemma-varphixi2\]](#lemma-varphixi2){reference-type="ref" reference="lemma-varphixi2"}, we have

$$\begin{aligned}
    &\varphi_N\left(\theta_2+\theta_3-1+\frac{1}{N+\frac{1}{2}}\right)\\\nonumber
    &=\varphi_N(\theta_2+\theta_3-1)+\varphi'_N(\theta_2+\theta_3-1)\frac{1}{N+\frac{1}{2}}\\\nonumber&+\frac{\varphi''_{N}(\theta_2+\theta_3-1)}{2}\frac{1}{(N+\frac{1}{2})^2}+O\left(\frac{1}{(N+\frac{1}{2})^2}\right)\\\nonumber
    &=\frac{N+\frac{1}{2}}{2\pi\sqrt{-1}}\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})-\frac{\pi\sqrt{-1}}{6(2N+1)}\frac{e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}\\\nonumber
    &-\frac{1}{2}\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\frac{\pi\sqrt{-1}}{2(2N+1)}\frac{e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}+O\left(\frac{1}{(N+\frac{1}{2})^2}\right). 
    
\end{aligned}$$ Expanding $\varphi_N\left(\theta_2-\theta_3+\frac{1}{N+\frac{1}{2}}\right)$, $\varphi_N(\theta_2+\theta_1)$, $\varphi_N(\theta_2)$ and $\varphi_N(\theta_2-\theta_1)$ similarly, we obtain $$\begin{aligned}
    &\frac{1}{N+\frac{1}{2}}\left(\varphi_N(\theta_2+\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}}-1)+\varphi_{N}(\theta_2-\theta_3+\frac{\frac{1}{2}}{N+\frac{1}{2}})\right.\\\nonumber
    &\left.-\varphi_N(\theta_2+\theta_1)-\varphi_N(\theta_2)-\varphi_N(\theta_2-\theta_1)\right)\\\nonumber
    &=\frac{1}{2\pi\sqrt{-1}}\left(\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})\right.\\\nonumber
&\left.-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right)-\frac{1}{2}\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})\\\nonumber
&-\frac{1}{2}\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})+w'_{N}(\theta_1,\theta_2,\theta_3),
\end{aligned}$$ where $$\begin{aligned}
    &w'_{N}(\theta_1,\theta_2,\theta_3)\\\nonumber
    &=\frac{\pi\sqrt{-1}}{12}\left(2\frac{e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}+2\frac{e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}+\frac{e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}\right.\\\nonumber
    &\left.+\frac{e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}+\frac{e^{2\pi\sqrt{-1}\theta_2}}{1-e^{2\pi\sqrt{-1}\theta_2}}+O\left(\frac{1}{N+\frac{1}{2}}\right)\right).
\end{aligned}$$ Let $$\begin{aligned}
   w_{N}(\theta_1,\theta_2,\theta_3)=  w'_{N}(\theta_1,\theta_2,\theta_3)-\frac{3(p+q)+2}{6},
\end{aligned}$$ then we obtain the formula ([\[formula-VNexpansion\]](#formula-VNexpansion){reference-type="ref" reference="formula-VNexpansion"}). ◻
:::

We consider the critical point of $\hat{V}(\theta_1,\theta_2,\theta_3)$ which is given by the solution of the following equations

$$\begin{aligned}
 \label{equation-critical1}
\hat{V}_{\theta_1}=\pi\sqrt{-1}((q-2)\theta_1+1)+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})=0,   
\end{aligned}$$ $$\begin{aligned}
 \label{equation-critical2}
\hat{V}_{\theta_2}&=-2\pi\sqrt{-1}-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})+\log(1-e^{2\pi\sqrt{-1}\theta_2})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})=0,    
\end{aligned}$$ $$\begin{aligned}
 \label{equation-critical3}
\hat{V}_{\theta_3}&=\pi\sqrt{-1}((4p+2)\theta_3-(2p+3))-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})=0.    
\end{aligned}$$

::: proposition
[]{#prop-critical label="prop-critical"} The critical point equations ([\[equation-critical1\]](#equation-critical1){reference-type="ref" reference="equation-critical1"}), ([\[equation-critical2\]](#equation-critical2){reference-type="ref" reference="equation-critical2"}) and ([\[equation-critical3\]](#equation-critical3){reference-type="ref" reference="equation-critical3"}) has a unique solution $(\theta_1^0,\theta_2^0,\theta_3^0)$ in the region $D_{0\mathbb{C}}=\{(\theta_1,\theta_2,\theta_3)\in \mathbb{C}^3| (\text{Re}(\theta_1),\text{Re}(\theta_2),\text{Re}(\theta_3))\in D_0\}$.
:::

::: proof
*Proof.* See Appendix [\[Appendix-criticalexists\]](#Appendix-criticalexists){reference-type="ref" reference="Appendix-criticalexists"} for a proof. ◻
:::

Now we set $\zeta(p,q)$ to be the critical value of the potential function $\hat{V}(p,q;\theta_1,\theta_2,\theta_3)$, i.e. $$\begin{aligned}
    \zeta(p,q)=V(p,q,\theta_1^0,\theta_2^0,\theta_3^0),
\end{aligned}$$ and set $$\begin{aligned}
 \label{formula-zetaR(p)}
    \zeta_\mathbb{R}(p,q)=\text{Re} \zeta(p,q)=\text{Re} \hat{V}(p,q,\theta_1^0,\theta_2^0,\theta_3^0). 
\end{aligned}$$

::: lemma
[]{#lemma-volumeestimate label="lemma-volumeestimate"} When $(p,q)\in S$, we have the following estimation for $\zeta_{\mathbb{R}}(p,q)$ $$\begin{aligned}
    2\pi \zeta_{\mathbb{R}}(p,q)\geq 3.56337.
\end{aligned}$$
:::

::: proof
*Proof.* See Appendix [\[Appendix-geometry\]](#Appendix-geometry){reference-type="ref" reference="Appendix-geometry"} for a proof. ◻
:::

Set $z_1=e^{2\pi\sqrt{-1}\theta_1}, z_2=e^{2\pi\sqrt{-1}\theta_2}$, and $z_3=e^{2\pi\sqrt{-1}\theta_3}$, by straightforward computations, we have

$$\begin{aligned}
    \hat{V}_{\theta_1\theta_1}&=(q-2)\pi\sqrt{-1}-\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}-\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2-\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)}}\\\nonumber
    &=2\pi\sqrt{-1}\left(\frac{q}{2}-1-\frac{1}{z_1/z_2-1}-\frac{1}{1/(z_1z_2)-1}\right)
\end{aligned}$$ $$\begin{aligned}
    \hat{V}_{\theta_1\theta_2}&=-\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}+\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2-\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)}}\\\nonumber
    &=2\pi\sqrt{-1}\left(\frac{1}{z_1/z_2-1}-\frac{1}{1/(z_1z_2)-1}\right),
\end{aligned}$$ $$\begin{aligned}
    \hat{V}_{\theta_1\theta_3}=0.
\end{aligned}$$

$$\begin{aligned}
    \hat{V}_{\theta_2\theta_2}&=\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}+\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}-\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}}\\\nonumber
    &-\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}\theta_2}}{1-e^{2\pi\sqrt{-1}\theta_2}}-\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2-\theta_1)}}{1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)}}\\\nonumber
    &=2\pi\sqrt{-1}\left(-\frac{1}{z_1/z_2-1}-\frac{1}{1/z_2-1}-\frac{1}{1/(z_1z_2)-1}\right.\\\nonumber
    &\left.+\frac{1}{1/(z_2z_3)-1}+\frac{1}{z_3/z_2-1}\right).
\end{aligned}$$ $$\begin{aligned}
    \hat{V}_{\theta_2\theta_3}&=\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}-\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}\\\nonumber
    &=2\pi\sqrt{-1}\left(\frac{1}{1/(z_2z_3)-1}-\frac{1}{z_3/z_2-1}\right).
\end{aligned}$$

$$\begin{aligned}
    \hat{V}_{\theta_3\theta_3}&=\pi\sqrt{-1}(4p+2)+\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)}}+\frac{2\pi\sqrt{-1}e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}{1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}}\\\nonumber
    &=2\pi\sqrt{-1}\left((2p+1)+\frac{1}{1/(z_2z_3)-1}+\frac{1}{z_3/z_2-1}\right).
\end{aligned}$$

We let $$\begin{aligned}
 \hat{f}(\theta_1,X_1,\theta_2,X_2,\theta_3,X_3)=\text{Re}\hat{V}(p,q,\theta_1+\sqrt{-1}X_1,\theta_2+\sqrt{-1}X_2,\theta_3+\sqrt{-1}X_3),  
\end{aligned}$$ then for $i\in \{1,2,3\}$, $$\begin{aligned}
\hat{f}_{X_i}&=\text{Re}(\sqrt{-1}\hat{V}(p,q,\theta_1+\sqrt{-1}X_1,\theta_2+\sqrt{-1}X_i,\theta_3+\sqrt{-1}X_3)\\\nonumber
&=-\text{Im}\hat{V}_{\theta_i}(p,q,\theta_1+\sqrt{-1}X_1,\theta_2+\sqrt{-1}X_2,\theta_3+\sqrt{-1}X_3)
\end{aligned}$$ and $$\begin{aligned}
\hat{f}_{X_iX_i}=-\text{Im}\left(\sqrt{-1}\hat{V}_{\theta_i\theta_i}(p,q,\theta_1+\sqrt{-1}X,\theta_2+\sqrt{-1}X_2,\theta_3+\sqrt{-1}X_3)\right).    
\end{aligned}$$

Hence the Hessian matrix of $\hat{f}$ is given by $$\begin{aligned}
   Hess(\hat{f})&=\begin{pmatrix}
     \hat{f}_{X_1X_1} & \hat{f}_{X_1X_2} & \hat{f}_{X_1X_3} \\
     \hat{f}_{X_2X_1} & \hat{f}_{X_2X_2} & \hat{f}_{X_2X_3} \\ 
     \hat{f}_{X_3X_1} & \hat{f}_{X_2X_2} & \hat{f}_{X_3X_3}
    \end{pmatrix}\\\nonumber
    &=2\pi \text{Im}\begin{pmatrix}
   a+c   & -a+c & 0 \\
     -a+c & a+b+c+d+e & d-e \\ 
     0 & d-e & d+e
    \end{pmatrix}
\end{aligned}$$ where $$\begin{aligned}
a&=-\text{Im}\frac{1}{1-z_2/z_1}=-\frac{\sin(2\pi(\theta_2-\theta_1))}{e^{2\pi(X_2-X_1)}+e^{-2\pi(X_2-X_1)}-2\cos(2\pi(\theta_2-\theta_1))} \\\nonumber
b&=-\text{Im}\frac{1}{1-z_2}=-\frac{\sin(2\pi \theta_2)}{e^{2\pi X_2}+e^{-2\pi X_2}-2\cos(2\pi \theta_2)}  \\\nonumber
c&=-\text{Im}\frac{1}{1-z_1z_2}=-\frac{\sin(2\pi( \theta_2+\theta_1))}{e^{2\pi (X_2+X_1)}+e^{-2\pi (X_2+X_1)}-2\cos(2\pi (\theta_2+\theta_1))} \\\nonumber
d&=\text{Im}\frac{1}{1-z_2z_3}=\frac{\sin(2\pi (\theta_2+\theta_3))}{e^{2\pi (X_2+X_3)}+e^{-2\pi (X_2+X_3)}-2\cos(2\pi (\theta_2+\theta_3))}\\\nonumber
e&=\text{Im}\frac{1}{1-z_2/z_3}=\frac{\sin(2\pi (\theta_2-\theta_3))}{e^{2\pi (X_2-X_3)}+e^{-2\pi (X_2-X_3)}-2\cos(2\pi (\theta_2-\theta_3))}.  
\end{aligned}$$

Obviously, when $\frac{1}{2}<\theta_2-\theta_1,\theta_2,\theta_2+\theta_1<1$, $1<\theta_2+\theta_3<\frac{3}{2}$ and $0<\theta_2-\theta_3<\frac{1}{2}$, we have that $a,b,c,d,e>0$.

Set $$\begin{aligned}
    D_{H}=\{(\theta_1,\theta_2,\theta_3)\in D_0| \frac{1}{2}<\theta_2\pm \theta_1,\theta_2<1, 1<\theta_2+\theta_3<\frac{3}{2}, 0<\theta_2-\theta_3<\frac{1}{2}\}.
\end{aligned}$$ We obtain

::: proposition
[]{#proposition-Hessianf label="proposition-Hessianf"} For $(\theta_1,\theta_2,\theta_3)\in D_{H}$, the Hessian matrix $$\begin{aligned}
    Hess(\hat{f})
\end{aligned}$$ is positive definite.
:::

::: proof
*Proof.* Since $$\begin{aligned}
&    \begin{vmatrix}
   a+c   & -a+c & 0 \\
     -a+c & a+b+c+d+e & d-e \\ 
     0 & d-e & d+e
\end{vmatrix}\\\nonumber
&=abd+abe+4acd+4ace+4ade+cbd+cbe+4cde>0,
\end{aligned}$$ $$\begin{aligned}
&    \begin{vmatrix}
   a+c   & -a+c \\
     -a+c & a+b+c+d+e 
\end{vmatrix}\\\nonumber
&=ab+4ac+ad+ae+cb+cd+ce>0
\end{aligned}$$ and $a+c>0$ by $a,b,c,d,e>0$ when $(\theta_1,\theta_2,\theta_3)\in D_{H}$. ◻
:::

## The case $m_2\neq 0$

We say that a Fourier coefficient $\hat{h}_{N}(m_1,m_2,m_3)$ can be neglected if exists some $\epsilon>0$, such that $$\begin{aligned}
    \hat{h}_{N}(m_1,m_2,m_3)=O(e^{(N+\frac{1}{2})(\zeta_{\mathbb{R}}(p,q)-\epsilon)}). 
\end{aligned}$$

We introduce $$\begin{aligned}
&\hat{V}(\theta_1,\theta_2,\theta_3,m_1,m_2,m_3)=\hat{V}(\theta_1,\theta_2,\theta_3)-2\pi\sqrt{-1}\sum_{i=1}^3m_i\theta_i\\\nonumber
&=\pi\sqrt{-1}\left(\frac{3q}{2}+\left(\frac{q}{2}-1\right)\theta_1^2-(2m_1+1)\theta_1+2(m_2+1)\theta_2+(2p+1)\theta_3^2-(2p+3+2m_3)\theta_3\right)\\\nonumber
&+\frac{1}{2\pi\sqrt{-1}}\left(\frac{\pi^2}{6}+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})\right.\\\nonumber
&\left.-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right).
\end{aligned}$$

First, when $m_2=-1$, it is easy to see that $$\begin{aligned}
 \label{formula-ReV-1}
&\lim_{X_2\rightarrow +\infty}\text{Re}\hat{V}
(\theta_1+\sqrt{-1}X_1,\theta_2+\sqrt{-1}X_2,\theta_3+\sqrt{-1}X_3;m_1,m_2,m_3)|_{X_3=X_1=0}\\\nonumber
&=\lim_{X_2\rightarrow +\infty}\text{Re}\left(\frac{1}{2\pi\sqrt{-1}}\left(\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3+\sqrt{-1}X_2)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3+\sqrt{-1}X_2)})\right.\right.\\\nonumber &\left.\left.
-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1+\sqrt{-1}X_2)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\sqrt{-1}X_2)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1+\sqrt{-1}X_2)})\right)\right)\\\nonumber
&=0.
\end{aligned}$$

It follows that the term $\hat{h}_{N}(m_1,-1,m_3)$ can be neglected for any $m_1,m_3\in \mathbb{Z}$.

Next, we consider the case $m_2\neq-1$. Motivated by Lemma [\[lemma-Li2\]](#lemma-Li2){reference-type="ref" reference="lemma-Li2"}, for $(\theta_1,\theta_2,\theta_3)\in D_{0}$, we introduce the following function $$\label{eq:2}
F(X_1,X_2,X_3;m_1,m_2,m_3)=\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2+X_3\geq 0) \\
         &\left(\theta_2+\theta_3-\frac{3}{2}\right)(X_2+X_3) & \ (\text{if} \ X_2+X_3<0)
                          \end{aligned} \right.$$ $$+\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2-X_3\geq 0) \\
         &\left(\theta_2-\theta_3-\frac{1}{2}\right)(X_2-X_3) & \ (\text{if} \ X_2-X_3<0)
                          \end{aligned} \right.$$ $$-\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2\geq 0) \\
         &\left(\theta_2-\frac{1}{2}\right)X_2 & \ (\text{if} \ X_2<0)
                          \end{aligned} \right.$$ $$-\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2+X_1\geq 0) \\
         &\left(\theta_2+\theta_1-\frac{1}{2}\right)(X_2+X_1) & \ (\text{if} \ X_2+X_1<0)
                          \end{aligned} \right.$$ $$-\left\{ \begin{aligned}
         &0  &  \ (\text{if} \ X_2-X_1\geq 0) \\
         &\left(\theta_2-\theta_1-\frac{1}{2}\right)(X_2-X_1) & \ (\text{if} \ X_2-X_1<0)
                          \end{aligned} \right.$$

$$+\left(-\left(\frac{q}{2}-1\right)\theta_1+m_1+\frac{1}{2}\right)X_1+(m_2+1)X_2+\left(p+\frac{3}{2}+m_3-(2p+1)\theta_3\right)X_3$$ where we use $\theta_2+\theta_3-\frac{3}{2}$ instead of $\theta_2+\theta_3-\frac{1}{2}$ in the first summation since in our situation $1< \theta_2+\theta_3<2$.

The following simple observation is useful.

::: lemma
[]{#lemma-X1X2X3 label="lemma-X1X2X3"} Given a linear function on $F(X_1,X_2,X_3)=AX_1+BX_2+CX_3$ over $\mathbb{R}^3$ with $X_1\geq X_2\geq X_3\geq 0$, we have

\(1\) If $A<0$ or $A+B<0$ or $A+B+C<0$, then we can find a direction with $X_1^2+X_2^2+X_3^2\rightarrow \infty$, such that $F(X_1,X_2,X_3)\rightarrow -\infty$;

\(2\) If $A>0$ and $A+B>0$ and $A+B+C>0$, then we have $F(X_1,X_2,X_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.
:::

Then we have

::: proposition
[]{#prop-inequalities26 label="prop-inequalities26"} If $(\theta_1,\theta_2,\theta_3)\in D_0$ satisfies the following 26 inequalities: $$\begin{aligned}
&(1): m_2+1>0 \nonumber \\\nonumber 
&(2): (2p+1)\theta_3<p+m_2+m_3+\frac{5}{2}\\\nonumber
&(3): 2p\theta_3+\theta_2<p+m_3+2\\\nonumber
&(4): (2p-1)\theta_3-\theta_2<p-m_2+m_3\\\nonumber
&(5): \theta_2>m_2+\frac{1}{2}\\\nonumber
&(6): (2p-1)\theta_3+\theta_2>p+m_2+m_3+1\\\nonumber
&(7):   2p\theta_3-\theta_2>p+m_3 \\\nonumber 
&(8): (2p+1)\theta_3>p-m_2+m_3+\frac{1}{2} \\\nonumber
&(9):  (2p+1)\theta_3+(\frac{q}{2}-1)\theta_1<p+m_2+m_3+m_1+3
\end{aligned}$$ $$\begin{aligned}
&(10): (\frac{q}{2}-1)\theta_1<m_2+m_1+\frac{3}{2} \nonumber \\\nonumber
&(11): \theta_2-\frac{q}{2}\theta_1>-m_1\\\nonumber
&(12): (2p+1)\theta_3-(\frac{q}{2}-1)\theta_1<p+m_2+m_3-m_1+2\\\nonumber
&(13): (\frac{q}{2}-1)\theta_1>-m_2+m_1-\frac{1}{2}\\\nonumber
&(14): \theta_2+\frac{q}{2}\theta_1>m_1+1 \\\nonumber
&(15): 2p\theta_3+\frac{q}{2}\theta_1<p+m_3+m_1+2\\\nonumber
&(16): 2p\theta_3-\frac{q}{2}\theta_1<p+m_3-m_1+1\\\nonumber
&(17): (2p-1)\theta_3-\theta_2+(\frac{q}{2}+1)\theta_1<p-m_2+m_3+m_1+\frac{1}{2}\\\nonumber
&(18): (2p-1)\theta_3-\theta_2-(\frac{q}{2}+1)\theta_1<p-m_2+m_2-m_1-\frac{1}{2}\\\nonumber
\end{aligned}$$ $$\begin{aligned}
&(19): \theta_2-(\frac{q}{2}+1)\theta_1>m_2-m_1\nonumber\\\nonumber
&(20): \theta_2+(\frac{q}{2}+1)\theta_1>m_2+m_1+1\\\nonumber
&(21): (2p-1)\theta_3+\theta_2-(\frac{q}{2}+1)\theta_1>p+m_2+m_3-m_1+\frac{1}{2}\\\nonumber
&(22): (2p-1)\theta_3+\theta_2+(\frac{q}{2}+1)\theta_1>p+m_2+m_3+m_1+\frac{3}{2}\\\nonumber
&(23): 2p\theta_3-\frac{q}{2}\theta_1>p+m_3-m_1\\\nonumber
&(24): 2p\theta_3+\frac{q}{2}\theta_1>p+m_3+m_1+1\\\nonumber
&(25): (2p+1)\theta_3-(\frac{q}{2}-1)\theta_1>p-m_1+m_3-m_1\\\nonumber
&(26): (2p+1)\theta_3+(\frac{q}{2}-1)\theta_1>p-m_2+m_3+m_1+1
\end{aligned}$$ then we have $F(X_1,X_2,X_3,m_1,m_2,m_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.
:::

We prove the proposition by subdividing $(X_1,X_2,X_3)\in \mathbb{R}^3$ into 48 regions.

Case I: $X_2\geq X_3\geq 0$,

I-A: $X_2\geq X_3\geq X_1\geq 0$, then $$\begin{aligned}
 &F(X_1,X_2,X_3;m_1,m_2,m_3)\\\nonumber
 &=(m_2+1)X_2+(p+m_3+\frac{3}{2}-(2p+1)\theta_3)X_3+(m_1+\frac{1}{2}-(\frac{q}{2}-1)\theta_1)X_1   
\end{aligned}$$ By Lemma [\[lemma-X1X2X3\]](#lemma-X1X2X3){reference-type="ref" reference="lemma-X1X2X3"}, if $$\begin{aligned}
m_1+1>0, \  \ (2p+1)\theta_3<p+m_2+m_3+\frac{5}{2},    
\end{aligned}$$ and $$\begin{aligned}
(2p+1)\theta_3+(\frac{q}{2}-1)\theta_1<p+m_2+m_3+m_1+3    
\end{aligned}$$ then we have $F(X_1,X_2,X_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.

I-B: $X_2\geq X_1\geq X_3\geq 0$, $$\begin{aligned}
 &F(X_1,X_2,X_3;m_1,m_2,m_3)\\\nonumber
 &=(m_2+1)X_2+(m_1+\frac{1}{2}-(\frac{q}{2}-1)\theta_1)X_1   +(p+m_3+\frac{3}{2}-(2p+1)\theta_3)X_3
\end{aligned}$$ By Lemma [\[lemma-X1X2X3\]](#lemma-X1X2X3){reference-type="ref" reference="lemma-X1X2X3"}, if $$\begin{aligned}
m_2+1>0, \ (\frac{q}{2}-1)\theta_1<m_2+m_1+\frac{3}{2}    
\end{aligned}$$ and $$\begin{aligned}
(2p+1)\theta_3+(\frac{q}{2}-1)\theta_1<p+m_2+m_3+m_1+3    
\end{aligned}$$ then we have $F(X_1,X_2,X_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.

I-C: $X_2\geq X_1\geq X_3\geq 0$, $$\begin{aligned}
 &F(X_1,X_2,X_3;m_1,m_2,m_3)\\\nonumber
 &=(m_1+\theta_2-\frac{q}{2}\theta_1)X_1+(m_2+\frac{3}{2}-\theta_2+\theta_1)X_2+(p+m_3+\frac{3}{2}-(2p+1)\theta_3)X_3   
\end{aligned}$$ By Lemma [\[lemma-X1X2X3\]](#lemma-X1X2X3){reference-type="ref" reference="lemma-X1X2X3"}, if $$\begin{aligned}
m_1+\theta_2-\frac{q}{2}\theta_1>0, \ (\frac{q}{2}-1)\theta_1<m_2+m_1+\frac{3}{2}    
\end{aligned}$$ and $$\begin{aligned}
(2p+1)\theta_3+(\frac{q}{2}-1)\theta_1<p+m_2+m_3+m_1+3    
\end{aligned}$$ then we have $F(X_1,X_2,X_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.

I-D: $X_2\geq X_3\geq -X_1\geq 0$, $$\begin{aligned}
 &F(X_1,X_2,X_3;m_1,m_2,m_3)\\\nonumber
 &=(m_2+1)X_2+(p+m_3+\frac{3}{2}-(2p+1)\theta_3)X_3+(-m_1-\frac{1}{2}+(\frac{q}{2}-1)\theta_1)(-X_1)   
\end{aligned}$$ By Lemma [\[lemma-X1X2X3\]](#lemma-X1X2X3){reference-type="ref" reference="lemma-X1X2X3"}, if $$\begin{aligned}
m_2+1>0, \ (2p+1)\theta_3<p+m_2+m_3+\frac{5}{2}    
\end{aligned}$$ and $$\begin{aligned}
(2p+1)\theta_3-(\frac{q}{2}-1)\theta_1<p+m_2+m_3-m_1+2    
\end{aligned}$$ then we have $F(X_1,X_2,X_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.

I-E: $X_2\geq -X_1\geq X_3\geq 0$, $$\begin{aligned}
 &F(X_1,X_2,X_3;m_1,m_2,m_3)\\\nonumber
 &=(m_2+1)X_2+(-m_1-\frac{1}{2}+(\frac{q}{2}-1)\theta_1)(-X_1)+(p+m_3+\frac{3}{2}-(2p+1)\theta_3)X_3   
\end{aligned}$$ By Lemma [\[lemma-X1X2X3\]](#lemma-X1X2X3){reference-type="ref" reference="lemma-X1X2X3"}, if $$\begin{aligned}
m_2+1>0, \ (\frac{q}{2}-1)\theta_1>-m_2+m_1-\frac{1}{2}    
\end{aligned}$$ and $$\begin{aligned}
(2p+1)\theta_3-(\frac{q}{2}-1)\theta_1<p+m_2+m_3-m_1+2    
\end{aligned}$$ then we have $F(X_1,X_2,X_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.

I-F: $-X_1\geq X_2\geq X_3\geq 0$, $$\begin{aligned}
 &F(X_1,X_2,X_3;m_1,m_2,m_3)\\\nonumber
 &=(-m_1-1+\theta_2+\frac{q}{2}\theta_1)(-X_1)+(m_2+\frac{3}{2}-\theta_2-\theta_1)X_2+(p+m_3+\frac{3}{2}-(2p+1)\theta_3)X_3   
\end{aligned}$$ By Lemma [\[lemma-X1X2X3\]](#lemma-X1X2X3){reference-type="ref" reference="lemma-X1X2X3"}, if $$\begin{aligned}
\theta_2+\frac{q}{2}\theta_1>m_1+1, \ (\frac{q}{2}-1)\theta_1>-m_2+m_1-\frac{1}{2}    
\end{aligned}$$ and $$\begin{aligned}
(2p+1)\theta_3-(\frac{q}{2}-1)\theta_1<p+m_2+m_3-m_1+2    
\end{aligned}$$ then we have $F(X_1,X_2,X_3)\rightarrow +\infty$ as $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.

Hence from the above 6 cases I-A,B,C,D, E and F, we obtain $8$ inequalities: $$\begin{aligned}
    & m_1+1>0, \\\nonumber 
    & (2p+1)\theta_3<p+m_2+m_3+\frac{5}{2} \\\nonumber
    & (2p+1)\theta_3+(\frac{q}{2}-1)\theta_1<p+m_2+m_3+m_1+3\\\nonumber
    & (\frac{q}{2}-1)\theta_1<m_2+m_1+\frac{3}{2} \\\nonumber
    & \theta_2-\frac{q}{2}\theta_1>-m_1\\\nonumber
    & (2p+1)\theta_1-(\frac{q}{2}-1)\theta_2<p+m_1+m_3-m_1+2 \\\nonumber
    & (\frac{q}{2}-1)\theta_1>-m_2+m_1-\frac{1}{2}\\\nonumber
    &\theta_2+\frac{q}{2}\theta_1>m_1+1
\end{aligned}$$

Similarly, by considering the other $7$ cases II:$Y\geq X\geq 0$, III: $Y\geq -X\geq 0$, IV: $-X\geq Y\geq 0$, V: $-X\geq -Y\geq 0$, VI: $-Y\geq -X\geq 0$, VII:$-Y\geq X\geq 0$, and VIII: $X\geq -Y\geq 0$, we finally obtain the 26 inequalities in Proposition [\[prop-inequalities26\]](#prop-inequalities26){reference-type="ref" reference="prop-inequalities26"}.

From the inequalities (1) and (5), we have $$\begin{aligned}
   -1<m_2<\theta_2-\frac{1}{2}<\frac{1}{2} 
\end{aligned}$$ since $\theta_2<1$. Hence for any $(\theta_1,\theta_2,\theta_3)\in D_0$, when $m_2< -1$ or $m_2\geq 1$, $F(X_1,X_2,X_3;m_1,m_2,m_3)$ goes to $-\infty$ in some direction of $X_1^2+X_2^2+X_3^2\rightarrow +\infty$.

In conclusion, when $m_2\neq 0$, the Fourier coefficients $\hat{h}_{N}(m_1,m_2,m_3)$ can be neglected. In the following, we consider the Fourier coefficient $\hat{h}_{N}(m_1,m_2,m_3)$ with $m_2=0$.

## The case $m_2=0$ but $(m_1,m_3)\neq (0,0)$

::: theorem
[]{#theorem-m_1 label="theorem-m_1"} When $m_1=0$ and $m_3\geq 1$, then $$\begin{aligned}
\hat{h}_{N}(0,0,m_3)    
\end{aligned}$$ can be neglected.
:::

::: proof
*Proof.* For $c_3\geq \frac{1}{2}+\frac{7}{8p}$, then $\tilde{c}_3\geq \frac{7}{8p}$, by Lemmas [\[theorem-inprincipal1\]](#theorem-inprincipal1){reference-type="ref" reference="theorem-inprincipal1"} and [\[theorem-inprincipal2\]](#theorem-inprincipal2){reference-type="ref" reference="theorem-inprincipal2"}, we have $$\begin{aligned}
    &2\pi \text{Re}\hat{V}(p,q; \theta_1,\theta_2,c_3=\frac{1}{2}+\tilde{c}_3;0,0,m_3)\\\nonumber
    &\leq 2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\pi^2 \tilde{c}_3^2\\\nonumber
    &\leq 2\pi\text{Re}\hat{V}\left(p,q,\theta_1\left(\frac{1}{2}\right),\theta_2\left(\frac{1}{2}\right),\frac{1}{2}\right)-\pi^2\frac{49}{64}\frac{1}{p^2}\\\nonumber
    &< Vol\left(M_{p,q}\right).  
\end{aligned}$$ Then the integral over the region $\{(\theta_1,\theta_2,\theta_3)\in D_0|\theta_3\leq \frac{1}{2}+\frac{7}{8p}\}$ can be neglected by using Theorem [\[theorem-usedinm1\]](#theorem-usedinm1){reference-type="ref" reference="theorem-usedinm1"}.

Moreover, when $m_3\geq 1$, from the inequalities (6) and (7), we obtain $$\begin{aligned}
(4p-1)\theta_3>2p+2m_3+1    
\end{aligned}$$ Hence $$\begin{aligned}
\theta_3>\frac{1}{2}+\frac{4m_3+3}{2(4p-1)}>\frac{1}{2}+\frac{7}{8p}.    
\end{aligned}$$

Therefore, over the region $\{(\theta_1,\theta_2,\theta_3)\in D_0|\theta_3\leq \frac{1}{2}+\frac{7}{8p}\}$, we can find a direction of $X_1^2+X_2^2+X_3^2\rightarrow +\infty$ such that $$\begin{aligned}
\text{Re}\hat{V}(p,q;0,0,m_3,\theta_1,\theta_2,\theta_3)\rightarrow -\infty.     
\end{aligned}$$ It follows that the integral over this region can be neglected. Therefore, the whole integral can be neglected. ◻
:::

::: theorem
[]{#theorem-m3 label="theorem-m3"} When $m_1\geq 1$ and $m_3=0$, then $$\begin{aligned}
\hat{h}_{N}(m_1,0,0)    
\end{aligned}$$ can be neglected.
:::

::: proof
*Proof.* For $\frac{2}{q}\leq c_1<\frac{1}{4}$, by Lemmas [\[theorem-inprincipal3\]](#theorem-inprincipal3){reference-type="ref" reference="theorem-inprincipal3"} and [\[theorem-inprincipal4\]](#theorem-inprincipal4){reference-type="ref" reference="theorem-inprincipal4"}, we have $$\begin{aligned}
 \label{formula-inequality}
    2\pi \text{Re}\hat{V}(p,q; c_1,\theta_2,\theta_3;m_1,0,0)&\leq Vol\left(S^3\setminus \mathcal{K}_p\right)-\frac{3}{2}\pi^2 c_1^2\\\nonumber
    &\leq Vol\left(S^3\setminus \mathcal{K}_p\right)-6\pi^2\frac{1}{q^2}\\\nonumber
    &<Vol\left(M_{p,q}\right).  
\end{aligned}$$ Then the integral over the region $\{(\theta_1,\theta_2,\theta_3)\in D_0|\theta_1> \frac{2}{q}\}$ can be neglected by using Theorem [\[theorem-usedinm3\]](#theorem-usedinm3){reference-type="ref" reference="theorem-usedinm3"}.

Moreover, when $m_1\geq 1$, from the inequalities (14), we obtain $$\begin{aligned}
\theta_1>\frac{2(2-\theta_2)}{q}>\frac{2}{q},
\end{aligned}$$

Therefore, over the region $\{(\theta_1,\theta_2,\theta_3)\in D_0|\theta_1\leq \frac{2}{q}\}$, we can find a direction of $X_1^2+X_2^2+X_3^2\rightarrow +\infty$ such that $$\begin{aligned}
\text{Re}\hat{V}(p,q;\theta_1,\theta_2,\theta_3;m_1,0,0)\rightarrow -\infty.     
\end{aligned}$$ It follows that the integral over this region can be neglected.

Therefore, the whole integral can be neglected. ◻
:::

::: theorem
When $m_1\geq 1$ and $m_3\geq 1$, then $$\begin{aligned}
\hat{h}_{N}(m_1,0,m_3)    
\end{aligned}$$ can be neglected.
:::

::: proof
*Proof.* First, when $m_1\geq 1$, from the inequalities (14), we obtain $$\begin{aligned}
\theta_1>\frac{2(2-\theta_2)}{q}>\frac{2}{q},
\end{aligned}$$

Therefore, over the region when $\theta_1< \frac{2}{q}$, we can find a direction of $X_1^2+X_2^2+X_3^2\rightarrow +\infty$ such that $$\begin{aligned}
\text{Re}\hat{V}(p,q;\theta_1,\theta_2,\theta_3;m_1,0,m_3)\rightarrow -\infty.     
\end{aligned}$$

It follows that the integral over the region $\{\theta_1< \frac{2}{q}\}$ can be neglected.

For $\frac{2}{q}\leq c_1\leq \frac{1}{4}$, on the region $D_0(c_1)=\{\theta_1=c_1\} \cap D_0$, we estimate the integral $$\begin{aligned}
    \int_{D_0(c_1)}\sin(\pi c_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(c_1,\theta_2,\theta_3;m_1,0,m_3)}d\theta_2d\theta_3
\end{aligned}$$ as follows.

For $\theta_3<\frac{1}{2}+\frac{7}{8p}$, then $\theta_3<\frac{1}{2}+\frac{7}{2(4p-1)}$, in this case, we can find a direction of $X_2^2+X_3^2\rightarrow +\infty$ such that $$\begin{aligned}
\text{Re}\hat{V}(p,q;c_1,\theta_2,\theta_3;m_1,0,m_3)\rightarrow -\infty.     
\end{aligned}$$ So the integral over $\theta_3<\frac{1}{2}+\frac{7}{8p}$ can be neglected.

For $\theta_3\geq \frac{1}{2}+\frac{7}{8p}$, we use the one-dimensional saddle point method. Let $\theta_3=c_3$, for $c_3\geq \frac{1}{2}+\frac{7}{8p}$, then by Lemma [\[Lemma-inequ\]](#Lemma-inequ){reference-type="ref" reference="Lemma-inequ"} and formula ([\[formula-inequality\]](#formula-inequality){reference-type="ref" reference="formula-inequality"}), we have $$\begin{aligned}
 &2\pi \text{Re}\hat{V}(p,q;m_1,0,m_3,c_1,T_2(c_1,\frac{1}{2}+\tilde{c}_3),c_3=\frac{1}{2}+\tilde{c}_3)\\\nonumber
 &<2\pi \text{Re} \hat{V}(p,q;m_1,0,0,c_1,\theta_2(c_1),\theta_3(c_1))\\\nonumber
 &<Vol\left(M_{p,q}\right).
\end{aligned}$$ By using the one-dimensional saddle method, see Appendix [\[appendix-onedim\]](#appendix-onedim){reference-type="ref" reference="appendix-onedim"}, we can show that integral over the region $\theta_3\geq \frac{1}{2}+\frac{7}{8p}$ can also be neglected.

Hence the whole integral can be neglected. ◻
:::

Therefore,

::: proposition
There exists $\epsilon>0$, such that $$\begin{aligned}
 \label{formula-propRT}
RT_{r}(M_{p,q})=4\hat{h}_{N}(0,0,0)+O(e^{(N+\frac{1}{2})(\zeta_{\mathbb{R}}(p,q)-\epsilon)}).     
\end{aligned}$$
:::

Finally, we only need to estimate the integral $\hat{h}_{N}(0,0,0)$.

## The contribution of $\hat{h}_{N}(0,0,0)$

We let $U_0'$ be the region determined by inequalities illustrated in Proposition [\[prop-inequalities26\]](#prop-inequalities26){reference-type="ref" reference="prop-inequalities26"} when $m_1=m_2=m_3=0$. Let $U_0=U'_0\cap D_0$, as a consequence of Proposition [\[prop-inequalities26\]](#prop-inequalities26){reference-type="ref" reference="prop-inequalities26"},

::: corollary
[]{#coro-U0noU0 label="coro-U0noU0"} For any $(\theta_1,\theta_2,\theta_3)\in D_0$,

\(i\) when $(\theta_1,\theta_2,\theta_3)\in U_0$, we have $$\begin{aligned}
    f(X_1,X_2,X_3)\rightarrow +\infty \ \text{as } \ X_1^2+X_2^2+X_3^2\rightarrow +\infty.
\end{aligned}$$

\(ii\) when $(\theta_1,\theta_2,\theta_3)\notin U_0$, $$\begin{aligned}
     f(X_1,X_2,X_3)\rightarrow -\infty \ \text{in some directions of} \  X_1^2+X_2^2+X_3^2\rightarrow +\infty.
\end{aligned}$$
:::

We introduce the cube MCB as shown in figure [1](#figure-cube){reference-type="ref" reference="figure-cube"}, the integrand is symmetric with respect to $\theta_3=\frac{1}{2}$, $\theta_1=0$ and by Lemma [\[lemma-regionD\'0\]](#lemma-regionD'0){reference-type="ref" reference="lemma-regionD'0"}, we have

<figure id="figure-cube">
<p><span class="math display">$$\begin{aligned}
\raisebox{-15pt}{
\includegraphics[width=450 pt]{Cube.pdf}}.
\end{aligned}$$</span></p>
<figcaption>The cube MCB</figcaption>
</figure>

$$\begin{aligned}
 &\int_{D_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3\\\nonumber
 &=4\int_{MCB}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3 +O(e^{\frac{N+\frac{1}{2}}{2\pi }(3.56337-\epsilon)})   
\end{aligned}$$

So we only need to consider the integral over the cube MCB $$\begin{aligned}
 \int_{MCB}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3.    
\end{aligned}$$

Consider the function $$\begin{aligned}
  v(\theta_1,\theta_3,\theta_3)&=\text{Re}\hat{V}(p,q,\theta_1,\theta_2,\theta_3)\\\nonumber
  &=\Lambda(\theta_2+\theta_3)+\Lambda(\theta_2-\theta_3)-\Lambda(\theta_2+\theta_1)-\Lambda(\theta_2)-\Lambda(\theta_2-\theta_1). 
\end{aligned}$$

we have $$\begin{aligned}
 \label{formula-vtheta1}
\frac{dv(\theta_1,\theta_2,\theta_3)}{d\theta_1}=\Lambda'(\theta_2-\theta_1)-\Lambda'(\theta_2+\theta_1)=2\log \frac{|\sin \pi(\theta_2+\theta_1)|}{|\sin \pi(\theta_2-\theta_1)|}<0    
\end{aligned}$$ and $$\begin{aligned}
 \label{formula-vtheta2}
\frac{dv(\theta_1,\theta_2,\theta_3)}{d\theta_3}=\Lambda'(\theta_2+\theta_3)-\Lambda'(\theta_2-\theta_3)=2\log \frac{|\sin \pi(\theta_2-\theta_3)|}{|\sin \pi(\theta_2+\theta_3)|}<0    
\end{aligned}$$ for $0<\theta_1< \frac{1}{2}$, $\frac{1}{2}<\theta_2<1$ and $\frac{1}{2}<\theta_3<1$.

Therefore, on the cube $CB_1: I_{21}J_2J_3I_{31}-E_{21}F_2F_3E_{31}$, for $(\theta_1,\theta_2,\theta_3)\in CB_1$, we have $$\begin{aligned}
 \label{formula-CB1}
&2\pi v(\theta_1,\theta_3,\theta_3)\leq  2\pi \max_{\theta_2\in (\frac{1}{2},1)} v\left(\frac{1}{4},\theta_2,\frac{3}{4}\right)\\\nonumber
&=2\pi v\left(\frac{1}{4},\frac{5}{6},\frac{3}{4}\right)=v_3 <3.56337.   
\end{aligned}$$ On the cube $CB_2: A_{21}B_2B_3A_{31}-I_{21}J_2J_3I_{31}$, for $(\theta_1,\theta_2,\theta_3)\in CB_2$, we have $$\begin{aligned}
 \label{formula-CB2}
&2\pi v(\theta_1,\theta_3,\theta_3)\leq 2\pi\max_{\theta_2\in (\frac{1}{2},1)}v\left(0,\theta_2,\frac{3}{4}\right)\\\nonumber
&=2\pi v\left(0,\frac{5}{6},\frac{3}{4}\right)=3.552296<3.56337.   
\end{aligned}$$ On the cube $CB_3: I_{01}J_0J_2I_{21}-E_{01}F_0F_2E_{21}$, for $(\theta_1,\theta_2,\theta_3)\in CB_3$, we have $$\begin{aligned}
  \label{formula-CB3}
&2\pi v(\theta_1,\theta_3,\theta_3)\leq 2\pi\max_{\theta_2\in (\frac{1}{2},1)}v\left(\frac{1}{4},\theta_2,\frac{1}{2}\right)\\\nonumber
&=2\pi v\left(\frac{1}{4},0.688635,\frac{1}{2}\right)=3.252728<3.56337.   
\end{aligned}$$

Now we consider the cube $SPM_1: A_{01}B_0B_2A_{21}-I_{01}J_0J_2I_{21}$ as shown in Figure [2](#figure2){reference-type="ref" reference="figure2"}, it is obvious that $$\begin{aligned}
MCB=SPM_1\cup CB_1\cup CB_2\cup CB_3.     
\end{aligned}$$ By the formulas ([\[formula-CB1\]](#formula-CB1){reference-type="ref" reference="formula-CB1"}), ([\[formula-CB2\]](#formula-CB2){reference-type="ref" reference="formula-CB2"}) and ([\[formula-CB3\]](#formula-CB3){reference-type="ref" reference="formula-CB3"}), we obtain $$\begin{aligned}
 &\int_{MCB}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}\\\nonumber
 &=\int_{SPM_1}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}+O(e^{\frac{N+\frac{1}{2}}{2\pi }(3.56337-\epsilon)}).  
\end{aligned}$$

<figure id="figure2">
<p><span class="math display">$$\begin{aligned}
\raisebox{-15pt}{
\includegraphics[width=500 pt]{Cube0.pdf}}.
\end{aligned}$$</span></p>
<figcaption>The cube <span class="math inline"><em>S</em><em>P</em><em>M</em><sub>1</sub></span></figcaption>
</figure>

Now we consider the integral over $SPM_1$. For the cube $CB_4: M_{11}N_1N_2M_{21}-I_{11}J_1J_2I_{21}$.

For any fixed $(c_1,c_3)\in M_{11}M_{21}J_{21}I_{11}$, i.e. $c_{10}\leq c_1<\frac{1}{4}$ and $c_{20}\leq c_3<\frac{3}{4}$, the critical point equation $\hat{V}_{\theta_2}(p,q,c_1,\theta,c_3)=0$ has a unique solution $\theta_2(c_1,c_3)$ with $\text{Re}(\theta_2(c_1,c_3))\in (\frac{1}{2},1)$, see Appendix [\[appendix-onedim\]](#appendix-onedim){reference-type="ref" reference="appendix-onedim"}. By Proposition [\[prop-Rec1c3decrease\]](#prop-Rec1c3decrease){reference-type="ref" reference="prop-Rec1c3decrease"}, we obtain $$\begin{aligned}
&2\pi \text{Re}\hat{V}(p,q,c_1,\theta_2(c_1,c_3),c_3)\\\nonumber
&\leq 2\pi\text{Re}\hat{V}(p,q,c_{10},\theta_2(c_{10},c_{30}),c_{30}))\\\nonumber
&=2\pi\text{Re}\hat{V}(p,q,0.1225320,0.808058-0.111315\sqrt{-1},0.600484))\\\nonumber
& =3.25806<3.56337
\end{aligned}$$

By using the one-dimensional saddle point method, see Appendix [\[appendix-onedim\]](#appendix-onedim){reference-type="ref" reference="appendix-onedim"} for checking the condition, we estimate the integral $$\begin{aligned}
\int_{\frac{1}{2}}^1 \sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(c_1,\theta_2,c_3)}d\theta_2  =O(e^{\frac{N+\frac{1}{2}}{2\pi}(3.56337-\epsilon)}) 
\end{aligned}$$ for some $\epsilon>0$. Therefore, $$\begin{aligned}
&\int_{CB4}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}\\\nonumber
&=\int_{(\theta_1,\theta_3)\in M_{11}M_{21}J_{21}I_{11}} \left(\int_{\frac{1}{2}}^{1}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_2\right)d\theta_1d\theta_3\\\nonumber
&=O(e^{\frac{N+\frac{1}{2}}{2\pi }(3.55337-\epsilon)}).
\end{aligned}$$

On the Triangular Prism $TPL_1: A_{01}M_{03}M_{01}-A_{2}M_{23}M_{21}$, for $(\theta_1,\theta_2,\theta_3)\in TPL_1$, by formula ([\[formula-vtheta2\]](#formula-vtheta2){reference-type="ref" reference="formula-vtheta2"}), we have $$\begin{aligned}
 \label{formula-TPL1}
&2\pi \max_{(\theta_1,\theta_2,\theta_3)\in TPL_1} v(\theta_1,\theta_2,\theta_3)\\\nonumber 
   &=2\pi \max_{(\theta_1,\theta_2)\in A_{01}M_{03}M_{01}}v(\theta_1,\theta_2,\frac{1}{2})\\\nonumber
   &=2\pi \max_{0\leq c\leq c_{10}}v\left(c,c+\frac{1}{2},\frac{1}{2}\right)\\\nonumber
   &=2\pi v\left(c_{10},c_{10}+\frac{1}{2},\frac{1}{2}\right)=3.37448<3.56337. 
\end{aligned}$$ Similarly, on the Triangular Prism $TPR_1: B_{0}M_{06}N_{0}-B_{2}M_{25}N_{2}$, we have $$\begin{aligned}
 \label{formula-TPR1}
&2\pi \max_{(\theta_1,\theta_2,\theta_3)\in TPR_1} v(\theta_1,\theta_2,\theta_3)\\\nonumber
&=2\pi \max_{(\theta_1,\theta_3)\in B_{0}M_{05}N_0} v\left(\theta_1,\theta_2,\frac{1}{2}\right)\\\nonumber
&=2\pi \max_{0\leq c\leq c_{10}}v(c,1-c,\frac{1}{2})\\\nonumber
&=2\pi v\left(c_{10},1-c_{10},\frac{1}{2}\right)=2.93274<3.56337.
\end{aligned}$$ On the Triangular Prism $TPL_2: A_{01}A_{12}A_{11}-I_{01}I_{12}I_{11}$, we have $$\begin{aligned}
&2\pi \max_{(\theta_1,\theta_2,\theta_3)\in TPL_2} v(\theta_1,\theta_2,\theta_3)\\\nonumber
&=2\pi \max_{(\theta_2,\theta_3)\in A_{01}A_{12}A_{11}} v(0,\theta_2,\theta_3)\\\nonumber
&=2\pi \max_{0\leq c\leq c_{30}}v(0,c,c)\\\nonumber
&=2\pi v(0, c_{30},c_{30})=2.27746<3.56337.
\end{aligned}$$ On the Triangular Prism $TPR_2: B_{0}B_{1}A_{16}-J_{0}J_{1}I_{16}$, we have $$\begin{aligned}
&2\pi \max_{(\theta_1,\theta_2,\theta_3)\in TPR_2} v(\theta_1,\theta_2,\theta_3)\\\nonumber
&=2\pi \max_{(\theta_2,\theta_3)\in B_{0}B_{1}A_{16}} v(0,\theta_2,\theta_3)\\\nonumber
&=2\pi \max_{0\leq c\leq c_{30}}v\left(0,\frac{3}{2}-c,c\right)\\\nonumber
&=2\pi v\left(0, \frac{3}{2}-c_{30},c_{30}\right)=3.56337.
\end{aligned}$$

Note that the intersections of $TPL_1$ and $TPL_2$ is a truncated triangular prism $TTPL: A_{01}Q_{12}A_{11}-M_{01}M_{12}M_{11}$, and the intersections of $TPR_1$ and $TPR_2$ is a truncated triangular prisim $TTPR: B_0Q_{16}B_1-N_{01}M_{16}N_1$.

Now, we let $SPM_2=SPM_1-TPL_1-TPR_1-(TPL_2\setminus TTPL)-(TPR_2\setminus TTPR)$, by previous formulas, we have $$\begin{aligned}
&\int_{SPM_1}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}\\\nonumber
&=\int_{SPM_2}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}+O(e^{\frac{N+\frac{1}{2}}{2\pi}(3.55337-\epsilon)}).  
\end{aligned}$$

For the Trapezoidal Prism $TZP_1: A_{11}B_1M_{15}M_{13}-A_{21}B_2M_{25}M_{23}$, first, we add two triangular prisms $A_{11}M_{13}M_{11}-A_{21}M_{23}M_{21}$ and $B_1M_{15}N_1-B_2M_{25}N_2$ to $TZP_1$, we obtain a cube $CB_5: A_{11}B_1B_2A_{21}-M_{11}N_1N_2M_{21}$,

By formulas ([\[formula-TPL1\]](#formula-TPL1){reference-type="ref" reference="formula-TPL1"}) and ([\[formula-TPR1\]](#formula-TPR1){reference-type="ref" reference="formula-TPR1"}), we obtain that $$\begin{aligned}
&\int_{TZP_1}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}\\\nonumber
&=\int_{CB_5}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}+O(e^{\frac{N+\frac{1}{2}}{2\pi}(3.55337-\epsilon)})
\end{aligned}$$

For any fixed $(c_1,c_3)\in A_{11}A_{21}M_{21}M_{11}$, i.e. $0\leq c_{1}\leq c_{10}$ and $c_{20}\leq c_3<\frac{3}{4}$, the critical point equation $\hat{V}_{\theta_2}(p,q,c_1,\theta,c_3)=0$ has a unique solution $\theta_2(c_1,c_3)$ with $\text{Re}(\theta_2(c_1,c_3))\in (\frac{1}{2},1)$, see Appendix [\[appendix-onedim\]](#appendix-onedim){reference-type="ref" reference="appendix-onedim"}. By Proposition [\[prop-Rec1c3decrease\]](#prop-Rec1c3decrease){reference-type="ref" reference="prop-Rec1c3decrease"} we obtain $$\begin{aligned}
&2\pi \text{Re}\hat{V}(p,q,c_1,\theta_2(c_1,c_3),c_3)\\\nonumber
&\leq 2\pi\text{Re}\hat{V}(p,q,c_{10},\theta_2(c_{10},c_{30}),c_{30}))\\\nonumber
&=2\pi\text{Re}\hat{V}(p,q,0,0.8270666460-0.1216893136\sqrt{-1},0.600484))\\\nonumber
& =3.563367<3.56337.
\end{aligned}$$

By using the one-dimensional saddle point method, see Appendix [\[appendix-onedim\]](#appendix-onedim){reference-type="ref" reference="appendix-onedim"} for checking the condition, we estimate the integral $$\begin{aligned}
\int_{\frac{1}{2}}^1 \sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(c_1,\theta_2,c_3)}d\theta_2  =O(e^{\frac{N+\frac{1}{2}}{2\pi}(3.56337-\epsilon)}) 
\end{aligned}$$ for some $\epsilon>0$. Therefore, $$\begin{aligned}
&\int_{CB_5}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}\\\nonumber
&=\int_{(\theta_1,\theta_3)\in A_{11}A_{21}M_{21}M_{11}}\left(\int_{\frac{1}{2}}^{1}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_2\right)d\theta_1d\theta_3\\\nonumber
&=O(e^{\frac{N+\frac{1}{2}}{2\pi }(3.56337-\epsilon)}).
\end{aligned}$$

For the Trapezoidal Prism $TZP_2: M_{01}N_0M_{16}M_{12}-I_{01}J_0I_{16}I_{12}$, we can estimates its integral similarly as the computation for $TZP_1$.

Finally, we obtain a polyhedron $SPM_2=MCB-\cup_{i=1}^6CB_i-\cup_{i=1}^2 TPL_i-\cup_{i=1}^2 TPR_i$. Then we use the polyhedron $SPM_2$ to do the reflection along the plane $\theta_3=\frac{1}{2}$ and $\theta_1=0$ to obtain a new polyhedron denoted by $P$, the key point is that $P\subset D_{H}$. Let $D_0''=P\cap D_{0}$, the above analysis tell us that $$\begin{aligned}
&\int_{D_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3\\\nonumber
&=\int_{D''_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3+O(e^{(N+\frac{1}{2})\zeta_{\mathbb{R}}(p,q)-\epsilon}).    
\end{aligned}$$

::: proposition
[]{#prop-m0n0 label="prop-m0n0"} For $(p,q)$ satisfies the condition ([\[formula-pqconditions\]](#formula-pqconditions){reference-type="ref" reference="formula-pqconditions"}), we have $$\begin{aligned}
 \label{formula-D''}
    \hat{h}_N(0,0,0)&=-\kappa''_r\int_{D_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3   \\\nonumber
    &=\kappa''_r\omega(p,q)e^{(N+\frac{1}{2})\zeta_{\mathbb{R}}(p,q)}\\\nonumber
&\cdot\left(1+\sum_{i=1}^d\kappa_i(p,q)\left(\frac{2\pi\sqrt{-1}}{N+\frac{1}{2}}\right)^i+O\left(\frac{1}{(N+\frac{1}{2})^{d+1}}\right)\right),
    
\end{aligned}$$ for $d\geq 1$, where $\omega(p,q)$ and $\kappa_i(p,q)$ are constants determined by $M_{p,q}$.
:::

::: proof
*Proof.* We need to estimate the following integral $$\begin{aligned}
 &\int_{D_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3. 
\end{aligned}$$

According to formula ([\[formula-D\'\'\]](#formula-D''){reference-type="ref" reference="formula-D''"}), we only need to estimate the integral $$\begin{aligned}
  \label{formula-integralD''}
\int_{D''_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3. 
\end{aligned}$$

We will verify the conditions of Proposition [\[proposition-saddlemethod\]](#proposition-saddlemethod){reference-type="ref" reference="proposition-saddlemethod"} for saddle point method in Proposition [\[propostion-checksaddle\]](#propostion-checksaddle){reference-type="ref" reference="propostion-checksaddle"}. By Proposition [\[prop-VNexpansion\]](#prop-VNexpansion){reference-type="ref" reference="prop-VNexpansion"} and Remark [\[remark-saddle\]](#remark-saddle){reference-type="ref" reference="remark-saddle"}, we can apply the Proposition [\[proposition-saddlemethod\]](#proposition-saddlemethod){reference-type="ref" reference="proposition-saddlemethod"} to the above integral ([\[formula-integralD\'\'\]](#formula-integralD''){reference-type="ref" reference="formula-integralD''"}). Let $(\theta_1^0,\theta_2^0,\theta_3^0)$ be the critical point of $\hat{V}(p,q,\theta_1,\theta_2,\theta_3)$, we obtain that

$$\begin{aligned}
  &\int_{D''_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3\\\nonumber
        &=\left(\frac{\pi}{N+\frac{1}{2}}\right)^{\frac{3}{2}}\frac{\alpha(\theta_1^0,\theta_2^0,\theta_3^0)}{\sqrt{\det \left(-\frac{1}{2}\text{Hess}(\hat{V})(\theta_1^0,\theta_2^0,\theta_3^0)\right)}}e^{(N+\frac{1}{2})\zeta(p,q)}\\\nonumber
        &\left(1+\sum_{i=1}^d\kappa_i(p,q)\left(\frac{2\pi\sqrt{-1}}{N+\frac{1}{2}}\right)^i+O\left(\frac{1}{(N+\frac{1}{2})^{d+1}}\right)\right)   
\end{aligned}$$ where the function $$\begin{aligned}
    &\alpha(\theta_1^0,\theta_2^0,\theta_3^0)\\\nonumber
    &=\sin(\pi\theta_1^0)\sin(2\pi\theta_3^0)e^{\pi\sqrt{-1}\left(2\theta_2^0+(p-2q+\frac{7}{4})\right)-\frac{1}{2}\log(1-e^{2\pi\sqrt{-1}(\theta_2^0+\theta_3^0)})-\frac{1}{2}\log(1-e^{2\pi\sqrt{-1}(\theta_2^0-\theta_3^0)})}\\\nonumber
    &=\frac{(-1)^{p-\frac{1}{4}}z_2^0(z_3^0-\frac{1}{z_3^{0}})(\sqrt{z_1^0}-\frac{1}{\sqrt{z_1^0}})}{4\sqrt{(1-z_2^0z_3^0)(1-z_2^0\frac{1}{z_{3}^0})}}.
\end{aligned}$$ the determinant of the Hessian matrix at $(\theta_1^0,\theta_2^0,\theta_3^0)$ is given by $$\begin{aligned}
    &\det \left(-\frac{1}{2}\text{Hess}(\hat{V})(\theta_1^0,\theta_2^0,\theta_3^0)\right)=(-\frac{1}{2})^3(2\pi\sqrt{-1})^3H(p,q;z_1^0,z_2^0,z_3^0)
\end{aligned}$$ where $$\begin{aligned}
  &H(p,q;z_1^0,z_2^0,z_3^0)=4\frac{z_2^0}{z_1^0-z_2^0}\cdot \frac{z_1^0z_2^0}{1-z_1^0z_2^0}\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)\\\nonumber
  &-4\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\frac{z_2^0z_3^0}{1-z_2^0z_3^0}\cdot\frac{z_2^0}{z_3^0-z_2^0}+\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\frac{z_2^0}{1-z_2^0}\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)\\\nonumber
  &+(8p+4)\frac{z_2^0}{z_1^0-z_2^0}\cdot \frac{z_1^0z_2^0}{1-z_1^0z_2^0}+(2p+1)\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\frac{z_2^0}{1-z_2^0}\\\nonumber
  &-(2p+\frac{q}{2})\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}\right)\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)-(\frac{q}{2}-1)\frac{z_2^0}{1-z_2^0}\left(\frac{z_2^0z_3^0}{1-z_2^0z_3^0}+\frac{z_2^0}{z_3^0-z_2^0}\right)\\\nonumber
  &+4(\frac{q}{2}-1)\frac{z_2^0z_3^0}{1-z_2^0z_3^0}\cdot\frac{z_2^0}{z_3^0-z_2^0}-(2p+1)(\frac{q}{2}-1)\left(\frac{z_2^0}{z_1^0-z_2^0}+\frac{z_1^0z_2^0}{1-z_1^0z_2^0}+\frac{z_2^0}{1-z_{2}^0}-\frac{z_2^0z_3^0}{1-z_2^0z_3^0}-\frac{z_2^0}{z_3^0-z_2^0}\right).
\end{aligned}$$

Therefore, we have

$$\begin{aligned}
  &\int_{D''_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3\\\nonumber
        &=\frac{(-1)^{p}\sqrt{-1}z_2(z_3-z_3^{-1})(\sqrt{z_1}-\frac{1}{\sqrt{z_1}})}{4(N+\frac{1}{2})^{\frac{3}{2}}\sqrt{(1-z_2z_3)(1-z_2z_{3}^{-1})}\sqrt{H(p,q;z_1^0,z_2^0,z_3^0)}}e^{(N+\frac{1}{2})\zeta(p,q)}\\\nonumber
        &\cdot\left(1+\sum_{i=1}^d\kappa_i(p,q)\left(\frac{2\pi\sqrt{-1}}{N+\frac{1}{2}}\right)^i+O\left(\frac{1}{(N+\frac{1}{2})^{d+1}}\right)\right). 
\end{aligned}$$ Hence $$\begin{aligned}
     \hat{h}_N(0,0,0)&=-\kappa''_r\int_{D_0}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3\\\nonumber
     &=(-1)^{p+1}\frac{\sqrt{-1}}{4}e^{\sigma((\mathcal{K}_p)_q)\left(\frac{3}{2N+1}+\frac{N+1}{2}\right)\pi\sqrt{-1}}
     \omega(p,q)e^{(N+\frac{1}{2})\zeta(p,q)}\\\nonumber
        &\cdot\left(1+\sum_{i=1}^d\kappa_i(p,q)\left(\frac{2\pi\sqrt{-1}}{N+\frac{1}{2}}\right)^i+O\left(\frac{1}{(N+\frac{1}{2})^{d+1}}\right)\right)
\end{aligned}$$ where $$\begin{aligned}
 \label{formula-omega}
    \omega(p,q)=\frac{z_2^0(z_3^0-(z_3^0)^{-1})(\sqrt{z_1^0}-\frac{1}{\sqrt{z_1^0}})}{\sqrt{(1-z_2^0z_3^0)(1-z_2^0(z_{3}^0)^{-1})}\sqrt{H(p,q;z_1^0,z_2^0,z_3^0)}}.
\end{aligned}$$ ◻
:::

::: proposition
[]{#propostion-checksaddle label="propostion-checksaddle"} When we apply Proposition [\[proposition-saddlemethod\]](#proposition-saddlemethod){reference-type="ref" reference="proposition-saddlemethod"} (saddle point method) to the integral ([\[formula-integralD\'\'\]](#formula-integralD''){reference-type="ref" reference="formula-integralD''"}), the assumptions of Proposition [\[proposition-saddlemethod\]](#proposition-saddlemethod){reference-type="ref" reference="proposition-saddlemethod"} holds.
:::

::: proof
*Proof.* We note that, by Lemma [\[lemma-varphixi3\]](#lemma-varphixi3){reference-type="ref" reference="lemma-varphixi3"}, $\hat{V}_N(p,q;\theta_1,\theta_2,\theta_3)$ uniformly converges to the $\hat{V}(p,q;\theta_1,\theta_2,\theta_3)$ on $D''_0$ as $N\rightarrow \infty$. Hence, we only need to verify the assumptions of the saddle point method for $\hat{V}(p,q;\theta_1,\theta_2,\theta_3)$. We show that there exists a homotopy $D''_\delta$ ($0\leq \delta\leq 1$) between $D''_0$ and $D''_1$ such that $$\begin{aligned}
 &(\theta_1^0,\theta_2^0,\theta_3^0)\in D''_1,  \label{saddle-1} \\ 
    &D''_1-\{(\theta_1^0,\theta_2^0,\theta_3^0)\}\subset \{(\theta_1,\theta_2,\theta_3)\in \mathbb{C}^3|Re V(p,q;\theta_1,\theta_2,\theta_3)<\zeta_\mathbb{R}(p,q)\}, \label{saddle-2} \\
    & \int_{\partial D''_{\delta}} \sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3=O\left(e^{(N+\frac{1}{2})(\zeta_{\mathbb{R}}(p,q)-\epsilon)}\right). \label{saddle-3}
\end{aligned}$$

In the fiber of the projection $\mathbb{C}^3\rightarrow \mathbb{R}^3$ at $(\theta_{1R},\theta_{2R},\theta_{3R})\in D_0''$, we consider the flow from $(X_1,X_2,X_3)=(0,0,0)$ determined by the vector field $(-\frac{\partial \hat{f}}{\partial X_1},-\frac{\partial \hat{f}}{\partial X_2},-\frac{\partial \hat{f}}{\partial X_3})$. By the construction of the region $D''_0\subset D_{H}$, together with Corollary [\[coro-U0noU0\]](#coro-U0noU0){reference-type="ref" reference="coro-U0noU0"} and Proposition [\[proposition-Hessianf\]](#proposition-Hessianf){reference-type="ref" reference="proposition-Hessianf"}, the convex neighborhood $U_0$ of $(\theta^0_{1R},\theta^0_{2R},\theta^0_{3R})$ satisfies the following holds.

-   If $(\theta_{1R},\theta_{2R},\theta_{3R})\in U_0$, then $\hat{f}$ has a unique minimal point, and the flow goes there.

-   If $(\theta_{1R},\theta_{2R},\theta_{3R})\in D''_0\setminus U_0$, then the flow goes to infinity.

We put $\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})=(g_1(\theta_{1R},\theta_{2R},\theta_{3R}),g_2(\theta_{1R},\theta_{2R},\theta_{3R}),g_2(\theta_{1R},\theta_{2R},\theta_{3R})$ to be the minimal point of $(1)$. In particular, $|\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})|\rightarrow \infty$ as $(\theta_{1R},\theta_{2R},\theta_{3R})$ goes to $\partial U_0$. Further, for a sufficiently large $R>0$, we stop the flow when $|\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})|=R$. We construct the revised flow $\hat{\mathbf{g}}(\theta_{1R},\theta_{2R},\theta_{3R})$, by putting $\hat{\mathbf{g}}(\theta_{1R},\theta_{2R},\theta_{3R})=\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})$ for $(\theta_{1R},\theta_{2R},\theta_{3R})\in U_0$ with $|\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})|<R$, otherwise, by putting $|\hat{\mathbf{g}}(\theta_{1R},\theta_{2R},\theta_{3R})|=(R,R,R)$.

We define the ending of the homotopy by $$\begin{aligned}
    D''_1=\{(\theta_{1R},\theta_{2R},\theta_{3R})+\hat{\mathbf{g}}(\theta_{1R},\theta_{2R},\theta_{3R})\sqrt{-1}|(\theta_{1R},\theta_{2R},\theta_{3R})\in D''_0\}. 
\end{aligned}$$ Further, we define the internal part of the homotopy by setting it along the flow from $(\theta_{1R},\theta_{2R},\theta_{3R})$ determined by the vector field $\left(-\frac{\partial \hat{f}}{\partial X_1},-\frac{\partial \hat{f}}{\partial X_2},-\frac{\partial \hat{f}}{\partial X_3}\right)$.

We show ([\[saddle-1\]](#saddle-1){reference-type="ref" reference="saddle-1"}) and ([\[saddle-2\]](#saddle-2){reference-type="ref" reference="saddle-2"}) as follows. We consider the function $$\begin{aligned}
    h(\theta_{1R},\theta_{2R},\theta_{3R})=\text{Re} V(\theta_{1R}+\sqrt{-1}\hat{g}_1,\theta_{2R}+\sqrt{-1}\hat{g}_2,\theta_{3R}+\sqrt{-1}\hat{g}_3). 
\end{aligned}$$ If $(\theta_{1R},\theta_{2R},\theta_{3R})\notin U_0$, by (2), $-h(\theta_{1R},\theta_{2R},\theta_{3R})$ is sufficiently large (because we let $R$ be sufficiently large), hence ([\[saddle-2\]](#saddle-2){reference-type="ref" reference="saddle-2"}) holds in this case. Otherwise, $(\theta_{1R},\theta_{2R},\theta_{3R})\in U_0$, in this case, $\hat{\mathbf{g}}(\theta_{1R},\theta_{2R},\theta_{3R})=\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})$. It is shown from the definition of $\hat{\mathbf{g}}(\theta_{1R},\theta_{2R},\theta_{3R})$ that $$\begin{aligned}
    \frac{\partial \text{Re} \hat{V}}{\partial X_1}=\frac{\partial \text{Re} \hat{V}}{\partial X_2}=\frac{\partial \text{Re} \hat{V}}{\partial X_3}=0 \ \text{at} \ (X_1,X_2,X_3)=\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R}),
\end{aligned}$$ which implies $$\begin{aligned}
    \text{Im}\frac{\partial \hat{V}}{\partial \theta_1}=\text{Im} \frac{\partial \hat{V}}{\partial \theta_2}=\text{Im} \frac{\partial \hat{V}}{\partial \theta_3}=0 \ \text{at} \ (\theta_{1R},\theta_{2R},\theta_{3R})+\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})\sqrt{-1}.
\end{aligned}$$ On the other hand, for $i=1,2,3$, $$\begin{aligned}
        \frac{\partial h}{\partial \theta_{iR}}=\text{Re}\frac{\partial \hat{V}}{\partial \theta_i}, \ \text{at} \ (\theta_{1R},\theta_{2R},\theta_{3R})+\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})\sqrt{-1}.
    
\end{aligned}$$ Therefore, when $(\theta_{1R},\theta_{2R},\theta_{3R})+\mathbf{g}(\theta_{1R},\theta_{2R},\theta_{3R})\sqrt{-1}$ is a critical point of $\hat{V}$, $(\theta_{1R},\theta_{2R},\theta_{3R})$ is a critical point of $h(\theta_{1R},\theta_{2R},\theta_{3R})$. Hence by Proposition [\[prop-critical\]](#prop-critical){reference-type="ref" reference="prop-critical"}, $h(\theta_{1R},\theta_{2R},\theta_{3R})$ has a unique maximal point at $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)$ which is equal to $\zeta_{\mathbb{R}}(p,q)$. Therefore, ([\[saddle-1\]](#saddle-1){reference-type="ref" reference="saddle-1"}) and ([\[saddle-2\]](#saddle-2){reference-type="ref" reference="saddle-2"}) holds.

We show ([\[saddle-3\]](#saddle-3){reference-type="ref" reference="saddle-3"}) as follows. Note that the boundary of $\partial D''_0$ consists of $D_0(c_{10})$, $D_0(c_{30})$ and the partial boundaries of $D_0$ denoted by $D_{0b}$. Hence $\partial D''_{\delta}$ consists of three parts denoted by $$\begin{aligned}
    \partial D''_{\delta}=A_1\cup A_2\cup B,
\end{aligned}$$ where $A_1$ and $A_2$ comes from the flows start at $(\theta_{1R},\theta_{2R},\theta_{3R})\in D_0(c_{10})$ and $(\theta_{1R},\theta_{2R},\theta_{3R})\in D_0(c_{30})$ respectively, while $B$ comes from the flows start at $(\theta_{1R},\theta_{2R},\theta_{3R})\in D_{0b}$.

By its definition, $D_{0b}\subset \partial D_{0}\subset \{(\theta_{1},\theta_{2},\theta_{3})\in \mathbb{C}^3|\text{Re} \hat{V}(p,q;\theta_{1},\theta_{2},\theta_{3})<\zeta_\mathbb{R}(p,q)-\epsilon\}$, and the function $\text{Re} \hat{V}(p,q;\theta_1,\theta_2,\theta_3)$ decreases under the flow, so we have $$\begin{aligned}
 \label{formula-integralB2}
    \int_{B}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3=O\left(e^{(N+\frac{1}{2})(\zeta_{\mathbb{R}}(p,q)-\epsilon)}\right).
\end{aligned}$$

By Theorems [\[theorem-usedinm1\]](#theorem-usedinm1){reference-type="ref" reference="theorem-usedinm1"} and [\[theorem-usedinm3\]](#theorem-usedinm3){reference-type="ref" reference="theorem-usedinm3"}, the integrals on $D_0(c_{10})$ and $D_0(c_{30})$ is also of order $O(e^{(N+\frac{1}{2})(\zeta_\mathbb{R}(p,q)-\epsilon}))$. By applying the saddle point method to the slices of the region $A_1\cup A_2$ as shown in Appendix [\[Appendix-twodimsaddle\]](#Appendix-twodimsaddle){reference-type="ref" reference="Appendix-twodimsaddle"}, we can prove that $$\begin{aligned}
 \label{formula-integralA1A22}
    \int_{A_1\cup A_2}\sin(\pi \theta_1)\sin(2\pi\theta_3)e^{(N+\frac{1}{2})\hat{V}_N(\theta_1,\theta_2,\theta_3)}d\theta_1d\theta_2d\theta_3=O\left(e^{(N+\frac{1}{2})(\zeta_{\mathbb{R}}(p,q)-\epsilon)}\right).
\end{aligned}$$ Combining formulas ([\[formula-integralB2\]](#formula-integralB2){reference-type="ref" reference="formula-integralB2"}) and ([\[formula-integralA1A22\]](#formula-integralA1A22){reference-type="ref" reference="formula-integralA1A22"}) together, we prove ([\[saddle-3\]](#saddle-3){reference-type="ref" reference="saddle-3"}).

By ([\[saddle-1\]](#saddle-1){reference-type="ref" reference="saddle-1"}) ([\[saddle-2\]](#saddle-2){reference-type="ref" reference="saddle-2"}) and ([\[saddle-3\]](#saddle-3){reference-type="ref" reference="saddle-3"}), the required homotopy exists. Hence the assumptions of Proposition [\[proposition-saddlemethod\]](#proposition-saddlemethod){reference-type="ref" reference="proposition-saddlemethod"} holds when we apply the saddle point method to the integral ([\[formula-integralD\'\'\]](#formula-integralD''){reference-type="ref" reference="formula-integralD''"}). ◻
:::
