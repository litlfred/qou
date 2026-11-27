---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-024-61-a-recursive-formula-for-x
section_title: "A recursive formula for X"
section_number: 6.1
pages: 28-29
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
we translate relation (6.1) into a recursive formula for the compone nts Xµ.
Proposition 6.1. Let
X =
∑
µ∈Q+
Xµ ∈ ˆU +, with Xµ ∈U +
µ.
The following are equivalent:
(1) For all x ∈Bc,s one has xBX = Xx.
(2) For all i ∈I one has Bi
B
X = XBi.
(3) For all µ ∈Q+ and all i ∈I one has
ri(Xµ) = −(qi −q−1
i )
(
Xµ+Θ( αi)−αiciXi +siXµ−αi
)
,(6.2)
ir(Xµ) = −(qi −q−1
i )
(
q−(Θ( αi),αi)ciXiXµ+Θ( αi)−αi +siXµ−αi
)
.(6.3)
If these equivalent conditions hold then additionally
(4) For all µ ∈Q+ such that Xµ ⁄= 0, one has Θ(µ) = −µ.
Proof. (1) ⇒ (2) : Property (2) is the special case x =Bi of property (1).
(2) ⇔ (3) : Fix i ∈I. Using the deﬁnition (5.8) of Bi, deﬁnition (2.23) of Bi and
deﬁnition (5.12) of Bi
B
, we see that (2) is equivalent to
(
Fi +ciXiK −1
i +siK −1
i
)
X = X
(
Fi +ciXiKi +siKi
)
.(6.4)
Now compare the ( µ −αi)-homogeneous components for all µ ∈Q+. One obtains
that Equation (6.4) holds if and only if for all µ ∈Q+ one has
[Xµ,Fi] = −
(
Xµ−αi+Θ( αi)ciXi +siXµ−αi
)
Ki
+K −1
i
(
q−(αi,Θ( αi))ciXiXµ−αi+Θ( αi) +siXµ−αi
)
.
By (2.15), this is equivalent to relations (6.2) and (6.3) for all µ ∈Q+.
(3) ⇒ (4) : We prove this implication by induction on ht( µ). For µ = 0 there is
nothing to show. Assume that µ> 0. If Xµ ⁄= 0, then by (2.18), there exists i ∈I
such that ri(Xµ) ⁄= 0. By (6.2) we have either Xµ+Θ( αi)−αi ⁄= 0 or siXµ−αi ⁄= 0.
In the case Xµ+Θ( αi)−αi ⁄= 0, by induction hypothesis Θ( µ + Θ(αi) −αi) = −(µ +
Θ(αi) −αi), which implies Θ( µ) = −µ. In the case siXµ−αi ⁄= 0, the condition
s ∈ S implies that Θ( αi) = −αi, while the induction hypothesis implies that
Θ(µ −αi) = −(µ −αi). Together, this gives Θ( µ) = −µ.
(3) ⇒ (1) : We have already seen that (3) ⇒ (2) and hence xBX = Xx forx =Bi.
Let β ∈QΘ and assume that Xµ ⁄= 0. The implication (3) ⇒ (4) gives Θ( µ) =
−µ. On the other hand Θ( β) = β and therefore ( β,µ ) = 0. This implies that
KβXµK −1
β =q(β,µ)Xµ = Xµ and consequently xBX = Xx for all x ∈U 0
Θ .
Finally, let i ∈X and again assume that Xµ ⁄= 0. As Ki ∈U 0
Θ and Fi =Bi, we
already know that ad( Ki)(Xµ) = Xµ and ad(Fi)(Xµ) = 0. Hence Xµ is the lowest
weight vector for the left adjoint action of Uqi (sl2)i on Uq(g). As U + is locally
ﬁnite for the left adjoint action of U +, we conclude that Xµ is also a highest weight
vector, and hence
0 = ad(Ei)(Xµ) = EiXµ −KiXµK −1
i Ei =EiXµ − XµEi.
ThusEiXµ = XµEi and consequently xBX = Xx for all x ∈ MX .
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 29
This proves that the relation xBX = Xx holds for the generators of the algebra
Bc,s and hence it holds for all x ∈Bc,s. □
The proof of the implication (3) ⇒ (4) only refers to Xµ′ withµ′ ≤µ. Hence we
get the following corollary.
Corollary 6.2. Letµ ∈Q+ and let (Xµ′ )µ′≤µ∈Q+ , with Xµ′ ∈U +
µ′ , be a collection
of elements satisfying (6.2) and (6.3) for all µ′ ≤µ and all i ∈I. If Xµ ⁄= 0 then
Θ(µ) = −µ.
