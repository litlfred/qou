---
doc_id: akemann-2022-j-phys-a-math-theor-55-194002
doc_title: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk"
section_id: sec-003-3-gap-probabilities-and-level-spacing-distributi
section_title: "Gap probabilities and level spacing distributions"
section_number: 3
pages: 11-14
source_pdf: Akemann_2022_J._Phys._A__Math._Theor._55_194002.pdf
source_sha256: 3753499c4b23f189
toc_source: outline
doc_brief: "Consecutive level spacings in the chiral Gaussian unitary ensemble: from the hard and soft edge to the bulk — 20 sections: Front matter; Consecutive level spacings in the ; Introduction"
---
Let us underscore that most of the ensuing discussion in the present section holds for arbitrary
positive real spectra with a finite number of eigenvalues. Thus our particular choice of an
ensemble can be readily generalised.
We start from a generic joint probability density Pn({x}) of the set of n unordered eigenval-
ues {x} = {xi}n
i=1, with xi ∈R+ for all i = 1, . . ., n. The emphasis on ‘unordered’ is impor-
tant, as some combinatorial constants depend on whether the eigenvalues have been ordered or
not. In our case, the normalised joint probability density of the χGUE [16, 41] with Nf inserted
characteristic polynomials is given by
P(Nf)
ν,n ({x}) =
1
Z(Nf)
ν,n ({m})
Δn

{x2}
2
n

j=1
⎛
⎝x2ν+1
j
e−x2
j
Nf

f=1
(x2
j + m2
f)
⎞
⎠,
(33)
with the Vandermonde determinant defined as Δn({x}) = 
1⩽a<b⩽n(xb −xa). This density
depends on several external parameters: Nf masses {m} = {m f}Nf
f=1, the quark masses in appli-
cations to QCD, and the topological charge ν ∈N counting the number of zero eigenvalues of
the Dirac operator (rectangularity of the n × (n + ν) random matrix). For more details in this
relation to QCD we refer to [18]. The normalisation constant (partition function) is denoted by
ZNf
ν,n({m}) =

[0,∞)ndx1 . . . dxnΔn

{x2}
2
n

j=1
⎛
⎝x2ν+1
j
e−x2
j
Nf

f=1
(x2
j + m2
f)
⎞
⎠.
(34)
As already mentioned, one common technique to compute the level spacing distribution is via
gap probabilities using Fredholm determinants, see [8]. These yield the probability that a cer-
tain interval is void of eigenvalues. As we aim for the level spacing distribution between a
specific pair of consecutive eigenvalues, we define the kth gap probability as follows. It imple-
ments the condition that k eigenvalues lie below the gap, and the remaining n −k eigenvalues
10
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
are above the gap. When the gap is the interval [a, b] ∈R+, this conditional gap probability is
defined by the n-fold integral
Ek([a, b]) =
n!
k!(n −k)!

[0,a]kdx1 . . . dxk

[b,∞)n−kdxk+1 . . . dxnPn({x}).
(35)
The combinatorial pre-factor takes care of the fact that the eigenvalues are unordered and
ensures the proper normalisation. For k = 0, only the second set of integrals is present, that
is all eigenvalues are larger than or equal to b. The gap probability can be also expressed
in terms of the kernel of the corresponding orthogonal polynomials, that is the generalised
Laguerre polynomials for the χGUE at Nf = 0, see section 4. However, we will directly
compute the spacing distribution in a different way to be introduced now, circumventing the
problem to determine the orthogonal polynomials when introducing Nf flavours in the weight
function.
When taking the mixed second derivative of equation (35) in a and b for k ⩾1, we obtain
the joint density that the kth eigenvalue sits at the position a and the (k + 1)st eigenvalue at
the position b. Defining the spacing s = b −a, and integrating over their starting point a = xk,
yields the level spacing distribution between the kth and (k + 1)st eigenvalue,
pk,n(s) =
n!
(k −1)!(n −k −1)!
 ∞
0
dxk

[0,xk]k−1dx1 . . . dxk−1
×

[xk+s,∞)n−k−1dxk+2 . . . dxnPn(x1, . . . , xk, xk + s, xk+2, . . . , xn).
(36)
Here, we explicitly spell out the arguments of the joint density Pn({x}). When k = 1 the set
of integrals over [0, xk] is absent. It can be shown that the spacing distribution is properly
normalised for all k,
! ∞
0 ds pk,n(s) = 1, cf [43, appendix A].
Our aim is to study the spacing for the smallest eigenvalues. Therefore, we fix the small-
est k + 1 in the large n-limit. This means that the integral over the remaining n −k −1
eigenvalues can be understood as being proportional to a partition function of n −k −1
eigenvalues, depending on an extended number of shifted masses. Indeed, a standard trick
[22] is to define new variables y j =
"
x2
k+1+ j −(xk + s)2 for j = 1, . . . , n −k −1. These can
be interpreted as eigenvalues of a positive definite Hermitian random matrix of dimension
(n −k −1) × (n −k −1 + 2). The expression for the level spacing distribution in terms of
the shifted variables only changes marginally
pk,n(s) =
n!
(k −1)!(n −k −1)!
 ∞
0
dxk

[0,xk]k−1dx1 . . . dxk−1
×

[0,∞)n−k−1
n−k−1

