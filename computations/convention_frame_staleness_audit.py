#!/usr/bin/env python3
"""convention_frame_staleness_audit.py — witnesses left in the convention-C
frame under a producer that has since migrated to convention D.

WHY THIS EXISTS. PR #4899 excised convention C from the producer layer ("178
sites -> 0") and reported "witnesses regenerated across 68 producers". Two
witnesses it missed were then found INDEPENDENTLY, from different directions,
by two different sessions:

  * `qou-580o` — `qbeta-*`, found while auditing the c_3 ladder (PR #5265).
  * `qou-h4ab` — `wedderburn-lp-ew-wiring`, found while porting that producer
    off float64; its `t_legacy_matrix_entries` moved 13-21%.

Two independent hand-finds of the same class is the signal that the class is
not two items long. This looks for the class.

THE DECISIVE TEST, and why the scan alone is not it. A candidate is CONFIRMED
by swapping the producer's `z` back to the C form and checking that the
COMMITTED value reappears. Both confirmed cases reproduce exactly:

    wedderburn-lp-ew-wiring  proton  0.6003377241833765   -> 2.1e-16
                             neutron 0.3727036271108378   -> 5.7e-16
    fr-pullback-cosh-h       best_variance_finite
                             1.537500801376956 (D gives 1.488319082475366)

That last one was found BY this scan and then confirmed, which is what makes
the scan worth committing rather than a grep someone ran once.

WHAT THE SCAN CAN AND CANNOT SAY. It is high-recall by construction and its
output is a CANDIDATE list requiring an agent verdict, in the same spirit as
`lean-vacuity-axiom-audit` and the raw-float64 ratchet. Specifically:

  * `q**3/(q**2+1)` is a SHAPE, not a meaning. The scan requires it to be
    bound to a Markov-named variable (`z`, `z_mark`, `z_D`, `z_electron`, …)
    to avoid matching arbitrary arithmetic. A producer that computes the
    Markov parameter under some other name is MISSED.
  * "witness predates the migration date" does not prove its values are
    C-frame — the producer may not have used `z` in anything serialized.
  * `scriptHash` matching means the producer is UNCHANGED since the witness
    was written, so that same D code produced it. Those are dropped: their
    early date is evidence the D form predates the migration for that file,
    not evidence of staleness.

Run:  python3 -u convention_frame_staleness_audit.py 2>&1 | tee /tmp/cfs.log
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for _p in (HERE, HERE / "substrate", HERE / "hecke"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

ROOT = HERE.parent

#: The owner ruling making convention D canonical is 2026-08-15; the producer
#: layer flipped on 2026-08-10 (PR #4899). The earlier date is the right cut:
#: a witness written before the producers moved cannot carry D values.
D_MIGRATION = "2026-08-10"

#: Markov-parameter variable names seen in the corpus. Deliberately a NAME
#: list rather than "any assignment": the shape alone over-matches badly (121
#: candidates unfiltered vs 137 producers here, with the difference being
#: arbitrary `x**3/(y**2+1)` arithmetic).
_Z_NAME = r"(?:z|z_\w+|\w+_z|zmark|z_mark|markov\w*|\w*_markov)"
D_BOUND = re.compile(
    rf"^\s*{_Z_NAME}\s*=\s*[^=\n]*\*\*\s*3\s*/\s*\(\s*\w+\s*\*\*\s*2\s*\+\s*1\s*\)",
    re.IGNORECASE | re.MULTILINE)


def _witnesses_by_producer(comp: Path) -> dict:
    out: dict[str, list] = {}
    for w in comp.rglob("*.witness.json"):
        if "_deprecated" in str(w):
            continue
        try:
            d = json.loads(w.read_text())
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        sf = d.get("scriptFile")
        if sf:
            out.setdefault(Path(sf).name, []).append((w, d))
    return out


def scan(comp: Path) -> list[dict]:
    by_prod = _witnesses_by_producer(comp)
    rows = []
    for py in comp.rglob("*.py"):
        if "_deprecated" in str(py):
            continue
        try:
            text = py.read_text()
        except Exception:
            continue
        m = D_BOUND.search(text)
        if not m:
            continue
        cur = hashlib.sha256(text.encode()).hexdigest()[:12]
        for w, d in by_prod.get(py.name, []):
            rows.append({
                "producer": py.relative_to(ROOT).as_posix(),
                "witness": w.relative_to(ROOT).as_posix(),
                "computedAt": (d.get("computedAt") or "")[:10],
                "hash_ok": d.get("scriptHash") == cur,
                "z_line": m.group(0).strip(),
            })
    return rows


def main() -> int:
    comp = HERE
    rows = scan(comp)
    dated = [r for r in rows if r["computedAt"]]
    pre = [r for r in dated if r["computedAt"] < D_MIGRATION]
    # producer unchanged => the same D code wrote it => not a migration victim
    suspect = sorted((r for r in pre if not r["hash_ok"]),
                     key=lambda r: r["computedAt"])

    print("=" * 78)
    print("Convention-frame staleness — C-frame witnesses under D producers")
    print("=" * 78)
    print(f"  producers with a D-form bound to a Markov-named variable : "
          f"{len({r['producer'] for r in rows})}")
    print(f"  their witnesses                                          : {len(rows)}")
    print(f"  witness predates {D_MIGRATION}                           : {len(pre)}")
    print(f"  ... and producer changed since (SUSPECT)                 : {len(suspect)}")
    print(f"  ... dropped, producer unchanged (same D code wrote it)   : "
          f"{len(pre) - len(suspect)}\n")
    print("  CANDIDATES — each needs the decisive test (swap z to the C form,")
    print("  check the COMMITTED value reappears) before being called stale:\n")
    for r in suspect:
        print(f"    {r['computedAt']}  {r['witness']}")
        print(f"        <- {r['producer']}")

    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:
        print("\n(witness_base unavailable — scan-only)")
        return 0

    w = (WitnessBuilder("convention-frame-staleness-audit", engine="static-scan")
         .add_parameter("d_migration_date", D_MIGRATION)
         .add_parameter("detector", "D-form bound to a Markov-named variable"))
    w.add_assertion("scan_completed", "1", "1", tolerance="0")
    w.add_data("producers_with_d_form", len({r["producer"] for r in rows}))
    w.add_data("witnesses_examined", len(rows))
    w.add_data("suspect_count", len(suspect))
    w.add_data("dropped_producer_unchanged", len(pre) - len(suspect))
    w.add_data("confirmed_by_decisive_test", [
        {"witness": "computations/wedderburn-lp-ew-wiring.witness.json",
         "bean": "qou-h4ab", "c_frame_reproduces_to": "2.1e-16 / 5.7e-16"},
        {"witness": "computations/fr-pullback-cosh-h.witness.json",
         "bean": "qou-g49k-followup",
         "committed": "1.537500801376956",
         "convention_D": "1.488319082475366",
         "convention_C": "1.537500801376956 (exact)"},
    ])
    w.add_data("candidates", [
        {"witness": r["witness"], "producer": r["producer"],
         "computedAt": r["computedAt"]} for r in suspect])
    out = w.save()
    print(f"\nWrote: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
