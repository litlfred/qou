---
doc_id: arxiv-2111.06645v3
doc_title: "Knots, Perturbative Series and Quantum Modularity"
section_id: sec-031-73-state-sums
section_title: "State-sums"
section_number: 7.3
pages: 55-57
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
toc_source: outline
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.995
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α 7→Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
[]{#sub.statesum label="sub.statesum"}

In this subsection, we explain where the formulas just given come from. More precisely, we discuss a heuristic method to discover a formula for the first column of the matrix $\mathbf{J}^{(5_2)}$ given a formula for its top entry i.e., for the Kashaev invariant of the knot. This method produces periodic functions similar to the constant term of the formal power series discussed in Section [\[sec.perturbation\]](#sec.perturbation){reference-type="ref" reference="sec.perturbation"}. It also generalizes to the further columns, by replacing the Kashaev invariant by the other in its top row (i.e., in the row of the matrix that is expected always to have entries belonging to the rational Habiro ring), thus producing predictions for the entire matrix $\mathbf{J}$. This is useful in particular for the numerical confirmation of the generalized quantum modularity conjecture.

Our starting point is the formula [\[Kashaev.52\]](#Kashaev.52){reference-type="eqref" reference="Kashaev.52"} for the Kashaev invariant of the $5_2$ knot. Let $$b_{k,\ell}(q) =q^{-(\ell+1)k} \frac{(q;q)_\ell^2}{\big(q^{-1};q^{-1}\big)_k}$$ denote the summand of the Kashaev invariant of $5_2$ in equation [\[Kashaev.52\]](#Kashaev.52){reference-type="eqref" reference="Kashaev.52"}. The function $b_{k,\ell}(q)$ (which is proper $q$-hypergeometric in the sense of [@WZ]) satisfies the linear $q$-difference equations $$\begin{gathered}
\label{eq.b1}
\frac{b_{k+1,\ell}(q)}{b_{k,\ell}(q)} = q^{-\ell} \big(1-q^{k+1}\big)^2,
\qquad
\frac{b_{k,\ell+1}(q)}{b_{k,\ell}(q)} = q^{-(k+1)} \frac{1}{1-q^{-\ell-1}},
\end{gathered}$$ whose right-hand sides are in $\mathbb Q\big(q,q^k,q^\ell\big)$. It follows that for natural numbers $r$, $s$ we have $$\frac{b_{k+r,\ell}(q)}{b_{k,\ell}(q)} = q^{-r\ell} \big(q^{k+1};q\big)_r^2,
\qquad
\frac{b_{k,\ell+s}(q)}{b_{k,\ell}(q)} = q^{-(k+1)s} \frac{1}{\big(q^{-\ell-1};q^{-1}\big)}$$ and hence $$\begin{aligned}

\frac{b_{k+r,\ell+s}(q)}{b_{k,\ell}(q)} &= q^{-k s -r \ell-(r+1)s}
\frac{\big(q^{k+1};q\big)_r^2}{\big(q^{-\ell-1};q^{-1}\big)_s} .
\end{aligned}$$ Setting $q^k=z_1$, $q^\ell=z_2$, $q=1$ and equating the ratios of equations [\[eq.b1\]](#eq.b1){reference-type="eqref" reference="eq.b1"} to $1$, we get the gluing equations for $(z_1,z_2)$ $$\label{eq.ge}
z_2^{-1}(1-z_1)^2=1, \qquad z_1^{-1}\big(1-z_2^{-1}\big)^{-1}=1 .$$ Although the summation for the Kashaev invariant when $q$ is a primitive $N$-th root of unity is a subset of $[0,N-1]^2$ and when $\big(q^k,q^\ell\big)$ is near $(z_1,z_2)$ is outside the summation range, we will pretend that we have performed analytic continuation. Choose $\zeta=\mathbf{e}(a/c)$ where $(a,c)=1$ and ${c>0}$ and . In other words, we choose $\theta_i$ to be arbitrary $c$-th roots of $z_i$ ($i=1,2$). Then we can define $a_{r,s}(\theta_1,\theta_2;\zeta)$ by $$\begin{aligned}
 a_{r,s}(\theta_1,\theta_2;\zeta)&=
\frac{b_{k+r,\ell+s}(q)}{b_{k,\ell}(q)} \big|_{q^k=\theta_1, q^\ell=\theta_2, q=\zeta} = \zeta^{-(r+1)s} \theta_1^{-s} \theta_2^{-r}
\frac{(\zeta \theta_1;\zeta)_r^2 }{\big(\zeta^{-1}\theta_2^{-1};\zeta^{-1}\big)_s} .
\end{aligned}$$ The principle of equipeaked Gaussians in the asymptotics of $J(\gamma X)$ with $\gamma=\bigl(\smallmatrix a&b\\c&s\endsmallmatrix\bigr) \in \mathrm{SL}_2(\mathbb Z)$ (as used in Section [\[sub.proof41\]](#sub.proof41){reference-type="ref" reference="sub.proof41"} for the case of the $4_1$ knot) suggests the expression $$\begin{aligned}
\label{eq.a1}
S(\theta_1,\theta_2;\zeta)=\sum_{r,s=0}^{c-1} a_{r,s}(\theta_1,\theta_2) .
\end{aligned}$$ The first observation is that the sum in equation [\[eq.a1\]](#eq.a1){reference-type="eqref" reference="eq.a1"} is $c$-periodic, i.e., that $r,s \in \mathbb Z/c\mathbb Z$. This follows from the fact that $(z_1,z_2)$ satisfy the gluing equations [\[eq.ge\]](#eq.ge){reference-type="eqref" reference="eq.ge"}. A second observation, which we will not make use of, if the fact that $b_{k,\ell}(q)$ determines $a_{r,s}(\theta_1,\theta_2)$ according to the above definitions. Conversely, $a_{r,s}(\theta_1,\theta_2;\zeta)$ determines $b_{k,\ell}(q)$ by $a_{r,s}(1,1;\zeta)=b_{r,s}(\zeta)$. A curious consequence of this is that $S(1,1;\zeta)=J(\zeta)$ recovers the Kashaev invariant. The gluing equations [\[eq.ge\]](#eq.ge){reference-type="eqref" reference="eq.ge"} can be solved as follows: $z_1=-\xi^{-3}$, $z_2=\xi^{-2}$, where $\xi^3-\xi^2+1=0$. The three solutions give rise to the three embeddings of the trace field of $5_2$ into the complex numbers. For ${\zeta=\mathbf{e}(a/c)}$, let $F_c=F(\zeta)$ and $F_{G,c}=F_c(\theta_1,\theta_2)$, giving extensions $F \subset F_c \subset F_{G,c}$, where $F_{G,c}/F_c$ is an abelian Galois (Kummer) extension with group $(\mathbb Z/c\mathbb Z)^2$ and $S(\theta_1,\theta_2) \in F_{G,c}$. To find how $S(\theta_1,\theta_2;\zeta)$ transform under the Galois group, we compute $$\begin{aligned}
 \frac{a_{r,s}(\zeta \theta_1,\theta_2;\zeta)}{a_{r+1,s}(\theta_1,\theta_2;\zeta)}
 &= \theta_2 (1-\zeta \theta_1)^{-2} = a_{1,0}(\theta_1,\theta_2;\zeta)^{-1},\\
 \frac{a_{r,s}(\theta_1,\zeta \theta_2;\zeta)}{a_{r,s+1}(\theta_1,\theta_2;\zeta)}
 &= \zeta \theta_1\big(1-\zeta^{-1}\theta_2^{-1}\big) = a_{0,1}(\theta_1,\theta_2;\zeta)^{-1}
\end{aligned}$$ (where the left-hand side of the above equations is independent of $r$ and $s$ hence it must equal to the right-hand side). Since the sum in equation [\[eq.a1\]](#eq.a1){reference-type="eqref" reference="eq.a1"} is $c$-periodic, it follows that $$\label{eq.Sq1Sq2}
\begin{align}
\label{eq.Sq1}
 S(\zeta \theta_1,\theta_2;\zeta) &= S(\theta_1,\theta_2;\zeta) \theta_2 (1-\zeta \theta_1)^{-2}
 = S(\theta_1,\theta_2;\zeta)a_{1,0}(\theta_1,\theta_2;\zeta)^{-1},\\
\label{eq.Sq2}
 S(\theta_1, \zeta \theta_2;\zeta) &= S(\theta_1,\theta_2;\zeta) \zeta \theta_1 \big(1-\zeta^{-1} \theta_2^{-1}\big)
 =S(\theta_1,\theta_2)a_{0,1}(\theta_1,\theta_2;\zeta)^{-1}.
\end{align}$$ To fix the Galois invariance of $S(\theta_1,\theta_2;\zeta)$, we consider the product $$P(\theta_1,\theta_2;\zeta) = \prod_{r=0}^{c-1} \big(1-\zeta^{r+1} \theta_1\big)^{2r}
\prod_{s=0}^{c-1} \big(1-\zeta^{-s-1}\theta_2^{-1}\big)^{-s}.$$ We can rewrite the above product using the cyclic quantum dilogarithm function [\[Dm\]](#Dm){reference-type="eqref" reference="Dm"} as follows $$\begin{gathered}
\label{eq.PD}
P(\theta_1,\theta_2;\zeta)
= z_1^{-1} z_2^{-1}
\frac{D_\zeta(\theta_1)^2}{D_{\zeta^{-1}}\big(\theta_2^{-1}\big)} .
\end{gathered}$$ From the transformation property for the cyclic quantum dilogarithm $$\frac{D_\zeta(x)}{D_\zeta\big(\zeta^{-1}x\big)} =\frac{(1-x)^c}{1-x^c}, \qquad
D_\zeta(x) D_{\zeta^{-1}}(x) = (1-x^c)^c(1-x)^c$$ and the fact that $(z_1,z_2)$ solve the gluing equations [\[eq.ge\]](#eq.ge){reference-type="eqref" reference="eq.ge"}, we obtain that $$\label{eq.Ps1Ps2}
\begin{align}
\label{eq.Ps1}
P(\zeta \theta_1, \theta_2;\zeta) &=
P(\theta_1,\theta_2;\zeta) \big( \theta_2^{-1} (1-\zeta \theta_1)^{2} \big)^c
= P(\theta_1,\theta_2;\zeta)  a_{1,0}(\theta_1,\theta_2;\zeta)^c, \\
\label{eq.Ps2}
P(\theta_1, \zeta \theta_2;\zeta) &= P(\theta_1,\theta_2;\zeta) \big(
\zeta^{-1} \theta_1^{-1} \big(1-\zeta^{-1}\theta_2^{-1}\big)^{-1} \big)^c
= P(\theta_1,\theta_2;\zeta)  a_{0,1}(\theta_1,\theta_2;\zeta)^c .
\end{align}$$ Equations [\[eq.Sq1Sq2\]](#eq.Sq1Sq2){reference-type="eqref" reference="eq.Sq1Sq2"} and [\[eq.Ps1Ps2\]](#eq.Ps1Ps2){reference-type="eqref" reference="eq.Ps1Ps2"} imply that $$P^{1/c}(\theta_1,\theta_2;\zeta) S(\theta_1,\theta_2;\zeta) \in \varepsilon^{1/c} F_c,$$ where $\varepsilon$ is a unit, which in fact coincides with the one constructed in [@CGZ].

The expression given in the above equation, after multiplication by a prefactor, coincides with of equation [\[52H\]](#52H){reference-type="eqref" reference="52H"} if we choose $\theta_1$ and $\theta_2$ corresponding to the root $\xi_i$ of $\xi^3-\xi^2+1=0$.

In this way, we have succeeded in guessing the entries of the first column of the matrix $\mathbf{J}^{(5_2)}$ of the $5_2$ knot starting from the formula [\[Kashaev.52\]](#Kashaev.52){reference-type="eqref" reference="Kashaev.52"} for its Kashaev invariant. All of this seems to reek a little of "black magic". But the same method applied to the case of the $4_1$ knot (whose Kashaev invariant is given in [\[Q41J0Q0\]](#Q41J0Q0){reference-type="eqref" reference="Q41J0Q0"}) reproduces the formulas given in [\[Q41abcd\]](#Q41abcd){reference-type="eqref" reference="Q41abcd"}. In fact, we believe that this will work for any knot, giving each entry of the first column of the $\mathbf{J}$-matrix as a sum of products of cyclic quantum dilogarithms with summands modelled on the solution of the Neumann--Zagier gluing equations of the knot triangulation in the same way that the expression [\[eq.PD\]](#eq.PD){reference-type="eqref" reference="eq.PD"} is modelled on the gluing equations [\[eq.ge\]](#eq.ge){reference-type="eqref" reference="eq.ge"}.
