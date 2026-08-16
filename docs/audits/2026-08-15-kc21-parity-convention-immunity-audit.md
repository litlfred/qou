# KC21's "structural parity is convention-immune": verified or asserted?

**Date:** 2026-08-15 · **Branch:** `claude/kc21-parity-immunity-audit-2026-08-15` ·
**Bean:** `qou-kc21im` · **PR:** #5123 ·
**Probe:** [`qbeta_kc21_parity_convention_immunity_probe.py`](../../computations/qbeta/qbeta_kc21_parity_convention_immunity_probe.py)
(witness [`qbeta-kc21-parity-convention-immunity.witness.json`](../../computations/qbeta/qbeta-kc21-parity-convention-immunity.witness.json),
12/12 assertions, exit 0, 60 dps, proton pin) ·
**Lean:** [`LadderParityReflection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderParityReflection.lean)
(`lean`-direct exit 0, sorry-free, no `sorryAx`) ·
**Tier:** scope-(a) provenance audit; no convention adjudicated; no `c_k`
wired; no value-layer tier changed.

## Verdict up front

**VERIFIED.** The parity is convention-immune, and this audit measured it
rather than restating it. It was **asserted** when PR #5107 added the sentence
— the `1/u³` half of that same sentence carried a measurement (swing ratio
D/C = 1.0052), the parity half carried none.

**Two corrections came with the verification**, and both matter more than the
confirmation does:

1. The statement is about **`Im S`**. The literal reading `S(−ε) = −S(ε)` of
   the full complex value is **false**.
2. The operative hypothesis is **real coefficients, not bar-oddness**. The
   parity therefore **is not evidence** that the channel carrying it is
   bar-odd — which is work the corpus has been letting it do.

## 1. What was claimed, and why it was not obvious

PR #5107 correctly split the c₃ record into a C-conditional value layer and a
structural layer, and wrote into the KC21 row (registry §9g):

> the structural parity statement (`S(−ε)=−S(ε)`) and the `1/u³` result are
> convention-immune

The doubt is specific. `c₃(q)` is not a convention-free object: it is *defined
by* an extractor whose `N=1` rung consumes the convention-C Markov parameter
(`α = (z−1)h/2`, [`qbeta_utils.py:124-125`](../../computations/qbeta/qbeta_utils.py)),
and the same `z_C` sits in the exact-series core
([`qbeta_ck_sseries_exact_rational.py:20,248`](../../computations/qbeta/qbeta_ck_sseries_exact_rational.py)).
Under D the extractor returns a numerically and structurally different
function — c₃ ≈ −974 rather than ≈ −2.07, rung convergence 58× → 1.12×.
**Parity of `f_C` does not transfer to `f_D` merely because both are spelled
`c₃`.**

The neighbouring immunity claims in the same audit were *checked*: the
anchor-swing mechanism and the entropy bound were shown immune **because their
inputs (`u`, `Q_A`, σ) are z-free**. The parity claim had no analogous
demonstration on record, and `S = h·D(ũ)` runs through the ladder that #5107
itself marks C-conditional in the same sentence.

## 2. Route 1 — re-derive the parity under D

Complexify the extractor and evaluate at `q = q₀ ± iε`.

**One trap worth recording.** `qbeta_utils` writes `Q_A` with
`mpfabs(q**2 - 2*q - 1)`. `abs` is real-valued and **not holomorphic**, so a
complex-ε probe that keeps it silently tests a different function. At
`q₀ ≈ 1.11` the argument is `−1.9879 < 0`, so the analytic continuation is the
**signed** form `(2q+1−q²)` — which is what the exact-series ladder already
uses. Assertion A2 pins this.

| assertion | result |
|---|---|
| A1 regression — complexified extractor at `ε = 0` reproduces the corpus | `c₃^C(q₀) = −2.06934258`; relerr vs `qbeta_utils` **1.7e-60**, absdiff vs committed **2.9e-9** (the committed value's own rounding) |
| A3 `ε`-parity under **C** | `Im` odd and `Re` even, worst relerr **0.0**, over `ε ∈ [10⁻³⁰, 10⁻²]` |
| **A4 `ε`-parity under D** | `Im` odd and `Re` even, worst relerr **0.0**, same eight decades |
| A5 non-vacuity | `Im c₃^D(q₀ + 10⁻⁸i) = 0.0385845 ≠ 0` — A4 is not `0 = −0` |
| A6 the frames are genuinely different functions | `c₃^D(q₀) = −974.4319` vs `c₃^C(q₀) = −2.0693`; gap **972.36 = 469.9× \|c₃^C\|** |
| A7 `Im` vanishes at real substrate, both frames | `0.0` (the `fig8Trace_im_real_zero` analogue) |

The eight-decade sweep is deliberate: a parity that held only at linear order
in `ε` would break at the `10⁻²` end. It does not.

## 3. Route 2 — the reduction, which is stronger than "z-free"

The bean asked for a chain showing "no z-bearing input intervenes". The honest
chain is slightly different, and better: **`z` does intervene — it just cannot
matter.**

The parity is **Schwarz reflection**. A function holomorphic on a
conjugate-symmetric neighbourhood of a real interval and real-valued on that
interval satisfies `f(conj q) = conj f(q)`; writing `q = q₀ + iε` gives `Re`
even and `Im` odd immediately. The property is closed under `+`, `−`, `×`, `÷`,
composition, `√` on the principal branch away from the cut, and `cos`.

| A8 — Schwarz reflection `f(conj q) = conj f(q)`, worst relerr over a grid |
|---|
| `h`, `ℏ_q`, `b`, `u`, `Q_A(signed)`, `z_C`, `z_D`, `z_X`, `cos` — **all 0.0** |

So the composite ladder is reflective, and the **only** thing the argument
reads about the Markov parameter is that it is real-valued on the real
q-axis. It never reads `z`'s formula. Two consequences:

- **A9** — `z_D`'s reflection is *exact*, verified symbolically in sympy: it
  is a rational function with rational coefficients.
- **A10 (the decisive one)** — a control convention `z_X = q/(1+q²)`, which
  appears in **no channel of the corpus**, has the parity too. The immunity is
  a property of the *class*, not a coincidence of the two registered
  conventions.

### 3a. Formalized

[`LadderParityReflection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/LadderParityReflection.lean)
isolates `Reflective f : ∀ z, f (conj z) = conj (f z)`, derives
`reflective_im_odd` / `reflective_re_even` / `reflective_im_real_zero` from it
alone, and proves closure under add/sub/mul/neg/inv/div/pow/comp and real
constants. The payoff is quantified over conventions:

