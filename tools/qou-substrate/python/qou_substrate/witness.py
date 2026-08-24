# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Unified witness infrastructure for QOU computation scripts.

Every Python computation that produces a witness statement should use
this module to ensure consistent structure, commit SHA tracking, and
content-block integration.

Usage:
    from qou_substrate.witness import WitnessBuilder
    # equivalently: from qou_substrate import WitnessBuilder

    w = WitnessBuilder("my-computation", engine="sympy")
    w.set_description("Computes foo from bar")
    w.add_assertion("Vol(4_1)", computed=2.0298, expected=2.0298, tolerance=1e-10, source="SnapPy")
    w.add_parameter("q", q0)
    w.add_data("extra_result", {"key": "value"})
    w.set_content_block("prop:my-proposition")
    w.save()  # writes my-computation.witness.json

The output conforms to the ComputationWitness interface in
folio-assistant/schemas/types.ts.

@module qou_substrate.witness
"""

import hashlib
import json
import os
import re as _re
import warnings as _warnings
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PurePath
from typing import Any, Mapping, Optional, Union


# ── Git helpers ──────────────────────────────────────────────────

def _repo_root() -> Path:
    """Find the repository root (walk up from this file)."""
    d = Path(__file__).resolve().parent
    while d != d.parent:
        if (d / ".git").exists():
            return d
        d = d.parent
    return Path(__file__).resolve().parent.parent.parent


# ── q₀-anchor provenance ─────────────────────────────────────────
# The substrate modulus q₀ has two documented pins (AGENTS.md §"q₀ anchor
# convention"): the IDEAL / canonical 3-CAL value is MUON-anchored, the
# PHYSICAL-Observations value is PROTON-anchored, ~11.5 ppb apart. A witness
# value is meaningless without knowing WHICH anchor produced it — the recurring
# "flip-flop" bug (bean tnjb) is a consumer silently reading a muon value as
# proton (or vice-versa). Every witness therefore records `q0Anchor` + `q0Value`
# so the anchor is explicit and the value can never be misread. The anchor is
# resolved from the SAME source the runtime uses to pick q₀
# (`computations/q0_anchor_manifest.json` + the QOU_Q0_ANCHOR env override), so
# the stamped label always matches the value the producer actually computed.
#
# THE VOCABULARY (`q0Anchor`) has five values. The last two are not resolvable
# from the manifest and must be declared by the producer:
#
#   "muon"        ideal / canonical 3-CAL pin; carries the muon `q0Value`
#   "proton"      experimental / Physical-Observations pin (the standing
#                 default for new compute, owner directive 2026-08-07)
#   "ambiguous"   the compute DEPENDS on q₀ but the pin is undetermined —
#                 `gen_q0_anchor_manifest.py` assigns this when a witness
#                 carries BOTH signatures. A queue for a manual ruling.
#   "independent" the compute NEVER READS q₀. No `q0Value` exists, and one
#                 appearing alongside this label is a contradiction the audit
#                 reports as Q0_FLIP.
#   "comparison"  the compute reads MORE THAN ONE anchor DELIBERATELY — the
#                 comparison is the subject. Carries `q0Values`, a mapping
#                 {anchor: 50-digit value} with an entry per pin read, and NO
#                 bare `q0Value` (there is no single pin; one alongside this
#                 label is a Q0_FLIP, exactly as under `independent`).
#
# Why `comparison` is not one of the other four. A cross-anchor probe fits none
# of them: `muon`/`proton` each assert ONE pin; `independent` would be a FALSE
# claim of layer-freedom when the compute reads q₀ twice; and `ambiguous`, though
# descriptively true that both signatures are present, is defined above as "the
# pin is UNDETERMINED … a queue for a manual ruling" — a deliberate comparison is
# not undetermined, and filing it there mislabels it for whoever drains that
# queue. Before this value such probes had no honest option and landed in
# `Q0_ANCHOR_MISSING`, indistinguishable from producers that simply forgot
# (bean `qou-po7i`).
#
# This matters beyond bookkeeping. AGENTS.md §"q₀ anchor convention" makes
# mixing an ideal-layer input with an experimental-layer one inside a single
# quantity a DEFECT ("never straddle the two layers inside one quantity" — the
# μ₃ Fréchet probe, an 11.54 ppb error). `comparison` is what lets the audit
# separate that real defect from a probe whose whole point is telling the pins
# apart; without it both look the same and the defects hide in a bucket of ~1890.
#
# `comparison` is also the ONE label the audit can VERIFY rather than take on
# trust: `independent` asserts something about an import cone and can only be
# checked by re-deriving it, whereas `comparison` NAMES its pins, and each named
# pin either matches its canonical value or does not. So:
#
#   w.save({"q0Anchor": "comparison",
#           "q0Values": {"muon": q_muon_str, "proton": q_proton_str},
#           "q0AnchorReason": "measures the c_3 cross-anchor swing; both pins "
#                             "are read on purpose and each is reported under "
#                             "its own key"})
#
# `resolve_q0_anchor` never returns it, for the same reason it never returns
# `independent`: no manifest lookup can establish intent.
#
# `q0AnchorReason` (free text) states WHY, and belongs with every
# `independent` — and with `ambiguous`, where it names what is undetermined.
# The token alone is a weak record: a reader opening the witness sees
# `"independent"` and has no way to check it without re-deriving the import
# cone, which is the work the declaration was supposed to save them. Compare
# the `<!-- literal-source: … -->` convention on the same axis, where the
# marker is worth almost nothing and the sentence after the colon is the whole
# value. So:
#
#   w.save({"q0Anchor": "independent",
#           "q0AnchorReason": "Sabra shell-spacing ratio q = 1 + eps over "
#                             "EPS_SWEEP; no substrate value read"})
#
# is the shape to write, not the bare token. `Q0_INDEPENDENT_NO_REASON` in
# `q0_anchor_consistency_audit.py` counts the ones that omit it, so a thin
# declaration stays visible instead of reading as a complete one. Recorded as
# bean `qou-mw1p`, from design advice on PR #5124: a positive declaration has
# to survive the next reader, and `true` does not.
#
# `independent` is producer-declared only: `w.save({"q0Anchor": "independent"})`.
# It cannot be inferred, and the manifest generator must not try. Its scan sees
# this class already and drops it (`# neither: no q₀ field — omit`), because
# "the witness serializes no q₀" does not imply "the compute never used q₀" — a
# producer can use q₀ and simply not record it. Inferring independence there
# would mint false claims of layer-freedom at scale. An agent reads the import
# cone and asserts it; the audit then distinguishes a q₀-free producer from one
# that merely forgot, which before this value it could not (bean qou-rw91, and
# earlier qou-pin1 on the purely symbolic `chi-deuteron-h6`).

def q0_comparison(*, muon, proton, reason: str, dps: int = 52) -> dict:
    """Build the ``comparison`` q₀-anchor stamp for a cross-anchor producer.

    A producer that reads BOTH pins DELIBERATELY — where the comparison is the
    subject — declares it by passing this dict to ``save()``::

        wb.save(q0_comparison(
            muon=qm, proton=qp,
            reason="measures the c_3 cross-anchor swing; both pins are read on "
                   "purpose and each is reported under its own key"))

    Pass the values the producer ACTUALLY COMPUTED WITH, not the canonical
    constants. The audit re-checks each leg against its canonical pin, so
    stamping the constant would make the check a tautology; stamping the
    computed value makes it a real test — a producer that thinks it read the
    muon pin but read the proton one is then caught, which is the flip-flop bug
    happening inside a comparison.

    Deliberately emits NO bare ``q0Value``: there is no single pin, and one
    alongside this label is a ``Q0_FLIP``.

    See the vocabulary note at the top of this module for why this is a
    separate value from ``ambiguous`` and ``independent`` rather than a reuse
    of either (bean ``qou-po7i``).
    """
    if not str(reason or "").strip():
        raise ValueError(
            "q0_comparison requires a reason: the label states that two pins "
            "were read on purpose, and without saying what is being compared a "
            "reader cannot tell it from an accidental layer straddle (which "
            "AGENTS.md makes a defect)."
        )

    def _fmt(v) -> str:
        if isinstance(v, str):
            return v
        try:
            import mpmath as _mp
            return _mp.nstr(_mp.mpf(v), dps, strip_zeros=False)
        except Exception:  # noqa: BLE001
            return str(v)

    return {
        "q0Anchor": "comparison",
        "q0Values": {"muon": _fmt(muon), "proton": _fmt(proton)},
        "q0AnchorReason": reason,
    }


_Q0_VALUE_CACHE: dict = {}


def _q0_value_for_anchor(anchor: str) -> Optional[str]:
    """The 50-digit q₀ string for a given anchor (cached). muon ← the committed
    q-pinning witness; proton ← the package constant.

    REVERTED 2026-08-15, same day, after a red-team pass. I had changed the
    muon branch to DERIVE from ``q_muon_at()``. That was a regression, and the
    reasoning behind it was false. Both are recorded because the second error
    is subtle and someone will try the same fix again.

    **The change broke the field's purpose.** ``q0Value`` records the value the
    producer actually computed with. A muon-tagged producer computes with the
    witness string, so deriving the label made the stamp disagree with the
    compute — measured 1.1099785955573347 computed vs 1.1099785955541805
    stamped. Before the change they agreed. That is exactly the misread this
    field exists to prevent, introduced while claiming to prevent it.

    **The justification was also wrong.** I claimed re-running
    ``q_pinning_50_digit.py`` would flip every muon stamp to a PROTON value,
    since that script sets ``Q = q_at(mp.dps)``. It does not.
    ``q_pinning_50_digit`` is listed in ``computations/q0_anchor_manifest.json``
    under ``ideal_muon``, so ``q_parameter`` resolves the anchor from the argv
    stem and rebinds ``q_at`` to return the witness string. Verified under the
    producer's real argv: ``q_at(70)`` -> ``1.10997859555733471989…``. The
    producer is a FIXED POINT; re-running it changes nothing.

    **The real defect, which that story obscured, is CIRCULARITY.** The muon
    50-dps constant certifies itself — the producer reads, via ``q_at``, the
    witness it writes. It has never been derived from a closed form, which is
    exactly why ``q_muon_at()`` does not reproduce it. Breaking the loop means
    giving the muon anchor a real derivation and re-running its dependents; it
    must move the LABEL and the COMPUTED VALUE together, or it reintroduces the
    disagreement above.

    Note ``computations/substrate/q_parameter.py`` asserts the witness starts
    with ``1.109978595557``, so substituting the canonical string there
    hard-fails all 257 ``ideal_muon`` producers, and a second copy of that
    guard ships in the published ``qou_mass`` package.
    """
    if anchor in _Q0_VALUE_CACHE:
        return _Q0_VALUE_CACHE[anchor]
    val: Optional[str] = None
    try:
        if anchor == "muon":
            p = _repo_root() / "computations" / "q-pinning-50-digit.witness.json"
            val = json.loads(p.read_text(encoding="utf-8"))["derived_50_digit"]["q"]
        elif anchor == "proton":
            from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: PLC0415
            val = str(Q_50_DIGIT_STR)
    except Exception:  # noqa: BLE001
        val = None
    _Q0_VALUE_CACHE[anchor] = val
    return val


_Q0_PREFIXES = (("proton", "1.10997858275"), ("muon", "1.10997859555"))
_Q0_FIELDS = ("q_0_50dps", "q0", "q_0", "q0_50dps")


def _q0_anchor_from_payload(payload: Mapping) -> Optional[str]:
    """The anchor a payload's own q₀ VALUES imply, or None if it records none.

    Evidence only — used to refuse carrying a stale `q0Anchor` across a
    re-anchoring, never to invent a pin. Returns None when the payload records
    no recognisable q₀, and also when it records BOTH pins: a payload that
    legitimately spans layers (a cross-anchor comparison) must not have either
    one asserted over it.
    """
    seen = set()

    def walk(node, depth=0):
        if depth > 4 or len(seen) > 1:
            return
        if isinstance(node, Mapping):
            for k, v in node.items():
                if k in _Q0_FIELDS and isinstance(v, str):
                    for name, pre in _Q0_PREFIXES:
                        if v.strip().startswith(pre):
                            seen.add(name)
                elif isinstance(v, (dict, list)):
                    walk(v, depth + 1)
        elif isinstance(node, list):
            for v in node[:64]:
                walk(v, depth + 1)

    walk(payload)
    return seen.pop() if len(seen) == 1 else None


def resolve_q0_anchor(
    script_path: Union[str, Path], *, env: Optional[Mapping[str, str]] = None,
) -> tuple:
    """Return ``(anchor, q0_value)`` for the producer at ``script_path``.

    ``anchor`` ∈ {``"muon"``, ``"proton"``, ``"ambiguous"``}. Precedence mirrors
    ``q_parameter``: an explicit ``QOU_Q0_ANCHOR`` env var wins; otherwise the
    producer's file stem is looked up in ``q0_anchor_manifest.json``
    (``ideal_muon`` ⇒ muon, ``physical_proton`` ⇒ proton, ``ambiguous`` ⇒
    ambiguous, and — matching the runtime default — anything else ⇒ proton).
    ``q0_value`` is the matching 50-digit string, or ``None`` for ambiguous.

    Never returns ``"independent"`` or ``"comparison"``. Those two state
    something about the producer's INTENT — that q₀ is never read, or that two
    pins are read deliberately — which no manifest lookup can establish (see the
    vocabulary note at the top of this module). A producer declares them via
    ``save({"q0Anchor": "independent"})`` / ``save({"q0Anchor": "comparison",
    "q0Values": {...}})``.
    """
    environ = os.environ if env is None else env
    e = (environ.get("QOU_Q0_ANCHOR", "") or "").strip().lower()
    if e in ("ideal", "muon", "canonical"):
        anchor = "muon"
    elif e in ("physical", "proton", "experimental"):
        anchor = "proton"
    else:
        anchor = None
        try:
            man = json.loads(
                (_repo_root() / "computations" / "q0_anchor_manifest.json")
                .read_text(encoding="utf-8")
            )
            stem = Path(script_path).stem
            if stem in man.get("ideal_muon", []):
                anchor = "muon"
            elif stem in man.get("physical_proton", []):
                anchor = "proton"
            elif stem in man.get("ambiguous", []):
                anchor = "ambiguous"
        except Exception:  # noqa: BLE001
            anchor = None
        if anchor is None:
            anchor = "proton"  # runtime default: not-ideal_muon ⇒ proton
    return anchor, (_q0_value_for_anchor(anchor) if anchor in ("muon", "proton") else None)


def q0_anchor_is_declared(
    script_path: Union[str, Path], *, env: Optional[Mapping[str, str]] = None,
) -> bool:
    """Whether this producer's pin is POSITIVELY declared, vs merely defaulted.

    ``resolve_q0_anchor`` returns ``"proton"`` for any stem absent from
    ``q0_anchor_manifest.json`` — that is the runtime *default*, not evidence.
    The manifest lists ~309 of ~780 producers, so absence is the common case
    and says nothing about the real pin.

    Callers that want to *contradict* a recorded pin must gate on this: without
    a positive declaration there is no ground to overrule what a producer
    previously recorded, and doing so would strip legitimate ``muon`` labels
    from every unlisted producer.
    """
    environ = os.environ if env is None else env
    e = (environ.get("QOU_Q0_ANCHOR", "") or "").strip().lower()
    if e in ("ideal", "muon", "canonical", "physical", "proton", "experimental"):
        return True
    try:
        man = json.loads(
            (_repo_root() / "computations" / "q0_anchor_manifest.json")
            .read_text(encoding="utf-8")
        )
    except Exception:  # noqa: BLE001
        return False
    stem = Path(script_path).stem
    return any(stem in man.get(k, [])
               for k in ("ideal_muon", "physical_proton", "ambiguous"))


def _git_head_sha() -> str:
    """Return the current HEAD commit SHA."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(_repo_root()),
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception as exc:  # noqa: BLE001
        if not getattr(_git_head_sha, "_warned", False):
            print(
                f"[qou_substrate.witness] git rev-parse failed ({exc!r}); "
                "commitSha will serialise as 'unknown'. Common cause in "
                "fresh sandboxes: dubious-ownership refusal — run "
                "`git config --global --add safe.directory <repo-root>`.",
                file=sys.stderr,
            )
            _git_head_sha._warned = True  # type: ignore[attr-defined]
        return "unknown"


