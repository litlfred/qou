---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-020-63-interpreting-flip-moves-using-23-moves
section_title: "Interpreting flip moves using 2–3 moves"
section_number: 6.3
pages: 39-41
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.911
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
In order to carry out step ([\[retriangulate step 1\]](#retriangulate step 1){reference-type="ref" reference="retriangulate step 1"}) of our plan in Remark [\[retriangulate strategy\]](#retriangulate strategy){reference-type="ref" reference="retriangulate strategy"}, we will interpret the flip moves in terms of the 2--3 and 3--2 moves allowed in Theorem [\[thm.00\]](#thm.00){reference-type="ref" reference="thm.00"}.

1.  First, consider a 2--3 flip in one polyhedron. This is simply a 2--3 move. Since the triangulations on either side of the move are in $\mathcal X_M^{\mathrm{EP}}$, they are both 1--efficient by Remark [\[Xbar\^EP 1-efficient\]](#Xbar^EP 1-efficient){reference-type="ref" reference="Xbar^EP 1-efficient"}. Therefore the triangulations have the same index by Theorem [\[thm.00\]](#thm.00){reference-type="ref" reference="thm.00"}.

2.  Second, consider an external 2--2 flip. See Figure [\[2-2move_external\]](#2-2move_external){reference-type="ref" reference="2-2move_external"}. The base of the pyramid is on a face of the polyhedron that is glued to a polygonal pillow. The two triangles on the base of the pyramid are glued to either a single tetrahedron in the pillow, or two tetrahedra in either the polygonal pillow or the polyhedron on the other side of the polygonal pillow.

    -   If the two triangles are glued to a single tetrahedron then we are in the situation shown in the top diagram of Figure [\[2-2move_external\]](#2-2move_external){reference-type="ref" reference="2-2move_external"}, and we can perform a 3--2 move, which performs the flip to the polyhedron, and removes the single tetrahedron from the layered triangulation of the polygonal pillow.

    -   Otherwise, we perform a 2--3 move, which performs the flip to the polyhedron, and adds a flat tetrahedron to the layered triangulation of the polygonal pillow. (Note that we could use only this move, even in the previous case; the difference between the two options is a 0--2 move.)

    Once again, the triangulations on either side of the move are in $\mathcal X_M^{\mathrm{EP}}$, so they are both 1--efficient and the triangulations have the same index.

3.  Lastly, consider an internal 2--2 flip. See Figure [\[2-2move_internal\]](#2-2move_internal){reference-type="ref" reference="2-2move_internal"}. We can perform a 2--3 move followed by a 3--2 move, which together perform the flip. Since the four vertices in the circuit are coplanar, at the intermediate step we introduce a flat tetrahedron. The intermediate triangulation is not in $\mathcal X_M^{\mathrm{EP}}$, since it includes a flat tetrahedron in a polyhedron, and so the polyhedron does not have a regular triangulation. However, the intermediate triangulation still has a natural semi--angle structure in the obvious way, and so it is 1--efficient, and again the three triangulations involved all have the same index.

<figure id="2-2 moves">

<figcaption>The possible 2–2 moves on a triangulation of a point configuration, realised using 2–3 and 3–2 moves. Again in each case, vertices <span class="math inline"><em>v</em><sub>1</sub></span> through <span class="math inline"><em>v</em><sub>4</sub></span> are coplanar.</figcaption>
</figure>

The arguments so far show that we can achieve step ([\[retriangulate step 1\]](#retriangulate step 1){reference-type="ref" reference="retriangulate step 1"}) of Remark [\[retriangulate strategy\]](#retriangulate strategy){reference-type="ref" reference="retriangulate strategy"}. Now we need to deal with step ([\[retriangulate step 2\]](#retriangulate step 2){reference-type="ref" reference="retriangulate step 2"}).
