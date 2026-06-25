# Scope — discharging Identity I's two `PlancherelSnData` axioms (the `S_n` rep-theory Mathlib-infra program)

**Date:** 2026-06-24
**Status:** scoping only — a *multi-PR / multi-session* program, deliberately **not** attempted in one session.
**Context PRs:** #2655 (per-partition (A), merged), #2709 (the conditional-class formalization this program would un-condition).

> **Update (2026-06-25, [#2760](https://github.com/litlfred/qou/pull/2760)) — per-`n` down-payment landed.** The slice (i)/(ii) need at small `n` is now discharged **without** any of the P1–P5 infra below: explicit `PlancherelSnData {3,…,12}` instances (`IdentityIPlancherelInstances.lean`) wire the already-`decide`-verified `dim_validated_le12` / `idB_verified_le12` computations (`dim:=dimHLF`) into the class, so Identity I and `twoM_eq_plancherel_hook_sum` are **unconditional for `n ≤ 12`** (covering the deuteron `n=3`, keystone `n=5`, defect-cubic sign flip `n=7`).  The keystone defect coefficient `n144C` itself is then grounded in the genuine Plancherel squared-hook sum (`n144C_eq_twelve_plancherel` / `defect_closedform_plancherel`), eliminating the carried `def twoM`. `#print axioms` on the capstones = `[propext, Classical.choice, Quot.sound]` (no `sorry`, no custom axiom). This does **not** discharge the general-`n` class (P5 below); it is the tractable down-payment that makes the conditional terminus also an *unconditional* result on the physically-used `n`.

## Goal

Fully close **Identity I** `M(n) = (1/n!)·Σ_{λ⊢n} dim(λ)²·Σ_{c∈λ} h_c² = n(3n−1)/2` in Lean,
**sorry-free and unconditional**, thereby turning the s5-so3 keystone's carried
`WLambdaDefect.twoM` into a proved quantity (and so the falsifiable defect cubic
`144·C(n) = −n(n−1)(2n−13)` rests only on proved inputs).

[`IdentityIPlancherelConditional.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/IdentityIPlancherelConditional.lean)
(#2709) already proves Identity I **conditional** on the class `PlancherelSnData n`, which
axiomatises exactly the two standard facts the pinned Mathlib lacks:

- **(i)** `Σ_λ dim(λ)² = n!` — `sum_dim_sq`;
- **(ii)** `2·Σ_λ dim(λ)²·Σ_c c(c)² = n(n−1)·n!` — `two_sum_dim_sq_content` (the
  Jucys–Murphy / Okounkov–Vershik content-square Plancherel mean, cleared of `1/n!`).

The per-partition glue **(A)** `Σ_c h_c² = Σ_c c(c)² + n²` is already proved unconditionally
(#2655). So this program is exactly: **prove (i) and (ii) in Lean, then provide the
`PlancherelSnData n` instance for general `n`** (discharging the class), which collapses the
conditional theorems to unconditional ones.

## Why this is multi-PR (the pinned-Mathlib gap)

Recon (2026-06-24, toolchain `v4.24.0`): Mathlib provides `Combinatorics/Young/{YoungDiagram,
SemistandardTableau}` and basic `RepresentationTheory` (FDRep, characters, Maschke) but **none**
of the partition-indexed `S_n` representation theory the two axioms need:

- no **Specht modules** / `S_n`-irreducibles indexed by partitions `λ ⊢ n`;
- no **Jucys–Murphy elements** `X_k = Σ_{i<k} (i k) ∈ ℂ[S_n]`;
- no **Okounkov–Vershik** content theorem (the `X_k` act on the Gelfand–Tsetlin basis of `V_λ`
  with eigenvalues = cell contents).

Each is a substantial formalisation; collectively they are the kind of contribution that
normally lands **upstream in Mathlib** over many PRs, not in a paper repo in one session.

## Phased build

| Phase | Deliverable | Depends on | Rough size | Discharges |
|------|-------------|-----------|-----------|-----------|
| **P1** | `S_n` irreducibles indexed by `λ ⊢ n` (Specht modules over `ℚ`/`ℂ`): construction, irreducibility, completeness (every irrep is some `S^λ`) | Mathlib `RepresentationTheory`, `Combinatorics.Young` | large (foundational) | prerequisite for (i),(ii) |
| **P2** | `dim(λ) = #SYT(λ)`; `Σ_λ dim(λ)² = n!` via the RSK correspondence (bijection `S_n ≃ Σ_λ SYT(λ)²`) **or** the regular-rep decomposition `ℂ[S_n] ≅ ⊕_λ End(S^λ)` | P1 | medium–large | **(i)** `sum_dim_sq` |
| **P3** | Jucys–Murphy elements `X_k`; centrality of `Σ_k X_k²`; its eigenvalue on `S^λ` is `Σ_{c∈λ} c(c)²` (Okounkov–Vershik / the GZ-basis content action) | P1 | large | core of **(ii)** |
| **P4** | Plancherel average = identity coefficient: `(1/n!)Σ_λ dim²·(scalar of Σ X_k² on S^λ) = [Σ_k X_k²]_e = Σ_{k<n}(k−1) = binom(n,2)` — the arithmetic core `jm_identity_coeff_two` is **already proved** | P3 + `jm_identity_coeff_two` | small–medium | **(ii)** `two_sum_dim_sq_content` |
| **P5** | bridge the abstract `λ ⊢ n` index to the `List ℕ` model used by (A)/`PlancherelSnData` (sorted-list ↔ `Nat.Partition`/`YoungDiagram`), then provide `instance : PlancherelSnData n` for all `n`; collapse #2709's conditional theorems to unconditional | P2, P4, #2709 | medium | **the class itself** |

P2 has two independent routes (RSK bijection vs regular-rep `Σ dim²=|G|`); the regular-rep route
may already be partly in Mathlib's character theory (`∑ χ(1)² = |G|`) — **a P0 spike should first
check** whether `Σ_{irrep} dim² = card G` exists in the pinned Mathlib and only needs the
partition-indexing of P1 to become (i). If so, P2 reduces to P1 + a re-indexing.

## Decisions for the owner

1. **Upstream vs in-repo.** Specht modules + JM are natural **Mathlib upstream** contributions;
   doing them in-repo duplicates effort the community may want. Recommend: build minimal in-repo
   versions only as far as (i),(ii) need, and flag the general pieces for upstreaming.
2. **Is it worth it?** The two axioms are textbook-standard and the conditional formalization
   (#2709) is a legitimate, honest terminus (§3b-cond). Unconditioning buys *rigor-completeness*
   of one keystone input, **not** any new physics. Outside-view: the keystone's *open* object is
   the geometric `W_λ` realization (owner-gated, #2488/#2524/#2503/#2608), not Identity I — so
   this program is **rigor hygiene, not frontier progress**. Prioritise accordingly.
3. **Scope of P1.** Full Specht-module theory, or only the slice (i)/(ii) need (dimensions +
   the content action on a single distinguished basis)? The latter is much smaller.

## Discipline

No fit; base ring `ℤ`/`ℚ`/`ℂ` (nothing archimedean). Every phase lands as its own PR with
`lean`-direct verification; each `sorry` (if a phase is staged) carries a `-- Ref:` to this doc.
The conditional formalization (#2709) is the current honest state; this program only removes the
two named axioms — it changes no statement and no physical claim.

## Cross-references

- [`IdentityIPlancherelConditional.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/IdentityIPlancherelConditional.lean) — the conditional theorems + `PlancherelSnData`.
- [`IdentityIContentDecomposition.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/IdentityIContentDecomposition.lean) — (A), proved (#2655); `jm_identity_coeff_two` (P4 core).
- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — `twoM` (the carried Identity I).
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger.
- Literature: Okounkov–Vershik (GZ basis / content eigenvalues), James (Specht modules), the RSK correspondence for `Σ dim² = n!`.
