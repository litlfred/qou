---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-008-23-interpretation-in-the-representation-theory-o
section_title: "Interpretation in the representation theory of GLn(Fq)"
section_number: 2.3
pages: 7-8
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
q). If q = pe is a power of a prime
number, the previous identities may be interpreted in the se tting of the representation theory of the
group of invertible n × n matrices GL(n, /BY
q). Indeed, it is a well-known fact [ Iwa64] that the relations
deﬁning Hn,q are those of the convolution algebra
/BV [B(n, /BY
q)\GL(n, /BY
q)/B(n, /BY
q)] = {f ∈ /BV [GL(n, /BY
q)] | ∀ b, b′ ∈ B(n, /BY
q), f (bgb′) = f (g)} ,
where B(n, /BY
q) is the Borel subgroup of GL(n, /BY
q), containing the invertible upper-triangular matrices.
Now, consider the GL(n, /BY
q)-module of functions on the ﬂag variety GL(n, /BY
q)/B(n, /BY
q) — or, in
other words, right B(n, /BY
q)-invariant complex functions on GL(n, /BY
q). Since GL(n, /BY
q) acts transitively
on the ﬂag variety, a GL(n, /BY
q)-endomorphism u of this module is entirely determined by a function
h ∈ /BV [GL(n, /BY
q)] such that:
u(/BD
B(n, /BY
q)) =
∑
g∈G
h(g) /BD
g.
8 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
Moreover, the condition u ∈ EndGL(n, /BY
q)
/BV [GL(n, /BY
q)/B(n, /BY
q)] implies that h is left and right B(n, /BY
q)-
invariant. As a consequence, we have an isomorphism
Hn,q
iso
≃ /BV [B(n, /BY
q)\GL(n, /BY
q)/B(n, /BY
q)]
iso
≃ EndGL(n, /BY
q)
/BV [GL(n, /BY
q)/B(n, /BY
q)],
whence a decomposition of the (GL(n, /BY
q), Hn,q)-bimodule /BV [GL(n, /BY
q)/B(n, /BY
q)] similar to the classical
Schur-Weyl duality between GL(n, /BV ) and Sn:
GL(n, /BY
q)↷
{
/BV [GL(n, /BY
q)/B(n, /BY
q)]
}
↶ Hn,q
=
∑
λ∈Yn
Uλ(q) ⊗
/BV
Sλ(q).
The Uλ(q) are called unipotent modules of GL(n, /BY
q). Each Uλ(q) is irreducible and of complex dimension
dim Uλ(q) = Dλ(q) = qb(λ) {n!}q∏
/oblong∈λ{h(/oblong)}q
.
Thus, the natural probability measure Mn,q on the set of characters of Hn,q is also the natural probability
measure on the set of unipotent characters of GL(n, /BY
q). Moreover, the regular trace τq is just the restric-
tion of the normalized trace of End
/BV
/BV [GL(n, /BY
q)/B(n, /BY
q)] to the subalgebra of GL(n, /BY
q)-morphisms,
that is to say, Hn,q.
Remark 2. In a much more general context, given a (connected, non-twis ted) Chevalley group GF over
/BY
q and a cuspidal irreducible character ρ of a Levi subgroup LF , the decomposition in irreducibles of the
GF -module RGF
LF (ρ) obtained by parabolic induction yields a probability measu re on the set of characters
of a multiple-parameter Hecke algebra of the ramiﬁcation gr oup
W (ρ) = {w ∈ Norm(LF )/LF | ρ ◦ w = ρ}.
This ramiﬁcation group is a Coxeter group and a subgroup of th e relative Weyl group N (LF )/LF ;
moreover, the multiple-parameter Hecke algebra is in fact i somorphic to the group algebra /BV W (ρ) (see
[HL80, Lus84, Gec93]), so the probability measure is in fact over the isomorphis m classes of irreducible
representations of W (ρ). The case we are studying in this paper is when GF = GL( n, /BY
q), LF = ( /BY
q)n,
ρ = 1 is the trivial character and W (ρ) = W = Sn.
3. Obser v ables of diagrams
In this section, we introduce the algebra of observables of d iagrams O. This subalgebra of the algebra
of functions on the set of all Young diagrams Y = ⨆
n∈ /C6
Yn is isomorphic to the algebra of (complex)
symmetric functions, and it is known to be a powerful tool in t he setting of asymptotic representation
theory of symmetric groups, see [ IO02]. In this paper, the authors introduced four algebraic base s of
O: the power sums (pk)k≥1 in the Frobenius coordinates, the power sums (~pk)k≥2 in the interlacing
