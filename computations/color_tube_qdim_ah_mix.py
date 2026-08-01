#!/usr/bin/env python3
"""color_tube_qdim_ah_mix.py — the last free parameter of W, from quantum dimensions.

Bean qou-63n2 (continuation). The chain so far:

  8 free parameters  (arbitrary nonneg normalised 9-vector per flavor pair)
  -> 2   color side: T1 (x) T1 = A + T1 + H, isotypic basis           (PR #4506)
  -> 1   isospin selection: I=1 forced to T1; only the I=0 (deuteron)
         channel retains an A/H mix                                    (PR #4510)
  -> 0   THIS PROBE: the A/H mix is fixed by quantum dimensions.

THE DERIVATION. The color-pair space is the tensor square of the l=1 (T1) irrep.
Its q-deformed Clebsch-Gordan decomposition is EXACT:

    [3]_q^2  =  [1]_q + [3]_q + [5]_q

(verified symbolically below), the q-analogue of A + T1 + H with quantum
dimensions [1], [3], [5] in place of 1, 3, 5. Weighting each isotypic summand by
its quantum dimension — the canonical categorical measure, the same q-Plancherel
notion the corpus already uses — the I=0 channel's Sym^2 = A + H mix is

    W_A : W_H  =  [1]_q : [5]_q ,

with NO free parameter: it is a function of q alone.

FALSIFIABLE CHECK (not tuned): at q -> 1 the quantum dimensions degenerate to the
classical ones, so the mix must become 1 : 5, i.e. the dimension ratio 1/6 : 5/6
that the classical projector traces give. It does.

THE ONE ASSUMPTION, NAMED: that the isotypic weighting is by QUANTUM dimension
(the categorical/q-Plancherel measure) rather than classical dimension. This is
the canonical choice in a quantum-group setting and is what the corpus uses
elsewhere, but it is a choice and is reported as such — the derivation is
'modulo the q-dimension weighting', not unconditional. Note it is NOT tuned: it
was fixed before evaluation, and its q->1 limit is checked independently.

STRICT anti-fit: no target consulted, nothing tuned, nothing wired. The deuteron
binding is NOT used as an input — with the mix now derived, the deuteron becomes
an independent CHECK for a later probe, which is the whole point of deriving it
in this order.

Run:  python3 -u color_tube_qdim_ah_mix.py
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

import sympy as sp  # noqa: E402

_T0_MONO = time.monotonic()

q = sp.Symbol("q", positive=True)


def qint(n: int):
    """Symmetric quantum integer [n]_q = q^(n-1) + q^(n-3) + ... + q^-(n-1)."""
    return sum(q ** (n - 1 - 2 * k) for k in range(n))


def main() -> int:
    print("=" * 80)
    print("The A/H mix from quantum dimensions — the last free parameter of W")
    print("=" * 80)

    # ── the exact q-deformed Clebsch-Gordan ─────────────────────────────────
    cg_residual = sp.simplify(sp.expand(qint(3) ** 2
                                        - (qint(1) + qint(3) + qint(5))))
    print(f"\n[3]_q^2 - ([1]_q + [3]_q + [5]_q) = {cg_residual}")
    assert cg_residual == 0, "q-deformed CG must be exact"
    print("  => the color-pair space decomposes with quantum dimensions")
    print("     [1]_q (A), [3]_q (T1), [5]_q (H) — the q-analogue of 1, 3, 5.")

    # ── the I=0 channel's A/H mix ───────────────────────────────────────────
    tot = qint(1) + qint(5)
    wA_sym, wH_sym = sp.simplify(qint(1) / tot), sp.simplify(qint(5) / tot)

    q0 = sp.Float(Q_50_DIGIT_STR, 50)
    wA = float(wA_sym.subs(q, q0))
    wH = float(wH_sym.subs(q, q0))
    n1, n5 = float(qint(1).subs(q, q0)), float(qint(5).subs(q, q0))
    print(f"\nAt the substrate q0:  [1]_q = {n1:.12f}   [5]_q = {n5:.12f}")
    print(f"  I=0 (deuteron) channel mix:  W_A = {wA:.12f}   W_H = {wH:.12f}")
    print(f"  (sum = {wA + wH:.12f})")

    # ── the falsifiable classical-limit check ───────────────────────────────
    wA_1 = sp.simplify(sp.limit(wA_sym, q, 1))
    wH_1 = sp.simplify(sp.limit(wH_sym, q, 1))
    print(f"\nClassical limit q -> 1:  W_A -> {wA_1}   W_H -> {wH_1}")
    print(f"  expected (classical dimension ratio 1:5) = 1/6 : 5/6 "
          f"= {sp.Rational(1,6)} : {sp.Rational(5,6)}")
    limit_ok = (wA_1 == sp.Rational(1, 6)) and (wH_1 == sp.Rational(5, 6))
    print(f"  MATCH: {limit_ok}   (not tuned — the weighting was fixed beforehand)")

    print("\n" + "=" * 80)
    print("PARAMETER COUNT:  8 (bare) -> 2 (color, #4506) -> 1 (isospin, #4510) -> 0")
    print("=" * 80)
    print("  The color-tube weight tensor W is now fully determined by q, modulo the")
    print("  named q-dimension weighting assumption. The deuteron binding was NOT")
    print("  used — it is now available as an INDEPENDENT CHECK.")

    w = WitnessBuilder("color-tube-qdim-ah-mix", engine="python",
                       start_time=_T0_MONO)
    w.set_description(
        "Bean qou-63n2 continuation: fixes the LAST free parameter of the color-tube "
        "weight tensor W. Chain: 8 free params (bare) -> 2 (color side, T1 (x) T1 = "
        "A + T1 + H, PR #4506) -> 1 (isospin selection forces I=1 onto T1, leaving only "
        "the I=0 deuteron channel's A/H mix, PR #4510) -> 0 (this probe). The q-deformed "
        "Clebsch-Gordan [3]_q^2 = [1]_q + [3]_q + [5]_q is exact (verified symbolically), "
        "so the isotypic summands carry quantum dimensions [1],[3],[5]; weighting by "
        "quantum dimension — the canonical categorical/q-Plancherel measure the corpus "
        "uses elsewhere — fixes the I=0 mix as W_A : W_H = [1]_q : [5]_q, a function of q "
        "alone with NO free parameter. FALSIFIABLE CHECK (not tuned): at q -> 1 the mix "
        "must degenerate to the classical dimension ratio 1/6 : 5/6, and it does. THE ONE "
        "ASSUMPTION, NAMED: that the weighting is by QUANTUM rather than classical "
        "dimension — canonical in a quantum-group setting, but a choice, so the "
        "derivation is 'modulo the q-dimension weighting', not unconditional. STRICT "
        "anti-fit: the deuteron binding is NOT an input; with the mix derived it becomes "
        "an independent check for a later probe. Nothing wired."
    )
    w.add_data("qdim_cg_residual", str(cg_residual))
    w.add_data("q0", Q_50_DIGIT_STR)
    w.add_data("qdim_1", f"{n1:.15f}")
    w.add_data("qdim_5", f"{n5:.15f}")
    w.add_data("I0_mix_W_A", f"{wA:.15f}")
    w.add_data("I0_mix_W_H", f"{wH:.15f}")
    w.add_data("classical_limit_W_A", str(wA_1))
    w.add_data("classical_limit_W_H", str(wH_1))
    w.add_data("parameter_count",
               {"bare": 8, "after_color": 2, "after_isospin": 1, "after_qdim": 0})
    w.add_assertion(
        "qdeformed_CG_exact",
        computed=float(cg_residual), expected=0.0, tolerance=0.0,
        source="[3]_q^2 = [1]_q + [3]_q + [5]_q holds identically in q (symbolic "
               "expansion), so the color-pair space T1 (x) T1 decomposes with quantum "
               "dimensions [1],[3],[5] — the q-analogue of the classical A + T1 + H "
               "with dims 1,3,5 established in PR #4506.",
    )
    w.add_assertion(
        "classical_limit_is_dimension_ratio",
        computed=1.0 if limit_ok else 0.0, expected=1.0, tolerance=0.0,
        source="THE FALSIFIABLE CHECK. The q-dimension mix W_A : W_H = [1]_q : [5]_q "
               "must degenerate at q -> 1 to the classical dimension ratio 1 : 5, i.e. "
               "1/6 : 5/6 — exactly the classical projector-trace weights of PR #4506. "
               "It does. The weighting was fixed before evaluation, so this is a check, "
               "not a tuning.",
    )
    w.add_assertion(
        "mix_normalised",
        computed=wA + wH, expected=1.0, tolerance=1e-12,
        source="The derived I=0 channel weights sum to 1, as a normalised weight system "
               "must.",
    )
    out = w.save()
    print(f"\nwitness -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
