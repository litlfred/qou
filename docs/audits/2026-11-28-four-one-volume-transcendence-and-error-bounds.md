# Where Hyperbolic Knot Volume Transcendentals Enter: $4_1$ Steinberg Torsion, $2$–$3$ Pachner Error Bounds, Formal/Surreal-Jet Transcendence, and the Weight-2 Liouville–Apéry Wall (`2026-11-28`)

**Epic:** `qou-s028`
**Branch:** `claude/four-one-volume-pachner-error-and-jet-transcendence-20261128`
**Lean Module:** [`QOU/BraidsAndKnots/FigureEightPachnerAndJetTranscendence.lean`](../../folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/FigureEightPachnerAndJetTranscendence.lean) (`0 sorry`, standard axioms only, `0` `[Field]`/`field_simp` binders, `0` `QOU/Transcendental/` taint)
**Cross-Linked Existing QOU Modules:**
- `QOU/MassTheory/NahmBlochBridge.lean` (`nahmClass_mem_blochGroup`, `fig8Class_eq_nahmClass`, `delta_gen_three_ne_zero`)
- `QOU/MassTheory/BlochRigidity/Algebra.lean` & `QOU/Transcendental/MassTheory/BlochRigidity/Rigidity.lean` (`eq_mul_of_fiveTerm`)
- `QOU/Core/LawvereCut.lean` (`CutEvaluation`, `Coev`, `AdicCut.stage_sub_mem`)
- `QOU/Core/TarskiSignKashaev.lean` (`kashaevFigureEight_five`, `signPrefix_five`)
- `QOU/MassTheory/SurrealGradingPrune.lean` (`no_separation_of_standard`, `grade_blind_to_rationality`) & `QOU/MassTheory/TowerHeightAttack.lean`
**Probe & Witness (`95` compute dps / `80` output dps, `q0Anchor = "proton"`, `probe-float64-guard --strict` clean):**
- [`computations/probes/four_one_volume_transcendence_error_bounds_probe.py`](../../computations/probes/four_one_volume_transcendence_error_bounds_probe.py)
- [`computations/probes/four-one-volume-transcendence-error-bounds-probe.witness.json`](../../computations/probes/four-one-volume-transcendence-error-bounds-probe.witness.json) (`5/5` assertions PASS)

---

## 1. Direct Answer to the Architectural Question

**Question:** *Where do transcendentals from hyperbolic knot volumes actually enter in QOU's triangulation pipeline, what algebraic constraint forces a transcendental out of error bounds, and what can (and cannot) be proved for $4_1$ by algebraic error-bound / surreal-jet methods?*

The triangulation pipeline separates cleanly into **four stages**, and the transition from pure algebra to period transcendence happens at an exact, machine-locatable boundary:

1. **Stage 1 — Ideal Triangulation & Steinberg/Bloch Torsion (`100% Algebraic`, Degree 2 for $4_1$):**
   The Neumann–Zagier gluing equations of $4_1$ (`m004`, two regular ideal tetrahedra) force $z_0 = z_1 = \omega$ with $\omega^2 - \omega + 1 = 0$ ($\omega \in \overline{\mathbb{Q}}$ of degree $2$, $|\omega| = |1 - \omega| = 1$, $1 - \omega = \omega^{-1}$, $\omega^6 = 1$). Over **any** commutative ring $R$ (`fourOne_steinberg_torsion`), the multiplicative Steinberg wedge $\omega \wedge (1 - \omega)$ is **2-torsion and 6-torsion** ($2 \cdot (\omega \wedge (1 - \omega)) = 0$). No transcendental number exists anywhere in the triangulation shapes, the $A$-polynomial, the Habiro cyclotomic ring $\widehat{\mathbb{Z}[q]}$ (`AdicCut.stage_sub_mem`), the 1-loop adjoint Reidemeister torsion (`(2\tau_{\mathrm{DG},\mu})^2 = -3`, `AdjointTorsionSaddlePrefactors.lean`), or the Kashaev root-of-unity evaluations $J_N(4_1; e^{2\pi i/N}) \in \mathbb{Z}[2\cos(2\pi/N)]$ (`TarskiSignKashaev.lean`).
