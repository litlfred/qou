---
doc_id: s00526-018-1443-6
doc_title: "On the analyticity of critical points of the Möbius energy"
section_id: sec-002-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: s00526-018-1443-6.pdf
source_sha256: 34f3cd94e3b2d9d7
toc_source: outline
doc_brief: "On the analyticity of critical points of the Möbius energy — We prove that smooth critical points of the Möbius energy E parametrized by arc-length are analytic."
---
Knots are part of our everyday life, while tying our shoes, in art works or on a ﬁsherwoman’s
boat. They have always played an important role in craft and trades, culture and arts. During
the last two centuries, knot theory has arisen to a research topic of great interest and it has
had a sustainable impact on mathematics, especially on the development of topology in the
nineteenth century [41]. Currently, the theory of knots appears in several branches of mathe-
matics, such as calculus of variations, nonlinear and geometric analysis, and topology as well
as in modern quantum physics, see for example in Kauffman’s essay [23], and biochemistry
(protein molecules, e.g. [25], or DNA, e.g. [7,15]).
In mathematical terms, a knot can be described as a closed curve γ : R/Z →R3 which
embeds a circle R/Z into R3 continuously. Two knots belong to the same knot class if there
exists a deformation from one knot to the other called ambient isotopy, which avoids “cutting
and gluing” and any self-intersection. In order to determine a representative with a particular
“nice” shape within a given knot class, so-called knot energies appeared three decades ago.
A knot is considered as “nice” if it is as smooth, symmetric, and as barely entangled as
possible, which may be reached by modeling a form of self-avoidance and subsequently
ﬁnding a minimizer of the knot energy.
Such a knot energy was ﬁrst constructed by Fukuhara, who focused on polygonal knots
[13]. Later, O’Hara investigated several potential energies of knots in [31,32]. Amongst others
he deﬁned for any closed, Lipschitz continuous and regular curve γ : R/Z →Rn for any
n ∈N, n ≥2, the energy
E(γ ) :=

(R/Z)2

1
|γ (u) −γ (v)|2 −
1
D(γ (u), γ (v))2

| ˙γ (u)|| ˙γ (v)|dudv
which is called Möbius energy due to its invariance under Möbius transformations proved
in [10, Theorem 2.1]. Here, D(γ (x), γ (y)) denotes the intrinsic distance of γ (x) and γ (y)
along the curve, i.e.
D(γ (x), γ (y)) := min{L(γ |[x,y]), L(γ ) −L(γ |[x,y])}
for all |x −y| ≤1
2 where L(γ ) :=
 1
0 | ˙γ (t)|dt is the length of γ . It is easy to see that all
values of E are non-negative, since the intrinsic distance of two points of the curve is always
greater than the Euclidean distance. So E is indeed bounded from below. Furthermore, E is
invariant under reparametrization of the curve due to the factor |γ ′(u)||γ ′(v)|. O’Hara in
[33, Theorem 1.1] and Freedman et al. in [10, Lemma 1.2] proved that E is self-repulsive.
However, the Möbius energy is not tight due to [33, Theorem 3.1]; which means that E does
not blow up for a sequence of small knots that pulls tight. Let us mention that Ishizeki and
Nagasawa decomposed the Möbius energy into three parts each of which is again Möbius
invariant [20,21]. One of these parts is equal to the cosine formula of Doyle and Schramm
[2]. For further information about the Möbius energy, other knot energies and their properties
we refer to [34,39].
Now let for the rest of this article γ : R/Z →Rn, n ∈N, be a simple, closed curve
parametrized by arc-length if not stated differently. Here, “simple” means that γ is injective
on [0, 1). It was shown in [4] that such curves have ﬁnite Möbius energy if and only if they
belong to the fractional Sobolev space H
3
2 (R/Z, Rn).
He proved in [17, Chapter 5] based on Freedman et al. [10, Theorem 5.4] that any local
minimizer γ of E with respect to the L∞-topology and n = 3 is smooth in the sense that
γ ∈C∞(R/Z, R3). Reiter generalized this result to a larger class of O’Hara’s knot energy
On the analyticity of critical points of the Möbius energy
Page 3 of 28
16
in [38] and furnished a proof that any critical point γ of E in H2(R/Z, Rn) is smooth [38,
Theorem 1.2]. The latest result that will be useful for our further investigations comes from
Blatt, Reiter and Schikorra:
Theorem 1.1 ([6]) Any critical point γ of E with γ ∈H
3
2 (R/Z, Rn) parametrized by arc-
length, i.e. every γ ∈H
3
2 (R/Z, Rn) that satisﬁes
δE(γ ; h) :=
lim
τ→0,τ̸ =0
E(γ + τh) −E(γ )
τ
= 0
∀h ∈C∞(R/Z, Rn),
belongs to C∞(R/Z, Rn).
These results of course raise the question, whether a critical point of the Möbius energy in
H
3
2 (R/Z, Rn) is not only smooth, but also analytic. The main result of this article answers
this question:
Theorem 1.2 Let γ : R/Z →Rn be a closed, simple, and by arc-length parametrized curve
in H
3
2 (R/Z, Rn). If γ is a critical point of the Möbius energy E, then γ is analytic.
Together Theorem 1.1 and the characterization of the energy spaces in [4] immediately
gives the following corollary.
Corollary 1.3 Let γ : R/Z →Rn be a closed, simple, and by arc-length parametrized curve
of ﬁnite Möbius energy. If γ is a critical point of the Möbius energy E, then γ is analytic.
There exist many results on the analyticity of solutions of classical analytic nonlinear
elliptic partial differential equations. In 1904, Bernstein showed the analyticity of a solution
of class C3 to a nonlinear analytic elliptic equation of two independent variables in [3] by
estimating higher order derivatives of solutions. Gevrey in [14] and Radó in [36] showed
Bernstein’s result by a similar strategy later. Also by the method of estimating higher order
derivatives of solutions, Morrey and Nirenberg generalized the result to linear elliptic systems
in [28] in 1957 and moreover, Friedman to nonlinear elliptic systems of partial differential
equationsin[12]in1958.AnothermethodgoesbacktoLewyin1929,whoprovedBernstein’s
theorem by extension to the complex domain in [26]. By using this alternative method, Hopf
in [18], Petrovski in [35] and Morrey [29,30] generalized bit by bit Bernstein’s theorem up
to the analyticity of solutions of analytic nonlinear elliptic systems of partial differential
equations as well. New ideas for proving the analyticity of solutions of analytic nonlinear
elliptic equations were developed by Kato in [22] and Hashimoto in [16].
To best of the authors knowledge, the result above is the ﬁrst analyticity result in the
context of non-local differential equations.
