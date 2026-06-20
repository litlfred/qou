# Aufbau ℓ-grading — does the eigenvalue split derive penetration?

**Date.** 2026-06-20.
**Probe.** [`computations/aufbau_ell_grading_from_eigensplit.py`](https://github.com/litlfred/qou/blob/claude/amazing-fermat-35cgc9/computations/aufbau_ell_grading_from_eigensplit.py)
→ witness `computations/aufbau-ell-grading-from-eigensplit.witness.json`.
**Discipline.** Formalize-first (prediction committed before the run);
no fitting.

## Context — two periodic-table gaps

| | gap | prior status |
|---|---|---|
| **Capacity** `2n²` | Gap 1 | essentially solved — the electron–nucleus transfer matrix `T_{γe}` (tr `= q − q⁻¹`, det `= −1`) has eigenvalues `λ_+ = q`, `λ_- = −1/q`; sub-shell `ℓ` counts the angular components in the **sub-dominant** `λ_-`, giving capacity `2(2ℓ+1)` and `Σ_{ℓ<n} 2(2ℓ+1) = 2n²` (content: [`shell-eigenvalue-properties.md`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/predicted-spectra/shell-eigenvalue-properties.md)) |
| **Ordering** (noble gases) | Gap 2 | a prior probe showed the **bare `T_ee`** crossing (same `σ` for every orbital, ℓ-independent) gives **no ℓ-splitting** → closed shells stay at the pure-`2n²` set `[2,10,28,60]` (Ni, Nd), **not** the noble gases `[2,10,18,36]` (Ar, Kr). The missing ingredient was localized as **ℓ-penetration** (screening that *rises* with ℓ). |

## The question

Does the orbital's **own** angular structure — the `ℓ` components already
sitting in `λ_-` (the *same* split that yields the capacity) — modulate the
filling energy by `ℓ`, **deriving** penetration instead of inserting a
fitted `c·ℓ`?

The zero-parameter structural energy of sub-shell `(n,ℓ)` is the
log-magnitude of its transfer weight (`n` factors, `ℓ` sub-dominant):

```
ln|W(n,ℓ)| = (n−ℓ) ln λ_+ + ℓ ln|λ_-| = (n−ℓ) ln q + ℓ ln(1/q) = (n − 2ℓ) ln q
```

so the induced **filling key** is the linear form `K(n,ℓ) = n − 2ℓ`, whose
ℓ-coefficient `a = −2` is **fixed** by the single ratio
`|λ_-|/λ_+ = 1/q₀² ≈ 0.8117`. No free parameter.

## Formalize-first prediction (committed before running)

Madelung order is the linear form `n + ℓ` (ℓ-coefficient `+1`). The
structural key `n − 2ℓ` has ℓ-coefficient `−2`: **opposite sign**. They are
independent linear forms; no overall sign/scale choice maps one to the
other. ⇒ the eigenvalue split alone must give the **wrong-sign** ℓ-grading
and cannot reproduce the noble gases.

## Result — prediction confirmed

The decisive, *analytic* discriminator is the **3d-vs-4s crossover**: the
post-`np` gap that produces Ar = 18 and Kr = 36 exists **iff** the
higher-ℓ sub-shell `(n,2)` is pushed *above* `(n+1,0)`:

```
K(n,2) − K(n+1,0) = 2a − 1 > 0   ⇔   a > 1/2.
```

| model | ℓ-coeff `a` | fill order (first 10) | `2a−1` | closures |
|---|---:|---|---:|---|
| hydrogenic (bare `T_ee`) | `0` | 1s 2s 2p 3s 3p 3d 4s 4p 4d 4f | `−1` | `[2,10,28,60]` (pure-`2n²`) |
| Madelung reference | `+1` | 1s 2s 2p 3s 3p **4s 3d** 4p 5s 4d | `+1` | noble-type order (4s before 3d) |
| **EIGENSPLIT structural** | `−2` | 7i 6h 5g 7h 4f 6g 3d 5f 7g 2p | `−5` | `[26,48,88]` — neither |

- **Bare `T_ee` (`a=0`) → `[2,10,28,60]`** — reconstructs the prior (lost)
  baseline.
- **Eigensplit (`a=−2`, zero-parameter) → wrong sign** (`2a−1 = −5 < 0`,
  i.e. 3d far *below* 4s): it pushes high-ℓ sub-shells to fill *earlier*,
  the exact opposite of penetration. **Prediction confirmed.**
- The crossover needs `a > 1/2` (positive, **tuned**); the fixed ratio
  `1/q₀²` gives `a = −2`, a distance of `2.5` in ℓ-coefficient units on the
  wrong side. Any positive `c·ℓ` reproducing `[2,10,18,36]` would be a
  **fit** (and Madelung is itself only approximate — Cr, Cu, Pd, La break
  it).

## What this settles (Gap-2 localization sharpened)

The `λ_+/λ_-` split is the right object for **capacity** but supplies an
**anti-penetration** ℓ-grading. Therefore **penetration is a *separate*
ℓ-graded `T_ee` coupling, not the dominant/sub-dominant eigenvalue split.**
The open question is correspondingly singular and structural:

> Where does an **ℓ-graded `T_ee` coupling with positive ℓ-coefficient**
> come from categorically — what makes a low-ℓ orbital couple *more*
> strongly to the inner core (penetrate) than a high-ℓ one, beyond the
> eigenvalue split that fixes capacity?

This is one structural input, not a separate many-body theory (the SDP
already supplies the free optimizer). The honest next probe is whether the
orbital's own `V_ℓ` angular block modulates the `T_ee` **Markov weight**
(closing-loop `[2ℓ+1]_q` rather than the bare `σ` eigenvalue) with the
correct sign — flagged in advance as a probe that **could also come out
null**.

## Status of the two periodic-table items

| | gap | verdict |
|---|---|---|
| **Capacity** `2n²` | Gap 1 | done — self-square `[n]_q² = Σ[2ℓ+1]_q` of one cosh-parity element |
| **Ordering** (noble gases) | Gap 2 | SDP optimizer free; eigenvalue split **does not** derive penetration (wrong-sign ℓ-grading, this probe); ℓ-penetration is the one remaining categorical input, now sign-localized |
