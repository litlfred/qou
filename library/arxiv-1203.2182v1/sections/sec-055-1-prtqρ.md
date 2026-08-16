---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-055-1-prtqρ
section_title: "PRt(q−ρ"
section_number: 1
pages: 55-58
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
1 ;q2,q 1) (4.2)
×
∑
S
(q2
q1
) |S|+|P |−|Q|
2
sP t/S(q−ρ
1 q−R
2 )sQ/S(q−Rt
1 q−ρ
2 ).
In particular
C••R(q−1
1 ,q −1
2 ) = (−1)|R|
(q1
q2
) |R|/2
q||Rt||2/2
1
∏
(i,j)∈R
1
1 −qa(i,j)+1
1 ql(i,j)
2
, (4.3)
wherea(i,j ) =Ri −j andl(i,j ) =Rt
j −i denote the arm-length and leg-length in a diagram
R.
– 54 –
A few notational remarks are in order. Parameters t and q from the original formu-
lation in [76] are replaced in the above expression respecti vely by q1 and q2, which agrees
with conventions in [35, 44]. The non-reﬁned limit correspo nds to q1 = q2. Similarly as in
[76], in computing open string amplitudes we use vertex ampl itudes with inverse parameters
CP QR(q−1
1 ,q −1
2 ). Moreover, following the convention in [35], we denote sym metric represen-
tation Sr by a Young diagram R = (r).
The framing factor (associated to the amplitude already exp ressed in terms of q−1
1 and
q−1
2 ) is deﬁned as
fR(q1,q 2) = (−1)|R|
(q1
q2
) n(R)
q
− κR
2
2 , (4.4)
where
n(R) :=
∑
i
(i − 1)Ri. (4.5)
We typically allow general values of framing by including th is factor raised to the power −f.
So, in particular, for the representation R = (r) the framing factor takes the form
f(r)(q1,q 2)−f = ( −1)f rq
f
2 r(r−1)
2 .
Using the above conventions we are able to compute reﬁned BPS state generating func-
tionsZ open
BPS (u,q 2,q 1) of toric manifolds in the presence of branes. However, what we are really
interested in are diﬀerence operators which annihilate thes e open reﬁned BPS partition func-
tions (up to, possibly, some universal inhomogeneous term) and reﬁned mirror curves which
arise as classical limits of these diﬀerence operators. As we demonstrate below, from the
knowledge of Z open
BPS (x,q 2,q 1) we are able to determine such diﬀerence operators, at least f or
a class of toric manifolds which do not contain compact 4-cyc les. It turns out that the role
of parameters in these operators is as follows: q2 is the quantum parameter which enters the
commutation relation
ˆyˆx = q2ˆxˆy, (4.6)
and, therefore, it plays the role of q in previous sections. 14 Combining this with the fact
that q1 = q2 = q deﬁnes the unreﬁned limit, i.e. the limit t = −1 in the notations of the
previous sections, we quickly conclude that, up to a slight r edeﬁnition q1 ↦→q2
1 and q2 ↦→q2
2,
the identiﬁcation of the parameters is essentially as in (3. 67):
q = q2, t = −q1
q2
. (4.7)
Note, with this identiﬁcation of the parameters, in the clas sical limit, i.e. when q =q2 = 1,
we can simply identifyt with −q1. Of course, with diﬀerent choices of the preferred direction ,
etc., the role of q1 and q2 could be diﬀerent.
14This will become clearer a little later, when in (4.10) and (4 .18) we start writing the generating functions
Zopen
BPS (x, q2, q1) in terms of products of the form ∏ k
i=1(1 − q1qi−1
2 ), where q2 plays the key role.
– 55 –
q2
1q =(        1: Nekrasov−Shatashvili limit) q12q =         1: classical limit
q = q = q
unrefined
1
2
quantization
refinement
t=−q
refinement
q
q1
2
t = −
1(deformation parameter             )
Figure 9: With our choice of conventions, the parameter q2 =q =eℏ is responsible for quantization,
whereas t = − q1
q2
is the deformation parameter responsible for the reﬁnement. Hen ce, the “classical
limit” corresponds to q2 = 1, while q1 = 1 is the so-called Nekrasov-Shatashvili limit. Finally, q1 =q2
deﬁnes a locus in the space of parameters where reﬁnement is turn ed oﬀ, and the problem can be
formulated in terms of ordinary topological strings.
Having found the diﬀerence operator, or quantum curve, we can analyze asymptotic be-
havior of Z open
BPS (x,q 2,q 1) and determine the leading order amplitude S0(x,q 1) =
∫
logy dx
x .
Using saddle point analysis we can also determine the form of the reﬁned mirror curve
Aref(x,y ;q1), and show that it agrees with the classical limitq2 → 1 of the diﬀerence equation.
Before we present detailed results, let us stress that the form of the open string amplitude
depends on various choices, such as preferred direction, fr aming, and the edge of a toric
diagram to which the brane is attached. We will mainly discus s the most interesting case
of branes on the external edges, along the preferred directi on. This is certainly the most
interesting case for C3 geometry, as in that case Z open
BPS (x,q 2,q 1) is a nontrivial function of
both q1 andq2. For branes associated to either of the two non-preferred di rections of C3, the
amplitudesZ open
BPS (x,q 2,q 1) are given entirely in terms of eitherq1 orq2, and essentially do not
diﬀer from non-reﬁned amplitudes [76]. Moreover, for branes along the preferred direction,
an inhomogeneous term arises in the diﬀerence equation. Havi ng found such inhomogeneous
equation, we show that it implies that a homogeneous equatio n of a higher order is also
satisﬁed. For more complicated geometries some simpliﬁcat ions occur for branes along non-
preferred directions, which is also a reason why the branes a long the preferred direction are
– 56 –
most interesting in general. In all cases, we will consider b ranes with arbitrary value of
framing.
