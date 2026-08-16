---
doc_id: aif-2009-59-1-347-0
doc_title: "L’INSTITUT FOURIER"
section_id: sec-007-24-proof-of-theorem-26
section_title: "Proof of Theorem 2.6"
section_number: 2.4
pages: 19-22
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
doc_brief: "ANNALESDEL’INSTITUTFOURIER ANNALES L’INSTITUT FOURIER — 18 sections: Introduction; Part 1. Convergent q-Borel and q-L; Convergent q-Euler series"
---
We know that our germs φ(q,ξ ), q ∈ (η, 1], of analytic functions at 0
admit an analytic continuation along d. Moreover, for q <1, the functions
φ(q,ξ ) are actually meromorphic over C, which means that they are linear
combination of a basis of solutions of Nqy = 0 at ∞. The main point of the
proof is the careful choice of such a basis, which will allow us to prove that
φ(q,x ) converges uniformly to φ(1,ξ ) on an inﬁnite sector containing the
direction d. Of course this ends the proof since Equations ( 2.1) and ( 2.2)
imply that for any x ∈V we have:
(2.3)
lim
q→1
y(q,x ) = lim
q→1
∫ x
1−q
0
( (1 −q)qξ
x ;q
)
∞
φ(q,ξ )dqξ
=
∫ ∞ei arg(x)
0
lim
q→1
(
eq
(qξ
x
)−1
φ(q,ξ )
)
dξ
=
∫ ∞ei arg(x)
0
φ(1,ξ )e− ξ
xdξ.
The theorem results of the combination of two lemmas. First of all let
us prove the uniform convergence around zero:
Lemma 2.12. — The familyφ(q,ξ ) converges uniformly toφ(1,x ), when
q → 1, on a closed disk centered at 0.
Proof. — Let us write φ(q,ξ ) = ∑
n/greaterorequalslant0φn(q)xn for any q ∈ (η, 1]. Then
there exists N > 0 such that for any n > Nthe coeﬃcients φn(q) verify
a well deﬁned recursive relation whose coeﬃcients do not degenerate (5) . A
direct estimates of the recursive relation allows to conclude that |φn(q)| ⩽
C n for a convenient real constant C, any n > Nand any q ∈ (η, 1]. This
estimate, together with the fact that φn(q) is a continuous function of q,
implies the uniform convergence on a convenient closed disk centered at 0
(cf. for instance the estimates in [ 17, Lemma 1.2.6]). □
The last assumption in 2.7 implies that φ(q,x ) is a linear combination,
whose coeﬃcients are entries of the matrix C(q), of the canonical solutions
at ∞, constructed in [ 16, §1], using a q-analog of the Frobenius method.
As noticed in [ 16, §3], the uniform part of the canonical solution at ∞
converges uniformly on any compact of P1
C /integerdivide{0} where it is analytic, to
the uniform part of the solutions of N1y = 0 constructed with the classi-
cal Frobenius methods, once that the gauge transformation C(1) has been
(5) Notice that we have not assumed that 0 is a regular singular point with non resonant
exponents at 0.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 365
applied to the companion matrix. Since the entries of C(q) converge to the
entries ofC(1) by assumption, to obtain the uniform convergence in a neigh-
borhood of ∞ it is enough to control the convergence of the so called log-car
matrix(6) . Let ζ = 1/ξ. The uniform convergence of (1 −q)ζθ ′(q,ζ )/θ(q,ζ )
over the inﬁnite sector {| arg(ζ)| < π −ε} to logζ is already proved in
Lemma 1.6. We need an analogous result for θ(q,ζ )/θ(q,cx ) which is solu-
tion of the q-diﬀerence equation y(qζ ) = cy(ζ), c ∈ C∗. We give a proof of
the needed estimate, although it is a classical result:
Lemma 2.13. — Let c(q) ∈ C∗ be a function of q ∈ (0, 1) such that
limq→1
log c
ln q =γ,ϵ ∈ (0,π ) and consider the sector Vϵ := {ζ ∈ C∗ : | argζ| ⩽
π −ϵ}. As q → 1−, the following uniform estimate holds uniformly over Vϵ:
θ(q,ζ )
θ(q,cζ ) =ζ γ(1 +o(1 −q)).
Proof. — Let us consider again the modular equation ( 1.10) :
θ(q, √q) =
√
2π
ln(1/q)e− log2 x
2 ln q θ(q∗, √q∗x∗),
where
x∗ =e− 2πi
ln q log x, q ∗ =e
4π2
ln q.
We observe that (ζ/√q)∗ = −ζ ∗ and (cζ/√q)∗ = −c∗ζ ∗. Therefore we
obtain:
θ(q,ζ )
θ(q,cζ ) =e
log c
ln q (log( ζ√q )+ log c
2 ) θ(q∗, −√q∗ζ ∗)
θ(q∗, −√q∗c∗ζ ∗).
As in the proof of Lemma 1.6, we observe that for any ζ ∈ Vϵ, ζ ∗ ∈ V ∗
ϵ ;
see ( 1.12) for more details. Moreover, when X and Y denote two complex
numbers such that |X|, |Y | ∈ (q∗, 1), we have the estimate:
⏐⏐⏐⏐
θ(q∗,X )
θ(q∗,Y )
⏐⏐⏐⏐ ⩽
(−|X|;q∗)∞(− q∗
|X| ;q∗)∞
(|Y |;q∗)∞( q∗
|Y | ;q∗)∞
= θ(q∗, |X|)
θ(q∗, −|Y |).
An elementary calculation using ( 1.12) allows to conclude, since q∗ → 0+
and c∗ →e−2πiγ . □
(6) The terminology comes from the juxtaposition of the terms “logarithm” and “charac-
ter”, meaning the solution matrix of a constant coeﬃcient diﬀerential (resp. q-diﬀerence)
system is obtained by a combinatoric procedure from the logarithm (resp. q-logarithm)
and a family of characters (resp. q-characters). A solution in a regular singular point,
whose exponents are non resonant, is given by the product of an analytic matrix, called
uniform part, by the “log-car” matrix.
We are choosing here as a q-logarithm the logarithmic derivative of the Jacobi θ
function and as q-characters convenient quotient of the θ functions. For more details in
the q-diﬀerence setting cf. [16].
TOME 59 (2009), F ASCICULE 1
366 Lucia DI VIZIO & Changgui ZHANG
Resuming, the function φ(q,ξ ) is a linear combination, with coeﬃcients
that are continuous functions of q, of a canonical basis of solutions at ∞:
we have proved that both the canonical solutions and the coeﬃcients of the
linear combination admit a uniform limit in a bounded sector containing d,
centered at ∞ and of arbitrary radius R> 0. Combined with Lemma 2.12,
this means that φ(q,x ) converges uniformly to φ(1,x ) in a neighborhood
of the direction d, which allows to conclude the proof.
Appendix A. Jackson’s integral
Definition A.1. — We set
F (x) =
∫ x
0
f (t)dqt = (1 −q)x
∑
n/greaterorequalslant0
f (qnx)qn,
whenever the right hand side converges.
Remark A.2. —
1. Notice that if F (x) is well-deﬁned then dqF (x) = f (x).
2. Iff (x) is continuous on the closed disk D(0,r +), thenF (x) is well deﬁned
for any x ∈ D(0,r +). In fact there exists M > 0 such that |f (qnx)qn| ⩽
M |q|n, which guarantees the convergence of the inﬁnite sum.
Proposition A.3. —
1. If f (x) is an analytic function over the disk D(0,r −), then F (x) is also
analytic over D(0,r −).
2. If F (x) is analytic over the disk D(0,r −) and if G(x) is another analytic
function over D(0,r −) such that dqG(x) = f (x), then
∫ x
0
f (t)dqt =G(x) −G(0).
Proof. —
1. It follows from the fact that F (x) is a uniformly convergent series of
analytic function over D(0,r −ε+), for any r>ε> 0.
2. It follows immediately from the remark that the subﬁeld of constants
of the ring of analytic function over D(0,r −) with respect to the operator
f (x) ↦→f (qx) is C. In fact this implies that F (x) −G(x) ∈ C.
□
Definition A.4. — Let us ﬁx a q-orbit qZα ⊂ C and suppose that for
anyx ∈qZα the integral F (x) =
∫ x
0 f (t)dqt is well-deﬁned. Then we set
∫
qZ α
f (t)dqt = lim
|x|→∞
x∈qZα
∫ x
0
f (t)dqt.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE 367
Remark A.5. — A straightforward calculation shows that∫
qZ α
f (t)dqt = (1 −q)α
∑
n∈Z
f (qnα)qn
and in particular that
∫
qZα
f (t)dqt
t = (1 −q)
+∞∑
n=−∞
f (qnα),
whenever the right side converges.
