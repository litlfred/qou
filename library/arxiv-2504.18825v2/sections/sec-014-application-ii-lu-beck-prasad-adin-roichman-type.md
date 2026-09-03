---
doc_id: arxiv-2504.18825v2
doc_title: "MURNAGHAN\u2013NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU"
section_id: sec-014-application-ii-lu-beck-prasad-adin-roichman-type
section_title: "Application II: Lu\u0308beck\u2013Prasad\u2013Adin\u2013Roichman-type formula"
section_number: 7
pages: 34-43
source_pdf: 2504.18825v2.pdf
source_sha256: 829f97190cb1c8ad
doc_brief: "MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS NAIHUAN JING AND NING LIU — 16 sections: Introduction; Preliminaries; Murnaghan–Nakayama rule for the cy"
---
In this section, as the second application of our Murnaghan–Nakayama rule, we will establish a Lübeck–Prasad–Adin–Roichman formula for the cyclotomic Hecke algebra Hm,n (q, u).
(λ(1) ,λ(2) ,··· ,λ(m) )
To proceed with this, We will present an algorithm for χµ
using the corresponding single partition λ with empty m-core and (λ(1) , λ(2) , · · · , λ(m) ) as its m-quotient.
Finally, we will explain how our formula recovers the Adin-Roichman formula for the complex reflection group Wm,n [AR22], and particularly the Lübeck-Prasad formula for the
hyperoctahedral group [LP21].
7.1. A restatement of the Murnaghan–Nakayama rule. In this subsection, we restate the Murnaghan–Nakayama rule established in Section 3 in terms of ητλ;r defined as
below.
Definition 7.1. Let λ = (λ(1) , λ(2) , · · · , λ(m) ) ∈ Pn,m , τ = (τ (1) , τ (2) , · · · , τ (t) ) be a t-tuple
of partitions with each partition having at most m parts and r be a positive integer. Define
ητλ;r as the sum of values obtained by all possible applications of the following algorithm:
Initialization: ε := 1.
(1) If t = 0, end the program and output ε.
(2) If l(τ (t) ) < m, add 0’s to the tail to make sure τ (t) has m components.


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
35

!

!








!

















(3,1),(2,1,1),(2,2)

Figure 4. Four possible removal processes for η(2,1);r
. Here t =
1 and we choose σ = id. The sum terms they contribute are respectively ur2 (1 − q −2 )3 (−q −2 )0 , ur2 (1 − q −2 )3 (−q −2 )0 , ur2 (1 − q −2 )2 (−q −2 )0 and
ur2 (1 − q −2 )2 (−q −2 )0 .
(t)

(3) Choose a permutation σ ∈ Sm . Remove a τσ(j) -generalized ribbon θj from λ(j) for
all j = 1, 2, · · · , m. If there is no such σ to do the removal process, set ε = 0 and
end the program.
Pm
Pm
(4) Multiply ε by urm (1 − q −2 )−1+ j=1 cc(θj ) (−q −2 ) j=1 ht(θj ) , where cc(θj ) (resp. ht(θj ))
is the number of connected components (resp. the height) of θj . And m := max{1 ≤
(t)
j ≤ m | τσ(j) ̸= 0}.
(5) Redefine τ := (τ (1) , τ (2) , · · · , τ (t−1) ) and t := t − 1.
(6) Return to step (1).
Figure 4 presents four possible removal processes.
For a partition µ = (µ1 , µ2 , · · · , µt ) (µt > 0), define Pm (µ) := {(τ (1) , τ (2) , · · · , τ (t) ) |
(j)
τ
⊢ µj and l(τ (j) ) ≤ m, 1 ≤ j ≤ t}. Let λ, µ ∈ Pn,m . Then we have the following
restatement of the Murnaghan–Nakayama rule:
χλµ = q n−l(µ)

m
X

X

ητλ;r .

(7.1)

r=1 τ ∈Pm (µ(r) )

7.2. A Lübeck–Prasad–Adin–Roichman-type formula. Now, we will identify a partition λ with its boundary sequence ∂(λ), which is a finite 0/1 sequence constructed as
follows: commence at the southwestern vertex of the diagram of λ, and traverse along the
edges of the southeastern boundary proceeding towards the northeastern vertex; represent


