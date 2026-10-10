#!/usr/bin/env python3
"""Partition the clean drain class into LOCAL vs RELAY.

A producer that READS another witness and re-emits its numbers cannot be
drained before its upstream: the float64 arrives already rounded, so casting
it to mpf and serializing at 60 digits would manufacture precision that the
value does not have.

Worked case that prompted this: categorical_q_decay_ba_low_isotopes (125
dirty fields) reads mass-formula-6term.witness.json (55 dirty), whose
`B_pred_term1_plus_term4` is a float. `float(r[...])` in the relay is a
no-op; the loss already happened upstream.

Nothing here writes.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path("/home/user/qou")
COMP = ROOT / "computations"
sys.path.insert(0, str(COMP))
import witness_raw_float64_audit as A  # noqa: E402

ORPHANS = set()
for b in (ROOT / ".beans").glob("qou-baye--*.md"):
    for m in re.findall(r"[a-z0-9][a-z0-9/_-]*\.witness\.json", b.read_text()):
        ORPHANS.add(m.split("/")[-1])

WIT_READ = re.compile(r"""["'][^"']*\.witness\.json["']""")


def producer_for(wpath):
    stem = wpath.name[: -len(".witness.json")]
    u = stem.replace("-", "_")
    for n in (stem + ".py", u + ".py", u + "_probe.py", stem + "_probe.py"):
        c = wpath.parent / n
        if c.exists():
            return c
    for n in (stem + ".py", u + ".py", u + "_probe.py", stem + "_probe.py"):
        hits = list(COMP.rglob(n))
        if hits:
            return hits[0]
    return None


def main():
    res = A.scan()
    local_f = local_n = relay_f = relay_n = 0
    relays = []
    locals_ = []
    for rel, fields in sorted(res.items(), key=lambda kv: -kv[1]):
        if fields <= 0:
            continue
        w = ROOT / rel
        if w.name in ORPHANS:
            continue
        prod = producer_for(w)
        if prod is None:
            continue
        src = prod.read_text(errors="replace")
        if "set_compute_dps" not in src or "import numpy" in src:
            continue
        # does it READ a witness other than the one it writes?
        own = w.name
        reads = {m.strip("\"'").split("/")[-1] for m in WIT_READ.findall(src)}
        reads.discard(own)
        if reads:
            relay_f += fields
            relay_n += 1
            relays.append((fields, rel, sorted(reads)[:3]))
        else:
            local_f += fields
            local_n += 1
            locals_.append((fields, rel, prod.relative_to(ROOT).as_posix()))

    print("Clean class partitioned by whether the producer READS another witness\n")
    print(f"  RELAY (downstream-limited): {relay_n:>4} witnesses, {relay_f:>6} fields")
    print(f"  LOCAL (drainable now):      {local_n:>4} witnesses, {local_f:>6} fields")
    print(f"  total:                      {relay_n+local_n:>4} witnesses, "
          f"{relay_f+local_f:>6} fields\n")
    print("TOP LOCAL TARGETS (drainable without touching an upstream):")
    for fields, rel, prod in locals_[:20]:
        print(f"  {fields:5d}  {rel}")
        print(f"         prod={prod}")
    print("\nTOP RELAYS (need their upstream drained first):")
    for fields, rel, reads in relays[:8]:
        print(f"  {fields:5d}  {rel}")
        print(f"         reads {', '.join(reads)}")


if __name__ == "__main__":
    main()
