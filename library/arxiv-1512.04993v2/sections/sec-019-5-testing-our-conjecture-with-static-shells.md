---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-019-5-testing-our-conjecture-with-static-shells
section_title: "Testing our conjecture with static shells"
section_number: 5
pages: 30-31
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
So far we have considered the complexiﬁcation rate of an isolated black hole. We would
like to test our proposal by adding controlled complications. One test is an ingoing
shell (a shock wave), which will be considered in §6; in this section we will instead
consider a static shell (a Dyson sphere), see Fig. 7.
static shell at fixed r   ¯r
Figure 7: A black hole surrounded by a static sphere.
Consider a static sphere at r = ¯r, buttressed against collapse by its compressive
strength. Outside the shell the metric is the Schwarzschild metric with mass M +δM ,
ds2
⏐⏐⏐
r>¯r
=−
(
1− 2G(M +δM )
r + r2
𝓁2
AdS
)
dt2 + dr2
1− 2G(M+δM)
r + r2
𝓁2
AdS
+r2dΩ 2
2. (5.1)
Inside the shell r < ¯r the metric is the Schwarzschild metric with mass M with a
(locally unobservable) time dilation relative to inﬁnity from being deep in the shell’s
gravitational well,
ds2
⏐⏐⏐
r<¯r
=−
1− 2G(M+δM)
¯r + ¯r2
𝓁2
AdS
1− 2GM
¯r + ¯r2
𝓁2
AdS
(
1− 2GM
r + r2
𝓁2
AdS
)
dt2 + dr2
1− 2GM
r + r2
𝓁2
AdS
+r2dΩ 2
2.
(5.2)
Now let’s calculate the action. The shell itself lies outside the horizon, and so only
directly contributes to the time-independent (boost-invariant) part of the action. The
only eﬀect on the rate of change of action is indirect, through the change in the interior
metric: the rate of change of action picks up exactly one gravitational time dilation
29
factor,
dA
dtL
⏐⏐⏐⏐⏐
shell
=
vuu√1− 2G(M+δM)
¯r + ¯r2
𝓁2
AdS
1− 2GM
¯r + ¯r2
𝓁2
AdS
dA
dtL
⏐⏐⏐⏐⏐
no shell
. (5.3)
According to the action prescription, therefore, on the one hand, static shells do not
compute, and, on the other hand, computers in gravitational wells slow down due to
time dilation. Since both of these are exactly the behavior we would hope for, the
proposal of Eq. 1.1 passes this test.
This argument applies to any ordinary static matter outside the horizon—it does
not compute to leading order in G and its only eﬀect is that of gravitational time
dilation, which is to slow the rate of computation of the black hole. This is consistent
with the conjecture that an isolated black hole is the fastest computer in nature.
Let us return now to the superconducting instability of charged black holes. When
the black hole becomes highly charged it will tend to expel charge into the atmosphere
between the horizon and the AdS boundary. As discussed in Sec.4.5, the charge may
then condense into a zero-entropy inert shell-like condensate. The remnant black hole
at the center of the superconducting shell will not be close to extremality. Thus we
will have an example of a far-from-extremal black hole surrounded by a static inert
shell. The argument for static shells can be used to insure that the superconducting
black holes do not violate the bound on computation.
