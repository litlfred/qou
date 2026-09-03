# Owner decision needed: which knot is the deuteron?

> **🟧 OWNER RULING (2026-08-29): Option A.** The deuteron knot is the canonical
> braid closure (trefoil / Hopf, Vol = 0), with the explicit corollary that **the
> deuteron binding is NOT a hyperbolic-volume term** (the Bloch volume leg is proved
> identically 0). The 2-body binding is to be sourced from the **Gram/Frobenius
> pairing (⟨g,g⟩) + confinement SDP** channel, not the volume leg. Item 4 of the
> bk-crossing arc is re-scoped accordingly; the 6₂ census assignment is retired as a
> bare lookup. This resolves the `qou-e5jf` blocking ambiguity.

**Date:** 2026-08-29
**Tier:** decision (no new result — consolidates the blocking state for an owner ruling)
**Bean:** `qou-e5jf` (BLOCKING, todo) · **Arc:** bk-crossing mass-binding
**Why this is owner-facing:** it is a *choice of object*, not a computation. Every
2-nucleon-sector weight and the whole Bloch-group magnitude route depend on it, and the
corpus cannot resolve it from within — three derivation paths give three different knots.

## The disagreement

The corpus carries **three live, mutually inconsistent** deuteron knot assignments:

| Route | Knot | Vol | Source |
|---|---|---|---|
| braid-closure (canonical for Δ_λ) | trefoil T(2,3) | **0** (2 flat tetrahedra, shapes {1/2, 2}) | `deuteron-octahedral-gluing.witness.json` (SnapPy 3.3.2, 70 dps) |
| census-assigned | 6₂ | **4.40083251612** | `knot_volumes.py:139`, `binding_manybody_series.py:11`, 4 probes |
| linear-chain | Hopf L2a1 | **0** | `volume-binding-four-point.witness.json:87` |

The candidate Bloch term differs by the **whole of Vol(6₂) ≈ 4.40** between frames. You cannot
derive a knot invariant while the knot itself is undetermined — this is upstream of every
flattening/magnitude question and is where the extended-Bloch route actually stops.

## What is already settled (so the decision is clean)

- **Two of the three routes give Vol = 0** (trefoil and Hopf). Only the *census lookup* gives
  4.40, and it is assigned, not derived from the braid.
- **The volume leg is provably 0** on any real-shape triangulation at any tetrahedron count,
  flattening-independent — `QOU.MassTheory.BlochVolumeLeg` (PR #5242, sorry-free). So the
  canonical (braid-closure) frame yields **0 no matter how the triangulation is refined**.
- **One structural leg of the exclusion is machine-checked** (PR #5363, sorry-free):
  `ClosureComponentsSignInvariant.wordPerm_eq_of_indices_eq` — a signed braid word's induced
  permutation depends only on its index sequence, never on crossing signs, so the closure
  component count is sign-independent.
- **The `+0.2%` deuteron "match" was an artifact:** `volume-binding-four-point.witness.json`
  itself flags that it came from substituting Vol(𝓑₃) for Vol(Hopf) — an unjustified
  substitution. So the one apparent numerical success does not support any assignment.
- **The hyperbolicity ruling does not apply.** Owner ruling `qou-985x` ("assume hyperbolicity
  is granted") is about *whether* a manifold is hyperbolic, not *which* manifold — and the
  committed SnapPy data for the canonical braid closure says flat, Vol = 0.

## The decision (pick one)

- **Option A — the deuteron knot is the canonical braid closure (trefoil / Hopf, Vol = 0).**
  Consequence: the deuteron binding **cannot** come from a hyperbolic-volume term (it is exactly
  0, proved). The 2-body binding must then be sourced from a *different* mechanism (the
  coordination/crossing weight or a colour-trace term, not the volume leg). This is the
  evidence-favoured option: two routes agree, the volume leg is proved 0, and the 6₂ number is a
  bare census lookup.
- **Option B — the deuteron knot is 6₂ (Vol = 4.40).** Consequence: you must justify why the
  census assignment *overrides* the canonical braid-closure (the object the rest of the Δ_λ
  machinery is built on), and reconcile it with the proved Vol = 0 of that closure. Absent that
  justification this is fitting a volume to a target.
- **Option C — declare the identification genuinely open** and forbid any deuteron *magnitude*
  claim that depends on the knot until a derivation (not a census lookup) fixes it. This keeps
  the corpus honest but leaves the 2-body sector blocked.

## Recommendation

**A**, with the explicit corollary that the deuteron binding is *not* a volume term. It is the
only option consistent with the proved results (Vol = 0 canonical, volume leg proved 0) and it
does not require overriding the canonical braid closure with a census lookup. It also redirects
the 2-body search productively — toward the coordination/colour-trace weight (arc item 4),
where the recent Magnus Ω₂ progress already lives — instead of chasing a volume that is proved
to vanish. Technical detail: bean `qou-e5jf`.