def _git_file_sha(path: str) -> str:
    """Return the last commit SHA that touched a given file. `git log` exits
    cleanly with empty stdout for paths that have never been committed
    (e.g. a script generating its first witness pre-commit), so empty
    output is also normalised to "unknown" — matching `_git_head_sha`.

    Per Copilot review on PR #484: never return an ambiguous empty
    string; "unknown" is the canonical sentinel and serialises into
    witness JSON as a clear marker rather than `""`.

    An *exception* (as opposed to empty output) means the git
    invocation itself failed — e.g. the sandbox's dubious-ownership
    refusal when the checkout is owned by another uid. That case is
    warned to stderr instead of being silently conflated with the
    legitimate "file not yet committed" case (2026-06-13)."""
    try:
        sha = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", path],
            cwd=str(_repo_root()),
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        return sha if sha else "unknown"
    except Exception as exc:  # noqa: BLE001
        if not getattr(_git_file_sha, "_warned", False):
            print(
                f"[qou_substrate.witness] git log failed for {path!r} "
                f"({exc!r}); scriptCommitSha will serialise as 'unknown'. "
                "Common cause in fresh sandboxes: dubious-ownership "
                "refusal — run `git config --global --add safe.directory "
                "<repo-root>`. (Warned once; further failures are "
                "silent.)",
                file=sys.stderr,
            )
            _git_file_sha._warned = True  # type: ignore[attr-defined]
        return "unknown"


def file_content_hash(path: str, length: int = 12) -> str:
    """SHA-256 content hash (hex prefix) of a file, matching lean-witness.ts."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:length]


# ── Environment capture (software/library versions) ──────────────

def capture_environment() -> dict:
    """Capture the interpreter + numeric-library versions that produced a
    witness.

    Recorded in every witness under ``environment`` so version-driven drift
    is *attributable* — e.g. a different mpmath/sympy build shifting q₀ at
    ~1e-8 and cascading into every derived mass is now visible in the
    witness rather than an unexplained diff. Versions are read from package
    metadata (no module imports forced); missing packages are simply
    omitted. The list is deliberately small (the libraries whose version
    actually affects numeric output).
    """
    import importlib.metadata as _md

    env: dict[str, str] = {"python": sys.version.split()[0]}
    for pkg in ("numpy", "scipy", "sympy", "mpmath", "pyhecke-native", "clarabel"):
        try:
            env[pkg.replace("-", "_")] = _md.version(pkg)
        except Exception:
            # Not installed / no metadata — omit rather than guess.
            pass

    # `pyhecke_native` is built from this repo's own `tools/hecke-engine`
    # and is NOT published, so its version string is a hand-maintained crate
    # number, not a release identifier. Measured: across 21 commits to
    # `hecke-engine` and 2 to `pyhecke-native` between 2026-08-11 and
    # 2026-08-21 — including flipping `trace_weights` to `h*z^2 + z` and
    # enabling native dispatch on convention D, both of which move numbers —
    # the recorded versions never left `0.9.0` / `0.8.0`.
    #
    # So for the one dependency whose code lives in this repo, the block
    # above is blind in exactly the case it exists to catch. That is not
    # hypothetical: `atomic_tr_m_mpfr_50dps` fails to reproduce its
    # committed tr_M by ~40.7 ppb with an `environment` block matching the
    # committing run *exactly*, and seven other candidate causes are refuted
    # by measurement (bean `qou-ibbr`). A matching environment was read as
    # evidence the compute was the same; it is only evidence the provenance
    # cannot tell.
    #
    # The compiled object is content-addressed instead, which needs no
    # cooperation from the Rust side and cannot drift from what actually ran.
    h = _pyhecke_native_build_hash()
    if h:
        env["pyhecke_native_build"] = h
    return env


_PYHECKE_NATIVE_BUILD_HASH: Optional[str] = None


def _pyhecke_native_build_hash() -> Optional[str]:
    """sha256 prefix of the compiled `pyhecke_native` extension, or None.

    Located via `find_spec` so the module is never imported just to record
    provenance (the same restraint `capture_environment` shows for the
    version reads). Cached: the file cannot change within a process, and
    hashing ~3 MB per witness would otherwise be pure waste.
    """
    global _PYHECKE_NATIVE_BUILD_HASH
    if _PYHECKE_NATIVE_BUILD_HASH is not None:
        return _PYHECKE_NATIVE_BUILD_HASH or None
    _PYHECKE_NATIVE_BUILD_HASH = ""  # negative-cache; "" is falsy
    try:
        import hashlib as _hl  # noqa: PLC0415
        import importlib.util as _iu  # noqa: PLC0415

        spec = _iu.find_spec("pyhecke_native")
        if spec is None:
            return None
        roots = list(spec.submodule_search_locations or [])
        if not roots and spec.origin:
            roots = [str(Path(spec.origin).parent)]
        for root in roots:
            for so in sorted(Path(root).rglob("*.so")):
                _PYHECKE_NATIVE_BUILD_HASH = _hl.sha256(
                    so.read_bytes()).hexdigest()[:16]
                return _PYHECKE_NATIVE_BUILD_HASH
    except Exception:  # noqa: BLE001 — provenance never breaks a producer
        pass
    return None


# ── Upstream-witness hash recording (anti-staleness) ────────────

def load_and_hash_upstream(path: Union[str, Path]) -> tuple[dict, dict]:
    """Load an upstream witness file and return (body, hash_record).

    The hash_record is the data a downstream consumer needs to verify
    it has the same upstream as when its own witness was last
    regenerated: file sha256, commitSha, scriptCommitSha, computedAt.

    See ``witness_dependency_drift.py`` for the validator that walks
    ``upstream_witness_hashes`` arrays and reports staleness.
    See ``docs/audits/2026-05-16-stale-witness-infra-gap.md`` for
    the adoption pattern.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"Required upstream witness not found: {p}\n"
            f"Run its producer first."
        )
    raw = p.read_bytes()
    body = json.loads(raw.decode("utf-8"))
    return body, {
        "path":            p.name,
        "sha256":          hashlib.sha256(raw).hexdigest(),
        "size_bytes":      len(raw),
        "commitSha":       body.get("commitSha"),
        "scriptCommitSha": body.get("scriptCommitSha"),
        "computedAt":      body.get("computedAt"),
    }


