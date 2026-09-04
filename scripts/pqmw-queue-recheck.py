#!/usr/bin/env python3
"""Re-measure and TRIAGE bean `qou-pqmw`'s 78 bare-projection entries.

The bean's list is a snapshot taken 2026-08-10.  Draining it entry-by-entry
without re-checking writes disclosures onto declarations that have since been
fixed, moved or deleted -- `core-levi-form.lean` is the worked case: all three
of its entries are stale, because `6c17f7203d` (2026-08-31, bean `qou-z9ws`)
had already rewritten the file to the data-as-parameters shape.

Buckets, by whether the entry still RESOLVES (not whether it is still a defect):

  file-gone      the path no longer exists
  decl-gone      the file exists, the declaration name is not in it
  moved          resolves, at a different line than the bean records
  same-line      resolves, exactly where the bean records

`decl-gone` means "no longer resolves by name" -- a rename and a deletion look
identical here, and separating them needs `git log -S`, which this does not do.

Beyond resolving, each surviving entry is triaged on INHABITATION: does the
class it projects have an instance anywhere in `content/`?  Per
`docs/audits/2026-08-09-inhabitation-is-a-weak-discriminator.md` that is
**necessary, not sufficient** -- a reflexive-diagonal or trivial-index instance
inhabits without saying anything -- so `inhabited` means "needs a human read",
never "legit".  `uninhabited` is the decisive direction: the class is in the
honest 3b-tax open state, so the projection is the disclosure shape.

Worked case for why this column exists: all four `QHookBound.lean` entries are
non-defects.  Two no longer resolve; the other two project
`QIntRatioBoundSmall` and `QFactRatioBound`, which have THREE and FOUR
`nlinarith`-proved instances for the concrete `m`/`k` the file uses.  Draining
that sub-cluster "together", as the bean suggests, would have written a
"derives nothing" disclosure onto two proved bundles.

Usage:  python3 scripts/pqmw-queue-recheck.py [--json OUT]
"""
import re, sys, json, pathlib

DECL = r"(?:private[ \t]+)?(?:noncomputable[ \t]+)?(?:theorem|lemma|def|abbrev|instance)"

# The class a declaration projects, from its `[inst : C ...]` binder.
#
# Two corrections, both from wrong output rather than from reading the regex:
# (1) take the LAST bracket binder, not the first -- a declaration written
#     `{C : Type} [Category C] [inst : Foo C]` otherwise reports `Category`,
#     and the first run of this script attributed six entries to `CommRing`
#     and `CategoryTheory.Category`, which are not conjecture carriers;
# (2) require each dotted segment to start uppercase, so the capture cannot
#     end on a `.` -- the same run emitted `Category.` and `CommRing`.
BINDER = re.compile(
    r"\[\s*(?:[A-Za-z_][A-Za-z0-9_']*\s*:\s*)?"
    r"([A-Z][A-Za-z0-9_']*(?:\.[A-Z][A-Za-z0-9_']*)*)")

# Mathlib structure classes that are never the conjecture carrier.
_AMBIENT = {"CommRing", "Ring", "Field", "AddCommGroup", "Module", "Fintype",
            "DecidableEq", "Category", "CategoryTheory", "MonoidalCategory",
            "Nontrivial", "LinearOrderedField", "TopologicalSpace", "Algebra",
            "CommMonoid", "AddCommMonoid", "Monoid", "Group", "Inhabited"}

# The carrier column is a HEURISTIC -- "last bracket binder that is not on the
# ambient list".  It is right for a conventionally-written declaration and can
# be wrong for an unusual binder order, and the ambient list is hand-kept, so a
# Mathlib class not on it will be reported as a carrier.  Treat the column as a
# pointer to read, never as a verdict.


def _carrier(sig: str):
    """Last bracket binder that is not an ambient Mathlib class."""
    names = [m.group(1) for m in BINDER.finditer(sig)]
    names = [n for n in names if n.split(".")[-1] not in _AMBIENT
             and n.split(".")[0] not in _AMBIENT
             # a bare single capital is a type variable (`R`, `C`, `M`), not a
             # carrier -- `descent_surjective` reported `R` before this guard
             and len(n.split(".")[-1]) > 1]
    return names[-1] if names else None
