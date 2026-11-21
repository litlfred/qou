---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-043-b-spherical-shock-waves-at-finite-time-and-energ
section_title: "B Spherical shock waves at finite time and energy"
section_number: null
pages: 59-62
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
toc_source: outline
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
Spherical shock waves at ﬁnite time and energy
We will work in D = 2+1 dimensions for simplicity. The shock wave has energy E and
the black hole has energy M, so we want to patch together a spacetime with energy
E + M (to the left of the shock) and a spacetime with energy M (to the right of the
58
shock). See Fig. 18. We will follow [26, 51] for the matching conditions between the
two spacetimes.
Let us associate coordinates (u, v) with the patch with energy M and (˜u, ˜v) with
the patch with energy E + M. Because of the increase in mass, the horizons are at
diﬀerent radii in the two spacetimes, rh and ˜rh, respectively. In the patch with energy
M, the relationship between Kruskal coordinates and Schwarzschild coordinates in the
asymptotic region to the left of the horizon is
u =
rr −rh
r + rh
e−rhtL/ℓ2
AdS,
v = −
rr −rh
r + rh
erhtL/ℓ2
AdS,
(B.1)
and in the patch with energy M + E the relationship is20
˜u =
r
r −˜rh
r + ˜rh
e−˜rhtL/ℓ2
AdS,
˜v = −
r
r −˜rh
r + ˜rh
e˜rhtL/ℓ2
AdS,
(B.2)
where on this boundary, time runs backwards so that the upper left of Fig. 18 is at
tL = −∞.21 We must have ˜rh > rh since the horizon jumps out when it swallows the
shock, and in fact the two horizon radii are related by
˜rh = rh
r
M + E
M
= rh
√
1 + ϵ,
(B.3)
where we’ve deﬁned ϵ ≡E/M.
We will parametrize the shock wave by its boundary time tw and its energy ϵ. In
the (u, v) coordinates, we can describe the shock wave as traveling along a null surface
of constant u = u0. In the (˜u, ˜v) coordinates, the shock wave travels on a null surface
at constant ˜u = ˜u0. We see from Eq. B.1 and Eq. B.2 that by demanding that the
shock leave the boundary at time tw that these surfaces are given by
u0 = e−rhtw/ℓ2
AdS,
˜u0 = e−˜rhtw/ℓ2
AdS,
(B.4)
respectively.
Next, we need to relate the (˜u, ˜v) coordinates to the (u, v) coordinates. The match-
ing conditions [51] amount to ensuring that the metric is continuous. First, we match
across the radius of the transverse space. This gives
˜rh
1 −˜u0˜v
1 + ˜u0˜v = rh
1 −u0v
1 + u0v
(B.5)
20We have ﬁxed a relative boost ambiguity by demanding that the boundary time tL is continuous.
21Note: in this Appendix we have reversed our time conventions for precursors W(t). Here, we
will take both left boundary Hamiltonian time evolution tL and Killing time evolution in the bulk to
increase to the past.
59
Figure 18: Kruskal diagram of shock wave at ﬁnite time tw. The white region to the
right of the shock has energy M and is covered by coordinates (u, v). The gray region
to the left of the shock has energy M + E and is covered by coordinates (˜u, ˜v). The
shock is drawn in blue and travels along the surface u0 = e−rhtw/ℓ2
AdS or equivalently
˜u0 = e−˜rhtw/ℓ2
AdS.
Solving for ˜v, we see that it’s a fractional linear transformation of v,
˜v(v) = 1
˜u0
(˜rh −rh) + (˜rh + rh)u0v
(˜rh + rh) + (˜rh −rh)u0v

(B.6)
Now normally we’d expand Eq. B.6 in the limit ϵ →0 and tw →∞, with ϵ/u0 ﬁxed.
Then, we’d ﬁnd ˜v(v) = v+ϵ/4u0 and that crossing the shock induces a simple shift. At
this order, we’d also have ˜rh = rh, and we’d pick ˜u(u) = u to satisfy the ﬁnal matching
condition. However, since tw →∞, the shock would have to lie on the horizon u = 0.
Since ϵ →0, the shock would have to have vanishing mass.
Instead, let’s study ﬁnite energy shocks at ﬁnite time, keeping ϵ and tw ﬁnite and
arbitrary. The only thing left to do is to relate ˜u and u. The ﬁnal matching condition
[51] is that guv dudv = g˜u˜v d˜ud˜v along the shock
−
4ℓ2
AdS
(1 + uv)2dudv|u=u0 = −
4ℓ2
AdS
(1 + ˜u˜v)2d˜ud˜v|˜u=˜u0
(B.7)
This reduces to the following condition on ˜u′(u)
˜u′(u)|u=u0 = u
√1+ϵ−1
0
√
1 + ϵ.
(B.8)
While there is still some freedom in the function ˜u(u) away from the shock, we can
simply satisfy Eq. B.8 by taking
˜u = u
√1+ϵ.
(B.9)
60
This condition makes the ﬁrst derivative smooth across the shock on the boundary,
but causes a kink across the shock on the singularity.
Now that we have ˜u(u) and ˜v(v), we can ﬁnd out how far the horizon jumps out
after absorbing the shock by inverting ˜v(v) = 0. This is the analog of the simple shift
we are used to
v(˜v = 0) = −1
u0
√1 + ϵ −1
√1 + ϵ + 1

,
(B.10)
which goes like −ϵ/4u0 in the limit ϵ →0, exactly as expected from [26]. The Kruskal
diagram is shown in Fig. 18. Below the shock in the white region, we use the (u, v)
coordinates. Above the shock in the gray region, we use coordinates (˜u(u), ˜v(v)). We
see that (as expected) there’s no kink across the shock at the boundary, but there is a
kink at the matching across the singularity.
Let us make a brief remark on the action of W in the geometry shown in Fig. 18. As
we will explain in the next subsection, we ﬁnd something very diﬀerent from Eq. 6.15.
Here, for times tL before the perturbation tw the rate of growth with tL would be M,
but for times after the perturbation, the rate would be M + E. This is indicative of
the fact that this geometry actually represents energy E being injected into the state
on the left boundary at time tL.
