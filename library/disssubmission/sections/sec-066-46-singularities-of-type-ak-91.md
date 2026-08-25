---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-066-46-singularities-of-type-ak-91
section_title: "Singularities of type Ak 91"
section_number: 4.6
pages: 99-103
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
So it sufﬁces to show
Hi
c(E,Λ) =



Λ(− i
2) if i∈{2,4, . . . ,2n−2}\{ n},
Λ2(− i
2) if i = n andn is even,
0 otherwise .
For this we use that the projection[u0 : u1 :··· : un]↦→ [u1 :··· : un] with
centerp deﬁnes a rank one vector bundle
π : E−→Qn−1⊂ Pn−1
over the smooth quadricQn−1 ={[u1 :··· : un]∈ Pn−1| u2
1 +··· +u2n = 0}
of dimensionn−2. Using Poincar´e duality and the homotopy invariance of
cohomology, we thus obtain
Hi
c(E,Λ)∼= (H2n−2−i(E,Λ)(n−1))∨∼= (H2n−2−i(Qn−1,Λ)(n−1))∨
and the result follows by plugging in on the right hand side the cohomology
of the smooth quadricQn−1. □
CHAPTER 5
A family of surfaces with monodromyW(E6)
LetX be a complex principally polarized abelian variety (ppav for short)
of dimensiong≥ 2, and ﬁx a theta divisorΘ⊂ X which deﬁnes the given
polarization and which is symmetric in the sense that it is stable under the
inversion morphism−idX : X−→X. For points x∈ X(C) let Θx = Θ+x
denote the corresponding translate of the theta divisor. The geometry of the
intersections
Yx = Θ∩Θx
is closely connected with the moduli of the given ppav and has been studied
in relation with Torelli’s theorem [25], with the Schottky problem [27] and
with the Prym map [61]; these intersections are also among the few concrete
examples for varieties with ample cotangent bundle [24]. One of our goals
is to understand how their cohomology varies with the pointx. As we will
see later on, this is closely related to the convolution square of the theta
divisor (in the sense of the previous chapters).
To set the stage for what follows, in section 5.1 we discuss some general
features of the intersectionsYx. If the theta divisor is smooth or has at most
isolated singularities, then for generalx∈ X(C) a Bertini-type argument
will show thatYx is smooth and that the involutionσx : Yx−→Yx, y↦→x−y
is ´etale so that the quotient
Y+
x = Yx/σx
is again a smooth variety. After a survey of the casesg≤ 3 where a close
connection with the moduli of Prym varieties emerges, we focus on the
dimensiong = 4. Here we are dealing with a family of smooth surfaces of
general type with a beautiful explicit geometry. We will see that the varying
part of the cohomology of these surfaces deﬁnes over a Zariski-open dense
subsetU⊂ X a variation of Hodge structuresV+ of rank six whose ﬁbres
are of pure Hodge type(1,1). One of the main results of this chapter will
be the proof of the following conjecture of R. Weissauer.
THEOREM 5.1. For a general complex ppav X of dimension g= 4, the
monodromy group G of the local system underlyingV+ is either the Weyl
group W(E6) or its unique simple subgroup of index two which is the kernel
of the sign homomorphism sgn: W(E6)−→{±1}.
93
94 Chapter 5 – A family of surfaces
Here by the monodromy groupG = Im(π1(U,x)−→AutC(V+,x)) we
mean the image of the monodromy representation of the fundamental group
on the stalk ofV+ at some chosen pointx∈U(C). Up to isomorphism this
image is of course independent of our choices.
We remark that the occurance of the Weyl groupW(E6) in the present
context can be related to the 27 lines on a cubic surface via the work of
E. Izadi on Prym-embedded curves [61], though this relationship will not
be used in what follows (for more about this see section 5.5 below). For the
proof of theorem 5.1 a detailed guideline will be provided in section 5.2,
so let us here only mention the most important points. To show that the
monodromy groupG must be a subgroup ofW(E6), we give in section 5.3
and 5.4 a detailed study of the integral cohomology and of the N´eron-Severi
lattices of the smooth surfacesYx andY+x for generalx∈ X(C). Once this
has been done, the main task will be to ﬁnd a sufﬁciently large lower bound
on the monodromy group. For this we use two ideas. On the one hand, in
section 5.6 we relate the variation of Hodge structuresV+ to the convolution
square of the theta divisor — this allows to apply the Tannakian formalism
from chapters 2 and 3 and theorem 4.2 to conclude that for a general ppav
the monodromy groupG acts irreducibly on the stalks. On the other hand, a
degeneration argument will show that in dimensiong = 4 this monodromy
group contains as a subgroup the corresponding monodromy group for the
Jacobian varietyJC of a general curveC.
For Jacobian varieties we have the following result. LetC be a smooth
complex projective curve of even genusg = 2n, and identify the symmetric
product
Cn = (C×···× C)/Sn
with the set of effective divisors of degreen. We then have the difference
morphism
dn : Cn×Cn−→JC = Pic0(C)
which sends a pair(D,E) of effective divisors of degreen on the curveC
to the isomorphism class of the line bundleOC(D−E). Using the Poincar´e
formula we will see in section 5.8 that the morphismdn is generically ﬁnite
of degree N =(2n
n
). In particular, over some Zariski-open dense subset
of X the difference morphism restricts to a ﬁnite´etale cover, and it makes
sense to speak of its Galois groupG(dn). An application of Brill-Noether
sheaves [106] to be explained in proposition 5.24(b) shows that if C is
a non-hyperelliptic curve of genusg = 4, the Galois groupG(d2) can be
identiﬁed in a natural way with the monodromy group of the local system
underlyingV+ on the Jacobian variety. The desired lower bound for the
proof of theorem 5.1 is then given by the following observation.
