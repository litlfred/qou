---
doc_id: arxiv-2301.00125v3
doc_title: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd"
section_id: sec-013-g-elementary-proofs-from-contour-deformations
section_title: "G Elementary proofs from contour deformations"
section_number: null
pages: 28-29
source_pdf: 2301.00125v3.pdf
source_sha256: 7ecd0cff7d6c2ec4
doc_brief: "Generating Function for Pinsky’s Combinatorial Second Mom ent Formula for the Generalized Ulam Problem Samen Hossein The Bronx High School of Science 75 Bronx Science Bvd — Given a uniform random"
---
Here we will prove Lemmas 3.6 and 3.7.
Proof of Lemma 3.6: Note that if ξ∈ (c2(x),d 1(x)) then by Lemma 3.4 we have
c1(x)<c 2(x)<ξ <d 1(x)<d 2(x). (214)
Therefore, forD1 as in Remark 2.3,
∀ξ∈ (c2(x),d 1(x)), we have ξ−c1(x), ξ−c2(x), d1(x)−ξ, d2(x)−ξ∈D 1. (215)
Similarly, if ξ∈ C\ R then we also have the conditions on the right-hand-side of (215) be cause the diﬀerences
above are also in C\ R (because c1(x),c2(x),d1(x) and d2(x) are all in R). So this proves that for ξ∈D 3(x),
we have the conditions on the right-hand-side of (215). So g(x;·) is analytic, as given by the formula in (65).
Note that
(
g(x;ξ)
)2
=Q1(x;ξ) by Lemma 3.2, equation (52). Also note that 1 is in ( c2(x),d 1(x)) by
Lemma 3.4 . So g(x; 1)∈ (0,∞) by (65) and (214). Since
(
g(x;ξ)
)2
and
(
f (x;ξ)
)2
satisfy
(
g(x;ξ)
)2
=Q1(x;ξ) and
(
f (x;ξ)
)2
= Q1(x;ξ)
ξ2 , (216)
and since g(x; 1) and f (x; 1) have the same phase (they are both real and positive) we see t hat g(x;ξ)/ξ and
f (x;ξ) are equal, for ξ in a neighborhood of 1. But then deﬁne the domain ~D3(x) by
~D3(x) = D2(x)∩D 3(x) =
(
U(0;d1(x))\U(0;c1(x))
)
\ (c1(x),d 1(x)). (217)
By analytic continuation this means
∀ξ∈ ~D3(x), we have g(x;ξ) = ξ·f (x;ξ). (218)
This follows because ~D3(x) is a connected, simply connected set. Therefore, there is unique analytic con-
tinuation of both ξ↦→g(x;ξ) and ξ↦→ξ·f (x;ξ) from a neighborhood of 1 to the entire domain ~D3(x). So
f (x;ξ) = g(x;ξ)/ξ on that whole domain. □
Proof of Lemma 3.7: We note that by continuity of the analytic function g, and the fact that D4(x) is
a subset of the closure of D3(x) (which is all of C), we may give the alternative formula
∀ξ∈D 4(x), we have ~g(x;ξ) = lim
ζ→ξ
ζ∈D3(x)
g(ζ). (219)
What we mean by saying this is the following: equations (69) and (70) a re equivalent to (219). In order to
see that for ~g the limits are well-deﬁned on all of D4(x), note that for ξ∈ (−∞,c 1(x)) we have for ζ =ξ +iǫ
with ǫ> 0, that
√
ζ−c1(x) =
√
−(c1(x)−ξ) +iǫ = i
√
c1(x)−ξ + ǫ√
c1(x)−ξ
+O(ǫ)2, (220)
28
and √
ζ−c2(x) =
√
−(c2(x)−ξ) +iǫ = i
√
c2(x)−ξ + ǫ√
c2(x)−ξ
+O(ǫ)2, (221)
as ǫ→ 0+. Therefore, we have
lim
ǫ→0+
g(x;ξ +iǫ) = x·
(
i
√
c1(x)−ξ
)(
i
√
c2(x)−ξ
)
·
√
d1(x)−ξ·
√
d2(x)−ξ. (222)
But, similarly, we will have
lim
ǫ→0+
g(x;ξ−iǫ) = x·
(
−i
√
c1(x)−ξ
)(
−i
√
c2(x)−ξ
)
·
√
d1(x)−ξ·
√
d2(x)−ξ. (223)
Since i2 = (−i)2 =−1 these two limits are equal. (The same will not be true for points ξ∈ (c1(x),c 2(x)), as
we will see shortly.) Therefore, the limit exists and equals
~g(x;ξ) = −x·
√
c1(x)−ξ·
√
c2(x)−ξ·
√
d1(x)−ξ·
√
d2(x)−ξ. (224)
A similar argument shows that if instead we had ξ∈ (d2(x),∞) then the limit lim ζ→ξg(x;ζ) would exist and
would equal
~g(x;ξ) = −x·
√
ξ−c1(x)·
√
ξ−c2(x)·
√
ξ−d1(x)·
√
ξ−d2(x). (225)
By elementary results of complex analysis, as in [1], it is easy to see tha t~g(x;·) is analytic on all of D4(x)
since it is the limit of the analytic function g(x;·) which is continuous across (−∞,c 1(x)) and (d2(x),∞). For
example, using the Cauchy integral formula and Morera’s theorem a nd the fact that the contour integrals are
continuous across (−∞,c 1(x)) and (d2(x),∞), one can check the integral conditions to be analytic (and there
are undoubtedly more elegant approaches using Riemann surfaces ). Now ~g(x;·)/ξ equals f (x;·) on ~D3(x) by
equations (66) and (69), or for example (218). But by continuity, the equality can be extended to all of D2(x)
sinceD2(x)⊆D 4(x). □
