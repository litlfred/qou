The [substrate parameter](#def:substrate-parameter) is described
in the text as an element of
$\mathrm{End}(\mathbf{1}) \cong k^\times$, the fibre coordinate
on a $\mathbb{G}_m$-family.  This remark makes the
$\mathbb{G}_m$-structure explicit and reformulates the
not-root-of-unity axiom as torsion avoidance.

**The multiplicative group scheme.**
The substrate parameter is a section of $\mathbb{G}_m$: a map
$q \colon M \to \mathbb{G}_m(k)$ where
$\mathbb{G}_m(k) = k^\times$ is the group of units.  The
$\mathbb{G}_m$-family of operators

$$
  d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d
$$

is a universal deformation parametrised by the tautological
coordinate on $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$.

The Lusztig integral form
$\mathcal{U}^\mathbb{Z}_q(\mathfrak{su}(2))$ is a
$\mathbb{Z}[q, q^{-1}]$-algebra.  A ring homomorphism
$\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ is a
$k$-point of $\mathbb{G}_m$, and base change along $\iota$
specialises the universal family to the quantum group at
$q_0 = \iota(q)$.

**Torsion points of the multiplicative group.**
The torsion subgroup of $\mathbb{G}_m$ is the group of roots
of unity:

$$
  \mathbb{G}_m[n] = \mu_n = \{\zeta \in k^\times : \zeta^n = 1\},
  \qquad
  \mathbb{G}_m[\mathrm{tors}] = \mu_\infty = \bigcup_{n \geq 1} \mu_n.
$$

The not-root-of-unity axiom in the
[substrate parameter](#def:substrate-parameter) says exactly:

$$
  q(p) \notin \mu_\infty(k)
  \qquad\text{for all } p \in M.
$$

That is: the section $q \colon M \to \mathbb{G}_m$ avoids the
torsion subscheme.  The image of $q$ lies in the complement
$\mathbb{G}_m \setminus \mu_\infty$.

**Necessity of torsion avoidance.**
At a torsion point $q_0 = e^{2\pi i m/n}$:

1. The quantum dimension $[n]_{q_0} = 0$ (the $n$-th quantum
   integer vanishes).
2. The Frobenius pairing degenerates on the representation
   $V_{(n-1)/2}$ (quantum dimension zero means null vector).
3. The non-degeneracy axiom (QOU axiom 1) fails.
4. The representation category truncates to finitely many
   simple objects, becoming a modular tensor category
   (Chern--Simons TQFT at level $n$).

At $q_0 = 1$: this is the **universal torsion point** ($1^n = 1$
for all $n$).  The quantum integer $[k]_1 = k$ never vanishes
for $k \geq 1$, but the comultiplication becomes cocommutative
($R_1 = 1 \otimes 1$) and the braiding becomes symmetric.  The
Frobenius pairing does not degenerate, but the braided structure
collapses to a symmetric one.

**The projective compactification.**
Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via the
standard inclusion $k^\times \hookrightarrow k \cup \{\infty\}$.
The two boundary points are:

- $q = 0$: the $d_q$ operator is undefined ($q^{-1}$ pole).
  This is the boundary where the spatial differential $d$
  diverges.
- $q = \infty$: $d_q \to \pi_V \circ d$ (pure vertical
  projection).  The spatial world vanishes and only the Reeb
  (internal spin) direction survives.

The torsion points $\mu_\infty$ are dense in $\mathbb{G}_m$
(over $\mathbb{C}$).  The substrate parameter must avoid this
dense set, living in the **non-torsion locus**

$$
  \mathbb{G}_m^{\mathrm{nt}}
  = \mathbb{G}_m \setminus \mu_\infty.
$$

For the archimedean realisation over $\mathbb{R}$: the torsion
points in $\mathbb{R}^\times$ are just $\{1, -1\}$.  The
condition $q > 1$ (from $q(p) \geq 1$) combined with
$q \neq 1$ places $q$ in $(1, \infty) \subset \mathbb{R}^\times$,
which is torsion-free.

**The $q = 1$ limit as torsion specialisation.**
The [NS regularity problem](#def:ns-regular-qou) asks what
happens when the section
$q \colon M \to \mathbb{G}_m^{\mathrm{nt}}$ is extended to a
section $\bar{q} \colon M \to \mathbb{G}_m$ that hits the
torsion point $q = 1$.

In algebraic geometry, extending a family across a torsion
specialisation is controlled by the **Neron model** of the
abelian scheme.  The obstruction to extending the Frobenius--Hopf
structure across $q = 1$ lives in the **special fibre** of the
Neron model:

$$
  \mathrm{obs}(q \to 1)
   \in 
  \Phi_{q=1}(\mathbb{G}_m)
  = 
  \text{component group of the special fibre}.
$$

For $\mathbb{G}_m$ itself, the Neron model is trivial (smooth
group scheme), so the component group is trivial and the
extension exists.  But the Frobenius--Hopf structure is **not**
a $\mathbb{G}_m$-torsor — it is a family of Hopf algebras
parametrised by $\mathbb{G}_m$, and the extension problem is
more subtle.

**Connection to the NS obstruction.**
The [NS obstruction class](#prop:ns-obstruction-tower)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ lives in the
cohomology with coefficients in the banding sheaf
$\mathcal{B} = \mathcal{O}_M^\times$.  The sheaf of units
$\mathcal{O}_M^\times$ is the sheaf of sections of
$\mathbb{G}_m$.  So:

$$
  \kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m)
$$

and the specialisation $q \to 1$ is the pullback along the
inclusion $\{1\} \hookrightarrow \mathbb{G}_m$:

$$
  \kappa_n\big|_{q=1}
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{ \mathrm{sp}_{q=1}}
  H^2(\mathcal{S}, \mu_\infty).
$$

The specialisation map $\mathrm{sp}_{q=1}$ factors through the
Kummer sequence

$$
  1 \to \mu_n \to \mathbb{G}_m \xrightarrow{(\cdot)^n}
  \mathbb{G}_m \to 1
$$

and the obstruction persists iff $\kappa_n$ is **not** divisible
by $n$ in $H^2(\mathcal{S}, \mathbb{G}_m)$ for any $n$.

For the Descartes universe with $\chi(A) = -6$, this is a special
case of [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction):
$\kappa_0$ is non-trivial at every finite place $p \nmid 6$, so the
specialisation $\kappa_0|_{q = \zeta_n}$ at every primitive $n$-th
root of unity with $\gcd(n, 6) = 1$ is non-zero in
$H^2(\mathcal{S}, \mu_n)$. The NS obstruction does not collapse —
this is the fluid-dynamics realization of the substrate's perpetual
obstruction at every cyclotomic place.
