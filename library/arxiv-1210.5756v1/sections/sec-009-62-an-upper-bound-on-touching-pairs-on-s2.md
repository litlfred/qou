---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-009-62-an-upper-bound-on-touching-pairs-on-s2
section_title: "An upper bound on touching pairs on S2"
section_number: 6.2
pages: 16-16
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.974
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Our goal is to show that the number of touching pairs in an arbitrary packing of spherical caps of angular radius $\pi/6$ on $\mathbb{S}^2$ is at most $25$. The proof presented here is indirect and it is based on the previous section. The details are as follows.

Let $X=\{\mathbf{x}_{1},...,\mathbf{x}_{N}\}$ be a point set on $\mathbb{S}^2$ with $N \leq 12$ and minimum spherical distance $\pi/3$ between any two points in $X$. Taking the Delaunay triangulation $\mathcal{D}_{X}$ of $X$ on $\mathbb{S}^2$, we let $f$ be the number of faces, $e$ be the number of edges, and $N$ be the number of vertices. Since $\mathcal{D}_{X}$ is a triangulation of $X$ on $\mathbb{S}^2$, every face is a triangle, and so $e=\frac{3}{2}f$. Moreover, just as in the previous section, Euler's formula implies that $f=2N-4$.

Now, assume to the contrary that there exist at least $26$ touching pairs in a packing of $N$ spherical caps of angular radius $\pi/6$ on $\mathbb{S}^2$ with the center points forming $X$ and with $N\le 12$. Then $e=3(N-2)\ge 26$ implies that either $N=12$ or $N=11$.

If $N=12$, then $f=20$ and $e=30$. Hence, the indirect assumption implies that the number of edges of length $>\frac{\pi}{3}$ of $\mathcal{D}_{X}$ is at most $4$ and so, there are at most $8$ irregular triangles in $\mathcal{D}_{X}$. (Here an irregular triangle of $\mathcal{D}_{X}$ means a triangle of $\mathbb{S}^2$ different from the one having side lengths equal to $\frac{\pi}{3}$.) Thus, one can repeat the proof of the previous section under the case $N=12$ leading to a contradiction.

Finally, if $N=11$, then $f=18$ and $e=27$. Hence, the indirect assumption implies that the number of edges of length $>\frac{\pi}{3}$ of $\mathcal{D}_{X}$ is at most $1$ and so, there are at most $2$ irregular triangles in $\mathcal{D}_{X}$. (Here again an irregular triangle of $\mathcal{D}_{X}$ means a triangle of $\mathbb{S}^2$ different from the one having side lengths equal to $\frac{\pi}{3}$.) Thus, one can repeat the proof of the previous section under the case $N=11$ leading to a contradiction.

This finishes our indirect proof on the number of touching pairs in Theorem [\[spherical-main-theorem\]](#spherical-main-theorem){reference-type="ref" reference="spherical-main-theorem"}.
