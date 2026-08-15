---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-009-32-the-unit-lattice
section_title: "The unit lattice"
section_number: 3.2
pages: 8-9
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
K ofKis the set of algebraic integers
αsuch thatα −1 is also an algebraic integer. By Dirichlet’s unit theorem (see, for
example, [32, Chapter 1.7]) the group of units (modulo the roots of unity)O×
K/{±1}
can be viewed as a lattice of rankd−1 inR d via the embedding
u7→(log|σ 1(u)|,...,log|σ d(u)|).
This is a lattice of rankd−1 inside the hyperplane
H={x∈R d :x 1 +···+x d = 0}.
The covolume of this lattice inHis
√
dRK, whereR K is the regulator (see [32,
Chapter 1, Proposition 7.5]). We write
B×(Y) ={α∈O ×
K :|log|σ i(α)||≤Yfor all 1≤i≤d}.
We note here the trivial, but crucial, fact that integers inB ×(Y) are still bounded
in the additive sense also, so that
B×(Y)⊆B +(eY ).
It is a well-known fact that points in the unit lattice are separated by an absolute
constant (independent of both the field and degree). This follows, for example, from
Schinzel’s lower bound for the Mahler measure [36, Theorem 2]. For our purposes
the following simple lemma (suggested by GPT-5.5 Pro) will suffice. Letϕ= 1+
√
5
2 ,
so that 0≤x 2 +x−2−2<1 wheneverx∈(ϕ −1,ϕ).
Lemma 3.4.Ifu∈O ×
K andϕ−1 <|σ i(u)|<ϕfor all1≤i≤dthenu∈{±1}.
Proof.Letα=u 2 +u−2−2∈O K. Ifα̸= 0 then, for each embeddingσ, we have
0<σ(u) 2 +σ(u)−2−2<1,
soσ(α)∈(0,1). This contradicts thatN(α) = Qσ(α) must be an integer. It
follows thatα= 0, whenceu 2 = 1 and sou∈{±1}.□
The proof of the following is similar to that of Lemma 3.3.
Lemma 3.5.LetKbe a totally real number field of degreed. For anyY≥1
Yd−1d−1/2R−1
K ≤|B×(Y)|≤10(5Y+ 1) d−1.
In the proof of Lemma 3.5 we will require bounds on the (d−1)-dimensional
volume ofH∩{x∈R d :∥x∥∞≤r}. Hensley [21] proved that
(3.1) (2r) d−1≤vold−1(H∩{x∈R d :∥x∥∞≤r})≤5(2r) d−1.
THE SUM-PRODUCT CONJECTURE IS F ALSE FOR REAL NUMBERS 9
In fact, the central limit theorem implies that this volume is∼
p
6/π(2r)d−1 as
d→∞(a remark which Hensley attributes to Selberg).
Proof.Losing only a factor of 2 (sinceuand−uare both mapped to the same
vector) the setB ×(Y) can be viewed as a subset of theL ∞ ball of radiusY,
intersected with the hyperplaneH. Moreover, by Lemma 3.4, points in this lattice
are at least (logϕ)-separated in theL∞ norm. Indeed, ifx,y∈O ×
K andx̸∈{y,−y}
thenx/y∈O ×
K\{±1}, and hence there existsσsuch that
|σ(x)|/|σ(y)|̸∈(ϕ −1,ϕ).
Combining the same standard packing argument as in the proof of Lemma 3.3 with
(3.1), there are at most 5( 2
cY+ 1) d−1 manyc-separated points inHintersected
with anL∞ ball of radiusY. This proves the upper bound since 2/log(ϕ)<5.
For the lower bound, we use the same idea as before: the covolume of the lattice
is
√
dRK, and hence there exists someasuch that the number of lattice points in
a+{x∈H:∥x∥ ∞≤Y/2}is at least
vold−1({x∈H:∥x∥ ∞≤Y/2})√
dRK
≥ Yd−1
√
dRK
.
The conclusion now follows by taking the difference set of these points.□
