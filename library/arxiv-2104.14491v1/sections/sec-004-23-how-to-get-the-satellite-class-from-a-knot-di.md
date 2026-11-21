---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mos"
section_id: sec-004-23-how-to-get-the-satellite-class-from-a-knot-di
section_title: "How to get the satellite class from a knot diagram"
section_number: 2.3
pages: 5-6
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.718
latex_coverage_ratio: 0.974
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
---
#### The first Reidemeister of the companion and the full twist in the pattern.

The parameter $k$ of the satellite defined by ([\[tor-cab-top\]](#tor-cab-top){reference-type="ref" reference="tor-cab-top"},[\[tw-cab-top\]](#tw-cab-top){reference-type="ref" reference="tw-cab-top"}) is a topological invariant, since it enters in the relations of the topologically invariant quantities. On the other hand, a satellite is often presented with its the planar diagram, e.g., with one in fig.[\[fig:sat\]](#fig:sat){reference-type="ref" reference="fig:sat"}. Then $k$ must be expressed via the number of the half-twists in the pattern, $w$, and the writhe number of the companion knot $\mathcal{K}$, $\nu$. Both these quantities change under the same continuous transformation of the knotted tube, which deletes a crossing with adjacent contractible loop on the knot diagram (the RI transformation [@KnotBook]) and causes a full twist of the tube. The attached two-strand braid gains then two more half-twists of the same orientating as the deleted crossing[^1]  [@KnotBook]. Hence, $2\nu+w=inv$. Only one linear combination of $\nu$ an $w$ must be a topological invariant, since the both numbers would be invariants otherwise. Hence, $k=2\nu+w+c$, for some constant $c$. The form of the Khovanov polynomial as function of the pattern dictates the natural chose of $c=\mathtt{Sh}_{\mathcal{K}}$ given by ([\[ShKn\]](#ShKn){reference-type="ref" reference="ShKn"}) (see sec.[\[sec:PPCD\]](#sec:PPCD){reference-type="ref" reference="sec:PPCD"} for further details).

#### Satellite class in the cabling formula.

The invariance of $k=2\nu+w$ also follows from computation of the HOMFLY polynomial using the knot diagram. E.g., one can take the cabling formulae for torus satellites [@AMcab]. These formulae are originally applied to the renormalised $\check{H}$ polynomials and read $$\begin{aligned}
\check{H}^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}=-q^{w}\check{H}^{\mathcal{K}}_{\mathtt{asm}}+q^{-w}\check{H}^{\mathcal{K}}_{\mathtt{sym}},\label{tor-cab-vert-u}
\end{aligned}$$ Each of the knot polynomials $H$, $H_{\mathtt{asm}}$, $H_{\mathtt{sym}}$ differs from $\check{H}$, $\check{H}_{\mathtt{asm}}$, $\check{H}_{\mathtt{sym}}$, respectively, by the known factor whose power depends on the knot diagram[^2]. The explicit form of the factors is such that ([\[tor-cab-vert-u\]](#tor-cab-vert-u){reference-type="ref" reference="tor-cab-vert-u"}) becomes $$\begin{aligned}
A^{-4\nu-w}H^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}&=&-q^{w}A^{-2\nu}q^{2\nu}H^{\mathcal{K}}_{\mathtt{asm}}+q^{-w}A^{-2\nu}q^{-2\nu}H^{\mathcal{K}}_{\mathtt{sym}},\nonumber\\
H^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}&=&-(Aq)^{2\nu+w}H^{\mathcal{K}}_{\mathtt{asm}}+(A/q)^{2\nu+w}H^{\mathcal{K}}_{\mathtt{sym}},
\label{tor-cab-top-u}
\end{aligned}$$ and the comparison with ([\[tor-cab-vert-u\]](#tor-cab-vert-u){reference-type="ref" reference="tor-cab-vert-u"}) gives $k=2\nu+w$. Again, one can redefine the topological class by adding an arbitrary constant, $k\to k+c$.

#### What is $k$ on the standard diagram?

A satellite knot is commonly presented with a standard planar diagram, where a "thick" companion is attached to an "extra" element. In our cases this element has a form of the two-strand or Whitehead tangle (as in fig.[\[fig:sat\]](#fig:sat){reference-type="ref" reference="fig:sat"}). Then it *seems* natural to use the torus or twist knot that is the closure of this tangle (fig.[\[fig:tortw\]](#fig:tortw){reference-type="ref" reference="fig:tortw"}) to determine the pattern. Yet this is generally wrong, because (as follows from the above discussion) the "extra" tangle has a sense only together with the companion knot, and moreover with the framing of its "thickened" version.

However, the half-twist number in the attached tangle does define the pattern for a given framed companion. We introduce for *each* companion its own pattern variable $k=w+2\nu+\mathtt{Sh}_{\mathcal{K}}$ with the respective last term from ([\[ShKn\]](#ShKn){reference-type="ref" reference="ShKn"}). In fig.[\[fig:sat\]](#fig:sat){reference-type="ref" reference="fig:sat"}, $\nu=0$ and $\mathtt{Sh}=0$, and hence $k=w$ (but this is not so generally).

## Summary of Jones formulae[]{#sec:Jones label="sec:Jones"}

Now we address to the case which is currently the only definite common point of the HOMFLY and Khovanov cases. This is the case of Jones polynomial, which is obtained for $A=q^2$ from the former and for $t=-1$ from the latter ones. Explicitly, the Jones polynomial of the satellites we consider has the form $$\begin{aligned}
\arraycolsep=0.5mm
\begin{array}{ccccccc}
    J^{\mathcal{S}_{\mathtt{Tor}_k}^{\mathcal{K}}}(q)&=&q^{-3k+1}\Big(-\cfrac{1}{1+q^2}&+&q^{2k-2}\cfrac{1-q^6}{1-q^4}&J^{\mathcal{K}}_{\mathtt{adj}}(q)\Big),\\
    J^{\mathcal{S}_{\mathtt{Tw}_k}^{\mathcal{K}}}(q)&=&q^{-4}\Big(\phantom{-}\cfrac{1+q^4}{1+q^2}&-&q^{-2k\phantom{-2}}\cfrac{1-q^6}{1+q^2}&J^{\mathcal{K}}_{\mathtt{adj}}(q)\Big).\label{Jcab}
\end{array}
\end{aligned}$$ The antisymmetric Jones as well as the trivial Jones identically equals one. Both kinds of the satellite polynomials are now expressed via the same coloured Jones, which is the descendent of both the adjoint and symmetric HOMFLY and explicitly equals $$\begin{aligned}
\arraycolsep=1mm
\begin{array}{ccrccccc} 
    J^{\mathtt{Tor}_n}_{\mathtt{adj}}(q)&=&q^{-8n}\!\cdot\!\hspace{-5mm}&\bigg(\cfrac{q^2(q^2-1)}{q^6-1}&-&q^{2n}&+&\cfrac{q^{10}-1}{q^2(q^6-1)}q^{6n}\bigg),\\[8mm]
    J^{\mathtt{Tw}_n}_{\mathtt{adj}}(q)&=&&\cfrac{(q^{18}-1)(q^2-1)}{q^{12}(q^6-1)^2}&+&q^{-12}(1+q^6)(1-q^4)q^{-2n}&+&\cfrac{(q^{10}-1)(q^4-1)(q^2-1)}{q^{10}(q^6-1)}q^{-6n}
    \label{Jcol}
\end{array}
\end{aligned}$$ We present these expressions for the sake of reference. Namely, one can verify that ([\[ppcd-tw-sat\]](#ppcd-tw-sat){reference-type="ref" reference="ppcd-tw-sat"},[\[ppcd-tor-sat\]](#ppcd-tor-sat){reference-type="ref" reference="ppcd-tor-sat"}) are reduced to ([\[Jcab\]](#Jcab){reference-type="ref" reference="Jcab"}), and the polynomials ([\[FAK\]](#FAK){reference-type="ref" reference="FAK"}) explicitly given in sec.[\[sec:AAK-tor\]](#sec:AAK-tor){reference-type="ref" reference="sec:AAK-tor"},[\[sec:AAK-tw\]](#sec:AAK-tw){reference-type="ref" reference="sec:AAK-tw"} are reduced to ([\[Jcol\]](#Jcol){reference-type="ref" reference="Jcol"}) for $t=-1$.

#### Disclaimer.

Note that $n$ in ([\[Jcol\]](#Jcol){reference-type="ref" reference="Jcol"}) must be odd for torus knots and even for twist knots (see sec.[\[app:coltor\]](#app:coltor){reference-type="ref" reference="app:coltor"},[\[app:coltw\]](#app:coltw){reference-type="ref" reference="app:coltw"}).

If one substitutes $-q^{-2n}$ with $(-q^2)^{-n}$ in the torus formula, it yields the correct adjoint polynomials both for torus knots with odd $n$ and torus links with even $n$. The twist formula with $(-q^2)^{-n}$ instead of $q^{-2n}$ also gives a polynomial for any $n$, and these polynomials satisfy $J^{\mathtt{Tw}_n}_{\mathtt{adj}}(q)=q^{16}J^{\mathtt{Tw}_{-n+1}}_{\mathtt{adj}}(q^{-1})$. I.e., the formula still gives the true adjoint polynomials of the twist knots for even $n$, while the one with the odd $n$ now gives the polynomials of the mirror knots up to the extra factor of $q^{16}$. This property seems to be accidental and does not survive neither in HOMFLY, nor in Khovanov cases. In other words, there is no "analytic" formula for twist knots with any integer $n$ as the half-twist number (see sec.[\[app:coltw\]](#app:coltw){reference-type="ref" reference="app:coltw"}).

[^1]: The $m$-strand case is discussed in App.[\[app:FT\]](#app:FT){reference-type="ref" reference="app:FT"}

[^2]: The ratio of the topological and the vertical framings [@AMcab], sec.5.
