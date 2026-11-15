---
doc_id: 1104248094
doc_title: "Hochschild and cyclic homology of quantum groups"
section_id: sec-006-51-formal-functions
section_title: "Formal Functions"
section_number: 5.1
pages: 21-25
source_pdf: 1104248094.pdf
source_sha256: c1fdb4791afcad3b
toc_source: inferred
doc_brief: "Hochschild and cyclic homology of quantum groups — For an arbitrary complex linear semisimple Lie group G, we consider Hopf algebras of the deformations of the formal and algebraic functions on G."
---
This is the reason for us to treat formal and algebraic functions separately.
5.2. Algebraic Functions. Now we do not have a nice filtration for C[XC] as we
have for C
f(Kc), so we have to look for other ways to compute the Lie algebra
homology for algebraic functions. First of all we notice the following
Lemma (5.2.1). σ and σ0 commute with the right translation by the Carton subalgebra
o/g
Proof. Right translation corresponds to the action of left invariant vector field.
V/ίeh, notice that [H
l
9ωr]=Q and adH(R) = Q, it is obvious that we have
[H*,σ(J
fl)] = 0. This should also be obvious from the geometric interpretation of
the actions σ and σ0.
For algebraic functions on Kc, the infinitesimal right action of the Cartan
subalgebra acts semi-simply, with the eigenvalues ranging over the weight lattice
Λ of (g, h). We have the decomposition
©Kλ, 
(5.9)
λeΛ
and because of the previous lemma we have
®Hn<s*,Vλ). 
(5.10)
λeΛ
502 
P. Feng and B. Tsygan
We can identify Vλ as
Kλ^{/6C
Λ(Gc)|/(^)-e-
(Λ-^w/(^),V^6Gc,X6hc0nc}, 
(5.11)
where hc = tc 0 ac, tc is the Cartan subalgebra of kc ^ g, λ is a linear functional on
tc extending trivially to that on hc0nc,pa is a linear functional on a c©n c^g*
extending to that on hc 0 nc; g* acts on Vλ by σ = σ0 + pa and σ0 has been identified
with the infinitesimal left translation.
We notice the close relationship between our Vλ and induced representation
[25] for real Lie group G. Let Uλ be a (T,ac)-module such that T acts by e
λ and
ac acts trivially. The induced representation for G is defined as
(5.12)
where λ is real linear on t and complex linear on tc, extends naturally to hc® nc;pa
is real linear on a and complex linear on ac, extends naturally to hc©nc; and G
acts by left translation
(gf)(h) = f(g-
1h\ 
V0,ΛeG. 
(5.13)
The Lie algebra of G acts by infinitesimal left translation, which extends naturally
to an action of the complexified Lie algebra gc. Note in (5.12) the minus sign in
front of pa is due to the fact that our nc corresponds to the negative restricted roots.
Here we use TAN to denote the minimal parabolic subgroup instead of the
standard MAN since we want to emphasize the fact that M:= Zx(ac) = T (because
G is also complex). Since G,X are real forms of GC,KC we have natural
homomorphism from Vλ to lndγAN(Uλ). 
Actually Vλ is identified with the
Harish-Chandra module [18,25] of Ind°AN(Uλ).
We thus have reduced the computation of the E
2 of the spectral sequence
converging to the Hochschild homology of the quantum algebraic groups to the
computation of Lie algebra homology of ac © nc with coefficient in Harish-Chandra
modules Vλ for λeλ the weight lattice of (kc, tc). We will also think of λ as a linear
functional on hc = tc©ac with λ\Λc = 0. As for the formal functions we will use the
double complex (4.22) to compute the Lie algebra homology, but this time we
compute the nc-homology first. The nc-homology of Harish-Chandra modules
has been extensively studied for its importance in representation theory [6,18].
But unfortunately the nc-homologies of Harish-Chandra modules are not explicitly
known in general. What makes life much easier for us is the following. First of all
G has a complex structure G ^ Kc and TAN is a minimal parabolic subgroup.
Secondly we only consider those induced representations lndγAN(Uλ) such that ac
acts on Uλ trivially. As we will see this simplifies the computation a great deal.
Thirdly even in our special cases we do not need a full knowledge of nc-homology
of Harish-Chandra modules. #*(nc, Vλ) is only the E
1 term of the spectral sequence
associated with the double complex (4.22), its E
2 term is //π(ac,//.(nc, Vλ}\ so we
may forget about those of nc-homology on which ac acts with non-zero (generalized)
eigenvalues.
Let us first recall some facts about Harish-Chandra modules.
Lemma (5.2.2) [5]. Any Harish-Chandra module is finitely generated over U(nc).
Hochschild and Cyclic Homology of Quantum Groups 
503
Lemma (5.2.3) [18]. The nc-homology of any Harish-Chandra module is a
Harish-Chandra module for MA (which in our case is TA).
So nc-homology of Harish-Chandra 
module is finite dimensional, and
decomposes into Jordan cells under the action of tcφac. We define the generalized
eίgenspace with generalized eigenvalue μea* to be the largest subspace on which
x — μ(x) acts nilpotently for all xeac. Note T acts semisimply on C[XC] and Fλ,
thus also acts semisimply on H ^(n^ Vλ). But in general ac does not act semisimply
on Vλ so we expect some non-trivial Jordan cells in H^(nc, Vλ) with respect to the
action of ac.
Definition (5.2.4) [18]. Let V be a Harish-Chandra module for G, then vea* is a
homology exponent of H^(nC9 V) if HH^.(nc, V)v ^0, where
#*(
nc> JOv = generalized (v — pa) eίgenspace of #*(nc, V). 
(5.14)
A leading homology exponent is one that cannot be expressed as the sum of another
homology exponents and a non-zero sum of negative restricted roots, i.e., leading
homology exponents are the largest ones with respect to the obvious partial order
induced by the positive restricted roots.
The shift by pa is to make the notation compatible with Harish-Chandra's
labelling of the infinitesimal characters of Z(gc), the minus sign in front of pa is
determined by the fact that our nc corresponds to the negative restricted roots.
Note that we are only interested in those of H^(nc, V) on which ac acts
nilpotently via σ = σ0 + pa, i.e., ac acts by generalized eigenvalue (— pa) via σ0.
Recall that σ0 is the natural geometrical action, thus we are only interested in the
homology exponent zero.
Lemma (5.2.5) (Schmid's Vanishing Theorem [18, 38]). Let vbea leading homology
exponents, then Hn(nc, V}v = 0, unless n = 0.
The best we can hope now is that zero is the leading homology exponent. Then
only //0(nc, Vλ) contributes to the ac-homology, therefore the spectral sequence of
the double complex (4.22) is degenerate at E
2, i.e.,
HΛ(acθnc, Vλ) = E* ^ E
2
n = Hn(*c,H0(nc, Vλ)) * C
/(Λ)® Λ"ac, 
(5.15)
where l(λ) is the number of irreducible Jordan cells in #0(nc, Kλ)0. Actually zero
is a leading exponent (thus the unique one) as a consequence of the following
lemma, which also gives the dimension of H0(ac, Vλ)0.
Lemma (5.2.6) (Osborne's Conjecture [18]). Let V be a Harish-Chandra module
of G, ΘG(V] the global character, then
(5.16)
where. G' is the set of the regular semisimple elements of G. (TA) 
is specified as
follows:
504 
P. Feng and B. Tsygan
(TA)~ = interior, in TA, of the set
(5.17)
p 
j
where A ~ is the negative Weyl chamber cut out by the positive restricted root system,
A' = {aeA\e«(a) < 0, VαeΦ
+(gc,ac)}.
The restriction to G' is to avoid certain singularities in the global character,
and the restriction to (TA)~ is to avoid complicated sign conventions. Actually
every T^l-character is completely determined by its restriction to (TA)~ nG'. We
remind the reader that the above formulation is for our case in which G has a
complex structure. In general one should write MA in the place of TA.
The global character of induced representations is known. See, for example,
[25,45]. It is especially simple in our case.
where tae(TA)~ nG', W the Weyl group of (kc,tc).
One immediately sees that zero is the leading homology exponent. Indeed,
according to Schmid's vanishing theorem there is no cancellation in the alternating
sum on the right-hand side of (5.16) for the leading homology exponents, so they will
show up on the right-hand side. But zero is the only exponent one can count on the
left-hand side of (5.16). Another immediate consequence is
dim (#0(nc, KΛ)0) = \W\ = the order of the Weyl group. 
(5.19)
Therefore when λ is regular, i.e., w^λ = w2λ, if and only if w x = w2, there are
no non- trivial Jordan cells and we get l(λ) = \W\. When λ is singular there might
be non-trivial Jordan cells and we will see there are. The last lemma we are going
to quote from representation theory is the Frobenius reciprocity theorem which
will help us pin down H0(nc, Vλ)0.
Lemma (5.2.7) (Frobenius Reciprocity Theorem [5]). Let V be a Harish-Chandra
module for G, Uff v be a (T,ac)-module such that T acts by character σ and ac acts
by vea*. Then we have
Hom^ίFJnd^^)) ^ Hom(r>tcθac)(tf0(nc, K), I7σ§v). 
(5.20)
The isomorphism in the reciprocity theorem is given as follows. For
ΦeHom(X>gc)(K, Ind?^(l/,iV)), define
φ:V-^υσ^ 
φ(υ)=Φ(υ}(e\ 
Vt eK 
(5.21)
It is easy to see that φeHom(T tcθflc)(#0(nc, V\ Uσ t V) and Φis uniquely determined
by Φ
Note the right-hand side of (5.20) only counts the irreducible Jordan cells of
tc0ac, but tc acts semisimply so it only counts those of ac. This is exactly what
we are interested in for ac-homology. Now we need to know the dimension of the
space of the intertwining operators between our Vλ and lnd^AN(Ue^ 1>0), weW. It
is known that this is one ([25] Theorem (14. 13), (14.43)). So the number of the
