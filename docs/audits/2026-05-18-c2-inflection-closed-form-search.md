# C2 inflection point — closed-form search (Item 5 spike)

## Status: research-grade, may not close

This audit kicks off Item 5 of the post-batch-4 queue: search for a
categorical / closed-form interpretation of the substrate-pure
proton-mass derivation route that selects the inflection point of
$A(a)$ on the Bring/color-tube cubic.

## What's known numerically

Numerical inflection finder
[`folio-assistant/computations/probe_c2_general_and_energy.py`](../../folio-assistant/computations/probe_c2_general_and_energy.py)
locates the C2 inflection point at

| Quantity | float64 value (scipy.integrate) |
|----------|---------------------------------|
| $a_{C_2}$ | $0.406\,427\,618\,3$ |
| $A(a_{C_2})$ | $2.461\,646\,839\,5$ |
| $m_p^\mathrm{pred} = \mathrm{Vol}_\mathrm{Bor}/\hbar_q^2 \cdot A \cdot m_e$ | $938.918$ MeV (-0.07% vs CODATA) |

Substrate constants at $q_0$:

| Constant | 40 dps value |
|----------|--------------|
| $q_0$ | $1.109\,978\,595\,554\,180\,575\,281\,594\,079\,609\,509\,377\,993$ |
| $\hbar_q = (q_0-1)/q_0$ | $0.099\,081\,726\,435\,698\,885\,820\,014\,342\,688\,412\,528\,468$ |
| $z_\mathrm{mark} = 1/(q_0^{1/2}+q_0^{-1/2})$ | $0.499\,320\,334\,033\,598\,250\,020\,669\,084\,676\,721\,506\,369$ |
| $\mathrm{Vol}_\mathrm{Bor}/\hbar_q^2$ | $746.417\,851\,076\,766\,839\,203\,683\,060\,009\,950\,141\,065\,2$ |

## Candidate closed forms tried

Scanned `(q_0, hbar_q, z_mark, Vol_Bor, c_q, pi)` against
$a_{C_2} = 0.406\,427\,618\,3$. Best matches:

| Candidate | Value | Relative error |
|-----------|-------|----------------|
| $1 / A(a_{C_2})$ — i.e. fixed-point $A \cdot a = 1$ | $0.406\,232\,114$ | $4.8 \times 10^{-4}$ |
| $\hbar_q \cdot 4.1$ — i.e. $a_{C_2} / \hbar_q \approx 4.10$ | $0.406\,235\,078$ | $4.7 \times 10^{-4}$ |
| $z_\mathrm{mark} + 0.094$ | $0.405\,320\,334$ | $2.7 \times 10^{-3}$ |

Both leading candidates sit at the relative-error floor of the
float64 inflection finder ($\sim$ $5 \times 10^{-4}$, dominated by the
`np.gradient` discrete second derivative on a 500-point grid). They
are **not distinguishable from noise** at the current precision.

## What's needed to close

1. **High-precision inflection finder.** Re-implement `A(a)` and
   its second derivative in mpmath at $\ge 30$ dps:
   - Replace `scipy.integrate.quad` → `mpmath.quad` on the color-
     tube cubic integrands.
   - Replace `np.gradient` finite differences → `mpmath.diff` (or
     close-form $A''(a)$ if expressible).
   - Solve $A''(a) = 0$ via `mpmath.findroot`.

2. **Test the two leading candidates** at the resulting 30-dps
   $a_{C_2}$:
   - If $1/A(a_{C_2}) = a_{C_2}$ holds to 30 dps, it's a **fixed-
     point identity** with a likely categorical interpretation
     (probably: the inflection IS where the ratio is unity, which
     would tie back to a Wedderburn-block normalization).
   - If $a_{C_2}/\hbar_q$ is a clean rational/algebraic (e.g.
     $4 + \text{small correction}$), look for the missing factor.

3. **If neither closes** — record the precision-resolved $a_{C_2}$
   in the audit doc as a "named substrate constant" candidate; ship
   the numerical derivation as a **conditional-on-conjecture**
   proposition (per §3b-cond) with the empirical $a_{C_2}$ as a
   class instance and the mass prediction proved conditional on it.

## Owner direction

Per the user's session direction "1 2 then 3", this audit is the
**start** of Item 5, not its conclusion. Subsequent sessions can
take any of the three paths above. Best-faith assessment: the
fixed-point identity $A \cdot a = 1$ at the inflection is the most
likely to close cleanly because of its dimensional symmetry, but
needs $\ge 30$ dps integration to test.

## Pointer files

- Numerical finder:
  [`probe_c2_general_and_energy.py`](../../folio-assistant/computations/probe_c2_general_and_energy.py)
- Cubic + thimble machinery:
  [`picard_lefschetz_thimble.py`](../../folio-assistant/computations/picard_lefschetz_thimble.py)
- Substrate constants:
  [`q_parameter.py`](../../folio-assistant/computations/q_parameter.py),
  [`_li_2_q_util.load_q_50dps`](../../folio-assistant/computations/_li_2_q_util.py)
- Sibling audit (Items A/B/C):
  [`2026-05-18-mp-chain-items-abc-findings.md`](2026-05-18-mp-chain-items-abc-findings.md)
- Sibling audit (substrate flavor split):
  [`2026-05-18-m-p-scale-gap-investigation.md`](2026-05-18-m-p-scale-gap-investigation.md)
