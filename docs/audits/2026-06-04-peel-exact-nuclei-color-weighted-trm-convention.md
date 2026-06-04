# Peel exact-for-nuclei (#508 P2) — diagnosis + the color-weighted tr_M convention question (2026-06-04)

Investigation while moving the L1 cross-check gate from 1 ppb → 1 ppQ
(PR #1829). The 1 ppQ certification now rests on the three float-clean
methods (Hoefsmit / chi-cache / Habiro, agree to ~1e-48); **markov_peel**
was demoted to a labelled float independent check because its exact
symbolic path **raises for every nucleus**. This doc records exactly why,
the fix that makes it run, and the convention question that fix exposes.

## 1. Why the exact peel path raised on nuclei

`markov_peel.crossing_from_cd` knew only 4 crossing templates
(`σ`, `σ⁻¹`, `½(σ+σ⁻¹)=σ−h/2`, `𝟙`). The production atomic braid
(`mass_at_3A_proper.atom_braid_word_3A`, `pn_convention="bring_color_weighted"`)
emits a **fifth** crossing on every p-n bond:

    σ_i − h·(1/2 − δ/4)·𝟙
    (mass_at_3A_proper.atom_braid_word_3A, pn_convention="bring_color_weighted")

with `δ = canonical_braid_crossings._avg_color_delta()`. Numerically
`d ≈ −0.10446`, which differs from `−h/2 ≈ −0.10453` by ~7e-5 — outside
the classifier tolerance, so it raised `unknown (c,d) crossing`. The
fast LaurentQ path hit the same classifier and raised too. (The 4-template
classifier was always the open #508 Phase-2 item.)

## 2. δ is an EXACT q-rational (answers "can we get a q-poly?")

`δ` is **not** an opaque numerical constant. From `_li_2_q_util`:

    δ_leading(q) = (q−1)²·(1 − q⁻⁴) / 3          (prop:flavor-split-substrate)
    δ(q)         = δ_leading(q) · (1 + ℏ_q³),     ℏ_q = (q−1)/q

i.e.

    δ(q) = (q−1)²·(1 − q⁻⁴)/3 · (1 + ((q−1)/q)³)

This symbolic form evaluated at q₀ matches `_avg_color_delta()` to 2.6e-19.
So the color-weighted crossing can be carried **exact-in-q** — extending
`crossing_from_cd` with this symbolic δ(q) makes the exact peel path RUN
for nuclei (deuteron 2.6 s, ³He 5.3 s, exact-in-q).

## 3. The convention question this exposes (the real #508-P2 blocker)

With the color-weighted crossing wired in, the exact peel **disagrees with
the on-disk Hoefsmit/peel witnesses by exactly 1.8e-4** — the δ term:

| atom | exact peel (color-weighted) | Hoefsmit witness (−h/2, color-blind) | rel Δ |
|------|------|------|------|
| deuteron | 0.388357209984596816 | 0.388286424074788877 | 1.8e-4 |
| ³He | 0.206578470100370555 | 0.206540817020739648 | 1.8e-4 |

So the cross-check witnesses compute the **color-blind** `tr_M` (−h/2),
while production + the formalized δ(q) are **color-weighted**. The open
question is **where the color weighting lives**:

- **(A) inside tr_M** — the trace itself uses `σ−h·(½−δ/4)`; the witnesses
  are stale and should be regenerated color-weighted. The exact peel
  above is then "more correct" than the witnesses.
- **(B) as a post-trace mass dressing** — `tr_M` is color-blind (−h/2,
  witnesses right), and the flavor split is applied to the MASS after the
  trace. The paper/Lean evidence points here: the formalization lives in
  `lean/QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean` and
  `brings-surface/inter-nucleon-channel-color-tube.{md,lean}` — a
  *dressing* applied to the dressed mass, not a modification of the Hecke
  trace.

**This is a framework-intent call** (owner / canonical-derivation review),
not a code fix. Until it is resolved, do NOT regenerate the tr_M witnesses
color-weighted and do NOT flip `markov_peel`'s `use_fast` default — the
1 ppQ certification correctly rests on the three float-clean (color-blind,
internally consistent) methods.

## 4. Where this is formalized (paper + Lean)

| Object | Content (.md/.ts) | Lean |
|--------|-------------------|------|
| δ(q) flavor split | `observations/flavor-split-substrate.md` (`prop:flavor-split-substrate`) | `observations/flavor-split-substrate.lean` |
| Color dressing of the mass | `brings-surface/inter-nucleon-channel-color-tube.md` | `lean/QOU/FlavorDressing.lean`, `…/DressedMassFromSubstrateSplit.lean`, `lean/QOU/HadronicMass.lean` |
| δ(q) in the binding amplitude | `braids-and-knots/hoefsmit-binding-amplitude.md` | — |

## 5. Concrete next steps (when the convention is settled)

If **(B)** (post-trace dressing) is confirmed — the likely reading:
- Leave tr_M color-blind; the witnesses + 1 ppQ certification stand.
- Document in the cross-check that peel's exact path is color-blind
  (`pn_convention="strict_averaged"`, `−h/2`) for tr_M consistency, and
  the color weighting is a downstream mass dressing.
- The #508-P2 classifier extension is then only needed if a color-weighted
  tr_M is ever wanted; carry δ(q) symbolically (§2) and also teach the
  LaurentQ fast path to ingest the δ(q) element (it currently fails
  `LaurentQ.from_sympy` on the q⁻⁴ term).

If **(A)** (inside tr_M):
- Regenerate Hoefsmit/peel/chi-cache witnesses with the color-weighted
  crossing, re-certify 1 ppQ, then flip `use_fast`→False.
