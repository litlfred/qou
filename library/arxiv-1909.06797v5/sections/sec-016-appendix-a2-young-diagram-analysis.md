---
doc_id: arxiv-1909.06797v5
doc_title: "Quantum Mechanics of Plancherel Growth"
section_id: sec-016-appendix-a2-young-diagram-analysis
section_title: "Appendix A.2 Young diagram analysis"
section_number: null
pages: 27-28
source_pdf: 1909.06797v5.pdf
source_sha256: 87095d7e46ebe286
toc_source: outline
doc_brief: "Quantum Mechanics of Plancherel Growth — Growth of Young diagrams, equipped with Plancherel measure, follows the automodel equation of Kerov."
---
The exponential appearing in the partition function of the single plaquette model can be expanded
into an inﬁnite series which runs over representations R of unitary group U(N),
Z =
X
R
X⃗
k
ε(⃗β,⃗k)
z⃗k
X⃗
l
ε(⃗β,⃗l)
z⃗l
χR(C(⃗k))χR(C(⃗l)).
(A.5)
Here χR(C(⃗k)) is the character of conjugacy class C(⃗k) of permutation group S K, K = P
n nkn
and
ε(⃗β,⃗k) =
∞
Y
n=1
Nknβkn
n ,
z⃗k =
∞
Y
n=1
kn!nkn.
(A.6)
Sum of representations of S U(N) can be written as a sum over diﬀerent Young diagrams. Say,
ni is the number of boxes in the i-th row of the Young diagram. We decompose the sum over
representations as a sum over all possible Young diagrams that one can draw for the symmetric
group. We introduce N new variables which are deﬁned as:
hi = ni + N −i
∀
i = 1, · · · , N.
(A.7)
hi’s are called hook numbers and they satisfy the following constraint
h1 > h2 > · · · > hN ≥0.
(A.8)
In terms of the new variables hi, the partition function (A.5) is therefore given by,
Z =
X
{hi}
X⃗
k,⃗l
ε(⃗β,⃗k)ε(⃗β,⃗l)
z⃗kz⃗l
χ⃗h(C(⃗k))χ⃗h(C(⃗l))
(A.9)
where⃗h denotes a particular representation.
As before we deﬁne continuous variables in the large N limit
hi
N = h(x),
kn = N2k′
n,
x = i
N
with
x ∈[0, 1].
(A.10)
27
Writing characters χ⃗h in terms of h(x) and k′
n, partition function (A.5), in large N limit, can be
written as
Z =
Z
[dh(x)]
Y
n
Z
dk′
ndl′
n exp
h
−N2S h
e f f[h(x),⃗k′
n,⃗l′
n]
i
,
(A.11)
where S h
e f f is the eﬀective action in Young diagram basis. Dominant contribution to partition
function comes from those representations which minimise the eﬀective action S h
e f f. To ﬁnd the
most dominant representations at large N, we introduce a function called Young tableaux density
deﬁned as,
u(h) = −dx
dh.
(A.12)
Thus we see that the unitary matrix model under consideration can be expressed in two diﬀerent
basis - eigenvalue basis (picture I) and Young diagram basis (picture II). Diﬀerent large N phases
can be characterised either by distributions of eigenvalues or Young diagrams. Therefore it is
expected that there is a relation between these two pictures. We now discuss this relation.
