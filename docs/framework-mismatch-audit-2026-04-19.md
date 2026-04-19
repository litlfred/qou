# Framework mismatch — H_{3A} Plancherel vs H_A 3-channel Wedderburn

Domain audit following user directive 2026-04-19:

> "per-A structure growth... Weighted partitions? Follow derivation from
> frobenius to mass tower endomorphism"

## The derivation

The canonical chain [Frobenius pairing] → [mass tower endomorphism]
→ [nuclear binding energy] leads to:

**[prop:mass-endomorphism-tower]** (single vortex, n strands, n−1
generators — derived for a proton, electron, or any single knot):

$$
\mathfrak{m}(\varrho) = |\prod_{i=0}^{n-2} \hat{V}_i| + \sum_i \Phi_q(\hat{V}_i)
                      + \sum_{i<j} z^2 \Phi_q(\hat{V}_i \hat{V}_j).
$$

**[prop:tower-binding-energy]** (multi-nucleon atom with A nucleons, A−1
generators in H_A(q), NOT 3A generators in H_{3A}(q)):

$$
B(Z, N) = \sum_{\lambda \in \{sym, std, alt\}} w_\lambda \cdot m_e
          \cdot \sum_{i=0}^{A-2} \ln|\Phi_q(\hat{V}_i^\lambda)|,
$$

with Wedderburn weights
- $w_{sym} = w_{alt} = 1 / ([2]_q^2 + 2) \approx 0.165$
- $w_{std} = [2]_q^2 / ([2]_q^2 + 2) \approx 0.669$

and energy unit $m_e = 0.511$ MeV (electron mass), NOT $E_0 = 0.782$ MeV
(β-decay Q).

## The mismatch

During this session I've been running SDP decisions and error analyses
against `mass_at_3A_proper.py` and `canonical_plus_multibrane.py`.
Both of these operate in **H_{3A}(q)**:

- `mass_at_3A_proper.binding_3A`: Plancherel sum over p(3A) partitions,
  canonical Markov trace only.
- `canonical_plus_multibrane.binding_canonical_plus_multibrane`:
  symbolic canonical Markov trace + single-vortex formula applied to
  3A−1 generators with $\hbar_q^{2n}$ brane damping.

Both apply the single-vortex formula (which has a $\prod_i \hat{V}_i$
term over n−1 factors) to an atom braid with 3A−1 generators. The ∏
grows exponentially with A; this is the per-A blow-up I observed
(4He tower raw = 21,745 MeV, scaled to 213 MeV vs AME 28 MeV).

## What the correct framework looks like

[`full-tower-mass.py`](../folio-assistant/computations/full-tower-mass.py)
already implements the correct prop:tower-binding-energy formula and
produces the audit table at the top of prop:tower-binding-energy:

| Atom | Z | N | B_pred | B_AME | err |
|------|---|---|-------:|------:|------|
| D    | 1 | 1 |   4.92 |  2.22 | −0.144% |
| 4He  | 2 | 2 |  19.41 | 28.30 | +0.238% |
| 7Li  | 3 | 4 |  42.24 | 39.24 | −0.046% |
| 12C  | 6 | 6 |  82.89 | 92.16 | +0.083% |
| 40Ca | 20 | 20 | 317.38 | 342.05 | +0.066% |

**Mean error across Z=1..20: 0.071%.** No per-A blow-up.

Framework characteristics:
- **H_A(q)** — A strands, A−1 generators. Each "strand" represents a
  nucleon, not a quark.
- **Three Wedderburn channels** (sym, std, alt) with fixed weights, NOT
  a Plancherel sum over all p(n) partitions.
- **$\ln|\Phi_q|$** per generator per channel, NOT the single-vortex
  $|\prod V| + \Sigma\Phi_q + \Sigma z^2 \Phi_q$ formula.
- **m_e** as energy unit, NOT β-decay E_0.

## What the session's SDP work did

All SDP decisions I've implemented so far
(`sdp_inter_nucleon.py`, `sdp_gluon_multiplicity.py`,
`electron_knot_operator_sdp.py`, `electron_demand_supply_sdp.py`,
`electron_demand_supply_sdp_h3A.py`) use the H_{3A}(q) Plancherel
framework. They are internally consistent with that framework, but
that framework itself is a distinct (non-prescribed) extension of
the single-vortex formula to a multi-nucleon braid, NOT the
content-block prescription.

**Status of those SDPs:** They are correctly solved under their chosen
objective (min tr_M_atom at H_{3A} Plancherel), but the objective
itself is not the one prescribed by prop:tower-binding-energy.

## What needs to happen

To run SDP decisions on the CORRECT framework, all 12 decision points
from the earlier audit need to be reformulated against
`full-tower-mass.py`'s 3-channel per-generator V̂^λ structure:

- `sdp_inter_nucleon.py` → decide (m_pp, m_pn, m_nn) by minimising
  error under the 3-channel B formula, not min tr_M_atom at H_{3A}.
- `sdp_gluon_multiplicity.py` → decide per-nucleon gluons using
  per-channel per-gen V̂^λ, not Plancherel tr_M.
- `electron_*_sdp.py` → decide electron knot operator / position using
  the 3-channel V̂^λ and ln|Φ_q| per-generator structure.

The correct framework's V̂^λ is per-generator per-channel (symmetric,
standard, alternating), computed from the per-nucleon quark content +
inter-nucleon crossings + gluon decoration. No A-growth of raw tower
because each generator contributes independently via ln|Φ_q|, which
is bounded.

## Next steps

Options for the user:

1. **Retarget SDP work** to the `full-tower-mass.py` framework. All
   SDP decision points should use the 3-channel V̂^λ per generator
   as their computation primitive, not Plancherel tr_M at H_{3A}.

2. **Run the current full-tower-mass.py on current atoms** to establish
   the baseline before any SDP. Mean 0.071% error is already 3–5× better
   than any SDP result from this session on H_{3A}.

3. **Reconcile the two frameworks** in content: is H_{3A} Plancherel
   an accepted alternative derivation? If so, document; if not,
   deprecate `mass_at_3A_proper` and `canonical_plus_multibrane`
   in favour of `full-tower-mass`.
