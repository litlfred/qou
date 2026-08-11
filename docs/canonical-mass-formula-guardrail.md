# Canonical nucleon/atom mass — guardrail (READ BEFORE touching mass compute)

> **🛑 ABSOLUTE MASS EXCISED (owner ruling 2026-08-11, bean `qou-exam`).** The
> framework no longer claims/targets/scores an **absolute** nucleon or atomic mass
> in MeV as a prediction. The canonical formula below **still stands** — but its
> MeV output is an `m_e`-scaled *realization of the dimensionless ratio* `m_p/m_e`,
> not an absolute-mass claim. This guardrail is retained to keep the *ratio*
> realization on the one correct (muon-anchored) form and off the deprecated
> Borromean-volume forms. Full ruling:
> [`audits/2026-08-11-excise-absolute-mass-notion.md`](audits/2026-08-11-excise-absolute-mass-notion.md).

**Owner ruling 2026-06-24.** There is **one** correct [now: `m_e`-scaled] nucleon
mass form: the **muon-anchored Hecke energy** (the production substrate-identity).
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

## 🗣 Status-claim guard (conversational / audit / strategy) — added 2026-08-01

The compute layer is guarded (facade + `DeprecationWarning`), but the error also recurs in
**prose** — chat answers, audit docs, strategy notes citing a *remembered* "m_p gap". It
recurred 2026-08-01 (an agent with this guardrail in context still said "m_p misses ~437× /
2.89% Vol·ρ gap" in a strategy answer). Root cause: **conflating two different "m_p miss"
numbers.** Do not.

### ✅ Live status (cite THIS when asked about m_p / absolute-mass accuracy)

**Canonical m_p is CODATA to `+1.35 ppb`** (muon-anchored Hecke energy via
`canonical_mass.proton_mass_mev()`); m_n `+2.39 ppb`. **Absolute nucleon mass is solved to the
ppb level.** Source of record: `computations/per-observable-100x-status.witness.json` — cite
its `err_ppb`, never a remembered figure.

### ⚠ The two numbers that must NEVER be conflated

| number | what it is | cite as m_p status? |
|---|---|---|
| **`+1.35 ppb`** | real: canonical de-fitted round-trip. The "**437× miss**" is *this* vs the **3-ppt research-grade** 100× target (m_p's σ_exp is 0.31 ppb, so 100×-of-that is 0.003 ppb). Real but *tiny* — it "misses" only because m_p is measured sub-ppb. | **YES** — this is the live status |
| **`+2.89% / +2.96% / 966 MeV`** (also `406 MeV / −57%`) | DEPRECATED `Vol(𝓑₃)·λ_A/ℏ_q²` wrong form — a purged fit. **Not a real discrepancy.** | **NEVER** |

**Rule.** When asked "how accurate is m_p / is there an m_p gap", the answer is **1.35 ppb**
(solved to ppb). Never present `2.89% / 2.96% / 966 / 406 / −57% / "Vol(𝓑₃)·ρ gap" / "λ_scale"`
as the *live* status. The "437×" is a **research-target** artifact, not a gross discrepancy —
say so if you cite it. Absolute nucleon mass is **not** where the L2 gap lives; the real L2
content is the *relations* (μ–p tension m_μ +210 ppb; Q_β/Δ_pn) — see
[`docs/coordination/2026-08-01-l2-strategy-q0-observed-delta-lambda-scope.md`](coordination/2026-08-01-l2-strategy-q0-observed-delta-lambda-scope.md).

### Machine backstop

[`computations/canonical_mass_status_guard.py`](../computations/canonical_mass_status_guard.py)
(warn-only; `--strict` fails) scans `content/` + `docs/` for the deprecated absolute-mass
magnitudes presented near m_p/proton-mass, with an allowlist for this guardrail + the
deprecation audits. Run it before shipping an audit/strategy doc that discusses m_p accuracy.
