---
doc_id: arxiv-math-0110119v1
doc_title: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus"
section_id: sec-002-n-of-a-disk-with-2n-boundary-points
section_title: "n of a disk with 2n boundary points"
section_number: null
pages: 3-4
source_pdf: 0110119v1.pdf
source_sha256: 4904a86e8a340f59
toc_source: inferred
doc_brief: "Idempotents of the Hecke algebra become Schur functions in the skein of the annulus — The Hecke algebra Hn contains well known idempotents Eλ which are indexed by Young diagrams with n cells."
---
We consider a rectangle F with n outgoing points at the top and n incoming
points at the bottom, n ≥0. We denote the Homﬂy skein of this surface by Rn
n.
It is known to be isomorphic to the Hecke algebra Hn.
Rn
n gets an algebra structure by deﬁning D · E as putting D above E so that
the incoming points of D match with the outgoing points of E. Clearly, Rn
n is
generated as an algebra by the elementary braids σ1, . . . , σn−1 where σi agrees
with the identity braid up to a single positive crossing between the arcs which
connect the boundary points i and i + 1 (numbered from the left).
As a module, Rn
n is linearly spanned by the positive permutation braids ωπ
where π is a permutation on n letters (see [9] for details).
Rn
n has a well known quasi-idempotent an which is given in terms of the
positive permutation braids ωπ on n strings as
an =
X
π∈Sn
sl(π)ωπ
where l(π) is the writhe of the braid ωπ. This element ‘swallows’ an elementary
braid σi at the expense of a scalar s (see [9]).
Lemma 3.1 anσi = σian = san for any 1 ≤i ≤n −1.
This behaviour implies that an is central in Rn
n because the elementary braids
σ1, . . . , σn−1 generate Rn
n. Lemma 3.1 enables an inductive proof that anan =
αnan where the scalar αn is given by
αn = s
n(n−1)
2
[n][n −1] · · · [1]
where [i] = si−s−i
s−s−1 for any integer i ≥0.
We recall the map ρ from section 1.
Lemma 3.2 ρ

1
αnan

=
1
αnan for any n ≥1.
Proof We have ρ(ab) = ρ(a)ρ(b) for any elements a, b ∈Rn
n. This multiplicativity
together with lemma 3.1 implies that
σiρ(an) = ρ(σ−1
i )ρ(an) = ρ(σ−1
i an) = ρ(s−1an) = sρ(an)
in Rn
n. Hence, anρ(an) = αnρ(an). When we apply the map ρ to this equation we
get ρ(an)an = ρ(αn)an. The left hand sides of the previous two equations are equal
because an is central. Hence, αnρ(an) = ρ(αn)an and thus ρ

1
αnan

=
1
αnan.
⋄
3
·
=
Figure 2:
The multiplication in the skein of the annulus C.
Figure 3:
The additional arcs for the closure map ∆n : Rn
n →C.
Aiston and Morton [2] constructed idempotents Eλ in Rn
n for any Young di-
agram λ with n cells. To do this, they considered a three-dimensional version
of Rn
n where the distinguished boundary points are lined up along the cells of
the Young diagram λ.
In this setting they arranged several copies of idem-
potents ai and varaints bi of them along the rows and columns of λ to get a
quasi-idempotent. This element which is denoted eλ in the equivalent Rn
n-setting
satisﬁes eλeλ = αλeλ. It is suﬃcient to prove that αλ̸ = 0 for the specialization
v = s = 1 which turns Rn
n into the symmetric-group algebra as explained in [1].
We consider the rational functions in v and s as the set of scalars for the skein
Rn
n. Then, the element Eλ =
1
αλeλ is an idempotent of Rn
n.
