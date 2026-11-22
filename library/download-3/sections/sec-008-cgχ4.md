---
doc_id: download-3
doc_title: "Algebraic index theorem"
section_id: sec-008-cgχ4
section_title: "C.(gχ4) '"
section_number: null
pages: 13-17
source_pdf: Download (3).pdf
source_sha256: 7c2b83ba9f9baad7
toc_source: inferred
doc_brief: "Algebraic index theorem — We prove the Atiyah-Singer index theorem where the algebra of pseudo- differential operators is replaced by an arbitrary deformation quantization of the algebra of functions"
---
235
Let A be another copy of A but with shifted grading: At = A,-\. Consider the
differential graded Lie algebra g x A,
Π x a = 9 +4; [4,4] = 0
[D,a\ = [D,a] 
for D <Ξ g, 0 G A
<$(£>) = 0, D G g; 
<5(α) - (-l)
Hα</(» .
For an element X of §xA define the operator
by
lflo 
£>(flι ) 0 fl2 ® ' ' 0
Lemma 2.2.1. For any X in g xA,
[b,iχ] + ii>x =0.
Proof. Direct computation.
Definition 2.2.2. Let χτ be the map
given by
χτ(Xl Λ
where α G CCΓ'(^o) and sgn(σ) is the sign of the permutation σ of graded ele-
ments X ] , . . . ,Xm determined by
sgn 
i 
" 
~ 
i = t — i ϊ
v κ * ' > ' ' '
A l^ '
+ 1^
Proposition 2.2.3.
*τ 
3
L ι e=£χ τ;
χτ 
δ = bχτ .
Proof. Direct computation.
Corollary 2.2.4. The following 
is a commutative diagram of morphisms 
of
complexes:
C.(gχ4) "
 
/Γ
236 
R. Nest, B. Tsygan
2.3. Poincare Duality. Suppose now that A is a unital algebra over k, AQ is an ideal
in A and τ is an ad (^4)-in variant trace on AQ. Replacing A, AQ by M^(A), M^(AQ)
and τ by ^τ(an\ we can apply the construction of χτ to g = g//γ(/4) and get the
commutative triangle of morphisms of complexes
Clearly, Ql^(k) acts on all three complexes, and all the maps are g/yv(/0-equivariant.
Therefore we get a similar diagram of complexes of coinvariants. Note that
g//v(/0 xMκ(A} = QΪN(A[η]) with the differential d/Sη, where
k[η] = k { η } / ( η
2 ) ; 
d e g » f = l ; 
A[η]=A®k[η].
Making N big enough and applying Proposition 2.1.8 we obtain a map
(defined when * < TV); now notice two simple facts following immediately from
definitions.
i) by restriction from M^ (AQ) to subalgebra {a 
δ,j} ^ AQ one gets a map
ii) under this restriction, the elements of A appear only through the correspond-
ing inner derivations ad (a). Hence the composition CC*-\(A[η]) — > CC~e*(Ao),
which we still denote by /τ, descends to the reduced cyclic complexes CC*-\(A[η]).
Therefore we end up with the following commutative diagram of morphisms of
complexes:
C C * - ι ( A [ η ] )
Definition 2.3.1. The induced map χτ : ~HC*^}(A) -» //C*er(^o) is called the Poin-
care duality map associated to a trace τ.
Recall that there is the long exact sequence
> HCn(k) -* HCn(A) -^ ΉCn(A) Λ HCn-λ(k) -+ - - - .
Theorem 2.3.2. The Poincare duality map χτ factorizes through the boundary
map d:
7/C*-ιM)
where
Proof. 
Note that χτ factorizes through the characteristic map for the differential
graded algebra A [ η ] . But (A[η],δ) is a contractible comples:
δ
0 — >Aη^A — > 0,
Algebraic Index Theorem 
237
and therefore the cyclic homology of A[η] is trivial, as can be seen from the spec-
tral sequence associated to the double complex (CC*(A[η];b,δ). In particular, the
boundary map
is an isomorphism. This proves that there exists χτ making the above diagram
commute. It remains to calculate χτ.
Lemma 2.3.3. 
i) the chain η®
n defines a reduced cyclic homology class in
HC2n-ι(A[η]), 
_
11) Xτ(η®
n) = (ϊ±ϊγS-"τ in HC2n^(A[η}} ,
"0 5 0 " = 
^
2'
7~
2 in
Note that the theorem follows from the above lemma immediately.
Proof of 2.3.3. i) is obvious (both b and d vanish at η®
n)\
ii) follows from Definition 2.2.2 of χτ and Proposition 2.1.8; note that for α in
°f mC
cycle (0 1 . . .n — 1 ) and equals zero otherwise. (Here Eι — j- = £M+ι for i < n — 1
and £,7-1,0 for i — n — 1.)
Let us prove (iii). Recall the definition of the cyclic complex C*
y (Remark
2.1.5). Note that in C
cJ(A[η]),
b(η®
m ) - 0; 
δ(η®
m ) - 1 0 η®
m~
 ] 
