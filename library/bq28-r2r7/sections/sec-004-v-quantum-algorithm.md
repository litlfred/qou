---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-004-v-quantum-algorithm
section_title: "V.. QUANTUM ALGORITHM"
section_number: null
pages: 7-10
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
Here we describe a quantum circuit of size poly(n)
that prepares a state |ψg⟩/∥ψg∥; see Eq. (15). Our circuit
applies the quantum Fourier transform over group Sn to a
certain subset state constructed in the following lemma.
Lemma 3. Let g ∈Sn be a permutation and Cg ⊆Sn be
the conjugacy class of g. There exists a quantum circuit of
size poly(n) that prepares a subset state
|Cg⟩=
1
|Cg|

h∈Cg
|h⟩.
(22)
We defer the proof till the end of this section. Recall
that a QFT over the symmetric group Sn is deﬁned as a
unitary operator QFTn with input Hilbert space C[Sn] =
span(|g⟩: g ∈Sn) and output Hilbert space 
λ⊢n Cdλ ⊗
Cdλ such that
QFTn|g⟩=

λ⊢n

dλ
n!
dλ

i,j =1
⟨i|ρλ(g)|j ⟩|λ, i, j ⟩
(23)
for all permutations g ∈Sn.
Here dλ is the dimension of λ. The inverse QFT acts as
QFT†
n|λ, i, j ⟩=

dλ
n!

g∈Sn
⟨i|ρλ(g)|j ⟩∗|g⟩.
(24)
It is known [18] that QFTn can be implemented by a quan-
tum circuit of size poly(n). Applying QFTn to the subset
state |Cg⟩gives a state
|θg⟩= QFTn|Cg⟩
=

λ⊢n

dλ
n!
dλ

i,j =1
1
|Cg|

h∈Cg
⟨i|ρλ(h)|j ⟩|λ, i, j ⟩. (25)
Since 
h∈Cg h is a central element of the group algebra
C[Sn], we infer that

h∈Cg
ρλ(h) = bIdλ
(26)
for some complex number b ∈C. Here Idλ is the identity
matrix of size dλ. Taking the trace of Eq. (26) gives
b = |Cg|χλ(g)
dλ
.
(27)
Substituting Eqs. (26) and (27) into Eq. (25) and using the
identity |λ, i, j ⟩= |λ⟩⊗|i, j ⟩shows that
|θg⟩=

|Cg|
n!

λ⊢n
χλ(g)|λ⟩⊗|φλ⟩,
where
|φλ⟩=
1
√dλ
dλ

i=1
|i, i⟩.
Let U be a unitary operator that maps |λ⟩⊗|0⟩to |λ⟩⊗
|φλ⟩. One can realize U by a quantum circuit of size
poly(n), for example using the techniques of Ref. [34],
since the dimension dλ can be computed in time poly(n)
using the well-known hook length formula [35].
Applying U−1 to state |θg⟩and tracing out the second
register gives a state
|ωg⟩=

|Cg|
n!

λ⊢n
χλ(g)|λ⟩=
1
|Eg|

λ⊢n
χλ(g)|λ⟩,
where Eg is the centralizer of g; see Eq. (21). This a nor-
malized version of the desired state |ψg⟩if one encodes a
partition λ ⊢n by a bit string xλ+τ, as discussed in Sec.
III. By measuring state |ωg⟩in the standard basis one can
sample an irrep λ ⊢n from a probability distribution
Pg(λ) = (χλ(g))2
|Eg|
(row sampling).
(28)
This is equivalent to sampling a row of the character table
of Sn with the probability proportional to the character
squared.
A similar method can prepare a superposition of all per-
mutations g ∈Sn with amplitudes proportional to χλ(g) for
a given irrep λ ⊢n. Indeed, apply QFT†
n to an initial state
|θλ⟩=
1
√dλ
dλ

i=1
|λ, i, i⟩.
This gives a state
|ωλ⟩= QFT†
n|θλ⟩=
1
√
n!

g∈Sn
χλ(g)∗|g⟩
(the complex conjugate can be omitted since Sn charac-
ters are real). By measuring state |ωλ⟩in the standard basis
one can sample a permutation g ∈Sn from a probability
distribution
Pλ(g) = (χλ(g))2
n!
(column sampling).
(29)
This is equivalent to sampling a column of the character
table of Sn with the probability proportional to the charac-
ter squared (here we assume that columns are labeled by
permutations rather than conjugacy classes). We discuss
the classical hardness of these sampling problems in the
next section.
It is tempting to use our access to row and column sam-
pling to estimate the characters themselves via repeated
sampling. However, column sampling fails to yield eﬃ-
cient algorithms. To see this, note that χλ(g)2 ≤d2
λ ≤
e−C√nn! (C > 0 is a constant), where the second inequality
follows from known asymptotics [36]. Thus, the probabil-
ities in Eq. (29) are always superpolynomially small in n
and diﬃcult to estimate. Could row sampling yield eﬃcient
estimates of characters? All characters could be estimated
when |Eg| is polynomial in n. This holds, for example,
when c(g) = O(1). But, in this case, the MPS algorithm
of Sec. IV computes all characters in time polynomial in n.
One could look for cases where both |Eg| and χλ(g)2 are
large; a task we leave to future work. We note that similar
approaches were considered for computing multiplicities
in tensor product representations [27,37].
Proof. Let k = |Cg| and
Cg = {h1, h2, . . . , hk}.
Suppose that one can construct permutations f1, f2, . . . , fk ∈
Sn such that
hj = fj gf −1
j
(30)
for all j = 1, . . . , k and that there exists a quantum circuit
Q of size poly(n) such that
Q|hj ⟩⊗|0⟩= |hj ⟩⊗|fj ⟩
(31)
for all j = 1, . . . , k. Then the desired state |Cg⟩can be
prepared as follows. First prepare a state
|ψ1⟩=
1
√
n!

