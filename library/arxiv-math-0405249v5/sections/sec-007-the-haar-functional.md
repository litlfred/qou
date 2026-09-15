---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL(2)"
section_id: sec-007-the-haar-functional
section_title: "the haar functional"
section_number: null
pages: 9-10
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
doc_brief: "Twisted homology of quantum SL(2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra o f the quan- tum SL(2) group"
---
The Hopf algebra A is cosemisimple [11], that is, there is a unique linear
functional h :A→ k satisfying h(1) = 1 and
(h⊗ id)∆( x) = h(x)1 = (id⊗h)∆( x) ∀x∈A (26)
If k = C and q∈ R, then A can be made into a Hopf ∗-algebra whose
C*-algebraic completion is Woronowicz’s quantumSU (2) group [24]. The
functional h extends to the Haar state of this compact quantum group.
Hence (with slight abuse of terminology) we also in the gener al case call
h the Haar functional of A. For any x, y∈A , we have
h(xy) = h(yσmod(x)) (27)
where σmod is the so-called modular automorphism of A given by
σmod(a) = q−2a, σ mod(d) = q2d, σ mod(b) = b, σ mod(c) = c (28)
So h is a σ−1
mod-twisted cyclic 0-cocycle.
3.3 the automorphism group of A(SLq(2))
Forλ,µ∈k× there are unique automorphisms σλ,µ ,τλ,µ ofA with
σλ,µ (a) = λa, σ λ,µ (b) = µb, σ λ,µ (c) = µ−1c, σ λ,µ (d) = λ−1d,
τλ,µ (a) = λa, τ λ,µ (b) = µ−1c, τ λ,µ (c) = µb, τ λ,µ (d) = λ−1d. (29)
It is easy to check that this list is complete, although we do n ot know a
reference where this was pointed out explicitly:
proposition 3.1 Ifσ is an automorphism of A(SLq(2)), then either σ =
σλ,µ or σ =τλ,µ for some λ,µ .
Proof. Using the Z-grading and the N-ﬁltrations mentioned above it is a
straightforward calculation to check that up to rescaling a nd exchanging
b and c the original generators are the only elements of the algebra that
fulﬁll the deﬁning relations. ✷
The σλ,µ act diagonally with respect to the generators a,b,c,d . The
τλ,µ are also diagonalizable. For ﬁxed λ,µ deﬁne x± = c±µb. Then
τλ,µ (x±) =±x±, and a,x +,x −,d generateA. So by Proposition 2.1:
corollary 3.2 ForA =A(SLq(2)), and for each n and every automor-
phism σ, we have HHσ
n (A)∼=Hn(A,σA).
9
4 Twisted Hochschild homology of A(SLq(2))
