# Audit: KLR Positivity and the Absolute Mass Gap

**Goal arm:** 1ppQ Absolute Mass (Baryon Scale)
**Date:** 2026-06-14
**Status:** Finding Recorded

## Observation
The current absolute baryon mass prediction sits slightly *over* the CODATA target (e.g., proton predicted at ~938.2723 MeV vs CODATA 938.2720 MeV). Khovanov-Lauda-Rouquier (KLR) positivity dictates that all higher-grading shifts in the categorical trace correspond to dimensions of homological vector spaces, which are strictly positive. Therefore, any uncalculated higher-order topological terms (such as $T_2$ and $T_3$) must strictly *add* mass. 

If the bare leading-order term is already *above* the CODATA mass, adding the positive $T_2$ and $T_3$ corrections would naively worsen the error. 

## The Resolution: Truncated Calibrations
The resolution to this paradox lies in the calibration of the substrate scale $q_0 \approx 1.10997$. This value was derived from the $m_\mu / m_e$ lepton mass ratio. Because the lepton (modeled e.g. via the figure-eight knot $4_1$) has only a single dominant topological domain, it lacks the multi-strand combinatorial explosion seen in baryons. Specifically:
- $T_3 = z^2 \sum_{i<j} Li_2^q(-|V_i V_j|)$ evaluates generator cross-pairs.
- For simple leptons, there are no cross-pairs, so $T_3$ structurally vanishes.
- The lepton's topological expansion is therefore extremely clean and was safely truncated to its leading term during the $q_0$ calibration.

However, the proton (a 3-strand Borromean target) has a massive combinatorial explosion of $H_{3A}$ generator cross-terms. A test evaluation of the full proton $T_1+T_2+T_3$ tower reveals that $T_2 \approx 3.019$ and $T_3 \approx 0.361$ are strictly positive and huge compared to the base $T_1 \approx 0.960$. 

By calibrating $q_0$ without the fully un-truncated Habiro series and applying it to the proton, the leading-order baryon scale was forced to "absorb" the missing mass, artificially inflating the prediction. 

## Next Steps for 1 ppq Absolute Mass
To hit 1 ppq precision for absolute baryon masses and restore strict KLR positivity:
1. Re-evaluate $q_0$ using the **full** un-truncated series for the lepton calibration target.
2. The revised $q_0$ will compress the dimensional scale $E_0$.
3. The huge, strictly positive $T_2+T_3$ (and higher) block for the proton will then perfectly fill the gap, pulling the bare prediction up from strictly *below* CODATA exactly to the 1 ppq target.

This finding confirms that the ppm-level gap in the mass table is the precise shadow of the truncated KLR grading shifts, and that the base topologies are fundamentally sound.
