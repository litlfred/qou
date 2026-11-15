---
doc_id: arxiv-hep-th-0006111v2
doc_title: "arXiv:hep-th/0006111v2 14 Jul 2003"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 0006111v2.pdf
source_sha256: e024febd3d0886a3
toc_source: undetermined
doc_brief: "arXiv:hep-th/0006111v2 14 Jul 2003 — 6 sections: Page 1; Page 2; Page 3"
---
fermion species, with the partition function now being evaluated in a ﬁxed topological sector of eﬀective charge
ν = 1 + 2/β. Taking into account the deﬁnition (2), we then get, with Z(β)
ν
({µ}) denoting the partition functions in
the microscopic limit,
ω(β)
k (ζ1, . . . , ζk; {µ}) =
lim
N→∞
 k
Y
i=1
|ζi|
8N

Ω(β)
N,k( ζ2
1
8N , . . . , ζ2
k
8N ; { µ2
8N })
= const. e−βζ2
k/8ζ
β ν+1
2
−ν−1+ 2
β
k
Nf
Y
j=1
(µ2
j + ζ2
k)
1
2 −1
β
k−1
Y
i=1

ζβ(ν+1)−1
i
(ζ2
k −ζ2
i )
β
2 −1
Nf
Y
j=1
(ζ2
i + µ2
j)
 k−1
Y
i>j
(ζ2
i −ζ2
j )β
Nf
Y
j=1
µν
j
×
Z(β)
1+2/β(
p
µ2
1 + ζ2
k, . . . ,
q
µ2
Nf + ζ2
k,
β
z
}|
{
q
ζ2
k −ζ2
1, . . . ,
q
ζ2
k −ζ2
1, . . . ,
β
z
}|
{
q
ζ2
k −ζ2
k−1, . . . ,
q
ζ2
k −ζ2
k−1,
β(ν+1)/2−1
z
}|
{
ζk, . . . , ζk )
Z(β)
ν
(µ1, . . . , µNf )
.
(8)
This is the main result of our paper. It shows that the joint probability distribution of the ﬁrst k eigenvalues is given,
apart from the relatively simple prefactor, by a ratio of ﬁnite-volume partition functions. The new partition function
that enters in the numerator of Eq.(8) has the Nf original fermion masses shifted according to µi →
p
µ2
i + ζ2
k,
contains β(k −1) new fermions of masses
p
ζ2
k −ζ2
1, . . . ,
q
ζ2
k −ζ2
k−1 (each mass β-fold degenerate), β(ν + 1)/2 −1
additional degenerate fermion species of common mass ζk, and this whole partition function is evaluated in a sector of
ﬁxed topological charge ν = 1+2/β. While this topological index is fractional for β = 4, there is no diﬃculty with the
evaluation of the pertinent partition function. (Indeed, it can alternatively be viewed as a partition function in a sector
of topological charge ν = 0 and 3 additional massless fermions.) This expression entirely in terms of the eﬀective ﬁeld
theory partition functions strongly suggests that it should be possible to derive these analytical expressions starting
directly from the eﬀective ﬁeld theory, perhaps partially quenched as in Ref. [8]. The proportionality constant in
Eq.(8) depends on the normalization conventions of the involved partition functions. We ﬁx this numerical factor
uniquely by the requirement that the total probability of ﬁnding any given eigenvalue is normalized to unity.
Correlation functions of the rescaled eigenvalues {ζk1, . . . , ζkp−1, ζk} are obtained from ω(β)
k (ζ1, . . . , ζk; {µ}) by inte-
grating out the remaining eigenvalues in a cell 0 ≤ζ1 ≤· · · ≤ζk. In particular, the distribution of the k-th smallest
eigenvalue ζ, p(β)
k (ζ; {µ}), is given by
p(β)
k (ζ; {µ}) =
Z ζ
0
dζ1
Z ζ
ζ1
dζ2 · · ·
Z ζ
ζk−2
dζk−1 ω(β)
k (ζ1, . . . , ζk−1, ζ; {µ}) .
(9)
We note that this gives a very simple representation of the probability distribution of the k-th smallest Dirac operator
eigenvalue. In particular, already for the most elementary case of just the lowest Dirac operator eigenvalue in the
β = 2 universality class we obtain a very simple expression for an arbitrary topological sector ν. In the normalization
convention of, e.g., [7],
p(2)
1 (ζ, {µ}) = ζ
2e−ζ2/4 Nf
Y
j=1
µj
ν Z2(
p
µ2
1 + ζ2, . . . ,
q
µ2
Nf + ζ2,
ν
z }| {
ζ, . . . , ζ)
Zν(µ1, . . . , µNf )
,
(10)
a more compact and convenient expression than the one
provided in Ref. [23]. For example, in the quenched case
of Nf = 0 it yields the simple relation
p(2)
1 (ζ) = ζ
2e−ζ2/4 det[I2+i−j(ζ)] ,
(11)
where the determinant is over a matrix of size ν ×ν. It is
worth pointing out that also the corresponding quenched
distributions for β = 1 become exceedingly simple:
p(1)
1 (ζ) = const. ζ(3−ν)/2e−ζ2/8 Pf [(i −j)Ii+j+3(ζ)] ,
(12)
where the indices i and j run between −ν/2 + 1 and
ν/2 −1, and the Pfaﬃan is thus taken over a matrix of
size (ν −1) × (ν −1) [2]. For example, for ν = 1 this
formula gives
p(1)
1 (ζ) = ζ
4e−ζ2/8 ,
(13)
for ν = 3 we obtain
p(1)
1 (ζ) = 1
2e−ζ2/8I3(ζ) ,
(14)
3
