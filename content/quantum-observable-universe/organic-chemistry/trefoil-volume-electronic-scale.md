**Statement.**
The molecular crossing-energy quantum
$\lvert q + q^{-1}\rvert_{\mathrm{mol}}$
([molecular crossing quantum](#prop:molecular-crossing-quantum))
admits an independent verification at high (mpmath, $60$ decimal
digits) precision using the trefoil knot $3_{1} = T(2,3)$ as the
electronic-scale topological invariant.

The trefoil's Alexander polynomial is, by
[$\Delta_{T(2,N)}$ closed form](#lem:alexander-T2N-closed-form) at
$N = 3$:

$$
  \Delta_{3_{1}}(q) = q^{2} - 1 + q^{-2}.
$$

At the substrate value $q_{0}$, this evaluates to a positive real
number and is recorded in the witness as the electronic-scale
invariant.

**Why the trefoil and not its hyperbolic volume.**
The trefoil is a torus knot, hence non-hyperbolic — SnapPy reports
$\mathrm{Vol}(3_{1}) = 0$.  The natural electronic-scale topological
invariant of the trefoil is therefore its Alexander polynomial, not
a hyperbolic volume.  This is the precise analogue of the
hyperbolic-volume cross-check for hyperbolic knots such as $4_{1}$.

**Verification.**
The cross-check confirms two things:

1. The high-precision value of $\lvert q + q^{-1}\rvert_{\mathrm{mol}}$
   computed via $\mathrm{Vol}(4_{1})$-derived $q$ at mpmath precision
   $60$ agrees with the float-precision C1 value to within
   $10^{-9}\ \mathrm{eV}$.
2. The trefoil Alexander polynomial closed form
   $\Delta_{3_{1}}(q) = q^{2} - 1 + q^{-2}$ is positive at the
   substrate value, confirming that the electronic-scale invariant is
   well-defined.

The witness `crossing-energy-mol-direct.witness.json` records the
high-precision $q$, $\lvert q + q^{-1}\rvert$, the trefoil Alexander
evaluation, and the precision-agreement assertion.

**Caveat.**
Both routes share the inputs $\alpha$, $m_{e}/m_{p}$, and
$\lvert q + q^{-1}\rvert_{\mathrm{nuc}} = 8\ \mathrm{MeV}$, so the
cross-check verifies *precision*, not *full independence*.  A
strongly independent route requires deriving
$\lvert q + q^{-1}\rvert_{\mathrm{nuc}}$ from the Skein-binding
Lagrangian.
