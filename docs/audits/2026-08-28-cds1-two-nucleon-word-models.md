# Two nucleon-word models are both called Δ — and the D-frame trace baseline is priced across them

Bean: `qou-cds1` (S1, the Q_β `c_k` ladder re-derivation under convention D).
Probe: [`computations/qbeta/qbeta_delta_element_fork_pricing_probe.py`](../../computations/qbeta/qbeta_delta_element_fork_pricing_probe.py), 15/15, exact symbolic ℚ(q), no float64.
Witness: `computations/qbeta/qbeta-delta-element-fork-pricing.witness.json`.

**Scope-(a) throughout.** Nothing here is refuted, no `c_k` is proposed, no
value is wired, and which model is canonical is *not* decided. What is
established is which corpus statement holds of which element, and what each
model prices at on its own.

## The finding in one line

The corpus's Q_β chain names one object, `Δ = NF(n) − NF(p)`, and **two
different elements of `H_3(q)` answer to the description**. Both of the closed
forms in [`qbeta-counit-closed-form.md`](../../content/quantum-observable-universe/nuclear-interactions/qbeta-counit-closed-form.md)
hold for the smaller one and **fail** for the larger one — and
`qbeta_d_frame_trace_baseline_probe` takes its baseline from the first and its
Markov trace from the second.

## The two models

| | Δ_S — the SHORT model | Δ_L — the LONG model |
|---|---|---|
| source | `deuteron-binding-dressing-proton-net.md`: `net(p) = 1 − h/2`, `net(n) = 1 − 3h/2 + h²/2` | `hecke_core._PROTON_G0/_G1`, `_NEUTRON_G0/_G1` |
| crossings | 1 (proton), 2 (neutron) | **11** each |
| reduced | `(h²/2, −h/2, −h/2, 0, 0, 0)` | `(−h/2, −h²/4, −h²/4, −h(q⁴+1)/(4q²), 0, 0)` |
| `net(Δ)` | `h²/2 − h` = `epsNPq` = **−0.187207** | **−0.233198** |
| `tr_M^z(Δ)` | `h²/2 − h·z` (**affine in z**) | **quadratic in z** |
| `χ^(2,1)(Δ)` | **0**, identically | −0.106814 |

Δ_S's crossing count is *derived*, not assumed: a typed crossing `(σ_g + d)`
has `net = 1 + d`, and `net` is multiplicative across **distinct** generators,
so `net(n) = (1 − h/2)(1 − h)` — an exact factorisation the probe checks — is a
1-crossing proton and a 2-crossing neutron. Δ_L's count of 11 is what
`hecke_core` stores, and matches
[`q-beta-c3-hopf-three-fold-markov.md`](../../content/quantum-observable-universe/mass-theory/q-beta-c3-hopf-three-fold-markov.md)'s
statement that the construction uses *"proton uud / neutron udd, both 11 typed
crossings"*.

**The mechanism, exactly.** `net` is multiplicative across distinct generators
but **not within one**, because `T_0² = h·T_0 + 1` reduces:
`net(T_0²) = 1 + h` while `net(T_0)² = 1`. So adding same-generator crossings
moves `net`, and an 11-crossing word cannot carry a 1-crossing coefficient.
This is why the mismatch is structural rather than a slip.

**Calibration, run before anything was concluded.** Δ_L reproduces all three
`χ^λ` in the committed `qbeta-d-frame-trace-baseline.witness.json` to
`6.1e-50`. So Δ_L *is* the element that probe traces — not a lookalike.

## Consequence 1 — the published pricing is mixed

`qbeta_d_frame_trace_baseline_probe` hard-codes `eps = h**2/2 - h` (that is
Δ_S) and computes `chi_all_lambda` from the 11-crossing words (that is Δ_L).
Its committed `gap_over_ladder_ratio = 92.1058…` is reproduced here **exactly**,
which is what confirms the attribution.

| | ratio to the ladder's own 0.1678 % move |
|---|---|
| published, **mixed** (counit Δ_S / trace Δ_L) | 92.106× |
| consistent on Δ_S — the element `Q_A` is built from | **257.260×** |

The published figure **understates** the gap by **2.793×**. Per the owner's
2026-08-26 correction this is not a reason to leave the re-derivation undone —
it changes the *expectation set on it*, in the harder direction.

Per-functional prices (MeV, error vs CODATA `Q_β = 0.7823334093`):

```
  short/net              0.783645827375     +0.16776 %   <- Q_A, the ladder's baseline
  short/augmentation     0.879890561260    +12.470   %
  short/tr_M_zC          0.345489779235    -55.839   %
  short/tr_M_zD          0.444700408522    -43.157   %
  long/net               0.976161273530    +24.776   %
  long/augmentation      1.089977815770    +39.324   %
  long/tr_M_zC           0.594714571668    -23.982   %
  long/tr_M_zD           0.661452049276    -15.451   %   <- the published -15.451 %
```

## Consequence 2 — the phase identity is short-model-specific