36

NAIHUAN JING AND NING LIU

Figure 5. λ = (7, 7, 7, 6, 3, 3, 2, 1), the boundary of λ is marked by arrows.
Thus, ∂(λ) = 10101001 | 1101000 and the anchor of ∂(λ) is 8.
each horizontal movement by a 1, and each vertical movement by a 0. Clearly, λ is determined by its boundary sequence ∂(λ) and invariant under adding 0’s (resp. 1’s) to the
head (resp. tail) of ∂(λ). We define the anchor of ∂(λ) = (s1 , s2 , · · · , st ) is the position i
such that #{1 ≤ j ≤ i | sj = 1} = #{i + 1 ≤ j ≤ t | sj = 0}. We usually insert a vertical
line “|” into ∂(λ) to indicate the anchor. See Figure 5 for an example.
Now we describe the bijection Ψm between the set of m-multipartitions of n (denoted
0
). Here, the
by Pn,m ) and the set of partitions of mn with empty m-core (denoted by Pmn
m-core of a partition λ is obtained by removing as many m-ribbons from λ as possible.
(i)

(i)

Definition 7.2. For a given λ = (λ(1) , λ(2) , · · · , λ(m) ) ∈ Pn,m , suppose ∂(λ(i) ) = (s1 , · · · , sd ),
i = 1, 2, · · · , m. Here we add the leading 0’s and trailing 1’s to make ∂(λ(i) ) have the same
length d and the same anchor for all 1 ≤ i ≤ m. We let Ψm (λ) be the unique partition
such that ∂(Ψm (λ)) is
(1)

(2)

(m)

(1)

(2)

(m)

(1)

(2)

(m)

s1 , s1 , · · · , s1 , s2 , s2 , · · · , s2 , · · · , sd , sd , · · · , sd .
We claim Ψm is a bijection. Indeed, λ = (λ(1) , λ(2) , · · · , λ(m) ) is the m-quotient of Ψm (λ).
Moreover, we have |Ψm (λ)| = m|λ| (see also [AR22, Remark 2.9]).
Example 7.3. We choose λ as follows:









.

,

,

The boundary sequence of each component of λ is 10 | 110, 100 | 10 and 11 | 00, respectively.
Add the leading 0’s and tailing 1’s to make sure they have the same length and the same
anchor. So their boundary sequences can be presented as follows:
010 | 110
100 | 101
011 | 001


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
37

1
3
2
3
2
1
2
3
˜
˜
Figure 6. ∂(λ)
= 010101001 | 110100011, k(∂(λ))
= 9 and the row-color
sequence is marked in the leftmost column. Thus, the green generalized ribbon is colored by 1.

Therefore, the boundary sequence of Ψm (λ) is 010101001 | 110100011. This is exactly the
partition in Figure 5 when remove the leading 0’s and the tailing 1’s.
Lemma 7.4. Let λ = (λ1 , · · · , λl ) (λl ≥ 0) be a partition with its boundary sequence
∂(λ) = (s1 , s2 , · · · ). We collect the following facts from [AR22]:
(1) Removing a k-ribbon from λ is equivalent to exchanging si = 1 with si+k = 0, for
some i.
(2) The position in ∂(λ) of the zero corresponding to λi is equal to λi + l − i + 1.
˜
For a given partition λ with empty m-core and length l, denote by ∂(λ)
the boundary
sequence given by Definition 7.2 (before removing the leading 0’s and the tailing 1’s).
˜
˜
Note that ∂(λ)
relies on the choice of ∂(λ(1) ), ∂(λ(2) ), · · · , ∂(λ(m) ). Define k(∂(λ))
:= #{j |
˜
∂(λ)j = 0}. We define the row-color sequence a(λ) of λ by a(λ) := (a1 , · · · , al ), where
˜
1 ≤ ai ≤ m and ai ≡ λi + k(∂(λ))
− i + 1 (mod m), i = 1, 2, · · · , l.3 We claim that
˜
a(λ) is independent of the choice of ∂(λ).
Indeed, if we have another boundary sequence
ˆ
∂(λ) obtained from Definition 7.2 via distinct choice of ∂(λ(1) ), ∂(λ(2) ), · · · , ∂(λ(m) ), then
˜
ˆ
m | (k(∂(λ))
− k(∂(λ))),
which implies they gives the same a(λ) by definition.
We say the starting point (resp. ending point) of a ribbon is the northeastmost (resp.
southwestmost) box of the ribbon. A ribbon is colored by i if the row-color of the row
containing the starting point of the ribbon equals i. That is, if the starting point is in the
j-th row then aj = i. More generally, We say a generalized ribbon is colored by i if all of
its connected components are colored by i. See Figure 6 for an example.
Proposition 7.5. Let λ be a partition with empty m-core and m-quotient (λ(1) , λ(2) , · · · , λ(m) ).
We have that removing a k-generalized ribbon with p connected components from λ(i) is
3We remark that the definition of the row-color sequence is slightly different from that in [AR22,

Definition 3.3].


