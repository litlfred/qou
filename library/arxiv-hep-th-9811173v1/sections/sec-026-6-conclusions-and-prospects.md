---
doc_id: arxiv-hep-th-9811173v1
doc_title: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links"
section_id: sec-026-6-conclusions-and-prospects
section_title: "Conclusions and prospects"
section_number: 6
pages: 26-27
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.988
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are rationally related to"
---
Perhaps more than in any other piece of research which either author has undertaken, this work has been vitally enabled by the internet. It provided us with the opportunity to blend number theory, topology, geometry, analysis, physics and computer science, in a global empirical mixing bowl, thanks to:

-   ready access to significant data at Bordeaux, Claremont CA, Florham Park NJ, Knoxville TN, Melbourne, Minneapolis MN, as detailed in footnotes;

-   the ability to run high-level packages, such as Maple, Pari and Reduce, on whatever machine best served our purposes, irrespective of the contingencies of our personal geographic co-ordinates;

-   wonderful specialized resources, downloadable as per our footnotes, namely: David Bailey's superb PSLQ and FFT routines, Oliver Goodman's port of high-precision Snap to DigitalUnix, and Al Manoharan's attractive adaptation to Windows95 of Jeff Weeks' amazing SnapPea program, all supported by generous email advice;

-   access to powerful computers in England, Newfoundland[^1] and Vancouver, yielding high-precision results such as those in ([\[50dp\]](#50dp){reference-type="ref" reference="50dp"}) and ([\[C\]](#C){reference-type="ref" reference="C"}), and the 1800-digit hyperbolic volumes of Tables 20 and 21, achieved by dedicated multiple-precision [@TRANSMP] code, after exploratory work enabled by the above.

The facility with which we were able to plug into all these valuable resources advertises how rich the opportunities for empirical mathematics are becoming. The tools came together to offer more patterns than we had dared to hope for. Enterprises such as we have limned promise to be more and more a part of mathematical and physical research in the next few decades.

That said, many of the results which we have exhibited remain tantalizingly far from proof, let alone understanding. Here we repeat 4 of many remaining puzzles:

-   How might one begin to derive relations such as ([\[modern\]](#modern){reference-type="ref" reference="modern"}), between dilogarithms with arguments in radically different number fields?

-   Why do 1-loop Feynman diagrams, at very specific values of the Mandelstam variables, generate even more relations than we were able to reify by quadratic links?

-   Why do Feynman diagrams, with 7, 8 and 11 loops, lead to 5 Dedekind-zeta knots, at 10, 12 and 18 crossings, with odds of a chance association being at least $10^5:1$ against?

-   Can the mere dilogarithms of 3-dimensional hyperbolic geometric tell us anything about the unidentified 10th-order polylogarithms of 7-loop quantum field theory?

When faced by such visible expansion of one's lack of wisdom, it is probably best to concentrate on that which is easiest to state. Hence we conclude with a rewriting of the simplest unproven relation ([\[modern\]](#modern){reference-type="ref" reference="modern"}) in terms of the Dirichlet series ([\[chi\]](#chi){reference-type="ref" reference="chi"}). From light-by-light scattering at $s=t=7$, and -- just as mysteriously -- from the hyperbolic volume of the link $6^3_1$, we infer that $$\begin{aligned}
&&\sum_{n>0}\left\{
 3\left(-\frac34+\frac{\sqrt{-7}}{4}\right)^n
-3\left(-\frac34+\frac{\sqrt{-7}}{4}\right)^{2n}
 +\left(-\frac34+\frac{\sqrt{-7}}{4}\right)^{3n}\right\}\frac{1}{n^2}
\nonumber\\
&&\qquad\qquad{}=13\,\zeta(2)-6\,\pi \,\arctan\sqrt {7}
+\frac{7\sqrt{-7}}{4}
\sum_{n>0}\left(\frac{n}{7}\right)\frac{1}{n^2}
\label{finis}
\end{aligned}$$ The real part of this empirical and indubitable equality is easily proven; in its imaginary part, with the Jacobi symbol $\left(\frac{n}{7}\right)$, resides a flinty kernel which is -- to us at least -- intractable. A proof of ([\[finis\]](#finis){reference-type="ref" reference="finis"}) and the other quadratic identities would be most welcome.

[^1]: ` http://www.cecm.sfu.ca/`$\,
    \widetilde{}\,$`jborwein/PUP_report_March15/report.html`
