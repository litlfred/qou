# α_EM B2 τ-scale — canonical-scale-ratio attempt: the "25 = deg(5-isogeny)²" observation cannot be made fully normalization-free (outcome iii); the surviving conditional restatement is θ₅ = 0 under H₅

**Date:** 2026-07-25 · **Epic:** `qou-k42c` · **Axis:** α_EM per-loop measure,
the B2 τ-identification's scalar `c` (τ-scale gate) · **Discipline:** standing
2026-07-19 owner ruling respected — the per-loop identification is NOT
derived-proved; no fit; no tuning; nothing wired; no `TauRhoHodgeLift`
instance; `1/(8π)` stays phase-4; conditional language throughout. Route C's
refutation ([`alpha-em-b2-invariant-c.witness.json`](../../computations/alpha-em-b2-invariant-c.witness.json))
stands untouched and is the *starting point* here.

**Probe:** [`computations/alpha_em/alpha_em_b2_canonical_scale_ratio_probe.py`](../../computations/alpha_em/alpha_em_b2_canonical_scale_ratio_probe.py)
· **Witness:** [`alpha-em-b2-canonical-scale-ratio.witness.json`](../../computations/alpha_em/alpha-em-b2-canonical-scale-ratio.witness.json)
(8/8, mpmath 50 dps + 10 guard).

## 1. The question

The route-C canonical representative `c_geo = det(G_M·G_H⁻¹)^{1/4} =
0.9947074314…` has `c_geo·8π = 24.9997244717` — within 1.1e-5 (relative) of
`25 = deg(5-isogeny)²` (W7 of the merged
[CM/Weierstrass probe](2026-07-25-alpha-em-b2-cm-weierstrass-scale.md)). That
value carries the entry-`[0,0] = 1` convention on **both** Grams. The premise
tested here: if the Markov side is pinned by an *intrinsic* Hecke normalization
(Markov trace `tr(1)=1` / `y_λ`) and the Hodge side by the Néron/ℚ-model
periods, the ratio becomes convention-free and "= 25 exactly?" becomes
well-posed. This was the only route that could promote the τ-scale gate from
"discrete set" to a derived integer.

## 2. K1 — the gauge group has THREE scales, not two

The Schur scalar in `τ(G_Markov) = c·G_Hodge` transforms under

$$G_M \mapsto \lambda G_M,\qquad G_H \mapsto \mu G_H,\qquad P \mapsto s\,P$$

