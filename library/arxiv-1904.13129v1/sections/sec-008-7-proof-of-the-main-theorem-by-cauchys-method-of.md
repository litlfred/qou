---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-008-7-proof-of-the-main-theorem-by-cauchys-method-of
section_title: "Proof of the main theorem by Cauchy's method of majorants"
section_number: 7
pages: 17-23
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.976
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — We prove the analyticity of smooth critical points for O’Hara’s knot energies Eα,p, with p = 1 and 2"
---
[]{#sec:mainpart label="sec:mainpart"}

We now turn to the proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"}. Our strategy is to first establish a recursive estimate for $\|\partial^l \gamma \|_{H^{\alpha -1} }$ from which we can infer, by Cauchy's method of majorants, the analyticity of the curve $\gamma$.

Let $m := 1 > \frac{1}{2}$ and $\gamma = (\gamma_1,\ldots, \gamma_n) :\mathbb{R}/ \mathbb{Z}\rightarrow \mathbb{R}^n$ be a simple closed arc-length parametrized curve that is in the class $C^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$. If $\gamma$ is a critical point of $\mathcal{E}^\alpha + \lambda \mathcal{L}$, i.e. if we have $$\begin{aligned}
\delta \mathcal{E}^\alpha(\gamma;h) + \lambda \int_{\mathbb{R}/ \mathbb{Z}} \langle \dot{\gamma}, \dot{h} \rangle \mathrm{d}x = 0
\end{aligned}$$ for all $h\in H^{\frac{\alpha +1}{2},2}(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$, then Theorem [\[thm:1stvar\]](#thm:1stvar){reference-type="ref" reference="thm:1stvar"} and integration by parts imply that the curve $\gamma$ solves the Euler-Lagrange equation $$\begin{aligned}
( H^\alpha\gamma + \lambda \ddot{\gamma},h)_{L^2([0,1], \mathbb{R}^n)} = 0
\end{aligned}$$ for all $h \in  H^{\frac{\alpha +1}{2},2}(\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$. Thus by the decompositions [\[formula:H\]](#formula:H){reference-type="eqref" reference="formula:H"} and [\[formula:Htilde\]](#formula:Htilde){reference-type="eqref" reference="formula:Htilde"} of the gradient of O'Hara's knot energies, we conclude that $$H^\alpha\gamma = \alpha P^\perp_{\dot{\gamma}} Q^\alpha\gamma + 2 \alpha P^\perp_{\dot{\gamma}} R_1^\alpha\gamma  - 2  P^\perp_{\dot{\gamma}} R_3^\alpha
\gamma  + \lambda \ddot{\gamma} \equiv 0$$ on $\mathbb{R}/ \mathbb{Z}$. Moreover, by Corollary [\[kor:Ql\]](#kor:Ql){reference-type="ref" reference="kor:Ql"} with $\beta:= \alpha -2 \in (0,1)$ and the triangle inequality, it follows for any integer $l\geq 0$ that $$\begin{aligned}
\label{formula:partiallgamma}
\|\partial^{l+3} \gamma \|_{H^{1+\beta} } & \leq \widetilde{C} \|\partial^l Q^\alpha\gamma\|_{H^1} \nonumber\\
& = \widetilde{C} \left\| \partial^l \left( \alpha P^T_{\dot{\gamma}} Q^\alpha\gamma  - 2\alpha P^\perp_{\dot{\gamma}} R_1^\alpha\gamma  + 2 P^\perp_{\dot{\gamma}} R_2^\alpha \gamma - \lambda \ddot{\gamma} \right) \right\|_{H^1}   \nonumber\\
& \leq 6\widetilde{C}    ( 
\|\partial^l P^T_{\dot{\gamma}} Q^\alpha\gamma\|_{H^1} 
+ \|\partial^l P^\perp_{\dot{\gamma}} R_1^\alpha\gamma \|_{H^1}  
\nonumber\\ &\hspace{2cm}
+ \|\partial^l P^\perp_{\dot{\gamma}} R_3^\alpha\gamma \|_{H^1} 
+ \lambda \|\partial^{l+2} \gamma \|_{H^1}  ).
\end{aligned}$$ In order to get a recursive estimate on $\|\partial^l \gamma \|_{H^{1+\beta} }$ we aim to derive suitable estimates for the first three terms on the right-hand side of [\[formula:partiallgamma\]](#formula:partiallgamma){reference-type="eqref" reference="formula:partiallgamma"}. To do so for the tangential part of $Q^\alpha$, we use the fractional Leibniz rule from Section [\[sec:bilinearHilberttransform\]](#sec:bilinearHilberttransform){reference-type="ref" reference="sec:bilinearHilberttransform"} in the following:

::: lem
[]{#est:Q label="est:Q"} Let $l\in\mathbb{N}_0$, $\beta:= \alpha -2 \in (0,1)$ for some $2 < \alpha < 3$ and $0<\varepsilon\leq \frac 12$. Then there exists a positive constant $C_{Q^\alpha}$ independent of $\varepsilon$, $\gamma$ and $l$ such that $$\begin{aligned}
    &\|\partial^l P^T_{\dot{\gamma}} Q^{\alpha,\varepsilon}\gamma\|_{H^1} \\
    &\qquad \leq  C_{Q^\alpha} \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  \|\partial^{l-k_1+2} \gamma \|_{H^{1+\beta}} \|\partial^{k_1-k_2+2} \gamma \|_{H^{1+\beta}} \|\partial^{k_2 +1}\gamma \|_{H^1}. 
    
\end{aligned}$$
:::

::: proof
*Proof.* Using formula [\[formula:compTQ\]](#formula:compTQ){reference-type="eqref" reference="formula:compTQ"} and the Leibniz rule twice yields $$\begin{aligned}
    &\partial^l  \Big(P^T_{\dot{\gamma}} Q^{\alpha,\varepsilon}\gamma (x)\Big)\\
    &=  \partial^l \Big(2  \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iint_{[0,1]^2} (1-t) (-t) \frac{\left<\ddot{\gamma}(x+tw), \ddot{\gamma}(x+stw)\right>_{\mathbb{R}^n}}{w |w|^{\alpha-2}} \dot{\gamma}(x) \mathrm{d}s \mathrm{d}t \mathrm{d}w \Big) \\
    &=   2  \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iint_{[0,1]^2} (1-t) (-t) \partial^l \left(\frac{\left<\ddot{\gamma}(x+tw), \ddot{\gamma}(x+stw)\right>_{\mathbb{R}^n}}{w|w|^{\beta}} \dot{\gamma}(x)\right) \mathrm{d}s \mathrm{d}t \mathrm{d}w \\
    &=  2  \int_{|w|\in [\varepsilon, \frac{1}{2}]} \iint_{[0,1]^2} (1-t) (-t) \\
    & \quad \times \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2} \frac{\left<\partial^{l-k_1+2} \gamma(x+tw), \partial^{k_1-k_2+2} \gamma (x+stw)\right>_{\mathbb{R}^n}}{w|w|^{\beta}} \partial^{k_2 +1}\gamma(x) \mathrm{d}s \mathrm{d}t \mathrm{d}w \\ 
    &=  2 \iint_{[0,1]^2} (1-t) (-t)  \\
    & \quad \times \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  \sum_{k=1}^n H_{t,st, \beta}^\varepsilon(\partial^{l-k_1+2} \gamma_k, \partial^{k_1-k_2+2} \gamma_k )(x) \partial^{k_2 +1}\gamma(x) \mathrm{d}s \mathrm{d}t,
    
\end{aligned}$$ where the smoothness of the integrand allows interchanging of integrals and derivative. Then for all $1\leq m \leq n$ we obtain the component-wise estimate $$\begin{aligned}
\label{formula:compQ}
    & \|\partial^l (P^T_{\dot{\gamma}} Q^{\alpha,\varepsilon}\gamma)_m\|_{H^1} \nonumber\\
    & \leq  2 \iint_{[0,1]^2} |1-t| |t|    \nonumber\\
    & \quad   \times \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  \sum_{k=1}^n C_{1} \| H_{t,st,\beta}^\varepsilon(\partial^{l-k_1+2} \gamma_k, \partial^{k_1-k_2+2} \gamma_k )\|_{H^1} \|\partial^{k_2 +1}\gamma_m \|_{H^1} \mathrm{d}s \mathrm{d}t \nonumber\\
    & \leq  2 C_{1} \iint_{[0,1]^2} |1-t| |t|   \nonumber\\
    & \quad  \times \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  \left( \sum_{k=1}^n C_H\|\partial^{l-k_1+2} \gamma_k \|_{H^{1+\beta}} \|\partial^{k_1-k_2+2} \gamma_k \|_{H^{1+\beta}} \right) \|\partial^{k_2 +1}\gamma_m \|_{H^1}  \mathrm{d}s \mathrm{d}t  \nonumber\\
    & \leq  2 C_{1} C_H \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  \|\partial^{l-k_1+2} \gamma \|_{H^{1+\beta}} \|\partial^{k_1-k_2+2} \gamma \|_{H^{1+\beta}} \|\partial^{k_2 +1}\gamma_m \|_{H^1}  
    
\end{aligned}$$ via the Banach algebra property [\[prop:Banachalgebra\]](#prop:Banachalgebra){reference-type="eqref" reference="prop:Banachalgebra"} of $H^1$ and the fractional Leibniz rule for each of the components (i.e. Theorem [\[thm:BilinearHT\]](#thm:BilinearHT){reference-type="ref" reference="thm:BilinearHT"}). The desired statement follows from [\[formula:compQ\]](#formula:compQ){reference-type="eqref" reference="formula:compQ"} and the equivalence between the $1$-norm and the $2$-norm with a finite positive constant $C_{Q^\alpha}:= 2 C_{1} C_H \sqrt{n}$. ◻
:::

Next we estimate the orthogonal projection of the truncated remaining parts $R_1^{\alpha,\varepsilon} \gamma$ and $R_2^{\alpha,\varepsilon} \gamma$. The important ingredients for this are the forms of $P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma$ and $P^\perp_{\dot{\gamma}} R_2^{\alpha,\varepsilon} \gamma$ derived in Chapter [\[sec:remaining parts\]](#sec:remaining parts){reference-type="ref" reference="sec:remaining parts"}, Faà di Bruno's formula and the Banach algebra property of $H^1$.

::: lem
[]{#est:R1 label="est:R1"} Let $l\in\mathbb{N}_0$, $2 < \alpha < 3$, and consider the mapping $f = (f_{1},\ldots, f_{5n})  : \mathbb{R}/ \mathbb{Z}\rightarrow \mathbb{R}^n \setminus \{0,1\} \times \mathbb{R}^{4n}$ given by $$f(x) := (
    \dot{\gamma} (x),
    \dot{\gamma} (x),
    \ddot{\gamma}(x),
    \ddot{\gamma}(x),
    \ddot{\gamma}(x))
    .$$ Then there exist positive constants $C_{R_1^\alpha}$ and $r$ independent of $\varepsilon$, $\gamma$ and $l$ such that the universal polynomials $p_l^{(5n)}$ from the multivariate form of Faà di Bruno's formula. [\[eqn:FdB\]](#eqn:FdB){reference-type="eqref" reference="eqn:FdB"} satisfy $$\begin{aligned}
    \|\partial^l P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma \|_{H^1} 
    &   \leq C_{R_1^\alpha} 
    p_l^{(5n)}\Big(\Big\{\frac{(|\eta|+1)!}{r^{|\eta|+1}} \Big\}_{|\eta| \leq l},
     \Big\{C_1\|f_{i}^{(j)}\|_{H^1} \Big\}_{
    \substack{
    1\leq i \leq 5n \\
           1\leq j \leq l\ \, }      
     }\Big)
    ,
\end{aligned}$$ where $C_1$ is the constant from the estimate [\[prop:Banachalgebra\]](#prop:Banachalgebra){reference-type="eqref" reference="prop:Banachalgebra"} with $m=1$.
:::

::: proof
*Proof.* By Theorem [\[thm:formR1\]](#thm:formR1){reference-type="ref" reference="thm:formR1"} we can express $P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma$ as $$\begin{aligned}
    (P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma )(x) = \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4}  (r_1-r_2)^2  G_1^\alpha (f_1(x)) \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}}
    
\end{aligned}$$ where $G_1^\alpha : \mathbb{R}^n \setminus \{0,1\} \times \mathbb{R}^{4n} \rightarrow \mathbb{R}^n$ is an analytic function and $$\begin{aligned}
    f_1(x) := \begin{pmatrix}
    \int_0^1 \dot{\gamma} (x+sw) \mathrm{d}s \\
    \dot{\gamma} (x) \\
    \ddot{\gamma}(x+r_2w+(r_1-r_2)\psi_1 w) \\
    \ddot{\gamma}(x+r_2w+(r_1-r_2)\psi_2 w))  \\
    \int_0^1 \ddot{\gamma}(x+tw) \mathrm{d}t
    \end{pmatrix}.
    
\end{aligned}$$ Due to the smoothness of the integrand and the generalized Faà di Bruno's formula [\[eqn:FdB\]](#eqn:FdB){reference-type="eqref" reference="eqn:FdB"}, we component-wise find for all $1 \leq k\leq 5n$ that $$\begin{aligned}
    & \partial^l (P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma )_k(x) \\
    & = \partial^l \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4}  (r_1-r_2)^2  G_{1,k}^\alpha (f_1(x)) \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}} \\
    & = \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4}  (r_1-r_2)^2  \partial^l G_{1,k}^\alpha (f_1(x)) \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}} \\
    & = \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4}  (r_1-r_2)^2   \\
    & \hspace{3em} \times p_l^{(5n)}\Big(\{(\partial^\eta G_1^\alpha)_k(f_1(x)) \}_{|\eta| \leq l}, \{f_{1,i}^{(j)}(x) \}_{
\substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, }  
    }\Big) \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}}.
    
