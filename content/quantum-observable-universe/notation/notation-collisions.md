A handful of common letters carry overloaded meanings in the
literature. The following conventions are enforced throughout this
paper to keep them disambiguated:

- **$c$** = color (never charm; charm is $\mathfrak{c}$).
- **$b$** = generic variable (never bottom quark; bottom is $\mathfrak{b}$).
- **$p$** = brane point (never proton number; proton number is $Z$).
- **$E$** alone = not used for an exceptional divisor, energy, or
  elliptic curve. Use $\mathcal{S}_p$, $\mathbf{E}$, or $\mathcal{E}_q$
  respectively. $E_{\mathfrak{H}}$ (with hadron subscript) is allowed
  for crossing energy.
- **$\gamma$** = Euler–Mascheroni constant or Dirac matrices only.
  Never use $\gamma$ for a vortex or closed cycle; use $\varrho$.
- **$\chi_q$** = Lyapunov exponent (distinct from $\chi_\zeta(c)$,
  the character).
- **$\zeta$** = three distinct uses, never bare. $\zeta_n := e^{2\pi i/n}$
  (primitive $n$-th root of unity, **always with integer subscript** —
  e.g. $\zeta_5$, $\zeta_6 = e^{i\pi/3}$); $\zeta(s)$ (Riemann
  zeta function, **always parenthesised**, e.g. $\zeta(2) = \pi^2/6$,
  $\zeta(3) = $ Apéry); $\chi_\zeta(c)$ (character, **always with
  $\chi$ prefix and argument**). The bare token $\zeta$ alone is
  **not used**.
- **$\mathcal{P}_n$** = Goncharov period filtration class (weight-$n$
  periods modulo lower-weight). Distinct from $P_\ell$ = elementary
  symmetric polynomials in Jucys–Murphy elements
  ([`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou)),
  which are non-calligraphic and indexed by symmetric-polynomial
  degree.
- **$H_q$** alone = not used. Three distinct concepts share the
  letter $H$: $\mathcal{H}_q$ (shuffle Hopf algebra), $\hat{H}_q$
  (Hamiltonian operator), $H_n(q)$ or $H_q(\lambda)$ (Hecke /
  hook-length, always with argument).
- **$r$** = spinor information rate, $r = q^{1/2}$, $r^2 = q$.
  Eigenvalue of the elementary half-twist on the spin-½ fundamental
  rep of $\mathrm{SU}_q(2)$. Reserved exclusively for this purpose.
  **Never** use $r$ for radius (use $\rho$), recurrence rate (use
  $\nu$), or Wenzl level (use $\ell$ — see below). The relation to
  $q$ is exactly analogous to $i$ vs $-1$: $r$ opens up the 2-D
  spinor (spin-½) representation from the 1-D adjoint (spin-1)
  representation. **Never** use $t$ for $q^{1/2}$ either ($t$ is
  the standard knot-polynomial variable in $V_K(t)$, and $t$ is
  also reserved for time-like usage).
- **$\ell$** = Wenzl principal-specialisation length (number of
  points in $s_\lambda(1, q^2, \ldots, q^{2(\ell-1)})$). **Renamed
  from $r_W$** to free $r$ for the spinor rate. Old code/docs
  using $r_W$ should migrate to $\ell$.
- **Numerical $q = 1.1097$** (or any specific value of the substrate
  parameter) should not appear outside the introduction, Chapter 8
  (Information Theory, for falsifiability computations), and
  Chapter 11 (Observations). Geometry chapters should use symbolic
  $q$.

**Approximation convention (derived / observed values).** Numerical
values derived from the substrate parameter $q_0$ or compared to
experimental data use $\approx$ (or $\simeq$), never $=$, unless an
explicit error term is present. Exact algebraic identities (e.g.\
$c_q = 1/(q-1)$) use $=$ since they hold for all $q$.

**Hecke–Skein convention.** The Hecke algebra generator is
$\sigma_i$ (never $T$, never $t$ or $A$ for the Jones polynomial
variable). The Iwahori–Hecke algebra $H_n(q)$ is presented as a
quotient of the braid group algebra of $B_n$, so the same symbol
$\sigma_i$ denotes both the braid-group generator and its image in
$H_n(q)$ — context disambiguates. The Jones polynomial is always
$J_K(q)$, not $V_K(t)$.

**Categories vs CPT operators.** Categories are typeset bold,
$\mathbf{C}$, $\mathbf{Rep}$, etc. The calligraphic $\mathcal{C}$
is **reserved for the charge-conjugation operator** in CPT
discussions (parity $\mathcal{P}$, time-reversal $\mathcal{T}$,
combined $\mathcal{CP}$, $\mathcal{CPT}$). Calligraphic $\mathcal{C}$
must never denote a category in this paper; readers should always
parse a calligraphic $\mathcal{C}$ in context as a discrete
symmetry operator. The $\mathcal{P}$ / $\mathcal{T}$ / $\mathcal{CP}$
companions are likewise CPT operators; they do not collide with any
categorical or geometric reservation.
