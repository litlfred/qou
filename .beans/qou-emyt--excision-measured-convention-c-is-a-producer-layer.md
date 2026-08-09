---
# qou-emyt
title: 'EXCISION (measured): convention C is a PRODUCER-layer problem -- 70 producers, 86 witnesses, 12 content blocks'
status: todo
type: task
created_at: 2026-08-09T19:35:36Z
updated_at: 2026-08-09T19:35:36Z
---


## What the ruling asked for, and what it actually costs

Owner ruling 2026-08-09: **"excise all convention C"**, "switch to D, we need to be
consistent anywhere." The scope was estimated from a grep (`181 files match`).
That estimate was wrong in an important way — most of those matches are
*labelled* C references (history, comparisons, excision notes) which are fine
and should stay. The real surface is smaller in content and far larger in code.

Measured 2026-08-09 with the new mechanical axis
`content/pipeline/trace-convention-audit.ts` (committed 997cfca7a, selftest 10/10):

| layer | C sites | note |
|---|---|---|
| live producers hardcoding `z_C = 1/(q^½+q^-½)` | **70** | `computations/`, `qou-mass/`, `tools/`; excludes `_deprecated/` |
| committed witness JSONs carrying a C value | **86** | regenerate-only, never hand-edit |
| content blocks failing the axis | **12** | 1 critical + 11 `gram-inverse-unqualified` |
| shipped `qou-mass` package | **1** | |

Content sweep: 3108 blocks scanned, 646 in scope, 12 failing. So the content
layer is ~2% of the job. **The excision is a producer-layer change**, and every
producer touched drags its witnesses with it.

## The one critical content defect

`prf:interface-knot-markov-z`
(`content/quantum-observable-universe/mass-theory/interface-knot-markov-z-proof.md:56`)
— the 4-atom verification table is entirely convention-C arithmetic:

| atom | p₊ | p₋ | in the block (C) | under production D | shift |
|---|---|---|---|---|---|
| D    | 1 | 0 | 0.49932033 | 0.61268803 | +22.7% |
| T    | 1 | 1 | 0.14493273 | 0.24729788 | +70.6% |
| ³He  | 2 | 0 | 0.24932079 | 0.37538663 | +50.6% |
| ⁴He  | 2 | 1 | 0.07236786 | 0.15151645 | **+109.4%** |

(computed at 60 dps with `decimal`, NO-FLOAT64 respected; `h = q − q⁻¹ =
0.20906029879563931543`, `z_C = 0.49932033418369445241`,
`z_D = 0.61268803714646525160`.)

**Two defects in one block.** Besides the convention, it claims "Max rel. err.
across all 4 atoms: ~10⁻¹⁵ — exact at f64 precision" — a float64 claim under a
NO-FLOAT64 directive.

**Do not hand-edit this table.** Producer is `computations/mass_at_3A_proper.py`
(`atom_braid_word_3A`) via `pyhecke_native`; regenerate under D.

**The identity itself is convention-independent.** `tr_M^FULL/tr_M^CONSTIT =
z^{p₊}(z−h)^{p₋}` follows from the Markov property plus the Hecke quadratic
relation and holds for *any* Markov parameter `z`. So regenerating under D
should reproduce agreement to the same ~10⁻¹⁵ — and if it does, the block gets
*stronger*, because the identity is then confirmed at two independent values of
`z` rather than one. That is the check to run, not a number to retype.

## The 11 `gram-inverse-unqualified` blocks are a MATH defect, not a label defect

These assert the Markov pairing on `H_n(q)` is non-degenerate, that
`det G ≠ 0`, and that `G⁻¹` enters the Frobenius co-Casimir
`C = Σ (G⁻¹)_{ij} b_i b_j`. Under D **all of that is false about `H_n`**:
`y₍₁³₎ = 0`, so the antisymmetric block *is* the radical and `det G = 0` exactly.

Not "numerically singular" — exactly. Under C, `y₍₁³₎ = 0.0227449…` is small but
nonzero and `G` genuinely inverts. A `G⁻¹` computed under C is **not an
approximation** to one under D, because the latter does not exist.

Blocks affected:
- `prop:vertex-algebra-relations` (climax-volume-mass) md:249
- `prf:shell-closure-stability` (knots-particles-confinement) md:27
- `def:frobenius-dual-h3` (mass-theory) md:2, 11
- `rem:frobenius-gram-matrix-context` (mass-theory) md:5, 6
- `prop:frobenius-gram-matrix` (mass-theory) ts:37
- `rem:gram-matrix-spectral-connection` (mass-theory) md:9,10,12,14,33,68,77,78 ← worst
- `prf:operator-selection-lp` (mass-theory) md:56
- `rem:confinement-frobenius-reciprocity-interpretation` (nuclear-interactions) md:7,20,23
- `sec:garside-gram-intro` (nuclear-interactions) md:1
- `conj:e-hartree-categorical-derivation` (predicted-spectra) md:49
- `prf:knot-operator-selection` (predicted-spectra) md:44

