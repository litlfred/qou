---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-011-7-conclusion
section_title: "Conclusion"
section_number: 7
pages: 25-34
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
In this paper we show that the growth of Young diagrams equipped with Plancherel measure can be
studied through a simple unitary matrix model, namely Gross-Witten-Wadia model. Considering
the growth process to be Markovian and governed by Plancherel probability naturally we write
down a partition function for such growth process. Plancherel growth also serves as an interesting
toy model to study growth or melting of2d crystals [8, 53]. Strictly speaking, the partition function
can be evaluated exactly as one can explicitly perform the sum over all possible representations.
However, in order to capture the growth process via saddle point analysis in the limit of large box
number, we introduce a cut-oﬀ N on the number of rows in the Young diagrams. The regularised
partition function turns out to be identical to that of the GWW model with N playing the role of
the rank of the gauge group. We performed a saddle point analysis of the regularised partition
function and ﬁnd that in the continuum limit the partition function is dominated by a class of
diagrams. The class is isomorphic to no-gap phase of GWW model. Di ﬀerent diagrams in this
class are characterised by a single parameter 0 < ξ < 1/2. The limiting diagram ξ → 1/2
corresponds to limit shape and mapped to GWW transition point in the eigenvalue side. This
gives an alternate proof of the limit shape theorem of large Young diagrams [3, 4] . In [5], Kerov
introduced a diﬀerential model for the growth of Young diagrams, known as the automodel. We
ﬁnd that in continuum limit the above one parameter class of diagrams falls in the automodel class
of Kerov with renormalised box number playing the role of time.
There exists a correspondence between unitary matrix models and free Fermi droplets in two di-
mensions. Using this correspondence, we see that the evolution of Young diagrams in automodel
class can be mapped to diﬀerent shapes of incompressible ﬂuid droplets in two dimensions. Auto-
model evolution corresponds to area preserving deformation of these ﬂuid droplets. Such identiﬁ-
cation was possible due to the equivalence between GWW model and automodel partition function
[7]. Since eigenvalues of unitary matrices behave like position of free fermions, two dimensional
ﬂuid droplets are identiﬁed with classical phase space of these free fermions [7, 18]. Although the
model under consideration is non-dynamical, we introduce time in an ad-hoc manner by identify-
ing our eigenvalue distribution with the Fermi distribution at zero temperature thus constructing
a one particle Hamiltonian. We subsequently use the techniques developed in [22] to provide a
Hilbert space description for the growth process of Young diagrams. In order to achieve this, we
25
quantise these free Fermi droplets and ﬁnd that the boundary modes satisfy Kac-Moody algebra.
Edge excitations of fractional quantum Hall ﬂuid also satisfy similar algebra [54]. We construct
the Hilbert space associated with the quantised droplets and identify a mapping between Young
diagrams and coherent states in the Hilbert space. Firstly, the ground state of the Hilbert space
corresponds to the circular shape of the Fermi surfaces and are identiﬁed with no box diagram.
Secondly, a generic excited state corresponds to O(1/N) ripples on the Fermi surface. Thirdly, a
O(1) deformation to the Fermi surfaces are captured by coherent states in the Hilbert space and is
mapped to regularised large N diagrams. Certain coherent states in the Hilbert space correspond
to automodel Young diagrams. Young diagrams in automodel class are characterised by a one pa-
rameter class of coherent states. Hence, growth of Young diagrams are mapped with evolution of
these coherent states in the Hilbert space. We also observe that the shape of arbitrary ﬂuctuations
matches with the ﬂuctuations of limit shape studied earlier by Ivanov and Olshanki. [9].
Acknowledgments: We are grateful to Rajesh Gopakumar, Debashis Ghoshal, Dileep Jatkar,
Parikshit Dutta, Nabamita Banerjee, Ashoke Sen for helpful and illuminating discussions. The
work of AC is supported by a Simons Foundation Grant Award ID 509116 and by the South
African Research Chairs initiative of the Department of Science and Technology and the National
Research Foundation. The work of SD is supported by the grant no. EMR /2016/006294 and
MTR/2019/000390 from the SERB, Government of India. SD also acknowledges the Simons
Associateship of the Abdus Salam ICTP, Trieste, Italy. AC and SD would like to thank the hos-
pitality of ICTP where part of the project was completed. We all indebted to people of India for
their unconditional support towards research in basic science.
Appendix A. Analysing Unitary Matrix Models
Appendix A.1. Eigenvalue analysis
In this section, we will brieﬂy review the eigenvalue analysis, the Young diagram analysis and
their connection in the context of the so-called single plaquette model. Interested readers may
refer to [18] for further details.
In the diagonal basis the partition function of the single plaquette model described by the action
(2.2) is given by (up to an overall volume dependent factor),
Z =
∫ N∏
i=1
dθi
∏
i< j
sin2
(θi−θ j
2
)
exp N
∑
n
2βn
n
N∑
i=1
cos nθi. (A.1)
In the large N limit, the discrete eigenvalues θi goes over to a smooth continuous function θ(x)
where x∈ [0, 1]. One can write down a saddle point equation in the continuum limit which is
given by
−
∫ 1
0
dy cot
(θ(x)−θ(y)
2
)
=
∑
n
βn cos nθ(x). (A.2)
26
Deﬁning a distribution function (called eigenvalue density) ρ(θ) for eigenvalues over a unit cir-
cle
ρ(θ) = 1
N
N∑
i=1
δ(θ−θi) = dx
dθ. (A.3)
the saddle point equation (A.2) can be recast as
−
∫
dθ′ cot
(θ−θ′
2
)
ρ(θ′) =
∑
n
βn cos nθ, with
∫
dθρ(θ) = 1. (A.4)
Appendix A.2. Young diagram analysis
The exponential appearing in the partition function of the single plaquette model can be expanded
into an inﬁnite series which runs over representations R of unitary group U(N),
Z =
∑
R
∑
⃗k
ε(⃗β,⃗k)
z⃗k
∑
⃗l
ε(⃗β,⃗l)
z⃗l
χR(C(⃗k))χR(C(⃗l)). (A.5)
Here χR(C(⃗k)) is the character of conjugacy class C(⃗k) of permutation group S K, K = ∑
n nkn
and
ε(⃗β,⃗k) =
∞∏
n=1
Nknβkn
n, z⃗k =
∞∏
n=1
kn!nkn. (A.6)
Sum of representations of S U(N) can be written as a sum over di ﬀerent Young diagrams. Say,
ni is the number of boxes in the i-th row of the Young diagram. We decompose the sum over
representations as a sum over all possible Young diagrams that one can draw for the symmetric
group. We introduce N new variables which are deﬁned as:
hi = ni + N− i ∀ i = 1,··· , N. (A.7)
hi’s are called hook numbers and they satisfy the following constraint
h1 > h2 >··· > hN≥ 0. (A.8)
In terms of the new variables hi, the partition function (A.5) is therefore given by,
Z =
∑
{hi}
∑
⃗k,⃗l
ε(⃗β,⃗k)ε(⃗β,⃗l)
z⃗kz⃗l
χ⃗h(C(⃗k))χ⃗h(C(⃗l)) (A.9)
where⃗h denotes a particular representation.
As before we deﬁne continuous variables in the large N limit
hi
N = h(x), kn = N2k′
n, x = i
N with x∈ [0, 1]. (A.10)
27
Writing characters χ⃗h in terms of h(x) and k′
n, partition function (A.5), in large N limit, can be
written as
Z =
∫
[dh(x)]
∏
n
∫
dk′
ndl′
n exp
[
−N2S h
e f f [h(x),⃗k′
n,⃗l′
n]
]
, (A.11)
where S h
e f f is the e ﬀective action in Young diagram basis. Dominant contribution to partition
function comes from those representations which minimise the e ﬀective action S h
e f f . To ﬁnd the
most dominant representations at large N, we introduce a function called Young tableaux density
deﬁned as,
u(h) =− dx
dh. (A.12)
Thus we see that the unitary matrix model under consideration can be expressed in two di ﬀerent
basis - eigenvalue basis (picture I) and Young diagram basis (picture II). Diﬀerent large N phases
can be characterised either by distributions of eigenvalues or Young diagrams. Therefore it is
expected that there is a relation between these two pictures. We now discuss this relation.
Appendix A.3. Finding the connection between two pictures
The character of permutation group is given by Frobenius formula
χR(C(⃗k)) =
∆(x)
∏
n
(Pn(x))kn

