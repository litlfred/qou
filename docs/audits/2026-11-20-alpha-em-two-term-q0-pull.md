# Why the two-term proton pin makes α_em worse — and what the α_em constructions actually say about q₀

Date: 2026-11-20. Branch `claude/alpha-em-witten-kappa-2026-11-20`, PR #8562.
Owner question (Carl, 2026-11-20): *"why did the two-term make the fine structure constant worse?"*

Every number below was measured this session by
[`computations/probes/alpha_em_two_term_q0_pull_probe.py`](../../computations/probes/alpha_em_two_term_q0_pull_probe.py)
(mpmath, 70 dps, CODATA 2022 read from `qou_substrate.codata`, 5/5 checks pass,
no witness). All three pins are re-derived inside the probe, not copied; the
one-term pin reproduces `qou_substrate.constants.Q_50_DIGIT_STR` to 1e-48 and the
two-term pin reproduces the 60-digit value in PR #8554 to 1e-55.

## 1. The short answer

The form-B α_em⁻¹ (the scorecard construction) depends on `q` steeply:

    d ln(1/α) / d ln q  =  6.833390293   at the one-term proton pin.

The two-term pin of PR #8554 sits **+11.170941 ppb** above the one-term pin. So
the residual moves by `6.8334 × 11.1709 = 76.335 ppb`:

