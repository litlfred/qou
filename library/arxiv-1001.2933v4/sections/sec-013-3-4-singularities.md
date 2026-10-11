---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-013-3-4-singularities
section_title: "Singularities"
section_number: "3.4"
pages: 48-55
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
doc_brief: "Analytic Continuation Of Chern-Simons Theory — The title of this article refers to analytic continuation of three-dimensional ChernSimons gauge theory away from integer values of the usual coupling"
---
3.4 Singularities
In studying an oscillatory integral Rd
nx exp(iλf), for a single and fairly generic polynomial
f, it is reasonable to expect that the critical points of f are isolated and irreducible, as we
have assumed so far. But as soon as f depends on one or more parameters, one should
expect to meet singularities, where two or more critical points meet.
Singularities play an important role because Stokes surfaces always pass through the locus
(in the parameter space of the polynomial f) at which two or more critical points meet. If
we vary a parameter in f so that two critical points pσ and pτ coincide, then f(pσ) = f(pτ ),
which certainly ensures that Im (iλf(pσ)) = Im (iλf(pτ )). So a Stokes surface always passes
through the singular locus with pσ = pτ .
Moreover, the flow equations simplify at a singularity. To understand what happens to
the Lefschetz thimbles in crossing a Stokes surface, in general we must solve the flow equation
in n complex dimensions. However, near a singularity, most of the n complex variables are
unimportant. If a singularity can be modeled by the behavior of a complex polynomial in
k variables – where in practice k will often be 1 or 2 – then near the singularity, the flow
equations reduce effectively to equations for those k variables; the other modes are “massive”
and decay quickly in solving the flow equations.
The relation between singularities and Stokes phenomena is therefore very useful in practice. Indeed, the subject reviewed in this section was developed partly for analyzing singularities and their relation to oscillatory integrals [35].
In section 5, where we study the analytic continuation of the colored Jones polynomial,
we will vary one parameter (the ratio of the highest weight of a representation to the ChernSimons level) and we will encounter three rather generic types of singularity. These will be
described here.
3.4.1 More on the Airy Function
The only singularity that arises generically in varying a single complex parameter in the
absence of any symmetries is a meeting of two critical points. Even if this phenomenon
happens in complex dimension n, only one complex variable is essential in describing it. We
48

simply consider a cubic polynomial that depends on a parameter ǫ:
f(x) = x
3
3
− ǫx. (3.54)
There are two critical points at x = ±
√
ǫ; they meet at ǫ = 0.
The corresponding oscillatory integral I(λ, ǫ) = Rdx exp(iλf) is essentially the Airy
function. We can use the scaling x → xλ−1/3to express this integral in terms of a function
of one variable:
I(λ, ǫ) = λ
−1/3
I(1, λ2/3ǫ) = λ
−1/3
Z
dx exp(i(x
3 − λ2/3
ǫx)). (3.55)
Setting ǫ = 0, a special case is I(λ, 0) ∼ λ
−1/3
. Comparing this to a Gaussian integral
Ie(λ) = Rdx exp(iλx2) ∼ λ
−1/2
, the ratio is
I(λ, 0)
Ie(λ)
∼ λ
1/6
, λ → ∞. (3.56)
These facts will be useful in section 5.3.2.
For our remaining remarks, we use the above scaling to reduce to the case λ = 1. The
good regions at infinity in the complex x-plane where exp(if(x)) decays are then independent
of ǫ and were sketched in fig. 1. The Lefschetz thimble associated to a critical point always
connects two of the good regions.
Since the values of I = if at the critical points are ∓2ǫ
3/2/3, the condition for a Stokes
curve is that ǫ
3/2
should be imaginary; thus Arg ǫ should equal π or ±π/3. In particular,
several Stokes curves meet at ǫ = 0. It is clear why this is so: at ǫ = 0, the two critical points
meet, and therefore have the same value of I and in particular the same value of Im I.
Our application will involve the case that ǫ is real. If ǫ is positive, we write p± for
the critical points at x = ±
√
ǫ, and J± for the corresponding Lefschetz thimbles. If ǫ is
negative, we write pe± for the critical points at which the action is positive or negative,
respectively. Thus the points pe± are located at x = ∓i
√
−ǫ, and the action takes the values
I± = ±(2/3)(−ǫ)
3/2 at those points. We write Je− for the Lefschetz thimble associated to
pe−. The Lefschetz thimble Je+ associated to pe+ is ill-defined if ǫ < 0, because the ray ǫ < 0
is a Stokes ray. We define Je+ by taking the limit as ǫ approaches the negative axis from
above.
It is not difficult to describe the cycles J± and Je± qualitatively as curves in the complex
x-plane (fig. 4). From the figure, we see that the relation between these two bases for the
49

