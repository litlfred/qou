---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh"
section_id: sec-009-6-a-reparametrization
section_title: "A Reparametrization"
section_number: 6
pages: 13-20
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized envel oping algebras of type A Robert Marsh — Let U be the quantum group associated to a Lie algebra g of type An."
---
We will now use the rectangle combinatorics from the previou s section to calculate the Lusztig
parametrizations cj(j),cP (j) of the canonical basis elements arising in Theorem 4.4; her e j is ﬁxed
as the reduced expression ( n,n − 1,n,n − 2,n − 1,n,... , 1, 2,... ,n ) for w0.
Deﬁnition 6.1 Suppose P is a partial quiver and D(P ) is the diagram for P as deﬁned above.
The rectangles ρ(Y ) for Y a component of P divide D(P ) into smaller rectangles, which we shall
call boxes. (In the example near the start of Section 5, there are 6 boxes). We regard these boxes
as appearing in diagonal rows, from top left to bottom right A s we work our way down the diagonal
rows of boxes, starting from the top right of D(P ), the number of boxes in each diagonal is at ﬁrst
odd, and then even, or is at ﬁrst even, and then odd. We draw a ce ntral line Z on D(P ) dividing
these two sets of diagonal rows of boxes. In our example, the n umber of boxes in each row is 1,3,2,
so the central line is indicated by the dashed line in Figure 7 .
Let Y be a component of P , and deﬁne a set S(Y ) of positive roots as follows. The rectangle
ρ(Y ) for Y is divided into two parts by the central line. Let ρ∗(Y ) be the part of ρ(Y ) which is
labelled. The root α ij lies in S(Y ) if and only if the intersection of a diagonal row of D(P ) (see
Deﬁnition 5.2) with ρ∗(Y ) contains the numbers i,i + 1,... ,j − 1, in order, reading from top left to
bottom right. Then S(P ) is deﬁned to be the union of the sets S(Y ) for Y a component of P . In
our example, S(L1) = {α 1,α 2,α 3}, S(R1) = {α 4 +α 5} and S(L2) = {α 1 +α 2 +α 3,α 2 +α 3 +α 4},
so S(P ) = {α 1,α 2,α 3,α 4 +α 5,α 1 +α 2 +α 3,α 2 +α 3 +α 4}.
Let v(P ) ∈ Nk be deﬁned as follows. The reduced expression j deﬁnes an ordering on the positive
roots; we write β l =sj1sj2 · · ·sjl−1(α jl), forl = 1, 2,... ,k . Then let v(P )l be equal to 1 if β l ∈S(P )
and 0 otherwise. So in the example above, v(P ) = (0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1).
If j ∈ [1,n ], we deﬁne S(j) by specifying that the root α ij lies in S(j) if and only if there is a
diagonal row of D(j) containing the numbers i,i + 1,... ,j − 1, in order, reading from top left to
bottom right. We deﬁne v(j) in the same way as v(P ) is deﬁned using S(P ).
We know that, if b ∈ B and i ∈ [1,n ], then ~Fib ≡ b′ (mod vL′) for some unique b′ ∈ B. With
respect to our ﬁxed reduced expression j, this deﬁnes an action on Nk, deﬁned by ~Fi(ϕ j(b)) = ϕ j(b′).
Using the identiﬁcation in the last paragraph, this also ind uces an action on sets of positive roots,
which we also denote by ~Fi. Reineke, in [17, §1], describes the action of ~Fi on Nk:
13
Proposition 6.2 (Reineke)
Suppose v = (v1,v 2,... ,v k) ∈ Nk. Write, for 1 ≤i<j ≤n + 1,vij =vl, where β l =α ij. For such
i<j , deﬁne
fij =
n+1∑
l=j
vil −
n+1∑
l=j+1
vi+1,l.
Letj0 be minimal so that fij0 = max jfij. Then ~Fi increasesvij0 by 1, decreasesvi+1,j 0 by 1 (unless
i + 1 = j0, when this latter eﬀect does not occur), and leaves the other vij’s unchanged.
Deﬁnition: Let 2 ≤a ≤b ≤n, and let Q be a quiver. We deﬁne the ( a,b )-sub partial quiver of Q
to be the partial quiver P with P ≤Q, leftmost directed edge numbered b and rightmost directed
edge numbered a.
As conjectured by Carter, we have:
Theorem 6.3 LetQ be a quiver, with i ∈χ n compatible with Q. Suppose that (c, i) is a chamber
of Q, with P =P (c, i). Let j = (n,n − 1,n,n − 2,n − 1,n,... , 1, 2,... ,n ). Let bP be the canonical
basis element arising in Theorem 4.4. Then the Lusztig parametr ization cP (j) of bP is given by
v(P ). Similarly the Lusztig parametrization cj(j) of bj is given by v(j).
Proof: We have to calculate Sj
i (a(c, i)) or Sj
i (a(j, i)), and thus we consider the corresponding
monomial of root operators acting on 1, ~F (P ) = ~F a1
i1
~F a2
i2 · · · ~F ak
ik · 1. Here P = P (c, i) in the ﬁrst
case and j in the second. Theorem 5.3 gives a description of ~F (P ) in terms of D(P ). Recall that
D(P ) consists of a number of diagonal rows (see Deﬁnition 5.2), where diagonal row number 1 is
the one which is at the top right of D(P ), diagonal row number 2 is below this (down and to the
left), and so on. We now make a claim.
Letx be a position in D(P ) containing a number, i. Suppose x is in (diagonal) row a. Let r be the
total number of rows in D(P ), and let ~F (s), s = 1, 2,... ,r , be the part of ~F (P ) arising from the
sth row. Thus ~F (P ) = ~F (r) ~F (r − 1) · · · ~F (1) · 1. For s = 1, 2,... ,r , let ds be the number at the
rightmost end of the sth row. Deﬁne ~F [x] := ~F λ i
i ~F λ i+1
i+1 · · · ~F λ da
da
~F (a − 1) · · · ~F (2) ~F (1) · 1, where, if
j appears in row a, λ j is the multiplicity associated to it.
So ~F [x] is a ﬁnal segment of ~F (P ), arising from the ﬁrst a−1 rows of the diagram, together with the
part of the ath row to the right of x, including x. Let c ∈ Nk be deﬁned by ~F [x] ≡F c
i (mod vL′).
Note that there is no problem working here modulo vL′. We shall have ~F [x] ≡b (mod vL′) for a
unique b ∈ B from Kashiwara’s approach, and b ≡F c
i (mod vL′) for a unique c ∈ Nk by Lusztig’s
approach and the comparison theorem [10, §2.3].
LetS(x) be the corresponding multiset of positive roots, obtained by using the ordering on the set
of positive roots induced by j. We claim that S(x) is given by the union of the following two sets:
The ﬁrst, S1(x) is deﬁned to be those roots in S(P ) arising from rows 1 , 2,... ,a − 1, together with
those roots in S(P ) arising from row a of the form α s +α s+1 + · · · +α t where s ≥i. The second,
S2(x), is deﬁned to be the set of roots of form α i +α i+1 +· · ·+α t, where α s +α s+1 +· · ·+α t is a root
in S(P ) arising from row a withs<i (we call this procedure of passing from α s +α s+1 + · · · +α t
to α i +α i+1 + · · · +α t, ‘cutting oﬀ’).
14
We will prove the claim by induction on x. Let us assume that for a given x in D(P ), S(x) is
as described. Let c be as above, corresponding to x. Let y be one position to the left of x in
the ath row of D(P ). We understand this to mean the rightmost element of the ( a + 1)st row of
D(P ) if x is the leftmost element of the ath row. In this case for the purposes of the argument
below we actually take x to be in the same row as y, immediately down and to the right of y, with
corresponding (ﬁctitious) label 1 more than that of y (i.e. actually just outside the diagram D(P )).
Note that in this case, as we are assuming the claim to be true f or x, we have S2(x) = φ. Suppose
there is an i in position y. Then there is an i + 1 in position x. Suppose that x and y both lie
in the ath row of D(P ). We will show that the claim is also true for y. The base case, when x is
taken to be one position to the right of (and below) the rightm ost position of the ﬁrst row, with
S(x) = φ, is trivially true. The Theorem will follow from the inducti on argument, as it is the claim
for the case when x is the leftmost position of the last row of the diagram.
We must show that the set of positive roots (deﬁned by j) corresponding to c′, where ~F [y] =
~F λ i
i ~F [x] ≡ F c′
i (mod vL′) is given by S1(y) ∪S2(y), where i is the number labelling position
y. In the case where y is the rightmost element of its row (numbered a), we take ~F [x] to be
~F (a − 1) · · · ~F (2) ~F (1) · 1. We deﬁne c ∈ Nk by writing cij = 1 if α ij ∈S(x) and cij = 0 otherwise.
We start with an important
Lemma 6.4 If l>i + 1 then we cannot have both cil = 1 and ci+1,l = 1.
Proof: (of Lemma). First of all note that if P = j ∈ [1,n ], the Lemma is obvious, following
easily from the structure of D(P ). So we can assume that P is a partial quiver. Suppose, for a
contradiction, that cil =ci+1,l = 1. So β1 :=α i +α i+1 + · · ·+α l−1 andβ2 :=α i+1 +α i+2 + · · ·+α l−1
both lie in S(x). We are assuming the claim to be true for x, so S(x) = S1(x) ∪S2(x). We shall
see that the structure of D(P ) leads to a contradiction; to do this we consider various cas es:
Case (a) For i = 1, 2, if βi ∈ S2(x), let γi be the root in S(P ) which is ‘cut oﬀ’ to give βi.
Otherwise, let γi = βi. Suppose that γ1,γ 2 both come a rectangle for a component Y of P of
type L which is the ( a1,b 1)-sub partial quiver of Q. The set of positive roots in S(P ) arising
fromY is {α 1,n −b1,α 2,n +1−b1,... ,α s,n +s−1+b1} (where the central line passes through the rectangle
corresponding to Y immediately below the row with leftmost number s). If α =α pq is any positive
root, write r(α ) = q − 1 and l(α ) = p. For each γ in this list, r(γ) is distinct, and since ‘cutting
oﬀ’ a root γ does not aﬀect r(γ), we conclude that this case cannot occur, since r(β1) = r(β2).
Case (b) Suppose that β1,β 2 both come from a component of P of type R, as in (a). We argue as
in case (a) to see that this case cannot occur.
Case (c) Suppose that β1 and β2 arise from distinct components of P and that β1,β 2 ∈S1(x). Let
h be the height of the roots in S(P ) arising from a component Y of P . Then the height of the
roots in S(P ) arising from the component of P immediately to the right of Y (if such exists) is
h +t, where t is the number of directed edges in Y . Thus, since ht( β1) = 1 + ht( β2) (ht denotes
height), for this case to occur, we must be in the situation wh ere we have two components Y and
Z ofP , where Z immediately follows Y , and Y has precisely one directed edge. We assume that Y
is of type L andZ is of type R (the argument in the other case is very similar). Suppose tha t Z is
the (a1,b 1)-sub partial quiver of Q. The two rectangles ρ(Y ) and ρ(Z) will appear in D(P ) as in
Figure 8, where as usual, the dashed line indicates the centr al line in D(P ). Then the roots for Y
will be taken from above this line, and the roots for Z from below, such roots α will have diﬀering
values of r(α ) so we see that this case cannot occur.
Case (d) Suppose we have β1,β 2 ∈S2(x). Suppose ﬁrst that x lies above the central line. We know
15
..................................................................................................................................................................................................................................................................................................................................
..................................................................................................................................................................................................................................................................................................................................
.................................................................................................................................................................................................................................................................................................................................. ..................................................................................................................................................................................................................................................
.................................................................................................................................................................................................................................................. ..................................................................................................................................................................................................................................................................................................................................
........................................................................................................................................................................................................................................................................................................................................................
b1
2+
b1 −a1
1
n −b1
n + 1−a1
n − 1
n + 2−a1
n
Z
Y
Figure 8: The rectangles ρ(Y ) and ρ(Z).
that the lines in D(P ) which are the bottom right edges of rectangles ρ(Y ) where Y is a component
ofP of type L are all distinct and parallel. It follows that r(β1) ⁄=r(β2), a contradiction. A similar
argument holds if x lies below the central line.
Case (e) Suppose that β1 ∈S1(x) and β2 ∈S2(x). If β1 arises from the ath row of D(P ), we can
argue as in (d) (we will have again r(β1) ⁄=r(β2), a contradiction). So assume that β1 arises from
the bth row, where 1 ≤ b < a. We know that β2 arises via cutting oﬀ from a root γ2 ∈ S(P )
which comes from the ath row of D(P ). Since ht( β2) < ht(γ2) and ht(β1) = 1 + ht( β2), we have
ht(β1)< ht(γ2). Therefore, arguing as in (c), we see that β1 comes from a component X1 occurring
to the left of that giving rise to γ2 (and thus β2). We call the latter X2. Suppose that X1 does not
occur immediately to the left of X2, or that X2 is of type R. Then by the structure of D(P ), the
bottom right lines T1, T2 delimiting the rectangles ρ(X1) and ρ(X2) are distinct. Indeed, the line
for ρ(X2) occurs below and to the right of ρ(X1).
We know that there is an l − 1 in the intersection of the bth row with ρ(X1), immediately to the
left and above the line T1. Similarly, there is an l − 1 in the intersection of the ath row with ρ(X2),
immediately to the left and above the line T2, by the construction of β1,β 2. The relative position
of lines T1 and T2 tells us that the former l − 1 lies strictly to the left of the latter, while the fact
that b < atells us that the latter l − 1 lies strictly to the left of the former, a contradiction. We
are left with the case when X1 immediately precedes X2 and X2 is of type L. In this case T1 and
T2 coincide along part of their lengths. Now X1 is of type R, so β1 arises from a row below the
central line, and X2 is of type L, so β2 arises from a row above the central line. It follows that
r(β1) ⁄=r(β2), a contradiction.
Case (f) Suppose that β1 ∈S2(x), β2 ∈S1(x), and β1 and β2 arise from diﬀerent components. If
β2 arises from the ath row, we can argue as in (d). So assume β arises from the bth row, where
1 ≤ b < a. Then β1 arises via cutting oﬀ from a root γ1 ∈ S(P ) which comes from the ath row.
Since ht(β1)< ht(γ1) and ht(β1) = 1 + ht(β2), we have ht(β2)< ht(γ1), and we can argue as in (e).
We have now covered all possible cases for β1,β 2 ∈S(x), and we see that the Lemma is proved. □
16
We now investigate further the structure of c. By assumption, for each j,k , cjk is equal to 0
or 1. The above shows that we cannot have both cil = ci+1,l = 1 for l > i + 1. We shall
now pin down further the possible values for cil and ci+1,l . We know that, for each l > i+ 1,
(cil,c i+1,l ) = (0, 0), (0, 1) or (1, 0). If we let ci+1,i +1 := 1 −ci,i +1, then this is also true for l =i + 1.
Form = 0, 1, 2,...n −i, write am =ci,i +m+1 and bm =ci+1,i +m+1, so the pairs we are interested
in are of form xm = (am,b m),m = 0, 1, 2,...n −i. We ﬁrst need a Lemma describing the action of
~Fi in terms of these pairs, using Proposition 6.2:
Lemma 6.5 Suppose c is as in the above, and we have written the pairs x0, x1,... , xn−i as above,
with each xm equal to (0, 0), (0, 1) or (1, 0). Rewrite this sequence, replacing pairs of these types
with 0, ‘−’ and ‘ +’, respectively. Cross out all 0’s, except initial 0’s. Cross out all non-initial
pairs of symbols of form +−, and repeat until there are no such pairs of symbols in the seq uence
left. Use the following table of possible sequences to deter mine a symbol in the resulting sequence of
symbols. This is deﬁned to be the symbol that is indicated by a l ine above it. Every time a sequence
of symbols appears in the list, as in −, −,... , −, this means that the symbol concerned must occur
at least once.
(i) 0, −, −,... ,
−, +, +,... , +,
(ii) 0, −, −,... , −,
(iii) 0, +, +,... , +,
(iv) 0,
(v) (+, −), −, −,... , −, +, +,... , +,
(vi) (+, −), −, −,... , −,
(vii) (+, −), +, +,... , +,
(viii) +, −,
(ix) −, −,... , −, +, +,... , +,
(x) −, −,... , −,
(xi) +, +,... , +.
In this way, a symbol in the original sequence is determined, a nd therefore an xm. Then acting ~Fi
has the following eﬀect on c. If xm = (0, 1) (i.e. a ‘ −’), then ci+1,i +m+1 = 1 . This is changed
to zero (having no eﬀect if m = 0 ), and ci,i +m+1 is changed from zero to 1, thus changing the
corresponding symbol in the sequence from a ‘ −’ to a ‘ +’. If xm = (1, 0) or (0, 0), then we must
have m = 0 (as no initial symbols are crossed out), and ~Fi has the eﬀect of increasing ci,i +1 by 1.
Proof: We consider how the fij’s are related to the xp’s (see Proposition 6.2 for the deﬁnition of
the fij’s). For each 0 ≤ p ≤ n −i, write δp := fi,i +p+2 −fi,i +p+1. A simple calculation shows us
that δp = 1 if ( xp, xp+1) = (0, −) or ( −, −), that δp = −1 if ( xp, xp+1) = (+, +) or (+ , 0), and is
zero in all other cases. Thus the sequence in the Lemma enable s us to calculate the value of the
fij’s, given the value of fi,i +1 (for our ﬁxed i). Recall that Proposition 6.2 tells us that, in order to
see how ~Fi acts, we need to calculate the smallest j for which fij is maximal; write j0 for this value
of j. It is easy to check that the crossing out routines described above never cross out the symbol
corresponding to xp where i +p + 1 = j0. Thus recalculating this after doing the crossing out does
not aﬀect the ﬁnal result. After crossing out is done, the only possible sequences are those as listed
in the Lemma. It is then easy to check that j0 is given by j0 =i +p + 1 where p is given by the
rules in the Lemma in each case (i)-(xi). □
17
c12 c23 c34 c45 c56
c13 c24 c35 c46
c14 c25 c36
c15 c26
c16
=
1 1 0 1 0
0 0 0 0
1 0 0
0 0
0
Figure 9: The vector c.
Example: To illustrate this Lemma we go back to our example (see Deﬁnit ion 5.1 and Deﬁni-
tion 6.1). So P = LRL− and D(P ) is as in Figure 7. Suppose x is the position of the rightmost
4 in D(P ), the last element in the third diagonal row of D(P ). Then y is the leftmost 3 in
D(P ), the second element in the third diagonal row, so i = 3. The set S1(x) is by assump-
tion {α 1,α 2,α 1 +α 2 +α 3}, and S2(x) is {α 4}. Thus S(x) is the union of these two sets and
c = (0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1). We can write c as in Figure 9.
We have x0 = (c34,c 44) = (0 , 1), x1 = (c35,c 45) = (0 , 1), and x2 = (c36,c 46) = (0 , 0) — these
are indicated by underlining in Figure 9 (note that c44 does not appear in the diagram). Thus
the sequence of symbols as in Lemma 6.5 is ( −, −, 0). In the reduction step, we remove the
ﬁnal zero to get ( −, −) and see we are in case (x) of the Lemma, and that the ﬁnal ‘ −’ is
marked. This corresponds to x1 and the Lemma tells us that applying ~Fi changes c35 from 0
to 1 and c45 from 1 to 0. As a more complicated example, consider the seque nce of symbols
(0, 0, +, +, −, −, +, +, +, 0, −, 0, −, −, +, −, −, −, −, 0, 0). We ﬁrst of all remove non-initial zeros to
get (0, +, +, −, −, +, +, +, −, −, −, +, −, −, −, −) and then remove + , − pairs to get (0, −, −, −) —
which is case (ii) of the Lemma. Thus the last ‘ −’ is indicated, corresponding to the last ‘ −’ of the
original sequence.
We now begin the investigation as promised.
Lemma 6.6 Suppose that xj = (1, 0). Then ci,i +j+1 = 1 , so that α i,i +j+1 ∈ S(x). Suppose that
in fact α i,i +j+1 ∈ S1(x). Then there is m > jso that xj+1 = xj+2 = · · · = xm−1 = (0, 0) and
xm = (0, 1). Thus ci+1,i +m+1 = 1, so α i+1,i +m+1 ∈S(x); in fact α i+1,i +m+1 ∈S1(x).
Proof: Let l =i +j + 2; we know that α i +α i+1 + · · ·+α l ∈S1(x). So α i +α i+1 + · · ·+α l ∈S(P )
and arises from the intersection of row b ofD(P ) with a rectangle ρ, where b<a (sinceα i appears
in it). Thus if P = j ∈ [1,n ], we have a contradiction by the structure of D(P ) (which consists
of only one rectangle); i can appear at the start of one row in D(P ) only. So in this case the
circumstances of the Lemma cannot occur. Therefore we can as sume P is a partial quiver and we
deﬁne X to be the component of P corresponding to ρ. Suppose that row b is not immediately
above the central line in D(P ). Then row b + 1 of D(P ) intersects ρ, the rectangle for X. This
is because i occurs in row a, in position y, where a > b. If row b were the bottom row in the
rectangle for X, i would appear in the left hand corner of this rectangle, and th erefore in no later
row in D(P ) (by the structure of D(P )), a contradiction. Thus the intersection of row b + 1 with
the rectangle for X gives a root α i+1 +α i+2 + · · · +α l+1 ∈S(P ). Since b + 1 ≤a and the label at
position x inD(P ) is i + 1, this root lies in S1(x) (i.e. is not cut oﬀ), as required (with m =j + 1).
18
So we are left in the case where row b does lie immediately above the central line of D(P ). Then X
must be of type L. Suppose ﬁrst that X is the rightmost component of P . Then i appears in the
leftmost column (where a column is perpendicular to what we a re calling a row) of D(P ), and also
is immediately above the central line. The central line coin cides with the bottom left delimiting
line of the rectangle for X. Consider now the rectangle for the component Y immediately to the
left of X. This has bottom right delimiting line parallel to that for X, but length (from top left
to bottom right) less than that for X. Thus its upper left delimiting line is down and to the right
of that for X, and i is in the left hand corner of the rectangle for X. Then all of the upper left
delimiting lines for components other than X appear down and to the right of that for X, so i
cannot appear below the central line. But as b<a , x is below the central line, and therefore so is
y, which is labelled i, and we have a contradiction. Thus there is a component immed iately to the
right of X in P ; we call this Y . Let α i+1 +α i+2 + · · · +α t (some t > l+ 1) in S(P ) be the root
arising from the intersection of the ( b + 1)st row of D(P ) with the rectangle for Y . Then as before
α i+1 +α i+2 +· · ·+α t ∈S1(x). Put m =t−i, and we have (am,b m) = (ci,i +m+1,c i+1,i +m+1) = (0, 1),
as required. We now have to show that xj+1 = xj+2 = · · · = xm−1 = (0, 0). That is, we have to
show that
(a) α i +α i+1 + · · · +α u ⁄∈S(x) for l + 1 ≤u<t , and
(b) α i+1 +α i+2 + · · · +α u ⁄∈S(x) for l + 1 ≤u<t .
We start with (a), and take l + 1 ≤u < t. Since all roots β ∈S2(x) satisfy l(β ) = i + 1, we have
α i +α i+1 + · · ·+α u ⁄∈S2(x). Therefore, it is enough to show that α i +α i+1 + · · ·+α u ⁄∈S(P ). But
ht(α i +α i+1 + · · · +α u) is strictly between the heights of the roots in S(P ) arising from X and Y ,
and so by our description of the heights of the roots in S(P ) in case (c) of the proof of Lemma 6.4,
we see that α i +α i+1 + · · · +α u ⁄∈S(P ) and (a) holds.
For (b), we consider again l + 1 ≤ u < t. If u ⁄= l + 1, the argument used for (a) shows that
α i+1 +α i+2 + · · · +α u ⁄∈S(P ). But if u = l + 1, then this root has the same height as roots
in S(P ) arising from X. So if it were in S(P ), it would have arisen from the intersection of the
rectangle for X with row b + 1 of D(P ). But this row is below the central line of D(P ), whence
α i+1 +α i+2 + · · · +α l+1 does not arise in this way, and so does not lie in S(P ). Next, suppose
that we had α i+1 +α i+2 + · · · +α u ∈S2(x). Then, since x must be below the central line, u must
be immediately to the upper left of the bottom right line deli miting a rectangle corresponding to a
component Z of P of type R. Since α i+1 +α i+2 + · · · +α u is assumed to be in S2(x), it must be
the ‘cut oﬀ’ from a root γ =α p +α p+1 + · · · +α u ∈S(P ),p ≤i, where γ arises from the rectangle
corresponding to Z. Since ht( γ) > ht(α i+1 +α i+2 + · · · +α l+1), Z must lie strictly to the right
of X in P . We know that α i+1 +α i+2 + · · · +α t corresponds to the ﬁrst line of the rectangle for
Y below the central line in D(P ), so Z is strictly to the right of Y , as u < t. Thus the bottom
right delimiting line for Z is strictly down to the right of that for Y . Thus this u lies to the right
of the u corresponding to the α u in α i+1 +α i+2 + · · · +α t (in the ( b + 1)st row of D(P )), and
this u lies below the central line. This is impossible, as all u’s in D(P ) to the right of the u in
the (b + 1)st row (which is immediately below the central line), lie above the central line. Thus
α i+1 +α i+2 + · · · +α u ⁄∈S2(x) and so it is not in S forl + 1 ≤u<t . So we see (b) also holds, and
the Lemma is proved. □
Remark Note that all roots in S2(x) have a corresponding xj of form (0 , 1). All roots in S1(x)
arising from the ath row of D(P ) will be of form α p +α p+1 + · · · +α l, for l ≥p ≥i + 1, so only if
p =i + 1 will they contribute to an xj; in this case we shall get a corresponding xj of form (0, 1).
19
We can now apply Lemma 6.5 in our situation. By Lemma 6.5, afte r the crossing out process, our
sequence looks like ((+ , −), −, −,... , −), ((0), −, −,... , −) or (( −), −,... , −). By Lemma 6.5,
applying ~Fi will change the last minus to a plus, and repeated applicatio ns will change the ﬁnal
λ i minuses to pluses. By the proof of Lemma 6.6, it is clear that a ll of the −’s in the sequence,
except for those in brackets, correspond to precisely those xp’s which correspond to roots of form
α i+1 +α i+2 + · · · +α l ∈S2(x). Suppose ﬁrst that there is no edge of a rectangle between x and y.
By structure of D(P ),λ i is the number of roots in S2(x). Applying ~Fi λ i times thus replaces each
root α i+1 +α i+2 + · · · +α l ∈S2(x) by α i +α i+1 + · · · +α l (see Lemma 6.5). Next, suppose that
there is an edge which is the bottom right edge of a rectangle b etweenx and y. By the structure
of D(P ), λ i is 1 more than the number of roots in S2(x). Applying ~Fi λ i − 1 times thus replaces
each root α i+1 +α i+2 + · · · +α l ∈S2(x) by α i +α i+1 + · · · +α l (see Lemma 6.5). We must have
ci,i +1 = 0, so that the initial symbol in our sequence is a ‘ −’, and we must have a sequence of form
(−), −, −,... , −. From this we can conclude that applying ~Fi one more time changes this initial ‘ −’
(in brackets) into a ‘+’, introducing the root α i intoS(x). Finally, suppose there is an edge which
is the top left edge of a rectangle between x and y. By the structure of D(P ),λ i is 1 less than the
number of roots in S2(x). Applying ~Fiλ i times thus replaces each root α i+1 +α i+2 +· · ·+α l ∈S2(x)
byα i +α i+1 + · · · +α l (see Lemma 6.5), except for the one with minimal value of l. Thus we see
that in each case, applying ~Fi λ i times replaces S(x) with S(y), proving that our claim is also true
for y, and we see it is true for all points in the diagram. It follows that Theorem 6.3 is true. □
