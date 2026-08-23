---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R)"
section_id: sec-032-9-representation-theoretic-meaning-for-certain-i
section_title: "Representation theoretic meaning for certain integral transforms"
section_number: 9
pages: 88-89
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum Double and Harmonic Analysis on GL+_q(2,R) — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual"
---
tegral transforms
In this section, we state without proof certain integral transfor mations of Gb that
arise in the calculations of certain representation relations.
Proposition 9.1. The pentagon equation W23W12 =W12W13W23 is equivalent to
the 4-5 relation (Lemma 3.10)
Gb(α)Gb(β)Gb(γ)
Gb(α +γ)Gb(β +γ) =
∫
C
dτe −2πγτ Gb(α +iτ )Gb(β +iτ )
Gb(α +β +γ +iτ )Gb(Q +iτ ). (9.1)
By a change of variables and using the reﬂection formula, it c an be rewritten as
Gb(α +γ)Gb(β +γ)Gb(α)Gb(β)
Gb(α +β +γ) =
∫
C
dτe −2πi(β+iτ )(α+iτ )Gb(α +iτ )Gb(β +iτ )Gb(γ−iτ )Gb(−iτ ).
(9.2)
Scaling all the variables by b and taking the limit b−→ 0 by applying Theorem 3.5,
we recover precisely Barnes’ ﬁrst lemma:
Γ(a +c)Γ(b +c)Γ(a)Γ(b)
Γ(a +b +c) = 1
2π
∫
C
Γ(a +iτ )Γ(b +iτ )Γ(c−iτ )Γ(−iτ )dτ (9.3)
in the special case for d = 0.
Next, as noted in Section 8.4, by comparing Wm =∫∫ ⊕T λ,t/2dtdµ(λ) as corep-
resentation, we obtain the following relation that is ﬁrst observed b y Volkov [44]:
Proposition 9.2. The 6-9 relation for Gb(x) can be written as
∫
C
e−2πτ (δ−iτ )Gb(α +iτ )Gb(β +iτ )Gb(γ +iτ )Gb(δ−iτ )Gb(−iτ )
Gb(α +β +γ +δ +iτ ) dτ
= Gb(α)Gb(β)Gb(γ)Gb(α +δ)Gb(β +δ)Gb(γ +δ)
Gb(α +β +δ)Gb(α +γ +δ)Gb(β +γ +δ) , (9.4)
88
where the contour goes along R and separates the increasing and decreasing sequence
of poles. By the asymptotic properties of Gb, the integral converges for any choice
of parameters.
Again by scaling all the variables by b and applying Theorem 3.5, we recover
Barnes’ second lemma:
∫
C
Γ(a +iτ )Γ(b +iτ )Γ(c +iτ )Γ(d−iτ )Γ(−iτ )
Γ(a +b +c +d +iτ ) dτ
= Γ(a)Γ(b)Γ(c)Γ(a +d)Γ(b +d)Γ(c +d)
Γ(a +b +d)Γ(a +c +d)Γ(b +c +d) , (9.5)
which in turn is a generalization of Pfaﬀ-Saalsch¨ utz’s sum
∑
j≥0
(n +m +l +k−j)!
(m−j)!(l−j)!(k−j)!(n +j)!j! = (n +m +l)!(n +m +k)!(n +l +k)!
m!l!k!(n +m)!(n +l)!(n +k)! .
(9.6)
Finally, in [46] an alternative description of the multiplicative unitary lyin g
instead inA⊗A is deﬁned to be (slightly modiﬁed to ﬁt our deﬁnition):
V =gb(B−1⊗q−1BA−1)e
i
2πb 2 log(qAB −1)⊗log A−1
, (9.7)
so that
V (x⊗ 1)V ∗ = ∆( x). (9.8)
On comparing
W ∗(1⊗x)W = ∆( x) = V (x⊗ 1)V ∗ (9.9)
as operators onH⊗H , we obtain a new relation involving Gb(x), which is essentially
the same as the relation in [42, Theorem 5.6.7] in the case n = 1:
Proposition 9.3. The 3-2 relation is given by
∫
C
Gb(α +iτ )Gb(β−iτ )Gb(γ−iτ )e−2πi(β−iτ )(γ−iτ )dτ =Gb(α +γ)Gb(α +β),
(9.10)
where the contour goes along R and separates the poles for iτ and−iτ . By the
asymptotic properties for Gb, the integral converges for Re(α−β−γ)< Q
2 .
