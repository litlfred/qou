#!/usr/bin/env python3
# polynomial_q_not_applicable: build-hygiene instrumentation, emits no numeric physics.
"""Localize WHERE a float64 enters an mpmath computation — per producer, by source line.

Owner directive: NO FLOAT64.

`witness_float64_padding_audit.py` says a committed witness *has* fake
precision. `producer_repad_sweep.py` says a producer *regenerates* it. Neither
says **where the float64 came in**, and that is the question that decides the
fix.

## Why this is mechanizable, contrary to the audit's earlier claim

`docs/audits/2026-08-07-producer-repadding-empirical-sweep.md` concluded that
the residual re-padders each need "its own trace from the padded field back to
where float64 enters … genuine per-file work and is not mechanizable." The
*judgment* is indeed per-file (see "What this tool does NOT decide" below).
The *localization* is not: mpmath funnels every float -> mpf conversion through
a single function, so the entry site can be read off directly instead of
reasoned about.

## Mechanism

`is_f64_padded` flags a decimal string whose relative distance to the nearest
binary64 is ~1e-50 — i.e. the value **is** a double's expansion. A value
acquires that property in exactly one way: a Python `float` (53 bits) becomes
an `mpf`, and is later serialized at 50 dps, printing the dyadic tail.

In mpmath (python backend) both routes to that conversion —

    mp.mpf(x)          # explicit promotion          -> ctx_mp_python.py:846
    mpf_value * x      # implicit arithmetic coercion -> ctx_mp_python.py:78

— call `from_float(x)` at the default `prec=53`. A numpy scalar takes a
*separate* path (`from_npfloat`), and `ctx_mp` holds its own binding of
`from_float`, so all of them are patched; intercepting only the obvious one
silently misses every numpy-sourced value.

## Attribution: mpmath's own floats are not the producer's

mpmath uses bare floats internally as convergence heuristics — e.g.
`functions/zeta.py:483`, `if abs(z) >= 1.4`, reached through `clsin`. Walking
out of mpmath to the nearest repo frame attributes that `1.4` to whichever
line called the special function, which is a false positive: the value is
mpmath's, it never reaches a witness, and there is nothing to fix.

Depth cannot separate the two, because `mpf()` is itself an mpmath function:
the innermost frame is mpmath both for `mpf(tf)` written in a producer and for
mpmath's own `1.4`. Classification is lexical instead — is the float a
constant of an mpmath code object on the stack (see `_attribute`). Only
`origin="repo"` sites are candidates; `mpmath-internal` ones are counted and
set aside.

## Exact, not heuristic

A float is only *padding-prone* if it is not exactly representable as a short
decimal. `decimal.Decimal(x)` yields a double's **exact** value, so the test is
a digit count with no tolerance anywhere:

    Decimal(0.5)  -> 0.5                                 1 sig digit  -> harmless
    Decimal(0.1)  -> 0.1000000000000000055511151231…    55 sig digits -> padding-prone

`mpf(0)`, `mpf(1.0)`, `mpf(0.5)` and dyadic tolerances are therefore not
reported, for the same reason the import-time gate does not flag them.

## Two coverage limits — read these before trusting a zero

**Forked workers are invisible.** Instrumentation lives in the process that
installs it. A producer that computes inside `multiprocessing.Pool` forks
children that inherit the patches but keep their own counters, which die with
them — so those conversions are never reported.
`rho_k_co_casimir_extended` does exactly this. `--no-fork` makes such a
producer take its serial path so the work happens where the tracer can see it.
Without that flag, a zero from a forking producer means nothing.

**`--budget` truncates.** Attribution walks the stack per padding-prone
conversion, which on a producer doing ~5e5 of them costs more than the
computation. A budget removes the patches once spent, restoring native speed —
at the price of making sites a **lower bound**. `truncated` records which
reading applies: a site found is real, but none found is not evidence of none.

Both failures are one-directional: they can only hide entry sites, never invent
them. So a non-empty result stands on its own; an empty one is only meaningful
when `truncated` is false and the producer does not fork.

## What this tool does NOT decide

It reports where a float64 entered, never whether that is *wrong*. The
per-file judgment the sweep deferred still stands: a quantity may be
**genuinely** float64-precision (fix: stop promoting it / serialize at true
precision) or **downcast upstream** from a full-precision value (fix: the lost
precision, of which the padding is only a symptom). A `1e-12` comparison
tolerance is reported and should not be "fixed" at all. Sites are evidence for
that judgment, not a verdict.

Usage:
    # from a detached worktree — producers write witnesses
    python3 computations/float64_entry_tracer.py computations/probes/foo.py
    python3 computations/float64_entry_tracer.py --all-repadders --out /tmp/sites.json
"""
from __future__ import annotations

