---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains"
section_id: sec-011-24-geometry-of-the-potential-function
section_title: "Geometry of the potential function"
section_number: 2.4
pages: 16-21
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
toc_source: outline
text_source: latex
latex_prose_ratio: 0.784
latex_coverage_ratio: 0.991
---
[]{#geoWL label="geoWL"}

To understand the critical values of the potential functions, we need to find a concrete triangulation of the link complement associated to the potential function. The triangulation is the one appeared in [@T79]. First of all, we prepare an ideal octahedra (Figure [1](#f1){reference-type="ref" reference="f1"}). The idea is to glue the two blue faces together and the two red faces together (Figure [2](#f2){reference-type="ref" reference="f2"}) to form a cylinder.\

![ideal octahedron](f1){#f1 width="0.7\\linewidth"}

![glue the faces with the same color together](f2){#f2 width="0.4\\linewidth"}

The following pictures illustrate how to obtain a cylinder from an ideal octahedron.\

![the faces $B_1$ and $B_2$ are glued together](f3){width="\\linewidth"}

![deform the object so that it looks like a cylinder](f4){width="\\linewidth"}

![the faces $D_1$ and $D_2$ are glued together](f5){width="\\linewidth"}

![deform the object to obtain a cylinder with a clasp removed](f6){width="\\linewidth"}

\
Next, we consider the curl face of the cylinder. The labels $1,2,3,4$ refer to the truncated faces of the ideal octahedron. If we glue the top of the cylinder to the bottom according to the rule $C_2 \to C_1$ and $A_2 \to A_1$, we will obtain a decomposition of the boundary torus into parallelograms. Note that this torus is exactly the boundary torus of a tubular neighborhood of the belt component of the Whitehead link.\

![decomposition of the curl face into parallelograms](f7){width="\\linewidth"}

Next, we decompose the ideal octahedron into 5 ideal tetrahedra and assign shape parameters to them (Figure [3](#f8){reference-type="ref" reference="f8"}). The parameters $U,Z$ and $W$ are related by $U=(ZW)^{-1}$. The decomposition of the truncated faces and the assignments of shape parameters to them are shown in Figure [4](#f9){reference-type="ref" reference="f9"}.\

![decomposition of the ideal octahedron into 5 ideal tetrahedra](f8){#f8 width="0.9\\linewidth"}

<figure id="f9">
<p><img src="f9" alt="image" /><span id="f9" label="f9"></span></p>
<figcaption>assignment of shape parameters</figcaption>
</figure>

After that, we slide the left edge down (Figure [5](#f10){reference-type="ref" reference="f10"}) to obtain the geometric triangulation of the curl surface.\

![triangulation of the boundary torus of the belt component](f10){#f10 width="0.8\\linewidth"}

Recall that for each triangle, the shape parameters are given in counter-clockwise by $A$, $A' = \frac{1}{1-A}$ and $A'' = 1 - \frac{1}{A}$ respectively. From direct computation, for the boundary torus of the belt component, the edges equations are given by

-   vertex (i): $$\begin{aligned}
    &= \frac{-1}{W}\frac{-1}{Z}\frac{-1}{Z}\frac{-1}{B_2^{-1}W}\frac{-1}{B_2U}\frac{-1}{U}=1 
    \end{aligned}$$

-   vertex (ii): $$\begin{aligned}
    (WU'W'') ( (B_2U)' (B_2^{-1}W)'' (B_2U) )
    = \left(\frac{U'}{W'} \right) \left( \frac{(B_2U)''}{(B_2^{-1}W)''} \right)^{-1}
    = \frac{B_2\left(1-\dfrac{B_2}{W}\right)(1- W)}{(1-B_2U)\left(1-\dfrac{1}{U}\right)} \label{beltv2}
    \end{aligned}$$

-   vertex (iii): $$\begin{aligned}
    &= \frac{-1}{W}\frac{-1}{Z}\frac{-1}{Z}\frac{-1}{B_2^{-1}W}\frac{-1}{B_2U}\frac{-1}{U}=1
    \end{aligned}$$

-   vertex (iv): $$\begin{aligned}
    (UW'U'') ( (B_2^{-1}W)' (B_2U)'' (B_2^{-1}W) )
    = \left[\left(\frac{U'}{W'} \right) \left( \frac{(B_2U)''}{(B_2^{-1}W)''} \right)^{-1}\right]^{-1}\
    = \frac{(1-B_2U)\left(1-\dfrac{1}{U}\right)}{B_2\left(1-\dfrac{B_2}{W}\right)(1- W)} \label{beltv4}
    \end{aligned}$$

For the top and bottom truncated faces, we have\

![triangulation of the boundary torus of the belt component](f11){#f11 width="0.8\\linewidth"}

From direct computation, for the boundary torus of the clasp component, the edges equations are given by

-   vertex (v): $$\begin{aligned}
    (W) (B_2U)(B_2^{-1}W)''  (B_2U)' (W)'' (U') 
    = \left(\frac{U'}{W'} \right) \left( \frac{(B_2U)''}{(B_2^{-1}W)''} \right)^{-1}
    = \frac{B_2\left(1-\dfrac{B_2}{W}\right)(1- W)}{(1-B_2U)\left(1-\dfrac{1}{U}\right)}  \label{claspv1}
    \end{aligned}$$

-   vertex (vi): $$\begin{aligned}
    (B_2^{-1}W) (B_2U)''(W')  (U)'' (B_2^{-1}W)' (U) 
    = \left[\left(\frac{U'}{W'} \right) \left( \frac{(B_2U)''}{(B_2^{-1}W)''} \right)^{-1}\right]^{-1}
    = \left[ \frac{B_2\left(1-\dfrac{B_2}{W}\right)(1- W)}{(1-B_2U)\left(1-\dfrac{1}{U}\right)} \right]^{-1}\label{claspv2}
    \end{aligned}$$

Now we can explore the correspondence between the critical point equations of the potential function and the edges equations of this triangulation. For $\Phi^{+(s_1,s_2)}(z_1,z_2)$, recall that the critical point equations are given by

::: empheq
align &(1-e\^2i (s_2 -1)e\^-2i z_1 - 2i z_2) + (1 - e\^2i z_1 + 2i z_2) - (1 - e\^2i z_1)\
&= 2i[]{#smeridian1 label="smeridian1"}\
\
&(1-e\^2i (s_2 -1)e\^-2i z_1 - 2i z_2) + (1 - e\^2i z_1 + 2i z_2) - (1 - e\^2i (s_2 - 1) - 2i z_2)\
&- (1 - e\^2i z_2) []{#slong1 label="slong1"}\
&= 2i (s_2 - 1)
:::

Put $Z=e^{2\pi i z_1}$, $W=e^{2\pi i z_2}$, $U= (ZW)^{-1}$, $B_1 = e^{2\pi i s_1}$ and $B_2 = e^{2\pi i s_2}$. After taking exponential, we have

::: empheq
align &= B_1\^-1 B_2 []{#smeridian2 label="smeridian2"}\
&= B_2 []{#slong2 label="slong2"}
:::

In particular, from $(\ref{slong2})$ we have $$\left(\frac{U'}{W'} \right) \left( \frac{(B_2U)''}{(B_2^{-1}W)''} \right)^{-1} = 1$$ i.e. the edge equations of the triangulation ([\[beltv2\]](#beltv2){reference-type="ref" reference="beltv2"}), ([\[beltv4\]](#beltv4){reference-type="ref" reference="beltv4"}), ([\[claspv1\]](#claspv1){reference-type="ref" reference="claspv1"}) and ([\[claspv2\]](#claspv2){reference-type="ref" reference="claspv2"}) are satisfied. Furthermore, by ([\[smeridian2\]](#smeridian2){reference-type="ref" reference="smeridian2"}), the holonomy of the meridian of the belt component (Figure [5](#f10){reference-type="ref" reference="f10"}) is given by $$\begin{aligned}
m_1 = \frac{W''  U'}{W'' Z' (B_2 U)''} =\frac{B_2\left( 1-Z \right)}{\left(1 - B_2 U \right)\left( 1 - \dfrac{1}{U}\right)} = B_1 
\end{aligned}$$

By ([\[slong2\]](#slong2){reference-type="ref" reference="slong2"}), the holonomy of the longitude of the clasp component (Figure [6](#f11){reference-type="ref" reference="f11"}) is given by $$\begin{aligned}
\label{slong2B2}
l_2 = \quad \frac{(B_2^{-1}W)'}{(B_2U)'} \cdot \frac{U''}{W''} =  \frac{(1-B_2U)\left(1-\dfrac{1}{U}\right)}{\left(1-\dfrac{B_2}{W}\right)(1- W)} \times B_2 = B_2^2
\end{aligned}$$

Finally, for the potential function $\Phi^{-(s_1,s_2)}(z_1,z_2)$, by replacing $B_1$ by $B_1^{-1}$ in the above, we have the same correspondence between critical point equations of the potential function and the hyperbolic gluing equation for the triangulation of the link complement.
