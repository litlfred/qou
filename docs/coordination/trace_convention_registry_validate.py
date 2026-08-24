#!/usr/bin/env python3
"""Validate trace-convention-registry.json; guard doc-vs-code convention drift.

The H_3(q) trace-convention registry
(`docs/coordination/trace-convention-registry.md` + its JSON twin
`trace-convention-registry.json`) is the single source of truth for WHICH
Markov trace a given corpus artifact uses. Added 2026-08-08 (bean `qou-n1dj`)
after two defects that a machine check would have caught immediately:

  1. A content block (`mass-theory/h3-markov-wenzl-weights-context.md`)
     stated that the mass computations use the full-Hecke Ocneanu trace
     (convention **C**) while production supplied convention **D**. The two
     differ by 195.8 ppm on beta_Bor; switching to the trace the paper named
     moves m_p by -197 ppm. The disagreement sat unnoticed because nothing
     compared the doc's claim to the code's behaviour.
  2. `markov_peel.tr_M_atomic` was compared against a beta_Bor value as if it
     were a fifth trace convention. It traces a DIFFERENT (11-crossing) braid
     word, so the 6.7 % "convention gap" was a braid-word difference. The
     registry records it as an EXCLUDED tracer so the category error cannot
     be repeated.

Rules (errors unless marked):

  R1  schema/uniqueness: every convention row has a unique single-letter id,
      a name, a `forcing_status` from the enum, a non-empty `implementations`
      list, and a `source`.
  R2  a row with a non-null `value_at_beta_bor` must either name a `verify`
      recipe or explain itself in `value_note`.
  R3  VALUE CHECK (`--check-values`, on by default): recompute each row's
      beta_Bor value from the code named by its `verify` recipe and compare to
      the recorded string at 1e-15 relative. A declared convention that
      disagrees with what the code actually produces is an error. Missing
      imports (sandbox) degrade to a warning, never to a silent pass.
  R4  ENTRY-POINT DECLARATION: every `entry_points` row's function must
      declare its convention in its own source, within `discovery.window_lines`
      of its `def` line, as a case-insensitive `convention <X>` matching the
      registry. Error inside `production_files`, warning elsewhere.
  R5  DISCOVERY: scan computations/ for Borromean trace functions (a
      trace-stem name containing "borromean"). Any such function that is
      neither an `entry_points` row nor `discovery.exempt` must still declare
      a convention. Error inside `production_files`, warning elsewhere.
  R6  DOC-vs-CODE: for each `doc_claims` row, resolve the channel's
      convention for the stated `layer` ("definition" or "production") and
      compare with `names_convention`. A mismatch is an ERROR -- this is
      defect (1) above. A `quote` that no longer occurs in the file is a
      warning (the claim went stale and needs re-review).
  R7  MISLABEL GUARD: no `excluded_tracers` symbol (or alias) may appear in
      any convention row's `implementations`. With `--lint-docs`, also warn on
      any docs/ or content/ line that mentions an excluded symbol together
      with a Borromean reference and the word "convention".
  R8  DISPUTED CHANNELS: a channel whose definitional_convention differs from
      its production_convention must have status "disputed" AND a non-null
      `open_item` carrying a bean and an audit. A disputed channel silently
      recorded as agreed is an error.

      "disputed" answers "which convention is right?". It cannot answer "the
      owner settled it and the code has not moved yet" -- so recording the
      2026-08-15 ruling on `qbeta-decay`, whose production still returns z_C,
      forced a choice between lying about the code and losing the ruling.
      "agreed-migration-pending" (added 2026-08-16, bean qou-cdh1) is that
      third state: it additionally requires a `resolution` block naming the
      ruling and its date, and a `production_convention_target` equal to the
      settled definitional convention.
  R9  EVALUATION (added 2026-08-09, bean qou-wgta item 12): import every entry
      in `evaluators` and CALL IT at q_0, comparing the result to the declared
      convention's own `z_at_q0` / `weights_at_q0` at 1e-40 absolute.

      This is the rule the others could not be. R3 checks two curated
      beta_Bor values; R4 and R5 compare a DOCSTRING STRING to a REGISTRY
      STRING and never look at a number. On 2026-08-09 a stale docstring and
      a stale registry agreed with each other, and this validator reported
      `PASS, 0 errors` while the repo held four convention-C production entry
      points, three convention hybrids (D in one factor, C in another inside
      one function) and a symbolic path serving convention C out of a JSON
      witness cache. Every one of those is invisible to a string comparison
      and none survives an evaluation.

      A failure names the convention the code ACTUALLY implements, not just
      that it disagrees. Entries whose declared convention is C are checked
      just as hard -- the deliberately preserved C reference and the one
      blocked migration must STAY C, and R9 is what notices if they stop.

`--selftest` replays the `regression_cases` rows through the same checkers and
fails if any of them is NOT caught. That is what keeps the guard honest: the
validator must still detect the original defects after future refactors.

Usage:
  python3 docs/coordination/trace_convention_registry_validate.py \
      [--lint-docs] [--strict] [--selftest] [--no-check-values]

Exit 0 unless an error fired (or, with --strict, any warning fired).
CI: warn-only by default, `--strict` to fail, mirroring
computations/lp_dual_witness_validator.py.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
REGISTRY = HERE / "trace-convention-registry.json"

FORCING_STATUS = {
    "forced-given-premise",
    "pinned-by-definition",
    "not-a-z-trace",
    "deprecated",
}
CHANNEL_STATUS = {"agreed", "disputed", "agreed-migration-pending"}
CONV_DECL = re.compile(r"convention[\s:]+([A-D])\b", re.IGNORECASE)
REL_TOL = 1e-15


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _read(rel: str) -> str | None:
    p = REPO / rel
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8", errors="replace")


def _def_window(src: str, symbol: str, window: int) -> str | None:
    """Source slice from `def <symbol>` for `window` lines."""
    lines = src.splitlines()
    pat = re.compile(r"^\s*def\s+%s\s*\(" % re.escape(symbol))
    for i, line in enumerate(lines):
        if pat.match(line):
            return "\n".join(lines[i:i + window])
    return None


def _declared_conventions(window: str) -> set[str]:
    return {m.group(1).upper() for m in CONV_DECL.finditer(window)}


# --------------------------------------------------------------------------
# R1 / R2 -- schema
# --------------------------------------------------------------------------
def check_schema(reg: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    seen: set[str] = set()
    for row in reg.get("conventions", []):
        cid = row.get("id")
        if not cid or not re.fullmatch(r"[A-Z]", str(cid)):
            errors.append("R1 convention id %r is not a single capital letter" % cid)
            continue
        if cid in seen:
            errors.append("R1 duplicate convention id %s" % cid)
        seen.add(cid)
        if not row.get("name"):
            errors.append("R1 %s: missing name" % cid)
        if row.get("forcing_status") not in FORCING_STATUS:
            errors.append("R1 %s: forcing_status %r not in %s"
                          % (cid, row.get("forcing_status"), sorted(FORCING_STATUS)))
        if not row.get("implementations"):
            errors.append("R1 %s: implementations must be non-empty" % cid)
        if not row.get("source"):
            errors.append("R1 %s: missing source" % cid)
        if row.get("forcing_status") == "forced-given-premise" \
                and not row.get("forcing_premise"):
            errors.append("R1 %s: forcing_status 'forced-given-premise' requires "
                          "forcing_premise naming the unmet premise" % cid)
        if row.get("value_at_beta_bor") is not None:
            if not row.get("verify") and not row.get("value_note"):
                errors.append("R2 %s: a recorded beta_Bor value needs either a "
                              "`verify` recipe or a `value_note`" % cid)
        else:
            if not row.get("value_note"):
                warnings.append("R2 %s: null beta_Bor value with no value_note" % cid)
    if not seen:
        errors.append("R1 registry has no convention rows")
    return errors, warnings


# --------------------------------------------------------------------------
# R3 -- live value check
# --------------------------------------------------------------------------
def _verify_trM_borromean():
    """Convention D straight from the production closed form."""
    sys.path.insert(0, str(REPO / "computations"))
    import mpmath as mp  # noqa: PLC0415
    from m_p_substrate_identity_50dps import trM_borromean  # noqa: PLC0415
    # Q_MP, not `mpf(str(Q))`: the f64 constant is ~16 significant digits, so
    # the old form laundered it and then computed to 50 dps on top of a
    # 16-digit input — precision theatre. The OUTER mpf(str(...)) is kept: it
    # normalises whatever numeric type trM_borromean returns.
    from q_parameter import Q_MP as Q0  # noqa: PLC0415
    with mp.workdps(50):
        return {"D": mp.mpf(str(trM_borromean(Q0)))}


def _verify_probe_writhe0():
    """Conventions C and D from the 3x3 Ocneanu solve (registry's own probe)."""
    for sub in ("", "markov", "substrate", "hecke"):
        sys.path.insert(0, str(REPO / "computations" / sub))
    import sympy as sp  # noqa: PLC0415
    from hecke_character_symbolic import q_character_on_braid_word  # noqa: PLC0415
    from q_parameter import Q as Q0  # noqa: PLC0415

    qs, z = sp.symbols("q", positive=True), sp.symbols("z")
    q0 = sp.Float(str(Q0), 50)
    parts = [(3,), (2, 1), (1, 1, 1)]
    classes = [[], [(0, "sigma")], [(0, "sigma"), (1, "sigma")]]
    targets = [sp.Integer(1), z, z ** 2]
    rows = [[sp.cancel(sp.sympify(q_character_on_braid_word(lam, w, qs)))
             for lam in parts] for w in classes]
    sol = sp.Matrix(rows).solve(sp.Matrix(targets))
    y = {lam: sp.cancel(sol[i]) for i, lam in enumerate(parts)}
    bor = [(0, "sigma"), (1, "sigma_inv")] * 3
    chi = {lam: sp.cancel(sp.sympify(q_character_on_braid_word(lam, bor, qs)))
           for lam in parts}
    out = {}
    for cid, zval in (("C", 1 / (sp.sqrt(qs) + 1 / sp.sqrt(qs))),
                      ("D", qs ** 3 / (qs ** 2 + 1))):
        tr = sp.cancel(sum(y[lam].subs(z, zval) * chi[lam] for lam in parts))
        out[cid] = sp.N(tr.subs(qs, q0), 40)
    return out


VERIFIERS = {
    "trM_borromean": _verify_trM_borromean,
    "probe_writhe0": _verify_probe_writhe0,
}


def check_values(reg: dict) -> tuple[list[str], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    notes: list[str] = []
    wanted: dict[str, set[str]] = {}
    for row in reg.get("conventions", []):
        recipe = row.get("verify")
        if recipe and row.get("value_at_beta_bor") is not None:
            wanted.setdefault(recipe, set()).add(row["id"])
    for recipe, ids in sorted(wanted.items()):
        fn = VERIFIERS.get(recipe)
        if fn is None:
            errors.append("R3 unknown verify recipe %r (rows %s)"
                          % (recipe, sorted(ids)))
            continue
        try:
            got = fn()
        except Exception as exc:  # noqa: BLE001 -- sandbox tolerance, never silent
            warnings.append("R3 verify recipe %r could not run (%s: %s); "
                            "values NOT confirmed"
                            % (recipe, type(exc).__name__, exc))
            continue
        for cid in sorted(ids):
            row = next(r for r in reg["conventions"] if r["id"] == cid)
            if cid not in got:
                warnings.append("R3 recipe %r produced no value for %s"
                                % (recipe, cid))
                continue
            rec, act = row["value_at_beta_bor"], got[cid]
            try:
                import mpmath as mp  # noqa: PLC0415
                with mp.workdps(50):
                    a, b = mp.mpf(str(rec)), mp.mpf(str(act))
                    rel = abs(a - b) / abs(b) if b != 0 else abs(a - b)
            except Exception as exc:  # noqa: BLE001
                warnings.append("R3 %s: comparison failed (%s)" % (cid, exc))
                continue
            if rel > REL_TOL:
                errors.append(
                    "R3 %s: registry records beta_Bor = %s but %s produces %s "
                    "(rel %.3e > %.0e) -- the declared convention disagrees "
                    "with the code" % (cid, rec, recipe, mp.nstr(b, 20),
                                       float(rel), REL_TOL))
            else:
                notes.append("R3 %s: beta_Bor value CONFIRMED against %s "
                             "(rel %.2e <= %.0e)"
                             % (cid, recipe, float(rel), REL_TOL))
    return errors, warnings, notes


# --------------------------------------------------------------------------
# R4 / R5 -- declaration
# --------------------------------------------------------------------------
def check_declarations(reg: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    prod = set(reg.get("production_files", []))
    disc = reg.get("discovery", {})
    window = int(disc.get("window_lines", 45))
    exempt = {e["file"] for e in disc.get("exempt", [])}
    covered: set[tuple[str, str]] = set()

    # R4 -- the curated entry points
    for ep in reg.get("entry_points", []):
        f, sym, conv = ep["file"], ep["symbol"], ep["convention"]
        covered.add((f, sym))
        src = _read(f)
        sink = errors if f in prod else warnings
        if src is None:
            errors.append("R4 %s: file not found" % f)
            continue
        win = _def_window(src, sym, window)
        if win is None:
            errors.append("R4 %s::%s: no `def %s(` found" % (f, sym, sym))
            continue
        decl = _declared_conventions(win)
        if not decl:
            sink.append("R4 %s::%s traces a braid without declaring its "
                        "convention (expected 'convention %s' in the first %d "
                        "lines of the def)" % (f, sym, conv, window))
        elif conv not in decl:
            errors.append("R4 %s::%s declares convention(s) %s but the registry "
                          "records %s" % (f, sym, sorted(decl), conv))

    # R5 -- discovery over every Borromean tracer under `discovery.roots`.
    #
    # WIDENED 2026-08-09 (bean qou-wgta). This used to be
    # `(REPO / "computations").rglob("*.py")` and nothing else, which
    # structurally excluded tools/ (the Rust engine and its nine language
    # bindings), qou-mass/ (a shipped package carrying a verbatim
    # pre-excision copy of y_lambda_at) and content/**. Those are exactly
    # where the 2026-08-09 audit found the missed convention-C sites.
    pat = re.compile(disc.get("def_pattern", r"^def\s+(\w+)\s*\("), re.MULTILINE)
    need = (disc.get("name_must_contain") or "borromean").lower()
    roots = disc.get("roots") or ["computations"]
    seen: set[tuple[str, str]] = set()
    for root_name in roots:
        root = REPO / root_name
        if not root.exists():
            warnings.append("R5 discovery root %r does not exist" % root_name)
            continue
        for py in sorted(root.rglob("*.py")):
            rel = py.relative_to(REPO).as_posix()
            slashed = "/" + rel
            if ("/_deprecated/" in slashed or "/archive/" in slashed
                    or "/node_modules/" in slashed or "/target/" in slashed
                    or rel in exempt):
                continue
            src = py.read_text(encoding="utf-8", errors="replace")
            for m in pat.finditer(src):
                sym = m.group(1)
                if need not in sym.lower():
                    continue
                if (rel, sym) in covered or (rel, sym) in seen:
                    continue
                seen.add((rel, sym))
                win = _def_window(src, sym, window)
                if win is None or not _declared_conventions(win):
                    sink = errors if rel in prod else warnings
                    sink.append("R5 %s::%s computes a Borromean Markov trace "
                                "without declaring its convention" % (rel, sym))
    return errors, warnings


# --------------------------------------------------------------------------
# R9 -- THE NUMERIC CHECK: evaluate every registered implementation at q0
# --------------------------------------------------------------------------
# R3 checks two curated beta_Bor values. R4/R5 compare a DOCSTRING STRING to a
# REGISTRY STRING. Neither ever calls the implementation and compares the
# NUMBER, and on 2026-08-09 that gap let a stale docstring and a stale registry
# agree with each other while four production entry points, three convention
# hybrids and a cache-served convention-C symbolic path all disagreed with
# both -- and the validator printed PASS.
#
# R9 imports each entry in `evaluators` and calls it at q0, comparing to the
# declared convention's own `z_at_q0` / `weights_at_q0`. It cannot be defeated
# by a stale docstring, a stale registry row, a vendored copy, or a witness
# cache, because none of those change what the code returns.

_N3_PARTITIONS = ((3,), (2, 1), (1, 1, 1))


# Working precision for R9. Must exceed the 50 significant digits the registry
# records, or `mp.mpf(Q_50_DIGIT_STR)` silently truncates and every comparison
# fails at ~1e-17 -- which is exactly what happened on the first run of this
# rule, at mpmath's default dps of 15.
_R9_DPS = 70


def _q0_mpf():
    import mpmath as mp  # noqa: PLC0415
    for sub in ("substrate", ""):
        cand = REPO / "computations" / sub
        if str(cand) not in sys.path:
            sys.path.insert(0, str(cand))
    from q_parameter import Q_50_DIGIT_STR  # noqa: PLC0415
    with mp.workdps(_R9_DPS):
        return +mp.mpf(Q_50_DIGIT_STR)   # unary + pins the precision


def _import_for(entry):
    import importlib  # noqa: PLC0415
    for rel in entry.get("sys_path", []):
        pth = str(REPO / rel)
        if pth not in sys.path:
            sys.path.insert(0, pth)
    return importlib.import_module(entry["module"])


def _eval_z(entry, mod, q0):
    """Return the entry's z at q0 as an mpf."""
    import mpmath as mp  # noqa: PLC0415
    kind = entry["kind"]
    obj = mod
    for part in entry["symbol"].split("."):
        obj = getattr(obj, part)
    if kind == "callable_q":
        return mp.mpf(str(obj(q0)))
    if kind == "module_attr_float":
        return mp.mpf(str(obj))
    if kind == "sympy_expr_q":
        import sympy as sp  # noqa: PLC0415
        free = [x for x in obj.free_symbols]
        if len(free) != 1:
            raise ValueError("expected exactly one free symbol, got %s" % free)
        return mp.mpf(str(sp.N(obj.subs(free[0], sp.Float(mp.nstr(q0, 60), 60)), 55)))
    # --- function-level kinds -------------------------------------------
    # R9 could previously reach only MODULE ATTRIBUTES. Anything computed
    # inside a function was invisible to it, and that is exactly where
    # pyhecke.gram's 50-dps mpmath path sat: `z` (module attr) is convention
    # D and was checked; `z_mp()` and `tr_m_mp()` return convention C and
    # were not. A convention that only exists at call time is still a
    # convention, and the high-precision path is the one you reach for when
    # the answer matters.
    if kind == "callable_no_arg":
        return mp.mpf(str(obj()))
    if kind == "callable_index":
        idx = entry.get("index")
        if idx is None:
            raise ValueError("callable_index requires an `index`")
        return mp.mpf(str(obj()[idx]))
    if kind == "callable_q_index":
        idx = entry.get("index")
        if idx is None:
            raise ValueError("callable_q_index requires an `index`")
        return mp.mpf(str(obj(q0)[idx]))
    raise ValueError("unknown z kind %r" % kind)


def _eval_weights(entry, mod, q0):
    """Return {partition: mpf} at n = 3."""
    import mpmath as mp  # noqa: PLC0415
    kind = entry["kind"]
    fn = getattr(mod, entry["symbol"])
    if kind == "weights_n_q":
        raw = fn(3, q0)
    elif kind == "weights_n_sympy":
        import sympy as sp  # noqa: PLC0415
        q_sub = sp.Float(mp.nstr(q0, 60), 60)
        raw = {k: sp.N(sp.cancel(v).subs(
            [(x, q_sub) for x in sp.cancel(v).free_symbols], simultaneous=True), 55)
            for k, v in fn(3).items()}
    elif kind == "weights_per_partition_q":
        raw = {lam: fn(list(lam), q0, dps=50) for lam in _N3_PARTITIONS}
    else:
        raise ValueError("unknown weights kind %r" % kind)
    return {tuple(k): mp.mpf(str(v)) for k, v in raw.items()}


def check_evaluated(reg: dict) -> tuple[list[str], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    notes: list[str] = []
    ev = reg.get("evaluators")
    if not ev:
        warnings.append("R9 no `evaluators` block in the registry -- nothing is "
                        "numerically checked; R4/R5 are string comparisons only")
        return errors, warnings, notes
    try:
        import mpmath as mp  # noqa: PLC0415
        mp.mp.dps = max(mp.mp.dps, _R9_DPS)
        q0 = _q0_mpf()
    except Exception as exc:  # noqa: BLE001
        warnings.append("R9 could not obtain q0 (%s: %s); NOTHING numerically "
                        "checked" % (type(exc).__name__, exc))
        return errors, warnings, notes

    by_id = {c["id"]: c for c in reg.get("conventions", [])}
    default_tol = mp.mpf(str(ev.get("abs_tol", "1e-40")))

    with mp.workdps(_R9_DPS):
        for entry in ev.get("z", []):
            cid = entry["convention"]
            want_s = (by_id.get(cid) or {}).get("z_at_q0")
            if want_s is None:
                errors.append("R9 %s: convention %s records no z_at_q0"
                              % (entry["id"], cid))
                continue
            tol = mp.mpf(str(entry.get("abs_tol", default_tol)))
            try:
                got = _eval_z(entry, _import_for(entry), q0)
            except Exception as exc:  # noqa: BLE001
                warnings.append("R9 %s: could not evaluate (%s: %s); NOT confirmed"
                                % (entry["id"], type(exc).__name__, exc))
                continue
            want = mp.mpf(want_s)
            d = abs(got - want)
            if d > tol:
                other = [k for k, c in by_id.items()
                         if c.get("z_at_q0") is not None
                         and abs(got - mp.mpf(c["z_at_q0"])) <= tol]
                hint = (" -- it is actually convention %s" % other[0]) if other else ""
                errors.append(
                    "R9 %s: registry says convention %s (z = %s) but the CODE "
                    "returns %s (|d| = %s > %s)%s"
                    % (entry["id"], cid, want_s, mp.nstr(got, 25),
                       mp.nstr(d, 4), mp.nstr(tol, 2), hint))
            else:
                notes.append("R9 %s: z CONFIRMED convention %s by evaluation "
                             "(|d| = %s)" % (entry["id"], cid, mp.nstr(d, 4)))

        # --- R10: one module, one convention ------------------------------
        # R9 checks each entry against the registry INDEPENDENTLY, so a module
        # whose symbols disagree with EACH OTHER passes it entry by entry.
        # pyhecke.gram does exactly that: `z` is D, `z_mp()` and `tr_m_mp()`
        # are C, and every one of them is correctly registered -- R9 confirms
        # all three and says nothing is wrong.
        #
        # A caller does not import a registry entry, it imports a module, and
        # `from pyhecke.gram import z` versus `gram.z_mp()` differ by 18.5%
        # with nothing at the call site to suggest it. So the divergence is
        # the defect even when both halves are accurately recorded.
        #
        # Waivable, because a module MAY legitimately export a preserved
        # historical constant beside its production one -- that is what
        # schur_principal_mpmath does, and it says so in the symbol name.
        # The waiver has to name the module, so the exception is a decision
        # somebody made rather than a silence.
        waived = set(reg.get("intra_module_split_waivers", []))
        by_module: dict = {}
        for entry in ev.get("z", []):
            by_module.setdefault(entry.get("module", "?"), []).append(entry)
        for mod_name, entries in sorted(by_module.items()):
            convs = {e["convention"] for e in entries}
            if len(convs) < 2:
                continue
            detail = ", ".join(
                "%s=%s" % (e["id"], e["convention"])
                for e in sorted(entries, key=lambda x: x["id"]))
            msg = ("R10 %s exports MORE THAN ONE convention (%s): %s"
                   % (mod_name, "/".join(sorted(convs)), detail))
            if mod_name in waived:
                # A waiver downgrades to WARNING, never to a note. A note is
                # read once and then scrolled past; a warning is counted in
                # the summary line, so a known split stays visible for as long
                # as it is open. Waiving is for "tracked and not blocking",
                # not for "resolved".
                warnings.append(msg + " -- WAIVED in intra_module_split_waivers "
                                "(open defect, not an approved design)")
            else:
                errors.append(
                    msg + " -- a caller imports a module, not a registry entry, "
                    "so two conventions behind one import is a defect even when "
                    "both are accurately recorded. Fix the module, or waive it "
                    "by name in `intra_module_split_waivers`.")

        # --- R11: derived quantities must match their own z ----------------
        # R9 checks the Markov parameter itself. Everything DERIVED from it --
        # tr_M(sigma_1^2) = h*z+1, the H_2 weight (q*z+1)/(q^2+1), the entries
        # of the TR_M vector -- gets written out in closed form, and a closed
        # form derived under one convention keeps working, silently, after z
        # moves. `scan_closed_forms` hunts those statically, but it keys on the
        # BINDING NAME (trM, W2, y_lambda, ...), and a name-keyed detector is
        # exactly what has been blind three times over in this excision:
        # missed the half-argument spelling, missed returns, missed the
        # reciprocal form. A numeric identity cannot be evaded by spelling.
        #
        # It has a track record. TR_M[5] was z^3 rather than h*z^2+z until
        # docs/audits/2026-05-19-trm5-markov-bug.md, and main carries the
        # commit "flip trace_weights to h*z^2 + z -- Rust and Python finally
        # agree". This is that check, at 1e-40, keyed off the registry.
        _IDENTITIES = {
            "z": lambda z, h, q: z,
            "z^2": lambda z, h, q: z ** 2,
            "z^3": lambda z, h, q: z ** 3,
            "h*z+1": lambda z, h, q: h * z + 1,
            "h*z^2+z": lambda z, h, q: h * z * z + z,
            "z+h*z^2": lambda z, h, q: z + h * z * z,
            "(q*z+1)/(q^2+1)": lambda z, h, q: (q * z + 1) / (q ** 2 + 1),
        }
        for entry in ev.get("derived", []):
            cid = entry["convention"]
            ident = entry.get("identity")
            z_s = (by_id.get(cid) or {}).get("z_at_q0")
            if z_s is None or ident not in _IDENTITIES:
                errors.append("R11 %s: convention %s has no z_at_q0, or unknown "
                              "identity %r" % (entry["id"], cid, ident))
                continue
            tol = mp.mpf(str(entry.get("abs_tol", default_tol)))
            try:
                got = _eval_z(entry, _import_for(entry), q0)
            except Exception as exc:  # noqa: BLE001
                warnings.append("R11 %s: could not evaluate (%s: %s); NOT confirmed"
                                % (entry["id"], type(exc).__name__, exc))
                continue
            zc = mp.mpf(z_s)
            want = _IDENTITIES[ident](zc, q0 - 1 / q0, q0)
            d = abs(got - want)
            if d > tol:
                errors.append(
                    "R11 %s: should equal %s = %s for convention %s, but the CODE "
                    "returns %s (|d| = %s > %s). The derived form has drifted from "
                    "the z it is derived from."
                    % (entry["id"], ident, mp.nstr(want, 25), cid,
                       mp.nstr(got, 25), mp.nstr(d, 4), mp.nstr(tol, 2)))
            else:
                notes.append("R11 %s: CONFIRMED %s under convention %s (|d| = %s)"
                             % (entry["id"], ident, cid, mp.nstr(d, 4)))

        for entry in ev.get("weights_n3", []):
            cid = entry["convention"]
            want_map = (by_id.get(cid) or {}).get("weights_at_q0")
            if not want_map:
                errors.append("R9 %s: convention %s records no weights_at_q0"
                              % (entry["id"], cid))
                continue
            tol = mp.mpf(str(entry.get("abs_tol", default_tol)))
            try:
                got = _eval_weights(entry, _import_for(entry), q0)
            except Exception as exc:  # noqa: BLE001
                warnings.append("R9 %s: could not evaluate (%s: %s); NOT confirmed"
                                % (entry["id"], type(exc).__name__, exc))
                continue
            keymap = {(3,): "(3)", (2, 1): "(2,1)", (1, 1, 1): "(1^3)"}
            worst = mp.mpf(0)
            bad = []
            for lam, label in keymap.items():
                if label not in want_map:
                    continue
                w = mp.mpf(want_map[label])
                g = got.get(lam)
                if g is None:
                    bad.append("%s missing" % label)
                    continue
                d = abs(g - w)
                worst = max(worst, d)
                if d > tol:
                    bad.append("%s: want %s got %s (|d| = %s)"
                               % (label, want_map[label], mp.nstr(g, 25),
                                  mp.nstr(d, 4)))
            if bad:
                errors.append("R9 %s: registry says convention %s but the CODE "
                              "disagrees -- %s" % (entry["id"], cid, "; ".join(bad)))
            else:
                notes.append("R9 %s: y_lambda(3) CONFIRMED convention %s by "
                             "evaluation (worst |d| = %s)"
                             % (entry["id"], cid, mp.nstr(worst, 4)))
    return errors, warnings, notes


# --------------------------------------------------------------------------
# R6 -- doc vs code
# --------------------------------------------------------------------------
def _channel_convention(reg: dict, channel_id: str, layer: str):
    for ch in reg.get("channels", []):
        if ch["id"] == channel_id:
            key = ("definitional_convention" if layer == "definition"
                   else "production_convention")
            return ch.get(key), ch
    return None, None


def check_doc_claims(reg: dict, claims=None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    for claim in (claims if claims is not None else reg.get("doc_claims", [])):
        f = claim["file"]
        layer = claim.get("layer", "production")
        if layer not in ("definition", "production"):
            errors.append("R6 %s: layer %r must be 'definition' or 'production'"
                          % (f, layer))
            continue
        want, ch = _channel_convention(reg, claim["about_channel"], layer)
        if ch is None:
            errors.append("R6 %s: unknown channel %r" % (f, claim["about_channel"]))
            continue
        named = claim.get("names_convention")
        if named != want:
            errors.append(
                "R6 %s names convention %s for the %s %s layer, but the "
                "registry records %s (%s)"
                % (f, named, claim["about_channel"], layer, want,
                   ch.get("production_source" if layer == "production"
                          else "definitional_source", "")[:120]))
        src = _read(f)
        if src is None:
            errors.append("R6 %s: file not found" % f)
        elif claim.get("quote") and claim["quote"] not in src:
            warnings.append("R6 %s: the recorded quote is no longer present -- "
                            "the claim went stale and needs re-review "
                            "(quote: %r)" % (f, claim["quote"][:70]))
    return errors, warnings


# --------------------------------------------------------------------------
# R7 -- mislabel guard
# --------------------------------------------------------------------------
def check_excluded(reg: dict, lint_docs: bool, conventions=None):
    errors: list[str] = []
    warnings: list[str] = []
    excl = reg.get("excluded_tracers", [])
    symbols: list[tuple[str, str]] = []
    for ex in excl:
        for s in [ex["symbol"]] + list(ex.get("aliases") or []):
            symbols.append((s, ex["symbol"]))
    for row in (conventions if conventions is not None
                else reg.get("conventions", [])):
        blob = " ".join(row.get("implementations") or [])
        for sym, owner in symbols:
            if re.search(r"\b%s\b" % re.escape(sym), blob):
                errors.append(
                    "R7 convention %s lists the excluded tracer %s: %s"
                    % (row.get("id"), sym,
                       next(e["reason"] for e in excl
                            if e["symbol"] == owner)[:160]))
    if lint_docs:
        bor = re.compile(r"borromean|beta_Bor|β_\{?\\?mathrm\{Bor|β_Bor",
                         re.IGNORECASE)
        for base in ("docs", "content"):
            root = REPO / base
            if not root.exists():
                continue
            for md in root.rglob("*.md"):
                rel = md.relative_to(REPO).as_posix()
                for n, line in enumerate(
                        md.read_text(encoding="utf-8", errors="replace")
                        .splitlines(), 1):
                    if "convention" not in line.lower() or not bor.search(line):
                        continue
                    for sym, _owner in symbols:
                        if re.search(r"\b%s\b" % re.escape(sym), line):
                            warnings.append(
                                "R7 %s:%d mentions the excluded tracer %s "
                                "alongside a Borromean convention claim -- it "
                                "traces a different braid word, so it is not a "
                                "convention" % (rel, n, sym))
    return errors, warnings


# --------------------------------------------------------------------------
# R8 -- disputed channels
# --------------------------------------------------------------------------
def check_channels(reg: dict, channels=None) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    ids = {r["id"] for r in reg.get("conventions", [])}
    for ch in (channels if channels is not None else reg.get("channels", [])):
        d, p = ch.get("definitional_convention"), ch.get("production_convention")
        for label, v in (("definitional", d), ("production", p)):
            if v is not None and v not in ids:
                errors.append("R8 channel %s: %s_convention %r is not a "
                              "registry row" % (ch["id"], label, v))
        st = ch.get("status")
        if st not in CHANNEL_STATUS:
            errors.append("R8 channel %s: status %r not in %s"
                          % (ch["id"], st, sorted(CHANNEL_STATUS)))
            continue
        if d != p:
            if st not in ("disputed", "agreed-migration-pending"):
                errors.append("R8 channel %s: definitional %s != production %s "
                              "but status is %r -- must be 'disputed' or "
                              "'agreed-migration-pending'"
                              % (ch["id"], d, p, st))
            oi = ch.get("open_item") or {}
            if not oi.get("bean") or not oi.get("audit"):
                errors.append("R8 channel %s is disputed (%s vs %s) but has no "
                              "open_item with a bean and an audit -- a "
                              "convention disagreement may not be recorded "
                              "silently" % (ch["id"], d, p))
            # 'agreed-migration-pending' separates the two questions R8
            # originally ran together: WHICH convention is right (settled by an
            # owner ruling) and HAS THE CODE MOVED (not yet). The old vocabulary
            # could express only "disputed", so recording a settlement forced a
            # choice between lying about the code (production := D while the
            # code returns z_C) and losing the ruling. It demands strictly MORE
            # evidence than 'disputed' -- which required a bean and an audit and
            # nothing else -- so it cannot be used to quiet a live dispute.
            if st == "agreed-migration-pending":
                res = ch.get("resolution") or {}
                for field in ("ruling", "date"):
                    if not res.get(field):
                        errors.append(
                            "R8 channel %s is 'agreed-migration-pending' but "
                            "its resolution block has no %r -- a settlement "
                            "must name the authority that settled it"
                            % (ch["id"], field))
                tgt = ch.get("production_convention_target")
                if tgt != d:
                    errors.append(
                        "R8 channel %s is 'agreed-migration-pending' with "
                        "production_convention_target %r, which does not match "
                        "the settled definitional_convention %r -- the target "
                        "of the migration IS the settled convention"
                        % (ch["id"], tgt, d))
        elif st == "disputed":
            warnings.append("R8 channel %s: status 'disputed' but the two "
                            "conventions agree (%s)" % (ch["id"], d))
    return errors, warnings


# --------------------------------------------------------------------------
# --selftest -- the regression cases must still be caught
# --------------------------------------------------------------------------
def selftest(reg: dict) -> tuple[list[str], list[str]]:
    """Replay `regression_cases` and fail if any is NOT detected."""
    errors: list[str] = []
    notes: list[str] = []
    for rc in reg.get("regression_cases", []):
        rid, want = rc["id"], rc["must_error_with"].lower()
        fired: list[str] = []
        if "doc_claim" in rc:
            fired, _ = check_doc_claims(reg, claims=[rc["doc_claim"]])
        elif "convention_row" in rc:
            fired, _ = check_excluded(reg, False,
                                      conventions=[rc["convention_row"]])
        elif "channel" in rc:
            fired, _ = check_channels(reg, channels=[rc["channel"]])
        else:
            errors.append("selftest %s: unrecognised regression-case shape" % rid)
            continue
        hit = [e for e in fired if want in e.lower()]
        if hit:
            notes.append("selftest %s CAUGHT: %s" % (rid, hit[0]))
        else:
            errors.append("selftest %s NOT caught -- the guard has regressed. "
                          "Expected an error mentioning %r; got %s"
                          % (rid, rc["must_error_with"], fired or "nothing"))
    return errors, notes


# --------------------------------------------------------------------------
def main() -> int:
    strict = "--strict" in sys.argv
    lint_docs = "--lint-docs" in sys.argv
    do_selftest = "--selftest" in sys.argv
    do_values = "--no-check-values" not in sys.argv

    if not REGISTRY.exists():
        print("ERROR: registry not found: %s" % REGISTRY)
        return 1
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if reg.get("schema") != "trace-convention-registry/v1":
        print("ERROR: unexpected schema %r" % reg.get("schema"))
        return 1

    errors: list[str] = []
    warnings: list[str] = []
    notes: list[str] = []
    for fn in (check_schema, check_channels):
        e, w = fn(reg)
        errors += e
        warnings += w
    e, w = check_doc_claims(reg)
    errors += e
    warnings += w
    e, w = check_declarations(reg)
    errors += e
    warnings += w
    e, w = check_excluded(reg, lint_docs)
    errors += e
    warnings += w
    if do_values:
        e, w, n = check_values(reg)
        errors += e
        warnings += w
        notes += n
        e, w, n = check_evaluated(reg)
        errors += e
        warnings += w
        notes += n
    else:
        warnings.append("R3 value check skipped (--no-check-values)")
        warnings.append("R9 numeric evaluation skipped (--no-check-values) -- "
                        "only string comparisons ran")
    if do_selftest:
        e, n = selftest(reg)
        errors += e
        notes += n

    print("trace-convention registry: %d convention(s), %d channel(s), "
          "%d entry point(s), %d doc claim(s), %d excluded tracer(s)"
          % (len(reg.get("conventions", [])), len(reg.get("channels", [])),
             len(reg.get("entry_points", [])), len(reg.get("doc_claims", [])),
             len(reg.get("excluded_tracers", []))))
    for n in notes:
        print("  note    : %s" % n)
    for w in warnings:
        print("  WARNING : %s" % w)
    for e in errors:
        print("  ERROR   : %s" % e)
    ok = not errors and not (strict and warnings)
    print("%s  (%d error(s), %d warning(s)%s)"
          % ("PASS" if ok else "FAIL", len(errors), len(warnings),
             ", strict" if strict else ""))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
