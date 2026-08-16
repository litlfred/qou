---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and diﬀerential equations. From C to Cp Tˆohoku-Hokkaidˆo lectures in Arithmetic Geometry Yves Andr´ e (with appendices by F. Kato and N. Tsuzuki)"
section_id: sec-577-3-totaros-theorem-235
section_title: "TOTARO’S THEOREM. 235"
section_number: 3
pages: 239-240
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry Yves André (with appendices by F. Kato and N. Tsuzuki) — 580 sections: INTRODUCTION; INTRODUCTI"
---
maximal tori of P (λ)/U (λ) by the natural projection T ↦→T . Hence, the
invariant norm on G induces the one on P (λ)/U (λ). Fix a maximal torus
T of G. Since the image of λ is contained in the center of P (λ)/U (λ), the
perfect pairing associated to the invariant norm determine s the dual of λ
in X∗(T ). This dual can extend to a character ⊗Q of P (λ)/U (λ). Now we
deﬁne a G-line bundle⊗Q,Lλ, onFλ by the associated one to the negative
of the dual character ⊗Q of λ. By construction, the line bundle ⊗Q, Lλ,
depends only on the conjugacy class of λ and is ample.
Let J be a smooth aﬃne group scheme over Qp such that
J(Qp) ={g∈G(K0)| g(bσ) = (bσ)g}
(which is introduced in [ RZ96]). Since JK0⊂ GK0, the pull back Lλ ˘E of
Lλ onFλ ˘E is an ample J ˘E-line bundle.
By the same construction as above, ν in 2.2 gives a character ⊗Q of
P (ν). The opposite of this character ⊗Q determines a J ˘E-action⊗Q on the
trivial line bundle on Fλ ˘E since JK0⊂P (ν). We denote it by L0
ν.
We put a J ˘E-line bundle⊗Q, L =Lλ ˘E⊗L0
ν, onFλ ˘E. Then it is ample
and depends only on b and the conjugacy class of λ. We denote by F ss
λ (L)
the set of semistable points in Fλ with respect to L in the sense of D.
Mumford [ MFK94].
Theorem 3.6. [T ot96] Suppose thatG is connected and reductive. For any
ﬁnite extension K of ˘E, we have
F wa
λ,b (K) =F ss
λ ˘E(L)(K).
We shall sketch Totaro’s proof. First, let G =GL(n) and let us consider
the invariant norm induced by the pairing
(α,β ) =
∑
i,j
ij dim
K 0 gri
F .
α
grj
F .
β
(K n)
for one-parameter subgroups⊗Q,α,β ofGL(n) overK. If one puts µα(V ) =
(
∑
i
i dimK gri
F .
α
(V⊗K))/ dim V , then one has
(α,β ) =
∫
(µα(F j
β )−µα(V )) dimKF j
βdj +µα(V )µβ(V ) dim V.
So, (ξ,b ) is weakly admissible if and only if ( ξ,α ) + (ν,α ) ≤ 0 for any
one-parameter subgroup α of GL(n) over K0 with the ﬁltration F .
α as
subisocrystals. In other words, ( ξ,b ) is weakly admissible if and only if
(ξ,α ) + (ν,α )≤ 0 for any one-parameter subgroup α of J over Qp. Hence,
the assertion follows from the calculation of Mumford’s num erical invariant
below.
Lemma 3.7. If µ(ξ,α,L ) is Mumford’s numerical invariant of ξ∈F λ for a
one-parameter subgroupα of J over Qp, then
µ(ξ,α,L ) =−(ξ,α )− (ν,α ).
236 C. p-ADIC SYMMETRIC DOMAINS AND TOTARO’S THEOREM
Next, let G be arbitrary,V a faithfully representation of G, and consider
the invariant norm onG induced from the above norm by the natural immer-
sionG→GL(V ). The Mumford’s numerical invariant of weakly admissible
points is non-negative for any one-parameter subgroup of J(GL(V )). Hence
it is so for any one-parameter subgroup of J, and the weak admissibility
implies the semistability. To see the converse, one needs to show that, if
ξ∈F ss
λ (L)(K), (ξ,α ) + (ν,α )≤ 0 for any one-parameter subgroup α of
J(GL(V )) over Qp. If α is semistable for the GK -line bundle Lα onFα, the
assertion follows from the ﬁrst part. In the case where α is not semistable,
one can use Kempf’s ﬁltration [ Kem78] and Ramanan and Ramanathan’s
work [RR84], and obtains the required inequality.
Finally one needs to prove the independence of the choice of t he norm.
Suppose that the identity is valid for the particular norm. S ince G is a
quotient of a product of a torus and some simple algebraic gro ups by a
ﬁnite central subgroup [ BT65], one can reduce the assertion in the case of
tori and simple groups. In the case of tori it was proved in [ RZ96], and in
the case of simple groups it is true since the norm of the simpl e group comes
from the Killing form up to a positive rational multiple. □
4. p-adic symmetric domains.
Let k be the algebraic closure of the prime ﬁeld Fp, Cp the p-adic com-
pletion of a ﬁxed algebraic closure Qp of Qp, and K0 = ˆQur
p the p-adic
completion of the unramiﬁed extension in Cp.
