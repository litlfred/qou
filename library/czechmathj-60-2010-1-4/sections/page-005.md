---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
toc_source: undetermined
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
---
is clearly a minimal Gröbner-Shirshov basis for the left ideal k⟨X⟩S. Then k⟨X⟩S
is a free k⟨X⟩-module with the basis S1 by Lemma 2.3. Thus, we get the following
well-known result.
Corollary 2.4 (Cohn [12]). Any left (right) ideal of a free algebra k⟨X⟩is a free
left (right) k⟨X⟩-module.
Now, we quote below Kang-Lee’s Composition-Diamond lemma. Let S, T ⊂k⟨X⟩,
A = k⟨X|S⟩, let AM =A A/A(T + Id(S)) be a left A-module and f, g ∈k⟨X⟩. In
Kang-Lee’s paper [16], the composition of f and g is deﬁned as follows.
Deﬁnition 2.5 ([16], [17]).
Let < be a monomial ordering on X∗.
(a) If there exist a, b ∈X∗such that w = fa = bg with deg(f) > deg(b), then the
composition of intersection is deﬁned to be (f, g)w = fa −bg.
(b) If there exist a, b ∈X∗such that w = afb = g, then the composition of inclusion
is deﬁned to be (f, g)w = afb −g.
(c) A composition (f, g)w is said to be right-justiﬁed if w = f = ag for some a ∈X∗.
If f −g = P αiaisibi + P βjcjtj, where αi, βj ∈k, ai, bi, cj ∈X∗, si ∈S, tj ∈T
with aisibi < w and cjtj < w for each i and j, then f −g is called trivial with
respect to S and T and denoted by f ≡g mod(S, T ; w). When T = ∅, we simply
write f ≡g mod(S, w). If for any f, g ∈S, (f, g)w is deﬁned and f ≡g mod(S, w),
then we say S is closed under composition. Note that if this is the case, S is called
a Gröbner-Shirshov basis in k⟨X⟩which was ﬁrst introduced by Shirshov [26] (see
also [1], [2]).
Remark. A Gröbner-Shirshov basis S in k⟨X⟩is called minimal if there is no in-
clusion composition in S. If a subset S of k⟨X⟩is not a Gröbner-Shirshov basis, then
we can add to S all nontrivial compositions of polynomials of S, and by continuing
this process (maybe inﬁnitely) many times, we eventually obtain a Gröbner-Shirshov
basis Sc in k⟨X⟩. Such a process is called the Shirshov algorithm. If we delete from Sc
all polynomials with the leading term containing the leading term of other polynomi-
als in Sc as subwords, then we will get a minimal Gröbner-Shirshov basis equivalent
to Sc.
Deﬁnition 2.6 ([16], [17]).
Let S, T be monic subsets of k⟨X⟩. We call (S, T ) a
Gröbner-Shirshov pair for the A-module AM =A A/A(T +Id(S)), where A = k⟨X|S⟩,
if S is closed under composition, T is closed under the right-justiﬁed composition
with respect to S and T , and for any f ∈S, g ∈T and w ∈X∗such that if
(f, g)w is deﬁned (it means that afb = cg, where a, b, c ∈X∗, f ∈S, g ∈T and
deg(f) > deg(c)), we have (f, g)w ≡0 mod(S, T ; w).
62
