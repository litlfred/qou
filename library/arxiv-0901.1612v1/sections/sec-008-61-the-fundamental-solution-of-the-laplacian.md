---
doc_id: arxiv-0901.1612v1
doc_title: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links"
section_id: sec-008-61-the-fundamental-solution-of-the-laplacian
section_title: "The fundamental solution of the Laplacian"
section_number: 6.1
pages: 18-20
source_pdf: 0901.1612v1.pdf
source_sha256: b4f3efcadd1e5caf
toc_source: outline
doc_brief: "Triple linking numbers, ambiguous Hopf invariants and integral formulas for three-component links — Three-component links in the 3-dimensional sphere were classi- fied up to link homotopy by John"
duplicate_of: "deturck-melvin-gluck-komendarczyk-shonkwiler-2008-triple-lin"
---
Proposition. The fundamental solution of the scalar Laplacian on the 3-torus T 3 is
given by the formula
ϕ(x, y, z) = −1
8π3
X ei(ℓx+my+nz)
ℓ2 + m2 + n2
where the sum is over all integers ℓ, m and n (positive and negative) with the exception
of ℓ= m = n = 0.
Even though we have expressed ϕ in terms of complex exponentials, the value of ϕ
is real for real values of x, y and z because of the symmetry of the coeﬃcients, and
can therefore also be expressed as a Fourier cosine series.
Figure 12 shows the graph of the corresponding fundamental solution of the scalar
Laplacian on the 2-torus T 2, displayed over the range −3π ≤x, y ≤3π. If we think
of the 2-torus as obtained from a square by identifying opposite sides, then this shows
the function ϕ to have a negative inﬁnite minimum at the single vertex, two saddle
points in the middle of the two edges, and a maximum in the middle of the square.
18
Triple linking numbers, ambiguous Hopf invariants and integral formulas
Figure 12. Fundamental solution of the scalar Laplacian on the 2-torus
Presumably the fundamental solution ϕ on the 3-torus displays a corresponding Morse-
like behavior.
6.2. Completing the proof of Theorem B. Now we have an explicit formula for
the fundamental solution ϕ of the scalar Laplacian on the 3-torus T 3, and we know that
both the scalar and vector Green’s operators act by convolution with ϕ. In particular,
if V is a smooth vector ﬁeld on T 3, then Gr(V ) = V ∗ϕ, that is,
Gr(V )(τ) =
Z
T 3 V (σ)ϕ(τ −σ) dσ.
To obtain the formula for the magnetic ﬁeld BS(V ), we take the negative curl of the
above formula and get
BS(V )(τ) = −∇τ × Gr(V )(τ) = −
Z
T 3 ∇τ × (V (σ)ϕ(τ −σ)) dσ
=
Z
T 3 V (σ) × ∇τϕ(τ −σ) dσ.
Then the helicity of V is given by
Hel(V ) =
Z
T 3 V (τ) • BS(V )(τ) dτ
=
Z
T 3×T 3 V (σ) × V (τ) • ∇σϕ(σ −τ) dσ dτ.
19
DeTurck, Gluck, Komendarczyk, Melvin, Shonkwiler and Vela-Vick
Applying this to the vector ﬁeld VL associated with our 3-component link L, we get
the desired formula for the Pontryagin invariant ν of gL:
ν(gL) = Hopf(gL) = Hel(VL) =
Z
T 3 BS(VL) • VL d(vol)
=
Z
T 3×T 3 VL(σ) × VL(τ) • ∇σϕ(σ −τ) dσ dτ.
Hence by Theorem A, Milnor’s µ-invariant of the 3-component link L is given by
µ(L) = 1
2 ν(gL) = 1
2
Z
T 3×T 3 VL(σ) × VL(τ) • ∇σϕ(σ −τ) dσ dτ,
