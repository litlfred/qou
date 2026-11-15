---
doc_id: arxiv-math-0203206v1
doc_title: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002"
section_id: sec-016-6-concrete-braided-and-symmetric-categories
section_title: "Concrete Braided and Symmetric Categories"
section_number: 6
pages: 37-43
source_pdf: 0203206v1.pdf
source_sha256: 371611f719e6f53c
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.613
doc_brief: "arXiv:math/0203206v1 [math.QA] 20 Mar 2002 — We give a pedagogical survey of those aspects of the abstract representation theory of quantum groups which are related to the Tannaka-Krein"
---
[]{#s-braid label="s-braid"} In this section we prove that a braiding for the concrete tensor $*$-category ${\cal C}$ gives rise to an $R$-matrix for the associated aqg $(A,\Delta)$. If ${\cal C}$ is symmetric and the embedding functor $E$ is *symmetric* monoidal then we may conclude that $(A,\Delta)$ is cocommutative.

The flip automorphism $\sigma$ of $A\otimes A$ defined by $\sigma(a\otimes b)=b\otimes a$ is a non-degenerate $*$-homomorphism. Thus there exists a unique extension to an involutive $*$-automorphism of $M(A\otimes A)$ which we denote by the same symbol.

::: defin
[]{#d-quasit label="d-quasit"} An aqg $(A,\Delta)$ is said to be quasitriangular w.r.t. $R$ iff $R$ is an invertible element of $M(A\otimes A)$ and satisfies

1.  $(\Delta\otimes\iota)(R)=R_{13}R_{23}$,

2.  $(\iota\otimes\Delta)(R)=R_{13}R_{12}$,

3.  $\Delta^{op} =R\Delta(\cdot )R^{-1}$,

where $\Delta^{\mbox{\scriptsize op}}\equiv \sigma\Delta$. We sometimes refer to such an element $R$ as an $R$-matrix. If, in addition, $\sigma(R)=R^{-1}$ we call $(A,\Delta)$ triangular.
:::

The first equation means that the invertible element $R\in M(A\otimes A)$ is a non-degenerate corepresentation of $(A,\Delta)$ on $A$. It is easy to see that $(A,\Delta)$ is quasitriangular w.r.t. $R$ iff $(A, \Delta^{op})$ is quasitriangular w.r.t. $\sigma (R)$.

::: defin
[]{#d-braiding label="d-braiding"} A braiding for a (strict) tensor category ${\cal C}$ is a family of isomorphisms $c_{X,Y}: X\otimes Y\rightarrow Y\otimes X$, for all $X,Y\in{\cal C}$ natural in both arguments $$t\otimes s\,\circ\,c_{X,Y}=c_{X',Y'}\,\circ\,s\otimes t \quad \forall s: X\rightarrow X', t: Y\rightarrow Y',$$ satisfying $$\begin{aligned}
   c_{X,Y\otimes Z} &=& \mathrm{id}_Y\otimes c_{X,Z}\,\circ\,c_{X,Y}\otimes\mathrm{id}_Z, \\
   c_{X\otimes Y,Z} &=& c_{X,Z}\otimes \mathrm{id}_Y\,\circ\,\mathrm{id}_X\otimes c_{Y,Z}, \\
   c_{X,{\bf 1}} &=& c_{{\bf 1},X}=\mathrm{id}_X
\end{aligned}$$ for all $X,Y,Z\in {\cal C}$. A braiding is called a symmetry if, in addition, it satisfies $$c_{X,Y}\,\circ\,c_{Y,X}=\mathrm{id}_{Y\otimes X} \quad\forall X,Y\in{\cal C}.$$ A tensor category with a (chosen) braiding or symmetry is called a braided or symmetric tensor category, respectively. A braided functor $F: {\cal C}\rightarrow{\cal D}$ is a monoidal functor between strict braided tensor categories making $$\label{e-braidfunc}
\begin{diagram}
F(X)\otimes F(Y) & \rTo^{d^F_{X,Y}} & F(X\otimes Y) \\
\dTo^{c_{F(X),F(Y)}} & & \dTo_{F(c_{X,Y})} \\
F(Y)\otimes F(X) & \rTo_{d^F_{Y,X}} & F(Y\otimes X)
\end{diagram}$$ commutative for all $X, Y\in{\cal C}$.
:::

The following result establishes the relation between $R$-matrices for $(A,\Delta)$ and braidings for $\mathrm{Rep}_f(A,\Delta)$.

::: prop
[]{#p-braidR label="p-braidR"} Let $(A,\Delta)$ be a discrete aqg. Let $R\in M(A\otimes A)$ and consider $$c_{(H,\pi),(H',\pi')} \equiv \Sigma_{H,H'} \, (\overline{\pi\otimes\pi'})(R), \quad (H,\pi),
    (H',\pi')\in\mathrm{Rep}_f(A,\Delta).$$ Here $\Sigma_{H,K}$ is the canonical unitary flip from $H\otimes K\rightarrow K\otimes H$. Then the family $(c_{(H,\pi),(H',\pi')})$ is a braiding for $\mathrm{Rep}_f(A,\Delta)$ iff $R$ is an $R$-matrix. Also $c_{(H,\pi),(H',\pi')}$ is unitary for all $(H,\pi),(H',\pi')$ iff $R$ is unitary. If these equivalent conditions are satisfied then $(A,\Delta)$ is triangular iff the corresponding braiding for $\mathrm{Rep}_f(A,\Delta)$ is symmetric.
:::

*Proof. * Throughout the proof we write $c_{\pi, \pi'}$ for $c_{(H,\pi),(H',\pi')}$ and note that $c_{\pi, \pi'}: H\otimes H'\rightarrow H'\otimes H$, for all $(H,\pi ), (H' \pi ')\in \mathrm{Rep}_f(A,\Delta)$. Also note that $$\overline{(\pi\otimes\pi')}\ \sigma (a) 
=\Sigma_{H',H}\ \overline{(\pi'\otimes\pi )}\ (a)\ \Sigma_{H, H'} 
\quad \forall\  (H,\pi), (H',\pi')\in\mathrm{Rep}_f(A,\Delta)\quad \forall\ a\in M(A\otimes A).$$ Now suppose $R\in M(A\otimes A)$ satisfies $\Delta^{op}(\cdot )R =R\Delta(\cdot)$. Then $$\begin{aligned}
  c_{\pi, \pi'}\ (\pi\times \pi' )(a) &=& \Sigma_{H,H'} \,
   (\overline{\pi\otimes\pi'})(R)\ (\overline{\pi\otimes\pi'})\Delta(a) 
   =\Sigma_{H,H'} \, (\overline{\pi\otimes\pi'}) (R\Delta(a))
   =\Sigma_{H,H'} \, (\overline{\pi\otimes\pi'}) (\Delta^{op} (a) R)  \\
 &=& \Sigma_{H,H'} \, (\overline{\pi\otimes\pi'}) \Delta^{op} (a)\ (\overline{\pi\otimes\pi'})(R)
   =\Sigma_{H,H'} \, (\overline{\pi\otimes\pi'}) (\sigma\Delta(a))\ \Sigma_{H',H}\ \Sigma_{H,H'}\
    (\overline{\pi\otimes\pi'})(R) \\ 
 &=& (\overline{\pi '\otimes\pi})\Delta(a)\ \Sigma_{H,H'}\ (\overline{\pi\otimes\pi'})(R)
    =(\pi'\times \pi )(a)\ c_{\pi, \pi'},
\end{aligned}$$ so we have seen that $c_{\pi, \pi'} :\pi\times \pi '\rightarrow\pi'\times \pi$ for all $\pi, \pi '\in\mathrm{Rep}_f (A,\Delta)$. Conversely, by reversing the above calculations, we see that $\Delta^{op}(\cdot ) R=R\Delta(\cdot )$ if $c_{\pi, \pi'} :\pi\times \pi '\rightarrow\pi'\times \pi$ for all $\pi, \pi '\in\mathrm{Rep}_f (A,\Delta)$.

It is straightforward to see that $R$ is invertible iff $c_{\pi, \pi'}: \pi\times\pi'\rightarrow\pi'\times\pi$ is an isomorphism for all $\pi,\pi'\in\mathrm{Rep}_f(A,\Delta)$, that $R$ is unitary iff $c_{\pi, \pi'}$ is unitary for all $\pi, \pi '\in\mathrm{Rep}_f (A,\Delta)$, and that $R^{-1}=\sigma (R)$ iff $c_{\pi', \pi}\ c_{\pi, \pi '} =\mathrm{id}_{\pi, \pi'}$ for all $\pi, \pi '\in\mathrm{Rep}_f (A,\Delta)$.

Pick $\pi,\pi', \pi''\in\mathrm{Rep}_f (A,\Delta)$. Then $$\begin{aligned}
 \lefteqn{  \overline{(\pi\otimes \pi'\otimes\pi'' )}(\iota\otimes\Delta)(R)
  =\overline{(\pi\otimes (\pi'\times\pi ''))}(R) } \\
 && =\Sigma_{H'\otimes H'', H}\ \Sigma_{H, H'\otimes H''}\ \overline{(\pi\otimes (\pi'\times\pi ''))}(R)
   =\Sigma_{H'\otimes H'', H}\ c_{\pi, \pi'\times \pi'' }, 
\end{aligned}$$ whereas $$\begin{aligned}
 \lefteqn{ \overline{(\pi\otimes \pi'\otimes\pi'' )}(R_{13} R_{12})
  =(\Sigma_{H'', H}\ \Sigma_{H,H''}\ \overline{(\pi\otimes \pi'')} (R))_{13}\ 
  (\Sigma_{H', H}\ \Sigma_{H,H'}\ \overline{(\pi\otimes \pi')} (R))_{12} } \\
 && =(\Sigma_{H'', H}\ c_{\pi, \pi''} )_{13}\ (\Sigma_{H', H}\ c_{\pi, \pi'} )_{12}
  =(\Sigma_{H'', H})_{13}\ (c_{\pi, \pi''} )_{13}\ (\Sigma_{H', H})_{12}\ (c_{\pi, \pi'} )_{12} \\
 && =\Sigma_{H'\otimes H'', H}\ (c_{\pi, \pi''} )_{23}\ \ (c_{\pi, \pi'} )_{12}. 
\end{aligned}$$ Hence $(\iota\otimes\Delta)(R)=R_{13}R_{12}$ iff $$c_{\pi, \pi'\times \pi'' } =(c_{\pi, \pi''} )_{23}\ \ (c_{\pi, \pi'} )_{12}
=\mathrm{id}_{\pi '}\otimes c_{\pi,\pi ''}\,\circ\,c_{\pi, \pi '}\otimes\mathrm{id}_{\pi ''},$$ for all $\pi,\pi', \pi''\in\mathrm{Rep}_f (A,\Delta)$. Similarly, one shows that $(\Delta\otimes\iota )R=R_{13}R_{23}$ iff $$c_{\pi\times \pi', \pi'' } =(c_{\pi, \pi''} )_{12}\ \ (c_{\pi', \pi''} )_{23}
=c_{\pi,\pi ''}\otimes\mathrm{id}_{\pi'}\,\circ\,\mathrm{id}_{\pi }\otimes c_{\pi', \pi ''},$$ for all $\pi,\pi', \pi''\in\mathrm{Rep}_f (A,\Delta)$.

::: thm
[]{#t-braid1 label="t-braid1"} Let ${\cal C}$ be a semisimple braided tensor $*$-category with conjugates and $E: {\cal C}\rightarrow{\cal H}$ a faithful $*$-preserving tensor functor. Let $(A,\Delta)$ and $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ be as constructed in Theorem [\[t-main-equiv\]](#t-main-equiv){reference-type="ref" reference="t-main-equiv"}. Then $(A,\Delta)$ is quasitriangular w.r.t. a unique $R\in M(A\otimes A)$ such that the functor $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ is an equivalence of braided tensor categories w.r.t. the braiding for $\mathrm{Rep}_f(A,\Delta)$ provided by $R$. $R$ is unitary iff $c_{X,Y}$ is unitary for all $X,Y$. $(A,\Delta)$ is triangular iff the corresponding braiding for $\mathrm{Rep}_f(A,\Delta)$ is symmetric.
:::

*Proof. *For $i,j\in I_{\cal C}$ we have $$F(c_{X_i,X_j})\in\mathrm{Mor}_{\cal H}(E(X_i)\otimes E(X_j), E(X_j)\otimes E(X_i))=B(E(X_i)\otimes E(X_j),
    E(X_j)\otimes E(X_i)).$$ Thus $\Sigma_{E(X_j),E(X_i)}F(c_{X_i,X_j})\in B(E(X_i)\otimes E(X_j))$ and we can define $R\in M(A\otimes A)=\prod_{ij}B(E(X_i)\otimes E(X_j))$ by $R_{ij}=\Sigma_{E(X_j),E(X_i)}F(c_{X_i,X_j})$. Naturality of the braiding and functoriality of $F$ now imply that we have $$F(c_{X,Y})=\Sigma_{E(X),E(Y)} \, (\overline{\pi_X\otimes\pi_Y})(R) \quad \forall X,Y\in {\cal C}.$$

Since $F$ is an equivalence, we see that the family $F(c_{X,Y})$ is a braiding for $\mathrm{Rep}_f (A,\Delta)$. Denote this family by $(c_{(E(X),\pi_X),(E(Y),\pi_Y )})$, so $$c_{(E(X),\pi_X),(E(Y),\pi_Y )}=\Sigma_{E(X),E(Y)} \, (\overline{\pi_X\otimes\pi_Y})(R) \quad
    \forall X,Y\in {\cal C}.$$ By Proposition [\[p-braidR\]](#p-braidR){reference-type="ref" reference="p-braidR"}, the element $R\in M(A\otimes A)$ is therefore an $R$-matrix which is unitary iff $c_{X,Y}$ is unitary for all $X,Y$ and satisfies $\sigma (R)=R^{-1}$ iff $c_{Y,X}\,\circ\,c_{X,Y} =\mathrm{id}_{X\otimes Y}$ for all $X,Y$. With the braiding on $\mathrm{Rep}_f (A,\Delta)$ given by $R$ according to Proposition [\[p-braidR\]](#p-braidR){reference-type="ref" reference="p-braidR"}, we get by definition $F(c_{X,Y})=c_{F(X),F(Y)}$, for all $X,Y$, as $F(X)=(E(X),\pi_X )$ for all $X$. Thus $F$ is a braided functor.

::: rema
It seems worthwhile comparing our result with [@kas Proposition XIII.1.4], where it is shown that the tensor category of left modules over a bialgebra $(H,m,\eta,\Delta,\varepsilon)$ is braided iff $H$ is quasitriangular w.r.t. some $R$-matrix. The proof uses the left regular representation of $H$ and therefore would not apply to the category of finite dimensional $H$-modules if $H$ is infinite dimensional. Our setting differs too in that $A$ is non-unital whenever it is infinite dimensional.
:::

::: rema
As is well known, the category ${\cal H}$ of Hilbert spaces has a unique braiding, the flip $\Sigma_{H,K}: H\otimes K\rightarrow K\otimes H$. It is thus natural to ask when the functors $E$ respects this braiding. If so, then $$E(c_{X,Y}\,\circ\,c_{Y,X}) = E(c_{X,Y})\,\circ\,E(c_{Y,X}) = \Sigma_{E(X),E(Y)}\,\circ\,\Sigma_{E(Y),E(X)}
   =\mathrm{id}_{E(Y)\otimes E(X)}= \mathrm{id}_{E(Y\otimes X)}=E(\mathrm{id}_{Y\otimes X}),$$ where we suppressed the isomorphisms $d^E_{X,Y}$ as is our policy throughout. If $E$ is faithful this implies $c_{X,Y}\,\circ\,c_{Y,X}=\mathrm{id}_{Y\otimes X}$, thus ${\cal C}$ is symmetric. In other words, for non-symmetric categories ${\cal C}$ there is no embedding functor satisfying $E(c_{X,Y})=\Sigma_{E(X),E(Y)}$. For symmetric ${\cal C}$ we have the following easy yet important result.
:::

::: cor
[]{#c-symm label="c-symm"} Let ${\cal C}$ be a semisimple symmetric tensor $*$-category and let $E: {\cal C}\rightarrow{\cal H}$ be a symmetric embedding functor, i.e., $E(c_{X,Y})=\Sigma_{E(X),E(Y)}$ for all $X,Y\in{\cal C}$. Then the corresponding discrete aqg $(A,\Delta)$ is cocommutative and $F$ is a $*$-preserving symmetric monoidal equivalence.
:::

*Proof. *It is clear from the definition of the $R$-matrix $R$ in the proof of Theorem [\[t-braid1\]](#t-braid1){reference-type="ref" reference="t-braid1"}, that $R=1$ in this case, so $\Delta^{op}=\Delta$.

We are now in a position to re-prove the classical Tannaka-Krein duality theorem for compact groups.

::: thm
Let ${\cal C}$ be a semisimple tensor $*$-category with conjugates and unitary symmetry, and let $E: {\cal C}\rightarrow{\cal H}$ be a $*$-preserving faithful symmetric tensor functor. Then there exists a compact group $G$ and an equivalence $F': {\cal C}\rightarrow\mathrm{Rep}_fG$ of symmetric tensor $*$-categories such that $K'\circ F'=E$, where $K': \mathrm{Rep}_fG\rightarrow{\cal H}$ is the forgetful functor. The group $G$ is canonically isomorphic to the intrinsic group $G_E$ of the embedding functor.
:::

*Proof. *Under the given assumptions, Theorem [\[t-braid1\]](#t-braid1){reference-type="ref" reference="t-braid1"} provides us with a discrete aqg $(A,\Delta)$ and an equivalence $F: {\cal C}\rightarrow\mathrm{Rep}_f(A,\Delta)$ of tensor $*$-categories such that $K\circ F=E$. By assumption, $E$ preserves the symmetries, i.e. $E(c_{X,Y})=\Sigma_{E(X),E(Y)}$ for all $X,Y\in{\cal C}$. Then by Corollary [\[c-symm\]](#c-symm){reference-type="ref" reference="c-symm"} $(A,\Delta)$ is cocommutative. Let $G$ be the intrinsic group of $(A,\Delta)$ as defined in Definition [\[d-intrins\]](#d-intrins){reference-type="ref" reference="d-intrins"}. By Theorem [\[t-cocomm2\]](#t-cocomm2){reference-type="ref" reference="t-cocomm2"} we have a (concretely given) equivalence $D: \mathrm{Rep}_f(A,\Delta)\rightarrow\mathrm{Rep}_f G$ of tensor $*$-categories. Thus the composition $F'=D\circ F: {\cal C}\rightarrow\mathrm{Rep}_f G$ is the desired equivalence of tensor $*$-categories. It satisfies $K'\circ F'=K'\circ D\circ F=K\circ F=E$. The final claim is obvious, since the unitary grouplike elements of $(A,\Delta)$ are by definition of $(A,\Delta)$ precisely the unitary natural isomorphisms of $E$ that are compatible with the tensor structures, in the sense of ([\[e-nat\]](#e-nat){reference-type="ref" reference="e-nat"}).

We end this section with some general facts on $R$-matrices for quasitriangular aqg.

::: prop
Let $(A,\Delta)$ be a quasitriangular aqg w.r.t. $R$. Then the following statements hold:

1.  $R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}$.

2.  $(\varepsilon\otimes\iota )R=1=(\iota\otimes\varepsilon )R$.

3.  $(S\otimes\iota )R=R^{-1} =(\iota\otimes S^{-1} )(R)$.

4.  $(S\otimes S)R=R$.

The first equation is called the 'quantum Yang-Baxter equation'.
:::

*Proof. *$R$ is a non-degenerate corepresentation of $(A,\Delta)$ on $A$, so 2. and the first equation in 3. follow immediately. The second equation in 3. thus follows by noting that $(A, \Delta^{op})$ is quasitriangular w.r.t. $\sigma (R)$ with coinverse $S^{-1}$. Claim 4 follows from 3. by $(S\otimes S)R=(\iota\otimes S)(S\otimes\iota )R=(\iota\otimes S)(R^{-1}) 
=(\iota\otimes S)(\iota\otimes S^{-1})R =R$. Finally, to prove 1. first note that both the maps $\Delta^{op}\otimes\iota$ and $R_{12}(\Delta\otimes\iota )(\cdot )R_{12}^{-1}$ are non-degenerate homomorphisms from $A\otimes A$ to $M(A\otimes A\otimes A )$, and thus both have unique extensions to $M(A\otimes A)$. Because $\Delta^{op}=R\Delta(\cdot )R^{-1}$ these maps clearly coincide on $A\otimes A$, and thus on $M(A\otimes A)$, extensions being unique. Hence $$R_{12}R_{13}R_{23}R_{12}^{-1}=R_{12}(\Delta\otimes\iota)(R)R_{12}^{-1}=(\Delta^{op}\otimes\iota )(R)
=(\sigma\otimes\iota )(\Delta\otimes\iota)(R)=(\sigma\otimes\iota )(R_{13}R_{23})=R_{23}R_{13},$$ as desired.

::: prop
Suppose $(A,\Delta)$ is a quasitriangular aqg w.r.t. $R$. Let $U$ denote the universal corepresentation of $(A,\Delta)$ as defined in Theorem [\[t-univ-corep\]](#t-univ-corep){reference-type="ref" reference="t-univ-corep"}. Define $\pi_R :\hat{A}\rightarrow M(A)$ as in Proposition [\[p-functP\]](#p-functP){reference-type="ref" reference="p-functP"}. Then the following hold:

1.  $\pi_R$ is a non-degenerate homomorphism.

2.  $(\pi_R\otimes\pi_R )\hat{\Delta}=\Delta^{op}\pi_R$.

3.  $\Delta^{op} (\cdot)(\iota\otimes\pi_R )U =(\iota\otimes \pi_R )U\Delta(\cdot )$.

Conversely, any map $\pi: \hat{A}\rightarrow M(A)$ satisfying these three properties arises from a unique $R\in M(A\otimes A)$ with $\pi=\pi_R$ making $(A,\Delta)$ into a quasitriangular aqg. Moreover, the map $\pi_R$ is $*$-preserving iff $R$ is unitary.
:::

*Proof. * It suffices to show that statement 2 is equivalent to $(\iota\otimes\Delta)(R)=R_{13}R_{12}$, this being the only non-trivial step not covered by Proposition [\[p-functP\]](#p-functP){reference-type="ref" reference="p-functP"} and Theorem [\[t-univ-corr\]](#t-univ-corr){reference-type="ref" reference="t-univ-corr"}. But by Theorem [\[t-univ-corep\]](#t-univ-corep){reference-type="ref" reference="t-univ-corep"}, we get $$\begin{gathered}
 (\pi_R\otimes\pi_R )\hat{\Delta}\omega =(\pi_R\otimes\pi_R )\hat{\Delta}(\omega\otimes\iota )U
   =(\pi_R\otimes\pi_R )(\omega\otimes\iota\otimes\iota )(\iota\otimes \hat{\Delta})U
 =(\pi_R\otimes\pi_R )(\omega\otimes\iota\otimes\iota )(U_{12}U_{13}) \\
   =(\omega\otimes\iota\otimes\iota )(\iota\otimes\pi_R\otimes\pi_R )(U_{12}U_{13})
=(\omega\otimes\iota\otimes\iota )[((\iota\otimes\pi_R )U)_{12}((\iota\otimes\pi_R )U)_{13}]
=(\omega\otimes\iota\otimes\iota )(R_{12}R_{13}) 
\end{gathered}$$ for all $\omega\in\hat{A}$, whereas $$\Delta^{op}\pi_R (\omega )=\Delta^{op}(\omega\otimes\iota )R 
   =(\omega\otimes\iota\otimes\iota )(\iota\otimes\Delta^{op})R$$ for all $\omega\in\hat{A}$.

Note that 1. and 2. just mean that $\pi_R$ is a morphism of multiplier Hopf algebras from $(\hat{A},\hat{\Delta})$ to $(A,\Delta^{op} )$. It is even an aqg morphism iff $R$ is unitary by the last statement of the proposition.

In Definition [\[d-corepf\]](#d-corepf){reference-type="ref" reference="d-corepf"} we introduced the tensor product $V\times V' =V_{12}V'_{13}\in M(A\otimes B\otimes B')$ of two unitary corepresentations $V$ and $V'$ on $B$ and $B'$, respectively. Another choice of a tensor product which works equally well, is given by $V\times_{op} V' =V'_{13}V_{12}\in M(A\otimes B\otimes B' )$. In general there is no relation between these two tensor products. In view of the relation between representations of an aqg and corepresentations of its dual aqg (and the relation between the identity representation and the universal corepresentation), the following result should not come as a big surprise.

::: prop
Let $(A,\Delta)$ be an aqg with universal corepresentation $U$, so $hat{U}=\sigma (U)$ is the universal corepresentation of $(\hat{A},\hat{\Delta})$ on $A$. Let $R$ be any element of $M(A\otimes A)$. Then $\Delta^{op}(\cdot )R=R\Delta(\cdot )$ iff $$(\hat{U}\times_{op}\hat{U})R_{23} =R_{23}(\hat{U}\times\hat{U}).$$
:::

*Proof. * By Theorem [\[t-univ-corep\]](#t-univ-corep){reference-type="ref" reference="t-univ-corep"}, we get $$\Delta^{op}(a )R =(\Delta^{op}(\iota\otimes a)U )R =(\sigma\Delta(\iota\otimes a)U)R$$ $$=((\sigma\otimes a)(\Delta\otimes\iota )U)R 
   =((\iota\otimes\iota\otimes a )(\sigma\otimes\iota )(U_{13}U_{23}))R
   =(\iota\otimes\iota\otimes a )(U_{23}U_{13}R_{12})$$ for all $a\in A$, whereas $$R\Delta(a ) =R\Delta(\iota\otimes a)U  =R(\iota\otimes\iota\otimes a)(\Delta\otimes\iota )U 
   =R(\iota\otimes\iota\otimes a )(U_{13}U_{23})
   =(\iota\otimes\iota\otimes a )(R_{12}U_{13}U_{23})$$ for all $a\in A$. Hence $\Delta^{op}(\cdot )R=R\Delta(\cdot )$ iff $U_{23}U_{13}R_{12}=R_{12}U_{13}U_{23}$. Permuting indices, we see that the latter equation is equivalent to $U_{31}U_{21}R_{23}=R_{23}U_{21}U_{31}$, which again is equivalent to $\hat{U}_{13}\hat{U}_{12}R_{23}=R_{23}\hat{U}_{12}\hat{U}_{13}$ as desired.

So given any unitary $R$-matrix $R$, the map $f\in \mathrm{Hom}(A\otimes A,A\otimes A)$ given by $f(b)=RbR^*$, for all $b\in A\otimes A$, is an arrow from $\Delta$ to $\Delta^{op}$ and from $\hat{U}\times\hat{U}$ to $\hat{U}\times_{op}\hat{U}$ in the sense of Remark [\[r-cat\]](#r-cat){reference-type="ref" reference="r-cat"}. Also $\delta_R (a)=f(1\otimes a)$ for $a\in A$, is a coaction in the sense of Remark [\[r-actcoact\]](#r-actcoact){reference-type="ref" reference="r-actcoact"}. Similarly, the linear map $\delta_R ' :A\rightarrow M(A\otimes A)$ given by $\delta_R ' (a)=f(a\otimes 1)$, for all $a\in A$, is a non-degenerate $*$-homomorphism such that $(\delta_R '\otimes\iota )\delta_R ' =(\iota\otimes\Delta^{op} )\delta_R '$ and $(\iota\otimes\varepsilon )\delta_R ' =\iota$.
