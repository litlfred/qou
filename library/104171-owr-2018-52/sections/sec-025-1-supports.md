---
doc_id: 104171-owr-2018-52
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 52/2018"
section_id: sec-025-1-supports
section_title: "Supports"
section_number: 1
pages: 50-52
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 52/2018 — The workshop brought together experts investigating algeb raic Lie theory from the geometric and categorical viewpoints."
---
Markus Reineke
(joint work with Xin Fang)
1. Supports
Suppose given a proper algebraic map f : X→ Y between irreducible complex
algebraic varieties, with X being smooth. Then the variation of cohomology of the
ﬁbres Xy =f −1(y) is encoded in the complex of constructible sheaves Rf∗QX , in
particular the cohomology of the ﬁbres of f is given by the stalks of its cohomology
sheaves,
H ∗(Xy) =H∗
y(Rf∗QX ).
By the Decomposition Theorem, Rf∗QX is isomorphic to a ﬁnite direct sum of
shifts of intersection cohomology complexes,
Rf∗QX≃
n⨁
i=1
IC(Si,Li)[di],
where the Si are certain locally closed subvarieties of Y , the Li are local systems
on Si, and di∈ Z. We call {S1,..., Sn} the set of supports of f . This is thus an
invariant of the map f , which encodes the variation of cohomology along its ﬁbres
in terms of the singularities (or, more precisely, their local intersec tion cohomology)
of the subvarieties Si.
For an introduction to the concept of supports and an overview of known results,
see [4]. For example, if f is a semismall map, the supports are precisely the so-
called relevant strata, and if f is ﬂat with irreducible d-dimensional ﬁbres, all
supports have codimension less than d (Goresky-Macpherson). For certain abelian
ﬁbrations, Ngo’s support theorem describes the supports, and a result of Migliorini
and Shende localizes the supports inside so-called higher discriminant loci.
It is an interesting problem to describe the supports for proper ma ps featuring
in contexts of Geometric Representation Theory, which we will do in t he following
for the ﬂat family of so-called linear degenerations of ﬂag varieties.
Enveloping Algebras and Geometric Representation Theory 3131
2. Linear degenerations
Let n≥ 1, and let V be an ( n + 1)-dimensional complex vector space. Then the
ﬂag variety SL(V )/B is realized as the closed subset
Fl(V ) ={U1⊂U2⊂... ⊂Un⊂V| dimUi =i}
of the product Gr = ∏ b
i=1 Gri(V ) of Grassmannians of V .
We would like to degenerate Fl( V ) inside Gr by relaxing the containment rela-
tion between the subspaces constituting the ﬂag. For a tuple f∗ = (f1,...,f n−1)∈
Hom(V,V )n−1, we deﬁne
Flf∗ (V ) ={(U1,...,U n)∈ Gr|fi(Ui)⊂Ui+1}
as the f∗-degenerate ﬂag variety . For example, if all fi are isomorphisms, we
recover Fl, and in the most degenerate case fi = 0, we ﬁnd Gr. We call r(f∗) =
(rank(fj−1◦... ◦fi))i<j the rank tuple of f∗ and note that Fl f∗ (V ) only depends
on r = r(f∗); thus we can denote it by Fl r(V ). The following is proved in [1]:
• The degenerate ﬂag variety Fl f∗ (V ) is irreducible of dimension n(n + 1)/2
if and only if r(f∗)≥ r1 = (n + 1 +i−j)i<j.
• In this case, Fl f∗ (V ) is a normal locally complete intersection variety,
admitting an aﬃne paving and an algebraic group action with a dense
orbit.
• Flr1
is isomorphic to E. Feigin’s degenerate ﬂag variety.
• The degenerate ﬂag variety Fl f∗ (V ) is of dimension n(n + 1)/2 if and only
if r(f∗) ≥ r2 = (n +i−j)i<j, in which case it is a locally complete
intersection variety admitting an aﬃne paving.
• The number of irreducible components of Fl r2
(V ) equals the n-th Catalan
number.
DeﬁneU⊂ Hom(V,V )n−1 as the open subset of all tuples f∗ such that r(f∗)≥
r1, on which the group G = GL(V )n acts naturally via base change; the orbits
O(r) for this action can be indexed by rank tuples r≥ r1. We deﬁne the linear
degeneration family
Fl ={(f∗,U ∗)∈U× Gr|fi(Ui)⊂Ui+1}⊂U× Gr,
which admits G-equivariant maps
Gr
p
←F l
π
→U
such that p is open in a homogeneous bundle (and thus identifying Fl as smooth
and irreducible), and π is projective and ﬂat with irreducible ﬁbres π−1(f∗) =
Flf∗ (V ) by the above theorem. We want to determine the supports of π.
3132 Oberwolfach Report 52/2018
