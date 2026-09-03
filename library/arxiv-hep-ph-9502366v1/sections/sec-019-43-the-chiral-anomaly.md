---
doc_id: arxiv-hep-ph-9502366v1
doc_title: ""
section_id: sec-019-43-the-chiral-anomaly
section_title: "The chiral anomaly"
section_number: 4.3
pages: 13-14
source_pdf: 9502366v1.pdf
source_sha256: 56df064956ca03f8
doc_brief: "An introduction to the basic ideas and methods of Chiral Perturbation Theory is presented."
---
Although the QCD Lagrangian (3.10) is invariant under local chiral transforma-
tions, this is no longer true for the associated generating f unctional. The anomalies of
the fermionic determinant break chiral symmetry at the quan tum level (Adler 1969,
Bardeen 1969, Bell and Jackiw 1969). The fermionic determin ant can always be de-
ﬁned with the convention that Z[v, a, s, p] is invariant under vector transformations.
Under an inﬁnitesimal chiral transformation
gL,R = 1 + iα ∓ iβ + . . . (4.6)
the anomalous change of the generating functional is then gi ven by (Bardeen 1969):
δZ [v, a, s, p] = − NC
16π2
∫
d4x ⟨β(x) Ω( x)⟩, (4.7)
Ω( x) = εµνσρ
[
vµνvσρ + 4
3 ∇µaν∇σaρ + 2
3 i {vµν, aσaρ} + 8
3 i aσvµνaρ + 4
3 aµaνaσaρ
]
, (4.8)
vµν = ∂µvν − ∂νvµ − i [vµ, vν] , ∇µaν = ∂µaν − i [vµ, aν] . (4.9)
(NC = 3 is the number of colours, and ε0123 = 1). Note that Ω( x) only depends on
the external ﬁelds vµ and aµ. This anomalous variation of Z is an O(p4) eﬀect, in the
chiral counting.
So far, we have been imposing chiral symmetry to construct th e eﬀective ChPT
Lagrangian. Since chiral symmetry is explicitly violated b y the anomaly at the
fundamental QCD level, we need to add a functional ZA with the property that its
change under a chiral gauge transformation reproduces (4.7 ). Such a functional was
ﬁrst constructed by Wess and Zumino (1971), and reformulate d in a nice geometrical
way by Witten (1983). It has the explicit form:
S[U, ℓ, r]W ZW = − iNC
240π2
∫
dσijklm⟨
Σ L
i Σ L
j Σ L
k Σ L
l Σ L
m
⟩
− iNC
48π2
∫
d4x εµναβ
(
W (U, ℓ, r)µναβ − W (1, ℓ, r)µναβ)
, (4.10)
∗ Since the loop amplitude increases with the number of possib le Goldstone mesons in the internal lines,
this estimate results in a slight dependence of Λ χ on the number of light-quark ﬂavours Nf (Soldate
and Sundrum 1990, Chivukula et al 1993): Λ χ ∼ 4πfπ/√ Nf .
