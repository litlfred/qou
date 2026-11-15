---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-001-2-defining-equations-and-elementary-properties
section_title: "Defining Equations and Elementary Properties"
section_number: 2
pages: 2-3
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 1.0
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#sec: defining equations label="sec: defining equations"}

In this section we shall introduce Bring's curve describing its basic properties, its period matrix and its automorphisms. We begin with two descriptions: one as a model in $\mathbb{P}^4$ and the second as a plane curve. In particular we shall construct the birational map between these models, which we believe new. Such a map enables us to concretely translate calculations from one model to another and will be helpful later in §[\[sec: quotients by subgroups\]](#sec: quotients by subgroups){reference-type="ref" reference="sec: quotients by subgroups"} when we look at quotients of the curve.

::: definition
**Bring's Curve $\mathcal{B}$** is defined in $\mathbb{P}^4$ by the (homogeneous) equations[^1] $$\label{eq: P4 model of Bring}
H_k := \sum_{i=1}^5 x_i^k = 0  , \quad k=1, 2, 3,$$ where we have taken the coordinates $[x_1 : x_2 : x_3 : x_4 : x_5] \in \mathbb{P}^4$.
:::

We will call ([\[eq: P4 model of Bring\]](#eq: P4 model of Bring){reference-type="ref" reference="eq: P4 model of Bring"}) the $\mathbb{P}^4$-model of Bring's curve. Historically, this curve was attributed to Bring by Klein in his lectures on the icosahedron [@Klein1888]. Bring's improvement on the Tschirnhaus transformation enabled the general quintic to be brought to the Bring-Jerrard form $x^5 + ex+f=0$ [@Adamchik2003]: if $x_i$, $i=1,\dots, 5,$ are the roots of this equation then the symmetric sums $\sum_i x_i^k=0$ for $k=1, 2, 3$, and so the above curve emerges. Green [@Green1978] exploits this relation to Bring's curve to (implicitly) solve the quintic using automorphic forms. At this stage we may observe that $S_5\leq \mathop{\mathrm{Aut}}(\mathcal{B})$.

::: remark
In the above definition we have implicitly taken $\mathbb{P}^4 = \mathbb{CP}^4$, and indeed this will be our definition throughout. At various junctures we will however highlight the number fields within $\mathbb{C}$ that are relevant fields of definition for morphisms of the curve, or geometrically important points on the curve.
:::

For many calculations a plane model of a curve in $\mathbb{P}^2$ is useful. One of the main tools we will utilise in this paper is the Riemann surfaces module of SageMath [@sagemath2021] which requires such a model. As such we introduce the following.

::: definition
The **Hulek-Craig (HC) model** of Bring's curve is the (singular) plane curve in $\mathbb{P}^2$ given by $$\label{eq: P2 model of Bring}
  F(X,Y,Z) :=
    X(Y^5+Z^5) + (XYZ)^2 - X^4YZ -2(YZ)^3  = 0  ,$$ taking homogeneous coordinates $[X:Y:Z] \in \mathbb{P}^2$.
:::

This model was used in [@Hulek1985; @Craig2002] where they studied the curves modular properties. Indeed Craig gives a parameterization of the curve in terms of modular functions following work of Ramanujan. Craig does not identify the curve as Bring's, whereas Hulek finds the equation as a hyperplane section of a surface that parameterises elliptic normal curves of degree 5, and then refers to previous results to connect it with Bring. This connection was first made in [@Naruki1978], where the curve is attributed to Klein. Indeed, because of this interpretation, one can write down Bring's curve as $$\overline{\mathcal{H}/\Gamma_0(2, 5)} \quad \text{where} \quad \Gamma_0(2,5) = \Gamma_0(2) \cap \Gamma(5) =  \left\lbrace\begin{pmatrix} a & b \\ c & d \end{pmatrix} \in SL_2(\mathbb{Z}) \, \big\vert \, \begin{array}{l} a \equiv d \equiv 1\pmod 5 \\ \phantom{d \equiv } \;  b \equiv 0  \pmod 5 \\ \phantom{d \equiv } \; c \equiv 0  \pmod{10} \end{array} \right \rbrace .$$ To our knowledge, [@Hulek1985] is the first occurrence of this plane model of the curve; Klein will write it down in [@Klein1888 p. 165, p. 242] but the relation to a plane model of Bring's curve is not made explicit. We will call ([\[eq: P2 model of Bring\]](#eq: P2 model of Bring){reference-type="ref" reference="eq: P2 model of Bring"}) the HC-model of Bring's curve. In the following subsection we shall show the birational equivalence of ([\[eq: P2 model of Bring\]](#eq: P2 model of Bring){reference-type="ref" reference="eq: P2 model of Bring"}) and ([\[eq: P4 model of Bring\]](#eq: P4 model of Bring){reference-type="ref" reference="eq: P4 model of Bring"}).

Another plane model of Bring's curve is given by $y^5-(x+1)x^2(x-1)^{-1}=0$, introduced in [@Weber2005 Proposition 3.1] by considering the curve as a cyclic cover of $\mathbb{P}^1$, see §[\[sec: quotients by subgroups\]](#sec: quotients by subgroups){reference-type="ref" reference="sec: quotients by subgroups"}.

[^1]: Note here we use the notation $H_k$ of [@Burns1983] for the symmetric sum, whereas [@Edge1978] uses $S_k$.
