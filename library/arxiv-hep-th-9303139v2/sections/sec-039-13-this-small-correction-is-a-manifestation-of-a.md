---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-039-13-this-small-correction-is-a-manifestation-of-a
section_title: "This small correction is a manifestation of a very general phenomenon: from the"
section_number: 13
pages: 31-35
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
point of view of symmetries (Ward identities) it is more natural to consider ZV not as a
function of T -variables, but of some more complicated combination ˆTk + rk, depending on
the shape of potential V . If V is a polinomial of degree p + 1, ˆTk = 1
ktr(V ′(λ))−k/p, while
rk =
p
k(p−k)Res (V ′(µ))1−k
p dµ. For monomial potentials these expressions become very
simple: ˆTk = Tk and rk = −
p
p+1δk,p+1. See [39] and section 4.9 below for more details.
In most places in these notes we prefer to use invariant potential-independent times Tk,
instead of ˆTk, but then Ward identites acquire some extra terms with rk (which in fact
will be very simple in our examples, which are all given for monomial potentials).
28
Thus we found that the WI of the Gaussian Kontsevich model (2.47)
coincide with those of the ordinary 1-matrix model, moreover the size of the
matrix N in the latter model is associated with the ”zero-time” in the former
one. This result [56] of course implies, that the two models are identical:
e−NT0Z X2
2 {N, T1, T2, . . .} ∼ZN{T0, T1, T2, . . .}.
(2.53)
We shall discuss direct connection between these two matrix integrals (2.1)
and (2.47) in the next section, after some more details will be presented
about the structure of ”eigenvalue” matrix models.
2.7
Continuous Virasoro constraints for the V =
X3
3
Kontsevich model
This example is a little more complicated than that in the previous subsec-
tion, and we do not present calculations in full details (see [24] and [30]). Our
goal is to demonstrate that the constraints which arise in this model, though
still form (Borel subalgebra of) some Virasoro algebra, are different from
(2.6). From the point of view of the CFT-formulation the relevant model is
that of the twisted (in this particular case - antiperiodic) free ﬁelds. These so
called ”continuous Virasoro constraints” give the simplest illustration of the
diﬀerence between discrete and continuous matrix models: this is essentially
the diﬀerence between ”homogeneous” (Kac-Frenkel) and ”principal” (soli-
ton vertex operator) representation of the level k = 1 Kac-Moody algebra.
From the point of view of integrable hierarchies this is the diﬀerence between
Toda-chain-like and KP-like hierarchies. We shall come back to a more de-
tailed discussion of this diﬀerence later, when the ”multi-scaling continuum
limit” will be considered.
Another (historical) aspect of the same relation also deserves mentioning,
since it also illustrates the interrelation between diﬀerent models. The dis-
crete 1-matrix model arises naturally in description of quantum 2d gravity as
sum over 2-geometries in the formalism of random equilateral triangulations.
The model, however, decribes only lattice approximation to 2d gravity and
(double-scaling) coninuum limit should be taken in order to obtain the real
(continuous) theory of 2d gravity. This limit was originally formulated in
terms of the contraint algebra (equations of motion or ”loop” or ”Schwinger-
Dyson” equations - terminology is taste-dependent), leaving open the prob-
29
lem of what is the form of partition function Zcont{T} of continuous theory.
Since the relevant algebra appeared to be just the WI for Kontsevich model
(with V (X) = X3
3 ), this proves that the latter one is exactly the continuous
theory of pure 2d gravity. At the same time, Kontsevich model itself can be
naturally introduced as a theory of topological gravity (in fact this is how
the model was originally discovered in [22]). From this point of view the
constraint algebra, to be discussed below in this subsection, plays central
role in the proof of equivalence between pure 2d quantum gravity and pure
topological gravity (in both cases ”pure” means that ”matter” ﬁelds are not
introduced).
After these introductory remarks we proceed to calculations. Actually
they just repeat those for the Gaussian model, performed in the previous
subsection, though formulas get somewhat more complicated. This time we
do not include zero-time N and just use eq.(2.37) with V (X) = X3
3 . Now
it is also much more tricky (though possible) to work in matrix notations
(because fractional powers of L will be involved) and we rewrite everything
in terms of the eigenvalues of L.
We substitute
C X3
3 =
Q
δ e
2
3 λ3/2
δ
rQ
γ,δ(√λδ +
q
λγ)
,
 ∂2
∂L2
tr
!
γγ
= ∂2
∂λ2
γ
+
X
δ̸=γ
1
λγ −λδ
 ∂
