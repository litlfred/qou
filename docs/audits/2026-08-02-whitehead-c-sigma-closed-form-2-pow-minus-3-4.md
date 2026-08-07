# Whitehead-link VC sub-leading constant c_σ = 2^{-3/4} — high-precision identification + torsion template

**Date:** 2026-08-02
**Branch:** `claude/whitehead-c-sigma-torsion-2026-08-02`
**Bean:** qou-k00d (Whitehead arc, item 4)
**Follow-up to:** [`2026-07-26-whitehead-vc-verification-and-p-exponent.md`](2026-07-26-whitehead-vc-verification-and-p-exponent.md)

## Result

The Whitehead link (L5a1) colored-Jones Volume-Conjecture asymptotic

$$
|J_N(e^{2\pi i/N})| \;\sim\; c_\sigma \, N^{3/2}\, e^{(\mathrm{Vol}/2\pi)\,N},
\qquad \mathrm{Vol}=4G,
$$

has sub-leading constant

$$
\boxed{\,c_\sigma = 2^{-3/4} = 0.59460355750136053\ldots\,}
$$

confirmed to **20 significant digits** (relative error 3.1×10⁻²¹) by a fully
arbitrary-precision (mpmath) computation. `2^{-3/4}` is **parameter-free** and
**π-free** — it was stated as a structural hypothesis *before* the high-precision
search, and no constant was tuned.

## How it was pinned (mpmath end-to-end, per the "no float64" owner directive)

[`computations/whitehead_c_sigma_hiprec.py`](../../computations/whitehead_c_sigma_hiprec.py)
computes van der Veen's exact positive-sum colored Jones (Lemma 1,
arXiv:math/0611181 — the transcription already validated three ways in
`whitehead_van_der_veen.py`) entirely in `mpf`/`mpc` at **dps = 100**, over a
tower **N = 400 … 3000** (well past the float64 overflow wall at N≈1281, where
`|J_N|∼e^{583}`), then Neville/Richardson-extrapolates c_σ(N) = |J_N|·N^{-3/2}·
e^{-(Vol/2π)N} to 1/N → 0. Convergence onto 2^{-3/4}:

| resolution | extrapolated c_σ | agreement to 2^{-3/4} |
|---|---|---|
| dps=60, N≤1400 | 0.5946035575013604799 | 16 digits |
| **dps=100, N≤3000** | **0.5946035575013605334** | **20 digits** |

Pushing N and precision moved the match **from 16 to 20 digits, converging onto**
2^{-3/4} — the signature of a true limit, not a float64 coincidence. Runner-up
parameter-free candidates all miss at the first digit: 2^{-5/4}=0.4204,
1/√2=0.7071, 3^{-1/4}=0.7598.

The growth exponent is simultaneously pinned: the least-squares fit gives
**p = 1.4999992** (witness) / the figure-eight control gives 1.49999998, i.e.
**p = 3/2 exactly** — settling the 2-cusp-link p-exponent question left open in the
2026-07-26 note (the earlier instability was an artifact of the O(N⁹) R-matrix's
N≤14 ceiling; the O(N²) van der Veen formula has no such wall).

Witness: [`whitehead-c-sigma-hiprec.witness.json`](../../computations/whitehead-c-sigma-hiprec.witness.json).

## Structural interpretation: the 1-loop torsion template — VALIDATED on 4_1

The refined Volume Conjecture / Ohtsuki 1-loop asymptotic identifies the
sub-leading constant with the **adjoint Reidemeister torsion** τ of the complement
at the geometric flat connection:

$$
c_\sigma^{K} = |\tau_{\mathrm{adjoint}}(K)|^{-1/2}\quad\text{(reduced-colored-Jones normalization).}
$$

This template is **validated on a known case** by running the *same* c_σ pipeline
on the figure-eight knot
([`whitehead_c_sigma_fig8_calib.py`](../../computations/whitehead_c_sigma_fig8_calib.py)),
whose reduced colored Jones at e^{2πi/N} is the Habiro/Kashaev single positive sum
`J'_N(4_1)=Σ_k ∏_{j≤k}(2 sin(πj/N))²` (same unknot-normalization class):

| knot | pipeline c_σ (dps=60, N≤3000) | known closed form | agreement |
|---|---|---|---|
| **4_1** | 0.75983568565159255077 | **3^{-1/4}** = (√3)^{-1/2}, \|τ(4_1)\|=√3 | **17 digits** |

`c_σ(4_1)=3^{-1/4}` is the standard figure-eight prefactor (trace field ℚ(√-3);
also recorded in the corpus's own `whitehead-c0-mpmath.witness.json` as the
reference `-¼ln3`). Reproducing it to 17 digits confirms the c_σ pipeline **is**
the 1-loop torsion prefactor |τ|^{-1/2}, not a coincidence.

Applying the validated template to the Whitehead:

$$
c_\sigma(\text{L5a1}) = 2^{-3/4} = (2\sqrt2)^{-1/2}
\;\Longrightarrow\; |\tau_{\mathrm{adjoint}}(\text{L5a1})| = 2\sqrt2 = 2^{3/2}.
$$

The value 2^{3/2} is a **pure power of 2**, exactly the algebraic scale the
Whitehead complement = **regular ideal octahedron** predicts: its shapes have
|z| = |1+i| = √2 and its trace field is ℚ(i). (Contrast the figure-eight's √3
from ℚ(√-3).) Witness:
[`whitehead-c-sigma-fig8-calib.witness.json`](../../computations/whitehead-c-sigma-fig8-calib.witness.json).

## Honest verdict — identification, not (yet) a first-principles derivation

Per the anti-laundering / "sorry-free ≠ derived" discipline, the two epistemic
tiers are kept distinct:

- **Established (this PR):** c_σ = 2^{-3/4} as a **high-precision numerical
  identification** — 20 digits, parameter-free, π-free — with a **structural
  interpretation** (= |τ|^{-1/2}) whose template is independently **validated on
  the figure-eight** (3^{-1/4}, 17 digits). This is strong and, being
  parameter-free, effectively certain as a *value*.

- **NOT established (the residual):** a **first-principles derivation** of
  |τ_adjoint(L5a1)| = 2√2 from the octahedron's Neumann–Zagier data / Porti's
  torsion, *independently of inverting c_σ*. The template supplies the torsion
  *from* c_σ; it does not yet *derive* the torsion *from the geometry*. Computing
  the octahedron adjoint torsion directly (Dimofte–Garoufalidis 1-loop
  `τ = ±½ det(A/z'' + B z')` from the L5a1 NZ matrices — needs SnapPy, unavailable
  in this sandbox — or Fox calculus on the Whitehead group presentation) is the
  step that would upgrade "identified + template-validated" to "derived."

**No production wiring.** All three witnesses are `audit_only`. c_σ = 2^{-3/4} is
NOT a fit (nothing was tuned to an experimental anchor), but it is also not yet a
categorical-driver derivation, so it stays out of any dashboard/production script
as canonical.

## Files

- [`computations/whitehead_c_sigma_hiprec.py`](../../computations/whitehead_c_sigma_hiprec.py) — mpmath c_σ extrapolation
- [`computations/whitehead_c_sigma_fig8_calib.py`](../../computations/whitehead_c_sigma_fig8_calib.py) — figure-eight template calibration
- [`computations/whitehead-c-sigma-hiprec.witness.json`](../../computations/whitehead-c-sigma-hiprec.witness.json)
- [`computations/whitehead-c-sigma-fig8-calib.witness.json`](../../computations/whitehead-c-sigma-fig8-calib.witness.json)
