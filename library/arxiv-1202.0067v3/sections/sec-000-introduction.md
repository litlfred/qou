---
doc_id: arxiv-1202.0067v3
doc_title: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN\u2013NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 1202.0067v3.pdf
source_sha256: 2ce621c8982ee764
doc_brief: "CHARACTER DEFLATIONS AND A GENERALIZATION OF THE MURNAGHAN–NAKAYAMA RULE ANTON EVSEEV, ROWENA PAGET AND MARK WILDON — 8 sections: Introduction; Deflation by averaging; Skew characters"
---
Tableaux combinatorics is a pivotal theme in the representation theory
of the symmetric groups. Fundamental results in this area include the
Murnaghan–Nakayama rule for the values taken by irreducible characters
of symmetric groups and the Littlewood–Richardson rule (as well as its
special case, Young’s rule), which determines the restrictions of irreducible
characters to Young subgroups of symmetric groups.
The two main results of this paper are Theorems 1.5 and 6.3, which give
a combinatorial description of the restrictions of characters of symmetric
groups to their maximal imprimitive subgroups. Theorem 1.5 is a simultaneous generalization of the Murnaghan–Nakayama rule and Young’s rule.
Theorem 6.3 gives a further generalization, in which Young’s rule is replaced
by a family of special cases of the Littlewood–Richardson rule.
As a corollary of Theorem 1.5, we obtain in Proposition 5.1 a new recursive formula for the character multiplicities that are the subject of Foulkes’
Date: October 2013.
2010 Mathematics Subject Classification. Primary 20C30; Secondary 05E10, 20C15.
Key words and phrases. deflation, wreath product, Murnaghan–Nakayama rule,
Littlewood–Richardson rule.


2

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

Conjecture, a long-standing problem which spans representation theory, invariant theory and algebraic combinatorics. We use this formula to verify
Foulkes’ Conjecture in some new cases, extending the results in [14]. Figures 3 and 4 in §5 show some of the data computed using this formula.
1.1. Character deflations. We now introduce the ideas needed to state
Theorem 1.5. By a construction originally due to Frobenius, the irreducible
characters of the symmetric group Sr are canonically labelled by the partitions of r. As is usual, we write χλ for the irreducible character labelled by
the partition λ, and χλ/µ for the character labelled by the skew-partition
λ/µ. We refer the reader to [8, Chapter 2] or [19, §7.18] for a construction
of these characters and to [19, page 309] for background on skew-partitions.
For each r ∈ N, it is well known (see, for example, [4, Exercise 5.2.8])
that the maximal imprimitive subgroups of Sr are precisely the imprimitive
wreath products Sm o Sn ≤ Sr for m, n ∈ N such that mn = r. Let ϑ be a
character of Sm , and let V be a representation of Sm affording ϑ. Then V ⊗n
is a representation of the base group Sm × · · · × Sm . The complement Sn of
this base group acts on V ⊗n by permuting the factors:
g(v1 ⊗ · · · ⊗ vn ) = vg−1 (1) ⊗ · · · ⊗ vg−1 (n)
for g ∈ Sn and v1 , . . . , vn ∈ V . These two actions combine to give a rep×n the
resentation of Sm o Sn on V ⊗n (see [8, 4.3.6]). We shall denote by ϑg
character of Sm o Sn afforded by this representation. We also need the characters of Sm o Sn whose kernel contains Sm × · · · × Sm . These characters are
precisely the inflations of the characters of Sn to Sm o Sn along the canonical
surjection Sm o Sn  Sn . If ν is a partition of n, we denote by Inf SSnm oSn χν
the irreducible character of Sm o Sn constructed in this way. It is easily seen
×n Inf Sm oSn χν obtained by multiplying characters of
that the characters ϑg
Sn
these two types are irreducible. (By [8, Theorem 4.3.33], any irreducible
character of Sm o Sn is induced from a suitable product of characters of this
form.)
Given a finite group G, we let C(G) denote the abelian group of virtual
characters of G.
Definition 1.1. Let m, n ∈ N and let ϑ be an irreducible character of Sm .
Let ξ be an irreducible character of Sm o Sn . We define

χν if ξ = ϑg
×n Inf Sm oSn χν where ν is a partition of n
Sn
Def ϑSn ξ =
0
otherwise.
Let Def ϑSn : C(Sm o Sn ) → C(Sn ) be the group homomorphism defined by
linear extension of this definition. Given ψ ∈ C(Sm oSn ), we say that Def ϑSn ψ


CHARACTER DEFLATIONS

3

