---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three"
section_id: sec-003-rank-two
section_title: "Rank two"
section_number: null
pages: 6-11
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.978
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three — We classify connected ´etale algebras A’s in pre-modular fusion categories B with rank(B) ≤3 including"
---
A rank two pre-MFC has two simple objects $\{1,X\}$. There are two fusion rings, $\mathbb Z/2\mathbb Z$ and $K(\text{Fib})$. We start from the $\mathbb Z/2\mathbb Z$ case.

### $\mathcal B\simeq\text{Vec}_{\mathbb Z/2\mathbb Z}^\alpha$

The pre-MFCs $\mathcal B$'s have two simple objects $\{1,X_h\}$. They obey the $\mathbb Z/2\mathbb Z$ fusion ring $$\forall b\in\mathcal B,\quad1\otimes b\cong b\cong b\otimes1,\quad X\otimes X\cong1,$$ and have $$\text{FPdim}_{\mathcal B}(1)=1=\text{FPdim}_{\mathcal B}(X).$$ Accordingly, the pre-MFCs have $$\text{FPdim}(\mathcal B)=2.$$ The quantum dimension $d_X$ is a solution of $d_X^2=1$, and there are two possible values $$d_X=\pm1.$$ They both have the same categorical dimension $$D^2(\mathcal B)=2.$$ The $\mathbb Z/2\mathbb Z$ object $X$ can have conformal dimensions $$h=0,\frac14,\frac12,\frac34\quad(\text{mod }1).$$ Those with $h=0,1/2$ mod 1 are anomaly-free $(\alpha=1)$, and the others $h=1/4,3/4$ mod 1 are anomalous $(\alpha=-1)$. Therefore, for the $\mathbb Z/2\mathbb Z$ fusion ring, we have $$4(\text{conformal dimension }h)\times2(\text{quantum dimension }d_X)\times2(\text{categorical dimension }D=\pm\sqrt2)=16$$ pre-MFCs. For a pre-MFC to be unitary, we need $d_X=1$. Furthermore, for such pre-MFCs to be modular, we need $h=\frac14,\frac34$.[^1] Therefore, there are $$2(\text{conformal dimension }h)\times1(d_X=1)\times2(\text{categorical dimension }D)=4$$ unitary MFCs, consistent with [@RSW07]. However, we do not assume non-degeneracy nor (pseudo-)unitarity. Rather, we search for connected étale algebras in all 16 pre-MFCs simultaneously.

First, since $\text{FPdim}(\mathcal B)=2$, an upper bound on ranks of $\mathcal B_A$'s is $$r_\text{max}=2.\label{rank2Z2rmax}$$ Fusion categories up to rank two are completely classified [@O02], and there are only three fusion categories, $\text{Vect}_{\mathbb C}$, $\text{Vec}_{\mathbb Z/2\mathbb Z}^\alpha$, and $\text{Fib}$. The Fibonacci fusion ring has $\text{FPdim}=\frac{5+\sqrt5}2>\text{FPdim}(\mathcal B)$, and is ruled out. The other two satisfy three conditions, and remain as candidates.

