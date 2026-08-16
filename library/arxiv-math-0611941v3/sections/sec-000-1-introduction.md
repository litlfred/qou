---
doc_id: arxiv-math-0611941v3
doc_title: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 0611941v3.pdf
source_sha256: bf6f2d55c7adee51
doc_brief: "HECKE ALGEBRAS OF FINITE TYPE ARE CELLULAR MEINOLF GECK — Let H be the one-parameter Hecke algebra associated to a ﬁnite Weyl gr oup W , deﬁned over a ground ring in which “bad” primes for W are"
---
The concept of “cellular algebras” was introduced by Graham and Le hrer [16]. It provides
a systematic framework for studying the representation theory of non-semisimple algebras
which are deformations of semisimple ones. The original deﬁnition was modeled on properties
of the Kazhdan–Lusztig basis [22] in Hecke algebras of type An. There is now a signiﬁcant
literature on the subject, and many classes of algebras have been shown to admit a “cellular”
structure, including Ariki-Koiki algebras, q-Schur algebras, Temperley–Lieb algebras, and a
variety of other algebras with geometric connections; see, e.g., [16 ], [17], [3], [1] and the
references there. However, the question of whether all Hecke a lgebras of ﬁnite type (i.e.,
the originally motivating examples) are cellular remained open. A positiv e answer to this
question would provide a general theory of “Specht modules” which so far has only been
established in types An, Bn (see [2], [27], [4], [16]) and, with some restrictions on the ground
ring, in type Dn with n odd (see [28], [20]). In these cases, the constructions heavily rely o n
the underlying combinatorics of Young tableaux.
The purpose of this paper is to solve this problem in general. We prove :
Theorem 1.1. Let H be the one-parameter Hecke algebra associated with a ﬁnite W eyl
group W , deﬁned over an integral domain in which all “bad” primes for W are invertible.
Then H admits a natural “cellular” structure, where the elements i n the “cellular basis” are
integral linear combinations of Kazhdan–Lusztig basis ele ments Cw with constant value a(w)
(Lusztig’s a-function [24]).
If we apply this in type An, the linear combinations will have only one non-zero term and
we recover the Kazhdan–Lusztig basis in this case. In type Bn, we obtain a cellular structure
which is diﬀerent from the one by Dipper–James–Murphy [4] or Graha m–Lehrer [16]. Our
construction works in the general setting of multi-parameter Hec ke algebras, assuming that
Date: March, 2007.
1
2 MEINOLF GECK
Lusztig’s conjectures on Hecke algebras with unequal parameter s in [25, Chapter 14] hold.
We can also formulate a similar result for Hecke algebras associated t o non-crystallographic
ﬁnite Coxeter groups W ; some additional care is needed since Q is not a splitting ﬁeld for
such a group W .
Thus, if “bad” primes are invertible in the ground ring, then all Hecke algebras of ﬁnite type
are “cellular”. The general theory of cellular algebras then produc es “cell representations”
and a natural parametrisation of the irreducible representations for non-semisimple versions
of H, in terms of properties of certain bilinear forms on the cell represe ntations; see [16, §3].
We show that this parametrization is precisely given by the “canonica l basic sets” introduced
by Rouquier and the author [7], [15], [11].
This paper is organised as follows. In Section 2 we recall the fundame ntal facts from
Kazhdan–Lusztig theory, including Lusztig’s construction of the “ asymptotic ring” J. We
also establish a basic result about the representations of J in Proposition 2.6. In Section 3,
we prove Theorem 1.1 and brieﬂy discuss non-crystallographic Coxe ter groups in Remark 3.3.
The cellular basis that we construct turns out to be unique up to inte gral equivalence of the
representations of J. Finally, in Section 4, we consider examples and discuss the application s
to non-semisimple specialisations. For types An and Bn, we explain the relation of our cellular
bases with the previously known ones.
