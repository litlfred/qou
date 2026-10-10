#!/usr/bin/env python3
# polynomial_q_not_applicable: static source/provenance audit; emits no numeric physics.
"""Guard for detector-blindness taxonomy row 50: the prediction path does no arithmetic.

Bean `qou-s16e` (T5), epic `qou-8lxd`.

**What this answers.** `qou-s16e` asks for a proof that `predict(obs)` is a
closed term with no numeric literal untraceable to a calibration or a proved
categorical constant, and names
[`computations/no_free_parameter_certificate.py`](../no_free_parameter_certificate.py)
as the mechanism. That certificate classifies numeric literals in *arithmetic*
position in Python source. **`qou_mass.api.predict()` has none**: it calls
`_lookup_row(Z, N)`, which loads a per-Z JSON shard and returns the stored
`M_pred_MeV` / `err_ppm` verbatim.

So adding `predict` as a sixth certificate entry point would print a clean
`0 untraceable` and establish nothing. This probe pins that, and pins the
mechanism that *does* establish traceability for that path: the shards are
full witness files carrying their own provenance, byte-identical to their
`computations/` sources.

**What it checks.**

| check | what a failure would mean |
|---|---|
| the certificate's closure from the facade is **1 module** | the walk now follows the facade's imports — the 0-literal result would no longer be vacuous, so re-read row 50 |
| the classifier finds **0** arithmetic literals in `qou_mass/api.py` | the facade grew arithmetic; it may no longer be a data lookup |
| every isotope shard carries `scriptFile`/`scriptHash`/`commitSha`/`q0Anchor` | a shard's provenance is missing, so that row's number is genuinely untraceable |
| every isotope shard is byte-identical to its `computations/` source | the vendored copy has drifted from its producer (cf. `sync-qou-mass-vendor.py`) |

**The closure check is the discriminator; the literal count alone is not.**
`binding_K_direct` classifies **0** literals over a 7-module closure, so a bare
zero proves nothing either way. What makes the facade's zero vacuous is that the
walk never left the file: `SEARCH_ROOTS` excludes the `qou-mass` tree, every
first-party import in `api.py` is relative, and two of those are deferred inside
function bodies.

🛑 **Do not "fix" this by adding `qou-mass/` to `SEARCH_ROOTS`.** `predict()`
does no arithmetic at any closure size, so a wider walk would make the clean
result *more* convincing rather than more meaningful.

**Epistemic scope (STRICT).** Clean here is *not* a certificate that
`predict()` is parameter-free; it is the narrower, checkable pair of facts that
(a) a source-literal audit cannot speak to this path and (b) the path's
provenance mechanism is intact. The certificate's own docstring makes the same
disclaimer about itself: *"A clean run is evidence the path is parameter-free,
never a theorem that it is."*

Exit 0 when all three checks pass, 1 otherwise. `--selftest` pins the catch and
the limit and hardcodes neither.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent

FACADE = REPO / "qou-mass" / "src" / "qou_mass" / "api.py"
SHARDS = REPO / "qou-mass" / "src" / "qou_mass" / "data" / "isotopes"
SOURCE = REPO / "computations"
PROVENANCE = ("scriptFile", "scriptHash", "commitSha", "q0Anchor")

# The certificate's existing entry points that DO compute. Named so a reader can
# see why the gap stayed latent: the facade is the first non-computing one tried.
COMPUTING_ENTRY_POINTS = (
    "canonical_mass",
    "per_observable_100x_status",
    "meson_mass_from_hecke",
    "binding_K_direct",
)


def _sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def _load_certificate():
    """Import the committed classifier. Returns the module, or None if absent."""
    sys.path.insert(0, str(SOURCE))
    try:
        import no_free_parameter_certificate as cert  # noqa: PLC0415
    except Exception:  # pragma: no cover - the certificate is expected present
        return None
    return cert


def classify_module(path: pathlib.Path, name: str = "probe_target") -> list[dict]:
    """Run the certificate's own `audit_module` against an arbitrary file."""
    cert = _load_certificate()
    if cert is None:
        raise RuntimeError("no_free_parameter_certificate not importable")
    original = cert._resolve

    def _resolve(mod: str):
        return path if mod == name else original(mod)

    cert._resolve = _resolve
    try:
        return cert.audit_module(name)
    finally:
        cert._resolve = original


def closure_from(path: pathlib.Path, name: str = "probe_target") -> tuple[list[str], list[str]]:
    """Run the certificate's own `_closure` with `path` standing in for `name`."""
    cert = _load_certificate()
    if cert is None:
        raise RuntimeError("no_free_parameter_certificate not importable")
    original = cert._resolve

    def _resolve(mod: str):
        return path if mod == name else original(mod)

    cert._resolve = _resolve
    try:
        return cert._closure([name])
    finally:
        cert._resolve = original


