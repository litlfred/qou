---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
The classical Murnaghan–Nakayama rule provides an efficient recursive method to compute the values
of irreducible characters of symmetric groups. This method can be adapted to the finite general linear
and unitary groups, where it then allows to compute values of unipotent characters not on arbitrary but
just on regular semisimple elements, see [10, Prop. 3.3]. This adaptation uses the fact that the unipotent
characters of general linear groups coincide with Lusztig’s so-called almost characters and then applies
the Murnaghan–Nakayama rule for the symmetric group.
In the present paper, we derive a Murnaghan–Nakayama rule for the values of unipotent characters
of the finite classical groups on regular semisimple elements, see Theorem 3.3. Our approach here is not
via a corresponding formula for the underlying Weyl group (of type Bn or Dn ), since for classical groups
Lusztig’s Fourier transform is non-trivial and thus the relation between almost characters and unipotent
characters becomes quite tricky. Instead we combine Asai’s result expressing the decomposition of Lusztig
induction in terms of hooks and cohooks of symbols and which already has a Murnaghan–Nakayama like
form, with Lusztig’s character formula.
As a first application we derive a vanishing result for irreducible characters of quasi-simple groups on
ℓ-singular elements:
Theorem 1. Let ℓ > 2 be a prime and G a finite quasi-simple group of ℓ-rank at least 3. Then for any
non-trivial character χ ∈ Irr(G) there exists an ℓ-singular element g ∈ G with χ(g) = 0, unless either G
is of Lie type in characteristic ℓ, or ℓ = 5 and one of:
(1) G = L5 (q) with 5||(q − 1) and χ is unipotent of degree χ(1) = q 2 Φ5 ;
(2) G = U5 (q) with 5||(q + 1) and χ is unipotent of degree χ(1) = q 2 Φ10 ;
(3) G = Ly and χ(1) ∈ {48174, 11834746}; or
(4) G = E8 (q) with q odd, dℓ (q) = 4 and χ one character in the Lusztig-series of type D8 .
Received by the editors August 24, 2018.
2010 Mathematics Subject Classification. Primary 20C20; Secondary 20C33,20C34 .
Key words and phrases. Murnaghan–Nakayama rule, classical groups, simple endotrivial modules, Loewy length, zeroes
of characters.
The second author gratefully acknowledges financial support by ERC Advanced Grant 291512.
c XXXX American Mathematical Society

1


2

FRANK LÜBECK AND GUNTER MALLE

The second main ingredient in the proof, apart from our Murnaghan–Nakayama formula, is a result
asserting the existence of ℓ-singular regular semisimple elements in classical groups of Lie type (see
Lemma 2.1) which may be of independent interest.
We then apply this vanishing result in order to classify simple endotrivial modules over fields k of
positive characteristic ℓ for finite classical groups.
Theorem 2. Let G be a finite quasi-simple group of classical Lie type Bn , Cn , Dn or 2Dn with noncyclic Sylow ℓ-subgroup. Then there exists a non-trivial simple endotrivial kG-module V if and only if
G = Sp8 (2), k has characteristic ℓ = 5, and dim(V ) = 51.
Our approach relies on the fact, proven in [11, Thm. 1.3] that any endotrivial module is liftable to a
characteristic 0 representation, which can then be studied by ordinary character theory. In particular,
its character cannot vanish on any ℓ-singular element, and this latter condition can be checked with the
previous Murnaghan–Nakayama formula.
As a further application we give a (partial) answer to a question of Koshitani, Külshammer and
Sambale [9], which is then used in [10] to settle this question completely:
Theorem 3. Let G be a finite simple group of classical Lie type Bn , Cn , Dn or 2Dn . Let ℓ > 2 be a
prime for which Sylow ℓ-subgroups of G are non-cyclic. Then the ℓ-modular projective cover of the trivial
character of G has at least three ordinary constituents.
In particular the first Cartan invariant of G satisfies c11 ≥ 3.
Our paper is organised as follows. In Section 2 we prove the existence of regular semisimple elements
in suitable maximal tori of groups of classical type and determine possible overgroups of collections of
maximal tori. Section 3 contains the proof of the Murnaghan–Nakayama rule, see Theorem 3.3. We
apply this in Section 4 to prove a vanishing result on ℓ-singular elements, see Theorems 4.1 and 4.2. In
Section 5 we show Theorem 2 classifying simple endotrivial modules for classical groups. In Section 6 we
collect the previous results to prove the vanishing result in Theorem 1. Finally, in Section 7.1 we show
the application to the proof of Theorem 3.
Acknowledgement: We thank Andrew Mathas for useful explanations concerning the notation and
results of [8]. We also thank the anonymous referee for his helpful comments.