\end{aligned}$$ Moreover, by applying the $H^1$-norm on $\partial^l (P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma )$ component-wise for any $1 \leq k \leq 5n$, we find via the Banach algebra property of $H^1$ that $$\begin{aligned}
    &\|\partial^l (P^\perp_{\dot{\gamma}} R_1^{\alpha,\varepsilon} \gamma )_k\|_{H^1}  \\
    & \leq \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4}  |r_1-r_2|^2  \\
    & \hspace{2.5em}\times  
    \Big\|p_l^{(5n)}\Big(
    \{(\partial^\eta G_1^\alpha)_k(f_1) \}_{|\eta| \leq l}, \{f_{1,i}^{(j)} \}_{    
\substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, }             
    }\Big) 
    \Big\|_{H^1} \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}} \\
    & \leq  \int_{|w|\in [\varepsilon, \frac{1}{2}]}  \iiiint_{[0,1]^4}  |r_1-r_2|^2   \\
    & \hspace{2.5em}
    \times  p_l^{(5n)}\Big(
    \{ \left\|(\partial^\eta G_1^\alpha)_k(f_1)\right\|_{H^1} \}_{|\eta| \leq l}, \{C_1\|f_{1,i}^{(j)}\|_{H^1} \}_{
\substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, }         
    }\Big) 
    \mathrm{d} \psi_1 \mathrm{d} \psi_2 \mathrm{d} r_1 \mathrm{d} r_2 \frac{\mathrm{d} w}{|w|^{\alpha-2}} 
    ,
