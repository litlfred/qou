---
doc_id: arxiv-math-0409593v1
doc_title: "Categorification of sl_2 and braid groups"
section_id: sec-002-21-a-general-construction
section_title: "A general construction"
section_number: 2.1
pages: 2-4
source_pdf: 0409593v1.pdf
source_sha256: ad965f5c80838824
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.936
doc_brief: "Categorification of sl_2 and braid groups — 20 sections: Front matter; Introduction; Self-equivalences"
---
### 

This section can probably be skipped in a first reading.

We will be working here with *algebraic* triangulated categories (following Keller), a simple setting that provides functorial cones.

Let ${\mathcal{E}}$ be a Frobenius category (an exact category with enough projective and injective objects and where injective and projective objects coincide). Let $\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}\operatorname{\!-proj}\nolimits)$ be the category of acyclic complexes of projective objects of ${\mathcal{E}}$. Let $\operatorname{Frob}\nolimits$ be the $2$-category of Frobenius categories, with $1$-arrows the exact functors that send projectives to projectives and $2$-arrows the natural transformations of functors.

The construction ${\mathcal{E}}\mapsto \operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}\operatorname{\!-proj}\nolimits)$ is an endo-$2$-functor of $\operatorname{Frob}\nolimits$. The $2$-functor from ${\mathcal{E}}$ to the $2$-category of triangulated categories that sends ${\mathcal{E}}$ to its stable category $\bar{{\mathcal{E}}}$ factors through the previous functor.

The important point is that the category $\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}\operatorname{\!-proj}\nolimits)$ has functorial cones. Given $F,G:\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}\operatorname{\!-proj}\nolimits)\to
\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}'\operatorname{\!-proj}\nolimits)$ and $\phi:F\to G$, then we have a well defined cone $C(\phi)$ of $\phi$ and we have morphisms $G\to C(\phi)$ and $C(\phi)\to F[1]$ such that $F\to G\to C(\phi)\to F[1]$ gives a distinguished triangle of functors from $\bar{{\mathcal{E}}}$ to $\bar{{\mathcal{E}}'}$.

Note that if $\phi_0:F_0\to G_0$ is a morphism of functors (exact, preserving projectives) between ${\mathcal{E}}$ and ${\mathcal{E}}'$, then we get via $\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}(-)$ a morphism of functors $\phi:F\to G$, with $F,G:\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}\operatorname{\!-proj}\nolimits)\to
\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}'\operatorname{\!-proj}\nolimits)$.

