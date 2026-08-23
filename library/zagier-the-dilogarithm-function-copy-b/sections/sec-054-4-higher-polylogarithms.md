---
doc_id: zagier-the-dilogarithm-function-copy-b
doc_title: "The Dilogarithm Function Don Zagier"
section_id: sec-054-4-higher-polylogarithms
section_title: "Higher polylogarithms"
section_number: 4
pages: 56-58
source_pdf: zagier-the-dilogarithm-function-copy-b.pdf
source_sha256: c584944a501ef0c5
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
duplicate_of: "zagier-the-dilogarithm-function"
---
In Chapter I we already introduced the higher polylogarithm functions Lim(z),
their one-valued modiﬁcations Dm(z), and the idea that there might be rela-
tions among special values of Dedekind zeta functions at integral argumen ts
and the values of polylogarithms at algebraic arguments, analogous to those
existing for the dilogarithm. But at the time when that text was writt en, I
knew only a few sporadic results, and the chapter ends with the sent ence “the
general picture is not yet clear.” After it was written I did a lot of num eri-
cal calculations with special values of higher polylogarithm functions and was
able to formulate a general conjecture which has now been proved in a s mall
number and numerically veriﬁed in a large number of cases. Since the re are
already several expositions of these conjectures ([45], [46], Chapter 1 of [47]), I
The Dilogarithm Function 59
give only a sketch here, the more so because higher polylogarithms seem so far
to play much less of a role in mathematical physics than the dilogarithm . (See,
however, [35].) Nevertheless, the higher polylogarithm story is very pretty and
it seemed a pity to omit it entirely.
We describe the conjectures in Section A and some supporting exampl es
in Section B. It turns out that the theory works better if one replaces the
function Dm(z) deﬁned in Chapter I by the slightly diﬀerent function
Lm(z)= ℜm
( m−1∑
k=0
Bk
(log |z|2)k
k! Lim−k(z)
)
,
where ℜm denotes ℜ for m odd and ℑ for m even and Bk is the kth Bernoulli
number. Thus L2(z)= D2(z)= D(z), but L3(z)= D3(z)+ 1
6 log2 |z| log
⏐
⏐ 1−z
√z
⏐
⏐.
Like Dm, Lm is a single-valued real-analytic function on P1(C) /integerdivide{0, 1, ∞},
but it is has the advantages of being continuous at the three singular point s,
of having clean functional equations (for instance, the logarithmic ter ms in
the two functional equations for D3 given in §3 of Chapter I are absent when
these are written in terms of L3), and of leading to a simpler formulation of
the conjectures relating the polylogarithms to zeta values and to algeb raic
K-theory.
A. Higher Bloch groups and higher K-groups. In Chapter I we deﬁned
the Bloch group B(F ) of a ﬁeld F (where we have changed the notation from
the previous BF , because we will have higher Bloch groups Bm(F ) as well)
as A(F )/C(F ), where A(F ) is the set of all elements ξ =∑ ni[xi] ∈ Z[F ]
satisfying ∂(ξ): =∑ ni(xi) ∧ (1 − xi)=0a n d C(F ) the subgroup generated
by the ﬁve-term relations V (x, y) and by its degenerations [ x]+[ 1 /x]a n d
[x]+[1 −x]. Because the elements of C(C) are in the kernel of the Bloch-Wigner
dilogarithm D we have a map D : B(C) → R. The key statement is that for a
number ﬁeld F of degree r1+2r2 over Q (r1 real and 2r2 complex embeddings),
the group B(F )h a sr a n kr2 and the map LF : B(F )/(torsion) → Rr2 induced
by the values of D on the various conjugates of ξ ∈ B(F ) (there are only r2
essentially diﬀerent such values because D(¯x)= −D(x) ) is an isomorphism
onto a lattice whose covolume is essentially equal to ζF (2).
The conjectural picture for the mth polylogarithm, m ≥ 3, is that we can
introduce similarly deﬁned higher Bloch groups Bm(F )= Am(F )/Cm(F ),
where Am(F ) is a suitably deﬁned subgroup of Z[F ]a n d Cm(F ) ⊆ Am(F )
is the subgroup corresponding to the functional equations of the higher poly-
logarithm function Lm, in such a way that the rank of Bm(F ) is equal to
r2 or r1 + r2 (depending whether m is even or odd) and that the map
Lm,F : Bm(F )/(torsion) → R(r1+)r2 induced by the values of Lm on the
various conjugates of ξ ∈ Z[F ] is an isomorphism onto a lattice of ﬁnite co-
volume. (Note that Lm(¯x)=( −1)m−1Lm(x), which is why there are only r2
essentially diﬀerent values of Lm if m is even, but r1 + r2 if m is odd.) Again,
this implies the existence of numerous Q-linear relations among the values of
60 Don Zagier
Lm(x), x ∈ F . Moreover, the covolume of the lattice Im( Lm,F ) is supposed to
be a simple multiple of ζF (m), so that one also obtains (conjectural) formulas
for the values of the Dedekind zeta functions of arbitrary number ﬁel ds at
s = m in terms of the mth polylogarithm function with algebraic arguments.
Furthermore, the whole picture is supposed to correspond to the hi gher
K-groups of F , as already mentioned at the end of Chapter I. For each i ≥ 0
one has K-groups Ki(F )a n d Ki(OF ) which for i ≥ 2 become isomorphic
after tensoring with Q. The group Ki(OF ) is ﬁnitely generated and its rank
was determined by Borel [5]: it is 0 for i even and is r2 or r1 + r2 (depending
as before whether m is even or odd) if i =2 m − 1, m ≥ 2. Moreover, Borel
showed that there is a natural “regulator” map Rm,F : K2m−1(F ) → R(r1+)r2
which gives an isomorphism of K2m−1(F )/(torsion) onto a sublattice whose
covolume is a simple multiple of ζF (m). The motivation for the polylogarithm
conjectures as stated above is that we expect there to be an isomorphis m
(at least after tensoring with Q) between K2m−1(F )a n d Bm(F ) such that
the Borel regulator map Rm,F and the polylogarithm map Lm,F correspond.
This is not known at all in general, but de Jeu [12] and Beilinson–Deligne [ 2]
deﬁned a map compatible with Rm,F and Lm,F from (a version of) Bm(F )t o
K2m−1(F ), and for m = 3 Goncharov [20] proved the surjectivity of this map,
establishing in this special case my conjecture that ζF (3) for any number ﬁeld
F can be expressed in terms of polylogarithms.
In the rest of this subsection, we describe the inductive deﬁni tion of the
groups Bm(F ) in a way which is algorithmically workable, though theoretically
unfounded.
The ﬁrst case is m = 3. A ﬁrst candidate for A3(F ) is Ker( ∂3), where
∂3 : Z[F ] → F × ⊗ Λ2F × is the map sending [ x]t o( x) ⊗ ((x) ∧ (1 − x)) if
x ⁄=0 , 1 (and to 0 if x = 0 or 1). If this deﬁnition and the above hypothetical
statements are correct, we deduce—even without knowing the deﬁni tions of
C3(F )a n d B3(F )—that any r1 + r2 + 1 values L3(σ(x)), where σ : F → C
is a ﬁxed embedding and x ranges over values in F , should be Q-linearly
dependent. Numerical evidence supported this for totally real ﬁeld s. For in-
stance, if F = Q(
√
5) then the three one-term elements [1], [(1 +
√
5)/2] and
[(1 −
√
5)/2] belong to Ker( ∂3) and we ﬁnd (numerically, but here provably)
that L3
( 1+
√
5
2
)
+L3
( 1−
√
5
2
)
= 1
