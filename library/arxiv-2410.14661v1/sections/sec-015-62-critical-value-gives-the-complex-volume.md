---
doc_id: arxiv-2410.14661v1
doc_title: "ON THE ASYMPTOTIC EXPANSION OF VARIOUS QUANTUM INVARIANTS III: THE RESHETIKHIN-TURAEV INVARIANTS OF CLOSED HYPERBOLIC 3-MANIFOLDS OBTAINED BY DOING INTEGRAL SURGERY ALONG THE TWIST"
section_id: sec-015-62-critical-value-gives-the-complex-volume
section_title: "Critical value gives the complex volume"
section_number: 6.2
pages: 43-45
source_pdf: 2410.14661v1.pdf
source_sha256: 3362fcd5e28eb1f0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.625
latex_coverage_ratio: 0.81
---
Recall that $$\begin{aligned}
    \hat{V}&=\pi\sqrt{-1}\left(\frac{3}{2}q+\frac{q}{2}\theta_1^2-\theta_1^2-\theta_1-2\theta_2-(2p+3)\theta_3+(2p+1)\theta_3^2\right)\\\nonumber
    &+\frac{1}{2\pi\sqrt{-1}}\left(\frac{\pi^2}{6}-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})\right.\\\nonumber
    &\left.+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})\right).
\end{aligned}$$ The critical point equations of $\hat{V}$ are given by $$\begin{aligned}
 \label{equation-Vs}
\hat{V}_{\theta_1}=\pi\sqrt{-1}(q\theta_1-2\theta_1-1)+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})=0,
\end{aligned}$$ $$\begin{aligned}
  \label{equation-Vt}
\hat{V}_{\theta_2}&=-2\pi\sqrt{-1}-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})\\\nonumber
&+\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})+\log(1-e^{2\pi\sqrt{-1}\theta_2})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})=0,    
\end{aligned}$$ and $$\begin{aligned}
 \label{equation-Vu}
\hat{V}_{\theta_3}&=\pi\sqrt{-1}((4p+2)\theta_3-(2p+3))-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})\\\nonumber&+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})=0.    
\end{aligned}$$

By equation ([\[equation-Vs\]](#equation-Vs){reference-type="ref" reference="equation-Vs"}), we have $$\begin{aligned}
&q(-2\pi\sqrt{-1}\theta_1)+4\pi\sqrt{-1}\theta_1+2\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\\\nonumber
&-2\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})=-2\pi\sqrt{-1}.    
\end{aligned}$$ Comparing to the equation ([\[equantion-geom1\]](#equantion-geom1){reference-type="ref" reference="equantion-geom1"}), we must have $$\begin{aligned}
 \label{equation-s}
    \log (w-1)+\log x+\log y-\log(y-1)=-\pi\sqrt{-1}(2\theta_1+1)
\end{aligned}$$ and $$\begin{aligned}
\log x+\log y=\pi\sqrt{-1}(2\theta_1-1)+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})    
\end{aligned}$$ By equation ([\[equation-Vu\]](#equation-Vu){reference-type="ref" reference="equation-Vu"}), we have $$\begin{aligned}
  &p2\pi\sqrt{-1}(2\theta_3-1)+\pi\sqrt{-1}(2\theta_3-1)-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})\\\nonumber
  &+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})=2\pi\sqrt{-1}.  
\end{aligned}$$ Comparing to equation ([\[equantion-geom1\]](#equantion-geom1){reference-type="ref" reference="equantion-geom1"}), we have $$\begin{aligned}
 \label{equation-u}
 \log x+\log z=2\pi\sqrt{-1}(\theta_3-1)
\end{aligned}$$ and $$\begin{aligned}
  &-\log(w-1)-\log x-\log z+\log(z-1)\\\nonumber
  &=2\pi\sqrt{-1}\theta_3-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}).   