def record_upstream(path: Union[str, Path], into: list) -> dict:
    """Load an upstream witness and append its hash record to ``into``.

    ``WitnessBuilder.add_upstream`` is a *method*, so it can only be used once
    a builder exists. A survey of this corpus found that 290 of 330 producers
    that consume a witness read it **before** constructing their builder — the
    prevailing shape is "read the inputs at the top, build the witness at the
    bottom". That ordering, not oversight, is why ``add_upstream`` adoption sat
    at 5.7%: the API asked for a structure most producers do not have.

    This function closes that gap without a restructure::

        _UP: list = []
        q0 = mpf(record_upstream(Q_PIN, _UP)["derived_50_digit"]["q"])
        ...
        w = WitnessBuilder("my-witness").add_upstream_records(_UP)

    **The list is the caller's, deliberately.** The obvious alternative — a
    module-level accumulator that ``WitnessBuilder`` drains on construction —
    is unsafe in two entirely ordinary situations: producer P imports Q, and
    Q recorded upstreams at *its* import time, so P's builder drains and
    claims Q's records; or a test imports a producer for its symbols and any
    later builder inherits them. Both silently attach the wrong provenance,
    which is the precise failure this metadata exists to detect. Passing an
    explicit list makes that class of bug unrepresentable: a record can only
    reach the witness whose author named the list.

    Returns the parsed body, so it is a drop-in for
    ``json.loads(path.read_text())`` at the call site.
    """
    body, hash_record = load_and_hash_upstream(path)
    into.append(hash_record)
    return body


# ── Assertion type ───────────────────────────────────────────────

class Assertion:
    """A single named claim with computed vs expected values."""

    def __init__(
        self,
        name: str,
        computed: Union[float, str],
        expected: Union[float, str],
        tolerance: Union[float, str, None] = None,
        unit: Optional[str] = None,
        source: Optional[str] = None,
        passed_override: Optional[bool] = None,
        extra: Optional[dict] = None,
    ):
        self.name = name
        self.computed = computed
        self.expected = expected
        self.tolerance = tolerance
        self.unit = unit
        self.source = source
        # A verdict the producer computed itself, rather than one derived from
        # computed/expected/tolerance. Legacy payload assertions are frequently
        # of the form {"name": …, "passed": bool(some_predicate)} with no
        # numeric pair to compare — the predicate IS the check. Honoured
        # verbatim so adoption cannot change a producer's stated result.
        self.passed_override = passed_override
        # Keys the corpus attaches beyond the schema (`detail`, `manifold`,
        # `particle`, …). Preserved so adoption is lossless.
        self.extra = dict(extra) if extra else {}

    @property
    def passed(self) -> bool:
        if self.passed_override is not None:
            return self.passed_override
        if self.tolerance is None:
            return self.computed == self.expected
        try:
            # `float()` on the tolerance too: producers draining raw float64
            # (qou-t0rf) pass computed/expected/tolerance as precision-preserving
            # STRINGS, and a str tolerance would otherwise make `<=` raise and
            # silently fall through to string equality — a wrong verdict, not an
            # error. Coercing here keeps the numeric check numeric.
            return abs(float(self.computed) - float(self.expected)) <= float(self.tolerance)
        except (ValueError, TypeError):
            return str(self.computed) == str(self.expected)

    def to_dict(self) -> dict:
        d: dict[str, Any] = {
            "name": self.name,
            "computed": self.computed,
            "expected": self.expected,
            "passed": self.passed,
        }
        if self.tolerance is not None:
            d["tolerance"] = self.tolerance
        if self.unit:
            d["unit"] = self.unit
        if self.source:
            d["source"] = self.source
        # Adopted extras last, and they may not shadow a schema key.
        for k, v in self.extra.items():
            if k not in d:
                d[k] = v
        return d


def _assertion_from_mapping(rec: Mapping[str, Any]) -> "Assertion":
    """Build an `Assertion` from a legacy payload assertion dict.

    `wrap_legacy` used to DROP these (see its docstring), so this is the
    conversion that makes them count. Handles the shapes the corpus actually
    uses, surveyed across the 28 affected producers:

    * ``{"name", "passed"}`` — 11 sites. No numeric pair; the producer's own
      predicate is the verdict, so it becomes `passed_override`.
    * ``{"name", "computed", "expected", "passed", …}`` — 5 sites. Both are
      present; the explicit `passed` still wins, because it is what the
      producer asserted and adoption must not silently re-decide a verdict.
    * ``{"name", "expected", "tolerance", "unit", "source", …}`` — 10 sites,
      no `passed`; derived the normal way from computed/expected/tolerance.

    Anything else on the dict (``detail``, ``manifold``, ``particle``) is
    carried through in `extra` rather than discarded.
    """
    known = {"name", "computed", "expected", "passed", "tolerance",
             "unit", "source"}
    passed = rec.get("passed")
    return Assertion(
        name=str(rec.get("name", "")),
        # A missing computed/expected pair is rendered against the verdict so
        # the emitted assertion is still readable, rather than carrying `None`.
        computed=rec.get("computed",
                         ("1" if passed else "0") if passed is not None else ""),
        expected=rec.get("expected", "1" if passed is not None else ""),
        tolerance=rec.get("tolerance"),
        unit=rec.get("unit"),
        source=rec.get("source"),
        passed_override=bool(passed) if passed is not None else None,
        extra={k: v for k, v in rec.items() if k not in known},
    )


# ── WitnessBuilder ───────────────────────────────────────────────

# ── Raw-float64 guard (qou-t0rf) ──────────────────────────────────
#
# Every witness in this corpus is written through `WitnessBuilder.save`,
# which makes it the one place a raw Python float can be stopped before
# it reaches JSON. `computations/witness_raw_float64_audit.py` catches
# these after the fact and has been red on `main` with a backlog fed by
# several independent sessions; a check here is what prevents NEW ones.
#
# Deliberately OFF by default so this is not a breaking change while the
# backlog is drained. Flip it on in CI (and eventually by default) once
# the audit is green:
#
#     QOU_WITNESS_STRICT_FLOAT64=warn     report offending paths to stderr
#     QOU_WITNESS_STRICT_FLOAT64=1        raise ValueError
#
# The fix a producer should make is never to stringify the float — that
# is laundering, and `witness_float64_padding_audit.py` catches it. Carry
# `mpmath.mpf` from the source and serialize with `_precision.fmt`.

def _raw_float_paths(obj, path=""):
    """Yield JSON paths of every raw (non-integer-valued) float in `obj`."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _raw_float_paths(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            yield from _raw_float_paths(v, f"{path}[{i}]")
    elif isinstance(obj, float) and not isinstance(obj, bool):
        yield path


def _check_raw_float64(witness: dict, name: str) -> None:
    """Guard the single point where a witness is written.

    DEFAULT IS NOW `warn`, not off. The ratchet backlog it was staged behind
    has cleared — `witness_raw_float64_audit.py --strict` reports 0 NEW and 0
    REGRESSED and exits 0 — so a producer that starts emitting raw float64
    should say so at the moment it does it, not a CI run later.

    `warn` and not `raise`, deliberately: ~1580 baseline witnesses still carry
    float64 from before the ratchet, and defaulting to `raise` would break
    every one of their producers on re-run for a debt they are not adding to.
    The audit gate is what ENFORCES (it fails CI on any new or regressed file);
    this is what LOCATES, printing the exact JSON paths at the producer.

      QOU_WITNESS_STRICT_FLOAT64=1     raise — use in CI and when draining
      QOU_WITNESS_STRICT_FLOAT64=warn  print to stderr (the default)
      QOU_WITNESS_STRICT_FLOAT64=0     silence entirely
    """
    mode = os.environ.get("QOU_WITNESS_STRICT_FLOAT64", "warn").strip().lower()
    if mode in ("0", "off", "false"):
        return
    if mode == "":
        mode = "warn"
    paths = list(_raw_float_paths(witness))
    if not paths:
        return
    head = ", ".join(paths[:8]) + (" …" if len(paths) > 8 else "")
    msg = (f"{name}: {len(paths)} raw float64 field(s) would enter the "
           f"witness — {head}. Carry mpmath.mpf from the source and "
           f"serialize with _precision.fmt; do NOT stringify the float.")
    if mode in ("warn", "warning"):
        print(f"⚠ raw-float64: {msg}", file=sys.stderr)
    else:
        raise ValueError(f"raw-float64 guard: {msg}")


# ── Non-finite guard (NaN / Infinity) ───────────────────────────────
#
# `json.dump` emits bare `NaN`, `Infinity` and `-Infinity` by default. **JSON
# has no such tokens** (RFC 8259 numbers are finite decimals), so a witness
# containing one is not valid JSON and a strict parser rejects the whole file.
# Python's own loader accepts them, which is why this goes unnoticed: the
# producer round-trips its own output happily and only a non-Python consumer
# discovers the file is unreadable.
#
# Found by the 2026-08-09 sweep: 25 witnesses under `computations/` fail
# `json.load(..., parse_constant=raise)` — 20 live and 5 deprecated.
#
# Same shape as the raw-float64 guard above, deliberately: `warn` by default
# so this is not a breaking change while the existing ones are re-run, `=1` to
# raise in CI and when fixing a producer.
#
#     QOU_WITNESS_STRICT_NONFINITE=warn   report offending paths (default)
#     QOU_WITNESS_STRICT_NONFINITE=1      raise ValueError
#     QOU_WITNESS_STRICT_NONFINITE=0      silence entirely
#
# The fix is NOT to stringify the NaN and move on. A NaN in a witness is
# normally a 0/0 or an empty reduction that the producer did not notice; decide
# what the value should be, or record it as null with a caveat saying why.

def _nonfinite_paths(obj, path=""):
    """Yield JSON paths of every NaN / +-Infinity float in `obj`."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _nonfinite_paths(v, f"{path}.{k}")
    elif isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            yield from _nonfinite_paths(v, f"{path}[{i}]")
    elif isinstance(obj, float) and not isinstance(obj, bool):
        if obj != obj or obj in (float("inf"), float("-inf")):
            yield path


