# Path to 1 ppb — Computational Engine

*Canonical modules in `computations/` for the JSJ pipeline. `★` = use this. `⚠` = deprecated or subsidiary.*

## Substrate parameters

| module | role |
|--------|------|
| **`q_parameter.py`** ★ | canonical q₀, ℏ_q, ℏ_q², HA, z_markov (15-digit float) |
| **`q_pinning_50_digit.py`** ★ | mpmath at 50 digits — q₀, ρ_q, quantum ints, Plancherel weights |
| `lambda_descartes_q0.py` ★ | Legendre λ-invariant of Descartes curve (15-digit, verified); **port to 50-digit to enable ξ(q₀)** |

## JSJ + knot-volume canonical path

| module | role |
|--------|------|
| **`jsj_atom_volume.py`** ★ | B = 2m_e · A · 8G magic-atom formula |
| **`jsj_verification.py`** ★ | SnapPy census search → specific knot per atom |
| **`jsj_alpha_clustering.py`** ★ | α-cluster unfolding with c_αα = m_e · Vol(7²_1) |
| `knot-operator-table.py` ★ | per-torus-knot NFs + Markov traces |
| `basis_knot_tables.py` ★ | knot catalog (Vol, Jones, NF) |

## Markov trace / Hecke NF

| module | role |
|--------|------|
| `mass_endomorphism.py` ★ | basic per-gen Wedderburn V̂, Φ_q tower |
| `canonical_plus_multibrane.py` ★ | canonical Markov + ℏ_q² brane scaling |
| `binding_full_pipeline.py` ★ | top-level: Ocneanu + multibrane + Kähler orders |
| `unified_lift.py` ★ | Markov-stab + Kähler jet corrections (0,1,2) |
| `hecke_characters.py` ★ | Seminormal matrices, q-dim, Plancherel |
| `ocneanu_weights.py` ★ | ω_λ via inversion (with SYT-prefix cache) |
| `markov_trace_canonical.py` ★ | canonical Jones-Markov trace |

## DEPRECATED — do not use for B(atom)

| module | why deprecated |
|--------|----------------|
| **`exact_binding_per_operation.py`** ⚠ | sums log V̂, under-predicts 85-99% |
| **`predictive_binding_from_braid.py`** ⚠ | same issue |
| `atom_mass_volume.py` ⚠ | superseded by jsj_* |
| `atom_frobenius_volume.py` ⚠ | superseded |
| `tower_binding_full.py` ⚠ | old H_3-per-generator path |

## Probe modules (kept for reference)

| module | role |
|--------|------|
| `electron_chiral_probe.py` | negative result — weak-partner dressing |
| `positron_lifted_sdp.py` | negative result — explicit e⁻/e⁺ SDP |
| `proton_braid_sweep_gg.py` | negative result — γγ insertions |
| `three_E0_fit.py` | negative result — linear 3-E_0 |
| `per_block_phi_q.py` | negative result — per-block Φ_q saturates |
| `recursive_three_calibration.py` | partial-positive — A≤4 at 1.5% |
| `universal_three_calibration.py` | negative — atoms anti-bound |
| `pair_factorisation_probe.py` | negative — scalar vs traced V̂_ij |
| `content_weighted_pair_probe.py` | partial — JM-cell improvement on T/³He |
| `catalan_binding.py` | negative — α = m_e · 8G literal |
| `tower_volume_extractor.py` | preliminary — V_n per-level test |

## External libraries

- **SnapPy 3.3.2** — verified hyperbolic volumes (up to 50+ digits via `.high_precision()`)
- **mpmath 1.3.0** — arbitrary-precision arithmetic (50-100 digits standard)
- `sympy` — symbolic Hecke NF reduction
- `numpy`/`scipy` — transfer matrix linear algebra

## Entry points (bash)

```bash
# Quick sanity check: magic atoms match A·8G·2m_e
python3 computations/jsj_atom_volume.py

# Full atom-knot correspondence via census search
python3 computations/jsj_verification.py

# α-cluster unfolding for doubly-magic
python3 computations/jsj_alpha_clustering.py

# 50-digit substrate pinning
python3 computations/q_pinning_50_digit.py

# Canonical Markov + tower (production pipeline)
python3 computations/binding_full_pipeline.py
```
