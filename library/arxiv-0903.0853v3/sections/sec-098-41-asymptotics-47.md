---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-098-41-asymptotics-47
section_title: "ASYMPTOTICS 47"
section_number: 4.1
pages: 53-55
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
In each case the limit is taken for all Σ-invariant open subsetU of C∗ such that
U∞ :=p(U). Then the A (U∞) form a sheaf of C-algebras and the A0(U∞) a
sheaf of ideals.
Lemma 4.1.1 . — Let U ⊂ C be a Σ-invariant open set and K ⊂ V be a
Σ-invariant strict subset of U . There exists a real number ρ> 0 such that the
closed disc of radius ρ|z| and center z lies in U for all z∈K. Moreover it is
possible to choose ρ> 0 such that
⋃
z∈K
¯D(z,ρ|z|) be a Σ-invariant strict subset
of U .
Proof. — There exists by deﬁnition a subset K ′ ofK, compact inU, such that
K = Σ(K ′). By compacity the result of the lemma is true for every z∈ K ′;
using the action of Σ we get that it is also true for all z∈K.
Let f ∈ A (U∞) and ˆf := ∑
n≥0
anzn its asymptotic expansion. We set
Rn := z−n(
f−Sn−1 ˆf
)
. We have f =
n∑
p=0
apzp +zn+1Rn+1; therefore the
derivativef ′ is given by:
f ′ =
n∑
p=1
papzp−1 + (n + 1)znRn+1 +zn+1R′
n+1.
If K⊂U is a Σ-invariant strict subset, then Rn+1 is bounded by MK,n+1 on
K. Therefore, using Cauchy formula for the derivative and lem ma 4.1.1, R′
n
is bounded by some positive constant MK,n +1
ρ|z| on K.
We havef ′ =
∑
n≥1
nanzn−1 and:
z−n(
f ′(x)−Sn−1 ˆf ′)
=z−n

f ′(x)−
n∑
p=1
napzp−1

 = (n + 1)Rn+1 +zR′
n+1.
Since
⏐
⏐(n + 1)Rn+1 +zR′
n+1
⏐
⏐≤
(
n + 1 +1
ρ
)
MK,n+1, then z−n(
f ′(x)−Sn−1 ˆf ′)
is bounded on K, so that f ′ admits ˆf ′ as a q-asymptotic expansion on U.
Hence A (V∞) is a diﬀerential algebra and A0(V∞) is a diﬀerential ideal of
A (V∞).
4.1.2. Asymptotic expansions and C∞ functions in Whitney sense.
—
48 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
Lemma 4.1.2 . — Let U be a Σ-invariant open set of C and f ∈ A (U∞).
LetK⊂U be an invariant strict subset.
(i) There exists a positive constant CK (depending on f ) such that, for all
z1,z 2∈K∪{ 0}:
|f(z1)−f(z2)|≤ CK|z1−z2|.
(ii) For all n∈ N there exists a positive constant CK,n (depending on f )
such that, for all z1,z 2∈K∪{ 0}:
⏐
⏐
⏐
⏐
⏐
⏐
f(z1)−
n∑
p=0
f (p)(z2)
p! (z1−z2)p
⏐
⏐
⏐
⏐
⏐
⏐
≤CK,n|z1−z2|n+1.
(iii)
lim
z1→0,z 2→0
z1,z 2∈K∪{0},z 1⁄=z2
1
|z1−z2|n

f(z1)−
n∑
p=0
f (p)(z2)
p! (z1−z2)p

 = 0.
Proof. — (i) We choose ρ > 0 (depending on K) as in lemma 4.1.1; then
K1 :=
⋃
z∈K
¯D(z,ρ|z|) is an invariant strict subset of U. We set:
MK := sup
z∈K
|f(z)−f(0)|
|z| , M ′
K1 := sup
z∈K1
⏐
⏐f ′(z)
⏐
⏐ .
Let z1,z 2∈K∪{ 0}. We shall consider separately three cases: (a) z2 = 0;
(b) z2⁄= 0 and|z1−z2|≤ ρ|z2|; (c) z2⁄= 0 and|z1−z2|>ρ|z2|.
The cases (a) and (b) are easy. In fact, if z2 = 0, then:
|f(z1)−f(z2)| =|f(z1)−f(0)|≤ MK|z1| =MK|z1−z2|.
If z2⁄= 0 and|z1−z2|≤ ρ|z2|, then z2∈K and the closed interval [z1,z 2] is
contained in K1; therefore:
|f(z1)−f(z2)|≤ M ′
K1|z1−z2|.
Now consider case (c). If z2 ∈ K and|z1−z2| > ρ|z2|, then we write
f(z1)−f(z2) =f(z1)−f(0)−
(
f(z2)−f(0)
)
and we have:
|f(z1)−f(0)|≤ MK|z1|≤ MK
(
|z2| +|z1−z2|
)
≤
(1
ρ + 1
)
MK|z1−z2|
and
|f(z2)−f(0)|≤ MK|z2|≤ 1
ρMK|z1−z2|,
