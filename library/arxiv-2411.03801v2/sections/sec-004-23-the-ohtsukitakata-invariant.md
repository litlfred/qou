---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-004-23-the-ohtsukitakata-invariant
section_title: "The Ohtsuki–Takata invariant"
section_number: 2.3
pages: 7-9
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.9
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
[]{#sub.OT label="sub.OT"}

To define the Ohtsuki--Takata invariant, we consider two more functions associated with $\mathring{D}$. To define the first one, for each crossing, cup and cap of $\mathring{D}$, we choose two corners around it and associate a rational function with each of them, shown as in Figure [1](#fig.omega1){reference-type="ref" reference="fig.omega1"}. These functions are well-defined and non-zero for essential corners. The *first normalizing function* $\Omega_1$ is defined as the product of these rational functions over all essential corners among chosen ones.

<figure id="fig.omega1">

<figcaption>Rational functions associated with crossings, cups and caps.</figcaption>
</figure>

To define the last function, we fix an orientation of $\mathring{D}$. Then choose one corner around each crossing of $\mathring{D}$ and associate a rational function with the corner as in Figure [2](#fig.omega2){reference-type="ref" reference="fig.omega2"}. These functions are well-defined for essential corner. The *second normalizing function* $\Omega_2$ is defined as the product of these rational functions over all essential corners among chosen ones.

<figure id="fig.omega2">

<figcaption>Rational functions associated with crossings.</figcaption>
</figure>

We now have all the ingredients to define the Ohtsuki--Takata invariant.

::: definition
The *Ohtsuki--Takata invariant* of an essential open diagram $\mathring{D}$ is defined as $$\label{eqn.OT}
\omega(\mathring{D}) := \pm \frac{\Omega_1 \Omega_2}{2} \, \det \left (
x_i \dfrac{\partial}{\partial x_i} \left(x_j\, \dfrac{\partial V}{ \partial x_j}
\right)\right)_{1 \leq i,j \leq n}$$ where the right-hand side is evaluated at the solution $x^\circ$.
:::

It was proved that the Ohtsuki--Takata invariant is invariant under Reidemeister II and III moves involving interior crossings of essential diagrams [@OT2015 Prop.4.3], and was conjectured that the invariant $\omega(\mathring{D})$ is equal to the adjoint Reidemeister torsion associated to the holonomy representation.

**Example [\[ex.61\]](#ex.61){reference-type="ref" reference="ex.61"} continued.** The normalizing functions $\Omega_1$ and $\Omega_2$ of the essential open diagram $\mathring{D}$ given in Figure [\[fig.example\]](#fig.example){reference-type="ref" reference="fig.example"} are given by $$\Omega_1 =
\left(1-\frac{x_2}{x_1}\right)
\left( 1-\frac{x_3}{x_2}\right), \qquad
\Omega_2  =  \frac{1}{x_1^2} x_1^2 \, \dfrac{1}{x_3^2} \, x_3^2 = 1 \,.$$ The Ohtsuki--Takata invariant, evaluated at the geometric solution [\[61xapp\]](#61xapp){reference-type="eqref" reference="61xapp"} is $\omega(\mathring{D}) \approx  -0.487465 - 1.738045 i$. This agrees with the adjoint Reidemeister torsion of the knot $6_1$.
