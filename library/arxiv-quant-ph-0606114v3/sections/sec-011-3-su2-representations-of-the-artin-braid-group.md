---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-011-3-su2-representations-of-the-artin-braid-group
section_title: "SU(2) Representations of the Artin Braid Group"
section_number: 3
pages: 15-21
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
Group
The purpose of this section is to determine all the representations of the three
strand Artin braid group B3 to the special unitary group SU(2) and concomi-
tantly to the unitary group U(2). One regards the groups SU(2) and U(2) as
acting on a single qubit, and so U(2) is usually regarded as the group of local
unitary transformations in a quantum information setting. If one is looking
for a coherent way to represent all unitary transformations by way of braids,
then U(2) is the place to start. Here we will show that there are many rep-
resentations of the three-strand braid group that generate a dense subset of
U(2). Thus it is a fact that local unitary transformations can be ”generated
by braids” in many ways.
We begin with the structure of SU(2). A matrix in SU(2) has the form
M =
 
z
w
−¯w
¯z
!
,
where z and w are complex numbers, and ¯z denotes the complex conjugate of
z. To be in SU(2) it is required that Det(M) = 1 and that M† = M−1 where
Det denotes determinant, and M† is the conjugate transpose of M. Thus if
z = a + bi and w = c + di where a, b, c, d are real numbers, and i2 = −1, then
M =
 
a + bi
c + di
−c + di
a −bi
!
with a2 + b2 + c2 + d2 = 1. It is convenient to write
M = a
 
1
0
0
1
!
+ b
 
i
0
0
−i
!
+ c
 
0
1
−1
0
!
+ d
 
0
i
i
0
!
,
and to abbreviate this decomposition as
M = a + bi + cj + dk
where
1 ≡
 
1
0
0
1
!
, i ≡
 
i
0
0
−i
!
, j ≡,
 
0
1
−1
0
!
, k ≡
 
0
i
i
0
!
so that
i2 = j2 = k2 = ijk = −1
and
ij = k, jk = i, ki = j
ji = −k, kj = −i, ik = −j.
The algebra of 1, i, j, k is called the quaternions after William Rowan Hamil-
ton who discovered this algebra prior to the discovery of matrix algebra. Thus
the unit quaternions are identiﬁed with SU(2) in this way. We shall use this
identiﬁcation, and some facts about the quaternions to ﬁnd the SU(2) repre-
sentations of braiding. First we recall some facts about the quaternions.
1. Note that if q = a + bi + cj + dk (as above), then q† = a −bi −cj −dk
so that qq† = a2 + b2 + c2 + d2 = 1.
2. A general quaternion has the form q = a + bi + cj + dk where the value
of qq† = a2 + b2 + c2 + d2, is not ﬁxed to unity. The length of q is by
deﬁnition
q
qq†.
3. A quaternion of the form ri + sj + tk for real numbers r, s, t is said to
be a pure quaternion. We identify the set of pure quaternions with the
vector space of triples (r, s, t) of real numbers R3.
4. Thus a general quaternion has the form q = a + bu where u is a pure
quaternion of unit length and a and b are arbitrary real numbers. A unit
quaternion (element of SU(2)) has the addition property that a2+b2 = 1.
5. If u is a pure unit length quaternion, then u2 = −1. Note that the
set of pure unit quaternions forms the two-dimensional sphere S2 =
{(r, s, t)|r2 + s2 + t2 = 1} in R3.
6. If u, v are pure quaternions, then
uv = −u · v + u × v
whre u · v is the dot product of the vectors u and v, and u × v is the
vector cross product of u and v. In fact, one can take the deﬁnition of
quaternion multiplication as
(a + bu)(c + dv) = ac + bc(u) + ad(v) + bd(−u · v + u × v),
and all the above properties are consequences of this deﬁnition. Note
that quaternion multiplication is associative.
7. Let g = a + bu be a unit length quaternion so that u2 = −1 and a =
cos(θ/2), b = sin(θ/2) for a chosen angle θ. Deﬁne φg : R3 −→R3 by
the equation φg(P) = gPg†, for P any point in R3, regarded as a pure
quaternion. Then φg is an orientation preserving rotation of R3 (hence
an element of the rotation group SO(3)). Speciﬁcally, φg is a rotation
about the axis u by the angle θ. The mapping
φ : SU(2) −→SO(3)
is a two-to-one surjective map from the special unitary group to the
rotation group. In quaternionic form, this result was proved by Hamilton
and by Rodrigues in the middle of the nineteeth century. The speciﬁc
formula for φg(P) as shown below:
φg(P) = gPg−1 = (a2 −b2)P + 2ab(P × u) + 2(P · u)b2u.
We want a representation of the three-strand braid group in SU(2). This
means that we want a homomorphism ρ : B3 −→SU(2), and hence we want
elements g = ρ(s1) and h = ρ(s2) in SU(2) representing the braid group
generators s1 and s2. Since s1s2s1 = s2s1s2 is the generating relation for B3,
the only requirement on g and h is that ghg = hgh. We rewrite this relation
as h−1gh = ghg−1, and analyze its meaning in the unit quaternions.
Suppose that g = a + bu and h = c + dv where u and v are unit pure
quaternions so that a2 + b2 = 1 and c2 + d2 = 1. then ghg−1 = c + dφg(v) and
h−1gh = a + bφh−1(u). Thus it follows from the braiding relation that a = c,
b = ±d, and that φg(v) = ±φh−1(u). However, in the case where there is a
minus sign we have g = a + bu and h = a −bv = a + b(−v). Thus we can now
prove the following Theorem.
Theorem 1. If g = a + bu and h = c + dv are pure unit quaternions,then,
without loss of generality, the braid relation ghg = hgh is true if and only if
h = a + bv, and φg(v) = φh−1(u). Furthermore, given that g = a + bu and
h = a+bv, the condition φg(v) = φh−1(u) is satisﬁed if and only if u·v = a2−b2
2b2
when u̸ = v. If u = v then then g = h and the braid relation is trivially
satisﬁed.
Proof. We have proved the ﬁrst sentence of the Theorem in the discussion
prior to its statement. Therefore assume that g = a + bu, h = a + bv, and
φg(v) = φh−1(u). We have already stated the formula for φg(v) in the discussion
about quaternions:
φg(v) = gvg−1 = (a2 −b2)v + 2ab(v × u) + 2(v · u)b2u.
By the same token, we have
φh−1(u) = h−1uh = (a2 −b2)u + 2ab(u × −v) + 2(u · (−v))b2(−v)
= (a2 −b2)u + 2ab(v × u) + 2(v · u)b2(v).
Hence we require that
(a2 −b2)v + 2(v · u)b2u = (a2 −b2)u + 2(v · u)b2(v).
This equation is equivalent to
2(u · v)b2(u −v) = (a2 −b2)(u −v).
If u̸ = v, then this implies that
u · v = a2 −b2
2b2
.
This completes the proof of the Theorem.
✷
An Example. Let
g = eiθ = a + bi
where a = cos(θ) and b = sin(θ). Let
h = a + b[(c2 −s2)i + 2csk]
where c2+s2 = 1 and c2−s2 = a2−b2
2b2 . Then we can reexpress g and h in matrix
form as the matrices G and H. Instead of writing the explicit form of H, we
write H = FGF † where F is an element of SU(2) as shown below.
G =
 
