---
doc_id: arxiv-2604.05244v1
doc_title: "Edge universality in Floquet sideband spectra"
section_id: sec-026-proof-of-the-soft-edge-airy-limit-theorem-61
section_title: "Proof of the soft-edge Airy limit (Theorem 6.1)"
section_number: null
pages: 27-28
source_pdf: 2604.05244v1.pdf
source_sha256: a5097e763dd89d06
toc_source: outline
doc_brief: "Edge universality in Floquet sideband spectra — We show that, for non-interacting fermions under a monochromatic phase drive (Tien– Gordon regime), the outgoing sideband occupations at a sharp Fermi"
---
Proof of the soft-edge Airy limit (Theorem 6.1)
The proof combines the turning-point estimate (6.5) with a Riemann-sum argument.
Step 1: Pointwise approximation.
The Debye–Olver uniform asymptotic [21] for integer order
n near argument A gives κAJn(A) = Ai((n −A)/κA) + O(A−2/3) uniformly on compact sets.
Composing with the floor in the rescaling νA(s) = ⌊A + sκA⌋introduces a shift δ/κA with |δ| ≤1
in the Airy argument. By Lipschitz continuity of Ai on compacts, the resulting error is O(A−1/3),
giving (6.5). The global tail bound |κAJνA(s)(A)| ≤Ce−cs for s ≥0 (the weaker corollary of the
piecewise estimate stated in the main text) carries over with the same adjustment.
Step 2: Riemann-sum approximation.
Fix a compact rectangle Q = [−M, M]2. For u ≥0
define ϕA(u; s) := κAJνA(s)+⌊uκA⌋(A). By the same argument as Step 1, ϕA(u; s) = Ai(s + u) +
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
