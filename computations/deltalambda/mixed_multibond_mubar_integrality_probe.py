#!/usr/bin/env python3
"""
mixed_multibond_mubar_integrality_probe.py — the μ̄-idempotent hypothesis for the
mixed-multibond shared channel, tested against Milnor INTEGRALITY.

Owner steer (2026-07-18): "work on derived μ̄-idempotent / SDP-knot-ID invariant."

Context. The mixed-multibond miss (Model G open trio, audit
`2026-07-14-mixed-multibond-interface-derive-or-refute.md`) is a shared,
sub-additive channel. Next-step #1 there: "one |μ̄|-idempotent per light cluster,
not per bond" — i.e. the shared channel is the Milnor triple-linking (μ̄_ijk)
content of the light cluster bridging m α's. This probe tests the SIMPLEST such
form and — using the corpus's own Magnus μ̄ machinery
(`binding_mn_milnor_linking.py`) — refutes it, narrowing what the invariant can be.

The test (formalize-first, no fit). A light cluster X bridging m α's carries
C(m,2) potential Borromean triples (αᵢ, αⱼ, X). Milnor μ̄_ijk is an INTEGER
(coefficient in a Magnus expansion — verified here on Hopf/Borromean/chain). So the
simplest μ̄-idempotent — a COMMON scalar weight w times the (signed) integer count
of triples — predicts

    channel(m) = w · S(m),   S(m) ∈ ℤ,  |S(m)| ≤ C(m,2).

With the single triple at m=2 as the unit (w = channel(2)), channel(m)/w must be
an INTEGER for every m. It is not:

    m=2 → 1.00 (unit) ; m=3 → 1.22 ; m=4 → 0.35   (t-series ⁷Li,¹¹B,¹⁵N,¹⁹F).

¹⁹F sits at 0.35 of the unit — nearest integer 0, but the channel is 2.26 MeV ≠ 0.
Robust to ±5% (b,g) calibration (see below). So the bare-topological
μ̄-idempotent (common weight × integer triple count) does NOT reproduce the
t-series.

Verdict (scope-(a), NOT (b)). This refutes the μ̄-idempotent with a COMMON scalar
weight and an integer Borromean-triple count. It does NOT exclude the μ̄-idempotent
INGREDIENT: a q-WEIGHTED per-triple magnitude (each triple dressed by its own
per-block q-weight a_D^(2)·w_2 / Hoefsmit block, per binding_production_link_milnor
Part-6) is not tested here and survives — but that dressing is exactly the
confinement-SDP per-block weight (the environment-blocked 9b piece), so the
derivation genuinely needs the SDP weights, not just the link topology. Cited
invariant: μ̄_ijk ∈ ℤ (Milnor 1954; Magnus integrality).

EXPLORATORY — no production wiring, no fitted constant, no tier change.
"""
from __future__ import annotations
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from mpmath import mp  # noqa: E402
from codata_constants import _ame_binding_mev  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ── Magnus μ̄ machinery (replicated from binding_mn_milnor_linking.py) ──────────
D = 3


def _mul(p, r):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in r.items():
            m = m1 + m2
            if len(m) <= D:
                out[m] = out.get(m, 0) + c1 * c2
    return {m: c for m, c in out.items() if c != 0}


def _magnus_gen(i, sign):
    p = {(): 1}
    if sign > 0:
        p[(i,)] = 1
    else:
        for d in range(1, D + 1):
            p[tuple([i] * d)] = (-1) ** d
    return p


def _magnus_word(word):
    p = {(): 1}
    for g, e in word:
        p = _mul(p, _magnus_gen(g, e))
    return p


def _comm(a, b):
    return [(a, 1), (b, 1), (a, -1), (b, -1)]


def _mu(longitudes, seq):
    *pre, last = seq
    return _magnus_word(longitudes[last]).get(tuple(pre), 0)


BORROMEAN = {1: _comm(2, 3), 2: _comm(3, 1), 3: _comm(1, 2)}
CHAIN = {1: [(2, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1)]}


def _B(za):
    return _ame_binding_mev(*za)


