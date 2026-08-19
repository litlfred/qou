---
doc_id: gambaudo-ghys-braids-signatures-2005
doc_title: "Bull. Soc. math. France 133 (4), 2005, p. 541–579"
section_id: sec-060-52-the-gordian-space-in-this-section-we-prove-th
section_title: "The gordian space. — In this section, we prove Theorem C according"
section_number: 5.2
pages: 36-38
source_pdf: gambaudo-ghys-braids-signatures-2005.pdf
source_sha256: 647f4c28cab7428d
doc_brief: "Bull. Soc. math. France 133 (4), 2005, p. 541–579 — 62 sections: Introduction; (v1) −v1 =v2 −γ 2(v2) and deﬁne; (α,β ) which is a 2-fold branched"
---
to which it is possible to embed quasi-isometrically copies of Zd in the gordian
metric space ( Knots,d gordian). We begin with a simple observation, already
made in the case ω = −1 in [15].
Proposition 5.3 . — For any root of unity ω and any two knots λ 1,λ 2,
one has ⏐
⏐signω (λ 1) − signω (λ 1)
⏐
⏐ ≤ 2dgordian(λ 1,λ 2).
Proof. — One has to show that if one performs one crossing on a knot th en
any ω -signature changes by at most 2. Start with a knot λ with a generic
projection in the plane and let λ ′be the knot in which one changes one double
point of the projection, changing at that point the up and dow n part. There
is a classical “Seifert algorithm” (that one ﬁnds for instan ce in [12]) constructing
a Seifert surface from a knot projection. Comparing the Seif ert matrices for
the two knots λ,λ ′ associated to these Seifert surfaces, one realizes that the y
only diﬀer by one diagonal term. It follows that the associat ed quadratic forms
agree on a codimension 1 subspace. Therefore, the correspon ding signatures
diﬀer by at most 2.
In order to prove the existence of quasi-isometric embeddin gs of Zd in the
gordian metric space Knots, we shall need the following lemma.
Lemma 5.4 . — For each integer d ≥ 1, one can ﬁnd d elements α 1,...,α d of
some braid groups Bn1,..., Bnd and d roots of unity ω 1,...,ω d such that the
d ×d matrix with entries Sign ω i(α j ) is non-singular.
tome 133 – 2005 – n o 4
BRAIDS AND SIGNATURES 577
Let us ﬁnish the proof of Theorem C assuming this lemma.
Denote byn the sumn1+· · ·+nd and consider the braid group Bn. Grouping
the base points x0
1,...,x 0
n by groups of size n1,n 2,...,n d, we get d embeddings
φ 1,...,φ d of Bn1,..., Bnd in Bn whose images commute. The choice of d
elementsα 1,...,α d deﬁnes a homomorphism
ψ :m = (m1,...,m d) ∈ Zd ↦− →φ 1(α 1)m1 · · ·φ d(α d)md ∈ Bn.
Replacing if necessary all the α i’s by some suitable power, we may assume
that the image of ψ is contained in the pure braid group, which means that
the induced permutation of the n points is trivial. Let β = σ 1· · ·σ n− 1 in Bn,
which induces a cyclic permutation of the n points, so that any braid of the
form ψ (m) ·β has a closure which is a knot ( i.e. which is connected).
We claim that the map
ξ :m ∈ Zd ↦− → ˆψ (m) ·β ∈ Knots
is a quasi-isometric embedding as required by Theorem C. Rec all that we denote
with a hat the closure of a braid.
One distance estimate is obvious. If m1 andm2 are two elements of Zd, the
length of the element ψ (m1)ψ (m2)− 1 of Bn in the classical generating system
is obviously bounded by some constant times the norm of m1 −m2. It follows
that one can pass from the knot ˆψ (m1) ·β to ˆψ (m2) ·β by “undoing” a number
of crossings which is less than a constant times ‖m1 −m2‖.
The other estimate is of course the interesting one. We have t o show that
ifm1 andm2 are far apart in Zd, the same is true for the knots ξ (m1) andξ (m2)
in Knots. We shall use Lemma 5.4 and Proposition 5.3. Observe that hom o-
geneous quasimorphisms on abelian groups are homomorphism s (see for in-
stance [3]). This means that the map
Sign : m ∈ Zd ↦− →
(
Signω 1 (ψ (m)),..., Signω d(ψ (m))
)
∈ Rd
is a homomorphism which, according to Lemma 5.4, has a discre te co-compact
image in Rd. Therefore, there is a constant A> 0 such that for any m1,m 2
max
i=1,...,d
⏐
⏐Signω i(ψ (m1)) − Signω i(ψ (m2))
⏐
⏐ ≥ A‖m1 −m2‖.
Now recall that Sign and sign diﬀer by at most 2 n on Bn, that by Theorem A
the signatures of ψ (m) ·β andψ (m) diﬀer by at most 2 n, and that a diﬀerence
in signatures gives a lower bound for the gordian distance by Proposition 5.3.
Therefore, we have ﬁnally an estimate
A‖m1 −m2‖ −B ≤ dgordian
(
ξ (m1),ξ (m2)
)
≤ C‖m1 −m2‖
for some positive constants A,B,C . This proves Theorem C.
We still have to prove Lemma 5.4. We choose as the braid α i the element
σ 1· · ·σ 2i in B2i+1 fori = 1,...,d . We know that Sign exp(2iπθ )(α i) is a piecewise
BULLETIN DE LA SOCI ´ET´E MATH ´EMATIQUE DE FRANCE
578 GAMBAUDO (J.-M.) & GHYS (E.)
aﬃne function of θ which is constant in the interval [ i/ (2i + 1), (i + 1)/ (2i + 1)].
Choose θ j as a variable in the interval ]( j − 1)/ (2j − 1),j/ (2j + 1)[. In the
matrix Sign exp(2iπθ j )(α i) the entries above the diagonal are constant so that
when one expands the determinant, one realizes that it can be written as
a ·θ 1· · ·θ d +U (θ 1,...,θ d)
where a ⁄= 0 and U is a polynomial of degree ≤ d − 1. It follows that this
determinant cannot vanish identically and Lemma 5.4 is prov ed.
Note that the quasi-isometric embedding that we constructe d is very explicit
and can be made with torus knots.