is the deflation of ψ with respect to ϑ. Let DefresϑSn : C(Smn ) → C(Sn ) be
the group homomorphism defined by
χ
DefresϑSn χ = Def ϑSn ResSSmn
m oSn
for χ ∈ C(Smn ).
In the case when ϑ is the trivial character of Sm , we shall omit ϑ and simply write Def Sn and DefresSn . If V is a complex representation of Sm o Sn
with character χ, then Def Sn χ is the character of the maximal subrepresentation of V on which the base group Sm × · · · × Sm acts trivially.
Theorem 1.5 gives a combinatorial rule for the values of DefresSn χλ/µ
where λ/µ is a skew-partition of mn. In order to state this rule, we review
and extend the definition of a border-strip tableaux (see [19, §7.17]).
Recall that a skew-partition σ/τ is said to be a border strip (or rim hook)
if the Young diagram of σ/τ is connected and contains no 2 × 2 square.
The length of the border strip σ/τ is |σ/τ | and its height is defined to be
one less than its number of non-empty rows. If λ/µ is a skew-partition,
then we define a border-strip tableau of shape λ/µ to be an assignment of
the elements of a set J ⊆ N to the boxes of the Young diagram of λ/µ
so that the rows and columns are non-decreasing, and for each j ∈ J, the
boxes labelled j form a border strip; if J = {1, . . . , k}, and for each j ∈ J
the border strip formed by the boxes labelled j has length αj , then we say
that the tableau has type (α1 , . . . , αk ). We need the following three further
definitions, which are illustrated in Figure 1 and Example 1.6 below.
Definition 1.2. Let T be a border-strip tableau. The sign of T is defined
by sgn(T ) = (−1)h , where h is the sum of the heights of the border strips
forming T .
Definition 1.3. Let λ/τ be a border strip in a partition λ. If the lowestnumbered row of λ met by λ/τ is row k then we define the row number of
λ/τ to be k, and write N (λ/τ ) = k.
1 1 2 4 4 4
1 2 2
1 1
1
3
3 3
Figure 1. A border-strip tableau of shape (8, 5, 3, 2, 2, 2)/(2, 2, 1, 1, 1) and
type (6, 3, 3, 3). The heights of the border strips labelled 1, 2, 3, 4 are
3, 1, 1, 0 respectively, and the sign of this border-strip tableau is thus −1.


4

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

Note that if T is a border-strip tableau of shape λ/µ and type (α1 , . . . , αk )
then there are partitions
µ = λ0 ⊂ λ1 ⊂ · · · ⊂ λk−1 ⊂ λk = λ
such that for each j ∈ {1, . . . , k}, the border strip in T labelled j is λj /λj−1 .
Definition 1.4. Let m, n ∈ N and let λ/µ be a skew-partition of mn. Given
a composition γ = (γ1 , . . . , γd ) of n, let γ ?m = (γ1 , . . . , γ1 , . . . , γd , . . . , γd )
denote the composition of mn obtained from γ by repeating each part m
times. An m-border-strip tableau of shape λ/µ and type γ is a border-strip
tableau of shape λ/µ and type γ ?m such that for each j ∈ {1, 2, . . . , d}, the
row numbers of the border strips
λ(j−1)m+1 /λ(j−1)m , . . . , λjm /λjm−1
corresponding to the m parts in γ ?m of length γj satisfy
(1)

N (λ(j−1)m+1 /λjm ) ≥ · · · ≥ N (λjm /λjm−1 ).

Let
aλ/µ,γ =

X

sgn(T )

T

where the sum is over all m-border-strip tableaux T of shape λ/µ and type γ.
Theorem 1.5. Let m, n ∈ N and let λ/µ be a skew-partition of mn. If γ
is a composition of n and g ∈ Sn has cycle type γ then
(DefresSn χλ/µ )(g) = aλ/µ,γ .
Example 1.6. Let λ = (6, 5, 3, 2) and let µ = (3, 1). The three different
2-border-strip tableaux of shape λ/µ and type γ = (1, 2, 3) are shown below.
2 6 6
1 5 5 6
3 4 5
3 4

4 6 6
1 2 4 6
3 5 5
3 5

2 6 6
1 4 4 6
3 5 5
3 5

As required by Definition 1.4, for each j ∈ {1, 2, 3}, the row number of
the border strip labelled 2j − 1 in each tableau is at least the row number
of the border strip labelled 2j. Thus the first border strip corresponding
to each part of γ is added no higher up in each partition diagram than
the second. The sums of the heights of the border strips forming these
tableaux are 4, 4 and 3 and so their signs are +1, +1 and −1, respectively.
By Definition 1.4 we have aλ/µ,γ = 1. Hence Theorem 1.5 implies that
(DefresS6 χ(6,5,3,2)/(3,1) )(g) = 1 if g ∈ S6 has cycle type (1, 2, 3).


CHARACTER DEFLATIONS

5

Deflation is closely related to plethysm of Schur functions (see [12, §I.8]).
In fact, using the standard correspondence between characters of symmetric
groups and symmetric functions, one can show that the special case γ = (n)
of Theorem 1.5 is equivalent to a result proved in [3, Section 9]. Also, in
the special case µ = ∅, the combinatorial description of Theorem 1.5 can
be shown (using our Lemma 4.2 below) to be equivalent to the one given
for plethysm by Macdonald [12, §I.8, Example 8]. These connections are
discussed in more detail in §7.
We prove Theorem 1.5 in §§2–4. The only prerequisites, apart from some
basic character theory, are the Murnaghan–Nakayama rule and the combinatorics of the abacus. In addition to being self-contained, our proof is
highly combinatorial in the sense that the key steps, given in §3, can all be
stated in terms of explicit bijections between certain classes of tableaux.
1.2. Some special cases. It is clear than if m = 1 then DefresSn χ = χ for
any character χ of Sn , and so the special case m = 1 of Theorem 1.5 asserts
that χλ/µ (g) = aλ/µ,γ for any skew-partition λ/µ of n and any element
g ∈ Sn of cycle type γ. Equivalently,
X
χλ/µ (g) =
sgn(T )
T