(h1,h2,···hN)
(A.13)
where
Pn(x) =
N∑
i=1
xn
i, ∆(x) =
∏
i< j
(xi− x j) (A.14)
and (x1,··· , xN) are set of auxiliary variables. The notation [··· ](h1,···,hN) implies
[ f (x)]
(h1,···,hN) = coeﬃcient of xh1
1 ··· xhN
N in f (x). (A.15)
Promoting N auxiliary variables to N complex variables ( z1,··· , zN), Frobenius formula (A.13)
can be written as a residue of a complex function as follows
χ[h(x), C(⃗k′)] =
( 1
2πi
)N ∮ [Dz(x)]
z(x) exp[−N2Sχ(h[x],⃗k′)]. (A.16)
This is subsequently used in (A.5) to obtain
Z =
∏
n
∫
dk′
ndl′
n
∫
[dh(x)]
∮
[dz(x)]
∮
[dw(x)]
∫ ∞
−∞
dt
∫ ∞
−∞
ds exp
(
−N2S total
[
h, z, w,⃗k′,⃗l′, t, s
])
(A.17)
28
where,
−S total
[
h, z, w,⃗k′,⃗l′, t, s
]
=
∑
n
[
k′
n
(
1 + ln
(βnZn
nk′
n
))
+ l′
n
(
1 + ln
(βnWn
nl′
n
))]
+ 1
2
∫ 1
0
dx−
∫ 1
0
dy (ln|z(x)− z(y)| + ln|w(x)− w(y)|)
−
∫ 1
0
dxh(x) lnz(x)w(x) + it

