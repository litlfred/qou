Proposition~[braiding-eigenvalue-extraction](#prop:braiding-eigenvalue-extraction)
extracts $q$ from the eigenvalues of $c_{V,V}$ and assigns
$q := \lambda_+$ (the eigenvalue on the symmetric summand $S^2 V$).
This labelling is a **convention**: one could equally define
$q := \lambda_- = -q^{-1}$.  The present choice is the
**inside-unit-circle convention**.

**Why $\lambda_+$ and not $\lambda_-$.**  The
[substrate parameter existence](#prop:substrate-parameter-exists)
proof requires $q > 1$ over $\mathbb{R}$ (the `field_ge_one`
positivity axiom).  Under the Hecke relation
$(T - q)(T + q^{-1}) = 0$, the eigenvalue $\lambda_+= q$ lies
*outside* the unit circle when $q > 1$, while $\lambda_- = -q^{-1}$
lies inside.  Defining $q := \lambda_+$ is therefore equivalent to
choosing the eigenvalue of larger absolute value — the one that
controls the asymptotic growth of the braiding representation.

**Effect on the Hecke relation.**  The two eigenvalues satisfy
$\lambda_+ \cdot \lambda_- = -1$ (determinant condition), so
swapping them replaces $q$ by $-q^{-1}$.  The Hecke relation
$(T-q)(T+q^{-1}) = 0$ is manifestly asymmetric in $\lambda_+$
and $\lambda_-$; the choice $q := \lambda_+$ is the one that
makes the symmetric summand eigenvalue positive (for real $q > 1$)
and compatible with the standard orientation of the Kauffman bracket.

**No mathematical content changes.**  This is a naming convention:
the braiding endomorphism $c_{V,V}$ and the Hecke relation are fixed
by the category.  Choosing $q := \lambda_+$ simply fixes which of the
two eigenvalues receives the name ``$q$'', consistently with the
[substrate parameter](#def:substrate-parameter) and the physical
positivity axiom.
