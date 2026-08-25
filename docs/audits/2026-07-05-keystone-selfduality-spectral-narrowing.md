# Keystone value step: self-duality narrows the eigenfunction class (the reframe that replaces node-value screens)

**Date:** 2026-07-05
**Branch:** `claude/gap-9b-1208-2521-bf2nc0`
**Bean:** s013 (keystone value-map)
**Lean:** [`QOU/BraidKnot/KeystoneSelfDualSpectralNarrowing.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneSelfDualSpectralNarrowing.lean) — verified lean-direct, exit 0, sorry-free.
**Follows:** [`2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md`](2026-07-04-keystone-qhankel-eq2-vacuum-row-sourced-refutation.md) (the last q-Bessel node screen).
**New source identified:** [`library/arxiv-math-9805023v1/9805023v1.pdf`](../../library/arxiv-math-9805023v1/9805023v1.pdf) (owner upload, commit `8e311cb`) — Ciccoli N., Koelink E., Koornwinder T.H., "q-Laguerre polynomials and big q-Bessel functions and their orthogonality relations", *Methods and Applications of Analysis* **6** (1999) 109–127, arXiv:math/9805023 (math.CA); bib key `[ciccolikoelinkkoornwinder1999]`.

## Two questions, answered

1. **Does 1208.2521 (Koornwinder–Swarttouw q-Hankel) help close Step-9b?** No. 9b's open legs
   (per-λ FR-projector weight `χ^λ·χ^λ(e_{K*})`, the bar-odd κ writhe correction, the IMME `Δ³=0`
   checks) are compact, algebraic (Laurent-polynomial) Hecke/Markov-trace objects; the q-Hankel
   transform is a non-compact E_q(2) Plancherel kernel. No mechanism connects them, and the
   compact/non-compact type argument (keystone FACT 1) says a hit would be coincidence. 1208.2521 is
   **keystone (s013)** material — the value-map redirect (ii) — not 9b.

2. **Does math/9805023 (big q-Bessel) help?** Not as a node screen — and that failure is *diagnostic*.
   The big q-Bessel discrete orthogonality is supported on `{c·q^k : k∈ℤ}` for **any** `c > 0`
   (math/9805023 §4). The scale `c` is a **free parameter**, so a "screen its nodes against `d_q`"
   test is not 0-dof — it is a fit, which the discipline forbids. The Hahn–Exton/q-Hankel roots
   (2026-07-04) were parameter-free and gave a clean scope-(a) refutation; big q-Bessel cannot even be
   put in that dock. **Do not run the node screen.**

## The reframe (owner, 2026-07-05): invert the search

Both node screens share a wrong frame: import an off-the-shelf orthogonal family, then test its values.
The owner's redirect: read off the orthogonality/eigen constraints the framework's **own** structure
imposes, and let them narrow the class of orthogonal eigenfunctions — *before* pattern-matching to any
named q-special function. Three ingredients, each a constraint (not an import):

| Ingredient | What it says about the orthogonality condition |
|---|---|
| **(A) Frobenius pairing** `tr_M = Σ_λ y_λ χ_λ` | The Markov trace is a Frobenius form; under it the characters `χ_λ` are orthogonal with the **quantum-dimension measure** `μ(λ)=d_q(λ)²/D²` (corpus `verlindeMeasure_eq_plancherel`), and `d_q(λ)/D = χ_λ(1)/D` is the vacuum overlap. The orthogonal system is *supplied*, not imported. |
| **(B) 𝐂-action / Verlinde** | `S` simultaneously diagonalises the fusion operators; `d_q` is the **unique Perron–Frobenius-positive** common eigenvector (Ocneanu; Wenzl — corpus `y-lambda-closed-form-wenzl-bridge`). |
| **(C) Self-duality** `S = Sᵀ`, `S² = C` (`C²=1`) | `S` is a **self-reciprocal** transform — the categorical avatar of the self-reciprocal q-Hankel transform. This is the **spectral duality** the geometric program was not using. |

math/9805023 is itself a spectral-duality statement ("dual orthogonality for big q-Bessel =
orthogonality for completed q-Laguerre") — two bases exchanged by `𝓗_q`. So the value-map target
`d_q` should be a **fixed point** of the self-dual transform, not an arbitrary node value.

## What is formalized (the (C) leg, sorry-free)

`KeystoneSelfDualSpectralNarrowing.lean`, over generic `{R : Type*} [CommRing R]` (§7c):

- `SelfDualSTransform` — bundles a symmetric `S`, a charge-conjugation matrix `C`, and `S² = C`,
  `C² = 1`.
- **`sTransform_pow_four : S ^ 4 = 1`** — self-reciprocality. `S` has order dividing 4: `𝓗⁴ = id`,
  matching the self-reciprocal q-Hankel transform of 1208.2521. This is the structural fact the
  program should have matched against instead of screening node values.
- **`eigenvector_pow_four_fixed`** — an eigenvector `v` with `S v = ζ v` satisfies `ζ⁴ • v = v`
  (any `CommRing`); and **`eigenvalue_pow_four_eq_one`** — over a **field**, on a **nonzero** `v`,
  this sharpens to `ζ⁴ = 1`, so every eigenvalue is a 4th root of unity: the eigenfunction class is
  narrowed to the four
  charge-conjugation phases, as ordinary self-dual Fourier forces `iⁿ` on Hermite functions.
- **`vacuumRow_conj_invariant`** — the vacuum row `d_q(λ)/D` is fixed by the transpose involution
  (`d_q(λ′)=d_q(λ)`), so it lives in the `C = +1` **self-dual sector**. There `S² = +1`, the real
  symmetric `S` has eigenvalues `±1`, and the PF-positive `+1` ground state is `d_q` (inputs A+B).

## Scope (STRICT) and honest verdict

- **This is the keystone value step (s013), not Step-9b.** The banner-pairing of "gap-9b" with these
  q-Bessel uploads is a mislabel; the q-Bessel / E_q(2) material is redirect (ii) of the value map.
- **Not a closure — a narrowing.** The value step already has its non-geometric answer
  (redirect iii = Markov/PF uniqueness; `BWVacuumRowIsHecke.lean`). Leg (C) supplies the *constraint*
  any geometric realisation must satisfy, and the structural reason a **free-scale** q-Bessel family
  (big q-Bessel, math/9805023) cannot be it: the target is a fixed point of a self-reciprocal
  transform in its self-dual sector, not a scale-dependent node value.
- **The PF-selection step (B)** that pins the specific `+1`-eigenvector to `d_q` is **cited**
  (Ocneanu/Wenzl, corpus), not re-proved here. Per the STRICT "refuted" discipline this note is a
  **scope-(a)** re-scoping of the big-q-Bessel route (free-scale ⇒ not a disciplined 0-dof test), plus
  a positive structural contribution (the self-reciprocality narrowing), not a scope-(b) exclusion.

## Follow-up (queued, not run)

1. Sector refinement — **done** (PR #3362): `conjFixed_sSq_fixed` (`C w = w ⇒ S² w = w`) and
   `eigenvalue_selfdual_sector_pm_one` (over a field, nonzero `w` in the `C = +1` sector ⇒ `ζ² = 1`,
   i.e. `ζ = ±1`), both sorry-free. The `+1` PF ground state pin to `d_q` — **done** (follow-up PR,
   `KeystonePerronFrobeniusGroundState.lean`): the §3b-cond primary conjecture class
   `PerronFrobeniusGroundState` (content field `pf_proportional` = cited PF/Ocneanu–Wenzl up-to-scale
   uniqueness), and the derived sorry-free `eq_d_of_normalized` / `ground_state_unique` — a normalised
   positive ground eigenvector is uniquely `d_q`. Non-vacuity via a `Unit`-block instance; the
   physical Hecke-fusion instance stays owner-gated open.
2. ~~Strengthen `eigenvalue_pow_four_eq_one` to `ζ⁴ = 1` over `[Field R]`~~ — **done** (this PR,
   addressing Copilot review): field + nonzero `v` gives `ζ⁴ = 1` via a per-component domain argument.
3. Record in the s013 ledger that both q-Bessel uploads are keystone redirect-(ii), now superseded by
   the (A)+(B)+(C) narrowing.
