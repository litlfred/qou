---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-003-4-poly-bargmann-transforms
section_title: "Poly-Bargmann transforms"
section_number: 4
pages: 21-23
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.969
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
In this section, we discuss the poly-Bargmann transforms, a generalization of the classical Bargmann transform, which are needed later when we analyze the Berezin density at a boundary point. The poly-Bargmann transforms appeared in Vasilevski's paper [@vas], where the basic properties were presented.

We denote by $H_j$ the $j$-th Hermite polynomial with respect to the Gaussian weight $\mathrm e^{-\frac12t^2}$ ("probabilistic Hermite polynomials"). The generating function identity $$\mathrm e^{tz-\frac12z^2} = \sum_{j=0}^{+\infty} H_j(t)\frac{z^j}{j!}$$ allows us to write $$\frac{1}{(2\pi)^{1/4}}\mathrm e^{zt-\frac12z^2-\frac14t^2}=  
\sum_{j=0}^{+\infty} \frac{H_j(t)\mathrm e^{-t^2/4}}{(2\pi)^{1/4}\sqrt{j!}}
\times\frac{z^j}{\sqrt{j!}}.$$ We recall the standard definition of the Bargmann transform: $${\mathbf B}[f](z)= \frac{1}{(2 \pi)^{1/4}} \int_{{\mathbb R}}
 \mathrm e^{zt-\frac12z^2-\frac14t^2}f(t)\,{\mathrm d}t, \qquad
f \in L^2({\mathbb R}).$$ As the function systems $$\Big\{\frac{1}{(2\pi)^{1/4}\sqrt{j!}}H_j(t)\mathrm e^{-\frac14t^2} 
\Big\}_{j=0}^{+\infty}\quad\text{and}\quad \Big\{\frac{z^j}{\sqrt{j!}}
\Big\}_{j=0}^{+\infty}$$ form orthonormal bases for $L^2(\mathbb{R})$ and the Bargmann-Fock space $A^2_{1,1}({\mathbb C})$ (this is $A^2_{m,q}({\mathbb C})$ with $m=q=1$), respectively, we obtain the following well-known fact.

::: prop
The Bargmann transform ${\mathbf B}:L^2({\mathbb R})\to A_{1,1}^2({\mathbb C})$ acts isometrically and bijectively, and for each $j=0,1,2,\ldots$, the basis function $(2\pi)^{-1/4}(j!)^{-1/2}H_j(t)\mathrm e^{-\frac14t^2}$ is mapped to the basis function $(j!)^{-1/2}z^j$.
:::

Let $\partial_z,\bar\partial_z$ denote the standard Wirtinger differential operators $$\partial_z:=\tfrac12(\partial_x-{\mathrm i}\partial_y),\,\,\,
\bar\partial_z:=\tfrac12(\partial_x+{\mathrm i}\partial_y),
\quad\text{where}\,\,\, z=x+{\mathrm i}y.$$ For $r=0,1,2,\ldots$, we introduce the operator $${\mathbf T}_{r}[f](z):=\frac{1}{\sqrt{r!}} \mathrm e^{|z|^2}\,
\partial_z^r\big\{f(z)\mathrm e^{-|z|^2}\big\},$$ with the semi-group property ${\mathbf T}_1\circ{\mathbf T}_{r-1}=r^{1/2}{\mathbf T}_r$. We also consider the dilated variant $${\mathbf T}_{m,r}[f](z) = {\mathbf T}_r[f_{m^{-1/2}}](m^{1/2}z),$$ where $f_{m^{-1/2}}(z)=f(m^{-1/2}z)$. It has the semi-group property ${\mathbf T}_{m,1}\circ{\mathbf T}_{m,r-1}=r^{1/2}{\mathbf T}_{m,r}$, and may be expressed in more concrete terms: $${\mathbf T}_{m,r}[f](z) = \frac{m^{-r/2}}{\sqrt{r!}} \mathrm e^{m|z|^2}\,
\partial_z^r\big\{f(z)\mathrm e^{-m|z|^2}\big\}.$$ We now study the effect of ${\mathbf T}_r$ on the basis elements $(j!)^{-1/2}z^j$.