J− J+
Imx
Rex
a) b)
J˜−
J˜+
Imx
Rex
Figure 4: Qualitative behavior of Lefschetz thimbles for the Airy function for ǫ > 0 (a) and ǫ < 0
(b). In case (b), ǫ has been given a small imaginary part, since the negative ǫ axis is a Stokes curve.
relative homology is
J+ = −Je+ + Je−
J− = Je+ (3.57)
or equivalently
Je+ = J−
Je− = J+ + J−. (3.58)
3.4.2 An Example With SO(2) Symmetry
Now we will consider a singularity that can arise by varying one parameter in the presence
of SO(2) symmetry. A minimal case is a singularity that can be modeled by two variables
x, y, with SO(2) acting on the xy plane by rotations. The basic invariant is x
2 + y2
. The
origin x = y = 0 is a critical point of any SO(2)-invariant polynomial. There may also be
critical orbits characterized by nonzero values of x
2 + y2
. A meeting of two critical orbits
both with x
2 + y2 6= 0 can be modeled again by the Airy integral – the SO(2) action just
factors out. The new case is a collision between a critical orbit with x
2 + y2 6= 0 and the
critical point at the origin.
Like a collision of two critical points in the absence of any symmetry, this can happen
naturally as a result of adjusting one parameter. We simply consider the polynomial f(x, y) =
(x
2+y2
)
2/2−ǫ(x2+y2
). There is a critical point at x = y = 0 and a critical orbit x
2+y2 = ǫ.
We denote these as p and O respectively. O contains real points if ǫ > 0 but not if ǫ < 0.
As a real critical orbit, O thus disappears in passing through ǫ = 0. Setting I = iλf with
50

Figure 5: The two lines ǫ = r exp(±πi/2), with real r, are Stokes lines in the sense that flows
between the critical point p and the critical orbit O are possible on these lines. Jumping, however,
occurs only in crossing the line ǫ = r exp(−πi/2), shown here as a solid line. There is no jumping
of Lefschetz thimbles in crossing the dotted line.
λ > 0, the values of I on the critical orbits are Ip = 0 and IO = −iλǫ2/2. So the Stokes
curves are given by Re ǫ
2 = 0, which corresponds to the pair of lines ǫ = r exp(±πi/2), with
real r (fig. 5). As expected, they meet at the singularity at ǫ = 0.
A simple scaling reduces I(λ, ǫ) = Rdx dy expiλ(x
2 +y2
)
2 −ǫ(x2 +y2
)


to a function
of one variable. Setting x, y → λ
−1/4x, λ−1/4
y, we get
I(λ, ǫ) = λ
−1/2
I(1, λ1/2ǫ) = λ
−1/2
Z
dx dy expi

(x
2 + y2
)
2 − λ1/2
ǫ(x
2 + y2
)


. (3.59)
Setting ǫ = 0, a special case is I(λ, 0) ∼ λ
−1/2
. Let us compare this to the large λ behavior
for ǫ 6= 0. Assuming that (as in our application in eqn. (5.24)), the dominant contribution
comes from the isolated, nondegenerate critical point at x = y = 0, a simple scaling shows
that I(λ, ǫ) ∼ 1/λ for ǫ 6= 0, so the analog of (3.56) is
I(λ, 0)
I(λ, ǫ)|ǫ6=0
∼ λ
1/2
, λ → ∞. (3.60)
By introducing polar coordinates in the xy plane, I(λ, ǫ) can be expressed in terms of the
error function.
51



 J
