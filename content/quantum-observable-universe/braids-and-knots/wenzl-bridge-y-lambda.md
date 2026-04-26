**Why the Wenzl-bridge applies in QOU.**

The QOU axioms — rigid braided monoidal category $\mathbf{C}$ with
self-dual fundamental object $A$, fibre functor $\tau \colon
\mathbf{C} \to R\text{-mod}$, Tannaka--Krein Hopf algebra
$H := \mathrm{Aut}^\otimes(\tau)$ — give exactly the setup of
**Schur--Weyl duality** between the Hecke algebra $H_n(R, q)$ and
the centraliser of the diagonal $H$-action on
$V^{\otimes n}$, where $V := \tau(A)$:

$$
  H_n(R, q) \;=\; \mathrm{End}_H(V^{\otimes n}),
  \qquad
  V^{\otimes n}
  \;\cong\; \bigoplus_{\lambda \,\vdash\, n} V_\lambda^H \otimes V_\lambda^{H_n}
$$

with $\dim_R V_\lambda^{H_n} = d_\lambda$ the classical Hecke irrep
dimension.

The fibre-functor trace on $\mathrm{End}_R(V^{\otimes n})$
restricted to the $H_n(R, q)$ factor is the **unique Markov trace**
$\mathrm{tr}_M$ with parameter $z$ determined by
$z \cdot \dim_q V = 1$.  At our $z = 1/(\sqrt q + 1/\sqrt q)$, the
fibre functor's $q$-dimension on $V$ satisfies $\dim_q V = \sqrt q
+ 1/\sqrt q = [2]_q^{\mathrm{symm}}$ — consistent with $V$ being
the spin-$1/2$ standard representation of the Hopf algebra
$H \cong U_q(\mathfrak{sl}_2)$ of the running QOU example.

**Schur--Weyl decomposition of the trace.**
The Markov trace decomposes as
$\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$ where the
block weight is the **categorical $q$-dimension of the
$H$-multiplicity space** $V_\lambda^H$ normalised by the regular
representation:

$$
  y_\lambda(q, z)
  \;=\;
  \frac{\dim_q V_\lambda^H}
       {\sum_{\mu \,\vdash\, n} d_\mu \cdot \dim_q V_\mu^H}.
$$

The categorical $q$-dimension on $V_\lambda^H$ is the
**principal Schur specialisation**
$s_{\lambda, X}(Q)$ where $Q = q^2$ and $X = Q^r$ for the
"effective rank" $r$ determined by $\dim_q V = X^{1/2} + X^{-1/2}$
— equivalently, by the Markov constraint
$X = q \cdot z / (1 - Q + q \cdot z)$.

The Wenzl-bridge formula is therefore not assumed; it is
**forced** by Schur--Weyl + Tannaka--Krein + the categorical
$q$-dimension on the fibre functor.  Wenzl 1988 establishes that
this is the unique trace satisfying the Markov property, closing
the equivalence with
([procedure](#prop:alpha-k-derivation-procedure))'s linear-system
characterisation.

**Definition (Wenzl-bridge $y_\lambda$).**
Let $Q := q^2$ and

$$
  X(q, z) \;:=\; \frac{q \cdot z}{1 - Q + q \cdot z}.
$$

For $\lambda \vdash n$ with cells $(i, j)$ of content $c(i, j) =
j - i$ and hook length $h_\lambda(i, j)$, define the principal
Schur specialisation

$$
  s_{\lambda, X}(Q)
  \;:=\;
  Q^{n(\lambda)}
  \prod_{(i, j) \in [\lambda]}
    \frac{1 - X \cdot Q^{c(i, j)}}{1 - Q^{h_\lambda(i, j)}},
$$

with $n(\lambda) = \sum_i (i - 1)\lambda_i$ the Macdonald
$n$-statistic.  The Jones--Markov block weights are

$$
  \boxed{\;
  y_\lambda(q, z)
  \;=\;
  \frac{s_{\lambda, X}(Q)}
       {\sum_{\mu \,\vdash\, n} d_\mu \, s_{\mu, X}(Q)}
  \,\in\, R(\!(q, z)\!).
  \;}
$$

**Why the Markov trace is unique (1-dimensional trace space).**
The Hecke-algebra tower $\{H_n(R, q) \hookrightarrow H_{n+1}(R, q)\}$
admits a single coherent trace family $\{\mathrm{tr}_n\}$ satisfying

(a) **trace property**: $\mathrm{tr}_n(ab) = \mathrm{tr}_n(ba)$ for
$a, b \in H_n$,

(b) **Markov property**: $\mathrm{tr}_{n+1}(x \cdot \sigma_n) =
z \cdot \mathrm{tr}_n(x)$ for $x \in H_n$,

(c) **normalisation**: $\mathrm{tr}_1(1) = 1$
(the "vol $= 1$" normalisation — the unit element has unit trace).

The space of such families forms a **one-dimensional line** in
the trace functionals, and the scalar choice (c) selects a
specific point on it.  At generic $q$
(Ocneanu--Jones; Wenzl 1988): (a) + (b) iteratively reduce trace
values on $H_{n+1}$ to values on $H_n$, and (c) pins the overall
scale.  Equivalently, $\mathrm{tr}_M$ is the **Frobenius integral**
of $H_n(R, q)$ — the unique linear functional dual to the
Markov-property-respecting Frobenius pairing on the algebra.

Either characterisation is one-dimensional; the Wenzl-bridge
formula is the unique element with these properties, and the
linear-system formulation
([procedure](#prop:alpha-k-derivation-procedure)) is its
finite-$n$ truncation.

**Equivalence verification.**
Verified numerically against the linear-system witness at
$n \in \{2, \ldots, 12\}$ to machine precision; verified
symbolically (sympy.simplify) at $n \in \{2, 3, 4\}$.

**Why "fractional Wenzl".**
Classical Wenzl theory specialises $z$ to $1/[N+1]_q^{\mathrm{symm}}$
for some integer $N$, identifying the centraliser as
$\mathrm{SU}_q(N)$.  At $q_0 \approx 1.1097$ the equation
$X = Q^N$ solves at non-integer $N \approx 0.91$ — no integer
$\mathrm{SU}_q(N)$.  The bridge is that $X$ may be any $q$-rational
function of $(q, z)$; the principal Schur formula extends
analytically without an integer rank.  This is what permits the
QOU substrate value $q_0$ (chosen for physical observables, not
for $\mathrm{SU}_q(N)$ closure) to admit a clean closed-form
Markov trace.

**Witnesses.**
[`folio-assistant/computations/y-lambda-wenzl-witness.json`](#)
contains $y_\lambda$ at 100 dps for $n \in \{2, \ldots, 12\}$ and
symbolic q-rational forms for $n \in \{2, 3, 4\}$.  Generator:
[`y_lambda_wenzl_bridge.py`](#).  Wall-clock at $n = 12$:
$\sim 6$ s at 1000 dps.

**Consequences.**

| Existing block | Becomes |
|---|---|
| ([procedure](#prop:alpha-k-derivation-procedure)) — $y_\lambda$ as linear-system inverse | one of two equivalent characterisations |
| ([sign pattern](#rem:y-lambda-sign-pattern)) — empirical $y_{(1^n)} < 0$ for $n \geq 4$ | derived: at $X(q_0) > 1$ the alt-block factors flip sign at $n \geq 4$ |
| ([Plancherel boundedness](#prop:plancherel-weight-boundedness)) — $\sum d_\lambda y_\lambda = 1$ | tautology by construction (the denominator is the partition function) |