import argparse
import json
import linecache
import os
import runpy
import sys
import traceback
from collections import OrderedDict
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Above this many significant digits in the double's EXACT decimal value, the
# float is not exactly representable and will print a dyadic tail at 50 dps.
# Matches MIN_SIG_FRAC in witness_float64_padding_audit.
EXACT_SIG_LIMIT = 17

MAX_SITES = 4000


def sig_digits(x: float) -> int:
    """Significant digits in a double's *exact* decimal value."""
    if x != x or x in (float("inf"), float("-inf")):
        return 0
    d = Decimal(x).normalize()
    return len(d.as_tuple().digits)


def padding_prone(x) -> bool:
    """True iff this float is not exactly representable as a short decimal.

    Accepts numpy scalars as well as builtin floats — both reach the patched
    conversion functions.
    """
    try:
        v = float(x)
    except (TypeError, ValueError):
        return False
    return v == v and abs(v) != float("inf") and sig_digits(v) > EXACT_SIG_LIMIT


class Tracer:
    """Intercepts float -> mpf conversion and attributes it to a source line."""

    def __init__(self, roots: list[Path], budget: int | None = None):
        self.roots = [str(r) for r in roots]
        self.sites: "OrderedDict[tuple, dict]" = OrderedDict()
        self.total = 0
        self.prone = 0
        self.budget = budget
        self.truncated = False
        self._installed = False

    def _attribute(self, x):
        """Classify a conversion, and report the nearest non-mpmath source line.

        Returns (origin, filename, lineno). `origin` is "mpmath-internal" when
        the float is mpmath's own — its heuristic constants never reach a
        witness and there is nothing to fix.

        Depth cannot decide this. `mpf(x)` *is* an mpmath function, so the
        innermost frame is mpmath for a repo-authored promotion
        (`mpf(tf)`, tf a float) and for an mpmath-authored one
        (`if abs(z) >= 1.4` in functions/zeta.py) alike — an earlier revision
        classified on innermost frame and mislabelled every explicit `mpf(float)`
        in the corpus as internal.

        The discriminator is lexical instead: if the float is a **constant of an
        mpmath code object** on the stack, the literal is written in mpmath's
        source and the value is mpmath's. Otherwise it was handed in by the
        caller, and the first non-mpmath frame is where it entered.
        """
        import mpmath

        mp_dir = os.path.dirname(mpmath.__file__)
        me = __file__
        try:
            xv = float(x)
        except (TypeError, ValueError):
            xv = None
        internal = False
        for fr, lineno in traceback.walk_stack(None):
            fn = fr.f_code.co_filename
            if fn == me:  # the tracer's own frames
                continue
            # mpmath builds its arithmetic dunders by exec'ing a template, so
            # those frames carry the pseudo-filename "<string>" and live
            # outside mpmath's directory. Treat any "<...>" frame as
            # transparent: it is generated code, not a source location anyone
            # can fix.
            if fn.startswith(mp_dir) or (fn.startswith("<") and fn.endswith(">")):
                if xv is not None and not internal:
                    try:
                        internal = any(type(c) is float and c == xv
                                       for c in fr.f_code.co_consts)
                    except Exception:
                        pass
                continue
            if "runpy" in fn:
                continue
            origin = "mpmath-internal" if internal else (
                "repo" if any(fn.startswith(r) for r in self.roots) else "thirdparty")
            return origin, fn, lineno
        return ("mpmath-internal" if internal else "unknown"), "<unknown>", 0

    # Every route a float can take into an mpf. Patching only `from_float`
    # misses numpy scalars entirely.
    _TARGETS = (
        ("mpmath.ctx_mp_python", "from_float"),
        ("mpmath.ctx_mp_python", "from_npfloat"),
        ("mpmath.ctx_mp", "from_float"),
    )

    def _record(self, x):
        self.total += 1
        if not padding_prone(x):
            return
        self.prone += 1
        if len(self.sites) >= MAX_SITES:
            self._spend()
            return
        origin, fn, lineno = self._attribute(x)
        key = (origin, fn, lineno)
        rec = self.sites.get(key)
        if rec is not None:
            rec["count"] += 1
            return
        rel = fn
        for r in self.roots:
            if fn.startswith(r):
                rel = os.path.relpath(fn, r)
                break
        self.sites[key] = {
            "origin": origin,
            "file": rel,
            "line": lineno,
            "source": (linecache.getline(fn, lineno) or "").strip()[:200],
            "count": 1,
            "sample": repr(float(x)),
            "sample_exact": str(Decimal(float(x)))[:70],
        }
        self._spend()

    def _spend(self):
        """Stop tracing once the budget is gone, and take the overhead with it.

        Attribution walks the stack on every padding-prone conversion, which on
        a producer doing ~5e5 of them costs more than the computation. Removing
        the patches (rather than early-returning) restores native speed for the
        rest of the run.

        Sites are then a LOWER BOUND: one found is real, but none found is not
        evidence of none — `truncated` says which reading applies.
        """
        if self.budget is not None and self.prone >= self.budget:
            self.truncated = True
            self.uninstall()

    def install(self):
        import importlib

        self._saved = []
        for modname, attr in self._TARGETS:
            try:
                mod = importlib.import_module(modname)
            except ImportError:
                continue
            orig = getattr(mod, attr, None)
            if orig is None:
                continue
            self._saved.append((mod, attr, orig))

            def make(orig=orig):
                def traced(x, *a, **k):
                    self._record(x)
                    return orig(x, *a, **k)
                return traced

            setattr(mod, attr, make())
        self._installed = True

    def uninstall(self):
        if not self._installed:
            return
        for mod, attr, orig in self._saved:
            setattr(mod, attr, orig)
        self._installed = False

    def report(self) -> dict:
        sites = sorted(self.sites.values(), key=lambda s: -s["count"])
        repo = [s for s in sites if s["origin"] == "repo"]
        return {
            "conversions_total": self.total,
            "conversions_padding_prone": self.prone,
            "distinct_sites": len(sites),
            "truncated": self.truncated,
            "repo_sites": len(repo),
            "mpmath_internal_sites": sum(
                1 for s in sites if s["origin"] == "mpmath-internal"),
            "sites": sites,
        }


