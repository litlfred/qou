# Schur–Weyl push: the SU(2) row-count rule splits the lepton generations across spin vs colour

**Date:** 2026-06-22
**Branch:** `claude/keystone-schurweyl-su2-rowcount-2026-06-22`
**Status:** Positive/structural — an exact representation-theoretic selection rule with a sharp
generation-level consequence. No fit; no SU(2)-component↔W_λ numerical match asserted.
**Bean:** [`s5bb`](../../.beans/s5bb--s5-so3-keystone.md)
**Follows:** [`2026-06-22-keystone-wrt-color-schurweyl.md`](2026-06-22-keystone-wrt-color-schurweyl.md)
**Script:** [`scripts/keystone_schurweyl_su2_rowcount_probe.py`](scripts/keystone_schurweyl_su2_rowcount_probe.py)
**Witness:** [`computations/keystone-schurweyl-su2-rowcount.witness.json`](../../computations/keystone-schurweyl-su2-rowcount.witness.json)

## The bridge made concrete — the Schur–Weyl selection rule

The previous probe pinned the colour↔W_λ bridge to **Schur–Weyl duality**. The bridge carries one
exact, parameter-free fact:

> **GL(2)/SU(2) Schur–Weyl.** `(ℂ²)^{⊗n} = ⊕_{λ : ≤2 rows} S^λ ⊗ V_λ^{SU(2)}` — **only partitions with
> at most 2 rows appear** (`V_λ^{GL₂}=0` once λ has a third row). The 2-row block `λ=(n−k,k)`
> corresponds to SU(2) spin `j=(n−2k)/2` (Wilson-line colour `2j+1=n−2k+1`).

So the SU(2)-coloured Poincaré-sphere `S³/2I` WRT can reach **exactly the ≤2-row `W_λ`**; any ≥3-row
block is invisible to spin and needs `ℂ³` colour (SU(3), 3 rows) or higher.

## Applied to `λ ⊢ 5`

| λ | rows | SU(2)-reachable? | spin j | min SU(N) | `W_λ` | role |
|---|------|------------------|--------|-----------|-------|------|
| (5) | 1 | yes | 5/2 | SU(1) | 0.00762 | |
| (4,1) | 2 | yes | 3/2 | SU(2) | 0.12862 | |
| **(3,2)** | **2** | **yes** | **1/2** | **SU(2)** | **0.20754** | **muon** |
| **(3,1,1)** | **3** | **NO** | — | **SU(3)** | **0.29467** | **electron** |
| (2,2,1) | 3 | NO | — | SU(3) | 0.20754 | (3,2)-twin |
| (2,1,1,1) | 4 | NO | — | SU(4) | 0.12862 | |
| (1⁵) | 5 | NO | — | SU(5) | 0.00762 | |

- **SU(2)-reachable (≤2-row):** {(5), (4,1), (3,2)} ↔ spins {5/2, 3/2, 1/2}.
- **Needs colour SU(≥3) (≥3-row):** {(3,1,1), (2,2,1), (2,1,1,1), (1⁵)}.

## The sharp consequence — generations split across the spin/colour boundary

The two lepton home blocks fall on **opposite sides** of the Schur–Weyl row-count boundary:

- **muon `(3,2)`** — 2 rows ⇒ **SU(2)-reachable** (spin `1/2`): it lives in the Poincaré-sphere
  (spin) WRT sector;
- **electron `(3,1,1)`** — 3 rows ⇒ **not spin-reachable** ⇒ a genuinely **colour `ℂ³` (SU(3))**
  object.

So the keystone **factorises**: the **spin sector** (≤2-row `W_λ`, including the muon) comes from the
`S³/2I` WRT; the **colour/≥3-row sector** (including the electron) is an **SU(3)** Schur–Weyl object.
This is exactly the corpus's **spacetime-spin-`ℂ²` ⊥ colour-`ℂ³`** split (#2364, and the Wu-manifold
obstruction's "independent factors" correction) — now appearing **at the generation level**, derived
from the exact Schur–Weyl row-count rather than posited.

## What this is, and what it is not

- **Is:** an exact representation-theoretic selection rule (the ≤2-row theorem) with a parameter-free,
  derive-not-fit consequence — the muon/electron blocks are spin/colour-separated.
- **Is not:** a numerical `SU(2)-WRT-component = W_λ` identity. That still needs the level-`k` modular
  `S`-matrix data for the spin sector (and the SU(3) coloured invariants for the colour sector),
  through the bar/Habiro bridge. No such match is asserted here (forcing one would be numerology).

## The keystone arc — where it now rests

The open object was driven, this session, through a strictly-narrowing chain, ending at an explicit
**factorisation**:

1. finite Sasakian + equivariant index *(arena ruled out)*;
2. modular block weights `d²/D²` *(reframe)*;
3. non-compact `E_q(2)` contraction at real `q₀` *(identification)*;
4. Habiro-WRT(Σ(2,3,5)) at `1/q₀` *(q-series operational)*;
5. colour-resolution + Schur–Weyl obstruction *(index bridge)*;
6. **here:** the Schur–Weyl **row-count rule** factorises `W_λ` into a **spin sector** (≤2-row,
   Poincaré-WRT, *muon*) and a **colour sector** (≥3-row, SU(3), *electron*).

The remaining work is the per-sector numerical realisation (spin: level-`k` `S`-matrix of `S³/2I`;
colour: SU(3) coloured invariants), each a finitely-stated rep-theory + q-series object — **not
differential geometry**.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-22-keystone-wrt-color-schurweyl.md`](2026-06-22-keystone-wrt-color-schurweyl.md) — the colour-resolution + Schur–Weyl obstruction this makes concrete.
- [`2026-06-22-keystone-habiro-wrt-s3-2i.md`](2026-06-22-keystone-habiro-wrt-s3-2i.md) — the bare WRT invariant + bar/Habiro bridge.
- [`2026-06-16-keystone-wu-manifold-reeb-obstruction.md`](2026-06-16-keystone-wu-manifold-reeb-obstruction.md) — the independent spacetime⊥colour factorisation (#2364) this realises at generation level.
