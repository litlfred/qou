---
doc_id: arxiv-2211.13362v2
doc_title: "Double-slit experiment revisited"
section_id: sec-006-comparison-to-the-kpm-experiment
section_title: "Comparison to the KPM experiment"
section_number: null
pages: 9-11
source_pdf: 2211.13362v2.pdf
source_sha256: 3becbeaa1135d2e1
doc_brief: "Double-slit experiment revisited — The double-slit experiment is one of the quintessential quantum experiments."
---
As mentioned in the introduction, there have been many realizations of the double-slit experiment.
One experiment of particular interest is that of KPM [10], which recorded not only the detected
positions, but also the flight times. The resulting joint position and time distribution is displayed
in Fig. 6, for three different locations of the detection screen. These experimentally obtained
distributions show qualitative similarity with the Bohmian distributions shown in Fig. 3a. However,
as we will explain here, this similarity is deceiving.
Let us first consider the details of the KPM experiment. In the experiment, metastable helium
atoms (denoted He * ) are sourced from a gas-discharge tube by firing a 15 𝜇s pulse of electric
current. A few spurious fast-moving atoms along with slower atoms with velocities ranging
between 1− 3× 103 ms−1 are produced by the source. The ejected atoms pass through a skimmer
and are collimated by a 5 𝜇m-wide slit. Further downstream, they encounter a microfabricated
double-slit structure of inter-slit separation 2Δ= 8𝜇m and slit-width𝜎𝑠 = 1𝜇m, eventually striking
the detector plate at 𝑑. He * atoms eject secondary electrons upon hitting the conductive surface
of the detector—a process assumed to take place on a time scale of 10 −12 s. These electrons are
9
carefully imaged onto a single-electron detection unit based on a chevron assembly of multichannel
plates [53]. The spatial (temporal) resolution achieved with this detector is on the order of 500 nm
(100 ns). For three different slit-screen separations𝑑, KPM recorded the detection events(𝑥,𝑦,𝑡 𝑓)
of individual atoms by repeatedly firing the source, shown in Fig. 6. Notice that the fast atoms
produce a “geometrical shadow” of the slits at the bottom of each figure [10, p. 151]. In the KPM
experiment the ToF from the source to the detection is rescaled as 𝑡𝑑 =(𝑑/𝐿)𝑡𝑓 , taken to be the
time from the passage through the slits to the screen.
While the KPM plots show a striking similarity with the Bohmian plots, there is an important
difference. We have employed the same initial wave function for each run of the DSE, whereas
the discharge tube in the KPM experiment yields a statistical mixture of wave packets of different
longitudinal velocities, thermally distributed, see [54, Fig. 4]. The mixed state character together
with the fact that the longitudinal velocities are a few thousand meters per second implies that the
temporal spread of the distributions plotted in Fig. 6 stems mainly from the spread of the velocity
distribution and not from the longitudinal spread of the initial wave function. This is also why
KPM treat the longitudinal motion as classical. (And why it makes sense to consider the rescaled
time𝑡𝑑 =(𝑑/𝐿)𝑡𝑓 to represent the time between detection and passage through the screen.) This is
unlike our Bohmian simulations, where the temporal spread in the distribution stems solely from
the longitudinal spread of the wave function.
Let us back up these statements quantitatively. For this, assume that, on the contrary, the
temporal spread is largely due to the longitudinal spread of the wave functions and that the mixed
state character (which is unavoidable) only plays a minor role. Consider for example the parameters
for Fig. 6 (c). The temporal spread in this figure is several hundreds of𝜇s. Let us assume therefore
that a single wave function can produce a spread in the detection time of at least, say, 100 𝜇s.
Taking a velocity of 10 3ms−1, this means that the longitudinal width of the wave function is of
the order of 10 5𝜇m. (This is assuming that detections take place while the support of the wave
function crosses the detection screen.) Assuming Gaussian spreading so that the width 𝜎(𝑡) at
time𝑡 is given by 𝜎(𝑡) = 𝜎
√︁
1+(ℏ𝑡/𝑚𝜎 2)2, with 𝜎 the initial width, 𝑚 = 6.64× 10−27kg the
mass of a Helium atom, and taking 𝑡 to be the time to traverse 3m, which is the distance between
the collimating slit and the detection screen (see [10, Fig. 2]), with a velocity of 103ms−1, we find
that a final width of𝜎(𝑡)= 105𝜇m implies an initial width𝜎≈ 5× 10−4𝜇m. This is much smaller
than the transverse dimensions of the setup, like the transverse width of 5 𝜇m of the collimating
slit or the distance between the slits of 8 𝜇m. Conversely, assume a longitudinal width of a wave
function of 5𝜇m at the time of passage through the collimating slit (so the same as the transverse
width of this slit). Assuming again Gaussian spreading, the width will be less than 10 𝜇m by the
time the wave function crosses the screen. This will entail a temporal spread of merely 10 −2𝜇s,
which is even smaller than the detector resolution of 10−1𝜇s.
It is also the case that the temporal spread displayed in the figure can be accounted for by the
spread of the velocities. With velocities ranging from 10 3m to 3× 103m, the associated temporal
spread is of the order of 103𝜇m, which agrees with what is shown in Fig. 6 (c).
In conclusion, in the KPM experiment the ToF is determined by the time each wave function
crosses the detection screen and does not require a quantum treatment (even though this could
of course be covered using the Bohmian dynamics). The same holds for other experimental
realizations to date. To explore the quantum aspect of the ToF in the case of the double-slit
experiment, the wave function should have a ratio of longitudinal spread and velocity that is much
larger than the temporal detector resolution. In addition, the initial velocity should be controlled as
precisely as possible to reduce velocity spread. Ultracold neutrons which have a velocity of about
1m/s may be a possibility [14]. Alternatively, one could perhaps consider a different placement of
the detection screen, as recently proposed in [77].
10