38

NAIHUAN JING AND NING LIU

equivalent to removing a km-generalized ribbon with p connected components colored by i
from λ.
(i) (i)
˜
Proof. Suppose ∂(λ(i) ) = (s1 , s2 , · · · ) is the boundary sequence of λ(i) and ∂(λ)
=
(s1 , s2 , · · · ) is the boundary sequence given by Definition 7.2. By Lemma 7.4 (1), removing
a k-generalized ribbon with p connected components from λ(i) is equivalent to exchanging
(i)
(i)
(i)
(i)
(i)
(i)
si1 = 1 with sj1 = 0, si2 = 1 with sj2 = 0, · · · , sip = 1 with sjp = 0 in ∂(λ(i) ) for
P
some i1 < j1 < i2 < j2 < · · · < ip < jp such that pa=1 (ja − ia ) = k. It follows from
the definition of Ψm that this is further equivalent to exchanging
Pp su1 = 1 with sv1 = 0,
su2 = 1 with sv2 = 0, · · · , sup = 1 with svp = 0 such that a=1 (va − ua ) = km and
ua ≡ va ≡ i (mod m), 1 ≤ a ≤ p. Lemma 7.4 (1) implies that this is equivalent to removing a km-generalized ribbon with p connected components from λ. If we assume the
starting points of the connected components of this km-generalized ribbon are respectively
˜
in the row t1 , t2 , · · · , tp in λ, then Lemma 7.4 (2) yields that λta + k(∂(λ))
− ta + 1 = va ,
˜
1 ≤ a ≤ p. So λta + k(∂(λ)) − ta + 1 ≡ i (mod m), 1 ≤ a ≤ p, i.e., this km-generalized
ribbon is colored by i, which completes the proof.
□

Example 7.6. If we remove the generalized ribbon (its two components are in color yellow
and green) from λ(2) = (2, 1, 1) as follows:



.





,

,

This is equivalent to removing the following generalized ribbon colored by 2 (its two components are in color yellow and green) from (7, 7, 7, 6, 3, 3, 2, 1):
1
3
2
3
2
1
2
3
For any finite sequence a = (a1 , a2 , · · · ), we define its inversion number by
inv(a) := #{(i, j) | i < j, ai > aj }.
Let a(λ) = (a1 , a2 , · · · , al ) be the row-color sequence of λ. Define its m-inversion number
by
invm (λ) := inv(a(λ)).


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
39

For any finite sequence a = (a1 , · · · , ad ), we assume that b = (b1 , · · · , bd ) is a permutation
of a. Define I(a; b) by
I(a; b) := min{inv(σ) | σ ∈ Sd , such that ai = bσ(i) for all i = 1, 2, · · · , d}.
Here the permutation σ is viewed as a word (or sequence). For instance, σ = (13254) is
identified with the word 35214 for the reason that


1 2 3 4 5
σ=
.
3 5 2 1 4
For example, we choose a = (1, 2, 5, 1, 3, 2, 7), b = (2, 5, 1, 3, 2, 7, 1). Then the permutation
σ with the minimal inversion number satisfying ai = bσ(i) is 3127456. So I(a; b) = 5.
Remark 7.7. I(a; b) can be computed graphically. Indeed, I(a; b) is equal to the minimal
value of all possible applications of the following process:
(1) Put sequences a and b in two rows and align them;
(2) Connect the same number in the generic manner: no three lines intersect at one
point;
(3) Count the intersection number of the lines.
In the above example, we can draw the lines, which produce the minimal intersection number
as follows:
1

