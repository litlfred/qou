# The recorded Φ₃ column discriminates the four candidate strand counts

**Date:** 2026-09-12
**Bean:** `qou-jgg0` (the two atomic braids sharing a name and the symbol `𝒜`)
**Probe:** [`computations/probes/phi3_column_discriminates_the_strand_count_probe.py`](../../computations/probes/phi3_column_discriminates_the_strand_count_probe.py) — 35/35, exit 0
**Owner ruling recorded:** option (a), `A+Z`, taken as a *scoping* decision — see §7

---

## 0. What this adds

Bean `qou-jgg0` established on 2026-09-05 that the corpus carries two different
objects called "the atomic braid", both written `𝒜`, and on 2026-09-06 that the
disagreement is really a 2×2 with four live cells. Through 2026-09-11 the arc
measured **where** each reading is carried — content blocks, Lean, Python — and
**what turns on** the choice, but it never found a quantity that *decides* it.
The bean's own framing was a naming problem with a priced consequence.

There is a quantity, and it was already in the corpus, unconnected: **the
recorded Φ₃ column of the Z=1–20 atomic mass table.** It separates the four
cells, and only one of them reproduces it.

## 1. The four cells

|  | electrons in | electrons out |
|---|---|---|
| **nucleon-strand** | `A+Z` — `def:atomic-braid` — **(a)** | `A` — a declared "Default-coarse" approximation |
| **quark-strand** | `3A+Z` — `atomic-mass-gb-nf.md:3` — **(c)** | `3A` — production `atom_braid_word_3A` — **(b)** |

`A < A+Z < 3A < 3A+Z` strictly over all `Z ∈ 1..60, N ∈ 0..60` — 3600 pairs,
zero coincidences (probe check 4), so nothing reconciles them by accident.

## 2. The target, and its provenance

[`phi_allpairs_reconstruction.py`](../../computations/phi_allpairs_reconstruction.py)
(on `main`, `1fe569c05`) closes Φ₂ and Φ₃ of `thm:wedderburn-mass-formula`:

    Φ₃ = w · ln q,   w = 2[ 2·C(Z,2) − C(N,2) − Z² ] = −2Z − N(N−1)

exact on **19 of 19** non-hydrogen rows. Ar is a **held-out** confirmation: it is
the row that refuted the previous candidate `−Z(2N−Z+1)`.

The `w` integers come from `computations/wedderburn_mass_table_z1_20.py:116-132`,
whose Φ₃ column traces to the witness `atom-mass-complete-wedderburn` —
**recovered, and out of tree since the miga split.** Verified rather than
assumed (check 2): every recorded Φ₃ decimal is `w · ln q₀` with `w` an exact
integer, at the proton pin, to a worst relative deviation of **1.23e-5** —
uniform across rows, i.e. the six-decimal recording precision, not a mismatch.

**Known defect in the target, stated up front:** that producer's own third
coefficient is `β₃ = 0.0499` while the published formula carries
`h_A² = 0.0437073`, a 14.2 % departure; `β₃` reproduces 20/20 published masses
and `h_A²` reproduces 0/20
([`wedderburn_beta3_vs_hA2_discrimination.py`](../../computations/audits/wedderburn_beta3_vs_hA2_discrimination.py)).
That coefficient *multiplies* Φ₃, so it does not touch the integer column this
result rests on — but it is an open defect on the same object and should not be
discovered later by someone reading this.

## 3. The signs are derived, not transcribed

`phi_allpairs_reconstruction.py` hardcodes the six Φ₃ signs. This probe derives
them from `tbl:atomic-braid-table1-data`'s own `(c, d)` values by exact symbolic
arithmetic (check 3): with `λ_sym = cq + d` and `λ_alt = −c/q + d`, the term
`ln|λ_sym/λ_alt|` is `k·ln q` for an integer `k`, and

| pair | crossing | `(c, d)` | derived `k` |
|---|---|---|---|
| `pp` | `σ` | `(1, 0)` | **+2** |
| `nn` | `σ⁻¹` | `(1, −h)` | **−2** |
| `pn` | `½(σ+σ⁻¹)` | `(2, −h)` | **0** |
| `pe` | `σ⁻¹` | `(1, −h)` | **−2** |
| `ne` | `id` | `(0, 1)` | **0** |
| `ee` | `σ` | `(1, 0)` | **+2** |

Three of the six are electronic. The pair *counts* `C(Z,2)` (ee) and `Z²` (pe)
presuppose `Z` electron strands — that is cell (a), and nothing else.

## 4. Parameter-free result

Table 1's signs, each cell's own pair counts, exact integers, no tolerance:

| cell | reproduces the column | He, against a recorded −6 |
|---|---|---|
| `A` | **0/19** | 0 |
| **`A+Z` — (a)** | **19/19** | **−6** |
| `3A` — (b) | **0/19** | 0 |
| `3A+Z` — (c) | **0/19** | −22 |

