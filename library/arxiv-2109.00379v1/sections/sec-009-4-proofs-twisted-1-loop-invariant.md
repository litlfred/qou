---
doc_id: arxiv-2109.00379v1
doc_title: "TWISTED NEUMANN–ZAGIER MATRICES"
section_id: sec-009-4-proofs-twisted-1-loop-invariant
section_title: "Proofs: twisted 1-loop invariant"
section_number: 4
pages: 16-21
source_pdf: 2109.00379v1.pdf
source_sha256: f0c9bd89312a761c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.957
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
---
[]{#sec.part2 label="sec.part2"}

In this section we give proofs of the properties of the twisted 1-loop invariant.

::: proof
*Proof.* (of Theorem [\[thm.top\]](#thm.top){reference-type="ref" reference="thm.top"}) We will use the notation of Theorem [\[thm.NZpachner\]](#thm.NZpachner){reference-type="ref" reference="thm.NZpachner"} which relates the NZ matrices of two triangulations $\mathcal T$ and $\overline{\mathcal T}$ obtained by a 2--3 Pachner move shown in Figure [\[fig.pachner\]](#fig.pachner){reference-type="ref" reference="fig.pachner"}. Recall that a 2--3 Pachner move on $\mathcal T$ is determined by two tetrahedra $\Delta_\alpha$ and $\Delta_\beta$ with a common face in $\mathcal T$. Dividing the bipyramid $\Delta_\alpha \cup \Delta_\beta$ into three tetrahedra $\Delta_a, \Delta_b,$ and $\Delta_c$ as in Figure [\[fig.pachner\]](#fig.pachner){reference-type="ref" reference="fig.pachner"}, we obtain a new ideal triangulation $\overline{\mathcal T}$ with one additional edge $e_0$. Note that one can read off relations of shape parameters between $\mathcal T$ and $\overline{\mathcal T}$ directly from Figure [\[fig.pachner\]](#fig.pachner){reference-type="ref" reference="fig.pachner"}: $$\label{eqn.shapes}
z'_a= z_\alpha z_\beta, \ z'_b=\frac{1-1/z_\beta}{1-z_\alpha},\,
z'_c = \frac{1-1/z_\alpha}{1-z_\beta} \textrm{ and }
z_\alpha = \frac{1-1/z'_b}{1-z'_c}, \,  z_\beta = \frac{1-1/z'_c}{1-z'_b}$$ with the gluing equation $z'_a z'_b z'_c=1$ for the edge $e_0$.

We first consider the flattening part of the definition [\[1loopt\]](#1loopt){reference-type="eqref" reference="1loopt"}. A combinatorial flattening of $\overline{\mathcal T}$ satisfies the equation $f'_a+f'_b+f'_c=2$ (coming from the edge $e_0$) and determines that of $\mathcal T$ by $$\label{eqn.flat}
\begin{aligned}
f_\alpha & =f_b+f''_c, & f'_\alpha & = f''_a+ f_c & f''_\alpha & =f_a+f''_b,\\
f_\beta & =f''_b+f_c, &  f'_\beta & = f''_a + f_b, & f''_\beta & =f_a+f''_c.
\end{aligned}$$ Then a straightforward computation shows that $$\label{eqn.com}
\prod_\square \zeta^{\square f^\square_a}_a \zeta_b^{\square f^\square_b}
\zeta^{\square f^\square_c}_c =
\pm \frac{z_\alpha  (1-z_\alpha)z_\beta(1-z_\beta)}{1-z_\alpha z_\beta}
\prod_\square \zeta^{\square f^\square_\alpha}_\alpha
\zeta^{\square f^\square_\beta}_\beta  .$$ Moreover, combining Equation [\[pre5G\]](#pre5G){reference-type="eqref" reference="pre5G"} with [\[eqn.shapes\]](#eqn.shapes){reference-type="eqref" reference="eqn.shapes"}, one checks that $$\begin{aligned}
&   
\begin{pmatrix}
\displaystyle\sum_\square \overline{\mathbf{G}}^\square(t)_{a}\zeta^\square_a  & 
\displaystyle\sum_\square \overline{\mathbf{G}}^\square(t)_{b}\zeta^\square_b & 
\displaystyle\sum_\square \overline{\mathbf{G}}^\square(t)_{c}\zeta^\square_c \end{pmatrix}   
\begin{pmatrix}
\frac{1}{z_\alpha z_\beta} & \frac{1}{z_\alpha z_\beta}-1 & \frac{1}{z_\alpha z_\beta}-1 \\
0 & \frac{z_\beta(1-z_\alpha)(1-z_\alpha z_\beta)}{1-z_\beta} & 0 \\
0 & 0 & \frac{z_\alpha(1-z_\beta)(1-z_\alpha z_\beta)}{1-z_\alpha}
\end{pmatrix}\\
& = Q \begin{pmatrix}
1& 0  & 0 \\
\ast & \displaystyle\sum_\square \mathbf{G}^\square(t)_{\alpha} \zeta^\square_\alpha
&  \displaystyle\sum_\square \mathbf{G}^\square(t)_{\beta}\zeta^\square_\beta 
\end{pmatrix}
\begin{pmatrix} 1 & 0 & 0\\
0 & z_\alpha z_\beta(1-z_\alpha) & z_\alpha(1-z_\alpha) \\
0 & z_\beta (1-z_\beta) & z_\alpha z_\beta(1-z_\beta)           
\end{pmatrix}\,,
\end{aligned}$$ where the determinant of the $3 \times 3$ matrix in the left (resp., right) hand side is $(1-z_\alpha z_\beta)^2$ (resp., $z_\alpha (z_\alpha-1) z_\beta (z_\beta-1)
(1-z_\alpha z_\beta))$. Combining this fact with the equation [\[eqn.com\]](#eqn.com){reference-type="eqref" reference="eqn.com"} and the fact that $\det Q=1$, we conclude that $\tau^{\mathrm{CS}}(\overline{\mathcal T},t) = \pm \tau^{\mathrm{CS}}(\mathcal T,t)$. ◻
:::

::: proof
*Proof.* (of Theorem [\[thm.1\]](#thm.1){reference-type="ref" reference="thm.1"}) Using Equation [\[Gnkt\]](#Gnkt){reference-type="eqref" reference="Gnkt"} and the fact that a combinatorial flattening of $\mathcal T^{(n)}$ is simply given by $n$ copies of that of $\mathcal T$, it follows that $$\begin{aligned}
\tau^\mathrm{CS}(\mathcal T^{(n)},t^n) &= \det\left( \displaystyle\sum_{k \in \mathbbm Z}
  \left(  \sum_\square \mathbf{G}_k^{(n)\square}\,
    \mathrm{diag}(\zeta^\square,\ldots,\zeta^\square)\right) t^{nk}\right)  \cdot
\left(\prod_{j=1}^N\zeta_j^{f_j} \zeta_j'^{f_j'} \zeta_j''^{f_j''}\right)^{-n}  \\
&=\det \begin{pmatrix*}[c]
W_0 &  W_1& \cdots & W_{n-2}& W_{n-1} \\
t^{n} W_{n-1} &  W_0& \cdots & W_{n-3}& W_{n-2}  \\
\vdots & \vdots & \ddots & \vdots \\
t^{n} W_1 & t^n W_2& \cdots &t^n W_{n-1}& W_0 
\end{pmatrix*}
\cdot  \left(\prod_{j=1}^N\zeta_j^{f_j} \zeta_j'^{f_j'} \zeta_j''^{f_j''}\right)^{-n}
\label{eqn:cyctor}
\end{aligned}$$ where $W_r = \sum_{k \in \mathbbm Z} \sum_\square \mathbf{G}_{nk+r}^{\square} \,
\mathrm{diag} (\zeta^\square)\,t^{nk}$ for $0 \leq r \leq n-1$.

The block matrix in the equation [\[eqn:cyctor\]](#eqn:cyctor){reference-type="eqref" reference="eqn:cyctor"} is called a *factor block circulant matrix* where the factor is $\mathrm{diag}(t^n,\ldots, t^n)$. It is known that a factor block circulant matrix admits a block-diagonalization in terms of the *representer* $P(z)= W_0+W_1 z +\cdots + W_{n-1}z^{n-1}$: $$\begin{pmatrix*}[c]
    W_0 &  W_1& \cdots &  W_{n-2} & W_{n-1} \\
    t^{n} W_{n-1} &  W_0& \cdots&  W_{n-3} & W_{n-2}  \\
    \vdots & \vdots & \ddots & \vdots \\
    t^{n} W_1 & t^n W_2& \cdots & t^n  W_{n-1} &W_0 
\end{pmatrix*} = V \begin{pmatrix*}[c]
 P(t) &   &  &   & \\
 &   P(\omega \, t) &  &   &   \\
 &  & \ddots &  \\
  & &  &  & P(\omega^{n-1} \, t) 
\end{pmatrix*} V^{-1}$$

where $\omega$ is a primitive $n$-th root of unity and $V$ is a block Vandermonde matrix $$V= \begin{pmatrix}
I & I &\cdots  & I \\
H_0  &H_1 &\cdots & H_{n-1} \\
H_0^2  &H_1^2 &\cdots & H_{n-1}^2 \\
\vdots & \vdots & & \vdots \\
H_0^{n-1}  &H_1^{n-1} &\cdots & H_{n-1}^{n-1}\\     
\end{pmatrix}, \quad H_i = w^{i} \, \mathrm{diag}(t,\ldots,t).$$ We refer to [@circulant] for details. In particular, we have $$\det \begin{pmatrix*}[c]
W_0 &  W_1& \cdots &  W_{n-2} & W_{n-1} \\
t^{n} W_{n-1} &  W_0& \cdots&  W_{n-3} & W_{n-2}  \\
\vdots & \vdots & \ddots & \vdots \\
t^{n} W_1 & t^n W_2& \cdots & t^n  W_{n-1} &W_0 
\end{pmatrix*} =\prod_{\omega^n=1} \det P(\omega\, t)$$ where, by definition, $$\begin{aligned}
P(\omega\, t) &= \sum_{r=0}^{n-1} W_r (\omega\, t)^r \\
&=\sum_{r=0}^{n-1} \sum_{k \in \mathbbm Z} \left( \sum_\square
  \mathbf{G}_{nk+r}^{\square} \mathrm{diag} (\zeta^\square) \right) t^{nk+r} \omega^{nk+r}
\\
&=\sum_{k \in \mathbbm Z} \left(\sum_\square \mathbf{G}_{k}^{\square}
  \mathrm{diag} (\zeta^\square)\right)(\omega\, t)^{k}
\qquad (\text{since} \,\, \omega^n=1).
\end{aligned}$$ Combining the above calculations, we obtain $$\tau^{\mathrm{CS}}(\mathcal T^{(n)},t^n)  =
\prod_{\omega^n=1} \frac{\det\left(\sum_{k\in\mathbbm Z}
  \sum_\square  \mathbf{G}_{k}^{\square}\,
      \mathrm{diag} (\zeta^\square)\,(\omega\, t)^{k}\right)}{
  \prod_{j=1}^N\zeta_j^{f_j} \zeta_j'^{f_j'} \zeta_j''^{f_j''}} =
\prod_{\omega^n=1} \tau^{\mathrm{CS}}(\mathcal T, \omega\, t).$$ ◻
:::

::: proof
*Proof.* (of Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}) Let $R(t) = \sum_{\square} \mathbf{G}^\square (t)\, \mathrm{diag}(\zeta^\square)$ and $R_i(t)$ denote its $i$-th row. Since the sum of all rows of $\mathbf{G}^\square(1) =
\mathbf{G}^\square$ is $(2,\ldots,2)$ and $\zeta_j + \zeta'_j+ \zeta''_j =0$, the sum $R_1(1)+\cdots+R_N(1)$ is a zero vector. It follows that $\det R(1)=0$ and thus $\tau^{\mathrm{CS}}(\mathcal T,1)=0$.

Since the determinant is a linear map, we have $$\left. \frac{\partial}{\partial t} \right |_{t=1} \det R(t) 
= \sum_{i=1}^{N} \det
\begin{pmatrix}
R_1(1) \\
\vdots \\
\left.\frac{\partial}{\partial t}\right |_{t=1} R_i(t) \\
\vdots \\
R_N(1)
\end{pmatrix}  .$$ For $i \neq N$ we exchange the $i$-th row $\left.\frac{\partial}{\partial t} \right |_{t=1} R_i(t)$ with the $N$-th row $R_N(1)$ and replace $R_N(1)$ by $-R_1(1)-\cdots-R_{N-1}(1)$. Then after some elementary row operations, we obtain $$\left. \frac{\partial}{\partial t} \right |_{t=1} \det R(t) 
=\sum_{i=1}^N \det
\begin{pmatrix*}[c]
R_1(1) \\
\vdots \\
R_{N-1}(1) \\
\left.\frac{\partial}{\partial t}\right |_{t=1} R_i(t)
\end{pmatrix*}
= \det
\begin{pmatrix*}[c]
R_1(1) \\
\vdots \\
R_{N-1}(1) \\
 \left.\frac{\partial}{\partial t}\right |_{t=1} \sum_{i=1}^N R_i(t)
\end{pmatrix*}  .$$ Comparing the definitions of equation [\[1loop\]](#1loop){reference-type="eqref" reference="1loop"} and [\[1loopt\]](#1loopt){reference-type="eqref" reference="1loopt"}, it suffices to show that $\left.\frac{\partial}{\partial t}\right
|_{t=1} \sum_{i=1}^N R_i(t)$ agrees with $\frac{1}{2}\sum_\square \mathbf{C}_\lambda^\square  \mathrm{diag}(\zeta^\square)$ up to linear combination of $R_1(1),\ldots, R_{N}(1)$.

Let $\widetilde\Sigma$ be the pre-image of the peripheral torus $\Sigma$ under the covering map $\widetilde M \rightarrow M$. Note that $\mathcal T$ induces a triangulation of $\widetilde\Sigma$ where vertices and triangles of $\widetilde\Sigma$ correspond to edges and tetrahedra of $\widetilde\mathcal T$, respectively. For each triangle $\Delta$ of $\widetilde\Sigma$ corresponding to the tetrahedron $\mu^k \cdot \widetilde\Delta_j$, we assign a *corner parameter* $t^k \log z^\square_j$ to each corner of $\Delta$ according to the quad type of $\Delta_j$. Then the sum $r_i(t)$ of corner parameters around a vertex of $\widetilde\Sigma$ corresponding to the edge $\widetilde e_i$ is $$\label{eqn.corner}
r_i(t)=\sum_{j=1}^N \sum_\square (\mathbf{G}^\square(t))_{ij}
\log z_j^\square .$$ It follows that (see Equation [\[eqn.zeta\]](#eqn.zeta){reference-type="eqref" reference="eqn.zeta"}) $$\label{eqn.Rr}
R_i(t) = \begin{pmatrix}
\frac{\partial}{\partial z_1} r_i(t) & \cdots &\frac{\partial}{\partial z_N} r_i(t)
\end{pmatrix}  .$$

We choose any lift $\widetilde\lambda$ of $\lambda$ to $\widetilde\Sigma$. Since $\alpha(\lambda)=0$, $\widetilde\lambda$ is still a loop in $\widetilde\Sigma$. Up to homotopy, we may assume that $\widetilde\lambda$ is an edge-path in $\widetilde\Sigma$ so that the surface $S$ bounded by $\widetilde\lambda$ and $\mu \cdot \widetilde\lambda$ is triangulated. Here we view $S$ as a closed cylinder whose boundary is consisted of $\widetilde\lambda$ and $\mu\cdot \widetilde\lambda$. Let $c_\lambda(t)$ (resp., $\check{c}_\lambda(t)$) be the sum of corner parameters in $S$ that are adjacent (resp., not adjacent) to $\widetilde\lambda$. By definition, the equation $c_\lambda(1)=0$ represents the completeness equation of $\lambda$. Hence, $$\label{eqn.lambda}
\sum_\square \mathbf{C}_\lambda^\square  \mathrm{diag}(\zeta^\square) = 
\begin{pmatrix}
  \frac{\partial}{\partial z_1} c_\lambda(1) & \cdots &
  \frac{\partial}{\partial z_N} c_\lambda(1)
\end{pmatrix}  .$$ Also, since $S$ consists of triangles and $\zeta_j + \zeta'_j +\zeta''_j=0$ for all $j$, we have $$\label{eqn:ab}
\frac{\partial}{\partial z_j} (c_\lambda(t)+\check{c}_\lambda(t))=0  .$$ On the other hand, $t c_\lambda(t)$ is the sum of corner parameters adjacent to $\mu \cdot \widetilde\lambda$ and not in $S$. It follows that the sum of corner parameters around vertices in $D \setminus \widetilde\lambda$ is given by $tc_\lambda(t)+\check{c}_\lambda(t)$. Since $D \setminus \widetilde\lambda$ is a fundamental domain of $\Sigma$, exactly two vertices in $D \setminus \widetilde\lambda$ correspond to a lift of $e_i$ for each $1 \leq i \leq N$. It follows that $$t c_\lambda(t)+\check{c}_\lambda(t)= \sum_{i=1}^N (t^{a_i}+t^{b_i}) \, r_i(t)  .$$ for some $a_i$ and $b_i \in \mathbbm Z$ and thus $$\begin{aligned}
  \left. \frac{\partial}{\partial t} \right|_{t=1}
  (t c_\lambda(t)+\check{c}_\lambda(t)) = \sum_{i=1}^N  (a_i+b_i) r_i(1) +2 \left.
    \frac{\partial}{\partial t} \right|_{t=1} \sum_{i=1}^Nr_i(t)  .
\end{aligned}$$ Taking the partial derivative with respect to $z_j$, we obtain $$\begin{aligned}
  \left. \frac{\partial}{\partial t} \right|_{t=1} \frac{\partial}{\partial z_j}
  \sum_{i=1}^Nr_i(t) &= \frac{1}{2} \frac{\partial}{\partial z_j} \left.
    \frac{\partial}{\partial t} \right|_{t=1}
  (t c_\lambda(t)+\check{c}_\lambda(t))
  - \frac{1}{2} \sum_{i=1}^N (a_i+b_i) \frac{\partial}{\partial z_j}r_i(1)
  \\
  &=\frac{1}{2} \frac{\partial}{\partial z_j} c_\lambda(1)
  - \frac{1}{2} \sum_{i=1}^N (a_i+b_i) \frac{\partial}{\partial z_j}r_i(1) \,,
  \label{eqn.fin}
\end{aligned}$$ where the second equation is followed from the equation [\[eqn:ab\]](#eqn:ab){reference-type="eqref" reference="eqn:ab"} with the fact $t c_\lambda(t)+\check{c}_\lambda(t)=(t-1)c_\lambda(t)
+ c_\lambda(t)+\check{c}_\lambda(t)$. Combining the equations [\[eqn.Rr\]](#eqn.Rr){reference-type="eqref" reference="eqn.Rr"}, [\[eqn.lambda\]](#eqn.lambda){reference-type="eqref" reference="eqn.lambda"}, and [\[eqn.fin\]](#eqn.fin){reference-type="eqref" reference="eqn.fin"}, we obtain the desired result that $\left.\frac{\partial}{\partial t}\right |_{t=1} \sum_{i=1}^N R_i(t)$ agrees with $\frac{1}{2}\sum_\square \mathbf{C}_\lambda^\square  \mathrm{diag}(\zeta^\square)$ up to linear combination of $R_1(1),\ldots, R_{N}(1)$: $$\left. \frac{\partial}{\partial t} \right|_{t=1} \sum_{i=1}^N R_i(t)
  = \frac{1}{2}\sum_\square \mathbf{C}_\lambda^\square  \mathrm{diag}(\zeta^\square)
  + \frac{1}{2} \sum_{i=1}^N (a_i+b_i) R_i(1)  .$$ ◻
:::

::: proof
*Proof.* (of Corollary [\[cor.sym\]](#cor.sym){reference-type="ref" reference="cor.sym"}) The statement is equivalent to $$\label{eqn.symm}
\det\left( \mathbf{A}(t)\, \mathrm{diag}(\zeta) + \mathbf{B}(t)\, \mathrm{diag}(\zeta'')
\right)= \varepsilon t^r
\det\left( \mathbf{A}(1/t)\, \mathrm{diag}(\zeta) + \mathbf{B}(1/t)\,
\mathrm{diag}(\zeta'') \right)$$ for some $\varepsilon= \pm1$ and some integer $r$ and some choice of quads of $\mathcal T$. We make such a choice such that $\mathbf{B}$ is non-singular. This is always possible; see [@DG1 App.A]. Then, $\det \mathbf{B}(t) \neq 0$, since $\mathbf{B}(1)=\mathbf{B}$. Conjecture [\[conj.ABt\]](#conj.ABt){reference-type="ref" reference="conj.ABt"} implies that $\det \mathbf{B}(t)=\varepsilon t^r \det \mathbf{B}(1/t) \neq 0$. This, combined with Theorem [\[thm.sympl\]](#thm.sympl){reference-type="ref" reference="thm.sympl"} gives $$\begin{aligned}
&\det\left( \mathbf{A}(t) \,\mathrm{diag}(\zeta)
+ \mathbf{B}(t)\, \mathrm{diag}(\zeta'') \right)\\
&= \det \mathbf{B}(t) \det \left(\mathbf{B}(t)^{-1} \mathbf{A}(t)
+ \mathrm{diag}(\zeta''/\zeta)\right) \det(\mathrm{diag}(\zeta))
\\
& =\varepsilon t^r\det \mathbf{B}(1/t) \det \left(\mathbf{B}(1/t)^{-1} \mathbf{A}(1/t)
+ \mathrm{diag}(\zeta''/\zeta)\right) \det(\mathrm{diag}(\zeta))
\\
&=\varepsilon t^r\det\left( \mathbf{A}(1/t)\, \mathrm{diag}(\zeta) + \mathbf{B}(1/t)\,
\mathrm{diag}(\zeta'') \right)
\end{aligned}$$

Note that Theorem [\[thm.sympl\]](#thm.sympl){reference-type="ref" reference="thm.sympl"} implies that $\mathbf{B}(t)^{-1} \mathbf{A}(t)= (\mathbf{B}(1/t)^{-1} 
\mathbf{A}(1/t))^T$ which is used in the second equality above. ◻
:::

We end this section by giving a proof of Equation [\[behavior2\]](#behavior2){reference-type="eqref" reference="behavior2"}. Taking the derivative of Equation [\[1loopcyclic\]](#1loopcyclic){reference-type="eqref" reference="1loopcyclic"} at $t=1$ and then simplifying the result by Theorem [\[thm.2\]](#thm.2){reference-type="ref" reference="thm.2"}, we obtain $$\label{behavior1}
\frac{\tau^\mathrm{CS}_\lambda(\mathcal T^{(n)})}{\tau^\mathrm{CS}_\lambda(\mathcal T)}
= \frac{1}{n}  \prod_{ \substack{\omega^n=1 \\ \omega \neq 1}} \tau^\mathrm{CS}(\mathcal T,w)$$ which is equivalent to Equation [\[behavior2\]](#behavior2){reference-type="eqref" reference="behavior2"} due to Theorem 4.1 of [@Porti:torsion] (explicitly, the ratio $\tau_\lambda^{\mathrm{CS}}(\mathcal T)/\tau_\mu^{\mathrm{CS}}(\mathcal T)$ is the cusp shape of $M$ and $\tau_\lambda^{\mathrm{CS}}(\mathcal T^{(n)})/\tau_\mu^{\mathrm{CS}}(\mathcal T^{(n)})$ is $n$ times of that).
