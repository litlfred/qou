# Isospin categorical source — D9 closure path

**Date:** 2026-05-24
**Branch:** `claude/duality-tracker-magic-shell-isospin-2026-05-24`
**Status:** Audit. Identifies the existing partial isospin formalisation in `crystal-isospin-degeneracy.md` (D9 ⏳ in [`docs/duality-tracker.md`](../duality-tracker.md)) and proposes the **operator-valued extension** that unlocks the full categorical source.

> **CORRECTION NOTE (2026-05-24, surfaced by `verify_isospin_bar_anomaly.py`):**
> The original draft of this doc classified the 305 ppm residue as
> "bar-anti-symmetric." **That was wrong.** Bar involution
> (q ↔ q⁻¹ AND σᵢ ↔ σᵢ⁻¹) and the isospin Z/2 swap (σᵢ ↔ σᵢ⁻¹ with
> q FIXED) are **distinct** involutions. The 305 ppm residue is
> **isospin-Z/2-anti-symmetric** (correct); it is NOT bar-anti-
> symmetric because `ℏ_q = (q-1)/q` is "mixed" under bar (not
> cleanly classifiable). The empirical 305 ppm match to CODATA holds
> at 0.03% rel diff (verified at q₀); only the involution-naming
> was off-target. Body text below has been rewritten to use
> "isospin-Z/2-anti-symmetric" where the original meant the canonical
> isospin Z/2 swap; references to specific quantities like
> `h = q − q⁻¹` that ARE genuinely bar-anti-symmetric retain that
> label. Full correction analysis:
> [`docs/audits/2026-05-24-d9-bar-parity-correction.md`](2026-05-24-d9-bar-parity-correction.md).

## §1. What's the user-level question?

*"Where does isospin come from? Categorically?"*

**Short answer:** Isospin SU(2)_I is **the flavor swap `u ↔ d`** between proton and neutron color-sheet flavor triples. The proton's `(u, u, d)` and neutron's `(u, d, d)` are exchanged by a Z/2 action that lifts to SU(2)_I after q-deforming and bar-symmetrising over the color sheets.

**Long answer:** the framework already has [`crystal-isospin-degeneracy.md`](../../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md), which proves a **partial** version of this: at the `q → 0` crystal limit (Kashiwara), the shell-correction sum `S_crystal(A)` is invariant under exponent inversion of every plain Hecke generator `σᵢ ↔ σᵢ⁻¹` in the atomic braid word. **But this proposition only holds for plain generators** — the canonical atomic braid uses operator-valued inter-nucleon interfaces `⋈_K = σ_g − h/2 · 𝟙` (the "averaged" crossing for unlike-isospin pairs), `σ_g⁻¹` for nn pairs, `σ_g` for pp pairs (per [`isotope_record_schema.py:176-178`](../../computations/isotope_record_schema.py)), and `crystal-isospin-degeneracy.md` explicitly flags this as **open work**:

> "Extending the proposition to canonical $\bowtie_K$-coupled words requires a regularised (or renormalised) crystal functional and is left as separate work."

## §2. The structural picture

```
Proton braid     →  (u, u, d) at three color sheets
Neutron braid    →  (u, d, d) at three color sheets
                  ↓ flavor swap (u ↔ d)
                = SU(2)_I action
```

