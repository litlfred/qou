---
doc_id: arxiv-1202.0461v1
doc_title: "Draft version October 11, 2018 DOUBLE DEGENERATE MERGERS AS PROGENITORS OF HIGH-FIELD MAGNETIC WHITE DWARFS"
section_id: sec-002-2-the-stellar-dynamo
section_title: "THE STELLAR DYNAMO"
section_number: 2
pages: 1-3
source_pdf: 1202.0461v1.pdf
source_sha256: 656a2ea80ef2e25c
doc_brief: "Draft version October 11, 2018 DOUBLE DEGENERATE MERGERS AS PROGENITORS OF HIGH-FIELD MAGNETIC WHITE DWARFS — High-ﬁeld magnetic white dwarfs have been long suspected to be the result of stellar"
---
The merger of two degenerate cores is the ﬁnal des-
tiny of the evolution of a sizable fraction of binary sys-
tems. Three-dimensional simulations of the merger pro-
cess (Guerrero et al.
2004; Yoon et al.
2007; Lor´en–
Aguilar et al. 2009) indicate that the remnant of the co-
alescence of two white dwarfs consists of a central white
dwarf which contains all the mass of the primary. On top
2
of it a hot corona, which is made of approximately half
of the mass of the disrupted secondary, can be found.
Finally, surrounding this compact remnant a rapidly ro-
tating Keplerian disk is formed, containing nearly all the
mass of the secondary which has not been incorporated
to the hot corona. According to these calculations little
mass (∼10−3 M⊙) is ejected from the system during the
merger. The structure of the remnant of the coalescence
is illustrated in Fig. 1.
The existing simulations show that the temperature
gradient in the hot corona is high, and consequently the
corona is convective.
We computed the boundaries of
the convective region using the Schwarzschild criterion,
and we found that the inner and outer edges of the con-
vective region are located at radii R ≈0.012 R⊙, and
R ≈0.026 R⊙, respectively, and that the total mass in-
side this region is ∼0.24 M⊙(see Fig. 1). Moreover, this
region rotates diﬀerentially, and is prone to magneto-
rotational instability.
Assuming energy equipartition,
the resulting αω dynamo produces a magnetic ﬁeld
B2/8π ≈ρ(ωR)2/2. For the typical values found in the
simulations of Lor´en–Aguilar et al. (2009), the magnetic
ﬁeld amounts to B ∼3.2 × 1010 G. Thus, the energy
available in the convective corona is suﬃciently large to
produce strong magnetic ﬁelds. We note that even in
the case in which only 0.1% of the total energy of the
convective shell is invested in magnetic energy the ﬁelds
produced in this way are of the order of 107 G, a value
typical of high-ﬁeld magnetic white dwarfs. We also note
that there are very few white dwarfs with magnetic ﬁelds
larger than 109 G, and that when these ﬁelds are ob-
served, these are conﬁned to spots on their surfaces.
For this mechanism to be eﬃcient at producing the
observed magnetic ﬁelds, the dynamo must work for sev-
eral convective turnovers before the energy of the hot
corona is radiated away. The temperature of the corona
is so high that is preferentially cooled by neutrino emis-
sion.
The neutrino luminosity of the corona is Lν ∼
4.0 × 102 L⊙, while the total thermal energy of the non-
degenerate material in the corona is U ∼8.8 × 1048 erg.
Hence, the convective shell lasts for τhot ∼1.8 × 105 yr.
The convective turnover timescale is τconv ≈HP /vconv,
where HP ≈2.7×108 cm is the pressure scale height and
vconv ≈8.0 × 107 cm/s is the convective velocity. Thus,
τconv ∼3.3 s, and during the lifetime of the hot corona
the number of convective cycles is suﬃciently large. Con-
sequently, the αω mechanism is able to produce a strong
magnetic ﬁeld. We also note that if the duration of the
convective shell is substantially smaller than that esti-
mated here, large magnetic ﬁelds can still be produced.
Speciﬁcally, even assuming durations 103 times smaller
than that previously estimated, the number of convective
cycles would still be enough to produce magnetic ﬁelds
comparable to those observationally found in high-ﬁeld
magnetic white dwarfs. We thus conclude that the stel-
lar dynamos produced in the aftermath of the merger of
two degenerate cores can produce magnetic ﬁelds of the
order of 107 G. From now on we adopt this value (typical
of high-ﬁeld magnetic white dwarfs) as a ﬁducial value
for the rest of the calculations.
Once the magnetic ﬁeld is established we need to know
if it can diﬀuse outwards, to the surrounding disk, or
inwards, to the degenerate primary.
To this end we
Fig. 1.— Dynamo conﬁguration in a white dwarf merger. Tem-
perature (solid line, left scale) and rotational velocity (dashed line,
right scale) proﬁles of the ﬁnal remnant of a white dwarf merger
as a function of radius are shown for the case of a binary system
composed of two stars of 0.6 and 0.8 M⊙. In our simulations ap-
proximately half of the mass of the disrupted secondary (∼0.3 M⊙)
is accreted onto the primary, while the rest of the mass goes to form
the Keplerian disk, which extends up to ∼0.3 R⊙. The tempera-
ture of the central white dwarf depends on the initial temperature
of the coalescing white dwarfs (Yoon et al. 2007; Lor´en–Aguilar et
al. 2009). However, the temperature of the hot corona is remark-
ably similar in all the simulations, T ≈8.7 × 108 K. The central
spinning white dwarf rotates as a rigid body with a rotational ve-
locity ω ∼0.26 s−1, and the corona rotates diﬀerentially, with a
peak rotation rate ω ∼0.33 s−1. These velocities arise from energy
and angular momentum conservation, since little mass is ejected
from the system, so the orbital angular momentum of the binary
system is invested in spinning up the remnant, while the available
energy is primarily invested in heating the corona. The location of
the convective region is displayed by the shaded area.
solved the diﬀusion equation (Jackson 1998; Wendell et
al. 1987):
∂⃗B
∂t = −⃗∇×
 c2
