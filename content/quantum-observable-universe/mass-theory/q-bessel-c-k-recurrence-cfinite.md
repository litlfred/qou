**Proof.** The power-series coefficients $c_k$ of the $q$-Bessel function
satisfy a first-order ($C$-finite / $q$-holonomic) recurrence, with the
closed form for the general coefficient fixed by the recurrence together
with its initial term.

**Formalization.** The closed-form coefficient
`QOU.QBeta.qbessel_coeff_closed_form` and the first-order recurrence it
satisfies are proved sorry-free in
[`QBesselContiguityRecurrence.lean`](../lean/QOU/QBeta/QBesselContiguityRecurrence.lean),
algebraically in $q$.

**Computation.** The script
[`qbeta_qbessel_contiguity_cfinite.py`](../../../computations/qbeta/qbeta_qbessel_contiguity_cfinite.py)
checks the $q$-holonomic structure of the recurrence against the canonical
coefficient values (witness
[`qbeta-qbessel-contiguity-cfinite.witness.json`](../../../computations/qbeta/qbeta-qbessel-contiguity-cfinite.witness.json)).

This is the fibre-level ($q$-holonomic) skeleton of the recursion; it does
not by itself pin a $Q_\beta$ scale, and the production $c_k$ ladder stays
calibration-anchored (per the $c_k$ truncation-order framing).
