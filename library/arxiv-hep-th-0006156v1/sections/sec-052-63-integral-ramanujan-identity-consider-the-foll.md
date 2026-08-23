---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-052-63-integral-ramanujan-identity-consider-the-foll
section_title: "Integral Ramanujan identity . Consider the following Fourier inte-"
section_number: 6.3
pages: 16-17
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
gral:
Ψ(u,v,w ) ≡
∫
R
eb(x +u)
eb(x +v)e2πiwx dx,(23)
where
ℑ(v +cb)> 0, ℑ(−u +cb)> 0, ℑ(v −u)< ℑw< 0.(24)
Restrictions (24) actually can be considerably relaxed by d eforming the in-
tegration path in the complex x plane, keeping the asymptotic directions of
the two ends within the sectors ±(| argx| −π/2) > argb. So, the enlarged
in this way domain for the variables u,v,w has the form:
| arg(iz)|<π − argb, z ∈ {w,v −u −w,u −v − 2cb}.(25)
Regarding eb(z) as a ‘non-compact’ analogue of the q-exponent ( x;q)∞,
deﬁnition (23) can be interpreted as the corresponding inte gral counterpart
of the Ramanujan sum:
1ψ1(x,y,z ) ≡
∑
n∈Z
(x;q)n
(y;q)n
zn.
The latter is known to be evaluated explicitly, the result be ing the famous
Ramanujan summation formula:
1ψ1(x,y,z ) = (q;q)∞(y/x;q)∞(xz;q)∞(q/xz;q)∞
(y;q)∞(q/x;q)∞(z;q)∞(y/xz;q)∞
.
Remarkably, integral (23) can be evaluated explicitly as we ll. Indeed, using
the residue method, we easily come to the following result:
Ψ(u,v,w ) = eb(u −v −cb)eb(w +cb)
eb(u −v +w −cb) e−2πiw (v+cb)+iπ (1−4c2
b )/ 12(26)
= eb(v −u −w +cb)
eb(v −u +cb)eb(−w −cb)e−2πiw (u−cb)−iπ (1−4c2
b )/ 12,(27)
STRONGLY COUPLED QUANTUM DISCRETE LIOUVILLE THEORY 17
where the two expressions in the right hand side are related t o each other
through the inversion relation (16). The similarity of this result with Ra-
manujan sum becomes very transparent if we rewrite the latte r in the form:
∑
n∈Z
(yq n;q)∞
(xqn;q)∞
zn = (y/x;q)∞(q/z;q)∞
(y/xz;q)∞
θq(xz)
θq(x)θq(z) (q;q)2
∞,(28)
where the θq-function is deﬁned by
θq(x) ≡ (q;q)∞(x;q)∞(q/x;q)∞ =
∑
n∈Z
qn(n−1)/ 2(−x)n.(29)
Comparing the inversion relation (16) with eqn (29), we conc lude that the
non-compact analogue of the θ-function is the Gaussian exponent, and the
structures of eqns (28) and (26) are now quite similar.
