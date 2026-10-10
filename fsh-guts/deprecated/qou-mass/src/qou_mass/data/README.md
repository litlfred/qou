# Deprecated: unreachable witness copies

These files are **not loaded at runtime and never were**.

The vendored modules under `_internal/` resolve their witness paths relative to
`Path(__file__).resolve().parent.parent`, which inside the package is
`_internal/` -> `qou_mass/`. So a witness must sit in the **package root** to be
found; a copy under `data/` raises `FileNotFoundError` if anything tries to load
it. `scripts/sync-qou-mass-vendor.py` documents this in its `WITNESS_DEST`
header.

Each file here duplicated a name that already exists in the package root. The
root copy is the live one and is kept in sync by
`scripts/sync-qou-mass-vendor.py --apply`; these were not, so they silently
aged. Two had drifted about a month behind their root twin by 2026-08-22:

    q-pinning-50-digit.witness.json       root 2026-08-21  here 2026-07-18
    atomic-tr-m-mpfr-50dps.witness.json   root 2026-08-19  here 2026-08-10

`q-pinning-50-digit` is the substrate modulus record, so the package carried two
versions of q₀ a month apart — inert, but readable by a human who would have no
way to know which was live.

Retained rather than deleted: removing a shipped file is an API decision, and
the sync script takes the same posture with its `orphans` report. `_deprecated`
is excluded from the sync and from the coverage counts, matching
`computations/_deprecated/` and `docs/audits/_deprecated/`.

**Do not add files here to silence a coverage warning.** If a witness belongs in
the package, it belongs in the root where the resolver looks.

Bean: `qou-cdj8`.
