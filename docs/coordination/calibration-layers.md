# The three calibration layers — math ideal / observational ideal / fitted ideal

**Status:** convention record — **the fitted-ideal layer is PAUSED, see the
banner below.** Owner-specified 2026-08-26.
**Beans:** `qou-mkgt` (epic), `qou-nds9` (this doc), `qou-zeeg` (producer).

> ## 🛑 PAUSED — do not build on the fitted ideal (owner ruling, 2026-08-26)
>
> **The large fitted q₀ variation means the model is not yet correct enough for
> this layer to mean anything. A term is missing in binding.**
>
> The owner's ruling, in their words: *"the large q_0 fitted variation means
> model is not correct enough yet to do this… we are missing term in binding."*
>
> **Why the layer's own numbers say the same thing.** A calibration layer is
> only meaningful when the fitted values land *near* the measured ones — then
> the residual is model error and the calibration is a calibration. Here they do
> not: the fit demands `m_e = 1.9455 MeV` against CODATA's 0.51100 (**3.8×**)
> and moves `q` **+3.26 %** off the substrate pin. Two calibration parameters
> travelling that far are not exercising calibration freedom; they are
> **absorbing model error into calibration values**, which is exactly the
> signature a missing extensive term in `B` produces. The held-out split says it
> again from the other side: the light and heavy regimes want moduli 3.4 % apart
> (`1.14615` vs `1.10861`), so no single three-point choice serves both.
>
> **What this does and does not retract.**
>
> - **The diagnostic stands.** The measurements below are correct as recorded
>   and were the point: they *bound what recalibration alone can buy* (93.09 % →
>   28.80 % in-sample, and worse out-of-sample), and they are independent
>   evidence for the missing **additive extensive** term. Nothing here is
>   withdrawn.
> - **The layer is not usable as a calibration.** Do not quote the fitted values
>   as a calibration of the framework, do not wire them anywhere, and do not
>   score any observable against them. They were already labelled a fit
>   (`anti_fit_label.may_be_wired_to_production: false`); this ruling is
>   stronger — the layer itself is on hold, not merely unwired.
> - **The unblocking condition is the missing binding term**, not more fitting.
>   Once `B` carries the super-pairwise additive extensive object, re-run the
>   producer: if the fitted calibration then lands near CODATA and the two
>   regimes agree on `q`, the layer becomes meaningful. That convergence is the
>   test to apply — and it is a real one, since the layer can currently fail it.
>
> **Do not open a follow-on that fits harder.** Widening the objective, adding
> isotopes, or freeing more parameters all move in the wrong direction: they
> make a mis-specified model fit better without making it more correct. The
> ⁴He outlier (−59.2 %) and the `m_K/m_π` CAL-3 option are both **on hold** for
> this reason.

The framework has **exactly three calibration points** in every layer below.
The layers differ *only* in **how the three values are chosen** — never in how
many there are. No layer introduces a fourth degree of freedom, and the count
identity with `H¹(Bring) = 2W` (rank-2 W-plane scale + modulus + one orthogonal
class; 2+1 = 3, Lean `QOU.Mass.calibrations_eq_cohomology`) is untouched.

| Layer | The three points are… | Chosen by |
|---|---|---|
| **Math ideal** | the canonical triple CAL-1 `m_e`, CAL-2 `𝔇_β`, CAL-3 `𝔇_π` | definition — this is *what the calibration is* |
| **Observational ideal** | the same three, taken as **measured values** (CODATA / PDG), via their numerical proxies `m_e`, `m_μ/m_e` (or `m_p/m_e`), `m_π` | measurement |
| **Fitted ideal** | the same three, treated as **free parameters** | minimising binding-energy error over a set of low isotopes (²H, ³H, ³He, ⁴He, …) against AME2020 |

## What the fitted ideal is for

It separates two things the other two layers confound:

- the **choice of calibration** (which observables you elect to reproduce exactly), and
- the **model's own error** (how well the framework's *shape* tracks nature once
  calibration is chosen as favourably as possible).

