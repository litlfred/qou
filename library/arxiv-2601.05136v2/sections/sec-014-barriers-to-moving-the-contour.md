---
doc_id: arxiv-2601.05136v2
doc_title: "N(K,ρ,µ ) of a knotK, a representationρ: π1(S3\K)→ SL2(C), andalogarithm µofameridianeigenvalueof ρ. Itcanbeinterpretedasa geometrictwistoftheKashaevinvariantorasaquantizationofthe"
section_id: sec-014-barriers-to-moving-the-contour
section_title: "Barriers to moving the contour"
section_number: null
pages: 15-19
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
doc_brief: "Stateintegralsforthequantized SL2(C)Chern-Simonsinvariant CalvinMcPhail-Snyder DepartmentofMathematics,DukeUniversity calvin@sl2.site — Previous work of the author and N."
---
EstablishingthevolumeasymptoticsofConjecture1requiresreplacingouroriginalstateintegrals
JN(D,µ,β|k) :=
Z
[0,1]E
expN (SN(D,µ|t +β/N)− 2πik·t) dt
withshiftedones
eJN(D|k) :=
Z
Γ
expN (S(D|t)− 2πik·t) dt.
This is Step 2 forZψ
N. The idea is to use Stokes’ Theorem to shift the initial contour[0, 1]E to
somenewcontour Γinsaddlepositionforthecorrectcriticalpoint. Theobviousproblemisthat
References 15
X
ζ
ζ + [−1, 1]
ζ/2 + [−1, 1]
Figure1: Theargumentsofthedilogarithmsinthestateintegrals JN(D,µ,β|k)areoftheform
ζ/N +ti−tj withti,tj∈ [0, 1]. AsN→∞ thesegmentsoverwhichtheyvaryapproachthe
singularregion X = (−∞, 0]∪ [1,∞).
Stokes’Theoremcanmoveonlytheinteriorofthecontour,nottheboundary. 9 Thisisaserious
issue. AsshowninFigure1theargumentsofthequantumdilogarithmsintheactionintheoriginal
state integral approach the real axis asN→∞ . Unfortunately the real axis is precisely where
the problems are: asN →∞ the singularities ofe±ϕN become dense inX. Near this region
SN(D,µ ) can fail to uniformly converge toS(D), which is related to the fact that the branch
points of the dilogarithm lie there. While the interior of the contour can be moved away the
remaining boundary will still approach the singular region. Understanding why the remaining
boundarytermscancelordonotcontributeisahardanalyticproblem. Theremaybesubtleties
herethatobstructConjecture1forcertain (ρ,µ ).
One case where this occurs is already known. Whenρis boundary-parabolic experimental
evidence[McP25a,Remark6.2]suggests Zψ
N(K,ρ,µ )vanishesunless 2µ≡− 1 (mod N Z). This
suggeststherecanbenontrivialcancellationsinthesum (3.10)and/orindicateotherbarriersto
moving the contour. Examining these issues may shed light on why it sometimesispossible to
movethecontourandproveasymptoticgrowth.
References
[ADO92] YasuhiroAkutsu,TetsuoDeguchi,andTomotadaOhtsuki.“Invariantsofcoloredlinks”.
In:JournalofKnotTheoryanditsRamiﬁcations 1.2(1992),pp.161–184. issn:0218-2165.
doi: 10.1142/S0218216592000094.
[AGP23] FathiBenAribi,FrançoisGuéritaud,andEiichiPiguet-Nakazawa.“Geometrictriangu-
lationsandtheTeichmüllerTQFTvolumeconjecturefortwistknots”.In: Quantum
Topol. 14.2 (2023), pp. 285–406.issn: 1663-487X.doi: 10 . 4171 / QT / 178. arXiv:
1903.09480 [math.GT].
[AGW25] Fathi Ben Aribi, Antonin Guilloux, and Ka Ho Wong.FAMED by computer: proving
the Andersen-Kashaev volume conjecture for 42,000 knots. 2025. arXiv:2512 . 17437
[math.GT].
[AK13] Jørgen Ellegaard Andersen and Rinat Kashaev.A new formulation of the Teichmüller
TQFT.2013.arXiv: 1305.4291 [math.GT].
[AK14] JørgenEllegaardAndersenandRinatKashaev.“ATQFTfromquantumTeichmüller
theory”. In:Commun. Math. Phys.330.3 (2014), pp. 887–934.issn: 0010-3616.doi:
10.1007/s00220-014-2073-2.arXiv: 1109.6295 [math.QA].
[AW24] FathiBenAribiandKaHoWong. The Andersen-Kashaev volume conjecture for FAMED
geometric triangulations.2024.arXiv: 2410.10776 [math.GT].
References 16
[BB04] Stéphane Baseilhac and Riccardo Benedetti. “Quantum hyperbolic invariants of 3-
manifolds with PSL(2,C)-characters”. In:Topology43.6 (Nov. 2004), pp. 1373–1423.
doi: 10.1016/j.top.2004.02.001.arXiv: math/0306280 [math.GT].
[BWY21] FrancisBonahon,HelenWong,andTianYang. Asymptotics of quantum invariants of
surface diﬀeomorphisms I: conjecture and algebraic computations.Dec.23,2021.arXiv:
2112.12852 [math.GT].
[CKK14] JinseokCho,HyukKim,andSeonhwaKim.“OptimisticlimitsofKashaevinvariants
andcomplexvolumesofhyperboliclinks”.In: J. Knot Theory Ramiﬁcations23.9(2014).
Id/No 1450049, p. 32.issn: 0218-2165.doi: 10.1142/S0218216514500497 . arXiv:
1301.6219 [math.GT].
[CZ23] QingtaoChenandShengmaoZhu. On the asymptotic expansions of various quantum
invariants II: the colored Jones polynomial of twist knots at the root of unitye
2π√−1
N + 1
M and
e
2π√−1
N .2023.arXiv: 2307.13670 [math.GT].
[FG09] V. V. Fock and A. B. Goncharov. “The quantum dilogarithm and representations of
quantumclustervarieties”.In: Invent.Math. 175.2(2009),pp.223–286. issn:0020-9910.
doi: 10.1007/s00222-008-0149-3.arXiv: math/0702397 [math.QA].
[FKV01] L.D.Faddeev,R.M.Kashaev,andA.Yu.Volkov.“Stronglycoupledquantumdiscrete
Liouvilletheory.I:Algebraicapproachandduality”.In: Commun. Math. Phys.219.1
(2001), pp. 199–219.issn: 0010-3616.doi: 10 . 1007 / s002200100412. arXiv: hep -
th/0006156.
[GM08] SergeiGukovandHitoshiMurakami.“ SL(2, C)Chern-Simonstheoryandtheasymp-
totic behavior of the colored Jones polynomial”. In:Lett. Math. Phys.86.2-3 (2008),
pp.79–98. issn:0377-9017. doi: 10.1007/s11005-008-0282-3.arXiv: math/0608324
[math.GT].
[Guk05] SergeiGukov.“Three-dimensionalquantumgravity,Chern-Simonstheory,andthe
A-polynomial”. In:Communications in Mathematical Physics255.3 (2005), pp. 577–
627.issn: 0010-3616.doi: 10.1007/s00220-005-1312-y . arXiv:hep-th/0306165
[hep-th].
[Ish26] TsukasaIshibashi.CyclicquantumTeichmüllertheory .2026.arXiv: 2501.02316 [math.GT].
[Kas95] R.M.Kashaev.“Alinkinvariantfromquantumdilogarithm”.In: ModernPhysicsLetters
A10.19(1995),pp.1409–1418. issn:0217-7323. doi: 10.1142/S0217732395001526.
arXiv: q-alg/9504020 [math.QA].
[Kas97] R. M. Kashaev. “The hyperbolic volume of knots from the quantum dilogarithm”.
In: Letters in Mathematical Physics39.3 (1997), pp. 269–275.issn: 0377-9017.doi:
10.1023/A:1007364912784.arXiv: q-alg/9601025 [math.QA].
[Kas99] R.M.Kashaev.“LiouvillecentralchargeinquantumTeichmüllertheory”.In: Matem-
aticheskaya ﬁzika. Problemy kvantovoj teorii polya. Sbornik statej. K 65-letiyu so dnya
rozhdeniyaakademikaLyudvigaDmitrievichaFaddeeva .Moskva:Nauka;Moskva:MAIK
Nauka/Interperiodika,1999,pp.63–71. isbn:5-02-002357-4;5-78-460080-X.arXiv:
hep-th/9811203.
[KC26] Seonhwa Kim and Philip Choi.Diagram.site: Boundary parabolic representations for
knots.Jan.2026. url: https://diagram.site.
References 17
[KKY18] HyukKim,SeonhwaKim,andSeokbeomYoon.“Octahedraldevelopingofknotcom-
plement I: Pseudo-hyperbolic structure”. In:Geometriae Dedicata197.1 (Jan. 2018),
pp.123–172. doi: 10.1007/s10711-018-0323-8.arXiv: 1612.02928 [math.GT].
[KR05] R.KashaevandN.Reshetikhin.“Invariantsoftangleswithﬂatconnectionsintheir
complements”.In: GraphsandPatternsinMathematicsandTheoreticalPhysics .American
MathematicalSociety,2005,pp.151–172. doi: 10.1090/pspum/073/2131015.arXiv:
1008.1384 [math.QA].
[Liu+25] TianyueLiu,ShuangMing,XinSun,BaojunWu,andTianYang. Turaev-Viro invariant
from the modular double ofUqsl(2; R).2025.arXiv: 2508.05120 [math.GT].
[McP22] CalvinMcPhail-Snyder. Hyperbolic structures on link complements, octahedral decompo-
sitions, and quantumsl2.2022.arXiv: 2203.06042v1 [math.GT].
[McP25a] CalvinMcPhail-Snyder. A quantization of theSL2(C)Chern-Simons invariant of tangle
exteriors.2025.arXiv: 2509.02365v3 [math.QA].
[McP25b] CalvinMcPhail-Snyder. “Octahedralcoordinatesfrom theWirtinger presentation”.
In: Geom. Dedicata219.4 (May 2025).doi: 10.1007/s10711- 025- 01012- 7. arXiv:
2404.19155 [math.GT].
[MM01] HitoshiMurakamiandJunMurakami.“ThecoloredJonespolynomialsandthesimpli-
cialvolumeofaknot”.In: Acta Mathematica186.1(2001),pp.85–104. doi: 10.1007/
bf02392716.arXiv: math/9905075 [math.GT].
[MR25] CalvinMcPhail-SnyderandNicolaiReshetikhin. CyclicUξ(sl2)-modulesandinvariants
of knots with ﬂatsl2 connections in the complement.Sept.2025.arXiv: 2509.02354v1
[math.QA].
[MY18] HitoshiMurakamiandYoshiyukiYokota. Volume conjecture for knots.Vol.30.Springer-
BriefsMath.Phys.Singapore:Springer,2018. isbn:978-981-13-1149-9;978-981-13-
1150-5.doi: 10.1007/978-981-13-1150-5.
[Neu04] WalterD.Neumann.“ExtendedBlochgroupandtheCheeger-Chern-Simonsclass”.In:
Geometry & Topology8(2004),pp.413–474. issn:1465-3060. doi: 10.2140/gt.2004.
8.413.arXiv: math/0307092 [math.GT].
[Oht16] TomotadaOhtsuki.“OntheasymptoticexpansionoftheKashaevinvariantofthe 52
knot”.In: Quantum Topol.7.4(2016),pp.669–735. issn:1663-487X. doi: 10.4171/QT/
83.
[Oht17] TomotadaOhtsuki.“OntheasymptoticexpansionsoftheKashaevinvariantofhyper-
bolicknotswithsevencrossings”.In: Int. J. Math.28.13(2017).Id/No1750096,p.143.
issn:0129-167X. doi: 10.1142/S0129167X17500963.
[OT15] Tomotada Ohtsuki and Toshie Takata. “On the Kashaev invariant and the twisted
Reidemeistertorsionoftwo-bridgeknots”.In: Geom. Topol.19.2(2015),pp.853–952.
issn:1465-3060. doi: 10.2140/gt.2015.19.853.
[OY18] Tomotada Ohtsuki and Yoshiyuki Yokota. “On the asymptotic expansions of the
Kashaev invariant of the knots with 6 crossings”. In:Math. Proc. Camb. Philos. Soc.
165.2(2018),pp.287–339. issn:0305-0041. doi: 10.1017/S0305004117000494.
[Wit10] EdwardWitten. Analytic Continuation Of Chern-Simons Theory.Jan.18,2010.arXiv:
1001.2933 [hep-th].
[Wit89] EdwardWitten.“QuantumﬁeldtheoryandtheJonespolynomial”.In: Commun. Math.
Phys.121.3(1989),pp.351–399. issn:0010-3616. doi: 10.1007/BF01217730.
References 18
[Won25] Ka Ho Wong.Asymptotics aspects of Teichmüller TQFT for generalized FAMED semi-
geometric triangulations.2025.arXiv: 2512.23198 [math.GT].
[Yok00] Yoshiyuki Yokota.On the volume conjecture for hyperbolic knots. 2000. arXiv:math/
0009165 [math.QA].
[Zag07] Don Zagier. “The dilogarithm function”. In:Frontiers in number theory, physics, and
geometry II. On conformal ﬁeld theories, discrete groups and renormalization. Papers from
the meeting, Les Houches, France, March 9–21, 2003.Berlin:Springer,2007,pp.3–65.
isbn: 978-3-540-30307-7.doi: 10 . 1007 / 978 - 3 - 540 - 30308 - 4_ 1. url: https :
//people.mpim- bonn.mpg.de/zagier/files/doi/10.1007/978- 3- 540- 30308-
4_1/fulltext.pdf.
