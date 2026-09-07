---
doc_id: arxiv-1108.1048v3
doc_title: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS OF FINITE CLASSICAL TYPE"
section_id: sec-004-13-construction-of-irreducible-r-modules
section_title: "Construction of irreducible R-modules"
section_number: 1.3
pages: 10-14
source_pdf: 1108.1048v3.pdf
source_sha256: 6f2b83450ba923d0
doc_brief: "CONSTRUCTION OF IRREDUCIBLE REPRESENTATIONS OVER KHOVANOV-LAUDA-ROUQUIER ALGEBRAS OF FINITE CLASSICAL TYPE — We give an explicit construction of irreducible modules ove r Khovanov-Lauda- Rouquier"
---
In this subsection, we give a construction of irreducible gr aded R-modules as the irreducible
heads of certain induced modules, which is compatible with t he Kashiwara operators. More
precisely, set I(n+1) = I and let I(k) ⊂ I (k = 1, . . . , n) be subsets of I such that I(k) ⊆ I(k+1)
and |I(k)| = k. Let Bk be the crystal obtained from B(∞) by forgetting the i-arrows for
i /∈ I(k). Using highest weight vectors of connected components of Bk, we deﬁne irreducible
R-modules Nk(v) for k = 1, . . . , n and v ∈ B(∞). Then, we construct a crystal isomorphism
Φ : B(∞) → B(∞) deﬁned by Φ( v) = hd Ind(N1(v) ⊠ · · · ⊠ Nn(v)) (Proposition 1.10). We
emphasize that this crystal isomorphism Φ exists for an arbi trary symmetrizable Cartan
datum.
For M ∈ R(β)-fmod, Mk ∈ R(βk)-fmod (k = 1, . . . , m) and d ∈ Z>0, set
M ⊠0 = C, M ⊠d = M ⊠ · · · ⊠ M/bracehtipupleft
/bracehtipdownright/bracehtipdownleft/bracehtipupright
d
m
⊠
k=1
Mk = M1 ⊠ · · · ⊠ Mm.
Lemma 1.7. Let Mk ∈ R(βk)-fmod, dk ∈ Z≥0, and ik ∈ I dkβk for k = 1 , . . . , m. Suppose
that ik occurs in ch Ind(M ⊠dk
k ) with multiplicity ξk ∈ Z>0 for k = 1, . . . , m. Assume
(i) Ind (Mk ⊠ Mk′) ≃ Ind (Mk′ ⊠ Mk) for k, k′ = 1, . . . , m,
(ii) Ind
(
M ⊠dk
k
)
is irreducible for k = 1, . . . , m, and
(iii) i := i1 ∗ · · · ∗ im occurs in ch Ind
( m
⊠
k=1
M ⊠dk
k
)
with multiplicity ξ1ξ2 · · ·ξm.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 11
Then Ind
( m
⊠
k=1
M ⊠dk
k
)
is irreducible.
Proof. Let Nk = Ind
(
M ⊠dk
k
)
for k = 1, . . . , m, and let Q be a nonzero quotient of the module
Ind
( m
⊠
k=1
Nk
)
. By (ii) and Lemma 1.5 (2), we have an injective homomorphism
m
⊠
k=1
Nk֒→Resd1β1,...,dmβmQ.
Hence, by (iii), i occurs in chQ with multiplicity ξ1ξ2 · · ·ξm. Since Q is arbitrary, we obtain
that hd Ind
( m
⊠
k=1
Nk
)
is irreducible.
Now it follows from (i) that
Ind
( m
⊠
k=1
Nk
)
≃ Ind (Nm ⊠ Nm−1 ⊠ · · · ⊠ N1) .
Let L be a nonzero submodule of Ind
( m
⊠
k=1
Nk
)
. By (ii) and Lemma 1.5, there exists a
surjective homomorphism
ResL ։
m
⊠
k=1
Nk,
which implies that i occurs in chL with multiplicity ξ1ξ2 · · ·ξm by (iii). Therefore, we conclude
Ind
( m
⊠
k=1
Nk
)
= Ind
( m
⊠
k=1
M ⊠dk
k
)
is irreducible. □
Lemma 1.8. Let ∅ = I(0) ⊊ I(1) ⊊ I(2) ⊊ · · · ⊊ I(m) ⊂ I, and assume βk ∈ ∑
i∈I(k)
Z≥0αi for
k = 1, . . . , m. Let Mk ∈ R(βk)-fmod (1 ≤ k ≤ m) be such that
(i) εi(Mk) = 0 for i ∈ I(k−1),
(ii) hdMk is irreducible, and
(iii) hdMk occurs with multiplicity one as a composition factor of Mk.
Then
(1) hd Ind
( m
⊠
k=1
Mk
)
is irreducible,
(2) hd Ind
( m
⊠
k=1
Mk
)
occurs with multiplicity one as a composition factor of Ind
( m
⊠
k=1
Mk
)
,
(3) if ˜fik1 ≃ hdMk for some ik ∈ I βk , then ˜fi1
˜fi2 · · · ˜fim1 ≃ hd Ind
( m
⊠
k=1
Mk
)
.
Proof. We may assume that Mk ⁄= 1 for k = 1 , . . . , m. Let dk = |βk| for k = 1 , . . . , m, and
set d = d1 + · · · + dm. For w ∈ Sd and a reduced expression w = σi1 · · ·σis, let
τw = τi1 · · · τis.
12 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
For k = 1 , . . . , m, take ik = ( ik,1, . . . , ik,dk ) ∈ I βk such that e(ik)Mk ⁄= 0. It follows from (i)
that ik,1 ∈ I(k) \ I(k−1). Since Mk ∈ R(βk)-fmod, we have
e(β1, . . . , βm)τwe(i1 ∗ · · · ∗ im) ⁄= 0 if and only if w = id
for w ∈ Sd/Sd1 × · · · × Sdm. Therefore,
Resβ1,...,βm
(
Ind
( m
⊠
k=1
Mk
))
≃
m
⊠
k=1
Mk.
Let L =
m
⊠
k=1
hdMk. It follows from (ii) and (iii) that [ L] occurs with multiplicity one in
[Resβ1,...,βm
(
Ind
( m
⊠
k=1
Mk
))
] in the Grothendieck group G0(R(β1) ⊗ · · · ⊗ R(βm)). Let Q be
a nonzero quotient of Ind
( m
⊠
k=1
Mk
)
. By Lemma 1.5, we have a nontrivial homomorphism
m
⊠
k=1
Mk → Resβ1,...,βmQ,
which implies that [ L] occurs in [ Resβ1,...,βmQ] with multiplicity one. Since Q is arbitrary, we
obtain assertions (1) and (2).
Now assume that N = hd Ind
( m
⊠
k=1
Mk
)
, and let Nk = hdMk for k = 1, . . . , m. Then there
is a surjective homomorphism
Ind
( m
⊠
k=1
Mk
)
։ Ind
( m
⊠
k=1
Nk
)
,
which implies that N = hd Ind
( m
⊠
k=1
Nk
)
. We will use induction on |wt(N )|. If |wt(N )| = 0,
there is nothing to prove, so suppose that |wt(N )| > 0. Since N1 is nontrivial, we can take
i ∈ I(1) such that εi(N1) ⁄= 0. Let ε = εi(N1). Then, by (i) and Lemma 1.5, we have
ε = εi
(
Ind
( m
⊠
k=1
Nk
))
= εi(N ).
Since ei is exact, there is a surjective homomorphism
eε
i
(
Ind
( m
⊠
k=1
Nk
) )
։ eε
i N.
Then, by [15, Lem. 3.9], we know that [ eε
i N ] = q−ε+1
i [ε]qi! [˜eε
i N ] and
[
eε
i
(
Ind
( m
⊠
k=1
Nk
))]
= [Ind ((eε
i N1) ⊠ N2 ⊠ · · · ⊠ Nm)]
= q−ε+1
i [ε]qi! [Ind ((˜eε
i N1) ⊠ N2 ⊠ · · · ⊠ Nm)]
at the level of the Grothendieck group G0(R(β1 + · · · + βm − εαi)). Since hd Ind((˜eε
i N1) ⊠
N2 ⊠ · · · ⊠ Nm) is irreducible by (1), we obtain
hd Ind(˜eε
i N1 ⊠ · · · ⊠ Nm) ≃ ˜eε
i N.
REPRESENTATIONS OVER KLR ALGEBRAS OF FINITE CLASSICAL TYPE 13
Therefore, assertion (3) follows from a standard induction argument. □
Let n = |I| be the rank of Uq(g), and let I(k) ⊂ I (k = 1 , . . . , n) be subsets of I = I(n+1)
such that I(k) ⊂ I(k+1) and |I(k)| = k for all k. We denote by Uq(gk) the subalgebra of Uq(g)
generated by ei, f i (i ∈ I(k)) and qh (h ∈ P∨). Let Bk be the crystal obtained from B(∞)
by forgetting the i-arrows for i /∈ I(k). Then Bk can be viewed as a Uq(gk)-crystal.
Lemma 1.9. For each k = 1, . . . , n, every connected component of Bk has a unique highest
weight vector.
Proof. Let C be a connected component of Bk. For λ ∈ P+, let ιλ : B(λ) → B(∞) ⊗ Tλ ⊗ C
be the embedding in (1.1) and let
~C = {v ⊗ tλ ⊗ c | v ∈ C} ⊂ B(∞) ⊗ Tλ ⊗ C.
By taking λ ≫ 0, we can assume that ~C ∩ im(ιλ) ⁄= ∅. Since Cλ := ι−1
λ ( ~C) is a nontrivial
highest weight subcrystal of the crystal obtained from B(λ) by forgetting the i-arrows with
i /∈ I(k), there is an element uC ∈ C such that ι−1
λ (uC ⊗ tλ ⊗ c) is the highest weight vector
of the subcrystal Cλ. Note that uC does not depend on the choice of λ if ~C ∩ im(ιλ) ⁄= ∅. By
construction, the element uC is a unique highest weight vector of C. □
Take v ∈ B(∞). Let u0 = v and let uk be the highest weight vector of the connected
component Ck of Bk containing v for k = 1 , . . . , n. By construction, there is a chain of
injective maps
C1֒C 2֒· · ·֒C n−1֒→B(∞).
For k = 1, . . . , n, let ik be a sequence of I such that uk−1 = ˜fikuk. Note that v = ˜fi1
˜fi1 · · · ˜fin1.
Let
Nk(v) = ˜fik1 ∈ B(∞).(1.4)
Hence, for each v ∈ B(∞), we have the corresponding n-tuple ( N1(v), N2(v), . . . ,Nn(v)) of
modules in B(∞).
Proposition 1.10.
(1) For v ∈ B(∞), let Nk(v) be the irreducible module deﬁned by (1.4). Then hd Ind
( n
⊠
k=1
Nk(v)
)
is irreducible.
(2) The map Φ : B(∞) − →B(∞) deﬁned by
Φ( v) = hd Ind
( n
⊠
k=1
Nk(v)
)
for v ∈ B(∞)
is a crystal isomorphism.
14 GEORGIA BENKART, SEOK-JIN KANG, SE-JIN OH, AND EUIYONG PA RK
Proof. Since it is obvious that Φ( 1) = 1, we assume 1 ⁄= v ∈ B(∞) and let Nk(v) = ˜fik1 be
the corresponding irreducible module given in (1.4) for k = 1 , · · · , n. By construction, we
have
v = ˜fi1
˜fi1 · · · ˜fin1 and εi(Nk(v)) = 0 for all i ∈ I(k−1).
Therefore, it follows from Lemma 1.8 that hd Ind
( n
⊠
k=1
Nk(v)
)
is irreducible and
Φ( ˜fi1
˜fi2 · · · ˜fin1) = hd Ind
( n
⊠
k=1
Nk(v)
)
= ˜fi1
˜fi2 · · · ˜finΦ( 1).
□
