---
# qou-3o59
title: 'CITE: eight arc Lean files carry zero -- Ref: lines while deferring premises to literature — C — the sorry-free cited-not-proved surface falls through the AGENTS.md §1 gate'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T09:07:37Z
updated_at: 2026-10-04T15:17:54Z
parent: qou-mub3
---

**Class C — the arc's cited-not-proved surface, measured: honest prose, zero
resolvable pointers.**

Nine Lean files carry the hyperbolic-volume / eightfold arc. **Eight of them have
zero `-- Ref:` lines**, while every one contains prose deferring an input to the
literature:

| file | `-- Ref:` lines | what it defers, and where |
|---|---:|---|
| `Eightfold/ContactDistributionRank.lean` | **0** | `:91` *"a cited fact about contact geometry"* (Darboux / `dim = 2n+1`) |
| `Eightfold/HyperbolicVolumeFormType.lean` | **0** | `:49` *"standard hyperbolic geometry, cited and not formalised"*; `:81,152` Mostow rigidity, `Vol(4₁) = 2·Cl₂(π/3)` — *"Both cited."* |
| `Eightfold/HookContentMarkovParam.lean` | **0** | `:20` the hook-content principal-specialisation identity, *"cited against a `sympy` check"* |
| `Eightfold/OcneanuRankFamily.lean` | **0** | `:95` the same identity, *"cited rather than proved"* |
| `QuantumObservableUniverse/SelfDualityDegree.lean` | **0** | `:89-90` Woronowicz's 4D bicovariant classification |
| `QuantumObservableUniverse/VolumeFormDegree.lean` | **0** | `:63,148` `Λ^{N−1}W ⊗ W → Λ^N W ≅ 𝟙` in a rigid monoidal category, *"cited and not [proved]"* |
| `QuantumObservableUniverse/CalculusDimensionObstruction.lean` | **0** | `:89-94` Woronowicz structure equations; `Ω¹(𝒪_q(SU(2)))` free of rank 3 |
| `BringsSurface/CoveringDegreeRamification.lean` | **0** | `:73,91` the Riemann–Hurwitz theorem itself |
| `Eightfold/CircleBundleBettiObstruction.lean` | 2 | `:63` `[hatcher2002]` — **and that key does not exist** (separate bean) |

**Every one of these files is sorry-free.** (Checked: the `sorry` matches in
`HookContentMarkovParam`, `OcneanuRankFamily`, `VolumeFormDegree`,
`CoveringDegreeRamification` and `EmCouplingBringZeroMode` are all the string
*"sorry-free"* in prose, or commented-out instances. A naive `grep -c '\bsorry\b'`
reports 1–4 and is wrong — I made that error before checking.)

**So AGENTS.md §1 ("every `sorry` requires a `-- Ref:`") does not formally bind
here.** That is exactly why this is worth a bean: the discipline is keyed on
`sorry`, and a *sorry-free file that defers a premise in prose* falls through it.
The corpus already has a detector for the sorry case
(`docs/audits/2026-09-03-cited-not-proved-surface.json`, 3529 files scanned, keyed
on `sorries` / `axioms` / `prose_occurrences`) — these files postdate it and would
not be caught by its `sorries` arm anyway.

**What to do, in decreasing value:**

1. **Add `-- Ref:` lines** at the nine sites above. Four of them are blocked on a
   registry gap and have their own beans (Woronowicz calculi; Riemann–Hurwitz;
   CR/contact; `[hatcher2002]`); the rigid-monoidal one and the hook-content one
   are not, and are cheap:
   - `VolumeFormDegree.lean:63` — `[kassel1995]` is registered and already cited
     for `q`-integers and Hecke braiding elsewhere in this directory; check whether
     its Ch. XIV covers the rigidity/duality pairing, else register
     Etingof–Gelaki–Nikshych–Ostrik, *Tensor Categories* (AMS Math. Surveys 205,
     2015), which is **not** in `references.ts`.
   - `HookContentMarkovParam.lean:20` / `OcneanuRankFamily.lean:95` — the
     principal-specialisation identity is Stanley, *Enumerative Combinatorics II*,
     Cor. 7.21.3, or Macdonald *I.3* Ex. 1. **Neither `stanley1999` nor
     `macdonald1995` is registered.** Note `HookContentMarkovParam` now *proves*
     the `n = 2` instance and says so at `:84` — *"nothing here should be cited as
     though it were"* the general identity. Keep that distinction in the Ref.
2. **Consider extending the cited-not-proved detector** to a `prose_occurrences`
   arm keyed on *"cited, not"* / *"cited rather than"* / *"classical input"* /
   *"not proved here"* in sorry-free files, so this class is machine-visible.
   The JSON schema already has a `prose_occurrences` field.

Found by the citation-gap sweep, `docs/audits/2026-09-04-citation-gap-inventory.md`.
