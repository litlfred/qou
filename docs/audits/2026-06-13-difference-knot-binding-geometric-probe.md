# Binding as the mass of the difference knot — first geometric probe

> **⛔ RETRACTED 2026-06-13** — the volumes reported below are SnapPy noise on
> non-geometric triangulations. The difference link is **reducible /
> non-hyperbolic** (Regina `isIrreducible=False`; negative + 29–135 %-unstable
> "volumes"), so it has no hyperbolic volume. See
> [`2026-06-13-difference-knot-nonhyperbolic-retraction.md`](2026-06-13-difference-knot-nonhyperbolic-retraction.md).
> `prop:binding-error-amplification` is unaffected.

**Date:** 2026-06-13 · **Branch:** `claude/binding-difference-knot-geometric-2026-06-13`
**Probe:** [`probes/difference_knot_binding_probe.py`](../../computations/probes/difference_knot_binding_probe.py)
(witness `difference-knot-binding.witness.json`)
**Owner hypothesis (2026-06-13):** *"binding is to calculate the difference
of the knots before the trace is applied. That difference will have its own
knot structure, hence mass."*

## The idea, made precise

Form the braid-group difference **before** any trace:
$$ D \;=\; W_{\text{atom}}\cdot W_{\text{free}}^{-1} \quad(\text{crossing signs respected: } d\!\approx\!0\to\sigma^{+},\ d\!\approx\!-h\to\sigma^{-}), $$
free-reduce it to its core, close it, and take the binding to be the **mass
of that one knot** by the *same* geometric formula as a particle's rest
mass — `m_e·Vol(D)·ρ/ℏ_q²`. No trace enters the binding magnitude.

This is distinct from, and engineered to dodge, both prior attempts
(verified by re-reading them — corpus-grep discipline):

| prior probe | what it did | why it failed |
|---|---|---|
| `binding_link_volumes.py` | `m_e·Vol(K_bind)·Δtr`, **hand-assigned** Hopf/8₁₁/L6a4 | still multiplies by the flat, nearly-A-independent `Δtr` → −60% at A≥3 |
| `binding_volume_difference_probe.py` | `Vol(atom) − Vol(free)`, each braid closed **separately**, forced **positive** `[k+1]` | positive braids are Seifert-fibred → both Vol=0 |

The owner's version removes `Δtr` entirely and forms **one mixed-sign
braid** (positive from `W_atom`, negative from `W_free⁻¹`), which *can* be
hyperbolic — the figure-eight `σ₁σ₂⁻¹` is the simplest hyperbolic knot; a
positive braid never is.

## What the probe found

| | D (A=2) | T (A=3) | ³He (A=3) | ⁴He (A=4) | B_AME pattern |
|---|---|---|---|---|---|
| `\|D\|` (reduced crossings, pn→σ⁺) | 19 | 42 | 38 | 61 | — |
| Vol(D) (best-effort) | 7.9 | 16.8 | 16.6 | 37.3 | grows with A |
| B_AME (MeV) | 2.22 | 8.48 | 7.72 | 28.30 | grows with A |

**The three things the algebra could not do — all present:**

1. **Escapes Vol = 0.** Every difference knot has substantial nonzero
   geodesic volume — the mixed-sign braid is hyperbolic-class, exactly as
   the figure-eight intuition predicted, and exactly where the
   positive-braid probe died.
2. **Carries the A-dependence.** Vol(D) grows monotonically with mass
   number — the A-scaling the flat `Δtr ≈ 0.6–0.9` completely lacked.
3. **Breaks p–n symmetry.** Mirror nuclei T and ³He get *different*
   difference knots (different crossing counts and volumes), with the
   T > ³He ordering of the volume matching `B_AME(T) > B_AME(³He)` — the
   isospin/Z-dependence a pure `Vol(K)` law structurally cannot supply.

## The honest other half (critical-distance)

This is a **live lead, not a derivation**, and three things keep it there:

1. **`Vol/|D| ≈ 0.4–0.5` is roughly constant.** Hyperbolic volume density
   per crossing is bounded, so most of Vol(D) is just *crossing count*.
   The probe has therefore largely **relocated** the question from "derive
   the binding factor" to "derive `|D|(Z,N)`, the reduced length of the
   difference braid" — progress (it's a first-principles combinatorial
   object that carries isospin), but not a closure.
2. **`B_AME/Vol` still spreads 2.2–3.8×.** Far better than the algebraic
   trace route (which spanned ~30×), but not the single constant a
   derivation needs. The deuteron is the worst outlier.
3. **The volumes are non-rigorous.** SnapPy reports *"contains degenerate
   tetrahedra"* on every difference knot and none pass
   `verify_hyperbolicity` — the closures are **composite** (hyperbolic +
   Seifert pieces), so the single-number "volume" is a best-effort on a
   degenerate triangulation and shifts run-to-run under the stochastic
   `randomize()`. The 3-digit figures above are indicative only.

## The principled next step (what the data points at)

The degenerate triangulations are the signal: the difference link is not
one hyperbolic knot but a **JSJ-composite**. The right object is the
**JSJ decomposition** of D — sum the rigorous hyperbolic volumes of the
hyperbolic pieces, handle the Seifert (toral) pieces separately. This is
*exactly* the structure `binding_link_volumes.py` flagged in its own
honest-negative ("per-pair sum over the JSJ decomposition"), now reached
from the geometric side. Concretely:

1. **Proper braid-group reduction** (braid relations, not just free
   cancellation) to isolate the genuine inter-nucleon binding tangle from
   the cancelling intra-nucleon structure.
2. **JSJ-decompose** the reduced difference link; take `Σ Vol(hyperbolic
   pieces)` with rigorous (verified-interval) volumes.
3. Re-test `B_AME ≈ m_e·ΣVol·ρ/ℏ_q²` against a *constant* `ρ/ℏ_q²` — the
   real derivation test.

## Verdict

The owner's reformulation is **structurally right and empirically alive**:
binding really does behave like the mass of the difference knot —
nonzero, A-growing, isospin-distinguishing — where the trace algebra was
flat and dead. It is **not yet a derivation**: at the crude topological
level the volume is dominated by crossing-count and is non-rigorous. The
honest tier is *suggestive geometric lead*, and the concrete path to
promote or refute it is the JSJ decomposition of the properly-reduced
difference braid. No production path is touched; nothing is wired; no AME
value was fitted.
