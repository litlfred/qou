# Binding active sets are tiny → O(A·few) scaling, not O(p(3A)) (2026-06-10)

**Status:** compute-optimization audit (exploratory; no production rewire
here — this is the *plan* + the measurement). Probe + witness:
[`low_isotopes_binding_sweep.py`](../../computations/low_isotopes_binding_sweep.py)
/ `low-isotopes-binding-sweep.witness.json`.

> ## ⚠ SUPERSEDED IN PART, 2026-09-06 (bean `qou-fq0f`)
>
> **The exact-0 carve-out below is satisfied, and this document's search for it
> looked at the wrong factor.**
>
> The directive admits dropping a partition "only if `χ^λ(β_atom) = 0` is
> provable", and the search for character zeros came back empty. That finding is
> correct and reproduces today: at tritium all **30 of 30** partitions have
> `χ^λ ≠ 0`.
>
> But the summand is `y_λ · χ^λ`, and under production convention **D** it is the
> **weight** that vanishes, not the character. `z = q³/(q²+1)` pins the Wenzl
> level to `Q^r = q⁴ = Q²`, i.e. **r = 2 exactly**, so Wenzl's row cap gives
> `y_λ = 0` identically for every λ with three or more rows
> (`WenzlWeightVanishing.lean`; Orellana, *Crelle* **508** (1999) 157–178, p. 5).
>
> Measured at tritium, n = 9:
>
> | | count |
> |---|---:|
> | partitions with `χ^λ ≠ 0` — this document's search | **30 of 30** |
> | partitions with `y_λ · χ^λ` **exactly** 0 — the droppable set | **25 of 30** |
>
> These are not small terms. `χ_(4,3,2) = 2.384` is the **largest** character
> magnitude at n = 9 and its weight is exactly zero.
>
> This is *more* precise than the active-set truncation rejected below, not less:
> it drops only provable zeros and **keeps** every nonzero term, including
> `[5,4]` (contribution −0.00527) which the "≲ 1 % each" reading would have
> dropped. No tail bound is needed, so the "legitimate truncation path
> (formalize-first)" further down is moot.
>
> **Why this document could not have seen it.** It is dated 2026-06-10; the
> C → D convention migration landed 2026-08-09. Under convention C the level was
> r ≈ 2.5995 — not an integer — and there was **no row cap**, so the ≥3-row tail
> really was nonzero at ~10⁻³–10⁻⁹ as measured here. The reasoning was sound in
> the frame it was written in.
>
> Taken in `tr_m_wenzl_bridge_mpfr` (`_apply_wenzl_row_cap`): 99.5× on the
> five-atom producer, H₁₂ from unreachable to ~17 s, output bit-identical. Not
> yet taken in `tr_m_atom_via_transfer`, which still evaluates all 385 partitions
> at ⁶Li when 10 carry weight.

## FINAL POSITION (owner directive 2026-06-10): NO truncation — only provable exact-0

Truncating nonzero contributions is **rejected** regardless of how small
the tail is — the precision discipline admits dropping a partition **only
if `χ^λ(β_atom) = 0` is provable**. The exact-0 search came back **empty**:
`exact-χ-zeros = 0` on both D and T — every partition has a nonzero
character (the atom braid is a *generic* full-crossing word; no character
selection rule). **Therefore no partitions are droppable, and the binding
sum must run over all `p(3A)` partitions** for 1-ppQ precision.

**Corollary — a current bug:** the matrix-M χ cache uses a `max_dim` cap
that **skips** the high-dim partitions (12/30 for T). Those carry
~10⁻³–10⁻⁹ each, so the cached `tr_M` is itself a **~10⁻³ truncation**,
*not* 1-ppQ-precise. A 1-ppQ binding path must drop the `max_dim` cap and
sum all partitions.