def _version_tuple(v: str) -> tuple:
    """Leading dotted-numeric prefix of a version string, for ordering.

    `"1.4.1" -> (1, 4, 1)`; `"0.11.1" -> (0, 11, 1)`. Stops at the first
    non-numeric component, so `"1.3.0rc2"` compares as `(1, 3)` — deliberately
    coarse. This decides only whether to PRINT a warning, so a tie on a
    pre-release suffix costs nothing, whereas guessing at PEP 440 ordering
    here would add a dependency and a new way to be wrong.
    """
    out: list[int] = []
    for part in str(v).split("."):
        digits = ""
        for ch in part:
            if not ch.isdigit():
                break
            digits += ch
        if not digits:
            break
        out.append(int(digits))
        if digits != part:
            break
    return tuple(out)


def _environment_delta(old, new) -> dict:
    """Compare two `environment` blocks. Returns the four-way delta.

    Split out of `_check_environment_regression` so `save()` can ask the
    same question on the *preserve* path, where no write happens and the
    guard therefore never used to run at all.

    `weaker` is deliberately dominant: a block that both drops one library
    and adds another is treated as a regression, not a repair. Losing a
    recorded library is provenance damage whatever else came with it.
    """
    if not isinstance(old, dict) or not isinstance(new, dict):
        return {"stripped": [], "downgraded": [], "added": [], "upgraded": []}
    stripped = [k for k in old if k not in new]
    downgraded = [
        f"{k} {old[k]} -> {new[k]}"
        for k in old
        if k in new and old[k] != new[k]
        and _version_tuple(new[k]) < _version_tuple(old[k])
    ]
    added = [k for k in new if k not in old]
    upgraded = [
        f"{k} {old[k]} -> {new[k]}"
        for k in old
        if k in new and old[k] != new[k]
        and _version_tuple(new[k]) > _version_tuple(old[k])
    ]
    return {"stripped": stripped, "downgraded": downgraded,
            "added": added, "upgraded": upgraded}


def _environment_is_repair(old, new) -> bool:
    """True iff `new` is strictly STRONGER provenance than `old`.

    Strictly stronger = nothing dropped, nothing downgraded, and at least
    one library added or upgraded. That monotonicity is what makes it safe
    to write on the otherwise-preserve path: only upward moves write, so
    two containers alternating cannot ping-pong the file (the weaker one
    never writes), and a repair write is idempotent once applied.
    """
    d = _environment_delta(old, new)
    if d["stripped"] or d["downgraded"]:
        return False
    return bool(d["added"] or d["upgraded"])


def _check_environment_regression(witness: dict, existing, name: str,
                                  preserved: bool = False) -> None:
    """Warn when a re-run RECORDS LESS than the witness already on disk.

    The `environment` block is provenance: it says which libraries produced
    the numbers. Re-running a producer in a container that is missing one of
    them, or carrying an older version, silently rewrites that record — the
    numbers may be untouched while the file now claims they came from a
    weaker environment than they did.

    History (bean `qou-y0xk`). `rho-k-co-casimir-extended` was regenerated on
    convention D in a container lacking `scipy` and `clarabel` and carrying
    `mpmath 1.3.0` against the recorded `1.4.1`, and the stripped block was
    merged. The re-run with the environment restored changed **zero** physics
    fields — so the loss was pure provenance damage, which is exactly the kind
    that survives review: nothing looks wrong in the numbers. The same class
    was caught the same day on `derivation-chain-audit`, where an agent
    correctly declined to commit.

    WARN-ONLY, and deliberately so. A dropped library is sometimes legitimate
    (a producer stops using it) and only the agent can tell which case this
    is. What the check removes is the *silence*: the regression is now stated
    at write time rather than discovered in a diff, or not at all. Set
    `QOU_WITNESS_STRICT_ENV=error` to escalate, `off` to silence.
    """
    mode = os.environ.get("QOU_WITNESS_STRICT_ENV", "warn").strip().lower()
    if mode in ("0", "off", "false"):
        return
    if not isinstance(existing, dict):
        return
    old = existing.get("environment")
    new = witness.get("environment")
    if not isinstance(old, dict) or not isinstance(new, dict):
        return

    delta = _environment_delta(old, new)
    stripped, downgraded = delta["stripped"], delta["downgraded"]
    if not stripped and not downgraded:
        return

    bits = []
    if stripped:
        bits.append(f"dropped {', '.join(sorted(stripped))}")
    if downgraded:
        bits.append(f"downgraded {'; '.join(sorted(downgraded))}")

    if preserved:
        # Nothing was written: the payload matched, so the STRONGER on-disk
        # block was kept. Saying "rather than committing the weaker record"
        # here would describe a write that did not happen.
        msg = (f"{name}: this container would record LESS than the witness on "
               f"disk — {'; '.join(bits)}. The file was NOT modified and its "
               f"stronger environment block was kept. Nothing to commit; but "
               f"any OTHER witness you regenerate here will carry the weaker "
               f"record, so install the missing libraries before a batch run.")
    else:
        msg = (f"{name}: the environment block records LESS than the witness on "
               f"disk — {'; '.join(bits)}. If this container is simply missing a "
               f"library, install it and re-run rather than committing the "
               f"weaker record; the numbers can be identical while the provenance "
               f"silently degrades. If the producer genuinely stopped using it, "
               f"say so in the commit.")
    if mode in ("warn", "warning", ""):
        print(f"⚠ environment: {msg}", file=sys.stderr)
    else:
        raise ValueError(f"environment guard: {msg}")


def _check_nonfinite(witness: dict, name: str) -> None:
    """Guard the single point where a witness is written. See the note above."""
    mode = os.environ.get("QOU_WITNESS_STRICT_NONFINITE", "warn").strip().lower()
    if mode in ("0", "off", "false"):
        return
    if mode == "":
        mode = "warn"
    paths = list(_nonfinite_paths(witness))
    if not paths:
        return
    head = ", ".join(paths[:8]) + (" \u2026" if len(paths) > 8 else "")
    msg = (f"{name}: {len(paths)} non-finite value(s) (NaN/Infinity) would "
           f"enter the witness — {head}. JSON has no such token, so the file "
           f"will not parse under a strict loader. Decide the value or record "
           f"null with a caveat; do not stringify it and move on.")
    if mode in ("warn", "warning"):
        print(f"\u26a0 non-finite: {msg}", file=sys.stderr)
    else:
        raise ValueError(f"non-finite guard: {msg}")