B(η®
m ) = m ( 1 0 η®
m )
for any m. Therefore the homology class of η®
n G CC2n-ι(A[η]) is represented in
C*
y by a cycle whose component in A [ η ] ® A [ η ] 
is equal to (—I)""
1
 (n\γ 
l
Note that C^m(k) = k\ one checks easily that the homology class of 1 G C^m(k) is
represented by (-1)"' ^ 1^
2'"
+1) G CC2m(^). From this we conclude that
(n-\)\
whence the statement of the lemma. 
D
Let us recall that (reduced) cyclic homology carries the cup product
U : ΉCa(A) 0 ΉCb(B) -+ ΉCa+M(A (g) B) .
At the level of the complex (NC*(A\b' + δ) (Remark 2.1.5.1) it is given by the
standard shuffle of tensors.
Proposition 2.3.4. There exists the product
• : HCa(k) 0 HCb(k) -> HCa+b+2(k)
238 
R. Nest, B. Tsygan
such that:
^ t .(Π+o = (Jn)[l^(2n+\) for any n ^ o;
ii) for α G #cl(Λ), 0 G #C*(5)
δ(α (Jβ} = dx 
dβ .
Remark 2.3.5. Formula (2.3.4) i) is equivalent to S([*
n) = -l^-D for any n > 0.
Proof of 2.3.4. The composition
CCa(A[η])®CCb(B[η]) 
-> C
defines a product for which η
Un = (n — l)\η®
n. Now, as we have seen above,
the boundary map d induces the isomorphisms HCa(A[η]) — » HCa-\(k\ etc., and
- U(/7+l) _ (2w)[ ι(g;(2/ι+l) 
Π
' 
— 
/?! 
. i — i
Remark 2.3.6. It is easy to write the explicit formula for the Poincare duality map
χτ. Let jci 0 
®xp G ~CC P-\(A\ a0 0 
0 ap G CC^o). Let / = (1 2... p) be
the cyclic permutation. Then
(χτ(x\ Θ 
Θ *„),*<) ^ * ' 0 βp) =(-l)
M/?"
1)/2 Σ sgn(/')
2.4. Examples. Let A—A§+A\ be a Z^ -graded algebra. Let F G A\ such that
F
2 — 1. Let τs : A — > A: be an even supertrace on /I; i.e., τs(ab) = (—l)\
a\\
b\τ s(ba).
Note that F^
2'
7 is a cycle of CC2w_i(^). It is easy to see that dF®
2" = 2n - 1
0/7.
One has
, a,] 
[F, a2,,])
for ciQ,... 9a2n G AQ. Thus we obtain Connes' formula for the Chern character of a
Fredholm module. Theorem 2.3.2 implies that the cocycle in the formula above is
cohomologous to S~"τs.
Now, let us keep the same assumptions as above except F
2 = 1. There are two
odd elements in the algbera QxA, where g = Der(/4); one is ad(F), the other is
F!.
Therefore there is the subspace Λ*(& 
F
2, + k 
ad(F)) in C*($xA); this sub-
space consists of all symmetric polynomial functions of ad(F) and F
2.
Let V be an odd element of a different graded Lie algebra α . Formally, we can
consider any symmetric function in V as an element in C*(α ).
Lemma 2.4.1. If
in α , then ev is a cycle in C*(α ).
Lemma 2.4.2. Put V = ad(F) - F
2,; then
in g x A.
Algebraic Index Theorem 
239
The proof follows from direct computations. Expand ev as a power series in
ad(F) and F
2, and apply the definition of χτs to this infinite sum of chains of
C*($xA). It is easy to see that for 0o, ...,#„ £ A,
χτs (exp(ad(F) - F^))(θQ9 . . . , an ) = / τs(aQe-^ [F, a{\e~^
 F"
A
