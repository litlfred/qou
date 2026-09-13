# The ℚ(q)-coefficient leg of the bar-odd discriminator — vacuous over ℚ(q), one line over the bar-fixed field, and that line is not a Markov trace

**Date:** 2026-09-08 · **Bean:** `qou-0e2p` (continues `qou-99qc` / #7118) · **Sibling context:** #7115 (the augmentation *is* the Markov trace at `z = q`)
**Probe:** [`qbeta_bar_odd_qq_coefficient_leg_probe.py`](../../computations/qbeta/qbeta_bar_odd_qq_coefficient_leg_probe.py) — 24/24, exact sympy over ℚ(q); the proton pin enters only at readout as an exact `Rational`
**Tier:** extends #7118's exclusion-within-the-span; the new statement is *"no bar-odd **Markov** trace on `Δ_L` with p↔n-neutral coefficients"*. Nothing wired, no functional adopted, no value proposed.

[#7118](2026-09-07-bar-oddness-discriminates-the-two-qbeta-elements.md) §4a left one leg open: what happens when the coefficients of the trace span live in ℚ(q) rather than ℚ, so that the bar involution `q ↦ 1/q` acts on them too. This closes it — and corrects that document's §5 on the way, because its "truncated reference" diagnosis was inverted.

---

## 1. The setup, and why "coefficients in ℚ(q)" is a semilinear question

Write `F = ℚ(q + 1/q)` for the bar-fixed subfield and `h = q − 1/q`, so that `ℚ(q) = F ⊕ F·h` with bar acting as `+1` on `F` and `−1` on `h`. Every `X ∈ ℚ(q)` splits uniquely as `X = X_e + h·X_o` with `X_e, X_o ∈ F` (the probe verifies each split lands in `F`).

For an element `Δ` write `A := tr_M^{z=q}(Δ)` and `B := tr_M^{z_D}(Δ)`, the two admissible traces (#7115 established the augmentation is the Markov trace at `z = q`, so both are points of one family). The question is the solution set

```
S(Δ) = { (a, b) ∈ ℚ(q)² : bar(aA + bB) = −(aA + bB) }.
```

Because bar is only `F`-linear, `S(Δ)` is an **`F`-vector space, not a ℚ(q)-subspace**. Splitting `(a, b) = (a₀ + a₁h, b₀ + b₁h)` over `F`, the condition "even part of `aA + bB` vanishes" is **one `F`-linear equation in four `F`-unknowns**:

```
a₀·A_e + h²·a₁·A_o + b₀·B_e + h²·b₁·B_o = 0 .
```

## 2. The result — three coefficient fields, three answers

| coefficients in | `Δ_S` | `Δ_L` |
|---|---|---|
| **ℚ** | all of ℚ² | `{0}` — *reproduces #7118* |
| **`F`** (bar-even) | all of `F²` | **one `F`-line**, `(a : b) = (B_e : −A_e)`, with `A_e/B_e = (q²+1)²/(q⁴+1)` — q-dependent, never `f(q)·(rational pair)` |
| **ℚ(q)** | `dim_F = 3` | `dim_F = 3` — **vacuous** |

Every cell is a sympy identity in the probe. The bottom row is the leg #7118 asked about, and the answer is that **it has no content**: the equation has codimension one for *every* nonzero element, and `(a, b) = (h/A, 0)` makes any trace bar-odd by fiat — `bar(h) = −h`. "Bar-odd under some ℚ(q)-rescaling" is true of everything.

So the leg only means something once the coefficient parity is restricted, and the physically motivated restriction is the middle row: a **bar-even coefficient is one that is itself p↔n neutral**, so a combination with `a, b ∈ F` is a functional whose *normalisation* does not carry isospin. That this is the right restriction is an interpretive choice, stated here rather than derived (§5).

On that row the two elements separate exactly as #7118 found over ℚ, but with a sharper statement for `Δ_L`: it admits **exactly one** bar-odd functional (up to `F`-scaling), and it is a genuinely q-dependent mixture of the two admissible traces.

## 3. That unique functional is not a Markov trace

Normalising `ε(1) = a + b = 1` on the line gives closed forms:

```
a = −(q⁴ + 1) / (2q²),      b = (q² + 1)² / (2q²),      a + b = 1 .
```

At the proton pin `(a, b) = (−1.0219, +2.0219)` — a negative weight on the augmentation.

A mixture `a·tr_q + b·tr_{z_D}` with `ab ≠ 0` is a trace functional (linear, cyclic, and it kills the `(1³)` block since both constituents do) — but the Markov property at two levels, `ε(σ₁) = z'·ε(1)` and `ε(σ₁σ₂) = z'·ε(σ₁)`, forces

```
(aq + b z_D)² = (a + b)(aq² + b z_D²)     ⟺     ab·(q − z_D)² = 0 ,
```

so no `z'` exists. The unique bar-odd functional on `Δ_L` over `F` sits **outside the Markov family** — it is Option-G territory in the [decision doc](2026-09-05-qbeta-functional-decision-options.md) (a non-Markov admissible functional), not a point of the family D7 rules on.

Its readout, recorded as a diagnostic and **not proposed**: `Q_β[ε_odd, Δ_L] = 0.22356 MeV`, −71.42 % against AME. Under §NO FITTING a number this far off is neither for nor against anything; it is what the construction gives.

**Scope.** Combined with #7118: over ℚ, `Δ_L` has no bar-odd admissible trace; over `F`, it has no bar-odd *Markov* trace; over ℚ(q) the criterion says nothing. `Δ_S` is bar-odd on the whole span in every row. This remains an exclusion *within the admissible span* — scope-(a) outside it — and rests on the same premise as #7118 (bar is p↔n conjugation, `qou-e58e`).

## 4. Correcting #7118 §5 — the reference was not truncated; the witness's own reference was rounded

#7118 §5 reported *"an 8-significant-figure reference in a corpus that computes at 60 dps"*, from `codata_constants.Q_BETA_MEV = 0.78233341` differing from the fork-pricing witness's implied reference `0.7823334093099085` by `8.8e-10`. Measured, the diagnosis runs the other way:

- **`Q_BETA_MEV = 0.78233341(61)` is σ-limited, not truncated.** AME-2020 quotes the value to `σ/6`; `codata_2022_source.py` says so at the literal ("stored at the σ-limited precision"). A truncated value would carry digits below σ — this one does not have them to carry.
- **The witness's reference is `qou_substrate.constants.Q_NEUTRON_MEV = M_N_MEV − M_P_MEV − M_E_MEV`, evaluated in float64**, and its `M_N_MEV` is the AME-*derived* literal `939.56542179` — which is `M_P + M_E + Q_β = 939.56542179069` **rounded to 8 decimals**, dropping `0.69e-9 MeV`. That dropped rounding is the whole `8.8e-10` (`0.69e-9 / 0.78233341 = 8.82e-10`, matching the recorded figure). The witness's reference is the *degraded* one, and it is the one on a float64 path.
- **The registry does carry a more precise neutron–proton difference — from a different dataset.** `neutron-proton mass difference energy equivalent in MeV = 1.29333251(38)` (CODATA 2022) gives `Q_β = 0.78233355931(38)`: **+191 ppb** above AME, `0.2σ` combined — consistent, and not the same measurement. `Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT` in `codata_2022_source.py` already computes exactly this value; its docstring quoted the CODATA-2018-proton figures (`0.78233482931`, "1810 ppb") and is corrected in this PR.

So the "fix Q_BETA_MEV" half of bean `qou-0e2p` dissolves into two different things: a **float64 defect** in `qou_substrate.constants.Q_NEUTRON_MEV` (a precision fix, exemption 1 of the 2026-09-07 directive, not made here because that module is `tools/qou-substrate`'s and its `M_N_MEV`/`M_P_MEV`/`M_E_MEV` are all floats — the fix is the module's, not one line), and a **dataset choice** — below.

## 5. What is put to the owner — the CAL-3 dataset

**The decision.** Whether `Q_β` (the CAL-2 proxy, carried as `codata_constants.Q_BETA_MEV` via `cal-3-q-beta.witness.json`) should come from AME-2020's direct value `0.78233341(61)` or from the CODATA-2022 registry's neutron–proton difference, `0.78233355931(38)`. The 2026-08-22 muon ruling's reason — *CAL-1, CAL-2 and CAL-3 must come from one experimental dataset* — and #7069's "derive, don't choose" both point at the registry; the blast radius is why it is asked rather than done.

**Option 1 — keep AME-2020 (the default; nothing changes).** What it means: `Q_BETA_MEV` stays `0.78233341(61)`, sourced from AME's own Q-value measurement. Costs nothing. Risks: CAL-2's proxy sits in a different dataset from CAL-1 (`m_e`, CODATA 2022) and the proton pin, which is the inconsistency the muon ruling excluded. Commits to: nothing; the registry value stays available as `Q_BETA_MEV_DERIVED_FROM_CODATA_DIRECT` for comparison.

**Option 2 — derive `Q_BETA_MEV` from the registry (CODATA 2022 `m_n − m_p` minus `m_e`).** What it means: `build_cal_3_q_beta_witness.py` reads `qou_substrate.codata` instead of the AME literal, as the α_EM producers did in #7069; the witness carries `0.78233355931(38)`. Costs: one producer edit, one witness regenerated, and the **116 `computations/` files** that read `Q_BETA_MEV` or the CAL-3 witness go stale by +191 ppb. Risks — the physics ones: every `c₃` extraction moves by `Δc₃ ≈ (ΔQ/Q)/u³ = +0.309` (≈ **15 %** of `c₃ ≈ −2.069`, through the `1/u³` ladder-extraction amplification), so the `c₃ ≈ −2 = J_Hopf(q=1)` near-match (3.47 %) and the `S_leak`, `q*_S`, N=4→N=5 non-monotonicity story built on it all move; the `Q_β` row of the L2 dashboard moves by 191 ppb against a 7.8 ppb target; `m_n = m_p + m_e + Q_β` moves by 0.16 ppb (and then agrees with CODATA-direct `m_n` exactly, by construction). Reversible (one commit). Commits to: CODATA 2022 as the single dataset, which is the standing ruling for the other two calibrations.

**Recommendation (judgement, not finding):** Option 2, because the owner has already ruled for one dataset and the c₃-ladder is convention-C-frame and awaiting re-derivation anyway (`qou-cds1`), so the 15 % move lands on numbers already scoped as provisional. But it is a 116-file change that the 2026-09-07 directive says to ask about, so it waits.

## 6. What was NOT done

- **No `Q_BETA_MEV` change**, no producer re-run, no witness regenerated besides the new probe's own — §5.
- **No fix to `qou_substrate.constants` floats** — recorded in the bean; it is that module's arc.
- **No claim that bar-even coefficients are *the* restriction.** That is the interpretive step; the ℚ(q) vacuity and the `F`-line are identities regardless.
- **`n = 3` only** (`H_3`, the algebra D7 names for the decay channel); nothing for general `n`. ORDER-ZERO-ONLY on the tower ruling.

-- Ref: [manuscript] beans qou-0e2p, qou-99qc, qou-e58e, qou-cds1; PRs #7118, #7115, #7069
