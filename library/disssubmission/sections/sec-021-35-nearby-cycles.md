---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-021-35-nearby-cycles
section_title: "Nearby cycles"
section_number: 3.5
pages: 62-66
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
To describe the behaviour of the above Tannaka groups with respect to
degenerations, we work over the spectrum S of a strictly Henselian discrete
valuation ring with closed point s and generic point η. We assume that the
prime l is invertible on S. Fix a geometric point η over η, and denote by S
the normalization of S in the residue ﬁeld of η.
Let X →S be a semiabelian scheme, i.e. a smooth commutative group
scheme over S whose ﬁbres Xs and Xη are semiabelian varieties. In what
follows we always assume the generic ﬁbre Xη is an abelian variety. We
put X = X ×S S and write Xs = Xs and Xη for its geometric ﬁbres.
Xs
i
/
uuuuu
uuuuu
X
{vvvvv
Xη
j
o

ysssss
Xs

i
/

X


Xη

j
o
s
ssssss
ssssss
/ S
zttttt
o
η
xrrrrrr
s
/ S
η
o
Degenerations of constructible sheaves can in this setting be studied via the
functor of nearby cycles [32, exp. XIII-XIV]
Ψ :
D(Xη) −→D(Xs),
Ψ(K) = i∗(R j∗(K)).
By [60, th. 4.2 and cor. 4.5] this functor commutes with Verdier duality and
restricts to an exact functor between the abelian categories P(Xη) and P(Xs)
of perverse sheaves. However, the following example illustrates that unlike
for abelian schemes, in the case of semiabelian schemes the functor Ψ in
general does not preserve the Euler characteristic.
3.5. Nearby cycles
55
EXAMPLE 3.12. For n ∈N consider the kernel X[n] of the multiplication
morphism [n] : X −→X. This kernel is a quasi-ﬁnite group scheme over S
and decomposes as a disjoint union
X[n] = Y ⨿Z
where Y is ﬁnite over S and where Z ∩Xs = ∅. In general Z̸ = ∅, but the
perverse skyscraper sheaf
δZη ∈P(Xη)
satisﬁes
Ψ(δZη) = 0
since the support of the nearby cycles must be contained in Z ∩Xs = ∅.
For the rest of this section we will always assume that for all geometric
points t of S the ﬁbre Xt satisﬁes the generic vanishing assumption GV(Xt)
from section 3.1. We can then consider the quotient categories
D(Xt) = D(Xt)/T(Xt)
and
P(Xt) = P(Xt)/S(Xt)
as deﬁned in section 3.4. Note that the Euler characteristic is well-deﬁned
on objects of these quotient categories.
LEMMA 3.13. The functor Ψ descends to a functor Ψ : P(Xη) →P(Xs),
for all P,Q ∈P(Xη) we have
0 ≤χ(Ψ(P)) ≤χ(P),
(i)
0 ≤χ(Ψ(P)∗Ψ(Q)) ≤χ(Ψ(P∗Q)),
(ii)
and Ψ(P)∗Ψ(Q) is a direct summand of Ψ(P∗Q) in the category P(Xs).
Proof. We begin with some preliminary remarks. Let f : Y →Z be a
homomorphism of semiabelian S-schemes. By abuse of notation we again
write f for any base change of it. Consider for Y = Y ×S S and Z = Z ×S S
the commutative diagram
Ys
i
/
f

Y
f

Yη
j
o
f

Zs
i
/ Z
Zη
j
o
over S. For K ∈D(Y) this gives a commutative diagram
i∗(Rf!(K))
bc!
/
α

Rf!(i∗(K))
β

i∗(Rf∗(K))
bc∗
/ R f∗(i∗(K))
56 Chapter 3 — Perverse sheaves on semiabelian varieties

where a@ and B denote the forget support morphisms and where bc; and bc,.
are the base change morphisms. Let us briefly recall how these latter two
are defined — the direct image of the adjunction morphism K —> i, (i*(K))
yields two morphisms

Rfi(K) — Rfilis@(K))) = i(RAGT(K))),

Rf(K) —> Rfs(ie@(K))) = ie(Rfe(F(K))),
and again by adjunction these give rise to the base change morphisms bc,
and bc, from above. We also remark [7, exp. XVII, th. 5.2.6] that as a
result of the proper base change theorem, the base change morphism bc, is

always an isomorphism. Putting K = Rj,(L) with L € D(¥q), we obtain a
factorization

Rfi(Py(L)) p Rf.(Yy(L))
obo a
Wz(Rf(L))

where Py and ‘Pz denote the nearby cycles for Y + S resp. Z + S. We will
apply this in the following two situations.

First we take f : X — S to be the structure morphism with Y= X,Z=S
and L = P. In this case the above diagram more explicitly says that the
forget support morphism f for the cohomology of the nearby cycles Y(P)
admits the following factorization.