As the third step, we check which fusion categories satisfy axioms. We start from the candidate $\text{Vec}_{\mathbb Z/2\mathbb Z}^\alpha$. The fusion category has $\text{FPdim}=2$, and ([\[FPdimA\]](#FPdimA){reference-type="ref" reference="FPdimA"}) demands $\text{FPdim}_{\mathcal B}(A)=1$. For such an object to be connected, the only candidate is $$A\cong1.\label{rank2Z2rank2alg}$$ This is the trivial connected étale algebra giving $\mathcal B_A\simeq\mathcal B$. Next, we study the rank one candidate $\text{Vect}_{\mathbb C}$. The fusion category has $\text{FPdim}=1$, and ([\[FPdimA\]](#FPdimA){reference-type="ref" reference="FPdimA"}) demands $\text{FPdim}_{\mathcal B}(A)=2$. For such an object to be connected, the only candidate is $$A\cong1\oplus X.\label{rank2Z2rank1alg}$$ The candidate is connected, however, fails to be commutative depending on conformal dimensions. Let us study when the candidate is commutative. Since $X^*\cong X$ is invertible, we have [@K05] $$\alpha=F^{XXX}_X=\frac{\nu_2(X)}{d_X}.\label{FSindX}$$ The formula ([\[cbb\]](#cbb){reference-type="ref" reference="cbb"}) gives $$c_{X,X}\cong e^{-2\pi ih_X}\alpha d_Xid_1\cong\begin{cases}id_1&(d_X,h)=(1,0),(-1,\frac12),\\-id_1&(d_X,h)=(1,\frac12),(-1,0),\\+i\cdot id_1&(d_X,h)=(1,\frac14),(-1,\frac34),\\-i\cdot id_1&(d_X,h)=(1,\frac34),(-1,\frac14).\end{cases}$$ Therefore, the candidate ([\[rank2Z2rank1alg\]](#rank2Z2rank1alg){reference-type="ref" reference="rank2Z2rank1alg"}) is commutative iff $(d_X,h)=(1,0),(-1,\frac12)$ mod 1 for $h$. In other words, our pre-MFC $\mathcal B\simeq\text{Vec}_{\mathbb Z/2\mathbb Z}^\alpha$ can admit nontrivial connected étale algebra if it is anomaly-free $\alpha=1$, and anomalous $\alpha=-1$ ones are completely anisotropic. The result has a simple (partial) physical explanation. When the symmetry $\mathbb Z/2\mathbb Z$ is anomaly-free, we can gauge it. Thus, it is expected that there are more algebra objects. On the other hand, if the symmetry is anomalous, it cannot be gauged and there cannot exist a $\mathbb Z/2\mathbb Z$ algebra object. (This is the reason why there are fewer possible values of ground state degeneracies in anomalous theories compared to anomaly-free theories.)

Note that not all commutative algebras are separable. For $A\cong1\oplus X$ to be separable, it should have quantum dimension one. In $\mathcal B_A$, we have [@KO01] $$d_{\mathcal B_A}(c)=\frac{d_{\mathcal B}(c)}{d_{\mathcal B}(A)},$$ where $d_{\mathcal C}(c)$ is the quantum dimension of $c$ as an object of $\mathcal C$. When $d_X=-1$, this cannot be one. Therefore, we conclude $$A\cong1\oplus X\quad(d_X,h_X)=(1,0).\quad(\text{mod }1\text{ for }h)\label{Z2etale}$$

To summarize, we arrive

::: center
::: {#rank2Z2anomfreeresults}
                               Connected étale algebra $A$                                    $\mathcal B_A$         $\text{rank}(\mathcal B_A)$   Lagrangian?
  ------------------------------------------------------------------------------------- --------------------------- ----------------------------- -------------
                                            1                                                  $\mathcal B$                       2                    No
   $1\oplus X$ for ([\[Z2etale\]](#Z2etale){reference-type="ref" reference="Z2etale"})   $\text{Vect}_{\mathbb C}$                1                    No

  : Connected étale algebra in rank two pre-MFC $\mathcal B\simeq\text{Vec}_{\mathbb Z/2\mathbb Z}^1$
:::

,
:::

and

::: center
::: {#rank2Z2anomresults}
   Connected étale algebra $A$   $\mathcal B_A$   $\text{rank}(\mathcal B_A)$   Lagrangian?
  ----------------------------- ---------------- ----------------------------- -------------
                1                 $\mathcal B$                 2                    No

  : Connected étale algebra in rank two pre-MFC $\mathcal B\simeq\text{Vec}_{\mathbb Z/2\mathbb Z}^{-1}$
:::

.
:::

### $\mathcal B\simeq\text{Fib}$

The pre-MFCs $\mathcal B$'s have two simple objects $\{1,X_h\}$ obeying the Fibonacci fusion ring $$\forall b\in\mathcal B,\quad1\otimes b\cong b\cong b\otimes1,\quad X\otimes X\cong1\oplus X.$$ They thus have $$\text{FPdim}_{\mathcal B}(1)=1,\quad\text{FPdim}_{\mathcal B}(X)=\zeta:=\frac{1+\sqrt5}2,$$ and $$\text{FPdim}(\mathcal B)=\frac{5+\sqrt5}2\approx3.6.$$ The quantum dimension $d_X$ is a solution of $d_X^2-d_X-1=0$, and it can take two values $$d_X=\zeta,-\zeta^{-1}.$$ Accordingly, they have categorical dimensions $$D^2(\mathcal B)=\frac{5+\sqrt5}2,\quad\frac{5-\sqrt5}2,$$ respectively, and modular matrices $$\widetilde S=\begin{pmatrix}1&\zeta\\\zeta&-1\end{pmatrix},\quad T=\begin{pmatrix}1&\\&e^{2\pi ih}\end{pmatrix}\quad(d_X=\zeta),$$ or $$\widetilde S=\begin{pmatrix}1&-\zeta^{-1}\\-\zeta^{-1}&-1\end{pmatrix},\quad T=\begin{pmatrix}1&\\&e^{2\pi ih}\end{pmatrix}\quad(d_X=-\zeta^{-1}).$$ The former has $$h=\frac25,\frac35\quad(\text{mod }1),$$ and the latter has $$h=\frac15,\frac45\quad(\text{mod }1).$$ Therefore, we have $$2(\text{quantum dimension }d_X)\times2(\text{conformal dimension }h)\times2(\text{categorical dimension }D(\mathcal B))=8$$ pre-MFCs. Those with $d_X=\zeta$ are unitary, and there are four unitary MFCs, consistent with [@RSW07]. We study connected étale algebras in all eight pre-MFCs simultaneously.

First, since $\text{FPdim}(\mathcal B)\approx3.6$, an upper bound on ranks of $\mathcal B_A$'s is $$r_\text{max}=3.\label{rank2fibrmax}$$ Fusion categories up to rank three have been classified in [@O02; @O13] assuming an existence of pivotal structure for rank three. There are $$1(\text{rank}=1)+2(\text{rank}=2)+5(\text{rank}=3)=8$$ fusion rings. All but one are free of multiplicity, and they are summarized in AnyonWiki [@anyonwiki] based on [@LPR20; @VS22]. The one with multiplicity has fusion ring $K(1,0,2,0)$ in the notation of [@O13], however, it has Frobenius-Perron dimension[^2] $\text{FPdim}(\mathcal C)=6+2\sqrt3\approx9.4$, and we can rule it out at the outset. As in [@KK23GSD], one can easily check there are no one- and three-dimensional NIM-reps. Hence, we are left with rank two $\mathcal B_A$'s. They have fusion rings[^3] $$\text{FR}^{2,0}_1,\text{FR}^{2,0}_2.$$ In order to search for all rank two $\mathcal B_A$'s, we solve two-dimensional NIM-reps. We find a unique (up to basis transformations) solution $$n_1=1_2,\quad n_X=\begin{pmatrix}0&1\\1&1\end{pmatrix}.$$ Let $m_1,m_2\in\mathcal M$ be basis. The NIM-rep gives actions $$\begin{aligned}
    1\triangleright m_j&\cong m_j,\\
    X\triangleright m_1&\cong m_2,\\
    X\triangleright m_2&\cong m_1\oplus m_2,
\end{aligned}$$ or monoidal products $$\begin{aligned}
    F(m_j)\cong F(1\triangleright m_j)\equiv\underline{\text{Hom}}(m,1\triangleright m_j)&\cong\underline{\text{Hom}}(m,m_j),\\
    F(m_2)\cong F(X\triangleright m_1)\equiv\underline{\text{Hom}}(m,X\triangleright m_1)&\cong X\otimes\underline{\text{Hom}}(m,m_1),\\
    F(m_1)\oplus F(m_2)\cong F(X\triangleright m_2)\equiv\underline{\text{Hom}}(m,X\triangleright m_2)&\cong X\otimes\underline{\text{Hom}}(m,m_2).
\end{aligned}$$ In order to find forms of algebras, we set an ansatz $$A\cong F(m)\cong a1\oplus bX,$$ with $a,b\in\mathbb N$. If $m\cong m_1$, the second monoidal product yields $$F(m_2)\cong b1\oplus(a+b)X.$$ The third monoidal product is automatically satisfied. For the candidate to be connected, we need $a=1$, or $A\cong F(m_1)\cong1\oplus bX$. It has $\text{FPdim}_{\mathcal B}(A)=1+b\zeta$. For this to solve ([\[FPdimA\]](#FPdimA){reference-type="ref" reference="FPdimA"}), we need $b=0$ and fusion ring $\text{FR}^{2,0}_2$. Namely, we only get the trivial connected étale algebra $A\cong1$ giving $\mathcal B_A\simeq\mathcal B$. The other case $m\cong m_2$ gives the same result.

In conclusion, we arrive

::: center
::: {#rank2fibresults}
   Connected étale algebra $A$   $\mathcal B_A$   $\text{rank}(\mathcal B_A)$   Lagrangian?
  ----------------------------- ---------------- ----------------------------- -------------
                1                 $\mathcal B$                 2                    No

  : Connected étale algebra in rank two pre-MFC $\mathcal B\simeq\text{Fib}$
:::

.
:::

Note that since rank three $\mathcal B_A$'s are ruled out, we do not have to assume $\mathcal B_A$ admits a pivotal structure or its fusion ring be multiplicity-free. The result implies all $\text{Fib}$'s are completely anisotropic, giving another proof of the known fact [@BD11].

[^1]: A pre-MFC with $X_h$ has $S$-matrix (in the basis $\{1,X\}$) $$\widetilde S=\begin{pmatrix}1&d_X\\d_X&e^{-4\pi ih}\end{pmatrix}.$$

[^2]: Simple objects $\{1,X,Y\}$ obey fusion rules

    ::: center
       $\otimes$   1           $X$           $Y$
      ----------- --- --------------------- -----
          $1$      1           $X$           $Y$
          $X$          $1\oplus2X\oplus Y$   $X$
          $Y$                                $1$

    ,
    :::

    and have $$\text{FPdim}_{\mathcal C}(1)=1=\text{FPdim}_{\mathcal C}(Y),\quad\text{FPdim}_{\mathcal C}(X)=1+\sqrt3.$$

[^3]: The notation in [@anyonwiki] is the following. A rank $r$ fusion ring with $n$ non-self-dual simple objects is denoted by $\text{FR}^{r,n}_i$. The subscript $i=1,\dots$ labels different fusion rings with the same $r$ and $n$.
