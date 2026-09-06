# The ℏ_q⁰ floor is interface parity — and it is invariant under both contested word conventions

**Date:** 2026-09-06
**Bean:** `qou-zrx2` (GAP: the signed trace difference has an ℏ_q⁰ classical floor)
**Probes:**
[`classical_floor_is_markov_cycle_count_probe.py`](../../computations/probes/classical_floor_is_markov_cycle_count_probe.py),
[`classical_floor_is_interface_parity_probe.py`](../../computations/probes/classical_floor_is_interface_parity_probe.py)
**Scope:** (a) scope-limited. Exact `Fraction`/integer arithmetic; `q` is never evaluated. No
witness, nothing wired, no Lean, no content block.

## 🛑 First: I re-derived work that was already on `main`

`computations/probes/classical_floor_derivation_probe.py` and
[`QOU/MassTheory/ClassicalTraceFloor.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ClassicalTraceFloor.lean)
(sorry-free), landed by commit `7d15b2abbc` on 2026-09-04, **already** derive this floor by
Schur–Weyl, **already** establish `c(σ_free) = 2A` and `c(σ_atom) = A+1` for `A = 2 … 20`, and
**already** state `c₀(A) = 2^(−A) − 2^(1−2A)`. So does the `⚠ CORRECTED 2026-08-31` note inside
`derivation_chain.E_0_CONVENTIONS["B_q_value_absorbed"]`, which cites both by name.

`classical_floor_is_markov_cycle_count_probe.py` (PR #6879) re-derived all of that without finding
it. That is a corpus-grep failure on my part — the artifacts are on `main`, under obvious names, and
one grep for `classical_floor` would have returned them. It is **not** a discovery and must not be
cited as one. What it legitimately is: an **independent confirmation by a different route**. It
reaches `dim V_λ / 2^n` from convention D's row cap `y_λ = [n−2k+1]_q/[2]_q^n`; the prior probe
reaches the same place from `y_λ = s_λ(1,Q)/(1+Q)^n` with `Q = q²` (bean `qou-ssz6`). Two normalisers
agreeing at `q = 1` is worth having on the record, and that is the whole of its value.

**What is new is this document's subject and only this**: the interface-multiplicity generalisation,
the parity law, the convention invariance, and `A = 1`. Grep-verified against both prior artifacts:
**zero** occurrences of `m_pp` / `m_pn` / `m_nn` / `multiplic` / `parity` / `intra_order` /
`pn_convention`, and no `A = 1` row. The prior work fixes `m = 1` throughout, which is why `A + 1`
appears there as a fact rather than as the `O = A − 1` special case it is.

## The claim

`qou-zrx2` measured that the binding observable `tr_M(W_free) − tr_M(W_atom)` does **not** vanish at
`q = 1`, leaving floors of `1/8` (deuteron) and `7/128` (⁴He), and read them as *"a topological
remainder: the free word and the atom word close to different links whatever `q` is."* Right, and
qualitative. The floor is

    floor(A, O)  =  2^(−A) · (1 − 2^(−O))

where `A = Z + N` and `O` is the number of inter-nucleon interfaces whose crossing multiplicity is
**odd**. Under the canonical `m_pp = m_pn = m_nn = 1` every interface is odd, so `O = A − 1` and

    floor(A)  =  2^(−A) − 2^(1−2A)  =  (2^(A−1) − 1) / 2^(2A−1)

`1/8` at `A = 2` and `7/128` at `A = 4`, matching the bean's independently-swept values exactly.

## How it is derived

This section is the part already on `main` (see the banner above); it is restated because the parity
result below is built on it, and because the route through convention D's row cap is a second
independent path to step 1. Four steps; only the third is checked rather than quoted, and it is
checked in integers.

1. Convention D gives `y_λ = [n−2k+1]_q / [2]_q^n`, zero off ≤2 rows. At `q = 1` that is
   `(n−2k+1)/2^n`, and `n − 2k + 1` is exactly `dim V_λ`, the `sl₂` irrep dimension of `(n−k, k)`.
2. So `tr_M(w)|_1 = Σ_λ y_λ χ^λ(w) = (1/2^n)·Σ_λ dim(V_λ)·χ^λ(w)`.
3. **`Σ_λ dim(V_λ)·χ^λ(w)` is the trace of `w` place-permuting `(ℂ²)^⊗n`** — Schur–Weyl — and equals
   `2^cyc(w)`. Verified by counting the basis states `w` fixes: **6/6 exactly**, across D, T and ⁴He,
   free and atom words.
4. Hence `tr_M(w)|_1 = 2^(cyc w − n) = z₁^(n − cyc w)` with `z₁ = z_D(1) = q³/(q²+1)|_{q=1} = 1/2`,
   and the floor is the difference of two such terms.

The cycle counts are then not per-isotope lookups. Measured exactly for `A = 1 … 20`:

    cyc W_free = 2A                    cyc W_atom = 2A − O

**Why parity.** At `q = 1` the deformation parameter `h = q − 1/q` is `0`, so all three letter
classes — `σ` (`d = 0`), `σ⁻¹` (`d = −h`) and the averaged `σ − (h/2)·1` — collapse to the same
transposition `s_g`. An interface applied `m` times contributes `s_g^m`, which is `s_g` for odd `m`
and the **identity** for even `m`. The interfaces sit along a chain
(`ordering = ['p']*Z + ['n']*N`, interface `k` at generator `3k+2`), so each odd one attaches a fresh
nucleon to the growing blob and always merges two distinct cycles, dropping `cyc` by one. Even ones
do nothing. `cyc W_free` is the `O = 0` case.

Predicted-from-`(Z, N, m)` against measured-from-the-word agrees on every configuration tested,
including mixed-parity ones (`m_nn = 2` at `A = 6`: `O = 3`, floor `7/512`).

## What this changes for the bean

### 1. The floor is invariant under both word conventions the corpus argues about

Identical rationals under `intra_order ∈ {borromean, grouped}` and
`pn_convention ∈ {bring_color_weighted, strict_averaged}`, at `A = 2, 3, 4, 6`, and under both at
once. Those choices are not small — the intra reordering alone moved absolute traces by `3.785×`
(²H) to `14.325×` (⁴He) — and they do not touch this.

**So the floor is not the source of the `5.35×` `E₀` disagreement** `qou-zrx2` catalogues between
`binding_canonical.binding_canonical` (`0.4354 MeV`) and
`derive_binding_chain_cooperative.bond_binding` (`2.3297 MeV`) on the identical deuteron trace
difference. That ratio is a scale choice and is a separate defect (`qou-59j5`). This **narrows** the
bean; it does not resolve it.

### 2. The floor is exactly zero for a single nucleon

`A = 1` has no interface, so `O = 0` and `cyc W_free = cyc W_atom = 2`. The ℏ_q⁰ contamination is
created by binding; it is not carried by the nucleon.

### 3. 🛑 The floor can be zeroed by an even multiplicity — that is a diagnostic, not a repair

`m_pp = m_pn = m_nn = 2` gives `O = 0` and `floor ≡ 0` at every `A`, measured. **Do not read that as
a fix.** Choosing the interface multiplicity because it makes the observable cleanly ℏ_q¹ is
selection against the target — a fit in the exact sense AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3"
names, with no continuous parameter tuned and a free choice made all the same. `m = 1` is the
modelling choice the corpus made on other grounds and stands or falls on those grounds. What this
licenses is a statement about the observable's structure, not a change to the word.

### 4. The contamination is exponentially small in A

`floor·2^A = 1 − 2^(1−A) → 1`, so `floor ~ 2^(−A)` from below:

| A | floor | decimal |
|---|---|---|
| 1 | 0 | 0 |
| 2 | 1/8 | 0.125 |
| 4 | 7/128 | 0.0546875 |
| 8 | 127/32768 | 0.003875732 |
| 12 | 2047/8388608 | 0.000244021 |
| 20 | 524287/549755813888 | 0.000000954 |

Against `qou-zrx2`'s measured fractions of the full trace difference — 22.46 % (D), 4.88 % (⁴He) —
this is a **light-nucleus** problem. It does not thereby go away: the observable is still a sum of
two different ℏ_q orders at every `A`, and no single `E₀` scale pairs with both.

## What remains open

The bean's actual subject is untouched. Explaining the floor does not choose an `E₀` convention, and
`derivation_chain.E_0_CONVENTIONS["B_q_value_absorbed"]`'s claim that *"the trace-difference operator
carries the ℏ_q² scaling"* is still wrong on two counts: the leading term is ℏ_q⁰, not ℏ_q², and the
deformation part above it is ℏ_q¹. If anything a floor with a clean parameter-free closed form is
*more* clearly a genuine ℏ_q⁰ term and less dismissible as numerical noise, so the bean's own
conclusion — *"its two parts sit at different orders, and no single scale can pair with it"* —
stands undisturbed.

## Falsification

Every row of the prediction table is an exact rational an ℏ_q sweep must return. `T`/`³He` (`3/32`),
`⁶Li` (`31/2048`), `⁷Li` (`63/8192`) and `¹²C` (`2047/8388608`) were never measured by the bean. One
sweep returning a different rational refutes the closed form.
