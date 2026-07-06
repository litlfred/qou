# VolDensity(K, q₀) — derivation trace (READ-ONLY audit)

**Date:** 2026-06-01
**Branch:** `claude/vol-density-derivation-trace-2026-06-01`
**Scope:** Trace HOW the production `VolDensity(K, q₀)` is derived, where it
connects to the upstream categorical action / Yekutieli non-abelian Stokes
step, and — the payoff — whether the derivation **forces** a per-Wedderburn-block
decomposition `M_λ(K)` or whether `M_λ` would have to be **invented** downstream
(latent-fit risk). No code modified, nothing fitted; this is a citation-backed
read of what `main` actually computes.

---

## TL;DR (the answer up front)

1. **Production `VolDensity(𝓑₃, q₀)` is NOT `τ(tr_M(ρ(𝓑_K)))`.** The paper's
   canonical chain (cheat-sheet step 6→9, `prop:hoefsmit-scattering-pipeline`
   Stage 4) says `m(K) = m_e · Geom(K) · Σ_λ w_λ χ_λ(β)/dim(λ)` — a per-block
   Markov-trace sum times a scalar `Geom(K)`. The production code
   (`_li_2_q_util.vol_density_borromean`, line 210) computes a **different**
   object: `Vol(𝓑₃)/ℏ_q² × linking_weight(q)`, where
   `linking_weight = (3q²+4+3q⁻²)/4 = 5/2 + (3/4)h²`. The per-block Markov-trace
   factor `Σ_λ w_λ χ_λ(𝓑₃)/dim(λ)` **does not appear in the production
   evaluation at all.**

2. **The non-abelian Stokes (Yekutieli) step does NOT enter the compute.**
   `grep -n "Yekutieli\|non-abelian\|Stokes\|holonomy\|surface-ordered" hecke_core.py
   hecke_character_symbolic.py` → **empty**. Yekutieli appears only as (a) a
   *narrative* conditional conjecture (`conj:geom-yekutieli-alignment`,
   axiomatized, not proved), and (b) the explicitly **PURGED / EXPLORATORY**
   `yekutieli_correction_h2` (`_li_2_q_util.py:309`), which production must not
   call. The Hecke quadratic relation `σ_i² = (q−q⁻¹)σ_i + 1` is asserted as a
   Hoefsmit/seminormal datum, not derived from a curvature 2-form anywhere in
   code.

3. **The dimensional bridge (→ MeV) is `m_e` (CAL-1) × a global pure number.**
   `m(K) = m_e · VolDensity(K, q₀)` with `VolDensity` a single scalar
   (`m_p_borromean_verification_50dps.py:193, 313`). The pure number is
   **global, not per-block** in production. There is no per-λ Archimedean
   functor application in the production path.

4. **Φ_q vs Li_2^q:** production `vol_density_borromean` uses **neither** — it is a
   bare algebraic `Vol/ℏ_q² × (3q²+4+3q⁻²)/4`. Li_2^q (`li_2_q`, line 69) is
   reserved for the brane-tower / binding context (correct per cheat-sheet §4);
   Φ_q lives in `_phi_q_util.py` for the mass-anchor context. The baryon
   `VolDensity` path touches no q-dilogarithm.

5. **THE KEY ANSWER — does the derivation force a per-block `M_λ`?**
   **No — not in the production object as currently built.** Production
   `VolDensity` is a global scalar `Vol/ℏ_q² × λ_A(q)` with the per-block
   `χ_λ(𝓑₃)` structure already collapsed away. The ONE thread that connects
   `λ_A` to a per-block sum is `λ_A = (1/4)Σ_{λ⊢4} dim_q V_λ` — but (i) that sum
   is over **partitions of 4 (H₄)**, not the H₃ blocks of the Borromean braid
   `𝓑₃ ∈ B₃`; (ii) the `Σ` is only in the **docstring/comment** — the Lean and
   the production helper hard-code the closed form `(3q²+4+3q⁻²)/4`, never
   iterating blocks; (iii) the link from `λ_A` to the actual Borromean trace
   `tr_M(𝓑₃) = 1+(3/16)h²` is an **empirical `mpmath.identify` coincidence**
   with an unexplained renormalization factor of 4. **Therefore a per-block
   `M_λ(K)` would have to be invented downstream — it is a latent-fit risk, not
   a forced composite.** See "The gap" and "Per-block verdict" below.

---

## 1. Where VolDensity is defined/computed

### Canonical production implementation

`computations/_li_2_q_util.py:210-254` — `vol_density_borromean(q)`:

