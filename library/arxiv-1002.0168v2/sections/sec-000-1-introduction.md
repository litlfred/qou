---
doc_id: arxiv-1002.0168v2
doc_title: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1002.0168v2.pdf
source_sha256: c95d5d193d57b097
doc_brief: "Non-cyclotomic fusion categories Scott Morrison Noah Snyder — Etingof, Nikshych and Ostrik ask in [ 7,§2] if every fusion category can be completely deﬁned over a cyclotomic ﬁeld."
---
In [7,§2], Etingof, Nikshych and Ostrik ask if every fusion category over the complex
numbers can be deﬁned over a cyclotomic ﬁeld. More precisely, does every fusion
category over C have a complete rational form over a cyclotomic ﬁeld? (See Section
2 for deﬁnitions and examples of the key notions “rational form” and “complete
rational form.”)
Their question is motivated by the following results.
• The representation category of any ﬁnite group has a complete rational form
over a cyclotomic ﬁeld. (This is a classical result of Brauer’s, see [25, §12.3].)
• The semisimpliﬁed representation category of any quantum group at a root of
unity has a complete rational form over a cyclotomic ﬁeld. (This follows from
the usual construction of Weyl modules.)
• The Frobenius-Perron dimension of any object in a fusion category is a cyclo-
tomic integer [7].
• The global dimension of a fusion category is a cyclotomic integer [7].
• The entries of the S-matrix of a modular category lie in a cyclotomic ﬁeld
[5, 6].
We answer this question in the negative.
Theorem 1.1 The principal even part of the Haagerup subfactor and the principal
even part of the extended Haagerup subfactor are fusion categories which do not
have a complete rational form over any cyclotomic ﬁeld.
1
arXiv:1002.0168v2  [math.QA]  2 May 2010
We hope that this result will eventually allow a more robust technique for establishing
the “exotic” nature of these fusion categories. No construction that preserves
cyclotomicity can produce these fusion categories starting from groups or quantum
groups. Alternately this result might suggest new techniques for constructing these
fusion categories.
LetH0 andH1 be the Haagerup [1, 22] and extended Haagerup [ 2] subfactors which
are the unique subfactors with the following principal graph pairs.
Γ(H0) =



,



Γ(H1) =



,



Given a subfactor A⊂B there are two tensor categories Sp andSd (consisting of
certain A-A bimodules and certain B-B bimodules respectively) called the principal
even part and dual even part. If the subfactor is ﬁnite depth then Sp andSd are
fusion categories over C. We will be looking at the fusion categories Hp
𝓁 andHd
𝓁 for
𝓁∈{ 0, 1}.
Denote by D0 = 5+
√
13
2 ≃ 4.30278 and D1 = 8
3 + 2
3 Re 3
√
13
2
(
−5− 3i
√
3
)
≃ 4.3772
the Jones indices of H0 andH1. Fix
λ0 =i
√
−1 +
√
13
6 ≃ 0.658983i
and
λ1 =
vuu√−1
5 + 2 Re
3
√
117− 65i
√
3
2250 ≃ 0.648585i.
Let ζm denote the primitive mth root of unity exp(2πi/m). Note that
D0 = 2−ζ2
13−ζ5
13−ζ6
13−ζ7
13−ζ8
13−ζ11
13
D1 = 3 +ζ2
13 +ζ3
13 +ζ10
13 +ζ11
13
so D𝓁∈ Q(ζ13) while λ𝓁 is not cyclotomic. In fact, Q(λ𝓁) is not Galois. The Galois
group of the Galois closure of Q(λ0) is the dihedral group of order 8, and the Galois
group of the Galois closure of Q(λ1) is Z/2Z≀ Z/3Z∼= Z/2Z×A4.
Theorem 1.2 The following statements hold for 𝓁 = 0, 1.
(1) The even partsHp
𝓁 andHd
𝓁 each have a (possibly incomplete) rational form
over Q(D𝓁).
(2) The dual even part Hd
𝓁 has a complete rational form over k if and only if
D𝓁∈k.
2
(3) The principal even part Hp
𝓁 has a complete rational form over k if and only if
λ𝓁∈k.
(4) The Drinfel’d center Z(Hp
0)∼=Z(Hd
0) has a complete rational form over k as
a ribbon fusion category if and only if ζ39∈k.
Theorem 1.1 follows immediately from part 3 of Theorem 1.2. Part 4 is of interest
because it means these results do not exclude the possibility that every braided fusion
category is deﬁned over a cyclotomic ﬁeld. We prove part 1 and the “if” direction
of parts 2 and 3 in Section 3. We prove the “only if” direction of parts 2 and 3 in
Section 4. We prove part 4 in Section 5.
The main technique in this paper is to show that, in the context of fusion cate-
gories associated to 3-supertransitive subfactors, the (correctly normalized) “twisted
moments” of any Q-linear combination of projections gives an element of the base
ﬁeld of any complete rational form. These twisted moments can be computed using
techniques from Jones’s preprint [ 15]. In the construction of the Haagerup subfactor
by Peters [22], the moments and twisted moments of the “generator” are the only
scalars needed to deﬁne the subfactor. The λ𝓁 above are Q(D𝓁) multiples of the
third twisted moments of 1
2 (1P− 1Q) (where P and Q are the two simple objects
immediately after the branch).
There is a third subfactor with index in the interval (2 , 3 +
√
3) called the Asaeda-
Haagerup subfactor [1]. Our techniques do not give an obstruction to cyclotomicity
for either of the fusion categories coming from the Asaeda-Haagerup subfactor,
because the analogous moments and twisted moments are cyclotomic. However, since
there is not yet a construction of the Asaeda-Haagerup planar algebra following the
Jones-Peters approach [15, 22, 2], the lack of obstruction does not guarantee that
the even parts of the Asaeda-Haagerup subfactor are cyclotomic.
The authors would like to thank Emily Peters for teaching us about the Haagerup
planar algebra and Pavel Etingof for encouraging us to write this paper. We’d like
to thank Victor Ostrik, Ben Webster, and Pasquale Zito for suggesting arguments
which we used to improve Section 5. (For Pasquale Zito’s suggestions, see Math
Overﬂow http://mathoverflow.net/questions/17641/.) In addition we would
also like to thank Stephen Bigelow, Vaughan Jones, Dmitri Nikshych, and Dylan
Thurston for helpful conversations. Scott Morrison was at the Miller Institute for
Basic Research at UC Berkeley during this work, and Noah Snyder was supported
by an NSF Postdoctoral Fellowship at Columbia University.
