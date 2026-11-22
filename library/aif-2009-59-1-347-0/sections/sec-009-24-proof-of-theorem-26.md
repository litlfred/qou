---
doc_id: aif-2009-59-1-347-0
doc_title: "On q-summation and confluence"
section_id: sec-009-24-proof-of-theorem-26
section_title: "Proof of Theorem 2.6"
section_number: 2.4
pages: 19-21
source_pdf: AIF_2009__59_1_347_0.pdf
source_sha256: 35b8422990e24888
toc_source: outline
doc_brief: "On q-summation and confluence — 28 sections: Front matter; Introduction; Part 1. Convergent q-Borel and q-L"
---
We know that our germs φ(q, ξ), q ∈(η, 1], of analytic functions at 0
admit an analytic continuation along d. Moreover, for q < 1, the functions
φ(q, ξ) are actually meromorphic over C, which means that they are linear
combination of a basis of solutions of Nqy = 0 at ∞. The main point of the
proof is the careful choice of such a basis, which will allow us to prove that
φ(q, x) converges uniformly to φ(1, ξ) on an inﬁnite sector containing the
direction d. Of course this ends the proof since Equations (2.1) and (2.2)
imply that for any x ∈V we have:
(2.3)
lim
q→1 y(q, x) = lim
q→1
Z
x
1−q
0
(1 −q)qξ
x
; q

∞
φ(q, ξ)dqξ
=
Z ∞ei arg(x)
0
lim
q→1
 
eq
qξ
x
−1
φ(q, ξ)
!
dξ
=
Z ∞ei arg(x)
0
φ(1, ξ)e−ξ
x dξ.
The theorem results of the combination of two lemmas. First of all let
us prove the uniform convergence around zero:
Lemma 2.12. — The family φ(q, ξ) converges uniformly to φ(1, x), when
q →1, on a closed disk centered at 0.
Proof. — Let us write φ(q, ξ) = P
n⩾0 φn(q)xn for any q ∈(η, 1]. Then
there exists N > 0 such that for any n > N the coeﬃcients φn(q) verify
a well deﬁned recursive relation whose coeﬃcients do not degenerate(5). A
direct estimates of the recursive relation allows to conclude that |φn(q)| ⩽
Cn for a convenient real constant C, any n > N and any q ∈(η, 1]. This
estimate, together with the fact that φn(q) is a continuous function of q,
implies the uniform convergence on a convenient closed disk centered at 0
(cf. for instance the estimates in [17, Lemma 1.2.6]).
□
The last assumption in 2.7 implies that φ(q, x) is a linear combination,
whose coeﬃcients are entries of the matrix C(q), of the canonical solutions
at ∞, constructed in [16, §1], using a q-analog of the Frobenius method.
As noticed in [16, §3], the uniform part of the canonical solution at ∞
converges uniformly on any compact of P1
C ∖{0} where it is analytic, to
the uniform part of the solutions of N1y = 0 constructed with the classi-
cal Frobenius methods, once that the gauge transformation C(1) has been
(5)Notice that we have not assumed that 0 is a regular singular point with non resonant
exponents at 0.
ANNALES DE L’INSTITUT FOURIER
ON q-SUMMATION AND CONFLUENCE
365
applied to the companion matrix. Since the entries of C(q) converge to the
entries of C(1) by assumption, to obtain the uniform convergence in a neigh-
borhood of ∞it is enough to control the convergence of the so called log-car
matrix(6). Let ζ = 1/ξ. The uniform convergence of (1 −q)ζθ′(q, ζ)/θ(q, ζ)
over the inﬁnite sector {| arg(ζ)| < π −ε} to log ζ is already proved in
Lemma 1.6. We need an analogous result for θ(q, ζ)/θ(q, cx) which is solu-
tion of the q-diﬀerence equation y(qζ) = cy(ζ), c ∈C∗. We give a proof of
the needed estimate, although it is a classical result:
Lemma 2.13. — Let c(q) ∈C∗be a function of q ∈(0, 1) such that
limq→1
log c
ln q = γ, ϵ ∈(0, π) and consider the sector Vϵ := {ζ ∈C∗: | arg ζ| ⩽
π −ϵ}. As q →1−, the following uniform estimate holds uniformly over Vϵ:
θ(q, ζ)
θ(q, cζ) = ζγ(1 + o(1 −q)).
Proof. — Let us consider again the modular equation (1.10) :
θ(q, √q) =
s
2π
ln(1/q)e−log2 x
2 ln q θ(q∗, √q∗x∗),
where
x∗= e−2πi
ln q log x,
q∗= e
4π2
ln q .
We observe that (ζ/√q)∗= −ζ∗and (cζ/√q)∗= −c∗ζ∗. Therefore we
obtain:
θ(q, ζ)
θ(q, cζ) = e
log c
ln q (log( ζ
√q )+ log c
2
) θ(q∗, −√q∗ζ∗)
θ(q∗, −√q∗c∗ζ∗).
As in the proof of Lemma 1.6, we observe that for any ζ ∈Vϵ, ζ∗∈V ∗
ϵ ;
see (1.12) for more details. Moreover, when X and Y denote two complex
numbers such that |X|, |Y | ∈(q∗, 1), we have the estimate:

θ(q∗, X)
θ(q∗, Y )

 ⩽
(−|X|; q∗)∞(−q∗
|X|; q∗)∞
(|Y |; q∗)∞( q∗
|Y |; q∗)∞
= θ(q∗, |X|)
θ(q∗, −|Y |).
An elementary calculation using (1.12) allows to conclude, since q∗→0+
and c∗→e−2πiγ.
□
(6)The terminology comes from the juxtaposition of the terms “logarithm” and “charac-
ter”, meaning the solution matrix of a constant coeﬃcient diﬀerential (resp. q-diﬀerence)
system is obtained by a combinatoric procedure from the logarithm (resp. q-logarithm)
and a family of characters (resp. q-characters). A solution in a regular singular point,
whose exponents are non resonant, is given by the product of an analytic matrix, called
uniform part, by the “log-car” matrix.
We are choosing here as a q-logarithm the logarithmic derivative of the Jacobi θ
function and as q-characters convenient quotient of the θ functions. For more details in
the q-diﬀerence setting cf. [16].
TOME 59 (2009), FASCICULE 1
366
Lucia DI VIZIO & Changgui ZHANG
Resuming, the function φ(q, ξ) is a linear combination, with coeﬃcients
that are continuous functions of q, of a canonical basis of solutions at ∞:
we have proved that both the canonical solutions and the coeﬃcients of the
linear combination admit a uniform limit in a bounded sector containing d,
centered at ∞and of arbitrary radius R > 0. Combined with Lemma 2.12,
this means that φ(q, x) converges uniformly to φ(1, x) in a neighborhood
of the direction d, which allows to conclude the proof.
