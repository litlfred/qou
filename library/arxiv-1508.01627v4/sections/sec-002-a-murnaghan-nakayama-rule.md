---
doc_id: arxiv-1508.01627v4
doc_title: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups"
section_id: sec-002-a-murnaghan-nakayama-rule
section_title: "A Murnaghan\u2013Nakayama rule"
section_number: 3
pages: 5-9
source_pdf: 1508.01627v4.pdf
source_sha256: 778e60219862e371
doc_brief: "A Murnaghan-Nakayama rule for values of unipotent characters in classical groups — 7 sections: Introduction; Maximal tori in classical groups; A Murnaghan–Nakayama rule"
---
In this section we derive a Murnaghan–Nakayama type formula for the values of unipotent characters
of classical groups of Lie type on regular semisimple elements. It relies on a result of Asai on the
decomposition of Lusztig restriction.


6

FRANK LÜBECK AND GUNTER MALLE

3.1. Lusztig restriction. We consider the following setup: G is a connected reductive algebraic group
over an algebraic closure of the finite field Fp , and F : G → G is a Steinberg endomorphism of G, with
finite group of fixed points GF . For an F -stable Levi subgroup L ≤ G of G Lusztig defined, via certain
ℓ-adic cohomology constructions, induction and restriction functors
G
: ZIrr(LF ) → ZIrr(GF )
RL

and

∗

G
RL
: ZIrr(GF ) → ZIrr(LF )

between the respective groups of virtual characters. These are adjoint to one another with respect to
the usual scalar product of characters. We need the following connection between Lusztig restriction and
ordinary restriction on regular semisimple conjugacy classes:
Proposition 3.1. Let L ≤ G be an F -stable Levi subgroup. Let χ ∈ Irr(GF ) and s ∈ LF be regular
G
semisimple. Then ∗ RL
(χ)(s) = χ(s).
Proof. According to the character formula in [5, Prop. 12.2(ii)] we have
X
|C ◦ (s)F |
C ◦ (s)
∗ G
QCG
(u, 1) χ(s),
RL (χ)(s) = ◦L F
◦
L (s)
|CG (s) |
◦
F
u∈CG (s)u

C ◦ (s)

◦
where the sum runs over unipotent elements in CG
(s)F , and QCG
is a certain 2-parameter Green
◦
L (s)
◦
function. Since s is assumed to be regular semisimple, T := CG
(s) = CL◦ (s) is a torus. Hence the only
term in the sum is the one for u = 1, and by [5, p. 98] the Green function takes the value
C ◦ (s)

T
QCG
◦ (s) (1, 1) = QT (1, 1) = 1
L

◦
(again using that CG
(s) contains no non-trivial unipotent elements). The claim follows.



3.2. Symbols. We now specialise to simple groups of classical type. By Lusztig’s results their unipotent
characters are parameterised by so-called symbols. Here, a symbol is an unordered pair of finite sets of
non-negative integers, usually denoted as
  

X
λ1 λ2 . . . λr
S=
=
µ1 µ2 . . . µ s
Y
with λ1 < λ2 < . . . < λr and µ1 < µ2 < . . . < µs where r, s ≥ 0. Two symbols are said to be equivalent
if one can be obtained from the other by a sequence of shift operations


0 λ1 + 1 λ2 + 1 . . . λr + 1
S 7→
0 µ1 + 1 µ2 + 1 . . . µ s + 1
or by interchanging the rows X and Y of S. The rank of S is by definition
s
r
j  r + s − 1 2 k
X
X
µi −
.
λi +
rk(S) =
2
i=1
i=1
The defect of S is def(S) := |r − s|. Note that the rank and the defect are well-defined on equivalence
classes. We will use the following notation to describe explicit symbols: n := {0, 1, . . . , n} and for a set
X, a k ∈ X and l ∈
/ X we write X \ k ∪ l := X \ {k} ∪ {l}.
Let d be a positive integer. We say that S has a d-hook h at x ∈ X if 0 ≤ x − d ∈
/ X, and similarly at
′
x ∈ Y . Removing that d-hook leads to the symbol S \ h := XY with X ′ = X \ x ∪ (x − d) (respectively

S \ h := YX′ with Y ′ = Y \ x ∪ (x − d)). Attached to the hook h is the sign ǫh := (−1)m where
m := |{y ∈ X | x − d < y < x}| (respectively m := |{y ∈ Y | x − d < y < x}|). We say that S has a
d-cohook c at x ∈ X if 0 ≤ x − d ∈
/ Y , and similarly at x ∈ Y . Removing that d-cohook leads to the

