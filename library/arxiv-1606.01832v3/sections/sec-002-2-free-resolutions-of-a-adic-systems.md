---
doc_id: arxiv-1606.01832v3
doc_title: "FLATNESS AND COMPLETION REVISITED AMNON YEKUTIELI"
section_id: sec-002-2-free-resolutions-of-a-adic-systems
section_title: "Free Resolutions of a-Adic Systems"
section_number: 2
pages: 7-9
source_pdf: 1606.01832v3.pdf
source_sha256: da982c95b9674382
doc_brief: "FLATNESS AND COMPLETION REVISITED AMNON YEKUTIELI — We continue investigating the interaction between ﬂatness and a- adic completion for inﬁnitely generated A-modules."
---
As before, A is a commutative ring and a is an ideal in it.
Let us recall some deﬁnitions from our paper [Ye1]. Let Z be a set and let N
be an A-module. The set of all functions f :Z→N is denoted by F(Z,N ). It is
an A-module in the obvious way. The support of a function f : Z→N is the set
{z∈Z|f(z)⁄= 0}. We denote by F ﬁn(Z,N ) the submodule of F(Z,N ) consisting
of ﬁnite support functions. For N =A, the A-module Fﬁn(Z,A ) is free, with basis
the collection{δz}z∈Z of delta functions. For everyA-moduleN there are canonical
isomorphisms
(2.1) F ﬁn(Z,A )⊗AN∼= Fﬁn(Z,N )∼=
⨁
z∈Z
N.
Given a set Z, we have an a-adic system of A-modules
{
Fﬁn(Z,Ak)
}
k∈N. See
Deﬁnition 1.2 regarding morphisms of a-adic systems.
Deﬁnition 2.2. An a-adic system ofA-modulesP is said to be a free a-adic system
if there is an isomorphism of a-adic systems
P∼=
{
Fﬁn(Z,Ak)
}
k∈N
for some set Z.
Deﬁnition 2.3. Let M ={Mk}k∈N be an a-adic system of A-modules. A free
resolution of M is a diagram of a-adic systems
···→P−2 d−1
−−→P−1 d0
−→P 0 η
− →M→0,
such that each Pi ={Pi
k}k∈N is a free a-adic system, and for every k the diagram
of A-modules
(2.4) ···→P−2
k
d−1
k
−−→P−1
k
d0
k
−→P 0
k
ηk
−→Mk→0
is an exact sequence, i.e. it is a free resolution of the Ak-module Mk. We denote
this resolution by η:P→M.
In other words, a free resolution of M ={Mk}k∈N is a commutative diagram
...

...

...

...

···//P−2
1 //

P−1
1 //

P 0
1 //

M1 //

