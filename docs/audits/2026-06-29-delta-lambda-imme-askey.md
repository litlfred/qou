# Δ_λ residual is degree-2 in isospin — the IMME, and its Askey home (2026-06-29)

**Branch:** `claude/delta-lambda-z-magnitude-mirror-2026-06-29` (PR #3104).
Follow-up to #3089 (merged). **Discipline:** formalize-first; Δ_λ gate (no fit);
tiered status. **Status:** structural characterization of the residual; near-match
tier; **not wired**.

## The question

#3089 split the canonical residual `log_{q₀} Δ_λ` into a bar-even leading term +
a bar-odd Z-correction, and measured the Z-correction (the writhe) on mirror
pairs (−1.34 at A=3, −1.77 at A=7). Two open questions remained: *what is the
full functional form?* and *is there a quadratic term?* (owner). The answer to
both is the **Isobaric Multiplet Mass Equation**.

## The IMME form

As a function of the isospin projection `T₃ = (Z−N)/2`, the residual is a
**degree-2 polynomial**:

$$ \log_{q_0}\Delta_\lambda(Z,N) \;=\; a(A) \;+\; b(A)\,T_3 \;+\; c(A)\,T_3^2 \;+\;\dots $$

This is the Wigner (1957) IMME shape. The three terms split across two parity
channels under the mirror `T₃ → −T₃`:

| term | parity | identity in #3089 / here | isolated by |
|---|---|---|---|
| `a(A)` (isoscalar) | **even** | the bar-even leading `q₀^(10A−5)` (A≤4) | `f(0)` |
| `b(A)·T₃` (linear) | **odd** | the bar-odd **writhe** Z-correction | mirror diff `f(+T₃)−f(−T₃) = 2b·T₃` |
| `c(A)·T₃²` (quadratic) | **even** | **new** — cancels in mirror pairs | triplet `f(1)+f(−1)−2f(0) = 2c` |

**Why mirror pairs only measured `b`:** the mirror difference cancels *both*
bar-even terms (`a` and `c·T₃²`) — proved exactly in #3089
(`mirror_baseline_cancels`) and refined here with the explicit quadratic
(`imme_mirror_diff`). The quadratic `c` is invisible to a pair and needs an
**isobaric triplet** (`T₃ = −1, 0, +1`).

## Measurement — the quadratic is real (isobaric triplets)

`delta_lambda_imme_triplet.py` computes triplets via the canonical Jones–Markov
binding (`binding_canonical.py`) and extracts `a, b, c` by the exact 3-point
formulae:

| triplet (A) | members (T₃ = −1, 0, +1) | a | b (linear) | c (raw, T=0-contam.) | **c (same-T, clean)** |
|---|---|---|---|---|---|
| 6 | ⁶He / ⁶Li / ⁶Be | 36.12 | −1.73 | −1.24 | **−0.11** |
| 8 | ⁸Li / ⁸Be / ⁸B | 41.67 | −1.80 | −3.44 | **−0.10** |

- **`b` (charge-asymmetry, linear)** ~saturates: −1.34 (A=3), −1.73 (A=6),
  −1.80 (A=8) — consistent across the #3089 mirror pairs and these triplets.
- **`c` (quadratic): the raw value is mostly T=0/T=1 contamination, not the
  IMME quadratic.** The raw `c` (−1.24 → −3.44, apparently "Coulomb-growing")
  used the **T=0** ground state at `T₃=0`. Correcting that member to its **T=1
  isobaric-analog state** (the same-T fix, §"Same-T resolution" below) collapses
  it: **c ≈ −0.10, small and A-INDEPENDENT** (−0.109 at A=6, −0.096 at A=8). The
  apparent growth was the Wigner-energy (T=0 vs T=1) splitting, ≈3.6 MeV (A=6) /
  16.6 MeV (A=8). So the genuine same-T quadratic is small relative to the linear
  `b` (≈−1.8): **the cleaned residual is linear-(writhe)-dominated.**

## Same-T resolution (the clean Wigner IMME)

A clean IMME needs three members of the **same** isospin `T`. The `T₃=0` ground
states (⁶Li, ⁸Be) are **T=0**; their **T=1** isobaric-analog states sit `E_x`
higher (measured: ⁶Li 0⁺ T=1 at **3.563 MeV**; ⁸Be 2⁺ T=1 at **16.626 MeV** —
J-matched to the `T₃=±1` ground states). Subtracting `E_x` corrects the `T₃=0`
member to T=1 (`E_x` are experimental inputs, **not** a fit). Result:

    c(same-T):  A=6 → −0.109,  A=8 → −0.096    (raw: −1.24, −3.44)

i.e. the quadratic nearly vanishes and stops growing. This is the honest
outcome: **the residual's dominant `T₃` structure is the bar-odd linear `b`
(the writhe); the genuine bar-even quadratic is a small, roughly constant
≈−0.1 correction** — consistent with real-nucleus IMME `c` (small vs `b`).
`b` itself (the writhe Z-correction) is untouched by this correction (the
`T₃=±1` members are unchanged).

## The Askey connection

Two orthogonal-polynomial structures, one per quantum number:

- **Body-order `n`.** The b-ladder `a(n+2) = 2cosh(10η₀)·a(n+1) − a(n)` (where
  the `10` is #3089's per-nucleon slope, `η₀ = log q₀`) is a **three-term
  recurrence** — continuous q-Hermite / Al-Salam–Chihara in the **Askey
  q-scheme** (the binding tower's q-Hermite / Rogers–Szegő / Hahn–Exton q-Bessel
  home, per `docs/coordination/2026-06-05-step9-binding-closure.md §7`). Solution
  `a(n) = A·q₀^{10n} + B·q₀^{−10n}`; the leading `q₀^(10A−5)` is the dominant
  mode.
- **Isospin `T₃`.** The IMME is the **degree-2 truncation in `T₃`** — Wigner's
  "charge-dependent forces are rank-≤2 isotensors" is the **Askey–Racah cutoff**.
  Formalized falsifiably as `imme_third_diff_zero`: the third finite difference
  of the residual vanishes (no `d·T₃³`), the testable identity a fourth multiplet
  member must satisfy.

## Lean (exact algebra, sorry-free)

`QOU/BraidKnot/DeltaLambdaIMME.lean` (generic `[CommRing R]`, all `ring`,
lean-direct exit 0):

| decl | statement |
|---|---|
| `imme_at_zero` | `imme a b c 0 = a` (isoscalar) |
| `imme_mirror_diff` | `imme T₃ − imme(−T₃) = 2·b·T₃` (mirror isolates `b`; refines #3089) |
| `imme_triplet_2nd_diff` | `imme 1 + imme(−1) − 2·imme 0 = 2·c` (triplet isolates `c`) |
| `imme_third_diff_zero` | `Δ³ imme = 0` (Askey–Racah / Wigner rank-≤2 truncation) |

## Witness provenance / main-side caveat

The `a, b, c` values were computed against `binding_canonical.py` as of the
#3089 merge. As of this PR's rebase, `binding_canonical` (deuteron and all
nuclei) **raises on current `main`** —
`chi_monotone_transfer.word_to_mpfr: unrecognised crossing (d=−0.10446)` — a
**pre-existing main regression** from the flavor-split δ landings (the p-n
color-weight was refined but this consumer was not updated to recognise the new
value). This branch touches neither `binding_canonical` nor
`chi_monotone_transfer`; the committed witness reflects the last-working δ. The
IMME *structure* (Lean algebra, parity bookkeeping, the same-T collapse of `c`)
is robust to small δ shifts; only the exact numerals would move once main's
binding path is repaired.

## Status / not done

- **Not wired** (near-match tier); no fit (Δ_λ gate). The IMME degree-2 *form*
  and the parity bookkeeping are the robust, Lean-proved content; the same-T
  measurement shows the genuine quadratic is small (≈−0.1) and the residual is
  linear-(writhe)-dominated.
- **Correction recorded:** an earlier draft read the raw `c` (−1.24 → −3.44) as a
  "Coulomb-growing quadratic." The same-T (IAS) fix supersedes that — it was
  T=0/T=1 contamination; the clean `c ≈ −0.1` is small and A-independent.
- Open: whether the small same-T `c ≈ −0.1` has a categorical origin; the
  geometric meaning of `b`'s slow growth (≈−1.3 → −1.8); extending the same-T
  triplet ladder (A=10, 12) to confirm `c` stays ≈ constant.
