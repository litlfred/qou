---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-001-11-cusp-shapes-and-areas
section_title: "Cusp shapes and areas"
section_number: 1.1
pages: 1-3
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
---
neighborhood of a torus boundary component becomes a cusp, homeomorphic to T 2 × [0, ∞).
Mostow–Prasad rigidity implies that each cross-sectional torus T 2 is endowed with a ﬂat
metric, or cusp shape , that is determined up to similarity by the topology of M . When
M has a single torus boundary component, we may expand a horoba ll neighborhood until
Kalfagianni is supported in part by NSF–FRG grant DMS-04561 55 and by NSF grant DMS–0805942.
Purcell is supported in part by NSF grant DMS-0704359.
May 28, 2018.
1
2 D. FUTER, E. KALF AGIANNI, AND J. PURCELL
it meets itself. This maximal horoball neighborhood completely determines a ﬂat metric on
the torus, and one can measure lengths of curves and area on th e torus using this metric.
We will refer to such a metric as a maximal cusp metric . Similarly, when a 3–manifold
has multiple cusps, a maximal horoball neighborhood is give n by expanding a collection of
horoball neighborhoods until none can be exapanded further while keeping their interiors
disjoint. In the case of multiple cusps, the choice of horoba ll neighborhoods is no longer
unique. However, if we are required to expand the cusp neighb orhoods in a ﬁxed order, this
expansion recipe once again determines a collection of maxi mal cusp metrics.
It is known, due to Nimershiem, that the set of similarity cla sses of tori that can be realized
as cusps of hyperbolic 3–manifolds is dense in the moduli spa ce of 2–tori [47]. However, in
general it is not known how to determine the cusp shape of a man ifold. For simple manifolds,
for example those built of a small number of ideal tetrahedra , or links with a small number
of crossings, Weeks’ computer program SnapPea will determi ne shapes of cusps and maximal
cusp metrics [58]. For other, larger classes of 3–manifolds , some bounds on cusp shape have
been obtained. Aitchison, Lumsden, and Rubinstein found cu sp shapes of certain alternating
links, but the metrics they used were singular [5]. For non-s ingular hyperbolic metrics, Adams
et al. found upper bounds on the cusp area of knots, in terms of the cr ossing number of
a diagram [3]. Purcell found that for “highly twisted” knots , the lengths of shortest arcs
on a maximal cusp metric are bounded above and below in terms o f the twist number of a
diagram [49]. These results were obtained using cusp estima tes on a class of links called fully
augmented links, whose cusp shapes and lengths of slopes on m aximal cusp metrics were also
worked out by Purcell [49] and Futer and Purcell [28].
In this paper, we prove explicit, readily applicable bounds on cusp shapes and maximal
cusp metrics of punctured torus bundles and 4–punctured sph ere bundles, as well as of 2–
bridge knot complements. These manifolds have a natural ide al triangulation, ﬁrst discovered
for punctured torus bundles by Floyd and Hatcher [24], and la ter studied by many others
[6, 7, 30, 38]. One feature that makes these 3–manifolds part icularly attractive is that their
geometry can be described in terms of the combinatorics of th e Farey tessellation of H2.
Hence, we refer to these manifolds as Farey manifolds.
To state an example of our results in this direction, let M be a hyperbolic once–punctured
torus bundle. The monodromy of M can be thought of as a conjugacy class in SL2(Z). As
such, it has a (unique up to cyclic permutation of factors) pr esentation of the form
±
[
1 a1
0 1
][
1 0
b1 1
]
· · · · · · · · ·
[
1 as
0 1
][
1 0
bs 1
]
,
where ai, bi are positive integers. The integer s is called the length of the monodromy.
Theorem 4.1. LetM be a punctured–torus bundle with monodromy of length s. Let C be a
maximal horoball neighborhood about the cusp of M . Then
16
√
3
147 s ≤ area(∂C ) < 2
√
3v8
v3
s,
where v3 = 1.0149... is the volume of a regular ideal tetrahedron and v8 = 3.6638... is the
volume of a regular ideal octahedron.
Furthermore, if γ is a non-trivial simple closed curve on ∂C (that is, any simple closed
curve that is transverse to the ﬁbers), then its length ℓ(γ) satisﬁes
ℓ(γ) ≥ 4
√
6
147 s.
CUSP AREAS OF F AREY MANIFOLDS 3
The proof of Theorem 4.1 contains two main steps. First, we de rive an estimate for the
size of horoballs in the universal cover of punctured torus b undles (see Proposition 3.6).
Then, we pack the cusp torus with the shadows of these horobal ls.
Our estimate on horoball size should be compared with Jørgen sen’s work on quasifuchsian
punctured torus groups, which appears in a well–known but un ﬁnished manuscript [34]. A
careful exposition of Jørgensen’s work was given by Akiyoshi, Sakuma, Wada, and Yamashita
[8]. Jørgensen’s results can be applied in our setting to sho w that the universal cover of a
punctured torus bundle contains a number of maximal horobal ls whose size is bounded from
below (see [34, Lemma 4.3] and [8, Lemma 8.1.1]). Jørgensen c onjectured the existence of
a much better lower bound for this horoball size; and indeed, our Proposition 3.6 improves
Jørgensen’s lower bound by a factor of more than 10. This impr ovement is very important
in our setting, since a 10–fold improvement in horoball size yields a 100–fold improvement
in the cusp area estimate. See the end of Section 3.3 for a more detailed discussion.
