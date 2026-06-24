# Canonical nucleon/atom mass — guardrail (READ BEFORE touching mass compute)

**Owner ruling 2026-06-24.** There is **one** correct absolute nucleon
mass: the **muon-anchored Hecke energy** (the production substrate-identity).
Two Borromean-volume forms that look canonical are **wrong** and are
deprecated. This doc exists so the error does not recur.

## ✅ The canonical formula (use this)

```
m_p = dim V_{(2,1)} · (m_μ · F_Bor − |S_3| · m_e) = 2·(m_μ·F_Bor − 6·m_e)
m_μ   = m_e · Vol(4₁) / ℏ_q²            # muon anchor — figure-8 knot 4₁
F_Bor = |tr_M(β_Bor)| · [3]_q! / q³     # dimensionless Borromean Hecke factor
      → m_p ≈ 938.27 MeV,  m_n ≈ 939.56 MeV   (matches CODATA; m_n predicted)
```

The `c_q² = 1/ℏ_q²` factor is applied **once**, in the muon anchor `m_μ`,
then dressed by the **dimensionless** Borromean factor `F_Bor`.

**Single entry point (facade):** [`computations/canonical_mass.py`](../computations/canonical_mass.py)
— `proton_mass_mev()`, `neutron_mass_mev()`, `nucleon_mass_mev(species)`,
`proton_neutron_mass_mev()`. Route **every** absolute-mass consumer through
it. Producer: [`m_p_substrate_identity_50dps.py`](../computations/m_p_substrate_identity_50dps.py);
witness `m-p-substrate-identity-50dps.witness.json`.

## ❌ The wrong forms (do NOT use for absolute mass)

| form | function | m_p | why wrong |
|---|---|--:|---|
| `m_e·Vol(𝓑₃)·λ_A/ℏ_q²` | `vol_density_borromean` / `mass_vol_density` | 966 (+2.96%) | λ_A is a CODATA-implied **fit**; applies 1/ℏ_q² to the **Borromean** volume |
| `m_e·Vol(𝓑₃)·tr_M/ℏ_q²` | `vol_density_per_block` (as abs mass) | 406 (−57%) | naive per-knot; same wrong-volume error |

Both apply `1/ℏ_q²` to **Vol(𝓑₃)** (Borromean) — but the `c_q²` belongs in
the **muon** anchor `Vol(4₁)`. `mass_vol_density()` now emits a
`DeprecationWarning`. `linking_weight_family_a` / `λ_A` is the fit itself
(see `docs/coordination/2026-06-24-lambda-a-fit-excised-per-knot-density.md`).

**`vol_density_per_block` is still fine for BINDING** (trace *ratios*
`B = α·ln(tr_free/tr_atom)` where the absolute density scale cancels and the
p≠n distinction matters). It is wrong only as an **absolute mass**.

## Why this kept happening

AGENTS.md historically stated the mass formula as `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²`,
which — read with `K = 𝓑₃` — *is* the wrong form. Agents (incl. the dashboard
work that triggered this) followed it. The correct reading uses the muon
anchor `Vol(4₁)` plus the dimensionless `F_Bor`, not `Vol(𝓑₃)·ρ`. The
AGENTS.md banner now points here.

## Checklist before writing/altering mass compute

1. Absolute nucleon/atom mass? → call `canonical_mass` facade. Do **not**
   reimplement `Vol·ρ/ℏ_q²`.
2. Binding/shell (ratios, differences)? → per-knot `tr_M` is fine; the scale
   cancels.
3. Studying λ_A itself (a research probe)? → allowed, but it is a **fit**, not
   a derived density; label it so.

Resolution audit: [`docs/audits/2026-06-24-lambda-a-refutation-artifact-audit.md`](audits/2026-06-24-lambda-a-refutation-artifact-audit.md).