class WitnessBuilder:
    """
    Build a structured witness JSON conforming to ComputationWitness.

    Automatically captures:
      - Git commit SHA (HEAD and script file)
      - Script content hash (for staleness detection)
      - Timestamp
      - Engine and version
      - Execution duration

    Parameters
    ----------
    name : str
        Computation name (becomes the filename: `<name>.witness.json`).
    engine : str
        One of: "sympy", "mpmath", "snappea", "sage", "numpy", "python".
    engine_version : str, optional
        Explicit version string. Auto-detected if omitted.
    output_dir : str or Path, optional
        Directory for the witness file. Defaults to the directory of
        the calling script.
    """

    def __init__(
        self,
        name: str,
        engine: str = "python",
        engine_version: Optional[str] = None,
        output_dir: Optional[Union[str, Path]] = None,
        start_time: Optional[float] = None,
        _script_path: Optional[Union[str, Path]] = None,
    ):
        self.name = name
        self.engine = engine
        self.engine_version = engine_version or self._detect_version(engine)
        # `start_time` lets callers pre-stamp the duration baseline at
        # the *start* of an expensive computation, then construct the
        # builder later (e.g. via `wrap_legacy`) without losing the
        # measurement. Falls back to "now" for builders constructed
        # before the work begins (the original pattern).
        self._start_time = (
            start_time if start_time is not None else time.monotonic()
        )
        # Which clock `_start_time` is on. `build()` differences against
        # `time.monotonic()`, whose zero is arbitrary (typically boot), while
        # 14 producers pass a `time.time()` baseline — epoch seconds, ~1.79e9.
        # Differencing those two clocks yielded `durationMs ≈ -1.79e12` in 12
        # committed witnesses (found by Copilot review on PR #4928).
        #
        # Fixed here rather than in the 14 callers: the parameter is documented
        # only as "the duration baseline", names no clock, and both clocks are
        # plain floats — so nothing distinguishes a right call from a wrong one
        # at the call site. Fourteen identical mistakes against 215 correct ones
        # is a footgun, not fourteen slips.
        #
        # The discriminator is safe by a wide margin: `time.monotonic()` counts
        # from an arbitrary but *recent* zero (uptime — 1e8 s is over 3 years of
        # continuous uptime), while `time.time()` has been above 1e9 since 2001.
        self._start_is_epoch = (
            start_time is not None and start_time > 1e8
        )

        # Resolve caller frame ONLY when script path not explicitly
        # provided (factory classmethods like ``wrap_legacy`` pass it
        # in directly so they don't capture witness_base.py itself).
        if _script_path is not None:
            caller_file = Path(_script_path).resolve()
        else:
            import inspect
            caller_frame = inspect.stack()[1]
            caller_file = Path(caller_frame.filename).resolve()
        self._script_path = caller_file

        # Determine output directory
        if output_dir:
            self._output_dir = Path(output_dir)
        else:
            self._output_dir = caller_file.parent

        self.description: Optional[str] = None
        self.content_block: Optional[str] = None
        self.audit_only: Optional[str] = None
        self.assertions: list[Assertion] = []
        self.parameters: dict[str, Any] = {}
        self.data: dict[str, Any] = {}
        self.caveats: list[str] = []
        # Anti-staleness hashes for every upstream witness this
        # builder's caller has consumed.  Populated via
        # ``add_upstream(path)``; emitted by ``build()`` under
        # ``data.upstream_witness_hashes`` for the drift validator
        # (``witness_dependency_drift.py``) to walk.
        self._upstream_hashes: list[dict] = []
        # Extra top-level keys (used by wrap_legacy to preserve the
        # original flat layout of hand-written witnesses during P30
        # migration). Merged in by ``build()`` after the structured
        # fields, so structured values win on key collision.
        self._extra_top_level: dict[str, Any] = {}

    @staticmethod
    def _detect_version(engine: str) -> str:
        """Auto-detect engine version."""
        try:
            if engine == "sympy":
                import sympy
                return f"sympy {sympy.__version__}"
            elif engine == "mpmath":
                import mpmath
                return f"mpmath {mpmath.__version__}"
            elif engine in ("snappea", "snappy"):
                import snappy
                return f"snappy {snappy.version()}"
            elif engine == "sage":
                return "sage (version not detected)"
            elif engine == "numpy":
                import numpy
                return f"numpy {numpy.__version__}"
            else:
                return f"python {sys.version.split()[0]}"
        except ImportError:
            return f"{engine} (not installed)"

    def set_description(self, desc: str) -> "WitnessBuilder":
        """Set the human-readable description."""
        self.description = desc
        return self

    def set_content_block(self, label: str) -> "WitnessBuilder":
        """Link this witness to a content block label (e.g. 'prop:foo')."""
        self.content_block = label
        return self

    def set_audit_only(self, report_path: str) -> "WitnessBuilder":
        """Mark this witness as audit-only — produced by an audit/probe whose
        report lives in ``docs/audits/*.md`` and which is **not expected** to
        wire to a content block via ``computation.witness``.

        Setting this field excludes the witness from the orphan tally
        computed by ``scripts/audit-wiring.ts``.

        Parameters
        ----------
        report_path : str
            Path to the audit report (typically
            ``docs/audits/YYYY-MM-DD-<slug>.md``), relative to repo root.

        Examples
        --------
        ::

            w = WitnessBuilder("path-b-evacuation", engine="numpy")
            w.set_audit_only("docs/audits/2026-05-06-path-b-evacuation.md")
            ... # compute
            w.save()
        """
        self.audit_only = report_path
        return self

    def add_assertion(
        self,
        name: str,
        computed: Union[float, str],
        expected: Union[float, str],
        tolerance: Union[float, str, None] = None,
        unit: Optional[str] = None,
        source: Optional[str] = None,
    ) -> "WitnessBuilder":
        """Add a named assertion. Pass `computed`/`expected`/`tolerance` as
        STRINGS to keep a value out of float64 — that is the drained convention
        (qou-t0rf); `passed` coerces with `float()` either way."""
        self.assertions.append(
            Assertion(name, computed, expected, tolerance, unit, source)
        )
        return self

    def add_parameter(self, key: str, value: Any) -> "WitnessBuilder":
        """Record an input parameter."""
        self.parameters[key] = value
        return self

    def add_data(self, key: str, value: Any) -> "WitnessBuilder":
        """Attach arbitrary computation data."""
        self.data[key] = value
        return self

    def add_caveat(self, text: str) -> "WitnessBuilder":
        """Add a caveat or limitation note."""
        self.caveats.append(text)
        return self

    def add_upstream(self, path: Union[str, Path]) -> dict:
        """Load an upstream witness file, record its hash, return body.

        Replaces ``json.loads(path.read_text())`` at the call site
        while accumulating the sha256 + commit-SHA + computedAt of
        every upstream consumed.  The accumulated list is emitted by
        ``build()`` under ``data.upstream_witness_hashes`` for the
        drift validator ``witness_dependency_drift.py`` to walk.

        See ``docs/audits/2026-05-16-stale-witness-infra-gap.md`` for
        the rationale.
        """
        body, hash_record = load_and_hash_upstream(path)
        self._upstream_hashes.append(hash_record)
        return body

    def add_upstream_records(self, records: list) -> "WitnessBuilder":
        """Attach upstream hash records captured before this builder existed.

        The companion to the module-level ``record_upstream`` below. See its
        docstring for why the pair exists.

        Idempotent by ``(path, sha256)``: re-attaching the same list, or a list
        that overlaps with upstreams already declared through ``add_upstream``,
        cannot duplicate an edge. Producers that both record early and declare
        late therefore stay correct.
        """
        seen = {(r.get("path"), r.get("sha256")) for r in self._upstream_hashes}
        for r in records or []:
            key = (r.get("path"), r.get("sha256"))
            if key not in seen:
                seen.add(key)
                self._upstream_hashes.append(r)
        return self

    # ── Reserved structured keys used by ``wrap_legacy`` ─────────
    # Keys that are routed to dedicated WitnessBuilder slots rather
    # than being preserved as raw top-level fields. Anything else in
    # the legacy payload is kept verbatim under ``_extra_top_level``.
    _RESERVED_LEGACY_KEYS = frozenset({
        "computation",
        "description",
        "contentBlock",
        "auditOnly",
        "engine",
        "engineVersion",
        "computedAt",
        "commitSha",
        "scriptFile",
        "scriptHash",
        "scriptCommitSha",
        "durationMs",
        "allPassed",
        "assertions",
    })

    @classmethod
    def wrap_legacy(
        cls,
        name: str,
        payload: Mapping[str, Any],
        *,
        script_path: Union[str, Path],
        engine: str = "python",
        engine_version: Optional[str] = None,
        output_dir: Optional[Union[str, Path]] = None,
        start_time: Optional[float] = None,
    ) -> "WitnessBuilder":
        """Wrap a legacy hand-written witness payload.

        Migrates a pre-existing ``json.dump(out_dict, f)`` writer to
        the ``WitnessBuilder`` API **without** changing the on-disk
        layout: every original top-level key is preserved verbatim,
        and the structured fields ``scriptHash``, ``scriptCommitSha``,
        ``engine``, ``engineVersion``, ``computedAt``, and
        ``durationMs`` are added so that ``run_pipeline.py`` can
        detect staleness (P30 in the compute-audit catalogue).

        Reserved keys (``description``, ``auditOnly``, etc.) are
        routed to their structured slots; everything else is held in
        ``_extra_top_level`` and emitted verbatim by ``build()``.

        Parameters
        ----------
        name : str
            Witness filename stem (becomes ``<name>.witness.json``).
        payload : Mapping[str, Any]
            The dict the legacy script was dumping with ``json.dump``.
        script_path : str or Path
            Absolute path to the calling script. Required because
            ``wrap_legacy`` is a classmethod and cannot reliably
            inspect the caller frame.
        engine, engine_version, output_dir
            Same as the constructor.

        Returns
        -------
        WitnessBuilder
            A builder whose ``save()`` will produce a witness JSON
            that contains every original key plus the staleness
            metadata. Bit-equivalence on the original keys is
            preserved.

        Example
        -------
        ::

            out = {"computation": "my-thing", "description": "...", ...}
            (WitnessBuilder.wrap_legacy(
                "my-thing", out, script_path=__file__,
                engine="mpmath",
            )
                .set_audit_only("docs/audits/2026-05-08-compute-audit-workplan.md")
                .save())
        """
        # Use the explicit script_path; engine_version is auto-detected
        # if not supplied. `start_time` lets the caller pre-stamp the
        # duration baseline (taken at the start of the heavy compute,
        # before `wrap_legacy` is invoked) so `durationMs` reflects
        # real runtime rather than just the save step.
        builder = cls(
            name=name,
            engine=engine,
            engine_version=engine_version,
            output_dir=output_dir,
            start_time=start_time,
            _script_path=script_path,
        )
        for key, value in payload.items():
            if key == "description" and isinstance(value, str):
                builder.set_description(value)
            elif key == "contentBlock" and isinstance(value, str):
                builder.set_content_block(value)
            elif key == "auditOnly" and isinstance(value, str):
                builder.set_audit_only(value)
            elif key == "computation":
                # ADOPT a value that is not simply the name; skip only the
                # redundant case.
                #
                # `build()` sets `computation = self.name`, so a payload
                # `computation` key does not survive: the key remains and its
                # VALUE is replaced. A key-set diff therefore shows NO loss,
                # which is what made this invisible.
                #
                # The old rationale — "filename already encodes this" — holds
                # when the value IS the name, and measured on main that is the
                # overwhelming case: of 188 payload `computation` keys, 146 are
                # the witness name and 32 the script stem or path, all of which
                # the clobber reproduces or normalises. Skipping those is right
                # and is preserved below.
                #
                # It does NOT hold when the producer put something else there.
                # Seven producers pass a structured dict — `engine`, `dps`,
                # `script`, `reads`, and in one case `C_n_eps`, a computed
                # constant. Checking the committed witnesses, `dps` and
                # `script` survive under other fields, but `C_n_eps`
                # (dilog-archimedean-limit-partA) and `reads`
                # (lever1-binding-core-characterization,
                # lever1-binding-core-root-distribution) appear NOWHERE in the
                # emitted witness. `reads` is upstream-dependency provenance,
                # so its loss is load-bearing for staleness tracking.
                #
                # Adopting rather than raising mirrors the `assertions` fix
                # directly above (bean qou-l5zi) and breaks no producer: every
                # name-valued case still takes the `continue`.
                _norm = lambda t: _re.sub(r"[^a-z0-9]", "", str(t).lower())
                if isinstance(value, str) and (
                        _norm(value) == _norm(name)
                        or _norm(value) == _norm(Path(str(script_path)).stem)
                        or value.endswith(".py")):
                    continue
                # Anything else carries content the name cannot. Preserve it
                # under a key `build()` does not overwrite, and say so, so a
                # producer writing a fresh payload learns at once rather than
                # discovering it in a diff.
                builder._extra_top_level.setdefault("computationDetail", value)
                _warnings.warn(
                    f"wrap_legacy({name!r}): the payload's `computation` value "
                    "is not the witness name, and `build()` overwrites that "
                    "field with the name. It has been preserved as "
                    "`computationDetail`. Write it under your own key to "
                    "silence this.",
                    UserWarning, stacklevel=3,
                )
                continue
            elif key == "assertions" and isinstance(value, list):
                # ADOPT, do not skip. `assertions` and `allPassed` are in
                # `_RESERVED_LEGACY_KEYS`, so both used to fall through to the
                # `continue` below on the reasoning that `build()` recomputes
                # them from `add_assertion`. For a producer that writes its
                # checks as a payload literal — the prevailing legacy shape —
                # that silently DISCARDED them, and `build()` then emitted
                #
                #     "assertions": [], "allPassed": true
                #
                # with `allPassed` true *vacuously*, because nothing was
                # registered. No warning, no exception: a probe whose headline
                # check FAILED reported success.
                #
                # Measured before the fix: 29 producers passed `assertions` in a
                # wrap_legacy payload, 28 of them without also calling
                # `add_assertion`; 389 of 2083 witnesses carrying an `allPassed`
                # field (19 %) had it true with zero assertions.
                #
                # Adopting rather than raising is deliberate. The producer's
                # verdict was never wrong — it was discarded — so converting it
                # is a faithful reading of what the caller asked for, and it
                # repairs all 28 without a flag day. An explicit `passed` in the
                # payload always wins over a derived comparison, so adoption
                # cannot re-decide a result.
                for _rec in value:
                    if isinstance(_rec, Mapping):
                        builder.assertions.append(_assertion_from_mapping(_rec))
                continue
            elif key in cls._RESERVED_LEGACY_KEYS:
                # Skip auto-generated metadata; build() will recompute
                continue
            else:
                builder._extra_top_level[key] = value
        return builder

    @staticmethod
    def stamp_staleness_metadata(
        payload: dict,
        *,
        script_path: Union[str, Path],
        engine: str = "python",
        engine_version: Optional[str] = None,
        q0_anchor: Optional[str] = None,
        q0_value: Optional[str] = None,
    ) -> dict:
        """Public helper: stamp the WitnessBuilder staleness fields onto
        an existing dict in place (used when the legacy filename is
        non-standard and ``wrap_legacy().save()`` cannot be applied
        without breaking consumers).

        Mutates and returns ``payload`` with ``scriptHash``,
        ``scriptCommitSha``, ``commitSha``, ``engine``, ``engineVersion``,
        ``computedAt``, and ``durationMs`` set. Avoids the need to
        import the underscore-prefixed ``_git_head_sha`` /
        ``_git_file_sha`` helpers from outside this module.
        """
        spath = str(script_path)
        payload["scriptHash"] = file_content_hash(spath)
        payload["scriptCommitSha"] = _git_file_sha(spath)
        payload["commitSha"] = _git_head_sha()
        payload["engine"] = engine
        payload["computedAt"] = datetime.now(timezone.utc).isoformat()
        payload["durationMs"] = 0
        if engine_version is None:
            # Mirror the auto-detection logic in __init__
            try:
                if engine == "mpmath":
                    import mpmath
                    engine_version = f"mpmath {mpmath.__version__}"
                elif engine == "sympy":
                    import sympy
                    engine_version = f"sympy {sympy.__version__}"
                elif engine == "python+mpmath":
                    import mpmath
                    engine_version = (
                        f"python {sys.version_info.major}."
                        f"{sys.version_info.minor} + "
                        f"mpmath {mpmath.__version__}"
                    )
            except Exception:
                pass
        if engine_version is not None:
            payload["engineVersion"] = engine_version
        # q₀-anchor provenance: make the muon/proton pin explicit so the value
        # can never be silently misread (bean tnjb flip-flop). Auto-resolved from
        # the manifest + env unless the caller passes an explicit anchor/value.
        if q0_anchor is None:
            q0_anchor, _rv = resolve_q0_anchor(spath)
            if q0_value is None:
                q0_value = _rv
        # A q0Anchor the producer already wrote into the payload WINS over the
        # one resolved from the manifest/env. `build()` has always had this
        # guard (`if "q0Anchor" not in witness`); this path did not, so the two
        # writers of one field disagreed, and this one silently relabelled an
        # explicit declaration. A producer that spans both layers on purpose --
        # e.g. `markov/peel_anchor_identification_probe.py`, whose whole subject
        # is telling the pins apart -- declares `q0Anchor: "ambiguous"`, a
        # category the anchor audit has precisely for this, and got "proton"
        # stamped over it from the running script's manifest entry. That is the
        # exact failure mode the field exists to prevent: a witness asserting a
        # pin its contents do not carry.
        #
        # An explicit `q0_anchor=` argument still wins over both, since a caller
        # passing it is making the same declaration one call frame out.
        if "q0Anchor" not in payload:
            payload["q0Anchor"] = q0_anchor
            if q0_value is not None:
                payload["q0Value"] = q0_value
        return payload

    def is_fresh(self) -> bool:
        """Return True if an existing witness JSON on disk records the
        same script content hash as the current source.

        Use this to short-circuit expensive recomputations::

            w = WitnessBuilder("my-computation", engine="sympy")
            if w.is_fresh():
                print(f"✓ {w.name}.witness.json fresh; skipping")
                return
            ... # expensive compute
            w.add_assertion(...)
            w.save()

        Returns False if the witness file does not exist, is malformed,
        or records a different `scriptHash`.
        """
        out_path = self._output_dir / f"{self.name}.witness.json"
        if not out_path.is_file():
            return False
        try:
            with out_path.open("r", encoding="utf-8") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, OSError):
            return False
        current_hash = file_content_hash(str(self._script_path))
        return existing.get("scriptHash") == current_hash

    def _capture_invocation(self) -> dict:
        """Record how this producer was invoked, per `qou-nok3`.

        Returns ``{"argv": [...], "reproduce": "..."}``. ``argv[0]`` is
        rewritten to the script's repo-relative path; the remaining entries
        are verbatim, so a flag the builder knows nothing about is still
        recorded.

        An empty argument list is recorded as such — that is informative,
        not absent. It distinguishes "run with no flags" from "written
        before this field existed", which is what absence means.
        """
        argv = list(sys.argv)
        try:
            rel = self._script_path.resolve().relative_to(_repo_root())
            head = str(rel)
        except Exception:
            head = self._script_path.name
        argv = [head] + argv[1:]
        return {
            "argv": argv,
            "reproduce": "python3 -u " + " ".join(argv),
        }

    def build(self) -> dict:
        """Build the witness dictionary (without writing to disk)."""
        # Difference against the clock the baseline was actually taken on.
        _now = time.time() if self._start_is_epoch else time.monotonic()
        duration_ms = int((_now - self._start_time) * 1000)
        # Backstop: a duration is never negative. If a future caller finds a
        # third way to mismatch the clocks, this records an unknown duration as
        # 0 rather than committing a negative epoch-like number that reads as
        # data to every consumer.
        duration_ms = max(duration_ms, 0)
        head_sha = _git_head_sha()
        script_sha = _git_file_sha(str(self._script_path))
        script_hash = file_content_hash(str(self._script_path))

        all_passed = all(a.passed for a in self.assertions)

        witness: dict[str, Any] = {
            # ── Structured fields (ComputationWitness interface) ──
            "engine": self.engine,
            "engineVersion": self.engine_version,
            "computedAt": datetime.now(timezone.utc).isoformat(),
            "commitSha": head_sha,
            "assertions": [a.to_dict() for a in self.assertions],
            "allPassed": all_passed,
            "durationMs": duration_ms,
            # ── Extended fields for staleness tracking ──
            "computation": self.name,
            "scriptFile": self._script_path.name,
            "scriptHash": script_hash,
            "scriptCommitSha": script_sha,
        }

        # ── Precision metadata (from qou_substrate.precision) ──────
        # Records the compute library's error floor so downstream
        # consumers know the truncation bound of every serialized value.
        try:
            from qou_substrate.precision import (
                COMPUTE_DPS, OUTPUT_DPS, PRECISION_GUARD,
            )
            witness["precisionMetadata"] = {
                "compute_dps": COMPUTE_DPS,
                "output_dps": OUTPUT_DPS,
                "guard_digits": PRECISION_GUARD,
                "truncation_bound": f"1e-{OUTPUT_DPS}",
            }
        except ImportError:
            pass

        # ── Environment / software versions ────────────────────────
        # Interpreter + numeric-library versions, so version-driven drift
        # (e.g. mpmath/sympy shifting q₀ at ~1e-8) is attributable.
        witness["environment"] = capture_environment()

        # ── Invocation ─────────────────────────────────────────────
        # WHAT this fixes: a producer can gate real compute on sys.argv,
        # and nothing in its witness said so. Measured case —
        # `whitehead_c0_mpmath.py` puts its N=12 data point behind
        # `"--n12" in sys.argv`; the committed witness CONTAINS N=12, so it
        # was made with the flag, and a plain re-run silently drops the
        # point and moves the headline `factor` 1.9678 -> 1.8973 (3.6 %).
        # The diff reads as ordinary drift. Scanned: 4 producers confirmed
        # to gate payload on an unrecorded flag (bean qou-nok3).
        #
        # This mirrors `Generation` in `tools/hecke-engine/src/provenance.rs`,
        # which already does it for the Rust binaries. Its design note argues
        # for RAW ARGV over modelled per-flag fields, because modelling needs
        # updating whenever a binary gains an option and silently drops
        # anything not yet modelled — which is the failure being fixed. The
        # same reasoning applies here, so this stores argv, not parsed flags.
        #
        # `argv[0]` is normalised to a repo-relative path so the record does
        # not depend on where the script was invoked from; without that, the
        # field would differ between machines for the same run and every
        # comparison would be noise.
        #
        # NOT ephemeral, deliberately: the point is that a re-run with
        # different flags shows up as a difference rather than hiding.
        witness["invocation"] = self._capture_invocation()

        if self.description:
            witness["description"] = self.description
        if self.content_block:
            witness["contentBlock"] = self.content_block
        if self.audit_only:
            witness["auditOnly"] = self.audit_only
        if self.parameters:
            witness["parameters"] = self.parameters
        # Surface accumulated upstream hashes in ``data`` so the drift
        # validator (witness_dependency_drift.py) can find them.  Done
        # before the ``self.data`` check so a builder that tracked
        # only upstreams (no other data) still emits the field.
        if self._upstream_hashes:
            self.data.setdefault(
                "upstream_witness_hashes", self._upstream_hashes
            )
        if self.data:
            witness["data"] = self.data
        if self.caveats:
            witness["caveats"] = self.caveats

        # Append legacy top-level keys captured by ``wrap_legacy``
        # WITHOUT overwriting structured fields above. This preserves
        # the original layout of hand-written witnesses during P30
        # migration so downstream readers that key on top-level paths
        # do not break.
        for k, v in self._extra_top_level.items():
            if k not in witness:
                witness[k] = v

        # Stamp the q₀ pin when it is POSITIVELY declared for this producer
        # (env var or an explicit `q0_anchor_manifest.json` entry). Without
        # this, `q0Anchor` is only written by producers that remember to call
        # `stamp_staleness_metadata` — 184 of ~780 — so the manifest carried no
        # weight at write time and stale pins survived on preserve-forward.
        # Undeclared producers are still left unstamped: Q0_ANCHOR_MISSING is a
        # tolerated state, and defaulting one in would assert a pin nobody
        # established.
        if "q0Anchor" not in witness:
            try:
                if q0_anchor_is_declared(self._script_path):
                    _a, _v = resolve_q0_anchor(self._script_path)
                    if _a in ("muon", "proton"):
                        witness["q0Anchor"] = _a
                        if _v is not None:
                            witness["q0Value"] = _v
            except Exception:  # noqa: BLE001
                pass

        return witness

    def save(self, extra: Optional[dict] = None) -> Path:
        """Build and write the witness JSON file. Returns the path.

        **Content-diff-aware:** if the on-disk witness already exists and
        differs from the new one ONLY in ephemeral meta fields (commitSha,
        scriptCommitSha, computedAt, durationMs), the on-disk file is
        PRESERVED unchanged. This breaks the CI drift loop (each commit
        embeds a fresh commitSha, but CI's strict-diff check would always
        fail) while keeping commitSha as a staleness audit-trail: it
        records the LAST commit that substantively changed the witness
        content, not the most recent commit that ran the validator.
        """
        witness = self.build()
        if extra:
            witness.update(extra)

        out_path = self._output_dir / f"{self.name}.witness.json"

        existing = None
        if out_path.exists():
            try:
                with open(out_path, "r", encoding="utf-8") as f:
                    existing = json.load(f)
            except (json.JSONDecodeError, OSError):
                # On-disk file unreadable: fall through and overwrite.
                existing = None

        # Carry a recorded q₀ pin forward.
        #
        # `q0Anchor`/`q0Value` are written by `stamp_staleness_metadata`, which
        # a producer has to call explicitly — 184 do, while 596 witnesses carry
        # the pin, most of it backfilled. So rebuilding a witness whose
        # producer does not stamp DROPS the pin, and 557 of those 596 are in
        # exactly that position: a value-preserving re-run that silently
        # removes the guard against reading a muon value as a proton one
        # (bean tnjb), which `audits/q0_anchor_consistency_audit.py` exists to
        # enforce.
        #
        # Preserve only. A witness with no recorded pin still gets none —
        # inventing one would assert a pin the producer never established, and
        # Q0_ANCHOR_MISSING is a tolerated state.
        # ...but NEVER across an actual re-anchoring. Carrying a stale pin is
        # strictly worse than dropping one: a dropped pin reads as
        # Q0_ANCHOR_MISSING, a tolerated state the audit reports, whereas a
        # carried one ASSERTS a layer the numbers no longer belong to — the
        # muon-value-read-as-proton confusion of bean tnjb, with a provenance
        # field vouching for it.
        #
        # TWO independent ways a carried pin can be FALSE. We drop on EITHER,
        # because neither subsumes the other (merge of two fixes that landed
        # concurrently, 2026-08-09):
        #
        #  (1) PAYLOAD EVIDENCE — the freshly computed q₀ in the payload
        #      disagrees with the recorded label. Measured:
        #      `markov_peel_atomic_witness` re-anchored to proton (its stem is
        #      NOT in `q0_anchor_manifest.json`) and the rebuilt witness still
        #      carried `q0Anchor: muon` with the muon `q0Value`, next to a
        #      proton `parameters.q0`. Being undeclared, (2) misses it.
        #  (2) DECLARED RE-ANCHORING — an env var or an explicit manifest entry
        #      contradicts the recorded label. Measured: `qbeta_ck_cache`
        #      computed at the proton pin while its witness read
        #      `q0Anchor: "muon"`; the Q_β prediction had moved 30.4 ppb under
        #      a label saying it had not. Where the payload carries no readable
        #      q₀, (1) misses it.
        #
        # (1) is payload EVIDENCE, not the resolver default, so it does NOT
        # have the failure mode that rules out gating on `resolve_q0_anchor`
        # alone: that defaults to "proton" for the ~470 producers absent from
        # the manifest, and gating on it would strip legitimate `muon` labels
        # wholesale. Reading the actual computed value does not.
        #
        # On either contradiction DROP rather than correct: writing the
        # resolved pin here would assert a stamp the producer never
        # established — the very thing the "preserve only" rule above exists to
        # prevent — and Q0_ANCHOR_MISSING is explicitly tolerated. A producer
        # that wants a positive label calls `stamp_staleness_metadata`.
        #
        # A carried-forward `independent` can go false the same way, so it gets
        # the mirror of check (1): the label says the compute never reads q₀,
        # and the payload now carries a recognisable q₀. Only payload evidence
        # applies here — (2) cannot, since `resolve_q0_anchor` never yields
        # `independent` and would "contradict" every such witness with its
        # proton default.
        if isinstance(existing, dict):
            _recorded = existing.get("q0Anchor")
            _stale = False
            if _recorded == "independent":
                _stale = _q0_anchor_from_payload(witness) is not None
            if _recorded in ("muon", "proton"):
                _actual = _q0_anchor_from_payload(witness)
                if _actual is not None and _actual != _recorded:
                    _stale = True                      # (1) payload evidence
                if not _stale:                         # (2) declared re-anchor
                    try:
                        if q0_anchor_is_declared(self._script_path):
                            _resolved, _ = resolve_q0_anchor(self._script_path)
                            _stale = (_resolved in ("muon", "proton")
                                      and _resolved != _recorded)
                    except Exception:  # noqa: BLE001
                        _stale = False
            if not _stale:
                # `q0AnchorReason` rides with the anchor it explains, and is
                # dropped with it: a reason carried past a dropped anchor would
                # explain a label that is no longer there, which is worse than
                # no reason at all.
                # `independent` and `comparison` FORBID a bare `q0Value`
                # (see the vocabulary note at the top of this module): one
                # alongside either label is a contradiction the anchor audit
                # reports as Q0_FLIP. So when the NEW witness declares one of
                # them, the old `q0Value` must not ride along -- carrying it
                # forward would manufacture exactly the contradiction the
                # declaration exists to avoid.
                #
                # Measured: declaring `q0Anchor: independent` on two producers
                # that provably do not read q0 (fitted_labelled_canonical_audit,
                # compute_audit_scan -- byte-identical output under
                # QOU_Q0_ANCHOR=muon vs =proton, differing only in the
                # q0Anchor/q0Value pair itself) still emitted the inherited
                # 50-digit MUON value next to `independent`. It went unreported
                # only because both filenames end in a suffix the anchor audit
                # exempts, so the flip check never ran on them.
                # GENERALISED 2026-08-24: `independent`/`comparison` were only
                # the visible half. A `q0Value` must not ride forward whenever
                # the NEW witness declares an anchor of ITS OWN -- muon and
                # proton included -- because the stamping block above writes
                # `q0Value` only inside `if "q0Anchor" not in payload`. A
                # producer that states its own anchor therefore arrives here
                # with no value, and this loop supplied the PREVIOUS run's.
                # When the anchor changed between runs that pairs a fresh,
                # correct label with the old label's number: a Q0_FLIP
                # manufactured by the block that exists to prevent one.
                #
                # Measured on `confinement_b3_enumeration_recheck_probe`, whose
                # committed witness came from a `QOU_Q0_ANCHOR=ideal` run: it
                # went out `q0Anchor: proton` carrying the MUON 50-dps value,
                # and `q0_anchor_consistency_audit` scored it Q0_FLIP. Neither
                # half could be caught on its own -- the producer's label was a
                # literal, so it could not disagree with itself.
                #
                # Leaving the field absent is the right failure: the anchor
                # audit's Q0_ANCHOR_MISSING is tolerated and VISIBLE, whereas
                # an inherited value is silently wrong. A producer that wants
                # both states both (see `q0_stamp.pin_value_for_anchor`).
                _forbids_value = witness.get("q0Anchor") in ("independent", "comparison")
                _declares_anchor = "q0Anchor" in witness
                for _k in ("q0Anchor", "q0Value", "q0AnchorReason"):
                    if _k == "q0Value" and _declares_anchor:
                        continue
                    if _k not in witness and _k in existing:
                        witness[_k] = existing[_k]
                if _forbids_value:
                    witness.pop("q0Value", None)

        # If an existing witness is substantively identical (ignoring
        # ephemeral meta fields), preserve it — avoids CI drift loops
        # when only commitSha/computedAt/durationMs would change.
        #
        # `environment` is one of those masked fields, which used to make
        # this branch swallow provenance in BOTH directions (bean qou-dc0n):
        #
        #   * a degraded block already on disk could not be REPAIRED. Once
        #     written, re-running with the missing libraries installed took
        #     this branch (the payload matches), so the fresh, complete block
        #     was discarded and the weak one kept. Only deleting the witness
        #     and re-running restored it.
        #   * and the guard below never ran, because this returns above it.
        #     So the degraded record went SILENT at exactly the moment it was
        #     wrong — while `_check_environment_regression` was telling the
        #     agent to "install it and re-run", which did nothing.
        #
        # So ask the environment question here too. Only a strictly STRONGER
        # block writes; a weaker one still preserves (never degrade a file we
        # were not otherwise rewriting) but now says so.
        if isinstance(existing, dict) and _witnesses_substantively_equal(
                existing, witness):
            _env_repair = _environment_is_repair(
                existing.get("environment"), witness.get("environment"))
            if not _env_repair:
                # Weaker or lateral. Keep the file; warn only if weaker.
                _check_environment_regression(
                    witness, existing, out_path.name, preserved=True)
                # Re-print the assertion summary for the validator runner
                # without re-writing the file.
                print(f"✓ Witness: {out_path.name}  "
                      f"({len(self.assertions)} assertions, "
                      f"{'all passed' if witness['allPassed'] else 'FAILURES'}) "
                      f"[unchanged — kept on-disk commitSha for staleness]")
                return out_path
            # Strictly stronger: fall through and write, so the recovered
            # provenance lands. The numbers are unchanged by construction —
            # this branch is only reachable when the payload already matched.
            print(f"↑ environment: {out_path.name}: recording a STRONGER "
                  f"environment block than the copy on disk; rewriting "
                  f"provenance only (payload unchanged).", file=sys.stderr)

        _check_producer_takeover(existing, witness, out_path)

        _check_raw_float64(witness, out_path.name)
        _check_nonfinite(witness, out_path.name)
        _check_environment_regression(witness, existing, out_path.name)

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(witness, f, indent=2, ensure_ascii=False, default=str)
            f.write("\n")

        print(f"✓ Witness: {out_path.name}  "
              f"({len(self.assertions)} assertions, "
              f"{'all passed' if witness['allPassed'] else 'FAILURES'})")

        return out_path


