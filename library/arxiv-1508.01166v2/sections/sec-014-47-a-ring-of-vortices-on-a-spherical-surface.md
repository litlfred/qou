---
doc_id: arxiv-1508.01166v2
doc_title: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes"
section_id: sec-014-47-a-ring-of-vortices-on-a-spherical-surface
section_title: "A ring of vortices on a spherical surface"
section_number: 4.7
pages: 27-29
source_pdf: 1508.01166v2.pdf
source_sha256: 0abff3bfd7d3d3e4
toc_source: outline
doc_brief: "Discrete exterior calculus discretization of incompressible Navier-Stokes equations over surface simplicial meshes — A conservative discretization of incompressible Navier-Stokes equations is de"
---
The behavior of a ring ofN equidistant point vortices, having the same strength,
positioned on a circle with ﬁxed latitude on a spherical surface was previously in-
vestigated theoretically [32]. It was shown that with such a conﬁguration, the
vortices will rotate around the z-axis in a stable fashion given that the circle’s lat-
itudeθ is below a critical value and the number of vortices N≤ 7. For N = 6, the
critical polar angleθc∼ 0.464 [33]. The behavior of such a ring of vortices is sim-
ulated, where the point vortices are replaced with vortices having the distribution
ω = τ
cosh2( 3r
a )
(27)
withτ to be the vortex strength,a is the vortex radius, andr is the distance between
any ﬁeld point and the vortex center.
Six identical vortices, having a strength τ = 3 and a radius a = 0.15, are
placed on a unit sphere at latitude θ = 0.4. In order to satisfy the condition
27
(a)
 (b)
(c)
 (d)
Figure 7: The vorticity contour plot for two Taylor vortices on a spherical surface
meshed with 327680 elements at time: (a) T =0.0, (b) T=2.0 and (c) T=10.0. (d)
The convergence of the relative kinetic energy error with the time step at simula-
tion time T = 10.0. The dashed red line represents the second order slope.
28
that the integration of the vorticity over a spherical surface is zero, an additional
vortex, with a strengthτ =−18 and a radius a = 0.15, is placed at the south pole
(θ =π). The spherical surface is meshed with 81920 elements, and the simulation
is conducted for an inviscid ﬂow with a time step ∆t = 0.005.
Figs. 8a and 8b show the vorticity contour plots at time T = 0 and T =
36, respectively. It is observed that the vortices positions seem unchanged after
such simulation time, with some ﬂow ﬂuctuations around the vortices due to the
inviscid nature of the ﬂow. The cyclic rotation of the vortices around the z-axis
can be detected by monitoring the relative solution change, with respect to the
original solution, with time. Recalling that the vectorU(t) contains the ﬂuxes over
all mesh edges at time t, the relative solution change is then deﬁned as ||U(t)−U(0)||
||U(0)|| .
Such relative solution change should be equal to zero each time the six vortices
rotate by an angleπ/3 around the z-axis. The relative solution change versus time
is shown in Fig. 8c, which reveals the periodic nature of the vortices motion. The
six vortices perform aπ/3 rotation around the z-axis in a time period of almost 12
time units. Accordingly, at time T = 36, the six vortices have rotated by an angle
π around the z-axis. A small non-vanishing relative solution change, of almost
0.01, is observed after each cycle, which is due to the developing ﬂow ﬂuctuations
around the vortices, as was shown in Fig. 8b. Finally, the vorticity strength along
the circle with latitudeθ = 0.4 is shown in Fig. 8d at simulation times T = 0 and
T = 36. The ﬁgure indicates more quantitatively that at time T = 36 the vortices
positions are similar to the original positions due to their π rotation around the
z-axis. The vorticity strength drop at the center of all the six vortices is due to
the developed ﬂow ﬂuctuations around the vortices. Recalling that the vorticity
integration over the spherical surface is always by construction maintained at zero,
and noting that the strength of the single vortex at the south pole only changed by
0.002% at time T = 36, the vorticity developed around the six vortices due to
ﬂow ﬂuctuations is compensated from the six vortices themselves. In regards to
the kinetic energy, the relative change in the kinetic energy at time T = 36 is
KE (T=0)−KE (T=36)
KE (T=0) = 9.0× 10−6.
