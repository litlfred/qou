---
doc_id: asens-1986-4-19-1-57-0
doc_title: "Entropy and index for subfactors"
section_id: sec-010-2-tl-eny
section_title: "^T((l-^)EN(y;.)"
section_number: 2
pages: 17-22
source_pdf: ASENS_1986_4_19_1_57_0.pdf
source_sha256: 09b6a599167bb9e8
toc_source: inferred
doc_brief: "Entropy and index for subfactors — 38 sections: Front matter; Introduction; Preliminaries"
---
2)^£T(l-^)
so that T (/?) + T (^) > 1. 
If we denote q =p A y;. e M then
T^)=T(^)+T(y;)-T(^vy;)^T(^)+T(y;.)-i>o.
Moreover ^ satisfies
^(q)=^(pAf,)^(pf,p)=pE^(f,)p^2p^2.
Thus given arbitrary e>0 we can find a nonzero projection qeM such that
EN (<?) ^ s^2- This shows that ^4 = 0.
Q.E.D.
2.4. Remark. — One can use the preceding theorem and a maximality argument to
show that if [M:N]=oo then for any e>0 there exists a nonzero projection eeM such
that: (i). EN«)^£. IN; (ii) the spectral projection of E^(e) corresponding to the set{e}
has trace ^1—e. It would be interesting to decide whether one can find the projection
e such that Ey(e)=s 1^.
Each of the four constants involved in the formulas of Theorem 2.2 make sense for
any pair of finite von Neumann algebras (and even for arbitrary von Neumann algebras
in case there is a normal conditional expectation of M onto N). Therefore we can chose
any of them as a replacement of the index for the general case when N c M are not
necessary finite factors. We shall use the first constant because of its close relation to
the relative entropy that will be considered in the next two sections.
2.5. NOTATION. — Let M be a finite von Neumann algebra with faithful trace T,
T (!)=!, and B^, B^ c: M two von Neumann subalgebras of M, with B^ c= Bp 
We
denote )i(Bi, B^) =max { X^O | Eg^ (x) ^x, x e B^ + }.
The consideration of the constant X is particularly useful to reduce the index problems
from the II i factor case to problems concerning imbeddings of finite dimensional
algebras. To be more precise, let us consider the following situation: Let { N^}, { M^}
be increasing sequences of von Neumann subalgebras of the finite factor M, with
Nfc <= M^, and assume that M^ generate M and N^ generate a subfactor N c M. Then
we wish to have [M: N]~1 =limX(Mfc, N^). This is obviously false in general, as we can
modify the limit of ^(M^, N^), by taking the limit of MM^, N^) instead. The additional
hypothesis that has to be made is EN^E^=E^, fe^l. Note that this condition is
4'= SERIE - TOME 19 - 1986 - N" 1
ENTROPY AND INDEX FOR SUBFACTORS 
73
equivalent to E^ E^ = E^ Ep^ = E^ and it implies N^inM^N^. In fact for
this to hold it is sufficient that EN ^ (M^) c= N^.
2.6. PROPOSITION. — (i) // {B^}, {A^} are increasing sequences of von Neumann
subalgebras in the finite von Neumann algebra M, such that A^ c B^, n^l, and if
B=UB^, A=UA^, r^n X(B,A)^limsup?i(B^A^). 
(ii) If in addition E^^E^=E^
n ^ 1, ^n ^ (B, A) = lim ^ (B^, AJ, decreasingly.
Proof. - Let ^=)i(B^A^), )i=limsup MB,,, A,,) and £>0. Then there exists a
subsequence {^}n such ^t \.^-£, ^1. Since UB^UB^ it follows that if
xeUB^then
E^ (X)^EB, (X)^(?I-£)EB, (x)
and letting n -> oo, EA(X)^(^-£) EB(X)=(^-£)X. As £>0 is arbitrary we get the first
part of the proposition.
If E^EB,=E^ then by induction E^E^=E^ and letting k ^ w, E^a^E^.
Thus if x e B^ then E^, (x) = E^ (x) ^ X- (B, A) x, so that ^ (B, A) ^ ^. This shows that
?i(B,A)^liminf^.
Q.E.D.
A similar proof to that used in Theorem 2.2 for factors shows that if A c= B then
'k (B, A) ^ ^ == inf{ || EA (/) || |/e B nonzero Projection}
and that
^=inff||EA(x)||j/||x||j|xeB^x^O},
X3=inf{||EA(x)||/||x|||xeB^x^O}
lie between 7.(B, A) and ^4. It is easily seen that ^, ^3, ^4. satisfy a statement similar
to 2.6 (i) and that ^ satisfies 2.6 (ii) as well, but it is not clear whether ^3 and ^4 also
satisfy it. In fact even the problem of whether all these constants coincide or not is
open. However we shall prove in Section 6 that for finite dimensional algebras they are
all equal to ^. Proposition 2.6 then applies to get the equality for more general pairs
of approximately finite dimensional algebras. Indeed if A^, B^ satisfy the hypothesis of
2.6(ii) and ^(B^, AJ=^(B^, A^) for all n, then X(B, A)^(B, A) and since the
opposite inequality allways holds we actually have ^(B, A)=^-4(B, A).
It seems to be of great interest to prove (or disprove) that any pair of hyperfinite
factors can be constructed as an inductive limit of finite dimensional algebras {A^},
{ B^} satisfying the conditions of proposition 2.5. In other words: if Rg c R are hyperfi-
nite factors, does there exist an increasing sequence of finite dimensional subalgebras B
inRwithUB^=R 
and 
such 
that E^E^=E^E^ 
Or at 
least 
such thai
U (B^ U RcO^Ro? This last problem is related to a problem of Sakai (see [23] p. 241).
ANNALES SCIENTIFIQUES DE L'ECOLE NORMALE SUPERIEURE
74 
M. PIMSNER AND POPA
3. Relative entropy: some generalities
In [9] A. Connes and E. Stormer extended the notion of entropy from the classical
ergodic theory to the nonabelian frame of operator algebras. Their first step was to
define the entropy of a finite dimensional subalgebra and more generally the relative
entropy between two finite dimensional subalgebras B^, B^cM, as a substitute of the
entropy and relative entopy for partitions: Let S be the set of all finite families (x^,..., x^)
of positive elements in M with £ x^ = 1 (as usual M is a finite von Neumann algebra
with fixed trace r). 
If T| : [0, oo) -> (— oo, oo) is defined by T| (Q = — tint, then
W
H(BjB2)= sup I(Tr|EB,(x,»-TT|E^(x,))
(xi)eS i
is the entropy of B^ relative to B^. 
If B^=C then H(Bi | C) is simply the entropy of B^
and is denoted by H(B^). In the particular case when M is commutative, B^, B^ are
generated by some partitions of the unity P^, P^ and H(BjB2) coincides with the
classical relative entropy h(P^ | P^).
Connes and Stormer use this relative entropy mainly as a technical tool in the proof
of their Kolmogorow-Sinai type theorem. They show that for subalgebras of dimension
less than some n e N the usual « distance »
8(Bi, B2)=sup{||x-E^(x)||2|xeBi, ||x||^l}
is comparable with H(Bi | B^). Thus if 8 is small then H is small. However it is easy
to see that 5^1 and that in fact §==1 whenever B^ is "far" from B^, whereas H may
take different values even if § = 1. In particular if B^ =3 B^ the relative entropy H (B^ | B^)
is more appropriate to express the relative size of B^ with respect to B^. It is this
feature of the relative entropy that we shall exploit here.
Note that the definition (^) does not depend on B^, B^ being finite dimensional, so
that we may consider H(Bi IB^) as in (^) for arbitrary von Neumann subalgebras B^,
B^ c: M and allow H (B^ | B^) = oo.
In fact we shall consider the case when B^ = M and B^ =N is a subalgebra of M. Then
H(M|N) is clearly invariant to conjugation of N by x-preserving automorphisms of
M. 
Our aim in the rest of the paper is to relate this invariant to the index.
In this section we first recall the basic properties concerning the relative entropy and
then prove some useful technical results.
1° In is operator increasing on (0, oo);
2° T| is operator concave on [0, oo) and operator continuous on [0, 1];
3° ifx, ^eM+, xy=yx, then r|(x^)=r|(x)^+xr| (y)\
4° if xeM+ then r|x=0 iff x is a projection;
5° if x, yeM+, then TT|(.x;+^)^Tr|x+TT|^ and if xy=0 then we have equality;
6° if BcM is a von Neumann subalgebra and xeM+ then T| EB(x)^Eg(r|x), in
particular T|T (x) ^ TT| Eg (x) ^ TT| x;
7° if x e M + is a scalar multiple of a projection then TT| Eg (x) = TT| x iff x e B;
4° SERIE - TOME 19 - 1986 - N° 1
ENTROPY AND INDEX FOR SUBFACTORS 
75
8° if BI, B^cM are von Neumann subalgebras then H(Bj B^O and H(BjB2)=0
iffBiczB^;
9° if 
BI, 
B^, 
B3c=M 
are 
von 
Neumann 
subalgebras 
then
H(BjB3)^H(BjB2)+H(B,|B3);
10° H(Bi | B^) is increasing in B^ and decreasing in B^;
11° if Be: M is finite dimensional and e^..., ^eB is a set of minimal projections in B
with^=l thenH(B|C)=H(B)==^riT(eO.
For the proof of 1°, 2°, 6°, see [15], [16], [II], [4]. 
A unified exposition of these results
can be found in [1].
3° and 4° are easy consequences of the functional calculus.
To prove 5° (see [10]) note first that by adding some small positive scalar we may
assume x, y, x-}-y have the spectrum in (0, oo). As In is operator increasing on (0, oo)
we 
get 
\n(x-^-y)^\n x, 
ln(x+.>0^1n y 
so 
that 
T(xln(x+.v))^T(xlnx),
T (y In (x +^)) ^ T (y In ^). Summing up we get rr| (x +y) ^ TT| x + TT| ^.
If x=c^ in 7°, for some projection eeM and ceR+, then TT| Eg (x) = T| (c)
T (e) + c Tr| EB (^)and Tr| x = T| (c) T (^) so that TT| EB (x) = TT| x iff T| Eg (e) = 0. As Eg (e) is
a projection iff E^(e)=e, 4° applies to get 7°.
8° is now an easy consequence of 6°, 7°: if B^B^ then there exists a projection eeB^
such that ^B^, thus
H(BjB,)^(Tr|E^(^)-Tr|^)+(Tr|EB,(l-^)-Tr|(l-^))^TTiEB,()>0.
9° and 10° are clear by the definition and by 6°.
11° is proved in [9].
From now on a finite family x^, . . ., x^eM of positive elements with ^x^=l will be
called a partition of the unity in M.
3.1. LEMMA. — J/B^cBi are von Neumann subalgebras in M and S'cS is the set of
all finite families (xo, x\, x^..., x^) in S mth each x^ f^ 1, a scalar multiple of a projection
and x^eB^, then
H(BjB^)= sup S(TTiEB,(xO-TTiE^)).
(^)eS' i
Proof. — It is clear from the definition (^) that to compute H(Bi|B2) it is enough
to consider partitions (x^) in B^. 
If (x^) e S with all x^ e B^, then by spectral decomposition
there exist x^eB^ such that O^x^Xp x^—x^s and x^ have finite spectrum, i.e.
Xi=^^ij€ij for some scalars oc^.^O and some mutually orthogonal projections (^.)y in
j
BI. As T| is continuous we get
^ (TT1 EB, (X,) - TT1 X,) ^ ^ (T71 EB, (x;) - ^ X,) + 8 (c)
where 8 (e) -^ 0 when s -^ 0. 
By 5° we have
^ ^2 (x^ ^ E Tr!E^ (^ije^ 
and 
^^^ (^D = S Tr! (a^ ^)
j 
j
ANNALES SCIENTIFIQUES DE L'ECOLE NORMALE SUPERIEURE
76 
M. PIMSNER AND POPA
so that
^ (TT| E^ (X,) - TT| X,) ^ ^ (TT| E^ (a,, ^.)
-TT|(a^,))+5(E)^ sup (TriEB^Cy,)-TTv,)+§(£).
(yf) e S'
Q.E.D.
3.2. LEMMA. — Let BcM ^ a uon Neumann subalgebra and {fn}n>i a sequence of
projections in M with || /„— 1 \\^ -> 0.
(i) J/^eB, n^l, then H(M|B)=lim H(M^ B^).
n
(ii) Iff^ e W H M and B 15 a factor then again
H (M | B) = lim H (M^ | B^).
n
[In both (i), (ii) the entropy H(M^ B^) is considered with respect to the induced
trace T^ (/.x/,) = T (/,) -1 T (/^).]
Proof. — Consider first the case when /^eB. Let (x^,..., x^) be a partition of the
unity in M^. 
If Eg 
denotes the i^-preserving conditional expectation of M^ onto
B. then
J n
H(M | B) ^^(TTl EB(X.)-TTI X,)+(TT1 Ee(l -/,)-T11 (1 -/„))
I
= <fn) (Z ^ ^ EB^ (^f) - ^ ^1 ^f) + ^^1 EB ( 1 -/n)-
This shows that H (M | B) ^ lim sup H (M^ | B^).
n
Now if (xi, . . ., x^) is a partition of the unity in M then/^x^./^ tends strongly to x^ so
that Eg (fn^ifn) tends strongly to Eg^.) and as T| is operator continuous
^ (T^ T| EB^ (/„ x, /„) - T^ (/„ x,^))
i
tends to ^(^E^x^-^Xi). This shows that H(M|B)^liminfH(M^|B^).
If /^eB'HM then note that for xe/^M/^ we have Es^eB' 0 B=Z(B) and
EB (/n) EB^ (^) =fn KB (^)- It 
follows 
as 
before 
(for 
/„ e B) 
that 
H (M | B) ^
liminfH(MjB^).
Finally let x^,..., x^ be a partition of/,, for some fixed n. Then
H (M | B) ^ ^ (TT1 EB (X,) - TT1 X,) ^ ^ (T (/„ TI EB (X,)) - TT1 X,)
i 
i
= Z (T11 (/„ Eg (X,)) - TT1 X,) = ^ (TT1 (EB (/„) EB^ (X,)) - TT1 X.)
I 
I"
= Z ^(EB (/„) TI EB^ (X,)) + T (E^ (X,) r| EB (/„)) - Til X,).
4' SEME - TOME 19 - 1986 - N° ]
ENTROPY AND INDEX FOR SUBFACTORS