2. **Stage 2 — $2$–$3$ Pachner Pentagon Invariance Forces an Infinite Non-Polynomial / Non-Algebraic Jet (`Proved in Lean, 0 sorry`):**
   Why cannot a knot volume functional invariant under $2$–$3$ Pachner moves be an algebraic polynomial or rational function of the tetrahedron shapes?
   - **Boundary Pole-Residue Obstruction (`pachner_pentagon_no_polynomial_jet`):** Clearing denominators $x^N (1 - y)^N$ in the 5-term Bloch–Wigner $2$–$3$ Pachner equation for any degree-$N$ polynomial jet $P(z) = \sum_{k=0}^N c_k z^k$ ($N \ge 1$) yields at $y = 1$ the exact `[CommRing]` identity
     $$\mathcal{P}_N(P; x, 1) = c_N (x^N - 1)(1 - x)^N.$$
     At $x = 2$, $\mathcal{P}_N(P; 2, 1) = c_N (2^N - 1)(-1)^N \neq 0$ whenever $c_N \neq 0$: **every finite-birthday / polynomial truncation has strictly non-zero $2$–$3$ Pachner error**.
   - **All-$M$ Rational Truncation Error Bounds (`dilogTrunc_duplication_two_sided_bounds`):** For $L_N(z) = \sum_{k=1}^N z^k / k^2$, parity cancellation leaves an exact strictly positive tail $\Delta_{\mathrm{dup}}(2M, z) = \sum_{k=M+1}^{2M} z^{2k}/k^2$ bracketed for all $M \ge 1$ and $0 < z^2 \le 1$ by
     $$\frac{z^{2(M+1)}}{(M+1)^2} \le \Delta_{\mathrm{dup}}(2M, z) \le \frac{M \, z^{2(M+1)}}{(M+1)^2}.$$
     On the interior Abel 5-term point $(x, y) = (1/2, 1/3)$, exact rational arithmetic confirms $\Delta_5(N) \neq 0$ for all $1 \le N \le 60$ ($\Delta_5(1) = -1/75$, $\Delta_5(2) = -7/1250$), with $2^N (N+1)^2 |\Delta_5(N)| \to 1$ ($0.96941174\dots$ at $N = 60$).
