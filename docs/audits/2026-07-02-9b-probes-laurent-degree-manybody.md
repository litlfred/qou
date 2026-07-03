# 9b probes: Laurent-degree bookkeeping of the q₀^(10A−5) residual + exact many-body expansion of the Phase-5q closed form (2026-07-02)

**Status:** exploratory / derive-or-refute probes (owner-approved; beans
`drjk` + `iv3r`). **Nothing here is wired to production; no new constants
introduced** (Δ_λ gate: no seventh fit ansatz). Both verdicts are
**scope-(a) refutations** per the refutation-scope discipline — they
constrain the tested bookkeeping routes only; no structural exclusion is
claimed (no proved invariant).

| probe | script | witness | verdict |
|---|---|---|---|
| PROBE 1 (bean `drjk`) | [`probe_9b_laurent_degree_10a5.py`](../../computations/probe_9b_laurent_degree_10a5.py) | [`probe-9b-laurent-degree-10a5.witness.json`](../../computations/probe-9b-laurent-degree-10a5.witness.json) (11/11 assertions) | **REFUTED scope-(a)** — degree bookkeeping alone does not produce 10A−5 |
| PROBE 3 (bean `iv3r`) | [`probe_9b_manybody_expansion.py`](../../computations/probe_9b_manybody_expansion.py) | [`probe-9b-manybody-expansion.witness.json`](../../computations/probe-9b-manybody-expansion.witness.json) (10/10 assertions) | **REFUTED scope-(a)** — the exact 4-body cross-term is 34–184× below the magic-A value |

## Context

The trace-canonical binding baseline
([`binding_canonical.py`](../../computations/binding_canonical.py), per the
trace-convention reconciliation
[`2026-06-09-binding-trace-convention-split.md`](2026-06-09-binding-trace-convention-split.md))
is `B_pred = Q_β·(tr_M(W_free) − tr_M(W_atom))` on the Jones–Markov trace,
and its residual satisfies the near-integer law
`Δ_λ(K) = B_AME/B_pred ≈ q₀^(10A−5)`
([`2026-06-09-delta-lambda-canonical-residual.md`](2026-06-09-delta-lambda-canonical-residual.md):
D −0.01, T −0.07, ⁴He +0.27, ³He −1.40 q₀-units). The Phase-5q closed form
([`closed_form_tau_M.py`](../../computations/closed_form_tau_M.py)) gives
the exact factorization

```
tr_M(𝓑_K) = tr_M³(𝓑_p)^Z · tr_M³(𝓑_n)^N · ∏_i f_i(q)
f_pp = z,   f_nn = z − h,   f_pn = z − h·(1/2 − δ(q)/4)
z = 1/(√q + 1/√q),   h = q − q⁻¹,   δ(q) = (q−1)²(1−q⁻⁴)/3
```

(bring_color_weighted; δ is the **proven leading** flavor split — the
posited subleading was de-wired 2026-06-29). Scale note: the MeV
multiplier is `Q_β(n) ≈ 0.78233` MeV, the parameter `binding_canonical.py`
historically misnamed `E_0`; the separate scale `E_0 = m_e/(q₀(q₀−1)) ≈
4.186` MeV is used only in the PROBE-3 comparison columns because the
many-body-ceiling audit
([`2026-06-02-binding-many-body-ceiling.md`](2026-06-02-binding-many-body-ceiling.md))
quoted its pairwise bonds on that scale.

## Shared byproduct — the closed form is now verified as an EXACT identity

Both probes rest on the closed form, so PROBE 1 first hardened it beyond
the Phase-5q 1e-49 numeric validation:

- **Exact-ℚ identity (new):** the full symbolic H₆ (D) and H₉ (T)
  canonical Jones–Markov traces of the canonical atom words — with the
  p-n interface carried as the **exact rational** `−h·(1/2 − δ(q)/4)` —
  equal `tr_p^Z·tr_n^N·∏f_i` **exactly in ℚ** at rational points
  s = √q ∈ {3/2, 7/5} (differences cancel to literal 0). This is the
  first exact-arithmetic verification under the bring_color_weighted
  convention.
