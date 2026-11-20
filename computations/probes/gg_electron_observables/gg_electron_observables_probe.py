#!/usr/bin/env python3
"""gg_electron_observables_probe.py — invariants separating the γγ electron candidates V^0, V^3, V^6.

Bean qou-a1hh. Pre-registered in preregistration.md (commit 43188f82802) before this file.
V = σ0 σ1^{-1}. Nothing is fitted, selected, or compared with measurement.
mpmath 40 dps (level characters, spectrum); SnapPy for link type / volume / chirality
(SnapPy high-precision volume, carried as a string).

-- Ref: [leitner2026] bean qou-a1hh; probe h2_gg_electron
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "h2_gg_atom"))
import h2_gg_atom_probe as ga  # noqa: E402

base, kct = ga.base, ga.kct
from qou_substrate.witness import WitnessBuilder  # noqa: E402

Q = base.Q
H = Q - 1 / Q


def rep21(word):
    I = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(1)]]
    return mp.matrix(kct.right_apply(I, word, [2, 1]))


def snappy_block(k):
    import snappy
    if k == 0:
        return {"components": 3, "linking_matrix": [[0] * 3] * 3, "identify": "3-component unlink",
                "hyperbolic": False, "volume": "0 (not hyperbolic)", "amphichiral": True}
    L = snappy.Link(braid_closure=[1, -2] * k)
    M = L.exterior()
    iso = M.is_isometric_to(L.mirror().exterior(), return_isometries=True)
    return {
        "components": len(L.link_components),
        "linking_matrix": [list(map(int, r)) for r in L.linking_matrix()],
        "identify": [str(x) for x in M.identify()],
        "hyperbolic": True,
        "volume": str(M.high_precision().volume()),
        "amphichiral": any(i.extends_to_link() for i in iso),
    }


def main() -> int:
    checks, out = [], {}

    def check(name, ok, src):
        checks.append((name, bool(ok), src))
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {src}", flush=True)

    # closed form: on (2,1), V has det 1 and trace -1-h^2, so eigenvalues e^{±iθ}, 2cosθ = -1-h^2
    theta = mp.acos((-1 - H ** 2) / 2)
    V1 = rep21(base.V(0))
    check("C1_trace_V_21_closed_form", abs(V1[0, 0] + V1[1, 1] - (-1 - H ** 2)) < mp.mpf("1e-35"),
          f"tr={mp.nstr(V1[0,0]+V1[1,1], 20)}")
    check("C2_det_V_21_is_1", abs(mp.det(V1) - 1) < mp.mpf("1e-35"), "")
    out["theta_over_2pi_div_3"] = mp.nstr(theta / (2 * mp.pi / 3), 30)

    for k in (0, 3, 6):
        w = base.V(0) * k
        lc = ga.level_chars(base.diag_of(w, 3), 3, 1)
        Mk = rep21(w)
        ev = mp.eig(Mk)[0] if k else [mp.mpf(1), mp.mpf(1)]
        chi21 = Mk[0, 0] + Mk[1, 1]
        row = {
            "level_chars": {f"{m}:{mu}": mp.nstr(v, 25) for (m, mu), v in lc.items()},
            "min_level_char": mp.nstr(min(lc.values()), 25),
            "chi21": mp.nstr(chi21, 30),
            "chi21_closed_form_2cos_k_theta": mp.nstr(2 * mp.cos(k * theta), 30),
            "eig21": [mp.nstr(e, 25) for e in ev],
            "dist_from_identity_21": mp.nstr(mp.mnorm(Mk - mp.eye(2), 1), 25),
            "equals_nucleon_word": {"V^3": k == 3, "V^6": k == 6},
        }
        row.update(snappy_block(k))
        out[f"V^{k}"] = row
        check(f"C3_chi21_closed_form_k{k}", abs(chi21 - 2 * mp.cos(k * theta)) < mp.mpf("1e-30"), row["chi21"])
        print(k, row, flush=True)

    ok = all(c[1] for c in checks)
    wb = WitnessBuilder("gg-electron-observables", engine="mpmath", output_dir=HERE)
    for name, good, src in checks:
        wb.add_assertion(name, computed="1" if good else "0", expected="1", source=src)
    wb.save({
        "q0Anchor": "proton",
        "q0AnchorReason": "via h2_one_rule (cf.Q, proton pin)",
        "description": "PROBE (bean qou-a1hh): invariants of the gamma-gamma electron candidates V^0, V^3, V^6 "
                       "(V = s0 s1^-1). Pre-registered. Nothing fitted, selected or compared with measurement.",
        "results": out,
    })
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
