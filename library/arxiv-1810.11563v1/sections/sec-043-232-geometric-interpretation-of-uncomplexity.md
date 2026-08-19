---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-043-232-geometric-interpretation-of-uncomplexity
section_title: "Geometric Interpretation of Uncomplexity"
section_number: 23.2
pages: 77-84
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
Figure 39 illustrates a one-sided AdS black hole formed by the collapse of some matter. In
the upper right corner the small slash-mark indicates the exponential time at which the
complexity becomes maximal. In Lecture II I explained the reasons for thinking that a
76
breakdown of classical GR and possibly the occurrence of ﬁrewalls might take place at this
time. The ﬁgure also shows Alice at time t who is contemplating a jump into the black
hole. She would like to know how much spacetime volume is available to her to explore.
Finally the ﬁgure also shows the WDW patch at time t, and in particular the portion
of the WDW patch behind the horizon.
Figure 39
Let’s consider the question: What is the uncomplexity of the quantum state of the
black hole at timet? To compute the uncomplexity we must ﬁrst determine the complexity.
According to the complexity-action duality the complexity is proportional to the action of
the portion of the WDW patch behind the horizon, in other words the spacetime volume
of the darker orange region.
Next, to compute the uncomplexity we must know the maximum possible complexity.
That’s given by the complexity evaluated at the time of the slash. The relevant spacetime
volume is shown in ﬁgure 40.
77
Figure 40
The uncomplexity is of course the diﬀerence between the maximum complexity and
the actual complexity at time t,
Uncomplexity =Cmax−C (t). (23.96)
which is the spacetime volume shown in blue in ﬁgure 41.
78
Figure 41
What is the meaning of the blue region in ﬁgure 41? It is the total available spacetime
that Alice can visit if she jumps in after timet. Thus we ﬁnd an elegant geometric meaning
to uncomplexity as a kind of spacetime resource available to observers who jump into the
black hole after time t.
Of course Alice can do a lot better if she happens to have a few thermal photons to
spare. For each clean thermal photon that she throws in, the uncomplexity increases by
an exponential amount. The mechanism was explained in Lecture II where we saw that a
thermal photon can clear out any ﬁrewalls for an exponential time.
Thus we see the remarkable power of one clean qubit in two ways, one involving com-
putation and one involving the elimination of ﬁrewalls behind the horizon.
Part IV
Conclusion
To me, the idea that computational complexity might govern the interior geometries of
black holes was startling. Complexity, especially quantum complexity, is such a subtle and
79
ﬁnespun quantity that ordinarily it is impossible to measure or even to compute. What
makes complexity so tenuous is that it is deﬁned as a global minimum, whereas in most
physical contexts local minima are the relevant things. This is especially concerning when
we consider the very long time behavior of a black hole.
Although I have not stressed it in these lectures, relative complexity can be thought of
in geometric terms (Dowling, Nielsen https://arxiv.org/pdf/quant-ph/0701004.pdf)
as the length of the shortest geodesic between two points U and V , the geometry being
deﬁned by a certain right-invariant complexity metric. The evolution of a system U(t)
sweeps out a geodesic, which for some period of time is the shortest geodesic connecting the
identity to U(t). Eventually a cut-locus https://en.wikipedia.org/wiki/Cut_locus_
(Riemannian_manifold) will be reached, at which point a shorter geodesic will emerge.
An example is a torus with incommensurate cycles. Starting at a point that we may call
I we may move along a geodesic forever without coming back to the same point. The
length of the geodesic, measured from I will grow forever. But once we pass the cut-
locus, a shorter geodesic will suddenly emerge. The original geodesic continues on, and is
completely smooth at the cut-locus, but it is no longer the global minimum. We saw just
this type of behavior in ﬁgure 16 in Lecture I where shorter paths materialized when the
complexity reached its maximal value.
That complexity governs the geometry of black hole interiors has sometimes been
greeted with skepticism just because of the global character of complexity. The argu-
ment is often expressed by saying that there is no physical reason for the geometry to
suddenly make a transition at the cut-locus since the Hamiltonian evolution of a black
hole is completely smooth. To put it another way, physics is governed by local stationary
points.
Consider ﬁgure 15. The transition from the linearly growing behavior to complexity
equilibrium occurs sharply—as it would at a cut-locus—even though the Hamiltonian
evolution of the system is perfectly smooth. If we suppose that the geometry of the
wormhole is insensitive to such transitions, the growth of the wormhole would continue
forever. The light blue extrapolation in ﬁgure 42 illustrates what the growth of a wormhole
volume might look like in that case, while the complexity would follow the original curve
in ﬁgure 15.
80
Figure 42
To see why this must be wrong, let’s consider the extreme situation in which the
complexity executes a quantum recurrence at the doubly exponential time exp exp S. The
obvious interpretation of the V-shaped portion of the red curve is that a white-hole black-
hole bounce has taken place, as in ﬁgure 17. Down at the bottom of the V the system
has returned to a state very close to the thermoﬁeld-double. The TFD is a state in which
the wormhole length vanishes. It would not be hard to conﬁrm that the wormhole is
short. A simple diagnostic would be the correlation function of ﬁelds at opposite ends of
the wormhole; a short wormhole would indicate a large correlation; a very long wormhole
would indicate a very small correlation. The fact that a quantum recurrence occurred
implies that the correlation would be large.
Therefore we must conclude that somewhere between t = 0 and t = exp exp S the
derivative of the wormhole length must have turned around. The natural place for that to
happen is when the system reaches complexity equilibrium, i.e., at the cut locus.
81
I’ll conclude these lectures with some philosophical remarks that I think apply not
only to my own lectures but to the entire PiTP 2018 series, especially to the lectures
about entanglement, chaos, SYK, and complexity. They represent my own views and
other lecturers may or may not agree with them.
For some time we have been moving toward the view that there are no independent laws
of gravity, only laws of quantum mechanics applied to certain kinds of complex systems.
The laws of gravity are emergent, and moreover they are not really laws; they are statistical
tendencies. The trend goes all the ways back to the laws of black holes as formulated by
Bardeen, Carter, and Hawking in 1972. In particular the second law of black holes states
that the total area of all horizons increases with time. This follows from the Einstein
ﬁeld equations which we usually think of as the absolute laws of gravity. But following
Bekenstein, we now know that the second law of black holes is nothing but the second law
of thermodynamics: total entropy increases. However the second law is not an absolute
law. It is a statistical tendency—a very strong tendency—but nonetheless a tendency.
Scrambling, chaos, and operator growth ( D. Roberts, D. Stanford and A. Streicher,
https://arxiv.org/pdf/1802.02633.pdf ) are very general phenomena seen in most
quantum systems with large number of degrees of freedom. It now seems that they are
connected with the Newtonian law that the momentum of an object increases as it falls, in
particular as it falls toward a horizon (https://arxiv.org/pdf/1802.01198.pdf https:
//arxiv.org/pdf/1804.04156.pdf). Scrambling and operator growth are phenomena
that apply to all complex quantum systems, but again they are statistical tendencies.
Finally, in these lectures I discussed the growth of spacetime behind horizons—another
consequence of Einstein’s equations. It has much in common with the growth of horizon
area, but unlike that phenomenon it is not connected with the ordinary second law of
thermodynamics. Instead it is a consequence of the second law of quantum complexity
which is also a statistical tendency.
All quantum systems exhibit these tendencies to a greater or lesser extent, but only
special quantum systems exhibit the detailed kind of locality that we identify with Ein-
stein gravity. In the context of AdS/CFT only special CFTs give rise to bulk locality on
scales much smaller than the AdS radius. Those systems require very strongly coupled
large-N gauge theories. Most quantum ﬁeld theories cannot be extrapolated to large cou-
pling without encountering phase transitions or worse. Only supersymmetric QFTs have
analyticity properties that ensure against such breakdown at large coupling. Thus, to my
knowledge, only super-theories have sub-AdS locality. That includes not only AdS/CFT
82
but also BFSS matrix theory https://arxiv.org/pdf/hep-th/9610043.pdf.
Of course the “real world” is not even approximately supersymmetric, yet it is very
local on microscopic scales. This is a big puzzle that nothing in my lectures, or the other
PiTP lectures address.
De Sitter space presents an even thornier puzzle. DS does not have the kind of time-like
boundary that underpins gauge-gravity duality. The tools from AdS/CFT do not seem to
apply in their currently understood form, possibly including the the connection between
complexity and spacetime geometry. Nevertheless we live in a de Sitter world in which
gravity is perfectly healthy. Evidently we are missing some important things which this
PiTP program not touched on. Sooner of later we will need to get out of the comfort zone
and move past AdS and supersymmetry.
83
