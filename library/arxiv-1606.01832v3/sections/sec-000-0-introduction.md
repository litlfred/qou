---
doc_id: arxiv-1606.01832v3
doc_title: "FLATNESS AND COMPLETION REVISITED AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-4
source_pdf: 1606.01832v3.pdf
source_sha256: da982c95b9674382
doc_brief: "FLATNESS AND COMPLETION REVISITED AMNON YEKUTIELI — We continue investigating the interaction between ﬂatness and a- adic completion for inﬁnitely generated A-modules."
---
1. a-Adic Systems 4
2. Free Resolutions of a-Adic Systems 7
3. a-Adic Flatness 9
4. Weakly Proregular Ideals 12
5. Modules of Decaying Functions 14
6. The Non-Noetherian Example 18
References 20
0. Introduction
In this paper we continue investigating the interaction between ﬂatness and adic
completion for inﬁnitely generated modules over a commutative ring, that we had
started in [Ye1].
Let A be a commutative ring, and let a be an ideal in it. For each k∈N we
deﬁne the quotient ringAk :=A/ak+1. The collection of rings{Ak}k∈N is an inverse
system, and the a-adic completion of A is the commutative ring ˆA := lim←k Ak.
There is a canonical ring homomorphism A→ˆA.
An a-adic system of A-modules is an inverse system {Mk}k∈N, where each Mk
is an Ak-module, and the induced homomorphisms
Ak⊗Ak+1Mk+1→Mk
Date: 6 September 2017.
Key words and phrases. adic completion, adic system, ﬂat module, noetherian ring, weakly
proregular ideal.
Mathematics Subject Classiﬁcation 2010. Primary 13J10; Secondary 13B35, 13E05, 13C10,
13C11, 13D07.
1
arXiv:1606.01832v3  [math.AC]  6 Sep 2017
2 AMNON YEKUTIELI
are all bijective. The limit of the system is the A-module ˆM := lim←k Mk.
Given an A-module M, we let Mk := Ak⊗AM. The collection of A-modules
{Mk}k∈N is an inverse system, that we call the a-adic system induced by M. The
limit ˆM of the induced system is the a-adic completion of M. There is a canonical
A-module homomorphism τM :M→ˆM, and M is called a-adically complete ifτM
is an isomorphism. (Some texts, mostly older ones, would say that M is complete
and separated.)
Our initial motivation was to prove the following theorem, that we consider
important.
Theorem 0.1. If A is a noetherian commutative ring, a is an ideal in A, and M
is a ﬂat A-module, then the a-adic completion ˆM is a ﬂat A-module.
Of course the module M has to be inﬁnitely generated for this statement to be
interesting.
We were under the impression that this was an open question, solved only in
special cases (cf. [En], [BS], [Sct], and [Ye1, Theorems 4.2 and 3.4(2)]). This im-
pression was based on a literature search and email correspondence with several
experts. A few months ago we found a relatively simple proof of this result (it is
now the proof of Theorem 0.6(2) below).
However, after email correspondence with a few more experts, to whom we
showed a preliminary version of this paper, we learned that:
(1) There is already a proof of Theorem 0.1. It is [SP, Lemma 0AGW], pre-
sumably due to de Jong, from around 2013.
(2) There is an elementary proof of Theorem 0.1, indicated to us by Gabber
and Ramero, along the lines of [GR, Lemma 7.1.6].
Thus we turned our attention to a few theorems of secondary importance, that
are totally new, and to which our methods could be applied. This is the content of
the present paper.
Before going on, let us make several general remarks abouta-adic completion and
a-torsion, that are not widely known. For an A-module M, let us write Λ a(M) :=
ˆM, and let Γ a(M) be the a-torsion submodule of M. So Λ a and Γ a are A-linear
functors from the category ModA of A-modules to itself.
If the ideal a is ﬁnitely generated, then for every A-module M its a-adic com-
pletion ˆM is a-adically complete. Thus the functor Λ a is idempotent, in the sense
that Λ a◦Λ a∼= Λ a. There are counterexamples to this idempotence when the ideal
a is not ﬁnitely generated. See [Ye1, Corollary 3.6 and Example 1.8].
Even when the ring A is noetherian (which of course forces the ideal a to be
ﬁnitely generated), the functor Λ a is not left-exact nor right-exact. It is true that
when A is noetherian, the functor Λ a is exact when restricted to the category
ModfA of ﬁnitely generated A-modules.
The functor Γ a is always right exact and idempotent.
The ﬁrst main result of our paper is on a-adic systems. It is a vast generalization
of the classical case, in which A is noetherian and each Mk is a ﬁnitely generated
Ak-module.
Theorem 0.2. Let A be a commutative ring, let a be a ﬁnitely generated ideal in
A, and let {Mk}k∈N be an a-adic system of A-modules, with limit ˆM. Then :
(1) The A-module ˆM is a-adically complete.
FLATNESS AND COMPLETION REVISITED 3
(2) For every k≥0 the canonical homomorphism Ak⊗AˆM→Mk is bijective.
This theorem is repeated as Theorem 1.8 in Section 1 and proved there. An
immediate consequence of Theorem 0.2 is that when the ideala is ﬁnitely generated,
every a-adic system{Mk}k∈N is induced from a module. See Corollaries 1.10 and
1.11.
Now we turn to ﬂatness. An A-module M is said to be a-adically ﬂat if
TorA
i (N,M ) = 0 for every i> 0 and every a-torsion A-module N. Clearly ﬂatness
implies a-adic ﬂatness.
Here is a useful characterization of a-adically ﬂat modules.
Theorem 0.3. LetA be a commutative ring, let a be an ideal in A, and let M be
an A-module. The following conditions are equivalent :
(i) The A-moduleM is a-adically ﬂat.
(ii) For everyi> 0 andk≥0 the module TorA
i (Ak,M ) vanishes, and Ak⊗AM
is a ﬂat Ak-module.
(iii) For every i> 0 the module TorA
i (A0,M ) vanishes, and A0⊗AM is a ﬂat
A0-module.
This is repeated as Theorem 3.3 in the body of the paper. Observe that there
are no ﬁniteness conditions on A, a or M. The result is similar to [SP, Lemma
051C] – see Remark 3.7 for a comparison. The proof of Theorem 0.3 relies on some
basic properties of the derived tensor product.
Supposea = (a1,...,an) is a ﬁnite sequence of elements inA. The sequence a is
called weakly proregular if it satisﬁes a rather complicated condition, involving the
Koszul complexes associated to powers of a. The deﬁnition is recalled in Section
4. The ideal a is called weakly proregular if it is generated by some weakly proreg-
ular sequence. It is known that when A is noetherian, every ideal in it is weakly
proregular. But there are fairly natural examples of weakly proregular ideals in
non-noetherian rings (see Theorem 6.2 for such an example). It is now understood
(see [PSY1] and [PSY2]) that weak proregularity of the ideal a is a necessary and
suﬃcient condition for the derived functors LΛ a and RΓ a to have “good behavior” .
As the next results show, adic ﬂatness belongs to the “twilight zone” between
the weakly proregular case and the noetherian case. Adic ﬂatness comes up in the
weakly proregular situation:
Theorem 0.4. LetA be a commutative ring, let a be a weakly proregular ideal in
A, and let M be an a-adically ﬂat A-module, with a-adic completion ˆM. Then the
A-module ˆM is a-adically ﬂat.
But then the two notions of ﬂatness merge in the noetherian case:
Theorem 0.5. Let A be a noetherian commutative ring, let a be an ideal in A,
and let ˆM be an a-adically ﬂat a-adically complete A-module. Then ˆM is a ﬂat
A-module.
Theorem 0.4 is repeated as Theorem 4.3 in the body of the paper. The proof
uses derived categories and the MGM equivalence. On the other hand, Theorem 0.5
(repeated as Corollary 5.12), is a consequence of item (2) of the following theorem,
combined with Theorem 0.3.
An a-adic system{Mk}k∈N is called ﬂat if each Mk is a ﬂat Ak-module.
4 AMNON YEKUTIELI
Theorem 0.6. LetA be a commutative ring, let a be an ideal inA, and let{Mk}k∈N
be a ﬂat a-adic system, with limit ˆM.
(1) If the ideal a is weakly proregular, then ˆM is an a-adically ﬂat A-module.
(2) If the ring A is noetherian, then ˆM is a ﬂat A-module.
Parts (1) and (2) of the theorem are repeated as Theorems 5.9 and 5.11 respec-
