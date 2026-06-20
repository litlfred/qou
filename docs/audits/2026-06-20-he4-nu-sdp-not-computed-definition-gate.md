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

## Update — a candidate definition, validated on the B₃ atoms (D, ³He)

Taking the formalize-first first step (pin a definition, validate against known
anchors *before* any H₁₂ compute), one concrete parameter-free rule **reproduces
the confirmed values** on the two atoms whose canonical braid is in B₃ (so the H₃
Hoefsmit seminormal is available in pure Python):

> **ν_SDP(K_w) = #{ λ ⊢ n, λ ≠ (n) : ρ_λ(T_w) lies in the PSD cone }**
> (symmetric part `(M+Mᵀ)/2 ⪰ 0`; the trivial rep `(n)` is **excluded** because
> `ρ_(n)(T_w) = q^{writhe} > 0` is always positive — never an informative
> confinement channel).

Probe [`computations/probes/he_nu_sdp_definition_b3_validation.py`](../../computations/probes/he_nu_sdp_definition_b3_validation.py)
· witness `he-nu-sdp-definition-b3-validation.witness.json` (`numpy`; H₃ Hoefsmit
inlined from `joint_tower_sdp_solver_v2.py`):

| atom | knot | writhe | (3) triv | (2,1) std sym-eigs | (1,1,1) sign | non-triv PSD | **ν_pred** | ν_canon |
|------|------|-------:|---------|--------------------|--------------|-------------:|-----------:|--------:|
| D | 6_2 | +2 | +1.232 PSD *(excl)* | `[−0.89, +0.03]` → **not PSD** | +0.812 PSD | {(1,1,1)} | **1** | 1 ✓ |
| ³He | L6a4 | 0 | +1.000 PSD *(excl)* | `[+0.98, +1.01]` → PSD | +1.000 PSD | {(2,1),(1,1,1)} | **2** | 2 ✓ |

The discriminating block is the **std (2,1)** rep: indefinite for D (→ ν=1), PSD
for ³He (→ ν=2). The naive *total* PSD count (2, 3) does **not** match; excluding
the always-positive trivial rep does.

**Honest caveat (2-point validation).** D and ³He are the only confirmed atoms in
B₃. On these two points the rule coincides with "(#PSD blocks) − 1" (the trivial
rep is always PSD, so the two readings are identical here). The **discriminator**
is the third confirmed atom **T (8_11, ν=2), which is in B₅** and needs the H₅
Hoefsmit seminormal (deferred to the Rust crate) to tell the two readings apart.
Applying the rule to ⁴He needs Hoefsmit at H₁₂ (p(12)=77 blocks). This probe does
**not** extrapolate ⁴He — it pins + validates the definition on what is computable
today, and gives the ⁴He computation a concrete, falsifiable recipe (count
non-trivial PSD blocks of `ρ_λ(T_w(⁴He))`).

This upgrades the open item from *"no operational definition exists"* to *"a
candidate definition validated on 2/3 confirmed atoms; T@H₅ is the discriminator,
then ⁴He@H₁₂."*

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
