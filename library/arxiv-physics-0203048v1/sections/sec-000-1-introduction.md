---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic fields"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 0.923
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magnetic ﬁelds is presented."
---
The topological structure of magnetic fields is an important subject in plasma physics. There, among other issues, it is related to the problem of stability of a plasma and to its energy content. Fields with an enormous wealth of entangled, braided or knotted field lines exist for example in the solar atmosphere. Note that the topological complexity of these solar magnetic fields is only revealed, if first, one takes into account that the observed loops anchored in the photosphere are closed by subphotospheric fields, and second, that already simple toroidal equilibria contain many different knotted and linked field lines. The simplest examples are the so called torus knots, which are formed by field lines where the quotient of the number of windings around the core and the torus axis is rational.

In general, magnetic fields in plasmas are not static, but evolve due to the motion of the plasma. The evolution of solar as well as most astrophysical magnetic fields is given in good approximation by the induction equation of ideal magnetohydrodynamics (IMHD) $$\frac{\partial }{\partial t} {\bf B} 
        - \nabla \times ({\bf v} \times {\bf B})  = 0,
        \label{idindeq}$$ which shows that the field can be considered as frozen-in with respect to the plasma velocity ${\bf v}$. The approximation of IMHD which leads to this law is valid as long as the evolution does not lead to small scale structures, e.g. thin current sheets.

The ideal induction equation guarantees the conservation of the topology of field lines under the flow of ${\bf v}$, i.e. every linkage or knottedness of magnetic flux is preserved. Mathematically speaking, the flow of ${\bf v}$ is a differentiable isotopy of the space under consideration. It maps the field lines of ${\bf B}$ at time $t_0$ to a topologically equivalent set of field lines for any later time $t> t_0$. Let us note that, following the usual terminology in plasma physics, the term 'topological equivalent' is used here in the sense of a diffeomorphic isotopy.

<figure id="Whitehead">
<div class="center">
<p><embed src="ghcmfig1.eps" style="width:4cm" /> <embed src="ghcmfig2.eps" style="width:5cm" /></p>
</div>
<figcaption>The Borromean rings (left) and the Whitehead link (right).</figcaption>
</figure>

In order to describe the structure of magnetic fields, it is desirable to have measures of complexity. These measures should be topological, i.e. they should be invariant under an arbitrary isotopy of the magnetic field, and therefore invariant under the ideal induction equation. An example of a topological measure for magnetic fields is the magnetic helicity, a quantity which has attracted a great deal of attention in recent years (see e.g. Brown ). Magnetic helicity, which measures the linkage of magnetic flux, is only a lowest order topological measure. It fails for instance to detect the interlocking of magnetic flux tubes in form of the Borromean rings or the Whitehead link (see Figure [\[borro\]](#borro){reference-type="ref" reference="borro"}). The total magnetic helicity of these configurations vanishes just as it does for three or two unlinked flux tubes. Both configurations must possess a higher order linkage or knottedness of magnetic flux which is not detected by magnetic helicity. This naturally raises the question whether corresponding higher order measures similar to magnetic helicity exist which are sensitive to these linkages. Here we would like to remark that the configurations shown in Figure [\[borro\]](#borro){reference-type="ref" reference="borro"} are highly idealized. In any real plasma we would not find this pure linkage but a mixture of different types of linkages, each of which is to be measured by a different integral.

In knot theory different invariants are known which distinguish e.g. the Borromean rings or the Whitehead link from unlinked rings. The problem is that invariants used in physical applications, e.g. in magnetohydrodynamics, should be expressed in terms of observable quantities, in our setting in terms of the magnetic field $\bB$. Up to now only the helicity, which is related to the Gauß  linking number, has been formulated as an invariant for magnetic fields in a satisfactory manner. As was recognized first by Monastyrsky and Sasorov (1987) and independently by Berger (1990) and Evans and Berger (1992), the link invariants based on so-called higher Massey products (see Massey 1958, 1969, Kraines 1966, Fenn 1983) can be written as invariants applicable to magnetic flux tubes. Similar to helicity, they only involve the magnetic fields and can be expressed as volume integrals over the space in consideration. Their disadvantage is that their usage is restricted to magnetic fields confined to isolated flux tubes. In addition, these flux tubes must not possess a linkage lower than the linkage which is measured.

In this paper we present a generalized third-order invariant for three magnetic fields not confined to isolated flux tubes. In the case of isolated flux tubes this invariant coincides with the invariant known from the Massey triple product. Using gauge fields in the context of an $SU(2)$ symmetry, the generalized invariant can be shown to originate from the same equation as helicity. Therefore, we will first recapitulate some basic facts about magnetic helicity before we turn to our main subject, the third-order link invariant.