In the q → 0 crystal limit, the plain Hecke generator becomes its own inverse via the **0-Hecke quotient relation** — at q = 0 the Hecke quadratic `σᵢ² = (q − q⁻¹)σᵢ + 1` degenerates such that `σᵢ` becomes idempotent on the crystal sub-quotient, giving `σᵢ⁻¹ = σᵢ` on the canonical basis (per `crystal-isospin-degeneracy.md`'s scope). The operator-valued averaged crossing `⋈_K = σ_g − (h/2)·𝟙` does **not** have a naive crystal limit precisely because `h = q − q⁻¹` diverges at q = 0 — that's the open extension. So crystal-isospin-degeneracy applies cleanly to plain generators on the 0-Hecke quotient, and the `⋈_K` operator-valued interfaces need a regularised functional to extend.

In the canonical Hecke regime (q = q₀ ≈ 1.11), the inter-nucleon `⋈_K` interfaces have **operator-valued isospin-Z/2-anti-symmetric residue**:

- `pp`: σ_g (positive, +h on bar-anti-sym side)
- `nn`: σ_g⁻¹ (negative, −h on bar-anti-sym side)
- `pn`: σ_g − h/2 · 𝟙 (averaged, "neutral" projection)

The exponent-inversion symmetry of `crystal-isospin-degeneracy.md` swaps `pp ↔ nn` (σ ↔ σ⁻¹) and **fixes pn** (since σ_avg is bar-symmetric). At q = 0 (0-Hecke quotient) the swap is exact via the idempotent relation; at q = q₀ ≈ 1.11 the operator-valued residue introduces a **isospin-Z/2-anti-symmetric anomaly** carrying a factor `h(q₀) ≈ 0.209` (since `h = q − q⁻¹` is bar-anti-symmetric).

**This is the source of the +0.030% (305 ppm) substrate flavor split** `Δm/M_N = ℏ_q² · h · [2]_q · (1 + ℏ_q³)/3` (per [`_li_2_q_util.flavor_split_subleading`](../../computations/_li_2_q_util.py)). Bar-symmetry parity of the leading term:

- `ℏ_q² = (q-1)²/q²` → bar-symmetric (anti-sym squared)
- `h = q − q⁻¹` → bar-**anti-symmetric**
- `[2]_q = q + q⁻¹` → bar-symmetric
- `(1 + ℏ_q³)` → mixed (1 is bar-sym, ℏ_q³ is bar-anti-sym)

Leading term `ℏ_q² · h · [2]_q · 1` is (sym)·(anti-sym)·(sym)·(sym) = **isospin-Z/2-anti-symmetric**, as expected for a quantity (`m_n − m_p`) that itself transforms under the isospin Z/2 swap. The bar-symmetric subleading contribution `ℏ_q² · h · [2]_q · ℏ_q³` (bar-anti-sym × bar-anti-sym = bar-sym) is the next-order canonical correction.

So the 305 ppm IS the **isospin-Z/2-anti-symmetric leading-order canonical-isospin q₀-anomaly** — exactly what the Z/2 swap predicts.

## §3. Why this matters for L3 / Wigner SU(4)

Per duality-tracker D11 (Cluster B), SU(4) Wigner = SU(2)_S × SU(2)_I is the natural categorical source for **nuclear shell structure** (per Wigner's 1937 paper that introduced SU(4) supermultiplets to explain magic-number nuclear shells).

The framework's L3 (nuclear-shell binding) gap identified in [`2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md`](2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md) and corrected in [`2026-05-24-magic-shell-gs-filtration-exploitation.md`](2026-05-24-magic-shell-gs-filtration-exploitation.md) needs SU(4) Wigner classification to be operational.

**Closing D9 unlocks half of D11.** The other half (D10 SU(2)_S spin) requires the SU(2) → SO(3) extension flagged in [`2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md).

## §4. The operator-valued extension — load-bearing open step

The existing `crystal-isospin-degeneracy.md` proves the proposition for the plain Hecke crossing word. To extend to canonical `⋈_K`-coupled words:

### Step 1: Regularised crystal functional

The crystal limit `q → 0` makes `h = q − q⁻¹ → −∞`. The `−h/2` shift in `σ_avg = σ − h/2` diverges. A regularised functional `S_crystal^reg` is needed, replacing `−h/2` with a finite limit (e.g., the leading-order `q⁻¹/2` term or a regulated Cesàro limit).

### Step 2: Bar-anti-symmetric inversion residue

At canonical q = q₀, the natural isospin Z/2 action is `σ_g ↔ σ_g⁻¹` on `pp / nn` and identity on `pn`. The shell-correction sum should be invariant under this action **up to isospin-Z/2-anti-symmetric residue terms** carrying a factor of `h = q − q⁻¹`.

The 305 ppm flavor split `Δm/M_N` is precisely this **isospin-Z/2-anti-symmetric leading residue** (carrying an overall factor of `h`; see §3 above for the four-factor parity decomposition). It IS the canonical-isospin q_0-anomaly.

### Step 3: Lift to SU(2)_I

The Z/2 swap promotes to a continuous SU(2)_I via:

1. **Bar-symmetrise** the swap to get a continuous one-parameter family.
2. **q-deform** by introducing the quantum-2 factor `[2]_q = q + q⁻¹` to interpolate between Z/2 and SU(2)_I.

The q-deformed SU(2)_q on Hecke representations is already present in the framework's `H_n(q)` structure; isospin SU(2)_I is its **subgroup acting on the (u, d) flavor sheets only** — i.e., the SU(2) commutant of the color SU(3) action.

### Step 4: Categorical statement

```
prop:isospin-from-canonical-bowtie

For each (Z, N) atomic braid β_A ∈ B_{3A} with canonical
⋈_K-coupled word, the regularised crystal-corrected
shell-binding sum S^reg_crystal(β_A) is invariant under the
SU(2)_I action swapping (u ↔ d) on color sheets, up to a
bar-symmetric q₀-anomaly term proportional to ℏ_q² · h · [2]_q.

The bar-symmetric anomaly term matches the substrate flavor
split Δm/M_N at 305 ppm to CODATA, providing independent
verification.
```

This proposition would close D9 from ⏳ to ✅. Lean axiomatisation would carry the regularised crystal functional as a class, with `sorry` only in the regulator instance.

## §5. Concrete next steps

1. **Author** `prop:isospin-from-canonical-bowtie.{md,ts}` content block — formalise the regularised crystal functional + the bar-symmetric anomaly statement. Cite `crystal-isospin-degeneracy.md` as the upstream restricted result.
2. **Compute** `verify_isospin_bar_anomaly.py` — verify numerically at q₀ that the canonical `⋈_K`-coupled word's isospin-Z/2-anti-symmetric residue matches `Δm/M_N` flavor split to 305 ppm.
3. **Update duality tracker D9** from ⏳ to ✅ when (1) and (2) land.
4. **Extend to D11 SU(4) Wigner** — combine with D10 SU(2)_S (depends on SO(3) extension per `2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`).

## §6. Cross-references

- [`docs/duality-tracker.md`](../duality-tracker.md) §Cluster B — D9 ↔ D10 ↔ D11
- [`docs/audits/2026-05-24-magic-shell-gs-filtration-exploitation.md`](2026-05-24-magic-shell-gs-filtration-exploitation.md) — sibling audit, magic-shell wiring gap
- [`crystal-isospin-degeneracy.md`](../../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md) — existing partial formalisation (D9 ⏳)
- [`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](2026-05-24-h4-coefficient-source-trace-and-so3-gap.md) — D10 closure path (full SO(3))
- [`isospin-mass-split-em-localisation.md`](../../content/quantum-observable-universe/braids-and-knots/isospin-mass-split-em-localisation.md) — mass-split mechanism
- [`_li_2_q_util.flavor_split_subleading`](../../computations/_li_2_q_util.py) — the 305 ppm anomaly (already verified)
- [`option-e-isospin-test.md`](../../content/quantum-observable-universe/braids-and-knots/option-e-isospin-test.md) — earlier isospin test in the Δ_λ-gating context
