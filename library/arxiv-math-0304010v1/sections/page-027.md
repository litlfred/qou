---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-027
section_title: "Page 27"
section_number: null
pages: 27-27
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Theorem 5.4 (Law of large numbers, 1st form). Let λ range over Yn, and
let us view ¯λ( · ) as a random function deﬁned on the probability space (Yn, Mn),
where Mn is the Plancherel measure. Let Ωbe as above. Then we have
lim
n→∞
Z
(¯λ(x) −Ω(x))xkdx = 0
in probability, for any k = 0, 1, . . ..
(5.2)
Proof. Let Mn be the pushforward of Mn under the embedding Yn֒ →D0. Then
M n is a probability measure on the space D0. Given a “test” function f on D0, let
⟨f, ¯
Mn⟩denote the result of pairing between f and M n:
⟨f, Mn⟩=
X
λ∈Yn
f(¯λ( · ))Mn(λ).
Recall that the elements of A can be interpreted as functions on D0, see Deﬁnition
2.10 b). Let us take them as “test” functions.
We claim that
lim
n→∞⟨f, Mn⟩= f[Ω],
f ∈A.
(5.3)
In other words, the measures Mn on the space D0 converge to the Dirac measure
at Ω∈D0 in the weak topology deﬁned by the function algebra A.
Let us prove (5.3). Without loss of generality we may assume that f is a ho-
mogeneous element with respect to the weight grading in A. Then, by virtue of
Proposition 2.11,
⟨f, Mn⟩= n−wt(f)/2 ⟨f⟩n .
(5.4)
By Proposition 5.2, ⟨f⟩n is a polynomial in n of degree less or equal to 1
2 deg1(f).
Note that deg1( · ) ≤degN( · ) and degN( · ) coincides with wt( · ), see Proposition
4.10. Thus, the degree of ⟨f⟩n does not exceed 1
2 wt(f), which implies that (5.4)
has a limit as n →∞.
Expand f in the basis {p#
ρ }:
f =
X
ρ
fρp#
ρ .
By virtue of Proposition 5.1,
lim
n→∞n−wt(f)/2 ⟨f⟩n = f(1wt(f)/2)
with the understanding that the symbol f(1k/2) means 0 whenever k is odd.
Next, Proposition 4.9 (together with Proposition 4.10) implies the multiplicativ-
ity property
(fg)(1wt(fg)/2) = f(1wt(f)/2)g(1wt(g)/2) ,
where f, g are arbitrary weight homogeneous elements. Consequently, it suﬃces to
examine the case f = epk , i.e., to show that
(epk)(1k/2) = epk[Ω].
27
