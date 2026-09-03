---
doc_id: arxiv-math-9807106v2
doc_title: "An Extension of the Character Ring of sl(3) and Its Quantisat ion"
section_id: sec-004-6-quantised-q-characters
section_title: "Quantised ‘q’-characters"
section_number: 6
pages: 25-28
source_pdf: 9807106v2.pdf
source_sha256: e3cd089e3df5d71f
doc_brief: "An Extension of the Character Ring of sl(3) and Its Quantisat ion — We construct a commutative ring with identity which extends the ring of characters of ﬁnite dimensional representations of sl(3)."
---
Recall ﬁrst the integrable case where the ‘classical’ g characters χλ , λ ∈ P+ are
converted into C-valued ‘q’-characters, labelled by the set {λ ∈P k
+} of integrable highest
weights at (positive) integer level k. Essentially one turns the formal exponentials eλ ,λ ∈
P into ‘true’ exponentials,
eλ → eλ (µ) := e
−2πi
k+n ⟨λ ,µ +ρ ⟩, µ ∈P. (6.1)
This ‘quantises’ the ‘classical’g characters into ‘periodic’ characters,χ(h)
λ (µ) = χ(h)
λ +h Q(µ),
h =k +n, i.e., (skew-)invariant under the full aﬃne Weyl group at lev el k,
det(w) χ(h)
w·(λ +kΛ 0 )
(µ) = χ(h)
λ (µ) = χ(h)
λ (w · (µ +kΛ 0)), w ∈W , (6.2)
so that we can restrict the ‘dual’ set (the set of µ’s) to the integrable alcove P k
+ itself. 4
The ‘q’-characters are given explicitly by a ratio χ(h)
λ (µ) = S(h)
λ µ /S(h)
0 µ of matrix elements
of the integrable modular matrix S(h)
λ µ , a unitary, symmetric matrix. It is recovered up
to an overall constant by the second equality in (3.2), with κ = −1 and exponentials
transformed as in (6.1), i.e., (3.2) turns into the Kac–Pete rson formula [11]. Thus the
complex numbers {χ(h)
λ (µ), µ ∈ P h−n
+ } can be interpreted as eigenvalues of the matrix
Nλ of fusion rule coeﬃcients ( Nλ )β
α = N β
λ α of the integrable WZW conformal models.
This relates the Verlinde formula for N β
λ α to the classical Weyl-Steinberg formula [11],
4 Alternatively the ‘ q’-characters are obtained restricting the standard group characters to
the discrete subset of elements {diag(e
−2πi
h ⟨ei ,µ +ρ ⟩ , i = 1 , 2, . . . , n ) , µ ∈ P h−n
+ } in the Cartan
subgroup of SU (n). Here
∑ n
i=1 ei = 0 , e i = ¯Λ i − ¯Λ i−1 , ¯Λ 0 = 0 = ¯Λ n .
25
[16], [8]. In what follows we shall also need χ(h)
λ (µ) for µ belonging to some of the shifted
hyperplanes H (lh)
α := {µ ∈ ¯h∗| ⟨µ +ρ,α ⟩ =lh }, α ∈ ∆ + , l ∈ Z. While the Kac-Peterson
formula has no sense on these hyperplanes, since both the num erator and the denominator
vanish, the characters χ(h)
λ (µ) are well deﬁned through the analog of the last equality in
(3.2), or any of the standard determinant formulæ for the cla ssical sl(3) characters.
Following the analogy with the integrable case the idea is to replace the aﬃne Weyl
group with the aﬃne KW group at level κ − 3 = 3 /p − 3, i.e., to extend the invariance
(3.17) of the ‘classical’ characters with respect to the rig ht action of the horizontal Weyl
group W to invariance with respect to the right action of the aﬃne gro upW [p]. This will
lead to (1.2) with the structure constants given by the conje ctured in [9] formula (1.3),
which now derives from the ‘classical’ formula (4.9). Final ly inverting (1.2) we will recover
in section 7 the Pasquier–Verlinde type formula (1.1).
Apparently there are two problems to be solved. We have to ﬁnd an analog of the
discrete set {µ ∈P k
+} and furthermore the elements of the group algebra of ˜W have to be
converted into some C-valued functions on this set.
Denote by Ep the ‘double alcove’ region
Ep = {µ ∈P+ |0 ≤ ⟨µ,α i⟩ ≤p − 1, i= 1, 2}
=P p−3
+ ∪
(
wθ (P p−3
+ ) + (p − 2)θ
)
∪α ∈∆ +
(
H (p)
α ∩P 2p−2
+
)
⊂P 3p−3
+ .
(6.3)
This set, which can be also looked as P p−1
+ ∪ {wθ (P p+1
++ ) + pθ }, contains p2 weights,
|Ep| ≡ |P +,p |, and we shall argue below that it is the analog for k = 3/p − 3 of the
integrable ‘dual’ set{µ ∈P h−3
+ }, see ﬁgs. 9a, 9b, where Ep is depicted for p = 5 and p = 4
(the dotted lines indicate the hyperplanes H (lp)
α ). For p = 2 Ep consists of the alcove
P 1
+ and the weight ( p − 1,p − 1) = (1, 1) and thus represents the Z3 factorisation of the
integrable alcove at level 3 p − 3, P 3p−3
+ , obtained after identifying the points σl
[3p−3](λ)
along an orbit of the σ automorphism of P 3p−3
+ , including the σ stable point (p − 1,p − 1).
Forp >2 this factorisation leads to a subset of the alcove P 3p−3
+ which is of cardinality
|Ep| + |P p−3
+ |> |Ep|.
We look for a solution of the invariance condition
χy w(·) = det(w)χy(·), w ∈W [p], (6.4)
together with
χy a(·) = χy(·), a ∈A[p], y ∈ ˜W (+)
p . (6.5)
26
Accounting for the invariance of the characters with respec t to the horizontal Weyl group
W (3.17) the requirement (6.4) reduces to the periodicity con dition
χy tp ν (·) = χy(·), ν ∈Q. (6.6)
The formula (3.25) for the characters χy(·) involves the three basic ingredients – the
elements of the group A, the sl(3) characters χλ , and the combination F in (3.24), so
we have to give meaning to some C - valued counterparts γ(·), χλ (·), F (·). The natural
realisation for the generator of the group A – isomorphic to the cyclic group Z3, reads
γ →γ(µ) := e
2π i m
3 τ (µ ), m = 1, 2, mod 3 . (6.7)
The periodicity requirement (6.6) suggests to look for a rea lisation of the sl(3) characters
in (3.25) in terms of the integrable characters χ(p)
λ (µ) at (shifted) level p, determined for
µ ∈P p−3
+ ,
χλ →χλ (µ) := ελ ,µ χ(p)
λ (µ), ε 3
λ ,µ = 1. (6.8)
In (6.8) we have allowed for an arbitrary overall phase const antελ ,µ , invariant with respect
to both indices under the shifted action of the aﬃne Weyl grou p. We can choose
ελ ,µ =e
−2π i l
3 τ (µ ) τ (λ ), l = 1, 2, mod 3 , (6.9)
which eﬀectively leads to the realisation of the formal expo nentials as
e−κλ → e−κλ (µ) := e
−2π i l
3 τ (µ ) τ (λ )e
−2π i
p ⟨λ,µ +ρ ⟩. (6.10)
The need for this phase is dictated by the requirement (6.5), which combined with (3.19),
(5.5) reads for each of the parts χ(±)
y in χy = χ(+)
y +F χ(−)
y (treating for the time being
F (µ) as a formal variable)
γ(µ)χ(±)
y (µ) = χ(±)
t−σ [p−1](λ ) (µ)
(
=χ(±)
t−σ [p−3] (λ −2 ¯Λ 2 )
(µ)
)
for y =t−λ ,
γ(µ)χ(±)
y (µ) = χ(±)
w0t−σ 2
[p−2] (λ )
(µ)
(
=χ(±)
w0t−σ 2
[p−3](λ − ¯Λ 1 )
(µ)
)
for y =w0t−λ .
(6.11)
The above conditions and the corresponding standard proper ty of the integrable ‘ q’-
characters
χ(p)
σ [p−3](λ )(µ) = e
2π i
3 τ (µ )χ(p)
λ (µ), (6.12)
27
ﬁx the integer l to l = p mod 3 (using that p2 − 1 = 0 mod 3), and keeps arbitrary the
powerm in the phase in (6.7). Without lack of generality we can choos e m =l =p since
otherwise the remaining phases can be absorbed using the ana logous to (6.12) symmetry
with respect to the index µ,
χ(p)
λ (σ[p−3](µ)) = e
2π i
3 τ (λ )χ(p)
λ (µ), (6.13)
thus changing the value of µ toµ′ =σm−p
[p−3](µ) ∈P p−3
+ ; we can do this since the three terms
in each of χ(±)
y are described by sl(3) characters of weights of diﬀerent triality τ = 0, 1, 2.
Now we turn to the operator F =w0 +w1 +w2. We recall that it commutes with the
elements of A as well as with the sl(3) characters. Preserving the relation (4.2) – which
is the basic relation used to derive the character ring struc ture constants, we see that the
square of F (·) can be determined by the (fundamental) integrable charact ers, i.e.,
F 2 →F 2(µ) := 3 + χ(p)
¯Λ 1
(µ) +χ(p)
¯Λ 2
(µ) (6 .14)
for any µ ∈ P . This determines F (µ) up to a sign, F (µ) = ε(µ)
√
F 2(µ), ε (µ) = ±1.
The r.h.s of (6.14) is equivalently reproduced by
F 2(µ) = |R(µ)|2,
R(µ) =
∑
¯a∈ ¯A
e− 2π i
3p ⟨¯a(θ),µ +ρ ⟩ =e− 2π i
3p ⟨θ,µ +ρ ⟩ +e
2π i
3p ⟨α 1,µ +ρ ⟩ +e
2π i
3p ⟨α 2,µ +ρ⟩. (6.15)
One has the relations
i 3p
√
