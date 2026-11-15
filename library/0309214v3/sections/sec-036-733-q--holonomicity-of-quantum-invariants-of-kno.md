---
doc_id: 0309214v3
doc_title: "The colored Jones function is q –holonomic"
section_id: sec-036-733-q--holonomicity-of-quantum-invariants-of-kno
section_title: "q--holonomicity of quantum invariants of knots"
section_number: 7.3.3
pages: 31-33
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
toc_source: outline
doc_brief: "The colored Jones function is q –holonomic — A function of several variables is called holonomic if, roughly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many linear"
---
First let us recall the deﬁnition of quantum knot invariant.
Using the braiding B: M(λ) →M(λ) one can deﬁne a representation of the
braid group τ : Bm →(M(λ))⊗m by putting
τ(σi) := id⊗i−1 ⊗B ⊗id⊗m−i−1 .
Let ρ denote the half-sum of positive roots. For an element x ∈U and an
U –module V , the quantum trace is deﬁned as
trq(x, V ) := tr(xK−2ρ, V ).
Suppose a framed knot K is obtained by closing a braid β ∈Bm. We would
say that the colored Jones polynomial is the quantum trace of τ(β). However,
since M(λ) is inﬁnite-dimensional, the trace may not make sense. Instead, we
will use a trick of breaking the knot. Let K′ denote the long knot which is the
closure of all but the ﬁrst strand of β.
Recall that τ(β) acts on (M(λ))⊗m. Let
τ(β)(λ)n′
1,...,n′
m
n1,...,nm ∈Z[v±1/D]
be the entries of the matrix τ(β)(λ). We will take partial trace by ﬁrst putting
n1 = n′
1 = 0 and then take the sum over all n2 = n′
2, . . . , nm = n′
m. The
following lemma shows that the sum is actually ﬁnite.
Lemma 7.7 Suppose n1 = 0. There are only a ﬁnite number of collections of
(n2, n3, . . . , nm) ∈Nt−1 such that
τ(β)(λ)n1,...,nm
n1,...,nm
is not zero.
Proof Let M′(λ) be the maximal proper U –submodule of M(λ).
Then
L(λ) = M(λ)/M′(λ) is a ﬁnite dimensional vector space. In particular it has
only a ﬁnite number of non-trivial weights. Hence, all except for a ﬁnite number
of fn, n ∈Nt, are in M′(λ).
We present the coeﬃcients B±(λ) graphically as in Figure 3.
Note that if (B±)m1,m2
n1,n2
is not equal to 0, then fm2 can be obtained from fn1
by action of an element in U , and similarly, fm1 can be obtained from fn2 by
action of an element in U . Thus if we move upwards along a string of the braid,
Geometry & Topology, Volume 9 (2005)
1284
Stavros Garoufalidis and Thang T Q Lˆe
Figure 3: (B+)m1,m2
n1,n2
and (B−)m1,m2
n1,n2
the basis element at the top can always be obtained from the one at the bottom
by an action of U .
Because the closure of β is a knot, by moving around the braid one can get any
point from any particular point. Because the basis element f0 is not in M′(λ),
we conclude that if
τ(β)(λ)n1,...,nm
n1,...,nm
is not 0, with n1 = 0, then all the basis vectors fn2, . . . , fnm are not in M′(λ),
and there are only a ﬁnite number of such collections.
R ecall that 2ρ is the sum of all positive roots. Let us deﬁne
JK′(λ) =
X
n2,...nm∈Nt,n1=0,
(K−2ρ τ(β)(λ))n1,...,nm
n1,...,nm.
From q–holonomicity of τ(β)(λ) it follows that JK′(λ) is q–holonomic. JK′(λ)
is a long knot invariant, and is related to the colored Jones polynomial JK of
the knot K by
JK(λ) = JK′(λ) × dimq(L(λ)),
where L(λ) is the ﬁnite-dimensional simple U –module of highest weight λ, and
dimq(L(λ)) is its quantum dimension, and is given by the formula
dimq(L(λ)) =
Y
α>0
v(λ+ρ,α) −v−(λ+ρ,α)
v(ρ,α) −v−(ρ,α)
.
Since dimq(L(λ)) is q–holonomic in λ, we see that JK(λ) is q–holonomic. This
completes the proof of Theorem 6.
Remark 7.8 The invariant JK′ of long knots is sometime more convenient.
For example, JK(λ) might contain fractional power of q, but (if K′ has framing
0,) JK′(λ) is always in Z[q±1], see [20]. Also the function JK′ can be extended
to the whole weight lattice.
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q–holonomic
1285
7.4
