---
doc_id: arxiv-1908.07065v3
doc_title: "Prepared for submission to JHEP Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-013-7-conclusions
section_title: "Conclusions"
section_number: 7
pages: 37-47
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve ofN = 2, SU (2) super Yang–Mills"
---
In this paper we have used non-perturbative techniques inspired by supersymmetric gauge theory
and topological string theory to study the quantization of the Seiberg–Witten curve of N =
2, SU (2) super Yang–Mills theory, which gives the modiﬁed Mathieu operator. On the one
hand, building upon [5–8], we have obtained integral equations for the Borel resummation of the
quantum periods obtained with the all-orders WKB method. These equations predict as well the
resurgent structure of these periods, and in particular their Stokes discontinuities. The results
obtained in this way have been tested against calculations in the WKB method to very high
order. We have also clariﬁed the relation between these Borel-resummed quantum periods and
the “exact” quantum periods given by instanton calculus (in the NS limit). On the other hand,
we have used the TS/ST correspondence of [2, 3] to obtain a closed formula for the spectral
determinant of the modiﬁed Mathieu operator, and we have compared this formula to previous
results by Zamolodchikov.
Our results raise several issues. An important problem concerns the relation between the
TBA equations obtained in the context of SW theory, and the analytic bootstrap program ﬁrst
proposed in [21] and reloaded in [8, 9]. In the TBA equations obtained in [7, 8] for quantum
mechanics with polynomial potentials, one only needs the boundary condition associated to the
classical behavior (i.e. at ℏ→ 0, or equivalently at θ →∞ ). The boundary behavior when
θ→−∞ is ﬁxed by the integral equations. As pointed out already in [7] and further discussed in
section 3.3 of this paper, the integral equations for the modiﬁed Mathieu operator admit many
possible boundary conditions at θ→−∞ , and one needs additional information to ﬁx them.
One can use the quantum Matone relation and the ﬁrst quantum correction to the periods to
obtain additional constraints. However, it seems clear from the study of this example that the
analytic bootstrap might require additional asymptotic information to determine uniquely the
resummed quantum periods. As suggested in [7], one might obtain the appropriate boundary
conditions by ﬁrst solving the full TBA equations of [5] (before taking the conformal limit) and
then implementing the conformal limit directly on the solution.
Another problem that should be discussed more carefully is how to solve eﬃciently the TBA
equations to compute the Borel resummed quantum periods. In particular, we should understand
in detail how to to solve the inﬁnite tower of TBA equations appearing in the weak coupling
region.
It would be very interesting to extend the techniques developed in this paper to quantum
mirror curves. This would provide a relation between BPS states in local CY threefolds (studied
for example in [91]) and the resurgent properties of the corresponding quantum periods. Work
along this direction has been already done in [92, 93]. Another interesting class of quantum
curves which could be studied with our methods is the one given by quantum A-polynomials
of knots (see e.g. [94]). In this case, the resurgent properties should be closely related to the
resurgent properties of Andersen–Kashaev invariants [95], which have been considered in [96–
98]. They might correspond to BPS states in the supersymmetric dual obtained with the 3d/3d
correspondence of [99].
Another intriguing point is the following. Based on previous works [7, 8], we have shown
that the conformal limit of the GMN TBA equations encode in a precise way the NS limit of
the Omega background for the pure SU(2) theory. On the other hand it is interesting to observe
– 36 –
that, as pointed out in [65], there is another set of TBA equations which computes the selfdual
limit of the Omega background. The latter was obtained by Zamolodchikov in [100], see also
[101]. Interestingly also such TBA can be obtained from [5] upon a suitable limiting procedure.
It would be interesting to investigate more concretely if and how the full TBA equations of [5]
encode the full Omega background. Work along this direction was performed in [102].
In addition it should be possible to extend the results of section 6 to Painlev´ e III 2, III1, V
and VI. In these cases, the rˆ ole of the modiﬁed Mathieu operator is replaced by the quantum
SW curve of SU (2) gauge theory with Nf = 1, 2, 3, 4 ﬂavours, respectively. In particular, for
Nf = 4 one should recover the connection between Painlev´ e VI and the Heun operator [103] (see
also [104]). Likewise the spectrum of the Calogero-Moser system should make contact with the τ
function describing the isomonodromic deformations on the torus [105]. The details will appear
somewhere else [106].
The situation for Painlev´ e I, II, IV is more subtle since these correspond to Argyres–Douglas
theories of typeH0,H 1,H 2, respectively [107]. At present we do not know how to write Nakajima-
Yoshioka blowup equations for these theories. Nevertheless, it should be possible to connect the
NS limit to the selfdual limit of the Ω background also in these theories, since the Hi theories
can be derived from SU (2) gauge theories with Nf = 1, 2, 3 upon a suitable limiting procedure
[108, 109]. By following [110, 111], such connection would provide a relation between the exact
spectrum of the quantum SW curves underlying the H0,H 1,H 2 theories, and Painlev´ e I, II, IV
tau functions. Note that the quantum SW curve of the H0 and H1 theories correspond to the
cubic and quartic oscillators, respectively. Connections between Painlev´ e equations and the above
quantum mechanical systems have been observed in [112–115].
Acknowledgements
We would like to thank Vladimir Bazhanov, Katsushi Ito, Davide Gaiotto, Qianyu Hao, Lotte
Hollands, Amir-Kian Kashani–Poor, Sergei Lukyanov, Davide Masoero, Gregory Moore, Andy
Neitzke, Stefano Negro, Nikita Nekrasov, Hongfei Shu, Leon Takhtajan, Roberto Tateo and Peter
Wittwer for useful discussions and correspondence. The work of J.G. and M.M. is supported in
part by the Fonds National Suisse, subsidy 200021-175539 and by the NCCR 51NF40-182902
“The Mathematics of Physics” (SwissMAP).
A The four dimensional SU (N ) spectral determinant
In this Appendix we explain how the exact formula (5.6) can be extended to the family of
operators studied in [18]. These operators have the form,
HN = ΛN(
ep + e−p)
+
N−1∑
k=0
(−1)kxN−khk, [x, p] = iℏ, (A.1)
where N ≥ 2 is a positive integer and we set h0 = 1, h1 = 0. They can be regarded as
deformations of the standard non-relativistic Schr¨ odinger operators with a polynomial potential.
When N is even, they have a discrete spectrum and their inverses are of trace class. When
N is odd, one can perform a standard analytic continuation and obtain a discrete spectrum of
resonances, as explained in [18]. In both cases, one can deﬁne a Fredholm determinant as
ΞN(h2,··· ,hN) = det
(
1 +hN(−1)N
HN
)
. (A.2)
– 37 –
Here,h2,··· ,hN−1 are the moduli appearing in the potential, while (−1)N−1hN can be identiﬁed
with the energy and is the standard auxiliary variable appearing in the deﬁnition of Fredholm
determinants.
As explained in [18], we can engineer the following operator from the quantum mirror curve
to the YN,0 geometry. We follow [18] and deﬁne
γ = 1
2
N∑
i=1
(−1)i−1ei, (A.3)
whereei are the weights of the fundamental representation of SU (N). We denote by
WN·γ ={w(γ) :w∈W N} (A.4)
the Weyl orbit of γ, and we introduce
a =
N−1∑
j=1
aiλ, (A.5)
where{λi}i=1,···,N−1 are the fundamental weights ofSU (N). The quantities ai are related to the
parametershi in (A.1) by using the four dimensional mirror maps or quantum Matone relations
(see for instance eqs (3.95)–(3.107) in [18] and reference therein). For instance, we have
h2 (a; ℏ) = lim
ϵ2→0
(
− 1
Z
∑
Y
(
(−1)NΛ2N)𝓁(Y )
C2(a,Y )ZY
)
,
h3 (a; ℏ) = lim
ϵ2→0
(
2
Z
∑
Y
(
(−1)NΛ2N)𝓁(Y )
C3(a,Y )ZY
)
,
(A.6)
whereZY,Z are deﬁned in (4.9) and (4.8), and Y is a vector of Young diagrams as in (4.4).
Moreover,
C2(a,Y ) = 1
2
N∑
I=1
α2
I− iℏϵ2𝓁(Y ),
C3(a,Y ) = iℏϵ2
(
iℏ +ϵ2
2 𝓁(Y ) + iℏ
N∑
I=1
c2(Yt
I ) +ϵ2
N∑
I=1
c2(YI)−
N∑
I=1
αI𝓁(YI)
)
+ 1
6
N∑
I=1
α3
I,
(A.7)
where 𝓁(Y ) is deﬁned in (4.6) and we use
c2(Y ) = 1
2
∑
i≥1
yi(yi− 1). (A.8)
We also denote
ai =αi−αi+1, i = 1,··· ,N− 1, (A.9)
– 38 –
with
N∑
i=1
αi = 0. (A.10)
With a procedure analogous to the one of section 5.1, we obtain the explicit formula
ΞN(h2,··· ,hN) =AN(ℏ, Λ,h 2,··· hN−1)
∑
n∈WN·γ
eJ 4d
n . (A.11)
The quantity eJ 4d
n is deﬁned as follows. If N is even we have:
eJ 4d
n = exp
( i
ℏ
∂FNS
∂a ·n
) ∏
α∈∆+
(
2 sinh
(πa·α
ℏ
))−(n·α)2
, (A.12)
while if N is odd we have
eJ 4d
n = exp
( i
ℏ
∂FNS
∂a ·n− π
ℏa·n
) ∏
α∈∆+
(
2 sinh
(πa·α
ℏ
))−(n·α)2
, (A.13)
where FNS is deﬁned in (4.12). The quantity AN(ℏ, Λ,h 2,··· hN−1) is an integration constant,
analogous to A(ℏ) in (5.6), which now depends on the moduli h2,··· ,hN−1. The above spectral
determinant vanishes precisely when the quantization conditions obtained in [18] are satisﬁed.
When N = 2 we recover exactly the result (5.6). When N = 3 we have
Ξ3(h3,h 2) =A3(ℏ, Λ,h 2)
[
1 + 1− e−2πa1/ℏ
1− e−2π(a1+a2)/ℏ e−2πa2/ℏeiφ2 + 1− e−2πa2/ℏ
1− e−2π(a1+a2)/ℏ eiφ1
]
× csch
(πa1
ℏ
)
csch
(πa2
ℏ
)
e−π(a1−a2)
3ℏ −i 1
3 (φ1+φ2),
(A.14)
where φi, i = 1, 2, are deﬁned as [18]
φ1(a1,a 2; ℏ) = 1
ℏ
(∂FNS
∂a2
− 2∂FNS
∂a1
)
, φ 2(a1,a 2; ℏ) = 1
ℏ
(
2∂FNS
∂a2
− ∂FNS
∂a1
)
. (A.15)
We have tested (A.14) by expanding the r.h.s of (A.14) around h3 = 0 and comparing with the
numerical values of the spectral traces. We ﬁnd perfect agreement.
B Zamolodchikov’s TBA equation for the modiﬁed Mathieu equation
In [116] Zamolodchikov considered the thermodynamic TBA ansatz for the sinh-Gordon model.
This model depends on the parameter b∈ C, and we introduce
Q =b + 1
b, (B.1)
as well as
p = b2
1 +b2, a = 1− 2p = 1−b2
1 +b2. (B.2)
The TBA equation for this theory is given by
ϵ(θ) =mR cosh(θ)− (φ⋆L ) (θ), (B.3)
– 39 –
In this equation, R is the radius of the circle where the theory lives, m is the mass of the particle
in the spectrum,
L(θ) = log
(
1 + e−ϵ(θ)
)
, (B.4)
and
φ(θ) = 1
2π
( 1
cosh(θ− iπa/2) + 1
cosh(θ + iπa/2)
)
= 1
2π
4 sin(πp) cosh(θ)
cosh(2θ)− cos(2πp). (B.5)
The ⋆ in (B.3) denotes, as it is standard, the convolution
(f ⋆g) (θ) =
∫
R
f(θ−θ′)g(θ′)dθ′. (B.6)
The ground state energy is then given by
E(R) =−m
2π
∫
R
cosh(θ)L(θ)dθ, (B.7)
and the eﬀective central charge is
ceﬀ =−6R
π E(R). (B.8)
The formal conformal limit of the above TBA equation was analyzed in [19] in relation to
the generalized Mathieu equation
−u′′(x) +
(
µ−e−bx +µ+ebx
)
u(x) =−P 2u(x). (B.9)
The parameters µ± have the following obvious symmetry
µ+→µ+e−ε/b , µ −→µ−e+εb , x →x +ε , (B.10)
and therefore only the combination
µ =µb
+µ1/b
− (B.11)
matters. The parameter b is identiﬁed with the parameter of the sinh-Gordon model, µ corre-
sponds to its coupling constant, while the energy
E =−P 2 (B.12)
is identiﬁed with the Liouville momentum, and enters into the eﬀective central charge of the
theory, see (B.28). In the conformal limit, the TBA equation (B.3) becomes
ϵ(θ) =πeθ− 2 (φ⋆L ) (θ). (B.13)
The dependence on P comes through as the boundary condition of the TBA solution when
θ→−∞ ,
ϵ(θ)∼ 4QPθ− 2C(P ) +··· (B.14)
where P >0 and
C(P ) = log Γ(2P )Γ(1 + 2P )
2π + 4P log 16√π
Γ(1/4)2 . (B.15)
– 40 –
It is then argued in [116] that the Fredholm determinant of the generalized Mathieu equation is
given by [19]
Ξ(µ,P ) = X(µ,P )
X(µ, 0), (B.16)
where
X(µ,P ) = exp [−ϵ(θ,P )/2] (B.17)
andµ is related to θ by (5.30). We have indicated the explicit dependence of ϵ onP through the
boundary condition (B.14).
The ordinary modiﬁed Mathieu equation is obtained when
b = 1, µ − =µ+ =µ. (B.18)
Let us focus on this case. The TBA equation becomes
ϵ(θ) =πeθ−
∫
R
L(θ′)
cosh(θ−θ′)
dθ′
π . (B.19)
To impose the boundary condition (B.14), we use a trick due to Zamolodchikov. We ﬁrst note
that, as a consequence of (B.14), we have
L(θ)∼− 8Pθ + 2C(P ), θ →−∞, (B.20)
and we introduce the function
L0(θ) = 4P log(1 + e−2θ), (B.21)
which has the same leading asymptotics than L(θ),
L0(θ)∼− 8Pθ +O(e−|θ|), θ →−∞. (B.22)
We have
f0 = 2φ⋆L 0 = 8P log(1 + e−θ), (B.23)
and we can rewrite the TBA equation as
ϵ(θ) =πeθ−f0− 2φ⋆ (L−L0). (B.24)
This has by construction the right asymptotic behavior (B.14).
One property of (B.19) which is relevant for our analysis is the following. The asymptotic
behavior of the solution ϵ(θ) as θ→∞ is of the form
ϵ(θ) =πeθ +ϵ(1)e−θ +··· , (B.25)
where
ϵ(1) =− 2
π
∫
R
eθ log
(
1 + e−ϵ(θ)
)
dθ. (B.26)
On the other hand, this correction is proportional to the eﬀective central charge of the theory 10,
ceﬀ = 6
π
∫
R
eθ log
(
1 + e−ϵ(θ)
)
dθ =−3ϵ(1), (B.27)
which according to [19] can be computed in terms of P only
ceﬀ = 1 + 24P 2. (B.28)
This means that
ϵ(1) =−1
3
(
1 + 24P 2)
. (B.29)
10There is a factor of 2 missing in eq. (4.4) of [19].
– 41 –
References
[1] N. A. Nekrasov and S. L. Shatashvili, Quantization of integrable systems and four dimensional
gauge theories, in 16th International Congress on Mathematical Physics, Prague, August 2009,
265-289, World Scientiﬁc 2010 , 2009. 0908.4052.
[2] A. Grassi, Y. Hatsuda and M. Mari˜ no, Topological strings from quantum mechanics, Annales
Henri Poincar´ e17 (2016) 3177–3235, [ 1410.3382].
[3] S. Codesido, A. Grassi and M. Mari˜ no, Spectral theory and mirror curves of higher genus , Annales
Henri Poincar´ e18 (2017) 559–622, [ 1507.02096].
[4] M. Mari˜ no,Spectral Theory and Mirror Symmetry , Proc. Symp. Pure Math. 98 (2018) 259,
[1506.07757].
[5] D. Gaiotto, G. W. Moore and A. Neitzke, Four-dimensional wall-crossing via three-dimensional
ﬁeld theory, Commun. Math. Phys. 299 (2010) 163–224, [ 0807.4723].
[6] D. Gaiotto, G. W. Moore and A. Neitzke, Wall-crossing, Hitchin Systems, and the WKB
Approximation, 0907.3987.
[7] D. Gaiotto, Opers and TBA , 1403.6137.
[8] K. Ito, M. Mari˜ no and H. Shu, TBA equations and resurgent Quantum Mechanics , JHEP 01
(2019) 228, [ 1811.04812].
[9] M. Mari˜ no,From resurgence to BPS states , talk given at the conference Strings 2019, Brussels,
https://livestream.com/accounts/7777696/events/8742238/videos/193704304, 2019.
[10] M. Mari˜ no and S. Zakany,Matrix models from operators and topological strings , Annales Henri
Poincar´ e17 (2016) 1075–1108, [ 1502.02958].
[11] A. Mironov and A. Morozov, Nekrasov functions and exact Bohr–Sommerfeld integrals , JHEP
1004 (2010) 040, [ 0910.5670].
[12] W. He and Y.-G. Miao, Mathieu equation and elliptic curve , Commun. Theor. Phys. 58 (2012)
827–834, [1006.5185].
[13] M.-x. Huang, On gauge theory and topological string in Nekrasov–Shatashvili limit , JHEP 06
(2012) 152, [ 1205.3652].
[14] G. Ba¸ sar and G. V. Dunne, Resurgence and the Nekrasov–Shatashvili limit: Connecting weak and
strong coupling in the Mathieu and Lam´ e systems, JHEP 02 (2015) 160, [ 1501.05671].
[15] A.-K. Kashani-Poor and J. Troost, PureN = 2 super Yang–Mills and exact WKB , JHEP 08
(2015) 160, [ 1504.08324].
[16] S. K. Ashok, D. P. Jatkar, R. R. John, M. Raman and J. Troost, Exact WKB analysis of N = 2
gauge theories, JHEP 07 (2016) 115, [ 1604.05520].
[17] S. Codesido, M. Mari˜ no and R. Schiappa, Non-Perturbative Quantum Mechanics from
Non-Perturbative Strings, Annales Henri Poincare 20 (2019) 543–603, [ 1712.02603].
[18] A. Grassi and M. Mari˜ no,A Solvable Deformation of Quantum Mechanics , SIGMA 15 (2019) 025,
[1806.01407].
[19] A. B. Zamolodchikov, Generalized Mathieu equations and Liouville TBA , in Quantum Field
Theories in Two Dimensions , vol. 2. World Scientiﬁc, 2012.
[20] A. Voros, Spectre de l’´ equation de Schr¨ odinger et m´ ethode BKW. Publications Math´ ematiques
d’Orsay, 1981.
[21] A. Voros, The return of the quartic oscillator. The complex WKB method , Annales de l’I.H.P.
Physique Th´ eorique39 (1983) 211–338.
[22] E. Delabaere, H. Dillinger and F. Pham, Exact semiclassical expansions for one-dimensional
quantum oscillators , J. Math. Phys. 38 (1997) 6126–6184.
[23] K. Iwaki and T. Nakanishi, Exact WKB analysis and cluster algebras , J. Phys. A 47 (2014)
474009.
– 42 –
[24] R. Balian, G. Parisi and A. Voros, Quartic oscillator , in Feynman Path Integrals, vol. 106,
pp. 337–360. Springer–Verlag, 1979.
[25] W. Lerche, Introduction to Seiberg-Witten theory and its stringy origin , Nucl. Phys. Proc. Suppl.
55B (1997) 83–117, [ hep-th/9611190].
[26] A. Marshakov, Seiberg-Witten theory and integrable systems . World Scientiﬁc, 1999.
[27] N. Seiberg and E. Witten, Electric-magnetic duality, monopole condensation, and conﬁnement in
N = 2 supersymmetric Yang–Mills theory, Nucl. Phys. B426 (1994) 19–52, [ hep-th/9407087].
[28] M. Matone, Instantons and recursion relations in N = 2 SUSY gauge theory , Phys. Lett. B357
(1995) 342–348, [ hep-th/9506102].
[29] R. Flume, F. Fucito, J. F. Morales and R. Poghossian, Matone’s relation in the presence of
gravitational couplings, JHEP 04 (2004) 008, [ hep-th/0403057].
[30] G. Ba¸ sar, G. V. Dunne and M. ¨Unsal, Quantum geometry of resurgent
perturbative/non-perturbative relations, JHEP 05 (2017) 087, [ 1701.06572].
[31] A. Gorsky and A. Milekhin, RG-Whitham dynamics and complex Hamiltonian systems , Nucl.
Phys. B895 (2015) 33–63, [ 1408.0425].
[32] S. Codesido and M. Mari˜ no,Holomorphic Anomaly and Quantum Mechanics , J. Phys. A51
(2018) 055402, [ 1612.07687].
[33] I. Aniceto, G. Basar and R. Schiappa, A Primer on Resurgent Transseries and Their Asymptotics ,
Phys. Rept. 809 (2019) 1–135, [ 1802.10441].
[34] H.-Y. Chen, N. Dorey and K. Petunin, Wall Crossing and Instantons in Compactiﬁed Gauge
Theory, JHEP 06 (2010) 024, [ 1004.0703].
[35] M. Kontsevich and Y. Soibelman, Stability structures, motivic Donaldson-Thomas invariants and
cluster transformations, 0811.2435.
[36] F. Ferrari and A. Bilal, The Strong coupling spectrum of the Seiberg-Witten theory , Nucl. Phys.
B469 (1996) 387–402, [ hep-th/9602082].
[37] A. Klemm, W. Lerche, P. Mayr, C. Vafa and N. P. Warner, Selfdual strings and N=2
supersymmetric ﬁeld theory, Nucl. Phys. B477 (1996) 746–766, [ hep-th/9604034].
[38] L. F. Alday, J. Maldacena, A. Sever and P. Vieira, Y-system for Scattering Amplitudes , J. Phys.
A43 (2010) 485401, [ 1002.2459].
[39] T. R. Klassen and E. Melzer, Purely Elastic Scattering Theories and their Ultraviolet Limits ,
Nucl. Phys. B338 (1990) 485–528.
[40] M. Mari˜ no, R. Schiappa and M. Weiss,Nonperturbative eﬀects and the large-order behavior of
matrix models and topological strings , Commun. Num. Theor. Phys. 2 (2008) 349–419,
[0711.1954].
[41] K. Ito and H. Shu, Generalized ODE/IM correspondence and its application to N=2 gauge
theories, poster presented at the conference String Math 2018 (2018) .
[42] L. Hollands and A. Neitzke, Exact WKB and abelianization for the T3 equation, 1906.04271.
[43] A. B. Zamolodchikov, Resonance factorized scattering and roaming trajectories, J. Phys. A39
(2006) 12847–12862.
[44] A. B. Zamolodchikov, Thermodynamic Bethe Ansatz in Relativistic Models. Scaling Three State
Potts and Lee-Yang Models, Nucl. Phys. B342 (1990) 695–720.
[45] N. A. Nekrasov, Seiberg–Witten prepotential from instanton counting, Adv. Theor. Math. Phys. 7
(2004) 831–864, [ hep-th/0206161].
[46] N. Nekrasov and A. Okounkov, Seiberg-Witten theory and random partitions , Prog. Math. 244
(2006) 525–596, [ hep-th/0306238].
[47] R. Flume and R. Poghossian, An Algorithm for the microscopic evaluation of the coeﬃcients of
the Seiberg-Witten prepotential, Int. J. Mod. Phys. A18 (2003) 2541, [ hep-th/0208176].
– 43 –
[48] U. Bruzzo, F. Fucito, J. F. Morales and A. Tanzini, Multiinstanton calculus and equivariant
cohomology, JHEP 05 (2003) 054, [ hep-th/0211108].
[49] M. Aganagic, M. C. Cheng, R. Dijkgraaf, D. Kreﬂ and C. Vafa, Quantum geometry of reﬁned
topological strings, JHEP 1211 (2012) 019, [ 1105.0630].
[50] A. S. Losev, A. Marshakov and N. A. Nekrasov, Small instantons, little strings and free fermions ,
hep-th/0302191.
[51] M. Bullimore and H.-C. Kim, The Superconformal Index of the (2,0) Theory with Defects , JHEP
05 (2015) 048, [ 1412.3872].
[52] M. Bullimore, H.-C. Kim and P. Koroteev, Defects and Quantum Seiberg-Witten Geometry , JHEP
05 (2015) 095, [ 1412.6081].
[53] F. Fucito, J. F. Morales and R. Poghossian, Wilson loops and chiral correlators on squashed
spheres, JHEP 11 (2015) 064, [ 1507.05426].
[54] A. Sciarappa, Bethe/Gauge correspondence in odd dimension: modular double, non-perturbative
corrections and open topological strings, JHEP 10 (2016) 014, [ 1606.01000].
[55] Y. Hatsuda and M. Mari˜ no,Exact quantization conditions for the relativistic Toda lattice , JHEP
05 (2016) 133, [ 1511.02860].
[56] K. Kozlowski and J. Teschner, TBA for the Toda chain , 1006.2906.
[57] M. C. Gutzwiller, The Quantum Mechanical Toda Lattice, Annals Phys. 124 (1980) 347.
[58] B. Simon, Notes on inﬁnite determinants of Hilbert space operators , Advances in Mathematics 24
(1977) 244.
[59] A. Laptev, L. Schimmer and L. A. Takhtajan, Weyl type asymptotics and bounds for the
eigenvalues of functional-diﬀerence operators for mirror curves , Geom. Funct. Anal. 26 (2016)
288–305, [1510.00045].
[60] J. Kallen and M. Mari˜ no,Instanton eﬀects and quantum spectral curves , Annales Henri Poincar´ e
17 (2016) 1037–1074, [ 1308.6485].
[61] M.-x. Huang and X.-f. Wang, Topological strings and quantum spectral problems, JHEP 1409
(2014) 150, [ 1406.6178].
[62] S. Codesido, A. Grassi and M. Mari˜ no, Exact results in N=8 Chern-Simons-matter theories and
quantum geometry, JHEP 1507 (2015) 011, [ 1409.1799].
[63] S. L. Lukyanov, unpublished, .
[64] S. H. Katz, A. Klemm and C. Vafa, Geometric engineering of quantum ﬁeld theories , Nucl.Phys.
B497 (1997) 173–195, [ hep-th/9609239].
[65] G. Bonelli, A. Grassi and A. Tanzini, Seiberg–Witten theory as a Fermi gas , Lett. Math. Phys.
107 (2017) 1–30, [ 1603.01174].
[66] A. Voros, The zeta function of the quartic oscillator , Nucl. Phys. B165 (1980) 209–236.
[67] A. Gorsky, A. Milekhin and N. Sopenko, Bands and gaps in Nekrasov partition function , JHEP
01 (2018) 133, [ 1712.02936].
[68] M. Beccaria, On the large Ω-deformations in the Nekrasov-Shatashvili limit of N = 2∗ SYM,
JHEP 07 (2016) 055, [ 1605.00077].
[69] P. Dorey and R. Tateo, Anharmonic oscillators, the thermodynamic Bethe ansatz, and nonlinear
integral equations, J.Phys. A32 (1999) L419–L425, [ hep-th/9812211].
[70] P. Dorey, C. Dunning and R. Tateo, The ODE/IM Correspondence, J. Phys. A40 (2007) R205,
[hep-th/0703066].
[71] S. L. Lukyanov, Critical values of the Yang-Yang functional in the quantum sine-Gordon model ,
Nucl. Phys. B853 (2011) 475–507, [ 1105.2836].
[72] V. Y. Novokshenov, Movable poles of the solutions of painleve’s equation of the third kind and
their relation with mathieu functions , Functional Analysis and Its Applications 20 (1986) 113–123.
– 44 –
[73] A. Sciarappa, Exact relativistic Toda chain eigenfunctions from Separation of Variables and gauge
theory, JHEP 10 (2017) 116, [ 1706.05142].
[74] A. Grassi and M. Mari˜ no,The complex side of the TS/ST correspondence , J. Phys. A52 (2019)
055402, [1708.08642].
[75] A. Grassi and J. Gu, BPS relations from spectral problems and blowup equations , Lett. Math.
Phys. 109 (2019) 1271–1302, [ 1609.05914].
[76] O. Gamayun, N. Iorgov and O. Lisovyy, How instanton combinatorics solves Painlev´ e VI, V and
IIIs, J. Phys. A46 (2013) 335203, [ 1302.1832].
[77] A. Its, O. Lisovyy and Yu. Tykhyy, Connection problem for the sine-Gordon/Painlev´ e III tau
function and irregular conformal blocks , Int. Math. Res. Notices 18 (2015) 8903–8924,
[1403.1235].
[78] P. Gavrylenko and O. Lisovyy, PureSU (2) gauge theory partition function and generalized Bessel
kernel, Proc. Symp. Pure Math. 18 (2018) 181–208, [ 1705.01869].
[79] H. Nakajima and K. Yoshioka, Instanton counting on blowup. I , Invent. Math. 162 (2005)
313–355, [math/0306198].
[80] H. Nakajima and K. Yoshioka, Instanton counting on blowup. II. K-theoretic partition function ,
math/0505553.
[81] H. Nakajima and K. Yoshioka, Lectures on instanton counting, in CRM Workshop on Algebraic
Structures and Moduli Spaces Montreal, Canada, July 14-20, 2003 , 2003. math/0311058.
[82] K. Sun, X. Wang and M.-x. Huang, Exact Quantization Conditions, Toric Calabi-Yau and
Nonperturbative Topological String, JHEP 01 (2017) 061, [ 1606.07330].
[83] X. Wang, G. Zhang and M.-x. Huang, New exact quantization condition for toric Calabi–Yau
geometries, Phys. Rev. Lett. 115 (2015) 121601, [ 1505.05360].
[84] S. Franco, Y. Hatsuda and M. Mari˜ no,Exact quantization conditions for cluster integrable
systems, J. Stat. Mech. 1606 (2016) 063107, [ 1512.03061].
[85] M. A. Bershtein and A. I. Shchechkin, Bilinear equations on Painlev´ eτ functions from CFT ,
Commun. Math. Phys. 339 (2015) 1021–1061, [ 1406.3008].
[86] M. Bershtein and A. Shchechkin, Painlev equations from NakajimaYoshioka blowup relations , Lett.
Math. Phys. 109 (2019) 2359–2402, [ 1811.04050].
[87] N. Nekrasov, “Some applications of defects in supersymmetric gauge theory.” Talk given at IHES
January 2019.
[88] N. Iorgov, O. Lisovyy and J. Teschner, Isomonodromic tau-functions from Liouville conformal
blocks, Commun. Math. Phys. 336 (2015) 671–694, [ 1401.6104].
[89] M. A. Bershtein and A. I. Shchechkin, q-deformed Painlev´ eτ function and q-deformed conformal
blocks, J. Phys. A50 (2017) 085202, [ 1608.02566].
[90] M. Jimbo, H. Nagoya and H. Sakai, CFT approach to the q-Painlev´ e VI equation, Journal of
Integrable Systems 2 (09, 2017) .
[91] M. R. Douglas, B. Fiol and C. Romelsberger, The Spectrum of BPS branes on a noncompact
Calabi-Yau, JHEP 09 (2005) 057, [ hep-th/0003263].
[92] R. Eager, S. A. Selmani and J. Walcher, Exponential Networks and Representations of Quivers ,
JHEP 08 (2017) 063, [ 1611.06177].
[93] S. Banerjee, P. Longhi and M. Romo, Exploring 5d BPS Spectra with Exponential Networks ,
Annales Henri Poincare 20 (2019) 4055–4162, [ 1811.02875].
[94] T. Dimofte, S. Gukov, J. Lenells and D. Zagier, Exact Results for Perturbative Chern-Simons
Theory with Complex Gauge Group , Commun. Num. Theor. Phys. 3 (2009) 363–443, [ 0903.2472].
[95] J. Ellegaard Andersen and R. Kashaev, A TQFT from Quantum Teichm¨ uller Theory, Commun.
Math. Phys. 330 (2014) 887–934, [ 1109.6295].
[96] S. Gukov, M. Mari˜ no and P. Putrov,Resurgence in complex Chern-Simons theory , 1605.07615.
– 45 –
[97] D. Gang and Y. Hatsuda, S-duality resurgence in SL(2) Chern-Simons theory , JHEP 07 (2018)
053, [1710.09994].
[98] J. E. Andersen and W. E. Petersen, Resurgence Analysis of Quantum Invariants: Seifert
Manifolds and Surgeries on The Figure Eight Knot , 1811.05376.
[99] T. Dimofte, D. Gaiotto and S. Gukov, Gauge Theories Labelled by Three-Manifolds , Commun.
Math. Phys. 325 (2014) 367–419, [ 1108.4389].
[100] A. B. Zamolodchikov, Painleve III and 2-d polymers , Nucl.Phys. B432 (1994) 427–456,
[hep-th/9409108].
[101] P. Fendley, Airy functions in the thermodynamic Bethe ansatz , Lett. Math. Phys. 49 (1999)
229–233, [hep-th/9906114].
[102] S. Cecotti, A. Neitzke and C. Vafa, Twistorial topological strings and a tt∗ geometry forN = 2
theories in 4d, Adv. Theor. Math. Phys. 20 (2016) 193–312, [ 1412.4793].
[103] A. Litvinov, S. Lukyanov, N. Nekrasov and A. Zamolodchikov, Classical Conformal Blocks and
Painleve VI, JHEP 07 (2014) 144, [ 1309.4700].
[104] M. Lencss and F. Novaes, Classical Conformal Blocks and Accessory Parameters from
Isomonodromic Deformations, JHEP 04 (2018) 096, [ 1709.03476].
[105] G. Bonelli, F. Del Monte, P. Gavrylenko and A. Tanzini, N = 2∗ gauge theory, free fermions on
the torus and Painlev´ e VI, 1901.10497.
[106] M. Bershtein, P. Gavrylenko and A. Grassi, “In preparation.”.
[107] G. Bonelli, O. Lisovyy, K. Maruyoshi, A. Sciarappa and A. Tanzini, On painlev´ e/gauge theory
correspondence, Letters in Mathematical Physics 107 (Dec, 2017) 2359–2413.
[108] P. C. Argyres and M. R. Douglas, New phenomena in SU(3) supersymmetric gauge theory , Nucl.
Phys. B448 (1995) 93–126, [ hep-th/9505062].
[109] P. C. Argyres, M. R. Plesser, N. Seiberg and E. Witten, New N=2 superconformal ﬁeld theories in
four-dimensions, Nucl. Phys. B461 (1996) 71–84, [ hep-th/9511154].
[110] A. Grassi and J. Gu, Argyres-Douglas theories, Painlev´ e II and quantum mechanics, JHEP 02
(2019) 060, [ 1803.02320].
[111] K. Ito and H. Shu, ODE/IM correspondence and the Argyres-Douglas theory , JHEP 08 (2017)
071, [1707.03596].
[112] D. Masoero, Poles of Integrale Tritronquee and Anharmonic Oscillators. Asymptotic localization
from WKB analysis , Nonlinearity 23 (2010) 2501, [ 1002.1042].
[113] D. Masoero, Poles of integrale tritronqu´ ee and anharmonic oscillators. A WKB approach, J. Phys.
A 43 (2010) 2501, [ 0909.5537].
[114] V. Novokshenov, Poles of Tritronqu´ ee Solution to the Painlev´ e I Equation and Cubic Anharmonic
Oscillator, Reg. Chaotic Dyn. 15 (2010) 390–403.
[115] C. M. Bender and J. Komijani, Painlev´ e Transcendents and PT-Symmetric Hamiltonians, J.
Phys. A48 (2015) 475202, [ 1502.04089].
[116] A. B. Zamolodchikov, On the thermodynamic Bethe ansatz equation in sinh-Gordon model , J.
Phys. A39 (2006) 12863–12887, [ hep-th/0005181].
– 46 –
