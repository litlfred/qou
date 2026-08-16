---
doc_id: 104171-owr-2018-52
doc_title: "Mathematisches Forschungsinstitut Oberwolfach Report No. 52/2018"
section_id: sec-027-4-techniques
section_title: "Techniques"
section_number: 4
pages: 52-58
source_pdf: 10.4171-owr-2018-52.pdf
source_sha256: b33ed36eaa470877
doc_brief: "Mathematisches Forschungsinstitut Oberwolfach Report No. 52/2018 — The workshop brought together experts investigating algeb raic Lie theory from the geometric and categorical viewpoints."
---
To prove the main result, we use G. Lusztig’s geometric realization of quantized
enveloping algebras and their canonical bases [3]. Denoting by Q the linearly
oriented type An quiver, for any dimension type d∈ Nn we consider the variety
Rd(Q) parametrizing d-dimensional representations of Q, on which an algebraic
group Gd acts naturally. The space
⨁
d
K0(PervGd(Rd(Q)))⊗Z Q(v)
of suitably extended Grothendieck groups of the categories of Gd-equivariant per-
verse sheaves on Rd(Q) carries a natural Nn-graded associative convolution prod-
uct∗, and a natural basis B given by intersection cohomology complexes along the
(ﬁnitely many) orbits of each Rd(Q). The resulting based algebra is isomorphic
toU +
v (sln+1), with Chevalley generators Ei subject to quantized Serre relations,
together with Lusztig’s canonical basis.
The relation to linear degenerations of ﬂag varieties is provided by th e observa-
tion thatU⊂ Rd(Q) for d = (n + 1,...,n + 1), that the canonical basis elements
b(r) corresponding to intersection cohomology complexes on this varie ty are nat-
urally indexed by rank tuples r, and that O(r) is a support of π :Fl→U if and
only if b(r) appears with non-zero coeﬃcient in the expansion of the monomial
E(n)
1 ...E (1)
n E(1)
1 ...E (n)
n =
∑
r≥r1
γ(r)b(r)
in the canonical basis. Using the Knight-Zelevinsky multisegment dua lity [2] and
explicit degree estimates for the coeﬃcients γ(r), the above description of supports
is achieved.
Enveloping Algebras and Geometric Representation Theory 3133
References
[1] G. Cerulli Irelli, X. Fang, E. Feigin, G. Fourier, M. Rein eke, Linear degenerations of ﬂag
varieties , Math. Z. 287 (2017), no. 1–2, 615–654.
[2] H. Knight, A. Zelevinsky, Representation of quivers of type A and the multisegment dua lity,
Adv. Math 117 (1996) , 273–293.
[3] G. Lusztig, Quivers, perverse sheaves, and quantized enveloping algeb ras , J. Amer. Math.
Soc. 4 (1991), no. 2, 365–421.
[4] L. Migliorini, Support theorems for algebraic maps , Milan J. Math. Vol. 83 (2015), 21–45.
Elliptic quantum groups
V alerio Toledano Laredo
(joint work with Sachin Gautam)
The dynamical Yang–Baxter equations (DYBE) were introduced by Felder in 1994
to circumvent the fact that the Yang–Baxter equations do not ad mit elliptic so-
lutions outside of type An [3]. Felder showed that the classical DYBE possess
elliptic solutions for all Lie types, proposed that elliptic quantum grou ps be the
quantum groups associated to elliptic solutions of the quantum YBE v ia the RTT
construction of Faddeev–Reshetikhin–Takhtajan, and gave an e lliptic solution of
the quantum DYBE in type A.
Jimbo–Konno–Odake–Shiraishi [11] and Etingof–Schiﬀmann [1] later showed
that elliptic solutions of the quantum DYBE exist for any complex semis imple
Lie algebra g and ﬁnite–dimensional representation V of the quantum loop alge-
bra Uq(Lg) of g. This led to a tentative deﬁnition of the elliptic quantum group
Eℏ,τ (g) as the algebra Uq(Lg), where q = exp(πιℏ), but with a diﬀerent, dy-
namical coproduct obtained by twisting the standard coproduct o fUq(Lg) by the
corresponding fusion operator.
A more intrinsic presentation was obtained by Kojima–Konno [4] for g = sln
and, more recently, by Farghly–Konno–Oshima [2] for any complex s emisimple g,
under the assumption that the elliptic parameter p = exp(2πιτ ) is formal, so that
the odd theta function ϑ(z) = z1/2 ∏
n>0(1−zpn)(1−z−1pn−1)(1−pn)−2/2πι is
regarded as a formal power series in p with coeﬃcients in C[z±1]. The presentation
is given in terms of Drinfeld full currents, or equivalently integer mod ed generators,
which satisfy commutation relations involving ϑ.
In joint work with Sachin Gautam [10], we propose a deﬁnition of the ca tegory of
ﬁnite–dimensional representations of Eℏ,τ (g) which is intrinsic, uniform for all Lie
types, and valid for numerical values of p. Our presentation of Eℏ,τ (g) is given in
terms of Drinfeld half rather than full currents, which are elliptic ra ther than distri-
butional functions of a complex parameter, and recovers Farghly –Konno–Oshima’s
presentation if p is regarded as formal. Interestingly, however, our presentation
cannot be given by canonical generators and relations for p numerical since ϑ(z)
has essential singularities at z = 0,∞ in that case.
We classify simple objects in Rep fd(Eℏ,τ (g)) in terms of elliptic Drinfeld poly-
nomials. Our classiﬁcation is new even for g = sl2, and is analogous to Drinfeld’s
3134 Oberwolfach Report 52/2018
and Chari–Pressley’s highest weight classiﬁcation of irreducible ﬁnite –dimensional
representations of Yangians and quantum loop algebras [6, 5]. This a nalogy does
not extend to proofs, however, since Eℏ,τ (g) does not seem to admit Verma mod-
ules. We circumvent this issue by constructing a functor Θ from ﬁnit e–dimensional
representations of the quantum loop algebra Uq(Lg) to those of Eℏ,τ (g), which is
such that Θ( V) is irreducible if and only if V is, and relying on the classiﬁcation
of simples in Rep fd(Uq(Lg)).
The functor Θ is governed by the monodromy of the p–diﬀerence equations
fi(pz) = Ψ i(z)fi(z) determined by the commuting (half–)currents of Uq(Lg) on a
ﬁnite–dimensional representation V. It is a trigonometric version of the functor
from ﬁnite–dimensional representations of the Yangian Yℏ g to those of Uq(Lg) we
constructed in our previous work [7, 8, 9].
Our presentation of Eℏ,τ (g) is valid for an arbitrary symmetrisable Kac–Moody
algebra g, as is our classiﬁcation, provided ﬁnite–dimensionality is replaced by a n
integrability and category O conditions.
References
[1] P. Etingof, O. Schiﬀmann, On highest weight modules over elliptic quantum groups , Lett.
Math. Phys. 47 (1999), 179–188.
[2] R. Farghly, H. Konno, K. Oshima, Elliptic algebra Uq,p (ˆg) and quantum Z–algebras, Algebr.
Represent. Theory, 18 (2015), 103–135.
[3] G. Felder, Conformal ﬁeld theory and integrable systems associated to elliptic curves , Pro-
ceedings of the International Congress of Mathematicians, Vol. 1, 2 (Z¨ urich, 1994), 1247–
1255, Birkh¨ auser, Basel, 1995.
[4] T. Kojima, H. Konno, Elliptic algebra Uq,p (ˆslN ) and the Drinfeld realization of the elliptic
quantum group Bq,λ (ˆslN ), Comm. Math. Phys. 239 (2003), 405-447.
[5] V. Chari, A. Pressley, Quantum aﬃne algebras and their representations , Representations
of groups (Banﬀ, AB, 1994), 59–78, CMS Conf. Proc., 16, Amer. Math. Soc., 1995.
[6] V. Drinfeld, A new realization of Yangians and quantum aﬃne algebras , Soviet Math. Dokl.
36 (1988), 212–216.
[7] S. Gautam, V. Toledano Laredo, Yangians and quantum loop algebras , Selecta Math. (N.S.)
19 (2013), 271–336.
[8] S. Gautam, V. Toledano Laredo, Yangians, quantum loop algebras, and abelian diﬀerence
equations, J. Amer. Math. Soc., 29 (2016), 775–824.
[9] S. Gautam, V. Toledano Laredo, Meromorphic tensor equivalence for Yangians and quantum
loop algebras, Publ. Math. Inst. Hautes ´Etudes Sci. 125 (2017), 267–337.
[10] S. Gautam, V. Toledano Laredo, Elliptic quantum groups and their ﬁnite–dimensional rep-
resentations, arXiv:1707.06469, 52 pages.
[11] M. Jimbo, H. Konno, S. Odake, J. Shiraishi, Quasi-Hopf twistors for elliptic quantum
groups, Transform. Groups, 4 (1999), 303–327.
Enveloping Algebras and Geometric Representation Theory 3135
Rigid indecomposable modules and real Schur roots
Christof Geiß
(joint work with Bernard Leclerc, Jan Schr¨ oer)
Let A be a ﬁnite dimensional hereditary K-algebra. Its Grothendieck group
K0(A) = ZI for I ={1, 2,...,n } comes with the canonical basis ( αi)i∈I given
by the classes of the simple A-modules. The homological bilinear form
(M,N )↦→dimK HomA(M,N )− dimK Ext1
A(M,N ),
on the category of ﬁnite dimensional A-modules descends to an integral bilinear
form on K0(A) determined by
⟨αi,αj⟩(C,D,Ω) =





