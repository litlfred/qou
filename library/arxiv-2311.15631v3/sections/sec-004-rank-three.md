---
doc_id: arxiv-2311.15631v3
doc_title: "Classification of connected étale algebras in pre-modular fusion categories up to rank three"
section_id: sec-004-rank-three
section_title: "Rank three"
section_number: null
pages: 11-23
source_pdf: 2311.15631v3.pdf
source_sha256: a3cc6d51cd04fc07
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.979
doc_brief: "Classification of connected étale algebras in pre-modular fusion categories up to rank three — We classify connected ´etale algebras A’s in pre-modular fusion categories B with rank(B) ≤3 including"
---
A rank three pre-MFC has three simple objects $\{1,X,Y\}$. As we reviewed above, with the assumption of pivotal structure, there are five fusion rings, $\text{FR}^{3,2}_1,\text{FR}^{3,0}_1,\text{FR}^{3,0}_2,\text{FR}^{3,0}_3,K(1,0,2,0)$. The last with multiplicity is known [@HH07] not to admit braiding. Thus, we classify connected étale algebras in the first four[^1] pre-MFCs.

### $\mathcal B\simeq\text{Vec}_{\mathbb Z/3\mathbb Z}^1$ {#Z3}

The pre-MFCs $\mathcal B$'s have three simple objects $\{1,X_{h_X},Y_{h_Y}\}$ obeying $\mathbb Z/3\mathbb Z$ fusion ring

::: center
   $\otimes$   1   $X$   $Y$
  ----------- --- ----- -----
      $1$      1   $X$   $Y$
      $X$          $Y$   $1$
      $Y$                $X$

.
:::

Hence, they have $$\text{FPdim}_{\mathcal B}(1)=\text{FPdim}_{\mathcal B}(X)=\text{FPdim}_{\mathcal B}(Y)=1,$$ and $$\text{FPdim}(\mathcal B)=3.$$ The quantum dimensions $d_X,d_Y$ are solutions of $d_X^2=d_Y,\ d_Y^2=d_X,\ d_Xd_Y=1$. The only solution is $$d_X=d_Y=1.$$ Thus, the pre-MFCs are unitary. Consequently, the pre-MFCs have a unique categorical dimension $$D^2(\mathcal B)=3.$$ The nontrivial simple objects are dual to each other, $X^*\cong Y$, and they have the same conformal dimensions $$h_X=h_Y=0,\frac13,\frac23\quad(\text{mod }1).$$ This implies the pre-MFCs are always anomaly-free $\alpha=1$. (We have already specified this fact in the name of this subsubsection.) Therefore, there are $$3(\text{conformal dimension }h_X=h_Y)\times2(\text{categorical dimension }D(\mathcal B)=\pm\sqrt3)=6$$ pre-MFCs with $\mathbb Z/3\mathbb Z$ fusion ring. Among them, those with nontrivial conformal dimensions are modular. There are four of them, consistent with [@RSW07]. We study all six pre-MFCs including degenerate ones simultaneously.

