# Keystone value map (s013): colored LR residue character derived; channel + q-Bessel-row amplitudes pruned

**Date:** 2026-07-02
**Bean:** [`s013`](../../.beans/s013--keystone-value-map-colored-lawrence-rozansky-s-mat.md)
**Follows:** [`2026-06-30-keystone-colored-sigma235-e8-family.md`](2026-06-30-keystone-colored-sigma235-e8-family.md) (structure) and the first-pass compact screen (`keystone_valuemap_screen_s013.py`, merged 2026-07-01: [e]_q / sin(πe/30) / sinh(ηe) refuted; target narrowed to the non-compact q-Bessel vacuum row)
**Script:** [`computations/probes/keystone_valuemap_qbessel_gate_s013.py`](../../computations/probes/keystone_valuemap_qbessel_gate_s013.py)
**Witness:** [`computations/probes/keystone-valuemap-qbessel-gate-s013.witness.json`](../../computations/probes/keystone-valuemap-qbessel-gate-s013.witness.json)
**Status:** two positive structural results (derived, machine-verified) + three (a)-scope prunes. No fit; nothing wired.

## Sandbox constraint, stated up front

The primary sources for the genuine colored amplitude (Lawrence–Rozansky 1999; Hikami
arXiv:1811.05376; Andersen–Mistegård arXiv:2205.01282) are **firewalled in this sandbox**
(arXiv/proxy 403 on every route tried: paper-search MCP, WebFetch on arxiv.org /
export.arxiv.org / sigma-journal.com / ncatlab.org; `library/` does not carry them). Per the
s013 discipline note ("the colored-amplitude FORMULA is where fabrication risk is real"),
this round therefore restricts itself to what is **derivable and machine-verifiable in-repo**
— nothing below is quoted from memory of the papers.

## 1. Positive result — the colored LR residue character, derived exactly

With $x = e^{-z/30}$, the colored sinh-product of the $\Sigma(2,3,5)$ Lawrence–Rozansky
integrand satisfies the exact rational-function identity

$$
\frac{2\sinh(z/2)\,2\sinh(z/3)\,2\sinh(\alpha z/5)}{2\sinh(z)}
 \;=\; \mathrm{num}_\alpha(x)\cdot\sum_{k\ge 0} x^{60k},
\qquad
\mathrm{num}_\alpha(x) = (x^{-15}-x^{15})(x^{-10}-x^{10})(x^{-6\alpha}-x^{6\alpha})\,x^{30},
$$

a finite Laurent-polynomial statement (sympy-exact integer coefficients; numeric residual
≤ 4×10⁻⁴¹ at 50 dps). Folding the expansion coefficients into an odd 60-periodic character —
with a consistency vote across every window occurrence of each residue class, so the
transient region (the |n|=1 class of α=1 sits solely at n=−1) is handled mechanically —
**derives** rather than assumes:

| α | support (1..30) | signs | fold consistent | weights |
|--:|---|---|:-:|---|
| 1 | {1, 11, 19, 29} | uniform −1 | ✓ | all ±1 |
| 2 | {7, 13, 17, 23} | uniform −1 | ✓ | all ±1 |
| 3 | {7, 13, 17, 23} | uniform −1 | ✓ | all ±1 |
| 4 | {1, 11, 19, 29} | uniform −1 | ✓ | all ±1 |

- α=1 reproduces the bare validated support {1,11,19,29} (= H₄ exponents); α=1 ∪ α=2 = all
  eight E₈ exponents — confirming the merged #3190 structure from the exact identity.
- The sign is **uniform on each support and identical across colours** — a single global
  orientation/framing sign relative to the prior probes' all-plus convention; the colored
  family's *relative* structure is unchanged. (Bonus: α=4 ≡ α=1 and α=3 ≡ α=2 — the colour
  supports are 5-periodic under the fibre reflection, as expected for the order-5 fibre.)
- **Decisively: every residue weight is ±1.** The colored Lawrence–Rozansky residue data is
  *pure sign* — it carries no magnitude structure at all. The value map
  $\mathrm{bwS0}(\lambda) = d_q(\lambda)/D$ **cannot** be realized by the residue weights.

## 2. Positive result — the per-exponent channel decomposition, validated

The colored family decomposes into 8 per-exponent false-theta channels
$\tilde\Psi^{(e)}(q) = \sum_{n\equiv\pm e\ (60)} \pm\, q^{n^2/120}$, the per-colour,
per-block amplitudes the bean's value step names. At $1/q_0$:

| e | 1 | 7 | 11 | 13 | 17 | 19 | 23 | 29 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| $\tilde\Psi^{(e)}(1/q_0)$ | 0.9900 | 0.8915 | 0.7886 | 0.7265 | 0.5831 | 0.5030 | 0.3294 | 0.0480 |

