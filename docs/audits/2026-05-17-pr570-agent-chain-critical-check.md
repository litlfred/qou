# Critical check: PR #570 agent's "CAL-only" chain for μ_u, μ_d

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**Source**: PR #570 agent message (relayed by owner 2026-05-17)

The PR #570 agent corrected their earlier answer and proposed the
following derivation chain:

> "CAL-2 m_μ/m_e fixes q_0 via Vol(4_1)/ℏ_q².  CAL-1 m_e fixes
>  the dimensional bridge.  CAL-3 𝔇_π(n) fixes E_0.  From those
>  three, β_p, β_n are topologically determined (no fit), and
>
>    m_{q,K} = |tr_M(ρ(β_K))|
>
>  gives m_p(q_0), m_n(q_0) STRUCTURALLY.  CODATA values are
>  falsifiability targets, not calibrations.  Then the Skein-pair
>  decomposition gives μ_u, μ_d as further predictions.
>
>  Net: μ_u, μ_d come out of {m_e, q_0, Q_β(n)} only — three
>  inputs, two-step structural chain."

## Critical assessment — the chain DOES NOT close numerically

The agent's claim is **theoretically valid** but the **first step
fails empirically** in the existing implementations.

### Step 1 — m_p from `|tr_M(β_p)|` alone

Under the formula `m_p = |tr_M(ρ(β_p))| · m_e`:

| quantity | value |
|---|---:|
| `|tr_M(β_p)|` (substrate-derived) | 1.0653 |
| m_e (CAL-1) | 0.511 MeV |
| `\|tr_M(β_p)\| · m_e` | **0.544 MeV** |
| CODATA m_p | **938.272 MeV** |
| **residual** | **−99.94 %** |

The straight `|tr_M| · m_e` formula gives **0.544 MeV, NOT 938 MeV**.
A factor of ~1723× is missing — exactly the ρ_K factor identified in
[`2026-05-17-rho-vs-rho-K-paper-discrepancy.md`](2026-05-17-rho-vs-rho-K-paper-discrepancy.md).

### Why the agent's chain over-promises

`atomic-mass-gb-nf.md` line 32 explicitly states the mass formula as:

```
M(K) = m_e · ρ_K · |tr_M(NF_GS(β_K))|
                ↑
             this factor
```

Without `ρ_K`, the formula gives 0.544 MeV (off by 1700×). The PR
#570 agent's chain `m_{q,K} = |tr_M(ρ(β_K))|` (in cat-units,
multiplied by m_e to MeV) **omits** `ρ_K` — equivalently, assumes
`ρ_K = 1`. But empirically `ρ_K = 1723.6` for the proton (per
`atomic-mass-gb-nf.md` line 62).

The paper itself acknowledges this at line 71:

> "**Open question: categorical derivation of ρ_K**"

The agent's chain corresponds to "what the formula WOULD give if
ρ_K were 1", which it isn't.

### Alternative reading — agent might mean Picard-Lefschetz chain

The Picard-Lefschetz formula in [`picard_lefschetz_thimble.py`](../../computations/picard_lefschetz_thimble.py) does close numerically:

```
m_p = Vol(𝔅_3) / ℏ_q² · A(q_0) · m_e   ≈   938.27 MeV   (6 ppm)
```

But this uses **A(q_0)** ≈ 2.46 (a different substrate quantity)
in place of `|tr_M(β_p)|` ≈ 1.0653.  And A(q_0) is itself
**post-hoc best-fit** of the integration limit `a = (4-q)/(4q+3)`
(per [`2026-05-17-substrate-m-p-m-n-compute-audit.md`](2026-05-17-substrate-m-p-m-n-compute-audit.md)).

So even the PL chain ISN'T a pure substrate prediction — it's
"substrate + best-fit integration limit".

### Step 2 — Skein pair decomposition

The agent's Step 2 (`m_p = 𝒮_uu + 2·𝒮_ud` etc.) is an **ALGEBRAIC
IDENTITY** for distributing m_p, m_n across (μ_u, μ_d).  If you
have m_p AND m_n from somewhere, you CAN solve for μ_u, μ_d:

