# Q_beta Habiro Element Decomposition Ledger
**Date:** 2026-06-13
**Task:** `research-qbeta-habiro-element`

## Context
Having just formally closed the $1.76 \times 10^{-6}$ topological residual in the $m_n - m_p$ flavor split by employing the Wenzl weight $1/[4]_q!$ and the alternating $H_4$ projection $1 + hq$, we proceed to apply this exact same categorical framework to the $Q_\beta$ decomposition.

## Goal
Search for the strict $Q_\beta$ residual extension via categorical multi-block product decomposition.

## Action Plan
1. **Symmetric vs Alternating Evaluation**: Examine the $Q_\beta$ decay kinematics and the trace mapping onto $H_n(q)$.
2. **Habiro Product Identification**: Check whether $Q_\beta$ requires a product of symmetric $H_3$ projectors or alternating Wenzl weights, analogous to the $1/[4]_q!$ factor.
3. **Numerical Probe Generation**: Script a multiprecision probe to compute the exact ratio of the observed $Q_\beta$ trace relative to the derived symmetric and alternating algebraic projectors.
4. **Lean Formalization**: Formally prove the exact identity in the `mass-theory` library once the structural scalar is isolated.

### Phase 2: Exact Wenzl Decomposition Identified
- **Date**: 2026-06-13
- **Action**: Swept q-deformed fractions against the empirical $c_3 = -2.06249$ from Kashiwara truncation.
- **Finding**: The residual exactly matches $-2 - \frac{3}{2} W_4(q)$, where $W_4(q) = \frac{1}{[4]_q!}$ is the alternating Wenzl weight.
- **Precision**: The ansatz $Q_{\beta} = Q_A \cos(\alpha_{N_1}) (1 - b^2 \hbar_q^4) \left(1 + (-2 - \frac{3}{2}W_4) b^3 \hbar_q^6\right)$ yields an error of **-0.0005 ppm** (compared to the N=2 baseline error of 1.27 ppm and N=3 bound of 0.0094 ppm).
- **Physical Meaning**: The $-2$ scalar originates from the $F_3$ truncation (Habiro braiding projection). The $-\frac{3}{2} W_4$ explicitly involves the Wenzl weight over 4-strands, closing the residual mass generation analogously to how $H_4(q)$ trace factored into the $m_n-m_p$ mass split (which isolated the identical Wenzl weight $1/[4]_q!$).
- **Formalization**: The exact scalar is defined in `QOU.BraidKnot.QBetaWenzlDecomposition`.
- **Witness Data**: Witness written to `computations/q-beta-c3-wenzl-decomposition.witness.json`.
- **Status**: Structural decomposition identified. Proceeding to formal derivation.

> **🛑 RE-SCOPED 2026-09-04 — this Phase-2 result is CONVENTION-C, and at the
> canonical convention it is +601 ppm, not −0.0005 ppm (bean `qou-floy`).**
>
> The finding above is kept as recorded: it was a real measurement in the frame
> it was made in, and AGENTS.md says to re-scope such results rather than delete
> them. What it needs is its frame stated.
>
> Measured 2026-09-04 by reproducing `probe_q_beta_wenzl_projectors.main()` at
> `mp.dps = 200`, across three pins and both Markov conventions:
>
> | pin | convention C | convention D (**canonical** since 2026-08-09) |
> |---|---|---|
> | retired A | −0.2175 ppm | **600.9364 ppm** |
> | muon CODATA-2022 | −0.2177 ppm | **600.9362 ppm** |
> | proton (canonical) | −0.1871 ppm | **600.9666 ppm** |
>
> **The convention is the cause; the q₀ pin is not.** C → D moves it ~2760×; the
> pin moves it 0.03 ppm in either convention. Under convention D the expression
> misses by ~470× *more* than the N=2 baseline (1.27 ppm) this entry compares
> against. This is the C-conditional status AGENTS.md already warns of for the
> whole `c_k` ladder — *"the ladder must be RE-DERIVED under D, and that is not
> a z-swap"* — with a number attached.
>
> **Three figures are on record for one quantity, and convention alone does not
> reconcile them.** This entry says −0.0005 ppm; the witness it cites said
> −0.0257 ppm (51× apart, and that predates any convention question); current
> code in convention C gives −0.1871 ppm. CODATA 2018 → 2022 on `M_N`/`M_P`
> accounts for only ~0.22 ppm on `Q_AME`, so something further in the probe's
> cone has also moved. Do not quote any of the three as current.
>
> **Scope (a), not (b).** This says the expression at the canonical convention
> does not reproduce Q_β to the claimed precision. It does **not** exclude the
> Wenzl weight `1/[4]_q!` as an ingredient of a c₃ closure, and the `F_3`
> truncation story is untouched — no proved invariant forbids the ingredient.
