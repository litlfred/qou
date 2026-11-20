**Proof.** 
The lepton assignment follows from the torus-knot mass tower \cite{jones1987}. The electron is the trefoil $T(2,3)$ (3 crossings), the muon is the cinquefoil $T(2,5)$ (5 crossings), and the tau is the septafoil $T(2,7)$ (7 crossings). Each is a braid $\sigma_1^n$ in $H_2(q)$.

The meson assignment follows from the quark flavor–torus-knot identification. The $d$-quark carries the $T(2,3)$ crossing structure (3 crossings per constituent), and the $s$-quark carries $T(2,5)$ (5 crossings per constituent). A meson $q_1\bar{q}_2$ at $H_3$ has total crossings $n_1 + n_2$:

- $\pi$: $\bar{u}d = 3 + 3 = 6$ crossings
- $K$: $\bar{u}s = 3 + 5 = 8$ crossings
- $\phi$: $s\bar{s} = 5 + 5 = 10$ crossings; $\eta$ sits at the same rung but is an $\mathrm{SU}(3)_{\mathrm{f}}$-octet mixture of $u\bar{u}$, $d\bar{d}$ and $s\bar{s}$ rather than pure $s\bar{s}$

The normal form in $H_3(q)$ is determined by the Hecke reduction of the meson braid word $\mathfrak{M}_+$ ([Meson (categorical)](categorical-meson.md)). $\square$

## The structural duality

The dictionary reveals a highest-weight / lowest-weight duality between the two sectors:

| Feature | Lepton ($H_2$) | Meson ($H_3$) |
|---|---|---|
| Braid type | $\sigma^n$ (all positive) | $\mathfrak{M}_+ = (\sigma_0\sigma_1)^2\sigma_1\sigma_0$ (all positive) |
| Hecke eigenvalue | $q$ only (highest weight) | $q$ dominates: symmetric partition $(3)$ carries $62\%$ of the Markov trace at $6$ crossings, rising to $100\%$ as crossing count $\to \infty$ |
| SDP selection | trivial (1-dim $H_2$) | symmetric-channel-dominated (all-positive crossings force eigenvalue $q > \lvert{-q^{-1}}\rvert$ at every crossing) |
| Mass formula input | $\mathrm{Vol}(4_1)/\hbar_q^2$ (hyperbolic volume) | $\mathrm{tr}_M(\mathfrak{M}, q_0)$ (Markov trace at substrate) |
| Calibration | CAL-2: $P_{\mathrm{skew}}^{\beta}$, proxy $m_\mu/m_\mathfrak{e}$ (exact, proved modulo CAL-2) | CAL-3: $P_{\mathrm{avg}}^{\pi}$, proxy $m_\pi$ (genuinely independent of $m_\mathfrak{e}$, $q_0$) |
| Role of $4_1$ | transition knot $T(2,3) \to T(2,5)$ giving mass ratio | same transition, different evaluation (dual volume?) |

The lepton sector evaluates in the Kashaev $N \to \infty$ limit (hyperbolic volume). The meson sector evaluates at finite $q_0$ (Markov trace). This is the highest-weight / lowest-weight exchange. The asymptotic invariant (volume) governs fundamental particles, while the finite-$q$ invariant (trace) governs composite bound states.
