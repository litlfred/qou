---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL(2)"
section_id: sec-003-twisted-hochschild-and-cyclic-homology
section_title: "twisted hochschild and cyclic homology"
section_number: null
pages: 4-6
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
doc_brief: "Twisted homology of quantum SL(2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra o f the quan- tum SL(2) group"
---
LetA be a unital, associative algebra over a ﬁeld k (assumed to be of
characteristic zero) and σ an automorphism. We deﬁne the cyclic object
[2], [14] underlying twisted cyclic homology HCσ
∗ (A) of A relative to σ.
SetCn :=A⊗(n+1). For clarity, we will denote a0⊗a1⊗···⊗ an∈Cn by
(a0,a 1,...,a n). Deﬁne
dn,i (a0,a 1,...,a n) = (a0,...,a iai+1,...,a n) 0 ≤i≤n− 1
dn,n (a0,a 1,...,a n) = (σ(an)a0,a 1,...,a n−1)
sn,i (a0,a 1,...,a n) = (a0,...a i, 1,ai+1,...,a n) 0 ≤i≤n
4
τn(a0,a 1,...,a n) = (σ(an),a 0,...,a n−1) (8)
For σ = id these are the face, degeneracy and cyclic operators of th e
standard cyclic object associated to A [14]. For general σ the operator
Tn :=τn+1
n is not equal to the identity, but all other relations of the cy clic
category are fulﬁlled. Hence C∗ becomes what is called a paracyclic object
[6]. To obtain a cyclic object, we pass to the cokernels Cσ
n := Cn/C1
n,
C 1
n := im(id−Tn). Dualizing [12], we call the cyclic homology of this cyclic
object the σ-twisted cyclic homology HCσ
∗ (A) of A. Hence HCσ
∗ (A) is
the total homology of Connes’ mixed ( b,B )-bicomplex
b4
↓ b3
↓ b2
↓ b1
↓
Cσ
3
B2
←−−−−Cσ
2
B1
←−−−−Cσ
1
B0
←−−−−Cσ
0
b3
↓ b2
↓ b1
↓
Cσ
2
B1
←−−−−Cσ
1
B0
←−−−−Cσ
0
b2
↓ b1
↓
Cσ
1
B0
←−−−−Cσ
0
b1
↓
Cσ
0
(9)
The maps bn and Bn are given by
bn =
n∑
i=0
(−1)idn,i, B n = (1 + (−1)nτn+1)snNn, (10)
withNn = ∑ n
j=0 (−1)njτj
n, and sn :Cσ
n→Cσ
n+1 the “extra degeneracy”
sn(a0,a 1,...,a n) = (1,a 0,a 1,...,a n) (11)
We calculate HCσ
∗ (A) via the spectral sequence associated to the
mixed complex. Let HHσ
∗ (A) denote the entries of its ﬁrst page, that
is, HHσ
n (A) := Hn(Cσ
∗,b ∗) (the homologies of the columns). For σ = id
these are the Hochschild homologies HH ∗(A) = H∗(A,A). Hence we call
HHσ
∗ (A) as in [12] the σ-twisted Hochschild homology of A.
To computeHHσ
∗ (A) consider the mixed complex (9) with Cσ
n replaced
by the original Cn. This is not a bicomplex: the commutation relations
in a paracyclic object imply that the (lifts of the) operator s b∗ and B∗
anticommute according to (see [6], Theorem 2.3)
bn+1Bn +Bn−1bn = id−Tn. (12)
But the columns form the complex (C∗,b ∗) which computes the Hochschild
homology H∗(A,σA) of A with coeﬃcients in the bimodule σA which is
A as a vector space with bimodule structure
a⊲b⊳c :=σ(a)bc (13)
In many cases Cn =C 0
n⊕C 1
n, C 0
n := ker(id−Tn), for example when σ is
diagonalizable. In this case, Tn =σ⊗(n+1) is also diagonalizable, and C 0
n
and C 1
n are the eigenspace of Tn corresponding to the eigenvalue 1 and
the direct sum of all other eigenspaces, respectively. Then :
5
proposition 2.1 If Cn =C 0
n⊕C 1
n, then H∗(A,σA)∼=HHσ
∗ (A).
Proof. Note that (12) implies that b∗ commutes with id −T∗, so the
decomposition Cn = C 0
n⊕ C 1
n deﬁnes a decomposition of complexes,
and we can identify HHσ
∗ (A) with the homologies of the subcomplex
(C 0
∗,b ∗)⊂ (C∗,b ∗). Hence H∗(A,σA) is the direct sum of HHσ
∗ (A) and
the homologies of ( C 1
∗,b ∗). But (id −Tn)|C1n is a bijection under these
assumptions, and we have on C 1
n again by (12) the relation
bn+1(1−Tn)−1Bn + (1−Tn)−1Bn−1bn = id.
So (id −Tn)−1B∗ is a contracting homotopy for ( C 1
∗,b ∗) and the claim
follows. ✷
This will allow us to calculate HHσ
∗ (A) using standard techniques of
homological algebra.
The spectral sequence calculation is most eﬃciently done by passing to
the normalized mixed complex (see for example [23], Applica tion 9.8.4).
This leaves the ﬁrst page unchanged. The second step is to cal culate the
horizontal homology of the rows relative to the maps Bn which in the
normalized complex are given explicitly by
Bn(a0,...,a n) =
n∑
i=0
(−1)ni(1,σ (ai),...,σ (an),a 0,...,a i−1). (14)
For quantumSL(2), we ﬁnd that everything stabilises at the second page,
and we can then read oﬀ the twisted cyclic homology.
For later use we note that by using the Hochschild-Kostant-R osenberg
theorem applied to an appropriate subalgebra, we obtain:
lemma 2.2 If x, y are commuting elements of A, with σ(x) = x, σ(y) =
y, then for any s, t≥ 0 we have
B0[xsyt] = t[(xsyt−1,y )] +s[(xs−1yt,x )]∈HHσ
1 (A)
From now on, we will drop the suﬃces and write bn as b.
