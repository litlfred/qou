---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-098-65-betti-polynomials
section_title: "Betti polynomials"
section_number: 6.5
pages: 152-153
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
To ﬁnish the proof of theorem 6.1 it remains to compute the contribution
of the negligible complexcδα from the end of section 6.2. Recall that this
complex is a direct sum of degree shifts ofδX, which will allow to control it
in terms of hypercohomology. More speciﬁcally, for anyK∈ Dbc (X,C) we
have the Betti polynomial
h(K,t) = ∑
i∈Z
dimC(Hi(X,K))·ti∈ C[t, t−1].
If K∼= D(K) is isomorphic to its Verdier dual, then the polynomialh(K,t)
is invariant under the coordinate transformationt↦→ 1/t and hence can be
written as a polynomialp(K,ξ)∈ C[ξ] in the new variable
ξ = t−1/2 +t1/2
where of course only even powers ofξ occur. Note thatp(δX,ξ) = ξ2g so
that this new variable is particularly useful for the detection of the direct
summandsδX we are interested in.
LEMMA 6.7. For any d∈ N0 we have
p(δd,ξ) =
d
∑
c=0
(2(g−1−c)
d−c
)· ξ2c .
Proof.By deﬁnitionδd =Rhd∗(δCd) =Rhd∗(CCd[d]) is the direct image
of the constant perverse sheaf under the Abel-Jacobi morphismhd :Cd→X,
so its hypercohomology is
H•(X,δd) = H•+d(Cd,C).
Now the cohomology of symmetric products of a curve has been computed
in [72, eq. 4.2]. For the Betti polynomial this gives
h(δd,t) =
d
∑
m=0
( 2g
d−m
)Pm(t) where Pm(t) =
m
∑
c=0
t2c−m.
Hence it will sufﬁce to check that
Pm = ∑
c≥0
(−1)m−c(m+1+c
m−c
)· ξ2c for all m≥ 0,(i)
(2(g−1−c)
d−c
) = ∑
m≥0
(−1)m−c( 2g
d−m
)(m+1+c
m−c
) for all c≥ 0.(ii)