```lean
theorem alphaPhase_im_odd_of_reflective_markov {zf : ℂ → ℂ} (hz : Reflective zf)
    (q0 eps : ℝ) :
    (alphaPhase zf ⟨q0, -eps⟩).im = -(alphaPhase zf ⟨q0, eps⟩).im
```

*Any* reflective Markov parameter gives the parity. `zD_reflective` discharges
the D instance concretely. The C instance needs the principal `√` branch,
outside that file's algebraic scope, so it is measured at 60 dps (A8) rather
than proved — stated as such in the module docstring.

**A future convention can only break this by supplying a `z` that is not
real-valued on the real q-axis** (an explicit `i`), or that drags a branch
point or pole into the disc used. Neither C nor D does: `z_C`'s branch point
is at `q = 0`, `z_D`'s poles at `q = ±i`, both far from `q₀ ≈ 1.11`.

## 4. Correction 1 — the literal statement is false

`S(−ε) = −S(ε)`, read of the full complex value, requires `Re S` to be both
even and its own negation, i.e. zero. It is not: **A12** measures
`Re S = −0.0394593` at the proton pin (the corpus's own `S(proton) = −0.03946`),
and `|S(−ε) − (−S(ε))| = 0.0789`.

The true statement — and the one `fig8Trace_im_odd` actually proves — is about
the **imaginary part / decay projection**:
`Im S(q₀ − iε) = −Im S(q₀ + iε)`. The registry now writes `Im S`.
`reflective_re_even` is in the Lean file precisely to make the failure of the
literal reading a theorem rather than a remark.

## 5. Correction 2 — the parity is not evidence for bar-oddness

This is the finding with downstream consequences.

KC21 and the [capstone](2026-07-12-c3-wall-resolution-capstone.md) both derive
the parity as:

> `S` is bar-odd under `σ: q ↦ q⁻¹`; with `q = q₀+iε`, `S(−ε) = −S(ε)`, so
> `sign S = sign ε`.

**That is not the implication the Lean proves.** Read
[`ImQDecayLinearResponse.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ImQDecayLinearResponse.lean):
the chain is `fig8TraceC_conj` (*real integer coefficients* ⇒ conjugation
commutes with evaluation) ⇒ `fig8Trace_im_odd`. Bar-oddness is never used. The
hypothesis is real-analyticity; `σ: q ↦ q⁻¹` does not appear.

Measured consequence (**A11**): the manifestly bar-**even** `Q_A` has the
*identical* `ε`-parity, worst relerr 0.0. Every real-analytic ingredient of the
ladder has it. So observing `Im` odd in `ε` **does not discriminate the bar-odd
channel** — it is a property of the whole ladder, bar-odd parts and bar-even
parts alike.

The immunity conclusion is unaffected (if anything it is broader: it holds for
ingredients regardless of bar parity). What is affected is the *evidential
weight* the corpus has attached to the parity. "The sign-flip is structural,
not a fit, because `S` is bar-odd" should read "…because `S` is real-analytic
in `q`" — which is a much weaker premise, satisfied by essentially everything
in the ladder, and correspondingly says much less about which channel `S`
lives in.

## 6. What this does NOT do

Three explicit non-doings, because the neighbouring questions are live:

1. **No convention is adjudicated for the Q_β channel.** Bean `qou-b3nk` is
   unchanged: whether the mass-channel two-row forcing transfers to the decay
   channel (whose explicit weight instance has `y_(1³) ≠ 0`) is still open, and
   the channel is still unregistered in
   [`trace-convention-registry.json`](../coordination/trace-convention-registry.json).
2. **No C-conditional value is revived.** c₃, (H1) `c₃^even = −Vol(4₁)`,
   `[3]_q/25`, `J−ℏ²`, `S_leak`, `q*_S` all remain C-conditional per §9g. Per
   §"Defined residual ≠ derived decomposition", `S = c₃ + Vol(4₁)` is a
   residual of a C-frame extraction and nothing here upgrades it.
3. **The bar involution is untouched.** `σ: q ↦ q⁻¹` is a *different*
   involution from complex conjugation. `bar(z_D) = q⁻⁴·z_D` (§9g) and the
   `z_C` full-bar-condition failure (`MarkovZFullBarCondition.lean`, PR #5111,
   not yet on `main`) stand exactly as stated. **The `h·D(ũ)` bar-split
   inherits none of the `ε`-parity's immunity** — that is a separate claim
   about a separate involution, and the bean's companion question (whether
   trace-derived quantities still carry clean *bar* parity now that `z_C` fails
   the full-bar condition) remains open. Correction 2 makes that question
   *more* pressing, not less: the `ε`-parity that was doing duty as evidence
   for the bar-odd reading turns out not to bear on it at all.

## 7. Adjacent findings (mechanical)

- **Drained a live precision red.** The NO-FLOAT64 ratchet listed **2** NEW
  dirty witnesses; both came from `"durationSec": round(...)` serializing a raw
  float64 — one in this branch's own probe, one left by PR #5107's
  `qbeta_c3_ladder_trace_convention_sensitivity_probe.py`. Both fixed at the
  producer and re-run; count is now **0**. No computed number changed (that
  probe's 9/9 still pass).
- **Left standing, and not from this branch:**
  `computations/rho-k-co-casimir-extended.witness.json` REGRESSED 3 → 4 raw
  float64 fields. Pre-existing on `main`, different domain (Δ_λ co-Casimir).
- **q0-drift audit count moved** 776 → 781 proton-pin fields (the new and
  regenerated witnesses, both correctly recording `q0Anchor: "proton"`).
  `STALE` unchanged at 317, below its 329 baseline.
- **Registry validator**: 22 rows, 0 errors, 9 warnings — byte-identical
  before and after this change (all nine are pre-existing KC2/KC3/KC4
  `_of_`-naming warnings in a `docs/scope/` file this branch does not touch).

## 8. Registry actions taken in this PR

- KC21 row (`.md` **and** JSON twin): immunity relabelled **VERIFIED** with
  both routes named; statement rewritten as `Im S`; the "bar-odd ⇒ odd in ε"
  reading superseded; `lean` field extended with `reflective_im_odd`,
  `alphaPhase_im_odd_of_reflective_markov`, `zD_reflective`.
- New **§9h** carrying the routes, the exact hypothesis, both corrections, and
  the three non-doings above.
- No tier flipped in either direction. KC21 stays `proved-lean`; the value
  layer stays C-conditional.
- Ledger row: [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).
