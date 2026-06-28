**Remark (isospin midpoint).**
The value $h/2 = (q - q^{-1})/2$ is the arithmetic mean of the
symmetric eigenvalue $q$ and the antisymmetric eigenvalue $-q^{-1}$
of the Hecke generators.  Self-conjugate partitions sit at the
exact isospin midpoint of the Hecke spectrum.

**Remark (pn invisibility).**
The per-crossing trace contribution in the $[3,2,1]$ representation
is:

| Crossing type | Coefficient $d$ | $\mathrm{tr}(\sigma + d \cdot I)/\dim$ |
|:---:|:---:|:---:|
| $pp$ | $0$ | $h/2$ |
| $nn$ | $-h$ | $-h/2$ |
| $pn$ | $-h/2$ | $0$ |

The proton-neutron crossing is **invisible** to $[3,2,1]$: its
trace contribution $h/2 - h/2 = 0$ vanishes exactly.  Only
$pp$ ($+h/2$) and $nn$ ($-h/2$) crossings contribute, with
opposite signs.

Consequently the $[3,2,1]$ BW scaling is

$$
  S_{[3,2,1]}(Z,N) = \frac{(Z - N)(A - 1)}{A^{4/3}}
$$

where $(Z{-}N)(A{-}1) = Z(Z{-}1) - N(N{-}1)$ counts the net
$pp$ minus $nn$ crossing asymmetry, NOT the isospin Casimir
$T(T{+}1)$.  This is why $\chi_{[3,2,1]}$ vanishes for deuterium
(pure $pn$) and ${}^3\mathrm{He}$ (where the single $pp$
crossing's contribution is cancelled by the full matrix
product structure at second order in $h$).

**Remark (character structure).**
The nuclear character $\chi_{[3,2,1]}$ has universal factor
$h^2 \cdot \Phi_6(q^2)$ where $\Phi_6(q^2) = q^4 - q^2 + 1
= (q^6 + 1)/(q^2 + 1)$ is the 6th cyclotomic polynomial evaluated
at $q^2$.  The $h^2$ factor encodes the isospin sensitivity (the
character vanishes at $q = 1$, i.e., in the classical limit).
