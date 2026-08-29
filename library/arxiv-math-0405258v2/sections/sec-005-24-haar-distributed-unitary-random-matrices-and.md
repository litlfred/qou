---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-005-24-haar-distributed-unitary-random-matrices-and
section_title: "Haar distributed unitary random matrices and the Weingarten function"
section_number: 2.4
pages: 6-7
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
garten function. In the following we will be interested in the asymp-
totics of special matrix integrals over the group U(N) of unitary N ×N-
matrices. We always equip the compact group U(N) with its Haar
probability measure and accordingly distributed random matrices we
shall call Haar distributed unitary random matrices . Thus the expec-
tation E over this ensemble is given by integrating with respect to the
Haar measure.
The expectation of products of entries of Haar distributed unitar y
random matrices can be described in terms of a special function on t he
permutation group. Since such considerations go back to Weingart en
[W], Collins [C] calls this function the Weingarten function and denotes
it by Wg. We will follow his notation. In the following we just recall the
relevant information about this Weingarten function, for more det ails
we refer to [C, C ´S, X].
We use the following deﬁnition of the Weingarten function. For
π ∈ Sn and N ≥ n we put
Wg(N, π) = E
(
U11 · · · Unn
U 1π(1) · · · U nπ(n)
)
,
where U = (Uij)N
i,j=1 is an N ×N Haar distributed unitary random ma-
trix. Sometimes we will suppress the dependence on N and just write
Wg(π). This Wg( N, π) depends on π only through its conjugacy class.
FLUCTUATIONS OF UNITARY RANDOM MATRICES 7
General matrix integrals over the unitary groups can be calculated as
follows:
(3) E
(
Ui′
1j′
1 · · · Ui′
nj′n
U i1j1 · · · U injn
)
=
∑
α,β∈Sn
δi1i′
α(1)
· · · δini′
α(n)
δj1j′
β(1)
· · · δjnj′
β(n)
Wg(βα −1).
The Weingarten function is a quite complicated object, and its full
understanding is at the basis of questions around Itzykson-Zube r inte-
grals. For our purposes, only the behaviour of leading orders in N of
Wg(N, π) is important. One knows (see, e.g., [C, C ´S]) that the leading
order in 1 /N is given by |π| + n and increases in steps of 2.
Let us use the following notation for the ﬁrst two orders ( π ∈ S(n)):
Wg(N, π) = µ(π)N −(|π|+n) + φ(π)N −(|π|+n+2) + O
(
N −(|π|+n+4))
.
One knows that µ is multiplicative with respect to the cycle decom-
position, i.e.,
µ(π1 × π2) = µ(π1) · µ(π2).
The important part of the second order information is contained in
the leading order of Wg( π1 × π2) − Wg(π1)Wg(π2), which is given by
µ2(π1, π2)N −(|π1|+|π2|+m+n+2) for π1 ∈ Sm and π2 ∈ Sn and where
µ2(π1, π2) := φ(π1 × π2) − µ(π1)φ(π2) − φ(π1)µ(π2).
Note that we have
µ2(π1, π2) = µ2(π2, π1).
Collins [C] has general counting formulas for the calculation of µ and µ2
(and also higher order analogues); however, a conceptual explan ation
of µ2 seems still to be missing. µ is the M¨ obius function of the lattice
of non-crossing partitions (thus determined by Catalan numbers) , and
this fact is quite well understood by the relation between µ and asymp-
totic freeness of unitary random matrices. In a similar way, one sho uld
get a conceptual understanding of µ2 by the relation with second order
freeness. In the present paper we will not pursue further this dir ection,
but we will come back to it in forthcoming investigations. Here we will
not rely on the concrete values of µ or µ2, but will only use the basic
properties mentioned above.
