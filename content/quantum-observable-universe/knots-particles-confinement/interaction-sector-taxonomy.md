**Definition (interaction-sector taxonomy).**
*The framework's interactions form three sectors — **strong**, **electromagnetic**, and **weak** — classified by the bar-involution parity of the sector's primary observable, the calibration its scale anchors to, and its coupling object.*

| Sector | Primary observable | Bar parity ($q \mapsto q^{-1}$) | Scale anchor | Coupling object |
|---|---|---|---|---|
| strong | binding $\mathfrak{E}_{\mathrm{bind}}$, volume | even (cosh channel) | $E_0 = m_e/(q_0(q_0-1))$ | Borromean Markov trace $\mathrm{tr}_M(\beta_{\mathrm{Bor}})$; confinement-SDP duals |
| electromagnetic | Coulomb energy, Hartree scale | not established | $E_h = \alpha_{EM}^2\, m_e c^2$ | $\alpha_{EM}^{-1} = q_0\,[9]_q\,[10]_q$ dressed by the Chern–Simons tower |
| weak | $\mathfrak{Q}_\beta$, decay widths $\mathfrak{D}_\beta$ | odd (sinh channel) | CAL-2 ($\mathfrak{D}_\beta$, proxy $m_\mu/m_e$) | bar-odd channel of the complex volume |

*Processes* are not sectors: a [fusion process](#def:fusion-process) is a strand-balanced rearrangement inside the strong sector, while β-decay moves proton number on the subject side and is thereby routed to the weak sector. The bar-even and bar-odd channels are intertwined by the bar involution itself — the rotation between the two channel recurrences of [the binding–$Q_\beta$ complex volume conjecture](#conj:binding-qbeta-complex-volume) — so the taxonomy's parity column is a statement about where each sector's observable lives, not a wall between algebras.

The Lean formalization records the taxonomy as a total assignment and proves that weak is the unique bar-odd-assigned sector, that strong is the unique bar-even one, and that the electromagnetic parity assignment is exactly the open one; no electromagnetic bar parity is asserted anywhere in the corpus and none is introduced here.
