---
doc_id: arxiv-math-0611181v2
doc_title: "Proof of the volume conjecture for Whitehead chains"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0611181v2.pdf
source_sha256: 6931e3ebca584de9
doc_brief: "Proof of the volume conjecture for Whitehead chains — We prove the volume conjecture for an inﬁnite family of links called White- head chains that generalizes both the Whitehead link and the"
---
The volume conjecture relates the colored Jones polynomials of a kn ot to the
simplicial volume of its complement. More precisely, let us denote the n ormal-
ized N -colored Jones polynomial of a knot K by JN (K) and let Vol( K) be v3
times the simplicial volume (Gromov norm) of S3 −K, where v3 is the volume
of the hyperbolic regular ideal tetrahedron. The volume conjectu re can now be
stated as follows:
Conjecture 1. (Volume conjecture) [7]
For any knot K we have:
lim
N →∞
2π
N log |JN (K)(e
2πi
N )| = Vol(K)
So far the conjecture has been proven for only the ﬁgure eight kn ot, torus knots,
Whitehead doubles of certain torus knots and connected sums of t hese knots,
[6], [4], [11].
It is well known that the volume conjecture is false for many splittab le links
so it is unclear how to extend the volume conjecture to links. On the o ther hand,
the volume conjecture has been shown to hold for the Whitehead link [11] and
the Borromean rings [1]. In this paper, we introduce the family of Whit ehead
chains generalizing both the Whitehead link and the Borromean rings a nd we
settle the volume conjecture for this family.
The Whitehead chains are deﬁned in terms of the tangles Belt, Clasp a nd
Twist depicted in ﬁgure 1 on the next page.
1
Figure 1: The tangles Belt, Twist and Clasp
Deﬁnition 1. Leta,b,c,d be integers such that b ≥ 1 and c,d ≥ 0. Deﬁne the
Whitehead chain Wa,b,c,d to be the closure of the composition of a tangles of type
Twist (or a mirror images of type Twist when a <0), b tangles of type Belt, c
tangles of type Clasp and d mirror images of tangles of type Clasp.
The tangles Belt, Twist, Clasp and their mirror images commute, so th e order
of composition is immaterial. Therefore the Whitehead chains are well deﬁned.
In the notation of the previous deﬁnition the Whitehead link is W0, 1, 1, 0 and the
Borromean rings are W0, 1, 1, 1.
Our main theorem is the following asymptotic expansion for the colore d
Jones polynomial of a Whitehead chain. As usual x ∼ y means that the quo-
tient converges to 1.
Main theorem. Leta,b,c,d be integers, such that b ≥ 1 and c,d ≥ 0.
JN (Wa,b,c,d )(e
2πi
N ) ∼ exp
( 1
2π {(Vol(Wa,b,c,d ) +iCS)N + D log(N ) + E}
)
- The value of CS is −4a+c−d
8 2π2 if c +d = 1 and −4a−7c+7d
8 2π2 otherwise.
- If b = 1 we have D = 3π and E can be expressed explicitly as an integral,
see the proof of lemma 4.
- If b ≥ 2 the expansion is only valid for odd N andJ2M (Wa,b,c,d )(e
2πi
2M ) = 0 .
For odd N we ﬁnd D = 2πb and E = 2π(c +d) log 2 + 4a+3c−3d
4 2π2i.
By taking absolute values and restricting ourselves to the leading te rm we see
that the volume conjecture holds true for b = 1, while it is false for b ≥ 2. In
the latter case the volume conjecture is true when we restrict to o dd values
2
of N . This phenomenon might have something to do with the fact that the
complement of the Whitehead chain is hyperbolic when b = 1, while the torus
decomposition contains a Seifert-ﬁbered piece when b ≥ 2.
According to the complexiﬁed volume conjecture proposed in [8] the value
of CS is equal to 2 π2 times the Chern-Simons invariant. For a = 0 this is indeed
the case because the Chern-Simons invariant is additive with respec t to belted
sum and its value on the Whitehead link and its mirror image is ± 1
8 , [9].
In [3] the number D in the above asymptotic expansion is conjecture d to be
the number of prime factors of a knot. In [2] a diﬀerent interpret ation is given in
terms of the knot complement. In the same paper it is also conjectu red that the
number E is determined by the Ray-Singer torsion of the complement twisted
by the holonomy representation. We hope to investigate these con jectures for
the Whitehead chains in a subsequent publication.
The main theorem shows that the original volume conjecture may fa il even
for non-splittable links, but adds credibility to the following weaker ve rsion of
the volume conjecture for links:
Conjecture 2. For any non-splittable link L we have:
lim sup
N →∞
2π
N log |JN (L)(e
2πi
N )| = Vol(L)
