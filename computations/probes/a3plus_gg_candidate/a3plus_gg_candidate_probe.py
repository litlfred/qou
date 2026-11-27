#!/usr/bin/env python3
"""A≥3 Reeb/assembly chain on the #7741 γγ candidate word — comparison arm.

Pre-registration: `preregistration.md` (this directory), pushed before any
number was computed. Owner card 2026-11-21. Adopts nothing: the γγ word is not
ruled (#7876).

Word (generators 0-indexed): V = σ_a σ_{a+1}^{-1}.
  nucleon k  : V³ on (3k, 3k+1), proton and neutron alike;
  free       : nucleon blocks only;
  atom arm L : after nucleon k < A−1, bond V³ on (3k+1, 3k+2);
  atom arm R : after nucleon k < A−1, bond V³ on (3k+2, 3k+3).

χ^λ for every λ ⊢ 3A is computed at 50 dps with
`pyhecke_native.chi_lambda_all_partitions_mpfr` at the proton q₀. The
production producers `binding_reeb_phase_decomposition.py` and
`binding_a3plus_full_theta_assembly.py` are then run UNMODIFIED in a scratch
copy whose `atom-chi-rust-*` inputs are replaced by these χ. Nothing in the
real tree is written except this probe's own witness.

Usage:
    python3 -u computations/probes/a3plus_gg_candidate/a3plus_gg_candidate_probe.py \
        2>&1 | tee /tmp/a3plus_gg_candidate.log
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parents[1]
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401, E402

import mpmath as mp  # noqa: E402
import pyhecke_native as pn  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import fmt  # noqa: E402

DPS = 50
ATOMS = [("D", "d", 1, 1), ("T", "t", 1, 2), ("3He", "3he", 2, 1), ("4He", "4he", 2, 2)]
PRODUCERS = ["binding_reeb_phase_decomposition.py",
             "binding_a3plus_full_theta_assembly.py"]
ASM_INPUTS = ["chi-deuteron-h6-at-q0-50dps.witness.json",
              "chi-tritium-h9-at-q0-50dps.witness.json",
              "chi-helium-3-h9-at-q0-50dps.witness.json",
              "chi-helium-4-h12-at-q0-50dps.witness.json"]
ASM_NAME = "binding-a3plus-full-theta-assembly.witness.json"


def v_cubed(a: int) -> list[tuple[int, int]]:
    """V³ = (σ_a σ_{a+1}^{-1})³ as a signed 1-indexed braid word."""
    return [(1, a + 1), (-1, a + 2)] * 3


def word(A: int, arm: str | None) -> list[tuple[int, int]]:
    w: list[tuple[int, int]] = []
    for k in range(A):
        w += v_cubed(3 * k)
        if arm is not None and k < A - 1:
            w += v_cubed(3 * k + 1 if arm == "L" else 3 * k + 2)
    return w


def chi_all(n: int, w) -> list[dict]:
    t0 = time.time()
    out = [{"partition": list(shape), "dim": -1, "chi_lambda": s}
           for shape, s in pn.chi_lambda_all_partitions_mpfr(n, w, Q_50_DIGIT_STR, DPS)]
    print(f"    {n} strands, {len(w)} letters, {len(out)} partitions: "
          f"{time.time() - t0:.1f}s", flush=True)
    return out


def main() -> int:
    mp.mp.dps = DPS + 10
    t_start = time.time()
    chi: dict[str, dict] = {}
    for name, slug, Z, N in ATOMS:
        A = Z + N
        n = 3 * A
        print(f"{name}: A={A}, n={n}", flush=True)
        chi[name] = {"free": chi_all(n, word(A, None)),
                     "L": chi_all(n, word(A, "L")),
                     "R": chi_all(n, word(A, "R"))}
        print(f"  elapsed {time.time() - t_start:.0f}s", flush=True)

    production = json.loads((COMP / ASM_NAME).read_text())
    arms: dict[str, dict] = {}
    for arm in ("L", "R"):
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            for p in PRODUCERS:
                shutil.copy(COMP / p, tdp / p)
            for f in ASM_INPUTS:
                shutil.copy(COMP / f, tdp / f)
            for name, slug, Z, N in ATOMS:
                (tdp / f"atom-chi-rust-{slug}.witness.json").write_text(json.dumps(
                    {"data": {"free": {"by_partition": chi[name]["free"]},
                              "atom": {"by_partition": chi[name][arm]}}}))
            env_path = f"{COMP}:{COMP / 'substrate'}"
            for p in PRODUCERS:
                r = subprocess.run([sys.executable, str(tdp / p)], cwd=COMP,
                                   env={**__import__("os").environ, "PYTHONPATH": env_path},
                                   capture_output=True, text=True)
                if r.returncode != 0:
                    print(r.stdout[-2000:], r.stderr[-2000:], file=sys.stderr)
                    raise SystemExit(f"arm {arm}: {p} exited {r.returncode}")
            arms[arm] = json.loads((tdp / ASM_NAME).read_text())["data"]

    def summarise(data: dict) -> dict:
        out = {}
        for atom in ("D", "T", "3He", "4He"):
            row = {"sum_y_dim_abs_dtheta": data["per_atom_sums"][atom]["sum_y_dim_abs_dtheta"]}
            for rho, block in data["rho_candidate_tests_volume_scaled"].items():
                if not isinstance(block, dict) or "per_atom" not in block:
                    continue
                pa = block["per_atom"][atom]
                row[rho] = {"B_pred_MeV": pa["B_pred_MeV"], "rel_err": pa["rel_err"]}
            out[atom] = row
        return out

    summary = {"production_borromean": summarise(production["data"]),
               "gg_arm_L": summarise(arms["L"]),
               "gg_arm_R": summarise(arms["R"])}

    print("\n|rel_err| at rho_v2_mu_0 (volume-scaled):")
    print(f"  {'atom':5s} {'production':>12s} {'gg arm L':>12s} {'gg arm R':>12s}")
    for atom in ("D", "T", "3He", "4He"):
        vals = [mp.mpf(summary[k][atom]["rho_v2_mu_0"]["rel_err"]) * 100
                for k in ("production_borromean", "gg_arm_L", "gg_arm_R")]
        print(f"  {atom:5s} " + " ".join(f"{mp.nstr(v, 5):>11s}%" for v in vals))

    wb = WitnessBuilder("a3plus-gg-candidate", engine="pyhecke_native mpfr + mpmath",
                        output_dir=HERE)
    wb.set_description(
        "COMPARISON ARM, adopts nothing. A>=3 Reeb/assembly chain on the #7741 "
        "gamma-gamma candidate word (nucleon V^3, bond V^3 in two pre-registered "
        "site arms L/R) beside the production Borromean word. The candidate is "
        "not ruled (#7876); Vol(K_bind) is the production volume, not derived "
        "for this word.")
    wb.add_data("word", {"V": "sigma_a sigma_{a+1}^-1", "nucleon": "V^3 on (3k,3k+1)",
                         "bond_arm_L": "V^3 on (3k+1,3k+2)",
                         "bond_arm_R": "V^3 on (3k+2,3k+3)", "dps": DPS,
                         "q0": Q_50_DIGIT_STR})
    wb.add_data("chi", {a: {k: v for k, v in chi[a].items()} for a in chi})
    wb.add_data("summary", summary)
    wb.add_assertion("both_arms_and_four_atoms_computed",
                     computed=sum(len(summary[k]) for k in summary), expected=12,
                     tolerance=0, source="3 columns x 4 atoms")
    wb.save({"q0Anchor": "proton"})
    print(f"\ntotal {time.time() - t_start:.0f}s; witness written", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
