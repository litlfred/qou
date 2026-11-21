---
doc_id: du-fu-quantum-gln-qschur-survey
doc_title: "QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR"
section_id: page-008
section_title: "Page 8"
section_number: null
pages: 8-8
source_pdf: du-fu-quantum-gln-qschur-survey.pdf
source_sha256: 6852134eaffb3137
toc_source: undetermined
doc_brief: "Quantum gl_n, q-Schur algebras and their infinite/infinitesimal counterparts — We present a survey of recent developments of the Beilinson–Lusztig–MacPherson approach in the study of quantum gln"
---
8
JIE DU AND QIANG FU
(2) There is an algebra monomorphism ι : U(η) →bK(η) satisfying
Eh 7→Eh,h+1(0), Kj1
1 Kj2
2 · · · Kjn
n 7→0(j), Fh 7→Eh+1,h(0).
Hence, im(ι) = V(η).
(3) For any positive integer r, there is an algebra homomorphism ξr : U(η) →bK(η, r)
satisfying
Eh 7→Eh,h+1(0, r), Kj1
1 Kj2
2 · · · Kjn
n 7→0(j, r), Fh 7→Eh+1,h(0, r)
such that V(η, r) = im(ξr) is a subalgebra of bK(η, r). In particular, V(η, r) is gener-
ated by the elements Eh,h+1(0, r), Eh+1,h(0, r), and 0(j, r) for all h ∈η⊣and j ∈Nη.
(4) By identifying U(η) with V(η) via ι, the algebra homomorphism ξr in (3) satisﬁes
ξr(A(j)) = A(j, r), for any A ∈Ξ±(η), j ∈Zη.
Remarks 4.2. (1) From Theorem 4.1(2), U(η) ∼= V(η) gives a realization of quantum glη.
This realization provides explicit multiplication formulas between the generators and basis
elements A(j); see [1, 5.3] and [7, 4.2].
(2) It is known U(η, r) ∼= V(η, r) if η is ﬁnite. We shall see in §9 that U(∞, r) ∼= V(∞, r).
In particular, V(∞, r) is a realization of U(∞, r).
5. Constructions of uk(η)
In this section, we discuss the realizations of ˜uk(η) and uk(η). As set in §2, k is a ﬁeld
and ε ∈k is an l′th primitive root of 1.
Let eΞl(η) be the set of all A = (ai,j) ∈eΞ(η) such that ai,j < l for all i̸ = j. Let eΞ±
l (η) be
the set of all A ∈eΞl(η) whose diagonal entries are zero. Let Ξl,l′(η) be the set of all n × n
matrices A = (ai,j) with ai,j ∈N, ai,j < l for all i̸ = j and ai,i ∈Zl′ := Z/l′Z for all i. We
have an obvious map pr : eΞl(η) →Ξl,l′(η) deﬁned by reducing the diagonal entries modulo
l′.
Let K(η)k = K(η)⊗Z k. Mimicking the construction of bK(η), we deﬁne bK(η)k to be the k-
vector space of all formal (possibly inﬁnite) k-linear combinations P
A∈eΞ(η) βA[A] satisfying
the property (4.0.2) with a similar multiplication. This is an associative algebra with an
identity: the sum of all [D] with D a diagonal matrix in eΞ(η). The elements A(j) deﬁned
earlier becomes
A(j) =
X
z∈Zn
εj·z[A + diag(z)] ∈bK(η)k,
where j · z = Σijizi. Clearly, A(j) = A(j′) whenever ¯j = ¯j′. Here ¯ : Zη →(Zl′)η is the map
deﬁned by (j1, j2, · · · , jn) = ( ¯j1, ¯j2, · · · , ¯jn). Thus, we shall write A(¯j) := A(j). Similarly, we
shall use A(¯j, r) := A(j, r) to denote the element deﬁned earlier with υ replaced by ε for the
q-Schur algebra U(n, r)k = U(n, r) ⊗Z k over k.
Let W be the subspace of bK(η)k spanned by
Bk = {A(¯j) | A ∈eΞ±
l (η),¯j ∈(Zl′)n}.
We have clearly dim W ⩽(l′)nln2−n if |η| = n.
