The Planck step $t_P(q) = q/(q-1)$
([discrete Planck step](#rem:discrete-planck-step)) is a rational
function of $q$, so it — and the iteration $f_q(z) = z^2 + c(q)$ —
realise over any field. This remark records the finite-field and
$p$-adic incarnations of the Planck dynamics.

**Finite-field dynamics.**
Over $k = \mathbb{F}_\pp$ with $q \in \mathbb{F}_\pp^\times$, the
iteration $f_q \colon \mathbb{F}_\pp \to \mathbb{F}_\pp$ is a map
on a finite set.  Every orbit is eventually periodic, and the orbit
structure encodes the "Planck dynamics" of the finite-field QOU:

- **Orbit length** $|O_x|$ = number of Planck steps before the
  state $x$ recurs.  This is the analogue of the Poincaré
  recurrence time.
- **Fixed points** of $f_q$: the states $z$ satisfying
  $z^2 + c(q) = z$, i.e., $z^2 - z + c = 0$.  These exist in
  $\mathbb{F}_\pp$ iff $1 - 4c$ is a quadratic residue mod $\pp$.
- **Period-$n$ orbits**: the roots of
  $f_q^{\circ n}(z) = z$ that are not fixed by any
  $f_q^{\circ d}$ with $d \mid n$.  The number of such orbits
  is related to the Weil zeta function of the curve
  $w^2 = z^2 + c$ over $\mathbb{F}_\pp$.

The Julia set $J(f_q)$ over $\mathbb{C}$ is the "complexification"
of this finite orbit structure: the boundary between escaping and
bounded orbits is the continuous analogue of the partition of
$\mathbb{F}_\pp$ into short-period and long-period orbits.

**$p$-Adic Planck step.**
Over $\mathbb{Q}_\pp$, the substrate parameter $q$ has a $\pp$-adic
valuation.  The Planck time $t_P = q/(q-1)$ has
$v_\pp(t_P) = v_\pp(q) - v_\pp(q-1)$.  When $q \equiv 1 \pmod{\pp^n}$ (near the classical limit in the $\pp$-adic
topology), $v_\pp(q-1) \geq n$ and $t_P$ has large $\pp$-adic
valuation — the Planck time is "$\pp$-adically large",
corresponding to slow dynamics.  When $v_\pp(q-1) = 0$ (the
Big Bang regime in $\pp$-adic terms), $t_P$ has minimal valuation
and the dynamics is fastest.

The Witt vector lift
([Witt vector lift](#rem:witt-lift-qou)) promotes the
$\mathbb{F}_\pp$ orbit structure to a $\mathbb{Z}_\pp$-lattice:
the finite orbits of $f_q$ over $\mathbb{F}_\pp$ lift to
Teichmüller representatives in $\mathbb{Z}_\pp$, and the
$\pp$-adic Planck step acts on these lifts via the Frobenius
endomorphism.  The passage $\mathbb{F}_\pp \to \mathbb{Q}_\pp \to \mathbb{C}$ is the arithmetic analogue of the cosmological
progression from discrete (Big Bang) to continuous (classical
limit).
