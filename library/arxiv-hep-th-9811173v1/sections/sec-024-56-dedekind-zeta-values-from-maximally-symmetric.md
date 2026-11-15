---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-024-56-dedekind-zeta-values-from-maximally-symmetric
section_title: "Dedekind zeta values from maximally symmetric knots"
section_number: 5.6
pages: 23-25
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.992
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
Jim Hoste, Morwen Thistlethwaite and Jeff Weeks (hereafter HTW) have recently completed an impressive symmetry analysis [@HTW] of all 1,701,936 prime knots with up to 16 crossings. From the University of Tennessee at Knoxville, we obtained files[^1] that identify highly symmetric alternating and non-alternating knots at crossing numbers from 11 to 16. Before analyzing the most symmetric of these, we comment on the situation up to 10 crossings, in territory charted by Dale Rolfsen [@Rolfsen] and predecessors.

Table 23 gives the hyperbolic alternating and non-alternating[^2] knots of maximal symmetry at crossing numbers from 4 to 10, together with the symmetry groups, invariant trace fields, signatures and discriminants of their complementary manifolds. Where the field has a single complex place (i.e. signature $[n-2,1]$ at degree $n$) we give the rational Dedekind-zeta invariant, $a/b$. Table 24 shows our remaining finds of Dedekind-zeta invariants, for knots up to 10 crossings. The latter are likely to be complete up to 9 crossings; at 10 crossings we analyzed all non-alternating knots, but only about 20% of the alternating knots.

Some comments are in order.

1.  Up to 9 crossings, maximal symmetry is a good -- yet far from infallible -- diagnostic of a single-complex-place field.

2.  The maximally symmetric knots designated by Rolfsen [@Rolfsen] as $6_3$, $7_7$, $8_{21}$, $9_{40}$ and $10_{123}$ have invariant trace fields with more than one complex place.

