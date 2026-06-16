# linking_weight residual — canonical-object determination (CONFIRM/REFUTE)

**Date:** 2026-06-01
**Branch:** `claude/linking-weight-residual-fix-2026-06-01`
**Scope:** CONFIRM-OR-REFUTE. No fit, no tuning to m_p / CODATA. Every number
is RAW. Independent reproduction of two merged sibling audits.

**Compute:** [`linking_weight_canonical_object_lwfix.py`](../../computations/linking_weight_canonical_object_lwfix.py),
witness [`linking-weight-canonical-object-lwfix.witness.json`](../../computations/linking-weight-canonical-object-lwfix.witness.json).

---

## Coordination — sibling branch is on a DIFFERENT residual

The sibling branch `claude/h4-residual-structural-derivation-2026-06-01`
(coord ledger `docs/coordination/2026-06-01-h4-residual-derivation.md`) is
working the **54 ppb residual on the Ocneanu `(α_em/π)/dim H_3` near-match**
(Form A `1+(1−π²/80)h⁴`, Form B `1+(7/8)h⁴+(G/(8π))h⁶`). That is a
*separate* object from this task's **`linking_weight` ≈ 2.533 / +2.89% m_p
residual** in `vol_density_borromean`. No collision; distinct files. The
sibling's verdict on its own residual is NULL at PSLQ-basis level (Task 1
positive cross-anchor, Task 2 negative integer-relation search) — that
does not bear on the linking_weight question here.

## The issue (from the two merged audits)

Production `vol_density_borromean = Vol(𝓑₃)/ℏ_q² × linking_weight_family_a(q)`,
where `linking_weight_family_a = (3q²+4+3q⁻²)/4 = 5/2 + (3/4)h² ≈ 2.533` at
q₀ — an H₄ (partitions-of-4) quantum-dimension average. The owner asked
whether this is the *canonical* object or whether the H₃ per-block trace
(the 3-strand Borromean braid lives in H₃) is the correct object.

## VERDICT: H₄ average is canonical-by-default but ASSERTED (CAL-4); +2.89% is the genuine residual

1. **The canonical object BY DERIVATION is neither a clean H₄ nor a clean
   H₃ trace.** Per `lambda-scale-substrate-form.md`, the H₄ average
   `λ_A = (1/4)Σ_{λ⊢4} dim_q V_λ` is a Lean-proved *identity* but an
   **acknowledged CAL-4 empirical near-match** — falsified as a categorical
   derivation by **eight independent structural searches** (Family A,
   32 sign-flip variants at H₄, Hecke levels H₂–H₇, transcendental ansätze,
   single-knot ansatz, q-locality, …). It is NOT the paper's Stage-4
   per-block factor and it does NOT index the knot's own braid (H₄ vs the
   H₃ 3-strand braid), by acknowledged design.

2. **Switching to the H₃ per-block trace REGRESSES m_p.** The 3-strand
   Borromean trace `J_𝓑₃ ≈ 1` (wenzl) gives `m_avg ≈ 406 MeV` (−56.7%),
   ~20× worse than production's +2.89%. So "switch to H₃ for the 3-strand
   braid" is RULED OUT — it is not the better canonical object.

3. **The +2.89% is the genuine current-best residual** between Family A's
   H₄ average (2.533) and the CODATA-implied `λ ≈ 2.460` (the value that
   round-trips m_p). It is NOT closable by changing the index set; it is the
   categorical-exactness refinement gap recorded in
   `docs/lambda-scale-absorbed-into-vol-density.md` (open R&D, no fit).

## Raw m_avg per candidate (from the lwfix witness)

Inputs (60 dps): `q₀ = 1.10997858…`, `m_e = 0.51099895` MeV,
`Vol(𝓑₃)/ℏ_q² = 746.418`, `m_avg^CODATA = 938.91875` MeV.

| candidate factor | factor at q₀ | m_avg = m_e·Vol/ℏ_q²·factor | err vs CODATA m_avg |
|---|---:|---:|---:|
| (A) production **H₄ average** | **2.532780** | **966.050 MeV** | **+2.890 %** |
| (B) H₃ bare-Borromean trace (wenzl) | 0.998562 | 380.870 MeV | −59.435 % |
| (B2) H₃ atomic-proton trace (PR #1623 §6, Rust) | 1.065310 | 406.329 MeV | −56.724 % |
| (C) bare (linking_weight = 1) | 1.000000 | 381.419 MeV | −59.377 % |

- **CODATA-implied λ target** (AUDIT-ONLY, the value that round-trips m_p):
  `(m_p/m_e)/(Vol/ℏ_q²) = 2.461648`. Family A's 2.532780 sits **+2.890 %**
  above it — that residual IS the +2.89 % m_p gap.
- **Ratio production / atomic-proton trace = 2.37750** — reproduces the
  documented 2.38× gate (PR #1623 §4) exactly.
- Family A h-coefficients: h⁰ = 5/2, h² = 3/4, h⁴⁺ = 0 (TERMINATES) — a
  Lean-proved exact identity, structurally distinct from the H₃ trace
  (leading 1, non-terminating tail).

The H₃ readings (bare-Borromean 0.9986 → 381 MeV; atomic-proton 1.0653 →
406 MeV) both regress catastrophically (−57 % to −59 %). The exact H₃
value depends on which 3-strand braid you trace, but **neither beats
production** — confirming that "switch the index set to H₃ for the
3-strand braid" is not the better canonical object. No fit applied; all
numbers from the witness.

## Discipline

- No tuning of `linking_weight` to hit CODATA. The +2.89% is REAL and
  reported honestly.
- Production default NOT changed; this is a confirm/refute audit + witness.
- Every number traces to the lwfix witness.

## Cross-references

- merged PR #1613 [`2026-06-01-vol-density-compute-vs-paper-audit.md`](2026-06-01-vol-density-compute-vs-paper-audit.md)
- merged PR #1623 [`2026-06-01-yekutieli-volume-join-derivation.md`](2026-06-01-yekutieli-volume-join-derivation.md)
- canonical framing [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)
- `content/quantum-observable-universe/mass-theory/lambda-scale-substrate-form.md`
- sibling (different residual) `docs/coordination/2026-06-01-h4-residual-derivation.md`
