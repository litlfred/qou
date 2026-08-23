# Precision goals — what "1 ppQ" means in QOU

> Canonical reference for all agents (Claude, Copilot, Gemini, future
> collaborators) working on QOU mass-prediction precision.
>
> Per user direction (2026-05-18, updated 2026-05-26): the framework's
> headline precision goal has **two independent legs**, not one.
>
> **Precision target upgrade (2026-05-26).** L1 compute precision
> target upgraded from **1 ppb** (10⁻⁹) to **1 ppQ** (1 part per
> quadrillion, 10⁻¹⁵). Rationale: at 50 dps / 40 dps output, the
> compute truncation is ~10⁻³⁴ ppb — the 1 ppb target was trivially
> met and no longer discriminating. The Q_β precision ladder (N=5)
> already produces formula residuals at ~10⁻¹⁰, approaching territory
> where the 1 ppb L1 floor is noise. "1 ppQ" = "1 part per
> quadrillion" (10⁻¹⁵ relative, 10⁻⁶ ppb). The "Q" is fitting —
> everything in this paper is q.

## TL;DR

> **🛑 Absolute mass EXCISED (owner ruling 2026-08-11, bean `qou-exam`).** The
> framework no longer claims/targets/scores **absolute** nucleon or atomic mass
> in MeV (m_p, m_n, m_⁴He). Absolute mass = `m_e · (dimensionless ratio)`, and
> m_e (CAL-1) sets the MeV scale *by fiat* — so the only content is the ratio;
> reporting m_p in MeV double-counts the calibration. The L2 scorecard below is
> therefore reframed to the **dimensionless / differential** predictions only
> (`m_μ/m_e`, `m_K/m_π`, `Q_β`, `Δ_pn`, `B(K)`); the absolute `m_p`/`m_n` rows —
> perpetual ~400× misses that were only ever met by fitting — are **removed, not
> carried**. No proved result or compute is deleted; the MeV numbers remain
> derivable as `m_e × ratio`, they are simply no longer a claim. Full ruling:
> [`audits/2026-08-11-excise-absolute-mass-notion.md`](audits/2026-08-11-excise-absolute-mass-notion.md).
> The "N/7 meet" figures below are retained for historical continuity but are
> **superseded** by the reframed (absolute-mass-free) scorecard.

