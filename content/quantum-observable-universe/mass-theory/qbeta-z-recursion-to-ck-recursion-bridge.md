**Proposition (forward form of the $z$-recursion).** *For any
`ZRecursionCoeffs` instance with Taylor coefficient sequence $a_n$,
and for $n \geq 1$,*

$$
  a_{n+1} = -\frac{3n}{2(n+1)} \cdot a_n
            -\frac{2n-1}{4(n+1)} \cdot a_{n-1}.
$$

*Equivalently, $a_{n+1}$ is a linear combination of $a_n$ and $a_{n-1}$
with $n$-dependent coefficients (kernel functions of $n$, NOT constant
in $n$).*

**Proof.** Algebraic rearrangement of the 3-term recursion
`4(n+1) · a_{n+1} + 6n · a_n + (2n-1) · a_{n-1} = 0` from
[`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
§Extension #5, dividing through by $4(n+1)$ (positive for $n \geq 0$).
The Lean proof is `field_simp` + `linarith` on the recursion equation.
$\square$

## Structural relationship to `CKRecursion`

The `QOU.QBeta.CKRecursion.CKRecursion ℝ` structure defined in
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
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

**Why the kernels differ.** The constant-kernel structure of
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
   the open f-map (cf. 1ppQ-Q$_\beta$ ledger). If the f-map identifies
   the Habiro element $F(q)$ whose Taylor coefficients are the $c_k$,
   and if $F(q)$'s $q$-difference equation has constant Laurent
   coefficients in $\xi$, then the resulting `CKRecursion ℝ` instance
   would inherit its kernel from $F$ — **not** from the $z$-recursion.
2. The $z$-recursion's role in this picture is **upstream auxiliary
   data**: the Markov parameter $z(q)$ enters $\Delta\tau_M(q)$
   through the canonical Wenzl weights $y_\lambda(q)$
   (see [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
   §Extension #4), and the $z$-Taylor expansion is what one would
   eventually convolve against the per-block characters to recover
   the f-map. The $z$-recursion is a structural input to the f-map
   derivation, not a substitute for the ladder $c_k$ recursion.

## What this block does NOT establish

- **A concrete `CKRecursion ℝ` instance.** That would require the
  open f-map identification (the 1ppQ-Q$_\beta$ keystone).
- **A formula for the $c_k$ in terms of the $a_n$.** Open, contingent
  on the f-map.

## Cross-references

- Parent block #1 (upstream):
  [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
  (`ZRecursionCoeffs` class).
- Parent block #2 (sibling on main):
  [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
  (`CKRecursion` structure).
- 1ppQ-Q$_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).
