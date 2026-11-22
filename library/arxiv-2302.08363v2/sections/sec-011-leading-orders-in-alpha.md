---
doc_id: arxiv-2302.08363v2
doc_title: "On the structure of trans-series in quantum field theory"
section_id: sec-011-leading-orders-in-alpha
section_title: "Leading orders in alpha"
section_number: null
pages: 28-29
source_pdf: 2302.08363v2.pdf
source_sha256: c2244e03b17048fb
toc_source: outline
doc_brief: "On the structure of trans-series in quantum field theory — Many observables in quantum field theory can be expressed in terms of trans-series, in which one adds to the perturbative series a typically"
---
The leading order in ˜α is obtained by neglecting all terms with the integral operator I. In this
case we obtain simple recursive relations. The uk are solved by
u(0,0)
k
=
Υ
2k −1,
u(0,s)
k
= Υ
2
X
s+1
2
≥r≥1
¯ρru(0,s+1−2r)
r
k + r −1
,
(5.101)
which is simple to solve order by order, although hard to solve in closed form. Similarly, we
obtain
u(0,0)
i
= 1,
u(0,s)
i
= Υ
X
s+1
2
≥r≥1
¯ρru(0,s+1−2r)
r
2r −1 + Υ ,
f(0,0)
v
= 1,
f(0,s)
v
= −Υ
X
s+1
2
≥r≥1
¯ρru(0,s+1−2r)
r
2r −1 −Υ .
(5.102)
From these building blocks, regular power series manipulations are sufficient to extract a0,ℓ. For
example, we obtain
a0,0 = 1,
a0,1 = 2
Υ−2
Υ Υ2¯ρ1
Υ2 −1 ,
a0,2 = 2
Υ−4
Υ Υ2¯ρ2
1
(Υ + 1)2 ,
a0,3 = 1
32−Υ+6
Υ
3Υ2(3Υ −7)¯ρ3
1
(Υ + 1)3
+
4¯ρ2
Υ2 −9

.
(5.103)
All the an,ℓare polynomials in the residues ¯ρi, but only monomials ¯ρp1
i1 ¯ρp2
i2 · · · ¯ρpk
ik that satisfy
k
X
j=1
pj(2ij −1) = ℓ
(5.104)
– 27 –
contribute to an,ℓ. The polynomial coefficients for a0,ℓare rational up to an overall irrational
power of 2, and only at higher orders in ˜α does one find transcendental numbers. Nevertheless,
the ¯ρk are themselves transcendental, as can be seen in (5.81).
The next to leading order in ˜α can be immediately obtain from the leading one. Because
the perturbative part of ¯u(η) is one order lower than the non-perturbative, i.e.
u(0,0)(η) = 1
η,
u(0,n)(η) = 0,
u(1,ℓ)(η) = ¯u(ℓ)(η)

v=0,
(5.105)
the recursive problem is the same and the solution only differs by an overall constant. Concretely,
u(1,s)
k
= −∆u(0,s)
k
,
u(1,s)
i
= −∆u(0,s)
i
,
f(1,s)
v
= −∆f(0,s)
v
F(1,s)
v
= −2∆F(0,s)
v
.
(5.106)
For the change of variables, we find first that
v = ˜α
2 + O(˜α2),
(5.107)
without any term proportional to q± at order ˜α or lower. Furthermore,
q1,ℓ= ∆ℓ
Υ q0,ℓ,
(5.108)
which leads to
a1,ℓ= ∆
 ℓ
Υ −1

a0,ℓ.
(5.109)
Naturally, G1(y) has the same radius of convergence as G0(y). At the next order in ˜α, there are
no such shortcuts.
