---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
The aim of this paper is to connect the theory of quantum Marko v semi-groups to certain coho-
mological properties of their algebras. Quantum Markov sem i-groups are continuous semi-groups of
trace preserving unital completely positive maps on a ﬁnite von Neumann algebra. Such quantum
Markov semi-groups naturally arise in time evolutions of op en systems that undergo decoherence.
With the emergence of non-commutative probability, their t heory had been investigated thoroughly.
We refer in particular to the papers of Goldstein-Lindsay [G oLi95] and Cipriani [Cip97].
A result that is of fundamental importance to us was obtained by Cipriani and Sauvageot in
[CiSa03]. They showed that any generator ∆ of a quantum Marko v semi-group ( e−t∆ )t≥0 admits a
closable derivation ∂ as its square root, i.e. ∆ = ∂∗∂. Since derivations are 1-cocycles in Hochschild
cohomology, this is the ﬁrst instance that shows relevance o f quantum Markov semi-groups to
cohomology.
The results from [CiSa03] had several consequences in non-c ommutative potential theory and
quantum probability. Much more recently also links to appro ximation and rigidity properties of
von Neumann algebras were made. In particular, amenability [CiSa17] and Haagerup property
[CaSk15] can be characterized in terms of quantum Markov sem i-groups with suﬃcient decay (see
also [Cas18, Appendix]). Further rigidity properties of vo n Neumann algebras can be obtained
[Cas18] by using quantum Markov semi-groups as input for the machinery developed by Ozawa-
Popa [OzPo10a], [OzPo10b] and Peterson [Pet09]. A crucial t ool here is the gradient form (or carr´ e
du champ) of a quantum Markov semi-group (or classically a di ﬀusion semi-group)
We describe these rigidity results a bit further. In the cele brated paper [Voi96] Voiculescu
showed, using free entropy, that free group factors do not po ssess a Cartan subalgebra. Later on,
using completely diﬀerent methods, Ozawa and Popa [OzPo10a] re-obtained this result. Ozawa
and Popa in fact prove a stronger result. Namely, they show th at the normalizer of any amenable
diﬀuse von Neumann subalgebra generates a von Neumann algebr a that is amenable again. This
property became known as strong solidity and plays a central role in the theory. Strong solidity
Date: February 14, 2020.
1
2 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
results are usually proved from a combination of weak compac tness and a malleable deformation
or a group geometric/cohomological property.
In particular, the rigidity results of [OzPo10b], [Pet09] s how that proper 1-cocycles in group
cohomology with values in the coarse bimodule (or any bimodu le weakly contained in it) can
be used to show that von Neumann algebras are strongly solid. After [OzPo10b], [Pet09] these
results were improved upon in [ChSi13], [PoVa14] and [Iso15 ], where it was shown that also the
Akemann-Ostrand property, which in the case of a group von Ne umann algebra compares to quasi-
cocycles in bounded (group) cohomology, can be used to get st rong solidity results and further
prime factorization results [OzPo04].
In the current paper we address the question whether also der ivations in Hochschild cohomology
can be used to obtain (quasi-)cohomological properties lik e the Akemann-Ostrand property. We
do this as follows. Fix a ﬁnite von Neumann algebra M with a quantum Markov semi-group
on it having a dense ∗-algebraA in the domain of its generator. We ﬁrst show that we can
construct natural n-cocycles in the Hochschild cohomology of A. The case n = 1 reduces to the
work of Cipriani-Sauvageot mentioned above [CiSa03]. The n-cocycles are deﬁned inductively and
in each inductive step their coeﬃcient bimodule changes by a construction which we refer to as
the ‘gradient tensor product’. Say that the n-cocycles take values in the n-fold gradient tensor
L2(M )∇(n) (we omit the construction here in the introduction). We then analyze when L2(M )∇(n)
is quasi-contained in the coarse bimodule; meaning that it i s contained as a bimodule in an inﬁnite
direct sum of copies of the coarse bimodule. In order to do thi s we introduce the notion of gradient-
Sp for a quantum Markov semi-group and prove the following.
Theorem A. If a quantum Markov semi-group is gradient- S2n then L2(M )∇(n) is quasi-contained
in the coarse bimodule of M .
So essentially under gradient-S2n the cohomology takes place in the coeﬃcient bimodule given
by the coarse bimodule. Note that gradient- S2n becomes weaker for higher n. We illustrate this
for q-Gaussians algebras introduced by Bo˙ zejko and Speicher [B oSp91], see also [BKS97].
Theorem B. For|q| < dim(HR)−1/p we have that the Ornstein-Uhlenbeck semi-group on the
q-Gaussian algebra Γ q(HR) is gradient-Sp.
The importance of Theorems A and B is so far mostly witnessed i n the case n = 1. In fact, in
Theorem 4.1 we show that the cohomology of the ∗-algebras associated with q-Gaussians vanishes
for n≥ 2 so that the cocycles we construct are in fact coboundaries. For n = 1 we show that
Theorem B can be used to obtain further results that serve as i n input for the machinery developed
in [PoVa14] and [Iso15]. We give suﬃcient conditions on a der ivation to imply the Akemann-
Ostrand property. We analyze these conditions in the case of group algebras but also many other
algebras by assuming that the quantum Markov semi-group has a type of ﬁltration (or is radial in
some sense). In many known natural examples these condtions are veriﬁed, see the end of Section
5. As a culminating result we single out the following.
Theorem C. For|q| ⩽ dim(HR)−1/ 2 the q-Gaussian algebra Γ q(HR) satisﬁes the Akemann-Ostrand
property; more precisely condtion AO + from [Iso15].
In [Shl04] Shlyakhtenko obtained the same result for |q| <
√
2− 1 using that the q-Toeplitz
algebra is nuclear in this range. In fact the q-Toeplitz algebras are isomorphic within this range
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 3
[DyNi93] and nuclearity for
√
2− 1 ⩽ |q| < 1 is still an open problem. Theorem C thus strictly
extends the known range of q for which Γ q(HR) has AO + for dimension up until 5.
The outline of this paper is as follows. After the preliminar ies we introduce the gradient tensor
construction in Section 3. We analyze when a repeated tensor product is contained in the coarse
bimodule through the notion of being gradient- Sp (Theorem A). We also show that in the group
case, under a domain condition, one may always average quant um Markov semi-groups to a semi-
group of Fourier multipliers retaining the gradient Sp-properties. In Section 4 we illustrate this
using q-Gaussians and we show that the Ornstein-Uhlenbeck semi-gr oup is gradient-Sp for|q| <
dim(HR)−1/p (Theorem B). Section 5 is then concerned with the question of which derivations
imply condition AO +. We give suﬃcient conditions for the Cipriani-Sauvageot de rivations [CiSa03];
amongst many other examples this includes q-Gaussians and we conclude Theorem C.
Acknowledgements. The authors thank Ebrahim Samei for useful discussions and A dam Skalski
for sharing a short proof of Lemma 3.13. The authors thank the referees for several comments that
led to an improvement of the manuscript. Research of MW was pa rtially supported by National
Science Centre (NCN) grant 2016/21/N/ST1/02499, long term structural funding – Methusalem
grant of the Flemish Government – and by European Research Co uncil Consolidator Grant 614195
RIGIDITY. Parts of this work were completed during a visit of MW to TU Delft; he thanks the
university and the host for a stimulating research environm ent.
