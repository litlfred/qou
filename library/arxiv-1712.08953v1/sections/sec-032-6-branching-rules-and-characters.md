---
doc_id: arxiv-1712.08953v1
doc_title: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY"
section_id: sec-032-6-branching-rules-and-characters
section_title: "Branching rules and characters"
section_number: 6
pages: 36-46
source_pdf: 1712.08953v1.pdf
source_sha256: 005e0b1ad63c173e
doc_brief: "REPRESENTATIONS OF THE ORIENTED SKEIN CATEGORY — The oriented skein category OS(z, t ) is a ribbon category which un- derpins the deﬁnition of the HOMFLY-PT invariant of an orien ted link, in the"
---
We continue with the setup of the previous section. In this section, we introduce a
biadjoint pair of endofunctors E andF of Mod-OS, which lift the endofunctors↑⊗? and
↓⊗? ofOS (z,t ). We will use the Jucys-Murphy elements from section 4 to decompo se
these endofunctors into direct sums of reﬁned functors Ei and Fi, which we study by
comparing them to some well-known induction and restriction functo rs on Mod-OS◦.
To start with, let us recall some standard facts about induction an d restriction for
the Iwahori-Hecke algebra Hr. Let
indr
r−1 : Mod-Hr−1→ Mod-Hr, resr
r−1 : Mod-Hr→ Mod-Hr−1 (6.1)
be the usual induction and restriction functors with respect to th e natural embedding
Hr−1֒→Hr,Si↦→Si. So ind r
r−1 is deﬁned by tensoring over Hr−1 with Hr viewed as
an (Hr−1,Hr)-bimodule and resr
r−1 is deﬁned by tensoring over Hr withHr viewed as
an (Hr,Hr−1)-bimodule; equivalently, resr
r−1 is the functor HomHr (Hr, ?). Adjointness
of tensor and hom implies that induction is left adjoint to the restrict ion functor resr
r−1.
It is also right adjoint; cf. [DJ1, Theorem 2.6]. The Jucys-Murphy element
Lr :=Sr−1··· S2S1S1S2··· Sr−1∈Hr (6.2)
centralizesHr−1, so left multiplication by it deﬁnes an endomorphism of the (Hr−1,Hr)-
bimoduleHr. For any i∈ k , leti-indr
r−1 be thei-induction functor deﬁned by tensoring
with the summand of this bimodule that arises as the generalized i-eigenspace of this
endomorphism. Let i-resr
r−1 be the biadjointi-restriction functor; explicitly,i-resr
r−1M
may be realized as the generalized i-eigenspace of Lr on resr
r−1M .
The following “classical” branching rules 3 describe the eﬀect of these functors on the
Specht module S λ. In formulating the result, we identify partition λ with its Young
diagram, that is, the set {(i,j )|i≥ 1, 1≤j≤λr}, and deﬁne the content of the node
3Probably the best way to prove them is by applying the “Schur f unctor” to an analogous result for
quantum GLn.
ORIENTED SKEIN CATEGORY 37
A = (i,j )∈ N×N from cont(A) := q2(j−i)∈ k . For example, here is the Young diagram
λ = (5, 3, 2) with its nodes labeled by their contents:
1 q2 q4 q6 q8
q−2 1 q2
q−4 q−2
.
LetI1 be the set of all possible contents of nodes of partitions. More gen erally, for any
c∈ k ×, we let
Ic :={cq2n|n∈ Z}⊆ k ×. (6.3)
Lemma 6.1. The following hold for each i∈ k ×:
(1) For λ⊢ (r− 1), the Hr-module i-indr
r−1 Sλ has a multiplicity-free ﬁltration
with sections Sµ for µ⊢r obtained by adding a node of content i to the Young
diagram of λ.
(2) For λ⊢ r, the Hr-module i-resr
r−1 Sλ has multiplicity-free ﬁltration with sec-
tions∼= Sµ for µ⊢ (r− 1) obtained by removing a node of content i from the
Young diagram of λ.
In both cases, the ﬁltration should be ordered according to t he usual dominance ordering
on the partitions labelling the sections, most dominant at t he bottom. Hence:
indr
r−1 =
⨁
i∈I1
i-indr
r−1, resr
r−1 =
⨁
i∈I1
i-resr
r−1. (6.4)
The results just explained extend immediately to Hr,s =Hr⊗Hs. For these algebras,
there are two commuting i-induction functors i-indr,s
r−1,s and i-indr,s
r,s−1, deﬁned by
tensoring with the bimodules that arise by taking the generalized i-eigenspaces of the
endomorphisms of Hr,s deﬁned by left multiplication by Lr⊗ 1 or 1⊗Ls, respectively.
The biadjoint i-restriction functors are denoted i-resr,s
r−1,s and i-resr,s
r,s−1. Lemma 6.1
extends in an obvious way to describe the eﬀect of these functors on the modules
Sλ↑⊠ Sλ↓ .
The next step is to use the Morita equivalences from Lemma 5.2 to tra nsport the
branching rules for Hr,s just described to the algebra OS◦. Let
ı◦
↓ :OS◦→OS◦, f ↦→↓⊗f, (6.5)
ı◦
↑ :OS◦→OS◦, f ↦→↑⊗f (6.6)
be the algebra homomorphisms associated to the functors ↓⊗− :OS◦(z,t )→OS◦(z,t )
and↑⊗− :OS◦(z,t )→OS◦(z,t ). These are not locally unital algebra homomorphisms:
they send the idempotent 1 a to 1↑a and to 1↓a, respectively. Then let
↑OS◦ :=
⨁
a,b∈⟨↑,↓⟩
1↑aOS◦1b, OS ◦
↑ :=
⨁
a,b∈⟨↑,↓⟩
1aOS◦1↑b, (6.7)
↓OS◦ :=
⨁
a,b∈⟨↑,↓⟩
1↓aOS◦1b, OS ◦
↓ :=
⨁
a,b∈⟨↑,↓⟩
1aOS◦1↓b, (6.8)
which we view as ( OS◦,OS◦)-bimodules with left and right actions of a,b∈OS◦ onf
deﬁned by a·f·b :=ı◦
↑(a)fb,afı ◦
↑(b),ı◦
↓(a)fb andafı◦
↓(b), respectively. Tensoring with
these bimodules give us four endofunctors of Mod- OS◦:
E↑ :=?⊗OS ◦↑OS◦ : Mod-OS◦→ Mod-OS◦, (6.9)
F↑ :=?⊗OS ◦OS◦
↑ : Mod-OS◦→ Mod-OS◦, (6.10)
38 J. BRUNDAN
F↓ :=?⊗OS ◦↓OS◦ : Mod-OS◦→ Mod-OS◦, (6.11)
E↓ :=?⊗OS ◦OS◦
↓ : Mod-OS◦→ Mod-OS◦. (6.12)
The functors E↑ and F↓ send OS◦
r,s-modules to OS◦
r+1,s- and OS◦
r,s+1-modules, re-
spectively; they will be called induction functors . The functors F↑ andE↓ sendOS◦
r,s-
modules to OS◦
r−1,s- and OS◦
r,s−1-modules, respectively; they will be called restriction
functors. This terminology is justiﬁed by the following lemma.
Lemma 6.2. The following diagrams commute up to natural isomorphisms:
Mod-Hr+1,s
Υ r+1,s
−−−−→ Mod-OS◦
r+1,s
↑indr+1,s
r,s ցα
↑E↑
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s,
Mod-Hr+1,s
Υ r+1,s
−−−−→ Mod-OS◦
r+1,s
↓ resr+1,s
r,s
βր
↓F ↑
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s,
Mod-Hr,s+1
Υ r,s+1
−−−−→ Mod-OS◦
r,s+1
↑indr,s+1
r,s ցγ
↑F ↓
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s,
Mod-Hr,s+1
Υ r,s+1
−−−−→ Mod-OS◦
r,s+1
↓ resr,s+1
r,s
δր
↓E↓
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s.
Hence, the functors E↑ and F↑ are biadjoint, as are the functors E↓ and F↓.
Proof. First we construct the isomorphism α : Υ r+1,s◦ indr+1,s
r,s
∼
→ E↑◦ Υ r,s. The
northwest functor is deﬁned by tensoring over Hr,s with the (Hr,s,OS◦)-bimodule
Hr+1,s⊗Hr+1,s 1↓s↑r+1OS◦∼= 1↓s↑r+1OS◦.
The southeast functor is deﬁned by tensoring with
1↓s↑rOS◦⊗OS ◦↑OS◦∼= 1↑↓s↑rOS◦.
The following gives an isomorphism between these two bimodules:
1↓s↑r+1OS◦ ∼
→ 1↑↓s↑rOS◦,
f
a
s r
↦→
a
s r
f
for any f∈ 1↓s↑r+1OS◦1a. This establishes the existence of α.
To deduce the existence of β, we claim that F↑ is right adjoint to E↑. To see
this, F↑M = M⊗OS ◦ OS◦
↑ = ⨁
a∈⟨↑,↓⟩M 1↑a ∼= ⨁
a∈⟨↑,↓⟩ HomOS ◦ (1↑aOS◦,M ). So,
by adjointness of tensor and hom, F↑ is right adjoint to ⨁
a∈⟨↑,↓⟩?⊗OS ◦ 1↑aOS◦ =
?⊗OS ◦ ↑OS◦ = E↑. Since res r+1,s
r,s is right adjoint to ind r+1,s
r,s , and the horizontal
functors in our diagrams are equivalences of categories, we can no w deduce the existence
of the desired isomorphism β using the previous paragraph and unicity of right adjoints.
The construction of γ is very similar to that of α. In fact, it is even easier since
both of the ( Hr,s,OS◦)-bimodules being considered turn out to be the same bimodule
1↓s+1↑rOS◦, so we can take γ to be induced by the identity map. Then we get δ from
γ as in the previous paragraph. □
Now we need versions of Jucys-Murphy elements for OS◦, which extend the Jucys-
Murphy elements of Hr,s. For ∅ ⁄= b∈⟨↑,↓⟩, deﬁne X◦(b)∈ 1bOS◦1b by setting
ORIENTED SKEIN CATEGORY 39
X◦(↑) := 1↑,X◦(↓) := t−21↓, and then recursively deﬁning
X◦(↑↑b) := X ◦(↑b)
b
b
, X ◦(↑↓b) := X ◦(↑b)
b
b
, (6.13)
X◦(↓↓b) := X ◦(↓b)
b
b
, X ◦(↓↑b) := X ◦(↓b)
b
b
, (6.14)
for any a∈⟨↑,↓⟩; cf. (4.11)–(4.12).
Let ↑X◦ : ↑OS◦ → ↑OS◦ and X◦
↑ : OS◦
↑ → OS◦
↑ be the linear endomorphisms
deﬁned on 1 ↑aOS◦ or OS◦1↑a by left or right multiplication by X◦(↑a), respectively.
Similarly, replacing↑ by↓ everywhere, we deﬁne linear endomorphisms ↓X◦ and X◦
↓
of↓OS◦ and OS◦
↓ .
Lemma 6.3. All of the linear endomorphisms ↑X◦,X◦
↑,↓X◦ and X◦
↓ are (OS◦,OS◦)-
bimodule endomorphisms.
Proof. We just explain the argument for ↑X◦. It is obvious that this deﬁnes a right
OS◦-module homomorphism. To see that it also commutes with the left act ion of OS◦,
it suﬃces to check that it commutes with left multiplication by any eleme nt of OS◦
deﬁned by a crossing of a neighboring pairs of strands (excluding th e leftmost strand).
This quickly reduces by induction to checking the following four identit ies:
X◦(↑↑↑)◦ = ◦X◦(↑↑↑), X ◦(↑↓↓)◦ = ◦X◦(↑↓↓),
X◦(↑↓↑)◦ = ◦X◦(↑↑↓), X ◦(↑↑↓)◦ = ◦X◦(↑↓↑).
These are all straightforward on drawing the diagrams for these X◦’s explicity. □
For i∈ k ×, let E↑
i be the subfunctor of E that is deﬁned by tensoring with the
bimodule that is the generalized i-eigenspace of ↑X◦ :↑OS◦→↑OS◦. Deﬁne F↑
i,F↓
i
and E↓
i similarly using the endomorphisms X◦
↑,↓X◦ and X◦
↓ .
Lemma 6.4. The following diagrams commute up to natural isomorphisms:
Mod-Hr+1,s
Υ r+1,s
−−−−→Mod-OS◦
r+1,s
↑i-indr+1,s
r,s
↑E↑
i
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s,
Mod-Hr+1,s
Υ r+1,s
−−−−→Mod-OS◦
r+1,s
↓i-resr+1,s
r,s
↓F ↑
i
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s,
Mod-Hr,s+1
Υ r,s+1
−−−−→Mod-OS◦
r,s+1
↑t−2i−1-indr,s+1
r,s
↑F ↓
i
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s,
Mod-Hr,s+1
Υ r,s+1
−−−−→Mod-OS◦
r,s+1
↓t−2i−1-resr,s+1
r,s
↓E↓
i
Mod-Hr,s −−−−→
Υ r,s
Mod-OS◦
r,s.
Hence, the functors E↑
i andF↑
i are biadjoint, as are the functors E↓
i andF↓
i . Moreover:
E↑ =
⨁
i∈I1
E↑
i, F ↑ =
⨁
i∈I1
F↑
i, F ↓ =
⨁
i∈It−2
F↓
i, E ↓ =
⨁
i∈It−2
E↓
i. (6.15)
40 J. BRUNDAN
Proof. Consider the ﬁrst diagram. In the proof of Lemma 6.2, the isomorph ism of func-
tors α was induced by an explicit bimodule isomorphism 1 ↓s↑r+1OS◦→ 1↑↓s↑rOS◦.
This isomorphism intertwines the endomorphism of 1 ↓s↑r+1OS◦ deﬁned by left mul-
tiplication by ır+1,s(Lr+1⊗ 1) with the endomorphism of 1 ↑↓s↑rOS◦ deﬁned by left
multiplication by X◦(↑↓s↑r); the appropriate picture needed to see this is as follows:
s r
=
s r
.
Consequently, this bimodule isomorphism restricts to an isomorphism between the
appropriate summands of these bimodules, showing that the restr iction of α gives the
desired natural transformation.
The second diagram follows from the ﬁrst by unicity of adjoints on ob serving that
F↑
i is right adjoint to E↑
i , which follows from the explicit construction of the adjunction
in the second paragraph of the proof of Lemma 6.2.
The third diagram is established in the same way as the ﬁrst diagram. O ne needs
to check that the endomorphisms of 1 ↓s+1↑rOS◦ deﬁned by left multiplication by
t−2ır,s+1(1⊗Ls+1)−1 and by X◦(↓s+1↑r) are equal, which is clear from the follow-
ing picture:
t−2