where the sum is over all border-strip tableaux of shape λ/µ and type γ.
This is the Murnaghan–Nakayama rule, as stated in [19, Equation (7.75)].
It should be noted that we require the Murnaghan–Nakayama rule in §3.3
below, and so our work does not provide a new proof of this result. In practice the Murnaghan–Nakayama rule is most frequently used as a recursive
formula for the values of characters or skew characters. Equation (10) at
the end of §4 formulates Theorem 1.5 in this way.
As Stanley observes in [19, page 348], it is far from obvious that the
character values given by the Murnaghan–Nakayama rule applied to a skewpartition λ/µ and a composition γ are independent of the order of the parts
of γ. This remark applies even more strongly to Theorem 1.5. For example,
the reader may check that if λ/µ = (6, 5, 3, 2)/(3, 1), as in Example 1.6,
and γ 0 = (2, 1, 3), then there is a unique 2-border-strip tableau of shape
(6, 5, 3, 2)/(3, 1) and type γ 0 . Thus aλ/µ,γ 0 = 1, but the sums defining aλ/µ,γ
and aλ/µ,γ 0 are different.
Another special case of Theorem 1.5 worth noting occurs when g is the
identity element of Sn . If ξ is an irreducible character of Sm o Sn then either
the base group B = Sm × · · · × Sm is contained in the kernel of ξ and
hResB ξ, 1B i = ξ(1), or hResB ξ, 1B i = 0. Hence, by linearity, we have
(2)

(DefresSn χ)(1) = hResB χ, 1B i


6

ANTON EVSEEV, ROWENA PAGET AND MARK WILDON

for any character χ of Smn . It now follows from Theorem 1.5 and Frobenius
reciprocity that
E
D
1
×
·
·
·
×
1
aλ/µ,(1n ) = χλ/µ , IndSSmn
Sm
m ×···×Sm Sm
for any skew-partition λ/µ of mn. It is clear from Definition 1.4 that aλ/µ,(1n )
is the number of semi-standard tableaux of shape λ/µ and type (mn ). Therefore, by setting µ = ∅ in the previous equation, we obtain a special case of
Young’s rule (see [8, 2.8.5] or [19, Proposition 7.18.7]).
1.3. Outline of the paper. The remainder of the paper proceeds as follows. Throughout, we shall adopt the convention that if α is a partition of
r ∈ N, then gα ∈ Sr is an element of cycle type α, and zα is the size of
the centralizer of gα in Sr . (The choice of gα within the conjugacy class is
irrelevant.) If α = (α1 , . . . , αk ), we write nα = (nα1 , . . . , nαk ).
In §2 we prove Proposition 2.2, which implies that if χ is a character
of Smn and g ∈ Sn , then (DefresSn χ)(g) is the average value of χ on the coset
of the base group Sm × · · · × Sm in Sm o Sn corresponding to g. Equation (2)
above is a special case of this result. In the case when g ∈ Sn is an n-cycle,
we obtain Proposition 2.6(ii), which implies that if λ/µ is a skew-partition
of mn, then
(3)

DefresSn χλ/µ (g) =

X χλ/µ (gnα )
α

zα

where the sum is over all partitions α of m, and nα denotes the partition
obtained from α by multiplying each of its parts by n.
In §3 we state a theorem of Farahat (see [5, Section 4]), which gives a
formula for the character values χλ/µ (gnα ) appearing on the right-hand side
of (3). We then give a character-theoretic proof of this theorem.
In §4 we combine the results of §3 and §4 to show that Theorem 1.5 holds
when g ∈ Sn is an n-cycle (Proposition 4.3) and then to deduce it in general.
In §5 we apply our results on deflations to Foulkes’ Conjecture on permutation characters the symmetric group. In particular, we prove a new
recursive formula for the character multiplicities that appear in this conjecture. Using this formula we check Foulkes’ Conjecture in some new cases,
extending the results in [14].
In §6, we consider the more general deflation maps Def ϑSn . When ϑ =
b
χ(a,1 ) is labelled by a hook partition, Theorem 6.3 gives a combinatorial
description of the value of DefresϑSn χλ/µ on an n-cycle. This result generalizes the case γ = (n) of Theorem 1.5 and may be viewed as a simultaneous
generalization of the Murnaghan–Nakayama rule and a special case of the
Littlewood–Richardson rule. We also give an illustrative example showing


CHARACTER DEFLATIONS

7

how our methods can be used to compute values of deflated characters in
the non-hook case.
Finally, in §7, we discuss the aforementioned connections between Theorem 1.5 and results in [3, 12] stated in terms of symmetric functions.
