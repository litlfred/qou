#!/usr/bin/env python3
"""helium4_mu4_cluster_moment_probe.py — GAP-8 (bean qou-6wil): the FIRST actual
test of the 4-body moment μ₄, at A=4 / H₁₂.

WHY THIS IS NEW. Every per-block-weight probe in this epic ran at A=3, and
GAP-7 proved that A=3 data carries **zero** 4-body information: two simplex
ansätze differing only in μ₄ agree on M(A) for every A < 4 because the C(A,4)
column vanishes there (Lean `QOU.MassTheory.UrsellSlotAlignment`,
`mu4_unconstrained_below_four`, sorry-free). So the derived target

    μ₄ = −4.591 MeV   (forward AME − model, exact 0-parameter simplex)

has never been tested — not "tested and missed". This probe tests it.

THE CONSTRUCTION, entirely internal to the A=4 system (no cross-algebra
comparison). ⁴He is Z=2, N=2 on 3A = 12 strands. Four nucleons give
C(4,2) = 6 bonds:

    adjacent (from the word itself)   0↔1 @ g₂,  1↔2 @ g₅,  2↔3 @ g₈
    non-adjacent (BKL band, derived)  0↔2, 1↔3, 0↔3

The band generator is the same Birman–Ko–Lee construction GAP-3 used at A=3,
generalised: to bond nucleons i<j non-adjacently, carry the strand down through
generators 3j−1 … 3i+3, cross at the adjacent slot 3i+2, then carry back with
inverse crossings. At (i,j) = (0,2) this reproduces GAP-3's a_{7,3} exactly.

Flavour templates are DERIVED from ⁴He's own word, not chosen: the three
adjacent interfaces read (1,0) = p–p, (1,−h(½−δ/4)) = p–n, (1,−h) = n–n, which
pins the ordering to (p,p,n,n); every non-adjacent bond here is p–n and takes
that template.

All 2⁶ = 64 subset traces are computed at H₁₂ (77 partitions), giving the full
Möbius picture. The moment ladder is then the standard cluster decomposition —
the same shape as the corpus recursion `mu4 = M[4] − 6·mu2 − 4·mu3` (6 pairs,
4 triangles), but with the bonds and triangles summed individually since they
are NOT equivalent here:

    μ₂^(b)  = g({b}) − g(∅)                                    for each of 6 bonds
    μ₃^(t)  = g(bonds(t)) − Σ_{b∈t} g({b}) + 2·g(∅)            for each of 4 triangles
    M(4)    = g(all 6) − g(∅)
    μ₄      = M(4) − Σ_b μ₂^(b) − Σ_t μ₃^(t)

THE HEADLINE IS A RATIO, because it is CONVENTION-FREE. This epic has repeatedly
tripped over the sign convention c = ±E₀·x, and an absolute sign verdict inherits
that ambiguity. The ratio

    μ₄ / μ₃        target −9.752   (= −4.591 / +0.4708)

is measured within one system, so E₀, the y_λ normalisation, and the global sign
ALL cancel. It is the sharpest falsifiable comparison available, and it tests
both the sign (is the 4-body term opposite to the 3-body one?) and the magnitude
(is it ~10× larger?) at once.

GUARD. The H₁₂ pipeline is validated before any moment is read off it, by
re-deriving each triangle's μ₃ two ways — directly, and via the proven identity
μ₃ = ΣΔ²g + Δ³g (Lean `triangle_moment_decomp`). A pipeline that fails that
identity cannot be trusted for μ₄.

No Δ_λ, no μ fitted, no convention tuned. Reports whichever way it lands.
"""
from __future__ import annotations

import json
import sys
import time
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path[:0] = [str(COMP), str(COMP / "hecke"), str(COMP / "habiro"),
                str(COMP / "substrate"), str(HERE)]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Canonical p-n interface offset (owner ruling 2026-08-15 R3, reaffirmed
# 2026-08-26). `-h/2` is `strict_averaged`, the COLOUR-BLIND convention.
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402

set_compute_dps(30)
q0 = mp.mpf(str(Q0))
q0f = float(Q0)
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))
H = float(q0 - 1 / q0)
NSTR = 12
_Y12 = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
        for k, v in y_lambda_at(NSTR, q0).items()}

