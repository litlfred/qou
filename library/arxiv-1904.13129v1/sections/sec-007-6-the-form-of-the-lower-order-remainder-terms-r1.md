---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-007-6-the-form-of-the-lower-order-remainder-terms-r1
section_title: "The form of the lower order remainder terms R1 and R2"
section_number: 6
pages: 14-17
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.89
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
---
[]{#sec:remaining parts label="sec:remaining parts"}

We show that the orthogonal projection of the truncated remainder terms of the decomposition of $\delta \mathcal{E}^\alpha$ found in Section [\[section:decomposition\]](#section:decomposition){reference-type="ref" reference="section:decomposition"} can be expressed as multiple integrals of analytic functions.

Let $0 < \varepsilon \leq \frac{1}{2}$, $x\in [0,1]$ and $\gamma \in C^\infty(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ be a simple closed arc-length parametrized curve. We recall that the truncated remainder terms are given by $$\begin{aligned}
(R_1^{\alpha,\varepsilon} \gamma)(x) &= \int_{|w| \in [\varepsilon, \frac{1}{2}]} (\gamma(x+w)-\gamma(x)-w\dot{\gamma}(x)) \left(\frac{1}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} - \frac{1}{ |w|^{\alpha +2}}\right)\mathrm{d} w, \\
(R_2^{\alpha,\varepsilon} \gamma)(x) &= \int_{|w| \in [\varepsilon, \frac{1}{2}]} \ddot{\gamma}(x)\left(\frac{1}{|\gamma(x+w)-\gamma(x)|^{\alpha}} - \frac{1}{ |w|^{\alpha }}\right)\mathrm{d} w
.
\end{aligned}$$

We begin with transforming the more elementary part $P^\perp_{\dot{\gamma}} R_2^{\alpha,\varepsilon} \gamma$.

::: thm
The term $P^\perp_{\dot{\gamma}} R_2^{\alpha,\varepsilon} \gamma$ can be re-written as multiple integral of the form $$\begin{aligned}
    (P^\perp_{\dot{\gamma}} R_2^\varepsilon \gamma )(x) =  
    \int_{|w|\in [\varepsilon, \frac{1}{2}]} 
     \iiiint_{[0,1]^4} (s_1-s_2)^2 \mathsf{G}^{\alpha}_2(\gamma)(x)  \mathrm{d} \phi_1 \mathrm{d} \phi_2 \mathrm{d} s_1 \mathrm{d} s_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}}  ,
    
\end{aligned}$$ where $$\begin{aligned}
    \mathsf{G}^{\alpha}_2(\gamma)(x) 
    &= \mathsf{G}^{\alpha}_2(\gamma)(x;{s_1,s_2,\phi_1,\phi_2,w}) \\    
    &= 
    G^{\alpha}_2\Big(  
    \int_0^1 \dot{\gamma} (x+tw) \mathrm{d} t,
    \dot{\gamma}(x),    \ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_1 w), \\
    &\hspace{3cm}
    \ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_2 w), 
    \ddot{\gamma}(x)  \Big) 
    
\end{aligned}$$ for some analytic function $G_2^\alpha : \mathbb{R}^n \setminus \{0,1\} \times \mathbb{R}^{4n} \rightarrow \mathbb{R}^n$.
:::

