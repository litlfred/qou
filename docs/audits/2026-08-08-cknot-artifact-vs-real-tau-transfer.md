# Deuteron `C_knot = 5.853`: normalization ARTIFACT, not a missing many-body magnitude — the τ-transfer test

**Date:** 2026-08-08 · **Branch:** `claude/cknot-artifact-vs-real-tau-transfer-2026-08-08` · **PR:** #4804
· **Beans:** `qou-1h3n` (verdict), `qou-u8w5` (deuteron 5.853), `qou-e84e` (proved-value witness)
· **Axis:** Δ_λ / `C_knot` magnitude · **Tier:** fibre→archimedean τ-transfer decomposition;
derive-then-check; **scope-(a) artifact verdict; no fit; B_AME diagnostic-only, never inverted;
nothing wired.**

## 0. BLUF — the decisive verdict

**The deuteron `C_knot = 5.853` is a master-formula NORMALIZATION ARTIFACT, not a real missing
many-body magnitude.** It is the ratio between two different q₀-geometric normalizations of the *same*
deuteron binding, in which the electron-mass scale `m_e` **cancels exactly**, the bulk is supplied by
the counit per-crossing scale `1/h ≈ 4.78`, and no dynamical many-body (handle-commutator) term appears
anywhere. Therefore **the H₆-interface handle-commutator many-body-magnitude program — insofar as it
targets the deuteron 5.853 — is bookkeeping, not physics.** This is a scope win: that hard construction
is *not warranted* for the deuteron.

**Scope boundary (honest, NOT over-claimed):** this settles the **deuteron `C_knot` only**. The **A≥3
chain extensivity term** (the 12.72× A-growth; the intensive-vs-extensive proof + the pairwise-cap
`ρ_A ≤ C(A,2)` proof, `2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md` §4) is a
**separate, proved-real, still-open** object and is **not** dissolved by this verdict.

## 1. The two routes to `B(deuteron)` in the corpus

