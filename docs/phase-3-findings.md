# Phase 3 — Atom-knot derivation: first findings

*Companion to `docs/path-to-1ppb-04-plan.md` Phase 3. Records the
initial attempt to replace the SnapPy census search in
`jsj_verification.py` with a direct braid-closure derivation.*

## Summary

The plan's step 1 — "atom braid β_{Z,N} ∈ B_{3A} via
`atom_braid_word_3A`" — is **insufficient as written**.  The word
produced by `atom_braid_word_3A` collapses the braid-group information
that the JSJ hyperbolic piece needs.

## The problem

`atom_braid_word_3A` (in `folio-assistant/computations/mass_at_3A_proper.py`)
emits the nucleon confinement chain as a **block**:

    g0 chain:   σ_0 · σ_0 · σ_0
    g1 chain:   σ_1⁻¹ · σ_1⁻¹ · σ_1⁻¹

This is equivalent in the Hecke algebra H_{3A}(q₀) to the braid-group
element

    (σ_0 · σ_1⁻¹)^3

because the Hecke algebra imposes the braid relation
σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}.  But these two words are
**different** elements of the braid group B_{3A} — they have different
Markov closures.

## Experimental verification (q₀ = 1.1097)

| word | closure | components | Vol |
|------|--------|-----------:|----:|
| `σ_0³ σ_1⁻³` (block)        | `snappy.Link(braid_closure=[1,1,1,-2,-2,-2])` | 1 | 2.05·10⁻⁶ (non-hyperbolic) |
| `(σ_0 σ_1⁻¹)³` (interleaved) | `snappy.Link(braid_closure=[1,-2,1,-2,1,-2])` | 3 | **7.3277 (= 8G = Vol(Borromean rings))** |

The interleaved form **is** the Borromean rings L6a4, whose complement
has volume 8G (8 times Catalan's constant).

## Fix

Added an `interleave` parameter to
`folio-assistant/computations/atom_link_derivation.py`:

- `interleave="block"` — reproduce the current behaviour (collapsed,
  non-hyperbolic).
- `interleave="interleaved"` — per nucleon, interleave its g_0 chain
  with its g_1 chain before emitting.  Restores braid-group
  faithfulness.

## Result with interleaved mode

All four light atoms **do** produce hyperbolic closures under
interleaved mode.  Volumes (float + 50-digit verified via SnapPy
ManifoldHP):

| atom | components | crossings | Vol_float | Vol_50digit | A·8G | err vs A·8G |
|------|-----------:|----------:|----------:|:-----------|-----:|------------:|
| D    | 3 | 23 | 20.5230 | 20.522817202562213956825578568814725140079015219955 | 14.66 | +40.0% |
| T    | 4 | 35 | 35.7121 | 35.712144838226308332064508475986184594673809242794 | 21.98 | +62.5% |
| ³He  | 4 | 35 | 25.8563 | 25.856306769460333538419003494036025228275871329306 | 21.98 | +17.6% |
| ⁴He  | 5 | 47 | 41.0458 | 41.045634405124427913651157137794451263113886131589 | 29.31 | +40.0% |

Compared to the Kashaev target B/ρ:

| atom | Vol_derived | B/m_e | err | B/(2m_e) | err |
|------|------------:|------:|----:|---------:|----:|
| D    | 20.52 |  4.35 | +371% |  2.18 | +843% |
| T    | 35.71 | 16.60 | +115% |  8.30 | +330% |
| ³He  | 25.86 | 15.10 | +71%  |  7.55 | +242% |
| ⁴He  | 41.05 | 55.37 | −26%  | 27.69 | +48% |

## Interpretation

Interleaved mode is **correct as a braid-group lift** but the
per-nucleon construction currently interleaves **all** g_0/g_1
factors, including the quark-pair addenda — not just the 3+3 pure
confinement factors.  The quark-pair addenda should probably be
appended (or attached as connect-summed components), not interleaved
with the confinement chain.

Likely next steps:

1. Try "confinement-only interleave, quark-pairs appended" — keep
   `(σ_0 σ_1⁻¹)^3` interleaved per nucleon, but leave the quark-pair
   σ/σ⁻¹ factors as a block after it.
2. Test whether the inter-nucleon crossings (at 3k+2) should be
   interleaved with the adjacent nucleon's confinement, or treated as
   Markov stabilizations.
3. Verify 3He = single Borromean (A·8G = 22) vs ⁴He = two Borromeans
   joined (4·8G = 29.3) and see if the interleaved output recovers
   these shapes.

## Key result

**The critical obstruction flagged in the handover plan's Phase 3 is
real**: naive use of `atom_braid_word_3A` cannot derive the atom's
knot.  The braid word needs a braid-group-faithful construction, and
the current per-nucleon block encoding collapses precisely the
braid-group information that determines link class.

This doc captures the finding; the corrected Phase 3 path needs more
work on the interleave policy before it will predict B(atom) from
braid closure alone.

## Pointers

- Script: `folio-assistant/computations/atom_link_derivation.py`
- Witness: `folio-assistant/computations/atom-link-derivation.witness.json`
- Related: `folio-assistant/computations/jsj_verification.py`
  (census-search variant — currently the authoritative path)
- Upstream: `folio-assistant/computations/mass_at_3A_proper.py`
  `atom_braid_word_3A` (block-form producer)
