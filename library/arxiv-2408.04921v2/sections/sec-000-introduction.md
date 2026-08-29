---
doc_id: arxiv-2408.04921v2
doc_title: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 2408.04921v2.pdf
source_sha256: dcfe112640a8adda
doc_brief: "IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP HUIMIN GAO AND NAIHUAN JING — 5 sections: Introduction; Irreducible characters of Ck ≀ Sn; X ij"
---
The character theory of the symmetric group Sn plays an important role
in representation theory [8]. It is well known that the irreducible characters
χλ of Sn are indexed by partitions λ of n, and explicit character values are
given by the celebrated Frobenius formula, which expresses the character
values as the transition coefficients between the Schur symmetric functions
and the power-sum symmetric functions [8, 15]. The character formula can
also be formulated using a vertex algebraic method [9], where the irreducible
character values of Sn are expressed by matrix coefficients of Bernstein vertex operators [25] and products of Heisenberg operators.
The theory of irreducible characters of the wreath product G ≀ Sn , where
G is any finite group, was given by Specht [22]. Under the Frobenius-type
charactersitic, the irreducible characters χλ of G ≀ Sn correspond to the
wreath product Schur symmetric functions [23] labelled by partitions λ colored by the irreducible characters of G. The character values are then given
by the transition coefficients between the wreath product Schur symmetric
functions and power-sum symmetric functions of partitions colored by the
conjugacy classes of G.
Zelevinsky also studied the representations of G ≀ Sn using the language
of PSH-algebras [25]. The Grothendieck group of the category of finitedimensional complex representations possesses an additional structure of
Hopf algebra obeying positivity and self-adjointness axioms.
In [5, 7] Frenkel, Wang and the second named author reformulated the
Specht character theory using the vertex algebraic method in the context
of the McKay correspondence. The character values are given by matrix
coefficients of vertex operators of the form
Y
Y
h pρi (c),
Xγ (λi )i,
1


2

HUIMIN GAO AND NAIHUAN JING

where Xγ (λi ) are the components of some vertex operators indexed by irreducible character λi of G and pρi (c) are power-sum symmetric functions
colored by the conjugacy classes of G.
It is generally believed that the character theory of the generalized symmetric group Cp ≀ Sn , the wreath product of the cyclic group Cp and Sn ,
is closely related to the modular character theory of the symmetric group
Sn over characteristic p (cf. [13]). All Weyl groups of classical type are essentially generalized symmetric groups. If k = 1, the generalized symmetric
group reduces to Sn ; if k = 2, it is specially called the hyperoctahedral group,
which is isomorphic to the Weyl group in type B. A character identity relating irreducible character values of the hyperocta-hedral group C2 ≀ Sn and
those of the symmetric group S2n was recently found [14, 1]. It is natural to
study how to effectively compute character values of the generalized symmetric group Ck ≀ Sn . Pfeiffer has given programs to compute the character
tables of the Weyl groups in GAP [21].
The classical Murnaghan-Nakayama rule is a combinatorial rule for computing the irreducible character χλ on conjugacy class ρ of the symmetric
group Sn [18, 19]. Recall that a partition λ of n is a decreasing sequence of
positive integers λi whose total sum is n, denoted by λ ⊢ n. The number of
λi is the length of λ, denoted by l(λ). If the parts λi are not ordered, then
we call λ a composition of n.
There are several generalizations of the classical Murnaghan-Nakayama
rule. Osima [20] had given a Murnaghan-Nakayama rule in terms of skew
representations of the generalized symmetric groups, and Stembridge [24]
rediscovered the rule and studied associated combinatorial formulas. This
version of the Murnaghan-Nakayama rule requires information of restricting an irreducible representation of Ck ≀ Sn to Ck ≀ Sn−m , so it needs extra work for computer programming. Finally Ariki and Koike [2] found the
Murnaghan-Nakayama rule for the generalized symmetric group that naturally generalizes the classical one and independent of a priori information
of the restriction functor. There are also generalizations of the MurnaghanNakayama rule for other related structures [17, 3, 4, 6, 12].
In this paper, we study the Murnaghan-Nakayama rule for the generalized
symmetric groups Ck ≀ Sn aiming to compute the characters effectively. We
first reformulate the Ariki-Koike version of the Murnaghan-Nakayama rule
using the vertex algebraic method. Our treatment relies upon the vertex
operator realization of Schur functions [10, 11] to derive the iterative formula
for the irreducible characters, which is perhaps a quicker derivation of the
rule. Another benefit of the vertex algebraic method is that it also gives a
new iterative rule or the dual rule for the generalized symmetric group by
reducing the partition of the irreducible representation by rows.
Our reformulation of the Murnaghan-Nakayama rule is the following result, which is obtained by splitting the operators corresponding to conjugacy
classes. This version gives an iterative formula to compute the irreducible
characters that may simplify computational complexity.