3. **Stage 3 — Surreal / Formal-Jet Resolution (`Proved Transcendence Degree 2 over ℚ[z] in Lean, 0 sorry`):**
   - **What fails on collapsed reals:** `QOU/MassTheory/SurrealGradingPrune.lean` (`no_separation_of_standard`, `grade_blind_to_rationality`) already proved that once Archimedean `Coev` collapses a jet to a standard real in $\mathbb{R}$, Conway–Gonshor `ord_ω` grade-squeezing is constant on $\mathbb{R}_{>0}$ and **cannot** decide rationality or transcendence.
   - **What succeeds BEFORE collapsing the jet parameter $z$:** Keeping the deformation / surreal-jet indeterminate $z$ alive in `PowerSeries ℚ` ($\mathbb{Q}[[z]]$, matching `TowerHeightAttack`'s formal $\hbar$-lift prior to `Coev`), the formal dilogarithm jet $L_2(z) = \sum_{k=1}^\infty z^k / k^2$ satisfies the exact Fuchsian operator equation $(1 - z)\theta^2 L_2 = z$ ($\theta = z\partial_z$, `dilogSeries_fuchsian_ode`). Using **two coupled division-free Wronskian descents** — an $(X - 1)$-multiplicity descent at $X = 1$ for $L_1 = -\ln(1-X)$ (`no_polynomial_wronskian_one_sub_X`) and an $X$-multiplicity descent at $X = 0$ on $(\mathbb{Q}[T])[X]$ for $L_2 = \mathrm{Li}_2(X)$ (`no_bivariate_wronskian_dilog`) — `FigureEightPachnerAndJetTranscendence.lean` proves **unconditionally (`0 sorry`)**:
     - `logSeries_transcendental`: $L_1(z)$ is transcendental of all degrees over $\mathbb{Q}[z]$;
     - `logSeries_dilogSeries_alg_independent`: $(L_1(z), L_2(z))$ are **algebraically independent** over $\mathbb{Q}[z]$ (transcendence degree $2$);
     - `dilogSeries_transcendental`: **for every degree $m \ge 1$, no non-zero polynomial $\Phi(Y) \in (\mathbb{Q}[z])[Y]$ vanishes at $Y = \mathrm{Li}_2(z)$**.
   Together with Bloch–Wigner rigidity (`BlochRigidity/Rigidity.lean`, `eq_mul_of_fiveTerm`: every continuous measurable solution of the $2$–$3$ Pachner 5-term + inversion relations is $c \cdot D(z)$), $2$–$3$ Pachner invariance uniquely forces a transcendental formal jet!
4. **Stage 4 — Specializing $z \mapsto \omega = e^{i\pi/3}$ Hits the Open Weight-2 Kontsevich–Zagier Period Wall (`Measured to 80 dps`):**
   Does formal-jet transcendence of $\mathrm{Li}_2(z)$ over $\mathbb{Q}(z)$ imply that the **specialized real number**
   $$\mathrm{Vol}(4_1) = 2 D(\omega) = 2\,\mathrm{Cl}_2\!\left(\frac{\pi}{3}\right) = \frac{3\sqrt{3}}{2} L(2, \chi_{-3}) = 2.02988321281930725004\dots$$
   is transcendental over $\mathbb{Q}$? **NO — that remains a famous open problem in mathematics** (`kontsevich-zagier2001` §1–2, `zagier-dilogarithm` §I.2 & §II.3)! Even irrationality of $\mathrm{Vol}(4_1)$ (and of Catalan's constant $G = \tfrac{1}{2}\mathrm{Vol}(\text{Whitehead})$) is open! Part D of the Lean module (`liouville_eval_rat_lower_bound`: $|P_{\mathbb{Q}}(p/q)| \ge q^{-d}$ whenever $P(p/q) \neq 0$) together with the 95-dps probe pinpoints **exact arithmetic why**:
   - **Real vs Imaginary Split at the 6-Torsion Point $\omega = e^{i\pi/3}$:**
     $$\mathrm{Li}_2(e^{i\pi/3}) = \underbrace{\frac{\pi^2}{36}}_{\text{Re: transcendental (Lindemann)}} + i\,\underbrace{\mathrm{Cl}_2\!\left(\frac{\pi}{3}\right)}_{\text{Im: }\frac{1}{2}\mathrm{Vol}(4_1)\text{ (OPEN!)}}.$$
     The real part collapses by the distribution relation to $\tfrac{1}{6}\zeta(2) = \pi^2/36$ (transcendental because $\pi$ is a weight-1 period via $e^{i\pi} = -1$), whereas the imaginary part cancels all $\pi^2$ terms and isolates the pure odd Dirichlet $L$-value $\tfrac{3\sqrt{3}}{4} L(2, \chi_{-3})$.
   - **Why Weight-1 Padé/Legendre Succeeds While Weight-2 Mod-3 Hits the $\mathrm{lcm}^2$ Wall:**
     - *Weight 1 ($\ln 2$, or $\mathrm{Im}(-\ln(1-\omega)) = \pi/3$):* Legendre kernel $P_n(x)$ produces rational approximants with denominator dividing $d_n = \mathrm{lcm}(1,\dots,n)^1 \sim e^{n}$, while the integral decays as $(\sqrt{2}-1)^{2n} = e^{-1.762747\dots n}$. Net exponent:
       $$2\ln(\sqrt{2}-1) + 1 = -0.76274717403908605047\dots < 0 \quad (\text{beats Liouville bound; at } n=12,\; d_{12}|a_{12}\ln 2 - b_{12}| = 3.11658\times 10^{-6} < 1).$$
     - *Weight 2 Untwisted ($\zeta(2) = \pi^2/6$, `beukers1979`):* Squaring denominators raises the cost to $\mathrm{lcm}(1,\dots,n)^2 \sim e^{2n}$, which already defeats 1D Legendre ($-1.7627 + 2 = +0.2373 > 0$); Beukers's 2D kernel rescues $\zeta(2)$ barely via $5\ln(\tfrac{\sqrt{5}-1}{2}) + 2 = -0.40605912529801723749\dots < 0$ (irrationality only, not degree-$d$ transcendence!).
     - *Weight 2 Conductor-3 ($\mathrm{Vol}(4_1) = \tfrac{3\sqrt{3}}{2} L(2, \chi_{-3})$):* Arithmetic progressions $3k+1, 3k+2$ force denominators dividing $\mathrm{lcm}(1,\dots,3n)^2 \sim e^{6n}$, shifting the exponent to
       $$5\ln\!\left(\frac{\sqrt{5}-1}{2}\right) + 6 = +3.59394087470198276251\dots > 0 \quad (\text{exponential blow-up; at } n=12,\; q_{12}|L(2,\chi_{-3}) - p_{12}/q_{12}| \approx 7.3457\times 10^{21} \gg 1).$$
   - **Why Kashaev Root-of-Unity Approximants Also Miss Liouville/Mahler Bounds:**
     For $J_N(4_1; e^{2\pi i/N}) \in \mathbb{Z}[2\cos(2\pi/N)]$ (`alg_degree` $= \varphi(N)/2$; e.g. $J_5(4_1) = 46 + 2\sqrt{5}$ exact to $1.2\times 10^{-94}$), the Andersen–Hansen 1-loop saddle expansion gives
     $$\frac{2\pi}{N}\ln J_N(4_1) - \mathrm{Vol}(4_1) = \frac{2\pi}{N}\left(\frac{3}{2}\ln N - \frac{1}{4}\ln 3\right) + O(N^{-2}),$$
     so the approximation error decays **logarithmically/algebraically** as $O(\ln(N)/N)$ ($0.828285\dots$ at $N=40$), whereas the logarithmic Weil height grows **linearly** ($h(J_N) \sim c N$, reaching $h(J_{40}) = 10.50037\dots$ at degree $8$). Liouville/Schmidt/Nesterenko algebraic-approximation theorems require error $\ll \exp(-\kappa \, d_N \, h_N) \sim \exp(-c' N \varphi(N))$, failing by an exponential gap (`O(\ln N / N)` vs $\exp(-c' N \varphi(N))$).

---

## 2. Summary of Proved Lean 4 Theorems (`FigureEightPachnerAndJetTranscendence.lean`)

| Declaration | Base / Carrier | What It Proves (`0 sorry`) |
|---|---|---|
| `fourOne_sixth_root_identities` | `[CommRing R]` | $\omega(1-\omega) = 1$, $\omega^3 = -1$, $\omega^6 = 1$, $\omega^2(1-\omega)^2 = 1$ from $\omega^2 - \omega + 1 = 0$ |
| `fourOne_steinberg_torsion` | `[CommRing R]`, `[AddCommGroup M]` | $2 \cdot (\omega \wedge (1-\omega)) = 0$ and $6 \cdot (\omega \wedge (1-\omega)) = 0$ for any bimultiplicative skew wedge |
| `clearedPachnerPentagon_eval_one` | `[CommRing R]` | Universal pole-residue identity $\mathcal{P}_N(P; x, 1) = c_N (x^N - 1)(1 - x)^N$ for all $N \ge 1$ |
| `pachner_pentagon_no_polynomial_jet` | `Polynomial ℚ` | No non-constant polynomial jet (`1 ≤ P.natDegree`) satisfies the $2$–$3$ Pachner 5-term relation |
| `dilogTrunc_duplication_tail` | `ℚ` | Exact parity-cancellation tail $\Delta_{\mathrm{dup}}(2M, z) = \sum_{k=M+1}^{2M} (z^2)^k / k^2$ |
| `dilogTrunc_duplication_two_sided_bounds` | `ℚ` | All-$M$ two-sided rational bounds $\frac{z^{2(M+1)}}{(M+1)^2} \le \Delta_{\mathrm{dup}}(2M, z) \le \frac{M z^{2(M+1)}}{(M+1)^2}$ |
| `abelFiveTermDefectHalfThird_one_and_two` | `ℚ` | Interior Abel 5-term defect at $(1/2, 1/3)$ equals $-1/75$ at $N=1$ and is non-zero at $N=2$ |
| `dilogSeries_fuchsian_ode` | `PowerSeries ℚ` | Exact Fuchsian jet equation $(1 - X)\,\theta(\theta(\mathrm{Li}_2(X))) = X$ |
| `no_polynomial_wronskian_one_sub_X` | `Polynomial ℚ` | Division-free $(X-1)$-multiplicity infinite descent blocking rational antiderivatives of $(1-X)^{-1}$ |
| `logSeries_transcendental` | `PowerSeries ℚ` | All-degree transcendence of $-\ln(1-X)$ over $\mathbb{Q}[X]$ |
| `no_bivariate_wronskian_dilog` | `(ℚ[T])[X]` | Division-free $X = 0$ infinite descent blocking rational-in-$(X, -\ln(1-X))$ solutions for $\mathrm{Li}_2(X)$ |
| `logSeries_dilogSeries_alg_independent` | `PowerSeries ℚ` | Algebraic independence of $(-\ln(1-X), \mathrm{Li}_2(X))$ over $\mathbb{Q}[X]$ (transcendence degree $2$) |
| `dilogSeries_transcendental` | `PowerSeries ℚ` | **Main Jet Theorem:** $\mathrm{Li}_2(X) = \sum_{k \ge 1} X^k / k^2$ is transcendental of **all degrees** over $\mathbb{Q}[X]$ |
| `dilogSeries_not_rational` / `dilogSeries_not_quadratic` | `PowerSeries ℚ` | Explicit degree-$1$ and degree-$2$ non-algebraicity corollaries |
| `liouville_eval_rat_lower_bound` | `ℤ`, `ℚ` | Division-free homogenized integrality & rational root-separation bound $|P_{\mathbb{Q}}(p/q)| \ge q^{-d}$ |

---

## 3. Verified 80-dps Numerical Ledger (`q0Anchor = "proton"`)

From [`four-one-volume-transcendence-error-bounds-probe.witness.json`](../../computations/probes/four-one-volume-transcendence-error-bounds-probe.witness.json) (`WORK_DPS = 95`, `OUT_DPS = 80`, zero `float64`, zero muon-pin values per `2026-11-28` owner ruling):

- **Proton-pinned deformation parameter:**
  - $q_0^{(p)} = 1.1099785827513808075916690956107688798744991218735787360728142401817989635744830$
  - $\hbar_{q_0} = \ln q_0^{(p)} = 0.10434072031951951231590627997307239705374428082898430325086225895200129757583535$
- **Figure-eight hyperbolic volume & proton-scale ratio (zero fitting):**
  - $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) = 2.0298832128193072500424051085490405718833786150605995840349782135531949525164880$
  - $L(2, \chi_{-3}) = \tfrac{2}{3\sqrt{3}}\mathrm{Vol}(4_1) = 0.78130241289648629686718742962409235636513433654528542022210006296688698465161822$
  - $\mathrm{Vol}(4_1) / \hbar_{q_0}^2 = 186.45043066397743847711694553076814719789797366397553525568808696359390535051239$ (recorded purely as a derived proton-pin ratio; note the CAL-2 muon-calibration identification $\mathrm{Vol}(4_1)/\hbar_q^2 \leftrightarrow m_\mu/m_e$ is held under the `2026-11-28` proton-pin ruling).