eiθ
0
0
e−iθ
!
F =
 
ic
is
is
−ic
!
This representation of braiding where one generator G is a simple matrix of
phases, while the other generator H = FGF † is derived from G by conjugation
by a unitary matrix, has the possibility for generalization to representations of
braid groups (on greater than three strands) to SU(n) or U(n) for n greater
than 2. In fact we shall see just such representations constructed later in this
paper, by using a version of topological quantum ﬁeld theory. The simplest
example is given by
g = e7πi/10
f = iτ + k√τ
h = frf −1
where τ 2+τ = 1. Then g and h satisfy ghg = hgh and generate a representation
of the three-strand braid group that is dense in SU(2). We shall call this the
Fibonacci representation of B3 to SU(2).
Density. Consider representations of B3 into SU(2) produced by the method
of this section. That is consider the subgroup SU[G, H] of SU(2) generated by
a pair of elements {g, h} such that ghg = hgh. We wish to understand when
such a representation will be dense in SU(2). We need the following lemma.
Lemma. eaiebjeci = cos(b)ei(a+c) +sin(b)ei(a−c)j. Hence any element of SU(2)
can be written in the form eaiebjeci. for appropriate choices of angles a, b, c. In
fact, if u and v are linearly independent unit vectors in R3, then any element
of SU(2) can be written in the form
eauebvecu
for appropriate choices of the real numbers a, b, c.
Proof. It is easy to check that
eaiebjeci = cos(b)ei(a+c) + sin(b)ei(a−c)j.
This completes the veriﬁcation of the identity in the statement of the Lemma.
Let v be any unit direction in R3 and λ an arbitrary angle. We have
evλ = cos(λ) + sin(λ)v,
and
v = r + si + (p + qi)j
where r2 + s2 + p2 + q2 = 1. So
evλ = cos(λ) + sin(λ)[r + si] + sin(λ)[p + qi]j
= [(cos(λ) + sin(λ)r) + sin(λ)si] + [sin(λ)p + sin(λ)qi]j.
By the identity just proved, we can choose angles a, b, c so that
evλ = eiaejbeic.
Hence
cos(b)ei(a+c) = (cos(λ) + sin(λ)r) + sin(λ)si
and
sin(b)ei(a−c) = sin(λ)p + sin(λ)qi.
Suppose we keep v ﬁxed and vary λ. Then the last equations show that this
will result in a full variation of b.
Now consider
eia′evλeic′ = eia′eiaejbeiceib′ = ei(a′+a)ejbei(c+c′).
By the basic identity, this shows that any element of SU(2) can be written in
the form
eia′evλeic′.
Then, by applying a rotation, we ﬁnally conclude that if u and v are linearly
independent unit vectors in R3, then any element of SU(2) can be written in
the form
eauebvecu
for appropriate choices of the real numbers a, b, c.
✷
This Lemma can be used to verify density of a representation, by ﬁnding
two elements A and B in the representation such that the powers of A are dense
in the rotations about its axis, and the powers of B are dense in the rotations
about its axis, and such that the axes of A and B are linearly independent in
R3. Then by the Lemma the set of elements Aa+cBbAa−c are dense in SU(2).
It follows for example, that the Fibonacci representation described above is
dense in SU(2), and indeed the generic representation of B3 into SU(2) will
be dense in SU(2). Our next task is to describe representations of the higher
braid groups that will extend some of these unitary repressentations of the
three-strand braid group. For this we need more topology.
4
