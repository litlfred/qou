# L2 / 1 ppQ strategy — q₀ is observed-not-derived; the real gap is relational (Δ_λ); dilog machinery is foundational

**Date:** 2026-08-01. **Context:** after closing the dilog Part-B epic (the a.e.
Borel–Cantelli positive, `DilogPartBAEFinal.lean`), the question was raised: *how do we use
this machinery, and does it close the 1 ppQ gap?* This doc records the honest answer plus a
corrected L2 strategy. Supersedes the loose framing that the dilog limit or an "un-derived
q₀ / 2.89% m_p gap" is where L2 lives.

## 1. The dilog-archimedean-limit machinery is FOUNDATIONAL, not an L2 lever

`conj:dilogarithm-archimedean-limit` (`(1−q)·log Φ_n(x;q) → Li₂(x)`, Faddeev scaling; Part A
q→1⁻ closed #4157, Part B W-P1/W-P2 + a.e. positive closed 2026-07-31/08-01) is a
**correctness/uniqueness** input to the derivation chain, not a precision knob. Its three
corpus consumers (grep `uses[]` cone, 2026-08-01):

- `archimedean-functor-uniqueness` — the **step-9 archimedean functor `τ`** ("the only
  analytic limit; τ *is* the observation"). The dilog limit makes the q→1 evaluation
  well-defined and unique.
- `borromean-bloch-group-element` — the Bloch-group element for 𝓑₃.
- `phi-q-wkb-greens-function` — the WKB Green's function.

It fixes the **leading** `Li₂` term. The precision that determines Q_β/relations to ppb lives
in the **subleading** structure (the c_k truncation ladder / Q_β Habiro element), a *different*
fibre object the leading limit says nothing about. The `−π²/3` it produces is an **abelian
dilog cusp value** (two `π²/6` boundary terms), NOT a curvature/anomaly correction (ledger
2026-07-26). **Claiming it closes L2 would be laundering.** It is load-bearing scaffolding for
step 9; orthogonal to the numeric accuracy of any single observable.

## 2. q₀ is OBSERVED (measured locally), not derived — reframing Subgoal-2

Corpus convention (two-layer, AGENTS.md §q₀-anchor): q₀ is **pinned on m_p/m_e at 0.06 ppb** —
a *measured* substrate parameter, like a VEV or the local expansion rate. Consequence:

- **"Derive q₀ ab initio" (the old Subgoal-2 framing) is the wrong target.** You do not derive
  a locally-measured parameter; you measure it and predict *relations*. This makes the
  absolute-mass L2 targets semi-vacuous — they demand the framework out-resolve the
  experimental precision of its own calibration input.
- **q₀ varies spatially (x,t) — owner proposal 2026-08-01, NOT yet in corpus.** A grep found no
  existing q₀-spatial-variation content. If `q₀ = q₀(x,t)`, every substrate-derived constant
  co-varies *together*, mapping onto varying-fundamental-constant observations (Webb et al.
  α-variation; quasar μ = m_p/m_e bounds ~10⁻⁶–10⁻⁷). This converts the apparent weakness
  ("why q₀ = 1.1097?") into a **falsifiable prediction** (locked co-variation of all
  constants). **Recommended new first-class conjecture:** `conj:substrate-parameter-locality`
  — q₀ is a local observable; its variation drives correlated constant-variation. (Formalize-
  first: state the co-variation relation `d log(observable_i)/d log q₀` as the predicted,
  measurable signature.)

## 3. Real L2 dashboard (2026-08-01, proton-pinned q₀) — absolute mass is solved to ppb

`per-observable-100x-status.witness.json` (compute 70 dps):

| obs | pred err (ppb) | exp σ (ppb) | 100× target (ppb) | miss × | reading |
|---|--:|--:|--:|--:|---|
| m_p | **1.35** | 0.31 | 0.0031 | 437 | ≈ the pin; **solved to ppb** |
| m_n | **2.39** | 0.57 | 0.0057 | 416 | **solved to ppb** |
| Q_β | 1248 | 780 | 7.8 | 160 | within ~1.6 σ_exp |
| **m_μ** | **210** | 22 | 0.22 | 964 | **the 9.5σ μ–p tension — the real signal** |

The "miss factors" for m_p/m_n are artifacts of how precisely those masses are *measured*
(sub-ppb σ_exp ⇒ 100×-target at 3–6 ppt, research-grade). The canonical m_p is the
**muon-anchored Hecke energy** `m_p = 2(m_μ·F_Bor − 6m_e)` (`canonical_mass.py`), CODATA-matching;
the **deprecated** `Vol(𝓑₃)·λ_A/ℏ_q²` form (966 MeV, +2.96%) is a purged fit
(`docs/canonical-mass-formula-guardrail.md`) and is NOT the live status.

**So the genuine L2 content is not absolute mass — it is the overdetermined *relations*:** the
μ–p tension (m_μ +210 ppb) and Q_β/Δ_pn.

## 4. Where the gap actually closes: Subgoal-1 (Δ_λ / operator-valued branching)

Per `docs/precision-goals.md`, the achievable route (targets ≥ ~780 ppb CAL-2 floor) is the
per-isotope Borromean-tower extension + the **operator-valued branching combiner** — the
`Δ_λ` closure / the per-isotope binding `M_n(K)` edge-set. This is the shared root of the
Q_β/m_n/Δ_pn trio (`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`) and is
**open for all** (owner reversals 2026-07-11 / 2026-07-13). The Δ_λ gate: six closure ansätze
failed on the deuteron; PROBE-4 (KL-positivity vs the mixed-sign target) is Lean-proved-pruned;
Option E via the A=4 interface operator (PROBE 2) + `conj:s5-so3-fiber-action` is the live
direction. Anti-fit discipline stands: a Δ_λ obtained by inverting the AME anchors is a fit,
not a derivation.

**The one number that most tests the framework is the μ–p tension (210 ppb, 9.5σ).** The
decisive question for Subgoal-1: does the operator-valued branching / subleading structure
*predict* that 210 ppb (real deviation), or *close* it (theory error)? Either outcome is
publishable — a locked deviation is a prediction; a closure is a precision win.

## 5. Concrete next actions

1. **Scope the Δ_λ / branching attack** on the μ–p + Q_β/Δ_pn relations via Option E (A=4
   interface operator) — formalize-first (state the invariant that would justify a
   scope-(b) exclusion before running any wide fit).
2. **Add `conj:substrate-parameter-locality`** (q₀ observed-local + co-variation prediction) as
   a first-class conjecture with the `d log O_i / d log q₀` signature — the distinctive
   falsifiable-physics direction, currently absent from the corpus.
3. Keep the dilog machinery labelled **foundational** (step-9 bridge), not L2 — so it is not
   mis-cited as a precision result.
