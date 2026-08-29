---
doc_id: arxiv-2406.05311v1
doc_title: "A QUANTUM MURNAGHAN\u2013NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE"
section_id: sec-003-quantum-equals-classical
section_title: "Quantum equals classical"
section_number: 4
pages: 12-15
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
doc_brief: "A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE — 5 sections: Introduction; A Murnaghan–Nakayama rule for (cla; A Murnagha"
---
A recurring theme in quantum Schubert calculus is that oftentimes the numerical part
w,α := −α q α w
q Cu,v (∈ N) of a quantum Littlewood–Richardson number (a Gromov–Witten
Nu,v
′
invariant) is naturally identified with a related classical Littlewood–Richardson number cw
u′ ,v′ .
This is seen in the quantum Monk formula (3.1) in which these numerical parts are all 1
as in the classical Monk formula (2.4). Bertram’s quantum Giambelli formula [9] and the
results of Buch, Kresch, and Tamvakis [11] are other examples. Leung and Li [23] discuss this
thoroughly and then establish very general results, including some that naturally identify
different Gromov–Witten invariants on the same flag variety. Their result is type-free and
expressed in the language of algebraic groups, and they use it to deduce a weaker version
of the result we need, Lemma 4.4. We first state some results from [23] for the type A flag
variety using the notation from Section 3 and extract a useful statement from one of their
proofs, from which we deduce Lemma 4.4.
Fix i ∈ [n−1]. Let ei := (0, . . . , 0, 1, 0, . . . , 0) be the ith standard basis vector, so that
ei
q = qi . Write si := (i, i+1), the ith simple transposition. We will also need the linear map
̟i : Zn−1 → Z, defined by ̟i (α) := −αi−1 + 2αi − αi+1 , where α0 = αn = 0. Thus
q2,4 = q (01100) = q e2 +e3 ,

635214s2 = 653214 ,

̟2 (12232) = −1 + 4 − 2 = 1 ,

and

635214s3 = 632514 ,

̟4 (12232) = −2 + 6 − 2 = 2 .

For i ∈ [n−1], we also define a map sgi : Sn → {0, 1} which records whether or not u ⋖i usi ,

1
if usi ⋖i u equivalently, if u(i + 1) < u(i)
.
sgi (u) :=
0
if u ⋖i usi equivalently, if u(i) < u(i + 1)
That is, sgi (u) = 1 when u has a descent at i and it equals 0 when u has an ascent at i.
Proposition 4.1. [23, Theorem 1.1] Let x, y, z ∈ Sn and α ∈ Nn−1 .
z,α
(1) We have that Nx,y
= 0 unless sgi (z) + ̟i (α) ≤ sgi (x) + sgi (y) for all i ∈ [n−1].


QUANTUM MURNAGHAN–NAKAYAMA RULE

13

