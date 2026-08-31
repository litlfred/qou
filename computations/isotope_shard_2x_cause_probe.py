#!/usr/bin/env python3
"""qou-85o2 -- what actually moved the Z21..Z99 isotope shards, and by how much.

THE CLAIM UNDER TEST (bean qou-85o2).  98 `canonical-isotope-witness-Z*.json`
shards carry `computedAt` 2026-08-23T17:15, i.e. BEFORE the convention-C
excision `a24fdac8a1` (2026-08-24T11:04).  A spot re-run of Z=26, N=19 was
reported as `qclt_binding = 120.70 MeV` against the recorded `55.088 MeV` --
a factor **2.19** -- where the convention move predicted **0.73**.  The bean
correctly refused to call that convention drift on arithmetic that disagrees.

FINDINGS

1. The re-run is stable: three runs, bit-identical.

2. **2.19 is a STAGE MISMATCH, not a discrepancy.**  The L4 row is

       prediction = qclt_binding(Z, N) - coulomb_energy_mev(Z, A)

   `120.70` is the *pre-Coulomb* strong term; `55.088` is the *post-Coulomb*
   prediction.  2.19 = 120.70/55.088 divides one stage by the other, so it is
   not a ratio of any single quantity across the boundary.  Nothing moved by
   2.19 and nothing needed to.

3. The like-for-like moves, measured against the pre-excision sources:

       qclt_binding   166.7625 -> 120.7012   x0.7238   (predicted x0.7283)
       L4 prediction   55.0883 ->   9.0270   x0.1639

   The second is the first amplified by subtracting a CONSTANT Coulomb term
   (111.674 MeV, byte-identical across the boundary) from a shrinking strong
   term.  A 28% drop in the strong term becomes an 84% drop in the residual
   because the residual is a small difference of two large numbers.

4. **Single cause, attributed per file.**  `a24fdac8a1` touches exactly two
   Python files: `channel_binding.py` and `substrate/hecke_core_symbolic.py`.
   This probe overlays each at its pre-excision revision INDEPENDENTLY.  The
   whole move is `hecke_core_symbolic` (z: convention C -> D); the
   `channel_binding` diff is a comment plus a hardcoded self-test constant and
   contributes exactly zero.  The producer `canonical_isotope_witness.py` is
   itself byte-stable across the boundary (`scriptHash e56cabeee1ea` on both
   sides), which is why a `scriptHash`-keyed staleness check cannot see this:
   it is import-cone drift, the class AGENTS.md documents for
   `binding_canonical` / `tr_m_atom_via_transfer`.

5. Reconstructing the recorded shard: with both files at their pre-excision
   revision the L4 row reproduces the committed `55.0883274583714925` to
   ~1.2e-16 relative -- float64 resolution.  That floor is the producer's own
   `float(qclt_binding(...))` cast at `canonical_isotope_witness.py:347`, a
   NO-FLOAT64 violation reported here, not adopted.

PRECISION.  All arithmetic in this probe is carried as `mpmath.mpf`; `float()`
is never used in a computation.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "computations"))

import mpmath as mp  # noqa: E402

mp.mp.dps = 70

EXCISION = "a24fdac8a1"
Z, N = 26, 19
A = Z + N

#: The two Python files `a24fdac8a1` touches, by their path in the repo.
#: Both resolve as bare-name imports (`substrate/` is on sys.path via
#: `_path_bridge`), so either can be shadowed by an overlay dir placed first.
TOUCHED = {
    "channel_binding": "computations/channel_binding.py",
    "hecke_core_symbolic": "computations/substrate/hecke_core_symbolic.py",
}

# WHY NOT sys.path.  `_path_bridge` inserts `computations/` and every one of
# its subdirs at sys.path[0] on import, so an overlay's position depends on
# import order and on how each path string happens to resolve.  A losing
# overlay is SILENT: the run simply reports "0 contribution", which reads
# exactly like a real negative.  This probe did report a spurious 0.0 MeV for
# `hecke_core_symbolic` before the guard below existed.
#
# So the overlay is installed deterministically: each shadowed module is
# exec'd from its pre-excision source and registered in `sys.modules` BEFORE
# anything can import it.  `sys.modules` is consulted ahead of any path, so
# this cannot be overtaken.  Dependencies are registered first
# (`hecke_core_symbolic` before its importer `channel_binding`), and an
# assertion still verifies each module's `__file__` before any number is
# trusted.
_CHILD = """
import sys
sys.path.insert(0, {comp!r})
import _path_bridge  # noqa: F401
import importlib.util as _iu
for _name, _src in {overlay!r}:
    _spec = _iu.spec_from_file_location(_name, _src)
    _mod = _iu.module_from_spec(_spec)
    sys.modules[_name] = _mod
    _spec.loader.exec_module(_mod)
