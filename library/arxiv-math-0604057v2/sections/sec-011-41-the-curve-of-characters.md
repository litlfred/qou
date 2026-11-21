---
doc_id: arxiv-math-0604057v2
doc_title: "Volume conjecture, regulator and SL2(C)-character variety of a knot"
section_id: sec-011-41-the-curve-of-characters
section_title: "The curve of characters"
section_number: 4.1
pages: 7-9
source_pdf: 0604057v2.pdf
source_sha256: 649fad141dc34eb9
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.951
doc_brief: "Volume conjecture, regulator and SL2(C)-character variety of a knot — In this paper, by using the regulator map of Beilinson-Deligne, we show that the quan- tization condition posed by Gukov is true"
---
In this subsection, we give some elementary properties about the character varieties and its component $D_0$.

Since $\partial M_K$ is a torus, we identify $R(\partial M_K)$ with the set $\{(A,B)|A,B\in SL_2(\mathbb{C}), AB=BA\}$, where $A=\rho(\mu)$, $B=\rho(\lambda)$ for $\rho$ a representation of $\pi_1(\partial M_K)$ in $SL_2(\mathbb{C})$. As in Section $2.3$, $R_{D}\subset R(\partial M_K)$ is the subvariety consisting of the representations of diagonal matrices. We have the isomorphism $p:R_{D}\rightarrow \mathbb{C}^{*}\times \mathbb{C}^{*}$ defined by $p(\rho)=(m,l)$ if $$\rho(\mu)=
  \left[
  \begin{matrix}
    m & 0\\
    0 & m^{-1}
  \end{matrix}
  \right], \;\;
\rho(\lambda)=
  \left[
  \begin{matrix}
    l & 0\\
    0 & l^{-1}
  \end{matrix}
  \right].$$

Let $R_{D}$ be identified with $\mathbb{C}^{*}\times
\mathbb{C}^{*}$ via $p$. By the proof of [@CS Proposition 1.4.1], $\chi\in X(\partial M_K)$ is determined by its values on $\mu$, $\lambda$ and $\mu\lambda$. Define a map $t:R(\partial M)\rightarrow \mathbb{C}^3$ by $t(\rho)=(\sigma(\rho(\mu)),\sigma(\rho(\lambda)),\sigma(\rho(\mu\lambda)))$ . Then $X(\partial M_K)=t(R(\partial M_K))$. This map is the regular surjective morphism $t:R(\partial M_K)\rightarrow
X(\partial M_K)$. That is why we use the same letter $t$. The map $t_D$, the restriction of $t$ on $R_D=\mathbb{C}^{*}\times
\mathbb{C}^{*}$, is given explicitly by, for $(m,l)\in
\mathbb{C}^{*}\times \mathbb{C}^{*}$, $$t_D(m,l)=(m+m^{-1}, l+l^{-1}, ml+m^{-1}l^{-1}).$$ It is straightforward to check that $t_D(\mathbb{C}^{*}\times
\mathbb{C}^{*})=X(\partial M_K)$ and $t_D$ is $2:1$ except at four points $(\pm 1, \pm 1)$ where it is $1:1$.

We have the following diagram:

$$\begin{CD}
    R(M_K)\supset R_0   @. D_0=t^{-1}_{D}(Y_0)\subset \mathbb{C}^{*}\times \mathbb{C}^{*}=R_D\subset R(\partial M_K)\\
     @VtVV   @Vt_DVV\\
    X(M_K)\supset X_0=t(R_0) @>r>> Y_0=\overline{r(X_0)}\subset X(\partial
    M_K).
\end{CD}$$

First we characterize the map $t_D$ and the character variety $X(\partial M)$.

