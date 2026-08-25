---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-006-5-nielsen-thurston-classification-and-the-geomet
section_title: "Nielsen-Thurston classification and the geometry of closed braid complements"
section_number: 5
pages: 16-20
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
closed braid complements
In this section, we describe an application of theorem 1 for genus
one closed surface, namely, essential torus. A description of ess ential
torus in closed braid complements is studied in [BM2],[N] by using
braid foliation machinery. Since an essential torus deeply involves th e
geometry of link complements, we can extract some of geometrical
information of closed braids from theorem 1.
5.1. Nielsen-Thurston classiﬁcation. First of all, we recall the Nielsen-
Thurston classiﬁcation of braids. Nielsen-Thurston theorem stat es that
BRAID ORDERING AND THE GEOMETRY OF CLOSED BRAID 17
an isotopy class of orientation preserving homeomorphism [ f ] of com-
pact oriented surface F , that is, an element of mapping class group
M CG(F ) of F , is classiﬁed into following three types:
(1) periodic: there exists a positive integer m such that f m is iso-
topic to the identity.
(2) reducible: there exist an essential 1-submanifold C of F , which
is invariant under f .
(3) pseudo-Anosov: f is isotopic to a pseudo-Anosov homeomor-
phism.
We do not describe precise deﬁnition of pseudo-Anosov homeomor-
phism, because we do not use it.(see [FLP] for more details about
Nielsen-Thurston theory.) Let Dn be a n-punctured disc. Since braid
group Bn is identiﬁed with the group of boundary-ﬁxing isotopy class
of homeomorphisms of Dn which is identity on ∂Dn, there exist natu-
ral projection π : Bn → M CG(Dn) regarding an element of Bn as an
isotopy class of homeomorphism of Dn whose restriction on ∂Dn are
not necessarily identity. Therefore we can deﬁne the Nielsen-Thur ston
classiﬁcation of braids by taking pull-back of the Nielsen-Thurston c las-
siﬁcation of M CG(Dn). Concretely, the Nielsen-Thurston classiﬁcation
of Bn can be described as following way:
(1) periodic : some powers of β is equal to some powers of Garside
fundamental braid ∆.
(2) pseudo-Anosov : its representing homeomorphism is pseudo-
Anosov.
(3) reducible: its representing homeomorphism is reducible.
Periodic braids are the most simple braids and it is known that
periodic braids are conjugate to some powers of braid ( σ1σ2 · · · σn−1)
or ( σ1σ2 · · · σn−1σ1), which represents rotation of disc.
We remark that the Nielsen-Thurston classiﬁcation of mapping class
groups has very beautiful connection to the geometry of its mapp ing
torus. Let F be a closed surface, ϕ be a homeomorphism of F and Fϕ
be the mapping torus of ϕ . The topology of mapping torus Fϕ only
depends on the isotopy class of ϕ .
It is known that F admit a complete hyperbolic structure if and
only if ϕ is pseudo-Anosov and Fϕ is Seifert-ﬁbered if and only if ϕ
is periodic. Moreover, Fϕ contains an essential torus (hence decom-
posable with respect to geometric decomposition) if and only if ϕ is
reducible. Thus, there exist one-to-one correspondence betwe en the
Nielsen-Thurston classiﬁcation of mapping class group and the geom -
etry of its mapping torus. Hence, in this regard, theorem 2 can be
18 TETSUYA ITO
seen as some generalization of this well-known fact in the knot theor y
settings.
5.2. Proof of Theorem 2. First we investigate non-braided satellite
knots. Recall that a satellite knot K is called braided-satellite if its
complements has essential tori T which is circular foliated under ap-
propriate choice of closed braid representatives of K. In general it
is diﬃcult to handle non-braided satellite knot in braid theory, but
fortunately they do not appear under assumption of theorem 2.
Propotition 4. Let β ∈ Bn be a braid such that K = ˆβ is a non-
braided satellite knot. Then, [β ]D < 3.
Proof. Assume [ β ]D ≥ 3. Then theorem 2 shows all of essential tori
in the complement of K is circular, contradicts to assumption K is
non-braided satellite. □
Remark 4. In [MN], it is proved that if a closure of β is a composite
knot, then [ β ]D < 2. Proposition 4 can be seen some kind of gen-
eralization of this result because composite knots are special type s of
non-braided satellite knots.
To prove theorem 2, We need the following result of Menasco con-
cerning about Torus knots.
Theorem 3 (Menasco([Me1],[Me2])). Torus knots are exchange-reducible.
That is, For every closed braid representative ˆβ of (p, q )-torus knot,
there exists a sequence of closed braids
ˆβ = ˆβ0 → ˆβ1 → · · · → ˆβm
such that ˆβi+1 is obtained by performing exchange move or destabiliza-
tion or isotopy of ˆβi, and βm = (σ1σ2 · · · σp−1)q.
We remark that this Menasco’s theorem is also proved by braid fo-
liation techniques.
Proof of theorem 2. First assume β ∈ Bn and K = ˆβ is a torus knot. If
n is not the braid index of knot K, that is, if K can be represented as
a closure of other braids which have strictly smaller number of stran ds,
then Menasco’s theorem says K admit exchange move or destabiliza-
tion, hence by the proposition 2 (5), we conclude [ β ]D ≤ 1, which
contradicts our assumption [ β ]D ≥ 3. Therefore we can assume that
n is braid index of K. In this case, also Menasco’s theorem says β is
conjugate to braid ( σ1σ2 · · ·σn−1)p for some p, hence β is periodic.
On the other hand, it is known that periodic braids are conjugate to
braids ( σ1σ2 · · · σn−1)s or ( σ1σ2 · · ·σn−1σ1)s for some s , both of which
BRAID ORDERING AND THE GEOMETRY OF CLOSED BRAID 19
represent rotation of disc. Since closure of ( σ1σ2 · · · σn−1σ1)s never
become a knot, it is obvious that closure of periodic braids represen t
torus knots.
Next assume K = ˆβ is a satellite knot. Let T be a essential torus
in the complement of K. Of course there might be some of choice for
such torus, we can take arbitrary one. Our assumption [ β ]D ≥ 3 and
theorem 1 shows T is circular-foliated, so intersection of T with some
ﬁber Hθ gives reducing 1-submanifolds of β as a homeomorphism of
Dn, hence β is reducible. The converse is trivial.
Since both classiﬁcations are exclusive, we conclude that ˆβ is a hy-
perbolic knot if and only if β is pseudo-Anosov.
□
As a corollary, we get an inﬁnite, almost disjoint family of hyper-
bolic knots for each pseudo-Anosov element of mapping class group of
punctured disc. Although it is known that ”almost all” prime knots
are hyperbolic knot, in general it is not so easy to determine given no t
is hyperbolic or not. Especially, most of known family of knots known
to be hyperbolic are deﬁned through knot diagrams such as alterna -
tiveness. We now construct many families of hyperbolic knot throug h
braid-theoretical approach.
Corollary 1. Suppose [f ] ∈ M CG(Dn) be a pseudo-Anosov element
of mapping class group of n-punctured disc and π : Bn → M CG(Dn)
be the natural projection. Let P ([f ]) = { ˆβ | β ∈ π −1([f ]), [β ]D ≥ 3}.
Then P ([f ]) consists of inﬁnite number of distinct hyperbolic knots.
Moreover, let [g] ∈ M CG(Dn) be another pseudo-Anosov element which
is not conjugate to [f ] in M CG(Dn). Then, the intersection of P ([f ])
and P ([g]) are ﬁnite.
Proof of corollary 1. Since P ([f ]) consists of pseudo-Anosov braids with
Dehornoy ﬂoor larger than three, Theorem 2 shows their closures are
all hyperbolic knots. Proposition 2 (6) says braids having suﬃciently
large Dehornoy ﬂoor is a unique closed representative of its closure in
braid index n, therefore P ([f ]) consists of inﬁnite number of distinct
hyperbolic knots and P ([f ]) and P ([g]) have ﬁnite intersection unless
[g] is conjugate to [ f ]. □
Remark 5. Since every hyperbolic knots are represented as a clo-
sure of pseudo-Anosov braids, one might expects our construct ion of
hyperbolic knots produces all hyperbolic knots; That is, for every hy-
perbolic knots, there exists pseudo-Anosov mapping class [ f ] such that
K ∈ P ([f ]). Unfortunately, this too optimistic conjecture is not true.
20 TETSUYA ITO
For example, we can prove ﬁgure-eight knot, the most simple hyper -
bolic knots, do not appear as an element of P ([f ]). More generally, we
can show genus one hyperbolic knots cannot be constructed from our
method. This is a corollary of results of our subsequent paper [I].
Finally, we state a special case of theorem 2 which simpliﬁes the
situation.
Corollary 2. Let p be a prime and β ∈ Bp be a braid whose closure
is a knot and [β ]D ≥ 3. Then ˆβ is a hyperbolic knot if and only if β is
non-periodic.
Proof of corollary 2. Since p is prime and ˆβ is a knot, β is never re-
ducible braid. Assume ˆβ is satellite. Then proposition 4, ˆβ is braided-
satellite, so theorem 2 means β is reducible, which contradicts above.
Thus, under the assumption of corollary, ˆβ is either hyperbolic or torus
knot and β is either periodic or pseudo-Anosov, so theorem 2 estab-
lishes the result. □
Although there is an algorithm to determine Nielsen-Thurston clas-
siﬁcation, it requires exponential times with respect to word length of
braid. On the other hand, since to determine given braids are period ic
or not is easy and it requires only quadratic times, corollary 2 produc es
very many hyperbolic knots explicitly and rapidly. In particular, we
conclude that for prime p, closure of braids β ∈ Bp satisfying [ β ]D ≥ 2
are almost all hyperbolic knots.
