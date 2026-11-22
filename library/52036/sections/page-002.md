---
doc_id: 52036
doc_title: "Torus Knots Extremizing the Möbius Energy"
section_id: page-002
section_title: "Page 2"
pages: 2-2
pdf_page: 2
source_pdf: 52036.pdf
source_sha256: ab02866e1f7191b7
text_source: ocr
granularity: page
doc_brief: "Torus Knots Extremizing the Möbius Energy — 9 sections: Page 1; Page 2; Page 3"
---
2 Experimental Mathematics, Vol. 2 (1993), No. 1

In this article we construct the first explicit ex-
amples of knotted curves that are critical for E.
Our basic observation is that the Mébius-invariant
energy E extends naturally to simple closed curves
I. c R™ (Section 2). In particular, if T is a simple
closed curve in S? C R‘ and o : S? + R?Uco
is stereographic projection, then E(o(I)) = E(L)
provided o([) C R®. Then we use the principle of
symmetric criticality (Section 3) to show that for
each relatively prime pair of integers (p, q) there is
a (p,q)-torus knot T,,, C S® critical for E. This
curve I’,,, is a principal orbit of an isometric action
of St on $°. In the same way, we construct crit-
ical orbital links with more than one component
(Section 4).

The energies E(I,,,) can be computed explic-
itly in terms of rational trigonometric integrals.
This makes them ideal benchmarks to check the
accuracy of computer experiments with various dis-
cretized energies. One such discrete model is men-
tioned in Section 5. We have implemented sev-
eral programs using this model, run experiments,
and tabulated some of the results, but clearly more
work needs to be done. In this regard, we mention
that several Japanese mathematicians and, inde-
pendently, Bryson [Bryson et al. 1993] have also
conducted computer experiments to seek nontriv-
ial extrema. In particular, Bryson reports find-
ing a trefoil—that is, a (2,3)-torus knot—with en-
ergy approximately equal to 74, which is close to
the critical value of 74.4120 (see Table 1 in Sec-
tion 5).

It is well-known (see [Schubert 1953, p. 250],
for example) that torus knots are prime, and it is
tempting to conjecture that the stereographic im-
ages o(I',,,) are the energy minimizers guaranteed
to exist by [Freedman et al.]. However, we expect
this to be false when both p and q are large, for
the following reason: We can view I, as a p- or
q-strand braid lying on the surface of a torus, and
if both p and q are at least three, energy can be
saved when “extra strands” of T,,, depart from the
surface of the torus and push into the interiors of
the complementary solid tori.

The right conjecture, which is supported by our
most recent experiments (Section 6), appears to
be this: [’,, is a stable local minimum for E when
p = 2 or q = 2, but is not a minimizer otherwise.
The general E-stability question will be explored
elsewhere [Kusner and Sullivan].

2. MOBIUS INVARIANCE

Suppose [ Cc R” is a simple closed curve of class
C', that is, one that admits a parametrization
T.: S'< R” whose first derivative I” is Lipschitz.
(Weaker differentiability assumptions are possible
[Freedman et al., § 1], but we find C1 best suited
to our purposes.) Let D(z, y) denote the distance
between I(x) and I'(y) along I’, that is,

D(2,y) = min( Ir'(2)| af IP’(2)| iz).

Definition and Proposition. Given T as above, the
Mobius energy

E() = I/ (ma Tur 7 Pew)

Stx gt

x |I"(a)| P"(y)| da dy

is finite and independent of the parametrization of
T. Moreover, if is a Mobius transformation of
R”™ U co, then E(u(L)) = E(L) provided p(T) C
R”.

Proof. The arguments, with only formal modifica-
tions to move from 3 to m dimensions, are essen-
tially those of [Freedman et al., §§1 and 2]. In
particular, concerning the Mobius invariance, the
first term in the integrand is pointwise invariant,
whereas the second term in the integral is “intrin-
sic”, in the sense that, for any « > 0, the asymp-
totic expansion

IT'(x)| IP’(w)| _ 40
I Day) @ray= : 4+ O(e)

is invariant under all C1! diffeomorphisms of R™,
not only Mébius transformations. Oo