# Ephemeral meta fields that change on every validator run regardless of
# whether the substantive content drifted. Masked in the equality check
# so the on-disk witness is preserved when only these would change.
# Ephemeral meta fields — stripped before the "substantively equal"
# comparison in `_witnesses_substantively_equal`, so on-disk witnesses
# are PRESERVED when only these fields would change. Rationale:
#
#   - commitSha, scriptCommitSha — change on every commit; would
#     trigger CI drift loops if comparison were exact
#   - computedAt, durationMs — wall-clock metadata; not numeric content
#   - durationSeconds, duration_sec — the seconds-valued spellings of
#     durationMs. `durationMs` (integer ms) is the WitnessBuilder
#     convention and is overwhelmingly the majority (2423 witness JSONs
#     vs 3 + 2 for these two), but the seconds spellings exist and
#     carry identical wall-clock semantics, so they are masked too
#     rather than left to be compared as substantive content.
#
#     Spelling note — there is NO `durationSec` in this corpus. That
#     name appears only in prose (a producer comment, and bean
#     qou-pg2r, which took the shorthand from it); as a JSON key it
#     occurs zero times. Masking the string "durationSec" would be a
#     silent no-op. The real keys are the two above; measure with
#     `grep -rl '"<key>"' --include=*.json .` before adding another.
#   - environment — Python + numeric-library versions; tracked for
#     attribution (see `capture_environment` docstring above) but a
#     runtime swap alone (e.g. 3.11.15 ↔ 3.12.3) shouldn't trigger
#     rewrites of otherwise-identical witnesses
#   - elapsed_seconds, elapsed_sec — per-item timing metrics buried
#     in `data` payloads; same rationale as durationMs
#
# The fields are RECURSIVELY stripped — `elapsed_seconds` nested
# inside `data.computations[...].elapsed_seconds` is caught too.
#
# Collision-risk note: the recursive mask strips ANY dict key with
# these names regardless of where it appears in the witness JSON. If
# a producer ever emits a substantive payload field named
# `elapsed_seconds` or `elapsed_sec` whose value carries numeric
# content (not timing metadata), it will be incidentally masked and
# could cause false substantive-equality matches. Mitigation:
# producers should prefix non-timing fields with a domain qualifier
# (e.g. `decay_seconds`, `physical_elapsed_s`) rather than reusing
# `elapsed_seconds`. The masked names are reserved for runtime-
# metadata semantics across the witness corpus.
#
# Sync note: mirrored in `qou-mass/src/qou_mass/_internal/witness_base.py`
# (PyPI bundle copy). The cross-package sync is asserted by the
# `test_ephemeral_mask_sync` test in `tools/qou-substrate/tests/`.
#: Set to a non-empty value to allow a producer takeover that would otherwise
#: be refused. This is the deliberate-ownership-transfer escape hatch — use it
#: when a witness is genuinely moving to a new producer AND the field loss is
#: intended, and say so in the commit.
_TAKEOVER_OVERRIDE_ENV = "QOU_WITNESS_ALLOW_PRODUCER_TAKEOVER"