rs


−1
=t−2
r s
.
The fourth diagram follows by adjunction as before.
The ﬁnal statement of the lemma follows using these diagrams plus fa cts we have
already discussed about the induction and restriction functors fo r Hr,s. □
We assemble the results so far into the following theorem, which desc ribes all of the
branching rules for the functors E↑
i ,F↑
i , F↓
i and E↓
i .
Lemma 6.5. The following hold for i∈ k × and λ∈ Bipr,s.
(1) E↑
i S(λ ) has a multiplicity-free ﬁltration with sections S(µ ) for µ ∈ Bipr+1,s
obtained by adding a node of content i to the Young diagram of λ↑.
(2) F↑
i S(λ ) has a multiplicity-free ﬁltration with sections S(µ ) for µ ∈ Bipr−1,s
obtained by removing a node of content i from the Young diagram of λ↑.
(3) F↓
i S(λ ) has a multiplicity-free ﬁltration with sections S(µ ) for µ ∈ Bipr,s+1
obtained by adding a node of content t−2i−1 to the Young diagram of λ↓.
(4) E↓
i S(λ ) has a multiplicity-free ﬁltration with sections S(µ ) for µ ∈ Bipr,s−1
obtained by removing a node of content t−2i−1 from the Young diagram of λ↓.
In all cases, the ﬁltrations should be ordered according to t he usual dominance ordering
on the partitions labelling the sections, most dominant at t he bottom.
Proof. This follows from Lemmas 6.4 and 6.1. □
Now we turn our attention at last to OS itself. Mimicking the deﬁnitions made above
for OS◦, we write ı↓ : OS→OS and ı↑ : OS→OS for the algebra homomorphisms
associated to the functors ↓⊗− :OS (z,t )→OS (z,t ) and↑⊗− :OS (z,t )→OS (z,t ).
Then let
↑OS :=
⨁
a,b∈⟨↑,↓⟩
1↑aOS1b, OS ↑ :=
⨁
a,b∈⟨↑,↓⟩
1aOS1↑b, (6.16)
↓OS :=
⨁
a,b∈⟨↑,↓⟩
1↓aOS1b, OS ↓ :=
⨁
a,b∈⟨↑,↓⟩
1aOS1↓b, (6.17)
ORIENTED SKEIN CATEGORY 41
which we view as ( OS,OS )-bimodules with left and right actions of a,b ∈ OS on f
deﬁned by a·f·b :=ı↑(a)fb,afı ↑(b),ı↓(a)fb andafı↓(b), respectively. A key diﬀerence
to the situation for OS◦ emerges right away:
Lemma 6.6. We have that OS↑∼=↓OS and OS↓∼=↑OS as (OS,OS )-bimodules.
Proof. The mutually inverse bimodule isomorphisms OS↓→↑OS and↑OS→OS↓ are
deﬁned on diagrams by the maps
f
a
b
↦→ f
a
b
and f
a
b
↦→ f
a
b
,
respectively. The isomorphism OS↑∼=↓OS is constructed similarly. □
This means that we only need to deﬁne two functors:
E :=?⊗OS↑OS ∼= ?⊗OSOS↓ : Mod-OS→ Mod-OS, (6.18)
F :=?⊗OS↓OS ∼= ?⊗OSOS↑ : Mod-OS→ Mod-OS. (6.19)
Note that
E(1aOS) = 1 aOS⊗OS (↑OS) = 1 a(↑OS) = 1↑aOS, (6.20)
and similarly F (1aOS) = 1↓aOS. By adjointness of tensor and hom, the functor E has
a canonical right adjoint
⨁
a∈⟨↑,↓⟩
HomOS (1↑aOS, ?)∼= ?⊗OSOS↑, (6.21)
with the isomorphism here sending f in the ath summand to f (1↑a)⊗ 1↑a. In view of
Lemma 6.6, the functor ? ⊗OS OS↑ on the right hand side of (6.21) is isomorphic to
F . Thus, we see that ( E,F ) is an adjoint pair. Explicitly, the unit Id → FE of this
adjunction is deﬁned by the bimodule homomorphism
OS→↑OS⊗OS↓OS, f
a
b
↦→ f
a
b
⊗
b
, (6.22)
and the counit EF→ Id is deﬁned by
↓OS⊗OS↑OS→OS, f
a
b
⊗ g
b
c
↦→
f
g
c
a
. (6.23)
Reversing the roles of ↑ and↓ in this argument, we get another canonical adjunction
making (F,E ) is an adjoint pair. So E andF are biadjoint, hence, they are exact, and
preserve locally ﬁnite-dimensional, ﬁnitely generated, ﬁnitely cogen erated, projective
and injective objects; cf. [BD, Theorem 2.11].
Recalling (4.10), let ↑X :↑OS→↑OS be the bimodule endomorphism deﬁned on
1↑bOS by left multiplication by X(↑b), and let X↓ :OS↓→OS↓ be deﬁned on 1 bOS↓b
by right multiplication by X(↓b). These are intertwined by the isomorphism from
Lemma 6.6; this depends on (4.4). Similarly, switching ↑ with↓ everywhere, we get
endomorphisms↓X :↓OS→↓OS and X↑ :OS↑→OS↑, which are again intertwined
by the isomorphism from Lemma 6.6.
42 J. BRUNDAN
Lemma 6.7. There are short exact sequence of (OS◦,OS )-bimodules
0−→OS◦
↑⊗OS ♯OS
α
−→OS◦⊗OS ♯ OS↑
β
−→↓OS◦⊗OS ♯ OS−→ 0, (6.24)
0−→OS◦
↓⊗OS ♯OS
α
−→OS◦⊗OS ♯ OS↓
β
−→↑OS◦⊗OS ♯ OS−→ 0. (6.25)
The maps α and β in the ﬁrst sequence satisfy α◦ (X◦
↑⊗ id) = (id ⊗X↑)◦α and
β◦ (id⊗X↑) = ( ↓X◦⊗ id)◦β. The maps in the second sequence have analogous
properties.
Proof. We just go through the details for the ﬁrst short exact sequence . The bimodule
homomorphisms α and β are deﬁned on pure tensors as follows:
α : f
b
a
⊗ g
b
c
↦→f
b
a
⊗ g
b
c
, β : f
b
a
⊗ g
b
c
↦→ f
a
b
⊗ g
b
c
. (6.26)
It is straightforward to see these are well-deﬁned bimodule homomo rphisms. Also
β◦α = 0. Indeed, if we apply β◦α to a pure tensor as above, we produce a pure tensor
of the form f⊗g such that the strand of g starting in the top left corner is a rightward
cup. This cup commutes past the tensor to give zero since we are vie wing↓OS◦ as a
rightOS♯-module by inﬂation.
To show that the sequence is exact, we pick bases. Recall that ⟨↑,↓⟩r,s denotes
words which have exactly r letters↑ and s letters↓. For a, b∈⟨↑,↓⟩r,s, let Aa,b be a
basis for 1 aOS◦1b consisting of reduced lifts of matchings. Similarly, for b∈⟨↑,↓⟩r,s
and c∈⟨↑,↓⟩r+t,s+t for t≥ 0, let Bb,c be a basis for 1 bOS−1c consisting of reduced
lifts of matchings. By Lemma 5.1, we see that
P :=
{
f⊗g
⏐⏐⏐⏐
f∈Aa,↑b,g∈Bb,c for r,s,t ≥ 0 and
a∈⟨↑,↓⟩r+1,s, b∈⟨↑,↓⟩r,s, c∈⟨↑,↓⟩r+t,s+t,
}
,
Q :=
{
f⊗g
⏐⏐⏐⏐
f∈Aa,b,g∈Bb,↑c for r,s,t ≥ 0 with s +t≥ 1 and
a, b∈⟨↑,↓⟩r,s, c∈⟨↑,↓⟩r+t,s+t−1,
}
,
R :=
{
f⊗g
⏐⏐⏐⏐
f∈A↓a,b,g∈Bb,c for r,s,t ≥ 0 and
a∈⟨↑,↓⟩r,s, b∈⟨↑,↓⟩r,s+1, c∈⟨↑,↓⟩r+t,s+t+1,
}
are bases for OS◦
↑⊗OS ♯ OS, OS◦⊗OS ♯ OS↑ and↓OS◦⊗OS ♯ OS, respectively. Then
we partition the set Q as Q1⊔Q2 so that Q1 consists of all f⊗g∈ Q such that the
reduced lift g has a propagating upward strand on its left edge, and Q2 consists of all
remaining elements of Q. Note for each f⊗g∈ Q2 that the strand of g starting in
the bottom left corner is a rightward cap. Then it is clear that the ma p α maps P
bijectively onto Q1 and β maps Q2 bijectively onto R. This completes the proof.
Now we check that α◦ (X◦
↑⊗ id) = (id ⊗X↑)◦α. Take f⊗g∈ OS◦
↑⊗OS ♯ OS.
We must show that ( f◦X◦(↑b))⊗ (↑g) = f⊗ ((↑g)◦X(↑c)) for f∈ 1aOS◦1↑b and
g∈ 1bOS1c. We can move X◦(↑b) over the ﬁrst tensor product and commute X(↑c)
with↑g, to reduce to checking that 1 ↑b⊗X(↑b) = 1↑b⊗X◦(↑b). The morphism X◦(↑b)
can be transformed into X(↑b) by using the quadratic relation to switch some positive
crossings to negative crossings. This produces some error terms which involve caps
at the top of the picture, which become zero when commuted back o ver the tensor
product. (This argument can be made more formal by using inductio n on the length
of the word b, using the recursions (4.11) and (6.13).)
The proof that β◦ (id⊗X↑) = (↓X◦⊗ id)◦β is similar; one needs to use also (4.3)
and Lemma 6.3. □
ORIENTED SKEIN CATEGORY 43
Finally, we reﬁne the functors E and F . For i∈ k ×, let Ei be the subfunctor of E
that is deﬁned by tensoring with the bimodule that is the generalized i-eigenspace of
↑X :↑OS→↑OS; equivalently, it may be deﬁned by tensoring with the generalized
i-eigenspace of X↓ : OS↓→ OS↓. Similarly, switching ↑ and↓ everywhere, deﬁnes a
subfunctor Fi of F . Let
I :=I1∪It−2 =
{
q2n,t−2q−2n⏐⏐n∈ Z
}
⊂ k ×. (6.27)
Lemma 6.8. There are short exact sequences of functors for each i∈ k ×:
0−→ ∆ ◦F↑
i −→Fi◦ ∆ −→ ∆ ◦F↓
i −→ 0, (6.28)
0−→ ∆ ◦E↓
i −→Ei◦ ∆ −→ ∆ ◦E↑
i −→ 0. (6.29)
Moreover, the functors Ei and Fi are biadjoint, and we have that
E =
⨁
i∈I
Ei, F =
⨁
i∈I
Fi. (6.30)
Proof. Note to start with that although ↓OS is not ﬁnite-dimensional (or even a direct
sum of ﬁnite-dimensional bimodules as was the case for ↓OS◦), it is locally ﬁnite-
dimensional in the sense that it is the direct sum of the ﬁnite-dimensio nal vector spaces
1↓aOS1b for a, b∈⟨↑,↓⟩. The endomorphism ↓X leaves each of these ﬁnite-dimensional
vector spaces invariant. This is enough to see that each generalize di-eigenspace of ↓X
is a summand of the bimodule ↓OS. However, until we have proved (6.30), there may
also be summands arising from generalized eigenspaces correspond ing to eigenvalues of
↓X not inI⊂ k ×, and there could also be summands arising from non-linear irreducible
factors of the characteristic polynomial. Similar remarks apply to Fi.
To deﬁne an adjunction making ( Ei,Fi) into an adjoint pair, we project the adunc-
tion for ( E,F ) onto the summands Ei and Fi. To see that this does the job, one
needs to use the explicit forms for the unit and counit of the adjunc tion (E,F ) given
in (6.22)–(6.23). The key point is that ↑X⊗ id = id ⊗↓X as an endomorphism of
↑OS⊗OS↓OS and↓X⊗ id = id⊗↑X as an endomorphism of ↓OS⊗OS↑OS. A similar
argument produces an adjunction ( Fi,Ei) the other way around. It then follows that
Ei and Fi are both exact; one can also see this since they are summands of th e exact
functors E andF .
The short exact sequences from Lemma 6.7 may be viewed equivalent ly as short
exact sequences of functors
0−→ ∆ ◦F↑−→F◦ ∆ −→ ∆ ◦F↓−→ 0,
0−→ ∆ ◦E↓−→E◦ ∆ −→ ∆ ◦E↑−→ 0.
Similarly, using the ﬁnal assertion of the lemma, we get (6.28)–(6.29) from Lemma 6.7
on passing to the appropriate generalized eigenspaces.
Finally, we must establish (6.30). The short exact sequences of fun ctors obtained
in the previous paragraph plus (6.15) imply that (6.30) holds on any st andard module
∆( λ ). By exactness and Corollary 5.11, it follows that it also holds on any in decom-
posable projective module. Hence, it is true on any module. □
With these branching rules in hand, we can proceed to the deﬁnition o f the formal
character of a locally ﬁnite-dimensional OS-module.
First, we must reﬁne the idempotents 1 a for a ∈ ⟨↑,↓⟩. Let ⟨↑,↓⟩I be the set
of words in the letters {↑i,↓i| i ∈ I}. Thus, an element of ⟨↑,↓⟩I has the form
ai = ( an)in··· (a1)i1 for words a = an··· a1 ∈⟨↑,↓⟩ and i = in··· i1 ∈ ⟨I⟩. Take
a word ai∈⟨↑,↓⟩I of length n. Let Xi be the Jucys-Murphy element in 1 aOS1a that is
deﬁned by a dot on the ith strand from the right, so that X1,...,X n generate a com-
mutative subalgebra of the ﬁnite-dimensional algebra 1 aOS1a. It follows that there
44 J. BRUNDAN
is an idempotent 1 ai ∈ 1aOS1a which projects any 1 aOS1a-module onto the simul-
taneous generalized eigenspaces of X1,...,X n corresponding to eigenvalues i1,...,i n,
respectively. For a given a, all but ﬁnitely many 1 ai are zero.
Now deﬁne the formal character of a locally ﬁnite-dimensional OS-module M by
chM :=
∑
ai∈⟨↑,↓⟩I
(dimM 1ai)ai, (6.31)
which is an element of the ring of (possibly inﬁnite) Z-linear combinations of elements
of the monoid⟨↑,↓⟩I . From the proof of the following lemma plus (6.30), one sees that
1a =∑
i 1ai. Note also that ch is additive on short exact sequences.
Lemma 6.9. chM =∑
i∈I↓i(chEiM ) +∑
i∈I↑i(chFiM ).
Proof. Take ai∈⟨↑,↓⟩I and suppose that a =↑b, i = ij. We claim that dim M 1ai =
dim(FiM )1bj . The lemma follows from this together with the analogous statement
argument with↑ replaced with ↓ and Fi replaced with Ei. To prove the claim, using
(6.20), we have that
M 1a∼= HomOS (1aOS,M )∼= HomOS (E(1bOS),M )
∼= HomOS (1bOS,FM )∼= (FM )1b.
Under this isomorphism, the generalized i-eigenspace of • ⊗ 1b corresponds to the
summand (FiM )1b. The result follows. □
Lemma 6.10. The characters
{
ch L(λ )
⏐⏐λ∈e-Bip
}
of the irreducible OS-modules are
linearly independent.
Proof. Take λ ∈ e-Bipr,s. As L( λ ) is the shortest word module of type λ , its formal
character is a sum Aλ of words of the form ↓ir+s··· ↓ir+1↑ir··· ↑i1 , plus a sum Bλ of
words that are obtained from the ones in Aλ by properly shuﬄing the ↓’s and↑’s, plus
a sum Cλ of strictly longer words. By unitriangularity, it suﬃces to show that the
“leading terms” Aλ are linearly independent for ﬁxed r,s and all λ∈e-Bipr,s. But Aλ
is just the product of the formal characters of D λ↓ and Dλ↑ in the usual sense of the
Hecke algebras Hs andHr. So these words are linearly independent by the well-known
linear independence of irreducible characters for the Hecke algebr a4. □
Now we deﬁne the ( t-shifted) bipartition graph to be the I-colored directed graph
with vertices Bip and an edge λ
i
→ µ if one of the following holds:
• µ is obtained from λ by adding a node of content i to λ↑;
• λ is obtained from µ by adding a node of content t−2i−1 to µ↓.
A small piece of this graph is displayed in Figure 2.
By a pathγ : λ↝ µ we mean an undirected path in the bipartition graph starting
at λ and ending at µ . The type of such a path γ is type(γ) := ai∈⟨↑,↓⟩I where
i = in··· i1 records the colors on the edges of the path λ i1 ··· in µ and a =
an··· a1 ∈ ⟨↑,↓⟩ is deﬁned so am = ↑ or↓ according to whether the mth edge is
traversed forwards or backwards according to its direction. For example, the path
( , ∅ )
t−2
←− ( , )
1
←− (∅ , )
t−2
−→ ∅∅∅
t−2
←− (∅ , )
is of type ↓t−2↑t−2↓1↓t−2 .
Theorem 6.11. For λ∈ Bip, we have that ch ˜∆( λ ) =
∑
γ:∅∅∅↝ λ
type(γ).
4This may be proved in the same way as is explained for the symme tric group in [Kl, Lemma 11.2.5].
ORIENTED SKEIN CATEGORY 45
Proof. Note the inﬁnite sum in the theorem makes sense since there are only ﬁnitely
many paths of any given length. From (6.28)–(6.29) and Lemma 6.5, w e get some
explicit ˜∆-ﬁltrations of Ei ˜∆( λ ) and Fi ˜∆( λ ) with sections ˜∆( µ ) for each µ
i
← λ or
µ
i
→ λ , respectively. Applying Lemma 6.9, we deduce that
ch ˜∆( λ ) =
∑
i∈I
( ∑
µ
i
←λ
↓i ch ˜∆( µ ) +
∑
µ
i
→λ
↑i ch ˜∆( µ )
)
.
Now use induction on path length. □
Corollary 6.12. Take λ ∈ Bip and µ ∈ e-Bip. If L(µ ) is a composition factor of
˜∆( λ ) then there is a path γ : ∅∅∅ ↝ λ and a minimal length path δ : ∅∅∅ ↝ µ such that
type(γ) = type(δ).
Proof. Pick any word ai∈⟨↑,↓⟩I that appears with non-zero coeﬃcient in the formal
character of the shortest word space of L( µ ). Since [ ~∆( λ ) : L( µ )] and [ ~∆( µ ) : L( µ )]
are both non-zero, ai also has non-zero coeﬃcients in ch ~∆( λ ) and ch ~∆( µ ). So Theo-
rem 6.11 implies that there are paths γ : ∅∅∅ ↝ λ and δ : ∅∅∅ ↝ µ of the same type ai.
Moreover,δ is of minimal length amongst all paths ∅∅∅ ↝ µ . □
Corollary 6.13. Suppose that µ ∈ e-Bipr,s. If either t /∈{± qn|n∈ Z}, or e = 0 ,
t =qn for n∈ N and h(µ )≤n, then we have that P(µ ) = ∆( µ ).
Proof. In view of Corollary 5.11, it suﬃces to show that [ ¯∆( λ ) : L( µ )] = δλ,µ for all
λ ∈ e-Bip. Since ¯∆( λ ) and L( µ ) have the same shortest word spaces, this follows
if we can show for λ ∈ e-Bip that [ ¯∆( λ ) : L( µ )]⁄= 0 ⇒ λ ∈ e-Bipr,s. So suppose
that [ ¯∆( λ ) : L( µ )]⁄= 0. Corollary 6.12 implies that there is a path γ : ∅∅∅ ↝ λ of
the same type as a minimal length path δ : ∅∅∅ ↝ µ . Being of minimal length means
thatδ is some permutation of the word ↑ir+s··· ↑ir+1↓ir··· ↓i1 , where i1,...,i r are the
↑-contents of the nodes of µ↑ and ir+1,...,i r+s are the↓-contents of the nodes of µ↓.
If t /∈ {±qn|n ∈ Z}, then the set of possible ↑-contents of nodes of partitions
is disjoint from the set of possible ↓-contents. So any path of type δ starting at ∅∅∅
necessarily ends at an element of Bip r,s. We deduce that λ ∈ e-Bipr,s as required.
Instead, suppose that e = 0,t =qn for n∈ N, and h(µ )≤|n|. Recalling that h(µ ) is
∅∅∅
( , ∅ ) ( ∅, )
(
, ∅
)
( , ∅ ) ( , )
(
∅,
)
(∅, )
(
, ∅
) (
, ∅
)
( , ∅ )
(
,
)
( , )
(
,
)
( , )
(
∅,
) (
∅,
)
(∅, )
1 t−2
q−2
q2 t−2 1 t−2q2 t−2q−2
q−4
q2
t−2
q−2
q4
t−2
q−2
q2
t−2q2
t−2q−2
1 t−2q4
t−2q−2 1
t−2q2
t−2q−4
Figure 2. Bipartition graph up to word length 3
46 J. BRUNDAN
the total number of non-zero parts in both µ↑ and µ↓, these assumptions imply that
i1,...,i r+s are all distinct, and there is a unique path of type δ starting at ∅∅∅ . This
shows that γ =δ, hence, λ = µ . □
Proof of Theorem 1.6. Corollary 6.13 shows that P( λ ) = ∆( λ ) for all λ ∈ e-Bip. So
the standardization functor ∆ sends the indecomposable project ives{Y(λ )|λ∈e-Bip}
in Mod-OS◦ to the indecomposable projectives {P(λ )| λ∈e-Bip} in Mod-OS. Since
this functor is also exact, it follows that it is an equivalence of catego ries. □
Proof of Theorem 1.5. Suppose that q is not a root of unity and t /∈{±qn|n∈ Z}. The
ﬁrst assumption means that e = 0, so OS◦ is semisimple. Hence, OS, or equivalently
˙OS (z,t ), is semisimple thanks to Theorem 1.6. The parametrization of indeco mposable
objects in ˙OS (z,t ) follows from Theorem 5.3: up to isomorphism they correspond to
the irreducible projective modules {∆( λ )| λ∈ Bip}. Moreover, Theorem 5.18 shows in
this case that K0( ˙OS (z,t )) may be identiﬁed with Sym ⊗Z Sym so that [∆( λ )]↔χλ .
It remains to show that OS is not semisimple for all other parameter choices. If q
is a root of unity and t /∈{± qn|n∈ Z}, this follows from Theorem 1.6, since Hecke
algebras are not semisimple at roots of unity. Finally, suppose that q is arbitrary but
t =±qn for some n∈ Z. Using the isomorphisms (2.11)–(2.12), we may as well assume
that t = qn for n∈ N. Example 5.4 shows that ¯∆(((n), ∅ )) is reducible, since it has
a composition factor isomorphic to L((( n + 1), (1))). Since ¯∆(((n), ∅ )) is a ﬁnitely
generated module with irreducible head, it is therefore not complete ly reducible, and
OS is not semisimple. □
