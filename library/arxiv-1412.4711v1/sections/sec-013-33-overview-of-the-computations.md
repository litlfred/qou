---
doc_id: arxiv-1412.4711v1
doc_title: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT"
section_id: sec-013-33-overview-of-the-computations
section_title: "Overview of the computations."
section_number: 3.3
pages: 13-16
source_pdf: 1412.4711v1.pdf
source_sha256: 4fb1d6ee062cca8c
doc_brief: "CHARACTER VARIETIES FOR SL (3, C): THE FIGURE EIGHT KNOT — We give a description of several representation varieties of the fundamental group of the complement of the ﬁgure eight knot in PGL(3, C) or"
---
be proven using a prime decomposition of the ideal
ID =⟨Le∪Lf∪Lc⟩.
Indeed, as Defor(M,T ) is the zeroes set of this ideal, a prime decomposition
would give the three components and we would be able to check their proper-
ties. However, our system depends on 12n variables (24 variables in the case
of the ﬁgure eight knot complement) and is of rather high degree (degree
6 for some equations for the ﬁgure eight knot complement). So we are far
beyond the scope of the state of the art algorithms of prime decomposition.
We will use the shape of the equations to simplify the system. The method
we present is rather general for this kind of systems up to some points
(number of factors in some polynomials). It could be applied, in principle
on numerous systems with the same properties. For example, it can replace
14 E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
the one used in [11]. Before explaining our method, let us deﬁne one more
object: forbidden points.
Denote by SD =Le∪Lf∪Lc the set of polynomials generating the ideal
ID. Note that if z∈ V (ID)⊂ C12n, then none of its coordinates belong
to{1, 0} because of the equations induced by the internal relations Lc.
We hence call forbidden points the points with any coordinate in {0, 1} and
we introduce FD ={z,z − 1,z ∈ Z}⊂ Q[Z]. It may seem useless at this
point as this is contained in the internal relations. But recall that we will
eliminate a lot of variables through projections. During these projections, as
said before, some spurious components (i.e. all included in forbidden points)
may appear. So we will always keep the equations deﬁning the forbidden
points and saturate our ideals by these equations. This will lower the number
of components and ease the computations.
Here are the steps of our method:
• Step A: elimination. We iteratively detect equations inSD which
are aﬃne in a variable, i.e. of the form
Dz(X)z−Nz(X) with X⊂Z\{z},
and with the additional condition that Dz(X) cancels only at for-
bidden points. We can then substitute z by Nz(X)
Dz(X) in the other
polynomials generating ID, take the numerators of these equations
and remove their factors (algorithm [ γ]) that cancel exclusively at
forbidden points (and thus never cancel on Defor(M,T )). This gives
a new ideal with one less variable and one less equation.
At the end of the process, denote by SY ⊂ Q[Y ] with Y ⊂Z the
remaining equations. We keep in mind, through the set RY⊂ Q[Z],
the equations used for the substitutions. Of course, by substituting
inRY , we may assume that all these equations express a substituted
variable in terms of the variables in Y , i.e. they have the form:
Dz(Y )z−Nz(Y ), with z∈Z\Y .
We also want to keep in mind the forbidden points. So denote by
FY ∈ Q[Y ] the list of prime factors that appear in FD after having
performed the same substitution.
We can interpret the relations RY = 0 as a projection πY :
Defor(M,T )→ V (⟨SY⟩) which is not necessarily surjective. How-
ever, the complement of the image V (⟨SY⟩)\πY (Defor(M,T )) only
contains forbidden points which might have been introduced by the
use of rational fractions in the substitutions.
So we compute (algorithm [β]) the idealIY , which is the saturation
of⟨SY⟩ byFY in order to get V (IY ) =πY (Defor). The union of the
zeroes of the polynomials FY deﬁnes the forbidden points of V (IY )
which are images by πY of the forbidden points of C12n.
Putting this in a diagram, we have :
15
C12n → C♯Y
Defor(M,T ) ≈πY V (IY )\ (∪f∈FYV (f))
(x,y ) → y(
Nx(y)
Dx(y),y
)
← y.
• Step B: splitting. In IY , we ﬁnd a polynomial PY ∈ Q[Y ] that
factorizes (algorithm [γ]) intok factors in Q[Y ] : PY =∏
i=1...kPY,i.
By construction, as Defor(M,T ) does not contain forbidden points,
we then get Defor(M,T ) =∪i=1...kV (JY,i), where JY,i⊂ Q[Z] is the
saturation of ID +⟨PY,i⟩ byFD.
We can even further saturate our ideals, in order to avoid the same
component appearing twice. We perform cascading saturations for
some permutation σ of the indices: we iteratively compute (algo-
rithm [β]) the ideal IY,σ(i) =IY +⟨PY,σ(i)⟩ and saturate this ideal by
FY as well as with{PY,σ(1),...,P Y,σ(i−1)} in order to remove possible
components that are already in IY,σ(1),...,I Y,σ(i−1). The eﬃciency
of the process strongly depends on the chosen permutation.
At the end of this step, one can set Di = V (IY,i +ID). By con-
struction,Di is the inverse image byπi of the zeroes set of IY,i. And
we get the decomposition:
Defor(M,T ) =∪i=1...kDi.
• Step C: further elimination. The ideals IY,i are still too big to
perform directly a prime decomposition. So, for each IY,i, we apply
once again step A. We may even try to iteratively apply Steps A
and B and so on, but in our case, a single additional pass of Step A
turns out to be enough. So we explain only this single pass.
Indeed, for each IY,i, we ﬁnd a polynomial that is aﬃne in one
of the variables and, moreover, can be written ai(z)y +bi(z) with
z ∈ Yi = Y \{y} and ai(z) only vanishing at forbidden points.
We stress that the suitable variable y to eliminate depends on the
diﬀerent ideals IY,i.
The result of Step A is then an ideal IYi⊂ Q[Yi] together with
a projection πYi : V (IY,i)→ V (IYi) and a set of polynomials FYi
(deﬁning the forbidden points of V (IYi)) such that we get:
πYi(V (IY,i)) =V (IYi).
Setting πi =πYi◦πY , we may write πi(Di) =V (IYi) and get the
diagram similar to the previous one:
C12n → C♯Y−1
Di ≈πYi
V (IYi)\ (∪f∈FYi
V (f))
Beware that the diﬀerent projections πYi are only deﬁned on their
respective component Di and do not land in the same space, as the
last eliminated variable may diﬀer for diﬀerent components.
16 E. FALBEL, A. GUILLOUX, P.-V. KOSELEFF, F. ROUILLIER AND M. THISTLETHWAITE
• Step D: Prime decomposition. At this stage, each ideal IYi be-
longs to the scope of a Prime Decomposition algorithm (named here
algorithm [η]). Doing so, we extract the Q-irreducible components
or just a check that theIYi is prime. We denote by IYi,k the diﬀerent
prime ideals appearing in the decomposition of IYi.
The Steps A to D are general functions that also have been applied for
other computations, for example for computing unipotent solutions for many
cases of varieties with a triangulation involving up to 4 tetrahedra ([11]).
At this point, we have a decomposition of Defor( M,T ) in components,
for which we have a prime decomposition. Proving the theorem for this
decomposition is now just a matter of checking properties and here the
method is very speciﬁc to the ﬁgure eight knot complement. Other manifolds
M may give other behaviors. In particular, it turns out in our case that, at
this step, each ideal IYi has a component principal and prime and maybe
another component of lesser dimension and which is redundant:
• Speciﬁc Step 1: irreducibility and smoothness Check that for
each i there is a unique prime ideal of maximal dimension among
the prime factors. We denote here by IYi,1 this prime factor. Check
that Defor(M,T ) is included in the union of the π−1
i (IYi,1). In other
terms, the components of lesser dimension are redundant. Then
check that eachIYi,1⊂ Q[Yi] is a principal ideal of Q[Yi] (the output
of algorithm [α] is a unique polynomial), and, if so, denote by Hi∈
Q[Yi] its generator.
Eventually verify (algorithm [γ]) thatHi is irreducible in C[Yi] and
check that the singular points of each Hi are exclusively forbidden
points.
• Speciﬁc Step 2: connectedness. LetIi be the ideal generated by
IYi,1 and ID. It veriﬁes that V (Ii) = Di. We compute (algorithm
[α]) the ideal I1 +... +Ik. And we check if is not trivial.
If the results of these two speciﬁc steps are indeed what is announced, then
the theorem is easily proven: πi(Di) is a dense open set in V (Hi) which is
a smooth aﬃne (irreducible) variety so that πi(Di) and thus Di are smooth
and connected. Moreover, as the ideal I1 +... +Ik is not trivial, we get
that D1∩... ∩Dk is a non empty set of points. As each Di is connected,
we conclude that Defor(M,T ) =∪i=1...kDi is connected.
