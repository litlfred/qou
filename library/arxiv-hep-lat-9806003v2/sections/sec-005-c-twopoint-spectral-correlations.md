---
doc_id: arxiv-hep-lat-9806003v2
doc_title: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra"
section_id: sec-005-c-twopoint-spectral-correlations
section_title: "Two–Point Spectral Correlations"
section_number: C
pages: 6-10
source_pdf: 9806003v2.pdf
source_sha256: e34739e703aae6db
doc_brief: "Statistical analysis and the equivalent of a Thouless energy in lattice QCD Dirac spectra — 8 sections: INTRODUCTION; COMPLETE DIRAC SPECTRA IN SU(2) GA; DATA ANALYSIS"
---
In an interval of length L in units of the mean level spacing, the mean number of eigenvalues should be equal to L,
see Eq. (12). The variance of this number is deﬁned by [30]
Σ2(L) = ⟨(L −nα(L))2⟩.
(15)
Thus, an interval of length L contains on average L ±
p
Σ2(L) levels. For uncorrelated Poisson spectra Σ2(L) = L.
RMT predicts for the number variance stronger correlations, namely Σ2(L) ∼log L.
Another important quantity is the spectral rigidity ∆3(L), deﬁned as the least square deviation of the staircase
function from the straight line [30],
∆3(L) =
*
1
LminA,B
Z α+L
α
dξ(N(ξ) −Aξ −B)2
+
.
(16)
Since it can be expressed as an integral over the number variance
∆3(L) = 2
L4
Z L
0
dr(L3 −2L2r + r3)Σ2(r) ,
(17)
it is smoother than Σ2(L).
The number variance can be expressed as an integral of the two–point cluster function Y2(r) [30], which depends
for translational invariant spectra only on the diﬀerence r = |ξ2 −ξ1| between two levels at ξ1 and ξ2,
Σ2(L) = L −2
Z L
0
(L −r)Y2(r)dr .
(18)
The cluster function is related to the two–point correlation function X2(r) which measures the probability density to
ﬁnd two levels at a distant r by X2(r) = 1 −Y2(r). In contrast to P(s), these two levels are not restricted to adjacent
ones.
In Fig. 5, number variance and spectral rigidity for scales up to L = 20 and L = 100, respectively, are shown.
Lattice data and RMT predictions agree remarkably well, even the oscillations in Σ2(L) are accurately reproduced.
Naturally, previous analyses [11] with smaller data sets have less statistical signiﬁcance.
Two–point cluster and
correlation function which usually are not accessible in data analysis are shown in Fig. 6. Again, the agreement is
impressive.
Beyond this scale there are considerable deviations of ∆3(L) as well as of Σ2(L) from RMT predictions which
depend on the unfolding procedure used. We mention that on general grounds one can show that any scales in Σ2(L)
and ∆3(L), say LΣ and L∆, respectively, are related by L∆: LΣ = 4 : 1, or so [1], see Fig. 5. Thus, any deviations
from RMT behavior appear at smaller L in Σ2(L) as compared to ∆3(L).
If we unfold with the ensemble staircase function N(λ), we obtain the following results. The number variance can
be seen in Fig. 7. Data for diﬀerent lattice sizes and diﬀerent gauge couplings are shown in comparison to the RMT
predictions for some regions of the spectra. We ﬁnd that the point where the deviation sets in, scales with the square
root of the lattice volume,
λRMT
D
≈C
√
V .
(19)
The numerical constant C is approximately given by C ≈0.3. This should be compared with the result obtained in
[18] for the microscopic region. There, the scaling λRMT/D ∼0.3 . . . 0.7
√
V was found. This is independent of the
region of the spectra we consider and of the coupling strength β. This is shown in Fig. 7. There diﬀerent regions
of the spectra are considered, each corresponding to diﬀerent values of ρ(λ), see Fig. 1. The results are the same.
Furthermore, the deviation points for diﬀerent β appear to coincide, whereas the local average density depends on
6
the gauge coupling, ρ(λ) = ρ(λ, β), see Fig. 1. The scaling relation (19) can nicely be seen from Fig. 8, in which the
L axes of Fig. 7 is rescaled with
√
V . We see that the crossover from RMT to non–universal behavior appears to be
the same for all lattice sizes independent of β. But the slope varies for diﬀerent couplings and regions of the spectra.
When we use windowing instead, we get the same results as obtained by ensemble unfolding. But the data points
scatter more compared to Figs. 7 and 8.
The importance of a proper choice of the unfolding method becomes manifest as the above picture changes drastically
if we unfold each conﬁguration separately. As displayed in Fig. 9, the polynomial unfolding leads to an overshooting
of the data over the predictions but further out, compared to ensemble unfolding, while in the Gaussian as well as in
the local case Σ2(L) saturates. Note the diﬀerent scale compared to Fig. 7 and also the diﬀerence in scale between
number variance and spectral rigidity, as mentioned above. The result of the polynomial approach does not depend on
the degree n of the polynomial. Furthermore we ﬁnd no scaling with
√
V for the deviations of polynomial unfolding,
see Fig. 10. The deviation point appears to be the same for diﬀerent lattice sizes. The saturation of the small lattices
is due to the limited number of eigenvalues in the considered energy range. The same picture arises for the number
variance: overshooting for the polynomial, saturation for Gaussian and local approach. The general tendency of this
results are already obtained for each conﬁguration separately, but the data points scatter. After averaging over all
conﬁgurations the scattering becomes much smaller, see Figs. 5 and 9.
D. Higher Order Spectral Correlations
The wealth of data allows us to go beyond a previous analysis [12] of higher moments of the eigenvalue partition,
µk(L) = ⟨(L −nα(L))k⟩.
(20)
We notice that µ2(L) = Σ2(L). The skewness and the excess [30] are deﬁned by
γ1(L) = µ3(L)µ2(L)−3/2
(21)
and
γ2(L) = µ4(L)µ2(L)−2 −3 ,
(22)
respectively. The comparison of RMT predictions with lattice data for these both quantities in Fig. 11 again shows
very good agreement.
The measures γ1(L) and γ2(L) only contain a small amount of information of the spectral correlations. Moreover,
γ1(L) and γ2(L) also involve lower order correlations: γ1 is a combination of the two– and the three–point correlator,
Y2(r) and Y3(r1, r2), and γ2 involves in addition the four–point correlator Y4(r1, r2, r3). The representation of the
moments in terms of integrals over the correlators reads
µ3(L) = L −6
Z L
0
(L −r)Y2(r)dr −6
Z L
0
dr1
Z L−r1
0
dr2(L −r1 −r2)Y3(r1, r2)
(23)
and
µ4(L) = L −(14 −12L)
Z L
0
(L −r)Y2(r)dr + 12
"Z L
0
(L −r)Y2(r)dr
#2
+ 36
Z L
0
dr1
Z L−r1
0
dr2(L −r1 −r2)Y3(r1, r2)
−24
Z L
0
dr1
Z L−r1
0
dr2
Z L−r1−r2
0
dr3(L −r1 −r2 −r3)Y4(r1, r2, r3) .
(24)
Obviously, by analyzing γ1(L) and γ2(L), one cannot easily estimate to what extent the three– and the four–point
correlators themselves obtained from the lattice calculations follow the predictions of RMT.
Here, the three– and the four–point cluster functions, Y3(r1, r2) and Y4(r1, r2, r3) are written as functions of the
arguments ri (i = 1, 2, 3) which are deﬁned terms of the original arguments ξi (i = 1, 2, 3, 4) by
r1 = ξ2 −ξ1,
r2 = ξ3 −ξ2,
r3 = ξ4 −ξ3.
(25)
7
We constructed from the data the two–point and the three–point correlation functions X2(s) and X3(s1, s2) and
the corresponding cluster functions Y2(s) and Y3(s1, s2). Here, for convenience, we redeﬁned the arguments for the
three–point correlators as follows:
s1 = ξ2 −ξ1 = r1,
s2 = ξ3 −ξ1 = r1 + r2.
(26)
The results for X3(s1, s2) and Y3(s1, s2) are plotted with error bars in Fig. 12 for some given values of s1. The results
do not depend on unfolding. In the construction of these correlators, we ﬁrst performed a spectral average by using
the translational invariance due to unfolding, and then averaged over the ensemble. The errors for X3(s1, s2) and
Y3(s1, s2) were estimated as the variance of the ensemble ﬂuctuations. Once more, very good agreement with the
RMT predictions for X3(s1, s2) is found, apart from a small systematic deviation which we believe can be understood
as follows. From the relation between X3(s1, s2) and X2(s)
X3(s1, s2) = Y3(s1, s2) −2 + X2(s1) + X2(s2) + X2(s1 −s2),
(27)
one has
X3(s1, s2)|s2→∞= X2(s1).
(28)
Therefore, even a small point–deviation of the two–point correlator at s1 from the theoretical predictions can result
in a systematic deviation of the whole curve X3(s1, s2) versus s2 for this given s1. For Y3(s1, s2), the quality of the
agreement with RMT is only slightly reduced, but still remarkable. In addition to the systematic deviation, one can see
some random ﬂuctuations around the theoretical curves. This is because Y3(s1, s2) is the disconnected correlator, and
it should represent the true three–point correlation, while X3(s1, s2) also contains the two– and one–point functions.
They play a dominate role and are in good agreement with the corresponding GSE predictions. We notice that this
analysis was only possible due to the extremely higher number of levels available.
E. Qualitative discussion of the deviations for conﬁguration unfolding
Using ensemble unfolding, we ﬁnd deviations from RMT behavior, which scale with the square root of the volume
according to the theoretical predictions. But as we unfold each conﬁguration separately this eﬀect vanishes. There
are still deviations left but none of them show a
√
V scaling law. Moreover, we have a dependence of the results on
the unfolding approach.
Concerning local and Gaussian unfolding, an explanation seems to be easy at hand. As mentioned above, both
procedures have an intrinsic, artiﬁcial, scale. In units of the mean level spacing it has the value L ≈100 for V = 164
in both cases. This is approximately where the saturation of the statistics seen in Fig. 9 sets in. We conclude that
this artiﬁcial scale causes Σ2(L) and ∆3(L) to saturate. In other words, both approaches are not capable to allow
statements at scales L >∼100. Nevertheless, both approaches do not show a behavior as shown in Figs. 7,8 for L < 100.
On the other hand, the polynomial unfolding also deviates from RMT predictions, see Fig. 10. As this approach
does not contain an additional scale, we can rule out eﬀects like the one discussed above. The question is, whether
the deviations in Fig. 10 are due to a Thouless energy or if they have another origin.
The ﬂuctuating part of the integrated level density Nﬂuc(λ) should be of order O(1), as mentioned above. In the
upper part of Fig. 13 the diﬀerence between the real staircase function and the smooth polynomial staircase function,
N(λ) −Npoly(λ), for one speciﬁc conﬁguration is plotted.
This picture remains qualitatively the same whatever
conﬁguration is chosen. The polynomial ﬁts have a systematic deviation from a smooth behavior larger than O(1).
The diﬀerence between the ensemble staircase and polynomial ﬁt N(λ)−Npoly(λ) is shown in the lower part of Fig. 13.
A polynomial of degree n = 3 gives the same result as n = 4. To obtain a better insight in this obviously not universal
behavior, we calculate the power spectrum
F(f) =
Z ∞
−∞
dλe2πifλK(λ1, λ2, λ) d
dλ (N(λ) −Npoly(λ)) .
(29)
By construction, the derivative in the integrand gives the ﬂuctuations of the level density. The window function
K(λ1, λ2, λ) has to be introduced because we only have a ﬁnite interval of eigenvalues in the Fourier transform over
the whole real axis. It is zero outside the interval λ1 ≤λ ≤λ2. The choice is not unique inside [31]. Thus, the Fourier
transform is a convolution of the transforms of N(λ) −Npoly(λ) and K(λ1, λ2, λ). In order to reduce the inﬂuence of
the Fourier transform of K(λ1, λ2, λ) on the results as far as possible, we use a triangle window [31]. The result is
shown in Fig. 14. In the right part one sees the Fourier transform of the ensemble averaged density. Only the very ﬁrst
8
peak is left, both for polynomial of degree n = 4 and n = 5. The latter is reduced in amplitude. On the left side the
transform of an arbitrary chosen conﬁguration is plotted. The ﬁrst peaks are reduced in amplitude again for n = 5,
whereas the remaining ones are the same for both degrees. We conclude that only the ﬁrst peak, corresponding to the
long wave part of Fig. 13, is common to all conﬁgurations. All others ﬂuctuate from conﬁguration to conﬁguration.
We conclude that the average level density ρave(λ) and thus the average integrated level density Nave(λ) consist of
two parts, namely a very smooth polynomial–like part and another, non–universal, part,
Nave(λ) = Npoly(λ) + Nosc(λ) .
(30)
We stress again that the existence of a polynomial–like smooth part is suggested by pertubative and 1/Nc expansions
of the QCD level density [26,27]. It is expected to be governed by the available phase space: for free fermions the
spectral density is given at |λ| →∞by ρave(λ) = NcV |λ|3/4π2 [32], where Nc is the number of colors. This also
holds in a 1/Nc expansion of the interacting theory on scales which are large compared to the hadronic scale [27].
This is the region we investigated in the spectra, as the eigenvalues are given in units of the inverse lattice spacing
as a−1 ≈10 fm−1 ≈2 GeV, see Figs. 1 and 13. This is why we tried to approximate the average level density by a
function which is as smooth as a polynomial.
The additional structure of the level density appears to have similarities to oscillations, see Figs. 13 and 14. Thus,
we refer to it as “oscillatory part”, Nosc(λ). This oscillatory part explains the diﬀerent behavior of ∆3(L) and Σ2(L)
for large L for diﬀerent unfolding methods. The polynomial unfolding is clearly unable to remove the oscillations
and ﬁts only Npoly(λ). Thus, the oscillatory part is still present in the unfolded spectrum. The presence of these
oscillations leads to values for ∆3(L) larger than predicted by RMT, because a ﬁt to a straight line can only be done
in a less accurate manner. In contrast to that, the Gaussian and the local unfolding is capable to ﬁt Npoly(λ) and
part of Nosc(λ). However, it is not clear whether the ﬁt to the oscillatory part is done completely or if, on the other
hand, it does not smooth out part of the universal ﬂuctuations, i.e. overﬁts the data points. But, because of the
saturation of Σ2(L) and ∆3(L), see Fig. 9, we think that probably the latter happens.
However, as argued above, since we expect the physical density to be as smooth as a polynomial, the oscillatory
part is likely to be a lattice artifact. This is suggested by Figs. 13 and 14 which show that these oscillations live
on the scale of the inverse lattice spacing 1/a. As |λ| cannot be arbitrarily large in lattice gauge theory, due to an
ultraviolet cutoﬀin momentum for ﬁnite lattice spacing a, the increase of the density is disturbed by lattice artifacts.
For the large lattices, i.e. V = 164, the deviations due to lattice artifacts set in at approximately the same scale as
the expected equivalent of a Thouless energy. This can be seen from the
√
V scaling of the smaller lattices. A rough
estimate gives λRMT/D ≈30 for V = 164 for Σ2(L). Therefore one should be careful with the determination of the
deviation point for large lattices in the bulk of the spectra. After removing this part from the data, we ﬁnd for Σ2(L)
reasonable agreement with the RMT prediction up to at least L ≈300 and with some uncertainties even to L ≈500,
see Fig. 15. Because of the complicated structure of the average level density it is not possible to make any statement
beyond this scale. In chaotic billiards, so–called bouncing ball modes generate eﬀects which are similar to the ones
here [29]. In that case, however, an analytical prediction for the oscillatory behavior was at hand. Such a result is
also highly desirable in our case. It would be needed to furnish our phenomenological removal of the oscillations with
a theoretical justiﬁcation.
In any case, we may use the information displayed in Fig. 14 to phenomenologically remove the oscillatory part. We
cut the power spectrum at a certain interval, back transform the remaining peaks in the frequency interval [0, fcut]
and subtract the smooth oscillatory part of the integrated level density obtained in this manner. We do this for
each conﬁguration separately. This procedure changes the result of the statistical analysis in a crucial way, as can
be seen from Fig. 15. There, the results for spectral measures are shown for diﬀerent choices of fcut. Because only
the very ﬁrst peak is common to all spectra whereas higher frequencies appear to be speciﬁc for each conﬁguration,
a choice of fcut > 3.0 · (2a) is actually too large.
This manifests in a saturation of the statistics in Fig. 14 for
fcut = 7.0 · (2a), 10.0 · (2a). A cutoﬀof fcut = 1.5 . . .3.0 · (2a) seems to be the best choice, but we are not able to
give an exact value. This ﬁgure also shows a comparison between β = 2.4 and β = 2.5 for V = 164. Both values of
β give almost the same result. The procedure also removes the slight diﬀerences seen in Fig. 3 for the polynomials
for L >∼200. From all this, we conclude that the deviations in Fig. 10 are due to a non polynomial–like part in the
average level density and not due to an equivalent a Thouless energy.
A possible way to circumvent the problems encountered by lattice artifacts is windowing as discussed in Sec. III A 3.
However, this works only if the size of the windows δλ is at least so small that the oscillations of Fig. 13 are not
important, i.e. δλ ≪a−1. Another way might be ensemble unfolding, Sec. III A 1. As the lattice artifacts are seen in
each conﬁguration as well as in the average integrated level density this approach might remove the oscillations. But
it is by no means clear if it really does, especially for large interval lengths. As both approaches give similar results for
small lattices, V ≤104, for intervals L <∼20, we conclude that the artifacts are not important on these scales. This is
supported by the observations that deviations due to them set in at L ≈25 for polynomial unfolding, independently
9
of the lattice size, see Fig. 10. Thus, these artifacts become important for analysis of larger lattices, i.e. V = 164, and
for even larger ones in future examinations.
From all this we conclude that we do not see an equivalent of a Thouless energy if we unfold each conﬁguration
separately. This is in complete contrast to the results gained by ensemble unfolding. The former surely removes the
ﬂuctuations in Fig. 2, whereas the latter does not. We conclude that this ﬂuctuation with respect to the ensemble
already contains the information needed to determine the Thouless energy. After removing this information it seems
that there is no further information in the spectra, i.e. we ﬁnd agreement with RMT on huge scales.
