---
doc_id: arxiv-math-0604094v1
doc_title: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant"
section_id: sec-001-examples
section_title: "Examples"
section_number: null
pages: 12-15
source_pdf: 0604094v1.pdf
source_sha256: f0c4c36ab0acf537
doc_brief: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant — We study quantum invariant Zγ(M) for cusped hyperbolic"
---
cusped hyperbolic 3-manifolds.
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 13
4.1 Figure-Eight knot 41
We set K as the Figure-Eight knot 41 which is depicted as
It is well known that the complement of the ﬁgure eight knot, M = S 3 \ K, is given by two ideal
tetrahedra, and the triangulation induces the quantum invariant as
Zγ(Mu) =
∫
R
dp δC(p; u) ⟨p1, p2|S |p3, p4⟩
⟨
p4, p3|S −1|p2, p1
⟩
(4.1)
Modulus of two tetrahedra are given by w = ep4−p2 and z = ep1−p3. The developing map is drawn
in Fig. 3, and the meridian is read to be
w
z = e−2u
which shows that the condition δC(p; u) is
p4 − p2 − (p1 − p3) = −2 u
The complete hyperbolic structure is realized when u = 0.
Figure 3. Developing map of the complement of the ﬁgure-eight knot. The gray
ﬁlled triangle corresponds to top vertex of the tetrahedron(central vertex of circle
in (3.1)) with modulus w in projection of (3.1). A curve denotes a meridian of
cusp.
We then obtain
Zγ (Mu) = 1
4 π γ
∫
dx Φγ(x + i π + i γ)
Φγ(−x − 2 u − i π − i γ) e
−1
2iγ 4u(u+x) (4.2)
14 K. HIKAMI
In a limit γ → 0, we have
Zγ(Mu) ∼
∫
dx exp
( 1
2 iγ
(
Li2(ex) − Li2(e−x−2u) − 4 u (u + x)
) )
=
∫
dx exp
( 1
2 iγ VM(ex; eu)
)
(4.3)
where the potential function is set to be
VM(x; m) = Li2(x) − Li2
( 1
x m2
)
− 4 logm log(x m) (4.4)
To evaluate the integral (4.3), we may apply the saddle point method, and a condition (3.11)
reduces to
− x
m2 (1 − x) (1 − m2 x) = 1 (4.5)
From (3.12) the longitude is given by
1
m2 x (m2 x − 1) = ℓ (4.6)
Completeness condition m = 1 gives x = 1±
√
3 i
2 from (4.5). Substituting this solution for the
potential function (4.4), the imaginary part coincides wit h the hyperbolic volume of the ﬁgure-
eight knot V ol(S 3 \ 41) = 2.02988 · · ·.
For a deformed manifold Mu, we get an algebraic equation of ℓ and m by eliminating x
from (4.5) and (4.6) as
A(ℓ, m) = 0 (4.7)
Here A(ℓ, m) is the A-polynomial for the ﬁgure-eight knot;
A(ℓ, m) = −m4 + ℓ (1 − m2 − 2 m4 − m6 + m8) − ℓ2 m4 (4.8)
which can be expressed as in the Newton polygon as follows;



















0 1 0
0 −1 0
−1 −2 −1
0 −1 0
0 1 0



















We note that a set of equations (4.5) and (4.6) gives
2 v = −2 π i + 4
√
3 iu + 16 i√
3
u3 + 368 i
15
√
3
u5 + 2848 i
45
√
3
u7 + · · ·
which coincides with a result in Ref. 44 under (3.15).
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 15
