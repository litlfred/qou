# Paper discrepancy — ρ vs ρ_K in the mass formula

**Branch**: `claude/isotope-mass-witness-data-x5lCh`
**Status**: CRITICAL — explains the 173× missing factor in m_p prediction
**Owner ask**: "make sure ρ is actually correct. do we need ρ_knot or
are these different?" + "may be discrepancies in paper. be critical"

## The discrepancy

The paper uses TWO different symbols named "ρ" for the prefactor in
the mass formula, and they refer to **different mathematical
quantities** with **different empirical values**:

| Symbol | Source | Type | proton value | Definition |
|---|---|---|---:|---|
| **ρ** | [`atom-knot-mass-derivation.md`](../../content/quantum-observable-universe/braids-and-knots/atom-knot-mass-derivation.md) line 13 | integer ∈ ℤ_>0 | **1** | "multiplicity of $T_w$'s SDP solution in the Wedderburn decomposition" |
| **ρ_K** | [`atomic-mass-gb-nf.md`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md) line 51 | scalar ∈ ℝ_>0 | **1723.6** | "categorical density" — `ρ_K = M(K)/(m_e · |tr_M(NF_GS(β_K))|)` |

**The two are NOT the same quantity.** ρ_K can be ~1700× larger than ρ.

## Two incompatible formulas for M(𝔥)

### Formula 1 — atom-knot-mass-derivation.md line 13-52

> $M(\mathfrak{H}) := \rho \cdot m(\mathfrak{H}) = \rho \cdot \bigl[\,|\text{tr}_M(T_w)| + \text{tower}(T_w) + \text{tr}_M(C_{\dim_q})\,\bigr]$

> $B(\mathfrak{H}) = m_e \cdot M(\mathfrak{H}) = m_e \cdot \rho \cdot \text{tr}_M(T_w)$

For the proton: ρ = 1, m(𝔥) = T1 + T2 + T3 + T4 + T5 + T6 = 10.59 cat
- M(𝔥) = 1 · 10.59 = 10.59 cat
- B(𝔥) = 0.511 · 10.59 = **5.41 MeV**
- vs CODATA 938.27 MeV → residual **−99.42 %**

### Formula 2 — atomic-mass-gb-nf.md line 32, 50-54

> $\mathcal{M} = m_e \cdot \rho_K \cdot |\text{tr}_M(\text{NF}_{GS}(\beta_K))|$

> $\rho_K = \frac{\mathcal{M}(K)}{m_e \cdot |\text{tr}_M(\text{NF}_{GS}(\beta_K))|}$

For the proton: ρ_K = 1723.6 (CODATA-fit), |tr_M(NF_GS)| = 1.0653
- M_pred = 0.511 · 1723.6 · 1.065 = **938.27 MeV** (by construction)
- vs CODATA 938.27 MeV → residual **0 %** (by definition — circular)

### Reconciliation attempt

If both formulas are simultaneously correct, then:

$$m_e \cdot \rho_K \cdot T_1 = m_e \cdot \rho \cdot (T_1 + T_2 + \ldots + T_6)$$

$$\rho_K = \rho \cdot \frac{T_1 + T_2 + \ldots + T_6}{T_1}$$

For the proton with ρ = 1 and m_hecke / T_1 = 10.59 / 0.96 = 11.0:
- ρ_K_predicted = 1 · 11.0 = **11.0**
- ρ_K_CODATA = **1723.6**
- Discrepancy: **factor of ~157×**

Note also that the paper's `|tr_M(NF_GS)| = 1.0653` for the proton
differs from this branch's T1 = 0.9604 by ~10% — a separate
Wedderburn-weight-convention mismatch (Plancherel-normalised vs
unnormalised Wenzl).

## Paper acknowledges the open problem

[`atomic-mass-gb-nf.md`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md) **line 71 explicitly states**:

> "**Open question: categorical derivation of ρ_K**"

And the empirical table at line 60-67 shows ρ_K growing super-linearly
in A:

| Atom | A | \|tr_M(NF_GS)\| | M_CODATA | ρ_K_CODATA |
|---|---:|---:|---:|---:|
| proton | 1 | 1.0653 | 938.272 | 1723.6 |
| neutron | 1 | 0.9232 | 939.565 | 1991.6 |
| D | 2 | 0.3883 | 1875.613 | 9453.0 |
| T | 3 | 0.1041 | 2808.921 | 52828.5 |
| ³He | 3 | 0.2065 | 2808.392 | 26609.2 |

ρ_K(T) / ρ_K(³He) = 1.9853 exactly compensates
|tr_M(³He)| / |tr_M(T)| = 1.9850, so ρ_K is **mirror-symmetric**
(per line 107-114) and depends on the specific braid β_K — NOT
just on (A, n_strands).

The graded ρ_K expansion (line 80-86) attempts to split ρ_K · |tr_M(β_K)|
into LO + binding-correction pieces:

$$m_e \cdot |tr_M(β_K)| \cdot ρ_K = \underbrace{Z m_p + N m_n + Z m_e}_{\text{LO}} + \underbrace{α \sum_i \ln|\hat{V}_i|}_{\text{single-gen}} + \underbrace{α z^2 \sum_{i<j} \ln|\hat{V}_i \hat{V}_j|}_{\text{pair-gen (OPEN)}} + \ldots$$

The **LO piece is "proved"** via Wenzl 1988 Markov multiplicativity for
disjoint braids; **single-gen takes ρ_K to 0.18% mean across Z=1..20**
([atomic-braid-mass](../../content/quantum-observable-universe/braids-and-knots/atomic-braid-mass.md));
**pair-gen and higher are explicitly OPEN**.

So:
- **m_p prediction at LO (Wenzl-proved)** = m_p_CODATA / m_e · m_e = m_p_CODATA (trivially CODATA, because the LO piece uses m_p_CODATA as input)
- **m_p prediction at single-gen** = m_p_CODATA + α·Σ ln|V̂_i| correction (0.18% accurate)

The framework's **m_p_pred = m_p_CODATA by construction at LO**;
the single-gen correction is what's "proved" to 0.18% accuracy.

## Critical reading

The paper has TWO MUTUALLY INCONSISTENT formulas for M(𝔥):

1. `atom-knot-mass-derivation.md`: M(𝔥) = ρ · m(𝔥) with ρ ∈ ℤ_>0
   (the SDP multiplicity, = 1 for proton). Predicts m_p ≈ 5 MeV.
   **Does not match CODATA.**

2. `atomic-mass-gb-nf.md`: M = m_e · ρ_K · |tr_M(β_K)| with ρ_K ∈ ℝ_>0
   (empirical "categorical density", = 1723.6 for proton, CODATA-fit).
   Matches CODATA **by construction**.

The graded ρ_K expansion (3rd form) decomposes ρ_K · |tr_M|·m_e into
LO constituent sum + corrections. **LO uses m_p_CODATA as input,
so it's circular as a derivation; the corrections are 0.18% accurate
at single-gen level, with pair-gen onwards OPEN.**

**This means**:

- The "m_p_pred = 5.41 MeV (99.42% residual)" that this branch's
  Li_2^q + *_q compound tower reports is **the prediction under
  Formula 1**, where ρ = 1 and the brane tower is computed from
  first principles.

- The 173× missing factor is **exactly ρ_K** under Formula 2.

- **ρ_K is acknowledged open** in the paper.  The framework's
  categorical derivation of m_p (without using m_p_CODATA as input
  via ρ_K = M_CODATA/(m_e·|tr_M|)) **is not closed**.

## Recommendations

### For the audit

This discrepancy is the **structural root** of the 173× missing
factor in this branch's m_p_pred. It is NOT a bug in the
implementation — the implementation correctly applies Formula 1.

### For the paper

1. **Disambiguate notation**: `ρ` and `ρ_K` should have distinct
   symbols (e.g., `μ_SDP` and `ρ_cat`).

2. **Mark the two formulas explicitly**: state which one is the
   "operational predicting" formula and which is "calibration
   bookkeeping". As written, both look like first-principles
   predictions; only Formula 1 actually is, and it doesn't close.

3. **Surface the open problem**: ρ_K's categorical derivation is
   the unresolved structural piece. The paper does say so (line
   71 of `atomic-mass-gb-nf.md`) but the headline framing in
   `atom-knot-mass-derivation.md` makes M(𝔥) = ρ · m(𝔥) look
   complete with ρ = SDP multiplicity. This invites confusion.

4. **The "0.18% accuracy" claim** of the single-gen correction
   (line 102 of `atomic-mass-gb-nf.md`) needs auditing — does
   it use m_p_CODATA as an input via the LO piece? If so, the
   accuracy is a self-consistency check, not a prediction.

### For follow-up implementation

To close the m_p categorical derivation:

1. **Derive ρ_K from first principles** — the unresolved task.
2. **Or**: re-interpret the brane tower as a *correction* to the
   constituent calibration LO sum, where m_p_CODATA is allowed as
   input (i.e., abandon the "no CODATA inputs except CAL-1/2/3"
   discipline for m_p_pred). This is a calibration choice.
3. **Or**: switch CAL-1 from m_e to m_p, then derive m_e =
   m_p_CODATA / ratio_pred. Trade-off: ρ_K would need re-derivation
   under m_p anchor.

## Audit cross-references

- [INDEX](2026-05-16-compute-paper-lean-audit-INDEX.md) GAP #19
  (mass-endomorphism tower drift) — this discrepancy is the
  upstream root cause.
- [hydrogen row provenance](2026-05-17-hydrogen-row-provenance.md)
  — per-row trace under Formula 1.
- PR #663 status: m_p_pred under Formula 1 reports 99.42% residual.
  This is HONEST framework state pending ρ_K derivation.