- **Transfer cross-check:** closed form vs the independent fine-Bratteli
  transfer path (`tr_m_atom_zn`) at q₀ agrees to ≤ 9.2e-20 on all four
  anchors (the residual is the f64-q₀-baked δ inside the canonical word
  vs the 50-digit δ(q₀) used by the probe; the free traces agree to
  ≤ 1.4e-49).
- **Exact symbolic nucleon traces:** `tr_p(q)`, `tr_n(q)` extracted as
  Laurent rationals in s = √q, bar-symmetric with degree range
  [−19, +19] in s (±9.5 in q); at q₀:
  `tr_p = 1.06531 = q₀^{+0.6063}`, `tr_n = 0.92323 = q₀^{−0.7655}`.

## PROBE 1 — Laurent-degree bookkeeping for 10A−5

**Hypothesis tested (not assumed):** `10A−5 = 5(2A−1) = 5·[A nucleons +
(A−1) interfaces]` — a per-block / per-interface q₀⁵ factorization that
should fall out of exact degree bookkeeping of the closed form.

### Exact degree / writhe bookkeeping (all exact integers or half-integers)

| atom | deg_q(1−∏f) [s→0, s→∞] | deg_q(Δtr) [s→0, s→∞] | e(W_atom)−e(W_free) | 10A−5 |
|---|---|---|---|---|
| D | [−5.0, 3.0] | [−24.0, 22.0] | 0 | 15 |
| T | [−6.0, 4.0] | [−34.5, 32.5] | −1 | 25 |
| ³He | [−4.5, 2.5] | [−33.0, 31.0] | +1 | 25 |
| ⁴He | [−5.5, 3.5] | [−43.5, 41.5] | 0 | 35 |

No exact Laurent degree of `Δtr = tr_free·(1−∏f)` — leading, lowest, or
their difference — has the form 10A−5 (the Δtr degree grows by
9.5/nucleon + interface increments, wrong slope and wrong offset), and
the writhe/exponent-sum difference is the interface sign census
`#pp − #nn ∈ {−1, 0, +1}`, nowhere near 10A−5.

### The 50-dps log_{q₀} decomposition (where the exponent actually lives)

`log_{q₀}Δ_λ = log_{q₀}(B_AME/Q_β) − log_{q₀}(tr_free) − log_{q₀}(1−∏f)`:

| atom | log(B_AME/Q_β) | −log tr_free | −log(1−∏f) | total | 10A−5 |
|---|---|---|---|---|---|
| D | 10.016 | 0.159 | 4.814 | 14.99 | 15 |
| T | 22.842 | 0.925 | 1.167 | 24.93 | 25 |
| ³He | 21.938 | −0.447 | 2.105 | 23.60 | 25 |
| ⁴He | 34.389 | 0.318 | 0.565 | 35.27 | 35 |

Per-nucleon increments (law demands +10 each):

| step | Δlog Δ_λ | B_AME-side | trace-side |
|---|---|---|---|
| D→T (+n, +nn) | +9.95 | +12.83 | −2.88 |
| D→³He (+p, +pp) | +8.61 | +11.92 | −3.32 |
| T→⁴He | +10.34 | +11.55 | −1.21 |
| ³He→⁴He | +11.68 | +12.45 | −0.77 |

**The refuting structure:** the closed form's entire trace-side
contribution (−log tr_free − log(1−∏f)) **shrinks** with A (4.97 at D →
0.88 at ⁴He) while the law grows by +10 per nucleon; the growth is
carried by the experimental `B_AME/Q_β` term, which the closed form does
not model. There is no per-block ≈5 and no per-interface ≈5 anywhere in
the exact factor structure (exponent dictionary: `log_{q₀}`: z = −6.66,
f_pp = −6.66, f_pn = −8.91, f_nn = −11.86, g_pp = −6.63, g_pn = −4.81,
g_nn = −3.29, tr_p = +0.61, tr_n = −0.77).

### Verdict (PROBE 1)

