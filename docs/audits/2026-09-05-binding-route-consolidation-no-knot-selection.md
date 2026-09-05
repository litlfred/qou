# Binding-route consolidation: no knot-selection routes

**Date:** 2026-09-05 · **Owner ruling:** "NO knot-selection routes allowed"
· **Beans:** `qou-qnqf`, `qou-bygw`, `qou-4tui`, and the new derivation-path bean
· **Scope:** a decision plus the verification behind it. Nothing deleted; blocks
are marked, not excised. No number moves.

## What was ruled out, and why

A **knot-selection route** is one that assigns each atom a knot (or a per-`A`
knot factor) and reads the binding off that assignment. Two routes qualify.

### 1. The census route (`computations/mass_table_ppb.py`)

`ATOM_ASSIGN` is a hand-written per-atom lookup:

    2H  -> knot 6_2,  nu_sdp 1   "hyp: census-assigned (EXPLORATORY pending R5-full SDP)"
    3H  -> knot 8_11, nu_sdp 2   "hyp: census-assigned (EXPLORATORY pending R5-full SDP)"
    3He -> knot L6a4, nu_sdp 2   "hyp: census-assigned (EXPLORATORY pending R5-full SDP)"
    4He -> magic rule, A_units 4, nu_sdp 2  "(nu_SDP=2 extrapolated, pending R5-full)"
    5Li, 6Li, 7Li -> GAP

with `B = nu_SDP * m_e * Vol(K)`. **The selection is made against the
experiment.** The gap rows store `vol_kashaev_target_m_e_units = B_AME/m_e`, and
the gap comment states the rule outright: A ∈ {5,6,7} have no prediction because
"no census knot/link with Vol ≈ B_AME/m_e ... yet found". Choosing a knot from a
census so its volume reproduces the measured binding is fitting by selection: no
continuous parameter is tuned, but the discrete choice is made against the data,
and the gap is the proof.

The file header asserts "No fitting. Nothing calibrated from AME values." That
is **false as stated** for the assignment step and should be corrected.

**The `4He` "magic" rule is not an independent confirmation.** Verified:

    Vol(L6a4) = Vol(Borromean) = 8G = 7.32772475342
    B(3He) = 2*m_e*Vol(L6a4) =  7.4889 MeV
    B(4He) = 2*m_e*4*8G      = 29.9557 MeV
    ratio                     = 4.0 exactly

It reuses the volume the census assigned to `3He`, carries `nu = 2` over, and
multiplies by `A = 4`. It is the `3He` assignment scaled, so it inherits the
selection wholesale.

### 2. The dedicated route (`hecke_core_legacy.knot_factor` and callers)

`knot_factor` dispatches on mass number with per-knot factors:

    A == 2: dedicated formula elsewhere in binding_energy
    A == 3: 1 - h^2        (figure-eight amphicheiral, Fricke relation)
    A == 4: (1 - h^2)^2    (double amphicheiral)
    A >= 5: 1.0            (generic BW)

Its accuracy on `D`, `T`, `3He`, `4He` is exactly where the bespoke factors are.
Two further concerns, independent of the ruling:

- `K = 6 is the OPTIMAL partition cutoff`, chosen by "empirical sweep" and
  justified by accuracy against experiment ("40Ca: 0.001 at K=6 -> 0.012 at
  K=9"). A truncation order selected by matching data is a fitted parameter
  under the 2026-08-25 no-fitting directive. `K_PARTITION_MAX = 11` also
  contradicts its own comment's "capped at 8".
- `Satula et al. 1997 (empirical Wigner energy)` is cited as an input.

The factors `1 - h^2` and `(1 - h^2)^2` are derived-looking rather than
numerically tuned; they are special cases, not fits. The ruling excludes the
route for the dispatch, not for those values.

### Also retired: the unified path

`B_unif` gives the deuteron a **negative** binding energy (-16.45 MeV) and
misses `208Pb` by 58 %. Its own proof block frames the trade honestly: it "uses
one symbolic algorithm with zero fitted parameters and no special-case
branches", and is much worse for it. Implemented in
`hecke_core_legacy.py`, itself a DEPRECATION-CANDIDATE.

## What survives

Exactly one route has no per-atom assignment, no census, and no swept
parameter: the **free-versus-bonded trace ratio**,

    L = log( Z_free / Z_bonded ),

computed from a rule-derived word (`p^Z n^N`) by the exact engine, with one
declared calibration constant `alpha`. Its failures are documented and real —
31 % of `4He`, the definitional `A = 2` ordering inversion, no valley of
stability in any sum over per-bond constants — but they are the honest failures
of an unfitted model rather than the residuals of a search. A 5.87 % miss
obtained by picking a knot whose volume matches is weaker evidence than a 69 %
miss obtained by computing.

`rem:bond-log-ratio-is-a-free-energy` already records that `L` is a
free-energy difference and that `B = alpha L` is an open interpretation. That
stands unchanged.

## The unbuilt route

`prf:confined-knot-binding` specifies the principled version: "the character
ratio measures the volume departure from the free constituents. The total knot
factor multiplies these strict, empirically-independent character ratios across
all levels." And `knot_factor`'s own docstring concedes it is not running it:
"The per-level character ratio (nucleus/free-nucleon product) and confined-state
accumulation provide the categorical derivation path. **Currently using the
product formula for A<=4 and generic for A>=5.**"

So the corpus has specified an unfitted derivation path and never implemented
it, substituting hardcoded per-`A` factors. That is the one piece of machinery
that could change the picture without selecting against the data, and it now has
its own bean.

## What this changes in the corpus

Nothing is deleted and no number moves. `magic-A-binding-formula`,
`binding-alpha-shift-extension` and the atlas registry's canonical table are
marked with their status and pointed here; their `origin` fields already said
"EXPLORATORY", which the rendered table did not carry.

Not claimed: that the census assignments are wrong, that hyperbolic volumes are
irrelevant to binding, or that `L` is right. Only that a route which selects its
object against the target cannot be the corpus's consolidated binding route.
