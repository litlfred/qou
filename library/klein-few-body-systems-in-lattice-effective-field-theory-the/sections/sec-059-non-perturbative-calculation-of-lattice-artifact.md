---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-Body Systems in Lattice Effective Field Theory"
section_id: sec-059-non-perturbative-calculation-of-lattice-artifact
section_title: "Non-perturbative calculation of lattice artifacts in the two-boson sector"
section_number: null
pages: 99-103
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
toc_source: outline
doc_brief: "Few-Body Systems in Lattice Effective Field Theory — 62 sections: Front matter; Introduction and Motivation; The standard model of particle phy"
---
in the two-boson sector
In Chap. 6 we argued that a non-perturbative treatment of cutoﬀ/ lattice spacing eﬀects in an eﬀective
framework is preferable but not practical. However, in the two-body sector with only contact interaction
it is possible. In the following we give explicit expressions for the coupling constants ∆C0 and Cq2 which
cancel the cutoﬀartifacts at O(a) and O(a3) in the T-matrix of the two-body sector. In general, we follow
the arguments of [112, 167]. The potential is written as
V

p, p′
= C + C2

p2 + p′2
,
(E.1)
where p, p′ are the momenta of incoming and outgoing state. For simplicity, C consists of its LO and
NLO term, C = C0 + ∆C. Then Eq. (E.1) can be reexpressed as
V

p, p′
=
1
X
i,j=0
p′2iλi jp2 j,
(E.2)
with
λ =
 C
C2
C2
0
!
.
(E.3)
Now the Lippmann-Schwinger equation has the form
T

p′, p; E

=
1
X
i,j=0
p′2iτi j(E)p2 j,
(E.4)
where τ must fulﬁll the following equation
τ(E) = λ + λI(E)τ(E),
(E.5)
with
I(E) =
 I0(E)
I2(E)
I2(E)
I4(E)
!
.
(E.6)
93
Appendix E Non-perturbative calculation of lattice artifacts in the two-boson sector
The full expressions for the integrals In(E) read
In(E) =
Z
π
a
−π
a
dk
2π
kn
E −k2
2µ + iϵ
,
(E.7)
I0(E) =
√
2µ tanh−1 
π
√
2a √Eµ

π √Eµ
,
(E.8)
I2(E) =
2
√
2µ √Eµ tanh−1 
π
√
2a √Eµ

π
−2µ
a ,
(E.9)
I4(E) = −2π2µ
3a3 −
4
√
2E2µ3 q
−1
Eµ tan−1

π
q
−1
Eµ
√
2a

π
−4Eµ2
a
.
(E.10)
Remember that the integral momentum cutoﬀΛ is given by Λ = π/a. The reduced mass of the system
reads µ. We can solve the integral equation in Eq. (E.5) and get an explicit solution for the T-matrix,
1
T on(E) =
C2I2 (E) −12 −I0(E)
h
C + C2
2I4 (E)
i
C + C2
C2
I4 (E) −4EI2 (E) µ (Eµ + 1)	 + 4Eµ (Eµ + 1).
(E.11)
Note that the integrals I2(E) and I4(E) are UV divergent for a →0. Therefore we regularize the
expressions such that the divergent parts are absorbed by the bare coupling constants. In the following
we use the regularized expressions, but we do not change the notation for better readability. Then the
inverse T-matrix reads
1
T on(E) =
√
2 √µ tanh−1 
π
√
2a
√
E √µ

(C + 4C2Eµ) −π
√
E
√
E

4
√
2C2
2E3/2µ5/2(2Eµ + 1) tanh−1 
π
√
2a
√
E √µ

−π C + 4C2Eµ(Eµ + 1).
(E.12)
As we want to do an eﬀective range expansion, we rewrite the previous equation in terms of p2 using the
dispersion relation E = p2/(2µ),
1
T on(p) =
√
2

√
2 √µ

C + 2C2p2
tanh−1

π
a √µ
r
p2
µ
−
π
r
p2
µ
√
2

r
p2
µ

2C2
2

p2 + 1

µ5/2 
p2
µ
3/2
tanh−1

π
a √µ
r
p2
µ
−π

C + 2C2

p2
2 + 1

p2

.
(E.13)
First of all, we set a = 0 and C2 = 0. Then the inverse scattering amplitude reads
1
T on(p) = 1
C + iµ
p,
(E.14)
which is the well-known solution in the case of momentum-independent zero-range interaction and which
gives a binding energy of EB = −C2m/4, the exact result already given by [62]. We expand the general
94
equation up to O(a3) and O(p2),
1
T on(p) = −2a3p2µ
3π4
−2aµ
π2 + p2

C2
2µ2
C
−2C2
C2
+ 1
C + iµ
p + O

a4, p4
,
(E.15)
where the lattice artifacts can be removed by redeﬁning the coupling constants depending on the lattice
spacing,
C(a) = C0 −
2aC2
0µ
2aC0µ + π2 ,
(E.16)
C2(a) =
C(a)
"
2
C(a)2 −
r
8a3µ3
3π4C(a) +
4
C(a)4
#
2µ2
.
(E.17)
Then the corrections start at least at O(a4) or in higher orders of the eﬀective range expansion, e.g. O(p4).
This means that we have successfully removed the lattice artifacts up to and including O(a3) in the
two-body sector.
95
