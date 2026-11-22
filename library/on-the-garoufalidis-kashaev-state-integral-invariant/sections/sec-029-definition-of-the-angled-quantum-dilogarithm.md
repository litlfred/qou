---
doc_id: on-the-garoufalidis-kashaev-state-integral-invariant
doc_title: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT"
section_id: sec-029-definition-of-the-angled-quantum-dilogarithm
section_title: "Definition of the Angled Quantum Dilogarithm"
section_number: null
pages: 29-31
source_pdf: On the Garoufalidis-Kashaev State-Integral Invariant.pdf
source_sha256: eda230da2a596783
toc_source: outline
doc_brief: "ON THE GAROUFALIDIS-KASHAEV STATE-INTEGRAL INVARIANT — 67 sections: Front matter; ACKNOWLEDGMENTS; ABSTRACT"
---
Definition of the Angled Quantum Dilogarithm
Definition 8 (Angled Quantum Dilogarithm as a Distribution [7]). The angle-dependent
quantum dilogarithm is defined as the tempered distribution
Ψa,c ∈S′( bB × B),
whose representative on test functions (α, x) ∈bB × (B \ {¨a−1}) is given almost
everywhere by the complex-valued formula:
Ψa,c(α, x) =
1
α((1 −¨ax)¨c) ·
∥¨ax∥˙c
∥1 −¨ax∥1−˙a.
20
Here, ∥·∥denotes the absolute value on F ×, and the expression is well-defined except
at the singularity x = ¨a−1. The interpretation as a tempered distribution ensures
that all convolution, Fourier, and integral identities involving Ψa,c are valid in the
sense of distributions.
Definition 9 (Angled quantum dilogarithm as a Distribution [7]). Fix an angle pair
a = (˙a, ¨a), c = (˙c, ¨c) ∈C = R × F ×. Define
Ψa,c ∈S′(A)
to be the tempered distribution whose representative on (α, x) ∈c
F × × (F × \ {¨a−1})
is
Ψa,c(α, x) =
1
α((1 −¨ax)¨c)
∥¨ax∥˙c
∥1 −¨ax∥1−˙a
(the expression is well-defined except at the singularity x = ¨a−1.). The interpretation
as a tempered distribution ensures that all convolution, Fourier, and integral identities
involving Ψa,c are valid in the sense of distributions (see [7] Lemma #).
Specialization to the inverse Fourier transform
The conjugate form is given by:
¯Ψa,c(α, x) := Ψ¯a,¯c(α, x) = α
1 −x/¨a
¨c

·
∥x/¨a∥˙c
∥1 −x/¨a∥1−˙a.
Setting (a, c) = (0, 0) gives ¨a = ¨c = 1 and ˙a = ˙c = 0. Hence from the conjugate
formula
¯Ψ0,0(α, x) = α(1 −x)
|x|0
|1 −x|1 = α(1 −x)
|1 −x| .
21
Recall
˜φ(β, y) =
1
β(y −1)
1
∥1 −y−1∥, y̸ = 1,
and interpret β = −α as the inverse character β = α−1. With y = x−1:
˜φ(α−1, x−1) =
1
α−1(x−1 −1)
1
|1 −x| = α(x−1 −1)
1
|1 −x|.
Since x−1 −1 = (1 −x)/x and α(x−1 −1) = α(1 −x)α(x)−1, it follows
α(x) ˜φ(α−1, x−1) = α(1 −x)
|1 −x| = ¯Ψ0,0(α, x).
Thus the correct specialization is
¯Ψ0,0(α, x) = α(x) ˜φ(α−1, x−1).
