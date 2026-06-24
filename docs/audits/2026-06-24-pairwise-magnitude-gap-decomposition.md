# Pairwise-magnitude gap — per-bond decomposition (A=3)

**Date:** 2026-06-24
**Branch:** `claude/pairwise-magnitude-gap-2026-06-24`
**Follow-up to:** PR #2630 (structured combiner isolated the A=3 binding gap to the
pairwise / leading trace, not the 3-body sign sector).

## What this probe does

`pairwise_magnitude_gap_probe.py` decomposes the A=3 pairwise (leading-trace)
binding per bond, `|χ|` combiner over the H₉ joint trace (Rust kernel), **0 fit**:

| atom | bond 0 (gen 2) | bond 1 (gen 5) | `B_pair` model | per-bond avg | AME B |
|---|---:|---:|---:|---:|---:|
| ³H  | +2.320 | +2.701 | **+5.021** | +2.51 | 8.482 |
| ³He | +2.200 | +2.672 | **+4.872** | +2.44 | 7.718 |

## Two robust observations (do not depend on the target choice)

1. **Each modeled bond is deuteron-scale** — 2.20–2.70 MeV, i.e. each adjacent
   interface bond is already *at or slightly above* the free deuteron B₂ = 2.225 MeV.
   The leading-trace per-bond binding is **not** anomalously weak.
2. **The shortfall is uniform across isotopes.** Whatever scale separates the model
   from the full AME binding is ≈ isotope-independent per bond (T vs ³He per-bond
   deficit spread **8.6 %**), i.e. it is **not** a bond-type (pp / pn / nn) specific
   correction to the per-interface factor (`z` / `z−h` / `z−h/2`). A bond-type
   correction would split T (pn, nn bonds) from ³He (pp, pn bonds); it does not.

## The target choice — explicit caveat (not a closure)

The probe also reports a deficit against a **reference target `3·B₂` = 6.674 MeV**
(three independent deuteron-strength pairs in a triangle). This is a **modeling
reference, not a derived quantity** — the linear-chain model carries only 2 explicit
adjacent bonds, and the third (long-range) pair is geometrically suppressed to
+0.26 MeV in the joint trace (PR #2630 §B), not a full ~2.2 MeV bond. So the
"deficit vs 3·B₂" (≈ 1.65–1.80 MeV, ≈ 25–27 %) conflates two effects:

- the **missing/suppressed long-range third bond** (geometry), and
- a genuine **per-bond cooperative shortfall** (the bonds present give 2.5 MeV each
  but the total still trails the full AME binding by ~38 % even with all three).

The probe does **not** disentangle these two — it localizes the gap to the leading
trace and shows it is uniform, but `3·B₂` is a yardstick, not a prediction.

## Reading

Per the §"refuted/ruled out" discipline this is a **scope-limited (a) finding**: the
multiplicative leading-trace model, *alone*, underbinds A=3 uniformly per bond. It
does **not** exclude any ingredient. The uniformity is consistent with — but does not
prove — a missing **cooperative (non-multiplicative) enhancement common to all bonds**
(the operator-valued branching combiner / q-Reeb `|Δθ_λ|` magnitude, sibling #2612),
rather than a per-interface-factor fix. Next: check whether the q-Reeb per-λ phase
supplies a uniform per-bond enhancement of the right ~0.85 MeV/bond scale.

→ `computations/probes/pairwise_magnitude_gap_probe.py` ·
`computations/pairwise-magnitude-gap-decomposition.witness.json`

## Consistency bridge — the deficit IS the cancelled q-Reeb phase (J_ν, not I_ν)

Running `binding_reeb_phase_decomposition.py` (which splits each Wedderburn block λ
into a **rotation/J_ν** channel — `arccos`, `|r_λ|≤1`, carries the q-Reeb phase
`Σ|Δθ_λ|` — and a **growth/I_ν** channel — `arccosh`, `|r_λ|>1`, extensive) against
the deficit above gives a clean, parameter-free relation:

| atom | deficit D (MeV) | `Σ|Δθ|` (rad) | `D / Σ|Δθ|` (MeV/rad) |
|---|---:|---:|---:|
| ³H  | 1.652 | 8.223 | 0.2009 |
| ³He | 1.802 | 8.494 | 0.2121 |

`D / Σ|Δθ| ≈ 0.206 MeV/rad` (**5.4 % spread**, = `E₀·0.0493`). Both the deficit and
the phase are uniform across isotopes, and they **co-vary**.

**This revises the initial `I_ν`-growth guess.** The growth channel collapses
free→atom (T: 93.1 → 1.58, ×0.017) — that collapse **is** the leading binding, and
the `|χ|` combiner already captures it. The missing residual lives in the
**rotation/J_ν phase channel**, which `|χ|` *cancels* (`|e^{iθ}| = 1` regardless of
`θ`). That cancelled phase is exactly the **q-Reeb `|Δθ_λ|`** object of sibling
#2612 — so #2612's phase is a concrete candidate for the missing magnitude, and this
deficit fixes its conversion scale (~0.21 MeV/rad) **without fitting**.

**Honest caveats (scope-(a)):** N=2 isotopes is too thin for a law; 0.206 MeV/rad is
not (yet) a canonical scale; D inherits the `3·B₂` yardstick caveat. This is a
*consistency relation + a falsifiable target*, not a derivation.

**Falsification.** If the relation holds, ⁴He (`Σ|Δθ| = 17.233` rad) should show a
leading-trace deficit ≈ `0.206 × 17.233 ≈ 3.56 MeV`. That is the next test.

→ `computations/probes/reeb_phase_deficit_consistency_probe.py` ·
`computations/reeb-phase-deficit-consistency.witness.json`
