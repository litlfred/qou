# Q_β kernel hunt — Stage C scope (target the q-difference kernel R(q,ξ), not the order recurrence)

> **Bean.** [`qkhc`](../../.beans/qkhc--qbeta-kernel-hunt-stage-c.md) (parent `qz9k`).
> **Discipline.** Formalize-first (narrow before running). This doc is a **scope +
> one structural pruning result**, NOT a probe run — the fibre-Habiro axis is
> owner-gated multi-session research
> ([`refuted-class-map §5`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)).
> No probe branch is opened here.

## 0. Two distinct "stage" lineages — disambiguated first

"Stage X" is overloaded in the Q_β corpus; pin both before reading on:

- **Hoefsmit per-block infra lineage** (operator machinery):
  *Stage A* = per-block χ^λ operator infra at q₀ (validated, commit `3d142447`);
  *Stage B* = per-block **c_3 cross-anchor localization** probe — "is c_3 dominated
  by one Wedderburn block λ⊢3 of H_3, or multi-block?" — infra **unblocked 2026-06-05**
  (`dcd598f1`) but the localization test is **still not executed** (the commit labelled
  "Stage C: per-block χ^λ closed forms" `01802133` computed the closed forms but did
  **not** run the cross-anchor ladder-inversion localization)
  ([`hoefsmit-stage-b scope`](2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md)).
