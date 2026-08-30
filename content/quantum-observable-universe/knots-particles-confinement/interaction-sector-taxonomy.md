**Definition (interaction-sector taxonomy).**
*The framework's interactions form three sectors — **strong**, **electromagnetic**, and **weak** — classified by the bar-involution parity of the sector's primary observable, the calibration its scale anchors to, and its coupling object.*

| Sector | Primary observable | Bar parity ($q \mapsto q^{-1}$) | Scale anchor | Coupling object |
|---|---|---|---|---|
| strong | binding $\mathfrak{E}_{\mathrm{bind}}$, volume | even (cosh channel) | $E_0 = m_e/(q_0(q_0-1))$ | Borromean Markov trace $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$; confinement-SDP duals |
| electromagnetic | Coulomb energy, Hartree scale | open at observable level; coupling object: exact $\cosh + \sinh$ mix | $E_h = \alpha_{EM}^2\, m_e c^2$ | $\alpha_{EM}^{-1} = q_0\,[9]_q\,[10]_q$ dressed by the Chern–Simons tower |
| weak | $\mathfrak{Q}_\beta$, decay widths $\mathfrak{D}_\beta$ | odd (sinh channel) | CAL-2 ($\mathfrak{D}_\beta$, proxy $m_\mu/m_e$) | bar-odd channel of the complex volume |

*Processes* are not sectors: a [fusion process](#def:fusion-process) is a strand-balanced rearrangement inside the strong sector, while β-decay moves proton number on the subject side and is thereby routed to the weak sector. The bar-even and bar-odd channels are intertwined by the bar involution itself — the rotation between the two channel recurrences of [the binding–$Q_\beta$ complex volume conjecture](#conj:binding-qbeta-complex-volume) — so the taxonomy's parity column is a statement about where each sector's observable lives, not a wall between algebras.

The Lean formalization records the taxonomy as a total assignment and proves that weak is the unique bar-odd-assigned sector, that strong is the unique bar-even one, and that the electromagnetic parity assignment is exactly the open one at the observable level.

At the *coupling* level the electromagnetic cell is now derived. The quantum integer $[n]_q$ is bar-even — invariant under $q \mapsto q^{-1}$ — so in the bare coupling $C(q) = q\,[9]_q[10]_q$ only the exponential prefactor moves under the bar involution, giving the exact decomposition

$$
  C(q) \pm C(q^{-1}) \;=\; (q \pm q^{-1})\,[9]_q[10]_q .
$$

The bar-even part of the electromagnetic coupling is the cosh-channel (strong-side) multiple and the bar-odd part the sinh-channel (weak-side) multiple of one invariant factor $B = [9]_q[10]_q$: the electromagnetic coupling is the full exponential mix $e^{\lambda} B$ with $\lambda = \ln q$, sitting at the intertwiner point between the two pure channels rather than in either. At the substrate anchor the odd-to-even ratio is $\tanh(\ln q_0) \approx 0.10396$ exactly for the bare coupling, and $\approx 0.10356$ for the Chern–Simons-dressed value, whose tower is not bar-covariant in a single parity ($\hbar_q^2 \mapsto q^2 \hbar_q^2$). The decomposition is proved over any field, without nondegeneracy hypotheses, in the library module `QOU.Interactions.EmCouplingBarParity`; the numeric twin is `computations/probes/alpha_em_bar_parity_probe.py`.
