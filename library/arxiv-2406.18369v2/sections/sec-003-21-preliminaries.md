---
doc_id: arxiv-2406.18369v2
doc_title: "112 years of listening to Riemannian manifolds"
section_id: sec-003-21-preliminaries
section_title: "Preliminaries"
section_number: 2.1
pages: 4-12
source_pdf: 2406.18369v2.pdf
source_sha256: 20b3f8dbc40eacc3
toc_source: outline
doc_brief: "112 years of listening to Riemannian manifolds — In1910, HendrikAntoonLorentzdelvedintotheenigmaticLaplace eigenvalue equation, also known as the Helmholtz equation, pondering to what extent the"
---
mulated by Lorentz, we establish key notations and preliminaries. A domain
Ω⊂ Rn is a connected open subset of Rn. We always assume that Ω is com-
pact. The boundary of Ω is denoted by∂Ω. For a domain Ω⊂ Rn, we let|Ω|
denote then-dimensional volume ofΩ and|∂Ω| the (n− 1)-dimensional volume of
the boundary ofΩ. In particular, ifn = 2 then|Ω| and|∂Ω| denote the area and
the perimeter ofΩ, respectively.
The Laplace operatoron Rn is given by (2). For a functionf : Ω→ C, we write
f∈ C∞(Ω) if f is infinitely differentiable, that is, iff is N times differentiable for
everyN∈ N. Moreover, we writef∈ C∞
c (Ω) if f∈ C∞(Ω) and the support off
is compactly contained inΩ.
A functionf∈ C∞(Ω) is said to satisfyDirichlet boundary conditionsif f = 0
on ∂Ω. Similarly,f satisfies Neumann boundary conditionsif
∂f
∂n = 0 on ∂Ω,
where ∂f
∂n is the normal derivative off pointing outwards fromΩ. Iff is not iden-
tically zero, satisfies Dirichlet boundary conditions, and (1) holds for someλ∈ C,
then λ is an eigenvalue with corresponding eigenfunction f. The Dirichlet/Neu-
mann spectrumof Ω is the set of all eigenvalues with eigenfunctions satisfying the
Dirichlet/Neumann boundary condition, respectively.
For one dimensional domains, it is perfectly sufficient to solve the Helmholz
equation by searching for smooth functions that satisfy either the Dirichlet or Neu-
mann boundary conditions. However, for domains in higher dimensions, especially
in cases when the boundary of the domain is not smooth, to rigorously define the
Laplace operator, one must specify the Hilbert space of functions on which the
operator acts and is essentially self-adjoint. For this reason and to be inclusive of
all readers we recall
Definition 2.1. For a domain Ω⊂ Rn, L2(Ω) is defined as the set of equiva-
lence classes consisting of Lebesgue measurable functionsf : Ω→ C such that the
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 5
Lebesgue integral
R
Ω|f(x)|2dx< ∞, where two functionsf,g are equivalent if
{x∈ Ω :f(x)̸=g(x)}
has Lebesgue measure 0. We write f ∈ L2(Ω) to indicate that there exists an
equivalence class inL2(Ω) containing f. If f ∈ L2(Ω) and in addition the weak
partial derivatives off of order up to k exist and are in L2(Ω), then we write
f∈Hk(Ω). For further details of these Hilbert spaces we refer to [48, p. 51]. The
space H1
0(Ω) is the completion ofC∞
c (Ω) with respect to the norm of the Hilbert
space H1(Ω) (which properly containsC∞
c (Ω)).
Now let (M,g ) be a compact Riemannian manifold, possibly with boundary.
The Laplace operator is defined in (4). If ∂M = ∅ then the operator acts on
H2(M), or if∂M̸=∅ and the Laplace operator acts onH2(M) we refer to this as
the Neumann Laplace operator. The Dirichlet Laplace operator acts onH1
0(M)∩
H2(M). These definitions are completely analogous for (bounded) domains inRn.
In all of the aforementioned cases, the eigenvalues are discrete and non-negative,
forming a countable set in[0,∞). We letN(λ) denote the number of eigenvalues
less than or equal toλ,
(5) N(λ) = #{n∈ N :λn≤λ}.
Here we count multiplicity, so that an eigenvalue with, say,m linearly independent
eigenfunctions is countedm times.
To state Weyl’s law, we recall the notion of asymptotic equivalence of functions.
Two functionsf,g : R→ C are asymptotically equalas x→∞ if
lim
x→∞
f(x)
g(x) = 1.
We write this asf(x)∼ g(x), x→∞ . Functions being asymptotically equal as
x→ 0 are defined analogously.
2.2. Weyl’s law. Here we show how Weyl proved what is now known asWeyl’s
law. In two dimensions, Weyl’s law says that
(6) lim
λ→∞
N(λ)
λ =|Ω|
4π.
One key idea needed to prove (6) is to coverΩ by rectangles and consider the
eigenvalues on those. This is useful because on rectangles the eigenvalues and
eigenfunctions can be computed analytically. Indeed, suppose
Ω = (0 ,l 1)× (0,l 2) for some l1,l 2 > 0 as shown in Figure 1. Consider the
eigenvalue problem with Dirichlet boundary conditions:
(7)
(
∆U(x,y ) =λU(x,y ) in (0,l 1)× (0,l 2),
U(x,y ) = 0 on ∂Ω.
We solve this by separating variables. In other words, we look for solutions of the
form X(x)Y (y). Inserting this into (7) gives
X′′(x)Y (y) +X(x)Y′′(y) +λX(x)Y (y) = 0
or
X′′(x)
X(x) =−Y′′(y)
Y (y) −λ.
6 G. MÅRDBY AND J. ROWLETT
(l1, 0)
(0,l 2)
(l1,l 2)
Ω
Figure 1. This domain Ω is a rectangle with side lengthsl1 and
l2.
The left side depends only onx whereas the right side depends only ony therefore
both sides are constant. They are essentially the same equation, which is a regular
Sturm-Liouville problem, thanks to the boundary condition. ForX this can be
written, for some constantµ, as
X′′(x) =µX(x), X (0) = 0, X (ℓ1) = 0.
If µ = 0, then the equation becomesX′′(x) = 0, whose general solution isX(x) =
Ax +B. The boundary conditions immediately give thatA =B = 0, soX(x) = 0
is the only solution in this case. Ifµ̸= 0, then all solutions are linear combinations
of ex±√µ. It is straightforward to show that the only non-zero linear combination
that satisfies the boundary condition is a scalar multiple ofsin(mπx/ℓ1) with cor-
responding µm =−m2π2/ℓ2
1 for n∈ Z\{ 0}. Since sin(−x) and sin(x) are linearly
dependent, we simply setXm(x) = sin( mπx/ℓ1) for m∈ N. Proceeding analo-
gously we findYn(y) = sin(nπx/ℓ2) for n∈ N. The eigenvalues and corresponding
eigenfunctions for the rectangle are then respectively
λm,n = m2π2
ℓ2
1
+ n2π2
ℓ2
2
, sin
mπx
ℓ1

sin
nπy
ℓ2

, m,n ∈ N.(8)
By [76, p. 83] these eigenfunctions constitute an orthogonal basis ofL2((0,l 1)×
(0,l 2)), and therefore we have found all eigenfunctions (uniquely up to multiplica-
tion by non-zero scalars) and therewith all eigenvalues.
Now assume that (7) has the Neumann boundary conditions. Then we solve the
equation in the same way and obtain eigenvalues and corresponding eigenfunctions
λm,n = m2π2
ℓ2
1
+ n2π2
ℓ2
2
, cos
mπx
ℓ1

cos
nπy
ℓ2

, m,n ∈ Z≥0.(9)
Similarly, inthiscasetheseeigenfunctionsconstituteanorthogonalbasisof L2((0,l 1)×
(0,l 2)), and therefore we have found all eigenfunctions (uniquely up to multiplica-
tion by non-zero scalars) and therewith all eigenvalues. Knowing the eigenvalues
and eigenfunctions on rectangles, we can prove that Weyl’s law holds on them for
both the Dirichlet and Neumann boundary conditions.
Proposition 2.2. Let I = (a1,b 1)× (a2,b 2)⊂ R2 be a rectangle. Then both the
Dirichlet and Neumann eigenvalues onI satisfy
lim
λ→∞
N(λ)
λ =|I|
4π.
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 7
l1R
π
l2R
π
Figure 2. A quarter ellipse whose radii are proportional toR.
Each lattice point in its interior corresponds to a unit square. The
total area of the squares and the area of the quarter ellipse both
grow on the orderR2 asR→∞ , while the error is of the orderR.
Hence the number of lattice points in the interior of the quarter
ellipse is asymptotically equal to its area asR→∞ .
Proof. By possibly translating I, we may assume that ai = 0 and bi = li, for
i = 1, 2. The Dirichlet eigenvalues are given in (8) while the Neumann eigenvalues
are given in (9). For anyR >0, note thatN(R2) is the number of lattice points
p = (m,n ) such that (mπ/l1)2 + (nπ/l2)2≤ R2. This is asymptotically equal to
the area of the quarter ellipse
ER :=

(x,y ) : x2π2
l2
1
+ y2π2
l2
2
≤R2, x,y≥ 0

,
namely|ER| =l1l2R2/4π.
To see this, note that each lattice point(m,n ) corresponds to a square of length
1 as shown in Figure 2. Since two such squares have disjoint interiors, and each
square has volume 1, N(R2) equals the number of squares which fit inside the
quarter ellipse. This deviates from its area by less than the length of its arc, which
is of the orderR asR→∞ . Similarly, number of the lattice points on the boundary
of the ellipse is of the orderR as R→∞ . It therefore follows that the error terms
which are of orderR can be gleefully discarded, and we have
lim
R→∞
N(R2)
|ER| = 1,
Thus, we get
N(R2)∼ l1l2R2
4π ⇐⇒ N(λ)∼ l1l2λ
4π , λ→∞.
Noting that|I| =l1l2 completes the proof. □
What we have done so far with Weyl’s law can easily be generalized to n-
dimensional Euclidean space. Indeed, ifΩ =Qn
i=1(0,li)⊂ Rn is ann-dimensional
8 G. MÅRDBY AND J. ROWLETT
rectangle, then for Dirichlet boundary conditions the eigenvalues become
nX
i=1
m2
iπ2
l2
i
with corresponding eigenfunctions
nY
i=1
sin(miπxi
li
), mi≥ 1, xi∈ (0,li).
Similarly, for Neumann boundary conditions we get the same eigenvalues except
that we now havemi≥ 0 instead. The eigenfunctions become
nY
i=1
cos(miπxi
li
), mi≥ 0, xi∈ (0,li).
Thisisprovenbyseparatingvariablesinthe n-dimensionaleigenvalueproblemanal-
ogous to the two-dimensional case. From this, we can analogously deduce Weyl’s
law from the proof of Proposition 2.2. We see thatN(R2) becomes asymptotically
equal to the volume of(
(x1,...,x n) :
nX
i=1
x2
iπ2
l2
i
≤R2, xi≥ 0
)
.
This is, by a standard calculation,
ωnRn
(2π)n
nY
i=1
li,
where ωn denotes the volume of then-dimensional unit ball. Thus,
N(λ)∼ ωn|I|
(2π)nλn/2, λ→∞,
which shows that
lim
λ→∞
N(λ)
λn/2 = ωn|I|
(2π)n.
Our next goal is to show that Weyl’s law holds for arbitrary bounded, connected
domains in Rn. To do this, we need the variational principles, also known as
Rayleigh-Ritz principles, which were developed around the same time as Lorentz’s
lectures in 1910 [80], [102], [100].
Theorem 2.3. Let Ω be a domain with piecewise smooth boundary. Ifλk denotes
thekth eigenvalue of the Laplace operator with corresponding eigenfunctionfk, then
λk =



inff∈H
f̸=0
R
Ω|∇f|2
R
Ω|f|2 and is attained byf1, if k = 1,
inff∈H
f̸=0
n R
Ω|∇f|2
R
Ω|f|2 :⟨f,fj⟩L2(Ω) = 0, j = 1,...,k − 1
o
and is attained byfk, if k≥ 2,
(10)
λk = sup
L⊂H
dim L=k−1
inf
f∈L⊥
f̸=0
R
Ω|∇f|2
R
Ω|f|2 ,(11)
λk = inf
L⊂H
dim L=k
sup
f∈L
f̸=0
R
Ω|∇f|2
R
Ω|f|2 ,(12)
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 9
Figure 3. The domainΩ has an inner and outer covering consist-
ing of finitely many rectangles. The rectangles contained in the
interior are marked with a cross.
where the integrals are taken with the respect to the Lebesgue measure. Here,H =
H1
0(Ω) for Dirichlet boundary conditions, andH =H1(Ω) for Neumann boundary
conditions.
Remark 2.4. The expression R
Ω|∇f|2
R
Ω|f|2
may be called theRayleigh quotient, Ritz quotient,or Rayleigh-Ritz quotientof f.
As mentioned earlier, Weyl developed his law as part of his broader research
in mathematical physics and differential geometry, particularly in the context of
elliptic partial differential equations and the spectrum of differential operators.
While it is difficult to pinpoint exactly how he discovered or learned about the
variational principles, we expect that he was familiar with Rayleigh’s works on the
principles of sound [102] and may also have accessed Ritz’s methods published in
1909 [100].
We can now show that Weyl’s law holds for an arbitrary domainΩ by approxi-
mating it with rectangles and using the Dirichlet and Neumann eigenvalues on the
approximating rectangles together with the variational principles, following Weyl’s
original proof [118]. This is known as Dirichlet-Neumann bracketing. We will show
the proof in detail for planar domains, and afterwards we will explain briefly how
to obtain the analogous result for domains inRn.
Theorem 2.5 (Weyl’s law). Let Ω⊂ R2 be a bounded domain and let0 < λ1≤
λ2≤... be the Dirichlet eigenvalues of the Laplace operator onΩ. If the boundary
∂Ω is piecewise smooth, then
lim
λ→∞
N(λ)
λ =|Ω|
4π.
10 G. MÅRDBY AND J. ROWLETT
Proof. Let ϵ > 0. We choose an inner covering ΩI = SN
i=1 ΩI,i and an outer
covering ΩO =SM
j=1 ΩO,j each consisting of finitely many disjoint rectangles; they
may only overlap on their boundaries. We choose these coverings such that the
area of the region between the outer and inner coverings has area less thanϵ, that
is|Ω0\Ω1|<ϵ . This is shown in Figure 3.
Let λk(Ω·) and µk(Ω·) denote thekth Dirichlet and Neumann eigenvalues, re-
spectively, onΩ·. We take the unions
[
i,k
{λk(ΩI,i)},
[
j,k
{λk(ΩO,j)},
[
i,k
{µk(ΩI,i)},
[
j,k
{λk(ΩO,j)}
of the respective eigenvalues over the rectangles and reorder them into increasing
sequences. Denote the results by{˜λk(ΩI)},{˜λk(ΩO)},{˜µk(ΩI)}, and{˜µk(ΩO)},
respectively. We now require the following lemma.
Lemma 2.6. With the notations above, we have for everyk
˜µk(ΩO)
(1)
≤ µk(ΩO)
(2)
≤ λk(ΩO)
(3)
≤ λk(Ω)
(4)
≤ λk(ΩI)
(5)
≤ ˜λk(ΩI).
Proof of lemma 2.6.There are five inequalities to prove, (1) through (5). We start
with (3). Since Ω⊂ ΩO, we can extend functionsf∈H1
0(Ω) to equal 0 onΩO\Ω.
Then we havef∈H1
0(ΩO), and soH1
0(Ω)⊂H1
0(ΩO). Now (3) follows immediately
from the variational principle (12) because taking the infimum over a larger set
yields a smaller result. Inequality (4) follows in the same way sinceΩI⊂ Ω. In
fact, the same argument works for (5) because for each rectangle we can extend its
H1
0 functions to be zero outside it, and then it will be included inΩI. Similarly, (2)
follows from the fact that for Neumann boundary conditions (12) minimizes over
H1, which is larger than what we minimize over for Dirichlet boundary conditions,
namely H1
0.
Thus, it remains to show (1). Recall that for Neumann boundary conditions on a
rectangle, 0 is an eigenvalue with corresponding eigenfunctions being non-zero con-
stant functions. Thus, if we letR1,...,R M denote the rectangles ofΩO, then each
Ri has 0 as an eigenvalue. This means that˜µ1(ΩO) =··· = ˜µM(ΩO) = 0. Since
µi(ΩO)≥ 0 for everyi, it follows that˜µi(ΩO)≤µi(ΩO) fori = 1,...,M . The next
eigenvalue, ˜µM+1(ΩO), will then be the smallest positive eigenvalue coming from
all the rectanglesR1,...,R M. After re-labeling, we may assume that˜µM+1(ΩO)
comes from rectangleR1.
The next step is to use the variational principle (11). We have
(13) µM+1(ΩO) = sup
L⊂H1(ΩO)
dim L=M
inf
f∈L⊥
f̸=0
R
ΩO
|∇f|2
R
ΩO
|f|2 .
Now let˜L be theM-dimensional subspace ofH1(ΩO) spanned by the characteristic
functions on the rectangles, so that a basis of˜L is given by{f1,...,f M} where
fi(x) =
(
1, x∈Ri,
0, x /∈Ri.
To show that˜µM+1(ΩO)≤µM+1(ΩO), by (13) it’s enough to show that
˜µM+1(ΩO)≤ inf
f∈˜L⊥
f̸=0
R
ΩO
|∇f|2
R
ΩO
|f|2 .
112 YEARS OF LISTENING TO RIEMANNIAN MANIFOLDS 11
Note that the eigenfunctionu corresponding to ˜µM+1(ΩO) is in ˜L⊥. Indeed, this
is immediate forR2,...,R M since we extendu to be 0 on those. ForR1, recall
the variational principle (10) which says thatu is orthogonal to the eigenfunctions
corresponding to ˜µ1,..., ˜µM. These eigenfunctions are constant functions, so we
obtain
R
R1
u = 0 and thereforeu is also orthogonal to the characteristic functions
on R1, henceu∈ ˜L⊥.
In fact, for anyf∈ ˜L⊥ we have
R
Ri
f = 0 for everyi by definition of˜L. In partic-
ular, f is orthogonal to the eigenfunctions corresponding to˜µ1(ΩO),..., ˜µM(ΩO).
This gives, by (10), that for everyi
˜µ(i)≤
R
Ri
|∇f|2
R
Ri
|f|2 ,
where ˜µ(i) is the first positive Neumann eigenvalue onRi. ThenZ
Ri
|∇f|2≥ ˜µ(i)
Z
Ri
|f|2≥ ˜µM+1(ΩO)
Z
Ri
|f|2,
and soR
ΩO
|∇f|2
R
ΩO
|f|2 =
PM
i=1
R
Ri
|∇f|2
PM
i=1
R
Ri
|f|2
≥
˜µM+1(ΩO)PM
i=1
R
Ri
|f|2
PM
i=1
R
Ri
|f|2
= ˜µM+1(ΩO).
Since this holds for allf∈ ˜L⊥, it also holds for the infimum:
˜µM+1(ΩO)≤ inf
f∈˜L⊥
f̸=0
R
ΩO
|∇f|2
R
ΩO
|f|2 .
This completes the proof that˜µM+1(ΩO)≤µM+1(ΩO). Inequality (1) now follows
by induction onk. □
Continuing with the proof of the theorem, letNN(λ, Ω·) and ND(λ, Ω·) denote
the number of Neumann and Dirichlet eigenvalues less than or equal toλ on Ω·,
respectively. By Lemma 2.6, we have
PN
i=1ND(λ,ΩI,i)
λ ≤ ND(λ,ΩI)
λ ≤ ND(λ,Ω)
λ
≤ ND(λ,ΩO)
λ ≤ NN(λ,ΩO)
λ ≤
PM
j=1NN(λ,ΩO,j)
λ
because having larger eigenvalues means that there are fewer eigenvalues up to some
fixed number. By Weyl’s law on rectangles (see Proposition 2.2),
lim
λ→∞
PN
i=1ND(λ, ΩI,i)
λ =
PN
i=1|ΩI,i|
4π =|ΩI|
4π ,
and similarly
lim
λ→∞
PM
j=1NN(λ, ΩO,j)
λ =|ΩO|
4π .
Thus, we obtain
|ΩI|
4π ≤ lim inf
λ→∞
ND(λ, Ω)
λ ≤ lim sup
λ→∞
ND(λ, Ω)
λ ≤|ΩO|
4π .
Letting ϵ→ 0 gives
lim
λ→∞
ND(λ, Ω)
λ =|Ω|
4π,
12 G. MÅRDBY AND J. ROWLETT
as desired. □
If we had ann-dimensional domain Ω⊂ Rn, we could analogously approximate
it by an inner and outer covering ofn-dimensional rectangles. Since both Weyl’s
law and the variational principles hold for such rectangles, the proof would look
exactly the same, and we would obtain
lim
λ→∞
N(λ)
λn/2 = ωn|Ω|
(2π)n.
Weyl’s law formulated as in Theorem 2.5 also holds for Neumann boundary con-
ditions. However, the proof is more difficult than the Dirichlet case, partly because
there is no obvious analogue of Dirichlet-Neumann bracketing. In particular, two
domains Ω1 and Ω2 satisfying Ω1⊂ Ω2 need not satisfyλk(Ω2)≤ λk(Ω1) in the
Neumann case, as they do in the Dirichlet case. In light of Theorem 2.3, while
functions f∈H1
0(Ω1) can easily be extended to being inH1
0(Ω2) by defining them
to be zero inΩ2\Ω1, functionsf∈H1(Ω1) cannot always be extended toH1(Ω2).
Interestingly, while we only considered domains with piecewise smooth boundary,
Weyl’s law can be proven to hold for any bounded domain inRn with Dirichlet
boundary conditions. This is, however, not true in the Neumann case, where the
domain in addition needs to satisfy the so calledextension property. See [49, Ch.
3] for details. See also [68] for examples of domains which do not satisfy Weyl’s law
in the Neumann case.
As mentioned in §1, Weyl’s law shows that the spectrum of ann-dimensional
domain determines its dimensionn and itsn-dimensional volume. A natural ques-
tion then is whether the spectrum determinesall of the geometry of a domain, or
more generally a Riemannian manifold. As one might guess, this is a hard prob-
lem because for for most Riemannian manifolds one cannot compute the spectrum
explicitly. There is, however, one particular class of examples for which one can
explicitly compute the spectrum in a certain sense, namelyflat tori.
