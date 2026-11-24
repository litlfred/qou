# Section 2 Slide Deck & Storyboard: The Rules of the Game & the Three Calibrations

**Companion to:** [Survey Article §2](../survey-article.md#2-the-rules-of-the-game-model-versus-measurement-and-the-three-calibrations) | [Suite Index](../README.md)  
**Target Runtime:** ~7 minutes 00 seconds (7 slides)  
**Visual Style Palette:** Split-screen epistemic boundary (`#0F172A` model side in cool sapphire `#38BDF8`, `#18181B` measurement side in lab emerald `#10B981`); ideal hyperbolic tetrahedra in translucent glass teal (`#2DD4BF`) with golden dihedral arcs (`#FBBF24`); discrepancy/tension markers in vivid crimson (`#F43F5E`).

---

## Slide 2.1 — The Numerology Trap (And How to Escape It)

### On-Screen Text & Formula
- **Title:** How Not to Fool Yourself
- **Forbidden Moves (`STRICT`):**
  - Tuning continuous exponents or coefficients
  - Shopping a knot census for a near-match
  - Picking cutoffs or branches against experimental data

### Host Narration (Word-for-Word)
"Whenever someone claims to connect pure mathematics to famous numbers like one over one-thirty-seven or the muon mass, your skepticism meter should shoot straight into the red. Give any clever human—or worse, a modern computer search—enough exponentials, pi's, and knot tables, and you can curve-fit the phone book to eight decimal places. Worse yet, a fitted model is scientifically useless when you're trying to discover physics: the moment you tune a knob to hide an error, you erase the exact clue that would have shown you where your algebra was wrong. So the Quantum Observable Universe project enforces a ruthless rule across every line of code: zero curve-fitting."

### Visual & Animation Storyboard
- **0:00–0:20 (The Curve-Fitting Trap):** Animate a jagged polynomial curve wriggling through five green data points as four glowing red sliders (`c₁, c₂, K_cutoff, knot_id`) auto-tune themselves; when a sixth data point appears on the right, the fitted polynomial shoots wildly off-screen. Stamp with a red `FITTED = UN-FALSIFIABLE` seal.
- **0:20–0:45 (The Zero-Fit Rule):** Sweep away all sliders. Show a rigid interlocking brass-and-crystal gear train driven by a single shaft ($q_0$): every output dial turns deterministically. Where one dial misses a green target mark, a bright crimson diagnostic arrow points directly at the gear tooth responsible (`Diagnostic Signal Preserved`).

---

## Slide 2.2 — Model Terms vs. Physical Comparison

### On-Screen Text & Formula
- **Title:** Where Mathematics Ends and Physics Begins
- **Left (`Mathematical Model`):** Defined objects (`photon`, `electron`, `proton`, $F_{\mathrm{Bor}}(q)$)
- **Right (`Empirical Boundary`):** CODATA 2022 · PDG 2024 · AME2020

### Host Narration (Word-for-Word)
"Rule number one keeps our language honest. Inside the QOU monograph, words like 'photon,' 'electron,' 'proton,' and 'binding energy' are names of mathematical constructions inside a braided algebra—just as a topologist calls a three-crossing knot 'the trefoil' without claiming it grows in a clover field. Everything upstream of experiment is pure mathematics, judged by formal Lean proofs. Physics enters *only* at the comparison boundary, where a dimensionless ratio computed by the model is set right next to CODATA, Particle Data Group, or Atomic Mass Evaluation measurements. At that boundary, 'it's just a model name' is never an excuse for a wrong number."

### Visual & Animation Storyboard
- **0:00–0:25 (The Glass Comparison Wall):** Divide the screen down the center with a luminous vertical glass plane labeled `THE COMPARISON BOUNDARY`.
  - **Left hemisphere (Sapphire):** Floating 3D braid words ($\sigma_0\sigma_1\sigma_0$, $(\sigma_0\sigma_1^{-1})^3$) and Lean 4 theorem badges (`0 sorry`), outputting pure dimensionless decimal streams.
  - **Right hemisphere (Emerald):** Penning-trap cyclotron, LHC detector cross-section, and nuclear mass spectrometer tables (`CODATA 2022`, `PDG 2024`, `AME2020`).
- **0:25–0:48 (Comparison Spark):** Two dimensionless numbers meet right on the glass plane—producing either a green `ppb / % residual` readout or a stark crimson discrepancy bar.

---

## Slide 2.3 — Exactly Three Calibrations (`CAL-1`, `CAL-2`, `CAL-3`)

### On-Screen Text & Formula
- **Title:** The Only Three Empirical Pins (`dim H¹ = 2 + 1 = 3`)
- **Table:**
  - **`CAL-1` ($m_e$):** Sets the $\mathrm{MeV}$ energy unit ($0.51099895\;\mathrm{MeV}$)
  - **`CAL-2` ($\mathcal{D}_\beta \leftrightarrow q_0$):** Sets substrate deformation $q_0$ (pinned via $m_p / m_e$)
  - **`CAL-3` ($\mathcal{D}_\pi \leftrightarrow m_\pi$):** Sets orthogonal meson length ($r_\pi \approx 1.414\;\mathrm{fm}$)

### Host Narration (Word-for-Word)
"If curve-fitting is banned, how many measured numbers *are* allowed to connect dimensionless algebra to human laboratory units like mega-electronvolts and femtometers? Exactly three—matching the three real cohomological degrees of freedom of Bring's genus-four surface. Calibration one is the electron mass m-e, which simply defines our mega-electronvolt ruler; because m-e sets the unit by fiat, the model scores dimensionless ratios and bindings, never claiming the proton's absolute mass in MeV as an independent prediction. Calibration two is the weak beta-decay scale, which fixes our dimensionless parameter q-naught—pinned most precisely from the proton-to-electron mass ratio. And calibration three is the orthogonal pion scale—which even drops out completely on self-consistent electromagnetic hadron splittings!"

### Visual & Animation Storyboard
- **0:00–0:25 (Cohomology Alignment):** Show a translucent 4-holed surface ($\Sigma_{\mathrm{Bring}}$) at top center; highlight three independent non-contractible cycle vectors ($2$ golden cycles on the primary $W$-plane + $1$ teal orthogonal meson cycle) projecting downward into three locked hardware input sockets labeled `CAL-1`, `CAL-2`, `CAL-3`.
- **0:25–0:50 (Unit-Ruler Callout):** Zoom on `CAL-1`: show a dimensionless rod of length `1836.15267...` being stamped with an `× m_e (MeV)` ruler; cross out `"Prediction: m_p = 938.27 MeV"` and replace with `"Scored: Dimensionless Ratios, Splittings & Bindings"`.

---

## Slide 2.4 — Hyperbolic Geometry of the Figure-Eight Knot ($4_1$)

### On-Screen Text & Formula
- **Title:** Equation (2): The Simplest Hyperbolic Knot & the Muon Ratio
- **Key Formula:**

$$
\frac{m_\mu}{m_e} = \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}, \qquad \hbar_q := 1 - q^{-1}, \qquad \mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2\!\left(\frac{\pi}{3}\right) \approx 2.0298832
$$

