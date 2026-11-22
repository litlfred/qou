---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-022-43-a-deformation-of-the-gamma-kernel
section_title: "A deformation of the Gamma kernel"
section_number: 4.3
pages: 26-28
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
in the principal or in the complementary series cases. In [9] and [11], the authors show that
with such a choice of parameters, the z-measure, viewed as a point process on Z′, converges as
ξ tends to 1, without any scaling, to a determinantal point process with a correlation kernel
expressed only through the Gamma function. They call this kernel the ”Gamma kernel”. The
goal of this section is to show that such a statement still holds for the Christoﬀel deformation
of the z-measure of order one, i.e. with k = 1. Our argument is a slight modiﬁcation of
the one presented in [9], Theorem 2.3. As mentioned in the introduction, our result must
be compared with the one from [19], where a hierarchy of Palm deformations of the process
with the Gamma kernel is established.
Before stating the Theorem, we give some deﬁnitions: for a ∈Z′, we deﬁne:
gz,z′(a) :=
p
Γ(z −a + 1/2)Γ(z′ −a + 1/2)Γ(−z + a + 1/2),
(23)
26
and for u ∈R and a ∈Z′, we set:
hz,z′(u, a) =
Γ(z′ −z)
fz,z′(u)gz,z′(a),
(24)
recalling that fz,z′(u) has been deﬁned in (17). We will denote by h′
z,z′(u, a) the derivative
of hz,z′(u, a) with respect to u. We will also use the notation
φa(u; z, z′, ξ) = ψ′
a(u; z, z′, ξ) −log(ξ)
2
ψa(u; z, z′, ξ),
(25)
recalling that ψa(u; z; z′, ξ) has been deﬁned in (14).
Theorem 4.5. Let (z, z′) be admissible parameters either in the principal or in the comple-
mentary series cases, and let K1
z,z′,ξ be the correlation kernel of the Christoﬀel deformation
of order 1 at u ∈R deﬁned by (16). We have, for all x, y ∈Z′, x̸ = y:
lim
ξ→1(1 −ξ)2K1
z,z′,ξ(x, y) =
Cz,z′
|(x −u)(y −u)|
Az,z′(x, y)
Φz,z′,0,−1(u)2(x −y)
where:
Az,z′(x, y) =
2
X
i,j=0
Φz,z′,a(i)b(i)(u)Φz,z′,a(j)+1,b(j)+1(u)Ψz,z′,i,j(x, y),
Ψz,z′,i,j(x, y) = hz,z′(x, −1/2 + i)hz′,z(y, 1/2 + j) + hz′,z(x, −1/2 + i)hz,z′(y, 1/2 + j)
−hz,z′(x, 1/2 + j)hz′,z(y, −1/2 + i) −hz′,z(x, 1/2 + j)hz,z′(y, −1/2 + i),
Φz,z′,a(i),b(i)(u) = hz,z′(u, −1/2 + a(i))h′
z′,z(u, −1/2 + b(i))
+ hz′,z(u, −1/2 + a(i))h′
z,z′(u, 1/2 + b(i))
−hz,z′(u, −1/2 + b(i))h′
z′,z(u, −1/2 + a(i))
−hz′,z(u, 1/2 + b(i))h′
z,z′(u, −1/2 + a(i)),
a(0) = −1, a(1) = a(2) = 0
;
b(0) = b(1) = −2, b(2) = −1,
Cz,z′ = (z + 3)(z + 2)(z + 1)(z′ + 2)(z′ + 1)z′.
The diagonal entries are obtained by l’Hospital rule.
27
Remark 4.6. An explicit expression for the function Ψz,z′,i,j(x, y) may be found from:
hz,z′(x, a)hz′,z(y, b) + hz′,z(x, a)hz,z′(y, b) −hz,z′(x, b)hz′,z(y, a) −hz′,z(x, b)hz,z′(y, a)
= Γ(z −z′)Γ(z′ −z)
×
Γ(x + z + 1/2)Γ(x + z′ + 1/2)Γ(y + z + 1/2)Γ(y + z′ + 1/2)
Γ(z −a + 1/2)Γ(z′ −a + 1/2)Γ(z −b + 1/2)Γ(z′ −b + 1/2)
1/2
×

1
Γ(−z + a + 1/2)Γ(−z′ + b + 1/2)Γ(x + z′ + 1/2)Γ(y + z + 1/2)
+
1
Γ(−z′ + a + 1/2)Γ(−z + b + 1/2)Γ(x + z + 1/2)Γ(y + z′ + 1/2)
−
1
Γ(−z′ + a + 1/2)Γ(−z + b + 1/2)Γ(x + z′ + 1/2)Γ(y + z + 1/2)
−
1
Γ(−z + a + 1/2)Γ(−z′ + b + 1/2)Γ(x + z + 1/2)Γ(y + z′ + 1/2)

.
It only involves the Gamma function. A similar expression for the function Φz,z′,j can be
obtained in the same way, and would involve the Gamma function and its ﬁrst derivative.
Remark 4.7. The factor (1−ξ)2 appearing in our statement should be interpreted as (1−ξ)2k
in order to recover Borodin-Olshanski Theorem from [9] and [11] in the case k = 0.
