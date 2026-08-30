# Nucleon construction: the reader measurement, and two corrections to my own framing

**Date:** 2026-08-30 · **Bean:** `qou-1qsw` · **Status:** measurement complete,
migration NOT executed

The owner authorised "measure first, then retire the 9-crossing, and also
retire braid-order #2". The measurement is below. It **contradicts the cost
basis the decision was made on**, and one of the three options I offered is not
a coherent operation. Recording before acting.

## What I told the author when the options were framed

| # | builder | readers | claimed cost of retiring |
|---|---|---|---|
| 1 | `build_nucleon_nf` (9 crossings) | 18 | 18 call sites |
| 2 | `build_atom_nf` / `_exact` (11, braid order) | 6 | "24 call sites total" |
| 3 | `nucleon_gen_chains` (11, monotone) | 53 | — (keep) |

Those figures came from the bean, recorded 2026-08-29. I quoted them without
re-measuring. Both are wrong against the live tree.

## What is actually there

Measured on `main` @ `adf471d341`, file-level, excluding `_deprecated` and the
defining module itself; "publishes" means a committed `*.witness.json` names
the producer in `scriptFile`.

| # | builder | readers | of which publish witnesses |
|---|---|---|---|
| 1 | `build_nucleon_nf` / `PROTON_NF` / `NEUTRON_NF` | **13** | **5** |
| 2 | `build_atom_nf` / `build_atom_nf_exact` | **30** | **16** |

The five publishers under #1: `atom_mass_derived`, `compound_shift_nf`,
`hadron_knot_table`, `integer_lp_gluon_convention_d`, `shift_from_nf_basis`.

The sixteen under #2 include `atomic_tr_m_mpfr_50dps`, which alone emits
**five** committed witnesses and is a canonical L1 producer, plus
`all_nuclides_sdp_admissibility`, `all_nuclides_wedderburn_spectral_v2`,
`molecular-frobenius-lp`, `universal-ilp` and
`sublemma_2_1_h9_tritium_verify` (2 witnesses).

## Correction 1 — the cost of retiring #2 is ~5× what I said

Not "6 readers, 24 call sites total" but **30 files and 16 published
witnesses**. Every one of those witnesses is a number currently on `main`.

## Correction 2 — retiring #2 "in favour of #3" is not a coherent operation

This is the more serious error, and it is in the framing rather than the count.

```
build_atom_nf(Z, N)              -> "Build atom NF via Hecke multiplication."
nucleon_gen_chains(quarks, ...)  -> "Per-generator crossing chains for one nucleon."
```

**#2 is the ATOM-level builder; #3 is per-nucleon.** They are not two spellings
of one object and are not interchangeable. My options table listed all three
under "nucleon constructions", which is where the error entered: something must
still assemble atoms from nucleons, and #3 does not do that. "Retire #2" as
written would leave the atom layer with no builder.

There may still be a real question *inside* #2 — the per-nucleon word it lays
down is the braid-order one — but that is a different and smaller change than
retiring the function, and it is not what was authorised because it is not what
I described.

## What this does not disturb

**The 9-vs-11 decision stands and is unaffected.** Both arguments for it are
structural, not consumer-count arguments:

* the γγ→qq̄ SDP decomposes the proton into four components — H₃ for B₃, H₃ per
  quark pair, **H₂ for the 2·σ₀ gluon self-coupling**, and the LR cross-level
  embedding: 6 + 3 + 2 = 11;
* `QOU.QBeta.GluonVertexPsdParity.vertex_psd_iff_even` (sorry-free) makes σ₀²
  the minimal non-zero admissible gluon vertex.

`build_nucleon_nf` is the only model that drops that component, and retiring it
touches 13 readers of which 5 publish — smaller than I said, not larger.

## Recommendation

1. **Proceed with retiring #1**, sequenced: re-run the five publishers under
   both models, diff the witnesses, then migrate. Cost and blast radius are now
   measured and modest.
2. **Do not execute "retire #2"** on the authorisation given, because the
   authorisation was given for an operation I described incorrectly. If the
   intent was "make the per-nucleon word inside the atom builder monotone", that
   is a separate, much narrower change and should be re-framed and re-decided on
   its own terms.

---

# CORRECTION 2026-08-30 (later): "zero published numbers move" was wrong, and it was wrong because of a fourth counting error

The measurement above concluded that no published number moves. **That is
false.** The correct figure is **two assertions moving 50 % and 57.5 %**, in
the one publishing consumer I never ran.

## The fourth counting error

The AST scan that produced "7 real consumers" matched `ast.Name` nodes with the
target identifiers — which matches **assignment targets** as well as uses. So
`computations/atom_mass_derived.py` was counted as a consumer when in fact it
**defines its own**:

```python
PROTON_NF  = build_nucleon(['u', 'u', 'd'])     # line 271, its OWN build_nucleon
NEUTRON_NF = build_nucleon(['u', 'd', 'd'])
```

It never imports `pyhecke.atom`. Its witness not moving was therefore expected
and carried no information about the change — and I had reported it as the
main evidence that the change was inert.

## The corrected consumer set

Resolving by **import** rather than by name:

| class | count | files |
|---|---|---|
| true consumers (import the symbol) | **6** | `hadron_knot_table`, `hecke_core_legacy`, `qbeta_counit_silver_ratio_adjudication_probe`, `qbeta_nf_single_wrap_vs_typed_probe`, `substrate/hecke_core`, `qou-mass/_internal/hecke_core` |
| defines its own, same name | 1 | `atom_mass_derived` |
| text-only mention | 6 | — |

Layer-2 (importing the re-export from `hecke_core`) adds nothing new.

**Of the six true consumers, exactly one publishes a witness:
`hadron_knot_table`** — and it is the one that could not be run, because it
does not finish (deuterium alone >50 min; AGENTS.md).

So "zero published numbers moved" measured five producers of which **none was
a consumer of the changed function**.

## The actual blast radius, measured directly

`hadron_knot_table` calls `build_nucleon_nf(quark_list)` for exactly the rows
that pass `quarks` — `("proton", 1, 0, "uud")` and `("neutron", 0, 1, "udd")`.
Every other row goes through `build_atom_nf`, which this change does not touch.

Computing `nf_tr` on the new NF against the committed witness's assertions:

| assertion | committed (9×) | new (11×) | change | Frobenius |
|---|---|---|---|---|
| `tr_M(proton)` | 0.419562177934 | **0.629328402203** | **+50.00 %** | stable |
| `tr_M(neutron)` | 0.301675079767 | **0.475133517156** | **+57.50 %** | stable |

The other **21 of 23** assertions are unaffected.

**A third exact cross-check falls out of this.** The new `tr_M(proton) =
0.629328402203` matches the braid-order value this bean recorded earlier —
`tr_M braid-order = 0.62932840220292191817` — to every printed digit. The
11-crossing `build_nucleon_nf` now reproduces the braid-order nucleon exactly,
which is what it should do, and is a check the change was not tuned against.

## Consequence: this is NOT safe to land as it stands

Landing the code change makes `computations/hadron-knot-table.witness.json`
stale by 50 % on two assertions, and **the witness cannot be regenerated in
this container** — the producer does not finish. Hand-editing the two numbers
is forbidden. Truncating the ATOMS list would produce a different witness, not
a regenerated one.

The correct sequencing is: regenerate `hadron-knot-table.witness.json` in an
environment that can run the producer to completion, in the same change as the
code. Until then the code change should not merge.