H2(X,,¥(P)) H*(Xs,'P(P))

Ne

H*(Xq,P)

Now consider a character y of the tame fundamental group of X, and denote
by % € II(X;) its pull-back to the fibre X, over the special point t = s or over
the geometric generic point t = 7). The projection formula (see section 3.6)
implies that we have
WP (Py) = (L(P))x

for any such character. In lemma 3.16 we will see that 7 can be chosen in
such a way that the characters 7; and 7 are both generic. By the generic
vanishing axiom GV(X;) we can therefore assume that the forget support
morphism f is an isomorphism, in which case the above factorization shows
that H*(X,,P(P)) is a direct summand of H*(X,,P). Furthermore, by the
generic vanishing axiom GV (X;) we can also assume that all the occuring
hypercohomology groups are concentrated in cohomology degree zero, in
which case it follows that 0 < 7(‘¥(P)) < x(P). In particular, the nearby
3.5. Nearby cycles
57
cycles functor Ψ then sends the Serre subcategory S(Xη) ⊂P(Xη) into the
Serre subcategory S(Xs) ⊂P(Xs) and hence induces a functor
Ψ : P(Xη) −→P(Xs)
between the quotient categories. The property (i) of Ψ is inherited from the
corresponding estimate for Ψ shown above.
Secondly we take f = m to be the group law, with Y = X ×k X, Z = X
and L = P⊠Q. In D(Xs) we can identify ΨZ(Rf∗(L)) with Ψ(P∗Q). Since
by [60, th. 4.7] the exterior tensor product ⊠commutes with nearby cycles,
we can also identify Rf∗(ΨY(L)) with Ψ(P)∗Ψ(Q). Then the factorization
of β from above shows that the nearby cycles Ψ(P∗Q) admit Ψ(P)∗Ψ(Q)
as a direct summand in P(Xs). Hence (ii) follows.
□
In general we cannot expect Ψ to be a tensor functor since it does not
preserve the Euler characteristic (see example 3.12). In what follows we
will call a perverse sheaf P on Xη admissible if
χ(Ψ(P)) = χ(P).
Note that for an abelian scheme X →S every perverse sheaf is admissible
since the nearby cycles are compatible with proper morphisms.
LEMMA 3.14. The admissible objects form a rigid symmetric monoidal
full abelian subcategory
P(Xη)ad ⊂P(Xη)
which is stable under the formation of extensions and subquotients.
Proof. Any short exact sequence 0 →P1 →P2 →P3 →0 in P(Xη) is
mapped under the nearby cycles functor to a short exact sequence in the
category P(Xs). Then in particular
χ(P2) = χ(P1)+ χ(P3)
and
χ(Ψ(P2)) = χ(Ψ(P1))+ χ(Ψ(P3))
because the Euler characteristic is additive in short exact sequences. But on
the other hand χ(Pi) ≥χ(Ψ(Pi)) for i = 1,2,3 by lemma 3.13 (i). Hence it
follows that
χ(Pi) = χ(Ψ(Pi))
holds for i = 2 iff it holds for i = 1 and i = 3.
In other words, the perverse sheaf P2 is admissible if and only if both P1
and P3 are admissible. So the category of admissible objects is stable under
the formation of extensions and subquotients.
58
Chapter 3 – Perverse sheaves on semiabelian varieties
It remains to show that for admissible P1,P2 ∈P(Xη) also P1 ∗P2 is
admissible. This follows from
χ(P1 ∗P2) = χ(P1)· χ(P2)
(part (d) of lemma 3)
= χ(Ψ(P1))· χ(Ψ(P2))
(admissibility of P1, P2)
= χ(Ψ(P1)∗Ψ(P2))
(part (d) of lemma 3)
≤χ(Ψ(P1 ∗P2))
(part (ii) of lemma 12)
≤χ(P1 ∗P2)
(part (i) of lemma 12)
which implies that the last two estimates must in fact be equalities.
□
Concerning the failure of tensor functoriality it now follows that the
situation is as good as one could possibly hope for.
THEOREM 3.15. On the rigid symmetric monoidal abelian subcategory
of admissible objects, the nearby cycles deﬁne a tensor functor ACU
Ψ :
P(Xη)ad −→P(Xs)
so that for P ∈Pad
η we obtain a closed immersion G(Ψ(P)) ,→G(P).
Proof. Let P1,P2 ∈P(Xη)ad. The last statement in lemma 3.13 (ii) gives
a split monomorphism
Ψ(P1)∗Ψ(P2) ,→Ψ(P1 ∗P2)
in the abelian category P(Xs). But χ(Ψ(P1)∗Ψ(P2)) = χ(Ψ(P1 ∗P2)) as we
have seen in the proof of lemma 3.14. So the above monomorphism is an
isomorphism in P(Xs), and hence Ψ is a tensor functor on P(Xη)ad. For the
statement about the Tannaka groups, recall that by deﬁnition every object
of ⟨Ψ(P)⟩is a subquotient of the image under Ψ of some object in ⟨P⟩. So
our claim follows from the Tannakian formalism [33, prop. 2.21b)].
□
