---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-038-92-the-coproduct-of-the-quasi-k-matrix-x
section_title: "The coproduct of the quasi K-matrix X"
section_number: 9.2
pages: 47-49
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
K-matrix as X = ∑
µ∈Q+ Xµ ∈ U with Xµ ∈U +
µ . Deﬁne
XK2 =
∑
µ∈Q+
Kµ ⊗ Xµ ∈ U (2)
0 .(9.6)
This element will appear as a factor in the coproduct of X.
Lemma 9.3. For any i ∈I one has
(1 ⊗ri)(XK2) = (qi −q−1
i )XK2 ·
(
ρiKαi−Θ( αi) ⊗T −1
wX (Eτ (i)) −siKi ⊗ 1
)
in U (2) whereρi =cτ (i)s(i)q−(αi,Θ( αi)), in particular ρi =si = 0 if i ∈X.
48 MARTINA BALAGOVI ´C AND STEF AN KOLB
Proof. By Equation (6.2) one has
(1 ⊗ri)(XK2) =
∑
µ∈Q+
Kµ ⊗ri(Xµ)
= −(qi−q−1
i )
∑
µ∈Q+
Kµ ⊗
(
ciXµ+Θ( αi)−αiXi +siXµ−αi
)
= −(qi−q−1
i )ci
∑
µ∈Q+
(Kµ+Θ( αi)−αi ⊗ Xµ+Θ( αi)−αi) (Kαi−Θ( αi) ⊗Xi)
− (qi−q−1
i )si
∑
µ∈Q+
(Kµ−αi ⊗ Xµ−αi ) (Ki ⊗ 1)
= −(qi−q−1
i )XK2
(
ciKαi−Θ( αi) ⊗Xi +siKi ⊗ 1
)
.(9.7)
By the explicit expression (7.14) for Xi and by relation (5.17) for ci one has
ciXi = −ρiT −1
wX (Eτ (i)).(9.8)
Inserting (9.8) into (9.7) one obtains the desired formula. □
By Proposition 6.1.(4) the element XK2 commutes with Fi ⊗Ej for all i,j ∈X
and hence
RX · XK2 = XK2 ·RX.(9.9)
Now we are ready to compute the coproduct ∆( X) ∈ U (2) of the quasi K-matrix
X ∈ U in terms of the elements R(τ,X ) deﬁned in (9.2) and XK2 deﬁned in (9.6).
Theorem 9.4. The intertwiner X satisﬁes the relation
∆(X) = ( X ⊗ 1) ·R(τ,X ) · XK2(9.10)
in U (2)
0 .
Proof. By the deﬁnition (2.4) of the coproduct of Uq(g) the left hand side of Equa-
tion (9.10) belongs to ∏
µ∈Q+U +Kµ ⊗U +
µ . The right hand side of (9.10) also
belongs to ∏
µ∈Q+U +Kµ ⊗U +
µ , as follows from the deﬁnition (9.6) of XK2 and
from Lemma 9.1. By Lemma 2.4 it hence suﬃces to show that
⟨y ⊗z,∆ (X)⟩ =
⟨
y ⊗z, (X ⊗ 1) ·R(τ,X ) · XK2
⟩
(9.11)
for all y,z ∈ U −. By linearity it suﬃces to show this in the case where z =
Fi1Fi2...F ir is a monomial in the generators Fi of U −. We perform induction on
r.
Forr = 0, we have z = 1 and both sides of (9.11) equal ⟨y, X⟩. Now assume that
(9.11) holds for all y ∈ U − and all monomials z ∈ U − of length shorter or equal
than r. Then we get for any i ∈I the relation
⟨y ⊗zFi,∆ X⟩
(2.9)
= ⟨yzFi, X⟩
(2.17)
= −1
qi −q−1
i
⟨yz,ri(X)⟩
(6.2)
=
⟨
yz, X(ciXi +si)
⟩
(9.8)
= −
⟨
yz, X(ρiT −1
wX (Eτ (i)) −si)
⟩
,
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 49
where as before ρi =cτ (i)s(i)q−(αi,Θ( αi)). By induction hypothesis we obtain
⟨y ⊗zFi,∆ X⟩ = −
⟨
y ⊗z,ρi(X ⊗ 1) ·R(τ,X ) · XK2 ·∆(T −1
wX (Eτ (i)))
⟩
(9.12)
+
⟨
y ⊗z,si(X ⊗ 1) ·R(τ,X ) · XK2
⟩
.
On the other hand, using Lemma 9.2 and Lemma 9.3 one gets
− 1
qi −q−1
i
(1 ⊗ri)
(
(X ⊗ 1) ·R(τ,X ) · XK,2
)
= −ρi(X ⊗ 1) ·R(τ,X ) ·RX · (T −1
wX (Eτ (i)) ⊗ 1) ·RX · (Ki ⊗Ki)XK2(1 ⊗K −1
i )
−ρi(X ⊗ 1) ·R(τ,X ) · XK2 · (Kαi−Θ( αi) ⊗T −1
wX (Eτ (i)))
+si(X ⊗ 1) ·R(τ,X ) · XK2 · (Ki ⊗ 1).
Using the above formula, Equation (9.9), and again Proposition 6.1.(4 ) one obtains
⟨
y ⊗zFi, (X ⊗ 1)R(τ,X )XK2
⟩
= − 1
qi −q−1
i
⟨
y ⊗z, (1 ⊗ri)((X ⊗ 1) ·R(τ,X ) · XK,2)
⟩
= −ρi
⟨
y ⊗z, (X ⊗ 1) ·R(τ,X ) · XK2 ·RX · (T −1
wX (Eτ (i)) ⊗ 1) ·RX
⟩
(9.13)
−ρi
⟨
y ⊗z, (X ⊗ 1) ·R(τ,X ) · XK,2 · (K−Θ( αi) ⊗T −1
wX (Eτ (i)))
⟩
+si
⟨
y ⊗z, (X ⊗ 1) ·R(τ,X ) · XK,2
⟩
.
Now we want to compare Equation (9.12) with Equation (9.13). If i ∈X then both
expressions vanish and hence coincide. Assume now that i ∈I \X. Applying T −1
wX
to the relation Eτ (i)Fτ (j)Kτ (j) =q−(αi,αj )Fτ (j)Kτ (j)Eτ (i) for j ∈X one sees that
T −1
wX (Eτ (i))Ej =q(αj,wX (ατ (i)))EjT −1
wX (Eτ (i)) for all j ∈X
and hence K−Θ( αi) ⊗T −1
wX (Eτ (i)) commutes with RX . Using (3.14) one now gets
∆(T −1
wX (Eτ (i))) = RX ·
(
T −1
wX (Eτ (i)) ⊗ 1 +K−Θ( αi) ⊗T −1
wX (Eτ (i))
)
·RX
=RX ·
(
T −1
wX (Eτ (i)) ⊗ 1
)
RX +K−Θ( αi) ⊗T −1
wX (Eτ (i)).
Inserting the above relation into (9.12) and comparing the outcome with (9.13) one
obtains ⟨
y ⊗zFi, (X ⊗ 1) ·R(τ,X ) · XK2
⟩
= ⟨y ⊗zFi,∆ (X)⟩
also for i ∈I \X. This completes the induction step. □
