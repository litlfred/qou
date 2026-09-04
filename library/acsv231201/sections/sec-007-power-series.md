---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-007-power-series
section_title: "Power series"
section_number: null
pages: 35-38
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
Generating functions impose an algebraic structure on arrays of complex num-
bers, analogous to (and thus most easily expressed using the same notation
as) convergent power series. To that end, let z = (z1,..., zd) be a vector of
indeterminates and consider the set of formal expressions
C[[z]] =C[[z1,..., zd]] :=

∑
r∈Nd
arzr : ar∈C for allr∈Nd
 .
If F(z) = ∑
r frzr ∈ C[z] then f is called a formal power series , the co-
eﬃcient of zr in F is [zr]F(z) : = fr, and we also single out the constant
coeﬃcient F(0) := [z0]F(z) = f0. The setC[[z]] becomes the ring of formal
power series by deﬁning addition term-wise
[zr]
(
F(z) + G(z)
)
:= [zr]F(z) + [zr]G(z)
and multiplication by convolution
[zr]F(z)G(z) :=
∑
s∈Nd
[zs]F(z)· [zr−s]G(z),
17
18 Generating functions
where [zr−s]G(z) is deﬁned to be zero if r−s has a negative coordinate (so
the sum in the convolution is always ﬁnite). The generating function of the
array{ar :r∈Nd} is the formal power series ∑
r∈Nd arzr∈C[[z]].
The additive identity in C[[z]] is the series 0 (where every coe ﬃcient is
zero) and the multiplicative identity is the series 1 (which has a coe ﬃcient of
zero for every index vectorr, 0).
Exercise 2.1. Prove that F(z)∈C[[z]] has a multiplicative inverse if and only
if F(0), 0.
Exercise 2.1 implies C[[z]] is a local ring , meaning that it has a unique
maximal ideal m that, in this case, consists of all non-units. Local rings come
equipped with a notion of convergence: a sequence of elementsFn(z)∈C[[z]]
converges to F(z) ∈ C[[z]] if and only if for every k ∈ N the di ﬀerence
Fn(z)− F(z) lies in mk for all suﬃciently large n. An easier way to say this
is that Fn(z)→ F(z) if and only if for any r∈ Nd there exists Nr∈ N such
that [zr]Fn(z) = [zr]F(z) for all n≥ Nr. In other words, each coe ﬃcient
eventually stabilizes.
For 1≤ k≤ d we write∂k for the formal partial derivative operator which
takes f (z) = ∑
r∈Nd arzr and returns
(∂k f )(z) = ∂
∂zk
f (z) :=
∑
r∈Nd
rkarzr−δk.
Powers∂r
k of ∂k denote repeated diﬀerentiation, with (∂0
k f )(z) = f (z), and a
monomial∂r = ∂r1
1··· ∂rd
d represents repeated di ﬀerentiation with respect to
each variable. We also use the shorthand fzr(z) and f (r)(z) for (∂r f )(z) =
(∂|r| f/∂r1
z1··· ∂rd
zd)(z).
Although formal power series are simply algebraic objects, we often con-
sider them as representing convergent series expansions, and thus analytic
functions, in certain subsets of Cd. The (open) polydisk centered at p∈ Cd
with polyradiusb∈Rd
>0 is the set
Db(p) :={z∈Cd :|z j− p j|< b j for 1≤ j≤ d},
and a neighborhood of a pointp∈Cd is any polydisk containingp. The torus
centered atp∈Cd with polyradiusr∈Rd
>0 is the set
Tp(r) :={z∈Cd :|z j− p j| = r j for 1≤ j≤ d}.
To ease notation we writeT(r) for a torus centered at the originp = 0, and for
everyw∈ Cd
∗ (hereC∗ = C\{ 0} is the set of non-zero complex numbers) we
deﬁne
T(w) = T(|w1|,..., |wd|) ={z∈Cd :|z j| =|w j| for 1≤ j≤ d}.
2.1 Power series 19
LetN be a neighborhood of the origin and suppose that F, G ∈ C[[z]] are
the generating functions of the sequences { fr} and{gr}. If ∑
r∈Nd| frwr| and∑
r∈Nd|grwr| are ﬁnite for allw∈N then F and G are absolutely convergent
series onN, meaning they represent analytic functions, and taking the sum
F(z) + G(z) or product F(z)G(z) as formal series or analytic functions gives
the same result. If f represents an analytic function on a neighborhood of Cd
then every partial derivative of f does as well.
Since a ﬁnite intersection of neighborhoods of the origin is a neighborhood
of the origin, the collection of series that converge in some neighborhood of the
origin is a proper subring C{z} ofC[[z]], called the ring of germs of analytic
functions. The interior D ⊂Cd of the domain on which the formal power
series F converges is the union of open polydisks, and is hence characterized
by its intersectionDR withRd. The domainD is in fact log-convex, meaning
that the set{x∈Rd : (ex1,..., exd)∈D R} is convex; see Chapter 6 for further
details and generalizations.
Because there are formal power series that fail to converge in any open poly-
disk centered at the origin, to which we cannot apply analytic methods, it can
be convenient to work with a rescaled series ∑
r∈Nd
ar
g(r)zr for a judiciously
chosen function g. In combinatorial contexts, it is often useful to let g(r) be
a product of factorials ri!, and a generating function normalized in this way
is called an exponential generating function. In addition to facilitating conver-
gence of power series, exponential generating functions also have important
combinatorial interpretations (see Section 2.5 below).
Remark. In examples we often write ( x, y, z) for ( z1, z2, z3), and ( r, s, t) for
(r1, r2, r3), to remove the need for subscripts.
Exercise 2.2. Which of the following formal power series lie inC{x}?
(a)
∞∑
n=0
n!xn
(b)
∞∑
n=0
n2xn
(c)
∞∑
n=1
xn
n
20 Generating functions