def trace_producer(script: Path, repo_root: Path, timeout_note: str = "",
                   budget: int | None = None, no_fork: bool = False) -> dict:
    """Run one producer in-process with instrumentation; never raises.

    A producer that dies before computing anything yields `repo_sites == 0` for
    the same reason a producer that will not start yields no padding: it was
    never measured. Read `status` before reading the site list — "untested" is
    not "clean", exactly as in `producer_repad_sweep.py`.
    """
    tr = Tracer([repo_root], budget=budget)
    forked = None
    if no_fork:
        # Producers branch on cpu_count() to decide whether to Pool. Reporting
        # 1 makes them take the serial path, so the work happens in THIS
        # process where the patches are live. Numerics are unchanged; only the
        # scheduling is.
        import multiprocessing
        forked = multiprocessing.cpu_count
        multiprocessing.cpu_count = lambda: 1
    tr.install()
    argv, cwd, path = list(sys.argv), os.getcwd(), list(sys.path)
    status, err = "ok", ""
    try:
        sys.argv = [str(script)]
        # `python foo.py` puts foo's directory on sys.path; runpy.run_path does
        # not. Without this, sibling-importing producers die on ImportError and
        # look falsely clean.
        sys.path.insert(0, str(script.parent))
        os.chdir(repo_root)
        runpy.run_path(str(script), run_name="__main__")
    except SystemExit as e:
        if e.code not in (0, None):
            status, err = "exit_nonzero", f"exit {e.code}"
    except BaseException as e:  # a producer that dies can still have converted
        status = "raised"
        err = f"{type(e).__name__}: {e}"[:400]
    finally:
        tr.uninstall()
        if forked is not None:
            import multiprocessing
            multiprocessing.cpu_count = forked
        sys.argv, sys.path = argv, path
        os.chdir(cwd)

    rep = tr.report()
    rep.update({"producer": script.name, "status": status, "error": err,
                "no_fork": no_fork})
    if timeout_note:
        rep["note"] = timeout_note
    return rep