::: proof
*Proof.* We begin by computing the first term in the integrand of $R_2^{\alpha,\varepsilon} \gamma$. To do so we use the fundamental theorem of calculus and the arc-length parametrization of the curve $\gamma$ (as in the proof of [@BR13 Prop. 3.2]) to get $$\begin{aligned}
\label{formula:R2gammaint1}
&
\frac{1}{|\gamma(x+w)-\gamma(x)|^\alpha} -  \frac{1}{|w|^\alpha}  \nonumber\\
&\qquad= \frac{|w|^\alpha}{|\gamma(x+w)-\gamma(x)|^\alpha} \frac{1- \frac{|\gamma(x+w)-\gamma(x)|^\alpha}{|w|^\alpha}}{1- \frac{|\gamma(x+w)-\gamma(x)|^2}{w^2}}  \frac{1- \frac{|\gamma(x+w)-\gamma(x)|^2}{w^2}}{|w|^\alpha} \nonumber\\
& \qquad= g_2^\alpha\left(\int_0^1 \dot{\gamma} (x+tw) \mathrm{d} t \right) \frac{2\left(1- \frac{|\gamma(x+w)-\gamma(x)|^2}{w^2}\right)}{|w|^\alpha} \nonumber\\
&\qquad = g_2^\alpha\left(\int_0^1 \dot{\gamma} (x+tw) \mathrm{d} t \right) \frac{\iint_{[0,1]^2} |\dot{\gamma}(x+s_1w)-\dot{\gamma}(x+s_2w)|^2 \mathrm{d} s_1 \mathrm{d} s_2}{|w|^\alpha},
\end{aligned}$$ where $g_2^\alpha(x) = \frac{1}{2|x|^\alpha}\frac{1-|x|^\alpha}{1-|x|^2}$ for all $x\in \mathbb{R}^n \setminus\{0,1\}$ is analytic away from the origin. Since we have by the fundamental theorem of calculus $$\begin{aligned}
\label{formula:R2gammaint2}
& \frac{|\dot{\gamma}(x+s_1w)-\dot{\gamma}(x+s_2w)|^2}{w^2}   
=    \int_0^1 \int_0^1 (s_1 - s_2)^2 \nonumber \\
& \qquad \times \left< \ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_1 w), \ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_2 w) \right>_{\mathbb{R}^n} \mathrm{d} \phi_1 \mathrm{d} \phi_2 ,
\end{aligned}$$ we can express $R_2^{\alpha,\varepsilon} \gamma$ as $$\begin{aligned}
 (R_2^{\alpha,\varepsilon}  \gamma) (x)  
 &=  \int_{|w|\in [\varepsilon, \frac{1}{2}]} \iiiint_{[0,1]^4} (s_1-s_2)^2  \nonumber \\
&\qquad \times  \widetilde{G_2^\alpha}\Big( 
\int_0^1 \dot{\gamma} (x+tw) \mathrm{d} t, 
\ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_1 w), 
\\
&\hspace{3cm}
\ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_2 w), 
\ddot{\gamma}(x)  \Big) 
  \mathrm{d} \phi_1 \mathrm{d} \phi_2 \mathrm{d} s_1 \mathrm{d} s_2  \frac{\mathrm{d} w}{|w|^{\alpha-2}} 
,
\end{aligned}$$ where $\widetilde{G_2^\alpha}: \mathbb{R}^n \setminus \{0,1\} \times \mathbb{R}^{3n}  \rightarrow \mathbb{R}^n$ defined by $\widetilde{G_2^\alpha}(a, x, y, z):= g_2^\alpha(a) \left<x,y \right>_{\mathbb{R}^n} z$ is an analytic function away from the origin in the first variable as well. If we apply the orthogonal projection $P^\perp_{\dot{\gamma}}$ on $R_2^{\alpha,\varepsilon} \gamma$, we finally get the following representation $$\begin{aligned}
(P^\perp_{\dot{\gamma}} R_2^{\alpha,\varepsilon} \gamma )(x) =  \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4} (s_1-s_2)^2 \mathsf{G}^{\alpha}_2(\gamma)(x) \mathrm{d} \phi_1 \mathrm{d} \phi_2 \mathrm{d} s_1 \mathrm{d} s_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}}
,
\end{aligned}$$ where $$\begin{aligned}
\mathsf{G}^{\alpha}_2(\gamma)(x) 
&= \mathsf{G}^{\alpha}_2(\gamma)(x;{s_1,s_2,\phi_1,\phi_2,w}) \\    
&= 
G^{\alpha}_2\Big(  
\int_0^1 \dot{\gamma} (x+tw) \mathrm{d} t,
\dot{\gamma}(x),    \ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_1 w), \\
&\hspace{3cm}
\ddot{\gamma}(x+s_2w + (s_1-s_2)\phi_2 w), 
\ddot{\gamma}(x)  \Big) 
\end{aligned}$$ and $G_2^\alpha : \mathbb{R}^n \setminus \{0,1\} \times \mathbb{R}^{4n} \rightarrow \mathbb{R}^n$ given by $G_2^\alpha (a,v,x,y,z) := P^\perp_{v} \widetilde{G_2^\alpha} (a,x,y,z)$ is clearly analytic. ◻
:::