def _top_level_data_keys(w: object) -> set:
    """Top-level keys plus `data.*` keys — the shape a consumer reads.

    Nested payload keys are deliberately NOT walked: per-partition tables and
    result lists legitimately change shape run to run, and comparing them would
    make the guard fire on ordinary recomputation.
    """
    if not isinstance(w, dict):
        return set()
    keys = {k for k in w if k not in _EPHEMERAL_META_FIELDS}
    data = w.get("data")
    if isinstance(data, dict):
        keys |= {f"data.{k}" for k in data}
    return keys


def _check_producer_takeover(existing: object, witness: dict,
                             out_path: "Path") -> None:
    """Refuse to let a DIFFERENT producer silently overwrite a poorer witness.

    The failure this exists for (bean `qou-okl8`): two producers emitted the
    same witness name with different schemas —
    `per_irrep_pole_atom.py` writes `f"per-irrep-pole-{atom}-h{n}"`, which for
    the deuteron is exactly the literal `per_irrep_pole_deuteron_h6.py` writes.
    Whichever ran last won. Running the atom-specific one over the committed
    atom-produced witness deleted `cemetery_class_signed_power_projection`,
    `net_signed_power`, `is_pure_power_in_cemetery` and the per-`gen_idx`
    breakdown — 230 deletions against 39 insertions — with no warning of any
    kind. It was caught by eye in a diff; nothing in the pipeline objected.

    **Why this keys on OWNERSHIP CHANGE and not on field loss.** The obvious
    guard is "refuse to shrink a witness", and it is the wrong one: ordinary
    schema evolution drops fields all the time, so a shrink-guard would fire
    constantly on legitimate work and be silenced. Ownership change is the
    actual signal — `scriptFile` is already recorded on every witness, so the
    comparison is free and near-zero-false-positive. Both conditions must hold:

      * a *different* `scriptFile` is writing this name, AND
      * the incoming payload *lacks* keys the on-disk one has.

    A different producer writing an equal-or-richer witness is a legitimate
    consolidation and passes with a note. The same producer dropping a field is
    schema evolution and is not this function's business.

    Scope, measured rather than assumed: a scan of every `WitnessBuilder(...)`
    name in `computations/` found **zero** literal-vs-literal collisions and
    exactly **two** template-vs-literal ones, both this same
    generalised-supersedes-specific shape (`per-irrep-pole-deuteron-h6` and
    `per-irrep-pole-proton-h3`). So this guard is a backstop for a small,
    bounded family — not a widespread class — and it is written to stay quiet.

    Raises RuntimeError unless `QOU_WITNESS_ALLOW_PRODUCER_TAKEOVER` is set.
    """
    if not isinstance(existing, dict):
        return
    old_script = existing.get("scriptFile")
    new_script = witness.get("scriptFile")
    if not isinstance(old_script, str) or not isinstance(new_script, str):
        return

    # Compare BASENAMES. `save()` writes `self._script_path.name`, but 32
    # committed witnesses carry a path-qualified `scriptFile`
    # (`computations/foo.py`, `markov/bar.py`) from older producers — and 29 of
    # those resolve to a file that still exists. Comparing the raw strings
    # would read every one of them as a producer change on its next run, which
    # is how a guard like this earns a reputation for crying wolf and gets
    # switched off. Measured before the first commit, not after a bug report.
    if PurePath(old_script).name == PurePath(new_script).name:
        return

    lost = sorted(_top_level_data_keys(existing) - _top_level_data_keys(witness))
    if not lost:
        print(f"  note: {out_path.name} changed producer "
              f"{old_script} -> {new_script}; no fields lost.")
        return

    if os.environ.get(_TAKEOVER_OVERRIDE_ENV):
        print(f"  ⚠ {out_path.name}: producer takeover "
              f"{old_script} -> {new_script} DROPS {len(lost)} field(s): "
              f"{', '.join(lost)} — allowed by "
              f"{_TAKEOVER_OVERRIDE_ENV}.")
        return

    raise RuntimeError(
        f"REFUSING to overwrite {out_path.name}: it was written by "
        f"{old_script!r}, this run is {new_script!r}, and the new payload "
        f"drops {len(lost)} field(s) the committed one carries: "
        f"{', '.join(lost)}.\n"
        f"Two producers are writing the same witness name with different "
        f"schemas (bean qou-okl8). Either run the owning producer "
        f"({old_script}), or give this one a distinct witness name. If this "
        f"IS a deliberate ownership transfer and the field loss is intended, "
        f"re-run with {_TAKEOVER_OVERRIDE_ENV}=1 and say so in the commit."
    )


