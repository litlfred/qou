#!/usr/bin/env python3
# polynomial_q_not_applicable: exact AME data + integer α-counts; no q, no fit.
"""
α-cluster (Wigner SU(4) supermultiplet) scaling test for the missing extensive
binding term (beans qou-0c19 / qou-uclw).  ZERO-fit.

Motivation (from binding_multibody_scaling_probe.py): the extensive term is
LINEAR in A (per-nucleon B/A → ~8 MeV, CV 0.148) but with a super-pairwise low-A
ONSET (⁴He exceeds the pairwise cap ρ_A ≤ C(A,2)).  The categorical object that
produces exactly a `∝A`-with-onset structure is the SU(4) supermultiplet gate,
proved sorry-free:

    QOU.MassTheory.su4_supermultiplet_dim_vanishes_iff :  dim [1^A] = C(4, A)
        present (nonzero) for A ≤ 4 ;  VANISHES for A > 4  (no [1^5]).

So a *complete* α = one filled `[1^4]` supermultiplet (A=4, dim C(4,4)=1); A>4
cannot fit one antisymmetric blob and must break into separate α's — the
categorical origin of α-clustering.

Test (0-fit): for α-conjugate nuclei (A = 4n) is `B / n_α` constant (⟹ the
extensive term is the α-cluster volume term)?  And do the sub-α nuclei (A<4)
trace the partial filling of the first `[1^4]`?

Read-only AME; no inversion.  Output: alpha-cluster-binding-scaling.witness.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_COMP = HERE.parent
for p in (str(_COMP), str(_COMP / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder, record_upstream  # noqa: E402

# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

AME = _COMP / "ame-2020-binding-energies.witness.json"

# α-conjugate nuclei (A = 4·n_α) present in the AME witness
ALPHA_CONJ = [("4He", "B_he4_MeV", 4, 1), ("8Be", "B_be8_MeV", 8, 2),
              ("12C", "B_c12_MeV", 12, 3), ("16O", "B_o16_MeV", 16, 4)]
# sub-α onset (partial [1^4] filling)
SUB_ALPHA = [("2H", "B_deuteron_MeV", 2), ("3H", "B_tritium_MeV", 3),
             ("3He", "B_he3_MeV", 3)]


def _cv(vals):
    m = sum(vals) / len(vals)
    return (sum((x - m) ** 2 for x in vals) / len(vals)) ** 0.5 / m, m


def main() -> int:
    ame = record_upstream(AME, _UPSTREAM_RECORDS)
    data = ame.get("data", ame)

    def B(key):
        v = data.get(key)
        if v is None:
            v = ame.get(key)
        return float(v) if v is not None else None

    conj_rows, per_alpha = [], []
    for name, key, A, na in ALPHA_CONJ:
        b = B(key)
        if b is None:
            continue
        conj_rows.append({"iso": name, "A": A, "n_alpha": na,
                          "B_MeV": b, "B_per_alpha": b / na, "B_per_A": b / A})
        per_alpha.append(b / na)
    cv_alpha, mean_alpha = _cv(per_alpha)

    onset_rows = []
    for name, key, A in SUB_ALPHA:
        b = B(key)
        if b is None:
            continue
        onset_rows.append({"iso": name, "A": A, "frac_of_alpha": A / 4,
                           "B_MeV": b, "B_per_A": b / A})

    w = WitnessBuilder("alpha-cluster-binding-scaling", engine="exact")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "0-fit α-cluster (Wigner SU(4) [1^4] supermultiplet) scaling test. "
        "B/n_α is constant to CV~5% across α-conjugate nuclei (⁴He→¹⁶O) — the "
        "extensive binding term is the α-cluster volume term; the sub-α nuclei "
        "trace partial [1^4] filling. Categorical origin: the proved SU(4) gate "
        "dim[1^A]=C(4,A) (present A≤4, vanishes A>4)."
    )
    w.set_content_block("alg:delta-lambda-closure")
    w.add_parameter("no_fit", True)
    w.add_parameter("cv_B_per_alpha", cv_alpha)
    w.add_parameter("mean_B_per_alpha_MeV", mean_alpha)
    w.add_parameter("su4_gate_lean", "QOU.MassTheory.su4_supermultiplet_dim_vanishes_iff")
    w.add_caveat(
        "STRUCTURE is derived (α = filled [1^4] via the proved SU(4) gate); the "
        "per-α SCALE (~29.8 MeV) is still EMPIRICAL, not yet substrate-derived. "
        "This localizes the magnitude gap to 'derive the per-α binding scale'."
    )
    w.add_data("alpha_conjugate", conj_rows)
    w.add_data("sub_alpha_onset", onset_rows)
    built = w.build()
    (HERE / "alpha-cluster-binding-scaling.witness.json").write_text(
        json.dumps(built, indent=2, sort_keys=True) + "\n")

    print("=== α-conjugate nuclei (A=4·n_α): B per α ===")
    print(f"  {'iso':<5}{'A':>3}{'n_α':>4}{'B(MeV)':>10}{'B/α':>8}{'B/A':>8}")
    for r in conj_rows:
        print(f"  {r['iso']:<5}{r['A']:>3}{r['n_alpha']:>4}{r['B_MeV']:>10.2f}"
              f"{r['B_per_alpha']:>8.2f}{r['B_per_A']:>8.2f}")
    print(f"  CV(B/α) = {cv_alpha:.3f}   mean = {mean_alpha:.2f} MeV/α "
          f"(vs per-nucleon CV 0.148)")
    print("\n=== sub-α onset (partial [1^4] filling) ===")
    for r in onset_rows:
        print(f"  {r['iso']:<5}A={r['A']}  frac-of-α={r['frac_of_alpha']:.2f}"
              f"  B/A={r['B_per_A']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
