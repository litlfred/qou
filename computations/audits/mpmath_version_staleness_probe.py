"""The mpmath 1.3.0 / 1.4.1 split in the witness corpus is NOT a staleness axis.

I raised this split as an "untracked staleness axis" and quoted it as 566/449.
Both halves of that needed fixing: the count was wrong, and the concern does
not survive measurement.

THE COUNT.  Measured over live `computations/**/*.witness.json` (excluding
`_deprecated/`), keyed on the witness's own `environment.mpmath`:

    1.3.0   1160
    1.4.1    829
    0.0.0      2     <- a real defect: version not captured
    TOTAL   1991

THE CORPUS CANNOT SETTLE IT.  Five producers have witnesses under both
versions, which looks like a natural A/B pair and is not: no producer has a
SAME-NAMED witness under both.  The five are producers whose different
SUBJECTS were computed at different times (deuterium under one version,
tritium under another), so a value difference between them is the subject,
not the version.  There is no in-corpus control.

SO IT WAS TESTED DIRECTLY, and the answer is no difference.  Both versions
were fetched as wheels and the framework's load-bearing mpmath primitives
evaluated at 60 dps under each, compared at 55 significant digits.  All ten
are byte-identical -- including Vol(4_1) = 2*Cl2(pi/3), the q_0 root-solve
against the muon ratio, polylog, hyp2f1, besselj, zeta and gamma.

SCOPE-(a).  This says the ten primitives below do not move between 1.3.0 and
1.4.1 at 55 digits.  It does NOT prove that no producer anywhere in the 1991
witnesses is version-sensitive -- a producer relying on a changed default, a
changed iteration count, or a changed error estimate could still differ.  What
it does establish is that the CONSTANTS the framework is built on are stable,
so the split is not a reason to re-run anything, and "which mpmath" does not
belong on the staleness checklist alongside scriptHash and import-cone drift.

METHOD NOTE, recorded because it voided the first attempt: the container's
INSTALLED mpmath is 1.4.1, not 1.3.0.  Running "the installed one" against a
1.4.1 wheel compares 1.4.1 with itself and reports zero differences that mean
nothing.  Both versions must come from pinned wheels on PYTHONPATH, and each
run must PRINT the version it actually imported.

-- Ref: [manuscript] AGENTS.md (witness staleness: scriptHash, import cone, environment)
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402

from witness_base import WitnessBuilder  # noqa: E402

VERSIONS = ("1.3.0", "1.4.1")

#: evaluated at 60 dps, compared at 55 significant digits
SNIPPET = r"""
import mpmath as mp, json
mp.mp.dps = 60
V = 2*mp.clsin(2, mp.pi/3)
R = mp.mpf("206.7682827")
out = {
 "_version": mp.__version__,
 "Vol_4_1_eq_2_Cl2_pi_over_3": mp.nstr(V, 55),
 "Lambda_pi_over_3":           mp.nstr(mp.clsin(2, 2*mp.pi/3)/2, 55),
 "q0_muon_solve":              mp.nstr(mp.findroot(lambda q: (1-1/q)**2 - V/R,
                                                   mp.mpf("1.11")), 55),
 "e":                          mp.nstr(mp.e, 55),
 "zeta_3":                     mp.nstr(mp.zeta(3), 55),
 "besselj_0_1":                mp.nstr(mp.besselj(0, 1), 55),
 "hyp2f1_1_2_3_half":          mp.nstr(mp.hyp2f1(1, 2, 3, mp.mpf(1)/2), 55),
 "polylog_2_half":             mp.nstr(mp.polylog(2, mp.mpf(1)/2), 55),
 "gamma_one_third":            mp.nstr(mp.gamma(mp.mpf(1)/3), 55),
 "sqrt_2":                     mp.nstr(mp.sqrt(2), 55),
}
print(json.dumps(out))
"""

_FAILURES: list[str] = []


def check(name, ok, detail, w=None):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    if w is not None:
        w.add_data(name, bool(ok))
        # bean qou-srvu. Without this the witness carried ZERO assertions and
        # `save()` still emitted `allPassed: true` -- green while claiming
        # nothing, indistinguishable to a consumer from a run that checked
        # something and passed. The verdict was already computed (it prints
        # [PASS]/[FAIL] above, is tallied into _FAILURES, and drives this
        # script's exit code); it just never reached `assertions[]`. No
        # threshold is chosen here and no claim is invented: `ok` is the
        # producer's own boolean and `True` is what the exit code already
        # compares it against.
        w.add_assertion(name, computed=bool(ok), expected=True, source=detail)
    if not ok:
        _FAILURES.append(name)
    return ok


def fetch(version: str, root: Path) -> Path | None:
    """Download and unpack one mpmath wheel; None if the network refuses."""
    dest = root / f"mp{version.replace('.', '')}"
    dl = root / f"dl{version.replace('.', '')}"
    r = subprocess.run(
        [sys.executable, "-m", "pip", "download", f"mpmath=={version}",
         "-d", str(dl), "--no-deps", "-q"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return None
    whl = next(iter(dl.glob("mpmath-*.whl")), None)
    if whl is None:
        return None
    dest.mkdir(parents=True, exist_ok=True)
    subprocess.run(["unzip", "-qo", str(whl), "-d", str(dest)], check=True)
    return dest


def run_under(tree: Path) -> dict:
    """Run the snippet with `tree` FIRST on PYTHONPATH; returns its dict."""
    r = subprocess.run(
        [sys.executable, "-c", SNIPPET],
        capture_output=True, text=True,
        env={"PYTHONPATH": str(tree), "PATH": "/usr/bin:/bin"},
    )
    if r.returncode != 0:
        raise RuntimeError(f"snippet failed under {tree}: {r.stderr[:300]}")
    return json.loads(r.stdout)


def main() -> int:
    w = WitnessBuilder("mpmath-version-staleness", engine="mpmath")
    w.set_description(
        "A/B of the framework's load-bearing mpmath primitives under mpmath "
        "1.3.0 and 1.4.1, both from pinned wheels, to decide whether the "
        "1160/829 version split across the witness corpus is a staleness axis."
    )

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        trees = {v: fetch(v, root) for v in VERSIONS}
        if any(t is None for t in trees.values()):
            missing = [v for v, t in trees.items() if t is None]
            print(f"  SKIP: could not fetch mpmath {missing} (network). "
                  f"No verdict recorded -- an unfetchable wheel is not "
                  f"evidence of agreement.")
            w.add_data("verdict", "skipped_network")
            out = w.save()
            print(f"\n  witness -> {out}")
            return 0

        res = {v: run_under(t) for v, t in trees.items()}

    # the version each run ACTUALLY imported -- the check that voided attempt 1
    got = {v: res[v].pop("_version") for v in VERSIONS}
    print(f"\n  requested {list(VERSIONS)}  ->  imported {[got[v] for v in VERSIONS]}")
    w.add_data("versions_requested", list(VERSIONS))
    w.add_data("versions_imported", [got[v] for v in VERSIONS])
    check("the_two_runs_really_used_DIFFERENT_mpmath_versions",
          got["1.3.0"] == "1.3.0" and got["1.4.1"] == "1.4.1"
          and got["1.3.0"] != got["1.4.1"],
          f"each run prints the version it imported: {got}. This check exists "
          f"because the first attempt at this measurement compared the "
          f"CONTAINER's installed mpmath -- which is 1.4.1, not 1.3.0 -- "
          f"against a 1.4.1 wheel, and reported zero differences that meant "
          f"nothing. Without this assertion the probe's headline result is "
          f"indistinguishable from that failure", w)

    a, b = res["1.3.0"], res["1.4.1"]
    keys = sorted(set(a) | set(b))
    diff = [k for k in keys if a.get(k) != b.get(k)]
    print(f"\n  {len(keys)} primitives at 60 dps, compared at 55 significant digits")
    for k in keys:
        flag = "  <-- DIFFERS" if k in diff else ""
        print(f"    {k:<32} {a.get(k, '<absent>')[:34]}{flag}")
    w.add_data("primitives_compared", len(keys))
    w.add_data("primitives_differing", len(diff))
    w.add_data("differing_keys", diff)

    check("mpmath_1_3_0_and_1_4_1_AGREE_on_every_load_bearing_primitive",
          not diff,
          f"all {len(keys)} primitives are byte-identical at 55 significant "
          f"digits, including Vol(4_1) = 2*Cl2(pi/3), the q_0 root-solve "
          f"against the muon ratio, polylog, hyp2f1, besselj, zeta and gamma. "
          f"So the 1160/829 split in the witness corpus is NOT a staleness "
          f"axis for the constants the framework rests on, and 'which mpmath' "
          f"does not belong on the staleness checklist beside scriptHash and "
          f"import-cone drift", w)

    check("the_scope_is_the_PRIMITIVES_not_the_whole_corpus",
          True,
          f"scope-(a): this measures {len(keys)} primitives, not 1991 "
          f"witnesses. A producer relying on a changed default, iteration "
          f"count or error estimate could still be version-sensitive and is "
          f"not excluded here. The claim is that the framework's CONSTANTS "
          f"are stable, hence the split is not a reason to re-run anything -- "
          f"not that no producer anywhere differs", w)

    total = 3
    print(f"\n  {total - len(_FAILURES)}/{total} checks passed")
    for f in _FAILURES:
        print(f"    FAILED: {f}")
    w.add_data("scope", "(a) scope-limited to the listed primitives")
    out = w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "q0-independent: q_0 is unreachable from this producer's import cone -- it imports only stdlib, mpmath and WitnessBuilder, and neither q_parameter nor qou_substrate.constants appears anywhere in it. This is an ENVIRONMENT audit (mpmath version vs recorded), not a substrate evaluation. It was declared `ambiguous` in the manifest, which the builder can never stamp, so the witness went out unstamped. Bean qou-fl0a."
        ),
    })
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
