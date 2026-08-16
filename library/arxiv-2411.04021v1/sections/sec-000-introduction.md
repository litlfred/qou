---
doc_id: arxiv-2411.04021v1
doc_title: "On the Gram determinants of the Specht modules Linda Hoyer ∗"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2411.04021v1.pdf
source_sha256: f5b6980f08d25394
doc_brief: "On the Gram determinants of the Specht modules Linda Hoyer ∗ — For every partitionλ of a positive integern, letSλ be the corresponding Specht module of the symmetric group Sn, and let det(λ)∈ Z"
---
Let n be a positive integer and letSn be the symmetric group ofn letters. There
is a canonical bilinear form on the Specht moduleSλ for a partitionλ of n, arising
from the embedding of the Specht module in a permutation representation. In [6],
James and Murphy introduced the determinantdet(λ)∈ Z of the Gram matrix of
the canonical bilinear form ofSλ with respect to the standard basis. For any prime
p, we define the integera(p)
λ such that
det(λ) = m·pa(p)
λ ,
where m is coprime top. We further denotefλ := dim(Sλ) and say thatλ is even
(resp. odd) if and only iffλ is.
∗linda.hoyer@rwth-aachen.de
1
arXiv:2411.04021v1  [math.CO]  6 Nov 2024
Amajorchallengeinrepresentationtheoryisthedeterminationofthedimensions
of the irreducible representationsDλ of Sn in positive characteristicp for λ a p-
regular partition ofn. Some results are known, for instance by [7, Theorem 7.3.18]
it holds that
dim(Dλ)≥fλ−a(p)
λ .
Now, there is an easy formula forfλ given by the hook lengths of the Young diagram
[λ], leaving open if there is something to be said abouta(p)
λ .
In this paper, we will show that forp = 2, the following statement holds:
Theorem 1.1.Letλ be an even partition ofn. Thena(2)
λ is even.
This confirms a special case of a conjecture of Richard Parker (see [9, Conjec-
ture 1.3]) about the Gram determinants (called theorthogonal determinantsin loc.
cit.) of theρ(G)-invariant, non-degenerate, symmetric bilinear forms of the repre-
sentations ρ affording the orthogonally stable characters ofG, for G an arbitrary
finite group.
Note that Theorem 1.1 fails to hold for some odd partitions; indeed, already
det((1, 1)) = 2. This implies that understanding the parity of a partition will be of
importance to us.
We now explain our strategy for the proof of Theorem 1.1. Letr be the integer
such that2r≤n< 2r+1. In [5, Theorem A] it was shown that for an odd partitionµ
ofn, there is a unique odd partitionD(µ) ofn− 2r such that the characterχD(µ) of
Sn−2r is a constituent of odd multiplicity ofResSn
Sn−2r (χµ). The partitionD(µ) can
explicitly be constructed by removing the unique2r-hook from the Young diagram
of λ, see also [1]. We extend the definition ofD to the set of all partitions, where
D in particular preserves the parity. We define theoddness rankto be the minimal
number of iterations ofD until the result becomes stationary, with a partition having
maximal oddness rank if and only if it is odd.
The formula given in [6] fordet(λ) uses certain partitions that arise by removing
the rim of some cell(i,j ) from the Young diagram ofλ and then wrapping it around
some row k with k < i. In [11], these partitions were called the branches of λ.
We will investigate theodd branches P odd
λ , for which we introduce an equivalence
relation on P odd
λ by saying that µ1 ∼ µ2 if and only if D(µ1) = D(µ2). The
desired statement then follows by an induction on the oddness rank ofλ and the
understanding of the arising equivalence classes ofP odd
λ .
This paper is a slightly modified version of results that have appeared in the
author’s PhD thesis [4]. In this thesis, we investigated the orthogonal determinants
of the finite groups of Lie type, the finite Coxeter groups and the alternating groups.
As it turns out, Theorem 1.1 has far-reaching consequences for the orthogonal de-
terminants of other classes of groups: Since the characters of the alternating groups
and the characters of the Coxeter groups of typesBn and Dn are built from the
2
characters of Sn, the theorem allows us to extend the result to these groups. With
some computer help for the exceptional groups, all finite Coxeter groups can be
covered. Moreover, Theorem 1.1 is essential in proving [9, Conjecture 1.3] for the
general linear groupsGLn(q) for an odd prime powerq; this relies on first reducing
to the unipotent characters and then using the formulas of the Gram determinants
of the Specht modules of Iwahori–Hecke algebras of typeAn found in [2], which will
be discussed elsewhere.
