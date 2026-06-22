# Lepton-generation mass mechanisms — the full landscape and the one shared root

**Date:** 2026-06-22
**Branch:** `claude/lepton-generation-mass-landscape-2026-06-22`
**Status:** Synthesis — one map of every explored mechanism for deriving `m_τ/m_e` (and the
generation hierarchy) from `q₀`, WRT and non-WRT, with the obstruction they all share. No new probe
(the obvious ones are corpus-explored); no fit. Incorporates this session's WRT-line terminus.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md), [`mtxi`](../../.beans/mtxi--m-tau-path-a.md), [`k9td`](../../.beans/k9td--koide-tau-forcing.md)

## The problem

The muon ratio is derived from `q₀` alone (CAL-2): `m_μ/m_e = Vol(4₁)/ℏ_q² ≈ 206.768`, reproduced to
`10⁻²⁰` at `q₀`. The paper claims `m_τ/m_e` is likewise "predicted from `q₀` alone" but never surfaces
the formula. **That formula is the open object.** Below is every mechanism the corpus has tried for it.

## The mechanisms and their status

| # | mechanism | form | status | source |
|---|-----------|------|--------|--------|
| 1 | **knot-volume** (simplest cohomological extension of the muon identity) | `m_τ/m_e = Vol(K_τ)/ℏ_q^{k_τ}` | **REFUTED** — best 8₁ at +1.33% (≈13000σ); no single knot, no pair-product under 0.1% | [`2026-06-03-m-tau-knot-prediction-falsification.md`](2026-06-03-m-tau-knot-prediction-falsification.md) |
| 2 | **Koide relation** | `(Σm)/(Σ√m)² = 2/3` ⇒ `m_τ` | forces `m_τ` to 62 ppm, but is a **CAL-4 import (fit)** — QOU derives no Z/3 democracy, no √m-amplitude, no categorical 2/3 | [`2026-06-16-koide-tau-forcing-assessment.md`](2026-06-16-koide-tau-forcing-assessment.md) (k9td) |
| 3 | **Path A — analytic ξ_ℓ(q)** | `m_ℓ/m_e = ξ_ℓ(q)·Vol_q^{tower}` | **UNDERDETERMINED** — lepton `V̂_i` unpublished; bar-symmetry + Kashaev don't fix `ξ_ℓ`; no candidate functional form; only the forbidden Path-B fit closes it | [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md) (mtxi) |
| 4 | **operator-valued ℓ=3 branching** (WRT / Markov) | `tau = ℓ=3` block of the `S₅→S₃` fibre map; `W_λ` weights | this session's line — driven to its **terminus: the W_λ↔WRT relation is Schur–Weyl DUALITY, not an equation**; the Poincaré-sphere WRT *selects* the icosahedral modular data but does not *compute* `W_λ` (dual S_n-side weights) | this session, PRs #2584–#2616 |
| 5 | queued extensions of #1 | Vol+i·CS; polylog tower `Li_{n>2}`; satellite/Whitehead double; KR-strata sum; tower-correction `(1−c₂ℏ²+…)` | **not run** — each is a *search over a hypothesis class*; the falsification doc + Δ_λ-gate discipline forbid running them as fits | [`2026-06-03-…falsification.md`](2026-06-03-m-tau-knot-prediction-falsification.md) §"Extensions" |

## The one shared root

Every mechanism bottoms out at the **same** obstruction:

> There is no **structurally-forced selector** for the higher generations — no derived `K_τ`, no
> derived `ξ_ℓ(q)`, no derived `ℓ=3` branching closure. The muon works because its selector **is**
> forced: `4₁` is the simplest hyperbolic knot (and amphichiral, `CS=0`), so `Vol(4₁)/ℏ_q²` has no free
> choice. No analogous forcing exists one generation up.

- #1 needs a forced `K_τ` — searching 25 knots is fishing.
- #2 needs the `2/3` to be categorical — it isn't (it's imported).
- #3 needs a forced functional form for `ξ_ℓ` — none exists.
- #4 needs the `ℓ=3` branching to *compute* `W_λ` — but `W_λ` is the Schur–Weyl *dual* of the WRT
  data, so the WRT line cannot supply the number (only select the modular data).
- #5 are searches that, without a forced selector, are fits by construction.

So the generation-mass problem is **genuinely open**, blocked at a single point: **the absence of a
derived higher-generation selector.** This is not a gap any of the five mechanisms closes; it is the
prerequisite they all assume.

## Critical-distance verdict

`m_τ/m_e` is **not** currently derivable from `q₀` alone in the corpus — the paper's "predicted from
`q₀` alone" claim for the tau is, as of now, **unsubstantiated** (the muon claim is solid; the tau
claim has no surfaced formula and every attempt to supply one is refuted, underdetermined, or a fit).
Forcing it by any of #1, #2, #5 is a CAL-4 / fit and is correctly caught by the three-calibration
discipline. A genuine closure requires **deriving the higher-generation selector** — the real research
core, which neither the WRT nor the non-WRT angle has cracked.

This is the honest terminus of the generation-mass exploration: the landscape is now fully mapped, and
the open work is sharply localised to the one missing piece.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored. The author closes the related beans (§4a).

## Cross-references

- [`2026-06-22-keystone-schurweyl-dual-sides.md`](2026-06-22-keystone-schurweyl-dual-sides.md) — the WRT-line terminus (#4) this incorporates.
- [`2026-06-03-m-tau-knot-prediction-falsification.md`](2026-06-03-m-tau-knot-prediction-falsification.md) — #1 falsified + #5 extensions.
- [`2026-06-16-koide-tau-forcing-assessment.md`](2026-06-16-koide-tau-forcing-assessment.md) — #2 (Koide = fit).
- [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md) — #3 (Path A underdetermined).
- [`content/quantum-observable-universe/mass-theory/calibration-inputs.md`](../../content/quantum-observable-universe/mass-theory/calibration-inputs.md) — the "tau predicted from q₀ alone" claim this audit flags as unsubstantiated.