∑
n
nk′
n− K′
 + is

∑
n
nl′
n− K′
.
(A.18)
Extremising S total with respect to h(x), z(x), w(x), k′
n and l′
n, we see that the saddle point equations
are given by
∑
n
nk′
n
Zn
zn(x) +−
∫ 1
0
dy z(x)
z(x)− z(y)− h(x) = 0 (variation w.r.t z(x)) (A.19)
where,
Zn =
∫ 1
0
dxz n(x). (A.20)
Similar equation can be obtained when we vary action with respect tow(x). Variation with respect
to h(x) gives
z(x)w(x) = e−i(t+s) = constant (independent of x). (A.21)
Finally, variation with respect to k′
n and l′
n provides,
βnZn
nk′
n
= e−itn, and βnWn
nl′
n
= e−isn. (A.22)
Since the contours are unit circle around origin, one can take a consistent solution to the above
two equations (A.21,A.22) as
z(x) = eiθ(x), w(x) = e−iθ(x), t = s = 0 (A.23)
and
k′
n = l′
n = βnρn
n , where Zn =
∫
dθρ(θ) cosnθ≡ρn. (A.24)
Deﬁningρ(z) = dx
dz equation (A.19) can be written as
h(z) =⊖
∫
C
dz′ρ(z′) z
z− z′ +
∑
n
nk′
n
Zn
zn. (A.25)
We deﬁne a quantity ¯h(z)
¯h(z) =
∮
C
dz′ρ(z′) z
z− z′ +
∑
n
nk′
n
Zn
zn. (A.26)
29
¯h(z) is analytic everywhere in complex z plane except inside the support of ρ(z) on C. It has a
branch cuts along the support ofρ(z). If h+(z) and h−(z) are values of ¯h(z) on either sides of branch
cuts then we have
h±(z) = +
∑
n
nk′
n
Zn
zn +
∮
C
dz′ρ(z′) z
z− z′± iπzρ(z). (A.27)
Considering contour C to be unit circle we have
∑
n
nk′
n
Zn
einθ +−
∫ π
−π
dθρ(θ′) eiθ
eiθ− eiθ′− h±(θ)±πρ(θ) = 0 (A.28)
Evaluating the partition function (A.17) on equations (A.19,A.21, A.22) we ﬁnd,
Z =
∫
[Dθ] exp
N2
∞∑
n=1
2βn
nρn + N2 1
2−
∫
dθρ(θ)−
∫
dθ′ρ(θ′) ln
⏐⏐⏐⏐⏐⏐4 sin2
(θ−θ′
2
)⏐⏐⏐⏐⏐⏐
. (A.29)
Thus we see that the partition function is exactly same as the partition function of one plaquette
model written in eigenvalue basis (equation (A.1)) withρ(θ) being the eigenvalue density. Hence,
we identify the auxiliary variables we used to write the character of symmetric group with eigen-
values of the corresponding unitary matrix model involved.
Separating the saddlepoint equation (A.28) into real and imaginary part we see that the imaginary
part of this equation is same as the saddle point equation (5.9) for ρ(θ). Hence we are left with
only the real part, which is given by,
h±(θ) = 1
2 +
∑
n
βn cos nθ±πρ(θ). (A.30)
The above two relations can be written as a solution of a quadratic equation of h
h2− 2S (θ)h + S (θ)−π2ρ2(θ) = 0 (A.31)
where S (θ) = 1
2 + ∑
nβn cos nθ.
Appendix B. Spectral curve
Complexifying the above equation by replacingθ→− i ln z yields,
h(z)2− 2S (z)h(z) + S 2(z)−π2ρ2(z) = 0, S (z) = 1
2 +
∑
n
βn
2
(
z + z−1)
. (B.1)
h(z) is deﬁned on a two-sheeted cover of our original complex plane. The two sheets correspond
to the two solutions of the quadratic equation (B.1). The solutions are given by
h±(z) = S (z)±πρ(z). (B.2)
30
The analytic properties of h±(z) on two Riemann sheets depends on the ρ(z). S (z) is a known
meromorphic function with pole at z = 0. For no-gap solution πρ(z) = S (z) and hence h+(z) =
2S (z) and h(z) = 0. Therefore both h+(z) and h−(z) are analytic on both the Riemann sheets. There
is no way one can connect these two Riemann sheets. The resulting geometry is given by S 2∪ S 2
once we identify the points at inﬁnity for both the Riemann sheets separately.
For a s-gap solutionρ(z) has the following form [17]
ρ(z) =
√F(z)
2π , where F(z) = f (z)
s∏
i=1
(
z + ai + 1
z
)
, (B.3)
with ai , a j for i , j. ai is also real and−2≤ ai≤ 2,∀i. The function f (z) is analytic. Hence
h±(z) has s branch cuts on unit circles on both the Riemann sheets. One can, therefore, glue these
two Riemann sheets along s cuts. As a result, the geometry is given by a genus g = s− 1 Riemann
surface.
Appendix C. Asymmetric solutions
In large k limit the matrix model (4.5) renders another class of solution [7]. This solution is given
by
u(h) = 2
π cos−1

