---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK"
section_id: sec-004-25-representations-of-j
section_title: "Representations of J"
section_number: 2.5
pages: 5-7
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl gr oup W , deﬁned over a ground ring in which “bad” primes for W are"
---
Upon substituting v ↦→1 ∈ Q, the algebra H specialises to Q[W ]. Hence, we obtain a
homomorphism of Q-algebras
φ 1 : Q[W ] → JQ, where JQ = Q ⊗Z J.
This is an isomorphism by the argument in [25, 20.1]. Since Q[W ] is split semisimple, we
can conclude that JQ also is split semisimple. Via the isomorphism φ 1 : Q[W ] → JQ, the set
Λ can be used to parametrize the irreducible representations of JQ (up to isomorphism). As
in [25, 20.2], we write
Irr(JQ) = {Eλ
♠ | λ ∈ Λ },
where Eλ
♠ coincides with Eλ as Q-vector space and the action of j ∈ JQ on Eλ
♠ is the same
as the action of φ −1
1 (j) on Eλ. Now, by [25, 20.1(b)], the algebra J is symmetric where
{tw | w ∈ W } and {tw−1 | w ∈ W } form a pair of dual bases. Thus, we have the following
orthogonality relations:
∑
w∈W
trace
(
tw, E λ
♠
)
trace
(
tw−1, E µ
♠
)
=
{ dλ fλ if λ = µ,
0 if λ ⁄= µ.
(The fact that fλ appears on the right hand side is shown in [25, 20.11].) Choosing a vecto r
space basis of Eλ, we obtain a matrix representation
ρλ : JQ → Mdλ (Q), t w ↦→
(
ρλ
st(tw)
)
s,t∈M (λ),
where M(λ) = {1, . . . , d λ}. Then the following Schur relations hold; see [14, §7.2]. For
λ, µ ∈ Λ, s, t ∈ M(λ) and u, v ∈ M(µ), we have:
∑
w∈W
ρλ
st(tw) ρµ
uv(tw−1) =
{ fλ if ( λ, s, t) = ( µ, v, u),
0 otherwise .
These equations can be inverted and this yields the “second” Schur relations:
∑
λ∈Λ
∑
s,t∈M (λ)
1
fλ
ρλ
st(tx) ρλ
ts(ty−1) =
{ 1 if x = y,
0 otherwise .
By a general argument, every irreducible representation of JQ leaves a positive-deﬁnite qua-
dratic form invariant. More precisely, we have the following result.
Proposition 2.6. Let λ ∈ Λ . Then a basis of Eλ can be chosen such that
6 MEINOLF GECK
(a) ρλ
st(tw) ∈ Z for all w ∈ W and s, t ∈ M(λ).
Furthermore, there exists a symmetric, positive-deﬁnite m atrix
Bλ = (β λ
st)s,t∈M (λ) where β λ
st ∈ Z for all s, t ∈ Mdλ ,
such that the following two conditions hold:
(b) Bλ · ρλ(tw−1) = ρλ(tw)tr · Bλ for all w ∈ W ;
(c) Any prime which divides det(Bλ) ⁄= 0 is L-bad for W .
(For any matrix M, we denote by M tr the transpose of M.)
Proof. To simplify the notation, write E = Eλ, d = dλ and ρ = ρλ so that we can omit
a subscript or superscript λ in the subsequent formulas. Since J is deﬁned over Z, the
statement in (a) follows by a general argument; see, for example, [14, 7.3.7]. Now let
B1 =
∑
y∈W
ρ(ty)tr · ρ(ty) ∈ Md(Z).
This matrix clearly is symmetric. Now let 0 ⁄= e = ( e1, . . . , e d) ∈ Zd. Since ρ is irreducible,
there exists some y ∈ W such that eρ(ty)tr ⁄= 0 and, hence, the standard scalar product of
this vector with itself will be strictly positive. Consequently, we have eB1etr > 0. Thus, B1
is positive-deﬁnite and, in particular, det( B1) ⁄= 0. For any x ∈ W , we have
B1 · ρ(tx−1) =
∑
y∈W
ρ(ty)tr · ρ(tytx−1) =
∑
y,z∈W
γy,x−1,z−1 ρ(ty)tr · ρ(tz).
Now γy,x−1,z−1 = γx−1,z−1,y by (P7) in [25, 14.2], and γx−1,z−1,y = γz,x,y −1 by [25, Prop. 13.9].
Hence, the right hand side of the above identity equals
∑
y,z∈W
γz,x,y −1ρ(ty)tr · ρ(tz) =
∑
z∈W
ρ(tztx)tr · ρ(tz) = ρ(tx)tr · B1.
Let 0 ⁄= n ∈ Z be the greatest common divisor of all non-zero coeﬃcients of B1 and B =
n−1B1 ∈ Md(Z). Then B is a symmetric, positive-deﬁnite matrix such that (b) holds. It
remains to prove (c). Let p be a prime number and denote by ¯B the matrix obtained by
reducing all coeﬃcents modulo p. By reduction modulo p, we also obtain an Fp-algebra
Jp = Fp ⊗Z J and a corresponding matrix representation ¯ ρ : Jp → Md(Fp). Hence we have
¯B ⁄= 0 and ¯B · ¯ρ(tw) = ¯ρ(tw−1)tr · ¯B for all w ∈ W .
By [25, 13.9], the map tw ↦→tw−1 deﬁnes an involutory anti-automorphism of J. Hence the
assignment tw ↦→¯ρ(tw−1)tr also deﬁnes a representation of Jp. The above identity now shows
that ¯B ⁄= 0 is an “intertwining operator”. Hence, if we knew that ¯ ρ was irreducible, then
Schur’s Lemma would imply that ¯B were invertible and so p could not divide det( B).
Thus, it remains to show that ¯ρ is an irreducible representation of Jp whenever p is L-good.
But this follows from a general argument about symmetric algebras . Indeed, as already noted
HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR 7
in §2.5, J is symmetric and we have the Schur relations for the matrix coeﬃcien ts of ρ = ρλ.
Reducing these relations modulo p, we obtain:
∑
w∈W
¯ρλ
st(tw) ¯ρλ
uv(tw−1) =
{ fλ mod p if s = v, u = t,
0 otherwise .
Since fλ ⁄≡0 mod p, one easily deduces from this that ¯ ρλ is (absolutely) irreducible; see [14,
Remark 7.2.3]. □
