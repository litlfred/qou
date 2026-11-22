---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-065-time-dependent-schrödinger-equation
section_title: "Time-dependent Schrödinger equation"
section_number: null
pages: 72-75
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
To keep the treatment as simple as possible, we commence by considering the one-dimensional time-dependent
Schrédinger equation (fi = 1)
a) 1 a?
i—w(t,x) = Hw(t,x) = —~— W(t, x) + V@)w(e, x), (311)
at 2 dx?
with initial condition y (0, x) = Wo(x). If we look for a solution of the form y(t, x) = $(t)g(x), itis clear that, by substituting
into (311), one gets #(t) = e~, where E is a constant and (x) is the solution of the second order differential equation

oy

dx?
If E > V the solution is oscillatory, whereas if E < V the solution is a linear combination of exponentially increasing and
decreasing functions. For bounded problems, this last condition always takes place at the boundaries. Since

five. pPax = [ Ipeo de < oo, (313)

it is clear that the exponentially increasing solutions have to be canceled, and this can only occur for certain values of the
constant E, which are precisely the eigenvalues of the problem.

Let us assume that the system has only a discrete spectrum, and denote by {En, @n}p°.9, with Ej < Ej, i < j, the complete
set of eigenvalues and associated eigenvectors. It is well known that we can take {y,}7°., as an orthonormal basis and, since
(311) is linear, any solution can be written as

+V(x)y = Eg. (312)

oo
VEX = Dore gne). (314)
n=0
Using the standard notation for the inner product, one has
(gaa) |e, x)) = il OR (x) We (t, x)dx = cy ew (315)

and

Gna) (t, x))1? = lenl?
S. Blanes et al. / Physics Reports 470 (2009) 151-238 223

is the probability of finding the system in the eigenstate g,, so that }°, |cn/? = 1. The energy is given by

6 = (iin) = f wat We de= YY Gent (316)

n=1m=1

where
An.m = (m|H|n) = (@m|H|¢n)-

In general, the coefficients c, decrease very fast with n and, in some cases, the system allows only a finite number of states.
In that situation, one may consider the Schrédinger equation as a finite dimensional linear system where the Hamiltonian
is a matrix with elements Hy, m. This is precisely the case for the examples examined in Section 4.

When the Hamiltonian is explicitly time-dependent, this procedure is no longer valid. Instead, one may use some
alternative techniques which we now briefly review.

(i) Spectral decomposition. Let us assume that the system is perturbed with a time-dependent potential, i.e., Eq. (311)
takes the form

a ~ nn
pV) = HOWE %) = (T+ V(t)) w(t, x), (317)

where

n 12° » ~
Tw =-S7y, VW = (VQ) + VUE, x))Y.
2 dx’
In this case, we cannot use separation of variables. However, since {g,} is a complete basis we can still write the solution as

d—1

VEN ~ Do calthe™ gn), (318)

n=0

0, and the complex coefficients c, give the

where E, and g, are the exact eigenvalues and eigenfunctions when V=
= 1 for all t). Then, substituting (318) into (317)

probability amplitude to find the system in the state gp (}°,, |Cn (t)|?
we obtain the matrix equation

Set) =H(t)e(t), c(0) = eo, (319)

where ¢ = (Co,...,Ca_1)' € C4 and H € C*™? is a Hermitian matrix associated to the Hamiltonian
HO) = (GIAO — Hola) MO", j= 1,...d

and Ao = Att = 0). Given the initial wave function y (0, x), the components of ¢p are determined by co,; = (g;| (0, x)).

Obviously, any complete basis can be used in this case, although the norm of the matrix H(t) may depend on the choice.
In addition, the number of basis elements (i.e. the minimum dimension d necessary to obtain a sufficiently accurate result)
also depends on the chosen basis.

(ii) Space discretization. This procedure intends to take advantage of the structure of the Hamiltonian Ain (317): V is
diagonal in the coordinate space and T is diagonal in the momentum space. Let us assume that the system is defined in the
interval x € [Xo, xp] with periodic boundary conditions. We can then split this interval in d parts of length Ax = (xs — Xo) /d
and consider c, = w(t, Xn) where x, = Xp + nAx,n = 0,1,...,d — 1. Then a finite dimensional linear equation similar
(but with a different coefficient matrix H) to Eq. (319) results. Since Vis diagonal in the coordinate space and T is diagonal
in momentum space, it is possible to use complex Fast Fourier Transforms (FFTs) for evaluating the products Hc, where
Twit, Xn) = F~'DrF W(t, Xn), and Dr is a diagonal operator.

We thus see that whatever the procedure used (spectral decomposition or space discretization), one ends up with a linear
equation of the form

d
iM =HOVO, wO)=vYo (320)

where w(t) now represents a complex vector with d components which approximates the (continuous) wave function.
The computational Hamiltonian H(t) appearing in (320) is thus a space discretization (or other finite-dimensional model)
of A(t) =T + V(t). Numerical difficulties come mainly from the unbounded nature of the Hamiltonian and the highly
oscillatory behavior of the wave function.

