---
doc_id: agt-v3-n1-p17-p
doc_title: "Published: 16 June 2003 Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum"
section_id: sec-006-5-the-colored-jones-polynomial-of-twist-knots
section_title: "The colored Jones polynomial of twist knots"
section_number: 5
pages: 17-20
source_pdf: agt-v3-n1-p17-p.pdf
source_sha256: df196f0a732ad6b9
doc_brief: "Skein-theoretical derivation of some formulas of Habiro Gregor Masbaum — We use skein theory to compute the coecients of certain power series considered by Habiro in his theory ofsl2 invariants of"
---
In this last section, we illustrate one use of !p ,n a m e l yt og i v eaf o r m u l af o rt h e
colored Jones polynomial of twist knots (see Figure 3) in terms of the coecients
c
0
n;p . The results of this section are known to K. Habiro and T.Q.T. Le.

p full
twists
Figure 3: The twist knot Kp . (Here p2Z.) For p =1 , Kp is a left-handed trefoil,
and for p =−1, Kp is the 
gure eight knot.
The colored Jones polynomial of a knot K colored with the N -dimensional
irreducible representation of sl2 can be expressed as the Kau
man bracket of
K cabled by (−1)N−1eN−1 :
JK(N)=( −1)N−1hK(eN−1)i :
(The factor of (−1)N−1 is included so that JUnknot (N)=[ N].) We will use the
normalization
J0
K (N)= JK(N)
JUnknot (N) =hK(eN−1)i
heN−1i :
H e r e ,w ea s s u m et h ek n o tK is equipped with the zero framing.
Let us compute hKp(eN−1)i. We use the surgery description given in Fig. 4.
Recall that !p =Pc0
k;pR0
k . By induction, one can check that
eN−1 =
N−1X
n=0
(−1)N−1−n
 N +n
N−1−n

Rn : (47)
Algebraic &GeometricTopology, Volume 3 (2003)
554 Gregor Masbaum
The key observation (which I learned from T.Q.T. Le) is that
Rn
R0
k =0
for k6=n. This is because each component of this link is a zero-framed unknot
having a spanning disk pierced twice by the other component, and circling with
Rm annihilates all even polynomials in z of degree < 2m.
Thus only terms with k =n survive, and so we have
hKp(eN−1)i =
N−1X
n=0
(−1)N−1−n
 N +n
N−1−n

c0
n;p
Rn
R0
n
(48)
Now, using that Rn−en has degree <n , we compute
Rn
R0
n =
en
R0
n
= 2
n
n
n
2n
R0
n
= 2
nCn;nhR0
n;e 2ni
=(−1)nan(n+3)=2f2n +1g!
f1g
where we have used (42) in the last but one equation, and Cn;n andhRn;e 2ni
are given in (44) and (5), respectively (but notice we are usingR0
n =(fng!)−1Rn
here).
Plugging this into (48), we obtain the following result.
Algebraic &GeometricTopology, Volume 3 (2003)
Skein-theoretical derivation of some formulas of Habiro 555
!p
Figure 4: A surgery description of the twist knot Kp with zero framing.
Theorem 5.1 The colored Jones polynomial of the twist knot Kp is given by
J0
Kp (N)=
1X
n=0
fKp;n
fN−ngfN−n +1gf N +ng
fNg ; (49)
where
fKp;n =an(n+3)=2c0
n;p :
(The sum is actually 
nite, the terms with nN being all zero.)
Note that since c0
n;p is a Laurent polynomial in a,s oa r et h ec o e  c i e n t sfKp;n .
For example, for the 
gure eight knotK−1 ,w eh a v efK−1;n = 1, and for the left-
handed trefoil K1 ,w eh a v efK1;n =(−1)nan(n+3) . (The right-handed trefoil is
the mirror image of K1 , so one just needs to take the conjugate of J0
K1 (N).)
These formulas can be found in [H2].
Remark 5.2 Here is another expression for J0
Kp (N). Put q = a2 =A4 and,
as is customary in q-calculus,
(x)n =( 1−x)(1−xq) (1−xqn−1) :
Then (49) gives
J0
Kp (N)=
1X
n=0
~fKp;n(q1−N )n(q1+N )n ;
where
~fKp;n =(−1)nq−n(n+1)=2fKp;n :
For example, for the 
gure eight knotK−1 ,w eh a v e~fK−1;n =(−1)nq−n(n+1)=2 ,
and for the left-handed trefoil K1 ,w eh a v e~fK1;n =qn . These formulas can be
found in [L2] (see also [L1]).
Algebraic &GeometricTopology, Volume 3 (2003)
556 Gregor Masbaum
