#!/usr/bin/env python3
"""Mirror-pair isospin splitting: Coulomb vs categorical chirality.

Symbolically proves (sympy) that the factorized q-CLT chirality split and the
Coulomb split share the isospin factor (Z-N)(A-1) but scale as A^-1 and A^-1/3
respectively, so the over-split is ~A^-2/3 — hence NO constant damping factor
kappa can map the categorical split onto the physical one. Numerically validates
against the 3H/3He (A=3) and 7Li/7Be (A=7) mirror pairs from AME2020: one Coulomb
length r0 ~ 1.6 fm fits both, where kappa is inconsistent (0.50 vs 0.85).

Audit: docs/audits/2026-06-15-bqclt-isospin-split-coulomb-not-categorical.md

EXPLORATORY presentation/analysis — no production rewire; the only free input is
the length r0 (flagged). The symbolic proof and the Coulomb validation run with
sympy + the vendored AME2020 table alone; the categorical comparison recomputes
the bond-type ratios live via the canonical trace tr_m_atom_zn (no hardcoded
constants), and is skipped with a note when the substrate package is absent.
"""
from __future__ import annotations

import json
import math
import sys
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

# The categorical comparison needs the canonical Markov trace, which transitively
# pulls in the substrate package. Attempt the import once here (EAFP); when it is
# absent — e.g. the post-#2310 content-repo sandbox — the categorical section is
# skipped with a note (its numbers are recorded in the audit doc). noqa: E402 —
# these bare-name imports require the sys.path inserts above.
try:
    from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
    from q_parameter import Q as _Q0  # noqa: E402
    from codata_constants import M_E_MEV as _ME_MEV  # noqa: E402
    _HAS_SUBSTRATE = True
except ImportError:
    _HAS_SUBSTRATE = False

AHC = 1.43996  # alpha_EM * hbar*c  [MeV.fm]  (= e^2/4 pi eps0)

# mirror pairs as ((Z,N) of the n-rich member, (Z,N) of the p-rich member, A, name)
PAIRS = [((1, 2), (2, 1), 3, "3H/3He"), ((3, 4), (4, 3), 7, "7Li/7Be")]


def symbolic_proof():
    """Prove the (Z-N)(A-1) factorization and the A^-2/3 over-split scaling."""
    import sympy as sp
    Z, N, Lpp, Lnn, E0, Kc = sp.symbols("Z N L_pp L_nn E_0 K_C", positive=True)
    A = Z + N
    coul_num = sp.factor(Z * (Z - 1) - N * (N - 1))
    cat_split = sp.simplify(
        E0 * (A - 1) / sp.binomial(A, 2)
        * (sp.binomial(N, 2) - sp.binomial(Z, 2)) * (Lnn - Lpp))
    coul_split = Kc * (Z * (Z - 1) - N * (N - 1)) / A ** sp.Rational(1, 3)
    over = sp.simplify(cat_split / coul_split)
    print("[symbolic] common isospin factor:  Z(Z-1) - N(N-1) =", coul_num)
    print("[symbolic] categorical (B_qCLT_fac) split =", cat_split, "   [~ A^-1]")
    print("[symbolic] Coulomb split                  =", sp.simplify(coul_split),
          "   [~ A^-1/3]")
    print("[symbolic] over-split = categorical/Coulomb =", over,
          "   [~ A^-2/3  =>  no constant kappa]")
    return over


def _ame():
    d = json.loads((HERE / "data" / "ame2020.json").read_text())
    rows = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = rows.values() if isinstance(rows, dict) else rows
    return {(r["Z"], r["A"]): r["binding_energy_total_keV"] / 1000.0
            for r in rows if r.get("binding_energy_total_keV") is not None}


def coulomb_validation(ame):
    """One Coulomb length r0 per mirror pair (right A^-1/3 scaling)."""
    print("\n[Coulomb] split = (3/5)(alpha_EM hbar c / r0) [Z(Z-1)-N(N-1)] / A^(1/3):")
    out = {}
    for (lo, hi, A, name) in PAIRS:
        split = ame[(lo[0], A)] - ame[(hi[0], A)]            # B(n-rich) - B(p-rich)
        num = hi[0] * (hi[0] - 1) - lo[0] * (lo[0] - 1)      # = (Z-N)(A-1)
        r0 = 0.6 * AHC * num / (split * A ** (1 / 3))
        out[name] = (split, r0)
        print(f"  {name:9s} A={A}  AME split={split:.3f} MeV  ->  r0={r0:.3f} fm")
    r0s = [v[1] for v in out.values()]
    print(f"  => one r0 ~ {sum(r0s) / len(r0s):.2f} fm fits both "
          f"(spread {abs(r0s[0] - r0s[1]) / (sum(r0s) / len(r0s)) * 100:.1f}%)")
    return out


def _cat_split(Z, N, L, E0):
    A = Z + N
    sig = comb(Z, 2) * L["pp"] + Z * N * L["pn"] + comb(N, 2) * L["nn"]
    return E0 * (A - 1) * sig / comb(A, 2)


def categorical_comparison(ame):
    """The categorical kappa is A-dependent (inconsistent) — recompute live."""
    me, q0 = float(_ME_MEV), float(_Q0)
    E0 = me / (q0 * (q0 - 1.0))
    L = {}
    for key, (Z, N) in (("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))):
        ta, tf, _, _ = tr_m_atom_zn(Z, N, dps=50)
        L[key] = math.log(float(tf) / float(ta))
    print(f"\n[categorical] E0={E0:.4f} MeV; bond L: pp={L['pp']:.4f} "
          f"pn={L['pn']:.4f} nn={L['nn']:.4f}  (live tr_m_atom_zn at q0, 50 dps)")
    for (lo, hi, A, name) in PAIRS:
        fac = _cat_split(*lo, L, E0) - _cat_split(*hi, L, E0)
        split = ame[(lo[0], A)] - ame[(hi[0], A)]
        print(f"  {name:9s} A={A}  B_qCLT_fac split={fac:.3f}  kappa={split / fac:.3f}"
              f"  (over-split {fac / split:.2f}x)")


def main() -> int:
    symbolic_proof()
    ame = _ame()
    coulomb_validation(ame)
    if _HAS_SUBSTRATE:
        categorical_comparison(ame)
    else:
        print("\n[categorical] skipped: substrate trace package not available in "
              "this env; values are recorded in the audit doc Findings 1/3 "
              "(A=3 kappa=0.504, A=7 kappa=0.845 — inconsistent, as proven).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
