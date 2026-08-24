---
doc_id: arxiv-math-0105186v2
doc_title: "Along exact sequence for symplectic Floer cohomology Paul Seidel"
section_id: sec-002-11-exact-symplectic-geometry-and-ﬁbrations
section_title: "Exact symplectic geometry and ﬁbrations"
section_number: 1.1
pages: 4-10
source_pdf: 0105186v2.pdf
source_sha256: e1552ceb6c82c27c
doc_brief: "A long exact sequence for symplectic Floer cohomology — 45 sections: Introduction; Dehn twists, and all that; Exact symplectic geometry and ﬁbra"
---
By an exact symplectic manifold we mean a compact manifold M with boundary,
together with a symplectic form ω and a one-form θ satisfyingdθ =ω, such that
θ|∂M is a contact one-form and makes ∂M convex. An isomorphism of exact
symplectic manifolds is a diﬀeomorphism φ : M → M ′ which is symplectic,
satisﬁes φ∗θ′ = θ in some neighbourhood of ∂M , and such that [ φ∗θ′−θ]∈
H 1(M,∂M ; R) is zero. This means that there is a unique function Kφ∈C∞
c (M\
∂M, R) such that φ∗θ′ =θ +dKφ. We denote by Symp e(M ) the group of those
exact symplectic automorphisms of M which are the identity near ∂M . Its Lie
algebra consists of vector ﬁelds X such that ω(·,X ) = dH for some H which
vanishes near ∂M , and is thus identiﬁed with C∞
c (M\∂M, R).
An exact Lagrangian submanifold in M is a pair consisting of a Lagrangian
submanifoldL⊂M (always assumed to be disjoint from ∂M ) and a functionKL
on it such that dKL =θ|L. The image of L under an isomorphism φ :M→M ′
of exact symplectic manifolds is again an exact Lagrangian s ubmanifold, in a
canonical way; the associated function is
Kφ(L) = (KL +Kφ|L)◦φ−1. (1.1)
In particular, Symp e(M ) acts on the set of exact Lagrangian submanifolds. A
special situation which will occur later on is that φ∈ Sympe(M ) satisﬁes φ(L) =
L in the ordinary sense. Then (supposing L to be connected) Kφ(L) =KL +c
for some constant c =Kφ|L, which needs not be zero. This means that φ may
not map L to itself as an exact Lagrangian submanifold, instead “shif ting” it
by some amount.
A notion of ﬁbre bundle suitable for exact symplectic geomet ry is as follows.
Let S be a smooth connected manifold, possibly with boundary (one could
also allow corners), and π : E→ S a diﬀerentiable ﬁbre bundle whose ﬁbres
are compact manifolds with boundary. Write ∂hE⊂ E for the union of the
boundaries of all the ﬁbres. If the boundary of S is empty,∂hE =∂E ; otherwise
∂E has another face ∂vE =π−1(∂S ), and the two faces meet at a codimension
4
two corner. An exact symplectic ﬁbration is such an ( E,π ) equipped with
Ω ∈ Ω 2(E) and Θ ∈ Ω 1(E), satisfyingdΘ = Ω, such that each ﬁbre Ez withωz =
Ω|Ez and θz = Θ |Ez is an exact symplectic manifold. There is an additional
condition of triviality near ∂hE, by which we mean the following: choose some
z∈ S and consider the trivial ﬁbration ˜ π : ˜E = S×Ez→ S, with the forms
˜Ω , ˜Θ which are pullbacks of ωz,θz. There should be a ﬁbrewise diﬀeomorphism
N /d47/d47
π
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63 ˜N
˜π/d127/d127/d127/d127/d127/d127/d127/d127/d127
S
(1.2)
betweeen neighbourhoods N⊂E, ˜N⊂ ˜E of ∂hE resp. ∂h ˜E, which maps ∂hE
to ∂h ˜E, equals the identity on the ﬁbre over z, and sends Ω , Θ to ˜Ω , ˜Θ. Note
that the choice of z and the diﬀeomorphism are not considered to be part of the
data deﬁning an exact symplectic ﬁbration; only their exist ence is assumed.
Lemma 1.1. Take a point z∈S and a chart ψ :U→S, with U⊂ Rk a con-
tractible neighbourhood of 0, such that ψ(0) = z. Then there is a trivialization
Ψ : U×Ez→ψ∗E, such that Ψ |{ 0}× Ez = id and
Ψ ∗Θ = θz +
k∑
i=1
Hidti +dR.
HereH1,...,H k,R∈C∞(U×Ez, R) are functions which vanish near U×∂Ez,
and ti the coordinates on Rk. Moreover, the diﬀerence between any two such
trivializations Ψ 1, Ψ 2 is a map Ψ −1
2 ◦ Ψ 1 : (U, 0)→ (Sympe(Ez), id).
The proof is by a standard argument involving Moser’s Lemma. The result
means ﬁrst of all that any exact symplectic ﬁbration ( E,π ) has a structure of
Sympe(Ez)-ﬁbre bundle, where Ez is any ﬁbre. In addition to that, E carries
a preferred connection, which gives rise to canonical paral lel transport maps
ρc :Ec(a)→Ec(b) over smooth paths c : [a;b]→S; these are exact symplectic
isomorphisms, and lie in Symp e(Ec(a)) if c is closed. To deﬁne the preferred
connection, one can use a local trivialization as before and set A = ∑
iHidti,
which is a one-form on U with values in C∞
c (Ez\∂Ez, R). It is easy to check
that this transforms in the proper way. A more intrinsic appr oach is to observe
that TEx =TEh
x⊕TEv
x splits into a horizontal and a vertical piece, given by
TEv
x = ker(Dπx) and
TEh
x ={X∈TEx : Ω( X,·)|TEv
x = 0}. (1.3)
EachZ∈TSz has a unique lift Zh∈C∞(TEh|Ez), and these vectors deﬁne the
same connection as before (conversely, one can show that giv en a Symp e(M )-
ﬁbre bundle and a compatible connection, one can equip its to tal space with
5
the structure of an exact symplectic ﬁbration). In a local tr ivialization as in
Lemma 1.1, the curvature of the connection is
FA =
∑
i<j
(
−∂Hi
∂tj
+ ∂Hj
∂ti
−ωz(Xi,Xj)
)
dti∧dtj, (1.4)
where Xi is the family of Hamiltonian vector ﬁelds on Ez corresponding to
Hi(t,·). If one takes the more intrinsic view, the curvature is a two -form on S
with values in functions on the ﬁbres, and is given by ( Z1,Z 2)↦→Ω( Zh
1,Zh
2 ). In
the case where the base S is an oriented surface, we say that ( E,π ) is nonneg-
atively curved if for any oriented chart ψ and trivialization Ψ, the function in
front of dt1∧dt2 in (1.4) is nonnegative; or equivalently, if Ω |TEh is nonnega-
tive for the induced orientation of TEh. To see what this means, consider an
exact symplectic ﬁbration ( E,π ) over the closed unit disc ¯D(1)⊂ C, and the
monodromy ρ = ρ∂ ¯D(1) : E1→ E1 around the boundary in positive sense. If
the curvature is nonnegative, one can write ρ as time-one map of some (time-
dependent) Hamiltonian on E1 which vanishes near ∂E1 and is≤ 0 everywhere.
Example 1.2. Let Eρ = R×M/(t,x )∼ (t− 1,ρ (x)) be the mapping torus of
ρ∈ Sympe(M ). To make this into an exact symplectic ﬁbration over S1 = R/Z,
one chooses a function Rρ∈C∞(R×M, R) such that Rρ(t−1,ρ (x)) = Rρ(t,x )−
Kρ(x), and then sets Ω Eρ = ω, Θ Eρ = θ +dRρ. The preferred connection is
the one induced from the trivial connection on R×M , and its monodromy is ρ
itself. It is easy to prove that all exact symplectic ﬁbratio ns over a circle are of
this form.
For future use, we make an observation on the compatibility o f symplectic
parallel transport with Lagrangian submanifolds. Let c : [a;b]→S be a smooth
embedded path. Suppose that we have an exact Lagrangian subm anifold in each
ﬁbre Ec(t), depending smoothly on t; by this we mean a subbundle Q⊂E|im(c)
such that each ﬁbre Qc(t)⊂Ec(t) is Lagrangian, together with a KQ∈C∞(Q, R)
whose restrictions KQc(t) =KQ|Qc(t) make the Qc(t) exact.
Lemma 1.3. Assume that all the Qc(t) are connected. Then the following con-
ditions are equivalent:
(i) Ω|Q = 0;
(ii) Θ|Q =dKQ +π∗κQ for some κQ∈ Ω 1(im(c));
(iii) the maps ρc|[s;s′] : Ec(s) → Ec(s′) satisfy ρc|[s;s′](Qc(s)) = Qc(s′) for all
s,s ′.
The proof is straightforward. To be precise, (iii) concerns Qc(s) as Lagrangian
submanifolds only. Taking the functions into account and us ing (1.1) yields
Kρc|[s;s′](Qc(s)) =KQc(s′ ) +
∫
c|[s;s′]
κQ.
Hence ρc|[s;s′](Qc(s)) = Qc(s′) holds in the sense of exact Lagrangian submani-
folds iﬀ κQ = 0, or what is the same, Θ |Q =dKQ.
6
Just like any kind of ﬁbre bundle with connection, exact symp lectic ﬁbra-
tions can be manipulated by cut-and-paste methods. As an exa mple, take
two oriented surfaces Sk, k = 1, 2, and boundary circles Ck ⊂ ∂Sk; and let
S be the surface obtained by identifying C1,C 2 orientation-reversingly. Sup-
pose that we have exact symplectic ﬁbrations ( Ek,πk, Ω k, Θ k) over Sk whose
monodromies around Ck, taken in opposite senses, coincide. Then, assuming
additionally that (Ek,πk) is ﬂat (has zero curvature) near Ck, one can construct
from them an exact symplectic ﬁbration ( E,π ) over S. It is maybe useful to
give some details of this. To start, take oriented collars ψ1 : (−1; 0]×R/Z→S1,
ψ2 : [0; 1)× R/Z→ S2 around C1,C 2 respectively, so that S can be deﬁned
by using ψ2◦ (ψ1)−1 to identify the two circles. Our main assumption is that
there should be an exact symplectic isomorphism between the ﬁbres of Ek over
ψk(0, 0), say, which relates the monodromies around ψk({0}× R/Z). Because
of ﬂatness, an equivalent formulation is that there is some m apping torus Eρ as
in Example 1.2 and diﬀeomorphisms
(−1; 0]×Eρ
/d15/d15
Ψ 1
/d47/d47E1
π1
/d15/d15
(−1; 0]× R/Z
ψ1
/d47/d47S1
[0; 1)×Eρ
/d15/d15
Ψ 2
/d47/d47E2
π2
/d15/d15
[0; 1)× R/Z
ψ2
/d47/d47S2
such that (Ψ k)∗Ω k = Ω Eρ and (Ψ k)∗Θ k = Θ Eρ +dRk for some functions Rk.
Clearly, one can introduce modiﬁed forms ˜Θ k = Θ k−d ˜Rk with suitable functions
˜Rk, in such a way that (Ψ k)∗ ˜Θ k = Θ Eρ near{0}× Eρ. Gluing together the
(Ek,πk) along Ck via Ψ 2◦ (Ψ 1)−1 yields a smooth ﬁbration ( E,π ) over S,
and the Ω k, ˜Θ k match up to forms Ω , Θ on it, making it an exact symplectic
ﬁbration. Since we have not changed the symplectic connecti on, nonnegativity
of the curvature of ( Ek,πk) implies the same for ( E,π ).
Remark 1.4. The ﬂatness condition on (Ek,πk) near Ck can be removed.
Namely, suppose that it is not satisﬁed for k = 1 . What one does then is to
choose a function g ∈ C∞([−1; 0], R) such that g(s) = s for s close to −1,
g(s) = 0 for s close to 0, and g′(s)≥ 0 everywhere; and deﬁne a self-map p
of the surface S1 by p(z) = z for z /∈ im(ψ1), p(ψ1(s,t )) = ψ1(g(s),t ). This
collapses a small neighbourhood of C1 onto that boundary circle, so if we re-
place (E1,π 1) by its pullback under p, it becomes ﬂat near C1, and the previous
construction goes through. It is noteworthy that this still preserves nonnegative
curvature, becauseDp has determinant ≥ 0 everywhere.
The basic objects of Picard-Lefschetz theory are ﬁbrations over surfaces,
where the ﬁbres are allowed to have certain particularly sim ple singularities. Let
S be a connected oriented surface, possibly with boundary. An exact Lefschetz
ﬁbration 1 overS consists of data ( E,π, Ω , Θ ,J 0,j 0) as follows. E is a (2n + 2)-
1Called “exact Morse ﬁbration” in [28]. The present terminol ogy is more in line with
general usage, since the notion is closely related to, even t hough not quite the same as, the
symplectic Lefschetz ﬁbrations considered by Donaldson, G ompf, and others.
7
dimensional manifold whose boundary is the union of two face s ∂hE and ∂vE,
meeting at a codimension two corner. π :E→S is a proper map with ∂vE =
π−1(∂S ) (so this may be empty), and such that both π|∂hE : ∂hE→ S and
π|∂vE : ∂vE → ∂S are smooth ﬁbre bundles. π can have at most ﬁnitely
many critical points, and no two may lie on the same ﬁbre (more over, because
of the previous assumptions, they must lie in the interior of E). Denote by
Ecrit ⊂ E, Scrit ⊂ S the set of critical points resp. of critical values. J0 is
an almost complex structure on a neighbourhood of Ecrit, and j0 a positively
oriented complex structure on a neighbourhood of Scrit. These are such that π
is (J0,j 0)-holomorphic near Ecrit, and the Hessian D2π at any critical point is
nondegenerate as a complex quadratic form. The closed two-f orm Ω ∈ Ω 2(E)
must be nondegenerate on TEv
x = ker(Dπx) for each x ∈ E, and a K¨ ahler
form for J0 in some neighbourhood of Ecrit. Θ ∈ Ω 1(E) must satisfy dΘ = Ω.
We also require triviality near ∂hE, which means the existence of a map (1.2)
with the same properties as for exact symplectic ﬁbrations. For brevity, exact
Lefschetz ﬁbrations will usually be denoted by ( E,π ) alone, as we have already
done for exact symplectic ﬁbrations.
For any x ∈ E there is a decomposition TEx = TEh
x⊕ TEv
x with TEh
x
deﬁned as in (1.3); the horizontal part is zero at critical po ints, and projects
isomorphically to TSz, z = π(x), at any other point. We say that an exact
Lefschetz ﬁbration has nonnegative curvature if Ω |TEh
x ≥ 0 for each x. Note
that if x /∈ Ecrit is close to a critical point, Ω |TEh
x is strictly positive anyway,
because of the K¨ ahlerness assumption on Ω. A standard argum ent based on
this shows
Lemma 1.5. If β ∈ Ω 2(S) is a suﬃciently positive two-form, Ω + π∗β is a
symplectic form on S.
Symplectic parallel transport for an exact Lefschetz ﬁbrat ion is well-deﬁned
as long as one avoids the critical ﬁbres; indeed, if one remov es those ﬁbres, the
remainder is an exact symplectic ﬁbration over S\Scrit. We now take a look
at the structure of the critical points. Take z0∈Scrit and local j0-holomorphic
coordinates ξ : U → S, where U ⊂ C is a neighbourhood of the origin, such
that ξ(0) = z0. By assumption there is a unique critical point x0∈ Ez0 . The
holomorphic Morse Lemma says that one can ﬁnd a neighbourhoo d of the origin
W⊂ Cn+1 and a J0-holomorphic chart Ξ : W→E with Ξ(0) = x0, such that
(ξ−1◦π◦ Ξ)(x) = x2
1 +··· +x2
n+1
is the standard nondegenerate quadratic form on Cn+1. We call ( ξ, Ξ) a holo-
morphic Morse chart. In general, it is not possible to choose Ξ in such a way
that Ξ ∗Ω is the standard K¨ ahler form on W⊂ Cn+1; however, one can remedy
this by a suitable local deformation.
Lemma 1.6. Let (E,π, Ω , Θ ,J 0,j 0) be an exact Lefschetz ﬁbration, and x0 a
critical point of π. Then there are smooth families Ω µ∈ Ω 2(E), Θ µ∈ Ω 1(E),
0≤µ≤ 1, such that
8
(i) Ω 0 = Ω , Θ 0 = Θ ;
(ii) for all µ, Ω µ = Ω 0 and Θ µ = Θ 0 outside a small neighbourhood of x0;
(iii) each (E,π, Ω µ, Θ µ,J 0,j 0) is an exact Lefschetz ﬁbration;
(iv) there is a holomorphic Morse chart (ξ, Ξ) aroundx0 such that Ξ ∗Ω 1, Ξ ∗Θ 1
agree near the origin with the standard forms ωCn+1 = i
2
∑ dxk∧d¯xk,
θCn+1 = i
4
∑ xkd¯xk− ¯xkdxk.
The proof is based on an elementary local statement about K¨ a hler forms.
Lemma 1.7. Letω be a K¨ ahler form on the ball B =B2n+2(r) of radius r> 0
in Cn+1. Then there is another K¨ ahler form ω′ which agrees with ω near ∂B ,
and which close to the origin is some small multiple of ωCn+1.
Proof. The ﬁrst step is to ﬁnd a K¨ ahler form ω′′ which is equal to ω near ∂B ,
and which has constant coeﬃcients near the origin. For this w rite2ω =β+ddcf ,
withβ constant andf vanishing to second order at x = 0. Take a cutoﬀ function
g∈ C∞(R+, R) such that g(t) = 1 for t≤ 1 and g(t) = 0 for t≥ 2, and set
fǫ(x) = g(||x||/ǫ)f (x). A straightforward computation shows that as ǫ→ 0, the
functionsfǫ not only have increasingly small support, but also tend to 0 i n the
C2 topology. The desired form is, for small ǫ,
ω′′ =ω−ddcfǫ =β +ddc(f−fǫ). (1.5)
In a second step, choose some small t > 0 such that the constant form
β′ =β−tωCn+1 is still K¨ ahler. Take a two-formγ on Cn+1 which is of type (1,1)
and nonnegative everywhere, which vanishes near the origin , and which is equal
to ωCn+1 outside a compact subset; this can be obtained as γ =−ddch(||x||2)
for a suitable convex function h. Pulling γ back by a linear map transforms
it into another nonnegative (1,1)-form γ′, zero near the origin and equal to β′
outside a compact subset. Then γ′′ =γ′ +tωCn+1 is K¨ ahler, equalstωCn+1 near
the origin, and β outside a compact subset. That compact subset can be made
arbitrarily small by retracting linearly and rescaling; th e two-form obtained in
that way can be plugged into ω′′ locally near zero, yielding ω′.
Proof of Lemma 1.6. Take some holomorphic Morse chart (ξ, Ξ) for x0. Lemma
1.7 says that one can ﬁnd a two-form Ω 1 onE which agrees with Ω = Ω 0 outside
im(Ξ), such that Ξ ∗Ω 1 is K¨ ahler and, near the origin, equals cω Cn+1 for some
small constant c > 0. The obstruction to ﬁnding a Θ 1∈ Ω 1(E) which agrees
with Θ = Θ 0 outside im(Ξ) and satisﬁes dΘ 1 = Ω 1 lies in H 2(B,∂B ; R), with
B a (2n + 2)-dimensional ball; which is zero. An arbitrarily chosen Θ 1 needs to
be modiﬁed to make Ξ ∗Θ 1 equal to cθ Cn+1 near x = 0, but that can be done
by adding the diﬀerential of some function to it. By restrict ing ξ, Ξ to smaller
neighbourhoods, and rescaling them by c−1/2 andc−1 respectively, one achieves
2The deﬁnition of dc in this paper is such that ω C = − ddc( 1
4 |z|2). This diﬀers from the
majority convention by a negative constant.
9
that Ξ ∗Ω 1 =ωCn+1 and Ξ ∗Θ 1 =θCn+1 near the origin. Finally, Ω µ and Θ µ are
deﬁned by interpolating linearly between µ = 0 and 1; the required properties
are obvious.