e∈Sn
|e⟩⊗|g⟩.
Apply a classical reversible circuit that maps |e⟩⊗|g⟩to
|e⟩⊗|ege−1⟩. This gives a state
|ψ2⟩=
1
√
n!

e∈Sn
|e⟩⊗|ege−1⟩.
Let Eg be the centralizer of g,
Eg = {b ∈Sn : gb = bg}.
Since left cosets of Eg in Sn can be identiﬁed with elements
of Cg, any permutation e ∈Sn can be uniquely decomposed
as e = fb for some f ∈{f1, . . . , fk} and some b ∈Eg. Thus,
|ψ2⟩=
1
k|Eg|
k

j =1

b∈Eg
|fj b⟩⊗|fj gf −1
j
⟩.
Here we noted that n! = k|Eg|. Tensoring in the third reg-
ister prepared in the |0⟩state and applying circuit (31) to
the second and third registers gives a state
|ψ3⟩=
1
k|Eg|
k

j =1

b∈Eg
|fj b⟩⊗|fj gf −1
j
⟩⊗|fj ⟩.
Next apply a classical reversible circuit that maps |fj b⟩⊗
|fj ⟩to |b⟩⊗|fj ⟩to the ﬁrst and third registers of |ψ3⟩. This
gives a state
|ψ4⟩=
1
k|Eg|
k

j =1

b∈Eg
|b⟩⊗|fj gf −1
j
⟩⊗|fj ⟩.
Now the ﬁrst register is left in a pure state (1/|Eg|)

b∈Eg |b⟩. Tracing out the ﬁrst register gives a state
|ψ5⟩=
1
√
k
k

j =1
|fj gf −1
j
⟩⊗|fj ⟩.
Applying the inverse of circuit (31) gives a state
|ψ6⟩=
1
√
k
k

j =1
|fj gf −1
j
⟩⊗|0⟩.
Finally, tracing out the second register we obtain a state
|ψ7⟩=
1
√
k
k

j =1
|fj gf −1
j
⟩=
1
|Cg|

h∈Cg
|h⟩= |Cg⟩.
Here the second equality makes use of Eq. (30) and the
equality Cg = {h1, h2, . . . , hk}.
It remains to construct permutations f1, . . . , fk and a
quantum circuit Q satisfying Eqs. (30) and (31). Suppose
that g consists of aℓcycles of length ℓ, where aℓis an
integer in the range [0, n] and
n =
n

ℓ=1
ℓaℓ.
(32)
Clearly, the conjugacy class Cg depends only on a1, . . . , an.
Let T be a Young tableau with n boxes and aℓrows of
length ℓfor ℓ= 1, . . . , n. We ﬁll T with integers 1, 2, . . . , n
in the row major order starting from the leftmost box in the
ﬁrst (top) row. Now integers 1, 2, . . . , n can be identiﬁed
with boxes of T. We can assume without loss of generality
that g cyclically shifts boxes in each row of T such that the
ith box in a row j goes to the (i + 1)th box in the same row
and the last box in a row j goes to the ﬁrst box in the same
row.
Consider a permutation h ∈Cg. Clearly, h has the same
cyclic type as g although boxes spanning each cycle of h
may be scattered over many rows of T. This determines a
partition of T into a disjoint union of subsets
T =
n
ℓ=1
aℓ

j =1
Tℓ,j
such that |Tℓ,j | = ℓand the boxes in each subset Tℓ,j span
a length-ℓcycle in h. Let bℓ,j ∈Tℓ,j be a box contained
in Tℓ,j with the smallest integer label (recall that each box
of T is labeled by an integer between 1 and n). Order the
subsets Tℓ,j with a ﬁxed ℓsuch that
bℓ,1 < bℓ,2 < · · · < bℓ,aℓ.
Let Bℓ,j be the ﬁrst (leftmost) box of T in the j th length-ℓ
row (rows are counted starting from the top). Let f ∈Sn
be a permutation such that
f [gp(Bℓ,j )] = hp(bℓ,j )
for all p = 0, 1, . . . , ℓ−1 (33)
and all ℓ, j . Here gp ∈Sn denotes the pth power of g. Since
any box of T can be obtained from some box Bℓ,j by apply-
ing powers of g, permutation f is uniquely determined by
h. Also, it is clear that the map h →f is computable in
time poly(n). Next we claim that h = fgf −1. Since h cycli-
cally shifts boxes in each subset Tℓ,j , it suﬃces to check
that
hp(bℓ,j ) = (fgf −1)p(bℓ,j )
(34)
for all ℓ, j , p. The above is equivalent to
hp(bℓ,j ) = f [gpf −1(bℓ,j )] = f [gp(Bℓ,j )],
(35)
which follows from Eq. (33). A classical circuit of size
poly(n) computing the map h →f can be converted to a
polynomial-sized quantum circuit Q1 computing a map
Q1|h⟩⊗|0⟩⊗|0⟩= |h⟩⊗|garbage(h)⟩⊗|f ⟩.
Here garbage(h) represents auxiliary bits used to make all
gates reversible. Making a copy of the third register in
the standard basis and applying the inverse of Q1 gives
a polynomial-sized circuit Q computing a map
Q|h⟩⊗|0⟩= |h⟩⊗|f ⟩,
where h = fgf −1. This is the circuit deﬁned in Eq. (31).
■
We note that the problem of preparing conjugacy class
states |Cg⟩for more general groups is considered in Ref.
[38]. Our proof of Lemma 3 closely follows the strategy
outlined in Appendix D of Ref. [38].
