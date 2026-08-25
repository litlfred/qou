---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-029-51-doubled-a1-example
section_title: "Doubled A1 example"
section_number: 5.1
pages: 23-27
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
of a single vertex and no arrows. It depends on a parameter z∈ C∗.
(i) The lattice Γ = Z· γ has rank one, and thus ⟨−,−⟩ = 0;
(ii) The central charge Z : Γ → C is determined by Z(γ) = z∈ C∗;
(iii) The only non-vanishing BPS invariants are Ω( ±γ) = 1.
The Riemann-Hilbert problem associated to this BPS structure is triv ial since all elements of Γ
are null. Let us instead consider the double of this BPS structure
(Γ D, Z, Ω) , Γ D = Γ⊕ Γ ∨.
Let γ∨∈ Γ ∨ be the unique generator satisfying γ∨(γ) = 1. Note that the deﬁnition ( 11) shows
that the skew-symmetric form ⟨−,−⟩ on Γ D satisﬁes⟨γ∨, γ⟩ = 1.
To deﬁne the Riemann-Hilbert problem for the doubled BPS structur e we must ﬁrst choose
a constant term ξD∈ TD, where TD is the twisted torus corresponding to the lattice Γ D. For
simplicity we take ξD(γ∨) = 1, and write ξ = ξD(γ)∈ C∗.
24 TOM BRIDGELAND
The only active rays are ℓ± =±R>0· z, and Lemma 4.8 shows that
Xr,γ(t) = exp(−z/t)· ξ
for any non-active ray r ⊂ C∗. The non-trivial part of the Riemann-Hilbert problem for the
doubled BPS structure consists of the functions
Yr(t) = Yr,γ∨(t) : Hr→ C∗.
It follows from Remark 4.5 that the functions Yr(t) for non-active rays r⊂ C∗ lying in the
same component of C\ R· z are analytic continuations of each other. Thus we obtain just two
holomorphic functions
Y±(t) : C∗\ iℓ±→ C∗,
corresponding to non-active rays lying in the half-planes ± Im(z/t) > 0. Using Remark 4.4, the
Riemann-Hilbert problem for the doubled BPS structure can theref ore be restated as follows.
Problem 5.1. Find holomorphic functions Y± : C∗\ iℓ±→ C∗ such that:
(i) There are relations
Y+(t) =
{
Y−(t)· (1− ξ+1· e−z/t)−1 if t∈ Hℓ+,
Y−(t)· (1− ξ−1· e+z/t)−1 if t∈ Hℓ−. (25)
(ii) As t→ 0 in C∗\ iℓ± we have Y±(t)→ 1.
(iii) There exists k > 0 such that
|t|−k <|Y±(t)| <|t|k
as t→∞ in C∗\ iℓ±.
To understand condition (i) note that if t∈ Hℓ+ then t lies in the domains of deﬁnition Hr of
the functions Yr corresponding to suﬃciently small deformations of the ray ℓ+. Thus ( 21) applies
to the ray ℓ+ and we obtain the ﬁrst of the relations ( 25). The second follows similarly from ( 21)
applied to the opposite ray ℓ−.
5.2. Solution in the doubled A 1 case. The formula
Λ( w) = ew· Γ( w)√
2π· ww− 1
2
(26)
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 25
deﬁnes a meromorphic function of w∈ C∗, which is multi-valued due to the factor
ww− 1
2 = exp
(
(w− 1
2 ) log w
)
.
Since Γ( w) is meromorphic on C with poles only at the non-positive integers, it follows that Λ( w)
is holomorphic on C∗\ R<0. We specify it uniquely by taking the principal branch of log.
The Stirling expansion [ 31, Section 12.33] gives an asymptotic expansion
log Λ( w)∼
∞∑
g=1
B2g
2g(2g− 1) w1−2g, (27)
where B2g denotes the (2 g)th Bernoulli number. This expansion is valid as w→∞ in the comple-
ment of a closed sector containing the ray R<0. It implies in particular that Λ( w)→ 1.
Proposition 5.2. When ξ = 1, Problem 5.1 has a unique solution, namely
Y+(t) = Λ
( z
2πit
)
, Y −(t) = Λ
(−z
2πit
) −1
.
Proof. Note that the function Y+(t) is indeed holomorphic on the domain C∗\ iℓ+ as required,
because if we set w = z/2πit then
t∈ iℓ+ ⇐⇒ w∈ R<0.
Similarly Y−(t) is holomorphic on C∗\ iℓ−. The Euler reﬂection formula gives
Γ( w)· Γ(1− w) = π
sin(πw), w ∈ C\ Z.
Since Γ( n) = ( n− 1)! for n∈ Z>0, it follows that Γ( w) is nowhere vanishing. The same is therefore
true of Λ( w). The reﬂection formula also implies that for w∈ C\ Z
Λ( w)· Λ(−w) = 1
2π· π
sin(πw)· e−((w− 1
2 ) log(w)+(−w+ 1
2 ) log(−w)),
where we used Γ(1 − w) = (−w)· Γ(−w). For the principal branch of log we have
log(w) = log(−w)± πi when ± Im(w) > 0.
Thus we conclude that
Λ( w)· Λ(−w) = i· e−πi(w− 1
2 )
eπiw− e−πiw = (1− e2πiw)−1 (28)
26 TOM BRIDGELAND
when Im( w) > 0. Note that if w = z/2πit then
t∈ Hℓ− ⇐⇒ Im(w) > 0,
so we get the second of the relations ( 25). The other follows in the same way. Property (ii) is
immediate from the Stirling expansion ( 27). Property (iii) is a simple consequence of the fact that
Γ( w) has a simple pole at w = 0. Finally, the uniqueness statement follows from Lemma 4.9. □
5.3. The ﬁnite uncoupled case. In the case of a ﬁnite, uncoupled, integral BPS structure we
can construct a unique solution to the Riemann-Hilbert problem by su perposing the solutions from
the previous section.
Theorem 5.3. Let (Z, Γ , Ω) be a ﬁnite, uncoupled, integral BPS structure. Suppose that ξ∈ T
satisﬁes ξ(γ) = 1 for all active classes γ∈ Γ . Then the corresponding Riemann-Hilbert problem
has a unique solution, which associates to a non-active ray r the function
Yr,β(t) =
∏
Z(γ)∈iHr
Λ
(Z(γ)
2πit
) Ω( γ)⟨β,γ ⟩
(29)
where the product is taken over the ﬁnitely many active class es γ∈ Γ for which Z(γ)∈ iHr.
Proof. Note ﬁrst that the expression ( 29) is holomorphic and non-zero on Hr because in each factor
both Z(γ)/i and t lie in Hr, so the argument of Λ does not lie in R<0. The properties (RH2) and
(RH3) then follow immediately as in the proof of Proposition 5.2. Consider two non-active rays
r− and r+ obtained by small perturbations, anti-clockwise and clockwise resp ectively, of an active
ray ℓ. Then ℓ⊂ iHr+ whereas−ℓ⊂ iHr−. Assume that t∈ Hr−∩ Hr+. Then t∈ Hℓ and hence
−Z(γ)/2πit lies in the upper half-plane whenever Z(γ)∈ ℓ. Using ( 28) we therefore obtain
Xr+,β(t)
Xr−,β(t) =
∏
Z(γ)∈ℓ
(
Λ
(Z(γ)
2πit
)
· Λ
(−Z(γ)
2πit
) ) Ω( γ)⟨β,γ ⟩
=
∏
Z(γ)∈ℓ
(1− e−Z(γ)/t)Ω( γ)⟨γ,β ⟩
This is precisely the condition ( 21) since Lemma 4.8 and the assumption on ξ implies that Xγ(t) =
exp(−Z(γ)/t) whenever Ω( γ)⁄= 0. □
Using the Stirling expansion we obtain an asymptotic expansion
log Xr,β(t)∼ Z(β)
t − 2πiθ(β) +
∑
g≥1
∑
γ∈Γ
Ω( γ)⟨β, γ⟩B2g
4g (2g− 1)
( 2πit
Z(γ)
) 2g−1
, (30)
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 27
valid as t→ 0 in the half-plane Hr. We have set ξ(β) = exp(2 πiθ(β)). The extra factor of 2 in
the denominator arises because in ( 29) we take a product over half the classes in Γ. Note that this
expansion is independent of the choice of ray r⊂ C∗.
