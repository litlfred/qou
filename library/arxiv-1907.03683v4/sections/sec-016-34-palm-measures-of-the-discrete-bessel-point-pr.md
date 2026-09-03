---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-016-34-palm-measures-of-the-discrete-bessel-point-pr
section_title: "Palm measures of the discrete Bessel point process. In regards of subsection"
section_number: 3.4
pages: 17-18
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
2.4 and Proposition 2.7, we can now give a description of the Palm measures of the discrete
Bessel point process S0
∗(Pα), the determinantal point process with kernel Kα given by (4).
17
Theorem 3.3. Let ˜u1, ..., ˜uk ∈Z be pairwise distinct. For α > 0, let (S0
∗(Pα))k be the
reduced Palm measure of the discrete Bessel point process at ˜u1, ..., ˜uk. Then, the process
(S0
∗(Pα))k is a determinantal process with kernel
K ˜u1,...,˜uk
α
(x, y) :=
α
2k+1
2
C2
k,k
Qk
i=1 |(x −˜ui)(y −˜ui)|
Ak,k(x)Ak,1+k(y) −Ak,k(y)Ak,1+k(x)
x −y
.
Remark 3.4. From [5], Theorem 4.1, the kernel K ˜u1,...,˜uk
α
serves as the correlation kernel of
the TASEP with initial step condition at time t = α under the condition that the position
˜u1, ..., ˜uk are occupied.
Proof of Theorem 3.3. By Propositions 2.7 and 2.1, the reduced Palm measure at ˜u1 +
N, ..., ˜uk + N of the N-th Charlier ensemble with parameter α/N, shifted by −N, is a
determinantal point process with kernel Kα/N,k
N−k (x + N, y + N). The case k = 0 of Theorem
3.1 together with Proposition 2.6 imply that the reduced Palm measure of the N-th Charlier
ensemble at ˜u1 + N, ..., ˜uk + N shifted by −N converges to the reduced Palm measure of the
discrete Bessel point process at points ˜u1, ..., ˜uk. On the other hand, slight modiﬁcations of
the proof of Theorem 3.1 (precisely, we just replace N by N −k) lead to
lim
N→+∞Kα/N,k
N−k (x + N, y + N) = K ˜u1,...,˜uk
α
(x, y).
We deduce from this fact that the latter kernel K ˜u1,...,˜uk
α
serves as a kernel for the point
process (S0
∗(Pα))k.
□
