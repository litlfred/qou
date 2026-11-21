---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-016-barriers-to-moving-the-contour
section_title: "Barriers to moving the contour"
section_number: null
pages: 15-19
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
doc_brief: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant — Previous work of the author and N."
---
Establishing the volume asymptotics of Conjecture 1 requires replacing our original state integrals
JN(D, µ, β|k) :=
Z
[0,1]E exp N (SN(D, µ|t + β/N) −2πik · t) dt
with shifted ones
eJN(D|k) :=
Z
Γ
exp N (S(D|t) −2πik · t) dt.
This is Step 2 for Zψ
N. The idea is to use Stokes’ Theorem to shift the initial contour [0, 1]E to
some new contour Γ in saddle position for the correct critical point. The obvious problem is that
References
15
X
ζ
ζ + [−1, 1]
ζ/2 + [−1, 1]
Figure 1: The arguments of the dilogarithms in the state integrals JN(D, µ, β|k) are of the form
ζ/N + ti −tj with ti, tj ∈[0, 1]. As N →∞the segments over which they vary approach the
singular region X = (−∞, 0] ∪[1, ∞).
Stokes’ Theorem can move only the interior of the contour, not the boundary.9 This is a serious
issue. As shown in Figure 1 the arguments of the quantum dilogarithms in the action in the original
state integral approach the real axis as N →∞. Unfortunately the real axis is precisely where
the problems are: as N →∞the singularities of e±ϕN become dense in X. Near this region
SN(D, µ) can fail to uniformly converge to S(D), which is related to the fact that the branch
points of the dilogarithm lie there. While the interior of the contour can be moved away the
remaining boundary will still approach the singular region. Understanding why the remaining
boundary terms cancel or do not contribute is a hard analytic problem. There may be subtleties
here that obstruct Conjecture 1 for certain (ρ, µ).
One case where this occurs is already known. When ρ is boundary-parabolic experimental
evidence [McP25a, Remark 6.2] suggests Zψ
N(K, ρ, µ) vanishes unless 2µ ≡−1 (mod NZ). This
suggests there can be nontrivial cancellations in the sum (3.10) and/or indicate other barriers to
moving the contour. Examining these issues may shed light on why it sometimes is possible to
move the contour and prove asymptotic growth.
References
[ADO92]
Yasuhiro Akutsu, Tetsuo Deguchi, and Tomotada Ohtsuki. “Invariants of colored links”.
In: Journal of Knot Theory and its Ramiﬁcations 1.2 (1992), pp. 161–184. issn: 0218-2165.
doi: 10.1142/S0218216592000094.
[AGP23]
Fathi Ben Aribi, François Guéritaud, and Eiichi Piguet-Nakazawa. “Geometric triangu-
lations and the Teichmüller TQFT volume conjecture for twist knots”. In: Quantum
Topol. 14.2 (2023), pp. 285–406. issn: 1663-487X. doi: 10 . 4171 / QT / 178. arXiv:
1903.09480 [math.GT].
[AGW25]
Fathi Ben Aribi, Antonin Guilloux, and Ka Ho Wong. FAMED by computer: proving
the Andersen-Kashaev volume conjecture for 42,000 knots. 2025. arXiv: 2512.17437
[math.GT].
[AK13]
Jørgen Ellegaard Andersen and Rinat Kashaev. A new formulation of the Teichmüller
TQFT. 2013. arXiv: 1305.4291 [math.GT].
[AK14]
Jørgen Ellegaard Andersen and Rinat Kashaev. “A TQFT from quantum Teichmüller
theory”. In: Commun. Math. Phys. 330.3 (2014), pp. 887–934. issn: 0010-3616. doi:
10.1007/s00220-014-2073-2. arXiv: 1109.6295 [math.QA].
[AW24]
Fathi Ben Aribi and Ka Ho Wong. The Andersen-Kashaev volume conjecture for FAMED
geometric triangulations. 2024. arXiv: 2410.10776 [math.GT].
References
16
[BB04]
Stéphane Baseilhac and Riccardo Benedetti. “Quantum hyperbolic invariants of 3-
manifolds with PSL(2,C)-characters”. In: Topology 43.6 (Nov. 2004), pp. 1373–1423.
doi: 10.1016/j.top.2004.02.001. arXiv: math/0306280 [math.GT].
[BWY21]
Francis Bonahon, Helen Wong, and Tian Yang. Asymptotics of quantum invariants of
surface diﬀeomorphisms I: conjecture and algebraic computations. Dec. 23, 2021. arXiv:
2112.12852 [math.GT].
[CKK14]
Jinseok Cho, Hyuk Kim, and Seonhwa Kim. “Optimistic limits of Kashaev invariants
and complex volumes of hyperbolic links”. In: J. Knot Theory Ramiﬁcations 23.9 (2014).
Id/No 1450049, p. 32. issn: 0218-2165. doi: 10.1142/S0218216514500497. arXiv:
1301.6219 [math.GT].
[CZ23]
Qingtao Chen and Shengmao Zhu. On the asymptotic expansions of various quantum
invariants II: the colored Jones polynomial of twist knots at the root of unity e
2π√−1
N+ 1
M and
e
2π√−1
N
. 2023. arXiv: 2307.13670 [math.GT].
[FG09]
V. V. Fock and A. B. Goncharov. “The quantum dilogarithm and representations of
quantum cluster varieties”. In: Invent. Math. 175.2 (2009), pp. 223–286. issn: 0020-9910.
doi: 10.1007/s00222-008-0149-3. arXiv: math/0702397 [math.QA].
[FKV01]
L. D. Faddeev, R. M. Kashaev, and A. Yu. Volkov. “Strongly coupled quantum discrete
Liouville theory. I: Algebraic approach and duality”. In: Commun. Math. Phys. 219.1
(2001), pp. 199–219. issn: 0010-3616. doi: 10.1007/s002200100412. arXiv: hep-
th/0006156.
[GM08]
Sergei Gukov and Hitoshi Murakami. “SL(2, C) Chern-Simons theory and the asymp-
totic behavior of the colored Jones polynomial”. In: Lett. Math. Phys. 86.2-3 (2008),
pp. 79–98. issn: 0377-9017. doi: 10.1007/s11005-008-0282-3. arXiv: math/0608324
[math.GT].
[Guk05]
Sergei Gukov. “Three-dimensional quantum gravity, Chern-Simons theory, and the
A-polynomial”. In: Communications in Mathematical Physics 255.3 (2005), pp. 577–
627. issn: 0010-3616. doi: 10.1007/s00220-005-1312-y. arXiv: hep-th/0306165
[hep-th].
[Ish26]
Tsukasa Ishibashi. Cyclic quantum Teichmüller theory. 2026. arXiv: 2501.02316 [math.GT].
[Kas95]
R. M. Kashaev. “A link invariant from quantum dilogarithm”. In: Modern Physics Letters
A 10.19 (1995), pp. 1409–1418. issn: 0217-7323. doi: 10.1142/S0217732395001526.
arXiv: q-alg/9504020 [math.QA].
[Kas97]
R. M. Kashaev. “The hyperbolic volume of knots from the quantum dilogarithm”.
In: Letters in Mathematical Physics 39.3 (1997), pp. 269–275. issn: 0377-9017. doi:
10.1023/A:1007364912784. arXiv: q-alg/9601025 [math.QA].
[Kas99]
R. M. Kashaev. “Liouville central charge in quantum Teichmüller theory”. In: Matem-
aticheskaya ﬁzika. Problemy kvantovoj teorii polya. Sbornik statej. K 65-letiyu so dnya
rozhdeniya akademika Lyudviga Dmitrievicha Faddeeva. Moskva: Nauka; Moskva: MAIK
Nauka/Interperiodika, 1999, pp. 63–71. isbn: 5-02-002357-4; 5-78-460080-X. arXiv:
hep-th/9811203.
[KC26]
Seonhwa Kim and Philip Choi. Diagram.site: Boundary parabolic representations for
knots. Jan. 2026. url: https://diagram.site.
References
17
[KKY18]
Hyuk Kim, Seonhwa Kim, and Seokbeom Yoon. “Octahedral developing of knot com-
plement I: Pseudo-hyperbolic structure”. In: Geometriae Dedicata 197.1 (Jan. 2018),
pp. 123–172. doi: 10.1007/s10711-018-0323-8. arXiv: 1612.02928 [math.GT].
[KR05]
R. Kashaev and N. Reshetikhin. “Invariants of tangles with ﬂat connections in their
complements”. In: Graphs and Patterns in Mathematics and Theoretical Physics. American
Mathematical Society, 2005, pp. 151–172. doi: 10.1090/pspum/073/2131015. arXiv:
1008.1384 [math.QA].
[Liu+25]
Tianyue Liu, Shuang Ming, Xin Sun, Baojun Wu, and Tian Yang. Turaev-Viro invariant
from the modular double of Uqsl(2; R). 2025. arXiv: 2508.05120 [math.GT].
[McP22]
Calvin McPhail-Snyder. Hyperbolic structures on link complements, octahedral decompo-
sitions, and quantum sl2. 2022. arXiv: 2203.06042v1 [math.GT].
[McP25a]
Calvin McPhail-Snyder. A quantization of the SL2(C) Chern-Simons invariant of tangle
exteriors. 2025. arXiv: 2509.02365v3 [math.QA].
[McP25b]
Calvin McPhail-Snyder. “Octahedral coordinates from the Wirtinger presentation”.
In: Geom. Dedicata 219.4 (May 2025). doi: 10.1007/s10711-025-01012-7. arXiv:
2404.19155 [math.GT].
[MM01]
Hitoshi Murakami and Jun Murakami. “The colored Jones polynomials and the simpli-
cial volume of a knot”. In: Acta Mathematica 186.1 (2001), pp. 85–104. doi: 10.1007/
bf02392716. arXiv: math/9905075 [math.GT].
[MR25]
Calvin McPhail-Snyder and Nicolai Reshetikhin. Cyclic Uξ(sl2)-modules and invariants
of knots with ﬂat sl2 connections in the complement. Sept. 2025. arXiv: 2509.02354v1
[math.QA].
[MY18]
Hitoshi Murakami and Yoshiyuki Yokota. Volume conjecture for knots. Vol. 30. Springer-
Briefs Math. Phys. Singapore: Springer, 2018. isbn: 978-981-13-1149-9; 978-981-13-
1150-5. doi: 10.1007/978-981-13-1150-5.
[Neu04]
Walter D. Neumann. “Extended Bloch group and the Cheeger-Chern-Simons class”. In:
Geometry & Topology 8 (2004), pp. 413–474. issn: 1465-3060. doi: 10.2140/gt.2004.
8.413. arXiv: math/0307092 [math.GT].
[Oht16]
Tomotada Ohtsuki. “On the asymptotic expansion of the Kashaev invariant of the 52
knot”. In: Quantum Topol. 7.4 (2016), pp. 669–735. issn: 1663-487X. doi: 10.4171/QT/
83.
[Oht17]
Tomotada Ohtsuki. “On the asymptotic expansions of the Kashaev invariant of hyper-
bolic knots with seven crossings”. In: Int. J. Math. 28.13 (2017). Id/No 1750096, p. 143.
issn: 0129-167X. doi: 10.1142/S0129167X17500963.
[OT15]
Tomotada Ohtsuki and Toshie Takata. “On the Kashaev invariant and the twisted
Reidemeister torsion of two-bridge knots”. In: Geom. Topol. 19.2 (2015), pp. 853–952.
issn: 1465-3060. doi: 10.2140/gt.2015.19.853.
[OY18]
Tomotada Ohtsuki and Yoshiyuki Yokota. “On the asymptotic expansions of the
Kashaev invariant of the knots with 6 crossings”. In: Math. Proc. Camb. Philos. Soc.
165.2 (2018), pp. 287–339. issn: 0305-0041. doi: 10.1017/S0305004117000494.
[Wit10]
Edward Witten. Analytic Continuation Of Chern-Simons Theory. Jan. 18, 2010. arXiv:
1001.2933 [hep-th].
[Wit89]
Edward Witten. “Quantum ﬁeld theory and the Jones polynomial”. In: Commun. Math.
Phys. 121.3 (1989), pp. 351–399. issn: 0010-3616. doi: 10.1007/BF01217730.
References
18
[Won25]
Ka Ho Wong. Asymptotics aspects of Teichmüller TQFT for generalized FAMED semi-
geometric triangulations. 2025. arXiv: 2512.23198 [math.GT].
[Yok00]
Yoshiyuki Yokota. On the volume conjecture for hyperbolic knots. 2000. arXiv: math/
0009165 [math.QA].
[Zag07]
Don Zagier. “The dilogarithm function”. In: Frontiers in number theory, physics, and
geometry II. On conformal ﬁeld theories, discrete groups and renormalization. Papers from
the meeting, Les Houches, France, March 9–21, 2003. Berlin: Springer, 2007, pp. 3–65.
isbn: 978-3-540-30307-7. doi: 10 . 1007 / 978 - 3 - 540 - 30308 - 4 _ 1. url: https :
//people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-
4_1/fulltext.pdf.