**The repair is citation, not deletion.** The Frobenius structure is real — it
lives on `H_n / rad τ ≅ TL_n(δ)`, not on `H_n`. `QOU/QBeta/MarkovGramDegenerate.lean`
proves both halves so each block can be repaired by pointing at a theorem:

1. `TemperleyLiebTower.conventionD_kills_antisymmetriser` — the pin forces `y₍₁³₎ = 0`
2. `block_mem_radical` — a zero-weight block lies in the trace radical (cyclicity is the content)
3. `gram_det_eq_zero_of_radical_combination` — a radical element in the span puts a
   nonzero vector in `ker G`, so `det G = 0` ← **this refutes the 11 blocks**
4. `TemperleyLiebTower.traceRadical_two_sided` — radical is a two-sided ideal, quotient is a ring
5. `pairing_descends` — the pairing is constant on radical cosets
6. `mem_radical_of_pairing_zero` — and is non-degenerate on the quotient
   ← **this tells the 11 blocks where to move the claim**

Corank accounting (`RankAccounting` section): `n=3` corank 1, `n=4` corank 10
(`3²+1²`), `n=5` corank 78 (`6²+5²+4²+1²`).

## Order of attack

1. ✅ mechanical axis committed, so a relapse is detectable (997cfca7a)
2. ✅ Lean refutation + descent (`MarkovGramDegenerate.lean`)
3. repair the 11 gram blocks by citation — cheap once (2) builds
4. regenerate `prf:interface-knot-markov-z` from its producer under D
5. the 70 producers + 86 witnesses — **needs a scoped plan and owner sign-off on
   blast radius**: this moves published numbers (per the registry, 195.8 ppm on
   β_Bor and −197 ppm on m_p). Do NOT start this as a text substitution.

## NEEDS OWNER

Step 5 is the real excision and it is not a mechanical edit. Two sub-questions:
- do the 70 producers switch to D wholesale, or does each get audited for whether
  its result is convention-scoped at all (many may be C-independent)?
- the 86 witnesses regenerate from their producers — but that is 86 producer runs,
  serialised (never two producers concurrently in one checkout).

---

## CORRECTION (same session): the producer count above is WRONG

The "70 producers" figure in the table above, and in commit 8e8860509's message,
is an artefact of a loose grep. The pattern included a bare `0.5 + ` alternative,
which matches any occurrence of that string anywhere in any Python file — it was
not measuring convention C at all.

Re-measured with patterns that actually pin the convention-C definition of `z`
(`q0**0.5 + q0**(-0.5)`, `Q0**0.5 + Q_INV0**0.5`, `q_half + q_half_inv`,
`sqrt(q) + 1/sqrt(q)`, `A + 1/A`), excluding `_deprecated/`:

| layer | claimed | **actual** |
|---|---|---|
| live producers defining `z` the C way | 70 | **13** |
| witness JSONs with a C fingerprint | 86 | **59** at ≥8 sig digits (86 at ≥7 — the looser threshold pulls in short quotations) |
| content blocks failing the axis | 12 | 12 (unchanged — this one was mechanical) |

The 13:

```
computations/atom_mass_derived.py
computations/atom_mass_partition.py
computations/deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py
computations/deltalambda/nuclear_quotient_jones_torus_link_probe.py
computations/free-neutron-decay.py
computations/garside-irrep-qvalues.py
computations/mass-from-q-symbolic.py
computations/phase5/phase3b_universal_vs_knot_specific_decomposition.py
computations/qbeta/qbeta_habiro_phase5q_dn_refactorize.py
computations/qbeta/qbeta_symbolic_chain_alpha_b.py
computations/rigid_monoidal_gap_invariance_check.py
computations/substrate/deuteron_tower_fusion_frame_probe.py
computations/substrate/hecke_core_symbolic.py
```

Six other producers already define `z` the D way, and the registry's
`entry_points` are **all** convention D — which is the tell I should have taken
seriously before quoting 70. The mass/binding pipeline has already migrated; what
is left is a tail of probes and two or three live computations.

**This makes the excision materially smaller and changes the recommendation.**
It is no longer "needs a scoped plan and owner sign-off on blast radius" as a
blocker — 13 files is a reviewable change. The blast-radius question still stands
for whichever of the 13 feed published numbers (`atom_mass_derived.py`,
`mass-from-q-symbolic.py`, `free-neutron-decay.py` are the ones to check first),
but the other ten look like probes whose results are convention-scoped anyway.

Lesson for the axis: the mechanical content sweep was right (12, and it stayed
12). The two numbers I got wrong were both hand-greps done outside the
instrument. Where a detector exists, quote the detector.
