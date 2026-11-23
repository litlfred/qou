**Proof.** 
The lepton assignment follows from the torus-knot mass tower \cite{jones1987}. In the backup reading used here, the electron is the trefoil $T(2,3)$ (3 crossings), the muon is the cinquefoil $T(2,5)$ (5 crossings), and the tau is the septafoil $T(2,7)$ (7 crossings), each a braid $\sigma_1^n$ in $H_2(q)$. Under the owner ruling of 2026-11-21 the electron is instead the word $\sigma_0\sigma_1\sigma_0 \in B_3$, whose closure is the Hopf link; its crossing count is still $3$, so the first-generation label is unchanged, while the muon and tau entries have not been re-derived under that ruling.

The meson assignment uses the quark flavour–lepton partner relation. Each quark is an unknot strand carrying one crossing letter, whose orientation ($\sigma$ or $\sigma^{-1}$) is the quark's own. Its index is the crossing count of its lepton partner: $3$ for the $u$- and $d$-quarks (partner $T(2,3)$) and $5$ for the $s$-quark (partner $T(2,5)$). These indices are generation labels, not crossings carried by the quark strands. A meson $q_1\bar{q}_2$ at $H_3$ is assigned the label sum $n_1 + n_2$:

- $\pi$: $\bar{u}d = 3 + 3 = 6$
- $K$: $\bar{u}s = 3 + 5 = 8$
- $\phi$: $s\bar{s} = 5 + 5 = 10$; $\eta$ sits at the same rung but is an $\mathrm{SU}(3)_{\mathrm{f}}$-octet mixture of $u\bar{u}$, $d\bar{d}$ and $s\bar{s}$ rather than pure $s\bar{s}$

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
