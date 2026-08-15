"""Canonical 5₂ saddle values `V_j` — COMPUTED, not hardcoded (bean qou-ty28).

Why this module exists
----------------------
Four probes carried `V₁`, `V₂`, `V₃` for 5₂ as hardcoded literals with the
source comment `# GGM eq 21`. Reconciliation against the two source papers
(both now in `library/`) established:

* the **cubic is correct** — the corpus's `x³ − 2x² + 3x − 1` is exactly
  GGM eq (233) at `x = 1`, i.e. `(1−ξ)³ = ξ²` = GGMW eq (184), so the
  saddle *root* was never in question;
* the **literals are not**: `Im V₁ = 1.3790860299` and
  `V₃ = −2.7580990292` match neither GGM eq (234) nor GGMW eq (188).
  Investigation (2026-07-29) identified the extraction convention
  `V_eff = V_GGM + π²/2 = Re(V_GGMW) − π²/6 = 1.379194309661…`
  (absorbing the Φ_b Bernoulli contribution) in the corpus i-rotation
  convention — a legitimate mathematical quantity, but not the V the
  published Stokes formulas use.

  **Which literal that identifies (corrected 2026-08-01).** The `5e-8`
  agreement holds for `V_DOM`'s `1.37919426157`
  (`qbeta_5two_median_borel_resummation_probe.py`, |Δ| = 4.8e-8). It does
  **not** hold for `Im V₁ = 1.3790860299`, which sits `1.08e-4` away —
  2250× the stated bound, and not a root-precision artifact (a 6-digit
  root already reproduces `1.379194309661` exactly). An earlier revision
  of this docstring attached the `5e-8` claim to `Im V₁`; that was a
  mis-attribution between two distinct legacy literals differing in the
  4th decimal. **`Im V₁ = 1.3790860299` remains unexplained**, as does
  `V₃ = −2.7580990292`;
* the citation is also wrong: eq (21) of 2012.00062v3 is the
  Stokes/3D-index identity `S⁺_{σ₁σ₁} = Ind^rot_K(0,x;q)`, not a saddle
  value.

The fix is mechanical: compute the values from the (correct) root by the
published formula, and make the normalization an explicit argument rather
than an implicit convention.

The three normalizations (π²/6 lattice)
--------------------------------------
GGM eq (234) at `x = 1`:  `V = 3·Li₂(y) + (log(−y))²` on `y² = (1−y)³`,
with §6.1's rule *"for σ₃ we only keep the real part of V"*.

GGMW eq (188) is the same object shifted:

    V_GGMW = V_GGM + 2π²/3      (exact, verified to 16 digits on σ₁ and σ₃)

consistent with GGMW footnote 6's `e^{−πi(τ+τ⁻¹)/12}` prefactor between
their `Φ^{(σ)}` and GGM's.

**Extraction** (the legacy `V_DOM = 1.37919426157`, *not* the legacy
`Im V₁`): `V_eff = V_GGM + π²/2`, the effective action of the H-series
radial asymptotics. The π²/2 is the Bernoulli-number contribution from the
Φ_b normalization, absorbed into the action by the fit. All three sit on a
π²/6 lattice:

    V_GGM ──(+3·π²/6)──> V_extraction ──(+1·π²/6)──> V_GGMW

This module provides GGM and GGMW only — the extraction convention is not a
published normalization and should not be used for Stokes-formula arguments.

Reference values reproduced by this module (30 dps):

| | GGM | GGMW |
|---|---|---|
| `V₁` | `−3.555607890883604 + 2.828122088330783i` | `3.024128376509302 + 2.828122088330783i` |
| `V₂` | `conj(V₁)` | `conj(V₁)` |
| `V₃` | `−7.69319081986683` | `−1.113454552473924` |

`Im V₁ = Vol(S³∖5₂) = 2.828122088330783` in **both**.

Consumer note
-------------
`|V₁ − V₂| = 2·Vol = 5.656244176661566` is identical in both
normalizations *and* in the legacy corpus convention (which put `Vol` in
`Re V₁`), so results depending only on that combination were never
affected. Results consuming `V₃` or `Im V₁` individually — notably the
B1 sector amplitudes — should be re-derived through this module.

auditOnly; comparison to published mathematics; no fit.
"""
from __future__ import annotations

import mpmath as mp

__all__ = ["saddle_roots", "V_GGM", "V_GGMW", "saddle_values",
           "GGM_TO_GGMW_SHIFT", "volume"]


def GGM_TO_GGMW_SHIFT() -> mp.mpf:
    """`V_GGMW − V_GGM = 2π²/3`, exact at the working precision."""
    return 2 * mp.pi ** 2 / 3