This matters more than the number. `qou-cds1` records as **(D1)** the identity

    2·α(z) = net(Δ) − tr_M^z(Δ),      α = (z−1)h/2

and reads it as the derivation of the ladder phase — *"α is neither free nor
fitted: it IS the discrepancy"*. It is **affine in z**, and it is affine
because Δ_S is supported only on `{γ, σ₀, σ₁}`, where `net − tr_M^z` takes the
values `0, 1−z, 1−z`.

Δ_L is supported on `L₊` as well, where the Ocneanu trace is `z²`. On Δ_L the
same difference is **quadratic in z**, so `α = (z−1)h/2` is not the
counit-minus-trace gap there at all.

**So the ladder phase being a linear function of the Markov parameter — the
property that makes the C→D move look like a substitution in the first place —
is a fact about the short model, not about the 11-crossing nucleon words the
corpus names.**

## What this means for the D-frame re-derivation

The re-derivation cannot be *posed*, let alone done, until the model is
settled, and the two answers send it to different places:

- **If Δ_S is canonical.** The phase leg is derived — (D1) holds identically in
  `z`, so `α_D` follows, and the bar-odd projection `α_D − h²/4` and the forced
  D weights apply as `qou-cds1` records. The D price is **257×**, not 92×. What
  remains is the `c_k` assembly, still anti-fit fenced.
- **If Δ_L is canonical.** (D1) is unavailable — the only derivation of `α` the
  corpus has does not hold of this element — and with the α-trichotomy's
  branch 1 closed in full (`BraidImageEigenphaseAlgebraic.lean`) and branch 2
  circular, **branch 3 (KZ / Kohno–Drinfeld holonomy) is the only remaining
  place a derivation of `α` can live**, exactly as the bean already says. Also
  `χ^(2,1)(Δ_L) ≠ 0`, so "the phase is blind to the 2-dimensional block" and
  the `net(dC) = −h·y_(2,1)(1)` floor would both need restating.

This is a *narrowing*, not progress toward a number: it says the choice of
element is load-bearing for the phase leg, and nobody has made it.

## Relation to `qou-avt6` / `qou-goc9` (PR #5893) — complementary, not overlapping

`qou-avt6` proves (scope-(b), norm form on `ℤ[√2]`) that no typed-crossing word
difference has **augmentation** `h²/2 − h`, and PR #5893 sharpens that fork by
showing the live typed counit survives the same invariant.

That whole line is about the **augmentation** (`σ ↦ q`, an algebra map). This
audit is about the **coordinate sum** `net` (`T_w ↦ 1`), which is the
functional `epsNPq` actually is (`qou-99qc`) and the one `Q_A` is computed
from. Under `net` the element does exist — it is Δ_S. Neither result implies
the other, and the probe states this in its docstring so the two are not later
merged by a reader.

## Flagged, NOT claimed — a possible third model

`pyhecke.atom.PROTON_NF` / `NEUTRON_NF` are 6-vectors whose coordinate sums are
`0.999125` and `0.810835`, difference **−0.188291** — within 0.58 % of
`epsNPq = −0.187207`, and matching neither Δ_S (−0.187207 exactly) nor Δ_L
(−0.233198).

**This is an observation, not a finding.** Those constants are stored float64,
and I did **not** verify that `pyhecke` uses the same basis ordering, so the
coordinate sum may not be `net`. Recorded so the next agent has the pointer;
resolving it needs the basis convention checked first. Bean `qou-bg3w`.

## Verification

CI is `workflow_dispatch`-only and Copilot review does not arrive
(`qou-gwe9`), so the agent's own verification is the gate.

- Probe **15/15**. All arithmetic is exact: sympy over ℚ(q), substitution
  `q → q₀` as an exact `Rational`, handed to mpmath through a 60-digit decimal
  string. No Python float is used in any computation.
- The reduction runs in the corpus's **own** 6-dimensional regular
  representation, imported from `qbeta_net_trace_invariance_probe`, whose
  committed controls (augmentation and regular character cyclic on all 36
  ordered basis pairs) validate the multiplication table.
- Two calibrations were run *before* any conclusion: the `χ^λ(Δ_L)` match to
  the committed trace witness (`6.1e-50`), and the exact reproduction of the
  published `92.1058…` ratio.
- `scripts/precision-gates.sh --changed` reports RED on **`import-time dps
  ratchet`** and **`audits-tree raw-float64`**. Both are **pre-existing on
  `origin/main` and not from this branch**, established by the decisive test
  rather than asserted: with this branch's two files moved out of the tree the
  import-time audit still reports the same single NEW file
  (`computations/audits/y_lambda_two_row_cap_gate.py`, not mine); restoring
  them leaves it at **1 NEW / 0 REGRESSED**. The audits-tree gate scans
  `docs/audits` witnesses, and this branch adds none.

## What was NOT done

No `c_k` derived or proposed. No convention-C site migrated. `−974` remains a
sensitivity measurement, wired nowhere. `qou-cds1` stays **open**.
