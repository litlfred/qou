---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-007-32-vertices-and-face-centres
section_title: "Vertices and Face-Centres"
section_number: 3.2
pages: 17-18
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.911
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
Using Figure 2 of [@Braden2012] we are able to link the Petrie polygon to the R&R model of the curve, and this gives us a concrete expression for the remaining geometric points.

::: prop
[]{#FCprop label="FCprop"} The face-centres are exactly the points fixed by an order-5 automorphism of the curve. They are given in the $\mathbb{P}^4$-model by the permutations of $[1:\zeta:\zeta^2:\zeta^3:\zeta^4]$. The corresponding points in the HC-model are the desingularizations of $V_k$, together with $a$, $b$, $c$, $d$, and

1.  $[-2\zeta^3 - 2\zeta^2 : \zeta^3 + \zeta^2 - 1 : 1] = [\sqrt{5}+1 : -\sqrt{5}/2-3/2 : 1] = [2j : j^\prime-2: 1]$,

2.  $[-2\zeta^3 - 2 : -2\zeta^3 - \zeta - 1 : 1]$,

3.  $[-2\zeta^2 - 2\zeta : -\zeta^3 + \zeta + 1 : 1]$,

4.  $[2\zeta^3 + 2\zeta^2 + 2\zeta : \zeta^3 + 2\zeta^2 + 2\zeta + 1 : 1]$,

5.  $[-2\zeta^2 - 2 : \zeta^3 - \zeta^2 + \zeta : 1]$,

6.  $[2\zeta^3 + 2\zeta + 2 : \zeta^2 - \zeta + 1 : 1]$,

7.  $[-2\zeta^3 - 2\zeta : 2\zeta^3 + \zeta^2 + \zeta + 2 : 1]$

8.  $[2\zeta^3 + 2\zeta^2 + 2 : -\zeta^3 - \zeta^2 - 2 : 1] = [-\sqrt{5}+1 : \sqrt{5}/2-3/2:1] = [2j^\prime : j-2 : 1]$,

9.  $[2\zeta^2 + 2\zeta + 2 : -\zeta^3 - 2\zeta^2 - \zeta : 1]$,

10. $[-2\zeta - 2 : -\zeta^2 - 2\zeta - 1 : 1]$,

where $j, j^\prime$ are the roots identified by Dye mentioned in §[\[subsec: automorphism group\]](#subsec: automorphism group){reference-type="ref" reference="subsec: automorphism group"}.
:::

::: proof
*Proof.* Certainly the order-5 rotation about a face-centre fixes that centre, and so a Riemann-Hurwitz counting argument gives us that the $24$ face-centres are the fixed points of order-5 automorphisms. It is a simple matter of computation to verify the given expressions are fixed; this may be done in Sage. ◻
:::

The Galois group $\operatorname{Gal}(\mathbb{Q}[\zeta]/\mathbb{Q}) \cong C_4$ acts element-wise on the face-centres and the orbits partition the set of face-centres into 6 sets of 4. Each set of 4 face-centres form the vertices of a quadrilateral whose edges lie in $\left\{ H_2=0 \right\}$ [@Edge1978]. Moreover, the faces of the dodecadodecahedron corresponding to the face-centres in each quadrilateral are parallel.

We have a similar result for the vertices.

::: prop
[]{#Vprop label="Vprop"} The vertices are exactly the points fixed by an order-4 automorphism of the curve. They are given in the $\mathbb{P}^4$-model by the permutations of $[1: i: -1: -i: 0]$.
:::

We could use our birational map as above to give the vertices in HC coordinates, but these are not very illuminating. For example, that vertex $[1:i:-1:-i:0]$ maps to $$[X : Y : Z] = [(3\zeta^3 - \zeta^2 + 2\zeta + 1)i + 3\zeta^3 + 3\zeta^2 + 5 : (2\zeta^3 + 2\zeta + 1)i + 2\zeta^3 + 2\zeta^2 + 2 : 1]$$ though $[1:-1:i:-i:0]$ maps to $[1: (-1+i)/2: (-1+i)/2]$.
