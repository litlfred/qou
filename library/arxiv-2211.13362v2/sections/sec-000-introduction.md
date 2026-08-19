---
doc_id: arxiv-2211.13362v2
doc_title: "Double-slit experiment revisited"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2211.13362v2.pdf
source_sha256: 3becbeaa1135d2e1
doc_brief: "Double-slit experiment revisited — The double-slit experiment is one of the quintessential quantum experiments."
---
Diffraction and interference phenomena occupy a prominent place in the phenomenology of quan-
tum physics, Young’s double-slit experiment (DSE) being an archetypal example which, according
to Feynman “has in it the heart of quantum mechanics” [1]. Quantum physicists have discussed
the DSE and augments thereof, e.g., the which-way [2, 3], or the delayed-choice DSE [4], with
varying degrees of rigour. Several notable realizations employing single electrons [5, 6], neutrons
[7, 8], atoms [9, 10], and even macro-molecules [11] have been performed.
The interference fringes in a DSE are formed by the accumulation of single-particle impact
positions on a screen. What tends to be overlooked, however, is that each imprinted position with
screen coordinates(𝑥,𝑦) is associated with a definite, but random, time of flight1 (ToF)𝑡𝑓 , given by
the (measured) time of detection on the screen minus the (known) time of emission at the source.
Therefore, specifying the joint distribution 𝜌(𝑥,𝑦,𝑡 𝑓)—whose marginal
∫
d𝑡𝑓 𝜌(𝑥,𝑦,𝑡 𝑓) provides
the pattern of the fringes—is indispensable for a satisfactory account of the DSE, or any other
scattering experiment for that matter[12–15].
1Also known as arrival time, transit time, or detection time.
1
arXiv:2211.13362v2  [quant-ph]  20 Nov 2024
One might be inclined to think that the distribution 𝜌(𝑥,𝑦,𝑡 𝑓) on the screen corresponds to
|𝜓(𝑥,𝑦,𝑑,𝑡 𝑓)| 2, where𝜓(𝑥,𝑦,𝑧,𝑡 ) is the particle’s wave function at time𝑡 and𝑧=𝑑 the detection
plane. But this is incorrect because |𝜓(𝑥,𝑦,𝑧,𝑡 )| 2 is, according to Born’s rule, the distribution of
positions at a specified time 𝑡, while what is needed is a joint distribution of positions and times
detected at a specified surface.2
Nevertheless, under certain conditions, such as a narrow spread in the longitudinal direction,
i.e., in the direction towards the screen, which tend to apply to present-day experiments, the
detection times at the screen can be treated classically, leading in effect to a joint distribution that
is well approximated by|𝜓|2 [14, Eq. (9)]. This is something that needs to be taken into account
in order to really probe the quantum nature of the time distribution.
While there is no recognized observable for time in quantum mechanics, in contrast to position,
there is a multitude of (disparate) ToF proposals [16–18] (some of them being questionable [19–
25]). Barring a few works checking tunneling-time predictions, e.g., [26–30], surprisingly, so far
none of the ToF proposals have been benchmarked against experiment.
The goal of this paper is to consider the Bohmian approach to this problem, by considering the
first-passage (or hitting) distribution, i.e., the joint distribution of times and locations of particles
crossing the detection screen. While this approach ignores the possible effect of the screen itself,
this seems a natural and practicable approximation. The potential for treating ToF experiments this
way has long been recognized [13, 31–34], with numerous applications to arrival- and tunneling-
time problems; see [35–52]. In section 2, we will consider the DSE setup and simulate the evolution
of an initial Gaussian wave packet passing through the slits. The first-passage distribution of the
Bohmian trajectories is considered for three different placements of the detection screen, leading
to qualitatively different behavior. Subsequently, we consider a challenging variant of the DSE,
dubbed the dynamic DSE, in which one of the slits is shut in flight. This serves as an illustration
of the potency of the adopted approach.
On the experimental side, Kurtsiefer, Pfau, and Mlynek (hereafter KPM) [10, 53, 54] reported
the joint position distribution using metastable (i.e., electronically excited) helium atoms (see
below for further details). In [53], two marginals distributions are plotted: Fig. 1a shows the
distribution of(𝑥,𝑦) on the screen, while Fig. 1b shows that of(𝑥,𝑡 𝑓). In [10], the joint distribution
is plotted for three different distances of the detection screen, see Fig. 6. The Bohmian first-
passage distribution, shown in 3a, shows striking similarity. However, this similarity is deceptive,
as these plots concern different quantum ensembles. As we will explain in section 3, in our
Bohmian analysis we assumed an ensemble where each wave function is the same and has an
appreciable longitudinal spread. The ensemble considered by KPM, on the other hand, concerns
a mixture of wave functions whose longitudinal velocity is thermally distributed, and which do
not have appreciable longitudinal spread. So in the latter case the temporal spread is not due to
the longitudinal spread of the wave function, but due to the random initial longitudinal velocity,
allowing KPM to treat the ToF classically. This also seems to be the case in other interference
experiments to date. To actually probe the quantum nature of the time distribution, it is important to
consider similar experimental setups for which the longitudinal spread of the initial wave function
of the mixture has a considerable contribution to the temporal spread of the joint distribution.
2The conjectured quantity is not even normalizable in simple examples. Therefore, it cannot be a legitimate
probability density.
2
89
25 50 75 100 125 150 175 2000
25
50
75
100
125
150
175
200
x / pixel
y / pixel
dark
spot
hot
spot
1
25
50
75
100
125
150
0
100
200
0 100 200
Fig. 5. Contour plot of the detector sensitivity for the conﬁguration (a) of
the detector, taken from the illumination with a homogenous atomic beam.
The sensitivity at the edges falls off slowly because of clipping at the ﬁrst
aperture. The numbers at the contours indicate the (spatially smoothed)
count rate per pixel after 3 minutes of integration time in a continuous
atomic beam
image from a 12.5 µm period mesh close to the conversion
surface. The two images are taken with different angular ori-
entations of the mesh with respect to the principal directions
of the conversion surface, so that the apparent grid spacing
is different.
Another important property for a quantitative mapping
of an atomic distribution is the variation of the detector sen-
sitivity over the whole ﬁeld of view. Especially for a small
electronic magniﬁcation, we clearly see the inﬂuence of the
ﬁnite size of the extraction hole in electrode E
2. Figure 5
shows the spatial distribution of detected events with the
conversion surface illuminated homogeneously with a con-
tinuous atomic beam. Additionally to the drop of the detec-
tion efﬁciency from the center to the outer regions of the
ﬁeld of view, a dark region on our MCP as well as a hot
spot can be identiﬁed.
The ﬁnest resolved structure for an atomic beam pattern
was obtained using the large magniﬁcation setup shown in
Fig. 2b, and a slit pair with openings of 1 µm (see Fig. 6a,b).
The separation between the detector and the slit pair was
15 cm, and the atomic beam was collimated to an angular
divergence of 3.6 µrad. Furthermore, we restricted the mea-
surement to atoms faster than 30000 m/s by measuring the
arrival time of the atoms after being emitted from a pulsed
source. Therefore, diffraction of the matter wave packet of
the atoms did not cause a broadening of the pattern. With this
method, we observed two peaks with a FWHM of 1 .25 µm
and 1 .29 µm, respectively. Within our experimental accu-
racy of position discretisation, the observed widths can be
explained as the geometrical shadow in the atomic beam
from the 1 µm wide slits, resulting in an expected width of
1.19 µm.
A critical point for reaching this resolution is a careful
alignment of the investigated distribution with respect to the
principal axis of the detector.
Fig. 6a,b. Finest structure observed with the atom detector in the conﬁgura-
tion b. The image was formed as a shadow of a double slit in conﬁguration
similar to the one shown in Fig. 3, where only Helium atoms with a ve-
locity higher than 30000 m/s were taken into account with a time-of-ﬂight
technique. Part a shows the actual beam image of the double slit, and b is
an integration along the slit direction y within the dashed lines in a. The
length calibration in x-direction was obtained from the known separation
of the two slit images of 8.8 µm. The solid line shows a ﬁt of two Gaussian
distributions to the measured distribution (squares). The obtained FWHM
values give an upper bound for the spatial resolution of the whole detection
scheme of 1.25 µm
0 100 200
0
1
2
x / pixel
tf / ms
0 100 200
0
100
200
x / pixel
y / pixel
(a)
20 µm
(b)
Fig. 7. Atomic interference pattern from a Y oung’s double slit experiment.
Part a shows the spatial distribution observed with the 2D-detector, where
only atoms with velocities between 2400 and 3100 m/s are selected with
a time-of-ﬂight technique. The drop in detector sensitivity due to the lim-
ited entrance aperture can clearly be seen. A sum over the counts along
the y-direction within the dashed lines is shown in b as a function of the
time-of-ﬂight t
f . The shadow of the double slit can be identiﬁed for the
very fast atoms, whereas for smaller velocities corresponding to a deBroglie
wavelength in the range of 50 pm, the diffraction pattern with the charac-
teristic velocity dispersion appears. The dashed lines indicate the range for
t
f used in part a
4 Applications
Probably one of the most striking phenomena in the ﬁeld of
atom optics is the observation of the wavelike behavior of
the atomic motion in an atom interferometer. The interfer-
ometers set up for fast atoms up to now often suffer from the
low atomic ﬂux, limiting the accuracy of any measurement
due to drifts over long integration times. Our main interest
in developing such a detector was therefore getting an easy
access to atomic beam structures on the scale of 1 µm for
atom interferometry purposes, with a possibility to resolve
the arrival time of each atom with a sufﬁcient accuracy.
Figure 7 shows an interference pattern from a double slit
experiment, using a double slit interferometer with a slit sep-
aration of 8 µm and a slit width of 1 µm like in [5]. The dou-
(a) (b)
Figure 1: Figures from the KPM experiment [53] (reproduced with permission). (a) Double-
slit interference pattern observed on a screen after many single-atom detection events. (b) Joint
distribution of the ToF𝑡𝑓 and the𝑥-screen-coordinate of the detection events. Impact positions of
atoms arriving in the𝑡𝑓 range indicated by the dashed lines in (b) were accumulated to produce (a).
A fraction of very fast atoms emanating from the source cast a shadow of the slits at the bottom.