(`P` = the Schur intertwiner, unique up to scalar — Lean-proved covariance
`invariantForm_pullback_smul`,
[`InvariantFormTransport.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/InvariantFormTransport.lean))
as `c ↦ (λ/(μ s²))·c`. Machine-verified by direct transform (deviation
5e-60); route C's I1 had fixed `P = id` implicitly. **Consequence: canonically
pinning both Grams still leaves the intertwiner gauge `s²`** — a fully
normalization-free magnitude is impossible with two pins. The premise "both
sides canonical ⇒ convention-free" is false as stated; the third scale *is*
the τ-scale gate restated.

## 3. K2 — the surviving conditional restatement (the maximum extractable)

The merged Weierstrass probe (W6) narrowed the residual Néron-normalized
freedom to a **discrete** set (isogeny-degree pullbacks, natural support
powers of 5). **IF** all three residual gauges are 5-power-graded
(hypothesis **H₅** — motivated Hodge/intertwiner-side by W6, *unverified*
Markov-side), then

$$\theta_5 := \mathrm{frac}\bigl(\log_5(c\cdot 8\pi)\bigr)$$

is gauge-invariant, and the normalization-independent restatement of
"25 = deg²" is **θ₅ = 0**. Measured in the route-C gauge at 50 dps:
`log₅(c·8π) = 1.99999315…`, **θ₅ = −6.85e-6**, selected pullback grade
`k = 2`. This is the honest translation of the same 1.1e-5 residual —
*conditional on H₅, not derived*.

## 4. K3 — the Markov leg of H₅ fails for the declared intrinsic pins

Three intrinsic Hecke-side candidates, declared in advance (no selection),
computed at q₀:

| pin | value at q₀ | frac(log₅) folded |
|---|---|---|
| (a) Jones–Markov `y_(4,1)` ([`wedderburn_jones_markov.y_lambda_at`](../../computations/wedderburn_jones_markov.py); `tr(1)=1` certified: `Σ_λ y_λ f^λ = 1` to 6.6e-51) | 0.10937853185894286297 | −0.374977 |
| (b) Wedderburn weight `w_(4,1) = d_q²/[5]_q!` (the [`alpha_em_b2_scalar_c_probe`](../../computations/alpha_em_b2_scalar_c_probe.py) normalization) | 0.12862000417524688333 | −0.274291 |
| (c) cellular/Murphy anchor candidate `γ_{T^λ} = [4]_{q²}!` relative to the corpus-STRICT presentation (dictionary `T = q·σ`, `(T−q²)(T+1)=0`, machine-exact) | 47.042282292036314839 | +0.392790 |

**F1 — no unique canonical Markov 5-class.** The three candidates are
mutually inequivalent mod 5^ℤ (pairwise 5-class distances 0.101 / 0.232 /
0.333, all ≫ 1e-3). "The" canonical Markov pin does not exist as a unique
5-class — H₅'s Markov leg fails for the declared menu.

**F2 — trace pins transmit no module scale (structural).** Every
Markov-trace observable lives on `End(V)`, where the module-form scale
cancels (`G`-adjoint invariant under `G ↦ λG`, machine-verified to 0). The
canonical *algebra* scalars (a), (b) are not canonical *module* forms; the
contravariant solve returns a line (Schur), and no trace datum selects a
point on it. Pin (c) is the one candidate at module level; its two unverified
convention legs are named (tableau-0 = row-reading `T^λ`; Hoefsmit-natural =
Murphy-unitriangular seminormal) — not asserted.

## 5. K4 — the 25 does not survive the declared pins (scope-(a), per pin)

Under each declared pin the ratio moves off the 5-power grading:

| pin | `c·8π` under pin | dist to 5^ℤ grading |
|---|---|---|
| y_λ | 2.734 | 0.375 |
| w_Wedderburn | 3.215 | 0.274 |
| γ_cellular | 1176.0 | 0.393 |

The 24.9997 ≈ 25 match is (so far) a property of the entry-`[0,0]=1`
convention, not of any canonical normalization. **Scope-(a):** this refutes
the declared pins *as stated, alone* as the normalization-freedom route; it
does not structurally exclude a future verified module-level pin + Hodge
anchor combination. No pin was selected — selecting the pin that preserves 25
would be tuning.

## 6. K5 — the exact matching condition (what a future τ-derivation must satisfy)

$$\text{"25 survives canonically"} \iff \frac{\lambda_M}{\mu_H\, s^2} \in 5^{\mathbb Z}
\iff \mathrm{frac}\bigl(\log_5(\mu_H s^2)\bigr) = \mathrm{frac}(\log_5 \lambda_M).$$

Per-pin targets for the Hodge×gauge anchor: −0.3750 (y), −0.2743 (w),
+0.3928 (γ). Sharp, falsifiable, recorded — not adjudicated (owner-level).

## 7. K6 — the Hodge canonical pin is blocked, precisely named

The curve-integration Hodge form `h(ω,η) = (i/2)∫_Bring ω∧η̄` is the one
genuinely convention-free scale in the problem, but evaluating its scalar
against the transported Markov form needs:

1. the **Riera–Rodríguez integral-symplectic period matrix `Z`** — absent
   from the corpus (named open in the
   [attack-options doc](2026-07-24-alpha-em-b2-tau-identification-attack-options.md));
2. the **Néron period magnitudes `|Ω_i|²`** of the four 50a factors —
   non-CM (CM refuted, W1 of the merged probe), so no Chowla–Selberg closed
   form; the 50a minimal models are not corpus data (only the two
   j-invariants are).

The isogeny-adapted frame is not S₅-equivariant (c-pin probe V5), so
per-factor Néron pins cannot be transported to the invariant scalar without
`Z` — the anticipated "3 × E_{5τ₀} vs 1 × E_{τ₀} breaking a uniform scale"
obstruction manifests exactly here. Blocked, not fabricated.

## 8. Verdict — outcome (iii), scope-(a)

The single-ratio question "does `c·8π = 25` exactly?" **cannot be made fully
normalization-free**: (O1) no unique intrinsic Markov module-scale (trace
pins don't transmit; declared candidates mutually inequivalent mod 5^ℤ);
(O2) two pins cannot fix the three-scale gauge (Lean-proved `s²` covariance);
(O3) the Hodge canonical evaluation is gated on the absent `Z` + non-CM
periods. What survives: the **conditional restatement θ₅ = 0 under H₅**
(§3) and the **exact matching condition** (§6) that a legitimate
τ-identification must satisfy for the deg² = 25 observation to become a
derived integer. The observation **remains open, owner-level, double-gated**
— now triple-annotated with the condition for its eventual promotion.
Nothing wired; `1/(8π)` stays phase-4.

## Status table

| item | status |
|---|---|
| three-scale gauge group (λ, μ, s²) | certified (transform check 5e-60; Lean `invariantForm_pullback_smul`) |
| θ₅ = frac(log₅(c·8π)) = −6.85e-6, k = 2 | measured (route-C gauge); restatement **conditional on H₅** |
| H₅ Markov leg for declared pins (y, w, γ) | **fails** — mutually inequivalent mod 5^ℤ (F1); scope-(a) |
| trace pins → module scale | **structurally non-transmitting** (End(V) blindness, F2) |
| 25 under declared pins | does **not** survive (K4, per-pin rows, no selection) |
| matching condition for future closure | stated (K5), owner-level |
| Hodge canonical pin | **blocked** — Riera–Rodríguez `Z` absent + non-CM periods (K6) |
| ratio 24.9997 ≈ 25 = deg² | **unchanged: observation, OPEN, owner-level, double-gated** |
| τ-identification / scalar `c` / `1/(8π)` | **unchanged: OPEN / phase-4** (2026-07-19 ruling) |

## Cross-references

- The 25 = deg² observation (input): [`2026-07-25-alpha-em-b2-cm-weierstrass-scale.md`](2026-07-25-alpha-em-b2-cm-weierstrass-scale.md)
- Route-C refutation (input): [`../../computations/alpha_em_b2_invariant_c_probe.py`](../../computations/alpha_em_b2_invariant_c_probe.py)
- Sub-piece (ii) quantified: [`../../computations/alpha_em_b2_tau_intertwiner_probe.py`](../../computations/alpha_em_b2_tau_intertwiner_probe.py)
- Attack plan: [`2026-07-24-alpha-em-b2-tau-identification-attack-options.md`](2026-07-24-alpha-em-b2-tau-identification-attack-options.md)
- Gauge covariance (Lean): [`InvariantFormTransport.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/InvariantFormTransport.lean)
- Ruling (read-first): [`2026-07-19-alpha-em-r2-owner-ruling.md`](2026-07-19-alpha-em-r2-owner-ruling.md)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
