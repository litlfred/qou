---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-019-6-from-ptolemy-coordinates-to-shapes
section_title: "From Ptolemy coordinates to shapes"
section_number: 6
pages: 17-18
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
We now deﬁne a monomial mapµ from Ptolemy assignments to shape assignments. Given
a Ptolemy assignment c on a simplex ∆ 3
n, deﬁne z : ∆3
n−2(Z)× ˙∆3
2(Z) by
(6.1)
z1100
s =z0011
s = cs+1001cs+0110
cs+1010cs+0101
z0110
s =z1001
s = cs+0101cs+1010
cs+1100cs+0011
z1010
s =z0101
s = −cs+1100cs+0011
cs+1001cs+0110
.
Lemma 6.1. The assignment (6.1) is a shape assignment, i.e. we have a well deﬁned map
(6.2) µ:{Ptolemy assignments on ∆ 3
n}→{ shape assignments on ∆ 3
n}.
Proof. Using the Ptolemy relation, we obtain
1
1−z0101
s
= 1
1 + cs+1100cs+0011
cs+1001cs+0110
= cs+1001cs+0110
cs+1100cs+0011 +cs+1001cs+0110
= cs+1001cs+0110
cs+1010cs+0101
=z1100
s .
The other two equations in (4.5) follow similarly. □
Lemma 6.2. The map µ respects pullbacks.
Proof. It is enough to prove this for the permutations σ01, σ12 and σ23. We prove it for σ01,
the other cases being similar. Since sgn( σ01) =−1, we must prove that
(6.3) ( µ(σ∗
01c))e
s = (µ(c)σ01(e)
σ01(s))−1.
We prove this for the edge e = 1100, the other cases being similar. Using (5.8), we obtain
(6.4) ( µ(σ∗
01c))1100
s = (σ∗
01c)s+1001(σ∗
01c)s+0110
(σ∗
01c)s+1010)(σ∗
01c)s+0101
= cs′+0101cs′+1010
cs′+0110cs′+1001
= (µ(c)1100
s′ )−1
where s′ =σ01(s). This proves (6.3), hence the result. □
Theorem 6.3. LetT be a concrete triangulation ofM, and let ct,∆ be a Ptolemy assignment
on (M,T ). The induced shape assignment on each simplex satisﬁes the generalized gluing
equations and thus induces a shape assignment on (M,T ). □
Corollary 6.4. The map µ induces a map µ: Pn(T )→Vn(T ). □
18 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
We divide the proof of Theorem 6.3 into three parts, one for each type of equation. The
idea is to prove the result for the local model near an integral point of each type. Although
the local model is not a manifold, Ptolemy assignments are deﬁned in the obvious way,
i.e. by identifying Ptolemy coordinates of identiﬁed faces via the pullback of the face pairing
permutations.
