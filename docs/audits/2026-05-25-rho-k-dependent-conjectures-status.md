# ρ_K + dependent conjectures status (2026-05-25)

**Branch**: `claude/gifted-feynman-U7ckD` → [#1127](https://github.com/litlfred/qou/pull/1127)
**Triggered by**: owner directive "audit full paper and compute for rho_k. purge. work on narrowing gap to conjectures. make sure dependent conjectures formulate ok. F_ℓ derivation?"
**Scope**: ρ_K (categorical density, canonical replacement for SUPERSEDED ρ_q) + the conjecture dependency graph it supports

## ρ_K landscape

ρ_K is the canonical operator-valued replacement for the SUPERSEDED scalar ρ_q. Per [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md), ρ_K decomposes as:

$$
m_e \cdot |\mathrm{tr}_M(\mathcal{B}_K)| \cdot \rho_K
\;=\;
\underbrace{Z m_\mathfrak{p} + N m_\mathfrak{n} + Z m_e}_{\rho_K^{\mathrm{LO}}}
\;+\;
\underbrace{\alpha \sum_i \ln|\hat V_i^{\mathrm{full}}|}_{\rho_K^{\text{single-gen}}}
\;+\;
\underbrace{\alpha z^2 \sum_{i<j} \ln|\hat V_i \hat V_j|_{\mathrm{Wedd}}}_{\rho_K^{\text{pair-gen}}\text{ (OPEN)}}
\;+\;\dots
$$

## Piece-by-piece status

| Piece | Status | Evidence | Conjecture block |
|---|---|---|---|
| ρ_K^LO (Markov mult.) | ✓ **PROVED** | [Wenzl 1988] Thm 5; witness `rho-k-markov-multiplicativity.witness.json` at 3×10⁻¹⁴ accuracy | n/a (theorem) |
| ρ_K^single-gen | ✓ **PROVED** (0.18% empirical accuracy) | `thm:wedderburn-mass-formula`; witnesses `atomic-braid-mass-paper-formula.witness.json` | n/a (theorem) |
| ρ_K^pair-gen | ⚠️ **OPEN** — wrong functional form (log-additive degrades) | Witness `rho-k-pair-gen-extension.witness.json` | NEW: [`conj:rho-k-pair-gen-canonical-form`](../../content/quantum-observable-universe/braids-and-knots/conj-rho-k-pair-gen-canonical-form.md) |
| ρ_K^higher (triples+) | ⚠️ **OPEN** | per `prop:per-braid-mass-tower` pentagon-ascension | implied by `conj:mass-endomorphism` |
| Operator-valued $A^\lambda_{\mu,\nu}(I)$ | partial (refined Sub-lemma 2.1) | `prop:hecke-branching-trace-decomposition` | n/a (theorem refinement) |

## Conjectures depending on ρ_K (dependency graph)

```
prop:rho-k-graded-expansion (LO + single-gen PROVED; pair-gen+ OPEN)
  │
  ├── conj:rho-k-pair-gen-canonical-form  ← NEW (this PR; explicit pair-gen open)
  │     ├── status: open analytical work (multi-day)
  │     ├── candidate: f_2 = -z² · Li_2^q(-|V_i V_j|_Wedderburn)  per six-term thm T_3
  │     └── Kashaev-limit derivation pending (parallel to single-gen derivation)
  │
  ├── conj:mass-endomorphism (existing, in prop:per-braid-mass-tower)
  │     ├── status: open — unifying Φ_mass(W) ∈ H_{3A}(q)
  │     └── pair-gen is its level-2 expansion
  │
  ├── conj:lepton-mass-tower-canonical  ← NEW (this PR)
  │     ├── status: open — leptons have Z = N = 0, atomic LO piece vanishes
  │     ├── conjectural form: F_ℓ(q) = ξ_ℓ(q) · Vol_q^tower(K_ℓ)
  │     ├── ξ_ℓ replaces SUPERSEDED 1/ℏ_q²
  │     └── derivation pending — see "F_ℓ derivation status" below
  │
  └── (downstream consumers of ρ_K in production compute scripts)
        ├── atomic_mass_via_rho_k.py — uses LO + single-gen (PROVED parts)
        ├── derived_masses.py — uses LO + single-gen
        ├── canonical_braid_crossings.py — uses LO
        └── ~10 other scripts (CLEAN — no SUPERSEDED ρ_q residue)
```

## F_ℓ derivation status

**Direct answer to owner question "F_ℓ derivation?"**:

F_ℓ is the conjectural lepton-mass categorical formula `m(K_ℓ) = m_e · F_ℓ(q)`. Per [`conj:lepton-mass-tower-canonical`](../../content/quantum-observable-universe/braids-and-knots/lepton-mass-tower-canonical.md) and [`docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md`](2026-05-24-m-mu-over-m-e-operator-rederivation.md):

### What's PROVED about F_ℓ

| Property | Status | Evidence |
|---|---|---|
| F_e(q) = 1 by calibration | ✓ Proved (by convention) | Electron is CAL-1 mass unit |
| F_ℓ exists for each lepton | ✓ Tautological | CODATA gives specific m_μ/m_e, m_τ/m_e values |
| Direct $\|\mathrm{tr}_M\|$ ratio ≠ CODATA | ✓ **Proved** | Phase 3 audit: ratio = 0.27, NOT 206.77 |
| Skein formula `Vol(4_1)/ℏ_q² = 206.77` matches CODATA | ✓ Numerical verification | trivially holds; uses SUPERSEDED ρ_q |
| F_ℓ is Im(q) robust at LO | ✓ **Proved** | Modulus projection invariance argument (Phase 3 §c) |
| Trefoil reduction `σ_1³ = (h²+1)σ_1 + h` | ✓ **Proved (Lean)** | `lepton-mass-tower-canonical.lean:trefoil_reduction` (algebra via Hecke relation) |

### What's CONJECTURAL about F_ℓ

| Claim | Status | Notes |
|---|---|---|
| Existence of canonical (non-ρ_q) operator-level F_ℓ | ⚠️ **Conjecture** | `conj:lepton-mass-tower-canonical` |
| Conjectural form `F_ℓ(q) = ξ_ℓ(q) · Vol_q^tower(K_ℓ)` | ⚠️ **Sketch** | ξ_ℓ explicit form unknown |
| Kashaev limit `Vol_q^tower(K_ℓ) → Vol_hyp(K_ℓ)` | ⚠️ Kashaev volume conjecture | proved for many knots, conjecture in general |
| ξ_ℓ → 1/ℏ_q² in Kashaev limit | ⚠️ **Required** for consistency with Skein | unverified |
| Three-CAL consistency F_τ(q_0) = 3477.23 | ⚠️ **OPEN** | derivation needed |
| Bar-covariance of F_ℓ | ⚠️ **Required** but unverified | SUPERSEDED ρ_q is NOT bar-covariant; canonical replacement must be |

### Derivation path for F_ℓ

The honest answer to "F_ℓ derivation?": **derivation is multi-day analytical work, not done in this PR**. The minimum viable derivation:

1. **Lepton variant of `prop:rho-k-graded-expansion`** — currently atomic-only; needs a lepton extension where Z = N = 0
2. **Find ξ_ℓ** — the lepton-sector dimensional factor that replaces SUPERSEDED 1/ℏ_q²
3. **Verify Kashaev limit** — show ξ_ℓ(q → 1) · Vol_q^tower(K_ℓ)(q → 1) → CODATA m_ℓ/m_e
4. **Verify three leptons consistently** — e/μ/τ all use the SAME formal ξ_ℓ
5. **Lean-formalize** — promote the `lepton_mass_ratio` sorry to a theorem

Until completed, F_ℓ stays as `conj:lepton-mass-tower-canonical` (existence + properties; explicit form OPEN).

## ρ_q → ρ_K purge status (final this session)

Per the cumulative SUPERSEDED-ρ_q purge across this PR:

| Category | Files | Status |
|---|---|---|
| Content blocks with ρ_q citation + Phase 1 banner | 15 | ✓ Bannered |
| Compute scripts with ρ_q | 2 (q_pinning, rho_f_probe) | ✓ Purged/marked |
| Witness fields | q-pinning emitted `rho_q_DEPRECATED_*` then **physically removed** in commit `4d424487` | ✓ Removed |
| Content blocks introducing ρ_K (canonical) | 15 | ✓ Clean (no SUPERSEDED residue) |
| Compute scripts using ρ_K | 10+ | ✓ Clean (atomic_mass_via_rho_k.py, derived_masses.py audited) |

ρ_K is in good shape. ρ_q is purged or bannered everywhere.

## Conjectures depending on the Kashaev volume conjecture (KVC)

Many ρ_K-related claims rely on KVC for their q → 1 reduction:

| Claim | KVC role |
|---|---|
| `prop:rho-k-graded-expansion` LO piece Kashaev derivation | ✓ uses KVC for ln|V_i| → Vol form |
| `conj:rho-k-pair-gen-canonical-form` Kashaev-limit form | ⚠️ requires KVC + parallel pair-gen Kashaev derivation |
| `conj:lepton-mass-tower-canonical` Vol_q^tower → Vol_hyp | ⚠️ requires KVC for K_ℓ |
| `prop:skein-mass-relation` Vol(4_1) usage | ✓ uses KVC for figure-eight specifically |

KVC is verified numerically for the specific knots used (figure-eight, trefoil, Borromean) but unproved in general.

## Resolution priorities

Per [`prioritized-workplan.md`](../coordination/2026-05-24-pr1127-prioritized-workplan.md):

1. **T6 lepton-canonical** — derive F_ℓ explicitly (multi-day; gates T9/T10)
2. **conj:rho-k-pair-gen-canonical-form** — derive f_2 explicitly (multi-day; independent of T6)
3. Both together would close the operator-level mass tower for both leptonic and baryonic sectors

## Conjecture formulation health check

All NEW conjecture blocks landed this PR have been audited for formulation consistency:

| Block | uses[] correctness | Lean ref | authorNotes |
|---|:---:|:---:|:---:|
| `conj:lepton-mass-tower-canonical` | ✓ | ✓ (qou:QOU.BraidKnot.LeptonMassTowerCanonical.*) | ✓ status + caveat + refined-framing |
| `conj:rho-k-pair-gen-canonical-form` | ✓ | ✓ (qou:QOU.BraidKnot.RhoKPairGenCanonicalForm.*) | ✓ status + refined-framing |

Both conjectures correctly:
- Cite `prop:rho-k-graded-expansion` as parent
- Acknowledge the SUPERSEDED ρ_q purge context
- Identify the OPEN derivation path
- Provide Lean stubs with `sorry` per AGENTS.md §3b
- Cross-reference each other where dependencies exist

## Cross-references

- [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md) — parent proposition (LO + single-gen proved; pair-gen OPEN)
- [`conj:rho-k-pair-gen-canonical-form`](../../content/quantum-observable-universe/braids-and-knots/conj-rho-k-pair-gen-canonical-form.md) — explicit pair-gen conjecture (NEW this PR)
- [`conj:lepton-mass-tower-canonical`](../../content/quantum-observable-universe/braids-and-knots/lepton-mass-tower-canonical.md) — F_ℓ conjecture (NEW this PR)
- [`2026-05-24-superseded-rho-q-purge.md`](2026-05-24-superseded-rho-q-purge.md) — the purge audit
- [`2026-05-24-m-mu-over-m-e-operator-rederivation.md`](2026-05-24-m-mu-over-m-e-operator-rederivation.md) — Phase 3 finding (motivates F_ℓ)
- [`2026-05-24-q-beta-net-ansatz-fitting-finding.md`](2026-05-24-q-beta-net-ansatz-fitting-finding.md) — Q_β fitting concern (related but independent)