### Host Narration (Word-for-Word)
"To see how topology produces mass ratios, meet the simplest hyperbolic knot in all of three-dimensional geometry: the four-crossing figure-eight knot, four-sub-one. In the late nineteen-seventies, William Thurston showed that if you drill the figure-eight knot out of three-dimensional space, the surrounding complement naturally curves into constant negative hyperbolic geometry, glued cleanly out of *two* regular ideal tetrahedra with sixty-degree dihedral angles. Each tetrahedron has volume Clausen-two of pi over three—about 1.01494—giving a total hyperbolic volume of 2.0298832. Divide that exact geometric volume by the square of the categorical quantum, h-bar-sub-q equals one minus one-over-q, and you get the model's muon-to-electron mass ratio."

### Visual & Animation Storyboard
- **0:00–0:22 (3D Knot-Complement Triangulation):** Rotate a glowing 3D figure-eight knot ($4_1$, four alternating crossings). Invert space around the knot tube so two shimmering teal ideal hyperbolic tetrahedra (vertices stretched to infinity on the Poincaré ball boundary, concave hyperbolic faces, $60^\circ = \pi/3$ golden dihedral arcs) snap together along their faces.
- **0:22–0:48 (Volume Integration Readout):** Each tetrahedron pulses with `Cl₂(π/3) = 1.0149416...`; the pair merges into `Vol(4₁) = 2·Cl₂(π/3) = 2.0298832128...`, then divides visually by a square grid tile of side $\hbar_q = 1 - q^{-1}$.

---

## Slide 2.5 — Equation (3): Pinning $q_0$ on the Borromean Proton

### On-Screen Text & Formula
- **Title:** How $q_0$ Is Pinned (`m_p / m_e` Is an Input Pin, NOT an Output!)
- **Key Formula:**

$$
\frac{m_p}{m_e} = 2\,\frac{\mathrm{Vol}(4_1)}{\hbar_{q_0}^2}\,|\mathrm{tr}_M(\beta_{\mathrm{Bor}})|\,\frac{[3]_{q_0}!}{q_0^3} - 12 \quad \Longrightarrow \quad q_0 = 1.1099785827513808\dots
$$

### Host Narration (Word-for-Word)
"Now watch closely, because honesty about what is an input versus an output is everything here. On three strands, the proton's core is the six-crossing Borromean braid, beta-Borromean. Equation three relates the proton-to-electron mass ratio to twice the figure-eight scale times the closed Markov trace of the Borromean braid and the three-strand antisymmetric Schur factor, minus twelve. Notice two critical facts: first, we *feed in* the measured CODATA proton-to-electron ratio—1836.1526734—to solve this equation numerically for q-naught, pinning q-naught at 1.10997858275... So m-p over m-e is our input pin, never a prediction! Second, the monograph explicitly flags that selecting the one-over-q-cubed Schur normalizer here is currently asserted rather than derived from first axioms."

