---
doc_id: arxiv-1811.05376v4
doc_title: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres"
section_id: sec-014-a2-borel-laplace-resummation
section_title: "A.2 Borel-Laplace resummation"
section_number: null
pages: 36-40
source_pdf: 1811.05376v4.pdf
source_sha256: a486709d0a78d19c
doc_brief: "Resurgence Analysis of Quantum Invariants of Seifert Fibered Homology Spheres — For a Seifert ﬁbered homology sphereX we show that the q-series invariant ˆZ0(X;q) introduced by Gukov-Pei-Putrov-Vafa"
---
We now discuss in more detail the relation between the Borel transformB and the Laplace trans-
form, which we now introduce. Letγ⊂ C be an oriented contour. Letg be a measurable function
deﬁned in a neighbourhood ofγ. Denote byLγ(g) the Laplace transform given by
Lγ(g)(λ) =
∫
γ
exp(−λ·z)g(z) dz, (88)
for allζ∈ C such that the integral is absolutely convergent. Here we think ofλ∈ C∗ as a large
modulus asymptotics parameter. For any α∈ C∗ we let the contourαR+ be oriented in the
direction ofα unless we state otherwise.
That the transformsB andLR+ are formally inverses of each other should be understood as
follows. Ifα∈ C satisﬁesRe(α)>−1 and l∈ N then
LR+
(
ζα log(ζ)l)
= dl
dαl
(Γ(α + 1)
λα+1
)
.
We may introduce a polynomialQα,l∈ C[x] of degreel such that
LR+
(
ζα log(ζ)l)
=λ−α−1Qα,l(log(λ)). (89)
Let z∈ C with Re(z)> 0 and letm∈ N. We then have that
LR+◦B (λ−z log(λ)m) =λ−z log(λ)m,
B◦L R+(ζz−1 log(ζ)m) =ζz−1 log(ζ)m.
(90)
Resurgence Analysis of Quantum Invariants 37
Lemma 2.LetB : R+→ C be a measurable function and assume the integral deﬁningLR+(B)(λ)
is absolutely convergent forRe(λ)> 0. Assume there exists an increasing sequence{αj}∞
j=0 of real
numbers strictly greater than−1 and a sequence{βj}∞
j=0 of positive integers giving an asymptotic
expansion
B(t)∼t→0
∞∑
j=0
bjtαj log(t)βj.
Then the following holds
1. There exists for largeλ an asymptotic expansion ˜ϕ(λ) of the form
LR+(B)(λ)∼λ→∞ ˜ϕ(λ)
where
˜ϕ(λ) =
∑
α,β
bjλ−αj−1Qαj,βj(log(λ))
and Qαj,βj∈ C[x] is the degreeβj polynomial introdced in(89).
2. The Borel transform of˜ϕ is equal to the expansion ofB
B( ˜ϕ)(t) =
∞∑
j=0
bjtαj log(t)βj.
Proof. The Lemma is an elementary consequence of Equations (89) and (90).
The following theorem explains Borel-Laplace resummation. The content of Theorem 15 is
standard in resurgence, and a proof can be found in e.g. [50].
Theorem 15. Let
˜ϕ(λ) =
∞∑
j=0
cjλαj log(λ)βj (91)
be a formal series as in Deﬁnition 3 withα0 >−1. Assume that
• there exists a sectorS⊂ C, such that for allζ∈ S of suﬃciently small modulus the Borel
transformB( ˜ϕ)(ζ) converges to a holomorphic functionˆϕ(ζ) (possibly upon choosing a branch
of log(ζ) deﬁned onS), and that
• the function ˆϕ extends by analytic continuation along a half axisΓ(θ) = e2πiθR+⊂ S (for
some θ∈ [0, 1] say) and there exists a contantC >0 such that in a neighbourhood ofΓ(θ)
we have ˆϕ(z) =O(exp(C|z|)).
Then the following holds.
1. The Laplace transformLΓ(θ)( ˆϕ) is holomorphic on the open unbounded set{λ∈ C|| λ| >
C, ∀s∈S\{ 0} Re(λs)> 0}.
2. The Laplace transformLΓ(θ)( ˆϕ) has ˜ϕ as its largeλ asymptotic expansion
LΓ(θ)( ˆϕ)(λ)∼λ→∞ ˜ϕ(λ)
One of the goal’s of Ecalle’s theory [21, 22] is to consider the case where the formal series˜ϕ
(91) is obtained as a formal solution to some dynamical problem, which can be for instance an
ODE or a diﬀerence equation (with a singularity atλ−1 = 0). In such situations, the function
LΓ(θ)◦B ( ˜ϕ) will be a holomorphic solution, and resurgence is developed as a tool to analyze the
monodromy (known as Stokes phenomena), which occur upon varying the choice of directionθ in
which the Laplace transform is performed.
Resurgence Analysis of Quantum Invariants 38
References
[1] J. E. Andersen. The Witten-Reshetikhin-Turaev invariants of ﬁnite order mapping tori I.J.
Reine Angew. Math., 681:1–38, 2013.
[2] J. E. Andersen. Resurgence analysis of the wrt-tqft, online seminarhttps://sites.google.
com/view/gaugesummerwithbv/home/abstracts#h.rcu9ixszi7xk. June 2020.
[3] J. E. Andersen and S. K. Hansen. Asymptotics of the quantum invariants for surgeries on the
ﬁgure 8 knot.J. Knot Theory Ramiﬁcations, 15(4):479–548, 2006.
[4] J. E. Andersen, Benjamin Himpel, S. F. Jørgensen, J: Martens, and B. McLellan. The Witten-
Reshetikhin-Turaev invariant for links in ﬁnite order mapping tori I.Adv. Math., 304:131–178,
2017.
[5] J. E. Andersen and W. E. Petersen. Asymptotic expansions of the Witten-Reshetikhin-Turaev
Invariants of Mapping Tori I.Transactions of the American Mathematical Society, 2018.
[6] Inês Aniceto, Gökçe Bas,ar, and Ricardo Schiappa. A Primer on Resurgent Transseries and
Their Asymptotics. arXiv e-prints, page arXiv:1802.10441, Feb 2018.
[7] H. U. Boden and C. L. Curtis. The SL2(C) Casson invariant for Seifert ﬁbered homology
spheres and surgeries on twist knots.J. Knot Theory Ramiﬁcations, 15(7):813–837, 2006.
[8] Kathrin Bringmann, Jonas Kaszian, and Antun Milas. Higher depth quantum modular forms,
multiple eichler integrals, andsl3 false theta functions, 2017.
[9] KathrinBringmann, KarlMahlburg, andAntunMilas. Quantummodularformsandplumbing
graphs of 3-manifolds.arXiv e-prints, page arXiv:1810.05612, Oct 2018.
[10] Kathrin Bringmann, Karl Mahlburg, and Antun Milas. Higher depth quantum modular forms
and plumbed 3-manifolds. arXiv e-prints, page arXiv:1906.10722, Jun 2019.
[11] L. Charles and J. Marché. Knot state asymptotics II: Witten conjecture and irreducible
representations. Publ. Math. Inst. Hautes Études Sci., 121:323–361, 2015.
[12] Miranda C. N. Cheng, Sungbong Chun, Francesca Ferrari, Sergei Gukov, and Sarah M. Har-
rison. 3d Modularity.arXiv e-prints, page arXiv:1809.10148, Sep 2018.
[13] Sungbong Chun, Sergei Gukov, Sunghyuk Park, and Nikita Sopenko. 3d-3d correspondence
for mapping tori.arXiv e-prints, page arXiv:1911.08456, Nov 2019.
[14] Hee-Joong Chung. BPS Invariants for Seifert Manifolds. arXiv e-prints , page
arXiv:1811.08863, Nov 2018.
[15] Ovidiu Costin and S. Garoufalidis. Resurgence of the Kontsevich-Zagier series.Ann. Inst.
Fourier (Grenoble), 61(3):1225–1258, 2011.
[16] C. L. Curtis. An intersection theory count of the SL2(C)-representations of the fundamental
group of a3-manifold. Topology, 40(4):773–787, 2001.
[17] C. L. Curtis. Erratum to: “An intersection theory count of the SL2(C)-representations of
the fundamental group of a 3-manifold” [Topology 40 (2001), no. 4, 773–787; MR1851563
(2002k:57022)]. Topology, 42(4):929, 2003.
[18] Tudor Dimofte and Stavros Garoufalidis. Quantum modularity and complex Chern-Simons
theory. arXiv e-prints, page arXiv:1511.05628, Nov 2015.
[19] D. Dorigoni. An Introduction to Resurgence, Trans-Series and Alien Calculus.ArXiv e-prints,
November 2014.
[20] G. V. Dunne and M. Unsal. What is QFT? Resurgent trans-series, Lefschetz thimbles, and
new exact saddles.ArXiv e-prints, November 2015.
Resurgence Analysis of Quantum Invariants 39
[21] J. Écalle.Les fonctions résurgentes. Tome I, volume 5 ofPublications Mathématiques d’Orsay
81 [Mathematical Publications of Orsay 81]. Université de Paris-Sud, Département de Math-
ématique, Orsay, 1981. Les algèbres de fonctions résurgentes. [The algebras of resurgent
functions], With an English foreword.
[22] J. Écalle.Les fonctions résurgentes. Tome II, volume 6 ofPublications Mathématiques d’Orsay
81 [Mathematical Publications of Orsay 81]. Université de Paris-Sud, Département de Mathé-
matique, Orsay, 1981. Les fonctions résurgentes appliquées à l’itération. [Resurgent functions
applied to iteration].
[23] R. Fintushel and R. J. Stern. Instanton homology of Seifert ﬁbred homology three spheres.
Proc. London Math. Soc. (3), 61(1):109–137, 1990.
[24] Daniel S. Freed and Robert E. Gompf. Computer calculation of Witten’s3-manifold invariant.
Comm. Math. Phys., 141(1):79–117, 1991.
[25] Hiroyuki Fuji, Kohei Iwaki, Hitoshi Murakami, and Yuji Terashima. Witten-Reshetikhin-
Turaev function for a knot in Seifert manifolds.arXiv e-prints, page arXiv:2007.15872, July
2020.
[26] S. Garoufalidis. Chern-Simons theory, analytic continuation and arithmetic. Acta Math.
Vietnam., 33(3):335–362, 2008.
[27] S. Gukov, M. Marino, and P. Putrov. Resurgence in complex Chern-Simons theory.ArXiv
e-prints, May 2016.
[28] Sergei Gukov and Ciprian Manolescu. A two-variable series for knot complements. arXiv
e-prints, page arXiv:1904.06057, Apr 2019.
[29] Sergei Gukov, Du Pei, Pavel Putrov, and Cumrun Vafa. 4-manifolds and topological modular
forms. arXiv e-prints, page arXiv:1811.07884, Nov 2018.
[30] K. Hikami. Mock (False) Theta Functions as Quantum Invariants. Regular and Chaotic
Dynamics, 10(4):509, Jan 2005.
[31] Kazuhiro Hikami. q-series and l-functions related to half-derivatives of the andrews–gordon
identity. 2003.
[32] Kazuhiro Hikami. Quantum invariant for torus link and modular forms.Comm. Math. Phys.,
246(2):403–426, 2004.
[33] Kazuhiro Hikami. On the quantum invariant for the Brieskorn homology spheres.Internat.
J. Math., 16(6):661–685, 2005.
[34] Kazuhiro Hikami. Quantum invariant, modular form, and lattice points.Int. Math. Res. Not.,
(3):121–154, 2005.
[35] Kazuhiro Hikami. Quantum invariants, modular forms, and lattice points II. Journal of
Mathematical Physics, 47(10):102301–102301, Oct 2006.
[36] Kazuhiro Hikami. Decomposition of Witten-Reshetikhin-Turaev invariant: linking pairing
and modular forms. In Chern-Simons gauge theory: 20 years after, volume 50 ofAMS/IP
Stud. Adv. Math., pages 131–151. Amer. Math. Soc., Providence, RI, 2011.
[37] P. A. Kirk and E. P. Klassen. Chern-Simons invariants of3-manifolds and representation
spaces of knot groups.Math. Ann., 287(2):343–367, 1990.
[38] T. Kitano and Y. Yamaguchi. SL(2;R)-representations of a Brieskorn homology 3-sphere.
ArXiv e-prints, February 2016.
[39] R. Lawrence and L. Rozansky. Witten-Reshetikhin-Turaev invariants of Seifert manifolds.
Comm. Math. Phys., 205(2):287–314, 1999.
Resurgence Analysis of Quantum Invariants 40
[40] Ruth Lawrence and Don Zagier. Modular forms and quantum invariants of3-manifolds. Asian
J. Math., 3(1):93–107, 1999. Sir Michael Atiyah: a great mathematician of the twentieth
century.
[41] William Elbæk Mistegård. Quantum Invariants and Chern-Simons Theory. PhD thesis,
Aarhus University, 2019.
[42] William Elbæk Mistegård. Quantum modularity and resurgence, online seminar www.
researchgate.net/publication/341574789_quantum_modularity_and_resurgence. May
2020.
[43] C. Mitschi and D. Sauzin.Divergent series, summability and resurgence. I, volume 2153 of
Lecture Notes in Mathematics. Springer, [Cham], 2016. Monodromy and resurgence, With
a foreword by Jean-Pierre Ramis and a preface by Éric Delabaere, Michèle Loday-Richaud,
Claude Mitschi and David Sauzin.
[44] T. Ohtsuki. A polynomial invariant of integral homology3-spheres. Math. Proc. Cambridge
Philos. Soc., 117(1):83–112, 1995.
[45] T. Ohtsuki. Finite type invariants of integral homology3-spheres. J. Knot Theory Ramiﬁca-
tions, 5(1):101–115, 1996.
[46] T. Ohtsuki. A polynomial invariant of rational homology3-spheres. Invent. Math., 123(2):241–
257, 1996.
[47] Sunghyuk Park. Higher rankˆZ and FK. arXiv e-prints, page arXiv:1909.13002, Sep 2019.
[48] N.Y.ReshetikhinandV.G.Turaev. Ribbongraphsandtheirinvariantsderivedfromquantum
groups. Comm. Math. Phys., 127(1):1–26, 1990.
[49] N. Y. Reshetikhin and V. G. Turaev. Invariants of 3-manifolds via link polynomials and
quantum groups. Invent. Math., 103(3):547–597, 1991.
[50] D. Sauzin. Resurgent functions and splitting problems.ArXiv e-prints, June 2007.
[51] Kevin Walker. An extension of Casson’s invariant, volume 126 of Annals of Mathematics
Studies. Princeton University Press, Princeton, NJ, 1992.
[52] E. Witten. Analytic continuation of Chern-Simons theory. InChern-Simons gauge theory:
20 years after, volume 50 ofAMS/IP Stud. Adv. Math., pages 347–446. Amer. Math. Soc.,
Providence, RI, 2011.
Jørgen Ellegaard Andersen2
Center for Quantum Mathematics
Danish Institute for Advanced Study
University of Southern Denmark
DK-5000 Odense C, Denmark
jea-qm@mci.sdu.dk
William Elbæk Mistegård3
IST Austria
AT-3400, Austria
william.mistegaard@ist.ac.at
2This work is supported in part by the center of excellence grant "Center for Quantum Geometry of Moduli
Spaces" from the Danish National Research Foundation (DNRF95) and by the ERC-Synergy grant "ReNewQuan-
tum".
3This project has received funding from the European Union’s Horizon 2020 research and innovation programme
under the Marie Skłodowska-Curie grant agreement No 754411.
