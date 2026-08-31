---
doc_id: arxiv-1804.03926v3
doc_title: "Weighted Poincaré inequalities, concentration inequalities and tail bounds related to Stein kernels in dimension one"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1804.03926v3.pdf
source_sha256: 8ad8e2d5a8881a5b
---
Since its introduction by Charles Stein ([Ste72, Ste86]), t he so-called Stein’s method is a corpus of
techniques that revealed itself very successful in studying probability approximation and convergence
in law (see for instance [CGS11, Cha14, LRS17] and reference s therein). Much less is known regard-
ing the interplay between Stein’s method and functional ine qualities. Recently, a series of papers
([LNP15, LNP17, FN17, CFP17]) started to ﬁll this gap.
More precisely, Ledoux et al. [LNP15] provide some improvem ent of the log-Sobolev inequality
and Talagrand’s quadratic transportation cost inequality through the use of a Stein kernel and in
particular, the Stein discrepancy that measures the closen ess of the Stein kernels to identity. In a
second paper [LNP17], these authors also provide a lower bou nd of the deﬁcit in the Gaussian log-
Sobolev inequality in terms Stein’s characterization of the Gaussian distribution. Recently, Fathi and
Nelson [FN17] also consider free Stein kernel and use it to im prove the free log-Sobolev inequality.
Finally, Courtade et al. [CFP17] proved that the existence a reversed weighted Poincar´ e inequality
is suﬃcient to ensure existence of a Stein kernel. To do so, th ey use an elegant argument based on
the Lax-Milgram theorem. They also provide bounds on the Ste in discrepancy and application to a
quantitative central limit theorem.
Particularizing to dimension one, the present paper aims at pursuing investigations about the
relations between Stein’s method - especially Stein kernels - and some functional inequalities, together
1
with some concentration inequalities. The limitation to di mension one comes, for most of the results,
from the one-dimensional nature of the covariance identities given in Section 2, that are instrumental
for the rest of the paper and which crucially rely on the use of the properties of the cumulative
distribution function.
We prove that a measure ν having a ﬁnite ﬁrst moment and a density with connected suppo rt
satisﬁes a weighted Poincar´ e inequality in the sense of [BL 09b], with the weight being the Stein
kernelτν (see the deﬁnition in Section 2 below), that is unique in this case. More precisely, for any
f ∈L2 (ν), absolutely continuous, we have
Var (f (X)) ≤ E
[
τν (X)
(
f ′ (X)
) 2]
. (1)
The latter inequality allows us to recover by diﬀerent techniques some weighted Poincar´ e inequal-
ities previously established in [BL14] for the Beta distrib ution or in [BJM16a] for the generalized
Cauchy distribution and to highlight new ones, considering for instance Pearson’s class of distribu-
tions.
It is also well-known that Muckenhoupt-type criteria chara cterize (weighted) Poincar´ e and log-
Sobolev inequalities on the real line ([ABC +00, BG99]). We indeed recover, up to a multiplicative
constant, inequality (1) from the classical Muckenhoupt cr iterion. Furthermore, using the criterion
ﬁrst established by Bobkov and G¨ otze [BG99] to characterize log-Sobolev inequalities on the real line,
we prove that, under the conditions ensuring the weighted Poincar´ e inequality (1), together with some
asymptotic assumptions on the behavior of the Stein kernel a round the edges of the support of the
measure ν, the following inequality holds,
Entν
(
g2)
≤Cν
∫
τ2
ν
(
g′) 2dν , (2)
for some constant Cν > 0 and with Ent ν
(
g2)
=
∫
g2 logg2dν −
∫
g2dν log
∫
g2dν. More precisely,
if the support of ν is compact, then inequality (2) is valid if τ−1
ν is integrable at the edges of the
support. If on contrary, an edge of the support is inﬁnite, th en a necessary condition for inequality
(2) to hold is that the Stein kernel does not tend to zero aroun d this edge.
We also derive asymmetric Brascamp-Lieb type inequalities related to the Stein kernel and show
that existence of a uniformly bounded Stein kernel is suﬃcie nt to ensure a positive Cheeger isoperi-
metric constant.
There is also a growing literature, initiated by Chatterjee ([Cha07]), about the links between
Stein’s method and concentration inequalities. Several ap proaches are considered, from the method
of exchangeable pairs ([Cha07, CD10, MJC +14, PMT16]), to the density approach coupled with
Malliavin calculus ([NV09, Vie09, EV13, TM15]), size biase d coupling ([GG11b, GG11a, GGR11,
CGJ18]), zero bias coupling ([GIs14]) or more general Stein couplings ([BRW18]). As emphasized
for instance in the survey by Chatterjee [Cha14], one major s trength of Stein-type methodologies
applied to concentration of measure is that it often allows to deal with dependent and complex system
of random variables, ﬁnding for instance applications in st atistical mechanics or in random graph
theory.
In the present work, we investigate relationships between S tein kernels and concentration of
measure by building upon ideas and exporting techniques abo ut the use of covariance identities for
Gaussian concentration from Bobkov, G¨ otze and Houdr´ e [BGH01].
Considering ﬁrst the case where a Stein kernel is uniformly b ounded, we recover the well-known
fact that the associated random variable admits a sub-Gauss ian behavior. But we also prove in this
setting some reﬁned concentration inequalities, that we ca ll generalized Mills’ type inequalities, in
2
reference to the classical Mills’ inequality for the normal distribution (see for instance [D¨ um10]).
Assume also that a Stein kernel τv exists for the measure ν, is uniformly bounded, and denote
c = ‖τv‖−1
∞ . Then the Furthermore, the functionTg (r) =ecr2/ 2E (g − Eg) 1{g−Eg≥r} is non-increasing
in r ≥ 0. In particular, for all r> 0,
P (g − Eg ≥r) ≤ E (g − Eg)+
e−cr2/ 2
r . (3)
In particular, Beta distributions have a bounded Stein kern el and our concentration inequalities
improve on previously best known concentration inequaliti es for Beta distributions, recently due to
Bobkov and Ledoux [BL14].
Furthermore, we consider the situation where a Stein kernel has a sub-linear behavior, recovering
and extending in this case sub-Gamma concentration previou sly established by Nourdin and Viens
[NV09]. We also prove some generalized Mills’ type inequalities in this case. More generally, we prove
that the Laplace transform of a Stein kernel controls the Lap lace transform of a Lipschitz function
taken on the related distribution. Take f a 1-Lipschitz function with mean zero with respect to ν
and assume that f has an exponential moment with respect to ν, that is there exists a> 0 such that
E
[
eaf (X)]
< +∞. Then for any λ ∈ (0,a ),
E
[
eλf (X)
]
≤ E
[
eλ 2τ ν (X)
]
. (4)
It is worth noting that to prove such a result, we state a gener ic lemma - Lemma 19 Section 4 -
allowing to bound the Laplace transform of a random variable . We believe that this lemma has an
interest by itself, as it may be very convenient when dealing with Chernoﬀ’s method in general.
We also obtain lower tail bounds without the need of Malliavin calculus, thus extending previous
results due to Nourdin and Viens [NV09] and Viens [Vie09].
The paper is organized as follows. In Section 2 we introduce s ome background material, by
discussing some well-known and new formulas for Stein kerne ls and Stein factors in connection with
Menz and Otto’s covariance identity. We also provide formul as involving the Stein operator, for
densities and tails. Then we prove in Section 3 some (weighte d) functional inequalities linked to
the behavior of the Stein kernel. In Section 4 we make use of so me covariance inequalities to derive
various concentration inequalities for Lipschitz functions of a random variable having a Stein kernel.
Finally, we prove some tail bounds related to the behavior of the Stein kernel - assumed to be unique
- in Section 5.
