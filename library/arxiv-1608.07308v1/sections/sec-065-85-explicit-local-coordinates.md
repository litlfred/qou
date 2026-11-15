---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-065-85-explicit-local-coordinates
section_title: "Explicit local coordinates"
section_number: 8.5
pages: 62-64
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 0.909
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:localcoord label="sub:localcoord"}

In this section, we will use the special coefficients to describe the neighborhood of the fixed point $I_T$ for any standard Young tableau $T$: $$\label{eqn:localization}
\mathring{\mathrm{FHilb}}_T := \left( \mathrm{FHilb}_n \right)_{\text{localized at }T}$$ and the dg local ring $\mathring{\mathcal{A}}^\text{dg}_T = \mathbb{C}[\mathring{\mathrm{FHilb}}^\text{dg}_T ]$. In fact, we will actually describe an open subscheme of $\mathrm{FHilb}_T$ given by the non-vanishing of certain torus invariant functions. The resulting open subschemes also form a cover of $\mathrm{FHilb}_n$ because of the principle [\[eqn:principletorus\]](#eqn:principletorus){reference-type="eqref" reference="eqn:principletorus"}, so we abuse notation and use [\[eqn:localization\]](#eqn:localization){reference-type="eqref" reference="eqn:localization"} both for the local neighborhood and for the open subscheme $\mathring{\mathrm{FHilb}}_T \subset \mathrm{FHilb}_T$.

::: proposition
[]{#prop:chart label="prop:chart"}

For any standard Young tableau $T \vdash n$, the complex $\mathcal{E}_n$ of [\[eqn:complex\]](#eqn:complex){reference-type="eqref" reference="eqn:complex"} is: $$\label{eqn:localcomplex}
\mathcal{E}_n|_{\mathring{\mathrm{FHilb}}_T} \stackrel{\mathrm{q.i.s.}}\cong \left[\bigoplus^{\blacksquare\text{ outer}}_{\text{corner of }T} \mathcal{O}\cdot e_\blacksquare\stackrel{\psi}\longrightarrow \bigoplus^{\square\text{ inner}}_{\text{corner of }T} \mathcal{O}\cdot f_\square\right]$$ Theorem [\[thm:complex\]](#thm:complex){reference-type="ref" reference="thm:complex"} describes the map $\pi: \mathrm{FHilb}_{n+1} \rightarrow \mathrm{FHilb}_n$ as the projectivization of $H^0(\mathcal{E}_n)$. Locally, this map takes the form: $$\pi^{-1}\left(\mathring{\mathrm{FHilb}}_T \right) = \bigcup^{\square\text{ inner}}_{\text{corner of }T} \mathring{\mathrm{FHilb}}_{T \cup \square}$$ where $\mathring{\mathrm{FHilb}}_{T \cup \square} \subset \mathbb{P}H^0\left( \mathcal{E}^{\vee}_n|_{\mathring{\mathrm{FHilb}}_T} \right)$ is the affine chart of [\[eqn:localcomplex\]](#eqn:localcomplex){reference-type="eqref" reference="eqn:localcomplex"} given by $f_\square= 1$. We conclude [\[eqn:genrel\]](#eqn:genrel){reference-type="eqref" reference="eqn:genrel"}, where the generators are $f_{\square'}$ for inner corners $\square'\neq \square$ and the relations are $r_{\blacksquare} = \psi(e_\blacksquare)$.
:::

::: proof
*Proof.* From each box in $T$, draw two lines of unit length, one going up and one to the right:

::: picture
(70,155)(-140,-5) []{#fig label="fig"}

(7,6)$1$ (7,46)$3$ (7,86)$4$ (47,6)$2$ (47,46)$5$ (87,6)$6$ (87,46)$8$ (127,6)$7$

(0,0)(1,0)160 (0,40)(1,0)160 (0,80)(1,0)120 (0,120)(1,0)40

(0,0)(0,1)120 (40,0)(0,1)120 (80,0)(0,1)80 (120,0)(0,1)80 (160,0)(0,1)40

(20,100)(8,0)5 (60,60)(8,0)5(1,0)4 (60,20)(0,8)5(0,1)4 (100,60)(0,8)5 (140,20)(0,8)5

(20,20)(1,0)120 (140,20) (20,20)(0,1)80 (20,100) (100,20)(0,1)40 (100,60) (60,60) (20,60)(1,0)40
:::

The lines are of two types: thick or dotted, and black or red. The color of a line is determined by whether the line points to a box in $T$ or outside of $T$. The shape of a line is determined by the following rule: If $i>i'$ where $i'$ is the label of the box to the southeast (respectively northwest) of $i$, then we make the horizontal (respectively vertical) line starting at $i$ thick. All the boxes below and to the left of the diagram are thought to have label $0$ for the purpose of this rule, and all the boxes above and to the right of the diagram are thought to have label $\infty$. By definition: $$\label{eqn:localcomplex2}
\mathcal{E}_n = \Big[ qt\mathcal{T}_{n} \stackrel{\Psi}\longrightarrow q \mathcal{T}_n \oplus t \mathcal{T}_n \oplus \mathcal{O}\stackrel{\Phi}\longrightarrow \mathcal{T}_n \Big]$$ When we restrict the complex to the affine chart $\mathring{\mathrm{FHilb}}_T$, we observe that the tautological bundles are already trivialized by the basis $e_1,...,e_n$ of Definition [\[def:chart\]](#def:chart){reference-type="ref" reference="def:chart"}: $$\mathcal{T}_n |_{\mathring{\mathrm{FHilb}}_T} = \mathcal{O}\cdot e_1 \oplus ... \oplus \mathcal{O}\cdot e_n$$ Therefore, the middle term of [\[eqn:localcomplex2\]](#eqn:localcomplex2){reference-type="eqref" reference="eqn:localcomplex2"} has a basis which we will denote by $e_1,...,e_n, e_1',...,e_n',1$. We claim that the projection that forgets some of these basis vectors induces an isomorphism: $$\label{eqn:localkernel}
\text{Ker}\ \Phi|_{\mathring{\mathrm{FHilb}}_T} \cong \bigoplus^{\text{red or dotted horizontal}}_{\text{lines from box }i} \mathcal{O}\cdot e_i \bigoplus^{\text{red or dotted vertical}}_{\text{lines from box }i} \mathcal{O}\cdot e_i'$$ In other words, we claim that if one specifies rescaled basis vectors $c_i e_i$ and $d_i e_i'$ corresponding to the red and dotted edges, then there exist unique rescaled basis vectors $\gamma_i e_i$ and $\delta_i e_i'$ corresponding to the black thick edges, and a function $f$, such that: $$(X-x_{n+1})\left(\sum_{i\text{ dotted}} c_i e_i + \sum_{i\text{ thick}} \gamma_i e_i \right) + (Y-y_{n+1})\left(\sum_{i\text{ dotted}} d_i e_i + \sum_{i\text{ thick}} \delta_i e_i \right) + f e_1 = 0$$ Any box $k$ has a unique black thick line going to the left or down. Assume without loss of generality that the black thick line from $k$ leads one step left to the box $i$. Then [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"} implies that equating the coefficient of $e_k$ in the left hand side to 0 yields the equation: $$\gamma_i \in \sum_j (c_j \text{ or } d_j) \cdot \text{coefficients} + \sum_j (\gamma_j \text{ or }\delta_j) \cdot \mathring{\mathfrak{m}}_T$$ This system of equations can be solved in the localization $\mathring{\mathcal{A}}_T$, since its determinant is in $1+\mathring{\mathfrak{m}}_T$. Therefore, we conclude that in the local chart $\mathring{\mathrm{FHilb}}_T$, we have: $$\label{eqn:zzz}
\mathcal{E}_n|_{\mathring{\mathrm{FHilb}}_T} \stackrel{\mathrm{q.i.s.}}\cong \left[\bigoplus_{i=1}^n \mathcal{O}\cdot e_i \stackrel{\Psi}\longrightarrow \bigoplus^{\text{red or dotted horizontal}}_{\text{lines from box }i} \mathcal{O}\cdot e_i \bigoplus^{\text{red or dotted vertical}}_{\text{lines from box }i} \mathcal{O}\cdot e_i' \right]$$ The Proposition will be proved once we show that projecting the two terms in the above complex to a certain subset of factors induces a quasi-isomorphism. Specifically, in the domain of $\Psi$ we consider the subspace spanned by basis vectors $e_\blacksquare$ corresponding to outer corners $\blacksquare$, and in the codomain of $\Psi$ we project onto one basis vector $f_\square$ corresponding to each inner corner. The rule is that $f_\square= e_i$ or $e_{i'}'$, depending on whether the number $i$ to the left of $\square$ is bigger or smaller than the number $i'$ below $\square$. In other words, the only $e_i$ or $e_i'$ we will consider in the codomain of $\Psi$ are the ones corresponding to thick red lines: $$\label{eqn:zzzz}
\mathcal{E}_n|_{\mathring{\mathrm{FHilb}}_T} \stackrel{\mathrm{q.i.s.}}\cong \left[\bigoplus^{\blacksquare\text{ outer}}_{\text{corner of }T} \mathcal{O}\cdot e_\blacksquare\stackrel{\psi}\longrightarrow \bigoplus^{\square\text{ inner}}_{\text{corner of }T} \mathcal{O}\cdot (e_{\square\leftarrow} \text{ or } e'_{\square\downarrow}) \right]$$ In plain English, the claim is that for any $e_i$ where $i$ is not an outer corner of $T$, quotienting the codomain of [\[eqn:zzz\]](#eqn:zzz){reference-type="eqref" reference="eqn:zzz"} by the vector: $$\label{eqn:quotientvector}
\sum^{\text{red or dotted horizontal}}_{\text{lines between boxes }\bar{jk}} (x_i^j - \delta_j^i x_{n+1}) e_j + \sum^{\text{red or dotted vertical}}_{\text{lines between boxes }\bar{jk}} (y_i^j - \delta_j^i y_{n+1}) e_j'$$ will allow us to solve for one of the $e_j,e_{j}'$. The only basis vectors which remain unsolved for should be the ones that appear in the codomain of [\[eqn:zzzz\]](#eqn:zzzz){reference-type="eqref" reference="eqn:zzzz"}. For example, suppose we are trying to solve for $e_j$, where $j$ corresponds to a dotted horizontal edge $\bar{jk}$. Then with the notation in the following picture:

::: picture
(100,90)(-160,-5)

(10,10)$i$ (10,65)$j$ (65,10)$j'$ (65,65)$k$ (0,0)(1,0)80 (0,40)(1,0)80 (0,80)(1,0)80 (0,0)(0,1)80 (40,0)(0,1)80 (80,0)(0,1)80

(20,60)(8,0)5(1,0)4

(60,20)(0,1)40
:::

let us observe that [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"}--[\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"} imply that $y_i^j  = x_i^{j'} = y_{j'}^k \in 1 + \mathring{\mathfrak{m}}_T$. Then the vector [\[eqn:quotientvector\]](#eqn:quotientvector){reference-type="eqref" reference="eqn:quotientvector"} lies in $e_j + \mathring{\mathfrak{m}}_T$, and $e_j$ can therefore be solved for in the localization $\mathring{\mathcal{A}}_T$. ◻
:::