def check_facade_closure_collapses() -> tuple[bool, str]:
    """The walk must still fail to leave api.py — that is what makes 0 vacuous."""
    mods, unresolved = closure_from(FACADE)
    ok = len(mods) == 1
    detail = f"closure={len(mods)} module(s) {mods}, unresolved={unresolved}"
    if not ok:
        detail += " — the walk now follows the facade's imports; row 50 needs re-measuring"
    return ok, detail


def check_facade_has_no_literals() -> tuple[bool, str]:
    rows = classify_module(FACADE)
    n = len(rows)
    ok = n == 0
    detail = f"{n} arithmetic literal(s) classified in {FACADE.name}"
    if not ok:
        detail += " — the facade now computes; row 50's premise has changed"
    return ok, detail


def check_shard_provenance() -> tuple[bool, str]:
    shards = sorted(SHARDS.glob("*.witness.json"))
    if not shards:
        return False, f"no shards under {SHARDS}"
    missing: dict[str, int] = {k: 0 for k in PROVENANCE}
    anchors: dict[str, int] = {}
    hashes: dict[str, int] = {}
    rows = 0
    for f in shards:
        d = json.loads(f.read_text())
        for k in PROVENANCE:
            if not d.get(k):
                missing[k] += 1
        anchors[str(d.get("q0Anchor"))] = anchors.get(str(d.get("q0Anchor")), 0) + 1
        hashes[str(d.get("scriptHash"))] = hashes.get(str(d.get("scriptHash")), 0) + 1
        rows += len(d.get("data", {}).get("rows", []))
    ok = not any(missing.values())
    return ok, (
        f"{len(shards)} shard(s), {rows} row(s); missing={missing}; "
        f"anchors={anchors}; scriptHash={hashes}"
    )


def check_shards_match_source() -> tuple[bool, str]:
    shards = sorted(SHARDS.glob("*.witness.json"))
    same = diff = absent = 0
    drifted: list[str] = []
    for v in shards:
        cands = list(SOURCE.rglob(v.name))
        if not cands:
            absent += 1
            continue
        if _sha(v) == _sha(cands[0]):
            same += 1
        else:
            diff += 1
            drifted.append(v.name)
    ok = diff == 0 and absent == 0
    detail = f"identical={same} drifted={diff} no_source={absent}"
    if drifted:
        detail += " :: " + ", ".join(drifted[:5])
    return ok, detail


CHECKS = (
    ("closure collapses to the facade itself", check_facade_closure_collapses),
    ("facade does no arithmetic", check_facade_has_no_literals),
    ("shard provenance complete", check_shard_provenance),
    ("shards match computations/", check_shards_match_source),
)


def self_test() -> int:
    """Pin the catch and the limit; hardcode neither verdict."""
    failures = 0

    # THE CATCH — the classifier must be live, i.e. it must find literals in a
    # module that genuinely has them. Without this the first check above is
    # satisfied by the classifier being broken, which is taxonomy row 48.
    cert = _load_certificate()
    if cert is None:
        print("  selftest FAIL: certificate not importable")
        return 1
    computing = [m for m in COMPUTING_ENTRY_POINTS if cert._resolve(m) is not None]
    if not computing:
        print("  selftest FAIL: none of the computing entry points resolve")
        failures += 1
    else:
        found = {m: len(cert.audit_module(m)) for m in computing}
        if not any(found.values()):
            print(f"  selftest FAIL: classifier found 0 literals in every "
                  f"computing entry point {found} — it is dead, not clean")
            failures += 1
        else:
            print(f"  selftest ok: classifier is live on computing paths {found}")
        # Closure sizes are the contrast row 50 rests on. Reported, not asserted:
        # the computing entry points are someone else's arc and may legitimately move.
        sizes = {m: len(cert._closure([m])[0]) for m in computing}
        print(f"  selftest info: computing-path closure sizes {sizes} "
              f"vs facade {len(closure_from(FACADE)[0])}")

    # THE LIMIT — the facade must still be a lookup. Asserted by structure, not
    # by the literal count, so the two cannot certify each other.
    src = FACADE.read_text()
    if "_lookup_row(" not in src:
        print("  selftest FAIL: api.py no longer calls _lookup_row; row 50's "
              "premise (predict is a data lookup) needs re-measuring")
        failures += 1
    else:
        print("  selftest ok: api.py still routes predict() through _lookup_row")

    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        print("predict_path_literal_scope_probe --selftest")
        return self_test()

    print("Row 50 guard — the prediction path does no arithmetic")
    print(f"  facade: {FACADE.relative_to(REPO)}")
    failures = 0
    for label, fn in CHECKS:
        ok, detail = fn()
        print(f"  [{'ok ' if ok else 'RED'}] {label}: {detail}")
        if not ok:
            failures += 1
    print()
    if failures:
        print(f"RED — {failures} check(s) failed")
        return 1
    print("clean — a source-literal audit cannot speak to this path, and the "
          "path's provenance mechanism is intact. NOT a parameter-free certificate.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
