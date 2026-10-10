---
doc_id: 1104248094
doc_title: "Commun. Math. Phys. 140, 481-521 (1991) Communications in Mathematical Physics© Springer-Verlag 1991 Hochschild and Cyclic Homology of Quantum Groups"
section_id: sec-014-62-quantum-algebraic-groups-this-subsection-is-m
section_title: "Quantum Algebraic Groups. This subsection is mainly devoted to the proof2"
section_number: 6.2
pages: 26-40
source_pdf: 1104248094.pdf
source_sha256: c1fdb4791afcad3b
doc_brief: "Commun. Math. Phys. 140, 481-521 (1991) Communications in Mathematical Physics© Springer-Verlag 1991 Hochschild and Cyclic Homology of Quantum Groups — For an arbitrary complex linear semisimple Lie"
---
that the spectral sequence leading to the Hochschild homology is also degenerate
at E2 for the algebraic case.
In the formal case the E2 term turns out to be that of the Cartan subgroup.
Since the Cartan subgroup is unquantized, the comparison theorem immediately
yields the Hochschild and cyclic homology in the formal case. But now the E2
2 The proof in our first draft was incomplete, as was pointed to us independently by J. Block
and E. Getzler
Hochschild and Cyclic Homology of Quantum Groups 507
term is related to the normalizer of the Cartan subgroup. Since there is no
unquantized normalizer in quantum algebraic groups, it is not obvious that we
have degeneracy at E2 as in the formal case. However one does expect the spectral
sequence associated with the Planck constant to be degenerate at E2. As the
philosophy of quantization goes, everything should be determined by its
quasiclassical limit, in other words, nothing new happens beyond the first term in
the deformation. In terms of spectral sequence the quasiclassical limit is taken care
of by (E^,dι). If nothing is new beyond that, one expects that the spectral sequence
is degenerate at E2.
We first reduce the proof of E2 ^ E™ to that of E2 ^ £*. The following lemma
is a special case of a Grothendieck theorem about the superposition of functors.
Lemma (6.2.1). Let A, B be associative algebras, M' left A-module, M right A-module;
φ:A^>B algebra homomorphism. Then there is a spectral sequence with
( ' j
Proof. Consider the following double complex
Γ Γ Γ"φ d' φ d' ^(M®A2®B)®M'< - (M®A2®B)®B®M'< - (M®A2®B)®B2®M'
(M®A®B)®Mf < (M®A®B)®B®M' < (M®A®B)®B2®M1'
\d" \d" \d"Φ ψ ψ
(M®B)®Mf ^— (M®B)®B®Mr ^— (M®B)®B2®M'
(6.6)
where
d' = (- l)ndB(M ®An®B9 M'), d" = dA(M, B) ® 1
and dA(M,M') denotes the boundary operator of the standard complex for
Tor^(M,M') It is easy to check that this really is a double complex. We can
compute the associated spectral sequences. If we compute the vertical complex
first, we get
Alternatively we can compute the horizontal complex first. Note M ® An ® B is a
free β-module. Therefore
and
Tor£(M (x) An ® B, M') = (M ® A" ® B) ®BM' = M ® An ® Mr,
We see the spectral sequence is degenerate and
(M9M').
508 P. Feng and B. Tsygan
From now on, A = Ch[G], B = CΛ[/ί], φ :A -> B is induced by the Hopf algebra
imbedding C/(hc) -> Uh(g). M' = C((h)) = k as a left A-module via the counit ε,
M = CΛ[G] as a right A-module via p, i.e.,
where Δ(a) = ^aj®aj and 5 indicates the antipode. Note as Hopf algebra
j
CΛ[H] = C[H]®C((Λ)). Recall that Tor^(M,/c) is the Hochschild homology of
the quantum group CΛ[G] as proved in Proposition (2.4).
Lemma (6.2.2). Denote the double complex (6.6) by 3~orB^(3~or^(M,B\k) and the
standard complex for Tor^ by 3~or^. There is a quasί-isomorphίsm of complexes
3Γorl(3~or*(M, B\ k) -> Γoι*(M ®AB, k).
Proof. Obviously there is a natural complex map. Note the quasi-classical limit
of the double complex (6.6) is exactly the double complex (4.22) that computes the
Lie algebra homology #*(g*,C[G]). The lemma simply follows from the fact
that the second term of the spectral sequence of the double complex (4.22)
E2j = //ί(ac, /f/(nc, C[G])) is non-vanishing only when j = 0.
Proposition (6.2.3). The spectral sequence leading to the Hochschild homology of
Cή[G] is degenerate at E2, i.e.,
HHflCJίG] ) * tf/g*, C[G] ) <g> C((Λ)X
if and only if
Proof. By the previous lemma we have two complexes quasi-isomorphic For each
complex we can consider the spectral sequence induced by the Planck constant.
Obviously their E2 terms are isomorphic. So one is degenerate at E2 if and only
if the other one is. For the complex &~oτ^(M®AB,k), it is easy to see that the
spectral sequence is degenerate at E2 if and only if
Thus the lemma.
The main result of this subsection is the following
Theorem (6.2.4).
c, (6.7)
where M = A = C/,[G], and A acts on M by p.
The proof will be divided into a series of lemmas. Proposition (6.2.3) and
Theorem (6.2.4) together assert that the spectral sequence induced by the Planck
constant for the Hochschild homology is indeed degenerate at E2.
In computing the Lie algebra homology HM(g*,C[G]) we use the fact that
the g* action on C[G] commutes with the infinitesimal right translation by the
Cartan subalgebra hc. We decomposes C[G] according to this right translation
C[G] = © Vλ,
Hochschild and Cyclic Homology of Quantum Groups 509
where A is the weight lattice, and we get
λeΛ
We observe that this decomposition also holds at the quantum level. Recall the
Cartan subalgebra is not quantized. We define an action of U(hc) on M in the
following way:
xel/(hc), (6.8)
j
where Δ(f) = Σfj®fj> and <»> is the natural paring between C[G] and I7Λ(g).
j
Apparently the classical limit of this action is the infinitesimal right translation.
Since CΛ[G] is the deformation of C[G], we have
λeΛ
The following Lemma asserts that Mλ is also a right A-module via p.
Lemma (6.2.5). The actions of £/(hc) and CΛ[G] on M commute.
Proof. Consider arbitrary #ehc, αeCh[G],/6M. It follows from the definition that
r(H)(fJ2) = r(H)(/ι)/2 + MH)(f2).
Therefore
r(H)p(a)(f) - p(a)r(H)(f) = Σ \_r(H}(άsj)faj + a]
j
where Δ(a) = Σ aj®&j Denote
3
(A® l)Δ(a) = (l®Δ)Δ(a) = Σ bk®ck®dk.
k
Note for CΛ[G] we have Δ(s(a)) = (s®s)Pl2Δ(a\ where P12 is the permutation
operator. It then follows that
Σ <H, c{ + ck)fjbk = 0.
k
As a consequence of the lemma, (6.7) is equivalent to
#o(g*> KJ®cfc = MA®^/c. (6.9)
Recall that (E$)λ = H0(g*, KA) has dimension | Oλ\. We denote the orbit in A through
λ generated by the Weyl group W by (9λ and the number of distinct weights on
the orbit by \(9λ\. This provides an upper bound for the dimension of
(E™)λ = Mλ®Ak. Since M®Ak~ A /[A, A], we can get a lower bound on that
dimension by constructing traces over A. The main theorem is proved if we can
show that the lower bound is also \Θλ\. The following several lemmas are about
constructing and counting the traces over A.
Lemma (6.2.6). Let a,b,c,d be the generators of Ch[SL2] as in Example (3.14).
There are two families of traces for Cfc[SL2], denoted by τ*,τ*, where n is an integer
510 P. Feng and B. Tsygan
and n 7^ 0 for τsn. The following are the only non-zero values of the traces:
(1) n>0
~+" ^O; (6.10)l-q2k+n
(2) n<0
*cfc) = v 3fc—, fc^O; (6.11)
(3) n = 0
τ«(Λί*)=l, fc^O; (6.12)
where q = eh.
We use the elements of the Weyl group W = {e, s} to label the families of traces.
The naturalness of this notation will become clear later. The proof of this lemma
is straightforward and is given in Appendix B. Note the lemma proves the main
theorem for CΛ[SL2]
In general, the family of traces associated with the identity of the Weyl group
is simply constructed as follows. Recall that the Cartan subalgebra is not quantized.
The natural imbedding
induces the Hopf algebra homomorphism
π:CA[G]->CΛ[/ί] = C[//](8)cC(W). (6.13)
Note
AeΛ
and C[#]λ is one-dimensional. Choose a basis {fλ} for C[#] such that fλeC[H~\λ.
Let {/*} be the dual basis. Define
τ; = /* π:Cfc[G]->fc. (6.14)
This is the family of traces associated with the identity of the Weyl group. We see
that the unquantized Cartan subgroup contributes to E™.
In quantizing the universal enveloping algebra [11,21], one chooses a Cartan
subalgebra and a set of simple roots a1?a2,...,ar. For every simple root aj? there
is a Hopf algebra imbedding
which induces a Hopf algebra homomorphism
, (6.15)
Consider an arbitrary element w of the Weyl group. Let w = stί si2 - - stl be a minimal
representation for w. Here / = /(w) is the length of w. s7 is the simple reflection
associated with the simple root α,-. Define, for arbitrary Ae/l, nίn2 n{ φ 0, a linear
functional
Hochschild and Cyclic Homology of Quantum Groups
by
511
(6.16)
Lemma (6.2.7). τ™(n1,n2, ..,nl) is a trace. It vanishes identically unless
(6.17)
When n1,n2,...,nl are thus fixed, τj> = τj>(«1,n2,...,nj) takes non-zero values only
on Mλ. Different elements of Weyl group give linearly independent traces.
Proof. Since A, π^ are algebra homomorphisms and τeλ, τ* are traces, (6.16) definitely
defines a trace for CA[G]. Note
VHεhc,
we have
Thus τ* vanishes on Mλ,Φλ.
To get the constraints (6.17), we notice that l/(hc) also acts from the left on
CΛ[G]. Explicitly, for any Hel/(hJ, /eCA[G],
(6.18)
where 4(/) = Σ//®7/ ^ f°U°ws from the definition that
The constraints on n(l,...,n(| follow from the observation
and
τsn πj(l(H)(f}) = τsn πj(r(Sj(H))(f)).
(6.19)
(6.20)
(6.21)
Recall that CΛ[G] is spanned by the matrix elements of the finite dimensional
representations of l/Λ(g). We always assume that ί/(hc) is diagonalized in these
representations. Since τ\ is non-zero only on the diagonal matrix elements for
which the left and right actions of t/(hc) are the same, we get (6.20). To get (6.21),
we observe that there is the g-analogue of the Weyl group as defined in [24].
Denote the ^-analogue of Sj by w,-, which generates the g-Weyl group. These w/s
act on the representations of £/Λ(g). One can easily check that for Ch[SL2] the
matrix elements with non-zero trace τ*, i.e., bmcn, are on the diagonal when
multiplied by the w. This gives us
τsn π//(fi)(/)) = τ>/r(
512 P. Feng and B. Tsygan
But the g-Weyl group action on hc coincides with that of the ordinary Weyl group,
i.e.
Thus follows (6.21).
It is obvious that τj is not identically zero when λ satisfies the constraint (6.17)
with n1 -nl^Q. From the above argument, it is also clear that τ£ is non-zero
only on the subspace of Mλ corresponding to the weight w(λ) under the left action
of hc. The linear independence of the traces thus follows immediately.
We have constructed families of traces labeled by the elements of the Weyl
group. We remark that they are intrinsically related to the Levendorski-Soibelman-
Vaksman modules [41,42,26] labeled by the Weyl group and Cartan subgroup.
Informally, the relation is as follows. One can take the formal traces from these
modules when \q\ < 1. Unfortunately they do not all vanish on the commutant
[,4, ,4]. The reason is that certain elements of A = Ch[G] are represented by
operators which are not of the trace class. What saves the day is that we can use
weight space decomposition to pin down the bad components of the formal traces.
The good ones are exactly τ\ with constraints on λ as stated in the previous lemma.
More on this in Appendix B.
Our next job is to count how many wety provide traces to an arbitrary fixed
λe A The previous lemma tells us what Mλ will be provided a trace by a particular
weW. Let us first reformulate this in a more geometrical way.
Fix a λeΛ9 and a minimal representation w = s^s^ s^. Let Pw(λ) denote the
ordered set of weights {λl9λl_19...9λl9λ0}9 where
AI = A, λk_ j = Sik(/fc), /C = /,... , 2, 1.
We call this the path associated with the pair (A,w) (with a chosen minimal
representation for w). We say the path has stationary points if λk = λk _ ί for some k.
Lemma (6.2.8). Let Pw(/l) and P'w(λ) be two paths corresponding to two choices of
minimal representations for w. Then P^(λ) has stationary points if and only if P'J(λ)
has.
Proof. Let us look at the different parts of the two paths. They come from the
non-trivial Coxeter relations
where
(6.22)
and (a.j) is the Cartan matrix. For any λ, the sequence st(λ)9 SjS^λ), . . . , (st-s7-)miJW
form a closed path. Assume λ is fixed by si9 then it is easy to see that its opposite
point on the closed path is fixed by Sj. If 1 is a stationary point on Pw(λ) then
either 1 or the opposite point of 1 is on P'w(λ). Thus P'w(λ) also has stationary
points.
We say w is maximal relative to λ if Pw(λ) does not have stationary points. Of
course this property is independent of the choice of minimal representation for w.
Hochschild and Cyclic Homology of Quantum Groups 513
Corollary (6.2.9). wePF provides a trace τ" for Mλ if and only if w is maximal
relative to λ.
Proof. From the Lemma (6.2.7), w provides traces to all integral weights except
those on the union of the following set of hyperplanes:
(6.23)
This is equivalent to
ίo = <λ,αίl>,
where <,> denotes the inner product in the weight space. The above equations
mean λk is fixed by sfk. The claim is proved.
Lemma (6.2.10). For any λeΛ, the number ofWeyl group elements that are maximal
relative to λ equals to \Θλ\, the number of points on the orbit (9λ generated by the
Weyl group W through λ.
Proof. We first construct a cell complex &λ whose vertices are the points on &λ.
Two distinct vertices are connected by an edge if they are transformed into each
other by a simple reflection Sj. We attach a face to every closed path corresponding
to a non-trivial Coxeter relation (6.22) such that the boundary of the face is the
closed path. We also choose a base point λ0 which is either in the fundamental
domain (when λ is regular) or on the boundary of the fundamental domain (when
λ is singular). The base point is of course unique for every orbit. We claim that
Θλ is connected and simply connected.
Let us construct another cell complex W. The vertices are the elements of the
Weyl group. There is an edge between vv^ and w2 if wx = Sj\v2 for some j. For every
closed path corresponding to a non-trivial Coxeter relation, a face is assigned
whose boundary is the closed path. We choose the identity e to be the base point.
By definition W is connected and simply connected. Note the stabilizer subgroup
Wλo of AO is of the Weyl group type and the associated cell complex Wλo is connected
and simply connected. The homotopy fibration
W^W-*&^ (6.24)
induces the homotopy exact sequence
From this we immediately get
πι(0J = 0 = π0(0J. (6.25)
Thus Sλ is connected and simply connected.
For any Λe/1, the Weyl group can be viewed as a union of cosets Wλλ, labeled
514 P. Feng and B. Tsygan
by the points λΈ(9λ. The elements in Wλλ, transform λ to λ'. Since (9λ is simply
connected, there is only one element in each coset that is maximal relative to λ.
Thus the total number of maximal elements relative to λ is \&λ\. The lemma is
proved.
Proof of Theorem (6.2.4). We have reduced the proof to that of
Since #0(g*, Vλ) has dimension \Θλ\9 this provides an upper bound for the
dimension of Mλ®Ak. The above lemma provides a lower bound which is also
\Φλ\. This means elements of E% all survive to E%. The theorem is proved.
In summarizing, we have
Theorem (6.2.11). The Hochschίld homology of the quantum algebraic group is
where Ωn\_No] is defined in (5.22).
The last thing we are going to compute in this paper is the cyclic homology
of the quantum algebraic groups. This is now fairly easy when we know the
Hochschild homology. Recall HC^(A) is computed by the double complex
where b and B are defined at the beginning of Sect. 2.
The Hochschild homology is only the E1 term of the spectral sequence
associated with the double complex. The complex for E2 is
000
— HH i <
B
o
B
^--. (6.26)
0
HH0<
As is well-known from [10,17], the derivation of r(H), Hehc on A induces the
operation of Lie derivative
&a:HHβ(A)-+HH,,(A)
and
Hochschild and Cyclic Homology of Quantum Groups 515
such that
B'ίH + iH B=<?H. (6.27)
From this one sees immediately that B is exact on all weight components of &H
except zero. Hence the only contributions to E2 (except for the top row in (6.26))
is from λ = 0. Recall
HHn(A) * Hπ(g*, C[G] ) = 0 tf n(g*, Vλ).
λ
Note that Hn(g*, V0) is one dimensional and is represented by / = constant. So
except for the contributions from the top row in (6.26) we can identify the total
homology of the double complex (6.26) with the invariant differential forms on
the Cartan subgroup H. The contribution from the top row is simply
Ωn[NG]/dΩn_ί[NG']. It is also easy to see the spectral sequence is degenerate at
E2. The following theorem is now obvious.
Theorem (6.2.12). The cyclic homology for the quantum algebraic group is
tfC»(C,IG])^(4[^G]/^
(6.28)
where ΏΠ[JVG] is defined in (5.22).
This concludes our computation for the Hochschild and cyclic homology of
quantum algebraic groups. We found that they are determined by the quasiclassical
limit.
Appendix A.
We explain some of our conventions for the calculus on Lie groups.
Let /α, a = 1, 2, . . . , dim g be the basis for the Lie algebra g, which is identified
with the tangent space at the identity e\ fcab the structure constant, Ja the dual
basis, Xla, Xra the left, right invariant vector field on G such that Xla(e) = Xra(e) = /fl;
<ϋp ωar the left, right invariant 1-form with ωat(e) = ωar(e) = Ja. Repeated index always
means summation.
First of all,
Both X'a(g) and X'a(g) span the tangent space at g, they can be transformed into
each other as
faXlb(g); (A.2)
and similarly,
ω« = (Ad*_,)X, < = (Ad*)X. (A.3)
Let yχ denote the Lie derivative corresponding to the vector field X, then
χ*?*=rΛ ^*;=o,'er ^ ' '
516 P. Feng and B. Tsygan
and from <J^,ωJ> = <A^,ω*> = δba, we have
a a
The adjoint action is defined to be
<c) = fcabJb (A.6)
The exterior derivative d acts as
dωar=fabcωbrΛωcr. (A.I)
The (infinitesimal) left translation of g on C°°(G) is
1(1) f(g) = - &χrf(g) = lim -(/(*~"0) - /to))- (A.8)f-K> ί
Appendix B. Example G = SL2
The quantum algebraic group structure is as discussed in Sect. 3, specifically in
Example (3.14). So we will not repeat those definitions.
B.I. The Quasiclassical Limit. We start with the computation of #n(g*,C[G]).
i/i o \ i/o ι\ i/o o\ . , . f
H = - , E+ = - , JE_ =- is a basis for g,L ,L ,L the
4\o -i/ 2\o o; 2\ι oydual basis for g*. The action of g* on C[G] as defined in Proposition (4.4) is as
follows:
\-b—, (B.I)
dd l '
a
da
u ,r 3 L d d j d
where N = a \-b \-c \-d —.
da db dc dd
We choose a basis for C[G] as follows
Xp^n:=apbq(bc)n, p,qeZ, n^O, (B.2)
where ap\= d~p, bq:= c~q if p,q < 0. On this basis we get
-f XP»<3>H J P,Q>n p,g,π+l'
Hochschild and Cyclic Homology of Quantum Groups 517
p + l,q'/P,
/ Y^
p,q,π p + 1,9
fp,q,n^p+ί,q
/PΛΛ+1.,
fπ.a.nXpΊ,a
-2σ(L_)A MiI1 =
p- l,q- l
Xp,q,n p
P^O,
P<0,
P>0,
p>0,
P^O,
P^O,
where fpΛJΛ = |p| + |9| + 2n + 2,0^,, = - |p| + \q\ + 2n + 2.
Note
(B.3)
(B.4)
and Vλ is invariant under the action of g* as expected.
#n(g*, Vλ) is computed by the double complex given in Lemma (4.11), and we
choose to compute the nc-homology first. Note [L+,L~] =0, this again can be
computed by a double complex. The calculation is straightforward and we simply
write down the result here.
Case 1. λ = 0
ac acts on HQ(nc, K0) non-semisimply,
σ(L°)l = -2c,
σ(L°)6c - - 2bc - 4(bc)2 = - 2σ(L+ )dc * 0.
Therefore
Case 2. A = p — ^f > 0
H1(nc,KJ =
H0(nc, Vλ) =
(B.5)
(B.6)
(B.7)
(B.8)
Of course terms involving - are there only when - makes sense, i.e., is an integer.
Even when they exist, ac acts with non-zero eigenvalue. So they do not survive to
be in the g*-homology. On the other hand
(B.9)
σ(L°)aλ= -(λ + 2)aλ(bc)= -
σ(L°)cλ = - λcλ - (λ + 2)cλ(bc) = 2σ(L_)acλ~l ^ 0.
518 P. Feng and B. Tsygan
Thus
Case 3. λ < 0 is similar to case 2.
B.2. The Traces for the Quantum Algebra. We want to check that the linear
functionals defined in Lemma (6.2.6) are indeed traces, i.e., they vanish on the
commutators [CΛ[SL2], CΛ[SL2]]. By Proposition (2.4), the commutator of a Hopf
algebra A is the same as the image of A under the right action of A via p. So we
only need to check that the linear functionals in Lemma (6.2.6) vanish on
ρ(tij)(Ch[_SL2~\\ where (ίy) = ί a j are the generators of CΛ[SL2]. Recall
and
'a bS[ , c dJJ \—q~1c a
where we denote q = eh. We have
p(b)(akbmcn) = q~k(l - qk+m+n + 2)(ab)(akbmc")
f}( f*\( fj*h^f*^\ ί 1 ft "* " \ft h™f^ ~^~ —I— n Γ1 π "* " ^/7 r>"* ~^" f^ ~^~
p(c)(d*&wc") = 4*(l-ι
p(d)(dkbmcn) = q'm-ndkbmcn -q~k+ΐ(l - q~k~m-n'2)dkbm+icn+1. (B.I 1)
From this it is easy to see the tracial properties of the linear functionals in
Lemma (6.2.6).
The family of traces τen is easy to understand. They correspond to the
unquantized Cartan subgroup. How to understand the τ*, n Φ 0? The answer is
that while τen corresponds to the point-like symplectic leaves, τ^ corresponds to
the extended symplectic leaves in the Poisson Lie group (SL2, π). In [42] Soibelman
and Vaksman construct irreducible modules for Ch[Sl/(2)] corresponding to the
symplectic leaves of the Poisson Lie group SU(2). They work with the compact
quantum group and we work with the complex quantum group. The difference is
not important in the discussion here. For the trivial symplectic leaves corresponding
to the Cartan subgroup, they get one-dimensional representations. This provides
the family of traces τ*. For the non-trivial symplectic leaves, the corresponding
Levendorski-Soibelman-Vaksman modules are infinite dimensional. Specifically,
they are
Hochschild and Cyclic Homology of Quantum Groups 519
with the module structure given by
d-e0 = Q9 a en = en + 1, b-en = aqnen, c en = βq"en, (B.12)
where αβ = — q. From this module we can get formally the following "trace," with
the only non-zero value given by
m,n^0. (B.I 3)
But this is not really a trace on Ch[SL2], since
τa(ad -da) = (q-1- q)τ.(bc) = -q~2^Q.
This is due to the fact that α, d are not of "trace class." The way out of this difficulty
is to look at the weight decomposition of τα,
We find that τ*, n Φ 0 are traces and τs0 is not a trace. As we have seen in
Subsect. 6.2, this weight space decomposition proves to be very effective in the
general case.
B3. The Results. As we remarked in Subsect. 6.2, the construction of the traces
in the previous subsection actually shows that the spectral sequence is degenerate
at E2 for CΛ[SL2]. Thus
HHn(Ch[G}) s HB(g*, C[G])® C((Λ)). (B.14)
As for the cyclic homology, the direct computation is actually not hard to
carry out for quantum SL2. Corresponding to the new complex for the Hochschild
homology (2.16), there is a new double complex (C^(A\d,D) for the cyclic
homology, where D = ξ'Bξ just as d = ξ'bξ. We consider the spectral sequence
associated with this new double complex whose E1 term is the Hochschild
homology. Since only HH0 and HHl is non-zero, the double complex for the E2
becomes
where D2(f) = η(Σfj®fj + f® 1) = Σ//®(dfj)(e) with Δ(f) = Σfj®?J
It is easy to calculate
D2(aλ) = λ(aλ®L° + 2aλ~ lc® L+\
520 P. Feng and B. Tsygan
Therefore we get
H0(g*,C[G])(χ)C((/ι)) n = 0
n= 1,3,5,... (B.17)
H°ΌR(Tc)®C((h)) n = 2,4,6,...
as expected.