h +ξ− 1/2
2
√
ξh
, for p≤ h≤ q
= 0 otherwise
(C.1)
where,
√p =
√
ξ− 1√
2
, and √q =
√
ξ + 1√
2
(C.2)
and fugacity z (or a) is given by
z = 4ξ2
4ξ− 1. (C.3)
The solution is valid forξ >1/2. The Young diagrams for this distribution is not symmetric under
transposition.
This is a valid solution in the context of GWW model. In case of GWW model the sum in equation
(4.11) was over the representations of unitary group U(N) for which the maximum number of
boxes in the ﬁrst column of a Young diagram is N. Therefore, the symmetric representation fails
to be a valid solution of GWW when the ﬁrst column saturates this bound. As a result, GWW
model undergoes a third order phase transition at ξ = 1/2, known as Gross-Witten-Wadia phase
transition.
However we are dealing with partition function (3.2) where the sum is running over the represen-
tations of symmetric group. In this case there is no such restriction on N (number of boxes in the
ﬁrst column). Thus we do not see any such phase transition here.
31
References
[1] S. Kerov, Asymptotic Representation Theory of the Symmetric Group and its Application in Analysis . Transla-
tions of mathematical monographs, American Mathematical Society, 2003.
[2] A. Hora, The limit shape problem for ensembles of Young diagrams . Springerbriefs in mathematical physics,
Tokyo: Springer, 2016.
[3] A. Vershik and S. Kerov, “Asymptotics of the Plancherel measure of the symmetric group and the limiting form
of Young tableaux,”Dokl. Akad. Nauk, vol. 233, pp. 1024–1027, 1977.
[4] B. Logan and L. Shepp, “A variational problem for random Young tableaux,”Advances in Mathematics, vol. 26,
pp. 206–222, 1977.
[5] S. V . Kerov, “A Diﬀerential Model Of Growth Of Young Diagrams,”Proceedings of St.Petersburg Mathematical
Society, 1996.
[6] V . A. Kazakov, M. Staudacher, and T. Wynter, “Character expansion methods for matrix models of dually
weighted graphs,” Commun. Math. Phys., vol. 177, pp. 451–468, 1996, hep-th/9502132.
[7] S. Dutta and R. Gopakumar, “Free fermions and thermal AdS/CFT ,” JHEP, vol. 03, p. 011, 2008, 0711.0133.
[8] B. Eynard, “All orders asymptotic expansion of large partitions,” J. Stat. Mech. , vol. 0807, p. P07023, 2008,
0804.0381.
[9] V . Ivanov and G. Olshanski, “Kerov’s central limit theorem for the Plancherel measure on Young diagrams,”
arXiv Mathematics e-prints, p. math/0304010, Apr 2003, math/0304010.
[10] A. Chattopadhyay, D. Suvankar, and Neetu, “Chern-Simons Theory on Seifert Manifold and Matrix Model,”
Phys. Rev. D, vol. 100, no. 12, p. 126009, 2019, 1902.07538.
[11] J. Jurkiewicz and K. Zalewski, “Phase structure of U(N→∞ ) gauge theory on a two-dimensional lattice for a
broad class of variant actions,”Nuclear Physics B, vol. 220, no. 2, pp. 167 – 184, 1983.
[12] G. Mandal, “Phase Structure of Unitary Matrix Models,” Mod. Phys. Lett., vol. A5, pp. 1147–1158, 1990.
[13] D. J. Gross and E. Witten, “Possible Third Order Phase Transition in the Large N Lattice Gauge Theory,” Phys.
Rev., vol. D21, pp. 446–453, 1980.
[14] S. R. Wadia, “ N =∞ Phase Transition in a Class of Exactly Soluble Model Lattice Gauge Theories,”Phys. Lett.,
vol. 93B, pp. 403–410, 1980.
[15] E. Brezin, C. Itzykson, G. Parisi, and J. B. Zuber, “Planar Diagrams,” Commun. Math. Phys. , vol. 59, p. 35,
1978.
[16] M. R. Douglas, “Conformal ﬁeld theory techniques in large N Yang-Mills theory,” inNATO Advanced Research
Workshop on New Developments in String Theory, Conformal Models and Topological Field Theory Cargese,
France, May 12-21, 1993, 1993, hep-th/9311130.
[17] P. Dutta and S. Dutta, “Phase Space Distribution for Two-Gap Solution in Unitary Matrix Model,”JHEP, vol. 04,
p. 104, 2016, 1510.03444.
[18] A. Chattopadhyay, P. Dutta, and S. Dutta, “Emergent Phase Space Description of Unitary Matrix Model,”JHEP,
vol. 11, p. 186, 2017, 1708.03298.
[19] P. Dutta and S. Dutta, “Phase Space Distribution of Riemann Zeros,” J. Math. Phys. , vol. 58, no. 5, p. 053504,
2017, 1610.07743.
[20] L. H. Thomas, “The calculation of atomic ﬁelds,” Mathematical Proceedings of the Cambridge Philosophical
Society, vol. 23, no. 5, p. 542–548, 1927.
[21] E. Fermi, “Un metodo statistico per la determinazione di alcune priorieta dell’atome,”Rend. Accad. Naz. Lincei,
vol. 6, no. 602-607, p. 32, 1927.
[22] A. Chattopadhyay, S. Dutta, D. Mukherjee, and Neetu, “From 2d Droplets to 2d Yang-Mills,” 10 2020,
2010.11923.
[23] A. Jevicki and B. Sakita, “Collective ﬁeld approach to the large- N limit: Euclidean ﬁeld theories,” Nuclear
Physics B, vol. 185, no. 1, pp. 89 – 100, 1981.
[24] M. Hamermesh, Group Theory and its Application to Physical Problems . Dover Publication, 1989.
[25] W. Fulton and J. Harris, Representation Theory: A First Course. Graduate texts in mathematics, Springer, 1991.
[26] S. Kerov, “Gaussian limit for the plancherel measure of the symmetric group.,” Comptes Rend. Acad. Sci. Paris,
vol. S´erie I, t.316, pp. 303–308, 1993.
[27] K. Johansson, “On ﬂuctuations of eigenvalues of random hermitian matrices,” Duke Math. J., vol. 91, pp. 151–
32
204, 01 1998.
[28] P. ´Sniady, “Gaussian ﬂuctuations of characters of symmetric groups and of Young diagrams,”arXiv Mathematics
e-prints, p. math/0501112, Jan 2005, math/0501112.
[29] L. V . Bogachev and Z. G. Su, “Central limit theorem for random partitions under the Plancherel measure,”arXiv
Mathematics e-prints, p. math/0607635, Jul 2006, math/0607635.
[30] L. V . Bogachev and Z. Su, “Gaussian ﬂuctuations of young diagrams under the plancherel measure,” Proc. R.
Soc. A, vol. 463.
[31] M. Dolega and V . F´eray, “Gaussian ﬂuctuations of young diagrams and structure constants of jack characters,”
arXiv e-prints, Feb 2014, 1402.4615.
[32] L. Erd ˝os and D. Schr ¨oder, “Fluctuations of Rectangular Young Diagrams of Interlacing Wigner Eigenvalues,”
Aug 2016, 1608.05163.
[33] M. Dolega and P. ´Sniady, “Gaussian ﬂuctuations of Jack-deformed random Young diagrams,” arXiv e-prints ,
p. arXiv:1704.02352, Apr 2017, 1704.02352.
[34] J. A. Mingo and R. Speicher, “Second Order Freeness and Fluctuations of Random Matrices: I. Gaussian and
Wishart matrices and Cyclic Fock spaces,”arXiv Mathematics e-prints, May 2004.
[35] J. A. Mingo, P. ´Sniady, and R. Speicher, “Second Order Freeness and Fluctuations of Random Matrices: II.
Unitary Random Matrices,” arXiv Mathematics e-prints, p. math/0405258, May 2004, math/0405258.
[36] B. Collins, J. A. Mingo, P. ´Sniady, and R. Speicher, “Second Order Freeness and Fluctuations of Random
Matrices, III. Higher order freeness and free cumulants,” arXiv Mathematics e-prints , p. math /0606431, Jun
2006, math/0606431.
[37] A. Borodin, A. Okounkov, and G. Olshanski, “Asymptotics of Plancherel measures for symmetric groups,”
arXiv Mathematics e-prints, p. math/9905032, May 1999, math/9905032.
[38] K. Johansson, “Discrete orthogonal polynomial ensembles and the Plancherel measure,” arXiv Mathematics
e-prints, p. math/9906120, Jun 1999, math/9906120.
[39] K. Johansson, “A multi-dimensional Markov chain and the Meixner ensemble,” Arkiv for Matematik , vol. 48,
pp. 79–95, Apr 2010, 0707.0098.
[40] O. Aharony, J. Marsano, S. Minwalla, K. Papadodimas, and M. Van Raamsdonk, “The Hagedorn - deconﬁne-
ment phase transition in weakly coupled large N gauge theories,” Adv. Theor . Math. Phys., vol. 8, pp. 603–696,
2004, hep-th/0310285. [,161(2003)].
[41] L. Alvarez-Gaume, C. Gomez, H. Liu, and S. Wadia, “Finite temperature eﬀective action, AdS 5 black holes, and
1/N expansion,” Phys. Rev., vol. D71, p. 124023, 2005, hep-th/0502227.
[42] M. Marino, “Chern-Simons theory, matrix models, and topological strings,” Int. Ser . Monogr . Phys., vol. 131,
pp. 1–197, 2005.
[43] B. Eynard, T. Kimura, and S. Ribault, “Random matrices,” 2015, 1510.04430.
[44] B. Eynard, Counting Surfaces: CRM Aisenstadt Chair lectures . Progress in Mathematical Physics 70,
Birkhauser Basel, 2016.
[45] L. Maoz and V . S. Rychkov, “Geometry quantization from supergravity: The Case of ‘Bubbling AdS’,”JHEP,
vol. 08, p. 096, 2005, hep-th/0508059.
[46] J. Avan and A. Jevicki, “Classical integrability and higher symmetries of collective string ﬁeld theory,” Phys.
Lett. B, vol. 266, pp. 35–41, 1991.
[47] J. Avan and A. Jevicki, “Quantum integrability and exact eigenstates of the collective string ﬁeld theory,” Phys.
Lett. B, vol. 272, pp. 17–24, 1991.
[48] A. Jevicki, “Development in 2-d string theory,” in Workshop on String Theory, Gauge Theory and Quantum
Gravity, pp. 96–140, 9 1993, hep-th/9309115.
[49] L. Grant, L. Maoz, J. Marsano, K. Papadodimas, and V . S. Rychkov, “Minisuperspace quantization of ‘Bubbling
AdS’ and free fermion droplets,”JHEP, vol. 08, p. 025, 2005, hep-th/0505079.
[50] R. Dijkgraaf, “Integrable hierarchies and quantum gravity,” Lect. Notes Phys., pp. 67–89, 1993.
[51] G. Segal and G. Wilson, “Loop groups and equations of KdV type,”Inst. Hautes Etudes Sci. Publ. Math., vol. 61,
no. 1, pp. 5–65, 1985.
[52] E. Date, M. Jimbo, M. Kashiwara, and T. Miwa, “Transformation groups for soliton equations. 3. Operator
approach to the Kadomtsev-Petviashvili equation,”J. Phys. Soc. Jap., vol. 50, pp. 3806–3812, 1981.
33
[53] B. Eynard, “A Matrix model for plane partitions and (T)ASEP,” J. Stat. Mech. , vol. 0910, p. P10011, 2009,
0905.0535.
[54] X.-G. Wen, “Topological orders and edge excitations in FQH states,” Adv. Phys., vol. 44, no. 5, pp. 405–473,
1995, cond-mat/9506066.
34
