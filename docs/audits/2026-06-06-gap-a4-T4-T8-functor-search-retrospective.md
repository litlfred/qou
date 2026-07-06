# GAP-A-4 functor-search retrospective: T4–T8 — 5 candidates REFUTED, icosahedral H is non-Schur-Weyl

**Date:** 2026-06-06
**Branch:** `claude/gap-a4-T4-schur-weyl-icosahedral-probe-2026-06-05` (PR #1904)
**Scope:** Five-probe sweep of natural cross-algebra functor candidates
linking the 5-strand A_5 fiber action (on H_5(q) Wedderburn blocks (3,2)
and (2,2,1)) to the 3-strand H_3(q) Borromean Markov trace's h⁴ = −3/4
coefficient. The chain extends the [2026-06-05 final retrospective](2026-06-05-gap-a4-final-retrospective.md)
(`docs/audits/2026-06-05-gap-a4-final-retrospective.md`) and operationalises
the [2026-06-01 audit](2026-06-01-s5-so3-su2-u1-fiber-action.md)'s
identified "missing categorical functor" as a search-space prune.

---

## VERDICT (one line)

**The icosahedral H is fundamentally a non-Schur-Weyl object.** All
standard quantum-group / representation-theoretic routes from the
5-strand A_5 fiber action to the 3-strand H_3 Borromean h⁴ = −3/4 are
now ruled out by formal refutation (T5×3, T7, T8). The missing
categorical functor must live OUTSIDE the q-Schur / Reshetikhin-Turaev
picture — likely involving the icosahedral subgroup structure of
SO(3) ⊂ PSL(2, ℂ) directly (Möbius / Bring / McKay E_8). T6 also
exhibits the H-sector's own internal h⁴ = +2 ≠ −3/4, reinforcing
that the cross-algebra link is the fundamental obstruction.

---

## The five candidate functors

The 2026-06-01 audit identified the open object as: a canonical functor
from `SO(3)/I level ℓ on the 5-strand color×nucleon space` to a
Wedderburn coefficient of the 3-strand Borromean H_3(q) Markov trace.
T4 confirmed claim (2) (the 5-strand structural matching at q=1); T5–T8
enumerate the natural functor candidates and refute each.

| # | Probe | Candidate | Verdict | Quantitative result |
|---|---|---|---|---|
| **F1** | T5 | Young's branching Res^{S_5}_{S_3} | REFUTED | m_{(2,1)} = 4; no natural normalisation → −3/4 |
| **F2** | T5 | dim_q ratio 2·[5]_q / [3]_q | REFUTED | h⁴ = −2/27 (off by 8/81 vs −3/4) |
| **F3** | T5 | Wenzl-weight ratio at q=1 | REFUTED | (5/12)/(2/3) = 5/8 (wrong sign and magnitude) |
| **F4** | T7 | Bratteli/Markov stabilization H_3 ↪ H_5 | REFUTED | Uniform 5/4 multiplier; would yield −15/16 not −3/4 |
| **F5** | T8 | RT / q-Schur duality (sl_m, m=2 and m=3) | REFUTED | V_2 absent at sl_2; H splits into two distinct sl_3 irreps |

## What each candidate ruled out

### F1 — Young's branching (T5)

Two-step `Res^{S_5}_{S_4} ∘ Res^{S_4}_{S_3}` applied to the icosahedral H
sector yields:

```
Res^{S_5}_{S_3} V_{(3,2)}   = V_{(3)} ⊕ 2·V_{(2,1)}
Res^{S_5}_{S_3} V_{(2,2,1)} =        2·V_{(2,1)} ⊕ V_{(1^3)}
```

The combined (2,1) multiplicity is 4. The naive transfer
4 · (−3/4) = −3 has no natural normalisation that lands on −3/4.
Several rescalings tried (dim_q-modulated, m/4, dim_q-ratio-weighted)
all miss.

### F2 — Algebraic h⁴ from dim_q ratio (T5)

Closed-form via algebraic identity `[5]_q = h⁴+5h²+5` and `[3]_q = h²+3`:

```
2·[5]_q / [3]_q  =  10/3 + (20/9)h² − (2/27)h⁴ + O(h⁶)
```

h⁴ coefficient −2/27. Ratio (−2/27)/(−3/4) = 8/81, no clean
structural interpretation.

### F3 — Wenzl-weight ratio (T5)

At q=1 (Plancherel measure):
`(y_{(3,2)} + y_{(2,2,1)}) / y_{(2,1)} = (5/12)/(2/3) = 5/8`.

Wrong sign AND magnitude vs −3/4.

### F4 — Bratteli/Markov stabilization (T7)

For β_Bor with image id ∈ S_3 and writhe 0,
`χ^{(3,2)}(F(β_Bor)) = χ^{(2,2,1)}(F(β_Bor)) = 1 + 2·χ^{(2,1)}(β_Bor)`.

The H-sector contribution factorises as
`(y_{(3,2)} + y_{(2,2,1)})·(1 + 2·χ^{(2,1)}(β_Bor))`.

Compared to the full Borromean H_3 trace:

| Component | H_5 H-sector | Borromean H_3 | Ratio |
|---|---|---|---|
| χ^{(2,1)} multiplier | 2·5/12 = 5/6 | 2/3 | **5/4** |
| Writhe-0 constant | 5/12 | 1/3 | **5/4** |

Uniform 5/4 ratio means H-sector h⁴ = (5/4)·(−3/4) = −15/16. Recovering
−3/4 cleanly requires ad-hoc rescaling by 4/5 with no framework derivation.
The 5/4 factor is the Plancherel-weighted version of T5 F1's m=4.

### F5 — RT / q-Schur duality (T8)

The Reshetikhin-Turaev framework via q-Schur duality between
H_n(q) and U_q(sl_m) on (ℂ_q^m)^⊗n is ruled out at TWO ranks:

**sl_2 (m=2):** Only 2-row partitions of 5 contribute. Their spin
labels: (5)↔j=5/2 (dim 6), (4,1)↔j=3/2 (dim 4), (3,2)↔j=1/2 (dim 2).
The dim-5 sl_2 rep V_2 (j=2) is **ABSENT** from (ℂ_q^2)^⊗5.
Classical Clebsch-Gordan check: V_{1/2}^⊗5 = V_{5/2} ⊕ 4·V_{3/2} ⊕
5·V_{1/2}, dim 32 = 2^5 ✓. V_2 multiplicity = 0.

**sl_3 (m=3):** Both (3,2) and (2,2,1) appear, but as TWO different
sl_3 irreps with highest weights (1,2) and (0,1). dim_q(S^λ) = [5]_q for
both, but they are NOT isomorphic as sl_3 reps. The icosahedral
H = V_{(3,2)} ⊕ V_{(2,2,1)} is a sum of two distinct sl_3
isotypic components — NOT a single 'spin j=2 / dim 5' RT-invariant.

Sanity assertion: sl_2 q-Schur centralizer identity
`[2]_q^5 = 1·[6]_q + 4·[4]_q + 5·[2]_q` verified to 50 dps at q_0.

---

## What T6 added (q-deformed character matrix's own h⁴)

T6 tabulated the q-deformed per-A_n-irrep weights
`Q_R(q) = Σ_λ dim_q(V_λ)·mult_R(λ)` and found two things:

1. **Clifford-excess identity** (new derivation, verified 50 dps):
   ```
   Σ_R Q_R(q) − Σ_λ dim_q(V_λ) = Σ_{λ=λ^T} dim_q(λ)
   ```
   The row-sum overshoot equals dim_q of the self-conjugate partition,
   which Clifford-splits into 2 conjugate A_n irreps under
   Res^{S_n}_{A_n}. At A_4: dim_q((2,2)); at A_5: dim_q((3,1,1)).

2. **H-sector closed form:**
   ```
   Q_H(q) = dim_q((3,2)) + dim_q((2,2,1)) = 2·[5]_q = 10 + 10h² + 2h⁴
   ```
   The icosahedral H-sector's own h⁴ coefficient is **+2** — different
   in sign AND magnitude from the Borromean H_3 reference h⁴ = −3/4.
   Ratio +2/(−3/4) = −8/3, no clean structural interpretation.

This reinforces F1–F5: even at the H-sector's OWN structural level,
its h⁴ is +2, not −3/4. The two h⁴ coefficients live in different
group algebras and don't link via any natural map.

---

## Why the negative is the right shape

This is the **formalize-first discipline** in action:

- **Empirical-fit rule.** Sourcing a normalisation by inspection
  (e.g. "the 5/4 in F4 looks close enough; let's call it 4/5 × something")
  is exactly the empirical-fit the three-calibration discipline
  forbids. The probes are designed to REFUTE rather than fit, so
  every "fail" is a derivation route closed.

- **No 6th ansatz.** Per AGENTS.md's Δ_λ-gate rule and "do not
  propose a 7th fit-based ansatz" guidance, the next move is NOT
  to invent a 6th candidate functor that gives −3/4 by tuning.
  The right move is to characterise the OPEN OBJECT structurally
  via the negative space — which is what F1–F5 collectively do.

- **Search-space prune.** F1–F5 cover essentially every standard
  representation-theoretic / quantum-algebra route. Their joint
  refutation tells us the missing functor is non-standard, which
  is more useful than yet another partial fit.

---

## The next direction (T9 follow-up)

T8's structural finding — the icosahedral H is non-Schur-Weyl —
points the search toward **the icosahedral subgroup structure of
SO(3) ⊂ PSL(2, ℂ) directly**:

| Candidate | Tractability | Source |
|---|---|---|
| **Möbius / Bring quintic** | Klein invariants F, H, T on ℂP¹ with A_5 action; Bring quintic surface's discriminant | classical, computable |
| **McKay correspondence E_8** | Binary icosahedral 2I ↔ Affine Ê_8; 240-root system | rich algebraic structure |
| **Klein invariants** | F (degree 12), H (degree 20), T (degree 30); syzygy F^5 + ... | computable closed forms |

These do NOT use a quantum group rep tower; they use the
finite-group / classical-algebraic side of the icosahedral
structure. None are ruled out by F1–F5. T9 (planned follow-up)
probes the Klein-invariant h-expansion.

---

## Cross-references

- Source conjecture: `conj:s5-so3-fiber-action`,
  [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean).
- The 2026-06-01 audit (original missing-functor identification):
  [`2026-06-01-s5-so3-su2-u1-fiber-action.md`](2026-06-01-s5-so3-su2-u1-fiber-action.md).
- The 2026-06-05 final retrospective (predecessor):
  [`2026-06-05-gap-a4-final-retrospective.md`](2026-06-05-gap-a4-final-retrospective.md).
- Borromean H_3 trace closed form (h⁴ = −3/4 source):
  [`borromean-markov-trace-closed-form.md`](../../content/quantum-observable-universe/mass-theory/borromean-markov-trace-closed-form.md).
- The SAME missing object on K_1 (inter-nucleon-color-tube):
  [`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md).
- Probes (PR #1904, this branch):
  - T4 [Schur-Weyl character bridge](../../computations/probes/gap_a4_T4_schur_weyl_icosahedral_probe.py)
  - T5 [candidate functor F1/F2/F3](../../computations/probes/gap_a4_T5_candidate_functor_probe.py)
  - T6 [q-deformed icosahedral matrix](../../computations/probes/gap_a4_T6_q_deformed_icosahedral_probe.py)
  - T7 [Bratteli/Markov stabilization](../../computations/probes/gap_a4_T7_bratteli_stabilization_probe.py)
  - T8 [RT / q-Schur duality](../../computations/probes/gap_a4_T8_rt_q_schur_probe.py)
