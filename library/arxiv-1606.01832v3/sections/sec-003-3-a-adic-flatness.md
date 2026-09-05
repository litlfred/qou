---
doc_id: arxiv-1606.01832v3
doc_title: "FLATNESS AND COMPLETION REVISITED AMNON YEKUTIELI"
section_id: sec-003-3-a-adic-flatness
section_title: "a-Adic Flatness"
section_number: 3
pages: 9-12
source_pdf: 1606.01832v3.pdf
source_sha256: da982c95b9674382
doc_brief: "FLATNESS AND COMPLETION REVISITED AMNON YEKUTIELI — We continue investigating the interaction between ﬂatness and a- adic completion for inﬁnitely generated A-modules."
---
In this section we prove Theorem 3.3, that characterizes adically ﬂat modules.
As before, A is a commutative ring and a is an ideal in it. We denote by D(A) =
D(ModA) the unbounded derived category of A.
Let us ﬁrst recall the notion of a-torsion. An element m in an A-module M
is called an a-torsion element if m is annihilated by some power of the ideal a.
The a-torsion submodule Γ a(M) of M is the submodule consisting of all a-torsion
elements. Thus
(3.1) Γ a(M) = lim
k→
HomA(Ak,M ),
where Ak = A/ak+1 as before. The module M is called an a-torsion module if
Γ a(M) =M.
It might be good to mention that if the ideal a is nilpotent, then all A-modules
are both a-torsion and a-adically complete. Thus the discussion is only interesting
when the ideal a is not nilpotent.
Deﬁnition 3.2. Let A be a commutative ring, let a be an ideal in A, and let M
be an A-module. We say that M is a-adically ﬂat if TorA
i (N,M ) = 0 for every
a-torsion A-module N and every i> 0.
Here is a useful characterization of adic ﬂatness. It holds in general – no ﬁniteness
or completeness assumptions are needed on A, a or M.
10 AMNON YEKUTIELI
Theorem 3.3. LetA be a commutative ring, let a be an ideal in A, and let M be
an A-module. The following three conditions are equivalent :
(i) The A-moduleM is a-adically ﬂat.
(ii) For everyi> 0 andk≥0 the module TorA
i (Ak,M ) vanishes, and Ak⊗AM
is a ﬂat Ak-module.
(iii) For every i> 0 the module TorA
i (A0,M ) vanishes, and A0⊗AM is a ﬂat
A0-module.
Proof. In terms of derived functors we have
TorA
i (N,M ) = H−i(N⊗L
AM)
asA-modules. Thus M is a-adically ﬂat if and only if for every a-torsionA-module
N, and everyi> 0, we have H−i(N⊗L
AM) = 0. This is equivalent to the condition
that the canonical morphism
N⊗L
AM→N⊗AM
in D(A) is an isomorphism. Let us write Mk :=Ak⊗AM.
(i)⇒(ii): Since Ak itself is an a-torsion A-module, the modules Tor A
i (Ak,M )
vanish for i> 0. Thus there is an isomorphism Mk∼=Ak⊗L
AM in D(Ak).
It remains to prove that Mk is ﬂat over Ak. Take some Ak-module N. By the
associativity of derived tensor products we have isomorphisms
N⊗L
Ak Mk∼=N⊗L
Ak Ak⊗L
AM∼=N⊗L
AM
in D(Ak). But N is an a-torsion module, so by our assumption we have
H−i(N⊗L
AM) = 0 for all i> 0. Therefore H−i(N⊗L
Ak Mk) = 0 for all i> 0.
(ii)⇒(i): Since for every i the functor Tor A
i (−,M ) commutes with arbitrary
direct limits, it suﬃces to check the vanishing of Tor A
i (N,M ) = 0 when N is a
ﬁnitely generated a-torsion A-module. But then N is an Ak-module for some k.
By assumption Mk is ﬂat over Ak, and Ak⊗L
AM∼= Mk in D(A). Then there are
isomorphisms
N⊗L
AM∼=N⊗L
Ak Ak⊗L
AM∼=N⊗L
Ak Mk∼=N⊗Ak Mk
in D(A). It follows that H−i(N⊗AM) = 0 for all i> 0.
(ii)⇒(iii): This is trivial.
(iii)⇒(ii): We will use induction on k: assuming that (ii) holds for k, we will
prove it for k + 1. For k = 0 this is given.
Let N be an Ak+1-module. Deﬁne N′:= a·N⊆N and N′′:= N/N′. We get
an exact sequence
0→N′→N→N′′→0
of Ak+1-modules, that we view as a distinguished triangle
(3.4) N′→N→N′′∆
− →
in D(A). Now the modules N′and N′′are annihilated by ak+1, so they are in
fact Ak-modules. By our assumption Ak⊗L
AM∼= Mk in D(Ak), and Mk is a ﬂat
Ak-module. So we have isomorphisms
(3.5) N′⊗L
AM∼=N′⊗L
Ak Ak⊗L
AM∼=N′⊗L
Ak Mk∼=N′⊗Ak Mk
FLATNESS AND COMPLETION REVISITED 11
in D(Ak). The same for N′′. Thus, upon application of the functor −⊗L
AM to the
distinguished triangle (3.4), we obtain the distinguished triangle
(3.6) N′⊗Ak Mk→N⊗L
AM→N′′⊗Ak Mk
∆
− →
in D(A). We conclude that H −i(N⊗L
AM) = 0 for all i > 0. In particular, tak-
ing N = Ak+1, this tells us that H −i(Ak+1⊗L
A M) = 0 for all i > 0, and that
Ak+1⊗L
AM∼=Mk+1 in D(Ak+1).
It remains to prove that Mk+1 is ﬂat over Ak+1. Again we take an arbitrary
Ak+1-module N, and examine the distinguished triangle (3.4), but now it is in
the category D(Ak+1). Using the isomorphisms from (3.5) we obtain these isomor-
phisms
N′⊗L
Ak+1Mk+1∼=N′⊗L
Ak+1Ak+1⊗L
AM∼=N′⊗L
AM∼=N′⊗Ak Mk
in D(Ak+1). The same for N′′. Therefore, when we apply the functor−⊗L
Ak+1Mk+1
to (3.4), we obtain the distinguished triangle
N′⊗Ak Mk→N⊗L
Ak+1Mk+1→N′′⊗Ak Mk
∆
− →
D(Ak+1). We see that H−i(N⊗L
Ak+1Mk+1) = 0 for all i> 0. □
Remark 3.7. Theorem 3.3 is similar to [SP, Lemma 051C]. The latter says that if
TorA
1 (A0,M ) = 0 and M0 is ﬂat over A0, then Mk is ﬂat over Ak for all k, and
TorA
1 (N,M ) = 0 for every a-torsion A-module N. It seems that this condition on
M is strictly weaker than being a-adically ﬂat; but we did not look for an example
demonstrating this.
Proposition 3.8. LetA be a commutative ring, let a be an ideal in A, and let M
be an a-adically ﬂat A-module. Then the canonical morphism LΛ a(M)→Λ a(M)
in D(A) is an isomorphism.
Proof. Let
(3.9) ···P−1→P 0 η
− →M→0
be a ﬂat resolution of the module M. We can view this as a quasi-isomorphism of
complexes η: P→M. Then the completion Λ a(η) : Λ a(P )→Λ a(M) represents
the canonical morphism LΛ a(M)→Λ a(M). We are going to prove that Λ a(η) is a
quasi-isomorphism.
For everyk∈N, applying Ak⊗A−to (3.9), there is a sequence
(3.10) ···Ak⊗AP−1→Ak⊗AP 0 ηk
−→Ak⊗AM→0.
The complex Ak⊗AP represents Ak⊗L
AM. Because M is a-adically ﬂat, we see
that H−i(Ak⊗A P ) = 0 for all i > 0. Therefore the sequence (3.10) is exact.
The Mittag-Leﬄer argument (see [KS, Proposition 1.12.4]) says that the inverse
limit of the sequences (3.10) is also exact. But then Λ a(η) : Λ a(P )→Λ a(M) is a
quasi-isomorphism. □
Remark 3.11. Let a be a ﬁnitely generated ideal in a commutative ring A. Our
a-adically ﬂat modules are very close to the ﬂat contramodules that were introduced
in [Po1], [PoRo]. According to Positselski, anA-moduleM is called a contramodule
if it is a-adically cohomologically complete in the sense of [PSY1], namely if the
canonical morphismM→LΛ a(M) in D(A) is an isomorphism. A contramodule M
12 AMNON YEKUTIELI
is called a ﬂat contramodule if each Mk :=Ak⊗AM is a ﬂat Ak-module. Thus, by
our Theorem 0.6(1) and Proposition 3.8, if M is an a-adically complete A-module
and the ideal a is weakly proregular, then M is an a-adically ﬂat module iﬀ it is a
ﬂat contramodule. We thank L. Positselski for mentioning this to us.
Remark 3.12. Let a be a ﬁnitely generated ideal in a commutative ring A. De-
note by Moda-torA the subcategory of a-torsion modules. Let M be an a-adically
complete A-module. It is easy to see that if M is a-adically ﬂat, then M is ﬂat
relative to the subcategory Moda-torA, i.e. the functor
(3.13) M⊗A−: Moda-torA→Moda-torA
is exact. The converse is true if the ideal a is weakly proregular, by Theorem 0.6(1).
But what if a is not weakly proregular?
Surprisingly, the converse does not hold without weak proregularity. Here is the
precise statement, communicated to us privately by Positselski (and can be proved
using ideas in his paper [Po2]). LetP be the a-adic completion of the freeA-module
of countable rank; so in the notation of Section 5 we have P = Fdec(N, ˆA). Since
Ak⊗AP is a free Ak-module (cf. Proposition 5.2), it follows that the A-module P
is ﬂat relative to the subcategory Moda-torA. However, Positselski claims that if
the A-moduleP is a-adically ﬂat, then the ideal a is weakly proregular.
