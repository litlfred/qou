# Retraction — the binding difference link is non-hyperbolic; its "volume" was SnapPy noise

**Date:** 2026-06-13 · **Probe:** [`probes/difference_knot_hyperbolicity_check.py`](../../computations/probes/difference_knot_hyperbolicity_check.py)
(witness `difference-knot-hyperbolicity-check.witness.json`)
**Retracts the quantitative claims of:** [PR #2235](https://github.com/litlfred/qou/pull/2235)
([`2026-06-13-difference-knot-binding-geometric-probe.md`](2026-06-13-difference-knot-binding-geometric-probe.md))
and [PR #2242](https://github.com/litlfred/qou/pull/2242)
([`2026-06-13-difference-knot-jsj-classification.md`](2026-06-13-difference-knot-jsj-classification.md)).
**Unaffected:** [`prop:binding-error-amplification`](../../content/quantum-observable-universe/mass-theory/binding-error-amplification.md)
(PR #2239) — a proven theorem, independent of any knot volume.

## The claim being retracted

PR #2235 reported that the binding difference link
`D = W_atom·W_free⁻¹` (Hecke weights stripped to crossing signs,
free-reduced, closed) has "nonzero, A-growing, p–n-distinguishing
hyperbolic volume" and called it a live geometric binding lead; PR #2242
reported per-nucleus high-precision volumes and a `2A−1` cusp structure.
Those volume numbers came from SnapPy's `.volume()` on the link complement,
**trusted without checking that the manifold is hyperbolic**. It is not.

## The decisive checks (run on Regina + SnapPy, this sandbox)

| nucleus | SnapPy vol cv (25 trials) | vmin | negatives /25 | Regina `isIrreducible` | `isHaken` |
|---|---|---|---|---|---|
| ²H | 135 % | **−1.80** | 8 | **False** | False |
| ³H | 96 % | **−5.87** | 4 | **False** | False |
| ³He | 55 % | **−3.10** | 2 | **False** | False |
| ⁴He | 25 % | +8.72 | 0 | **False** | False |

Three independent facts, each sufficient on its own:

1. **Negative "volumes."** A hyperbolic volume is positive and
   triangulation-independent. SnapPy returns *negative* values on the
   deuteron/tritium/³He links — the number is meaningless (a degenerate
   non-geometric triangulation), not a volume.
2. **29–135 % coefficient of variation.** Re-randomising the triangulation
   changes the "volume" by tens of percent. A genuine invariant does not
   move. The earlier "growth with A" and "T ≠ ³He distinction" were *within
   this noise*.
3. **`isIrreducible() = False` (Regina, Sage-free).** The link complements
   contain essential 2-spheres — the links are **split / reducible**. A
   reducible 3-manifold is **never hyperbolic** (hyperbolic ⇒ irreducible
   atoroidal). Definitive, and independent of any numerical triangulation.

## What went wrong, and what it converges with

The error was trusting `Manifold.volume()` without `verify_hyperbolicity`
(Sage-only) or a stability/irreducibility check. Installing **Regina**
(`pip install regina` — JSJ/decomposition without Sage) and a 25-trial
stability sweep exposes the artifact immediately.

This converges with a result already in the corpus:
[`binding_volume_difference_probe.py`](../../computations/probes/binding_volume_difference_probe.py)
found the *derived braid closures* non-hyperbolic ("Seifert-fibred /
degenerate, Vol ≈ 0") and concluded the only genuine hyperbolic volumes come
from the **hand-assigned census knots**. The corpus was right; PR #2235
re-walked into the same wall and misread SnapPy's noise as signal.

## What survives, and the corrected forward path

- **`prop:binding-error-amplification` (PR #2239) stands** — it is a pure
  error-propagation theorem (`binding error = δ·M/B`), with no dependence on
  any knot volume. The "9a gates 9b" conclusion is unchanged.
- **The geometric binding route is not dead, but the realisation is
  different.** The hyperbolic objects are the **hand-assigned census
  binding-links** (Hopf, 8₁₁, L6a4 — these *are* hyperbolic, e.g.
  Vol(8₁₁) = 8.286), per `binding_link_volumes.py`. The open problem is
  therefore the **assignment** itself — *which* hyperbolic knot is each
  nucleus's binding-link — i.e. [`conj:canonical-knot-id-sdp`](../../content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md),
  not a volume read off the raw difference braid. The volume-matching
  adjudication (PR #2192) is the live evidence there.

## Blocker 2 (the amplification "test") — dissolved, not unblocked

The earlier "independent geometric bound mass" needed to make the
amplification test non-tautological **does not exist as a separate
quantity**: physically the bound-state mass *is* `Σ m_nucleon − B`, so any
computation of it requires computing the binding. The amplification identity
is a **proven theorem** (PR #2239); it does not need — and cannot be given —
an independent empirical confirmation against a circular mass table. The
right object to compute is the binding itself (via the correctly-assigned
hyperbolic census knot), not a redundant "bound mass."

## Net

Using the proper tools (Regina + a stability sweep) on the two owner-selected
blockers produced a clean negative: the raw difference-knot volume is an
artifact (Blocker 1), and the amplification test has no non-circular form
(Blocker 2). Both redirect to the same real object — the
correctly-assigned **hyperbolic census binding-link** — and the proven
amplification theorem remains the one durable result. Closing a false lead
with rigorous tooling is the progress here.
