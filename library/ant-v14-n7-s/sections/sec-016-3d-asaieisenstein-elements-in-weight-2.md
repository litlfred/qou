---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-016-3d-asaieisenstein-elements-in-weight-2
section_title: "3D. Asai–Eisenstein elements in weight 2"
section_number: null
pages: 19-21
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
of OF divisible by some integer> 4. Recall that we have
Y∗
F,1(n)=0∗
F,1(n)\H3,
and that we showed in Proposition 2.5 that the natural map
ι: YQ,1(N)↪→ Y∗
F,1(n)
is a closed immersion. We also need the following map:
Deﬁnition 3.8. Let m> 1 and a∈ OF. Consider the map
κa/m: Y∗
F,1(m2n)→ Y∗
F,1(n)
given by the left action of
( 1
0
a/m
1
)
∈ SL2(F) on H3. This is well-deﬁned, since it is easy to see that
(1 a/m
0 1
)
0∗
F,1(m2n)
(1−a/m
0 1
)
⊂0∗
F,1(n),
and it depends only on the class of a modulo mOF.
Remark. Note thatκa/m is not in general well-deﬁned on YF,1(m2n), since
(1 a/m
0 1
)(−1 0
0 1
)( 1−a/m
0 1
)
=
(−1 2 a/m
0 1
)
,
which is not in0F,1(n) if 2a /∈ mOF.
The elements we care about are the following. Assume that n is divisible by some integer q> 4, as
above. Then we have maps
YQ,1(m2N) ι→ Y∗
F,1(m2n) κa/m−−→Y∗
F,1(n).
Moreover, writing HBM
∗ for Borel–Moore homology (homology with noncompact supports), there are
isomorphisms
H1(YQ,1(m2N), Z)∼= HBM
1 (YQ,1(m2N), Z), H2(YF,1(m2n), Z)∼= HBM
1 (YF,1(m2n), Z), (3-3)
given by cap-product with the fundamental classes in HBM
2 (YQ,1(m2N), Z) and HBM
3 (Y∗
F,1(m2n), Z)
respectively. Since Borel–Moore homology is covariantly functorial for proper maps, we can therefore
deﬁne a pushforward map ι∗: H1(YQ,1(m2N), Z)→ H2(Y∗
F,1(m2n), Z).
1686 David Loeﬄer and Chris Williams
Deﬁnition 3.9. For a∈ OF/mOF, m> 1, and c> 1 coprime to 6m N, deﬁne
c4m,n,a∈ H2(Y∗
F,1(n), Z)
to be the image of cCm2 N under the map(κa/m)∗◦ι∗.
Proposition 3.10. We have
(−1
1
)∗
· c4m,n,a= c4m,n,−a.
Proof. It is clear that
(−1
1
)
◦κa/m=κ−a/m◦
(−1
1
)
as maps Y∗
F,1(m2n)→ Y∗
F,1(n). Moreover, the action
of
(−1
1
)
on Y∗
F,1(m2n) preserves the image of YQ,1(m2N), and the involution of YQ,1(m2N) it induces
is the involutionρ of Lemma 3.7, which acts as−1 on cCm2 N . Finally, we have
(−1
1
)∗
◦ι∗=−ι∗◦ρ∗,
because
(−1
1
)
preserves the orientation of Y∗
F,1(n) and thus acts as+1 on the fundamental class in HBM
3 ,
butρ reverses the orientation of YQ,1(m2N) and thus acts as−1 on the fundamental class. □
Deﬁnition 3.11. Deﬁne
c8r
n,a∈ H2(
Y∗
F,1(n), Z
)
⊗Z Zp[(Z/pr)×]
by
c8r
n,a:=
∑
t∈(Z/pr)×
c4pr,n,at⊗[ t].
Lemma 3.12. If n| n′ are two ideals of OF with the same prime factors, then pushforward along the map
YF,1(n′)→ YF,1(n) sends c8r
n′,a to c8r
n,a (for any valid choices of c, a, r).
Proof. This is immediate from the norm-compatibility of the Siegel units; compare [Lei et al. 2014,
Theorem 3.1.2]. □
We now come to one of the key theorems of this paper, which shows that if m= pr with r varying,
then the above elements ﬁt together p-adically into a compatible family. We now impose the assumption
that n is divisible by all primesv| p of OF.
Theorem 3.13. Let r> 1, let a be a generator of OF/(pOF+ Z), and let
πr+1: H2(Y∗
F,1(n), Z)⊗Z Zp[(Z/pr+1)×]→ H2(Y∗
F,1(n), Z)⊗Z Zp[(Z/pr)×]
denote the map that is the identity on the ﬁrst component and the natural quotient map on the second
component. Then we have
πr+1(c8r+1
n,a)=(Up)∗· c8r
n,a,
where the Hecke operator(Up)∗ acts via its action on H2(Y∗
F,1(n), Z). Similarly, when r= 0 we have
π1(c81
n,a)=((Up)∗− 1)· c80
n,a.
Remark 3.14. Before embarking on the proof, which will occupy the next section of the paper, we pause
to give a brief description of how this is important for the construction of p-adic Asai L-functions, in
the simplest case of a Bianchi eigenform 9 of weight(0, 0). Deﬁne eord,∗:= limn→∞(U n!
p)∗ to be the
p-adic Asai L-functions of Bianchi modular forms 1687
ordinary projector on cohomology with Zp coefﬁcients associated to(Up)∗, so that(Up)∗ is invertible on
the space eord,∗H2(Y1(n), Zp). Given the theorem, we see that the collection
[(Up)−r
∗ eord,∗· c8r
n,a]r>1
forms an element c8∞
n,a in the inverse limit
eord,∗H2(Y∗
F,1(n), Zp)⊗ Zp[[Z×
p]].
As in Section 2H, the eigenform9 gives rise to a cohomology classφ∗
9∈ H1
c(Y∗
F,1(n), R), where R is the
ring of integers of some ﬁnite extension of Qp. If the(Up)∗-eigenvalue of9 is a unit in R, then the linear
functional on H2(Y∗
F,1(n), Zp)⊗ R given by pairing withφ∗
9 factors through the projector eord,∗. Hence
pairing c8∞
n,a withφ∗
9 gives a measure on Z×
p with values in R. This will be our p-adic L-function. By
construction, its values at ﬁnite-order characters are given by integrating9 against linear combinations of
Eisenstein series on YQ,1(m2N); these will turn out to compute the special values of the Asai L-function.
