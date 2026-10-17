---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-019-31-bloch-group-and-p-adic-dilogarithm
section_title: "Bloch group and p-adic dilogarithm"
section_number: 3.1
pages: 37-39
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
the dilogarithm function, the Bloch group, and their p-adic counterparts. The dilogarithm
function, defined initially for |x| < 1 by
Li2(x) =
∞
X
k=1
xk
k2 ,
(172)
satisfies the famous five-term functional equation. The five-term equation reflects the al-
gebraic structure of the third algebraic K-group of a field, which is isomorphic, modulo
well-understood torsion, with the Bloch group of the number field [9, 50]. Therefore, func-
tions that satisfy the five-term relation give homomorphisms from the Bloch group, and
hence from the third algebraic K-group. The Bloch-Wigner dilogarithm D : C →R, given
by D(z) = Im(Li2(z)) + arg(1 −z) log |z|, is one such function and satisfies the functional
equation
D(x) + D(y) = D(xy) + D
 1 −y
1 −x−1

+ D
 1 −x
1 −y−1

.
(173)
The usual dilogarithm is a holomorphic but multivalued function from C −{0, 1}.
The
Bloch-Wigner dilogarithm gives a well-defined continuous real valued function on C. Taking
a number field K and an infinite place σ (i.e. σ : K →C an embedding of the number
field into C) we can define a map Dσ : B(K) →R defined on the symbols in B(K) by
linearly extending Dσ([z]) = D(σ(z)). An analogous function valued in Cp was defined by
Coleman [11] for finite places. The main point is to find an analytic extension of Li2(z) in
equation (172), which only converges for z ∈Cp with |z| < 1. Coleman used an “analytic
continuation along Frobenius” to define such a function after choosing a logarithm log :
C×
p →Cp. For example, one could take the Iwasawa logarithm, which has log(p) = 0. (The
values of the dilogarithm only depend on this choice in the residue discs around 1 and ∞and
importantly the primes we consider will never require us to evaluate here.) Then Coleman
obtains a well-defined function Li2 : Cp ∖{1} →Cp and defines
Dp : Cp ∖{0, 1} →Cp,
z 7→Li2(z) + 1
2 log(z) log(1 −z) .
(174)
38
STAVROS GAROUFALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
This function also satisfies equation (173). Therefore, this gives homomorphisms from the
Bloch group in a completely analogous way to the Bloch-Wigner dilogarithm but for finite
places (i.e. σ : K →Cp an embedding of the field). Conveniently, for unramified primes p
of the field K, we can combine these functions Dσ into one function Dp : B(K) →Kp such
that the projection onto the various field factors of Kp corresponding to σ agree with the
function Dσ. Let R = OK[ 1
∆] as in (11) and R∧
p denote its p-adic completion. The p-adic
polylogarithm functions satisfy the following integrality properties:
Lemma 3.1. If z ∈R∧
p and |z|p = 1 and |z −1|p ≥1 then Dp(z) ∈p2R∧
p .
Proof. From [8, Cor. 4.9] we know that
Li2(ζ) ∈p2Zp[ζ]
and
Li1(ζ) ∈pZp[ζ] .
(175)
This implies that Dp(ζ) ∈p2R∧
p if ζ is a root of unity. Then expanding these as Taylor series
near ζ and noting that we assumed p > 3 is unramified proves the result on the unit discs
near ζ.
□
In what follows, we are mostly interested in evaluating Li2(ζ) when ζ is a root of unity of
order prime to p. This case is important because these are rank 1 elements, i.e., they satisfy
the equation
φpζ = ζp .
(176)
Although the p-adic polylogarithm Lin is a transcendental function for n > 0, its mod-
ulo p reduction can be described by a rational function, the finite polylogarithm function
introduced by Kontsevich (unpublished note, reproduced as an appendix to [17])
lin,p(z) =
p−1
X
k=1
zk
kn .
(177)
Below, we denote by Qps the unique unramified extension of Qp of degree s (with residue
field Fps), and its ring of integers by Zps.
Proposition 3.2. [6, Cor. 2.2] For a prime p and ζ ∈µ(Qps) with ζ̸ = 1, we have
p−2Dp(ζp) =
1
(ζ −1)pli2,p(ζ)
(mod p) .
(178)
We can use this proposition to prove the following.
Proposition 3.3. For every positive integer s, we have
SpanZp{p−2Dp(ζ) | ζ ∈µ(Qps)} = Zps .
(179)
Proof. It suffices to prove (179) modulo p. Consider the rational function
fp(x) =
li2,p(x)
(x −1)p .
(180)
Since li2,p(1) ≡0 (mod p) and li′
2,p(1) ≡0 (mod p), there exists a polynomial gp(x) of
degree p −3 such that fp(x) =
gp(x)
(x−1)p−2. We can view fp as a map
fp : Fps ∖{1} →Fps .
(181)
THE HABIRO RING OF A NUMBER FIELD
39
Then we see that f −1
p (c) ⊆{x ∈Fps∖{1} | c(x−1)p−2−gp(x)} and therefore #f −1
p (c) ≤p−2.
This gives a lower bound for the size of the image of fp
#image(fp) ≥ps −1
p −2
> ps−1 ,
(182)
which implies that ps−1 < pr = #SpanFp(image(fp))
≤
ps.
Therefore, we see that
SpanFp(image(fp)) = Fps. Since µ(Qps) ≃F×
ps, Proposition 3.2 implies that p−2Dp(ζ) span
Fps as an Fp-vector space. The result follows.
□
Note that if K/Q is a number field and p is unramified, so that p = Q
i pi, N(pi) = psi,
then Kp ≃Q
i Qpsi and Kn(Kp) ≃Q
i Kn(Qpsi) for every n.
Theorem 9. Assume p > 3. We have a Zp-linear isomorphism
Dp : K3(Kp; Zp) →p2OKp ,
(183)
and K3(Kp; Zp) is generated as a Zp-module by {[ζ] | ζ ∈µ(Kp)}.
For related work on p-adic regulators/dilogarithms, see Huber–Kings [30] and also Besser–
de Jeu [7, Thm.1.6(2)].
Proof. It is known that K3(Kp; Zp) ∼= H1(Kp, Zp(2)) is a free Zp-module of rank r, cf. [46,
Thm. 7.4] (the torsion-freeness follows from the vanishing of H0(Kp, Fp(2)), which follows
from p > 3). Under the isomorphism between K3 and the Bloch group (and noting that
there is no contribution from K2 = KM
2
to K3(−; Zp)) and using Lemma 3.1, one sees that
the image is contained in p2OKp. But the elements ord(ζ)Dp(ζ) ∈Kp generate the image.
Therefore, this gives a surjective map between two free Zp-modules of the same rank and
therefore the map has a trivial kernel.
□
An example that illustrates this theorem is given in Example 4.3 in Section 4.4.