| pin | q₀ | form-B 1/α | residual vs CODATA 2022 |
|---|---|---|---|
| one-term proton | `1.1099785827513808075916690956…` | 137.0359991269509 | **−0.36523 ppb** (−2.38 σ_α) |
| two-term proton (#8554) | `1.1099785951508859990875652036…` | 137.0360095876494 | **+75.97018 ppb** (+495.7 σ_α) |
| muon (CODATA 2022) | `1.1099785956427390466817951294…` | 137.0360100025955 | +78.99819 ppb (+515.5 σ_α) |

The linear account `−0.365226 + 6.83339 × 11.170941 = 75.970174 ppb` agrees with
the exact re-evaluation `75.970179 ppb` to 5e-6 ppb, so nothing nonlinear is
going on. α did not "get worse" for a reason of its own: **it was pinned to the
one-term proton value already, and the re-pin moved `q` away from it.**

## 2. Why the slope is ~7

The backbone of every live α construction except one is the bare
`q · [9]_q · [10]_q`. With `λ = ln q₀ = 0.10434072032` and
`[n]_q = sinh(nλ)/sinh(λ)`,

    d ln [n]_q / d ln q  =  n·coth(nλ) − coth(λ)   ≈ (n² − 1)·λ/3   for small nλ.

| factor | exact log-slope | small-λ estimate `(n²−1)λ/3` |
|---|---|---|
| `q` | 1 | 1 |
| `[9]_q` | 2.62960556967 | 2.78241920852 |
| `[10]_q` | 3.21444087703 | 3.44324377054 |
| **total (bare)** | **6.8440464467** | — |

The exact anatomy matches `mp.diff` to 1e-40. The slope is large because the
q-integer log-slope grows like `n²`, and 9 and 10 are the two largest
q-integers anywhere in the corpus's scored formulas. The additive terms
(`8/(12π)`, `αH`) dilute it slightly, to 6.8334 for form B. For comparison, the
mass relations have log-slopes **−20.997** (m_p/m_e) and **−18.185**
(m_μ/m_e, which is exactly `−2/(q−1)`). So per ppb of `q`, α moves about a
third as much as a mass ratio does, but α is measured ~100× more precisely than
m_μ/m_e. That combination is what makes α a sharp probe of `q₀`.

## 3. The α_em constructions side by side

Four distinct α_em⁻¹ functionals are live in the corpus (five rows with the bare
backbone). They are scored at the same three pins.

| construction | formula | where | Lean status | 1/α at one-term pin | resid (ppb) one-term / two-term / muon | log-slope |
|---|---|---|---|---|---|---|
| **B (Schwinger)** | `1/α = q[9]_q[10]_q + 8/(12π) + α·H·(1 − h²α)`, `H = [2]_q/(8π)`, `h = q − q⁻¹` | `computations/alpha_em_schwinger_ladder_probe.py`; the α_em⁻¹ scorecard row | `prop:em-coupling-bring-zero-mode` (`QOU/Archimedean/EmCouplingBringZeroMode.lean`, #3625). The Schwinger factor `c = 1` is **not derived**: the probe's own docstring records that the exact vertex-moment check gave +0.1281 against the claimed −0.0437, and the c that hits CODATA is 0.7312, with c = 1 outside its 1σ window | 137.0359991269509 | −0.365 / +75.970 / +78.998 | 6.83339 |
| A (quadratic) | B without the `(1 − h²α)` factor | same probe | same block | 137.035999313169 | +0.994 / +77.329 / +80.357 | 6.83339 |
| **CS tower (exact)** | `bare·(1 + c₁/(1 − c₁κ))`, `bare·c₁ = π²(10/9+16/15)·[2]_q/2·ℏ_q²`, `κ = det G_cl/det G_q` | `meson_em_sinh_closed_form.alpha_em_inv_derived`; **feeds the m_K/m_π row** (`per_observable_100x_status.py`) and #8557's `c_em` | `em-coupling-chern-simons.lean` states it with `G_q` a parameter of the class `ChernSimonsCorrectionConjecture`, no instance (bean `qou-gbsa`). The `[10]_q` linchpin is asserted (bean `qou-15sj`) | 137.0359350939756 | −467.636 / −390.982 / −387.942 | 6.86193 |
| 45·[3]_q form | `45[3]_q(1 + δ_CS + 8qδ_CS²)`, `δ_CS = ℏ_q⁴[5]_q` | `computations/probes/np_two_term_qed_mup_tension_probe.py::alpha_em_inv_qou`; quoted in `docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md` | **RULED OUT** as a single-point PSLQ fit (`docs/audits/2026-06-10-alpha-em-legacy-empirical-forms.md`; `DERIVATION-STATUS.md` ALPHA-2; `2026-08-22-alpha-em-derivation-redteam.md`) | 137.0359995317168 | +2.588 / +5.885 / +6.016 | 0.29511 |
| bare | `q[9]_q[10]_q` | — | — | 136.8232088535826 | −1.55×10⁶ (all pins) | 6.84405 |

**Defect found:** the np two-term probe calls the ruled-out 45·[3]_q form
"QOU derived fine-structure constant inverse" in its docstring, and the
2026-11-18 audit quotes it as `α_EM⁻¹(q_proton)` without the ruling. Neither
consumer is a scorecard row. Not fixed here (another arc's producer); recorded
in bean `qou-q0pl`.

### 3.1 Are B and the CS tower the same object, a truncation, or different?

**Different objects. Decided structurally, not by residual.** Both add ≈0.212 to
the bare backbone, but the two additive terms are different functions of `q`:

| q | form B: `8/(12π)` | CS tower: `π²(98/45)·[2]_q/2·ℏ_q²` | relative gap |
|---|---|---|---|
| 1.05 | 0.21220659078919 | 0.048796809531547 | −0.770 |
| **q₀ = 1.10998** | 0.21220659078919 | 0.21215835947176 | −2.27×10⁻⁴ |
| 1.2 | 0.21220659078919 | 0.60700097849498 | +1.860 |

One is a constant; the other vanishes like `ℏ_q²` as `q → 1`. They agree to
2.3×10⁻⁴ at `q₀` and nowhere else, so neither is a truncation or resummation
of the other. Their second-order terms also differ (form B `αH = 5.839×10⁻⁴`;
CS tower `bare·c₁²κ = 5.664×10⁻⁴`). That one-point near-coincidence is the
whole reason the two land 467 ppb apart instead of 10⁵ ppb apart, and it is
not evidence that they describe one object. A and B differ only by the
Schwinger factor, so they are one construction at two truncations of that
factor. The 45·[3]_q form shares no ingredient with any of them (bean
`qou-aemx`).

**What decides, and whose decision.** Which α_em functional is canonical is
not a measurement question. It is the open owner decision already recorded in
bean `qou-aemx` ("Decide which construction is canonical"). The structural fact
above narrows it: you cannot make both rows consistent by a choice of order,
truncation, or resummation; one functional has to be named.

## 4. Each construction read as a determination of q₀

Setting each α functional equal to CODATA 2022 defines its own `q*`. The
σ on `q` is `σ_rel(α) / |slope|`, with `σ_rel(α⁻¹) = 0.153244 ppb`.

| construction | q* − one-term (ppb) | q* − two-term (ppb) | q* − muon (ppb) | σ_q (ppb) |
|---|---|---|---|---|
| B | **+0.0534** (2.38 σ) | −11.117 (−495.7 σ) | −11.561 (−515.5 σ) | 0.02243 |
| A | −0.1454 (−6.48 σ) | −11.316 | −11.759 | 0.02243 |
| CS tower | +68.149 | +56.978 | +56.535 | 0.02233 |
| 45·[3]_q (ruled out) | −8.771 | −19.942 | −20.385 | 0.5193 |

The "α prefers the proton pin to 0.245 ppb" in the ladder probe's docstring is
traced to `computations/alpha_em_anchor_preference_probe.py`: it is **form A
against CODATA 2018** (+1.67 ppb in `1/α` ÷ 6.83 = 0.245 ppb in `q`). The code
of that probe reads CODATA 2022 from the registry, but its docstring and
witness `source` text still carry the 2018 figure. Against 2022 the form-A
offset is −0.145 ppb, and form B's is +0.053 ppb. The qualitative claim stands
(α sits within 0.25 ppb of the one-term proton pin under either edition). The
quoted figure is stale; bean `qou-q0pl`.

### 4.1 The joint picture

| determination | q (offset from one-term, ppb) | σ_q (ppb) | source of σ |
|---|---|---|---|
| m_p/m_e, one-term identity | 0 | **0.00083** | CODATA σ(m_p/m_e)/m_p/m_e = 0.0174 ppb ÷ 20.997 |
| m_p/m_e, two-term identity (#8554) | +11.1709 | 0.00083 | same datum |
| α_em form B | +0.0534 | 0.02243 | CODATA σ(α) ÷ 6.833 |
| m_μ/m_e | +11.6141 | **1.22335** | CODATA σ(m_μ/m_e)/m_μ/m_e = 22.247 ppb ÷ 18.185 |

Pairwise, σ in quadrature:

| pair | gap (ppb) | σ |
|---|---|---|
| α_B − m_p one-term | +0.0534 | 2.38 |
| m_μ − m_p one-term | +11.6141 | 9.49 |
| m_μ − m_p two-term | +0.4431 | 0.36 |
| α_B − m_p two-term | −11.1175 | **−495.4** |
| m_μ − α_B | +11.5606 | 9.45 |

(The m_p one-term vs two-term "gap" is one datum read through two formulas, so
its σ count means nothing and is omitted.)

**The data split two against two.** `{m_p one-term, α_B}` agree to 2.4σ.
`{m_p two-term, m_μ}` agree to 0.36σ. Between the two pairs is 11.1–11.6 ppb in
`q`, which is 9.5σ in muon units and ~500σ in α units. The two-term re-pin did
not remove a tension; it moved the proton from one side of it to the other.
Before it was "μ against {p, α}"; now it is "α against {p, μ}", and α is the
sharper witness.

The correction to the σ that the task brief quoted: 0.017 ppb is the CODATA
uncertainty of the **ratio** m_p/m_e. In `q` it is 0.00083 ppb, because the
ratio's log-slope is −21.

## 5. Explanations, ranked by evidence — not by residual

### E1. The two-term proton QED term is not a derived correction — strongest evidence

- **What it says.** The `+|tr_conn(p, V³)|` added to the proton identity is not
  the proton's electromagnetic self-energy. The one-term identity stands, and α
  agrees with it.
- **Evidence for.** PR #8554's own body scopes the term as *selection-scoped*:
  plain weighting at the m_e scale, from an adjacent pair insertion that is not
  braid-covariant. PR #8552 (closed) proves, in Lean and sorry-free, that the
  permutation-complete covariant pair insertion has `M`-coefficient **exactly 0**
  on both nucleons (T6). A nonzero coefficient arises only from a pair subset,
  i.e. a selection. PR #8557 proves the crossing-covariant strand-labelled
  first-order insertion is **exactly 0 on V³** for both nucleons at every `q`
  (`borromean_firstOrder_trace_zero`). Both are scope (b) *inside their stated
  operator classes* and scope (a) outside them. Every derived covariant QED
  insertion tested so far gives proton self-energy 0, and a zero proton
  self-energy is exactly the one-term identity that α_B agrees with to 2.4σ.
  The 2026-11-18 audit reached its +0.22 keV by choosing among a menu
  (QOU-P12, P13, …), which is selection against the target.
- **Evidence against.** Operators outside the covariant classes are not
  excluded. The physical proton does have a positive EM self-energy
  (Cottingham), so "zero" can only be a statement about the model as it stands.
- **Independent of α?** Yes. It rests on #8552/#8557 Lean, not on the α
  residual, so it is not circular.

### E2. The muon relation is the one missing a self-energy — consistent, unsupplied

- **What it says.** `m_μ/m_e = Vol(4₁)/ℏ_q²` lacks a term. That would resolve
  μ–p without moving the proton pin, and it is consistent with E1 and with α.
- **Size needed (diagnostic only; no candidate is chosen).** At the one-term
  pin the relation needs a multiplicative factor `1 + δ_μ` with
  `δ_μ = −211.2058 ppb`, i.e. `−9.09×10⁻⁵ · α/π`, `−3.97×10⁻³ · α²`, or
  `−2.15×10⁻⁵ · ℏ_q²`. None of these is close to an O(1) coefficient, so
  no natural one-loop term has this size. Any "match" would be numerology.
- **Corpus supply.** None found. Searched for "muon self-energy" /
  "self-energy … muon" in `docs/audits`, `computations`, `folio` and the beans;
  the only hits are the 2026-11-18 audit and bean `qou-eas4`, both about the
  **proton** side. That is an absence on that surface, not a proof that nothing
  exists.
- **Cost of the move.** That relation **is** the CAL-2 definition (the ideal
  layer). Adding a term redefines CAL-2. That is an owner decision, not an
  agent one.

### E3. α_em needs a matching two-term correction of the same origin — weak

- **What it says.** If the proton gains a QED term, α should gain the matching
  one.
- **Size needed.** It would have to be −76 ppb in 1/α at the two-term pin.
- **Corpus supply.** No α-side object exists, and none is derived from the
  same `tr_conn`.
- **Assessment.** Choosing a term because it cancels the 76 ppb is selection
  against the target. No evidence.

### E4. The α agreement itself is not derived — real, and it limits how much weight α carries

- **What it says.** α_B's 2.4σ agreement with the one-term pin may not be a
  derived result.
- **Evidence.** The Schwinger factor `c = 1` is not derived: its exact check
  failed (2026-07-14), and the CODATA-hitting `c = 0.7312` puts `c = 1` outside
  the 1σ window. The `8/(12π)` term's derivation status was not re-audited
  here. And the construction that *is* wired into a scored row, the CS tower
  feeding m_K/m_π, has `q*` +68 ppb from the one-term pin and +56.5 ppb from
  the muon pin, so it sits with neither group and cannot arbitrate.
- **But robust to the Schwinger choice.** Form A (no Schwinger) gives `q*` at
  −0.145 ppb, and form B at +0.053 ppb. Both are within 0.2 ppb of the
  one-term pin and 11.5 ppb from the muon pin. So the α vote for the one-term
  pin does **not** depend on the underived factor. It depends on the backbone
  `q[9]_q[10]_q + 8/(12π)`, whose `[10]_q` linchpin is itself asserted (bean
  `qou-15sj`).
- **Upshot.** E4 lowers α's evidential weight. It does not move α's vote.

**Net, as judgement and not a finding.** E1 is the only explanation that is
supported independently of the residuals. It says the re-pin built a selected
term into `q₀`. E2 is the logically clean complement, but nothing in the corpus
supplies it. E3 has no support. E4 is true but does not change which side α
is on.

## 6. Consequences for the scored rows

- **α_em⁻¹ row (form B).** At the one-term pin: −0.365 ppb, a 238.3× miss of
  the 100× target (0.0015324 ppb). At the two-term pin: +75.970 ppb, a
  **49,574× miss**. It fails L2 either way, so the 1/6 headline is unchanged,
  but the row degrades by ~208× in miss factor.
- **m_K/m_π row.** It uses the **CS tower**, not form B. The CS residual
  improves under the re-pin, −467.6 → −391.0 ppb, because the CS `q*` is above
  both pins. #8554 reports m_K/m_π 51.48 → 55.89 ppb (still passing). That row
  already carries α through an underived construction (qou-gbsa, qou-15sj), so
  its pass remains truncation-fitted and α-construction-conditional (0/6
  unconditional stands).
- **Witten-κ `sorry` (Task A).** The `sorry` in
  `mass-theory/gram-determinant-plancherel-ratio.lean`
  (`gram_kappa_numerical_value`) stated a false proposition. It is replaced by
  the sorry-free `gram_kappa_numerical_value_refuted`. The κ = 1.7216 that the
  CS tower uses is `det G_cl / det G_q` and never touched `gramKappa`. So the
  m_K/m_π row was **never conditional on that `sorry`**. Its α conditionality
  is the class `ChernSimonsCorrectionConjecture` with no instance (qou-gbsa),
  which is a different and still-open premise. "α_em-sorry-conditional" should
  be read as "α_em-construction-conditional".

## 7. Formalised here, and not

- **Formalised:** `gram_kappa_numerical_value_refuted` (Lean, sorry-free,
  axioms `propext, Classical.choice, Quot.sound`).
- **Not formalised:** the sensitivity identity `n·coth(nλ) − coth(λ)` and a
  monotonicity-based "two pins cannot both match" lemma. The generic version
  (a strictly monotone function hits a target at one point) is Mathlib-trivial
  and would add no content. The non-trivial version (monotonicity of the form-B
  cubic root in `q` on `q > 1`) was not attempted in this session. It is
  recorded as a follow-up in bean `qou-q0pl`.

## 8. Open items

| bean | what |
|---|---|
| `qou-wkgp` | GAP: a well-typed statement of the Plancherel-product ↔ det-ratio identification (common `n`, integer exponents, central elements). Without it, no `sorry` should be queued. |
| `qou-q0pl` | This measurement: the 2-vs-2 split; the mislabelled 45·[3]_q in the np probe; the stale 2018 "0.245 ppb" text in `alpha_em_anchor_preference_probe.py`; the form-B monotonicity lemma. |
| `qou-aemx` | Owner decision: which α_em functional is canonical (B vs CS tower; they are different objects, §3.1). |
| `qou-gbsa`, `qou-15sj`, `qou-gwio` | CS tower: `G_q` underived, `[10]_q` asserted, −467.6 ppb structural. |
