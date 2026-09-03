---
doc_id: arxiv-2406.05311v1
doc_title: "A QUANTUM MURNAGHAN\u2013NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: A_quantum_Murnaghan--Nakayama_rule_for_the_flag_ma.pdf
source_sha256: c431fca150329547
doc_brief: "A QUANTUM MURNAGHAN–NAKAYAMA RULE FOR THE FLAG MANIFOLD C. BENEDETTI, N. BERGERON, L. COLMENAREJO, F. SALIOLA, AND F. SOTTILE — 5 sections: Introduction; A Murnaghan–Nakayama rule for (cla; A Murnagha"
---
The Murnaghan–Nakayama rule is a method for computing values of the irreducible characters of symmetric groups [29, 30, 31]. Under the identification of the character ring with
the ring of symmetric functions, it translates into a rule for the multiplication of a Schur
symmetric function by a Newton power sum. As explained in [28, Sect. 2], in the cohomology
ring of a Grassmannian, the Murnaghan–Nakayama formula is a formula for the intersection
product of a Schubert variety with a component of the Chern character of the tautological
bundle (a tautological class), as these tautological classes are essentially Newton power sums.
Consequently, any formula describing multiplication by a tautological class will also be called
a Murnaghan–Nakayama rule.
Murnaghan–Nakayama rules have been described for many different algebras that carry a
notion of a Newton power sum. Fomin and Green gave a version for noncommutative symmetric functions, which led to formulas for characters of representations associated to stable
Schubert and Grothendieck polynomials [14]. Assaf and McNamara gave a skew version [1],
which Konvalinka generalized to a skew rule for multiplication by a ‘quantum’ (perturbed
by a parameter q) power sum function [20]. Bandlow, et al. gave a version in the cohomology of an affine Grassmannian [2], and Lee gave a version in the cohomology of the affine
flag manifold [22]. Tewari gave a version for noncommutative Schur functions [37], and Berg
et al. for the immaculate noncommutative symmetric functions [5]. Wildon gave a plethystic version [38]. Ross gave a version for loop Schur functions [34], providing a fundamental
step in the orbifold Gromov–Witten/Donaldson–Thomas correspondence [35]. Morrison and
Sottile gave Murnaghan–Nakayama rules in the cohomology ring of a flag manifold and in
the quantum cohomology of the Grassmannian [28]. Khanh, et al. gave a version in the
Grothendieck ring of the Grassmannian [19]. Khanh also gave a version for K-k-Schur and
k-Schur functions [18], generalizing [2]. Fan, et al. gave a Murnaghan–Nakayama formula for
Chern–Schwartz–MacPherson classes of Schubert cells in the flag variety [12].
2010 Mathematics Subject Classification. 05E05, 14N15.
Key words and phrases. Murnaghan–Nakayama rule, Schubert calculus, Schubert polynomials, quantum
cohomology.
1


QUANTUM MURNAGHAN–NAKAYAMA RULE

2

We first derive a formula for the multiplication of a Schubert polynomial by a hook Schur
polynomial and use this to give a new proof of the Murnaghan–Nakayama formula in the
cohomology of a flag variety that was originally derived in [28]. This hook multiplication
formula is related to the formula of Mészáros et al. [25, Thm. 2], but it does not use the
noncommutative Fomin–Kirillov algebra [15].
Our main result (Corollary 3.3) is a Murnaghan–Nakayama rule in the small quantum
cohomology ring of the flag manifold, proving a formula conjectured by Morrison at FPSAC
2014 [27]. This follows from a formula (Theorem 3.2) for multiplication by a quantum Schur
polynomial indexed by a hook partition. Mészáros et al. [25, Thm. 15] also gave a formula
for multiplication by a hook quantum Schur polynomial, which would imply our formula.
Unfortunately, their proof is not valid, as we explain in Section 3.5—this necessitates the
arguments we give. Our arguments involve a detailed analysis of chains and intervals in the
quantum Bruhat order, a partial order relevant to multiplication in the quantum cohomology
of a flag manifold. We also use the “quantum-equals-classical” result of Leung and Li [23]
as well as Postnikov’s cyclic symmetry [33] to show that structure constants for quantum
products by hook quantum Schur polynomials are equal to structure constants for the classical
product from [36], and thereby deduce our results.
In Section 2 we develop some background on the flag variety and Bruhat order, giving a new
proof of the Murnaghan–Nakayama formula in the cohomology of the flag variety. Section 3
develops background on the quantum cohomology ring of the flag variety, and gives a proof of
the Murnaghan–Nakayama formula in this setting, which relies on results established in two
subsequent sections. We extract some results of Leung and Li [23] in Section 4, including a
version of their “quantum-equals-classical” result (Lemma 4.4). The final Section 5 develops a
detailed combinatorics of chains in the quantum Bruhat order to prove the second result used
in our proof of the quantum Murnaghan–Nakayama rule (Theorem 5.1). It is the technical
heart of this paper.
A theme in the paper [6] is the relation between intervals in the k-Bruhat order ≤k (a
suborder of the Bruhat order on Sn ) and Littlewood–Richardson coefficients cw
u,v when v
is a Grassmannian permutation. For example, the isomorphism type of an interval [u, w]k
−1
in the k-Bruhat order only depends upon wu−1, and cw
u,v also only depends upon wu
when v is Grassmannian. Only substantially weaker versions of these and related results
hold for quantum cohomology. While an interval [u, q α w]qk in the quantum k-Bruhat order
(see Section 3.2) is not determined by wu−1, its isomorphism type is preserved by some
operations including a cyclic shift (Corollary 5.14) that is related to Postnikov’s cyclic shift
and is distinct from the cyclic shift in [6] (which does not preserve isomorphism type). When v
w,α
is Grassmannian, we show that the numerical part Nu,v
of a quantum Littlewood–Richardson
−1
coefficient (see Section 4) only depends upon wu (but q α may change); this is Theorem 4.6.
Remark 1.1. The results of this paper were announced in a published FPSAC conference
abstract [3]. Here, we provide all the proofs, clarify some definitions and statements, and
correct typos.