The observational ideal reproduces its three anchors *exactly by construction* —
so those three carry no information about model quality (this is the same
tautology `AGENTS.md` §"Precision goals" already forbids scoring: `m_e` and `m_p`
are inputs, not predictions). The fitted ideal instead spends the same three
degrees of freedom on an **over-determined** objective: 3 parameters against
N > 3 isotopes. The residual that survives is therefore a genuine, falsifiable
measure of model error, and it is the strongest of the three layers for judging
the framework.

## The fitted ideal is a fit, and is labelled one

Per `AGENTS.md` §"Axiomatization is NOT a Proof" and the Δ_λ anti-fit rule:

- The fitted-ideal values are **fitted**, not derived. They may be reported and
  compared; they may **not** be wired to production as canonical, and no
  quantity derived from them may be presented as a parameter-free prediction.
- The canonical layer remains the math ideal; the production numerical pin
  remains the **proton** experimental anchor (owner directive 2026-08-07,
  re-affirmed 2026-08-15 R2). This layer changes neither.
- It is *not* a fourth calibration: the count stays three. What changes is the
  objective the three are chosen against.

## Identifiability — measured, not assumed

Low-isotope binding enters the chain as

    B(K) = Q_β(n) · ( tr_M(W_free) − tr_M(W_atom) )

(`computations/binding_canonical.py`). Reading the three calibration DOF off
that formula:

1. **CAL-1 (`m_e`)** — a pure multiplicative MeV scale on every `B`. Identifiable,
   and only through the overall normalisation.
2. **CAL-2 (`𝔇_β`, proxy `q₀`)** — enters both `Q_β` and the dimensionless trace
   difference, non-linearly and differently per isotope. Identifiable.
3. **CAL-3 (`𝔇_π`, proxy `m_π`)** — **does not appear in `B` at all.** The
   low-isotope binding objective is therefore *flat* in CAL-3: it cannot be
   fitted against this target set.

So the fitted ideal has **three calibration points but two identifiable
directions** under a pure low-isotope-binding objective. CAL-3 must either be
held at its observational value, or the objective must be widened by a
meson-sector observable (e.g. `m_K/m_π`) that does constrain it. Any report of a
fitted-ideal calibration must say which of the two was done — a fitted CAL-3
quoted off a flat objective is meaningless.

## Result

Producer: [`computations/fitted_ideal_low_isotope_calibration.py`](../../computations/fitted_ideal_low_isotope_calibration.py)
→ `computations/fitted-ideal-low-isotope-calibration.witness.json`. Runs in 0.5 s.

`B_AME` is read from the **vendored AME2020 table** (`ame_2020_binding_energies._binding_mev_exact`,
exact `Decimal`) rather than from the sweep witness, so the target set is not
limited to what that witness happens to carry. Two low-set values differ from
the sweep in the 5th decimal (⁶Li 31.99399 vs 31.99453, ⁷Li 39.24508 vs
39.24453) — different AME routes; the exact table is the better source and the
difference is ~1e-5 relative, far below every residual below.

Relative-RMS binding error over the seven isotopes (²H, ³H, ³He, ⁴He, ⁶Li, ⁷Li, ⁷Be):

| Layer | rel-RMS | calibration values |
|---|---|---|
| Observational ideal | **93.09 %** | `q₀ = 1.10997858`, `Q_β = 0.78233 MeV`, `m_e = 0.51100 MeV` (all measured) |
| Fitted ideal, scale only | **62.26 %** | `q` held at `q₀`; scale free |
| Fitted ideal, both identifiable directions | **28.80 %** | `q = 1.14615282` (+3.26 %), `Q_β = 2.7435 MeV` (3.5×), implied `m_e = 1.9455 MeV` (3.8× CODATA) |

Per-isotope residual at the two-direction best fit:

| | ²H | ³H | ³He | ⁴He | ⁶Li | ⁷Li | ⁷Be |
|---|---|---|---|---|---|---|---|
| observational | −80.4 % | −91.8 % | −91.0 % | −96.9 % | −96.6 % | −97.2 % | −96.6 % |
| fitted | +31.4 % | −21.2 % | −17.4 % | **−59.2 %** | −12.3 % | +0.4 % | +20.2 % |