::: prop
[]{#T_r-prop label="T_r-prop"} For $j\ge r$, we have $${\mathbf T}_r\bigg[\frac{z^j}{\sqrt{j!}}\bigg]=
\frac{1}{\sqrt{r!}}\mathrm e^{|z|^2}
\partial^r_z\bigg\{\mathrm e^{-|z|^2}\frac{z^j}{\sqrt{j!}}\bigg\}= 
\sqrt{\frac{r!}{j!}}z^{j-r}L^{j-r}_r(|z|^2)$$ while for $j \leq r$, $${\mathbf T}_r\bigg[\frac{z^j}{\sqrt{j!}}\bigg]=
\frac{1}{\sqrt{r!}}\mathrm e^{|z|^2}\partial^r_z\bigg\{\mathrm e^{-|z|^2}
\frac{z^j}{\sqrt{j!}}\bigg\}= 
(-1)^{r-j}\sqrt{\frac{n!}{r!}}\,\bar{z}^{r-j}L^{r-j}_j(|z|^2)$$
:::

::: proof
*Proof.* The proof is based on an induction argument. The statement is obviously true for $r=0$ and all $j$. So, by induction, we assume that the statement holds for some $r-1\geq 0$ and all $j$. In case $j\ge r$, we then have $$\begin{gathered}
\partial^r_z\{\mathrm e^{-|z|^2}z^j\}= 
\partial_z\big\{(r-1)!\,z^{j-r+1}L^{j-r+1}_{r-1}(|z|^2)\mathrm e^{-|z|^2} 
\big\}
\\
=(r-1)! z^{j-r}
\big\{(j-r+1)L^{j-r+1}_{r-1}(|z|^2)-L^{j-r+2}_{r-2}(|z|^2)|z|^2  
-|z|^2L^{j-r+1}_{r-1}(|z|^2)\big\}\mathrm e^{-|z|^2} 
\\
= r! L^{j-r}_r(|z|^2)z^{j-r}\mathrm e^{-|z|^2},
\end{gathered}$$ if we use the standard identity $rL^{\alpha}_r(x) = (\alpha + 1 -x) 
L^{\alpha+1}_{r-1}(x) - xL^{\alpha+2}_{r-2}(x)$. Next, in case $j\leq r-1$, we have instead $$\begin{gathered}
\partial^r_z\{\mathrm e^{-|z|^2}z^j\}= (-1)^{r-1-j} \partial 
\big\{
j!\,\bar{z}^{r-1-j}L^{r-1-j}_j(|z|^2)\mathrm e^{-|z|^2} 
\big\} 
\\
=(-1)^{r-j} j! \bar{z}^{r-j} \big\{L^{r-j}_{j-1}(|z|^2)+ 
L^{r-j-1}_{j}(|z|^2) \big\}\mathrm e^{-|z|^2}
=(-1)^{r-j} j!\,\bar{z}^{r-j}L^{r-j}_j (|z|^2)\mathrm e^{-|z|^2},
\end{gathered}$$ which completes the proof. ◻
:::

Write $e_j(z):=(j!)^{-1/2}z^j$ for $j=0,1,2,\ldots$, which functions form the standard orthonormal basis for the space $A^2_{1,1}({\mathbb C})$. The function ${\mathbf T}_r[e_j]\in A^2_{1,r+1}({\mathbb C})$ is then a polynomial in $z,\bar z$, where the degree in $z$ remains equal to $j$, and the degree in $\bar z$ equals $r$. For general positive $m$, the functions $e_{j,m}(z):=
(j!)^{-1/2}m^{\frac12(j+1)}z^j$, with $j=0,1,2,\ldots$, form an orthonormal basis for the space $A^2_{m,1}({\mathbb C})$. The functions ${\mathbf T}_{m,r}[e_{j,m}]$ are computed using Proposition [\[T_r-prop\]](#T_r-prop){reference-type="ref" reference="T_r-prop"} above, and we then recognize that we can identify them with the basis elements which appear in Proposition [\[on-kanta\]](#on-kanta){reference-type="ref" reference="on-kanta"}. We clearly have that $$\mathrm{span}\big\{{\mathbf T}_{m,r}[e_{j,m}]:\,\, 0\le j\le n-1,\,\,0\le r\le q-1
\big\}=\mathrm{Pol}_{m,n,q},$$ and in view of the orthogonality properties in Proposition [\[on-kanta\]](#on-kanta){reference-type="ref" reference="on-kanta"}, we also must have $$\mathrm{span}\{{\mathbf T}_{m,r}[e_{j,m}]:\,\, 0\le j\le n-1\}
=\mathrm{Pol}_{m,n,r+1}\ominus \mathrm{Pol}_{m,n,r},
\label{eq-resspace1}$$ where the "$\ominus$" is with respect to the inner product in $L^2({\mathbb C},\mathrm e^{-m|z|^2})$. Following Vasilevski [@vas], then, we define the pure polyanalytic Fock space of level $r+1$: $${\delta\mathrm{Pol}}_{m,n,r+1}:=\mathrm{Pol}_{m,n,r+1}\ominus \mathrm{Pol}_{m,n,r},\quad
\delta A^2_{m,n,r+1}({\mathbb C}):=A^2_{m,r+1}({\mathbb C})\ominus A^2_{m,r}({\mathbb C}),
\label{eq-resspace2}$$ with the understanding that $\mathrm{Pol}_{m,n,0}:=\{0\}$ and $A^2_{m,0}({\mathbb C}):=\{0\}$. The operator ${\mathbf T}_{m,r}$ now becomes an isometric isomorphism $${\mathbf T}_{m,r}:A^2_{m,1}({\mathbb C})\to\delta A^2_{m,n,r+1}({\mathbb C}),\quad
{\mathbf T}_{m,r}:\mathrm{Pol}_{m,n,1}\to{\delta\mathrm{Pol}}_{m,n,r+1}.$$ We obtain the orthogonal decompositions $$\begin{aligned}
\mathrm{Pol}_{m,n,q} &= \bigoplus_{r=0}^{q-1} {\delta\mathrm{Pol}}_{m,n,r+1},
& A^2_{m,q}({\mathbb C})=\bigoplus_{r=0}^{q-1} \delta A^2_{m,r+1}({\mathbb C}).
\end{aligned}$$ As a consequence, if $K_{\delta:m,n,r+1}$ and $K_{\delta:m,r+1}$ denote the reproducing kernels for the spaces ${\delta\mathrm{Pol}}_{m,n,r+1}$ and $\delta A^2_{m,r+1}({\mathbb C})$, respectively, we must have that $$\begin{aligned}
\label{kernelsubspacedecomposition}
K_{m,n,q} &= \sum_{r=0}^{q-1} K_{\delta:{m,n,r+1}},
&  K_{m,q} &=\sum_{r=0}^{q-1} K_{\delta:{m,r}}.
\end{aligned}$$

For $m=1$, the poly-Bargmann transform of level $r$ is defined by $$\begin{aligned}
{\mathbf B}_r[f]:= {\mathbf T}_r\circ{\mathbf B}[f].
\end{aligned}$$

::: prop
[]{#prop-Br label="prop-Br"} We have $${\mathbf B}_r[f](z)= 
\frac{1}{(2\pi)^{1/4}\sqrt{r!}} \int_{{\mathbb R}}f(t)H_r(t-z-\bar{z})
\,\mathrm e^{tz-\frac12z^2-\frac14t^2} {\mathrm d}t,\qquad r=0,1,2,\ldots.$$
:::

::: proof
*Proof.* We proceed by induction. For $r=0$, the formula reduces to the usual Bargmann transform (if we recall that $H_0=1$). By the induction hypothesis, we suppose therefore that the formula is valid for all integers up to $r-1$. From the semi-group property ${\mathbf T}_1\circ{\mathbf T}_{r-1}=r^{1/2}{\mathbf T}_r$, we see that $${\mathbf B}_r[f]={\mathbf T}_r\circ{\mathbf B}[f]=
r^{-1/2}{\mathbf T}_1\circ{\mathbf T}_{r-1}\circ{\mathbf B}[f](z)= 
r^{-1/2}{\mathbf T}_1\circ{\mathbf B}_{r-1}[f].$$ Since the formula holds for $r-1$, the following calculation shows that it holds for $r$ as well: $$\begin{gathered}
r^{-1/2}\mathrm e^{|z|^2} 
\partial_z 
\bigg([(r-1)!]^{-1/2}H_{r-1}(t-z- \bar{z})
\,\mathrm e^{tz-\frac12z^2-\frac14t^2}\mathrm e^{-|z|^2}\bigg)  
\\
= (r!)^{-1/2}\left(-H'_{r-1}(t-z-\bar{z})+ 
(t-z- \overline{z})H_{r-1}(t-z-\bar{z}) \right)
\,\mathrm e^{tz-\frac12z^2-\frac14t^2}
\\
= (r!)^{-1/2} H_r(t-z-\bar{z})\mathrm e^{tz-\frac12z^2-\frac14t^2}; 
\end{gathered}$$ here, we used the standard identity $H_{r}(x)=xH_{r-1}(x)-H'_{r-1}(x)$. The proof is complete. ◻
:::
