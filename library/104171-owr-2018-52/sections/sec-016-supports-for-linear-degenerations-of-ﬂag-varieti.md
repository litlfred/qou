---
doc_id: 104171-owr-2018-52
doc_title: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018)"
section_id: sec-016-supports-for-linear-degenerations-of-ﬂag-varieti
section_title: "Supports for linear degenerations of ﬂag varieties"
section_number: null
pages: 50-55
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
toc_source: inferred
doc_brief: "Enveloping Algebras and Geometric Representation Theory (Oberwolfach Report No. 52/2018) — The workshop brought together experts investigating algebraic Lie theory from the geometric and categorical"
---
Markus Reineke
(joint work with Xin Fang)
1. Supports
Suppose given a proper algebraic map f : X →Y between irreducible complex
algebraic varieties, with X being smooth. Then the variation of cohomology of the
ﬁbres Xy = f −1(y) is encoded in the complex of constructible sheaves Rf∗QX, in
particular the cohomology of the ﬁbres of f is given by the stalks of its cohomology
sheaves,
H∗(Xy) = H∗
y(Rf∗QX).
By the Decomposition Theorem, Rf∗QX is isomorphic to a ﬁnite direct sum of
shifts of intersection cohomology complexes,
Rf∗QX ≃
n
M
i=1
IC(Si, Li)[di],
where the Si are certain locally closed subvarieties of Y , the Li are local systems
on Si, and di ∈Z. We call {S1, . . . , Sn} the set of supports of f. This is thus an
invariant of the map f, which encodes the variation of cohomology along its ﬁbres
in terms of the singularities (or, more precisely, their local intersection cohomology)
of the subvarieties Si.
For an introduction to the concept of supports and an overview of known results,
see [4]. For example, if f is a semismall map, the supports are precisely the so-
called relevant strata, and if f is ﬂat with irreducible d-dimensional ﬁbres, all
supports have codimension less than d (Goresky-Macpherson). For certain abelian
ﬁbrations, Ngo’s support theorem describes the supports, and a result of Migliorini
and Shende localizes the supports inside so-called higher discriminant loci.
It is an interesting problem to describe the supports for proper maps featuring
in contexts of Geometric Representation Theory, which we will do in the following
for the ﬂat family of so-called linear degenerations of ﬂag varieties.
Enveloping Algebras and Geometric Representation Theory
3131
2. Linear degenerations
Let n ≥1, and let V be an (n + 1)-dimensional complex vector space. Then the
ﬂag variety SL(V )/B is realized as the closed subset
Fl(V ) = {U1 ⊂U2 ⊂. . . ⊂Un ⊂V | dim Ui = i}
of the product Gr = Qb
i=1 Gri(V ) of Grassmannians of V .
We would like to degenerate Fl(V ) inside Gr by relaxing the containment rela-
tion between the subspaces constituting the ﬂag. For a tuple f∗= (f1, . . . , fn−1) ∈
Hom(V, V )n−1, we deﬁne
Flf∗(V ) = {(U1, . . . , Un) ∈Gr | fi(Ui) ⊂Ui+1}
as the f∗-degenerate ﬂag variety.
For example, if all fi are isomorphisms, we
recover Fl, and in the most degenerate case fi = 0, we ﬁnd Gr. We call r(f∗) =
(rank(fj−1 ◦. . . ◦fi))i<j the rank tuple of f∗and note that Flf∗(V ) only depends
on r = r(f∗); thus we can denote it by Flr(V ). The following is proved in [1]:
• The degenerate ﬂag variety Flf∗(V ) is irreducible of dimension n(n + 1)/2
if and only if r(f∗) ≥r1 = (n + 1 + i −j)i<j.
• In this case, Flf∗(V ) is a normal locally complete intersection variety,
admitting an aﬃne paving and an algebraic group action with a dense
orbit.
• Flr1 is isomorphic to E. Feigin’s degenerate ﬂag variety.
• The degenerate ﬂag variety Flf∗(V ) is of dimension n(n + 1)/2 if and only
if r(f∗) ≥r2 = (n + i −j)i<j, in which case it is a locally complete
intersection variety admitting an aﬃne paving.
• The number of irreducible components of Flr2(V ) equals the n-th Catalan
number.
Deﬁne U ⊂Hom(V, V )n−1 as the open subset of all tuples f∗such that r(f∗) ≥
r1, on which the group G = GL(V )n acts naturally via base change; the orbits
O(r) for this action can be indexed by rank tuples r ≥r1. We deﬁne the linear
degeneration family
Fl = {(f∗, U∗) ∈U × Gr | fi(Ui) ⊂Ui+1} ⊂U × Gr,
which admits G-equivariant maps
Gr
p←Fl
π→U
such that p is open in a homogeneous bundle (and thus identifying Fl as smooth
and irreducible), and π is projective and ﬂat with irreducible ﬁbres π−1(f∗) =
Flf∗(V ) by the above theorem. We want to determine the supports of π.
3132
Oberwolfach Report 52/2018
3. Main result
To a Motzkin path of length n, given by a tuple x∗= (0 = x0, x1, . . . , xn = 0) such
that xi ≥0 and xi −xi−1 ∈{−1, 0, 1}, we associate a rank tuple r(x∗), called a
Motzkin rank tuple, by
r(x∗)im = n + 1 −
max
i≤j≤k≤l≤m(xk−1 + xk −xj−1 −xl).
The main result is:
The set of supports of the family π : Fl →U is the set of Motzkin rank tuples
O(r(x∗)). In other words, we have
Rπ∗QFl ≃
M
x∗
IC(O(r(x∗))) ⊗V (x∗)•
for certain (unknown) graded Q-vector spaces V (x∗)• encoding multiplicities and
shifts.
4. Techniques
To prove the main result, we use G. Lusztig’s geometric realization of quantized
enveloping algebras and their canonical bases [3].
Denoting by Q the linearly
oriented type An quiver, for any dimension type d ∈Nn we consider the variety
Rd(Q) parametrizing d-dimensional representations of Q, on which an algebraic
group Gd acts naturally. The space
M
d
K0(PervGd(Rd(Q))) ⊗Z Q(v)
of suitably extended Grothendieck groups of the categories of Gd-equivariant per-
verse sheaves on Rd(Q) carries a natural Nn-graded associative convolution prod-
uct ∗, and a natural basis B given by intersection cohomology complexes along the
(ﬁnitely many) orbits of each Rd(Q). The resulting based algebra is isomorphic
to U+
v (sln+1), with Chevalley generators Ei subject to quantized Serre relations,
together with Lusztig’s canonical basis.
The relation to linear degenerations of ﬂag varieties is provided by the observa-
tion that U ⊂Rd(Q) for d = (n + 1, . . . , n + 1), that the canonical basis elements
b(r) corresponding to intersection cohomology complexes on this variety are nat-
urally indexed by rank tuples r, and that O(r) is a support of π : Fl →U if and
only if b(r) appears with non-zero coeﬃcient in the expansion of the monomial
E(n)
1
. . . E(1)
n E(1)
1
. . . E(n)
n
=
X
r≥r1
γ(r)b(r)
in the canonical basis. Using the Knight-Zelevinsky multisegment duality [2] and
explicit degree estimates for the coeﬃcients γ(r), the above description of supports
is achieved.
Enveloping Algebras and Geometric Representation Theory
3133
References
[1] G. Cerulli Irelli, X. Fang, E. Feigin, G. Fourier, M. Reineke, Linear degenerations of ﬂag
varieties , Math. Z. 287 (2017), no. 1–2, 615–654.
[2] H. Knight, A. Zelevinsky, Representation of quivers of type A and the multisegment duality,
Adv. Math 117 (1996) , 273–293.
[3] G. Lusztig, Quivers, perverse sheaves, and quantized enveloping algebras , J. Amer. Math.
Soc. 4 (1991), no. 2, 365–421.
[4] L. Migliorini, Support theorems for algebraic maps , Milan J. Math. Vol. 83 (2015), 21–45.
Elliptic quantum groups
Valerio Toledano Laredo
(joint work with Sachin Gautam)
The dynamical Yang–Baxter equations (DYBE) were introduced by Felder in 1994
to circumvent the fact that the Yang–Baxter equations do not admit elliptic so-
lutions outside of type An [3]. Felder showed that the classical DYBE possess
elliptic solutions for all Lie types, proposed that elliptic quantum groups be the
quantum groups associated to elliptic solutions of the quantum YBE via the RTT
construction of Faddeev–Reshetikhin–Takhtajan, and gave an elliptic solution of
the quantum DYBE in type A.
Jimbo–Konno–Odake–Shiraishi [11] and Etingof–Schiﬀmann [1] later showed
that elliptic solutions of the quantum DYBE exist for any complex semisimple
Lie algebra g and ﬁnite–dimensional representation V of the quantum loop alge-
bra Uq(Lg) of g. This led to a tentative deﬁnition of the elliptic quantum group
Eℏ,τ(g) as the algebra Uq(Lg), where q = exp(πιℏ), but with a diﬀerent, dy-
namical coproduct obtained by twisting the standard coproduct of Uq(Lg) by the
corresponding fusion operator.
A more intrinsic presentation was obtained by Kojima–Konno [4] for g = sln
and, more recently, by Farghly–Konno–Oshima [2] for any complex semisimple g,
under the assumption that the elliptic parameter p = exp(2πιτ) is formal, so that
the odd theta function ϑ(z) = z1/2 Q
n>0(1 −zpn)(1 −z−1pn−1)(1 −pn)−2/2πι is
regarded as a formal power series in p with coeﬃcients in C[z±1]. The presentation
is given in terms of Drinfeld full currents, or equivalently integer moded generators,
which satisfy commutation relations involving ϑ.
In joint work with Sachin Gautam [10], we propose a deﬁnition of the category of
ﬁnite–dimensional representations of Eℏ,τ(g) which is intrinsic, uniform for all Lie
types, and valid for numerical values of p. Our presentation of Eℏ,τ(g) is given in
terms of Drinfeld half rather than full currents, which are elliptic rather than distri-
butional functions of a complex parameter, and recovers Farghly–Konno–Oshima’s
presentation if p is regarded as formal. Interestingly, however, our presentation
cannot be given by canonical generators and relations for p numerical since ϑ(z)
has essential singularities at z = 0, ∞in that case.
We classify simple objects in Repfd(Eℏ,τ(g)) in terms of elliptic Drinfeld poly-
nomials. Our classiﬁcation is new even for g = sl2, and is analogous to Drinfeld’s
3134
Oberwolfach Report 52/2018
and Chari–Pressley’s highest weight classiﬁcation of irreducible ﬁnite–dimensional
representations of Yangians and quantum loop algebras [6, 5]. This analogy does
not extend to proofs, however, since Eℏ,τ(g) does not seem to admit Verma mod-
ules. We circumvent this issue by constructing a functor Θ from ﬁnite–dimensional
representations of the quantum loop algebra Uq(Lg) to those of Eℏ,τ(g), which is
such that Θ(V) is irreducible if and only if V is, and relying on the classiﬁcation
of simples in Repfd(Uq(Lg)).
The functor Θ is governed by the monodromy of the p–diﬀerence equations
fi(pz) = Ψi(z)fi(z) determined by the commuting (half–)currents of Uq(Lg) on a
ﬁnite–dimensional representation V. It is a trigonometric version of the functor
from ﬁnite–dimensional representations of the Yangian Yℏg to those of Uq(Lg) we
constructed in our previous work [7, 8, 9].
Our presentation of Eℏ,τ(g) is valid for an arbitrary symmetrisable Kac–Moody
algebra g, as is our classiﬁcation, provided ﬁnite–dimensionality is replaced by an
integrability and category O conditions.
References
[1] P. Etingof, O. Schiﬀmann, On highest weight modules over elliptic quantum groups, Lett.
Math. Phys. 47 (1999), 179–188.
[2] R. Farghly, H. Konno, K. Oshima, Elliptic algebra Uq,p(bg) and quantum Z–algebras, Algebr.
Represent. Theory, 18 (2015), 103–135.
[3] G. Felder, Conformal ﬁeld theory and integrable systems associated to elliptic curves, Pro-
ceedings of the International Congress of Mathematicians, Vol. 1, 2 (Z¨urich, 1994), 1247–
1255, Birkh¨auser, Basel, 1995.
[4] T. Kojima, H. Konno, Elliptic algebra Uq,p(d
slN) and the Drinfeld realization of the elliptic
quantum group Bq,λ(d
slN), Comm. Math. Phys. 239 (2003), 405-447.
[5] V. Chari, A. Pressley, Quantum aﬃne algebras and their representations, Representations
of groups (Banﬀ, AB, 1994), 59–78, CMS Conf. Proc., 16, Amer. Math. Soc., 1995.
[6] V. Drinfeld, A new realization of Yangians and quantum aﬃne algebras, Soviet Math. Dokl.
36 (1988), 212–216.
[7] S. Gautam, V. Toledano Laredo, Yangians and quantum loop algebras, Selecta Math. (N.S.)
19 (2013), 271–336.
[8] S. Gautam, V. Toledano Laredo, Yangians, quantum loop algebras, and abelian diﬀerence
equations, J. Amer. Math. Soc., 29 (2016), 775–824.
[9] S. Gautam, V. Toledano Laredo, Meromorphic tensor equivalence for Yangians and quantum
loop algebras, Publ. Math. Inst. Hautes ´Etudes Sci. 125 (2017), 267–337.
[10] S. Gautam, V. Toledano Laredo, Elliptic quantum groups and their ﬁnite–dimensional rep-
resentations, arXiv:1707.06469, 52 pages.
[11] M. Jimbo, H. Konno, S. Odake, J. Shiraishi, Quasi-Hopf twistors for elliptic quantum
groups, Transform. Groups, 4 (1999), 303–327.
Enveloping Algebras and Geometric Representation Theory
3135