0
···//P−2
0 //P−1
0 //P 0
0 //M0 // 0
in ModA, where P−i
k
∼= Fﬁn(Zi,Ak) for some sets Zi, the vertical homomorphisms
come from the ring surjections Ak+1→Ak, and the rows are exact.
For eachk≥0 let Pk be the complex of free Ak-modules
(2.5) Pk :=
(
···→P−2
k
d−1
k
−−→P−1
k
d0
k
−→P 0
k→0→···
{
8 AMNON YEKUTIELI
that occurs as part of the resolution (2.4). So there is a quasi-isomorphic of com-
plexes ηk :Pk→Mk.
Lemma 2.6. LetB be a commutative ring, with nilpotent ideal b, and let M be a
B-module. Deﬁne the ring ¯B :=B/b and the ¯B-module ¯M := ¯B⊗BM. Suppose
(2.7) ···→¯P−2 ¯d−1
−−→¯P−1 ¯d0
−→¯P 0 ¯η
− →¯M→0
is a free resolution of the module ¯M over the ring ¯B, such that for each i≥0 we
have ¯P−i = Fﬁn(Zi, ¯B) for some set Zi. Also suppose that TorB
i ( ¯B,M ) = 0 for all
i> 0.
Then the resolution (2.7) can be lifted to B. Namely, there is a free resolution
(2.8) ···→P−2 d−1
−−→P−1 d0
−→P 0 η
− →M→0
of the B-moduleM, such that P−i = Fﬁn(Zi,B ) for every i, and the sequence (2.7)
is gotten from the sequence (2.8) by applying the functor ¯B⊗B−.
Proof. The proof is by induction on i = 0, 1, 2,....
We start with i = 0. For each z∈Z0, we choose an arbitrary element mz∈M
lifting the element ¯η(δz)∈¯M. This determines a homomorphism of B-modules
η: Fﬁn(Z0,B )→M.
The Nakayama Lemma (in its nilpotent version) says that ηis surjective.
Now we take some i≥0, and we assume that a partial free resolution
(2.9) P−i d−i+1
−−−−→P−i+1→···
d0
−→P 0 η
− →M→0
was found, lifting
(2.10) ¯P−i ¯d−i+1
−−−−→¯P−i+1→···
¯d0
−→¯P 0 ¯η
− →¯M→0 ;
namely the sequence (2.10) is gotten from (2.9) by the operation ¯B⊗B−. Deﬁne
the modules L−i and ¯L−i to be the submodules of P−i and ¯P−i respectively that
make the sequences
(2.11) 0 →L−i→P−i d−i+1
−−−−→P−i+1→···
d0
−→P 0 η
− →M→0
and
(2.12) 0 →¯L−i→¯P−i ¯d−i+1
−−−−→¯P−i+1→···
¯d0
−→¯P 0 ¯η
− →¯M→0
exact. There is a homomorphism φ:L−i→¯L−i that is induced from the surjection
P−i→¯P−i.
We are given that the B-modules M,P 0,...,P−i satisfy TorB
j ( ¯B,−) = 0 for
everyj >0. By the usual syzygy argument this is also satisﬁed by L−i. Therefore
the sequence gotten by applying ¯B⊗B−to the exact sequence (2.11) remains
exact, and thus it is isomorphic to the sequence (2.12). This implies that the
homomorphism ¯B⊗BL−i→¯L−i is bijective; and henceφ:L−i→¯L−i is surjective.
As before, using the Nakayama Lemma, we can lift the given surjection
¯d−i : ¯P−i−1 = Fﬁn(Zi+1, ¯B)→¯L−i
to a surjection
d−i :P−i−1 = Fﬁn(Zi+1,B )→L−i.
□
FLATNESS AND COMPLETION REVISITED 9
Theorem 2.13. Let A be a commutative ring, let a be an ideal in A, and let
M ={Mk}k∈N be an a-adic system of A-modules. The following conditions are
equivalent:
(i) The a-adic system M admits a free resolution.
(ii) For every k≥0 and i> 0, the module TorAk+1
i (Ak,Mk+1) vanishes.
Proof. (i)⇒(ii): Assume M admits a free resolution η: P →M. We can
calculate TorAk+1
i (Ak,Mk+1) using the free resolution ηk+1 : Pk+1→Mk+1; see
formula (2.5). Now the complex Ak⊗Ak+1 Pk+1 is isomorphic to the complex Pk,
and therefore
H−i(Ak⊗Ak+1Pk+1) = 0
for all i> 0.
(ii)⇒(i): The proof is by induction on k. For k = 0 we choose a free resolution
···→P−2
0
d−1
0
−−→P−1
0
d0
0
−→P 0
0
η0
−→M0→0
of the A0-module M0, where P−i
0 = Fﬁn(Zi,A 0) for some sets Zi.
Now assume that for k≥0 we found a free resolution of the truncated a-adic
system{Mk′}0≤k′≤k. Let B :=Ak+1 and ¯B :=Ak. Consider the free resolution
···→P−2
k
d−1
k
−−→P−1
k
d0
k
−→P 0
k
ηk
−→Mk→0
over the ring ¯B. By Lemma 2.6 this resolution can be lifted to a free resolution of
Mk+1 over ring B, with the same indexing sets Z0,Z 1,.... □
The theorem immediately implies:
Corollary 2.14. IfM is a ﬂat a-adic system, then it has a free resolution.