∂λγ
−∂
∂λδ
!
and introduce a special notation for
D
Dλγ
≡C−1
X3
3
∂
∂λγ
C X3
3 =
∂
∂λγ
+
q
λγ −
1
4λγ
−1
2
X
δ̸=γ
1
q
λγ(√λδ +
q
λγ)
.
Then (2.37) turns into


 D
Dλγ
!2
+
X
δ̸=γ
1
λγ −λδ
 D
Dλγ
−D
Dλδ
!
Z X3
3 {T} = 0.
(2.54)
Now we need explicit expression for T:
Tk = 1
kL−k,
(2.55)
30
and as we already know from the previous subsection we also need
rk = −2
3δk,3.
(2.56)
It will not be explained untill we turn to consideration of integrable struc-
ture of Kontsevich model in the following sections, but Z X3
3 {T} is in fact
independent of all time-variables with even numbers (subscripts). Therefore
we can take only k = 2a + 1 in (2.55),
T2a+1 =
1
2a+1
P
δ λ
−a−1
2
δ
,
r2a+1 = −2
3δa,1
(2.57)
and
∂
∂λγ
Z X3
3 {T} =
P∞
a=0
∂T2a+1
∂λγ
∂Z
∂T2a+1 = −1
2
P∞
a=0 λ
−a−3
2
γ
∂Z
∂T2a+1;
∂2
∂λ2
γ
Z X3
3 {T} = 1
4
P∞
a,b=0 λ−a−b−3
γ
∂Z
∂T2a+1∂T2b+1 + 1
2
P∞
a=0(a + 3
2)λ
−a−5
2
γ
∂Z
∂T2a+1.
These expressions should be now substituted into (2.54) and we obtain:
1
4
∞
X
a,b=0
λ−a−b−3
γ
∂Z
∂T2a+1∂T2b+1
+
+
∞
X
a=0

1
2
∞
X
a=0
(a + 3
2)λ
−a−5
2
γ
−1
2
X
δ̸=γ
1
λγ −λδ

λ
−a−3
2
γ
−λ
−a−3
2
δ

−
−


q
λγ −
1
4λγ
−1
2
X
δ̸=γ
1
q
λγ(√λδ +
q
λγ)

λ
−a−3
2
γ


∂Z
∂T2a+1
+
+ [. . .] Z
=
∞
X
n=−1
1
λn+2
γ
LnZ
(2.58)
31
with
L2n =
∞
X
a=0

a + 1
2

(T2a+1 + r2a+1) ×
×
∂
∂T2a+2n+1
+ 1
4
X
a+b=n−1
a,b≥0
∂2
∂T2a+1∂T2b+1
+ 1
16δn,0 + 1
4T 2
1 δn,−1 =
= 1
2
∞
X
odd k=1
k(Tk + rk)
∂
∂Tk+2n
+ 1
4
2n−1
X
odd k=1
∂2
∂Tk∂T2n−k
+ 1
16δn,0 + 1
4T 2
1 δn,−1.
(2.59)
Factor 1
2 in front of the ﬁrst term at the r.h.s. in (2.59) is important for L2n
to satisfy the properly normalized Virasoro algebra:14
[L2n, L2m] = (n −m)L2n+2m.
Coeﬃcient 1
4 in front of the second term can be eliminated by rescaling of
time-variables: T →1
2T, then the last term turns into
1
16T 2
1 δn,−1.
We shall not actually discuss evaluation of the coeﬃcient in front of Z
(with no derivatives), which is denoted by [. . .] in (2.58) (see [24] and [30]).
In fact almost all the terms in original complicated expression cancel, giving
ﬁnally
[. . .] =
1
16λ2γ
+ T 2
1
4λγ
,
and this is represented by the terms with δn,0 and δn,−1 in expressions (2.59)
for the Virasoro generators L2n.
The term with the double T-derivative in (2.58) is already of the necessary
form. Of intermidiate complexity is evaluation of the coeﬃcient in front of
∂Z
∂T2a+1 in (2.58), which we shall brieﬂy describe now. First of all, rewrite this
coeﬃcient, reordering the items:
1
2

(a + 3
2)λ
−a−5
2
γ
−
X
δ̸=γ
1
λγ −λδ

λ
−a−3
2
γ
−λ
−a−3
2
δ

+
+

1
4λ
−a−5
2
γ
+ 1
2
X
δ̸=γ
λ−a−2
γ
√λδ +
q
λγ

−λ−a−1
γ
.
(2.60)
