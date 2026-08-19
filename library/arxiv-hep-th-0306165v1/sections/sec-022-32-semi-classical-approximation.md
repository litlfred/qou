---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-022-32-semi-classical-approximation
section_title: "Semi-Classical Approximation"
section_number: 3.2
pages: 25-30
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
Following the general prescription formulated in the end of the previous subsection,
here we study the semi-classical behavior of the partition f unctionZ(M ) by quantizing the
Hamiltonian system associated with ( P,ω ) and a Lagrangian submanifold L. As in the
standard classical mechanics, we introduce a canonical 1-f orm (also known as a Liouville
form), which in the canonical variables ( pi,q j) can be written as
θ =
∑
i
pidqi (3.16)
We note that this 1-form may not be globally deﬁned; this happ ens, for example, when the
phase space is compact. However, locally we can always write ω =dθ, and because ω|L = 0
holds by the deﬁnition of the Lagrangian submanifold L, we ﬁnd that the restriction of
the canonical 1-form to L is closed,
dθ|L = 0 (3 .17)
The cohomology class in H 1(L, I R) induced by the 1-form θ is called the Liouville class of
the Lagrangian immersion֒P . Lagrangian immersions for which the Liouville class is
trivial are called exact Lagrangian immersions.
Consistent quantization of ( P,ω ) with a Lagrangian submanifold L requires the Li-
ouville class of L to obey certain conditions. In order to explain these condit ions, let us
proceed with the WKB quantization and deﬁne a phase function S, usually called the
action integral, such that
dS =θ|L (3.18)
Then, the semi-classical approximation to the wave functio n supported on the Lagrangian
submanifold L is given by
Z≃
∑
α
ψ·eiS/ ¯heiπη/ 4 +O(¯h) (3 .19)
24
where the sum is over a discrete, ﬁnite set of the components o fL,η is the famous Maslov
correction to the phase of the semi-classical wave function , and the amplitude ψ is a half-
density on L, which obeys the transport equation [62,63]:
Lψ = 0 (3 .20)
In order to understand the meaning of each term in (3.19), it i s instructive to consider
a ﬁnite dimensional integral
Z =
∫ ∏
i
dqi eiS(qi)/ ¯h (3.21)
In the stationary phase approximation, this integral is dom inated by the contribution from
the critical points,
Z≃
∑
α
eiS/ ¯h
√
det
(
−i· Hess(S)
) +O(¯h) (3 .22)
where Hess(S) stands for the Hessian of the phase function S. Here, a phase of the square
root of the determinant requires extra care. Namely, if S is a real function, Hess( S)
has only real eigenvalues, λi. Each positive eigenvalue contributes ( −i)−1/ 2 =eiπ/ 4 to the
phase of the above expression, whereas each negative eigenv alue contributesi−1/ 2 =e−iπ/ 4.
Therefore, a reﬁned version of the formula (3.22) looks like :
Z≃
∑
α
eiS/ ¯heiπη/ 4| det
(
Hess(S)
)
|−1/ 2 +O(¯h) (3 .23)
where the η-invariant
η =
∑
i
sign λi (3.24)
is deﬁned as the (regularized) signature of the Hessian, Hes s(S), that is the total number of
positive eigenvalues of Hess(S) minus the total number of negative eigenvalues of Hess( S).
Now, let us return to the semi-classical wave function (3.19 ) associated with a La-
grangian submanifold L. Notice, that when the restriction of θ to L is an exact 1-form,
the phase function S =
∫
θ is well deﬁned. However, if the Lioville class of θ is non-trivial,
the phase function S depends on the choice of the integration path in L. In particular, a
diﬀerence between two such choices will change the action in tegral by a period of θ,
∆ S =
∮
C
θ,
25
where C is a closed 1-cycle on L. In order for the semi-classical expression (3.19) to be
unambiguously deﬁned, all the periods of θ must be integer multiples of 2 π¯h, for some
value of ¯h:
1
2π¯h
∮
C
θ∈ Z Z , ∀ C∈π1(L) (3 .25)
A Lagrangian submanifolds֒P which obeys this condition is called quantizable, and
the corresponding values of ¯ h for which (3.25) holds are called admissible for L. Notice,
that the set of quantizable Lagrangian submanifolds with la rge ﬁrst Betti number is usually
rather limited.
dq p
*
(l,m)
L
Fig. 7: The moduli space of the SL(2,C) Chern-Simons theory on a knot com-
plement is described by the A-polynomial of the knot. The act ion integral of the
corresponding quantum mechanics can be obtained by integra ting θ =
∑
i pidqi
over a path on the curve A(l, m) = 0.
Now, let us apply this to our problem. We set ¯ h = 1; the role of the Planck constant
is played by k−1 and σ−1, so that the semi-classical limit corresponds to k,σ → ∞.
Furthermore, from the deﬁning equations (3.7) and (3.16) we obtain a canonical 1-form,
θ = k
πθk +iσ
πθσ (3.26)
where θk and θσ are real 1-forms,
θk = Re(v)dRe(u) + Im(u)dIm(v) (3 .27)
and
θσ =−Re(u)dIm(v) + Re(v)dIm(u) (3 .28)
26
Since the 1-form θ is complex-valued, the condition for L to be quantizable implies
two independent sets of constraints corresponding, respec tively, to the imaginary and real
parts of the Bohr-Sommerfeld condition (3.25):
L quantizable :
∮
C
θσ = 0
1
π2
∮
C
θk∈ Q
(3.29)
Provided that these two conditions are satisﬁed for any 1-cy cle C⊂ L, the system can
be consistently quantized and one can write the semi-classi cal expression for the partition
function in the form (3.19). The ﬁrst condition in (3.29) ass erts that all the periods of θσ
must vanish. Equivalently, θσ should be an exact 1-form, when restricted to L.
It turns out that, for a Lagrangian submanifold L deﬁned as a zero locus of the A-
polynomial, the restriction of θσ to L is always an exact 1-form. Speciﬁcally, using a
classical formula of Schl¨ aﬂi concerning the volume of inﬁn itesimally deformed polyhedra,
one can show that
θσ|L = 1
2dVol(M ) (3 .30)
where Vol(M ) is the volume of the hyperbolic 3-manifold M , which in the present dis-
cussion is a complement of a knot K. This important result is due to Hodgson [64] with
improvements by Dunﬁeld [65]. Similarly, the real part of th e 1-form θ is related to the
Chern-Simons invariant of the 3-manifold M ,
θk|L =−π2dCS (M ) (3 .31)
This formula was originally conjectured by Neumann and Zagi er [52], and later proved by
Yoshida [55], see also [66,56].
From the equations (3.30) and (3.31) it follows that imagina ry and real components
of the action integral S are related, respectively, to the volume and the Chern-Simo ns
invariant of the knot complement M :
S = iσ
2π Vol(M )−πkCS (M ) (3 .32)
This is indeed the expected semi-classical behavior of the SL(2,C) Chern-Simons action
(1.7). We can also write it as
dS =tdF +tdF (3.33)
27
where
dF = 1
4π
(
vdu−udv +d(uv)
)
Combining the formulas (3.19) and (3.32) together, we obtai n:
Z(M )≃
∑
α
ψ·eiπη/ 4· exp
(
− σ
2π Vol(M )−iπkCS (M )
)
+... (3.34)
This is the usual expression for the semi-classical wave fun ction in a quantum mechanics
with the action integral (3.32). Let us now compare this resu lt with a general form of the
(unnormalized) semi-classical partition function in a Che rn-Simons theory [3]:
Z(M )≃
∑
α
det(∆)√
| det(L−)|
eiπη (A(α ))/ 4·eiI(A(α ) ) +... (3.35)
where ∆ is the standard Laplacian and L− denotes a restriction of the self-adjoint operator
L =∗D+D∗ to the space of odd forms on M (not to be confused with the character variety
L). For a Chern-Simons theory with complex gauge group one fur ther has [1,67]:
η(A(α )) = 0 (3 .36)
It is clear that our result (3.34) is very similar to (3.35). I n fact, one can easily see the
terms in both expression which have the same origin and, ther efore, should be identiﬁed.
For example, each critical point in the quantum mechanics pr oblem corresponds to a ﬂat
SL(2,C) connection, A(α ), in the Chern-Simons theory. Among these ﬂat connections,
there is a geometric one, associated with the hyperbolic str ucture on the knot complement
M . The Chern-Simons action, I(A(hyperb)), of this ﬂat connection is given by (3.32), and
it was already discussed in this section. Moreover, η(A(α )) should be identiﬁed with the
Maslov correction to the phase of the semi-classical expres sion (3.34), and (3.36) implies
that this correction vanishes. This should also follow dire ctly from the properties of the
A-polynomial. Finally, the absolute value of the ratio of th e determinants in (3.35), which
is often called the Reidemeister-Ray-Singer torsion, T (A(α )),
√
T (A(α )) = det(∆)√
| det(L−)|
(3.37)
is related to the amplitude, ψ, of the quantum wave function (3.34).
Notice that, besides the critical point corresponding to th e hyperbolic SL(2,C) con-
nection, the sum (3.34) also contains terms corresponding t o other ﬂat connections. Even
28
though the Chern-Simons action, I(A(α )), of these ﬂat connections is given by (3.32),
where the “volume” and the “Chern-Simons invariant” can be c omputed by integrating
the 1-forms (3.27) and (3.28) over diﬀerent branches of the z ero locus of the A-polynomial,
they no longer have a nice geometric interpretation. For exa mple, there are ﬂat connections
with negative “volume”. In particular, if K is a hyperbolic knot, then the semi-classical
behavior of the partition function (3.35) is dominated by th e ﬂat connection whose volume
is equal to minus the hyperbolic volume of M ,
Z(M )≃
√
T (A(hyperb)) exp
( σ
2π Vol(M ) +iπkCS (M )
)
+... (3.38)
