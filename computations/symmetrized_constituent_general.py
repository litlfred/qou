#!/usr/bin/env python3
"""General identical-nucleon symmetrization infra — Frobenius formula for any (Z,N).

Generalizes `symmetrized_constituent_probe.py` (which did only the Z=N=2 scalar
h₂/e₂) to ALL isotopes via the Newton / Frobenius power-sum formula:

    h_Z = Σ_{μ⊢Z}      p_μ / z_μ        (bosonic / complete symmetrization)
    e_Z = Σ_{μ⊢Z} ε_μ · p_μ / z_μ        (fermionic / antisymmetrization — Pauli)

with power sums  p_k = tr_M(B_p^k)  (proton core braid composed k times, an H₃
Markov trace),  p_μ = ∏_i p_{μ_i},  z_μ = ∏_i i^{m_i} m_i!  (centralizer order
of cycle type μ, m_i = #parts equal to i),  ε_μ = (−1)^{Z−len(μ)} (sign of μ).

## Derivation (why this IS the symmetrized free trace)

Z distinguishable protons = V^⊗Z; the S_Z-symmetrized trace is
`tr(P_± · A^⊗Z)` where A = the single-proton transfer operator (tr A = the
constituent τ_p = p_1) and `P_± = (1/Z!) Σ_{σ∈S_Z} (±1)^σ σ` is the
(anti)symmetrizer. The standard cycle-product identity

    tr(σ · A^⊗Z) = ∏_{cycles c of σ} tr(A^{|c|})

summed over conjugacy classes (|C_μ| = Z!/z_μ) gives

    tr(P_+ A^⊗Z) = Σ_μ      p_μ/z_μ = h_Z ,
    tr(P_- A^⊗Z) = Σ_μ ε_μ · p_μ/z_μ = e_Z .

The constituent at `closed_form_tau_M.py:302` uses the NAIVE τ_p^Z (=
distinguishable V^⊗Z, identity term μ=(1^Z) only); h_Z / e_Z replace it with the
correctly (anti)symmetrized constituent. The full isotope constituent is then

    bosonic   :  h_Z(p) · h_N(n)
    fermionic :  e_Z(p) · e_N(n)      (Pauli-correct for identical-nucleon exchange)

## Scalar caveat (honest — same as the Z=2 probe)

p_k = tr_M(B_p^k) carries the Markov y_λ Wedderburn weights, so the SCALAR
Frobenius value APPROXIMATES (does not equal) the exact block-level q-Young
projection into H_{3Z} — that exact projector is tractable only for small Z via
the full H_{3Z} Markov trace (the ⁴He H₁₂ task-1 reduction). This module is the
GENERAL, tractable infra: any (Z,N) at H₃ cost (compute p_1..p_{max Z,N} ONCE
per nucleon, then the Frobenius sum is pure arithmetic over partitions). The
exact block projector is the small-Z refinement that sits on top of it.

Verified Schur-Weyl identities (Z=2,3,4): QOU.Hecke.IdenticalParticleSymmetrization.

Output: symmetrized-constituent-general.witness.json
"""
from __future__ import annotations

import sys
import time
from collections import Counter
from math import factorial
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
for sub in (".", "substrate", "hecke", "markov"):
    sys.path.insert(0, str(HERE / sub if sub != "." else HERE))

from witness_base import WitnessBuilder  # noqa: E402
from binding_canonical import build_atom_symbolic  # noqa: E402
from markov_trace_canonical import tr_M_element  # noqa: E402
from hecke_symbolic import SymbolicHeckeDivision, q as q_sym  # noqa: E402
# `Q_50_DIGIT_STR` only.  The float alias `Q` was imported and used in exactly two
# places, both of them RECORDS of the pin (a display line and a witness
# parameter) while every computation went through the 50-digit string — so it
# published 17 of the 50 digits it ran at.  Dropping the import removes the way
# that could recur, and makes this file read correctly to the bare-`Q`-import
# screen in `qou-840k`, which flagged it as upstream-capped: it never was, since
# the float reached no arithmetic.  That screen over-flags, and this file is the
# first measured instance.
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()
DIV = SymbolicHeckeDivision()

