---
# qou-7q0a
title: wall-side-statement verdicts are not predicted by banner presence — 5 live fails need re-adjudication, oldest 2026-07-07
status: todo
type: task
priority: normal
created_at: 2026-09-03T04:42:32Z
updated_at: 2026-09-03T04:43:08Z
---

MEASURED 2026-09-03 on main d502ed06ce9 (+ this branch).

I added a rendered wall banner to nuclear-interactions/skein-binding-lagrangian.md
on the premise that wall-side-statement fails a block whose archimedean constructs
lack a rendered §7c banner (the block's banner was in authorNotes, which §4d says
does not render). THAT PREMISE IS NOT SUPPORTED. Measured over every block with
archimedean tokens in its .md AND a wall-side-statement verdict (n=17):

    verdict x md_banner:  pass/no-banner 11 | fail/no-banner 4
                          pass/banner     1 | fail/banner    1

ELEVEN blocks pass with no rendered banner, so a rendered banner is not what the
criterion keys on. And the single fail-with-banner is skein-binding-lagrangian
itself, AFTER my edit -- my block is now the only one failing while having the
thing I added to fix it.

Nor is it chapter-determined: mass-theory contains both passes and fails.

WHAT IS ACTUALLY TRUE. wall-side-statement is automated:false -- a per-block agent
judgement. qa-sweep marks agent criteria needs-agent but does NOT re-adjudicate an
existing entry, so a verdict persists until an agent replaces it. The five live
fails and their ages:

    knots-particles-confinement/magic-shell-coupling-kappa
    mass-theory/terminal-resolution
    mass-theory/neutron-proton-splitting
    nuclear-interactions/skein-binding-lagrangian      (2026-07-07, gemini-3.1-pro)
    nuclear-interactions/tritium-qvalue-symbolic

Each carries its own field_hash, and skein-binding's (4e4a3af31905) matches neither
the live .md nor the pre-edit one -- so it is provably stale, adjudicated against a
version of the text older than either.

WHAT IS OPEN. These five need an agent re-adjudication against their current text.
NOT by me for skein-binding: I edited that block, so clearing its fail is the one
verdict I should not be the one to write.

WHAT IS NOT WRONG. The banner addition itself stands on its own merits -- the block
now declares its wall side in the rendered narrative, matching the verbatim house
wording in mobius-energy.md / surreal-squeeze.md / mi-sw-abelianisation.md. It is
just not a fix for this criterion, and the PR must not claim it is.
