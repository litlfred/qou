**Proposition (torus-knot dictionary).**
*The lepton and meson mass towers are both indexed by torus knots
$T(2, n)$ for $n = 3, 5, 7, \ldots$ (odd primes), with the following
correspondence:*

| Generation | $n$ | Lepton ($H_2$) | Quark flavor ($H_3$) | Meson ($q\bar{q}$) |
|---|---|---|---|---|
| 1st | 3 | $\mathfrak{e}$ (electron) | $u, d$ | $\pi$ (pion) |
| 2nd | 5 | $\mu$ (muon) | $s$ (strange) | $K$ (kaon) |
| 3rd | 7 | $\tau$ (tau) | $s$ (heavy-strange) | $\eta, \phi$ |

*The lepton at generation $k$ is the closure of $\sigma_1^{2k+1}$ in
$H_2(q)$; the meson at the same generation is the Hopf-bound pair of
quarks whose flavor content involves $T(2, 2k+1)$ crossing structure
in $H_3(q)$.*

## The structural duality

The dictionary reveals a **highest-weight / lowest-weight duality**
between the two sectors:

| Feature | Lepton ($H_2$) | Meson ($H_3$) |
|---|---|---|
| Braid type | $\sigma^n$ (all positive) | $\mathfrak{M}_+ = (\sigma_0\sigma_1)^2\sigma_1\sigma_0$ (all positive) |
| Hecke eigenvalue | $q$ only (highest weight) | $q$ dominates: symmetric partition $(3)$ carries $62\%$ of the Markov trace at $6$ crossings, rising to $100\%$ as crossing count $\to \infty$ |
| SDP selection | trivial (1-dim $H_2$) | symmetric-channel-dominated (all-positive crossings force eigenvalue $q > \lvert{-q^{-1}}\rvert$ at every crossing) |
| Mass formula input | $\mathrm{Vol}(4_1)/\hbar_q^2$ (hyperbolic volume) | $\mathrm{tr}_M(\mathfrak{M}, q_0)$ (Markov trace at substrate) |
| Calibration | CAL-2: $m_\mu/m_\mathfrak{e}$ (exact, Lean-proved modulo CAL-2) | CAL-3: $m_\pi$ (genuinely independent of $m_\mathfrak{e}$, $q_0$) |
| Role of $4_1$ | transition knot $T(2,3) \to T(2,5)$ giving mass ratio | same transition, different evaluation (dual volume?) |

The lepton sector evaluates in the **Kashaev $N \to \infty$ limit**
(hyperbolic volume); the meson sector evaluates at **finite $q_0$**
(Markov trace).  This is the highest-weight / lowest-weight exchange:
the asymptotic invariant (volume) governs fundamental particles, while
the finite-$q$ invariant (trace) governs composite bound states.