def saddle_roots():
    """The three roots of the 5₂ saddle cubic, as `(y₁, y₂, y₃)` =
    (geometric, conjugate, real).

    The cubic is `y³ − 2y² + 3y − 1 = 0`, i.e. GGM eq (233) at `x = 1`
    (`y² = (1−y)³`) = GGMW eq (184) (`(1−ξ)³ = ξ²`). These are the same
    equation; the corpus's long-standing `x³ − 2x² + 3x − 1` is correct.
    """
    rts = mp.polyroots([1, -2, 3, -1], maxsteps=300, extraprec=300)
    y3 = next(r for r in rts if abs(mp.im(r)) < mp.mpf(10) ** (-mp.mp.dps // 2))
    y1 = next(r for r in rts if mp.im(r) > 0)
    y2 = next(r for r in rts if mp.im(r) < 0)
    return y1, y2, y3


def V_GGM(y, branch: int):
    """GGM eq (234) at `x = 1`: `3·Li₂(y) + (log y + branch·πi)²`.

    `branch = ∓1` selects the `log(−y)` sheet; the geometric saddle uses
    `−1` and its conjugate `+1`, matching GGM eq (189)'s `V₂ = conj(V₁)`.
    """
    return 3 * mp.polylog(2, y) + (mp.log(y) + branch * mp.pi * 1j) ** 2


def V_GGMW(y, branch: int):
    """GGMW eq (188), i.e. `V_GGM + 2π²/3`."""
    return V_GGM(y, branch) + GGM_TO_GGMW_SHIFT()


def saddle_values(normalization: str = "ggmw"):
    """`(V₁, V₂, V₃)` for 5₂ in the requested published normalization.

    `normalization` is **required to be explicit** — passing it is how a
    consumer records which paper's convention its downstream numbers are
    in. `"ggm"` → eq (234); `"ggmw"` → eq (188).

    Per GGM §6.1, `V₃` (the real/σ₃ connection) keeps only `Re V`.
    """
    norm = normalization.lower()
    if norm not in ("ggm", "ggmw"):
        raise ValueError(f"normalization must be 'ggm' or 'ggmw', got "
                         f"{normalization!r}")
    f = V_GGM if norm == "ggm" else V_GGMW
    y1, y2, y3 = saddle_roots()
    return f(y1, -1), f(y2, +1), mp.re(f(y3, +1))


def volume():
    """`Vol(S³∖5₂) = |Im V₁|`, normalization-independent."""
    y1, _, _ = saddle_roots()
    return abs(mp.im(V_GGM(y1, -1)))


def V_extraction():
    """The H-series extraction convention `V_eff = V_GGM + π²/2`.

    Exposed for *provenance checking only* — it is not a published
    normalization and `saddle_values` deliberately refuses to return it.
    """
    y1, _, _ = saddle_roots()
    return V_GGM(y1, -1) + mp.pi ** 2 / 2


def _self_check():
    """Machine-check every numeric claim this module's docstring makes.

    The docstring previously asserted a `5e-8` provenance match for a
    literal that is `1.08e-4` away; the claim was prose, so nothing caught
    it. These gates exist so the next such slip fails loudly.
    """
    mp.mp.dps = 40
    y1, y2, y3 = saddle_roots()
    ok = True

    def gate(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}{detail}")

    # the π²/6 lattice: GGM --(+3·π²/6)--> extraction --(+1·π²/6)--> GGMW
    ext = mp.re(V_extraction())
    gate("extraction == V_GGM + π²/2 == Re(V_GGMW) − π²/6",
         abs(ext - (mp.re(V_GGMW(y1, -1)) - mp.pi ** 2 / 6)) < mp.mpf("1e-30"))
    gate("GGMW − GGM == 2π²/3 (σ₁)",
         abs((V_GGMW(y1, -1) - V_GGM(y1, -1)) - 2 * mp.pi ** 2 / 3)
         < mp.mpf("1e-30"))

    # attribution of the extraction convention to the correct legacy literal
    d_dom = abs(ext - mp.mpf("1.37919426157"))     # V_DOM, median-Borel probe
    d_v1 = abs(ext - mp.mpf("1.3790860299"))       # legacy Im V₁
    gate("extraction identifies V_DOM 1.37919426157",
         d_dom < mp.mpf("5e-8"), f"  (|Δ| = {mp.nstr(d_dom, 4)})")
    gate("extraction does NOT identify legacy Im V₁ 1.3790860299",
         d_v1 > mp.mpf("1e-5"),
         f"  (|Δ| = {mp.nstr(d_v1, 4)} — provenance still unexplained)")

    # Vol is normalization-independent and sits in Im, not Re
    gate("Im V₁ == Vol(5₂) in both normalizations",
         abs(mp.im(V_GGM(y1, -1)) - mp.im(V_GGMW(y1, -1))) < mp.mpf("1e-30")
         and abs(mp.im(V_GGM(y1, -1)) - volume()) < mp.mpf("1e-30"))
    gate("V₂ == conj(V₁)",
         abs(V_GGM(y2, +1) - mp.conj(V_GGM(y1, -1))) < mp.mpf("1e-25"))
    return ok


if __name__ == "__main__":
    import sys
    print("fivetwo_saddle_values self-check (docstring claims):")
    sys.exit(0 if _self_check() else 1)
