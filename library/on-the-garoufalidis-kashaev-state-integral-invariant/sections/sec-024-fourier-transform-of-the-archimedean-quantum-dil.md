---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "On the Garoufalidis-Kashaev state-integral invariant"
section_id: sec-024-fourier-transform-of-the-archimedean-quantum-dil
section_title: "Fourier transform of the Archimedean quantum dilogarithm"
section_number: null
pages: 24-26
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
doc_brief: "On the Garoufalidis-Kashaev state-integral invariant — 61 sections: ACKNOWLEDGMENTS; ABSTRACT; LIST OF TABLES"
---
Lemma 1. Let F be an Archimedean local field (R or C), and set A := cF××F×.
For
φ(α,x) := α(1 +x), (α,x)∈A,x̸=−1,
the inverse Fourier transform (with respect to the kernel recalled in 2.4)
˜φ(β,y ) :=
Z
A
φ(α,x)
⟨(α,x); (β,y )⟩d(α,x)
is, for y̸= 1,
15
˜φ(β,y ) = 1
β(y− 1)
1
∥1−y−1∥.
Proof. Let F be an Archimedean local field, so that F× is a Lie group and A =
cF××F× is the special Gaussian group defined in §2.4.
Define the function φ(α,x) := α(1 +x) for (α,x)∈A, with x̸=−1. The inverse
Fourier transform of φ with respect to the Fourier kernel ⟨(α,x); (β,y )⟩ = α(y)β(x)
is given by
˜φ(β,y ) :=
Z
dF××F×
α(1 +x)
α(y)β(x)dαdx.
Using Fubini’s theorem, we write:
˜φ(β,y ) =
Z
F×
Z
dF×
α
1 +x
y

dα

β(x)−1dx.
The inner integral evaluates to the multiplicative Dirac delta function on F×,
which contributes only when the argument is equal to 1 (see [7] section 2.2):
Z
dF×
α
1 +x
y

dα =δF×
1 +x
y

.
This condition is satisfied when x =y− 1, so the outer integral becomes:
˜φ(β,y ) =
Z
F×
δF×(x− (y− 1))·β(x)−1dx = 1
β(y− 1)· 1
∥y− 1∥.
We now relate this expression to the variable 1 −y−1 using the identity:
1−y−1 = y− 1
y ⇒ ∥1−y−1∥ =∥y− 1∥
∥y∥ .
To express the result in terms of ∥1−y−1∥, we rearrange:
16
1
∥y− 1∥ = ∥y∥
∥1−y−1∥.
This extra factor∥y∥ arises from the change between measures on F and F×, as
explained in [7] equation 19. We obtain:
˜φ(β,y ) = 1
β(y− 1)· 1
∥1−y−1∥, y ̸= 1.
Remark 4. All Haar measures are taken in the self-dual normalisation for the pairing
cF××F×→ T, so that the Fourier inversion formula holds without extra constants.
