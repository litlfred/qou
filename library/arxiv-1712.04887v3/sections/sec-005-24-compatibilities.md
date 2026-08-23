---
doc_id: arxiv-1712.04887v3
doc_title: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture"
section_id: sec-005-24-compatibilities
section_title: "Compatibilities"
section_number: 2.4
pages: 14-15
source_pdf: 1712.04887v3.pdf
source_sha256: 024317c20a1d8b66
doc_brief: "Bloch groups, algebraic K-theory, units, and Nahm's conjecture — Given an element of the Bloch group of a number ﬁeld F and a natural num- ber n, we construct an explicit unit in the ﬁeld Fn = F"
---
respect to n, and in particular we compare Rζ to Rζq for any divisor q of n. This will be
important in Section 5, where we consider the relation of our map and the Chern class in
K-theory. We also discuss the compatibility of Rζ with respect to a change of ﬁeld.
Lemma 2.7. Let (n,wF ) = 1 and ζ =ζn as usual. Then the following compatibilities hold:
(1) If (n,k ) = 1, then Rζk(X) =Rζ(X)k−1
.
(2) Let n =qr, and let ζr =ζq
n. Then the image of Rζn(X) modulo rth powers is equal
to the image of Rζr(X) under the map
(
F×
r /F×r
r
)χ−1
→
(
F×
n/F×r
n
)χ−1
(25)
induced by the inclusion.
We note in passing that the map (25) is not always injective (a fact exploited in the proof
of Lemma 5.3).
Proof. The ﬁrst statement reﬂects the fact thatgRζ =Rg(ζ) forg∈G = Gal(Fn/F ). For the
second claim, we ﬁrst note by Lemma 2.4(b) that Dζn(1) =ζn/3
n ≡ζr/3
r =Dζr(1), where the
equivalence is modulo rth powers. (Either 3|r in which case both sides are literally equal,
or (3,r ) = 1 and 3rd roots of unity are rth powers.) Then we calculate
Dζn(1)Pζn(X) =
∏
k modn
(
1−ζk
nx
)k
=
∏
i modq
j modr
(
1−ζri+j
n x
)ri+j
≡
∏
i modq
j modr
(
1−ζi
qζj
nx
)j
=
∏
j modr
(
1−ζj
rxq)j
= Dζr(1)Pζr(X),
where the congruence is modulo rth powers. □
Next, we discuss a reduction of the map Pζn to the case that n is a prime power.
Lemma 2.8. Let n = ab with (a,b ) = 1 and ζ a primitive nth root of unity. If X ∈
A(F ; Z/nZ), let un = Rζ(X), ua = Rζb(X) and ub = Rζa(X). Then un determines and is
uniquely determined by ua and ub.
Proof. Part (2) of Lemma 2.7 shows that the image of un in F×
n/F×a
n is the image of ua
under the natural map
F×
a /F×a
a →F×
n/F×a
n .
Equivalently,ua determines un up to an ath power, and similarly ub determines un up to
a bth power. This is enough to determine un completely since a and b are coprime. The
converse has already been shown. □
Remark 2.9. Both lemmas hold also for (n,wF )> 1 if we replace Rζ byRwF
ζ .
We also have:
BLOCH GROUPS, ALGEBRAIC K-THEORY, UNITS, AND NAHM’S CONJECTURE 15
Lemma 2.10. LetE/F be a ﬁeld extension, and assume that (n,wE) = 1 andζ =ζn. Then
the following diagram commutes:
B(F )/nB(F ) Rζ
-(
F×
n/F×r
n
)χ−1
B(E)/nB(E)
?
Rζ
-(
E×
n/E×r
n
)χ−1
.
?
Proof. By construction, the maps Pζ(ξ) are compatible where the targets on the RHS are
replaced by the corresponding universal Kummer extensions. But by the uniqueness of the
lift Rζ(ξ) (Proposition 2.5(b)), the diagram commutes. □
