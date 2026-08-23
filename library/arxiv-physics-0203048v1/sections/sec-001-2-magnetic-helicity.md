---
doc_id: arxiv-physics-0203048v1
doc_title: "Towards a third-order topological invariant for magnetic ﬁelds"
section_id: sec-001-2-magnetic-helicity
section_title: "Magnetic helicity"
section_number: 2
pages: 2-4
source_pdf: 0203048v1.pdf
source_sha256: 47204f32280e91a3
doc_brief: "Towards a third-order topological invariant for magnetic fields — An expression for a third-order link integral of three magne tic ﬁelds is presented."
---
in recent years (see e.g. Brown et al 1999). Magnetic helicity, which measures the
linkage of magnetic ﬂux, is only a lowest order topological measure. I t fails for instance
to detect the interlocking of magnetic ﬂux tubes in form of the Borr omean rings or
the Whitehead link (see Figure 1). The total magnetic helicity of thes e conﬁgurations
vanishes just as it does for three or two unlinked ﬂux tubes. Both c onﬁgurations must
possess a higher order linkage or knottedness of magnetic ﬂux whic h is not detected
by magnetic helicity. This naturally raises the question whether corr esponding higher
order measures similar to magnetic helicity exist which are sensitive to these linkages.
Here we would like to remark that the conﬁgurations shown in Figure 1 are highly
idealized. In any real plasma we would not ﬁnd this pure linkage but a mix ture of
diﬀerent types of linkages, each of which is to be measured by a diﬀer ent integral.
In knot theory diﬀerent invariants are known which distinguish e.g. t he
Borromean rings or the Whitehead link from unlinked rings. The proble m is that
invariants used in physical applications, e.g. in magnetohydrodynam ics, should be
expressed in terms of observable quantities, in our setting in terms of the magnetic
ﬁeld B. Up to now only the helicity, which is related to the Gauß linking number,
has been formulated as an invariant for magnetic ﬁelds in a satisfact ory manner.
As was recognized ﬁrst by Monastyrsky and Sasorov (1987) and in dependently by
Berger (1990) and Evans and Berger (1992), the link invariants ba sed on so-called
higher Massey products (see Massey 1958, 1969, Kraines 1966, F enn 1983) can be
written as invariants applicable to magnetic ﬂux tubes. Similar to helicit y, they only
involve the magnetic ﬁelds and can be expressed as volume integrals o ver the space in
consideration. Their disadvantage is that their usage is restricted to magnetic ﬁelds
conﬁned to isolated ﬂux tubes. In addition, these ﬂux tubes must n ot possess a linkage
Figure 1. The Borromean rings (left) and the Whitehead link (right).
Third-order topological invariant 3
lower than the linkage which is measured.
In this paper we present a generalized third-order invariant for th ree magnetic
ﬁelds not conﬁned to isolated ﬂux tubes. In the case of isolated ﬂux tubes this invariant
coincides with the invariant known from the Massey triple product. U sing gauge
ﬁelds in the context of an SU (2) symmetry, the generalized invariant can be shown to
originate from the same equation as helicity. Therefore, we will ﬁrst recapitulate some
basic facts about magnetic helicity before we turn to our main subje ct, the third-order
link invariant.
2. Magnetic helicity
Magnetic helicity of a ﬁeld B with arbitrary vector potential A is deﬁned as
H(B) =
∫
V
A · B d3x, B · n|∂V = 0, (2)
which can readily be shown to be gauge invariant if no magnetic ﬂux cro sses the
boundary of the volume. Since it is quadratic in magnetic ﬂux it is often referred to
as a second-order topological invariant. Magnetic helicity measure s the total mutual
linkage of magnetic ﬂux. This interpretation can be motivated if we en visage a
simple system of two isolated and closed ﬂux tubes U1 andU2 with vanishingly small
cross-section. The latter condition ensures that the (self-)helic ities of the ﬂux tubes
vanish. Moﬀatt (1969) has shown that for this conﬁguration the h elicity integral yields
H(B) = 2 φ1φ2 lk(U1,U 2), where lk(U1,U 2) is the Gauß linking number (Gauß 1867)
of the two tubes and where φi is the magnetic ﬂux in the tube Ui. Introducing an
asymptotic linking number, Arnol’d (1974) was able to extend this inte rpretation to
the generic case where ﬁeld lines are not necessarily closed (see also Arnol’d & Khesin
1998, Part III, §4).
Similar to helicity we can introduce the more general cross-helicity of two
magnetic ﬁelds B1 and B2. For a simply connected volume V and provided that
B1 · n|∂V = B2 · n|∂V = 0 we deﬁne
H(B1, B2) :=
∫
V
A1 · B2 d3x =
∫
V
B1 · A2 d3x. (3)
The boundary conditions ensure that this is again a gauge invariant q uantity. To
see that the two integrals on the right-hand side are equivalent, no te that they diﬀer
only by a surface integral
∫
(A1 × A2) · n d2x. This can be shown to vanish using
the equivalence of Bi · n|∂V = 0 with Ai × n|∂V = 0 in a certain gauge and for a
simply connected volume V , as proved in Appendix A. Since both integrals are gauge
invariant this proves the equality for any gauge.
H(B1, B2) measures purely the cross linkage of ﬂux among the two ﬁelds. App lied
to our system of two isolated closed ﬂux tubes with ﬁelds B1 + B2 = B in the
corresponding tubes this invariant yields
H(B1, B2) = 2 φ1φ2 lk(U1,U 2), (4)
which is now valid without the assumption of vanishingly small tube cros s-sections.
The signiﬁcance of magnetic helicity arises from the fact that it is inva riant in
IMHD. Using merely the homogeneous Maxwell equations we obtain
∂t(A · B) + ∇ · (A0B + E × A) = −2E · B, (5)
Third-order topological invariant 4
which describes the time evolution of helicity density A · B. Here A0 is the electric
potential and E the electric ﬁeld. The term A0B + E × A is to be interpreted as
a helicity current , and −2E · B as a source term . In an ideal plasma, i.e. with
E + v × B = 0, the source term vanishes and the helicity current can be writte n as
A0B + E × A =A0B + v (A · B) − B (A · v). (6)
Therefore equation (5) takes the form:
∂t (A · B) + ∇ · (v (A · B)) = ∇ · (χB), (7)
withχ = −A0 + A · v. Elsasser (1956) already noticed that a particular gauge can be
found such that χ = 0. Using either this gauge or an arbitrary gauge together with
the boundary condition B · n
⏐
⏐
∂V = 0 this last equation implies the conservation of
helicity in a comoving volume for an ideal plasma, since
d
dt
∫
V
A · B d3x =
∫
V
∂t (A · B) + ∇ · (v (A · B)) d 3x =
∫
∂V
χB · n d2x = 0. (8)
The invariance of integral (2) was ﬁrst stated by Woltjer (1958).