::: proposition
[]{#f-prop label="f-prop"} The map $t_D:R_D=\mathbb{C}^{*}\times \mathbb{C}^{*}\rightarrow
X(\partial M_K)$ is a finite morphism.
:::

::: proof
*Proof.* The affine coordinate ring for $\mathbb{C}^{*}\times
\mathbb{C}^{*}$ is $\mathbb{C}[x,x^{-1},y,y^{-1}]$. Notice that $t_D$ is surjective, we can identify the coordinate ring of $X(\partial M_K)$ with the sub-ring $\mathbb{C}[x+x^{-1},y+y^{-1},xy+x^{-1}y^{-1}]$ of $\mathbb{C}[x,x^{-1},y,y^{-1}]$. Let $t=x+x^{-1}$, then $x$ and $x^{-1}$ are roots of the equation $X^2-tX+1=0$. Hence $x$ and $x^{-1}$ are integral over $\mathbb{C}[x+x^{-1},y+y^{-1},xy+x^{-1}y^{-1}]$, so are $y$ and $y^{-1}$. Now $x$, $x^{-1}$, $y$, $y^{-1}$ are integral over $\mathbb{C}[x+x^{-1},y+y^{-1},xy+x^{-1}y^{-1}]$, it follows that $\mathbb{C}[x,x^{-1},y,y^{-1}]$ is also integral over it. Therefore, $t_D$ is finite. ◻
:::

::: proposition
[]{#torus label="torus"} The character variety $X(\partial M_K)$ is a surface in $\mathbb{C}^3$ defined by $$\label{cha-torus}
    x^2+y^2+z^2-xyz-4=0.$$
:::

::: proof
*Proof.* Let $x$, $y$, $z$ be the traces of $a=\rho(\mu)$, $b=\rho(\lambda)$, $c=\rho(\mu\lambda)$ respectively. By the formula ([\[tf4\]](#tf4){reference-type="ref" reference="tf4"}), we have $$\sigma((ab)a^{-1}b^{-1})=\sigma(ab)\sigma(a^{-1}b^{-1})+\sigma(a^{-1})\sigma(a)+\sigma(b^{-1})\sigma(aba^{-1})
  -\sigma(ab)\sigma(a^{-1})\sigma(b^{-1})-\sigma(I).$$

Since $a$ and $b$ commute, $\sigma((ab)a^{-1}b^{-1})=\sigma(I)=2$, where $I$ is the $2\times 2$ identity matrix. This gives the equation ([\[cha-torus\]](#cha-torus){reference-type="ref" reference="cha-torus"}) by ([\[tf1\]](#tf1){reference-type="ref" reference="tf1"}) and ([\[tf2\]](#tf2){reference-type="ref" reference="tf2"}). Hence, $X(\partial M_K)$ is contained in the surface in $\mathbb{C}^3$.

On the other hand, let $(x,y,z)\in \mathbb{C}^3$ be a solution to ([\[cha-torus\]](#cha-torus){reference-type="ref" reference="cha-torus"}). It is a straightforward calculation that we can find $(m,l)\in \mathbb{C}^{*}\times \mathbb{C}^{*}$ such that $x=m+m^{-1}$, $y=l+l^{-1}$, and $z= ml+m^{-1}l^{-1}$. Hence the result follows. ◻
:::

For each $\gamma \in \pi_1(M_K)$, there is a natural regular map $I_{\gamma}: X(M_K)\rightarrow \mathbb{C}$ defined by $I_{\gamma}(\chi)=\chi (\gamma)$. The set of functions $I_{\gamma}$, $\gamma \in \pi_1(M_K)$ generates the affine coordinate ring of $X(M_K)$. Moreover, by [@CGLS Proposition 1.1.1], for each nonzero $\gamma \in
\pi_1(\partial M_K)$, the function $I_{\gamma}$ is non-constant on $X_0$. This implies that $r(X_0)\subset X(\partial M_K)$ has dimension $1$. We set $Y_0=\overline{r(X_0)}$, the Zariski closure of $r(X_0)$ in $X(\partial M_K)$. Then $Y_0$ is an irreducible affine curve. Denote by $D_0$ the inverse image $t^{-1}_{D}(Y_0)$.

::: proposition
[]{#d-curve label="d-curve"} (i) The inverse image $D_0\subset \mathbb{C}^{*}\times
\mathbb{C}^{*}$ is an affine algebraic set of dimension $1$;\
(ii) the image of each $1$-dimensional component of $D_0$ under $t_D$ is the whole $Y_0$;\
(iii) $D_0$ has no $0$-dimensional components and has at most two $1$-dimensional components.
:::

::: proof
*Proof.* (i). As $Y_0$ is closed, so is $D_0=t^{-1}_{D}(Y_0)$. Thus $D_0$ and $Y_0$ have the same dimension $1$ because $t_D$ is finite by Proposition [\[f-prop\]](#f-prop){reference-type="ref" reference="f-prop"}.

(ii). Next we show that if $V$ is a $1$-dimensional irreducible component of $D_0$, then $t_D(V)=Y_0$. In fact, since a finite morphism maps closed sets to closed sets, $t_D(V)\subset Y_0$ is closed, irreducible and its dimension is $1$. Hence $t_D(V)=Y_0$ due to the irreducibility of $Y_0$.

(iii). Suppose that $D_0$ has three distinct $1$-dimensional components $V_i$, $1\leq i \leq 3$. Since the $V_i \cap V_j$, $i\ne j$ are empty or finite sets, we can choose $y_0\in Y_0$ such that $y_0\notin t_D(V_i \cap V_j)$ for $\forall i\ne j$. We see that $t_D(V_i)=Y_0$, hence $t_D^{-1}(y_0)$ has three elements. This contradicts that $t_D^{-1}(y)$ has at most two elements for any $y\in Y_0$. Therefore, $D_0$ has at most two $1$-dimensional irreducible components.

Now we show that it has no $0$-dimensional components. Consider the morphism $\sigma: \mathbb{C}^{*}\times
\mathbb{C}^{*}\rightarrow \mathbb{C}^{*}\times \mathbb{C}^{*}$ defined by $\sigma(m,l)=(m^{-1},l^{-1})$. It is an involution and hence an automorphism of $\mathbb{C}^{*}\times \mathbb{C}^{*}$ with $\sigma(D_0)=D_0$. So it is an automorphism of $D_0$ when restricting on it. Therefore it maps $1$-dimensional component to $1$-dimensional component. Now for any $y\in Y_0$, $\sigma$ permutes elements of $t_D^{-1}(y)$ and at least one element of $t_D^{-1}(y)$ is contained in some $1$-dimensional component since $t_D$ maps every $1$-dimensional component onto $Y_0$. Therefore, no $0$-dimensional component for $D_0$. ◻
:::

::: remark
For the character variety $X(M_K)$, by [@CCGLS Proposition 2.4], there is no zero-dimensional components of $X(M_K)$. Proposition [\[d-curve\]](#d-curve){reference-type="ref" reference="d-curve"} part (iii) shows that $D_0$ in $R_D\subset R(\partial M_K)$ has no $0$-dimensional components.
:::

In summary, we have the following two cases:\
(I) $D_0$ itself is an irreducible affine curve;\
(II) $D_0=V_1\cup V_2$, where $V_i$ are two $1$-dimensional irreducible components. Each is an irreducible affine curve with $t_D(V_i)=Y_0$, $i=1,2$. Moreover, they are isomorphic to each other under the involution $\sigma$ by Proposition [\[d-curve\]](#d-curve){reference-type="ref" reference="d-curve"} (iii) . We also have $t_D: V_i\rightarrow Y_0$ is a one-to-one and onto regular map.
