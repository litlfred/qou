# VolDensity compute-vs-paper audit — order-by-order, RAW numbers

**Date:** 2026-06-01
**Branch:** `claude/vol-density-compute-vs-paper-audit-2026-06-01` (PR #1613)
**Scope:** AUDIT ONLY. Does production `VolDensity(𝓑₃,q₀)` match the paper's
forced per-block form? No fitting, no tuning to m_p/B_AME. Every number below
is a RAW computed value, reported whether it matches or not.
**Compute:** [`vol_density_compute_vs_paper_audit.py`](../../computations/audits/vol_density_compute_vs_paper_audit.py),
witness [`vol-density-compute-vs-paper-audit.witness.json`](../../computations/audits/vol-density-compute-vs-paper-audit.witness.json).
Cross-checked against the Rust-computed 50-dps witness
`borromean-markov-trace-h-expansion-50dps.witness.json`.

This audit builds on the read-only structural trace
[`2026-06-01-vol-density-derivation-trace.md`](2026-06-01-vol-density-derivation-trace.md)
(sibling branch) and adds the missing piece: the **actual order-by-order
numerical comparison** of the paper's `Σ_λ w_λ χ_λ(𝓑₃)/dim λ` against
production's `linking_weight`, the mass-bridge propagation of both, and the
quantified answer to "how much of the +2.89% does restoring the per-block sum
recover?".

**Prior art consulted (corpus-grep checklist, AGENTS.md):** the H₄ index choice
is already documented — `lambda-scale-substrate-form.md` records
`λ_A = (1/4)Σ_{λ⊢4} dim_q V_λ` as a **"PSLQ-style empirical fit (no categorical
derivation)" / acknowledged-CAL-4**, falsified as a categorical derivation by
**eight independent structural searches**. The per-block χ_λ single-block-vs-
multi-block divergence is flagged in
[`2026-05-25-vol-density-derivation-error-localization-and-klr-path.md`](2026-05-25-vol-density-derivation-error-localization-and-klr-path.md).
This audit therefore does **not** declare new "open math"; it supplies the
**numerical proof** of what those docs assert, plus one finding they do not
state (§4: the paper's literal per-block factor makes m_p *worse*, not better).

---

## TL;DR

1. **Production `VolDensity` does NOT match the paper's per-block sum — at any
   order, in any normalization.** Production: `linking_weight(q) =
   (3q²+4+3q⁻²)/4 = 5/2 + (3/4)h²` (h⁰ = **2.5**, h² = **0.75**, terminates).
   Paper's per-block factor `J_{𝓑₃}(q) = Σ_{λ⊢3} w_λ χ_λ(β)/dim λ` is a
   *normalized Markov trace* ≈ **1** (h⁰ = 1; an h⁴, h⁶, … tail that does NOT
   terminate). Different objects, different leading terms.

2. **The owner is right on all three counts.** (a) It IS a single opaque
   scalar — production never iterates Wedderburn blocks. (b) `linking_weight`
   is NOT per-knot and NOT per-block; it is a fixed rational in `q`, and the
   same 𝓑₃-derived scalar is applied to *every nucleus* in
   `mass_table_comprehensive.py` (FINDING-2). (c) Compute does NOT match paper.

3. **The H₃-vs-H₄ index mismatch is real but is a *known, documented*
   property, not a hidden bug.** The Borromean braid `(σ₁σ₂⁻¹)³` lives in
   **B₃ / H₃(q)** (`knot_braid_database.py:134` `"Borromean": 3`), so its
   per-block sum runs over the 3 partitions of 3. `linking_weight_family_a =
   (1/4)Σ_{λ⊢4} dim_q V_λ` sums over the 5 **partitions of 4 (H₄)**
   (`lambda_scale_all_c_i_family_a.py:92-104`). But `λ_A` is **not trying** to
   be the Borromean trace — `lambda-scale-substrate-form.md` records it as an
   independent CAL-4 empirical near-match. So the right statement is:
   **production's mass factor is an H₄ empirical fit that does not index the
   knot's braid, by acknowledged design — not the paper's H₃ Stage-4 trace.**

4. **The "factor of 4" is a single-coefficient coincidence, not a
   renormalization** (§3). It appears only in the *Jones* normalization, only
   at h². It fails at h⁰ (ratio 5/2, not 4) and at h⁴ (production = 0, Jones ≈
   −0.758).

5. **Restoring the paper's literal per-block sum makes m_p WORSE, by ~20×**
   (§4 — the one finding not already in the corpus). `J_{𝓑₃}(q₀) ≈ 0.9986`
   (≈ unknot value), so `m_e·Vol/ℏ_q²·J ≈ 381 MeV` (−59.4% vs CODATA m_avg)
   versus production's 966.05 MeV (+2.89%). **The +2.89% gap is NOT the dropped
   per-block factor.** It is the residual between Family A's H₄ average (2.533)
   and the CAL-4 empirical target (2.460).

---

## 0. The two objects, side by side

### Paper (prop:hoefsmit-scattering-pipeline Stage 4, `.md:86-90`)

```
m(K) = m_e · Geom(K) · Σ_λ w_λ · χ_λ(β)/dim(λ)
     = m_e · [Vol(K)/ℏ_q²] · J_K(q)
```

`Geom(K) = Vol(K)/ℏ_q²` is the bare hyperbolic-volume factor (Stage 3,
`.md:77-80`); `J_K(q) = Σ_λ w_λ χ_λ(β)/dim(λ)` is the normalized Markov trace
(`w_λ = dim_q(λ)²/[k]_q!`, `.md:52`) = what `markov_trace_for_knot("Borromean",
q, "wenzl")` computes.

### Production (`_li_2_q_util.vol_density_borromean`, line 210-254)

```
VolDensity(𝓑₃,q) = [Vol(𝓑₃)/ℏ_q²] · linking_weight(q),
linking_weight(q) = (3q²+4+3q⁻²)/4 = 5/2 + (3/4)h²   (line 172-197)
```

`J_K(q)` is **replaced by** `linking_weight(q)`, an H₄ quantum-dimension
average. No loop over λ, no character `χ_λ(β)`, no Markov trace.

---

## 1. Order-by-order h-expansion (RAW, 60-dps Vandermonde fit; h = q − q⁻¹)

Three forms of the Borromean per-block factor, because the paper's `J_K` is
normalization-sensitive and the code carries three conventions:

| h^k | **paper J (wenzl)** `markov_trace_for_knot` | **paper J (jones)** Jones/(√q+√q⁻¹)² | **production lw** Family A (H₄) |
|-----|---:|---:|---:|
| h⁰ | **0.99999999999** | **0.99999999999** | **2.5** |
| h² | **4.59e-9** (≈ 0) | **0.18750** (= 3/16) | **0.75** |
| h⁴ | −0.75000 | −0.75781 | ≈ 0 (terminates) |
| h⁶ | −0.062476 | −0.20239 | ≈ 0 |
| h⁸ | +0.015122 | +0.0095409 | ≈ 0 |

(wenzl column matches the Rust 50-dps witness `actual_h_coefficients_wenzl_jm`:
a₀ = 0.99999998934, a₂ = 0.0003284, a₄ = −0.808, a₆ = −1.394 — the witness's
a₂ is wider-sample fit-noise; the closed form `(4+h²−3h⁴−h⁶)/(h²+4)` gives a₂
= 4.6e-9, i.e. structurally ≈ 0.)

**Reading:**
- In the **wenzl** convention — the one `markov_trace_for_knot` actually uses
  for the mass formula (`markov_trace_for_knot.py:30`) — `J_{𝓑₃}` is
  `1 + 0·h² − 0.75h⁴ − …`: h⁰ = **1** (not 2.5), h² = **≈ 0** (not 0.75).
  Production's `lw / J_wenzl` ratio is 2.5 at h⁰ and **1.6×10⁸** at h².
- In the **jones** convention (`borromean_markov_trace_h2`, line 335) h⁰ = 1,
  h² = 3/16 — the only convention where "(3/16)·4 = 3/4" makes sense.

---

## 2. The owner's three questions — verdicts

### Q1. Why a single opaque scalar?

**Because production short-circuits the categorical chain.** The paper chain is
`ρ_λ → tr_M → Σ_λ w_λ χ_λ/dim λ → τ → Geom`. Production never carries a
per-block array: it writes the *claimed Stage-3 output* `Vol(𝓑₃)/ℏ_q²`
directly, then multiplies by `linking_weight`. The collapse happened in
`lambda_scale_all_c_i_family_a.py`, where `(1/4)Σ_{λ⊢4} dim_q V_λ = 5/2 +
(3/4)h²` was **proved as an identity** and the closed scalar hard-coded. The
identity is real (Lean-checkable); but it is a sum of **quantum dimensions**,
not the paper's `w_λ χ_λ(β)/dim λ` (which carries the braid character), and it
indexes **H₄, not the H₃ braid**. Status of the substitution: ASSERTED
(acknowledged CAL-4), not DERIVED.

### Q2. Is `linking_weight` wrongly non-per-knot?

**YES** — it is a fixed rational in `q` with no knot argument, the **𝓑₃-specific
H₄ average applied universally**:

- `mass_table_comprehensive.py:206` calls `vol_density_borromean(q)` for **every
  nucleus `(Z,N)`**, then `m_avg = m_e·vol_density` (line 208), redistributing
  via the flavor split. The **same 𝓑₃-collapsed scalar is the per-nucleon
  factor for the deuteron (6₂ braid), ⁴He (4·𝓑₃ tower), and every heavier
  isotope** — none of which is the bare Borromean rings. (FINDING-2.)
- The muon (4₁) path (`derive_m_baryon_volume_form.py:113`) correctly uses
  `Vol(4₁)/ℏ_q²` with linking_weight = **1** (it's a knot) and hits m_μ/m_e to
  0.05 ppb. So the framework *knows* linking_weight is per-knot in principle
  (1 for knots, >1 for links) — yet hard-codes the single 𝓑₃ value for all
  baryonic matter.

### Q3. Does compute match paper?

**NO.** At no order, in no normalization, does `linking_weight = 5/2+(3/4)h²`
equal `J_{𝓑₃}(q) = Σ_{λ⊢3} w_λ χ_λ(β)/dim λ`: wenzl 2.5 vs 1.0 leading; jones
ratios 5/2 (h⁰) and 4 (h²) are two different factors → not even a scalar
multiple; h⁴ diverges (production terminates, the true trace does not).

---

## 3. The factor-of-4 + h⁰-mismatch resolution

| coeff | production lw | jones J | ratio prod/jones |
|-------|---:|---:|---:|
| h⁰ | 2.5 | 1.0 | **2.50000** |
| h² | 0.75 | 0.18750 | **4.00000** |
| h⁴ | ≈ 0 | −0.75781 | ≈ 0 |

- The **factor of 4** is real but is the **h²-coefficient ratio only**:
  `0.18750 × 4 = 0.75000` (MATCH) — the "(n−1)-strand Jones normalization 4 =
  (1+1)²" of `borromean_markov_trace_h2`'s docstring (line 346-352).
- The **h⁰ does NOT match under that same factor**: `1.0 × 4 = 4 ≠ 2.5`. The
  h⁰ ratio is **5/2** (Family A's leading coefficient = H₄ partition count /4).
  So production agrees with the Jones trace at h⁰ with factor 5/2 and at h²
  with factor 4 — **two incompatible factors**, i.e. NOT a renormalization.
- **h⁴ is the smoking gun:** production terminates (c₄ = 0, Lean-proved); the
  actual Markov trace has a₄ ≈ −0.758. Even granting the h² coincidence, the
  series part company at the next order.

**Resolution:** the factor-of-4 and the h⁰ mismatch are the *same phenomenon*:
`linking_weight` is NOT a normalization of the Borromean trace. It agrees with
the Jones-normalized trace at exactly one Taylor coefficient (h²), under a
factor (4) that fails at h⁰ (5/2) and h⁴ (0 vs −0.758). A one-order
`mpmath.identify` coincidence documented in the code as if structural.

---

## 4. Does it match the +2.89% m_p gap? — RAW mass-bridge propagation

Inputs (60 dps): `q₀ = 1.10997858…`, `m_e = 0.51099895` MeV, `m_avg^CODATA =
938.91875` MeV, `Vol(𝓑₃)/ℏ_q² = 746.418`.

| factor | value at q₀ | m_avg = m_e·Vol/ℏ_q²·factor | gap vs CODATA |
|--------|---:|---:|---:|
| production `linking_weight` | **2.53278** | **966.050 MeV** | **+2.8896 %** |
| paper `J_{𝓑₃}` (wenzl) | **0.998562** | **380.870 MeV** | **−59.435 %** |

- **Fraction of the +2.89% gap recovered by restoring the per-block sum:
  −1957 %** (catastrophically negative — restoring the literal per-block factor
  blows the gap up ~20×).
- The empirical target production is implicitly chasing is
  `linking_weight^target = (m_p/m_e)/(Vol/ℏ_q²) ≈ 2.460`
  (`derive_m_baryon_volume_form.py:130` — a CODATA-divided AUDIT_ONLY number).
  Family A gives 2.533 = **+2.89% above 2.460** — that IS the gap.

**Conclusion:** the +2.89% gap is **not** the dropped per-block factor, the h⁰
mismatch, or the factor of 4. It is the residual between the H₄ Wedderburn
average (2.533) and the CAL-4 empirical target (2.460), exactly as
`lambda-scale-substrate-form.md` records (Family A's `+3/4 h²` vs the empirical
`−G h²`). **The paper's literal Stage-4 per-block factor (≈ 1 for the Borromean
rings) cannot close it — it would open a −59% gap.** This is the audit's one
finding beyond the existing corpus: it rules out "just restore the per-block
sum" as a fix direction.

---

## 5. Lean status

Lean toolchain not installed in this environment (`lean_status` mode: none) —
diagnostics are **compile-pending**; findings below are from source inspection.

- **`conj:geom-yekutieli-alignment` is a dressed-up tautology, not a literal
  `:= True`.** The theorem actually proven
  (`geom-yekutieli-alignment.lean:61-66`, `geom_yekutieli_alignment_conditional`)
  reduces to `frobenius_self_pairing_unitary`: `(vol/ℏ²)·(ℏ²/vol) = 1` — a
  `field_simp; ring` tautology that says nothing about `τ(J_K) = Vol(K)/ℏ_q²`.
- The conditional classes it depends on are **vacuous**
  (`ConditionalClasses.lean:36-71`): `SingleVolumeIrrational.pairing_unitary`
  is again `(vol/ℏ²)·(ℏ²/vol)=1`; `PLCorrectnessHypotheses.pl_decomposition_lower_bound`
  is `∀ q>1, 0 ≤ 0`. Both discharge with `field_simp` / `le_refl 0`. The
  audit-stub `HyperbolicVolumeIndependence.holds : True` (line 86) is literal.
- **`GeomFullFunctorial.functorial : True`** (`geom-universality.lean:74-75`) —
  the per-knot functoriality that would *justify* collapsing the per-block sum
  to a scalar `Geom(K)` is a literal `True` stub; the docstring (line 70)
  admits "**Open math.** Closing this class to a Lean-witnessed [proof]…".

**What the real statement would be:** the Stage-3 claim
`τ(J_K) = (Σ_λ w_λ χ_λ(β)/dim λ) · Vol(K)/ℏ_q²` (`.md:70-75`) asserts the
fibre functor `τ` factors the Jones polynomial into a geometric volume times
the algebraic trace. A real Lean theorem needs: (i) `τ` as an actual functor
(not the identity-on-scalars it currently is), (ii) the rigid-dualizing-complex
pairing computing `Vol(K)` (currently Adams 1985, no Lean), (iii) the
factorization. None exist; the chain is a tautology with the content
axiomatised away.

---

## 6. DERIVED / ASSERTED / FITTED / BUG — per step

| Step | Status | Evidence |
|------|--------|----------|
| `J_K(q) = Σ_λ w_λ χ_λ(β)/dim λ` (paper Stage 4) | DERIVED | `markov_trace_for_knot`, Wenzl bridge |
| `J_{𝓑₃}(q₀) ≈ 0.9986` (wenzl) | DERIVED (RAW) | this audit; `(4+h²−3h⁴−h⁶)/(h²+4)` |
| `linking_weight = (1/4)Σ_{λ⊢4} dim_q V_λ = 5/2+(3/4)h²` | DERIVED-as-identity | `lambda_scale_all_c_i_family_a.py`, Lean-proved |
| `linking_weight` substituted for `J_{𝓑₃}` in the mass formula | **ASSERTED / acknowledged CAL-4** | `lambda-scale-substrate-form.md`; different object, different index set, different leading term |
| H₄ index set for an H₃ braid | **ASSERTED (documented), not the paper's H₃ trace** | `lambda_scale…:92` (λ⊢4) vs `knot_braid_database:134` (n=3) |
| `(3/16)·4 = 3/4` Family-A↔trace link | **FITTED / coincidental** | h²-only; h⁰ ratio 5/2, h⁴ diverges |
| same 𝓑₃ scalar applied to all nuclei | **(non-per-knot) — see FINDING-2** | `mass_table_comprehensive.py:206` |
| `Geom(K) = τ(tr_M)` functoriality | **ASSERTED** (`:= True`) | `geom-universality.lean:74` |
| `τ(J_K) → Vol(K)/ℏ_q²` (Stage 3) | **ASSERTED** (tautology) | `geom-yekutieli-alignment.lean:61`; vacuous classes |
| `× m_e` dimensional bridge | DERIVED (CAL-1) | `m_p_borromean_verification_50dps.py:313` |
| +2.89% gap = Family A 2.533 vs empirical 2.460 | DERIVED (RAW) | this audit §4; corroborates `lambda-scale-substrate-form.md` |

---

## 7. FINDINGS (ranked) with concrete next-steps

> These are **findings**, not newly-discovered bugs: the H₄ index mismatch and
> the per-block single-vs-multi-block divergence are documented in the corpus
> (`lambda-scale-substrate-form.md`, `2026-05-25-vol-density-derivation-error-
> localization`). The ranking is by decision-relevance for the owner.

### FINDING-1 — the per-block restore direction is RULED OUT (HIGH, new)

The paper's literal Stage-4 factor `J_{𝓑₃} ≈ 1` gives m_avg = 381 MeV (−59%).
"Restore the dropped `Σ_λ w_λ χ_λ/dim λ`" is therefore **not** a viable fix —
it makes m_p ~20× worse. **Next-step:** stop framing the +2.89% as "the dropped
per-block sum"; it is the Family-A-2.533-vs-empirical-2.460 residual (already
the canonical framing in `lambda-scale-absorbed-into-vol-density.md`). This audit
supplies the number that closes the "what if we just restore it?" question.

### FINDING-2 — single 𝓑₃ scalar applied to all nuclei (MEDIUM, actionable)

`mass_table_comprehensive.py:206` applies `vol_density_borromean(q)` (a
𝓑₃-specific scalar) to every `(Z,N)`, including the deuteron (6₂ braid) and
⁴He (4·𝓑₃ tower). Each isotope has its own braid and should get its own
per-knot `VolDensity(K)`. **Next-step:** a `vol_density_for_knot(K, q) =
Vol(K)/ℏ_q² × <per-knot factor>(K, q)`. (Blocked on the open question of what
the per-knot factor IS — FINDING-1 shows the naive Markov trace ≈ 1 is wrong,
so this is the per-isotope Borromean-tower extension already on the L2
Subgoal-1 path, not a quick fix.)

### FINDING-3 — `linking_weight` docstring overstates the link to the trace (LOW, doc)

`_li_2_q_util.py:184` claims `linking_weight = (1/4)Σ_{λ⊢4} dim_q V_λ` is "the
linking-weight component of `VolDensity(𝓑₃)`". It is a sum of **quantum
dimensions** (a CAL-4 empirical near-match), not the paper's Stage-4
`w_λ χ_λ(β)/dim λ` trace factor (h²-coincident only). `borromean_markov_trace_h2`
(line 335-363) similarly presents "(3/16)·4 = 3/4 … establishing that Family A's
λ_A IS the Borromean braid trace" — the audit shows this holds at **h² only**.
**Next-step (this PR, doc-only):** soften both docstrings to "h²-coincident
empirical near-match (CAL-4), not a normalization of the trace — see this
audit", cross-linking `lambda-scale-substrate-form.md`. No production-math change.

### FINDING-4 — Geom-Yekutieli Lean is a tautology (LOW, formalization debt)

`geom_yekutieli_alignment_conditional` proves only `(vol/ℏ²)·(ℏ²/vol)=1`; the
conditional classes are vacuous (`0 ≤ 0`, `True`); `GeomFullFunctorial.functorial
:= True`. The Stage-3 volume-evaluation has zero Lean content. **Next-step
(long-term):** state the real `τ(J_K) = Σ_λ w_λ χ_λ/dim λ · Vol(K)/ℏ_q²`
theorem with a non-trivial `τ`. Out of scope for this audit.

---

## 8. What this audit does NOT claim

- It does **not** claim Family A's H₄ identity is wrong *as an identity* — it
  is Lean-proved. The claim is narrower: it is not the paper's Stage-4 per-block
  trace factor.
- It does **not** propose a fix that recovers the +2.89% (no fit). The honest
  RAW finding is that the paper's literal per-block factor makes m_p worse.
- It does **not** re-open the "derive λ_scale" frame — per
  `lambda-scale-absorbed-into-vol-density.md`, the residual is the
  categorical-exactness refinement of `VolDensity(𝓑₃)`, an acknowledged R&D gap.
- It does **not** touch the muon path (correct) or the binding/brane-tower
  Li_2^q path (separate; Φ_q-vs-Li_2^q discipline applies there, not here).

**Single most decision-relevant output:** the +2.89% gap is the
Family-A-2.533-vs-empirical-2.460 residual; restoring the paper's literal
Stage-4 per-block factor (≈ 1) would open a −59% gap, so that fix direction is
ruled out. The actionable items are FINDING-2 (per-knot Geom, on the existing
L2 Subgoal-1 tower path) and the doc softening in FINDING-3 (this PR).
