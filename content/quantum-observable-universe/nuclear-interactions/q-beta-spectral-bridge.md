**Proposition (conditional on Borromean quark conjecture — $\mathfrak{Q}_\beta$ spectral bridge).**

*Let $\mathcal{B}_n$ be the canonical free-neutron braid word with single wrap $A = 1$. Let $q = q_0$ be the substrate parameter and $h := q - q^{-1}$. We define the Markov–Jones parameter as:*
$$
  z \;:=\; \frac{1}{\sqrt q + 1/\sqrt q}.
$$
*Write $E_0 := m_e/(q(q-1))$ for the single-tick energy scale. Let:*
$$
  \mathfrak{Q}_\beta^{\mathrm{A}} \;:=\;
  \lvert \Delta(\mathrm{net}) \rvert \cdot E_0
  \qquad
  \mathfrak{Q}_\beta^{\mathrm{B}} \;:=\;
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}} \cdot \frac{E_0}{z}
$$
*denote the closed-form $Q$-value in the normal form counit basis and the transfer-matrix eigenfunction basis, respectively. Both forms are finite-depth truncations of the same spectral decomposition. They agree as:*
$$
  \frac{\mathfrak{Q}_\beta^{\mathrm{A}}}{\mathfrak{Q}_\beta^{\mathrm{B}}}
  \;=\;
  1 \;+\; \frac{(z-1)\,h}{2} \;+\; O(h^2),
$$
*with bridge identity:*
$$
  \mathfrak{Q}_\beta^{\mathrm{A}}
  \;=\;
  \ln\!\frac{V_{\mathrm{pp}}}{V_{\mathrm{nn}}} \cdot \frac{E_0}{z}
  \cdot \Bigl(1 + \tfrac{(z-1)\,h}{2} + O(h^2)\Bigr).
$$
*The remainder at depth $N$ in the brane-tower truncation decays exponentially.*

> **⚠ The `z` defined above is convention C, which is excised** (labelled
> 2026-09-05, `qou-i229`). $z := 1/(\sqrt q + 1/\sqrt q) = 0.4993\ldots$ is
> convention **C** of the
> [trace-convention registry](../../../docs/coordination/trace-convention-registry.md),
> there marked *EXCISED 2026-08-09*
> ([reconciliation](#rem:markov-z-reconciliation)). For the `qbeta-decay`
> channel the registry records the **definitional** convention as **D**,
> $z_{\mathrm{D}} = q^3/(q^2+1) = 0.6127\ldots$, per the owner ruling of
> 2026-08-15 (*"convention D is convention. excise convention C"*), with C
> **structurally excluded** — in D the loop values satisfy
> $z\,z_- = 1/[2]_q^2$ and the framing ratio is the monomial $a = q^2$, while C
> admits no such factorisation.
>
> **Not migrated here.** The channel's migration is scoped and tracked as
> `qou-cds1`; this block is one of its members, and moving it alone would leave
> the channel half-migrated. Labelled rather than recomputed, the same move
> `df13e845cee` made for the $q_0$ pins. The consequence is visible: the
> $\mathfrak{Q}_\beta$ figures shift by $\sim 0.05$ MeV between conventions.
> Analysis: [`docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md`](../../../docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md).

