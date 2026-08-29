---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-009-36-random-walks-changed-in-measure
section_title: "Random walks changed in measure"
section_number: 3.6
pages: 20-24
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
cursion in the higher dimensions. Since we do not want to enter details on mod-
Gaussian convergence for random vectors (for which we refer the reader to [KN12]
and [FMN13]), we shall only consider the simple case X = ( X(1), . . . ,X(d)) is a ran-
dom vector with values in Rd such that E[exp(z1X(1) +··· + zdX(d))] is entire in Cd.
We shall say that the sequence(Xn) of random vectors converges in the complex mod-
Gaussian sense with parameter tn and limiting function ψ(z1,··· , zd) if the following
convergence holds locally uniformly on compact subsets of Cd:
ψn(t) = E[exp(z1X(1)
n +··· + zdX(d)
n )] exp
(
−tn
(z1)2 +··· + (zd)2
2
)
→ ψ(z1, . . . ,zd).
In this vector setting, the assumptions (A) and (B) of Section 3 now simply amount to
the fact that the convergence above holds locally uniformly fort = (t(1),··· , t(d))∈ Rd
and that ψn and ψ are both in L1(Rd).
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS21
Following the case d = 1 we denote Pn the law of Xn on Rd,
Qn[dx] = e
‖x‖2
2tn
E
[
e
‖Xn‖2
2tn
] Pn[dx],
and Yn a random variable under the new law Qn. Note that here again hypothesis
(B) implies that Zn = E[e‖Xn‖2/2tn] is ﬁnite for all n∈ N. Indeed, with the notation
⟨u, v⟩ = u1v1 +··· + udvd, we have
∫
Rd
ψn(t) dt = E
[∫
Rd
e⟨t,Xn⟩− tn‖t‖2
2 dt
]
= E
[
e
(‖Xn‖2
2tn
(∫
Rd
e−‖Xn−tnt‖2
2tn dt
)]
=
(2π
tn
)d/2
E
[
e
‖Xn‖2
2tn
]
.
Therefore, the new probabilities Qn are well-deﬁned and
Zn = E[e‖Xn‖2/2tn] =
( tn
2π
)d/2∫
Rd
ψn(t) dt.
Then it is clear that Proposition 5 holds with Gn being a Gaussian vector with covari-
ance matrix 1/tn Id where Id is the identity matrix of size d. Similarly one can establish
an analogue of Theorem 6 in Rd.
Let Wn be a simple random walk on the lattice Zd≥2: at each step, each of the 2 d
neighbors of the state that is occupied has the same probability of transition (2d)−1.
The d-dimensional characteristic function of Wn = (W(1)
n , . . . ,W(d)
n ) is
E[ez1W(1)
n +···+zdW(d)
n ] =
(cosh z1 +··· + cosh zd
d
)n
.
Therefore, one has the asymptotics
log E
[
e
z1W(1)
n +···+zdW(d)
n
n1/4
]
= n log
(
1 + (z1)2 +··· + (zd)2
2dn1/2 + (z1)4 +··· + (zd)4
24dn + o
( 1
n
))
= n1/2 (z1)2 +··· + (zd)2
2d − 3((z1)2 +··· + (zd)2)2− d((z1)4 +··· + (zd)4)
24d2 + o(1).
One obtains a d-dimensional complex mod-Gaussian convergence of Xn = n−1/4 Wn
with parameters n1/2
d and limiting function
ψ(z1, . . . ,zd) = exp
(
−3 ((z1)2 +··· + (zd)2)2− d ((z1)4 +··· + (zd)4)
24d2
)
.
In [FMN13], we used this mod-convergence to prove quantitative estimates regarding
the breaking of the radial symmetry when one considers random walks conditioned to
be of large size (of order n3/4 instead of the expected order n1/2). With the notion of
L1-mod-Gaussian convergence, one can give another interpretation, but only for d = 2
22 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
or d = 3. Restricted to Rd, the limiting function is indeed not integrable for d≥ 4: if
t2, . . . ,td∈ [−1, 1], then
3 ((t1)2 +··· + (td)2)2− d ((t1)4 +··· + (td)4)≤ 3 ((t1)2 + (d− 1))2− d (t1)4
≤ (3− d)(t1)4 + 6(d− 1)(t1)2 + 3(d− 1)2.
So, restricted to the domain R× [−1, 1]d−1, ψ(t1, . . . ,td)≤ K exp(a(t1)4− b(t1)2) for
some positive constants a, b and K; therefore, this function is not integrable.
On the other hand, if d = 2 or d = 3, then ψ is integrable on Rd, and one has L 1-
mod-Gaussian convergence. Indeed, when d = 2, the limiting function is
ψ(t1, t2) = exp
(
− (t1)4 + (t2)4 + 6(t1t2)2
96
)
, (10)
which is clearly integrable; and the residues
ψn(t1, t2) = E
[
e
t1W(1)
n +t2W(2)
n
n1/4
]
e− n1/2 ((t1)2+(t2)2)
4
converge locally uniformly on R2 to ψ(t1, t2), but also in L1(R2). Indeed,
∫
R2
ψn(t1, t2) dt1 dt2 =
∫
R2
(
cosh t1
n1/4 + cosh t2
n1/4
2
)n
e− n1/2 ((t1)2+(t2)2)
4 dt1 dt2
= n1/2
∫
R2
(cosh u1 + cosh u2
2 e− (u1)2+(u2)2
4
)n
du1 du2,
and the function (u1, u2)↦→ cosh u1+cosh u2
2 e− (u1)2+(u2)2
4 reaches its unique global maxi-
mum at u1 = u2 = 0, with Taylor expansion
1− (u1)4 + (u2)4 + 6(u1u2)2
96 + o(‖u‖4)
around this point (see Figure 4).
Thus, by using the multi-dimensional Laplace method, one sees that the limit of the
integral
∫
R2 ψn(t1, t2) dt1 dt2 is
∫
R2 ψ(t1, t2) dt1 dt2, and the L 1 convergence is shown.
Similarly, when d = 3, the limiting function is
ψ(t1, t2, t3) = exp
(
− (t1t2)2 + (t1t3)2 + (t2t3)2
36
)
, (11)
and the following computation shows that it is integrable:
∫
R3
ψ(x, y, z) dx dy dz =
∫
R2
e− (yz)2
36
(∫
R
e− y2+z2
36 x2
dx
)
dy dz
= 6
√
π
∫
R2
e− (yz)2
36
√
y2 + z2 dy dz
= 3
√
π
∫ ∞
r=0
∫ π
θ=0
e− r4 sin2 θ
144 dr dθ
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS23
FIGURE 4. The function f (u1, u2) = cosh u1+cosh u2
2 e− (u1)2+(u2)2
4 .
= 12
√
3π
∫ ∞
r=0
e−r4
dr
∫ π
2
θ=0
dθ√
sin θ
< +∞
since 1√
sin θ is integrable at 0. On the other hand, the residues
ψn(t1, t2, t3) = E
[
e
t1W(1)
n +t2W(2)
n +t3W(3)
n
n1/4
]
e− n1/2 ((t1)2+(t2)2+(t3)2)
6
converge to ψ(t1, t2, t3) locally uniformly on R3 and in L1(R3). Indeed, one has again
∫
R3
ψn(t1, t2, t3) dt = n1/2
∫
R3
(cosh u1 + cosh u2 + cosh u3
3 e− (u1)2+(u2)2+(u3)2
6
)n
du
and the function in the brackets reaches its unique maximum at u1 = u2 = u3 = 0,
with Taylor expansion corresponding to the limiting functionψ after application of the
Laplace method.
The multidimensional analogue of Theorem 6 thus yields the following multidimen-
sional extension of the limit theorem for the Curie-Weiss model:
Theorem 11. Let Wn be a simple random walk in dimension d≤ 3. If Vn is obtained from Wn
by a change of measure by the factor exp(d‖Wn‖2/2n), then
Vn
n3/4 ⇀n→∞
ψ(x) dx∫
R3 ψ(x) dx ,
where ψ(x) = exp(−x4/12) in dimension 1, and ψ is given by Formulas (10) and (11) in
dimension 2 and 3.
Remark. Suppose d = 2. Then, there is a limit in law not only for Vn
n3/4 , but in fact for
the whole random walk ( Vk
n3/4 )k≤n, viewed as a random element ofC(R+, R2) or of the
Skorohod spaceD(R+, R2), see Figure 5.
24 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
22
FIGURE 5. A 2-dimensional random walk changed in measure by
e‖Wn‖2/n, here with n = 10000.
4. L OCAL LIMIT THEOREM AND RATE OF CONVERGENCE IN THE ELLIS -NEWMAN
LIMIT THEOREM
We keep the same notation as before and noteIn =∫
R ψn(x) dx and I∞ =∫
R ψ(x) dx.
In this section we wish to provide a quick approach based on Fourier analysis,
(1) to compute the Kolmogorov distance between the rescaled magnetization
Yn/n1/2 = Mn/n3/4
in the Curie-Weiss model and the random variable W∞ with density ψ(x)/I∞,
where ψ(x) = exp(−x4/12). This problem was recently solved in [EL10] using
Stein’s method. As in [EL10], our method would cover many more general
models as well: it is just a matter of specializing Lemma 12 and Lemma 13
below which are stated in all generality.
(2) to prove a new local limit theorem for the rescaled magnetization n−1/4Mn in
the Curie-Weiss model. Here again we shall indicate how one can establish local
limit theorems in more general situations.
