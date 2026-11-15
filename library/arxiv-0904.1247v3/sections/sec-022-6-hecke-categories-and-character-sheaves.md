---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-022-6-hecke-categories-and-character-sheaves
section_title: "Hecke categories and character sheaves"
section_number: 6
pages: 34-38
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.838
latex_coverage_ratio: 0.988
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
[]{#character section label="character section"}

In this section, we study the homotopical algebra of Hecke categories arising in representation theory. Our focus is the Hecke category of ${\mathcal D}$-modules on the double quotient stack $B\backslash G/B$ of a reductive group $G$ by a Borel subgroup $B\subset G$, and its unipotent monodromic variant. Our aim is to construct a topological field theory from these Hecke categories, and in particular to relate their traces and centers with character sheaves.

If we introduce the classifying stacks $X=BB$, $Y=BG$, then the double quotient stack can be realized as the fiber product $$B\backslash G/B\simeq X \times_Y X$$ From this point of view, the special technical features of this setup are the following:

1.  The morphism $p:X\to Y$ is proper.

2.  The diagonal $\delta:X\to X\times X$ is smooth.

The second property is especially restrictive though satisfied by classifying spaces of smooth group schemes. The above conditions will imply that we have a sufficient arsenal of duality and adjunctions.

## Hecke categories {#convolution algebras}

We establish here that Hecke categories

are semi-rigid categories with a canonical Calabi-Yau structure, and thus two-dualizable monoidal categories defining oriented topological field theories.

To begin, let $p:X\to Y$ be a morphism of stacks. Introduce the Hecke category $\mathcal H={\mathcal D}(X\times_Y X)$. Consider the convolution diagram $$\label{convolution diagram}
\xymatrix{
& \ar[dl]_-{p_{12}}\ar[dr]^-{p_{23}} \ar[d]_{p_{13}}X \times_Y X \times_Y X & \\
X \times_Y X& X \times_Y X& X \times_Y X}$$ Equip $\mathcal H={\mathcal D}(X\times_Y X)$ with the monoidal product defined by convolution $$\xymatrix{
\star:\mathcal H\otimes \mathcal H\ar[r] & \mathcal H
}$$ $$\xymatrix{
\mathfrak M\star \mathfrak N= p_{13*}(p_{12}^!(\mathfrak M) \otimes p_{23}^!(\mathfrak N))
\simeq p_{13*}(p_{12} \times p_{23})^!(\mathfrak M\boxtimes \mathfrak N)
}$$

Similar diagrams provide the usual associativity compatibilities of an algebra object. The monoidal unit $1_\mathcal H$ is given by the pushforward $u_*\omega_X$ along the map $u:X\to X \times_Y X$ induced by the diagonal $\delta:X \to X\times X$.

Recall that if $p:X\to Y$ is safe, then the integral transform construction gives a monoidal functor $$\xymatrix{
\mathcal H\ar[r] &  \mathop{\mathrm{Fun}}_{{\mathcal D}(Y)}({\mathcal D}(X), {\mathcal D}(X))
&
\mathfrak M\ar@{|->}[r] & p_{2*}(p_1^!(-) \otimes\mathfrak M)
}$$

::: remark
More formally, the monoidal structure on ${\mathcal D}(X\times_Y X)$ can be defined as follows. The stack $X \times_Y X$ can be identified with endomorphisms of $X$ in the $\infty$-category of stacks over $Y$ with morphisms given by correspondences. The assignment of categories of ${\mathcal D}$-modules extends to a symmetric monoidal functor on this $\infty$-category (see Remark [\[correspondences\]](#correspondences){reference-type="ref" reference="correspondences"}), hence induces an associative algebra structure on ${\mathcal D}(X \times_Y X)$.
:::

It is important to note that all of the maps involved in the monoidal structure of $\mathcal H$ are obtained by base change from either the diagonal map $\delta:X\to X \times X$ or the projection $p:X\to Y$. Moreover, the monoidal structure only uses pullbacks along maps of the first type and pushforwards along maps of the second type. Thus if we assume $\delta$ is smooth and $p$ is proper, the functors $\delta^!$ and $p_*$, and hence the monoidal product on $\mathcal H$, will be quasi-proper. In addition, ${\mathcal D}(X)$ is semi-rigid under tensor product, by Proposition [\[BG semirigid\]](#BG semirigid){reference-type="ref" reference="BG semirigid"}.

::: theorem
[]{#perfect Hecke label="perfect Hecke"} Suppose $X$ is a stack with smooth diagonal, $Y$ is a stack, and $X\to Y$ is a proper representable map.

Then the Hecke category $\mathcal H={\mathcal D}(X \times_Y X)$ is semi-rigid (hence 2-dualizable).
:::

::: proof
*Proof.* To prove the theorem, let us first establish a candidate for the dual of a compact object.

First, recall that Verdier duality $\mathbb D_{X \times_Y X}$ provides a self-duality $$\xymatrix{
\mathcal H={\mathcal D}(X \times_Y X) \simeq {\mathcal D}(X \times_Y X)' = \mathcal H'
}$$ By definition, the compact objects of $\mathcal H$ and $\mathcal H'$ form opposite categories to each other.

Next consider the swap involution $$\xymatrix{
\sigma: X \times_Y X\ar[r]^-\sim & X \times_Y X
& \sigma (x_1, y_{12}, x_2) = (x_2, y_{12}^{-1}, x_1)
}$$ where $y^{-1}_{12}$ is the path $y_{12}$ traced in the opposite direction. The induced equivalence on ${\mathcal D}$-modules intertwines the algebra structure and the opposite algebra structure $$\xymatrix{
\sigma:\mathcal H\ar[r]^-\sim & \mathcal H^{op}.
}$$

Finally, introduce the composite of the swap involution, Verdier duality and shift $$\xymatrix{
\iota : \mathcal H\ar[r]^-\sim & \mathcal H'
&
\iota(\mathfrak M) = \mathbb D_{X \times_Y X}(\sigma(\mathfrak M)) [2\dim X]
}$$

We will show that any compact object $\mathfrak M\in \mathcal H$ is left and right dualizable, with both duals identified with $\iota(\mathfrak M) \in \mathcal H$, thereby establishing that $\mathcal H$ is semi-rigid. Following the discussion of Section [\[duals\]](#duals){reference-type="ref" reference="duals"}, it suffices to establish for a compact object $\mathfrak M\in \mathcal H$, and arbitrary objects $\mathfrak L, \mathfrak N\in \mathcal H$, that there are functorial equivalences $$\xymatrix{
\mathop{\mathrm{Hom}}_{\mathcal H}(\mathfrak L\star \mathfrak M, \mathfrak N)
 \simeq \mathop{\mathrm{Hom}}_{\mathcal H}(\mathfrak L, \mathfrak N\star \iota(\mathfrak M))
& 
\mathop{\mathrm{Hom}}_{\mathcal H}(\mathfrak M\star \mathfrak L, \mathfrak N)
\simeq   \mathop{\mathrm{Hom}}_{\mathcal H}(\mathfrak L, \iota(\mathfrak M) \star\mathfrak N)
}$$

We will give a proof of the first. The second is similar or follows by applying $\sigma$ to the first and renaming objects.

Observe that it suffices to establish the equivalence for $\mathfrak L, \mathfrak N\in \mathcal H$ compact objects. For arbitrary objects $\mathfrak L, \mathfrak N\in \mathcal H$, it then follows by continuity by taking colimits first in $\mathfrak N$ then in $\mathfrak L$.

For $\mathfrak L, \mathfrak M, \mathfrak N\in \mathcal H$ compact objects, we will establish the equivalent identity $$\xymatrix{
\mathop{\mathrm{Hom}}_{\mathcal H}(\mathbb C_{X \times_Y X}, \mathbb D_{X \times_Y X}(\mathfrak L\star \mathfrak M)\otimes \mathfrak N)
 \simeq \mathop{\mathrm{Hom}}_{\mathcal H}(\mathbb C_{X \times_Y X}, \mathbb D_{X \times_Y X}(\mathfrak L)\otimes (\mathfrak N\star \iota(\mathfrak M)))
}$$

Since $p_{13}$ is a base change of $p$, it is proper and hence $p_{13*}$ commutes with Verdier duality. Since $p_{12}\times p_{23}$ is a base change of $\delta$, it is smooth of relative dimension $-\dim X$ and hence $(p_{12} \times p_{13})^* \simeq (p_{12} \times p_{13})^![2\dim X]$. Hence we have the identity $$\begin{aligned}
 \mathbb D_{X \times_Y X}(\mathfrak L\star \mathfrak M)
&\simeq  &  \mathbb D_{X \times_Y X}(p_{13*}((p_{12} \times p_{13})^!(\mathfrak L\boxtimes  \mathfrak M)))\\
&\simeq  &  p_{13*}\mathbb D_{X \times_Y X}(p_{12} \times p_{13})^!(\mathfrak L\boxtimes  \mathfrak M)\\
&\simeq  &  p_{13*}(p_{12} \times p_{13})^*(\mathbb D_{X \times_Y X}(\mathfrak L) \boxtimes  \mathbb D_{X \times_Y X}(\mathfrak M))\\
&\simeq  &  p_{13*}(p_{12} \times p_{13})^!(\mathbb D_{X \times_Y X}(\mathfrak L) \boxtimes  \mathbb D_{X \times_Y X}(\mathfrak M)) [2\dim X]\\
&\simeq  &  \mathbb D_{X \times_Y X}(\mathfrak L) \star  \mathbb D_{X \times_Y X}(\mathfrak M) [2\dim X]\\
\end{aligned}$$

Substituting this into the above sought after identity and renaming objects, we seek to establish the following general identity $$\label{general eq}
\Gamma_{X \times_Y X}((\mathfrak L\star \mathfrak M)\otimes \mathfrak N)
  \simeq  \Gamma_{X \times_Y X}(\mathfrak L\otimes (\mathfrak N\star \sigma(\mathfrak M)))$$

Let us first modestly reformulate how to calculate each side, in particular the quantities obtained before taking global sections. For the left hand side, consider the commutative diagram whose right hand square is Cartesian $$\xymatrix{
 && 
\ar[d]^-{{\rm id}\times p_{13}} \ar[dll]_-{\hspace{-3em} p_{12} \times p_{23} \times p_{13}}  (X\times_Y X\times_Y X)  \ar[r]^-{p_{13}} & X \times_Y X\ar[d]^-\Delta\\
(X \times_Y X)^3 && \ar[ll]^-{p_{12} \times p_{23} \times p_{45}} (X\times_Y X\times_Y X) \times (X \times_Y X) \ar[r]_-{p_{13} \times p_{45}} & (X \times_Y X)^2 
}$$ By a composition identity in the triangle and base change in the right hand square, there is a functorial equivalence $$(\mathfrak L\star \mathfrak M)\otimes \mathfrak N\simeq p_{13*}(p_{12}\times p_{23} \times  p_{13})^!
(\mathfrak L\boxtimes \mathfrak M\boxtimes \mathfrak N)$$

Similarly, for the right hand side, consider the commutative diagram whose right hand square is Cartesian $$\xymatrix{
&& 
\ar[d]^-{p_{13} \times {\rm id}} \ar[dll]_-{\hspace{-3em} p_{13} \times \sigma p_{23} \times  p_{12}}  (X\times_Y X\times_Y X)  \ar[r]^-{p_{13}} & X \times_Y X\ar[d]^-\Delta\\
(X \times_Y X)^3 && \ar[ll]^-{p_{12} \times \sigma p_{45} \times  p_{34}} (X \times_Y X) \times  (X\times_Y X\times_Y X)\ar[r]_-{p_{12} \times p_{35}} & (X \times_Y X)^2 
}$$ By a composition identity in the triangle and base change in the right hand square, there is a functorial equivalence $$\mathfrak L\otimes ( \mathfrak N\star \sigma(\mathfrak M)) \simeq p_{13*} (p_{13} \times \sigma p_{23} \times  p_{12})^!
(\mathfrak L\boxtimes \mathfrak M\boxtimes \mathfrak N)$$

Finally, observe that there is a natural commutative diagram $$\xymatrix{
\ar[drr]^-\sim_{r} \ar[d]_-{p_{13} \times \sigma p_{23} \times  p_{12}}  (X\times_Y X\times_Y X)  \ar[rr]^-{p_{13}} &&  X \times_Y X\\
(X \times_Y X)^3 && \ar[ll]^-{p_{12} \times  p_{23} \times  p_{13}}  (X\times_Y X\times_Y X)  \ar[u]_-{p_{13}} 
}$$ where the diagonal map $r$ is the rotational equivalence given by $$\xymatrix{
r (x_1, y_{12}, x_2, y_{23}, x_3) = (x_1, y_{12} \circ y_{23}, x_3, y^{-1}_{23}, x_2)
}$$ where the path $y_{12} \circ y_{23}$ is the composition of the paths $y_{12}, y_{23}$, and the path $y^{-1}_{23}$ is the path $y_{23}$ traced in the opposite direction.

Let us write $\pi:X \times_Y X\to pt$. We have seen that the two sides of the sought after equivalence [\[general eq\]](#general eq){reference-type="eqref" reference="general eq"} can be realized by going around the edges of the above diagram $$\Gamma_{X \times_Y X}((\mathfrak L\star \mathfrak M)\otimes \mathfrak N) \simeq 
\pi_*p_{13*}(p_{12} \times p_{23} \times p_{13})^!(\mathfrak L\boxtimes \mathfrak M\boxtimes \mathfrak N)$$ $$\Gamma_{X \times_Y X}(\mathfrak L\otimes (\mathfrak N\star \sigma(\mathfrak M)))
 \simeq \pi_*p_{13*}(p_{13} \times \sigma p_{23} \times p_{13})^!(\mathfrak L\boxtimes \mathfrak M\boxtimes \mathfrak N)$$ Thus the rotational equivalence $r$ intertwines them and we obtain the equivalence [\[general eq\]](#general eq){reference-type="eqref" reference="general eq"}. ◻
:::

::: theorem
[]{#CY Hecke label="CY Hecke"} Suppose $X,Y$ are as in Theorem [\[perfect Hecke\]](#perfect Hecke){reference-type="ref" reference="perfect Hecke"}. Then the Hecke category $\mathcal H={\mathcal D}(X \times_Y X)$ carries a canonical Calabi-Yau structure.
:::

::: proof
*Proof.* Let us briefly recall from [@HA Section 5.3.3] the realization of Hochschild homology and its $S^1$ symmetry from the point of view of topological chiral homology.

First, given a framed circle $S$, for example, the standard circle $S^1=[0,1]/\hspace{-0.25em}\sim$ with its natural induced orientation, let $I_S$ be the $\infty$-category given by the nerve of the poset of framed embeddings of finite disjoint unions of open intervals in $S$ with partial order given by framed inclusions. Given the $E_1$-algebra $\mathcal H$, introduce the natural functor $$\xymatrix{
\psi_\mathcal H:I_S\ar[r] &  St_\mathbb C
& \psi_{\mathcal H}(I) = \mathcal H^{\otimes \pi_0(I)}
}$$ whose structure on morphisms is given by the $E_1$-structure on $\mathcal H$. By definition, the topological chiral homology of $\mathcal H$ over $S$ is the colimit $$\xymatrix{
\int_{S} \mathcal H= \mathop{\mathrm{colim}}_{I_S} \psi_{\mathcal H}
}$$ Observe that the above makes sense for families of framed circles, and so exhibits $\int_{S} \mathcal H$ as the fiber of an $\infty$-local system over the moduli of framed circles $B\mathit{Diff^+}(S^1)$.

Recall as well that for the standard circle $S^1=[0,1]/\hspace{-0.25em}\sim$, the realization of the bar resolution in terms of subdivisions of the interval $[0,1]$ provides a natural morphism which is an equivalence $$\xymatrix{
\operatorname{Tr}(\mathcal H) \simeq | \mathcal H\otimes_{\mathcal H\otimes \mathcal H^{op}} C_*(\mathcal H)| \ar[r]^-\sim & \mathop{\mathrm{colim}}_{I_{S^1}} \psi_{\mathcal H} = \int_{S^1} \mathcal H
}$$

Now to endow $\mathcal H$ with a Calabi-Yau structure, let $\mathbb S\to B\mathit{Diff^+}(S^1)$ denote the universal framed circle, and let $\mathbb{V}\hspace{-0.25em}\operatorname{ect}_\mathbb C$ denote the constant $\infty$-local system on $B\mathit{Diff^+}(S^1)$ with fiber $\operatorname{Vect}_\mathbb C$. We must construct a morphism of $\infty$-local systems $$\xymatrix{
\tau:\int_{\mathbb S} \mathcal H\ar[r] &\mathbb{V}\hspace{-0.25em}\operatorname{ect}_\mathbb C
}$$ Moreover, for a given framed circle $S$ and pair of disjoint open intervals $I_1 \coprod I_2 \subset S$ (hence any framed circle with any pair of disjoint open intervals), the natural composite map $$\xymatrix{
\mathcal H\otimes \mathcal H\simeq \mathcal H^{\pi_0(I_1\coprod I_2)} \ar[r] & \int_{S} \mathcal H\ar[r]^-{\tau_S} &\mathbb{V}\hspace{-0.25em}\operatorname{ect}_\mathbb C
}$$ must be the evaluation pairing of a self-duality of $\mathcal H\in St_\mathbb C$.

To achieve this, given an object $I = \coprod_i I_i \in I_S$, let $\mathcal M(I)$ be the stack of maps $\coprod_i  I_i\to Y$ with lifts $\coprod_i \partial I_i \to  X$ at boundary points. (Note we do not regard the boundary points of the intervals as embedded in $S$ since they may coincide as, for example, for an interval of the form $I = S\setminus\{s\}$ where $s\in S$ is a single point.) Let $D$ be a closed disk with $\partial D = S$, and $\mathcal M(D, I)$ be the stack of maps $D\to Y$ with a lift over the complement $S\setminus (\coprod_i  I_i) \to  X$. Consider the natural correspondence $$\xymatrix{
 \mathcal M(I) & \ar[l]_-p \mathcal M(D, I) \ar[r]^-q & pt
 }$$ Observe that $\psi_\mathcal H(I) = {\mathcal D}(\mathcal M(I))$ and thanks to standard identities for ${\mathcal D}$-modules, the functor $$\xymatrix{
  {\mathcal D}(\mathcal M(I))\ar[r] &  \operatorname{Vect}_\mathbb C&  M \ar@{|->}[r] & q_*p^!M 
  }$$ provides a natural augmentation to the diagram given by $\psi_\mathcal H$ and hence a functor $$\xymatrix{
\tau_S:\int_{S} \mathcal H\ar[r] &\operatorname{Vect}_\mathbb C
}$$ Since the above makes sense for families of framed circles, it descends to the sought after morphism of $\infty$-local systems $$\xymatrix{
\tau:\int_{\mathbb S} \mathcal H\ar[r] &\mathbb{V}\hspace{-0.25em}\operatorname{ect}_\mathbb C
}$$

Finally, consider the natural composite map $$\xymatrix{
\mathcal H\otimes \mathcal H\simeq \mathcal H^{\pi_0(I_1\coprod I_2)} \ar[r] & \int_{S} \mathcal H\ar[r]^-{\tau_S} &\mathbb{V}\hspace{-0.25em}\operatorname{ect}_\mathbb C
}$$ Unwinding the above, we find it is given by the functor $$\xymatrix{
 \mathcal H\otimes \mathcal H\simeq {\mathcal D}(X \times_Y X\times X \times_Y X) \ar[r] &  \operatorname{Vect}_\mathbb C
 &
  M \ar@{|->}[r] & q_*p^!M 
  }$$ where $p:X \times_Y X\to X \times_Y X\times X \times_Y X$ is the diagonal and $q:X \times_Y X\to pt$ is the projection. Observe that under the identification of $\mathcal H\in St_\mathbb C$ with its dual given by Verdier duality, the above morphism is precisely the evaluation pairing. ◻
:::

::: remark
We will soon identify $\operatorname{Tr}(\mathcal H) \simeq \int_{S} \mathcal H$ with a full subcategory of ${\mathcal D}$-modules on the loop space $\mathcal LY$. Consider the natural correspondence of constant loops $$\xymatrix{
\mathcal LY & \ar[l]_-e Y \ar[r]^-\pi & pt
}$$ Thanks to standard identities for ${\mathcal D}$-modules, the trace $\tau_S:\int_{S} \mathcal H\to \operatorname{Vect}_\mathbb C$ will factor through the functor $$\xymatrix{
  {\mathcal D}(\mathcal LY)\ar[r] &   \operatorname{Vect}_\mathbb C& M \ar@{|->}[r] & \pi_*e^!M
  }$$
:::

The above theorems thus allow us to apply the Cobordism Hypothesis [@jacob; @TFT] to the Hecke category to obtain an oriented two-dimensional topological field theory.

::: cor
[]{#Hecke TFT label="Hecke TFT"} There is a unique symmetric monoidal functor $\mathcal Z: 2Bord \to Alg_{(1)}(St_\mathbb C)$

with $\mathcal Z(pt)=\mathcal H$.
:::

## Loop spaces and horocycle correspondences

We establish here the basic relation between Hecke categories and loop spaces. It is an abstraction of the horocycle correspondence from representation theory. We will continue with the assumptions that $p:X\to Y$ is proper and $X$ has smooth diagonal $\delta:X\to X\times X$.

Consider the fundamental correspondence $$\xymatrix{
 \mathcal LY  = Y\times_{Y\times Y} Y & \mathcal LY \times_Y X =X \times_{X \times Y} X \ar[l]_-{q} \ar[r]^-{\epsilon} & X\times_Y X.\\
}$$ where $q$ is a base change of $p$, and $\epsilon$ is a base change $\delta$.

Define the functor $$\xymatrix{
F: {\mathcal D}(X\times_Y X) \ar[r]^-{\epsilon^!} & {\mathcal D}(\mathcal LY \times_Y X) 
 \ar[r]^-{q_*}& {\mathcal D}(\mathcal LY) \\
}$$ Since $q$ is a base change of $p$ and hence proper, there is an adjunction $(q_*,q^!)$, and since $\epsilon$ is a base change of $\delta$ and hence smooth, of relative dimension $-\dim X$, there is an equivalence $\epsilon^*\simeq\epsilon^![2\dim X]$ and an adjunction $(\epsilon^*,\epsilon_*)$. Thus there is the continuous right adjoint $$\xymatrix{
F^r:{\mathcal D}(\mathcal LY)   \ar[r]^-{q^!}&{\mathcal D}(\mathcal LY \times_Y X)  \ar[rr]^-{\epsilon_*[-2\dim X]} && {\mathcal D}(X\times_Y X)\\
}$$

Let $\mathcal I(F) \subset {\mathcal D}(\mathcal LY)$ denote the cocompletion of the image of $F$. It is naturally equivalent to the left orthogonal ${}^\perp \mathcal K(F^r) \subset {\mathcal D}(\mathcal LY)$ to the kernel of $F^r$. Since $q^!$ satisfies descent, both in turn are naturally equivalent to the full subcategory of ${\mathcal D}(\mathcal LY)$ of objects whose image under $q^!$ is in the cocompletion of the image of $\epsilon^!$.

::: theorem
[]{#thm center label="thm center"} There is a natural commutative diagram $$\xymatrix{
 {\mathcal D}(X \times_Y X) & \\
{}^\perp \mathcal K(F^r) \ar[u]^-{F^r} \ar[r]^-\sim&  \ar[ul]_-\mathfrak z\operatorname{Z}({\mathcal D}(X \times_Y X)) 
}$$
:::

::: proof
*Proof.* For notational convenience, set $\mathcal A= {\mathcal D}(X \times_Y X)$ and $\mathcal B= {\mathcal D}(X)$. Observe that pushforward along the relative diagonal $\mathcal B\to \mathcal A$ is monoidal, and thus we may regard $\mathcal A$ as an algebra in $\mathcal B$-bimodules.

Given an algebra $\mathcal A$ in $\mathcal B$-bimodules, we have its relative bar resolution $$\xymatrix{
  \mathcal A\simeq 
  \left| \mathcal A^{\otimes_\mathcal B(\bullet+2)} \right| 
  }$$ which can be used to calculate its center $$\xymatrix{
\operatorname{Z}(\mathcal A) =  \mathop{\mathrm{Hom}}_{\mathcal A\otimes \mathcal A^{op}}(\mathcal A, \mathcal A) = \mathop{\mathrm{Hom}}_{\mathcal A\otimes \mathcal A^{op}}(\left| \mathcal A^{\otimes_\mathcal B(\bullet+2)} \right|,  \mathcal A) = 
  \mathop{\mathrm{Tot}}\left\{\mathop{\mathrm{Hom}}_{\mathcal B\otimes \mathcal B^{op}} (\mathcal A^{\otimes_\mathcal B\bullet},  \mathcal A) \right\}
}$$ We will access the center as the totalization of the cosimplicial object $$\mathcal C^\bullet =  \mathop{\mathrm{Hom}}_{\mathcal B\otimes \mathcal B^{op}} (\mathcal A^{\otimes_\mathcal B\bullet},  \mathcal A)$$

Unwinding the notation and using the canonical identity ${\mathcal D}(X)^{\otimes k} \simeq {\mathcal D}(X^k)$, we find the cosimplicial category $$\xymatrix{
\mathcal C^\bullet \simeq 
\mathop{\mathrm{Fun}}_{{\mathcal D}(X\times X)}^L({\mathcal D}( (X \times_Y X)^{\times_X\bullet } ), {\mathcal D}(X \times_Y X))
}$$

Using the canonical identification of functors with integral transforms of Proposition [\[prop int trans adjoint\]](#prop int trans adjoint){reference-type="ref" reference="prop int trans adjoint"}, we have a level-wise fully faithful map of cosimplicial diagrams $$\xymatrix{
\mathcal C^\bullet \ar[r] &  
 {\mathcal D}(X^{\times_Y (\bullet+1)} \times_Y \mathcal LY)
 }$$ where the cosimplicial structure maps on the latter are given by $!$-pullback functors.

Thus the center $\operatorname{Z}(\mathcal A)$ is equivalent to the full subcategory of ${\mathcal D}(\mathcal LY)$ of objects whose image under $q^!$ is in the cocompletion of the image of $\epsilon^!$. ◻
:::

::: cor
[]{#cor trace label="cor trace"} There is a natural commutative diagram $$\xymatrix{
& \ar[dl]_-\mathfrak {tr}{\mathcal D}(X \times_Y X) \ar[d]^-{F} &\\
\operatorname{Tr}({\mathcal D}(X \times_Y X)) \ar[r]^-\sim   & \mathcal I(F)
}$$
:::

::: proof
*Proof.* We have seen that ${\mathcal D}(X\times_Y X)$ is semi-rigid and pivotal, and hence its center and trace are equivalent. More precisely, the augmented semi-cosimplicial diagram calculating the center can be obtained from the augmented semi-simplicial diagram calculating the trace by passing to right adjoints. In particular, the universal central functor can be obtained as the right adjoint of the universal trace. Thus passing to left adjoints in the diagram of the previous theorem provides the diagram of the corollary. ◻
:::

## Character sheaves

Now we apply our previous results to our motivating example when $X=BB$, $Y=BG$, for a reductive group $G$ and Borel subgroup $B\subset G$. Thus we are studying the Hecke category $\mathcal H_G = {\mathcal D}(B\backslash G/B)$ of Borel bi-equivariant ${\mathcal D}$-modules on $G$.

With this setup, the fundamental correspondence is the horocycle correspondence $$\xymatrix{
G/G & \ar[l]_-{q} (G\times G/B)/G \ar[r]^-{\epsilon} & B\backslash G/B.
}$$ It contains the traditional Springer correspondence as a subspace $$\xymatrix{
G/G & \ar[l]_-{} \widetilde G/G\simeq B/B \ar[r]^-{} & B\backslash B/B \simeq BB
}$$ where $\widetilde G \subset G \times G/B$ comprises pairs where the group element fixes the flag.

::: definition
The dg category ${Ch}_G$ of unipotent character sheaves is defined to be the full subcategory of ${\mathcal D}(G/_{\hspace{-0.2em}ad}\hspace{0.1em}G)$ generated (under colimits) by the image of the Harish Chandra transform $F$.
:::

Applying our previous results, we immediately obtain the following.

::: theorem
[]{#thm char shvs label="thm char shvs"} The category of unipotent character sheaves ${Ch}_{G}$ is equivalent to both the trace and center of the Hecke category $\mathcal H_{G}$. The equivalences fit into natural adjoint commutative diagrams $$\xymatrix{
&  \mathcal H_{G} \ar[dl]_-\mathfrak {tr}\ar[d]<-1ex>_-{F}&\\
 \operatorname{Tr}(\mathcal H_{G}) \ar[r]^-\sim & \ar[u]<-1ex>_-{F^r} {Ch}_{G} \ar[r]^-\sim
 &  \ar[ul]_-\mathfrak z\operatorname{Z}(\mathcal H_G)
   }$$
:::