In order to classify connected étale algebras in our pre-MFCs, we first find an upper bound on $\text{rank}(\mathcal B_A)$. It is given by $$r_\text{max}=3.\label{rank3Z3rmax}$$ As we reviewed above, there are eight fusion categories which admit pivotal structures, but the condition $\text{FPdim}(\mathcal B_A)\le\text{FPdim}(\mathcal B)=3$ narrows down to three with fusion rings $$\text{FR}^{1,0}_1,\text{FR}^{2,0}_1,\text{FR}^{3,2}_1.$$ The rank two fusion ring cannot solve ([\[FPdimA\]](#FPdimA){reference-type="ref" reference="FPdimA"}), and is ruled out. This leaves only two candidates, $\text{FR}^{1,0}_1,\text{FR}^{3,2}_1$. Let us study the two candidates in detail.

We start from the rank three candidate. It has $\text{FPdim}(\mathcal C)=3$, and demands $\text{FPdim}_{\mathcal B}(A)=1$. This is nothing but the trivial connected étale algebra $A\cong1$ giving $\mathcal B_A\simeq\mathcal B$. Next, we study the rank one candidate $\text{Vect}_{\mathbb C}$. It has $\text{FPdim}=1$, and demands $\text{FPdim}_{\mathcal B}(A)=3$. Since any étale algebras are self-dual [@DMNO10], we are left with two possibilities, $1\oplus1\oplus1$ or $1\oplus X\oplus Y$. Connectedness of algebra rules out the first. Thus, the only candidate is $A\cong1\oplus X\oplus Y$. This is connected and separable, but it fails to be commutative depending on conformal dimensions. Let us first show those with nontrivial conformal dimensions are non-commutative. We check the necessary condition ([\[necessarycommutative\]](#necessarycommutative){reference-type="ref" reference="necessarycommutative"}). The relevant double-braidings are given by $$c_{X,X}\cdot c_{X,X}\cong e^{-2\pi ih_X}id_Y,\quad c_{Y,X}\cdot c_{X,Y}\cong e^{-4\pi ih_X}id_1,\quad c_{Y,Y}\cdot c_{Y,Y}\cong e^{-2\pi ih_Y}id_X.$$ (We used $h_X=h_Y$.) The phases are nontrivial for nontrivial conformal dimensions $h_X=h_Y=\frac13,\frac23$ mod 1, and they fail to satisfy the necessary condition. Hence, they are non-commutative. On the other hand, when the conformal dimensions are trivial $h_X=h_Y=0$ mod 1, the phases become trivial, and they pass the necessary condition. We thus need to compute half-braidings $c_{b,b'}$'s. We find[^2] $$c_{X,X}\cong id_Y,\quad c_{X,Y}\cong id_1,\quad c_{Y,Y}\cong id_X.$$ Therefore, the candidate $A\cong1\oplus X\oplus Y$ is commutative for trivial conformal dimensions.

To summarize, we found

::: center
::: {#rank3Z3results}
           Connected étale algebra $A$                $\mathcal B_A$         $\text{rank}(\mathcal B_A)$   Lagrangian?
  --------------------------------------------- --------------------------- ----------------------------- -------------
                        1                              $\mathcal B$                       3                    No
   $1\oplus X\oplus Y$ for $h_X=h_Y=0$ (mod 1)   $\text{Vect}_{\mathbb C}$                1                    No

  : Connected étale algebra in rank three pre-MFC $\mathcal B\simeq\text{Vec}_{\mathbb Z/3\mathbb Z}^1$
:::

.
:::

In other words, the pre-MFCs $\text{Vec}_{\mathbb Z/3\mathbb Z}^1$'s with nontrivial conformal dimensions $h_X=h_Y=\frac13,\frac23$ mod 1 are completely anisotropic.

### $\mathcal B\simeq\text{Ising}$

The pre-MFCs $\mathcal B$'s have three simple objects $\{1,X_{h_X},Y_{h_Y}\}$ obeying the Ising fusion ring

::: center
   $\otimes$   1   $X$       $Y$
  ----------- --- ----- -------------
      $1$      1   $X$       $Y$
      $X$          $1$       $Y$
      $Y$                $1\oplus X$

.
:::

Hence, they have $$\text{FPdim}_{\mathcal B}(1)=1=\text{FPdim}_{\mathcal B}(X),\quad\text{FPdim}_{\mathcal B}(Y)=\sqrt2,$$ and $$\text{FPdim}(\mathcal B)=4.$$ It is known [@DGNO09] that Ising fusion categories admit spherical structures and (non-degenerate) braidings. (We will make the most of the non-degeneracy later.) The quantum dimensions $d_X,d_Y$ are solutions of $d_X^2=1,\ d_Xd_Y=d_Y,\ d_Y^2=1+d_X$, and there are two solutions $$d_X=1,\quad d_Y=\pm\sqrt2.$$ (The sign of $d_Y$ fixes the spherical structure.) The pre-MFCs with positive $d_Y$ are unitary. The pre-MFCs have a unique categorical dimension $$D^2(\mathcal B)=4.$$ It is known that conformal dimensions take values $$h_X=\frac12,\quad h_Y=\pm\frac1{16},\ \pm\frac3{16},\ \pm\frac5{16},\ \pm\frac7{16}\quad(\text{mod }1).$$ (The conformal dimension $h_X=\frac12$ implies the rank two braided fusion subcategory generated by $\{1,X\}$ is isomorphic to $\text{sVec}$. Hence, an obvious $\mathbb Z/2\mathbb Z$ algebra $A\cong1\oplus X$ fails to be commutative because $c_{X,X}\cong-id_1$.) Therefore, there are $$2(\text{quantum dimension }d_Y)\times8(\text{conformal dimension }h_Y)\times2(\text{categorical dimension }D(\mathcal B))=32$$ pre-MFCs. Those with $d_Y=+\sqrt2$ are unitary, and there are 16 of them, consistent with [@RSW07]. We search for connected étale algebras in all 32 pre-MFCs simultaneously. Since the method is the same, we will be brief.

The Frobenius-Perron dimension $\text{FPdim}(\mathcal B)=4$ gives an upper bound $$r_\text{max}=4.\label{rank4Isingrmax}$$ Since there are no complete list of fusion categories up to rank four, here we practically have to assume fusion rings of $\mathcal B_A$'s be multiplicity-free. Then, there are seven[^3] fusion rings, but only five $$\text{FR}^{1,0}_1,\text{FR}^{2,0}_1,\text{FR}^{3,0}_1,\text{FR}^{4,0}_1,\text{FR}^{4,2}_1$$ satisfy the three conditions. Let us check which of them satisfy axioms.

We start from those with $\text{FPdim}=4$. The relation ([\[FPdimA\]](#FPdimA){reference-type="ref" reference="FPdimA"}) requires $\text{FPdim}_{\mathcal B}(A)=1$. For such an algebra to be connected, the only possibility is the trivial one $A\cong1$ giving $\mathcal B_A\simeq\mathcal B$. (This rules out rank four $\mathcal B_A$'s.) Next, let us see the rank one scenario. One finds there is no one-dimensional NIM-rep, and the fusion ring $\text{FR}^{1,0}_1$ is ruled out. Finally, let us study the last candidate $\text{FR}^{2,0}_1$. The scenario demands $\text{FPdim}_{\mathcal B}(A)=2$. For such an algebra to be connected, the only possibility is $A\cong1\oplus X$. Indeed, this is an algebra,[^4] however, it fails to be commutative because $X$ is a fermion $c_{X,X}\cong-id_1$. Thus, we do not get new connected étale algebra from the rank two scenario.

To summarize, we found

::: center
::: {#rank3isingresults}
   Connected étale algebra $A$   $\mathcal B_A$   $\text{rank}(\mathcal B_A)$   Lagrangian?
  ----------------------------- ---------------- ----------------------------- -------------
                1                 $\mathcal B$                 3                    No

  : Connected étale algebra in rank three pre-MFC $\mathcal B\simeq\text{Ising}$
:::
:::

regardless of quantum dimension $d_Y$, conformal dimension $h_Y$, or categorical dimension $D(\mathcal B)$. The result motivates the

**Theorem.** *All* $\mathcal B\simeq\text{Ising}$*'s are completely anisotropic.*

*Proof.* So far, we pretended we do not know $\mathcal B\simeq\text{Ising}$ be modular. However, as we recalled above, they are known to be modular [@DGNO09]. Thus, we can employ further constraints. When the ambient category $\mathcal B$ is modular, it is known [@KO01; @DMNO10] that the category of dyslectic modules $\mathcal B_A^0$ for connected étale algebra $A$ is modular obeying $$\begin{split}
    \text{FPdim}(\mathcal B_A^0)&=\frac{\text{FPdim}(\mathcal B)}{(\text{FPdim}_{\mathcal B}(A))^2},\\
    e^{2\pi ic(\mathcal B)/8}&=e^{2\pi ic(\mathcal B_A^0)/8}.
\end{split}\label{constsMFCB}$$ Here, the full subcategory $\mathcal B_A^0$ of $\mathcal B_A$ consists of dyslectic modules $(m,p)\in\mathcal B_A$ such that $p\cdot c_{A,m}\cdot c_{m,A}=p$. Since $\mathcal B_A^0\subset\mathcal B_A$, we also have $$\text{rank}(\mathcal B_A^0)\le\text{rank}(\mathcal B)\le\lfloor\text{FPdim}(\mathcal B)\rfloor.$$ In our example, we learn the maximal rank of $\mathcal B_A^0$ is four. Fortunately, MFCs up to rank four are completely classified [@GK94; @RSW07].[^5] According to the lists, the only MFCs which can match the (additive) central charges are Ising MFCs. Since the MFCs have $\text{FPdim}=4$, it demands $\mathcal B_A^0\simeq\mathcal B_A\simeq\mathcal B$, and $\text{FPdim}_{\mathcal B}(A)=1$. Therefore, the only connected étale algebra is the trivial one $A\cong1$, showing $\mathcal B\simeq\text{Ising}$ be completely anisotropic. $\square$

**Remark.** We have already included the theorem in the Table [2](#rank3isingresults){reference-type="ref" reference="rank3isingresults"}.

**Remark.** Some Ising MFCs are realized by Wess-Zumino-Witten (WZW) models:

::: center
   Unitary $\text{Ising}$ w/ $h_Y$ (mod 1)            Realization
  ----------------------------------------- --------------------------------
                   $3/16$                    $\widehat{\mathfrak{su}}(2)_2$
                   $5/16$                    $\widehat{\mathfrak{sp}}(4)_1$
                   $7/16$                    $\widehat{\mathfrak{so}}(7)_1$
                   $15/16$                   $(\widehat{\mathfrak{e_8}})_2$

.
:::

Connected étale algebras in MFCs $\mathcal C(\mathfrak g,k)$ describing $\widehat{\mathfrak{g}}_k$ WZW models are especially called quantum subgroups [@O00]. They have been studied extensively, and many results are known. Such connected étale algebras were classified in [@KO01] (for $\widehat{\mathfrak{su}}(2)_k$), in [@EP09] (for $\widehat{\mathfrak{su}}(3)_k$), in [@CEM23] (for $\widehat{\mathfrak{su}}(4)_k$), and many more in [@G23] (see also [@EM21]). Thus, the classification results for some Ising MFCs are known. Our results are consistent with them.[^6] However, we could not find a literature classifying connected étale algebras in the other Ising MFCs (in particular, non-unitary ones). Our results for those MFCs would be new. This example demonstrates a unified nature of our method; since what is central in our method is the Frobenius-Perron dimensions, it allows us to classify connected étale algebras in pre-MFCs (or more generally BFCs) with the same fusion ring -- including degenerate and non-(pseudo-)unitary ones -- simultaneously.

### $\mathcal B\simeq\text{Rep}(S_3)$

The pre-MFCs $\mathcal B$'s have three simple objects $\{1,X_{h_X},Y_{h_Y}\}$ obeying the fusion ring

::: center
   $\otimes$   1   $X$           $Y$
  ----------- --- ----- ---------------------
      $1$      1   $X$           $Y$
      $X$          $1$           $Y$
      $Y$                $1\oplus X\oplus Y$

.
:::

Hence, they have $$\text{FPdim}_{\mathcal B}(1)=1=\text{FPdim}_{\mathcal B}(X),\quad\text{FPdim}_{\mathcal B}(Y)=2,$$ and $$\text{FPdim}(\mathcal B)=6.$$ The quantum dimensions $d_X,d_Y$ are (nonzero) solutions to $d_X^2=1,\ d_Xd_Y=d_Y,\ d_Y^2=1+d_X+d_Y$, and there are two of them $$d_X=1,\quad d_Y=-1,2.$$ Accordingly, there are two categorical dimensions $$D^2(\mathcal B)=3,6.$$ As we reviewed in Appendix [\[repS3confdim\]](#repS3confdim){reference-type="ref" reference="repS3confdim"}, there are two classes of pre-MFCs with fusion ring $K(\text{Rep}(S_3))$, one non-symmetric, and another symmetric. The non-symmetric pre-MFCs have conformal dimensions $$h_X=0,\quad h_Y=\frac13,\frac23\quad(\text{mod }1)$$ with $d_Y=2$, and symmetric pre-MFCs have $$h_X=h_Y=0\quad(\text{mod }1).$$ Therefore, there are $$2(\text{sign of categorical dimension }D(\mathcal B))\times2(h_Y=\pm\frac13)=4$$ non-symmetric and $$2(\text{sign of categorical dimension }D(\mathcal B))\times2(d_Y=-1,2)=4$$ symmetric pre-MFCs, eight in total. Since none of them is modular, they should not be listed in MFCs, consistent with [@RSW07]. We classify connected étale algebras in all eight pre-MFCs simultaneously.

First, since $\text{FPdim}(\mathcal B)=6$, the rank of categories of right $A$-modules is bounded from above by $$r_\text{max}=6.\label{rank3RepD3rmax}$$ Fusion categories up to rank six have been classified in [@LPR20; @VS22] assuming multiplicity-free fusion rings. In order to apply our method, for a moment, we assume $\mathcal B_A$ have multiplicity-free fusion ring. Later, employing an improved method, we relax the assumption and complete the classification of connected étale algebras.

According to [@anyonwiki], we find seven fusion rings $$\text{FR}^{1,0}_1,\text{FR}^{2,0}_1,\text{FR}^{3,2}_1,\text{FR}^{3,0}_2,\text{FR}^{4,2}_2,\text{FR}^{6,2}_1,\text{FR}^{6,4}_1$$ can describe $\mathcal B_A$'s. The same analysis was done in [@KK23GSD], and we found only four $$\text{FR}^{1,0}_1,\text{FR}^{2,0}_1,\text{FR}^{3,2}_1,\text{FR}^{3,0}_2$$ can satisfy axioms. They correspond to candidates $$A\cong1\oplus X\oplus2Y,\quad1\oplus Y,\quad1\oplus X,\quad1,$$ respectively. Which of them are connected étale? The answer depends on conformal dimensions, or non/symmetry of our ambient category. We start from the non-symmetric ones.

#### Non-symmetric $\text{Rep}(S_3)$.

In this case, the simple object $Y$ has nontrivial braiding. The first two candidates fail to satisfy the necessary condition ([\[necessarycommutative\]](#necessarycommutative){reference-type="ref" reference="necessarycommutative"}),[^7] and we can safely discard them. We do know the last two are connected étale algebras.

#### Symmetric $\text{Rep}(S_3)$.

In this case, the simple object $Y$ also has trivial conformal dimension, and the candidates containing $Y$ can be commutative. We have to check whether the first two satisfy axioms of commutative algebra. Naively, one has to solve associativity axioms, however, luckily, we do not need any computation.[^8] The second candidate $A\cong1\oplus Y$ is known [@CZW18] to be connected étale when $d_Y=2$.[^9] (They call it condensable or normal.) Thus, we are left with the first candidate $A\cong1\oplus X\oplus2Y$. Note that we are in a special situation; our ambient category is symmetric, and if $A$ defines an algebra, it gives $\mathcal B_A\simeq\text{Vect}_{\mathbb C}$. Since the condensation gives a tensor functor $F:\mathcal B\to\mathcal B_A$, our question can be rephrased as follows. Is a symmetric fusion category $\mathcal B\simeq\text{Rep}(S_3)$ Tannakian? (A symmetric fusion category admitting a braided tensor functor $F:\mathcal B\to\text{Vect}_{\mathbb C}$ is called Tannakian. Since our $\mathcal B$ is symmetric and the only simple object of $\text{Vect}_{\mathbb C}$ is the unit, a tensor functor is automatically braided.) Once we have rewritten our problem in this form, we can immediately answer it; $\mathcal B\simeq\text{Rep}(S_3)$ is Tannakian iff it is positive [@D02; @EGNO15]. Recall a symmetric fusion category $\mathcal B$ is called positive if $\forall b\in\mathcal B$, $d_b\in\mathbb N^\times$. Namely, $A\cong1\oplus X\oplus2Y$ is connected étale[^10] if $d_Y=2$, but not otherwise. Finally, for $A\cong1\oplus X$ to be separable, we also need $d_Y=2$. The reason is as follows. In view of anyon condensation, $Y$ 'splits' into two simple objects. Thus, simple objects of $\mathcal B_A$ are given by $$1\oplus X,\quad Y,\quad Y.$$ They have quantum dimensions [@KO01] $d_{\mathcal B_A}(c)=\frac{d_{\mathcal B}(c)}{d_{\mathcal B}(A)}$. Since the only rank three fusion category with Frobenius-Perron dimension three is $\text{Vec}_{\mathbb Z/3\mathbb Z}^1$, for $A$ to be separable, the three simple objects should form $\text{Vec}_{\mathbb Z/3\mathbb Z}^1$. As we saw in section [0.0.1](#Z3){reference-type="ref" reference="Z3"}, simple objects of the fusion category have quantum dimensions one. Thus, for $A$ to give a fusion category, the simple objects need to have quantum dimensions one. This condition is satisfied only when $d_Y=2$.

So far, we assumed $K(\mathcal B_A)$ be multiplicity-free. However, employing the improved method [@KK23MFCrank9], we can relax the assumption.

We work with an ansatz $$A\cong1\oplus n_XX\oplus n_YY$$ with $n_j\in\mathbb N$. It has $$\text{FPdim}_{\mathcal B}(A)=1+n_X+2n_Y.$$ For this to obey $$1\le\text{FPdim}_{\mathcal B}(A)\le\text{FPdim}(\mathcal B)$$ resulting from ([\[FPdimA\]](#FPdimA){reference-type="ref" reference="FPdimA"}), the natural numbers can take only 12 values $$\begin{aligned}
    (n_X,n_Y)=&(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),\\
    &(3,0),(2,1),(1,2),(4,0),(3,1),(5,0).
\end{aligned}$$ The first is nothing but the trivial connected étale algebra $A\cong1$ giving $\mathcal B_A^0\simeq\mathcal B_A\simeq\mathcal B$. Among the other 11 candidates, five are ruled out by studying Frobenius-Perron dimensions. The two candidates $(n_X,n_Y)=(1,1),(3,0)$ have $\text{FPdim}_{\mathcal B}=4$, and demands $\text{FPdim}(\mathcal B_A)=\frac32$. However, there is no such fusion category, and the candidates are ruled out. Similarly, three candidates $(n_X,n_Y)=(0,2),(2,1),(4,0)$ have $\text{FPdim}_{\mathcal B}=5$, and demand $\text{FPdim}(\mathcal B_A)=\frac65$, but there is no such fusion category. Thus, the three candidates are also ruled out. We are left with six nontrivial candidates: $$(n_X,n_Y)=(1,0),(0,1),(2,0),(1,2),(3,1),(5,0).$$ Regardless of conformal dimensions, three of them, $(n_X,n_Y)=(2,0),(3,1),(5,0)$ or $A\cong1\oplus2X,1\oplus3X\oplus Y,1\oplus5X$, are ruled out by detailed study.

#### $A\cong1\oplus2X$.

It has $\text{FPdim}_{\mathcal B}(A)=3$, and demands $\text{FPdim}(\mathcal B_A)=2$. With the free module functor $F_A:=-\otimes A:\mathcal B\to\mathcal B_A$, we find candidate simple objects of $\mathcal B_A$: $$1\oplus2X,\quad2\oplus X,\quad3Y.$$ They have Frobenius-Perron dimensions $1,1,2$, respectively. Their contributions to $\text{FPdim}(\mathcal B_A)$ exceed two, and the candidate is ruled out.

#### $A\cong1\oplus3X\oplus Y$.

It has $\text{FPdim}_{\mathcal B}(A)=6$, and demands $\text{FPdim}(\mathcal B_A)=1$. The candidate simple objects of $\mathcal B_A$ are given by $$1\oplus3X\oplus Y,\quad3\oplus X\oplus Y,\quad\dots\ .$$ There exists additional simple objects, but their presence does not affect the following discussion. Their contributions to $\text{FPdim}(\mathcal B_A)$ exceed one, and the candidate is ruled out.

#### $A\cong1\oplus5X$.

It has $\text{FPdim}_{\mathcal B}(A)=6$, and demands $\text{FPdim}(\mathcal B_A)=1$. We obtain candidate simple objects (assuming the smallest Frobenius-Perron dimensions) $$1\oplus5X,\quad5\oplus X,\quad3Y.$$ They have $\text{FPdim}_{\mathcal B_A}=1,1,1$, and their contributions to $\text{FPdim}(\mathcal B_A)$ exceed one. Thus, the candidate is also ruled out.

Now, we are only left with three nontrivial candidates $$(n_X,n_Y)=(1,0),(0,1),(1,2).$$ We have seen that these give nontrivial connected étale algebras depending on quantum and conformal dimensions. From this analysis, we succeeded to relax the assumption of multiplicity on $K(\mathcal B_A)$.

To summarize, we found

::: center
::: {#rank3nonsymRepS3results}
   Connected étale algebra $A$              $\mathcal B_A$               $\text{rank}(\mathcal B_A)$   Lagrangian?
  ----------------------------- --------------------------------------- ----------------------------- -------------
                1                            $\mathcal B$                             3                    No
           $1\oplus X$           $\text{Vec}_{\mathbb Z/3\mathbb Z}^1$                3                    No

  : Connected étale algebra in rank three non-symmetric pre-MFC $\mathcal B\simeq\text{Rep}(S_3)$
:::
:::

for non-symmetric, and

::: center
::: {#rank3symRepS3results}
     Connected étale algebra $A$                   $\mathcal B_A$                 $\text{rank}(\mathcal B_A)$   Lagrangian?
  --------------------------------- -------------------------------------------- ----------------------------- -------------
                  1                                 $\mathcal B$                               3                    No
       $1\oplus X$ for $d_Y=2$         $\text{Vec}_{\mathbb Z/3\mathbb Z}^1$                   3                    No
       $1\oplus Y$ for $d_Y=2$       $\text{Vec}_{\mathbb Z/2\mathbb Z}^\alpha$                2                    No
   $1\oplus X\oplus2Y$ for $d_Y=2$           $\text{Vect}_{\mathbb C}$                         1                    No

  : Connected étale algebra in rank three symmetric pre-MFC $\mathcal B\simeq\text{Rep}(S_3)$
:::
:::

for symmetric $\mathcal B\simeq\text{Rep}(S_3)$. Thus, two symmetric ones with $d_Y=-1$ are completely anisotropic, while the other six $\mathcal B\simeq\text{Rep}(S_3)$'s fail to be completely anisotropic.

### $\mathcal B\simeq psu(2)_5$

The pre-MFCs $\mathcal B$'s have three simple objects $\{1,X_{h_X},Y_{h_Y}\}$ obeying the fusion ring $\text{FR}^{3,0}_3$

::: center
   $\otimes$   1       $X$               $Y$
  ----------- --- ------------- ---------------------
      $1$      1       $X$               $Y$
      $X$          $1\oplus Y$       $X\oplus Y$
      $Y$                        $1\oplus X\oplus Y$

.
:::

Hence, they have $$\text{FPdim}_{\mathcal B}(1)=1,\quad\text{FPdim}_{\mathcal B}(X)=\frac{\sin\frac{2\pi}7}{\sin\frac\pi7}\approx1.802,\quad\text{FPdim}_{\mathcal B}(Y)=\frac{\sin\frac{3\pi}7}{\sin\frac\pi7}\approx2.247,$$ and $$\text{FPdim}(\mathcal B)=\frac7{4\sin^2\frac\pi7}\approx9.3.$$ The quantum dimensions $d_X,d_Y$ are solutions of $d_X^2=1+d_Y,\ d_Y^2=1+d_X+d_Y,\ d_Xd_Y=d_X+d_Y$. There are three solutions $$(d_X,d_Y)=(\frac{\sin\frac\pi7}{\cos\frac\pi{14}},-\frac{\sin\frac{2\pi}7}{\cos\frac\pi{14}}),\ (-\frac{\sin\frac{3\pi}7}{\cos\frac{3\pi}{14}},\frac{\sin\frac\pi7}{\cos\frac{3\pi}{14}}),\ (\frac{\sin\frac{2\pi}7}{\sin\frac\pi7},\frac{\sin\frac{3\pi}7}{\sin\frac\pi7}),$$ and categorical dimensions $$D^2(\mathcal B)=\frac7{4\cos^2\frac\pi{14}},\quad\frac7{4\cos^2\frac{3\pi}{14}},\quad\frac7{4\sin^2\frac\pi7},$$ respectively. The pre-MFCs have conformal dimensions $$(h_X,h_Y)=\begin{cases}(\frac37,\frac17),(\frac47,\frac67)&(\text{1st quantum dimensions}),\\
    (\frac27,\frac37),(\frac57,\frac47)&(\text{2nd quantum dimensions}),\\
    (\frac17,\frac57),(\frac67,\frac27)&(\text{3rd quantum dimensions}),\end{cases}\quad(\text{mod }1)\label{psu25confdim}$$ respectively. Therefore, there are $$3(\text{quantum dimension})\times2(\text{sign of categorical dimension }D(\mathcal B))\times2(\text{conformal dimension})=12$$ pre-MFCs. (Actually, they are all modular. See the lemma in Appendix [\[psu25\]](#psu25){reference-type="ref" reference="psu25"}.) Those with the third quantum dimensions are unitary, and there are four of them, consistent with [@RSW07]. We study connected étale algebras in all 12 MFCs.

As the first step, we find an upper bound $$r_\text{max}=9\label{rank3psu25rmax}$$ on $\text{rank}(\mathcal B_A)$.[^11] According to [@anyonwiki], we find $\mathcal B_A$ can have only two fusion rings (assuming $K(\mathcal B_A)$ be multiplicity-free) $$\text{FR}^{1,0}_1,\text{FR}^{3,0}_3.$$ The second scenario requires $\text{FPdim}_{\mathcal B}(A)=1$. For such a candidate to be connected, the only candidate is $A\cong1$. This is the trivial connected étale algebra giving $\mathcal B_A\simeq\mathcal B$. To check the first candidate with rank one, we search for one-dimensional NIM-reps. One finds no solution, ruling out the possibility of rank one $\mathcal B_A$.

To summarize, we found

::: center
::: {#rank3psu25results}
   Connected étale algebra $A$   $\mathcal B_A$   $\text{rank}(\mathcal B_A)$   Lagrangian?
  ----------------------------- ---------------- ----------------------------- -------------
                1                 $\mathcal B$                 3                    No

  : Connected étale algebra in rank three pre-MFC $\mathcal B\simeq psu(2)_5$
:::

.
:::

The result motivates the

**Theorem.** *All $\mathcal B\simeq psu(2)_5$'s are completely anisotropic.*

*Proof.* As we recalled above, all pre-MFCs are actually modular. Thus, the algebra should obey ([\[constsMFCB\]](#constsMFCB){reference-type="ref" reference="constsMFCB"}). Since $\text{FPdim}(\mathcal B_A^0)\ge1$, we obtain an inequality[^12] $$1\le\left(\text{FPdim}_{\mathcal B}(A)\right)^2\le\text{FPdim}(\mathcal B).\label{FPdimA2bound}$$ The most general candidate can be written as $$A\cong\bigoplus_{j=1}^{\text{rank}(\mathcal B)}n_jb_j$$ with $n_j\in\mathbb N$. In order to get connected algebra, we set $n_j=1$ for $b_j\cong1$ at the outset. The candidate in our example thus has $$\text{FPdim}_{\mathcal B}(A)=1+\frac1{\sin\frac\pi7}\left(n_X\sin\frac{2\pi}7+n_Y\sin\frac{3\pi}7\right).$$ For this to obey ([\[FPdimA2bound\]](#FPdimA2bound){reference-type="ref" reference="FPdimA2bound"}), there are only two possibilities $$(n_X,n_Y)=(0,0),(1,0).$$ The first candidate is nothing but the trivial connected étale algebra $A\cong1$ giving $\mathcal B_A^0\simeq\mathcal B_A\simeq\mathcal B$. The second candidate means $A\cong1\oplus X$. It has double braiding $$c_{A,A}\cdot c_{A,A}\cong(1+e^{-4\pi ih_X})\iota\cdot id_1\cdot p+2\iota\cdot id_X\cdot p+e^{2\pi i(h_Y-2h_X)}\iota\cdot id_Y\cdot p.$$ Since $X$ has nontrivial conformal dimensions, the candidate fails to satisfy the necessary condition ([\[necessarycommutative\]](#necessarycommutative){reference-type="ref" reference="necessarycommutative"}), and it is ruled out. $\square$

**Remark.** We have already included the theorem in the Table [5](#rank3psu25results){reference-type="ref" reference="rank3psu25results"}.

[^1]: The fourth with fusion ring $\text{FR}^{3,0}_3$ does not seem to have a common name. Thus, we call it $psu(2)_5$ borrowing one famous realization.

[^2]: Employing the known [@RSW07] associators $F^{b_i,b_j,b_k}_{b_l}=1$, one can easily solve hexagon equations to find $R$-matrices $$R^{X,X}_Y=R^{X,Y}_1=R^{Y,X}_1=R^{Y,Y}_X=+1,$$ giving the half-braidings.

[^3]: We could take the rank three fusion ring with multiplicity into account, but it is ruled out because $\text{FPdim}>\text{FPdim}(\mathcal B)=4$.

[^4]: An easiest way to see this fact is to realize that $X$ generates anomaly-free $\mathbb Z/2\mathbb Z$ symmetry in physical systems.

[^5]: See also [@BNRW15] for classification of MFCs at rank five.

[^6]: For $\widehat{\mathfrak{su}}(2)_2$, $\mathcal B_A$ corresponds to the $A_3$ Dynkin diagram. Thus, the category $\mathcal B_A$ has three simple objects, implying $A\cong1$. For $\widehat{\mathfrak{sp}}(4)_1$ and $\widehat{\mathfrak{so}}(7)_1$, they do not admit exotic quantum subgroups. That is, all nontrivial algebras are their centers $\mathbb Z/2\mathbb Z$. However, simple objects generating them are fermions, and the $\mathbb Z/2\mathbb Z$ algebras fail to be commutative. Thus, they are also completely anisotropic. For $(\widehat{\mathfrak{e_8}})_2$, its only nontrivial algebra is the $\mathbb Z/2\mathbb Z$ [@G23], but it is fermionic and fails to be commutative. Thus, the MFC is also completely anisotropic, and our results are consistent.

    Of course, the critical Ising model is described by an Ising MFC with $h_Y=1/16$. The MFC is known (see, e.g., [@FRS03]) to be completely anisotropic, and our results are consistent. (The MFC has only one nontrivial connected separable algebra $A\cong1\oplus X$, but since $X$ is a fermion $c_{X,X}\cong-id_1$, it fails to be commutative.) See also [@KL02] for classification of connected étale algebras in minimal models.

[^7]: They have double braidings $$c_{A,A}\cdot c_{A,A}\cong(2+4e^{-4\pi ih_Y})\iota\cdot id_1\cdot p+(2+e^{-4\pi ih_Y})\iota\cdot id_X\cdot p+(8+4e^{-2\pi ih_Y})\iota\cdot id_Y\cdot p,$$ and $$c_{A,A}\cdot c_{A,A}\cong(1+e^{-4\pi ih_Y})\iota\cdot id_1\cdot p+e^{-4\pi ih_Y}\iota\cdot id_X\cdot p+(2+e^{-2\pi ih_Y})\iota\cdot id_Y\cdot p,$$ respectively.

[^8]: In order to check the associativity axioms directly, one may use the method developed in [@FRS02] and associators spelled out in, say, [@BBW21]. We checked the solution in [@CZW18] is consistent.

[^9]: The condition is needed because if $d_Y=-1$, the candidate has $$d_{\mathcal B}(A)=d_{\mathcal B}(1)+d_{\mathcal B}(Y)=0,$$ a contradiction.

[^10]: The half-braidings are given by $$c_{X,X}\cong id_1,\quad c_{X,Y}\cong id_Y,\quad c_{Y,Y}\cong id_1+id_X+id_Y.$$ One of the easiest ways to get these is as follows. First, since we know $A\cong1\oplus Y$ is commutative, we learn $$c_{Y,Y}\cong id_1+id_X+id_Y.$$ Then, one can easily solve hexagon equations to get the results above. From the half-braidings, one immediately finds $$c_{A,A}\cong6\Big(\iota\cdot id_1\cdot p+\iota\cdot id_X\cdot p+2\iota\cdot id_Y\cdot p\Big)\cong id_{A\otimes A}.$$

[^11]: Actually, we can do a little more. We can show a

    **Lemma.** *An upper bound on $\text{rank}(\mathcal B_A^0)$ is eight. Namely, $\text{rank}(\mathcal B_A^0)$ cannot be nine.*

    *Proof.* Assume the opposite, and suppose $\text{rank}(\mathcal B_A^0)=9$. Then, it is either pointed or non-pointed. If it is pointed, we only have two possibilities, $\mathcal B_A^0\simeq\text{Vec}_{\mathbb Z/9\mathbb Z}^1,\text{Vec}_{\mathbb Z/3\mathbb Z\times\mathbb Z/3\mathbb Z}^1$. The MFCs with such fusion rings cannot match the additive central charges. Thus, we are left with non-pointed possibilities. A rank nine non-pointed fusion category $\mathcal C$ with $\text{FPdim}(\mathcal C)\le\text{FPdim}(\mathcal B)=\frac7{4\sin^2\frac\pi7}$ is strongly constrained. Since it is non-pointed, there exists a non-invertible object $c\in\mathcal C$ with $\text{FPdim}_{\mathcal C}(c)>1$. It enters the Frobenius-Perron dimension by squared sum, $\text{FPdim}(\mathcal C)\equiv\sum_{i=1}^9(\text{FPdim}_{\mathcal C}(c_i))^2=(\text{FPdim}_{\mathcal C}(c))^2+\cdots$. Since any object has $\text{FPdim}_{\mathcal C}(c_i)\ge1$, $\sum_{c_i\neq c}(\text{FPdim}_{\mathcal C}(c_i))^2\ge8$, and we must have $1<\text{FPdim}_{\mathcal C}(c)<2$, or the squared sum reaches ten. Here, it is known [@ENO02] that such Frobenius-Perron dimension is expressed as $\text{FPdim}_{\mathcal C}=2\cos\frac\pi n$ for a natural number $n$ larger than three ($n=3$ is ruled out by our assumption $\text{FPdim}_{\mathcal C}>1$). Since the function is monotonically increasing, the smallest Frobenius-Perron dimension is achieved when $n=4$, or $\text{FPdim}_{\mathcal C}=\sqrt2$. The Frobenius-Perron dimensions of such fusion categories exceed the upper bound $\text{FPdim}(\mathcal B)=\frac7{4\sin^2\frac\pi7}\approx9.3$, leading to a contradiction. $\square$

[^12]: We thank Victor Ostrik for teaching us an upper bound on $\text{FPdim}_{\mathcal B}(A)$ in the related work [@KK23GSD].
