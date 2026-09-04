---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-034-8-modifications-in-the-degenerate-case
section_title: "Modifications in the degenerate case"
section_number: 8
pages: 54-56
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
Assume in this section that k is a ﬁeld of characteristic p≥ 0. As we have said
already in the introduction, when z = 0, the category OS (z,t ) should be replaced with
the oriented Brauer category OB(δ) studied in [BCNR].
Proof of Theorem 1.10. This follows by the same general argument as used to prove
Theorem 1.3 (also Remark 3.4). Instead of the quantized Schur-We yl duality used
before, one uses classical Schur-Weyl duality in its “characterist ic free” form established
in [CP, Theorems 4.1–4.2]. □
Now we discuss the degenerate analog of the results in sections 5, 6 and 7.
For section 5, we work with the locally ﬁnite-dimensional locally unital a lgebra
OB =
⨁
a,b∈⟨↑,↓⟩
1aOB1b where 1 aOB1b = HomOB(δ)(b, a).
It has a triangular decomposition
OB∼=OB+⊗KOB0⊗KOB−
like in Lemma 5.1. This actually becomes easier since there is no longer an y need to
be careful about upward strands passing underneath downward strands when deﬁning
OB0. The subsequent arguments in section 5 then go through easily on r eplacing the
Hecke algebra Hr with the group algebra k Sr of the symmetric group and e with p.
The results in section 6 go through too, but this needs a little more wo rk since the
deﬁnitions of the various Jucys-Murphy elements from (4.9), (6.2) and (6.13)–(6.14)
need some modiﬁcations, and the details in the proofs of Lemmas 6.4 a nd 6.7 then
need to be rechecked carefully. The aﬃne Hecke algebra AHr becomes the degenerate
aﬃne Hecke algebra dAHr whose polynomial generators x1,...,x r satisfy the relations
xixj =xjxi, s ixi+1 =xisi + 1 (8.1)
in place of (4.1). The unique homomorphism dAHr։ k Sr sendingsi↦→si andx1↦→0
sends xr to the Jucys-Murphy element
lr :=
r−1∑
i=1
(i r)∈ k Sr. (8.2)
These elements are the replacements for (6.2). Then the content s of nodes of an
ordinary Young diagram (which should always be interpreted as eleme nts of the ﬁeld
k ) are as in the following example
0 1 2 3 4
−1 0 1
−2 −1
.
In place of (6.3), we set
Ic :={c +n|n∈ Z}⊆ k (8.3)
for c∈ k . The appropriate analog of Lemma 6.1 uses I0⊆ k in place of I1⊆ k ×. It is
a classical result in the (modular) representation theory of the sy mmetric group.
The Jucys-Murphy elements of OB(δ) are the images of corresponding elements of
the aﬃne oriented Brauer category AOB(δ) introduced in [BCNR]. This strict k -linear
ORIENTED SKEIN CATEGORY 55
monoidal category is deﬁned by by adjoining an additional generatin g morphism •
toOB(δ), subject to the relation (dA) from Figure 1. The analog of Lemma 4 .2 is
explained in [BCNR, Theorem 3.3]: there is a k -linear functor β :AOB(δ)→OB (δ)
sending diagrams with no dots to the same diagrams in OB(δ), and sending • ↦→0.
The following computes the image of • (which is deﬁned so that (4.3)–(4.4) hold):
• =
•
= • − ↦→ −δ .
Then we deﬁne x(b)∈ HomOB(δ)(b, b) in the same way as (4.10) for any ∅ ⁄= b∈⟨↑,↓⟩.
There is no longer such a nice diagrammatic interpretation of these e lements like (4.9),
but there is a recursive deﬁnition as in (4.11)–(4.12): we have that x(↑) = 0 ,x (↓) =
−δ1↓, and
x(↑↑b) := x(↑b)
b
b
+
b
, x (↑↓b) := x(↑b)
b
b
−
b
, (8.4)
x(↓↓b) := x(↓b)
b
b
−
b
, x (↓↑b) := x(↓b)
b
b
+
b
, (8.5)
for any word b. Finally, the Jucys-Murphy elements x◦(b) ofOB◦(δ), i.e., the subcat-
egory consisting of all objects but only morphisms represented by diagrams with no
cups or caps, are deﬁned from x◦(↑) := 0,x◦(↓) :=−δ1↓, and
x◦(↑↑b) := x◦(↑b)
b
b
+
b
, x ◦(↑↓b) := x◦(↑b)
b
b
, (8.6)
x◦(↓↓b) := x◦(↓b)
b
b
−
b
, x ◦(↓↑b) := x◦(↓b)
b
b
. (8.7)
We leave it to the reader to verify with these new deﬁnitions that Lem mas 6.4 and 6.7
go through; see also [Re]. In the statement of Lemma 6.4, one should replace t−2i−1
with−i−δ, I1 with I0, and It−2 with I−δ. Also the set I from (6.27) becomes
I :=I0∪I−δ ={n,−n−δ|n∈ Z}⊆ k . (8.8)
Adjusting the subsequent combinatorics in analogous ways, all of t he other results of
section 6 follow as before.
Moving on to section 7, the Lie algebra g is the Kac-Moody algebra associated to
the Cartan matrix ( ci,j)i,j∈I deﬁned by (1.22). The module V (−Λ 1|Λt−2 ) becomes
V (−Λ 0|Λ−δ), and the degenerate analogs of (8.9)–(8.10) are
wt↑(λ ) :=−Λ 0 +
∑
A∈λ↑
αcont(A), (8.9)
wt↓(λ ) := Λ−δ−
∑
A∈λ↓
α−cont(A)−δ,. (8.10)
56 J. BRUNDAN
There are no other signiﬁcant discrepancies.
Proof of Theorem 1.11. This is the same as the proof of Theorem 1.9 given in the
previous section. □
