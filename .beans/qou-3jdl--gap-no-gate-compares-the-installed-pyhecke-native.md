---
# qou-3jdl
title: 'GAP: no gate compares the installed pyhecke_native wheel against the source it was built from — __version__ provably cannot detect it'
status: todo
type: task
priority: normal
created_at: 2026-09-08T08:24:28Z
updated_at: 2026-09-08T08:25:04Z
---

Split out of `qou-nm6y` on 2026-09-08, which is being closed: its *container's*
stale wheel is resolved, but the durable fix it recommends does not exist and the
class has now fired **three times**.

## The recommendation this carries, verbatim from `qou-nm6y`

> *"No gate compares the installed native wheel against the source it was built
> from. A stale wheel produces plausible numbers from stale mathematics, and
> every ratchet reads those as ordinary values. … Worth a version/commit stamp on
> the wheel, checked at import, so a producer using native code against a
> mismatched build fails loudly instead of quietly computing the wrong thing."*

## MEASURED: `__version__` cannot serve as that stamp

This is the part `qou-nm6y` asserted and did not demonstrate. Measured today:

| | value |
|---|---|
| `tools/pyhecke-native/Cargo.toml` | `version = "0.9.0"` |
| `tools/pyhecke-native/pyproject.toml` | `version = "0.9.0"` |
| installed `pyhecke_native.__version__` | `0.9.0` |
| last source change under `tools/pyhecke-native/` | **`096f0d89b9b`, 2026-08-31** |
| last commit touching `version` in `Cargo.toml` | **`b831ff34c3d`, 2026-08-29** |

**The version did not move when the source did.** A wheel built before
2026-08-31 and one built after both report `0.9.0`, so the only stamp currently
exposed is provably blind to the exact drift this gap is about.

And the 08-31 change is not cosmetic — its subject is *"the binding path's
seminormal matrices are NOT a representation of `H_n(q)`"*. A stale wheel there
computes different mathematics under an identical version string, in the binding
path.

The module exposes nothing else usable: `dir(pyhecke_native)` yields
`__version__` and function names (`build_atom_nf`, …) — no build commit, no
source hash.

## The class has fired THREE times and been closed per-incident each time

| bean | status | what fired |
|---|---|---|
| `qou-j6il` | **completed** | *"TRAP (critical): installed `pyhecke_native` .so is STALE and returns convention C — any producer run silently reintroduces C"* |
| `qou-nm6y` | closing now | a 2026-08-09 wheel still exporting `gram_inverse`, deleted from source 2026-08-15; a producer was receiving a 6×6 "inverse" of a singular form |
| — | — | this bean: the gate that would have caught both |

Each was diagnosed correctly and fixed **in one container**. None left anything
behind that would catch the next one. That is the same shape `qou-oyde` named for
the 0-byte witness on the same day: *"an instruction to the AGENT instead of a fix
to the PRODUCER"* — and, as there, three days later it fired again.

## Why the two existing signals do not cover it

- **`WitnessBuilder.capture_environment`** records `pyhecke-native` version in a
  witness's `environment` block — but it records `0.9.0`, so two witnesses
  computed from different mathematics carry an identical, reassuring stamp.
- **The try/except around the native call** makes it worse, as `qou-nm6y`
  observed: on a correct machine the removal is silently swallowed, so **neither**
  configuration announces itself.

## Next honest step

1. Emit a **build stamp** from the build (`scripts/build-pyhecke-native.sh`) —
   the source commit sha of `tools/pyhecke-native/` at build time — and expose it
   as e.g. `pyhecke_native.__build_commit__`.
2. Check it at import in `tools/pyhecke/python/pyhecke/` against the working
   tree's current sha for that directory, and **fail loudly** on mismatch rather
   than warn.
3. Decide deliberately whether the check is fatal or a warning: a bare container
   is the default here (`pyhecke_native` is **not on PyPI**), so a fatal check
   must not fire when the extension is simply absent — only when it is *present
   and mismatched*.

**Not attempted here**, and not exempt under the 2026-09-07 ask-first override:
adding an import-time failure path is a contract change on every consumer of
`pyhecke`, which is the same reason `qou-li9a`'s exit-code change was left for
the owner. Measure the consumer set first.
