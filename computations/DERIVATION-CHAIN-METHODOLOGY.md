# Derivation chain methodology

**Directive (post-PR-#472):** every numerical claim in the QOU
computation pipeline must trace back to the seven first-principles
entrypoints via a **`DerivationChain`** that walks step-by-step
with explicit **jet order**, **GB filtration level**, **spectral
stratum**, and **trust basis** annotations.

Existing computational scripts are **not trusted by default** —
they must be backed by (or pushed back via) a derivation chain.

## The seven first-principles entrypoints

`derivation_chain.FirstPrinciple` (canonical names + Lean refs):

| Enum | Canonical ref | Meaning |
|------|---------------|---------|
| `HECKE_ENERGY` | `Hecke.Energy` | per-crossing energy `(q − q^{-1})` from the Hecke relation |
| `CATEGORICAL_ACTION` | `Cat.Action` | categorical action of `B_n` via the R-matrix |
| `FROBENIUS_PAIRING` | `Frobenius.Pairing` | trace ↔ character duality + Reeb-foliation splitting |
| `NONABELIAN_STOKES` | `Nonabelian.Stokes` | holonomy consistency of the q-connection |
| `WEDDERBURN` | `Wedderburn` | semisimple decomposition `H_n(q) ≅ ⊕_λ M_{f_λ}(K(q))` |
| `SCHUR` | `Schur` | Schur–Weyl duality `U_q(sl_2) ↺ V^{⊗n}` and weights `w_λ(q)` |
| `FINITE_JONES` | `FiniteJones` | existence + uniqueness of the Markov trace |

These are the **only** nodes without inputs.  Everything else
must derive from them by named operations.

## Trust basis hierarchy

`derivation_chain.TrustBasis` (strongest → weakest):

| Basis | Meaning | Required fields |
|-------|---------|-----------------|
| `AXIOM` | first-principles entrypoint | `lean_ref` |
| `LEAN_PROVEN` | Lean theorem with no `sorry` | `lean_ref` |
| `MATHLIB_CITED` | invokes a Mathlib lemma | `lean_ref` |
| `DERIVED` | proven within this chain by a prior trusted step | (none) |
| `SCRIPT_CITED` | cites an existing computational script | `notes` containing `script: <path>` |
| `COMPUTATIONAL` | bare numerical eval (sympy / mpmath) | usually only at the leaf |

A chain with **zero `SCRIPT_CITED` steps** is the goal —
"fully-trusted modulo axioms".  The validator flags chains with a
`SCRIPT_CITED` frontier to make the remaining work explicit.

## Per-step annotations

Every `DerivationStep` records:

- **`jet_order`** — order of the underlying object (0 for algebraic,
  1 for connections / 1-forms, 2 for curvatures / 2-forms, …).
  `None` when jet order doesn't apply.
- **`gb_filtration_level`** — `J^ℓ / J^{ℓ+1}` stratum of the
  GS-filtered Hecke algebra; `0` is the descended (E⁰) page,
  higher levels are residue contributions.  `None` when
  filtration-independent.
- **`spectral_stratum`** — which residue / cyclotomic stratum
  (e.g. `"ζ_3"`, `"archimedean (q_0 ∈ ℝ_{>1})"`).  `None` when
  not spectral.

These annotations let downstream tooling track WHERE in the
GB-filtration / jet-tower / spectral picture each numerical claim
sits.

## Authoring a chain

1. Pick a target value (e.g. `tr_M(He, q_0) ≈ ?`).
2. Write a `build_*.py` script that constructs a
   `DerivationChain`, step by step, with the seven first-principles
   referenced **only as the inputs of the first few steps**.
3. Each subsequent step references previous step `output_name`s
   and / or first-principles.
4. Save with `chain.save(path)`; the schema enforces structural
   well-formedness (`structural_check`).
5. The validator (`derivation_chain_validator.py`) walks the
   chain bottom-up and:
     - re-checks structural well-formedness,
     - cross-checks the COMPUTATIONAL leaf's value against the
       chain's `target_value`,
     - re-evaluates simple algebraic DERIVED steps where possible,
     - reports the trust profile (axiom / lean / mathlib / derived
       / script-cited / computational counts).

## Pushing back the SCRIPT_CITED frontier

Every `SCRIPT_CITED` step is a debt: it accepts the cited script's
output as ground truth without re-deriving.  To pay it off, write
a derivation chain whose target is exactly that script's output;
the chain becomes the new reference, and the original script
becomes an empirical-only check (its witness is then
`derivation-backed` per the audit).

## Witness trust marking

`derivation_chain_validator.py audit_witness_trust` classifies each
`*.witness.json` as:

- `derivation-backed` if some chain references its producing
  script (matched via `scriptFile` field or filename convention),
- `computational-only` (default) if no chain references it.

The audit is reported in `derivation-chain-audit.witness.json`
as the single source of truth for the methodology rollout state.

## Current chains (this directory)

| Chain | Target | Trust profile | Frontier? |
|-------|--------|---------------|-----------|
| `c-q-q0.derivation.json` | `c_q(q_0) ≈ 9.0926` | 2 axiom + 0 mathlib + 2 derived + 1 computational | **fully-trusted** |
| `schur-weyl-weight-3.derivation.json` | `w_(3)(q)` symbolic | 1 axiom + 2 mathlib + 2 derived | **fully-trusted** |
| `hoefsmit-rep-21-sigma1.derivation.json` | `ρ^{(2,1)}(σ_1)` symbolic | 1 axiom + 1 mathlib + 3 derived | **fully-trusted** |
| `p-tr-M-q0.derivation.json` | `tr_M(p, q_0) ≈ 2.1226` | 1 axiom + 1 mathlib + 5 script + 1 computational | script-frontier |
| `n-tr-M-q0.derivation.json` | `tr_M(n, q_0) ≈ 1.5894` | same | script-frontier |
| `D-tr-M-q0.derivation.json` | `tr_M(D, q_0) ≈ 0.1774` | same | script-frontier |

The two new frontier-paydown chains (`schur-weyl-weight-3`,
`hoefsmit-rep-21-sigma1`) discharge 4 of the 5 SCRIPT_CITED
steps in the atom chains: Schur-Weyl weights, Wedderburn block
dimensions, Hoefsmit-recipe categorical action, and Frobenius
pairing.  Only the atomic-braid-recipe step remains as
SCRIPT_CITED.

## Open frontier (next chains to author)

Roughly in priority order:

1. `atomic_braid_recipe` chain — pushes back the last remaining
   SCRIPT_CITED step in the atom chains.  Once this lands, the
   atom chains become **fully-trusted**.
2. After that: `c_q`-derived constants (`ℏ_q`, `η_q`, `χ_q`,
   `d_H(q)`) — short algebraic chains anchored in `c_q`.
3. Mass formulas: per-atom `𝔪 = Vol/ℏ_q²`, `M = 𝔪 · E_0`.
4. The 375 remaining `computational-only` witnesses (per the
   audit), in dependency order.