---

## 4. Newly Ingested & Upgraded Period / Dilogarithm References

Verified against Crossref REST API (`2026-11-28Z`), registered in `folio/schema/references.ts`, synced to `references.bib`, and attested in `test/attestations/bib-verification/reference/`:

1. `kontsevich-zagier2001` — Maxim Kontsevich & Don Zagier (2001), *Periods*, in *Mathematics Unlimited — 2001 and Beyond*, Springer, 771–808, DOI `10.1007/978-3-642-56478-9_39`.
2. `zagier-dilogarithm` (**upgraded**) — Don Zagier (2007), *The Dilogarithm Function*, in *Frontiers in Number Theory, Physics, and Geometry II*, Springer, 3–65, DOI `10.1007/978-3-540-30308-4_1`.
3. `nahm2007` — Werner Nahm (2007), *Conformal Field Theory and Torsion Elements of the Bloch Group*, in *Frontiers in Number Theory, Physics, and Geometry II*, Springer, 67–132, DOI `10.1007/978-3-540-30308-4_2` (also resolves 3 `lean-ref` sites in `NahmBlochBridge.lean` and `TwistKnotNahm.lean`).
4. `dupont-sah1982` — Johan L. Dupont & Chih-Han Sah (1982), *Scissors congruences, II*, *J. Pure Appl. Algebra* **25**(2), 159–195, DOI `10.1016/0022-4049(82)90035-4`.
5. `apery1979` — Roger Apéry (1979), *Irrationalité de $\zeta(2)$ et $\zeta(3)$*, *Astérisque* **61**, 11–13, SMF (`NUMDAM AST_1979__61__11_0`).
6. `beukers1979` — Frits Beukers (1979), *A Note on the Irrationality of $\zeta(2)$ and $\zeta(3)$*, *Bull. London Math. Soc.* **11**(3), 268–272, DOI `10.1112/blms/11.3.268`.
7. `rivoal2000` — Tanguy Rivoal (2000), *La fonction zêta de Riemann prend une infinité de valeurs irrationnelles aux entiers impairs*, *C. R. Acad. Sci. Paris Sér. I Math.* **331**(4), 267–270, DOI `10.1016/S0764-4442(00)01624-4`.
8. `nesterenko1996` — Yuri V. Nesterenko (1996), *Modular functions and transcendence questions*, *Sb. Math.* **187**(9), 1319–1348, DOI `10.1070/SM1996v187n09ABEH000158`.