import mpmath as mp
from _precision import set_compute_dps
set_compute_dps(70)
import channel_binding, hecke_core_symbolic  # noqa: E401
{assertion}
from channel_binding import qclt_binding
from coulomb_energy import coulomb_energy_mev
b = mp.mpf(qclt_binding({z}, {n}, colour_weighted=True))
c = mp.mpf(coulomb_energy_mev({z}, {a}))
print(mp.nstr(b, 45))
print(mp.nstr(c, 45))
"""

#: Registration order: a module must be registered before its importers.
_ORDER = ["hecke_core_symbolic", "channel_binding"]


def _measure(overlay_dir: Path | None = None) -> dict[str, mp.mpf]:
    """Compute the two L4 components, optionally with `overlay_dir` shadowing."""
    items: list[tuple[str, str]] = []
    assertion = ""
    if overlay_dir is not None:
        present = {f.stem for f in overlay_dir.glob("*.py")}
        items = [(n, str(overlay_dir / f"{n}.py"))
                 for n in _ORDER if n in present]
        for name, _ in items:
            assertion += (
                f"assert {name}.__file__ == {str(overlay_dir / (name + '.py'))!r}"
                f", 'OVERLAY NO-OP: {name} loaded from ' + {name}.__file__\n"
            )
    code = _CHILD.format(
        comp=str(ROOT / "computations"), overlay=items,
        assertion=assertion, z=Z, n=N, a=A,
    )
    out = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, cwd=ROOT
    )
    if out.returncode != 0:
        raise RuntimeError(f"probe failed:\n{out.stderr[-2000:]}")
    b_s, c_s = out.stdout.split()
    b, c = mp.mpf(b_s), mp.mpf(c_s)
    return {"qclt": b, "coulomb": c, "l4": b - c}


def _overlay(names: list[str]) -> Path:
    """Materialise the named modules at their PRE-excision revision."""
    d = Path("/tmp/85o2-overlay-" + "+".join(sorted(names)))
    d.mkdir(parents=True, exist_ok=True)
    for n in names:
        blob = subprocess.run(
            ["git", "show", f"{EXCISION}^:{TOUCHED[n]}"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
        (d / f"{n}.py").write_text(blob)
    return d


def main() -> int:
    print("=" * 74)
    print("qou-85o2 -- Z=26, N=19 (Fe-45), layer L4-qclt-colour-weighted")
    print("=" * 74)

    # --- 1. stability ------------------------------------------------------
    print("\n[1] STABILITY -- three runs at HEAD")
    runs = [_measure() for _ in range(3)]
    for i, r in enumerate(runs):
        print(f"    run {i}: qclt={mp.nstr(r['qclt'], 25)}  "
              f"L4={mp.nstr(r['l4'], 25)}")
    if len({mp.nstr(r["qclt"], 45) for r in runs}) != 1:
        print("    !! NOT STABLE -- that is the finding; stop here.")
        return 1
    print("    bit-identical across 3 runs: True")
    now = runs[0]

    # --- 2. per-file attribution ------------------------------------------
    print(f"\n[2] PER-FILE ATTRIBUTION -- each file overlaid at {EXCISION}^")
    both = _measure(_overlay(list(TOUCHED)))
    only_cb = _measure(_overlay(["channel_binding"]))
    only_hcs = _measure(_overlay(["hecke_core_symbolic"]))
    print(f"    HEAD (both files post-excision)   qclt="
          f"{mp.nstr(now['qclt'], 22)}  L4={mp.nstr(now['l4'], 22)}")
    print(f"    channel_binding      reverted     qclt="
          f"{mp.nstr(only_cb['qclt'], 22)}  L4={mp.nstr(only_cb['l4'], 22)}")
    print(f"    hecke_core_symbolic  reverted     qclt="
          f"{mp.nstr(only_hcs['qclt'], 22)}  L4={mp.nstr(only_hcs['l4'], 22)}")
    print(f"    BOTH                 reverted     qclt="
          f"{mp.nstr(both['qclt'], 22)}  L4={mp.nstr(both['l4'], 22)}")
    print()
    print(f"    channel_binding contributes:      "
          f"{mp.nstr(only_cb['qclt'] - now['qclt'], 5)} MeV  "
          f"(zero: {only_cb['qclt'] == now['qclt']})")
    print(f"    hecke_core_symbolic contributes:  "
          f"{mp.nstr(only_hcs['qclt'] - now['qclt'], 8)} MeV")
    print(f"    the two together:                 "
          f"{mp.nstr(both['qclt'] - now['qclt'], 8)} MeV")
    print(f"    hecke_core_symbolic alone == both: "
          f"{only_hcs['qclt'] == both['qclt']}")

    # --- 3. does pre-excision reproduce the committed shard? --------------
    shard = ROOT / "computations/canonical-isotope-witness-Z26.witness.json"
    row = [r for r in json.load(open(shard))["data"]["rows"] if r["N"] == N][0]
    recorded = mp.mpf(row["prediction_MeV_50dps"])
    print("\n[3] DOES PRE-EXCISION REPRODUCE THE COMMITTED SHARD?")
    print(f"    recorded (Z26 shard) = {mp.nstr(recorded, 30)}")
    print(f"    pre-excision L4      = {mp.nstr(both['l4'], 30)}")
    rel = abs(both["l4"] - recorded) / recorded
    print(f"    relative diff        = {mp.nstr(rel, 5)}")
    print(f"    at float64 floor (<1e-15): {rel < mp.mpf('1e-15')}  "
          "<- producer casts through float(), see docstring")

    # --- 4. the ratios ------------------------------------------------------
    print("\n[4] THE ACTUAL MOVES")
    print(f"    coulomb unchanged across boundary: "
          f"{both['coulomb'] == now['coulomb']}")
    r_q = now["qclt"] / both["qclt"]
    r_l4 = now["l4"] / both["l4"]
    print(f"    qclt_binding  {mp.nstr(both['qclt'], 12)} -> "
          f"{mp.nstr(now['qclt'], 12)}   x{mp.nstr(r_q, 8)}")
    print(f"    L4 prediction {mp.nstr(both['l4'], 12)} -> "
          f"{mp.nstr(now['l4'], 12)}   x{mp.nstr(r_l4, 8)}")

    print("\n[5] WHERE 2.19 CAME FROM -- a stage mismatch")
    print(f"    fresh qclt / recorded L4 = "
          f"{mp.nstr(now['qclt'] / recorded, 10)}   <- the reported '2.19'")
    print("    numerator PRE-Coulomb, denominator POST-Coulomb.")
    print(f"    rebuilt from the two real quantities: "
          f"{mp.nstr((both['qclt'] * r_q) / both['l4'], 10)}")

    print("\n[6] PREDICTED vs MEASURED convention move")
    f_c, f_d = mp.mpf("0.3948"), mp.mpf("0.5082")
    pred = mp.log(f_d) / mp.log(f_c)
    print(f"    f_pn(std): C={mp.nstr(f_c, 6)} -> D={mp.nstr(f_d, 6)}")
    print(f"    log-ratio prediction  x{mp.nstr(pred, 8)}")
    print(f"    measured on qclt      x{mp.nstr(r_q, 8)}")
    print(f"    disagreement          "
          f"{mp.nstr(abs(pred - r_q) / r_q * 100, 4)} %")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
