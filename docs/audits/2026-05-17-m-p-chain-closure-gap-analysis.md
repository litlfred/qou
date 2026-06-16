# m_p chain closure — what's actually missing

**Date:** 2026-05-17
**Branch:** `claude/post-670-story-b-mp-c5-c6`
**Status:** Analysis of the residual gap in the proton-mass derivation
chain after PR #663's honesty pass. Identifies the structural
follow-ups needed before `m_p` can move from `derivation_pending` to
`derived`.

## TL;DR

PR #663's closure path stated: *"`build_proton_mass_50dps_chain.py`
closes T1+T4 in `mass_endomorphism.py`."* This is **partially** true
— T1+T4 are individually computable at 50 dps — but T1+T4 **alone**
gives

$$
\frac{m_p^{\mathrm{Hecke}}}{m_e^{\mathrm{Hecke}}}
\;=\; 1.169 \quad\not\approx\quad 1836.15 \;=\; (m_p/m_e)_{\mathrm{CODATA}}
$$

at 50 dps. Tightening `M_P_DERIVED_MAX_REL_DIFF` from 1 % to 1 ppm
won't help; the partial Path A is structurally three orders of
magnitude too small. **What's missing is T2 + T3 at A = 1, T5 and T6
structural ansätze, or a different tower assembly entirely.**

This audit identifies the three open R&D items that would actually
close the chain.

## Tower decomposition (from `mass_endomorphism.mass_from_tower()`)

For each particle, `mass_endomorphism.mass_from_tower(vols)` returns

| term | formula | role |
|---|---|---|
| T1 | $\prod_g \hat V_{\mathrm{full}, g}$ | descended Markov trace product |
| T2 | $\sum_g \Phi_q(|\hat V_{\mathrm{full}, g}|)$ | single-generator blow-up centres |
| T3 | $\sum_{i<j} z^2 \cdot \Phi_q(|\hat V_i \hat V_j|)$ | pair blow-up centres |
| **(T1+T2+T3)** | sum | full mass-endomorphism tower |

Path A reports T1+T4 explicitly (the per-vortex Frobenius co-Casimir
is a fourth term separate from the tower above). The proton row in
`six-term-mpfr-50dps.witness.json` quarantines:

| quarantined term | proton 50-dps value | reason |
|---|---|---|
| T2+T3 (brane tower) | `KeyError at A=1` | A=1 not in tower witness; "structurally empty under current level-selection rule" |
| T5 (chirality BW) | $-7.79$ | sign-indefinite, magnitude inflated, no known ansatz |
| T6 (Habiro residue) | $\sim 0.68$ | small tail correction; consistent with residue tail |

## What the numbers actually say

```
$ python3 computations/build_proton_mass_50dps_chain.py
target_value:  0.59741815 MeV
CODATA m_p:    938.27208816 MeV
rel_diff:      0.9994  (9.99363e+08 ppb; target 1 ppb)
```

So `(T1+T4)_p / (T1+T4)_e × M_E_MEV_CODATA = 0.5974 MeV`. The proton
under-shoots CODATA by a factor of ~1571. Equivalent statement: the
mass ratio $m_p / m_e$ from T1+T4 alone is **1.169**, not 1836.15.

Tightening the sanity threshold catches this. The bug PR #663 fixed —
the table reading `m_p_derived = 937.7615 MeV` — was reading from a
stale upstream witness from before the honesty rewrite, *not* from a
T1+T4 calculation that worked. So **no version of `mass_endomorphism.py`
ever made $m_p / m_e$ come out to 1836**; the previous "good" number
was a different formula (the LEGACY values `M_HECKE_PIPELINE_AT_Q0_LEGACY
= {"e": 0.0007783, "p": 1.4283}` whose ratio is 1835.8 — explicitly
labelled as "numerological placeholder (audit only)" in
`derivation_chain.py:225-228`).

## Three open R&D items to close the chain

### Item A — Reformulate or instantiate T2+T3 at A=1

The tower term `single + cross = Σ_g Φ_q(|V|) + Σ_{i<j} z² Φ_q(|V_i V_j|)`
relies on generator-pair structure. At A=1 the proton has 3 strands
(2 generators), so the sum has $\binom{2}{2} = 1$ pair — **not** empty.
The "KeyError at A=1" diagnostic suggests the *witness* file
`terms-2-3-atom-per-gen-mpfr-50dps.witness.json` doesn't tabulate A=1,
not that the formula is empty. Either:

1. **Regenerate the witness for A=1** — straight extension of the
   existing per-gen pipeline, only `mass-formula-6term-mpfr-50dps`'s
   exclusion of A=1 needs lifting.
