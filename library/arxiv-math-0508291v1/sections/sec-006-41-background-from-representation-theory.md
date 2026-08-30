---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-006-41-background-from-representation-theory
section_title: "Background from representation theory"
section_number: 4.1
pages: 16-18
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
about the representation theory of Gelfand pairs. A useful r eference is Chap-
ter 7 of [Mac].
The induced representation 1 G
K decomposes in a multiplicity free way as
⊕s
r=0Vr, where V0 denotes the trivial representation of G. Let dr denote the
dimension of Vr. For 0 ≤ r ≤ s, let ωr denote the corresponding spherical
function on G, deﬁned by
ωr(x) = 1
|K|
∑
k∈K
χ(r)(x−1k)
where χ(r) is the character of Vr. The functions ωr are a basis of the space
of functions on G which are constant on the double cosets of K in G. Let
K0, · · ·,K s denote the double cosets of K in G and let g0, · · ·,g s be corre-
sponding double coset representatives, so that Ki =KgiK. It is convenient
to take g0 to be the identity element of G. From page 389 of [Mac], one has
that ωi(g0) = 1 for all i.
It is useful to recall facts which are analogs of those in Subs ection 3.1.
Lemma 4.1. ([Mac], page 389) Let ω be a spherical function of the Gelfand
pair (G,K ). Then ω(x−1) = ω(x).
The following two orthogonality relations are also useful.
Lemma 4.2. ([Mac], page 389) For 0 ≤i,j ≤s,
di
|G|
s∑
r=0
|Kr|ωi(gr)ωj(gr) = δi,j.
Lemma 4.3. For 0 ≤r,t ≤s,
s∑
i=0
diωi(gr)ωi(gt) = δr,t
|G|
|Kr|.
Proof. Consider thes×s matrix whose entry in the ith column and rth row is√
di|Kr|
|G| ωi(gr). By Lemma 4.2, the columns of this matrix are orthonormal.
Hence so are its rows, proving the lemma. □
If P is a K biinvariant probability on G (i.e. constant on double cosets
of K in G), let pm(Kr) denote the probability that the m-fold convolution
of P assigns to the double coset KgrK. Lemma 4.4 is an analog of Lemma
3.4 and could be proved along similar lines, as in [HSS]. Inst ead, we use the
language of Fourier analysis, as developed on page 395 of [Ma c].
17
Lemma 4.4. LetP be the K biinvariant probability on G which associates
mass 1 to the double coset Ku and mass 0 to all other K double cosets of
G. Then for 0 ≤r ≤s,
pm(Kr) = |Kr|
s∑
i=0
di
|G|ωi(gu)mωi(gr).
Proof. If f is a complex valued K biinvariant function on G, deﬁne ˆf (ωi)
(the Fourier transform of f at the spherical function ωi) by
ˆf (ωi) =
∑
g∈G
f (g)ωi(g).
Then the Fourier inversion theorem gives that
f = 1
|G|
s∑
i=0
ˆf (ωi)diωi.
It is also true that the Fourier transform of the convolution of two K biin-
variant functions is the product of their Fourier transform s. Thus the m-fold
convolution of f is equal to
1
|G|
s∑
i=0
(
ˆf (ωi)
) m
diωi.
The lemma now follows by taking f =P . □
To connect the study of random spherical functions with spec tral graph
theory, suppose for convenience that ( G,K ) is a symmetric Gelfand pair,
which means that KgK = Kg −1K for all g. This condition holds for the
examples in Subsections 4.3 and 4.4. Then ﬁxing a double cose tKu, one can
deﬁne a graph Hu whose vertices are the right cosets of K by connecting
Kh1 to Kh2 if and only if Kh1h−1
2 K = Ku. A more general construction
appears in [Le]. The graph Hu is vertex transitive, since G acts transitively
on the right cosets of K by sending Kh toKhg −1, and Kh1 is connected to
Kh2 if and only if Kh1g−1 is connected to Kh2g−1. Lemma 4.5 determines
the spectrum of random walk on Hu.
Lemma 4.5. Let (G,K ) be a symmetric Gelfand pair. Then for any double
coset Ku, random walk on the graph Hu has eigenvalues ωi(gu) occurring
with multiplicity di for 0 ≤i ≤s.
Proof. LetM be the transition matrix for random walk on Hu. Since Hu is
vertex transitive, the trace of M k is |G|/|K| multiplied by the probability
that the random walk on Hu started at the right coset K is at K after k
steps. By Theorem 7.5 of [Le], this return probability is
|K|
|G|
s∑
i=0
diωi(gu)k,
18
so that the trace of M k is∑ s
i=0diωi(gu)k. Since this is true for all k ≥ 0,
the result follows. □
Note that since d0+· · ·+ds = |G/K|, one can deﬁne a probability measure
on {0, · · ·,s } (or equivalently on the set {ω0, · · ·,ω s}) by choosing i with
probability di|K|
|G| . This is the Gelfand pair analog of the Plancherel measure
of a ﬁnite group, and in this paper it will be referred to as Pla ncherel mea-
sure. Lemma 4.5 showed that if ( G,K ) is a symmetric Gelfand pair, then the
eigenvalues of certain graphs on G/K occur with multiplicity proportional
to Plancherel measure.
