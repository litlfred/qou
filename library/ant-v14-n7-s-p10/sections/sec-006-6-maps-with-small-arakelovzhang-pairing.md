---
doc_id: ant-v14-n7-s-p10
doc_title: "Abelian extensions in dynamical Galois theory"
section_id: sec-006-6-maps-with-small-arakelovzhang-pairing
section_title: "Maps with small Arakelov–Zhang pairing"
section_number: 6
pages: 11-13
source_pdf: ant-v14-n7-s-p10.pdf
source_sha256: 8d3e47aa779ad9c7
doc_brief: "Abelian extensions in dynamical Galois theory — 11 sections: Introduction; Some algebraic lemmas; Ramiﬁcation and postcritically inﬁ"
---
We now describe how to extend the ideas used in the proof of Theorem 12 to treat polynomials which
are not necessarily K -conjugate to powering maps, but which are K ab-conjugate to some polynomial
φ(x)∈ K[x] that is arithmetically close to a powering map.
We ﬁrst recall the deﬁnitions of several arithmetic-dynamical objects associated to a polynomial
φ(x)∈ K[x] of degree d≥ 2 deﬁned over a number ﬁeld K ; see [Silverman 2007, Sections 3.4–3.5] for
further details. The Call–Silverman canonical height functionˆhφ: K→ R may be deﬁned by the limit
ˆhφ(x)= lim
n→+∞
h(φn(x))
dn
and can be characterized by the identityˆhφ(φ(x))= dˆhφ(x) together with the fact that h−ˆhφ is bounded
on K . Locally, given a ﬁnite extension L/K , for each place v∈ ML deﬁne the canonical local height
1992 Jesse Andrews and Clayton Petsche
function by
λφ,v: Cv→ R, λ φ,v(x)= lim
n→+∞
1
dn log+|φn(x)|v. (10)
Then an alternative expression for the canonical height is given by
ˆhφ(α)=
∑
v∈ML
rvλφ,v(α), (11)
for allα∈ L, a formula which may be viewed as analogous to (5).
For each placev∈ MK , standard arguments show thatλφ,v(x)≥ 0 for all x∈ Cv, with equality if and
only if x is in the ﬁlled Julia set
Fφ,v={ x∈ Cv||φn(x)|v is bounded as n→+∞}
associated toφ. The canonical measureµφ,v associated toφ is aφ-invariant unit Borel measure supported
on Fφ,v which describes the limiting distribution of preperiodic points and iterated inverse images with
respect toφ. There are several equivalent constructions of this measure in the literature; see [Freire et al.
1983; Ljubich 1983] in the Archimedean case and [Baker and Rumely 2006; Chambert-Loir 2006; Favre
and Rivera-Letelier 2006] in the non-Archimedean case. (Technically, when v is a non-Archimedean
place, the objectsλφ,v , Fφ,v , andµφ,v need to be interpreted on the Berkovich afﬁne line A1
v. We will
not need to go into these details in the present paper.)
Given two polynomialsφ(x),ψ( x)∈ K[x] of degree at least two, the Arakelov–Zhang pairing can be
deﬁned by either of the two expressions
⟨φ,ψ⟩=
∑
v∈MK
rv
∫
λφ,v dµψ,v=
∑
v∈MK
rv
∫
λψ,v dµφ,v. (12)
Thus⟨φ,ψ⟩ is a nonnegative real number, and in some sense it measures the global arithmetic-dynamical
distance between the two maps. This pairing was originally deﬁned as a limit of arithmetic intersection
products by Zhang [1995], and described analytically using Berkovich spaces by Petsche, Szpiro and
Tucker [Petsche et al. 2012]. For our purposes the most important fact about the Arakelov–Zhang pairing
is that it is closely related to points which have small canonical height with respect to one of the two
maps. In particular, it was shown in [Petsche et al. 2012] that if {αn} is a sequence of distinct points in K
withˆhφ(αn)→ 0, thenˆhψ(αn)→⟨φ,ψ⟩.
In the special case ψ(x)= xd for d≥ 2, the canonical heightˆhψ is the same as the usual Weil height
h,λψ,v(·)= log+|·|v, Fψ,v is the closed unit disc, and µψ,v is equal to the normalized Haar measure
supported on the unit circle of Cv= C whenv is Archimedean, and equal to the Dirac measure supported
at the Gauss point of A1
v whenv is non-Archimedean. In particular, the value of the pairing⟨φ, xd⟩ does
not depend on d.
Abelian extensions in dynamical Galois theory 1993
Theorem 14. Letφ(x)∈ K[x] be a polynomial of degree d≥ 2 deﬁned over K such that⟨φ, xd⟩> 0,
and letα be a nonexceptional point forφ. If K∞(φ,α)⊆ L⊆ K , then
B0(L)≤⟨φ, xd⟩. (13)
Proof. For each n≥ 1, let αn∈ K∞⊆ L satisfyφn(αn)=α; since α is not an exceptional point we
may assume that the αn are distinct. It follows from properties of the canonical height that ˆhφ(αn)=
ˆhφ(α)/dn→ 0 as n→+∞ . By Theorem 1 of [Petsche et al. 2012], it follows that h(αn)→⟨φ, xd⟩> 0,
and (13) follows from the deﬁnition of B0(L). □
As a sample application of Theorem 14, we can show that for any number ﬁeld K , a certain inﬁnite
family of polynomials satisﬁes the Conjecture.
Corollary 15. For each number ﬁeldK , there exists a constantCK such that Gal(K∞((x p−x)/p,α)/ K)
is nonabelian over K for allα∈ K and all primes p≥ CK . In particular, Gal(K∞((x p− x)/p,α)/ Q) is
nonabelian for allα∈ Q and all p≥ 29.
Proof. It has been shown by Petsche and Stacy [2019] that⟨(x p− x)/p, xd⟩= log p/(p− 1). Thus if
K∞((x p− x)/p,α)⊆ K ab, Theorem 14 implies that B0(K ab)≤ log p/(p− 1). But since B0(K ab)> 0
[Amoroso and Zannier 2000], we have a contradiction for large enough p. In particular, it was shown by
Amoroso and Dvornicich [2000] that B0(Qab)≥(log 5)/12, which exceeds log p/(p−1) once p≥ 29. □
We remark that, according to the Conjecture, we expect thatGal(K∞((x p− x)/p,α)/ K) is nonabelian
for all number ﬁelds K , allα∈ K , and all primes p.
