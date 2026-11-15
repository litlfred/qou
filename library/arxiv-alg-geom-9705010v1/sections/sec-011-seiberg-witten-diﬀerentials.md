---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-011-seiberg-witten-diﬀerentials
section_title: "Seiberg-Witten Diﬀerentials"
section_number: null
pages: 18-19
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
In the Seiberg-Witten picture of super Yang-Mills, there are the charges ai and
aD
i which are described locally as holomorphic functions on the quantum moduli
space B. There is less ambiguity in choosing these ai, aD
i
than in the coordinates
zi, wi on the base of an algebraically integrable system: the group of their linear
combinations Σniai + nD
i aD
i
(with integer coeﬃcients ni) should be uniquely de-
termined in the pure SYM case, and determined modulo the masses of the added
particles in general. A natural way to get functions with precisely such ambiguity
on the base of an integrable system π : X →B is to choose a meromorphic diﬀer-
ential 1-form λ on X and let ai, aD
i be its periods over a set of 1-cycles representing
αi, βi respectively and avoiding the poles of λ. We want ai, aD
i
to be a possible
choice of the coordinates zi, wi, which are deﬁned up to translation (once we have
ﬁxed the αi, βi). In other words, we want
dai = dzi,
daD
i = dwi.
Since dzi, dwi were deﬁned as the contraction of αi, βi respectively with the sym-
plectic form σ, the condition becomes simply:
dλ = σ.
The behavior of the singularities of λ is constrained by this condition.
When
restricted to a general ﬁber Xb, λ will have poles along the union of some irreducible
divisors Db,j. One constraint is that the residue Resj of λ along Db,j is (locally
in B) independent of b. A Seiberg-Witten diﬀerential is a meromorphic 1-form λ
satisfying dλ = σ and Resj = mj, the mass of the j-th particle. On an algebraically
SEIBERG-WITTEN INTEGRABLE SYSTEMS
19
integrable system with a speciﬁed Seiberg-Witten diﬀerential, the local coordinates
zi, wi can be speciﬁed as the charges ai, aD
i , with just the right ambiguity.
One way to describe an integrable system (though by no means the only way!)
is in terms of a family C →B of spectral curves Cb. In the simplest situation,
the abelian varieties Xb are just the Jacobians J(Cb). More generally, Xb may
be realized as the Prym of Cb with respect to an involution, or as the generalized
Prym with respect to a correspondence, cf. [D1]. An example of such a system,
due to Mukai [Mu], is obtained from the Jacobians of a complete linear system
C →B of curves on a symplectic surface (S, ¯σ). The symplectic form σ on X
then corresponds via Abel-Jacobi to the pullback to C of ¯σ. Mukai studied the case
where S is a K3 surface. Taking S = T ∗E to be the cotangent bundle of some curve
E yields Hitchin’s system on E. One obtains many more examples by allowing S
to have a symplectic form ¯σ0 deﬁned only on an open subset S0 ⊂S, and imposing
appropriate restrictions on the intersection of the spectral curves Cb with S −S0.
For example, we can take S to be the total space of the line bundle ωE(D) for
some eﬀective divisor D on E, to recover Markman’s system [Mn] parametrizing
meromorphic Higgs bundles on E. Note that this S has a natural meromorphic 1-
form ¯λ, given away from D (i.e. where S can be identiﬁed with T ∗E) as the action
1-form ¯λ = pdq, whose diﬀerential is d¯λ = ¯σ0. It follows that the “tautological” 1-
form on C (pullback of ¯λ) induces the Seiberg-Witten diﬀerential λ on the integrable
system X = J(C/B) →B. The system discussed in §3 is of this form.
