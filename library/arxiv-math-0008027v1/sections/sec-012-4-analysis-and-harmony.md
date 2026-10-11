---
doc_id: arxiv-math-0008027v1
doc_title: "KASHAEV’S INVARIANT AND THE VOLUME OF A"
section_id: sec-012-4-analysis-and-harmony
section_title: "Analysis, and Harmony"
section_number: 4
pages: 9-9
source_pdf: 0008027v1.pdf
source_sha256: 8bce0b8a1bca372e
doc_brief: "KASHAEV’S INVARIANT AND THE VOLUME OF A — I follow Y."
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.983
---
[]{#sec:harmony label="sec:harmony"} In §[\[sec:algebra\]](#sec:algebra){reference-type="ref" reference="sec:algebra"} we know that if we calculate the Kashaev invariant of the figure-eight knot only the parameter $j$ contributes. Due to Kashaev [@Kashaev:LETMP97], the asymptotic behavior of $\langle 4_1\rangle_N$ for large $N$ is $$\int\exp
  \left[
    \frac{N}{2\pi\sqrt{-1}}
    \left\{
      -\operatorname{Li}_2(z)+\operatorname{Li}_2(z^{-1})
    \right\}
  \right]\,dz,$$ where $\operatorname{Li}_2(z)=-\int_{0}^{z}\log(1-u)/u\,du$ is the dilogarithm function. Note that $z$ corresponds to $q^{j}$ and that $-\operatorname{Li}_2(z)$ and $\operatorname{Li}_2(z^{-1})$ corresponds to $(q)_{j}$ and $(q^{-1})_{j}$ respectively. We can apply the saddle point method to this integral and know that for large $N$ it is approximated by the value $$\exp\left[\frac{N\,V(z_0)}{2\pi\sqrt{-1}}\right]$$ with $V(z):=-\operatorname{Li}_2(z)+\operatorname{Li}_2(z^{-1})$ and $z_0$ satisfies $d\,V(z_0)/d\,z=0$. Since $$\frac{d\,V(z)}{d\,z}=\frac{\log(1-z)}{z}+\frac{\log(1-z^{-1})}{z},$$ $z_0$ satisfies $$\label{eq:saddle}
  z_0^2-z_0+1=0.$$ Now the Kashaev conjecture follows in this case since $V(z_0)$ is the volume of the figure-eight knot complement, which is twice the volume of the regular tetrahedron.

On the other hand in §[\[sec:geometry\]](#sec:geometry){reference-type="ref" reference="sec:geometry"} we know that only two tetrahedra parameterized by $b$ and $d$ survive. Moreover from the cusp condition these two parameters coincide and satisfy the equation $$b^2-b+1=0,$$ which coincides with [\[eq:saddle\]](#eq:saddle){reference-type="eqref" reference="eq:saddle"}! Observe that $-\operatorname{Li}_2(z)$ corresponds to $(q)_{j-1}=N/(q)_{[-j]}$ which comes from the angle between the edges around the second crossing labeled $0$ and $j$, and $\operatorname{Li}_2(z^{-1})$ to $(q^{-1})_{j-1}=N/(q^{-1})_{[-j]}$ which comes from the angle around the fourth crossing between the edges labeled $0$ and $j$.

Yokota proved in [@Yokota:volume] similar situations occur for much more general knots including non-alternating knots, showing that for a fixed knot diagram the angles between the surviving labelings of the summation in $\langle{K}\rangle_N$ correspond to the surviving dihedral angles in the ideal tetrahedron decomposition and that the partial differential equations defining the saddle point of the integral approximating $\langle{K}\rangle_N$ for large $N$ coincide with the hyperbolicity condition. I hope that this note will help the reader to read Yokota's rather complicated but beautiful paper [@Yokota:volume].
