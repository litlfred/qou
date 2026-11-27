The NF decomposition of a knot operator determines which
particle channel it opens on a given incoming pair — in
particular whether its $e^-$ coefficient is nonzero, i.e.
whether it produces the electron channel. Tabulating these
decompositions is therefore what realises the operator/channel
selection that this appendix examines.

This appendix gives the complete NF decomposition of
$b_i \cdot \beta(T) \cdot b_j$ for every pair of NF basis
elements and every tabulated operator $T$, **symbolic in
$h = q - q^{-1}$**.  All results are exact in $q$ — numerical
values appear only in the witness file for comparison at $q_0$.

**Notation.**  $h = q - q^{-1}$ (Hecke amplitude).  The NF basis
is $\{\ \gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\ \}$,
with $e^- = \sigma_0\sigma_1\sigma_0$.  An operator is named by the
closure of its braid word $\beta(T)$: $T_{2,n}$ is the word
$\sigma_0^n$ in the two-strand braid group $B_2$, whose closure is
the $(2,n)$ torus knot or link, and $T_{2,n}^{(3)}$ is a word in the
three-strand braid group $B_3$ whose closure is the same
$(2,n)$ torus link.  Two such words are used: $\sigma_0\sigma_1\sigma_0$,
whose closure is the Hopf link $T(2,2)$, and $(\sigma_0\sigma_1)^2\sigma_0$,
whose closure is the $T(2,4)$ torus link.  Both closures have two
components, as every odd-length word in $B_3$ does.

---

## Table L.1: NF basis multiplication table ($T_{1,0}$ — identity operator)

The identity operator $\beta(T_{1,0}) = \mathbf{1}$ gives
the raw product $b_i \cdot b_j$.  Every entry below is **exact
in $h$**.

See [Table 1](#tbl:knot-operator-basis-table-table1-data).

**Key observations:**

1. **$e^-$ channel universality under $T_{2,2}^{(3)}$**: When the
   electron operator $\beta(T_{2,2}^{(3)}) = e^-$ is inserted, the
   $e^-$ coefficient is always nonzero (36/36 pairs).  In contrast, under the
   identity operator $T_{1,0}$, only 19/36 pairs produce a nonzero
   $e^-$ coefficient, leaving the channel closed for the remaining
   pairs.

2. **$e^- \cdot e^- = \gamma + h\sigma_0 + h\sigma_1 + h^2 L_+ + h^2 L_- + (h^3+h)e^-$**:
   the self-product of the electron populates all six basis
   elements.  The $e^-$ coefficient is $h^3 + h = h(h^2 + 1)$,
   which is always positive for $q > 1$.

3. **No negative coefficients** appear in any basis product.
   Negative NF coefficients arise only from inverse elements
   ($\sigma_i^{-1}$), i.e., antiparticles.

---

## Table L.2: $T_{2,2}^{(3)}$ operator (electron)

$\beta(T_{2,2}^{(3)}) = \sigma_0\sigma_1\sigma_0 = e^-$, whose
closure in $B_3$ is the Hopf link.

The product $b_i \cdot e^- \cdot b_j$ is computed by composing
the $T_{1,0}$ table entries.  Key entries (symbolic in $h$):

See [Table 2](#tbl:knot-operator-basis-table-table2-data).

**All 36 pairs produce nonzero $e^-$ coefficient under $T_{2,2}^{(3)}$.**

The electron operator **unconditionally opens the electron
channel** regardless of the incoming state, confirming
$T_{2,2}^{(3)}$ as the universal pair-production operator.

---

## Table L.3: $T_{2,1}$ operator (single crossing)

$\beta(T_{2,1}) = \sigma_0$.

See [Table 3](#tbl:knot-operator-basis-table-table3-data).

**24/36 pairs produce $e^-$ under $T_{2,1}$** — but the
photon-photon pair ($\sigma_0 \cdot \sigma_0 \cdot \sigma_0$)
does **not**.  $T_{2,1}$ requires specific polarization content
to open the electron channel.

---

## Summary: operator channel opening

See [Table 4](#tbl:knot-operator-basis-table-table4-data).

$T_{2,2}^{(3)}$ is the **unique lowest-crossing operator that
unconditionally produces the electron channel for all incoming
pairs**.  Higher operators ($T_{2,4}^{(3)}$, etc.) also open all
channels but at higher crossing energy cost ($h^2$ vs $1$
for the photon-photon pair).
