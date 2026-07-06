**Proof.** The $q$-Bessel function satisfies a second-order $q$-difference
equation whose coefficient recurrence is the companion of the first-order
contiguity relation. The equation and the recurrence it induces on the
power-series coefficients are established formally and verified
computationally, including the classical $q \to 1$ Bessel limit.

**Formalization.** The second-order recurrence
`QOU.QBeta.qbessel_second_order_recurrence` is proved sorry-free in
[`QBesselContiguityRecurrence.lean`](../lean/QOU/QBeta/QBesselContiguityRecurrence.lean),
algebraically in $q$.

**Computation.** The script
[`qbessel_second_order_qdifference_equation.py`](../../../computations/qbeta/qbessel_second_order_qdifference_equation.py)
verifies the second-order $q$-difference equation for the $q$-Bessel
function and its limits (witness
[`qbessel-second-order-qdifference-equation.witness.json`](../../../computations/qbeta/qbessel-second-order-qdifference-equation.witness.json)).

Fibre-level structural result (formal $q$); it claims no $Q_\beta$ or
binding scale, and the production $c_k$ ladder remains calibration-anchored.
