# η²-fibre descent: bean 0zr0's prediction CONFIRMED exactly (margin 9); naive cosh normalization refuted

**Date:** 2026-07-04
**Branch:** `claude/parabolic-cylinder-channels-fh08ia` (restarted post-#3284)
**Probe:** [`qbeta_eta_square_fibre_probe.py`](../../computations/qbeta/qbeta_eta_square_fibre_probe.py)
(witness `qbeta-eta-square-fibre-probe.witness.json`; exact
$\mathbb{Q}(\sqrt3)$ arithmetic, ORD = 17, 08ds conventions; 16 s).

## What was tested

Bean `0zr0`'s formalize-first scoping (2026-07-03), executed. Inputs: the
ζ4-partner Lean (`ComplexVolumeZeta4Partner` — the rotation
$z \mapsto z + i\pi/2$ negates the bar-even channel, keeps bar-odd) and the
08ds ORD-17 exact bar-split of the net-route $\log R$ into $E$ (bar-even) and
$O$ (bar-odd). Model: $(E, O)$ descend from one complex fibre $F(\eta)$ with a
bar-odd argument $\eta(s)$ (η(s)). Two exact parameter-free consequences:

- **(A)** unit-normalized cosh/sinh identification
  ($E = \cosh\eta - 1$, $O = \sinh\eta$) forces the Pythagorean identity
  $P := E^2 + 2E - O^2 = 0$;
- **(B)** the bean's core prediction: $\eta := \operatorname{arcsinh}(O)$
  (exact series $\log(O + \sqrt{1+O^2})$) is bar-odd, and $\eta^2$ lies in
  the bar-even algebra $\mathbb{Q}(\sqrt3)[[\tilde u]]$ (u~-series).

## Results

| test | verdict | detail |
|---|---|---|
| (A) Pythagorean | **refuted at order $s^2$** (scope-(a)) | the specific unit-normalized $\cosh$ relation is not how $E$ sits over $\eta$ |
| (B0) $\eta$ bar-odd | **exact, all orders ≤ 17** | $\eta + \bar\eta = 0$ identically |
| (B) $\eta^2 \in \mathbb{Q}(\sqrt3)[[\tilde u]]$ | **exact, margin 9** | 8 rungs solved (first two vanish; $\eta^2 = 11.9286\ldots\tilde u^3 + 240.700\ldots\tilde u^4 + \cdots$), all 9 held-out orders vanish identically |

## Reading

**The fibre-descent structure is real.** The bar-odd channel $O$ determines,
with no free parameters, a bar-odd argument $\eta$ whose square lands
*exactly* in the same bar-even $\tilde u$-algebra that $E$ (08ds) lives in —
the precise sense of "E and O are even/odd parts of one fibre" predicted
before matching. A 17-order exact confirmation with 9 over-determined orders
is not a numerical coincidence class: the identities hold in
$\mathbb{Q}(\sqrt3)$.

**What (A)'s failure adds:** the fibre is not $\exp(\eta)$-normalized — $E$
is some *other* element of $\mathbb{Q}(\sqrt3)[[\tilde u]]$ over the same
$\eta^2$ generator. The next constraint is functional: identify
$E = G(\eta^2)$ with $G \in \mathbb{Q}(\sqrt3)[[\cdot]]$ by comparing the
$\eta^2$ rung sequence ($0, 0, 11.93, 240.7, 1871.1, 12050.0, 89293.4,
554177.2$ at $\tilde u^{1..8}$) against $E$'s rungs — a finite exact linear
question at each order, not a fit.

**Scope discipline:** (A) is a class-(a) scope-limited negative (one
normalization); (B) is an exact positive. Nothing is wired; the ζ4/odd-sector
conjecture `conj:binding-qbeta-complex-volume` gains structural support at
the fibre level.

## Follow-up (queued)

1. Solve the functional relation $E = G(\eta^2)$ order-by-order (exact
   linear solves; the 08ds $E$-rungs vs the $\eta^2$-rungs above), and test
   whether $G$ matches a recognizable q-special-function profile
   ($\log\cosh$-type, q-Bessel-type per the Layer-2 kernel, or the ζ4
   rotation image of one).
2. If $G$ closes, formalize the descent as a §3b class tying
   `ComplexVolumeZeta4Partner` to the 08ds series data.