> **REFUTED — scope (a) only.** Leading-degree / writhe / interface
> bookkeeping of the Phase-5q closed form, **alone**, does not produce
> 10A−5. This constrains this bookkeeping route only; it does **not**
> structurally exclude a per-object q₀⁵ factor arising elsewhere in the
> chain (e.g. in the archimedean realization / energy-scale step) — no
> proved invariant, so no scope-(b) claim.

### Observation-tier residues (near-match, NOT derived, NOT wired)

1. **`h(q₀) = q₀^{−15.0002}`** — the Hecke skein parameter's q₀-exponent
   equals the deuteron law exponent 15 to 2e-4 relative, i.e.
   `Δ_λ(D) ≈ 1/h(q₀)`. A one-parameter near-integer fact about q₀
   (q − q⁻¹ ≈ q^{−15} at the substrate anchor); recorded as an anchor
   for any future derivation attempt, nothing more.
2. **The deuteron's clean 10+5 split** (B_AME-side 10.016 + trace-side
   4.97) is real at A=2 but does **not** persist (trace side → 0.88 at
   ⁴He) — so it cannot be the mechanism of the law.
3. **The ³He −1.40 outlier decomposes mechanically** (T vs ³He gap
   +1.338): p/n nucleon-trace asymmetry `−log(tr_n/tr_p)` = **+1.372**,
   interface-sign swap (nn↔pp census) = **−0.938**, AME mirror asymmetry
   = **+0.904**. Interface **signs alone do not** account for the
   outlier; the dominant single term is the p/n trace asymmetry
   `tr_n/tr_p = q₀^{−1.372}`, numerically close to (but not identified
   with) the −1.40 deviation.

## PROBE 3 — exact many-body expansion of the closed form

`ln tr_M = Z·ln tr_p + N·ln tr_n + Σ_i ln f_i` is exact, so with
`g_i := 1 − f_i` the binding defect has the exact finite
inclusion–exclusion expansion (no new constants)

```
B = Q_β · tr_free · [ Σ_i g_i − Σ_{i<j} g_i g_j + Σ_{i<j<k} g_i g_j g_k − … ]
```

whose order-k term touches k+1 nucleons when the chain interfaces are
consecutive (the ⁴He order-2 subset {pp, nn} is the disconnected
2+2-body term). At q₀: g_pp = 0.50068, g_pn = 0.60514, g_nn = 0.70974 —
**not small**, so the expansion is alternating and non-perturbative.
Orders sum exactly to B_pred (witness assertion at 1e-40).

| atom | order (bodies) | T_k (MeV, Q_β scale) | % of B_pred | % of B_AME @Q_β | % of B_AME @E_0 |
|---|---|---|---|---|---|
| D | 1 (2-body) | +0.46562 | +100.00% | +20.93% | +111.99% |
| T | 1 (2-body) | +0.93406 | +148.51% | +11.01% | +58.92% |
| T | 2 (3-body) | −0.30510 | −48.51% | −3.60% | −19.25% |
| ³He | 1 (2-body) | +0.90643 | +137.74% | +11.74% | +62.84% |
| ³He | 2 (3-body) | −0.24835 | −37.74% | −3.22% | −17.22% |
| ⁴He | 1 (2-body) | +1.37396 | +192.58% | +4.86% | **+25.98%** |
| ⁴He | 2 (3/4-body) | −0.82323 | −115.39% | −2.91% | −15.57% |
| ⁴He | 3 (4-body) | +0.16273 | +22.81% | +0.58% | +3.08% |

Consistency hook: the ⁴He order-1 (pairwise) fraction of B_AME at the
E_0 scale is **25.98%**, reproducing the many-body-ceiling audit's "26%
pairwise" figure — the two computations describe the same object.

### The ⁴He 4-body cross-term vs the magic-A value

| quantity | value |
|---|---|
| exact connected 4-body cross-term `+Q_β·tr_free·g_pp·g_pn·g_nn` | **0.1627 MeV** (Q_β scale) / **0.8707 MeV** (E_0 scale) |
| magic-A `2·m_e·A·8G = 2·m_e·4·8·Catalan` | **29.956 MeV** (+5.87% vs AME) |
| shortfall | **184×** @Q_β / **34×** @E_0 |