_INHAB_CACHE: dict = {}


def _sig_of(block: str) -> str:
    """Signature = text up to `:=` or `where`."""
    cuts = [block.find(t) for t in (":=", "where") if block.find(t) != -1]
    return block[:min(cuts)] if cuts else block


def _decl_blocks(src: str):
    """(keyword, signature) for each top-level declaration.  Instances put the
    class on a LATER line than the `instance` keyword routinely, so a
    single-line grep misses them -- making that mistake is why this exists."""
    starts = list(re.finditer(rf"^[ \t]*({DECL})[ \t]+", src, re.M))
    for i, m in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(src)
        yield m.group(1).split()[-1], _sig_of(src[m.start():end])


# --- the decisive column: is the proof term a BARE PROJECTION? ---
#
# Neither "still resolves" nor "class is uninhabited" decides whether an entry
# is a defect.  `q_bkm_criterion` is uninhabited AND is not a projection: it
# composes TWO fields into an iff (`⟨ctx.bkm_necessity, ctx.bkm_continuation⟩`),
# which AGENTS.md §3b-cond names as the VERIFIED EXEMPLAR of the pattern working.
# The discriminator is the Aug-30 one -- derives vs projects -- so test the proof
# term directly: a bare projection's term is one field access, optionally applied
# to the theorem's own binders, and nothing else.
_NOT_BARE = ("⟨", "by ", "by\n", "fun ", "λ", "Iff.", "And.", "· ", "<|", "$")


def proof_is_bare_projection(block: str) -> bool | None:
    """None when the term cannot be isolated (tactic block, or no `:=`)."""
    i = block.find(":=")
    if i == -1:
        return None
    term = block[i + 2:].strip()
    if not term:
        return None
    term = term.split("\n\n")[0].strip()
    if any(t in term for t in _NOT_BARE):
        return False
    head = term.split()[0] if term.split() else ""
    return "." in head and head[0].isalpha()


def class_has_refutation(cls: str, path: str) -> bool:
    """Is there a companion `theorem … : ¬ C …` in the same file?

    A parametrised carrier with a proved refutation is a GATE, not a defect:
    `_forward` extracts the bound and `_reject` shows the class is uninhabitable
    when the bound fails, so the projection is the gate's intended API.  Four of
    the nine "drain" entries are this shape.

    Searched over the WHOLE signature block.  A first version looked one line
    past the `theorem` keyword and returned NONE for all nine -- including
    `mass_anchor_stable_reject`, whose `¬ MassAnchorStableGateClass` is on the
    THIRD line.  That zero was caught only because the file had been read first."""
    src = pathlib.Path(path).read_text(errors="replace")
    pat = re.compile(rf"¬\s*\(?\s*{re.escape(cls.split('.')[-1])}\b")
    return any(kw in ("theorem", "lemma") and pat.search(sig)
               for kw, sig in _decl_blocks(src))


def class_is_inhabited(cls: str, root: pathlib.Path) -> bool:
    """Does any `instance` in the tree declare `cls` in its signature?"""
    if cls in _INHAB_CACHE:
        return _INHAB_CACHE[cls]
    base = cls.split(".")[-1]
    pat = re.compile(rf"\b{re.escape(base)}\b")
    found = False
    for f in root.rglob("*.lean"):
        if ".lake" in f.parts:
            continue
        src = f.read_text(errors="replace")
        if not pat.search(src):
            continue
        if any(kw == "instance" and pat.search(sig) for kw, sig in _decl_blocks(src)):
            found = True
            break
    _INHAB_CACHE[cls] = found
    return found

