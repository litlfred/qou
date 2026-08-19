---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-008-3-algebraic-number-theory
section_title: "Algebraic number theory"
section_number: 3
pages: 7-8
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
In this section we review the necessary concepts required from algebraic number
theory; with the exception of Theorem 3.2, these are all classical results that can
be found in most textbooks on the subject.
LetKbe a totally real number field of degreedoverQ, and let ∆ K be the
discriminant ofK(which is strictly positive ifKis totally real). LetR K be the
regulator ofK. For those unfamiliar with algebraic number theory, the important
role of these parameters for our purposes is that they control the covolume of the
lattices of the algebraic integers and units respectively. The only fact that we will
require aboutK(aside from it being totally real) is that these are both bounded
above byO(1) d. This is usually done with emphasis on ∆ K, but similar control on
RK follows from the following lemma.
Lemma 3.1.IfKis a totally real number field of degreed≥2then
RK≤∆ K.
Proof.As in the proof of [27, XIII, Theorem 3], for any reals >1, ifh K is the
class number ofKthen
2dRKhK≤2s(s−1)(π −d/2∆1/2
K )sΓ(s/2)dζ(s)d.
In particular, lettings= 2, sinceh K≥1 andd≥2,
RK≤R KhK≤4(π/12) d∆K≤∆ K.□
It therefore suffices to produceKwith ∆ K≤O(1) d, for arbitrarily larged. Such
towers were first constructed by Martinet [29].
Theorem 3.2(Martinet).There exists an absolute constantC >0such that,
for infinitely manyd, there exist totally real number fieldsKwith degreedwith
∆K≤C d.
There aredembeddingsK ,→R. These let us view the algebraic integers as
d-dimensional lattices. As we are concerned with both sums and products, both
the additive and multiplicative versions of these lattices will be useful to us.
3.1.The additive lattice.The ring of algebraic integersO K can be viewed as a
lattice of rankdinR d via the Minkowski embedding
α7→(σ 1(α),...,σ d(α)),
whereσ 1,...,σ d are the embeddingsσ i :K ,→R. The covolume of this lattice is
∆1/2
K (see [27, V, Lemma 2]). We write
B+(X) ={α∈O K :|σ i(α)|≤Xfor all 1≤i≤d}.
Lemma 3.3.LetKbe a totally real number field of degreed. For anyX≥1
Xd∆−1/2
K ≤|B +(X)|≤(2X+ 1) d.
Proof.In the embedding described above,B +(X) is contained inside theL ∞ ball
of radiusX. Moreover, points in this lattice are at least 1-separated in theL ∞
norm: ifx̸=y∈O K then, sincex−yis a non-zero algebraic integer, it has a
non-zero integral norm. Furthermore, sinceN(α) = Qd
i=1σi(α), we deduce
1≤|N(x−y)|≤
dY
i=1
|σi(x−y)|,
8 THOMAS F. BLOOM, WILL SA WIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
so there must exist 1≤i≤dsuch that|σ i(x)−σ i(y)|≥1. By a standard packing
argument (for example, placing disjoint balls of radius 1/2 around each lattice
point) there are at most (2X+ 1) d many 1-separated points in a ball of radiusX,
and we are done.
For the lower bound we use Blichfeldt’s lemma: the covolume of the lattice is
∆1/2
K , and hence there exists someasuch that the number of lattice points in
a+{x∈R d :∥x∥∞≤X/2}is at least
vol({x:∥x∥ ∞≤X/2})
∆1/2
K
= Xd
∆1/2
K
.
The conclusion now follows by taking the difference set of these points.□
