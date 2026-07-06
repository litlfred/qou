**Definition of CP violation.**
CP symmetry combines charge conjugation C (swapping particles with antiparticles) and parity P (mirroring spatial coordinates). Under exact CP symmetry, matter and antimatter would behave as perfect mirror images. **CP violation** occurs when processes distinguish matter from antimatter fundamentally.

**Experimental evidence.**

CP violation is established in three systems:

1. **Neutral kaons** (1964). Cronin and Fitch observed the long-lived kaon $K_L$ decaying to two pions: $K_L \to \pi^+\pi^-$ at a rate of $\sim 2 \times 10^{-3}$ \cite{christenson1964}. CP symmetry dictates decay to three pions only. This was the first evidence of CP violation.
2. **$B$ mesons** (2001). The BaBar \cite{aubert2001} and Belle experiments measured CP-violating asymmetries in $B^0 \to J/\psi\, K_S$ decays. This confirmed the Kobayashi-Maskawa mechanism: the CKM quark-mixing matrix contains an irreducible complex phase $\delta_{\mathrm{CKM}}$.
3. **$D$ mesons** (2019). LHCb observed CP violation in charm decays ($D^0 \to K^+K^-$ versus $D^0 \to \pi^+\pi^-$) at the $10^{-4}$ level.

**The matter-antimatter asymmetry.**

Sakharov (1967) identified three necessary conditions for the universe's baryon asymmetry:
1. Baryon number violation.
2. C and CP violation.
3. Departure from thermal equilibrium.

The Standard Model CKM phase satisfies the second condition but remains quantitatively insufficient to explain the observed ratio $n_B / n_\gamma \sim 6 \times 10^{-10}$. Additional sources of CP violation are necessary.

**QOU interpretation.**

Under the [complex chirality rotation](#conj:complex-chirality-rotation) framework, CP violation originates from a residual phase $\theta$ of the complex substrate parameter $q = |q|e^{i\theta}$:

- The observable sector projects $\theta \to 0$, but a small residual phase $\theta_{\mathrm{res}}$ may survive an imperfect projection.
- The CP-violating discriminant scales as $\delta_{\mathrm{CP}} \sim \mathcal{O}(\theta_{\mathrm{res}}^2)$ for single-crossing systems like the electron-positron pair.
- For **multi-crossing composites** such as kaons (quark-antiquark pairs with multiple internal crossings), the phase accumulates linearly: $\delta_{\mathrm{CP}} \sim n_c\theta_{\mathrm{res}}$, where $n_c$ is the total crossing number of the hadronic braid word.
- This gives a **geometric origin** for the CKM phase. It represents the total accumulated crossing phase from the complex-$q$ sector, projected onto the observable quark-mixing matrix.

**Quantitative gap.**

The [crossing energy decomposition](#prop:crossing-energy-decomposition) yields an electromagnetic-to-strong ratio of $\tanh(\ln q) \approx 0.104$. If the residual phase scales similarly — $\theta_{\mathrm{res}} \sim \tanh(\ln q) \cdot \alpha_{\mathrm{EM}}$ — then $\delta_{\mathrm{CP}} \sim 10^{-3}$. This magnitude correctly aligns with kaon CP violation but falls short of explaining baryogenesis. The required enhancement likely emerges from the **cosmological regime**, where the observability constraint itself breaks down.
