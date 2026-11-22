---
doc_id: du-fu-quantum-gln-qschur-survey
doc_title: "QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR"
section_id: page-016
section_title: "Page 16"
section_number: null
pages: 16-16
source_pdf: du-fu-quantum-gln-qschur-survey.pdf
source_sha256: 6852134eaffb3137
toc_source: undetermined
doc_brief: "Quantum gl_n, q-Schur algebras and their infinite/infinitesimal counterparts — We present a survey of recent developments of the Beilinson–Lusztig–MacPherson approach in the study of quantum gln"
---
16
JIE DU AND QIANG FU
orthogonal idempotent elements labelled by the elements in the set Λ([−n, n], r). This fact
is useful in the proof of Theorem 8.2.
(2) It is interesting to point out that the Doty-Giaguinto type presentation described in
Theorem 6.1(1) does not exist for V(∞, r).
9. Infinite q-Schur algebras and their elementary structure
In this section, we ﬁrst introduce the q-Schur algebra S(η, r) at η. We will mainly focus
on the structure of inﬁnite q-Schur algebras.
Let H be the Hecke algebra over Z associated with the symmetric group Sr on r letters.
Then H as a Z-algebra has a basis {Tw}w∈Sr subject the relations (cf. Theorem 6.7): for all
w ∈Sr and s ∈S := {(i, i + 1) | 1 ⩽i ⩽n −1},
TsTw =
(
Tsw,
if sw > w,
(v −v−1)Tw + Tsw,
if sw < w.
Let H = H ⊗Q(v).
Let η be a consecutive segment of Z. Let Ωη be a free Z-module with basis {ωi}i∈η and
let Ωη = Ωη ⊗Q(v). H acts on Ω⊗r
η
from the right by “place permutations”:
(ωi1· · · ωir)T(j,j+1) =





ωi1· · · ωij+1ωij· · · ωir,
if ij <ij+1;
vωi1· · · ωir,
if ij =ij+1;
(v−v−1)ωi1· · · ωir + ωi1· · · ωij+1ωij· · · ωir,
if ij >ij+1.
The algebras
S(η, r) := EndH(Ω⊗r
η ),
S(η, r) := EndH(Ω⊗r
η )
are called q-Schur algebras at η.
Note that S(n, r) := S(η, r) for η = [1, n] is the q-
Schur algebra we discussed before. Clearly,, if η is ﬁnite, S(η, r) ∼= S(|η|, r) and S(η, r) ∼=
S(η, r) ⊗Z Q(v). When η = Z, the algebras S(∞, r) := S(Z, r) and S(∞, r) are called
inﬁnite q-Schur algebras.
Since the H-action commutes with the action of U(η), it follows that U(η, r) ⊆S(η, r).
Hence, we obtain algebra homomorphisms
(9.0.1)
ζr : U(η) →S(η, r),
ζr|U(η) : U(η) →S(η, r).
These homomorphisms are surjective whenever η is ﬁnite. In particular, we have U(n, r) =
S(n, r) and U(n, r) = S(n, r) for all n, r ⩾1.
Since Ω⊗r
[−n,n] is a direct summand of the H-submodule Ω⊗r
[−n−1,n+1] for all n ⩾1, it follows
that we may embed S([−n, n], r) as a centralizer subalgebra of S([−(n+1), n+1], r). Hence,
we obtain a direct limit system {S([−n, n], r)}n⩾1. By Lemma 3.1(2), we have
K(∞, r) ∼= lim
−→
n
S([−n, n], r),
K(∞, r) ∼= lim
−→
n
S([−n, n], r).
This isomorphism implies immediately the second isomorphism in the following.