\end{aligned}$$ where the constant $C_1$ appears only in front of $\|f_{1,i}^{(j)}\|_{H^1}$ because of the one-homogeneity of $p_l^{(5n)}$ in its first components.

For any $1\leq j \leq l$ we also observe that $\|f_{1,k}^{(j)}\|_{H^1}  \leq \|f_k^{(j)}\|_{H^1}$ whenever $1\leq k\leq n$, $4n+1\leq k \leq 5n$ and that $\|f_{1,k}^{(j)}\|_{H^1}  = \|f_k^{(j)}\|_{H^1}$ whenever $n+1\leq k\leq 4n$. Moreover, $\|f_k^{(j)}\|_{H^1}$ does not depend on any of the parameters $w,\psi_i, r_i, s, t$ for all $1\leq k\leq 5n$ and $1\leq j \leq l$. In addition, since $G_1^\alpha$ is an analytic function, we can deduce from the proof of [@BV19 Theor. 7.2] that $$\left\|(\partial^\eta G_1^\alpha)(f_1)\right\|_{H^1}  
    \leq \widetilde{C}_{R_1^\alpha}  \frac{(|\eta|+1)!}{r^{|\eta|+1}}$$ for some positive constant $\widetilde{C}_{R_1^\alpha}$ independent of $\varepsilon$, $\gamma$ and $l$.