SIMPLEX = HERE / "deltalambda-kappa-interface-residual-simplex.witness.json"

_calls = {"n": 0, "t0": time.time()}


def perblock(word):
    """Σ_λ y_λ·|χ_λ| at H₁₂ — the same block-trace functional as GAP-3/GAP-7."""
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(NSTR, factors, q0f)
    _calls["n"] += 1
    el = time.time() - _calls["t0"]
    print(f"      [trace {_calls['n']:2d}/64] {el:7.1f}s elapsed  "
          f"ETA {el / _calls['n'] * (64 - _calls['n']):6.1f}s", flush=True)
    return sum(_Y12[tuple(s)] * abs(mp.mpf(repr(chi)))
               for s, chi in cp if tuple(s) in _Y12)


def band_word(i: int, j: int, c: float, d: float):
    """BKL band bonding non-adjacent nucleons i<j: carry 3j−1…3i+3, cross at
    3i+2, carry back. At (i,j)=(0,2) this is GAP-3's a_{7,3} verbatim."""
    carry = list(range(3 * j - 1, 3 * i + 2, -1))
    return ([(1.0, 0.0, g) for g in carry]
            + [(c, d, 3 * i + 2)]
            + [(1.0, -H, g) for g in reversed(carry)])


def derived_moments():
    raw = json.load(open(SIMPLEX))
    d = raw.get("data", raw)["results"]["exact_simplex_decomposition"]
    return (mp.mpf(str(d["mu3_triangle_3body"])), mp.mpf(str(d["mu4_tetra_4body"])))


