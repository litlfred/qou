# Per-crossing transfer chain V̂_i(q) for atomic p/n braids — DERIVED from the Hoefsmit seminormal rep

**Date:** 2026-06-01
**Branch:** `claude/vhat-per-crossing-transfer-chain-2026-06-01` (PR #1631)
**Scope:** DERIVE missing input #2 named by the keystone audit
[`2026-06-01-yekutieli-volume-join-derivation.md` §5 item 1](2026-06-01-yekutieli-volume-join-derivation.md),
or characterize the gap. No fit, no tuning to m_p / B_AME. The cached
production volumes are the FALSIFICATION TEST, not a fit target.

**Compute:** [`vhat_per_crossing_chain.py`](../../computations/vhat_per_crossing_chain.py),
witness [`vhat-per-crossing-chain.witness.json`](../../computations/vhat-per-crossing-chain.witness.json).
Every number is RAW; the canonical proton/neutron generator chains
(`pyhecke/atom.py`) and the H₃ seminormal matrices (`mass_at_3A_proper`)
are the only inputs.

---

## VERDICT: (A) DERIVED — V̂_i is the Markov trace of the per-generator reduced element

**V̂_i(q) = z·a_i + b_i is fully DERIVED, with zero free parameters, from
the standard-channel Hoefsmit/seminormal representation of H₃.** It is the
**Markov trace** of the per-generator reduced Hecke element a_i·σ_i + b_i,
not a norm, det, or eigenvalue. The derivation composes to reproduce the
canonical tr_M values exactly (proton ∏V̂ = 1.06531 to 4×10⁻⁶), and it
**differs for proton vs neutron** — the p/n / isospin signal lives in the
per-crossing chain.

**One RED finding (the load-bearing one):** the genuine seminormal V̂_i is
ALREADY computed by production (it is the `"std"` channel of
`atom_per_generator_volumes`), but the brane tower CONSUMES a *different*
object — the W-weighted 3-channel `"full"` scalar
`W_sym·λ_sym + W_std·V_std + W_alt·λ_alt` — which is NOT
`thm:markov-trace-product`'s V̂_i and differs from it by up to **15 %** per
crossing. The audit's "missing input #2" is therefore better described as a
**mis-wired** input than a missing one: the genuine per-crossing V̂_i exists,
but the tower does not eat it.

---

## 1. What V̂_i IS — the matrix functional (DERIVED, cited)

Per [`thm:markov-trace-product`](../../content/quantum-observable-universe/mass-theory/markov-trace-product.md):
after Hecke reduction the crossings at generator σ_i collapse (via the Hecke
quadratic σ² = h·σ + 1) to a linear element

```
    a_i·σ_i + b_i,    a_i, b_i ∈ ℤ[q^{±1}].
```

The Markov trace of this element, using tr_M(σ_i) = z and tr_M(1) = 1, is

```
    V̂_i(q) = z·a_i + b_i,    z = 1/(q^{1/2} + q^{-1/2}).
```

So **the functional is the Markov trace** — `z` times the σ-coefficient plus
the identity-coefficient. This is exactly
[`def:algebraic-quantum-volume`](../../content/quantum-observable-universe/mass-theory/algebraic-quantum-volume.md)'s
`V̂_i = z·a_i + b_i` ("traced volume of generator i"), and the product
∏ V̂_i = tr_M(ρ(β)) is the algebraic quantum volume.

**The (a_i, b_i) transfer recurrence.** For a chain of crossings (c, d) at
generator i, the reduced coordinate (a, b) evolves by left-multiplication by
the 2×2 standard-rep matrix of c·σ + d·1:

```
    a ← a·c·h + a·d + b·c
    b ← a·c     + b·d            (initial (a, b) = (0, 1))
```

This recurrence is the standard-channel **Hoefsmit seminormal matrix** of
c·σ + d·1 acting on span{σ, 1}. The probe confirms this two independent ways
(§3): the scalar (a, b) recurrence agrees with the explicit 2×2 Hoefsmit
matrix product to < 10⁻⁹.

**Which channel.** H₃ has three Wedderburn blocks (partitions of 3):

| partition | dim | seminormal σ_i | role |
|---|---|---|---|
| (3) symmetric | 1 | eigenvalue `q` (i.e. `c·q + d`) | λ_sym |
| (2,1) standard | **2** | the 2×2 Hoefsmit matrix | **V̂_i = z·a+b lives here** |
| (1,1,1) alternating | 1 | eigenvalue `−q⁻¹` (i.e. `−c·q⁻¹ + d`) | λ_alt |

V̂_i is the Markov trace in the **standard (2,1) block only**. This is fully
dictated by the definitions — there is NO latent functional choice (norm vs
trace vs det): `thm:markov-trace-product` names the trace, and `z` is the
Markov parameter. **No RED flag on the functional itself.**

---

## 2. The proton (uud) vs neutron (udd) crossing chains

From [`pyhecke/atom.py::nucleon_gen_chains`](../../tools/pyhecke/python/pyhecke/atom.py),
the per-generator crossing chains are derived from quark content with zero
free parameters (B₃ confinement (σ₀σ₁⁻¹)³ + quark-pair crossings + 2 gluon σ₀):

| generator | chain (c, d per crossing) | crossing reading |
|---|---|---|
| proton σ₀ (uud) | 3×(1,0), 1×(1,−h/2), 2×(1,0) | 3 σ₀ + 1 **ud-mixed** + 2 gluon |
| proton σ₁ (uud) | 3×(1,−h), 1×(1,−h/2) | 3 σ₁⁻¹ + 1 **ud-mixed** |
| neutron σ₀ (udd) | 3×(1,0), 2×(1,−h/2), 2×(1,0) | 3 σ₀ + 2 **ud-mixed** + 2 gluon |
| neutron σ₁ (udd) | 4×(1,−h) | 4 σ₁⁻¹ (the **dd** pair) |

The crossing assignment per quark pair: u-u → σ (c,d) = (1,0); d-d → σ⁻¹
(1,−h); u-d mixed → (1,−h/2). The proton (uud) and neutron (udd) chains
differ precisely in the quark-pair crossings — this is the **only** input
distinguishing them, and it carries the full p/n split.

---

## 3. The derivation — raw per-crossing V̂_i at q₀

q₀ = 1.10997858…, h = 0.20906…, z = 0.49932…. RAW (witness `per_crossing`):

| generator | V̂ = z·a+b (genuine) | V̂ via explicit 2×2 tr_M | production `"full"` | genuine vs `"full"` |
|---|---|---|---|---|
| proton σ₀ | **1.146101** | 1.146101 | 0.989007 | **−13.71 %** |
| proton σ₁ | **0.929504** | 0.929504 | 0.971070 | +4.47 % |
| neutron σ₀ | **1.003852** | 1.003852 | 0.854210 | **−14.91 %** |
| neutron σ₁ | **0.919690** | 0.919690 | 0.975509 | +6.07 % |

- **Cross-check 1 (internal):** the scalar (a, b) recurrence equals the
  explicit 2×2 Hoefsmit-matrix product for all four chains to < 10⁻⁹. This
  confirms V̂ = z·a+b IS the Markov trace of the seminormal matrix, not a
  coincidental scalar formula.

- **Cross-check 2 (falsification against canonical tr_M):** composing the
  genuine per-crossing factors gives

  ```
    proton  ∏V̂ = 1.146101 · 0.929504 = 1.065306
    neutron ∏V̂ = 1.003852 · 0.919690 = 0.923233
  ```

  The keystone audit (§4) cites `tr_M(proton) = 1.06531`. The genuine
  composition reproduces it to **4×10⁻⁶** (the audit value is quoted to 5 dp).
  **The product of the derived per-crossing V̂_i IS the canonical Markov
  trace — falsification test PASS, zero free parameters.**

---

## 4. The RED finding — production consumes the wrong per-crossing object

Tracing the production consumer
[`terms_2_3_atom_per_gen_mpfr_50dps.atom_per_generator_volumes_mpfr`](../../computations/terms_2_3_atom_per_gen_mpfr_50dps.py)
(lines 244–253) and `pyhecke/atom.py::vertex_volume`:

```python
Vs = z·a + b                               # genuine seminormal V̂ (the "std" field)
Vf = w_sym·λ_sym + w_std·Vs + w_alt·λ_alt  # W-weighted 3-channel ("full" field)
```

with `w_sym = w_alt = 1/nf₃`, `w_std = [2]_q²/nf₃`, `nf₃ = [1]_q[2]_q[3]_q`,
normalized to sum 1.

The brane tower (`_li_2_q_util.compute_t2_t3_from_vols`, consumed by
`derive_m_p_hecke_full_tower_50dps`) eats the **`"full"`** field
`|V̂_i^full|`, NOT the `"std"` field.

**Consequence:** the genuine per-crossing V̂_i (the audit's "missing input
#2") is not actually missing — it is computed and stored as `"std"`, exactly
matching `thm:markov-trace-product` (1.146101, 0.929504, … — verified to all
digits against `atom_per_generator_volumes`). The tower simply consumes a
*different* object:

- **Genuine** `V̂_i = z·a+b` (standard channel) — `∏V̂ = tr_M` exactly.
- **Production `"full"`** = W-weighted average of the symmetric eigenvalue
  product λ_sym, the standard V_std, and the alternating eigenvalue product
  λ_alt. This is the H₃ Wedderburn 3-channel average; its product is NOT
  tr_M (proton ∏ = 0.960, neutron ∏ = 0.833), and per crossing it differs
  from the genuine V̂ by up to 15 %.

The W-weighted 3-channel object IS a legitimate Wedderburn construction, but
it is **not** the per-generator Markov-trace factor of
`thm:markov-trace-product`. Whether the tower *should* consume `"std"` or
`"full"` is a wiring decision that changes the m_p / binding numbers — out of
scope for this DERIVE task, and flagged for the owner. This RED is the same
class as the sibling perblock-wiring-fix gate: production uses a 3-channel
Wedderburn average where the paper's per-generator factor is the std-channel
Markov trace.

---

## 5. p/n signal test (isospin) — PASS

The derived per-crossing V̂_i **differ for proton vs neutron** (witness
`pn_signal`):

| generator | V̂_proton | V̂_neutron | relative Δ |
|---|---|---|---|
| σ₀ (strong/quark) | 1.146101 | 1.003852 | **+13.23 %** |
| σ₁ (quark) | 0.929504 | 0.919690 | +1.06 % |

The split is dominated by gen 0 (the strong/quark channel): the proton (uud)
chain has one ud-mixed crossing, the neutron (udd) has two; gen 1 differs
because the neutron's dd pair adds a fourth σ₁⁻¹. **The per-operator V̂_i
chain genuinely carries the p/n / L2 isospin signal**, confirming the audit's
expectation (§5 item 1, "this is also where the isospin / L2 per-operator
signal lives"). It does so in BOTH the genuine `"std"` channel and the
production `"full"` channel — both distinguish p from n — but only the
genuine `"std"` product equals tr_M.

---

## 6. What this audit does and does not claim

- **Does** derive V̂_i = z·a+b end-to-end from the Hoefsmit seminormal rep,
  zero free parameters, and verify it composes to the canonical tr_M (4×10⁻⁶).
- **Does** identify the functional unambiguously (Markov trace of the std
  (2,1) block) — no latent norm/det/eigenvalue choice.
- **Does** confirm the p/n signal lives in the per-crossing chain.
- **Does NOT** tune anything to m_p / B_AME; the canonical tr_M and the
  production `"full"` values are reported as the falsification test.
- **Does NOT** switch the production tower from `"full"` to `"std"` — that
  is a wiring decision (changes m_p) for the owner; this audit only reports
  that the genuine per-crossing V̂_i exists, is the `"std"` channel, and is
  NOT what the tower currently consumes.

**Single most decision-relevant output:** missing input #2 is DERIVED. V̂_i =
z·a_i+b_i is the standard-channel Hoefsmit Markov trace, it composes to tr_M,
and it differs for p vs n. The genuine factor is already present in
production as the `"std"` channel; the brane tower consumes the 15 %-different
W-weighted `"full"` channel instead — a wiring choice, not a derivation gap.
