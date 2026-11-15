---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-006-32-branched-covers-of-p1
section_title: "Branched covers of P1"
section_number: 3.2
pages: 4-5
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.627
latex_coverage_ratio: 0.957
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section3.2 label="section3.2"}

We now consider the curve ([\[craig\]](#craig){reference-type="ref" reference="craig"}) as a branched cover of $\mathbb{P}^1$ with $x$ as the coordinate. The affine part of the HC curve is obtained by setting $z=1$ in [\[craig\]](#craig){reference-type="eqref" reference="craig"} yielding $$\label{craigp1}
  x y^5 + x + x^2 y^2 - x^4 y - 2 y^3 = 0.$$ There are 5 sheets above the generic $x$, with branch points at $0,
\infty$ and $$\left\{ \frac{\zeta^k}{4}
    \big(1674\pm 870\mathrm{i}\sqrt{15}\big)^{1/5}
    : \;  k \in \{0,\dots,4\}
  \right\}.$$ There is also a double solution at $x=\zeta^k$ but these are precisely the singular points similar to $[1,1,1]$ we investigated before and after resolution the cover is regular there.

At $x=0$ we have two preimages, one corresponding to $[0,0,1]$ with an expansion $$\label{eq:x0exp1}
  y = \frac{1}{2^{1/3}} x^{1/3} + \cdots,$$ where three sheets come together, and the other corresponding to $[0,1,0]$ with expansion $$\label{eq:x0exp2}
  y = \sqrt{2} x^{-1/2} + \cdots$$ where two sheets come together. Similarly at $x=\infty$ we have two preimages after desingularisation: $[1,0,0]_1$ where from $[1,t^4,t]\equiv [t\sp{-1},t\sp{3},1]$ and $y\approx x\sp{-3}$; and $[1,0,0]_2$ where from $[1,t,t^4]\equiv [t\sp{-4},t\sp{-3},1]$ and $y\approx x\sp{3/4}$. The other 10 branch points correspond to the solutions of $256 x^{10}-837 x^5+3456=0$ and have two sheets coming together at each[^1].

[^1]: We remark that the Maple command `monodromy`$(x y^5 + x + x^2 y^2 - x^4 y - 2 y^3,x,y,$`showpaths``)` will produce the monodromy data for the HK curve, together with the paths and sheet numbering necessary to make sense of this data. The branch point $0$ has monodromy $[1,2][3,4,5]$ while that of $\infty$ is $[1,4,5,2]$; these are the cycle structures described above. The remaining ten branch points arranged with increasing argument have monodromies $[1,4]$, $[2,4]$, $[2,5]$, $[1,5]$, $[1,3]$, $[2,3]$,$[2,4]$, $[1,4]$, $[1,5]$ respectively, here indicating the two sheets that come together.