```python
def vol_density_borromean(q, q_inv=None):
    qi = 1/q if q_inv is None else q_inv
    hbar_q = 1 - qi                      # ℏ_q = (q-1)/q
    vol_b3 = 8 * mp.catalan              # Vol(𝓑₃) = 8·G (Adams 1985)
    geom_leading = vol_b3 / hbar_q ** 2  # bare hyperbolic-volume term
    linking_weight = linking_weight_family_a(q, qi)
    return geom_leading * linking_weight
```

- **Inputs:** `q` (substrate), nothing else. Vol(𝓑₃) is a fixed constant
  `8·Catalan` (Adams 1985).
- **Sequence of operations:** `ℏ_q ← 1−q⁻¹`; `geom_leading ← 8G/ℏ_q²`;
  `linking_weight ← (3q²+4+3q⁻²)/4`; return their **product**.
- **Opaque scalar or per-block?** **OPAQUE SCALAR.** No loop over λ, no character
  evaluation, no Markov-trace call. The function never references `χ_λ`, `y_λ`,
  `dim_q(λ)`, or `θ_λ`. It is two scalars multiplied.

`linking_weight_family_a` (`_li_2_q_util.py:172-197`) likewise returns the
closed form `5/2 + (3/4)·h²` directly — **no `Σ_λ` loop**, despite the docstring
claiming `= (1/4)·Σ_{λ⊢4} dim_q V_λ` (line 184).

### Consumer

`m_p_borromean_verification_50dps.py:192-193`:

```python
from _li_2_q_util import vol_density_borromean as _vol_density_borromean
GEOM_FULL_BORROMEAN = _vol_density_borromean(Q)
```

then `m_avg_pred = GEOM_FULL_BORROMEAN * M_E_CODATA_MEV` (line 313). The
proton/neutron split is applied **afterward** via the substrate flavor-split
`Δm/M_N = ℏ_q²·h_q·[2]_q·(1+ℏ_q³)/3` (line 308) — again a scalar redistribution,
not a per-block decomposition.

### The proof-of-`λ_A` script

`lambda_scale_all_c_i_family_a.py:84-115` is the ONLY place a `Σ_λ` actually
runs. It builds `dim_q_lambdas` for the 5 partitions of 4 (line 92-98):
`{(4):1, (3,1):[3]_q, (2,2):[4]_q/[2]_q, (2,1,1):[3]_q, (1,1,1,1):1}`, sums and
divides by 4 (line 104), then **proves the result collapses to the closed form**
`5/2+(3/4)h²` (line 112-128). So even here, the per-block structure exists only
to be **proved equal to a global polynomial** — it is consumed as a scalar, and
production imports the scalar form, not the sum.

---

## 2. The non-abelian Stokes (Yekutieli) link — WHERE IT IS, AND WHERE IT ISN'T

### Cheat-sheet claim (the narrative ideal)

`docs/canonical-derivation-cheat-sheet.md:40-44` — step 2: "Non-abelian Stokes
(Yekutieli): Hecke quadratic `σ_i² = (q−q⁻¹)σ_i + 1` as curvature 2-form".
Then step 6→9: `tr_M = Σ_λ y_λ χ_λ` → Archimedean functor → MeV. The narrative
chain has `Geom` *downstream* of the per-block trace sum.

### What the compute actually contains

`grep -n "Yekutieli\|non-abelian\|non_abelian\|surface-ordered\|path-ordered\|
holonomy\|Stokes"` over `hecke_core.py` + `hecke_character_symbolic.py` returns
**nothing**. The Hecke relation and Hoefsmit matrices are entered as algebraic
data; there is no curvature-2-form / surface-ordered-exponential derivation in
code. The "non-abelian Stokes → Hecke" arrow is **ASSERTED in narrative**, with
no executable derivation.

### The only Yekutieli code is EXPLORATORY / PURGED