The category of functors (exact, preserving projectives) $\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}\operatorname{\!-proj}\nolimits)\to \operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}'\operatorname{\!-proj}\nolimits)$ is a Frobenius category. We define the category $\mathrm{AlgTr}({\mathcal{E}},{\mathcal{E}}')$ to be its stable category. Its objects are the exact functors $\operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}\operatorname{\!-proj}\nolimits)\to \operatorname{Comp}\nolimits_{\operatorname{acyc}\nolimits}({\mathcal{E}}'\operatorname{\!-proj}\nolimits)$ and $\operatorname{Hom}\nolimits_{\mathrm{AlgTr}({\mathcal{E}},{\mathcal{E}}')}(F,G)$ is the image of $\operatorname{Hom}\nolimits(F,G)$ in $\operatorname{Hom}\nolimits_{\operatorname{Fun}\nolimits(\bar{{\mathcal{E}}},\bar{{\mathcal{E}}'})}(\bar{F},\bar{G})$.

This defines the $2$-category of algebraic triangulated categories $\mathrm{AlgTr}$, with objects the Frobenius categories ${\mathcal{E}}$. We have a $2$-functor from $\mathrm{AlgTr}$ to the $2$-category of triangulated categories obtained by sending ${\mathcal{E}}$ to $\bar{{\mathcal{E}}}$. It is $2$-fully faithful.

###  {#constrequiv}

Let ${\mathcal{C}}$ and ${\mathcal{D}}$ be two algebraic triangulated categories, $F:{\mathcal{C}}\to{\mathcal{D}}$, $G:{\mathcal{D}}\to{\mathcal{C}}$ be two functors and $\Phi$ be a self-equivalence of ${\mathcal{C}}$. Let there be given also two adjoint pairs $(F,G)$ and $(G,F\Phi)$. We have four morphisms (units and counits of the adjunctions) $$\eta:1_{\mathcal{D}}\to F\Phi G,\ \ \ \varepsilon:GF\Phi\to 1_{\mathcal{C}}$$ $$\eta':1_{\mathcal{C}}\to GF,\ \ \ \varepsilon':FG\to 1_{\mathcal{D}}.$$ Let $\Upsilon$ be the cocone of $\varepsilon'$ and $\Upsilon'$ be the cone of $\eta$ : there are distinguished triangles of functors $\Upsilon\to FG\buildrel \varepsilon'\over \longrightarrow 1_{\mathcal{D}}\rightsquigarrow$ and $1_{\mathcal{D}}\buildrel \eta\over \longrightarrow F\Phi G \to\Upsilon'\rightsquigarrow$.

Assume $$\label{GF}
1_{\mathcal{C}}\xrightarrow{\eta'}GF\xrightarrow{\varepsilon\Phi^{-1}}\Phi^{-1}
{\buildrel 0\over\rightsquigarrow}$$ is a distinguished triangle.

::: prop
[]{#inversibilitetriang label="inversibilitetriang"} The functors $\Upsilon$ and $\Upsilon'$ are inverse self-equivalences of ${\mathcal{D}}$.
:::

::: proof
*Proof.* Let $\gamma$ be the map $F\Phi G\to \Upsilon'$ in the triangle above, *i.e.*, we have the distinguished triangle $1_{\mathcal{D}}\buildrel \eta\over \longrightarrow F\Phi G\xrightarrow{\gamma}\Upsilon'
\rightsquigarrow$. We have a commutative diagram with horizontal and vertical distinguished triangles $$\xymatrix{
&& \\
&& FG\ar@{~>}[u] \\
FG \ar[rr]^-{FG\eta}\ar[urr]^-{\operatorname{id}\nolimits} && FGF\Phi G \ar[rr]^-{FG\gamma}\ar[u]_-{F\varepsilon G} &&
 FG\Upsilon' \ar@{~>}[r] & \\
&& F\Phi G\ar[u]^-{F\eta'\Phi G}
}$$ The octahedral axiom shows that $(FG\gamma)\circ(F\eta'\Phi G):F\Phi G\buildrel \sim\over\to FG\Upsilon'$ is an isomorphism.

We have a commutative diagram $$\xymatrix{
F\Phi G\ar[rr]^-{F\eta'\Phi G}\ar[drr]_-{\operatorname{id}\nolimits} && FGF\Phi G\ar[rr]^-{FG\gamma}
 \ar[d]^-{\varepsilon'F\Phi G} && FG\Upsilon' \ar[d]^-{\varepsilon'\Upsilon'}\\
&& F\Phi G \ar[rr]_-{\gamma} && \Upsilon'
}$$ The distinguished triangle $\Upsilon \Upsilon'\to FG\Upsilon'\xrightarrow{\varepsilon'\Upsilon'} \Upsilon'
\rightsquigarrow$ gives a distinguished triangle $\Upsilon \Upsilon'\to F\Phi G\xrightarrow{\gamma} \Upsilon'\rightsquigarrow$, hence $\Upsilon \Upsilon'\simeq 1_{\mathcal{D}}$.

The case of $\Upsilon'\Upsilon$ is similar --- note that the triangle ([\[GF\]](#GF){reference-type="ref" reference="GF"}) shows that $GF\simeq \operatorname{id}\nolimits_{\mathcal{D}}\oplus \Phi^{-1}$, hence $\Phi$ commutes with $GF$. ◻
:::

::: rem
One sees easily that $\eta F+F\Phi\eta':F\oplus F\Phi\buildrel \sim\over\to F\Phi GF$ and $G \eta +\eta'\Phi G:G\oplus \Phi G\buildrel \sim\over\to GF\Phi G$ are isomorphisms. One can show that the requirement that $\eta FG+F\Phi\eta'G:FG\oplus F\Phi G\to F\Phi GFG$ and $FG \eta +F\eta'\Phi G:FG\oplus F\Phi G\to FGF\Phi G$ are isomorphisms, instead of the stronger requirement that ([\[GF\]](#GF){reference-type="ref" reference="GF"}) is a distinguished triangle, is enough to get Proposition [\[inversibilitetriang\]](#inversibilitetriang){reference-type="ref" reference="inversibilitetriang"}.
:::

###  {#section-1}

Let us recall a version of Barr-Beck's Theorem ([@Mac §VI.7, exercice 7], [@De2 §4.1]).

Let ${\mathcal{C}}$ be a category. A comonad is the data of a functor $H:{\mathcal{C}}\to{\mathcal{C}}$, of $c:H\to H^2$ and $\varepsilon:H\to\operatorname{id}\nolimits$ such that $(cH)\circ c=(Hc)\circ c$ and $(\varepsilon H)\circ c=(H\varepsilon)\circ c$. Note that $\varepsilon$ is determined by $c$.

A coaction of $(H,c,\varepsilon)$ on an object $M$ of ${\mathcal{C}}$ is the data of $\rho:M\to H(M)$ such that $\varepsilon(M)\circ\rho=\operatorname{id}\nolimits_M$ and $c\circ\rho=F(\rho)\circ\rho$. The category $(H,c,\varepsilon)\operatorname{\!-comod}\nolimits$ has objects the pairs $(M,\rho)$ and a morphism $(M,\rho)\to (M',\rho')$ is a morphism $f:M\to M'$ such that $\rho'f=H(f)\rho$.

Let ${\mathcal{A}}$ and ${\mathcal{B}}$ be two abelian (resp. algebraic triangulated categories), $T:{\mathcal{A}}\to{\mathcal{B}}$ an exact functor (resp. a triangulated functor). Assume $T$ has a right adjoint $U$. Put $H=TU$, denote by $\varepsilon:H\to \operatorname{id}\nolimits_{\mathcal{B}}$ and $\eta:\operatorname{id}\nolimits_{\mathcal{A}}\to UT$ the counit and unit of adjunctions and let $c=T\eta U:H\to H^2$.

We have a functor ${\tilde{T}}:{\mathcal{A}}\to (H,c,\varepsilon)\operatorname{\!-comod}\nolimits$ given by $M\mapsto (TM,T\eta(M))$.

The following Theorem is an easy application of Barr-Beck's general result to abelian and triangulated categories.

::: thm
If $T$ is faithful, then ${\tilde{T}}:{\mathcal{A}}\buildrel \sim\over\to(H,c,\varepsilon)\operatorname{\!-comod}\nolimits$ is an equivalence.
:::

We deduce from this Theorem that the category ${\mathcal{C}}$, together with the functors $F$, $G$ and the adjunctions, is determined by ${\mathcal{D}}$, $\Theta=FG$ and $c=F\eta'G:\Theta\to \Theta^2$. We view this as a categorical version of the "fixed points" construction.

::: rem
Let $V=K_0({\mathcal{D}})$, $U=K_0({\mathcal{C}})$, $f=[F]:U\to V$ and $g=[G]:V\to U$. Assume $[\Phi]=\operatorname{id}\nolimits_U$. Then, $gf=2 \operatorname{id}\nolimits_U$ and $\theta=[\Theta]:x\mapsto x-fg(x):V\to V$ is an involution. One recovers $U$ (up to unique isomorphism) from $\theta$ acting on $V$ as $V^{\theta}$.
:::