### Verdict (PROBE 3)

> **REFUTED — scope (a) only.** The multiplicative interface product of
> the Phase-5q closed form, **alone**, at either canonical scale, does
> not generate the 4-body α-cooperativity: its exact connected 4-body
> cross-term is 1.5–2.3 orders of magnitude below the magic-A value.
> Per the permanence principles, the probe **measures the size of the
> missing higher-order term** (≈ 20.9 MeV of ⁴He binding is not in the
> A−1-interface chain product at any expansion order); it does not
> exclude the closed-form factors from a larger closure.

## What this means for the step-9b gap

1. **The 10A−5 law is a property of B_AME relative to the closed-form
   baseline, not of the closed form itself.** Any categorical derivation
   must generate the +10/nucleon exponent in the step that the closed
   form does not model — the archimedean realization / energy-scale side
   — not in H_{3A} trace-degree bookkeeping. This sharpens the 9b-H1
   open item rather than closing it.
2. **The α-cooperativity is likewise outside the interface chain
   product** at every exact order — consistent with, and now exactly
   quantified against, the many-body-ceiling audit and the magic-A
   formula.
3. Both refutations are **(a)-scoped**: the closed form remains an exact,
   now ℚ-verified, permanent piece; the probes bound what it can supply,
   not what may be added to it.

---

## Follow-up (2026-07-03, owner request): h-power re-parametrization + p/n-asymmetry estimate

Probe: [`probe_9b_h_power_asymmetry.py`](../../computations/probe_9b_h_power_asymmetry.py)
(witness `probe-9b-h-power-asymmetry.witness.json`, 3/3 assertions; inputs read
from the PROBE 1 witness — **no new constants**, κ = log_q₀(tr_n/tr_p) is the
derived closed-form trace asymmetry).

**Exponent correction.** The h-form of the resolved `5(2A−1)` law is
`Δ_λ(K) ≈ h(q₀)^(−(2A−1)/3)` — the h-exponent carries the **1/3**
(since −log_q₀ h = 15.0002 = 3·5), not the bare `−(2A−1)`.

| model (log_q₀ units) | D | T | ³He | ⁴He |
|---|---:|---:|---:|---:|
| M0 law `10A−5` | +0.011 | +0.066 | **+1.404** | −0.272 |
| M1 h-form `−log_q₀h·(2A−1)/3` | +0.011 | +0.066 | +1.405 | −0.272 |
| M2 M1 + κ·(Z−N) | +0.011 | **+1.438** | +0.033 | −0.272 |
| M3 M1 + κ·[Z>N] | +0.011 | +0.066 | **+0.033** | −0.272 |

**Verdicts.** M2 (antisymmetric mirror application) **REFUTED scope-(a)** —
breaks T. M3 (proton-excess gate) **NEAR-MATCH, unwired**: collapses the ³He
outlier +1.40 → +0.033 with the derived κ, leaves D/T intact; ⁴He (−0.272,
Z = N so the gate cannot act) is now the dominant residual. The one-sided
gate is consistent with PROBE 1's mirror decomposition (interface-sign swap
−0.938 and AME mirror +0.904 nearly cancel, leaving the trace asymmetry on
the proton-excess side only) but is an **observation, not a derived rule** —
the open follow-up is derive-or-refute `[Z>N]` from the interface algebra,
and the ⁴He −0.272 residual.

---

## Gate derivation (cywi): the [Z>N] proton-excess gate is an A=3 near-cancellation, not a derived rule

Probe: [`probe_9b_gate_interface_algebra.py`](../../computations/probe_9b_gate_interface_algebra.py)
(witness `probe-9b-gate-interface-algebra.witness.json`, 10/10 assertions;
inputs: PROBE 1 witness traces + exact interface formulas + vendored
AME2020 — **no new constants**).

### Exact mirror decomposition (identity, ≤ 1e-30)

For a mirror pair (Z,N) vs (N,Z) with Z < N and the chain census
`(Z−1)·pp + 1·pn + (N−1)·nn`, the closed-form Δ_λ definition gives the
algebraic identity

