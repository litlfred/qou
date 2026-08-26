---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-006-22-boundary-slopes-and-homology-of-cable-spaces
section_title: "Boundary slopes and homology of cable spaces"
section_number: 2.2
pages: 6-9
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
---
isotopy class of a simple closed curve on T . Let S(T ) denote the set of slopes of T . The
elements in S(T ) are represented by elements of Q ∪ {1/0}. With this in mind we will
often refer to a slope by its corresponding numerical value. A homology class in H1(T, Z)
is called primitive if it is not a non-trivial integer multiple of another elemen t in H1(T, Z).
There is a 2-1 correspondence between primitive classes in H1(T, Z) and elements in S(T ),
where α, β ∈ H1(T, Z) give the same slope if and only iﬀ α = ±β.
Next we need the following lemma.
Lemma 2.6. Consider a cable knot complement MKp,q = Cp,q ∪ MK as above. Let s ∈
S(T−) be a slope on T− of Cp,q , corresponding to a/b ∈ Q ∪ {1/0}. Suppose that in Cp,q
we have a properly embedded, connected, essential surface F such that:
(1) The boundary ∂F intersects both of T− and T+.
(2) Each component of ∂F on T− has slope s.
(3) The total slope of ∂F ∩ T+ is a boundary slope in MK .
Then a/b is a boundary slope in MKp,q.
Proof. Suppose that the total slope of ∂F ∩ T+ corresponds to c/d ∈ Q ∪ {1/0}. Let E
be a essential surface in MK with ∂E having total slope c/d. By passing to the doubles if
necessary, we may assume that E and F are orientable. Let x and y denote the number
of components of ∂F and ∂E on T+, respectively. In Cp,q consider a surface F ′ that is y
copies of F and in MK consider a surface E′ that is x copies of E. Each of ∂E ′ and ∂F ′
has xy components on T+. After isotopy on T+ we may assume that ∂E ′ = ∂F ′. Now
S = E′ ∪ F ′ is a properly embedded surface in MKp,q. By assumption, each component
of S\\T+ is essential in the component of MKp,q\\T+ it lies in. Thus by Lemma 2.5, S is
essential in MKp,q. □
The following lemma should be compared with [21, Lemma 2.3].
Lemma 2.7. Let Cp,q be a cable space with ∂C = T− ∪ T+ as above. Let S− and S+ denote
the set of slopes on T− and T+ respectively. There is a bijection
φ : S− − → S+,
such that for every s ∈ S − there is a connected, essential properly embedded surface F ⊂
Cp,q , intersecting both components of ∂Cp,q , and such that each component ∂F ∩ T− has
slope s while each component of ∂F ∩ T+ has slope φ(s).
7
Proof. To simplify our notation, throughout this proof, we will use X := Cp,q . Identify
H1(∂X ; Q) with H1(T−; Q) ⊕ H1(T+; Q).
We claim that the maps i± : H1(T±; Q) − →H1(X; Q), induced by the inclusions of
T± in X are isomorphisms. To see that i− is an isomorphism consider the solid torus
X ∪ n(Tp,q ), and apply the Mayer–Vietoris long exact sequence to this d ecomposition. To
see that i+ is an isomorphism decompose X into a ﬁbered solid torus and an I-bundle
T+ × I along a vertical annulus and again apply the Mayer–Vietoris long exact sequence.
The fact that i± are isomorphisms implies the following: Given a primitive c lass α− ∈
H1(T−; Z) ⊂ H1(T−; Q) there is a unique primitive class α+ ∈ H1(T+; Z) ⊂ H1(T+; Q) so
that
(1) α+ = r i −1
+ ◦ i−(α−), for some r ∈ Q.
As discussed above, a slope s ∈ S ± determines a primitive class α± ∈ H1(T±; Z) up to
sign. Given s ∈ S −, determining a primitive element α− ∈ H1(T−, Z) up to sign, deﬁne
φ(s) to be the slope in S+ that describes the class α+ ∈ H1(T+, Z) deﬁned in equation (1).
This clearly deﬁnes a bijection.
By above discussion, there are relatively prime integers m, n such that
mi−(α−) + ni+(α+) = 0 .
Thus the element mα−+nα+ is in the kernel of the map i− ⊕i+ : H1(∂X ; Z) − →H1(X; Z).
Looking at the homology long exact sequence for the pair ( X, ∂X ), we conclude that there
is a class A ∈ H1(X, ∂X ; Z) such that ∂(A) = mα− + nα+ under the boundary map
∂ : H1(X, ∂X ; Z) − →H1(∂X ; Z). Now 3-manifold theory assures that there is a 2-sided,
embedded, essential surface S that represents A [16, Lemma 6.6]. That is [ S] = A. By
construction, each component of ∂S ∩ T− has slope s while each component of ∂S ∩ T+
has slope φ(s).
Now S may not be connected. However since S represents A, we have ∂(A) = mα− +
nα+ ⁄= 0. There must be a component F ⊂ S such that ∂([F ]) ⁄= 0. We claim that F must
intersect both components of ∂X . For, suppose that it doesn’t intersect one component
of ∂X ; say F ∩ T+ = ∅. Then the class ∂([F ]) ⁄= 0 would be a non-zero multiple of
α− ∈ H1(∂X ; Z). But this is impossible, since i−(α−) has inﬁnite order in H1(X; Z).
Thus F ∩ T± ⁄= ∅. To ﬁnish the proof of the lemma, note that since F ⊂ S and S is
essential, each component ∂F ∩ T− has slope s while each component of ∂F ∩ T+ has slope
φ(s). □
2.3. The proof of Theorem 2.2. We are now ready to prove Theorem 2.2. For part (a)
let K be a non-trivial knot and let ( p, q) coprime integers. Suppose that a/b is a boundary
slope of K. Let Kp,q be the cable knot of K. As above we will consider the complement
MKp,q obtained by gluing a cable space Cp,q to the complement MK. We must show that
there is an essential surface S in MKp,q such that the total slope of S ∩ ∂MKp,q is q2a/b.
On the boundary component T− = ∂MKp,q consider a pair ( µ, λ) of meridian and canon-
ical longitude whose homology classes generate H1(T−; Z). Let r := gcd( aq2, b) and let
x = aq2/r and y = b/r. Consider a simple closed curve γ whose numerical slope is x/y.
That is in H1(T−; Z) we have
[γ] = xµ + yλ.
8
By Lemma 2.7, applied for s = x/y we have a slope φ(s) on the other component T+ of
Cp,q such that the following is true: There is an essential, conne cted, properly embedded
surface F ⊂ Cp,q , with ∂F intersecting both components of ∂Cp,q , and such that each
component ∂F ∩ T− has slope s while each component of ∂F ∩ T+ has slope φ(s).
Since Cp,q is a Seifert ﬁbered space, up to isotopy, essential surfaces are either vertical
or horizontal with respect to the Seifert ﬁbration [14]. Sin ce the base space of Cp,q is an
annulus, the only vertical surfaces in Cp,q are annuli. In fact, essential surfaces in cable
spaces are classiﬁed by Gordon and Litherland in [13, Lemma 3 .1]. From that lemma
and its proof, it follows that if F is a vertical annulus in Cp,q , then every component of
∂F ∩ T− has slope pq, while every component of ∂F ∩ T+ has slope p/q. In particular, we
have a/b = p/q and our hypothesis implies that for this to happen p/q must be a boundary
slope of K. On the other hand x/y = pq which, by Lemma 2.3, is always a boundary slope
of MKp,q. Thus the desired conclusion holds in this case.
Now suppose that the surface F is horizontal with respect to the Seifert ﬁbration of
Cp,q . On T− a regular ﬁber of the ﬁbration can be identiﬁed with the knot H := Kp,q .
The only singular ﬁber of the ﬁbration (that has multiplicit y |q|) may be identiﬁed with
the knot K on T+. If N is the number of times that F intersects the regular ﬁbers of Cp,q ,
then since the base of the ﬁbration is an annulus we have
0 − χ(F )/N = 1 − 1/|q|.
It follows that χ(F ) = n′(1 − |q|), where N = n′q. Since the intersection number of µ and
H is 1 we conclude that on ∂T−, the meridian curve µ is a cross section of the ﬁbration and
in H1(∂MKp,q) we have [ γ] = nqµ + mH, where n = n′/r, m ∈ Z and we have ( nq, m) = 1.
On the other hand we must have H = pqµ + λ. Hence we obtain that each component of
[∂F ] = r(nq + mq)µ + rmλ, thus s = x/y = (nq + mpq)/m.
In Cp,q we have a horizontal planar surface that intersects T+ in a single meridian, call
it µ′, and it intersects T− in q copies of µ. This surface may be taken to be the image
of a meridian disk of a neighborhood of K in Cp,q . By choosing appropriate orientations
of µ, µ′, and by the proof of Lemma 2.7, we may assume that φ(µ) = µ′ and that in
H1(Cp,q ; Z) we have µ′ = qm.
In H1(T+; Z), the ﬁber H corresponds to the slope p/q and each component of T+ ∩ ∂F
has the form nµ′ + mH. Thus, as also stated in [13, Lemma 3.1], T+ ∩ ∂F has total slope
(n + mp)/(mq). The number of components T+ ∩ ∂F is t = gcd(n + mp, mq). Since in Q we
have that ( n + mp)/(mq) = a/b we may take a′ := a/w = n + mp/t and b′ := b/w = mq/t,
where w = gcd( a, b). Thus we may assume that φ(s) = a′/b′. By assumption a/b is a
boundary slope in MK. Thus, Lemma 2.6 applies to conclude that s = q2a/b is a boundary
slope in MKp,q. This ﬁnishes the proof of part (a) of Theorem 2.2.
For a non-trivial knot K, part (b) follows at once from part (a). To ﬁnish the proof of
part (b) assume that K is the trivial knot and let ( p, q) coprime integers. Now Kp,q is the
(p, q) torus knot. The only boundary slope of K is a/b = 0/1 and the boundary slopes of
Kp,q are 0 and pq. Thus q2bsK ∪ {pq} = {0, pq} = bsKp,q. □
We close the section with the following corollary that will b e useful to us in subsequent
sections.
9
Corollary 2.8. Let MKp,q = Cp,q ∪ MK be the complement of a cable knot, where |q| > 1.
Let F ⊂ Cp,q be a properly embedded essential surface, that is not an annu lus, and such that
each component of ∂F ∩ T+ has integral slope a. Suppose that there is a connected essential
surface S′ ⊂ MK such that each component of ∂S ′ has slope a. Then the followings hold.
(1) ∂F ∩ T+ has |q| components and ∂F ∩ T− has a single component of slope q2a ∈ Z.
(2) There is a connected essential surface S ⊂ MKp,q, such that each component of ∂S
has slope q2a and
χ(S) = |q|χ(S′) +
⏐⏐∂S ′⏐⏐(1 − |q|)|p − aq|,
where |∂S ′| denotes the number of boundary components of S′. Furthermore, we
have |∂S | = |∂S ′|.
Proof. Let F be as in the statement above. By the proof of Theorem 2.2, sinc e F is not
an annulus, F may be isotopied to be horizontal with respect to the Seifert ﬁbration of
Cp,q . Furthermore, ∂F ∩ T+ has total slope ( n + mp)/(mq), while ∂F ∩ T− has total slope
(nq + mpq)/m, for some coprime integers m, n. The number of components of ∂F ∩ T+ is
t = gcd( n + mp, mq), and each has slope b/c where b = ( n + mp)/t and c = mq/t. Since
b/c ∈ Z and gcd( m, n) = 1, it follows that m = ±1 and t = |q|. Hence n = m(qa − p),
where we will have m = 1 or m = −1 according to whether qa ≥ p or qa ≤ p. Furthermore
n > 0, χ(F ) = n(1 − |q|). The rest of the claims in part (1) follow.
Now we prove part (2): By the proof of Theorem 2.2, an essentia l surface S realizing
the boundary slope q2a for Kp,q is as in the proof of Lemma 2.6. Since ∂F ∩ T+ has |q|
components, S is constructed by gluing |q| copies of S′ with |∂S ′| copies of F . Hence we
have
χ(S) = χ(MK ∩ S) + χ(Cp,q ∩ S) = |q|χ(S′) +
⏐⏐∂S ′⏐⏐|aq − p|(1 − |q|).
The last equation follows from the fact that χ(Cp,q ∩ S) = |∂S ′|χ(F ) and the above
discussion on χ(F ). □
