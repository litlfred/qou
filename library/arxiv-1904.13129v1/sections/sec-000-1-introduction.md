---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
doc_brief: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity — W e prove the analyticity of smooth critical points for O’Har a’s knot energies E α,p , with p = 1"
---
Knots have always played an important role in arts and crafts , commerce and
trade, as well as in our everyday life. Therefore they natura lly became a topic of
interest for mathematicians. During the 19th century the st udy of knots strongly in-
ﬂuenced the development of topology [ TvdG96]. Today the theory of knots appears
in several branches of mathematics such as in calculus of var iations, geometric anal-
ysis, topology as well as in applications to modern quantum p hysics (e.g. [ Kau05])
and biochemistry (e.g. protein molecules [ KS98] or DNA [ CKS98, GM99]).
A knot in mathematical terms is a Jordan curve in the three-di mensional Eu-
clidean space (i.e. a continuous embedding of the circle R/Z into R3). We say that
two given knots belong to the same knot class if one knot can be deformed into
the other without any ‘cuttings and gluings’ nor any self-in tersections. Within this
context, the following two questions arise: Is it possible t o determine ‘nicely’ shaped
representatives of each knot class? And if so, how ‘nice’ are they?
The ﬁrst question was originally addressed by Fukuhara [ Fuk88] in the context of
polygonal knots. In order to detect optimal shapes of a polyg onal knot, an energy
modelling a form of self-avoidance on the space of polygonal knots was introduced—
from which optimal shapes can be identiﬁed as energy minimiz ers. Subsequently,
O’Hara [O’H91, O’H92] extended Fukuhara’s approach to geometric knots. For any
Jordan curve γ : R/Z → R3, he introduced the potential energies
E α,p(γ) =
∫∫
(R/Z)2
( 1
|γ(x) −γ(y)|α − 1
D(γ(x),γ (y))α
) p
| ˙γ(x)|| ˙γ(y)|dxdy. (1.1)
Date: May 1, 2019.
2010 Mathematics Subject Classiﬁcation. 35B65, 57M25.
Key words and phrases. Analyticity, knot energy, O’Hara’s knot energies, method of majorants,
fractional Leibniz rule.
The author acknowledges support by the Austrian Science Fun d (FWF), Grant P 29487.
1
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 2
Here the quantity D(γ(x),γ (y)) denotes the intrinsic distance between the points
γ(x) and γ(y) along the curve, i.e. for |x −y| ≤ 1
2 we have
D(γ(x),γ (y)) = min {L(γ|[x,y]), L(γ) − L(γ|[x,y])},
where L(γ) =
∫ 1
0 | ˙γ(t)|dt denotes the length of the curve γ. All values of E α,p
are non-negative due to the fact that the intrinsic distance between two points of
the curve is always greater than the Euclidean distance. The factor |γ′(x)||γ′(y)|
guarantees the invariance of E α,p under reparametrization of the curve. In addition,
E 2 = E 2,1 is called Möbius energy since it is invariant under Möbius tr ansformations
(cf. [ FHW94, Theor. 2.1]). For p ≥ 1 and 0 < αp <2p + 1 the energies E α,p are
globally minimized by circles, whereas for αp ≥ 2p + 1 their values become inﬁnite
for every closed regular curve (cf. [ ACF+03, Corol. 3]).
To distinguish between knot classes, it is desirable for a kn ot energy to be self-
repulsive (i.e. to penalize self-intersections) and tight (i.e. to blow up on a sequence
of small knots that pull tight). O’Hara showed that the knot e nergies E α,p are
indeed self-repulsive for the cases p ≥ 2
α , 0< α≤ 2 and 1
α−2 > p≥ 2
α , 2< α≤ 4
(cf. [ O’H94, Theor. 1.1]) and tight if and only if αp >2 (cf. [ O’H92, Theor. 3.1]).
Moreover, [ O’H94, Theor. 3.2] showed that for αp > 2 there exist minimizers of
the energies within every knot class among all curves with ﬁx ed length. In case of
the Möbius energy, we also have self-repulsiveness but not t ightness (cf. [ O’H94,
Theor. 3.1]) and we only know that there exist minimizers in p rime knot classes
(cf. [FHW94, Theor. 4.3]). We see that due to the well-deﬁnedness and exi stence of
minimizers of a certain range of O’Hara’s energies E α,p, this approach for answering
our ﬁrst question looks promising.
In the following we want to focus on the second question by det ermining the
regularity properties of minimizers of the knot energies. F or that reason we restrict
ourselves to examining O’Hara’s energies E α = E α,1 for 2 ≤ α < 3 as they are
well-deﬁned in a knot-theoretic sense and have a non-degene rate ﬁrst variation (in
contrast to the p> 1 case). For the Möbius energy, one of the ﬁrst regularity resu lts
goes back to He [ He00, Chap. 5] who states, based on Freedman, He and Wang’s
work [ FHW94, Theor. 5.4], that any local minimizer γ of E 2 with respect to the
L∞-topology belongs to C∞(R/Z, R3). Reiter [ Rei12] generalized this result to the
class of O’Hara’s knot energies E α for 2 ≤ α <3 and n ≥ 3 by showing that any
critical point γ of E α in the class H α(R/Z, Rn) with γ′′ ∈L2(R/Z, Rn) is smooth.
A subsequent improvement on the energy space conditions fur nishes the following
C∞-result.
Theorem 1.1 (Blatt and Reiter [ BR13]). Let γ : R/Z → Rn be a simple closed
Lipschitz-continuous arc-length parametrized curve with γ ∈ H
α +1
2 ,2(R/Z, Rn) for
any 2<α< 3. If γ is a critical point of E α +λL, i.e.
δE α(γ;h) +λ
∫
R/Z
⟨˙γ, ˙h⟩dx = 0 for all h ∈H
α +1
2 ,2(R/Z, Rn),
then γ belongs to C∞(R/Z, Rn).
An important characterization of curves with ﬁnite O’Hara e nergy goes back to
Blatt [Bla12] who showed that curves γ have ﬁnite energy E α(γ)< ∞ if and only if
they belong to the fractional Sobolev space H
α +1
2 ,2(R/Z, Rn). This result, combined
with Theorem 1.1, raises the question whether critical points of O’Hara’s en ergies
E α of ﬁnite energy are not only smooth but also analytic. For the Möbius energy
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 3
E 2 this question was solved in the aﬃrmative by [ BV19]. One might conjecture
that it is possible to transfer this result to the energy clas ses E α for 2 < α <3.
Unlike the Möbius energy case, the ﬁrst variation of E α for 2<α< 3 leads to the
appearance of a fractional derivative of the product of two f unctions. The latter
is subsequently analyzed via a new fractional Leibniz rule i nstead of the bilinear
Hilbert transform, which was used in the Möbius energy case.
The main result of this article conﬁrms the above analyticit y conjecture, namely:
Theorem 1.2. Letγ : R/Z → Rn be a closed simple arc-length parametrized curve
in C∞(R/Z, Rn). If γ is a critical point of O’Hara’s energy E α, 2<α< 3, with a
length term L, i.e. E α +λL, then the curve γ is analytic.
This theorem, together with the characterization of the ene rgy spaces in [ Bla12]
and Theorem 1.1, implies the following:
Corollary 1.3. Letγ : R/Z → Rn be a closed simple arc-length parametrized curve
with E α(γ)< ∞ for 2<α< 3. If γ is a critical point of E α +λL, then the curve
γ is analytic.
Note that we study critical points of O’Hara’s energy E α subject to a Lagrange
multiplier length term since E α for 2 < α <3 is not scale-invariant in contrast to
the Möbius energy case.
Exposé of the present work. The main goal of this article is to give a rigorous
proof of Theorem 1.2. We adapt the methods from the Möbius energy case in
[BV19] to generate a proof which is as elementary as possible. For t he convenience
of the reader we will provide detailed proofs in this article on the one hand to
emphasize the diﬀerences to [ BV19] and, on the other hand, to make the article
comprehensible without the need for a detailed reading of [ BV19].
In Section 2 we recall some basic deﬁnitions and properties of fractiona l Sobolev
spaces and Fourier series. We also characterize analytic fu nctions and state an or-
dinary diﬀerential equation (ODE)-version of the theorem o f Cauchy-Kovalevskaya.