2

5

1

3

2

7

2

5

1

3

2

7

1

So I(a; b) = 5.
′

Lemma 7.8. Let λ be a partition obtained from λ by removing a generalized ribbon with
connected components ξ1 , ξ2 , · · · , ξp . Suppose ui and vi are respectively the indices of the
rows in λ containing the starting point and ending point of ξi (1 ≤ i ≤ p) such that
u1 < v1 < u2 < v2 < · · · < up < vp . If we assume the row-color sequence of λ is
a(λ) = (· · · , au1 , · · · , av1 , · · · , au2 , · · · , av2 , · · · , aup , · · · , avp , · · · ).
|
{z
}
|
{z
}
|
{z
}
v1 −u1 +1

v2 −u2 +1

vp −up +1

Then we have
′

a(λ ) = (· · · , au1 +1 , · · · , av1 , au1 , · · · , au2 +1 , · · · , av2 , au2 , · · · , aup +1 , · · · , avp , aup , · · · );
|
{z
}
{z
}
|
|
{z
}
v1 −u1 +1

v2 −u2 +1

vp −up +1

(7.2)
′

′

I(λ/λ ) := I(a(λ); a(λ )) =

p
X

#{j | ui < j ≤ vi , aj ̸= aui };

(7.3)

i=1
′

′

(−1)invm (λ)−invm (λ ) = (−1)I(λ/λ ) .

(7.4)


40

NAIHUAN JING AND NING LIU

Proof. (7.2) can be obtained by using the same arguments as those in [AR22, Lemma 3.5].
(7.3) follows from (7.2) by definition (or Remark 7.7). Now we show (7.4). It follows from
(7.2) that
′

invm (λ) − invm (λ ) =

p
X


#{j | ui < j ≤ vi , aj < aui } − #{j | ui < j ≤ vi , aj > aui } ,

i=1
′

which has the same parity as I(λ/λ ) by (7.3). This completes the proof.

□

Definition 7.9. Let λ be a partition of mn, τ = (τ (1) , τ (2) , · · · , τ (t) ) be a t-tuple of partitions with each partition having at most m parts and r be a positive integer. Define ητλ;r as
the sum of values obtained by all possible applications of the following algorithm:
Initialization: ε := 1.
(1) If t = 0, end the program and output ε.
(2) If l(τ (t) ) < m, add 0’s to the tail to make sure τ (t) has m components.
′
(t)
(3) Choose a permutation σ ∈ Sm . Remove a mτσ(1) -generalized ribbon θ1 colored by
(t)

′

′

1 from λ, and then remove a mτσ(2) -generalized ribbon θ2 colored by 2 from λ/θ1 .
(t)

′

Continue this process until we remove a mτσ(m) -generalized ribbon θm colored by m
′
′
from λ/(θ1 ∪ · · · ∪ θm−1 ). If there is no such σ to do the removal process, set ε = 0
and end the program.
Pm
Pm
′
′
′
′
(4) Multiply ε by urm (1 − q −2 )−1+ j=1 cc(θj ) (−q −2 ) j=1 (ht(θj )−I(θj )) , where cc(θj ) (resp.
′
′
ht(θj )) is the number of connected components (resp. the height) of θj . And m :=
(t)
max{1 ≤ j ≤ m | τσ(j) ̸= 0}.
(5) Redefine τ := (τ (1) , τ (2) , · · · , τ (t−1) ) and t := t − 1.
(6) Return to step (1).
Now we are ready to give a Lübeck–Prasad–Adin–Roichman formula for the cyclotomic
Hecke algebra, computing the irreducible characters by using partitions instead of mmultipartitions.
Theorem 7.10. Let λ = (λ(1) , λ(2) , · · · , λ(m) ), µ ∈ Pn,m . We assume that λ is the unique
partition with empty m-core and (λ(1) , λ(2) , · · · , λ(m) ) as its m-quotient. Then we have
m
X
X
λ
n−l(µ)
χµ = q
ητλ;r ,
(7.5)
r=1 τ ∈Pm (µ(r) )