def main() -> int:
    print("=== μ̄-idempotent for the mixed-multibond channel: integrality test ===\n")

    # (0) confirm Milnor μ̄ is an INTEGER on the reference links (the cited invariant)
    bor = _mu(BORROMEAN, (1, 2, 3))
    chain = _mu(CHAIN, (1, 2, 3))
    integrality = all(isinstance(x, int) for x in (bor, chain)) and abs(bor) == 1 and chain == 0
    print(f"[0] Milnor μ̄ integrality (Magnus): Borromean μ̄_123 = {bor} (int, |·|=1), "
          f"chain μ̄_123 = {chain} (int, 0)  → μ̄ ∈ ℤ  {'✓' if integrality else '✗'}")

    # (1) the pure t-series shared channel (single light cluster = triton, A_light=3)
    ALPHA, T = (2, 4), (1, 3)
    b, g = mp.mpf("0.78192"), mp.mpf("2.4155")
    series = [("7Li", 3, 7, 1), ("11B", 5, 11, 2), ("15N", 7, 15, 3), ("19F", 9, 19, 4)]
    ch = {}
    print("\n[1] t-series shared channel  (miss = deficit − b·3·m − g·C(m,2)[m≥3]):")
    print(f"    {'iso':>5}{'m':>3}{'C(m,2)':>8}{'channel(MeV)':>14}")
    for name, Z, A, m in series:
        deficit = _B((Z, A)) - m * _B(ALPHA) - _B(T)
        c = float(deficit - b * 3 * m - (g * comb(m, 2) if m >= 3 else mp.mpf(0)))
        ch[m] = c
        print(f"    {name:>5}{m:>3}{comb(m, 2):>8}{c:>14.4f}")

    # (2) integer-multiple test: with the m=2 single triple as unit w, channel/w ∈ ℤ?
    w = ch[2]
    print(f"\n[2] μ̄-idempotent (common weight × integer triple count): unit w = channel(2) "
          f"= {w:.4f} MeV/triple")
    max_resid_frac = 0.0
    for m in (3, 4):
        ratio = ch[m] / w
        near = round(ratio)
        resid = abs(ratio - near)
        # relative to the unit (not to the value) — the honest "is it an integer" metric
        max_resid_frac = max(max_resid_frac, resid)
        print(f"    m={m}: channel/w = {ratio:.4f}  nearest int {near}  |off| = {resid:.4f} triples "
              f"(allowed |S| ≤ {comb(m, 2)})")
    is_integer_multiple = max_resid_frac < 0.10  # within 0.1 of an integer triple count
    print(f"    → integer-triple-multiple? {'YES' if is_integer_multiple else 'NO'} "
          f"(worst offset {max_resid_frac:.3f} triples from ℤ)")

    # (3) robustness of the NO to ±5% (b,g)
    print("\n[3] robustness of the refutation to ±5% (b,g):")
    robust_no = True
    for db, dg in [(-0.05, -0.05), (0.05, 0.05), (-0.05, 0.05), (0.05, -0.05)]:
        bb, gg = b * (1 + db), g * (1 + dg)
        vals = {}
        for name, Z, A, m in series:
            deficit = _B((Z, A)) - m * _B(ALPHA) - _B(T)
            vals[m] = float(deficit - bb * 3 * m - (gg * comb(m, 2) if m >= 3 else mp.mpf(0)))
        ww = vals[2]
        offs = [abs(vals[m] / ww - round(vals[m] / ww)) for m in (3, 4)]
        this_integer = max(offs) < 0.10
        robust_no &= (not this_integer)
        print(f"    (b{db:+.0%},g{dg:+.0%}): m=3 {vals[3]/ww:.3f}, m=4 {vals[4]/ww:.3f} "
              f"→ integer? {'yes' if this_integer else 'no'}")
    print(f"    → refutation robust across all corners: {robust_no}")

    ok = integrality and (not is_integer_multiple) and robust_no
    print(f"\nVERDICT (scope-(a)): the simple μ̄-idempotent (common weight × integer "
          f"Borromean-triple count) does {'NOT' if ok else '(?)'} reproduce the t-series "
          f"shared channel.\n  ¹⁹F needs 0.35 triples (nearest int 0, but channel = "
          f"{ch[4]:.2f} MeV ≠ 0); the values are not a common-scale ℤ multiple.\n"
          f"  The invariant must carry a q-WEIGHTED per-triple magnitude (the SDP per-block "
          f"weight) — the bare topological Borromean count is insufficient. μ̄-idempotent\n"
          f"  INGREDIENT not excluded; only the common-scalar-weight form is.")

    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("mixed-multibond-mubar-integrality", engine="python-magnus")
        wb.set_description(
            "EXPLORATORY: tests the μ̄-idempotent hypothesis for the mixed-multibond "
            "shared channel against Milnor integrality. μ̄_ijk ∈ ℤ (Magnus, verified on "
            "Borromean/chain). The t-series shared channel {6.44, 7.84, 2.26} MeV (¹¹B/¹⁵N/¹⁹F) "
            "is NOT a common-scale integer-triple multiple (¹⁹F = 0.35 units, nearest int 0 "
            "≠ nonzero channel; robust to ±5% b,g). Refutes the common-scalar-weight × "
            "integer Borromean-count form (scope-(a)); the μ̄-idempotent must be q-weighted "
            "per triple (the SDP per-block weight). No fit, no wire.")
        wb.add_data("mu_bar_integrality", {"borromean_123": bor, "chain_123": chain})
        wb.add_data("t_series_channel_MeV", {f"m={m}": round(v, 4) for m, v in ch.items()})
        wb.add_data("channel_over_unit", {f"m={m}": round(ch[m] / w, 4) for m in (2, 3, 4)})
        wb.add_assertion(
            name="mubar_idempotent_common_weight_refuted",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Milnor μ̄∈ℤ; t-series shared channel is not a common-scale integer "
                    "Borromean-triple multiple (¹⁹F 0.35 units, robust to ±5% b,g). The "
                    "common-scalar-weight μ̄-idempotent is refuted (scope-(a)); the invariant "
                    "needs a q-weighted per-triple magnitude (SDP per-block weight)."))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness emit skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
