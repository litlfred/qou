---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-104-2121-we-then-apply-lemma-423-herebelow-and-theor
section_title: "We then apply lemma 4.2.3 (herebelow) and theorem 4 .2.5 (further"
section_number: 2.1.2.1
pages: 59-61
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
below).
Lemma 4.2.3 . — LetR be a C({z})-vector space on whichσq operates. With
the notations of the previous proposition, P : R→ R is onto if, and only if,
σq−AP :Rn→Rn is onto.
Proof. — (i) Assume P is onto. To solve ( σq−AP )



x1
.
.
.
xn


 =



y1
.
.
.
yn


, put
xi+1 := σqxi−yi; one sees that x1 just has to be solution of an equation
Px 1 =z, where z is some explicit expression of the yi.
(ii) Assume σq−AP is onto. To solve Pf = g, it is enough to solve σqX−
APX =





0
.
.
.
0
g




 and to set f to the ﬁrst component of X.
Remark 4.2.4 . — This computation is directly related to the homotopy of
complexes discussed in A.8.2.
54 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
Theorem 4.2.5. — The endomorphism P of A0(U∞) is onto.
Proof. — We give the proof under the assumption that the slopes are i ntegral,
which is the only case we need in this paper; the reader will ea sily deduce the
general case by ramiﬁcation. The counterpart of the slope ﬁl tration on the
side of q-diﬀerence operators is the existence of a factorisation [ 31, 51, 58 ] of
P as a product of non commuting factors: elements of C{z}∗ (which induce
automorphisms of A0(U∞)) and ﬁrst order operators zµσq−a,µ∈ Z,a∈ C∗.
We are therefore reduced to the following lemma. (This is where some analysis
comes in !)
Lemma 4.2.6 . — The endomorphism f↦→zµσqf−af of A0(U∞) is onto.
Proof. — Write L this endomorphism. Let h∈ A0(U∞); for all n∈ N and
each strict stable subset V of U, there exists Cn,V > 0 such that |h(z)| <
Cn,V|z|n overV . We distinguish two cases: (i) µ≤ 0; (ii) µ> 0.
Case (i): µ≤ 0 (easy case). Let Φ be the automorphism of A0(U∞) deﬁned
by Φ(f) := aqµz−µσq−1f; one has Φ mf = amqµm(m+1)/2z−mµσq−mf for all
m≥ 0. Since |h(z)|≤ Cn,V|z|n on each stable strict subset V of U and all
integersn≥ 0, one ﬁnds:
∀z∈V ,
∑
m≥0
|Φmh(z)|≤ Cn,V
∑
m≥0
|a|m|q|µm(m+1)/2|q|−nm|z|n.
One deduces that the series ∑
m≥0 Φmh deﬁnes a ﬂat function over U, write
it H∈ A0(U∞). Observing that LH =zµσq(H− ΦH) = zµσqh, we see that
L is onto over A0(U∞).
Case (ii): µ > 0 (hard case). For all j ∈ N, set Uj := q−jU0 ={z ∈
C∗|qjz∈U0}; these are pairwise disjoint sinceU was assumed to be adequate.
We are going to build successively f0,f 1,f 2,... overU0,U 1,U 2,... , which will
give rise to a function f deﬁned overU =q−NU0, with fj =f|Uj and Lf =h.
For all j∈ N, let hj := h|Uj : Uj→ C. Since ( σqf)|Uj =σqfj−1, equation
Lf =h is equivalent to system:
∀j∈ N∗, zµσqfj−1−afj =hj,
also written:
(4.1) ∀j∈ N∗ , fj = (zµσqfj−1−hj)/a.
