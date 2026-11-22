---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-015-36-the-dirac-operator-and-its-square
section_title: "The Dirac operator and its square"
section_number: 3.6
pages: 29-30
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
The Dirac operator DA that takes the inner ﬂuctuations into account is given by the sum of
two terms
DA = D(1,0) + γ5 ⊗D(0,1),
(3.28)
where D(0,1) is given by (3.11) and D(1,0) is of the form
D(1,0) =
√
−1 γµ(∇s
µ + Aµ),
(3.29)
where ∇s is the spin connection (cf. (3.2)).
The gauge potential Aµ splits as a direct sum in the decomposition associated to HF =
Hf ⊕H ¯f and its restriction to Hf is given by Proposition 3.9.
In order to state the next step, i.e. the computation of the square of DA, we introduce the
notations
T(M1, M2, ϕ) =


0
0
M∗
1 ϕ1
M∗
1 ϕ2
0
0
−M∗
2 ¯ϕ2
M∗
2 ¯ϕ1
M1 ¯ϕ1
−M2 ϕ2
0
0
M1 ¯ϕ2
M2 ϕ1
0
0


(3.30)
with ϕ = (ϕ1, ϕ2) and Mj a pair of matrices, and
M(ϕ) = T(Y(↑3), Y(↓3), ϕ) ⊗13 ⊕T(Y(↑1), Y(↓1), ϕ) ⊕T(Y(↑3), Y(↓3), ϕ) ⊗13 ⊕T(Y(↑1), Y(↓1), ϕ)
(3.31)
By construction M(ϕ) is self-adjoint and one has
Tr(M(ϕ)2) = 4 a |ϕ|2 ,
a = Tr(Y ∗
(↑1)Y(↑1) + Y ∗
(↓1)Y(↓1) + 3(Y ∗
(↑3)Y(↑3) + Y ∗
(↓3)Y(↓3)))
(3.32)
Lemma 3.12. The square of DA is given by
D2
A = ∇∗∇−E,
(3.33)
where ∇∗∇is the connection Laplacian for the connection
∇= ∇s + A
(3.34)
and the endomorphism E is given, with s = −R the scalar curvature, by
−E = 1
4 s ⊗id +
X
µ<ν
γµγν ⊗Fµν −i γ5 γµ ⊗M(Dµ ϕ) + 14 ⊗(D0,1)2
(3.35)
30
CHAMSEDDINE, CONNES, AND MARCOLLI
with H = ϕ1 + ϕ2j as above, and ϕ = (ϕ1, ϕ2). Here Fµν is the curvature of the connection
A and ϕ = (ϕ1, ϕ2) is a row vector. The term Dµϕ in (3.35) is of the form
Dµ ϕ = ∂µ ϕ + i
2 g2 W α
µ ϕ σα −i
2 g1 Bµ ϕ .
(3.36)
Proof. By construction D1,0 anticommutes with γ5. Thus, one has
D2
A = (D1,0)2 + 14 ⊗(D0,1)2 −γ5 [D1,0, 14 ⊗D0,1].
The last term is of the form
[D1,0, 14 ⊗D0,1] =
√
−1 γµ [(∇s
µ + Aµ), 14 ⊗D0,1].
Using (3.3), one can replace ∇s
µ by ∂µ without changing the result. In order to compute the
commutator [Aµ, D0,1], notice ﬁrst that the oﬀdiagonal term of D0,1 does not contribute,
since the corresponding matrix elements of Aℓ
µ are zero. Thus, it is enough to compute the
commutator of the matrix
W =


−i
2g1Bµ
0
0
0
0
i
2g1Bµ
0
0
0
0
−i
2g2W 3
µ
−i
2g2(W 1
µ −iW 2
µ)
0
0
−i
2g2(W 1
µ + iW 2
µ)
i
2g2W 3
µ


(3.37)
with a matrix of the form
T(M1, M2, ϕ) =


0
0
M∗
1 ϕ1
M∗
1 ϕ2
0
0
−M∗
2 ¯ϕ2
M∗
2 ¯ϕ1
M1 ¯ϕ1
−M2 ϕ2
0
0
M1 ¯ϕ2
M2 ϕ1
0
0


(3.38)
One gets
[W, T(M1, M2, ϕ)] = T(M1, M2, ψ),
(3.39)
where
(ψ1, ψ2) = −i
2g1Bµ(ϕ1, ϕ2) + i
2g2W α
µ (ϕ1, ϕ2) σα.
(3.40)