\end{aligned}$$ In conclusion, we have the correspondence $$\label{equation-corresponding}
\left\{ \begin{aligned}
         &\log (w-1)+\log x+\log y-\log(y-1)=-\pi\sqrt{-1}(2\theta_1+1), \\
          &       \log x+\log y=\pi\sqrt{-1}(2\theta_1-1)+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_1)}), \\
          &  \log x+\log z=2\pi\sqrt{-1}(\theta_3-1),\\
          &-\log(w-1)-\log x-\log z+\log(z-1),\\\nonumber
  &=2\pi\sqrt{-1}\theta_3-\log(1-e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\log(1-e^{2\pi\sqrt{-1}(\theta_2-\theta_3)}). 
                          \end{aligned} \right.$$

Then we will prove the following identity.

::: theorem
[]{#theorem-critical=volume label="theorem-critical=volume"} Suppose $(\theta_1^0,\theta_2^0,\theta_3^0)$ is a solution of the critical point equations ([\[equation-Vs\]](#equation-Vs){reference-type="ref" reference="equation-Vs"}), ([\[equation-Vt\]](#equation-Vt){reference-type="ref" reference="equation-Vt"}) and ([\[equation-Vu\]](#equation-Vu){reference-type="ref" reference="equation-Vu"}), and for $(p,q)\in S$, then we have $$\begin{aligned}
2\pi \hat{V}(p,q;\theta_1^0,\theta_2^0,\theta_3^0)=Vol(M_{p,q})+\sqrt{-1}CS(M_{p,q})+(3q-p-7)\pi^2\sqrt{-1}.    
\end{aligned}$$
:::

For convenience, we introduce two variables $\gamma_1=\frac{1}{p}, \gamma_2=\frac{1}{q}$. Suppose $(\theta_1,\theta_2,\theta_3)$ is solution of the critical point equations ([\[equation-Vs\]](#equation-Vs){reference-type="ref" reference="equation-Vs"}), ([\[equation-Vt\]](#equation-Vt){reference-type="ref" reference="equation-Vt"}) and ([\[equation-Vu\]](#equation-Vu){reference-type="ref" reference="equation-Vu"}), the the corresponding $(x,y,z,w)$ by formula ([\[equation-corresponding\]](#equation-corresponding){reference-type="ref" reference="equation-corresponding"}) is a solution to the geometric equation ([\[equantion-geom1\]](#equantion-geom1){reference-type="ref" reference="equantion-geom1"}). Then both $\hat{V}$ and $Vol(M_{p,q})+\sqrt{-1}CS(M_{p,q})$ can be regarded as a function of $\gamma_1, \gamma_2$.

So we define $$\begin{aligned}
 \label{formula-Fgamma1gamma2}
&F(\gamma_1,\gamma_2)\\\nonumber
&=\pi^2\sqrt{-1}\left(-2\theta_1+\frac{1}{\gamma_2}\theta_1^2-2\theta_1^2-4\theta_2-2\left(\frac{2}{\gamma_1}+3\right)\theta_3+2\left(\frac{2}{\gamma_1}+1\right)u^2\right)\\\nonumber
&+\left(\frac{1}{\gamma_1}+7\right)\pi^2\sqrt{-1}+\frac{1}{\sqrt{-1}}\left(\frac{\pi^2}{6}+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_3)})+\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_3)})\right.\\\nonumber
&\left.-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2+\theta_1)})-\text{Li}_2(e^{2\pi\sqrt{-1}\theta_2})-\text{Li}_2(e^{2\pi\sqrt{-1}(\theta_2-\theta_1)})\right).    
\end{aligned}$$ and $$\begin{aligned}
  \label{formula-Ggamma1gamma2}
G(\gamma_1,\gamma_2)&=-\frac{1}{\sqrt{-1}}\left(R(w)+R(x)+R\left(\frac{1}{1-y}\right)+R\left(\frac{1}{1-z}\right)\right)\\\nonumber
&-\frac{\pi}{2}\left(-2\pi\sqrt{-1}-(\log(w-1)+\log(x)+\log(y)-\log(y-1)+\pi\sqrt{-1})\right.\\\nonumber
&\left.+\gamma_1(2\pi\sqrt{-1}+\log(w-1)+\log(x)+\log(z)-\log(z-1)+\pi\sqrt{-1})\right)  
\end{aligned}$$