Validation: the α=1 channel sum is 2.329577, matching the bare invariant Ψ(1/q₀) ≈ 2.3296
from `keystone_habiro_wrt_s3_2i_probe` — the decomposition is exact.

## 3. Prune — the channel amplitudes are the L-value family, not the d_q family

Screened against the d_q targets (ratios 1, 4.110, 5.220, 6.220 on the dual-pair
representatives e = 1, 7, 11, 13): raw channel, pair-sum, and pair-difference are **all
refuted** (ratios 0.90/0.80/0.73, 1.18/1.24/1.26, 0.60/0.30/0.15 respectively — not even
monotone-increasing).

Sharper, anchor-independent: as $q \to 1^-$ the channel ratios converge to the **L-values**

$$\frac{\tilde\Psi^{(e)}}{\tilde\Psi^{(1)}} \;\longrightarrow\; \frac{L(0,\chi_e)}{L(0,\chi_1)} = \frac{30-e}{29},$$

verified numerically (ε = 10⁻⁴ ratios 0.7932/0.6553/0.5863 vs predicted 0.7931/0.6552/0.5862).
The channel amplitude family **decreases** in e at every anchor while the d_q targets
**increase** (1 → 4 → 5 → 6 classically). Scope (a): the per-exponent channel evaluation,
*alone, as-is*, is not the value map — at any anchor, not just q₀.

## 4. Prune — no single-argument (q-)Bessel vacuum row passes the 1-dof gate

The first-pass narrowing ("the value map is the non-compact E_q(2)/Hahn–Exton q-Bessel
vacuum row") admits a disciplined minimal form: a single-argument row $A(e) = J_e(x)$ with
one degree of freedom $x$, tested overdetermined — pin $x$ by the first ratio
($J_7/J_1 = t_2$, root-enumerated over the full window), then cross-check the two remaining
ratios at **every** root (1 dof, 2 net checks; PASS = both within 10⁻⁶ relative):

| row | targets | roots | best max rel err |
|---|---|--:|--:|
| ordinary $J_e(x)$ (E(2) contraction) | classical dims 1,4,5,6 | 18 | 5.6×10⁻¹ |
| ordinary pair $J_e + J_{30-e}$ | classical dims | 16 | 9.0×10⁻¹ |
| Hahn–Exton $J_e(x;\hat q)$, $\hat q = q_0^{-2}$ | d_q | 23 | 4.7×10⁻¹ |
| Hahn–Exton pair | d_q | 24 | 1.3×10⁻¹ |

**None passes** (best is 13% off — nowhere near). Scope (a): the *single-argument*
(q-)Bessel row with the E₈ dual-pair-representative order assignment, alone, is pruned.
This does **not** exclude the q-Bessel structure as such: the genuine E_q(2) harmonic
analysis pairs each channel with its own lattice argument through the q-Hankel/Plancherel
kernel (Koelink–Swarttouw), which is exactly what could not be built here without the
firewalled primary sources.

## Where the value step now stands (sharpened)

1. **Not the residue weights** (§1 — derived: pure signs).
2. **Not the per-exponent channel evaluations** (§3 — derived: the L-value family, wrong
   monotonicity at every anchor).
3. **Not a single-argument (q-)Bessel row** (§4 — 1-dof overdetermined gate fails by 10⁵×
   the tolerance).
4. **Open (literature-gated):** the genuine colored amplitude — the E_q(2)
   q-Hankel/Plancherel pairing with per-channel arguments (Koelink–Swarttouw kernel), or
   equivalently the true colored Lawrence–Rozansky/Hikami S-matrix residue weights *at the
   level of the modular transform* (not the naive residue signs). Requires the primary
   sources; next session should run from an environment where arXiv is reachable, or the
   owner can drop the PDFs (Hikami arXiv:1811.05376; Andersen–Mistegård arXiv:2205.01282;
   Lawrence–Rozansky CMP 205 (1999)) into `library/`.

The keystone structure result (E₈-exponent family, 4↔4 monotone correspondence, H₄⊂E₈
folding) is untouched by these prunes — they sharpen where its *numerical realization* must
come from.

## Discipline

- Formalize-first: every claim above is either sympy-exact, 50-dps verified against an
  in-repo validated anchor (bare Ψ = 2.3296), or an analytic L-value law verified
  numerically. No formula was imported from memory of firewalled papers.
- All negative results are scope (a) — construction-limited, with the tested construction
  and assignment named. No structural exclusion is claimed anywhere.
- No fit: the only free parameter anywhere (the Bessel-row x) is pinned by one target and
  cross-checked on two others, with every root enumerated.
- Three-calibration discipline untouched; nothing wired to production.