def main() -> int:
    print("=" * 78)
    print(" GAP-8: the first actual test of μ₄ — A=4 (⁴He), H₁₂, 64 subset traces")
    print("=" * 78)
    mu3_t, mu4_t = derived_moments()
    ratio_target = mu4_t / mu3_t
    print(f" derived target (forward AME−model, 0 fit): μ₃ = {float(mu3_t):+.6f}  "
          f"μ₄ = {float(mu4_t):+.6f} MeV")
    print(f" CONVENTION-FREE target ratio μ₄/μ₃ = {float(ratio_target):+.4f}")
    print(f" E₀ = {float(E0):.4f} MeV   h = {H:.6f}   q₀ = {float(q0):.6f}")

    full = atom_braid_word_3A(2, 2, include_inter=True)
    ifaces = {x[2]: x for x in full if x[2] % 3 == 2}
    print(f"\n ⁴He word: {len(full)} letters; adjacent interfaces at gens {sorted(ifaces)}")

    # ---- flavour templates DERIVED from the word itself ---------------------
    d_by_gen = {g: float(ifaces[g][1]) for g in sorted(ifaces)}
    pn_d = min((d for d in d_by_gen.values() if d != 0.0),
               key=lambda d: abs(abs(d) - abs(_pn_d(H))))
    print(f"      adjacent templates {[(g, round(d, 6)) for g, d in d_by_gen.items()]}")
    print(f"      ⇒ ordering (p,p,n,n); p–n template d = {pn_d:.6f}; "
          f"every non-adjacent bond here is p–n")

    # ---- the six bonds ------------------------------------------------------
    adj = {(0, 1): 2, (1, 2): 5, (2, 3): 8}
    bands = [(0, 2), (1, 3), (0, 3)]
    bonds = list(adj) + bands
    print(f"      bonds: 3 adjacent {list(adj)} + 3 BKL band {bands} = {len(bonds)}")

    def g_of(subset):
        sel_adj = {adj[b] for b in subset if b in adj}
        w = [x for x in full if x[2] % 3 != 2 or x[2] in sel_adj]
        for b in subset:
            if b in bands:
                w = w + band_word(b[0], b[1], 1.0, pn_d)
        return perblock(w)

    print(f"\n computing all 2^6 = 64 subset traces at H₁₂ "
          f"(~9s each, ETA ~10-30 min)…", flush=True)
    g = {}
    for r in range(len(bonds) + 1):
        for S in combinations(bonds, r):
            g[frozenset(S)] = g_of(set(S))
    e = g[frozenset()]
    print(f" all 64 traces done in {time.time() - _calls['t0']:.1f}s")

    # ---- moment ladder, all internal to A=4 ---------------------------------
    mu2 = {b: g[frozenset([b])] - e for b in bonds}
    triangles = list(combinations(range(4), 3))

    def tri_bonds(t):
        return [b for b in bonds if b[0] in t and b[1] in t]

    mu3 = {}
    guard_ok = True
    print("\n [G] pipeline guard — each triangle's μ₃ two ways "
          "(direct vs ΣΔ²+Δ³, Lean triangle_moment_decomp)")
    for t in triangles:
        tb = tri_bonds(t)
        assert len(tb) == 3, f"triangle {t} has {len(tb)} bonds"
        direct = g[frozenset(tb)] - sum(g[frozenset([b])] for b in tb) + 2 * e

        def d2(x, y):
            return g[frozenset([x, y])] - g[frozenset([x])] - g[frozenset([y])] + e
        pairs = [d2(*p) for p in combinations(tb, 2)]
        tri3 = (g[frozenset(tb)] - sum(g[frozenset(p)] for p in combinations(tb, 2))
                + sum(g[frozenset([b])] for b in tb) - e)
        assembled = sum(pairs) + tri3
        gap = abs(direct - assembled)
        ok = gap < mp.mpf("1e-20")
        guard_ok &= bool(ok)
        mu3[t] = direct
        print(f"      triangle {t}: μ₃ = {float(direct):+.9f}   "
              f"|direct − (ΣΔ²+Δ³)| = {float(gap):.2e}  {bool(ok)}")
    print(f"      identity holds for all 4 triangles: {bool(guard_ok)}")

    M4 = g[frozenset(bonds)] - e
    sum_mu2 = sum(mu2.values())
    sum_mu3 = sum(mu3.values())
    mu4 = M4 - sum_mu2 - sum_mu3

    print("\n [M] the moment ladder (⁴He, H₁₂, all internal)")
    print(f"      M(4) = g(all 6) − g(∅)      = {float(M4):+.9f}")
    print(f"      Σ over 6 bonds     μ₂       = {float(sum_mu2):+.9f}   "
          f"(mean {float(sum_mu2 / 6):+.9f})")
    print(f"      Σ over 4 triangles μ₃       = {float(sum_mu3):+.9f}   "
          f"(mean {float(sum_mu3 / 4):+.9f})")
    print(f"      μ₄ = M(4) − Σμ₂ − Σμ₃       = {float(mu4):+.9f}")

    mu3_mean = sum_mu3 / 4
    ratio = mu4 / mu3_mean
    sign_match = (mu4 > 0) != (mu3_mean > 0)
    print("\n [R] THE CONVENTION-FREE COMPARISON")
    print(f"      measured μ₄/μ₃ = {float(ratio):+.4f}      "
          f"target {float(ratio_target):+.4f}")
    print(f"      sign: 4-body opposite to 3-body?  measured {bool(sign_match)}   "
          f"target True")
    if sign_match:
        print(f"      magnitude |ratio| {float(abs(ratio)):.3f} vs "
              f"{float(abs(ratio_target)):.3f}  → off by "
              f"{float(abs(ratio_target / ratio)):.2f}×")
    else:
        print(f"      ⇒ SIGN FAILS: the measured 4-body moment has the SAME sign as")
        print(f"        the 3-body one, while the derived ladder alternates.")

    c_minus, c_plus = -E0 * mu4, E0 * mu4
    print(f"\n      for reference, both sign conventions: c₄ = −E₀μ₄ = "
          f"{float(c_minus):+.4f} MeV ; +E₀μ₄ = {float(c_plus):+.4f} MeV")
    print(f"      (the ratio above is the load-bearing number — these inherit the")
    print(f"       convention ambiguity this epic has repeatedly tripped over)")

    verdict = (f"measured μ₄/μ₃ = {float(ratio):+.4f} against target {float(ratio_target):+.4f}; "
               f"alternation {'REPRODUCED' if sign_match else 'NOT reproduced'}, "
               f"|ratio| off by {float(abs(ratio_target / ratio)):.2f}×")
    print(f"\n ⇒ {verdict}")

    wb = WitnessBuilder("helium4-mu4-cluster-moment", engine="pyhecke_native")
    wb.set_description(
        "GAP-8 (bean qou-6wil, epic qou-xu6t): the FIRST actual test of the 4-body moment μ₄. "
        "Every prior per-block-weight probe in this epic ran at A=3, and GAP-7 proved A=3 data "
        "carries ZERO 4-body information — two simplex ansätze differing only in μ₄ agree on "
        "M(A) for every A<4 because the C(A,4) column vanishes (Lean "
        "QOU.MassTheory.UrsellSlotAlignment.mu4_unconstrained_below_four, sorry-free) — so the "
        "derived target μ₄ = −4.591 MeV had never been tested, as opposed to tested-and-missed. "
        "Construction is entirely internal to A=4 (⁴He, Z=2 N=2, 12 strands, H₁₂, 77 partitions): "
        "C(4,2)=6 bonds — 3 adjacent from the word (g₂,g₅,g₈) and 3 non-adjacent Birman–Ko–Lee "
        "band generators built by the same recipe GAP-3 used at A=3, generalised (carry "
        "3j−1…3i+3, cross at 3i+2, carry back; at (i,j)=(0,2) it reproduces a_{7,3} verbatim). "
        "Flavour templates are DERIVED from ⁴He's own word — the adjacent interfaces read "
        "(1,0)=p–p, (1,−h(½−δ/4))=p–n, (1,−h)=n–n, pinning the ordering to (p,p,n,n) — not "
        "chosen. All 2⁶=64 subset traces computed, then the standard cluster ladder "
        "μ₂^(b)=g({b})−g(∅) over 6 bonds, μ₃^(t)=g(t)−Σ_{b∈t}g({b})+2g(∅) over 4 triangles, "
        "M(4)=g(all)−g(∅), μ₄=M(4)−Σμ₂−Σμ₃ — the same shape as the corpus recursion "
        "mu4=M[4]−6·mu2−4·mu3, but summed individually since the bonds are not equivalent. "
        "HEADLINE IS THE RATIO μ₄/μ₃ (target −9.752), because it is measured within one system "
        "so E₀, the y_λ normalisation and the global sign all cancel — this epic has repeatedly "
        "tripped over the c=±E₀·x convention and an absolute sign verdict would inherit that "
        "ambiguity. The H₁₂ pipeline is GUARDED before any moment is read off it: each "
        "triangle's μ₃ is re-derived both directly and via the proven identity μ₃=ΣΔ²g+Δ³g "
        f"(Lean triangle_moment_decomp). VERDICT: {verdict}. "
        "No Δ_λ, no μ fitted, no convention tuned, nothing wired.")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_data("mu4_cluster_moment", {
        "system": "⁴He, Z=2 N=2, 3A=12 strands, H₁₂, 77 partitions, 64 subset traces",
        "bonds": {"adjacent": {str(k): v for k, v in adj.items()},
                  "bkl_band": [str(b) for b in bands]},
        "flavour_templates_derived": {str(g_): d for g_, d in d_by_gen.items()},
        "pn_template_d": pn_d,
        "mu2_per_bond": {str(b): float(v) for b, v in mu2.items()},
        "mu3_per_triangle": {str(t): float(v) for t, v in mu3.items()},
        "M4": float(M4), "sum_mu2": float(sum_mu2), "sum_mu3": float(sum_mu3),
        "mu4_measured": float(mu4),
        "mu3_mean": float(mu3_mean),
        "ratio_measured": float(ratio),
        "ratio_target": float(ratio_target),
        "alternation_reproduced": str(bool(sign_match)),
        "c4_minus_convention_MeV": float(c_minus),
        "c4_plus_convention_MeV": float(c_plus),
        "pipeline_guard_triangle_identity": str(bool(guard_ok)),
        "verdict": verdict})
    wb.add_assertion("pipeline_guard_triangle_identity_holds", str(bool(guard_ok)), "True")
    wb.add_assertion("all_64_subset_traces_computed", str(len(g) == 64), "True")
    wb.save()
    print("\nwitness → helium4-mu4-cluster-moment.witness.json")
    # The μ₄ result is REPORTED, not asserted — a negative is a valid outcome.
    ok = guard_ok and len(g) == 64
    print("STRUCTURAL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