We use the previous computations to rewrite the orthogonal projection of the first remaining part.

::: thm
[]{#thm:formR1 label="thm:formR1"} The term $P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma$ can be re-written as multiple integral of the form $$\begin{aligned}
    (P^\perp_{\dot{\gamma}} R_1^\varepsilon \gamma )(x) =  
    \int_{|w|\in [\varepsilon, \frac{1}{2}]} 
    \iiiint_{[0,1]^4} (r_1-r_2)^2 \mathsf{G}^{\alpha}_1(\gamma)(x)  \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}}  ,
    
\end{aligned}$$ where $$\begin{aligned}
    \mathsf{G}^{\alpha}_1(\gamma)(x) 
    &= \mathsf{G}^{\alpha}_1(\gamma)(x;{r_1,r_2,\psi_1,\psi_2,w}) \\    
    &= 
    G^{\alpha}_1\Big(\int_0^1 \dot{\gamma} (x+sw) \mathrm{d} s,
    \dot{\gamma}(x), 
    \ddot{\gamma}(x+r_2w + (r_1-r_2)\psi_1 w), \\
    &\hspace{3cm}   
    \ddot{\gamma}(x+r_2w + (r_1-r_2)\psi_2 w), 
    \int_0^1 \ddot{\gamma}(x +tw)(1-t) \mathrm{d}t \Big) 
    
\end{aligned}$$ for some analytic function $G_1^\alpha : \mathbb{R}^n \setminus \{0,1\} \times \mathbb{R}^{4n} \rightarrow \mathbb{R}^n$.
:::

