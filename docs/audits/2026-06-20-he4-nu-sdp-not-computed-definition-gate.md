# ⁴He ν_SDP is not computed — the open item is a *definition*, not a *compute* (2026-06-20)

**Status:** audit — reframes an "open" item per the corpus-grep discipline. No fit,
no forced number. Owner-authorized scoped attempt at the n=4 magic-A prefactor.

## What was authorized vs. what the corpus actually shows

The magic-A n=4 binding term is `B = ρ_F · m_e · A · 8G` with `8G =
Vol(Borromean rings) = Vol(L6a4)` an **exact** hyperbolic identity (8·Catalan;
two ideal octahedra) and `ρ_F = ν_SDP` a **settled structural identity**
([`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md)).
`ρ_F` is the only non-geometric factor, so verifying `ν_SDP(⁴He)` is the live
piece of the n=4 mechanism.

The kashaev block's `## Status` and
[`2026-05-31-binding-magic-A-wireup.md`](2026-05-31-binding-magic-A-wireup.md)
§"ρ_F = 2 — what derives it?" frame the open item as *numerical verification
only*: "extend the joint-tower SDP solver to produce `ν_SDP(⁴He)` directly and
confirm the value 2 … The structural derivation is **not** open; only the
numerical verification for ⁴He is."

**That framing is stale.** Per the corpus-grep discipline (source-file `## Status`
is not authoritative), the runnable state is:

1. **No solver computes ν_SDP for *any* atom.** The confirmed values
   (D = 1, T = 2, ³He = 2) are **hardcoded inputs** in
   [`joint_tower_sdp_solver_v2.py`](../../computations/joint_tower_sdp_solver_v2.py)
   (`REGISTRY_PHASE_3B[i]["rho_factor"]`, methodology
   `"manual-historical-volume-match"`). The `sdp_feasibility_h3` routine only
   checks per-block PSD-feasibility (a boolean) of the *given* historical braid —
   it never **counts** a saturating set to *produce* ν_SDP.
2. **The Rust witness's `rho_factor` does not match.**
   [`joint-tower-sdp-rust.witness.json`](../../computations/joint-tower-sdp-rust.witness.json)
   carries `rho_factor = 0, 1, 1` for its first three atoms — neither the
   canonical `1, 2, 2` nor any active-set / saturating-block count (no such
   field exists in the certificate). It is a different, unvalidated quantity.

So "only numerical verification remains" is incorrect: there is **no operational
definition of ν_SDP implemented that reproduces the confirmed D/T/³He = 1, 2, 2**.
The values were matched by hand to the historical knot identifications.

## The extrapolated ⁴He = 2 is not uniquely determined by the data

The confirmed triple is `ν_SDP(D, T, ³He) = 1, 2, 2` at `(Z,N) = (1,1), (1,2),
(2,1)`. Multiple parameter-free rules fit all three and **diverge at ⁴He**:

| rule | D | T | ³He | **⁴He** |
|------|--:|--:|----:|--------:|
| confirmed (manual) | 1 | 2 | 2 | — |
| `max(Z, N)` | 1 | 2 | 2 | **2** |
| `A − 1` | 1 | 2 | 2 | **3** |
| like-pairs `C(Z,2)+C(N,2)` `+1` | 1 | 2 | 2 | **3** |

T and ³He are both `A = 3`, so the data cannot distinguish an "`A`-driven" rule
(→ 3) from a "`max(Z,N)`-driven" rule (→ 2). ⁴He is exactly where a naive pattern
breaks — and it is the doubly-magic atom, the one case the framework already
flags as structurally special ("no single hyperbolic knot"). The assumed value
`ρ_F = 2` is *plausible* (it is what `max(Z,N)` gives) but is **not forced** by
the confirmed data. (These rules are listed to demonstrate non-uniqueness, **not**
proposed as derivations — fitting a 3-point pattern would be the numerology trap.)

## The real gate (formalize-first)

The genuine first step is **not** an H₁₂ compute — it is to pin the *operational
definition* of ν_SDP and show it reproduces `1, 2, 2`:

> `ν_SDP(K_w) =` the multiplicity of the canonical Hecke element `T_w`'s
> **saturating operator-selection SDP solution** in the Wedderburn decomposition
> (= the number of Frobenius-positivity channels with dual shadow price
> `y_star[i] > 0`, per `lp_dual_solver.solve_psd_operator_selection_sdp`).

This must be made runnable and validated against D (knot `6_2`, B₃) and ³He
(link `L6a4`, B₃) — both H₃, where the Hoefsmit seminormal is already in
`joint_tower_sdp_solver_v2.py` — reproducing `ν_SDP = 1` and `2`. Only **after**
the definition reproduces the confirmed values does extending it to ⁴He (H₁₂,
`atom_braid_word_3A(2,2)`, p(12) = 77; needs Hoefsmit at H₁₂ — the ~1–2-session
Rust extension flagged in `geck_pfeiffer.rs`) become meaningful. Running an H₁₂
SDP under a *guessed* definition would produce a number that cannot be checked
against the known anchors — the exact rainbow the formalize-first discipline
forbids.

## Update — a per-block-PSD count was tested, and REFUTED by T (8_11) at H₅

Taking the formalize-first first step (pin a candidate definition, validate against
**all** known anchors before any ⁴He compute), one concrete parameter-free rule was
tested:

> **candidate:  ν_SDP(K_w) = #{ λ ⊢ n, λ ≠ (n) : ρ_λ(T_w) lies in the PSD cone }**
> (symmetric part `(M+Mᵀ)/2 ⪰ 0`; the trivial rep `(n) = q^{writhe} > 0` is always
> positive, so it is excluded — equivalently "(#PSD blocks) − 1", the two readings
> being identical since the trivial rep is *always* PSD).

Computed in the **canonical orthogonal Hoefsmit seminormal form**
([`hoefsmit_numpy.hoefsmit_matrices_numpy`](../../computations/hoefsmit_numpy.py),
the principled basis where `ρ_λ(σ_i)` is symmetric) for **all three** confirmed
atoms — including T (8_11) at H₅, the first out-of-sample test at a new strand
count. Probe
[`computations/probes/he_nu_sdp_psd_count_test.py`](../../computations/probes/he_nu_sdp_psd_count_test.py)
· witness `he-nu-sdp-psd-count-test.witness.json`:

| atom | knot | n | non-trivial PSD blocks | ν_pred | ν_canon |
|------|------|--:|------------------------|-------:|--------:|
| D | 6_2 | 3 | {(1,1,1)} | 1 | 1 ✓ |
| ³He | L6a4 | 3 | {(2,1), (1,1,1)} | 2 | 2 ✓ |
| **T** | **8_11** | **5** | **{(1,1,1,1,1)} only** | **1** | **2 ✗** |

**Verdict: REFUTED.** The rule reproduces the two B₃ atoms but **fails the
out-of-sample H₅ atom T**: only the fully-antisymmetric sign rep `(1⁵)` is PSD; all
five higher-dimensional non-trivial blocks `(4,1), (3,2), (3,1,1), (2,2,1),
(2,1,1,1)` are indefinite (min sym-eigenvalues `−1.03, −0.83, −1.19, −1.36, −1.32`),
giving `ν_pred = 1 ≠ 2`. The 2-point B₃ agreement was coincidental. (A consistency
note retired: "exclude trivial" and "(#PSD) − 1" are *identical*, not two readings —
the trivial rep is `q^{writhe} > 0` for any braid, hence always PSD.)

**Implication.** ν_SDP is **not** a per-block PSD sign test on `ρ_λ(T_w)`. The actual
object is the **operator-selection SDP** (objective `t` + Frobenius Gram `G` + target
`n_target`, per `lp_dual_solver.solve_psd_operator_selection_sdp`), whose saturating
set is the multiplicity — not a per-block sign count. No per-atom `(t, G, n_target)`
spec reproducing `1, 2, 2` exists in the corpus. So the core finding above stands and
is **sharpened**: the obvious per-block-PSD shortcut is now explicitly refuted, and
pinning ν_SDP requires reconstructing the per-atom operator-selection SDP itself.

## Net

- **No fit, no forced ⁴He number.** The honest state: ν_SDP is uncomputed for
  every atom; the confirmed `1, 2, 2` are manual; the extrapolated ⁴He `= 2` is
  one of several rules the data admits.
- **The open item is reclassified:** from "numerical verification of a known
  value" to "pin + validate an operational ν_SDP definition (reproduce D/³He at
  H₃), then compute ⁴He." This corrects the kashaev block's `## Status` and the
  2026-05-31 wireup audit.
- **n=4 mechanism impact:** `ρ_F` (the magic-A prefactor, the +5.87% anchor's
  scale factor) is less settled than the audit chain states. `8G = Vol(Borromean)`
  remains exact; the prefactor's *value* awaits the definition.

## Cross-references

- [`conj:kashaev-density-equals-sdp-multiplicity`](../../content/quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.md) — the `ρ_F = ν_SDP` identity + the (stale) ⁴He `## Status`.
- [`2026-05-31-binding-magic-A-wireup.md`](2026-05-31-binding-magic-A-wireup.md) §"ρ_F = 2 — what derives it?" — the framing this audit corrects.
- [`computations/joint_tower_sdp_solver_v2.py`](../../computations/joint_tower_sdp_solver_v2.py) — hardcoded `rho_factor`; H₃-only PSD-feasibility check.
- [`computations/magic_A_formula.py`](../../computations/magic_A_formula.py) — `B = ρ_F·m_e·A·8G`, `ρ_F = 2` for ⁴He.
- [`docs/coordination/2026-06-05-step9-binding-closure.md`](../coordination/2026-06-05-step9-binding-closure.md) — the n=4 SW-residue / body-order closure framing.