Therefore, in order to prove Thereom [\[theorem-critical=volume\]](#theorem-critical=volume){reference-type="ref" reference="theorem-critical=volume"}, we only need to prove the following identity.

$$\begin{aligned}
 \label{identity-criticalvolume}
F(\gamma_1,\gamma_2)=G(\gamma_1,\gamma_2)    
\end{aligned}$$

By some tedious calculations of the derivatives, we can prove that $$\begin{aligned}
 F_{\gamma_1}(\gamma_1,\gamma_2)=G_{\gamma_1}(\gamma_1,\gamma_2), \ F_{\gamma_2}(\gamma_1,\gamma_2)=G_{\gamma_2}(\gamma_1,\gamma_2)    
\end{aligned}$$ and $F(0,0)=G(0,0)$, hence we finish the proof of Theorem [\[theorem-critical=volume\]](#theorem-critical=volume){reference-type="ref" reference="theorem-critical=volume"}.

We introduce $$\begin{aligned}
\zeta(p,q)=\hat{V}(p,q;\theta_1^0,\theta_2^0,\theta_3^0),     
\end{aligned}$$ and $$\begin{aligned}
\zeta_{\mathbb{R}}(p,q)=\text{Re}\hat{V}(p,q;\theta_1^0,\theta_2^0,\theta_3^0).     
\end{aligned}$$

::: corollary
[]{#corollary-zetaR label="corollary-zetaR"} For $(p,q)\in S_{p,q}$, we have $$\begin{aligned}
2\pi \zeta_{\mathbb{R}}(p,q)>3.56337.
\end{aligned}$$
:::

::: proof
*Proof.* One can compute that when $(p,q)\in S$, we have $$\begin{aligned}
    Vol\left(M_{p,q}\right)>3.56337. 
\end{aligned}$$ According to Theorem [\[theorem-critical=volume\]](#theorem-critical=volume){reference-type="ref" reference="theorem-critical=volume"}, we have $$\begin{aligned}
  2\pi \zeta_{\mathbb{R}}(p,q)=Vol\left(M_{p,q}\right).   
\end{aligned}$$ ◻
:::

## Proof of Proposition [\[prop-critical\]](#prop-critical){reference-type="ref" reference="prop-critical"} {#Appendix-criticalexists}

The proof of this Proposition is similar to the proof of Proposition 5.3 in [@CZ23-1].

::: lemma
[]{#lemma-t0s0 label="lemma-t0s0"} Suppose $(\theta_1^0,\theta_2^0,\theta_3^0)$ is a critical point of $\hat{V}(\theta_1,\theta_2,\theta_3)$ with $(\text{Re}(\theta_1^0),\text{Re}(\theta_2^0),\text{Re}(\theta_3^0))\in D_0$, then we have $(\text{Re}(\theta_1^0),\text{Re}(\theta_2^0),\text{Re}(\theta_3^0))\in U_0$.
:::

::: proof
*Proof.* Suppose $\theta_i^0=\theta_{iR}^0+X_i^0\sqrt{-1}$, $(i=1,2,3)$ is a critical point of $\hat{V}$ with $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)\in D_0$, i.e.

$$\label{formula-criticalpoint}
\left\{ \begin{aligned}
         &\frac{\partial \hat{V}}{\partial \theta_1}(\theta_{1}^0,\theta_{2}^0,\theta_{3}^0)=0,  \\
         & \frac{\partial \hat{V}}{\partial \theta_2}(\theta_{1}^0,\theta_{2}^0,\theta_{3}^0)=0. \\ 
         & \frac{\partial \hat{V}}{\partial \theta_3}(\theta_{1}^0,\theta_{2}^0,\theta_{3}^0)=0
                          \end{aligned}\right.$$

We will prove that $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)\in U_0$. Note that $$\begin{aligned}
    \frac{\partial f}{\partial X_i}&=\frac{\partial \text{Re} \hat{V}(\theta_1+X_1\sqrt{-1},\theta_2+X_2\sqrt{-1},\theta_3+X_3\sqrt{-1})}{\partial X_2}\\\nonumber
    &=\text{Re} \left(\sqrt{-1}\frac{\partial \hat{V}(\theta_1+X_1\sqrt{-1},\theta_2+X_2\sqrt{-1},\theta_3+X_3\sqrt{-1})}{\partial \theta_i}\right)\\\nonumber
    &=-\text{Im} \left(\frac{\partial \hat{V}}{\partial \theta_i}\right),
\end{aligned}$$

According to the equation ([\[formula-criticalpoint\]](#formula-criticalpoint){reference-type="ref" reference="formula-criticalpoint"}), we obtain $$\begin{aligned}
 \label{equation:critical}
    \frac{\partial \hat{f}}{\partial X_i}(\theta_{1R}^0+X_1^0\sqrt{-1},\theta_{2R}^0+X_2^0\sqrt{-1},\theta_{3R}^0+X_3^0\sqrt{-1})&=0,  
\end{aligned}$$

By a straightforward computation, we obtain $$\begin{aligned}
    \frac{\partial \hat{f}}{\partial X_1}&=-\pi(q-2)\theta_1+\pi-\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2+\theta_1+(X_1+X_2)\sqrt{-1}\right)})\\\nonumber
    &+\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2-\theta_1+(X_2-X_1)\sqrt{-1}\right)}),
