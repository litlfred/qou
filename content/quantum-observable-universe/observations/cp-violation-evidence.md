**What is CP violation?**
CP symmetry is the combined operation of charge conjugation C
(swap particle $\leftrightarrow$ antiparticle) and parity P
(mirror spatial coordinates).  If physics were CP-symmetric,
matter and antimatter would behave as exact mirror images.
**CP violation** means this symmetry is broken: certain processes
distinguish matter from antimatter at a fundamental level.

**Experimental evidence.**

CP violation is firmly established in three systems:

1. **Neutral kaons** (1964).  Cronin and Fitch observed that the
   long-lived kaon $K_L$ (which should decay only to three pions
   under CP symmetry) occasionally decays to two pions:
   $K_L \to \pi^+\pi^-$ at rate $\sim 2 \times 10^{-3}$
   \cite{christenson1964}.  This was the first evidence that CP
   is not an exact symmetry.

2. **$B$ mesons** (2001).  The BaBar \cite{aubert2001} and Belle
   experiments measured CP-violating asymmetries in
   $B^0 \to J/\psiK_S$ decays, confirming the
   Kobayashi--Maskawa mechanism: the CKM quark-mixing matrix
   contains an irreducible complex phase $\delta_{\mathrm{CKM}}$
   that cannot be removed by field redefinitions.

3. **$D$ mesons** (2019).  LHCb observed CP violation in
   charm decays ($D^0 \to K^+K^-$ vs $D^0 \to \pi^+\pi^-$)
   at the $10^{-4}$ level.

**The matter--antimatter asymmetry.**

Sakharov (1967) showed that three conditions are necessary for the
observed baryon asymmetry of the universe:
(i) baryon number violation,
(ii) C and CP violation,
(iii) departure from thermal equilibrium.
The Standard Model CKM phase provides (ii) but is quantitatively
too small by several orders of magnitude to explain the observed
ratio $n_B / n_\gamma \sim 6 \times 10^{-10}$.  Additional
sources of CP violation are needed.

**QOU interpretation.**

In the [complex chirality rotation](#conj:complex-chirality-rotation)
framework, CP violation arises from a residual phase $\theta$ of
the complex substrate parameter $q = |q|e^{i\theta}$:

- The observable sector projects $\theta \to 0$, but this projection
  may be imperfect — a small residual $\theta_{\mathrm{res}}$ could
  survive.
- The CP-violating discriminant is
  $\delta_{\mathrm{CP}} \sim \mathcal{O}(\theta_{\mathrm{res}}^2)$
  for single-crossing systems (electron/positron).
- For **multi-crossing composites** (kaons: quark--antiquark with
  multiple internal crossings), the phase accumulates:
  $\delta_{\mathrm{CP}} \sim n_c\theta_{\mathrm{res}}$, where
  $n_c$ is the total crossing number of the hadronic braid word.
- This provides a **geometric origin** for the CKM phase: it is
  the total accumulated crossing phase from the complex-$q$ sector,
  projected onto the observable quark-mixing matrix.

**Quantitative gap.**
The [crossing energy decomposition](#prop:crossing-energy-decomposition)
gives the electromagnetic/strong ratio $\tanh(\ln q) \approx 0.104$.
If the residual phase scales similarly —
$\theta_{\mathrm{res}} \sim \tanh(\ln q) \cdot \alpha_{\mathrm{EM}}$
— then $\delta_{\mathrm{CP}} \sim 10^{-3}$, which is the right
order of magnitude for kaon CP violation but still too small
for baryogenesis.  The missing enhancement may come from the
**cosmological regime** where the observability constraint itself
weakens.
