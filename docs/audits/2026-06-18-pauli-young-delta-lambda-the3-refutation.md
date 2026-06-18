# Pauli-Young / Wigner-SU(4) Δ_λ — refuted by the T/³He sign test; "novel" claim corrected

**Date:** 2026-06-18
**Probe:** [`probe_pauli_young_delta_lambda_the3_signtest.py`](../../computations/probe_pauli_young_delta_lambda_the3_signtest.py)
→ `probe-pauli-young-delta-lambda-the3-signtest.witness.json`
**Status:** EXPLORATORY (per `production-vs-exploratory-discipline`); asserts the
refutation (expected-negative ⇒ CI-safe). Δ_λ remains an open gate (GAP-A-3/A-4);
this **closes the Pauli-Young branch** of it.
**Subject:** the Δ_λ angle proposed in [PR #2461](https://github.com/litlfred/qou/pull/2461)
("generalize Pauli-channel → weighted channels").

## What PR #2461 proposed

The pick-one Pauli channel map (`pp/nn → alternating`, `pn → standard`) is the
S₂ special case of a per-partition weighting; lifting to `λ ⊢ k` lands on the
framework's per-isotope formula

$$B(K) = m_e \sum_{\lambda} y_\lambda(q_0)\,\chi^\lambda(\beta_K)\,\Delta_\lambda ,$$

with the proposal that **Δ_λ is a spin-isospin Young-symmetry (Pauli)
projection** — `Δ_λ = ⟨χ^λ, χ_{spin⊗isospin}⟩`, a Wigner
SU(4) = SU(2)_S × SU(2)_I multiplicity. PR #2461's body asserts a **"corpus-grep
verdict: NOVEL"** and marks the angle "specified but not run".

Both assertions are wrong. This audit records the correction and the decisive
test.

## Correction 1 — NOT novel (corpus already carries this angle)

The "spin-isospin Young-symmetry" / Wigner-SU(4) angle for the mass/binding
trace is already in the corpus; the prior session's corpus-grep used too narrow
a search (the compound phrase, plus only the six *named* refuted ansätze) and
missed:

- [`particle-interactions/wigner-su4-from-spin-isospin.md`](../../content/quantum-observable-universe/particle-interactions/wigner-su4-from-spin-isospin.md)
  — conjecture **D11**, maps `A → SU(4)` supermultiplet explicitly
  (`A=2: 4⊗4 = 6⊕10`; `A=4: 4^{⊗4} ⊃ 1`), i.e. the spin-isospin Young symmetry
  on nucleons.
- [`mass-theory/schur-weyl-mass-decomposition.ts`](../../content/quantum-observable-universe/mass-theory/schur-weyl-mass-decomposition.ts)
  — "Schur–Weyl decomposition of the atomic mass trace" (status `verified`),
  with `prop:wigner-2-coefficient`, `wigner-np-pairing`,
  `wigner-coefficient-derivation.lean`.

This is the exact failure mode the STRICT corpus-grep checklist (CLAUDE.md
§"Before declaring open…", precedent PRs #1515/#1532/#1543) exists to catch:
a "this is new" claim that the corpus already contains.

## Correction 2 — and refuted (the decisive T/³He sign test)

The sharp test is the [`2026-06-02`](2026-06-02-volume-wedderburn-delta-lambda-probe.md)
necessary condition. **T (³H) and ³He share `n = 9`** (same 30 partitions, same
`y_λ` — verified `max|y_λ drift| = 0.0`), so the *entire* same-`n` binding split
is one number:

$$\frac{B_T - B_{^3\mathrm{He}}}{m_e} = \sum_\lambda \Delta_\lambda\, v_\lambda
  = +1.4947, \qquad v_\lambda := y_\lambda\,(\chi^\lambda(\beta_T) - \chi^\lambda(\beta_{^3\mathrm{He}})).$$

A Pauli / spin-isospin Young-symmetry projection is a **multiplicity**, hence
`Δ_λ ≥ 0`. Evaluating the concrete, parameter-free weight
`Δ_λ = dim GL(4)-irrep(λ) = #SSYT(λ, 4 letters) = ⟨χ^λ, χ_{(ℂ⁴)^{⊗9}}⟩`
(hook-content formula) and the uniform control:

| Δ_λ weight | `Σ_λ Δ_λ v_λ` | target | verdict |
|---|---|---|---|
| Wigner-SU(4) `dim GL(4)(λ)` | **−45.02** | +1.4947 | wrong sign, ~30× |
| uniform `Δ_λ = 1` | −0.1025 | +1.4947 | wrong sign |

The symmetric weight loads `dim` onto exactly the 2-row blocks
`[7,2]=540, [6,3]=480, [8,1]=440` whose `v_λ` are the *most negative* — it is
maximally anti-aligned with the target.

**Structural reason (corpus).** Per
[`2026-05-24-isospin-categorical-source.md`](2026-05-24-isospin-categorical-source.md),
the T/³He split **is isospin breaking** — the 305 ppm anomaly carrying the
bar-anti-symmetric factor `h = q − q⁻¹`. An isospin-**symmetric** SU(4)
projection cannot supply an isospin-**breaking** differential: T and ³He are
partners in one supermultiplet, so the nucleon-level reading predicts the split
**exactly 0**, and the strand-level (`dim GL(4)`) reading predicts **−45**.
Neither is +1.4947. You cannot get isospin breaking out of an isospin-symmetric
projection.

**Index-mismatch note.** PR #2461's "lift to `λ ⊢ k`" conflates two indices: the
framework's `Δ_λ` is indexed by `λ ⊢ 3A = 9` (braid strands), but a spin-isospin
multiplicity is naturally indexed by `μ ⊢ A = 3` (nucleons). Both readings are
covered above (strand: −45; nucleon: 0 by isospin symmetry); there is no
canonical `λ⊢9 → μ⊢3` map, and any chosen one is itself a degree of freedom.

## Correction 3 — refining the 2026-06-02 necessary condition (honest narrowing)

The direct `v_λ` sign census **corrects an over-strong claim** in the 2026-06-02
audit. That audit, having scanned only the Bloch-Wigner volume *family* (best
−0.42), wrote "a positive per-block volume cannot reproduce even the sign." The
census shows `v_λ` is **not** sign-definite:

```
v_λ sign census over 30 partitions:   positive: 10   negative: 20   zero: 0
v_max = +2.241e-4    v_min = −2.744e-2
```

Because 10 partitions carry `v_λ > 0`, the non-negative **cone** is unbounded
above — sign-correct non-negative weights **do exist**. So the obstruction is
*not* "positivity forbids the sign" (too strong); it is the sharper-and-narrower:

> Every *principled, shape-fixed* non-negative weight tested (Bloch-Wigner
> volumes, uniform, Wigner-SU(4) dim) lands at the wrong sign, because the
> binding's `v_λ` weight is concentrated negative on the high-dimension
> low-row blocks. Any non-negative `Δ_λ` that *does* hit +1.4947 must
> selectively up-weight the 10 positive-`v_λ` partitions — i.e. it is a **free
> fit**, not a derivation, and the Δ_λ gate rejects it.

## Verdict

- **Pauli-Young / Wigner-SU(4) Δ_λ branch: CLOSED (refuted).** As a *principle*
  it gives the wrong sign by ~30× on the sharpest same-`n` test; as a *fit* it is
  the gated seventh ansatz. It is also not novel.
- **Δ_λ remains open** (GAP-A-3/A-4). The direction the evidence still points to
  is unchanged from 2026-06-02's own follow-up: a **signed / chirality-aware**
  per-block weight — oriented (signed) tetrahedron volumes in the full
  Turaev–Viro state-sum, or the Type-B fold / bar-involution `h`-structure that
  the corpus already identifies as the *source* of the isospin breaking. A
  non-negative symmetry multiplicity is structurally the wrong object.

## Cross-references

- [PR #2461](https://github.com/litlfred/qou/pull/2461) — the proposal corrected here
- [`2026-06-02-volume-wedderburn-delta-lambda-probe.md`](2026-06-02-volume-wedderburn-delta-lambda-probe.md) — the same-`n` T/³He necessary condition (refined here)
- [`2026-05-24-isospin-categorical-source.md`](2026-05-24-isospin-categorical-source.md) — T/³He split = isospin breaking (the `h` anomaly)
- [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the six refuted ansätze + the gate
- [`wigner-su4-from-spin-isospin.md`](../../content/quantum-observable-universe/particle-interactions/wigner-su4-from-spin-isospin.md), [`schur-weyl-mass-decomposition.ts`](../../content/quantum-observable-universe/mass-theory/schur-weyl-mass-decomposition.ts) — the prior corpus content (⇒ not novel)
