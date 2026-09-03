---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-010-2-tξη2dt
section_title: "(t−ξ−¯η)2dt"
section_number: 2
pages: 26-30
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
=
e ¯ηξ
r!
√
2π
Z −¯η−ξ
−∞
Hr(t + ¯η −¯ξ)Hr(t + ξ −η)e−1
2 t2dt.
The proof is complete.
□
Remark 5.5. The special case r = 0 of the kernel in Proposition 5.4 is eξ ¯ηerf(−ξ −¯η),
which is what we have on the right-hand side in Lemma 5.3.
The blow-up of the polynomial space at the boundary point. We turn to the
polyanalytic analogue of the left-hand side of Lemma 5.3.
Deﬁnition 5.6. We introduce the blow-up space at 1,
Pol⟨1⟩
m,n,q :=
n
e−m1/2ξp(1 + m−1/2ξ) : p ∈Polm,n,q
o
,
which we equip with the norm

ξ 7→e−m1/2ξp(1 + m−1/2ξ)

δPol⟨1⟩
m,n,q := m1/2e
1
2 m∥p∥L2(C,e−m|z|2).
For 0 ≤r ≤q −1, we denote by δPol⟨1⟩
m,n,r+1 the subspace
δPol⟨1⟩
m,n,r+1 :=
n
e−m1/2ξp(1 + m−1/2ξ) : p ∈δPolm,n,r+1
o
,
equipped with the same norm.
An elementary change of variables argument allows us to identify the norm
on Pol⟨1⟩
m,n,q with that of A2
m,q(C):
(5.3)

ξ 7→e−m1/2ξp(1 + m−1/2ξ)

Pol⟨1⟩
m,n,r+1 =

ξ 7→e−m1/2ξp(1 + m−1/2ξ)

A2
1,r+1(C).
As a consequence, we may regard Pol⟨1⟩
m,n,q and δPol⟨1⟩
m,n,r+1 as norm closed subspaces
of A2
1,q(C). We may read oﬀfrom the deﬁnition of the norm in δPol⟨1⟩
m,n,r+1 that the
kernel on the left-hand side in Lemma 5.3 is the reproducing kernel for the space
Pol⟨1⟩
m,n,1. So, Lemma 5.3 can be understood as saying that
(5.4)
KPol⟨1⟩
m,n,1(ξ, η) = KB0[L2(R−)](ξ, η) + O(m−1
2 +ε),
The Polyanalytic Ginibre Ensembles
27
where KPolm,n,1 and KB0[L2(R−)] denote the reproducing kernels of the spaces in the
subscripts, and the bound is locally uniform on compact subsets. We want to
generalize (5.4) beyond r = 0. To this end, we make use of the operators Tr.
Proposition 5.7. For r = 1, 2, 3, . . ., we have that
r−1/2T1 : δPol⟨1⟩
m,n,r →δPol⟨1⟩
m,n,r+1
is an isometric isomorphism.
Proof. From the isometry properties of Tr−1 and Tr together with the semi-group
property r−1/2T1 ◦Tr−1 = Tr, we get that
r−1/2T1 : δA2
1,r(C) →δA2
1,r+1(C)
is an isometric isomorphism. In view of (5.3), the isometry part of the assertion
follows. It remains to show that the operator is onto. This is an algebraic exercise
which we leave to the reader.
□
By iterating Proposition 5.7, we obtain the following.
Corollary 5.8. For r = 1, 2, 3 . . ., we have that
Tr : Pol⟨1⟩
m,n,1 →δPol⟨1⟩
m,n,r+1
is an isometric isomorphism.
The blow-up of the polynomial reproducing kernel at a boundary point. From
Corollary 5.8 above, we get that
(5.5)
KδPol⟨1⟩
m,n,r+1(ξ, η) = [Tr]ξ[ ¯Tr]η

KPol⟨1⟩
m,n,1(ξ, η)

,
where the subscripts z and w are used to indicate that the operator is acting with
respect to that variable, and the bar means complex conjugation of the operator.
To be more precise,
¯Tr[ f](z) :=
1
√
r!
e|z|2 ¯∂r
z
n
f(z)e−|z|2o
.
We would like to plug in the approximation (5.4) into (5.5). The operator Tr is a
sum of certain polynomials in ¯z of degree ≤r times the diﬀerential operator ∂z
to powers ≤r. The Cauchy integral formula allows us to control the size of the
derivatives on a compact subset in terms of the size of the functions on a slightly
bigger compact subset. This means that the approximation (5.4) carries over, and
we ﬁnd that
(5.6)
KδPol⟨1⟩
m,n,r+1(ξ, η) = [Tr]ξ[ ¯Tr]η

KB0[L2(R−)](ξ, η)

+ O(m−1
2 +ε),
with uniform control on compact subsets. Next, as
Pol⟨1⟩
m,n,q =
q−1
M
r=0
δPol⟨1⟩
m,n,r+1,
28
Haimi and Hedenmalm
we get that
(5.7)
KPol⟨1⟩
m,n,q(ξ, η) =
q−1
X
r=0
KδPol⟨1⟩
m,n,r+1(ξ, η)
=
q−1
X
r=0
[Tr]ξ[ ¯Tr]η

KB0[L2(R−)](ξ, η)

+ O(m−1
2 +ε),
again with uniform control on compact subsets. Next, it should be rather clear
that
[Tr]ξ[ ¯Tr]η

