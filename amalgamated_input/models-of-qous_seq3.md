<!-- FILE_START: symmetric-point-intro.md -->
The [mass-gap conjecture](#conj:yang-mills-mass-gap) locates the
vanishing of the gap on the $2$-torsion locus
$\mu_2 = \{1, -1\} \subset \mathbb{G}_m$.  This section examines the
symmetric point $q = 1$ directly: which structures of the mass tower
$\mathrm{End}_{\mathbf{C}}(A_n)$ survive the specialisation, which
degenerate, and at what order in $h = q - 1$ each lost structure is
restored when the deformation is switched back on.  The pattern that
emerges is uniform: the symmetric point deletes no spectrum, but loses
*resolution* — distinctions that braiding maintains (chirality of
crossings, inter-nucleon channel identity, accidental level
coincidences) collapse at $q = 1$ and reopen at definite infinitesimal
orders.
<!-- FILE_END: symmetric-point-intro.md -->

<!-- FILE_START: symmetric-point-channel-collapse.md -->
At the symmetric point $q = 1$ the three Hecke channels $\sigma$,
$\sigma^{-1}$, and $(\sigma + \sigma^{-1})/2$ degenerate to a single
operator; the reason is a purely algebraic identity in any field.

**Proposition.** *Let $R$ be a field with $2 \neq 0$ and let $s \in R$
satisfy $s^2 = 1$.  Then $s^{-1} = s$, and consequently*

$$
  \frac{s + s^{-1}}{2} \;=\; s .
$$

**Remark.** Any family of operator assignments drawn from
$\{\sigma,\ \sigma^{-1},\ (\sigma + \sigma^{-1})/2\}$ collapses to a
single operator under the specialisation $q = 1$ of the Hecke relation
$(\sigma - q)(\sigma + q^{-1}) = 0$, which at $q = 1$ reads
$\sigma^2 = 1$.
<!-- FILE_END: symmetric-point-channel-collapse.md -->

<!-- FILE_START: physical-units-gap-linear.md -->
The observable gap and the categorical bound scale differently near the symmetric point $q = 1$: expressing the gap in physical units divides the cubically-vanishing categorical bound by $\hbar_q^{\,2}$, and that change in vanishing order — cubic to linear — is the point.

**Proposition.** *Let $q \in \mathbb{R}$ with $q \neq 0, 1$, let
$\mathfrak{E}_\times(q) = \tfrac{1}{2}(q - q^{-1})$ be the
[crossing energy](#def:crossing-energy), and let
$\hbar_q = (q-1)/q$.  Then the crossing-energy gap bound
$\Delta_q = \mathfrak{E}_\times(q)\,(q-1)^2$ satisfies the exact
identity*

$$
  \frac{\Delta_q}{\hbar_q^{\,2}}
  \;=\;
  \frac{q\,(q-1)(q+1)}{2},
$$

*so the gap in physical units vanishes **linearly** in
$h = q - 1$ as $q \to 1$, while the categorical bound $\Delta_q$
itself vanishes cubically.  Both vanish identically at $q = 1$.*

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: its one archimedean commitment is treating $q$ as a real physical scale near $q = 1$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: physical-units-gap-linear.md -->

<!-- FILE_START: symmetric-point-resolution-loss.md -->
The specialisation $q = 1$ deletes no part of the mass tower: the
weight spectrum of $\mathrm{End}_{\mathbf{C}}(A_n)$ remains semisimple,
with every Plancherel weight
$w_\lambda(q) = [n]_q! \,/\, H_q(\lambda)^2$ strictly positive at
$q = 1$ (the classical measure $d_\lambda^2/n!$).  What the symmetric
point loses is *resolution*, in two graded ways, collected into a
stratification.

**Channel identity.**  By
[channel collapse](#prop:symmetric-point-channel-collapse), the three
inter-nucleon assignments $\sigma$, $\sigma^{-1}$,
$(\sigma + \sigma^{-1})/2$ coincide at $q = 1$: the distinctions
carrying chirality and pairing data are invisible at the symmetric
point.

**Accidental degeneracy.**  At $n = 6$ — the two-nucleon strand
count — the weight tower has six distinct levels for $q \neq 1$ but
five at $q = 1$: the conjugate pair $\{(5,1), (2,1^4)\}$ and the pair
$\{(3,3), (2,2,2)\}$, distinct for all $q \neq 1$, land on the common
classical value $25/720$.  The deformation resolves an accidental
coincidence of the symmetric group ($d_{(5,1)} = d_{(3,3)} = 5$) that
the classical point cannot see.  The splitting reopens at second
order,

$$
  w_{(3,3)}(1+\varepsilon) - w_{(5,1)}(1+\varepsilon)
  \;=\; \tfrac{5}{18}\,\varepsilon^2 + O(\varepsilon^3),
$$

with the linear term excluded by the bar-invariance
$w_\lambda(q) = w_\lambda(q^{-1})$.

**The stratification.**  Collecting these rates with the gap orders of
the [linear-vanishing identity](#prop:physical-units-gap-linear) gives
a uniform picture of the infinitesimal neighbourhood $q = 1 + \varepsilon$:

| order | surviving / reopening structure |
|---|---|
| $\varepsilon^0$ | semisimple tower; classical Plancherel weights; vacuum level |
| $\varepsilon^1$ | physically normalised mass gap $\tfrac{1}{2}q(q-1)(q+1)$; Dirac--Reeb coupling $(1 - q^{-1})$ |
| $\varepsilon^2$ | degeneracy resolution (the $n = 6$ inter-nucleon channel splitting, coefficient $5/18$) |
| $\varepsilon^3$ | categorical gap bound $\tfrac{1}{2}(q - q^{-1})(q-1)^2$ |

Every structure survives the limit *surreally* — as a positive
infinitesimal of definite order — while only the standard parts of the
gap quantities vanish.  This is the computational content of the
$\mu_2$-vanishing clause of the
[mass-gap conjecture](#conj:yang-mills-mass-gap): the classical point
is not an impoverished theory but an unresolved one.  Numerical
verification at fifty digits, including the $5/18$ coefficient and the
convention checks against the canonical pinning witness, is recorded in
[`q1-mass-gap-probe.witness.json`](../../../computations/q1-mass-gap-probe.witness.json).
<!-- FILE_END: symmetric-point-resolution-loss.md -->

<!-- FILE_START: unit-circle-photonic-sector.md -->
On the unit circle $q = e^{i\theta}$ the
[crossing energy](#def:crossing-energy) is purely imaginary,

$$
  \mathfrak{E}_\times(e^{i\theta})
  \;=\; \tfrac{1}{2}\bigl(e^{i\theta} - e^{-i\theta}\bigr)
  \;=\; i \sin\theta ,
$$

so a crossing on $|q| = 1$ generates *phase*, not energy: the circle
direction of $\mathbb{G}_m$ carries interference and transport — the
electrodynamic, photonic sector — while real, positive crossing energy
requires leaving the circle ($q$ real, $q > 1$).  The two real points
$\mu_2 = \{1, -1\}$, where the circle meets the real axis, are doubly
degenerate: there both the phase resolution and the mass scale vanish
at once.

The [categorical Dirac operator](#def:categorical-dirac-operator)
realises the same split internally: its deviation from the bare
connection is the Reeb-direction coupling weighted by
$(1 - q^{-1})$, which vanishes at $q = 1$ and is first order in
$h = q - 1$ — the same order at which the physically normalised gap
opens.  Mass, in this reading, is a first-order radial phenomenon on
$\mathbb{G}_m$; electrodynamics is the angular phase flow that
survives on the circle.

At the fibre level the deformation parameter remains a formal,
possibly complex variable; it is the archimedean evaluation that
selects a real $q_0 > 1$ and thereby a massive sector.  The remark
records the geometry of that selection: massless (photonic) content is
at home on $|q| = 1$, and any chiral or massive content requires
$|q| \neq 1$.
<!-- FILE_END: unit-circle-photonic-sector.md -->