$$
\log_{q_0}\Delta_\lambda(\text{n-rich}) - \log_{q_0}\Delta_\lambda(\text{p-rich})
= \underbrace{(N{-}Z)\log_{q_0}(\mathrm{tr}_p/\mathrm{tr}_n)}_{\text{asym} = -\kappa} \,+\,
\underbrace{\log_{q_0}\frac{1-P_{(N,Z)}}{1-P_{(Z,N)}}}_{\text{swap}} \,+\,
\underbrace{\log_{q_0}\frac{B_{\mathrm{AME}}(\text{n-rich})}{B_{\mathrm{AME}}(\text{p-rich})}}_{\text{mirror}},
\qquad P_{(Z,N)} = f_{pp}^{Z-1} f_{pn} f_{nn}^{N-1}.
$$

**Sign reconciliation of the earlier "0.06 gap".** PROBE 1's sum
1.372 − 0.938 + 0.904 = 1.338 is the T−³He **gap**, while the ³He
outlier +1.404 is its residual **against the law**; since both A=3
isobars share the law value 25, `res(³He) − res(T) = gap` exactly —
the "missing 0.066" is precisely **T's own law residual**, not a δ or
tr_free term (asserted to 1e-30).

### What the gate IS

M3 assigns the whole mirror gap to the trace asymmetry, so identically

> **gate exact ⟺ swap + mirror = 0**, and
> `res_M3(³He) − res_M3(T) = swap + mirror` (asserted ≤ 1e-30).

It is a **near-cancellation with computable residual, not an identity**:
swap is interface algebra at q₀, mirror is AME data, and nothing ties
them. At A=3: `swap + mirror = −0.938014 + 0.904360 = −0.033654`, which
is exactly the difference of the two M3 residuals (+0.0665 vs +0.0329).

### Generality: the cancellation is A=3-specific

| pair | A | asym | swap | mirror | swap+mirror | gap |
|---|---:|---:|---:|---:|---:|---:|
| T/³He | 3 | +1.3718 | −0.9380 | +0.9044 | **−0.0337** | 1.3382 |
| ⁵He/⁵Li† | 5 | +1.3718 | −0.1173 | +0.4376 | +0.3202 | 1.6921 |
| ⁷Li/⁷Be | 7 | +1.3718 | −0.0167 | +0.4102 | **+0.3935** | 1.7653 |

† particle-unstable pair — corroborating only; ⁷Li/⁷Be is the clean
bound-pair AME test.

1. The candidate A-independent factorization `swap = log g_pp − log g_nn
   = −3.344` is **false** (actual −0.938 at A=3): `1−∏f` does not factor
   over interfaces, so the swap term is A-dependent.
2. All three interface factors satisfy `0 < f < 1` at q₀ (f_pp ≈ 0.499,
   f_pn ≈ 0.395, f_nn ≈ 0.290, asserted), so `P_(Z,N) → 0` geometrically
   and **swap → 0 with A** — a *derived* property of the closed form.
3. The AME mirror term does **not** decay (+0.904 / +0.438 / +0.410), so
   `swap + mirror` cannot stay near 0: at ⁷Li/⁷Be it is +0.394, an order
   of magnitude above the A=3 residual −0.0337.

### Verdict (cywi)

> **"[Z>N] gate is a derived generic rule of the interface algebra":
> REFUTED — scope (a) ONLY.** The interface algebra, alone, supplies a
> swap term that decays geometrically with A while the experimental
> mirror term it must cancel stays O(0.4); the A=3 cancellation is a
> numerical coincidence of that one pair. This constrains the
> gate-as-rule reading only — it does not exclude the trace asymmetry κ
> from a larger closure (no proved invariant; scope-(b) not claimed).
> **M3 at A=3 remains NEAR-MATCH** with its residual now *stated
> exactly*: `swap + mirror = −0.0337 = res_M3(³He) − res_M3(T)`.
> Prediction for any heavier AME-testable mirror pair: the M3 gate
> over-corrects the p-rich member by ≈ `mirror(A)` (+0.39 at A=7).
