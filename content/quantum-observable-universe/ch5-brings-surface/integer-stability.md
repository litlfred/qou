The beta-stability line
([beta-stability](#prop:beta-stability)) gives a continuous curve
$p^*(A)$ in the $(A, p)$-plane.  Physical nuclei must have
integer proton and neutron numbers.  The valley of stability is
the set of integer lattice points nearest to this curve.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with
$q = 1.110$.  For each mass number $A \in \mathbb{Z}_{\geq 1}$,
define the continuous optimum

$$
  p^*(A)
  \;=\;
  \frac{A}{2 + c \, A^{2/3}},
  \qquad
  c \;=\; \frac{a_C}{2\,a_A}
  \;=\; \frac{(q - q^{-1}) \cdot \lambda_C}{2\,a_A}
  \;\approx\; 0.01497.
$$

The **stable proton number** is the integer minimizer

$$
  p_{\mathrm{stab}}(A)
  \;=\;
  \operatorname*{arg\,min}_{p \in \{0, 1, \ldots, A\}}
  M(p,\, A - p)
$$

where $M(p, n)$ is the nuclear mass from the Skein binding
Lagrangian ([Skein binding Lagrangian](#def:skein-binding-lagrangian)).

**Integer selection.**
The continuous optimum $p^*(A)$ is generically irrational (the
exponent $A^{2/3}$ ensures $p^*$ is not a rational function of
$A$).  The integer minimizer satisfies

$$
  p_{\mathrm{stab}}(A)
  \;\in\;
  \bigl\{\lfloor p^*(A) \rfloor,\;
  \lceil p^*(A) \rceil\bigr\}
$$

with the even-even rule: among the two candidates, the pair
$(p, n)$ with both $p$ and $n$ even is preferred by the pairing
energy $\mathcal{L}_{\mathrm{pair}}$ from the Skein binding
Lagrangian.

**Diophantine error.**
Define the fractional error

$$
  \varepsilon(A)
  \;=\;
  |p_{\mathrm{stab}}(A) - p^*(A)|.
$$

Since $p^*(A)$ involves the irrational exponent $A^{2/3}$, the
sequence $\{\varepsilon(A)\}_{A \geq 1}$ is equidistributed in
$[0, \tfrac{1}{2}]$ (by Weyl's theorem applied to the fractional
parts of $A/(2 + cA^{2/3})$).  The **magic numbers** — the
mass numbers $A$ at which nuclei are anomalously stable — correspond
to values where $\varepsilon(A)$ is near zero: the continuous
optimum falls close to an integer, so the lattice approximation
incurs minimal energy cost.

**Magic numbers from Diophantine approximation.**
The observed magic proton numbers $\{2, 8, 20, 28, 50, 82\}$
and magic neutron numbers $\{2, 8, 20, 28, 50, 82, 126\}$
are characterised by two simultaneous conditions:

1. **Small Diophantine error**: $\varepsilon(A) < \delta$ for
   a threshold $\delta \approx 0.1$.
2. **Shell closure**: the Skein polynomial of the multi-nucleon
   link $\mathcal{N}(p, n)$ factors into a product of closed
   Hopf sub-links at these values, analogous to closed orbits
   in the shell model.

The first condition is purely number-theoretic; the second is
topological.  Their coincidence at the magic numbers is a
consequence of the specific value $q = 1.110$ — at other values
of $q$, the magic numbers would shift.
