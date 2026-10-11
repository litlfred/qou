---
doc_id: arxiv-1803.04009v2
doc_title: "Prepared for submission to JHEP IPMU-18-0045"
section_id: sec-002-3-symmetry-enhancement
section_title: "Symmetry enhancement"
section_number: 3
pages: 27-41
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.989
---
[]{#sec:symm label="sec:symm"}

Using the proposed 6d interpretation of $T^{DGG}[N,X_A]$ in [\[Relation-T6d-TDGG\]](#Relation-T6d-TDGG){reference-type="eqref" reference="Relation-T6d-TDGG"}, we will determine the symmetry enhancement pattern of the $U(1)_{X_A}$ symmetry associated to the knot based on a topological type of the boundary cycle $A$. See the Table [1](#Sym enhancement in DGG){reference-type="ref" reference="Sym enhancement in DGG"} for the summary whose details will be explained in Sec. [0.1](#sec:en){reference-type="ref" reference="sec:en"}.

::: {#Sym enhancement in DGG}
   $A \in H_1 \big{(}\partial N,\mathbb{Z}\big{)}$   Symmetry enhancement of $U(1)_{X_A}$ in $T^{ DGG}[N,X_A]$
  ------------------------------------------------- -----------------------------------------------------------
                      closable                                     $U(1)_{X_A} \rightarrow U(1)$
             non-closable, $SO(3)$ type                           $U(1)_{X_A} \rightarrow SO(3)$
             non-closable, $SU(2)$ type                           $U(1)_{X_A} \rightarrow SU(2)$

  : Symmetry enhancement in $T^{DGG}[N,X_A]$. The definitions of "$SU(2)/SO(3)$ types" are explained in Sec. [\[sec:DGG\]](#sec:DGG){reference-type="ref" reference="sec:DGG"}. The definitions of "closable/non-closable" are explained in Sec. [0.1](#sec:en){reference-type="ref" reference="sec:en"}.
:::

In Sec. [0.2](#sec:SU(3)){reference-type="ref" reference="sec:SU(3)"}, we will find infinitely many examples of pair $(N,A)$ and $(N',A')$ whose corresponding DGG theories are identical and both of $A$ and $A'$ are non-closable but one of them (say $A$) is $SO(3)$ type while the other ($A'$) is $SU(2)$ type. In that case, combining the table [1](#Sym enhancement in DGG){reference-type="ref" reference="Sym enhancement in DGG"} with a group theoretical argument, we can argue[^1] that the DGG theory has enhanced $SU(3)$ symmetry. Using the argument, we prove that $T^{DGG}[M=S^3, K]$ theories for all hyperbolic twist knots $K$ have $SU(3)$-symmetry. We checked the enhancement for several twist knots which gives non-trivial empirical evidence for the Table [1](#Sym enhancement in DGG){reference-type="ref" reference="Sym enhancement in DGG"}.

## $SO(3)/SU(2)$ enhancement {#sec:en}

From the relation between $T_{\rm irred}^{6d}$ and $T^{DGG}$ in [\[Relation-T6d-TDGG\]](#Relation-T6d-TDGG){reference-type="eqref" reference="Relation-T6d-TDGG"}, we understand the symmetry breaking mechanism of $su(2)_A$ to $U(1)_{X_A}$. For the symmetry breaking to happen, we need the $su(2)$ moment map operator $\mu$ in $T^{6d}_{\rm irred}$ theory. Otherwise, the $su(2)_A$ is not broken by the mechanism and the resulting $T^{DGG}$ is expected to have an $su(2)$ symmetry. Therefore, we need to know when $\mu$ is absent.

This question can be answered by an inspection of the 5d picture discussed in Sec. [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}. In the description there, the moment map operator comes from the holomorphic $su(2)_C$ moment map of $T[SU(2)]$ theory which is put along a knot $K$. After $S^1$ compactification, the $T[SU(2)]$ has 2d ${\cal N}=(4,4)$ supersymmetry. In the Language of ${\cal N}=(2,2)$ supersymmetry, there is a twisted chiral operator $\widetilde{\mu}$ and a chiral operator $\mu$, [^2] both of which are associated to the Coulomb branch $su(2)_C$ symmetry of $T[SU(2)]$.

Now suppose that the Higgs branch operator $\widetilde{\nu}$ gets a nonzero expectation value. Then, the nonzero VEV in Higgs branch makes the Coulomb branch fields massive. Therefore, in the low energy limit, the operators $\mu$ and $\widetilde{\mu}$ become empty;

$$\begin{aligned}
\textrm{In $T[SU(2)]$ theory on $\langle \tilde{\nu} \rangle \neq 0$, $\mu$ is absent at low-energy}
\end{aligned}$$

In the coupled system (5d SYM+ $T[SU(2)]$), as shown in [\[HolA and nu\]](#HolA and nu){reference-type="eqref" reference="HolA and nu"}, the VEV of the moment operator $\widetilde{\nu}$ is given by $\log  \rho_{\rm hol} (A)$ of complexified gauge field $\mathcal{A}$. The $\mathcal{A}$ is a flat connection in $\chi_0[N]$ defined in [\[Dehn-surgery com\]](#Dehn-surgery com){reference-type="eqref" reference="Dehn-surgery com"} and [\[Dehn-surgery com-2\]](#Dehn-surgery com-2){reference-type="eqref" reference="Dehn-surgery com-2"}. Thus the above relation implies that the $T^{6d}_{\rm irred}$ theory on $\mathbb{R}^2\times S^1$ does not contain $\mu$ if there is no $PSL(2,\mathbb{C})$ flat-connection in $\chi_0[N]$ with trivial $\rho_{\rm hol}({\cal A})$. Let us define

$$\begin{aligned}
\begin{split}
&\textrm{A primitive boundary cycle $A\in H_1 (\partial N, \mathbb{Z})$ is `closable'}
\\
&\textrm{if there is a point in $\chi_0[N]$ with $ \rho_{\rm hol}(A)= 1$\;.} \label{Def : closable cycle}
\end{split}
\end{aligned}$$

We remark that in the massless case $m=0$, the eigenvalues of $\rho_{\rm hol}(A)$ are trivial ($\pm 1$), but $\rho_{\rm hol}(A)$ may contain off-diagonal components and hence the above condition is nontrivial. Then,

$$\begin{aligned}
\begin{split}
&\textrm{$A \in H_1 (\partial N, \mathbb{Z})$ is non-closable } 
\\
& \Rightarrow \; \textrm{$\mu$ is absent in $T^{6d}_{\rm irred} [N,A]$ on $\mathbb{R}^2 \times S^1$ for any radius of $S^1$ at low energy} 
\\
& \Rightarrow \; \textrm{$\mu$ is absent in $T^{6d}_{\rm irred} [N,A]$ on $\mathbb{R}^3$ at low energy } 
\\
&\Rightarrow \; T^{DGG}[N,X_A]= T^{6d}_{\rm irred}[N,A] \textrm{ has $su(2)$ symmetry at low energy}\;.
\end{split}
\end{aligned}$$

Strictly speaking, the step from ${\mathbb R}^2 \times S^1$ to ${\mathbb R}^3$ is nontrivial, but we assume that this step holds.

One necessary condition for $A$ to be 'non-closable' is that the Dehn filled manifold $N_A$ is non-hyperbolic.

$$\begin{aligned}
\textrm{If $N_A$ is hyperbolic} \; \Rightarrow \; \textrm{$A$ is closable}\;.
\end{aligned}$$

This is because that the flat connection corresponding to the hyperbolic structure on $N_A$ is always contained in $\chi_0[N]$ with trivial $\rho_{\rm hol}(A)$. According to Thurston's hyperbolic Dehn surgery theorem, for given hyperbolic $N$, there are only finite number of primitive boundary cycles $A$ which give non-hyperbolic $N_A$. So, we can conclude that

$$\begin{aligned}
|\{\textrm{Set of  primitive `non-closable' boundary cycles $A \in H_1 (\partial N ,\mathbb{Z})$} \}| < \infty\;.
\end{aligned}$$

Combining with Table [1](#Sym enhancement in DGG){reference-type="ref" reference="Sym enhancement in DGG"}, it implies that the $u(1)_{X_A}$ symmetry of $T^{DGG}[N,X_A]$ is not enhanced to $su(2)$ except for only finite many $A$s. The Thurston's theorem is consistent with our field theoretical consideration in the previous section that the moment map operator $\mu$ generically (although not always) exists; see the discussion in the paragraph containing [\[eq:STk\]](#eq:STk){reference-type="eqref" reference="eq:STk"}.

One sufficient condition for $A$ to be 'non-closable' is that the Dehn filled manifold $N_A$ is Lens-space

$$\begin{aligned}
\textrm{If $N_A$ is Lens space} \; \Rightarrow \; \textrm{$A$ is non-closable}\;. \label{non-closable : Lens}
\end{aligned}$$

Lens space $L(p,q)$ is defined as

$$\begin{aligned}
L(p,q) := \big{(}S^3\backslash (\textrm{unknot}) \big{)}_{p\mu+ q\lambda}
\end{aligned}$$

The reason is as follows. If $A$ is closable, by definition, there should be an irreducible flat connection in $\chi_0[N]$ with trivial $\rho_{\rm hol}(A)$. Such a flat connection can be thought as an irreducible flat connection on $N_A$. But if $N_A$ is a Lens space, there can not be any irreducible flat connection because the fundamental group $\pi_1$ of Lens space is abelian. Thus the cycle $A$ can not be closable. When $N_A$ is neither hyperbolic nor a Lens space, no simple criterion to determine the closability has been found.

An alternative definition of closable/non-closable cycle, which seems to be equivalent to the above definition, is using 3d index which is introduced in [@Dimofte:2011py] as a topological invariant of 3-manifolds with torus boundaries and is generalized in Appendix [\[sec : 3d index\]](#sec : 3d index){reference-type="ref" reference="sec : 3d index"} to cover closed 3-manifolds.

$$\begin{aligned}
\begin{split}
&\textrm{A primitive boundary cycle $A\in H_1 (\partial N, \mathbb{Z})$ is closable (non-closable)}
\\
&\textrm{if $\mathcal{I}_{N_A}(x) \neq 0$\;($\mathcal{I}_{N_A}(x) = 0$)\;.} 
\end{split}
\end{aligned}$$

Here $\mathcal{I}_{N_A}(x)$ is the 3d index on a closed 3-manifold $N_A$. That a primitive boundary cycle $A \in H_1 (\partial N, \mathbb{Z})$ is 'non-closable' means that we can not 'close' (or eliminate) the co-dimension two defect along a $K$ on $M$ in a supersymmetric way after sitting on the vacuum $P_{\rm SCFT}$. As we will study in the next section, there is an operation in SCFT side of 3d/3d correspondence which corresponds to the operation of 'closing the knot'. If $A$ is non-closable cycle, we expect that the resulting 3d theory $T^{6d}_{\rm irred}[M]$ after taking the closing knot operation on $T^{6d}_{\rm irred}[M,K]$ will be a theory with supersymmetry broken.[^3] The index $\mathcal{I}_{M=N_A}(x)$ computes the superconformal index of the theory $T^{6d}_{\rm irred}[M]$ and expected to be zero when $A$ is non-closable and thus supersymmetry is broken. This is a heuristic argument supporting the equivalence between the two definitions and no rigorous mathematical proof is known. We checked the equivalence for various examples and the equivalence seems to hold possibly except for exotic cases. As an example, see Table [2](#Boundary cycles of 4-1){reference-type="ref" reference="Boundary cycles of 4-1"} for the case when $N=S^3\backslash \mathbf{4_1}=m004$.

::: {#Boundary cycles of 4-1}
   $A \in H_1 (\partial N, \mathbb{Z})$              [Closability]{.roman}                 $\mathcal{I}_{N_{A}}(x)$
  -------------------------------------- --------------------------------------------- ---------------------------------
    $p\mu + \lambda \; ( |p| \geq 5)$     closable ($\Leftarrow$ $N_A$ is hyperbolic)   non-trivial power series in $x$
      $p\mu + \lambda \; ( |p| = 4)$                       closable                                divergent
      $p\mu + \lambda \; ( |p|< 4)$                        closable                                    1
                  $\mu$                                  non-closable                                  0

  : Closability of boundary cycles of $N=S^3\backslash \mathbf{4_1}$. The $\mu$ is meridian and $\lambda$ is longitude. We determine the closability using the definition in [\[Def : closable cycle\]](#Def : closable cycle){reference-type="eqref" reference="Def : closable cycle"} and the $\mathcal{D}[N,\mathcal{T}]$ in [\[deformation variety-m004\]](#deformation variety-m004){reference-type="eqref" reference="deformation variety-m004"} with [\[Hol-m004-1\]](#Hol-m004-1){reference-type="eqref" reference="Hol-m004-1"} and [\[Hol-m004-2\]](#Hol-m004-2){reference-type="eqref" reference="Hol-m004-2"}
:::

We can further determine the global structure of enhanced symmetry, whether $SO(3)$ or $SU(2)$, from the $SO(3)/SU(2)$ type of $A$. When $A$ is non-closable and of $SU(2)$ type, the compact $U(1)_{X_A}$ symmetry of $T^{DGG}[N,X_A]$ is embedded into the enhanced $su(2)_A$ symmetry via $\mathbf{2}_{su(2)_A}\rightarrow (\pm 1)_{U(1)_{X_A}}$. This is manifest from the relations given in eq. [\[Hol(A) in terms of edges\]](#Hol(A) in terms of edges){reference-type="eqref" reference="Hol(A) in terms of edges"} and [\[(XA,PB)\]](#(XA,PB)){reference-type="eqref" reference="(XA,PB)"} between the variable $X_A$, associated to the $U(1)_{X_A}$, and the $PSL(2,\mathbb{C})$ holonomy variables $a$, associated to the $su(2)_A$. Namely, $\mathbf{2}_{su(2)}$ has properly quantized $U(1)_{X_A}$ charges and the theory can have operators charged under half integer spin representations of $su(2)_A$ which means that the symmetry is $SU(2)$. Similarly we can see that only operators in integer spin representation are allowed when $A$ is of $SO(3)$ type. See also Appendix [\[app:susotypes\]](#app:susotypes){reference-type="ref" reference="app:susotypes"} for more justifications from different arguments.

In general, it is not easy to determine the $SO(3)/SU(2)$ type of a given primitive boundary cycle $A$ in $H_{1}(\partial N, \mathbb{Z})$. When $N$ is a knot complement in a homological sphere, there is a canonical choice of the basis of $H_{1}(\partial N, \mathbb{Z})$, meridian $(\mu)$ and longitude ($\lambda$). Meridian cycle is defined to be the circle around the knot and longitude cycle is determined by the condition that $\lambda \in \textrm{Ker}\big{(}i_* : H_1 (\partial N, \mathbb{Z}) \rightarrow H_1 (N, \mathbb{Z})\big{)}$. Then, $\lambda$ is of $SU(2)$-type by definition while $\mu$ is always of $SO(3)$-type. More generally, when $N$ is a knot complement in a $\mathbb{Z}_2$-homological sphere ($p$ and $q$ are coprime)

$$\begin{aligned}
p\mu+q \lambda \textrm{ is of }
 \begin{cases}
 \textrm{$SU(2)$-type}\;,\; \textrm{for even $p$ }\;,
 \\
\textrm{$SO(3)$-type}\;,\;\textrm{for odd $p$}\;. \label{SO(3)/SU(3) type in Z2-homology sphere}
\end{cases} 
\end{aligned}$$

Here $\mu\in H_1 (\partial N, \mathbb{Z})$ is the meridian cycle and $\lambda$ is a boundary cycle in $\textrm{Ker}\big{(}i_* : H_1 (\partial N, \mathbb{Z}) \rightarrow H_1 (N, \mathbb{Z}_2)\big{)}$. The choice of $\lambda$ is not unique but can be shifted by $2\mu$.

#### Example : $N=S^3\backslash \mathbf{4_1}= m004$ and $A =\mu$

In the case, the merdian cycle $\mu$ is non-closable and of $SO(3)$-type and we expect $SO(3)$ symmetry enhancement of $u(1)_{X_{\mu}}$ in $T^{DGG}[m004, X_{\mu}]$ whose Lagrangian is give in eq. [\[TDGG\[m004\]\]](#TDGG[m004]){reference-type="eqref" reference="TDGG[m004]"}. In the next section, we argue that $u(1)_{X_\mu}$ is actually enhanced to $SU(3)$ which contain the $SO(3)$ as a subgroup.

#### Example : $N= \overline{(S^3\backslash \mathbf{5^2_1})_{3\mu_1 - 2 \lambda_1}}= m007$ and $A =\mu_2$

As another example, we consider a knot complement called $m007$ in SnapPy's census. The knot complement can be obtained by performing Dehn filling on one component of Whitehead link complement.

<figure id="fig:Whitehead">
<div class="center">
<embed src="whitehead.pdf" />
</div>
<figcaption> Whitehead link (<span class="math inline"><strong>5</strong><sub>1</sub><sup>2</sup></span>). It is one of the simplest (having smallest volume <span class="math inline"> ≃ 3.664</span>) two-component hyperbolic link.</figcaption>
</figure>

Whitehead link is denoted by $\mathbf{5}^2_1$, the 1st link with 2 components and 5 crossings, as shown in Fig. [1](#fig:Whitehead){reference-type="ref" reference="fig:Whitehead"}. The orientation of the link complement ($S^3\backslash \mathbf{5}^2_1$) is chosen as the one induced from an ideal triangulation in [\[Gluing eqns for Whitehead\]](#Gluing eqns for Whitehead){reference-type="eqref" reference="Gluing eqns for Whitehead"}. We always choose a particular orientation of each ideal tetrahedron in an ideal triangulation which is reflected in the choice of CS level sign of $T_{\Delta}$ in [\[DGG : step 1\]](#DGG : step 1){reference-type="eqref" reference="DGG : step 1"}. Then, the Dehn filled manifolds have natural orientation induced from the link complement. The overline in the equation $N= \overline{(S^3\backslash \mathbf{5^2_1})_{3\mu_1 - 2 \lambda_1}}$ means that $N=m007$ has opposite orientation to the one induced from $S^3\backslash \mathbf{5}^2_1$ when the orientation of $N$ is chosen to be the one induced from an ideal triangulation in [\[triangulation of m007\]](#triangulation of m007){reference-type="eqref" reference="triangulation of m007"}. The Dehn filling also gives an induced basis of $H_1 (\partial N, \mathbb{Z})= \langle \mu_2, \lambda_2 \rangle$ on $N$ from the basis choice of $H_1 (\partial (S^3\backslash \mathbf{5^2_1}),\mathbb{Z}) = \langle \mu_1, \mu_2 , \lambda_1, \lambda_2 \rangle$. From the topological fact that

$$\begin{aligned}
N_A = (S^3 \backslash \mathbf{5^2_1})_{3\mu_1- 2 \lambda_1, \mu_2} =  (S^3\backslash ({\rm unknot}))_{3\mu- 2 \lambda}= L(3,-2)\;,
\end{aligned}$$

we see that $A$ is non-closable according to [\[non-closable : Lens\]](#non-closable : Lens){reference-type="eqref" reference="non-closable : Lens"}. The $N$ is a knot complement in a $\mathbb{Z}_2$-homological sphere, $N_A = L(3,-2)$, and according to [\[SO(3)/SU(3) type in Z2-homology sphere\]](#SO(3)/SU(3) type in Z2-homology sphere){reference-type="eqref" reference="SO(3)/SU(3) type in Z2-homology sphere"} $A$ is of $SO(3)$ type. So from Table [1](#Sym enhancement in DGG){reference-type="ref" reference="Sym enhancement in DGG"}, we expect the $u(1)_{X_{\mu_2}}$ in $T^{DGG}[m007, X_{\mu_2}]$ is enhanced to $SO(3)$. Now, let us check the enhancement from explicit construction of the DGG theory. According to SnapPy, the knot complement can be triangulated by 3 ideal tetrahedra and the corresponding gluing data are (we choose $B=4\mu_2-\lambda_2$)

$$\begin{aligned}
\begin{split}
&C_1 = Z_1 +2Z_2+Z_3\;, \quad C_2 = Z_1+Z_1''+Z_2'+Z_3+Z_3''\;,
\\
&C_3 = 2Z_1'+Z_1''+Z_2'+2Z_2''+2Z_3'+Z_3''\;,
\\
& a_{\mu_2 } = -Z_1 -Z_1''-Z_2+Z_3''+i\pi\;,
\\
&b_{4\mu_2 -\lambda_2} = 2 (- i \pi +Z_1+Z_2) \label{triangulation of m007}
\end{split}
\end{aligned}$$

Since $(A,B)$ are of $(SO(3),SU(2))$-type, we choose

$$\begin{aligned}
X_{\mu_2} =  a_{\mu_2 }\;, \quad P_{4\mu_2  - \lambda_2} = \frac{1}2 b_{4\mu_2 - \lambda_2}\;.
\end{aligned}$$

Then, the symplectic matrix in [\[g_N\]](#g_N){reference-type="eqref" reference="g_N"} for this example is

$$\begin{aligned}
\begin{split}
& g_{m007} = \left(
\begin{array}{cccccc}
 -1 & -1 & 0 & -1 & 0 & 1 \\
 1 & 2 & 1 & 0 & 0 & 0 \\
 1 & -1 & 1 & 1 & -1 & 1 \\
 1 & 1 & 0 & 0 & 0 & 0 \\
 0 & 0 & 0 & 0 & 0 & 1 \\
 0 & 1 & 0 & 0 & 0 & 0 \\
\end{array}
\right)\;.
\end{split} 
\end{aligned}$$

The matrix can be decomposed into $g_{m007} = g^s_{J_{m007}} g^t_{K_{m007}} g^{gl}_{U_{m007}}$ with [\[T,S and GL type\]](#T,S and GL type){reference-type="eqref" reference="T,S and GL type"}

$$\begin{aligned}
U_{m007} = \left(
\begin{array}{ccc}
 1 & 1 & 0 \\
 0 & 2 & 1 \\
 0 & 1 & 0 
\end{array}
\right)\;, \quad K_{m007} = \left(
\begin{array}{ccc}
 1 & 0 & 0 \\
 0 & 0 & 0 \\
 0 & -1 & 3
\end{array}
\right)\;, \quad J_{m007} = \left(
\begin{array}{ccc}
 1 & 0 & 0 \\
 0 & 0 & 0 \\
 0 & 0 & 1
\end{array}
\right)\;.
\end{aligned}$$

Following each steps in eq. [\[DGG : step 1\]](#DGG : step 1){reference-type="eqref" reference="DGG : step 1"},[\[DGG : step 2\]](#DGG : step 2){reference-type="eqref" reference="DGG : step 2"} and [\[DGG : final\]](#DGG : final){reference-type="eqref" reference="DGG : final"}, the Lagrangian for $T^{DGG}[m007,X_{\mu_2};P_{4\mu_2 -\lambda_2}]$ is given by

$$\begin{aligned}
\begin{split}
&\mathcal{L}_{T^{DGG}[m007,X_{\mu_2};P_{4\mu_2 -\lambda_2}]}
\\
&=  \int d^4\theta \left( \frac{1}{4\pi } \big{(}\frac{3}2 \Sigma_2  V_2+  2V_{X}\Sigma_1  +2V_{C} \Sigma_2\big{)} + \big{(} \Phi_{1}^\dagger e^{V_1-V_2} \Phi_1+\Phi_{2}^\dagger e^{V_2} \Phi_2+\Phi_{3}^\dagger e^{-V_1-V_{2}} \Phi_3 \big{)} \right)
\\
& \quad + \frac{1}2 \int d^2 \theta  \Phi_1 \Phi_2^2 \Phi_3 +(c.c) \;.
\end{split}
\end{aligned}$$

In the Lagrangian, $V_1$ and $V_2$ are dynamical $u(1)$ vector multiplets. The superpotential term comes from an easy internal edge $C_1$, $O_{C_1} = \Phi_1 \Phi_2^2 \Phi_3$. The theory has $u(1)_{X_\mu}$ and $u(1)_C$ whose background vector multiplets are $V_X$ and $V_C$ respectively. Applying the mirror symmetry in eq. [\[3d mirror-1\]](#3d mirror-1){reference-type="eqref" reference="3d mirror-1"} and [\[3d mirror-2\]](#3d mirror-2){reference-type="eqref" reference="3d mirror-2"} with the following replacement

$$\begin{aligned}
\Phi_A \rightarrow \Phi_1, \Phi_B \rightarrow \Phi_3, W \rightarrow V_X+ V_2, U \rightarrow -2 V_2\;.
\end{aligned}$$

we have

$$\begin{aligned}
\begin{split}
&\mathcal{L}_{T^{DGG}[m007,X_{\mu_2};P_{4\mu_2 -\lambda_2}]}
\\
&=  \frac{1}{4\pi }\int d^4\theta \big{(}\frac{3}2 \Sigma_2  V_2 +2V_{C} \Sigma_2 +\Phi_{2}^\dagger e^{V_2} \Phi_2+ (T_p)^\dagger e^{V_X+ V_2} T_p +(T_m)^\dagger e^{-V_X+V_2} T_p +M^\dagger e^{-2V_2} M \big{)}
\\
& \quad + \bigg{(} \int d^2 \theta M ( \frac{1}2\Phi_2^2 + T_m T_p)  +(c.c) \bigg{)}\;.
\end{split}
\end{aligned}$$

In the dual picture, the $SO(3)$ symmetry is manifest after the redefinition of chiral fields as $$\begin{aligned}
\begin{split}
&\phi_1 := \Phi_2, \phi_2 := \frac{1}{\sqrt{2}} (T_m +T_p),\phi_3 := \frac{i}{\sqrt{2}} (T_m -T_p)\;,
\\
&\Rightarrow M(\frac{1}2\Phi_2^2+ T_m T_p )=\frac{1}2 M( \phi_1^2 +\phi_2^2 +\phi_3^2 )\;.
\end{split}
\end{aligned}$$

The $u(1)_X$ is in the Cartan of this $SO(3)$.

## $SU(3)$ enhancement {#sec:SU(3)}

From the point of view of 6d ${\cal N}=(2,0)$ theories, we only expect that the symmetry associated to codimension-2 defects (which are knots in 3-manifolds) are $su(2)$. However, we will see that there are many theories which have larger symmetry enhancement.

We consider a pair of $(N,A;B)$ and $(N',A';B')$ such that

$$\begin{aligned}
\begin{split}
&1) \;\textrm{$A$ is of $SO(3)$ type  while $A'$ is of $SU(2)$ type}\;,
\\
&2) \;\mathcal{I}_{N}^{(A,B)} (m,e;x)= \mathcal{I}_{N'}^{(A',B')} (m,e;x)\;,
\\
&3)\; \textrm{Both of $A$ and $A'$ are  non-closable cycles\;.} \label{Def: SU(3) pair}
\end{split}
\end{aligned}$$

which we call $SU(3)$-enhancement pair. The $\mathcal{I}_{N}^{(A,B)}$ in 2) denotes a topological invariant called 3d index, see Appendix [\[sec : 3d index\]](#sec : 3d index){reference-type="ref" reference="sec : 3d index"}. For such a pair, we claim that

$$\begin{aligned}
\begin{split}
&\textrm{I. Two theories $T^{DGG}[N,X_A]$ and $T^{DGG}[N',X_{A'}]$ are identical}
\\
&\quad \;\textrm{possibly modulo a topological sector}
\\
&\textrm{II. The theory has enhanced $SU(3)$ flavor symmetry where $SO(3)_{A}$  and $SU(2)_{A'}$ are}
\\
&\quad \;\textrm{embedded into the $SU(3)$ in a way that $\mathbf{3}_{SU(3)}\rightarrow \mathbf{3}_{SO(3)_{A}}$ and $\mathbf{3}_{SU(3)}\rightarrow (\mathbf{2}\oplus \mathbf{1})_{SU(2)_{A'}}$}\;. \label{claim : SU(3) enhancement}
\end{split}
\end{aligned}$$

The 3d index ${\cal I}_{N}^{(A,B)}(x)$ is equivalent to the superconformal index of $T^{DGG}[N,X_A]$ in charge basis. For hyperbolic complement $N$, the index is a non-trivial power series in $x$. The non-trivial match of the superconformal indices in the 2nd condition strongly suggests that two theories are actually equivalent possibly up to a topological sector.

From 1st and 3rd conditions in [\[Def: SU(3) pair\]](#Def: SU(3) pair){reference-type="eqref" reference="Def: SU(3) pair"}, the theory $T^{DGG}[N,X_A]=T^{DGG}[N',X_{A'}]$ has both of $SU(2)_A$ and $SO(3)_{A'}$ symmetry where the $U(1)_{X_A}=U(1)_{X_A'}$ is embedded into them as $\mathbf{2}_{SU(2)} = (\pm 1)_{U(1)}$ and $\mathbf{3}_{SO(3)} =(\pm 1, 0)_{U(1)}$ respectively. The only consistency way of this happening is that the theory has a $SU(3)$ symmetry into which the $SU(2)_A$ and $SO(3)_{A'}$ are embedded as II in [\[claim : SU(3) enhancement\]](#claim : SU(3) enhancement){reference-type="eqref" reference="claim : SU(3) enhancement"}. The reason is that the $SU(2)_A$ enhancement requires that there are conserved currents with charge $\pm 2$ under $U(1)_{X_A}$ from off-diagonal components of $SU(2)_A$, while the $SO(3)_{A'}$ enhancement requires that there are conserved currents with charge $\pm 1$ under $U(1)_{X_A'}$. Then the conserved currents with charge $\pm 1$ from $SO(3)_{A'}$ is a doublet of $SU(2)_A$. A minimal completion of such a situation to a Lie algebra is to embed the symmetries to the $SU(3)$ algebra.

One may wonder if there exits such a pair. Surprisingly, we can find infinitely many examples of these pairs. A class of examples is

$$\begin{aligned}
\begin{split}
&N= (S^3 \backslash \mathbf{5}^2_1)_{\mu_1+ k \lambda_1}\;, \quad  A = \mu_2\;, \quad B= 2\mu_2 +\lambda_2
\\
&N'= \overline{(S^3\backslash \mathbf{5}^2_1)_{(4k+1)\mu_1 - k \lambda_1}}\;, \quad  A' = 2\mu_2 - \lambda_2\;, \quad B'= \mu_2 - \lambda_2 \;. \label{SU(3) pair : twist knot}
\end{split}
\end{aligned}$$

<figure id="fig:1/k-surgery-Whitehead">
<div class="center">
<embed src="surgery-on-whitehead.pdf" />
</div>
<figcaption>A rational surgery calculus <span class="citation" data-cites="rolfsen1984rational"></span> shows that <span class="math inline">(<em>S</em><sup>3</sup>∖<strong>5</strong><sub><strong>1</strong></sub><sup><strong>2</strong></sup>)<sub><em>μ</em><sub>2</sub> + <em>k</em><em>λ</em><sub>2</sub></sub></span> is a twist knot <span class="math inline"><em>K</em><sub><em>k</em></sub></span>. For example, <span class="math inline"><em>K</em><sub><em>k</em> = 1</sub> = <strong>4</strong><sub><strong>1</strong></sub>, <em>K</em><sub><em>k</em> =  − 2</sub> = <strong>5</strong><sub><strong>2</strong></sub></span> and <span class="math inline"><em>K</em><sub><em>k</em> = 2</sub> = <strong>6</strong><sub>1</sub></span>. </figcaption>
</figure>

As shown in fig. [2](#fig:1/k-surgery-Whitehead){reference-type="ref" reference="fig:1/k-surgery-Whitehead"}, the $N$ above are nothing but twist knots which will be denoted as $K_k$. Let us check that the pair satisfy the 3 conditions in [\[Def: SU(3) pair\]](#Def: SU(3) pair){reference-type="eqref" reference="Def: SU(3) pair"}. First, note that both of $N$ and $N'$ can be considered as a knot complement in $\mathbb{Z}_2$-homological spheres, $L(1,k)=(N)_{\mu_2}$ and $L(4k-1,-k)=(N')_{\mu_2}$ respectively. Applying [\[SO(3)/SU(3) type in Z2-homology sphere\]](#SO(3)/SU(3) type in Z2-homology sphere){reference-type="eqref" reference="SO(3)/SU(3) type in Z2-homology sphere"} with $\mu=\mu_2$ and $\lambda= \lambda_2$, we can conclude that $A/A'$ is of $SO(3)/SU(2)$ type. Now let us check the 2nd condition in [\[Def: SU(3) pair\]](#Def: SU(3) pair){reference-type="eqref" reference="Def: SU(3) pair"}. Combining the $\mathbb{D}_8$-symmetry [\[D_8 of Whitehead\]](#D_8 of Whitehead){reference-type="eqref" reference="D_8 of Whitehead"} of the Whitehead link index $\mathcal{I}_{\mathbf{5}^2_1}$ [\[Whitehead index\]](#Whitehead index){reference-type="eqref" reference="Whitehead index"} and the following polarization transformation rules of 3d index

$$\begin{aligned}
\begin{split}
&\mathcal{I}_{S^3\backslash \mathbf{5}^2_1}^{(- \lambda_1, \mu_2;\mu_1,2\mu_2+ \lambda_2)} (m_1 , m_2, e_1, e_2;x) =\mathcal{I}_{\mathbf{5^2_1}} (e_1, m_2, -m_1, e_2-m_2;x)
\\
&\mathcal{I}_{S^3\backslash \mathbf{5}^2_1}^{(4\mu_1 - \lambda_1, 2 \mu_2 - \lambda_2 ;\mu_1, \lambda_2-\mu_2)}  (m_1, m_2, e_1, e_2)=\mathcal{I}_{\mathbf{5^2_1}} (e_1,2 m_2+e_2, 2e_1-m_1, m_2+e_2;x)
\\
\end{split}
\end{aligned}$$ and the following matrix multiplication ($S_2$ is a generator of the $\mathbb{D}_8$ in [\[D_8 of Whitehead\]](#D_8 of Whitehead){reference-type="eqref" reference="D_8 of Whitehead"})

$$\begin{aligned}
\begin{split}
&\left(\begin{array}{c}e_1 \\ 2m_2 +e_2\\ 2e_1-m_1 \\ m_2+e_2\end{array}\right)_{(e_1,e_2)\rightarrow (-e_1,-e_2)}= S_2  \cdot \left(\begin{array}{c}e_1 \\ m_2 \\ -m_1 \\ e_2-m_2 \end{array}\right)\;
\end{split}
\end{aligned}$$

we have following identity

$$\begin{aligned}
\mathcal{I}_{S^3\backslash \mathbf{5}^2_1}^{(- \lambda_1, \mu_2;\mu_1,2\mu_2+ \lambda_2)} (m_1 , m_2, e_1, e_2;x) =  \mathcal{I}_{S^3\backslash \mathbf{5}^2_1}^{(4\mu_1 - \lambda_1, 2 \mu_2 - \lambda_2 ;\mu_1, \lambda_2-\mu_2)} (m_1 , m_2, -e_1, -e_2;x)\;.
\end{aligned}$$

Applying the Dehn filling formula in eq. [\[3d index-2\]](#3d index-2){reference-type="eqref" reference="3d index-2"} to the above equality,

$$\begin{aligned}
\begin{split}
&\mathcal{I}_{(S^3\backslash \mathbf{5}^2_1)_{\mu_1 + k \lambda_1}}^{( \mu_2;2\mu_2+ \lambda_2)} ( m_2,  e_2;x) =  \mathcal{I}_{(S^3\backslash \mathbf{5}^2_1)_{(4k+1)\mu_1 - k \lambda_1}}^{( 2 \mu_2 - \lambda_2 ;\lambda_2-\mu_2)} ( m_2, -e_2;x)\;, 
\\
&\Rightarrow  \mathcal{I}_{(S^3\backslash \mathbf{5}^2_1)_{\mu_1 + k \lambda_1}}^{( \mu_2;2\mu_2+ \lambda_2)} ( m_2,  e_2;x) =  \mathcal{I}_{\overline{(S^3\backslash \mathbf{5}^2_1)_{(4k+1)\mu_1 - k \lambda_1}}}^{( 2 \mu_2 - \lambda_2 ;\mu_2-\lambda_2)} ( m_2, e_2;x)\;, \quad \textrm{for all $k\in \mathbb{Z}$}\;.
\end{split}
\end{aligned}$$

we confirm 2) in [\[Def: SU(3) pair\]](#Def: SU(3) pair){reference-type="eqref" reference="Def: SU(3) pair"}. In the above, we use the transformation rule of 3d index under the orientation reversal in [\[Index under orientation reversal\]](#Index under orientation reversal){reference-type="eqref" reference="Index under orientation reversal"}. Finally, from the following topological facts [@martelli2002dehn]

$$\begin{aligned}
\begin{split}
&N_A = (S^3\backslash \mathbf{5}^2_1)_{\mu_1+k \lambda_1, \mu_2}= L(1,k)\;, 
\\
&  (N')_{A'}=(S^3\backslash \mathbf{5}^2_1)_{(4k+1)\mu_1- k \lambda_1,2\mu_2- \lambda_2} = L(-8k-2,-2k-1)\;,
\end{split}
\end{aligned}$$

we see that both of $A$ and $A'$ are non-closable cycles according to [\[non-closable : Lens\]](#non-closable : Lens){reference-type="eqref" reference="non-closable : Lens"}. So we confirm that the pair, $(N,A)$ and $(N',A')$, in [\[SU(3) pair : twist knot\]](#SU(3) pair : twist knot){reference-type="eqref" reference="SU(3) pair : twist knot"} satisfy all the conditions in [\[Def: SU(3) pair\]](#Def: SU(3) pair){reference-type="eqref" reference="Def: SU(3) pair"} and the corresponding DGG theory is expected to have $SU(3)$ flavor symmetry. We will check the ehancement explicitly for $k=1,-2$ by explicitly constructing $T^{DGG}[N,A]$ and $T^{DGG}[N',A']$.

#### For $k=1$

In the case,

$$\begin{aligned}
\begin{split}
&(S^3\backslash \mathbf{5}^2_1)_{\mu_1 + \lambda_1} = (S^3\backslash \mathbf{4}_1) = m004\;,
\\
&\overline{(S^3\backslash \mathbf{5}^2_1)_{5\mu_1 -  \lambda_1}} = (\textrm{Sister of }S^3\backslash \mathbf{4}_1) = m003\;. \label{m003/m004 from whitehead}
\end{split}
\end{aligned}$$

$m003$ is a knot complement called sister of figure-eight knot complement. Both 3-manifolds have the same hyperbolic volume and are the smallest hyperbolic 3-manifolds with one cusp torus boundary. From ideal triangulations of $m003$ and $m004$ given below, their orientation are fixed. The equality in the above means not only that the two manifolds are homeomorphism but also that they have the same orientation, i.e. the orientation of $m004$ is same as the orientation induced from a Dehn filling on $S^3\backslash \mathbf{5^2_1}$, whose orientation is induced from an ideal triangulation in [\[Gluing eqns for Whitehead\]](#Gluing eqns for Whitehead){reference-type="eqref" reference="Gluing eqns for Whitehead"}.

According to SnapPy, both can be ideally triangulated by two tetrahedra and have common internal edge variables given in [\[internal edges of 4_1\]](#internal edges of 4_1){reference-type="eqref" reference="internal edges of 4_1"} while boundary variables are different by a factor $2$ or $1/2$

$$\begin{aligned}
\begin{split}
& a_{\mu_2} = Z_1-Z_2\;, \quad  b_{\lambda_2+2 \mu_2} = 4Z_1-2Z_1'-2Z_2\;,  \quad \textrm{ for $m004$}\;. 
\\
& a_{2\mu_2-\lambda_2}= 2 Z_1-2 Z_2\;, \quad b_{\mu_2 -\lambda_2} = 2Z_1-Z_1'-Z_2\;,   \quad \textrm{ for $m003$}\;. 
\end{split}
\end{aligned}$$

For DGG's construction, we choose

$$\begin{aligned}
\begin{split}
& X_{\mu_2}= a_{\mu_2}\;, \quad P_{2\mu_2+\lambda_2}=\frac{1}2 b_{2\mu_2+\lambda_2} \;,   \quad \textrm{ for $m004$}\;. 
\\
& X_{2\mu_2-\lambda_2}= \frac{1}2 a_{2\mu_2-\lambda_2}\;, \quad P_{\mu_2}= b_{\mu_2-\lambda_2} \;,   \quad \textrm{ for $m003$}\;. 
\end{split}
\end{aligned}$$

Thus, both DGG theories are identical and described by the Lagrangian in [\[TDGG\[m004\]\]](#TDGG[m004]){reference-type="eqref" reference="TDGG[m004]"} up to background CS level for $U(1)_{X}$ which is irrelevant in symmetry enhancement. We reproduce the Lagrangian here with the modified background CS level;

$$\begin{aligned}
\begin{split}
&\mathcal{L}_{T^{DGG}[m004, X_{\mu_2} ;P_{2 \mu_2 +\lambda_2}]} (V_{X}, V_C)  = \mathcal{L}_{T^{DGG}[m003, X_{2\mu_2-\lambda_2} ;P_{\mu_2-\lambda_2}]} (V_{X}, V_C) 
\\
&=\frac{1}{4\pi} \int d^4 \theta \left(- \frac{1}2 \Sigma_C V_X + \Sigma (2V_C + 3 V_X) + \Sigma_X V_X \right) + \int d^4 \theta \left( \Phi_1^\dagger e^{V+\frac{V_X}2}\Phi_1 +\Phi_2^\dagger e^{V- \frac{V_X}2}\Phi_2 \right) \;.\label{TDGG[m004]reproduced}
\end{split}
\end{aligned}$$

So the theory is

$$\begin{aligned}
\begin{split}
&T^{DGG}[m004,\mu_2] = T^{DGG}[m003,2\mu_2- \lambda_2] 
\\
&=\textrm{A $U(1)$  vector multiplet coupled to 2 chirals of charge $+1$} \;.
\end{split}
\end{aligned}$$

The theory has manifest $u(1)_{\rm top} \times su(2)_{\rm manifest}$ where $u(1)_{\rm top}$ is the topological monopole charge of the $u(1)_{\rm gauge}$ gauge symmetry, and $su(2)_{\rm manifest}$ acts on the two chiral fields. This $u(1)_{\rm top} \times su(2)_{\rm manifest}$ will be enhanced to $SU(3)$.

The $u(1)_{C}$ flavor symmetry associated to the background field $V_C$ corresponds to the topological symmetry $u(1)_{\rm top}$ and will be embedded to $SU(3)$ as

$$\begin{aligned}
u(1)_C = u(1)_{\rm top}= T_8 := \textrm{diag}(-1/3, -1/3, 2/3) \in SU(3)\;.
\end{aligned}$$

This is because the "off-diagonal components" of $SU(3)$ (which are not in $u(1)_{C}\times su(2)_{\rm manifest}$) are provided by monopole operators with monopole charge $\pm 1 = \pm (1/3 - (-2/3))$.

On the other hand, the $V_X$ is coupled to the system as follows. Let

$$\begin{aligned}
T_3:=\textrm{diag}(1/2,-1/2,0)\;.
\end{aligned}$$

be the Cartan generator of the manifest $su(2)_{\rm manifest}$. The $V_X$ is coupled to the chiral fields via this generator $T_3$. Also, notice that $V_X$ is coupled to the monopole current $\Sigma$ with coefficients $3/2$. Therefore the $u(1)_{X}$ is embedded in $SU(3)$ as

$$\begin{aligned}
u(1)_X =  \frac{3}2 T_8+T_3 = \textrm{diag} (0,-1,1) \in SU(3)\;.
\end{aligned}$$

This $u(1)_X$ must be enhanced to $su(2)_X$ because the $A$-cycle is non-closable.

Notice that this $su(2)_X$ is different from the manifest $su(2)_{\rm manifest}$ symmetry. Therefore, if $u(1)_X$ is enhanced to $su(2)_X$, then the $u(1)_{\rm top}\times su(2)_{\rm manifest}$ must be enhanced to $SU(3)$. This agrees with our general discussion that this theory has enhanced $SU(3)$ symmetry.

The superconformal index of theory is

$$\begin{aligned}
\begin{split}
&\mathcal{I}_{m003/m004}(u_1,u_2;x) 
\\
&=\sum_{(e_1,e_2)\in \mathbb{Z}^2} (-x^{\frac{1}2})^{e_2}  \mathcal{I}_{\Delta }(-e_2,-e_1+2e_2;x)\mathcal{I}_{\Delta}(-e_2,e_1-e_2;x)  u_1^{e_1}u_2^{e_2}\;.
\end{split}
\end{aligned}$$

Here $u_1$ and $u_2$ fugacity variable for $u(1)_{X}$ and $u(1)_{C}$ symmetry respectively. The index depends on the choice of $R$-charge mixing between $u(1)_R$ and $u(1)_C$. In the above expression, we in particularly choose[^4],

$$\begin{aligned}
R(\Phi_a) =\frac{1}3,\quad   R(V_\pm) = \frac{2}3\;.
\end{aligned}$$

Here $V_\pm$ denote a BPS monopole operator of charge $\pm 1$. Then the index show the $SU(3)$ structure :

$$\begin{aligned}
\begin{split}
&\mathcal{I}_{m003/m004}(u_1, u_2;x)  =1- (\chi_{1,1}) x-(\chi_{0,0}+\chi_{1,1}) x^2+(\chi_{2,2}-\chi_{0,0}-\chi_{1,1})x^3
\\
&\qquad \quad +(\chi_{3,0}+\chi_{2,2}+\chi_{0,3}-\chi_{0,0} )x^4+(\chi_{0,3}+2\chi_{1,1}+2 \chi_{2,2}+\chi_{3,0}) x^5+\ldots
\end{split}
\end{aligned}$$

Here $\chi_{m,n}(u_1, u_2)$ is the character of $SU(3)$-representation with Dynkin labels $(m,n)$. The correct IR R-charge mixing should be determined by F-maximization, but the non-trivial appearance of the $SU(3)$ in a particular choice strongly suggests that the choice gives the correct R-charge assignment. The first non-trivial terms comes form operators listed in the Table below.

[]{#leading operators in T[m003/m004] label="leading operators in T[m003/m004]"}

::: {#leading operators in T[m003/m004]}
                           $u(1)_C$             $u(1)_X$                             SCI contribution
  ----------------------- ---------- ------------------------------- ------------------------------------------------
   $\phi_a (\psi^*_+)_b$      0       $\pm \frac{1}2 \pm \frac{1}2$            $-(2+u_1 + \frac{1}{u_1}) x$
      $V_-  (\phi_a)$        $1$                $(1, 2)$                       $- (u_1 u_2  + u_1^2 u_2) x$
      $V_+ (\phi_a )$        $-1$               $(-1,-2)$             $- (\frac{1}{u_1^2 u_2} + \frac{1}{u_1 u_2})x$
:::

[]{#leading operators in T[m003/m004] label="leading operators in T[m003/m004]"}

In the table, $\phi_a$ and $(\psi_{\pm})_a$ denote the scalar and fermionic fields in chiral field $\Phi_{a}$ respectively with $a=1,2$. $V_\pm (\ldots)$ denote a gauge invariant BPS monopole operator of charge $\pm 1$ dressed by matter fields $(\ldots)$. All these operators have quantum numbers $(R,j_3,\Delta)= (1, \frac{1}2, \frac{3}2)$ and form descents of conserved current multiplet for $SU(3)$ flavor symmetry. In 3d $\mathcal{N}=2$ SCFT, a conserved current multiplet of flavor group $F$ consists of following operators in the adjoint representation of $F$:

$$\begin{aligned}
^{(0)}_{\Delta=1} \xrightarrow[\text{}]{\; Q,\tilde{Q}\; } [\frac{1}2]^{(1)}_{\Delta = \frac{3}2} \oplus [\frac{1}2]^{(-1)}_{\Delta = \frac{3}2} \xrightarrow[\text{}]{\; Q,\tilde{Q}\; }  [1]^{(0)}_{\Delta=2} \oplus [0]^{(0)}_{\Delta=2}
 
\end{aligned}$$

Here operators are denoted by its quantum number $[j]^{(r)}_{\Delta}$ where $j$ denote a spin of space-time rotational symmetry $su(2)$ in a normalization such that $[1/2]$ corresponds to the fundamental representation.

#### For $k=-2$

In the case,

$$\begin{aligned}
\begin{split}
&(S^3\backslash \mathbf{5}^2_1)_{\mu_1 - 2 \lambda_1}  = \overline{S^3 \backslash \mathbf{5}_2}= \overline{m015};,
\\
&\overline{(S^3\backslash \mathbf{5}^2_1)_{-7\mu_1 +2 \lambda_1}} = \overline{m017}\;. \label{m015/m017 from whitehead}
\end{split}
\end{aligned}$$

Both manifolds have the same hyperbolic volume $\textrm{vol}(m015)=\textrm{vol}(m017) = 2.82812\ldots$. According to SnapPy, both can be ideally triangulated by three tetrahedra and have common internal edge variables

$$\begin{aligned}
\begin{split}
&C_1 = Z_1'+Z_1''+2Z_2+Z_3'+Z_3''\;, \quad C_2 =Z_1+Z_1'+Z_2'+Z_3+Z_3'\;, 
\\
&C_3 = Z_1+Z_1''+Z_2'+2 Z''_2+Z_3+Z_3''\;.
\end{split}
\end{aligned}$$

while boundary variables are different by a factor $2$ or $1/2$

$$\begin{aligned}
\begin{split}
& a_{\mu_2}= -Z_1 +Z_2\;, \quad b_{-2 \mu_2-\lambda_2} = 2(2Z_1-Z_1''-2Z_2+Z_3'')\;,   \quad \textrm{ for $m015$}\;. 
\\
& a_{2\mu_2-\lambda_2}= -2Z_1 +2Z_2\;, \quad b_{ \lambda_2 - \mu_2} =2Z_1-Z_1''-2Z_2+Z_3''\;,   \quad \textrm{ for $m017$}\;. 
\end{split}
\end{aligned}$$

We choose

$$\begin{aligned}
\begin{split}
& X_{\mu_2}= a_{\mu_2}\;, \quad P_{-2\mu_2-\lambda_2}=\frac{1}2 b_{-2\mu_2-\lambda_2} \;,   \quad \textrm{ for $m015$}\;. 
\\
& X_{2\mu_2-\lambda_2}= \frac{1}2 a_{2\mu_2-\lambda_2}\;, \quad P_{\mu_2}= b_{\lambda_2-\mu_2} \;,   \quad \textrm{ for $m017$}\;. 
\end{split}
\end{aligned}$$

Then, the $Sp(6,\mathbb{Z})$+(affine-shifts) are

$$\begin{aligned}
\begin{split}
&\left(\begin{array}{c} X \\ C_1 \\ C_2 \\ P \\ \Gamma_1 \\ \Gamma_2\end{array}\right) = g_{m0015/m017} \cdot  \left(\begin{array}{c} Z_1 \\ Z_2 \\ Z_3 \\  Z_1'' \\ Z_2'' \\ Z_3''\end{array}\right) +  i \pi \nu_{m015/m017}
\\
&g_{m015/m017}= \left(
\begin{array}{cccccc}
 -1 & 1 & 0 & 0 & 0 & 0 \\
 -1 & 2 & -1 & 0 & 0 & 0 \\
 0 & -1 & 0 & -1 & -1 & -1 \\
 2 & -2 & 0 & -1 & 0 & 1 \\
 0 & 0 & 0 & 0 & 0 & -1 \\
 0 & 1 & 0 & 0 & 0 & 0 \\
\end{array}
\right)\;, \quad \nu_{m015/m017}= \left(\begin{array}{c} 0 \\ -2 \\ -3 \\  0 \\ 0 \\ 0\end{array}\right) 
\end{split}
\end{aligned}$$

The matrix $g_{m015/m017}$ can be decomposed into $g_{m015/m017} = g^s_{J_{m015}} g^t_{K_{m015}} g^{gl}_{U_{m015}}$ [\[T,S and GL type\]](#T,S and GL type){reference-type="eqref" reference="T,S and GL type"}

$$\begin{aligned}
&U_{m015}  = \left(
\begin{array}{ccc}
 -1 & 1 & 0   \\
 -1 & 2 & -1   \\
 0 & 1 & 0   \\
\end{array}
\right)\;, \quad 
K_{m015}  = \left(
\begin{array}{ccc}
 -2 & 0 & 0   \\
 0 & 0 & 0   \\
 0 & 0 & 1   \\
\end{array}
\right)\;, \quad 
J_{m015} = \left(
\begin{array}{ccc}
 0 & 0 & 0   \\
 0 & 0 & 0   \\
 0 & 0 & 1   \\
\end{array}
\right)\;.
\end{aligned}$$

Using the decomposition, we have

$$\begin{aligned}
\begin{split}
&\mathcal{L}_{T^{DGG}[m015, X_{\mu_2};P_{-2\mu_2- \lambda_2}]} (V_X, V_{C_1}, V_{C_2}) = \mathcal{L}_{T^{DGG}[m017, X_{2\mu_2- \lambda_2};P_{\lambda_2 - \mu_2}]} (V_X, V_{C_1}, V_{C_2})
\\
&=  \frac{1}{4\pi }\int d^4\theta \big{(}- 3\Sigma_{X} V_{X} + \Sigma_{X} V_{C_1} -\frac{1}2 (\Sigma_{C_1}- \Sigma)(V_{C_1}-V) +2  \Sigma V_{C_2} \big{)}
\\
& \quad +\int d^4\theta \big{(}\Phi_{1}^\dagger e^{V-V_{X}} \Phi_1+\Phi_{2}^\dagger e^{V} \Phi_2+\Phi_{3}^\dagger e^{V+V_{X}-V_{C_1}} \Phi_3 \big{)}\;. \label{TDGG[m015]}
\end{split}
\end{aligned}$$

Here $V$ is a dynamical $u(1)$ vector multiplet. Since $C_1$ and $C_2$ are hard internal edges and we can not add $O_{C_1}$ and $O_{C_2}$ to superpotential. So, the DGG theory is

$$\begin{aligned}
\begin{split}
&T^{DGG}[m015,\mu_2] = T^{DGG}[m017,2\mu_2- \lambda_2] 
\\
&=\textrm{A $u(1)_{-1/2}$  vector multiplet coupled to 3 chirals of charge $+1$} \;.
\end{split}
\end{aligned}$$

The theory has manifest $SU(3)$ flavor symmetry rotating 3 chrials as expected.

# Dehn filling in 3d/3d correspondence {#sec : Dehn-filling}

In this section, we generalize the DGG's construction to obtain $T^{6d}_{\rm irred}[M]$ for closed 3-manifolds $M$ by incorporating Dehn filling operation. Refer to [@Pei:2015jsa; @Gadde:2013sca; @Gukov:2017kmk; @Alday:2017yxk] for previous discussions on Dehn filling operation in the context of 3d/3d correspondence and the construction of 3d theory, which we will denote $T^{6d}_{(\rm  irred)^c}[M]$, labelled by Seifert manifolds $M$.[^5]

## Dehn filling on $T^{6d}_{\rm irred}[N]$

For a hyperbolic knot complement $N$ and a primitive boundary cycle $(pA+qB) \in H_1 (\partial N, \mathbb{Z})$,

$$\begin{aligned}
T^{6d}_{\rm irred}[N_{pA+qB}] = (\textrm{Giving a nilpotent vev to  $\mu$ of  $T^{6d}_{\rm irred}[N,pA+qB]$})\;.
\end{aligned}$$

The fact that the closing of codimension-2 defects (i.e., knots) corresponds to giving the nilpotent vev to $\mu$ is standard in 4d class S theories. See e.g., [@Tachikawa:2013kta] and references therein. This is also in accord with our terminology 'closable/non-closable', because non-closable cycles have empty $\mu$ and hence it is not possible to do the above operation while preserving supersymmetry. See Table [4](#table:closing){reference-type="ref" reference="table:closing"} below.

::: {#table:closing}
   $pA+qB \in H_1 \big{(}\partial N,\mathbb{Z}\big{)}$             $T^{6d}_{\rm irred}[N_{pA+qB}]$
  ----------------------------------------------------- ------------------------------------------------------
        non-exceptional ($\Rightarrow$ closable)                           non-trivial SCFT
                exceptional and closable                 Gapped theory (possibly with decoupled free chirals)
                      non-closable                                           SUSY broken

  : Basic property of $T^{6d}_{\rm irred}[N_{pA+qB}]$. A primitive boundary cycle $pA+qB$ is called exceptional if $N_{pA+qB}$ is non-hyperbolic.
:::

If the $A$ is non-closable and $q=1$, the above relation can be simplified as follows. The theory $T^{6d}_{\rm irred}[N, pA+B]$ is related to the theory $T^{6d}_{\rm irred}[N,A;B]$ by the transformation $ST^p \in SL(2,{\mathbb Z})$ as \^6d\_irred\[N, pA+B\] = T\^6d\_irred\[N,A;B\] - su(2)\_p - T\[SU(2)\], where $su(2)_p$ is gauging the $su(2)$ symmetry of $T^{6d}_{\rm irred}[N,A;B]$ and the $su(2)_H$ symmetry of $T[SU(2)]$. The Chern-Simons level of this group is $p+[\text{original value}]$, where $[\text{original value}]$ means the contribution of $T^{6d}_{\rm irred}[N,A;B]$ to the Chern-Simons level. To specify this contribution, we have to specify not only the $A$-cycle, but also the $B$-cycle. This is the reason why we are writing $B$ explicitly in the notation $T^{6d}_{\rm irred}[N,A;B]$.

Now, the operator $\mu$ comes from the moment map operator of $T[SU(2)]$ associated to the $su(2)_C$ symmetry which is not gauged. If we give a nilpotent vev to this operator $\mu$, the $T[SU(2)]$ becomes massive and flows to an empty theory in the low energy limit up to the Goldstone multiplets associated to the symmetry breaking of $su(2)_C$ by the vev [@Gaiotto:2008ak]. Neglecting those Goldstone multiplets, the $T[SU(2)]$ disappears and hence we get

$$\begin{aligned}
\begin{split}
T^{6d}_{\rm irred}[N_{pA+B}] &= (\textrm{Gauging $su(2)$ of $T^{6d}_{\rm irred}[N,A;B]$ with additional CS level $p$})\;, 
\\
&= (\textrm{Gauging $su(2)$ of $T^{DGG}[N,A;B]$ with additional CS level $p$})\;.
\label{integral Dehn filling = gauging}
\end{split}
\end{aligned}$$

where we have assumed that $A$ is non-closable and hence $T^{6d}_{\rm irred}[N,A;B] = T^{DGG}[N,A;B]$.

As examples, we consider closed 3-manifolds obtained from $m003/m004/m015$ by performing a Dehn filling. Combing [\[TDGG\[m004\]reproduced\]](#TDGG[m004]reproduced){reference-type="eqref" reference="TDGG[m004]reproduced"},[\[TDGG\[m015\]\]](#TDGG[m015]){reference-type="eqref" reference="TDGG[m015]"} and [\[integral Dehn filling = gauging\]](#integral Dehn filling = gauging){reference-type="eqref" reference="integral Dehn filling = gauging"}, we have[^6]

$$\begin{aligned}
\begin{split}
&T^{6d}_{\rm irred}[(m003)_{ p(2\mu_2-\lambda_2)+(\mu_2-\lambda_2)} = \overline{(S^3\backslash \mathbf{5}^2_1)_{5\mu_1 -  \lambda_1,~ p(2\mu_2-\lambda)+(\mu_2-\lambda_2)}} ]
\\
& = \frac{\textrm{A $u(1)_0$ vector coupled to 2 chrials of charge +1}  }{SU(2)_{p+1/2}}\;,
\\
&T^{6d}_{\rm irred}[(m004)_{ p \mu_2 + (\lambda_2+2 \mu_2)} =(S^3\backslash \mathbf{4}_1)_{(p+2) \mu + \lambda} ]
\\
& = \frac{\textrm{A $u(1)_0$ vector coupled to 2 chrials of charge +1}  }{SO(3)_{p+2}}\;,
\\
&T^{6d}_{\rm irred}[(m015)_{ p \mu_2 + (-2\mu_2- \lambda_2)} =(S^3\backslash \mathbf{5}_2)_{(p-2)\mu + \lambda}]
\\
& = \frac{\textrm{A $u(1)_{-1/2}$ vector coupled to 3 chrials of charge +1}  }{SO(3)_{p-6}}\;.
 \label{Theory for m003/m004 Dehn-filled}
\end{split}
\end{aligned}$$

Here the notation $/G_k$ means that we couple a vector multiplet of group $G$ with the Chern-Simons level $k$. The theories in the numerator has $SU(3)$ symmetry at IR as argued in sec. [0.2](#sec:SU(3)){reference-type="ref" reference="sec:SU(3)"} and we are gauging its $SO(3)/SU(2)$ subgroup. Since the $u(1)_X$ is embedded to the $SU(2)$ (resp. $SO(3)$) in a way that $\mathbf{2}_{su(2)} = (\pm 1)_{u(1)_X}$ (resp. $\mathbf{2}_{su(2)} = (\pm \frac{1}2)_{u(1)_X}$), the CS level $+1$ for $u(1)_X$ in [\[TDGG\[m004\]reproduced\]](#TDGG[m004]reproduced){reference-type="eqref" reference="TDGG[m004]reproduced"} corresponds to CS level $1/2$ (resp. 2) for the $su(2)$. Similarly the CS level $-3$ for $u(1)_X$ in [\[TDGG\[m015\]\]](#TDGG[m015]){reference-type="eqref" reference="TDGG[m015]"} corresponds to CS level $-6$ for the $su(2)$. A parity operation filps the signs of CS levels of the $T^{6d}_{\rm irred}$ theories. The parity operation corresponds to orientation reversal on the internal 3-manifold. It is compatible with following topological facts

$$\begin{aligned}
\begin{split}
 &(m003)_{p(2\mu_2-\lambda_2)+(\mu_2-\lambda_2)}  =\overline{(m003)_{(-p-1)(2\mu_2-\lambda_2)+(\mu_2-\lambda_2)}}\;,
 \\
 &
 (m004)_{ p \mu_2 + (\lambda_2+2 \mu_2)}  =\overline{ (m004)_{ (-p-4) \mu_2 + (\lambda_2+2 \mu_2)} }\;.
 \end{split}
\end{aligned}$$

After gauging $SU(2)/SO(3)$ subgroup of $SU(3)$, the resulting theory generically has following flavor symmetry

$$\begin{aligned}
\begin{split}
&T^{6d}_{\rm irred}[(S^3\backslash \mathbf{5}^2_1)_{5\mu_1 -  \lambda_1,~ p(2\mu_2-\lambda)+(\mu_2-\lambda_2)}] \; \textrm{has $u(1)$ flavor symmetry }
\\
&T^{6d}_{\rm irred}[(S^3\backslash \mathbf{4}_1)_{(p+2)\mu_2 +\lambda_2}] \; \textrm{has no flavor symmetry }
\\
&T^{6d}_{\rm irred}[(S^3\backslash \mathbf{5}_2)_{(p-2)\mu + \lambda}]  \; \textrm{has $u(1)$ flavor symmetry }
\end{split}
\end{aligned}$$

The $u(1)$ for the 3rd case comes from the topological symmetry of $u(1)_{-1/2}$ gauge symmetry of the theory in the numerator. The above is correct when $|p|$ is large enough where the semiclassical analysis is reliable. When $|p|$ is small, the theories could have accidental symmetries. Actually from following topological fact (see Figure. [\[fig:rational-surgery-moves\]](#fig:rational-surgery-moves){reference-type="ref" reference="fig:rational-surgery-moves"}),

$$\begin{aligned}
(S^3\backslash \mathbf{4}_1)_{ -5 \mu +\lambda } = (S^3\backslash \mathbf{5}_2)_{5\mu +\lambda}
\end{aligned}$$

we can conclude that $T^{6d}_{\rm irred}[(S^3\backslash \mathbf{4}_1)_{(p+2)\mu_2 +\lambda_2}]$ has accidental $u(1)$ symmetry for $p=3$ and $p=-7$. We will come back to this point in sec [\[sec: Duality/Surgery\]](#sec: Duality/Surgery){reference-type="ref" reference="sec: Duality/Surgery"}.

[^1]: We thank Y. Tachikawa for this argument.

[^2]: Let $\phi$ be the neutral scalar chiral field and let $\Sigma$ be twisted chiral field which comes from $u(1)$ vector multiplets in 2d. Then the Cartan components of $\widetilde{\mu}$ and $\mu$ are given by $\Sigma$ and $\phi$. However, in the discussion of Sec. [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}, we have to exchange the role of chiral and twisted chiral by regarding $\phi$ as twisted chiral and $\Sigma$ as chiral, because of the subtle mirror symmetry in the relation between 5d SYM and $T^{6d}$ in [\[eq:comm\]](#eq:comm){reference-type="eqref" reference="eq:comm"}.

[^3]: Here notice the difference between $T^{6d}_{\rm irred}[M,K]$ and $T^{6d}[M,K]$. The $T^{6d}[M]$ theory after removing knot still have a supersymmetric vacuum because there is always trivial flat connection on any closed 3-manifold $M$. The trivial flat connection on $M$ disappears in the moduli space ${\cal M}_{\rm vacua}(T^{6d}_{\rm irred}[M,K] \textrm{ on }\mathbb{R}^2\times S^1)$ after put on the vacua $P_{SCFT}$.

[^4]: In general, R-charge of BPS monopole operators $V_+, V_-$ of charge $\pm 1$ are related to the R-charges of chiral multiplets $\Phi_a$ as $R(V_\pm ) = \frac{1}2\sum q_a  (1-R(\Phi_a))$ where $q_a$ is the $u(1)_{\rm gauge}$ charge of $\Phi_a$.

[^5]: Their theory $T^{6d}_{(\rm  irred)^c}[M]$ is different from our $T^{6d}_{\rm irred}[M]$ theory. For example, when $M$ is a Lens space, their $T^{6d}_{(\rm  irred)^c}[M]$ is a non-trivial SCFT while supersymmetry is broken in our $T^{6d}_{\rm  irred}[M]$ theory. As discussed in section  [\[sec:6d\]](#sec:6d){reference-type="ref" reference="sec:6d"}, we need to specify a point $P \in {\cal M}_{\rm vacua}(T^{6d}[M] \textrm{ on } \mathbb{R}^3)$ to obtain a 3d effective theory. Their theory may correspond to different choice of $P$ other than $P_{\rm SCFT}$ in [\[Relation-T6d-TDGG:intro\]](#Relation-T6d-TDGG:intro){reference-type="eqref" reference="Relation-T6d-TDGG:intro"}.

[^6]: Taking account of orientation reversal in [\[m015/m017 from whitehead\]](#m015/m017 from whitehead){reference-type="eqref" reference="m015/m017 from whitehead"}, the boundary 1-cycle basis $(\mu_2, \lambda_2)$ of the $S^3\backslash \mathbf{5}_2$ induced from the basis of $S^3\backslash \mathbf{5}^2_1$ can be identified with $(\mu, -\lambda)$=(meridian, -(longitude)) of the knot complement. For $S^3 \backslash \mathbf{4}_1$ case, on the other hand, the $(\mu_2, \lambda_2)$ can be identified with $(\mu, \lambda)$ without sign change. Note that there is no orientation reversal in [\[m003/m004 from whitehead\]](#m003/m004 from whitehead){reference-type="eqref" reference="m003/m004 from whitehead"}.
