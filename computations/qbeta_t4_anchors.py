"""qbeta_t4_anchors.py — the single source for the T4-inverted ϑ anchors.

WHY THIS MODULE EXISTS (bean `qou-vbw1`). The T4 ϑ values were typed as 8-digit
literals into nine probes. When the T4 `q₀` was corrected (PR #4513 — a UNIT
CONFLATION, not a typo: the substrate quantity `0.20906` is `h = q₀ − 1/q₀`,
not `2·ln q₀`), every one of them went stale, and one probe's *sample grid* had
been tuned to sit just above a derived `A_crit` that also moved — a regression
that was invisible until the probe was re-run.

So: **ϑ is DERIVED here, never typed.** Change `q₀` or an anchor `S` and every
consumer follows automatically.

═══════════════════════════════════════════════════════════════════════════
CIRCULARITY WARNING — READ BEFORE USING `theta_t4`
═══════════════════════════════════════════════════════════════════════════
These ϑ are obtained by INVERTING the channel equation at `A_ω = 3`:

    S_K = A_ω · κ · (ln²q₀ − ϑ_K²)      ⇒      ϑ_K = √(ln²q₀ − S_K/(A_ω·κ))

`A_ω = 3` is IMPORTED from Garoufalidis–Gu–Mariño. It is **not derived** in
this corpus (beans `qou-rp5f`, `qou-cons`). Consequently:

  * `theta_t4(...)` is **A_ω-conditioned**. It is a *reading*, not a
    measurement, and it may NOT be offered as evidence for `A_ω = 3` — that is
    the exact circularity the `qou-skum` certificate exists to make visible.
  * `A_ω` and `ϑ_K` are ONE degree of freedom, not two. Two anchors give two
    equations in three unknowns.
  * A candidate ϑ route that reproduces these values has reproduced an
    inversion, not a prediction.

What is **A_ω-free**, and therefore safe to compare a candidate against, is
`AFREE_RATIO` below — see its docstring.

Provenance of each input is recorded in `PROVENANCE`.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

__all__ = [
    "kappa_41", "A_OMEGA_41", "S_ANCHORS", "ANCHORS",
    "q0", "ln_q0", "L", "theta_t4", "theta_all", "afree_ratio",
    "AFREE_RATIO_NOTE", "PROVENANCE",
]

# ── Inputs ────────────────────────────────────────────────────────────────

#: Measured S-leaks at the two anchors. TYPED because they are measurements;
#: everything downstream is derived from them.
S_ANCHORS = {
    "muon": "0.00968298",
    "proton": "-0.03945936",
}

ANCHORS = tuple(S_ANCHORS)

#: GGM Stokes constant for 4₁. **IMPORTED, NOT DERIVED** — see the module
#: docstring. Flagged ADJUDICATED_FREE in the qou-skum certificate so it is not
#: waved through as a small-integer literal.
A_OMEGA_41 = 3


def kappa_41() -> mp.mpf:
    """Cusp modulus of 4₁: `κ = √3/4`, from the cusp shape `τ = −i√3`.

    A PROVED geometric datum (`DeltaLambdaBindingAssembly.cuspModulus`), not a
    fit. Computed rather than typed so it carries full working precision.
    """
    return mp.sqrt(3) / 4


def q0(dps: int = 50) -> mp.mpf:
    """Canonical substrate q₀ — the EXPERIMENTAL (proton) pin.

    Per the AGENTS.md owner directive of 2026-08-07, all new compute defaults to
    the proton pin. Read from `qou_substrate.constants`, never typed: the whole
    point of `qou-vbw1` is that a typed q₀ went stale and took nine probes with
    it.
    """
    return q_at(dps)


def ln_q0(dps: int = 50) -> mp.mpf:
    return mp.log(q0(dps))


def L(dps: int = 50) -> mp.mpf:
    """`L = ln²q₀`, the boost term of the channel."""
    return ln_q0(dps) ** 2


# ── Derived ϑ ─────────────────────────────────────────────────────────────

def theta_t4(anchor: str, dps: int = 50, A_omega: float | None = None) -> mp.mpf:
    """T4-inverted ϑ at `anchor` ∈ {"muon", "proton"} — **A_ω-conditioned**.

        ϑ = √(ln²q₀ − S/(A_ω·κ))

    Raises if the radicand is negative, which is the honest failure mode: for
    `A_ω` below `S_muon/(κ·ln²q₀) ≈ 2.05` the muon anchor admits NO real
    angular deformation at all. That threshold is `A_crit`; do not hardcode it,
    call `a_crit()`.
    """
    if anchor not in S_ANCHORS:
        raise KeyError(f"unknown anchor {anchor!r}; expected one of {ANCHORS}")
    A = mp.mpf(A_OMEGA_41 if A_omega is None else A_omega)
    S = mp.mpf(S_ANCHORS[anchor])
    rad = L(dps) - S / (A * kappa_41())
    if rad < 0:
        raise ValueError(
            f"no real ϑ at anchor {anchor!r} for A_ω = {mp.nstr(A, 8)}: "
            f"radicand {mp.nstr(rad, 8)} < 0 (A_crit = {mp.nstr(a_crit(dps), 10)})"
        )
    return mp.sqrt(rad)


def theta_all(dps: int = 50, A_omega: float | None = None) -> dict[str, mp.mpf]:
    """Both T4-inverted ϑ, keyed by anchor. **A_ω-conditioned** — see module doc."""
    return {a: theta_t4(a, dps, A_omega) for a in ANCHORS}


def a_crit(dps: int = 50) -> mp.mpf:
    """Smallest `A_ω` admitting a real ϑ at BOTH anchors.

    Driven by the muon (the only anchor with `S > 0`): `A ≥ S_μ/(κ·ln²q₀)`.
    DERIVE sample grids from this — never hardcode a number just above it. A
    grid tuned to a superseded `A_crit` silently drops its own samples when q₀
    moves, which is precisely what happened in `qou-offl` (PR #4513).
    """
    return max(
        mp.mpf(S_ANCHORS[a]) / (kappa_41() * L(dps))
        for a in ANCHORS
    )


# ── The A_ω-free invariant ────────────────────────────────────────────────

AFREE_RATIO_NOTE = (
    "r = S_muon/S_proton is free of BOTH A_omega and q0 by construction "
    "(QOU.QBeta.AfreeThetaConstraint.afree_invariant). Eliminating A_omega "
    "between the two anchor equations leaves "
    "(L - theta_mu^2)/(L - theta_p^2) = r, the one falsifiable A-free "
    "statement the channel makes. CAUTION: `ratio_attained` proves a witness A "
    "exists for every y > 1, so merely LANDING on r is unfalsifiable and is not "
    "evidence for anything."
)


def afree_ratio() -> mp.mpf:
    """`r = S_muon/S_proton` — free of `A_ω` and of `q₀`. See `AFREE_RATIO_NOTE`."""
    return mp.mpf(S_ANCHORS["muon"]) / mp.mpf(S_ANCHORS["proton"])


PROVENANCE = {
    "q0": "qou_substrate.constants.q_at — canonical EXPERIMENTAL (proton) pin",
    "kappa_41": "sqrt(3)/4 from cusp shape tau = -i*sqrt(3); PROVED "
                "(DeltaLambdaBindingAssembly.cuspModulus)",
    "A_omega_41": "GGM (Garoufalidis-Gu-Marino) — IMPORTED, NOT DERIVED; "
                  "open per beans qou-rp5f / qou-cons; ADJUDICATED_FREE",
    "S_anchors": "measured S-leaks; typed here as the primitive inputs",
    "theta": "DERIVED by inversion at A_omega = 3 — A_omega-conditioned, "
             "not an independent determination (bean qou-qnnq / qou-8vt2)",
}


if __name__ == "__main__":  # pragma: no cover - manual inspection aid
    set_compute_dps()
    print(f"q0        = {mp.nstr(q0(), 20)}   (canonical proton pin)")
    print(f"ln q0     = {mp.nstr(ln_q0(), 20)}")
    print(f"L         = {mp.nstr(L(), 20)}")
    print(f"kappa_41  = {mp.nstr(kappa_41(), 20)}")
    print(f"A_omega   = {A_OMEGA_41}   (GGM, IMPORTED not derived)")
    print(f"A_crit    = {mp.nstr(a_crit(), 20)}")
    for a, t in theta_all().items():
        print(f"theta[{a:<6}] = {mp.nstr(t, 20)}   (A_omega-conditioned)")
    print(f"afree r   = {mp.nstr(afree_ratio(), 20)}")