KB0[L2(R−)](ξ, η)

is the reproducing kernel for the space TrB0[L2(R−)] = Br[L2(R−)], which was
identiﬁed in terms of Hermite polynomials back in Proposition 5.4. We write this
down as a proposition.
Proposition 5.9. Fix a positive real number ε. Then the reproducing kernel for Pol⟨1⟩
m,n,q
has the following form:
KPol⟨1⟩
m,n,q(ξ, η) =
q−1
X
r=0
eξ ¯η
r!
√
2π
Z −ξ−¯η
−∞
Hr(t + ξ −η)Hr(t + ¯η −¯ξ)e−1
2 t2dt + O(m−1
2 +ε),
as m, n →+∞while n = m + O(1), where the control is uniform on compact subsets.
If we like, we may use the classical Christoﬀel-Darboux identity
(5.8)
q−1
X
r=0
1
r!Hr(x)Hr(y) =
Hq(x)Hq−1(y) −Hq−1(x)Hq(y)
(q −1)!(x −y)
to rewrite the above sum. Also, we should note that reproducing kernel for the
blow-up space Pol⟨1⟩
m,n,q is connected with the reproducing kernel Km,n,q for Polm,n,q
via the identity
(5.9)
KPol⟨1⟩
m,n,q(ξ, η) = m−1e−m−m1/2(ξ+ ¯η)Km,n,q(1 + m−1/2ξ, 1 + m−1/2η).
The blow-up of the 1-point intensity near a boundary point. The 1-point intensity
function is
Km,n,q(z, z)e−m|z|2,
and the localized version with z = 1 + m−1/2ξ is
Um,n,q(ξ) := m−1Km,n,q(1 + m−1/2ξ, 1 + m−1/2ξ) e−m|1+m−1/2ξ|2,
where we throw in a factor of m−1 to compensate for the Jacobian. In view of (5.9)
together with Proposition 5.9, we obtain
Um,n,q(ξ) =
q−1
X
r=0
1
r!
√
2π
Z −2 Re ξ
−∞
Hr(t)2e−1
2 t2dt + O(m−1
2 +ε).
So, essentially, the 1-point intensity function is determined by the density
t 7→
q−1
X
r=0
1
r!
√
2π
Hr(t)2e−1
2 t2,
The Polyanalytic Ginibre Ensembles
29
which corresponds to ﬁlling the lowest energy eigenstates of the harmonic oscil-
lator. By the Wigner semi-circle law, then, we get the approximation
Um,n,q(ξ) ≈2q
π
Z −q−1/2 Re ξ
−1
√
1 −τ2dτ,
valid for big m, n with n = m + O(1), and big q (but much smaller than m, n). So,
if we rescale to characteristic distance q1/2m−1/2 we ﬁnd an interesting law in the
limit.
The blow-up Berezin density at a boundary point. The blow-up Berezin density
at 1 is given by
ˆB⟨1⟩
m,n,q(ξ) = m−1B⟨1⟩
m,n,q(1 + m−1/2ξ) = m−1e−m|1+m−1/2ξ|2 |Km,n,q(1 + m−1/2ξ, 1)|2
Km,n,q(1, 1)
.
From (5.9), we have that
KPol⟨1⟩
m,n,q(0, 0) = m−1e−mKm,n,q(1, 1),
while Proposition 5.9 gives
KPol⟨1⟩
m,n,q(0, 0) =
q−1
X
r=0
1
r!
√
2π
Z 0
−∞
Hr(t)2e−1
2 t2dt + O(m−1
2 +ε),
as m, n →+∞with n = m + O(1). Now, as each Hermite polynomial Hr is either
even or odd,
Z 0
−∞
Hr(t)2e−1
2 t2dt = 1
2
Z +∞
−∞
Hr(t)2e−1
2 t2dt = r!
√
2π
2
,
which leads to
KPol⟨1⟩
m,n,q(0, 0) = q
2 + O(m−1
2 +ε)
and
Km,n,q(1, 1) = 1
2 mqem[1 + O(m−1
2 +ε)].
A similar calculation gives that
Km,n,q(1 + m−1/2ξ, 1) = mem+m1/2ξKPol⟨1⟩
m,n,q(ξ, 0)
= mem+m1/2ξ
 q−1
X
r=0
1
r!
√
2π
Z −ξ
−∞
Hr(t + ξ)Hr(t −¯ξ)e−1
2 t2dt + O(m−1
2 +ε)

.
Putting things together, we obtain the following asymptotics for the blow-up
Berezin density.
Theorem 5.10. Fix a positive real number ε. Then the blow-up Berezin density at 1 has
the following form:
ˆB⟨1⟩
m,n,q(ξ) = 1
πq

q−1
X
r=0
1
r!
Z −ξ
−∞
Hr(t + ξ)Hr(t −¯ξ)e−1
2 t2dt

2
+ O(m−1
2 +ε),
as m, n →+∞while n = m + O(1), where the control is uniform on compact subsets.
Remark 5.11. When we make some explicit calculations based on Theorem 5.10,
we see that the Fresnel zone pattern is less pronounced for a boundary point z.
30
Haimi and Hedenmalm
Acknowledgements. We would like to thank Philip Kennerberg for sharing shar-
ing his MATLAB-code and discussing the practicalities in simulating the process.
