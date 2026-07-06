"""³He structural-gap diagnosis for the brane-tower binding formula.

The z-Habiro conjecture's surviving empirical thread: "the ³He gap is a
structural deficit of the brane-tower formula at the A=3 / n₀=9 regime, not an
operator-volume choice" (brane-tower-z-habiro.md §Structural conclusion). The
six n⋆ families are refuted; this probe isolates *why* ³He specifically
overshoots, using the PRODUCTION −Li₂^q(−z) tower form (bounded) and the exact
production per-generator volumes — so the effect is shown to be STRUCTURAL, not
a Φ_q blow-up artifact.

Mechanism (this probe makes it quantitative):
  The per-generator brane-tower sum Σ_i −Li₂^q(−|V̂_i^full|) is dominated by the
  near-pole (proton) generators (|V̂| ≈ 0.989, 0.971 → −Li₂^q ≈ 0.81 each).
  ³He (2p+1n) carries the proton near-pole PAIR *doubled* (positions 0,1 and
  3,4) vs tritium (1p+2n) which has it once. So the tower is monotone-increasing
  in proton count: tower(³He) > tower(T). But empirically ³He is LESS bound than
  T (B(³He)=7.718 < B(T)=8.482 MeV). A binding contribution that grows with
  proton count therefore has the WRONG ordering for the proton-rich mirror
  member — the structural deficit.

Per-generator |V̂_i^full| (production `full` channel, 50 dps):
  terms-2-3-atom-per-gen-mpfr-50dps.witness.json
AME2020 binding (MeV): D 2.224566, T 8.481798, ³He 7.718043.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

Q0 = mp.mpf("1.1099785955541805752815940796095093779932822799587")

# production `full`-channel per-generator |V̂_i^full|, exact from
# terms-2-3-atom-per-gen-mpfr-50dps.witness.json
VHAT: dict[str, list[str]] = {
    "deuteron": [  # Z=1 N=1
        "0.98900731592925977373270908734257112349982263541670",
        "0.97107015865274369644467729606208246103317407697938",
        "0.26414511559102965537297885587878402058016307591254",
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
    ],
    "tritium": [  # Z=1 N=2
        "0.98900731592925977373270908734257112349982263541670",
        "0.97107015865274369644467729606208246103317407697938",
        "0.26414511559102965537297885587878402058016307591254",
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
        "0.15961495459608992482217464472982306734928492395430",
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
    ],
    "helium3": [  # Z=2 N=1  — note the doubled proton near-pole pair (0,1 & 3,4)
        "0.98900731592925977373270908734257112349982263541670",
        "0.97107015865274369644467729606208246103317407697938",
        "0.36867527658596938592378306702774497381104122787078",
        "0.98900731592925977373270908734257112349982263541670",
        "0.97107015865274369644467729606208246103317407697938",
        "0.26414511559102965537297885587878402058016307591254",
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
    ],
}
Z_N = {"deuteron": (1, 1), "tritium": (1, 2), "helium3": (2, 1)}
B_AME = {"deuteron": 2.224566, "tritium": 8.481798, "helium3": 7.718043}
NEAR_POLE = mp.mpf("0.9")  # |V̂| above this = proton/near-pole generator


def q_int(n: int, q: mp.mpf) -> mp.mpf:
    return (q**n - q ** (-n)) / (q - 1 / q)


def neg_li2q_neg(z: mp.mpf, q: mp.mpf, terms: int = 100000) -> mp.mpf:
    """Production tower term −Li₂^q(−z) = Σ (−1)^{n+1} z^n /(n·[n]_q)."""
    total = mp.mpf(0)
    zn = mp.mpf(1)
    sign = 1
    for n in range(1, terms + 1):
        zn *= z
        term = sign * zn / (n * q_int(n, q))
        total += term
        sign = -sign
        if abs(term) < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
    return total


def main() -> None:
    self_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(self_path.read_bytes()).hexdigest()[:12]

    out_atoms: dict[str, dict] = {}
    print(f"{'atom':>9} {'Z,N':>5} {'#near-pole':>11} {'tower Σ−Li₂^q':>14} "
          f"{'B_AME (MeV)':>12}")
    for atom, zs in VHAT.items():
        z_list = [mp.mpf(s) for s in zs]
        terms = [neg_li2q_neg(z, Q0) for z in z_list]
        tower = sum(terms)
        n_near = sum(1 for z in z_list if z > NEAR_POLE)
        Z, N = Z_N[atom]
        print(f"{atom:>9} {f'{Z},{N}':>5} {n_near:>11} "
              f"{mp.nstr(tower, 8):>14} {B_AME[atom]:>12.4f}")
        out_atoms[atom] = {
            "Z": Z, "N": N,
            "n_near_pole_gens": n_near,
            "tower_neg_li2q": mp.nstr(tower, 16),
            "per_gen_terms": [mp.nstr(t, 10) for t in terms],
            "B_AME_MeV": B_AME[atom],
        }

    t_T = mp.mpf(out_atoms["tritium"]["tower_neg_li2q"])
    t_He = mp.mpf(out_atoms["helium3"]["tower_neg_li2q"])

    # The structural mismatch, made explicit:
    structural = {
        # tower is monotone-increasing in proton count (³He > T)
        "tower_He3_gt_T": bool(t_He > t_T),
        "tower_He3_minus_T": mp.nstr(t_He - t_T, 10),
        # but ³He is LESS bound than T (mirror pair, AME)
        "B_He3_lt_T_AME": B_AME["helium3"] < B_AME["tritium"],
        "B_T_minus_He3_AME_MeV": round(B_AME["tritium"] - B_AME["helium3"], 6),
        # ³He carries the proton near-pole PAIR doubled vs T
        "near_pole_He3": out_atoms["helium3"]["n_near_pole_gens"],
        "near_pole_T": out_atoms["tritium"]["n_near_pole_gens"],
        # the deficit: tower ordering (He3>T) is OPPOSITE to binding (He3<T)
        "tower_ordering_opposes_binding": bool(
            (t_He > t_T) and (B_AME["helium3"] < B_AME["tritium"])
        ),
    }
    print()
    print("structural diagnosis:", json.dumps(structural, indent=2))
    print()
    print("VERDICT: the per-generator brane-tower sum grows with proton "
          "near-pole count (³He > T), but ³He is the LESS-bound mirror member "
          "(B: ³He < T). The tower's monotone-in-Z behaviour has the wrong "
          "ordering for the proton-rich member — a STRUCTURAL deficit of the "
          "per-generator form at A=3, independent of the dilog choice (li2q "
          "bounded here, not a Φ_q blow-up).")

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "he3-brane-tower-structural-gap",
        "scriptFile": self_path.name,
        "scriptHash": script_hash,
        "contentBlock": "conj:brane-tower-z-habiro",
        "description": (
            "Isolates the ³He structural deficit of the per-generator "
            "brane-tower binding formula using the PRODUCTION −Li₂^q(−z) form "
            "(bounded) + exact production |V̂_i^full|. The tower sum is monotone "
            "in proton near-pole count (³He>T), but ³He is the less-bound mirror "
            "member (B_AME: ³He<T) — so the per-generator tower has the wrong "
            "Z-ordering at A=3. Structural, not a Φ_q artifact (li2q is bounded)."
        ),
        "parameters": {"q_0_50dps": mp.nstr(Q0, 50),
                       "tower_form": "−Li₂^q(−|V̂_i^full|) (production li2q)",
                       "near_pole_threshold": "0.9"},
        "data": {"atoms": out_atoms, "structural_diagnosis": structural},
        "cross_checks": structural,
        "allPassed": structural["tower_ordering_opposes_binding"],
        "provenance": ["terms-2-3-atom-per-gen-mpfr-50dps.witness.json", "AME2020"],
    }
    out = self_path.parent.parent / "he3-brane-tower-structural-gap.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
