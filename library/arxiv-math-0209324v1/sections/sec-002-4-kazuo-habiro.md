---
doc_id: arxiv-math-0209324v1
doc_title: "Cyclotomic completions of polynomial rings"
section_id: sec-002-4-kazuo-habiro
section_title: "KAZUO HABIRO"
section_number: 4
pages: 4-5
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "Cyclotomic completions of polynomial rings — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which arises from"
---
there is a sequence S′∋ n′⇔R···⇔ R n in S, then the homomorphism
ρR
S,S ′ is injective. A nonempty subset S⊂ N is said to be ⇔R-connected if
the graph Γ R(S) is connected. It follows that if S⊂ N is⇔R-connected,
then for any nonempty subset S′⊂ S the homomorphism ρR
S,S ′ is injective.
In particular, since N is⇔Z-connected, for each n∈ N the homomorphism
ρZ
N, {n} : Z[q]N→ Z[q]{n}(
= lim←−j≥0
Z[q]/ (Φ n(q)j)
)
is injective.
If ζ is a primitive nth root of unity, then the homomorphism
σ Z
N,ζ : Z[q]N→ Z[ζ][[q− ζ]],
which is induced by the inclusion Z[q]⊂ Z[ζ][q] and factors through ρZ
N, {n},
is injective (Theorem 5.4). In other words, each element of Z[q]N is uniquely
determined by its power series expansion in q−ζ. In particular, the invariant
I(M ) of an integral homology sphere M is completely determined by its
expansion in q− ζ for one root ζ of unity, which in the case ζ = 1 is the
Ohtsuki series [7]. Since Z[ζ][[q− ζ]] is an integral domain, it follows that
so is Z[q]N (Corollary 5.5).
We are also interested in the homomorphism
τR
S,T : R[q]S→ PT (R) =
∏
n∈T
R[q]/ (Φ n(q))
for T⊂ S⊂ N, induced by the homomorphism R[q]→ PT (R), f (q)↦→(f (q)
mod (Φ n(q)))n∈T , where R is a subring of the ﬁeld ¯Q of algebraic numbers.
If S is⇔R-connected, and for some n∈ S there are inﬁnitely many elements
m∈ T with m⇔R n, then τR
S,T is injective (Theorem 6.1). In particular,
if T⊂ N contains inﬁnitely many prime powers, then τZ
N,T : Z[q]N→ PT (Z)
is injective. Hence it follows that if Z is a set of roots of unity containing
inﬁnitely many elements of prime power order, then the homom orphism
τR
S,Z : Z[q]S→ PZ (Z) =
∏
ζ∈Z
Z[ζ],
induced by Z[q]→ PZ (Z), f (q)↦→(f (ζ))ζ∈Z , is injective (Theorem 6.3). In
other words, each element in Z[q]N is uniquely determined by its values at
roots of unity in such a set Z. In particular, it follows that the invariant
I(M ) of an integral homology sphere M is completely determined by the
Witten-Reshetikhin-Turaev invariants τζ(M ) with ζ∈ Z.
Recall that a holomorphic function deﬁned in a region is dete rmined either
by the power series expansion at one point or by its values at a ny inﬁnitely
many points contained in a compact set in the region. The prop erties of
Z[q]N described above may be interpreted that Z[q]N behaves like the ring of
“holomorphic functions deﬁned in the set of the roots of unit y”. These prop-
erties are not as obvious as they might ﬁrst appear; the ring Q[q]N, which
CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS 5
contains Z[q]N as a subring, is quite contrasting. We have an isomorphism
Q[q]N≃
∏
n∈N
Q[q]{n},
see Section 7.5. It follows that ρQ
N, {n} for n∈ N and τQ
N, N are not injective
(but surjective), and that Q[q]N is not an integral domain.
The results stated above are more or less generalized in the l ater sections.
The rest of the paper is organized as follows. In Section 2 we ﬁ x some
notations. Section 3 deals with what we might call “monic com pletions”
of R[q], which are generalizations of cyclotomic completions deﬁ ned using
monic polynomials instead of cyclotomic polynomials. In Se ction 4 we apply
the results in Section 3 to cyclotomic completions, and stud y the conditions
for the homomorphisms ρR
S,S ′ to be injective. In Section 5 we consider the
power series expansion of the elements of R[q]S in q− ζ with ζ∈ R root of
unity of order contained in S. In Section 6 we study the homomorphisms
τR
S,T and τR
S,Z . In Section 7 we give some remarks.