2. **Adopt a different level-selection rule for A=1** — the brane-tower-Z-Habiro
   conjecture (open) may forbid A=1 brane levels; this would force
   T2+T3 = 0 structurally and shift the missing mass to T5/T6.

`computations/probe_proton_t2_t3_at_a1.py` (proposed) —
extend the per-gen pipeline to A=1, see what T2+T3 actually contribute.

### Item B — Structural ansatz for T5 (chirality BW)

T5 is currently sign-indefinite ($-7.79$ proton, $-7.47$ neutron),
magnitude order ~1. If $m_p / m_e \approx 1836$ comes from a tower with
T1+T2+T3 ~ 1 and T5 contributing the bulk, then T5 needs a structural
explanation: what categorical object is $-7.79$ at $q_0$ for the proton?

Candidate categorical sources:

- **Chiral anomaly contribution** at the Hecke/skein level (PR #527
  framework for chirality on the symmetric crystal)
- **Frobenius-Schur indicator** of the proton's representation in the
  3-strand Hecke algebra ($\mathrm{FS}(V_{(2,1)}) = +1$, so should
  contribute +1 not $-7.79$ — magnitude mismatch)
- **Half-twist scalar** $\Delta_3^2$ on $H_3$ ($\Delta_3^2$ at $q_0$
  is *order unity*, also wrong order)

None of these naturally produce $-7.79$. T5 may be a numerical artefact
of double-counting between T1+T2+T3 and the chirality channel — a
*subtractive* term that's accidentally being added. This needs careful
audit.

`computations/probe_t5_chirality_categorical_audit.py`
(proposed) — enumerate candidate categorical objects at 50 dps and
compare to $-7.79$.

### Item C — Re-examine T6 (Habiro residue) as the dominant term

T6 ~ 0.68 is "consistent with a residue tail" but **structurally
small**. If the actual $m_p / m_e$ comes from a 1835-fold enhancement,
T6 alone can't carry it. *Unless* T6 has a different role at A=1 vs
A≥2: maybe at A=1 the Habiro infinite series doesn't truncate the way
it does for compounds, and the full residue is much larger.

`computations/probe_t6_habiro_residue_full_series.py`
(proposed) — evaluate the full Habiro generating-function residue at
$q_0$ for the 3-strand proton braid without the residue-tail
truncation.

## What this audit does NOT propose

- **No fitting.** Restoring the LEGACY values $0.0007783 / 1.4283$ to
  match CODATA $m_p / m_e = 1836$ is exactly the numerology pattern
  the three-calibration discipline forbids.
- **No precision tightening before closure.** The 1 % sanity threshold
  is the *honest* signal of the gap; tightening it to 1 ppm just
  paints over a structural hole.
- **No new derivation chain.** The chain shape is correct; what's
  missing is content for steps 2/3 (T2+T3 derivation) and an explicit
  T5/T6 categorical attribution.

## Recommended sequence

1. **Item A** (probe T2+T3 at A=1) — cheapest, may close most of the
   gap if A=1 isn't actually structurally empty
2. **Item C** (full Habiro residue) — also cheap, well-localised
3. **Item B** (T5 categorical attribution) — open R&D, may require
   new categorical constructions

If A+C together close the chain to within ~1%, B becomes lower
priority (T5 may genuinely be a small correction). If A+C don't close
it, B is essential.

## Cross-references

- [PR #663](https://github.com/litlfred/qou/pull/663) — isotope-mass-table
  honest no-cal regen + the 1 % sanity guard
- [`build_proton_mass_50dps_chain.py`](../../computations/build_proton_mass_50dps_chain.py) — chain assembly
- [`derive_m_p_hecke_path_a.py`](../../computations/derive_m_p_hecke_path_a.py) — T1+T4 partial
- [`mass_endomorphism.py`](../../computations/mass_endomorphism.py) — `mass_from_tower(vols)` definition
- [`docs/audits/2026-05-10-non-calibrated-mass-state-of-play.md`](2026-05-10-non-calibrated-mass-state-of-play.md) — prior state-of-play
- [`docs/audits/2026-05-12-1ppb-implementation-plan.md`](2026-05-12-1ppb-implementation-plan.md) — 1ppb plan

## CAL discipline

Uses only CAL-1 ($m_e$ scale-fix) and CAL-2 ($q_0$). The CODATA m_p
appears only as a validation comparator (`M_P_MEV_VALIDATION`), never
as a prediction input. T5 audit will reference categorical objects on
$H_3$ at $q_0$, no experimental data.