Now using the elementary estimate $\int_{|w|\in [\varepsilon, \frac{1}{2}]} \frac{\mathrm{d} w}{|w|^{\alpha-2}} \leq \frac{2}{3-\alpha} < \infty$ since $2 < \alpha < 3$ and the fact that $p_l^{(5n)}$ is one-homogeneous in the first components, we finally obtain $$\|\partial^l (P^\perp_{\dot{\gamma}} R_1^\varepsilon \gamma )\|_{H^1} 
     \leq C_{R^\alpha_1} \, p_l^{(5n)}
     \Big(\Big\{  \frac{(|\eta|+1)!}{r^{|\eta|+1}}\Big\}_{|\eta| \leq l}, \Big\{\|C_1f_{i}^{(j)}\|_{H^1} \Big\}_{
     \substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, } 
     }\Big) ,$$ where $C_{R^\alpha_1} := \widetilde{C}_{R_1^\alpha}  \frac{2}{3-\alpha}$ is finite and the right-hand side is independent of $\varepsilon$. ◻
:::

The orthogonal projection of the second remainder term can be estimated along the lines of the previous Lemma [\[est:R1\]](#est:R1){reference-type="ref" reference="est:R1"} to get the following:

::: lem
[]{#est:R2 label="est:R2"} Let $l\in\mathbb{N}_0$ and $f = (\dot{\gamma},\dot{\gamma},\ddot{\gamma}, \ddot{\gamma}, \ddot{\gamma})$ as in Lemma [\[est:R1\]](#est:R1){reference-type="ref" reference="est:R1"}. Then there exist positive constants $C_{R_2^\alpha}$ and $s$ that are independent of $\varepsilon$, $\gamma$ and $l$ such that $$\begin{aligned}
    &\|\partial^l P^\perp_{\dot{\gamma}} R_2^{\alpha,\varepsilon} \gamma \|_{H^1} \leq  C_{R_2^\alpha} \, p_l^{(5n)}\Big(\Big\{  \frac{(|\eta|+1)!}{s^{|\eta|+1}} \Big\}_{|\eta| \leq l}, \Big\{C_1\|f_{i}^{(j)}\|_{H^1} \Big\}_{
         \substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, } 
    }\Big) 
    ,
\end{aligned}$$ where $p_l^{(5n)}$ is the same universal polynomial as in Lemma [\[est:R1\]](#est:R1){reference-type="ref" reference="est:R1"}.
:::

As a direct consequence of the proof of [@BV19 Theor. 7.4] the estimates from Lemmas [\[est:Q\]](#est:Q){reference-type="ref" reference="est:Q"}, [\[est:R1\]](#est:R1){reference-type="ref" reference="est:R1"} and [\[est:R2\]](#est:R2){reference-type="ref" reference="est:R2"} also hold for the limit case $\varepsilon \downarrow 0$.

::: thm
[]{#thm:estimates label="thm:estimates"} Let $l\in\mathbb{N}_0$ and $f = (\dot{\gamma},\dot{\gamma}, \ddot{\gamma}, \ddot{\gamma}, \ddot{\gamma})$ as in Lemma [\[est:R1\]](#est:R1){reference-type="ref" reference="est:R1"}. Then there exist positive constants $r$, $s$, $C_{Q^\alpha}$, $C_{R_1^\alpha}$ and $C_{R_2^\alpha}$ which are independent of $\gamma$ and $l$ such that $$\begin{aligned}
    \|\partial^l P^T_{\dot{\gamma}} Q^\alpha\gamma\|_{H^1}  & \leq  C_{Q^\alpha} \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  \|\partial^{l-k_1+2} \gamma \|_{H^{1+\beta}} \|\partial^{k_1-k_2+2} \gamma \|_{H^{1+\beta}} \|\partial^{k_2 +1}\gamma \|_{H^1} \\
    \|\partial^l P^\perp_{\dot{\gamma}} R_1^\alpha \gamma \|_{H^1}  
    & \leq C_{R_1^\alpha} \, 
    p_l^{(5n)}\Big(\Big\{\frac{(|\eta|+1)!}{r^{|\eta|+1}} \Big\}_{|\eta| \leq l}, 
    \Big\{C_1\|f_{i}^{(j)}\|_{H^1} \Big\}_{
                 \substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, } 
           } \Big)\\
\|\partial^l P^\perp_{\dot{\gamma}} R_2^\alpha \gamma \|_{H^1} 
    &  \leq  C_{R_2^\alpha} \,
    p_l^{(5n)}\Big(\Big\{  \frac{(|\eta|+1)!}{s^{|\eta|+1}} \Big\}_{|\eta| \leq l}, 
    \Big\{C_1\|f_{i}^{(j)}\|_{H^1} \Big\}_{
             \substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, } 
           }\Big)  
,   
\end{aligned}$$ where $\beta := \alpha -2$ for some $2 < \alpha < 3$ and $p_l^{(5n)}$ is the universal polynomial from Lemma [\[est:R1\]](#est:R1){reference-type="ref" reference="est:R1"}.
:::

We are now in a position to give the proof of the main theorem.

::: proof
*Proof of Theorem [\[main\]](#main){reference-type="ref" reference="main"}.* Let $\beta = \alpha -2$ for $2 <\alpha < 3$. Now suppose $\gamma = (\gamma_1,\ldots, \gamma_n):\mathbb{R}/ \mathbb{Z}\rightarrow \mathbb{R}^n$ is a closed simple arc-length parametrized curve in the class $C^\infty (\mathbb{R}/ \mathbb{Z},\mathbb{R}^n)$ which is a stationary point of $\mathcal{E}^\alpha + \lambda \mathcal{L}$. Using the smoothness of the curve $\gamma$, we introduce an auxiliary function $f:\mathbb{R}/ \mathbb{Z}\rightarrow \mathbb{R}^{5n}$ given by $$f(x):= (
    \dot{\gamma}(x) ,
    \dot{\gamma}(x) ,
    \ddot{\gamma}(x) ,
    \ddot{\gamma}(x) , 
    \ddot{\gamma}(x))$$ and define $$a_l :=C_1  \|\partial^l f\|_{H^{1+\beta}}$$ for all integers $l\geq 0$. If we can establish the existence of finite positive constants $\delta$ and $C_\gamma$ such that $$\begin{aligned}
    a_l \leq C_\gamma \frac{l!}{\delta^l} 
    
\end{aligned}$$ we immediately obtain the analyticity of the curve $\gamma$ on $\mathbb{R}/ \mathbb{Z}$ by Corollary [\[cor:TayloranalyticSob\]](#cor:TayloranalyticSob){reference-type="ref" reference="cor:TayloranalyticSob"}.

In order to obtain the desired bounds on $a_l$ we first note that there exists a positive constant $\tilde{C}$ such that $$\begin{aligned}
    \|\partial^{l+3} \gamma \|_{H^{1+\beta} } 
    &\leq \widetilde{C}   \Big( 
    \|\partial^l P^T_{\dot{\gamma}} Q^\alpha\gamma\|_{H^1} 
    + \|\partial^l P^\perp_{\dot{\gamma}} R_1^\alpha\gamma \|_{H^1} \nonumber \\ &\qquad \qquad\quad 
    + \|\partial^l P^\perp_{\dot{\gamma}} R_3^\alpha\gamma \|_{H^1} 
    + \lambda \|\partial^{l+2} \gamma \|_{H^1} \Big)
    
\end{aligned}$$ by the criticality of the curve $\gamma$, the first variation formula of $\mathcal{E}^\alpha$ of Theorem [\[thm:1stvar\]](#thm:1stvar){reference-type="ref" reference="thm:1stvar"}, our decomposition of the first variation of $\mathcal{E}^\alpha + \lambda \mathcal{L}$ and Corollary [\[kor:Ql\]](#kor:Ql){reference-type="ref" reference="kor:Ql"}. Next we deduce from Theorem [\[thm:estimates\]](#thm:estimates){reference-type="ref" reference="thm:estimates"} and the Sobolev embedding of $H^{1+\beta} \subseteq H^1$ that $$\begin{aligned}
    a_{l+1} 
    & =  C_1 \|\partial^{l+1} f\|_{H^{1+\beta}} \\
    &  \leq C_1 (3 \|\partial^{l+3} \gamma \|_{H^{1+\beta}} + 2 \|\partial^{l+2} \gamma \|_{H^{1+\beta}}) \\
    & \leq 3\widetilde{C} C_1 \Big[
    \|\partial^l P^T_{\dot{\gamma}} Q^\alpha\gamma\|_{H^1} 
    + \|\partial^l P^\perp_{\dot{\gamma}} R_1^\alpha\gamma \|_{H^1} \nonumber\\ &\hspace{2cm}
    + \|\partial^l P^\perp_{\dot{\gamma}} R_2^\alpha\gamma \|_{H^1}  
    + \lambda \|\partial^{l+2} \gamma \|_{H^1} \Big] + 2 C_1 a_l\\
    & \leq    3\widetilde{C} C_1 \Big[
    C_{Q^\alpha} \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  
    \|\partial^{l-k_1+2} \gamma \|_{H^{1+\beta}} 
    \|\partial^{k_1-k_2+2} \gamma \|_{H^{1+\beta}} \|\partial^{k_2 +1}\gamma \|_{H^1} \\
    &\hspace{2cm} 
    + C_{R_1^\alpha} p_l^{(5n)}
    \Big(\Big\{ \frac{(|\eta|+1)!}{r^{|\eta|+1}} \Big\}_{|\eta| \leq l},
     \Big\{C_1\|f_{i}^{(j)}\|_{H^1} \Big\}_{
                 \substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, } 
           }\Big) \\
    & \hspace{2cm}\qquad 
    +  C_{R_2^\alpha} p_l^{(5n)}\Big(\Big\{\frac{(|\eta|+1)!}{s^{|\eta|+1}}  \Big\}_{|\eta| \leq l}, \Big\{C_1 \|f_{i}^{(j)}\|_{H^1} \Big\}_{
                 \substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, } 
           }\Big) \\
           &\hspace{2cm}\qquad\qquad  
           + \lambda \|\partial^{l+2} \gamma \|_{H^1} \Big]
            + 2 C_1 a_l.
    
\end{aligned}$$ Therefore, by the embedding of $H^{1+\beta} \subseteq H^1$ again, there exist positive constants $C > 1$ and $r_\gamma$ independent of $\gamma$ and $l$ such that $$\begin{aligned}
\label{formula:al+1}
    a_{l+1} 
    & \leq   C \Big[
    \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}  
    a_{l-k_1} a_{k_1-k_2} a_{k_2} \nonumber\\ &\hspace{3cm}
     + p_l^{(5n)}\Big(\Big\{ \frac{(|\eta|+1)!}{r_\gamma^{|\eta|+1}}\Big\}_{|\eta| \leq l}, \Big\{ a_j \Big\}_{1\leq j \leq l}\Big)  
     + a_l \Big] .
    
\end{aligned}$$ To apply Cauchy's method of majorants, we define a majorant $F: \mathbb{R}^{5n} \rightarrow \mathbb{R}^{5n}$ component-wise by setting $$\begin{aligned}
    F_i(y) := C \Big( y_i^3 + \frac{1 }{(1 +\frac{ 5na_0 -  (y_1 + \cdots + y_{5n})}{r_\gamma})^2} + y_i\Big) 
    
\end{aligned}$$ for any $y = (y_1,\ldots,y_{5n})\in \mathbb{R}^{5n}$ and all $1\leq i \leq 5n$. It is clearly analytic around $a_0 (1,\ldots, 1)$. Moreover, we consider the following initial value problem $$\begin{aligned}
\label{formula:ODE}
    \begin{split}
    \dot{c}(t) &= F( c(t)), \\
    c(0) &= a_0 (1,\ldots, 1).
    \end{split}
    
\end{aligned}$$ and note that the ODE has a unique smooth solution $c:     (-\varepsilon, \varepsilon) \to \mathbb{R}^{5n}$ that is also analytic around $0$ for some $\varepsilon >0$ by Theorem [\[CK\]](#CK){reference-type="ref" reference="CK"}. Hence we can write $c=c(t)$ as a Taylor series in a neighbourhood of $0$, i.e. $$\begin{aligned}
    c (t):= \sum_{k=0}^{\infty} \frac{\widetilde{a}_{k} (1,\ldots, 1)}{k!}  t^k 
    
\end{aligned}$$ where $\widetilde{a}_{k} (1,\ldots, 1)= c^{(k)}(0)$. Then by Theorem [\[thm:Tayloranalytic\]](#thm:Tayloranalytic){reference-type="ref" reference="thm:Tayloranalytic"} we can, for all $t\in B_{r_c}(0)$, bound $$\begin{aligned}
\label{formula:canalytic}
    |c^{(l)}(t)| \leq M \frac{l!}{r_c^l}
    
\end{aligned}$$ for some finite positive constants $r_c$ and $M$ which are independent of any integer $l\geq 0$. By applying the Leibniz rule and Faà di Bruno's formula [\[eqn:FdB\]](#eqn:FdB){reference-type="eqref" reference="eqn:FdB"} we have that $$\begin{aligned}
    &\partial^l F_i(c(t)) \\
    &=  C \Big[
    \sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}   c_i^{(l-k_1)}(t)  c_i^{(k_1-k_2)}(t) c_i^{(k_2)}(t) \\
    &\quad
 +p_l^{(5n)}\Big(
 \Big\{ \frac{(|\eta|+1)!}{r_\gamma^{|\eta|+1}} 
 \frac{1}{\left(1 + \left( \frac{5na_0}{r_\gamma} -\frac{\left(c_1(t) + \cdots + c_{5n}(t)\right)}{r_\gamma}\right)\right)^{|\eta|+2}} 
 \Big\}_{|\eta| \leq l}, \Big\{ c_i^{(j)}(t) \Big\}_{
                 \substack{
1\leq i \leq 5n \\
           1\leq j \leq l\ \, } 
           }\Big)\\
    &\quad\qquad + c_i^{(l)} (t) \Big]
    
\end{aligned}$$ for any $1\leq i\leq 5n$ and $l\in\mathbb{N}_0$. Then by considering the initial condition [\[formula:ODE\]](#formula:ODE){reference-type="eqref" reference="formula:ODE"} we find that $$\begin{aligned}
\label{formula:tildeal+1}
    \tilde a_{l+1} 
& = \partial^l F_i (c(0)) \nonumber\\
&=  C \Big[  
\sum_{k_1=0}^l \sum_{k_2=0}^{k_1} \binom{l}{k_1} \binom{k_1}{k_2}   
\tilde a_{l-k_1} \tilde a_{k_1-k_2} \tilde a_{k_2} \nonumber\\ &\hspace{2cm} 
     + p_l^{(5n)}\Big(\Big\{ \frac{(|\eta|+1)!}{r_\gamma^{|\eta|+1}} \Big\}_{|\eta| \leq l}, \Big\{\tilde a_j \Big\}_{1\leq j \leq l}\Big) + \tilde a_l  \Big]
    .
\end{aligned}$$ Finally an induction argument obtained from comparing [\[formula:al+1\]](#formula:al+1){reference-type="eqref" reference="formula:al+1"} and [\[formula:tildeal+1\]](#formula:tildeal+1){reference-type="eqref" reference="formula:tildeal+1"}, together with the fact that Faà di Bruno's polynomials $p_l$ [\[eqn:FdB\]](#eqn:FdB){reference-type="eqref" reference="eqn:FdB"} have non-negative coefficients and the initial condition $a_0 = \widetilde{a}_0$, gives $$\begin{aligned}
    a_l  \leq \widetilde{a}_{l}. 
    
\end{aligned}$$ Then by [\[formula:canalytic\]](#formula:canalytic){reference-type="eqref" reference="formula:canalytic"} we conclude that $\|\partial^{l+1} \gamma \|_{H^{1+\beta}} \leq a_l \leq M\frac {l!}{r_C^l}$ for all $l\in\mathbb{N}_0$ which, by Corollary [\[cor:TayloranalyticSob\]](#cor:TayloranalyticSob){reference-type="ref" reference="cor:TayloranalyticSob"}, implies the analyticity of the curve $\gamma$. ◻
:::