### Visual & Animation Storyboard
- **0:00–0:25 (Newton Root-Finder Lock):** Display CODATA `m_p / m_e = 1836.152673426` flowing *into* the left side of Equation (3) with a bright blue `INPUT PIN (CAL-2)` tag. Plot the smooth monotonic curve of the right-hand side versus $q$; zoom 14 orders of magnitude into the intersection until the crosshair locks onto `q₀ = 1.1099785827513808...` (80-dps `mpmath` ticker scrolling off to the right).
- **0:25–0:48 (Epistemic Callout Tag):** Highlight the factor `[3]_q! / q³` in amber with a clean `Asserted Schur Normalizer (k = -3; Derivation Open)` tag so the viewer sees the exact ledger discipline.

---

## Slide 2.6 — First Real Test: The $211\;\mathrm{ppb}$ Muon–Proton Tension

### On-Screen Text & Formula
- **Title:** Plugging Proton $q_0$ Into the Muon Formula
- **Comparison:**
  - **QOU Model (at proton $q_0$):** $m_\mu / m_e = 206.7683264$
  - **CODATA 2022 Experiment:** $m_\mu / m_e = 206.7682827(46)$
  - **Residual:** **$+211\;\mathrm{ppb}$** ($\approx 9.5\sigma$ tension; $\Delta q_0 \approx 11.5\;\mathrm{ppb}$)

### Host Narration (Word-for-Word)
"Now comes our very first genuine, zero-free-parameter test. Take that exact proton-pinned number—q-naught equals 1.10997858275—and plug it straight into Equation two for the muon-to-electron mass ratio, touching nothing. Out pops 206.7683264. Compare that to the experimental CODATA value: 206.7682827. With zero tuned constants, pure hyperbolic knot volume and the proton pin hit the muon mass to *two hundred and eleven parts per billion*—two hundredths of athousandth of one percent! And yet, because physicists have measured the muon to twenty-two parts per billion, two hundred and eleven parts per billion is a *nine-point-five sigma* miss!"

### Visual & Animation Storyboard
- **0:00–0:22 (Macroscopic Zoom):** Show a number line from `0` to `250`: the QOU prediction needle and the CODATA needle land visually on top of one another at `206.77` (`99.999979% match`).
- **0:22–0:50 (Microscope $10^7\times$ Zoom):** Magnify the point `206.76828...` by ten million times! Now the green CODATA $1\sigma$ error bar (`±0.0000046`) separates cleanly from the sapphire QOU marker (`206.7683264`), spanning `9.5σ` (`+211 ppb`) in crimson. Show the corresponding tiny split between `q₀(proton) = 1.109978583...` and `q₀(muon) = 1.109978596...` (`11.5 ppb`).

---

## Slide 2.7 — Why Stripping a Fit Beats Hiding a $9.5\sigma$ Gap

### On-Screen Text & Formula
- **Title:** Discipline in Action: Retiring False Precision
- **History Lesson (`constants.py`):**
  - Rounded integer polynomial `(1+46u⁴)(1+4u⁵)(1−29u⁶)` erased the gap $\longrightarrow$ **Audited & Stripped (Fit!)**
  - Raw $211\;\mathrm{ppb}$ tension kept live $\longrightarrow$ Drives W6 Joint Lepton–Hadron QED Resolvent

### Host Narration (Word-for-Word)
"Here is a behind-the-scenes story from the repository that tells you everything about how this project works. At one stage, a multiplicative correction polynomial with integer coefficients—forty-six, four, and minus twenty-nine—appeared to wipe out that 211-part-per-billion gap completely. Then an internal audit recomputed the true coefficient to high precision, found 46.0319, realized the rounded integers were a disguised curve-fit against the target, and stripped the polynomial out of the codebase the same day. Why? Because that exposed 211-part-per-billion tension between the muon and proton pins reappears in the fine-structure constant too—pointing directly toward a real, uncomputed radiative loop effect rather than a swept-under-the-rug fudge factor."

### Visual & Animation Storyboard
- **0:00–0:22 (Audit Rejection Animation):** Display the polynomial `(1 + 46 u⁴)(1 + 4 u⁵)(1 - 29 u⁶)` bridging the `11.5 ppb` gap; an audit magnifying glass reveals `46.0000 ≠ 46.0319`, stamps `RETROSPECTIVE FIT — EXCISED`, and lifts the bridge clean out, restoring the honest `211 ppb` crimson indicator.
- **0:22–0:45 (Bridge to Section 3):** Show three glowing braided loops—a 4-term photon, a Hopf-link electron, and a Borromean proton—orbiting Bring's genus-4 surface, setting up Section 3.