Proof. By (7.1), Definition 7.1 and Proposition 7.5, it suffices to show that ητλ;r = ητλ;r , for
which it is sufficient to verify that the factors of corresponding removal process under the
bijection established in Proposition 7.5 differ by some power of −q −2 . To be precise, if we
remove a k-generalized ribbon θi with height ht(θi ) from λ(i) , which, due to Proposition
′
′
7.5, is equivalent to removing a km-generalized ribbon θi colored by i with height ht(θi )
′
′
from λ, then we need to verify ht(θi ) = ht(θi ) − I(θi ). For the sake of argument, we make
the following assumptions:


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
41
′

′

′

′

• θi (resp. θi ) has p connected components ξ1 , ξ2 , · · · , ξp (resp. ξ1 , ξ2 , · · · , ξp ).
(i)
(i)
(i)
(i)
(i)
• Let u1 < v1 < u2 < v2 < · · · < up < vp (resp. u1 < v1 < u2 < v2 < · · · < up <
(i)
(i)
vp ) be the indices of rows in λ (resp. λ(i) ) such that the uq -th (resp. uq -th) row
(i)
and the vq -th (resp. vq -th) row contain respectively the starting point and ending
′
point of ξq (resp. ξq ), q = 1, 2, · · · , p.
(i)
(i)
(i)
(i)
(i)
• Let b1 < d1 < b2 < d2 < · · · < bp < dp (resp. b1 < d1 < b2 < d2 < · · · < bp <
(i)
dp ) be the indices of positions in ∂(λ) (resp. ∂(λ(i) )) such that we swap sbq = 1
′
(i)
with sdq = 0 (resp. si (i) = 1 with s (i) = 0) when remove ξq (resp. ξq ) from λ (resp.
bq

dq

(i)

λ ).
Thus, with the above notations in hand, we have
′

ht(ξq ) = #{t | st = 0, bq ≤ t < dq },

(i)

(i)
ht(ξq ) = #{t | st = 0, b(i)
q ≤ t < dq }.

By the definition of Ψm , we hence have
(i)

(i)
#{t | st = 0, b(i)
q ≤ t < dq } = #{t | st = 0, bq ≤ t < dq , t ≡ i (mod m)}.

Therefore,
′

ht(θi ) − ht(θi ) =

p
X


′
ht(ξq ) − ht(ξq )

q=1
p

=

X

#{t | st = 0, bq ≤ t < dq , t ̸≡ i (mod m)}

q=1
p

=

X

#{t | uq < t ≤ vq , at ̸= auq } (by the definition of a(λ))

q=1
′

=I(θi ) (by Lemma 7.8).
This finishes the proof.

□

Example 7.11. Figure 7 presents four removal processes corresponding to those of Figure
4. Let us take the leftmost one as an example. We firstly remove a 6-generalized ribbon
′
′
θ1 colored by 1, which has two connected components. So ht(θ1 ) = 2 + 1 = 3. As we
′
′
can see, a(λ) = (1, 3, 2, 3, 2, 1, 2, 3) and a(λ \ θ1 ) = (3, 2, 1, 3, 2, 2, 1, 3). So I(θ1 ) = 3.
′
′
Similarly, we have ht(θ2 ) = 2 and I(θ2 ) = 2. Thus, this process contribute the sum term
ur2 (1 − q −2 )3 (−q −2 )0 .
7.3. Specialization to Wm,n case. This subsection aims to explain how our result (Theorem 7.10) reduces to the special case for Wm,n , which was considered in [AR22]. As we
mentioned in section 4, the irreducible character ϕλ can be obtained from χλ by specializing u = ζ = (1, ζ, ζ 2 , · · · , ζ m−1 ) and q = 1, where ζ is the primitive m-th root of unity.
In this case, ητλ;m = 0 unless each partition τ (i) (1 ≤ i ≤ l(µ(m) )) has only one row, i.e.,
(m)
τ (i) = (µi ). Moreover, only those processes of removing ribbons (not generalized ribbons)


