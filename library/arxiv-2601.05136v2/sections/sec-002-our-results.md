---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant"
section_id: sec-002-our-results
section_title: "Our results"
section_number: null
pages: 3-4
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
doc_brief: "State integrals for the quantized SL₂(ℂ) Chern–Simons invariant — Previous work of the author and N."
---
LetK be an oriented, framed knot inS3 andρ a decorated representation ofK, which is a
representationρ: π1(S3\K)→ SL2(C) along with a choice of eigenspace for the image of
theperipheralsubgroupunder ρ. Inparticularthischoicedistinguishesaneigenvalue mofthe
meridians ofK. A log-meridian is a complex numberµ withe2πiµ = m. The main result of
[McP25a]isthedeﬁnitionofasequenceofinvariants 2
Zψ
N(K,ρ,µ )∈ C
forintegers N≥ 2. Wecanviewthemasaquantizationofthe SL2(C)Chern-Simonsinvariant,
as a geometric twist of the Kashaev [Kas95] and ADO [ADO92] invariants, or as a candidate
mathematicalrealizationof SL2(C)Chern-Simonstheory. Theconstructionmakessense(andour
resultsdotoo)forlinksandtanglesaswellbutforsimplicitywerestricttothecaseofknots.
LetD be an open knot diagram ofK (i.e a1-1 tangle diagram whose closure isK). LetE
be the set of internal segments (edges) ofD. Using quantum dilogarithms we deﬁne anaction
SN(D,µ ) : CE→ Csothat
t7→eNSN(D,µ|t) : CE→ C
is a meromorphic function. Given the choice of some additional gauge datau called ashadow
coloringtheinvariantof[McP25a]isbydeﬁnitionastatesum
Zψ
N(K,ρ,µ ) = 1
Ncr(D)
X
n∈[N]E
eNSN(D,µ|(β+n)/N)
where [N] ={0, 1,...,N − 1} and cr(D) is the crossing number ofD. The vectorβ∈ CE
encodes (ρ,u ). Foravector k∈ ZE withintegerentries 3 astate integralis
(1.2) JN(D,µ,β|k) :=
Z
[0,1]E
exp[N(SN(D,µ|β/N +t)− 2πik·t)] dt
InSection3weprove(Theorem1)that Zψ
N isgivenbythesumoverallstateintegrals:
(1.3) Zψ
N(K,ρ,µ ) =N(|E|−1)/2 X
k∈ZE
JN(D,µ,β|k)
1. Introduction 3
[McP25b]C.McPhail-Snyder,“Octahedralco-
ordinates from the Wirtinger presentation”.
arXiv doi
[Yok00]Y.Yokota, On the volume conjecture for
hyperbolic knots. arXiv
[BB04] S. Baseilhac and R. Benedetti, “Quan-
tumhyperbolicinvariantsof3-manifoldswith
PSL(2,C)-characters”. arXivdoi
[BWY21] F. Bonahon, H. Wong, and T. Yang,
Asymptotics of quantum invariants of surface dif-
feomorphisms I: conjecture and algebraic compu-
tations. arXiv
[KR05]R.KashaevandN.Reshetikhin,“Invari-
ants of tangles with ﬂat connections in their
complements”. arXivdoi
[AK14]J.E.AndersenandR.Kashaev,“ATQFT
fromquantumTeichmüllertheory”. arXiv doi
[AK13] J. E. Andersen and R. Kashaev,A new
formulation of the Teichmüller TQFT.arXiv
[Liu+25]T.Liu,S.Ming,X.Sun,B.Wu,andT.
Yang,Turaev-Viro invariant from the modular
double ofUqsl(2; R). arXiv
[Kas99]R.M.Kashaev,“Liouvillecentralcharge
inquantumTeichmüllertheory”. arXiv
[FG09] V. V. Fock and A. B. Goncharov, “The
quantum dilogarithm and representations of
quantumclustervarieties”. arXiv doi
[Ish26]T.Ishibashi, Cyclic quantum Teichmüller
theory. arXiv
[Oht17]T.Ohtsuki,“Ontheasymptoticexpan-
sions of the Kashaev invariant of hyperbolic
knotswithsevencrossings”. doi
[OY18] T. Ohtsuki and Y. Yokota, “On the
asymptoticexpansionsoftheKashaevinvariant
oftheknotswith6crossings”. doi
[CZ23]Q.ChenandS.Zhu, On the asymptotic
expansions of various quantum invariants II: the
colored Jones polynomial of twist knots at the root
of unitye
2π√−1
N + 1
M ande
2π√−1
N . arXiv
[AGP23]F.B.Aribi,F.Guéritaud,andE.Piguet-
Nakazawa,“Geometrictriangulationsandthe
TeichmüllerTQFTvolumeconjecturefortwist
knots”. arXivdoi
[AW24] F. B. Aribi and K. H. Wong, The
Andersen-KashaevvolumeconjectureforFAMED
geometric triangulations. arXiv
[AGW25] F. B. Aribi, A. Guilloux, and K. H.
Wong, FAMED by computer: proving the
Andersen-Kashaev volume conjecture for 42,000
knots. arXiv
[Won25]K.H.Wong, Asymptotics aspects of Te-
ichmüller TQFT for generalized FAMED semi-
geometric triangulations. arXiv
Themaintechnicaldiﬃcultyisensuringthecontourofintegrationavoidsthepolesof eNSN(D,µ).
WediscusstherequiredalgebraicconditioninSection2.2. Oncethisishandledusingthemethods
of[McP25b]re-writingthesumintermsoftheintegralsisanelementaryapplicationofFourier
series. Inparticulartheconvergenceoftheinﬁnitesumisautomatic.
AsN→∞ thefunctionsSN(D,µ )toafunction S(D)thatweinterpretastheChern-Simons
action. IntheliteratureS(D)isfrequentlycalledthe (Yokota)potentialfunction [Yok00]anddenoted
V. The critical points ofSN(D) are boundary-parabolic representations ofK and the critical
valuesaretheirChern-Simonsinvariants. AssuchTheorem1accomplishesStep1towardsproving
avolumeconjecturefor Zψ
N. Westatethisprecisely,explainhowthesumover ZE isnatural,and
discussbarrierstoStep2inSection4.