def main() -> int:
    beans = sorted(pathlib.Path('.beans').glob('qou-pqmw--*.md'))
    if not beans:
        print("bean qou-pqmw not found", file=sys.stderr); return 2
    rows = re.findall(r"^- `([^`]+):(\d+)` — `([^`]+)`", beans[0].read_text(), re.M)
    if not rows:
        print("no entries parsed -- the bean's list format changed", file=sys.stderr); return 2

    out = {"file_gone": [], "decl_gone": [], "moved": [], "same_line": []}
    for path, line, decl in rows:
        p = pathlib.Path(path)
        if not p.exists():
            out["file_gone"].append({"decl": decl, "path": path}); continue
        s = p.read_text(errors='replace')
        base = decl.split('.')[-1]
        m = re.search(rf"^[ \t]*{DECL}[ \t]+{re.escape(base)}\b", s, re.M)
        if not m:
            out["decl_gone"].append({"decl": decl, "path": path}); continue
        now = s[:m.start()].count('\n') + 1
        cls = _carrier(_sig_of(s[m.start():m.start() + 1200]))
        rec = {"decl": decl, "path": path, "bean_line": int(line), "now_line": now,
               "class": cls}
        if cls:
            rec["class_inhabited"] = class_is_inhabited(cls, pathlib.Path("content"))
        if cls:
            rec["class_refuted"] = class_has_refutation(cls, path)
        nxt = re.search(rf"^[ \t]*{DECL}[ \t]+", s[m.end():], re.M)
        blk = s[m.start(): m.end() + (nxt.start() if nxt else 4000)]
        rec["bare_projection"] = proof_is_bare_projection(blk)
        out["moved" if now != int(line) else "same_line"].append(rec)

    tot = len(rows)
    unresolved = len(out["file_gone"]) + len(out["decl_gone"])
    print(f"entries in the bean : {tot}")
    for k in ("file_gone", "decl_gone", "moved", "same_line"):
        print(f"  {k:12s}: {len(out[k])}")
    print(f"\nNO LONGER RESOLVES  : {unresolved} / {tot} ({100*unresolved/tot:.0f} %)")
    print(f"still at bean's line: {len(out['same_line'])}")

    live = out["moved"] + out["same_line"]
    inh = [r for r in live if r.get("class_inhabited")]
    uninh = [r for r in live if r.get("class_inhabited") is False]
    noclass = [r for r in live if r.get("class") is None]
    print(f"\nof the {len(live)} that still resolve:")
    print(f"  class INHABITED  : {len(inh):3d}   necessary-not-sufficient; needs a human read")
    print(f"  class uninhabited: {len(uninh):3d}   honest open state -> the disclosure shape")
    print(f"  no carrier binder: {len(noclass):3d}   only ambient Mathlib classes, or none")
    if inh:
        print("\n  --- INHABITED (do NOT blanket-disclose these) ---")
        for r in sorted(inh, key=lambda r: r["decl"]):
            print(f"    {r['decl']:42s} {r['class']}")

    bare = [r for r in live if r.get("bare_projection") is True]
    notbare = [r for r in live if r.get("bare_projection") is False]
    unk = [r for r in live if r.get("bare_projection") is None]
    print(f"\nDECISIVE COLUMN -- is the proof term a BARE PROJECTION?")
    print(f"  bare projection  : {len(bare):3d}   conclusion IS one field -> the real queue")
    print(f"  derives          : {len(notbare):3d}   composes/uses fields -> NOT a defect")
    print(f"  term not isolable: {len(unk):3d}   tactic block or no `:=`; needs a read")
    # The two columns CUT ACROSS each other, and the intersection is the queue.
    #   bare + inhabited   -> the bundle is built, so the accessor is the
    #                         ordinary Mathlib idiom (Aug-09: legit/advisory)
    #   bare + uninhabited -> honest open state AND a restatement: the disclosure
    #   derives            -> not a projection at all, whatever the inhabitation
    drain = [r for r in bare if r.get("class_inhabited") is False
             and not r.get("class_refuted")]
    gates = [r for r in bare if r.get("class_inhabited") is False
             and r.get("class_refuted")]
    legit = [r for r in bare if r.get("class_inhabited") is True]
    print(f"\n  bare AND uninhabited : {len(drain):3d}  <-- THE DRAIN QUEUE")
    print(f"  bare but inhabited   : {len(legit):3d}      bundle is built; Aug-09 legit/advisory")
    print(f"  bare, has refutation : {len(gates):3d}      a working GATE, not a defect")
    print("\n  --- THE DRAIN QUEUE ---")
    for r in sorted(drain, key=lambda r: r["path"]):
        print(f"    {r['decl']:42s} {str(r['class']):32s} {r['path'].split('/')[-1]}")

    if "--json" in sys.argv:
        dest = sys.argv[sys.argv.index("--json") + 1]
        json.dump(out, open(dest, "w"), indent=1)
        print(f"\nwrote {dest}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
