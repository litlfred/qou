# Scope — discharging Identity I's two `PlancherelSnData` axioms (the `S_n` rep-theory Mathlib-infra program)

**Date:** 2026-06-24
**Status:** scoping only — a *multi-PR / multi-session* program, deliberately **not** attempted in one session.
**Context PRs:** #2655 (per-partition (A), merged), #2709 (the conditional-class formalization this program would un-condition).

> **Update (2026-06-25, [#2760](https://github.com/litlfred/qou/pull/2760)) — per-`n` down-payment landed.** The slice (i)/(ii) need at small `n` is now discharged **without** any of the P1–P5 infra below: explicit `PlancherelSnData {3,…,12}` instances (`IdentityIPlancherelInstances.lean`) wire the already-`decide`-verified `dim_validated_le12` / `idB_verified_le12` computations (`dim:=dimHLF`) into the class, so Identity I and `twoM_eq_plancherel_hook_sum` are **unconditional for `n ≤ 12`** (covering the deuteron `n=3`, keystone `n=5`, defect-cubic sign flip `n=7`).  The keystone defect coefficient `n144C` itself is then grounded in the genuine Plancherel squared-hook sum (`n144C_eq_twelve_plancherel` / `defect_closedform_plancherel`), eliminating the carried `def twoM`. `#print axioms` on the capstones = `[propext, Classical.choice, Quot.sound]` (no `sorry`, no custom axiom). This does **not** discharge the general-`n` class (P5 below); it is the tractable down-payment that makes the conditional terminus also an *unconditional* result on the physically-used `n`.

> **Update (2026-06-26) — P0 spike RESOLVED (the "does Mathlib already have `Σ dim² = |G|`?" question below).** Reconnaissance against the **pinned** Mathlib commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` (toolchain `v4.24.0`), via GitHub code search over the dependency tree (the sandbox blocks `leansearch`/`leanfinder`/`loogle` with proxy 403, and has no restored oleans, so this is source-level recon, not an LSP/`decide` check — re-confirm against the pinned olean tree once a build is available):
>
> | Fact the program needs | Pinned-Mathlib status | Evidence |
> |---|---|---|
> | Irreducible-character **orthogonality** (`⟨χ_V, χ_W⟩ = [V≅W]`) | **present** | `Mathlib/RepresentationTheory/Character.lean` (`scalar_product_char_eq_finrank_equivariant`; the `if Nonempty (V ≅ W) then 1 else 0` orthogonality) |
> | **Simple-iff-norm-one** `∑_g χ(g)χ(g⁻¹) = card G` | **present** (ref-hedge: `FinGroupCharZero.lean` is recent and may postdate `f897ebcf`; verify on the pinned tree) | `Mathlib/RepresentationTheory/FinGroupCharZero.lean` (`FDRep.simple_iff_char_is_norm_one`) |
> | **Degree-square sum** `∑_{irrep} dim(V)² = card G` (regular rep at `e`) | **ABSENT** (no packaged lemma under expected names) | no `leftRegular`-character-decomposition lemma; `∑ … = Fintype.card G` hits are the *simple-norm-one* criterion, not the global degree-square sum |
> | **`#irreps = #conjugacy classes`** | **ABSENT** (undergrad-curriculum gap) | `docs/undergrad.yaml` lists it with external-URL placeholders, no `decl:` |
> | **Specht modules / partition-indexed `Sₙ` irreps** | **ABSENT** | only `Nat.Partition` *combinatorics* exists (e.g. Glaisher `Nat.Partition.card_restricted_eq_card_countRestricted`); no `S^λ`, no partition→irrep map |
>
> **Conclusion (negative, and it shapes the plan).** The hopeful shortcut the P2 note below floats — "maybe `Σ dim² = |G|` is already in Mathlib, so P2 collapses to P1 + a re-indexing" — **does not hold**: that lemma is *not* packaged in the pinned Mathlib. So P2's regular-rep route must still **build** `Σ dim² = |G|` from the orthogonality relations that *are* present (medium cost), then compose with P1's partition-indexing. Net effect on the plan:
> - **P2 stays medium-large**, not "free"; its cheapest path is regular-character decomposition (`χ_reg = ∑_λ dim(λ)·χ_λ`, also absent) evaluated at `e`, **built on** the present orthogonality — not an off-the-shelf citation.
> - **HLF / RSK is NOT on the critical path for axiom (i).** Via the regular-rep route, `∑_λ dim_Specht(λ)² = n!` needs only P1 (Specht irreps complete + partition-indexed) + the built degree-square sum — **no hook-length formula**. HLF only re-enters if one insists `dim = dimHLF` (the concrete `List ℕ` model), which the `n ≤ 12` instances already discharge *computationally* (`dim_validated_le12`). So a future general-`n` instance is cleaner with `dim := dim_Specht` than with `dim := dimHLF`.
> - **P1 (Specht) remains the foundational blocker**, confirmed genuinely absent — consistent with the doc's Decision 2 ("rigor hygiene, not frontier progress; the keystone's *open* object is the geometric `W_λ` realization, not Identity I").

> **Update (2026-06-26, cont.) — Lean build restored; sandbox-verifiability mapped; P5 bridge landed.** Owner directed "build all needed infra." Established a `lean`-direct verification path (restored `lake-cache/qou-v4-24-0` → 2951 Mathlib oleans; `lean`-direct exit 0 confirmed) and probed the pinned tree authoritatively from the oleans (not GitHub-search this time). Hard findings that bound what is *buildable here*:
>
> - **No `Mathlib.Combinatorics.RSK` module at all** at the pin (the `RSKBridge.lean` docstring's "partial Mathlib RSK" is stale for v4.24.0) — RSK is wholly absent, not partial.
> - **`Combinatorics.Young` has only `YoungDiagram` + `SemistandardTableau`** — **no `StandardYoungTableau` type, no `numStandardYoungTableaux`.** Even *stating* `∑_λ #SYT(λ)² = n!` needs an SYT type built from `YoungDiagram` first.
> - **`Mathlib.RepresentationTheory.*` oleans are ABSENT from the restored cache (0 present)** — they are outside QOU's dependency cone, so they were never cached, and the release server / `cache get` are network-blocked. **Consequence: the entire representation-theory half of this program (P1 Specht, P3 Jucys–Murphy, P4 Plancherel-average, and the regular-rep `∑dim²=|G|`) is *not lean-direct verifiable in this sandbox at all*** — it can only be built where a full-Mathlib olean tree (or CI from-source build) is available.
>
> **What landed (the one verifiable, sorry-free, genuinely-additive piece): phase P5's index bridge.** [`QOU/Mathlib/PartitionListBridge.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/PartitionListBridge.lean) — `Nat.Partition n ≃ {weakly-decreasing positive List ℕ summing to n}` (`toList`/`ofList`/`equivSortedList` + the landing lemmas `toList_sorted/pos/sum/coe`), core-Mathlib only, **`lean`-direct exit 0, sorry-free, axiom-clean**. This bridges Mathlib's abstract `λ ⊢ n` index to the computable `List ℕ` model the (A)/`PlancherelSnData` combinatorics use, so an abstract `∑_{Λ : Nat.Partition n}` (e.g. the `RSKBridge` Burnside sum for axiom (i)) transports to the sorted-list model and back. P5's "sorted-list ↔ `Nat.Partition`" prerequisite is now **done**.
>
> **Honest status of "all needed infra."** The bulk — the rep-theory tower for axioms (i)/(ii) — is **0% present in pinned Mathlib and un-verifiable in this sandbox**, confirming the doc's "multi-PR / multi-session, deliberately not one session" framing and Decision 2 ("rigor hygiene, not frontier progress"). The dependency-ordered remaining work, and *where* each piece can be built:
>
> | Piece | Buildable here? | Why / next step |
> |---|---|---|
> | **P5 index bridge** | ✅ **done** | `PartitionListBridge.lean`, sorry-free |
> | **SYT type + `numStandardYoungTableaux`** over `YoungDiagram` | ✅ verifiable here | Mathlib lacks it; build from `YoungDiagram` (next most foundational verifiable target) |
> | **P2/(i) RSK `∑#SYT²=n!`** | ⚠ verifiable but large | needs SYT type first; RSK bijection from scratch (Mathlib has none) |
> | **HLF `dimHLF=#SYT`** | ⚠ verifiable but large | Greene–Nijenhuis–Wilf / hook-walk; needs SYT type |
> | **P1 Specht / P3 JM / P4 + regular-rep `∑dim²=\|G\|`** | ❌ not verifiable here | `RepresentationTheory` oleans absent + unfetchable; needs full-Mathlib env or upstream Mathlib |
>
> So: continuing "in this sandbox" means the **combinatorial route** (SYT type → RSK/HLF), each a multi-session theorem; the **representation-theory route** (cleaner for (i) via `∑dim²=|G|`, and the only route for (ii)) needs an environment with the full Mathlib olean tree or lands upstream in Mathlib. This is an owner-steering fork (Decision 1: in-repo vs upstream), recorded here.

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
rests on Mathlib's character theory. **The P0 spike is now RESOLVED (see the 2026-06-26 update at
the top): `Σ_{irrep} dim² = card G` is NOT packaged in the pinned Mathlib** (`f897ebcf`, `v4.24.0`) —
only the irreducible-character *orthogonality* and the *simple-norm-one* criterion are present. So
P2 does **not** reduce to "P1 + a re-indexing"; it must build the degree-square sum from
orthogonality (regular-character decomposition evaluated at `e`), then compose with P1. The spike's
one favourable finding: HLF/RSK is **not** on the critical path for (i) via this route (only P1 +
the built degree-square sum), so a general-`n` instance is cleaner with `dim := dim_Specht` than with
the concrete `dim := dimHLF`.

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
