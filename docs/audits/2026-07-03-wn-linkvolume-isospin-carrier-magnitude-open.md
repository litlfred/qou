# θ_λ closure option 1 — link-volume is the isospin carrier, but the magnitude is not `a_D^(n)·Vol`

**Date:** 2026-07-03
**Branch:** `claude/theta-wn-closure-2026-07-03`
**Compute:** [`computations/theta_wn_jetfilt_linkvolume.py`](../../computations/theta_wn_jetfilt_linkvolume.py)
**Follow-up to:** option 2 (`…-wn-universal-kernel-refuted-mirror.md`), PR #3270 (mechanism).

## Setup

Option 2 refuted a universal scalar kernel (the ³H/³He mirror split ⇒ `w_n(K)` is
isospin-aware). Option 1 sets `w_n(K) ∝` the **hyperbolic volume of the n-body
sub-link** — which is isospin-aware by construction (³H and ³He sub-links differ).
This probe tests the **untried jet-filtration combination** (super-exp `a_D^(n)` ×
link-volume), since a prior *raw single-term* attempt undershot ~60%.

## Result (whole-atom link volumes: D=Hopf 0, ³H=8_11 8.286, ³He=L6a4 7.328)

| model | D | ³H | ³He | ⁴He | worst |
|---|--:|--:|--:|--:|--:|
| raw `m_e·Vol` | −100% | −50% | −52% | −87% | 100% |
| **jet `m_e·a_D^(A)·Vol`** | −100% | **−33%** | **−35%** | −67% | 100% |
| magic `2·m_e·A·Vol` | −100% | **+200%** | **+191%** | **+5.9%** | 200% |

## Reading — the carrier is right, the multiplier is open

1. ✅ **Volume is the correct isospin carrier.** `vol(³H)=8.29 > vol(³He)=7.33`
   matches the binding order (³H binds more than ³He) — the 13% mirror split that
   refuted the scalar kernel is *supplied* by the link topology, with no fit.
2. **The super-exp `a_D^(n)` helps but does not close.** It improves the A=3
   undershoot (−50% → −33%) but ⁴He stays −67%.
3. **The magic-shell `2·A` multiplicity fits ⁴He (+5.9%) but overshoots A=3 by
   +200%.** So `a_D^(n)=2.53` and the magic `2·A=8` are **different objects** — no
   single body-order multiplier reproduces both the light nuclei and ⁴He.
4. **Deuteron Hopf-link `Vol=0` is a structural wall** — the 2-body sub-link is
   Seifert-fibred (non-hyperbolic), so a pure-volume weight gives `B(D)=0`.

## Verdict (critical-distance)

**Option 1 does NOT close the θ_λ magnitude** as a single `a_D^(n)·Vol` (undershoots)
or `2·A·Vol` (overshoots light) product. What it **does** establish — cleanly and
without a fit — is that the **hyperbolic link-volume is the isospin (`T₃`) carrier**
of `w_n(K)`, confirming option 2's requirement. The residual is now sharply
localized:

> `w_n(K) = M_n(A) · Vol_n(K)`, where `Vol_n` (isospin, derived) is settled and the
> **body-order multiplicity `M_n(A)` is open** — it is neither the super-exp `a_D^(n)`
> (too small for ⁴He) nor the magic `2·A` (too large for A=3); and the deuteron
> `Vol=0` Hopf term needs separate (effective-volume) handling.

This is honest narrowing, not closure: three simple weight products
(`a_D^(n)·Vol`, `2·A·Vol`, raw `Vol`) are ruled out; the open piece is the
multiplicity `M_n(A)` on top of the (now-identified) volume carrier.

## Net across options 1/2/4 (θ_λ magnitude gate)

- **Mechanism** (extensive super-exp period): **derived + Lean-proved** (merged #3270).
- **Universal scalar kernel** (opt 2): **refuted** (mirror split).
- **Link-volume carrier** (opt 1): the volume **is** the isospin carrier (settled);
  the **magnitude multiplicity `M_n(A)` is open** (not `a_D^(n)`, not `2·A`).
- **na-Stokes `= lw` keystone** (opt 4): **owner-gated** (s5-so3, #2503).

The gate is not closed, but it is reduced to a single open scalar sequence
`M_n(A)` over an otherwise-derived structure — a much smaller target than the
original "derive `w_n(K)`".

## Provenance

Compute: `theta_wn_jetfilt_linkvolume.py` (volumes from
`binding-link-volumes.witness.json`; `a_D^(n)=lw(n−1)`; anchors from
`codata_constants`). Corpus: `conj:binding-manybody-jet-filtration`,
`prop:magic-A-binding-formula`, `prop:jet-filtration-binding-extensive` (#3270).
EXPLORATORY — no production wiring, no fitted constant.
