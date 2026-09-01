"""Pin the PHYSICAL brane-tower variable z and decide the z-Habiro / Φ_q
production-wiring question.

Context
-------
PR #2447 merged the algebraic z-Habiro Cauchy-limit infrastructure
(`QOU.MassEndomorphism.ZHabiroCauchy`: `eulerCoeff`, the localised Euler
family, the cyclotomic completion ring). PR #2460 built a numerical bridge
confirming `eulerCoeff` / `eulerTrunc = Σ cₘ Pₘ` at q₀, and flagged that the
N=0 → Φ_q correction is 9.36 % at the *representative* scale ``z = ℏ_q²`` —
"so the physical brane-tower variable z (|V̂_i|) differs from this scale."
Roadmap step 1 was: pin the actual physical z and decide the production wire.

This probe answers that, using ONLY values already computed in production
witnesses (no Hecke recompute):

  physical z_i = |V̂_i^full| = the additive Wedderburn traced volume per
  generator (`def:algebraic-quantum-volume`), the argument of the dilog in
  `prop:mass-endomorphism-tower`.

Sources (exact, 50 dps):
  - q₀                         terms-2-3-atom-per-gen-mpfr-50dps.witness.json
  - |V̂_i^full| per generator   same (full channel) + mass-endomorphism.witness.json (electron)

Two evaluators are compared at each physical z_i:
  - Φ_q(z)   = ∏_{k≥1} (1 − q^{−k} z)^{−1}          (compact-q-dilog — SUPERSEDED
               `brane-legacy` tower mode; the −737 MeV isospin pathology)
  - −Li₂^q(−z) = Σ_{n≥1} (−1)^{n+1} z^n /(n·[n]_q)   (symmetric — the
               PRODUCTION `li2q` tower mode in prop:mass-endomorphism-tower)
  with [n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹).

Verdict
-------
At every physical z_i (all < 1, max 0.98901) Φ_q is convergent-but-enormous
(10²–10⁶), while −Li₂^q(−z) is O(1). Wiring the per-generator Φ_q form into
the mass table therefore REGRESSES it (the documented isospin pathology); the
production `li2q` form is bounded there. The z-Habiro / Φ_q bridge has no
non-regressing production continuation: the only thing that could rescue a
truncated-Φ_q production form is the n⋆ level-selection rule, which is refuted
across all six probed families (docs/audits/2026-06-17-refuted-ansatz-lemmas.md).
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_MP  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from _witness_q0_stamp import stamp_q0  # noqa: E402 — bean 1j39, bucket C

set_compute_dps()

# --- exact constants from production witnesses (50 dps) ----------------------
# q0 comes from the pin table, never a literal. This held
# `1.1099785955541805`, the SUPERSEDED muon value -- it matches
# neither current pin, so nothing could compare it against
# anything. Owner ruling 2026-08-24, bean `qou/ftuv`.
Q0 = Q_MP
HBAR_Q = 1 - 1 / Q0  # quantum Planck constant ℏ_q = 1 − q₀⁻¹

# physical z_i = |V̂_i^full| (additive Wedderburn traced volume, FULL channel).
# proton/neutron/D/T/³He: terms-2-3-atom-per-gen-mpfr-50dps.witness.json
# electron: mass-endomorphism.witness.json (vols[0].full)
VHAT_FULL: dict[str, list[str]] = {
    "electron": ["0.5938490006705097"],
    "proton": [
        "0.98900731592925977373270908734257112349982263541670",
        "0.97107015865274369644467729606208246103317407697938",
    ],
    "neutron": [
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
    ],
    "deuteron": [
        "0.98900731592925977373270908734257112349982263541670",
        "0.97107015865274369644467729606208246103317407697938",
        "0.26414511559102965537297885587878402058016307591254",
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
    ],
    "tritium": [
        "0.98900731592925977373270908734257112349982263541670",
        "0.97107015865274369644467729606208246103317407697938",
        "0.26414511559102965537297885587878402058016307591254",
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
        "0.15961495459608992482217464472982306734928492395430",
        "0.85421031282583896067694429979116691556883293829130",
        "0.97550947110774594315687948247161058517697160610811",
    ],
    "helium3": [
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


def phi_q(z: mp.mpf, q: mp.mpf, terms: int = 100000) -> mp.mpf:
    """compact quantum dilogarithm phi_q(z) = ∏_{k≥1}(1 − q^{−k} z)^{−1}, q>1."""
    qinv = 1 / q
    prod = mp.mpf(1)
    qk = qinv
    for _ in range(terms):
        prod /= (1 - qk * z)
        qk *= qinv
        if qk * z < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
    return prod


def q_int(n: int, q: mp.mpf) -> mp.mpf:
    """Symmetric q-integer [n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)."""
    return (q**n - q ** (-n)) / (q - 1 / q)


def neg_li2q_neg(z: mp.mpf, q: mp.mpf, terms: int = 100000) -> mp.mpf:
    """Production tower term −Li₂^q(−z) = Σ_{n≥1} (−1)^{n+1} z^n /(n·[n]_q)."""
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

    print(f"q₀     = {mp.nstr(Q0, 20)}")
    print(f"ℏ_q    = {mp.nstr(HBAR_Q, 12)}   ℏ_q² = {mp.nstr(HBAR_Q**2, 12)}")
    print()

    # --- continuity anchor: PR #2460's 9.36 % at the representative scale ----
    z_rep = HBAR_Q**2
    corr_rep = (phi_q(z_rep, Q0) - 1) * 100
    print(f"[anchor] Φ_q(ℏ_q²) − 1 = {mp.nstr(corr_rep, 6)} %   "
          f"(PR #2460 reported 9.36 %)")
    # --- validation anchor: production witness electron single = 629.9354 ----
    phi_e = phi_q(mp.mpf(VHAT_FULL["electron"][0]), Q0)
    print(f"[anchor] Φ_q(|V̂_e|=0.59385) = {mp.nstr(phi_e, 8)}   "
          f"(mass-endomorphism.witness electron single = 629.9354)")
    print()

    atoms_out: dict[str, dict] = {}
    print(f"{'atom':>9} {'max|V̂_i|':>10} {'max Φ_q(z_i)':>16} "
          f"{'max −Li₂^q(−z_i)':>18} {'Φ_q/Li₂^q ratio':>18}")
    for atom, zs in VHAT_FULL.items():
        z_list = [mp.mpf(s) for s in zs]
        phis = [phi_q(z, Q0) for z in z_list]
        li2s = [neg_li2q_neg(z, Q0) for z in z_list]
        max_z = max(z_list)
        max_phi = max(phis)
        max_li2 = max(li2s, key=abs)
        ratio = max_phi / abs(max_li2)
        print(f"{atom:>9} {mp.nstr(max_z, 6):>10} {mp.nstr(max_phi, 6):>16} "
              f"{mp.nstr(max_li2, 6):>18} {mp.nstr(ratio, 6):>18}")
        atoms_out[atom] = {
            "z_i_physical": [mp.nstr(z, 30) for z in z_list],
            "phi_q_per_gen": [mp.nstr(p, 12) for p in phis],
            "neg_li2q_neg_per_gen": [mp.nstr(li, 12) for li in li2s],
            "max_z": mp.nstr(max_z, 30),
            "max_phi_q": mp.nstr(max_phi, 12),
            "max_neg_li2q": mp.nstr(max_li2, 12),
            "phi_over_li2_ratio": mp.nstr(ratio, 12),
            "all_z_below_one": all(z < 1 for z in z_list),
        }

    # cross-checks (P34): the probe's evaluators reproduce production anchors.
    cross = {
        "phi_q_hbar_sq_matches_pr2460_9_36pct": bool(
            abs(corr_rep - mp.mpf("9.36")) < mp.mpf("0.05")
        ),
        "phi_q_electron_matches_witness_629_9354": bool(
            abs(phi_e - mp.mpf("629.9354190959173")) < mp.mpf("1e-3")
        ),
        "all_physical_z_below_one": all(
            mp.mpf(s) < 1 for zs in VHAT_FULL.values() for s in zs
        ),
        "phi_q_blows_up_li2q_bounded": all(
            a["all_z_below_one"] and mp.mpf(a["max_phi_q"]) > 100
            and abs(mp.mpf(a["max_neg_li2q"])) < 5
            for a in atoms_out.values()
        ),
    }
    print()
    print("cross_checks:", json.dumps(cross, indent=2))

    # Assertions (bean qou-srvu). This witness had NO `assertions` key while
    # setting `allPassed`, so every consumer that reads `assertions` saw an
    # empty claim beside a green verdict. The three checks below were already
    # computed in `cross` above and already fed `allPassed`; they were simply
    # never surfaced per-check with their numbers. Nothing new is claimed.
    #
    # THRESHOLD PROVENANCE: 0.05 and 1e-3 are this file's OWN declared bars,
    # written into `cross` above and predating this change. Carrying the
    # computed value beside them lets a reader see the headroom instead of
    # taking a boolean on trust.
    #
    # `all_physical_z_below_one` is asserted as a COUNT, not a boolean: the bar
    # `z < 1` is the claim's own logic (a Markov parameter at or above 1 is
    # outside the physical regime this probe pins), and `expected` is the size
    # of VHAT_FULL, not a number chosen to match the result.
    #
    # NOT asserted: `phi_q_blows_up_li2q_bounded`. Its bars -- `max_phi_q > 100`
    # and `|max_neg_li2q| < 5` -- are order-of-magnitude thresholds with no
    # provenance in this file or its cone; "blows up" and "bounded" are
    # qualitative readings, and choosing 100 and 5 to make them true would be a
    # fit. It stays in `cross_checks` as recorded data.
    _all_z = [mp.mpf(s) for zs in VHAT_FULL.values() for s in zs]
    assertions = [
        {
            "name": "phi_q_hbar_sq_correction_pct_matches_pr2460",
            "computed": mp.nstr(corr_rep, 15),
            "expected": "9.36",
            "tolerance": "0.05",
            "passed": cross["phi_q_hbar_sq_matches_pr2460_9_36pct"],
            "source": "PR #2460 production anchor; bar is this file's own 0.05",
        },
        {
            "name": "phi_q_electron_matches_upstream_witness",
            "computed": mp.nstr(phi_e, 20),
            "expected": "629.9354190959173",
            "tolerance": "1e-3",
            "passed": cross["phi_q_electron_matches_witness_629_9354"],
            "source": "value recorded upstream; bar is this file's own 1e-3",
        },
        {
            "name": "physical_z_below_one_count",
            "computed": str(sum(1 for z in _all_z if z < 1)),
            "expected": str(len(_all_z)),
            "passed": cross["all_physical_z_below_one"],
            "source": "every Markov parameter in VHAT_FULL must satisfy z < 1 "
                      "to sit in the physical regime; expected is the size of "
                      "VHAT_FULL, not a number matched to the result",
        },
    ]

    witness = {
        "engine": "mpmath",
        "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "zhabiro-physical-z-pin",
        "scriptFile": self_path.name,
        "scriptHash": script_hash,
        "contentBlock": "prop:mass-endomorphism-tower",
        "description": (
            "Pins the physical brane-tower variable z = |V̂_i^full| (additive "
            "Wedderburn traced volume per generator) from production witnesses "
            "and compares the SUPERSEDED compact q-dilog Φ_q (brane-legacy) against the "
            "PRODUCTION symmetric −Li₂^q(−z) (li2q) at each physical z_i. At "
            "every z_i (all < 1) Φ_q is convergent-but-enormous (10²–10⁶) while "
            "−Li₂^q(−z) is O(1): wiring per-generator Φ_q regresses the mass "
            "table (the −737 MeV isospin pathology); the production li2q form is "
            "bounded. The z-Habiro / Φ_q bridge has no non-regressing production "
            "continuation — the n⋆ level-selection rule is refuted across all "
            "six probed families."
        ),
        "parameters": {
            "q_0_50dps": mp.nstr(Q0, 50),
            "hbar_q_squared": mp.nstr(HBAR_Q**2, 30),
            "phi_q_at_hbar_q_sq_correction_pct": mp.nstr(corr_rep, 8),
            "production_tower_mode": "li2q",
            "superseded_tower_mode": "brane-legacy (compact q-dilog Φ_q)",
        },
        "data": {"atoms": atoms_out},
        "cross_checks": cross,
        "assertions": assertions,
        "allPassed": all(cross.values()),
        "provenance": [
            "terms-2-3-atom-per-gen-mpfr-50dps.witness.json",
            "mass-endomorphism.witness.json",
            "vhat-std-vs-full-tower-compare.witness.json",
        ],
    }
    # Hand-rolled write: this payload never reaches `WitnessBuilder.build()`,
    # so it never picked up the `q0Anchor` provenance stamp and no number of
    # re-runs would add one (bean `1j39`, bucket C).
    stamp_q0(witness, __file__)

    out = self_path.parent.parent / "zhabiro-physical-z-pin.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