4πσ⃗∇×⃗B −⃗v ×⃗B

(1)
being σ the magnetic conductivity, for which we used the
most up-to-date prescription (Cassisi et al. 2007), while
the rest of the symbols have their usual meaning. We
ﬁrst integrated the diﬀusion equation for the surround-
ing disk using cylindrical coordinates, adopting the ve-
locity ﬁeld and density and temperature proﬁles resulting
from our SPH simulations (Lor´en–Aguilar et al. 2009).
The initial condition adopted here is⃗B(0) =⃗0, while
we also imposed the boundary condition ∂⃗B/∂t = 0 at
the outer edge of the disk. We used a Crank-Nicolson
integration scheme with variable coeﬃcients (Dautray &
Lions 2000) which turns out to be stable. We found that
the timescale for diﬀusion of the magnetic ﬁeld across
the disk is τdisk ∼2.0 × 1011 yr. We did the same calcu-
lation, this time using spherical coordinates, to estimate
the penetration of the magnetic ﬁeld in the dense, de-
generate primary.
The use of spherical coordinates is
perfectly justiﬁed because the departures of the com-
pact primary from sphericity are very small.
For this
3
calculation we followed the procedure outlined in Wen-
dell et al.
(1987).
In this case the electrical conduc-
tivity is totally dominated by degenerate electrons, and
depends on the adopted temperature of the isothermal
white dwarf. If a temperature T ≈7.6 × 107 K is taken
(Lor´en–Aguilar et al. 2009) the diﬀusion timescale turns
out to be τWD ∼4.3 × 109 yr. Since this timescale de-
pends on the adopted initial temperature we computed,
using an up-to-date stellar evolutionary code (Renedo et
al. 2010), a cooling sequence for a white dwarf of the
mass, 1.1 M⊙, and chemical composition of the remnant,
a carbon-oxygen core. The time to cool from 7.6×107 K
to a value typical of ﬁeld white dwarfs (say 3.0 × 106 K)
is very short, τcool ∼3.0 × 107 yr. Hence, we can safely
assume that as the white dwarf cools, the rapid increase
of the electrical conductivity does not allow the magnetic
ﬁeld to penetrate in the degenerate core of the primary,
and remains conﬁned to the surface layers.
Our model naturally predicts that the masses of high-
ﬁeld magnetic white dwarfs should be larger than average
and that they should be observed as single white dwarfs,
as observationally found — see, for instance, Valyavin
& Fabrika (1999). However, high-ﬁeld magnetic white
dwarfs are generally found to be slow rotators (Wick-
ramasinghe & Ferrario 2000). This apparent contradic-
tion of the model can be easily solved. If the rotation
and magnetic axes are misaligned, magneto-dipole radi-
ation rapidly spins down the white dwarf — see, how-
ever, Timokhin (2006) and Spitkovsky (2006), where the
time evolution of magnetospheres for axisymmetric and
oblique rotators is described in detail. The evolution of
the rotational velocity when both axes are misaligned
(Benacquista et al. 2003) is:
˙ω = −2µ2ω3
3Ic3 sin2 α,
(2)
where I is the moment of inertia of the white dwarf,
α is the angle between the magnetic and rotation axes
and µ = BR3
WD. Thus, the spin-down timescale is sim-
ply τMDR = ω/2 ˙ω. Adopting the values resulting from
our SPH simulations (Lor´en–Aguilar et al. 2009) we ob-
tain τMDR ∼2.4 × 108/ sin2 α yr, for a ﬁeld strength
B = 107 G. Hence, if both axes are perfectly aligned the
remnant of the coalescence will be a high-ﬁeld, rapidly
rotating magnetic white dwarf. On the contrary, if both
axes are nearly perpendicular magneto-dipole radiation
eﬃciently brakes the remnant. Consequently, the very
young, hot, ultramassive, slowly rotating magnetic white
dwarfs 1RXS J0823.6−2525 and PG 1658+441, which
have ﬁelds ∼3.5 × 106 G can be accommodated in our
model. For instance, PG 1658+441 has an eﬀective tem-
perature Teﬀ∼30 000 K and a mass M ∼1.3 M⊙
(Dupuis et al.
2003), which corresponds to a cooling
age of ∼3.7 × 108 yr, while the time needed to brake
the white dwarf equals to ∼8.4 × 107 yr if sin α = 1 is
adopted. Thus, our model can account for the slow ro-
tation rate of PG 1658+441, provided that the rotation
and magnetic axes are misaligned. We also note at this
point that given the small radii — or, equivalently, the
small radiating surfaces — of massive white dwarfs, their
cooling ages increase markedly for eﬀective temperatures
smaller than log Teﬀ≲4.7.
On the other hand, rapidly rotating magnetic white
dwarfs — of which an example is RE J 0317−853, a very
massive (∼1.3 M⊙) white dwarf belonging to a wide bi-
nary system (K¨ulebi et al.
2010) — could be the re-
sult of nearly equal-mass mergers in which both axes are
aligned. In this case no Keplerian disk is formed, so these
white dwarfs will not show infrared excesses. If, on the
contrary, the masses of the coalescing white dwarfs are
diﬀerent, the axes are not aligned, and the disk is able
to survive for long enough times, a second-generation
planetary system could be eventually formed (Garc´ıa–
Berro et al. 2007) and tidal disruption and accretion of
minor planets may contaminate the atmosphere of the
white dwarf, resulting in magnetic DAZ or DAZd white
dwarfs possibly showing infrared excesses. Examples of
such white dwarfs are NLTT 10480 (Kawka & Vennes
2011) and G77−5018 (Farihi et al. 2011), for which a
satisfactory explanation is still lacking.
The geometry of the surface magnetic ﬁelds of white
dwarfs has been investigated over the years using spectro-
polarimetric observations. The available wealth of obser-
vations shows that, in almost all cases, magnetic white
dwarfs have ﬁelds deviating strongly from dipolar struc-
ture.
In particular, it appears that in most cases the
geometry of the surface magnetic ﬁeld corresponds to
quadrupolar or higher multipoles — e.g., PG 1031+234
(Schmidt et al. 1986), REJ 0317−855 (Ferrario 1997),
HE 0241−0155 (Reimers et al.
2005), HE 1045−0908
(Euchner et al.
2005), or PG 1015+014 (Euchner et
al. 2006). This means that the toroidal component of
the magnetic ﬁeld must be stable, and that a poloidal
component should also be present. Our mechanism can
also qualitatively reproduce these observations. Indeed,
in the αω mechanism, convection is responsible for the
generation of poloidal ﬁelds, whereas rotation is respon-
sible for the generation of toroidal ﬁelds.
Speciﬁcally,
the energy available to generate the poloidal ﬁeld com-
ponent is ρv2
conv/2 ∼4.0 × 1020 erg, which is ∼10%
of the energy available to build the toroidal component,
ρ(ωR)2/2 ∼5.5 × 1021 erg. Thus, we expect that the
magnetic ﬁeld generated by the fast rotating convective
shell will have both toroidal and poloidal ﬁeld compo-
nents. Moreover, it is well known that purely toroidal
ﬁelds are unstable due to Tayler (1973) instability. How-
ever, the existence of a small poloidal component is a suf-
ﬁcient condition for stability. Actually, recent numerical
studies (Braithwaite 2009) show that the energy stored
in the poloidal ﬁeld component can be as high as 80% of
the total magnetic energy, and that even poloidal com-
ponents 10−6 times smaller than the toroidal one are
enough to warrant stability. Thus, toroidal ﬁelds gen-
erated by the rotating, convective shell produced in the
merger of two double degenerates are stable, and more-
over we expect that the magnetic ﬁelds generated in this
way will have a complex geometry, in agreement with
observations.
