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

| triplet (A) | members (T₃ = −1, 0, +1) | a | b (linear) | **c (quadratic)** |
|---|---|---|---|---|
| 6 | ⁶He / ⁶Li / ⁶Be | 36.12 | −1.73 | **−1.24** |
| 8 | ⁸Li / ⁸Be / ⁸B | 41.67 | −1.80 | **−3.44** |

- **`b` (charge-asymmetry, linear)** ~saturates: −1.34 (A=3), −1.73 (A=6),
  −1.80 (A=8) — consistent across the #3089 mirror pairs and these triplets.
- **`c` (quadratic)** is nonzero and **grows fast** (−1.24 → −3.44), the
  signature of a Coulomb-energy-like term (the quadratic Coulomb scaling in `Z`).

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

## Honest caveat (same-T)

A clean Wigner IMME needs three members of the **same** isospin `T`. The
experimental ground states at `T₃ = 0` (⁶Li, ⁸Be) are **T=0**, while their
`T₃ = ±1` partners are **T=1** (the true T=1, T₃=0 analog is an excited state).
So the extracted `c` **mixes** the genuine IMME quadratic with the T=0/T=1
structure difference. The **robust, framework-level** claim is parity-clean: the
residual carries a **nonzero bar-even quadratic** component beyond leading +
linear, which mirror pairs structurally cannot see. A clean `c` would use
isobaric analog states (same `T`).

## Status / not done

- **Not wired** (near-match tier); no fit (Δ_λ gate); the quadratic is a measured
  structural feature, not a closure ansatz.
- Open: a same-T extraction of `c`; whether `c(A)` is exactly the categorical
  Coulomb period; the geometric origin of `b`'s saturation vs `c`'s growth.
