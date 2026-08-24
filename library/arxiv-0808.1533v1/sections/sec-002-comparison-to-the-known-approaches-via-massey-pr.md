---
doc_id: arxiv-0808.1533v1
doc_title: "On the third order helicity of magnetic ﬁelds on invariant domains in S3 R. Komendarczyk ∗"
section_id: sec-002-comparison-to-the-known-approaches-via-massey-pr
section_title: "Comparison to the known approaches via Massey products."
section_number: null
pages: 27-31
source_pdf: 0808.1533v1.pdf
source_sha256: 85bb9732afdd70ea
doc_brief: "On the third order helicity of magnetic fields on invariant domains in S³ — We introduce an alternative approach to the third order heli city of a volume preserving vector ﬁeld B, which leads us to a"
duplicate_of: "arxiv-0808.1533v3"
---
products.
In several prior works [5, 14, 20, 22] higher helicities were develope d via the Massey product
formula for ¯µ123. These approaches should be equivalent to the one presented her e in the
sense that invariants obtained this way measure the same topologic al information. Most
notably the work [20] provides an explicit expression for the third or der helicity of the
borromean ﬂux tubes, where the ergodic interpretation in the sty le of Arnold’s asymptotic
linking number is also provided. In [22] one ﬁnds the following formula fo r the third order
helicity
M123(X1, X2, X3) =
∫
M
A1 ∧ A2 ∧ A3, (44)
where Ai = d−1(ιXiµ). This formula is valid for three distinct vector ﬁelds Xi on a closed
manifold M. For invariant domains with boundary (44) deﬁnes an invariant prov ided Ai
⏐
⏐
∂M =
0, but this only happens in certain situations (e.g. M is simply connected, and Ai’s are
appropriately chosen).
The most commonly known formula directly related to the Massey pro ducts was developed
by Berger [5], in the case of borromean ﬂux tubes: T = T1 ∪ T2 ∪ T3:
M123(X1, X2, X3) =
∫
∂T1
A1 ∧ F23 + F12 ∧ A3, (45)
in [5] it is expressed as a volume integral over T by applying so called gauge ﬁxing. When
Ti are topologically solid tori there exists a single Massey product < a 1, a2, a3 > in the
complement: S3 \ T , and the 2-form A1 ∧ F23 + F12 ∧ A3 is its representative. When Ti are
handlebodies there are multiple Massey products in the complement S3 \ T , but the formula
(45) should still be valid. Such extensions were not so far considere d in the literature and
the volume integrals over T may be harder to obtain in such case. One may also point out
that ergodic interpretations of Massey products are more involve d, [20], comparing to the
approach presented in Section 5.
27
Appendix A: Equations for the frozen-in-ﬁeld forms
Given a volume preserving vector ﬁeld X on M and a path t − →g(t) ∈ Diﬀ vol(M), let
X t := g∗(t)X .
Then for X 0 = X, by deﬁnition
˙X t = d
dt X t⏐
⏐
t=0= −LV X = −[V, X ], (46)
and as a result d
dtιX tµ|t=0 = −ι[V,X ]µ
Next, calculate ( ∂t + LV ≡ L ∂t+V )
(∂t + LV )ιX tµ = ∂t(ιX tµ) + LV ιX tµ
= ι ˙X tµ + ιX t(LV µ) + ι[V,X t]µ
= ι ˙X t+[V,X t]µ,
where in the second identity we applied the general formula: ι[A,B] = LAιB − ιBLA, and in
the third equation the fact that V is volume preserving i.e. LV µ = 0. As a result of (46) we
obtain
(∂t + LV )ιX tµ = 0 .
Appendix B: Zero contribution of short paths to the
time average
It is clear when β ∈ Ω 3(~T ) is at least a C 1 on ~T ⊂ S3 × S3 × S3, then f = β(X1, X2, X3) is
continuous on ~T and
∫
¯O 1
T (x)
∫
¯O2
T (y)
∫
¯O 3
T (z)
f =
(∫
O1
T (x)
+
∫
σ(Φ 1(x,T ),x)
)(∫
O 2
T (y)
+
∫
σ(Φ 2(y,T ),y)
)(∫
O 3
T (z)
+
∫
σ(Φ 3(z,T ),z)
)
f .
After expanding, it is obvious that we must show the following (for all choices), when T → ∞:
1
T 3
∫
σ(Φ 1(x,T ),x)
∫
O 2
T (y)
∫
O 3
T (z)
f − → 0, (47)
1
T 3
∫
σ(Φ 1(x,T ),x)
∫
σ(Φ 2(y,T ),y)
∫
O 3
T (z)
f − → 0, (48)
1
T 3
∫
σ(Φ 1(x,T ),x)
∫
σ(Φ 2(y,T ),y)
∫
σ(Φ 3(z,T ),z)
f − → 0. (49)
28
Since the lengths of the short paths in S are bounded by a common constant d, (47)-(49)
follow immediately, e.g. for (47) we have
⏐
⏐ 1
T 3
∫
σ(Φ 1(x,T ),x)
∫
O 2
T (y)
∫
O 3
T (z)
f
⏐
⏐ ≤ 1
T 3 d(T + d)(T + d)‖f ‖∞ − →0.
Appendix C: Notation
We adopt notation from the elegant exposition in [27]. Let M be an orientable manifold
with smooth boundary.
Ω k(M) = C ∞(M, Λ k), smooth diﬀerential forms on M.
Ω k
N (M) = {φ ∈ Ω k(M) | nφ = 0 , ndφ = 0 } the subspace satisfying the Neumann
boundary conditions, ( n denotes a normal component of a form along ∂M ).
The L2-inner product on Ω k(M) is deﬁned as
(
ω, η
)
L2 =
∫
M
ω ∧ ∗η,
L2Ω k(M), L2-diﬀerential forms on M.
H sΩ k(M) the Sobolev space of diﬀerential k-forms with s weak “derivatives” in L2.
Hk
N (M) = {λ ∈ H 1Ω k(M) | dλ = δλ = 0 , nλ = 0 } the subspace of the Neumann
harmonic ﬁelds.
Next we justify (40), ﬁrst observe that for any γ ∈ H 1Ω k−1(M):
(dγ, λ)L2 =
∫
∂M
tγ ∧ ∗nλ = 0, ∀λ ∈ H k
N (M), (50)
as a result if ω ∈ H k
N (M)⊥ we obtain a solution φ to the Neumann problem:
δdφ + dδφ = ω, ⇒ ω − dδφ = δdφ . (51)
Formula (50) implies: ( ω − dδφ) ∈ H k
N (M)⊥, moreover n(ω − dδφ) = n(δdφ) = δ n(dφ) = 0,
by the boundary condition in (39). If ω is a closed form, ω − dδφ is also closed, and clearly
coclosed by (51). Thus ω−dδφ is a harmonic ﬁeld with zero normal component, and therefore
it has to be in Hk
N (M), and therefore the zero form. This yields
ω = dδφ .
As a result we obtain a necessary and suﬃcient conditions for ω to be exact:
(i) dω = 0,
(ii) ( ω, λ)L2 = 0, ∀λ ∈ H k
N (M).
29
References
[1] P. Akhmetiev. On a new integral formula for an invariant of 3-com ponent oriented links.
J. Geom. Phys. , 53(2):180–196, 2005.
[2] V. Arnold. The asymptotic Hopf invariant and its applications. Selecta Math. Soviet. ,
5(4):327–345, 1986. Selected translations.
[3] V. Arnold and B. Khesin. Topological methods in hydrodynamics, volume 125 of Applied
Mathematical Sciences. Springer-Verlag, New York, 1998.
[4] M. E. Becker. Multiparameter groups of measure-preserving t ransformations: a simple
proof of Wiener’s ergodic theorem. Ann. Probab., 9(3):504–509, 1981.
[5] M. Berger. Third-order link integrals. J. Phys. A , 23(13):2787–2793, 1990.
[6] R. Bott and L. Tu. Diﬀerential forms in algebraic topology , volume 82 of Graduate Texts
in Mathematics . Springer-Verlag, New York, 1982.
[7] J. Cantarella. A general mutual helicity formula. R. Soc. Lond. Proc. Ser. A Math.
Phys. Eng. Sci. , 456(2003):2771–2779, 2000.
[8] J. Cantarella, D. DeTurck, and H. Gluck. The Biot-Savart opera tor for application to
knot theory, ﬂuid dynamics, and plasma physics. J. Math. Phys. , 42(2):876–905, 2001.
[9] J. Cantarella, D. DeTurck, H. Gluck, and M. Teytel. Isoperimetr ic problems for the he-
licity of vector ﬁelds and the Biot-Savart and curl operators. J. Math. Phys. , 41(8):5615–
5641, 2000.
[10] I. Chavel. Eigenvalues in Riemannian geometry , volume 115 of Pure and Applied Mathe-
matics. Academic Press Inc., Orlando, FL, 1984. Including a chapter by Bu rton Randol,
With an appendix by Jozef Dodziuk.
[11] F. R. Cohen. Private communication. 2007.
[12] F. R. Cohen and S. Gitler. On loop spaces of conﬁguration space s. Trans. Amer. Math.
Soc., 354(5):1705–1748 (electronic), 2002.
[13] D. DeTurck, H. Gluck, R. Komendarczyk, P. Melvin, C. Shonkwile r, and D. Vela-Vick.
Triple linking numbers, Hopf invariants and Integral formulas for th ree-component links.
in preparation.
[14] N. W. Evans and M. A. Berger. A hierarchy of linking integrals. In Topological aspects
of the dynamics of ﬂuids and plasmas (Santa Barbara, CA, 1991 ), volume 218 of NATO
Adv. Sci. Inst. Ser. E Appl. Sci. , pages 237–248. Kluwer Acad. Publ., Dordrecht, 1992.
30
[15] M. Freedman and Z. He. Divergence-free ﬁelds: energy and as ymptotic crossing number.
Ann. of Math. (2) , 134(1):189–229, 1991.
[16] J.-M. Gambaudo and ´E. Ghys. Enlacements asymptotiques. Topology, 36(6):1355–1379,
1997.
[17] B. Khesin. Topological ﬂuid dynamics. Notices Amer. Math. Soc. , 52(1):9–19, 2005.
[18] T. Kohno. Loop spaces of conﬁguration spaces and ﬁnite type invariants. In Invariants
of knots and 3-manifolds (Kyoto, 2001) , volume 4 of Geom. Topol. Monogr. , pages
143–160 (electronic). Geom. Topol. Publ., Coventry, 2002.
[19] P. Laurence and M. Avellaneda. A Moﬀatt-Arnold formula for th e mutual helicity of
linked ﬂux tubes. Geophys. Astrophys. Fluid Dynam. , 69(1-4):243–256, 1993.
[20] P. Laurence and E. Stredulinsky. Asymptotic Massey product s, induced currents and
Borromean torus links. J. Math. Phys. , 41(5):3170–3191, 2000.
[21] P. Laurence and E. Stredulinsky. A lower bound for the energy of magnetic ﬁelds
supported in linked tori. C. R. Acad. Sci. Paris S´ er. I Math. , 331(3):201–206, 2000.
[22] C. Mayer. Topological link invariants of magnetic ﬁelds. Ph.D. thesis , 2003.
[23] J. Milnor. Link groups. Ann. of Math. (2) , 59:177–195, 1954.
[24] J. Milnor. Isotopy of links. In R. Fox, editor, Algebraic Geometry and Topology , pages
280–306. Princeton University Press, 1957.
[25] J. Milnor. Topology from the Diﬀerentiable Viewpoint , chapter 7. Princeton Landmarks
in Mathematics and Physics. Princeton University Press, Princeton , NJ, 1997. Revised
reprint of 1965 original.
[26] E. Priest. Solar Magnetohydrodynamics. D.Redidel Publishing Comp., 1984.
[27] G. Schwarz. Hodge decomposition—a method for solving boundary value pr oblems, vol-
ume 1607 of Lecture Notes in Mathematics . Springer-Verlag, Berlin, 1995.
[28] H. v. Bodecker and G. Hornig. Link invariants of electromagnet ic ﬁelds. Phys. Rev.
Lett., 92(3):030406, 4, 2004.
[29] A. Verjovsky and R. F. Vila Freyer. The Jones-Witten invariant for ﬂows on a 3-
dimensional manifold. Comm. Math. Phys. , 163(1):73–88, 1994.
[30] T. Vogel. On the asymptotic linking number. Proc. Amer. Math. Soc., 131(7):2289–2297
(electronic), 2003.
31