- **Kernel-hunt lineage** (this bean): the search for the open keystone of
  [`refuted-class-map §1`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
  — the fibre-level Habiro element `F(q)` (whose Taylor coefficients **are** the
  ladder `c_k`) and its kernel `R(q,ξ)` in `F(qξ)=R(q,ξ)·F(ξ)`.

**Kernel-hunt Stage C** (defined here) is the stage that, with the real-q (C1–C4),
constant-kernel (C5), Pell-Lucas (C6), SDP (C7), and **mass-side trace (C8, C12)**
classes all refuted, turns to the **fibre-level q-difference kernel `R(q,ξ)`
directly**. The Hoefsmit Stage-B localization probe is a useful *input* (it would
tell us whether the residue is single-block), but it is not on the critical path to
the kernel and is separately scoped.

## 1. The Stage-C target, stated precisely

Construct (or rigorously constrain) the kernel `R(q,ξ)` of the proved, sorry-free
*conditional* recursion
$$
F(q\xi) = R(q,\xi)\,F(\xi) \;\Longrightarrow\; c_{k+1} = \textstyle\sum_j a_j(q_0)\,c_{k+1-j},
$$
where `F(q)` is fibre-level (formal-q / cyclotomic), `R(q,ξ)` is non-constant
q-rational, and `c_2 = −1` is the only canonical (Taylor-exact, anchor-stable) rung
([`ck-dk-canonical-registry §3`](../coordination/ck-dk-canonical-registry.md)). The
recursion **engine** already exists sorry-free
(`QOU/QBeta/RationalCoeffRecurrence.lean`, `pole_reciprocal_is_char_root`); the
**missing object is the kernel `R`**, so the formalization target is `R(q,ξ)`, not
another `c_k` value.

## 2. Formalize-first pruning result (the value-add of this scope)

**Claim.** The `c_k` ladder is governed by the *argument* q-difference recurrence
(q-holonomic), and is provably **not** in the *order*-recurrence (C-finite, constant-b)
class that governs the binding `Δ_λ` ladder. Any Stage-C probe that models `c_k` with
the q-Lommel **order** recurrence `c_{k+1}=b·c_k−c_{k−1}` (constant derived
`b=q₀¹⁰+q₀⁻¹⁰`, the binding-ladder coefficient) is **dead on arrival**.

**Why (grounded in already-proven corpus, three independent ways):**

1. **Two different recurrences, explicitly distinguished in Lean.**
   `QOU/QBeta/QLommelOrderRecurrence.lean` is the **order** three-term recurrence in
   the order index ν (`a(n+2)=b_n·a(n+1)−a(n)`), which the file's own docstring binds
   to the **binding Δ_λ ladder** (`Δ_λ(K) ≈ q₀^{10A−5}`, geometric in **mass number
   A** via `two_root_geometric`). Its docstring states it is *"distinct from the
   argument q-difference recurrence formalised in `QBesselContiguityRecurrence.lean`
   (q-holonomic / k-varying in the power-series index)."* The `c_k` are indexed by the
   **power-series index k**, so they live in the **argument/contiguity** recurrence —
   not the order recurrence.

2. **The c_k argument recurrence is first-order q-holonomic, NOT C-finite.**
   `QOU/QBeta/QBesselContiguityRecurrence.lean` proves the exact relation
   $$
   c_{k+1}\,(1-q^{k+1})(1-a\,q^{k}) = -q^{k}\,c_k, \qquad a=q^{\nu+1}\quad(\star)
   $$
   — first-order with **`q^k`-dependent coefficients**, i.e. q-holonomic. A
   constant-coefficient (C-finite) recurrence is only the **degeneration** at the
   `q→1` / rational limit. The kernel `R` of `F(qξ)=R·F(ξ)` is *"the q-Bessel
   q-difference operator, not a rational degeneration."* The order recurrence's
   constant `b` is precisely that degeneration.

3. **The C-finite class was already searched and refuted.** PR #1839 found **no
   low-order constant-coefficient recurrence** for the canonical `c_2..c_10` (registry
   §3; refuted-class row **C5** closes the constant-kernel axis through depth 4; **C6**
   closes the Pell-Lucas constant-b pattern at the first free rung `c_8`, wrong sign).

**Confirming numeric (secondary, with caveat).** A constant-`b` order recurrence
seeded `c_2=−1, c_3=−2` predicts `c_4 = b·c_3 − c_2 = 3.19113·(−2)−(−1) = −5.382`,
whereas the empirical canonical-anchor value is `c_4 ≈ −0.972`
([`ck-dk-canonical-registry §c_4`](../coordination/ck-dk-canonical-registry.md): CODATA
residual, flagged normalisation artifact). A ~5.5× mismatch. *Caveat:* `c_3=−2` is
itself only a falsified near-match, so this numeric is a consistency check on top of
the structural argument (1)–(3), not the argument itself.

**Consequence for Stage C.** Do **not** model `c_k` as `α·rⁿ+β·sⁿ` with `r=q₀¹⁰`
(that is the binding ladder). Model `F(q)` against the q-holonomic `(★)` / the
`RationalCoeffRecurrence` pole structure: the kernel `R(q,ξ)` is the q-Bessel
q-difference operator, and the open work is its **categorical** identification (which
Hahn–Exton `J_ν`, which order ν, which root-of-unity residue), not a constant-b fit.

## 3. Invariants any F(q) candidate must satisfy (unchanged, restated)

Per [`refuted-class-map §4`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md):
(a) **anchor-stability** — proton+muon swing `< 1%` (registry §8); (b) **bar-evenness**
`q↦q⁻¹` (c_2=−1 is bar-even, Kashiwara `f̃₁²`); (c) **q=1 classical shadow** reproduces
the known integer (`c_3→J_Hopf(1)=−2`) without fitting; (d) **direction sanity** —
magnitude of any scaling respects the target (the #1850 `z<1` lesson). A candidate that
fails (a)–(d) **symbolically** is killed on paper — add a refuted-class row, do not run
the anchor sweep.

## 4. Closed classes — do NOT re-run (cite the row)

`C1–C4` (real-q single / 2-factor / torus-knot / cinquefoil), `C5` (constant kernel),
`C6` (Pell-Lucas into free rungs), `C7` (SDP extraction), `C8` (algebra-tower
box-adding), `C9` (per-knot Vol flip, production), `C10–C11` (KR / volume-conjecture
imports), `C12` (trace-level Markov-stabilization). The mass-side `linking_weight≈2.53`
is **CODATA-implied near-match** territory, not an open keystone. The **one** open axis
is the decay-side fibre kernel `R(q,ξ)` of §1–§2.

## 5. Next concrete step (when an owner authorizes a probe branch)

1. **Coordinate first** (refuted-class-map §5): the fibre-Habiro axis overlaps the Hecke
   `tr_M` / fibre machinery of merged siblings #1808/#1816/#1841/#1850/#1811; post intent
   on any active Q_β sibling before opening a probe branch.
2. **Hoefsmit Stage-B localization** (separate, infra now unblocked) would tell us if the
   residue is single-block — a useful narrowing input, runnable without `pyhecke_native`
   via a convention-faithful in-script Hoefsmit n=3.
3. **Kernel identification**: against `(★)`, fix the Hahn–Exton order `ν` and the
   root-of-unity residue that make `R(q,ξ)`'s `q=1` shadow reproduce `c_2=−1` (proved)
   and the `c_3` near-match integer — a **symbolic** q-difference argument, formalized as
   a `class` + `-- Ref:` per §3b-cond, before any numeric anchor sweep.

## 6. Cross-references

- [`refuted-class-map`](../audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md) — C1–C12 + the open axis + formalize-first gate
- [`ck-dk-canonical-registry`](../coordination/ck-dk-canonical-registry.md) — per-rung canonical/empirical tiers
- [`1ppq-qbeta`](../coordination/1ppq-qbeta.md) — Q_β master ledger / flip-flop history
- Lean: `QOU/QBeta/QBesselContiguityRecurrence.lean` (★, c_k q-holonomic), `RationalCoeffRecurrence.lean` (kernel pole structure), `QLommelOrderRecurrence.lean` (binding Δ_λ ladder — the WRONG class for c_k)
- [`hoefsmit-stage-b scope`](2026-06-04-hoefsmit-stage-b-per-block-tbeta-scope.md) — the per-block localization probe (separate lineage)
