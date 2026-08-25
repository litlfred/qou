---
doc_id: arxiv-hep-th-9506138v1
doc_title: "Black Hole Complementarity vs. Locality"
section_id: sec-002-3-the-nice-slice-and-string-field-theory
section_title: "The Nice Slice and String Field Theory"
section_number: 3
pages: 8-13
source_pdf: 9506138v1.pdf
source_sha256: bb85afba0530402c
doc_brief: "Black Hole Complementarity vs. Locality — 8 sections: Introduction; The Nice-Slice Argument; The Nice Slice and String Field Th"
---
Although the nice-slice argument seems very general, we wil l present evidence from
string theory that it fails. A key assumption that goes into t he nice-slice argument is that
the underlying microscopic theory is approximately a local ﬁeld theory. Speciﬁcally, it
assumes that any nonlocality which results from the non-zer o size of strings is limited to
small space-like separations, but this is incorrect, as we s hall see later on.
7
The analysis begins by considering two spacetime points, x1 and x2, which lie on a
ﬁxed nice slice Σ t corresponding to Schwarzschild timet. The time t is chosen large, but not
so large that an appreciable amount of evaporation has occur red. The point x2 lies behind
the horizon, and could be chosen to lie on the hyperbola UV =R2. It may be thought of as
a point near the trajectory of a low-energy particle which ha s fallen through the horizon at
some early time. Point x1 lies outside the event horizon and should be associated with the
stretched horizon. According to the principle of black hole complementarity, an observer
who remains permanently outside the black hole sees the infa lling information stored in
this region. The point x1 may be chosen according to the following procedure. First,
consider the nice slice Σ 0, and pick a point outside the event horizon, for example, the
point U = U0 < 0, V = V0 > 0. Now push the point forward in time along a timelike
Killing vector until it arrives at the point
U1 =U0e−t/4GM
V1 =V0et/4GM ,
(3.1)
which lies on Σ t. As t increases, the spacelike separation between x1 and x2 grows like
exp(t/4GM ).
We will assume that some form of string ﬁeld theory allows us t o obtain component
ﬁelds φA(x) for each mass eigenstate of the string. A low-energy eﬀecti ve ﬁeld ˆφA(y) can
then be deﬁned by
ˆφA(y) =
∫
dDxf (x −y)φA(x), (3.2)
where the test function f is assumed to be smooth enough to eliminate variations of φA
on scales smaller than some cutoﬀ scale ε in an appropriate local frame. If a low-energy
observer at point ( U0,V 0) uses a test function f , then a low-energy observer at point x1
uses a test function which is obtained from the test function f by boosting along the
timelike Killing vector. Using the notation of equation (3. 1), this function is
f (x −x1) = f
(
et/4GM (U −U1),e −t/4GM (V −V1),⃗ x−⃗ x1
)
. (3.3)
The assumption of locality of the nice-slice theory can be te sted by calculating the
commutators of low-energy nice-slice ﬁelds obtained from l ight-front open bosonic string
ﬁeld theory. For technical reasons, we are unable to carry ou t such a calculation in the
Schwarzschild geometry. In the limit of large black hole mas s, however, the spacetime
region of interest is well approximated by ﬂat Minkowski spa ce, where the computations
are straightforward.
8
Using light-front coordinates
x± = 1√
2
(
x0 ∓xD−1)
, (3.4)
in which the Minkowski line element is
ds2 = −2dx+dx− +δijdxidxj, i,j ∈ {1,...,D − 2}, (3.5)
the light-front time x+ corresponds to U , the longitudinal direction x− corresponds to V ,
and the horizon becomes the planar lightlike hypersurface x+ = 0. A set of nice slices can
be constructed in Minkowski spacetime in exactly the same wa y as the black hole spacetime,
except that we must replace asymptotic time t by the Rindler time ω =t/4GM .
In Appendix A we calculate the matrix element
M (1, 2; 3) = ⟨0|[Φ(1) , Φ(2)] |3⟩, (3.6)
to leading order in the string coupling g. It gives the overlap of the commutator of two
light-front open bosonic string ﬁelds with state |3⟩. To leading order in g, the commutator
creates a single string state. The matrix element
MAB(1, 2; 3) = ⟨0|[φA(x1),φ B(x2)]|3⟩, (3.7)
for the commutator of any two mass eigenstate ﬁelds φA(x) can be obtained from equation
(3.6) by folding in with the appropriate transverse string w ave functions. We show that
there exist matrix elements of this form which are non-zero e ven when x1 −x2 is spacelike.
Finally we obtain, matrix elements of the commutator of low- energy nice-slice ﬁelds
ˆMAB(1, 2; 3) = ⟨0|[ ˆφA(x1), ˆφB(x2)]|3⟩, (3.8)
by integrating the mass eigenstate ﬁelds against test funct ions appropriate for nice-slice
observers at x1 and x2.
Because the spacelike separation between x1 and x2 grows exponentially with ω, one
would ordinarily expect the matrix elements (3.8) to tend to zero very rapidly with ω.
Indeed, for the commutator of tachyon component ﬁelds with a spectator tachyon, this is
what we ﬁnd. This does not give a good indication of the “size” of the commutator, how-
ever, because for large ω the commutator creates a high-mass string state which has ve ry
little overlap with any ﬁxed-mass spectator state. A better way to obtain the magnitude
9
of the commutator is to multiply the matrix element (3.8) by i ts complex conjugate and
sum over spectator states; in other words, to calculate a mat rix element of the form
ˆM (1, 2; 1′, 2′) = ⟨0|[ ˆφ1(x1), ˆφ2(x2)][ ˆφ2(x2
′), ˆφ1(x1
′)]|0⟩. (3.9)
A detailed calculation of these matrix elements to leading o rder in g is presented in Ap-
pendix B, but we shall describe the basic points of the calcul ation here. The matrix element
(3.9) has the form of a sum of ﬁnite time scattering amplitude s, which can be calculated
using the ﬁrst quantized formalism. The discussion is simpl iﬁed if we Fourier transform
the amplitude to momentum space. Since the spectator states are all single string states,
if we deﬁne s = −(p1 +p2)2 and t = −(p2 −p2′)2, then the relevant string world sheet
describes an s-channel diagram. One ﬁnds that as ω increases, the dominant contribution
to the matrix element comes from the region where the longitu dinal momenta p+
1 and p+
1′
are of order e−ω, and the s variable is large and positive. Heuristically, what happen s is
the scattering amplitudes are driven into the Regge region, where they behave as sα(t).
In open string theory, α(t) = α′t + 1 is the leading Regge trajectory. Because of the
Regge behavior, matrix elements of the form (3.9) do not decr ease as ω → ∞ , but stay
approximately constant. Moreover, since the behavior is do minated by the leading Regge
intercept, the extension to closed bosonic strings is strai ghtforward. The matrix element
for tachyon component ﬁelds in the closed string theory actu ally grows like eω.
One might have argued that the behavior found above should be expected, since the
spectrum of the bosonic string contains a tachyon. It should be clear from the above
discussion, however, that the existence of the tachyon has n o bearing on the result. In
fact, if one canonically quantizes a tachyon ﬁeld in Minkows ki space by imposing that the
ﬁeld commute with itself on some spacelike surface, the Lore ntz transformation properties
of scalar ﬁelds guarantee that the ﬁeld will commute with its elf on all spacelike surfaces.
It is the Regge behavior of strings, or in other words the exis tence of the inﬁnite tower
of massive states to which the commutator can couple, which g overns the behavior of
the matrix element (3.9) as ω → ∞ . This behavior will therefore also be present in the
tachyon-free superstring case.
The above results have important consequences for the nice- slice theory. The eﬀective
ﬁelds ˆφA(x1) and ˆφB(x2) are, by construction, low-energy ﬁelds as measured by nice -slice
observers. Since these ﬁelds belong to the algebra of operat ors of the regulated nice-slice
theory, then so must their commutator. Our explicit computa tion shows, however, that
the commutator (to leading order in the string coupling g) is an operator which creates
10
a single excited string which is stretched between x1 and x2. The mass squared of this
string state is of order s ∼eω/α′, and eventually becomes trans-Planckian as ω gets large.
Nevertheless, the nice-slice energy of the conﬁguration re mains low, and this state must
therefore be regarded as an unavoidable part of the nice-sli ce theory, which could never
have been discovered if we had ﬁrst truncated the theory to th e massless ﬁelds.
Let us consider how it is possible for conﬁgurations to have l ow values of the nice-
slice energy, and yet have huge trans-Planckian masses. Con sider a state with a massless
particle of low nice-slice energy at each of the points x1 and x2. Let the four-momentum
of the particle at x2 be
q2 = (q−
2,q +
2,⃗ q2), (3.10)
with the individual components of q2 being smaller than some cutoﬀ momentum. The
four-momentum of a low nice-slice energy particle at x1 is given by
q1 = (eωq−
1,e −ωq+
1,⃗ q1), (3.11)
with the components qµ
1 being smaller than the cutoﬀ momentum. Although the nice-sl ice
energy of this conﬁguration is small, the Minkowski mass of t he state rapidly becomes
trans-Planckian as ω increases:
m2 = −(q1 +q2)2 ∼eωq−
1q+
2 (3.12)
Generally, a state of low nice-slice energy will have very la rge mass squared if it is spread
over a large distance.
It is disturbing at ﬁrst sight to ﬁnd not only nonvanishing, b ut large values for the
commutator of ﬁelds with spacelike separated arguments. No te, however, that this ef-
fect is only encountered under very extreme kinematic circu mstances. In Appendix A.2,
it is shown that if one considers component ﬁelds appropriat e for low-energy Minkowski
observers, then the matrix elements (3.8) are given by the us ual ﬁeld-theoretic formulas,
and are therefore suppressed when the ﬁelds are spacelike se parated. This is simply be-
cause the invariant mass squared of this process is always mu ch smaller than 1 /α′, so the
commutator cannot couple to the higher mass, extended strin g states.
11
