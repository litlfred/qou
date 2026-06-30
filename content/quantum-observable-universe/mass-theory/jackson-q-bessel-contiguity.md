**Proof.** The first- and second-kind Jackson $q$-Bessel functions
$J_\nu^{(1)}(x;q)$ and $J_\nu^{(2)}(x;q)$ have power-series coefficients
$c_k$ satisfying purely algebraic first-order contiguity recurrences in the
order $\nu$, with a closed-form coefficient ratio. The recurrence is
established by formalization and cross-checked computationally.

**Formalization.** The closed forms are
`QOU.QBeta.qbessel_first_kind_coeff_closed_form` and
`qbessel_second_kind_coeff_closed_form` in the sorry-free file
[`QBesselContiguityRecurrence.lean`](../lean/QOU/QBeta/QBesselContiguityRecurrence.lean).
The recurrence is algebraic in the deformation variable $q$; no archimedean
input enters.

**Computation.** The script
[`qbessel_jackson_contiguity.py`](../../../computations/qbeta/qbessel_jackson_contiguity.py)
verifies that the closed-form coefficient ratios equal the actual Jackson
coefficient ratios symbolically for all $k \le 6$ and to $60$ decimal
places, and that the $q$-hypergeometric product solution reproduces the
coefficients
(witness [`qbessel-jackson-contiguity.witness.json`](../../../computations/qbeta/qbessel-jackson-contiguity.witness.json)).

This is a fibre-level (formal-$q$) structural identity fixing the
$SU_q(1,1)$ radial coefficient algebra; it claims no $Q_\beta$ or binding
scale, and the production $c_k$ ladder remains calibration-anchored.
