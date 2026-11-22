---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-027-treatment-of-general-nonlinear-equations
section_title: "Treatment of general nonlinear equations"
section_number: null
pages: 32-35
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
As a matter of fact, the Magnus expansion can be formally generalized to any nonlinear explicitly time-dependent
differential equation. Given the importance of the expansion, it has, indeed, been (re)derived a number of times along
the years in different settings. We have to mention, in this respect, the work of Agrachev and Gamkrelidze [106-108], and
S. Blanes et al. / Physics Reports 470 (2009) 151-238 183

Strichartz [53]. In the context of Hamiltonian dynamical systems, the expansion was first proposed in [109] and subsequently
applied in a more general context in [110] with the aim of designing new numerical integration algorithms.

By introducing nonstationary vector fields and flows, it turns out that one gets a linear differential equation in terms of
operators which can be analyzed in exactly the same way as in Section 2. Thus it is in principle possible to build approximate
solutions of the differential equation which preserve some geometric properties of the exact solution. The corresponding
Magnus series expansion allows us to write the formal solution, and then different approximations can be obtained by
truncating the series. Obviously, this formal expansion presents two difficulties in order to render a useful algorithm in
practice: (i) it is not evident what the domain of convergence is, and (ii) some device has to be designed to compute the
exponential map once the series is truncated.

Next we briefly summarize the main ideas involved in the procedure. To begin with, let us consider the autonomous
equation

x’ = f(x), x(0) = Xp) € R". (150)
If gy! denotes the exact flow of (150), i.e. x(t) = y' (Xo), then for each infinitely differentiable map g : R” —> R, g(g'(y))
admits the representation

g(y'(y)) = O'[gl(y) (151)

where the operator @' acts on differentiable functions [111]. To be more specific, let us introduce the Lie derivative (or Lie
operator) associated with f,

n
a
[p= _—. 152
It acts on differentiable functions F : R" —> R™ (see [112, Chap. 8] for more details) as

LpF (y) = F'(y)fy),
where F’(y) denotes the Jacobian matrix of F. It follows from the chain rule that, for the solution ¢' (xo) of (150),

d
art ox) = (L4F)(g" (Xo)), (153)

and applying the operator iteratively one gets

dé
ah Yo) = (LEF)(g" (Xo), k= 1.

Therefore, the Taylor series of F(y' (xo)) at t = 0 is given by

tk
F(G' (Xo) = D7 75 HEF) 0) = exp (tLe) FI (%o). (154)
k>0

Now, putting F(y) = Id(y) = y, the identity map, this is just the Taylor series of the solution itself

k
(Ko) = JF (Uf) (Ko) = exp (th [IA] 0%).

k>0

If we substitute F by g in (154) and compare with (151), then it is clear that &‘[g](y) = exp(tL,)[g](y). The object exp(tL,)
is called the Lie transform associated with f.
At this point, let us suppose that f(x) can be split as f(x) = f;(x) + f2(x), in such a way that the systems

x =f(x), x = f,(x)
have flows gj and 5, respectively, so that
&(g; (y)) = exp(tl, )[gl(y) i= 1, 2.
Then, for their composition one has

&(Y5,0 vi (y)) = exp(sLe,) exp(tLe, Ig] (y). (155)

This is precisely formula (154) with f = f;, t replaced with s and with F(y) = exp(tLe, )[g](y). Notice that the indices 1 and
2, as well as s and t to the left and right of Eq. (155), are permuted. In other words, the Lie transforms appear in the reverse
order to their corresponding maps [79].

The Lie derivative L¢ satisfies some remarkable properties. Given two functions y1, yo, it can be easily verified that

Leary + a2 Wo) = ale + ale, o1,0,2€R
Lei W2) = (Lei) va + Wi Lee
184 S. Blanes et al. / Physics Reports 470 (2009) 151-238

and by induction we can prove the Leibniz rule

k

Un Wa) = > (‘) (Liv) (Uva)
i=0

with Ley = Le (i 'W) and Ley = w, justifying the name of Lie derivative. In addition, given two vector fields f and g, then

Oy Lg + gL g = Loi traxg,
[Le, Lg] = Ip Lg — Lg lp = Ln,

where h is another vector field corresponding to the Lie bracket of the vector fields f and g, denoted by h = (f, g), whose
components are

“(08 afi

h; = (f, = [gi — Lg fi = —-g—). 156

i= (Eg): = Legi — Lgl 2 (55, si) (156)
Moreover, from (151) and (153) (replacing F with g) we can write

d d

Gr? Io) = F-8(H" (Xo) = (Les) (H" (Xo) = PLL ](%0).
Particularizing to the function g(x) = Id;(x) = x;, we get

d t t 7

ae? Ud) = PL lidl(y), j= 1,....m Y= Xo
or, in short,

d t t

—P' = P'ley, Y=Xo, (157)

dt
ie., a linear differential equation for the operator ©‘. Notice that, as expected, Eq. (157) admits as formal solution

&' =exp(tlay)), y= Xo- (158)
We can follow the same steps for the non-autonomous equation

x = f(t, x), (159)
where, now, the operational equation to be solved is

d t t

a? =P ley, Y=Xo- (160)

To simplify notation, from now on we consider Xo as a set of coordinates such that f(t, xo) is a differentiable function of Xo.
Since Ls is a linear operator, we can then directly use the Magnus series expansion to obtain the formal solution of (160) as
' = exp(Lwitx,)), With w = >, w;. The first two terms are now

t
wictsxa) =f f(s, Xo)ds
0

1 t $1
W2(t, Xo) = -/ as, [ ds (f(s1, Xo), f(S2, Xo)). (161)
0 0

Observe that the sign of wz is changed when compared with £22 in (43), and the integrals only affect the explicit time-
dependent part of the vector field. In general, due to the structure of Eqs. (30) and (160), the expression for w,(t, Xo) can be
obtained from the corresponding 2,,(t) in the linear case by applying the following rules:

(1) replace A(t)) by f(t), Xo);
(2) replace the commutator [-, -] by the Lie bracket (156);
(3) change the sign in w,(t, Xo) for even n.

Once wi"! = a w;(t, Xo) is computed, it still remains to evaluate the action of the Lie transform exp(Lyw(r,x9)) on the
initial conditions xo. At time t = T, this can be seen as the 1-flow solution of the autonomous differential equation
S. Blanes et al. / Physics Reports 470 (2009) 151-238 185

y =w"(T,y), y(0) = Xo, (162)

since y(1) = exp(Lwr,x9))Xo = X(T).

