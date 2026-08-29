# `prop:ground-state-ordering` — per-clause truth value

**Bean** `qou-48is`. **PR** [#4855](https://github.com/litlfred/qou/pull/4855).
Block: [`mass-theory/ground-state-ordering.md`](../../content/quantum-observable-universe/mass-theory/ground-state-ordering.md).
Lean: `QOU.ParticleInteractions.ground_state_ordering` (the stated `Prop`),
`QOU.MassTheory.GroundStateOrderingRefutation` (this audit's sorry-free result).

---

## Verdict, per clause

| Clause | Verdict | Evidence |
|---|---|---|
| **(i)+(ii)** interleaving + tail packing for `A ≥ 4` | **FALSE** | counterexample at `A = 5`, `Z = 1`; Lean-proved for a whole `q`-interval containing the anchor |
| **(iii)** sorted wins for `A ≤ 3` | **TRUE at `A = 3`** (both readouts, exhaustive), **FALSE as stated at `A = 2`** | `A = 2` is an exact tie under `Φ_nuc` and a strict *loss* for sorted under `Φ₁` |

Neither clause is what the block asserts. The block has been corrected.

---

## 1. Method

`Φ_q = Σ_i log|V̂_i|` was evaluated **exhaustively** over all `C(A, Z)`
arrangements for every `(Z, N)` with `Z ≤ N` and `A ≤ 16` — 128 sweeps,
55 588 arrangement evaluations, 131 s wall — at the **experimental (proton)**
`q₀ = 1.109978582751380807591669` (`q_parameter.q_at`, 50 dps).

Probe: [`computations/probes/ground_state_ordering_argmin_sweep.py`](../../computations/probes/ground_state_ordering_argmin_sweep.py).
Witness: [`computations/ground-state-ordering-argmin-sweep.witness.json`](../../computations/ground-state-ordering-argmin-sweep.witness.json).

Both readouts were swept separately, because they are **different objects**:

- **`Φ_nuc`** — the bare nucleon chain.
- **`Φ₁`** — the nucleon chain with the `["e"] * Z` electron tail appended,
  which is what `hecke_core_symbolic.compute_phi1_full_sym` actually calls.

### 1.1 The fast readout, and why it is exact

`_phi1_from_ordering_sym` is sympy-symbolic and unaffordable over 55 588
arrangements. The probe therefore uses a closed form derived from the corpus
implementation itself. The corpus transfer factor is

```
T(d) = [[h + d, 1], [1, d]] = S + d·1,     S = [[h, 1], [1, 0]],  h = q − q⁻¹,
```

so every `T(d)` is a polynomial in the single matrix `S`; they all commute
(`QOU.MassTheory.TransferFactorCommute`), and `M_i = Π_{j>i} T(d_ij)` depends
on the crossing coefficients **only as a multiset**. `S` has `tr S = h`,
`det S = −1`, hence eigenvalues `λ₊ = q`, `λ₋ = −q⁻¹`, and `S² = hS + 1`
collapses `M_i` to `α·1 + β·S`. Since `M[1][0] = β` and `M[1][1] = α`, the
corpus readout `V̂_i = z·M[1][0] + M[1][1]` becomes

```
V̂_i = c₊·μ₊ + c₋·μ₋ ,     μ± = Π_{j>i} (λ± + d_ij),
c₊ = (z + q⁻¹)/(q + q⁻¹),  c₋ = (q − z)/(q + q⁻¹),  z = √q/(q+1),
```

with `c₊ + c₋ = 1`. The per-`d` eigenfactors are

| crossing | `d` | `μ₊ ·=` | `μ₋ ·=` |
|---|---|---|---|
| `pp`, `ee` | `0` | `q` | `−q⁻¹` |
| `pn`, `np` | `−h/2` | `c = (q+q⁻¹)/2` | `−c` |
| `nn`, `pe`, `ep` | `−h` | `q⁻¹` | `−q` |
| `ne`, `en` | *(absent)* | *(skipped)* | *(skipped)* |

The `(n, e)` case has **no branch** in `_crossing_coeff_sym`; it returns
`None` and the corpus silently skips the factor. The probe reproduces that
skip verbatim rather than repairing it — the probe measures what production
computes, not what it arguably should.

**Cross-check.** The closed form agrees with `_phi1_from_ordering_sym` to a
worst relative difference of **1.7 × 10⁻⁵⁵** on 11 orderings, including
orderings that exercise the `(n, e)` skip.

---

## 2. The `A ≥ 4` clause is FALSE

### 2.1 Tally

Over the 62 `(Z, N)` cases with `4 ≤ A ≤ 16`, `Z ≤ N`:

| arrangement | argmin under `Φ_nuc` | argmax under `Φ_nuc` | argmin under `Φ₁` | argmax under `Φ₁` |
|---|---|---|---|---|
| prescribed (rules i+ii) | **17 / 62** | 12 / 62 | **10 / 62** | 8 / 62 |
| sorted | 1 / 62 | 2 / 62 | 1 / 62 | 2 / 62 |
| `_ground_state_ordering` (production) | 9 / 62 | 13 / 62 | 7 / 62 | 7 / 62 |

The prescribed arrangement is the minimiser in a minority of cases and is the
strict **maximiser** almost as often. It is not the ground state.

### 2.2 The counterexample

The sharpest case is `A = 5`, `Z = 1`, `N = 4`, where the two readouts agree
and the prescribed arrangement is the strict worst of all five:

| arrangement | `Φ_nuc` | rank | `Φ₁` | rank |
|---|---|---|---|---|
| `p n n n n` (**sorted**) | **−3.643520** | 1 / 5 | **−4.880498** | 1 / 5 |
| `n p n n n` (**prescribed**) | −2.291217 | **5 / 5** | −1.392626 | **5 / 5** |

The proposition reserves *sorted* for `A ≤ 3` and prescribes *interleaved* for
`A ≥ 4`. At `A = 5` the assignment is exactly inverted, by **1.352 nats**.

Other clean cases: `A = 5, Z = 2` (prescribed `npnpn` is rank 10/10 under
`Φ_nuc`); `A = 7, Z = 3` (rank 35/35 under both readouts); `A = 4, Z = 2`
— **⁴He** — where under `Φ₁` the prescribed `npnp` is rank 6/6 while the
argmin is `pnpn`.

### 2.3 Tail packing (rule (ii)) is refuted independently

Rule (ii) puts the excess neutrons at the **highest** positions. The exhaustive
argmin does the opposite. At `Z = 1` the minimising proton position under
`Φ_nuc` is, for every `6 ≤ N ≤ 15`, exactly `A − 5` — i.e. the excess neutrons
**head-pack**, leaving exactly four neutrons in the tail:

```
Z=1, N=15, A=16   argmin = n n n n n n n n n n n p n n n n
```

For `Z ≥ 2` the argmin is an interleaved `p n p n …` block placed at an
interior offset with neutron runs on **both** sides. No member of the sweep's
argmin family is tail-packed in the sense of rule (ii).

### 2.4 Lean

[`QOU/MassTheory/GroundStateOrderingRefutation.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/GroundStateOrderingRefutation.lean)
— sorry-free, registered in the `QOU` umbrella, `#print axioms` clean
(`propext`, `Classical.choice`, `Quot.sound` only) on all 13 declarations.

Writing `q = t²`, the two arrangements differ at positions `0, 1` only
(positions `2, 3` see the same all-neutron suffix, so their readouts are
literally the same expression). Clearing `z = √q/(q+1)` reduces the
comparison to a single polynomial inequality in `t`, with

```
Ã = t³ + t² + 1  (= c₊·K),   B̃ = t⁶ + t⁴ − t³  (= c₋·K),   K = (t²+1)(t⁴+1).
```

`A5_certificate` proves, for **every** `t > 1`:

```
(Ã − B̃t¹²)(t⁴+1)(t²+1)  <  (Ã + B̃t¹²)(Ã − B̃)
```

by the explicit factorisation

```
RHS − LHS = (t−1)·(72 + 1020(t−1) + 6984(t−1)² + … + 2(t−1)²⁰)
```

whose degree-20 cofactor has **all coefficients positive**. The counterexample
therefore survives on a whole interval above `q = 1` — it degenerates to
equality exactly at `q = 1`, where the deformation switches off. Numerically
the inequality holds for `1 < q ≲ 1.22`; the anchor `q₀ ≈ 1.10998` sits well
inside, and the sign hypothesis `hU : 0 ≤ Ã − B̃t¹²` evaluates to `+0.6047`
there.

`sorted_lt_prescribed_A5_full` then gives the four-position statement

```
|V̂₀V̂₁V̂₂V̂₃| (sorted)  <  |V̂₀V̂₁V̂₂V̂₃| (prescribed),
```

which is `Φ_q(pnnnn) < Φ_q(npnnn)`, and `prescribed_not_minimiser_A5` states
the refutation. The Lean definitions reproduce the probe's `Φ` values to
**1.2 × 10⁻⁶⁰** (`lean_bridge` block of the witness).

`transferEigen_isRoot` / `transferEigen_vieta` record the **one** conjunct of
the original `ground_state_ordering` `Prop` that survives: `λ₊·λ₋ = −1`.

### 2.5 The refutation is convention-independent (added 2026-08-24)

Everything in §2.4 was derived with the Markov parameter `z = √q/(q+1)`
(**convention C**), which the owner ruling of 2026-08-15 excises in favour of
`z = q³/(q²+1)` (**convention D**). The refutation survives, and not by
re-derivation: *the argument never reads `z`'s formula.*

`z` enters the readout only through the two weights, and their sum is `1`
identically in `z`. The whole `A = 5` comparison then collapses to

```
V̂₀V̂₁(npnnn) − V̂₀V̂₁(pnnnn) = 2·c₊c₋·c⁴·(q⁶ − 1)/q³,
4·c₊c₋ = 4q(q − z)(qz + 1)/(q² + 1)².
```

So for `q > 1` the counterexample holds **exactly when `−q⁻¹ < z < q`** — the
Markov parameter strictly between the two eigenvalues `λ₋ = −q⁻¹`, `λ₊ = q`.
Both conventions are in that window for every `q > 1`. At the anchor the
weights are `(c₊, c₋) = (0.69633, 0.30367)` under C and `(0.75270, 0.24730)`
under D.

The Lean was generalised accordingly (`prescribed_not_minimiser_A5` now
quantifies over `(q, z)`), with `prescribed_not_minimiser_A5_conventionD` and
`..._conventionC` as specialisations. §2.4's polynomial certificate is retained
as the convention-C cross-check. Declaration count is 13 → 30; `#print axioms`
is `propext`, `Classical.choice`, `Quot.sound` on every one. Probe:
[`ground_state_ordering_convention_independence_probe.py`](../../computations/probes/ground_state_ordering_convention_independence_probe.py),
8/8 exact.

**Two windows, and §2.4's "1 < q ≲ 1.22" is the right one — do not "correct" it
to 1.137.** `hU` is *sufficient, not necessary*: it is only what turns the gap
identity into an inequality between **absolute** values, and the conclusion
outlives it. Measured:

| convention | `hU` holds | conclusion `\|sorted\| < \|prescribed\|` holds |
|---|---|---|
| C (`√q/(q+1)`) | `1 < q < 1.13700` | `1 < q < 1.22092` |
| D (`q³/(q²+1)`) | `1 < q < 1.21061` | `1 < q < 1.57015` |

The anchor `q₀ ≈ 1.10998` is inside all four. The canonical convention D
therefore *widens* the interval on which the refutation is Lean-proved, and
`sortedV1_zD_nonneg` discharges `hU` outright on `1 < q ≤ 6/5` — so the
convention-D statement carries no hypothesis but the `q`-range.

---

## 3. The `A ≤ 3` clause

| case | `Φ_nuc` | `Φ₁` |
|---|---|---|
| `A = 3`, `Z = 1` (triton) | sorted `pnn` **argmin** (1/3) | sorted `pnn` **argmin** (1/3) |
| `A = 3`, `Z = 2` (³He, outside the stated `Z ≤ N`) | sorted `ppn` **argmin**, tied with `pnp` | sorted `ppn` **argmin** (1/3) |
| `A = 2`, `Z = 1` (deuteron) | `pn` = `np` **exact tie** | sorted `pn` is the **argmax** |

So the clause is:

- **true at `A = 3`**, on both readouts, and on both sides of `Z ≤ N`;
- **not true as stated at `A = 2`**. The prose says sorted *beats*
  interleaving; under `Φ_nuc` it is an exact tie (an instance of the
  multiset degeneracy — one crossing either way), and under `Φ₁` sorted is
  strictly worse (`−0.031` vs `−2.166`).

**Caveat, stated plainly.** `compute_phi1_full_sym` special-cases `A == 2`
with the trefoil formula and never routes the ordering through
`_phi1_from_ordering_sym`, so the `A = 2` `Φ₁` failure is a defect **of the
proposition as written**, not of a live production path.

**The `³He` degeneracy.** `ppn` and `pnp` are *exactly* equal under `Φ_nuc` —
the multiset consequence of the commuting transfer factors. Under `Φ₁` they
separate, but that separation is produced entirely by `_crossing_coeff_sym`
having no `(n, e)` branch. Whether the `(n, e)` skip is intended is a separate
open question and is **not** settled here.

---

## 4. Scope classification

- **`A ≥ 4` clause — scope-(b) structural exclusion.** Not "the numbers came
  out wrong": an explicit arrangement with strictly smaller `Φ_q`, proved in
  Lean for an interval of `q` containing the anchor. The invariant cited is
  the polynomial certificate `A5_certificate`, whose positivity is exact.
- **`A ≤ 3` clause at `A = 2` — scope-(b) for the strict reading**
  (`Φ_nuc` gives an exact equality, so "beats" is provably false), and a
  scope-(b) failure under `Φ₁` (explicit strict inversion).
- **`A ≤ 3` clause at `A = 3` — verified, not proved.** Exhaustive over all
  three arrangements at the anchor; no Lean proof. It is *true at `A = 3`*,
  not *proved for all `q`*.
- **The argmin family (§2.3) is scope-(a)**: a description of what the sweep
  found for `A ≤ 16`, not a proved characterisation. No claim is made beyond
  `A = 16`.

---

## 5. What this does **not** decide

Deliberately out of scope, and unchanged by this PR:

- **No production behaviour changed.** `closed_form_tau_M` is untouched, the
  production ordering is unswitched, the `A ≥ 3` binding table is not
  regenerated, `_ground_state_ordering` and the `a > 4` guard are not fixed.
  **No published number moves.**
- **Which ordering production *should* use** is the owner's call. This audit
  supplies only the precondition that was missing: the corpus's stated
  selection rule is not a `Φ_q` minimality rule, so reconciling the four
  ordering artefacts to it would relabel the arbitrariness rather than remove
  it.
- **Whether `Φ_q`-minimality is the right selection principle at all.** The
  sweep shows the corpus's own `Φ_q` argmin is not a simple closed family
  (interior interleaved blocks, head-packed excess neutrons); that is a
  different question from whether the ground state should minimise `Φ_q`.
- **The `(n, e)` missing branch** in `_crossing_coeff_sym`.
