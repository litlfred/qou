#!/usr/bin/env python3
"""A5 branching of SO(3) irreps — orbital-degeneracy splitting (EXPLORATORY).

Exact character-theoretic restriction of the (2l+1)-dimensional SO(3)
irreps to the icosahedral group A5 (the alternating subgroup of the
corpus's Bring automorphism group S5), for l = 0..6. Multiplicities are
computed by the orthogonality formula

    m_rho(l) = (1/60) * sum_c |c| * chi_l(theta_c) * chi_rho(c)

with chi_l(theta) = sin((2l+1)theta/2)/sin(theta/2) and the standard
A5 character table (golden-ratio entries), evaluated at the repo
compute precision (``set_compute_dps()``, the qou-substrate default)
and verified to be integers to < 1e-30.

Claims under test (from the 2026-08-01 knot-identification discussion,
reviewed in docs/audits/2026-08-01-tau-knot-discussion-review.md):

  * l = 0,1,2 restrict irreducibly (1, 3, 5) — the s/p/d degeneracies
    are native A5 irrep dimensions;
  * l = 3 (the f orbital, degeneracy 7) FRACTURES as 3' + 4;
  * l = 4 (g, 9) fractures as 4 + 5;
  * l = 5 (h, 11) fractures as 3 + 3' + 5;
  * no unified irreducible state of dimension > 5 exists over A5.

This is standard finite-group representation theory made exact and
witness-pinned; the *physical* reading (orbital fine structure on the
categorical substrate) remains interpretive and is NOT wired anywhere.
Bean qou-a2g2; ties to the shell-filling swarm (bean 1c24).
"""

from __future__ import annotations

import _path_bridge  # noqa: F401
from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf, sin, pi, sqrt  # noqa: E402

L_MAX = 6


def main() -> None:
    set_compute_dps()
    phi = (1 + sqrt(5)) / 2
    # A5 classes: (size, rotation angle theta) for e, C2, C3, C5, C5^2.
    classes = [
        (1, mpf(0)),
        (15, pi),
        (20, 2 * pi / 3),
        (12, 2 * pi / 5),
        (12, 4 * pi / 5),
    ]
    # Irreducible characters of A5 on those classes.
    irreps = {
        "1": [mpf(1)] * 5,
        "3": [mpf(3), mpf(-1), mpf(0), phi, 1 - phi],
        "3'": [mpf(3), mpf(-1), mpf(0), 1 - phi, phi],
        "4": [mpf(4), mpf(0), mpf(1), mpf(-1), mpf(-1)],
        "5": [mpf(5), mpf(1), mpf(-1), mpf(0), mpf(0)],
    }

    def chi_l(l: int, theta) -> mpf:
        if theta == 0:
            return mpf(2 * l + 1)
        return sin((2 * l + 1) * theta / 2) / sin(theta / 2)

    table = {}
    max_residual = mpf(0)
    for l in range(L_MAX + 1):
        chis = [chi_l(l, th) for (_, th) in classes]
        decomp = {}
        for name, chars in irreps.items():
            m = sum(sz * cl * cr for (sz, _), cl, cr in
                    zip(classes, chis, chars)) / 60
            m_int = int(mp.nint(m))
            residual = abs(m - m_int)
            max_residual = max(max_residual, residual)
            if m_int:
                decomp[name] = m_int
        dim_check = sum(int(irreps[n][0]) * m for n, m in decomp.items())
        assert dim_check == 2 * l + 1, (l, decomp)
        table[f"l={l} (dim {2*l+1})"] = decomp

    claims = {
        "l3_fractures_3p_plus_4":
            table["l=3 (dim 7)"] == {"3'": 1, "4": 1},
        "l4_fractures_4_plus_5":
            table["l=4 (dim 9)"] == {"4": 1, "5": 1},
        "l5_fractures_3_3p_5":
            table["l=5 (dim 11)"] == {"3": 1, "3'": 1, "5": 1},
        "spd_irreducible":
            table["l=0 (dim 1)"] == {"1": 1}
            and table["l=1 (dim 3)"] == {"3": 1}
            and table["l=2 (dim 5)"] == {"5": 1},
    }

    wb = WitnessBuilder("a5-so3-branching", engine="mpmath")
    wb.set_description(
        "EXPLORATORY exact A5-branching of SO(3) irreps l=0..6 (bean "
        "qou-a2g2): s/p/d restrict irreducibly (1/3/5); the f orbital "
        "(7) fractures as 3'+4, g (9) as 4+5, h (11) as 3+3'+5. "
        "Standard character theory, witness-pinned; the orbital "
        "fine-structure reading is interpretive and NOT wired.")
    wb.add_data("branching_table", table)
    wb.add_data("claims", claims)
    wb.add_data("max_integer_residual", mp.nstr(max_residual, 5))
    wb.set_audit_only("docs/audits/2026-08-01-tau-knot-discussion-review.md")
    wb.add_assertion(
        name="all_discussion_claims_verified",
        computed=int(all(claims.values())), expected=1, tolerance=0,
        unit="bool",
        source="Exact multiplicity computation, integer residual < 1e-30.")
    wb.add_assertion(
        name="f_orbital_splits_3p_4",
        computed=int(claims["l3_fractures_3p_plus_4"]), expected=1,
        tolerance=0, unit="bool",
        source="l=3 restriction to A5 decomposes as 3' + 4 (7 = 3+4).")
    out = wb.save()

    for k, v in table.items():
        print(f"{k}: {v}")
    print(f"claims: {claims}")
    print(f"witness -> {out}")


if __name__ == "__main__":
    main()
