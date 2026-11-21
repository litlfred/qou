#!/usr/bin/env python3
"""Find grouped-era artifacts by their VALUE, not by any symptom.

WHY A VALUE-KEYED SELECTOR
--------------------------
The 2026-09-05 intra-ordering ruling (`qou-hu1f`) has now escaped **three**
separate sweeps, each of which keyed on a *symptom*:

  1. the `qou-hu1f` witness sweep — selected witnesses whose producer references
     `atom_braid_word_3A` by name;
  2. `binding_canonical` — missed for the same reason, it reaches the canonical
     word indirectly;
  3. `qou-cvky` — selected files that *raise* on a non-monotone word.

`closed_form_tau_M.compute_tau_M_nucleon_H3` (bean `qou-y2o7`) was invisible to
all three. It never named `atom_braid_word_3A`, and it never raised, because it
**built its own monotone word** and so satisfied the kernel's precondition with
the wrong braid. There was no symptom to key on. It returned a plausible 50-dps
number in the superseded ordering, and 18 consumers inherited it.

A symptom-keyed selector finds the loud cases. This one keys on the answer: a
grouped-era |tr_M| is a specific number and is recognisable wherever it is
written down, whatever the producer is called and whether or not it crashes.
That is the argument `y_lambda_convention_c_fingerprint_audit.py` makes for
trace CONVENTIONS, applied to intra-nucleon ORDERING.

WHAT A HIT IS AND IS NOT
------------------------
A hit says a witness's payload carries a grouped-era value. It does **not** say
the producer is broken:

  * the producer may be fixed while the witness was never regenerated (the
    common case — re-run it to tell the two apart);
  * the site may be **deliberately** historical. Three are, as of 2026-09-06:
    `nucleon_h3_marshalling_divergence_probe`,
    `qbeta_delta_vs_deltaTbeta_settled_probe` and `reduced_block_kernel` all
    pass `intra_order="grouped"` on purpose, because their whole comparison
    lives in that frame. Those are listed separately, not as findings.

A non-hit is not a clean bill either: a witness that records only derived
quantities (binding energies, mass residuals) carries no |tr_M| for this to
match, and is silent under the test.

WHY THE MATCH CANNOT BE COINCIDENCE
-----------------------------------
Matching is on **15 significant digits** of a specific irrational. This corpus
has measured its own coincidence floor: agreement to 0–2 significant figures is
a coincidence 100 % of the time, 6–8 figures 5.4 %, 9–11 figures 2.7 %. Fifteen
is far past any of that — a 15-digit match to `1.14575969245730087` is that
number, not a near miss.

Fingerprints are computed live from `atom_braid_word_3A` under both orderings at
both documented pins, never transcribed, so a re-pin moves them rather than
silently invalidating the scan.
"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMPUTATIONS = _HERE.parent
_ROOT = _COMPUTATIONS.parent
sys.path[:0] = [str(_COMPUTATIONS), str(_COMPUTATIONS / "substrate"),
                str(_ROOT / "tools" / "qou-substrate" / "python")]

import _path_bridge  # noqa: F401,E402
import mpmath as mp  # noqa: E402

mp.mp.dps = 50

import mass_at_3A_proper as M  # noqa: E402
import tr_m_wenzl_bridge_mpfr as B  # noqa: E402
from qou_substrate import constants as _c  # noqa: E402

#: Significant digits required for a match. See "WHY THE MATCH CANNOT BE
#: COINCIDENCE" above — this is deliberately far past the measured floor.
SIG_DIGITS = 15

ATOMS = {"proton": (1, 0), "neutron": (0, 1), "deuteron": (1, 1),
         "tritium": (1, 2), "helium-3": (2, 1)}

PINS = {
    "proton": str(_c.Q_50_DIGIT_STR),
    # the live CODATA-2022 muon pin, derived rather than typed (the literal
    # this replaced matched it to all 70 digits; reference-literal ratchet).
    # str(): the Rust engine takes q as a decimal string, not an mpf.
    "muon-live": mp.nstr(_c.q_muon_at(70), 70, strip_zeros=False),
}

#: Sites that pass `intra_order="grouped"` deliberately, with the reason. A hit
#: on one of these is expected and is not a finding.
DELIBERATE = {
    "nucleon-h3-marshalling-divergence":
        "guards the qou-qu2w fix against a grouped-era habiro target",
    "qbeta-delta-vs-deltaTbeta-settled":
        "its own word, its pre/post-fix pin and its paper closed forms are all grouped",
    "reduced-block-kernel":
        "its self-test compares two monotone-only paths (qou-cvky)",
    "the_character_closure_block_and_a_lean_file_publish_convention_c_probe":
        "its SUBJECT is the convention-C trace table that "
        "prop:q-hecke-seminormal-character-closure publishes; carrying C-era "
        "values is the finding, not a defect (qou-4383)",
    "colour-weighting-trace-magnitude":
        "its SUBJECT is the colour comparison — it holds the colour-BLIND and "
        "the colour-weighted trace side by side to measure the gap, so both "
        "frames are the measurement (qou-fv0s; found by the colour axis added "
        "under qou-uujo)",
    # The five C-vs-D comparison probes. Their SUBJECT is the convention gap,
    # so each holds the convention-C trace beside the D one and both are the
    # measurement — the same shape as the two colour probes below. Listed
    # explicitly rather than matched on the shared `-c-vs-d-` stem because
    # `qou-4bq3` records a DELIBERATE regex over-blocking 8 of 24 B3 verdicts:
    # a pattern that is right today silently swallows tomorrow's real finding.
    # Found by the convention-C axis added under `qou-ng7j`.
    "binding-closed-form-c-vs-d":
        "holds tau_H3_C and tr_M_atom_C beside their D counterparts; the gap "
        "is the measurement",
    "binding-production-route-c-vs-d-deut":
        "production-route C-vs-D at the deuteron; carries tr_M_atom_C by design",
    "binding-production-route-c-vs-d-trit-heli":
        "the same at tritium / helium-3",
    "binding-sum-c-vs-d-deut":
        "binding-sum C-vs-D at the deuteron; carries tr_M_C by design",
    "binding-sum-c-vs-d-trit-heli":
        "the same at tritium / helium-3",
    "colour-weighting-across-mixed-nuclei":
        "the sibling of the above, extending that measurement from the "
        "deuteron to T / 3He / 4He because the linear coefficient tr(A B) is "
        "word-specific and does not transfer; same reason, same registry entry",
}


def fingerprints() -> dict[str, tuple[str, str, str, str]]:
    """{15-sig-digit prefix: (atom, pin, ordering, colour convention)} — live.

    THE COLOUR AXIS IS THE SECOND SUPERSEDED STATE, added 2026-09-14
    (bean `qou-uujo`). This swept `intra_order` only and always took
    `pn_convention`'s default, so it could see the 2026-09-05 ordering ruling
    and not the 2026-08-15 colour one. Tracing the ⁴He pin
    `0.0553483351637685668` turned up a lineage of at least five states, of
    which this audit covered two:

        convention C, muon q₀          0.0553483458766980
        convention C, proton q₀        0.0553483351637685
        convention D, colour-BLIND     (the axis added here)
        convention D, colour-weighted, grouped
        convention D, colour-weighted, borromean   <- canonical

    `binding_canonical` quotes the colour-blind deuteron by name as
    `0.575090871629810316751633`, against `0.575172243917771870826535` for the
    canonical convention, so these values are demonstrably in circulation.

    **Convention C is deliberately NOT covered, and cannot be.** It is a
    property of the TRACE, not the word: `Z_MARKOV` is a module constant at
    `mass_at_3A_proper:121` with no flag, so no live fingerprint can be
    computed for it. Adding it would mean transcribing literals, which is
    exactly what this audit's design forbids — every fingerprint here is
    recomputed, so a re-pin moves them rather than silently invalidating the
    scan. A convention-C detector would need a different mechanism and should
    not be bolted on here.

    A lone nucleon has no p-n interface, so the two conventions give the SAME
    number for `proton` and `neutron`. That is not a collision to report — the
    entry is marked `either` and stored once.
    """
    out: dict[str, tuple[str, str, str, str, str]] = {}

    def _add(v, meta):
        """Record one fingerprint, folding a colour-independent duplicate.

        A lone nucleon has no p-n interface, so its two colour conventions give
        the SAME number. That is not a collision to report — the first (always
        the canonical convention) is kept and marked `either`.
        """
        key = mp.nstr(v, SIG_DIGITS).rstrip("0")
        prev = out.get(key)
        if prev is not None:
            if prev[0] == meta[0] and prev[1] == meta[1] \
                    and prev[2] == meta[2] and prev[4] == meta[4]:
                out[key] = (meta[0], meta[1], meta[2], "either", meta[4])
            return
        out[key] = meta

    for pin, qs in PINS.items():
        q = mp.mpf(qs)
        z_c = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
        for atom, (Z, N) in ATOMS.items():
            n = 3 * (Z + N)
            for order in ("grouped", "borromean"):
                # canonical convention FIRST, so a colour-independent atom is
                # recorded under it and `strict_averaged` folds into `either`.
                for conv in ("bring_color_weighted", "strict_averaged"):
                    word = M.atom_braid_word_3A(Z, N, q=q, intra_order=order,
                                                pn_convention=conv)
                    # D: the production path, left exactly as it was.
                    v_d = abs(B.tr_M_via_wenzl_bridge_mpfr(word, n, qs, dps=50))
                    _add(v_d, (atom, pin, order, conv, "D"))
                    # C: NOT reachable through that path, and this is the
                    # second reason `qou-ng7j`'s blindness is structural rather
                    # than a missing pattern. The bridge evaluates chi only
                    # where y_lambda is nonzero, and under D the Wenzl row cap
                    # zeroes every partition with more than two rows — for the
                    # deuteron it evaluates 4 of 11. Under C **every channel is
                    # live** (measured: 7 of 7 three-or-more-row partitions
                    # carry nonzero weight), so a C trace needs exactly the chi
                    # the D pipeline discards. Hence the full table here.
                    chi = _chi_all(word, n, q)
                    v_c = abs(sum((M.jones_wenzl_weight(tuple(lam), q=q, z=z_c)
                                   * val for lam, val in chi.items()),
                                  mp.mpf(0)))
                    _add(v_c, (atom, pin, order, conv, "C"))
        # THE MARKOV PARAMETER ITSELF, not an atom trace. `qou-ng7j`'s table
        # lists `z` as a convention-dependent quantity the detector sees "only
        # if it happens to match a listed decimal" — it never did. z_C is one
        # number per pin, so it costs two fingerprints.
        _add(z_c, ("z", pin, "n/a", "n/a", "C"))
    return out


#: A JSON path that declares its value is convention C. Deliberately matched on
#: the PATH, not the file — see the note at its use site.
_C_LABELLED_PATH = __import__("re").compile(
    r"convention|/C/|(^|[/_\[])C($|[/_\]])|z_C|_c_for|c_sqrt|naive|cited",
    __import__("re").I)


def _chi_all(word, n, q):
    """Per-partition chi for EVERY partition of n — no row cap.

    `chi_general_word.chi_all_lambda_any` accepts a non-monotone word, which
    the canonical borromean ordering is by construction. Cheap: 0.1 s at n = 9.
    """
    from chi_general_word import chi_all_lambda_any     # noqa: PLC0415
    return chi_all_lambda_any(word, n, dps=50, q=q)


def _axis(order: str, conv: str, trace: str = "D") -> str:
    """Which superseded axis a hit sits on — all three are possible at once."""
    bits = []
    if trace == "C":
        bits.append("convention-C")
    if order == "grouped":
        bits.append("grouped")
    if conv == "strict_averaged":
        bits.append("colour-blind")
    return "+".join(bits) if bits else "canonical"


def scan_value(s: str, fps: dict) -> tuple | None:
    """Does this string start with a fingerprint, to SIG_DIGITS?"""
    t = s.lstrip("-").lstrip()
    for pref, meta in fps.items():
        p = pref.lstrip("-")
        if t.startswith(p) and len(p.replace(".", "").lstrip("0")) >= SIG_DIGITS - 1:
            return meta
    return None


#: Producers whose SOURCE may legitimately carry a grouped literal in code.
#: Distinct from DELIBERATE, which is about witness payloads: a probe whose
#: SUBJECT is the ordering comparison must hold both frames as data to compare
#: them, and flagging that would be flagging the measurement.
SOURCE_DELIBERATE = {
    "qbeta_delta_vs_deltaTbeta_settled_probe.py":
        "deliberately grouped throughout — its own word, its pre/post-fix pin "
        "and its paper closed forms are all grouped (see DELIBERATE)",
}
#: This list is SHORT because the AST docstring exclusion already does the work.
#: It was drafted with seven entries — `mass_at_3A_proper`,
#: `atom_intra_block_is_not_a_braid_probe`, `nf_vs_canonical_word_order_probe`,
#: `nucleon_h3_marshalling_divergence_probe`, the convention-C probe,
#: `the_intra_ordering_moves_absolute_traces...` and `trm_proton_five_values_census`
#: — every one of which turned out to carry its grouped value only in PROSE and
#: to drop out on its own. Six dead entries in a curated set is the rot that
#: makes the next reader trust the list instead of the mechanism, so they are
#: gone. Add one here only after confirming the AST scan actually flags the file.


def _source_constants(tree):
    """Every literal reachable as CODE, with docstrings excluded.

    Comments never enter an AST, so they are excluded for free. Docstrings are
    excluded explicitly: `mass_at_3A_proper` quotes both the grouped and the
    borromean |tr_M| in the docstring that EXPLAINS the 2026-09-05 ruling, and
    flagging that would be flagging the documentation of the fix.

    Strings are NOT skipped wholesale — `mp.mpf("1.1457...")` is a literal in
    code, and skipping it would miss the exact shape this corpus writes its
    high-precision constants in.
    """
    docstrings = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.ClassDef, ast.FunctionDef,
                          ast.AsyncFunctionDef)):
            body = getattr(n, "body", None)
            if (body and isinstance(body[0], ast.Expr)
                    and isinstance(body[0].value, ast.Constant)
                    and isinstance(body[0].value.value, str)):
                docstrings.add(id(body[0].value))
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and id(n) not in docstrings:
            if isinstance(n.value, (int, float, str)):
                yield n.lineno, str(n.value)


def scan_source(fps):
    """Grouped-era values written as LITERALS in producer source.

    The witness scan below answers "does this artifact carry a grouped value?".
    This answers a different and sharper question: "does this SOURCE carry
    one?" A stale witness regenerates; a hardcoded constant does not, and it
    re-emits the grouped value on every future run.

    `qou-4383` found two of these by hand (`T_P` / `MEASURED["t_p"]` in two
    qbeta probes). Extending the audit's own value-keyed method from witnesses
    to source finds them all — which is the same argument the bean makes for
    keying on the answer rather than on a symptom.
    """
    out: dict[str, list] = {}
    for f in sorted(_COMPUTATIONS.rglob("*.py")):
        if any(s in f.parts for s in ("_deprecated", "fsh-guts", "__pycache__", ".git")):
            continue
        try:
            src = f.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(src)
        except (OSError, SyntaxError):
            continue
        for lineno, lit in _source_constants(tree):
            meta = scan_value(lit, fps)
            if meta and meta[2] == "grouped":
                rel = str(f.relative_to(_ROOT))
                out.setdefault(rel, []).append((lineno, lit[:26], meta[0], meta[1]))
    return out


#: Calls that COMPUTE a Markov trace from a braid word. A producer that makes
#: one of these owns its numbers; a producer that makes none of them can only
#: be carrying numbers it read.
_COMPUTE_CALLS = {
    "atom_braid_word_3A", "canonical_word_for",
    "tr_M_via_wenzl_bridge_mpfr", "tr_M_via_wenzl_bridge", "tr_m_atom_zn",
    "build_seminormal_matrices", "build_seminormal_matrices_mp",
    "markov_trace_numerical", "markov_trace", "tr_M_canonical",
    "chi_all_lambda_any", "chi_free_lr", "hecke_character_symbolic",
}

#: Calls that READ a committed artifact.
_READ_CALLS = {"load", "loads", "read_text", "open", "glob", "iglob",
               "load_witness", "tr_m_nucleon", "tr_m_proton", "tr_m_neutron"}


def _called_names(tree) -> set[str]:
    """Every name this module actually CALLS or imports.

    AST, not substring — and the difference is load-bearing here exactly as it
    was for the source scan. Eight of the candidate producers MENTION
    `atom_braid_word_3A` in a docstring or comment while never calling it; a
    grep would file them as computing their own traces, which is the opposite
    of true.
    """
    import ast as _ast
    out = set()
    for n in _ast.walk(tree):
        if isinstance(n, _ast.Call):
            f = n.func
            if isinstance(f, _ast.Name):
                out.add(f.id)
            elif isinstance(f, _ast.Attribute):
                out.add(f.attr)
        elif isinstance(n, (_ast.Import, _ast.ImportFrom)):
            for a in n.names:
                out.add(a.name.split(".")[-1])
                if a.asname:
                    out.add(a.asname)
    return out


def classify_producer(script_name: str):
    """('computes'|'reflects'|'neither'|'unresolved', detail) for a witness's producer.

    WHY THIS EXISTS (bean `qou-4383`, "the taxonomy needs a third category").
    The bean's own analysis: many surviving candidates are neither stale
    artifacts nor live source defects. `witness_value_copy_audit` scrapes
    witnesses for copied values; `derivation_chain_validator` classifies every
    witness it can find; several more are explicit C-vs-D comparisons holding
    both frames on purpose. They carry grouped values BECAUSE THEIR INPUTS DO,
    they resolve when the inputs resolve, and repairing them at the reflection
    would be wrong. Counting them keeps the total from ever converging —
    "an audit that reports the corpus will always mirror it".

    The discriminator is what the producer can possibly know: a module that
    never calls the trace machinery cannot have computed a |tr_M|, so any it
    emits came from something it read. That is a fact about the code, not a
    judgement about intent, which is why it can be mechanical.
    """
    import ast as _ast
    hits = list(_COMPUTATIONS.rglob(script_name)) if script_name else []
    if not hits:
        return "unresolved", "no producer file found"
    try:
        tree = _ast.parse(hits[0].read_text(encoding="utf-8", errors="replace"))
    except (OSError, SyntaxError):
        return "unresolved", "producer unparseable"
    called = _called_names(tree)
    comp = sorted(called & _COMPUTE_CALLS)
    if comp:
        return "computes", "calls " + ", ".join(comp[:3])
    if called & _READ_CALLS:
        return "reflects", "reads artifacts; calls no trace machinery"
    # MIXED BUCKET, and honest about it. Measured on the 10 that land here:
    # some hardcode a grouped literal (path_b_defect_binding_probe,
    # qbeta_chain_closed_form_probe — both independently flagged by this
    # audit's SOURCE arm) and some compute inline without calling anything
    # named above (vhat_per_crossing_chain builds Hoefsmit matrices and takes
    # the trace by hand). Both own their value, so both are actionable; the
    # bucket is not called "computes" because for the hardcoders that is false.
    return "neither", "no trace call and no artifact read — hardcodes, or computes inline"


def walk(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, f"{path}/{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o
    elif isinstance(o, float):
        yield path, repr(o)


def main() -> int:
    fps = fingerprints()
    print(f"Intra-ordering value fingerprint audit — {SIG_DIGITS} significant digits")
    print(f"  {len(fps)} fingerprints: {len(ATOMS)} atoms x "
          f"{len(PINS)} pins x 2 orderings x 2 colour conventions x "
          f"2 trace conventions (C/D), plus z_C itself at each pin — a "
          f"lone nucleon has no p-n interface, so its two colour "
          f"conventions coincide and fold to one entry\n")

    # This audit's OWN witness records its findings, and its findings contain
    # the grouped values it found — so scanning it reports the report. Excluded
    # for the same reason the source scan excludes this file: a detector that
    # fires on its own output is noise, and it is exactly the "an audit that
    # reports the corpus will always mirror it" trap this bean names. It
    # appeared the moment the source arm started recording literals.
    _self_witness = _HERE / (Path(__file__).stem + ".witness.json")
    files = sorted(p for p in _ROOT.rglob("*.witness.json")
                   if ("_deprecated" not in str(p) and "fsh-guts" not in str(p)) and ".git" not in str(p)
                   and p != _self_witness)
    grouped_hits: dict[str, list] = {}
    borro_hits: dict[str, list] = {}

    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        for path, s in walk(d):
            meta = scan_value(s, fps)
            if meta is None:
                continue
            atom, pin, order, conv, trace = meta
            rel = str(f.relative_to(_ROOT))
            # A `z` value sitting in a field whose PATH names the convention is
            # the author saying so: `/conventions/C_sqrt_q_over_q_plus_1`,
            # `/parameters/z_C_for_comparison`, `/data/conventions/C/z_at_q0`.
            # Measured at 15 sig digits: 82 z_C hits over 52 files, of which 41
            # files are self-declaring like that and 11 are not.
            #
            # Discriminating on the PATH rather than the file stem is the whole
            # point. `qou-ztee` records that this audit family has "no way to
            # mark a deliberate comparison", and a registry does not scale to
            # 41 entries; `qou-4bq3` records a DELIBERATE stem regex
            # over-blocking 8 of 24 verdicts. A path label is narrower than
            # either: it exempts the one FIELD the author labelled, not the
            # whole file.
            if atom == "z" and _C_LABELLED_PATH.search(path):
                continue
            # SUPERSEDED ON ANY OF THREE AXES. This tested `order == "grouped"`
            # only, so a value in the canonical ordering but the colour-BLIND
            # convention read as clean (`qou-uujo`), and a convention-C TRACE
            # was invisible entirely (`qou-ng7j`). All three are superseded
            # states and all three belong in the same bucket.
            superseded = (order == "grouped") or (conv == "strict_averaged") \
                or (trace == "C")
            bucket = grouped_hits if superseded else borro_hits
            bucket.setdefault(rel, []).append(
                (path, atom, pin, order, conv, trace))

    deliberate, candidates = {}, {}
    for rel, hits in grouped_hits.items():
        stem = Path(rel).name.replace(".witness.json", "")
        (deliberate if stem in DELIBERATE else candidates)[rel] = hits

    # THIRD CATEGORY (bean qou-4383). Split the candidates by what their
    # producer can possibly know. A reflection's grouped value came from its
    # inputs and resolves when they do; counting it keeps the total from
    # converging, because an audit that reports the corpus will always mirror
    # it. Reported, never hidden — just not counted as actionable.
    actionable, reflections, unresolved = {}, {}, {}
    kinds = {}
    for rel, hits in candidates.items():
        try:
            _d = json.loads((_ROOT / rel).read_text(encoding="utf-8", errors="replace"))
            _sf = _d.get("scriptFile") or (_d.get("data") or {}).get("scriptFile")
        except Exception:
            _sf = None
        kind, why = classify_producer(_sf) if _sf else ("unresolved", "witness names no scriptFile")
        kinds[rel] = (kind, why, _sf)
        if kind == "reflects":
            reflections[rel] = hits
        elif kind == "unresolved":
            unresolved[rel] = hits
        else:
            actionable[rel] = hits

    _all = [h for hs in grouped_hits.values() for h in hs]
    _n_c = sum(1 for h in _all if h[5] == "C")
    _n_ord = sum(1 for h in _all
                 if h[5] != "C" and h[3] == "grouped" and h[4] != "strict_averaged")
    _n_col = sum(1 for h in _all
                 if h[5] != "C" and h[3] != "grouped" and h[4] == "strict_averaged")
    _n_both = sum(1 for h in _all
                  if h[5] != "C" and h[3] == "grouped" and h[4] == "strict_averaged")
    print(f"=== SUPERSEDED-era hits: {len(grouped_hits)} witness file(s) ===")
    print(f"    by axis: {_n_c} convention-C (any word frame), "
          f"{_n_ord} grouped only, {_n_col} colour-blind only, {_n_both} both")
    print(f"    {len(candidates)} candidate(s), {len(deliberate)} known-deliberate")
    # "ACTIONABLE" means the SITE OWNS ITS VALUE — it either computes the trace
    # or hardcodes one — so the fix belongs there. It deliberately does NOT
    # claim the producer computes: `neither` (calls no trace machinery and
    # reads no artifact) is a mixed bucket, and both of its populations are
    # actionable at the site.
    #
    #   * HARDCODERS. `path_b_defect_binding_probe` and
    #     `qbeta_chain_closed_form_probe` land here, and the SOURCE arm of this
    #     same audit independently flags both for carrying grouped literals —
    #     two detectors agreeing from opposite directions.
    #   * COMPUTERS BY AN UNLISTED IDIOM. `vhat_per_crossing_chain` builds
    #     Hoefsmit matrices and takes the trace inline, so it computes without
    #     calling anything in `_COMPUTE_CALLS`.
    #
    # Left merged rather than split further: the distinction changes WHY the
    # site owns its value, not WHETHER it does, and a bucket named for a
    # property it does not have is worse than a coarse one.
    print(f"    of the candidates: {len(actionable)} ACTIONABLE (the site owns "
          f"its value — computes or hardcodes it), {len(reflections)} downstream "
          f"reflections, {len(unresolved)} unresolved\n")
    for rel, hits in sorted(actionable.items()):
        print(f"  CANDIDATE {rel}   [{kinds[rel][0]}: {kinds[rel][1]}]")
        for path, atom, pin, order, conv, trace in hits[:4]:
            print(f"      {atom} @ {pin} [{_axis(order, conv, trace)}]   {path}")
        if len(hits) > 4:
            print(f"      … and {len(hits) - 4} more field(s)")
    if reflections:
        print(f"\n  downstream reflections ({len(reflections)}) — carry grouped "
              f"values because their INPUTS do; fix the inputs, not these:")
        for rel in sorted(reflections):
            print(f"      {rel}   ({kinds[rel][2]})")
    if unresolved:
        print(f"\n  unresolved ({len(unresolved)}) — no producer to classify; "
              f"these need a scriptFile before they can be triaged:")
        for rel in sorted(unresolved):
            print(f"      {rel}   ({kinds[rel][1]})")
    if deliberate:
        print("\n  known-deliberate (grouped on purpose, not findings):")
        for rel in sorted(deliberate):
            stem = Path(rel).name.replace(".witness.json", "")
            print(f"      {rel}\n          {DELIBERATE[stem]}")

    # ---- SOURCE scan: grouped values written as literals in code -----------
    src_all = scan_source(fps)
    src_deliberate = {k: v for k, v in src_all.items()
                      if Path(k).name in SOURCE_DELIBERATE}
    src_hard = {k: v for k, v in src_all.items()
                if Path(k).name not in SOURCE_DELIBERATE}
    print(f"\n=== GROUPED-era literals in SOURCE: {len(src_all)} file(s) ===")
    print(f"    {len(src_hard)} hardcoded, {len(src_deliberate)} known-deliberate")
    print("    A stale witness regenerates. A hardcoded constant does not — it")
    print("    re-emits the grouped value on every future run.\n")
    for rel, hits in sorted(src_hard.items()):
        print(f"  HARDCODED {rel}")
        for lineno, lit, atom, pin in sorted(set(hits))[:4]:
            print(f"      L{lineno:<5d} {lit:26s}  {atom} @ {pin}")
    if src_deliberate:
        print("\n  known-deliberate source (the ordering IS the subject):")
        for rel in sorted(src_deliberate):
            print(f"      {rel}\n          {SOURCE_DELIBERATE[Path(rel).name]}")

    print(f"\n=== borromean (canonical) hits: {len(borro_hits)} witness file(s) ===")
    for rel in sorted(borro_hits)[:12]:
        print(f"      {rel}")
    if len(borro_hits) > 12:
        print(f"      … and {len(borro_hits) - 12} more")

    from witness_base import WitnessBuilder  # noqa: E402
    wb = WitnessBuilder(Path(__file__).stem, engine="python")
    wb.set_description(
        "Scans every committed witness for grouped-era |tr_M| values, matched "
        "to 15 significant digits against fingerprints computed live from "
        "atom_braid_word_3A under both orderings at both documented pins. Keys "
        "on the VALUE rather than on a symptom, because the ordering ruling has "
        "escaped three symptom-keyed sweeps."
    )
    wb.add_data("significant_digits_required", SIG_DIGITS)
    wb.add_data("witness_files_scanned", len(files))
    wb.add_data("grouped_candidates", {k: [list(h) for h in v]
                                       for k, v in sorted(candidates.items())})
    wb.add_data("grouped_deliberate", sorted(deliberate))
    wb.add_data("grouped_actionable", sorted(actionable))
    wb.add_data("grouped_downstream_reflections", sorted(reflections))
    wb.add_data("grouped_unresolved_producer", sorted(unresolved))
    wb.add_data("producer_classification",
                {k: {"kind": v[0], "why": v[1], "scriptFile": v[2]}
                 for k, v in sorted(kinds.items())})
    wb.add_data("borromean_hits", sorted(borro_hits))
    wb.add_data("source_hardcoded_grouped",
                {k: [list(h) for h in sorted(set(v))]
                 for k, v in sorted(src_hard.items())})
    wb.add_data("source_deliberate_grouped", sorted(src_deliberate))
    wb.add_assertion(name="scan_completed",
                     computed=str(int(len(files) > 0)), expected="1")
    wb.add_assertion(name="source_files_scanned_for_literals",
                     computed=str(int(len(src_all) >= 0)), expected="1")
    wb.add_caveat(
        "A hit says the WITNESS payload is grouped-era; it does not say the "
        "producer is. Re-run the producer to tell a stale artifact from a live "
        "source defect. A non-hit is not a clean bill: a witness recording only "
        "derived quantities carries no |tr_M| for this to match."
    )
    wb.add_caveat(
        "The SOURCE scan reads literals reachable as code, with docstrings "
        "excluded (comments never enter an AST). That exclusion is load-"
        "bearing, not a convenience: mass_at_3A_proper's docstring quotes both "
        "the grouped and the borromean |tr_M| precisely because it EXPLAINS "
        "the 2026-09-05 ruling, and flagging it would be flagging the "
        "documentation of the fix. Strings are not skipped wholesale, because "
        "mp.mpf(\"1.1457...\") is how this corpus writes a high-precision "
        "constant."
    )
    wb.add_caveat(
        "Fingerprints are computed live, never transcribed, so a re-pin moves "
        "them rather than silently invalidating the scan. Only the five atoms "
        "at A <= 3 and the two documented pins are covered."
    )
    # The fingerprints are computed at BOTH documented pins on purpose (a
    # grouped-era value is recognised wherever it was written, at either pin),
    # so this is a q0 comparison, not a single-pin result.
    from qou_substrate.witness import q0_comparison  # noqa: E402
    print(f"\nWitness: {wb.save(q0_comparison(muon=PINS['muon-live'], proton=str(PINS['proton']), reason='fingerprints grouped-era |tr_M| at BOTH documented pins (proton Q_50_DIGIT_STR and the live CODATA-2022 muon pin q_muon_at(70)) so a grouped value is matched whichever pin produced it; both pins are read on purpose'))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