::: proof
*Proof.* By the integral form of the remainder of a first order Taylor approximation, we compute the integrand of $R_1^{\alpha,\varepsilon} \gamma$ as $$\begin{aligned}
\label{formula:R1integrand}
& (\gamma(x+w)-\gamma(x)-w\dot{\gamma}(x)) \left(\frac{1}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} - \frac{1}{ |w|^{\alpha +2}}\right) \nonumber\\
&\qquad =  w^2 \int_0^1 \ddot{\gamma}(x+tw)(1-t) \mathrm{d} t \ \left(\frac{1}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} - \frac{1}{ |w|^{\alpha +2}}\right) \nonumber\\
&\qquad =  \int_0^1 \ddot{\gamma}(x+tw)(1-t) \mathrm{d} t \ \left(\frac{w^2}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} - \frac{1}{ |w|^{\alpha}}\right).
\end{aligned}$$ Thus the last term in [\[formula:R1integrand\]](#formula:R1integrand){reference-type="eqref" reference="formula:R1integrand"} can be expressed as $$\begin{aligned}
\label{formula:R1integrand2}
& \frac{w^2}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} - \frac{1}{ |w|^{\alpha}} \nonumber\\
& \qquad =  \frac{|w|^{\alpha +2}}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} \left(\frac{1-\frac{|\gamma(x+w)-\gamma(x)|^{\alpha +2}}{|w|^{\alpha +2}} }{|w|^\alpha}\right) \nonumber\\
&\qquad  = \frac{|w|^{\alpha +2}}{|\gamma(x+w)-\gamma(x)|^{\alpha +2}} \frac{1-\frac{|\gamma(x+w)-\gamma(x)|^{\alpha +2}}{|w|^{\alpha +2}} }{1-\frac{|\gamma(x+w)-\gamma(x)|^{2}}{|w|^{2}}} \left(\frac{1-\frac{|\gamma(x+w)-\gamma(x)|^{2}}{|w|^{2}} }{|w|^\alpha}\right) \nonumber\\
&\qquad  =g_1^\alpha\left(\int_0^1 \dot{\gamma} (x+sw) \mathrm{d} s \right) \left(\frac{1-\frac{|\gamma(x+w)-\gamma(x)|^{2}}{|w|^{2}} }{|w|^\alpha}\right)
,
\end{aligned}$$ where $g_1^\alpha(x) = \frac{1}{2|x|^{\alpha+2}}\frac{1-|x|^{\alpha+2}}{1-|x|^2}$ for all $x\in \mathbb{R}^n\setminus \{0,1\}$ is analytic away from the origin. By transfering the computations in [\[formula:R2gammaint1\]](#formula:R2gammaint1){reference-type="eqref" reference="formula:R2gammaint1"} and [\[formula:R2gammaint2\]](#formula:R2gammaint2){reference-type="eqref" reference="formula:R2gammaint2"} to the last term in [\[formula:R1integrand2\]](#formula:R1integrand2){reference-type="eqref" reference="formula:R1integrand2"} we find that $$\begin{aligned}
&(R_1^{\alpha,\varepsilon} \gamma) (x) \\
&=  \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4} (r_1-r_2)^2 \\
&\quad\times
 \widetilde{G_1^\alpha} \bigg( \int_0^1 \dot{\gamma}(x+sw)\mathrm{d}s, 
  \ddot{\gamma}(x+r_2w + (r_1-r_2)\psi_1 w), 
  \\
 &\hspace{2cm}
 \ddot{\gamma}(x+r_2w + (r_1-r_2)\psi_2 w), 
 \int_0^1 \ddot{\gamma}(x+tw)(1-t) \mathrm{d} t \bigg) \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \mathrm{d} w
,
\end{aligned}$$ where $\widetilde{G_1^\alpha} : \mathbb{R}^n\setminus \{0,1\} \times \mathbb{R}^{3n} \rightarrow \mathbb{R}^n$ defined by $\widetilde{G_1^\alpha} (a,x,y,z) := g_1^\alpha(a) \left<x,y \right>_{\mathbb{R}^n} z$ is analytic away from 0 and 1 in the first variable.

Finally, by applying the orthogonal projection to $R_1^{\alpha,\varepsilon} \gamma$, we obtain $$\begin{aligned}
(P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma )(x) =  \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4}  (r_1-r_2)^2   \mathsf{G}^{\alpha}_1(\gamma)(x) \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \mathrm{d} w
,
\end{aligned}$$ where $$\begin{aligned}
\mathsf{G}^{\alpha}_1(\gamma)(x) 
&= \mathsf{G}^{\alpha}_1(\gamma)(x;{r_1,r_2,\psi_1,\psi_2,w}) \\    
&= 
G^{\alpha}_1\Big(\int_0^1 \dot{\gamma} (x+sw) \mathrm{d} s,
\dot{\gamma}(x), 
\ddot{\gamma}(x+r_2w + (r_1-r_2)\psi_1 w), \\
&\hspace{3cm}   
\ddot{\gamma}(x+r_2w + (r_1-r_2)\psi_2 w), 
\int_0^1 \ddot{\gamma}(x +tw)(1-t) \mathrm{d}t \Big) 
\end{aligned}$$ and $G_1^\alpha : \mathbb{R}^n \setminus \{0,1\} \times \mathbb{R}^{4n} \rightarrow \mathbb{R}^n$ given by $G_1^\alpha (a,v,x,y,z) := P^\perp_{v} \widetilde{G_2^\alpha} (a,x,y,z)$ is obviously analytic. ◻
:::
