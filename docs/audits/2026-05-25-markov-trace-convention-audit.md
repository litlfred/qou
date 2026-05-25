# Markov-trace convention audit — Wenzl JM vs q-Schur across the framework

**Date**: 2026-05-25
**Branch**: `claude/convention-audit-and-lean-q-schur-2026-05-25`
**Status**: Audit. Catalogs every compute script touching Markov-trace
weights `y_λ` and classifies it as Wenzl Jones-Markov (tr(σ_i) = z) or
q-Schur Plancherel (tr(σ_i) = h). Prevents future confusion between the
two conventions.

## §1. The two conventions

The framework uses TWO Markov-trace conventions on the Iwahori-Hecke
algebra `H_n(q)`, both producing valid Markov traces but with different
normalizations:

| Convention | `tr(σ_i)` | `y_λ` formula | Used by |
|------------|-----------|---------------|---------|
| **Wenzl Jones-Markov (JM)** | `z = 1/(√q + 1/√q)` | LP (Schur orthogonality sum); no clean closed form | Mass formula (Borromean), `mass_table_ppb.py` |
| **q-Schur Plancherel** | `h = q − q⁻¹` | **Closed form**: `q^{content_sum(λ)} / [n]_q!` | Torus knot characters, T(2,k) lepton tower |

**Both are "Markov traces"** in the formal sense (satisfying the Markov
axiom `tr_M(σ_i · w) = tr(σ_i) · tr_M(w)` for `w ∈ H_{n-1}`), but they
solve different normalization conditions. Same chi_λ values; different
y_λ values.

## §2. Cross-check: H_2

For the simplest non-trivial case, both conventions are well-known:

| Quantity | Wenzl JM | q-Schur |
|----------|----------|---------|
| `tr(σ_1)` | `z = 0.4993...` | `h = 0.2091...` |
| `y_(2)(q_0)` | `0.6963` (from `pn.trace_weights_n(2, q_0)`) | `0.5520 = q/[2]_q` (from `pn.trace_weights_n_q_schur(2, q_0)`) |
| `y_(1,1)(q_0)` | `0.3037` | `0.4480 = q⁻¹/[2]_q` |

**Different y_λ values; same chi_λ values.** Pick the convention that
matches your physics.

## §3. The Borromean closed form — Wenzl JM

The closed form `tr_M(β_𝓑_3) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)` (from
`prop:borromean-markov-trace-closed-form`, commit `21682492c`) is the
**Wenzl Jones-Markov trace**. Verified empirically:

```
Wenzl JM via LP at H_3:  0.998562 (matches closed form to 4 dp)
q-Schur at H_3:          0.668722 (does NOT match)
```

The framework's mass formula `B = ν_SDP · m_e · Vol(K)` therefore uses
**Wenzl JM convention**. The Borromean closed form is the structural
proof.

## §4. Per-script convention inventory

### §4.1 Wenzl Jones-Markov consumers (mass formula side)

These scripts use the Wenzl JM convention; consume `pn.trace_weights_n`
or the LP path:

| Script | Use |
|--------|-----|
| `alpha_k_jones_markov_h3.py` | H_3 reference solver — the canonical Wenzl JM impl |
| `alpha_k_jones_markov_h4.py` | H_4 extension (sibling commit `c70707397`) |
| `pyhecke_jones_markov_atlas.py` | Generic H_n LP solver (mine) |
| `run_jones_markov_atlas_all_atoms.py` | Per-atom runner |
| `mass_table_ppb.py` | Production mass table (single-block ν_SDP projection of Wenzl) |
| `crystal_yekutieli_probes_abcd.py` | Probe of Wedderburn weights |
| `chirality_avg_content_atomic.py` | Wedderburn weights for chirality |
| `y_lambda_symbolic_validate.py` | Symbolic Wedderburn validation |
| `closed_form_tau_M.py` | tau_M closed-form trace via Wedderburn weights |
| `habiro_coefficients_interpolate.py` | Habiro coefficient interpolation |

### §4.2 q-Schur Plancherel consumers (torus knot / lepton side)

These scripts use the q-Schur convention; consume hardcoded
`y_(2) = q/[2]_q, y_(1,1) = q⁻¹/[2]_q` (H_2 only) or the new
`pn.trace_weights_n_q_schur(N, q)` for arbitrary N:

| Script | Use |
|--------|-----|
| `torus_knot_markov_trace_closed_form.py` | H_2-only T(2,k) closed form (sibling `5418678c8`) |
| `torus_knot_markov_trace_generalized.py` | Arbitrary H_N (mine, PR #1258) |
| `bw_chirality_isotopes.py` | Hardcoded q-Schur for isotope chirality |
| `rt_route_w_specific_correction_probe.py` | Hardcoded q-Schur for W± route |
| `six_fifths_categorical_proof_attempt.py` | Hardcoded q-Schur |
| `nv_pslq_tr_pure_basis.py` | Hardcoded q-Schur |
| `nv_pslq_extended_basis.py` | Hardcoded q-Schur |
| `t6_three_halves_factor_probes.py` | T6 tau probes via [3]_q · [2]_q / [4]_q form |
| `tau_amphichiral_sdp_probe.py` | Tau amphichiral via q-bracket form |
| `sage-borromean-gA.sage` | Bring genus-A weights |

### §4.3 Trace-convention agnostic

Scripts using `chi_lambda_braid` (just the characters, no y_λ weights):
not in either column. Many of my recent probes are in this category.

## §5. Audit recommendations

### §5.1 Refactor opportunity (wiring sweep)

The 8 hardcoded q-Schur scripts (§4.2) can be refactored to use
`pn.trace_weights_n_q_schur` for deduplication:

```python
# BEFORE (hardcoded H_2)
sq_2_q = q + 1/q
y_2 = q / sq_2_q
y_11 = (1/q) / sq_2_q

# AFTER (generic via Rust upstream)
import pyhecke_native as pn
y_lambda = pn.trace_weights_n_q_schur(N, q)  # arbitrary N!
```

Low-risk per-call migration; preserves exact numerics (verified
machine-precision agreement in PR #1258).

### §5.2 Naming convention

Future scripts touching Markov traces should EXPLICITLY name the
convention in the docstring:

```python
"""... Uses Wenzl Jones-Markov convention (tr(σ_i) = z).
    Compatible with mass formula (Borromean closed form).
"""
```

or

```python
"""... Uses q-Schur Plancherel convention (tr(σ_i) = h).
    Compatible with T(2,k) torus knot closed forms.
"""
```

### §5.3 Lean formalization

The q-Schur closed form `y_λ(q) = q^{content_sum(λ)} / [n]_q!` should
be Lean-stated as a `theorem` with proof, anchoring the convention
formally. Stub: `QOU.BraidsAndKnots.QSchurClosedForm.lean`.

The Wenzl JM y_λ via Schur-orthogonality sum can also be stated as a
`def` with the orthogonality identity proved.

### §5.4 No mass-formula migration needed

The mass formula uses Wenzl JM (confirmed §3). DO NOT migrate
`mass_table_ppb.py` or related production callers to q-Schur — that
would CHANGE the predicted mass values. The two conventions are
NOT interchangeable for physics.

## §6. Open questions

1. **Is there a structural reason** the framework uses Wenzl JM for mass
   and q-Schur for lepton tower? They might both reduce to the same
   physical observable via an appropriate normalization — but currently
   each is anchored independently.

2. **Closed form for Wenzl JM**: confirmed analytically that there's no
   simpler form than the Schur-orthogonality sum. Heavy atoms (A ≥ 5)
   in Wenzl JM convention remain LP-bound.

3. **Lean cross-validation**: a theorem proving `Σ_λ y_λ_Wenzl · dim_q(λ)
   = 1` and `Σ_λ y_λ_q_schur · dim_q(λ) = 1` (both Markov-normalized)
   while showing they're distinct as functions of q.

## §7. Cross-references

- `pn.trace_weights_n(n, q)` — Rust upstream for Wenzl JM (LP-based)
- `pn.trace_weights_n_q_schur(n, q)` — Rust upstream for q-Schur (closed form, PR #1256)
- [`docs/audits/2026-05-25-infra-audit-h3-vs-hn-hardcoded-api.md`](2026-05-25-infra-audit-h3-vs-hn-hardcoded-api.md) — H_3 hardcode infra audit (companion)
- PR [#1258](https://github.com/litlfred/qou/pull/1258) — torus-knot generalization
- Sibling commit `5418678c8` — H_2 T(2,k) hardcoded closed form (q-Schur side)
- Sibling commit `21682492c` — `prop:borromean-markov-trace-closed-form` (Wenzl JM side)