- Sum equation: `m_p + m_n = 𝒮_uu + 4·𝒮_ud + 𝒮_dd` (gives μ_u + μ_d)
- Difference: `m_n − m_p = [2]_q·z·(μ_d − μ_u)` (gives μ_d − μ_u)

Solving: 2 equations, 2 unknowns, exact (up to the algebra of the
pair-Skein formula).

So Step 2 is **structurally valid**.  But it consumes m_p, m_n as
INPUTS — it doesn't derive them.

### The true derivation status

| chain step | claim | actual status |
|---|---|---|
| Step 0: CAL-1 + CAL-2 + CAL-3 fix (m_e, q_0, E_0) | OK | ✓ |
| Step 0.5: β_p, β_n topologically fixed | OK | ✓ (per β_p = (σ_1σ_2⁻¹)³, β_n similar) |
| Step 1: m_p = `|tr_M|·m_e` from CAL-only | "structural prediction" | **FAILS** by 1700× (ρ_K missing) |
| Step 1': m_p = Vol(𝔅_3)/ℏ_q² · A(q_0) · m_e via PL | substrate + best-fit | partial: 6 ppm BUT `a` post-hoc |
| Step 2: μ_u, μ_d via inverse Skein pair | "further predictions" | ✓ algebraic (given m_p, m_n) |

### Reduction summary

The agent's "19 → 3 reduction" (≥19 mass observables → 3 calibration
inputs) is **the target structural picture** but **not yet closed**.
Currently the framework reduces:

```
19 mass observables → CAL-1 + CAL-2 + CAL-3
                    + ρ_K (currently 1 implicit calibration per atom)
                    OR
                    + best-fit integration limit a (one post-hoc value)
```

So **4 inputs (3 CAL + 1 open piece)**, not 3.  The open piece is
the same one across all framings: `ρ_K` per atom OR equivalently
the PL integration limit `a` OR the dressed quark mass μ_avg ≈ 311
MeV.

## Conclusion — be critical of the over-claim

The PR #570 agent's chain is the **right structural skeleton** but
the **first step ("m_p from `|tr_M|·m_e` alone")** has not closed
empirically.  The agent's "net: μ_u, μ_d come out of {m_e, q_0,
Q_β(n)} only" overstates the current state of the derivation.

To bring the claim in line with reality, one of the following must
happen:

1. Derive the `ρ_K(β_K, q_0)` factor categorically (the
   atomic-mass-gb-nf.md open problem)
2. Derive the PL integration limit `a(q_0)` categorically (e.g.
   via SDP-bootstrap analog per probe_sdp_determines_pl_integration_limit.py)
3. Derive the dressed mass scale μ_avg ≈ 311 MeV categorically
   (per probe_mu_q_ell_1_substrate.py)

All three are EQUIVALENT formulations of the same open piece.

Until then, the framework is at **CAL + 1** (4-parameter), not
CAL-only (3-parameter).

## Cross-references

- [`docs/audits/2026-05-17-rho-vs-rho-K-paper-discrepancy.md`](2026-05-17-rho-vs-rho-K-paper-discrepancy.md)
- [`docs/audits/2026-05-17-substrate-m-p-m-n-compute-audit.md`](2026-05-17-substrate-m-p-m-n-compute-audit.md)
- [`docs/audits/2026-05-17-mu-u-mu-d-clarification-and-ell-1-investigation.md`](2026-05-17-mu-u-mu-d-clarification-and-ell-1-investigation.md)
- [`computations/probe_sdp_determines_pl_integration_limit.py`](../../computations/probe_sdp_determines_pl_integration_limit.py)
- [`computations/probe_mu_q_ell_1_substrate.py`](../../computations/probe_mu_q_ell_1_substrate.py)
- `atomic-mass-gb-nf.md` line 71 (paper's own acknowledgment of open ρ_K)