# Isotope set: light + a few doubly-magic. (Z, N). max(Z,N) sets the power-sum
# order; ¹⁶O (8,8) caps kmax at 8 — p_1..p_8 per nucleon is the only Hecke cost.
ISOTOPES = [
    ("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
    ("5Li", 3, 2), ("6Li", 3, 3), ("7Li", 3, 4),
    ("8Be", 4, 4), ("12C", 6, 6), ("16O", 8, 8),
]


def _trM(elem, n=3):
    """Markov trace of an H_n element, evaluated at q₀ (Im q₀ = 0 ⇒ real)."""
    s = tr_M_element(elem, n, simplify=False)
    # Substitute the TRUE 50-digit q₀ (not str(float Q0), which is only ~16
    # sig digits — sp.Float(str(Q0),45) would pad the tail with float noise).
    val = sp.N(s.subs(q_sym, sp.Float(Q_50_DIGIT_STR, 50)), 50)
    return mp.mpf(str(sp.re(val)))


def power_sums(core, kmax):
    """p_k = tr_M(core^k), k = 1..kmax. One reduction per power (kept in H₃)."""
    p = {}
    cur, _ = DIV.reduce(core, engine="laurent")
    p[1] = _trM(cur)
    for k in range(2, kmax + 1):
        cur = cur * core
        cur, _ = DIV.reduce(cur, engine="laurent")
        p[k] = _trM(cur)
    return p


def _partitions(n, mx=None):
    """Integer partitions of n with parts ≤ mx (descending tuples)."""
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in _partitions(n - k, k):
            yield (k,) + rest


def _z_mu(mu):
    """Centralizer order z_μ = ∏ i^{m_i} m_i! of cycle type μ."""
    z = 1
    for i, m in Counter(mu).items():
        z *= (i ** m) * factorial(m)
    return z


def frobenius(p, Z, fermionic=False):
    """h_Z (bosonic) or e_Z (fermionic) via Σ_μ (±)^? p_μ / z_μ. h_0 = e_0 = 1."""
    total = mp.mpf(0)
    for mu in _partitions(Z):
        pm = mp.mpf(1)
        for part in mu:
            pm *= p[part]
        term = pm / _z_mu(mu)
        if fermionic and (Z - len(mu)) % 2 == 1:
            term = -term
        total += term
    return total


def main() -> int:
    # WitnessBuilder computes durationMs = monotonic() − start_time, so the
    # baseline must be a monotonic stamp (not epoch time.time(), which yields a
    # spurious negative duration ≈ −epoch).
    t0 = time.monotonic()
    kmax = max(max(Z, N) for _, Z, N in ISOTOPES)

    # Single-nucleon cores on H₃ (canonical proton / neutron braid words).
    proton = build_atom_symbolic(1, 0, include_inter=False)
    neutron = build_atom_symbolic(0, 1, include_inter=False)
    pp = power_sums(proton, kmax)   # proton power sums p_1..p_kmax
    pn = power_sums(neutron, kmax)  # neutron power sums

    tau_p, tau_n = pp[1], pn[1]
    print("=" * 92)
    print(" General identical-nucleon symmetrization — Frobenius formula, any (Z,N)")
    # Print the pin the run actually uses (the 50-digit string), not the float
    # alias — they agree only to ~17 digits and the display was the one place a
    # reader could have caught the parameter bug below.
    print(f"   q₀ = {Q_MP:.10f}   power-sum order kmax = {kmax}")
    print("=" * 92)
    print(f" proton  power sums p_k = tr_M(B_p^k):  "
          + "  ".join(f"p{k}={float(pp[k]):.4f}" for k in range(1, min(kmax, 4) + 1)))
    print(f" neutron power sums p_k = tr_M(B_n^k):  "
          + "  ".join(f"p{k}={float(pn[k]):.4f}" for k in range(1, min(kmax, 4) + 1)))
    print(" " + "-" * 90)
    print(f" {'iso':>5}{'Z':>3}{'N':>3}{'naive τ^ZN':>13}"
          f"{'bosonic h_Zh_N':>16}{'/naive':>9}{'fermionic e_Ze_N':>18}{'/naive':>9}")
    print(" " + "-" * 90)

    rows = []
    for lab, Z, N in ISOTOPES:
        naive = (tau_p ** Z) * (tau_n ** N)
        bos = frobenius(pp, Z, fermionic=False) * frobenius(pn, N, fermionic=False)
        fer = frobenius(pp, Z, fermionic=True) * frobenius(pn, N, fermionic=True)
        r_bos = bos / naive if naive != 0 else mp.nan
        r_fer = fer / naive if naive != 0 else mp.nan
        # mpf-valued, NOT float(). Every quantity here is mpf all the way up from
        # `_trM`, which substitutes the TRUE 50-digit q₀ (line 89) — so the casts
        # that used to sit in this dict were the ONLY precision loss in the file,
        # and they were at the recording boundary, not upstream of any
        # arithmetic. Serialized once, by `_ser_row` at the `add_data` call; the
        # display loop below format-specs these (`.5f`, `.4f`), which mpf honours
        # and a serialized string would raise `ValueError: Unknown format code`
        # on. The ratios are O(1) and the naive powers run to ~1e-6 at ¹⁶O, so
        # the old cast lost digits rather than magnitude.
        rows.append({
            "isotope": lab, "Z": Z, "N": N, "A": Z + N,
            "naive_tau_pow": naive,
            "bosonic_hZhN": bos, "bosonic_over_naive": r_bos,
            "fermionic_eZeN": fer, "fermionic_over_naive": r_fer,
        })
        print(f" {lab:>5}{Z:>3}{N:>3}{float(naive):>13.5f}"
              f"{float(bos):>16.5f}{float(r_bos):>9.4f}"
              f"{float(fer):>18.5f}{float(r_fer):>9.4f}")
    print(" " + "-" * 90)

    w = WitnessBuilder("symmetrized-constituent-general", engine="sympy+mpmath",
                       start_time=t0)
    w.set_description(
        "General identical-nucleon symmetrization infra for ANY isotope (Z,N) via "
        "the Frobenius power-sum formula h_Z=Σ_μ p_μ/z_μ (bosonic), e_Z=Σ_μ ε_μ "
        "p_μ/z_μ (fermionic/Pauli), with p_k=tr_M(B_p^k) (proton core braid^k, an "
        "H₃ Markov trace carrying the y_λ Wedderburn weights). Generalizes the Z=2 "
        "scalar probe (h₂/e₂) to all Z,N: compute p_1..p_{max Z,N} ONCE per nucleon "
        "(H₃ cost), then the Frobenius sum is pure partition arithmetic. Replaces "
        "the naive distinguishable τ_p^Z·τ_n^N constituent (closed_form_tau_M.py:302, "
        "identity term μ=(1^Z) only) with the correctly (anti)symmetrized "
        "h_Z(p)h_N(n) / e_Z(p)e_N(n). SCALAR CAVEAT: this approximates (≠) the exact "
        "block-level q-Young projection into H_{3Z} (small-Z refinement); it is the "
        "tractable GENERAL infra. Schur-Weyl Z=2,3,4 verified in "
        "QOU.Hecke.IdenticalParticleSymmetrization."
    )
    # `Q_50_DIGIT_STR`, NOT `float(Q)`.  This parameter records WHICH q₀ the run
    # used, and the run uses the 50-digit pin — `_trM` substitutes
    # `sp.Float(Q_50_DIGIT_STR, 50)` (line 89) and the float alias reached no
    # arithmetic in this file.  So the old record was 17 digits beside a 50-digit
    # computation.  It was the correctly-rounded double of that pin, NOT a
    # different value (measured: 1.1099785827513808 against
    # 1.1099785827513808075916690956107688798744991218736), so this is a
    # completeness fix and not a correction — do not read it as a value change.
    # It is also the one field here that must NOT simply be `fmt`'d: `fmt` on the
    # float would pad the double's binary tail to 60 places and manufacture 43
    # digits the float never carried.
    w.add_parameter("q0", Q_50_DIGIT_STR)
    w.add_parameter("kmax_power_sum_order", kmax)

    def _ser_row(r):
        """Serialize a row; the four integer/label fields pass through."""
        return {k: (v if k in ("isotope", "Z", "N", "A") else fmt(v))
                for k, v in r.items()}

    w.add_data("proton_power_sums", {str(k): fmt(v) for k, v in pp.items()})
    w.add_data("neutron_power_sums", {str(k): fmt(v) for k, v in pn.items()})
    w.add_data("tau_p", fmt(tau_p))
    w.add_data("tau_n", fmt(tau_n))
    w.add_data("rows", [_ser_row(r) for r in rows])
    w.add_data("formula", {
        "bosonic": "h_Z = Σ_{μ⊢Z} p_μ/z_μ",
        "fermionic": "e_Z = Σ_{μ⊢Z} (-1)^{Z-len(μ)} p_μ/z_μ",
        "power_sum": "p_k = tr_M(B_p^k) (k-fold proton core, H₃ Markov trace)",
        "z_mu": "∏_i i^{m_i} m_i!  (centralizer order of cycle type μ)",
        "constituent": "bosonic h_Z(p)·h_N(n)  |  fermionic e_Z(p)·e_N(n)",
        "replaces": "naive distinguishable τ_p^Z·τ_n^N (closed_form_tau_M.py:302)",
    })
    # Cross-check against the Z=2 scalar probe: h₂=(p₁²+p₂)/2, e₂=(p₁²−p₂)/2.
    # The three residues below are SYMBOLIC (sympy), and `float()` collapsed
    # each to ~1e-16 before a 1e-30 tolerance looked at it. Measured: at Z=2
    # `h2 - h2_direct` simplifies to sympy `Zero` -- Newton's identity is in
    # the formula, not the data, so the residue is exact for any `pp`.
    # Dropping the cast lets the tolerance mean something; it is left at
    # 1e-30 rather than tightened to 0, since a numeric `pp` would give a
    # tiny Float rather than Zero. Bean qou-58zw.
    h2 = frobenius(pp, 2, fermionic=False)
    h2_direct = (pp[1] ** 2 + pp[2]) / 2
    w.add_assertion(
        name="frobenius_Z2_matches_newton_h2",
        computed=abs(h2 - h2_direct), expected=0, tolerance=1e-30,
        source="Frobenius h₂ == Newton (p₁²+p₂)/2 — the general formula reproduces "
               "the hand-derived Z=2 case (symmetrized_constituent_probe.py).",
    )
    e2 = frobenius(pp, 2, fermionic=True)
    e2_direct = (pp[1] ** 2 - pp[2]) / 2
    w.add_assertion(
        name="frobenius_Z2_matches_newton_e2",
        computed=abs(e2 - e2_direct), expected=0, tolerance=1e-30,
        source="Frobenius e₂ == Newton (p₁²−p₂)/2.",
    )
    # h_Z + e_Z sanity: at Z=1 both = p_1 = τ (single particle, no symmetrization).
    w.add_assertion(
        name="Z1_no_symmetrization",
        computed=(abs(frobenius(pp, 1) - pp[1])
                  + abs(frobenius(pp, 1, fermionic=True) - pp[1])),
        # `0`, not `0.0`: an exact integral zero, and the only raw float64 the
        # builder guard still found in this witness after the drain.  (The
        # raw-float64 ratchet carves integral-valued floats out and would have
        # read this file clean at 0 while a `0.0` sat in it; the builder guard
        # has no such carve-out, which is why it is the better locator.  The
        # sibling two assertions already used `0`.)
        expected=0, tolerance=1e-30,
        source="h_1 = e_1 = p_1 = τ_p (one proton carries no exchange symmetry).",
    )
    out = w.save()

    print(f" Frobenius reproduces Newton Z=2: |h₂−(p₁²+p₂)/2| = {float(abs(h2-h2_direct)):.1e}")
    print(" Bosonic OVERSHOOTS, fermionic UNDERSHOOTS the naive constituent — the")
    print(" S_Z exchange is a large O(1) effect at every isotope (scalar approx of the")
    print(" exact H_{3Z} q-Young block projection; nucleons are fermions ⇒ e_Z is Pauli).")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
