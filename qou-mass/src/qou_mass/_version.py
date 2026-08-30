"""Single source of truth for the qou-mass package version.

⚠ This is NOT currently the single source of truth, despite the line above
saying so. `pyproject.toml` carries a STATIC `version = ...` at [project],
not a `dynamic = ["version"]` declaration, so the two must be edited
together or the built wheel reports a different version from
`qou_mass.__version__`. They were already out of step in spirit — this file
said "single source of truth" while pyproject pinned its own copy. Either
keep them in sync by hand (current state) or switch pyproject to
`dynamic = ["version"]` with a setuptools `attr:` pointer here.

Bumping requires:

  1. Update __version__ here.
  2. Run `python -m build` to produce sdist + wheel under dist/.
  3. Tag v$(__version__) on the qou-mass repo (or paper repo until extracted).
  4. CHANGELOG.md gets a new section describing the bump.

SemVer convention (see qou-mass-architecture-plan §6):
  - MAJOR: any witness JSON byte-for-byte change (modulo timestamps),
    any removed/renamed public symbol, any default change.
  - MINOR: new public symbols, new optional kwargs, new observables.
  - PATCH: bug fixes, perf, docs.
"""

__version__ = "1.0.0"