The electron contribution has an exact closed form, on all 20 rows:

    w(A+Z) − w(A) = 2[ C(Z,2) − Z² ] = −Z(Z+1)

At Ar that is **342** — the difference between `−498` recorded and `−156`
electron-free.

## 5. Now grant each cell a fit

Deliberately generous to (b) and (c), run symmetrically on every cell, and
labelled a fit. Exact rational Cramer solve over all 969 anchor triples, best
kept:

| cell | best fit | coefficients | integral? |
|---|---|---|---|
| `A` | 18/19 | `(2, 0, −2)` | yes — **misses Ar, and only Ar** |
| **`A+Z` — (a)** | **19/19** | **`(4, −2, −2)`** | **yes** |
| `3A` — (b) | 10/19 | `(7/15, 1/5, −4/9)` | no |
| `3A+Z` — (c) | 10/19 | `(13/15, −1/5, −4/3)` | no |

Two things here matter more than the headline:

1. **The fit on (a)'s basis recovers the parameter-free answer.** `(4, −2, −2)`
   is `2(pp+ee)`, `2·nn`, `2·pe` read straight off Table 1 (check 14). A
   three-parameter search lands exactly on the values the crossing table already
   fixes.
2. **(b) and (c) cannot reach the column even when fitted**, and their best
   coefficients are fractions no crossing table produces.

The single row that separates the electron-free nucleon fit from the recorded
column is **Ar** — the only row with a large neutron excess (`Z=18, N=22`), and
the same row that carried the held-out confirmation in §2.

## 6. Scope — what this does NOT establish

- **Scope-(a), not a structural exclusion.** What is measured is that *these*
  pair-count constructions, on *these* bases, fail. A genuinely quark-level
  colour-weighted construction on `3A` is untested and is **not** excluded.
- **Φ₂ does not discriminate** (check 15): `Φ₂ = Z·N·ln(1+h²/4)`, and the `pn`
  count `Z·N` is identical under `A` and `A+Z`. Only Φ₃ separates them.
- **Φ₁ is not closed** under any reading and is untouched here.
- **Nothing about the mass formula's accuracy.** Declaring a reading canonical
  does not make the formula reproduce deuterium; it does not
  ([`wedderburn_Mi_constructor_test.py`](../../computations/wedderburn_Mi_constructor_test.py)).

## 7. A correction to the bean's own evidence

`qou-jgg0` offered, as its evidence *for* (b):

> *"For (b): nothing in `computations/` has ever built the `A+Z` object."*

**That is false** (check 16). `atom_gen_chains` / `atom_gen_chains_sym`
(`computations/substrate/hecke_core_symbolic.py:271`) build all-pairs nucleon
crossings **plus `Z` electrons each contributing `(1, −h)`** — the `pe` crossing.
Measured on `main` `03d6c9485`: that family has **23** importers; `atom_braid_word_3A`
has **380**; and **5 files import both**, among them
`tools/pyhecke/python/pyhecke/atom.py` (a library module) and
`scripts/word-provenance-gate.py` (a gate) — a live layer-straddle surface.
`computations/unified-mass-molecular.py` emits a witness and says so in its own
header: *"Full atomic braid `H_{A+Z}(q)`: nucleons + electrons."*

**Re-measure the counts; do not quote this line.** They are live file counts and
they move: the `3A` figure was **378** at `1c443dddc` a few hours earlier, and
two new sibling probes (`brng_dominant_summand_ursell_probe.py`,
`binding_word_3A_reembedding_probe.py`) took it to 380 without anything in this
analysis changing. What is durable is the **shape** — both objects are
implemented, `3A` by roughly sixteen times as many files, and a handful import
both — not the integers. Check 16 of the probe recomputes them on whatever base
it is run against, and asserts only the shape.

So the ledger entry that read "(a) has the definition, (b) has all the code" was
wrong in its second half. Both objects are implemented; they serve different
things.

## 8. The ruling

**Owner ruling, 2026-09-12: option (a).** `𝒜 ∈ H_{A+Z}(q)` is the atomic braid;
the production `3A` object is the electron-free nuclear core and keeps its own
already-registered name `𝓑_K ∈ H_{3A}(q)`
(`notation-register-table3-data.md:7`).

**The instrument is a scoping note plus a register entry, not a rename.** PR
#6952 recorded the corpus's own measurement that renaming the `3A` object costs
**685 call sites across 382 files**, considered and rejected in PR #5765. Under
(a) no rename is needed: the `3A` object already has a distinct registered
symbol, and what was missing was the statement that the two are different
objects.

**What stays open**, and `qou-jgg0` stays open with it (rule 13a):

- the `3A+Z` third cell in `mass-endomorphism/atomic-mass-gb-nf.md:3`;
- whether a quark-level construction could also reproduce Φ₃ (§6);
- Φ₁, and the `β₃` vs `h_A²` defect (§2);
- `qou-q6pp`'s wrong-signed p–n splitting, which this does not touch.
