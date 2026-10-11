---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-013-5-integral-transforms-for-d-modules
section_title: "Integral transforms for D-modules"
section_number: 5
pages: 30-34
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.969
---
[]{#integral transforms label="integral transforms"}

We continue with our standing assumptions of preceding sections. In particular, by a scheme, we mean a quasi-compact, separated derived scheme. By a stack, we mean a quasi-compact stack with affine diagonal, and by a representable morphism, we mean a quasi-compact schematic morphism. A stack is safe if its de Rham cohomology functor is continuous, and more generally, a morphism is safe if the pushforward of ${\mathcal D}$-modules along it is continuous.

In the previous section, we recalled that for any stacks $X_1, X_2$, external tensor product induces an equivalence $$\xymatrix{{\mathcal D}(X_1)\otimes{\mathcal D}(X_2)\ar[r]^-{\sim}& {\mathcal D}(X_1\times X_2).}$$ Verdier duality induces a canonical self-duality $$\xymatrix{{\mathcal D}(X_1)\simeq {\mathcal D}(X_1)'
 }$$

If in addition $X_1$ is safe, then the integral transform construction provides a description of the resulting equivalence $$\xymatrix{{\mathcal D}(X_1 \times X_2)\ar[r]^-\sim & \mathop{\mathrm{Fun}}^L({\mathcal D}(X_1), D(X_2))
 &
 \mathfrak M\ar@{|->}[r] &  \pi_{2*}(\pi_1^!(-) \otimes\mathfrak M)
 }$$

The above equivalences fit into a canonically commuting diagram $$\xymatrix{
\ar[d]_-\sim  {\mathcal D}(X_1)\otimes {\mathcal D}(X_2) \ar[r]^-\sim &  {\mathcal D}(X_1 \times X_2) \ar[d]^-\sim \\
  {\mathcal D}(X_1)'\otimes {\mathcal D}(X_2) \ar[r]^-\sim &   \mathop{\mathrm{Fun}}^L({\mathcal D}(X_1), D(X_2))
 }$$ Namely, for $\mathfrak M_1\in {\mathcal D}(X_1), \mathfrak M_2\in {\mathcal D}(X_2)$, there is a canonical identity $$\xymatrix{
 \pi_{2*}(\pi_1^!(-) \otimes (\pi_1^!\mathfrak M_1 \otimes \pi_2^!\mathfrak M_2)) \simeq 
 \Gamma(X_1, \mathfrak M_1 \otimes - ) \otimes \mathfrak M_2\simeq 
 \mathop{\mathrm{Hom}}_{{\mathcal D}(X_1)}(\mathbb D_{X_1} \mathfrak M_1, -) \otimes \mathfrak M_2
 }$$ between going around the upper right and the lower left parts of the diagram.

In this section, we will record some simple relative versions of the above assertions. While we will consider very restrictive hypotheses, the assertions often fail in any more relaxed setting.

## Functoriality over schemes

We will not need the results of this section but they naturally fit into the theme of the paper and are likely useful elsewhere.

::: theorem
[]{#relative product label="relative product"} For a diagram $X_1\to Y \leftarrow X_2$ where $X_1,X_2$ are stacks and $Y$ a scheme, the canonical map induced by $!$-pullbacks is an equivalence $$\xymatrix{
{\mathcal D}(X_1)\otimes_{{\mathcal D}(Y)} {\mathcal D}(X_2) \ar[r]^-\sim & {\mathcal D}(X_1\times_Y X_2).
}$$
:::

::: proof
*Proof.* The tensor product of ${\mathcal D}(Y)$-modules can be calculated as the geometric realization of the two-sided bar construction ([@HA 4.3.4]), the simplicial category with $k$-simplices $${\mathcal D}(X_1)\otimes{\mathcal D}(Y)\otimes\cdots \otimes{\mathcal D}(Y)\otimes{\mathcal D}(X_2),$$ where the factor ${\mathcal D}(Y)$ appears $k$ times

and the maps are given by the ${\mathcal D}(Y)$-module structures in the usual pattern. This is canonically equivalent to the simplicial category with $k$-simplices $${\mathcal D}(X_1 \times Y\times\cdots \times Y \times X_2)$$ where the factor $Y$ appears $k$ times and the maps are given by $!$-pullbacks in the usual pattern.

This extends to an augmented simplicial category with augmentation given by the pullback $$\xymatrix{
j_{-1}^!:{\mathcal D}(X_1 \times X_2)\ar[r] & {\mathcal D}(X_1 \times_Y X_2)
}$$ along the relative diagonal $$\xymatrix{
j_{-1}:X_1\times_Y X_2 \ar[r] & X_1 \times X_2
}$$ The map $j_{-1}$ is a base change of the diagonal map of $Y$, and since $Y$ is a separated scheme, $j_{-1}$ is a closed embedding.

Similarly, the analogous diagonal maps $$\xymatrix{
j_k: X_1 \times Y \times \cdots \times Y \times  X_2 \ar[r] & X_1\times Y\times \cdots \times Y \times Y \times X_2
}$$ where the factor $Y$ appears $k$ times in the domain and $k+1$ times in the codomain are closed embeddings.

Now let us consider pushforwards along the above closed embeddings and apply Kashiwara's lemma: for a closed embedding $j$ and a ${\mathcal D}$-module $\mathfrak M$, the natural adjunction map $\mathfrak M\to  j^!j_*\mathfrak M$ is an equivalence. Thus by base change, the pushforward $$\xymatrix{
j_{-1*}:{\mathcal D}(X_1 \times_Y   X_2) \ar[r] & {\mathcal D}(X_1 \times X_2)
}$$ and its higher analogues $$\xymatrix{
j_{k *}:{\mathcal D}(X_1 \times Y \times \cdots \times Y \times  X_2)\ar[r] & {\mathcal D}(X_1\times Y\times\cdots \times Y \times Y \times X_2)
}$$ provide a lift to a split augmented simplicial category.

