---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-013-36-q-characters
section_title: "q-characters"
section_number: 3.6
pages: 12-13
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
renormalized q-characters of the Iwahori-Hecke algebras. The theory of ch aracter of Iwahori-Hecke algebra
is a little more involved than the one of symmetric groups. In deed, given two permutations σ and τ in the
same conjugacy class of Sn, the T -basis elements Tσ and Tτ can have diﬀerent traces in a Hn,q-module:
for instance, (1, 2) and (1, 3) are conjugate in S3, but χ(T(1,2)) = q and χ(T(1,3)) = q3 if we consider
the one-dimensional index representation. However, if σ and τ are of minimal Coxeter length in their
conjugacy classes, then one has χ(Tσ) = χ(Tτ ) for any character χ. Moreover, the values of a character
χ on these particular elements determine χ, see [
Ram91, Propositions 5.1 and 5.2] or [ GP00, §8.2] for the
general case of an Iwahori-Hecke algebra of a Coxeter group. Consequently, if
σρ = (1, 2, . . . , ρ1) (ρ1 + 1, ρ1 + 2, . . . , ρ1 + ρ2) · · · (ρ1 + · · · + ρr−1 + 1, . . . , ρ1 + · · · + ρr),
then ς λ(q) is entirely determined by the values ς λ(ρ, q) = ς λ(Tσρ , q), where ρ runs over Yn. As in the
case q = 1, we denote by χλ(ρ, q) the rescaled character value (divided by the dimension of th e module).
In [Ram91], A. Ram uses the Schur-Weyl decomposition of (/BV
m)⊗n into irreducible (Uq(sl(m, /BV )), Hn,q)-
bimodules to compute explicitly the characters of the Iwaho ri-Hecke algebra Hn,q — the reader can also
consult [ RR W96] and [ RR97]. These computations lead to a generalization of the usual F robenius-Schur
formula.
To state it, we need to introduce a few notations about symmet ric functions (we try to be consistent
with the one in [ Mac95]): the notations hλ, mλ, sλ and pλ stand respectively for the complete, monomial,
Schur and power-sum basis of the symmetric function ring. We will also use the Hall scalar product, for
which complete function basis is dual to the monomial one, wh ile Schur functions are orthonormal and
power sums orthogonal.
Furthermore, let us deﬁne a q-analog of the power sum pk(X). Let ~qk(X, q) be the symmetric function
deﬁned by the formulas
~qk(X, q) = qk
q − 1 hk(X(1 − q−1)) ( λ-ring notations, X is an alphabet and q−1 is a variable ),
= qk
q − 1
∑
µ∈Yk
(1 − q−1)ℓ(µ) mµ(X) = 1
q − 1
∑
µ∈Yk
(qµ − 1)(zµ)−1 pµ(X),
where qµ − 1 means ∏ r
i=1 (qµi − 1), and where zµ equals ∏
i≥1 imi mi! if µ writes multiplicatively as
1m12m2 . . . sms. This is a slightly modiﬁed version of the Hall-Littlewood p olynomial Pk(X, q−1) described
in [
Mac95, Chapter 3]. Let us ﬁrst recall Frobenius formula for usual c haracter values of symmetric group:
∀ρ ∈ Yn, p ρ(X) =
∑
λ∈Yn
ς λ(ρ) sλ(X).
Here is the statement of Ram’s generalization of Frobenius- Schur formula:
Proposition 9 (q-Frobenius-Schur formula). If ~qρ = ~qρ1 · · · ~qρr , then the following generalized Frobenius-
Schur formula holds:
∀ρ ∈ Yn, ~qρ(X, q) =
∑
λ∈Yn
ς λ(ρ, q) sλ(X).
ASYMPTOTICS OF q-PLANCHEREL MEASURES 13
Many combinatoric rules follow from Proposition 9, e.g., a quantization of the classical Murnaghan-
Nakayama rule, see [ RR97, §2]. For the asymptotic analysis of the q-Plancherel measures, we shall use a
triangular relation between q-characters and standard characters:
ς λ(ρ, q) = ⟨~qρ(X, q) | sλ(X)⟩ = qn
(q − 1)ℓ(ρ)
⟨
hρ(X − q−1X)
⏐
⏐ sλ(X)
⟩
= qn
(q − 1)ℓ(ρ)
∑
ν∈Yn
⟨
hρ(X − q−1X)
⏐
⏐ pν(X − q−1X)
⟩ ⟨
pν(X − q−1X)
⏐
⏐ sλ(X)
⟩
⟨pν | pν⟩
= 1
(q − 1)ℓ(ρ)
∑
ν∈Yn
(qν − 1) ⟨hρ | pν⟩
zν
⟨pν | sλ⟩ = 1
(q − 1)ℓ(ρ)
∑
ν∈Yn
qν − 1
zν
⟨hρ | pν⟩ ς λ(ν)
As for q = 1, we deﬁne the following function on the set Y of all Young diagrams:
Σρ,q(λ) =
{
|λ|↓|ρ| χλ(ρ 1|λ|−|ρ|, q) if |ρ| ≤ | λ|;
0 else.
If |ρ| = |λ| = n, the previous formula can be rewritten:
(5) (q − 1)ℓ(ρ) Σρ,q(λ) =
∑
ν∈Yn
qν − 1
zν
⟨pν | hρ⟩ Σν(λ)
This is of course also true for |ρ| > |λ|. We will show that it still holds for k = |ρ| < |λ| = n. In this case,
the scalar product ⟨hρ 1n−k |pν⟩ in the sum above is given by:
⟨hρ 1n−k |pν⟩ =
⟨
hρ(p1)n−k ⏐
⏐ pν
⟩
=
∑
π1∈Yρ1 ,...,πm∈Yρm
(zπ1 · · · zπm)−1 ⟨
pπ(p1)n−k ⏐
⏐ pν
⟩
=
∑
π1,...,πm
zπ1n−k (zπ1 · · · zπm)−1
/BD
(ν=π1n−k) = (zν
/BD
(ν=νk1n−k))
∑
π1,...,πm
(zπ1 · · · zπm)−1
/BD
(νk=π)
= (zν /zνk) /BD
(ν=νk1n−k)
∑
π1,...,πm
(zπ1 · · · zπm)−1 ⟨pπ | pνk ⟩ = (zν/zνk ) /BD
(ν=νk1n−k) ⟨hρ | pνk ⟩
As a consequence, formula ( 5) can be seen as an equality of functions on Y . Note that this relation
between the symbols Σρ,q and Σν is triangular, because ⟨pν | hρ⟩ = 0 unless ν is ﬁner than ρ. Moreover,
as (mρ)ρ∈Y is the dual basis of (hρ)ρ∈Y , the inverse relation is easily obtained. We conclude that:
Proposition 10 (Quantization of the algebra of observables) . The symbols (Σρ,q)ρ∈Y form a /BV (q)-basis
of O(q) = O ⊗
/BV
/BV (q) and yield a quantization of the basis (Σρ)ρ∈Y of O. Moreover, the transition
matrices between the Σρ,q and the Σρ are triangular, given by:
(q − 1)ℓ(ρ) Σρ,q(λ) =
∑
ν∈Yk
qν − 1
zν
⟨pν | hρ⟩ Σν(λ);(6)
(qρ − 1) Σρ(λ) =
∑
ν∈Yk
(q − 1)ℓ(ν) ⟨mν | pρ⟩ Σν,q(λ).(7)
