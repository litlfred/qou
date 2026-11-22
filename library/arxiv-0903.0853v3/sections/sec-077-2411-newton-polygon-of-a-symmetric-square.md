---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-077-2411-newton-polygon-of-a-symmetric-square
section_title: "Newton polygon of a symmetric square"
section_number: 24.1.1
pages: 125-127
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.946
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
To find the equation satisfied by a product of two functions, one uses the tensor product of two systems or modules; for a square, one uses likewise the symmetric square.\
Let $M = (V,\Phi)$ be a $q$-difference module and $T^{2} M := M \otimes M = (V \otimes V,\Phi \otimes \Phi)$ its tensor square. The linear automorphism $x \otimes y \mapsto y \otimes x$ commutes with $\Phi \otimes \Phi$, so that it actually defines an involutive $q$-difference automorphism of $M \otimes M$, and a splitting: $$\label{not105}
T^{2} M = S^{2} M \oplus \Lambda^{2} M.$$ If $M$ has slopes $\mu_{1},\ldots,\mu_{k}$ with multiplicities $r_{1},\ldots,r_{k}$, then $T^{2} M$ has slopes the $\mu_{i} + \mu_{j}$ , $1 \leq i,j \leq k$ with multiplicities the $r_{i} r_{j}$. (Of course, if many sums $\mu_{i} + \mu_{j}$ are equal, the corresponding multiplicities $r_{i} r_{j}$ should be added; the same remark will hold for the following computations.) Said otherwise, the slopes of $T^{2} M$ are the $2 \mu_{i}$, $1 \leq i \leq k$ with multiplicities the $r_{i}^{2}$; and the $\mu_{i} + \mu_{j}$ , $1 \leq i < j \leq k$ with multiplicities the $2 r_{i} r_{j}$.\
The repartition of these slopes (breaking of the Newton polygon) among the symmetric and exterior square is as follows:

-   $S^{2} M$ has slopes the $2 \mu_{i}$, $1 \leq i \leq k$ with multiplicities the $\dfrac{r_{i}^{2} + r_{i}}{2}$; and the $\mu_{i} + \mu_{j}$ , $1 \leq i < j \leq k$ with multiplicities the $r_{i} r_{j}$.

-   $\Lambda^{2} M$ has slopes the $2 \mu_{i}$, $1 \leq i \leq k$ with multiplicities the $\dfrac{r_{i}^{2} - r_{i}}{2}$; and the $\mu_{i} + \mu_{j}$ , $1 \leq i < j \leq k$ with multiplicities the $r_{i} r_{j}$.

If there are two slopes $\mu < \nu$, with multiplicities $r,s$, no confusion of sums $\mu_{i} + \mu_{j}$ can arise, and we find:

-   $T^{2} M$ has slopes $2 \mu < \mu + \nu < 2 \nu$, with multiplicities $r^{2},2 r s,s^{2}$;

-   $S^{2} M$ has the same slopes, with multiplicities $\dfrac{r^{2}+r}{2},r s,\dfrac{s^{2}+s}{2}$;

-   $\Lambda^{2} M$ has the same slopes, with multiplicities $\dfrac{r^{2}-r}{2},r s,\dfrac{s^{2}-s}{2} \cdot$

We now take $M_{0} = \begin{pmatrix} a & 0 \\ 0 & b z \end{pmatrix}$ and $M = \begin{pmatrix} a & u \\ 0 & b z \end{pmatrix}$, where $a,b \in {\mathbf C}^{*}$ and $u \in {{\mathbf C}(\{z\})}$. The symmetric squares admit an obvious choice of basis and corresponding matrices: $$N_{0} = \begin{pmatrix} 
a^{2} & 0 & 0 \\ 
0 & a b z & 0 \\ 
0 & 0 & b^{2} z^{2} 
\end{pmatrix} 
\text{~and~}
N = \begin{pmatrix} 
a^{2} & 2 a u & u^{2} \\ 
0 & a b z & u b z \\ 
0 & 0 & b^{2} z^{2} 
\end{pmatrix}.$$ If $F = \begin{pmatrix} 1 & f \\ 0 & 1 \end{pmatrix}$ is such that $F[M_{0}] = M$, then we have $G[N_{0}] = N$ with $G$ given by: $$G = S^{2} F = \begin{pmatrix} 1 & 2 f & f^{2} \\ 
0 & 1 & f \\ 0 & 0 & 1 \end{pmatrix}.$$ Actually, if one does not cheat, when looking for $G = \begin{pmatrix} 1 & f_{1} & f_{2} \\ 
0 & 1 & f_{3} \\ 0 & 0 & 1 \end{pmatrix}$ such that $G[N_{0}] = N$, one has to solve the system: $$\begin{aligned}
a b z \sigma_qf_{1} &= a^{2} f_{1} + 2 a u, \\
b^{2} z^{2} \sigma_qf_{2} &= a^{2} f_{2}  + 2 a u f_{3} + u^{2}, \\ 
b^{2} z^{2} \sigma_qf_{3} &= a b z f_{3} + u b z.
\end{aligned}$$ Since we know from start that $b z \sigma_qf = a f + u$, we see that $f_{1} := 2 f$ and $f_{3} := f$ respectively solve the first and third equation; then, we find that $f_{2} := f^{2}$ solve the second equation.\
Using the system above, we find a second order inhomogeneous equation for $f_{2}$ alone as follows: $$\begin{aligned}
(b z \sigma_q- a) \, \dfrac{1}{2 a u} \, (b^{2} z^{2} \sigma_q- a^{2}) f_{2} & =
(b z \sigma_q- a) \, f_{3} + (b z \sigma_q- a) \, \dfrac{u^{2}}{2 a u} 
\Longrightarrow \\
\left(\dfrac{b z}{\sigma_q(u)} \sigma_q- \dfrac{a}{u}\right) \, 
(b^{2} z^{2} \sigma_q- a^{2}) f_{2} & = b z \sigma_q(u) + a u.
\end{aligned}$$ We leave to the reader to find a simpler form, as well as the corresponding third order homogeneous equation. At any rate, in the case that $u \in {\mathbf C}$ (Birkhoff-Guenther normal form) we have: $$(b z \sigma_q- a) \, (b^{2} z^{2} \sigma_q- a^{2}) f_{2} = b z + a.$$ In the particular case $a = b = -u = 1$ of the Tshakaloff series, we are led to the following equation: $$\label{equation:carre}
L \hat Y = 1 + z, \text{~where~} L := q^2z^3 \sigma_q^2 - z(1+z) \sigma_q+ 1.$$

::: rema
We refer here to the example [\[exem:geometrythreeslopes\]](#exem:geometrythreeslopes){reference-type="ref" reference="exem:geometrythreeslopes"} and specialize it to the case of the symmetric square $N$ above. We see that, when $u$ varies, the class of $N$ in $H^{1}({\mathbf{E}_{q}},\lambda^{(1)}) \oplus H^{1}({\mathbf{E}_{q}},\lambda^{(2)})$ has components $2 a u L_{1}(a^{2},a b) + u b L_{1}(a b,b^{2})$ and $u^{2} L_{2,0}(a^{2},b^{2})$: a nice parabola.
:::
