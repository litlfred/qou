---
doc_id: arxiv-1203.4538v1
doc_title: "The exponential-logarithmic equivalence classes of surreal numbers"
section_id: sec-005-4-sign-sequences-formulae-for-the-kappa-map
section_title: "Sign sequences formulae for the kappa map."
section_number: 4
pages: 9-13
source_pdf: 1203.4538v1.pdf
source_sha256: 5e44909e355c78d6
doc_brief: "The exponential-logarithmic equivalence classes of surreal numbers — 7 sections: Introduction.; Preliminaries on surreal numbers.; Sign sequences."
---
For any a ∈ No and n ∈ N, we denote by κa,n := logn(κa) and κa,−n = expn(κa), where
log0 and exp0 are equal to the identity map on No. The aim of this section is to show
that κa,n and κa,−n for any n are elements of ωωNo
, and to give their sign sequence. In
order to do so, we introduce the following auxiliary map ι and give its sign sequence.
Notation 4.1 •Consider a surreal number a = α0 ⊕ /binampersandβ0 ⊖ /binampersandα1 ⊕ /binampersandβ1 ⊖ /binampersand· · ·.
For any ordinal µ ∈ On intervening in the writing of a, we set:
γµ :=
∑
λ≤µ
αλ (ordinal sum).
•We set Ω0 to be the constant map equal to 1 in No and ǫ♭0 := 0.
9
Lemme 4.2 The recursive formula:
∀a ∈ No, ι (a) = ιa := ⟨ιaL /binampersandΩn(ǫ♭(aL)+ + 1) ⊕ | ιaR/binampersandn⊖⟩.
(where it is understood that n ∈ N) deﬁnes a map
ι : No → No
a ↦→ ι(a) := ιa
such that for any a = α0 ⊕ /binampersandβ0 ⊖ /binampersandα1 ⊕ /binampersandβ1 ⊖ /binampersand· · ·, the sign sequence of ιa is given
by:
ιa = ǫ♭γ0 ⊕ /binampersandωβ0 ⊖ /binampersandǫ♭γ1 ⊕ /binampersandωβ1 ⊖ /binampersand· · ·.
A uniformity property holds for this map.
Proof. We proceed by transﬁnite induction on l(a) ∈ On. We have ι0 = ⟨∅ | ∅⟩= 0.
Given a surreal number a ∈ No with l(a) > 0, we suppose that for any b with l(b) <
l(a), ιb is well deﬁned, with the corresponding sign sequence. Consi der a canonical
representation a = ⟨aL | aR⟩of a. For instance, in the case where l(a) is a successor
ordinal and a = aL/binampersand⊕. So aR <s aL et aR > aL. More precisely, either aL is only made
of ⊕’s in which caseaR = ∅ (case (i)), or aR is a truncation of aL, ending with a group
of ⊖’s ofaL of smaller number than the corresponding one in aL (case (ii)). In the case
(i), the sign sequence formula of ιa is:
ιa = ⟨ιaL /binampersandΩn(ǫ♭(aL)+ + 1) | ∅⟩
= ⟨ǫ♭(aL)+ /binampersandΩn(ǫ♭(aL)+ + 1) | ∅⟩
= ǫ♭(aL)++1
= ǫ♭a+
In the case (ii), denote byaL = α0 ⊕ /binampersandβ0 ⊖ /binampersand· · ·/binampersandαµ ⊕ /binampersandβµ ⊖ /binampersand· · ·. So aR = α0 ⊕ /binampersandβ0 ⊖
/binampersand· · ·/binampersandαµ ⊕ /binampersand˜βµ⊖ with ˜βµ < β µ (in On) for some µ ∈ On. By the induction hypothesis,
ιaL = ǫ♭γ0 ⊕/binampersandωβ0 ⊖/binampersand· · · /binampersandǫ♭γµ ⊕/binampersandωβµ ⊖/binampersand· · · < ǫ ♭γ0 ⊕/binampersandωβ0 ⊖/binampersand· · · /binampersandǫ♭γµ ⊕/binampersandω˜βµ⊖ = ιaR.
So we obtain as desired ιaL /binampersandΩn(ǫ♭(aL)+ + 1) < ιaR/binampersandn⊖ for any n ∈ N. Moreover,
ιa = ⟨ιaL /binampersandΩn(ǫ♭(aL)+ + 1) | ιaR /binampersandn⊖⟩
= ⟨(ǫ♭γ0 ⊕ /binampersandωβ0 ⊖ /binampersand· · ·/binampersandǫ♭γµ ⊕ /binampersandωβµ ⊖ /binampersand· · ·)/binampersandΩn(ǫ♭(aL)+ + 1) |
(ǫ♭γ0 ⊕ /binampersandωβ0 ⊖ /binampersand· · · /binampersandǫ♭γµ ⊕ /binampersandω˜βµ⊖)/binampersandn⊖⟩
= ǫ♭γ0 ⊕ /binampersandωβ0 ⊖ /binampersand· · ·/binampersandǫ♭γµ ⊕ /binampersandωβµ ⊖ /binampersand· · ·)/binampersandǫ♭(aL)++1
= ǫ♭γ0 ⊕ /binampersandωβ0 ⊖ /binampersand· · ·/binampersandǫ♭γµ ⊕ /binampersandωβµ ⊖ /binampersand· · ·)/binampersandǫ♭(a)+ .
The other cases for l(a) and a are analogous. They are left to the reader as an exercise.
Concerning the uniformity property, by the sign sequence fo rmula for ι, we note that
for any surreal numbers a, b ∈ No, a < b ⇒ ιa < ι b. So the uniformity property
follows from Theorem
2.1 in the same way as in [Gon86, Theorem 3.2, 3.5, Corollary
au Theorem 5.2] and in Theorem 3.2. □
The main result of this section is:
Theorem 4.3 1. For any a ∈ No, n ∈ N, we have κa,n, κ a,−n ∈ ωωNo
. More pre-
cisely:
10
κa,n = ωωb
with b = ιa/binampersandn⊖;
κa,−n−1 = ωωb
with b = ιa/binampersandΩn(ǫ♭a+ + 1) ⊕ .
In particular, κa = ωωιa
.
2. With the Notation 4.1, for any a ∈ No, n ∈ N, we have:
κa = ωω
ǫ♭γ0
⊕ /binampersand[(ωω
ǫ♭γ0
ω)2β0] ⊖ /binampersandǫ♭γ1 ⊕ /binampersand[(ǫ♭γ1ω)2β1] ⊖ /binampersand· · · ;
κa,n = κa/binampersand(ǫ♭a+ωn)⊖ ;
κa,−n−1 = κa/binampersand(Ωn+2(ǫ♭a+ + 1) ⊕ .
The second point of the theorem follows directly from the ﬁrs t one and the sign
sequences for the maps Ω(Theorem 2.9) and ι (Lemma 4.2). The ﬁrst point will be
deduced from the following lemma.
Lemme 4.4 For any a ∈ No and any λ ∈ On, if we set λ = ǫν + µ where ǫν is the unique
epsilon number (possibly 0) such that ǫν < λ ≤ ǫν+1, we have:
h(ιa/binampersandλ⊖) = ωιa/binampersand(λ+1)⊖;
h(ιa/binampersandλ⊕) = ωιa/binampersandǫ ⊕ /binampersand♭µ ⊕ avec λ > 0.
Proof. We proceed by transﬁnite induction on (l(a), λ) ∈ − − − − − − − − →
On × On (the lexicographi-
cal product of On with itself).
Suppose that l(a) = 0 i.e. a = 0. By the deﬁnition of the map h (see Theorem
2.7 (2.)),
we have h(0) = ⟨0 | 1/2n⟩= ω−1.
Moreover, 1 = ⊕ = ⟨0 | ∅⟩. So:
h(⊕) = ⟨0, h(0) | ω/2n⟩
= ⟨ω−1 | ω/2n⟩
= ⟨⊕/binampersandω ⊖ | ω ⊕ /binampersand⊖⟩by the Theorem 2.9
= ⊕ = ω0.
Consider now ( a, λ) ∈ No × On with λ > 0 in On. Suppose that the lemma
holds for any ( b, µ) ∈ No × On with ( l(b), µ) <lex (l(a), λ) in − − − − − − − − →
On × On. We have
ιa/binampersandλ⊖ = ⟨(ιa)L | ιa/binampersandµ⊖⟩with µ < λ in On. So, by the deﬁnition of h and by the
induction hypothesis:
h(ιa/binampersandλ⊖) = ⟨0, h((ιa)L) | h(ιa/binampersandµ⊖), ω ιa/binampersandλ⊖/2n⟩
= ⟨0, h(ιaL/binampersandΩn(ǫ♭(aL)+ + 1)⊕) | ωιa/binampersand(µ+1)⊖, ω ιa/binampersandλ⊖/2n⟩(Lemma
4.2)
= ⟨0, ω ιaL /binampersandΩn(ǫ♭(aL)+ + 1) ⊕ | ωιa/binampersandλ⊖/binampersand(ǫ♭a+n)⊖⟩by coﬁnality
= ωιa/binampersandλ⊖/binampersand(ǫ♭a+ω)⊖
= ωιa/binampersand(λ+1)⊖ by Theorem 2.9.
We set λ = ǫν + µ where ǫν < λ ≤ ǫν+1. We have ιa/binampersandλ⊕ = ιa/binampersandǫν ⊕ /binampersandµ⊕ =
⟨ιa/binampersandǫν ⊕ /binampersandρ ⊕ | (ιa)R⟩with ρ < µ in On. So, by the deﬁnition of h and by the induction
hypothesis:
11
h(ιa/binampersandλ⊕) = ⟨0, h(ιa/binampersandǫν ⊕ /binampersandρ⊕) | h((ιa)R), ω ιa/binampersandλ⊕/2n⟩
= ⟨0, ω ιa/binampersandǫν ⊕ /binampersand♭ρ ⊕ | h(ιaR/binampersandn⊖), ω ιa/binampersandλ⊕/2n⟩
= ⟨0, ω ιa/binampersandǫν ⊕ /binampersand♭ρ ⊕ | ωιaR /binampersand(n+1)⊖, ω ιa/binampersandλ⊕/2n⟩
(note that ιaR /binampersand(n + 1)⊖ > ιa/binampersandλ⊕)
= ⟨0, ω ιa/binampersandǫν ⊕ /binampersand♭ρ ⊕ | ωιaR /binampersand(n+1)⊖, ω ιa/binampersand(ǫ♭a+ ωλ) ⊕ /binampersand(ǫ♭a+ ωλn)⊖⟩
(Theorem 2.9 and coﬁnality)
= ωιa/binampersandǫ ⊕ /binampersand♭µ ⊕ .
Consider now a ∈ No with l(a) > 0, and suppose that the lemma holds for any
(b, µ) ∈ No × On with l(b) < l(a) in On. We have ιa = ⟨ιaL/binampersandΩn(ǫ♭(aL)+ + 1) ⊕ | ιaR/binampersandn⊖⟩
by Lemma 4.2. So, by the deﬁnition of h and the induction hypothesis, we have:
h(ιa) = ⟨0, h((ιa)L) | h((ιa)R), ω ιa/2n⟩
= ⟨0, h(ιaL/binampersandΩn(ǫ♭(aL)+ + 1)⊕) | h(ιaR/binampersandn⊖), ω ιa/2n⟩(Lemma 4.2)
= ⟨0, ω ιaL /binampersandΩn(ǫ♭(aL)+ + 1) ⊕ | ωιaR /binampersand(n+1)⊖, ω ιa/binampersand(ǫ♭a+n)⊖⟩(Theorem 2.9)
= ⟨0, ω ιaL /binampersandΩn(ǫ♭(aL)+ + 1) ⊕ | ωιa/binampersand(ǫ♭a+n)⊖⟩by coﬁnality
= ωιa/binampersand(ǫ♭a+ω)⊖
= ωιa/binampersand⊖ (Theorem 2.9).
□
Proof of Theorem 4.3 (1.). We proceed by tranﬁnite induction on (l(a), n) ∈ − − − − − − →
On × N.
Suppose that l(a) = 0, i.e. a = 0. In the proof of the Theorem
3.2, we proved that
κ0 = ω. So κ0 = ωω0
as desired.
Let n ∈ N∗. We suppose that the property holds for any ( b, m) ∈ No × N with
(l(b), m) < (l(a), n). We have:
κa,n = logn(κa)
= log(κa,n−1)
= log(ωωb
) with b = ιa/binampersand(n − 1)⊖
= ωh(ιa/binampersand(n−1)⊖) (Theorem 2.7)
= ωωb
with b = ιa/binampersandn ⊖ (Lemma 4.4)
We also have:
κa,−1 = exp(κa)
= exp(ωωιa
)
= ωωb
with b = g(ωιa) (Theorem 2.7)
= ωωb
with b = ιa/binampersand⊕
(Lemma 4.4 : g(ωιa) = ιa/binampersand⊕ ⇔ ωιa = h(ιa)
and
κa,−n−1 = expn+1(κa)
= exp(κa,−n)
= exp(ωωb
) with b = ιa/binampersandΩn−1(ǫ♭a+ + 1)⊕
= ωωb
with b = g(ωιa/binampersandΩn−1(ǫ♭a+ +1)⊕) (Theorem 2.7)
= ωωb
with b = ιa/binampersandΩn(ǫ♭a+ + 1) ⊕ (Lemma 4.4)
12
Consider a ∈ No with l(a) > 0, and suppose that the property holds for any (b, m) ∈
No × N with l(b) < l(a) and any m ∈ N. By the deﬁnition of κ (Theorem 3.2) and by
the induction hypothesis, we have:
κa = ⟨expn(0), expn(κaL) | logn(κaR)⟩
= ⟨n, ω ωb
| ωωc
, ω ιa/2n⟩with b = ιaL/binampersandΩn(ǫ♭(aL)+ + 1)⊕) and c = ιaR/binampersandn⊖
= ωωιa
(by coﬁnality and deﬁnition of ι, Lemma 4.2)
This ﬁnishes the proof of Theorem 4.3. □
Remark 4.5 1. One can ﬁnd in [ Gon86] partial results about these sign sequences.
Indeed, for any n ∈ N, any ordinal λ ∈ On, any epsilon-number ǫµ with µ ∈ On,
we have:
logn(ωωλ⊖
) = ωω(λ+n)⊖
by [Gon86, Theorem 10.15]
expn(ω) = Ω n+1(1) by [Gon86, Theorem 10.14]
expn(ǫµ) = Ω n+1(ǫµ + 1) by [Gon86, Theorem 10.14]
.
2. By the Theorems 2.9, 2.10 and 4.3, we have:
ǫNo ⊊κNo ⊊ωωNo
⊊ωNo ⊊No.
