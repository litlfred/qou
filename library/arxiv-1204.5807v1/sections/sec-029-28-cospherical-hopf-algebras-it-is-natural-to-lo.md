---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-029-28-cospherical-hopf-algebras-it-is-natural-to-lo
section_title: "Cospherical Hopf algebras. It is natural to look at the notions that"
section_number: 2.8
pages: 14-16
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect exampl es."
---
insure that the category of comodules of a Hopf algebra is piv otal or spherical.
This was done in [Bi, O].
Deﬁnition 2.16. A cospherical Hopf algebra is a pair (H,t ), where H is a
Hopf algebra and t ∈ Alg(H, k) is such that
S 2(x(1))t(x(2)) = t(x(1))x(2), x ∈H,(2.20)
trV ((idV ⊗t)ρVϑ) = trV ((idV ⊗t−1)ρVϑ), ϑ ∈ EndH (V ),(2.21)
5These control the passage from left to right integrals.
FROM HOPF ALGEBRAS TO TENSOR CATEGORIES 15
for all V ∈ CorepH. We say that t ∈ Alg(H, k) is a copivot when it satisﬁes
(2.20); pairs (H,t ) with t a copivot are called copivotal Hopf algebras . A
cospherical element is a copivot that fulﬁlls (2.21). Let H be a cospherical
Hopf algebra. Then the category CorepH is spherical; in fact, the left and
right traces are given by the sides of (2.21).
The set Alg(H, k) is a subgroup of the group Hom⋆(H, k) of convolution-
invertible linear functionals, which in turn acts on End(H) on both sides.
Hence (2.20) can be written as S 2∗t =t∗idH or else as S 2 =t∗idH ∗t−1. The
copivot is not unique but it is determined up to multiplicati on by an element
in Alg(H, k) that centralizes idH . The antipode of a copivotal Hopf algebra is
bijective, with inverse given by S −1(x) = ∑ t−1(x(1))S(x(2))t(x(3)), x ∈H.
The following statement is proved exactly as Proposition 2. 1.
Proposition 2.17. A copivotal Hopf algebra (H,t ) is cospherical if and only
if (2.21) holds for all simple H-comodules. □
Examples 2.18. (a) Assume that H is ﬁnite-dimensional. Then H is
copivotal (resp., cospherical) iﬀ H ∗ is pivotal (resp., spherical).
(b) Any involutory Hopf algebra is cospherical with t =ε.
(c) A copivotal Hopf algebra with involutive copivot is cosp herical.
(d) Condition (2.20) is multiplicative on x; also, it holds for x ∈G(H).
(e) Let H be a pointed Hopf algebra generated as an algebra by G(H)
and a family (xi)i∈I , where xi is (gi, 1) skew-primitive. Assume that
gixig−1
i =qixi, with qi ∈ k× \ {1} for all i ∈I. If t ∈ Alg(H, k), then
t(xi) = 0 , i ∈I. Hence t is a copivot iﬀ t(gi) = q−1
i , for all i ∈I.
(f) Let H be a pointed Hopf algebra as in item (e) and t ∈ Alg(H, k) a
copivot. Then H is cospherical iﬀ t(g) ∈ {±1} for all g ∈G(H).
(g) The notion of coribbon Hopf algebra is formally dual to th e notion
of ribbon Hopf algebra, see [H, LT]. Coribbon Hopf algebras a re
cospherical. For instance, the quantized function algebra Oq(G) of a
semisimple algebraic group is cosemisimple and coribbon, w hen q is
not a root of 1.
We recall now the contruction of universal copivotal Hopf al gebras.
Deﬁnition 2.19. [Bi] Let F ∈ GLn(k). The Hopf algebra H(F ) is the
universal algebra with generators (uij)1≤i,j≤n, (vij)1≤i,j≤n and relations
uvt =vtu = 1, vFu tF −1 =Fu tF −1v = 1.
The comultiplication is determined by ∆( uij) = ∑
kuik ⊗ukj , ∆( vij) =∑
kvik ⊗vkj and the antipode by S(u) = vt, S(v) = Fu tF −1. The Hopf
algebraH(F ) is copivotal, the copivot being tF (u) = (F −1)t andtF (v) = F .
Let H be a Hopf algebra provided with V ∈ CorepH of dimension n
such that V ∼= V ∗∗. Then there exist a matrix F ∈ GLn(k), a coaction
βV :V →V ⊗H(F ) and a Hopf algebra morphism π :H(F ) →H such that
(idV ⊗π)βV =ρV .
