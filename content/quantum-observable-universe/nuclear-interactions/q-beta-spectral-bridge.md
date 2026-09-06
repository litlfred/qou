**Proposition (conditional on Borromean quark conjecture — $\mathfrak{Q}_\beta$ spectral bridge).**

*Let $\mathcal{B}_n$ be the canonical free-neutron braid word with single wrap $A = 1$. Let $q = q_0$ be the substrate parameter and $h := q - q^{-1}$. We define the Markov–Jones parameter as:*
$$
  z \;:=\; \frac{q^{3}}{q^{2}+1} \;=\; \frac{q^{2}}{[2]_q}.
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

> **Migrated C → D, 2026-09-05** (`qou-i229` → `qou-cds1`, owner-approved:
> *"refresh and migrate"*). The definition above read
> $z := 1/(\sqrt q + 1/\sqrt q) = 0.4993\ldots$ — convention **C** of the
> [trace-convention registry](../../../docs/coordination/trace-convention-registry.md),
> marked there *EXCISED 2026-08-09*
> ([reconciliation](#rem:markov-z-reconciliation)). It is now
> $z = q^3/(q^2+1) = 0.6127\ldots$, convention **D**, which the registry records
> as this channel's **definitional** convention per the owner ruling of
> 2026-08-15 (*"convention D is convention. excise convention C"*), with C
> **structurally excluded** — in D the loop values satisfy $z\,z_- = 1/[2]_q^2$
> and the framing ratio is the monomial $a = q^2$, while C admits no such
> factorisation.
>
> **The table was migrated from the producer, not by hand.** Every value in
> [the data table](#tbl:q-beta-spectral-bridge-table-data) now comes from
> `q-beta-spectral-bridge.witness.json`, which has computed $q^3/(q^2+1)$ all
> along — the divergence measured here on 2026-09-05 was 21 % between a C-frame
> table and a D-frame producer, with both witness assertions passing because a
> producer checking itself against itself cannot see that it has drifted from the
> block it names.
>
> **The anchor moved too, and that is also executed rather than decided.** The
> table was on muon pin A; the producer is on the **proton** pin, migrated
> 2026-08-29 under `qou-cds3` with the authorisation recorded there — AGENTS.md
> §"q₀ anchor convention", *"we want proton unless for an explicit reason … fix
> all, even if not visible"*. So both axes were already ruled and the block
> simply had not followed.
>
> **What moved.** $\mathfrak{Q}_\beta^{\mathrm{A}}$ is essentially unchanged at
> $0.7836$ MeV, but $\mathfrak{Q}_\beta^{\mathrm{B}}$ moves $0.8324 \to 0.8234$
> MeV and the A/B disagreement **improves** from $0.0487$ to $0.0398$ MeV against
> the same $h^2 E_0 = 0.183$ MeV bound. The bridge ratio moves $1.898 \to 1.566$,
> which is the $1/z$ term following the convention.
>
> Analysis: [`docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md`](../../../docs/audits/2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md).