j=1
dy jy j
"
y2
j + (xk + s)2
× Pn
	
x1, . . . , xk, xk + s,
"
y2
1 + (xk + s)2, . . . ,
"
y2
n−k−1 + (xk + s)2

.
(37)
Once again we have explicitly spelled out the arguments of the joint probability density.
At first glance, the expression (37) looks more cumbersome than the one we started from.
Yet, for the joint probability density (33) of the χGUE with Nf flavours this is a considerable
11
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
simplification, because it relates two joint probability densities of the same random matrix
ensemble, but for different matrix sizes and different numbers of masses. In particular, using
that the Vandermonde determinant is invariant under translation of its variables, and the fact
that it can be split in terms of two sets of variables as follows,
Δn(x1, . . . , xk+1, z1, . . . , zn−k−1) = Δk+1(x1, . . . , xk+1)Δn−k−1(z1, . . . , zn−k−1)
×
k+1

i=1
n−k−1

j=1
(z j −xi),
(38)
it holds that
P(Nf)
ν,n
	
x1, . . . , xk, xk + s,
"
y2
1 + (xk + s)2, . . . ,
"
y2
n−k−1 + (xk + s)2

×
n−k−1

j=1
y j
"
y2
j + (xk + s)2
= Z( 
Nf)
2,n−k−1({#m})
Z(Nf)
ν,n ({m})
Δk+1

x2
1, . . . , x2
k, (xk + s)22(xk + s)2ν+1e−(n−k)(xk+s)2
×
⎛
⎝
Nf

f=1
((xk + s)2 + m2
f)
⎞
⎠
k
j=1
⎛
⎝x2ν+1
j
e−x2
j
Nf

f=1
(x2
j + m2
f)
⎞
⎠P( 
Nf)
2,n−k−1

{y}

.
(39)
Here, we have defined an extended number of flavours
$
Nf = Nf + ν + 2k.
(40)
The enlarged set of $
Nf (shifted) mass parameters is reading
{#m} =
%
xk + s, . . . , xk + s,
"
m2
1 + (xk + s)2, . . . ,
"
m2
Nf + (xk + s)2,
×
"
(xk + s)2 −x2
1,
"
(xk + s)2 −x2
1, . . . ,
"
(xk + s)2 −x2
k,
"
(xk + s)2 −x2
k
&
.
(41)
The set of new masses (xk + s) is ν-fold degenerate, whereas the masses
"
(xk + s)2 −x2
j
are two-fold degenerate for j = 1, . . . , k. Obviously the last two masses can be simplified to
√s(2xk + s). Notice that the shift has promotedthe ν zero-eigenvaluesin (33) to becomedegen-
erate mass-terms, whereas the squared Vandermonde determinant has created a fixed number
of zero-eigenvalues ν = 2 in the new variables y1, . . . , yn−k−1.
This relation has been exploited several times in the literature [20–22]. In our case, it creates
a short-cut as the pre-factor in front of the joint probability density P( 
Nf)
2,n−k−1

{y}

, the ratio
of two partition functions, is y-independent. Hence, the integral of P( 
Nf)
2,n−k−1

{y}

over all its
eigenvalues y1, . . . , yn−k−1 yields unity, so that we end up with a k-fold integral for the level
spacing distribution of the χGUE with Nf flavours
12
J. Phys. A: Math. Theor. 55 (2022) 194002
G Akemann et al
p(ν,Nf)
k,n
(s) =
n!
(k −1)!(n −k −1)!
 ∞
0
dxk

[0,xk]k−1dx1 . . . dxk−1
× Z( 
Nf)
2,n−k−1({#m})
Z(Nf)
ν,n ({m})
Δk

x2
1, . . . , x2
k
2(xk + s)2ν+1
× e−(n−k)(xk+s)2
Nf

f=1
((xk + s)2 + m2
f)
×
k
j=1
⎛
⎝[(xk + s)2 −x2
j]2x2ν+1
j
e−x2
j
Nf

f=1
(x2
j + m2
f)
⎞
⎠.
(42)
Notice that the last line is proportional to s2, due to the term with j = k. Certainly, part of the
difficulty has been moved into the evaluation of the new partition function Z( 
Nf)
2,n−k−1({#m}). Yet,
its explicit form is known in principle and will be spelled out in the following section.
One last remark is in order which applies to arbitrary ensembles. The level spacing
distribution (37) still has to be unfolded, meaning its first moment
¯sk,n =
 ∞
0
ds spk,n(s),
(43)
does not necessarily equal to 1 yet. This is especially the case for the result (42). Under the
assumption that the macroscopic or mesoscopic level density is already in a constant form (the
microscopic level density asymptotes to a constant when taking the limit into the bulk), we
only need to rescale the spacing distribution to make it comparable with standard distributions
such as the Wigner surmise (1), where the first moment is unity. This means, one needs to
consider the rescaled spacing distribution
¯pk,n(s) = ¯sk,npk,n

¯sk,ns

.
(44)
Note that when we rescale the spacing between two eigenvalueswe also have to rescale all other
eigenvalues, as well as the masses m j with the same scaling factor. For practical purposes one
can also compute the mean spacing ¯sk,n through the difference of the mean positions of the kth
and (k + 1)st smallest eigenvalue.
