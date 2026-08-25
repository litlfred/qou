---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-150-introduction
section_title: "Introduction"
section_number: null
pages: 287-289
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
One of the most prevalent questions in the representation theory of ﬁnite groups is to determine what
relationships hold between the set Irr(G) of irreducible complex characters of a ﬁnite group G and its
local structure, such as the structure of a Sylow p-subgroup P of G. There is, of course, the more
sophisticated question of relating the set Irr(B) of irreducible characters belonging to a given Brauer
p-block B of G with the structure of a defect group D of B.
G. Navarro and P. H. Tiep [2019] conjecture that for a prime p, one can determine the exponent of the
abelianization of P in terms of the action of certain Galois automorphisms on Irr(G). To be more precise,
for a ﬁxed prime p and an integer e≥ 1, letσe∈ Gal(Qab/Q)= G be such thatσe ﬁxes p′-roots of unity
and sends any root of unity of order a power of p to its(pe+1)-st power. In [Navarro and Tiep 2019] it is
proven that the exponent of P/P′ is less than or equal to pe whenever all of the irreducible characters of
p′-degree of G areσe-ﬁxed, and the converse is reduced to a question on ﬁnite simple groups. (Thanks to
Malle [2019] we know that the converse holds for p= 2.)
In the present work, we show that one can determine whether P is cyclic (for small primes) by just
counting the number of certain σ1-invariant elements of Irr(B0), where B0 is the principal p-block of G.
This is the main result of our paper.
This material is based upon work supported by the National Security Agency under Grant No. H98230-19-1-0119, The Lyda
Hill Foundation, The McGovern Foundation, and Microsoft Research, while the authors were in residence at the Mathematical
Sciences Research Institute in Berkeley, California, during the summer of 2019. Rizo and Vallejo acknowledge support by
Ministerio de Ciencia e Innovación PID2019-103854GB-I00 and FEDER funds. Vallejo further acknowledges support from the
Ministerio de Ciencia e Innovación, through the “Severo Ochoa Programme for Centres of Excellence in R&D” (SEV-2015-0554)
and from the Spanish National Research Council, through the “Ayuda extraordinaria a Centros de Excelencia Severo Ochoa”
(20205CEX001). Schaeffer Fry acknowledges support from the National Science Foundation under Grant No. DMS-1801156.
MSC2010: primary 20C15; secondary 20C20, 20C33.
Keywords: principal p-block, Galois action on characters, cyclic Sylow p-subgroups, Alperin–McKay–Navarro Conjecture.
1953
1954 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
Theorem A. Let G be a ﬁnite group of order divisible by p, where p∈{ 2, 3}. Let P∈ Sylp(G) and let
B0 be the principal p-block of G. Then
|Irrp′(B0)σ1|= p if, and only if, P is cyclic ,
where Irrp′(B0)σ1 is the set of irreducible characters in B0 with degree relatively prime to p that are ﬁxed
under the action ofσ1.
With the deﬁnition above,σ1 is an element of the subgroup H≤ G consisting of allσ∈ G for which
there exists some integer f such thatσ(ξ)=ξ p f
wheneverξ is a root of unity of order not divisible by p.
Navarro predicted [2004, Conjecture A] the existence of bijections for the McKay conjecture commuting
with the action of H on characters. This is the celebrated McKay–Navarro conjecture (sometimes also
referred to as the Galois–McKay conjecture), which has been recently reduced to a question on ﬁnite
simple groups in [Navarro et al. 2019]. The McKay–Navarro conjecture admits a blockwise version
[Navarro 2004, Conjecture B], which remains unreduced at the present moment and which we will refer
to as the Alperin–McKay–Navarro conjecture, as it can also be seen as a reﬁned version of the celebrated
Alperin–McKay conjecture. In this context, it is natural to wonder the extent to which Theorem A holds
for arbitrary blocks. We propose the following.
Conjecture B. Let p∈{ 2, 3}. Let G be a ﬁnite group and let B be a p-block of G with nontrivial defect
group D. Then
|Irr0(B)σ1|= p if, and only if, D is cyclic ,
where Irr0(B)σ1 is the set of height zero irreducible characters in the block B that are ﬁxed under the
action ofσ1.
We prove that Conjecture B follows from the Alperin–McKay–Navarro conjecture. In this sense,
Theorem A provides more evidence of the elusive Alperin–McKay–Navarro conjecture. Since the latter
holds whenever D is cyclic, by work of Navarro [2004], it follows that the “if” direction of Conjecture B
(and of Theorem A) holds. For many consequences of the (Alperin–)McKay–Navarro conjecture, the state-
ments take different forms depending on the prime (see, for instance, [Navarro et al. 2007; Schaeffer Fry
2019]). This might well be the case here, however, we are not yet aware of such a statement for p> 3.
To prove Theorem A, we use the classiﬁcation of ﬁnite simple groups. In particular, we contribute to
the problem of understanding Galois action on the characters in blocks of nonabelian simple groups in
the following way.
Theorem C. Let S be a nonabelian simple group of order divisible by p≤ 3, P∈ Sylp(S) and X∈
Sylp(Aut(S)). Let B 0 be the principal p-block of S.
(a) If P is cyclic , then p= 3 and Irrp′(B0)σ1={ 1S,φ 1,φ 2}, where the φi are nontrivial and not
Aut(S)-conjugate, and someφi is X-invariant.
(b) If P is not cyclic , then Irrp′(B0)σ1⊇{ 1S,φ 1,...,φ p}, where the nontrivial φi are pairwise not
Aut(S)-conjugate, and someφi is X-invariant.
Galois action on the principal block and cyclic Sylow subgroups 1955
This paper is structured as follows. In Section 1 we prove that Conjecture B follows from the Alperin–
McKay–Navarro conjecture. To do so, we study the action of σ1 on the irreducible characters of blocks
with normal defect group. The rest of the paper is devoted to proving Theorem A. In Section 2, we reduce
Theorem A to statements on ﬁnite simple groups, and in Section 3 we prove Theorem C thus completing
the proof of Theorem A.
