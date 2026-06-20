# Hoefsmit Stage B — per-block T_β,λ probe scoping

**Date:** 2026-06-04 (status updated 2026-06-05)
**Branch:** [`claude/qbeta-stageB-cosh-relabel-2026-06-04`](https://github.com/litlfred/qou/tree/claude/qbeta-stageB-cosh-relabel-2026-06-04) — PR [#1866](https://github.com/litlfred/qou/pull/1866)
**Status:** SCOPING — **infra UNBLOCKED 2026-06-05** (see "Infra status" below); the cross-anchor per-block-localization probe is now implementable.
**Parent:** [`3d142447`](https://github.com/litlfred/qou/commit/3d142447) (Stage A: Hoefsmit operator infra validated, per-block χ^λ at q_0)
**Trigger:** the 1-factor (28-cand, PR #1860) and 2-factor (1323-cand, PR #1831) scalar c_3 search spaces are now both saturated; the c_3 categorical residue is "irreducibly operator-valued" per the audit `0e30e23e`. Stage A delivered the operator infra; Stage B is the natural next mechanical step.

> **Infra status (2026-06-05 update).** The blocker recorded below — the
> `chi_lambda_braid` Python fallback only supporting `q_value == q_0` —
> was **resolved on main by [`dcd598f1`](https://github.com/litlfred/qou/commit/dcd598f1)**
> ("fix(hecke_characters): chi_lambda_braid Python fallback now accepts
> arbitrary q"). A sibling also shipped the closely-related
> [`01802133`](https://github.com/litlfred/qou/commit/01802133) ("Stage C:
> per-block χ^λ(trefoil) closed forms — no float64") and confirmed the
> c_4+ precision floor in [`7f36be0e`](https://github.com/litlfred/qou/commit/7f36be0e).
> The "Infra blocker" section below is retained for the historical record;
> the cross-anchor per-block **c_3-localization** probe (the distinctive
> piece Stage C did not do — Stage C computes the per-block closed forms
> but does not run the cross-anchor ladder-inversion localization test)
> is now implementable without the Rust kernel and is the recommended
> next probe. Coordinate with the Stage C author before implementing to
> avoid duplicating the per-block χ^λ computation.

## TL;DR

A clean **per-block T_β,λ cross-anchor probe** is the natural extension
of Stage A (which built per-block χ^λ at q_0) and PR #1831 (which
introduced the cross-anchor c_3 target inversion). The question to
answer:

> **Is c_3 block-localised — i.e. dominated by a single Wedderburn
> partition λ ⊢ 3 of H_3 — or does it require multi-block coupling?**

If block-localised, the residue-A categorical identification reduces
to identifying one operator on one block. If multi-block, the search
space is intrinsically the joint operator product structure (much
harder, motivates the KLR/crystal upstream infra scope).

## Infra blocker

> **⚠ CORRECTION (2026-06-20): this blocker is RESOLVED in the current web
> sandbox.** `pyhecke_native` **builds here** in ≈ 42 s (`cargo`/`rustc` are on
> PATH; `pip install maturin`; `maturin build --release -m
> tools/pyhecke-native/Cargo.toml`; `rug` compiles GMP+MPFR from source via `cc`).
> Arbitrary-q `chi_lambda_braid` (plus `trace_weights_n`, `lagrange_projectors_mpfr`,
> …) are now available, so the cross-anchor per-block c_3-localization probe below is
> runnable without re-deriving the projection in-script. Recipe + 1e-15 validation:
> [`docs/audits/2026-06-20-pyhecke-native-build-unblocked.md`](../audits/2026-06-20-pyhecke-native-build-unblocked.md).
> Original blocker text retained below for the historical record.

The Python fallback in `computations/hecke/hecke_characters.py::chi_lambda_braid` only supports `q_value == q_0`:

```
ValueError: chi_lambda_braid() Python fallback only supports q_value == q_0;
install the Rust kernel (pyhecke_native) for non-default q_value.
```

The Rust kernel `pyhecke_native` is the production path for arbitrary
q (Stage A used the cached q_0 path); installing it requires a
PyO3/maturin build chain that this sandbox does not have.

Without `pyhecke_native`, the per-block χ^λ at q_muon cannot be
computed via the canonical infra. A direct in-script Hoefsmit
seminormal-form implementation for n=3 is mathematically tractable
(the trivial (3) and sign (1,1,1) representations are 1-d and the
standard (2,1) is 2-d), but **re-deriving the Markov-trace projection
that `chi_lambda_braid` uses risks subtle convention drift**: Stage A's
witness values do not match naive matrix-trace formulas
(`χ^(3)(σ₀σ₁σ₀) = q^3` would predict ≈ 1.367, but Stage A reports
≈ 1.110), so the projection is non-trivial and must mirror the
canonical convention exactly.

Per CLAUDE.md "don't iterate Lean / compute blind when verification
is unavailable", a re-implementation here would be doing exactly that
in the numeric domain. The honest move is to scope the probe + leave
it for a session with `pyhecke_native` available.

## What Stage B would test (when infra unblocks)

```
For each partition λ ⊢ 3 (Wedderburn blocks of H_3):

  1. χ^λ(β_e)(q) = chi_lambda_braid(λ, electron_word, q_value=q)
     evaluated at BOTH q_proton and q_muon.

  2. Per-block c_3 contribution: define a candidate per-block
     extension of the ladder inversion, e.g.

       c_3,λ(q) = (Q_codata,λ(q) / Q_N2,λ(q) - 1) / u(q)^3

     where Q_codata,λ is the λ-block-projected Q-value (requires
     a per-block decomposition of the canonical Q_codata).

  3. Verdict
       - BLOCK-LOCALISED if ∃ λ* such that c_3,λ*(q_p), c_3,λ*(q_m)
         match the scalar c_3 targets within 1 ppm at BOTH anchors
       - MULTI-BLOCK if no single-block reproduction works
```

The cross-anchor discriminator (~0.05 swing on c_3) is the same
rejection criterion the existing 2-factor sweep used and is what
distinguishes a structural localisation from a single-anchor coincidence.

## Deliverable

A `qbeta_hoefsmit_stage_b_per_block_crossanchor_probe.py` that:
- Imports `chi_lambda_braid` and reuses Stage A's enumerate-and-evaluate harness
- Re-uses `qbeta_utils.c3_target_at` for the scalar reference values
- Reports per-block c_3 candidates at both anchors + verdict
- Emits a witness with the BLOCK-LOCALISED / MULTI-BLOCK conclusion

Honest expected outcome per the saturation discipline: probably
NEGATIVE for block-localisation (consistent with audit `0e30e23e`'s
"open math is well-localised to GAP-A-3 / GAP-A-4"). A POSITIVE would
be a genuine discovery and would dramatically narrow the categorical
search.

## Sequencing notes

This probe sits **above** the production code (it's structural diagnostic, not a derivation closure). It does not require new content blocks or Lean
extensions. The `pyhecke_native` install path is documented in
`tools/pyhecke-native/` and would unblock several other operator-valued
probes too; consolidating them into a single infra-unblock PR is the
natural sequencing.

## References

- Stage A producer: [`computations/qbeta/qbeta_hoefsmit_tbeta_matrix_build_probe.py`](../../computations/qbeta/qbeta_hoefsmit_tbeta_matrix_build_probe.py)
- Cross-anchor c_3 inversion: [`computations/qbeta/qbeta_utils.py::c3_target_at`](../../computations/qbeta/qbeta_utils.py)
- Saturation context: [`docs/audits/2026-06-04-three-paths-refuted-roadmap-update.md`](../audits/2026-06-04-three-paths-refuted-roadmap-update.md)
- Coordination ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Rust kernel home: [`tools/pyhecke-native/`](../../tools/pyhecke-native/)