P
J
O
J
P
J
O
u
v (b) v
u
(a)
Figure 6: For real ǫ, the cycle Jp is derived from a curve in the uv plane that starts at (u, v) =
(−ǫ, 0) and consists of half of one branch of the hyperboloid u
2 − v2 = ǫ2
. We pick the half that
is asymptotic to the curve u = v. For ǫ < 0, the relevant half is asymptotic to u = v = ∞, as
sketched in (a). For ǫ > 0, it is asymptotic to u = v = −∞, as sketched in (b). Accordingly, the
cycle Jp jumps when ǫ changes sign. The jumping is by Jp → Jp + JO, where JO is associated to
the line u = v in the uv plane, irrespective of the sign of ǫ. In other words, Jp in (a) or Jp + JO
in (b) is a path from (u, v) = (−ǫ, 0) to u = v = ∞.
The Lefschetz thimbles associated to critical orbits can be explicitly described in this
example, because the symmetry can be used to reduce everything to complex dimension 1.
Picking the Kahler metric ds
2 = |dx|2 + |dy|2
, the moment map for the action of SO(2)
becomes µ = −i(xy − yx). Setting µ = 0, we find that by an SO(2) rotation we can set
y = 0. The Lefschetz thimbles that lie at µ = 0 are therefore surfaces of revolution that can
be constructed by acting with the group SO(2) on a real curve in the complex x plane. For
the rest of our analysis, we scale x to set λ = 1.
The flow equation has a conserved quantity Im (if), so to find the right curve in the
x-plane, we do not need to solve flow equations; it suffices to set Im (if) to a constant.
Equivalently, we must set Re (x
2 − ǫ)2
to a constant c. Setting x
2 = ǫ + u + iv, the condition
becomes u
2 − v2 = c. For the Lefschetz thimble JO that flows down from the critical orbit
x
2 +y2 = ǫ, we set c = 0, and choose the branch u = v to ensure that the real part of if(x, y)
is negative. The Lefschetz thimble Jp that flows down from the critical point x = y = 0
passes through ǫ+u+iv = 0, so the constant u
2 −v2 = Re((u+iv)2
) is equal to Re(ǫ
2
). The
hyperboloid u
2 − v2 = Re (ǫ2
) has two branches. We pick the branch that passes through
(u, v) = (−ǫ, 0) (in other words, x = 0), and then Jp is derived from the half of this branch
that is asymptotic to u = v. As shown in fig. 6, this branch is asymptotic to u, v >> 0 or
u, v << 0 depending on ǫ. In particular, if ǫ is real, Jp has different asymptotic behavior
depending on the sign of ǫ.
52

From the figure, we can read off that between ǫ < 0 and ǫ > 0, the Lefschetz thimbles
change by
Jp → Jp + JO
JO → JO. (3.61)
The meaning of the second statement is that the curve JO, which is the diagonal u = v,
is unchanged in going from fig. 6(a) to fig. 6(b). But Jp in fig. 6(a) is a path from
(u, v) = (−ǫ, 0) to u = v = +∞, while in fig. 6, it runs from (−ǫ, 0) to u = v = −∞. In
fig. 6(b), to get a path from (−ǫ, 0) to (+∞, +∞), we need to take the sum Jp + JO. So Jp
jumps in passing through ǫ = 0, though JO does not. Invariance of JO has a more general
explanation that was described in section 3.3.4.
To recover the Lefschetz thimbles Jp and JO, we have to “rotate” (via SO(2)) the curves
that are sketched in fig. 6. In the case of Jp, the relevant curve is topologically a half-line
whose endpoint is SO(2)-invariant. Rotating it by SO(2), we find that as a manifold with
SO(2) action, Jp is equivalent to R
2
; SO(2) acts on Jp with a fixed point at the origin
that corresponds to the endpoint of the half-line. On the other hand, in the case of JO, the
relevant curve is a copy of R, with its ends at infinity. Rotating it by SO(2), we find that
as a manifold with SO(2) action, JO is equivalent to R × S
1 with a free action of SO(2) on
the second factor.
It is convenient to express (3.61) in a dual language. Given a general cycle C = npJp +
nOJO, to compensate for the jumping (3.61) and ensure that C varies smoothly, the coefficients jump by
np → np
nO → −np + nO. (3.62)
Finally, let us return to the Stokes lines of fig. 5. We write l+ and l− for the two Stokes
lines given by ǫ = r exp(±iπ/2) with real r. Scaling to λ = 1, the Morse function Re (if)
vanishes at p and equals ±r
2/2 on l±. So on l+, there can be a downward flow from O to
p, and on l− there can be a downward flow from p to O. Flows of each type actually exist,
as the reader can verify by slightly extending the analysis of fig. 6. (JO always corresponds
to the line u = v, and Jp to part of a hyperboloid through u + iv = −ǫ.) In general, the
jumping in eqn. (3.61) occurs in crossing l−, but there is no such jumping in crossing l+.
The algebraic invariant that “counts” the downward flows from O to p along l+ vanishes
(even though such flows exist), for a reason explained in section 3.3.4.
53

