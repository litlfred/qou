---
doc_id: arxiv-math-0103228v2
doc_title: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 0103228v2.pdf
source_sha256: 7d66dbbd4b87798f
toc_source: inferred
doc_brief: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002 — Coideal subalgebras of the quantized enveloping algebra ar e sur- veyed, with selected proofs included."
---
arXiv:math/0103228v2  [math.QA]  9 Apr 2002
Coideal Subalgebras and Quantum Symmetric Pairs
Gail Letzter 1
Mathematics Department
Virginia Polytechnic Institute
and State University
Blacksburg, V A 24061
Abstract
Coideal subalgebras of the quantized enveloping algebra ar e sur-
veyed, with selected proofs included. The ﬁrst half of the pa per studies
generators, Harish-Chandra modules, and associated quant um homo-
geneous spaces. The second half discusses various well know n quan-
tum coideal subalgebras and the implications of the abstrac t theory
on these examples. The focus is on the locally ﬁnite part of th e quan-
tized enveloping algebra, analogs of enveloping algebras o f nilpotent
Lie subalgebras, and coideals used to form quantum symmetri c pairs.
The last family of examples is explored in detail. Connectio ns are
made to the construction of quantum symmetric spaces.
The introduction of quantum groups in the early 1980’s has ha d a tremen-
dous inﬂuence on the theory of Hopf algebras. Indeed, quantu m groups pro-
vide a source of new and interesting examples. We shall discu ss the reverse
impact: the theory of quantum groups uses the Hopf structure extensively.
This special structure is often hidden in the classical sett ing, while it is
prominent and fundamental for quantum analogs.
Let g be a semisimple Lie algebra and write G for the corresponding con-
nected, simply connected algebraic group. There are two sta ndard types of
quantum groups associated to g and G. The ﬁrst is the quantized envelop-
ing algebra which is a quantum analog of the enveloping algeb ra of g. The
second is the quantized function algebra which is a quantum a nalog of the
algebra of regular functions on G. We will be focusing on a particular aspect
of the Hopf theory of both types of quantum groups: the study o f (one-sided)
coideal subalgebras.
1supported by NSA grant no. MDA 904-99-1-0033.
AMS subject classiﬁcation 17B37
1
One of the reasons coideal subalgebras are so important in th e study of
quantum groups is that quantum groups do not have “enough” Ho pf subal-
gebras. This shortage of Hopf subalgebras is especially not able for quantized
enveloping algebras. Consider a Lie subalgebra t of the Lie algebra g. The
enveloping algebra U(t) of t is a Hopf subalgebra of U(g). However, upon
passage to the quantum case, Uq(t), even when it is deﬁned, is often not iso-
morphic to a Hopf subalgebra of Uq(g). In many cases, there are subalgebras
ofUq(g) which are not Hopf subalgebras but are still good quantum an alogs
of U(t). Moreover, these subalgebras often turn out to be coideals . For ex-
ample, let g = n− ⊕ h ⊕ n+ be the triangular decomposition of g. There is a
natural subalgebra U + of Uq(g) which is an analog of the subalgebra U(n+)
of U(g). This subalgebra U + is a coideal but is not a Hopf subalgebra of
the quantizing enveloping algebra. Of more interest to us is the ﬁxed Lie
subalgebra gθ corresponding to an involution θ of g. In the classical case,
the symmetric pair gθ, g is used to form symmetric spaces. However, in the
quantum case, Uq(gθ ) does not usually embed inside of Uq(g). Thus it was
initially unclear how to develop the theory of quantum symme tric spaces. In
[K], Koornwinder constructed two-sided coideal analogs of gθ in type A1 and
used them to produce quantum symmetric spaces. More familie s of coideal
analogs were discovered in [N], [NS],[DN], and [L1]. In [L2] , a uniform ap-
proach was developed in the maximally split case using one-s ided coideal
subalgebras of the quantized enveloping algebra. The one-s ided coideal con-
dition turned out to be critical in characterizing these qua ntum analogs of
U(gθ ).
Quantum symmetric spaces were ﬁrst deﬁned using the quantiz ed func-
tion algebra. (See for example [KS, 11.6.3 and 11.6.4].) Koo rnwinder’s work
[K] inspired the development of a quantum symmetric space th eory using
analogs of gθ contained in Uq(g). The axiomatic theory of quantum symmet-
ric spaces (see [Di]) proceeded more rapidly than the discov ery of a general
way to construct examples. Indeed, Dijkhuizen [Di, end of Se ction 3] outlined
the desirable properties that analogs of gθ contained in Uq(g) should have
in order to form “nice” quantum symmetric spaces. As in Koorn winder’s
work [K], one of the key properties is the coideal condition. Another cru-
cial property of an analog is that its ﬁnite-dimensional sph erical modules be
characterized in a similar way to the characterization in th e classical case.
This is obtained in [L3] for the coideal subalgebras of [L2]. The proof uses
quantum Harish-Chandra modules associated to quantum symm etric pairs.
2
The coideal condition plays a prominent role in deﬁning and d eveloping the
theory of quantum Harish-Chandra modules ([L3]).
This paper is based on a talk given at the MSRI Hopf Algebra Wor kshop.
It oﬀers a panorama of the use of coideal subalgebras in const ructing quan-
tum symmetric pairs, in forming quantum Harish-Chandra mod ules, and in
producing quantum symmetric spaces. In the ﬁrst half of the p aper, we
present topics in the general theory of quantum coideal suba lgebras. Sec-
tion 1 sets notation and presents some basic facts about coid eal subalgebras
inside arbitrary Hopf algebras. In Section 2, we deﬁne Haris h-Chandra mod-
ules associated to quantum “reductive” pairs. We prove a bas ic result: every
Uq(g) module contains a large Harish-Chandra module associated to a quan-
tum reductive pair. In Section 3, we discuss how coideal suba lgebras of the
quantized enveloping algebra can be used in the dual quantum function al-
gebra setting. Connections are made to the theory of quantum homogeneous
spaces. Section 4 studies ﬁltrations on the quantized envel oping algebra and
their impact on coideal subalgebras. As a result, we obtain a nice description
of the generators of a coideal subalgebra under mild restric tions.
The ﬁnal three sections are devoted to speciﬁc coideal subal gebras of
the quantized enveloping algebra. Section 5 discusses the l ocally ﬁnite part,
F (U), of Uq(g). It is well known that the classical enveloping algebra U(g)
can be written as a direct sum of ﬁnite-dimensional ad g modules. This result
plays an important role in understanding the structure of U(g) and classifying
its primitive ideals. Unfortunately, the quantized envelo ping algebra contains
inﬁnite dimensional Uq(g) modules with respect to the adjoint action. Thus
it is often necessary to use the locally ﬁnite part, F (U), which is the maximal
subalgebra of Uq(g) that can be written as a direct sum of ﬁnite-dimensional
simple ad Uq(g) modules. This algebra F (U) is not a Hopf subalgebra of
Uq(g), but it is a coideal. The structure of this coideal subalgeb ra is brieﬂy
reviewed with some consideration for the implications of th e results of Sec-
tion 4. Certain quantum Harish-Chandra modules deﬁned orig inally in [JL3]
usingF (U) are elucidated in terms of the general approach presented i n Sec-
tion 2. Section 6 considers coideal subalgebra analogs of en veloping algebras
of nilpotent and parabolic Lie subalgebras of g. Much of the material in this
section is based on [Ke]. The last part, Section 7, is devoted to the theory
of quantum symmetric pairs. This material is largely drawn f rom [L2] and
[L3]. However, since the papers appeared, we have found simp ler approaches
which are presented here with many proofs included. We show h ow to lift a
3
maximally split involution θ of g to the quantum setting. Exploiting this lift,
we deﬁne a coideal subalgebra Bθ of Uq(g). As in [L2], Bθ is characterized
as the “unique” maximal coideal subalgebra of Uq(gθ ) which specializes to
U(gθ ) as q goes to 1. Using the results of Section 4, we give a new proof of
this uniqueness theorem which does not involve the intricat e specialization
arguments found in [L2]. We also take the opportunity to make some correc-
tions in the case work necessary to make the uniqueness tight . Results on the
Harish-Chandra module and quantum symmetric space theory a ssociated to
these pairs are described.
Acknowledgement. Part of this paper was written while the author spent
a month as a visiting professor at the University of Rheims. T he author
would like to thank the mathematics department there for the ir hospitality
and J. Alev for his valuable comments. The author would also l ike to thank
the referee for a painstakingly careful reading of the ﬁrst d raft and many
useful suggestions. Finally, the author would like to thank Dan Farkas whose
support transcends multiple revisions.
