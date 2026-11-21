---
doc_id: arxiv-1803.04009v2
doc_title: "Symmetry enhancement and closing of knots in 3d/3d correspondence"
section_id: sec-010-42-small-hyperbolic-manifolds
section_title: "Small hyperbolic manifolds"
section_number: 4.2
pages: 41-43
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
[]{#sec : small-manifolds label="sec : small-manifolds"}

Let us discuss the case of closed 3-manifolds $M=$Weeks, a oriented hyperbolic closed 3-manifold with smallest hyperbolic volume. This was already discussed in [@Gang:2017lsr] and here we supply a little bit more details. The Weeks manifold is obtained by performing a Dehn filling operation on $m003$, = (m003)\_-5_2 +2_2 = [Weeks]{.roman}. Corresponding 3d gauge theory is the theory in the second line of eq. [\[Theory for m003/m004 Dehn-filled\]](#Theory for m003/m004 Dehn-filled){reference-type="eqref" reference="Theory for m003/m004 Dehn-filled"} with $p=-3$.

The theory in the numerator has $SU(2)_X$ symmetry which is a subgroup of the $SU(3)$. The $SU(2)_X$ symmetry is different from the manifest $SU(2)_{\rm manifest}$ rotating two chirals. But using the Weyl symmetry of the $SU(3)$, the symmetry $SU(2)_X$ and $SU(2)_{\rm manifest}$ can be exchanged with each other. Therefore, we can take $SU(2)_X$ to be the manifest $SU(2)_{\rm manifest}$. We will just denote it as $SU(2)$ in the following.

Then by [\[Theory for m003/m004 Dehn-filled\]](#Theory for m003/m004 Dehn-filled){reference-type="eqref" reference="Theory for m003/m004 Dehn-filled"},

\^6d\_irred\[\] =.

#### AF duality

Now, we can further simplify this theory to a much simpler theory [@Gang:2017lsr]. There is a duality found by Aharony and Fleischer (AF) [@Aharony:2014uya] =. To apply this duality, we need to know the relation between the flavor $U(1)$ symmetries of both sides of this equation and their background Chern-Simons levels.

Here we supply the details promised in [@Gang:2017lsr]. In the AF duality, the $U(1)$ charge acting on two chiral fields with charge 1 on the left hand side corresponds to the topological charge of the $U(1)_{+3/2}$ gauge field multiplied by 2. The reason is that the $-1 \in U(1)$ acting on the two chiral fields can be compensated by the $-1 \in SU(2)_{-5/2}$ gauge transformation, and hence all gauge invariant operators have even charge on the left hand side. So the relation is &SU(2)\_-5/2\--U(1)\^bkg\_0\
 & - U(1)\_3/2 U(1)\^bkg\_n . []{#eq:AF label="eq:AF"} where $U(1)^{\rm bkg}$ is the global symmetry with background field, $n$ is the background Chern-Simons level, and $\times 2$ means that the $U(1)^{\rm bkg}_n$ is coupled to the topological current of $U(1)_{3/2}$ multiplied by two.

We want to determine the value of $n$. This can be done as follows. Let $\sigma^{\rm bkg}$ be the real scalar for the background $U(1)^{\rm bkg}$ vector multiplet, or in other words, the real mass associated to this symmetry. We choose the sign of it such that after integrating out the two chiral fields on the left hand side, the left hand side flows to U(2)\_-3 U(1)\^bkg\_-1. where $\oplus$ means that the two factors $SU(2)_3$ and $U(1)^{\rm bkg}_1$ are completely decoupled. Here we need to remark the important point. The $SU(2)_{-3}$ is the 3d ${\cal N}=2$ gauge theory at the level $-3$. This theory contains the gaugino, and by integrating out the gaugino, we get a pure topological Chern-Simons theory as U(2)\_-3 = SU(2)\^\_-1 Namely, the gaugino reduces the level by $2 = h^\vee _{su(2)}$. Therefore, the low energy limit is U(2)\^\_-1 U(1)\^bkg\_-1

The effect of $\sigma^{\rm bkg}$ on the right-hand-side of [\[eq:AF\]](#eq:AF){reference-type="eqref" reference="eq:AF"} is to give the dynamical $U(1)$ an FI parameter. We want the dynamical gauge group $U(1)$ to be not Higgsed so that we can match it with the $SU(2)^\text{topo CS}_{-1}$ later. Then, the D-term condition implies that the dynamical real scalar $\sigma$ gets a vev proportional to $\sigma^{\rm bkg}$ because the Lagrangian contains $3/2D \sigma + 2 \cdot 2D  \sigma^{\rm bkg}$ and we need to impose stationary condition for $D$. The vev of $\sigma$ gives the chiral field a mass term. The sign of the mass is anticipated by the fact that it must make the low energy CS level of the dynamical field as $U(1)_{-2}$. This is because the only consistent way for the duality to work in low energy is to use the duality of topological CS theory given by U(2)\^\_-1 = U(1)\^\_-2 \~U(1)\^\_2 where we have used the fact that the gaugino plays no role in $U(1)$ and hence $U(1)_{-2}=U(1)^\text{topo CS}_{-2}$. First equality is well-known (see, e.g., [@DiFrancesco:1997nk] for the corresponding statement in Wess-Zumino-Witten models which are related to topological Chern-Simons theories [@Witten:1988hf].). The second equality $U(1)^\text{topo CS}_{2} \sim  U(1)^\text{topo CS}_{-2}$ is more precisely given by $U(1)_2 \times U(1)_{-1} =U(1)_{-2} \times U(1)_{1}$ [@Seiberg:2016rsg; @Tachikawa:2016cha; @Tachikawa:2016nmo] and we have neglected $U(1)_{\pm 1}$ because these theories have only one state in the Hilbert space on any space (and they are called invertible field theory), and our argument is not careful enough to detect those invertible field theories.

After integrating out the chiral field, the right-hand-side of [\[eq:AF\]](#eq:AF){reference-type="eqref" reference="eq:AF"} is given by the Lagrangian ( 2 V+ 2 V\^bkg +n V\^bkg \^bkg ). where in the second term, the factor of $2$ have taken into account the fact that $\mathrm{U}(1)^{\rm bkg}$ is coupled to the topological current of $\mathrm{U}(1)$ by charge $2$. We shift the dynamical gauge field as $V \to V+V^{\rm bkg}$ to get ( 2 V+ (n-2) V\^bkg \^bkg ). This means that the low energy theory is given by (1)\^\_2 U(1)\^bkg\_n-2. Therefore by comparing the low energy limit of the left and right hand side of [\[eq:AF\]](#eq:AF){reference-type="eqref" reference="eq:AF"}, we get =n-2 n=1.

#### Weeks theory

Now let us gauge $U(1)^{\rm bkg}$ (but we use the same name for simplicity). The left hand side of [\[eq:AF\]](#eq:AF){reference-type="eqref" reference="eq:AF"} after gauging $U(1)^{\rm bkg}$ is precisely the theory $T^{6d}_{\rm irred}[\text{Weeks}]$.

Let us see the right hand side. The Chern-Simons action of the right-hand-side of [\[eq:AF\]](#eq:AF){reference-type="eqref" reference="eq:AF"} after putting $n=1$ is given by ( V+ 2 V\^bkg + V\^bkg \^bkg ). where in the second term, the factor of $2$ have taken into account the fact that $U(1)^{\rm bkg}$ is coupled to the topological current of $U(1)_{3/2}$ by charge $2$. If we integrate out $V^{\rm bkg}$, or in other words, by making the shift $V^{\rm bkg}  \to V^{\rm bkg}  + 2V$ and neglecting the decoupled $U(1)_{1}$ theory, we get ( ( -4) V) = ( - V).

We conclude that the theory $T^{6d}_{\rm irred}[\text{Weeks}]$ is given by \^6d\_irred\[\] = (). This is one of the small theories discussed in [@Gang:2017lsr].
