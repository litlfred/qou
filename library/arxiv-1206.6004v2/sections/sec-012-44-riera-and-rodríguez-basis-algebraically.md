---
doc_id: arxiv-1206.6004v2
doc_title: "Symmetry, Integrability and Geometry: Methods and Applications"
section_id: sec-012-44-riera-and-rodríguez-basis-algebraically
section_title: "Riera and Rodríguez basis algebraically"
section_number: 4.4
pages: 12-15
source_pdf: 1206.6004v2.pdf
source_sha256: b490672c8c3557dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.976
doc_brief: "Bring's Curve: its Period Matrix and the Vector of Riemann Constants — Bring’s curve is the genus 4 Riemann surface with automorphism group of maximal size, S5."
duplicate_of: "sigma12-065"
---
[]{#section4.4 label="section4.4"}

We are now in a position to express the Riera and Rodrı́guez basis on this branched cover. Recall that $$\alpha_i = (2i-1) + (2i)$$ as a prescription on which edges to traverse in the hyperbolic model.

This becomes a specification to look up the relevant edges in Table [\[tab:hypcraigedges\]](#tab:hypcraigedges){reference-type="ref" reference="tab:hypcraigedges"}, and construct a path that has its main component in the specified regions (circling $x=0$ and outside all finite branch points enough times to reach the correct sheets). In fact, just like Riera and Rodrı́guez we only need to construct $\alpha_1$ and $\alpha_2$ and then repeatedly apply $(x,y) \mapsto
(\zeta x, \zeta^2 y)$ to obtain the rest.

To be explicit and referring to Table [\[tab:hypcraigedges\]](#tab:hypcraigedges){reference-type="ref" reference="tab:hypcraigedges"}, $\alpha_1$ must go out along $x > 0$ with $y \gg 0$ near 0, loop around infinity until it can come back in to $x=0$ along a ray with $\arg x = \frac{2\pi}{5}$ and $\arg y = \frac{4\pi}{5}$ before looping around 0 until it can join up with the beginning again. A path conforming to this description is shown in Fig. [1](#fig:alpha12){reference-type="ref" reference="fig:alpha12"}.

Similarly $\alpha_2$ goes out along $x > 0$ with $y < 0$, loops and comes back with argument of $x$ as $-2\pi/5$ and argument of $y$ as $6\pi/5$; it is also depicted in Fig. [1](#fig:alpha12){reference-type="ref" reference="fig:alpha12"}.

![$\alpha_1$ and $\alpha_2$ homology cycles for the Hulek--Craig branched cover. Graphs of subsequent $\alpha_i$ are rotations of these by $\frac{2\pi\mathrm{i}}{5}$.](alpha_basis){#fig:alpha12}

Using the software[^1] introduced in [@bn10] with Klein's curve as an illustrative example, we may read these paths into `extcurves` and convert them into a full basis with the commands

    > curve, hom, names := read_pic("homology.pic"):
    > zeta := exp(2*Pi*I/5):
    > trans := (x,y) -> [zeta^3*x,zeta*y]:
    > for i from 1 to 3 do
        hom := [op(hom),
                transform_extpath(curve, hom[-2], trans),
                transform_extpath(curve, hom[-1], trans)];
      od:

An immediate check to this calculation is provided by calculating the intersection matrix of this constructed basis. The command

    > Matrix(8, (i,j) -> isect(curve, hom[i], hom[j]));

produces (with considerably less work and chance of error) precisely the matrix claimed by Riera and Rodrı́guez, namely $$\begin{pmatrix}
    0 & 1 & -1 & 1 & -1 & 0 & 1 & -1 \\
    -1 & 0 & 1 & -1 & 1 & 0 & 0 & 0 \\
    1 & -1 & 0 & 1 & -1 & 1 & -1 & 0 \\
    -1 & 1 & -1 & 0 & 1 & -1 & 1 & 0 \\
    1 & -1 & 1 & -1 & 0 & 1 & -1 & 1 \\
    0 & 0 & -1 & 1 & -1 & 0 & 1 & -1 \\
    -1 & 0 & 1 & -1 & 1 & -1 & 0 & 1 \\
    1 & 0 & 0 & 0 & -1 & 1 & -1 & 0
  \end{pmatrix}.$$

Finally we can calculate the period matrix. This may be done analytically (as in [@riera]) or numerically via the `extcurves` package which calculates the period matrix for any homology basis (implicitly using the Riemann period matrix given by `algcurves[periodmatrix]`). Using the the transformation from [\[basistrans\]](#basistrans){reference-type="eqref" reference="basistrans"} both methods yield

::: theorem
The homology cycles $\alpha_1$ and $\alpha_2$ for the Hulek--Craig branched cover reproduce the cycles of Riera and Rodrı́guez and their corresponding period matrix $$\tau = \tau_0
\begin{pmatrix}
  4  & 1  & -1 & 1  \\
  1  & 4  & 1  & -1 \\
  -1 & 1  & 4  & 1  \\
  1  & -1 & 1  & 4
\end{pmatrix},$$ where $\tau_0$ is defined by [\[deftau0\]](#deftau0){reference-type="eqref" reference="deftau0"}.
:::

We also note that the action on the homology basis $\alpha_{1,\ldots,8}$ associated with the antiinvolution of the real structure is given by $$\mathcal{S}':=\begin{pmatrix} 0&0&0&0&0&0&-1&0\\
0 &0&0&0&0&-1&0&0\\  0&0&0&0&-1&0&0&0
\\  0&0&0&-1&0&0&0&0\\  0&0&-1&0&0&0
&0&0\\  0&-1&0&0&0&0&0&0\\  -1&0&0&0
&0&0&0&0\\  0&1&0&1&0&1&0&1\end{pmatrix}.$$ It is algorithmic to show that $$\mathcal{S}:=T\mathcal{S}' T^{-1}=\begin{pmatrix} 1&0&0&0&1&0&0&0\\
0 &1&0&0&0&1&0&0\\  0&0&1&0&0&0&1&0
\\  0&0&0&1&0&0&0&1\\  0&0&0&0&-1&0&0
&0\\  0&0&0&0&0&-1&0&0\\  0&0&0&0&0&0
&-1&0\\  0&0&0&0&0&0&0&-1\end{pmatrix},$$ where $T$ is the symplectic transformation (with respect to the canonical symplectic form) $$T= \begin{pmatrix} -1&2&1&2&-1&1&0&1
\\  0&1&0&-3&0&0&0&-1\\  -2&1&2&-1&0
&1&0&0\\  0&0&-1&0&-1&0&-1&0\\  2&-2
&-3&-2&0&-1&-1&-1\\  -1&0&1&3&0&1&0&1
\\  1&-1&-1&-2&0&-1&0&-1\\  -1&2&3&2
&0&1&1&1\end{pmatrix}.$$ Here $\mathcal{S}$ is the canonical form for an antiholomorphic involution where there is one nondividing real oval (see for example [@vinnikov]), again showing there is one real oval.

[^1]: Located at <http://gitorious.org/riemanncycles>.
