---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-032-0-eπqj-φ
section_title: "(E,π,Q,J )−φ),"
section_number: 0
pages: 48-51
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
where the ﬁrst summand is of order {−κ} and the second of order [−κ +α;∞).
Moreover,φ is determined by the horizontal sections:
φ(⊗
e∈I +
⟨xe⟩) =
∑
{xe}e∈I−
#Mh({xe}e∈I −∪I + )(⊗
e∈I −
⟨xe⟩).
There is a version of this for the homotopies between the CΦ 0
rel for diﬀerent
48
choices of ( j,J ). The proof applies the same ideas as before to parametrized
moduli spaces, and is left to the reader.
Lemma 2.30. Let (E,π ), Q and κ be as in Proposition 2.28. Consider two
complex structures jk on S, k = 0, 1, and correspondingly two almost complex
structures Jk∈ Jreg,h(E,π,Q,j, {Je}); note that the Je are supposed to be the
same for both k. Then the maps CΦ 0
rel(E,π,Q,J k) are homotopic by a chain
homotopy which is of order (−κ;∞).
It is a familiar idea that when dealing with maps between R-graded vector
spaces, the “lowest order term” is usually the most importan t, and knowing it
is often suﬃcient to resolve a question. A particular instan ce of this is relevant
for our purpose.
Lemma 2.31. Let D be an R-graded vector space with a diﬀerential dD of
order [0;∞). Suppose that D has gap [ǫ; 2ǫ) for some ǫ> 0. One can then write
dD =δ + (dD−δ) with δ of order [0;ǫ), satisfying δ2 = 0, and (dD−δ) of order
[2ǫ;∞). Suppose that in addition, H(D,δ ) = 0 ; then H(D,dD) = 0 .
Proof. Thanks to the gap assumption, supp(D) can be decomposed into disjoint
subsets R1,...,R m such that for r∈Ri,s∈Rj,
r−s



≤− 2ǫ i<j,
∈ (−ǫ;ǫ) i =j,
≥ 2ǫ i>j.
Deﬁne a descending ﬁltration of ( D,dD),
Fk = ⨁
r∈Rk∪Rk+1∪···∪RmDr.
There is a “spectral sequence” which takes the form of a seque nce (Ek,∂k) of
diﬀerential vector spaces, such that Ek+1 = H(Ek,∂k). It starts with E0 =⨁
iFi/Fi+1, which has a diﬀerential ∂0 induced by dD. In our case this can be
identiﬁed with ( D,δ ), so the assumption says that E1 = 0. On the other hand
Ek∼=H(D,dD) for k≫ 0.
Lemma 2.32. Take three R-graded vector spacesC′,C,C ′′, each of them with a
diﬀerential of order (0;∞). Suppose that we have diﬀerential maps b :C′→C,
c :C→C′′ and a homotopy h :C′→C′′ betweenc◦b and the zero map, such
that that the following conditions are satisﬁed for some ǫ> 0:
(i) C′,C ′′ have gap (0; 3ǫ), and C has gap (0; 2ǫ).
(ii) For all r∈supp(C′) and s∈supp(C′′),|r−s|≥ 4ǫ.
(iii) One can write b =β + (b−β) with β of order [0;ǫ) and (b−β) of order
[2ǫ;∞); and c =γ + (c−γ) with the same properties. The low order parts
(which do not need be diﬀerential maps) ﬁt into a short exact s equence of
vector spaces
0→C′ β
− →C
γ
− →C′′→ 0.
49
(iv) h is of order [0;∞).
Then the maps on cohomology induced by b,c ﬁt into a long exact sequence
H(C′,dC ′ )
b∗ /d47/d47H(C,dC )
c∗ /d47/d47H(C′′,dC ′′ )./d105/d105 (2.32)
Proof. Consider intervals Ir = [r;r +ǫ) for r∈supp(C′), and Ir = (r−ǫ;r] for
r∈supp(C′′). By (i), (ii) these are pairwise disjoint, and the distance between
any two of them is ≥ 2ǫ. From (iii) one sees that supp(C) is contained in the
union of these intervals, which shows that D = C′⊕C⊕C′′ has gap [ ǫ; 2ǫ).
Consider the diﬀerential dD =δ + (dD−δ),
dD =


dC ′ 0 0
b d C 0
h c d C ′′

, δ =


0 0 0
β 0 0
0 γ 0

.
We know that dC ′,dC ,dC ′′ , (b−β), (c−γ) are of order [2 ǫ;∞). Combining (ii)
with (iv) shows that h is of order [4 ǫ;∞), so that ( dD−δ) is of order [2 ǫ;∞).
On the other hand δ is of order [0; ǫ), and (iii) says that H(D,δ ) = 0. Lemma
2.31 shows that H(D,dD) = 0, which by a general fact implies the existence of
a long exact sequence (2.32).
50
