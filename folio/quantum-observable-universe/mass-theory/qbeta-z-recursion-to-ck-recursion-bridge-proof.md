**Proof.** Algebraic rearrangement of the 3-term recursion
`4(n+1) · a_{n+1} + 6n · a_n + (2n-1) · a_{n-1} = 0` from
[Per-block character closed forms for $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$](../mass-endomorphism/qbeta-per-block-chi-closed-forms.md)
§Extension #5, dividing through by $4(n+1)$ (positive for $n \geq 0$).
The Lean proof is `field_simp` + `linarith` on the recursion equation.
$\square$

## Structural relationship to `CKRecursion`

The `QOU.QBeta.CKRecursion.CKRecursion ℝ` structure defined in
[$c_k$ precision-ladder recursion induced by the fibre-level Habiro $q$-difference equation](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
captures the **constant-kernel** depth-$d$ linear recursion

$$
  c_{k+1} = \sum_{j=0}^{d-1} \text{kernel}(j) \cdot c_{k-j}
$$

where `kernel : Fin d → ℝ` is a fixed coefficient vector independent
of $k$. The $z$-Taylor recursion above also has depth 2 in the sense
that each step uses two prior coefficients ($a_n$ and $a_{n-1}$),
but its kernel coefficients depend on $n$:

| Property | `CKRecursion` | $z$-Taylor recursion |
|---|---|---|
| **Depth** | $d$ (fixed) | 2 |
| **Kernel** | `Fin d → R` (constant) | $n \mapsto (\text{Fin 2} \to \mathbb{R})$ (variable) |
| **Linear in history** | Yes (proven, `applyRecursion_linear`) | Yes (state-dependent linear) |

**Origin of the kernel difference.** The constant-kernel structure of
`CKRecursion` reflects a fibre-level Habiro element whose
$q$-difference equation $F(q \xi) = R(q, \xi) \cdot F(\xi)$ has a
Laurent polynomial $R$ of fixed degree $d$; the change-of-basis from
the Habiro $(u; u)_m$ ring to the ladder $u^k$ inherits the constant
kernel. The $z$-Taylor recursion, by contrast, is the descent of a
**second-order linear ODE with rational coefficients** for
$z(q) = \sqrt q / (1 + q)$ around $q = 1$; the ODE's
polynomial-in-$q$ coefficients become polynomial-in-$n$ recursion
coefficients under Taylor expansion.

**Bridge to closure.** A literal `CKRecursion ℝ` instance cannot be
constructed from a `ZRecursionCoeffs` instance alone (the kernel
shapes differ). However:

1. The Q$_\beta$ ladder $c_k$ — which `CKRecursion` ultimately
   describes — is conjectured to be expressible in the $z$-basis via
   the open f-map. If the f-map identifies
   the Habiro element $F(q)$ whose Taylor coefficients are the $c_k$,
   and if $F(q)$'s $q$-difference equation has constant Laurent
   coefficients in $\xi$, then the resulting `CKRecursion ℝ` instance
   would inherit its kernel from $F$ — **not** from the $z$-recursion.
2. The $z$-recursion's role in this picture is **upstream auxiliary
   data**: the Markov parameter $z(q)$ enters $\Delta\mathrm{tr}_M(q)$
   through the canonical Wenzl weights $y_\lambda(q)$
   (see [Per-block character closed forms for $\chi_\lambda(\Delta_{T_\beta})(q)$ over $H_3(q)$](../mass-endomorphism/qbeta-per-block-chi-closed-forms.md)
   §Extension #4), and the $z$-Taylor expansion is what one would
   eventually convolve against the per-block characters to recover
   the f-map. The $z$-recursion is a structural input to the f-map
   derivation, not a substitute for the ladder $c_k$ recursion.

## Claims not established here

- **A concrete `CKRecursion ℝ` instance.** That would require the
  open f-map identification.
- **A formula for the $c_k$ in terms of the $a_n$.** Open, contingent
  on the f-map.