**The only admissible optimization is therefore LOSSLESS:** per-nucleon
H₃-block caching + partition inclusion (#2062 reduced-block) — it computes
**all** `p(3A)` partitions to 50 dps and only reuses cached nucleon blocks,
cutting the per-partition *constant* (no from-scratch seminormal builds,
cross-isotope reuse). It does **not** reduce the partition count `p(3A)`
(that's intrinsic to exact precision). The active-set measurement below is
retained **only as a concentration diagnostic / exploratory tool**, never a
production truncation.

## Measurement — the tr_M active set is 3–4 few-row partitions

From the matrix-M χ caches, ranking partitions by |contribution| to `tr_M`:

| isotope | 3A | p(3A) | partitions for **90%** of tr_M | the active partitions |
|---------|----|-------|-------------------------------|-----------------------|
| D | 6 | 11 | **3** | `[6]`, `[5,1]`, `[4,2]` |
| T | 9 | 30 | **4** | `[8,1]`, `[7,2]`, `[9]`, `[6,3]` |

The active set is the **few-row** family `[n], [n−1,1], [n−2,2], [n−3,3]`.
High-dim deep partitions (`[3,2,1]` dim 16; `[6,3]` dim 48; `[5,4]` dim
42) contribute ≲ 1% each. (The matrix-M `skipped-max-dim` partitions for
T are *exactly* these negligible high-dim ones — they were skipped
because high-dim, and they carry essentially none of the trace.)

## ⚠ PRECISION CAVEAT (correction 2026-06-10) — truncation is NOT free

**The non-active partitions are NOT zero — there is no exact-χ selection
rule** (`exact-χ-zeros: 0` on both D and T; every partition has nonzero
χ^λ). Dropping the few-row tail is therefore **truncation error**, and the
dropped mass is **~9.8×10⁻⁴ (≈10⁻³ relative)** — *far* above the
framework's `_precision` requirement (L1 = 1 ppQ = 10⁻¹⁵, 50 dps). So:

> **The active-set truncation as prototyped is INVALID for production
> precision.** You may truncate *only* if you can **prove** the net tail
> `|Σ_{rows(λ)>R} y_λ χ^λ| < ε` and that `ε < 10⁻¹⁵` — which is NOT
> established (the tail decays slowly: rows-4 ~10⁻⁴, rows-9 ~10⁻⁹, never
> reaching 10⁻¹⁵ for these light isotopes).

**Consequence for the optimization:** the *lossless* part is the
**per-nucleon block caching + partition inclusion** — it computes the
**same** partitions (all of them, to 50 dps) and only reuses cached
nucleon blocks, so it preserves precision exactly. The **truncation**
(dropping partitions) is the precision-violating part and must NOT be
shipped without a proven tail bound. The active-set measurement tells you
*where the physics concentrates* (few-row), and is fine for **exploratory**
work (0.1% tolerable) — but production keeps all partitions and gets its
speedup from caching, not truncation.

**Legitimate truncation path (formalize-first):** prove a bound
`|y_λ χ^λ(β_atom)| ≤ C·q₀^{−c·rows(λ)}` (or similar), then truncate at the
`R` where the geometric tail `< 10⁻¹⁵`. Until that's a theorem, no
truncation.

## Scaling consequence

`p(3A)` explodes: `p(6)=11, p(9)=30, p(12)=77, p(18)=385, p(24)=1575`.
But the binding only needs the **~4 few-row reps**. So:

> **Restrict the binding sum to the few-row active set → O(A·few) per
> isotope, instead of O(p(3A)).**

The dominant cost is building the `dim_V_λ × dim_V_λ` seminormal matrices;
truncating to few-row λ caps `dim_V_λ` to the small irreps and avoids the
high-dim ones entirely (the ones that blow up the wall-clock and the
`skipped-max-dim` cap).

## Caching + partition inclusion — don't recompute per isotope

Current infra (`mass_at_3A_proper`):
- `_cached_seminormal(shape)` — disk cache (`.cache/seminormal/*.npz`)
  keyed on the **global (3A)-shape**. So every new A → new shapes →
  recompute from scratch.
- module-level `BlockCache` (content-distance) + the matrix-M
  **reduced-block μ_p|μ_n kernel** (#2062) — already decomposes χ into
  per-nucleon blocks, but still keys on the global shape.

**The optimization** (the directive's "cache on nucleons + partition
inclusion"): the few-row active partitions have a clean branching
inclusion `few-row(H_{3A}) ↑ few-row(H_{3(A−1)})`, so the **per-nucleon
H₃ block is invariant across isotopes**. Key the cache on the
**per-nucleon block, not the global shape** — exactly #2062's Tier-3
"build the generators directly in the reduced/recursive representation"
so the full `dim_V_λ × dim_V_λ` matrices are never formed. Then:

- nucleon block computed **once**, reused for D, T, ³He, ⁴He, ⁶Li, …;
- new isotope = O(A) block compositions on the few-row active set;
- the `skipped-max-dim` wall disappears (the skipped reps were never
  needed).

## Δ_λ residual — honest negative

The `Δ_λ(K) = B_AME/B_pred ≈ q₀^(10A−5)` near-match (audit
`2026-06-09-delta-lambda-canonical-residual.md`) does **not** have a
clean structural derivation: the obvious quantities (crossing count
23/35/35/47, trace q₀-degree −9/−22/−15/−28, writhe 4/4/8/8) do not
reproduce 15/25/25/35, and ³He deviates 1.40. **Refuted at the
crossing/jet-bookkeeping level** — it stays a loose 4-point near-match,
not a law. (Recorded so it's not chased further as a closure.)

## Next steps

1. **Prototype active-set-truncated binding** — sum `binding_canonical`
   over only the few-row λ; verify it reproduces full `tr_M` to ≥ 99%.
   ✅ **DONE** ([`active_set_truncation_prototype.py`](../../computations/active_set_truncation_prototype.py)):
   `rows(λ) ≤ 3` recovers **99.96% (D) / 99.91% (T)** of `tr_M` — i.e. a
   **~10⁻³ truncation error**, NOT exact. Per the precision caveat above
   this is **invalid at 1 ppQ** and is NOT a shippable truncation; it only
   confirms *where* the trace concentrates (few-row). The valid scaling
   win is the lossless per-nucleon caching (step 2), which keeps all
   partitions.
2. **Per-nucleon block cache** keyed on the H₃ block (not (3A)-shape) +
   few-row branching composition — coordinate with #2062 (reduced-block
   kernel) and #2080 (A≥4 χ). This is what scales binding past ⁴He.
3. Drop the matrix-M `max_dim` cap from the binding path (the capped
   partitions are outside the active set — they were never contributing).
