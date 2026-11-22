---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-031-72-the-twisted-universal-k-matrix-in-the-kac-moo
section_title: "The twisted universal K-matrix in the Kac-Moody case"
section_number: 7.2
pages: 38-41
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
assumptions from Section 5.4 and Assumption ( τ0) from the previous subsection.
To construct the desired Bc,s-module homomorphism we require one additional
ingredient. Consider the function γ :I → K(q1/d) deﬁned by
γ(i) =
{
1 if i ∈X
cis(τ (i)) if i ∈I \X(7.7)
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 39
and note that by (7.4) and (7.5) one has γ(ττ 0(i)) = γ(i) for all i ∈I. Now assume
thatξ :P → K(q1/d)× is a function satisfying the following recursion
ξ(µ +αi) = γ(i)q−(αi,Θ( αi))−(µ,αi+Θ( αi))ξ(µ) for all µ ∈P , i ∈I.(7.8)
Such a function exists. Indeed, we may take an arbitrary map on an y set of repre-
sentatives of P/Q and uniquely extend it to P using (7.8).
Lemma 7.4. Let ξ : P → K(q1/d)× be any function which satisﬁes the recursion
(7.8). Then one has
ξ(µ +λ) = q−(λ,λ)−2(µ,λ)ξ(µ) for all µ ∈P , λ ∈QX.(7.9)
Proof. We prove this by induction on the height of λ. Assume that (7.9) holds for
a given λ ∈QX . Then one obtains for any i ∈X the relation
ξ(µ +λ +αi) = q−(αi,αi)−2(µ+λ,αi)ξ(µ +λ)
=q−(αi,αi)−2(µ+λ,αi)−(λ,λ)−2(µ,λ)ξ(µ)
=q−(λ+αi,λ+αi)−2(µ,λ+αi)ξ(µ)
which completes the induction step. □
As in Example 3.3 we may consider ξ as an element of U . The next theorem
shows that the element XξT −1
wX ∈ U deﬁnes a Bc,s-module isomorphism between
twisted modules in Oint.
Theorem 7.5. Letξ :P → K(q1/d)× be a function satisfying the recursion (7.8).
Then the element K′ = XξT −1
wX ∈ U deﬁnes an isomorphism of Bc,s-modules
K′
M :M tw◦τ0 →Mτ0τ, m ↦→XM ◦ξM ◦ (T −1
wX )M (m)
for any M ∈Ob(Oint). In other words, the relation
K′ tw(τ0(x)) = τ0(τ (x)) K′
holds in U for all x ∈Bc,s.
Proof. It suﬃces to check that
K′
M
(
x •tw◦τ0m) = x •ττ 0 K′
M (m) for all m ∈M(7.10)
wherex is one of the elements Kλ,Ei,Fi, or Bj forλ ∈QΘ ,i ∈X, and j ∈I \X.
Moreover, it suﬃces to prove the above relation for a weight vecto r m ∈ Mµ. In
the following we will suppress the subscript M for elements in U acting on M .
Case 1: x = Kλ for some λ ∈ QΘ . In this case wX (λ) = −τ (λ). Moreover, as
τ0 ∈ Aut(A,X ) one has τ0(wX (λ)) = wX (τ0(λ)). Hence one obtains
K′(Kλ •tw◦τ0m) = X ◦ξ ◦T −1
wX (tw(τ0(Kλ))m)
= X ◦ξ ◦T −1
wX (K−τ0(λ)m)
= X
(
K−wXτ0(λ)(ξ ◦T −1
wX (m))
)
=K−wXτ0(λ)X ◦ξ ◦T −1
wX (m)
=Kτ0τ (λ)K′(m)
=Kλ •τ0τ K′(m).
40 MARTINA BALAGOVI ´C AND STEF AN KOLB
Case 2: x = Ei for some i ∈ X. By relation (7.2) applied to MX we have
T −1
wX (Fi) = −Eτ (i)Kτ (i). Using this and the recursion (7.8) one obtains
K′(Ei •tw◦τ0m) = X ◦ξ ◦T −1
wX (−K −1
τ0(i)Fτ0(i)m)
= X ◦ξ
(
q(αi,αi)Eττ 0(i)K 2
ττ 0(i)T −1
wX (m)
)
= X
(
ξ(wX (µ)+αττ 0(i))ξ(wX (µ))−1q(αi,αi)+2(wX (µ),ατ 0τ (i))Eττ 0(i)ξ ◦T −1
wX (m)
)
(7.8)
= Eττ 0(i)X ◦ξ ◦T −1
wX (m)
= Ei •τ0τ K′(m).
This conﬁrms relation (7.10) for x =Ei wherei ∈X. The case x =Fi fori ∈X is
treated analogously.
Case 3: x = Bj = Fj −γ(j)TwX (Eτ (j))K −1
j +sjK −1
j for some j ∈ I \X. We
calculate
K′(Bj •tw◦τ0m) = X ◦ξ ◦T −1
wX
(
tw ◦τ0(Bj)m
)
(7.6)
= X ◦ξ
(
tw ◦τ0(T −1
wX (Bj))T −1
wX (m)
)
(7.6)
= X ◦ξ
((
T −1
wX (−Eτ0(j)Kτ0(j)) +γ(j)K −1
ττ 0(j)Fττ 0(j)KwX (ατ 0 (j))
+sjKwX (τ0(j))
)
T −1
wX (m)
)
= X ◦ξ
((
Fττ 0(j)γ(j)q(αj,αj )−(wX (µ),ατ τ 0 (j)+Θ( ατ τ 0 (j)))
−T −1
wX (Eτ0(j))Kτ0τ (j)q−(wX (µ),ατ 0 τ (j)+Θ( ατ 0 τ (j)))
+sjKτ0τ (j)q−(wX (µ),ατ 0 τ (j)+Θ( ατ 0 τ (j))))
T −1
wX (m)
)
.
To simplify the last term, recall from (5.7) that sτ0τ (j) = sj = 0 unless Θ( αj) =
−αj, in which case ατ0τ (j) + Θ( ατ0τ (j)) = 0. Additionally moving ξ to the right
one obtains
K′(Bj •tw◦τ0m) =
= X
((
Fττ 0(j)γ(j)q(αj,αj )−(wX (µ),ατ τ 0 (j)+Θ( ατ τ 0 (j)))ξ(wX (µ) −ατ0τ (j))
ξ(wX (µ))(7.11)
−T −1
wX (Eτ0(j))Kτ0τ (j)q−(wX (µ),ατ 0τ (j)+Θ( ατ 0 τ (j)))ξ(wX (µ)+wXατ0(j))
ξ(wX (µ))
+sτ0τ (j)Kτ0τ (j)
)
ξ ◦T −1
wX (m)
)
.
To simplify the above expression observe that
ξ(wX (µ) +wXαi)
(7.9)
= q−(wXαi−αi,wXαi−αi)−2(wX (µ)+αi,wXαi−αi)ξ(wX (µ) +αi)
= q−2(wX (µ),wXαi−αi)ξ(wX (µ) +αi)
(7.8)
= γ(τ0τ (i))q−(αi,Θ( αi))+(wX (µ),ατ (i)+Θ( ατ (i))ξ(wX (µ))
UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS 41
fori ∈I \X. Inserting this formula for i =τ0(j) into Equation (7.11) and applying
the recursion (7.8) also to the ﬁrst summand one obtains
K′(Bj •tw◦τ0m) = X
((
Fττ 0(j) −γ(τ (j))q−(αj,Θ( αj ))T −1
wX (Eτ0(j))Kτ0τ (j)+(7.12)
+sτ0τ (j)Kτ0τ (j)
)
ξ ◦T −1
wX (m)
)
.
Now set
βi = (−1)2αi(ρ∨
X )q(2ρX,αi) for i ∈I \X.
In view of [Lus94, 37.2.4] one has
TwX (Ei) = β−1
i T −1
wX (Ei) for all i ∈I \X,(7.13)
see also the proof of [BK15, Lemma 2.9]. Hence (7.12) gives
K′(Bj •tw◦τ0m) = X
((
Fττ 0(j)−
−γ(τ (j))q−(αj,Θ( αj))βτ0(j)TwX (Eτ0(j))K −1
τ0τ (j) +sjKτ0τ (j))
)
ξ ◦T −1
wX (m)
)
.
In view of the relation
γ(τ (j))q−(αj,Θ( αj ))βτ0(j) =s(τ (j))cj
one now obtains
K′(Bj •tw◦τ0m) = X
(
Bτ0τ (j)ξ ◦T −1
wX (m)
)
=Bτ0◦τ (j)K′(m) = Bj •ττ 0 K′(m)
which completes the proof of the Theorem. □
For later reference we note that relation (7.13) implies that the elem ent Xi
deﬁned by (5.4) satisﬁes the relation
Xi = −s(i)q−(2ρX,αi)T −1
wX (Eτ (i)) for all i ∈I \X,(7.14)
see also (5.1), (5.2) and property (3) in Deﬁnition 5.1 of an admissible p air.
Remark 7.6. The function ξ is an important ingredient in the construction of
the twisted K-matrix K′ and should be compared to the recursively deﬁned function
f involved in the construction of the commutativity isomorph isms [Lus94, 32.1.3] .
The recursion (7.8) is a necessary and suﬃcient condition on ξ for X ◦ξ ◦T −1
wX :
M tw◦τ0 →Mτ0τ to be a Bc,s-module homomorphism.