3.  In ([\[8_21\]](#8_21){reference-type="ref" reference="8_21"}) it is shown that the volume of $8_{21}$ reduces to a pair of Dedekind zeta values.

4.  In ([\[10_123\]](#10_123){reference-type="ref" reference="10_123"}) it is shown that the volume of $10_{123}$ reduces to that of a simple orthoscheme.

5.  Only one Dedekind-zeta knot, namely $9_{49}$, escapes the sieve of maximal symmetry up to 9 crossings. Moreover, ([\[5_2\]](#5_2){reference-type="ref" reference="5_2"}) shows that it yields a Dedekind zeta value already encountered at fewer crossings.

6.  At 10 crossings, we found 3 non-alternating Dedekind-zeta knots with less than maximal symmetry: the Feynman [@BKP; @BK15] pair, $10_{139}$ and $10_{152}$, with the modest symmetries $D_2$ and $Z_2$, and $10_{153}$, which SnapPea declared to be devoid of symmetry.

In the light of the above, we were prepared for a dwindling yield from maximal symmetry, above 10 crossings. The harvest proved to be even more meagre than we anticipated. Table 25 shows that *none* of the 11 maximally -- and visibly [@HTW] -- symmetric alternating knots from 11 to 16 crossings has a single-complex-place invariant trace field. From the 10 maximally -- and covertly [@HTW] -- symmetric non-alternating knots, we obtained 4 single-complex-place fields, yet only one of these entailed a new Dedekind zeta value, namely $$Z_{643,4}=\df15\times{\rm vol}({\rm n}14.13191)\label{643,4}$$ while those in $$\begin{aligned}
Z_{44,3}&=&\df14\,\times{\rm vol}({\rm n}12.642)\label{44,3}\\
Z_{448,4}&=&\df{1}{10}\times{\rm vol}({\rm n}15.112310)\label{448,4}\\
Z_{31,3}&=&\df{1}{15}\times{\rm vol}({\rm n}16.1007813)\label{31,3}
\end{aligned}$$ had already been obtained in ([\[9_48\]](#9_48){reference-type="ref" reference="9_48"},[\[8_18\]](#8_18){reference-type="ref" reference="8_18"},[\[10_157\]](#10_157){reference-type="ref" reference="10_157"}). The last of these duplicates merits further comment.

There are more [@HTW] than a million non-alternating hyperbolic 16-crossing knots. Amid this plethora, HTW identified the 1,007,813th (in their lexicographic ordering of Dowker codes) as uniquely maximally symmetric. It enjoys the 18-fold dihedral symmetry group $D_9$ of the nonagon, exquisitely disguised in any 16-crossing projection. If the reader has access to SnapPea, s/he should certainly not miss the opportunity to click in a depiction of the non-alternating knot in Fig. 7 of the highly readable article[^3] by HTW. Then the power of Jeff Weeks' topological engine [@SnapPea] becomes apparent, when its symmetry analyzer announces $D_9$. Morwen Thistlethwaite's website[^4] renders this more visible, by resort to a 5-braid presentation.

Intuition told us to expect a Dedekind zeta value from the HTW knot with symmetry group $D_9$. In this respect, we were not disappointed: the volume of the knot is $15\,Z_{31,3}$, giving a Dedekind-zeta invariant $a/b=1/15$ that is smaller than any we had previously encountered. We allayed the disappointment, at having already encountered $Z_{31,3}$, by the following *ex post facto* considerations. The $D_9$ knot is so special that it merits a simple invariant trace field. The quadratic field ${\bf Q}(\sqrt{-3})$ was taken by the figure-8 knot, in ([\[4_1\]](#4_1){reference-type="ref" reference="4_1"}). The cubic field with $D=-23$ had already been engaged by Feynman, at 12 crossings, in ([\[12A\]](#12A){reference-type="ref" reference="12A"}). The next cubic discriminant, $D=-31$, provides an eminently suitable resting place for the Hoste--Thistlethwaite--Weeks $D_9$ knot. Colleagues engaged on commensurability [@CGHN] analyses may now investigate the wondrously long chain $$\begin{aligned}
Z_{31,3}
&=&\df{1}{15}\times{\rm vol}({\rm n}16.1007813)\label{1/15}\\
&=&\df18\,\times{\rm vol}(10_{157})\label{1/8}\\
&=&\df14\,\times{\rm vol}({\rm v}3183)\label{1/4}\\
&=&\df13\,\times{\rm vol}(7^2_1)\label{1/3}\\
&=&\df12\,\times{\rm vol}({\rm m}034)\label{1/2}\\
&=&1\,\,\times{\rm vol}({\rm m}007(+4,1))\label{1/1}\\
&=&\df23\,\times{\rm vol}({\rm m}149(+1,2))\label{2/3}\\
&=&\df27\,\times{\rm vol}({\rm v}1963)\label{2/7}
\end{aligned}$$ of distinct rational Dedekind-zeta invariants from a common invariant trace field. The last 6 invariants cover 43 census manifolds. The volumes of the $D_9$ knot and $10_{157}$ are $30\,D(z)$ and $16\,D(z)$, where $z^3=1-z$, with $\Im z>0$, and $D(z)=\frac12Z_{31,3}$ is the volume of any one of the 4 ideal tetrahedra that triangulate ${\rm m}034$. Here, as in the Feynman case ([\[12A\]](#12A){reference-type="ref" reference="12A"}), the Dedekind zeta value collapses to a rational multiple of a single Bloch--Wigner dilogarithm.

[^1]: ` http://www.math.utk.edu/`$\,\widetilde{}\,$`morwen/knotscape.html`

[^2]: Below 8 crossings, all hyperbolic knots are alternating.

[^3]: ` http://www.pitzer.edu/`$\,\widetilde{}\,$`jhoste` also gives access to [@HTW].

[^4]: ` http://www.math.utk.edu/`$\,\widetilde{}\,$`morwen/d9.html`