| Leg | Target | Status |
|-----|--------|--------|
| **L1. Compute precision** | internal cross-method agreement ≤ 1 ppQ (10⁻¹⁵) on every observable at substrate q_0 | **CERTIFIED (2026-07-13) — 6/6 production atoms** (p, n, D, T, ³He, ⁴He). `cross_check_trM_1ppb.py` reports `allPassed=True` (`all_atoms_within_1ppQ`, `character_engine_matches_closed_form`); worst closed-form χ-anchor \|Δ\| = **5.6e-50** (proton 9.3e-50, neutron 3.3e-50), no float64 in the hot path. The last gap (⁴He, H₁₂) closed by building `pyhecke-native` from source. See [`audits/2026-07-13-l1-4he-certification-complete.md`](audits/2026-07-13-l1-4he-certification-complete.md). **Supersedes** the 2026-06-17 gap ([`audits/2026-06-17-l1-1ppq-certification-gap.md`](audits/2026-06-17-l1-1ppq-certification-gap.md)): the float64-limited `markov_peel` witness and the Habiro-divergence were replaced by the mpf / native-Rust path. *(The aggregate `onepb-status-dashboard.witness.json`, dated 2026-07-06, is stale and predates this certification.)* |
| **L2. Per-observable accuracy** | for each predicted observable O with experimental uncertainty σ_O: `σ_pred(O) ≤ σ_O / 100` (i.e. **100× more precise than experimental**) | **1/5 scoreable meet** — **`m_K/m_π` alone**, the only genuine prediction to meet. (Corrected 2026-08-18: this read "2/7 meet — one calibration anchor (m_e) + m_K/m_π". `m_e` is the CAL-1 **input** that fixes the MeV unit — error *defined* zero, not measured — so it is not scoreable, on the same grounds the dashboard already excludes `m_p`. Quote `beats_100x_scoreable`/`scoreable_total`.) `m_K/m_π` meets (closed via the meson EM correction `(3q²−1)/(2q²)`, PR #1442 — **caveat RESOLVED 2026-08-09, owner directive; LANDED IN CODE 2026-08-22, PR #5467 — for 13 days this ruling lived only in this sentence, and every producer, the dashboard, the tracker and the content block kept shipping the truncation** — the EM factor is now the **full series** `1 + log(1+ℏ_q)`, not the two-term truncation `(3q²−1)/(2q²)`. The truncation scored better (46.80 vs 102.86 ppb on the ratio², i.e. 23.40 vs 51.43 ppb on the ratio) but was not converging on anything: 3 terms gives 107.00 ppb and 4 terms 102.53 ppb, so the series converges to ~102.9 and the 2-term stop lands closer only because under-counting the EM term partially cancels the model's own positive residual. A truncation chosen because it matches is a fit. **It still MEETS L2**: σ_exp(m_K/m_π) = 26364.6 ppb ⇒ target 263.6 ppb, and the full series sits at 51.43 ppb — 5.13× margin (was 11.27×). So the caveat is retired at no cost to the scorecard, and `qou-v6oz`'s question ("why is `(3q²−1)/(2q²)` the physical object?") is **dissolved rather than answered** — it is not the physical object, it was where the series happened to be stopped; the `[3]_q[4]_q` core (99.98 %) is exact/Lean-proved and α_em is derived, so the ratio itself is parameter-free); the other 5 **miss** (m_p ~437×, m_μ ~964×, m_n ~416×, Q_β ~160×, Δ_pn ~159×). The de-fitted honest state — m_p dropped from "meet" 2026-07-04 when the fitted Habiro tower (that landed it on CODATA) was removed; live source `per-observable-100x-status.witness.json` (`beats_100x_scoreable=1`, `scoreable_total=5`; the legacy `beats_100x_count=2` counts the two calibration inputs and is not an accuracy result). |

Both legs apply. Hitting L1 alone is not sufficient; hitting L2 alone is not
the framework's working precision discipline.

## The 1 ppQ target is on the *theory residual* (2026-05-29 reframe)

> Per owner direction (2026-05-29): the headline "1 ppQ on predictions
> from CAL-1/2/3" is a target on the **framework's own theory residual**,
> not on the absolute prediction error. This resolves an earlier
> mis-framing ("1 ppQ on a prediction is unreachable because q₀ is only
> known to 0.06 ppb"). The two error sources are separate and must not
> be conflated.

**Error decomposition.** Every prediction `O` carries two independent
error terms:

```
σ_total(O)  =  σ_theory(O, N)   ⊕   σ_CAL(O)
              └ framework's own  └ propagated experimental error of the
                formula residual   CAL-1/2/3 inputs (m_e, q₀←m_p, m_π)
                at derivation
                order N
```

| Term | Owner | Improves by | Current scale |
|------|-------|-------------|---------------|
| **σ_theory(O, N)** — the formula's own residual at brane-tower / derivation order `N` | **us** (derivation) | adding *proved* higher-order terms | m_p: 242 ppb (μ-p floor); m_avg: 2.89 % bare → 819 ppm spectral |
| **σ_CAL(O)** — propagated CAL experimental error | external labs | CODATA / PDG re-measurement | q₀: **0.06 ppb** (CODATA m_p); m_e: 0.29 ppb; m_π: ~30 ppb |

**The 1 ppQ goal = drive `σ_theory(O, N) ≤ 1 ppQ`**, so every prediction
is **CAL-limited, not theory-limited**. Once there, `σ_total ≈ σ_CAL`,
and the prediction sharpens automatically as the three calibration
measurements improve — no framework change required.

### Accepted: q₀ is known to 0.06 ppb (CODATA-limited, not a framework ceiling)

q₀ is pinned from the CODATA m_p/m_e ratio (0.06 ppb, the most precise
available — see [`substrate-anchor-alternatives.md`](../content/quantum-observable-universe/observations/substrate-anchor-alternatives.md)).
Its 0.06 ppb uncertainty is **inherited from that one measurement**, and
**improves one-for-one as CODATA improves m_p/m_e**. It is *not* a limit
of the framework. (If the QOU substrate picture is correct, the highest
leverage experimental program is tightening the three CALs — m_e, the
neutron β-decay sector behind q₀, and m_π — since every QOU prediction
then sharpens at once.) The framework's job is to make `σ_theory` small
enough that this external `σ_CAL` is the only thing left.

### Infra requirement: true arbitrary precision end-to-end (no float64)

To *certify* `σ_theory ≤ 1 ppQ` (10⁻¹⁵), the compute stack must resolve
residuals well below 1 ppQ, which **forbids any float64 in the hot path**
— float64 carries only ~16 significant digits (machine ε ≈ 2.2×10⁻¹⁶),
so a cross-method agreement that bottoms out at ~10⁻¹⁶ is *measuring
float noise*, not certifying precision. Rules:

1. **No `float(...)` / numpy `float64` / `complex128` in any value that
   feeds a witnessed quantity.** Use `mpmath.mpf` (or exact `sympy`
   rationals) throughout. Audit: `compute-integration-watcher` I8.
2. **dps headroom.** `_precision.COMPUTE_DPS_DEFAULT = 50` gives ~35
   digits of headroom below 1 ppQ — adequate. Raise via
   `QOU_COMPUTE_DPS=<n>` when bounding higher-order residuals.
3. **The L1 cross-method gate must be tightened 1 ppb → 1 ppQ** once all
   methods are float-clean. As of 2026-05-29, `cross_check_trM_1ppb.py`
   still gates at 1 ppb because the `markov_peel` *fast path* computes in
   float64 (`cf, df = float(c), float(d)`; `h_num = float(_h_num)`) and
   only agrees with the true-mpf methods (Hoefsmit, chi-cache, Habiro)
   to ~2.7×10⁻¹⁶. Fix = route peel through the exact `use_fast=False`
   sympy path (or an mpf path), then drop the gate to 1 ppQ.

### Bounding `σ_theory` vs derivation order N

We must be able to say *"order N\* achieves ≤ 1 ppQ"* before committing
compute. Two distinct "orders" exist — do not conflate them:

| Order | What it indexes | Residual behaviour |
|-------|-----------------|--------------------|
| **Habiro order M** (Markov-trace expansion `Σ a_m u^{2m}`) | the *trace* tr_M | **terminates** at M=8 (proton/neutron): finite integer-`a_m` sum ⇒ trace residual is **0**, compute-limited only |
| **Brane-tower / shell order N** (the observable formula around the trace) | the *formula shell* (e.g. `2·Vol/ℏ²·F − 12`) | **open** — this is where `σ_theory` lives |

The trace is already exact (terminating Habiro sum), so 1 ppQ on the
trace is purely a compute-precision question (met at 50 dps). The open
work is the **shell**: tabulate `σ_theory(O, N)` as each *proved*
correction order is added and project the convergence rate to find N\*.
Empirical anchor so far (m_avg, no fitting): bare Family-A shell = +2.89 %
→ first spectral correction = 819 ppm (~35× per derived order). If that
rate held, ~9 proved correction orders would reach 1 ppQ — a *projection*
to be validated, not a result. Harness:
`per_observable_100x_status.py` should grow an `N`-sweep column
(`σ_theory` vs shell order) once the second derived correction lands.

> **Discipline note.** "Adding a higher-order term" means a **proved**
> categorical term (e.g. the next Habiro `a_m`, or a derived shell
> correction), **never** a CODATA-fitted tower. Fitting below the current
> `σ_theory` models the μ-p tension as signal — see
> [`audits/2026-05-28-mu-p-tension-substrate-floor.md`](audits/2026-05-28-mu-p-tension-substrate-floor.md).
> The μ-p 240 ppb is the floor of the *current low-order shell*; it is
> *derivable-below* (lower N residual), but *not fittable-below*.

## L1 — compute precision (default 1 ppQ)

**Definition.** Different methods computing the same quantity at substrate
q_0 must agree to at least 1 ppQ (10⁻¹⁵ relative, i.e. 10⁻⁶ ppb).

**Configuration.** Controlled by `computations/substrate/_precision.py`:

```python
COMPUTE_DPS_DEFAULT  = 65    # mpmath working precision (OUTPUT + GUARD)
OUTPUT_DPS_DEFAULT   = 50    # serialization precision
PRECISION_GUARD      = 15    # COMPUTE = OUTPUT + GUARD
```

The **1 ppQ target is the *minimum*** — raise via `QOU_COMPUTE_DPS=<n>`
environment override. At 50 dps output / 65 dps compute, serialization
truncation is ~10⁻⁵⁰ absolute (10⁻⁴¹ ppb), far exceeding 1 ppQ.

**Q_β is already at 0 ppQ (exact).** The Habiro expansion of the Markov
trace terminates at $M = 8$ for the proton/neutron (integer coefficients
$a_m \in \mathbb{Z}[u]$, evaluated at $u_0 = \sqrt{q_0}$). No
truncation error exists — the formula is a finite sum. See
[`prop:habiro-precision-ladder-equivalence`](../content/quantum-observable-universe/braids-and-knots/habiro-precision-ladder-equivalence.md).

> **Historical note (superseded).** The "precision ladder" (c_k
> coefficients at each "rung" N=3, N=4, N=5) was the Taylor expansion
> of this exact Habiro sum in powers of $\hbar_q^2$. It was useful when
> the closed form was unknown; now that the Habiro identification is
> established, the c_k are a compute artefact with no independent
> mathematical role. The per-rung table below is retained for historical
> reference only.

**Where measured.** `onepb-status-dashboard.witness.json`:

- Layer 1 (LP-dual / GB NF): 6/6 compounds, gap = 0
- Layer 2 (Markov-trace cross-method): 8 atoms, max_rel_delta = 0.0
- Layer 3 (Structural / AME publication rounding floor): 92.79 ppb max
  non-anchor Δ — this is the **measurement** floor, not a compute floor

**Audit rule.** Any new compute script MUST `from _precision import
set_compute_dps, fmt` and call `set_compute_dps()` before `mpmath`
operations. `compute-integration-watcher` I8 audit flags float64 leaks.

## L2 — per-observable accuracy (100× experimental)

**Definition.** For each predicted observable O, the *prediction error*
`|O_pred − O_exp| / |O_exp|` must be at most `σ_exp(O) / |O_exp| / 100`.

This is **variable per observable**. Most observables have very tight
σ_exp (CODATA 2022 absolute masses at sub-ppb), so most 100× targets
are in the ppt range. The single exception in the framework's L2 set
is the muon at σ_exp ≈ 22 ppb (100× target 0.22 ppb).

### Per-observable target table (CODATA 2022)

> **Anchor correction 2026-08-08.** The Q_β / m_n / Δ_pn rows previously read
> 1247 / 2.39 / 755 ppb. Those came from a `qbeta-ck-cache` built at the **muon**
> q₀ and consumed by a **proton**-pinned dashboard — a layer straddle worth
> 29.96 ppb on Q_β. The cache is now regenerated at the proton pin and the rows
> above are the layer-consistent values, which is why they now agree with the
> 1279 ppb / 164.0× figure already quoted in §"Key distinctions" below. No
> prediction improved or degraded; the numbers were mislabelled, not wrong.
> Detail: [`audits/2026-08-08-qbeta-l2-anchor-straddle-guard.md`](audits/2026-08-08-qbeta-l2-anchor-straddle-guard.md).

> **Table updated 2026-07-04 (m_p de-fitted; post q₀ re-pin #1422 +
> de-fitting #1416).** Only m_e meets trivially (scale anchor, err 0);
> **all five genuine predictions miss** the 100× target, and m_p — the
> CAL-2 *numerical* anchor — now also misses (~437×): its documented-pin
> round-trip is +1.35 ppb once the fitted Habiro tower is dropped (it had
> landed m_p on CODATA to 0.0004 ppb). m_K/m_π is the one prediction that
> meets. Earlier versions showed the *muon* pin (m_μ "meets, ratio-derived")
> and the *fitted* Q_β "5.7 ppb (N=5)" — both stale. Live source:
> `per-observable-100x-status.witness.json` (`beats_100x_count=2`).

| Observable | role | σ_exp_rel | **100× target** | Current pred error | Status |
|---|---|---:|---:|---:|---|
| m_e | CAL-1 anchor | 0.29 ppb | 2.9 ppt | 0 (anchor) | **anchor** ✓ |
| ~~m_p~~ (absolute) | ~~CAL-2 numerical anchor~~ | — | — | — | **EXCISED** (absolute mass, `qou-exam`; the ratio `m_p/m_e` remains the CAL-2 pin, a calibration *input*, not a scored prediction) |
| m_μ/m_e | prediction (ratio) | 21.8 ppb | **0.22 ppb** | 210 ppb | **misses ~964×** (9.5σ μ-p tension) — ratio, retained |
| Q_β | prediction (CAL-3 cross-check) | 0.78 ppm | **7.8 ppb** | 1279 ppb (1.28 ppm) | **misses ~164×** (de-fitted; N=5 ladder was a fit) — decay Q-value, retained |
| ~~m_n~~ (absolute) | ~~prediction (Path C)~~ | — | — | — | **EXCISED** (absolute mass, `qou-exam`; content lives in `Δ_pn` below + the m_e scale) |
| Δm_pn | prediction (Path C) | 474 ppb | **4.74 ppb** | 774 ppb | **misses ~163×** — splitting, retained |
| m_K/m_π | prediction (meson ratio) | 26.4 ppm | **264 ppb** | 23.4 ppb (post-#1442 closure via `(3q²−1)/(2q²)`) | **MET** (~11× margin below target) — ratio, retained |

**Honest summary: 1/5 SCOREABLE meet — `m_K/m_π` alone.** (Corrected
2026-08-18. This line previously read "2/7 'meet' — 1 calibration anchor
(m_e) plus m_K/m_π", which named the anchor and then counted it. `m_e` is
the CAL-1 input that fixes the MeV unit; its error is *defined* zero, not
measured, so it is not a prediction and does not belong in an accuracy
score — the same grounds on which the dashboard already excludes `m_p`.)
m_K/m_π (closed via the merged meson EM correction `(3q²−1)/(2q²)`
in PR #1442; was previously listed as missing by ~1098× pre-merge).
m_K/m_π is the first genuine prediction to meet the 100× target; the
other 5 (m_p, m_μ, Q_β, m_n, Δ_pn) still miss it.** (Was 3/7 through
2026-07-04, when the fitted m_p Habiro tower — which landed m_p on CODATA
to 0.0004 ppb — was dropped; the honest documented-pin round-trip is
+1.35 ppb, a ~437× miss.)
This is the de-fitted state: production reports the real residuals, not
CODATA-fitted towers. m_p's former "0.0004 ppb" was a calibration
round-trip *with* the fitted tower; de-fitted it is +1.35 ppb — still not
a framework prediction (it is the CAL-2 anchor round-trip), but no longer
sub-target. See [`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md`](audits/2026-07-04-c4-mu-p-tension-pin-dependence.md).

> **m_p is the numerical anchor (was a prediction pre-#1422).** Because
> q₀ is inverted from m_p/m_e, m_p matches CODATA nearly by construction —
> but only to +1.35 ppb: the *documented raw proton pin* (`Q_50_DIGIT_STR`)
> sits ~0.34 ppb off the exact base-formula solve, so the round-trip is
> +1.35 ppb, not 0 (the former 0.0004 ppb was the dropped fitted tower).
> The genuine baryon-mass test is the *bare* categorical value
> (Family-A Borromean tower, m_p = 965.38 MeV, +2.89% open gap) and the
> m_μ / m_n / Q_β predictions above.

> **Path C (2026-05-26).** `m_n = m_p + Q_β + m_e` bypasses the
> flavor-split X. With m_p the anchor and Q_β a 1.25 ppm prediction,
> m_n lands at ~1.04 ppb and Δ_pn at ~755 ppb — both now **miss** the
> 100× target (they previously "beat" it only via the fitted N=5 Q_β).

> **CAL-3 σ source.** Q_β experimental uncertainty here is the PDG 2024
> value Q_β(n) = 0.78233341(61) MeV (≈0.78 ppm, 779.7 ppb relative). The
> earlier 640 ppm draft was based on a coarser AME quote (0.78232 ± 0.00050
> MeV); that figure is **incorrect** at the precision we care about. See
> [`computations/cal-3-q-beta.witness.json`](../computations/cal-3-q-beta.witness.json).
>
> **Q_β Habiro-exact evaluation.** The Markov trace of the proton/neutron
> braid words lives in the Habiro ring $\widehat{\mathbb{Z}[q]}$ and
> terminates at $M = 8$ (integer coefficients $a_m \in \mathbb{Z}[u]$).
> Evaluating at $u_0 = \sqrt{q_0}$ gives the EXACT Q_β prediction at
> 5.744 ppb — below the 7.80 ppb target. No per-rung approximation
> needed. See [`prop:habiro-precision-ladder-equivalence`](../content/quantum-observable-universe/braids-and-knots/habiro-precision-ladder-equivalence.md).

For light-atom binding energies (B_D, B_T, B_³He, B_⁴He), the experimental
σ_B is dominated by the AME mass-table uncertainty (~10⁻⁶ for these atoms),
giving σ_rel(B) of order 0.04–0.45 ppm. **100× targets here are in the
0.35–4.5 ppb range — within reach post-Borromean-tower per-isotope extension.**

> **⚠ Δ_λ gate.** The per-isotope binding-energy formula is
> `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ(K)`. The per-partition **VALUE is now
> PROVED** (2026-08-02, sorry-free, general-n): `Δ_λ = (-1)^{n(λ)}·dim V_λ`
> (`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`, wired to
> `computations/delta-lambda-witness.json`). **What is still open is the
> many-body MAGNITUDE** — six closure ansätze (Frobenius co-Casimir,
> Demazure-fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented
> Markov) failed on the deuteron because they tried to force the magnitude
> `r* ≈ 1.585` into a per-block Δ_λ, which is structurally impossible (the
> missing term is a separate super-pairwise extensive object; pairwise cap
> `ρ_A ≤ C(A,2)` proved, `QOU.MassTheory.exchangeDet_pow_two_le_four`). See
> [`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md)
> and the closure-attempt history in
> [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](audits/2026-05-18-delta-lambda-gating-context.md).
> **L2 binding-energy targets remain presently unreachable** — not because
> of compute precision, and no longer because of the per-partition value,
> but because the super-pairwise extensive **magnitude** term is open R&D.
>
> **ℓ¹-ceiling sharpening (2026-08-07, `free_parameters = 0`).** The "magnitude
> is open" statement is now a *proved quantitative bound*, not an inference. The
> ℓ¹ norm `Σ_λ |y_λ χ^λ Δ_λ|` — the absolute ceiling reachable with **perfect
> constructive interference and zero cancellation** — is only `[0.36, 0.59]` of
> the AME target across **all four** atoms (D 0.516 · T 0.358 · ³He 0.592 ·
> ⁴He 0.406). So **no re-signing, no re-weighting, and no `Δ_λ` re-derivation
> can close the deficit** — the entire "find a better `Δ_λ`" family (where all
> six-plus prior ansätze lived) is foreclosed as scope-(a). A genuinely **new
> additive term is required**, and the ℓ¹ ceiling is the quantitative bar it
> must clear: it must supply **41–64 % of each target on its own**. The ≥3-body
> sector is the coherent one (`ℓ(λ)=3` cancellation ratio 0.98–1.00 at T/³He),
> and ⁴He's two-row sector is suppressed ~29,000× (a *strong, unproved*
> coincidence at the doubly-magic `[1⁴]` SU(4) singlet — not a proved selection
> rule). Current identified candidate for the new term: the He4-local ≥4-body
> cumulant `b₄ = −ln det(I + m·S)` (`eig(S) = {±√5, ±1}`), whose lone open scalar
> `m ∈ (0, 1/√5)` must be **derived forward**, not selected by AME (fit trap:
> no Σ(2,3,5) object is structurally forced below the ceiling). Full probe:
> [`docs/audits/2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md`](audits/2026-08-07-l1-ceiling-confirms-magnitude-absent-and-he4-two-row-suppression.md).

| Atom | B_AME (MeV) | σ_B / B | 100× target |
|---|---:|---:|---:|
| D  |   2.224 | 0.45 ppm | 4.5 ppb |
| T  |   8.482 | 0.12 ppm | 1.2 ppb |
| ³He |  7.718 | 0.13 ppm | 1.3 ppb |
| ⁴He | 28.296 | 0.035 ppm | 0.35 ppb |

### Two subgoals (L2 split)

**Subgoal-1 (currently met only by the two anchors).** 100× targets
≥ ~780 ppb CAL-2 floor. Met: m_e (CAL-1 anchor), m_p (CAL-2 numerical
anchor) — both trivial calibration matches. **No genuine prediction
currently meets Subgoal-1.** Q_β is the closest (1.25 ppm vs 7.8 ppb
target, ~160×) after de-fitting (#1416) removed the CODATA-fitted N=5
ladder that previously read "5.7 ppb"; Δ_pn (~755 ppb) and m_n
(~1.04 ppb) follow Q_β. Closing them is the GAP-A program (per-isotope
Borromean-tower extension + operator-valued branching), NOT a fit.

> **Superseded (do not restore).** Prior text claimed "Q_β N=5
> categorical meets Subgoal-1 (5.7 ppb)" and "Δ_pn via Path C beats
> (4.0 ppb)". Both relied on the CODATA-fitted N=5 Q_β ladder removed
> in #1416. The honest de-fitted values miss the target.

**Subgoal-2 (research-grade).** 100× targets < CAL-2 floor. Includes
absolute m_p (3 ppt), m_n (6 ppt), m_⁴He (0.6 ppt). **Requires
substrate-derivation of q_0**, which the coordination ledger explicitly
declined on 2026-05-08:
> "Q_β derivation? **No** (explicit) — 780 ppb floor stands."
>
> By extension, q_0 (CAL-2) substrate-derivation is also declined.

Subgoal-2 was **out of scope** unless and until the ledger decision is
reverted by the repo owner. That reversal happened on 2026-07-11 (general
reversal below) — **but the q₀-derivation item was then PERMANENTLY
RE-GATED by the owner on 2026-08-02:**

> **🛑 OWNER RULING 2026-08-02 — substrate-q₀ derivation is FOREVER GATED
> (bean `qou-eic1`).** No agent may pursue deriving `q₀` from the substrate,
> in any form, ever — a **permanent** gate, **not** a decline awaiting
> reversal. It **supersedes the 2026-07-11 "open for all" reversal for the
> q₀-derivation item ONLY.** `Δ_λ` magnitude, per-isotope binding, absolute
> `m_p / m_n / m_⁴He` via any **non-q₀** route, and the s5-so3 keystone
> remain open for all. A route that goes through "derive `q₀`" is
> **forbidden — stop it.**

> **Narrow owner reversal (2026-06-19, recorded 2026-06-22; PRs
> [#2503](https://github.com/litlfred/qou/pull/2503) /
> [#2524](https://github.com/litlfred/qou/pull/2524)).** The owner reversed
> the decline **only for the s5-so3 keystone geometric-realization
> construction** — the DG / WRT(S³/2I) build of the `W_λ` index (see
> [`docs/coordination/s5-so3-keystone.md`](coordination/s5-so3-keystone.md)).
> That geometric `W_λ` build was the first item brought in scope. *(Superseded
> in breadth by the 2026-07-11 general reversal below; still valid as the
> first-opened item.)*

> **🟧 GENERAL owner reversal — Subgoal-2 open for all (2026-07-11).** The owner
> reversed the 2026-05-08 decline **generally**: the geometric / substrate-
> derivation routes to the Subgoal-2 targets (absolute m_p / m_n / m_⁴He;
> ~~substrate-derivation of q_0~~ **[🛑 FOREVER GATED 2026-08-02 —
> q₀-derivation is permanently excluded; see the ruling above]**; the
> per-isotope binding `M_n(K)` edge-set /
> coordination-graph closure; the s5-so3 keystone) are now **in scope for all
> agents** — no longer owner-gated, no per-item sign-off required (**except
> q₀-derivation, which is permanently gated**). The
> [step-9 binding-closure ledger](coordination/2026-06-05-step9-binding-closure.md)
> and [`s5-so3-keystone.md`](coordination/s5-so3-keystone.md) carry the working
> threads. Context: the qou-v0yw binding-weight closure (the M₃/M₄ weights of
> `conj:binding-manybody-eq-jet-filtration`) was blocked *only* by this gate plus
> the anti-fit rule; the gate is now lifted.
>
> **What the reversal does NOT change — the anti-fit / anti-laundering honesty
> discipline still stands.** "Open for all" grants permission to *pursue and
> derive*; it does **not** license passing a fit off as a derivation. The Δ_λ
> "no seventh fit-based ansatz" rule, the §"Axiomatization is NOT a Proof"
> anti-laundering rule, and the "sorry-free ≠ derived" / "conditional-proved ≠
> premise-established" rules are **orthogonal to the scope gate** and remain in
> force: a `wₙ(K)` obtained by inverting the AME anchors is still a fit and must
> be labelled one, not wired to production as canonical. Only a *derived*
> `R(q,x)` / geometric bond-count / substrate q_0 may be wired as canonical. If
> the owner later wants fit-based results themselves wired as canonical, that is
> a separate ruling not granted here.

### Measurement-limited ceiling on 4 of the 5 L2 misses (2026-07-18)

Two sorry-free Lean theorems from the 07-17→18 window establish that, **absent a
substrate-derivation of q₀**, four of the five L2 misses are gated on the
**experimental neutron Q_β measurement**, not on any framework compute:

- **Anchor-invariance prune** — `QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing`
  ([`SRigidityPrune.lean`](../content/quantum-observable-universe/lean/QOU/QBeta/SRigidityPrune.lean),
  sorry-free): no *anchor-invariant* datum can equal the c₃ carrier `S` (which
  swings 2.44 % between the proton and muon q₀ anchors). This excludes deformed
  median resummation (anchor-blind) and classical CS/Stokes (anchor-invariant) as
  c₃ realisations. All four geometric routes to the swing are now closed (median
  resummation smooth #3813; CS/Stokes prune; 5₂ quantum volume anchor-smooth
  #3902; branch-point locus generic #3902-cont). c₃/S is intrinsically the
  anchor-dependent quantum `𝔙_q` at q₀ — the `1/u³` inversion of a smooth
  numerator crossing zero at q\* — precision-limited by experimental Q_β
  (`dq*/dQ_β ≈ −0.54`).
- **μ–p pin-sensitivity map** — `PinRobustnessOfRatios.lean` (sorry-free, #3847):
  the μ–p tension lives entirely in the absolute anchor `ℏ_q⁻²`; every **ratio**
  observable (W_λ, m_p/m_μ, m_n/m_p, the McKay keystone) has `ν_ℏ = 0` and is
  structurally blind to the 11.5 ppb split. The geometric W_λ/Lawrence–Rozansky
  realisation is separately refuted (D=2 collapse) and structurally excluded
  (self-duality `S⁴=1`). ⇒ finishing any ratio/geometric-W_λ route will **not**
  move m_p/m_μ; only an anchor-free absolute q₀ can.

**Consequence for the roadmap** (re-scoped 2026-08-08, bean `qou-qb8a` — the
numbers below are unchanged; only the *scope* of the claim was wrong).

**Scope-(a), and established:** the **cal-anchored extraction** route is
measurement-limited. Extracting c₃ *from* a measured Q_β carries
`dq*/dQ_β ≈ −0.54`, and *verifying* any prediction below `σ_exp = 779.7 ppb`
requires a better measurement (target σ ≈ 0.024 eV). Both true, both unchanged.

**What was over-claimed:** the blanket reading — that Q_β (160×), m_n (416×),
Δ_pn (159×), m_p (437×), m_μ (964×) are *"measurement-limited"* full stop, and
that *"everything else on these four misses is a proved dead end"*. Per AGENTS.md
§"Before declaring refuted", that is a **scope-(b) structural exclusion stated
without a proved invariant**. Two facts cut against it:

* **The residual is a framework quantity, not a measurement one.** The 1248 ppb
  Q_β prediction error is the **c₃ truncation**. Under the proton pin, q₀'s
  *measurement* uncertainty contributes `≈ 0.06 ppb × 2.60 ≈ 0.16 ppb` to Q_β —
  **four orders below** the residual. No proved invariant excludes a categorical
  derivation of c₃ from improving it.
* **A better measurement makes the L2 target *harder*, not easier.** The target
  is `σ_exp/100`, so tightening `σ_exp` tightens the target proportionally.
  "Waiting for the measurement" does not close L2 by itself.

Note also that the escape clause as originally written — *"unless a substrate-q₀
derivation lands"* — points at a route the owner **permanently gated** on
2026-08-02 (bean `qou-eic1`). With that route forbidden, the blanket phrasing
read as *unfixable*, which is precisely the over-narrowing the refuted-scope
discipline exists to prevent.

**Open compute levers**: (i) **WITHDRAWN 2026-08-09 — the c₃ D-ladder
resummation was never a lever.** The two-variable form `log R = E(ũ) + h·D(ũ)`
still holds exactly, but the ladder is **convergent**, with radius

    ρ = ũ(q*) = 0.14279999664468968890572088577932032058109273315046
    q*        = 1.4898947996883652482253115227781736826531279179281

`q*` being the unique real root > 1 of the irreducible degree-12 factor of the
`Δ_net` numerator — a **zero of `Q_b`**, where `log R` has a plain logarithmic
branch point. The 2026-07-12 singularity search covered the sqrt branch points,
the `ũ′ = 0` folds, the `Q_A` zeros and the `cos α_eff` zeros, but **not the
`Q_b` zeros**; all three nearest singularities are `Q_b` zeros. Closed form
`D(w) = φ(w)·log(1 − w/ρ) + ψ(w)` with `φ(ρ) = 1/(2h*)`, `h* = q* − 1/q* =
0.818706471352`, giving `d_k = −(1/(2h*))·ρ^{−k}/k·(1 + O(1/k))` with no free
parameters.

There is therefore **nothing to resum**: Écalle/Φ_b resummation, the instanton
action, and the Stokes ambiguity were answering an ill-posed question. The old
text read "the ladder is **divergent** (Gevrey `exp(Bk + Ck·log k)`) … numerical
extraction of the instanton action is **length-blocked at k=41** … the
fibre-branch Stokes probe localises `A_ω = Δ_ω log Φ_b` to the **fibre**". Each
clause is superseded: `C` is a spurious parameter decaying like `1/log k`; the
k=41 wall was tooling cost, not information (k ≤ 21 already suffices); the
Stokes probe's "structural threshold `r* = 0.147`" is the ratio-test estimate of
`ρ` itself, and "ambiguity unsuppressed on the fibre" is the series diverging
outside its disk. The discriminator that settles it on the committed k ≤ 21
data: **`k²Δ²log|d_k| → 1` while `kΔ² → 0`, i.e. `κ = 0`.**

Practical consequence, and it is a gain: at the CAL-2/muon pin `ũ₀ = 0.0094540`
sits **15.10× inside `ρ`**, so `h·D(ũ₀) = −0.003486063636129187405605313929674524979867`
is pinned to 38 digits by the already-committed ladder with a rigorous tail
bound. **This does not derive c₃, does not change its `cal-anchored` tier, and
does not close L2** — the μ–p anchor swing remains 29.96 ppb = 3.84× the target,
and the carrier is still anchor-blind (spread 1.23e-9). The real gate is
unchanged: the map from a bar-odd, anchor-blind fibre object to an
anchor-*dependent* number.
[`docs/audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md`](audits/2026-08-09-dladder-is-convergent-radius-is-the-qb-zero.md).

Remaining lever: (ii) the α_EM per-loop theta-factor (#3911). The listed dead
ends stay dead as **scope-(a)** results (fixed-order/anchor-invariant
resummation; geometric q₀; ratio-based W_λ).

This is a *ceiling record*, not a target change: the L2 targets stand. Full
analysis: [`docs/audits/2026-07-18-1ppq-action-plan.md`](audits/2026-07-18-1ppq-action-plan.md);
re-scoping rationale
[`docs/audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md` §4](audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md).

## Pin discipline — every L2 claim must state its anchor (STRICT, bean `qou-qb8c`)

**The muon/proton anchor swing on Q_β is 3.84× the entire L2 target.** Measured
(mpmath 60 dps; symbolic-exact log-derivative):

```
q rel diff (proton − muon)/muon  =  −11.5371 ppb
dlnQ_β/dlnq                      =   −2.5968
⇒ anchor swing on Q_β            =    29.9596 ppb
L2 target for Q_β                =     7.797 ppb   ⇒  swing / target = 3.842×
```

Two readings, both load-bearing, and they point in opposite directions:

* **2.4% of the 1248 ppb residual** ⇒ re-pinning is **not** a lever that closes
  L2. Do not propose an anchor change as a precision fix.
* **3.84× the target** ⇒ deriving c₃ is **necessary but not sufficient**. A
  derivation that lands Q_β inside 7.797 ppb *at one anchor* has not met L2 if
  the other anchor moves it by 29.96 ppb.

**Therefore:** any claim of the form *"Q_β meets L2"* — in a witness, dashboard,
audit, PR, or chat — **must state which q₀ pin it was evaluated at**, and a claim
that holds at only one pin must say so. An unqualified "meets L2" is not
interpretable, because the two documented pins differ by 3.84 targets.

Per the 2026-08-07 owner directive, new compute defaults to the **experimental
(proton)** pin; the ideal-layer CAL-2 (muon) pin remains correct for the
canonical derivation. Never mix the two inside one computed quantity — see the
straddling hazard in AGENTS.md §"q₀ anchor convention".

Derivation: [`docs/audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md` §2](audits/2026-08-08-qbeta-l2-assessment-post-week-landings.md).

## Where measured

Live snapshot: `computations/per-observable-100x-status.witness.json`
(produced by `per_observable_100x_status.py`). Re-run on every Borromean /
calibration / formula change.

Reproduce:

```bash
python3 computations/per_observable_100x_status.py
```

## Distinction: compute precision ≠ absolute-prediction error

The mass-table sweep (`mass-table-ppb.witness.json`) reports a 6.80% **mean
absolute** error across 10/16 light atoms. This is **not** a compute-precision
failure (L1 is met at 0.0); it is a **structural completeness** gap in the
per-isotope mass formula (only m_p, m_n, μ are wired to Borromean tower).

When reading dashboards:

- **L1 dashboards** (`onepb-status-dashboard`) → cross-method identity at
  fixed compounds. Currently 0.0 / 92.79 ppb (publication rounding floor).
- **L2 dashboards** (`per-observable-100x-status`) → predicted vs CODATA.
  Currently **1/5 scoreable** (`m_K/m_π` alone); `m_p` and `m_e` are
  calibration **inputs**, not predictions, and are excluded. The four
  failing predictions (m_μ, Q_β, m_n, Δ_pn) miss by ~152× to ~970×.
  Quote `beats_100x_scoreable` / `scoreable_total` from the witness;
  `beats_100x_count=2` counts the inputs and must not be quoted as an
  accuracy result (corrected 2026-08-18).
- **Mass-table sweep** (`mass-table-ppb`) → 10/16 with zero-param rule;
  mean |err| 6.80%. This is downstream of Borromean per-isotope extension.

## Practitioner cheat sheet

When working on a precision-affecting change:

1. **Run the L1 dashboard.** If anything regresses below 1 ppb cross-method
   identity, that's a real precision failure — stop and fix.
2. **Run the L2 dashboard.** If a per-observable target gets *worse*, that's
   a regression on accuracy.
3. **Don't conflate** L1 (compute) and L2 (accuracy). A formula that's
   compute-stable to 50 digits can still miss its 100× target by 10⁴.
4. **Don't claim "1 ppb met"** unless you're specific about *which* leg.
   Use phrases like "L1 compute met" or "L2 met for Q_β" not bare "1 ppb".

## See also

- [`docs/audits/2026-05-18-1ppb-workplan-v7-100x-experimental.md`](audits/2026-05-18-1ppb-workplan-v7-100x-experimental.md) — current workplan
- [`docs/coordination/1ppb.md`](coordination/1ppb.md) — cross-PR coordination ledger
- [`computations/substrate/_precision.py`](../computations/substrate/_precision.py) — compute precision infrastructure
- [`computations/per_observable_100x_status.py`](../computations/per_observable_100x_status.py) — L2 status reporter
