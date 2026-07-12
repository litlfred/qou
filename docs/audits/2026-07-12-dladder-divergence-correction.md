# Correction: the D-ladder generating function is super-exponentially DIVERGENT (radius → 0), not convergent — the "radius 0.143" was a finite-n shadow

**Date:** 2026-07-12 · **Branch:** `claude/dladder-convergence-search-2026-07-12` ·
**Corrects:** [`2026-07-12-bar-odd-s-deformed-rung-followup.md`](2026-07-12-bar-odd-s-deformed-rung-followup.md)
§Route 2 (merged PR #3716) · **Tier:** numerical-derived + corpus-corroborated ·
**Discipline:** scope-(a) re-scope (the exact d_k stand; only the
convergent/divergent *reading* was wrong); no c_k wired; no fit; no tier change.

## The over-claim

PR #3716's Route 2 concluded that `D(ũ) = Σ dₖ ũᵏ` is **convergent** with a
Domb–Sykes radius ρ ≈ 0.143 and a weak branch point, and drew a "sharp contrast"
with the divergent κ-tower — claiming the two bar-odd-S routes are *not* the same
series. That reading was a **finite-n shadow artifact**, and the corpus already
documents exactly this trap.

Two things flagged it (owner hints "super-exponential..?" + "checkcorpus"):

1. **No singularity at ρ.** A convergent series with radius 0.143 must have a
   singularity of `log R(q(ũ))` at `|ũ| = 0.143`. A full search found none: the
   sqrt branch points `q⁴+q²+1=0` and the `ũ'(q)=0` folds map to `ũ=0`, the
   `cos(α_eff)=0` roots sit at `|ũ| ≥ 1.47`, and the nearest singularity of any
   kind (a `QA` zero / a complex fold) is at `|ũ| = 0.45–0.78 ≫ 0.143`. The root
   test `|dₖ|^{1/k} = 5.9` at k=21 is inconsistent with any of these radii.

2. **Corpus (checkcorpus).** The Lean-backed
   [alien-calculus / binding Gevrey-1/2 audit](2026-07-12-alien-calculus-review-binding-gevrey-half.md)
   already establishes that at the **real substrate `q₀`** these ladders undergo
   a *divergence-class change*: "the level-1/2 root test **rises without plateau**
   — the finite-n shadow of radius → 0 … the q-deformation **changes the
   divergence class** … q-Gevrey (Jackson q-Borel territory)." The
   [bridge growth-obstruction audit](2026-07-12-fmap-4one-qbeta-bridge-growth-obstruction.md)
   frames the same three-class picture (Gevrey-1 κ-tower; convergent Q_β `c_k`
   pole; and the substrate objects whose radius → 0).

## The corrected reading — super-exponentially divergent

The exact d_k are unchanged. Applying the corpus's own diagnostic:

- **Root test rises without plateau.** `|dₖ|^{1/k}`: 4.37 → 5.91 → 6.08 over
  k=4…27, still climbing at k=27 — the finite-n shadow of radius → 0, exactly as
  the alien-calculus audit describes.
- **Super-exponential growth law.** Fitting `log|dₖ| = A + B·k + C·k·log k` gives
  **C > 0** on every window (0.077 at k=6…21, 0.062 at k=6…27, 0.048 at k=14…27),
  and the fit is 50–300× tighter (SSR) than a pure-geometric `A + B·k`
  (constant-radius) law. The small C is why 27 terms of the *ratio* looked
  deceptively flat (~6.5): `(k!)^{C}` grows slowly enough to mimic a constant
  ratio, which the Domb–Sykes 1/k-fit then mis-read as a finite radius. C drifts
  *down* with the window (0.077→0.048), so it is not a fixed classical Gevrey
  index — the honest class at `q₀` is **q-Gevrey** (Écalle acceleration chain,
  per the corpus), reported as "super-exponentially divergent, C ≈ 0.05–0.08
  shadow," not a pinned index.

So `D(ũ)` is **super-exponentially divergent (radius → 0)** — in the *same*
resurgent family as the κ-tower, consistent with the corpus's q-Gevrey
class-change at `q₀`, **not** a convergent contrast to it. The exponent C is
small (much milder than the κ-tower's Gevrey-1 or the binding period's
Gevrey-1/2), and at `q₀` the honest class is q-Gevrey (an Écalle acceleration
chain, per the corpus), not a fixed classical Gevrey index — reported as
"super-exponentially divergent, C ≈ 0.08 shadow," not a pinned index.

## What still stands from Route 2 (unaffected)

- **Exact parity structure** (odd k → √3-part small-denominator; even k →
  rational part) — exact, unchanged.
- **3-smooth (Ohtsuki/Habiro) denominators** — exact, unchanged.
- **No holonomic P-recurrence** (order ≤ 4, deg ≤ 5) — unchanged; consistent with
  a q-Gevrey / non-holonomic-at-low-order object (the corpus reaches the same
  "not q-holonomic at low order" verdict for the binding tail).

Only the convergent-vs-divergent reading is corrected. The lesson is the same as
Route 3's top-row fix: a finite-truncation *reading* (there, the padded top row;
here, the 1/k radius extrapolation) was mistaken for structure.

## Honest scope (anti-laundering)

Scope-(a): the exact ℚ(√3) coefficients are correct; only the growth-class
reading is corrected, and the correction is corpus-corroborated (Lean-backed
Gevrey/q-Gevrey machinery), not a new claim. Nothing closes `S`, wires a `c_k`,
or changes any tier.
