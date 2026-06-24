# OV Tower — formalizing the Okounkov–Vershik labelling to discharge side‑2 of Identity (B)

**Status:** committed multi-session effort (owner directive 2026-06-24). Brick 1 in progress; bricks 2–5 are future work with honest `sorry` + `-- Ref:` placeholders.
**Goal:** fully discharge `RegularRepBlockTrace.SnWedderburnSpectralData` (the side‑2 hypothesis of Identity (B)) by formalizing the symmetric‑group representation theory that pins *which* Wedderburn block is *which* partition, with the Jucys–Murphy eigenvalue equal to the content‑square sum.

## Where we are

The Identity‑(B) trace equation `tr_reg(C₂) = n!·binom(n,2) = Σ_λ dim(λ)²·Σ_{c∈λ}c²` is formalized as:

| piece | status | where |
|-------|--------|-------|
| **Side 1** `tr_reg(C₂) = n!·binom(n,2)`, generic `CommRing` | **proved, merged** | `RegularRepTrace` (#2724) |
| **Side 2** conditional on `SnWedderburnSpectralData` | **proved, merged** | `RegularRepBlockTrace` (#2724) |
| **Existence** of the block decomposition (`k[S_n]` semisimple) | **proved** | `MaschkeSnSemisimple` (#2743) |
| **Structure** `k[S_n] ≃ ∏ᵢ Matrix(𝔫ᵢ)`, `Σ𝔫ᵢ² = n!` | **proved** | `WedderburnSn` (#2743) |
| **Labelling** `𝔫ᵢ ↔ partition λ`, `𝔫ᵢ = #SYT(λ)`, `ω = Σc²` | **THIS TOWER** | bricks 1–5 below |

After #2743, the *only* residual content of `SnWedderburnSpectralData` is the labelling — the
S_n‑specific Okounkov–Vershik layer, which is **not in Mathlib** (verified 2026‑06‑24: Mathlib has
`Combinatorics/Young/{YoungDiagram,SemistandardTableau}` and general `RepresentationTheory`, but **no
Specht modules, no StandardYoungTableau/#SYT, no partition↔irreducible classification, no hook‑length
formula, no Jucys–Murphy elements, no S_n character table**). So this tower is original
formalization, not infra‑fetching. Specht modules in particular are a long‑standing Mathlib
desideratum.

## The five bricks (dependency order)

```
  brick 1  StandardYoungTableau + numSYT            (pure combinatorics on YoungDiagram)
     │
  brick 2  SpechtModule S^λ                         (polytabloid construction)
     │
  brick 3  classification: {S^λ} = irreducibles     (Specht modules are a complete irredundant
     │                                                set of irreducibles of S_n over char‑0 k)
  brick 4  dim S^λ = numSYT λ                        (standard‑basis theorem)
     │
  brick 5  JM eigenvalue = contents (Okounkov–Vershik)
     │       (C₂ = Σ X_k² acts on S^λ by Σ_{c∈λ} content(c)²)
     ▼
  TOP      sn_spectralData_exists : Nonempty (SnWedderburnSpectralData k n)
           assemble bricks 3+4 (Idx = partitions, d = numSYT = 𝔫ᵢ, p/proj = isotypic blocks of the
           Wedderburn ∏Matrix from WedderburnSn) + brick 5 (ω = contents), discharging side 2 outright.
```

### Brick 1 — Standard Young tableaux + count
- `StandardYoungTableau (μ : YoungDiagram)` — bijective, row‑strict, column‑strict filling of `μ.cells` by `0..μ.card−1`.
- `numSYT (μ : YoungDiagram) : ℕ` — the count.
- **Refs:** [sagan2001] §3, [fulton1997]. **Status:** in progress this session (sorry‑free target).
- Pure combinatorics on Mathlib's `YoungDiagram`/`Ssyt`; the one fully‑tractable brick.

### Brick 2 — Specht modules
- `SpechtModule (k) (μ : YoungDiagram) : Type` (a `k[S_n]`‑module), via tabloids + polytabloids.
- **Refs:** [sagan2001] §2.3–2.4, [james1984representation], [dipper-james1986] (Hecke generalization).
- **Status:** future. Large. The construction (tabloids = cosets, polytabloid = signed column‑sum) plus the `k[S_n]`‑action.

### Brick 3 — classification
- `instIsSimpleModule_specht` and `specht_complete_irreducibles`: over a char‑0 field, `{S^λ : λ ⊢ n}` is a complete, pairwise‑non‑isomorphic list of the irreducible `k[S_n]`‑modules; hence the Wedderburn index set of `WedderburnSn.sn_wedderburnArtin` is (in bijection with) partitions of `n`.
- **Refs:** [sagan2001] §2.4, [james1984representation]. **Status:** future. Large.

### Brick 4 — dimension = #SYT
- `dim_specht_eq_numSYT : Module.finrank k (SpechtModule k μ) = numSYT μ` (standard‑basis theorem: the standard polytabloids are a basis). Combined with brick 3, identifies the Wedderburn `𝔫ᵢ` with `numSYT λ`.
- **Refs:** [sagan2001] Thm 2.5.2. **Status:** future. Large.

### Brick 5 — Jucys–Murphy eigenvalue = contents (the OV theorem)
- `JucysMurphy (k) (n) (i) : k[S_n]` (already present in spirit as `RegularRepTrace.centralC2 = Σ X_k²`); the Gelfand–Tsetlin basis of `S^λ`; and `jucysMurphy_eigenvalue : X_k` acts on the GZ basis vector indexed by a standard tableau `T` by the scalar `content(T⁻¹(k))`, hence `C₂ = ΣX_k²` acts on `S^λ` by `Σ_{c∈λ} content(c)²`.
- **Refs:** [vershik-kerov1977] (foundational), the Okounkov–Vershik approach. **Status:** future. Very large — this is the content of the OV paper.

### TOP — discharge `SnWedderburnSpectralData`
- `sn_spectralData_exists (n : ℕ) : Nonempty (SnWedderburnSpectralData k n)` (for a suitable char‑0 / split field, e.g. ℚ): build the structure with `Idx = partitions of n`, `d λ = numSYT λ` (brick 4), `ω λ = Σ_{c∈λ} content(c)²` (brick 5), and the isotypic projections from the `WedderburnSn` `∏ Matrix` decomposition (bricks 2–3). This **unconditionally** yields `RegularRepBlockTrace.identityB_conditional`, i.e. Identity (B) general‑n.
- **Status:** future, top of the chain.

## Infra / build notes

- **Universe:** everything stays `k : Type` (universe 0) — Mathlib's Maschke/Wedderburn instances are single‑universe and `Perm (Fin n) : Type 0`. ℚ/ℝ/ℂ are `Type 0`.
- **Olean builds (sandbox):** the Mathlib cache server is firewalled, so any uncached mathlib module is built from the `/tmp` source with lean‑direct `-o --root` (deps‑first). Already built this way: `RepresentationTheory.{Basic,Maschke}` (2 modules), the `SimpleModule.{WedderburnArtin,Isotypic,IsAlgClosed}` cone (9 modules). `Combinatorics/Young/*` likely needs the same. In real CI, `lake exe cache get` supplies all of these.
- **Sorry discipline:** every `sorry` in bricks 2–5 carries a `-- Ref:` citation to one of the keys above (per AGENTS.md §1). These are *proved theorems in the literature*, not conjectures, so they are `theorem … := by sorry  -- Ref: [key]`, never `conjecture`.
- **Wiring:** brick‑1 (sorry‑free) may be wired into the `BraidKnot` umbrella; the sorry‑bearing brick‑2–5 scaffold stays **unwired** until each is discharged, to keep the `lake build QOU` sorry surface honest.

## Honest scale assessment

This is a multi‑month, Mathlib‑contribution‑scale effort (Specht modules + Okounkov–Vershik). It is
tracked here so future sessions / sibling agents can pick up individual bricks. The framework
consequence is modest and should be stated plainly: it makes rigorous one leg (Identity (B)) of
*Identity I*, which is itself a **carried** input to the s5‑so3 keystone — discharging the OV
labelling does not advance the keystone's own assumptions, it removes a conditional from a supporting
lemma.