It is at this point when numerical algorithms based on the Magnus expansion, such as they have been formulated in
previous sections, come into play for integrating in time the linear system (320). To put them in perspective, let us first
introduce some other numerical methods also used in this context. Our exposition is largely based on the reference [182].
224 S. Blanes et al. / Physics Reports 470 (2009) 151-238

6.1.1.1. The implicit midpoint rule. The approximation to the solution of (320) provided by this scheme is implicitly defined
by
Was — Vi 1
i tna) 5 Unt + Yad, (321)
where tn41/2 = (tn + t,). Here, and in the sequel, for clarity, we have denoted by At the time step size and t, = nAt.
Alternatively,
. . 1+ 3z
Vn41 = 1(-iAtH (th41/2)) Wn, with r(z) = To
~ 2
Observe that, as r is nothing but the Cayley transform, the numerical propagator is unitary and consequently the Euclidean
norm of the discrete wave function is preserved along the evolution: || Wn+1|| = || Wnll. This is a crucial qualitative feature
the method shares with the exact solution, contrarily to other standard numerical integrators, such as explicit Runge-Kutta
methods. From a purely numerical point of view, the algorithm is stable for any step size At.
Another useful property of this numerical scheme is time-symmetry: exchanging in (322) n byn+ 1 and At by —At we
get the same numerical method again. Equivalently, r(—z) = r(z)~', exactly as the exponential e”.
With respect to accuracy, it is not difficult to show that, if H(t) is bounded and sufficiently smooth, the error verifies

Yn — W(tn)l| = O(At?) (323)

uniformly for nAt in a time interval [0, t;]. In other words, the implicit midpoint rule is a second-order method. It happens,
however, that the constant in the term @(At?) depends on bounds of H’ and H” and on the norm of the third derivative of
the solution y. Since, in general, the wave function is highly oscillatory in time, this time derivative can become large, and
so the use of very small time steps is mandatory.

. (322)
Z

6.1.1.2. The exponential midpoint rule. Another possibility to get approximate solutions of (320) consists of replacing r(z)
by exp(z) in (322):

Wn = exp(—iAt H(tny1/2)) Wn. (324)

Now, instead of solving systems of linear equations as previously, one has to compute the exponential of a large matrix times
a vector at each integration step. In this respect, the techniques reviewed in Section 5.6 can be efficiently implemented. The
exponential midpoint rule (324) also provides a unitary propagator and it is time-symmetric. In addition, the error satisfies
the same condition (323), but now the constant in the @(At’) term is independent of the time derivatives of w under certain
assumptions on the commutator [H(t), H(s)] [183]. As a consequence, much larger time steps can be taken to achieve the
same accuracy as with the implicit midpoint rule.

6.1.1.3. Integrators based on the Magnus expansion. The method (324) is a particular instance of a second order Magnus
method when the integral Ie H(s)ds is replaced by the midpoint quadrature rule. In fact, we have already used it in (274).
Obviously, if higher order approximations are considered, the accuracy can be enhanced a great deal. This claim has to
be conveniently justified, however, since the order of the numerical methods based on Magnus has been deduced when
|| AtH(t)|| = 0 and is obtained by studying the remainder of the truncated Magnus series. In the Schrédinger equation, on
the other hand, one has to cope with discretizations of unbounded operators, so in principle it is not evident how the previous
results on the order of accuracy apply in this context. In [183], Hochbruck and Lubich analyze, in detail, the application of
the fourth-order Magnus integrator (254) to Eq. (320), showing that it works extremely well even with step sizes for which

the corresponding || AtH(t)|| is large. In particular, the scheme retains fourth order of accuracy in At independently of the
norm of H(t) when H(t) = T + V(t), T is a discretization of — 3 ed (with maximum eigenvalue Emax ~ (Ax)~?) and V(t) is
sufficiently smooth under the time step restriction At.\/Emax < Const. This is so even when there is no guarantee that the
Magnus series converges at all.

6.1.1.4. Symplectic perspective. The evolution operator corresponding to (317) is not only unitary, but also symplectic with
canonical coordinates and momenta Re(y) and Im(w), respectively. If we carry out a discretization in space, this symplectic
structure is inherited by the corresponding Eq. (319). It makes sense, then, to write c = q + ip and consider the equations
satisfied by q, p € R“, namely

q=H@®p, p= —H(t)q, (325)

which can be interpreted as the canonical equations corresponding to the Hamiltonian [184]
HC, qs P) = p'H(t)p + q'H(t)q. (326)
Denoting z = (q, p)', it is clear that
z' = (A(t) + B(t)) z
S. Blanes et al. / Physics Reports 470 (2009) 151-238 225

where

a= (5 ): B® = (“ie 0): (327)

For this system it is possible, therefore, to apply the commutator-free Magnus integrators constructed in Section 5.8.2. In
addition, one has

[B, [B, [B, A]]] = [A [A, [A, B]]] = 0,

and this property allows us to use specially designed and highly efficient integration methods [178].
