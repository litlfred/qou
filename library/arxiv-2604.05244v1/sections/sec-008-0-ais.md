---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra Miguel Tierz"
section_id: sec-008-0-ais
section_title: "Ai(s +"
section_number: 0
pages: 27-28
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
doc_brief: "Edge universality in Floquet sideband spectra Miguel Tierz — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a"
---
O(A−1/3) uniformly on Q × [0, U] for any fixed U > 0. The rescaled kernel is the Riemann sum
bKA(s, t) = 1
κA
∞
X
r=0
ϕA
 r
κA
; s

ϕA
 r
κA
; t

(A.2)
with mesh 1/κA →0. The partial sum over r/κA ∈[0, U] converges uniformly on Q to
R U
0 Ai(s +
u) Ai(t + u) du.
Step 3: Tail control.
For U ≥M + 1 and s ∈[−M, M], the global tail bound gives |ϕA(u; s)| ≤
Ce−c(u−M) for u ≥M + 1, so |ϕA(u; s)ϕA(u; t)| ≤C2e−2c(u−M), which is integrable on [U, ∞) and
independent of A. The tail sum converges, as A →∞, to the corresponding integral, which can be
made arbitrarily small by taking U large. The same is true for
R ∞
U Ai(s + u) Ai(t + u) du.
27
Conclusion.
Combining Steps 2 and 3 gives supQ | bKA(s, t) −KAi(s, t)| →0. Since Q was arbi-
trary, the convergence is locally uniform on R2.
A.3
Photo-assisted noise from the correlator framework (sketch)
The photo-assisted noise formula (9.1) is a standard result of Floquet scattering theory [8, 9, 4].
Here we do not re-derive it but briefly sketch how it connects to the correlator C of the main text,
following [10], in order to make the appearance of the same discrete Bessel kernel in two different
observables transparent. The standard Floquet-scattering expression for zero-frequency PASN is
quadratic in the transmission block ˆtnm(E) =
√
T Jn−m(A) and in the reservoir occupations; after
inserting the double-step distribution (5.9) one recovers Eq. (9.1). The key identity linking the noise
integrand to the correlator C, valid at zero temperature where fL,R are sharp Fermi steps, is
X
m
fL(Em)[1 −fR(Em)] J2
n−m(A) = T −1
C(L)
nn −C(R)
nn

,
where C(L,R) are the correlators built from left and right reservoirs respectively. After carrying out
the energy integral and using the step structure, one recovers (9.1). The differentiation d/dV then
selects the Fermi-edge contribution, which is precisely K(disc)
A
(νV , νV )—the same kernel diagonal
that governs the fixed-E edge theorem. This is why the same Airy scaling appears in two a priori
different observables.
