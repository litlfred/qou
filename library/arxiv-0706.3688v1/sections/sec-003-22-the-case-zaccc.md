---
doc_id: arxiv-0706.3688v1
doc_title: "WHY THE STANDARD MODEL"
section_id: sec-003-22-the-case-zaccc
section_title: "The case Z(AC)=CC"
section_number: 2.2
pages: 6-7
source_pdf: 0706.3688.pdf
source_sha256: f2a18b0defebff66
toc_source: outline
doc_brief: "WHY THE STANDARD MODEL — The Standard Model is based on the gauge invariance principle with gauge group U(1) × SU(2) × SU(3) and suitable representations for fermions and bosons, which are begging"
---
We assume Z(AC) = C⊕C. Then there exists kj ∈N such that AC = Mk1(C)⊕Mk2(C)
as an involutive algebra over C. We let ej be the minimal projections ej ∈Z(AC) with
ej corresponding to the component Mkj(C).
Lemma 2.7.
(1) The representation β of AC ⊗A0
C in H of (2.6) is the direct sum
of two irreducible representations in the decomposition
(2.10)
H = e1H ⊕e2H = H1 ⊕H2 , β = β1 ⊕β2.
(2) The representation β1 (resp β2) is the only irreducible representation of the
reduced algebra of B by e1 ⊗e0
2 (resp. e2 ⊗e0
1).
(3) The dimension of Hj is equal to k1k2.
Proof. 1) Let Hj = ejH. Since ej ∈Z(A) the action of A in H is diagonal in the
decomposition (2.10). By Lemma 2.2 one has JejJ−1 = ek, k̸ = j, thus the action of
A0 is also diagonal in the decomposition (2.10). Thus the representation β decomposes
as a direct sum β = β1 ⊕β2. Moreover by Lemma 2.2 the antilinear involution J
interchanges the Hj. Let F1 be an invariant subspace for the action β1 of B in H1. Then
F1 ⊕JF1 ⊂H is invariant under both B and J and thus equal to H by irreducibility
which implies F1 = H1.
2) This follows since in each case one gets an irreducible representation of the reduction
of B by the projections ei ⊗e0
j, i̸ = j, which as an involutive algebra is isomorphic to
Mki(C) ⊗Mkj(C) ∼Mk1k2(C).
3) This follows from 2).
□
Proposition 2.8. Let H be a Hilbert space of dimension n.
Then an irreducible
solution with Z(AC) = C ⊕C exists iﬀn = 2k2 is twice a square. It is given by
AC = Mk(C) ⊕Mk(C) acting by left multiplication on itself and antilinear involution
(2.11)
J(x, y) = (y∗, x∗) ,
∀x, y ∈Mk(C) .
Proof. Let us ﬁrst show that k1 = k2. The dimension of AC is k2
1+k2
2. The dimension of
H is 2k1k2 by Lemma 2.7. The separating condition implies dim AC ≤dim H because
of the injectivity of the map a ∈AC 7→aξ ∈H for ξ such that A′ξ = H. This gives
k2
1 + k2
2 ≤2k1k2
which is possible only if k1 = k2. In particular n = 2k2 is twice a square. We have
shown that AC = Mk(C) ⊕Mk(C) and moreover by Lemma 2.7 the representation β
is the direct sum of the irreducible representations of the reduced algebras of B by the
projections e1 ⊗e0
2 and e2 ⊗e0
1. Thus we can assume that the representation β of B
is the same as in the model of Proposition 2.8. It remains to determine the antilinear
isometry J. We let J0(x, y) = (y∗, x∗) ,
∀x, y ∈Mk(C) as in (2.11) and compare
the antilinear isometry J of the given pair with J0. By the argument of the proof of
Proposition 2.5, we get that the ratio J−1
0 J commutes with B and hence is a diagonal
matrix of scalars

λ1
0
0
λ2

in the decomposition H = H1⊕H2. The condition J2 = 1
WHY THE STANDARD MODEL
7
shows that λ1 = λ2. Thus J = λJ0 and the argument of the proof of Proposition 2.5
applies to give the required uniqueness.
□
Remark 2.9. One can describe the above solutions (i.e. the algebra AC and its rep-
resentation in H, J) in a more intrinsic manner as follows. We let V and W be k-
dimensional complex Hilbert spaces. Then
(2.12)
AC = EndC(W) ⊕EndC(V ) .
We let H be the bimodule over AC given by
(2.13)
H = E ⊕E∗,
J(ξ, η) = (η∗, ξ∗)
where,
(2.14)
E = HomC(V, W) ,
E∗= HomC(W, V )
and the algebra acts on the left by composition:
(2.15)
(w, v)(g, h) = (w ◦g, v ◦h) ,
∀(w, v) ∈AC , (g, h) ∈E ⊕E∗.
The various real forms can then be described using additional antilinear isometries of
V and W.
