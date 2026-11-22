---
doc_id: du-fu-quantum-gln-qschur-survey
doc_title: "QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR"
section_id: page-012
section_title: "Page 12"
section_number: null
pages: 12-12
source_pdf: du-fu-quantum-gln-qschur-survey.pdf
source_sha256: 6852134eaffb3137
toc_source: undetermined
doc_brief: "Quantum gl_n, q-Schur algebras and their infinite/infinitesimal counterparts — We present a survey of recent developments of the Beilinson–Lusztig–MacPherson approach in the study of quantum gln"
---
12
JIE DU AND QIANG FU
We call M an integral monomial basis. This basis leads to several other bases for U(n, r)
which we now describe.
Fix the reduced expression
(6.4.1)
i = (i1, i2, · · · , iν) = (n −1, · · · , 2, 1, · · · , n −1, n −2, n −1)
of the longest word w0 of the symmetric group Sn, that is, w0 = si1si2 · · · siν. For any
c = (c1, · · · , cν) ∈Nν, deﬁne monomials in root vectors Ec
i and F c
i as in [19, 2.2] (using
braid group actions). Let ec
i = ζr(Ec
i ) and fc
i = ζr(F c
i ).
For any A ∈Ξ±(n), let c(A+) = (c1, · · · , cν) ∈Nν, where the ﬁrst n −1 components of
c(A+) is the n-th column of A+ reading upwords, and the next n −2 components is the
(n −1)-th column and so on, i.e.,
c1 = an−1,n, · · · , cn−1 = a1n, cn = an−2,n−1, · · · .
Deﬁne c(A−) symmetrically.
Theorem 6.5 ([8],[13]). We list the following Q(v)-bases for the q-Schur algebra U(n, r).
Let i0 be a ﬁxed integer with 1 ⩽i0 ⩽n.
(1) The monomial basis:
Ni0 =
n
e(A+)kjf(A−)  A ∈Ξ±(n), j ∈Nn, ji0 = 0, |j| + |A| ⩽r
o
;
(2) The BLM basis:
Bi0 =

A(j, r)
 A ∈Ξ±(n), j ∈Nn, ji0 = 0, |j| + |A| ⩽r
	
;
(3) The PBW basis:
Pi0 =

ec(A+)
i
kjfc(A−)
i
 A ∈Ξ±(n), j ∈Nn, ji0 = 0, |j| + |A| ⩽r
	
.
We end this section with an application.
We identify the Hecke algebra part of the
monomial basis M. We assume now n = r though all results hold for n ⩾r. Let̟
= (1, 1, · · · , 1) ∈Nn,
and let H = k̟ U(n, n)k̟
and H = k̟ U(n, n)k̟ . For any w ∈Sn, let Aw ∈Ξ(n, n) be
the permutation matrix deﬁned inductively by Aw = AyAsi, where w = ysi with y < w and
si = (i, i + 1) for some i.
Lemma 6.6 ([9, 9.1]). The algebra H is free over Z with basis
M̟
= {m(Aw) | w ∈Sn}.
Let Ci = m(Asi) = e(A+
si)kσ(Asi)f(A−
si), and let Ti = Ci −v−1.
Theorem 6.7 ([9, 9.3-4]). (1) The elements Ti, 1 ⩽i ⩽n−1, satisfy the following relations:





(a)
(Ti −v)(Ti + v−1) = 0;
(b)
TiTj = TjTi,
|i −j| > 1;
(c)
TiTi+1Ti = Ti+1TiTi+1, 1 ⩽i ⩽n −2.
In particular, Ti is invertible and T −1
i
= Ci −v.