_EPHEMERAL_META_FIELDS = frozenset({
    "commitSha", "scriptCommitSha", "computedAt", "durationMs",
    "durationSeconds", "duration_sec",
    "environment", "elapsed_seconds", "elapsed_sec",
})


def _strip_ephemeral_fields(d: object) -> object:
    """Recursively strip the ephemeral-meta fields from a witness dict.
    Returns a new structure suitable for substantive-equality comparison."""
    if isinstance(d, dict):
        return {k: _strip_ephemeral_fields(v) for k, v in d.items()
                if k not in _EPHEMERAL_META_FIELDS}
    if isinstance(d, list):
        return [_strip_ephemeral_fields(item) for item in d]
    return d


def _witnesses_substantively_equal(a: dict, b: dict) -> bool:
    """True iff `a` and `b` are equal after masking ephemeral meta fields.

    Substantive content includes: assertions, allPassed, computation,
    description, data payload (minus per-item timing), parameters,
    scriptFile, scriptHash, engineVersion. Ephemeral (masked):
    commitSha, scriptCommitSha, computedAt, durationMs, durationSeconds,
    duration_sec, environment, elapsed_seconds, elapsed_sec.

    Python-version swaps + per-item timing differences alone don't
    trigger witness rewrites of otherwise-identical numeric content.
    The fields stay IN the saved witness (for attribution / staleness
    audit trails) but are stripped BEFORE the substantive-equality
    comparison.

    See the `_EPHEMERAL_META_FIELDS` definition above for the
    per-field rationale and the recursive-mask collision-risk note.
    """
    return _strip_ephemeral_fields(a) == _strip_ephemeral_fields(b)


# ── Staleness checker ────────────────────────────────────────────

def check_witness_staleness(witness_path: str) -> dict:
    """
    Check if a witness JSON is stale relative to its script.

    Returns dict with:
      stale: bool
      reason: str (if stale)
      scriptHash: current vs recorded
      commitSha: current vs recorded
    """
    with open(witness_path, "r") as f:
        witness = json.load(f)

    result: dict[str, Any] = {
        "witnessFile": os.path.basename(witness_path),
        "stale": False,
    }

    # Check script hash
    script_file = witness.get("scriptFile")
    if script_file:
        script_path = os.path.join(os.path.dirname(witness_path), script_file)
        if os.path.exists(script_path):
            current_hash = file_content_hash(script_path)
            recorded_hash = witness.get("scriptHash")
            result["currentScriptHash"] = current_hash
            result["recordedScriptHash"] = recorded_hash
            if recorded_hash and current_hash != recorded_hash:
                result["stale"] = True
                result["reason"] = "script content changed since witness"
                return result

    # Check commit SHA (informational, not staleness)
    #
    # The commit SHA records WHEN the witness was generated, but doesn't
    # determine staleness. A new commit that doesn't touch the script
    # doesn't invalidate the witness. The scriptHash check above is the
    # authoritative staleness signal — if the script content is unchanged,
    # the witness is still valid regardless of intervening commits.
    commit_sha = witness.get("commitSha")
    if commit_sha and commit_sha != "unknown":
        current_head = _git_head_sha()
        result["currentCommitSha"] = current_head
        result["recordedCommitSha"] = commit_sha

    return result


# ── CLI ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Witness infrastructure utilities")
    sub = parser.add_subparsers(dest="command")

    # check-stale
    cs = sub.add_parser("check-stale", help="Check if a witness is stale")
    cs.add_argument("witness_file", help="Path to .witness.json")

    # check-all
    ca = sub.add_parser("check-all", help="Check all witnesses for staleness")

    args = parser.parse_args()

    if args.command == "check-stale":
        result = check_witness_staleness(args.witness_file)
        print(json.dumps(result, indent=2))
        sys.exit(1 if result["stale"] else 0)

    elif args.command == "check-all":
        comp_dir = Path(__file__).resolve().parent
        witnesses = sorted(comp_dir.glob("*.witness.json"))
        stale_count = 0
        for wf in witnesses:
            result = check_witness_staleness(str(wf))
            icon = "🔄" if result["stale"] else "✓"
            reason = f" — {result['reason']}" if result.get("reason") else ""
            print(f"  {icon} {wf.name}{reason}")
            if result["stale"]:
                stale_count += 1
        print(f"\n{len(witnesses) - stale_count} current, {stale_count} stale — {len(witnesses)} total")

    else:
        parser.print_help()
