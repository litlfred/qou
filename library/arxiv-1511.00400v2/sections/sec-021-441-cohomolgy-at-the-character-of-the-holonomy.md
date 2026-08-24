---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-021-441-cohomolgy-at-the-character-of-the-holonomy
section_title: "Cohomolgy at the character of the holonomy"
section_number: 4.4.1
pages: 32-35
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
In order to evaluate the torsion functions at the lift of the holonom y, some results
on the cohomology for this representation are required. Again the proofs are
postponed to Appendix B.
32
Theorem 4.19 (Theorem B.7). Let ̺∶ π1M 3 → SL2(C) be a lift of the holonomy.
(a) If k1 + k2 is odd, then ̺k1,k2 is acyclic.
(b) If k1 + k2 is even, k1 ≠k2, then
dim Hi(M 3; ̺k1,k2) =
⎧
⎪
⎪
⎨
⎪
⎪
⎩
1 if i = 1, 2 ,
0 otherwise.
Notice that when both k1 and k2 are odd, the homology of ̺k1,k2 diﬀers from
the generic homology of Sym k1,k2 on X0(M 3), there is a discontinuity in the
dimension of the cohomology, which is generically trivial.
We also need to discuss the basis. Let i∶ T 2 → M 3 denote the inclusion.
Proposition 4.20 (Corollary B.6 and Proposition B.8) . Let ̺∶ π1M 3 → SL2(C)
be a lift of the holonomy. Assume that k1 + k2 is even.
(a) dim H 0(T 2; ̺) = 1.
(b) For 0 ≠a ∈H 0(T 2; ̺), ⟨i∗(a ∩ [T 2])⟩ = H2(M 3; ̺k1,k2 ).
(c) For 0 ≠a ∈H 0(T 2; ̺) and 0 ≠γ ∈H1(T2; Z):
(i) ⟨i∗(a ∩ γ)⟩ = H1(M 3; ̺k1,k2 ) if k1 = 0 or k2 = 0; in addition
i∗(a ∩ γ1) = cs(γ1, γ2) i∗(a ∩ γ2) (32)
where cs(γ1, γ2) is the cusp shape (Deﬁnition 3.19).
(ii) i∗(a ∩ γ) = 0 if k1 ≠0 and k2 ≠0.
4.4.2 T orsion at the characters of the holonomy
Proposition 4.21. Let χ̺ be the character of a lift ̺ of the holonomy repre-
sentation
(a) When k1 + k2 is odd, Tk1,k2
M (χ̺) ≠0.
In particular, when k is odd, Tk
M (χ̺) ≠0.
(b) When k1 ≠k2 are both odd, Tk1,k2
M (χ̺) = 0.
(c) When k1 ≠k2 are both even and k1, k2 ≠0, for 0 ≠γ ∈H1(T2; Z), we have
Tk1,k2
M,γ (χ̺) = 0.
(d) For k even and 0 ≠γ ∈H1(T2; Z), Tk
M,γ (χ̺) ≠0. In addition
Tk
M,γ2 (χ̺)
Tk
M,γ1
(χ̺) = cs(γ2, γ1),
where 0 ≠γ1, γ2 ∈H1(T2; Z).
33
Proof. For item (a), Theorem 4.19 guarantees that the representation is acyclic
and therefore Tk1,k2
M (χ̺) ≠0. For (b), the same theorem tells that the cohomol-
ogy of ̺k1,k2 is nonzero in dimension 1 and 2. Since it is generically zero, what
we have is a discontinuity in the dimension of the cohomology groups. O n the
other hand, the zeroth homology group of ̺k1,k2 vanishes, thus Tk1,k2
M (χ̺) = 0.
The proof of (c) is analogous, using the vanishing of the cup produc t in dimen-
sion one (not two) of the cap product in Proposition 4.20. The non-v anishing of
the cup product of Proposition 4.20 for k1 even and k2 = 0 yields the ﬁrst part
of item (d), the second part follows from Equation (32).
Theorem 4.22 ([63]). For any peripheral curve γ,
lim
k→∞
log /divid⟩s.alt1T2k
M,γ (χ̺)/divid⟩s.alt1
(2k)2 = lim
k→∞
log /divid⟩s.alt1T2k+1
M (χ̺)/divid⟩s.alt1
(2k + 1)2 = 1
4π vol(M 3) . (33)
Again, the sign convention is the opposite to [63]. This theorem is prov ed
from M¨ uller’s Theorem 4.5 in the closed case, by using the approximation of the
cusped manifolds by closed manifolds obtained by Dehn ﬁlling. Since M¨ u ller’s
proof uses Ruelle zeta functions, the key point is to understand ge odesics (of
bounded lengths) of the closed manifolds that approximate a cuspe d one.
4.4.3 Dehn ﬁlling
The following is a generalization to other representations of the for mula for
Dehn ﬁlling in Proposition 3.25. In particular the same context and not ation is
used.
Proposition 4.23. Let M 3 be as above. For /divid⟩s.alt0p/divid⟩s.alt0+ /divid⟩s.alt0q/divid⟩s.alt0 suﬃciently large:
(a) For k1 or k2 odd,
τ k1,k2(M 3
p/sl⊗sh.leftq, σ) = Tk1,k2
M (χp/sl⊗sh.leftq,σ )
k1
/product.disp
i1=0
k2
/product.disp
i2=0
1
1 − (λp/sl⊗sh.leftq)2i1−k1 (λp/sl⊗sh.leftq)2i2−k2
.
(b) For k1 and k2 even, k1 ≠k2,
τ k1,k2(M 3
p/sl⊗sh.leftq) = Tk1,k2
M,pm+ql(χp,q) /product.disp
(i1,i2)∈I
1
1 − (λp/sl⊗sh.leftq)2i1−k1 (λp/sl⊗sh.leftq)2i2−k2
,
where (i1, i2) ∈I if 0 ≤i1 ≤k1, 0 ≤i2 ≤k2, and i1 ≠k1
2 or i2 ≠k2
2 .
Corollary 4.24.
lim
p2+q2
/divid⟩s.alt0τ 2k(M 3
p/sl⊗sh.leftq, σ)/divid⟩s.alt0= +∞ .
Proof. Use ﬁrst Proposition 4.21 (d) . Since the character χp,q converges to χ̺,
T2k
M,m(χ̺) ≠0, and /divid⟩s.alt0cs(pm + ql, m)/divid⟩s.alt0= /divid⟩s.alt0p + q cs(l, m)/divid⟩s.alt0→ ∞, one has
/divid⟩s.alt0T2k
M,pm+ql(χp,q)/divid⟩s.alt0→ ∞ .
As /divid⟩s.alt0λp/sl⊗sh.leftq/divid⟩s.alt0→ 1, the surgery formula in Proposition 4.23 yields the result.
The same proof as Corollary 3.28 yields:
34
Corollary 4.25. Given a spin structure, The set of modules of the torsions
/divid⟩s.alt0τ 2k1+1,k2 (M 3
p/sl⊗sh.leftq, σ)/divid⟩s.alt0 obtained by Dehn ﬁlling on M 3, so that σ can be extended,
is dense in
/brack⟩tl⟩ft.alt31
4 /divid⟩s.alt1τ 2k1+1,k2 (M 3, σ)/divid⟩s.alt1, +∞/par⟩nright.alt3 .
When k1 + k2 is even and k1k2 ≠0, then Tk1,k2
M (χ̺) = 0 (for ki odd) and
Tk1,k2
M,γ (χ̺) = 0 (for ki even). In this case, we cannot get conclusions from the
surgery formula.
