**Proposition (the three calibrations are the three cohomological data).**

The first cohomology of Bring's curve is $H^1 = 2W$ (rank $8$, two copies of
the irreducible $4$-dimensional $S_5$ representation $W$;
[`prop:prolonged-periods-fixed-depth`](#prop:prolonged-periods-fixed-depth)).
Its polarised Hodge structure has exactly **three** real degrees of freedom
that survive as observable units once the archimedean functor $\tau$ is applied:

| cohomological datum | calibration | channel |
|---|---|---|
| **scale** of the rank-2 $W$-Hodge plane $= a_D^{(e)}$ | CAL-1 $m_e$ ([`prop:electron-period-base`](#prop:electron-period-base)) | $h^0$ prefactor |
| **modulus** of that plane $=$ SL$_2$ trace $\tau = 2\cosh\theta$ | CAL-2 $q_0$ ([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)) | cosh / bar-even |
| **scale** of the $\operatorname{Vol}(\mathrm{Hopf})=0$ meson sector | CAL-3 $m_\pi$ | orthogonal class |

The rank-2 $W$-Hodge plane carries two invariants — a scale and a modulus — and
the meson sector (whose Hopf-link complement has zero hyperbolic volume, hence
no geometric scale derivable from $(m_e, q_0)$ — the meson scale-independence) contributes a third, orthogonal
scale: $2 + 1 = 3$, matching the three calibrations exactly. The alignment is
therefore not a coincidence of counting but the statement that **the three
calibration inputs are precisely the three undetermined cohomological data of
the Bring Hodge structure** — the choice of units forced at the
substrate-to-archimedean wall.

The Lean witnesses
[`QOU.Mass.calibrations_eq_cohomology`](#prop:calibration-cohomology-alignment)
(the calibration triple equals the cohomological triple) and
`cohomology_data_count` ($2+1=3$) record the correspondence and the count.
