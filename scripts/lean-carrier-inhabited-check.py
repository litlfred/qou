#!/usr/bin/env python3
"""Is the bundle a projection projects from ever BUILT?

The discriminator the vacuity review ledger already uses, and the sharpest one
available for a self-assuming projection (AGENTS.md §3b-cond item 5):

    "A projection like this is the legitimate Mathlib accessor idiom ONLY when
     something builds the bundle."

An accessor on an inhabited structure exposes an axiom of a thing that exists.
An accessor on an UNINHABITED one exposes an axiom of a thing nobody has ever
produced -- the theorem is then conditional on a hypothesis with no witness,
which is honest §3b-cond only if the block says so.

MULTI-LINE, AND THAT IS THE WHOLE POINT.  A line-anchored grep

    grep -E "^\\s*(instance|def)[^:]*:\\s*Bundle\\b"

reports ZERO for `SkeinMultisetInvariant`, which has an instance -- because
this corpus writes

    instance skeinMultisetInvariant_refl (config : NuclearConfig)
        (h_same : config.length = config.length)
        (h_perm : ...) :
        SkeinMultisetInvariant config config h_same h_perm :=
      ⟨rfl⟩

with the keyword on line 1 and the result type on line 4.  That false zero was
measured on this corpus before this script existed, and it points the wrong
way: it reports a carrier as UNINHABITED, which is the finding-shaped answer.

`--selftest` requires the four carriers known to be inhabited to be found.
It exists because the first version of this check passed nothing and reported
a clean sweep of zeros.

SECOND BLIND SPOT, MEASURED 2026-09-07: IT SCANNED `content/` ONLY.

`builders()` defaulted to `root="content"`, so a witness anywhere else was
invisible and the carrier read as UNINHABITED -- the finding-shaped answer
again, exactly like the line-anchored bug above.

That is not hypothetical.  Measured over the 58 distinct classes behind the
corpus's flagged self-assuming projections: 18 are built inside `content/`,
29 have no builder anywhere, and **11 are built ONLY outside it** -- all of
them in three audit probes that, by their own headers, have no imports and are
imported by nothing:

    docs/audits/2026-08-30-context-classes-hand-adjudicated.lean   7
    docs/audits/2026-08-30-gate-classes-admit-zero.lean            3
    docs/audits/2026-08-31-h2s-and-the-inert-radius-gate.lean      1

`BarEvenKernel` was a twelfth and was moved into `content/` on 2026-09-07
(PR #7125), which is why it no longer appears in that list.

SO THE FIX IS TO REPORT *WHERE*, NOT TO WIDEN THE SEARCH SILENTLY.

Scanning everything and printing one count would be worse than the bug, and
the reason is `2026-08-30-gate-classes-admit-zero.lean`: its instances are
`DirectionSanityGateClass 0`, `MassAnchorStableGateClass 0`,
`HasFiniteLPDuality emptyLP`, `HasMarkovTrace probeParticle 0`.  Those were
built to show the gates ADMIT ZERO -- a demonstration that they are too weak,
a negative result.  Counting them as "the bundle is built" would convert a
negative result into a certificate of health, which is the laundering AGENTS.md
§"Axiomatization is NOT a Proof" forbids.

A probe witness answers "is this satisfiable at all"; a witness at the class
answers "may a reader treat these projections as accessors".  They are
different questions, so the output labels which one it found and never merges
the counts.  `--probes` opts into the wider scan.

Usage:
  scripts/lean-carrier-inhabited-check.py <Carrier> [<Carrier> ...]
  scripts/lean-carrier-inhabited-check.py --probes <Carrier> [...]
  scripts/lean-carrier-inhabited-check.py --selftest
"""
from __future__ import annotations
import re, sys, pathlib

DECL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|protected\s+|private\s+)*"
                  r"(instance|def|abbrev|example)\b")

# Known inhabited on this corpus; a run that finds none of these is measuring
# itself.  `FiberAdjointInvolutionContext` is deliberately NOT here -- it is
# genuinely uninhabited and its docstring says why.
SELFTEST = ["SkeinMultisetInvariant", "HasStrongDuality",
            "QIntRatioBoundSmall", "Term7ShellCorrectionClass"]


def builders(carrier: str, root: str = "folio") -> list[str]:
    out = []
    pat = re.compile(rf"(?<![.\w]){re.escape(carrier)}(?![\w])")
    for p in pathlib.Path(root).rglob("*.lean"):
        lines = p.read_text(errors="ignore").split("\n")
        for i, l in enumerate(lines):
            if not DECL.match(l):
                continue
            j = i + 1
            while j < len(lines) and (lines[j].startswith((" ", "\t")) or not lines[j].strip()):
                j += 1
            body = "\n".join(lines[i:j])
            m = re.search(r":=", body)
            sig = body[:m.start()] if m else body
            # the RESULT type is what follows the final top-level colon; a
            # carrier merely passed as an argument does not count as building one
            if pat.search(sig.rsplit(":", 1)[-1]):
                out.append(f"{p}:{i+1}  {l.strip()[:70]}")
    return out


# Trees that are NOT the shipped formalization: probe / audit fragments which
# by their own headers have no imports and are imported by nothing.  A witness
# here is evidence of satisfiability, not of accessor legitimacy.
PROBE_ROOTS = ["docs", "scripts/lean"]


def main() -> int:
    args = sys.argv[1:]
    probes = "--probes" in args
    args = [a for a in args if a != "--probes"]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--selftest":
        bad = [c for c in SELFTEST if not builders(c)]
        if bad:
            print("SELFTEST FAIL — these are inhabited and were not found:", ", ".join(bad))
            print("The scanner is reporting about itself, not about the corpus.")
            return 1
        print(f"SELFTEST OK — all {len(SELFTEST)} known-inhabited carriers found")
        return 0
    if builders(SELFTEST[0]) == []:
        print("REFUSING: the built-in control is not found; run --selftest", file=sys.stderr)
        return 2
    worst = 0
    for c in args:
        b = builders(c)
        pb = []
        if probes:
            for r in PROBE_ROOTS:
                if pathlib.Path(r).is_dir():
                    pb += builders(c, r)
        if b:
            note = ""
        elif pb:
            note = ("   <-- PROBE-ONLY: satisfiable, but every witness is in a "
                    "fragment nothing imports; see the docstring before treating "
                    "this as accessor legitimacy")
        else:
            note = "   <-- UNINHABITED: not the accessor idiom"
        print(f"{len(b):>2}  {c}{note}")
        for h in b[:3]:
            print(f"      {h}")
        for h in pb[:3]:
            print(f"      [probe] {h}")
        worst = max(worst, 0 if b else 1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