`_li_2_q_util.py:309-332` — `yekutieli_correction_h2` returns `−G·h²` and its own
docstring says: "EXPLORATORY: the unproved −G·h² Yekutieli per-cell curvature
correction… What's unproved is our framework's claim that it yields −G·h²… Use
ONLY for exploratory comparison columns, never in production." The cheat-sheet
(`§5 fix #1`, line 186) and `lambda-scale-absorbed-into-vol-density.md:51` record
that the Yekutieli per-cell route was **briefly in production (a1f68d5e5) then
PURGED (71d674da1)** as non-canonical (bijection NEGATIVE, PR #985).

### How does `tr_M = Σ_λ y_λ χ_λ` become `VolDensity`?

In the paper: `prop:hoefsmit-scattering-pipeline` Stage 3 (`.md:64-80`) and
`prop:geom-universality` property 2 (`geom-universality.md:16-17`):
`Geom(K) = τ(tr_M(ρ(𝓑_K)))`. So narratively `Geom` IS the Archimedean (fibre
functor `τ`) image of the Markov trace — Stage 3 evaluates `τ(J_K)` on the knot
complement `S³∖K`, producing `Vol(K)/ℏ_q²` (hyperbolic) or `CS(K)·ℏ_q²` (torus).

**But** `prop:geom-universality` and `prop:geom-yekutieli-alignment` are BOTH
`conjecture()` blocks (verified: builder = `conjecture(` ×4 across the four
blocks). The Stage-3 "τ evaluates the trace to a geometric volume" step is the
content of `conj:geom-yekutieli-alignment` — **a conjecture, conditional on
`conj:hyperbolic-volume-transcendence` + `rem:baryon-period-ratio`**
(`hoefsmit-scattering-pipeline.md:1-4`, `geom-universality.md:1-4`).

So production **does not** flow `tr_M → τ → Geom`. It **shortcuts** straight to
the τ-image side: it writes `Vol(𝓑₃)/ℏ_q²` directly (the *claimed output* of
Stage 3 for a hyperbolic link) and multiplies by `linking_weight`. The
`Σ_λ w_λ χ_λ(𝓑₃)/dim(λ)` factor that Stage 4 (`.md:86-90`) puts **next to**
`Geom(K)` is silently dropped and replaced by `linking_weight`.

---

## 3. The Archimedean evaluation / dimensional bridge (where MeV appears)

- **Where:** `m_p_borromean_verification_50dps.py:313` —
  `m_avg_pred = GEOM_FULL_BORROMEAN * M_E_CODATA_MEV`. MeV enters solely through
  `m_e` (CAL-1, `codata_constants.M_E_MEV`, line 158-163).
- **What the Archimedean functor does:** in production it does **nothing
  per-block**. The dimensionless `VolDensity(𝓑₃, q₀)` is already a single real
  number (`Vol/ℏ_q² × λ_A` ≈ 1890, witness
  `mass-table-comprehensive.witness.json:1323` `vol_density_borromean_q ≈ 1890.5`),
  and the "Archimedean functor" is the trivial map "multiply by `m_e`". The
  per-block character sum `Σ_λ w_λ χ_λ/dim λ` — the place where a per-block
  `τ` action would live — is absent.
- **Is the pure number per-block or global?** **Global.** This is the crux:
  the cheat-sheet hope ("if the Archimedean functor acts per-block, `M_λ` falls
  out of `VolDensity` directly") is **not realized** in production code, because
  production never carries a per-block object into the Archimedean step — it
  collapsed to a scalar two steps earlier.

---

## 4. Φ_q (Faddeev) vs Li_2^q (Rogers)

- **Production baryon `VolDensity` uses neither.** `vol_density_borromean` and
  `linking_weight_family_a` are pure rational functions of `q`
  (`_li_2_q_util.py:172-254`). No `li_2_q` / `phi_q` call in the baryon path.
- **Li_2^q (`li_2_q`, `_li_2_q_util.py:69-103`)** is the bar-symmetric form, used
  for the **brane-tower / binding** context (`compute_t2_t3_from_vols`, line 128;
  module docstring lines 4-16). This is consistent with the cheat-sheet §4 claim
  that the binding channel uses the bar-symmetric `Li_2^q`.
- **Φ_q (Faddeev)** lives in `_phi_q_util.py` (mass-anchor / bar-asymmetric),
  per the same module docstring (lines 13-15). It is bar-asymmetric and carries
  the dimensional scale.
- **Verdict on the cheat-sheet claim:** correct **for the binding/brane-tower
  channel** — but it is **moot for the production baryon `VolDensity`**, which
  has no dilogarithm at all. So the Φ_q-vs-Li_2^q discipline does not gate the
  production proton-mass number; it only gates the (separate) binding-energy
  compute.

---

## 5. The per-block question (the payoff)

### Does the derivation FORCE `M_λ = m_e · (per-block summand)`?

**In the paper narrative — yes, structurally.** `prop:hoefsmit-scattering-pipeline`
Stage 4 (`.md:86-90`):

```
m(K) = m_e · Geom(K) · Σ_λ w_λ · χ_λ(β)/dim(λ)
```

This DOES present a per-block sum. The natural per-block summand would be:

```
M_λ(K) = m_e · Geom(K) · w_λ · χ_λ(𝓑_K)/dim(λ),
         w_λ = dim_q(λ)² / [k]_q!        (Wedderburn weight, .md:52)
```

i.e. the summand in `{χ_λ(K), dim_q(λ), w_λ}` — `Geom(K)` is the common scalar
prefactor, the per-block content is `w_λ χ_λ(K)/dim λ`. **This is well-defined
mathematically and is the object the paper's chain produces.**

**In the production code — NO, it is not present.** Production `VolDensity`
(`vol_density_borromean`) is `Vol/ℏ_q² × λ_A(q)` and **never computes the
`Σ_λ w_λ χ_λ(𝓑₃)/dim λ` factor.** The proton number comes out as a global
scalar; there is no per-block array anywhere in the production proton path.
A per-block `M_λ` would have to be **re-introduced** by going back to the
narrative Stage-4 form — which the production path abandoned.

### Why this matters for L2 Subgoal-1 (the latent-fit warning)

The cheat-sheet's framing ("`λ_scale` was absorbed into `VolDensity`") is the
mechanism by which the per-block structure was lost: the production object is
`Vol/ℏ_q² × λ_A`, and `λ_A = (3q²+4+3q⁻²)/4` is a **global** H₄ Wedderburn
average, not the H₃ Borromean per-block trace. Consequences:

- `λ_A` sums over **partitions of 4** (`lambda_scale_all_c_i_family_a.py:92`),
  but the Borromean braid `𝓑₃ = (σ₁σ₂⁻¹)³` lives in **B₃ / H₃(q)** (partitions
  of 3). The block index set of `λ_A` is **not the block index set of the knot
  whose mass it scales.** Any `M_λ(𝓑₃)` you build from `λ_A`'s 5 H₄ blocks is
  indexing-mismatched against `𝓑₃`'s 3 H₃ blocks.
- The only bridge offered (`_li_2_q_util.py:335-363`, `borromean_markov_trace_h2`)
  is: `tr_M(𝓑₃) = 1+(3/16)h²`, and `(3/16)×4 = 3/4` = `λ_A`'s h² coefficient.
  The factor **4** is described as "the (n−1)-strand normalization (Jones
  normalization factor 4 = (1+1)² at q=1 for n=3 strands)" — but the h⁰ terms
  do **not** match under the same factor (`1×4 = 4 ≠ 5/2`), so the "match" is
  the **h² coefficient only**, found via `mpmath.identify`. This is an
  **empirical coincidence at one Taylor order**, NOT a derivation. (The
  docstring itself calls it "empirical computation," line 354.)

**So: the per-block decomposition is genuinely NOT present in the production
derivation. Re-deriving `M_λ(K)` to gate L2 Subgoal-1 would mean reconstructing
the paper's Stage-4 `Σ_λ w_λ χ_λ(K)/dim λ` form and re-attaching it to
`Geom(K)` — which is exactly the (correct) categorical object, but it is
currently bypassed in code.** If instead one tries to read `M_λ` out of the
production `λ_A` H₄ sum, the index mismatch + the single-order `mpmath.identify`
coincidence make it a **latent fit**, not a forced composite.

---

## DERIVED vs ASSERTED vs FITTED — per step

| Chain step | Status | Evidence |
|---|---|---|
| Cat action `ρ_n: B_n → Aut(V^⊗n)` | DERIVED (algebraic) | `hecke_core.py` seminormal σ_i; standard Hoefsmit |
| Non-abelian Stokes → Hecke quadratic | **ASSERTED** (narrative only) | grep empty in compute; relation entered as datum, not derived from curvature 2-form |
| `tr_M = Σ_λ y_λ χ_λ` | DERIVED (Wenzl bridge) | `y_lambda_wenzl_bridge.py`; `hoefsmit-scattering-pipeline.md:42-55` |
| `Geom(K) = τ(tr_M(ρ(𝓑_K)))` (functoriality) | **ASSERTED / conjectural** | `prop:geom-universality` is `conjecture()`; Lean `GeomFullFunctorial.functorial := True` (trivial stub, `geom-universality.lean:74-75`) |
| `τ(J_K)` → `Vol(K)/ℏ_q²` (Stage 3) | **ASSERTED / conjectural** | `conj:geom-yekutieli-alignment`, conditional on `conj:hyperbolic-volume-transcendence`; `geom-yekutieli-alignment.lean` is conditional-on-class with `sorry`-class |
| Production `VolDensity = Vol/ℏ_q² × λ_A` | DERIVED-from-ASSERTION | `vol_density_borromean` computes it; but it presupposes the conjectural Stage-3 output `Vol/ℏ_q²` and substitutes `λ_A` for the dropped `Σ_λ w_λ χ_λ` factor |
| `λ_A = (3q²+4+3q⁻²)/4 = (1/4)Σ_{λ⊢4} dim_q V_λ` | DERIVED (Lean-proved) | `lambdaA_all_c_i` proves the closed form; sum is real but over **H₄, not the knot's H₃ blocks** |
| `λ_A` ↔ `tr_M(𝓑₃)` (the `(3/16)×4=3/4` link) | **FITTED / coincidental** | `borromean_markov_trace_h2` docstring: `mpmath.identify`, h²-coefficient-only, unexplained factor 4, "empirical computation" |
| Dimensional bridge `× m_e` | DERIVED (CAL-1) | `m_p_borromean_verification_50dps.py:313`; global scalar, not per-block |
| Per-block `M_λ(K)` | **NOT PRESENT in production** (would be ASSERTED if re-introduced from `λ_A`'s H₄ blocks; DERIVED only if rebuilt from the paper's Stage-4 `Σ_λ w_λ χ_λ(K)/dim λ`) | see §5 |

---

## The gap (most valuable finding)

**The production mass formula and the paper's canonical chain compute different
objects, and the join between them is conjectural + one empirical coincidence.**

- **Paper:** `m(K) = m_e · Geom(K) · Σ_λ w_λ χ_λ(K)/dim λ` — per-block trace sum
  × scalar volume. (`prop:hoefsmit-scattering-pipeline` Stage 4.)
- **Production:** `m(K) = m_e · [Vol(K)/ℏ_q² × λ_A(q)]` — global scalar, with the
  `Σ_λ w_λ χ_λ(K)/dim λ` factor **replaced** by `λ_A(q)` (an H₄ Wedderburn
  average that has the *wrong block index set* for `𝓑₃`).
- **The replacement is justified by:** (i) `prop:geom-universality` property 2,
  which is a **conjecture** with a trivial-`True` Lean functoriality class
  (`geom-universality.lean:74`), plus (ii) the `(3/16)×4 = 3/4` numerical match
  in `borromean_markov_trace_h2`, which is an `mpmath.identify` coincidence at
  the **h² Taylor order only** and does not match at h⁰.

This is precisely the structural reason the +2.89 % m_p gap is "honest, not an
error" (per the `_li_2_q_util.py:248` comment): production is multiplying the
hyperbolic volume by a **global** Wedderburn average rather than by the **knot's
own** per-block Markov-trace content. Closing the gap *categorically* almost
certainly requires reinstating the per-block `Σ_λ w_λ χ_λ(𝓑₃)/dim λ` factor (the
paper's Stage-4 object) in place of the global `λ_A` — i.e. the per-block `M_λ`
the L2-Subgoal-1 work needs is **the same object the production code dropped**,
and it is **forced by the paper chain but absent from the code.**

### Latent-fit risk verdict

`M_λ(K)` is **NOT a forced composite of the current production `VolDensity`** —
production has no per-block structure to read it from. Building `M_λ` by
re-using `λ_A`'s H₄ block sum would be a **latent fit** (index mismatch +
single-Taylor-order coincidence). Building `M_λ` from the paper's Stage-4
`m_e · Geom(K) · w_λ χ_λ(K)/dim λ` is the **derivation-honest** route — but it
requires (a) discharging `conj:geom-yekutieli-alignment` / the trivial-`True`
`GeomFullFunctorial` class, and (b) reconciling the dropped trace factor against
the production `Vol/ℏ_q² × λ_A` value (which currently reproduces ≈1890, the
"1700× scale factor", but only to +2.89 %).

---

## Files cited

- `computations/_li_2_q_util.py` (vol_density_borromean:210,
  linking_weight_family_a:172, li_2_q:69, yekutieli_correction_h2:309,
  borromean_markov_trace_h2:335)
- `computations/m_p_borromean_verification_50dps.py` (193, 313, 158)
- `computations/lambda_scale_all_c_i_family_a.py` (84-128)
- `computations/meson_vol_density.py` (59-62) — same `Vol/ℏ_q² × λ_A` baryon form
- `content/quantum-observable-universe/mass-theory/hoefsmit-scattering-pipeline.md` (Stage 1-4)
- `content/quantum-observable-universe/particle-interactions/geom-universality.md` + `.lean` (74)
- `content/quantum-observable-universe/mass-theory/geom-yekutieli-alignment.{md,lean}`
- `content/quantum-observable-universe/mass-theory/lambda-scale-substrate-form.lean`
- `docs/canonical-derivation-cheat-sheet.md`, `docs/lambda-scale-absorbed-into-vol-density.md`
