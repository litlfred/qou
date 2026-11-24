# Quantum Observable Universe: A *PBS Space Time*-Style Survey & Narrated Visual Storyboard Suite

> **Work-in-Progress Status & License:** This survey accompanies the open formal-mathematics monograph *Quantum Observable Universe* ([`litlfred/qou`](https://github.com/litlfred/qou)), released under **CC BY 4.0**. Many algebraic and topological theorems in the monograph are machine-checked in Lean 4 (`0 sorry`), several physical identifications remain conditional on stated conjectures, and multiple empirical comparisons still miss experiment by large margins. Every claim below separates **mathematical constructions inside the model** from **comparisons with physical measurement**.

---

## 1. Purpose & Audience

What happens if you throw away the background stage of three-dimensional space and flowing time, keep only Gottfried Wilhelm Leibniz's relational rules for how observations compose side by side and one after another, and deform classical permutation symmetry by a single real number $q_0 > 1$?

This folder presents a self-contained **12-page (~6,800-word) accessible survey article** paired one-to-one with **nine narrated slide decks and visual storyboards** (~68 slides total). Written in the conceptual, geometry-first, hype-free spirit of *PBS Space Time* (curious, science-literate viewers who appreciate real equations when every symbol is explained in plain English, and who want honest answers about where a theoretical model succeeds and where it breaks), the suite walks from pre-geometric braid strands up through particle physics, nuclear stability chambers, and chemical stoichiometry.

---

## 2. Two Non-Negotiable Rules of the Game

Every page of [`survey-article.md`](survey-article.md) and every narrated slide in [`slides/`](slides/) enforces two foundational disciplines of the repository:

1. **Model vs. Measurement Boundary:** Inside the Quantum Observable Universe (QOU) formalism, words such as *photon*, *electron*, *proton*, *neutron*, *mass*, and *binding energy* name defined algebraic and topological objects in a braided monoidal category, just as a topologist names a three-crossing knot *the trefoil*. Physics enters strictly at the comparison boundary, where dimensionless ratios computed from the algebra are set side by side against experimental tables (**CODATA 2022**, **PDG 2024**, and **AME2020**).
2. **Zero Curve-Fitting (`NO FITTING EXCEPT CAL-1/2/3`):** Apart from **three calibration inputs** aligning with the three cohomological degrees of freedom of Bring's genus-$4$ surface—the electron mass unit $m_e$ (`CAL-1`), the weak decay scale $\mathcal{D}_\beta$ whose dimensionless substrate parameter $q_0 = 1.1099785827513808\dots$ is pinned from the proton-to-electron mass ratio $m_p / m_e$ (`CAL-2`, making $m_p/m_e$ an **input pin**, never an output prediction), and the orthogonal pion scale $\mathcal{D}_\pi / m_\pi$ (`CAL-3`, which drops out altogether on self-consistent Route-1 electromagnetic hadron splittings)—no continuous or discrete parameter is tuned to match data. Where a parameter-free calculation misses experiment by $211\;\mathrm{ppb}$ or by $69\%$, the miss is left in plain view so the mathematics can be diagnosed rather than patched.

---

## 3. Contents & Master Map

### Primary Survey Monograph

- **[`survey-article.md`](survey-article.md)** — Complete 9-section accessible survey (~6,800 words, 11 display equations with plain-English symbol guides, carrying both the live monograph cover-status accuracy table from `sec:authors-note-status` and the November 2026 formal/80-dps multi-scale ledger).

### Per-Section Narrated Slide Decks & Visual Storyboards (`slides/`)

Every section of [`survey-article.md`](survey-article.md) has a dedicated companion deck containing **(a)** minimal on-screen titles and equations, **(b)** full word-for-word host narration written for spoken cadence, and **(c)** frame-by-frame 2D/3D/Manim visual and camera storyboards:

| Sec. | Survey Section | Companion Slide Deck | Slides | Key Formula(s) | Signature Visual / Animation Motif |
|:----:|:---------------|:---------------------|:------:|:--------------:|:-----------------------------------|
| **1** | [Space, Time, and Indiscernibles](survey-article.md#1-space-time-and-indiscernibles-replacing-the-background-stage) | [`slides/section-01-relational-space-and-hecke-algebra.md`](slides/section-01-relational-space-and-hecke-algebra.md) | 7 | Eq. (1): Hecke skein $\sigma_i - \sigma_i^{-1} = (q - q^{-1})\,\mathbf{1}$ | Dissolving Newton's 3D coordinate grid into braided world-strands, GNS trace-radical quotienting to $TL_n(q)$, and Nakayama twist loops |
| **2** | [The Rules of the Game & the Three Calibrations](survey-article.md#2-the-rules-of-the-game-model-versus-measurement-and-the-three-calibrations) | [`slides/section-02-rules-of-the-game-and-three-calibrations.md`](slides/section-02-rules-of-the-game-and-three-calibrations.md) | 7 | Eqs. (2)–(3): $\mathrm{Vol}(4_1)/\hbar_q^2$ & Borromean proton pin $q_0$ | Two ideal hyperbolic tetrahedra gluing into the figure-eight knot $4_1$ complement; pinning $q_0$ on $m_p/m_e$ vs. the $211\;\mathrm{ppb}$ $\mu\text{–}p$ tension |
| **3** | [Knots, Photons, and Bring's Genus-4 Surface](survey-article.md#3-knots-photons-and-brings-genus-4-surface) | [`slides/section-03-knots-photons-and-brings-surface.md`](slides/section-03-knots-photons-and-brings-surface.md) | 8 | Eq. (4): Chiral photon $\gamma(\varphi)$ & Borromean $V^3 = \gamma_+\gamma_-$ | 4-term photon braid with chiral vertex $\sigma_0\sigma_1^{-1}$, $\gamma\gamma$ pair production into Hopf-link electrons and Borromean baryons, and Bring's $S_5$ surface |
| **4** | [The Fine-Structure Constant and the Electroweak Architecture](survey-article.md#4-the-fine-structure-constant-and-the-electroweak-architecture) | [`slides/section-04-fine-structure-and-electroweak.md`](slides/section-04-fine-structure-and-electroweak.md) | 8 | Eqs. (5)–(6): $[n]_q$ & Bring–Schwinger $\alpha_{\mathrm{EM}}^{-1}$ fixed point | Torus knots $T(2,9)$ and $T(3,5)$ wrapping a genus-$4$ surface, $2\ln t = -\alpha_{\mathrm{EM}}$, $\sin^2\theta_W^0 = 3/8$ RG flow, and Higgs $125.23\;\mathrm{GeV}$ radial potential |
| **5** | [Ghost Particles on an Unknot: Neutrinos and Mixing](survey-article.md#5-ghost-particles-on-an-unknot-sweedlers-algebra-neutrinos-and-generations) | [`slides/section-05-neutrinos-sweedler-and-generations.md`](slides/section-05-neutrinos-sweedler-and-generations.md) | 7 | Eq. (7): Sweedler $k=12$ lift $m_e(q_0^2-1)^{12}$ & $\sin^2\theta_{13}$ | Unknot $0_1$ gaining $12.5\text{–}17.6\;\mathrm{meV}$ mass via 12 nilpotent Sweedler hops, $\mathbb{Z}$ vs. $\mathbb{Z}/2$ framing, and Bring $S_4$ branching $4 = 3 \oplus 1$ |
| **6** | [Inside the Nucleon and Beta Decay](survey-article.md#6-inside-the-nucleon-and-beta-decay-how-honest-failures-drive-discovery) | [`slides/section-06-nucleons-and-beta-decay.md`](slides/section-06-nucleons-and-beta-decay.md) | 7 | Eq. (8): Signed log $Q_\beta$ & Route-1 $p\text{–}n$ EM splitting | 9-strand left-coupled $\gamma\gamma + V^3$ chiral crossing $\sigma_5^{-1}$ (`C2_neg`), spectator cancellation ($0.33 \to 0.764\;\mathrm{MeV}$), and $m_\pi$-free Borromean Coulomb energy |
| **7** | [Building Atomic Nuclei: Chambers, the Hoyle State, and Alpha Tunneling](survey-article.md#7-building-atomic-nuclei-hidden-colour-toric-chambers-the-hoyle-state-and-alpha-tunneling) | [`slides/section-07-nuclear-chambers-hoyle-and-alpha-decay.md`](slides/section-07-nuclear-chambers-hoyle-and-alpha-decay.md) | 8 | Eq. (9): $\mathcal{C}_{\mathrm{phys}}$ facets & ${}^{210}\mathrm{Po}$ preformation $1/20$ | 6q–12q hidden-colour reconnection, the 73-chamber Gröbner fan zooming into $\mathcal{C}_{\mathrm{phys}}$ (${}^5\mathrm{He}$ drip + Hoyle $3\alpha \to {}^{12}\mathrm{C}$), and ${}^{210}\mathrm{Po}$ WKB barrier |
| **8** | [The Five-Layer Confinement Tower, Chemistry, and Horizons](survey-article.md#8-the-five-layer-confinement-tower-from-strands-to-chemistry-and-horizons) | [`slides/section-08-five-layer-confinement-tower-and-chemistry.md`](slides/section-08-five-layer-confinement-tower-and-chemistry.md) | 8 | Eqs. (10)–(11): Adiabatic ratio $\eta_k < 1$ & horizon pole $Z_1(s_\star)=1$ | Five-floor algebraic RG elevator ($\eta_2 = 1.8 \times 10^{-6}$ locking nuclei in chemistry), neutron-star $\eta_2 \to 1$ flip, and black-hole jet horizons |
| **9** | [The Honest Scoreboard and How to Break the Model](survey-article.md#9-the-honest-scoreboard-where-the-math-hits-where-it-fails-and-how-to-break-it) | [`slides/section-09-the-honest-scoreboard-and-open-frontiers.md`](slides/section-09-the-honest-scoreboard-and-open-frontiers.md) | 8 | Full Scoreboard Tables 1–3 (no new equations) | Split-screen precision bullseyes vs. glaring red open gaps (${}^4\mathrm{He}$ Wigner $\mathrm{SU}(4)$, $m_\tau$, $N_{\mathrm{gen}}=3$, $a_0$), plus Lean 4 + 80-dps verification pipeline |

---

## 4. Production Notes & Format Roadmap (`qou-w478` / `qou-kdmr`)

To keep the repository lightweight, diffable, and free of binary merge conflicts, all slide decks in [`slides/`](slides/) are authored in structured GitHub-Flavored Markdown with explicit `[SLIDE]`, `[ON-SCREEN]`, `[HOST NARRATION]`, and `[VISUAL & ANIMATION STORYBOARD]` blocks. Downstream production teams can compile this source along three independent tracks without modifying the mathematical text:

- **Visual Rendering Track:** Direct translation of the `[VISUAL & ANIMATION STORYBOARD]` specifications into **Manim Community** Python scenes (for 2D/3D braid isotopes, Gröbner fan cones, and RG plots), **Blender** geometry nodes (for hyperbolic ideal tetrahedra and Bring's genus-$4$ surface), or **Reveal.js / PowerPoint (`.pptx`)** lecture decks.
- **Audio Track:** Word-for-word human host recording (~55–65 minutes across all nine episodes at 145 words/minute, or a single condensed 25-minute flagship video from Sections 1–4 and 7–9), with optional text-to-speech animatic timing tests during storyboarding.
- **Verification Provenance:** Every numerical figure cited in the prose and narration is traceable to 80-decimal-place `mpmath` witnesses (`computations/**/*.witness.json`, zero `float64`) and Lean 4.24.0 modules (`folio/quantum-observable-universe/lean/QOU/`).