Although this is arguably the most direct way to construct a Magnus expansion for arbitrary time dependent nonlinear
differential equations, it is by no means the only one. In particular, Agrachev and Gamkrelidze [107,108] obtain a similar
expansion by transforming (160) into the integral equation

t
p= i+ [ &°X,ds (163)
0

which is subsequently solved by successive approximations. Here, for clarity, we have denoted x = Ls,xq)- Then one gets
the formal series

t . t 4 a
Id + | dtX, + | dt, il dt)XipX, +++
0 0 0

00 t t tm—1 . .
w+) [ a, [ ay f tin Xt + Xey- (164)
mai /0 0 0

An object with this shape is called a formal chronological series [107], and the set of all formal chronological series can be
endowed with a real associative algebra structure. It is then possible to show that there exists an absolutely continuous
formal chronological series

. 00 t 4 tm—1 . .
vicky = | an [ at f tin Gin(Xeys «++» Xt) (165)
ma1/0 0 0

such that

og

@ = exp(V;(X;)).

Here Gn (Xr ee Xin) are Lie polynomials, homogeneous of the first grade in each variable, which can be algorithmically
constructed. In particular,

G(X) = Xy

- 3 1- -
G, (Xr, > Xp) = 7 Xe , Xe]

ss 3 15 5s s > 2.3
G3(Xr, > Xp, Xt) = glx: [X,, Xt, ]] + [[X:,, Xt], X,,])-

The series (165) in general diverges, even if the Lie operator xX is analytic [106]. Nevertheless, in certain cases convergence
holds. For instance, if X, belongs to a Banach Lie algebra & for all t € IR, where one has a norm satisfying ||[X, Y]|| < ||X|I|lY |
for allX, Y € Band to IX \|ds = to || Le(s,xo) lds < 0.44, then V; (X) converges absolutely in B [107]. As a matter of fact, an
argument analogous to that used in [30,70] may allow us to improve this bound and get convergence for

t. 1 2% 1
il IXsllds < al — a ik = 1.08686870....
0 2Jo 2+5(1—cot5)
