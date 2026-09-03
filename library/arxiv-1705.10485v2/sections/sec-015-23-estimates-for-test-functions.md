---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-015-23-estimates-for-test-functions
section_title: "Estimates for test functions"
section_number: 2.3
pages: 12-14
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
We now give an estimate ofE[fn(Yn)]− E[fn(Y )], where (fn)n∈N is a sequence of test functions in
T0(R) or T1(R), and(Yn)n∈N is a sequence of random variables associated to a sequence(Xn)n∈N which
has a zone of control.
Proposition 16.Let (Xn)n∈N be a sequence of random variables,φc,α,β a reference stable law,Y with
law φc,α,β and Yn as in Proposition 3. We assume that:
(1) (Xn)n∈N has a zone of control[−K(tn)γ,K (tn)γ] with index (v,w );
(2) (fn)n∈N is a sequence of smooth test functions inT0(R), such that the support ofˆfn is included into
[−K(tn)γ+1/α,K (tn)γ+1/α].
Then,
Mod-φ convergence, II: Estimates on the speed of convergence 13
|E[fn(Yn)]− E[fn(Y )]|≤ C0(c,α,v )K1
‖fn‖L1
(tn)v/α,
whereC0(c,α,v ) = 2
v+1
α Γ((v+1)/α)
παcv+1 .
If instead of (2) we assume:
(2’)(fn)n∈N is a sequence of smooth test distributions inT1(R) such that ifφn =∂fn is the derivative of
the distributionfn, then the support ofˆφn is included into[−K(tn)γ+1/α,K (tn)γ+1/α].
Then
|E[fn(Yn)]− E[fn(Y )]|≤ C1(c,α,v )K1
‖φn‖L1
(tn)v/α,
whereC1(c,α,v ) = 2v/αΓ(v/α)
παcv .
Proof. Consider ﬁrst a sequence(fn)n∈N of test functions inT0(R), which satisﬁes (2). Using Parseval
formula and the zone of control assumption, we have
E[fn(Yn)]− E[fn(Y )] = 1
2π
∫ K(tn)γ+ 1
α
−K(tn)γ+ 1
α
ˆfn(ξ) eη(−iξ)
(
θn
(
−ξ/(tn)
1
α
)
− 1
)
dξ;
|E[fn(Yn)]− E[fn(Y )]|≤ K1‖ˆfn‖∞
2π(tn)v/α
∫ K(tn)γ+ 1
α
−K(tn)γ+ 1
α
|ξ|v e
−|cξ|α+K2
(
|ξ|
(tn )1/α
)w
dξ.
Forξ in [−K(tn)γ+1/α,K (tn)γ+1/α], since (tn)γ−1/(w−α)≤ 1, the second term in the exponent can be
bounded as follows:
K2
( |ξ|
(tn)1/α
)w
=K2|ξ|α
(
|ξ|
(tn)
1
α + 1
w−α
)w−α
≤K2|ξ|α
(
K(tn)γ− 1
w−α
)w−α
≤|cξ|α
2 .
This is compensated by the term−|cξ|α and, therefore,
|E[fn(Yn)]− E[fn(Y )]|≤ K1‖ˆfn‖∞
2π(tn)v/α
∫
R
|ξ|ve−|cξ|α
2 dξ
≤ 2
v+1
α K1
παcv+1(tn)v/α Γ
(v + 1
α
)
‖fn‖L1.
This ends the proof of the ﬁrst case. For test distributionsfn∈ T1(R) which satisﬁes the condition(2′),
let us introduce the signed measureµ = PYn− PY. One hasˆµ(0) = 0, and by hypothesis,
⏐⏐⏐⏐
ˆµ(ξ)
ξ
⏐⏐⏐⏐≤ K1|ξ|v−1
(tn)v/α e
−|cξ|α+K2
(
|ξ|
(tn )1/α
)w
.
Remark 15 applies, and thus,
|E[fn(Yn)]− E[fn(Y )]| =|⟨µ|fn⟩| = 1
2π
⏐⏐⏐
⟨
ˆfn
⏐⏐⏐ˆµ
⟩⏐⏐⏐ = 1
2π
⏐⏐⏐⏐
∫
R
ˆφn(ξ)ˆµ(−ξ)
ξ dξ
⏐⏐⏐⏐.
From there, the computations are exacly the same as before, with an indexv− 1 instead ofv. ⊓ ⊔