3.4.3 One More Case
The last singularity that we will encounter is more surprising. We will describe it first in a
language with SO(1, 1) rather than SO(2) symmetry. We consider SO(1, 1) acting on real
variables u, v by u → ru, v → r
−1
v, with r real. The basic invariant is uv. We consider an
integral Rdu dv exp(iλf(uv)) where f is a function of uv. The obvious case is that f is a
quadratic function. However, and surprisingly, in the world of knots in S
3
, there can be a
natural reason for f to be an odd function of uv.
Under these conditions, the basic example of a function exhibiting critical behavior is
f(u, v) = (uv)
3
/3 − ǫ(uv). (3.63)
Apart from the critical point p at u = v = 0, there are two critical orbits O± at uv = ±ǫ
1/2
.
For real ǫ, these critical orbits are real or imaginary depending on the sign of ǫ. (As real
orbits, these orbits are hyperboloids with two topological components.)
A closely related problem is the case of SO(2) action on the xy plane with f(x, y) =
(x
2+y2
)
3/3−ǫ(x2 +y2
). The relation becomes apparent upon complexification; one problem
can be mapped into the other by taking u = x + iy, v = x − iy. The problem of SO(1, 1)
acting on the real uv plane and the problem of SO(2) acting on the real xy plane correspond
to two real slices of the same situation with complex variables. One real slice is defined
by u = u, v = v and the other by u = v. To study analytic continuation, as usual we
must complexify the variables u and v, and then the SO(1, 1) and SO(2) problems become
equivalent. It is convenient to work with x and y. (We introduced u and v because the real
slice with SO(1, 1) symmetry will appear naturally in our application.)
First, we will determine the λ dependence of I(λ, ǫ) = Rdx dy exp(iλf(x, y)) using
scaling symmetry. An obvious scaling of x and y shows that
I(λ, ǫ) = λ
−1/3
I(1, λ2/3ǫ) = λ
−1/3
Z
dx dy exp(i((x
2 + y2
)
3
/3 − λ
2/3
ǫ(x
2 + y2
)). (3.64)
A special case is that I(λ, 0) ∼ λ
−1/3
. On the other hand, for ǫ 6= 0, and choosing ǫ < 0 so
that the only real critical point is the one at x = y = 0, a similar scaling gives I(λ, ǫ) ∼ λ
−1
.
So
I(λ, 0)
I(λ, ǫ)|ǫ<0
∼ λ
2/3
, λ → ∞. (3.65)
By introducing polar coordinates in the xy plane, one can express I(λ, ǫ) as a multiple of
the Airy function. The main difference is that there is an extra possible integration cycle for
I(λ, ǫ), as we now explain.
To study the analytic continuation systematically, we consider the integration cycles
associated to critical orbits. Let J0, J+, and J− be the Lefschetz thimbles associated,
54

respectively, to the critical point at x = y = 0 and to the critical orbits x
2 + y2 = ±ǫ1/2
.
The same reasoning as in section 3.4.2 can be used to describe them by applying an SO(2)
rotation to suitable curves in the complex x
2
-plane. In fact, apart from a substitution x → x
2
,
the polynomial f(x, 0) = (x
2
)
3/3 − ǫx2
is familiar from our study of the Airy function.
Accordingly, the Lefschetz thimbles J± obtained by flowing from the critical orbits O±, can
be derived from the curves that were depicted in fig. 4, but now in the x
2 plane. On the
other hand, the third Lefschetz thimble J0 is associated to a similar curve connecting the
point x
2 = 0 to infinity. By an analysis similar to that of section 3.4.2, one can determine
the jumping that occurs between ǫ > 0 and ǫ < 0. The change in J± is precisely the same
as it is for the Airy function; what is new is that J0 picks up a linear combination of J±.
We leave the details to the reader.
