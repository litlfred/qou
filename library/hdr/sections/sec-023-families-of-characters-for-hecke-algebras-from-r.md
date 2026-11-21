---
doc_id: hdr
doc_title: "Hecke algebras, generalisations and representation theory"
section_id: sec-023-families-of-characters-for-hecke-algebras-from-r
section_title: "Families of characters for Hecke algebras from rational Cherednik algebras"
section_number: null
pages: 45-48
source_pdf: HDR.pdf
source_sha256: 35c190fd2d2a393c
toc_source: outline
doc_brief: "Hecke algebras, generalisations and representation theory — 31 sections: Front matter; Algebras of Finite Type; Blocks"
---
Families of characters for Hecke algebras from rational Chered-
nik algebras
Since the algebra H0,c is ﬁnite dimensional, we can deﬁne its blocks in the usual way. Let E, E′ ∈Irr(W).
Following [GoMa], we deﬁne the Calogero–Moser partition of Irr(W) to be the set of equivalence classes
of Irr(W) under the equivalence relation:
E ∼CM E′ if and only if L(E) and L(E′) belong to the same block of H0,c.
We will simply write CMc-partition for the Calogero–Moser partition of Irr(W). Using the classiﬁcation
of irreducible complex reﬂection groups (see Theorem 3.1), Bellamy has shown the following [Bel1,
Theorem 1.1]:
Theorem 5.20 Let W be an irreducible complex reﬂection group.
The CMc-partition is trivial for
generic values of c if and only if W is of type G(l, 1, n) or G4.
Remark 5.21 The cases where the CMc-partition is trivial for generic values of c are exactly the cases
where the space (h ⊕h∗)/W admits a symplectic resolution.
5.4.1
The Calogero–Moser partition and Rouquier families
It just so happens that the cases where Xc(W) is generically smooth, and the Calogero–Moser partition
generically trivial, are exactly the cases where the Rouquier families are generically trivial (that is, the
Rouquier families associated with no essential hyperplane are singletons). This, combined with the fact
that the Calogero–Moser partition into blocks enjoys some property of semicontinuity, led to the question
whether there is a connection between the two partitions.
The question was ﬁrst asked by Gordon and Martino [GoMa] in terms of a connection between the
Calogero–Moser partition and families of characters for type Bn. In their paper, they computed the
CMc-partition, for all c, for complex reﬂection groups of type G(l, 1, n) and showed that for l = 2,
using the conjectural combinatorial description of Kazhdan–Lusztig cells for type Bn by [BGIL], the
CMc-partition coincides with the partition into Kazhdan–Lusztig families. After that, Martino [Mart]
compared the combinatorial description of the CMc-partition for type G(l, 1, n) given in [GoMa] with
the description of the partition into Rouquier families, given by [Ch3], for a suitable cyclotomic Hecke
algebra Hc of G(l, 1, n) (diﬀerent from the one deﬁned in §5.1.3). He showed that the two partitions
coincide when l is a power of a prime number (which includes the cases of type An and Bn), but not
in general. In fact, he showed that the CMc-partition for G(l, 1, n) is the same as the one obtained by
[BrKi]. He thus obtained the following two connections between the CMc-partition and the partition
into Rouquier families for G(l, 1, n), and he conjectured that they hold for every complex reﬂection group
W [Mart, 2.7]:
(a) The CMc-partition for generic c coincides with the generic partition into Rouquier families (both
being trivial for W = G(l, 1, n));
(b) The partition into Rouquier families reﬁnes the CMc-partition, for all choices of c; that is, if E, E′ ∈
Irr(W) belong to the same Rouquier family of Hc, then E ∼CM E′.
Conditions (a) and (b) are known as “Martino’s Conjecture”. Using the combinatorics of [GoMa]
and [Mart], Bellamy computed the CMc-partition, for all c, and proved Martino’s conjecture in the case
where W is of type G(l, p, n) [Bel2]; note that when p > 1 the generic partitions in this case are not trivial.
However, a counter-example for (a) was found by Thiel [Th] in the case where W = G25. Thiel calculated
the CMc-partition for generic c for the exceptional complex reﬂection groups G4, G5, G6, G8, G10, G23 =
H3, G24, G25 and G26. Comparing his results with the generic partition into Rouquier families for these
groups, given by [Ch4], he showed that Part (a) of Martino’s Conjecture holds in every case1 except for
when W = G25. In this particular case, the generic partition into Rouquier families simply reﬁnes the
CMc-partition for generic c. So we will state here as a conjecture only Part (b) of Martino’s conjecture,
which is still an open problem, and proved in all the above cases.
1for G4 this was already known by [Bel1].
42
Conjecture 5.22 (Martino’s Conjecture) Let W be a complex reﬂection group. The partition into
Rouquier families (for a suitably chosen cyclotomic Hecke algebra Hc of W) reﬁnes the CMc-partition,
for all choices of c; that is, if E, E′ ∈Irr(W) belong to the same Rouquier family of Hc, then E ∼CM E′.
Remark 5.23 Note that, in all the cases checked so far where W is a ﬁnite Coxeter group, the partition
into Rouquier families and the CMc-partition coincide. This covers the ﬁnite Coxeter groups of types
An, Bn, Dn and the dihedral groups for all choices of c, and H3 for generic c.
5.4.2
The Calogero–Moser partition and Kazhdan–Lusztig cells
In an eﬀort to develop a generalised Kazhdan–Lusztig cell theory, Bonnaf´e and Rouquier [BoRo1, BoRo2]
used the Calogero–Moser partition to deﬁne Calogero–Moser cells for all complex reﬂection groups. An
advantage of this, quite geometric, approach is that the Calogero–Moser partition exists naturally for all
complex reﬂection groups. It also implies automatically the existence of a semicontinuity property for
cells, a property that was conjectured and proved in some cases for Kazhdan–Lusztig cells by Bonnaf´e
[Bo2]. However, Calogero–Moser cells are very hard to compute and their construction depends on an
“uncontrollable” choice. After very long computations, it has been conﬁrmed that the Calogero–Moser
cells coincide with the Kazhdan–Lusztig cells for some ﬁnite Coxeter groups of rank 2: the Weyl groups
A2, B2, G2 [BoRo1] and the dihedral groups I2(m) with m odd [Bo3]; there is still a lot of work that
needs to be done.
43
44
Chapter 6
