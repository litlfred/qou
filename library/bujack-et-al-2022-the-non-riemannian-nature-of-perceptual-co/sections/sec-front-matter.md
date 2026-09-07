---
doc_id: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co
doc_title: "RESEARCHARTICLE PSYCHOLOGICALANDCOGNITIVESCIENCEMS The non-Riemannian nature of perceptual color space RoxanaBujacka,1 ,EmilyTeti a,b,JonahMiller a,ElektraCaffrey a,c,andTereceL.Tu"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-7
source_pdf: bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf
source_sha256: 2bc66a26d3901a29
---
RESEARCHARTICLE PSYCHOLOGICALANDCOGNITIVESCIENCEMS
The non-Riemannian nature of perceptual color space
RoxanaBujacka,1 ,EmilyTeti a,b,JonahMiller a,ElektraCaﬀrey a,c,andTereceL.Turton a
EditedbyBrianWandell,StanfordUniversity,Stanford,CA;receivedOctober28,2021;acceptedMarch13,2022
The scientific community generally agrees on the theory, introduced by Riemann and
furthered by Helmholtz and Schr¨odinger, that perceived color space is not Euclidean
but rather, a three-dimensional Riemannian space. We show that the principle of
diminishing returns applies to human color perception. This means that large color
differencescannotbederivedbyaddingaseriesofsmallsteps,andtherefore,perceptual
colorspacecannotbedescribedbyaRiemanniangeometry.Thisfindingisinconsistent
withthecurrentapproachestomodelingperceptualcolorspace.Therefore,theassumed
shape of color space requires a paradigm shift. Consequences of this apply to color
metrics that are currently used in image and video processing, color mapping, and the
paintandtextileindustries.Thesemetricsarevalidonlyforsmalldifferences.Rethinking
them outside of a Riemannian setting could provide a path to extending them to large
differences.Thisfindingfurtherhintsattheexistenceofasecond-orderWeber–Fechner
law describing perceived differences.
colorspace |Riemann |cognition |metric |diminishingreturns
Colorspacesarespecificorganizationsofcolors.Sincehumanshavethreeconestoperceive
color, color spaces are usually three-dimensional (3D). Color spaces can be directly
related to the three cones: red, green, and blue, such as CIE RGB. However, most color
spaces are mathematical constructs or models, such as CIE XYZ and CIE L*A*B*, with
transformation formulas* converting one to another (1). Apart from assigning a unique
coordinate to each color and arranging them in a sensible way, perceptual color spaces
arrange colors in a way that the distance between two colors reflects how differently
humans perceive them.
Background and Theory
We show how the principle of diminishing returns contradicts the paradigm of a
Riemannian color space, illustrated in Figs. 1 and 2. The key idea is that for a space to
be Riemannian, distancesΔE between stimuli A, B, C along a geodesic must satisfy
additivity: that is,
ΔE(A, B)+Δ E(B, C)=Δ E(A, C), [1]
while diminishing returns require the strict inequality of this relation (Eq.4).
RiemannianGeometryandColor. Inhisvisionarylecturewhereheintroducedageome-
trythatgeneralizesthenotionsofangle,curvature,andlengthtocurvedspaces,Riemann
(2) himself suggested that color forms a multidimensional manifold. This was probably
the largest step toward mathematical modeling of color since its description by means
of a vector space by Grassmann (3), which was rigorously formalized by Krantz (4). A
Riemannian manifold is a smooth manifoldM with a metricg smoothly varying overM
thatdefinesaninnerproductonthetangentspaceatpoint p ∈ M.Forafixedbasisin3D,
wecanexpressthemetricateachpoint pasamatrix gp ∈ R3×3 andtheinnerproductof
two vectorsu, v ∈ R3 at p as
< u, v >p= uT gp v. [2]
In this setting, the length of a curveγ :[ t0, t1]⊂ R→ M,
L(γ)=
∫ t1
t0
|γ′(t)|γ(t) dt =
∫ t1
t0
√ ⟨dγ(t)
dt , dγ(t)
dt
⟩
γ(t)
dt, [3]
will be of central importance. The path between two pointsA, B that minimizes the
length is called a geodesic, and its length is the distanceΔ(A, B) between these two
points, illustrated in Fig. 2.
*Thetransformationsometimesdependsonadditionalparameters:forexample,thewhitepoint.
Significance
Forover100y,thescientiﬁc
communityhasadheredtoa
paradigm,introducedbyRiemann
andfurtheredbyHelmholtzand
Schrodinger,whereperceptual
colorspaceisathree-dimensional
Riemannianspace.Thisimplies
thatthedistancebetweentwo
colorsisthelengthoftheshortest
paththatconnectsthem.We
showthataRiemannianmetric
overestimatestheperceptionof
largecolordiﬀerencesbecause
largecolordiﬀerencesare
perceivedaslessthanthesumof
smalldiﬀerences.Thiseﬀect,
calleddiminishingreturns,cannot
existinaRiemanniangeometry.
Consequently,weneedtoadapt
howwemodelcolordiﬀerences,
asthecurrentstandard, ΔE,
recognizedbytheInternational
CommissionforWeightsand
Measures,doesnotaccountfor
diminishingreturnsincolor
diﬀerenceperception.
Author aﬃliations:aComputer, Computational, and Sta-
tistical Sciences Division, Los Alamos National Labora-
tory,LosAlamos,NM87545; bDepartmentofPsychology,
Florida Atlantic University, Boca Raton, FL 33431; and
cDepartment of Computer Science, University of New
Mexico,Albuquerque,NM87106
Author contributions: R.B. designed research; E.C. and
T.L.T. performed research; E.T. analyzed data; J.M. pro-
vided mathematical theory; E.C. provided assistance with
experiments; and R.B., E.T., J.M., and T.L.T. wrote the
paper.
Theauthorsdeclarenocompetinginterest.
ThisarticleisaPNASDirectSubmission.
Copyright © 2022 the Author(s). Published by PNAS.
This article is distributed under CreativeCommons
Attribution-NonCommercial-NoDerivatives License 4.0
(CCBY-NC-ND).
1To whom correspondence may be addressed. Email:
bujack@lanl.gov.
PublishedApril29,2022.
PNAS 2022 Vol. 119 No. 18 e2119753119 https://doi.org/10.1073/pnas.2119753119 1of10
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Fig. 1. Diminishing returns imply that large color diﬀerences appear less
thanthesumoftheirparts.Thisimageisapurelyﬁgurativeillustrationofhow
thisphenomenoncouldpotentiallyoccur,eventhoughthisspeciﬁcgeometry
is not suggested in this paper. If an isoluminant plane through color space
(Upper) would, for example, have the shape of a curved two-dimensional
submanifold embedded in a 3D space (Lower), then the 3D Euclidean metric
wouldproducetheinequalityofdiminishingreturns.
vonHelmholtz(5)wasthefirsttodescribethedistancebetween
colorsbymeansofalineelement † inaRiemannianmanifold.He
defines the shortest path in a color space to be the path for which
the sum of its just noticeable differences is minimal. He bases his
line element on the Weber–Fechner law (6).
Schr¨odinger (7) also assumes that color perception is Rie-
mannian, but Schr¨odinger (7) strictly rejects Helmholtz’s line
element because it produces surfaces of isoluminance that are not
orthogonal to the direction of intensity increase and suggests an
alternative one.
Theseworksarebasedprimarilyongeometryandmathematical
reasoning and only partly on experiment. However, experimental
evidence against a Euclidean color space was found, for example,
in the Nickerson index of fading (8). Since then, many authors
have argued that color perception is not Euclidean but rather,
Fig. 2. Geodesics (shortest paths computed with the shooting method)
betweenthecornersofthesRGBcubeinCIELABwithitsnon-Euclideanmetric
ΔE∗
2000 (79) illustrate what has long been known for perceptual color spaces
in general, namely that in contrast to a Euclidean setting (e.g.,ΔE∗
1976), the
geodesics do not form straight lines. In this paper, we go one step further
and show what CIE LAB does not capture: that in contrast to a Riemannian
setting, their lengths do not even coincide with the distances between their
endpoints.
†Theconceptlineelement, ds2 = g,ispreferredintheliteratureovertheconceptofmetric,
buttheycanbeusedinterchangeablybecauseeachdeterminestheother.
Riemannian (9–16), with experiments undertaken to determine
coefficients of a Riemannian metric describing the perceived
differences of colors (11, 17–21).
Lastly, the interested reader should review Wyszecki and Stiles
(1) for an introduction to color theory, Resnikoff (22) for an
excellent summary of the historical development of the idea of
color space, and Vos (23, 24) for superb visualizations of the
differentlineelementsofcolorperceptionandahistoricalaccount
on their development.
The Principle of Diminishing Returns.The principle of dimin-
ishing returns in color refers to the phenomenon that large color
differencesareunderestimatedbyhumanperception,asshownin
Fig. 1. Even if a colorB lies on the shortest path betweenA and
C, the sum of the perceived lengths of the two segments exceeds
the total perceived length:
ΔE(A, B)+Δ E(B, C)>ΔE(A, C). [4]
Importantly, Eq.4 holds even along geodesics, making it distinct
from and stronger than the triangle inequality. The term “dimin-
ishing returns” was coined by Judd (13). He defines the concept
of an ideal color space as “a tridimensional array of points, each
representing a color, so located that the length of the straight
line between any two points is proportional to the perceived
size of the difference” (25). In his papers, he collects evidence
from the literature that such an ideal color space cannot exist
[e.g., referring to the experiments of Nickerson and Stultz (8)
andMacAdam(20)].Thelatterdescribesanexperimentinwhich
observers judged the perceived distances between neighboring
colors in three concentric, equiluminous hexagons of different
sizes in CIE xyY. He then determined the coefficients,H1, gij,
p ∈ R, i, j ∈{1,2},oftheweightedadaptationtoaRiemannian
distance formula
¯H = H1(g11(Δx)2 +2 g12ΔxΔy + g22(Δy)2)
p
2 [5]
tobestfittheseperceiveddifferences.Hefoundthattheexponent
p,whichmakestheformulanon-Riemanninan if p ⁄=1,isgener-
ally smaller than 1, indicating diminishing returns.
At approximately the same time, Helm (26) conducted ex-
periments in which the observer estimated color distances and
ratios between colors of constant luminance and saturation while
varying hue. He then used multidimensional scaling (MDS) to
estimate the dimensionality of the underlying space (27). For the
ratioexperiments,theresultrevealedatwo-dimensionalcircle,but
for the distances, the dimensionality was 12. Helm (26) argued
that this was the consequence of the underestimation of large
distances. A logarithmic transformation of the distances in CIE
xyY resulted in the expected dimensionality of two and a strong
correlationtotheoutcomeoftheratioexperiments.Inthecontext
of contrast constancy across frequencies of sinusoidal gratings,
Cannon (28) studied the relation between physical and perceived
contrast, with contrast defined as
(Lmax − Lmin)/(Lmax + Lmin), [6]
where L is physical luminance. In suprathreshold conditions, he
found a power law with an exponent of∼0.5 to be a good fit,
similartotheresultsofMacAdam(20).Despitethesefindings,the
topic remains controversial. Using MDS, many researchers have
found good agreement between color difference experiments and
an additive 3D Euclidean space (29–33). Exceptions are Ekman
(34), Helm (26), and Izmailov and Sokolov (35). The lattermost
found that color space can be embedded into a 3D spherical
submanifold of a four-dimensional Euclidean space in analogy to
2of10 https://doi.org/10.1073/pnas.2119753119 pnas.org
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Fig. 3. Thurstonian distance perception (58) of a triad modeled with (solid)
and without (dashed) additivity with an example scaling functionf(Δψ)=√Δψ. If additivity is assumed and the gray-shaded Gaussians are appropri-
ately centered, the diﬀerence between the means can be subtracted to give
theperceiveddiﬀerencebetweenthestandardandeithertest(shownasthe
shadedgreenandorangetriads).Thediﬀerencebetweenthesemeanswould
betheperceiveddiﬀerenceofdiﬀerences,whichcanbeplottedonaGaussian
centered at zero, as shown inLower, to predict how often participants would
be incorrect. However, if diminishing returns should exist, the means of
the green and orange Gaussians should be scaled as demonstrated by the
dashed distributions in the second row. The eﬀect of the scaling function is
an increased rate of predicted incorrect responses by more than an order of
magnitude.
thesettinginFig.3.TheyarguethattheEuclideandistances CAB
between colors A and B in their high-dimensional embedding
spaces provide the perceived differences and are related to the
arclengths DAB of the geodesics on the manifolds via
CAB =2 sin(DAB/2). [7]
They explicitly note the principle of diminishing returns: “that
the integral of just noticeable differences between colors does
not coincide with direct estimations of the subjective differences
between the colors” (35).
Currently, there is no officially recognized color space that
models the lack of additivity resulting from diminishing returns
(36, 37). Summarizing existing literature, there is experimen-
tal evidence for diminishing returns (20, 26, 28, 35, 38, 39),
anecdotal evidence for the opposite [i.e., large color differences
areoverestimated ΔE(A, B)+Δ E(B, C)<ΔE(A, C)](40),
and an overwhelming number of papers arguing against both
(i.e., small differences add up to large ones along the shortest
path)(Eq. 1)(29–33,40–43).Proponentsofdiminishingreturns
suggest three forms; Helm (26) assumes a logarithmic function,
MacAdam(20)assumesapolynomialfunction,andIzmailovand
Sokolov(35)assumeasinusoidalfunctionbetweenjustnoticeable
and large perceived color differences.
The Contradiction between Diminishing Returns and the
Paradigm of Riemannian Color Space.The principle of dim-
inishing returns has long served as an argument against the
existence of a Euclidean color space that models perceived color
differences(13,25,44,45).Sofar,however,ithasnotbeenusedas
anargumenttorejectaRiemanniancolorspace.Apossiblereason
might be that the idea of Riemannian geometry is thought of as
the union of all geometries, including straight and curved spaces,
instead of a specific geometry satisfying rigid axioms. However,
we know with certainty that MacAdam (14) was aware of the
possibility of color space not being Riemannian. He describes
that the principle of hue superimportance‡ as captured in the
Nickerson index of fading (8) is in violation of Riemannian
geometry in his work on Judd in 1979 (14). Most fascinatingly,
MacAdam (14) summarizes that “there was no strong evidence
that those conditions for representation by a Riemannian (non-
Euclidean) space are violated,” which indicates that his own
findings from 1963 about diminishing returns (20) seem not
to evoke skepticism of color space being Riemannian.
WhileargumentsagainstaEuclideancolorspaceareubiquitous
(8, 13, 25, 46) [e.g., Ennis and Zaidi (47) find that color per-
ception is approximately an affine space], there are few instances
in the literature that question the Riemannian nature of color
space. Exceptions are Zeyen et al. (48), who suggest an interpo-
lation algorithm for color maps that works in non-Riemannian
geometry,andGriffinandMylonas(49),whoexpressdoubtwhen
theydevelopaRiemanniancategoricalmetricfromtheprobability
distributions of a crowdsourced color-naming experiment.
Yet, the principle of diminishing returns contradicts the pre-
vailing paradigm of a Riemannian color space. Assume that color
space is Riemannian and thatγ is a geodesic between the colors
A=γ(t0) and C =γ(t2) containing the pointB =γ(t1) with
t0 < t1 < t2.Th e n ,t h ep a r to fγ between A and B, γ1 =γ|t0,t1,
is a geodesic, as is the part betweenB and C.§ Therefore, the dis-
tances between the three points in a Riemannian setting coincide
withthelengthsofthecurvesegments,andthecontradictionwith
the principle of diminishing returns, Eq.4, follows immediately
from the additivity of integration boundaries via
Δ(A, C)
Eq. 3
=
∫ t2
t0
|γ′(t)|γ(t) dt
=
∫ t1
t0
|γ′(t)|γ(t) dt +
∫ t2
t1
|γ′(t)|γ(t) dt
Eq. 3
=Δ (A, B)+Δ( B, C).
[8]
In the remainder of this paper, we show that diminishing returns
do exist in human color perception, and we provide an estimate
of the shape through experiments on the neutral axis, which we
assume to be a geodesic. This, in turn, proves that the current
paradigm of Riemannian color space is incorrect.
Pleasenotethatitissufficienttoshowoneplaceincolorspace
where additivity is violated to prove that the whole space is not
Riemannian. We conduct our experiments on the neutral axis
because it is the location with the highest probability of being a
geodesic based on existing experiments and standards (36). We
do not rule out that there are loci somewhere in color space that
locally have a Riemannian structure, but the full 3D color space
itself is not Riemannian if the neutral axis is not.
Experiment
Ramsay (30) suggests that the principle of diminishing returns
or its opposite may have been spuriously identified by other
‡Hue superimportance refers to the phenomenon that an isoluminant circle centered at
gray has a circumference aboutπ times its radius (8, 25). In our understanding of the
subject,huesuperimportancecanactuallybemodeledinaRiemannianspace.
§Iftherewasashorterconnection, γ′
1,connecting Aand B,thenreplacing γ′
1 with γ1 in γ
wouldbeshorterthan γ,contradictingthatitisageodesic.
PNAS 2022 Vol. 119 No.18 e2119753119 https://doi.org/10.1073/pnas.2119753119 3of10
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
researchers (daringly including his PhD advisor, Helm) because
of experimental procedures (successive intervals, paired compar-
isons) ill suited to the task. Indeed, open-ended and criterion-
dependent tasks give less accurate measures of similarity because
of individual factors (50) and the difficulty of the task (51). In
particular, humans are not good at judging questions of the type
“How big is the difference?” that form the basis for many large
difference experiments (31, 34, 35).
Instead, we use a more reliable two-alternative forced choice
(2AFC) task, where the participant simply answers the following
question: “Which is more different?” Specifically, we use a triad
arrangement of stimuli with the reference in the middle and one
test on either side. Each of 320 triads covering the neutral axis
wasjudgedbyatleast250differentparticipantsinacrowdsourced
study on Amazon Mechanical Turk (MTurk) (52).¶
Because of its reliability, this task has been previously used to
studyhumancolorperception(27,53–55).However,theanalysis
of this type of experiment requires more assumptions to derive
a continuous scale from binary responses, compared with Likert-
scaleoropen-endedtasks.Asaconsequence,inallexistingmodels,
additivity of small differences is inherent. Our analysis uses the
underlying theory without requiring this additivity.
Analysis
Regression to Investigate Diminishing Returns.We denote the
differences in a triad(t1, ref, t2) by di :=|L∗
ref − L∗
ti |, i =1,2 .
The existence of diminishing returns implies that as the average
difference of the triad¯d :=1/2(d1 + d2) increases, the propor-
tion of selecting one test over the other should approach chance.
To illustrate this, consider the two triads in Fig. 4, which were
selected to have the same difference in differencesΔd :=||d1|−
|d2||. If the differences were additive, as Thurstone (56) suggests,
participants should select t2 with the same frequency for both
triads.
Totestfortheexistenceofdiminishingreturns,weconsiderthe
degree of consensusC,
C =|pt2 −0.5|, [9]
where pt2 is the proportion that participants selected the lighter
test. As participants respond more at chance level,C approaches
Fig. 4. Two triads with the same diﬀerence in diﬀerencesΔd =12.5 in
L∗ units. (Upper) L∗ =45,50,67.5, respectively. ( Bottom) L∗ =20,50,92.5,
respectively.
¶Adetaileddescriptionoftheexperimentaldesigncanbefoundin Materials and Methods.
zero. If diminishing returns exist, the degree of consensus should
decreasewithincreasedaveragedifferenceinthetriad.Wecantest
this using least-squares regression,
ˆC =β0 +βΔd=5 ×δΔd=5 +βΔd=10 ×δΔd=10 +β¯d × ¯d.
[10]
Here, Δd is the difference in differences, and¯d is the average
difference. We use the differences inL∗ for this first analysis, so
Δd takes on three discrete values. We encode this variable as two
dummy variables using the KroneckerΔ,
δΔd=5 =
{1, Δ d =5,
0, Δ d ⁄=5. [11]
Diminishingreturnscanbeformalizedasanegativecoefficientfor
theaveragedifference, β¯d,indicatingresponsesapproachingpure
chance as the average difference in the triad increases.
Maximum Likelihood Estimation to Model Diminishing
Returns. Totransformbinaryresponsesfroma2AFCtaskintoa
perceptualscale,certainassumptionsabouttheunderlyingprocess
must be made. The most common analyses rely on Thurstone’s
theoryofaGaussianperceptualprocess(56).Here,theperception
of any stimulus,xi, is a normally distributed variable
Percept(xi)∼N (ψi,σ2) [12]
about its perceived strength (mean),ψi ∈ R, with some discrim-
inal dispersion (SD)σ ∈ R+. The perception of the difference
between stimulixi and xj takes the form
Percept(xi − xj)∼N (ψi −ψj,2σ2). [13]
This model revolutionized psychophysics because it explains how
different observers can judge stimuli differently and even how
one observer can judge them differently on different trials of an
experiment (56).
It follows that the perception of the difference of differences
in the triad is also a stochastic variable following a normal
distribution. The frequency of selecting one test should adhere to
the cumulative normal distribution whereμ=0,# as illustrated
in Fig. 3(58). The 2AFC experiment provides the proportion
of responses in which observers selected t1 as more different,
compared with the reference, than t2 [i.e., the probability
P(t1|ψref,ψt1,ψt2,σ)] .Th i si ss h o w na st h es h a d e dr e g i o ni n
theGaussian in Fig. 3,Lower. Fromthat, the perceived strengths,
ψref, ψt1,a n dψt2, can be estimated using the inverse of the
cumulativenormaldistribution, Φ,oressentiallybytransforming
the proportions of selectingt1 over t2 into z scores to represent
interpoint distances
P(t1|ψref,ψt1,ψt2,4σ2)
=Φ4σ2(|ψref −ψt1|−| ψref −ψt2|). [14]
There exist two suitable methods for this estimation. Torg-
erson (27) detailed how to solve MDS using these z scores.
This approach has been widely implemented using a variety of
algorithms to perform the matrix algebra (27, 41, 42, 55, 59).
More recently, maximum likelihood estimation (MLE) has been
used to construct a unidimensional perceptual scale from 2AFC
datausingThurstone’stheory(53,57,60).MLEestimatestheset
ofparameters,inourcase ψi andσ,ofastochasticprocess,Eq. 14,
thatismostlikelytoproduceagivensetofobservations(here,the
#AmoredetailedderivationisinMaloneyandYang(57).
4of10 https://doi.org/10.1073/pnas.2119753119 pnas.org
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
responses from the 2AFC experiment). If the likelihood function
can be differentiated with respect to the parameters, MLE can be
performedanalytically.Here,however,theparametersarediscrete,
soMLEmustbeperformednumerically.Bothoftheseapproaches
(MDS and MLE) directly rely on the additivity of normally
distributed variables, which implies that smaller differences can
beaddedtogetlargerdifferences(i.e.,theabsenceofdiminishing
returns).
If larger differences are overestimated when summing small
differences, the sum of small differences needs to be scaled. This
canbeachievedusingamoreflexibleMLEapproachthatdirectly
models the differencesΔ(i, j)= f(|ψi −ψj|) between stimuli
through a monotonic scaling function f : R→ R rather than
individual stimulus strengths. To do this, we replace Eq.14,
describing the probability that t1 is selected as closer to the
reference, by
P(t1|ψref,ψt1,ψt2,2σ2, f)
=Φ2σ (f(|ψref −ψt1|)− f(|ψref −ψt2|))
= 1
2σ
√
2π
∫ f(|ψref −ψt1|)−f(|ψref −ψt2|)
−∞
e− x2
4σ2 dx.
[15]
This probability can be used as the likelihood off given a single
response:
L(f|t1,ψref,ψt1,ψt2,2σ2)= P(t1|ψref,ψt1,ψt2,2σ2, f).
[16]
Thelikelihoodofthedatasetisthejointprobabilityofallresponses
given the parameter space. In practice, the logarithm is taken for
the individual likelihoods to be summed rather than multiplied.
ThisloglikelihoodismaximizedthroughMLEtofindtheoptimal
parameters, here the shape off.
The model, adapted from existing methods validated through
simulations(57,60),doesnotassumetheexistenceofadditivityor
diminishing returns. Rather, the shape off will reveal one or the
other. A concavef [i.e., f(Δψi)+ f(Δψj)> f(Δψi +Δψj)]
would indicate that diminishing returns exist. Alternatively, a
linear f [i.e., f(Δψi)+ f(Δψj)= f(Δψi +Δψj)] would in-
dicate that differences are additive and that diminishing returns
do not exist.
Our implementation uses a monotonic cubic spline function
as the structure for f, which makes no assumptions about the
concavity. For comparison, we have included MLE models of a
baselinecase,whichlinearlyscalesthe L∗ values,andacasewhere
the perceptual scale,g(L∗)= ψ, is estimated using a monotonic
cubic spline. When modeling the difference scaling functionf,
we use theψ-values determined byg. In addition to the spline
functionfor f,wecanalsouseMLEtoestimateadifferencescaling
function using three previously proposed functions: logarithmic,
polynomial, and sinusoidal.
UsingMLEtomodelapotentialscalingfunctionisananalysis
developed for responses to a 2AFC task that does not make the
assumption of additivity. As such, it is now possible to test the
existence of diminishing returns in color difference perception.
Results
Regression. The best-fit regression line produces the coefficients
in Table 1. The coefficient of interest is significantly negative
(β¯d =−0.005, p <0.001), supporting the existence of dimin-
ishing returns. This coefficient indicates that the frequency that
participants select a given test approaches chance when differ-
ences are larger. This effect can be seen in Fig. 5, showing how
participants’responsesareclosertochancewithincreasedaverage
Table1. Coeﬃcientsoftheregressionline
Coeﬃcient Estimate tstatistic Signiﬁcance
β0 0.161 t(60)= 8.894 <0.001
βΔd=5 0.048 t(60)= 2.815 0.010
βΔd=10 0.119 t(60)= 6.632 <0.001
β¯d −0.005 t(60)= −5.566 <0.001
Theregressionmodelproducedagoodﬁttotheexperimentaldata: R2 =0.556, F(3,60 )=
25.00, P <0.001.The β-coeﬃcientsareunstandardizedforinterpretability.
difference, ¯d, despite the value for the difference of differences,
Δd, being the same. This suggests the existence of diminishing
returns;however,itreliesonthe L∗ axisbeingnearlyperceptually
uniform. This assumption may not be appropriate, so we inter-
pret the negativity of theβ¯d as weakly supporting our claim of
nonadditivity and as motivation to carry out further analysis.
MLE. ToassessthevalidityandstabilityoftheMLE-approximated
scaling function, we used a combination of cross-validation
and bootstrapping. We used 10 different test/train splits where
each test set included a random selection of 50 responses per
triad, leaving between 199 and 254 responses per triad in the
training set. The training set contained a total of 75,896 trials.
To obtain CIs around the learned scaling function, we used 100
bootstrapped samples of size 48,000 or∼150 responses per triad
from each training set.
For each training set, a functiong : R→ R mapping fromL∗
to perceived strength and a functionf : R→ R mapping from
the difference in perceived strengths to the perceived difference
were estimated. Their concatenation then provides the perceived
difference to two stimulixi, xj via
f(|g(xi)− g(xj)|). [17]
This approach was introduced by Krantz (61) in 1967 but aban-
doned because of the large number of parameters to estimate.
We first estimate the perceptual functiong to transform theL∗
Fig. 5. Degree of consensus is the absolute value of selecting a given
test minus 50%. The negative slope of the lines indicates that participants’
responsestendtowardchancewithincreasingaveragediﬀerenceinthetriad,
despite the diﬀerence of diﬀerences remaining constant. A 95% CI around
eachlineisshowningray.
PNAS 2022 Vol. 119 No.18 e2119753119 https://doi.org/10.1073/pnas.2119753119 5of10
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
values to perceived strengthsψ and then, use the difference inψ
to estimate the difference scaling functionf.
Theperceptualfunction g ismodeledusingamonotonicspline
with four nonzero control points. The values of these points are
estimated in the optimization. These control points, along with
the point(0,0), completely determine the spline function. The
SDwassetto σ =1.Aftertheestimation, g wasrescaledtofitthe
original domain[0,100] since a new SD will be used to estimate
the scaling function.
Four functional forms of the difference scaling functionf are
used in the MLE. The first is a spline of the same form used to
approximate g. The remaining three are parameterized forms of
the hypothesized functions previously suggested to account for
diminishing returns. For these functions, the differences inψ
were first scaled to fall in[0,1]. In each of these functions, the
polynomial (20), the logarithm (26), and the sine (35), there is a
parametertodeterminetheshape, a,andaparametertodetermine
the range,b:
fpoly(Δψ)= bΔψa,
flog(Δψ)= blog(aΔψ +1)
log(a +1) ,
fsin(Δψ)= b
sin(Δψπ
2a+1)
sin( π
2a+1).
[18]
The optimal values of these parameters were found by the MLE.
In all functional forms off, the SD was set to one.
Allmodels,includingthecaseofmodelingonly gandabaseline
case where theL∗ values are scaled linearly to the optimal range
for an SD of one, were evaluated based on their ability to predict
participantresponsesinthetestset.Theaverageaccuracyofthese
models and error bars are the 95% confidence level is shown in
Fig. 6. Models were trained using data from all triads; however,
accuracy is visualized across the five levels of the standard. We see
herethatthebaselineaccuracyismuchlowerfortriadswithdarker
standards.
Themostaccuratemodelsaretheonesthatincludeboth g and
f, specifically whenf takes the spline form (green line) or the log
Fig. 6. Accuracyofoptimalmodels.
Fig. 7. Optimal perceptual function g from Eq. 17 mapping L∗ values to
perceived grayness, ψ. The shaded region indicates the middle 95% of all
learnedmodelsacrosstestsetsandbootstrappedtrainingsets.
(purpleline).Themodelsusingthepolynomialandsinefor f have
a larger spread and are not significantly higher than when using
only theg transformation.
The average perceptual functiong and a 95% CI are shown in
Fig. 7. The dashed line represents what would have been learned
ifthe L∗ axisperfectlydescribedthedata.Thedeviationfromthe
dashedlineoccursnearthe L∗ ofthebackground,suggestingthat
this may be due to the crispening effect (62).
The average learned scaling functionf using the flexible spline
form is shown in Fig. 8. The dashed black line indicates the
function that would have been learned if there was no evidence
of diminishing returns.
The average scaling functions using theparameterized hypoth-
esized forms off are shown in Fig. 9, with the spline function
showninblackforcomparison.Theparameterizedlogarithmfalls
closesttothespline,whichisinaccordancewiththeirsimilarand
high accuracies in Fig. 6.
Limitations and Mitigations
There are two assumptions that we make throughout our work
thatcouldlimitthegeneralityofourresults.Wediscussthemhere
and explain the design and verification choices that we made to
mitigate them.
InﬂuenceoftheBackground. Thebackgroundcanhaveastrong
influenceonthewaycolorsareperceived(63).We,therefore,keep
the background constant across all experiments.
The crispening effect causes colors in the vicinity of the back-
ground to appear more different from its neighbors than those
far away (64, 65). This effect could potentially interfere with the
measurement of diminishing returns. Sch¨onfelder’s law suggests
that the crispening effect is strongest at the exact location of the
backgroundcolor(63).Wechosethebackgroundtobedarkblue,
approximately equivalent to that used by Krantz (54). By using a
hue, the background is not in the direct vicinity of any stimulus
presented, and the crispening effect is significantly reduced (62).
Still,evenasmallcrispeningeffectcouldviolatetheassumptionof
6of10 https://doi.org/10.1073/pnas.2119753119 pnas.org
Downloaded from https://www.pnas.org by 136.47.145.179 on May 11, 2026 from IP address 136.47.145.179.
Fig. 8. Optimaldiﬀerencescalingfunction f fromEq. 17usingthesplinewith
fourcontrolpoints.Theshadedregionindicatesthemiddle95%ofalllearned
modelsacrosstestsetsandbootstrappedtrainingsets.
L∗ being a reasonable proxy for a perceptual scale. We, therefore,
model the transform g from L∗ to an actual perceptual scale
Ψ before estimating the effect of diminishing returns f.Th e
shape of our modeled g shows the expected compensation for
the crispening effect around the luminance of our background of
L∗ =20 (Fig. 7).
Apart from crispening, it has been observed that increments
in the lightness of the background can be perceived differently
than decrements (62, 66). To see if this effect could potentially
explain the measured nonadditivity, we performed experiments
around five different centers on the neutral axis, some closer and
Fig. 9. Optimal diﬀerence scaling functions using the hypothesized func-
tions. The shaded region indicates the middle 95% of all learned models
acrosstestsetsandbootstrappedtrainingsets.
some farther from the background and some involving stimuli
exclusively brighter than the background (L∗ =50,60,70 ).
Wecomparedtheincreaseinpredictivepowerduetoaccount-
ingforthesizeofthedifferencesusingthescalingfunctionacross
each center individually. At each center, there was a significant
increase in predictive power when using both theg and f trans-
formations compared with using onlyg alone, as seen in Fig. 6.
While there is less of an increase at the centers with increments
only( L∗ =50,60,70 ),theincreaseremainssignificant.Thisleads
ustotheconclusionthattheeffectofdiminishingreturnsisrobust
to some degree against the influence of the background.
TheNeutralAxisasaGeodesic. Itisnottrivialtoverifywhether
any given path through color space is a geodesic. We chose the
neutral axis because it is the one path on which all available data
agree that it is indeed a geodesic. For example, the neutral axis
is a geodesic in the commonly used color space CIE L*A*B* for
its 1976, 1994, and 2000 metrics. It is also a geodesic in the
Euclidean color spaces CIE CAM, CIE RGB, CIE XYZ, CIE
LUV,DIN99,AdobeRGB,andsRGB,whereitisalwaysastraight