\end{aligned}$$

$$\begin{aligned}
    \frac{\partial \hat{f}}{\partial X_2}&=2\pi+\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2+\theta_3+(X_2+X_3)\sqrt{-1}\right)})\\\nonumber
    &+\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2-\theta_3+(X_2-X_3)\sqrt{-1}\right)})+\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2-\theta_1+(X_2-X_1)\sqrt{-1}\right)})\\\nonumber
    &-\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2+\theta_1+(X_2+X_1)\sqrt{-1}\right)})-\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2+X_2\sqrt{-1}\right)})\\\nonumber
    &-\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2-\theta_1+(X_2-X_1)\sqrt{-1}\right)}),
\end{aligned}$$

$$\begin{aligned}
\frac{\partial \hat{f}}{\partial X_3}&=-\pi(4p+2)\theta_3+(2p+3)\pi+\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2+\theta_3+(X_2+X_3)\sqrt{-1}\right)})\\\nonumber
&-\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2-\theta_3+(X_2-X_3)\sqrt{-1}\right)}).
\end{aligned}$$

Furthermore, for $0<\theta_2\pm \theta_3-1<\frac{1}{2}$, then $$\begin{aligned}
2\pi\left(\theta_2\pm \theta_3-\frac{3}{2}\right)<\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2\pm \theta_3+(X_2\pm X_3)\sqrt{-1}\right)})<0    
\end{aligned}$$ and for $\frac{1}{2}<\theta_2\pm \theta_3-1<1$, then $$\begin{aligned}
0<\text{arg}(1-e^{2\pi\sqrt{-1}\left(\theta_2\pm \theta_3+(X_2\pm X_3)\sqrt{-1}\right)})<2\pi\left(\theta_2\pm \theta_3-\frac{3}{2}\right)    
\end{aligned}$$

By using the equation ([\[equation:critical\]](#equation:critical){reference-type="ref" reference="equation:critical"}), we get that if $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)\in D_{0}$, then $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)\in  D_{H}$. Then $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)$ must lie in $U_0$. Since if $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)\in D_{H}\setminus U_0$, by Proposition [\[proposition-Hessianf\]](#proposition-Hessianf){reference-type="ref" reference="proposition-Hessianf"}, the Hessian matrix $\hat{f}(X_1,X_2,X_3)$ is positive definite on $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)$, and $(X_1^0,X_2^0,X_3^0)$ is a critical point of $\hat{f}(X_1,X_2,X_3)$. On the other hand, by Lemma , we have that $f(X_1,X_2,X_3)\rightarrow -\infty$ in some direction of $X_1^2+X_2^2+X_3^2\rightarrow \infty$. It is a contradiction. Hence $(\theta_{1R}^0,\theta_{2R}^0,\theta_{3R}^0)\in U_0$. ◻
:::

Note that it is easy to generalize Lemmas 6.5-6.9 in [@CZ23-1] to be used in our case. Then we can finish the proof as in [@CZ23-1].
