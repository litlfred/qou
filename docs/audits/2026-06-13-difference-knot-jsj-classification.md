# Difference-knot binding — JSJ classification + the two blockers (2026-06-13)

**Probe:** [`probes/difference_knot_jsj_classification_probe.py`](../../folio-assistant/computations/probes/difference_knot_jsj_classification_probe.py)
(witness `difference-knot-jsj-classification.witness.json`)
**Follows:** [`2026-06-13-difference-knot-binding-geometric-probe.md`](2026-06-13-difference-knot-binding-geometric-probe.md)
(PR #2235) and [`prop:binding-error-amplification`](../../content/quantum-observable-universe/mass-theory/binding-error-amplification.md)
(PR #2239).
**Status:** exploratory / research-status — records what is established and
the two hard blockers that gate promotion. Nothing wired; no fit.

## What is established

The owner-selected next steps were (2) JSJ-decompose the difference knot for
rigorous volumes, and (3) a per-knot-Vol amplification diagnostic. Running
both to the point where they stop:

### The difference link is composite, with `2A−1` components

| nucleus | A | `|D|` | cusps | `2A−1` | HP volume (non-rigorous) |
|---|---|---|---|---|---|
| ²H | 2 | 19 | 3 | 3 | ≈ 6.09 |
| ³H | 3 | 34 | 5 | 5 | ≈ 14.65 |
| ³He | 3 | 38 | 5 | 5 | ≈ 16.55 |
| ⁴He | 4 | 53 | 7 | 7 | ≈ 32.85 |

Two facts, both real:

1. **The cusp count is exactly `2A−1`.** The reduced difference braid
   `D = W_atom·W_free⁻¹` closes to a link with one component per *chain
   object* — `2A−1 = A` (nucleons) `+ (A−1)` (inter-nucleon interfaces).
   This is the *same* `2A−1` that appeared as `q₀^{10A−5} = q₀^{5(2A−1)}`
   in the (trace-refuted) residual law
   ([H1 audit](2026-06-13-9b-h1-exponent-location-refuted.md)). The
   chain-object count is therefore **geometrically real** — it is the
   difference link's component count — whereas the per-object weight (the
   "5", or the per-piece volume) is exactly what remains open.

2. **The links are composite, not single hyperbolic knots.** Every closure
   stays `"contains degenerate tetrahedra"` even under `ManifoldHP` after
   simplification — the signature of a JSJ union (hyperbolic + Seifert
   pieces), not one geometric manifold. The single-number "volume" above is
   a best-effort on a non-geometric triangulation and is not rigorous.

## Blocker 1 (option 2 — rigorous JSJ): Sage-only tooling

The rigorous promotion requires the JSJ torus decomposition and
interval-verified volumes. In SnapPy these are **Sage-only**:
`verify_hyperbolicity`, `canonical_retriangulation`, and `splitting_surfaces`
all raise `SageNotAvailable` outside Sage. The plain SnapPy in this sandbox
can detect that the links are composite (multi-cusp, degenerate) but cannot
rigorously decompose them or interval-verify a per-piece volume.

**Unblock:** run the per-piece volume sum inside Sage (or a manual JSJ
decomposition of each `2A−1`-component link), then test
`B_AME ≈ m_e · Σ Vol(hyperbolic pieces) · ρ / ℏ_q²` against a *constant*
prefactor. This is the decisive promote-or-refute step for the geometric
binding route; it is a clean, well-defined Sage task for the next session.

## Blocker 2 (option 3 — amplification diagnostic): tautological vs the table

The natural diagnostic — confirm the proven amplification identity
`binding_err ≈ (M/B)·mass_err` against the production mass table — is
**tautological**, and honesty requires saying so. The mass table computes the
bound-nucleus mass as `m_pred = Σ m_nucleon − B_pred` (binding_method
"E₀×q⁻¹"), so `m_pred` is *defined from* `B_pred`. Then
`m_err = −(B_pred − B_AME)` exactly, and `binding_err% / mass_err% = −M/B`
falls out of the definition, not from any independent prediction. It
re-derives [`prop:binding-error-amplification`](../../content/quantum-observable-universe/mass-theory/binding-error-amplification.md)
rather than testing it.

**Unblock:** the non-tautological test needs the bound-nucleus mass computed
*independently* of the binding — i.e. directly from
`m_e · Vol(K) · ρ(K) / ℏ_q²` with a **per-knot** `Vol(K)` (the 9a object),
not from `Σ m_nucleon − B_pred`. Production does not currently expose that
geometric bound mass for nuclei (it uses the magic-A formula), so wiring the
per-knot geometric mass for the bound nucleus is the prerequisite — itself
the owner-gated 9a per-knot-Vol task.

## Net

Both owner-selected steps converge on the **same prerequisite**: a per-knot
geometric quantity computed rigorously and independently — either the JSJ
per-piece volume sum of the difference link (Sage), or the direct geometric
bound mass `m_e·Vol(K)·ρ/ℏ_q²` with per-knot `Vol(K)` (9a). The amplification
theorem (PR #2239) is what makes this the right target: it proves the
bound-state mass is the lever, so the per-knot geometric mass — not a new
binding ansatz — is where the next real progress lives. The `2A−1`
chain-object structure (now confirmed as the difference link's component
count) is the scaffolding both routes share.