IRREDUCIBLE CHARACTERS OF THE GENERALIZED SYMMETRIC GROUP

3

Theorem 1.1. Given colored partitions λ = (λ(0) , λ(1) , · · · , λ(k−1) ) and ρ =
(s)
(s)
(s)
(ρ(0) , ρ(1) , · · · , ρ(k−1) ) of n, where ρ(s) = (ρ1 , · · · , ρm , · · · , ρl(s) ). Then the
value of the irreducible character χλ of Ck ≀ Sn at the class ρ is given by
χλ
ρ =

k−1 X
X
λ\ξj
,
(−1)ht(λj ) ω −sj χ (s)
ρ\ρm

j=0 ξj

(1.1)

(s)

where ξj runs through all colored ρm -rim hooks contained in λ that are
supported at the j-th constituent.
Moreover, we can also break down the irreducible characters into lower
rank ones using a dual procedure, which leads to a new iterative rule for
the generalized symmetric group. Our rule at k = 1 seems to be a new
combinatorial formula for the irreducible character values of the symmetric
group Sn as well.
Theorem 1.2. (New iterative rule) Given colored partitions λ = (λ(0) , λ(1) ,
· · · , λ(k−1) ) and ρ = (ρ(0) , ρ(1) , · · · , ρ(k−1) ) of n. For any fixed color j, the
irreducible character value of Ck ≀ Sn is given by
χλ
ρ =

X

(j)
µ⊳ρ,kµk≥λ1
(j)
τ ⊢kµk−λ1

ω (η(τ )−η(µ))j

(−1)l(τ ) λ\λ(j)
χ 1
kl(τ ) zτ (ρ\µ)∪τ

(1.2)

summed over colored partitions µ and τ such that µ ⊳ ρ with weight bigger
(j)
(j)
than λ1 and τ of weight kµk − λ1 . Here zτ is defined below (2.10), τ is
P
the rearrangement of τ , and η(τ ), η(µ) are the weighted lengths i il(τ (i) ),
P
(i)
i il(µ ) respectively.

We point it out that the dual Murnaghan-Nakayama rule for the generalized symmetric group gives a different iteration procedure. The former one
given by Ariki and Koike simplifies the indexing colored-partition by removing all rim-hooks in each constituent, while our new rule simply removes the
largest part in a fixed constituent. This reveals a different relation between
representations of the generalized symmetric groups.
We also show how to use the Sagemath program [26] to implement the
algorithm. In theory, any irreducible character value of the generalized symmetric group can be iterated once according to our program pending on
computer’s CPU. The source code for this program can be found in the
appendix. As applications, we also find a numerical relation between the
irreducible character values of Ck ≀ Sn and those of modular Skn mod k.
The paper is organized into three parts. In section 2, we recall the basic
notions about generalized symmetric groups Ck ≀ Sn and the construction
of the irreducible character value [5]. In section 3, we derive the analog of
the Murnaghan-Nakayama rule and another iterative formula for the generalized symmetric groups, using the technique of vertex operators. The dual


4

HUIMIN GAO AND NAIHUAN JING

Maunaghan-Nakayama rule for the symmetric group is also obtained as a
consequence. In section 4, we discuss some examples and properties of irreducible character values based on our main results. In the end, we formulate
a numerical relation between the irreducible character values of Ck ≀ Sn and
those of modular Skn . The character tables of C3 ≀ S1 , C3 ≀ S2 , C3 ≀ S3 are
attached in the end.
