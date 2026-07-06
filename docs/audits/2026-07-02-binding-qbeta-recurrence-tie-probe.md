# Holomorphic-tie probe: do (binding, Q_β) satisfy one 3-term recurrence? (2026-07-02)

**Bean**: `1jrh` · **Branch**: `claude/agent-prepare-merge-dashboard-mxvyc2`
**Probe**: [`probe_binding_qbeta_recurrence_tie.py`](../../computations/probe_binding_qbeta_recurrence_tie.py)
(`binding-qbeta-recurrence-tie-probe.witness.json`, audit-only)
**Formalized structure it tests**: `QOU.Knot.SelfDuality.recurrence_descent`
(sorry-free) — a three-term recurrence `V₊ = c·Vₖ − V₋` with a σ-fixed
(bar-even) multiplier descends to BOTH parity ladders with the SAME `c`.
The probe asks whether the empirical trace ladders actually satisfy such a
recurrence (the hypothesis `h`), over neutron-number chains
`Z ∈ {1, 2}, N = 1..4`, in two forms: linear defect
`D = tr_free − tr_atom` and log form `L = ln(tr_free/tr_atom)`, each at
`q₀` and `q₀⁻¹` (50 dps).

## Results

| test | Z=1, D | Z=1, L | Z=2, D | Z=2, L |
|---|---:|---:|---:|---:|
| (1) constancy of `c(q₀)` (rel spread) | 5.1e-2 | **1.8e-17** | 2.3e-2 | **2.8e-17** |
| (2) bar-evenness `c(q₀) = c(q₀⁻¹)` (rel gap) | 1.23 ✗ | **1.9e-29** | 1.61 ✗ | **3.8e-17** |
| (3) parity tie `c^even = c^odd` (rel gap) | 4.2e-3 (artifact) | **1.7e-29** | 4.6e-4 (artifact) | **5.8e-17** |

## Findings

1. **Log form: the recurrence holds EXACTLY — but degenerately (`c = 2`).**
   `L_N` is exactly *arithmetic* in `N` (all three tests pass at
   ≤ 1e-15 relative, float-limited on the `q₀` leg), i.e. the free/atom
   trace ratio is exactly **geometric per added neutron** with a
   **Z-independent** factor:
   `ℓ(q₀) = 1.2369781644668708…` (`e^ℓ ≈ 3.44519` per neutron),
   `ℓ(q₀⁻¹) = 0.34477368001157065…` — identical on the Z=1 and Z=2 chains
   to all stable digits. `c = 2` is the degenerate boundary of the
   Chebyshev family `c = q^s + q^{-s}` (`s = 0`): the ladder satisfies
   `recurrence_descent`'s hypothesis, and both parities are tied — but any
   exactly-linear sequence does this, so the N-chain ladder carries **no
   non-trivial Askey–Wilson structure**. The non-trivial content is the
   exact per-neutron multiplicativity itself (consistent with the proved
   `FollowsRogersSzego` q-power structure and the prior probe's ≈ 6.68
   bar-ratio increment): a candidate **structural lemma** of the
   transfer-matrix word-builder — likely Lean-provable from the tensor
   extension of the atom word, queued as follow-up.

2. **Per-neutron parity quanta.** The bar-even / bar-odd parts of the
   increment are `E₀·ℓ_even ≈ 3.3106 MeV` and `E₀·ℓ_odd ≈ 1.8674 MeV`
   per neutron. The latter **exactly reproduces** the neutron-organized
   `B_odd` step found by the prior parity probe
   ([`2026-06-30-complex-volume-bar-parity-binding-probe.md`](2026-06-30-complex-volume-bar-parity-binding-probe.md):
   2.757 − 0.889 = 1.868 MeV) — the bar-odd (decay-face) channel is a
   clean per-neutron quantum, as the complex-volume framing predicts
   qualitatively.

3. **Linear-defect form: scope-limited negative.** `D_N` satisfies no
   constant σ-fixed recurrence — the implied multiplier drifts
   (1.75 → 1.97) and is strongly parity-violating
   (`c(q₀⁻¹) ≈ 3.9–5.1 ≠ c(q₀) ≈ 1.8–2.0`). The apparent even/odd tie
   (4e-3) is an **artifact**: `|D(q₀⁻¹)| ≤ 0.9% · |D(q₀)|`, so both
   parities are dominated by the same `D(q₀)/2` term. This refutes the
   tie **in the linear-defect N-chain form only** — it does not exclude
   the tie in the `u = b·ℏ_q²` c_k-rung form (the `c₂ = −1` proved /
   net-route `c₂ ≈ −8` pair), which remains the open leg.

4. **μ–p tension (tnjb substance): the residual is NOT the N=0 rung.**
   Back-extrapolating the bare-proton rung `V₀ = c·V₁ − V₂` gives
   `E₀·V₀^even ≈ +0.52 MeV` (D) / `−0.31 MeV` (L) — three orders above
   the μ–p residual `≈ 2.27e-4 MeV` (242 ppb of m_p,
   [`2026-05-28-mu-p-tension-substrate-floor.md`](2026-05-28-mu-p-tension-substrate-floor.md)).
   Scope-limited: the tension residual does not live on this ladder's
   N=0 rung; the complex-volume route to tnjb runs through the c_k-rung
   ladder, not the neutron chain.

## How the new framing helps tnjb (assessment recorded)

- **Proved prune**: `higgs_complex_volume_real` (amphichirality ⇒
  CS(4₁) = 0) shows the muon anchor has no missing imaginary face — any
  μ–p correction class must sit on the **proton/many-body side** (the
  binding defect 𝔙), not the anchor.
- **Named object**: the residual becomes a *specific computable object*
  (the Re-face of 𝔙) rather than an irreducible floor.
- **Falsifiable tie**: if the c_k-rung ladders of binding and Q_β share
  one bar-even multiplier (`recurrence_descent`), the m_p Re-face
  correction is **determined by measured CAL-2 data** — zero new
  parameters. This probe closed the N-chain version (degenerate-exact in
  log form; refuted in defect form); the u-rung version is the live
  follow-up.

## Cross-references

- Conjecture: [`binding-qbeta-complex-volume.md`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md)
- Prior probe: [`2026-06-30-complex-volume-bar-parity-binding-probe.md`](2026-06-30-complex-volume-bar-parity-binding-probe.md)
- Framing: [`2026-06-30-cal123-decay-width-complex-volume-reanalysis.md`](2026-06-30-cal123-decay-width-complex-volume-reanalysis.md)
- Lean: [`FigureEightSelfDuality.lean`](../../content/quantum-observable-universe/lean/QOU/Knot/FigureEightSelfDuality.lean)
