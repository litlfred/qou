---
doc_id: hdr
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-011-families-of-characters-and-rouquier-families
section_title: "Families of characters and Rouquier families"
section_number: null
pages: 29-30
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
doc_brief: "HAL Id: tel-01411063 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 27 sections: Algebras of"
---
Let ϕm :vC,j↦→qmC,j be a cyclotomic specialisation and let Hϕm(W ) be the corresponding cyclotomic
Hecke algebra associated with W . How can we deﬁne families of characters for Hϕm(W )? We cannot
apply Lusztig’s original deﬁnition, because parabolic subgroups of complex reﬂection groups1 do not have
a nice presentation as in the real case, and certainly not a “corresponding” parabolic Hecke algebra. On
the other hand, we do not have a Kazhdan–Lusztig basis forHϕm(W ), so we cannot construct Kazhdan–
Lusztig cells and use them to deﬁne families of characters for complex reﬂection groups in the usual way.
However, we can deﬁne the families of characters to be the Rouquier families of Hϕm(W ), that is, the
blocks ofHϕm(W ) over the Rouquier ring RK(q), where
RK(q) = ZK[q,q−1, (qn− 1)−1
n>1].
By Proposition 1.4, the Rouquier families are the non-empty subsets B of Irr(W ) that are minimal with
respect to the property: ∑
E∈B
ϕm(χE(h))
ϕm(sE) ∈R K(q) ∀h∈H (W ),
where χE and sE are respectively the character and the Schur element of K(v)H(W ) corresponding to
E∈ Irr(W ).
Brou´ e and Kim [BrKi] determined the Rouquier families for the complex reﬂection groups of type
G(l, 1,n ), but their results are only true when l is a power of a prime number or ϕm is a “good”
cyclotomic specialisation (for example, we have shown that their results hold when ϕm is the spetsial
cyclotomic specialisation [Ch3, Proposition 3.20]). The same problem persists, and some new appear,
in the determination of the Rouquier families for G(l,p,n ) by Kim [Kim]. Malle and Rouquier [MalRo]
calculated the Rouquier families for some exceptional complex reﬂection groups and the dihedral groups,
for the spetsial cyclotomic specialisation. More recently, we managed to determine the Rouquier families
for all cyclotomic Hecke algebras of all complex reﬂection groups [Ch1, Ch3, Ch4, Ch5], thanks to their
property of “semicontinuity”. In order to explain this property, we will need some deﬁnitions.
Let M = ∏
C,jvaC,j
C,j be a potentially essential monomial for W . We say that the family of inte-
gers m = (mC,j)(C∈A/W)(0⩽j⩽eC−1) belongs to the potentially essential hyperplane HM (of R
∑
CeC) if∑
C,jmC,jaC,j = 0.
Suppose that m belongs to no potentially essential hyperplane. Then the Rouquier families of
Hϕm(W ) are called Rouquier families associated with no essential hyperplane . Now suppose that m
belongs to a unique potentially essential hyperplane H. Then the Rouquier families of Hϕm(W ) are
unions of the Rouquier families associated with no essential hyperplane and they are called Rouquier
families associated with H. If they do not coincide with the Rouquier families associated with no essen-
tial hyperplane, then H is called an essential hyperplane for W . All these notions are well-deﬁned and
they do not depend on the choice of m because of the following theorem [Ch4, §4.4]:
Theorem 3.10 (Semicontinuity property of Rouquier families) Let m = (mC,j)(C∈A/W)(0⩽j⩽eC−1)
be a family of integers and let ϕm : vC,j↦→ qmC,j be the corresponding cyclotomic specialisation. The
Rouquier families of Hϕm(W ) are unions of the Rouquier families associated with the essential hyper-
planes that m belongs to and they are minimal with respect to this property.
Thanks to the above result, it is enough to do calculations in a ﬁnite number of cases in order to
obtain the families of characters for all cyclotomic Hecke algebras, whose number is inﬁnite.
Example 3.11 ForW = S3, the Rouquier families associated with no essential hyperplane are trivial
(that is, every block is a singleton). The hyperplane HM corresponding to the monomial M =vt,0v−1
t,1 is
essential, and it is the unique essential hyperplane for S3. Let ϕm :vt,j↦→qmj,j = 0, 1, be a cyclotomic
specialisation. We have that m = (m0,m 1) belongs to HM if and only if m0 = m1. There is a single
Rouquier family associated with HM, which contains all irreducible representations of S3.
1The parabolic subgroups of a complex reﬂection group W ⊂ GL(h) are the pointwise stabilisers of the subsets of h. It
is a remarkable theorem by Steinberg [St2, Theorem 1.5] that all parabolic subgroups of W are again complex reﬂection
groups.
26
We have computed the Rouquier families associated with no and each essential hyperplane:
• With the use of GAP3 for all exceptional complex reﬂection groups [Ch4]; the results can be found
on my webpage [Ch-web], while very recently, together with Jean Michel, we programmed the algo-
rithm described in [Ch4] in the GAP3 package CHEVIE (seechevie/contr/rouquierblockdata.g).
• Combinatorially for the groups of type G(l, 1,n ) [Ch3]; we will see more on these results in the
next chapter.
• With the use of Cliﬀord theory for the groups G(l,p,n ), for n >2 or n = 2 and p odd, from the
Rouquier families for G(l, 1,n ) [Ch5].
• Applying the algorithm of [Ch4] for G(l, 2, 2) [Ch5].
• With the use of Cliﬀord theory for the groups G(l,p, 2), for p even, from the Rouquier families for
G(l, 2, 2) [Ch5].
A consequence of the above results is the following:
Proposition 3.12 The Rouquier families associated with no essential hyperplane are trivial if and only
if W =G4 or W is of type G(l, 1,n ).
Note that, by deﬁnition, the Rouquier families associated with an essential hyperplane are not trivial
for any complex reﬂection group.
Now, part of the algorithm used for the determination of the Rouquier families is the easy-to-prove
fact that the function a +A is constant on the Rouquier families (see, for example, [BrKi, Proposition
2.9]). However, we have also managed to show that, similarly to the real case, both functions a and A
are constant on the Rouquier families, for all cyclotomic Hecke algebras of all complex reﬂection groups:
• With the use of GAP3 for all exceptional complex reﬂection groups [Ch2]; the programme used,
Degval.g, is available on my webpage [Ch-web].
• Combinatorially for the groups of type G(l, 1,n ) [BrKi, Ch3].
• With the use of Cliﬀord theory for the groups G(l,p,n ), for n >2 or n = 2 and p odd, from the
analogous result for G(l, 1,n ) [Ch5].
• With explicit calculations for G(l, 2, 2) [Ch5].
• With the use of Cliﬀord theory for the groups G(l,p, 2), for p even, from the analogous result for
G(l, 2, 2) [Ch5].
Finally, we would like to point out that the semicontinuity property of the Rouquier families is part
of the block behaviour of algebras whose Schur elements are of the form (3.3). We have studied the block
theory of this type of algebras, which we call essential algebras, in [Ch4]. Besides generic Hecke algebras
of complex reﬂection groups, another example of essential algebras are the Yokonuma–Hecke algebras
which will be studied in the last chapter.