(2) Suppose that sgi (z) + ̟i (α) = sgi (x) + sgi (y) = 2 for some i ∈ [n−1], then
(
zsi ,α−ei
Nx,ys
if sgi (z) = 0
i
z,α
z,α−ei
.
Nx,y
= Nxs
=
i ,ysi
zsi ,α
Nx,ys
if
sg
(z)
=
1
i
i
w,α
Note that if Nu,v
6= 0, then by part (1), we have ̟i (α) ≤ 2 for each i ∈ [n−1]. This
w,α
also constrains u, v, w. For example, if Nu,v(λ,k)
6= 0 and i 6= k, then sgi (v(λ, k)) = 0 and
Proposition 4.1(1) becomes

sgi (w) + ̟i (α) ≤ sgi (u) ≤ 1 .

(4.1)

We first recall two lemmas from [23].
Proposition 4.2. Suppose that α ∈ Nn−1 is a nonnegative nonzero exponent vector.
(1) ([23, Lemma 2.8]) There is an i ∈ [n−1] with ̟i (α) > 0.
(2) ([23, Lemma 2.10]) If ̟i (α) > 0 for a unique i ∈ [n−1], then ̟i (α) ≥ 2.
w,α
If Nu,v(λ,k)
6= 0 and i 6= k in Proposition 4.2(1), then ̟i (α) = 1 as ̟i (α) > 1 contradicts (4.1), and this implies that sgi (u) = 1 and sgi (w) = 0.
w,α
Theorem 1.2 in [23] is their “quantum equals classical” result. It states that if Nu,v(λ,k)
6= 0,
′

w,α
,0
then there exist w ′ , u′ ∈ Sn such that Nu,v(λ,k)
= Nuw′ ,v(λ,k)
= cw
u′ ,v(λ,k) . A consequence of their
−1
′ ′ −1
proof is that wu = w (u ) , but we require more than that. We state and prove the result
we will need; this is extracted from the proof of Theorem 1.2 in [23].
′

Proposition 4.3. Suppose that u, w ∈ Sn , λ is a partition, α ∈ Nn−1 is nonzero, and
w,α
Nu,v(λ,k)
6= 0.
(1) There exists i ∈ [n−1] such that sgi (u) = 1, sgi (w) = 0, and
either ̟i (α) = 1 if i 6= k

or

̟i (α) = 2 if i = k .

w,α
wsi ,α−ei
(2) For any partition µ with |µ| = |λ|, with i as in (1), we have Nu,v(µ,k)
= Nus
.
i ,v(µ,k)

Proof. We first prove statements (1) and (2) in the case when µ = λ. By Proposition 4.2(1),
there is an i ∈ [n−1] such that ̟i (α) > 0. Suppose that i is not unique with this property.
w,α
Then we may assume that i 6= k, from which it follows that sgi (v(λ, k)) = 0. As Nu,v(λ,k)
6= 0,
Equation (4.1) implies that sgi (u) = 1 = ̟i (α) and sgi (w) = 0. Thus sgi (wsi ) = 1 =
sgi (v(λ, k)si ), so that
sgi (wsi ) + ̟i (α) = sgi (u) + sgi (v(λ, k)si ) = 2 .
By Proposition 4.1(2) with x = u, y = v(λ, k)si , and z = wsi , we have that
wsi ,α
wsi ,α−ei
w,α
Nu,v(λ,k)s
= Nus
= Nu,v(λ,k)
.
i
i ,v(λ,k)

(As s2i = 1 and sgi (z) = sgi (wsi ) = 1).
Now suppose that there is a unique i with ̟i (α) > 0. Then by Proposition 4.2(2), we have
w,α
̟i (α) ≥ 2. As Nu,v(λ,k)
6= 0, Proposition 4.1(1) implies that
sgi (w) = 0 ,

̟i (α) = 2 , and sgi (u) = sgi (v(λ, k)) = 1 .

Since sgi (v(λ, k)) = 1, we must have that i = k, as v(λ, k) has a unique descent at k. As
w,α
sgi (w) = 0, Proposition 4.1(2) with x = v(λ, k), y = u, and z = w implies that Nv(λ,k),u
=
wsi ,α−ei
w,α
wsi ,α−ei
z,α
z,α
Nv(λ,k),usi . As commutativity implies that Nx,y = Ny,x , we have Nusi ,v(λ,k) = Nu,v(λ,k) .


QUANTUM MURNAGHAN–NAKAYAMA RULE

14

This proves statement (1) and statement (2), in the case when µ = λ. The assumption that
|µ| = |λ| implies that for all i ∈ [n−1], sgi (v(λ, k)) = sgi (v(µ, k)), as v(µ, k) is the identity
permutation when |µ| = 0, and otherwise it has a unique descent at k. The arguments we
w,α
w,α
gave for Nu,v(λ,k)
will then also hold for Nu,v(µ,k)
, which completes the proof.

α

q w
Lemma 4.4. Suppose that u, w ∈ Sn , λ is a partition, α ∈ Nn−1 , and Cu,v(λ,k)
6= 0. Then
−1
−1
there exist y, z ∈ Sn with y ≤k z, ℓ(z) − ℓ(y) = |λ|, and zy = wu such that for every
qα w
w,α
partition µ with |µ| = |λ|, we have q −α Cu,v(µ,k)
= Nu,v(µ,k)
= czy,v(µ,k) .
0

q w
Proof. We use induction on |α|. Let α ∈ Nn−1 . When |α| = 0, α = 0 and Cu,v(µ,k)
= cw
u,v(µ,k) .
Suppose that α 6= 0. Let i ∈ [n−1] be the index guaranteed by Proposition 4.3(1). By
w,α
wsi ,α−ei
Proposition 4.3(2), if µ is a partition with |µ| = |λ|, then Nu,v(µ,k)
= Nus
. In particular,
i ,v(µ,k)
wsi ,α−ei
q α−ei
−1
−1
wu = wsi (usi ) and Nusi ,v(λ,k) 6= 0, which implies that usi ≤k q
wsi . This completes
the proof.


Example 4.5. We illustrate these results. In Example 3.4, the term q5,8 S(1,6,7,3,5)u appears
in the product Su ∗ pq4 (x1 , . . . , x5 ). As 78251 346 = (1, 6, 7, 3, 5)u, by Equation (3.3), there
78251 346,q5,8
6= 0. Since q5,8 = q α for
is a hook partition λ ⊆ R5,3 with |λ| = 4 such that N68235 741,v(λ,5)
78251 346,q

5,8
=
α = (0, 0, 0, 0, 1, 1, 1), we have ̟7 (α) = 1, so that by Proposition 4.3(2), N68235 741,v(λ,5)

78251 364,q

5,7
N68235 714,v(λ,5)
, as q α−e7 = q5,7 . We may apply Proposition 4.3(2) again as ̟6 (α − e7 ) = 1 to

78251 364,q

78251 634,q

5,7
5,6
obtain that N68235 714,v(λ,5)
= N68235 174,v(λ,5)
.
β
If β = α − e7 − e6 , so that q = q5,6 = q5 , then i = 5 = k is the only index with ̟i (β) > 0
78251 634,q5
78256 134
and we have ̟5 (β) = 2. By Proposition 4.3(2) again, N68235
174,v(λ,5) = c68231 574,v(λ,5) . Figure 6
shows the interval [68231 574, 78256 134]5, which has one peakless chain (the vertical one in
blue, with labels 6, 3, 1, 3).

q α 78251 346

78256 134
78236 154 78253 164

78256 341 q α 78231 546 q α 68251 347

78235 164 78251 364 68253 174

78236 541 q α 68231 547 68257 341

68235 174 78231 564 68251 374

78235 641

68237 541
68235 741

68231 574

Figure 6. Two minimal intervals in the quantum 5-Bruhat order on S8 [q].
As this has height 3 (as does the minimal permutation (1, 6, 7, 3, 5)), we see that
134
c78256
68231 574,v((2,1,1,0,0),5) = 1, and thus all of the other coefficients considered above are 1.
134
Results in [6] also show that c78256
68231 574,v((2,2,0,0,0),5) = 1, and thus
78251 634,q

5,6
78256 134
1 = c68231
574,v((2,2,0,0,0),5) = N68235 174,v((2,2,0,0,0),5)

78251 364,q

78251 346,q

5,7
5,8
= N68235 741,v((2,2,0,0,0),5)
,
= N68235 714,v((2,2,0,0,0),5)

by Lemma 4.4. For λ 6= (2, 1, 1, 0, 0), (2, 2, 0, 0, 0) with |λ| = 4, these coefficients vanish.

⋄


QUANTUM MURNAGHAN–NAKAYAMA RULE

15

Observe that the intervals may change when applying a reduction as in Proposition 4.3(2),
even though these reductions do not change wu−1 . Indeed, the two intervals in Figure 6
demonstrate this. (In [6], it was shown that the classical interval [u, w]k depends only on
w,α
wu−1.) We show that the coefficient Nu,v(λ,k)
depends only upon wu−1.
Theorem 4.6. For a partition λ, permutations w, u, w, u in Sn , exponent vectors α, α ∈ Nn−1
w,α
w,α
and indices k, l < n if both coefficients Nu,v(λ,k)
are nonzero and wu−1 = w u−1 ,
and Nu,v(λ,l)
then the coefficients are equal.
w,α
Proof. Suppose that Nu,v(λ,k)
6= 0. By Lemma 4.4, there exist y, z ∈ Sn with y ≤k z such that
w,α
−1
−1
ℓ(z) − ℓ(y) = |λ|, zy = wu and Nu,v(λ,k)
= czy,v(λ,k) .
w,α
6= 0. By Lemma 4.4 again, there exist y, z ∈ Sn with y ≤l z such
Suppose also that Nu,v(λ,l)
w,α
−1
= czy,v(λ,l) .
that ℓ(z) − ℓ(y) = |λ|, z y = w u−1 and Nu,v(λ,l)
Since wu−1 = w u−1 , we have that zy −1 = z y −1 . Then [6, Thm. E] implies that czy,v(λ,k) =

czy,v(λ,l) , which completes the proof.
