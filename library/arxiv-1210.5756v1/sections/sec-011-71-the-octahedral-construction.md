---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-011-71-the-octahedral-construction
section_title: "The Octahedral Construction"
section_number: 7.1
pages: 16-18
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.752
latex_coverage_ratio: 1.0
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
We now consider an explicit construction of a unit sphere packing placed over the face-centered cubic lattice for which we obtain a high number of touching triplets and quadruples of unit balls in $\mathbb{E}^3$. For any positive integer $k \geq 2$, place $n(k)=\frac{2k^{3}+k}{3}$ lattice points of the face-centered cubic lattice such that their convex hull is a regular octahedron $\mathbf{K} \subset \mathbb{E}^3$ of edge length $2(k-1)$ having exactly $k$ lattice points along each of its edges (see Figure [1](#fig:OctahedralConstruction){reference-type="ref" reference="fig:OctahedralConstruction"} for $k=4$).

<figure id="fig:OctahedralConstruction">
<div class="center">
<img src="OctahedralConstruction4" />
</div>
<figcaption>The Octahedral Construction for <span class="math inline"><em>k</em> = 4</span>.</figcaption>
</figure>

It is not hard to see via layer by layer cross-sections that the number of regular tetrahedra of edge length 2 spanned by the lattice points in $\mathbf{K}$ is equal to $$2\sum\limits_{i=2}^{k-1} 2i(i-1) = \frac{4(k-2)(k-1)k}{3}\ .$$ This means that we can pack $n(k)=\frac{2k^{3}+k}{3}$ unit balls forming an octahedral shape in $\mathbb{E}^3$ such that there are exactly $N_{4}(k)=\frac{4(k-2)(k-1)k}{3}$ touching quadruples. We note that $\frac{3}{2}n(k) > k^{3}$ implies $\left(\frac{3}{2}\right)^{2/3}n^{2/3}(k) > k^2$, and observe that $n(k) < k^{3}$ implies $n^{1/3}(k) < k$. With these bounds, we can bound $N_{4}(k)$ in terms of $n$. $$N_{4}(k)=\frac{4(k-2)(k-1)k}{3}=2\Big(\underbrace{\frac{2}{3}k^{3}+\frac{1}{3}k}_{\text{n(k)}}\Big) - 4k^{2} + 2k > 2n(k) - 4\left(\frac{3}{2}\right)^{2/3}n^{2/3}(k) + 2n^{1/3}(k)\ ,$$ finishing the proof of $(iii)$ in Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} on touching quadruples.

We have seen that the number of regular tetrahedra of edge length 2 in the above mentioned Octahedral Construction is equal to $N_{4}(k)$; we now consider the number of regular triangles of side length $2$ spanned by the lattice points in $\mathbf{K}$ and label it by $N_{3}(k)$. We note that the volume of an octahedron of edge length $2$ is $\frac{8\sqrt{2}}{3}$ moreover, the volume of a tetrahedron of edge length $2$ is $\frac{\sqrt{8}}{3}$. Furthermore, the volume of $\mathbf{K}$ is equal to $\frac{8\sqrt{2}}{3}(k-1)^{3}$. Thus, the number of octahedra of edge length 2 in the Octahedral Construction is equal to, $$\frac{\frac{8\sqrt{2}}{3}(k-1)^{3}-\frac{4(k-2)(k-1)k}{3}\frac{\sqrt{8}}{3}}{\frac{8\sqrt{2}}{3}}=(k-1)^{3}-\frac{(k-2)(k-1)k}{3}$$ We also note that the number of regular triangles of side length 2 of the regular triangle of side length $2(k-1)$, which is the face of $\mathbf{K}$, is equal to $(k-1)^{2}$. Hence, the number of regular triangle faces of side length 2 (i.e., touching triplets) in the Octahedral Construction is,

$$N_{3}(k) = \frac{1}{2} \left(4N_{4}(k) + 8((k-1)^{3}-\frac{(k-2)(k-1)k}{3}(k))+8(k-1)^{2})\right)= \frac{4}{3}(k-1)k(4k-5)\ .$$ Using the bounds introduced before the preceding remark, we can now bound $N_{3}(k)$ in terms of $n$. $$N_{3}(k) = \frac{4}{3}(k-1)k(4k-5) = 8\Big(\underbrace{\frac{2}{3}k^{3}+\frac{1}{3}k}_{\text{n(k)}}\Big) -12k^{2} + 4k > 8n(k) - 12\left(\frac{3}{2}\right)^{2/3}n^{2/3}(k)+4n^{1/3}(k)\ ,$$ finishing the proof of $(iii)$ in Theorem [\[main-theorem\]](#main-theorem){reference-type="ref" reference="main-theorem"} on touching triplets.

## Tightness of the estimates in Problem [\[main-conjecture\]](#main-conjecture){reference-type="ref" reference="main-conjecture"}

We need to construct the corresponding polar coordinates for $12$ points on $\mathbb{S}^2$ with minimum spherical distance $\pi/3$ spanning $10$ regular triangles of side length $\pi/3$. By taking the points with the following polar coordinates, we can construct such a point set $P$ as seen in Figure [2](#fig:10tetrahedra){reference-type="ref" reference="fig:10tetrahedra"}:

::: center
Table 6. Polar coordinates of the points in $P$

::: center
                                 Polar Coordinates
  ---------- ---------------------------------------------------------
   $v_{1}$                       $\Big(1,0,0\Big)$
   $v_{2}$                     $\Big(1,\pi/3,0\Big)$
   $v_{3}$               $\Big(1,\pi/3,\arccos(1/3)\Big)$
   $v_{4}$               $\Big(1,\pi/3,2\arccos(1/3)\Big)$
   $v_{5}$               $\Big(1,\pi/3,3\arccos(1/3)\Big)$
   $v_{6}$               $\Big(1,\pi/3,4\arccos(1/3)\Big)$
   $v_{7}$      $\Big(1,\arccos(-7/18),-\arctan(2\sqrt{2}/5)\Big)$
   $v_{8}$        $\Big(1,2\arctan(\sqrt{2}),\arccos(1/3)/2\Big)$
   $v_{9}$    $\Big(1,\arccos(-7/18),\pi-\arctan(34\sqrt{2}/19)\Big)$
   $v_{10}$      $\Big(1,2\arctan(\sqrt{2}),5\arccos(1/3)/2\Big)$
   $v_{11}$      $\Big(1,2\arctan(\sqrt{2}),7\arccos(1/3)/2\Big)$
   $v_{12}$     $\Big(1,\arccos(-53/54),\arctan(4\sqrt{2}/17\Big)$
:::
:::

<figure id="fig:10tetrahedra">
<div class="center">
<img src="10tetrahedra" />
</div>
<figcaption>An explicit construction of 10 tetrahedra sharing a vertex.</figcaption>
</figure>

Last but not least, we need to generate $12$ points on $\mathbb{S}^2$ with minimum spherical distance $\pi/3$ having $24$ spherical line segments of length $\pi/3$ spanned by the $12$ points. If we place our points at the vertices of a cubeoctahedron with diameter $2$, then we satisfy these conditions.
