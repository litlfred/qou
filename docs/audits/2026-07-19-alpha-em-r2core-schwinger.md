# α_EM R2-core — the Schwinger normalization in fuller context (2026-07-19)

**Context:** owner: *"give fuller context — derive (or rule on) the
framework's proper-time measure normalization; take into account the
information-theory corpus and E = mc_q²"* — under the standing ruling
([`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)):
R2 is not derived-proved. Respected throughout: nothing here proves the
convention; everything provable around it is now Lean-proved.

**Lean (this PR):** [`QOU/Archimedean/SchwingerMeasureShape.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/SchwingerMeasureShape.lean)
— sorry-free, `lean`-direct exit 0.
**Probe:** [`alpha_em_r2core_schwinger_probe.py`](../../computations/alpha_em/alpha_em_r2core_schwinger_probe.py)
(+ witness, 4/4).

## Corpus inputs (information-theory chapter, all existing blocks)

| Block | Input |
|---|---|
| [`mass-energy-equivalence`](../../content/quantum-observable-universe/information-theory/mass-energy-equivalence.md) | `E = m·c_q²`, `c_q = 1/(q−1)` — the energy↔mass bridge |
| [`boltzmann-constant`](../../content/quantum-observable-universe/information-theory/boltzmann-constant.md) | `k_B = 1`; `ℏ_q = (q−1)/q` replaces `k_B·T` — **entropy in nats** |
| [`fibre-channel-capacity`](../../content/quantum-observable-universe/information-theory/fibre-channel-capacity.md) | per-crossing entropy `η_q = (2q−1)/q³` (≈ 0.892 at q₀); capacities additive |
| [`horizon-conformal-invariance`](../../content/quantum-observable-universe/information-theory/horizon-conformal-invariance.md) | boundary datum invariant under rescaling — **no preferred scale** |
| [`discrete-planck-step`](../../content/quantum-observable-universe/information-theory/discrete-planck-step.md) | **"one full Reeb circuit = one unit of time"** — a canonized unit convention resolving a transcendental factor |

## What is now proved (sorry-free Lean)

1. **Shape rigidity** — a scale-invariant proper-time density is `c/s`,
   uniquely up to the scalar c (`scale_invariant_density_unique`). Scale
   invariance is corpus-motivated (horizon rescaling invariance: the
   loop's UV end has no preferred proper-time scale).
2. **The nat reading** — one e-fold carries measure exactly c
   (`one_nat_per_efold`, log form): with `k_B = 1`, **c is the nat-count
   per proper-time e-fold**.
3. **The E-Jacobian** — via `E = m·c_q²`, `s ~ E⁻²`: one energy e-fold =
   two proper-time e-folds (`efold_jacobian_two`).
4. **The assembly** — `c = 1` total with the ½ split gives `1/(8π)`
   (`unit_total_gives_eighth`).

## R2-core, corpus-natively

> **"The loop expansion assigns one nat per proper-time e-fold
> (k_B = 1)."**

This is a unit convention of *exactly the species the corpus has already
canonized once*: `discrete-planck-step` resolves the transcendental 2π by
declaring one Reeb circuit = one time unit. R2-core is the analogous
declaration for the loop measure. Per the ruling it remains a convention —
unproven — but it is now stated in the framework's own
information-theoretic language, with its entire provable shell Lean-locked.

## The new adjudication (flagged OPEN — a fourth reading of the "2")

The `E = mc_q²` bridge creates a **rival** derivation of the ½: if the unit
convention counts *energy* e-folds, the s ~ E⁻² Jacobian supplies ½ with no
ρ-split needed. Exact table: ρ-split alone → 1/(8π) ✓; E-Jacobian alone →
1/(8π) ✓; **both → 1/(16π) ✗** (excluded by the working coefficient). The
two readings are mutually exclusive and observationally indistinguishable
at this order — the adjudication (which e-fold variable the convention
counts) is **open and owner-level**, joining the readings-of-2 saga.

## Residue after this tranche

```
R2-core = ONE unit convention  ("one nat per proper-time e-fold, k_B = 1")
        + ONE adjudication      (proper-time vs energy e-folds — the ½'s home)
Both corpus-native, both open, both owner-gated. Nothing wired; 1/(8π) phase-4.
```