X′
′
symbol S \ c := Y ′ with X = X \ {x}, Y ′ = Y ∪ {x − d} (respectively Y ′ = Y \ {x}, X ′ = X ∪ {x − d}).
Attached to the cohook c is the sign ǫc := (−1)m , where m := |{y ∈ X | y < x}| + |{y ∈ Y | y < x − d}|


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

7

(respectively m := |{y ∈ Y | y < x}| + |{y ∈ X | y < x − d}|), see [6, §3] for example. Note that removing
a d-hook or a d-cohook from a symbol of rank n yields a symbol of rank n − d.
For a symbol S = (X, Y ) with all entries of X, Y not larger than m we define the dual symbol
S ∨ = (X ′ , Y ′ ) where
X ′ = m \ {m − x | x ∈ X} and Y ′ = m \ {m − y | y ∈ Y }.
The hooks and cohooks of S and S ∨ are each in natural bijection such that removing hooks or cohooks commutes with the duality operation. This observation will allow us to simplify some of the later
statements and proofs.
3.3. Unipotent characters of symplectic and orthogonal groups. Now assume that G is simple
of type Bn , Cn or Dn , and F does not induce the triality automorphism when G is of type D4 nor the
exceptional graph automorphism in type B2 or C2 . According to Lusztig [12] the unipotent characters
of G := GF are then parameterised by (equivalence classes of) symbols of rank n. More precisely, if G is
of type Bn or Cn , the unipotent characters of G are parameterised by symbols of rank n and odd defect.
Now assume that G is of type Dn . If the Steinberg endomorphism F is untwisted, then the unipotent
characters of G are parameterised by symbols S of rank n and defect def(S) ≡ 0 (mod 4), where symbols
with two equal rows stand for two characters each. These are the so-called degenerate symbols. If GF is
of twisted type, then the unipotent characters of G are parameterised by symbols S of rank n and defect
def(S) ≡ 2 (mod 4).
If S is a symbol parameterising a unipotent character ρ of a classical group then the Alvis–Curtis
dual ρ∨ of ρ is parameterised by the dual symbol S ∨ which has the same rank, the same defect and the
same hook and cohook lengths (see [12, 4.5.5, 4.6.8]). (In fact, the degree ρ∨ (1) differs by a power of the
underlying characteristic of G from the degree ρ(1).)
3.4. Values of unipotent characters at regular semisimple elements. We first recall the following
result of Asai on the decomposition of Lusztig induction as given in [6, (3.1), (3.2)]. We restate it in
G
G
terms of the restriction functors ∗ RL
instead of the induction functors RL
as in the cited reference.
This is a summary of results from [1, 2.8], [2, 1.5] and [3, 2.2.3]. Note that there is a sign missing in the
formula [6, (3.2)] in the case Dn as can be seen by considering the trivial character.
Theorem 3.2 (Asai (1984)). Let G be of type Bn , Cn or Dn . Let d ≥ 1. Let S be a symbol of a
unipotent character of G = GF . If S is not degenerate, we write ρS for the corresponding character. If
S is degenerate we write ρS for the sum of the two corresponding characters.
d
(a) Let L be the centraliser in G of an F -stable torus Td of G with |TF
d | = q − 1. Then
X
∗ G
RL (ρS ) =
ǫh ρS\h
h d-hook

where h runs over the d-hooks of S.
d
(b) Let L be the centraliser in G of an F -stable torus Td of G with |TF
d | = q + 1. Then
X
∗ G
RL (ρS ) = (−1)δ
ǫc ρS\c
c d-cohook