Two things the numbers carry:

1. **Recalibration buys a lot and still fails.** 93.1 % → 28.8 % is a real
   improvement — the observational layer is a long way from the best this model
   can do — but 28.8 % RMS is still ~10⁷ times outside the L2 100× target, and
   the residual remains **shape-structured, not normalisation-structured**
   (²H over-predicts, ⁴He under-predicts by −59 %, ⁷Li lands at +0.4 %). ⁴He,
   the doubly-magic case, is the worst outlier at the fitted point.
2. **The fit demands calibration values far outside measurement.** Reaching
   28.8 % requires an implied `m_e` of 1.95 MeV against CODATA's 0.511 — a
   factor 3.8 — and `q` shifted +3.26 % off the substrate pin. So the fitted
   ideal is not a rescue of the model under a kinder calibration; it is a
   **bound on what recalibration alone can buy**, and the bound is far short.

**Reading (scope-(a), per `AGENTS.md` §"Before declaring refuted"):** a
scope-limited negative about the *current* binding construction — its
`A`-dependence is wrong, not merely its normalisation, and no choice of the
three calibration values fixes that. It excludes no ingredient. It is
independent evidence for the already-recorded finding that the missing object is
a separate super-pairwise **additive extensive** term rather than a per-block
re-weighting
(`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`).

### Held-out test — the sharpest result

The seven low isotopes are what the fitted ideal is *defined* against, so a fit
on them is in-sample. Eleven heavier nuclides (⁹Be, ¹⁰B, ¹¹B, ¹²C, ¹⁴N, ¹⁶O,
²⁰Ne, ²⁴Mg, ²⁸Si, ⁴⁰Ca, ⁵⁶Fe) are **never shown to the fit** and are used only to
ask whether a calibration fitted on the light nuclei *generalises*.

| held-out rel-RMS under… | value |
|---|---|
| the observational calibration | 97.89 % |
| the calibration fitted on the low set (`q = 1.14615`) | **4.48 × 10⁸ %** |
| a calibration refitted on the held-out set itself (`q = 1.10861`) | 15.44 % |

The middle row is not a rounding artefact. The trace deficit grows
geometrically in `A`, so the +3.26 % shift in `q` that the light nuclei want
compounds: predicted `B(⁵⁶Fe) = 7.3 × 10⁹ MeV` against 492 MeV measured.

**Do not read the blow-up itself as the finding.** That the construction
degrades past the light nuclei is already known and expected (it is what the
`dashboard-sweep` skill exists to display); extrapolating it to ⁵⁶Fe is outside
where the binding construction is claimed to apply, and a large number there is
not news.

**The finding is the disagreement between the two fitted moduli.** The light
nuclei want `q = 1.14615`; the heavier ones want `q = 1.10861` — which is within
0.13 % of the substrate pin `q₀ = 1.10998`, while the light-nucleus preference
sits 3.26 % away. **No single choice of the three calibration points serves both
regimes**, and the regime that disagrees with the substrate pin is the *light*
one. That is a statement about the model's `A`-dependence, not about calibration
choice — which is exactly the separation this layer was added to make.

### Convention check — verified D by VALUE, not by docstring

Asked directly whether the witness data underneath this layer was convention **C**
(the excised `z = √q/(q+1) ≈ 0.49932`) rather than the canonical **D**
(`z = q³/(q²+1) ≈ 0.61269`). It is **D**. Verified at the level of numbers, not
declarations — `AGENTS.md` records a case where "the declaration, the interface
and the constituent were three different answers", and #5812 has since found a
**fourteenth** live C-spelling in Lean (`QOU.Hecke.ClosedFormInterfaceFactors`,
`z = s/(s²+1)` with `q = s²` — C in a square-root variable, invisible to the
detector).

Three independent checks:

| check | result |
|---|---|
| `markov_z(q₀)` returned value | `0.6126880371464652516` = **D** exactly; C would be `0.49932033418369445241` |
| `y_(1³)` in both `y_λ` sources | `0` exactly (closed form) and `3.5e-72` (bridge) — the **D** signature; C has `y_(1³) ≠ 0` |
| committed `low-isotopes-binding-sweep` `B_pred` vs recomputation | matches **D** to `1.4–3.0e-7`; a **C** recomputation is off by **8–23 %** |

The third is the decisive one, because it tests the *gate reference* rather than
this producer: the committed sweep is what the gate ties the evaluator to, so if
it were C-frame the whole layer would inherit C regardless of what this code
does. The C/D separation is **six orders of magnitude** larger than the residual,
so it is not a marginal call.

Per-isotope, committed vs recomputed:

| | committed | `z_D` recomputed | rel | `z_C` recomputed | rel |
|---|---|---|---|---|---|
| ²H | 0.435403544348 | 0.435403481607 | 1.44e-7 | 0.535776972123 | **0.231** |
| ³H | 0.695131652156 | 0.695131497432 | 2.23e-7 | 0.774296399072 | **0.114** |
| ³He | 0.698552359972 | 0.698552209990 | 2.15e-7 | 0.814424403266 | **0.166** |
| ⁴He | 0.876064256364 | 0.876063997507 | 2.95e-7 | 0.944656580873 | **0.078** |

The ~2e-7 residual is a path difference (the committed sweep reaches `B_pred`
through cached χ matrices rather than this recomputation), not a convention
difference — a convention difference is 10⁶ times larger.

### One defect avoided, worth recording

`tr_m_wenzl_bridge_mpfr._load_y_lambda` picks a **cached** `y_λ` table by
matching `q_str` against the known anchors, and for an **unrecognised** `q₀`
"keeps the previous default rather than guessing" — the proton table. Inside a
fit loop *every* trial `q` is unrecognised, so calling the bridge naively pairs
proton-pinned `y_λ` with `χ_λ` evaluated at the trial `q`: a systematic instance
of the layer straddle `AGENTS.md` documents (the μ₃ Fréchet incident, 11.54 ppb
— and far worse here, since the trial `q` ranges over several percent rather
than sitting 11 ppb away). The producer takes `χ_λ` from the bridge's
`return_breakdown` (χ depends only on the word and `q`, never on the `y` table)
and recombines it with `y_λ(q)` from the live closed form at the same `q`.

Anyone extending this objective to another observable must do the same. The
producer is gated on reproducing the committed
`low-isotopes-binding-sweep.witness.json` `B_pred` at `q₀` to 1e-6 and refuses
to print a fitted number otherwise, precisely so a broken evaluator cannot
launder one.

## Superseded baseline (scale-only, kept for the record)

Fitting **only** the overall scale (CAL-1 direction) against the seven isotopes in
`computations/low-isotopes-binding-sweep.witness.json`, holding `q₀` at the
production pin:

| | RMS relative error | worst |
|---|---|---|
| Observational ideal (scale = 1, as-is) | 93.09 % | −97.18 % (⁷Li) |
| Fitted ideal, scale-only (scale ≈ 8.649) | 62.26 % | −75.62 % (⁷Li) |

The residual is **shape-structured, not normalisation-structured**: at the
best-fit scale ²H over-predicts by +69 % while every `A ≥ 4` isotope
under-predicts by −70…−76 %. The `B_AME/B_pred` ratios span 5.11 (²H) → 35.48
(⁷Li), a factor of ~7. A single multiplicative scale cannot absorb a factor-7
spread, and neither can adding one more smooth DOF in `q₀`.

**Reading (scope-(a), per `AGENTS.md` §"Before declaring refuted"):** this is a
scope-limited negative about the *current* binding construction — the
`A`-dependence of `B_pred` is wrong, not merely its normalisation. It is
consistent with, and independent evidence for, the already-recorded finding that
the missing object is a **separate super-pairwise additive extensive term**
rather than a per-block re-weighting
(`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`).
It excludes no ingredient; it bounds what recalibration alone can buy.
