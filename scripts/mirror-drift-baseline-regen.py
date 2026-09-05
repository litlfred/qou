import json
import subprocess

rows = json.loads(subprocess.run(
    ["python3", "scripts/mirror-drift-audit.py", "--only-live", "--json"],
    capture_output=True, text=True).stdout)

full = json.loads(subprocess.run(
    ["python3", "scripts/mirror-drift-audit.py", "--json"],
    capture_output=True, text=True).stdout)
totals = {
    "shared_fqns": len({r["fqn"] for r in full}),
    "sibling_declarations": len(full),
    "faithful": sum(1 for r in full if r["faithful"]),
    "drifted": sum(1 for r in full if not r["faithful"]),
    "live": len(rows),
}

out = {
    "schema": "mirror-drift/v1",
    "note": (
        "Ratchet: this list drains, never grows. `live` is a fully-qualified Lean name "
        "declared in BOTH a content-block `.lean` sibling and the library, WHERE the "
        "block's own `lean.ref` names that exact FQN -- so every per-block checker "
        "(`q-usage-*`, `wall-side-correct`, `proof-statement-integrity`, the `da-*` "
        "family) reads the sibling and never sees the declaration `lake build` compiles."
    ),
    "not_every_live_entry_is_a_defect": (
        "A FAITHFUL live mirror is working as designed: AGENTS.md 4a gates DRIFT, not "
        "mirroring, and a `definition` block is REQUIRED to carry a sibling (3). "
        "Deleting a faithful mirror would break that requirement. The actionable subset "
        "is `live_drifted`."
    ),
    "direction_is_not_uniform": (
        "Do not assume the library is canonical. Measured across the 163 substantive "
        "drifts: 91 have the library side edited more recently, 70 the sibling side. "
        "Recency is not canonicality -- `QOU.Information.speedOfLight` has the LIBRARY "
        "edited later and the SIBLING is the 7c-compliant one (generic base ring, "
        "division-free, defining relation discharged as a theorem). Every reconciliation "
        "requires reading both sides."
    ),
    "measured_at": "2026-09-05",
    "totals_note": (
        "These move as main moves -- 47 commits of main between two runs on "
        "2026-09-05 took shared_fqns 130 -> 129 and drifted 164 -> 163 with no "
        "change from this branch. Re-measure; do not quote."
    ),
    "totals": totals,
    "live": sorted(r["fqn"] for r in rows),
    "live_drifted": sorted(r["fqn"] for r in rows if not r["faithful"]),
}
with open("docs/audits/mirror-drift-baseline.json", "w") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
print("live", len(out["live"]), "| drifted", len(out["live_drifted"]))
