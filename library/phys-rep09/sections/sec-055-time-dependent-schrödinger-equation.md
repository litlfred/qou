---
doc_id: phys-rep09
doc_title: "Physics Reports The Magnus expansion and some of its applications"
section_id: sec-055-time-dependent-schrödinger-equation
section_title: "Time-dependent Schrödinger equation"
section_number: null
pages: 72-75
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
---
To keep the treatment as simple as possible, we commence by considering the one-dimensional time-dependent
Schrödinger equation (¯h = 1)
i ∂
∂t ψ(t, x) = Hψ(t, x) ≡−
1
2
∂2
∂x2 ψ(t, x) + V(x)ψ(t, x),
(311)
with initial condition ψ(0, x) = ψ0(x). If we look for a solution of the form ψ(t, x) = φ(t)ϕ(x), it is clear that, by substituting
into (311), one gets φ(t) = e−itE, where E is a constant and ϕ(x) is the solution of the second order differential equation
−
d2ϕ
dx2 + V(x)ϕ = Eϕ.
(312)
If E > V the solution is oscillatory, whereas if E < V the solution is a linear combination of exponentially increasing and
decreasing functions. For bounded problems, this last condition always takes place at the boundaries. Since
Z
|ψ(x, t)|2dx =
Z
|ϕ(x)|2dx < ∞,
(313)
it is clear that the exponentially increasing solutions have to be canceled, and this can only occur for certain values of the
constant E, which are precisely the eigenvalues of the problem.
Let us assume that the system has only a discrete spectrum, and denote by {En, ϕn}∞
n=0, with Ei < Ej, i < j, the complete
set of eigenvalues and associated eigenvectors. It is well known that we can take {ϕn}∞
n=0 as an orthonormal basis and, since
(311) is linear, any solution can be written as
ψ(t, x) =
∞
X
n=0
cn e−itEnϕn(x).
(314)
Using the standard notation for the inner product, one has
⟨ϕn(x)|ψ(t, x)⟩=
Z
ϕ∗
n(x) ψ(t, x)dx = cn e−itEn
(315)
and
|⟨ϕn(x)|ψ(t, x)⟩|2 = |cn|2
S. Blanes et al. / Physics Reports 470 (2009) 151–238
223
is the probability of finding the system in the eigenstate ϕn, so that P
n |cn|2 = 1. The energy is given by
E = ⟨ψ|H|ψ⟩=
Z
ψ∗(t, x)H ψ(t, x)dx =
∞
X
n=1
∞
X
m=1
c∗
ncmHn,m,
(316)
where
Hn,m ≡⟨m|H|n⟩= ⟨ϕm|H|ϕn⟩.
In general, the coefficients cn decrease very fast with n and, in some cases, the system allows only a finite number of states.
In that situation, one may consider the Schrödinger equation as a finite dimensional linear system where the Hamiltonian
is a matrix with elements Hn,m. This is precisely the case for the examples examined in Section 4.
When the Hamiltonian is explicitly time-dependent, this procedure is no longer valid. Instead, one may use some
alternative techniques which we now briefly review.
(i) Spectral decomposition. Let us assume that the system is perturbed with a time-dependent potential, i.e., Eq. (311)
takes the form
i ∂
∂t ψ(t, x) = ˆH(t)ψ(t, x) ≡(ˆT + ˆV(t))ψ(t, x),
(317)
where
ˆTψ ≡−
1
2
∂2ψ
∂x2 ,
ˆV(t)ψ ≡(V(x) + ˜V(t, x))ψ.
In this case, we cannot use separation of variables. However, since {ϕn} is a complete basis we can still write the solution as
ψ(t, x) ≃
d−1
X
n=0
cn(t)e−itEn ϕn(x),
(318)
where En and ϕn are the exact eigenvalues and eigenfunctions when ˜V = 0, and the complex coefficients cn give the
probability amplitude to find the system in the state ϕn (P
n |cn(t)|2 = 1 for all t). Then, substituting (318) into (317)
we obtain the matrix equation
i
d
dt
c(t) = H(t)c(t),
c(0) = c0,
(319)
where c = (c0, . . . , cd−1)T ∈Cd and H ∈Cd×d is a Hermitian matrix associated to the Hamiltonian
(H(t))ij = ⟨ϕi| ˆH(t) −ˆH0|ϕj⟩ei(Ei−Ej)t,
i, j = 1, . . . , d
and ˆH0 = ˆH(t = 0). Given the initial wave function ψ(0, x), the components of c0 are determined by c0,i = ⟨ϕi|ψ(0, x)⟩.
Obviously, any complete basis can be used in this case, although the norm of the matrix H(t) may depend on the choice.
In addition, the number of basis elements (i.e. the minimum dimension d necessary to obtain a sufficiently accurate result)
also depends on the chosen basis.
(ii) Space discretization. This procedure intends to take advantage of the structure of the Hamiltonian ˆH in (317): ˆV is
diagonal in the coordinate space and ˆT is diagonal in the momentum space. Let us assume that the system is defined in the
interval x ∈[x0, xf ] with periodic boundary conditions. We can then split this interval in d parts of length 1x = (xf −x0)/d
and consider cn = ψ(t, xn) where xn = x0 + n1x, n = 0, 1, . . . , d −1. Then a finite dimensional linear equation similar
(but with a different coefficient matrix H) to Eq. (319) results. Since ˆV is diagonal in the coordinate space and ˆT is diagonal
in momentum space, it is possible to use complex Fast Fourier Transforms (FFTs) for evaluating the products Hc, where
ˆTψ(t, xn) = F −1DTF ψ(t, xn), and DT is a diagonal operator.
We thus see that whatever the procedure used (spectral decomposition or space discretization), one ends up with a linear
equation of the form
i
dψ
dt (t) = H(t)ψ(t),
ψ(0) = ψ0
(320)
where ψ(t) now represents a complex vector with d components which approximates the (continuous) wave function.
The computational Hamiltonian H(t) appearing in (320) is thus a space discretization (or other finite-dimensional model)
of ˆH(t) = ˆT + ˆV(t). Numerical difficulties come mainly from the unbounded nature of the Hamiltonian and the highly
oscillatory behavior of the wave function.
It is at this point when numerical algorithms based on the Magnus expansion, such as they have been formulated in
previous sections, come into play for integrating in time the linear system (320). To put them in perspective, let us first
introduce some other numerical methods also used in this context. Our exposition is largely based on the reference [182].
224
S. Blanes et al. / Physics Reports 470 (2009) 151–238
6.1.1.1. The implicit midpoint rule. The approximation to the solution of (320) provided by this scheme is implicitly defined
by
iψn+1 −ψn
1t
= H(tn+1/2)
1
2(ψn+1 + ψn),
(321)
where tn+1/2 = 1
2(tn+1 + tn). Here, and in the sequel, for clarity, we have denoted by 1t the time step size and tn = n1t.
Alternatively,
ψn+1 = r(−i1tH(tn+1/2))ψn,
with r(z) =
1 + 1
2z
1 −1
2z .
(322)
Observe that, as r is nothing but the Cayley transform, the numerical propagator is unitary and consequently the Euclidean
norm of the discrete wave function is preserved along the evolution: ∥ψn+1∥= ∥ψn∥. This is a crucial qualitative feature
the method shares with the exact solution, contrarily to other standard numerical integrators, such as explicit Runge–Kutta
methods. From a purely numerical point of view, the algorithm is stable for any step size 1t.
Another useful property of this numerical scheme is time-symmetry: exchanging in (322) n by n + 1 and 1t by −1t we
get the same numerical method again. Equivalently, r(−z) = r(z)−1, exactly as the exponential ez.
With respect to accuracy, it is not difficult to show that, if H(t) is bounded and sufficiently smooth, the error verifies
∥ψn −ψ(tn)∥= O(1t2)
(323)
uniformly for n1t in a time interval [0, tf ]. In other words, the implicit midpoint rule is a second-order method. It happens,
however, that the constant in the term O(1t2) depends on bounds of H′ and H′′ and on the norm of the third derivative of
the solution ψ. Since, in general, the wave function is highly oscillatory in time, this time derivative can become large, and
so the use of very small time steps is mandatory.
6.1.1.2. The exponential midpoint rule. Another possibility to get approximate solutions of (320) consists of replacing r(z)
by exp(z) in (322):
ψn+1 = exp(−i1t H(tn+1/2))ψn.
(324)
Now, instead of solving systems of linear equations as previously, one has to compute the exponential of a large matrix times
a vector at each integration step. In this respect, the techniques reviewed in Section 5.6 can be efficiently implemented. The
exponential midpoint rule (324) also provides a unitary propagator and it is time-symmetric. In addition, the error satisfies
the same condition (323), but now the constant in the O(1t2) term is independent of the time derivatives of ψ under certain
assumptions on the commutator [H(t), H(s)] [183]. As a consequence, much larger time steps can be taken to achieve the
same accuracy as with the implicit midpoint rule.
6.1.1.3. Integrators based on the Magnus expansion. The method (324) is a particular instance of a second order Magnus
method when the integral
R 1t
0
H(s)ds is replaced by the midpoint quadrature rule. In fact, we have already used it in (274).
Obviously, if higher order approximations are considered, the accuracy can be enhanced a great deal. This claim has to
be conveniently justified, however, since the order of the numerical methods based on Magnus has been deduced when
∥1tH(t)∥→0 and is obtained by studying the remainder of the truncated Magnus series. In the Schrödinger equation, on
the other hand, one has to cope with discretizations of unbounded operators, so in principle it is not evident how the previous
results on the order of accuracy apply in this context. In [183], Hochbruck and Lubich analyze, in detail, the application of
the fourth-order Magnus integrator (254) to Eq. (320), showing that it works extremely well even with step sizes for which
the corresponding ∥1tH(t)∥is large. In particular, the scheme retains fourth order of accuracy in 1t independently of the
norm of H(t) when H(t) = T + V(t), T is a discretization of −1
2
∂2
∂x2 (with maximum eigenvalue Emax ∼(1x)−2) and V(t) is
sufficiently smooth under the time step restriction 1t√
Emax ≤Const. This is so even when there is no guarantee that the
Magnus series converges at all.
6.1.1.4. Symplectic perspective. The evolution operator corresponding to (317) is not only unitary, but also symplectic with
canonical coordinates and momenta Re(ψ) and Im(ψ), respectively. If we carry out a discretization in space, this symplectic
structure is inherited by the corresponding Eq. (319). It makes sense, then, to write c = q + ip and consider the equations
satisfied by q, p ∈Rd, namely
q′ = H(t)p,
p′ = −H(t)q,
(325)
which can be interpreted as the canonical equations corresponding to the Hamiltonian [184]
H(t, q, p) = pTH(t)p + qTH(t)q.
(326)
Denoting z = (q, p)T, it is clear that
z′ = (A(t) + B(t)) z
S. Blanes et al. / Physics Reports 470 (2009) 151–238
225
where
A(t) =

0
H(t)
0
0

,
B(t) =

0
0
−H(t)
0

.
(327)
For this system it is possible, therefore, to apply the commutator-free Magnus integrators constructed in Section 5.8.2. In
addition, one has
[B, [B, [B, A]]] = [A, [A, [A, B]]] = 0,
and this property allows us to use specially designed and highly efficient integration methods [178].
