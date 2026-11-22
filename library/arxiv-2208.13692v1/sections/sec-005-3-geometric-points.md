---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-005-3-geometric-points
section_title: "Geometric Points"
section_number: 3
pages: 12-13
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.867
latex_coverage_ratio: 0.993
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
[]{#sec: geometric points label="sec: geometric points"} We now have a good understanding of how the automorphism group acts on the curve, and so before looking at quotient Riemann surfaces in §[\[sec: quotients by subgroups\]](#sec: quotients by subgroups){reference-type="ref" reference="sec: quotients by subgroups"} we want to first consider orbits of points that have geometric significance on the curve. These points will have important connections to the function theory of the curve; they are also related to physical aspects of Euclidean realisations (i.e. can be immersed in Euclidean 3-space) of the curve. Such orbits are characterised by the following result from Wiman.

::: prop
There are only 3 orbits orbits of points of size less than $120$ on $\mathcal{B}$ and these have sizes 24, 30, and 60 respectively.
:::

::: proof
*Proof.* By [@Farkas1992 III.7.7] we know the stabilizer of a point must be a cyclic group. The cyclic subgroups of $S_5$ are $C_2$, $C_3$, $C_4$, $C_5$, $C_6$; the corresponding orbits would thus be of (respective) sizes $60$, $40$, $30$, $24$ or $20$. To obtain Wiman's result we must show that $C_3$ does not fix a point on Bring's curve. Using Riemann-Hurwitz we have $$3=120(g-1)+30 a_{60}+40 a_{40}+45 a_{30}+48 a_{24}
+50 a_{20}$$ where $a_k\ge0$ are the number of $S_5$ orbits of size $k$. There are no solutions to this for $g\ge1$. For $g=0$ we have the unique solution $1=a_{60}=a_{30}=a_{24}$. This shows there can be no points with $C_3$ stabilizer. ◻
:::

These points and corresponding geometric structures are important when relating Clebsch's diagonal surface to Hilbert modular surfaces [@Hirzebruch1976; @Bell2004]. We identify these orbits as the geometric points on the curve defined in [@Singerman1997].[^1] Explicitly they are the vertices, face-centres, and edge-centres of the the universal map $\left\{ 5,4 \right\} _6$ - the Petrie polygon (as defined in [@Coxeter1980 §8.6]) of degree 6 coming from the tiling of the hyperbolic disk by pentagons, where 4 meet at a vertex [@Singerman1988]. It is noted in [@Weber2005] that this tessellation has a Euclidean realisation as a dodecadodecahedron (Figure [1](#fig: DID){reference-type="ref" reference="fig: DID"}). This has 30 vertices, 60 edges, and 24 faces, giving genus $$g = 1 - \frac{V-E+F}{2} = 4  ,$$ as we expect. In a recent paper, this connection to the dodecadodecahedron was used to identify Bring's curve as the moduli space of equilateral plane pentagons up to the action of the conformal group [@Ramshaw2022]. The (small) stellated dodecahedron (Figure [2](#fig: SSD){reference-type="ref" reference="fig: SSD"}) also has genus 4 (having $V=12=F$, $E=30$), coming from the tessellation $\left\{ 5/2, 5 \right\}  \cong \left\{ 5, 5  |  3 \right\}$, which can be interpreted as adding 3 'holes' to the $\left\{ 5,5 \right\}$ tessellation [@Coxeter1980 §8.5]. This $\left\{ 5,5|3 \right\}$ tessellation has automorphism group $C_2 \times A_5$, which is an index-2 subgroup of $C_2 \times S_5$, the automorphism group of $\left\{ 5,4 \right\} _6$. This is due to the map $D_1$ defined in [@Hendriks2013 §3.1], which maps the dodecadodecahedron to the small sellated dodecahedron. We include both these tessellations in Figure [6](#fig: tessellations){reference-type="ref" reference="fig: tessellations"} below. Klein connects the small stellated dodecahedron to Bring's curve through a degree-3 covering $\mathcal{B} \to \mathbb{P}^1$ constructed from the hyperbolic triangles giving the tessellation [@Weber2005], and we will see this map later in §[\[sec: theta characteristics\]](#sec: theta characteristics){reference-type="ref" reference="sec: theta characteristics"} in a different context.

<figure id="fig: geometric realisations">
<figure id="fig: DID">
<img src="DID_crop.png" />
<figcaption>Dodecadodecahedron.</figcaption>
</figure>
<figure id="fig: SSD">
<img src="SSD_crop.png" />
<figcaption>Small Stellated Dodecahedron.</figcaption>
</figure>
<figcaption>Geometric realisations.</figcaption>
</figure>

<figure id="fig: tessellations">
<figure id="fig: 54 tessellation">
<img src="54_tessellation.png" />
<figcaption><span class="math inline">{5,4}</span> tessellation.</figcaption>
</figure>
<figure id="fig: 55 tessellation">
<img src="55_tessellation.png" />
<figcaption><span class="math inline">{5,5}</span> tessellation.</figcaption>
</figure>
<figcaption>Hyperbolic tilings. </figcaption>
</figure>

[^1]: Being a geometric point on a curve is a priori not an interesting statement unless we know the corresponding map is regular, as we have in this case.
