---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-006-8-modifications-in-the-degenerate-case
section_title: "Modifications in the degenerate case"
section_number: 8
pages: 54-57
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
toc_source: inferred
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an oriented link, in the same"
---
Assume in this section that k is a ﬁeld of characteristic p ≥0. As we have said
already in the introduction, when z = 0, the category OS(z, t) should be replaced with
the oriented Brauer category OB(δ) studied in [BCNR].
Proof of Theorem 1.10. This follows by the same general argument as used to prove
Theorem 1.3 (also Remark 3.4). Instead of the quantized Schur-Weyl duality used
before, one uses classical Schur-Weyl duality in its “characteristic free” form established
in [CP, Theorems 4.1–4.2].
□
Now we discuss the degenerate analog of the results in sections 5, 6 and 7.
For section 5, we work with the locally ﬁnite-dimensional locally unital algebra
OB =
M
a,b∈⟨↑,↓⟩
1aOB1b
where
1aOB1b = HomOB(δ)(b, a).
It has a triangular decomposition
OB ∼= OB+ ⊗K OB0 ⊗K OB−
like in Lemma 5.1. This actually becomes easier since there is no longer any need to
be careful about upward strands passing underneath downward strands when deﬁning
OB0. The subsequent arguments in section 5 then go through easily on replacing the
Hecke algebra Hr with the group algebra kSr of the symmetric group and e with p.
The results in section 6 go through too, but this needs a little more work since the
deﬁnitions of the various Jucys-Murphy elements from (4.9), (6.2) and (6.13)–(6.14)
need some modiﬁcations, and the details in the proofs of Lemmas 6.4 and 6.7 then
need to be rechecked carefully. The aﬃne Hecke algebra AHr becomes the degenerate
aﬃne Hecke algebra dAHr whose polynomial generators x1, . . . , xr satisfy the relations
xixj = xjxi,
sixi+1 = xisi + 1
(8.1)
in place of (4.1). The unique homomorphism dAHr ։ kSr sending si 7→si and x1 7→0
sends xr to the Jucys-Murphy element
lr :=
r−1
X
i=1
(i r) ∈kSr.
(8.2)
These elements are the replacements for (6.2).
Then the contents of nodes of an
ordinary Young diagram (which should always be interpreted as elements of the ﬁeld
k) are as in the following example
0
1
2
3
4
−1
0
1
−2
−1
.
In place of (6.3), we set
Ic := {c + n | n ∈Z} ⊆k
(8.3)
for c ∈k. The appropriate analog of Lemma 6.1 uses I0 ⊆k in place of I1 ⊆k×. It is
a classical result in the (modular) representation theory of the symmetric group.
The Jucys-Murphy elements of OB(δ) are the images of corresponding elements of
the aﬃne oriented Brauer category AOB(δ) introduced in [BCNR]. This strict k-linear
ORIENTED SKEIN CATEGORY
55
monoidal category is deﬁned by by adjoining an additional generating morphism
•
to OB(δ), subject to the relation (dA) from Figure 1. The analog of Lemma 4.2 is
explained in [BCNR, Theorem 3.3]: there is a k-linear functor β : AOB(δ) →OB(δ)
sending diagrams with no dots to the same diagrams in OB(δ), and sending
• 7→0.
The following computes the image of
• (which is deﬁned so that (4.3)–(4.4) hold):
• =
•
=
• −
7→−δ .
Then we deﬁne x(b) ∈HomOB(δ)(b, b) in the same way as (4.10) for any ∅̸ = b ∈⟨↑, ↓⟩.
There is no longer such a nice diagrammatic interpretation of these elements like (4.9),
but there is a recursive deﬁnition as in (4.11)–(4.12): we have that x(↑) = 0, x(↓) =
−δ1↓, and
x(↑↑b) :=
x(↑b)
b
b
+
b
,
x(↑↓b) :=
x(↑b)
b
b
−
b
,
(8.4)
x(↓↓b) :=
x(↓b)
b
b
−
b
,
x(↓↑b) :=
x(↓b)
b
b
+
b
,
(8.5)
for any word b. Finally, the Jucys-Murphy elements x◦(b) of OB◦(δ), i.e., the subcat-
egory consisting of all objects but only morphisms represented by diagrams with no
cups or caps, are deﬁned from x◦(↑) := 0, x◦(↓) := −δ1↓, and
x◦(↑↑b) :=
x◦(↑b)
b
b
+
b
,
x◦(↑↓b) :=
x◦(↑b)
b
b
,
(8.6)
x◦(↓↓b) :=
x◦(↓b)
b
b
−
b
,
x◦(↓↑b) :=
x◦(↓b)
b
b
.
(8.7)
We leave it to the reader to verify with these new deﬁnitions that Lemmas 6.4 and 6.7
go through; see also [Re]. In the statement of Lemma 6.4, one should replace t−2i−1
with −i −δ, I1 with I0, and It−2 with I−δ. Also the set I from (6.27) becomes
I := I0 ∪I−δ = {n, −n −δ | n ∈Z} ⊆k.
(8.8)
Adjusting the subsequent combinatorics in analogous ways, all of the other results of
section 6 follow as before.
Moving on to section 7, the Lie algebra g is the Kac-Moody algebra associated to
the Cartan matrix (ci,j)i,j∈I deﬁned by (1.22). The module V (−Λ1|Λt−2) becomes
V (−Λ0|Λ−δ), and the degenerate analogs of (8.9)–(8.10) are
wt↑(λ) := −Λ0 +
X
A∈λ↑
αcont(A),
(8.9)
wt↓(λ) := Λ−δ −
X
A∈λ↓
α−cont(A)−δ, .
(8.10)
56
J. BRUNDAN
There are no other signiﬁcant discrepancies.
Proof of Theorem 1.11. This is the same as the proof of Theorem 1.9 given in the
previous section.
□
References
[A]
S. Ariki, On the decomposition numbers of the Hecke algebra of G(m, 1, n), J. Math.
Kyoto Univ. 36 (1996), 789–808.
[BGHL]
A. Beliakova, Z. Guliyev, K. Habiro and A. Lauda, Trace as an alternative decategoriﬁ-
cation functor, Acta Math. Vietnam 39 (2014), 425–480.
[BHLW]
A. Beliakova, K. Habiro, A. Lauda and B. Webster, Current algebras and categoriﬁed
quantum groups, J. Lond. Math. Soc. 95 (2017), 248–276.
[BT]
G. Bellamy and U. Thiel, Highest weight theory for ﬁnite-dimensional graded algebras
with triangular decomposition; arXiv:1705.08024v2.
[B]
J. Brundan, On the deﬁnition of q-Heisenberg category, in preparation.
[BCNR]
J. Brundan, J. Comes, D. Nash and A. Reynolds, A basis theorem for the aﬃne oriented
Brauer category and its cyclotomic quotients, Quantum Topology 8 (2017), 75–112.
[BD]
J. Brundan and N. Davidson, Categorical actions and crystals, Contemp. Math. 684
(2017), 116–159.
[BK]
J. Brundan and A. Kleshchev, Blocks of cyclotomic Hecke algebras and Khovanov-Lauda
algebras, Invent. Math. 178 (2009), 451–484.
[BS]
J. Brundan and C. Stroppel, Gradings on walled Brauer algebras and Khovanov’s arc
algebra, Advances Math. 231 (2012), 709–773.
[CKM]
S. Cautis, J. Kamnitzer and S. Morrison, Webs and quantum skew Howe duality, Math.
Ann. 360 (2014), 351–390.
[CR]
J. Chuang and R. Rouquier, Derived equivalences for symmetric groups and sl2-
categoriﬁcation, Ann. Math. 167 (2008), 245–298.
[CW]
J. Comes and B. Wilson, Deligne’s category Rep GLδ and representations of general linear
supergroups, Represent. Theory 16 (2012), 568–609.
[CP]
C. de Concini and C. Procesi, A characteristic free approach to invariant theory. Advances
Math. 21 (1976), 330–354.
[De]
P. Deligne, La cat´egorie des repr´esentations du group sym´etrique St, lorsque t n’est pas
un entier naturel, in : “Algebraic groups and homogeneous spaces,” Tata Inst. Fund. Res.
Stud. Math., pp. 209–273, Mumbai (2007).
[DM]
P. Deligne and J. Milne, Tannakian categories, Hodge cycles, motives, and Shimura vari-
eties, Lecture Notes Math. 900 (1982), 101-228.
[DJ1]
R. Dipper and G. James, Representations of Hecke algebras of general linear groups, Proc.
London Math. Soc. 52 (1986), 20–52.
[DJ2]
, Blocks and idempotents of Hecke algebras of general linear groups, Proc. London
Math. Soc. 54 (1987), 57–82.
[Do]
S. Donkin, On tilting modules for algebraic groups, Math. Z. 212 (1993), 39–60.
[DPS]
J. Du, B. Parshall and L. Scott, Quantum Weyl reciprocity and tilting modules, Commun.
Math. Phys. 195 (1998) 321–352.
[EL]
B. Elias and I. Losev, Modular representation theory in type A via Soergel bimodules;
arXiv:1701.00560v1.
[EW]
B. Elias and G. Williamson, Soergel calculus, Represent. Theory 20 (2016), 295–374.
[E]
I. Entova-Aizenbud,
Categorical actions and multiplicities in the Deligne category
Rep GLt; arXiv:1607.04341v1.
[EHS]
I. Entova-Aizenbud, V. Hinich and V. Serganova, Deligne categories and the limit of
categories Rep(GL(m|n)); arXiv:1511.07699v2.
[EGNO]
P. Etingof, S. Gelaki, D. Nikshych and V. Ostrik, Tensor Categories, Amer. Math. Soc.,
2015.
[HOMFLY] P. Freyd, D. Yetter, J. Hoste, W. B. R. Lickorish, K. Millet and A. Ocneanu, A new
polynomial invariant of knots and links, Bull. Amer. Math. Soc. 12 (1985) 239–246.
[Ge]
M. Geck, The character table of the Iwahori-Hecke algebra of the symmetric group:
Starkey’s rule, C. R. Acad. Sci. Paris 329 (1999), 361–366.
[H]
M. H¨arterich, Murphy bases of generalized Temperley-Lieb algebras, Arch. Math. 72
(1999), 337–345.
[HN]
R. Holmes and D. Nakano, Brauer-type reciprocity for a class of graded associative al-
gebras, J. Algebra 144 (1991), 117–126.
ORIENTED SKEIN CATEGORY
57
[HM]
J. Hu and A. Mathas, Graded cellular bases for the cyclotomic Khovanov-Lauda-Rouquier
algebras of type A, Advances Math. 225 (2010), 598–642.
[J]
M. Jimbo, A q-analogue of U(gl(N + 1)), Hecke algebra, and the Yang-Baxter equation,
Letters in Math. Phys. 11 (1986), 247–252.
[JK]
J. H. Jung and M. Kim, Supersymmetric polynomials and the center of the walled Brauer
algebra; arXiv:1508.06469v2.
[KL]
M. Khovanov and A. Lauda, A categoriﬁcation of quantum sl(n), Quantum Top. 1 (2010),
1–92.
[Kl]
A. Kleshchev, Linear and Projective Representations of Symmetric Groups, Cambridge
University Press, Cambridge, 2005.
[Ko]
K. Koike, On the decomposition of tensor products of the representations of classical
groups: by means of universal characters, Advances Math. 74 (1989), 57–86.
[KM1]
M. Kosuda and J. Murakami, The centralizer algebras of mixed tensor representations of
Uq(gln) and the HOMFLY polynomial of links, Proc. Japan Acad. 58 (1992), 148–151.
[KM2]
, Centralizer algebras of the mixed tensor representations of quantum group
Uq(gl(n, C)), Osaka J. Math. 30 (1993), 475–507.
[LW]
I. Losev and B. Webster, On uniqueness of tensor products of irreducible categoriﬁcations,
Selecta Math. 21 (2015), 345–377.
[L]
G. Lusztig, Introduction to Quantum Groups, Birkh¨auser, 1993.
[MW]
M. Mackaay and B. Webster, Categoriﬁed skew Howe duality and comparison of knot
homologies; arXiv:1502.06011v1.
[M]
H. Morton, Power sums and HOMFLY skein theory, in: “Invariants of knots and 3-
manifolds (Kyoto, 2001)”, pp. 235–244, Geom. Topol. Monogr. 4, Geom. Topol. Publ.,
Coventry, 2002.
[MS]
H. Morton and P. Samuelson, The HOMFLY-PT skein algebra of the torus and the elliptic
Hall algebra, Duke Math. J. 166 (2017), 800–854.
[PT]
J. Przytycki and P. Traczyk, Invariants of links of Conway type, Kobe J. Math. 4 (1988),
115–139.
[PW]
B. Parshall and J.-P. Wang, Quantum linear groups, Mem. Amer. Math. Soc. 89 (1991),
1–157.
[QS]
H. Queﬀelec and A. Sartori, Mixed quantum skew Howe duality and link invariants of
type A; arXiv:1504.01225v1.
[Ra]
A. Ram, Seminormal representations of Weyl groups and Iwahori-Hecke algebras, Proc.
London Math. Soc. 75 (1997) 99–133.
[Re]
A. Reynolds, Representations of Oriented Brauer Categories, PhD thesis, University of
Oregon, 2015.
[RW]
S.
Riche
and
G.
Williamson,
Tilting
modules
and
the
p-canonical
basis;
arXiv:1512.08296v3.
[Ro]
R. Rouquier, 2-Kac-Moody algebras; arXiv:0812.5023v1.
[SS]
A. Sartori and C. Stroppel, Walled Brauer algebras as idempotent truncations of level 2
cyclotomic quotients, J. Algebra 440 (2015), 602–638.
[T1]
V. Turaev, Conway and Kauﬀman modules of a solid torus, J. Soviet Math. 52 (1990),
2799–2805.
[T2]
, Operator invariants of tangles, and R-matrices, Math. USSR Izvestiya 35 (1990),
411–444.
[T3]
, Quantum Invariants of Knots and 3-Manifolds, De Gruyter Studies in Mathe-
matics 18, De Gruyter, Berlin, 2016.
[TV]
V. Turaev and A. Virelizier, Monoidal Categories and Topological Field Theory, Progress
in Mathematics 322, Birkh¨auser, 2017.
[VV]
M. Varagnolo and E. Vasserot, Canonical bases and KLR-algebras, J. Reine Angew. Math.
659 (2011), 67–100.
[W1]
B. Webster, On graded presentations of Hecke algebras and their generalizations;
arXiv:1305.0599v3.
[W2]
, Canonical bases and higher representation theory, Compositio Math. 151 (2015),
121–166.
[W3]
, Knot invariants and higher representation theory, to appear in Mem. Amer.
Math. Soc., 2017.
Department of Mathematics, University of Oregon, Eugene, OR 97403, USA
E-mail address: brundan@uoregon.edu