where c runs over the d-cohooks of S, and δ = 0 for types Bn , Cn , δ = 1 for type Dn .
With this we can show a Murnaghan–Nakayama formula for values of unipotent characters at regular
semisimple elements.
Theorem 3.3. Let G be of type Bn , Cn or Dn . Let S be a symbol of a unipotent character of G = GF .
If S is not degenerate, we write ρS for the corresponding character. If S is degenerate we write ρS for the
sum of the two corresponding characters. Let s ∈ G be regular semisimple lying in an F -stable maximal
torus T of G parameterised by (λ, µ) ⊢ n.


8

FRANK LÜBECK AND GUNTER MALLE

(a) If λ has a part of length d then
ρS (s) =

X

ǫh ρS\h (s)

h d-hook

where h runs over the d-hooks of S.
(b) If µ has a part of length d then
ρS (s) = (−1)δ

X

ǫc ρS\c (s)

c d-cohook

where c runs over the d-cohooks of S, and δ = 0 for types Bn , Cn , δ = 1 for type Dn .
On the right hand side of these formulae the symbols and characters belong to a Levi subgroup of semisimple rank n − d and s lies in a maximal torus of that Levi subgroup corresponding to the pair of partitions
(λ \ d, µ) ⊢ (n − d) in case (a), respectively (λ, µ \ d) ⊢ (n − d) in case (b).
Proof. First assume that λ has a part of length d. Then the torus T has an F -stable subtorus Td with
d
|TF
d | = q − 1, see Section 2.1. We consider Lusztig restriction of ρ = ρS to the F -stable Levi subgroup
L := CG (Td ) ∼
= HTd , with H a group of the same type as G and of rank n − d. This is a d-split Levi
G
subgroup containing T, so s, and according to Asai’s Theorem 3.2(a), the constituents of ∗ RL
(ρ) are, up
F
to the sign ǫh as given in the statement, precisely those unipotent characters of L whose parameterising
symbol is obtained from S by removing a d-hook. Application of Proposition 3.1 then gives the claim
in (a).
d
If µ has a part of length d, then T has an F -stable subtorus Td with |TF
d | = q + 1, and we can argue
precisely as before using Theorem 3.2(b) for the decomposition of Lusztig restriction to L := CG (Td ) ≥
T ∋ s.

Note that in the theorem ρS\h , respectively ρS\c , is a unipotent character of the classical group LF
of rank n − d (of the same type as G, except that removing cohooks changes the value of the defect
modulo 4, so in type Dn interchanges the twisted and untwisted types), and that s is a fortiori regular
in L. Thus, the above result gives a recursive algorithm to compute the character values on all regular
semisimple elements.
In case of degenerate symbols we only get the values of the sum of two unipotent characters. These
unipotent characters form one element Lusztig families and so their values on regular semisimple classes
are the values of the corresponding degenerate irreducible characters of the Weyl group, see [12, (4.6.10)].
The two characters for a degenerate symbol have the same values on non-degenerate classes, but different values on the degenerate classes. See [15] for a definition of unique parameters for the degenerate
characters and classes and a formula to compute the missing values on degenerate classes.
The following vanishing result is immediate from the above:
Corollary 3.4. Let G, S and ρS be as in Theorem 3.3, and let s ∈ G be a regular semisimple element
lying in an F -stable maximal torus parameterised by (λ, µ). Then ρS (s) = 0 in any of the two following
cases:
(1) λ has a part of length d, but S does not have a d-hook; or
(2) µ has a part of length d, but S does not have a d-cohook.
Thus, if ρS (s) 6= 0 and (λ, µ) = ((λ1 , . . . , λr ), (µ1 , . . . , µs )), then it is possible to remove λi -hooks for
1 ≤ i ≤ r and µi -cohooks for 1 ≤ i ≤ s from S in any chosen order.
We remark that we have computed many character values on semisimple classes for classical groups
of rank ≤ 10 by Deligne–Lusztig theory. These examples helped to find the statements given in the next
section. And they also provided an independent check of the Murnaghan–Nakayama formula 3.3.


MURNAGHAN–NAKAYAMA RULE FOR UNIPOTENT CHARACTERS

9
