---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-004-212-standard-modules
section_title: "Standard modules"
section_number: 2.1.2
pages: 6-8
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
It is readily checked that for any ﬁnite N, the algebra Ta
N(m) obeying the deﬁning relations (8)–(9) is in fact
inﬁnite-dimensional. We wish however to focus on lattice models having a ﬁnite number of degrees of freedom per
site. Their proper description involves certain ﬁnite-dimensional representations of Ta
N, the so-called standard
modules Wj,eiφ, which depend on two parameters. Diagrammatically, the ﬁrst parameter deﬁnes the number
of through-lines 2j, with j = 0, 1,..., N
2 . In addition to the action of the algebra described in the previous
subsection, we now require that the result of this action be zero in the standard modules whenever the aﬃne
diagrams obtained have a number of through-lines strictly less than 2 j, i.e., whenever two or more free sites
are contracted. Moreover, for any j >0 it is possible, the algebra action can cyclically permute the free sites.
Such cyclic permutations give rise to a pseudomomentum, which we parametrize by φ and deﬁne as follows:
Whenever 2j through-lines wind counterclockwise around the annulus l times, we can unwind them at the price
of a factor eijlφ; and similarly, for clockwise winding, the phase is e−ijlφ [30, 36]. In other words, there is a
phase e±iφ/2 attributed to each winding through-line.
To deﬁne the representation Wj,eiφ in more convenient diagrammatic terms, we now make the following
remark. As free sites cannot be contracted, the pairwise connections between non-free sites on the inner
boundary is unchanged under the algebra action. This part of the diagrammatic information is thus irrelevant
and can be omitted. Therefore, it is enough to concentrate on the upper halves of the aﬃne diagrams, obtained
by cutting a diagram into two parts across its 2 j through-lines. Each upper half diagram is then called a link
6
state. We still call through-lines the cut “upper half” through-lines attached to the free sites on the outer
boundary (or, equivalently, top side of the framing rectangle). A phase eiφ/2 (resp. e−iφ/2) is attributed as
before, namely each time one of these through-lines moves through the periodic boundary condition of the
framing rectangle in the rightward (resp. leftward) direction. It is not diﬃcult to see that the Temperley-Lieb
algebra action obtained by stacking the aﬃne diagrams on top of the link states produces exactly the same
representations Wj,eiφ as deﬁned above.
To identify the dimensions of these modules Wj,eiφ over Ta
N(m) we simply need to count the link states. The
result is
ˆdj =
( N
N
2 +j
)
(10)
for thej >0 case, and we shall return to the j = 0 case below. Notice that these dimensions are independent of
φ (although representations with diﬀerent eiφ are not isomorphic). The standard modules Wj,eiφ are also called
cell Ta
N(m)-modules [29].
Let us parametrize m = q + q−1. For generic values of q and φ the standard modules Wj,eiφ are irreducible,
but degeneracies appear when the following resonance criterion is satisﬁed [29,30]: 3
eiφ = q2j+2k, for k> 0 integer. (11)
The representation Wj,q2j+2k then becomes reducible, and contains a submodule isomorphic to Wj+k,q2j. The
quotient of those two is generically irreducible, with dimension
¯dj := ˆdj− ˆdj+k, for j >0. (12)
For q a root of unity, there are inﬁnitely many solutions to (11), leading to a complex pattern of degeneracies
whose discussion we defer for now.
As already mentioned, the case j = 0 is a bit diﬀerent. There is no pseudomomentum in this case, but
representations are still characterized by a parameter other thanj, specifying now the weight of non-contractible
loops. (For obvious topological reasons, non-contractible loops are not possible for j >0.) Upon parametrizing
this weight as z +z−1, the corresponding standard module of Ta
N(m) is denoted W0,z2. Note that this module
is isomorphic to W0,z−2. With the identiﬁcation z =eiφ/2, the resonance criterion (11) still applies to the case
j = 0.
It is physically well-motivated to require that z +z−1 = m, meaning that contractible and non-contractible
loops get the same weight. Imposing this leads to the module W0,q2. Notice that this is reducible even for
generic q, as (11) is satisﬁed with j = 0, k = 1. Therefore W0,q2 contains a submodule isomorphic to W1,1, and
taking the quotient W0,q2/W1,1 leads to a simple module for generic q which we denote by W0,q2. This module
is isomorphic to W0,q−2. Its dimension is
¯d0 =
(N
N
2
)
−
( N
N
2 + 1
)
, (13)
which coincides with the general formula (12) for k = 1.
There is a geometrical signiﬁcance of the diﬀerence between W0,q2 and W0,q2. In the latter case, we only
register which sites are connected to which in the diagrams, while in the former one also keeps information of
how the connectivities wind around the periodic direction of the annulus (this ambiguity does not arise when
there are through-lines propagating). The corresponding formal result is the existence of a surjection ψ between
diﬀerent quotients of the Ta
N algebra:
ψ
−−−−→ (14)
The previous deﬁnition of link states as the upper halves of the aﬃne diagrams is also meaningful for j = 0. As
before, the representation W0,q2 requires keeping track of whether each pairwise connection between the sites
on the outer boundary (or top side of the framing rectangle) goes through the periodic boundary condition,
whereas the quotient module W0,q2 omits this information. In either case, it is easy to see that the number of
link states coincides with the dimension ˆd0 or ¯d0, respectively.
3In [29] a slightly diﬀerent criterion is given, involving some extra liberty in the form of certain ± signs. We shall however not
need these signs here.
7