Finally, by [@topos Lemma 6.1.3.16], in any $\infty$-category, split augmented simplicial diagrams are colimit diagrams. ◻
:::

::: theorem
[]{#thm selfdual label="thm selfdual"} Let $X$ be a stack, $Y$ a scheme, and $f:X\to Y$ a safe morphism (for example, a relative Deligne-Mumford stack). Then ${\mathcal D}(X)$ is a self-dual module over ${\mathcal D}(Y)$.
:::

::: proof
*Proof.* By Theorem [\[relative product\]](#relative product){reference-type="ref" reference="relative product"}, we have a canonical equivalence $${\mathcal D}(X)\otimes_{{\mathcal D}(Y)} {\mathcal D}(X) \simeq
{\mathcal D}(X\times_Y X).$$ Thus we can define a unit and counit by the correspondences $$\xymatrix{
u=\Delta_*f^!: {\mathcal D}(Y)  \ar[r] & {\mathcal D}(X\times_Y X) \simeq {\mathcal D}(X)\otimes_{{\mathcal D}(Y)} {\mathcal D}(X)
}$$ $$\xymatrix{
c=f_*\Delta^!: {\mathcal D}(X)\otimes_{{\mathcal D}(Y)} {\mathcal D}(X)  \simeq {\mathcal D}(X\times_Y X) \ar[r] & {\mathcal D}(Y)
}$$ where $\Delta:X\to
X\times_Y X$ is the diagonal. Here we assume $f:X\to Y$ is safe to ensure the continuity of the functor $f_*$.

We must check that the following composition is the identity $$\xymatrix{ 
{\mathcal D}(X)  \ar[r]^-{u \otimes\operatorname{id}} & {\mathcal D}(X)\otimes_{{\mathcal D}(Y)} {\mathcal D}(X)\otimes_{{\mathcal D}(Y)} {\mathcal D}(X)
\ar[r]^-{\operatorname{id}\otimes c}  & {\mathcal D}(X). 
}$$ Consider the following commutative diagram with Cartesian square: $$\xymatrix{
& 
\ar[d]_{\Delta} X \ar[rr]^-{\Delta} 
& &
X\times_Y X \ar[r]^-{\pi_1} \ar[d]^-{{\rm id}_1\times\Delta_{23}} 
& X 
\\
X
& 
\ar[l]_-{\pi_2} X\times_Y X \ar[rr]^-{ \Delta_{12}\times{\rm id}_3}
& &
X \times_Y X\times_Y X
& 
\\
}$$

Using standard identities for composition and base change, we calculate $$\begin{aligned}
(\operatorname{id}\otimes c)\circ (u \otimes\operatorname{id}) & = & 
\pi_{1*} ({\rm id}_1\times\Delta_{23})^!(\Delta_{12}\times{\rm id}_3)_*\pi^!_{2}\\
& \simeq & \pi_{1*} \Delta_*\Delta^!\pi^!_{2}\\
& \simeq & {\rm id}_{{\mathcal D}(X)}.
\end{aligned}$$ ◻
:::

If $X_1\to Y$ is safe as in the previous theorem, and $X_2\to Y$ is arbitrary, then the integral transform construction gives linear functors $$\xymatrix{{\mathcal D}(X_1 \times_Y X_2)\ar[r] & \mathop{\mathrm{Fun}}^L_{{\mathcal D}(Y)}({\mathcal D}(X_1), D(X_2))
 &
 \mathfrak M\ar@{|->}[r] &  \pi_{2*}(\pi_1^!(-) \otimes\mathfrak M)
 }$$ Its evident compatibility with the self-duality of Theorem [\[thm selfdual\]](#thm selfdual){reference-type="ref" reference="thm selfdual"} and the identification of Theorem [\[relative product\]](#relative product){reference-type="ref" reference="relative product"} immediately implies the following.

::: cor
[]{#cor selfdual label="cor selfdual"} Let $X_1, X_2$ be stacks, $Y$ a scheme, $X_1\to Y$ a safe morphism, and $X_2\to Y$ an arbitrary morphism. Then the natural maps are equivalences $$\xymatrix{
{\mathcal D}(X_1) \otimes_{{\mathcal D}(Y)} {\mathcal D}(X_2) 
\ar[r]^-\sim &  
{\mathcal D}(X_1\times_Y X_2) 
\ar[r]^-\sim & 
\mathop{\mathrm{Fun}}^L_{{\mathcal D}(Y)}({\mathcal D}(X_1), {\mathcal D}(X_2))
}$$ factoring the self-duality of ${\mathcal D}(X_1)$ over ${\mathcal D}(Y)$.
:::

## Functoriality over classifying stacks {#over stacks}

In this section, we present an equivariant generalization of Theorem [\[thm selfdual\]](#thm selfdual){reference-type="ref" reference="thm selfdual"} and its corollary realizing linear functors via integrals kernels on the fiber product. Unfortunately, results of this nature do not hold in great generality, but we will be content with the case when the base stack $Y$ is the classifying stack $BG$ of an affine group scheme $G$. What we specifically use is the restrictive property that the diagonal map of such stacks is smooth.

::: prop
[]{#BG semirigid label="BG semirigid"} For a stack $Y$ with smooth diagonal, the monoidal category ${\mathcal D}(Y)$ is semi-rigid with a canonical pivotal structure.
:::

::: proof
*Proof.* Since ${\mathcal D}(Y)$ is compactly generated and symmetric monoidal, it suffices to check that any compact object is dualizable.

For any compact object $\mathfrak M\in {\mathcal D}(Y)$, we will show that the monoidal dual is the shifted Verdier dual $\mathbb D_Y(\mathfrak M)[2\dim Y] \in {\mathcal D}(Y)$.

Following the discussion of Section [\[duals\]](#duals){reference-type="ref" reference="duals"}, it suffices to establish for any compact object $\mathfrak M\in {\mathcal D}(Y)$, and arbitrary objects $\mathfrak L, \mathfrak N\in {\mathcal D}(Y)$, that there is a functorial equivalence $$\label{dual eq}
\xymatrix{
\mathop{\mathrm{Hom}}_{{\mathcal D}(Y)}(\mathfrak L\otimes \mathfrak M, \mathfrak N)
 \simeq \mathop{\mathrm{Hom}}_{{\mathcal D}(Y)}(\mathfrak L, \mathfrak N\otimes \mathbb D_Y(\mathfrak M)[2\dim Y] )
}$$

Observe that it suffices to establish the equivalence for $\mathfrak L, \mathfrak N\in \mathcal H$ compact objects. For arbitrary objects $\mathfrak L, \mathfrak N\in \mathcal H$, it then follows by continuity by taking colimits first in $\mathfrak N$ then in $\mathfrak L$.

Using that the diagonal $\Delta:Y\to Y\times Y$ is smooth of relative dimension $-\dim Y$, note the following functorial equivalence $$\begin{aligned}
\mathbb D_Y(\mathfrak L\otimes \mathfrak M) & = & \mathbb D_Y\Delta^!(\mathfrak L\boxtimes \mathfrak M)\\
&  \simeq & \Delta^*(\mathbb D_Y(\mathfrak L) \boxtimes \mathbb D_Y(\mathfrak M))\\
& \simeq &  \Delta^!(\mathbb D_Y(\mathfrak L) \boxtimes \mathbb D_Y(\mathfrak M))[2\dim Y] \\
& \simeq &  \mathbb D_Y(\mathfrak L) \otimes \mathbb D_Y(\mathfrak M)[2\dim Y]
\end{aligned}$$

Now returning to the sought after equivalence [\[dual eq\]](#dual eq){reference-type="eqref" reference="dual eq"}, we find functorial equivalences $$\begin{aligned}
\mathop{\mathrm{Hom}}_{{\mathcal D}(Y)}(\mathfrak L\otimes \mathfrak M, \mathfrak N) &\simeq &\mathop{\mathrm{Hom}}_{{\mathcal D}(Y)}(\mathbb C_Y, \mathbb D_Y(\mathfrak L\otimes \mathfrak M) \otimes \mathfrak N) \\ 
&\simeq&  \mathop{\mathrm{Hom}}_{{\mathcal D}(Y)}(\mathbb C_Y, (\mathbb D_Y(\mathfrak L) \otimes \mathbb D_Y(\mathfrak M) [2\dim Y]) \otimes \mathfrak N)\\ 
&\simeq&\mathop{\mathrm{Hom}}_{{\mathcal D}(Y)}(\mathfrak L,  \mathbb D_Y(\mathfrak M)[2\dim Y]\otimes  \mathfrak N) 
\end{aligned}$$ ◻
:::

::: remark
Implicit in the proposition is the Poincaré duality identity $\mathbb D_Y(\omega_Y)[2\dim Y] \simeq \omega_Y$ since the dual of the monoidal unit must be the monoidal unit.
:::

::: cor
[]{#selfdual over stack label="selfdual over stack"} Let $Y$ be a stack with smooth diagonal, $X$ a stack, and $X\to Y$ an arbitrary morphism. Then ${\mathcal D}(X)$ is self-dual as a ${\mathcal D}(Y)$-module.
:::

::: proof
*Proof.* As a plain category, ${\mathcal D}(X)$ is self-dual, so the previous proposition and Proposition [\[bimodule dual\]](#bimodule dual){reference-type="ref" reference="bimodule dual"} imply the corollary. ◻
:::

If $X_1, X_2$ are stacks, $X_1\to Y$ is safe and $X_2\to Y$ is arbitrary, then there is a canonical map induced by $!$-pullbacks $$\xymatrix{
 \Psi: {\mathcal D}(X_1)\otimes_{{\mathcal D}(Y)} D(X_2) \ar[r] &  {\mathcal D}(X_1 \times_Y X_2)
  }$$ and the integral transform construction gives linear functors $$\xymatrix{
 \Phi:{\mathcal D}(X_1 \times_Y X_2)\ar[r] & \mathop{\mathrm{Fun}}^L_{{\mathcal D}(Y)}({\mathcal D}(X_1), D(X_2))
 &
 \Phi_\mathfrak M= 
 \pi_{2*}(\pi_1^!(-) \otimes\mathfrak M)
 }$$ Tracing back through the constructions and applying standard identities, the functors $\Psi,\Phi$ evidently provide a factorization $$\xymatrix{&{\mathcal D}(X_1 \times_Y X_2)\ar[dr]^-{\Phi}&\\
{\mathcal D}(X_1)\otimes_{{\mathcal D}(Y)} {\mathcal D}(X_2) \ar[rr]^-{\sim} \ar[ur]^-{\Psi}  &&\mathop{\mathrm{Fun}}^L_{{\mathcal D}(Y)}({\mathcal D}(X_1), {\mathcal D}(X_2))}$$ of the equivalence provided by Corollary [\[selfdual over stack\]](#selfdual over stack){reference-type="ref" reference="selfdual over stack"}. In general neither $\Psi,\Phi$ is itself an equivalence, but we have the following.

::: prop
[]{#prop int trans adjoint label="prop int trans adjoint"} Let $Y$ be a smooth stack with smooth diagonal, $X_1, X_2$ stacks, $X_1\to Y$ a safe morphism, and $X_2\to Y$ an arbitrary morphism.

Then the integral transform $\Phi$ admits a fully faithful left adjoint $\Phi^L$.
:::

::: proof
*Proof.* Tracing back through the algebraic arguments leading to Proposition [\[bimodule dual\]](#bimodule dual){reference-type="ref" reference="bimodule dual"}, one sees that the functor category $\mathop{\mathrm{Fun}}^L_{{\mathcal D}(Y)}({\mathcal D}(X_1), {\mathcal D}(X_2))$ can be calculated as the limit of the cosimplicial category with $k$-cosimplices $${\mathcal D}(X_1 \times Y\times\cdots \times Y \times X_2)$$ where the factor $Y$ appears $k$ times and the maps are given by pushforwards in the usual pattern. This naturally extends to an augmented cosimplicial category with augmentation given by the pushforward $$\xymatrix{
j_{-1*}: {\mathcal D}(X_1 \times_Y X_2) \ar[r] & {\mathcal D}(X_1 \times X_2)
}$$ along the relative diagonal $$\xymatrix{
j_{-1}:X_1\times_Y X_2 \ar[r] & X_1 \times X_2
}$$

By base change, this augmented cosimplicial category is left adjointable in the sense of [@HA Corollary 6.2.4.3], thus the integral transform construction $$\xymatrix{
\Phi:{\mathcal D}(X_1\times_Y X_2) \ar[r] & \mathop{\mathrm{Fun}}_{{\mathcal D}(Y)}({\mathcal D}(X_1), {\mathcal D}(X_2))
}$$ admits a fully faithful left adjoint. ◻
:::