def self_test() -> int:
    """Prove the discriminator on cases with known answers.

    Each snippet is compiled under a synthetic filename so it occupies a frame
    of its own. Calling mpmath directly from this module would be traced from
    inside `__file__`, whose frames `_attribute` skips by design — the test
    would then be exercising a path no real producer ever takes.
    """
    import tempfile

    from mpmath import mp

    checks, fails = [], 0
    tmpdir = Path(tempfile.mkdtemp(prefix="f64-selftest-"))

    def run(label, snippet, want_prone, want_origin=None):
        # Write to a real file under a real root, so origin classification is
        # exercised the way it is for an actual producer.
        caller = tmpdir / f"case_{len(checks)}.py"
        caller.write_text(snippet)
        tr = Tracer([tmpdir])
        env = {"mp": mp, "json": json}
        try:
            import numpy as np
            env["np"] = np
        except ImportError:
            pass
        tr.install()
        try:
            exec(compile(snippet, str(caller), "exec"), env)
        finally:
            tr.uninstall()
        rep = tr.report()
        got = tr.prone > 0
        ok = got == want_prone
        if want_origin is not None:
            ok = ok and any(s["origin"] == want_origin for s in rep["sites"])
        checks.append((label, want_prone, got, ok))

    mp.dps = 50
    # Caught: a float64 really does enter, and it is the REPO's float.
    run("mpf(<float literal>)", "mp.mpf(0.1)", True, want_origin="repo")
    run("arithmetic coercion mpf*float", "mp.mpf(1) * 0.1", True, want_origin="repo")
    run("hand-typed AME constant", "mp.mpf(2.22456607)", True, want_origin="repo")
    run("float out of json.loads", 'mp.mpf(json.loads(\'{"v":0.0013}\')["v"])',
        True, want_origin="repo")
    # The binding_factor_f_sequence.py:76 shape — `mpf(tf) - mpf(ta)`, tf/ta
    # floats out of `abs(complex(...))`. Classifying on innermost frame put
    # this in "mpmath-internal", because mpf() is itself an mpmath function.
    run("mpf(<float variable>) — the documented live instance",
        "tf = abs(complex('1.5952397103709324+0j'))\n"
        "ta = abs(complex('1.0+0j'))\n"
        "mp.mpf(tf) - mp.mpf(ta)\n", True, want_origin="repo")
    # Not caught: no information is lost, so nothing to report.
    run("mpf(0.5) exactly representable", "mp.mpf(0.5)", False)
    run("mpf('0.1') string-sourced", "mp.mpf('0.1')", False)
    run("mpf(int)", "mp.mpf(3) + 7", False)
    run("mpf(0)", "mp.mpf(0)", False)

    # numpy scalars take the from_npfloat path, not from_float.
    try:
        import numpy  # noqa: F401
        run("numpy float64 (from_npfloat path)", "mp.mpf(np.float64(0.1))", True)
        run("numpy float32 exact", "mp.mpf(float(np.float32(0.5)))", False)
    except ImportError:
        checks.append(("numpy (skipped — not installed)", None, None, True))

    # mpmath's own heuristic floats must NOT be attributed to repo code:
    # clsin reaches `if abs(z) >= 1.4` in mpmath/functions/zeta.py.
    run("mpmath-internal float not blamed on repo",
        "mp.clsin(2, mp.pi / 3)", True, want_origin="mpmath-internal")

    for label, want, got, ok in checks:
        if not ok:
            fails += 1
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}"
              + ("" if want is None else f"   (want prone={want}, got={got})"))
    print(f"\n{len(checks) - fails}/{len(checks)} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("scripts", nargs="*", help="producer scripts to trace")
    ap.add_argument("--repo-root", default=str(HERE.parent))
    ap.add_argument("--out")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--budget", type=int, default=None,
                    help="stop tracing after N padding-prone conversions; "
                         "sites then are a LOWER BOUND (see `truncated`)")
    ap.add_argument("--no-fork", action="store_true",
                    help="report cpu_count()==1 so a producer takes its serial "
                         "path; worker-side conversions are otherwise invisible")
    ap.add_argument("--self-test", action="store_true",
                    help="verify the discriminator against known cases")
    a = ap.parse_args()

    if a.self_test:
        return self_test()

    repo_root = Path(a.repo_root).resolve()
    if not a.scripts:
        ap.error("give at least one producer script")

    out = []
    for s in a.scripts:
        p = Path(s)
        if not p.is_absolute():
            p = (repo_root / s).resolve()
        if not p.exists():
            out.append({"producer": s, "status": "not_found", "sites": []})
            continue
        rep = trace_producer(p, repo_root, budget=a.budget, no_fork=a.no_fork)
        out.append(rep)
        if not a.quiet:
            print(f"\n=== {rep['producer']}  [{rep['status']}] "
                  f"{rep['conversions_padding_prone']}/{rep['conversions_total']} "
                  f"padding-prone · {rep['repo_sites']} repo site(s), "
                  f"{rep['mpmath_internal_sites']} mpmath-internal"
                  + ("  [TRUNCATED — sites are a lower bound]"
                     if rep.get("truncated") else ""))
            if rep.get("error"):
                print(f"    ! {rep['error']}")
            for st in rep["sites"][:12]:
                mark = {"repo": ">", "mpmath-internal": "~"}.get(st["origin"], "?")
                print(f"  {mark} [{st['origin']}] {st['file']}:{st['line']}  x{st['count']}")
                print(f"      {st['source']}")
                print(f"      sample {st['sample']} = {st['sample_exact']}…")

    if a.out:
        Path(a.out).write_text(json.dumps(out, indent=1))
        if not a.quiet:
            print(f"\n-> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