42

NAIHUAN JING AND NING LIU

1
3
2
3
2
1
2
3

Remove generalized ribbons colored by 1

3
2
1
3
2
2
1
3

3
1
3
2
2
2
1
3

3
2
3
1
2
1
2
Remove generalized ribbons colored by 2 3

3
2
1
3
2

3
3
2
1
2
1
2
3

3
2
3
1
2
1
1

Figure 7. Four removal processes corresponding to those in Figure 4. The
sum terms they contribute are same as those in Figure 4.
from λ can contribute the summation. Therefore, if τ ∈ Pm (µ(m) ), then ητλ;m u=ζ equals
q=1

the sum of values obtained by all possible applications of the following algorithm:
Initialization: ε := 1.
(1) If t = 0, end the program and output ε.
(m)
(2) Remove a mµt -ribbon θ from λ. If we can not find such a ribbon, set ε = 0 and
end the program.
(3) Multiply ε by (−1)ht(θ)−I(θ) .
(m)
(m)
(m) 
(4) Redefine τ := (µ1 ), (µ2 ), · · · , (µt−1 ) and t := t − 1.


MURNAGHAN–NAKAYAMA RULE FOR THE CYCLOTOMIC HECKE ALGEBRA AND APPLICATIONS
43

(5) Return to step (1).
Let ∅ = λ(0) ⊂ λ(1) ⊂ · · · ⊂ λ(r) = λ be a chain such that λ(i+1) /λ(i) is a ribbon. Then

Pr−1

(i+1)

(i)

Pr−1

(i+1) )−inv

/λ )
it follows from equation (7.4) that (−1) i=0 I(λ
= (−1) i=0 invm (λ
(−1)invm (λ)−invm (∅) . This, together with the above algorithm, implies that
λ
ητλ;m u=ζ = (−1)invm (λ)−invm (∅) γmµ
(m) .

(i)
m (λ )

=

(7.6)

q=1

Here γ λ is the irreducible character of the symmetric group indexed by the partition λ
(m)
(m)
with λ = (λ(1) , λ(2) , · · · , λ(m) ) as its m-quotient, mµ(m) = (mµ1 , mµ2 , · · · ) and τ ∈
Pm (µ(m) ).
Summarizing above, we get the special case of Theorem 7.10 as below, which firstly
appears in [AR22, Theorem 3.1].
Corollary 7.12. Let λ ⊢ mn, µ ⊢ n. Suppose the m-quotient of λ is (λ(1) , λ(2) , · · · , λ(m) ).
Then we have
(λ(1) ,λ(2) ,··· ,λ(m) )

ϕ(∅,··· ,∅,µ)
(1)

(2)

λ
= (−1)invm (λ)−invm (∅) γmµ
,

(7.7)

(m)

where ϕ(λ ,λ ,··· ,λ ) (resp. γ λ ) is the irreducible character of the complex reflection group
(resp. the symmetric group) indexed by (λ(1) , λ(2) , · · · , λ(m) ) (resp. λ).
Proof. Taking specialization u = ζ, q = 1 and µ = (∅, · · · , ∅, µ) on both sides of (7.5)
gives that
(λ(1) ,λ(2) ,··· ,λ(m) )

ϕ(∅,··· ,∅,µ)

λ
= η((µ
,
(m)
(m)
),(µ
),··· ,);m u=ζ
1

2

(7.8)

q=1

which, together with (7.6), yields (7.7). As desired.

□

Remark 7.13. It would be interesting to find a representation-theoretic interpretation of
P
λ
n−l(µ(m) )
and possiτ ∈Pm (µ(m) ) ητ ;m (up to an explicit normalization factor, e.g. involving q
−2
(1)
(2)
(m)
bly a power of −q ), for λ with empty m-core and m-quotient (λ , λ , · · · , λ ). More
precisely, one may ask whether this quantity arises as the value of a natural character (or
virtual character) associated with a suitable algebra related to Hm,n (q, u), for example a
subalgebra, a corner algebra, or a quotient/subquotient, evaluated at an element corresponding to g((∅, · · · , ∅, µ(m) )). In the Wm,n case, this interpretation is given by the symmetric
group Sn .