| Route | Formula | Scale | Value | vs AME (2.22457) |
|---|---|---|---|---|
| **A** — categorical master (first-order) | `B_A = m_e·\|Σ_λ y_λ χ^λ sgn f^λ\| = m_e·\|S(D)\|`, `\|S\|=0.7438` (#4543) | `m_e` | 0.38008 MeV | **`C_knot = 5.853×` deficit** |
| **B** — fibre rotational tier tower (parameter-free) | `μ₀·ℏ_q·[3]_q[4]_q → E⁺ = ·/(1−t) → ·(1+h²)` | `μ₀` | 2.22376 MeV | **−0.036%** |

Route B's scale is **derived, 0 free params**: `μ₀ = m_e/(3(q−q⁻¹)/2) ≈ 1.6295 MeV` — the per-crossing
MeV scale whose source is the **counit skein** `(q−q⁻¹)` (cheat-sheet L213/237; `eunit-counit-mu0`
tracing). Route B closes the deuteron to **360 ppm from q₀ alone**, no fit (`g2-frame-artifact`,
`deuteron_g2_frame_artifact_probe.py`). Verified this branch: `μ₀ = 1.6295104`, and
`μ₀·ℏ_q·[3]_q[4]_q = 2.0195829` (j = n/2 = 3) reproducing the committed `E_rot` to 2·10⁻⁶ %.

## 2. The τ-transfer — the decisive substitution (exact, 0-fit)

Both routes claim `B(deuteron)`. Since Route B closes it parameter-free, `C_knot = B_AME/B_A = E₂/B_A`.
Substitute the **derived** `μ₀ = m_e·2/(3h)` (with `h = q−q⁻¹`) into the tier-0 ratio:

```
E_rot/B_A = [ m_e·(2/(3h))·ℏ_q·[3]_q[4]_q ] / [ m_e·|S| ]
          = (2/(3h))·ℏ_q·[3]_q[4]_q / |S|        ←  the m_e CANCELS EXACTLY.
```

`C_knot` is therefore **not** an electron-mass magnitude — it is a **pure q₀-geometry ratio** of two
normalizations: the counit-scaled rotational band (numerator) over the `m_e`-scaled signed-character
sum (denominator). Measured exactly (probe, mpmath 50 dps):

| quantity | value |
|---|---|
| `C_knot = B_AME/B_A` | 5.85287 |
| numeric `E_rot/(m_e·\|S\|)` | 5.31356 |
| pure-geom `(2/(3h))·ℏ_q·[3]_q[4]_q/\|S\|` (m_e **cancelled**) | 5.31356 (residual 0.0) |
| counit per-crossing `1/h` | 4.78 |
| **tier-0 (normalization) share of `C_knot`** | **90.8 %** |
| dressing `(bar-odd × bar-even)` `E₂/E_rot` | ×1.10 |

**Reading:** 90.8 % of the "5.853× deficit" is the tier-0 normalization mismatch — the counit scale
`1/h ≈ 4.78` (an *antisymmetric Hecke-eigenvalue difference* `q−q⁻¹`, not a many-body magnitude) times
the pure q₀ rotational geometry `ℏ_q·[3]_q[4]_q`, divided by the character sum `|S|`. The remaining
×1.10 is the bar-odd × bar-even dressing, which `g2-frame-artifact` §3 proves is a **frame projection**,
not a dynamical term: the deuteron word `σ₁³` is a *single generator*, so every Magnus commutator
`[a,a]=0` and `Ω_{k≥2}=0` **exactly** (#4158). **No 5.853× many-body term exists anywhere in the
decomposition.**

## 3. Why the H₆ handle-commutator route is bookkeeping *for the deuteron*

The surviving "missing ingredient" named in `qou-u8w5` is an eigenphase-weighted per-block
handle-commutator charge on the non-abelian H₆ interface braid, tuned to reproduce 5.853. Two
independent proved facts make this bookkeeping for the deuteron:

1. **The deuteron carries no commutator content.** `σ₁³` is single-generator ⇒ `Ω_{k≥2}=0` exact
   (#4158); H₂(q) is commutative ⇒ every commutator vanishes (`TrefoilSurfaceStateSum.commutator_zero`,
   Lean sorry-free). The exhaustive scalar q-invariant scan (`2026-08-02-deuteron-symbolic-closed-form`)
   independently found *nothing* parameter-free at 5.853.
2. **Route B already supplies the 5.853 with 0 parameters.** Any H₆ charge fixed to hit 5.853 would
   **double-count** the counit normalization that Route B derives, i.e. it would be fitting to
   `B_AME/(m_e|S|)` — the forbidden inversion. The 5.853 is not an independent physical prediction; it
   is forced to equal `E₂/B_A`.

So a "derivation" of the deuteron 5.853 via H₆ is either (a) a re-derivation of the counit
normalization already in Route B, or (b) a fit to the diagnostic ratio. Neither is a missing physical
magnitude.

## 4. On `C_knot` non-universality (5.85 / 4.44 / 3.29 / 9.31) — supports artifact

`2026-08-02-c-knot-nonuniversal-pinned-weight.md` cited the 2.83× spread as refuting a *single-scale*
derivation. Under the τ-transfer reading this is exactly expected of an **artifact**: `C_knot` is a
ratio of two *per-knot* geometric objects (the knot's counit-scaled rotational band over its character
sum), so it is naturally per-knot. Non-universality does **not** distinguish artifact from real — but it
is fully consistent with the artifact reading, and the deuteron-pinned scale's cross-isotope
misprediction (+32/+78/−37 %) is just the statement that these two per-knot geometries have different
ratios, not that a many-body magnitude is hiding.

## 5. Verdict, and what stays open

- **scope-(a) — ARTIFACT (deuteron `C_knot`):** the 5.853 is a q₀-geometry normalization ratio between
  Route A (`m_e`-scaled character sum) and Route B (counit-scaled rotational band); `m_e` cancels, the
  counit `1/h` dominates, the dressing is a frame projection. The H₆ handle-commutator program targeting
  the deuteron 5.853 is **bookkeeping** — a scope win (that construction is not warranted here).
- **STILL OPEN (separate):** the **A≥3 extensive many-body term** (12.72× A-growth) — proved-real by the
  intensive-vs-extensive and pairwise-cap arguments. This verdict does **not** touch it. The deuteron
  is simply not the place that term shows up (A=2 pn pair, single-generator word, no commutator).
- **Recommendation:** close the deuteron-specific 5.853 beans (`qou-u8w5`) as **artifact / do-not-pursue
  the H₆-charge-for-the-deuteron route**; keep the A≥3 extensivity beans (`qou-prjo` residual,
  `qou-0c19` inter-nucleon channel) open and re-scoped to the *chain* magnitude, where a genuine
  many-body term lives.

## 6. Anti-fit ledger

| statement | status |
|---|---|
| target `C_knot=5.853` locked before compute | ✓ |
| `B_AME` used only as diagnostic ratio, never inverted | ✓ |
| `m_e` cancellation is algebraic (residual 0.0 at 50 dps), not tuned | **measured** |
| tier-0 normalization = 90.8 % of `C_knot`; dressing only ×1.10 | **measured, 0-fit** |
| `μ₀ = m_e/(3h/2)` derived (0 params); `E_rot = μ₀ℏ_q[3][4]` reproduces committed to 2e-6 % | **measured** |
| deuteron `σ₁³` has `Ω_{k≥2}=0` / H₂ commutative ⇒ no commutator charge | **Lean sorry-free** (#4158, `commutator_zero`) |
| A≥3 extensive term | **OPEN** (separate; not dissolved) |
| free parameters | 0 |
| nothing wired | ✓ |

**Refs:** probe [`c_knot_tau_transfer_artifact_probe.py`](../../computations/deltalambda/c_knot_tau_transfer_artifact_probe.py)
(+ witness `c-knot-tau-transfer-artifact.witness.json`); proved-value witness
[`emit_delta_lambda_value_witness.py`](../../computations/deltalambda/emit_delta_lambda_value_witness.py)
(+ `delta-lambda-witness.json`); `g2-frame-artifact` [`2026-07-26-g2-not-fitted-but-r-is-frame-artifact.md`](2026-07-26-g2-not-fitted-but-r-is-frame-artifact.md);
`C_knot` non-universality [`2026-08-02-c-knot-nonuniversal-pinned-weight.md`](2026-08-02-c-knot-nonuniversal-pinned-weight.md);
trefoil null [`2026-08-02-deuteron-symbolic-closed-form-trefoil-qinvariant.md`](2026-08-02-deuteron-symbolic-closed-form-trefoil-qinvariant.md);
A≥3 extensivity [`2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`](2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md) §4.