cicij if (i,j )∈ Ω,
ci if i =j,
0 else .
Here, C∈ ZI×I is a symmetrizable generalized Cartan matrix, D = diag((ci)i∈I )
is a (left) symmetrizer of C and Ω ⊂I×I is an orientation for C. We may suppose
that (i,j )∈ Ω implies i<j . In other words, K0(A) has the structure of a general-
ized Cartan lattice with an orthogonal exceptional sequence in the sense of Hubery
and Krause [8, Sec. 3]. We can consider ( C,D, Ω) as a basic combinatorial invari-
ant of A. Note that C will be symmetric if K is algebraically closed. From Kac’s
theorem and its relatives it follows that for many ﬁnite dimensional he reditary al-
gebras the classes of the ﬁnite dimensional indecomposable A-modules correspond
precisely to the positive roots of the corresponding Kac-Moody Lie algebra g(C).
This holds in particular if K is algebraically closed or ﬁnite, or if C is of ﬁnite or of
aﬃne type. The Weyl group W⊂ Aut(ZI ) is generated by the simple reﬂections
(si)i∈I , where
si(α) := α− 2(α,αi)
(αi,α ) αi,
and (−,−) denotes the symmetrized bilinear form. The real roots Φ re(C) :=
∪i∈IWαi can be considered as a subset of the roots of the Kac-Moody Lie alg ebra
g(C). The real Schur roots are a subset of the positive real roots Φ +
re(C) which
can be described combinatorially, following [8, Cor. 4.8], in terms of non -crossing
partitions, namely
Φ rS(C, Ω) = {α∈ Φ +(C)| 1<s α<s 1s2··· sn},
where < denotes the absolute order on W .
By work of Crawley-Boevey [2] and Ringel [9] the real Schur roots c an be iden-
tiﬁed with the classes of the rigid indecomposable A-modules for any ﬁnite dimen-
sional hereditary K-algebraA with combinatorial invariant (C,D, Ω). Here, rigid
means that the module has no self-extensions. From the work of Cr awley-Boevey
and Ringel follows also that the endomorphism ring of each rigid indeco mposable
A-module is isomorphic to the endomorphism ring of a simple A-module, and thus
by Schur’s Lemma it is isomorphic to a division algebra.
3136 Oberwolfach Report 52/2018
In previous work [5] we introduced for any ﬁeld F an 1-Iwanaga Gorenstein
F-algebra H := HF(C,D, Ω), deﬁned in terms of a quiver with relations. Its
modules of ﬁnite projective dimension form a hereditary exact cate gory. They
behave in many aspects like the modules over an hereditary algebra w ith the same
combinatorial invariants. For example the Grothendieck group of t hose modules
can be identiﬁed with ( ZI,⟨−,−⟩(C,D,Ω) ). In this spirit we can now show the
following result:
Theorem. Let H =HF(C,D, Ω) be as above. Then the following holds:
(a) Taking classes in the Grothendieck group of modules of ﬁnite pro jective
dimension, induces a bijection between the isoclasses of indecompos able
rigid H-modules of ﬁnite projective dimension, and the real Schur roots
Φ rS(C, Ω).
(b) If M is a rigid indecomposable H-module of ﬁnite projective dimension,
we have End H (M ) ∼
= F[ǫ]/(ǫci) for some i ∈ I, and M is free as an
EndH (M )-module.
(c) Taking classes in the Grothendieck group of all ﬁnite dimensional H-
modules induces a bijection between the isoclasses of left ﬁnite H-bricks
and dual real Schur roots Φ rS(CT, Ω).
Here, a module is called a brick if its endomorphism ring is a division algebra,
and it is called left ﬁnite if the smallest torsion class which contains it is functorially
ﬁnite.
In order to approach this result we note that the algebras ( HF(C,kD, Ω))k∈N+
form a directed system with elements ǫk∈Z(HF(C,kD, Ω)) and canonical isomor-
phisms
HF(C,kD, Ω)/(ǫl
kHF(C,kD, Ω)) ∼
=H(C,lD, Ω)
for l<k , such that ǫk is projected onto ǫl, see [6, Sec. 2.2]. It follows that
ˆH := lim←−k
HF(C,kD, Ω)
is naturally a noetherian F[ [ǫ] ]-algebra. Moreover we consider the localization ~H =
~HF( (ε) )(C,D, Ω) = ˆHε. It is easy to see that ˆH is free of ﬁnite rank as an F[ [ε] ]-
module and (except for trivial cases) of global dimension 2. On the o ther hand ~H
is a ﬁnite-dimensional hereditary F( (ε) )-algebra of type (C,D, Ω). The diagram
ˆH loc /d47/d47
proj
/d15/d15
~H
H
allows us to relate the F[ [ε] ]-lattices of ˆH, via the reduction functor H⊗ ˆH−, with
the ﬁnite dimensional H-modules of ﬁnite projective dimension, and similarly,
via the localization functor ~H⊗ ˆH−, with the ﬁnite dimensional modules of the
hereditary F( (ǫ) )-algebra ~H. This is quite similar to a p-modular system.
Enveloping Algebras and Geometric Representation Theory 3137
Although some of our basic constructions are closely related to [3], w e have
to work with the exchange graph of support tilting modules rather t han with
exceptional sequences. The following facts are crucial for the pr oof of our theorem:
• τ -rigid H-modules have in fact projective dimension at most 1 (L. De-
monet), thus the exchange graph of support tilting H-modules is |I|-
regular [1].
• The exchange graph of support tilting modules for ~H is connected and
|I|-regular [7].
• Statement (c) is an almost formal consequence of (a) and (b) by [4 ,
Thm. 4.1].
Finally it is worth to mention that the algebra ˆH = ˆHF[ [ε] ](C,D, Ω) can be
described as
F⟨⟨Q(C, Ω)⟩⟩/I,
where F⟨⟨Q(C, Ω)⟩⟩is the completed path algebra of the quiver Q(C, Ω), and I
is the ideal generated by the relations (H2), which were both introd uced in [5,
Sec. 1.4]. In this description, ˆH carries a F[ [ε] ]-algebra structure via the map
which sends ε to ∑
i∈Iεci
i ∈ ˆH. For example, with
C =
( 2 −1 0
−2 2 −2
0 −1 2
)
, D =
( 2 0 0
0 1 0
0 0 2
)
, Ω = {(1, 2), (2, 3)}
we get
Q(C, Ω) = 1
ε1
/d6/d6
2α/d111/d111
ε2
/d6/d6
3
β/d111/d111
ε3
/d6/d6
and ( H2) = (ε2
1α−αε2,ε 2β−βε2
3).
References
[1] T. Adachi, O. Iyama, I. Reiten: τ -tilting theory. Compos. Math. 150 (2014), no. 3, 415–452.
[2] W. Crawley-Boevey: Exceptional sequences of representations of quivers . Representations
of Algebras (Ottawa, ON, 1992), 117–124, CMS Conf. Proc. 14, Amer. Math. Soc., 1993.
[3] W. Crawley-Boevey: Rigid integral representations of quivers . Representation theory of
algebras (Cocoyoc, 1994), 155–163, CMS Conf. Proc., 18, Amer. Math. Soc., 1996.
[4] L. Demonet, O. Iyama, G. Jasso: τ -tilting ﬁnite algebras, bricks and g-vectors . Int. Math.
Res. Not. IMRN (2017): 1–41.
[5] Ch. Geiß, B. Leclerc, J. Schr¨ oer: Quivers with relations for symmetrizable Cartan matrices
I: Foundations. Invent. Math. 209 (2017), no. 1, 61–158.
[6] Ch. Geiß, B. Leclerc, J. Schr¨ oer: Quivers with relations for symmetrizable Cartan matrices
II: Change of symmetrizers . IMRN Vol. 2018 no. 9, 2866–2898.
[7] A. Hubery: The cluster complex of an hereditary artin algebra . Algebr. Represent. Theory
14 (2011), no. 6, 1163–1185.
[8] A. Hubery, H. Krause: A categoriﬁcation of non-crossing partitions . J. Eur. Math. Soc. 18
(2016), no. 10, 2273–2313.
[9] C.M. Ringel: The braid group action on the set of exceptional sequences of a hereditary
Artin algebra . Abelian Group Theory and Related Topics (Oberwolfach, 199 3), 339–352,
Contemp. Math. 171, Amer. Math. Soc., 1994
3138 Oberwolfach Report 52/2018
Conformal blocks for Galois covers of algebraic groups
Shrawan Kumar
(joint work with Jiuzu Hong)
